# Semantic Mechanics
### The Cultural Economics of Representation, Pragmatics, and Reclaimed Meaning
**Mathematical Linguistics Group (mlG)**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Paper: PDF](https://img.shields.io/badge/Paper-PDF%20(4%20Pages)-purple.svg)](papers/semantic_mechanics.pdf)
[![Model: Python](https://img.shields.io/badge/Model-Python%203.x-brightgreen.svg)](models/lifecycle.py)

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

Example output:
```text
=== Simulating Semantic Mechanics for: 'sick/ill' (Vernacular (AAVE/Hip-Hop)) ===
Epoch  State              Capital    Adoption   Entropy    Action
-----------------------------------------------------------------
1      sick/ill           1.00       0.00       1.00       Circulating
2      sick/ill           0.97       0.13       1.04       Circulating
3      sick/ill           0.92       0.26       1.11       Circulating
4      sick/ill           0.84       0.38       1.23       Circulating
5      sick/ill           0.75       0.51       1.38       Circulating
6      sick/ill           0.64       0.64       1.57       Circulating
7      sick/ill           0.53       0.76       1.80       Circulating
8      sick/ill           0.43       0.89       2.07       Circulating
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
├── data/
│   └── corpus/                  # Excerpts and comparative text corpora
└── README.md
```

---

## Identity & Collaboration

Semantic Mechanics is an initiative of the **Mathematical Linguistics Group (mlG)** (`https://github.com/Mathematical-Linguistics`), connecting formal syntax and category theory with cultural evolution, pragmatics, and living language.
