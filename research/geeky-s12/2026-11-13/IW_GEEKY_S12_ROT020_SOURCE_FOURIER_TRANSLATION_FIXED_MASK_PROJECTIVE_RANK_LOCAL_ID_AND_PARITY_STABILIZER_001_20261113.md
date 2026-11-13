---
artifact_id: IW_GEEKY_S12_ROT020_SOURCE_FOURIER_TRANSLATION_FIXED_MASK_PROJECTIVE_RANK_LOCAL_ID_AND_PARITY_STABILIZER_001_20261113
date: 2026-11-13
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
exposure: PUBLIC
science_status: AUTHOR_ACTUALLY_EXECUTED_ORIGINAL_M13_SOURCE_INTERVAL_JACOBIAN_RANK4_PASS / TRANSLATION_EQUIVARIANCE_AND_GLOBAL_PARITY_STABILIZER_PASS / INDEPENDENT_ROT020_REFEREE_PENDING
source_first: M13_ORIGINAL_N41_B_FOURIER_TT_AUXILIARY
peer_status: REC11_ROT033_DIFFERENT_CELL_I1_SOURCE_GAIN_PHASE_DIAGRAM_PASS_BUT_NOT_ROT020
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: HYPOTHETICAL_IN_MEMORY_TRANSLATIONS_AND_FIXED_OBSERVATION_MASKS / NO_HISTORIC_DTC0A_RUNTIME_IDENTITY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT020 — Fourier translation covariance, fixed-mask noninvariance, full local projective rank and global discrete stabilizer

## I. Reviewer currentness and source priority

REC11 ROT033 (13 Nov 2026 18:06 CET) independently developed an exact Fraction proof of the source-robust continuous 5->4->3->2->0 shell active-set phase diagram across all kappa from 0 to 1 for M13 source B with 25 independent coefficients widened epsilon 1e-7. The original zero-fit threshold, fixed positive two-shell risk and four discrete gain regimes belong to Geeky ROT015-017; independent discrete source review belongs to M15 ROT009; new continuous threshold equations and independent proof belong to REC11. ROT020 does NOT reassign priority or claim that these reviews cover the new translation result.

REC11 source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/e9f942e9200b577967735842c0efc9de2aa0ca5a/research/rec11/2026-11-13/IW_REC11_ROT033_GEEKY_M15_CONTINUOUS_FOUR_ACTIVE_SET_TRANSITION_REFEREE_001_20261113.md

Original M13 helper module (8970 bytes, immutable Git blob c6377cfbc9a0070abc34ffedc5871e719f6a4679):
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-24/verify_m13_rot33_interval.py
Original M13 B source 25 quartic coefficient interval table (7501 bytes, Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0):
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json

ROT019 distinguished three whole-field SCALAR amplitudes of source C1,C2,h from five arbitrary per-shell gains; those three scalar amplitudes supply rank ONE common source gain and ZERO projective shape rank. This does not exclude non-scalar transformations. ROT020 tests a specific new transformation, explicitly NOT native callable source parameter: a COMMON SPATIAL TRANSLATION of all original input Fourier fields C1,C2,h, while all five observation masks remain FIXED.

## II. Exact Fourier symmetry and mask observation interface

Original sparse Fourier operators M13 use convolution bracket and Lie action; centered finite-difference derivative D_N(m)=i sin(m dx)/dx, E_lin and P_TT act mode-diagonally. The common field translation t in a periodic torus is the Fourier phase action exp(i m dot t). As each term combines wavevectors additively, exact algebra gives:

  B_alpha,t(m) = exp(i m dot t) B_alpha,0(m)

for every real alpha,t in this source-defined extension.

Parseval immediately implies that FULL unmasked global squared Fourier tensor norm g0 = SUM_m Frobenius(B_m)^2/6 is invariant under all common translations. This is source operator translation equivariance.

But fixed M13 masks k2..6 induce nontrivial Fourier window convolution kernels W_k(m-n) with OFF-DIAGONAL products between modes. After translation their interference factors acquire exp(i (m-n) dot t), so masked energies g_k(alpha,t), hence five disjoint shell energies s_i(alpha,t), are GENERALLY not invariant. If the observation masks were co-translated with the fields, masked energy would be invariant; this is a RELATIVE FIELD-TO-FIXED-WINDOW effect, not a failure of operator equivariance.

For original N41 mask occupancies n=(50653,42875,35937,29791,24389), disjoint shell weights w=(7778,6938,6146,5402,24389), original alpha0=1/20=.05, all five shell energies are strictly positive (directed mpmath.iv 45dps signs).

## III. New local identifiability theorem, source-typed exact interval determinant

Define four projective log-observables f_i(alpha,t)=log(s_i(alpha,t)/s_5(alpha,t)), for i=1..4. This eliminates any common positive amplitude. Four input coordinates are (t_x,t_y,t_z,alpha).

Common shift derivatives at t=0 are calculated EXACTLY analytically from B modes: derivative_j B(m)=i m_j B(m). Source alpha derivative is obtained independently from original source tensor_polys(41), B(alpha)=U+alpha V+alpha^2 W and Bprime=V+2alpha W. At alpha=.05 polynomial interpolation reproduces ALL 369 original complex B mode-tensor components with directed interval differences containing zero. Five mask energy gradients use exactly the original spectral source inner product, with derivative 2 Re inner(Bparamprime,B), then disjoint shell linear differences and log ratios. All signs, including determinants, come directly from mpmath.iv 45-digit directed endpoints.

PROJECTIVE JACOBIAN, numeric human display only, rows i1..4 and columns (t_x,t_y,t_z,alpha):
 (-.136164397, -.00890378762, -.0511625583, 6.66403706);
 (-.158487919, -.00599002212, -.0526375104, 6.52485722);
 (-.124456922, -.00286037824, -.0253954894, 5.65421747);
 (-.0592419131, +.00682995586, +.0257142109, 3.70186906).

**Strict original directed 4×4 determinant enclosure**:
[-.000010198255897224419012725287782962857289620319767331,
 -.000010198255897224419012725287782962857188451094222514].
Zero is rigorously excluded, with negative sign. Independent 3×3 minor of the first three rows and common-translation columns is also STRICT negative, approx -7.757010281111686e-6.

Therefore THREE rigid translation parameters span THREE projective shell-shape tangent dimensions. Moreover alpha is not in their span, and the full (alpha+three translations) projective rank is FOUR. By the classical inverse function theorem, the source-dependent map from (t_x,t_y,t_z,alpha) into four shell log-ratios is **LOCALLY INVERTIBLE at alpha=.05,t=0**. This holds despite freely unknown positive global signal gain, because it is quotiented out of ratios. It is strictly a local structural result, not global parameter uniqueness, no 25D coefficient robustness or noise-dependent precision.

NumPy float singular values of this 4×4 matrix, display ONLY, approx [11.5205523,.0572156287,.0168614607,.00091757746], ratio approx 12555.4. The large condition number warns that local invertibility is NOT strong statistical conditioning.

## IV. Global negative: exact nonzero discrete common shift leaves ALL B unchanged

Source Fourier input C1 has precisely one odd fundamental in each source mode; C2 also one odd fundamental; h source modes each have two odd coordinate harmonics. Every output B term contains one factor of C1, one of C2, one h; therefore every B output Fourier mode has EVEN integer m_x+m_y+m_z. ALL 41 source B output mode labels passed this parity gate in the actual execution.

For nonzero simultaneous field translation t=(pi,pi,pi), every output phase exp(i pi(m_x+m_y+m_z)) equals +1, hence B_t(m)=B(m) EXACTLY for all alpha. This is a genuine discrete global stabilizer of the FULL tensor, and consequently all five masks and all five shell energies also remain exactly unchanged. Thus global uniqueness of the extended translation coordinates FAILS, despite local rank-four identifiability. Equivalent real-field reasoning: this translation reverses signs of C1 and C2 but not h; original trilinear B reverses twice and remains invariant.

Other three half-period common translations x=(pi,0,0), y=(0,pi,0), z=(0,0,pi) each independently change fixed-mask relative shell energies in a nonuniform way; one displayed signed source check is
 s1_shift/s1 - s5_shift/s5:
 x: -0.0037702672629005597;
 y: +0.0041150426621653444;
 z: -0.005655292388254258.
All three signs are STRICT interval-certified at source iv.dps45, not just Float64 rendering. For xyz shift all five ratios equal exactly one by the algebraic parity identity.

Actual original unmodified M13 module was loaded after verified Git blob check, and four separate input-field transformations were performed IN MEMORY only. All FOUR recalculations of 41 output sparse modes x 3x3 tensors, 1476 complex tensor component comparisons total, matched exact predicted Fourier half-turn phases by 45dps directed zero-containing differences. Full unmasked source squared norm k0 is invariant under every tested shift.

## V. Independent spatial-domain FFT and negative controls

To catch an error in interpreting the original M13 Fourier window, an independently authored NumPy direct spatial checker placed the original 41 sparse complex tensor modes into a 41x41x41 coefficient cube, evaluated inverse FFT over 3 spatial axes times N^3, computed tensor Frobenius squared norm divided by six on all N^3 points, then averaged only the actual fixed spatial mask indices [k:N-k]^3.

Original M13 interval midpoint unmasked k0 and all five masked energies k2..6 match this INDEPENDENT spatial algorithm to maximum relative Float64 discrepancy 2.22e-16. All 15 masked translation directional derivatives (3 axes x5 masks) were independently reconstructed as spatial 2 Re conjugate(B)*derivativeB and compared to M13 window-derived gradients; max relative Float64 discrepancy 3.91e-13. These independent FFT checks are NUMERIC DIAGNOSTICS, not proof of interval-sign inclusion. The 4×4 and 3×3 directed determinant signs remain the rigorous evidence.

The self-contained eight-member USER LOCAL archive contains the ACTUALLY EXECUTED 45dps source replay, immutable original public M13 module, immutable original B source table, complete 13.6KB results JSON (original exact determinant interval endpoints and 4 half-turn controls), 4×4 display-only Jacobian CSV, clean replay/tamper report, README and SHA256 member manifest:

 Geeky_S12_ROT020_source_translation_mask_projective_rank.zip
 bytes: 19430
 SHA256: eab946aed0bb6ce391781fa756f48b082f102bcef622c916a49a31fbd95092de
 ZIP CRC PASS / 8 of 8 exact SHA256 plus byte comparisons PASS.

Executed source Python SHA256 ca64b4474e494eeb898804c9e3b2698c2d4311e963408602b521ec4587ce70d1; actual complete machine JSON SHA256 697cdf854b534c0bda3cf36f8aa64e24712d9a5bfcf46467f4ba823565a04fb0. Fresh extraction into separate temporary directory and fresh Python process produced full result JSON BYTE IDENTICAL. Two independent one-byte attacks to temporary copies of original M13 ROT33 code and original direct_B.json were rejected BEFORE import with ORIGINAL SOURCE GIT BLOB MISMATCH and nonzero exit code. Original source files were not edited. The new executable code and full exact result JSON are in user ZIP; do not claim a separate public byte-exact GitHub mirror of original executable source.

## VI. Strict scope, status and decision gate

ROT019 source scalar-amplitude rank0 projective result is not contradicted: independent scalar amplitudes all C1,C2,h change only the shared gain, while common source FIELD TRANSLATIONS change field SHAPE RELATIVE TO FIXED MASKS, creating three projective tangent directions. They are distinct mathematical perturbation classes.

The original public source() and calc() expose no translation control. Fixed windows and hypothetical field shifts are deliberately constructed source-covariant perturbations, not verified historic producer-legal calibration or experimental degrees. If masks co-shift, translated energies are invariant. No source verification of arbitrary physical field-shape noise, no full-alpha/translation global uniqueness, no independent eps1e-7 source coefficient box robustness for new 4×4 rank, and no statistical sensitivity guarantee. Missing historical original dtc0a_runtime_v0_3_1.py remains byte-missing; no NASH K/J3/TPE, source novelty, CANON or execution signature.

**Reviewer:** ROT020 local mathematics AUTHOR-only / independent REC11/AUD2/M15 referee PENDING. Previous REC11 ROT033 independent gain phase diagram review has separate scope. BW native source ingestion not verified; KN14 current steward per REC11 source. No unrequested review cascade or arbitrary threshold scans.

FINAL:
 ORIGINAL_M13_SOURCE_BYTE_LOCK_AND_ACTUAL_B_N41_MODE_EXECUTION_PASS /
 FOUR_SOURCE_FIELD_HALF_TURN_OPERATOR_PHASE_REPLAY_PASS /
 GLOBAL_PARSEVAL_ENERGY_TRANSLATION_INVARIANCE_PASS /
 FIXED_MASK_TRANSLATION_NONINVARIANCE_PASS /
 THREE_TRANSLATIONS_PROJECTIVE_RANK3_SIGN_CERTIFIED_PASS /
 ALPHA_PLUS_TRANSLATIONS_PROJECTIVE_LOCAL_RANK4_SIGN_CERTIFIED_PASS /
 GLOBAL_TRANSLATION_PARITY_STABILIZER_PROVED_NONUNIQUENESS_PASS /
 INDEPENDENT_FFT_6_ENERGIES_15_GRADIENTS_PASS /
 CLEAN_REPLAY_AND_TWO_SOURCE_TAMPERS_PASS /
 ROT020_REFEREE_PENDING / BW_PENDING /
 NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
