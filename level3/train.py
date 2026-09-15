"""train.py  –  train FlyNet with a curriculum, logging everything the dashboard shows.

    python3 train.py --run run1            (resumes from the last checkpoint if one exists)

Plan (level3-plan): stages of 10 s then 20 s wander, batch 32, 3,000 iterations in all, Adam 1e-3,
gradient clipping 1.0, two trips per episode.  Promote to the next stage when the running-mean score
(last 50 iterations) is under 1.5, or after the stage's iteration cap.
Every 10 iterations: one log line.  Every 100: a checkpoint, the drift check (frozen score with F
allowed vs F held at zero, on fresh trips), and a recorded sample trip for the gate plots.
"""
import argparse, json, os, time, torch
from world import run_episode
from flynet import FlyNet

p = argparse.ArgumentParser()
p.add_argument('--run', default='run1'); p.add_argument('--iters', type=int, default=3000)
p.add_argument('--batch', type=int, default=32); p.add_argument('--stages', default='10,20')
p.add_argument('--stage_cap', type=int, default=1500); p.add_argument('--promote', type=float, default=1.5)
p.add_argument('--lr', type=float, default=1e-3); p.add_argument('--neurons', type=int, default=64)
p.add_argument('--use_fast', type=int, default=1); p.add_argument('--init', default='')
p.add_argument('--erase_penalty', type=float, default=0.05)   # the exam's charge for erasing with no food present
p.add_argument('--food_stand', type=float, default=0.5)       # seconds at food per trip; more ticks of food = more signal for the erase gate
args = p.parse_args()

RUN = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'runs', args.run); os.makedirs(RUN, exist_ok=True)
LOG = os.path.join(RUN, 'log.jsonl'); CK = os.path.join(RUN, 'ckpt.pt'); STATUS = os.path.join(RUN, 'status.json')
stages = [float(s) for s in args.stages.split(',')]

torch.manual_seed(0)
net = FlyNet(n=args.neurons, use_fast=bool(args.use_fast))
opt = torch.optim.Adam([q for q in net.parameters() if q.requires_grad], lr=args.lr)
state = dict(it=0, stage=0, stage_start=0, recent=[])
if args.init and os.path.exists(args.init):                     # run 2 starts from run 1's weights
    net.load_state_dict(torch.load(args.init)['net']); print('initialised from', args.init)
if os.path.exists(CK):                                          # resume
    ck = torch.load(CK); net.load_state_dict(ck['net']); opt.load_state_dict(ck['opt']); state = ck['state']
    print('resumed at iteration', state['it'])


def drift_check(t_out, seed):
    """Frozen network on fresh trips: F allowed vs F held at zero.  The gap is where the memory lives."""
    with torch.no_grad():
        a = run_episode(net, batch=64, t_out=t_out, seed=seed, food_stand=args.food_stand)
        net.zero_F = True
        b = run_episode(net, batch=64, t_out=t_out, seed=seed, food_stand=args.food_stand)
        net.zero_F = False
        rec = run_episode(net, batch=1, t_out=t_out, seed=seed + 1, record=True, food_stand=args.food_stand)
    return dict(score_F=a['score'], arrived_F=a['arrived'], score_noF=b['score'], arrived_noF=b['arrived'], traces=rec['traces'])


def write_status(msg):
    json.dump(dict(it=state['it'], stage=state['stage'], t_out=stages[min(state['stage'], len(stages)-1)],
                   iters=args.iters, msg=msg, time=time.time(), pid=os.getpid()), open(STATUS, 'w'))


write_status('running')
t_last = time.time()
while state['it'] < args.iters:
    it = state['it']; t_out = stages[min(state['stage'], len(stages) - 1)]
    r = run_episode(net, batch=args.batch, t_out=t_out, seed=10000 + it, erase_penalty=args.erase_penalty, food_stand=args.food_stand)
    opt.zero_grad(); r['loss'].backward()
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
                       running=running, sec_per_iter=sec, ws=float(net.ws), A_abs=float(net.A.abs().mean()), W_abs=float(net.W.abs().mean()))
        if it % 100 == 0:
            rec['drift'] = drift_check(t_out, seed=777 + it)
            torch.save(dict(net=net.state_dict(), opt=opt.state_dict(), state=state, args=vars(args), t_out=t_out), CK)
            torch.save(dict(net=net.state_dict(), t_out=t_out, it=it), os.path.join(RUN, f'ckpt_{it:05d}.pt'))
            print(f"it {it:5d} stage {state['stage']} t_out {t_out:.0f}  loss {rec['loss']:.2f} score {rec['score']:.2f} run {running:.2f}  "
                  f"drift F {rec['drift']['score_F']:.2f} noF {rec['drift']['score_noF']:.2f}  {sec:.2f}s/it", flush=True)
        with open(LOG, 'a') as f: f.write(json.dumps(rec) + '\n')
        write_status('running')

torch.save(dict(net=net.state_dict(), opt=opt.state_dict(), state=state, args=vars(args), t_out=stages[-1]), CK)
torch.save(dict(net=net.state_dict(), t_out=stages[-1], it=state['it']), os.path.join(RUN, 'final.pt'))
write_status('finished'); print('finished')
