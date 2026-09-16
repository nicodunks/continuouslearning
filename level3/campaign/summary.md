# Read this first

_Written at the end of the night, 16 September 2026, about 2 a.m. Everything below links to a run you can open on this page._

## What the night was for
Ten or more experiments, one knob each, on the level 3 network: 64 neurons that must find their way home by rewriting their own connections. The goals were the lowest honest score on 30-second wanders, earned through the curriculum, and the three ingredients of the fly's circuit appearing on their own: compass cells, writing weighted by speed, and a wipe of the memory at food.

## What happened, in five lines
Twenty-five runs including the restarts. The best earned 30-second score is 1.62 (run 19), against a random walk's 4.4 and the hand-built fly brain's 0.75; the night started at 2.37. All three fly ingredients now exist in one network, run 19: 32 compass cells, a write gate that follows speed (+0.69), and an erase gate that fires 0.38 per tick at food and 0.008 away, with peaks near 1. The reset was the hard part and took a diagnosis (the gate was deaf: a sigmoid parked at -5) and five rounds of the same repair (runs 7B, 10, 12, 14, 16), each leaving more erasing at food. Peter's delta-rule alternative failed in both forms (runs 15, 18): a rule that writes only the surprise stops writing when a tally must keep adding. The activity-only rival (run 20) never learned to home at all, which is the level 4 answer in its plainest form.

## The three things to look at
1. The leaderboard, sorted by the 30 s column, then the family tree to see which runs came from which.
2. Compare two runs: put run 3 on the left and run 19 on the right. Every panel shows what four hours of one-knob changes did.
3. The stress test: the hand brain is flat across trip length, the learned networks are not, and the rival is at the random line.

## What is honest to say, and what is not
The 30-second stage was started before the strict promotion rule was met (see the narrative). The erase-bias shift is a change to the network's starting point, not a knob about the world, and each shift was a warm start; the reset was found by the network but the road to it was built by us. The rival was tried once, with one recipe and one seed; "it did not learn" is true of this attempt, not of activity memories in general. Seed 1 replicated the 10-second learning and transferred to 20 seconds slowly (runs 11, 11B), so the recipe's robustness claim is narrow. And the learned tallies still leak: error grows with trip length where the hand brain's does not.

## What I would do next
A polish of run 19 at a tenth of the rate (the move that gave run 17 its number). A second seed of the whole reset line, to show the ratchet is repeatable. A rival with a fair budget: several learning rates and a longer stage before calling it. And the two-food-site test from the original plan, which the world does not yet support.
