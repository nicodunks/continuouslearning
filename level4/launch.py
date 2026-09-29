"""launch.py  –  start one level 4 run: write its entry.json (arm, knob, arguments, prediction) first, then
start train4.py in the background pinned to one thread.

    python3 level4/launch.py NAME ARM "PREDICTION" -- <train4 arguments>
"""
import json, os, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
name, arm, prediction = sys.argv[1], sys.argv[2], sys.argv[3]
args = sys.argv[sys.argv.index('--') + 1:]
d = os.path.join(HERE, 'runs', name); os.makedirs(d, exist_ok=True)
json.dump(dict(run=name, arm=arm, args=args, prediction=prediction, started=time.strftime('%Y-%m-%d %H:%M:%S')),
          open(os.path.join(d, 'entry.json'), 'w'), indent=1)
env = dict(os.environ, OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
p = subprocess.Popen([sys.executable, '-u', os.path.join(HERE, 'train4.py'), '--run', name] + args,
                     stdout=open(os.path.join(HERE, 'runs', name + '.out'), 'a'), stderr=subprocess.STDOUT, env=env,
                     start_new_session=True)
print(name, 'pid', p.pid)
