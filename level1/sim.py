"""sim.py  –  the world and the level 1 brain, run for a whole population at once.

This is the same game as the roadmap's world.py + brain1.py + exam1.py, but written so that
numpy handles MANY agents in one go instead of one agent in a Python loop.  Pure-Python ticks
are about 100x too slow for a search; vectorised, a generation takes about a second.

The idea: every quantity that was one number (x, y, heading, speed, the eight tallies...) becomes
an ARRAY with one entry per agent.  One line of numpy then updates every agent at once.

Agents are arranged as  pop x lanes.  Each candidate brain (pop) drives `lanes` independent agents,
and each agent runs `trips_per_lane` trips IN A ROW with its tallies carried over between trips.
Carrying tallies over is what makes the erase dial matter; a fly gets no clean board either.
"""
import numpy as np

DT, T_OUT, T_RET = 0.1, 30.0, 60.0        # tick, outbound seconds, max return seconds
N = 8                                     # direction columns
COLS = np.arange(N) * 2 * np.pi / N       # their angles: 0, 45°, 90° ... in radians
TONIC = 0.3                               # background read-out drive so every column speaks a little

DIALS = ['write', 'speed_dep', 'erase', 'fade', 'rot', 'gain']   # the six blanks, in this order
FLY = dict(write=1.0, speed_dep=1.0, erase=1.0, fade=0.0, rot=180.0, gain=3.0)   # what we believe the fly does


def score_population(params, lanes=10, trips_per_lane=3, seed=0):
    """Score every candidate in `params` on the same random trips.

    params : dict  dial name -> numpy array of shape (pop,)   one value per candidate
    returns: (mean closest approach per candidate, fraction of trips arrived per candidate)
             both shape (pop,).  Lower closest-approach = better brain.
    """
    rng = np.random.default_rng(seed)             # same seed => same trips for every candidate: a fair exam
    pop = len(params['write'])
    M = pop * lanes                               # total agents running side by side
    # Stretch each candidate's dial value across its lanes:  [a, b] -> [a, a, a, b, b, b]  for lanes=3.
    P = {k: np.repeat(np.asarray(params[k], float), lanes) for k in DIALS}

    W = np.zeros((M, N))                          # the tallies: one row of 8 per agent. Carried across trips.
    total_min = np.zeros(M)                       # running sum of closest approaches, per agent
    total_arr = np.zeros(M)                       # running count of arrivals, per agent
    n_ticks = int((T_OUT + T_RET) / DT)           # 900

    for trip in range(trips_per_lane):
        # ---- start of a trip: everyone at food, facing a random way ----
        x = np.zeros(M); y = np.zeros(M)
        hd = rng.uniform(0, 2 * np.pi, M)
        speed = np.ones(M); pause = np.zeros(M, int)
        min_d = np.full(M, np.inf); arrived = np.zeros(M, bool)

        for k in range(n_ticks):
            t = k * DT
            returning = t >= T_OUT                            # the switch: brain may drive the legs
            at_food = (t < 0.5) | arrived                     # first half second, or after arriving

            # ---- speed: slow drift, occasional pauses, zero while at food ----
            in_pause = pause > 0
            pause = np.where(in_pause, pause - 1, pause)
            start_pause = (~in_pause) & (rng.random(M) < 0.01)               # 1 % chance per tick
            pause = np.where(start_pause, (rng.uniform(1, 3, M) / DT).astype(int), pause)
            speed = np.clip(speed + 0.3 * rng.normal(size=M) * np.sqrt(DT) + 0.2 * (1 - speed) * DT, 0.3, 1.7)
            speed = np.where(in_pause | at_food, 0.0, speed)

            # ---- direction cells: cos of (column angle - heading), clipped at zero.  shape (M, 8) ----
            cells = np.maximum(0.0, np.cos(COLS[None, :] - hd[:, None]))

            # ---- write signal: blend of "on while moving" and "scaled by speed", set by speed_dep ----
            moving = (speed > 0).astype(float)
            wsig = P['speed_dep'] * speed + (1 - P['speed_dep']) * moving

            # ---- THE TALLY UPDATE.  This line is the continual learning. ----
            W += DT * (P['write'][:, None] * wsig[:, None] * cells - P['fade'][:, None] * W)
            W *= np.where(at_food, 1 - P['erase'], 1.0)[:, None]      # erase at food (erase=1 wipes clean)

            # ---- reader: tallies read through current cell activity, summed as arrows ----
            act = W * (cells + TONIC)
            ax = (act * np.cos(COLS)).sum(1); ay = (act * np.sin(COLS)).sum(1)
            # ---- rotation by `rot` degrees ----
            r = np.radians(P['rot'])
            rx = ax * np.cos(r) - ay * np.sin(r); ry = ax * np.sin(r) + ay * np.cos(r)
            # ---- steerer: turn toward the arrow, harder when the arrow is clean ----
            clean = np.hypot(rx, ry) / (act.sum(1) + 1e-9)
            turn = P['gain'] * np.sin(np.arctan2(ry, rx) - hd) * np.minimum(1.0, 2 * clean)
            turn = np.where(returning & ~arrived, turn, 0.0)         # only obeyed on the return

            # ---- the world moves.  Arrived agents stand still at food. ----
            hd = hd + np.where(arrived, 0.0, turn * DT + 0.8 * rng.normal(size=M) * np.sqrt(DT))
            step = np.where(arrived, 0.0, speed * DT)
            x += step * np.cos(hd); y += step * np.sin(hd)
            d = np.hypot(x, y)
            if returning:
                min_d = np.minimum(min_d, d)
                arrived |= d < 0.5

        total_min += min_d
        total_arr += arrived

    # average over trips, then over the lanes belonging to each candidate
    per_cand_score = total_min.reshape(pop, lanes).mean(1) / trips_per_lane
    per_cand_arr = total_arr.reshape(pop, lanes).mean(1) / trips_per_lane
    return per_cand_score, per_cand_arr
