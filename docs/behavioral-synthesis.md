# Fly navigation: building complete behavioral explanations

This is a growing synthesis, not a completed model of fly navigation. It currently incorporates full readings of Lyu et al. (2022) and Mussells Pires et al. (2024). Other papers in the library remain reading targets unless their logs say otherwise. The [research approach](../RESEARCH_APPROACH.md) defines the sequence: literature and synthesis first, then targeted connectome analysis and simulations.

## The motivating behavior

A fly encounters something useful, leaves, and later navigates toward it from its current situation. A mechanistic account must specify what experience changes, what persists, how current sensory/self-motion information is represented, how the remembered objective determines an action, and what ends or changes that action.

Several representations could support superficially similar behavior. An odor-value association, a remembered compass bearing, a home vector, recognition of a familiar view and a remembered location are different computational objects. Evidence for one does not establish all the others. The reading program must follow actual behavioral demonstrations rather than assume a metric map in advance.

## What the first two papers establish

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

The existing library covers compass dynamics, movement transformations, steering, learning and recent olfactory work. Read the companion Westeinde study next to compare PFL3 computation and neighboring PFL pathways. Then connect goal learning and odor/wind persistence to the upstream side, while returning to canonical compass papers to audit reference frames and memory claims. Follow necessary references beyond the initial 21 entries, especially papers experimentally connecting sensory history, persistent objectives and behavior.

Only after that synthesis should novel-cell hypotheses be prioritized. Their eventual records should state the candidate signal and behavioral role, anatomical and physiological support, alternatives, and what a simulation can discriminate. Successful simulation establishes a possible mechanism under stated assumptions; it does not alone discover the neuron's biological function.
