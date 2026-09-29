"""r4_summary.py  -  round 4 results: per arm, running score at the end, frozen exam at 10 s (200 trips, seed 4242),
how hard the fly turns on the way home (mean |turn|, full lock = 8; spinners sit near 7.8), and whether the memory
holds the way home at the turn (R^2 of a readout, 10 s wander)."""
import sys, json, glob, os, math, torch, statistics as st
sys.path.insert(0, '.'); sys.path.insert(0, '../level3'); torch.set_num_threads(1)
from nets import load
from world import run_episode
out = {}
for arm in ('fw', 'fwnohs', 'twin', 'twinhs', 'twintf'):
    rows = []
    for d in sorted(glob.glob(f'runs/r4_{arm}_s*')):
        if not os.path.isdir(d) or not os.path.exists(d + '/final.pt'): continue
        L = [json.loads(l) for l in open(d + '/log.jsonl')]
        net = load(d + '/final.pt'); turns = []; st0 = net.step
        def h(inp, active=None, st0=st0):
            o = st0(inp, active); turns.append(o[0].abs().mean().item()); return o
        net.step = h
        with torch.no_grad(): r = run_episode(net, batch=200, t_out=10, seed=4242)
        net.step = st0
        ret = turns[100:300]     # trip 1 return ticks
        rows.append(dict(run=os.path.basename(d), running=round(L[-1]['running'], 2), exam10=round(r['score'], 2),
                         arrived=round(r['arrived'], 2), turn_return=round(sum(ret) / len(ret), 2)))
    out[arm] = rows
    if rows: print(f"{arm:8s} exam10 {[x['exam10'] for x in rows]} mean {st.mean(x['exam10'] for x in rows):.2f} | running {[x['running'] for x in rows]} | |turn| home {[x['turn_return'] for x in rows]}")
with torch.no_grad():
    class RW:
        def reset_fast(s, b): s.b = b
        def reset_activity(s): pass
        def step(s, inp, active=None): z = torch.zeros(s.b); return z, z, z
    class SP(RW):
        def step(s, inp, active=None): z = torch.zeros(s.b); return torch.full((s.b,), 7.8), z, z
    out['never_steers_exam10'] = round(run_episode(RW(), batch=200, t_out=10, seed=4242)['score'], 2)
    out['spinner_exam10'] = round(run_episode(SP(), batch=200, t_out=10, seed=4242)['score'], 2)
print('never steers', out['never_steers_exam10'], 'spinner', out['spinner_exam10'])
json.dump(out, open('r4_results.json', 'w'), indent=1)
