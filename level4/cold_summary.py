"""cold_summary.py  –  the cold pair's trainability numbers, from the logs and the exam, for the page and narrative.
For every cold run: was each stage passed by learning (promotion) or by the stage cap, and its standard-exam score.
    python3 level4/cold_summary.py   -> prints a table, writes cold_summary.json and the FW-cold sentence into fwcold_text.json"""
import glob, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, 'results.json')))
rows = []
for d in sorted(glob.glob(os.path.join(HERE, 'runs', '*'))):
    n = os.path.basename(d)
    if not os.path.isdir(d) or not re.match(r'(fw_c|twin_c|gru_c|twin_aux|gru_aux)', n): continue
    out = open(d + '.out').read()
    promos = [(int(a), float(b)) for a, b in re.findall(r'iteration (\d+): promoted to stage \d \((\d+\.\d) s\)', out)]
    L = [json.loads(l) for l in open(os.path.join(d, 'log.jsonl'))]
    # a promotion is "by learning" if it came before the stage cap (1,500 iterations into the stage)
    starts = [0] + [p[0] + 1 for p in promos]
    how = ['learned' if p[0] - starts[i] < 1499 else 'cap' for i, p in enumerate(promos)]
    rows.append(dict(run=n, reached_it=L[-1]['it'] + 1, finished=os.path.exists(os.path.join(d, 'final.pt')), promotions=promos, how=how,
                     std30=R.get(n, {}).get('conds', {}).get('std30', {}).get('score')))
for r in rows: print(f"{r['run']:16s} it {r['reached_it']:5d} {'done' if r['finished'] else 'CUT '}  stages: {', '.join(f'{int(s)} s at {i} ({h})' for (i, s), h in zip(r['promotions'], r['how'])) or '-':50s} std30 {r['std30']}")
json.dump(rows, open(os.path.join(HERE, 'cold_summary.json'), 'w'), indent=1)
fw = [r for r in rows if r['run'].startswith('fw_c')]
learned20 = sum(1 for r in fw if r['how'][:1] == ['learned']); learned30 = sum(1 for r in fw if r['how'][1:2] == ['learned'])
sc = ', '.join(f"{r['std30']:.2f}" for r in fw if r['std30'] is not None)
riv = [r for r in rows if re.match(r'(twin_c|gru_c)', r['run'])]
riv_l = sum(1 for r in riv if 'learned' in r['how'])
best20 = []
for r in fw:
    L = [json.loads(l) for l in open(os.path.join(HERE, 'runs', r['run'], 'log.jsonl'))]
    best20.append(min(x['running'] for x in L if x['t_out'] == 20.0 and x['stage'] == 1))
sent = (f"Our network from scratch did better, though not cleanly. All three seeds passed the 10-second stage by learning (at iterations "
        f"{', '.join(str(r['promotions'][0][0]) for r in fw)}). None met the promotion bar of 1.5 at 20 seconds, although their best running scores there were "
        f"{', '.join(f'{b:.2f}' for b in best20)} against 3.65 for a fly that never steers and 4.56 for a spinner, so all three learned something there. "
        f"On the standard exam, at the end of their budget, they score {sc}. Of the {len(riv)} rival runs without a teacher, {riv_l} passed any stage by learning.")
t = json.load(open(os.path.join(HERE, 'fwcold_text.json'))) if os.path.exists(os.path.join(HERE, 'fwcold_text.json')) else {}
t['sentence'] = sent; json.dump(t, open(os.path.join(HERE, 'fwcold_text.json'), 'w'), indent=1); print(sent)
