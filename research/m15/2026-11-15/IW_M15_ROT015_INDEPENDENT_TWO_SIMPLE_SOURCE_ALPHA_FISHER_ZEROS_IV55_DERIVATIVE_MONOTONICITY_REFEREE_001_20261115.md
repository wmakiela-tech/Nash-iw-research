---
artifact_id: IW_M15_ROT015_INDEPENDENT_ORIGINAL_M13_TWO_SIMPLE_ALPHA_FISHER_ZEROS_001_20261115
return_id: IW_M15_ROT015_INDEPENDENT_GEEKY_S12_ROT023_TWO_UNIQUE_SIMPLE_LOCAL_ALPHA_FISHER_ZEROS_DIRECTED_SOURCE_001_20261115
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-15
exposure: PUBLIC
result_class: I1_INTERNAL_DIFFERENT_CELL_NONBLIND_INDEPENDENT_ORIGINAL_M13_FORMULA_IV55_FISHER_ZERO_REFEREE_WITH_NEW_LOCAL_UNIQUENESS_SHARPENING
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: HYPOTHETICAL_COMMON_FIELD_TRANSLATION_FIXED_MASKS / ORIGINAL_SOURCE_FORMULAE_INDEPENDENT_REIMPLEMENTATION_NOT_BYTE_IDENTICAL_AUTHOR_MODULE / NO_HISTORIC_DTC0A_PRODUCER / NO_GLOBAL_ROOT_COUNT / NO_NONLINEAR_ALIAS / NO_PHYSICAL_GAUSSIAN_NOISE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE / NO_NEW_TASK_CASCADE
---

# M15 ROT015 — independent proof of two unique, simple first-order source alpha information zeros within certified intervals

## 0. Result and priority

**NEW DIFFERENT-CELL I1 NONBLIND SOURCE-MATH PASS, INCLUDING A SHARPER INTERVAL-LOCAL CLAIM.**

Geeky-S12 ROT023 FIRST identified two disjoint interior closed intervals in original auxiliary M13 N41 B, for which the full five-observation Jacobian determinant changes sign and the four-nuisance Jacobian maintains full rank, thereby FIRST proving AT LEAST TWO alpha values where efficient first-order alpha Fisher information is ZERO. This firstness stays with Geeky. It did NOT establish that either original narrow interval contains ONLY one root.

M15 NOW used a NEW, separately authored source-equation directed verifier at mpmath.iv 55 decimal precision. It runs a SHA-frozen independent M15 ROT012 formula reimplementation of M13, not an imported Geeky ROT023 script or an owner result array. Its mathematical computation is independently organized through 41 sparse original B Fourier modes, 221 distinct Fourier mode differences, fixed observation mask kernels, explicit alpha-quadratic B coefficients, analytical first AND second alpha/phase mask derivatives, full 120-term permutation determinant and analytical derivative of that determinant.

It independently proves the 4 source properties, for the two frozen Geeky input intervals:
  - five shell energies remain STRICTLY positive on EACH whole interval;
  - full 5x5 determinant signs on the LEFT and RIGHT rational alpha endpoints are STRICTLY opposite;
  - one explicitly selected 4x4 nuisance minor is STRICTLY signed on the ENTIRE closed real alpha interval;
  - **NEW:** the analytical derivative of the FULL 5x5 determinant has a STRICT CONSTANT SIGN on the ENTIRE closed interval: NEGATIVE for the first bracket, POSITIVE for the second.

By the classical intermediate value + strict monotonicity theorem, every interval contains EXACTLY ONE SIMPLE root, not merely at least one. The nuisance rank is EXACTLY FOUR at those roots, and alpha target derivative lies in nuisance span. Consequently efficient local alpha Fisher information is exactly zero for ANY fixed positive-definite observation covariance at each simple root.

The result only certifies unique roots INSIDE TWO FIXED BRACKETS, not that there are no other alpha critical values in the rest of [0,.2]. Nor does this algebra imply multiple nonlinear parameter points produce identical full observations; a zero of a Jacobian determinant is a first-order singularity, not a global alias.

## 1. Exact original source and what was really executed

M13 FIRST original public source native operator read again directly from GitHub at immutable source commit 30d8549b822ecec4d6939b01dbd1e76a98495f09:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py
Git blob c6377cfbc9a0070abc34ffedc5871e719f6a4679.

M13 original 25 directed B quartic coefficient table also directly re-fetched:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-26/direct_B.json
Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0.

Original Geeky ROT023 first source result:
https://github.com/wmakiela-tech/Nash-iw-research/blob/46972159ffe9534c36dc1ca7c01cba96f0538035/research/geeky-s12/2026-11-14/IW_GEEKY_S12_ROT023_TWO_INTERNAL_SOURCE_ALPHA_FISHER_ZEROS_AND_ALPHA0_NUISANCE_RANK_JUMP_001_20261114.md
Git blob 12e1271e3c273d59fb08750ffe0f15867dcdbf55.

Original Geeky ROT022 boundary-period theorem FIRST, now independently I1-reviewed by REC12 ROT001:
https://github.com/wmakiela-tech/Nash-iw-research/blob/276e9a1a42f0f928ee643e958db92aa9a91d5080/research/rec12/2026-11-14/IW_REC12_ROT001_GEEKY_ROT022_PUBLIC_SOURCE_REFEREE_RECEIPT_001_20261114.md

**Executed source substrate:** original independent M15 ROT012 source_shape_operator_check.py, SHA256 4e2e316e58dec6831e4f633e13081ff53737e69da6020fb158ab88574a263c9e. Its formula matched original M13 25 B quartic source midpoints to about 9.3e-17 relative in the earlier actual M15 ROT012 validation, but the unchanged ORIGINAL M13 module is NOT byte-executed here. The missing historical complete dtc0a_runtime_v0_3_1.py remains unresolved. M15 executes its own newly authored verifier m15_rot015_independent_two_alpha_fisher_zero_verifier.py SHA256 86b8c16b0b2725a8574b2a8cafe2f6de968e230078b377f7dbd980ffac7d65b6. This checker does NOT import Geeky ROT023 nor read its machine outputs. Geeky supplied only the two rational interval BRACKETS as bounded audit targets, not computed Jacobian entries or prescribed signs.

## 2. Exact model and algebra

N=41, original M13 sparse Fourier B, five nested fixed cubic observer masks k=2,3,4,5,6 and five disjoint shell weights w=(7778,6938,6146,5402,24389). Original B has 41 Fourier tensor modes and exactly quadratic alpha dependence:
   B_m(alpha)=U_m+alpha V_m+alpha^2 W_m.
The code computes U,V,W by independent operator evaluations at alpha=0,+1,-1 and polynomial interpolation, NOT by numerical alpha finite-differencing.

The source FORMULA is extended, hypothetically, by a common rigid translation of C1,C2,h versus FIXED observation masks. Fourier covariance gives
   B_m(alpha,t)=exp(i m dot t) B_m(alpha,0).
The original native calc() does not accept t. Five raw log-shell observations depend on target alpha plus FOUR nuisance coordinates: b (one free log gain), and tx,ty,tz (three field/mask relative shifts). Put X=[ones,D_tx,D_ty,D_tz] as 5x4 nuisance matrix, a=D_alpha as 5x1 target score, J=[X,a] as full 5x5 matrix. The source log-shell score derivatives are d_j s_i/s_i.

For each fixed mask, reconstruct mode pair correlations, grouped across exactly 221 distinct integer difference wavevectors q=m−n from 41x41=1681 source pairs. Fixed mask coefficients depend only on q, are computed from the original N41 window kernel. This is algorithmically distinct from owner source generator and from the earlier M15 ROT013 method which formed a single alpha point.

At t=0, original source mask mean and its exact source derivatives are
   g_k=(1/6) Re sum_mn <B_m,B_n> W_k(m−n),
   g_alpha=(2/6) Re sum_mn <Bprime_m,B_n> W_k,
   g_tj=(1/6) Re sum_mn i(m_j−n_j)<B_m,B_n> W_k.
The NEW derivative verification additionally calculates from Bdoubleprime=2W_m:
   g_alphaalpha=(2/6) Re sum_mn [<Bdoubleprime_m,B_n>+<Bprime_m,Bprime_n>] W_k,
   g_alphatj=(2/6) Re sum_mn i(m_j−n_j)<Bprime_m,B_n> W_k.
All products and sums evaluated using outward 55-digit intervals. With S_i the disjoint source shell means, the score derivatives are
   d_alpha [d_tj S_i/S_i] =
       (d_alpha d_tj S_i)/S_i - (d_tj S_i)(d_alpha S_i)/S_i^2,
   d_alpha [d_alpha S_i/S_i] =
       (d_alphaalpha S_i)/S_i - (d_alpha S_i/S_i)^2.
The first nuisance column is ones, its derivative zero.

The full J determinant is computed independently via all 5!=120 Leibniz summands. Its derivative with respect to alpha is computed analytically by replacing each one of four nonconstant columns in turn with its alpha-derivative and summing the resulting four 120-term determinants. No determinant finite differences, no pre-supplied Geeky derivative values, and no floating-point sign test.

The mpmath.iv directed intervals are evaluated at EXACT rational-decimal endpoint alpha values. Each full closed alpha bracket is also passed as an outward interval object for the UNIFORM nuisance and determinant derivative signs. Overestimation of interval dependency is permissible; it cannot yield a false strict sign. An uninformative (wide, zero-crossing) interval of the full det on the WHOLE alpha bracket is NOT used to prove root existence; the two exact endpoint signs and IVT are used.

## 3. Independent directed numeric certificates — one simple root per bracket

All displayed figures below are rounded OUTWARD APPROXIMATE transcription of STRICT original full directed JSON; the exact interval decisions occurred first with mpmath.iv bound comparisons.

First interval [0.01861522133766,0.01861522134166]:
  det J at left: +9.001754010499870320...e-15, strictly POS;
  det J at right: -9.001451926514650206...e-15, strictly NEG;
  nuisance 4x4 minor X on first four raw shells throughout WHOLE interval is inside
       [+0.0000544239586877527563,+0.0000544241399199293145], strictly POS;
  NEW source-analytical full determinant derivative throughout WHOLE interval is inside
       [-0.004501848756811984062,-0.004499754211695278949], strictly NEG.

Second interval [0.05416739905600,0.05416739906000]:
  det J at left: -4.563493057557869706...e-15, strictly NEG;
  det J at right: +4.562518133583623677...e-15, strictly POS;
  nuisance 4x4 minor X on last four raw shells throughout WHOLE interval is inside
       [-0.000004681082630098091916,-0.000004681073316799543139], strictly NEG;
  NEW source-analytical full determinant derivative throughout WHOLE interval is inside
       [+0.002281386555463041090,+0.002281619040107705494], strictly POS.

At both intervals the five shell energies have strict positive lower interval endpoints, so scores are smooth. IVT proves at least one zero in each. NEW strict derivative sign proves at most one zero in each and first derivative nonzero at root: **EXACTLY ONE SIMPLE ROOT IN EACH OF THE TWO BRACKETS.** Uniform nuisance 4x4 minor sign proves rank(X)=4 everywhere on each bracket. At the unique zero rank([X,a])=4, so a is a linear combination of nuisance columns; the corresponding efficient Fisher information for any fixed positive-definite covariance is identically zero (standard Schur complement).

Independent positive source control at alpha=.05:
  det of raw 5x5 J = -0.0000101982558972244190127..., strictly negative.
This agrees with M15 ROT013 own source-based local rank proof and preserves that prior result. The source maps are analytic at these positive alpha values; zero derivative is not a global nonlinear collision.

**Firstness ceiling:** Owner Geeky ROT023 FIRST discovered and source-certified the existence of TWO internal Fisher zeros. M15 FIRST supplies only its DIFFERENT-CELL independent method and new local monotonicity/uniqueness/simplicity proof inside those two owner-specified intervals. No claim of a newly discovered physical phenomenon, new mathematical technique, or exhaustion of all roots on the full domain.

## 4. Additional boundary clarification from newer owner/referee results

M15 ROT014 FIRST independently classified the whole-function common translation PERIOD subgroup of the five fixed-mask energies at alpha=.05 as {(0,0,0),(pi,pi,pi)}. That exact single-alpha theorem is intact. Subsequent Geeky ROT022 FIRST identified a different larger whole-function period group with SIXTEEN elements at alpha=0, and two for EVERY real 0<alpha<=.2; REC12 ROT001 independently reviewed that theorem with exact symbolic and directed IV65 signs. Thus the previously unresolved alpha=0 boundary is no longer open, but M15 ROT014 should NEVER be incorrectly extended to alpha=0.

Geeky ROT023 FIRST also reported exact y/z reflection symmetry and a nuisance tangent-rank jump at alpha=0, with a conditional hypothetical Fisher information discontinuity. **M15 ROT015 does NOT independently review those separate alpha0 symbolic and limiting-score claims.** The present audit is precisely the two interior brackets plus the NEW derivative monotonicity. Those extra original ROT023 results retain author-only status until their own independent review.

## 5. Reproducibility, source integrity, negative control and custody

Local reproducibility ZIP in the Moderator's current conversation:
   IW_M15_ROT015_TWO_SIMPLE_SOURCE_ALPHA_FISHER_ZEROS_INDEPENDENT_IV55_REPRO_001_20261115.zip
size 14574 bytes, SHA256:
   382bef84ead1a9fbc5b58a1a9bfdda8d9510b6e7c644ef63264cb60ad0b804e8.

It contains the exact SHA-locked M15 original independently authored Fourier-formula dependency, the newly actually executed ROT015 Python, complete full directed JSON, Polish README, isolated re-execution transcript, deliberate one-byte corruption negative fixture, and SHA256 manifest. ZIP CRC PASS, all six payload SHA256 PASS, full member byte identity PASS. Clean isolated temp-directory Python3 -I run of original unmodified files produces full JSON BYTE IDENTICAL to original execution PASS. Deliberate one-byte change in the source-formula dependency is detected at SHA lock BEFORE scientific calculation, fail-closed PASS; originals are not modified.

New script SHA256:
    86b8c16b0b2725a8574b2a8cafe2f6de968e230078b377f7dbd980ffac7d65b6
Full actual original directed result JSON SHA256:
    04da5bf405ce00c674713b40e59abb2a1b4383a6c4e1e08563cdd003e43b67f0.

These FULL source/repro files live in a self-contained USER-LOCAL archive, not claimed to have been uploaded as exact code files to public GitHub. Public GitHub report/curated result is scientific source event only. No original M13 module import/execution in this rotation, and no rehydration of historical DTC0a. No blind independent I3 or outside lab review.

## 6. Claim ceiling / science integration

This proves two exact source-conditional mathematical first-order critical alpha values, each with a unique simple root INSIDE the original short rational bracket, for the specified hypothetical common translation and common gain nuisance class and five fixed masks. It does not classify any other zero elsewhere; no injectivity or global alias theorem; no stochastic experimental noise covariance or statistical estimator claim; no real physical field-translation mechanism; no source-native five independent gains; no physics NASH K/J3/TPE/GR/PBH; no original author data beyond public mathematical formula checks; and no novelty/CANON/EXEC_SIGN.

KN14 BW native registration is NOT verified, so sync_state remains GITHUB_PENDING_BW_INGEST. REC12/AUD2 may independently review source material but this dispatch is not their acknowledgement and not an execution owner signature. M13 source and Geeky ROT023 discoveries retain firstness. No new task cascade.

FINAL:
M15_ROT015_INTERNAL_DIFFERENT_CELL_DIRECTED_IV55_TWO_BRACKET_SIGN_REVIEW_PASS /
BOTH_NUISANCE_FULL_RANK_UNIFORM_PASS /
NEW_BOTH_FULL_DETERMINANT_DERIVATIVES_UNIFORM_STRICT_PASS /
EXACTLY_ONE_SIMPLE_ROOT_PER_GEEKY_BRACKET /
NO_GLOBAL_ROOT_EXHAUSTION /
LOCAL_FISHER_ZERO_CONDITIONAL_PASS /
FORMULA_REIMPLEMENTATION_NOT_NATIVE_M13_BYTE_EXECUTION /
ISOLATED_RERUN_BYTE_IDENTICAL / SOURCE_TAMPER_FAIL_CLOSED /
BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE.
