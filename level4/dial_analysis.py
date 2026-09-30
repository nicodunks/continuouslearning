"""dial_analysis.py  -  grade the dial (Path 1) and Path 4 runs: exam at 10 s (200 trips, seed 4242; learned = below 2.39)
and the within-reach measure (reach.points_home at iterations 0, 100, 200).   python3 level4/dial_analysis.py GLOB ... -> dial_results.json"""
import sys, os, glob, json, torch
torch.set_num_threads(4)
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'level3'))
from nets import load
from world import run_episode
from reach import points_home
OUT = os.path.join(HERE, 'dial_results.json')
res = json.load(open(OUT)) if os.path.exists(OUT) else {}
for p in sys.argv[1:]:
    for d in sorted(glob.glob(os.path.join(HERE, 'runs', p))):
        n = os.path.basename(d)
        if not os.path.isdir(d) or not os.path.exists(d + '/final.pt'): continue
        with torch.no_grad(): s = run_episode(load(d + '/final.pt'), batch=200, t_out=10, seed=4242)['score']
        row = dict(exam10=round(s, 2), learned=s < 2.39)
        for it in (0, 100, 200):
            f = f'{d}/ckpt_{it:05d}.pt'
            row[f'it{it}'] = points_home(load(f).eval()) if os.path.exists(f) else None
        res[n] = row; print(n, row, flush=True)
json.dump(res, open(OUT, 'w'), indent=1)
