# Initial MaleCNS graph exploration

Dataset `male-cns:v1.0`, downloaded and verified 2026-09-10. See [manifest](../data/manifest.json) and [checksum receipt](../data/download_receipt.json).

The initial pass downloaded the full confidence-0.5 segment graph plus annotations and transmitter predictions (1,109,008,094 bytes total). No graph edge-strength threshold was added.

| Local measurement | Value |
|---|---:|
| Annotation rows | 211,577 |
| Rows annotated with class CX | 2,950 |
| Full graph rows | 151,856,684 |
| Full graph sum of weights | 311,833,243 |
| Selected navigation seed neurons | 1,486 |
| Selected seed types | 76 |
| Within-seed graph rows | 131,701 |
| Within-seed sum of weights | 1,057,187 |

These are measurements of the downloaded exports, not the release's curated neuron or synapse headline counts. The full export includes segments beyond curated neurons; its weight sum must not be substituted for the publication's synapse count. The exact cause of any headline/export difference requires checking the release's counting conventions and segment filters.

The seed selection includes EPG/EPGt, PEN1/PEN2, PEG, Delta7, EL, PFL1/2/3, PFGs, and ER/PFN/PFR/FC/hDelta type prefixes. It is a reproducible starting set, not the complete CX or all navigation-related cells. Annotation rows without matching type labels are excluded. All edges among selected IDs are retained.

Outputs in [data/derived](../data/derived): neuron annotations and cross-dataset type labels, counts per type, cell-to-cell edges, aggregate type connectivity, and direct PFL2/PFL3 descending partners. Aggregate weights are raw sums, not effective coupling strengths or input-normalized selectivity.

A naming issue matters immediately: FC2 is split into FC2A/B/C in this release, and PEN1/PEN2 appear as `PEN_a(PEN1)` and `PEN_b(PEN2)`. Morphological/driver validation is required before transferring results from the experimental literature. No matched-female comparison or dynamical simulation has yet been performed.
