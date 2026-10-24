---
artifact_id: IW_PRF11_R33_NOISY_MULTISLOT_POISSON_LIMIT_AND_MEMORY_VISIBILITY_GATE_001_20261025
created_at: 2026-10-25
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
problem_id: LT4_CH7_MULTISLOT_PROCESS_MEMORY_NOISE_TERMINAL_HELSTROM_POISSON_CLASSICAL_LIMIT
exposure: PUBLIC_SAFE
canonical_body_path: research/prf11/2026-10-25/IW_PRF11_R33_NOISY_MULTISLOT_POISSON_LIMIT_AND_MEMORY_VISIBILITY_GATE_001_20261025.md
function: SOURCE_FIRST / OTHERS_FIRST / CLASSICAL_LIMIT / SHARP_ADMISSIBLE_RESOURCE / FALSIFICATION_FIRST / MATURE_HOST_SUBTRACTION
status: ANALYTIC_THEOREMS_PLUS_FINITE_MATRIX_RATIONAL_AND_POISSON_CONTROLS_PASS / INDEPENDENT_REFEREE_PENDING
bw_event_or_pending: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / NO_UNRESTRICTED_MULTISLOT_OPTIMUM / NO_DEVICE_STORAGE_LIFETIME_CLAIM / NO_NEW_OWNER_TASK
---

# PRF11 R33 — Noisy multi-slot memory: a classical Poisson Helstrom limit, sharp visibility scaling and loss of the noiseless symmetric projector

**Date:** 25 October 2026. **Class:** finite quantum-state theorem for an explicitly source-frozen synthetic family, not a device or physical-metric model. The new question is **robustness to independently specified endpoint dephasing of each probe**, not another proof of the ideal-memory R32.

## 0. Others first and scientific subtraction

1. **PRF11 R29** owns the static-once Cauchy frequency vs independent Cauchy-Lévy increments, identical all-time one-time CPTP channels, and Hahn echo; [source](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-24/IW_PRF11_R29_CONTINUOUS_SEMIGROUP_PROCESS_ECHO_AND_QUOTIENT_CONTRACT_001_20261024.md).
2. **PRF11 R30** owns the *unrestricted one-slot tester* optimum `D_1(T)=1−exp(−γT)` for a qubit with joint private quantum memory and any one CP instrument; [source](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-24/IW_PRF11_R30_FULL_ONE_SLOT_TESTER_NORM_CAUCHY_PROCESS_MEMORY_001_20261024.md).
3. **PRF11 R31** constructed equal-duration `n`-probe SWAP sampling with perfect memory: one static Cauchy phase across *all* probes vs independent intervals; `ρ_A(x,y)=2^(−n)q^||x|−|y||`, `ρ_B(x,y)=2^(−n)q^d_H(x,y)`; [source](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R31_MULTISLOT_SYMMETRY_MEMORY_PROCESS_NONMAP_001_20261025.md).
4. **REC10 ROT32** independently refereed R31 `PASS_WITH_ALL_PARAMETER_HELSTROM_EXTENSION`, proved n=4 all-q optimal symmetric final measurement and its exact one-slot advantage threshold `γT>2log(7/3)`; [source](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/rec10/2026-10-25/IW_REC10_ROT32_PRF11_FOURPROBE_SHARP_THRESHOLD_HELSTROM_REFEREE_20261025.md).
5. **PRF11 R32** proved for *perfect-memory* SWAP with all n and all q that `P_sym` is optimal against any final POVM, `D_n=2(1−S_n(q))`, and weak-noise earliest probe count `n_min∼4/(γT)`; [source](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R32_ALL_N_HELSTROM_SYMMETRY_AND_WEAK_NOISE_SAMPLE_COMPLEXITY_001_20261025.md). No independent referee of *R32* was found as of this bounded read; R31's referee is not R32's referee.
6. LT5 previously integrated R29/R30 and logic of one-time vs process into seven-chapter **WORKING** native REV021; no authorial changes are made by this report.
7. **Mature theory subtraction:** Le Cam's binomial-to-Poisson approximation (Pacific Journal of Mathematics **10** (1960), [original](https://msp.org/pjm/1960/10-4/pjm-v10-n4-p11-s.pdf)); Helstrom binary quantum hypothesis testing; qubit fidelity/Fuchs–van de Graaf and classical Poisson likelihood testing. Existing general quantum local asymptotic normality theory (Guţă and Kahn, PRA **73** 052108 (2006), [primary](https://doi.org/10.1103/PhysRevA.73.052108)) is a *neighboring host*, not a cited verbatim theorem for this Cauchy heavy-tail / rare-defect boundary experiment. **NO claim that the mathematical technique or physical effect is original.**

## 1. Exact resource and noise contract; two states for every finite n

Fix total time `T>0`, Cauchy scale `γ>0`, `a=γT`, `n≥2`, equal phase-exposure subinterval `∆=T/n`, `q_n=exp(−a/n)`; *one* phase-exposed system qubit and `n−1` initially fresh `|+>` protected probe qubits. Deterministic ideal SWAPs exchange the system and successive fresh probes. Only AFTER all phase exposures, apply to **each final probe once** an identical independent qubit dephasing CPTP channel

`D_r(ρ)=[(1+r)/2]ρ+[(1−r)/2]ZρZ`, `0≤r≤1`.

This is a **per-probe endpoint-visibility cost model**. It is NOT a waiting-time master equation or one common bath acting on all memory qubits. No environment readout, no reset of the static ξ across swaps, no postselection, no new physics. The same independent channel is applied to both hypotheses. Quantify over arbitrary joint final POVMs only; the intermediate SWAPs and input probes remain fixed. The channel's `r` may vary with n, denoted `r_n`.

Under hypothesis A, static `ξ∼Cauchy(0,γ)` sampled once per COMPLETE run; under hypothesis B, independent Cauchy-Lévy increments over the n intervals. For computational basis words `x,y∈{0,1}^n` with weights `|x|` and Hamming distance `h(x,y)`, the two exactly normalized positive density operators after endpoint dephasing are

```
ρ_A^(n,r)(x,y) = 2^(−n) [q_n]^||x|−|y|| r^h(x,y),
ρ_B^(n,r)(x,y) = 2^(−n) [q_n r]^h(x,y).                    (33.1)
```

Proof: a local `D_r` multiplies any computational off-diagonal by r; the existing R31 Cauchy characteristic factors give q to the static weight difference or to the independent Hamming distance. For `r=1` exactly the R31/R32 source model is recovered; `r=0` makes both states maximally mixed and indistinguishable.

Let `σ_(r,θ)=[I+r(cosθ X+sinθ Y)]/2` and `σ_r=[I+rX]/2`, and let `θ=ξT/n∼Cauchy(0,a/n)`. Then exactly

```
ρ_A^(n,r) = E_θ [σ_(r,θ)^(⊗n)],
ρ_B^(n,r) = σ_(r q_n)^(⊗n).                                (33.2)
```

These product-mixture identities are important: though the A state generally contains nonclassical coherences across product sectors, both hypotheses are mixtures of product states. No entanglement generation by the classical random-frequency model is claimed.

## 2. Theorem R33.1 — exact finite-n symmetry statistic, but P_sym can fail Helstrom

Let `P_sym` be the full permutation-symmetric n-qubit projector, and define

```
S_n(v)=Σ_(k=0)^n ((1+v)/2)^(n−k) ((1−v)/2)^k
      =2^(−n) Σ_(j=0)^floor(n/2) C(n+1,2j+1) v^(2j).       (33.3)
```

The power-series coefficients are positive, so S_n(v) increases for v∈[0,1]. For a single product state `σ_(r,θ)^(⊗n)`, the expectation of P_sym depends only on σ's *eigenvalues*, namely `p_±=(1±r)/2`, because `P_sym` commutes with collective unitary rotations. Thus the A mixture has the SAME projection probability S_n(r), independent of the actual θ; hypothesis B has S_n(rq). Consequently the exact binary test is

```
P_A(sym)=S_n(r),  P_B(sym)=S_n(rq),
TV_sym(n,r,q)=S_n(r)−S_n(rq) >=0.                          (33.4)
```

For r=1 this equals R32's optimal `1−S_n(q)`. For r<1, **P_sym need NOT be optimal**: A's output now has support outside the symmetric subspace and R32's Helstrom block sign argument no longer applies.

**Exact rational falsifier of a careless upgrade.** Choose n=5, q=1/2, r=4/5, and computational basis words numbered `x=0,...,31` with `bit0` the least significant bit. Put

```
v_x = 1_(|x|=3)*(1_(bit0=1)−3/5)
    − 1_(|x|=2)*(1_(bit0=1)−2/5).                           (33.5)
```

Each weight layer has zero coefficient sum, so `P_sym v=0`. Direct **Fraction** arithmetic on (33.1) gives

```
<v,v> = 24/5,
<v,(ρ_A−ρ_B)v> = 27/3125 >0,
<v/||v||,(ρ_A−ρ_B)v/||v||> = 9/5000 >0.                (33.6)
```

Therefore the difference has a *strictly positive direction outside* Sym; `P_sym` cannot be the Helstrom projector. Direct full 32×32 diagonalization independently yields `TV_sym=0.3720000000`, `TV_Helstrom≈0.3878400000`. The **strict mathematical refutation** comes from (33.6), not from a floating eigenvalue. This does not challenge perfect-memory R32 (whose r=1 hypothesis is different).

## 3. Theorem R33.2 — a uniform full-quantum indistinguishability bound

For a sequence `r_n∈[0,1)` with `n(1−r_n)→∞`, the ENTIRE terminal quantum states converge in trace distance,

```
||ρ_A^(n,r_n) − ρ_B^(n,r_n)||_1 → 0.                       (33.7)
```

Thus **not even an arbitrary joint entangled final POVM** can distinguish the hypotheses with nonvanishing advantage in this endpoint-noise model. A merely shrinking per-probe error `1−r_n→0` is NOT sufficient: it must be O(1/n), at least along any subsequence with nonzero limiting distinguishability.

**Proof with explicit finite-n upper bound, not a compactness assertion.** By convexity, `ρ_A=E_θ σ_(r,θ)^⊗n`. For two qubits with equal Bloch length r, the **squared** Uhlmann fidelity is exactly

`F(σ_(r,θ),σ_r)=1−r² sin²(θ/2)`.

Fidelity is multiplicative under tensor products, and Fuchs–van de Graaf gives

```
||σ_(r,θ)^⊗n − σ_r^⊗n||_1
 <= 2 sqrt(1−[1−r²sin²(θ/2)]^n)
 <= min(2, r sqrt(n) |θ|).                                 (33.8)
```

Here θ has a real Cauchy law with scale a/n, although only its phase enters the state. Integrate the explicit upper envelope: for `z=ra/sqrt(n)>0`,

```
||ρ_A−σ_r^⊗n||_1 <= ε_A(n,r,a)
 := (z/π) log(1+4/z²) + (4/π) arctan(z/2)
 = O_a(log n/sqrt n), **UNIFORMLY** for 0<=r<=1.          (33.9)
```

At z=0 define ε_A=0 by continuity. The evaluation is the Cauchy density integral `E[min(2,r sqrt(n)|θ|)]`; **no false finite first moment of the Cauchy law** was used.

For B, the two commuting qubit states `σ_r` and `σ_(rq)` have eigenbasis X and signed Bloch lengths r, rq. Using the elementary Hellinger/χ² inequality for two Bernoulli laws, their squared fidelity obeys

```
1−F(σ_r,σ_(rq)) <= r²(1−q)²/(1−r²), 0<=r<1.
```

Tensor fidelity and Fuchs–van de Graaf imply

```
||ρ_B−σ_r^⊗n||_1
 <= 2 r(1−q) sqrt(n/(1−r²))
 <= 2 r a/sqrt(n(1−r²)).                                  (33.10)
```

The triangle inequality combines (33.9),(33.10). Since `n(1−r_n)→∞` implies `n(1−r_n²)→∞`, BOTH terms vanish, proving (33.7). This proves a full-POVM NO-GO, not only a failure of P_sym.

**Important guard:** for `r_n=1` the denominator in (33.10) vanishes, and the theorem does NOT apply; R32's positive noiseless Helstrom limit is fully consistent. For r fixed <1 the bound gives explicit convergence; for r_n approaching 1 slower than 1/n it also gives convergence. `r_n=exp(−b/n)` falls outside the vanishing-noise hypothesis and is treated next.

## 4. Theorem R33.3 — sharp rare-flip Poisson limit of the COMPLETE Helstrom distance

Let `r_n=exp(−b/n)` for fixed `b>=0` and `a=γT>0`. Then

```
lim_(n→∞) ||ρ_A^(n,r_n)−ρ_B^(n,r_n)||_1
   = 2 TV(Pois(b/2), Pois((a+b)/2)).                       (33.11)
```

Furthermore the **separate individual X-basis measurements** of all n probes, followed by an optimal CLASSICAL decision based only on their number K of negative outcomes, attain the SAME asymptotic distance. Joint entangling readout becomes asymptotically unnecessary in this model, even though at finite n the symmetric projector need not be optimal.

**Proof.** By (33.9), uniformly in r_n,

`||ρ_A^(n,r_n)−σ_(r_n)^⊗n||_1=O_a(log n/sqrt n)→0`.

The B state is EXACTLY `σ_(r_n q_n)^⊗n`, and these two product states commute in the common X basis. The count K of X-negative outcomes has under the reference A product and under B exactly

```
K_ref,A ∼ Bin(n, p0_n), p0_n=(1−e^(−b/n))/2,
K_B     ∼ Bin(n, p1_n), p1_n=(1−e^(−(a+b)/n))/2.          (33.12)
```

Because conditional word probabilities given K are the same uniform probabilities under either hypothesis, the trace norm of the difference of commuting product states equals **twice the TV between these two binomials**. Standard Le Cam binomial-to-Poisson approximation and continuity of Poisson laws in their means give

`Bin(n,p0_n)→_TV Pois(b/2)`, `Bin(n,p1_n)→_TV Pois((a+b)/2)`.

The triangle reverse inequality shows the trace norm between actual A and B differs from the commuting-product trace norm by at most ε_A→0. The X-count measurement is optimal for the product comparison and differs on actual A by at most TV ε_A/2, proving (33.11) AND asymptotic measurement attainability. This is a standard probability approximation combined with a source-specific quantum-state trace-distance estimate. No novelty priority is asserted.

**Exact limiting classical Neyman–Pearson decision.** When b>0 the ratio of Poisson pmfs has a single crossing at

```
κ(a,b) = (a/2)/log(1+a/b).
```

Declare independent-increment B if the observed count `K>κ`; at an integer equality either assignment ties. With `m=floor(κ)+1`,

```
TV_Pois = Pr[Pois((a+b)/2)>=m]−Pr[Pois(b/2)>=m].           (33.13)
```

When b=0 take m=1, giving TV=1−exp(−a/2), so (33.11) exactly recovers the ideal R32 limiting trace norm (although its n-finite joint P_sym is a different optimal measurement). The classical Poisson host is the correct **limiting experiment** for this chosen scaling, not an assertion that all quantum memory tests reduce to Poisson or that quantum-local-asymptotic-normality papers contain this exact result.

**Three asymptotic regimes, no missing quantifier:**
- `n(1−r_n)→∞`: full quantum trace distance →0 (R33.2).
- `r_n=e^(−b/n)` with finite b: full quantum distance →(33.11)>0 (R33.3), including b=0.
- For an arbitrary sequence with bounded `n(1−r_n)` but no limit, individual subsequences `n(1−r_n)→b` inherit the corresponding Poisson formula. We do NOT assert a single limit without convergence of the noise budget.

## 5. Theorem R33.4 — exact asymptotic memory-error budget to beat an IDEAL one-slot tester

The source R30 optimum for ANY **ideal-noise-free** one-slot tester at the same total time is `D_1,ideal=1−e^(−a)`. We compare the **noisy** n-probe SWAP family with that stronger baseline; they do not have matching noise resources, which is explicitly a conservative benchmark.

Let `V_a(b)=TV(Pois(b/2),Pois((a+b)/2))`. Standard convolution by common `Pois(c/2)` shows `V_a(b+c)<V_a(b)` for c>0 because the original signed difference of the two distinct Poisson laws changes sign and the convolution has strictly positive weights on every nonnegative integer. Moreover `V_a(0)=1−e^(−a/2)` and `V_a(b)→0` by the Poisson relative entropy / Pinsker estimate as b→∞. Thus there is a UNIQUE positive critical error budget `b_crit(a)` solving

```
2 V_a(b_crit(a))=1−e^(−a).                                (33.14)
```

The asymptotic **full final-POVM** noisy SWAP advantage over ANY ideal one-slot tester exists iff `b<b_crit(a)`; equality is a tie, b>b_crit no advantage. This is NOT the threshold for actual device success: the model has ideal instantaneous SWAP and a single independent endpoint D_r per probe, not idle-time decay and gate faults.

A simple sufficient *suboptimal binary P_sym* criterion follows from (33.4): for `r_n=e^(−b/n)`, its achieved TV tends to

```
S_n(r_n)−S_n(r_n q_n)
 -> exp(−b/2) [1−exp(−a/2)].                              (33.15)
```

Hence P_sym alone beats ideal one-slot whenever

```
b < b_sym(a) := 2 log[2/(1+exp(−a/2))].                  (33.16)
```

Usually `b_sym≤b_crit`, with strict inequality when extra K thresholds improve the Poisson likelihood test. For small a, `b_sym(a)~a/2`. Numerically from the fully specified Poisson pmfs:

| a=γT | b_crit(a) full Helstrom | b_sym(a) sufficient symmetry | count cutoff at b_crit |
|---:|---:|---:|---:|
| .01 | .0049937500 | .0049937500 | 1 |
| .10 | .0493750651 | .0493750651 | 1 |
| .50 | .2344155214 | .2344155214 | 1 |
| 1.00 | .4381403928 | .4381403928 | 1 |
| 2.00 | .7597709861 | .7597709861 | 1 |
| 4 ln2 | 1.1863292719 | .9400072585 | 2 |
| 4.00 | 2.9087089213 | 1.1324383390 | 3 |

When `a=2,b=4`, the asymptotically optimal X-count threshold is `K≥3` and `TV_Pois≈0.2534863351`; the old binary symmetry test only attains `e^(−2)(1−e^(−1))≈0.0855482149`. This is an explicit asymptotic *measurement-selection* separation under imperfect memory. Finite-n P_sym failure already has the exact rational witness in §2.

## 6. Executed falsifiers and reproducible evidence

Standalone Python `reproduce_prf11_r33.py` uses NumPy/SciPy and a completely independent **Fraction** witness construction. It never imports or alters PRF11 R29–R32 code, NC files, M13 source, or any original project runtime.

1. **35/35 full quantum matrix tests** (`n=2,...,8`, five endpoint visibility/dephasing configurations) construct both `2^n×2^n` density matrices by (33.1), independently construct P_sym, confirm state PSD/normalization/commutation with P_sym, formula `S_n(r)−S_n(rq)` and trace-distance Helstrom lower bound. Maximum closed-form mismatch `3.33e−16`, maximum P_sym commutator entry `1.39e−17`.
2. **12/35 cases show nonoptimality of P_sym** with endpoint noise; n=5 q=.5 r=.8 exact `TV_sym=.372` and `TV_Helstrom≈.38784`.
3. **Independent exact Fraction witness** (33.5), ∥v∥²=24/5, v^*Δv=27/3125, normalized 9/5000>0, independent of eigensolver rounding.
4. **5 Poisson parameter pairs**, each with product-binomial finite-n comparison at n=100,1000,10000,100000, plus the analytically computed Cauchy mixing bound; exact Poisson single threshold evaluated via SciPy survival functions.
5. **7 critical-noise boundary calculations** with numerical root checks, exact P_sym sufficiency formula, one-slot comparison and endpoint monotonicity.
6. **12 fixed-r full-quantum indistinguishability upper bounds** for r=.5,.9,.99 and n=100,1000,10000,100000, all decreasing toward zero. These large-n entries are **analytic upper bounds**, not impossible 2^100000 eigendecompositions.

The independent script writes deterministic sorted JSON. The source choices are **NONBLIND**, selected after reading the previous R32 source and exploratory finite-matrix checks; no blind hypothesis-test claim. The 5-qubit witness was found via exploratory spectra and then verified using exact rational arithmetic; this provenance must remain visible. The terminal upload/re-execute manifest and GitHub readback are separate custody steps, not mathematical proofs.

## 7. STOP gates, interpretation, and return

- `PERFECT_MEMORY_R32_OPTIMAL_PSYM` != `NOISY_MEMORY_PSYM_OPTIMAL`. R33 disproves the latter at n=5, without modifying R32.
- `ENDPOINT_INDEPENDENT_D_r` != `CONTINUOUS_STORAGE_DECAY` != `GATE_NOISE` != `CORRELATED_BATH`. The 1/n visibility precision threshold is conditional on the first model only; real-memory noise budgets require a new legal source.
- `LOCAL_X_COUNT_ASYMPTOTICALLY_HELSTROM` != `LOCAL_X_COUNT_EXACT_FINITE_n_HELSTROM`. Finite-n quantum coherent readouts can be superior.
- `STOCHASTIC_PROBABILITY_REPRESENTATION` != `PHYSICAL_NONMARKOVIAN_QUANTUM_HARDWARE`. Identical one-time CPTP marginals are retained, but no quantum hardware was calibrated or tested.
- `FULL_FINAL_POVM_FOR_FIXED_SWAPS` != `ALL_MULTISLOT_COMBS_OPTIMUM`. No arbitrary adaptive intermediate testers were optimized here.
- `SOURCE_NATIVE_R33_MATH` != `NEW_MATHEMATICAL_PRIORITY`; mature Cauchy stable distributions, Le Cam approximation, Bernoulli Chernoff/Poisson threshold and quantum Helstrom/Fuchs–van de Graaf dominate the technique.
- No GR, curved York tensor, J3/K, PBH/BBN result, production DTC0a byte replay, BW ingestion, LT5 canon or Moderator EXEC follows. No owner task generated.

**Status:** `MATHEMATICAL_FINITE_AND_ASYMPTOTIC_PROOF_PASS / EXACT_FRACTION_WITNESS_PASS / NUMERICAL_MATRIX_CONTROLS_PASS / REPRO_SNAPSHOT_PENDING_UNTIL_VERIFIED / GITHUB_READBACK_PENDING_UNTIL_VERIFIED / INDEPENDENT_REFEREE_PENDING / BW_PENDING / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE`.
