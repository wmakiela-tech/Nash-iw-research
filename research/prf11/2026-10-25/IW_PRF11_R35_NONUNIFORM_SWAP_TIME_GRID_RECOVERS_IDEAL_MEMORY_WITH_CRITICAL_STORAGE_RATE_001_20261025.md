---
artifact_id: IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025
created_at: 2026-10-25
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
problem_id: LT4_CH7_R34_AGE_DEPENDENT_MEMORY_NONUNIFORM_SAMPLING_AND_EXPENDITURE_TRADEOFF
exposure: PUBLIC
canonical_body_path: research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md
sync_state: GITHUB_PENDING_BW_INGEST
status: MATHEMATICAL_PROOF_AND_36_FINITE_QUANTUM_CONTROLS_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / NO_FIXED_KAPPA_RECOVERY_CLAIM / NO_GLOBAL_MULTISLOT_OPTIMUM / NO_NEW_OWNER_TASK
function: SOURCE_FIRST / OTHERS_FIRST / POSITIVE_CONSTRUCTION / BOUNDED_FALSIFIER / MATURE_HOST_SUBTRACTION / ERROR_AS_DATA
---

# PRF11 R35 — An intentionally nonuniform SWAP time grid restores the ideal-memory discrimination limit under a critical age-dependent storage law

**Date:** 25 October 2026. **Research cell:** PRF11. **Scientific type:** a proof for a declared *synthetic time-grid and quantum storage noise model*, with independent finite-dimensional checks and a reproducible exact characteristic-function evaluation. There is no original hardware, device-noise calibration, NCDG J3/K, physical PBH or quantum-gravity interpretation.

## 0. First subtract existing science and report currentness

- **PRF11 R29** owns the underlying comparison: one static Cauchy(0,γ) frequency sampled once for a whole run versus independent Cauchy–Lévy increments, giving identical *one-time* CPTP dephasing semigroups but different multitime control responses. [Pinned public author report](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-24/IW_PRF11_R29_CONTINUOUS_SEMIGROUP_PROCESS_ECHO_AND_QUOTIENT_CONTRACT_001_20261024.md).
- **PRF11 R30** proves optimum **one active slot** `D_1^ideal(T)=1−e^(−γT)` even with an ancillary quantum memory and arbitrary one-slot joint instruments. [Source](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-24/IW_PRF11_R30_FULL_ONE_SLOT_TESTER_NORM_CAUCHY_PROCESS_MEMORY_001_20261024.md).
- **PRF11 R31/32** owns fixed *equal-duration* SWAP n-probe ideal-memory experiments. R32 proves final symmetric-space projector Helstrom-optimal for all n and obtains the exact limit `2(1−e^(−γT/2))` at fixed γT. [R31](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R31_MULTISLOT_SYMMETRY_MEMORY_PROCESS_NONMAP_001_20261025.md), [R32](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R32_ALL_N_HELSTROM_SYMMETRY_AND_WEAK_NOISE_SAMPLE_COMPLEXITY_001_20261025.md).
- **PRF11 R33** owns *common per-probe terminal visibility* `r_n` and uniform endpoint noise rare-event Poisson limit. **REC10 ROT34** independently reviewed R33 (`PASS_WITH_SHARPER_NOISE_THRESHOLD_AND_SMALLER_COUNTEREXAMPLE`), found a minimal n=4 instead of PRF's n=5 witness against the symmetric projector, and sharp Poisson decision threshold at `a_*=2.7400041976...`; this is REC10's follow-up, not R35. [R33](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R33_NOISY_MULTISLOT_POISSON_LIMIT_AND_MEMORY_VISIBILITY_GATE_001_20261025.md), [REC10](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/rec10/2026-10-25/IW_REC10_ROT34_PRF11_R33_NOISY_MEMORY_HELSTROM_THRESHOLD_REFEREE_20261025.md).
- **PRF11 R34** owns *age-dependent storage*, with `κ_n T` and visibility `r_j=e^(−κ_n(T−t_j))`, for an EQUAL-time grid; established full-POVM vanishing if `n κ_n T→∞`, and the MARKED inhomogeneous Poisson point-process limit if `n κ_nT→β`. It emphasized that time labels matter in its critical equal-time experiment. [R34](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R34_AGED_MEMORY_SHARP_VISIBILITY_POINT_PROCESS_AND_LABEL_SUFFICIENCY_001_20261025.md). **MT13 ROT040** independently discovered/repaired the labeled-versus-unlabeled Poisson nonmap (source original owner MT13 for independent mathematics). [MT13 report](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-25/mt13_rot040_prf11_age_dependent_storage_marked_poisson_memory_gate_001.md).
- In this R35 rotation PRF corrected publication-facing `exposure: PUBLIC` and `sync_state: GITHUB_PENDING_BW_INGEST` metadata in BOTH R33 and R34, after reading the SYSS5 guard instructions and exact repo preflight source. **Their scientific bodies were not changed**; exact full readbacks confirmed. Metadata corrections do not certify BW ingestion. Source commits: R33 `2c9159af27a2747ef10ecf064bea4ebd4b6d19a3`; R34 `dfa027ecd9588246bbec09cb8ebdd0a2bbb7d63f`.

**The genuinely new problem for the project:** R34 holds the sampling times `t_j=jT/n` fixed. Does the R34 loss at critical `κ_nT=β/n>0` survive if the *intermediate SWAP times themselves are legal design variables*, but total T, n memory resources, n−1 swaps, Cauchy source γ and storage law are fixed? **Answer for a particularly permissive control family: NO.** A nonuniform schedule can asymptotically make the memory age cost disappear and attain the same fixed-SWAP quantum endpoint limit as the ideal-memory experiment, with only individual X readouts. This is NOT a claim of best possible time-grid/quantum control among all resources or a priority claim in optimal experimental design.

**Mature mathematics:** elementary characteristic functions of Cauchy laws; tensor-product CPTP trace contraction; qubit state discrimination and Fuchs–van de Graaf; Le Cam (1960) [Poisson-binomial theorem](https://doi.org/10.2140/pjm.1960.10.1181), Ruzankin (2016) [Bernoulli-point-process approximation](https://www.cambridge.org/core/journals/journal-of-applied-probability/article/on-the-rate-of-poisson-process-approximation-to-a-bernoulli-process/4D3EEA9382A6C8BF556519CF62AFA120). This article's general mathematical structures are not a publication-priority novelty certificate.

## 1. Source-typed asymmetric schedule and stored-age model

Let n≥2 and choose **ANY deterministic strict partition**

```
0=t_0 < t_1 < ... < t_n=T,  Δ_j=t_j−t_(j−1)>0,
Σ_j Δ_j=T,
ξ∼Cauchy(0,γ) drawn ONCE in A, versus independent phase increments in B.
```

At each j<n, ideal instantaneous SWAP moves the already-exposed probe to a noiseless-input, but aging-storage memory location; the next exposed system qubit starts in |+>. No measurement/control of ξ. Stored probe j undergoes an independent dephasing channel `D_{r_j}` until the common final readout. The last probe needs no storage.

**Critical rate class** `κ_n T=β/n` for fixed β≥0, not constant physical κ as n grows. Let

```
d_j=Δ_j/T,
age_j=(T−t_j)/T,
r_j=exp(−β age_j/n),
q_j=exp(−a d_j),   a=γT>0.
```

The two exact n-qubit terminal states on binary words x,y are

```
ρ_A(x,y) = 2^(−n) exp[−a |Σ_j d_j (x_j−y_j)|] × ∏_{j:x_j≠y_j}r_j,
ρ_B(x,y) = 2^(−n) exp[−a Σ_j d_j|x_j−y_j|] × ∏_{j:x_j≠y_j}r_j.     (35.1)
```

Both are valid density matrices, because source integration and local dephasing are CPTP. When all d_j=1/n, (35.1) is exactly PRF R34. With nonuniform d_j, the A state is generally NOT permutation-symmetric, even at perfect storage, so R32's P_sym proof CANNOT be transplanted.

Define the normalized quadratic mesh and mean stored age:

```
E_n=Σ_j d_j²,
A_n=(1/n) Σ_j age_j,
Λ_n=Σ_j(1−r_j)≤β A_n.                              (35.2)
```

The contraction/loss bound Λ_n is deterministic; no Gaussian OU/noise model has been silently assumed. Every individual storage channel is identical between A and B. We optimize ONLY final readout after a PRECOMMITTED schedule. The physical rate `κ_n` tends to zero like 1/n; R35 does NOT contradict R34's non-recovery result for fixed κ>0.

## 2. Theorem R35.1 — schedule-dependent quantum trace bound and sufficient ideal-limit conditions

**Theorem.** Let `a>0` be fixed; for each n choose any positive partition as above and a common `β≥0`. If

```
E_n→0,   A_n→0,                                            (35.3)
```

then the complete terminal distinguishability, optimized over **ALL quantum final POVMs** but NOT other SWAP/control schemes, has the exact limit

```
lim_n ||ρ_A^(n)−ρ_B^(n)||_1 = 2(1−e^(−a/2)).                (35.4)
```

Furthermore a *non-entangled, locally measurable* binary statistic — measure every probe in the X basis and ask whether there is ANY `−` outcome — asymptotically attains the SAME limit:

```
lim_n TV_(K≥1 outcomes)=1−e^(−a/2).                         (35.5)
```

Therefore retaining time labels and quantum-coherent collective terminal POVMs is asymptotically unnecessary **FOR THIS engineered schedule and rate class**. The result does not imply that age labels were unnecessary in R34's *equal-time* critical point-process model.

### Proof: reduce static Cauchy to a nearly pure product uniformly in the unobserved phase

First remove storage noise. Put `H_n=|+><+|^(⊗n)`. Under A the pure conditional state for a fixed ξ is

```
|Ψ_ξ>=⊗_j (|0>+e^(i ξΔ_j)|1>)/√2.
```

Its squared overlap with the reference is `|<+^n|Ψ_ξ>|²=∏_j cos²(ξΔ_j/2)`. Since `1−∏(1−u_j)≤Σu_j`, `sin²(x)≤x²`, and two pure states have trace distance `2 sqrt(1−|<.|.>|²)`, we obtain pointwise

```
|| |Ψ_ξ><Ψ_ξ|−H_n ||_1 ≤min(2, |ξ| sqrt(Σ_jΔ_j²)).        (35.6)
```

By convexity this bounds the mixture under ξ. For `ξ/γ` standard Cauchy and `z=a sqrt(E_n)` integration of its **truncated** absolute moment gives the EXACT conservative bound

```
||ρ_A^ideal−H_n||_1 ≤ε(z)
  := (z/π) log(1+4/z²)+(4/π) arctan(z/2)
  =O(z log(1/z))→0   when E_n→0.                         (35.7)
```

No undefined `E|ξ|` has been used. This extends the R34 equal-time bound `z=a/sqrt(n)` to an arbitrary mesh. For fixed a, n→∞ with E_n→0, even the heavy-tailed correlated A is asymptotically INDIFFERENT at this final static-noise-free reference, not equal at finite n.

Under B without storage noise, the output is the product of commuting X-diagonal states

```
ρ_B^ideal=⊗_j (I+q_j X)/2.
```

Define `P_n=tr(H_n ρ_B^ideal)=∏_j (1+e^(−a d_j))/2`. Exactly

```
P_n=e^(−a/2) ∏_j cosh(a d_j/2).
```

Using `0≤log cosh u≤u²/2` and `Σ d_j=1`:

```
e^(−a/2) ≤P_n≤e^(−a/2)exp(a² E_n/8).               (35.8)
```

Because H_n is one of the commuting product eigenprojections of `ρ_B^ideal`, the trace norm is EXACTLY

```
||H_n−ρ_B^ideal||_1=2(1−P_n).
```

Consequently the noiseless two-state distance differs from `2(1−P_n)` by ≤ε(z), by reverse triangle inequality, hence approaches `2(1−e^(−a/2))` for **any** sufficiently fine time grid. This last fact is an asymptotic statement for the fixed SWAP protocol, not a universal n-slot process norm.

### Proof: age noise costs at most total bit-flip-channel probability

Each local dephaser is a convex mixture of identity (probability `(1+r_j)/2`) and conjugation by Z. Their tensor product channel Λ has identity-error component with probability `p0=∏_j (1+r_j)/2`. On EVERY state R, trace norm contraction and convexity give

```
||Λ(R)−R||_1≤2(1−p0)≤Σ_j(1−r_j)=Λ_n≤β A_n.         (35.9)
```

The actual outputs are `ρ_A=Λ(ρ_A^ideal)` and `ρ_B=Λ(ρ_B^ideal)`. Contractivity and applying (35.9) twice yield the quantitative sandwich

```
2(1−P_n)−ε(z)−2β A_n
  ≤||ρ_A−ρ_B||_1
  ≤2(1−P_n)+ε(z).                                       (35.10)
```

Both bounds converge to `2(1−e^(−a/2))` under (35.3). This proves (35.4) for ALL final POVMs by the Helstrom theorem.

### Proof: a local X-bit OR test already attains the limit

Let `K` count the number of negative X outcomes on the individual probes. Under the noise-free reference H_n, `K=0` surely. Under A with memory loss, (35.7)+(35.9) imply

```
P_A(K=0)≥1−[ε(z)+β A_n]/2→1.
```

Under B, direct independence gives

```
P_B(K=0)=∏_j (1+r_j q_j)/2
 =e^(−(a+βA_n)/2)∏_j cosh[(a d_j+β age_j/n)/2].  (35.11)
```

Since `A_n→0`, `max_j d_j≤sqrt(E_n)→0` and `max_j β age_j/n≤β/n`, the logarithmic product's quadratic remainder vanishes: `Σ_j(a d_j+βage_j/n)²→0`. Hence `P_B(K=0)→e^(−a/2)` and the two-outcome TV approaches `1−e^(−a/2)`. By the full-quantum upper bound no final POVM can asymptotically do better. QED.

**Converse limitation:** (35.3) is SUFFICIENT, not claimed necessary for all possible time grids or all different noise allocations. Its failure does NOT by itself prove a full-POVM no-go.

## 3. Constructive R35.2 — two-tier time grid with identical n and β budgets

For each n≥16, choose `m_n=ceil(sqrt(n))`, `δ_n=n^(−1/2)` and

```
t_j/T=(1−δ_n)j/m_n,                           j=0,...,m_n,
t_(m_n+ℓ)/T=(1−δ_n)+δ_n ℓ/(n−m_n),          ℓ=1,...,n−m_n.  (35.12)
```

Thus *m* probes span the first `1−δ` fraction of the experiment; the remaining `n−m` probes span the terminal `δ` fraction. The exact partition is positive, has n total exposures and n−1 deterministic SWAPs. Different intervals (not different xi samples) are exposed to the SAME ξ under A.

For this grid,

```
E_n=(1−δ_n)²/m_n + δ_n²/(n−m_n) =Θ(n^(−1/2)),
A_n= (1/n)[m_n−(1−δ_n)(m_n+1)/2
            + δ_n(n−m_n−1)/2] =Θ(n^(−1/2)).                (35.13)
```

Hence both premises of R35.1 hold. The source Cauchy mixing error is conservatively `O(n^(−1/4)log n)`, and aggregate storage noise error is `O(β n^(−1/2))`; no rate sharper than this conservative proof bound is asserted for the quantum trace itself.

**Age budgeting matters:** with the original equally spaced `t_j=jT/n`, `A_n=(n−1)/(2n)→1/2`, so critical `β/n` storage produces order-one aggregate background flips and the MARKED Poisson model of PRF R34/MT13. Under the two-tier schedule, `A_n→0`, so the background flip mass disappears; meanwhile exposure source contributions still sum to `a` because `Σ Δ_j=T`. The deliberately later concentration of *sample counts* need not concentrate the *physical time* of the underlying source — early time is covered by fewer but still increasingly fine exposures.

**Honest resource cost:** the smallest terminal interval here is `Θ(T n^(−3/2))`; the maximum required ideal instantaneous SWAP cadence increases as `Θ(n^(3/2)/T)`, FASTER than the `Θ(n/T)` uniform-rate clock. This study does not price this scheduling resource or include operation duration/error; the advantage cannot be claimed for a device with fixed maximum pulse rate. Indeed imposing `Δ_j≥cT/n` for fixed c>0 gives age_j≥c(n−j)/n and `A_n≥c(n−1)/(2n)`, so the R35 construction's sufficient vanishing-age property is impossible under such a rate floor (not a universal no-go for every other conceivable quantum strategy).

For **fixed κ>0**, as n grows `nκ T→∞`; R34's fixed-uniform grid no-go and this result are logically disjoint. This R35 does NOT claim recovery at fixed κ or physical improvement just by doing more SWAPs.

## 4. Exact finite-n non-oscillatory Fourier witness and independent numerical checks

For a two-tier grid there are only TWO distinct exposure lengths `d_e,d_l` (in units of T). Under A, the probability of seeing all positive results in the *local* X measurement is

```
P_A(K=0)=E_ξ ∏_j [1+r_j cos(ξ Δ_j)]/2.                 (35.14)
```

The identity

```
(1+r cos θ)/2 = (r/4)e^(−iθ) + (1/2) + (r/4)e^(+iθ)       (35.15)
```

has NONNEGATIVE coefficients. Convolving each interval's three-term coefficient array inside the early group and late group gives arrays `C_e(k), C_l(ℓ)` for integer signed lazy walks `k∈[−m,m]`, `ℓ∈[−(n−m),n−m]`. The exact Cauchy characteristic function then yields the strictly nonnegative finite formula

```
P_A(K=0)=Σ_{k,ℓ} C_e(k) C_l(ℓ) exp[−a|k d_e+ℓ d_l|].   (35.16)
```

No random-ξ simulation, oscillatory integral approximation, or size-2^n density matrix is involved in computing this scalar. The B probability is the closed product (35.11). Formula (35.16) is EXACT as an identity. Its numerical evaluation uses positive IEEE-double arithmetic, without destructive cancellation; **it is not a certified interval enclosure**. The strict asymptotic theorem above does not rely on finite-n floating-point evidence.

At `a=1, β=2` the executable independent controls give the following **actually recalculated, characteristic-function-based** finite cases:

| probes n | uniform local-X OR TV | R35 two-tier local-X OR TV | R35 mean age A_n |
|---:|---:|---:|---:|
| 64 | 0.198274751 | 0.206736631 | 0.117188 |
| 256 | 0.217900690 | 0.254086812 | 0.060547 |
| 1024 | 0.228121478 | 0.292569076 | 0.030762 |
| 4096 | 0.233345955 | **0.321584623** | 0.015503 |

For comparison the BEST **IDEAL** one-slot tester of PRF11 R30 at `a=1` has TV exactly `(1−e^(−1))/2≈0.3160602794143`. The R35 nonuniform **explicit four-thousand-ninety-six-probe OR tester** gives TV≈0.321584623, a numerical gap ≈0.00552434. This is not an optimized arbitrary multi-slot tester; it is a positive witness and a nonblind selected schedule. The schedule is fixed by n, not numerically optimized to this a,beta fixture.

Additional direct 36 full quantum dense-matrix controls: n=4,...,9 (six sizes) × both grid types × (a,beta)=(.25,1),(1,2),(2,.3). They construct every entry of the actual ρ_A,ρ_B via the unequal-exposure Fourier factors in (35.1), check Hermiticity/PSD/trace-one, check complete eigenvalue trace norm dominates exact local X-OR TV, and check (35.11) against direct |+> product matrix expectation. All PASS. **No dense-matrix calculation for n=4096 is claimed.**

An independent Gauss–Legendre/ Cauchy-tangent integration implementation was also attempted. It showed quadrature-dependent fluctuations as large as around 5×10^−5 even at 3072 points, caused by oscillatory far tails; its output was therefore **REJECTED as the primary finite-n source** and retained only as a secondary diagnostic. Main results were recomputed by (35.16). This correction preserves negative numerical knowledge: matching a few quadrature nodes does not certify a heavy-tailed oscillatory integral.

The code reports an n4096 rare-event control `Σ p_j²→small`, `Σ p_j→a/2`, and storage background `β A_n/2→0`. By classical Le Cam/Poisson approximation, the source-induced X clicks tend to `Pois(a/2)` and there is no asymptotic background click under A; thus a mere zero/nonzero count decision is sufficient for the limiting two-hypothesis experiment. A full point-process statement on **continuous marks** would require within-cell jitter or another common measurable embedding; we do NOT conflate discrete grid points with continuous locations in total-variation topology (the explicit MT13 ROT040 warning).

## 5. Negative controls, source-language and claims gate

- **R35 construction does NOT refute R34:** R34 fixes equal time steps (and analyzes age-dependent storage); R35 changes that source carrier's timing schedule while maintaining total T and n. It can alter the statistical experiment even when no physical memory law changes.
- **Critical storage law only:** `κ_nT=β/n` for a β held fixed, so as the number of probes grows the apparatus parameters improve. No hardware statement that an actual fixed apparatus enjoys κ_n→0.
- **Clock constraint matters:** instantaneous SWAP frequency rises superlinearly; timing constraints, jitter, calibration and pulse errors are UNMODELED. A physical optimum could reverse.
- **One-slot benchmark is the IDEAL optimal one-slot value**, deliberately challenging; the multi-slot R35 tester pays its explicit endpoint-storage noise but NOT other operations' cost.
- **Labels are context-dependent:** important in R34 *uniform* critical experiment, asymptotically unnecessary when the R35 design drives baseline background to zero. No claim that complete input-output process histories are generally compressible to one bit.
- **No new physics, no NASH K/J3, no claim R35 is novel relative to all classical experimental-design literature, no unrestricted process comb norm, no BW ingestion, no change to LT5's working native monograph and no owner/EXEC elevation.** Independent referee still required for these theorem extensions.

**Return status:** `ANALYTIC_THEOREM_SOURCE_TYPED_PASS / INDEPENDENT_36_FINITE_QUANTUM_CONTROLS_PASS / POSITIVE_FOURIER_NUMERIC_PASS / CLEAN_REPRODUCTION_PENDING_UNTIL_VERIFIED / PUBLIC_GITHUB_READBACK_PENDING_UNTIL_VERIFIED / INDEPENDENT_REFEREE_PENDING / GITHUB_PENDING_BW_INGEST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / NO_NEW_OWNER_TASK`.
