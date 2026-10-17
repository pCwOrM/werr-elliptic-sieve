# Werr Multi-Layer Algebraic Sieve & Vélu Isogeny Engine: High-Rank Elliptic Curve Records

[![NSF ICARM Leaderboard](https://img.shields.io/badge/NSF%20ICARM-Certified%20Leaderboard-blue)](https://elliptic-rank.icarm.cloud/user/114)
[![Curves Accepted](https://img.shields.io/badge/Accepted%20Curves-230%20(100%25%20Verified)-success)](https://elliptic-rank.icarm.cloud/user/114)
# Werr Multi-Layer Algebraic Sieve & Vélu Isogeny Engine: High-Rank Elliptic Curve Records

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23436282.svg)](https://doi.org/10.5281/zenodo.23436282)
[![NSF ICARM Leaderboard](https://img.shields.io/badge/NSF%20ICARM-Certified%20Leaderboard-blue)](https://elliptic-rank.icarm.cloud/user/114)
[![Curves Accepted](https://img.shields.io/badge/Accepted%20Curves-230%20(100%25%20Verified)-success)](https://elliptic-rank.icarm.cloud/user/114)
[![Conductor Certification](https://img.shields.io/badge/Conductor%20log%20N-100%25%20Factored%20(230%2F230)-brightgreen)](https://elliptic-rank.icarm.cloud/user/114)
[![#1 Records](https://img.shields.io/badge/%231%20Gold%20Records-30-gold)](https://elliptic-rank.icarm.cloud/user/114)
[![Top-3 Podiums](https://img.shields.io/badge/Top--3%20Podiums-80-orange)](https://elliptic-rank.icarm.cloud/user/114)
[![Top-10 Placements](https://img.shields.io/badge/Top--10%20Placements-418-blueviolet)](https://elliptic-rank.icarm.cloud/user/114)
[![License: CC-BY-4.0](https://img.shields.io/badge/License-CC--BY--4.0-yellow.svg)](LICENSE)
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
  ORCID: [0009-0000-1587-8703](https://orcid.org/0009-0000-1587-8703) &bull; Email: `pcworm@pcworm.net`
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
