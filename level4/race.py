"""race.py  -  after round 6, Path 2 (the race): among runs whose memory was within reach, what separates learners from spinners?
For each within-reach run of rounds 5-6 (reach.json) and the dial / Path-4 runs, at checkpoints 0, 50?, 100, 200, 300, 400:
  align = correlation, over the return, between the turn the network makes and the ideal turn (signed angle from heading
          to home); > 0 means it has started to steer home.
  spin  = mean |turn| on the return as a share of the maximum turn; rises towards 1 as it learns to spin.
1 trip, 10 s wander (20 s return), 400 flies, seed 4242.       python3 level4/race.py [run-glob ...]  -> level4/race.json"""
import sys, os, glob, json, math, torch
torch.set_num_threads(8)
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'level3'))
from nets import load
from world import run_episode
from flynet import TURN_MAX

def race(net):
    st = net.step; rec = {'k': 0, 'pos': None, 'tu': [], 'id': []}
    def h(inp, active=None):
        o = st(inp, active); k = rec['k']; rec['k'] += 1
        hv = inp[:, 0:2]; step = inp[:, 2:3] * hv * 0.1
        rec['pos'] = step if rec['pos'] is None else rec['pos'] + step
        if k >= 100:
            home = -rec['pos']; cross = hv[:, 0] * home[:, 1] - hv[:, 1] * home[:, 0]; dot = (hv * home).sum(1)
            far = home.norm(dim=1) > 0.5
            rec['tu'].append(o[0][far]); rec['id'].append(torch.atan2(cross, dot)[far])
        return o
    net.step = h
    with torch.no_grad(): run_episode(net, batch=400, t_out=10, trips=1, seed=4242)
    net.step = st
    tu = torch.cat(rec['tu']); idl = torch.cat(rec['id'])
    if not torch.isfinite(tu).all(): return None, None
    a = torch.corrcoef(torch.stack([tu, idl]))[0, 1]
    return round(float(a), 3), round(float(tu.abs().mean() / TURN_MAX), 3)

if __name__ == '__main__':
    reach = {r['run']: r for r in json.load(open(os.path.join(HERE, 'reach.json')))}
    pats = sys.argv[1:] or ['WITHIN']
    runs = []
    for p in pats:
        if p == 'WITHIN': runs += [n for n, r in reach.items() if r['within_reach']]
        else: runs += [os.path.basename(d) for d in sorted(glob.glob(os.path.join(HERE, 'runs', p))) if os.path.isdir(d)]
    out = json.load(open(os.path.join(HERE, 'race.json'))) if os.path.exists(os.path.join(HERE, 'race.json')) else {}
    for n in runs:
        row = {}
        for it in (0, 100, 200, 300, 400, 600):
            f = os.path.join(HERE, 'runs', n, f'ckpt_{it:05d}.pt')
            if os.path.exists(f): row[it] = race(load(f).eval())
        out[n] = row; print(n, reach.get(n, {}).get('learned'), row, flush=True)
    json.dump(out, open(os.path.join(HERE, 'race.json'), 'w'), indent=1)
