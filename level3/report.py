"""report.py  –  build the Night Report: every run compared, drawn from the real data.

    python3 level3/report.py            writes docs/roadmap/night-report.html and a scratch copy for the Artifact

Reads runs/<run>/{entry,results}.json, log.jsonl, test_*.json, campaign/{floor,lessons}.json, campaign/narrative.md.
Nothing here computes new results; it only lays out what train.py and test.py already measured.
"""
import json, os, glob, re, statistics as st, html
HERE = os.path.dirname(os.path.abspath(__file__)); RUNS = os.path.join(HERE, 'runs'); CAMP = os.path.join(HERE, 'campaign')
ROOT = os.path.dirname(HERE)

MANUAL = {  # runs that predate the campaign driver
 'run1': dict(knob='baseline (erase penalty 0.05, food stand 0.5 s)', parent=None, prediction='The plan\'s first run: learn to home on 10 s, then 20 s, with the memory in F.'),
 'run2': dict(knob='erase penalty 0.05 -> 0.5', parent='random start (same seed as run 1)', prediction='Making a constant fade expensive should push the erase gate toward firing only at food.'),
 'run3': dict(knob='food stand 0.5 s -> 2.0 s', parent='random start (same seed as run 1)', prediction='Four times more food ticks should give the erase gate enough signal to learn the reset.'),
}
def jload(p, d=None):
    try: return json.load(open(p))
    except Exception: return d

def metrics(T):
    tr = T['traces']
    sp = [s for s in tr['speed'] if s > 0]; w = [x for x, s in zip(tr['write'], tr['speed']) if s > 0]
    corr = 0.0
    if len(sp) > 2 and st.pstdev(sp) > 0 and st.pstdev(w) > 0:
        mw, ms = st.mean(w), st.mean(sp); corr = st.mean([(a-mw)*(b-ms) for a, b in zip(w, sp)]) / (st.pstdev(w)*st.pstdev(sp))
    ef = [e for e, f in zip(tr['erase'], tr['food']) if f > 0]; enf = [e for e, f in zip(tr['erase'], tr['food']) if f == 0]
    sat = st.mean([st.mean([1 if abs(v) > 0.98 else 0 for v in row]) for row in tr['F']]) if tr['F'] else 0
    return dict(A=T['bars']['A']['score'], B=T['bars']['B']['score'], C=T['bars']['C']['score'], arr=T['bars']['A']['arrived'],
                tuned=T['tuning']['n_tuned'], corr=corr, ef=st.mean(ef) if ef else 0, enf=st.mean(enf) if enf else 0, sat=sat,
                ws=T['ws'], Aabs=T['A_abs_mean'], t_out=T['t_out'], ckpt=os.path.basename(T['ckpt']))

def slim_test(T):
    tr = T['traces']; r3 = lambda a: [round(v, 3) for v in a]
    return dict(t_out=T['t_out'], ckpt=os.path.basename(T['ckpt']), bars=T['bars'], n=T['n'],
                strength=r3(T['tuning']['all_strength']), tuning_all=[r3(c) for c in T['tuning']['all_curves']],
                traces=dict(t=[round(v, 1) for v in tr['t']], speed=r3(tr['speed']), food=tr['food'], write=r3(tr['write']), erase=[round(v, 4) for v in tr['erase']], dist=r3(tr['dist']), F=[r3(row) for row in tr['F']]),
                A=[[round(v, 2) for v in row] for row in T['A_heat']], A_abs=round(T['A_abs_mean'], 4), ws=round(T['ws'], 4), m=metrics(T))

def collect():
    runs = {}
    for d in sorted(glob.glob(os.path.join(RUNS, 'run*'))):
        if not os.path.isdir(d): continue
        run = os.path.basename(d)
        entry = jload(os.path.join(d, 'entry.json'), None) or dict(run=run, **MANUAL.get(run, dict(knob='?', parent=None, prediction='')))
        results = jload(os.path.join(d, 'results.json'), None)
        status = jload(os.path.join(d, 'status.json'), {})
        L = [json.loads(l) for l in open(os.path.join(d, 'log.jsonl'))] if os.path.exists(os.path.join(d, 'log.jsonl')) else []
        log = [dict(it=r['it'], stage=r['stage'], t_out=r['t_out'], running=round(r['running'], 3), loss=round(r['loss'], 3), ws=round(r['ws'], 4), A=round(r['A_abs'], 4),
                    drift=(dict(F=round(r['drift']['score_F'], 3), noF=round(r['drift']['score_noF'], 3)) if 'drift' in r else None)) for r in L]
        tests = {}
        for f in sorted(glob.glob(os.path.join(d, 'test*.json'))):
            T = jload(f);
            if not T or 'bars' not in T: continue
            tests[os.path.basename(f)] = slim_test(T)
        runs[run] = dict(run=run, knob=entry.get('knob'), parent=entry.get('parent'), prediction=entry.get('prediction'), args=entry.get('args', []),
                         results=results, status=status, log=log, tests=tests, minutes=(results or {}).get('minutes'),
                         stopped_early=(results or {}).get('stopped_early'))
    return runs

def md_to_html(md):
    out = []; para = []
    def flush():
        if para: out.append('<p>' + html.escape(' '.join(para)) + '</p>'); para.clear()
    for line in md.splitlines():
        if line.startswith('# '): flush(); out.append(f'<h2>{html.escape(line[2:])}</h2>')
        elif line.startswith('## '): flush(); out.append(f'<h3>{html.escape(line[3:])}</h3>')
        elif line.startswith('_') and line.endswith('_'): flush(); out.append(f'<p class="note">{html.escape(line.strip("_"))}</p>')
        elif line.strip() == '': flush()
        else: para.append(line.strip())
    flush(); return '\n'.join(out)

def build():
    runs = collect(); floor = jload(os.path.join(CAMP, 'floor.json'), {}); lessons = jload(os.path.join(CAMP, 'lessons.json'), {})
    narrative = md_to_html(open(os.path.join(CAMP, 'narrative.md')).read()) if os.path.exists(os.path.join(CAMP, 'narrative.md')) else ''
    stress = jload(os.path.join(CAMP, 'stress.json'), None)
    data = json.dumps(dict(runs=runs, floor=floor, lessons=lessons, stress=stress, built=__import__('time').strftime('%Y-%m-%d %H:%M')), separators=(',', ':'))
    tpl = open(os.path.join(HERE, 'report_template.html')).read()
    page = tpl.replace('__DATA__', data).replace('__NARRATIVE__', narrative)
    body = page
    full = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n' +
            re.search(r'<title>.*?</title>', body, re.S).group(0) + '\n' + '\n'.join(re.findall(r'<link[^>]+>', body)) + '\n' + re.search(r'<style>.*?</style>', body, re.S).group(0) +
            '\n</head>\n<body>\n' + re.sub(r'<style>.*?</style>', '', re.sub(r'<link[^>]+>', '', re.sub(r'<title>.*?</title>', '', body, count=1)), count=1, flags=re.S).strip() + '\n</body>\n</html>\n')
    os.makedirs(os.path.join(ROOT, 'docs', 'roadmap'), exist_ok=True)
    open(os.path.join(ROOT, 'docs', 'roadmap', 'night-report.html'), 'w').write(full)
    scratch = os.environ.get('SCRATCH')
    if scratch: open(os.path.join(scratch, 'night-report.html'), 'w').write(page)
    print('report built:', len(runs), 'runs;', sum(len(r['tests']) for r in runs.values()), 'tests;', len(page)//1024, 'KB')

if __name__ == '__main__': build()
