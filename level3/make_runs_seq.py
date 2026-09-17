"""make_runs_seq.py – rebuild the per-run summary the study pages use (runs_seq.json) from the run folders.
    python3 level3/make_runs_seq.py <out.json>
"""
import json, glob, os, statistics as s, sys, re
HERE = os.path.dirname(os.path.abspath(__file__)); L = json.load(open(os.path.join(HERE, 'campaign/lessons.json')))
MAN = {'run1': ('baseline: erase penalty 0.05, food stand 0.5 s, curriculum 10 then 20 s', 'random start', 'Learn to home on 10 s then 20 s with the memory in F.'),
       'run2': ('erase penalty 0.05 → 0.5', 'random start', 'A dearer fade should push the erase gate toward firing only at food.'),
       'run3': ('food stand 0.5 s → 2 s', 'random start', 'Four times more food ticks should give the erase gate enough signal to learn the reset.')}
def key(r): m = re.match(r'run(\d+)([A-Z]?)', r); return (int(m.group(1)), m.group(2))
rows = []
for d in sorted([p for p in glob.glob(os.path.join(HERE, 'runs/run*')) if os.path.isdir(p)], key=lambda p: key(os.path.basename(p))):
    r = os.path.basename(d); e = json.load(open(d + '/entry.json')) if os.path.exists(d + '/entry.json') else {}
    res = json.load(open(d + '/results.json')) if os.path.exists(d + '/results.json') else {}
    knob, parent, pred = (e.get('knob'), e.get('parent'), e.get('prediction')) if e else MAN.get(r, ('?', None, ''))
    m = {}
    for f in sorted(glob.glob(d + '/test*.json')):
        T = json.load(open(f))
        if 'bars' not in T or 'traces' not in T: continue
        tr = T['traces']; ef = [x for x, fd in zip(tr['erase'], tr['food']) if fd]; en = [x for x, fd in zip(tr['erase'], tr['food']) if not fd]
        w = [x for x, sp in zip(tr['write'], tr['speed']) if sp > 0]; sp = [x for x in tr['speed'] if x > 0]; mw, ms = s.mean(w), s.mean(sp)
        corr = s.mean([(a - mw) * (b - ms) for a, b in zip(w, sp)]) / (s.pstdev(w) * s.pstdev(sp) + 1e-9)
        m[os.path.basename(f)] = dict(A=round(T['bars']['A']['score'], 2), B=round(T['bars']['B']['score'], 2), C=round(T['bars']['C']['score'], 2), ef=round(s.mean(ef), 4), en=round(s.mean(en), 4), corr=round(corr, 2), tuned=T['tuning']['n_tuned'], t=T.get('t_out', 20))
    rows.append(dict(run=r, knob=knob, parent=parent, pred=pred, lesson=(L.get(r) or {}).get('lesson', ''), title=(L.get(r) or {}).get('title', ''), tests=m, minutes=res.get('minutes'), stopped=res.get('stopped_early')))
json.dump(rows, open(sys.argv[1], 'w'), separators=(',', ':')); print(len(rows), 'runs')
