"""probe.py  –  level 4: look inside the frozen networks during the long stop (condition 4).

For each network, one 200-agent episode of the 30 s stop condition (walk 15 s, stand 30 s, walk 15 s) with
hooks on every tick, then two numbers per phase (walking before the stop, standing, walking after):
    TWIN   the hold gate u, averaged over neurons (0 = hold exactly, 1 = replace)
    FW     the erase gate (how much of the board fades per tick) and the write gate
and for both, how much the memory changes per tick while standing:
    TWIN   mean |x_new − x_old| over neurons;  FW   mean |F_new − F_old| over the board.
Also: how far the whole memory moved between the last tick before the stop and the last tick of it, as a
share of its size before (0% = held perfectly), so "did the count survive the stop" is measured directly,
not only through the score.

    python3 level4/probe.py --brains level4/brains.json --out level4/probe.json
"""
import argparse, json, math, os, sys, torch
torch.set_num_threads(1)
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
sys.path.insert(0, os.path.join(ROOT, 'level3')); sys.path.insert(0, HERE)
from world import run_episode, DT
from nets import load

STOP = (15.0, 30.0); T_OUT = 60.0


def probe(net):
    is_fw = hasattr(net, 'A')
    rec = dict(t=[], gate=[], write=[], change=[])
    mem = {}; vec = {'v': None}; home = {}
    orig = net.step
    def hooked(inp, active=None):
        old = (net.F.clone() if is_fw else net.x.clone())
        out = orig(inp, active)
        step = inp[:, 2:3] * inp[:, 0:2] * DT                  # what the inputs say was walked this tick
        vec['v'] = step if vec['v'] is None else vec['v'] + step
        new = net.F if is_fw else net.x
        k = len(rec['t']); rec['t'].append(k * DT)
        rec['gate'].append(float(out[2].mean()) if is_fw else (float(net.u.mean()) if hasattr(net, 'u') else float('nan')))
        rec['write'].append(float(out[1].mean()) if is_fw else 0.0)
        rec['change'].append(float((new - old).abs().mean()))
        for tag, tk in (('before', int(STOP[0] / DT) - 1), ('after', int((STOP[0] + STOP[1]) / DT) - 1)):
            if k == tk: mem[tag] = (net.F.flatten(1) if is_fw else net.x).clone(); home[tag] = vec['v'].clone()
        return out
    net.step = hooked
    run_episode(net, batch=600, t_out=T_OUT, trips=1, seed=4242, stop=STOP)
    net.step = orig
    return rec, mem, home


def decode(mem, home, lam):
    """Fit a straight-line readout of the home vector from the memory just before the stop, on half the flies;
    score it on the other half, before the stop and at its end (same readout, nothing walked in between).
    Returns the typical readout error in walking units, before and after."""
    Xb, Xa, Y = mem['before'], mem['after'], home['before']
    n = len(Y) // 2
    add1 = lambda X: torch.cat([X, torch.ones(len(X), 1)], 1)
    A = add1(Xb[:n]); W = torch.linalg.solve(A.T @ A + lam * torch.eye(A.shape[1]), A.T @ Y[:n])
    err = lambda X: float(((add1(X[n:]) @ W - Y[n:]) ** 2).sum(1).mean().sqrt())
    walked = float(Y[n:].norm(dim=1).mean())
    B = add1(Xa[:n]); W2 = torch.linalg.solve(B.T @ B + lam * torch.eye(B.shape[1]), B.T @ Y[:n])   # readout refitted after the stop
    refit = float(((add1(Xa[n:]) @ W2 - Y[n:]) ** 2).sum(1).mean().sqrt())
    return dict(before=err(Xb), after=err(Xa), after_refit=refit, walked=walked)


if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--brains', required=True); p.add_argument('--out', required=True)
    a = p.parse_args()
    out = {}
    with torch.no_grad():
        for b in json.load(open(a.brains)):
            if b['ckpt'] in ('hand', 'random'): continue
            net = load(os.path.join(ROOT, b['ckpt']))
            rec, mem, home = probe(net)
            t = torch.tensor(rec['t']); g = torch.tensor(rec['gate']); w = torch.tensor(rec['write']); c = torch.tensor(rec['change'])
            walk1 = (t > 1) & (t < STOP[0]); stand = (t >= STOP[0] + 1) & (t < STOP[0] + STOP[1]); walk2 = (t >= STOP[0] + STOP[1]) & (t < T_OUT)
            ph = lambda v: dict(walk_before=float(v[walk1].mean()), standing=float(v[stand].mean()), walk_after=float(v[walk2].mean()))
            drift = float((mem['after'] - mem['before']).abs().mean() / (mem['before'].abs().mean() + 1e-9))
            dec = decode(mem, home, lam=1.0 if mem['before'].shape[1] > 500 else 1e-2)
            out[b['name']] = dict(arm=b['arm'], decode=dec, gate=ph(g), write=ph(w), change_per_tick=ph(c), memory_moved_during_stop=drift,
                                  trace=dict(t=rec['t'][::5], gate=rec['gate'][::5], change=rec['change'][::5]))
            print(f"{b['name']:14s} gate walk {out[b['name']]['gate']['walk_before']:.4f} stand {out[b['name']]['gate']['standing']:.4f}   "
                  f"change/tick walk {out[b['name']]['change_per_tick']['walk_before']:.5f} stand {out[b['name']]['change_per_tick']['standing']:.5f}   "
                  f"memory moved {drift*100:.1f}%   decode error before {dec['before']:.2f} after {dec['after']:.2f} refit {dec['after_refit']:.2f} (walked {dec['walked']:.2f})", flush=True)
    json.dump(out, open(a.out, 'w'), indent=1)
