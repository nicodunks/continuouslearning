# Seelig & Jayaraman (2015): Neural dynamics for landmark orientation and angular path integration

[Paper](https://doi.org/10.1038/nature14446) · [Local PDF](main.pdf) · [Exact reading coverage](reading-log.md)

## What this contributes to a complete navigational behavior

This paper establishes a candidate internal angular reference: a localized activity bump in ellipsoid-body neurons tracks orientation relative to a visual scene, can update with self-motion in darkness, and retains an orientation-related state during pauses. The original name is EBw.s-PBg.b-gall.b; this population is commonly called EIP/EPG in subsequent work.

The motivating behavioral contribution is continuity. A fly needs some way to relate successive views and movements even while landmarks are unavailable. An angular state is a useful component of that computation. This paper does not establish a remembered food location, distance traveled, a return vector, target selection, or the downstream motor use of the state. Its angular path integration should not be silently expanded into two-dimensional spatial path integration.

## Experiment and measured variables

Head-fixed female flies walk on an air-supported ball while the authors image GCaMP6f in the EB under R60D05-GAL4. Five optical planes cover the EB, acquired at approximately 8.5 volumes/s. Sixteen manually defined wedge ROIs sample activity around the ring. Most experiments use a 6-mm, approximately 40-mg ball; darkness controls also use a 10-mm, approximately 175-mg ball. The preparation restricts head movement and is not natural free walking or flight.

A display covers 270° horizontally and 120° vertically. A bright stripe, a scene with multiple features, or two identical stripes moves in closed loop with ball rotation. Patterns wrap directly between the display's endpoints. Consequently, the two stripes are separated by 135° on the physical display, rather than two ordinary landmarks 180° apart in a continuous 360° environment. The 270° display range is rescaled to a full 360° EB representation for comparisons. A plotted gain near one therefore incorporates this coordinate convention.

The visual experiments remove the funiculus and arista. Some darkness experiments paint the eyes black. These manipulations matter when connecting this result to later wind and multisensory experiments: this preparation does not establish how an intact fly combines antennal signals with vision.

The major observations are calcium fluorescence and ball kinematics. The population-vector angle is an analysis-derived variable, not a directly measured downstream neural signal. Trial counts and walking-bout counts must not be confused with independent flies: the main visual groups include 15 single-stripe flies, nine multiple-feature flies and seven two-stripe flies; darkness includes 11 flies on the small ball and 13 on the large ball.

## Figure-by-figure reasoning

### Figure 1: a movable population bump

Imaging reveals a localized EB activity bump whose angular position follows the stripe during closed-loop walking. The activity can move around the EB while preserving a broad localized profile. The relationship has an offset that differs across flies and can change between trials. This is already inconsistent with a simple universal anatomical map in which one fixed wedge always means one particular retinal stripe position.

The paper interprets the bump as an internal orientation representation anchored to a landmark. That interpretation is stronger than saying these cells respond to vision, but it is still a representation claim. No selective manipulation here establishes that the fly uses the bump to steer.

### Figure 2: one angular state in a richer or ambiguous scene

A scene containing several visual features still generally produces one bump. Two identical stripes also generally produce one bump rather than two independent copies of the visual scene. This supports an internally selected orientation state rather than a literal image of every salient object.

Single-stripe and multiple-feature mean bump widths are about 82.3° and 84.9°, respectively; the reported comparison is not significant. This is not proof of exactly equal shapes. The two-stripe width is approximately 78.7° and differs statistically from the single-stripe condition in Extended Data. The careful statement is that broadly similar localized bumps occur across these scenes, not that the network enforces an invariant mathematical waveform.

A one-angle decoder necessarily discards ambiguity, but the authors also inspect/count bumps in the spatial activity itself. Thus, the single-bump result is not merely a trivial consequence of plotting one PVA angle. Occasional multiple bumps and short transitions are present.

### Figure 3: vision can correct a self-motion-related estimate

Abrupt stripe shifts put visual and self-motion information in conflict. Across 50 jumps in six flies, the bump generally relocates so that its relationship to the visual cue is preserved. Altering closed-loop gain similarly makes the neural estimate more consistent with scene movement than with unscaled ball rotation in most tested conditions.

Neither result establishes instantaneous or unconditional visual dominance. Examples show delayed relocking, and a low-gain example in Extended Data follows ball rotation more closely. The measurements concern a particular bright-landmark preparation; they do not provide a universal cue-weighting law for every natural scene.

### Figure 4: updating and retention without visual landmarks

In darkness, the bump often tracks accumulated ball rotation, with drift and gain errors. It can remain localized when the fly stops. Some pauses exceed 30 s, while the average pause used in the main comparison is about 6.7 s. The reported pre/post angle difference averages near zero but has substantial spread, approximately 0.76 radians. Near-zero mean error is not perfect trial-by-trial retention.

Activity sometimes becomes weak during standing and reappears in approximately the same wedges when walking resumes. This supports retention of an internal state beyond the immediate sensory input. It does not identify whether the entire memory is maintained by persistently elevated firing in the imaged population; weak or unobserved states elsewhere could also contribute.

## Extended Data: the qualifications that matter

| Figure | Contribution and interpretation |
|---|---|
| ED1 | Defines the stimulus geometries and distributions of forward, lateral and rotational movement across conditions. Different preparations should not be assumed to sample identical behavior. |
| ED2 | Single-stripe population results: generally one bump, broad width distribution and heading/cue tracking. The average fitted gain across 172 walking epochs is about 0.92, with considerable spread. Bump-count thresholds are analysis choices. |
| ED3 | Multiple-feature scenes: a single angular representation persists; the average fitted gain across 74 walking epochs is approximately 0.97. Offset can change across trials. |
| ED4 | Identical stripes: a single bump is common and gain is approximately 1.08 across 96 walking epochs. The modest width difference from the single-stripe condition is statistically significant. |
| ED5 | An example changes which identical stripe anchors the bump, especially around 38–42 s. An ambiguous view need not have a permanently fixed mapping to the internal state. |
| ED6 | Individual cue-jump/gain examples reveal delayed capture and exceptions to simple visual dominance. Population conclusions must retain these dynamics. |
| ED7 | Darkness produces wider bumps on average, about 90.9° versus 82.3° with a stripe, and variable angular gain. Larger-ball experiments also show gain below one. This is not a perfectly calibrated inertial compass. |
| ED8 | Per-fly scatter plots expose discrepancies that accumulated traces can obscure. Low rotational velocities are not always captured, and neural drift often accompanies weak PVA amplitude. This is a qualitative relation, not a validated probabilistic uncertainty decoder. |
| ED9 | Brief high/low visual-gain exposure does not produce strong matching recalibration in subsequent darkness. The post-high versus post-low comparison nevertheless has a reported P value of 0.04: do not turn “little recalibration” into “literally no difference.” |
| ED10 | Retention is examined before restart and at restart in darkness and visual scenes. Most pauses are short, with some much longer. Angular scatter remains substantial. The small-ball before-restart analysis uses 449 bouts, whereas the main text's related comparison uses 499; these are not interchangeable counts. |

ED9 is particularly useful for a navigation synthesis. In the visual phase, fitted gains average about 0.86 in the high-gain condition and 0.54 in the low-gain condition. Subsequent darkness gives approximately 0.57 and 0.46, respectively, with broad distributions. The experiment uses short exposure and selected flies with sufficient rotation and relatively low drift. It does not rule out learning over longer times, other experience statistics, or plasticity of the visual-to-compass offset rather than angular velocity gain.

## The mathematics, using complex exponentials

Let wedge centers be

\[
\phi_j=2\pi j/N,\qquad N=16,
\]

and let the measured fluorescence responses be \(r_j(t)\). The essential population-vector operation is

\[
Z(t)=\sum_{j=0}^{N-1}r_j(t)e^{i\phi_j},\qquad
\hat\theta(t)=\arg Z(t).
\]

Multiplying the sum by a positive normalization constant changes its magnitude but not its phase. The angle is undefined when the resultant vanishes and becomes noise-sensitive when it is small. The paper's PVA strength carries fluorescence units; it is not automatically a calibrated measure of certainty.

### Why perfect sinusoids are unnecessary here

Suppose the activity is a translated bump,

\[
r(\phi,t)=b+A f(\phi-\theta(t)).
\]

For a continuously sampled ring,

\[
Z(t)=\int_0^{2\pi}r(\phi,t)e^{i\phi}\,d\phi
=Ae^{i\theta(t)}\int_0^{2\pi}f(u)e^{iu}\,du.
\]

If the first angular harmonic of the bump is nonzero and stable, its phase follows \(\theta\), up to a fixed offset. The bump can be narrow, broad or non-sinusoidal. A symmetric bump centered at zero typically gives a real positive first-harmonic coefficient; asymmetric shapes can introduce an offset.

A spatial Fourier expansion makes the operation explicit:

\[
r(\phi)=\sum_{k\in\mathbb Z}c_ke^{ik\phi},
\qquad Z=2\pi c_{-1}
\]

under this sign convention. The decoder selects a harmonic; it does not prove that all the other harmonics are absent. With sixteen samples, high harmonics can alias, and uneven anatomical sampling, ROI errors and shape changes can bias phase. Consequently, “perfect sine waves are unnecessary for decoding a translated bump” does not imply that arbitrary tuning distortions are harmless to every downstream vector computation.

The later Lyu computation asks a different question: how multiple directional and velocity-dependent signals combine so that a downstream population carries a travel vector. One must examine those transfer functions and nonlinearities separately. Seelig's PVA extraction is not itself evidence that the biological downstream circuit implements the same linear decoder.

### What angular integration means

An ideal angular integrator obeys

\[
\theta(t)=\theta(0)+\int_0^t\hat\omega(s)\,ds,
\qquad z(t)=e^{i\theta(t)},\qquad \dot z=i\hat\omega z.
\]

This is an explanatory idealization, not a fitted circuit equation reported here. Gain error and noise make the estimate drift. Visual landmarks can anchor or reset its phase, but the paper does not identify the synaptic implementation of that correction.

By contrast, a spatial position estimate would require

\[
\hat x(t)=\hat x(0)+\int_0^t\hat v(s)\,ds,
\qquad \hat v=s(t)e^{i\psi(t)}.
\]

Heading \(\theta\) and traveling direction \(\psi\) differ during sideways/backward motion. A return vector to a remembered location \(x_g\) is \(g=x_g-\hat x\). Nothing in the 2015 experiment establishes that integral, the stored \(x_g\), or its motor readout.

### Shared reference frames are the key neighboring-circuit issue

A fly-specific compass offset is harmless if all relevant variables share it. If heading and a goal bearing both use an offset \(\alpha\),

\[
z_h=e^{i(\theta+\alpha)},\qquad
z_g=e^{i(\gamma+\alpha)},\qquad
z_g\overline{z_h}=e^{i(\gamma-\theta)}.
\]

The offset cancels. But if the compass relocks to a new cue while the stored goal remains in the old frame, that cancellation fails. The ambiguous-cue switches therefore pose a real question for complete behavior: how are stored goals or displacement estimates transformed, relearned or selected when the heading reference changes? This paper does not answer it.

## Methods and analysis details that change the interpretation

Planes are averaged and fluorescence is spatially filtered. Wedge signals use a low-fluorescence baseline based on the lowest 10% of frames in a trial. Temporal smoothing includes a seven-frame third-order Savitzky–Golay filter, approximately 822 ms, and a three-frame PVA boxcar, approximately 352 ms. The display images also use smoothing; those display settings should not be confused with the quantitative ROI calculation.

The plotted phase offset is estimated after the fact using the median circular difference during walking in the final 80% of a trial. Thus, good overlay after alignment does not demonstrate a universal online decoder with a known anatomical zero. The visual cue's retinal motion also has the opposite relationship to physical head rotation under a conventional fixed-world coordinate system; sign and display scaling must be checked before comparing equations across papers.

Several correlations compare unwrapped accumulated trajectories. Smooth accumulated time series can correlate strongly while local errors remain important. Gains are fit over walking epochs or 200-frame windows, about 23.5 s, with overlapping windows stepped by 25 frames. Such samples have temporal dependence. ED8 is valuable because it exposes local failure and drift more directly.

Standing bouts require at least 20 frames, about 2.35 s, with walking flanks and short pre/post averaging windows. Most retention measurements are consequently seconds-long, not demonstrations of indefinite memory. Calcium kinetics are much faster than the longest reported persistence, but the cited indicator kinetics are not a direct simultaneous calibration of EPG spikes in these recordings.

Bump width is measured after subtracting the frame minimum; bump counts use thresholding, including mean-plus-standard-deviation criteria. Neither metric establishes an exact dynamical attractor manifold. The paper discusses ring-attractor mechanisms as an explanation, but does not perturb the state to establish recovery, identify recurrent synapses, or distinguish all intrinsic and network mechanisms.

## Supplementary movies

All eight captions were read and 24 frames spanning each downloaded movie were inspected. This is sampled inspection, not frame-complete playback or a new quantitative analysis.

Movies 1–3 show the moving localized activity, behavior and cue/PVA traces for the three visual scenes. Movie 4 shows changing alignment to the two identical stripes. Movie 5 illustrates cue jumps, including a delayed return to alignment after the second jump. Movies 6–8 show dark updating and pause-related persistence, including the larger-ball/painted-eye control. The dark traces use different vertical scales for accumulated neural phase and ball rotation; their visual overlap is not unit-gain evidence. Playback is accelerated, and traces are smoothed. Those details prevent overinterpreting a compelling demonstration movie as a calibrated instantaneous readout.

## Remaining questions and productive connections

1. **How is the bump generated and stabilized?** The observed localization does not identify the recurrent mechanism. The ring-attractor perturbation, angular-integration and ultrastructural papers are necessary next links.
2. **What supplies angular velocity, and with what gain?** Proprioception, efference copy and other self-motion signals are not disentangled here. Darkness performance varies with preparation and speed.
3. **How does the network choose and learn a visual anchor?** Trial-dependent offsets and switches between identical landmarks motivate the later visual remapping/plasticity papers.
4. **What does low amplitude mean?** It can accompany drift, but fluorescence strength also depends on activity, imaging and state. A confidence interpretation needs a defined estimator and behavioral test.
5. **What preserves state when visible activity weakens?** Recurrent activity, subthreshold states, other cell populations and intrinsic mechanisms remain candidates in this paper.
6. **How does the heading estimate guide action?** A downstream goal comparator is absent here; the later goal/steering papers supply a distinct step.
7. **How does a persistent direction become a remembered place?** Translation integration, reward-triggered reset/storage, landmark-based relocalization and stopping at arrival are separate missing operations.

For connectomic work, the immediate value is to constrain candidate implementations of a measured angular state and its sensory/motor interfaces. A ring-shaped anatomy alone does not settle the dynamical mechanism or prove spatial memory. Subsequent structural analysis should preserve this distinction and explicitly connect a proposed neuron function to one missing operation in behavior.
