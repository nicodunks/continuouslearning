"""nets.py  –  level 4: the rivals.  Our fast-weight network (FW) is level3/flynet.py, unchanged.

TWIN   FW's twin: the same 64 neurons, inputs, table W, outputs and tanh, with the fast-weight board
       (F and its allowance A) removed and a hold gate added instead.  Each tick:
           proposal = tanh(W_in · input + W · x_old)          (exactly FW's update, minus the A∘F term)
           u        = sigmoid(U · x_old + V · input + b)      (the hold gate, one per neuron)
           x_new    = (1 − u) · x_old + u · proposal
       u near 0 holds the neuron's value exactly (a loop gain of 1); u near 1 is FW's plain update.
       This is the single-gate form of a GRU.  The write and erase outputs are kept so the world and the
       loss are identical, but they are wired to nothing: the gates are reported as zero.
GRURef A textbook GRU with 52 memory units, sized to match FW's parameter count.  Reference only.

Both keep FW's interface: reset_fast(batch), reset_activity(), step(inp, active) -> (turn, write, erase),
and a zero_F flag that does nothing (they have no F), so level 3's trainer and tests run them unchanged.
"""
import os, sys, torch, torch.nn as nn
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'level3'))
from flynet import FlyNet, TURN_MAX


class TwinNet(nn.Module):
    def __init__(self, n=64, gate_bias=0.0, gate_init='random'):
        super().__init__()
        self.n = n; self.zero_F = False
        self.W_in = nn.Linear(4, n)                            # same as FW
        self.W = nn.Parameter(0.1 * torch.randn(n, n))         # same as FW
        self.W_out = nn.Linear(n, 3)                           # same as FW: turn, (write), (erase)
        self.U = nn.Parameter(0.1 * torch.randn(n, n) if gate_init == 'random' else torch.zeros(n, n))
        self.V = nn.Linear(4, n)                               # hold gate from the inputs
        with torch.no_grad():
            if gate_init != 'random': self.V.weight.zero_()
            self.V.bias.fill_(gate_bias)

    @classmethod
    def from_fw(cls, fw_state):
        """Surgery: copy W_in, W, W_out from a trained FW; drop A, F and ws; add a hold gate that starts
        open (u = sigmoid(3) = 0.95 for every neuron, whatever the input), so the first tick is FW's
        update with its memory removed, plus a 5% hold."""
        n = fw_state['W'].shape[0]
        net = cls(n=n, gate_bias=3.0, gate_init='zero')
        own = net.state_dict()
        for k in ('W_in.weight', 'W_in.bias', 'W', 'W_out.weight', 'W_out.bias'): own[k] = fw_state[k].clone()
        net.load_state_dict(own); return net

    def reset_fast(self, batch): self.batch = batch; self.F = torch.zeros(1)
    def reset_activity(self): self.x = torch.zeros(self.batch, self.n)

    def step(self, inp, active=None):
        x_old = self.x
        proposal = torch.tanh(self.W_in(inp) + x_old @ self.W.t())
        u = torch.sigmoid(x_old @ self.U.t() + self.V(inp))
        x = (1 - u) * x_old + u * proposal
        out = self.W_out(x)
        turn = TURN_MAX * torch.tanh(out[:, 0] / TURN_MAX)
        if active is not None:
            x = active[:, None].float() * x + (1 - active[:, None].float()) * x_old
        self.x = x; self.u = u
        z = torch.zeros(self.batch)
        return turn, z, z

    def n_params(self): return sum(p.numel() for p in self.parameters() if p.requires_grad)


class GRURef(nn.Module):
    def __init__(self, h=52):
        super().__init__()
        self.h = h; self.zero_F = False
        self.cell = nn.GRUCell(4, h); self.out = nn.Linear(h, 1)

    def reset_fast(self, batch): self.batch = batch; self.F = torch.zeros(1)
    def reset_activity(self): self.x = torch.zeros(self.batch, self.h)

    def step(self, inp, active=None):
        x_old = self.x
        x = self.cell(inp, x_old)
        turn = TURN_MAX * torch.tanh(self.out(x)[:, 0] / TURN_MAX)
        if active is not None:
            x = active[:, None].float() * x + (1 - active[:, None].float()) * x_old
        self.x = x
        z = torch.zeros(self.batch)
        return turn, z, z

    def n_params(self): return sum(p.numel() for p in self.parameters() if p.requires_grad)


def build(arch, ckpt_args=None):
    a = ckpt_args or {}
    if arch.startswith(('fw_', 'kvq_')) or arch in ('mamba', 'transformer'):          # round 6 designs
        import frontier as fr
        if arch.startswith('fw_'): return fr.FWRule(rule=arch[3:], erase_rows=bool(a.get('erase_rows', 0)), direct_read=bool(a.get('direct_read', 0)))
        if arch.startswith('kvq_'): return fr.KVQNet(rule=arch[4:])
        return fr.MambaNet() if arch == 'mamba' else fr.TinyTransformer()
    if arch == 'fw': return FlyNet(n=int(a.get('neurons', 64)), use_fast=True, f_max=float(a.get('f_max', 1.0)), rule=a.get('rule', 'hebb'))
    if arch == 'twin': return TwinNet(n=int(a.get('neurons', 64)))
    if arch == 'gru': return GRURef()
    raise ValueError(arch)


def load(path):
    """Any checkpoint from level 3 or level 4 -> a frozen network ready for the exam."""
    ck = torch.load(path); a = ck.get('args', {}); arch = a.get('arch', 'fw')
    net = build(arch, a); sd = {k: v for k, v in ck['net'].items() if not k.startswith('aux.')}   # the diagnostic readout is not used at exam time
    net.load_state_dict(sd); net.eval(); return net
