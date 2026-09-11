# Lanz et al.: disinhibition of a recurrent goal-memory circuit

**Version read:** October 7, 2025 bioRxiv v1, DOI [10.1101/2025.10.07.681003](https://doi.org/10.1101/2025.10.07.681003). This remains a **preprint** in the publication records checked on September 10, 2026. The [61-page PDF](main.pdf) contains the main paper, methods, six main figures, ten Extended Data figures and four tables. All scientific text and references were read in the equivalent [PMC manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC12632281/); all sixteen scientific figure images were inspected, and PDF pages 25–28 were additionally rendered to verify the equations. The later public code is not identical to the v1 methods: see the version comparison below.

## What part of navigation does this explain?

A fly encounters odor, chooses an approximately upwind heading, and continues walking along it for several seconds after odor disappears. A plausible computational requirement is to retain the chosen direction while the sensory evidence is temporarily absent, then release that direction when the animal switches behavior.

The proposed mechanism is a recurrent loop between **PFG and hΔK**. PFG receives compass input. With hΔK inhibited, PFG follows that changing input. Removing inhibition recruits recurrent excitation, allowing the population pattern present at that moment to persist. Restoring inhibition releases the memory. FB5V is the candidate selective gate; FB6M provides a different, broader form of inhibition.

This is a candidate mechanism for temporarily holding an angular goal. It does not establish a remembered food location, accumulated displacement, destination distance, retrieval of several locations, or return after an arbitrary detour. It also does not directly demonstrate the entire proposed gating sequence through a behavioral manipulation of FB5V.

## Experimental preparation and what the measurements mean

Calcium experiments use walking, tethered flies on a 9-mm ball. Wind rotates in closed loop with measured heading; odor is presented in open loop. Thus these experiments study responses to imposed odor encounters, not a fly locating an actual source. Wind is 25 cm/s; odor is 0.5% apple cider vinegar. Stimuli are a 15-second step or 1, 4, 7 or 10 half-second pulses at 1 Hz. Imaging uses GCaMP7f plus tdTomato, three optical sections, eight volumes per second, and eight hand-drawn FB regions. Imaging flies are 9–12 days old; electrophysiology flies are 1–3 days old. Imaging saline is warmed to 33°C.

The methods specify 65-second trials with wind from 5 to 60 seconds, whereas the results describe 50-second wind trials. Preserve this discrepancy when reconstructing the paradigm. Animals enter analysis only if they reliably orient upwind on at least half their trials: the conclusions concern selected responsive flies, not the whole tested population.

The cell-specific imaging lines are SS63158 for hΔK and SS52590 for PFG. FB5V imaging uses SS88825, whereas its optogenetic physiology uses the broader R36B06 line. hΔK patch recordings and tetanus-toxin experiments use VT062617-LexA. R65C03 labels numerous tangential cells; calling all of its activation effects specifically “FB6A/D” is an approximation.

A detected bump lasts at least three seconds; nearby episodes are merged. The amplitude threshold is usually the trial minimum plus one standard deviation, but PFG persistence analyses in Figure 1 use 1.5 standard deviations to select large bumps. Position comes from a von Mises fit after approximately two-second smoothing. Comparisons of event lifetimes therefore depend on the detection rules and indicator dynamics. A bump's survival time is different from a fitted decay constant of its amplitude.

## Main figures: evidence and interpretation

**Figure 1 — shared persistent activity.** Both populations develop stronger bumps with odor, and activity often continues after odor offset. There are six flies per cell type. Bump termination accompanies heading deviation and reduced forward velocity. However, the hΔK association with a decrease in probability of upwind heading is only a trend (p = 0.0614), whereas the equivalent PFG comparison is significant. These are separate population recordings, not simultaneous proof that the two bumps are coupled trial by trial. Neural/behavioral persistence comparisons include only episodes with a bump spanning odor offset. Their similarity is suggestive, not an independent demonstration of a memory mechanism.

**Figure 2 — persistent excitation requires network output.** A four-second, +4-pA current injection evokes depolarization without the prolonged poststimulus response seen after synaptic stimulation. Activating R65C03 produces transient inhibition followed by slow excitation. Nicotinic antagonists reduce the persistent component (eight cells, p = 0.0391). Expressing tetanus toxin in hΔK strongly reduces persistence after the same stimulation (15 controls versus eight toxin cells, p = 0.0032). This supports feedback involving hΔK output. It does not isolate the hΔK→PFG→hΔK loop from other recurrent partners, nor prove that every intrinsic, context-dependent conductance is irrelevant.

ExR3 activation also produces slow excitation, reduced by methysergide (eight cells, p = 0.0367). FB6M and FB5V activation produces relatively fast inhibition, converted to excitation by 5-µM picrotoxin (five and six cells respectively). These recordings constrain functional sign and timing beyond anatomy. They remain network responses to population activation, not isolated unitary synaptic currents. The patched cells were deliberately depolarized to about −38 mV; picrotoxin experiments often required hyperpolarization to about −50 mV to avoid depolarization block.

**Figure 3 — slow feedback expands the range of persistent dynamics.** The model has 30 hΔK units, 18 PFG units, local reciprocal excitation and one global inhibitory unit. Narrow, broad and irregular inputs settle into a similar bump profile. Making excitation slow broadens the parameter region yielding intermediate decay times; with fast excitation, the transition from quick decay to sustained activity is sharper. This is the key model result. It is not evidence that synapse counts alone determine a memory lifetime. The persistence-distribution comparison draws excitation/inhibition values from imposed Gaussian distributions and excludes nondecaying simulations. It is conditional on those choices, not a fitted generative account of all biological trials.

**Figure 4 — the two populations do not always behave together.** PFG commonly retains a weak bump during turns and rest; hΔK largely disappears, reappearing during straight runs. PFG position moves in the expected direction during turns, with gain below one. Successive hΔK bumps can appear at new positions after turns. Maximum and cumulative bump movement differ substantially between populations, but those tests pool 281 and 434 bumps; they are not hundreds of independent flies. Heading correlations are positive in both populations, with no significant between-population difference (p = 0.0837). A fixed hΔK bump during a fixed heading cannot by itself separate a stored goal from current heading; the behavioral and physiological context supplies the interpretation.

**Figure 5 — a model latch.** Compass connections preferentially target PFG. Setting recurrent strength to zero allows PFG to follow the compass; turning recurrence on stabilizes the current pattern. Selective inhibition of hΔK produces the same functional switch without changing anatomical weights. Different gate times store different phases, and successive gate episodes overwrite the state. This is a simulation with prescribed inputs and gate timing. It does not show that a behaving fly can be made to store an arbitrary imposed heading by experimentally opening the proposed gate.

**Figure 6 — candidate gating neurons have appropriate signals.** FB5V is tonically active, suppressed by odor and continuing upwind runs, positively correlated with angular speed, and negatively correlated with upwind velocity. FB6M is suppressed mainly by wind, correlates with turning, and has no significant upwind-velocity correlation (p = 0.4382). Both increase around departure from the adopted goal. These are six-fly imaging datasets. FB5V selectively targets hΔK; FB6M targets both circuit populations and therefore cannot be treated as the same gate. Activity correlations support the model but do not establish whether inhibition initiates a turn, follows it, or receives a shared upstream command.

## Extended Data and tables

| Item | What it adds |
|---|---|
| ED1 | Reciprocal anatomical weights are strongly related. Postodor trajectory persistence is longer than baseline; the displayed fits are approximately 5.87 versus 2.75 seconds. Long baseline trajectories can run into subsequent stimulus onset, so baseline is not uniformly stimulus-free. |
| ED2 | Negative current steps also lack prolonged excitation. R65C03 overlaps multiple layer-6 cell types, around 17 cells per side. Larger optogenetic duty cycles tend to increase persistent excitation; pharmacology reduces it. |
| ED3 | FB6M synapses target hΔK axonal compartments, whereas FB5V predominantly targets its dendritic compartments. This is a meaningful distinction lost in a cell-level adjacency matrix. Driver stains are shown. |
| ED4 | Explicit connectivity operations and slow/fast synaptic filters clarify which timescale was changed. |
| ED5 | Real hemibrain connectivity can maintain bumps over much of the angular range, but amplitude and decay time vary strongly with angle. Gaussian weights give much more homogeneous results. The real-connectome result is not a perfect continuous attractor. |
| ED6 | PFG activation produces excitation in some hΔK cells and inhibition in others. Slow excitation through a global tangential unit can also stabilize the model, so PFG is not uniquely identified as the source of slow feedback. Some parameter regimes oscillate; these are excluded from decay analysis. |
| ED7 | A two-variable excitatory/inhibitory reduction retains the slow-feedback effect. This tests generality within models, not a second biological circuit. |
| ED8 | Without a gate, ongoing compass input keeps both model populations active. PFG correlates more with heading than travel direction; the equivalent hΔK comparison is not significant (p = 0.1733). |
| ED9 | Recurrent input is anatomically stronger than compass input. Inhibiting both populations does not preserve a separate PFG tracking state. Anatomical input ratios still are not measured effective physiological gains. |
| ED10 | Odor-pulse responses distinguish FB5V odor suppression from FB6M wind suppression across individual flies. |
| Tables 1–2 | Driver combinations, ages/preparations and receptor blockers delimit what each manipulation can identify. |
| Tables 3–4 | Statistical units vary between flies, cells, trials, bumps and turns. These tables prevent treating every plotted event as an independent animal. |

## Math, using complex exponentials

Let the compass be $H(t)=e^{i\theta(t)}$. In a convenient convention, the directional input to PFG unit $j$ is

$$I_j^P(t)=c_0+c_1\operatorname{Re}\{H(t)e^{-i\phi_j}\}.$$

This is a heading signal, not a displacement vector. Write hΔK activity as $u_K$, PFG activity as $u_P$, and their temporally filtered outputs as $U_K,U_P$. A compact transcription of the paper's model is

$$\tau_K\dot u_K=-\alpha_Ku_K+g_EW_{P\to K}U_P-W_{I\to K}U_I-q(t)\mathbf1,$$
$$\tau_P\dot u_P=-\alpha_Pu_P+g_EW_{K\to P}U_K-W_{I\to P}U_I+I^P(t).$$

The global inhibitory unit receives pooled excitation. Excitatory output functions are clipped between zero and one; inhibitory output is rectified. Synaptic filtering obeys

$$\ddot U_x+(a_x+b_x)\dot U_x+a_xb_xU_x=a_xb_xF_x(u_x).$$

For unequal positive rates, its impulse response is proportional to

$$h_x(t)=\frac{a_xb_x}{b_x-a_x}\left(e^{-a_xt}-e^{-b_xt}\right),\qquad t\geq0.$$

Thus the memory-timescale argument concerns **temporal exponentials in feedback**, distinct from the **spatial complex exponential encoding angle**. In v1 the fast filter uses $(a,b)=(10,10.1)$ and the slow filter $(0.8,1)$; membrane parameters are $\tau=1,\alpha=10$, giving an uncoupled activity relaxation time of 0.1 seconds.

When $q$ is large, hΔK is suppressed and the recurrent loop is ineffective. When $q$ is removed, recurrence can dominate the compass input, preserving a pattern with phase approximately equal to the heading at gate opening. A useful explanatory readout is

$$Z_K=\sum_j U_{K,j}e^{i\phi_j},\qquad g=\arg Z_K.$$

That phasor is our shorthand, not their von Mises estimator. Its magnitude can change while its phase stays nearly constant; losing amplitude below detection is different from the phase rotating. A narrow bump also contains higher Fourier harmonics. The model does not require every cell's tuning curve to be a perfect sinusoid to preserve an angular state.

For intuition, a linearized feedback mode with gain $\lambda$ and slow timescale $\tau_s$ can have $\tau_{\mathrm{eff}}\approx\tau_s/(1-\lambda)$ below instability. This is an explanatory approximation, not their full two-population derivation. Slower constituent dynamics allow useful persistence without placing the gain quite so close to the stability boundary; saturation and inhibition matter beyond the linear regime.

## Public code: useful, but a later revision

The [authors' repository](https://github.com/nagellab/Lanzetal2025) and [data release](https://zenodo.org/records/19687299) now exist despite v1 saying they will appear upon publication. Downloaded code is pinned in metadata to commit `b52ee5742e96a579356bc475d01a08d640759789`. I read both READMEs, network construction, core integration routines, parameter setup, gating routines and selected plotting/sampling helpers. I did not execute the simulations or read every analysis script.

Several substantive differences mean this archive must not be called an exact reproduction of the October manuscript:

- Gaussian widths are 0.25 in both directions rather than v1's 0.4 and 0.3. Real connectivity begins with 31 hΔK identities and explicitly removes the last to obtain 30. This explains why the anatomical schematic labels 31 while simulations use 30.
- Default filter parameters are $b=25$, $a_{fast}=4.63$, $a_{slow}=0.64$, rather than v1 values above.
- The numerical solver clips the integrated activity after each Euler update. That differs from keeping an unconstrained voltage variable and applying the nonlinearity only at its output.
- The displayed gate configuration uses recurrent scale 7 and compass scale 2, whereas v1 describes a 6:1 ratio. Matrix normalization and population sizes further prevent reading these scalar settings as a literal synaptic ratio.
- The model README mentions added sensitivity analyses and revised Extended Data numbering. The data README includes PFG wind/odor-shift experiments absent from the v1 account read here.

The model-data archive and data README are saved. The 5.33-GB imaging and 28.65-GB electrophysiology archives were inventoried, not downloaded or reanalyzed. A revised manuscript must be matched to this later code before interpreting the differences as errors in a final paper.

## Remaining questions for the complete behavior

1. **Does the gate cause storage and release?** Record both populations while selectively perturbing FB5V and independently changing compass input. The present physiological sign measurements plus activity correlations do not complete that causal chain.
2. **Where does persistent gate suppression originate?** FB5V suppression itself outlasts odor. Some memory may therefore be upstream rather than entirely generated by the hΔK–PFG loop.
3. **What is stored when motion and goal disagree?** Straight runs conflate desired heading, actual heading and travel direction. Turns erase or alter this candidate state; explaining return after a detour requires knowing what survives elsewhere.
4. **How is this memory read out alongside FC2 and other local populations?** Connectivity makes a path plausible, but the complete arbitration between multiple angular goals remains unresolved.
5. **How does an angle become a remembered place?** Returning to food after translation requires either updating a target displacement or another demonstrated navigational policy. This circuit contains no established distance integral or food-coordinate register.
6. **How do real weights, receptors and compartments cooperate?** Slow peptides/modulators, axonal versus dendritic inhibition, and state-dependent efficacy can change function without changing the connectome. Later structural analysis should retain these distinctions.

The paper supplies a plausible short-term memory component of odor-guided running. It is especially useful because it links recurrent anatomy to dynamics and then exposes why an additional gate is required. It leaves the multi-stage food-location behavior open.
