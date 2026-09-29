"""r5_analysis.py  -  round 5: do networks fail at HOLDING the way home or at READING it?
For each network, 600 flies, 10 s wander (one trip), seed 4242:
  exam10 : standard score (closest approach), 200 of the flies' worth of trips is not needed: we use the same 600
  hold   : R^2 of a straight-line readout of the home vector (from the inputs' own running sum) from the memory at the
           last tick before the turn (board F for FW, activity x for the twins); fitted on 300 flies, scored on 300
  read   : heading error, the average angle between where the fly faces and where home is, over seconds 1 to 3 of the
           return (moving flies), using the inputs' running sum for both; 0 deg = heading straight home, 90 deg = chance
Usage: python3 level4/r5_analysis.py  -> r5_results.json"""
import sys, glob, os, json, math, torch, numpy as np, statistics as st
sys.path.insert(0, '.'); sys.path.insert(0, '../level3'); torch.set_num_threads(1)
from nets import load, TwinNet
from flynet import FlyNet
from world import run_episode, DT
T_OUT = 10.0; KT = int(T_OUT / DT)

def analyse(net):
    is_fw = hasattr(net, 'A'); rec = {'v': None, 'mem': None, 'home': None, 'turn': [], 'ideal': [], 'xs': [], 'want': []}
    st0 = net.step
    def h(inp, active=None):
        k = h.k; h.k += 1
        o = st0(inp, active)
        step = inp[:, 2:3] * inp[:, 0:2] * DT
        rec['v'] = step if rec['v'] is None else rec['v'] + step
        if k == KT - 1: rec['mem'] = (net.F.flatten(1) if is_fw else net.x).clone(); rec['home'] = -rec['v'].clone()
        if KT <= k < KT + 30:
            rec['turn'].append(o[0].clone())
            hd0 = torch.atan2(inp[:, 1], inp[:, 0]); hdir0 = torch.atan2(-rec['v'][:, 1], -rec['v'][:, 0])
            rec['xs'].append(net.x.clone()); rec['want'].append(torch.sin(hdir0 - hd0))
        if KT + 10 <= k < KT + 30:
            hd = torch.atan2(inp[:, 1], inp[:, 0]); hdir = torch.atan2(-rec['v'][:, 1], -rec['v'][:, 0])
            err = torch.remainder(hdir - hd + math.pi, 2 * math.pi) - math.pi
            m = (inp[:, 2] > 0) & (rec['v'].norm(dim=1) > 0.5)
            rec['ideal'].append(torch.where(m, err.abs(), torch.full_like(err, float('nan'))))
        return o
    h.k = 0; net.step = h
    with torch.no_grad(): r = run_episode(net, batch=600, t_out=T_OUT, trips=1, seed=4242)
    net.step = st0
    M, Y = rec['mem'], rec['home']; half = 300
    A1 = torch.cat([M[:half], torch.ones(half, 1)], 1); lam = 1.0 if M.shape[1] > 500 else 1e-2
    W = torch.linalg.solve(A1.T @ A1 + lam * torch.eye(A1.shape[1]), A1.T @ Y[:half])
    P = torch.cat([M[half:], torch.ones(len(M) - half, 1)], 1) @ W
    hold = float(1 - ((P - Y[half:]) ** 2).sum() / ((Y[half:] - Y[half:].mean(0)) ** 2).sum())
    tu = torch.stack(rec['turn']).flatten().numpy(); idl = torch.stack(rec['ideal']).flatten().numpy()
    read = float(np.degrees(np.nanmean(idl)))
    # steer: can a straight-line readout of the neurons' activity give the ideal turn, sin(direction home - heading)?
    X = torch.stack(rec['xs']); Wt = torch.stack(rec['want'])          # [ticks, flies, n], [ticks, flies]
    Xtr = X[:, :half].reshape(-1, X.shape[2]); Ytr = Wt[:, :half].reshape(-1, 1)
    Xte = X[:, half:].reshape(-1, X.shape[2]); Yte = Wt[:, half:].reshape(-1, 1)
    B1 = torch.cat([Xtr, torch.ones(len(Xtr), 1)], 1)
    Ws = torch.linalg.solve(B1.T @ B1 + 1e-2 * torch.eye(B1.shape[1]), B1.T @ Ytr)
    Ps = torch.cat([Xte, torch.ones(len(Xte), 1)], 1) @ Ws
    steer = float(1 - ((Ps - Yte) ** 2).sum() / ((Yte - Yte.mean()) ** 2).sum())
    return dict(exam10=round(r['score'], 2), hold=round(hold, 2), steer=round(steer, 2), turn_abs=round(float(np.abs(tu).mean()), 2))

def headstart(t):
    with torch.no_grad():
        for i in range(16):
            ph = 2 * math.pi * i / 16; t.W_in.weight[i] = torch.tensor([math.cos(ph), math.sin(ph), 0., 0.]); t.W_in.bias[i] = 0
            t.W[i] = 0; t.U[i] = 0; t.V.weight[i] = 0; t.V.bias[i] = -5.3
    return t

out = {'groups': {}, 'refs': {}}
for arm in ('fw', 'fwe', 'tw', 'twhs'):
    rows = []
    for d in sorted(glob.glob(f'runs/r5_{arm}_s*')):
        if os.path.isdir(d) and os.path.exists(d + '/final.pt'):
            rows.append(dict(run=os.path.basename(d), **analyse(load(d + '/final.pt'))))
    out['groups'][arm] = rows
    for x in rows: print(f"{x['run']:12s} exam10 {x['exam10']:.2f}  hold R2 {x['hold']:5.2f}  steer R2 {x['steer']:5.2f}  |turn| {x['turn_abs']:.2f}")
torch.manual_seed(0); out['refs']['FW untrained'] = analyse(FlyNet().eval())
torch.manual_seed(0); out['refs']['TWIN untrained'] = analyse(TwinNet().eval())
torch.manual_seed(0); out['refs']['TWIN-HS untrained'] = analyse(headstart(TwinNet()).eval())
out['refs']['TWIN taught (twin_aux0)'] = analyse(load('runs/twin_aux0/final.pt'))
out['refs']['FW run 41'] = analyse(load('../level3/runs/run41/final.pt'))
for k, v in out['refs'].items(): print(f'{k:26s}', v)
json.dump(out, open('r5_results.json', 'w'), indent=1)
