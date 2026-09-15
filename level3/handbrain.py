"""handbrain.py  –  the level 1 fly brain written in torch, with the fly's settings.  Used only to
check that the torch world is the same game as the numpy one (it should score about 0.6 at 30 s)."""
import math, torch
from world import DT, W_MAX

N = 8
COLS = torch.arange(N) * 2 * math.pi / N
TONIC = 0.3


class HandBrain:
    def __init__(self, write=1.0, erase=1.0, rot=180.0, gain=3.0):
        self.p = dict(write=write, erase=erase, rot=math.radians(rot), gain=gain)
    def reset_fast(self, batch): self.W = torch.zeros(batch, N)
    def reset_activity(self): pass
    def step(self, inp, active):
        cos_h, sin_h, speed, food = inp[:, 0], inp[:, 1], inp[:, 2], inp[:, 3]
        hd = torch.atan2(sin_h, cos_h)
        cells = torch.clamp(torch.cos(COLS[None, :] - hd[:, None]), min=0.0)
        wsig = speed                                                     # write scales with speed
        self.W = self.W + (DT * self.p['write'] * wsig[:, None] * cells) * active[:, None]
        self.W = self.W * torch.where(food > 0, 1 - self.p['erase'], 1.0)[:, None]
        self.W = torch.minimum(self.W, torch.tensor(W_MAX))
        act = self.W * (cells + TONIC)
        ax = (act * torch.cos(COLS)).sum(1); ay = (act * torch.sin(COLS)).sum(1)
        r = self.p['rot']; rx = ax * math.cos(r) - ay * math.sin(r); ry = ax * math.sin(r) + ay * math.cos(r)
        clean = torch.hypot(rx, ry) / (act.sum(1) + 1e-9)
        turn = self.p['gain'] * torch.sin(torch.atan2(ry, rx) - hd) * torch.clamp(2 * clean, max=1.0)
        return turn, wsig, torch.where(food > 0, torch.full_like(food, self.p['erase']), torch.zeros_like(food))
