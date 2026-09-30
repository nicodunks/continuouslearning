"""frontier.py  -  round 6: the fly's task as a test bed for the memories used at the frontier of sequence models.

Every design shares FW's skeleton (level3/flynet.py): 64 neurons, x_new = tanh(W_in u + W x_old + read), outputs
turn / write / erase from W_out.  Only the MEMORY changes: what is stored, and the rule that rewrites it.

Fast-weight (matrix) memories, rewritten every tick:
  FWRule(rule)    FW's own board F (64 x 64), key = activity a tick ago, value = activity now (tied), read = (A o F) x
                  rule 'blend': per-tick gate beta chooses between add (beta=0, Hebb) and add-the-surprise (beta=1, delta)
                  rule 'deltan': delta with the key scaled to length 1 (plain tied delta is unstable: ws*w*|x|^2 ~ 2.3 > 2)
                  rule 'deltanA': deltan with A starting at 1, so the value carries the board's read and delta can count
  KVQNet(rule)    a 16 x 16 table S with SEPARATE learned key, value, query (linear attention / Mamba-2 / DeltaNet form)
                  rule 'hebb'   S = (1-e) S + w v k^T                   gated linear attention, Mamba-2
                       'hebbl'  same, with FW's write strength (0.1) and lid (+-1)   (added after the first E2 results)
                       'gdelta' S = (1-e) S + w (v - S k) k^T           Gated DeltaNet
                       'delta'  S = S + w (v - S k) k^T                 DeltaNet (no forget gate)
                       'titans' M = eta M + (1-eta) w (v - S k) k^T ; S = (1-e) S + M   Titans-style surprise with momentum
Vector (activity-style) memories:
  MambaNet        Mamba-1 style selective state space: per neuron 16 decaying numbers, decay and write set by the input
  (TwinNet, GRURef in nets.py)
Softmax attention (keeps every past step, no fixed-size memory):
  TinyTransformer one causal attention layer (2 heads, width 32) over the trip so far, with fixed sine-wave position codes
All small, single-layer versions of each design's MEMORY RULE, not the full architectures.
"""
import math, os, sys, torch, torch.nn as nn
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'level3'))
from flynet import FlyNet, TURN_MAX


class FWRule(FlyNet):
    """FW with a choice of rule. 'hebb' = FlyNet exactly. 'delta' = FlyNet's delta. 'blend' adds a 4th output, beta.
    Optional extras for the score push: per-neuron forget (erase_rows) and a direct read path to the turn (direct_read)."""
    def __init__(self, rule='hebb', erase_rows=False, direct_read=False, beta_bias=-3.0, **kw):
        super().__init__(rule='hebb' if rule in ('blend', 'deltan', 'deltanA') else rule, **kw)
        if rule == 'deltanA':                        # the board's read flows fully into the value, so delta can count
            with torch.no_grad(): self.A.fill_(1.0)
        self.rule2 = rule; self.erase_rows = erase_rows; self.direct_read = direct_read
        if rule == 'blend':                          # beta = clamp(W x + b, 0, 1), starting at exactly 0 (pure Hebb):
            self.beta = nn.Linear(self.n, 1)         # even beta = 0.05 breaks a trained FW (run 41: 1.49 -> 5.50)
            with torch.no_grad(): self.beta.weight.zero_(); self.beta.bias.zero_()
        if erase_rows: self.erase_row_bias = nn.Parameter(torch.zeros(self.n))
        if direct_read:
            self.read_out = nn.Linear(self.n, 1)
            with torch.no_grad(): self.read_out.weight.zero_(); self.read_out.bias.zero_()
        self.beta_log = []

    def step(self, inp, active=None):
        x_old = self.x
        readv = torch.bmm(self.A * self.F, x_old.unsqueeze(2)).squeeze(2)
        x = torch.tanh(self.W_in(inp) + x_old @ self.W.t() + readv)
        out = self.W_out(x)
        turn_raw = out[:, 0] + (self.read_out(readv)[:, 0] if self.direct_read else 0.0)
        turn = TURN_MAX * torch.tanh(turn_raw / TURN_MAX)
        write = torch.sigmoid(out[:, 1]); e_lin = out[:, 2]
        if self.erase_rows: erase = torch.sigmoid(e_lin[:, None] + self.erase_row_bias[None, :])[:, :, None]   # [b, n, 1]
        else: erase = torch.sigmoid(e_lin)[:, None, None]
        if self.rule2 == 'blend':
            beta = self.beta(x)[:, 0].clamp(0.0, 1.0); self.last_beta = beta
            pred = torch.bmm(self.F, x_old.unsqueeze(2)).squeeze(2)
            hebb = (x - beta[:, None] * pred).unsqueeze(2) * x_old.unsqueeze(1)
        elif self.rule2 in ('deltan', 'deltanA'):    # delta with the key scaled to length 1 (stable: step x |k|^2 < 2)
            kx = x_old / (x_old.norm(dim=1, keepdim=True) + 1e-6)
            pred = torch.bmm(self.F, kx.unsqueeze(2)).squeeze(2)
            hebb = (x - pred).unsqueeze(2) * kx.unsqueeze(1)
        elif self.rule == 'delta':
            pred = torch.bmm(self.F, x_old.unsqueeze(2)).squeeze(2)
            hebb = (x - pred).unsqueeze(2) * x_old.unsqueeze(1)
        else:
            hebb = x.unsqueeze(2) * x_old.unsqueeze(1)
        F = (1 - erase) * self.F + self.ws * write[:, None, None] * hebb
        F = F.clamp(-self.f_max, self.f_max)
        if active is not None:
            m = active[:, None, None].float(); F = m * F + (1 - m) * self.F
            x = active[:, None].float() * x + (1 - active[:, None].float()) * x_old
        if self.zero_F: F = torch.zeros_like(F)
        self.F = F; self.x = x
        return turn, write, erase.mean((1, 2)) if erase.dim() == 3 else erase

    @classmethod
    def from_fw(cls, sd, **kw):
        net = cls(**kw); own = net.state_dict()
        for k, v in sd.items():
            if k in own and own[k].shape == v.shape: own[k] = v.clone()
        net.load_state_dict(own); return net


class KVQNet(nn.Module):
    def __init__(self, rule='hebb', n=64, d=16):
        super().__init__()
        self.n, self.d, self.rule = n, d, rule; self.zero_F = False
        self.W_in = nn.Linear(4, n); self.W = nn.Parameter(0.1 * torch.randn(n, n)); self.W_out = nn.Linear(n, 3)
        self.Wk = nn.Linear(n, d, bias=False); self.Wv = nn.Linear(n, d, bias=False); self.Wq = nn.Linear(n, d, bias=False)
        self.Wr = nn.Linear(d, n, bias=False)
        if rule == 'titans': self.eta_raw = nn.Parameter(torch.tensor(2.0))      # momentum eta = sigmoid(2) = 0.88
        if rule == 'hebbl': self.ws = nn.Parameter(torch.tensor(0.1))            # round 6 exploration: FW's own safeguards
        with torch.no_grad(): self.W_out.bias[1] = 1.0; self.W_out.bias[2] = -5.0

    def reset_fast(self, batch):
        self.batch = batch; self.S = torch.zeros(batch, self.d, self.d); self.M = torch.zeros(batch, self.d, self.d)
        self.F = self.S
    def reset_activity(self): self.x = torch.zeros(self.batch, self.n)

    def step(self, inp, active=None):
        x_old = self.x
        q = self.Wq(x_old); q = q / (q.norm(dim=1, keepdim=True) + 1e-6)
        readv = self.Wr(torch.bmm(self.S, q.unsqueeze(2)).squeeze(2))
        x = torch.tanh(self.W_in(inp) + x_old @ self.W.t() + readv)
        out = self.W_out(x)
        turn = TURN_MAX * torch.tanh(out[:, 0] / TURN_MAX)
        write = torch.sigmoid(out[:, 1]); erase = torch.sigmoid(out[:, 2])
        k = self.Wk(x_old); k = k / (k.norm(dim=1, keepdim=True) + 1e-6); v = self.Wv(x)
        w = write[:, None, None]; e = erase[:, None, None]
        if self.rule == 'hebb': S = (1 - e) * self.S + w * v.unsqueeze(2) * k.unsqueeze(1); M = self.M
        elif self.rule == 'hebbl':                                   # add rule with FW's write strength and lid (+-1)
            S = ((1 - e) * self.S + self.ws * w * v.unsqueeze(2) * k.unsqueeze(1)).clamp(-1, 1); M = self.M
        else:
            err = v - torch.bmm(self.S, k.unsqueeze(2)).squeeze(2)
            G = err.unsqueeze(2) * k.unsqueeze(1)
            if self.rule == 'gdelta': S = (1 - e) * self.S + w * G; M = self.M
            elif self.rule == 'delta': S = self.S + w * G; M = self.M
            else:
                eta = torch.sigmoid(self.eta_raw)                      # momentum as an average, so the effective step stays w
                M = eta * self.M + (1 - eta) * w * G                   # (plain eta M + w G explodes: step ~ w / (1 - eta) = 6)
                S = (1 - e) * self.S + M
        if active is not None:
            m = active[:, None, None].float(); S = m * S + (1 - m) * self.S; M = m * M + (1 - m) * self.M
            x = active[:, None].float() * x + (1 - active[:, None].float()) * x_old
        if self.zero_F: S = torch.zeros_like(S)
        self.S, self.M, self.x = S, M, x; self.F = S
        return turn, write, erase


class MambaNet(nn.Module):
    """Mamba-1 style selective SSM inside FW's skeleton. Each neuron c has a state h_c of N=16 numbers:
       h_c <- exp(delta_c(u) * A_c) * h_c + delta_c(u) * B(u) * z_c,   y_c = C(u) . h_c,   x_c = tanh(y_c + D_c z_c)
    with z = W_in u + W x_old. delta, B, C depend on the current input u (the 'selection'); A_c < 0 is learned."""
    def __init__(self, n=64, N=16):
        super().__init__()
        self.n, self.N = n, N; self.zero_F = False
        self.W_in = nn.Linear(4, n); self.W = nn.Parameter(0.1 * torch.randn(n, n)); self.W_out = nn.Linear(n, 3)
        self.W_delta = nn.Linear(4, n); self.W_B = nn.Linear(4 + n, N); self.W_C = nn.Linear(4 + n, N)
        self.A_log = nn.Parameter(torch.log(torch.arange(1, N + 1).float()).repeat(n, 1))     # S4D-real init
        self.D = nn.Parameter(torch.ones(n))
        with torch.no_grad(): self.W_delta.bias.fill_(math.log(math.expm1(0.1)))            # delta starts ~0.1
    def reset_fast(self, batch): self.batch = batch; self.h = torch.zeros(batch, self.n, self.N); self.F = torch.zeros(1)
    def reset_activity(self): self.x = torch.zeros(self.batch, self.n)
    def step(self, inp, active=None):
        x_old = self.x
        z = self.W_in(inp) + x_old @ self.W.t()
        dt = nn.functional.softplus(self.W_delta(inp))                       # [b, n]
        A = -torch.exp(self.A_log)                                           # [n, N]
        dA = torch.exp(dt[:, :, None] * A[None])                             # [b, n, N]
        ux = torch.cat([inp, x_old], 1); Bu = self.W_B(ux); Cu = self.W_C(ux)  # [b, N], selected by input and activity
        h = dA * self.h + dt[:, :, None] * Bu[:, None, :] * z[:, :, None]
        y = (h * Cu[:, None, :]).sum(2)
        x = torch.tanh(y + self.D * z)
        out = self.W_out(x); turn = TURN_MAX * torch.tanh(out[:, 0] / TURN_MAX)
        if active is not None:
            m = active[:, None, None].float(); h = m * h + (1 - m) * self.h
            x = active[:, None].float() * x + (1 - active[:, None].float()) * x_old
        self.h, self.x = h, x; self.state = h
        zz = torch.zeros(self.batch); return turn, zz, zz


class TinyTransformer(nn.Module):
    """One causal softmax-attention layer over every tick of the current trip so far (context wiped at each trip start,
    like activity). Token = embedding of the 4 inputs + a learned position embedding (up to 2,700 ticks)."""
    def __init__(self, d=32, heads=2, ff=64, max_len=2700):
        super().__init__()
        self.d, self.h = d, heads; self.zero_F = False
        self.emb = nn.Linear(4, d)
        pos = torch.arange(max_len).float()[:, None]; div = torch.exp(torch.arange(0, d, 2).float() * (-math.log(10000.0) / d))
        pe = torch.zeros(max_len, d); pe[:, 0::2] = torch.sin(pos * div); pe[:, 1::2] = torch.cos(pos * div)
        self.register_buffer('pe', pe)                                       # fixed sine-wave positions, no parameters
        self.Wq = nn.Linear(d, d); self.Wk = nn.Linear(d, d); self.Wv = nn.Linear(d, d); self.Wo = nn.Linear(d, d)
        self.ln1 = nn.LayerNorm(d); self.ln2 = nn.LayerNorm(d)
        self.ff = nn.Sequential(nn.Linear(d, ff), nn.GELU(), nn.Linear(ff, d)); self.out = nn.Linear(d, 1)
    def reset_fast(self, batch): self.batch = batch; self.F = torch.zeros(1)
    def reset_activity(self): self.K, self.V, self.t = [], [], 0; self.x = torch.zeros(self.batch, self.d)
    def step(self, inp, active=None):
        t = min(self.t, self.pe.shape[0] - 1)
        e = self.emb(inp) + self.pe[t][None]
        a = self.ln1(e); hd = self.d // self.h
        q = self.Wq(a).view(-1, self.h, hd); self.K.append(self.Wk(a).view(-1, self.h, hd)); self.V.append(self.Wv(a).view(-1, self.h, hd))
        K = torch.stack(self.K, 2); V = torch.stack(self.V, 2)               # [b, h, t, hd]
        att = torch.softmax((K * q[:, :, None, :]).sum(3) / math.sqrt(hd), dim=2)
        o = (att[..., None] * V).sum(2).reshape(-1, self.d)
        x = e + self.Wo(o); x = x + self.ff(self.ln2(x))
        turn = TURN_MAX * torch.tanh(self.out(x)[:, 0] / TURN_MAX)
        self.x = x; self.t += 1
        zz = torch.zeros(self.batch); return turn, zz, zz


def n_params(net): return sum(p.numel() for p in net.parameters() if p.requires_grad)
