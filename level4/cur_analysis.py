"""cur_analysis.py  -  30 Sept: our board vs the transformer through the same shortened schedule (10 -> 20 -> 30 s, stage cap
700, 2,100 iterations, 3 tries each). Grades final.pt if it exists, else the latest checkpoint, on the standard 30 s exam
(200 trips, seed 4242) and the 10 s exam; records the last stage reached.   python3 level4/cur_analysis.py -> cur_results.json"""
import sys, os, glob, json, torch
torch.set_num_threads(4)
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'level3'))
from nets import load
from world import run_episode
from exam import exam, CONDS
out = {}
for d in sorted(glob.glob(os.path.join(HERE, 'runs', 'cur_*'))):
    if not os.path.isdir(d): continue
    n = os.path.basename(d); f = d + '/final.pt'
    if not os.path.exists(f):
        cks = sorted(glob.glob(d + '/ckpt_*.pt'))
        if not cks: continue
        f = cks[-1]
    L = [json.loads(l) for l in open(d + '/log.jsonl')]
    net = load(f)
    with torch.no_grad():
        e30 = exam(net, CONDS['std30'])['score']; e10 = run_episode(net, batch=200, t_out=10, seed=4242)['score']
    out[n] = dict(file=os.path.basename(f), last_it=L[-1]['it'], last_trip_s=L[-1]['t_out'], exam30=round(e30, 2), exam10=round(e10, 2))
    print(n, out[n], flush=True)
json.dump(out, open(os.path.join(HERE, 'cur_results.json'), 'w'), indent=1)
