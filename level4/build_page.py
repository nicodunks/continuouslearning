"""build_page.py  –  gather every level 4 number into one JSON blob and pour it into the page template.

    python3 level4/build_page.py        -> docs/roadmap/twin-test.html

Reads: level4/results.json (exam), level4/probe.json (inside the long stop), level4/sweeps.json,
every run's log.jsonl (learning curves, downsampled) and entry.json.
"""
import glob, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
J = lambda p, d=None: json.load(open(p)) if os.path.exists(p) else d

curves = {}
for d in sorted(glob.glob(os.path.join(HERE, 'runs', '*'))):
    if not os.path.isdir(d): continue
    name = os.path.basename(d); f = os.path.join(d, 'log.jsonl')
    if not os.path.exists(f): continue
    L = [json.loads(l) for l in open(f)]
    e = J(os.path.join(d, 'entry.json'), {})
    curves[name] = dict(arm=e.get('arm', ''), pts=[[x['it'], round(x['running'], 3), x['t_out'], round(x['score'], 3)] for x in L[::2]],
                        done=os.path.exists(os.path.join(d, 'final.pt')), prediction=e.get('prediction', ''))

text = J(os.path.join(HERE, 'page_text.json'), {})
parts = [open(os.path.join(HERE, f'page_text_{k}.html')).read() for k in ('predictions', 'honest') if os.path.exists(os.path.join(HERE, f'page_text_{k}.html'))]
if parts: text['honest'] = '\n'.join(parts)
data = dict(results=J(os.path.join(HERE, 'results.json'), {}), probe=J(os.path.join(HERE, 'probe.json'), {}),
            sweeps=J(os.path.join(HERE, 'sweeps.json'), {}), curves=curves, text=text, trap=J(os.path.join(HERE, 'trap.json'), {}))
tpl = open(os.path.join(HERE, 'page_template.html')).read()
out = tpl.replace('/*DATA*/null', json.dumps(data, separators=(',', ':')))
dst = os.path.join(ROOT, 'docs', 'roadmap', 'twin-test.html'); open(dst, 'w').write(out)
print('wrote', dst, len(out) // 1024, 'KB')
