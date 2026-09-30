"""slope.py  -  after round 6: measure the ground training stands on at birth (the landscape of section 8, with real numbers).
For an untrained network, walk a little way in two directions and record the grade training feels (the loss: distance from
home over the last 10 s of the return; lower is better):
  steer: add eps x (the best straight-line readout of the ideal turn, sin(direction home - heading), from the network's own
         untrained activity) to its turn, in radians per second.  This is 'start using the memory the network already has'.
  spin : add a constant turn sigma (radians per second).  This is 'turn harder', which needs no memory.
10 s wander, 2 trips, 500 flies; readout fitted on seed 11, loss measured on seed 4242 (the same flies for every step).
    python3 level4/slope.py  -> level4/slope.json"""
import sys, os, json, math, torch
torch.set_num_threads(4)
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'level3'))
from nets import build, TwinNet
from flynet import FlyNet, TURN_MAX
from world import run_episode, DT
from dial_probe import twin_k
KT = 100

def wrap(net, fn):
    st0 = net.step
    def h(inp, active=None):
        k = h.k; h.k += 1
        turn, w, e = st0(inp, active)
        step = inp[:, 2:3] * inp[:, 0:2] * DT
        h.v = step if h.v is None else h.v + step
        if k % (3 * KT) == 0 and k > 0: pass
        return fn(k, inp, turn, h.v), w, e
    h.k = 0; h.v = None; net.step = h
    return st0

def fit_readout(net):
    xs, ys = [], []
    def fn(k, inp, turn, v):
        kk = k % (3 * KT)
        if kk == 0: wrap.v0 = v.clone()
        if KT <= kk < KT + 30:
            hv = v - wrap.v0; hd = torch.atan2(inp[:, 1], inp[:, 0]); hdir = torch.atan2(-hv[:, 1], -hv[:, 0])
            xs.append(net.x.clone()); ys.append(torch.sin(hdir - hd))
        return turn
    st0 = wrap(net, fn)
    with torch.no_grad(): run_episode(net, batch=500, t_out=10, trips=1, seed=11, food_stand=2.0)
    net.step = st0
    X = torch.cat(xs); Y = torch.cat(ys)[:, None]
    A = torch.cat([X, torch.ones(len(X), 1)], 1)
    W = torch.linalg.solve(A.T @ A + 1e-2 * torch.eye(A.shape[1]), A.T @ Y)
    P = A @ W; r2 = float(1 - ((P - Y) ** 2).sum() / ((Y - Y.mean()) ** 2).sum())
    return W[:, 0], r2

def loss_with(net, W, eps=0.0, sigma=0.0):
    def fn(k, inp, turn, v):
        s = torch.cat([net.x, torch.ones(len(net.x), 1)], 1) @ W
        return (turn + eps * s + sigma).clamp(-TURN_MAX, TURN_MAX)
    st0 = wrap(net, fn)
    with torch.no_grad(): r = run_episode(net, batch=500, t_out=10, trips=2, seed=4242, food_stand=2.0, erase_penalty=0.05)
    net.step = st0
    return round(float(r['loss']), 3), round(r['score'], 3)

def fwe():
    n = FlyNet()
    with torch.no_grad(): n.ws.fill_(0.0)
    return n
DESIGNS = [('Our board', FlyNet), ('Our board, empty at birth', fwe), ('Transformer', lambda: build('transformer')),
           ('Twin', TwinNet), ('Twin + 4 counters', lambda: twin_k(4)), ('Twin + 16 counters', lambda: twin_k(16)),
           ('Keys and values + lid', lambda: build('kvq_hebbl')), ('Keys and values + lid, running-sum start', lambda: build('kvq_hebblc3')),
           ('Mamba', lambda: build('mamba')), ('Gated DeltaNet', lambda: build('kvq_gdelta'))]
EPS = [0, 1, 2, 4, 8]; SIG = [0, 1, 2, 4, 8]
if __name__ == '__main__':
    out = {}
    for name, mk in DESIGNS:
        rows = []
        for seed in (0, 1):
            torch.manual_seed(seed); net = mk().eval()
            W, r2 = fit_readout(net)
            steer = [loss_with(net, W, eps=e) for e in EPS]; spin = [loss_with(net, W, sigma=s) for s in SIG]
            rows.append(dict(seed=seed, readout_r2=round(r2, 3), steer=steer, spin=spin))
        out[name] = rows; print(name, rows, flush=True)
        json.dump(out, open(os.path.join(HERE, 'slope.json'), 'w'), indent=1)
