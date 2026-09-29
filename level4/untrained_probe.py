"""untrained_probe.py  -  what does a network hold BEFORE any training?  (paper second pass, 29 Sept)
For untrained FW, TWIN and GRU (3 random seeds each) and trained references:
  1. how many neurons are direction-tuned (same test as level3/test.py: resultant strength > 0.25)
  2. correlation of FW's write gate with speed on the outward walk
  3. can the home vector be read out of the memory at the moment of turning (tick 299 of a 30 s wander)?
     ridge readout fitted on 300 flies, scored on 300 others: R^2 and typical error in walking units
"""
import sys, json, math, torch, numpy as np
torch.set_num_threads(1)
sys.path.insert(0, '.'); sys.path.insert(0, '../level3')
from nets import TwinNet, GRURef, load
from flynet import FlyNet
from world import run_episode

def probe(net):
    is_fw = hasattr(net, 'A'); xs, hs, sp, wr, vec = [], [], [], [], {'v': None}; mem = {}
    st = net.step
    def h(inp, active=None):
        o = st(inp, active); k = len(xs)
        step = inp[:, 2:3] * inp[:, 0:2] * 0.1
        vec['v'] = step if vec['v'] is None else vec['v'] + step
        xs.append(net.x.clone()); hs.append(torch.atan2(inp[:, 1], inp[:, 0])); sp.append(inp[:, 2].clone()); wr.append(o[1].clone())
        if k == 299: mem['m'] = (net.F.flatten(1) if is_fw else net.x).clone(); mem['home'] = vec['v'].clone()
        return o
    net.step = h
    with torch.no_grad(): run_episode(net, batch=600, t_out=30, trips=1, seed=4242)
    net.step = st
    X = torch.stack(xs[5:300]); H = torch.stack(hs[5:300]); S = torch.stack(sp[5:300]); Wg = torch.stack(wr[5:300])
    mov = S > 0
    bins = ((H % (2 * math.pi)) / (2 * math.pi) * 16).long().clamp(max=15)
    n = X.shape[2]; tun = torch.zeros(n, 16); cnt = torch.zeros(16)
    for b in range(16):
        m = mov & (bins == b); cnt[b] = m.sum()
        tun[:, b] = (X * m[..., None]).sum((0, 1)) / m.sum().clamp(min=1)
    ang = torch.arange(16) * 2 * math.pi / 16; c = tun - tun.mean(1, keepdim=True)
    strength = torch.sqrt((c * torch.cos(ang)).sum(1) ** 2 + (c * torch.sin(ang)).sum(1) ** 2) / (tun.abs().sum(1) + 1e-9)
    corr = float(np.corrcoef(Wg[mov].numpy(), S[mov].numpy())[0, 1]) if is_fw else None
    M, Y = mem['m'], mem['home']; half = 300
    A1 = torch.cat([M[:half], torch.ones(half, 1)], 1); lam = 1.0 if M.shape[1] > 500 else 1e-2
    W = torch.linalg.solve(A1.T @ A1 + lam * torch.eye(A1.shape[1]), A1.T @ Y[:half])
    P = torch.cat([M[half:], torch.ones(len(M) - half, 1)], 1) @ W
    r2 = float(1 - ((P - Y[half:]) ** 2).sum() / ((Y[half:] - Y[half:].mean(0)) ** 2).sum())
    err = float(((P - Y[half:]) ** 2).sum(1).mean().sqrt()); dist = float(Y[half:].norm(dim=1).mean())
    return dict(n_tuned=int((strength > 0.25).sum()), n=n, write_speed=corr, r2=round(r2, 3), err=round(err, 2), dist=round(dist, 2))

out = {}
for s in (0, 1, 2):
    torch.manual_seed(s); out[f'FW untrained s{s}'] = probe(FlyNet().eval())
    torch.manual_seed(s); out[f'TWIN untrained s{s}'] = probe(TwinNet().eval())
    torch.manual_seed(s); out[f'GRU untrained s{s}'] = probe(GRURef().eval())
for name, ck in [('FW run41 trained', '../level3/runs/run41/final.pt'), ('TWIN taught (twin_aux0)', 'runs/twin_aux0/final.pt'),
                 ('TWIN spinner (twin_c0_lr1e-3)', 'runs/twin_c0_lr1e-3/final.pt')]:
    out[name] = probe(load(ck))
for k, v in out.items(): print(f'{k:32s}', v)
json.dump(out, open('untrained_probe.json', 'w'), indent=1)
