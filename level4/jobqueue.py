"""jobqueue.py - run shell commands in order, keeping at most N level-4 training/benchmark processes running on the
whole machine (counted with pgrep, so jobs started elsewhere count too).   python3 level4/jobqueue.py jobs.txt 14"""
import subprocess, sys, time, os
jobs = [l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]; N = int(sys.argv[2])
env = dict(os.environ, OMP_NUM_THREADS='1'); procs = []
def busy():
    r = subprocess.run("pgrep -f '^[^ ]*[Pp]ython[0-9.]* level4/(train4|bench)[.]py' | wc -l", shell=True, capture_output=True, text=True)
    return int(r.stdout.strip() or 0)
while jobs or any(p.poll() is None for p in procs):
    while jobs and busy() < N:
        cmd = jobs.pop(0); procs.append(subprocess.Popen(cmd, shell=True, env=env)); print(time.strftime('%H:%M:%S'), 'start', cmd[:110], flush=True); time.sleep(2)
    time.sleep(10)
print(time.strftime('%H:%M:%S'), 'all done', flush=True)
