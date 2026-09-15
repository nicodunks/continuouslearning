"""search.py  –  the evolution strategy, as an object you can step one generation at a time.

Guess, score, keep, nudge, repeat.  Nothing here knows which direction is better.  The nudges
are blind; the selection does the learning.
"""
import numpy as np
from sim import DIALS, FLY, score_population

DEFAULT_RANGES = dict(write=(0, 2), speed_dep=(0, 1), erase=(0, 1), fade=(0, 0.2), rot=(0, 360), gain=(0, 6))

DEFAULT_CONFIG = dict(
    pop=24,             # candidates per generation
    keep=6,             # survivors copied unchanged into the next generation
    lanes=10,           # agents per candidate running side by side
    trips_per_lane=3,   # trips each agent runs in a row (tallies carried over) -> 30 trips per score
    nudge=0.08,         # child = parent + bell-curve noise of (nudge x range) on every dial
    seed=0,             # for the starting population and the nudges
    ranges=DEFAULT_RANGES,
    start=None,         # None = random start; or a dict of dial values every candidate starts at
)


class Evolution:
    def __init__(self, config=None):
        self.cfg = dict(DEFAULT_CONFIG)
        if config:
            self.cfg.update({k: v for k, v in config.items() if v is not None})
        self.ranges = {k: tuple(self.cfg['ranges'].get(k, DEFAULT_RANGES[k])) for k in DIALS}
        self.rng = np.random.default_rng(int(self.cfg['seed']))
        self.gen = 0
        self.history = []                          # one record per generation, for the chart
        self.pop = self._initial_population()      # dict dial -> array (pop,)

    def _initial_population(self):
        pop = int(self.cfg['pop'])
        start = self.cfg.get('start')
        out = {}
        for k in DIALS:
            lo, hi = self.ranges[k]
            if start and start.get(k) is not None:
                out[k] = np.full(pop, float(start[k]))          # everyone starts at the given value
            else:
                out[k] = self.rng.uniform(lo, hi, pop)           # random inside the range
        return out

    def _nudge(self, parent_idx):
        """Make children by copying chosen parents and adding blind noise to every dial."""
        child = {}
        for k in DIALS:
            lo, hi = self.ranges[k]
            noise = self.rng.normal(size=len(parent_idx)) * float(self.cfg['nudge']) * (hi - lo)
            child[k] = np.clip(self.pop[k][parent_idx] + noise, lo, hi)
        return child

    def step(self):
        """One generation: score everyone on fresh trips, keep the best, breed the rest."""
        pop, keep = int(self.cfg['pop']), int(self.cfg['keep'])
        # Fresh trips every generation (seed changes) so nobody can memorise the exam;
        # same seed within the generation so every candidate sat the same exam.
        scores, arrived = score_population(self.pop, int(self.cfg['lanes']), int(self.cfg['trips_per_lane']),
                                           seed=1000 + int(self.cfg['seed']) * 100000 + self.gen)
        order = np.argsort(scores)                  # best (lowest) first
        best = int(order[0])
        record = dict(
            gen=self.gen,
            best_score=float(scores[best]),
            best_arrived=float(arrived[best]),
            mean_score=float(scores.mean()),
            best={k: float(self.pop[k][best]) for k in DIALS},
            population={k: [float(v) for v in self.pop[k]] for k in DIALS},
            scores=[float(s) for s in scores],
        )
        self.history.append(record)
        # survivors: copied unchanged.  children: nudged copies of random survivors.
        survivors = order[:keep]
        parents = survivors[self.rng.integers(keep, size=pop - keep)]
        children = self._nudge(parents)
        self.pop = {k: np.concatenate([self.pop[k][survivors], children[k]]) for k in DIALS}
        self.gen += 1
        return record

    def state(self):
        return dict(gen=self.gen, config={k: v for k, v in self.cfg.items() if k != 'ranges'},
                    ranges=self.ranges, fly=FLY, history=self.history)
