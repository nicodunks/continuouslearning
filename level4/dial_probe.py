"""dial_probe.py  -  after round 6, Path 1 (the dial): set the birth signal on purpose and measure it before training.
Transformer: query and key weights x s at birth (s = 1 normal; larger s = sharper, less even attention).
Twin: k of its neurons wired by hand as heading counters (k = 0 plain twin, 16 = round 5's head start).
Birth signal = R^2 of the unit home direction read linearly from activity at 10 s (as reach.py), 1,200 flies, seeds 0-2.
    python3 level4/dial_probe.py  -> level4/dial_probe.json"""
import sys, os, json, math, torch
torch.set_num_threads(8)
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'level3'))
from nets import build, TwinNet
from world import run_episode
from reach import points_home

def twin_k(k):
    t = TwinNet()
    with torch.no_grad():
        for i in range(k):
            ph = 2 * math.pi * i / k
            t.W_in.weight[i] = torch.tensor([math.cos(ph), math.sin(ph), 0., 0.]); t.W_in.bias[i] = 0
            t.W[i] = 0; t.U[i] = 0; t.V.weight[i] = 0; t.V.bias[i] = -5.3
    return t
def tf_s(s):
    n = build('transformer')
    with torch.no_grad(): n.Wq.weight.mul_(s); n.Wk.weight.mul_(s)
    return n
if __name__ == '__main__':
    out = {}
    for name, mk in [(f'transformer_s{s}', (lambda s=s: tf_s(s))) for s in (1, 3, 6, 12, 25)] + [(f'twin_k{k}', (lambda k=k: twin_k(k))) for k in (0, 2, 4, 8, 16)]:
        rs = []
        for seed in (0, 1, 2):
            torch.manual_seed(seed); rs.append(points_home(mk().eval()))
        out[name] = rs; print(name, rs, flush=True)
    json.dump(out, open(os.path.join(HERE, 'dial_probe.json'), 'w'), indent=1)
