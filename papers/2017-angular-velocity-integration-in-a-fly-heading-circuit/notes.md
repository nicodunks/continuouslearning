# Turner-Evans et al. (2017): angular velocity integration in a fly heading circuit

[Paper and published reviews](https://elifesciences.org/articles/23496), DOI **10.7554/eLife.23496**. Daniel Turner-Evans, Stephanie Wegener, Hervé Rouault, Romain Franconville, Tanya Wolff, Johannes Seelig, Shaul Druckmann and Vivek Jayaraman.

## What this contributes to a complete navigation behavior

A fly that turns while remembering a destination needs to update its orientation. This paper identifies a candidate implementation: P-EN neurons combine heading with signed angular velocity, and their spatially shifted recurrent interactions with E-PG compass neurons can move the compass bump. The evidence includes single-cell voltage/spikes, simultaneous population imaging, functional stimulation, synaptic blockade and a rate model.

The represented state is **heading**, not position, distance travelled, a food location or a desired direction. The paper supplies an important upstream operation for Lyu's body-to-world transformation and for the later heading–goal steering comparison. Neither the destination memory nor the behavioral readout is established here. Its own discussion explicitly distinguishes the experimenter's population-vector decoder from whatever downstream neurons actually compute.

The strongest causal result is that P-EN output helps maintain the strength and stability of E-PG activity. Blockade does not cleanly freeze the compass; activity can become weak and move erratically. Consequently this experiment does not establish that these P-ENs are the exclusive route for angular updating.

## Preparation, identity and conventions

- Imaging: head-fixed walking females, 7–10 days old, 8-mm/92-mg ball; E-PG R60D05 and P-EN R37F06 with GCaMP6f/jRGECO1a, including reversed indicator assignments. EB/NO volumes at 11.4 Hz; some PB volumes at 6.2 Hz.
- Electrophysiology: 1–2-day-old females, an 8-mm/47-mg ball, 4-kHz movement tracking and 20-kHz recording. Darkness or a closed-loop 15° stripe. The display covers 240°; physical gain 1 is subsequently mapped to a 360° analysis arena. Keep physical rotation, displayed position and analysis heading distinct.
- R37F06 additionally labels PFNv neurons. NO1 imaging avoids their NO2 compartment. The second driver VT008135 labels P-ENs as its only PB population, but has other cells elsewhere. Anatomical specificity is regional, not universal.
- P-EN here is the historical population label. The paper acknowledges a second subtype described by Green et al. (2017). Do not silently identify every historical P-EN experiment with every modern PEN subtype.
- Left/right refer to PB and cell-body side. Axons innervate the **contralateral** nodulus. Confusing nodular side with soma side reverses the sign of angular tuning.

## The computation, using complex exponentials

Write the heading state as

\[
z(t)=e^{i\theta(t)},\qquad \dot z=i\omega(t)z,
\qquad z(t+\Delta t)=e^{i\omega\Delta t}z(t).
\]

These equations specify the desired computation, not a measured cellular equation. Maintaining an angle means retaining phase when angular velocity is zero; integrating a turn means rotating phase by the accumulated angular velocity.

For a population at angular coordinates \(\phi_j\), define

\[
Z=\sum_j r_j e^{i\phi_j},\quad \widehat\theta=\arg Z.
\]

A translated localized profile \(r(\phi)=b(\phi-\theta)\) has a first angular moment proportional to \(e^{i\theta}\), provided its first harmonic is nonzero. It need not be a perfect sinusoid. Symmetry of the profile and stable sampling make its phase a useful center; asymmetry, unequal gains and weak activity can bias or destabilize it. This does not by itself prove that the fly implements this exact readout.

A conceptual shifted-loop calculation helps explain the anatomy. Suppose the two P-EN pathways inherit the current bump and project shifted versions back by \(\pm\delta\), with turn-dependent strengths \(a_+\) and \(a_-\). Their first-harmonic feedback is

\[
Z_{\rm fb}\propto\big(a_+e^{i\delta}+a_-e^{-i\delta}\big)Z.
\]

The imaginary part of the coefficient changes phase; its real part changes support for the bump. Equal strengths cancel the phase drive. A left–right imbalance creates phase motion. This is an explanatory reduction, **not** the complete published model or proof of exact multiplication by angular velocity.

The cell data show conjunctive tuning, but do not demonstrate a literal product \(r=h(\theta)\omega\). Heading and turn signals can be combined additively in membrane potential and sharpened by spike threshold. Both variables retain weaker tuning even under the other's nonpreferred condition.

### What the published rate model adds

There are 54 E-PG units and 18 P-EN units, nine per side. E-PGs receive spatially offset P-EN excitation; P-ENs receive local E-PG excitation, effective broad inhibition, a tonic drive, and a rectified turn input. Schematically,

\[
\tau_E\dot E=-E+[W_{EP}P]_+,
\qquad
\tau_P\dot P_\pm=-P_\pm+
[W_{PE,\pm}E-W_{I}E+1+[\pm v]_+]_+.
\]

Here the matrices, their normalization and the velocity-to-drive gain matter; the schematic equation is not an implementation specification. The inhibitory population is implicit. E-PGs have no autonomous recurrent ring in this model: persistence emerges through the cross-population loop.

The Methods use von Mises kernels. In exponential notation,

\[
f(\phi\mid\mu,\kappa)=
\frac{\exp\{\tfrac\kappa2[e^{i(\phi-\mu)}+e^{-i(\phi-\mu)}]\}}{2\pi I_0(\kappa)},
\]

with \(\kappa=12\), and

\[
K_L(\phi)=\tfrac12 f(\phi\mid0,\kappa)+f(\phi\mid35^\circ,\kappa),\quad
K_R(\phi)=\tfrac12 f(\phi\mid0,\kappa)+f(\phi\mid-35^\circ,\kappa).
\]

These are localized profiles with higher harmonics, not pure sinusoids. The Methods give \(\alpha=10,\beta=25,\tau_E=80\) ms and \(\tau_P=65\) ms. Time constants were selected to account for observed phase offsets; they are not independently measured membrane constants.

Delayed response to a moving input gives an approximate spatial lag \(\omega\tau\). Thus P-EN activity can lag E-PG in the bridge but lead it in the EB, where the projection is anatomically shifted. The Methods estimate saturation as \(v_{\rm sat}\approx\Delta/(\tau_E+\tau_P)\). This connects wiring displacement to a time scale and a maximum update rate; geometry alone does not fix the gain.

The model is approximately linear over a useful range after calibration, saturates at high turn rates and sticks at low velocities below about 15°/s. The authors did **not** observe this low-speed sticking in their imaging data. It exposes missing smoothing mechanisms or oversimplified discretization. The model assumes units in all nine PB positions to close the loop, simplifying the real inner/outer-glomerulus mismatch.

For randomly varying input, an Ornstein–Uhlenbeck process approximates movement statistics: 120-ms correlation and 50°/s stationary SD, informed by measured 128 ms and 54°/s. Network dynamics themselves are deterministic in this demonstration. Reported integration-error growth is

\[
\mathbb E[(\theta_{\rm input}-\theta_{\rm bump})^2]
\approx\sigma_0^2+2Dt,
\quad D=1.82\times10^{-3}\ {\rm rad^2/s}.
\]

This is a **simulation** error coefficient, not measured biological compass diffusion. The estimator is an uncentered squared-error statistic, interpreted as variance under the near-zero-mean error assumption. Figure 10 supplement 1 reports a roughly 30-ms lag from the supplied P-EN input to bump velocity; this is distinct from the approximately 130-ms neural lag after the fly's actual turn.

## Figure-by-figure evidence

| Figure | Observation and interpretation | What remains conditional |
|---|---|---|
| 1 | E-PG wedge-to-bridge and P-EN bridge-to-offset-tile anatomy motivate two oppositely shifted feedback loops. Example E-PG phase follows dark walking. | Arbor overlap suggests connectivity; this is not a synapse-resolved reconstruction. |
| 2 | Left/right nodular calcium alternates with turning; R−L signal correlates with filtered angular velocity, mean R=0.65±0.14 across ten flies. Forward-speed tuning is weak/inconsistent. | Behavioral filtering incorporates indicator kinetics; nodular activity pools cells and is not individual-cell evidence for heading tuning. |
| 3 | Whole-cell recordings show depolarization/spiking during ipsilateral turns and suppression during contralateral turns. | Responses outlast individual turns, so instantaneous movement and voltage peaks need not coincide. |
| 4 | Twelve cells show mirrored sigmoid angular tuning, mean fit R²=0.87±0.01; modulation 5.6±3.7 Hz and bandwidth 145±82°/s. Spike-triggered and regression analyses put neural response after turns, about 123 and 130 ms respectively. | Lag suggests feedback but does not identify proprioceptive input or exclude every motor-related contribution. Each cell responds across both turn signs rather than being an ideal one-sided detector. |
| 5 | Heading×velocity maps demonstrate conjunctive tuning; short selected epochs and longer recordings give compatible preferred angles. | One of six long visual recordings lacks adequate sampling; one short epoch fails significance. Short epochs were selected for sufficiently broad, balanced movement coverage. |
| 6 | Spiking modulation is larger when the other variable is preferred; weak tuning survives nonpreferred conditions. Membrane-potential modulation is less conjunctive. | Threshold sharpening is plausible; exact multiplicative computation and equality of nonsignificant conditions are not established. |
| 7 | P-EN presynaptic marker is stronger in EB/NO; E-PG has PB **and EB** presynaptic labeling. Ex-vivo P-EN activation excites E-PG. E-PG activation evokes variable P-EN responses at weak stimulation and more consistent excitation at strong stimulation. | Direct versus indirect transmission and recruitment of inhibition remain unresolved. Weak/strong illumination is 50/500 μW/mm², not mW/mm². |
| 8 | Two-color bridge imaging shows overlapping but shifted bumps, with P-EN following E-PG by roughly one glomerulus at fast turns. Width changes little; amplitudes rise. | Contralateral P-EN dendritic calcium rises even when corresponding spike output is suppressed. This is a substantive compartment-level discrepancy. Averaging method changes estimated offsets. |
| 9 | EB P-EN calcium leads E-PG during turns; mean offset rises from about 2.5° at slow turns to 20.7° at 150–180°/s for one indicator pairing. Widths remain roughly constant. | Reversing indicators yields smaller offsets, about 7.3° at the fastest bin; the supplement's across-bin ANOVA is nonsignificant, p=0.26. Qualitative agreement does not identify an exact physiological phase-delay curve. |
| 10 | Rate model produces a persistent bump, qualitative PB/EB phase relations and approximately linear angular integration; random-input tests show tracking with accumulating error. | Effective inhibition, simplified topology, tuned parameters and input calibration are supplied. Low-speed pinning and some amplitude relationships disagree with biology. |
| 11 | At restrictive temperature, P-EN shibire blockade prevents the normal activity-associated increase in E-PG bump strength or reduces it; two drivers support the result. Tracking becomes less reliable. | Blockade strength is unknown, temperature changes locomotion, and weakened bumps sometimes move dramatically. This is not a clean loss of angular motion alone. |

## Scientific supplements and published review: details that change interpretation

**Figure 4 supplements 1–2:** the approximately constant population sum is constructed from normalized recordings and a mirror-reflected copy, not a simultaneous measurement of every left and right P-EN. Coding bandwidth spans typical behavioral velocities at the population level; the response letter says a proposed individual-neuron/individual-fly bandwidth correlation was not significant (p=0.094). Loose-patch spike detection is relatively robust around the selected threshold, but waveforms deteriorate over time and late data can be excluded.

**Figure 5 supplement 1 and Figure 6 supplement 1:** sampling rectangles and selected epochs control occupancy bias; they also limit generalization beyond well-sampled conditions. The subthreshold-versus-spiking comparison gives p=0.454 versus p=0.009 in the reported two-way analyses. This supports sharpening at output, not a molecular multiplication mechanism. Heading fits use the sum of two von Mises terms because a trough as well as a peak can appear, especially in voltage.

**Figure 8 supplements 1–2:** spatial and temporal channel controls argue against major fluorescence bleed-through; VT008135 repeats the bridge-offset result. Neither control makes dendritic calcium identical to spikes. P-EN bridge activity on the nonpreferred side remains unexplained in the authors' response.

**Figure 9 supplements 1–2:** cross sections display considerable variability around averaged bumps; reversed-color data retain positive mean offsets but weaker statistical evidence for velocity-dependent growth. Quoting only the 20.7° number hides this uncertainty.

**Figure 10 supplements 1–2:** near-linear integration occupies a restricted excitation/inhibition regime. The connection matrix depicts local excitation as **reduced net inhibition**. A tonic current raises the operating point; it does not literally change a negative connection's derivative into a positive one. OU statistics are a simplified movement distribution, not an entire behavioral controller.

**Figure 11 supplement 1:** only turns exceeding 15°/s whose PVA strength stays above 0.025 are included. The weakened circuit's least decodable periods are therefore absent from tracking fits. Experimental slopes are not simply driven to zero; R² falls and large erroneous phase changes appear. The 55%-efficacy model instead tends to underintegrate, highlighting a real model–experiment difference.

**Supplementary files 1–2:** both DOCX tables are downloaded and fully read. File 1 has 12 electrophysiology recordings; apparent input resistances span 0.8–3.6 GΩ, with compensating negative holding currents and substantial resting-rate variation. File 2 tabulates imaging and pre/hot/post blockade behavior for 58 numbered flies. Its “Walking [%]” column contains fractions such as 0.65; interpret these as a reporting-unit mismatch, not 0.65% walking. Post-heating behavior can be strongly reduced, particularly in VT008135 examples. The Methods exclude recovery imaging from the main analysis because behavior and bump amplitude did not recover consistently. A reversible perturbation should not be described as having a successful demonstrated rescue here.

**Published decision letter and response, including both response images:** added presynaptic-marker experiments and more explicit model assumptions address review concerns. Response image 1 demonstrates that plausible indicator kernels produce very different apparent offsets; a selected fitted kernel can match data without uniquely recovering underlying neural dynamics. Response image 2 shows example negative visual gain: E-PG usually follows the fly's motion, sometimes the stripe; P-EN tuning is broadly similar across conditions. The authors removed the negative-gain claim from the final main scientific account pending further investigation. Do not turn the review's initial “no visual responses” concern into an established property of P-ENs.

The response's model description also contains older language equating population counts that differs from the final 54 E-PG/18 P-EN model. The final Methods and supplied code take precedence when specifying the implemented network.

**Movies:** all captions read; 24 evenly spaced frames inspected across each entire asset. Movie 1 illustrates the hypothesized shifted-loop sequence; Movie 2 displays E-PG, P-EN and overlaid activity with the walking animal. These are animation/example evidence, not independent replication. Sampling is not a frame-by-frame motion analysis.

## Targeted source-code check

[Archived model repository](https://github.com/elifesciences-publications/ang_veloc_integr), inspected at `22f32f5d43b1799ee97d789dea87b4fbc049bafa`. Read README, the dynamical function/connectivity construction, selected velocity calibration and trajectory sections of `veloc_integr.py`, and all `Ornstein_Uhlenbeck.py`. No simulation was executed or reproduction claimed.

The source implements threshold-linear input followed by leak, with 54 E-PGs and nine P-ENs per side. It decodes phase via first sine/cosine projections, equivalent to `arg(sum(r*exp(i*phi)))`. Several implementation details require preservation before any later reproduction:

- P-EN time constant is `0.080/1.2` seconds, about 66.7 ms, rather than the Methods' 65 ms. E-PG also receives a small negative offset, −0.0001.
- Local E-PG→P-EN weights use `alpha/n_wedgetot`, then all entries subtract `beta/n_wedgetot`; the printed local term is `alpha/3` with a separate `beta/N` global term. The source is not numerically identical to a literal transcription of that equation. With its defaults all effective E-PG→P-EN matrix entries remain negative, with local entries less negative.
- P-EN→E-PG kernels carry additional population normalization and discretized centers. The dominant and secondary kernel centers differ by 0.85 of a 40° model tile, or 34°, close to but not exactly the written 35°.
- Velocity drive is calibrated with `vel_in_coef=99.64`, and supplied physical angular velocities are divided by this factor. Matching degrees per second is not predicted from anatomy without calibration.
- The OU routine starts at zero, despite a comment claiming stationary initialization. It uses Euler–Maruyama; its returned `linspace` endpoint spacing is slightly different from the integration `dt`. These are implementation details, not new biological findings.

The equations also contain typesetting issues: the first E-PG derivative has an `eq:model` artifact where the time-constant factor should be; the heading-index formula is a magnitude but following prose refers to its argument. Use the complex moment before taking magnitude for preferred direction.

## Remaining questions and neighboring circuits

1. **Origin and calibration of angular velocity:** what sensory or motor signals reach P-ENs, how do walking/flight/passive transport differ, and how is gain maintained? The lag is not an identified input pathway.
2. **Actual recurrent architecture:** which P-EN subtypes, E-PG recurrent connections, inhibitory cells and other loops maintain versus translate the bump? Green (2017), Franconville (2018), Turner-Evans (2020) and Hulse (2021) are necessary next comparisons.
3. **Compartment and measurement mismatch:** why does turn-contralateral PB calcium rise while spike/nodular output falls? Future model constraints should specify which compartment and signal they predict.
4. **Smooth updating without ideal symmetry:** how does a small, uneven, discrete circuit avoid the model's low-speed pinning and still integrate accurately? Higher-harmonic distortions and individual gains matter even though perfect sinusoids are unnecessary for decoding.
5. **Cue capture and frame consistency:** when landmarks correct or remap the compass, what happens to a stored goal, displacement or route reference? This paper does not solve that coupling.
6. **Behavioral completion:** a turn integrator only updates orientation. A food-return account still needs translation integration, goal storage, retrieval, steering, obstacle handling and context-dependent switching into search or plume tracking.

For later connectomics, the useful test is whether subtype-specific signed effective loops and inhibitory pathways support these transformations under realistic constraints. A connectome can revise the assumed topology and nominate missing relays. Synapse counts alone cannot supply membrane time constants, state-dependent efficacy, sensory calibration or identify a unique navigation algorithm.
