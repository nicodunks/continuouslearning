# Lyu, Abbott & Maimon — allocentric travelling direction

Nature 601, 92–97 (2022); online 15 December 2021. DOI: [10.1038/s41586-021-04067-0](https://doi.org/10.1038/s41586-021-04067-0).

**Reading status:** complete main PDF, Methods, ten Extended Data figures and captions, supplementary text and reporting summary. Movies inspected through temporally sampled frames across their full durations; this is not frame-by-frame playback. No raw experimental-data replication performed. See [reading log](reading-log.md) for coverage.

## What the experiment distinguishes

Heading H tells us where the animal faces; travel T tells us where it moves. Sideways or backward translation separates them. The core finding is that hDeltaB's axonal population phase tracks T, while EPG tracks H. Four PFN populations provide a plausible and experimentally constrained coordinate transform between body-relative translation and world-relative travel. This is a computation of direction, not a demonstration of a home vector or integration of distance over a journey.

The strongest design choice is independent control of translational optic flow while a bright landmark remains under closed-loop yaw control. A sideward flow stimulus can change inferred travel without requiring the heading bump to make the same change. The relevant comparison is the relative neural phase, not just two neurons separately correlating with visual motion.

## Evidence, figure by figure

| Figure | Experiment or calculation | What it establishes; limit |
|---|---|---|
| 1 | Simultaneous EPG and presynaptically targeted hDeltaB calcium imaging during tethered flight; six simulated translation directions | EPG–hDeltaB phase difference follows body-relative travel. Population comparison includes 13 flies for directional stimuli. Movement is simulated optic flow, not physical displacement through space. |
| 2 | Vector decomposition and anatomical coordinate-transform schematic | Four nonnegative components can implement signed 2D vector arithmetic. This is an explanatory construction, not independent experimental evidence. |
| 3 | PFNd/PFNv spatial tuning, dual-color heading comparisons, directional optic-flow responses | Heading-related phase and translation-related amplitude coexist in PFNs. Left/right and d/v populations supply different translation axes. Approximate sinusoidal tuning supports phasor summation. Calcium tuning does not by itself identify the molecular multiplication mechanism. |
| 4 | Sum measured PFN components using idealized or anatomy-derived offsets and weights | Predicted output phase agrees with observed hDeltaB travel phase. “No free fitted parameters” still entails modeling assumptions and measured physiological inputs. It is not a prediction from connectome counts alone. |
| 5 | Disrupt EPG transmission; suppress PFNv; inhibit LNO1; excite SpsP | Heading coupling and front/back vector balance change in the predicted directions. Readout is principally PFR_a, an imperfect downstream proxy for hDeltaB. LNO1/SpsP manipulations are indirect routes to changing PFN balance. |

### Extended Data: details that change interpretation

1. **Compartment-specific imaging matters.** hDeltaB has separated dendritic and axonal arbors with approximately opposing phases. Cytoplasmic GCaMP can mix them; sytGCaMP emphasizes the axonal output and yields a clearer single bump. Driver labels at least 16 somas versus 19 hDeltaB cells in the hemibrain. Walking data provide an additional, non-flight comparison. EPG landmark tracking is noisier in flight than walking.
2. **Dual-color controls have limits.** PFN phase aligns with EPG, but weak PFNd jRGECO signal prevented the equivalent dual-color optic-flow test in PFNd. Do not silently generalize the PFNv measurement to an identical PFNd experiment.
3. **Sinusoidalization is a proposed mechanism.** Delta7 connectivity could reshape narrow EPG activity into smoother PFN activity. Anatomical fits and observed tuning support this proposal; they do not constitute selective causal isolation of Delta7's contribution.
4. **Velocity inputs have distinct measurement contexts.** LNO1 and SpsP show inverse tuning relative to their PFN targets, both for visual translation and leg-related movement. These observations suggest sign inversion but do not directly measure every synaptic sign. Left/right preferred axes are nearer 90 degrees in noduli than in PB measurements. Proprioception and efference copy remain alternatives for movement signals in darkness.
5. **PB angles are not a single obvious lookup table.** EPG-based mapping has a central discontinuity; Delta7-based mapping imposes eight-glomerulus periodicity. The paper adjusts PFN angular labels using measured phases. A MaleCNS analysis must state its convention before interpreting an apparent angular discrepancy.
6. **Spatially resolved synapses implement phase shifts.** PFNd contacts both hDeltaB compartments; PFNv mainly targets the dendritic compartment. The approximately 180-degree dendrite–axon separation makes some inputs oppose one another at the output. Counting all PFNd→hDeltaB synapses as one positive weight loses this computation.
7. **PFR is not interchangeable with hDeltaB.** PFR phase is biased toward forward heading relative to the travel estimate; hDeltaB is closer to the expected relation in these assays. PFR driver morphology predominantly matches PFR_a, with some ambiguous cells and no clearly identified PFR_b. Backward-walking analyses select bouts with sufficient speed and consistent sideward direction; 35 qualifying trials from 10 flies are not 35 independent animals.
8. **Speed is less completely accounted for than direction.** PFN amplitudes scale with translation speed, but hDeltaB/PFR speed scaling is nonuniform across directions. Nonuniformity persists in non-flying animals, so a flight-command/optic-flow mismatch cannot explain it all. Similar modulation of PFN mean and sinusoidal amplitude supports multiplicative combination, without proving its biophysics.
9. **Mixed-selectivity analogy is theoretical.** The comparison with primate parietal cortex illustrates a representational principle; it is not evidence of identical cellular implementation.
10. **Head-yaw cancellation has conditions.** If both heading and visual velocity are referenced to the head, yaw offsets can cancel in the transform. Combining a head-based compass with body/leg-based velocity requires additional accounting. This panel is a geometric argument, not a head-yaw perturbation experiment.

## Methods audit

Female flies, 2–6 days old; the principal assay uses tethered flight with wingbeat asymmetry controlling landmark yaw. The arena spans 270 degrees in azimuth; translational flow is always open loop. A virtual starfield simulates motion, generally at 35 cm/s, with additional speed conditions. Thus reported metric speed depends on the virtual scene's depth structure. Real-world clutter and multisensory consistency could affect generalization.

Imaging samples 3–5 z planes at approximately 4–10 volumes/s. PB phase uses a Fourier component with eight-glomerulus periodicity; EB and FB phase use population-vector estimates. Each fly's arbitrary landmark-to-bump offset is calibrated as a constant. Some comparisons interpolate to a common 10-Hz time base to account for acquisition timing. This supports relative angular comparisons, not an anatomically hard-coded absolute north.

Fluorescence normalization uses low-percentile baseline and, for some analyses, per-ROI dynamic-range normalization. The latter assumes differences in dynamic range mainly reflect recording/expression differences. The authors report that conclusions survive normalization and interpolation choices; reproducing that robustness requires the raw analysis, not merely rerunning the conceptual model.

Most genotypes lose fewer than 5% of flies to preparation/flight criteria, but approximately 70% are excluded in the heavily transgenic Fig. 5e–p experiments because of poor flight. This makes selection and state dependence particularly important for perturbation interpretation. Sample sizes were based on prior practice, not prospective power calculations; investigators were not blind to genotype. Tests include unpaired t-tests and circular Watson–Williams comparisons. Interpret observations at the fly level, retaining repeated-trial structure.

## The vector calculation, reconstructed

Let body-relative travel angle be beta = T − H. Four preferred axes are phi = {45, −45, −135, 135} degrees. Ideal nonnegative amplitudes are A_i = alpha + cos(beta − phi_i), with alpha at least 1. The spatially varying input is

    I(theta) = sum_i g A_i cos(−H − theta − phi_i) + constant.

Equal weights and the four evenly spaced axes cancel the baseline's directional component. Product-to-sum identities leave

    I(theta) = 2g cos(T + theta) + constant.

Therefore its maximum is theta = −T, given the paper's neural-angle convention. Reversing plotting conventions reverses this sign without reversing the computation. For unequal measured amplitudes and weights, calculate

    theta_peak = −H − atan2(sum_i g_i A_i sin(phi_i),
                           sum_i g_i A_i cos(phi_i)).

Use atan2, not a single-argument arctangent: backward travel needs the correct quadrant. If both components vanish, phase is undefined; software should report this rather than manufacture a direction. A monotonic postsynaptic nonlinearity can preserve the maximum, so a linear hDeltaB firing-rate response is not required. Linear summation of the modeled inputs is an assumption.

The anatomy-informed weights are approximately 92.9, 98.0, 67.0, 74.3, with angular offsets 44.5, −41.5, −131.5, 136.5 degrees. The d weights subtract dendritic from axonal contributions: for example 257.3 − 164.4 = 92.9. This assumes negligible compartment-dependent attenuation. Physiological PFN amplitudes are normalized by each population's average across tested movement directions. These are essential ingredients of the model, not hidden parameters we should omit when calling it constrained.

## What the separate supplementary text contributes

The supplement supplies the analytic cancellation above and explains why nonnegative four-axis components can encode a signed vector. It explicitly separates coordinate transformation from path integration: these measurements do not demonstrate PFNd/v accumulating position over time. Its discussion of Delta7 smoothing, alternative nonorthogonal bases and potential changes in input weighting proposes mechanisms to test. They are not additional demonstrated facts.

A useful next question is whether context changes the effective velocity basis, the anatomical transform, or only input gain. Those hypotheses can agree in one visual assay but diverge under head rotation, unusual optic-flow depth distributions, or independent visual and leg-motion perturbations.

## Movies

Video 1 animates the four PFN components as body-relative travel rotates through a full circle at fixed heading. The output bump rotates while the heading bump stays fixed; it illustrates the analytic model rather than adding biological samples. Video 2 shows EPG/PFR imaging and tethered behavior across static flow, progressive flow, and static flow again. The progressively moving scene tightens their phase relationship. The example is useful for seeing temporal variability hidden in averaged plots, but remains a single illustrative recording.

## Applying this to MaleCNS

The original anatomical analysis uses **female hemibrain v1.1**. Our dataset is **male whole-CNS v1.0**. Body IDs, cell counts, and type granularity are not transferable by assumption. Preserve PFNd/PFNv side, PB glomerulus, FB column and hDeltaB compartment information. The currently downloaded body-to-body graph can identify candidate cells and aggregate pathways; it cannot alone reproduce compartment-specific angular shifts.

Priority analyses: validate cross-dataset type correspondences; obtain spatial synapses for selected PFN/hDeltaB cells; estimate projection-phase kernels by compartment; compare equal-axis and measured-axis predictions; test sensitivity to missing cells, thresholding, gains, and dendritic attenuation. An apparent failure of the ideal orthogonal model could arise from angular indexing or sampling rather than a different computation.

## Remaining questions

This paper strongly constrains a coordinate transformation. It does not alone establish a full naturalistic velocity metric, location memory, goal selection, or steering policy. Its causal perturbations constrain vector balance but are not a direct selective perturbation of every proposed link. These boundaries are precisely why this circuit is unusually tractable without being completely solved.

Author analysis code: https://github.com/Cheng-Lyu/TravelingDirectionPaper_code (linked by the paper; not executed in this reading).

### Where do the sinusoids come from, and how perfect must they be?

This is a central mechanistic question, not merely a fitting detail. Two different approximately sinusoidal relationships enter the ideal model:

1. **Spatial tuning:** activity across PB glomeruli at a given moment has a dominant first spatial harmonic, with phase tied to heading.
2. **Movement tuning:** each PFN population's amplitude varies approximately as the projection of body-relative velocity onto its preferred axis.

The first makes spatial summation equivalent to phasor addition. The second, together with the anatomical offsets and gains, makes the resulting phasor point along allocentric travel. Either can fail independently.

**What Lyu actually establishes.** Fig. 3 and Extended Data Fig. 3 show profiles compatible with sinusoidal fits. Methods describe phase alignment, averaging, fitting and goodness-of-fit tests. Failing to reject a sinusoidal model is not proof of exact sinusoidal activity. Finite spatial sampling, calcium measurements and averaging limit sensitivity to deviations. Phase alignment itself does not force a sinusoid, but averaging can obscure trial-specific departures. Useful follow-up: quantify harmonics within individual flies and trials, alongside uncertainty, rather than inspecting only the mean fitted bump.

**The proposed generator.** Supplementary Information p2 explicitly proposes Delta7-mediated reshaping. Broad, spatially structured inhibitory input could transform a more localized EPG bump into a more sinusoidal PFN profile. Delta7 also feeds back to EPG. This is supported by anatomical and physiological observations, but selective causal proof that Delta7 generates the required PFN waveform is not supplied by this paper. Nor does saying “Delta7” finish the explanation: we still need to explain its projection kernel, effective synaptic signs and strengths, interaction with direct EPG input, and robustness across state and animals. Delta7-mediated spatial shaping also does not by itself explain the separate movement-direction tuning of PFN amplitudes.

**Why perfect sinusoids are not strictly necessary.** The following is our mathematical analysis, not an additional experimental result from Lyu. Use an angular convention in which an output centered on alpha has first-harmonic phasor proportional to exp(i alpha). Any real activity profile can be expanded as

    f(theta) = c0 + sum_{n>=1} [c_n exp(-i n theta) + conjugate(c_n) exp(i n theta)].

A spatial shift f(theta-alpha) multiplies c_n by exp(i n alpha). Under linear summation, the first harmonic therefore obeys

    C1 = sum_k g_k c_{k,1} exp(i alpha_k),

regardless of what other harmonics are present. First-harmonic phasor addition is still exact. To obtain the intended travel vector, these first-harmonic coefficients must also have the appropriate movement dependence and relative gains.

What fails for an arbitrary waveform is the stronger assertion that **the maximum of the entire output profile equals the phase of its first harmonic**. Higher harmonics can shift the maximum, produce multiple peaks, or distort a downstream nonlinear readout. A circuit that selectively reads the first harmonic could tolerate substantial waveform distortion; a peak-following circuit may tolerate less. An experimenter's population-vector decoder is not evidence that the biological downstream circuit implements that decoder. With finite columns, discrete sampling can also alias higher harmonics into the estimated first harmonic.

**A possible filtering mechanism.** In an ideal translation-invariant ring, synaptic convolution becomes multiplication in Fourier space:

    Y_n = K_n X_n.

A kernel with strong first-harmonic transmission and weak higher-harmonic transmission can extract a sinusoidal component from a sharper input. This provides a useful mathematical interpretation of the Delta7 proposal. Generic broad inhibition is not sufficient: its spatial structure and combination with excitation matter. Actual PB circuitry is finite, anatomically heterogeneous, and not automatically a translation-invariant convolution.

Four evenly spaced PFN axes do not cancel every possible waveform distortion. In the equal-axis construction with the ideal amplitude rule, some higher harmonics survive, including a third spatial harmonic. Thus fourfold symmetry alone does not establish robustness. Conversely, a pointwise strictly increasing output nonlinearity preserves the location of an input maximum even if it distorts the waveform; the paper does not require hDeltaB firing rate to remain sinusoidal or linear.

**Experiments and analyses to distinguish these possibilities:** measure trial-level PFN and hDeltaB spatial harmonics; perturb Delta7 while monitoring changes in waveform and heading phase separately; estimate compartment-resolved anatomical kernels and test whether plausible effective weights suppress higher modes; introduce controlled harmonic and gain errors into the model; compare predictions from a first-harmonic decoder, a peak decoder, and a biologically specified downstream readout. Evaluate error especially when the desired resultant is weak, where small distortions can dominate phase.

### Open questions within and beyond the coordinate transform

| Question | Why the existing result does not close it | Discriminating direction |
|---|---|---|
| How is body-relative velocity calibrated? | Optic flow depends on scene depth as well as speed; leg movement and actual displacement can differ. | Independently vary visual depth, visual motion and leg motion; quantify direction and speed errors separately. |
| How are gains, axes and compartments calibrated? | Synapse counts are not physiological weights; the model assumes how opposing compartmental contributions combine. | Test sensitivity to side-specific gains, angular mapping and dendritic attenuation; seek developmental or plastic calibration mechanisms. |
| Does magnitude represent speed, confidence or state? | Weak first-harmonic output can arise from weak input, cancellation or gain suppression. | Dissociate speed, cue conflict and behavioral state. A single complex first moment cannot preserve a general multimodal directional distribution. |
| How do compass and goal remain aligned after remapping? | A changed landmark-to-compass offset could invalidate a memory expressed in the old coordinates. | Track heading and goal representations together through cue conflict and relearning. Basnak et al. demonstrate cue integration/remapping, not a complete solution to cross-memory consistency. |
| Where is displacement integrated and corrected? | Instantaneous travel direction is distinct from the time integral of metric velocity. | Identify integration, leak, resets and landmark correction; distinguish persistent direction from accumulated position. |
| What is learned about a food source? | A goal bearing, place vector, visual scene and action sequence can produce similar trajectories in restricted assays. | Displacement and cue-rearrangement tests that distinguish these strategies; do not assume nest-like round trips are the relevant natural behavior. |
| How is a goal selected and retrieved? | A heading–goal comparator does not explain which goal should be active under hunger, competing rewards or uncertainty. | Connect learning and internal state to changes in the represented goal, not only steering output. |
| How does steering become successful closed-loop behavior? | Turning toward a bearing does not alone compensate for drift, obstacles or changes between walking and flight. | Predict trajectories, speed and behavioral switching under independently manipulated sensory and motor conditions. |
| Do the components work together in one animal? | The anatomical and functional evidence combines different preparations, individuals, datasets and conditions. | Build a quantitatively specified model that predicts joint representations and perturbation-induced behavioral errors, with parameters constrained across tasks. |

The newer work gives concrete partial mechanisms: FC2/PFL3 goal-to-steering comparisons, PFL2/PFL3 steering control, multisensory compass learning, and odor-dependent evidence integration/persistence. It would be inaccurate to label those entire topics unknown. Equally, those findings do not by themselves establish a unified system for finding, remembering and revisiting a food location.

Context sources (targeted checks, **not completed full-paper readings**):

- [Mussells Pires et al., 2024 — goal-to-steering transformation](https://www.nature.com/articles/s41586-023-07006-3).
- [Westeinde et al., 2024 — heading-to-steering transformation](https://www.nature.com/articles/s41586-024-07039-2).
- [Basnak et al., 2025 — multimodal cue integration and learning](https://www.nature.com/articles/s41593-024-01823-z).
- [Kathman et al., 2026 — working memory and odor evidence integration](https://www.nature.com/articles/s41467-026-75945-2).
