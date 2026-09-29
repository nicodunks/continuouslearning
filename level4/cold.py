"""cold.py  –  read the sweeps, pick each arm's learning rate by the charter's rule (lowest running score over the
last 50 iterations at 600), write the choice to sweeps.json, and launch that arm's cold seeds.

    python3 level4/cold.py            (prints the choice and launches)
"""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
RATES = ['3e-4', '1e-3', '3e-3']
COLD = ['--stages', '10,20,30', '--stage_cap', '1500', '--iters', '4000', '--lr_decay', '1',
        '--food_stand', '2.0', '--erase_penalty', '0.05', '--batch', '32']
PRED = {
    'twin': 'Cold pair. TWIN from a random start, run 3\'s recipe, curriculum 10 → 20 → 30 s. Predicted: finishes the curriculum (reaches 30 s by promotion, not by the cap) on more seeds than FW-cold.',
    'fw': 'Cold pair. FW from a random start, the same recipe and budget as TWIN-cold. Predicted: stalls at 20 s (reaches 30 s only by the stage cap, or scores above 2.5 there) on at least 2 of 3 seeds, as in campaign 2.',
    'gru': 'Reference arm, not in the verdict. A textbook GRU (52 units) from a random start, same recipe and budget. Predicted: lands within 0.3 of TWIN-cold, showing TWIN is not a strawman.',
}
choice = {}
for arch in ('twin', 'fw', 'gru'):
    rows = {}
    for lr in RATES:
        L = [json.loads(l) for l in open(os.path.join(HERE, 'runs', f'sweep_{arch}_{lr}', 'log.jsonl'))]
        rows[lr] = L[-1]['running']
    best = min(rows, key=rows.get)
    choice[arch] = dict(running_at_600=rows, chosen=best)
    print(arch, {k: round(v, 3) for k, v in rows.items()}, '->', best)
json.dump(choice, open(os.path.join(HERE, 'sweeps.json'), 'w'), indent=1)
if '--dry' in sys.argv: sys.exit()
# amendment 08:35: the activity arms' sweep was flat (all rates at the random walk), so they run at both 3e-4 and 1e-3
PLAN = [('fw', 'fw_c', choice['fw']['chosen'])] + [(a, f'{a}_c', lr) for a in ('twin', 'gru') for lr in ('3e-4', '1e-3')]
for arch, name, lr in PLAN:
    for seed in (0, 1, 2):
        tag = f'{name}{seed}' if arch == 'fw' else f'{name}{seed}_lr{lr}'
        subprocess.run([sys.executable, os.path.join(HERE, 'launch.py'), tag, f'{arch.upper()}-cold', PRED[arch] + f' Rate {lr}.', '--',
                        '--arch', arch, '--lr', lr, '--seed', str(seed)] + COLD, check=True)
