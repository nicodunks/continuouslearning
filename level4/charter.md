# Level 4 charter: is a memory held in fast weights better than a memory held in activity?

*Written by Claude for itself on 29 September 2026, before any code or run. Hard stop: five hours after Nico says go. Nothing in this file changes after the start except the "amendments" section at the bottom, which records every change with its time and reason.*

*Revision history before the start. Draft 1 used a standard, off-the-shelf GRU as the main rival. Draft 2 added a modernised fast-weight network to balance it. Nico's call for draft 3: leave our fast-weight network exactly as it is, and make the rival its twin, identical in every part except how it remembers. That is this version.*

## The question, in one sentence

Take our trained fast-weight network, keep everything about it except its memory, and give it the best activity memory of the same size instead: which one homes better, and under which conditions?

## The two twins

Both are the same machine: 64 neurons, the same four inputs (heading as two numbers, speed, food), the same slow connection table W between neurons, the same outputs, the same tanh squashing, the same world and loss. The only difference is the part that lets a number be held over time.

| | **FW**, fast weights (ours, unchanged) | **TWIN**, gated activity |
|---|---|---|
| how a number is held | written into the board F by the write gate, faded by the erase gate | held in the neurons' own activity by a hold gate |
| the extra part | the allowance table A: 64 × 64 = 4,096 numbers | the hold gate's weights: 64 × 64 + 64 × 4 + 64 = 4,416 numbers |
| total trainable numbers | 8,708 | 9,028 (4% more) |
| memory state per agent | 64 activities + 4,096 board cells | 64 activities |

**How the hold gate works.** Each tick, each neuron computes a proposal as before, `tanh(W_in · input + W · x_old)`, and a hold gate `u` between 0 and 1 from the same inputs. The new activity is `(1 − u) × x_old + u × proposal`. With `u` near 0 the neuron keeps its value exactly: a loop gain of exactly 1, the thing the roadmap says an activity memory needs and cannot easily get. With `u` near 1 it is our plain network. This is the single-gate version of a GRU (a standard gated recurrent network). So TWIN is the fairest possible form of the roadmap's claim: it is handed the very ability the roadmap says activity memories lack, and has to learn when to use it.

The write and erase outputs are kept on TWIN but connected to nothing, so the loss (which charges for erasing away from food) is identical for both. For TWIN that charge is always zero.

## Two pairs of runs

**The warm pair: each twin gets the same history.** FW's four trained seeds (runs 28, 40, 41, 45, the night-two recipe, 1.56 on average) are the starting point. For each one, TWIN is made by surgery: copy W_in, W and W_out; remove A and F; add the hold gate, starting fully open (`u` about 0.95) so that at the first tick TWIN behaves like FW with its memory removed. Then TWIN trains with the night-two recipe (two-speed world, 4 s at food, batch 32, rate 3e-4, cosine decay, F-size penalty irrelevant). It gets **2,400 iterations** at 30 s, three times FW's last step of 800, because it has to rebuild its memory from nothing while FW only refined one. That tilt is towards the rival, on purpose.

**The cold pair: neither twin gets any history.** FW-cold and TWIN-cold both start from random weights with the same seed, the same curriculum (10 → 20 → 30 s), the same promotion rule, up to 1,500 iterations per stage and 4,000 in all, and the same learning-rate sweep (3e-4, 1e-3, 3e-3 on the 10 s stage, 600 iterations, best running score wins). Three seeds each. This pair answers a different question: which memory is easier to learn from scratch? FW-cold stalled at 20 s in all three of campaign 2's cold starts, so this is a real test.

**One reference arm, not in the verdict.** A standard off-the-shelf GRU with 52 memory units (9,101 numbers), cold, same protocol, three seeds. It shows where a textbook design lands, so a reader can see whether TWIN is a weak rival. It costs about 20 minutes a run.

## What "better" means, fixed before anything runs

Every score is the standard ruler: mean closest approach to home over the return, lower is better, frozen networks, no retraining at test time. The hand-built fly brain and a random walk are on every chart.

| # | condition | what it asks | how it is built |
|---|---|---|---|
| 1 | standard exam, 30 s wander | plain homing | unchanged: seed 4242, 200 trips; repeated on 1,000 fresh trips (seed 5151) to check the exam is not lucky |
| 2 | longer wanders: 45, 60, 90 s | does the memory hold as the count grows? | same world, longer wander, return time scaled as always |
| 3 | drifting compass: 0.05 and 0.15 | does it survive a bad heading signal? | as in stress.py |
| 4 | a long stop: 10 s and 30 s standing still halfway through the wander | the roadmap's core argument: an activity memory must hold with gain exactly 1, a tally does nothing | new world option; speed forced to zero for the stop, nothing else changes |
| 5 | reset between trips: 5 trips per episode instead of 2 | does the memory wipe cleanly, trip after trip? (the plan's "two food sites" reduces to this, because each trip's home is measured from where it started) | score per trip number; flat means a clean reset |

Condition 5 carries a built-in unfairness, stated on its chart: the world wipes activity at the start of every trip for free. TWIN gets its reset from the world; FW must earn it with its erase gate. So condition 5 measures what the reset costs FW, not a contest.

## Fairness rules

1. Same world, loss, exam, arrival radius, compass noise and steering for everyone. Same code path in the trainer for both twins; the only switch is the memory.
2. Within each pair, identical protocol: same seeds, curriculum, budget, sweep grid. The only planned difference is TWIN-warm's extra iterations, which favours the rival.
3. **No rival run is stopped early for looking bad.** Runs are stopped only for crashes or a loss of NaN (not a number), and that is recorded. FW-cold gets the same rule.
4. Nothing in either arm changes after its seeds launch. A bug found in shared code is fixed for both and recorded.
5. Each run is pinned to one processor thread (benchmark on 29 September: no speed loss from 1 to 4 threads), so about 12 runs share the machine.
6. FW's full history is reported in numbers: total training iterations behind each FW seed, counted back to run 3, and the hand-made erase-bias shifts along the way.

## How a winner is called, fixed now

For each condition, each arm's score is the mean over its seeds, with every network's 95% interval from resampling its trips drawn as the exam's own noise.

- **Better**: the means differ by at least 0.2 and the seed ranges do not overlap.
- **Leans better**: the means differ by at least 0.2 but the ranges overlap.
- **Tie**: anything else.

The main verdict is the warm pair, FW against TWIN-warm:
- **Supported** ("fast weights beat activity memory here") if FW is better on the standard exam, or better on at least two of conditions 2, 3 and 4, and worse on none.
- **Not supported** if TWIN ties or beats FW on the standard exam and on conditions 2 to 4.
- **Mixed** otherwise, with the conditions named.

The cold pair gets its own verdict on trainability: how many seeds of each finish the curriculum, and their scores if they do. The GRU reference is reported beside both, never used to decide.

## Predictions, written before running

- TWIN-warm learns to use its hold gate and homes within 0.2 of FW on the standard exam: a tie. 55%.
- Long stop: TWIN-warm holds better than FW, because a gate can close whenever speed is zero, while FW's erase gate keeps fading the board at about 0.007 per tick. 55%.
- Longer wanders: TWIN-warm ties or beats FW, because FW is a leaky counter with a time constant of about 14 s. 55%.
- Reset: FW is flat within 0.15 across trips 1 to 5. 70%.
- Cold pair: TWIN-cold finishes the curriculum on more seeds than FW-cold. 65%. FW-cold stalls at 20 s on at least 2 of 3 seeds. 75%.
- The GRU reference lands within 0.3 of TWIN, which would show TWIN is not a strawman. 60%.
- Overall: I expect **not supported** or **mixed**. That would still be a real result: on this task, a same-sized network that can hold its activity is enough, and the fly's trick would need a harder task to show its advantage.

## Timeline (T = hours after go)

| time | work |
|---|---|
| T+0:00 to 0:40 | Build `level4/`: TWIN (with the surgery from an FW checkpoint), the GRU reference, the long-stop world option, `--arch` in a copy of the trainer, the test harness for all five conditions with resampled intervals. Checks: the harness reproduces run 41's 1.49 and the hand brain's 0.75; a freshly operated TWIN with the gate open scores like FW with F held at zero; the long stop really holds speed at zero; parameter counts as in the table. |
| 0:40 to 1:00 | Sweeps on the 10 s stage, all in parallel: TWIN-cold, FW-cold and GRU, three rates each. |
| 1:00 to 3:45 | Main training, about 12 at once: TWIN-warm ×4 first (the main verdict), then TWIN-cold ×3, FW-cold ×3, GRU ×3. Live dashboard as before. |
| 3:45 to 4:15 | Freeze everything; run all five conditions on every network, plus the 1,000-trip check. |
| 4:15 to 5:00 | Write-up: a level 4 page with the real charts (numbers on them, how each was measured) next to sketches of what a win, a tie and a loss would look like; both verdicts by the rules above; measured versus assumed; lessons; commit and push. |

If time runs short, cut in this order: the 90 s wander, the GRU reference, the third cold seed of each twin (both together). The warm pair and the verdict rule are never cut.

## What this cannot show, whatever happens

- One task. A tie says activity memory is enough for 30 to 90 s homing in this world, not that fast weights never help.
- FW is one design of fast weights, the fly-faithful one this project built. A different fast-weight design could do better or worse; that is not tested here.
- TWIN-warm starts from FW's weights, so it inherits FW's compass cells and anything else FW's history built. That is the point of the warm pair (same history), and it also means TWIN-warm's result is not a from-scratch result; the cold pair covers that.
- Condition 5 gives TWIN its reset for free.
- Three or four seeds per arm is small; a gap under about 0.2 cannot be told apart from training luck.

## Record

`level4/runs/<arm>_s<seed>/` for every run (arguments, prediction, log); `level4/results.json` (every network × every condition); `level4/narrative.md` (timestamped, as in campaign 2); `level4/lessons.json`.

## Amendments

**08:35 · the sweep could not choose a rate for the activity arms.** After 600 iterations on the 10 s stage, TWIN scored 2.29 / 2.40 / 2.41 and the GRU 2.30 / 2.39 / 2.39 at rates 3e-4 / 1e-3 / 3e-3, all at the random walk's 2.31: none of the rates learned, so the rule's pick (3e-4) is a coin flip between equal failures. FW scored 1.74 / 1.30 / 2.22 and gets 1e-3. Change: TWIN-cold and GRU-cold run three seeds at **both** 3e-4 and 1e-3, and each is judged at its better rate; FW-cold runs at its one chosen rate. This tilts the cold pair towards the rivals, on purpose. Both rates are reported.

**08:45 · the warm twins start in a dead zone of my own making.** Found by looking inside twin_w41 at iteration 800 (training score 8.8, worse than the random walk's 6.76 on the training world): FW's turn readout was balanced by what the board fed into the neurons, so after surgery the turn output sits at −7.8 of a possible ±8, where the tanh that caps it has a slope of about 0.06 and the learning signal barely passes. The hold gate had not moved from its starting 0.952. This is a flaw in the surgery, not a property of activity memory, and it would hand FW a win for the wrong reason. The pre-registered TWIN-warm runs continue unchanged and will be reported. Added: **TWIN-warm-B**, the same four surgeries plus one hand fix before training, re-centring the turn output's bias so the twin steers straight on average (checked: it then starts as a random walker, 6.75 against 6.76, with a learning signal about 20 times stronger). This is the same kind of fix FW received four times in its history (erase-bias shifts). The main verdict uses the better of TWIN-warm and TWIN-warm-B, which favours the rival, on purpose.

**08:43 · a diagnostic arm, outside the verdict.** The sweeps raise a question the verdict cannot answer by itself: when the activity networks fail to home, is it because they *cannot* hold a home vector, or because the homing loss is too weak a signal for gradient descent to *find* how? Added: TWIN-aux and GRU-aux, cold, same recipe and curriculum at rate 1e-3, two seeds each, with one extra term in the training loss: a straight-line readout from the activity must state the home vector at every tick of the wander, charged by its squared error × 0.1 (dense supervision, as Cueva and Wei 2018 trained path-integrating networks). The readout is discarded at exam time; the exam is unchanged. If these networks then home, the failure elsewhere is about the learning signal, not capacity. FW-aux (same term on FW's activity) is added if cores free up. None of these enter the verdict; they change the loss, which the charter forbids for verdict arms.

**08:48 · a gap in the verdict rule, closed before any exam has run.** Conditions 2, 3 and 4 have several levels each (45/60/90 s; drift 0.05/0.15; stop 10/30 s), and the rule did not say how to combine them. Fixed now, with no exam results in hand: a condition's verdict is "better" if FW is better at a majority of its levels (2 of 3, or both of 2), "worse" if worse at a majority, otherwise "tie". "Better" and "worse" here include "leans"; the per-level labels are shown so a reader can apply the strict version. The rival side in the warm verdict is whichever of TWIN-warm and TWIN-warm-B has the lower mean on the standard exam, chosen once and used for every condition. The page computes all of this from the numbers with the rule as written here, so it cannot be nudged by hand.

**09:01 · a symmetric warm diagnostic with the teacher, outside the verdict.** By 09:00 the teacher runs showed that both activity designs can hold a home vector when given dense supervision (GRU-aux 1.86 and TWIN-aux 2.2 running score at 20 s, against 3.65 for a fly that never steers), while every warm twin without a teacher had fallen into the spinning trap. So the warm verdict will measure trainability more than memory quality. To compare memory quality between working networks with the same history, added: TWIN-warm-aux (surgery from runs 41 and 45, turn re-centred, 2,400 iterations) and FW-warm-aux (runs 41 and 45 retrained 800 iterations, their own recipe), both with the same teacher term (×0.1). Both sides get the teacher, so neither is favoured. FW-warm-aux also answers night two's open question 1 (does a charge on the decoded home vector improve FW?). None of these enter the verdict.

**09:06 · a clock cutoff, set before knowing how the long runs end.** With every arm and diagnostic running, the machine carries about 21 active trainers on 18 cores (6 fast, 12 efficiency). FW-cold, the slowest arm (about 2.9 s per iteration at 20 s under this load), will not reach its 4,000 iterations before the hard stop. Rule: at 11:50 all training stops; any run not finished is examined at its latest checkpoint and reported with the iteration it reached. Every rival arm is expected to finish its full budget before then, so if the cutoff shortens anyone it is FW-cold, which tilts the cold pair towards the rivals.

**10:58 · closing note.** All runs finished their budgets; the 11:50 cutoff was not needed and was disarmed. Results, verdicts and the prediction scorecard are on the page (`docs/roadmap/twin-test.html`) and in `narrative.md`.
