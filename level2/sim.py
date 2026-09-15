"""sim.py  –  level 2: the world and brain, with the write and erase signals produced by two
learned decision units instead of wires we chose.

Everything about the world, the direction cells, the tally board, the reader and the steerer is
the same as level 1 (see level1/sim.py).  What changes:

  level 1:   write_signal = speed (blended with "moving")        erase_signal = erase_dial at food
  level 2:   write_signal = unit(w_write, speed, food, junk)     erase_signal = unit(w_erase, speed, food, junk)

A unit is the simplest possible neuron.  It has three incoming connections (from the speed sensor,
the food sensor, and a junk signal that means nothing) and one bias.  It adds up
    bias + w_speed*speed + w_food*food + w_junk*junk
and squashes the total into 0..1 with a sigmoid.  That output IS the signal.

Both units get the SAME three sensors.  Nothing tells the write unit "you are the speed one".
The search sets the eight numbers (2 units x (bias + 3 weights)); we look at where they land.

The junk signal exists so there is a wrong answer available.  A unit that trusts junk writes or
erases at random and gets lost.  A unit that learns to give it weight ~0 has made a choice.
"""
import numpy as np

DT, T_OUT, T_RET = 0.1, 30.0, 60.0
N = 8
COLS = np.arange(N) * 2 * np.pi / N
TONIC = 0.3
W_MAX = 40.0    # a synapse cannot grow forever.  One trip writes roughly 30 units across the columns, so a board
                # that is never erased hits this ceiling within a couple of trips and can no longer record new steps.
                # This is WHY a reset is needed at all; without a ceiling the search finds it can skip erasing.

DIALS = ['write', 'rot', 'gain']                                  # the three dials that remain
GATES = ['wb', 'ws', 'wf', 'wj', 'eb', 'es', 'ef', 'ej']           # write: bias, speed, food, junk ; erase: same
ALL = DIALS + GATES                                               # the eleven numbers the search sets
FLY = dict(write=1.0, rot=180.0, gain=3.0, wb=-3.0, ws=4.0, wf=0.0, wj=0.0, eb=-12.0, es=0.0, ef=16.0, ej=0.0)   # eb=-12: sigmoid(-12) is 6e-6, so the resting erase (the fade) is negligible
GATE_NAMES = dict(wb='write: bias', ws='write: from speed', wf='write: from food', wj='write: from junk',
                  eb='erase: bias', es='erase: from speed', ef='erase: from food', ej='erase: from junk')


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def junk_signal(t, phase, rng, M, mode):
    """The distractor.  'smooth': a slow sine in 0..1 plus a little noise, different phase per agent.
    'spiky': the same, but 2 % of ticks it jumps to 3, so trusting it is punished harder."""
    j = np.clip(0.5 + 0.5 * np.sin(0.7 * t + phase) + 0.1 * rng.normal(size=M), 0, 1)
    if mode == 'spiky':
        j = np.where(rng.random(M) < 0.02, 3.0, j)
    return j


def score_population(params, lanes=10, trips_per_lane=3, seed=0, junk_mode='smooth', w_max=W_MAX):
    """Score every candidate on the same random trips.  params: dict name -> array (pop,)."""
    rng = np.random.default_rng(seed)
    pop = len(params['write'])
    M = pop * lanes
    P = {k: np.repeat(np.asarray(params[k], float), lanes) for k in ALL}

    W = np.zeros((M, N))                       # the tallies, carried across trips
    total_min = np.zeros(M); total_arr = np.zeros(M)
    n_ticks = int((T_OUT + T_RET) / DT)
    phase = rng.uniform(0, 2 * np.pi, M)       # junk phase per agent, independent of the wandering

    for trip in range(trips_per_lane):
        x = np.zeros(M); y = np.zeros(M)
        hd = rng.uniform(0, 2 * np.pi, M)
        speed = np.ones(M); pause = np.zeros(M, int)
        min_d = np.full(M, np.inf); arrived = np.zeros(M, bool)
        since_arrival = np.zeros(M, int)     # ticks since arriving; after 5 the agent is 'done' and frozen

        for k in range(n_ticks):
            t = k * DT
            returning = t >= T_OUT
            done = since_arrival >= 5              # arrived 0.5 s ago: frozen, nothing updates (see level1/sim.py)
            active = ~done
            at_food = ((t < 0.5) | arrived) & active
            food = at_food.astype(float)

            in_pause = pause > 0
            pause = np.where(in_pause, pause - 1, pause)
            start_pause = (~in_pause) & (rng.random(M) < 0.02)
            pause = np.where(start_pause, (rng.uniform(1, 3, M) / DT).astype(int), pause)
            speed = np.clip(speed + 0.3 * rng.normal(size=M) * np.sqrt(DT) + 0.2 * (1 - speed) * DT, 0.3, 1.7)
            speed = np.where(in_pause | at_food, 0.0, speed)

            junk = junk_signal(t, phase, rng, M, junk_mode)
            cells = np.maximum(0.0, np.cos(COLS[None, :] - hd[:, None]))

            # ---- THE TWO UNITS.  Same three sensors into each; the weights decide what they listen to. ----
            write_signal = sigmoid(P['wb'] + P['ws'] * speed + P['wf'] * food + P['wj'] * junk)
            erase_signal = sigmoid(P['eb'] + P['es'] * speed + P['ef'] * food + P['ej'] * junk)

            # ---- tally update: grow by write_signal, shrink by erase_signal, every tick ----
            W += (DT * P['write'][:, None] * write_signal[:, None] * cells) * active[:, None]
            W *= np.where(active, 1.0 - erase_signal, 1.0)[:, None]
            np.minimum(W, w_max, out=W)                 # saturation: no column above the ceiling

            act = W * (cells + TONIC)
            ax = (act * np.cos(COLS)).sum(1); ay = (act * np.sin(COLS)).sum(1)
            r = np.radians(P['rot'])
            rx = ax * np.cos(r) - ay * np.sin(r); ry = ax * np.sin(r) + ay * np.cos(r)
            clean = np.hypot(rx, ry) / (act.sum(1) + 1e-9)
            turn = P['gain'] * np.sin(np.arctan2(ry, rx) - hd) * np.minimum(1.0, 2 * clean)
            turn = np.where(returning & ~arrived, turn, 0.0)

            hd = hd + np.where(arrived, 0.0, turn * DT + 0.8 * rng.normal(size=M) * np.sqrt(DT))
            step = np.where(arrived, 0.0, speed * DT)
            x += step * np.cos(hd); y += step * np.sin(hd)
            d = np.hypot(x, y)
            if returning:
                min_d = np.minimum(min_d, d)
                arrived |= d < 0.5
            since_arrival += arrived

        total_min += min_d
        total_arr += arrived

    return (total_min.reshape(pop, lanes).mean(1) / trips_per_lane,
            total_arr.reshape(pop, lanes).mean(1) / trips_per_lane)
