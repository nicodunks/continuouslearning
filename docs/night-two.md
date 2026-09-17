# Night two: what I tried, what happened, and what I still do not know

*Written by Claude on 17 September 2026 after the second overnight campaign (16 September, 20:15 PT, to 17 September, 02:00 PT). Every number here is from the standard exam unless it says otherwise: seed 4242, 200 trips, 30-second wanders on the steady-speed world, scored as the mean closest approach to home, with the fast weights allowed ("with F") and with them held at zero ("without F"). Lower is better. The hand-built fly brain scores 0.75 on this exam; a random walk scores about 4.4.*

---

## 1. The goal I set myself, and the rules

Nico asked for as many runs as needed by 05:00, "insanely high research taste," and a score "way way way improved" from run 19's 1.62. I wrote a charter before starting ([level3/campaign/charter2.md](../level3/campaign/charter2.md)). The rules it held me to:

- Do not touch the exam, the loss, the arrival radius, the compass noise or the steering. Every score is on the same ruler as the first night.
- Diagnose before spending compute.
- One knob per comparison. Singles from run 19 first, then stacks of what helped, then a polish, then the winner at more than one seed.
- Write the prediction before each run and the lesson after. Mark every explanation as measured or guess.
- Kill runs that are clearly dead within a few hundred iterations and spend the machine elsewhere.

The last rule got used a lot. Twenty-five runs were started (21 through 45); nine were stopped early by me.

## 2. The short version

The score did not go way down. It went down a little, and the little is real.

| recipe | 30-second score | how many training seeds |
|---|---|---|
| run 19's recipe, unchanged | 1.72, spread 0.16 | 5 (1.62, 1.99, 1.61, 1.66, 1.73) |
| same recipe plus a charge on the size of F | **1.56, spread 0.05** | 4 (1.60, 1.59, 1.49, 1.55) |
| best single network of both campaigns (run 41) | 1.49, 38% of trips arrive | one draw of the row above |

Twelve other knobs and one stack landed inside the plain recipe's spread or worse. The rest of this document is about why, because the "why" is where the night's value is.

## 3. The hour of diagnosis, and how it changed the plan

The first night ended with a plan whose first lever was the lid on the fast weights (see the "Counter With a Lid" page). Before running that, I spent an hour measuring run 19's final network with a new tool, [level3/diag.py](../level3/diag.py). Three measurements, no training:

**Can the home vector be read out of F?** I fitted a straight-line readout from the 4,096 fast weights to the true home vector on half of 128 trips and scored it on the other half. It recovers the vector with R² 0.97. So "the memory lives in F" is now measured directly, not inferred from the ablation. The readout's error grows along the wander: 0.12 units at 5 seconds, 1.04 at 25 seconds. Over the same span the share of cells pinned at the lid rises from 0 to 43%. That looked like confirmation of the lid story.

**Where along the trip is the score lost?** At the moment the fly turns for home, the decoded count is 1.2 units off out of 6.9 walked. Later I split that into a length part and a direction part: the direction is off by 7.7 degrees, the length by 0.93 units, and the length is biased short (the network undercounts by about 0.36 units). The fly's heading in the first 3 seconds of the return is off by 55 degrees, but so is the hand-built brain's (45 degrees), because the compass noise in this world swings the fly that much in 3 seconds; that number is the world, not the brain.

**Which parts are load-bearing?** Silencing the 32 compass cells at exam time takes the score from 1.62 to 5.8; silencing the other 32 cells, to 4.9; silencing any 8 neurons chosen at random, to 4.0. Nothing in the network is spare.

What this changed: it confirmed the lid as the first run, put the many-speeds world second (aimed at the write gate), and took the delta rule off the list entirely, since accumulation capacity was exactly the thing that looked short. Two of those three conclusions turned out to be wrong, which is the honest part of section 5.

## 4. Every run, with its reason

Verdicts: *helped*, *no effect* (inside the noise), *hurt*, *control* (a measurement, not an attempt to improve), *stalled* (a cold start that never transferred to 20-second wanders).

| run | what changed, from run 19 unless stated | why I tried it | 30 s result | verdict |
|---|---|---|---|---|
| 21 | lid ±1 → ±2 | the diagnosis showed pinning rising with the count's error | 1.96 (best checkpoint 1.83) | hurt |
| 22 | 128 neurons, cold start | no redundancy in the network; more room | learned 10 s in 302 iterations, never transferred to 20 s | stalled |
| 23 | train on 45-second wanders | make overflow cost loss during training | 2.05 at 30 s, 2.51 at 45 s | hurt |
| 24 | batch 32 → 64 | steadier gradient | 1.62 | no effect |
| 25 | erase penalty 20 → 5 | was 20 a tax on a gate that already works? | 1.92 | hurt |
| 26 | polish at a tenth of the rate | it gained 0.1 on run 13 | 1.71 | no effect |
| 27 | same recipe, training dice reseeded | measure the noise | 1.99 | control |
| 28 | a charge on the size of F (f_penalty 0.5) | the "smaller steps" lever | 1.60 | looked like no effect; see 40, 41, 45 |
| 29 | many-speeds training world | force the write gate to track speed continuously | 1.67, write~speed +0.69 → +0.77 | no effect |
| 30 | polish of run 29 | settle the many-speeds line | 1.78 | no effect |
| 31 | batch 64 plus a low-rate finish | stack the two optimisation improvements | 1.64 | no effect |
| 32 | cold start on the many-speeds world | does the lineage matter? | 10 s memory, stalled at 20 s | stalled |
| 33 | erase bias shift −2 (slower fade) | the fade compounds to an eighth over a wander | collapsed by 300 | hurt |
| 34, 35, 36 | same recipe, seeds 2, 3, 4 | pin down the mean and spread | 1.61, 1.66, 1.73 | control |
| 37 | cold start with the erase floor at 0.0009 | learn a slow fade and its readout together from scratch | earned 10 s at 804, stalled at 20 s; training raised its own fade to 0.014 | stalled |
| 38 | erase bias shift −1 | a gentler version of 33 | collapsed by 300 | hurt |
| 39 | erase bias shift −0.5 | the smallest step toward a slower fade | 1.57, reset intact | no effect on its own |
| 40, 41 | run 28's recipe, seeds 1 and 2 | does the lowest single score hold over seeds? | 1.59, 1.49 | helped |
| 42, 43, 44 | F penalty plus shift −0.5, from run 41, seeds 0, 1, 2 | do the two good moves add? | 1.66, 1.64, one collapse | no; fragile |
| 45 | run 28's recipe, seed 3 | fourth draw | 1.55 | helped |

Every run's prediction, written before it started, is in its `entry.json`; every lesson is in [level3/campaign/lessons.json](../level3/campaign/lessons.json); the turn-by-turn cards with mechanisms are in the deep-dive page's picker.

## 5. What did not work, and why, as best I can tell

**The lid (run 21).** This is the cleanest negative of the night, and it corrected the first night's main hypothesis. Doubling the lid did exactly what a lid does: pinned cells at 25 seconds fell from 43% to 8%. The count's error hardly moved (1.04 → 0.92 units at 25 seconds), and the score got worse, because every readout in the warm-started network had been tuned to cells that stop at 1 and had to re-tune to cells that reach 2. The Counter With a Lid page told a true story about the lid and a wrong story about its importance: the count's error grows with distance whether or not cells are pinned. *Measured.*

**The many-speeds world (run 29).** The diagnosis's second guess: since the write gate tracks speed at only +0.69, each tick's addition is only roughly proportional to distance, and those mis-weightings add up. So I built a training world where the speed changes to a random level every 5 seconds. The gate did learn to track speed better (+0.77). The score did not move. *Measured*, and it means speed weighting was not the binding part of the count's error either.

**Longer training trips (run 23).** Worse at both 30 and 45 seconds, and the reset weakened. *Guess* at the cause: the loss only looks at the last ten seconds of a return that is now 90 seconds long, so the training signal reaching what the network did in the first 45 seconds is weak and noisy; 600 such steps moved the network away from a good place rather than toward a better one.

**Lowering the erase penalty (run 25).** Worse, 1.92, but the gate barely changed (erase away from food 0.0077 → 0.0071, at food 0.38 → 0.31). I predicted the fade would grow; it did not. I do not have a mechanism for the 0.3 loss, and after the seed study I think a good part of it is noise. This card should be read with run 27 beside it.

**The optimisation family (runs 24, 26, 30, 31).** Batch 64, a low-rate polish, both together, on two lineages: all improved the fit to the training world (the best frozen checks of the campaign) and none moved the exam. *Measured.* The network is not held at 1.6 by noisy gradients or unsettled weights.

**Cold starts (runs 22, 32, 37).** All three learned the 10-second stage and none transferred to 20-second wanders in its budget, after one of two cold starts did the same on the first night. Run 3's clean transfer now looks like the fortunate case. *Guess* at the cause: the write gate settles high during the short stage and the tallies saturate at 20 seconds; unlearning that habit takes far more iterations than a night allows. I note that all three used run 3's recipe for the curriculum; a gentler length ramp was not tried.

**Slowing the fade by hand (runs 33, 38).** Both broke the network within 300 iterations. The fade did drop as intended (to 0.0012 and 0.003 per tick), and the wipe at food dropped with it because both live on the same gate, and the readout did not re-match. *Measured.* The −0.5 shift (run 39) was small enough to absorb, but on its own it is inside the noise, and stacked on the penalty (runs 42 to 44) it was worse than the penalty alone and collapsed on one seed of three.

**128 neurons (run 22).** Learned the 10-second stage in 302 iterations against run 3's 804, then stalled at 20 seconds. Capacity speeds up the first stage; it did not buy the transfer.

## 6. What worked, and how sure I am

**A charge on the size of F.** Adding 0.5 × the mean square of F at the end of each episode to the loss, as a regulariser. On its first draw it scored 1.60 and I wrote "no effect," because 1.60 against 1.62 is nothing. Then run 27 showed the plain recipe's noise was large, so I ran the penalty recipe at three more seeds: 1.59, 1.49, 1.55. Four draws in a band of 0.11, mean 1.56, against five plain draws with mean 1.72 and one at 1.99. Every penalty draw sits below four of the five plain draws. Run 41, the best draw, beats run 19 at all five stress conditions (30, 45, 60 seconds, two levels of compass drift), by a margin that shrinks with trip length.

How sure: fairly. Four versus five seeds is a small sample, and the two distributions overlap at the top. If I had to bet, the penalty recipe is better by about 0.1 to 0.2 on this exam. Its mechanism is only partly measured: the penalty keeps the board smaller (write strength 0.074 → 0.070, wipe at food 0.38 → 0.51), and run 41's decoded count length is a little better (0.87 against 0.93 units), but most of run 41's gain shows up after the turn, in the return, and I do not know why a smaller board steers better.

**The seed study itself.** Not an improvement to the score but the improvement to the night. One recipe, five seeds, spread 0.16, one draw at 1.99. Several first-night "improvements" of a tenth or two (the polish in run 17, the two-speed world's 2.10 → 1.98) are inside that spread and should be reread as ties until replicated. From here on the leaderboard should quote means over seeds.

## 7. What I think I learned

**The network's memory is a leaky integrator, and the readout knows it.** This is the finding I did not expect and now believe most. Every good run keeps the between-food fade at about 0.007 per tick, which compounds to an eighth over a 300-tick wander. I expected that to be a leak. Three separate tests say it is the code:

1. Scaling the fade down at exam time, with nothing retrained, makes run 19 worse: halved 2.02, quartered 2.46, removed 2.84. The readout expects a count that fades.
2. Forcing a slower fade by hand (runs 33, 38) breaks the readout within 300 iterations.
3. A cold start given a fade of 0.0009 from the first tick (run 37) raised its own fade to 0.014 during the 10-second stage. Offered a lasting count, training chose a fading one.

So the fade rests at 0.007 not because the gate is trapped on the flat part of the sigmoid (my first reading) but because a count with a time constant of about fourteen seconds is what this network can read well with a bounded, tanh-squashed board. That is also why the count is biased short and why the error grows with distance: the integrator is leaky by design. And it is why no knob that left the fade-and-readout pair alone could move the count's length.

**Where the error is.** Direction of the count: right to within 5 to 8 degrees. Length of the count: off by 0.9 units, short. Steering after the turn: near the noise floor. The bottleneck is "how far," and it is a property of the leaky-integrator solution.

**What the knob board can and cannot reach.** Every knob on the board (world, training, starting point) was tried or is now known not to be the lever. What is left changes the loss or the architecture, which the charter forbade tonight and which I think is the right next move (section 9).

**About my own process.** Two of my three diagnosis-driven bets (lid, speed tracking) were wrong, and I only found out by running them; the third (nothing spare) was right and did not lead anywhere useful. The diagnosis was still worth the hour: each wrong bet was cheap to refute because I had a measurement to refute it with, and the fade tests, which produced the real finding, only happened because the decoded-count numbers made the short bias visible. The reseeded control was the single most valuable run of the night and I scheduled it seventh; it should have been first.

## 8. What I still do not know, honestly

- **Why a smaller board steers better.** The penalty's gain is real over seeds but most of it is after the turn, where I have no mechanism. The count-length improvement (0.93 → 0.87) is too small to explain 0.15 of score on its own.
- **Whether a lasting count is learnable by this network at all.** The three fade results say the network prefers a fading count *given the training it got*. They do not say a lasting count plus a matched readout is impossible; they say it was not reachable by editing a trained network or by a low erase floor on a cold start that stalled anyway. A cold start with a low floor that made it through the curriculum would answer this, and none did.
- **Why cold starts stall at 20 seconds.** I have a guess (the write-gate habit) and no measurement of it. The one cold start that transferred cleanly (run 3) did so on the first night, on the steady-speed world, with a deaf erase gate. I do not know which of those mattered.
- **What the network's own readout does with the count.** The diagnosis tool reads F with a linear readout. The network's readout goes through A, the recurrent sum and a tanh. "The count's length is off by 0.9" means "off for a linear reader." The network's own error could be different, and the fade tests suggest its reader is not linear in the way mine is.
- **Whether run 27 is a bad seed or a bad start.** All five plain-recipe draws share run 14's weights and differ only in the training dice. The spread they show is the spread of the training process, not of the whole lineage; a fresh cold start would have more.
- **Whether the exam is representative.** Every number is one fixed set of 200 trips at 30 seconds. The stress test (30, 45, 60 seconds, two drift levels) agrees with the exam's ordering for run 41 against run 19, which is reassuring but is one comparison.
- **What the two-speed and many-speeds worlds cost.** Both improved the exam on the steady world, but I have not tested whether the networks trained on them have worse habits on trips the exam does not contain (very short trips, trips with long pauses).

## 9. Open questions I would put first, if there were a night three

1. **Learn the count and the readout together for a long time constant.** Add a term to the loss that charges for the decoded home vector's error at the turn (the diagnosis tool already computes it), or give the network a linear readout path so a growing count is easy to read. Both change the loss or the architecture; both target the one thing the knob board could not.
2. **A gentler length ramp for cold starts.** 10 → 15 → 20 → 30 seconds, or mixed lengths from the start, to see whether the stall at 20 seconds is about the jump or about the destination.
3. **Six seeds of the penalty recipe and six of the plain one, from a fresh cold start**, to know the lineage's spread rather than one warm start's.
4. **Lesion the network by function, not by position.** Silence the neurons that drive the erase gate during the return only, or the compass cells during the wander only, to see which phase each group serves.
5. **A fair rival, still owed from night one.** The activity-only network got one recipe and one seed. It should get an LSTM-style cell, a learning-rate sweep and a longer first stage before the level-4 claim is made firmly.

## 10. Where everything is

- The charter: `level3/campaign/charter2.md`
- Per-run predictions and lessons: `level3/runs/runN/entry.json`, `level3/campaign/lessons.json`
- The running narrative with timestamps: `level3/campaign/narrative.md`
- The night-two summary that heads the Night Report: `level3/campaign/summary2.md`
- Seed statistics: `level3/campaign/seeds.json`
- Diagnoses: `level3/campaign/diag_run19.json`, `diag_run21.json`, `diag_run29.json`, `diag_run41.json`, `diag_hand.json`; the fade test: `fade_test_run19.json`
- Stress test including run 41: `level3/campaign/stress.json`
- The tools: `level3/diag.py` (decode, phase split, lesions), the `--f_penalty` flag in `level3/train.py`, the `steps` speed profile in `level3/world.py`
- The pages: the Night Report (`docs/roadmap/night-report.html`) and Before the Deep Dive (`docs/roadmap/before-the-deep-dive.html`, question 12 and the Q1 turn picker)
