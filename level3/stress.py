"""stress.py  –  level 4: freeze networks and make the world harder, with no retraining.

    python3 level3/stress.py

Conditions: wander 30, 45, 60 s on the standard world (seed 4242, 200 trips), and 30 s with a compass
that drifts (0.05 and 0.15 per root-second).  Brains: the hand-built fly brain, and each checkpoint
listed in BRAINS, each run with F allowed and with F held at zero.  Writes campaign/stress.json.
"""
import json, os, sys, torch
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from world import run_episode
from flynet import FlyNet
from handbrain import HandBrain

BRAINS = [('hand brain', None), ('run17 · score line', 'runs/run17/ckpt_00200.pt'), ('run19 · all three ingredients', 'runs/run19/final.pt'),
          ('run16 · reset line', 'runs/run16/final.pt'), ('run3 · first homing network', 'runs/run3/ckpt_02300.pt'), ('run20 · rival (activity only)', 'runs/run20/final.pt')]
CONDS = [dict(name='30 s', t_out=30.0, drift=0.0), dict(name='45 s', t_out=45.0, drift=0.0), dict(name='60 s', t_out=60.0, drift=0.0),
         dict(name='30 s · drift 0.05', t_out=30.0, drift=0.05), dict(name='30 s · drift 0.15', t_out=30.0, drift=0.15)]

def load(path):
    ck = torch.load(os.path.join(HERE, path)); a = ck.get('args', {})
    net = FlyNet(n=ck['net']['W'].shape[0], use_fast=bool(a.get('use_fast', 1)), f_max=float(a.get('f_max', 1.0)), rule=a.get('rule', 'hebb'))
    net.load_state_dict(ck['net']); net.eval(); return net

out = dict(conds=[c['name'] for c in CONDS], brains=[])
with torch.no_grad():
    for name, path in BRAINS:
        if path and not os.path.exists(os.path.join(HERE, path)): print('skip', name); continue
        row = dict(name=name, F=[], noF=[], arr=[])
        for c in CONDS:
            if path is None:
                r = run_episode(HandBrain(), batch=200, t_out=c['t_out'], seed=4242, drift=c['drift']); row['F'].append(r['score']); row['noF'].append(None); row['arr'].append(r['arrived'])
            else:
                net = load(path)
                r = run_episode(net, batch=200, t_out=c['t_out'], seed=4242, drift=c['drift']); row['F'].append(r['score']); row['arr'].append(r['arrived'])
                net.zero_F = True; b = run_episode(net, batch=200, t_out=c['t_out'], seed=4242, drift=c['drift']); row['noF'].append(b['score'])
            print(f"{name:32s} {c['name']:18s} F {row['F'][-1]:.2f}  noF {row['noF'][-1] if row['noF'][-1] is None else round(row['noF'][-1],2)}  arrived {row['arr'][-1]*100:.0f}%", flush=True)
        out['brains'].append(row)
    # random walk baseline per condition
    class RW:
        def reset_fast(self, b): self.b = b
        def reset_activity(self): pass
        def step(self, inp, active=None): z = torch.zeros(self.b); return z, z, z
    out['random'] = [run_episode(RW(), batch=200, t_out=c['t_out'], seed=4242, drift=c['drift'])['score'] for c in CONDS]
json.dump(out, open(os.path.join(HERE, 'campaign', 'stress.json'), 'w'), indent=1); print('stress.json written')
