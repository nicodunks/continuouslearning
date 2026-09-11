# Kim et al. (2019): Generation of stable heading representations in diverse visual scenes

[Published article](https://doi.org/10.1038/s41586-019-1767-1) · [Main PDF](main.pdf) · [Scientific supplement](41586_2019_1767_MOESM1_ESM.pdf) · [Reading coverage](reading-log.md)

## What this contributes to a complete navigation account

The compass must learn how a particular visual environment maps onto its internal circular coordinate. This paper shows that experimentally pairing a visual scene with an imposed E-PG activity bump changes that mapping. A model learns the correspondence through plastic inhibition from visual ring neurons to compass neurons. The learned object is a calibration of heading, not a food location, a displacement vector, a desired heading, or a route.

That distinction becomes consequential when combined with long-term bearing behavior. If a goal is stored in compass coordinates, changing the scene-to-compass mapping can rotate the world direction associated with that goal. A complete navigator needs either stable calibration, coordinated transformation of remembered vectors, or a retrieval mechanism that reconstructs the relevant frame. The present study establishes the calibration problem and a possible solution within the compass; it does not solve the interface with destination memory.

## Preparation and measured variables

Head-fixed female flies fly in closed loop while E-PG calcium activity is imaged. The visual panorama turns according to the difference in wingbeat amplitudes. This is rotational virtual behavior, without physical translation. E-PGs express GCaMP6f and CsChrimson with SS00096. The Methods use 6–10-day-old females, while the reporting summary says 5–8 days; that discrepancy remains recorded rather than silently reconciled.

The arena covers 330° horizontally and 60° vertically. Its 30° rear gap is stitched out of the represented coordinate, and the remaining 330° is rescaled to 360°. This convention differs from preparations that retain a rear gap in their angular analysis. Wing imaging runs at 119.2 Hz, with closed-loop gain 5.1°/s per degree of wingbeat-amplitude difference; six-plane brain imaging is about 9.8 Hz. Natural photographs are reduced to four display levels, partly because bright visual stimulation can activate CsChrimson and interfere with imaging.

The crucial observation is the offset between scene orientation and the E-PG population phase. Neither a bump's anatomical position nor its offset is an absolute geographic heading. Changes in offset indicate recalibration, whereas instantaneous tracking with a stable offset indicates that visual input and the internal estimate are aligned.

## Experiments and figure logic

**Figure 1 — natural scenes can anchor a compass.** Both forest and open-space panoramas support stable within-trial mappings. Different flies and scenes can have different offsets. However, “arbitrary offset” should not be translated into an assertion of a perfectly uniform distribution: the open-space distribution is significantly nonuniform (P < 0.0001), whereas the forest distribution is not distinguishable from uniform (P = 0.3603). The relevant trial counts are 39 and 40 across ten flies. The source of the open-space preference is unresolved.

**Figure 2 — visual calibration is writable.** The experiment drives a bump at eight positions separated by 45°, each paired with the appropriate scene orientation for 2–2.5 seconds, repeatedly for five minutes. In the subsequent one-minute closed-loop probe, the scene anchors the bump at the imposed offset. Stripe experiments include 25 trials from 14 flies; natural-scene experiments include 19 trials from ten flies. Opposite imposed shifts are rotated into a common coordinate for pooling. This is a retained change in mapping, not simply an optogenetic deflection during illumination.

Controls without CsChrimson and manipulations in darkness do not reproduce the corresponding systematic shifts (P = 0.0934 and 0.6064, respectively). Those nonsignificant controls do not establish zero effects. Artificially induced bumps are on average 13.3% brighter than natural bumps, consistent with needing sufficient drive to displace the old activity pattern. Imaging itself may weakly activate CsChrimson and increase baseline variability.

The accompanying model weakens inhibition at coactive visual-ring/E-PG combinations. After learning, each E-PG is preferentially released from inhibition by the visual pattern encountered at its heading. This paper does not directly measure changes in individual ring-to-E-PG synaptic efficacy; the companion Fisher study must be considered separately.

**Figure 3 — even the direction of the mapping can be forced.** Ten minutes of reverse pairing produce reversed visual-to-bump motion in four of eight flies; three retain normal mappings and one has a poor mapping. The two-minute probe therefore demonstrates substantial flexibility, not universal reversal. The model eventually corrects the imposed reversal using the self-motion signal. That eventual correction is not established by the short biological probe.

**Figure 4 — partial experience can alter a larger map, conditionally.** Pairing only a 180° range can shift stripe mapping (six of ten flies); a 60° range succeeds in seven of twenty trials under the authors' shift criterion. Whether probing begins inside the manipulated range strongly affects success: six of thirteen versus one of seven for the stripe, and four of four versus three of sixteen when both bump and stripe are considered. These are small groups, and the reported binomial comparisons use probabilities estimated from the other group. The result supports completion through attractor dynamics plus continuing learning. It is not evidence that the entire unseen map is rewritten instantaneously, nor that completion always works. The natural-scene manipulation is also significant at the population level, with failures visible among individual flies.

**Figure 5 — visual input cannot be reduced to one azimuthal luminance profile.** Four identical objects at the same elevation create compass ambiguity. Moving them to different elevations improves stability even though their collapsed one-dimensional azimuthal profile is unchanged. Circular variance is approximately 0.7521 versus 0.1212 across forty trials from ten flies. Elevation-sensitive visual features can disambiguate yaw; this does not mean the compass encodes two-dimensional position. Repeated trials within flies should remain explicit when interpreting pooled bootstrap statistics.

## Extended Data and supplementary arguments

**Extended Data 1** supplies experimental and control detail for mapping manipulation. The controls and stronger imposed bump support a pairing-dependent effect, while fluorescence and imaging conditions remain relevant to quantitative interpretation.

**Extended Data 2** follows model weights from random initialization through experience, imposed remapping and consolidation. Ring-attractor dynamics create a bump before the weights have learned a useful visual map. The turning trace is a measured 400-second flight trace repeated three times; it is a supplied teaching signal, not a model-generated foraging trajectory.

**Extended Data 3** tests ambiguity without optogenetic pairing. Two opposite stripes can establish competing mappings. Only three of nineteen biological trials show a clear half-turn offset switch after returning to one stripe. In the other sixteen, the first fifteen seconds show more competing bumps and greater offset deviation than a later comparison trial. The supplement explicitly notes a mismatch: biological two-stripe responses often cover only half the EB, whereas the model covers the whole ring. This limits a literal identification of the simulation with every observed dynamic.

**Extended Data 4** supports the scene-disambiguation argument and model comparison. The meaningful input is the pattern across visual feature channels, not merely a sine wave over azimuth.

**Extended Data 5** rearranges a common set of features into two scenes. Re-exposure can retrieve the old offset, but both candidate plasticity rules reproduce the result because the scenes' filtered two-dimensional cross-correlation supplies a deterministic correspondence. Retrieval here is not sufficient evidence for two independently protected memories. In the depicted filter calculation, a 15° Gaussian standard deviation is described as a 30° FWHM; mathematically it is about 35.3°, so that size correspondence is approximate.

**Extended Data 6** compares distinct natural scenes and the effect of inactive visual channels. Returning to forest or open-space scenes tends to restore the original offset after an intervening scene. Presynaptically gated learning protects weights belonging to inactive visual inputs; postsynaptically gated learning can overwrite them whenever an E-PG fires. The paper also explicitly allows that residual weights under the postsynaptic rule could recover the former mapping. The experiments therefore constrain interference and retrieval without uniquely proving one plasticity rule.

The scientific supplement develops these alternatives, their simplifying assumptions and the complete simulation equations. It is essential to the mechanistic interpretation, not just ancillary methods.

## Mathematics: a learned input map acting on a circular state

Let f_n be E-PG activity, g_m visual ring-neuron activity and W_nm a positive inhibitory weight. In the paper's discrete model,

\[
\tau\dot f_n=-f_n+\left[\alpha f_n+D(f_{n+1}+f_{n-1})-\beta\sum_m f_m+1-\frac{v}{2}(f_{n+1}-f_{n-1})+I_n\right]_+,
\qquad I=-Wg+s.
\]

There are 32 E-PG units; τ = 0.05 s, α = −7.76, D = 5.19 and β = 1.96. The negative α is not a claim that all local recurrence is inhibitory: this parameterization separates the two neighboring terms, and α + 2D = 2.62. It should not be substituted unchanged into the earlier paper's Laplacian parameterization. The antisymmetric neighbor difference translates the bump; v is a calibrated model drive, not automatically an angular velocity in radians per second.

A complex summary of the compass is

\[
Z=\sum_n f_n e^{i\phi_n},\qquad \hat\theta=\arg Z.
\]

This first Fourier mode is a readout of the network. It is not the entire dynamical model: thresholding, higher spatial harmonics and learned visual inputs still matter. The inputs can be complicated mixtures of receptive fields. Perfect sinusoids are unnecessary for maintaining a phase and learning which visual pattern should anchor it.

For postsynaptically gated learning, the supplement gives

\[
\dot W_{nm}=\eta[f_n-f_{\rm th}]_+
\left[W_{\max}\left(1-\frac{g_m}{g_0}\right)-W_{nm}\right],
\qquad \eta=\epsilon v^2.
\]

For presynaptically gated learning,

\[
\dot W_{nm}=\eta[g_m-g_{\rm th}]_+
\left[W_{\max}\left(1-\frac{f_n}{f_0}\right)-W_{nm}\right].
\]

The illustrative constants include W_max = 0.33, g_0 = 0.33, f_0 = 0.08, f_th = 0 and g_th = 0.1, with clipping to the weight range. In either case, coactivity reduces inhibition. But the gate determines which *inactive associations* are modified. For constant activities, a gated weight approaches its target exponentially; when its gate is zero, it stays fixed. Thus presynaptic gating can leave an unseen scene's channels untouched. Postsynaptic gating instead drives a quiet visual channel toward strong inhibition whenever the relevant E-PG fires.

The v² factor is an assumed movement dependence intended to prevent prolonged fixation from dominating training. Its form is not a measured biochemical learning law. Equal potentiation/depression timescales, the thresholds, and simplified receptive fields are also model choices. There can be hybrid rules and additional modulatory gates.

The scene comparison can be written with exponentials too. If A(φ,h) and B(φ,h) are filtered panoramas, their rotational match is

\[
C_{AB}(\delta)=\int\!\int A(\phi,h)B(\phi+\delta,h)\,d\phi\,dh
=2\pi\sum_k\int\overline{\hat A_k(h)}\hat B_k(h)\,dh\ e^{ik\delta}
\]

for real scenes and the usual Fourier convention. Collapsing over elevation before comparison can destroy useful distinctions between objects. This is visual pattern alignment around a heading circle, not a representation of the fly's translational location.

## Source-code checks and quantitative limits

The author-hosted MATLAB simulation archive was downloaded and the core solver, ring parameters, main configuration and plasticity parameters were read. No simulation or quantitative reproduction was run. The released default configuration is one complex scene, 32 E-PGs, 32 visual units, postsynaptic learning and a 0.01-second timestep. Some figure-specific settings in the supplement differ from that default.

The solver normalizes visual and stimulation currents by angular discretization factors. Its learning implementation includes factors of three or six, a presynaptic threshold of 0.1/3, and movement normalization using mean(v²) + 1.5 standard deviations across the supplied trial. That normalization is a simulation preprocessing step; it is not an online neural mechanism. A calculated postsynaptic threshold variable is not used in the corresponding derivative expression. Weight bounds are implemented through a clipped proposed change inside the solver, so reproducing the equations requires reading those details rather than assuming a simple parameter-for-parameter transcription. These checks constrain reproducibility, not the qualitative evidence for remapping.

The movie animation uses accelerated learning and different integration settings from some plotted simulations. Four movies were inspected through captions and 24 evenly spaced frames each: natural-scene offset writing; a plasticity-model animation; inverse mapping; and ambiguity with two stripes. This is sampled inspection, not frame-complete viewing. The supplement's animation reference numbering should be checked against the actual inventory: Video 2 is the simulation, whereas Video 3 is the inverse-mapping experiment.

## Remaining questions and connectome relevance

1. **What protects a behaviorally useful goal when compass calibration changes?** If H = e^{i(θ+α)} and G = e^{i(g+α)}, then G conjugate(H) = e^{i(g−θ)} cancels a shared frame offset. If only the compass changes α, the cancellation fails. This paper does not identify a mechanism that transforms goal memories along with calibration.
2. **What controls when learning occurs?** Locomotion weighting, prediction error, novelty, reinforcement and internal state could serve different roles. The model's v² factor is not an answer at the cellular level.
3. **How many environments can be remembered?** Capacity depends on overlap of visual feature channels, interference, retrieval and the plasticity gate. A two-scene example does not establish lifetime capacity.
4. **How is heading stabilized during translation?** Nearby landmarks change bearing with position. The discussion suggests slow learning can downweight transient cues, but the tethered rotational experiments do not establish that solution in a moving animal.
5. **Where are the physical synaptic changes?** A connectome can constrain ring-to-E-PG convergence and candidate learning pathways. It cannot reveal an individual animal's learned efficacy matrix, its update rule, or the scene history that produced it from synapse counts alone.
6. **How does this support return to food?** It supplies a calibrated heading estimate. Remembering the destination, estimating displacement, selecting a target, and terminating navigation at the correct place require additional circuits and behavioral evidence.
