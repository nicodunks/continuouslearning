"""search.py  –  the same evolution strategy as level 1, over eleven numbers instead of six.

Three dials (write strength, rotation, turn gain) plus eight unit numbers (two units x
bias + three weights).  Nothing here knows what any number means.
"""
import numpy as np
from sim import ALL, DIALS, GATES, FLY, score_population

DEFAULT_RANGES = dict(write=(0, 2), rot=(0, 360), gain=(0, 10))
DEFAULT_CONFIG = dict(pop=24, keep=6, lanes=10, trips_per_lane=5, nudge=0.08, seed=0, w_max=40.0,
                      ranges=DEFAULT_RANGES, gate_range=16.0, junk_mode='smooth', start=None)


class Evolution:
    def __init__(self, config=None):
        self.cfg = dict(DEFAULT_CONFIG)
        if config:
            self.cfg.update({k: v for k, v in config.items() if v is not None})
        g = float(self.cfg['gate_range'])
        # every unit number shares one range, so no hint is smuggled in by giving the bias a different one
        self.ranges = {k: tuple(self.cfg['ranges'].get(k, DEFAULT_RANGES[k])) for k in DIALS}
        self.ranges.update({k: (-g, g) for k in GATES})
        self.rng = np.random.default_rng(int(self.cfg['seed']))
        self.gen = 0
        self.history = []
        self.pop = self._initial_population()

    def _initial_population(self):
        pop = int(self.cfg['pop']); start = self.cfg.get('start') or {}
        out = {}
        for k in ALL:
            lo, hi = self.ranges[k]
            if start.get(k) is not None:
                out[k] = np.full(pop, float(start[k]))
            else:
                out[k] = self.rng.uniform(lo, hi, pop)
        return out

    def _nudge(self, parent_idx):
        child = {}
        for k in ALL:
            lo, hi = self.ranges[k]
            noise = self.rng.normal(size=len(parent_idx)) * float(self.cfg['nudge']) * (hi - lo)
            child[k] = np.clip(self.pop[k][parent_idx] + noise, lo, hi)
        return child

    def step(self):
        pop, keep = int(self.cfg['pop']), int(self.cfg['keep'])
        scores, arrived = score_population(self.pop, int(self.cfg['lanes']), int(self.cfg['trips_per_lane']),
                                           seed=1000 + int(self.cfg['seed']) * 100000 + self.gen,
                                           junk_mode=self.cfg['junk_mode'], w_max=float(self.cfg['w_max']))
        order = np.argsort(scores); best = int(order[0])
        record = dict(gen=self.gen, best_score=float(scores[best]), best_arrived=float(arrived[best]),
                      mean_score=float(scores.mean()),
                      best={k: float(self.pop[k][best]) for k in ALL},
                      population={k: [float(v) for v in self.pop[k]] for k in ALL},
                      scores=[float(s) for s in scores])
        self.history.append(record)
        survivors = order[:keep]
        parents = survivors[self.rng.integers(keep, size=pop - keep)]
        children = self._nudge(parents)
        self.pop = {k: np.concatenate([self.pop[k][survivors], children[k]]) for k in ALL}
        self.gen += 1
        return record

    def state(self):
        return dict(gen=self.gen, config={k: v for k, v in self.cfg.items() if k != 'ranges'},
                    ranges=self.ranges, fly=FLY, dials=DIALS, gates=GATES, history=self.history)
