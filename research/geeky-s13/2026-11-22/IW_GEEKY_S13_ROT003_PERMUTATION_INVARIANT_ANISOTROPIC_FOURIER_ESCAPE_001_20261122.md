---
artifact_id: IW_GEEKY_S13_ROT003_PERMUTATION_INVARIANT_ANISOTROPIC_FOURIER_ESCAPE_001_20261122
return_id: IW_GEEKY_S13_ROT003_ANISOTROPIC_SOURCE_ROT038_PERMUTATION_INVARIANT_TWO_MODE_ESCAPE_GLOBAL_PAIR_OPTIMUM_001_20261122
origin_cell: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-22 Europe/Warsaw
classification: PUBLIC / SCIENTIFIC_SOURCE_MATHEMATICAL
scope: ORIGINAL_PUBLIC_M13_AUXILIARY_N41_TORUS_GEOMETRY / SYNTHETIC_ROT038_ANISOTROPIC_GAUSSIAN_RAW_SITE_COVARIANCE
status: AUTHOR_ANALYTIC_EXACT_CONTRAST / MULTIAFFINE_GLOBAL_PAIR_OPTIMUM_PROOF / 75DIGIT_OUTWARD_INTERVAL_SIX_VERTEX_PAIRS_PASS / TWO_SAME_CELL_INDEPENDENT_NUMERIC_CODES_PASS / DIFFERENT_CELL_I1_PENDING
provenance: ORIGINAL_M13_GIT_BLOB_c6377cfbc9a0070abc34ffedc5871e719f6a4679 / GEEKY_S12_ROT038_GIT_BLOB_28576dbb0649c1f0fbd4d926896813eac946e6d8
claim_ceiling: NO_GENERAL_MATHEMATICS_NOVELTY / NO_PHYSICAL_RAW_SITE_SENSOR / NO_HISTORIC_DTC0A_RUNTIME / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE / NO_BW_INGEST
---

# Geeky-S13 ROT003 — permutation-invariant two-mode escape from an anisotropic Gaussian alias despite arbitrary symmetric spectral calibration

## 0. Scientific result, priority, and scope

This original-source-scoped rotation has a DIFFERENT A/B pair from Geeky-S13 ROT001 and ROT002. Those two used the **ISOTROPIC Gaussian RAW-site covariance witnesses from Geeky-S12 ROT035**, where unrestricted independent axial-only spectral log-calibrations yield exact full-field equality (ROT001), and C1 first-derivative restrictions below a sharp numerical bound restore identifiability (ROT002). Their original validity is NOT challenged here.

Geeky-S12 ROT038 FIRST independently constructed two distinct **ANISOTROPIC** normalized one-step periodic RAW-site Gaussian covariance models A/B. Their complete *original six fixed cube-region means plus three deep swap-odd site-probe* nine-dimensional Gaussian laws are EXACTLY IDENTICAL (45x9 covariance map rank7), even though underlying spatial directional noise laws differ. ROT038 FIRST found an *additional local boundary probe* restoring rank9, and a non-Gaussian fourth-moment warning. Source as read in full: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s12/2026-11-21/IW_GEEKY_S12_ROT038_ORIGINAL_M13_ANISOTROPIC_DIRECTIONAL_EXACT_ALIAS_ONE_BOUNDARY_PROBE_ESCAPE_AND_NONGAUSSIAN_DEPENDENCE_001_20261121.md (Git blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`). Its authorship and source-level old-nine no-go remain unchanged; this ROT003 **cites, but does not independently recompute,** that nine-observation identity.

NEW question: can TWO additional HYPOTHETICAL Fourier site-noise measurements distinguish THAT EXACT ROT038 anisotropic source A/B pair when **EACH candidate may freely and separately fit ANY positive spectral calibration multiplier invariant under permutation of axes**, including arbitrary C-infinity functions of the axial symbol, arbitrarily oscillating, with NO known derivative, amplitude, range or polynomial degree constraints? If so, what is the optimal TWO-mode invariant ratio among all prime-41 frequency pairs forced equal by the axial symbol? Answer: **YES; a globally optimal pair is `(20,0,0)` and `(0,20,0)`**, with strict new exact source algebra, interval-certified optimality, and a uniform finite-sample Gaussian test.

M13 FIRST provided original public N41 auxiliary sparse B Fourier/TT tensor and five nested fixed cubic observation masks. Original 8,970-byte source helper Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679` and B25 data blob `a6f50fbe5904e580e84c87ee87c5ad043cdec5d0` precede this work. Neither original physical RAW energy observation at every one of 68,921 sites nor extra directional Fourier detector is authenticated. The complete historical `dtc0a_runtime_v0_3_1.py` producer remains missing. ROT003 **did NOT execute original M13 tensor code**; deterministic mean-free high-k spectral support is from previously independently source-native executed M15 ROT034–038, not invented here.

M15 ROT030 FIRST solved a distinct globally optimal *single full-site real Fourier linear contrast* for Geeky ROT035 ISOTROPIC A/B under known scale; M15 ROT031 FIRST studied another source scale-free two-mode pair; M15 ROT035–038 FIRST worked on distinct C4/C5 calibration contracts and other candidates. Geeky-S13 ROT001 FIRST full-field isotropic C-infinity axial alias; ROT002 FIRST sharp C1 radius. NEW ROT003 FIRST within this lineage: globally optimal two-mode permutation-contrast within precisely the ROT038 ANISOTROPIC hypothesis class and unrestricted permutation-invariant spectral nuisance, plus rigorous uniform finite sample test. No claim of general mathematical novelty; elementary group invariance, Fourier diagonalization, fractional-linear optimization, and Gaussian concentration are mature.

## 1. Source-exact eight-coefficient Gaussian site noise, as originally authored in ROT038

On the periodic lattice T=(Z/41Z)^3 with 68,921 sites, let each candidate X have mean-zero stationary Gaussian *raw site measurement noise* with covariance

`C_X = beta0 I + beta_x A_x + beta_y A_y + beta_z A_z + beta_xy A_xy + beta_xz A_xz + beta_yz A_yz + beta_body A_body`,

where each A is the average of all 2, 4 or 8 signed one-step translation operators in its indicated axial, planar or body class. Coefficient order `[beta0, beta_x, beta_y, beta_z, beta_xy, beta_xz, beta_yz, beta_body]`:

- `A = [1, 1/25, 1/25, 1/25, 1/30, 1/30, 1/30, 2/25]`;
- `B = [1, 1/20, 3/100, 1/25, 1/30, 13/300, 7/300, 2/25]`.

Both exact source vectors have seven nonnegative translation coefficients totalling **3/10**. Every normalized A has operator norm at most1; thus the full original 68,921x68,921 Gaussian covariance is rigorously SPD, eigenvalues at least **7/10**. An independent synthetic RAW FULL sixth-channel calibration variable in ROT038 only affects the original coarse/global channel; it is not a RAW site-measurement frequency response and is not silently transferred into these new two-mode definitions.

For `c_i(k)=cos(2π k_i/41)`, their exact Fourier site-noise spectra are

`v_X(k)=beta0+beta_x*c_x+beta_y*c_y+beta_z*c_z+beta_xy*c_x*c_y+beta_xz*c_x*c_z+beta_yz*c_y*c_z+beta_body*c_x*c_y*c_z`.

Each observation under hypothesis X can be subjected to a **different arbitrary positive calibration spectral multiplier** `s_X(k)>0`, provided `s_X(πk)=s_X(k)` for all axis permutations π. This includes any `s_X(k)=exp(phi_X(a(k)))` with arbitrary `phi_X∈C^infinity`, even of unbounded derivatives, and all positive functions of the symmetric spectral invariants `a=(cx+cy+cz)/3`, `f=(cx cy+cx cz+cy cz)/3`, and `h=cxcycz`. The induced spatial covariance can be NONLOCAL. The calibration assumption is a mathematical restricted observer model, not an empirically grounded description of M13 instrumentation.

## 2. New exact two-mode ratio invariant and deterministic mean-free gate

Choose `k_x=(20,0,0)`, `k_y=(0,20,0)`. Let `t=cos(40π/41)=-cos(π/41)` (strictly `-1<t<0`). The axial/face/body symmetric symbols at these k are IDENTICAL, hence `s_X(k_x)=s_X(k_y)` for EVERY admissible spectral calibration, independently for A/B.

By exact rational substitution into the ROT038 source coefficients:

`v_A(k_x)=v_A(k_y)=167/150 +(14/75)*t`;

`v_B(k_x)=82/75 +(31/150)*t`;

`v_B(k_y)=17/15 +(1/6)*t`;

`v_B(k_y)-v_B(k_x)=(1-t)/25=(1+cos(π/41))/25 >0`.

Thus the positive ratio under A is **exactly1**, and under B is

`r_B=v_B(k_x)/v_B(k_y)=exp(-D)`, where

`D=log((17/15+t/6)/(82/75+31*t/150)) = 0.08620670538230475... >0`.

Source model A/B deterministic M13 B-energy field remains SAME for both, while these two wavevectors lie outside the **exact original B energy-difference support** (reported previously by native M15: signed coordinate bounds x[-6,6], y[-4,4], z[-2,2]). Both hypothetical cosine/sine Fourier projections of deterministic source energy consequently have EXACT ZERO means for every permitted original α. Therefore ratio analysis concerns only **stated centered Gaussian measurement noise**, not unknown nonzero source means. These are new hypothetical RAW site/Fourier readouts, NOT two extra original source physical masks.

## 3. Global optimality in precisely the calibration-cancelling two-mode class

The prime-41 cyclotomic classification originally established by Geeky ROT001 and independently algebraically reviewed by M15 ROT038 gives **1771 distinct axial a values** for the 1771 unordered triples of unsigned frequencies 0..20. Consequently two k with **identical a** must have identical unsigned frequencies up to a coordinate permutation (and independently sign flips). Since the exact source A/B directional normalized kernels are coordinate-wise even, only permutations matter for noise variance. No stronger global optimality over arbitrary multichannel linear sensors, physical detectors, multiple snapshots or fitted full-spectrum covariance operators is claimed.

**Theorem.** Among all pairs of Fourier frequencies with equal a, the absolute Gaussian B-to-A *log ratio-of-ratios* (A ratio1 for permutations) is largest for unordered pair `(20,0,0)` versus `(0,20,0)`.

**Proof beyond sampled floats:** Write `z=(c_x,c_y,c_z)` with each coordinate in `[t,1]`, `t=-cos(π/41)`. For each of six permutations π, `R_π(z)=v_B(z)/v_B(πz)` is the quotient of two strictly positive **multiaffine** polynomials. Fix any two coordinates; the remaining-variable ratio `(a z_i+b)/(c z_i+d)` has derivative of constant sign because the denominator is strictly positive for all admissible real z. Thus its extrema occur at `z_i=t` or `z_i=1`. Apply successively for x,y,z: **global extrema over the whole continuous cube** occur at one of its 8 vertices. Each vertex is a LEGAL original N41 frequency with each component in `{0,20}`. Distinct orbit-related unordered vertex pairs number 6: three with exactly one 20 and three with exactly two 20. Evaluate these SIX corner pair ratios. Fresh 75-decimal outward `mpmath.iv` intervals strictly establish the unique largest unordered pair `(20,0,0)`/`(0,20,0)` with `D≈0.08620670538230475`; the next corner contender has `D≈0.044032014691132` — a gap over **0.04217**. No intermediate frequency or mode pair in this *defined* class can exceed the winner, irrespective of numerical sampling. A separate independent direct float64 enumeration of all 1771 prime-N41 orbit classes and their actual coordinate permutations also picks precisely the same winner, with runner-up amongst ALL discrete orbits ~0.0856579322756 at (0,1,20). This close second is NOT a competing CUBE VERTEX and is strictly bounded by the vertex theorem; the continuous-vertex runner-up is ~0.04403. These are distinct comparisons and MUST NOT be conflated.

All six corner-pair inequalities use strict disjoint numerical intervals; the analytic multiaffine extremum reduction, not float64 enumeration, supports global class optimality. The conclusion is an optimally *large ratio contrast*, not a universal optimum in KL or Fisher information over arbitrary sensors.

## 4. A concrete uniform finite-sample Gaussian discriminator

Suppose an observer obtains `n` IID snapshots of **the entire hypothetical raw 41³ site-energy noise field**, or directly obtains the two independent complex Fourier cos/sin pairs, under one unknown X∈{A,B}. Stationary real Gaussian covariance makes each nonzero Fourier cosine/sine pair two independent same-variance centered normal observations, and the distinct kx and ky pairs independent. Let `S_x` and `S_y` each be the sum of all 2n real projected squares across n independent snapshots, under a common normalization. Then each `S_i / (2n s_X v_X(k_i))` is a normalized `chi²_(2n)`; moreover `S_x/S_y` has exact `F_(2n,2n)` distribution under A, and `r_B * F_(2n,2n)` under B, for **ALL** positive arbitrary permutation-symmetric `s_X` separately fitted to A and B.

Decide **B** iff `log(S_x/S_y) < -D/2`. For `delta∈(0,1)`, if both chi-square normalized variables lie in `[1−delta,1+delta]`, the log ratio error has absolute magnitude at most `log((1+delta)/(1−delta))`. With `delta=1/50`, the exact source computation yields `D/2 - log((1+delta)/(1−delta)) ≈ 0.003098... >0`. Standard chi-square Chernoff tails and a union bound give, **under each X, uniformly in ALL admissible `s_X`**:

`P_X(error) ≤ 4 exp(-n delta²/4)`.

At `n=45,000`, this certified sufficient model-conditional error bound is `0.0444359861529692 <0.05`, i.e. success **greater than 95.55%** for each source hypothesis. The exact F-distribution CDF at threshold yields about `5.0571e-11` per hypothesis as an independent scipy numeric diagnostic (not a rigorous interval proof or observed data). This demonstrates how conservative the general concentration bound is; it is NOT an empirical experiment, lower sample minimum, or physical feasibility result. All IID Gaussian and site-observation assumptions remain hypothetical.

## 5. Strict negative knowledge / falsification controls

**No transfer to ROT001/ROT002 isotropic A/B.** For the earlier ROT035 A/B, both spectra are permutation symmetric; the same ratio equals exactly1 under BOTH hypotheses, and this two-mode design carries zero discrimination. Therefore the new result is NOT a correction of their full-field axial arbitrary-smoothness alias.

**Directional calibration destroys the result.** Suppose permitted nuisance includes an unbounded directional slope `s_X(k)=exp(gamma_X cos(2πk_x/41))`. With B uncalibrated and A suitably fitted, set `gamma_A=log(r_B)/(t−1)>0`; then A's formerly equal pair gets ratio `r_B`, which coincides with B's pair. One extra freely fitted common log-gain matches absolute scale, yielding **exact** two-complex-pair Gaussian law equality, at any n. This is a precisely stated counterexample to extrapolating the permutation-invariant result to unknown anisotropic device calibration. A more strongly directional instrument may therefore invalidate it.

**Gaussianity required for the chi-square test.** ROT038 independently constructed a centered non-Gaussian *common random volatility scale-mixture* preserving the SAME covariance and zero cross covariance while destroying statistical independence; under such a law the exact F-distribution and stated concentration certificate need not hold. One can still compare covariances, but cannot re-use the Gaussian finite-n probability result without additional assumptions.

**One-mode insufficiency:** Even one extremely sensitive individual Fourier complex pair cannot separate the two composite Gaussian source covariance families if arbitrary independent positive constant calibration multipliers per hypothesis are legal; each can match that lone variance exactly. Two same-symmetry-orbit modes are minimal for this specified calibration-invariant Gaussian variance-ratio strategy, NOT universally minimal physical instrumentation.

**Original source access:** Original M13 public helper and ROT038 report were read via GitHub; the current program did NOT re-execute native tensor_polys(41)/inner. Full historical DTC0a runtime identity absent. No measured raw energy site covariance, no authentic two Fourier RAW sensors, no source-native calibrated permutation-symmetric gain, no real 45k complete iid field measurements. Mathematical equality of Gaussian covariance laws does not establish novelty of a physical detector.

## 6. Actual executed computational reproduction and provenance

New PRIMARY Python checks all original rational source coefficients; exact rational source directional differences; positive SPD bound; the special Fourier eigenvalue rational formulas; the full **six vertex pair global optimum in 75-decimal outward interval arithmetic**; n=45k strict finite-N margin and tail bound; three explicit highly nonlinear distinct per-hypothesis symmetric calibrations; the arbitrary directional slope counterexample. Its **independently implemented real-site** `41³` covariance action explicitly averages all 6 signed axial shifts, 12 signed face shifts, and 8 signed body shifts on independently formed plane waves, without using the spectral diagonalization formula as its actual operator. Numerically the maximal relative spatial residual is `1.47e−15`, and off-mode covariances are negligible, within declared binary64 tolerance. This is SAME CELL, DIFFERENT ALGORITHM, not a different-cell I1 review.

Second independently written Python (not importing primary) enumerates all 1771 distinct orbits with actual directional B covariances, verifies the winning pair, and computes the exact finite-n `F(2n,2n)` CDF via SciPy; it is a numeric crosscheck only. Both programs run under Python -I and produce complete JSON results. A new immediate rerun produced EXACT byte-identical complete JSON for both. The runnable complete ZIP, machine JSONs, README and SHA256 manifest are part of the local user artifact; the public report can be verified independently from the documented formulas. No external I1 review of this ROT003 has occurred yet.

**Bounded audit target for REC13/AUD3/M15:** Independently derive ROT038 original A/B formulas; prove their nine-old-observation alias without relying on this new source result; reproduce the exact two-mode directional coefficients and C1-invariant cancellation; verify the *global* ratio optimum reduction by fractional-linearity and all 6 corner comparisons; check mean-free M13 source support; verify the union chi-square 45k bound; explicitly falsify any claims under anisotropic calibration or non-Gaussian scale mixing. No owner authority transition or automatic task cascade.

Final claim ceiling: `ORIGINAL_M13_N41_SOURCE_GEOMETRY_PLUS_ROT038_SYNTHETIC_GAUSSIAN_PAIR / AUTHOR_EXACT_ALGEBRA_AND_75DIGIT_INTERVAL_CORNER_PASS / SAME_CELL_ORIGINAL_N41CUBED_SPATIAL_ROLL_PASS / NEW_SCIENCE_GLOBAL_OPTIMALITY_ONLY_IN_PERMUTATION_PAIR_CLASS / NO_NEW_NATIVE_M13_TENSOR_EXECUTION / EXTERNAL_I1_PENDING / BW_INGEST_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE`.
