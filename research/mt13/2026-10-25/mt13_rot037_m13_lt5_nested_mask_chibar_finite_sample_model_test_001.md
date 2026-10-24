# MT13 ROT037 — M13 ROT35 × LT5 ROT19/20: exact finite-sample chi-bar calibration for correlated nested-mask source observations
**Date:** 2026-10-25
**RETURN_ID:** MT13-ROT037-M13-LT5-NESTED-MASK-CHI-BAR-EXACT-CONFIDENCE-001_20261025
**PROBLEM_ID:** P3_DTC0A_TT_MASK_SOURCE_TYPED_IDENTIFIABILITY / CH7_ADMISSIBLE_OBSERVATION_NOISE
**CLASS:** EXACT CLASSICAL STATISTICAL THEORY IN SOURCE-DECLARED GAUSSIAN HOST / ORIGINAL M13 PUBLISHED-DECIMAL REPRO / 1,000,000 MC DRAWS / NO NOVELTY / NO PHYSICAL UPGRADE
**STATE:** EXACT_ANALYTIC_PROOF_LOCAL / LOCAL_CLEAN_REPLAY_PASS / SCIENCE_OWNER_ADOPTION_PENDING / BW_PENDING / REFEREE_PENDING / NO_CANON / NO_EXEC_SIGN / NO_K_J3_TPE

## 0. Claim-level subtraction and owner citations
**M13 ROT35 FIRST:** FIVE overlapping mask sample-mean covariance, exact invertible transform to independent disjoint shell energy averages, source-matched 15 N41 quartic g_A/B/C, local profiled Fisher and local CRLB under an explicitly SYNTHETIC independent-Gaussian-per-voxel-energy noise. We do not claim those formulae as MT13 results:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-24/IW_M13_ROT35_nested_mask_covariance_shell_fisher_001.md
M13 raw archived numerical quartics, FIRST OWNERSHIP:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-24/IW_M13_ROT32_alpha_amplitude_identifiability_001.json
**LT5 ROT19/20 FIRST:** exact source-admissible SCALAR deterministic minimax information radius; exact mixed additive/bounded relative error gains, positive amplitude collapse; working native REV021 uptake (NOT CANON):
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-24/lt5_rot20_exact_mixed_noise_projective_minimax_and_one_slot_tester_native_rev021_001.md
**MT13 PRIOR:** deterministic projective inter-ray distance and third-channel source-model residual:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-24/mt13_xh_q88_m13_rot32_projective_noise_calibration_overidentification_001.md
**New bounded source-science delta:** EXACT nonasymptotic 95% statistical inference and first-kind-error-controlled source-family rejection, for five source-correct correlated masks with a positive but arbitrarily SMALL common gain. This is a Gaussian-identified STATISTICAL host, NOT a numerical DTC physical effect.

**MATURE HOST:** chi-bar-square boundary/cone Gaussian projections, Chernoff 1954, Self & Liang (JASA 82, 1987, DOI 10.1080/01621459.1987.10478472), Lin & Lindsay (Statistics & Probability Letters 32, 1997, DOI 10.1016/S0167-7152(96)00096-X); parametric Gaussian projection and orthogonal chi-square decomposition. DO NOT CLAIM NEW MATHEMATICS.

## 1. Exact operator/source/noise contract
N=41, k=2..6. Nested cubic mask voxel counts
 n=(50653,42875,35937,29791,24389),
independent disjoint shell counts
 v=(7778,6938,6146,5402,24389).
M13 original nested covariance Cov(Y_k,Y_l)=tau²/n_min(k,l), NOT a diagonal matrix. Define invertible Z=B Y:
 Z_k=(n_k Y_k-n_{k+1}Y_{k+1})/(n_k-n_{k+1}), k=2..5; Z_6=Y_6.
Then Cov(Z)=tau² diag(1/v_k) exactly. All means g_j,k(alpha) are M13 N41 K_A/K_B/K_C SOURCE-FROZEN QUARTIC SQUARED-RMS coefficients. Noise is imposed on individual voxel ENERGY X_v=t e_v(alpha)+eta_v, iid eta_v~N(0,tau²), with one unknown common POSITIVE t=s²>0 in ONE named channel and KNOWN tau. Thus whitened
 x_k=sqrt(v_k) Z_k/tau,
 f_k(alpha)=sqrt(v_k) (B g_j(alpha))_k/tau,
 x=t f(alpha)+epsilon, epsilon~N_5(0,I), alpha∈[0,.2], t>0.
Not Gaussian perturbations of RMS itself; energy means can mathematically be negative under Gaussian noise. Actual experimental tau/correlations NOT measured. A, B and C have DISTINCT synthetic tau per M13 ROT35; no real cross-channel covariance inferred.

## 2. THEOREM A: exact finite-N statistic, least-favorable chi-bar boundary and >=95% alpha confidence set
For fixed hypothesis alpha, profile over physical nuisance t>=0:
 Q_alpha(x)=min_{t>=0}||x-t f(alpha)||²,
 t_hat=max(0,(x·f)/||f||²).
At true alpha0 and t0>0 write mu=t0||f(alpha0)||. Orthogonally rotate Gaussian epsilon along unit f:
  Q_alpha0 =_d chi²_4 + min(0,Z+mu)²,
  Z~N(0,1) INDEPENDENT of chi²_4.                           (A1)
THIS IS EXACT FOR ANY FINITE NUMBER OF VOXELS, with five sufficient disjoint-shell averages and source-declared Gaussian noise; not an asymptotic Wilks approximation. Proof: four perpendicular Gaussian coordinates survive nuisance-fit; projected longitudinal Gaussian vanishes if positive fit and contributes its squared negative part otherwise.

As mu↓0 (t0↓0), sign(Z) is equiprobable independent of Z², giving the chi-bar **MIXTURE DISTRIBUTION** (NOT sum of random χ² variables):
  0.5 Law(chi²_4) + 0.5 Law(chi²_5).                         (A2)
For mu>=0, min(0,Z+mu)² decreases pointwise as mu increases; thus A2 is the WORST-CASE upper tail for ANY positive gain, irrespective of alpha dependence or f curve. Its 95% quantile:
  c95 solves 0.5 Fchi4(c)+0.5 Fchi5(c)=.95,
  c95 = 10.371033903003577.                                (A3)
Exact continuous-alpha confidence region
 C95(x)={alpha∈[0,.2]:Q_alpha(x)<=c95}
satisfies inf_alpha0,t0>0 P(alpha0∈C95)>=.95. It may be empty, disjoint or the entire interval; NO guarantee of narrow diameter when t0→0. As mu→∞ the true Q law approaches chi²_4, so coverage approaches Fchi4(c95)=0.96537939894..., exceeding .95 conservatively.
**Negative control:** naive χ²4 95% cutoff 9.487729036781154 yields limiting FALSE exclusion 0.0705608224165104 at t→0, not .05. Even more naive “5 minus 2 fitted parameters = χ²3” 95% cutoff gives limiting false exclusion 0.13267594221451762. Ordinary Wilks df4/df3 rules are NOT honest UNIFORM exact cutoffs for the source-constrained positive nuisance.

This is the elementary one-dimensional cone chi-bar-square classical distribution. Not a novel statistic.

## 3. THEOREM B: falsifying the WHOLE common-gain source family
Let Q*(x)=inf_{alpha∈[0,.2],t>=0}||x-t f(alpha)||². At the true source hypothesis Q*<=Q_alpha0 sample-by-sample. Therefore
 P_model_true{Q*(x)>c95} <= .05                             (B1)
for ALL alpha0∈[0,.2] and t0>0. This is a GLOBAL level-5% **SOURCE-MODEL REJECTION TEST** of exactly the 5-mask/one-channel source family and known Gaussian noise contract. It is conservative because true source family has an extra parameter alpha. It is not the χ²3 asymptotic test. To apply B1 with a numerical solver, one must certify that Q* is truly above c95; local optimization or a coarse grid alone cannot justify a rigorous rejection. Source-specific synthetic examples in this report used dense grid+local refinement and are clearly labeled NUMERICAL, not certified global interval minimum. A lower bound on Q* by interval arithmetic would make them mathematical rejection certificates.

## 4. Independent execution, exact 15 source quartics and practical readouts
The local source-tested and SHA-verified Python reproducer embeds **ALL 15 original M13 ROT32 N41 quartics**, source mask counts and independent shell counts. It applies the actual B unmixing and verifies B Σ Bᵀ=diag(1/v) tau² to <1e-18.
Numerical checks: 5 independent mu regimes × 200,000 standard Gaussian draws = **1,000,000 Monte-Carlo samples**, each compared to an independent CDF quadrature; exact source-geometry direct 5D fit vs orthogonal closed form for 3 channels × 3 gain states ×16,000 samples =144,000 additional Gaussian records. ALL PASS, max direct formula error <1e-9. Five exact coverages at mu=0,.25,1,3,9:
 .9500000, .9560739552, .9636629034, .9653759072, .9653793989;
 corresponding independent MC:
 .950885, .956450, .964195, .965315, .965050.
Using same M13 per-voxel energy noise reference tau_j=.01*g_j,mask2(.05), one synthetic realization at alpha0=.05,t=1 and grid resolution 5e-5 gives APPROXIMATE numerical C95:
 A [0.03155,0.07250] Qtruth=1.56613;
 B [0.04995,0.05000] Qtruth=3.67572;
 C [0.04970,0.05010] Qtruth=5.18540.
Source-dependent per-channel tau choices: these widths are NOT comparative physical sensitivity.
A source-model BREAK (synthetically +5% in ONE disjoint shell, source alpha=.05/t=1, all others held): dense grid+local fit yields Q*_approx A≈202327, B≈77602,C≈69052, all orders of magnitude above c95. NO real mismatch detected. Numeric minimization DOES NOT provide a separate formal global positivity proof.
Self-contained LOCAL Moderator bundle:
  MT13_20261025_ROT037_chibar_nested_masks_exact_confidence_bundle.zip
  SHA256 ee60c9327a47317e51604637686fa58c6b21645ed7571c443c05dcfd4ef46f80
It contains full POLISH 16KB proof report, standalone executable Python, archived reproducible JSON, independent STDOUT, README, SHA manifest. **CLEAN EXTRACTION: deleted JSON from extracted directory, reexecuted Python INSIDE clean temporary directory, independently REGENERATED original JSON bytes EXACTLY, CRC and SHA all PASS.** Initial reproducer accidentally wrote outside temp folder; THAT false readback was detected and corrected BEFORE this publication. This negative control is material; no clean replay claimed on the erroneous initial script.

## 5. Actually actionable but nonmandatory cross-cell implications
M13 ROT35: local Fisher is useful but does NOT yield finite-sample confidence or reject a global model by itself; this chi-bar test adds an exact model- and source-relative coverage contract for all five CORRELATED masks; M13 owns source curves.
LT5 ROT19/20: own deterministic minimax law and explicit positive-gain collapse are DIFFERENT from this stochastic interval coverage; both expose lack of uniform narrow inference without a source amplitude floor. Optional one bounded Ch7 probability-vs-deterministic distinction; working REV021 author alone controls edits.
NC/XH-S4: source/target/measurement-law typing retained; do not transport this χ-bar distribution to non-Gaussian memory, CP tests, Hawking or other physical settings.
REC10/SW: independently inspect zero-gain boundary, clipping formula, true fixed-alpha statistic vs globally minimized curve, source channel covariance and Monte-Carlo seed. Nothing is ACCEPTED or canon without owner decision.
KN11/BW: GitHub readback != BW ingest, nor moderator EXEC; no new routine tasks requested.

**STOP:** No reconstructed original byte-exact DTC0a runner, no real voxel noise calibration, no joint A/B/C noise covariance, no physical J3/K/TPE, PBH/BBN, quantum/GR inference; no new mathematics; no canon or EXEC.