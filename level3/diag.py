"""diag.py  –  diagnose a checkpoint before spending compute on it (campaign 2, hour 0).

    python3 diag.py --ckpt runs/run19/final.pt --out campaign/diag_run19.json

1. Decode: fit a straight-line readout from the 4,096 fast weights to the true home vector, on half the trips,
   score it on the other half, tick by tick. Tells us whether the count is in F in readable form and where it degrades.
2. Phase split: count error at the turn, heading error in the first 3 s of the return, closest approach, final distance.
3. Lesions: silence the compass cells, the erase drivers, the write drivers at exam time and rerun the exam.
Nothing here trains anything. Same world equations as world.py (one trip, standard world, seed 4242).
"""
import argparse, json, math, torch
from world import run_episode, DT
from flynet import FlyNet

p = argparse.ArgumentParser(); p.add_argument('--ckpt', required=True); p.add_argument('--out', required=True)
p.add_argument('--t_out', type=float, default=30.0); p.add_argument('--batch', type=int, default=128); p.add_argument('--seed', type=int, default=4242)
p.add_argument('--test', default=''); p.add_argument('--hand', type=int, default=0)   # test_*.json with tuning strengths, for the compass-cell lesion
a = p.parse_args()
if a.hand:
    from handbrain import HandBrain; net = HandBrain(); n = 1
else:
    ck = torch.load(a.ckpt); n = ck['net']['W'].shape[0]; ar = ck.get('args', {})
    net = FlyNet(n=n, f_max=float(ar.get('f_max', 1.0)), rule=ar.get('rule', 'hebb')); net.load_state_dict(ck['net']); net.eval()
torch.manual_seed(a.seed)

# ---------- one recorded trip: mirror of world.py's loop, standard world ----------
def trip(batch, seed):
    g = torch.Generator().manual_seed(seed); randn = lambda *s: torch.randn(*s, generator=g); rand = lambda *s: torch.rand(*s, generator=g)
    t_out = a.t_out; t_ret = 2 * t_out; n_ticks = int(round((t_out + t_ret) / DT)); food_ticks = int(round(4.0 / DT))
    net.reset_fast(batch); net.reset_activity()
    pos = torch.zeros(batch, 2); hd = rand(batch) * 2 * math.pi; speed = torch.ones(batch); pause = torch.zeros(batch, dtype=torch.long)
    arrived = torch.zeros(batch, dtype=torch.bool); since = torch.zeros(batch, dtype=torch.long); min_d = torch.full((batch,), 1e9)
    Fs, P, HD, RET = [], [], [], []
    for k in range(n_ticks):
        t = k * DT; returning = t >= t_out; done = since >= food_ticks; active = ~done
        at_food = ((t < 0.5) | arrived) & active; food = at_food.float()
        in_pause = pause > 0; pause = torch.where(in_pause, pause - 1, pause)
        start = (~in_pause) & (rand(batch) < 0.02); pause = torch.where(start, (rand(batch) * 2 + 1).div(DT).long(), pause)
        speed = (speed + 0.3 * randn(batch) * math.sqrt(DT) + 0.2 * (1 - speed) * DT).clamp(0.3, 1.7)
        speed = torch.where(in_pause | at_food | done, torch.zeros(batch), speed)
        inp = torch.stack([torch.cos(hd), torch.sin(hd), speed, food], 1)
        turn, write, erase = net.step(inp, active=active)
        moving = active & ~arrived
        dhd = (turn * DT if returning else torch.zeros(batch)) + 0.8 * randn(batch) * math.sqrt(DT)
        hd = hd + torch.where(moving, dhd, torch.zeros(batch)); step = torch.where(moving, speed * DT, torch.zeros(batch))
        pos = pos + torch.stack([step * torch.cos(hd), step * torch.sin(hd)], 1); d = pos.norm(dim=1)
        if returning: min_d = torch.minimum(min_d, d); arrived = arrived | (d < 0.5)
        since = since + arrived.long()
        if k % 5 == 0: Fs.append((net.F.reshape(batch, -1).clone() if hasattr(net, 'F') and not a.hand else torch.zeros(batch, 1))); P.append(pos.clone()); HD.append(hd.clone()); RET.append(returning)
    return dict(F=torch.stack(Fs), pos=torch.stack(P), hd=torch.stack(HD), ret=RET, min_d=min_d, final_d=d, arrived=arrived)

with torch.no_grad():
    R = trip(a.batch, a.seed + 7)
T, B, D = R['F'].shape
half = B // 2
# ---------- 1. decode the home vector (= -pos) from F, outbound ticks only, ridge regression ----------
out_idx = [i for i, r in enumerate(R['ret']) if not r]
X = R['F'][out_idx][:, :half].reshape(-1, D); Y = (-R['pos'][out_idx][:, :half]).reshape(-1, 2)
Xm = X.mean(0, keepdim=True); Ym = Y.mean(0, keepdim=True); Xc = X - Xm; Yc = Y - Ym
lam = 1e-2 * Xc.pow(2).sum() / D
Wd = torch.linalg.solve(Xc.T @ Xc + lam * torch.eye(D) + 1e-6 * torch.eye(D), Xc.T @ Yc)
def r2(Xe, Ye):
    pred = (Xe - Xm) @ Wd + Ym; ss = ((Ye - pred) ** 2).sum(); st = ((Ye - Ye.mean(0)) ** 2).sum(); return float(1 - ss / st), pred
Xte = R['F'][out_idx][:, half:].reshape(-1, D); Yte = (-R['pos'][out_idx][:, half:]).reshape(-1, 2)
r2_all, _ = r2(Xte, Yte)
by_time = []
for i in out_idx:
    if i % 10: continue
    s, pred = r2(R['F'][i][half:], -R['pos'][i][half:])
    err = (pred - (-R['pos'][i][half:])).norm(dim=1).mean(); true = R['pos'][i][half:].norm(dim=1).mean()
    by_time.append(dict(t=round(i * 5 * DT, 1), r2=round(s, 3), err=round(float(err), 3), true=round(float(true), 3)))
# pinned share of F over time
pinned = [(round(i * 5 * DT, 1), round(float((R['F'][i].abs() > 0.98 * getattr(net, 'f_max', 1.0)).float().mean()), 4)) for i in range(0, T, 10)]
# ---------- 2. phase split ----------
turn_i = out_idx[-1]
_, pred_turn = r2(R['F'][turn_i][half:], -R['pos'][turn_i][half:])
true_home = -R['pos'][turn_i][half:]
count_err = float((pred_turn - true_home).norm(dim=1).mean()); count_rel = float(((pred_turn - true_home).norm(dim=1) / true_home.norm(dim=1)).mean())
# heading error in first 3 s of return: angle between mean heading vector and true home direction
ret_idx = [i for i, r in enumerate(R['ret']) if r][:6]
hv = torch.stack([torch.stack([torch.cos(R['hd'][i]), torch.sin(R['hd'][i])], 1) for i in ret_idx]).mean(0)
home_dir = -R['pos'][turn_i]; home_dir = home_dir / home_dir.norm(dim=1, keepdim=True)
cosang = (hv / hv.norm(dim=1, keepdim=True) * home_dir).sum(1).clamp(-1, 1)
head_err_deg = float(torch.rad2deg(torch.acos(cosang)).mean())
phase = dict(count_err_units=round(count_err, 3), count_err_relative=round(count_rel, 3), heading_err_first3s_deg=round(head_err_deg, 1),
             closest_approach=round(float(R['min_d'].mean()), 3), final_distance=round(float(R['final_d'].mean()), 3), arrived=round(float(R['arrived'].float().mean()), 3),
             distance_at_turn=round(float(R['pos'][turn_i].norm(dim=1).mean()), 3))
# ---------- 3. lesions ----------
def lesion_exam(idx, label):
    idx = torch.tensor(sorted(set(idx)), dtype=torch.long)
    orig = net.step
    def step(inp, active=None):
        turn, w, e = orig(inp, active)
        if len(idx): net.x[:, idx] = 0.0
        return turn, w, e
    net.step = step
    r = run_episode(net, batch=200, t_out=a.t_out, seed=a.seed)
    net.step = orig
    return dict(label=label, n=int(len(idx)), score=round(r['score'], 3), arrived=round(r['arrived'], 3))
les = [] if a.hand else [lesion_exam([], 'no lesion')]
if a.test:
    Tj = json.load(open(a.test)); st = Tj['tuning']['all_strength']
    comp = [i for i in range(n) if st[i] > 0.25]; les.append(lesion_exam(comp, f'silence the {len(comp)} compass cells'))
    noncomp = [i for i in range(n) if st[i] <= 0.25]; les.append(lesion_exam(noncomp, f'silence the {len(noncomp)} non-compass cells'))
Wo = None if a.hand else net.W_out.weight.detach()
for row in ([] if a.hand else [0]):
    pass
for row, name in ([] if a.hand else [(2, 'erase'), (1, 'write')]):
    drv = torch.topk(Wo[row].abs(), 8).indices.tolist(); les.append(lesion_exam(drv, f'silence the 8 strongest {name}-gate drivers'))
import random; random.seed(0)
if not a.hand: les.append(lesion_exam(random.sample(range(n), 8), 'silence 8 random neurons'))
res = dict(ckpt=a.ckpt, t_out=a.t_out, decode=dict(r2_heldout_all_outbound=round(r2_all, 3), by_time=by_time), pinned=pinned, phase=phase, lesions=les)
json.dump(res, open(a.out, 'w'), indent=1)
print(f"decode R² (held-out trips, all outbound ticks): {r2_all:.3f}")
print('time  R²     err   true   pinned'); pin = dict(pinned)
for b in by_time: print(f"{b['t']:5.1f} {b['r2']:6.3f} {b['err']:6.3f} {b['true']:6.3f}  {pin.get(b['t'], float('nan')):.3f}")
print('phase:', json.dumps(phase)); print('lesions:'); [print('  ', l) for l in les]
