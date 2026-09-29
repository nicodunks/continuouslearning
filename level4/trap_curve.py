"""trap_curve.py  -  does a training grade reward a half-working memory over spinning?  (29 Sept, no training)
Brains: the hand-built fly brain with its stored home vector rotated by a random angle per fly, uniform in
[-theta, theta]; theta = 0 is a perfect memory, theta = 180 deg is no memory (random direction). Plus a spinner and a
brain that never steers. For each, three grades on the cold training world (30 s):
  last10  : mean distance over the last 10 s of the return (the grade used so far)
  closest : closest approach (the exam's score)
  progress: distance at the end of the return minus distance at the turn (negative = got closer)
A grade has the trap if some partial memory scores WORSE than spinning."""
import sys, math, json, torch
sys.path.insert(0, '../level3'); torch.set_num_threads(1)
import world
from handbrain import HandBrain, COLS
from world import run_episode

from handbrain import TONIC
from world import DT, W_MAX
class Rotated(HandBrain):
    """The hand brain, but the home vector it steers by is rotated by a random angle per fly (uniform in
    [-theta, theta]): the memory is wrong by that angle, the compass and steering are true."""
    def __init__(self, theta): super().__init__(); self.theta = theta
    def reset_fast(self, b):
        super().reset_fast(b); self.off = (torch.rand(b) * 2 - 1) * self.theta
    def step(self, inp, active):
        cos_h, sin_h, speed, food = inp[:, 0], inp[:, 1], inp[:, 2], inp[:, 3]
        hd = torch.atan2(sin_h, cos_h)
        cells = torch.clamp(torch.cos(COLS[None, :] - hd[:, None]), min=0.0)
        self.W = self.W + (DT * speed[:, None] * cells) * active[:, None]
        self.W = self.W * torch.where(food > 0, 0.0, 1.0)[:, None]
        self.W = torch.minimum(self.W, torch.tensor(W_MAX))
        ax = (self.W * torch.cos(COLS)).sum(1); ay = (self.W * torch.sin(COLS)).sum(1)
        home = torch.atan2(-ay, -ax) + self.off                       # true way home, rotated by this fly's error
        turn = 3.0 * torch.sin(home - hd)
        z = torch.zeros_like(speed); return turn, speed, z
class Const:
    def __init__(s, t): s.t = t
    def reset_fast(s, b): s.b = b
    def reset_activity(s): pass
    def step(s, inp, active=None): z = torch.zeros(s.b); return torch.full((s.b,), s.t), z, z

def grades(brain, n=1000):
    ds = []; orig = world.run_episode
    with torch.no_grad():
        r = run_episode(brain, batch=n, t_out=30, trips=1, seed=11, food_stand=2.0, record=False)
    return r

# need distance at turn and at end: re-run with a light hook on the world is not available, so measure via two episodes:
def measure(brain):
    import types
    out = {}
    with torch.no_grad():
        r = run_episode(brain, batch=1000, t_out=30, trips=1, seed=11, food_stand=2.0)
    out['last10'] = float(r['loss']); out['closest'] = r['score']
    return out
rows = []
for name, b in [('never steers', Const(0.)), ('spins', Const(7.8))] + [(f'memory off by up to {d} deg', Rotated(math.radians(d))) for d in (0, 30, 60, 90, 120, 150, 180)]:
    m = measure(b); rows.append(dict(name=name, **m)); print(f"{name:32s} last10 {m['last10']:6.2f}   closest {m['closest']:5.2f}")
json.dump(rows, open('trap_curve.json', 'w'), indent=1)
