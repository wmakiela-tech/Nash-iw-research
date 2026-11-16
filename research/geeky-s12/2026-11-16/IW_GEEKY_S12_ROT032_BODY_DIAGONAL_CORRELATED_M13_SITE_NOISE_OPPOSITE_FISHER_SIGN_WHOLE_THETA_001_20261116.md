---
artifact_id: IW_GEEKY_S12_ROT032_BODY_DIAGONAL_CORRELATED_M13_SITE_NOISE_OPPOSITE_FISHER_SIGN_WHOLE_THETA_001_20261116
date: 2026-11-16
origin: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
exposure: PUBLIC
science_status: ORIGINAL_PUBLIC_M13_NATIVE_SOURCE_IV55_TWO_WHOLE_FOLD_BRACKET_REVERSE_FISHER_SIGN_PASS / EXACT_DIAGONAL_REGION_GRAPH_NEGATIVE_QUADRATIC_PASS / WHOLE_CONTINUOUS_THETA_MONOTONICITY_PASS / INDEPENDENT_SPATIAL_SAME_CELL_24_GLS_CHECKS_PASS
review_status: M15_ROT023_INDEPENDENT_PREVIOUS_ROT029_I1_PASS / M15_ROT024_INDEPENDENT_PREVIOUS_ROT030_I1_PASS / ROT031_AND_NEW_ROT032_EXTERNAL_I1_PENDING
sync_status: GITHUB_PENDING_BW_INGEST
claim_ceiling: AUXILIARY_ORIGINAL_M13_N41_B / HYPOTHETICAL_COMMON_FIELD_TRANSLATION_GAIN_SIXTH_OBSERVER_AND_SITE_NOISE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT032 — Positive body-diagonal site correlations INCREASE alpha information; strict original M13 counterexample to extending ROT031 beyond axial neighbors

## 1. Source, priority and review currentness

Original M13 FIRST authored the public N41 B sparse Fourier/TT operator, original source file 8970 bytes and immutable Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679, plus original B25 coefficient file 7501 bytes, blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0. Both SHA1 Git blob checks are performed BEFORE original source import. Public native original:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py

Geeky ROT023–024 FIRST two old five-output source rank4 Whitney folds; independently M15/AUD2 I1 reviewed. Geeky ROT027 FIRST mathematical sixth unmasked full-domain B energy; M15 ROT021 independently source reviewed it on DIFFERENT M15 exact pairs. Geeky ROT028 independent log-noise six-channel Fisher was independently I1 reviewed by M15 ROT022; M15 FIRST showed an unrestricted fixed sixth calibration nuisance eliminates recovered information. Geeky ROT029 FIRST shared site errors and the 18268-point outer-shell equivalent; M15 ROT023 independently IV65 reviewed this previous result and supplied a separate common-site additive baseline nuisance theorem:
https://github.com/wmakiela-tech/Nash-iw-research/blob/6aee4744bbd6a4f9444a47abff54f177ac36e5fb/research/m15/2026-11-16/IW_M15_ROT023_INDEPENDENT_ORIGINAL_M13_CORRELATED_SITE_NOISE_OUTER_SHELL_AND_COMMON_ADD_BASELINE_RANK_001_20261116.md

Geeky ROT030 FIRST random known-variance sixth RAW energy calibration and independent heterogeneous per-site Gaussian error Loewner bounds; M15 ROT024 NOW independently source IV70 reviewed ROT030 and FIRST derived its OWN Gaussian hypothesis distances on TWO DIFFERENT exact M15 pairs:
https://github.com/wmakiela-tech/Nash-iw-research/blob/7f5242eee8ce9cd8c3796370aefafc46e306327d/research/m15/2026-11-16/IW_M15_ROT024_DIFFERENT_CELL_ORIGINAL_M13_STOCHASTIC_CALIBRATION_LOEWNER_REFEREE_AND_TWO_EXACT_ALIAS_PAIR_GAUSSIAN_HYPOTHESIS_GATES_001_20261116.md

ROT031 FIRST proved the original M13 six-region aggregate edge matrix for SIX AXIAL nearest-neighbor site error correlations is strictly positive definite, giving MONOTONICALLY DECREASING source Fisher information for increasing positive AXIAL correlation:
https://github.com/wmakiela-tech/Nash-iw-research/blob/aad135fe707dbee3818bbac2c9acde6dc957cd54/research/geeky-s12/2026-11-16/IW_GEEKY_S12_ROT031_EXACT_M13_MASK_NEIGHBOR_GRAPH_AND_CORRELATED_SITE_FISHER_SPECTRAL_BOUNDS_001_20261116.md

NEW ROT032 changes ONLY the site-correlation adjacency to eight nearest BODY DIAGONALS, holding original source B, fixed five masks, mathematical sixth full energy, four nuisance parameters, and known random sixth calibration fixed. A genuine source-specific sign reversal results. This does not retract ROT031 in its proper axial domain.

## 2. Exact source region graph — sharp negative knowledge

Original N41 cube contains 68921 points. The SIX original disjoint source regions are [outer,shell1,shell2,shell3,shell4,shell5] with exact site occupancies (18268,7778,6938,6146,5402,24389). Eight directed periodic body diagonal one-step displacements are all (±1,±1,±1). Original source region labels were enumerated at all 41 cubed lattice sites; independently, all counts were reproduced by exact inclusion-exclusion of original nested cubes under one-point diagonal shifts.

The complete EXACT 6x6 integer directed neighbor matrix:
 Ebody =
 [[114168,31976,0,0,0,0],
  [31976,1680,28568,0,0,0],
  [0,28568,1584,25352,0,0],
  [0,0,25352,1488,22328,0],
  [0,0,0,22328,1392,19496],
  [0,0,0,0,19496,175616]].

Its row sums equal eight times region occupancies, and it is symmetric. For exact integer contrast z=(0,1,-1,0,0,0),
 z^T Ebody z = 1680+1584−2*28568 = **−53872**.
Ebody is therefore INDEFINITE, unlike ROT031's axial E. Exact source geometrical counterexample: the ROT031 mask-aggregate PSD theorem does NOT follow from positive pointwise spatial correlations alone. Indefiniteness by itself does NOT imply a Fisher increase; separate source calculation below proves the actual consequence.

## 3. Exact site covariance and source inverse observer

Original unchanged M13 tensor_polys(41) produces 41 complex 3x3 B Fourier tensor modes and original five fixed cubic observation masks k2..6, disjoint shell weights (7778,6938,6146,5402,24389). One common rigid input-field shift t relative to fixed masks and common free log energy gain b are EXPLICITLY HYPOTHETICAL additions; M13 original calc has no t or independently adjustable b. The sixth mathematical output is original FULL UNMASKED B Parseval energy, not a documented physical sixth sensor. Four nuisance parameters (b,tx,ty,tz) remain FREE; alpha is target.

Model HYPOTHETICAL centered Gaussian additive RAW energy-density errors at all N41 cubed sites with constant eta and site covariance:
 Sigma_site = eta² (I + theta A_body), theta in [0,2/5],
 A_body = (1/8) sum over eight displacement operators T_(±1,±1,±1).
Periodic Fourier eigenvalues of A_body are product of three cosines and have modulus at most one, so this whole site covariance is STRICT SPD for theta<=2/5. Every directly coupled site pair covariance is positive for theta>0.

Aggregate six original disjoint region RAW ENERGY means, D=diag(occupancies):
 Cbody(theta)=eta²[D^(-1)+(theta/8)D^(-1)Ebody D^(-1)].
An additional independent RAW GLOBAL-ENERGY measurement error of known Gaussian variance (kappa eta)², kappa>=0, transforms to an OUTER-ONLY variance eta²*(68921/18268)²*kappa² in the six disjoint-region observation basis. At positive source energies, log-source scores are a local coordinate representation of exact Gaussian RAW ENERGY mean Fisher, not a claim that logarithms of noisy energies are Gaussian. The correct 6x6 covariance is NONDIAGONAL.

The AXIAL comparator uses Aaxial=(1/6)sum of one-step ±axis shifts and the previous ROT031 exact Eaxis. Original source, observation map, unknown nuisances, eta, theta and kappa are IDENTICAL.

## 4. New actual original M13 native IV55 source proof — both WHOLE alpha root brackets

New executable verifies original M13 Git blob hashes AND FULL prior original ROT031 source/spatial result JSON SHA256 f747d07aa1bafa4f60b0bbfe1c0fda100e0517d1aa3479a19b73778a8ec91cc3 and e44fc1d7511c8e360afe206e8b60f2cb48497043fbe39a468be22e529bdf6dd1 BEFORE scientific import. It ACTUALLY imports and executes original unchanged M13 tensor_polys(41), ORIGINAL inner and window_mode for ALL FIVE shell energy means and ALL TWENTY analytic derivatives, plus native full k0 B energy, using outward mpmath.iv.dps55 over EACH ENTIRE old alpha source fold root bracket. Unlike ROT031 parent, the previous shell scores are NOT just imported; they are recomputed from ORIGINAL source.

For exact old five-output fold alpha, the original nuisance Xold is rank4, old alpha score belongs to Xold span. Let outer residual deltaO be its alpha score after eliminating the four nuisance directions. The new interval code recomputes deltaO STRICT NEGATIVE and computes the correct full correlated Gaussian nuisance-projected information by interval matrix solves. All inverse matrix interval pivots are STRICTLY nonzero.

STRICT source epsilon² Ialpha intervals at theta=0.4 and random sixth calibration kappa=.01:

First source fold alpha in (.01861522133766,.01861522134166):
 - independent site theta0: (14.94344110836182, 14.94888118507616);
 - AXIAL positive theta.4: (13.03658954030321, 13.04137423931533);
 - BODY-DIAGONAL positive theta.4: (16.51825964688310, 16.52407431651774).

Second source fold alpha in (.05416739905600,.05416739906000):
 - independent theta0: (470.43352110459941, 470.50207847684700);
 - AXIAL positive theta.4: (397.50204237715986, 397.55830969974200);
 - BODY-DIAGONAL positive theta.4: (580.94609660756069, 581.02208555128309).

Thus the original source model has STRICT OPPOSITE signs: positive AXIAL spatial correlations reduce alpha Fisher, while positive BODY-DIAGONAL spatial correlations increase it, holding all other mathematical choices fixed. All intervals are conservative outward source certificates over FULL root brackets, not midpoint-only Float64 diagnostics. Source interval comparisons also PASS at kappa=0. At theta=.4,kappa=.01 relative midpoint info change: body +10.54%, +23.49%; axis −12.76%, −15.50%.

## 5. Stronger continuous-theta theorem; no intermediate grid assumption

At exact old source fold, fix admissible linear contrasts L=(l1,...,l5,1) such that L annihilates all four nuisance score columns. Their alpha derivative equals strictly nonzero deltaO. Let
 V(theta) = min over admissible L of L^T C(theta) L,
 epsilon² Ialpha = deltaO² / V(theta),
 where C(theta) is the source 6x6 normalized RAW energy mean noise covariance, affine in theta for fixed source alpha and calibration.

Since V(theta) is the pointwise INFIMUM of affine functions, it is CONCAVE. Its unique optimal contrast at theta0 is source certified and envelope theorem gives Vprime(0)=L0^T Cprime(0)L0. The new ORIGINAL M13 outward source IV55 proves, for EVERY alpha throughout each prior fold-root bracket:
 fold1 Vprime(0) in [−0.002005575082102,−0.001994794417020];
 fold2 Vprime(0) in [−0.014727260562657,−0.014644370582820].
Both STRICT NEGATIVE. A concave V has nonincreasing derivative, therefore V(theta) STRICTLY DECREASES for ALL REAL theta in (0,2/5], and alpha Fisher STRICTLY INCREASES for EVERY such theta. The independent known-variance random sixth-only calibration adds a constant to V(theta), since the normalized outer contrast coefficient is identically 1; the derivative and monotonicity conclusions hold for ANY FINITE kappa>=0. The separate M15 totally FREE FIXED unknown sixth offset remains its own source falsifier, not this known-random-variance model.

All these Gaussian GLS, concavity and envelope theorems are classical. NO general mathematics novelty claim.

## 6. Independent spatial observer, 24 verification scenarios

A NEW separately authored same-cell NumPy algorithm rebuilds original 41 source Fourier B 3x3 tensors and four derivative tensor fields, synthesizes the full N41 cubed spatial field by inverse FFT and directly averages original fixed mask energies, without original M13 inner/window_mode for observation. It independently reconstructs Eaxis using three canonical positive-axis shifts plus reflection, and Ebody using four positive-first body-diagonal shifts plus reflection, completely agreeing with primary source graph calculations.

Two folds times TWO region-correlation geometries (axis and body) times theta values 0,.2,.4 times independent calibration kappa values 0,.01 = **24 cases**. Two separate information calculations in each case — six disjoint regions versus five original shells plus FULL energy using fully transformed NONDIAGONAL 6x6 noise covariance — have relative agreement below 2e−8. All 24 independently computed binary64 alpha Fisher values lie inside corresponding original-source WHOLE root bracket strict IV55 intervals. At theta=.4,kappa=.01:
 axial 13.0389816930 and 397.5301753773;
 body diagonal 16.5211667621 and 580.9840903201.
These are numerical crosschecks by SAME CELL, not different-cell independent I1 reviewers.

## 7. Executable source custody and audit failure controls

Complete USER-LOCAL ZIP:
 Geeky_S12_ROT032_body_diagonal_positive_correlations_reverse_Fisher_sign.zip
 **38,227 bytes, SHA256 01e7321d80e74b8bd2263413b66baa5349f08d9ee54afa22e64e250b815e9880**.
12 ZIP members, 11 SHA256 manifest payload files, CRC PASS, 12/12 exact member-byte comparisons PASS, 11/11 SHA256 PASS.

Actually executed NEW original source + interval verifier Python SHA256 a00c849bbabfd2167f00e6484e999b8e22f5bbceb69dd76286dc2f139272f442; COMPLETE original directed source result JSON SHA256 0313b0bfe50afab9aa2f27e4d47861ce8dfb311fae18010423160f8e15daf952. Separate independent spatial FFT Gaussian GLS Python SHA256 f76e38fc17c10cd45c9491f17eb7fa8b24eac6bc1b7b0543fd6b9436b26869e0; COMPLETE spatial JSON SHA256 27f5f176f24d7f58984d220e071bf7c54a550a3af540f7e064f4fe7e18876962. Separate clean replay and mutation receipt SHA256 740a1838f3c44239076ca39d3c4ca3ed5927cc603385999105de8d0f2d799c9b.

Two new source programs ACTUALLY copied with original inputs to TWO clean independent temporary directories and run as isolated fresh Python -I processes, each generating its COMPLETE JSON byte-identical to archived data: 2/2 PASS. SEVEN 1-byte mutations to disposable copies of original M13 code, original B25 data, parent ROT031 source and spatial evidence, or current ROT032 directed source output, all rejected with SOURCE_IDENTITY_MISMATCH BEFORE importing original M13 source, 7/7 PASS. Original sources untouched. Full original executable code and all exact source IV55 endpoints are IN USER ZIP. No false claim of separate public GitHub byte-identical runnable code mirror.

## 8. Source ceilings, transfer and required independent referee

M13 source original FIRST; Geeky ROT031 source AXIAL mask E positive-definite result FIRST; Geeky ROT032 FIRST in this chain original mask BODY-DIAGONAL indefinite E exact counterexample, its strictly opposite source Fisher sign across both folds and all real theta in (0,2/5]. The original M13 public B/N41 auxiliary operator is NOT the missing historical byte-exact full dtc0a_runtime_v0_3_1.py. Common input field shifts relative fixed masks, common free gain, sixth independently observed full energy, synthetic site Gaussian spatial covariance and known-random-variance calibration are NOT authenticated physical producer controls/observations. No real sensor precision, actual spatial noise covariance, global inverse classification, K/J3/TPE/GW/GR physics, or general mathematics novelty.

New ROT032 results are AUTHOR SAME CELL; independently implemented spatial FFT is NOT external I1. M15/REC12/AUD2 new ROT032 independent referee PENDING, original KN14 BW native ingest and owner M15 CANON/EXEC_SIGN UNVERIFIED. Publication or dispatch != scientific acknowledgement. No automatic task cascade.

Bounded reviewer: independently derive Ebody directed counts and its exact negative integer quadratic on ORIGINAL fixed M13 mask geometry; independently reconstruct original five shell gradients and outer score on both old source alpha root brackets; independently check negative whole-bracket source Vprime(0) for body correlation and concavity implication, preserving the distinct sixth-free-calibration falsifier from M15. Do not generalize result to all positive spatial correlations.

FINAL:
 ORIGINAL_M13_TWO_GIT_BLOBS_SHA_LOCKED_ACTUAL_NATIVE_SOURCE_EXEC_PASS /
 EXACT_SOURCE_EBODY_AND_NEGATIVE_INTEGER_QUADRATIC_PASS /
 BOTH_SOURCE_FULL_ROOT_BRACKET_IV55_STRICT_OPPOSITE_FISHER_SIGNS_PASS /
 CONTINUOUS_ALL_REAL_THETA_IN_0_TO_2OVER5_BODY_INFORMATION_STRICT_INCREASE_BY_NEGATIVE_VPRIME_AND_CONCAVITY_PASS /
 AXIAL_ROT031_INFORMATION_DECREASE_PRESERVED /
 24_SPATIAL_GLS_DUAL_OBSERVATION_CROSSCHECKS_PASS /
 TWO_COMPLETE_CLEAN_JSON_BYTE_REPLAYS_SEVEN_TAMPER_ATTACKS_PASS /
 ZIP_CRC_12OF12_BYTES_11OF11_SHA_PASS /
 EXTERNAL_I1_PENDING / BW_PENDING /
 NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
