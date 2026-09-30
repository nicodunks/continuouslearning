"""bench.py  -  round 6, experiment E2: path integration as a memory benchmark, with no steering (so no spinning).
Each design plus a straight-line readout (memory -> 2 numbers) is trained to report the home vector at every tick of
30 s walks (dense supervision, as Cueva & Wei 2018 and Banino et al. 2018 trained path integrators). Then, frozen, it is
tested on 500 fresh walks: 30, 60 and 90 s; 30 s of walking with a 30 s stop in the middle; a drifting compass (0.15).
Walks follow the world's wander statistics (level3/world.py, steady-speed profile): heading noise 0.8 rad per root-second,
speed drifting in 0.3-1.7 with random 1-3 s pauses. Error = distance between readout and true home vector.
    python3 level4/bench.py --arch kvq_gdelta --seed 0      -> level4/bench/<arch>_s<seed>.json
"""
import argparse, json, math, os, sys, time, torch
torch.set_num_threads(1)
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'level3'))
from nets import build, TwinNet, GRURef
from flynet import FlyNet
DT = 0.1

def walks(batch, T, seed, stop=None, drift=0.0):
    """Yield (inputs [batch,4], true home vector [batch,2], moving mask) tick by tick."""
    g = torch.Generator().manual_seed(seed); rn = lambda *s: torch.randn(*s, generator=g); ru = lambda *s: torch.rand(*s, generator=g)
    pos = torch.zeros(batch, 2); hd = ru(batch) * 2 * math.pi; speed = torch.ones(batch); pause = torch.zeros(batch, dtype=torch.long); comp = torch.zeros(batch)
    for k in range(int(round(T / DT))):
        t = k * DT
        in_p = pause > 0; pause = torch.where(in_p, pause - 1, pause)
        sp = (~in_p) & (ru(batch) < 0.02); pause = torch.where(sp, (ru(batch) * 2 + 1).div(DT).long(), pause)
        speed = (speed + 0.3 * rn(batch) * math.sqrt(DT) + 0.2 * (1 - speed) * DT).clamp(0.3, 1.7)
        s = torch.where(in_p, torch.zeros(batch), speed)
        if stop and stop[0] <= t < stop[0] + stop[1]: s = torch.zeros(batch)
        comp = comp + drift * rn(batch) * math.sqrt(DT)
        inp = torch.stack([torch.cos(hd + comp), torch.sin(hd + comp), s, torch.zeros(batch)], 1)
        yield inp, -pos.clone()
        hd = hd + 0.8 * rn(batch) * math.sqrt(DT)
        pos = pos + torch.stack([s * DT * torch.cos(hd), s * DT * torch.sin(hd)], 1)

def make(arch):
    if arch == 'twin': return TwinNet()
    if arch == 'gru': return GRURef()
    return build(arch)

def state_dim(net, arch):
    return {'transformer': 32, 'gru': 52}.get(arch, 64)

def run(net, head, batch, T, seed, stop=None, drift=0.0, train=True):
    net.reset_fast(batch); net.reset_activity(); errs, sq = [], []
    for inp, home in walks(batch, T, seed, stop, drift):
        net.step(inp); pred = head(net.x)
        d2 = ((pred - home) ** 2).sum(1); sq.append(d2.mean())
        if not train: errs.append(d2.detach().sqrt())
    return torch.stack(sq).mean(), (torch.stack(errs) if errs else None)

if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--arch', required=True); p.add_argument('--seed', type=int, default=0)
    p.add_argument('--iters', type=int, default=1500); p.add_argument('--lr', type=float, default=1e-3)
    a = p.parse_args(); torch.manual_seed(a.seed)
    net = make(a.arch); head = torch.nn.Linear(state_dim(net, a.arch), 2)
    params = list(net.parameters()) + list(head.parameters()); opt = torch.optim.Adam(params, lr=a.lr)
    os.makedirs(os.path.join(HERE, 'bench'), exist_ok=True); out = os.path.join(HERE, 'bench', f'{a.arch}_s{a.seed}.json')
    t0 = time.time(); curve = []
    for it in range(a.iters):
        for g_ in opt.param_groups: g_['lr'] = a.lr * 0.5 * (1 + math.cos(math.pi * it / a.iters))
        loss, _ = run(net, head, 32, 30.0, 100000 * (a.seed + 1) + it)
        opt.zero_grad(); loss.backward(); torch.nn.utils.clip_grad_norm_(params, 1.0); opt.step()
        if it % 50 == 0: curve.append([it, round(float(loss), 4)]); print(it, round(float(loss), 3), f'{time.time() - t0:.0f}s', flush=True)
    res = dict(arch=a.arch, seed=a.seed, params=sum(q.numel() for q in net.parameters() if q.requires_grad), curve=curve, tests={})
    net.eval()
    with torch.no_grad():
        for name, T, stop, drift in [('walk30', 30., None, 0.), ('walk60', 60., None, 0.), ('walk90', 90., None, 0.),
                                     ('stop30', 60., (15., 30.), 0.), ('drift15', 30., None, 0.15)]:
            _, E = run(net, head, 500, T, 777, stop, drift, train=False)
            res['tests'][name] = dict(end=round(float(E[-1].mean()), 3), by10s=[round(float(E[k].mean()), 3) for k in range(99, E.shape[0], 100)])
            print(name, res['tests'][name]['end'], flush=True)
    json.dump(res, open(out, 'w'), indent=1)
