# Werr Multi-Layer Algebraic Sieve & Vélu Isogeny Engine: High-Rank Elliptic Curve Records

[![arXiv](https://img.shields.io/badge/arXiv-cs.LO%20%7C%20math.NT-b31b1b.svg)](arxiv_package/Werr_Elliptic_Sieve_ICARM_Preprint.pdf)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23436282.svg)](https://doi.org/10.5281/zenodo.23436282)
[![NSF ICARM Leaderboard](https://img.shields.io/badge/NSF%20ICARM-Certified%20Leaderboard-blue)](https://elliptic-rank.icarm.cloud/user/114)
[![Curves Accepted](https://img.shields.io/badge/Accepted%20Curves-230%20(100%25%20Verified)-success)](https://elliptic-rank.icarm.cloud/user/114)
[![Conductor Certification](https://img.shields.io/badge/Conductor%20log%20N-100%25%20Factored%20(230%2F230)-brightgreen)](https://elliptic-rank.icarm.cloud/user/114)
[![#1 Records](https://img.shields.io/badge/%231%20Gold%20Records-30-gold)](https://elliptic-rank.icarm.cloud/user/114)
[![Top-3 Podiums](https://img.shields.io/badge/Top--3%20Podiums-80-orange)](https://elliptic-rank.icarm.cloud/user/114)
[![Top-10 Placements](https://img.shields.io/badge/Top--10%20Placements-418-blueviolet)](https://elliptic-rank.icarm.cloud/user/114)
[![License: CC-BY-4.0](https://img.shields.io/badge/License-CC--BY--4.0-yellow.svg)](LICENSE)
[![Academic: werr.io](https://img.shields.io/badge/Academic%20Portal-werr.io-0284c7.svg?logo=cloudflare&logoColor=white)](https://werr.io/)
[![Web3: werracle.io](https://img.shields.io/badge/Web3%20Protocol-werracle.io-f59e0b.svg?logo=cloudflare&logoColor=white)](https://werracle.io/)
[![Corporate: werracle.com](https://img.shields.io/badge/Corporate%20Portal-werracle.com-2b3bd1.svg?logo=cloudflare&logoColor=white)](https://werracle.com/)
[![Cloud Vault: R2 Active](https://img.shields.io/badge/Cloud%20Vault-Cloudflare%20R2%20Active-f38020.svg?logo=cloudflare&logoColor=white)](https://werracle.com/)
[![ORCID: Volkan Dağlı](https://img.shields.io/badge/ORCID-0009--0000--1587--8703-green)](https://orcid.org/0009-0000-1587-8703)
[![ORCID: Zerrin Dağlı](https://img.shields.io/badge/ORCID-0000--0001--9490--6425-green)](https://orcid.org/0000-0001-9490-6425)
[![ORCID: Dağhan Dağlı](https://img.shields.io/badge/ORCID-0009--0003--2492--8313-green)](https://orcid.org/0009-0003-2492-8313)

---

## 🏛️ Executive Summary & Official Public Certification

This repository and dataset house the computational number theory research, algorithms, datasets, and reproduction tools developed by **ITouch Systems** for high-rank elliptic curves over ℚ.

Through a harmonized combination of:
1. **The 4-Stage Werr Multi-Layer Algebraic Sieve** (coupling algebraic root invariants gcd(a₄, a₆, Δ, c₄, c₆), cubic divisor peeling Δ = d₀ · s³, and parallel ECM/MPQS integer factorization), and
2. **Systematic Vélu 2- and 3-Isogeny Graph Transport** across rational torsion subgroups (ℤ/4ℤ ↔ ℤ/2ℤ × ℤ/2ℤ, ℤ/4ℤ → ℤ/2ℤ × ℤ/4ℤ, ℤ/6ℤ ↔ ℤ/6ℤ, ℤ/2ℤ ↔ ℤ/2ℤ),

we submitted and had **`230` distinct curves** (`#4308` through `#4537`) verified and permanently recorded on the **NSF Institute for Computer-Aided Reasoning in Mathematics ([ICARM](https://icarm.io/))** official [Elliptic Curve Rank Leaderboard](https://elliptic-rank.icarm.cloud/).

### 🏆 Key Official Achievements on `elliptic-rank.icarm.cloud`
* **Official Contributor Profile:** [Volkan Dagli (`user/114`)](https://elliptic-rank.icarm.cloud/user/114)
* **Total Accepted Top-10 Curves:** **`230` curves** (`status: created`)
* **Certified Conductor Factorizations (log N):** **`230 / 230` (`100.0%`)** with zero unfactored conductors (`?`)
* **Active `(Torsion, Rank)` Leaderboards in Top 10:** **`43` distinct leaderboards**
* **Total `#1` (First Place / Gold Record) Placements:** **`30` First-Place Records**
* **Total `Top-3` (Podium) Placements:** **`80` Podiums**
* **Total `Top-10` Metric Placements:** **`418` Placements** across Conductor N, Discriminant |Δ|, Faltings Height, and Naive Height.

---

## 🤝 Mathematical Foundations, Scientific Lineage & Intellectual Attribution

In mathematics and open science, true progress rests on transparency, rigorous verification, and generous intellectual honesty:

1. **Original Discoverers of High-Rank Curve Families:**  
   Full credit for the underlying geometric fibrations, parametric families, and numerical specialization searches belongs to their original discoverers in the literature:
   * **Prof. Noam D. Elkies** (Harvard University)
   * **Prof. Andrej Dujella** (University of Zagreb)
   * **Prof. Michael Rubinstein** (University of Waterloo)
   * **Dr. Zev Klagsbrun**
   * **Layr-Labs / Yukon Challenge Contributors & Specializers**
   * **K. Eriksson, P. Brumer, J. Silverman, J. Cremona, and collaborators.**

2. **NSF ICARM & Platform Maintainers:**  
   We gratefully acknowledge the **NSF Institute for Computer-Aided Reasoning in Mathematics (ICARM)**, supported by **U.S. National Science Foundation Grant DMS-2425401**, and thank **David Renshaw** (`@dwrensha`), **Seewoo Lee** (`@seewoo5`), and the ICARM team for maintaining the [elliptic-rank.icarm.cloud](https://elliptic-rank.icarm.cloud/) platform and its in-worker PARI/GP 2.17.2 WASM verification pipeline.

3. **Computing Infrastructure:**  
   Dedicated bare-metal verification clusters and computing resources were provided by **Bekirhan Dağlı** (Managing Partner) and **ITouch Systems Research & Development**.

4. **Our Algorithmic Contribution:**  
   Our specific scientific contribution was two-fold:
   * **Closing the log N Gap:** Resolving all remaining composite discriminant factorizations (up to 70–105 digits) using our 4-stage algebraic sieve so that conductors log N could be certified machine-verifiably for all 230 curves.
   * **Isogeny Frontier Exploration:** Uncovering strictly smaller minimal Weierstrass models (lower |Δ|, smaller Faltings and naive heights) along rational 2- and 3-isogeny graphs without altering the Mordell–Weil rank or conductor.

---

## 📊 Summary of #1 (Gold) Records (`30` First-Place Placements)

| Torsion Subgroup T | Rank Bound | #1 (Gold Record) Metrics | Curve ID | Additional Podium Placements |
| :--- | :---: | :--- | :---: | :--- |
| **ℤ/2ℤ × ℤ/2ℤ (`[2, 2]`)** | **`Rank ≥ 9`** | **🥇 `#1` Conductor (N)**<br> **🥇 `#1` Discriminant (\|Δ\|)**<br> **🥇 `#1` Faltings Height**<br> **🥇 `#1` Naive Height** | [`#4315`](https://elliptic-rank.icarm.cloud/curve/4315) | *Grand Slam: 4 out of 4 #1 records!* |
| **ℤ/2ℤ × ℤ/2ℤ (`[2, 2]`)** | **`Rank ≥ 8`** | **🥇 `#1` Naive Height** | [`#4314`](https://elliptic-rank.icarm.cloud/curve/4314) | 🥈 `#2` \|Δ\|, 🥈 `#2` Faltings, 🥉 `#3` Conductor |
| **ℤ/2ℤ × ℤ/2ℤ (`[2, 2]`)** | **`Rank ≥ 7`** | **🥇 `#1` Discriminant (\|Δ\|)**<br> **🥇 `#1` Faltings Height**<br> **🥇 `#1` Naive Height** | [`#4313`](https://elliptic-rank.icarm.cloud/curve/4313) | (`#6` Conductor N) |
| **ℤ/2ℤ × ℤ/4ℤ (`[4, 2]`)** | **`Rank ≥ 6`** | **🥇 `#1` Discriminant (\|Δ\|)**<br> **🥇 `#1` Faltings Height**<br> **🥇 `#1` Naive Height** | [`#4320`](https://elliptic-rank.icarm.cloud/curve/4320) | (`#5` Conductor N) |
| **ℤ/2ℤ × ℤ/4ℤ (`[4, 2]`)** | **`Rank ≥ 5`** | **🥇 `#1` Discriminant (\|Δ\|)**<br> **🥇 `#1` Faltings Height**<br> **🥇 `#1` Naive Height** | [`#4322`](https://elliptic-rank.icarm.cloud/curve/4322) | 🥈 `#2` Conductor N |
| **ℤ/4ℤ (`[4]`)** | **`Rank ≥ 8`** | **🥇 `#1` Discriminant (\|Δ\|)**<br> **🥇 `#1` Faltings Height**<br> **🥇 `#1` Naive Height** | [`#4319`](https://elliptic-rank.icarm.cloud/curve/4319) | 🥉 `#3` Conductor N |
| **ℤ/4ℤ (`[4]`)** | **`Rank ≥ 7`** | **🥇 `#1` Discriminant (\|Δ\|)**<br> **🥇 `#1` Faltings Height**<br> **🥇 `#1` Naive Height** | [`#4318`](https://elliptic-rank.icarm.cloud/curve/4318) | 🥉 `#3` Conductor N |
| **ℤ/5ℤ (`[5]`)** | **`Rank ≥ 7`** | **🥇 `#1` Discriminant (\|Δ\|)**<br> **🥇 `#1` Faltings Height**<br> **🥇 `#1` Naive Height** | [`#4321`](https://elliptic-rank.icarm.cloud/curve/4321) | 🥈 `#2` Conductor N |
| **ℤ/5ℤ (`[5]`)** | **`Rank ≥ 5`** | **🥇 `#1` Discriminant (\|Δ\|)** | [`#4380`](https://elliptic-rank.icarm.cloud/curve/4380) | 🥈 `#2` \|Δ\| ([`#4381`](https://elliptic-rank.icarm.cloud/curve/4381)), 🥉 `#3` Faltings |
| **ℤ/2ℤ (`[2]`)** | **`Rank ≥ 9`** | **🥇 `#1` Faltings Height**<br> **🥇 `#1` Naive Height** | [`#4312`](https://elliptic-rank.icarm.cloud/curve/4312) | 🥉 `#3` Discriminant \|Δ\| |
| **ℤ/2ℤ (`[2]`)** | **`Rank ≥ 7`** | **🥇 `#1` Naive Height** | [`#4311`](https://elliptic-rank.icarm.cloud/curve/4311) | 🥈 `#2` \|Δ\|, 🥈 `#2` Faltings ([`#4311`](https://elliptic-rank.icarm.cloud/curve/4311)), 🥉 `#3` \|Δ\| ([`#4511`](https://elliptic-rank.icarm.cloud/curve/4511)) |
| **ℤ/3ℤ (`[3]`)** | **`Rank ≥ 8`** | **🥇 `#1` Naive Height** | [`#4317`](https://elliptic-rank.icarm.cloud/curve/4317) | 🥈 `#2` Faltings ([`#4317`](https://elliptic-rank.icarm.cloud/curve/4317)), 🥉 `#3` \|Δ\| ([`#4324`](https://elliptic-rank.icarm.cloud/curve/4324)) |
| **ℤ/3ℤ (`[3]`)** | **`Rank ≥ 7`** | **🥇 `#1` Faltings Height**<br> **🥇 `#1` Naive Height** | [`#4316`](https://elliptic-rank.icarm.cloud/curve/4316) | 🥈 `#2` \|Δ\| ([`#4327`](https://elliptic-rank.icarm.cloud/curve/4327)), 🥈 `#2` Naive ([`#4330`](https://elliptic-rank.icarm.cloud/curve/4330)) |

---

## 👥 Canonical Authors & Institutional Affiliations

* **Volkan Dağlı** — Lead Researcher & Systems Architect  
  *Anadolu University, Eskişehir, Türkiye & ITouch Systems, Adana, Türkiye*  
  ORCID: [0009-0000-1587-8703](https://orcid.org/0009-0000-1587-8703) &bull; Email: `ask@answerr.me`
* **Zerrin Dağlı** — Mathematical Modeling & Data Verification  
  *Mersin University, Mersin, Türkiye & Yusuf Kalkavan Anadolu Lisesi, Mersin, Türkiye*  
  ORCID: [0000-0001-9490-6425](https://orcid.org/0000-0001-9490-6425)
* **Dağhan Dağlı** — Computational Benchmarking & Algorithmic Analysis  
  *Toros Science High School, MEV (Toros University), Mersin, Türkiye*  
  ORCID: [0009-0003-2492-8313](https://orcid.org/0009-0003-2492-8313)
* **Bekirhan Dağlı** — Managing Partner, ITouch Systems, Adana, Türkiye  
  *(Computing Clusters & Infrastructure Contributor)*

GitHub Repository: [pCwOrM/werr-elliptic-sieve](https://github.com/pCwOrM/werr-elliptic-sieve)

---

## 📜 Citation & Permanent Record

* **CERN Zenodo Concept DOI (All Versions):** [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23436282.svg)](https://doi.org/10.5281/zenodo.23436282) &bull; [10.5281/zenodo.23436282](https://doi.org/10.5281/zenodo.23436282)
* **CERN Zenodo Release v1.0 DOI:** [10.5281/zenodo.23436283](https://doi.org/10.5281/zenodo.23436283)
* **arXiv Preprint (`submit/8246351`, `cs.LO` | `math.NT` | `cs.SC` | `math.AG`):** [`arxiv_package/Werr_Elliptic_Sieve_ICARM_Preprint.pdf`](arxiv_package/Werr_Elliptic_Sieve_ICARM_Preprint.pdf) &bull; Bundle: [`arxiv_package/arxiv_bundle.tar.gz`](arxiv_package/arxiv_bundle.tar.gz)
* **arXiv Submission Guide:** [`ARXIV_YUKLEME_REHBERI.md`](ARXIV_YUKLEME_REHBERI.md)
* **Camera-Ready Research Monograph:** [`Werr_Elliptic_Sieve_ICARM_Leaderboard_Monograph.pdf`](Werr_Elliptic_Sieve_ICARM_Leaderboard_Monograph.pdf)

If you use this dataset, algorithms, or isogeny models in academic work, please cite:

```bibtex
@misc{dagli2026werr_elliptic_sieve,
  author       = {Da{\u{g}}l{\i}, Volkan and Da{\u{g}}l{\i}, Zerrin and Da{\u{g}}l{\i}, Da{\u{g}}han},
  title        = {{Werr Multi-Layer Algebraic Sieve & V{\'e}lu Isogeny Engine: 100% Conductor Certification (log N) and High-Rank Elliptic Curve Records on the NSF ICARM Leaderboard}},
  year         = {2026},
  month        = {oct},
  publisher    = {CERN Zenodo},
  doi          = {10.5281/zenodo.23436282},
  url          = {https://doi.org/10.5281/zenodo.23436282},
  howpublished = {\url{https://doi.org/10.5281/zenodo.23436282}},
  note         = {Certified on NSF ICARM Elliptic Curve Rank Leaderboard (Grant DMS-2425401), contributor: user/114. Computing infrastructure contributed by Bekirhan Da{\u{g}}l{\i} (ITouch Systems).}
}
```

---

## 🏛️ Associated Formal Verification, World Records & Scientific Corpus

All monographs, formal Lean 4 specifications, and empirical datasets across the **WERR & ITouch Systems Research Group** are permanently archived on **CERN Zenodo**, **arXiv**, **Elsevier SSRN**, and **Hugging Face**.  
*(Primary links use **CERN Zenodo Concept DOIs / Çatı DOI**, which automatically resolve to the latest published version while preserving exact version-pinned reproducibility.)*

| # | Pillar / Monograph | Core Contribution & Focus | 👑 Concept DOI (Always Latest) | 📌 Latest Version DOI | arXiv / SSRN / Hugging Face & Verification Status | Primary Repository |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | **Paper 1: FNS** | Procedural Weight Derivation & Non-Linear Decision Boundaries (v3) | [**`10.5281/zenodo.22774934`**](https://doi.org/10.5281/zenodo.22774934) | [`10.5281/zenodo.22867037`](https://doi.org/10.5281/zenodo.22867037) | [**SSRN: 7659198**](https://papers.ssrn.com/abstract=7659198) *(Distributed)* • Multi-Seed Pareto & Manifold Parity | [`pCwOrM/fractal-neural-synthesis`](https://github.com/pCwOrM/fractal-neural-synthesis) |
| **02** | **Paper 2: OED** | Orbital Error Dynamics, Ephemeral Parameter Resonance & CD4+ Gating (v1) | [**`10.5281/zenodo.22900464`**](https://doi.org/10.5281/zenodo.22900464) | [`10.5281/zenodo.22900465`](https://doi.org/10.5281/zenodo.22900465) | [`arXiv:2609.30115`](https://arxiv.org/abs/2609.30115) • [🤗 HF Paper](https://huggingface.co/papers/2609.30115) *(Verified)* • `TR 2026/016285` | [`pCwOrM/fractal-neural-synthesis`](https://github.com/pCwOrM/fractal-neural-synthesis) |
| **03** | **Paper 3: WERR Map** | Universal Natural Language Decision Map & Real-Time Edge Triage (v2) | [**`10.5281/zenodo.22867425`**](https://doi.org/10.5281/zenodo.22867425) | [`10.5281/zenodo.22939253`](https://doi.org/10.5281/zenodo.22939253) | [`arXiv:2609.25498`](https://arxiv.org/abs/2609.25498) • [🤗 HF Paper](https://huggingface.co/papers/2609.25498) • [🤗 HF Dataset](https://huggingface.co/datasets/pCwOrM/werr_open_decisions) | [`pCwOrM/werr`](https://github.com/pCwOrM/werr) • [`pCwOrM/answerr`](https://github.com/pCwOrM/answerr) |
| **04** | **Paper 4: Werracle** | Sub-Cent Intra-Block AI Reflex Oracles & Flash-Loan Circuit Breakers (v1) | [**`10.5281/zenodo.22942598`**](https://doi.org/10.5281/zenodo.22942598) | [`10.5281/zenodo.22942599`](https://doi.org/10.5281/zenodo.22942599) | [`arXiv:2609.30719`](https://arxiv.org/abs/2609.30719) • [**SSRN: 7626279**](https://papers.ssrn.com/abstract=7626279) • [🤗 HF Paper](https://huggingface.co/papers/2609.30719) | [`pCwOrM/werracle`](https://github.com/pCwOrM/werracle) • [`pCwOrM/werralem`](https://github.com/pCwOrM/werralem) |
| **05** | **Paper 5: Formal Lean 4** | Zero-Storage Procedural Synthesis: Lean 4 Verification & 40-Core Validation | [**`10.5281/zenodo.22774934`**](https://doi.org/10.5281/zenodo.22774934) | [`10.5281/zenodo.22867037`](https://doi.org/10.5281/zenodo.22867037) | [`arXiv:2609.33066`](https://arxiv.org/abs/2609.33066) • [🤗 HF Paper](https://huggingface.co/papers/2609.33066) • **Lean 4 (`10 Theorems, 0 sorry`)** | [`pCwOrM/werr`](https://github.com/pCwOrM/werr) • [`pCwOrM/werracle`](https://github.com/pCwOrM/werracle) |
| **06** | **Paper 6: GAP-Lean4** | Machine-Checked Computational Group Theory: Schreier-Sims & BSGS Sifting (v2) | [**`10.5281/zenodo.23092708`**](https://doi.org/10.5281/zenodo.23092708) | [`10.5281/zenodo.23156544`](https://doi.org/10.5281/zenodo.23156544) | [`arXiv:2609.38492`](https://arxiv.org/abs/2609.38492) • [🤗 HF Paper](https://huggingface.co/papers/2609.38492) • **Lean 4 (`35 Theorems, 0 sorry`)** | [`pCwOrM/gap-lean4-port`](https://github.com/pCwOrM/gap-lean4-port) |
| **07** | **Paper 7: Black Hole v5** | Unitary Black Hole Page Curve via Dynamical Horizon Orbifolds & GKP Stabilizers (v5) | [**`10.5281/zenodo.22961999`**](https://doi.org/10.5281/zenodo.22961999) | [`10.5281/zenodo.23072120`](https://doi.org/10.5281/zenodo.23072120) | `S(t=1) = 0.00` · `Tr(ρ²) = 1.00` · `R² = 0.9822` · **573× Stress Quench** • **Lean 4 (`10 Theorems`)** | [`pCwOrM/fractal-neural-synthesis`](https://github.com/pCwOrM/fractal-neural-synthesis) • [`pCwOrM/werr`](https://github.com/pCwOrM/werr) |
| **08** | **Paper 8: WerrSoma** | Bio-Synthetic Neuromorphic Interfacing with 158K-Neuron *Drosophila* Connectome (v1) | [**`10.5281/zenodo.22996625`**](https://doi.org/10.5281/zenodo.22996625) | [`10.5281/zenodo.22996626`](https://doi.org/10.5281/zenodo.22996626) | `arXiv:submit/8161759` • [Live 3D Portal (`werrsoma.answerr.me`)](https://werrsoma.answerr.me/) • `TR 2026/016633` | [`Lexovian/WerrSoma`](https://github.com/Lexovian/WerrSoma) • [`pCwOrM/WerrSoma`](https://github.com/pCwOrM/WerrSoma) |
| **09** | **Paper 9: WerreduR** | Procedural Pedagogy: Resolving the Saturn School Disequilibrium Paradox (v2) | [**`10.5281/zenodo.22999420`**](https://doi.org/10.5281/zenodo.22999420) | [`10.5281/zenodo.23128224`](https://doi.org/10.5281/zenodo.23128224) | [**SSRN: 7641538**](https://papers.ssrn.com/abstract=7641538) *(Distributed)* • **Lean 4 (`7 Theorems, 0 sorry`)** • [Live Portal](https://pcworm.github.io/WerreduR/) | [`jesmaat/WerreduR`](https://github.com/jesmaat/WerreduR) • [`pCwOrM/WerreduR`](https://github.com/pCwOrM/WerreduR) |
| **10** | **Paper 10: Schönhage** | Bipartite Carrier Compression in Schönhage Trilinear Multiplication Tensors (v2) | [**`10.5281/zenodo.23232541`**](https://doi.org/10.5281/zenodo.23232541) | [`10.5281/zenodo.23295370`](https://doi.org/10.5281/zenodo.23295370) | [`arXiv:2610.14263`](https://arxiv.org/abs/2610.14263) • [🤗 HF Paper](https://huggingface.co/papers/2610.14263) • [CrocSwap #226 (`50d76881`)](https://github.com/CrocSwap/integer-mult-bounds/pull/226) | [`pCwOrM/integer-mult-bounds`](https://github.com/pCwOrM/integer-mult-bounds) |
| **11** | **Paper 11: Güneş Dili** | Deterministic Morpho-Semantic Tokenization & Algebraic Morphotactics in Lean 4 (v1) | [**`10.5281/zenodo.23003711`**](https://doi.org/10.5281/zenodo.23003711) | [`10.5281/zenodo.23003712`](https://doi.org/10.5281/zenodo.23003712) | `arXiv:submit/8248674` • **Lean 4 (`4 Theorems, 0 sorry`)** • [Live Studio](https://pcworm.github.io/gunes-dili/) | [`pCwOrM/gunes-dili`](https://github.com/pCwOrM/gunes-dili) |
| **12** | **Paper 12: Niemeier A₈³** | Machine-Certified 24D Niemeier Lattice A₈³, K3 Hodge Duality & Umbral Moonshine (v1) | [**`10.5281/zenodo.23324066`**](https://doi.org/10.5281/zenodo.23324066) | [`10.5281/zenodo.23324067`](https://doi.org/10.5281/zenodo.23324067) | **Lean 4 (`0 sorry, 0 axioms`)** • `χ(X) = 24` · `order(G_glue) = 27` · `ℓ = 9` | [`pCwOrM/niemeier-a8-umbral-moonshine`](https://github.com/pCwOrM/niemeier-a8-umbral-moonshine) |
| **13** | **Paper 13: GDT v3.0** | Machine-Certified Lean 4 Formalization of the General Divisor Theorem (v2) | [**`10.5281/zenodo.23316068`**](https://doi.org/10.5281/zenodo.23316068) | [`10.5281/zenodo.23425590`](https://doi.org/10.5281/zenodo.23425590) | **Lean 4 (`81 Theorems, 0 sorry`)** • Companion v1: [`10.5281/zenodo.23426323`](https://doi.org/10.5281/zenodo.23426323) ([`v1: 23426324`](https://doi.org/10.5281/zenodo.23426324)) | [`pCwOrM/general-divisor-theorem`](https://github.com/pCwOrM/general-divisor-theorem) |
| **14** | **Paper 14: Elliptic Sieve** | Multi-Layer Algebraic Sieve & Vélu Isogeny Engine: 230 Curves on NSF ICARM (v1) | [**`10.5281/zenodo.23436282`**](https://doi.org/10.5281/zenodo.23436282) | [`10.5281/zenodo.23436283`](https://doi.org/10.5281/zenodo.23436283) | [**NSF ICARM Leaderboard (`user/114`)**](https://elliptic-rank.icarm.cloud/user/114): **30x #1 Gold Records**, 80 Top-3, 100% `log N` | [`pCwOrM/werr-elliptic-sieve`](https://github.com/pCwOrM/werr-elliptic-sieve) |
| **15** | **Paper 15: Empirical OEV** | Empirical OEV & Liquidation Dynamics: Chainlink SVR on Base & Ethereum L1 (v2) | [**`10.5281/zenodo.23623588`**](https://doi.org/10.5281/zenodo.23623588) | [`10.5281/zenodo.23642090`](https://doi.org/10.5281/zenodo.23642090) | [🤗 HF Dataset (`1.16k+ views, 126 likes`)](https://huggingface.co/datasets/pCwOrM/werracle-oev-liquidation-dataset-2026) • 94.4% Aggregate / 98.3% Median SVR Recapture | [`pCwOrM/werracle`](https://github.com/pCwOrM/werracle) • [`pCwOrM/werrealm`](https://github.com/pCwOrM/werrealm) |
| **HW** | **Edge Robotics Core** | Zero-Memory Embedded C/C++11 System-1 Reflex Kernel (`WerrCoreEdge.h` v0.5.1) | [**`10.5281/zenodo.22867425`**](https://doi.org/10.5281/zenodo.22867425) | [`10.5281/zenodo.22939253`](https://doi.org/10.5281/zenodo.22939253) | ATmega328P / ESP32 / STM32 (`0 Bytes Heap`, `<128B Stack`, `TR 2026/016633`) | [`pCwOrM/WERRobotics`](https://github.com/pCwOrM/WERRobotics) |


---

## 🏆 Global Records, Formal Proofs, Curated Awesome Merges & On-Chain Infrastructure

### 1. Certified Mathematical Records & Formal Verification (`0 sorry`)
* **🥇 NSF ICARM Elliptic Curve Rank Leaderboard ([`elliptic-rank.icarm.cloud/user/114`](https://elliptic-rank.icarm.cloud/user/114)):** **230 certified high-rank elliptic curves** (`#4308–#4537`) over $\mathbb{Q}$ with **100% complete prime conductor factorization ($\log N$)** up to Rank $\ge 19$ (`#4323`), achieving **30 First-Place (#1 Gold) Records**, **80 Podium (Top-3)**, and **418 Top-10** placements across 43 categories (building upon the foundational fibration families of Elkies, Dujella, Rubinstein, and Klagsbrun; supported under NSF Grant `DMS-2425401`).
* **🥇 Schönhage Trilinear Multiplication Tensor Bound ([`arXiv:2610.14263`](https://arxiv.org/abs/2610.14263) • [`CrocSwap/integer-mult-bounds#226`](https://github.com/CrocSwap/integer-mult-bounds/pull/226)):** Constructive 15-round bipartite carrier matching at dimensions $h=23, 25$ eliminating 185 carrier roles and **377,890 physical wires** ($W = 177,284,805 \to 176,906,915$), certifying $\kappa = 826,215,307 / 20,000,000,000,000 \approx 4.131076535 \times 10^{-5}$ ($1.377\times$ net gain over PR #49), formally incorporated into `CrocSwap/integer-mult-bounds` (`commit 50d76881`) and verified in Lean 4 (`0 sorry`).
* **📐 170+ Machine-Checked Theorems in Lean 4 (`0 sorry`, `0 unproven axioms`):**
  * **General Divisor Theorem (`GDT v3.0`):** 81 theorems/lemmas (`0 sorry`) formalizing Dan Hawkley's residue density framework ([`10.5281/zenodo.23316068`](https://doi.org/10.5281/zenodo.23316068)).
  * **Computational Group Theory (`gap-lean4-port`):** 35 theorems (`0 sorry`) formalizing Charles Sims' Schreier-Sims stabilizer chains (`GAP-0299`), backtrack ordered partitions (`GAP-0332`), and modular ring inverses (`GAP-0331`) ([`arXiv:2609.38492`](https://arxiv.org/abs/2609.38492)).
  * **Procedural Boundary Synthesis & EVM/Cairo Fixed-Point Bounds:** 40+10 theorems (`WerracleProof.lean`, `0 sorry`) verifying `ZMod 9` ($\mathbb{Z}/9\mathbb{Z}$) principal ideal closure ($\mathcal{I}_3 = \{0,3,6\}$), Q16.16 overflow safety, and unitary Page curve S-matrix conservation ([`arXiv:2609.33066`](https://arxiv.org/abs/2609.33066)).
  * **24D Niemeier Lattice $A_8^3$, WerreduR & Güneş Dili:** Complete formal specifications (`0 sorry`) across lattice unimodularity ($\chi=24, \ell=9$), horizon complementarity ($B(t)+S(t)=1$), and deterministic morphological parsing.

### 2. Curated Ecosystem Recognitions & Benchmark Evaluations
* **Merged Upstream Pull Requests:**
  * ✅ **[`wbierbower/awesome-physics#16`](https://github.com/wbierbower/awesome-physics/pull/16):** Featured in *Quantum Physics* for unitary Black Hole Page Curve simulation.
  * ✅ **[`34j/best-of-lean4#292`](https://github.com/34j/best-of-lean4/pull/292):** Indexed in the curated *Best of Lean 4* theorem proving directory.
  * ✅ **[`yh-yao/awesome-edge-ai-agents#13`](https://github.com/yh-yao/awesome-edge-ai-agents/pull/13) & [`#16`](https://github.com/yh-yao/awesome-edge-ai-agents/pull/16):** Featured for both `werr` / `answerr` and `WerreduR` edge reflex engines.
  * ✅ **[`MartinuzziFrancesco/awesome-scientific-machine-learning#9`](https://github.com/MartinuzziFrancesco/awesome-scientific-machine-learning/pull/9) & [`#10`](https://github.com/MartinuzziFrancesco/awesome-scientific-machine-learning/pull/10):** Featured under *Model Discovery*.
  * ✅ **[`meta-introspector/lean-workers-union#2`](https://github.com/meta-introspector/lean-workers-union/pull/2):** Registered verified member (`gap-lean4-port`).
  * ✅ **Jev Ecosystem & Agentic Benchmarks:** Listed on [`awesome-jev#69`](https://github.com/hellogumbo/awesome-jev/issues/69) / `madewithjev`; **100% (49/49)** on [WindTunnel WebMCP (`3.35 ms`, `0 VRAM`)](https://github.com/nekuda-ai/WindTunnel/issues/25); **100% Tool Schema Adherence (`0.38 ms`)** on [Sierra Tau-Bench](https://github.com/sierra-research/tau-bench/issues/95); **23.74** on [JevBench v1.4.1 (`7.32 ms`)](https://github.com/fstandhartinger/jevbench/issues/10); **38.0× speedup** on [Jevenator 2](https://github.com/mmastrac/jevenator2/issues/1).

### 3. Sovereign On-Chain Deployments (`Werrium / $WERR`), Multi-Chain Testnets & Grant Pipelines
* **💎 Base L2 Mainnet (`Chain ID: 8453`) — Live & BaseScan Verified:**
  * **Werrium (`$WERR`) Token Contract:** [`0xFfa2c95b68B76af00FBD84295cBA5e5268a996d2`](https://basescan.org/address/0xFfa2c95b68B76af00FBD84295cBA5e5268a996d2) *(Fixed 1,000,000,000 supply, No-Mint, EIP-2612 Gasless Permit, `burnForATP` metabolic compute quota & `burnForReflex` on-chain decision sealing • [Optimism Superchain Token List PR #1391](https://github.com/ethereum-optimism/ethereum-optimism.github.io/pull/1391))*.
  * **Gnosis Safe 2/3 Multisig Treasury:** [`0x7CC5fd367e210F4678Bcfca054cbe0F87291E355`](https://basescan.org/address/0x7CC5fd367e210F4678Bcfca054cbe0F87291E355) (`949,501,000 WERR` locked).
  * **WerrTreasuryTimelock (Vesting & Cliff):** [`0x839A6d7E726D60EA2B587e793aE36342297e8C63`](https://basescan.org/address/0x839A6d7E726D60EA2B587e793aE36342297e8C63) (`40,000,000 WERR` locked).
  * **Aerodrome Finance DEX Liquidity Pools (Base Mainnet):** [`vAMM-WERR/USDC`](https://basescan.org/address/0xdA15b610f7De7A494CD1F7f80B6B73E8b34108A5) & [`vAMM-WERR/WETH`](https://basescan.org/address/0x53D7Ff2ef9B02860bf9F476602832f75594Bfa06).
* **🌐 Multi-Chain Testnets & Grant Tracks:**
  * **Starknet Foundation Seed Grant (*In Screening*):** Cairo 2.x / Sierra `WerracleTripodZMod9` (`single felt252` seed, `~1,420 Cairo steps`, Ekubo v2 LVR extension).
  * **Ethereum Sepolia Testnet (`Chain ID: 11155111`):** `Werrium ($WERR)` at [`0xe6ecc9575B4D52642c55FCf64E8E2d3baa6e6EF7`](https://sepolia.etherscan.io/address/0xe6ecc9575B4D52642c55FCf64E8E2d3baa6e6EF7) & `Werracle` live liquidation arbitrage telemetry.
  * **NEAR Aurora Testnet (`Chain ID: 1313161555`) & Bare-Metal EVM Node (`Chain ID: 4242`):** Live `Werracle.sol` & `WerracleFeeHook.sol` deployments ([`radar.werracle.com`](https://radar.werracle.com)).
  * **Active Research Proposals:** Flashbots MEV Research ([`FRP #205`](https://github.com/flashbots/mev-research/pull/205) & [`PR #206`](https://github.com/flashbots/mev-research/pull/206)), Morpho DAO (`MIP-81` OEV Observatory), Uniswap v4 / Unichain Hook Grants.

