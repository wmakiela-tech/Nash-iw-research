---
artifact_id: IW_GEEKY_S12_ROT028_SIXTH_GLOBAL_M13_CHANNEL_CONDITIONAL_FISHER_NOISE_PROPAGATION_AND_FINITE_INFORMATION_CEILING_001_20261116
date: 2026-11-16
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
exposure: PUBLIC
source: ORIGINAL_PUBLIC_M13_N41_B_BYTE_LOCKED_UNMODIFIED_SOURCE_ACTUALLY_EXECUTED / PRIOR_ROT027_SOURCE_DIRECTED_BOXES_PINNED
science_status: AUTHOR_NEW_CONDITIONAL_SIX_CHANNEL_FISHER_RANK_ONE_UPDATE_SOURCE_IV75_TWO_WHOLE_FOLD_BRACKETS_PASS / INDEPENDENT_SPATIAL_FFT_NUMERIC_DIAGNOSTIC_PASS / DIFFERENT_CELL_ROT028_I1_PENDING
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: HYPOTHETICAL_IID_OLD_LOG_ERRORS_AND_INDEPENDENT_NEW_LOG_ERROR / M13_AUXILIARY_ONLY / NO_NATIVE_HISTORIC_SIXTH_SENSOR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT028 — the sixth global-energy channel restores local rank but its usable alpha Fisher information is bounded by old-shell nuisance uncertainty

## 0. New target, prior source firstness and different-cell science subtraction

Original M13 FIRST public N41 Fourier B/TT operator; immutable byte-identical 8970-byte helper at:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py
Git SHA-1 blob c6377cfbc9a0070abc34ffedc5871e719f6a4679. Original M13 7501-byte B25 source coefficient table Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-26/direct_B.json

Geeky ROT023 FIRST certified two distinct internal source alpha Jacobian singularities with four-dimensional nuisance rank; Geeky ROT024 FIRST identified two nondegenerate folds, independently reviewed I1 by M15 ROT017 and corrected AUD2 ROT016. M15 ROT018 FIRST constructed and interval-Krawczyk-certified separate M15 exact inverse pairs; Geeky ROT025 FIRST its two DIFFERENT approximate pairs; Geeky ROT026 first original unchanged M13 Python iv77 exact Krawczyk boxes for those own two pairs. M15 ROT020 independently subsequently replayed the separate original M15 ROT018 pair certificates with ACTUAL original native public M13 module iv78, not a review of Geeky ROT026 or new ROT028.

Geeky ROT027 FIRST introduced a SIXTH mathematical observation, the original public full periodic-domain UNMASKED B energy, beyond the five original disjoint fixed-mask shells, and proved both the exact Geeky ROT026 five-shell inverse collisions are STRICTLY separated by the sixth channel and BOTH source folds gain local full 6x5 column rank. The original 82-digit source theorem and its independent original M13 inner+FFT controls:
https://github.com/wmakiela-tech/Nash-iw-research/blob/7e1eec1e9740f52c92af2d41d7c392dc08c04f3f/research/geeky-s12/2026-11-16/IW_GEEKY_S12_ROT027_ORIGINAL_M13_SIXTH_FULL_DOMAIN_ENERGY_LIFTS_BOTH_CERTIFIED_LOCAL_FOLDS_AND_SEPARATES_EXACT_ALIASES_001_20261116.md
Its ACTUAL full 17145-byte result JSON SHA256 bb279334e39cbaabfdeae07085434ab10df6b1a5a9facc0b1eb370e34592e362 is locked as a direct ROT028 input.

M15 ROT019 FIRST independently proved EIGHT source local alpha information restoration gates by FIXING any ONE of four hypothetical nuisances b,tx,ty,tz. This is a different intervention from ROT027–028: all FOUR nuisance parameters remain UNKNOWN/FREE throughout ROT028. Original M15:
https://github.com/wmakiela-tech/Nash-iw-research/blob/8b4b43184a37557d74c9d9e43c96093186d220b2/research/m15/2026-11-16/IW_M15_ROT019_INDEPENDENT_TWO_SOURCE_FOLDS_EIGHT_LEAVE_ONE_NUISANCE_ABLATION_CAUCHY_BINET_IV65_REFEREE_001_20261116.md

No verified independent I1 referee for ROT027 or ROT028 at time of this work. No source priority collapse or claim of novelty of classical statistical results.

## 1. Exact source-defined measurement map versus hypothetical noise model

The ORIGINAL public M13 N=41 B sparse Fourier tensor source has 41 complex 3x3 tensor modes, B_m(alpha)=U_m+alpha V_m+alpha²T_m. The five ORIGINAL source fixed nested cubic interior masks k=2,3,4,5,6 correspond to five positive disjoint shell energies S_i(alpha,t), with exact source weights (7778,6938,6146,5402,24389). The input common torus translation t of all original C1,C2,h fields relative to FIXED observation masks is EXPLICITLY HYPOTHETICAL; original source()/calc() expose NO freely adjustable t or common amplitude c. The OLD five local raw log-energy observables are:
  F_i(b,t,alpha)=b+log S_i(alpha,t), i=1..5,
with a fourth nuisance b=log c, and target alpha.

The SIXTH mathematical output from ROT027 is
  F_6(b,alpha)=b+log g_full(alpha);
  g_full(alpha)=(1/6)*sum_m ||B_m(alpha)||_F².
Fourier phase covariance gives B_m(alpha,t)=exp(i m dot t) B_m(alpha), so g_full is EXACTLY translation-invariant by Parseval, without fixing any nuisance.

Original OLD observable Jacobian at the exact prior fold is J5=[X,a], where X is 5x4 nuisance score with columns (ones,Dtx log S,Dty log S,Dtz log S), full rank FOUR, and a is old 5x1 target alpha score. At the old fold, a lies EXACTLY in range(X). Original source SIXTH row: x6=(1,0,0,0), a6=g_full'(alpha)/g_full(alpha).

A NEW, expressly HYPOTHETICAL measurement-uncertainty model assumes independent raw log-shell Gaussian errors e1..e5 with identical variance sigma²>0, plus independent sixth raw log-energy Gaussian error e6 with variance tau²>0. No historical producer, real sensor, empirical covariance, or physical measurement noise is source-established; the Fisher numbers below are CONDITIONAL on these assumptions. For other covariance, local full Jacobian rank still holds where source-certified, but quantitative Fisher information changes.

## 2. General rank-one nuisance regression identity and fold formula

Let beta=(X^T X)^(-1) X^T a be least-squares old target score regression on the nuisance score X. Let x6=(1,0,0,0)^T. Classical linear weighted-least-squares / Schur-complement rank-one update yields, even away from a fold:
 I_alpha,6 = I_alpha,5 + (a6-x6^T beta)^2 / (tau²+sigma² q),
 q=x6^T (X^T X)^(-1) x6 >0,
 I_alpha,5=||a-X beta||²/sigma².

At each exact old fold, I_alpha,5=0 because a lies in range(X), and the alpha-normalized source null kernel vector is v=(v_b,v_tx,v_ty,v_tz,1) where v_nuis=-beta. Thus the source sixth direction from ROT027 is
  delta = a6+v_b = g_full'/g_full+v_b != 0,
and exactly
  **I_alpha,6 = delta²/(tau²+q*sigma²).**

The coefficient q is a *source nuisance score amplification*, not an arbitrary engineering constant. Let T=X[:,1:4] be the 5x3 source translation submatrix. Cauchy–Binet and a Gram cofactor identity give
 q = det(T^T T)/det(X^T X)
   = [sum over C(5,3)=10 of (det 3x3 row minors of T)^2]
     / [sum over C(5,4)=5 of (det 4x4 row minors of X)^2].
Both source numerator and denominator STRICT POSITIVE at both complete original fold-root intervals, as confirmed by new actual M13 source outward interval execution. Original code independently evaluates the Gram determinant ratio; the TWO source interval values have zero-containing differences, without taking Float64 equality as a proof. These mathematical Schur/Cauchy–Binet identities are STANDARD, not general-mathematical novelty.

Crucial limit:
 lim_(tau->0) sigma² I_alpha,6 = delta²/q,
**FINITE** for fixed sigma>0, q>0. Even a hypothetical zero-noise sixth channel cannot remove the uncertainty of the five noisy old shells when four nuisances remain unknown. In contrast as tau/sigma->infinity, the recovered alpha information tends to ZERO. This is quantitative negative knowledge beyond mere local 6x5 full rank of ROT027.

## 3. NEW original unchanged M13 source mpmath.iv75 full-bracket data

Actually import original public SHA-verified M13 unchanged Python module, execute its original tensor_polys(41), original inner/window_mode at outward mpmath.iv.dps75 over each WHOLE original root alpha interval. Directly construct all five positive disjoint shell energies and ALL four parameter-score vectors, five-by-four nuisance X and source full-domain g0 derivative, with NO rounded-source inputs or finite differences.

**First exact old fold contained in (0.01861522133766,0.01861522134166):**
- source delta strict NEGATIVE in [-0.068407500077325,-0.068115531580802].
- source q strict POSITIVE in [1.1359374329253,1.1359410934595].
- with tau=sigma, rigorous *sigma² I_alpha,6* in [0.0021722161049960,0.0021908816216690].
- with tau->0, rigorous *sigma² I_alpha,6* in [0.0040844773283140,0.0041195808247810].
- display-only interval midpoints: delta≈-0.06826151582906355, q≈1.13593926319237, equal-noise sigma² I≈0.00218154886333.

**Second exact old fold contained in (0.05416739905600,0.05416739906000):**
- source delta strict NEGATIVE in [-0.832958935899302,-0.832709442884505].
- source q strict POSITIVE in [7.7623305978076,7.7623688268024].
- with tau=sigma, rigorous *sigma² I_alpha,6* in [0.07913442471721,0.07918219715062].
- with tau->0, rigorous *sigma² I_alpha,6* in [0.08932904783843,0.08938302487277].
- display-only interval midpoints: delta≈-0.8328341893919034, q≈7.762349712304996, equal-noise sigma² I≈0.0791583109339.

Complete original 75-digit strict interval endpoints, positive Gram-minor sums and six tau/sigma choices for each source bracket are in ACTUALLY EXECUTED rot028_results.json, SHA256 fbd42c3c75d1c1a6b0c3c7c2eaca60ed68a25be12ee1efd90f842498028d015e. Human display decimals are not proof decisions; all strict signs sourced in original interval arithmetic.

A useful display-only statistical interpretation: with tau=sigma, conditional local Gaussian standard-deviation lower limits on alpha scale roughly 21.41*sigma at first fold and 3.55*sigma at second fold. Even as tau tends to 0 they remain roughly 15.61*sigma and 3.35*sigma respectively. For illustrative sigma=1e-4, the equal-noise local lower-bound scales about 0.00214 and 0.000355 in alpha, NOT a predicted real instrument error or a nonlinear finite-sample guarantee.

## 4. Separate independent 3D spatial FFT statistical crosscheck

An independently authored source-data-only NUMPY checker reconstructs the ORIGINAL 41 sparse 3x3 Fourier B modes and their four source derivatives in N41³ spectral cubes. It evaluates full spatial B and FOUR derivative fields via 3D inverse FFT, directly computes Frobenius real-space squared energy/6 and derivative energies on the actual fixed [k:N-k]³ cubes, then constructs the five shell raw log scores. It does NOT use the original M13 source inner/window_mode method to compute observation energies.

At midpoint of each source fold interval, this independent binary64 checker:
- calculates q from a separately coded numeric inverse of X^TX;
- calculates delta from separate numerical least-squares projection of target alpha score on X plus original k0 source full-FFT energy derivative;
- directly calculates full six-output efficient Fisher by projecting the 6x1 target score orthogonally off the 6x4 nuisance matrix;
- checks all three numbers strictly fall within the original source iv75 bracket enclosures and rank-one update matches the direct six-output projected information.

First midpoint independent FFT q≈1.13593926319079, delta≈-0.06826151525369, sigma² I≈0.00218153884103.
Second q≈7.76234971228326, delta≈-0.83283418907030, sigma² I≈0.07915830904491.
The original full-domain translation score is numerically zero to <1e-12, agreeing with source exact Fourier Parseval invariance.
These independently constructed Float64 controls are DIAGNOSTICS, not the original source-directed proof. A difference in last few interval midpoint display digits is expected from interval dependency (the source enclosures contain the independent values).

## 5. Prior exact-pair separation and real noise guard

Prior source-original ROT027, now cryptographically pinned, strictly distinguished each exact prior Geeky ROT026 B root in its ENTIRE certified 5D box by SIXTH log-energy:
 r1 |Delta6|≈5.46094225750019e-8;
 r2 |Delta6|≈6.66265741796117e-7.
These values are mathematical log-energy differences, extremely small. In a separate FIXED-BINARY-HYPOTHESIS experiment in which old five predicted means coincide exactly, an independent sixth-channel Gaussian noise tau yields signal separation |Delta6|/tau; the source data do not assign tau. This is a different conditional question from local continuous alpha Fisher profiling and must NOT be conflated.

If the new full-domain observation is a derived function of overlapping noisy old measurements, the independent-noise assumption fails and the above numeric Fisher formula MUST be revised for the full correlated covariance. The original true six-output source Jacobian full column rank from ROT027 remains a source mathematical fact, not an instrumentation prescription.

## 6. Full reproducibility, fail-closed source integrity and transparent timeout

USER LOCAL complete executable ZIP:
 Geeky_S12_ROT028_sixth_channel_conditional_Fisher_noise_budget.zip
 bytes 36,873
 SHA256 2a56026ff2b92d8098df0db60904a6ed01f9bf582d3efe9211f1ef576ac0df48.

15 entries, 14 SHA256-manifest payload files, CRC PASS, 15/15 exact member byte readback PASS and all 14/14 SHA256 payloads PASS. Original public M13 code, B25 table, original ROT025/026 input proof data, original ROT027 source verifier and complete directed result, new executed iv75 original-M13 helper program and full result, new independently authored NumPy FFT program and full result, separate replay/tamper controller and actual receipt, README and manifest included.

Actual new main original source Python SHA256 b229e0732953f6793d1480004a9575bf4a4da67192bd1c72f561c0e8dfc96136; actual iv75 output JSON SHA256 fbd42c3c75d1c1a6b0c3c7c2eaca60ed68a25be12ee1efd90f842498028d015e. Independent spatial JSON SHA256 23fde17e1f8b2c098a2e6d8cbe2ad184c354a8decab903d238c13c1649231834. Source negative/cold replay actual receipt SHA256 d95c84cebf2d3394c05c92863c616ae19bfb1fed8ee9a6717f5d9489bdd77bbe.

Two actually produced COMPLETE source and independently computed FFT output JSONs in a fresh isolated temp-directory were compared with archive originals, BYTE IDENTICAL both. SIX one-byte input mutations were tested separately across both programs: M13 original code, M13 B table and prior ROT027 source-result JSON for primary; M13 original code, M13 B data and ROT028 primary result JSON for FFT checker. Each fail-closed with SOURCE_IDENTITY_MISMATCH BEFORE original source import: 6/6 PASS; originals untouched.

**Execution honesty**: the first monolithic combined replay+all-tamper controller exceeded its runtime cap AFTER it generated both exact cold output JSONs but BEFORE controller completion. It is NOT marked PASS. A separate lightweight controller inspected the surviving concrete cold output file bytes and completed all six input mutation controls; this receipt is included. In a new computer, run the two scientific programs separately then compare their complete JSON bytes. The quick receipt itself is not a portable full cold-replay tool; it refers to completed temporary outputs from this source execution. No false claim that the executable itself is separately mirrored publicly as exact bytes; full scripts and strict endpoints reside in user ZIP.

## 7. Limitation, status, bounded next reviewer

The source is ORIGINAL PUBLIC M13 AUXILIARY N41 B ONLY, not byte-identical historical full dtc0a_runtime_v0_3_1.py (still MISSING). The input field translations and gain are EXPLICIT HYPOTHETICAL EXTRA knobs, the sixth full-domain scalar is mathematically defined in original helper but NOT known historically independently measurable, and old/new Gaussian noise/covariance assumptions are synthetic. No physical K/J3/TPE/GR/GW, no detector precision, global six-channel inverse uniqueness, general mathematical novelty, BW exact ingestion or owner M15 CANON decision.

M13 original source FIRST; Geeky ROT027 first mathematical sixth-channel local lift and two exact old box source distinctions; M15 ROT019 first four single-nuisance fixing gates; Geeky ROT028 first this source-specific conditional rank-one noise propagation and finite-information ceiling calculation inside this chain. Independent REC12/AUD2/M15 I1 for new ROT027/028 is PENDING; an FFT crosscheck in same cell is NOT an independent different-cell I1 referee. KN14 BW source ingest unverified.

A bounded independent audit would source-fetch original M13 and rederive full original five shell scores and global k0 score independently at the TWO old fold alpha brackets, certify q via positive Cauchy–Binet minor sums and the full 6-output Schur complement under stated independent Gaussian variances, compare direct six-output spatial numeric score, and recheck that tau->0 leaves a finite sigma-limited information value. No endless root scanning or physical interpretation without source.

FINAL:
 ORIGINAL_M13_BYTE_IDENTITY_AND_ACTUAL_SOURCE_IV75_EXECUTION_PASS /
 TWO_WHOLE_FOLD_BRACKETS_SOURCE_STRICT_POSITIVE_Q_PASS /
 TWO_WHOLE_BRACKET_CONDITIONAL_FISHER_AND_FINITE_TAU_ZERO_CEILING_PASS /
 ALTERNATIVE_GRAM_CAUCHY_BINET_INTERVAL_AGREEMENT_PASS /
 INDEPENDENT_NUMPY_N41_CUBED_SPATIAL_DIRECT_FISHER_CROSSCHECK_PASS /
 TWO_COMPLETE_COLD_RESULT_JSONS_BYTE_IDENTICAL_AND_SIX_MUTATIONS_FAILCLOSED_PASS /
 MONOLITHIC_CONTROLLER_TIMEOUT_NOT_COUNTED /
 USER_ZIP_CRC_SHA_BYTE_READBACK_PASS /
 ROT027_ROT028_DIFFERENT_CELL_REFEREE_PENDING / BW_PENDING /
 NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
