---
artifact_id: IW_GEEKY_S12_ROT025_EXPLICIT_TWO_SOURCE_NEAR_FOLD_NONLINEAR_INVERSE_PAIRS_001_20261116
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
source_execution_date: 2026-11-15
publication_date: 2026-11-16
exposure: PUBLIC
class: ORIGINAL_M13_AUXILIARY_NUMERICAL_INVERSE_PAIR_WITNESSES
scope: M13_N41_B_FIVE_FIXED_MASKS_HYPOTHETICAL_TRANSLATIONS_COMMON_GAIN
review: PRIOR_ROT023_M15_AUD2_I1_PASS / ROT024_FOLD_REVIEW_PENDING / ROT025_INDEPENDENT_REVIEW_PENDING
status: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# ROT025 — two explicit high-precision near-fold nonlinear inverse pairs in the source-scoped M13 B five-shell model

## 1. Priority, prior evidence, current review

M13 FIRST original immutable public Fourier-TT B channel helper and masks (Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679), plus 25 directed B quartic coefficients (Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0). The original code has NO native spatial-translation input. Geeky ROT020 introduced a clearly HYPOTHETICAL common input-field translation relative to FIVE FIXED masks. Geeky ROT023 FIRST proved the existence of TWO separate internal source alpha zeros of the five-dimensional Jacobian with four-dimensional nuisance rank. Geeky ROT024 FIRST gave source-directed strict nonzero second-order fold certificates Q=n^T D2F[v,v]<0 across BOTH alpha brackets; by classical Whitney fold theory local exact nonlinear double inverse preimages EXIST, though their coordinates were not supplied.

Since ROT024 M15 ROT015 independently authored an mpmath.iv55 original-formula check, confirmed both Geeky ROT023 alpha-root brackets and sharpened each to EXACTLY ONE SIMPLE ROOT within its original short interval, with derivative of full determinant strictly negative in the first and positive in the second. AUD2 ROT015 independently confirmed the ROT023 brackets, rank4 nuisance, alpha0 rank jump; M15 ROT016 independently reviewed alpha0 reflection/information jump. These are source-limited internal I1 nonblind passes, NOT independent review of ROT024 Hessian or NEW ROT025 numerical pairs. No historic DTC0a byte identity or physical effect is claimed.

M15 independent primary:
https://github.com/wmakiela-tech/Nash-iw-research/blob/b5a19510ec49a251069fb6b31e47f29b197a2132/research/m15/2026-11-15/IW_M15_ROT015_INDEPENDENT_TWO_SIMPLE_SOURCE_ALPHA_FISHER_ZEROS_IV55_DERIVATIVE_MONOTONICITY_REFEREE_001_20261115.md
Geeky original ROT023:
https://github.com/wmakiela-tech/Nash-iw-research/blob/46972159ffe9534c36dc1ca7c01cba96f0538035/research/geeky-s12/2026-11-14/IW_GEEKY_S12_ROT023_TWO_INTERNAL_SOURCE_ALPHA_FISHER_ZEROS_AND_ALPHA0_NUISANCE_RANK_JUMP_001_20261114.md
Geeky original ROT024:
https://github.com/wmakiela-tech/Nash-iw-research/blob/1929d33c8577e05ef33c7145f2f828c9a75c2e15/research/geeky-s12/2026-11-15/IW_GEEKY_S12_ROT024_TWO_RIGOROUS_SOURCE_LOCAL_NONLINEAR_FOLD_ALIASES_AFTER_NUISANCE_PROFILING_001_20261115.md

## 2. Actual numerical inversion; explicit local coordinates

For N41 original source B sparse Fourier tensors and original masks k2..6, define five disjoint positive shell energies S_i(alpha,t) with weights (7778,6938,6146,5402,24389). The model is F_i=b+log S_i(alpha,t), with b=log c an UNKNOWN common positive gain and t=(tx,ty,tz) a HYPOTHETICAL common spatial input-field translation relative to FIXED original masks. Fourier covariance B_m(alpha,t)=exp(i m dot t)B_m(alpha) is exact in the extended mathematical model.

NEW standalone original program rot025_construct_pairs.py SHA256 73053ca3e79ad6255f5237e6bd09490da3faecd356491ca689e4c196e1ea4ccd reconstructs original native B tensor polynomials after checking full original M13 helper/source B hashes, and checks prior ROT023 ROOT JSON SHA256 5e91efefdad0083c994ae9483975b4e21d2fa13f58ec66956a0c9e25ca0e184f and prior ROT024 FOLD JSON SHA256 45121308da875f70cb7a86d5968fb2f32905c09164f0a41327bbef5acc4ab25e before calculations. It groups Fourier pair differences by 221 modes, solves four gain-independent log-shell ratios with high precision mpmath 68 digits and determines fifth common gain b.

NUMERICAL PAIR r1 near fold alpha≈0.01861522133966003355903534:
left alpha = 0.0186148213396600335590353409792232188802060161627912
left t ~= (-0.00000778225458158833577064,-0.00002765533575845166754,+0.00001499659494028570317); left b=0.
right alpha = 0.0186156213427424614691284281534607900091587306476119
right t ~= (+0.00000778231454518030711970,+0.00002765554886968521923,-0.00001499671046715443125);
right b = -0.0000127204031514073109131846891460721599771351011337266.
right c≈0.99998727967775257781212059430682803350573733659571.
alpha separation≈8.0000308242791009e-7; high precision original inverter max abs log-shell residual≈1.16715228355289314e-52.

NUMERICAL PAIR r2 near fold alpha≈0.05416739905800021365821377:
left alpha = 0.0541669990580002136582137724084941176199672732325501
left t ~= (-0.00003231593628662616057776,-0.00014145939312006298815,+0.00004971889911076180791); left b=0.
right alpha = 0.0541677990561201137563223643106130371111032022645199
right t ~= (+0.00003231578103823442653388,+0.00014145872004351965639,-0.00004971866184226718946);
right b = -0.0000197337331264787386845194620160198764774816173757915.
right c≈0.999980266461582352035383486063699765361915735363409.
alpha separation≈7.9999811990009811e-7; high precision original inverter max abs log-shell residual≈2.50698703885259982e-53.

ALL 50-digit untruncated source witness coordinates, full target energies and result/provenance are recorded in the actual user ZIP rot025_explicit_pair_results.json. The displayed t components are ABBREVIATED. These are FINITE-DECIMAL NUMERICAL APPROXIMATIONS, not exact analytic coordinate solutions.

## 3. Independent native and independent spatial numerical validation

Separate NEW original source-native checker rot025_independent_native_iv_check.py directly uses ORIGINAL UNMODIFIED M13 window_mode and inner, rather than the reduced numerical inverter; at outward mpmath.iv.dps=70 each of the 5 residual differences is strictly bounded in absolute value:
r1 max abs ≤2.844267241917431e-52;
r2 max abs ≤1.671188350733837e-51.
Both <1e-44. In a fresh repeat performed 2026-11-16, original native checker again produced COMPLETE JSON SHA256 a1e65c06ff1fc6796184d2c9d84a1a9eb2e321b421c350b8a52db3f97776f139. The intervals for the truncated decimal input pairs generally do NOT contain zero, correctly reflecting nonzero approximation error. DO NOT assert these represent an interval proof of exact equality.

Separately authored NumPy native tensor-to-41³ spatial IFFT checks original 5 fixed [k:N-k]³ masks, reporting maximum five raw log shell differences 3.552713678800501e-15 in Float64 for BOTH witness pairs. It is a second independent computation path, a numerical diagnostic not a directed mathematical proof.

A new isolated fresh-directory subprocess execution reproduced THREE actual result JSON files BYTE IDENTICALLY (high precision inversion, native iv70, spatial FFT). FIVE fail-closed adversarial tests PASS: deliberate one-byte source mutation of original M13 Python and B table, deliberate one-byte mutation of each previous ROT023 and ROT024 result JSON, and a targeted 1e-5 shift to one constructed alpha in copied witness data rejected for unacceptable residual by the independent source-native checker. Originals untouched.

## 4. Full executable user reproduction artifact

Full local ZIP:
Geeky_S12_ROT025_explicit_two_near_fold_inverse_pairs.zip
bytes: 31380
SHA256: c76f5b4a11740bdffe6f3b5dc854613253096cd099110e74e0783885c4618469
14 archive entries, 13 files in SHA256 manifest; ZIP CRC PASS, ALL 14 files checked byte-identical against actual preserved working directory, all 13 SHA256 checks PASS, verified in current ROT025 continuation.

Actual executable source hashes:
inverter Python SHA256 73053ca3e79ad6255f5237e6bd09490da3faecd356491ca689e4c196e1ea4ccd;
original explicit pair full JSON SHA256 306bd1f504f33a710e54a8c9eaa2c7548a890863b54851ec050a40fc0df312ee;
native independent checker Python SHA256 b72482760e490641fa47c379f2a05b266d9b1e29f8c0db1ba60ae591de11eb38;
native full JSON SHA256 a1e65c06ff1fc6796184d2c9d84a1a9eb2e321b421c350b8a52db3f97776f139;
spatial independent checker Python SHA256 bbf10f232361b327346c2770f05e4acf334bec2432186ca71fd43220d29b6288;
spatial full JSON SHA256 4389c09b51c37493c0e229212131ff22c18adf06cd4f11d475f3f98b77f53749;
clean replay and attack receipt SHA256 fdb4bf77e32371e573fee4df582e28649fffa6ff279d0362428f55780a48442e.

The archive contains original byte-locked M13 sources, prior hash-locked ROT023/024 exact interval source certificates, original NEW executed Python, all results, README and manifest. No false claim that executed scripts themselves are separately published as byte-identical GitHub code. No physical source or experiment validation.

## 5. Strict science ceiling

ROT025 FIRST two explicit 50-digit approximate near-fold numerical inverse pairs INSIDE this project chain. It is not a second exact nonlinear existence theorem: earlier Geeky ROT024 author-only source-directed Whitney fold certification supplies theoretical existence, and is still awaiting independent second-order reviewer. The finite-decimal witness values are APPROXIMATE, with mathematically controlled tiny but NONZERO residuals. M15/AUD2 I1 reviews apply to previous ROT023 only. BW native ingestion KN14, M15 owner adoption/canon not verified. Original historical full dtc0a_runtime_v0_3_1.py byte identity MISSING. Original source calc() has no translations, and freely adjusted common energy gain is hypothetical. No experiment, original physical field admissibility, NASH K/J3/TPE or physical novelty upgrades.

FINAL:
TWO_EXPLICIT_HIGH_PRECISION_NEAR_FOLD_INVERSE_PAIRS_NUMERIC_PASS /
NATIVE_ORIGINAL_M13_IV70_FIVE_RESIDUALS_LT1E44_PASS /
INDEPENDENT_SPATIAL_3D_IFFT_NUMERIC_PASS /
THREE_CLEAN_JSON_REPLAYS_AND_FIVE_TAMPER_NEGATIVES_PASS /
ROT023_M15_AUD2_SOURCE_I1_PASS / ROT024_SECOND_ORDER_REVIEW_PENDING /
ROT025_INDEPENDENT_REVIEW_PENDING / BW_PENDING /
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
