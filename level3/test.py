"""test.py  –  freeze a checkpoint and ask where the memory lives, then look inside.

    python3 test.py --ckpt runs/run1/final.pt --t_out 20 --out runs/run1/test.json

Three brains on the same 200 trips (same seed):
    A  the trained network, F allowed
    B  the same network, F held at zero every tick
    C  a random walk (a brain whose turn is always zero)
Then the look-inside pictures, saved as JSON for the dashboard:
    tuning     each neuron's mean activity in 16 heading bins (built its own compass cells?)
    F traces   the fast strengths on the 12 highest-|A| connections over one trip (a tally board?)
    gates      write and erase over one trip next to speed and food
    A heatmap  the allowance table itself: where training put the memory
"""
import argparse, json, math, torch
from world import run_episode, DT
from flynet import FlyNet

p = argparse.ArgumentParser()
p.add_argument('--ckpt', required=True); p.add_argument('--t_out', type=float, default=20.0)
p.add_argument('--out', required=True); p.add_argument('--batch', type=int, default=200); p.add_argument('--seed', type=int, default=4242)
args = p.parse_args()

ck = torch.load(args.ckpt)
n = ck['net']['W'].shape[0]
net = FlyNet(n=n, f_max=float(ck.get('args', {}).get('f_max', 1.0))); net.load_state_dict(ck['net']); net.eval()


class RandomWalk:
    def reset_fast(self, batch): self.b = batch
    def reset_activity(self): pass
    def step(self, inp, active=None):
        z = torch.zeros(self.b); return z, z, z


with torch.no_grad():
    A_ = run_episode(net, batch=args.batch, t_out=args.t_out, seed=args.seed)
    net.zero_F = True
    B_ = run_episode(net, batch=args.batch, t_out=args.t_out, seed=args.seed)
    net.zero_F = False
    C_ = run_episode(RandomWalk(), batch=args.batch, t_out=args.t_out, seed=args.seed)
    bars = dict(A=dict(score=A_['score'], arrived=A_['arrived']), B=dict(score=B_['score'], arrived=B_['arrived']),
                C=dict(score=C_['score'], arrived=C_['arrived']))

    # ---- look inside: run one recorded episode with hooks on x, F, gates ----
    xs, Fs, gates, hds, speeds, foods, dists = [], [], [], [], [], [], []
    A = net.A.detach()
    idx = torch.topk(A.abs().flatten(), 12).indices
    ii, jj = (idx // n).tolist(), (idx % n).tolist()
    orig_step = net.step
    def hooked(inp, active=None):
        out = orig_step(inp, active)
        xs.append(net.x[0].clone()); Fs.append(torch.stack([net.F[0, i, j] for i, j in zip(ii, jj)]))
        gates.append((float(out[1][0]), float(out[2][0]))); hds.append(math.atan2(float(inp[0, 1]), float(inp[0, 0])))
        speeds.append(float(inp[0, 2])); foods.append(float(inp[0, 3]))
        return out
    net.step = hooked
    rec = run_episode(net, batch=8, t_out=args.t_out, trips=1, seed=args.seed + 9, record=True)
    net.step = orig_step
    X = torch.stack(xs); Fm = torch.stack(Fs)
    # tuning: mean |activity| per neuron per heading bin, only while moving
    bins = ((torch.tensor(hds) % (2 * math.pi)) / (2 * math.pi) * 16).long().clamp(max=15)
    mov = torch.tensor(speeds) > 0
    tuning = torch.zeros(n, 16); cnt = torch.zeros(16)
    for k in range(len(hds)):
        if mov[k]: tuning[:, bins[k]] += X[k]; cnt[bins[k]] += 1
    tuning = tuning / cnt.clamp(min=1)
    # a neuron is direction-tuned if its tuning curve has a clear single bump: resultant length of the curve
    ang = torch.arange(16) * 2 * math.pi / 16
    res = ((tuning - tuning.mean(1, keepdim=True)) * torch.cos(ang)).sum(1) ** 2 + ((tuning - tuning.mean(1, keepdim=True)) * torch.sin(ang)).sum(1) ** 2
    strength = res.sqrt() / (tuning.abs().sum(1) + 1e-9)
    order = torch.argsort(strength, descending=True)

json.dump(dict(
    ckpt=args.ckpt, t_out=args.t_out, batch=args.batch, bars=bars, n=n,
    tuning=dict(curves=tuning[order[:16]].tolist(), strength=strength[order[:16]].tolist(), neurons=order[:16].tolist(),
                n_tuned=int((strength > 0.25).sum()), all_curves=tuning.tolist(), all_strength=strength.tolist()),
    traces=dict(t=[k * DT for k in range(len(hds))], speed=speeds, food=foods, write=[g[0] for g in gates], erase=[g[1] for g in gates],
                dist=rec['traces']['dist'][:len(hds)], F=Fm.t().tolist(), F_conn=[[i, j, float(A[i, j])] for i, j in zip(ii, jj)]),
    A_heat=A.tolist(), A_abs_mean=float(A.abs().mean()), ws=float(net.ws),
), open(args.out, 'w'))
print(json.dumps(bars, indent=1)); print('direction-tuned neurons:', int((strength > 0.25).sum()), 'of', n)
