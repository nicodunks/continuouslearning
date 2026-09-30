"""reach.py  -  is a working memory within reach of training?  (29 Sept 2026, after round 6)
For every 10 s learnability run of rounds 5 and 6, how well does the network's ACTIVITY point home
(R^2 of the unit home direction, straight-line readout, 1,200 flies, 10 s wander, fit 600 / score 600)
at iterations 0, 100 and 200 of training?  Round 6 found that the learners start above ~0.7 at birth,
but FW with an empty board starts at ~0.2 and still learns: its memory is one knob away. This asks whether
a short look at the start of training captures "present or one knob away" in a single measurement.
    python3 level4/reach.py   -> level4/reach.json
"""
import sys, os, glob, json, torch
torch.set_num_threads(8)
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'level3'))
from nets import load
from world import run_episode

def points_home(net):
    st = net.step; rec = {'v': None, 'k': 0}
    def h(inp, active=None):
        o = st(inp, active); step = inp[:, 2:3] * inp[:, 0:2] * 0.1
        rec['v'] = step if rec['v'] is None else rec['v'] + step; rec['k'] += 1
        if rec['k'] == 100: rec['x'] = net.x.clone(); rec['home'] = rec['v'].clone()
        return o
    net.step = h
    with torch.no_grad(): run_episode(net, batch=1200, t_out=10, trips=1, seed=4242)
    net.step = st
    X, H = rec['x'], rec['home']
    if not torch.isfinite(X).all(): return None
    D = H / (H.norm(dim=1, keepdim=True) + 1e-6); half = 600
    A1 = torch.cat([X[:half], torch.ones(half, 1)], 1); W = torch.linalg.solve(A1.T @ A1 + 1e-2 * torch.eye(A1.shape[1]), A1.T @ D[:half])
    P = torch.cat([X[half:], torch.ones(len(X) - half, 1)], 1) @ W
    return round(float(1 - ((P - D[half:]) ** 2).sum() / ((D[half:] - D[half:].mean(0)) ** 2).sum()), 3)

if __name__ == "__main__":
  r5 = json.load(open(os.path.join(HERE, 'r5_results.json')))['groups']
  r6 = json.load(open(os.path.join(HERE, 'r6_results.json')))['e1']
  exam = {r['run']: r['exam10'] for g in r5.values() for r in g}
  exam.update({r['run']: r['exam10'] for g in r6.values() for r in g if r['run'].startswith('r6e1_')})
  out = []
  for d in sorted(glob.glob(os.path.join(HERE, 'runs', 'r5_*')) + glob.glob(os.path.join(HERE, 'runs', 'r6e1_*'))):
      n = os.path.basename(d)
      if not os.path.isdir(d) or n not in exam: continue
      row = dict(run=n, exam10=exam[n], learned=bool(exam[n] == exam[n] and exam[n] < 2.39))
      for it in (0, 100, 200):
          f = f'{d}/ckpt_{it:05d}.pt'
          row[f'it{it}'] = points_home(load(f).eval()) if os.path.exists(f) else None
      out.append(row); print(row, flush=True)
  json.dump(out, open(os.path.join(HERE, 'reach.json'), 'w'), indent=1)
