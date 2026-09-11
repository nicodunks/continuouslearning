# Fly navigation: building complete behavioral explanations

This is a growing synthesis, not a completed model of fly navigation. It currently incorporates full readings of Lyu et al. (2022), Mussells Pires et al. (2024) Westeinde et al. (2024), and Siliciano et al. (2026). Other papers in the library remain reading targets unless their logs say otherwise. The [research approach](../RESEARCH_APPROACH.md) defines the sequence: literature and synthesis first, then targeted connectome analysis and simulations.

## The motivating behavior

A fly encounters something useful, leaves, and later navigates toward it from its current situation. A mechanistic account must specify what experience changes, what persists, how current sensory/self-motion information is represented, how the remembered objective determines an action, and what ends or changes that action.

Several representations could support superficially similar behavior. An odor-value association, a remembered compass bearing, a home vector, recognition of a familiar view and a remembered location are different computational objects. Evidence for one does not establish all the others. The reading program must follow actual behavioral demonstrations rather than assume a metric map in advance.

## Coordinate operations established so far

| Link | Evidence read so far | Boundary |
|---|---|---|
| Body-relative movement and heading → world-relative travel direction | [Lyu](../papers/2022-lyu-allocentric-travel-vector/notes.md): PFNd/PFNv and hDeltaB computation, anatomy and physiology | Instantaneous travel estimate; does not identify a position integrator or stored destination |
| Heading and selected bearing → corrective steering | [Mussells Pires](../papers/2024-converting-an-allocentric-goal-into-an-egocentric-steering-signal/notes.md): FC2/PFL3 physiology, perturbations and model | Explains angular comparison; not target selection, positional memory or complete motor execution |
| Wind experience → subsequent orientation without wind | Pires wind-induced angular-memory task; EPG/PFL3 perturbations | Directional memory, not navigation to a food location; encoding, storage and retrieval not separately localized |

Lyu and Pires supply complementary coordinate operations. A demonstrated hDeltaB → memory → FC2 loop has **not** been established by reading these papers. Do not draw that edge as known.

## A behavior that is partially connected: remember a wind bearing

1. Wind provides a directional experience while the fly orients upwind.
2. After wind offset and rotation of the visual reference, the fly tends to recover the experienced direction relative to that reference.
3. Compass-pathway integrity supports this behavior; partial PFL3 output disruption impairs it.
4. In separate menotaxis experiments, FC2 can specify a desired bearing, and heading/goal convergence in PFL3 provides a mechanism for steering toward such a bearing.

The gap between steps 2 and 4 matters: the full wind-input, storage and retrieval pathway into FC2 has not been identified by this paper. FC2's expressed goal is not automatically the memory substrate. Other inputs and parallel policies remain possible.

## What changes for a remembered place?

For an explicit Euclidean location model, use complex position p(t) = x(t) + i y(t) and remembered destination p*. Then

\[
d(t)=p^*-p(t),\qquad q(t)=\frac{d(t)}{|d(t)|},\qquad
F(t)=K\operatorname{Im}\{q(t)e^{-iH(t)}\}.
\]

This illustrates the missing computation: even if p* remains fixed, q changes as the animal translates. A velocity estimate could contribute through \(\dot p=v_w\), but drift, calibration, reference-frame alignment, memory writing and correction must then be explained. The formula is an engineering decomposition, **not a claim that flies use an explicit Cartesian map**. At d = 0 the direction is undefined, and a separate arrival/stop policy is needed.

A home vector updated by self-motion, familiar-view matching, an odor/wind policy or route following could avoid representing p and p* separately. The literature must distinguish which behavior and mechanism is actually supported. Returning after angular perturbation alone cannot settle this.

## Questions to carry through every paper

- What behavioral episode is explained, and what ends it?
- What is remembered: identity, value, direction, displacement, view, place or route?
- Which variable is measured directly, inferred from behavior, assumed by a model or merely suggested by anatomy?
- In what reference frame and over what timescale does each signal operate?
- How is an objective acquired, retained, selected, updated with movement and expressed as action?
- Which links to neighboring circuits have functional evidence? Which are anatomical? Which remain untested?
- Which competing behavioral strategy would also explain the reported task?

## Reading frontier

The existing library covers compass dynamics, movement transformations, steering, learning and recent olfactory work. With Westeinde and Siliciano now read, connect goal learning and odor/wind persistence to the upstream side, while returning to canonical compass papers to audit reference frames and memory claims. Follow necessary references beyond the initial 21 entries, especially papers experimentally connecting sensory history, persistent objectives and behavior.

Only after that synthesis should novel-cell hypotheses be prioritized. Their eventual records should state the candidate signal and behavioral role, anatomical and physiological support, alternatives, and what a simulation can discriminate. Successful simulation establishes a possible mechanism under stated assumptions; it does not alone discover the neuron's biological function.

## Steering also needs control of response strength

[Westeinde](../papers/2024-transforming-a-head-direction-signal-into-a-goal-oriented-steering-command/notes.md) adds PFL2 and a proposed DNa03 gain pathway. PFL2 activation increases rotational speed and reduces forward velocity; its natural activity is strongest near the anti-goal. In the model, bilateral excitation changes the slope of a downstream nonlinearity, amplifying the directional bias supplied by PFL3. That downstream gain mechanism is anatomy/model-supported, while PFL2 activation and activity tuning are experimental findings. Simulated PFL2 removal is not an animal necessity experiment.

The combined account now includes selected bearing, heading comparison and error-dependent response strength. It still lacks identified memory writing/retrieval, translation-dependent target updating, arrival detection and a full mapping to locomotion. S (total input gain) and A (goal amplitude) are separate proposed controls; neither should be relabeled “memory strength” without evidence.

## A fuller episode: remember a direction that leads back into odor

[Siliciano et al.](../papers/2026-a-vector-based-strategy-for-olfactory-navigation-in-drosophila/notes.md) connects sensory history to repeated plume returns. The fly encounters odor, exits with an upwind-biased policy, explores outside, then steers in a direction associated with earlier entries. Successful encounters update that bearing. FC2 begins pointing toward the plume before the return turn, and FC2/EPG silencing impairs returns. Repetition advances the animal along the boundary, including a dynamic virtual plume.

This is a complete repeated behavioral motif, with important internal links still unresolved. Its model remembers goal velocity/direction rather than a fixed place: M is updated by a weighted sum of entry-direction phasors. Memory is held between encounters; the model does not derive a biological decay constant. It assumes an initial upwind exit bias, and evidence for a separate biological exit memory is weaker than evidence for the return goal.

The connection from expressed FC2 goal to heading comparison is supported by Pires/Westeinde. The connection from odor encounter to a stored synaptic pattern is still a proposal. In particular, FC2 follows heading again inside odor; another state must retain the return memory if it is temporarily absent from FC2's expressed phase. Odor-gated hDelta/tangential/PFN inputs are therefore a concrete reading and later anatomical frontier.

Arrival at a virtual source threshold does not explain recognition of food, feeding, satiety or a later revisit. A remembered return bearing is also insufficient for arbitrary navigation back to a fixed location after translation. Those are distinct branches of the literature, not details to fill by relabeling this memory.

## Maintaining an intention during gaps

[Kathman et al.](../papers/2026-neural-dynamics-for-working-memory-and-evidence-integration-during-olfactory-navigati/notes.md) links odor history to persistent FB activity and persistent upwind walking. The predominantly hΔK-labeled population shows a relatively stable bump while heading changes; silencing curtails persistence more clearly than initial orientation. This adds a mechanism-level question between choosing a heading and repeatedly correcting toward it: how is an intention kept active when sensory evidence briefly disappears?

Do not identify this short-lived goal state with Siliciano's learned entry-bearing memory. The former supports continued pursuit through odor gaps; the latter can direct a return toward a boundary following exploration. Their relation through hΔK/PFG, FC2 and steering readouts needs explicit evidence. Nor does an exponential distribution of bump lifetimes establish exponential amplitude decay or displacement integration.

The model supplies upwind direction and stochastic state transitions, then finds that an intermediate persistence benefits source occupancy. Its objective penalizes overshooting and lacks food recognition, highlighting why approach, arrival, feeding and revisiting need separate literature. The referenced Lanz follow-up addresses the recurrent persistence/gating mechanism; spatial-learning and idiothetic-search work address different missing behavioral capacities.

## Odor context to a wind-relative bearing: a corrected bridge

[Matheson et al. (2022), read with the 2024 addendum](../papers/2022-matheson-wind-guided-olfactory-navigation/notes.md), places odor-sensitive MB/LH pathways upstream of FB contextual inputs. Direct FB5AB/wind-PFN convergence is an anatomical result about hΔC. The physiology and behavioral perturbations used VT062617, which may predominantly label hΔK; hΔK does not receive those same direct inputs. The two findings require an intermediate-pathway explanation, not a global neuron-name substitution.

Its model establishes how a supplied directional representation could steer an agent. It does not derive the complete wind representation or identify all relays. The alternative model constructed from front-preferring PFNs has a restricted capture range. The main model's exact sinusoidal inputs do not explain the biological generation of tuning curves.

This paper distinguishes initial upwind turning from sustained orientation during odor; Kathman adds persistence after odor loss. Neither is equivalent to remembering a food location. MB activity can influence wind-relative action, but learned odor value, a selected bearing and a spatial destination remain different variables requiring separate evidence.

The PFL2 component also needs a historical correction: Matheson's model increases forward speed with PFL2 output, whereas Westeinde's later experiments implicate PFL2 in large-error steering and show increased turning with reduced forward speed under activation. A complete controller must follow the newer evidence and reconcile task differences, rather than concatenate those equations.

## Airflow sensing is distinct from the selected policy

[Currier et al. (2020)](../papers/2020-currier-airflow-orientation/notes.md) identifies front-oblique body-relative airflow responses in PFNa and PFNm/PFNp, with LNa as a plausible nodular input. Its behavior is downwind stabilization in tethered flight without food odor. The later upwind-walking papers therefore need context and locomotor-state transformations, not merely an unbroken chain of identically interpreted arrows. Shared tuning across columns in open loop does not exclude heading conjunction in closed loop.

The published review history corrected a proposed output route after checking synaptic direction and compartment: LNa is mainly an input to PFNs. This is an instructive use of connectomics to reject a mistaken route while leaving the actual behavioral readout unresolved. It reinforces the need to match cell identities and distinguish dominant flow from sparse feedback.

## A location memory makes a different prediction from a bearing memory

[Titova et al. (2023)](../papers/2023-titova-displacement-path-integration/notes.md) separates the physical reward site from a fictive site predicted by path integration that misses passive transport. Rewarded flies preferentially search near the fictive site after displacement. This supports a local internal navigation mechanism beyond simply accumulating at reward, while retaining uncertainty about the exact algorithm and circuit.

The geometry is explicit: if a fly at x retains return vector f−x after transport by d, it arrives at f+d. This is a predictable error of an internal estimate, not successful relocalization to the original physical site after arbitrary displacement. The experiment does not establish a long-term catalog of food locations.

The same paper demonstrates that naïve flies prefer a location previously occupied by rewarded flies, and shows that a chemical-mark model can mimic some earlier annular-search statistics. A complete account must therefore consider chemical cues, internal vectors, remembered bearings, and visual place recognition together. These can cooperate in natural behavior; similar trajectories do not identify the underlying representation. The earlier local-search studies are being read alongside this challenge, rather than accepted or dismissed solely through a later paper's characterization.

## The compass is an angular reference, with a learned-frame problem

[Seelig & Jayaraman (2015)](../papers/2015-neural-dynamics-for-landmark-orientation-and-angular-path-integration/notes.md) establishes localized, landmark-anchored activity that can update in darkness and retain orientation across pauses. It supplies an angular state, not a location or return vector. The original data include drift, variable self-motion gain, weak-activity epochs and delayed visual relocking.

Its population-vector analysis extracts the first angular harmonic of a localized bump. Exact sinusoids are unnecessary for that phase extraction; downstream vector arithmetic imposes additional constraints that must be checked in its own experiments. A decoded phase and a biologically implemented computation are separate claims.

The fly-specific phase offset cancels from heading–goal comparison if both variables share it. Cue ambiguity and relocking create a harder question: when the compass changes its reference, how is an existing goal or displacement memory kept consistent? The later sensory-remapping and goal-learning literature must close that interface. An intact heading representation by itself does not show that a remembered destination remains correctly registered to the world.

## A maintained compass state has an experimentally constrained mechanism

[Kim et al. (2017)](../papers/2017-ring-attractor-dynamics-in-the-drosophila-central-brain/notes.md) shows that directly overwriting EPG activity replaces the old bump and leaves a persistent state with organized drift. Two-site stimulation supports functional competition. The experiments favor local effective excitation and broad inhibition within the tested model space; they do not identify a unique set of direct synapses.

This provides a generative explanation for localized activity, extending the earlier phase-decoding description. The model produces a bounded smooth bump rather than requiring a pure sinusoid as its full-ring activity profile. Retention, accurate self-motion updating, goal storage and steering remain distinct functions.

The tethered-flight preparation preserves persistence while largely uncoupling the bump from motor-derived heading in darkness. Its targeted supplemental stripe assay nevertheless finds increased turning after compass manipulation. These results cannot be summarized as either a complete flight navigation mechanism or a compass with no behavioral effect. The model's input assumptions, fluorescence normalization and inference priors also constrain how strongly its effective connectivity can be inferred.

## Updating the compass requires dynamics as well as shifted wiring

[Turner-Evans et al. (2017)](../papers/2017-angular-velocity-integration-in-a-fly-heading-circuit/notes.md) links heading×angular-velocity tuning in P-ENs to spatially shifted recurrent interactions with E-PGs. Opposite shifted projections provide a mechanism for moving phase; inhibition and operating point support a localized state. Neither perfect sinusoids nor literal cellular multiplication are demonstrated requirements.

The paper constrains a heading updater, not translation integration or destination storage. Neural and synaptic time scales, input gain, real subtype topology and smooth movement through a discrete ring remain material assumptions. The rate model's low-speed sticking was not observed biologically. Its approximately calibrated integration and error diffusion are sufficiency results, not measurements of the whole fly's navigational accuracy.

P-EN blockade weakens and destabilizes E-PG activity, sometimes allowing large erroneous phase movements. It does not simply stop updating. Calcium phase offsets also depend on indicator assignment and compartment. A complete circuit account must preserve these differences rather than identify anatomical overlap, measured calcium phase and causal computation as the same evidence. Later connectomic and subtype-specific papers are needed to resolve which recurrent loops maintain state and which move it.

## Similar wiring can conceal different dynamics

[Green et al. (2017)](../papers/2017-a-neural-circuit-architecture-for-angular-integration-in-drosophila/notes.md) separates P-EN subtypes with similar shifted projections but different bridge phases and leading/trailing activity relative to EPG movement. Local activation gives the same anatomical displacement; natural participation can differ because the active locations differ. The proposed P-EN2 braking role remains a hypothesis in that paper.

Projecting measured bridge profiles through the anatomy fails to reproduce sharp EB profiles, especially for P-EN2. This is a concrete unresolved transformation for later physiology and connectomics to explain. A synapse table without compartment dynamics cannot settle it. The paper also exposes missing closure at the outer bridge glomeruli and suggests neighboring cells rather than assuming a perfect ring.

These studies constrain the current-heading estimator. They do not establish a remembered destination, and their temporal ordering relative to neural phase must not be mistaken for command timing relative to behavioral turns.

## Long-term bearing retrieval constrains the reference-frame interface

[Weisman et al. (2025 preprint)](../papers/2025-weisman-long-term-goal-angle/notes.md) shows days-to-weeks preferred bearings, repeated correction of virtual rotations and retrieval after twelve hours without the cue. Long intervals of deviation or incoherent dark walking need not erase the preference. This is virtual bearing maintenance, not demonstrated return to a remembered food location.

The same world bearing can survive darkness if the compass mapping remains stable, if the goal changes internal coordinates along with compass remapping, or if another controller retrieves the preference. The paper records behavior and does not resolve those circuit alternatives. It also does not establish whether the preference is learned versus an enduring individual bias. Static connectivity can constrain candidate interactions but cannot alone identify that distinction.

Survival selection (26 of 81 in the principal cohort), locomotion-dependent feeding, and substantial within-fly variability qualify generality. The timed-feeding supplement extends behavior to roughly two weeks and argues that the walking contingency is not required. These details belong in the behavioral account because state, retention and expression are separate mechanisms.

## Visual calibration is learned, so memory needs a compatible frame

[Kim et al. (2019)](../papers/2019-generation-of-stable-heading-representations-in-diverse-visual-scenes/notes.md) shows that scene-to-compass mapping can be experimentally rewritten, even reversed in some flies. Visual feature patterns need not be pure sinusoids: learning can align a complex visual input with a phase maintained by recurrent dynamics. Elevation-sensitive features disambiguate yaw without representing two-dimensional position.

The supplement makes memory interference explicit. Presynaptically gated inhibitory plasticity can protect inactive visual channels, whereas postsynaptically gated plasticity can modify them whenever the compass cell is active. Scene retrieval does not uniquely establish either rule; deterministic scene similarity or residual weights can also restore an offset. Connectivity alone does not reveal these learning rules or an individual's learned calibration.

This sharpens the interface with the long-term bearing results. A shared offset cancels from a goal–heading comparison, but changing the compass without transforming the goal rotates the intended world bearing. A complete food-return account must explain how calibration, goal retrieval and displacement memory stay compatible across scene changes and translation.

[Fisher et al. (2019)](../papers/2019-sensorimotor-experience-remaps-visual-input-to-a-heading-direction-network/notes.md) adds direct voltage measurements: visual inhibition of individual E-PGs is selective, ring-neuron perturbations affect that inhibition, and ambiguous visuomotor experience changes receptive fields. Broad anatomical overlap is therefore compatible with a selective, experience-dependent effective input map. The specific associative LTD/LTP rule and its precise synaptic locus remain inferred from intact-network measurements. Retained changes in a compass calibration are still distinct from storing a desired destination.

## Steering toward a bearing is a controller, not the destination memory

[Green et al. (2019)](../papers/2019-a-neural-heading-estimate-is-compared-with-an-internal-goal-to-guide-oriented-navigat/notes.md) establishes a useful causal constraint: moving the neural compass estimate in darkness elicits turns that tend to restore its prior phase. Heading and an inferred goal are distinct, and forward speed also depends on alignment. The experiment stimulates P-ENs and reads E-PGs; it does not identify a goal-storage population or prove an exact phasor multiplication.

The supplementary controls qualify the motor interpretation. E-PG impairment leaves some front fixation, and its reduction of turning largely disappears after matching baseline walking speed. Impaired slowing remains clearer for half-turn perturbations. A behavioral synthesis must distinguish arbitrary-bearing control, direct visual fixation and general locomotor state rather than attributing all three to a single compass pathway.

This task involves spontaneous bearing maintenance under conditions favoring dispersal. It supplies neither a remembered food coordinate nor a position-dependent goal vector. Later goal and steering studies need to be linked to the additional computations that produce and update a destination-bearing signal.


## A candidate gate between sensing a direction and retaining it

[Lanz et al., October 2025 preprint](../papers/2025-lanz-recurrent-goal-memory/notes.md) develops the recurrent-memory hypothesis adjacent to Kathman's hΔK results. PFG receives compass input; selective inhibition of hΔK can, in their model, leave PFG following heading, while disinhibition recruits recurrence and retains the direction present at gate opening. Slow excitation makes useful persistence less dependent on fine tuning. Physiology supports feedback-dependent persistence and identifies inhibitory tangential inputs; imaging finds appropriate odor/turn signals in FB5V. The causal demonstration of a selective gate writing and releasing an imposed memory remains incomplete in this version.

This adds a candidate mechanism for a postodor run, not a stored food coordinate. Persistence may partly originate upstream because FB5V suppression itself persists. hΔK largely disappears during turns, so a return after a detour still requires identifying another retained state or a retrieval mechanism. Later code/data are public but differ from v1; their revision must be matched before using them as an exact reproduction.


## Learned refuge locations provide a stronger behavioral target

[Ofstad et al. (2011)](../papers/2011-visual-place-learning/notes.md) shows learned search for an absent cool refuge whose location is specified by a surrounding panorama. Coupled rotation of panorama and refuge preserves the learned relationship; uncoupled and dark controls do not show comparable learning. Retention exceeds the uncoupled control through two hours. This is a useful demonstration of destination-like memory beyond maintained heading, but it does not distinguish coordinates from view matching or a conditional route policy. Training largely begins from the preceding refuge, and no neural activity is recorded.

Driver-defined ellipsoid-body ring populations are necessary across training/testing, while several mushroom-body manipulations spare this particular task and impair odor learning. Therefore the whole-food-navigation account must distinguish visual refuge memory from learned odor value rather than treating one memory center as universally responsible. Acquiring, storing, retrieving and converting the visual memory into a changing goal direction remain separate unknowns.
