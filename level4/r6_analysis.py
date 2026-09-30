"""r6_analysis.py  -  round 6 results.   python3 level4/r6_analysis.py [e1] [e2] [e3]   -> level4/r6_results.json (merged)
E1: per design, frozen exam at 10 s (200 trips, seed 4242), learned = below 2.39; plus the round-5 FW and twin baselines.
E2: per design, mean over starts of the benchmark errors (bench/*.json), and the "knows nothing" error (mean distance).
E3: per arm, the level-4 exam (standard, 1,000 fresh, 90 s, 30 s stop) and, for the blend, where beta went."""
import sys, os, glob, json, math, statistics as st, torch
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'level3'))
torch.set_num_threads(1)
from nets import load
from world import run_episode
from exam import exam, CONDS
OUT = os.path.join(HERE, 'r6_results.json')
res = json.load(open(OUT)) if os.path.exists(OUT) else {}
what = sys.argv[1:] or ['e1', 'e2', 'e3']

if 'e1' in what:
    e1 = {}
    for d in sorted(glob.glob(os.path.join(HERE, 'runs', 'r6e1_*'))):
        if not os.path.isdir(d) or not os.path.exists(d + '/final.pt'): continue
        n = os.path.basename(d); arch = 'fw_hebb (round 5)' if n.startswith('r5_fw') else 'twin (round 5)' if n.startswith('r5_tw') else n[5:].rsplit('_s', 1)[0]
        net = load(d + '/final.pt')
        with torch.no_grad(): s = run_episode(net, batch=200, t_out=10, seed=4242)['score']
        L = [json.loads(l) for l in open(d + '/log.jsonl')]
        e1.setdefault(arch, []).append(dict(run=n, exam10=round(s, 2), learned=s < 2.39, running=round(L[-1]['running'], 2)))
    r5 = json.load(open(os.path.join(HERE, 'r5_results.json')))['groups']   # round 5 graded its 10 s checkpoints the same way
    for g, name in (('fw', 'fw_hebb (round 5)'), ('tw', 'twin (round 5)')):
        e1[name] = [dict(run=r['run'], exam10=r['exam10'], learned=r['exam10'] < 2.39) for r in r5.get(g, [])]
    for a, rows in e1.items(): print(f"E1 {a:20s} learned {sum(r['learned'] for r in rows)} of {len(rows)}   exam10 {[r['exam10'] for r in rows]}")
    res['e1'] = e1

if 'e2' in what:
    import bench
    with torch.no_grad():
        base = {}
        for name, T, stop, drift in [('walk30', 30., None, 0.), ('walk60', 60., None, 0.), ('walk90', 90., None, 0.), ('stop30', 60., (15., 30.), 0.), ('drift15', 30., None, 0.15)]:
            homes = [h for _, h in bench.walks(500, T, 777, stop, drift)]
            base[name] = round(float(homes[-1].norm(dim=1).mean()), 3)
    e2 = {'knows_nothing': base, 'designs': {}}
    for f in sorted(glob.glob(os.path.join(HERE, 'bench', '*.json'))):
        r = json.load(open(f)); e2['designs'].setdefault(r['arch'], []).append(r)
    summ = {}
    for a, rs in e2['designs'].items():
        summ[a] = {t: round(st.mean(x['tests'][t]['end'] for x in rs), 3) for t in rs[0]['tests']}
        summ[a]['n'] = len(rs); summ[a]['params'] = rs[0]['params']
        print(f"E2 {a:12s} n={len(rs)} " + '  '.join(f"{t} {v}" for t, v in summ[a].items() if t not in ('n', 'params')))
    print('E2 knows nothing', base)
    e2['summary'] = summ; res['e2'] = e2

if 'e4' in what:
    e4 = {}
    for d in sorted(glob.glob(os.path.join(HERE, 'runs', 'r6e4_*'))):
        if not os.path.isdir(d): continue
        n = os.path.basename(d); arm = 'hebbl + teacher' if '_aux_' in n else 'hebbl'
        L = [json.loads(l) for l in open(d + '/log.jsonl')]
        moved = next((r['it'] for r in L if r['stage'] > 0 and r['t_out'] > 10), None)
        net = load(d + '/ckpt_01400.pt')   # the last checkpoint of the 10 s stage for every run
        with torch.no_grad(): s = run_episode(net, batch=200, t_out=10, seed=4242)['score']
        e4.setdefault(arm, []).append(dict(run=n, exam10_at_1400=round(s, 2), learned=s < 2.39, left_10s_at=moved, stopped_at=L[-1]['it']))
    for a, rows in e4.items(): print(f"E4 {a:16s} {rows}")
    res['e4'] = e4

if 'e3' in what:
    e3 = {}
    for d in sorted(glob.glob(os.path.join(HERE, 'runs', 'r6e3_*'))):
        if not os.path.isdir(d) or not os.path.exists(d + '/final.pt'): continue
        n = os.path.basename(d); arm = n.split('_')[1]; net = load(d + '/final.pt')
        row = dict(run=n)
        with torch.no_grad():
            for c in ('std30', 'std30_1k', 'len90', 'stop30'): row[c] = round(exam(net, CONDS[c])['score'], 3)
            if hasattr(net, 'beta'):
                bs = []; st0 = net.step
                def h(inp, active=None):
                    o = st0(inp, active); bs.append(float(net.last_beta.mean())); return o
                net.step = h; run_episode(net, batch=64, t_out=30, seed=4242); net.step = st0
                row['beta_mean'] = round(sum(bs) / len(bs), 4); row['beta_max'] = round(max(bs), 4)
        e3.setdefault(arm, []).append(row)
    for a, rows in e3.items():
        print(f"E3 {a:6s} std30 {[r['std30'] for r in rows]} mean {st.mean(r['std30'] for r in rows):.3f}  stop30 {st.mean(r['stop30'] for r in rows):.2f}  len90 {st.mean(r['len90'] for r in rows):.2f}" + (f"  beta {[r.get('beta_mean') for r in rows]}" if 'beta_mean' in rows[0] else ''))
    res['e3'] = e3
json.dump(res, open(OUT, 'w'), indent=1)
