# Semantic Mechanics
### The Cultural Economics of Representation, Pragmatics, and Reclaimed Meaning
**Mathematical Linguistics Group (mlG)**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Paper: PDF](https://img.shields.io/badge/Paper-PDF%20(4%20Pages)-purple.svg)](papers/semantic_mechanics.pdf)
[![Model: Python](https://img.shields.io/badge/Model-Python%203.x-brightgreen.svg)](models/lifecycle.py)
[![Notebooks: Jupyter (Python & R)](https://img.shields.io/badge/Notebooks-Jupyter%20(Python%20%26%20R)-orange.svg)](notebooks/)

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

## "Processing Culture": The Data Science Notebook Series

A complete series of executable Jupyter notebooks in Python and R applying rigorous data science, vector embeddings, dynamical systems modeling, and information theory to cultural evolution:

| # | Notebook | Environment | Core Methods & Empirical Findings |
|---|---|---|---|
| **01** | [`01_notational_economics_diffusion.ipynb`](notebooks/01_notational_economics_diffusion.ipynb) | Python 3 (`ipykernel`) | **Notational Economics & Historical Network Diffusion**: Bass diffusion models of Leibniz differentials vs. Newtonian fluxions (1690–1830) and Chomskyan phrase trees vs. Lambek pregroups (1955–2025). Quantifies typing/printing transaction costs and institutional lock-in. |
| **02** | [`02_semantic_inversion_embeddings.ipynb`](notebooks/02_semantic_inversion_embeddings.ipynb) | Python 3 (`ipykernel`) | **Semantic Inversion ($f \mapsto f^{-1}$) in Vernacular Embeddings**: Curated dual-register corpus (Standard vs. Hip-Hop). Empirically measures the catastrophic 90% false-negative failure rate of static sentiment analyzers (VADER) and projects lexical migration toward a **Virtuosity Attractor Pole** vs. **Pathology Attractor Pole**. |
| **03** | [`03_cultural_arbitrage_and_debasement.ipynb`](notebooks/03_cultural_arbitrage_and_debasement.ipynb) | R (`ir` kernel) | **Cultural Arbitrage, The Commercialization Cliff, and Slang Half-Life**: Modeled with `ggplot2` and `dplyr`. Simulates the 5-stage lifecycle across case studies (`on fleek`, `bae`, `rizz`, `ill`). Identifies the "Cringe Cliff" tipping point at $\theta^* \approx 35\%$ corporate penetration where marginal in-group utility drops below zero. |
| **04** | [`04_pragmatic_density_and_signifying.ipynb`](notebooks/04_pragmatic_density_and_signifying.ipynb) | Python 3 (`ipykernel`) | **Pragmatic Density, Gatesian *Signifyin(g)*, and Information Theory**: Multi-syllabic rhyme resonance matrices and dual-channel decoding asymmetry across commercial pop, traditional verse, and virtuosic hip-hop (MF DOOM, Rakim, Mos Def, Kendrick Lamar). Demonstrates how double-voiced poetics serves as cryptographic resistance. |

All notebooks follow the strict data science standards: modular cells, high-contrast publication plots, executable outputs, and structured final summary sections (`### Q&A`, `### Data Analysis Key Findings`, `### Insights or Next Steps`).

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

### Running the Lifecycle Simulation
A discrete-time dynamical simulation modeling in-group capital, mainstream adoption, and semantic entropy:

```bash
python3 models/lifecycle.py
```

### Running the Notebooks
To run or inspect the notebooks interactively:
```bash
jupyter lab notebooks/
```

---

## Repository Structure

```
semantic-mechanics/
├── papers/
│   ├── semantic_mechanics.tex    # LaTeX manuscript (single-column, anonymized)
│   └── semantic_mechanics.pdf    # Compiled research paper (4 pages)
├── models/
│   ├── lifecycle.py             # Simulation of token inflation & inversion
│   └── case_studies.json        # Structured case studies in math & vernaculars
├── notebooks/
│   ├── 01_notational_economics_diffusion.ipynb     # Python 3: Diffusion of calculus & syntax
│   ├── 02_semantic_inversion_embeddings.ipynb      # Python 3: Vernacular sign-flipping & VADER error
│   ├── 03_cultural_arbitrage_and_debasement.ipynb   # R (IRkernel): 5-stage slang lifecycle & cringe cliff
│   └── 04_pragmatic_density_and_signifying.ipynb    # Python 3: Multi-syllabic poetics & Signifyin(g)
├── data/
│   └── corpus/                  # Excerpts and comparative text corpora
└── README.md
```

---

## Identity & Collaboration

Semantic Mechanics is an initiative of the **Mathematical Linguistics Group (mlG)** (`https://github.com/Mathematical-Linguistics`), connecting formal syntax and category theory with cultural evolution, pragmatics, and living language.
