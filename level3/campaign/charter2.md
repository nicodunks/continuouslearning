# Campaign 2 charter (written by Claude for itself, 16 Sept 2026, 20:20 PT; hard stop 05:00 PT)

## Goal
Lower the honest 30-second score as far as it will go, starting from run 19 (1.62), without changing the exam, the loss, the arrival radius, the compass noise or the steering. Every number reported is the standard exam: seed 4242, 200 trips, standard world, with F allowed and with F held at zero.

## Method
1. Diagnose before spending compute: decode the home vector from F along the trip, split the error by phase (outbound count, return heading, search near home), lesion the compass cells and the gate drivers. Let the diagnosis pick the levers.
2. One knob per comparison. Singles from run 19 first, then stacks of the singles that helped, then a polish, then the winner replicated at a second seed.
3. Two trainers at a time (18 cores). Kill within five minutes if the F gap closes; kill any run that is clearly a dead end; restart as a B variant if the failure is hygiene.
4. Write the prediction before each run and the lesson after. Mark every mechanism as measured or guess.
5. The last run finishes by 04:30 so tests, the report and the deep-dive update are done by 05:00.

## Candidate levers (order decided by the diagnosis)
lid ±1 → ±2 (and ±4), a 45-second curriculum stage, batch 32 → 64, erase penalty 20 → 5, a small penalty on the size of F, 128 neurons from a cold start, seed 1 of the winner. Delta only if the diagnosis says accumulation is not the bottleneck.

## What I will not do
Touch the exam or the loss. Report a number without its F-held-at-zero partner. Call a gain real if it is inside the seed-to-seed noise without a replication.

## Deliverables at 05:00
Night Report rebuilt with every run; Before the Deep Dive updated with the new turns in the picker, each with numbers, a mechanism and a verdict; campaign/lessons.json and narrative.md extended; memory notes updated; everything committed and pushed.
