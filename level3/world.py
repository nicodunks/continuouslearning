"""world.py  –  the homing game, batched in PyTorch so training can trace backwards through it.

Same game as level1/sim.py and level2/sim.py: start at food, wander T_OUT seconds with the brain's turn
ignored, then up to 2*T_OUT seconds where the brain's turn drives the legs, then half a second at food.
Two trips per episode; the brain's fast state carries over between them, its activity does not.

Differences from the numpy worlds, all forced by training:
  * every quantity is a torch tensor with one entry per agent, so gradients can flow;
  * the loss is SMOOTH: mean distance from food over the last 10 s of each return (not "did it arrive");
  * a small penalty on the erase gate being open when food is absent (discourages a constant fade).
The score we report next to the loss is the same as levels 1 and 2: mean closest approach on the return.
"""
import math, torch

DT = 0.1
W_MAX = 40.0          # tally ceiling (used by the hand brain; FlyNet clamps F to ±1 instead)
ERASE_PENALTY = 0.05  # weight of the "erase open without food" penalty in the loss


def run_episode(brain, batch=32, t_out=20.0, trips=2, seed=None, drift=0.0, record=False):
    """Run one episode of `trips` trips for `batch` agents.  `brain` must implement:
         brain.reset_fast(batch)   -> start of episode: fast state to zero
         brain.reset_activity()    -> start of each trip: activity to zero (fast state untouched)
         brain.step(inp)           -> (turn, write_gate, erase_gate), inp is [batch, 4]
       Returns dict(loss, score, arrived, and optional traces of agent 0)."""
    g = torch.Generator().manual_seed(int(seed)) if seed is not None else None
    def randn(*s): return torch.randn(*s, generator=g)
    def rand(*s): return torch.rand(*s, generator=g)

    t_ret = 2.0 * t_out
    n_ticks = int(round((t_out + t_ret) / DT))
    brain.reset_fast(batch)
    dist_terms, pen_terms, score_terms, arr_terms = [], [], [], []
    traces = {k: [] for k in ('t', 'speed', 'food', 'write', 'erase', 'dist', 'hd')} if record else None

    for trip in range(trips):
        brain.reset_activity()
        pos = torch.zeros(batch, 2)
        hd = rand(batch) * 2 * math.pi
        comp = torch.zeros(batch)                       # compass error (level 4 drift test); 0 here
        speed = torch.ones(batch)
        pause = torch.zeros(batch, dtype=torch.long)
        arrived = torch.zeros(batch, dtype=torch.bool)
        since_arrival = torch.zeros(batch, dtype=torch.long)
        min_d = torch.full((batch,), float('inf'))

        for k in range(n_ticks):
            t = k * DT
            returning = t >= t_out
            done = since_arrival >= 5
            active = ~done
            at_food = ((t < 0.5) | arrived) & active
            food = at_food.float()

            # ---- speed: drift, pauses, zero at food / when done ----
            in_pause = pause > 0
            pause = torch.where(in_pause, pause - 1, pause)
            start_pause = (~in_pause) & (rand(batch) < 0.02)
            pause = torch.where(start_pause, (rand(batch) * 2 + 1).div(DT).long(), pause)
            speed = (speed + 0.3 * randn(batch) * math.sqrt(DT) + 0.2 * (1 - speed) * DT).clamp(0.3, 1.7)
            speed = torch.where(in_pause | at_food | done, torch.zeros(batch), speed)

            # ---- what the brain sees ----
            comp = comp + drift * randn(batch) * math.sqrt(DT)
            hd_seen = hd + comp
            inp = torch.stack([torch.cos(hd_seen), torch.sin(hd_seen), speed, food], 1)
            turn, write, erase = brain.step(inp, active=active)

            # ---- the world moves (only active, not-yet-arrived agents) ----
            moving = active & ~arrived
            dhd = (turn * DT if returning else torch.zeros(batch)) + 0.8 * randn(batch) * math.sqrt(DT)
            hd = hd + torch.where(moving, dhd, torch.zeros(batch))
            step = torch.where(moving, speed * DT, torch.zeros(batch))
            pos = pos + torch.stack([step * torch.cos(hd), step * torch.sin(hd)], 1)
            d = pos.norm(dim=1)
            if returning:
                min_d = torch.minimum(min_d, d.detach())
                arrived = arrived | (d.detach() < 0.5)
                if t >= t_out + t_ret - 10.0:
                    dist_terms.append(d)                              # smooth loss: distance over the last 10 s
            since_arrival = since_arrival + arrived.long()
            pen_terms.append((erase * (1 - food)).mean())             # erase open with no food present
            if record:
                traces['t'].append(t + trip * (t_out + t_ret)); traces['speed'].append(float(speed[0]))
                traces['food'].append(float(food[0])); traces['write'].append(float(write[0]))
                traces['erase'].append(float(erase[0])); traces['dist'].append(float(d[0])); traces['hd'].append(float(hd[0]))
        score_terms.append(min_d); arr_terms.append(arrived.float())

    loss = torch.stack(dist_terms).mean() + ERASE_PENALTY * torch.stack(pen_terms).mean()
    out = dict(loss=loss, score=float(torch.stack(score_terms).mean()), arrived=float(torch.stack(arr_terms).mean()))
    if record: out['traces'] = traces
    return out
