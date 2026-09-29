# Level 4 narrative (timestamped, written as it happens)

Charter: [charter.md](charter.md). Go at 08:22 PT, 29 September 2026. Hard stop 13:22.

**08:22 to 08:36 · build.** `level4/nets.py` (TWIN and the GRU reference), `level4/train4.py` (level 3's trainer with an `--arch` switch, surgery, one thread), `level4/exam.py` (all five conditions with resampled intervals), and two options in `level3/world.py` that change nothing unless asked for: `stop=(start, duration)` and per-agent scores in the output. Checks, all passed:
- the new harness reproduces run 41's standard exam exactly (1.491) and the hand brain's (0.748);
- trainable numbers: FW 8,708, TWIN 9,027, GRU reference 9,101;
- a freshly operated TWIN (gate open at 0.95) scores 5.921 on the exam, FW with F held at zero 5.921. Not a coincidence to worry about: both spin at full turn without a memory, and their turn outputs agree to within 0.02;
- during a long stop speed is exactly zero; the hand brain scores 0.72 with a 10 s stop against 0.75 without, as a perfect tally should.

**08:27 · launch.** One false start: the shell passed each argument list as a single string and every run refused to start; relaunched under bash a minute later, nothing had trained. Running now: the four warm twins (from runs 28, 40, 41, 45 with their seeds 0 to 3; 2,400 iterations at 30 s, night-two recipe) and nine sweep runs (TWIN, FW, GRU × rates 3e-4, 1e-3, 3e-3; 10 s stage, run 3's recipe, constant rate, 600 iterations). Dashboard for level 4 on port 8770.

**FW's history, in numbers (fairness rule 6).** Counting only the iterations that were carried forward along the lineage run 3 → 5 → 6 → 6B → 7B → 8 → 8B → 10 → 12 → 14 → 19 → 41 (and the same up to run 19 for runs 28, 40, 45): about 9,800 iterations, with four hand-made erase-bias shifts on the way (+2.5 at run 7B, then +1.5 at runs 10, 12 and 14). TWIN-warm inherits all of that and adds 2,400 of its own. The cold arms get 4,000 and no shifts.

**08:35 · sweeps.** Running score over the last 50 of 600 iterations on the 10 s stage (the random walk scores 2.31 there):

| arm | 3e-4 | 1e-3 | 3e-3 |
|---|---|---|---|
| FW | 1.74 | **1.30** | 2.22 |
| TWIN | 2.29 | 2.40 | 2.41 |
| GRU | 2.30 | 2.39 | 2.39 |

FW learns to home at 10 s within about 200 iterations at every rate but the highest. TWIN and the GRU learn nothing at any rate in 600 iterations; their curves track each other because they see the same training trips. Checked for a bug before believing it: both receive gradients through every weight (TWIN's hold-gate weights get about a twentieth of the push its table W gets), and the random walk really does score 2.31 here. Night one's plain activity rival (run 20) sat at 2.3 to 2.4 for 1,000 iterations in the same place. *Guess* at the cause, to be tested by the cold runs: FW's Hebbian board accumulates a tally with no training at all, so gradient descent only has to learn to *read* it; an activity network has to discover holding a number over 100 to 300 ticks from a loss that only looks at the end of the return, which is a much weaker signal.

Amendment recorded in the charter: since the sweep could not rank the rates for the activity arms, TWIN-cold and GRU-cold run at both 3e-4 and 1e-3 (three seeds each), and FW-cold at 1e-3. Fifteen cold runs started 08:35; nineteen trainers share eighteen cores.

**08:45 · the warm twins were stuck, and it was my surgery.** At iteration 800 of 2,400 the four warm twins were circling at full lock, worse than a random walk on the training world (8.8 against 6.76; FW's run 41 scores 2.49 there). Looking inside: the turn output sat at −7.8 of ±8, on the flat end of its tanh (slope about 0.06), and the hold gate had not moved from 0.952. FW's turn readout had been balanced by what the board fed in; removing the board left it lopsided. That is a flaw in how I built the rival. Amendment in the charter: four more warm twins (TWIN-warm-B) with the turn bias re-centred before training; the verdict uses the better of the two warm groups. The originals keep running and will be reported as they are. 23 trainers now share 18 cores, so everything runs about 40% slower.

**08:50 · the trap in the loss.** The warm twins B started as random walkers (after the re-centring) and within 600 iterations had drifted back towards circling, and the cold rivals at 3e-4 reached the 20 s stage by the stage cap (not by learning) and sit at 4.5 there. A measurement explains both. The training loss is the distance from home over the last 10 s of the return. For a brain with no memory, spinning on the spot keeps it near where it turned, while walking straight carries it further away:

| brain (no memory) | loss at 30 s, cold recipe | exam-style score |
|---|---|---|
| never steers | 11.5 | 4.57 |
| spins at full lock | **6.6** | 6.09 |

At 20 s the spinner scores 4.56, which is where the cold rivals are sitting. So the loss rewards spinning by almost half while the score punishes it: a trap that any network without a working memory falls into. FW never meets it, because its board starts accumulating a tally on the first tick with no training, and reading that tally beats spinning almost at once. *Measured* (the table); that this is *why* the rivals fail is a well-supported guess, tested next by the teacher runs: both TWIN-aux runs passed the 10 s stage (promoted at 762 and 810) and one GRU-aux run is learning (2.07 at 10 s).

Also measured at 08:46: FW-cold seed 0 was promoted to 20 s and is learning there (3.12 running, with F 3.40 against 4.70 without F); seed 1 is at 20 s but not yet learning; seed 2 is still at 10 s.

**08:57 · FW examined.** The four FW networks through every condition (table in `results.json`): standard exam 1.60 / 1.59 / 1.49 / 1.55 (mean 1.56, reproducing night two); on 1,000 fresh trips 1.68 / 1.67 / 1.55 / 1.57 (mean 1.62), so the usual exam is about 0.06 kind. A 30 s stop costs FW 0.6 (mean 2.17) while the hand brain does not notice it (0.72). Five trips in a row: trip 1 about 1.43, trips 2 to 5 about 1.6 to 1.9, so the reset leaves a little behind (about 0.2 to 0.3). 90 s wanders: 4.4, against 7.3 for a fly that never steers.

**09:00 · teachers work; nobody learns 20 s from scratch easily.** GRU-aux seed 0 runs at 1.86 at 20 s and the TWIN-aux runs at about 2.2 to 2.3 (a fly that never steers scores 3.65 at 20 s). So both activity designs can hold a home vector once the loss tells them what to hold. Without a teacher: the rival colds at 3e-4 sit at the spinner's 4.5 at 20 s; the four warm twins B slid back into spinning (8.6 on the training world); and FW-cold is struggling at 20 s too (3.6, 4.3, 3.9), the stall campaign 2 saw.

**09:02 · warm diagnostic with the teacher on both sides** (charter amendment 09:01): TWIN-warm-aux from runs 41 and 45, FW-warm-aux from runs 41 and 45. One launch error (the teacher readout was created before the FW weights were loaded, and loading insisted on an exact match); fixed with `strict=False` on `--init`, relaunched a minute later.

**09:18 · the warm twins B failed.** All four finished 2,400 iterations and score 5.88 to 5.95 on the standard exam (6.24 to 6.31 on 1,000 fresh trips), worse than a fly that never steers (4.38) and almost identical to each other: they all spin. Re-centring the turn gave them a fair start (they began as random walkers), and within a few hundred iterations training had pulled them back into the spinning trap, where they stayed. Their FW parents score 1.49 to 1.60 on the same trips. So the main verdict will almost certainly read "FW better", and the reason is visible: with the same history and more iterations, the activity version never found a way out of the trap that the homing loss sets for a network without a working memory.

Meanwhile, with the teacher: GRU-aux seed 0 is at 30 s with a frozen check of 1.61, close to FW's 1.56; TWIN-aux seed 0 at 30 s runs about 2.3. Activity memories that were told what to hold do nearly as well as FW on the standard trips. Whether they hold better in the long stop is the next measurement.

**09:41 · the teacher runs examined: working activity memories.** Two TWIN-aux and two GRU-aux networks, cold, 4,000 iterations each with the teacher term, examined without the teacher (it is dropped at exam time):

| network | standard | 1,000 fresh | 30 s stop (cost) | 90 s (cost from 30 s) |
|---|---|---|---|---|
| FW, mean of 4 | 1.56 | 1.62 | 2.17 (+0.61) | 4.44 (+2.9) |
| TWIN-aux 0 | 1.94 | 2.10 | 2.17 (+0.23) | 3.58 (+1.6) |
| TWIN-aux 1 | 2.61 | 2.68 | 2.74 (+0.13) | 5.05 (+2.4) |
| GRU-aux 0 | 2.11 | 2.31 | 2.29 (+0.18) | 5.05 (+2.9) |
| GRU-aux 1 | 2.98 | 3.05 | 3.04 (+0.05) | 5.87 (+2.9) |

Three things. First, activity memories can do the job: the best teacher-trained twin homes at 1.94 on standard trips, within 0.4 of FW, after 4,000 iterations against FW's roughly 9,800 and no hand fixes. Second, a working activity memory loses far less during a long stop (0.05 to 0.23) than FW (0.61), because its gate can hold while FW's board keeps fading; this is the opposite of the roadmap's original argument, and it matches the charter's prediction (55%). Third, on long trips it is mixed: the best twin degrades much less than FW (+1.6 against +2.9), the others about as much. These networks had a teacher, so none of this is in the verdict; it is the fairest look available at memory quality between networks that both work.

**09:45 · correction: the reset is clean.** At 08:57 I wrote that FW's reset "leaves a little behind (about 0.2 to 0.3)", because trips 2 to 5 scored worse than trip 1. That reading was wrong. The same five-trip test is harder on later trips for every brain: the random walk goes 4.10, 4.65, 4.92, 4.61, 5.30 across trips 1 to 5, and the teacher-trained twin, whose activity the world wipes for free, rises from 1.81 on trip 1 to 2.12 on trips 2 to 5 (+0.31). FW run 41 rises by +0.18. So FW's erase gate resets the board at food as cleanly as a free wipe, within what the trips themselves cause. The fair comparison is always against a brain facing the same trips.

**10:10 · everything but FW-cold examined.** Every rival trained without a teacher spins: TWIN-warm (the pre-registered four) 5.68 to 5.98 on the standard exam; TWIN-cold and GRU-cold at 1e-3 5.91 to 5.98 (at 3e-4, 5.81 to 5.91); even the warm twins with a teacher (TWIN-warm-aux) 5.89 and 5.38, though the cold twins with a teacher learned. The warm start from FW's weights is a worse place for an activity memory to begin than a random start. FW-warm-aux (FW retrained with the teacher) ended at 1.76 (from 1.49) and 1.59 (from 1.55): the mid-run dip to 3.8 recovered, and the teacher did not help FW. A ten-minute delay here was my own: a wait loop counted to 39 finished runs when there were 37.

**10:14 · the stop, looked at properly, and a correction to my own page text.** My draft said the working twins "close their hold gate and barely move while standing". The probe says otherwise: their hold gates stay about 0.6 open while standing, and their activity changes by about 30% over the stop. Activity movement is not a fair measure anyway (activity also tracks heading, which keeps changing as the fly turns on the spot), so I added a decode: a straight-line readout of the home vector fitted just before the stop, applied again at its end, and refitted at its end (half of 600 flies to fit, half to score). FW: 0.42 to 0.50 before; 3.0 to 3.6 with the same readout after; 0.80 to 1.14 refitted. So FW's board keeps the information but shrinks, and a fixed reading (the network's own) reads it short. Teacher-trained activity networks: 0.96 to 1.66 before; 1.69 to 2.74 refitted after. They lose more information than FW, and yet pay less for the stop on the exam. Unexplained; best guess (not measured): their own readout copes with the change better than FW's reading, which is calibrated to a count that fades at a fixed rate.

**10:58 · FW from scratch examined; everything is in.** The three FW-cold runs finished their full 4,000 iterations before the cutoff (so the cutoff shortened nobody). Standard exam: 1.86, 5.23, 2.60. All three passed the 10 s stage by learning (iterations 447, 247, 911); none met the promotion bar at 20 s, though all three learned something there (best running 1.61, 2.52, 2.15 against 3.65 for a fly that never steers). Seed 1 then fell into the spin at 30 s and ended at 5.23, so FW is not immune to the trap, only far less prone to it: 2 of 3 FW seeds ended as working navigators from scratch, against 0 of 12 rival runs. Seed 0's 1.86 comes within 0.3 of the warm FW networks, which had about 9,800 iterations and four hand fixes behind them.

Verdicts by the charter's rules. Warm pair: **supported** (FW better at every level of every condition, gaps 2.7 to 6.5). Cold pair (trainability): FW learned where the twins did not (3 of 3 against 0 of 6 at the first stage). Both verdicts are decided by trainability; the teacher diagnostics show that an activity memory which has been taught comes within about 0.4 of FW on ordinary trips and pays much less for a long stop.

## Round 3 (charter3.md), 11:09 to 12:10

**11:10 · the twin gets FW's head start.** FW's erase gate has started almost shut (bias −5) since night one, so its board holds by default; the twin's hold gate had started half open. Twelve cold runs with the twin's gate started almost shut (−5 and −3) and a GRU started at "keep", same recipe as this morning's FW-cold runs (the matched opponent, not retrained). Checked at the start: the twin's gate opens 0.0076 per tick, FW's erase gate 0.0067.

**11:14 · the head start was undone, and why.** At iteration 700 all twelve were at chance, and inside, training had opened the twin's gate from 0.0076 to 0.23 while the network turned hard. The reason is structural: FW has fast neurons (they follow the heading every tick) and a separate slow board; the twin has one population that must do both, so a slow start stops it following the heading and training opens the gates, the store with them. Added the split twin (32 neurons started fast like FW's, 32 started slow like FW's board), six runs, same size and recipe.

**11:16 · split twins at iteration 500:** all six at chance (2.30 to 2.38). FW-cold passed this stage by learning at iterations 247, 447 and 911, so this is not yet a verdict; they run their full 4,000.

**11:55 · round 3 result.** All 18 runs examined. Standard exam: split twins 5.92, 5.89, 4.86, 5.84, 5.93, 5.89; twins with the hold start 5.88 to 5.98; GRUs with the hold start 5.92 to 5.97. A fly that never steers scores 4.38; FW from scratch with the same recipe 1.86, 5.23, 2.60. The one split twin that learned the 10 s stage (seed 1, rate 1e-3, running 1.69) is the best rival network of the day without a teacher, and it still ends worse than not steering. With starting settings matched (the hold start) and structure matched (the split twin), the activity memory does not learn this task from this grading in 4,000 iterations; FW does on two of three seeds. Predictions: "the head start helps, at least one setting learns 10 s on 2 of 3 seeds" wrong (1 of 18 runs); "GRU-hold learns on at least 1 of 3" wrong; the stop and tie predictions were untestable because nothing learned.
