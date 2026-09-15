"""server.py  –  the level 3 dashboard.

    python3 level3/server.py        then open  http://localhost:8769

Training runs as its own process (train.py) and writes runs/<run>/log.jsonl; this page only reads.
Routes:
    GET  /                      the dashboard
    GET  /api/runs              list of runs with status
    GET  /api/log?run=run1      the log lines (with drift checks and sample traces)
    GET  /api/test?run=run1     the test.json for that run, if made
    GET  /api/code              sources for the tabs
    POST /api/start   {run, args}   start train.py for a run (resumes if a checkpoint exists)
    POST /api/stop    {run}         stop it (it resumes from its last checkpoint next start)
    POST /api/test    {run, ckpt, t_out}  run test.py on a checkpoint
"""
import json, os, sys, subprocess, glob, time
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

HERE = os.path.dirname(os.path.abspath(__file__)); RUNS = os.path.join(HERE, 'runs')
FILES = ['world.py', 'flynet.py', 'train.py', 'test.py', 'handbrain.py', 'server.py', 'index.html']
PROCS = {}


def run_status(run):
    d = os.path.join(RUNS, run); st = {}
    if os.path.exists(os.path.join(d, 'status.json')):
        try: st = json.load(open(os.path.join(d, 'status.json')))
        except Exception: pass
    alive = run in PROCS and PROCS[run].poll() is None
    if not alive and st.get('pid'):                      # started outside this server? ask the OS
        try: os.kill(int(st['pid']), 0); alive = st.get('msg') == 'running'
        except OSError: alive = False
    if not alive and st.get('msg') == 'running' and time.time() - st.get('time', 0) < 60:
        alive = True                                     # status file is fresh: the trainer is writing it
    if not alive and st.get('msg') == 'running': st['msg'] = 'stopped'
    ckpts = sorted(os.path.basename(f) for f in glob.glob(os.path.join(d, 'ckpt_*.pt')) + glob.glob(os.path.join(d, 'final.pt')))
    return dict(run=run, alive=alive, status=st, ckpts=ckpts, has_test=os.path.exists(os.path.join(d, 'test.json')))


class H(BaseHTTPRequestHandler):
    def _send(self, body, ctype='application/json'):
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        self.send_response(200); self.send_header('Content-Type', ctype); self.send_header('Content-Length', str(len(data))); self.end_headers(); self.wfile.write(data)
    def _body(self):
        n = int(self.headers.get('Content-Length', 0)); return json.loads(self.rfile.read(n) or b'{}')
    def _q(self):
        from urllib.parse import urlparse, parse_qs; u = urlparse(self.path); return u.path, {k: v[0] for k, v in parse_qs(u.query).items()}
    def do_GET(self):
        path, q = self._q()
        if path in ('/', '/index.html'):
            self._send(open(os.path.join(HERE, 'index.html'), 'rb').read(), 'text/html; charset=utf-8')
        elif path == '/api/runs':
            runs = sorted(d for d in os.listdir(RUNS) if os.path.isdir(os.path.join(RUNS, d))) if os.path.exists(RUNS) else []
            self._send([run_status(r) for r in runs])
        elif path == '/api/log':
            f = os.path.join(RUNS, q.get('run', 'run1'), 'log.jsonl')
            lines = [json.loads(l) for l in open(f)] if os.path.exists(f) else []
            self._send(dict(lines=lines, **run_status(q.get('run', 'run1'))))
        elif path == '/api/test':
            f = os.path.join(RUNS, q.get('run', 'run1'), 'test.json')
            self._send(json.load(open(f)) if os.path.exists(f) else {})
        elif path == '/api/code':
            self._send({f: open(os.path.join(HERE, f)).read() for f in FILES})
        else:
            self.send_response(404); self.end_headers()
    def do_POST(self):
        path, _ = self._q(); b = self._body()
        if path == '/api/start':
            run = b.get('run', 'run1'); extra = b.get('args', [])
            if run in PROCS and PROCS[run].poll() is None: self._send(dict(ok=False, msg='already running')); return
            os.makedirs(os.path.join(RUNS, run), exist_ok=True)
            PROCS[run] = subprocess.Popen([sys.executable, '-u', os.path.join(HERE, 'train.py'), '--run', run] + extra,
                                          stdout=open(os.path.join(RUNS, run + '.out'), 'a'), stderr=subprocess.STDOUT)
            self._send(dict(ok=True))
        elif path == '/api/stop':
            run = b.get('run', 'run1')
            if run in PROCS and PROCS[run].poll() is None: PROCS[run].terminate()
            self._send(dict(ok=True))
        elif path == '/api/test':
            run = b.get('run', 'run1'); ck = os.path.join(RUNS, run, b.get('ckpt', 'final.pt')); t_out = str(b.get('t_out', 20))
            out = os.path.join(RUNS, run, 'test.json')
            r = subprocess.run([sys.executable, os.path.join(HERE, 'test.py'), '--ckpt', ck, '--t_out', t_out, '--out', out], capture_output=True, text=True)
            self._send(dict(ok=r.returncode == 0, log=(r.stdout + r.stderr)[-3000:]))
        else:
            self.send_response(404); self.end_headers()
    def log_message(self, *a): pass


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8769)); print(f'Level 3 dashboard at http://localhost:{port}')
    ThreadingHTTPServer(('127.0.0.1', port), H).serve_forever()
