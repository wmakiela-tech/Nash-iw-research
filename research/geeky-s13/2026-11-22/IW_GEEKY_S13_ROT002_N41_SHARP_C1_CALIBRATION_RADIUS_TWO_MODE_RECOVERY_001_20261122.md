---
artifact_id: IW_GEEKY_S13_ROT002_N41_SHARP_C1_CALIBRATION_RADIUS_TWO_MODE_RECOVERY_001_20261122
return_id: IW_GEEKY_S13_ROT002_N41_FULLFIELD_SHARP_LIPSCHITZ_CRITICAL_ALIAS_AND_TWO_MODE_GAUSSIAN_TEST_001_20261122
origin_cell: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-22 Europe/Warsaw
source_scope: ORIGINAL_M13_PUBLIC_AUXILIARY_N41_GRID_PLUS_GEEKY_S12_ROT035_TWO_EXACT_RATIONAL_SYNTHETIC_GAUSSIAN_COVARIANCES
science_class: FINITE_FOURIER_LIPSCHITZ_BUDGET_SHARP_SOURCE_SPECIFIC_IDENTIFIABILITY_THREE_PHASES
status: AUTHOR_ANALYTIC_PROOF_PLUS_NEW_INDEPENDENT_75DIGIT_OUTWARD_INTERVAL_ENUMERATION_AND_85DIGIT_TEST / EXTERNAL_DIFFERENT_CELL_I1_PENDING
source_execution: ORIGINAL_M13_HELPER_READ_FROM_PUBLIC_GITHUB_PRIOR_TURN_BUT_NOT_EXECUTED_IN_ROT002
claim_ceiling: NO_GENERAL_MATHEMATICS_NOVELTY / NO_PHYSICAL_SOURCE_MEASUREMENTS / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE / BW_PENDING
---

# Geeky-S13 ROT002 — sharp C¹ axial spectral log-calibration derivative budget for full N41 Gaussian-law identifiability, with a mean-free two-mode finite-sample witness

## 0. Scientific question, exact priority and result

Geeky-S13 ROT001 FIRST showed an exact full-`41^3` Gaussian-law alias between two **fixed synthetic stationary Gaussian measurement-noise models A/B** from Geeky-S12 ROT035 if each source hypothesis may independently fit an arbitrarily oscillatory but smooth `C^infinity` axial-only log spectral calibration `phi_X(a)` with **no quantitative derivative limit**. Source M13 originally supplied the auxiliary sparse Fourier tensor and five spatial cube masks; **neither the Gaussian site-noise laws nor the full-site readout is native M13 physical instrumentation**. The full historical original `dtc0a_runtime_v0_3_1.py` remains unavailable.

New question: What is the **exact least first-derivative budget** at which the unrestricted axial alias reappears, when `phi_A,phi_B ∈ C^infinity(R)` and **each** obeys `||phi_X'||_infty ≤ L`? Does the entire site field have to be measured to regain discrimination below threshold?

**SOURCE-CONDITIONAL ANSWER:** On the original prime-41 Fourier grid and exact Geeky ROT035 A/B covariance parameters,

`L_* = 347.3569067741559430318885300664434734215713818651680044317137294...`

is SHARP. For `0 ≤ L < L_*`, there is a definite positive gap between two mean-free Fourier mode-variance ratios; source A/B Gaussian composite models are disjoint, and a uniform finite-N statistical test exists. For `L = L_*` **as well as** `L > L_*`, there exist **genuine globally C-infinity** calibrations, each individually meeting the first-derivative cap `L`, making **all 68,921 Gaussian spatial measurements identically distributed**; every sample size is then powerless for those admissible aliases. Distinct source covariance hypotheses remain distinct *before* nuisance fitting. The alias is a statement about composite models, not physical measurement error.

This is a finite-node specialization of mature Lipschitz extension theory and elementary Gaussian likelihood statistics, **not general mathematics novelty**. All numerical constants here depend on original source geometry and the exact fixed rational pair. It is NOT a new global NASH K/J3/TPE/GR/GW physical theorem, nor an owner-approved measurement proposal.

Owner/citation provenance:
- Original M13 source helper, Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`, unchanged and read earlier but **not executed in ROT002**: https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py
- Geeky-S12 ROT035 **FIRST** synthetic rational A/B covariance witnesses: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s12/2026-11-17/IW_GEEKY_S12_ROT035_EXACT_RATIONAL_M13_SIX_MASK_COVARIANCE_KL_INDISTINGUISHABILITY_AND_SITE_AGGREGATION_INFORMATION_LOSS_001_20261117.md
- Geeky-S13 ROT001 FIRST full-field `C^infinity` unbounded axial alias; immutable Git blob `1f24ee58c520c7f234e961cb9a38acc2713409b1`: https://github.com/wmakiela-tech/Nash-iw-research/blob/ae8103f65df0e932f064c51889e2df2f36b2cdec/research/geeky-s13/2026-11-22/IW_GEEKY_S13_ROT001_N41_FULLFIELD_CINFTY_AXIAL_CALIBRATION_ALIAS_001_20261122.md
- M15 ROT035 FIRST **five-mode bounded C4** source threshold; ROT036 FIRST **six-mode cubic+face bounded C4** Peano threshold; ROT037 FIRST **six-mode C5** enhancement; AUD3 ROT009 independent improvement for that C5 contract. These are **different derivatives, different nuisance classes and different source tasks**. None is reidentified as ROT002 firstness. M15 ROT037: https://github.com/wmakiela-tech/Nash-iw-research/blob/b25b591b94231adbcfd2df2e7ac614a733b4786c/research/m15/2026-11-22/IW_M15_ROT037_ORIGINAL_M13_C5_FIFTH_DERIVATIVE_REGULARITY_RESTORES_UNIFORM_GAUSSIAN_SHAPE_SEPARATION_IV110_001_20261122.md

## 1. Exactly scoped source model

On `G=(Z/41Z)^3`, set for `c_j(k)=cos(2π k_j/41)`:

`a(k)=(c_x+c_y+c_z)/3`, `f(k)=(c_x c_y+c_x c_z+c_y c_z)/3`, `h(k)=c_x c_y c_z`.

The original Geeky ROT035 Gaussian *hypothetical* stationary full-site error spectra are

`v_X(k)= beta0_X [1 + theta_axial_X a(k) + theta_face_X f(k) + theta_body_X h(k)]`,

with the EXACT source rationals:

```text
A: beta0=1; theta=(3/25, 1/10, 2/25).
B: beta0=99779719687217/100000000000000;
   theta=(316869474178226/2494492992180425,
          93110637627687/997797196872170,
          205860943554709/2494492992180425).
```

All are strictly SPD since each beta0>0 and each positive theta sum<1. Candidate X has independently fitted 

`V_X(k;phi_X)=v_X(k)*exp(phi_X(a(k)))`,

with `phi_X ∈ C^infinity(R)`, `||phi_X'||_infinity ≤ L`. Lower derivative/absolute function values and the common constant gain are otherwise free; the calibration is NOT forced to be the same for A and B, and its induced source spatial covariance can be NONLOCAL. Both candidates share the SAME stipulated original M13 deterministic B-energy mean field; there is no actual source/site sensor data.

ROT001 source prime-cyclotomic lemma shows each of the `C(23,3)=1771` unsigned unordered triples of wave numbers `0..20` has a distinct exact real `a` value. Their signed/ordered multiplicities sum to `41^3=68,921`, and each orbit has a single base source ratio `v_A/v_B`.

Write the strictly increasing exact axial nodes `a_0<...<a_1770` and the required relative calibration values

`d_i= log(v_A(k_i)/v_B(k_i))`.

Full Gaussian covariance equality requires and is equivalent to

`psi(a_i)=d_i` for every `i`, with `psi=phi_B−phi_A`.

## 2. Exact sharp full-field derivative boundary

Define the finite-data maximal secant constant

`K_* = max_{0<=i<1770} |d_(i+1)−d_i|/(a_(i+1)−a_i)`.

**Why adjacent pairs suffice:** a nonadjacent secant is a convex combination (weights = positive axial gaps) of the consecutive secants, hence its absolute value cannot exceed the maximum absolute adjacent secant.

**Necessity:** if `V_A≡V_B` then `psi(a_i)=d_i`; by the derivative caps, `||psi'||_infty≤2L`. The mean-value inequality gives `|d_(i+1)−d_i| ≤ 2L(a_(i+1)−a_i)`. Thus `2L≥K_*`; in particular if `L<K_*/2`, no equality of the complete Gaussian laws can occur.

**Sufficiency for L>K_*/2:** all prescribed data secants of `d` are strictly below `2L`. One can construct a globally smooth derivative `g=psi'` with `|g|<2L` whose integral on each adjacent interval equals `d_(i+1)−d_i`, and with `g=0` outside the node range. For every interval choose smooth nonnegative endpoint and middle partition functions, with endpoint supports arbitrarily thin, and fit an interior constant so the integral is exact. Every prescribed average lies strictly inside the cap. Integrate `g` with initial value `d_0` to get globally smooth `psi`; set `phi_A=−psi/2`, `phi_B=psi/2`. Their derivatives obey the individual cap and they match all `d_i`, hence all `V_A=V_B` exactly.

**Critical equality `L=K_*/2` — material stronger result:** there is EXACTLY ONE adjacent interval `i*=390` whose source secant saturates `|s_i|=K_*`, and its signed slope is **positive**. Set `g=K_*` identically on the complete critical interval. At its two endpoints prescribe `g=K_*`; at every other node prescribe `g=0` (except the already specified critical endpoints). On each remaining interval the required average `s_i` satisfies **strict** `|s_i|<K_*`. Hence choose a `C^infinity` partition of unity (endpoint/endpoint/middle) with tiny endpoint support and an interior constant `q_i∈(−K_*,K_*)` adjusted exactly to produce the average `s_i`. Every transition stays within `[−K_*,K_*]` as a convex combination of admissible values; each `g` is constant near endpoints, so all gluing jets match to every order. Set `g=0` outside the outermost nodes and integrate. This yields a GLOBAL `C^infinity` function `psi` with `||psi'||_infty = K_*` **and** `psi(a_i)=d_i` exactly. Set `phi_A=−psi/2` and `phi_B=psi/2`, each bounded by `K_*/2=L_*`, proving an **EXACT full 68,921-dimensional Gaussian-law alias AT the threshold**, not only an approximating sequence. Because the critical interval is unique there is no incompatible adjacent saturated interval forcing contradictory derivatives at a shared node.

**Important:** this exact-at-critical result is DIFFERENT from M15 ROT036's nonattained Peano critical `C4` bound. The classes and constraints are not interchangeable.

## 3. Original-source numerical proof certificate: all 1770 adjacent intervals

A fresh standalone source program reads only the exact rational A/B coefficients from the pinned source lineage (embedded and named in the program), not the original M13 tensor runtime. It generates all 1771 sorted frequency triples and uses:
- independently computed 85-digit `mpmath` values for axial nodes and log source ratios;
- a separate 75-decimal **outward-rounded** `mpmath.iv` evaluation of ALL cosine eigenvalues, all 1771 node values, all log ratios, all 1770 consecutive source secants;
- rigorous interval-positive ordering for **all 1770 consecutive node gaps**;
- strict interval separation of one unique winner from all alternatives, with winner lower bound minus second candidate upper bound **greater than 313**.

Certified source winner (zero-based adjacent index 390):

`(u_x,u_y,u_z)=(1,19,19)` followed immediately by `(7,15,16)` in sorted axial order.

```text
Δa          = 0.0000051208333213993...;
Δd          = 0.00355751364525457...;
K_* = Δd/Δa = 694.7138135483118860637770601328869468431427637...;
L_* = K_*/2 = 347.3569067741559430318885300664434734215713819... .
```

Strict 75-digit directed-interval enclosure:

`L_*∈[347.35690677415594303188853006644347342157138186516800443171372941996368597342045, 347.35690677415594303188853006644347342157138186516800443171372941996377072085161]`.

Second largest, still far below winner: consecutive `(2,15,19)` → `(5,13,20)`, absolute slope `381.253004097354482...`.

The original source B-energy Fourier differences lie within signed coordinate bounds `[-6,6]×[-4,4]×[-2,2]` as reported by M15 native-source work; the above winning representatives each have components outside that support, hence they are also **hypothetical original-energy-mean-free** Fourier cos/sin readouts for every alpha. This support statement is taken from verified upstream source results, **not independently reexecuted original M13 tensor calculations in ROT002**.

Caution on implementation: the initial strict control used binary64 conversions of the extremely narrow 75-digit interval endpoints and therefore **FAILED**, because both endpoints rounded to the same double. That false failure was diagnosed and repaired by using a high-precision point versus interval containment test. The corrected full program was rerun; only the corrected pass is counted. No source change or evidence deletion was hidden.

## 4. Constructive TWO-mode finite-sample discrimination, well below threshold

One need not actually observe all 68,921 modes to distinguish these two fixed base hypotheses under known *per-model* derivative bound L. Choose the two original-energy-mean-free Fourier pair projectors from the unique winner above, e.g. `k_low=(1,19,19)` and `k_high=(7,15,16)`, each cosine and sine. Their expected means are zero for original M13 source energy in this declared idealized model. Stationary centered Gaussian noise makes the two different Fourier pairs independent under each fixed calibration.

For each candidate X the **unknown actual** pair-variance logarithmic contrast has center `r_X=log(v_X(k_high)/v_X(k_low))` and unknown perturbation within `[−L Δa,+L Δa]`. The two center contrasts differ by `−Δd` exactly. Therefore the two possible contrast intervals have a strict separation

`gap(L)=Δd−2L Δa`, positive iff `L<L_*`.

For `n` independent hypothetical **complete RAW-site** Gaussian snapshots (or two direct orthogonal mode-pair measurements), define `S_i` as the sum of the squares of the normalized cosine and sine projections over all `n` snapshots; conditionally `S_i/V_X(k_i)∼χ²_(2n)`. Compute

`T_n = log(S_high/S_low)`.

The common chi-square normalization cancels. A fixed classifier chooses between A and B based on which SIDE of `(r_A+r_B)/2` the observed `T_n` falls; the decision does NOT use the fitted functions `phi_A,phi_B` or their constant gains. On the event for BOTH independent pairs that their normalized `χ²_(2n)/(2n)` lie within `[1−δ,1+δ]`, the noise contribution to `T_n` is no greater than

`log((1+δ)/(1−δ))`.

Thus a sufficient source condition for guaranteed correct classification on that event is

`gap(L)/2 > log((1+δ)/(1−δ))`.

Each one of the four chi-square tails is bounded by `exp[−nδ²/4]` for `0<δ<1` by standard Chernoff inequalities. Consequently, for each candidate X, the misclassification probability is bounded above by

`4 exp[−n δ²/4]`.

**Executed interval-certified example:** Choose known hypothetical derivative cap `L=100`, `δ=1/1600`, `n=45,000,000` IID complete source snapshots. The strict source uncertainty-adjusted log decision margin is

`Δd/2 −100Δa − log((1+1/1600)/(1−1/1600)) = 0.0000166733277269015101... >0`, 

and the analytical per-hypothesis error guarantee is **strictly below `0.049379`**. Therefore the **source-specific sufficient** equal-prior accuracy exceeds **95.062%** at this enormously large *hypothetical* sample count, uniformly in ALL unknown `C^infinity` calibrations satisfying each derivative cap ≤100. No actual 45-million spatial recordings, source noise or calibrated bound are available; neither sample efficiency nor physical feasibility is claimed. This is not a sample-size optimum.

## 5. Negative controls, non-transfer and standard prior art

Actual tests also exclude:
1. **False stronger robustness** at L=400: `gap(400)<0`, so an inference of robust uniform two-mode classification at such L is explicitly rejected.
2. **False all-N extrapolation**: the out-of-source N40 pair `(0,10,20)` and `(10,10,10)` has the same exact a=0, but unequal exact source A/B ratios owing to different face symbol f; its single-argument calibration cannot reconcile both. This shows the theorem requires the original prime-41 axis-node geometry.
3. **False one-frequency identification under free constant gain**: even at L=0, separate constant log calibration fits can match one fixed mode variance exactly; the two-mode contrast is essential under this nuisance contract.
4. **False physical transfer**: the theoretical full-site Fourier measurement and its Gaussian covariance are hypothetical; the original five fixed coarse masks plus mathematical global k0 are not a native 68,921-site recorder and not the extra high-frequency devices.

Standard relevant prior: classical McShane–Whitney real Lipschitz extension, and bounded smooth real interpolation. A basic pedagogical reference: https://mathworld.wolfram.com/LipschitzExtensionProblem.html . This ROT002 gives a **self-contained source-specific proof** and numerics; it does not claim new general mathematical method. Literature/source novelty remains unestablished and would need a separate full targeted review.

Scope STOP: the theorem does not survive automatically if phi must be shared between hypotheses, constrained by low polynomial degree or finite spatial range, satisfy the M15 C4/C5 derivative budgets instead, or if original source sensors cannot read the two selected modes. For a physically grounded claim, separately prove an actual calibration bound, independent raw Fourier observability, genuine noise model and cross-source identifiability. Original M13 historical producer remains missing.

## 6. Reproducibility, reviewer target and state

New complete program `geeky_s13_rot002_sharp_first_derivative_calibration.py` uses the exact rational coefficients above and two independent numerical arithmetic backends `mpmath` 85 digits plus directed `mpmath.iv` 75 digits. Complete source-specific JSON certificate `IW_GEEKY_S13_ROT002_SHARP_LIPSCHITZ_CERT_001_20261122.json` contains ALL decisive interval handles, winning/runner-up orbit data, strict margin, source SHA pointers, and negative control outcomes. The program is reproducible with `python -I` in a source-independent working directory and records the exact source/program SHA256 in its package manifest. The source does not recompute original M13 tensor C, nor does it depend on original M15 Python files. An unmodified original helper was read at prior turn, not executed in the present rotation.

**Bounded independent I1 request:** Independently reconstruct all 1771 prime-axis node classes from original N41 and both exact rational A/B spectral laws; certify via outward intervals that the unique maximum of 1770 consecutive absolute `d` secants is the selected `i=390`, confirm the exact-at-critical smooth construction (especially derivative matching near the critical segment), verify the two high-k modes outside original M13 221 energy-difference Fourier support, and check the two-mode concentration formula including the factor 4 and 45M sample claim. Verify N40 counterexample and do NOT promote the synthetic observer to a physical one.

Review/authority status: **AUTHOR SOURCE-TYPED PROOF / INDEPENDENT OUTWARD INTERVAL NUMERICS**; other-cell `REC13/AUD3` I1 **PENDING**, external I3 **NOT CLAIMED**, KN15 BW actual ingest **PENDING**, owner physical CANON/EXEC_SIGN **NOT GRANTED**. Publication and Slack handoff alone do not upgrade scientific acceptance. No task cascade.

**FINAL:** `N41_1771_EXACT_CYCLOTOMIC_ORBITS_ROT001_FIRSTNESS_RETAINED / 1770_ALL_ADJACENT_OUTWARD_IV75_ORDER_AND_SLOPE_PASS / UNIQUE_CRITICAL_MODE_PAIR_I390_PASS / SHARP_CINFTY_DERIVATIVE_LSTAR_347P356906774_SOURCE_PROOF_PASS / EXACT_CRITICAL_ALIAS_SMOOTH_GLUING_PROOF_PASS / L100_TWO_MEAN_FREE_MODE_TEST_45M_FINITE_N_GUARD_PASS / N40_COMPOSITE_COUNTEREXAMPLE_PASS / INITIAL_FLOAT_INTERVAL_CONTAINMENT_FALSE_FAIL_DIAGNOSED_AND_REPAIRED / NO_NATIVE_M13_HELPER_RUN / NO_GENERAL_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE`.