"""campaign.py  –  runs experiments from a queue, one at a time, and tests each one when it ends.

    python3 level3/campaign.py

The queue is level3/campaign/queue.json: a list of runs, each {run, knob, parent, prediction, args, test_t_outs}.
The supervisor (Claude) appends the next run after reading the last one's results, so hypotheses are chosen
as we learn, not fixed in advance.  If the queue is empty the driver waits and checks again every 30 s.
If the queue stays empty for `FALLBACK_AFTER` seconds and campaign/fallback.json has entries, one is used.

For every run it: launches train.py; watches the log and applies the stop rules; on finish runs test.py
on final.pt at each requested wander length and on the best checkpoint; writes runs/<run>/results.json
and appends a line to campaign/log.jsonl.  Nothing here changes the world, the loss or the test.
"""
import json, os, sys, subprocess, time, glob

HERE = os.path.dirname(os.path.abspath(__file__)); RUNS = os.path.join(HERE, 'runs'); CAMP = os.path.join(HERE, 'campaign')
QUEUE = os.path.join(CAMP, 'queue.json'); FALLBACK = os.path.join(CAMP, 'fallback.json'); LOG = os.path.join(CAMP, 'log.jsonl')
FALLBACK_AFTER = 1800
BASELINE = {10.0: 2.6, 20.0: 4.3, 30.0: 5.3}   # what a random walk scores, roughly, by wander length


def load(p, default):
    try: return json.load(open(p))
    except Exception: return default


def say(msg):
    print(time.strftime('%H:%M:%S'), msg, flush=True)


def stop_rules(run, lenient=False):
    """Return a reason string if the run should be killed, else None.  lenient: skip the gap rule
    (used for continuations across a curriculum promotion, where the gap closes for a while by design)."""
    f = os.path.join(RUNS, run, 'log.jsonl')
    if not os.path.exists(f): return None
    L = [json.loads(l) for l in open(f)]
    if not L: return None
    last = L[-1]
    if last['loss'] != last['loss']: return 'loss is NaN'
    D = [r for r in L if 'drift' in r]
    if not lenient and last['it'] >= 800 and len(D) >= 3:
        gaps = [d['drift']['score_noF'] - d['drift']['score_F'] for d in D[-3:]]
        if all(g <= 0.15 for g in gaps): return f'F-vs-noF gap closed for three checkpoints ({[round(g,2) for g in gaps]})'
    stage_lines = [r for r in L if r['stage'] == last['stage']]
    if len(stage_lines) >= 50:
        base = BASELINE.get(float(last['t_out']), 4.3)
        recent = [r['running'] for r in stage_lines[-50:]]
        if min(recent) >= 0.92 * base and last['it'] - stage_lines[0]['it'] >= 500: return f'score stuck at the random baseline for 500 iterations (min running {min(recent):.2f} vs baseline {base})'
    return None


def best_checkpoint(run):
    """The saved checkpoint at the final stage with the lowest frozen F-allowed score in the drift check."""
    L = [json.loads(l) for l in open(os.path.join(RUNS, run, 'log.jsonl'))]
    D = [r for r in L if 'drift' in r]
    if not D: return None
    final_stage = D[-1]['stage']
    cands = [r for r in D if r['stage'] == final_stage and os.path.exists(os.path.join(RUNS, run, f"ckpt_{r['it']:05d}.pt"))]
    if not cands: return None
    b = min(cands, key=lambda r: r['drift']['score_F'])
    return f"ckpt_{b['it']:05d}.pt", b['it'], b['drift']['score_F']


def run_test(run, ckpt, t_out, tag):
    out = os.path.join(RUNS, run, f'test_{tag}.json')
    r = subprocess.run([sys.executable, os.path.join(HERE, 'test.py'), '--ckpt', os.path.join(RUNS, run, ckpt), '--t_out', str(t_out), '--out', out], capture_output=True, text=True)
    if r.returncode != 0: say(f'test failed for {run} {ckpt} @ {t_out}: {r.stderr[-400:]}'); return None
    T = json.load(open(out)); return dict(ckpt=ckpt, t_out=t_out, bars=T['bars'], n_tuned=T['tuning']['n_tuned'], file=os.path.basename(out))


def execute(entry):
    run = entry['run']; args = entry['args']; os.makedirs(os.path.join(RUNS, run), exist_ok=True)
    json.dump(entry, open(os.path.join(RUNS, run, 'entry.json'), 'w'), indent=1)
    say(f"starting {run}: knob = {entry.get('knob')}; parent = {entry.get('parent')}")
    proc = subprocess.Popen([sys.executable, '-u', os.path.join(HERE, 'train.py'), '--run', run] + args,
                            stdout=open(os.path.join(RUNS, run + '.out'), 'a'), stderr=subprocess.STDOUT)
    stopped = None; t0 = time.time()
    while proc.poll() is None:
        time.sleep(60)
        why = stop_rules(run, lenient=bool(entry.get('lenient')))
        if why:
            stopped = why; say(f'{run}: stopping early: {why}'); proc.terminate(); time.sleep(3); break
    minutes = (time.time() - t0) / 60
    final = os.path.join(RUNS, run, 'final.pt')
    if not os.path.exists(final):                        # stopped early or crashed: test the last checkpoint instead
        cks = sorted(glob.glob(os.path.join(RUNS, run, 'ckpt_*.pt')))
        if cks: final_name = os.path.basename(cks[-1])
        else: say(f'{run}: no checkpoint to test'); final_name = None
    else: final_name = 'final.pt'
    tests = []
    if final_name:
        for t_out in entry.get('test_t_outs', [20]):
            r = run_test(run, final_name, t_out, f'final_{int(t_out)}');
            if r: tests.append(r)
        b = best_checkpoint(run)
        if b and b[0] != final_name:
            t_out = entry.get('test_t_outs', [20])[-1]
            r = run_test(run, b[0], t_out, f'best_{int(t_out)}')
            if r: r['drift_F'] = b[2]; tests.append(r)
    result = dict(run=run, knob=entry.get('knob'), parent=entry.get('parent'), prediction=entry.get('prediction'), args=args,
                  minutes=round(minutes, 1), stopped_early=stopped, tests=tests, finished=time.time())
    json.dump(result, open(os.path.join(RUNS, run, 'results.json'), 'w'), indent=1)
    with open(LOG, 'a') as f: f.write(json.dumps(result) + '\n')
    say(f'{run} done in {minutes:.0f} min; ' + '; '.join(f"{t['ckpt']}@{t['t_out']}s A {t['bars']['A']['score']:.2f} B {t['bars']['B']['score']:.2f} C {t['bars']['C']['score']:.2f}" for t in tests))


if __name__ == '__main__':
    say('campaign driver up'); idle_since = None
    while True:
        q = load(QUEUE, [])
        if q:
            entry = q.pop(0); json.dump(q, open(QUEUE, 'w'), indent=1); idle_since = None
            try: execute(entry)
            except Exception as e: say(f'error in {entry.get("run")}: {e!r}')
            continue
        if idle_since is None: idle_since = time.time(); say('queue empty; waiting for the supervisor')
        if time.time() - idle_since > FALLBACK_AFTER:
            fb = load(FALLBACK, [])
            if fb:
                entry = fb.pop(0); json.dump(fb, open(FALLBACK, 'w'), indent=1); say(f"no supervisor for {FALLBACK_AFTER//60} min: using fallback {entry['run']}"); idle_since = None
                try: execute(entry)
                except Exception as e: say(f'error in {entry.get("run")}: {e!r}')
                continue
        time.sleep(30)
