# Night two, read this first

_Written 17 September 2026, about 02:30. Campaign 2 ran from 20:15 to 02:00: 25 runs including restarts, starting from run 19 (1.62 at 30 s). Every number is the standard exam: seed 4242, 200 trips, 30-second wanders, with F allowed and with F held at zero._

## The answer to the question that was asked
The 30-second score did not go way down. It went down a little, and the little is real. The recipe that produced run 19 scores 1.72 on average over five seeds (1.62, 1.99, 1.61, 1.66, 1.73). Adding a small charge on the size of F (run 28's knob) gives 1.56 on average over four seeds (1.60, 1.59, 1.49, 1.55), with all four draws below four of the plain recipe's five. The best single network of both campaigns is run 41 at 1.49 with 38% arriving, and it beats run 19 at every stress condition. Everything else tried tonight, eleven other knobs and one stack, landed inside the plain recipe's spread or worse. The honest sentence for the leaderboard: this network, trained this way with the F-size charge, homes to about 1.56 units at 30 seconds, known to a twentieth over four seeds; the hand-built brain does 0.75.

## What was learned instead, which is more than the first night learned
1. **The count is real and readable.** A straight-line readout from the 4,096 fast weights recovers the home vector with R² 0.97 on held-out trips. "The memory lives in F" is now measured, not inferred.
2. **The count's direction is right; its length is not.** At the turn the decoded direction is off by 5 to 8 degrees and the length by about 0.9 units out of 6.9, biased short. The F-size charge trims the length error to 0.87; nothing else touched it.
3. **Saturation was not the leak.** Doubling the lid cut pinned cells from 43% to 8% and changed the count's error by almost nothing (run 21).
4. **Speed tracking was not the leak.** A many-speeds training world raised write-versus-speed from +0.69 to +0.77 and changed nothing on the exam (run 29).
5. **The fade is the code, not a leak.** Cutting the between-food fade at exam time makes run 19 worse (halved 2.02, removed 2.84). Forcing a slower fade by hand breaks the readout (run 33). Starting cold with a slow fade, training speeds the fade back up (run 37). The network's memory is a leaky integrator with a time constant of about fourteen seconds, and its readout is calibrated to exactly that. That is why it undercounts long trips, and why no knob that leaves the pair alone can fix it.
6. **Nothing in the network is spare.** Silencing any 8 of the 64 neurons takes the score from 1.6 to 4.0.
7. **One regulariser helps, modestly, over seeds.** A charge of 0.5 on the mean square of F keeps the board smaller (write strength down, wipe at food up) and lands about 0.15 lower than the plain recipe, on four draws with a spread of 0.05. Stacking it with a fade shift did not add and was fragile (one collapse in three).
8. **Optimisation is not the limit.** Batch 64, a low-rate polish, and both together improved the training-world fit and left the exam unchanged (runs 24, 26, 30, 31).
9. **Cold starts stall at 20 seconds.** Three of three tonight (128 neurons, the many-speeds world, the low erase floor), after one of two last night. Run 3's clean transfer looks like the fortunate case.
10. **The noise floor.** One recipe, five seeds, spread 0.15 with one draw at 1.99. Several first-night "improvements" of a tenth or two are inside this and should be read as ties.

## What is honest to say, and what is not
The plateau at 1.7 is a property of this recipe and this network, measured at five seeds; it is not a property of fast-weight networks in general. The single-knob results are all one seed each and should be read against the spread. The many-speeds world is a training-world change of the same kind as the two-speed world, allowed by the charter; the exam never changed. The diagnosis tool's readout is linear, so "the count's length is off by 0.9" means "off for a linear reader"; the network's own readout is not linear, and its error could differ.

## What I would do next
Not another knob from run 19. The three fade results say the way to a lasting count is to learn the count and the readout together for a long time constant, which means a different training signal, not a different starting point: for example, a loss that also charges for the decoded count's error at the turn, or a readout with a linear path so a growing count is easy to read. Both are changes to the loss or the architecture, and both are the right next experiment now that the knob board is exhausted.
