"""train4.py  –  level 4: level3/train.py with one switch, --arch (fw | twin | gru), plus --surgery (make a TWIN
from a trained FW checkpoint) and one processor thread per run.  Everything else, including the loss, the
curriculum, the promotion rule, logging and checkpoints, is level 3's trainer line for line.

(level 3's docstring follows)
train.py  –  train FlyNet with a curriculum, logging everything the dashboard shows.

    python3 train.py --run run1            (resumes from the last checkpoint if one exists)

Plan (level3-plan): stages of 10 s then 20 s wander, batch 32, 3,000 iterations in all, Adam 1e-3,
gradient clipping 1.0, two trips per episode.  Promote to the next stage when the running-mean score
(last 50 iterations) is under 1.5, or after the stage's iteration cap.
Every 10 iterations: one log line.  Every 100: a checkpoint, the drift check (frozen score with F
allowed vs F held at zero, on fresh trips), and a recorded sample trip for the gate plots.
"""
import argparse, json, os, sys, time, torch
torch.set_num_threads(1)
HERE4 = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE4, '..', 'level3'))
from world import run_episode
from flynet import FlyNet
from nets import TwinNet, GRURef

p = argparse.ArgumentParser()
p.add_argument('--run', default='run1'); p.add_argument('--iters', type=int, default=3000)
p.add_argument('--batch', type=int, default=32); p.add_argument('--stages', default='10,20')
p.add_argument('--stage_cap', type=int, default=1500); p.add_argument('--promote', type=float, default=1.5)
p.add_argument('--lr', type=float, default=1e-3); p.add_argument('--neurons', type=int, default=64)
p.add_argument('--use_fast', type=int, default=1); p.add_argument('--init', default='')
p.add_argument('--erase_penalty', type=float, default=0.05)   # the exam's charge for erasing with no food present
p.add_argument('--food_stand', type=float, default=0.5)       # seconds at food per trip; more ticks of food = more signal for the erase gate
p.add_argument('--trips', type=int, default=2)                # trips per episode; more trips = a dirty board hurts more
p.add_argument('--speed_profile', default='drift')            # 'drift' or 'legs' (slow half / fast half)
p.add_argument('--f_max', type=float, default=1.0)            # tally ceiling on F
p.add_argument('--lr_decay', type=int, default=0)             # 1 = cosine decay of the learning rate over the run (hygiene)
p.add_argument('--seed', type=int, default=0)                 # seed for the initial network
p.add_argument('--rule', default='hebb')                    # 'hebb' or 'delta' (Peter's note, docs/flynet-delta-rule.md)
p.add_argument('--f_penalty', type=float, default=0.0)      # campaign 2: charge on the mean square of F at the end of the episode (0 = off, every run before run 26)
p.add_argument('--erase_bias_shift', type=float, default=0.0) # added to the erase gate's bias after loading: moves the gate out of the flat part of the sigmoid
p.add_argument('--arch', default='fw')                       # level 4: fw | twin | gru
p.add_argument('--surgery', default='')                      # level 4: FW checkpoint to turn into a TWIN
p.add_argument('--gate_bias', type=float, default=None)     # round 3: starting bias of the twin's hold gate (-5 = FW's erase-gate start) / GRU update gate (sign flipped)
p.add_argument('--gate_split', type=int, default=0)          # round 3 amendment 11:15: half the twin's neurons start fast (hold-gate bias +5,
                                                             # like FW's neurons), half start slow (bias -5, like FW's board)
p.add_argument('--ws_init', type=float, default=None)      # round 4: FW write strength at the start (0 = no head start: the board starts empty)
p.add_argument('--headstart', type=int, default=0)          # round 4: twin with 16 neurons wired as slow heading counters at the start (after round 6: a number > 1 wires that many)
p.add_argument('--att_sharp', type=float, default=1.0)     # after round 6 (the dial): transformer query and key weights multiplied by this at birth
p.add_argument('--grade_mix', default='')                   # round 4: 'tau,w' = smooth closest approach + w x last-10-s grade
p.add_argument('--erase_rows', type=int, default=0)         # round 6: per-neuron forget (FW designs)
p.add_argument('--direct_read', type=int, default=0)        # round 6: board read straight to the turn (FW designs)
p.add_argument('--aux', type=float, default=0.0)            # level 4 diagnostic: weight of a charge on a linear readout's guess of the
                                                             # home vector at every wander tick (dense supervision, as in Cueva & Wei 2018)
p.add_argument('--recenter_turn', type=int, default=0)       # level 4 amendment 08:45: after surgery, move the turn output's bias so
                                                             # the operated twin starts steering straight on average (FW's turn readout
                                                             # was balanced by the board; without it the twin starts at full lock)
args = p.parse_args()

RUN = os.path.join(HERE4, 'runs', args.run); os.makedirs(RUN, exist_ok=True)
LOG = os.path.join(RUN, 'log.jsonl'); CK = os.path.join(RUN, 'ckpt.pt'); STATUS = os.path.join(RUN, 'status.json')
stages = [float(s) for s in args.stages.split(',')]

torch.manual_seed(int(args.seed))
if args.arch == 'fw': net = FlyNet(n=args.neurons, use_fast=bool(args.use_fast), f_max=args.f_max, rule=args.rule)
elif args.arch == 'twin': net = TwinNet.from_fw(torch.load(args.surgery)['net']) if args.surgery else TwinNet(n=args.neurons, gate_bias=args.gate_bias or 0.0)
elif args.arch.startswith(('fw_', 'kvq_')) or args.arch in ('mamba', 'transformer'):
    from nets import build as _build
    net = _build(args.arch, vars(args))
else:
    net = GRURef()
    if args.gate_bias is not None:   # PyTorch GRU: h' = (1 - z) n + z h, gates ordered (r, z, n); hold by default = z near 1
        with torch.no_grad(): h = net.h; net.cell.bias_ih[h:2*h].fill_(-args.gate_bias); net.cell.bias_hh[h:2*h].zero_()
if args.arch == 'twin' and args.surgery and args.recenter_turn:
    _pre = []; _st = net.step
    def _h(inp, active=None):
        o = _st(inp, active); _pre.append(net.W_out(net.x)[:, 0].detach()); return o
    net.step = _h
    with torch.no_grad(): run_episode(net, batch=128, t_out=float(args.stages.split(',')[0]), seed=99, food_stand=args.food_stand, speed_profile=args.speed_profile)
    net.step = _st
    with torch.no_grad(): _m = float(torch.stack(_pre).mean()); net.W_out.bias[0] -= _m
    print('turn output re-centred by', -_m, flush=True)
if args.aux > 0: net.aux = torch.nn.Linear(net.d if args.arch == 'transformer' else (net.h if hasattr(net, 'h') and isinstance(net.h, int) else net.n), 2)
if args.arch == 'twin' and args.gate_split:
    with torch.no_grad(): h = net.n // 2; net.V.bias[:h] = 5.0; net.V.bias[h:] = -5.0
if args.ws_init is not None and args.arch == 'fw':
    with torch.no_grad(): net.ws.fill_(args.ws_init)
if args.headstart and args.arch == 'twin':
    import math as _m
    with torch.no_grad():
        kc = args.headstart if args.headstart > 1 else 16
        for i in range(kc):                          # neuron i counts time spent facing direction phi_i
            ph = 2 * _m.pi * i / kc
            net.W_in.weight[i] = torch.tensor([_m.cos(ph), _m.sin(ph), 0.0, 0.0]); net.W_in.bias[i] = 0.0
            net.W[i] = 0.0; net.U[i] = 0.0; net.V.weight[i] = 0.0; net.V.bias[i] = -5.3   # hold gate ~0.005: keeps 99.5% per tick
if args.att_sharp != 1.0 and args.arch == 'transformer':
    with torch.no_grad(): net.Wq.weight.mul_(args.att_sharp); net.Wk.weight.mul_(args.att_sharp)
print('arch', args.arch, 'trainable numbers', sum(q.numel() for q in net.parameters() if q.requires_grad), flush=True)
opt = torch.optim.Adam([q for q in net.parameters() if q.requires_grad], lr=args.lr)
state = dict(it=0, stage=0, stage_start=0, recent=[])
if args.init and os.path.exists(args.init):                     # run 2 starts from run 1's weights
    net.load_state_dict(torch.load(args.init)['net'], strict=False); print('initialised from', args.init)
if args.erase_bias_shift and args.arch == 'fw':
    with torch.no_grad(): net.W_out.bias[2] += args.erase_bias_shift
    print('erase gate bias shifted by', args.erase_bias_shift, '-> resting erase', float(torch.sigmoid(net.W_out.bias[2])))
if os.path.exists(CK):                                          # resume
    ck = torch.load(CK); net.load_state_dict(ck['net']); opt.load_state_dict(ck['opt']); state = ck['state']
    print('resumed at iteration', state['it'])


def drift_check(t_out, seed):
    """Frozen network on fresh trips: F allowed vs F held at zero.  The gap is where the memory lives."""
    with torch.no_grad():
        kw = dict(food_stand=args.food_stand, trips=args.trips, speed_profile=args.speed_profile)
        a = run_episode(net, batch=64, t_out=t_out, seed=seed, **kw)
        net.zero_F = True
        b = run_episode(net, batch=64, t_out=t_out, seed=seed, **kw)
        net.zero_F = False
        rec = run_episode(net, batch=1, t_out=t_out, seed=seed + 1, record=True, **kw)
    return dict(score_F=a['score'], arrived_F=a['arrived'], score_noF=b['score'], arrived_noF=b['arrived'], traces=rec['traces'])


def write_status(msg):
    json.dump(dict(it=state['it'], stage=state['stage'], t_out=stages[min(state['stage'], len(stages)-1)],
                   iters=args.iters, msg=msg, time=time.time(), pid=os.getpid()), open(STATUS, 'w'))


write_status('running')
t_last = time.time()
while state['it'] < args.iters:
    it = state['it']; t_out = stages[min(state['stage'], len(stages) - 1)]
    if args.lr_decay:
        import math as _m
        for g_ in opt.param_groups: g_['lr'] = args.lr * 0.5 * (1 + _m.cos(_m.pi * it / max(1, args.iters)))
    _gm = tuple(float(v) for v in args.grade_mix.split(',')) if args.grade_mix else None
    r = run_episode(net, batch=args.batch, t_out=t_out, seed=10000 + it + 1000000 * int(args.seed), erase_penalty=args.erase_penalty, food_stand=args.food_stand, trips=args.trips, speed_profile=args.speed_profile, grade_mix=_gm)
    if args.aux > 0: r['loss'] = r['loss'] + args.aux * r['aux_loss']
    loss = r['loss'] + (args.f_penalty * net.F.pow(2).mean() if args.f_penalty > 0 and args.arch == 'fw' else 0.0)
    opt.zero_grad(); loss.backward()
    torch.nn.utils.clip_grad_norm_(net.parameters(), 1.0); opt.step()
    state['recent'] = (state['recent'] + [r['score']])[-50:]
    running = sum(state['recent']) / len(state['recent'])
    # ---- promotion ----
    if state['stage'] < len(stages) - 1 and len(state['recent']) == 50 and \
       (running < args.promote or it - state['stage_start'] >= args.stage_cap):
        state['stage'] += 1; state['stage_start'] = it + 1; state['recent'] = []
        print(f'iteration {it}: promoted to stage {state["stage"]} ({stages[state["stage"]]} s)')
    state['it'] = it + 1
    # ---- logging ----
    if it % 10 == 0:
        now = time.time(); sec = (now - t_last) / 10 if it else now - t_last; t_last = now
        with torch.no_grad():
            rec = dict(it=it, stage=state['stage'], t_out=t_out, loss=float(r['loss']), score=r['score'], arrived=r['arrived'],
                       running=running, sec_per_iter=sec, ws=float(getattr(net, 'ws', 0.0)), A_abs=float(net.A.abs().mean()) if hasattr(net, 'A') else 0.0, W_abs=float(net.W.abs().mean()) if hasattr(net, 'W') else 0.0)
        if it % 100 == 0:
            rec['drift'] = drift_check(t_out, seed=777 + it)
            torch.save(dict(net=net.state_dict(), opt=opt.state_dict(), state=state, args=vars(args), t_out=t_out), CK)
            torch.save(dict(net=net.state_dict(), t_out=t_out, it=it, args=vars(args)), os.path.join(RUN, f'ckpt_{it:05d}.pt'))
            print(f"it {it:5d} stage {state['stage']} t_out {t_out:.0f}  loss {rec['loss']:.2f} score {rec['score']:.2f} run {running:.2f}  "
                  f"drift F {rec['drift']['score_F']:.2f} noF {rec['drift']['score_noF']:.2f}  {sec:.2f}s/it", flush=True)
        with open(LOG, 'a') as f: f.write(json.dumps(rec) + '\n')
        write_status('running')

torch.save(dict(net=net.state_dict(), opt=opt.state_dict(), state=state, args=vars(args), t_out=stages[-1]), CK)
torch.save(dict(net=net.state_dict(), t_out=stages[-1], it=state['it'], args=vars(args)), os.path.join(RUN, 'final.pt'))
write_status('finished'); print('finished')
