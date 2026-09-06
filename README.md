# Semantic Mechanics
### The Cultural Economics of Representation, Pragmatics, and Reclaimed Meaning
**Mathematical Linguistics Group (mlG)**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Model: Python](https://img.shields.io/badge/Model-Python%203.x-brightgreen.svg)](models/lifecycle.py)
[![Notebooks: Python & R](https://img.shields.io/badge/Notebooks-Python%20%7C%20R%20(Jupyter)-orange.svg)](notebooks/)

---

## Overview

Language is rarely static. It is not an immutable lookup table stored in an institutional dictionary, nor is it merely a passive statistical medium. Language operates as a continuous, dynamical economy: representations are minted under social constraint, circulated as credit within trusted groups, targeted for commercial extraction, debased through hyper-inflation, and actively inverted to reclaim autonomy.

**Semantic Mechanics** investigates two fundamental phenomena:

1. **Representational Genealogy**: How historical representations in mathematics and linguistics were selected not purely by abstract truth, but by printing ergonomics, institutional capital, and cognitive coordination costs (e.g., Leibniz vs. Newton in calculus, Chomskyan trees vs. Lambek pregroups in formal syntax).
2. **Semantic Inversion**: The pragmatic mechanism in literature, poetry, and hip-hop vernaculars that reclaims meaning by inverting the polarity of stigmatized signs ($f \mapsto f^{-1}$, e.g., turning "bad", "ill", or "sick" into markers of virtuosic mastery).

---

## The Four Mechanics of Symbolic Assets

Language operates analogously to a currency market with distinct lifecycle phases:

```
[1. Subcultural Minting]  -->  [2. In-Group Liquidity]  -->  [3. Institutional Arbitrage]
         ^                                                              │
         │                                                              ▼
[5. Semantic Inversion]   <--  [4. Debasement & Inflation] <────────────┘
```

1. **Minting (The Subculture)**: Innovation happens at the creative edge (the street, the cipher, the studio). Terms are minted with high informational density (Minimum Description Length).
2. **In-Group Liquidity**: Within the community, the term carries high trust, high social credit, and pragmatic nuance.
3. **Institutional Arbitrage**: Mainstream advertising agencies, entertainment platforms, and tech companies identify the cultural capital and extract it for margin, externalizing the cost to originators.
4. **Debasement & Inflation**: Once broadcast across mass commercial channels, the token loses its signaling specificity. Its information entropy surges, rendering it sterile.
5. **Inversion & Reclamation**: The vernacular originators abandon the burned token and mint a fresh semantic inverse, resetting the cycle.

---

## "Processing Culture": The Dual-Track Data Science Notebook Suite

The project provides complete parallel suites of executable Jupyter notebooks in both **Python** (`ipykernel`) and **R** (`ir` / `ggplot2` / `dplyr`), applying vector embeddings, dynamical systems modeling, and information theory to cultural evolution:

### The Complete Series

| # | Topic | Python Track | R Track | Focus |
|---|---|:---:|:---:|---|
| **01** | **Notational Economics** | [`01_python`](notebooks/python/01_notational_economics_diffusion.ipynb) | [`01_r`](notebooks/r/01_notational_economics_diffusion.ipynb) | Bass diffusion of notation (Leibniz vs. Newton, Chomsky vs. Lambek) and cognitive friction. |
| **02** | **Semantic Inversion** | [`02_python`](notebooks/python/02_semantic_inversion_embeddings.ipynb) | [`02_r`](notebooks/r/02_semantic_inversion_embeddings.ipynb) | Polarity inversion ($f \mapsto f^{-1}$) and 90% benchmark error on vernacular praise. |
| **03** | **Cultural Arbitrage** | [`03_python`](notebooks/python/03_cultural_arbitrage_and_debasement.ipynb) | [`03_r`](notebooks/r/03_cultural_arbitrage_and_debasement.ipynb) | 5-stage token lifecycle, marginal utility decay, and corporate saturation thresholds ($\theta^* \approx 35\%$). |
| **04** | **Pragmatic Density** | [`04_python`](notebooks/python/04_pragmatic_density_and_signifying.ipynb) | [`04_r`](notebooks/r/04_pragmatic_density_and_signifying.ipynb) | Double-voiced discourse, multisyllabic rhyme density (MSRD), and cryptographic resistance. |
| **05** | **Visual Empirical Studies** | [`05_python`](notebooks/python/05_linguistic_hypotheses_visual_studies.ipynb) | [`05_r`](notebooks/r/05_linguistic_hypotheses_visual_studies.ipynb) | Empirical tests for notational extinction, vocabulary horizons, and vernacular shields. |
| **06** | **HPC Cultural Mechanics** | [`06_python`](notebooks/python/06_hpc_cultural_mechanics_pipeline.ipynb) | — | Streaming zero-copy HPC pipeline for corpus phonetics and dynamic phase portraits. |

---

## Representational Case Studies

### 1. Leibniz vs. Newton (Calculus Notations)
Newtonian fluxions ($\dot{x}, \ddot{x}$) were tied to kinematic geometry, requiring the reader to already grasp the physical trajectory. Leibniz designed his differential notation ($\frac{dy}{dx}, \int y\,dx$) as an algebraic ledger. European continental mathematics outpaced British mathematics for over a century because Leibniz's notation lowered the cognitive barrier to entry and was economically optimized for movable type printing foundries.

### 2. Chomsky Trees vs. Lambek Pregroups (Linguistic Syntax)
Chomskyan phrase structure trees dominated post-war linguistics because they directly matched early von Neumann pushdown automata and were heavily funded by Cold War DARPA/military machine-translation grants. Joachim Lambek's pregroup grammars and categorical calculus, despite their mathematical elegance, lacked hardware-era alignment and institutional subsidies.

### 3. Vernacular Polarity Inversion (Hip-Hop & AAVE)
In African American Vernacular English and rap poetics, artists systematically invert the algebraic sign of words:
$$\text{Valuation}: \quad \mathcal{V}(w) = -\mathcal{V}_{\text{inst}}(w)$$
Taking carceral, pathological, or debasing words ("bad", "ill", "cold") and inverting them into highest artistic praise operates as a cryptographic defense: an outsider hears pathology; an insider recognizes virtuosity.

---

## Quickstart

### Running the Python Simulation
```bash
python3 models/lifecycle.py
```

### Running the Jupyter Notebooks
To run either the Python or R suite:
```bash
# Python suite
jupyter lab notebooks/python/

# R suite (requires IRkernel)
jupyter lab notebooks/r/
```

---

## Repository Structure

```
semantic-mechanics/
├── lectures/
│   ├── lecture_01_representational_genealogy.pdf  # Monograph 01: Politics of Notation (6 pp)
│   ├── lecture_01_representational_genealogy.tex  # LaTeX source for Lecture 01
│   ├── lecture_01_representational_genealogy.md   # Notes, syllabus & environment setup
│   ├── lecture_02_semantic_inversion.pdf          # Monograph 02: Semantic Inversion (6 pp)
│   ├── lecture_02_semantic_inversion.tex          # LaTeX source for Lecture 02
│   └── lecture_02_semantic_inversion.md           # Notes, syllabus & phonetic PoW
├── models/
│   ├── lifecycle.py                        # Simulation of token inflation & inversion
│   └── case_studies.json                   # Structured case studies in math & vernaculars
├── notebooks/
│   ├── python/                             # Python 3 Jupyter Suite (01–06)
│   │   ├── 01_notational_economics_diffusion.ipynb
│   │   ├── 02_semantic_inversion_embeddings.ipynb
│   │   ├── 03_cultural_arbitrage_and_debasement.ipynb
│   │   ├── 04_pragmatic_density_and_signifying.ipynb
│   │   ├── 05_linguistic_hypotheses_visual_studies.ipynb
│   │   └── 06_hpc_cultural_mechanics_pipeline.ipynb
│   └── r/                                  # R (IRkernel / ggplot2) Suite (01–05)
│       ├── 01_notational_economics_diffusion.ipynb
│       ├── 02_semantic_inversion_embeddings.ipynb
│       ├── 03_cultural_arbitrage_and_debasement.ipynb
│       ├── 04_pragmatic_density_and_signifying.ipynb
│       └── 05_linguistic_hypotheses_visual_studies.ipynb
├── data/
│   └── corpus/                             # Empirical Linguistic & Cultural Datasets
│       ├── notational_extinction.csv
│       ├── vocabulary_horizon.csv
│       └── euphemism_treadmill.csv
└── README.md
```
