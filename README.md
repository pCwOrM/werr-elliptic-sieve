# Werr Multi-Layer Algebraic Sieve & Vélu Isogeny Engine: High-Rank Elliptic Curve Records

[![NSF ICARM Leaderboard](https://img.shields.io/badge/NSF%20ICARM-Certified%20Leaderboard-blue)](https://elliptic-rank.icarm.cloud/user/114)
[![Curves Accepted](https://img.shields.io/badge/Accepted%20Curves-230%20(100%25%20Verified)-success)](https://elliptic-rank.icarm.cloud/user/114)
[![Conductor Certification](https://img.shields.io/badge/Conductor%20log%20N-100%25%20Factored%20(230%2F230)-brightgreen)](https://elliptic-rank.icarm.cloud/user/114)
[![#1 Records](https://img.shields.io/badge/%231%20Gold%20Records-30-gold)](https://elliptic-rank.icarm.cloud/user/114)
[![Top-3 Podiums](https://img.shields.io/badge/Top--3%20Podiums-80-orange)](https://elliptic-rank.icarm.cloud/user/114)
[![Top-10 Placements](https://img.shields.io/badge/Top--10%20Placements-418-blueviolet)](https://elliptic-rank.icarm.cloud/user/114)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![ORCID: Volkan Dağlı](https://img.shields.io/badge/ORCID-0009--0000--1587--8703-green)](https://orcid.org/0009-0000-1587-8703)
[![ORCID: Zerrin Dağlı](https://img.shields.io/badge/ORCID-0000--0001--9490--6425-green)](https://orcid.org/0000-0001-9490-6425)
[![ORCID: Dağhan Dağlı](https://img.shields.io/badge/ORCID-0009--0003--2492--8313-green)](https://orcid.org/0009-0003-2492-8313)

---

## 🏛️ Executive Summary & Official Public Certification

This repository houses the computational number theory research, algorithms, datasets, and reproduction tools developed by **ITouch Systems & Dağlı Family Lab** for high-rank elliptic curves over $\mathbb{Q}$.

Through a harmonized combination of:
1. **The 4-Stage Werr Multi-Layer Algebraic Sieve** (coupling algebraic root invariants $\gcd(a_4, a_6, \Delta, c_4, c_6)$, cubic divisor peeling $\Delta = d_0 \cdot s^3$, and parallel ECM/MPQS integer factorization), and
2. **Systematic Vélu $2$- and $3$-Isogeny Graph Transport** across rational torsion subgroups ($\mathbb{Z}/4\mathbb{Z} \leftrightarrow \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$, $\mathbb{Z}/4\mathbb{Z} \to \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/4\mathbb{Z}$, $\mathbb{Z}/6\mathbb{Z} \leftrightarrow \mathbb{Z}/6\mathbb{Z}$, $\mathbb{Z}/2\mathbb{Z} \leftrightarrow \mathbb{Z}/2\mathbb{Z}$),

we submitted and had **`230` distinct curves** (`#4308` through `#4537`) verified and permanently recorded on the **NSF Institute for Computer-Aided Reasoning in Mathematics ([ICARM](https://icarm.io/))** official [Elliptic Curve Rank Leaderboard](https://elliptic-rank.icarm.cloud/).

### 🏆 Key Official Achievements on `elliptic-rank.icarm.cloud`
* **Official Contributor Profile:** [Volkan Dagli (`user/114`)](https://elliptic-rank.icarm.cloud/user/114)
* **Total Accepted Top-10 Curves:** **`230` curves** (`status: created`)
* **Certified Conductor Factorizations ($\log N$):** **`230 / 230` (`100.0%`)** with zero unfactored conductors (`?`)
* **Active `(Torsion, Rank)` Leaderboards in Top 10:** **`43` distinct leaderboards**
* **Total `#1` (First Place / Gold Record) Placements:** **`30` First-Place Records**
* **Total `Top-3` (Podium) Placements:** **`80` Podiums**
* **Total `Top-10` Metric Placements:** **`418` Placements** across Conductor $N$, Discriminant $|\Delta|$, Faltings Height, and Naive Height.

---

## 🤝 Foundational Principle: First Adab, Then Knowledge (*Önce Edep, Sonra İlim*)

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

3. **Our Algorithmic Contribution:**  
   Our specific scientific contribution was two-fold:
   * **Closing the $\log N$ Gap:** Resolving all remaining composite discriminant factorizations (up to 70–105 digits) using our 4-stage algebraic sieve so that conductors $\log N$ could be certified machine-verifiably for all 230 curves.
   * **Isogeny Frontier Exploration:** Uncovering strictly smaller minimal Weierstrass models (lower $|\Delta|$, smaller Faltings and naive heights) along rational $2$- and $3$-isogeny graphs without altering the Mordell–Weil rank or conductor.

---

## 📊 Summary of #1 (Gold) Records (`30` First-Place Placements)

| Torsion Subgroup $T$ | Rank Bound | #1 (Gold Record) Metrics | Curve ID | Additional Podium Placements |
| :--- | :---: | :--- | :---: | :--- |
| **$\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ (`[2, 2]`)** | **`Rank ≥ 9`** | **🥇 `#1` Conductor ($N$)**<br> **🥇 `#1` Discriminant ($|\Delta|$)**<br> **🥇 `#1` Faltings Height**<br> **🥇 `#1` Naive Height** | [`#4315`](https://elliptic-rank.icarm.cloud/curve/4315) | *Grand Slam: 4 out of 4 #1 records!* |
| **$\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ (`[2, 2]`)** | **`Rank ≥ 8`** | **🥇 `#1` Naive Height** | [`#4314`](https://elliptic-rank.icarm.cloud/curve/4314) | 🥈 `#2` $|\Delta|$, 🥈 `#2` Faltings, 🥉 `#3` Conductor |
| **$\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ (`[2, 2]`)** | **`Rank ≥ 7`** | **🥇 `#1` Discriminant ($|\Delta|$)**<br> **🥇 `#1` Faltings Height**<br> **🥇 `#1` Naive Height** | [`#4313`](https://elliptic-rank.icarm.cloud/curve/4313) | (`#6` Conductor $N$) |
| **$\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/4\mathbb{Z}$ (`[4, 2]`)** | **`Rank ≥ 6`** | **🥇 `#1` Discriminant ($|\Delta|$)**<br> **🥇 `#1` Faltings Height**<br> **🥇 `#1` Naive Height** | [`#4320`](https://elliptic-rank.icarm.cloud/curve/4320) | (`#5` Conductor $N$) |
| **$\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/4\mathbb{Z}$ (`[4, 2]`)** | **`Rank ≥ 5`** | **🥇 `#1` Discriminant ($|\Delta|$)**<br> **🥇 `#1` Faltings Height**<br> **🥇 `#1` Naive Height** | [`#4322`](https://elliptic-rank.icarm.cloud/curve/4322) | 🥈 `#2` Conductor $N$ |
| **$\mathbb{Z}/4\mathbb{Z}$ (`[4]`)** | **`Rank ≥ 8`** | **🥇 `#1` Discriminant ($|\Delta|$)**<br> **🥇 `#1` Faltings Height**<br> **🥇 `#1` Naive Height** | [`#4319`](https://elliptic-rank.icarm.cloud/curve/4319) | 🥉 `#3` Conductor $N$ |
| **$\mathbb{Z}/4\mathbb{Z}$ (`[4]`)** | **`Rank ≥ 7`** | **🥇 `#1` Discriminant ($|\Delta|$)**<br> **🥇 `#1` Faltings Height**<br> **🥇 `#1` Naive Height** | [`#4318`](https://elliptic-rank.icarm.cloud/curve/4318) | 🥉 `#3` Conductor $N$ |
| **$\mathbb{Z}/5\mathbb{Z}$ (`[5]`)** | **`Rank ≥ 7`** | **🥇 `#1` Discriminant ($|\Delta|$)**<br> **🥇 `#1` Faltings Height**<br> **🥇 `#1` Naive Height** | [`#4321`](https://elliptic-rank.icarm.cloud/curve/4321) | 🥈 `#2` Conductor $N$ |
| **$\mathbb{Z}/5\mathbb{Z}$ (`[5]`)** | **`Rank ≥ 5`** | **🥇 `#1` Discriminant ($|\Delta|$)** | [`#4380`](https://elliptic-rank.icarm.cloud/curve/4380) | 🥈 `#2` $|\Delta|$ ([`#4381`](https://elliptic-rank.icarm.cloud/curve/4381)), 🥉 `#3` Faltings |
| **$\mathbb{Z}/2\mathbb{Z}$ (`[2]`)** | **`Rank ≥ 9`** | **🥇 `#1` Faltings Height**<br> **🥇 `#1` Naive Height** | [`#4312`](https://elliptic-rank.icarm.cloud/curve/4312) | 🥉 `#3` Discriminant $|\Delta|$ |
| **$\mathbb{Z}/2\mathbb{Z}$ (`[2]`)** | **`Rank ≥ 7`** | **🥇 `#1` Naive Height** | [`#4311`](https://elliptic-rank.icarm.cloud/curve/4311) | 🥈 `#2` $|\Delta|$, 🥈 `#2` Faltings ([`#4311`](https://elliptic-rank.icarm.cloud/curve/4311)), 🥉 `#3` $|\Delta|$ ([`#4511`](https://elliptic-rank.icarm.cloud/curve/4511)) |
| **$\mathbb{Z}/3\mathbb{Z}$ (`[3]`)** | **`Rank ≥ 8`** | **🥇 `#1` Naive Height** | [`#4317`](https://elliptic-rank.icarm.cloud/curve/4317) | 🥈 `#2` Faltings ([`#4317`](https://elliptic-rank.icarm.cloud/curve/4317)), 🥉 `#3` $|\Delta|$ ([`#4324`](https://elliptic-rank.icarm.cloud/curve/4324)) |
| **$\mathbb{Z}/3\mathbb{Z}$ (`[3]`)** | **`Rank ≥ 7`** | **🥇 `#1` Faltings Height**<br> **🥇 `#1` Naive Height** | [`#4316`](https://elliptic-rank.icarm.cloud/curve/4316) | 🥈 `#2` $|\Delta|$ ([`#4327`](https://elliptic-rank.icarm.cloud/curve/4327)), 🥈 `#2` Naive ([`#4330`](https://elliptic-rank.icarm.cloud/curve/4330)) |

---

## 🔬 Mathematical Methodology

### 1. The 4-Stage Werr Multi-Layer Algebraic Sieve
Given a global minimal Weierstrass equation:
$$E: y^2 + a_1 xy + a_3 y = x^3 + a_2 x^2 + a_4 x + a_6, \quad a_i \in \mathbb{Z}$$
with modular invariants $c_4, c_6$ and minimal discriminant $\Delta = (c_4^3 - c_6^2) / 1728$, computing the conductor $N$ requires factoring $\Delta$:
$$N = \prod_{p \mid \Delta} p^{f_p(E)}$$
where $f_p(E) \in \{1, 2\}$ for $p > 3$ by the Ogg–Sain–Tate formula. For $70$ to $105$ digit discriminants, general-purpose integer factorization is computationally intractable without algebraic structure.

Our **4-Stage Werr Sieve** resolves this via:
* **Stage 1 (Algebraic Root Invariant Divisor):** Extracting common divisor kernels:
  $$g_0 = \gcd(c_4, c_6, \Delta, a_4, a_6)$$
  which immediately pulls out massive smooth factors shared between the Weierstrass division polynomials.
* **Stage 2 (Cubic Divisor Peeling):** Because $(c_4^3 - 1728\Delta) = c_6^2$, any large prime power dividing $\Delta$ cubically can be isolated via:
  $$\Delta = d_0 \cdot s^3$$
* **Stage 3 (Parallel Pollard $p-1$ & Suyama-Montgomery ECM):** Multi-core worker cores sweep algebraic cofactor bounds $B_1 = 10^5, B_2 = 5 \times 10^6$.
* **Stage 4 (PARI/GP 2.17.2 MPQS / ECM Closure):** Remaining cofactors are verified as certified primes using APR-CL / Miller-Rabin tests.

### 2. Vélu $2$- and $3$-Isogeny Transport
For a curve $E$ with rational torsion subgroup $G \subset E(\mathbb{Q})[\ell]$ with $\ell \in \{2, 3\}$, Vélu's formulas define an explicit isogeny $\phi: E \to E' = E/G$. Under isogeny:
$$\text{Rank}(E'(\mathbb{Q})) = \text{Rank}(E(\mathbb{Q})), \qquad N(E') = N(E)$$
However, the minimal discriminant $|\Delta'|$ and Faltings height $h_F(E')$ satisfy:
$$|\Delta'| = \ell^{\pm 12 k} |\Delta|, \qquad h_F(E') = h_F(E) + \frac{1}{2} \log \deg(\phi) - \dots$$
By mapping the Mordell–Weil generators $P_1, \dots, P_r \in E(\mathbb{Q})$ to $P_i' = \phi(P_i) \in E'(\mathbb{Q})$ and re-reducing to the Cremona minimal model, we systematically discovered curves in the same isogeny class that significantly reduced both $|\Delta|$ and $h_F$, claiming new `#1` records across the board.

---

## 💻 Reproducibility & Verification

To verify all 230 accepted curves, reproduce the audit metrics, or run the Werr algebraic sieve:

```bash
# Clone the repository
git clone https://github.com/pCwOrM/werr-elliptic-sieve.git
cd werr-elliptic-sieve

# Run the complete live leaderboard placement audit
python scripts/verify_leaderboard_audit.py

# Run the standalone Werr algebraic sieve test
python scripts/werr_algebraic_sieve.py
```

---

## 👥 Authors & Affiliations

**ITouch Systems & Dağlı Family Lab**  
* Mersin & Eskişehir, Turkey  
* GitHub: [@pCwOrM](https://github.com/pCwOrM)

* **Volkan Dağlı** — Lead Researcher & Systems Architect  
  ORCID: [0009-0000-1587-8703](https://orcid.org/0009-0000-1587-8703) &bull; Email: `pcworm@pcworm.net`
* **Zerrin Dağlı** — Mathematical Modeling & Data Verification  
  ORCID: [0000-0001-9490-6425](https://orcid.org/0000-0001-9490-6425) &bull; Mersin University
* **Dağhan Dağlı** — Computational Benchmarking & Algorithmic Analysis  
  ORCID: [0009-0003-2492-8313](https://orcid.org/0009-0003-2492-8313) &bull; Toros Science College

---

## 📜 Citation

If you use this dataset, algorithms, or isogeny models in academic work, please cite:

```bibtex
@misc{dagli2026werr_elliptic_sieve,
  author       = {Da{\u{g}}l{\i}, Volkan and Da{\u{g}}l{\i}, Zerrin and Da{\u{g}}l{\i}, Da{\u{g}}han},
  title        = {{Werr Multi-Layer Algebraic Sieve & V{\'e}lu Isogeny Engine: 100% Conductor Certification and High-Rank Elliptic Curve Records}},
  year         = {2026},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/pCwOrM/werr-elliptic-sieve}},
  note         = {Certified on NSF ICARM Elliptic Curve Rank Leaderboard (Grant DMS-2425401), contributor: user/114}
}
```
