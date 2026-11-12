---
artifact_id: IW_PRF13_ROT008_FINITE_LOCAL_INSTRUMENT_DEPTH_EXPLICIT_GAP_001_20261112
created_at: 2026-11-12
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_12 / PRF13
source_type: EXACT_SOURCE_NATIVE_THREE_QUBIT_BOUNDED_MEASUREMENT_DEPTH_RECURSIVE_CERTIFICATE
exposure: PUBLIC
sync_state: LOCAL_AUTHOR_COMPLETE_GITHUB_PENDING_BW_INGEST
status: CONDITIONAL_SOURCE_TYPED_FINITE_DEPTH_POSITIVE_GAP / EXPLICIT_DOUBLE_EXPONENTIAL_WEAK_BOUND / AUTHOR_REPRODUCED / EXTERNAL_REFEREE_PENDING
claim_ceiling: NO_FULL_UNBOUNDED_ROUND_LOCC_GAP / NO_ASYMPTOTIC_LOCC_CLOSURE / NO_GLOBAL_LOCC_OPTIMUM / NO_PHYSICAL_DEVICE / NO_NOVELTY_INFERENCE / NO_CANON / NO_EXEC_SIGN
---

# PRF13 ROT008 — Explicit positive Helstrom gap for arbitrary fixed finite local-instrument depth in the original three-qubit source test

**12 November 2026. Status: self-contained conditional mathematical result, independent external referee PENDING.** This result follows the PRF13 ROT007 first-informative-measurement information-loss theorem and gives an explicit quantitative gap for **each bounded number of local instrument events on any branch**. The first party MAY re-enter; every local measurement MAY have arbitrarily many classical outcomes; the protocol MAY adapt to all public messages and keep local quantum ancillas. The number of local instrument events per transcript path, not the number of communication broadcasts or the number of measurement labels, is the resource R. All values concern only the frozen ideal R04 single-copy three-qubit endpoint and do NOT imply a positive gap for the union or closure over unbounded R.

## 0. Source map and prior-art subtraction

- Source R04: `https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R04_THREE_PROBE_FINITE_SWAP_EXACT_X_READOUT_GAP_AND_SECTOR_DECOMPOSITION_001_20261026.md`. Exact ideal equal-time endpoint states for static shared Cauchy versus independent-increment Cauchy–Lévy, κ=0, ideal instantaneous SWAP, q=γT/3>0.
- Source R06: `https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R06_EXACT_SEP_VS_LOCC_NO_GO_LOCAL_ORTHOGONALITY_RIGIDITY_001_20261026.md`. Exact finite-round local rigidity, external review PENDING; the present result does **not** borrow its LOCC no-go reasoning.
- **Critical negative knowledge R09**: `https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R09_COARSE_GRAINING_COHEN_THEOREM_AUDIT_AND_CORRECTED_CLAIM_CEILING_001_20261026.md`. Positive uniform gap for all LOCC/closure from R07 was WITHDRAWN because a fine-grained measurement constraint was invalidly applied after binary coarse-graining. ROT008 does not reuse it.
- R08 adaptive three-laboratory witness `https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R08_EXACT_ADAPTIVE_LOCC_WITNESS_AND_DELTA_UPPER_BRACKET_001_20261026.md`.
- **Load-bearing new parent** ROT007: `https://github.com/wmakiela-tech/Nash-iw-research/blob/b0ad92550ea735ca2c5d3e9215f611a68034c9da/research/prf13/2026-11-12/IW_PRF13_ROT007_FIRST_LOCAL_INSTRUMENT_QUADRATIC_HELSTROM_LOSS_001_20261112.md`. For first local POVM with S=Σα_i||r_i||², even allowing full global quantum operations afterwards, first irreversible TV loss ≥C(x)S. Source-specific exact 8D spectral algebra with author tests; external referee PENDING.
- Mature external hosts: Chitambar–Leung–Mančinska–Ozols–Winter, *Everything You Always Wanted to Know About LOCC (But Were Afraid to Ask)*, Commun. Math. Phys. 328, 303–326 (2014), DOI `10.1007/s00220-014-1953-9` (LOCC instruments, finite/unbounded-round distinctions and compactness); Kretschmann–Schlingemann–Werner, *The Information-Disturbance Tradeoff and the Continuity of Stinespring's Representation*, IEEE Trans. Inform. Theory 54, 1708–1717 (2008), DOI `10.1109/TIT.2008.917696` (standard stability host; the needed local estimate is proved explicitly here); S. M. Cohen, *Local approximation of multipartite quantum measurements*, PRA 105, 022207 (2022), DOI `10.1103/PhysRevA.105.022207` (relevant to asymptotic measurement structure, NOT transferred to binary coarse-grained decisions). **No originality/priority assertion** about the existence of a finite-depth gap, the technique, or the bound.

## 1. Frozen quantum input and precisely delimited LOCC_R

The three laboratories A/B/C hold three spatially separate qubits, no initially shared entanglement. Let x=e^(−q)∈(0,1), b=1−x²>0. The source state difference D=ρ_A−ρ_B is the exact 8×8 R04 matrix

`D[u,v] = (x^|Σ_k(u_k−v_k)|−x^Σ_k|u_k−v_k|)/8`, for u,v∈{0,1}³.

It is permutation symmetric, Tr D=0, ‖D‖₁=b and ideal unrestricted Helstrom total-variation score is H=b/2.

Define `LOCC_R` as all source-blind, possibly randomly selected **local quantum instrument trees** on the three laboratories whose maximum number of *outcome-bearing local quantum operations on any root-to-leaf path* is at most the integer R. Each local instrument may be arbitrary (general CP maps with local ancillas and arbitrary labels), may use all previous classical history, and parties may return at later nodes. A local CP map with hidden Kraus labels may be refined and publicly announced at the SAME event (this only enlarges achievable discrimination). Pure local isometries, independent local classical coins, classical feedforward and label relabelling are free and do not increase R. A nonisometric channel with a single public outcome is counted as an instrument event unless it is represented as publicly revealed finer Kraus outcomes at the same event. No quantum transmission, preshared entanglement or joint nonlocal measurement is allowed during this R-event LOCC protocol. **R counts operations/events, not standard multi-party communication rounds; three simultaneous local observations count as three local events.**

The final classical A/B guess uses the transcript and is free; without any locally measured outcome it cannot depend on the source. Write V_R(q) for the supremum of the resulting classical total variation and Δ_R=H−V_R. The proof covers finite/countable outcome alphabets without cardinality bounds, and standard measurable normal-instrument extensions when corresponding direct-integral Stinespring representations exist; the rigorously frozen core is the finite/countable Kraus case. There is NO bound on the number of outcome labels at a node or on the number of local ancillary dimensions, only on per-path instrument depth R.

## 2. ROT008.1 — exact two-event optimum (new independent source check)

Tracing out any one of the three source qubits gives, with X,Y the local Pauli observables,

`D_AB = Tr_C D = b (X⊗X + Y⊗Y)/8`.

Its spectrum is `{+b/4, -b/4, 0, 0}`, so its trace norm is b/2 and the best **joint AB** measurement cannot exceed b/4 in total variation. Any protocol using at most two local instruments in total obtains its source-relevant classical labels from at most TWO laboratories; operations on an unobserved third lab cannot alter their marginal statistics (no signalling). Its value is thus ≤b/4, even if the two local measurements are adaptive or performed in the same lab.

Local X projective measurements on any TWO laboratories attain TV=b/4: the parity statistic has `Tr[D_AB (X⊗X)]=b/2`, and declaring according to parity attains b/4. Thus

`V_0=V_1=0`, `V_2=b/4`, `Δ_2=b/4` for every x∈(0,1).

The exact symbolic proof check in the reproducer rebuilds D_AB directly from the original 8×8 characteristic-function definition and verifies its Pauli representation, two nonzero eigenvalues, and X-parity witness.

## 3. ROT008.2 — replace a first informative instrument by a *free* random local isometry

Consider any fixed first laboratory and an arbitrary **efficient, fine-refined** first local instrument K_i: C²→H_i (local output plus accessible ancilla), satisfying ΣK_i†K_i=I₂. Polar decomposition gives

`K_i = U_i sqrt(E_i)`, with `E_i=K_i†K_i=α_i(I + r_i·σ)`, `α_i>=0`, `||r_i||<=1`, `Σα_i=1`, `Σα_i r_i=0`.

Extend each U_i to an isometry on the 2D input by harmless local ancillary enlargement if E_i is rank deficient. Set `S=Σα_i||r_i||²∈[0,1]`. Define the genuine publicly flagged Stinespring isometry and a *state-independent fake-first instrument*:

`V = Σ_i |i> ⊗ U_i sqrt(E_i)`,  `W = Σ_i |i> ⊗ sqrt(α_i) U_i`.

Both are isometries. W can be implemented with an independent classical coin of probability α_i, followed by the source-independent local isometry U_i conditional on its public value. **No source-informative local quantum measurement is used**, so the remaining protocol has at most R−1 counted local instrument events. For continuous alphabets, replace sums by direct integrals and use the same norm inequality on the corresponding Stinespring operator.

For each Bloch radius t=||r_i||∈[0,1], spectral calculus gives

`(sqrt(I+r_i·σ)-I)² ⪯ t² I`,

because `(sqrt(1±t)-1)²<=t²`. Consequently

`(V−W)†(V−W)=Σ_i(sqrt(E_i)-sqrt(α_i)I)² ⪯ S I`, hence `||V−W||∞ ≤ sqrt(S)`.

Since `||D||₁=b` and V,W are isometries,

`||V D V†−W D W†||₁ <= 2 b sqrt(S)`.

Dephasing the public flag and continuing with any adaptive LOCC tree cannot increase the trace norm, so the final classical total variations satisfy

`|TV_real−TV_fake| <= b sqrt(S)`.                  (8.1)

**Caution:** this calculation compares complete flagged quantum instruments before later operations; it does NOT replace a refined LOCC measurement by its two final binary decision effects and therefore does NOT repeat the R09 coarse-graining failure. Classical source-independent randomization of the first laboratory itself may be conditioned away or bounded by convexity.

## 4. ROT008.3 — recursion from the inherited ROT007 information loss

The independent source-typed ROT007 first-measurement theorem says for the SAME initial R04 pair and the SAME local POVM effects,

`TV_real <= H−C(x)S`, where `C(x)=b c(x)` and

`c(x)=(2−x²)/[144(1+x/3)]>0` for every x∈(0,1).

The fake-instrument argument (8.1) instead gives

`TV_real <= V_{R−1}+b sqrt(S)`.

Therefore, writing `δ_R=H−V_R`, every protocol with at most R events satisfies

`δ_R >= min_{0<=S<=1} max{ C(x) S, δ_{R−1}−b sqrt(S) }`.           (8.2)

A uniform explicit bound can be propagated without knowing actual δ_{R−1}. Put normalized `r_R = d_R/b`, start with EXACT `r_2=1/4`, and for every R≥3 define

`t_{R−1} = 2 r_{R−1} / [1+sqrt(1+4c(x)r_{R−1})]`

and

`r_R = c(x) t_{R−1}²`,  `d_R = b r_R`.                             (8.3)

The t solves `c t²+t=r_{R−1}` and belongs to (0,1), since 0<r_{R−1}≤1/4. The two expressions in the max intersect there. By induction and (8.2), **for each fixed finite integer R≥2**:

`TV_LOCC_R(q) <= H−d_R(q)`, with `d_R(q)>0` for every q>0.         (8.4)

The upper performance bound does NOT rely on finite outcome cardinality and does NOT prevent a party returning to quantum operations arbitrarily often up to depth R.

A weaker completely closed formula uses `a=c/(1+c)²`. Since the positive root satisfies `t=r/(1+c t) >= r/(1+c)`, one has `r_R>=a r_{R−1}²`, and inductively

`d_R >= (b/a)*(a/4)^[2^(R−2)]`, for R>=2.                    (8.5)

This double-exponential deterioration is a LIMITATION of the proof rather than evidence that the true best LOCC protocol improves at that rate. It yields weak necessary event-depth bounds for a prescribed tiny accuracy epsilon, but not a device resource optimum.

## 5. ROT008.4 — numerical fixtures (author-reproduced, not external independent referee)

At q=1/3, `x≈0.7165313105737893`, `b≈0.4865828809674080`, `H≈0.2432914404837040`, `C≈0.00405477648697132`, `c≈0.008333167165498605`. The following are **LOWER bounds on the unavoidable total-variation gap**, not measured gaps and not values of the exact LOCC optimum:

| maximum local instrument events R | certified d_R (lower bound on H−V_R) | proof status |
|---:|---:|---|
| 0,1 | H≈0.243291440484 | exact local marginal |
| 2 | 0.121645720242 | exact 2-qubit marginal, achieved by X parity |
| 3 | 0.000252373087657 | positive recurrence from ROT007 |
| 4 | 0.000000001090776058 | positive recurrence |
| 5 | 2.037625944855×10⁻²⁰ | positive recurrence |
| 6 | 7.110533586514×10⁻⁴² | positive recurrence |
| 7 | 8.658798890397×10⁻⁸⁵ | positive recurrence |
| 8 | 1.284010496959×10⁻¹⁷⁰ | positive recurrence |

Independent constructive consistency control: inherited PRF12 R08 adaptive A→B→C three-event LOCC witness achieves `TV≈0.198464903476238`, hence its actual gap ≈0.044826537007466 exceeds the extremely weak R=3 bound above. The bound does NOT optimize all 3-event protocols.

Reproduction route: 120-decimal mpmath recursion including the stable quadratic-root formula and the closed-form floor; exact SymPy polynomial characteristic-function 8D partial trace versus 2-qubit Pauli formula; 3000 seeded independently drawn fully valid 2m-outcome qubit POVM families. Each random POVM test checks (a) the flagged Lüders versus free-coin difference ≤b sqrt S, (b) the inherited R07 global first-step gap ≥C S and (c) the operator-square-root inequality. Randomized checks are independent diagnostic fixtures, NOT a substitute for exact algebraic proofs. The author reran the code successfully on Linux x86_64, Python3/SymPy/NumPy/mpmath, fixed seed 2026111208. Full stdout and JSON fixtures are in the local research bundle and reproduced by the standalone GitHub code.

## 6. Explicit falsifiers and claim ceiling

- F1: If the actual protocol has more than R **local quantum instrument events on a branch**, this bound is inapplicable; a single communication round can include multiple local measurements. Event-depth != number of broadcast messages.
- F2: If preshared entanglement/quantum communication/joint remote gates are allowed, replacing the first local instrument need not remain within the same physical class.
- F3: If initial noisy, finite-SWAP, κ>0 or non-equal-time R04 source is used, the exact b and inherited first-step coefficient must be recalculated.
- F4: If the preceding operation is a locally irreversible channel and is NOT counted in R, the first source contract is broken; such channels must be included as instruments (or be restricted to harmless isometries). Refining hidden Kraus labels costs the SAME event and is allowed.
- F5: Replacing an informative instrument by a random isometry must retain all classical branch labels and all follow-up controls. Dropping the label would be an invalid comparison; the proof explicitly preserves it.
- F6: `d_R→0` as R→∞, so the argument **does not** exclude asymptotic Helstrom via unlimited weak local measurements. Existence of a uniform full/closure LOCC gap remains OPEN. Nor does finite-R positivity imply actual protocol optimality.
- F7: R07 parent proof of C(x) needs external independent referee; current result inherits its scope and is therefore AUTHOR-PROVED, not globally accepted. The first-step comparison (8.1) and exact V2 are independently proven within ROT008.
- F8: Finite-round LOCC compactness and instrument continuity are mature; a no-match with a source-specific formula would not imply novelty. No patent, publication priority, measurement hardware demonstration, BW owner acceptance or Living Theory canon claim.

## 7. Return and owner route

Primary source intended for public `research/prf13/2026-11-12/`, reusable as a **self-contained bounded-depth tool** with exact source state, local-instrument cost definition, proof, code and negative knowledge. Scientific referee request to AUD1 / REC11: audit the polar-decomposition/isometry extension for rank-deficient E and unbounded local output labels; audit whether any zero-message channels have been inappropriately treated as free; reproduce exact V2 and check normalization of the trace-distance bound; check that R counts LOCAL INSTRUMENTS, not ordinary rounds. Under owner-approved qualification KN/BW may ingest; PRF13 does not write BW or Living Theory directly.

**Return:** `PRF13_ROT008 / THREE_Q_EXACT_V2_B_OVER_4 / FIRST_LOCAL_INSTRUMENT_FREE_COIN_ERASURE_ERROR_B_SQRT_S / EXPLICIT_POSITIVE_FINITE_INSTRUMENT_DEPTH_GAP / HIGH_PRECISION_RECURRENCE / WEAK_DOUBLE_EXPONENTIAL_LOWER_BOUND / FIRST_PARTY_REENTRY_COVERED / R09_COARSE_GRAINING_GUARD / NO_FULL_LOCC_CLOSURE / NO_NOVELTY / REFEREE_PENDING / NO_CANON / NO_EXEC_SIGN / BW_PENDING`.
