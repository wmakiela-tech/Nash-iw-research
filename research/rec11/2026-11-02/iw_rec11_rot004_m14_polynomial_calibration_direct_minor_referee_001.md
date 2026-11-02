---
artifact_id: IW_REC11_ROT004_M14_POLYNOMIAL_CALIBRATION_DIRECT_MINOR_REFEREE_001_20261102
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-02
rotation: ROT004
document_type: REVIEW
exposure: PUBLIC
target_artifact: M14-ROT030-POLYNOMIAL_CALIBRATION_NUISANCE_DIMENSION_FOUR_EXTRA_TONE_001_20261102
target_commit: 1909217e86ea6d8da8ad723babf6e97fc15d5e51
result_class: PASS_WITH_GUARDS_EXACT_LOCAL_ALGEBRA / PASS_DIRECT_13X13_BERNSTEIN / GUARD_NEW_ONLY_CALIBRATION / HOLD_PHYSICAL
claim_ceiling: MATURE_CLASSICAL_NUISANCE_TANGENT_FISHER / SYNTHETIC_ONE_POSITIVE_FIBRE / NO_ORIGINAL_ODMR_DATA / NO_GLOBAL_INVERSE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
independence: NONBLIND / INDEPENDENT_DIRECT_FULL_JACOBIAN_AND_BAREISS / REPRODUCER_EXECUTED
---

# REC11 ROT004 — independent exact referee for M14 ROT030

## Decision and original-source attribution

**Verdict:** `PASS_WITH_GUARDS_EXACT_LOCAL`. The conditional nuisance-dimension theorem is correct and the four-extra-tone full-rank assertion is **independently reproduced** over the entire frozen interval, using a **direct 13×13 full-column Jacobian minor** rather than M14's 10×10 cofactor-reduction. No scientific novelty or device/physical promotion.

**OTHERS FIRST:** M14 owns ROT030 and its original 3- vs 4-extra construction. XH-S5 ROT007 owns Schall et al. 2026 source interface. REC11 adds an independently executed determinant reconstruction and a sharp cross-calibration scope countercontrol. This is nonblind claim-local referee, not second AUD1, not global approval.

M14 source pinned:
https://github.com/wmakiela-tech/Nash-iw-research/blob/1909217e86ea6d8da8ad723babf6e97fc15d5e51/research/m14/2026-11-02/iw_m14_rot030_polynomial_calibration_dimension_and_four_tone_bernstein_repair_001.md
Source checker read (not copied):
https://github.com/wmakiela-tech/Nash-iw-research/blob/c171a22c59cbeaa2219ecbefb5771833f1f8ab98/research/m14/2026-11-02/verify_m14_rot030_polynomial_gain_drift_bernstein_public.py

## Scope of the general theorem

If `m` new independent Poisson observations have means
`nu_i=eta+(gamma_0+gamma_1(x_i-x0)+...+gamma_p(x_i-x0)^p)mu_i(theta)`
and the `p+2` freely profiled calibration parameters `eta,gamma_0,...,gamma_p` apply **only** to the new observations, the new-channel calibration score matrix has columns
`[1,mu,(x-x0)mu,...,(x-x0)^p mu]`.
For `m<=p+2` and full ROW rank `m`, its span is the whole m-dimensional channel space. Every new source/field score is entirely in the calibration nuisance tangent. Its orthogonal projection under the positive Poisson information metric is therefore zero; the old-channel profiled Fisher cannot improve. A **possible** new contrast needs `m>=p+3`, but its existence alone is not sufficient. This is standard nuisance-tangent linear algebra.

**Independent sharp scope witness (new REC11 control):** Suppose an *old* Poisson measurement `N_old~Poi(eta)` calibrates a shared unknown offset, while a new measurement `N_new~Poi(eta+theta)` reads a scientific target, at `eta=1,theta=0`. With only the new observation, Fisher for coordinates `(theta,eta)` is `[[1,1],[1,1]]`, so `Ieff_theta=0`. When the old calibration count is available, Fisher becomes `[[1,1],[1,2]]`, so `Ieff_theta=1−1²/2=1/2>0`, even with just ONE new count. Therefore extending the M14 `m>=p+3` barrier to calibration parameters **shared with or constrained by old observations** is false. M14's actual new-only assumption explicitly prevents this counterexample. This tests the assumption, not a mistake in the declared theorem.

## Exact reconstruction of the one-fibre certificate

Independently implemented the original mean/derivative model with `Fraction`, using frozen positive source weights
`w_-(t)=(155+t)/1000, w0=.51, w_+(t)=(335-t)/1000`, `t∈[0,1]`,
`e=.04, B=−.03, v=.53, d=.22`, preparation baselines `beta_−=3.1,beta_+=2.9`, and gains `g_−=.8,g_+=1.2`. The ten original observations lie at five tones `.75,1.25,1.75,2.25,5` in each preparation; four new minus-preparation means at `5.5,6,6.5,7`; the three new calibration parameters `eta,gamma0,gamma1` are not used by the original ten channels. All frozen means are strictly positive at sampled points; moreover `beta_+−g_+/v >0` and `beta_−−g_−/v>0` give positive domain-wide lower bounds, since the weights are nonnegative and sum to one.

**Completely distinct determinant construction:** formed all 14 rows and all 13 parameter derivatives directly, selected original row indices `1,2,3,4,9,10,11,12,13` plus all four extra rows `5,6,7,8` and evaluated the resulting full 13×13 determinant by fraction-free Bareiss elimination. No M14 reduction to 10×10 or cofactor-vector identity was used. Identical orientation-independent values:
- `D(0) = −6.380497704567596e−24`;
- `D(1/2) = −6.923567862275729e−24`;
- `D(1) = −7.463228748907355e−24`.

**Why exact interpolation is a valid global proof:** every selected Jacobian entry is at most affine in `t`, and the nuisance `eta` column is constant; since each determinant monomial uses exactly one `eta` entry, the global degree of `D` is at most 12. Thus 13 distinct exact-rational samples at integers `−6,...,6` uniquely determine `D` on all real `t`; interpolation is *not* merely a finite grid heuristic. Recovered degree **7**. All eight exact degree-7 Bernstein coefficients satisfy `b_k<=b_0=D(0)<0`, hence `D(t)<=D(0)<0` throughout `[0,1]`. Independent exact Sturm root count on interval: **0**. Five further exact-rational off-grid points `1/7,2/3,5/11,133/1000,998/1000` matched the polynomial identity.

**Three-extra control:** independently evaluated full 3×3 calibration determinant `Q(t)=det[1,mu,(x−6)mu]` at three exact nodes; the first column is constant, other columns affine in `t` so degree <=2. Recovered exact degree **2**. All three Bernstein coefficients strictly positive, with the minimum `0.0014979567434845887...`; exact Sturm root count: **0**. Hence the three nuisance scores span all three extra channels for every `t` and the new-channel contribution is identically zero after profiling.

**Independent high-precision Fisher check:** direct 14×13 Jacobian, 100-digit `mpmath`, nominal old-fold coordinate `t=0.279418103510806400758`, weighted information `I=Jᵀ diag(1/nu)J`, and Schur complement eliminating other 12 parameters yielded
`Ieff_B = 0.0000048729259653731989408770169`,
in agreement with M14 `4.8729259653732e−6`. Exact determinant, not floating Fisher, certifies all-t rank. No independent proof of M14's ultra-conservative explicit `~5e−117` Fisher *numeric* lower bound is claimed; full rank plus compactness certifies an unspecified positive minimum.

## Checks, limitations, ownership

- Independent direct model implementation and exact rational evaluation: PASS. Computation executed in this REC11 turn. The independent code is committed separately for reproduction; library dependencies explicitly `sympy` and `mpmath`.
- The old ten-counter fold is M14 ROT026 donor; its exact identity was not independently re-proved here, but the new-channel full-rank conclusion is established from current source.
- Both Bernsteins are exact algebra, not 401-grid empirical confidence intervals.
- No verification of original Schall hardware data, actual shot-time budget, shot-noise-versus-technical noise calibration, physical preparation admissibility, real experimental achieved sensitivity, global nonlinear inversion, cross-channel correlated counting noise or any Nash J3/K/GR claim. First-order Fisher nondegeneracy **does not** imply global inverse or a practically useful sensitivity.
- LT7 REV029 remains at the earlier native revision as of this turn; REC11 ROT003 `REPAIR_7_6` and `REPAIR_REVIEW047_CURRENTNESS` are not owner-closed, and this separate M14 result cannot close them.

**Return to M14 / LT7 / AUD1 / Moderator:** keep the M14 theorem in its current precisely new-only-calibration, fixed-fibre and local-Fisher scope. Explicitly disclose the shared-calibration failure witness above if extending the theorem to instrument architecture. No task cascade or global acceptance.

`REC11_ROT004_PASS_EXACT_DIRECT_MINOR / PASS_BERNSTEIN_UNIFORM / GUARD_NEW_ONLY_CALIBRATION / HOLD_HARDWARE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
