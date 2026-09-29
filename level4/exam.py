"""exam.py  –  level 4: every frozen network through every condition in the charter.

    python3 level4/exam.py --brains level4/brains.json --out level4/results.json [--only std30,len45]

Conditions (charter, "What better means"): the standard exam (seed 4242, 200 trips, 30 s), the same on
1,000 fresh trips (seed 5151), longer wanders (45, 60, 90 s), a drifting compass (0.05, 0.15), a long stop
halfway through a 30 s walk (10 s and 30 s standing still), and five trips per episode (score per trip).
Each score comes with a 95% interval from resampling the trips 1,000 times: the exam's own noise.
Fast-weight networks are also run with F held at zero on the standard exam.
"""
import argparse, json, os, sys, time, torch
torch.set_num_threads(1)
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
sys.path.insert(0, os.path.join(ROOT, 'level3')); sys.path.insert(0, HERE)
from world import run_episode
from handbrain import HandBrain
from nets import load

CONDS = {
    'std30':   dict(t_out=30.0, seed=4242, batch=200),
    'std30_1k': dict(t_out=30.0, seed=5151, batch=1000),
    'len45':   dict(t_out=45.0, seed=4242, batch=200),
    'len60':   dict(t_out=60.0, seed=4242, batch=200),
    'len90':   dict(t_out=90.0, seed=4242, batch=200),
    'drift05': dict(t_out=30.0, seed=4242, batch=200, drift=0.05),
    'drift15': dict(t_out=30.0, seed=4242, batch=200, drift=0.15),
    'stop10':  dict(t_out=40.0, seed=4242, batch=200, stop=(15.0, 10.0)),   # walk 15 s, stand 10 s, walk 15 s
    'stop30':  dict(t_out=60.0, seed=4242, batch=200, stop=(15.0, 30.0)),   # walk 15 s, stand 30 s, walk 15 s
    'trips5':  dict(t_out=30.0, seed=4242, batch=200, trips=5),
}


class RandomWalk:
    zero_F = False
    def reset_fast(self, b): self.b = b
    def reset_activity(self): pass
    def step(self, inp, active=None): z = torch.zeros(self.b); return z, z, z


def interval(per_agent, n=1000):
    """95% interval of the mean closest approach, resampling agents (each agent's trips averaged first)."""
    a = per_agent.mean(0); g = torch.Generator().manual_seed(0)
    idx = torch.randint(0, len(a), (n, len(a)), generator=g)
    m = a[idx].mean(1).sort().values
    return [float(m[int(0.025 * n)]), float(m[int(0.975 * n)])]


def exam(brain, c):
    kw = {k: v for k, v in c.items()}
    r = run_episode(brain, **kw)
    pa = r['per_agent']
    out = dict(score=r['score'], arrived=r['arrived'], ci=interval(pa))
    if kw.get('trips', 2) > 2: out['per_trip'] = [float(x) for x in pa.mean(1)]
    return out


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--brains', required=True); p.add_argument('--out', required=True); p.add_argument('--only', default='')
    a = p.parse_args()
    brains = json.load(open(a.brains))                        # [{"name":..., "arm":..., "ckpt": path or "hand"/"random"}]
    conds = a.only.split(',') if a.only else list(CONDS)
    res = json.load(open(a.out)) if os.path.exists(a.out) else {}
    with torch.no_grad():
        for b in brains:
            row = res.setdefault(b['name'], dict(arm=b['arm'], ckpt=b['ckpt'], conds={}))
            for cn in conds:
                t0 = time.time()
                if b['ckpt'] == 'hand': brain = HandBrain()
                elif b['ckpt'] == 'random': brain = RandomWalk()
                else: brain = load(os.path.join(ROOT, b['ckpt']))
                row['conds'][cn] = exam(brain, CONDS[cn])
                if cn == 'std30' and hasattr(brain, 'A'):          # FW only: the memory is in F?
                    brain.zero_F = True; row['conds']['std30_noF'] = exam(brain, CONDS[cn]); brain.zero_F = False
                print(f"{b['name']:28s} {cn:9s} {row['conds'][cn]['score']:.3f}  ci {row['conds'][cn]['ci'][0]:.2f}-{row['conds'][cn]['ci'][1]:.2f}  arrived {row['conds'][cn]['arrived']*100:.0f}%  ({time.time()-t0:.0f}s)", flush=True)
            json.dump(res, open(a.out, 'w'), indent=1)
