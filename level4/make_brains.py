"""make_brains.py  –  list every level 4 network for the exam: final.pt if the run finished, else its latest
checkpoint (the 11:50 cutoff), plus the four FW networks, the hand brain and the random walk.
    python3 level4/make_brains.py [--only-new results.json] > level4/brains_all.json"""
import glob, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ARM = {'twin_w': 'TWIN-warm', 'twinB_w': 'TWIN-warm-B', 'twinA_w': 'TWIN-warm-aux', 'fwA_': 'FW-warm-aux', 'fw_c': 'FW-cold',
       'twin_c': 'TWIN-cold', 'gru_c': 'GRU-cold', 'twin_aux': 'TWIN-aux', 'gru_aux': 'GRU-aux'}
out = [dict(name='hand', arm='hand', ckpt='hand'), dict(name='random', arm='random', ckpt='random')] + \
      [dict(name=f'fw{r}', arm='FW', ckpt=f'level3/runs/run{r}/final.pt') for r in (28, 40, 41, 45)]
for d in sorted(glob.glob(os.path.join(HERE, 'runs', '*'))):
    n = os.path.basename(d)
    if not os.path.isdir(d) or n.startswith('sweep'): continue
    arm = next((v for k, v in sorted(ARM.items(), key=lambda kv: -len(kv[0])) if n.startswith(k)), None)
    if arm is None: continue
    if '_lr' in n: arm += '@' + n.split('_lr')[1]
    fin = os.path.join(d, 'final.pt'); cks = sorted(glob.glob(os.path.join(d, 'ckpt_0*.pt')))
    ck = fin if os.path.exists(fin) else (cks[-1] if cks else None)
    if ck is None: continue
    out.append(dict(name=n, arm=arm, ckpt=os.path.relpath(ck, os.path.join(HERE, '..')), finished=os.path.exists(fin)))
if '--done' in sys.argv: out = [b for b in out if b.get('finished') and b['arm'] not in ('FW', 'hand', 'random')]
print(json.dumps(out, indent=1))
