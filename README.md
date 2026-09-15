# continuouslearning

Nico's learning fork of [pwang724/fly-circuit-exploration](https://github.com/pwang724/fly-circuit-exploration): a plan to train a tiny model that keeps learning by rewriting its own weights, the way the fly's home-vector circuit is proposed to.

- [Tiny Fly Model Roadmap](docs/roadmap/index.html): five levels from the hand-built simulation to our own trained model, with exact numbers, code, success criteria and failure fixes.
- [The Homing Exam](docs/roadmap/homing-exam.html): the level 1 experiment as a live, playable simulation.
- [Level 3 Training Plan](docs/roadmap/level3-plan.html): build order, decisions, compute, curriculum, checks, success and the failure playbook, before any code runs.
- [Inside Runs 1, 2 and 3](docs/roadmap/inside-runs.html): what the level 3 networks actually learned, drawn from their checkpoints, explained for a beginner.
- `level1/` and `level2/`: local apps that run the level 1 and level 2 searches (`python3 level1/server.py`, `python3 level2/server.py`); `level3/` trains the network and serves a live dashboard (`python3 level3/server.py`).

Original project README follows.

---

# Fly circuit exploration

A research workspace for understanding navigation in the Drosophila central complex, using the **MaleCNS v1.0** connectome and primary literature. Started 2026-09-10.

- [Research objective and sequence](RESEARCH_APPROACH.md): complete behavioral accounts first, then targeted structure/function analysis.
- [Paper library](papers/README.md): one folder per paper, PDFs/supplements, reading status, and detailed notes.
- [Reading map](docs/literature.md): canonical results and 2024–2026 developments.
- [Circuit map and open questions](docs/circuit-and-open-questions.md).
- [First graph analysis](docs/connectome.md).
- [Audit of the findings and whole-brain screens, 2026-09-13](docs/audit-2026-09-13.md).

## Reproduce the data work

```sh
python3 -m pip install -r requirements.txt
python3 scripts/download_connectome.py
python3 scripts/analyze_circuit.py
```

Raw connectome files live in `data/raw/` (gitignored). The downloader pins cloud object generations, checks publisher MD5 and sizes, and records SHA-256. The repository contains provenance and small derived tables so a clone can reproduce the analysis without putting the 1.1 GB graph in Git.

Downloaded: full segment-to-segment graph, neuron annotations, and body-level neurotransmitter predictions. Not downloaded: EM imagery, full spatial synapse tables, all skeletons, or a neuPrint database. [Official download information](https://male-cns.janelia.org/download/).

Paper notes distinguish completed full-text/figure/supplement readings from preliminary entries. No claim that all papers are fully reviewed until each folder's reading record says so.

## Attribution

MaleCNS data: FlyEM/HHMI Janelia, University of Cambridge, MRC LMB, and Google Research; [project](https://male-cns.janelia.org/), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Derived connectivity tables retain this attribution. Paper PDFs retain their authors' and publishers' licenses; original research notes are separate from source documents.
