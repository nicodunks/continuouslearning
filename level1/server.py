"""server.py  –  a tiny local web app around the level 1 search.

    python3 level1/server.py        then open  http://localhost:8765

Only the Python standard library plus numpy.  The page (index.html) talks to these routes:
    GET  /               the page
    GET  /api/state      current generation, config, and the whole history (for the chart)
    GET  /api/code       the source of sim.py, search.py, server.py, index.html (to show on the page)
    POST /api/reset      body: JSON config  ->  start a fresh evolution with that config
    POST /api/step       body: {"n": 1}     ->  run n generations, return new records
"""
import json, os, sys
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from search import Evolution

STATE = {'evo': Evolution()}
FILES = ['sim.py', 'search.py', 'server.py', 'index.html']


class Handler(BaseHTTPRequestHandler):
    def _send(self, body, ctype='application/json'):
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        self.send_response(200); self.send_header('Content-Type', ctype)
        self.send_header('Content-Length', str(len(data))); self.end_headers(); self.wfile.write(data)

    def _body(self):
        n = int(self.headers.get('Content-Length', 0))
        return json.loads(self.rfile.read(n) or b'{}')

    def do_GET(self):
        if self.path in ('/', '/index.html'):
            with open(os.path.join(HERE, 'index.html'), 'rb') as f: self._send(f.read(), 'text/html; charset=utf-8')
        elif self.path == '/api/state':
            self._send(STATE['evo'].state())
        elif self.path == '/api/code':
            self._send({f: open(os.path.join(HERE, f)).read() for f in FILES})
        else:
            self.send_response(404); self.end_headers()

    def do_POST(self):
        if self.path == '/api/reset':
            STATE['evo'] = Evolution(self._body())
            self._send(STATE['evo'].state())
        elif self.path == '/api/step':
            n = int(self._body().get('n', 1))
            recs = [STATE['evo'].step() for _ in range(n)]
            self._send(dict(records=recs, gen=STATE['evo'].gen))
        else:
            self.send_response(404); self.end_headers()

    def log_message(self, fmt, *args):
        sys.stderr.write('%s %s\n' % (self.command, self.path))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8765))
    print(f'Level 1 search running at http://localhost:{port}')
    ThreadingHTTPServer(('127.0.0.1', port), Handler).serve_forever()
