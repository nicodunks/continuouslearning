# Siliciano et al. (2026): A vector-based strategy for olfactory navigation in Drosophila

[Published paper](https://doi.org/10.1038/s41586-026-10827-7), Nature 657, 443–454. Published online 22 July 2026. Andrew F. Siliciano, Sun Minni, Chad Morton, Charles K. Dowell, Noelle B. Eghbali, Silas E. Busch, Juliana Y. Rhee, L. F. Abbott and Vanessa Ruta.

## What behavior does this explain?

A hungry walking fly encounters an odor plume, leaves it, explores in clean air, and returns toward its boundary using information from previous encounters. Repeating this sequence produces progress along the plume. This is a substantial bridge from a persistent angular goal to an actual foraging behavior. It is not yet a demonstration of learning a food location, finding that location from arbitrary starting points, or commuting between remembered places.

The remembered quantity is a **direction that previously led into odor**, referenced to an externally anchored compass. It is not the coordinates of the previous entry, distance from the boundary, or a displacement vector integrated along the path. The behavioral model expresses that memory as a *goal velocity*: magnitude carries speed/bias strength, not distance. This distinction also generated substantial discussion during peer review.

## Experimental world and what the fly can sense

A tethered female fly walks on a 6–6.5 mm air-supported ball. FicTrac measures movement at 60–61 Hz. A rotating nozzle supplies wind from a constant virtual world direction; odor concentration depends on the fly's virtual position. Experiments are in darkness. Wind supplies an external directional reference, while proprioception and movement history remain available. No visual landmarks are required here.

The standard corridor is 50 mm wide and 1,000 mm long. Imaging uses a 10 mm corridor. Apple cider vinegar (ACV) is delivered at boundaries with an approximately 500 ms onset/offset delay, producing a speed-dependent boundary smear of roughly several millimetres. Airspeed is 15–25 cm/s. This is not a physical plume whose left/right gradients are sampled independently by the antennae.

Flies are 1–5-day-old females, starved 16–24 h according to Methods. Food history matters: Wurzburg food gave more reliable tracking than standard cornmeal food. Fewer than 10% were excluded for failure to walk/acclimate, absence of an ACV response, or tracking failure. Thus generalization to satiated flies, males, free flight, and unrestricted natural environments requires separate evidence.

## Evidence, figure by figure

### Figure 1: edge tracking is a structured repeated behavior

Forty flies predominantly follow one boundary. Odor bouts are brief (mean 4.9 s over 755 bouts); mean penetration is 10.4 mm, and fewer than 4% of 793 bouts traverse the corridor. Inside odor, flies turn to exit rapidly and make much of their upwind progress. Outside, longer exploratory excursions terminate in more directed returns. Inbound paths are shorter and more perpendicular to the boundary than outbound paths. The aligned trajectory average illustrates this asymmetry, but individual trajectories remain variable.

ED1 measures stimulus delay and documents naïve tracking. ED2 shows tracking with increasing, decreasing, and constant longitudinal concentrations. This argues against a requirement for the longitudinal gradient in this assay, not against all uses of odor concentration. ED3 replaces a sharp boundary with a Gaussian lateral profile: occupancy concentrates near the steepest slope, with longer inside bouts than in a sharp corridor.

ED4 synchronously activates Orco sensory neurons with CsChrimson. A fictive odor corridor plus wind produces edge tracking; without wind flies remain locally attracted but make little longitudinal progress. This shows that bilateral odor comparison is unnecessary for this behavior under these conditions. Optogenetic and real-odor trajectories differ quantitatively: several excursions are shorter, and inside walking is slower with optogenetic stimulation. The stimulus timing and recruited receptor populations differ.

### Figure 2: a remembered bearing rather than a remembered endpoint

Flies track corridors rotated 45° or 90° relative to wind, including downwind returns to a horizontal corridor. Entry directions depend strongly on geometry. Exits retain a strong upwind bias, explaining preference for the upwind boundary.

After 10 min of tracking, the plume disappears during an outside excursion. Flies continue in the general direction previously used for return, even beyond the last boundary. A jumping corridor displaced 20 mm away at each exit can also be tracked. These manipulations support directional guidance without an obligatory remembered endpoint. They do not establish that flies lack positional memory in other tasks.

ED5 compares random walks built from empirical run-length and turn-angle distributions, with or without an upwind bias. Such models can return by chance, but inefficiently and without the same outbound/inbound asymmetry. The biased null especially fails at tilted plumes. These results reject the tested null policies; they do not exhaust every possible reactive or history-dependent alternative.

ED6 quantifies geometry dependence and individual variability. ED7 shows improvement across early returns most clearly for tilted/jumping plumes; the vertical-plume change is not significant. Survival/selection and varying available bout counts matter when interpreting successive-return summaries.

### Figure 3: compass activity is needed

EPG phase follows heading during tracking (16 trials from 9 flies). EPG bump shape/amplitude are comparable inside and outside odor. Silencing EPG throughout jumping-plume trials impairs efficient returns (12 experimental, 6 control flies). The controls do not show the same light effect.

This establishes a requirement for the heading circuit during the task. Whole-trial inhibition does not isolate memory formation from maintenance, retrieval, reference-frame alignment, or steering execution.

### Figure 4: a behavioral model predicts learning and adaptation

A switching state-space model has leaving and returning states, separate entry and exit memories, and noisy velocity dynamics. The states are **not** identical to being inside/outside odor: state changes are delayed and odor dependent.

The model captures many trajectory statistics across corridor orientations. A mirror-segment assay then tests adaptation: after tracking a +45° corridor, flies tend to persist in a direction inappropriate for a −45° corridor. Odor delivery contingent on headings appropriate for the new corridor improves subsequent tracking. Reinforcing headings appropriate for the old corridor does not. Additional training beyond the first session produces little further improvement.

Important detail: entering the test corridor itself provides another correctly directed odor encounter. “One training session” does not mean exactly one reinforcement event across the entire protocol. The fixed-rate average model changes its entry memory more slowly than behavior-inferred memories in the real flies.

ED8 gives the latent-state graph, inference checks on simulated ground truth, parameter heterogeneity, and training-set selection. ED9 compares geometry-specific histograms; Table S2 reports correlations between *histogram bin heights*, not trial-by-trial prediction accuracy. Correlations range from 0.332 to 0.989; the fit is weaker for some outside speed distributions.

ED10 ablates model memories. Removing entry memory harms tracking across geometries. A fixed exit bias works substantially better than a purely upwind or newly resampled exit bias in some geometries. Continual exit-memory learning is less essential than entry-memory learning. Therefore a biological implementation with one learned return memory plus a persistent, context-dependent exit bias remains plausible.

ED11 supplies operant controls. ED12 replays the same odor timing independently of the animal's movement: the previously acquired directional bias is progressively overwritten toward the baseline upwind tendency. This supports sensitivity to the conjunction of direction and odor encounter. It does not reveal the cellular plasticity rule.

### Figure 5: extending to a dynamic plume

The authors replay a measured surface plume through the virtual environment. Their expanded stimulus stretches space and time fivefold; it is binarized, and experimental odor encounters are extended to at least 1 s because of delivery dynamics. Ten of twelve flies reach within 50 mm of the virtual source.

Near the coherent plume ribbon, entry directions and model-inferred memories become more predictive. Farther downwind, transient filaments can contact an almost stationary animal, making encounters less informative about which direction led into the plume. Memory improves simulated performance particularly where the boundary is coherent. Main comparisons retain 1,850 of 2,000 scaled-plume simulations under effective-entry criteria; the original-scale analysis retains 1,593 of 2,000. ED13 shows the original-scale benefit is smaller.

This is evidence that the strategy can operate in a more complex virtual chemical landscape. Scaling preserves a fluctuation velocity but not all fluid statistics or the relationship between plume geometry and the animal's body/movement. It is not an outdoor free-navigation validation. Nor does this experiment identify the neural switch between alternative strategies.

### Figure 6: FC2 expresses the return goal

Simultaneous EPG and FC2 imaging (6 flies) is a particularly useful link to Pires and Westeinde. Before encountering odor, FC2 and EPG broadly align during upwind walking. Inside the plume and around exits, FC2 follows heading. During an outside return, FC2 points toward the boundary several seconds before the fly turns that way. FC2 inhibition impairs jumping-plume returns (14 experimental, 9 controls; Table S1).

This supports FC2 as a goal signal that contributes to directing the return. It does not identify FC2 as the physical storage site. A persistent memory elsewhere, intermittently read into FC2, is compatible with these data.

The Figure 6a cartoon includes entry and exit memories converging on a goal signal. The Discussion explicitly says that **FC2 did not provide evidence for an exit-angle memory**. Do not treat the cartoon as an observation of both memories.

ED14 shows diverse inputs to FC2A/B/C in hemibrain v1.2.1: hDelta, vDelta, other FC, PFN and tangential populations. Input identities differ across FC2 subtypes. Mean synapse counts are anatomical evidence, not measured functional weights. The FC2 return bump is broader/less coherent than the exit bump: PVA changes significantly (p=0.0077), while mean fluorescence does not. A goal can therefore become behaviorally relevant without becoming a larger, cleaner sinusoid.

## The mathematics in complex notation

Choose orthogonal world axes with the real axis upwind and imaginary axis crosswind. A travel direction is the unit phasor

\[
\hat v_k=e^{i\theta_k}.
\]

The actual paper uses two-dimensional real vectors; the following is an equivalent complex rewriting, not an additional neural model. Each encounter updates the appropriate memory:

\[
M^{\rm entry}_{k+1}=a_e M^{\rm entry}_k+b_e e^{i\theta^{\rm entry}_k}+\epsilon_{e,k},
\qquad
M^{\rm exit}_{k+1}=a_x M^{\rm exit}_k+b_x e^{i\theta^{\rm exit}_k}+\epsilon_{x,k}.
\]

In simulations the memory-noise terms are set to zero. Between boundary crossings memories remain unchanged. There is no continuous passive decay in this model. For repeated entries,

\[
M^e_n=a_e^nM^e_0+b_e\sum_{k=0}^{n-1}a_e^{n-1-k}e^{i\theta_k}.
\]

This is an exponentially weighted history **over encounters**, not over elapsed time. Nearby angles reinforce; inconsistent angles partially cancel. The remembered bearing is \(\arg M\), and magnitude reflects coherence and the target speed/bias. Uniformly distributed entry directions tend to cancel the directional component, though a finite history retains noise.

The fitted average parameters are \(a_e=0.727\), \(b_e=0.437\,\mathrm{mm/s}\), \(a_x=0.956\), \(b_x=0.482\,\mathrm{mm/s}\). Repeated identical angles would approach \(b/(1-a)\), about 1.60 mm/s for entry and 10.95 mm/s for exit. These are mathematical limits of the fitted rule, not measured neural firing rates. The memory amplitudes need not equal observed instantaneous walking speeds because noisy velocity dynamics and state transitions intervene.

At 0.2-s steps, complex velocity evolves as

\[
V_t=c_sV_{t-1}+(1-c_s)M_s+\xi_{s,t},
\]

where \(M_s=M^x\) in the leaving state and \(M_s=M^e\) in the returning state. Average values are \(c_r=0.733,\sigma_r=3.23\,\mathrm{mm/s}\) and \(c_l=0.6,\sigma_l=3.255\,\mathrm{mm/s}\). For a fixed state and memory, expected velocity relaxes toward that memory. The effective velocity relaxation time is \(-\Delta t/\log c_s\), approximately 0.64 s returning and 0.39 s leaving. This is **not** the goal-memory lifetime.

Odor-conditioned state dwell times follow negative-binomial distributions. The average leaving-after-exit parameters are \(r=1,p=0.81\), and returning-after-entry parameters are \(r=2,p=0.505\), using the paper's \(NB(r,1-p)\) convention. The state only switches if the relevant odor condition still holds. Behavioral delay includes stimulus delivery and may not correspond directly to a neuronal decision latency.

Entry memory begins at zero; the initial exit memory includes 6.299 mm/s upwind plus a uniformly sampled crosswind component between ±3.39 mm/s. Simulated exit updates are ignored when the exit direction is more than 60° from upwind. These are consequential built-in constraints. The model does not learn the entire policy from an unconstrained initial state.

### Connecting to phasor circuit computations

A candidate spatial population encoding of the goal would be

\[
g(\phi)=g_0+\operatorname{Re}\{M e^{-i\phi}\}.
\]

The encounter update could then be implemented as a change in the first spatial harmonic of a synaptic pattern. With heading \(H=e^{i\psi}\), the egocentric angular relationship is represented by \(M\overline H\). Its imaginary component supplies a signed error for an idealized steering controller. Pires/Westeinde provide more anatomically specific nonlinear population mechanisms for a related comparison.

**This paper does not demonstrate the synaptic implementation of the encounter update.** Nor does it show that PFL3 reads the behavioral model's target speed literally. The behavioral velocity process abstracts away turning dynamics, individual neurons, and the motor plant. The connection is a constrained hypothesis that must be reconciled with the other papers.

Perfect sinusoids are unnecessary for estimating a first-harmonic direction: \(Z=\sum_j r_j e^{i\phi_j}\) remains defined for a broad/asymmetric bump. However, higher harmonics, baseline changes, sampling geometry, and broad weak bumps affect readout reliability. ED14's broader FC2 return bumps make this a practical issue rather than a purely mathematical concern.

## Inference and measurement details that affect interpretation

- Models exclude speed below 1 mm/s. Boundary events require several consecutive samples on each side and use a normalized velocity averaged over about 1 s. Instantaneous body heading and this averaged travel direction are not identical variables.
- Variational EM jointly estimates hidden states and memory trajectories; the posterior is factorized across state, entry-memory and exit-memory sequences. The mean of the inferred posterior is a model-conditioned estimate, not a direct memory recording.
- Average parameters are fitted using 28 trajectories with at least 30 returns. This enriches for animals that already perform many returns; fitting does not by itself explain failure to initiate tracking. Additional state/velocity summaries use 46 trajectories with at least 20 returns.
- Inference allows memory noise; simulations set it to zero. The first outside bout is removed in the prominent efficiency comparison because the initial return memory is zero. These choices should be preserved in any later reproduction.
- Imaging acquires 3–10 volumes/s, then interpolates onto 100-ms bins. Sixteen wedges approximate each EPG/FC2 angular pattern. Fluorescence baseline is the lowest 10% of signals.
- World-coordinate calibration uses a rolling 2-s EPG-phase-minus-heading offset, applied equally to FC2 and EPG. This stabilizes alignment but means calibrated EPG/world correspondence is not an entirely independent validation. The relative FC2–EPG phase remains particularly informative.
- Laser heating promotes straighter paths; the imaging experiment introduces 3-mm jumps after initial experience to elicit longer returns. It is not identical to the 20-mm whole-behavior jumping assay. Methods says every third subsequent entry; Figure 6 describes shifts during returns. Precise trigger timing should be checked against code before reproduction.
- Whole-trial FC2/EPG silencing leaves encoding-versus-retrieval unresolved. The model contains no explicit neuronal or synaptic perturbation mechanism.

## Supplement and peer-review checks

Table S1 provides exact sample sizes/tests. FC2 returns: p=0.009; upwind distance: p=0.005, with controls nonsignificant. EPG returns: p=0.0049; upwind distance: p=0.0087. These are within-condition contrasts, not proof that all cross-group interaction tests were performed.

There are reporting inconsistencies to preserve rather than silently resolve: the EPG row in Table S1 says 660 nm while Methods specifies 530 nm; the ED1 caption says starvation >24 h while Methods says 16–24 h; the generic statistics paragraph says no randomization while specific Methods/reporting passages describe pseudorandomized or randomized condition order. Some sample counts/tests in extended-data captions differ from the table. Use per-analysis source data/code before attempting exact replication.

The 29-page peer-review exchange clarifies why the final paper adds FC2 inhibition, Gaussian boundaries and more naturalistic tracking. It also explicitly discusses (i) one return memory plus exit bias, (ii) the difference between velocity vectors and positional vectors, (iii) the lack of a reliable memory-decay estimate, and (iv) limitations of scaled plumes. Statements labeled “data not shown” about odor inhibition of hDelta inputs, satiety, or externally imposed wind shifts are hypotheses/context, not an independently inspectable result here.

Movies illustrate the rotating nozzle, continuous edge tracking, jumping boundaries, and dynamic-plume trajectories. They were sampled across their full duration, not exhaustively inspected frame by frame; see reading-log.md.

## Remaining questions and neighboring circuits to follow

1. **Memory substrate:** which neurons/synapses hold the entry-bearing history while FC2 temporarily follows current heading inside odor? Persistent firing, synaptic plasticity and other hidden state remain alternatives.
2. **Write signal:** which odor-onset/offset pathways detect a meaningful encounter and gate direction-dependent updates? How do concentration derivatives, reward value and hunger affect them?
3. **Readout switch:** what changes FC2 from heading aligned to memory aligned? Tangential inputs could gate hDelta/PFN contributions, but this is not causally traced here.
4. **Exit control:** is there a separate exit memory, a slowly changing bias, a wind reflex with overshoot, or a combination? The two-memory behavioral model does not settle this.
5. **Travel versus heading:** which direction is written during sideways/backward movement? Lyu supplies one candidate travel signal, but this study does not identify the writer's input cell type.
6. **Confidence and forgetting:** do inconsistent encounters weaken memory amplitude, change learning rate, or recruit a different search policy? No decay constant or adaptive learning circuit is measured.
7. **Changing reference frames:** how are memory and compass kept aligned when the wind changes independently of the fly? A constant virtual wind avoids much of that problem.
8. **Complete foraging:** how does a plume boundary lead to source recognition, feeding, satiety, disengagement, remembered-place revisits and travel between places? These require additional behaviors and circuits; plume tracking alone does not answer them.

For later connectomics, prioritize the subtype-specific hDelta/vDelta/PFN/tangential inputs to FC2 and possible odor-dependent gates. Keep the analyzed hemibrain anatomy separate from the downloaded male CNS dataset, with explicit cell-type correspondence. Simulations should compare plausible mechanisms for the unresolved transitions, not assume that the behavioral model already names the neurons implementing each state.

## Cross-paper links

- [Lyu: body-to-world travel-vector computation](../2022-lyu-allocentric-travel-vector/notes.md).
- [Pires: allocentric goal to egocentric steering](../2024-converting-an-allocentric-goal-into-an-egocentric-steering-signal/notes.md).
- [Westeinde: steering command and error-dependent gain](../2024-transforming-a-head-direction-signal-into-a-goal-oriented-steering-command/notes.md).
- Next required upstream readings: Kathman et al. on working memory/evidence integration, Matheson et al. on odor/wind convergence, Dan et al. on angular learning, and Okubo/Currier/Basnak on wind and compass alignment. These links are a reading agenda, not claims that the missing mechanisms are already established.
