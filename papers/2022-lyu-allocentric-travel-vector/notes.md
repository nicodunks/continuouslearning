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

## Remaining uncertainty

This paper strongly constrains a coordinate transformation. It does not alone establish a full naturalistic velocity metric, location memory, goal selection, or steering policy. Its causal perturbations constrain vector balance but are not a direct selective perturbation of every proposed link. These boundaries are precisely why this circuit is unusually tractable without being completely solved.

Author analysis code: https://github.com/Cheng-Lyu/TravelingDirectionPaper_code (linked by the paper; not executed in this reading).
