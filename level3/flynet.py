"""flynet.py  –  our own model.  No compass columns, no tally board.  64 neurons, all connected, and a
rule that lets connections change while the network runs.

Three kinds of numbers, three clocks:
  slow   W_in, W, A, W_out, ws     set by training, then frozen.  The rulebook.  ~8,700 numbers.
  fast   F  [batch, N, N]          zero at the start of an episode; changed every tick by the rule;
                                   never trained; carried across the two trips of an episode.
  activity  x [batch, N]           changes every tick; reset to zero at the start of each trip.

Effective strength of the connection j -> i  =  W[i,j] + A[i,j] * F[i,j]
Rule, every tick:  F = (1 - erase) * F + ws * write * outer(x_new, x_old),  clamped to ±1.
write and erase are the network's own outputs (sigmoids), so it decides when to rewrite itself.

Flags for the tests:
  use_fast=False   A is zero and frozen -> brain B / the level 4 rival (memory can only be activity)
  zero_F=True      F is forced to zero every tick at test time -> "F held at zero"
"""
import torch, torch.nn as nn

N = 64
TURN_MAX = 8.0     # radians per second; a smooth ceiling on the turn output


class FlyNet(nn.Module):
    def __init__(self, n=N, use_fast=True):
        super().__init__()
        self.n = n; self.use_fast = use_fast; self.zero_F = False
        self.W_in = nn.Linear(4, n)                            # 4 inputs -> neurons (weights + biases)
        self.W = nn.Parameter(0.1 * torch.randn(n, n))         # slow strengths, j -> i
        self.A = nn.Parameter(0.1 * torch.randn(n, n))         # how much each connection's fast strength counts
        self.W_out = nn.Linear(n, 3)                           # neurons -> turn, write gate, erase gate
        self.ws = nn.Parameter(torch.tensor(0.1))              # write strength inside the rule (level 1's write dial)
        with torch.no_grad():                                  # gates start mostly closed, like an LSTM forget bias:
            self.W_out.bias[1] = 1.0                           #   write ~0.73 open
            self.W_out.bias[2] = -5.0                          #   erase ~0.007 per tick, so F can accumulate at all
        if not use_fast:
            self.A.requires_grad_(False); self.A.zero_()

    def reset_fast(self, batch):
        self.F = torch.zeros(batch, self.n, self.n); self.batch = batch

    def reset_activity(self):
        self.x = torch.zeros(self.batch, self.n)

    def step(self, inp, active=None):
        x_old = self.x
        eff = self.W + self.A * self.F                                       # [batch, N, N]
        recurrent = torch.bmm(eff, x_old.unsqueeze(2)).squeeze(2)
        x = torch.tanh(self.W_in(inp) + recurrent)
        out = self.W_out(x)
        turn = TURN_MAX * torch.tanh(out[:, 0] / TURN_MAX)
        write = torch.sigmoid(out[:, 1]); erase = torch.sigmoid(out[:, 2])
        hebb = x.unsqueeze(2) * x_old.unsqueeze(1)                           # outer(x_new, x_old)
        F = (1 - erase[:, None, None]) * self.F + self.ws * write[:, None, None] * hebb
        F = F.clamp(-1, 1)
        if active is not None:                                               # frozen agents: nothing changes
            m = active[:, None, None].float(); F = m * F + (1 - m) * self.F
            x = active[:, None].float() * x + (1 - active[:, None].float()) * x_old
        if self.zero_F: F = torch.zeros_like(F)
        self.F = F; self.x = x
        return turn, write, erase

    def n_params(self): return sum(p.numel() for p in self.parameters() if p.requires_grad)
