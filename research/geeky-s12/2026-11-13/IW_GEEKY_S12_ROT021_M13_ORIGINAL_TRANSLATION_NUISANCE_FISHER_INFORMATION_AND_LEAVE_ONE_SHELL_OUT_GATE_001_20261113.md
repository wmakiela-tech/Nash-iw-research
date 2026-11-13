---
artifact_id: IW_GEEKY_S12_ROT021_M13_ORIGINAL_TRANSLATION_NUISANCE_FISHER_INFORMATION_AND_LEAVE_ONE_SHELL_OUT_GATE_001_20261113
date: 2026-11-13
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
exposure: PUBLIC
science_status: AUTHOR_ACTUAL_ORIGINAL_M13_NATIVE_SOURCE_IV45_FIVE_LOG_SHELL_LOCAL_INFORMATION_AND_COFACTOR_GATE_PASS / ROT021_INDEPENDENT_REFEREE_PENDING
source_first: M13_PUBLIC_B_N41_OPERATOR / GEEKY_S12_ROT020_FIRST_FIXED_MASK_TRANSLATION_LOCAL_RANK4
prior_review: REC11_ROT035_AND_M15_ROT012_DIFFERENT_CELL_I1_REVIEW_ROT019_SCALAR_AMPLITUDE_RANK_ONE_NOT_ROT020_OR_ROT021
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: LOCAL_STRUCTURAL_HYPOTHETICAL_LOG_NOISE_METRIC_ONLY / NO_HISTORIC_DTC0A_RUNTIME / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT021 — source-native 5-shell sensitivity: 99.344% profiled information loss and any-one-shell deletion removes alpha's local information

## 0. Source firstness, new review and negative knowledge custody

M13 FIRST generated the original N41 Fourier TT auxiliary B source and 25 direct quartic coefficients. Original byte-identical source and original frozen B table were fetched, locked and executed by Geeky ROT011, subsequent source math original Geeky ROT019/020. ROT020 FIRST proved full local rank-four of alpha plus THREE hypothetical common rigid input translations (relative to FIVE fixed observation masks) modulo a common energy gain, and the exact nonzero discrete global translation stabilizer (pi,pi,pi). ROT020 did NOT assert robust estimation from noisy shell data.

NEW peer reviews REC11 ROT035 and M15 ROT012 independently confirm Geeky ROT019 scalar whole-field amplitudes rank ONE, but neither has reviewed ROT020 or ROT021:
- REC11 ROT035 independent source code inspection plus exact Fraction 25D box projective distance: https://github.com/wmakiela-tech/Nash-iw-research/blob/d801444618e72fc5c23ab43b5ce992def2c99d03/research/rec11/2026-11-13/IW_REC11_ROT035_GEEKY_S12_ROT019_NATIVE_FIELD_SCALAR_PROJECTIVE_REFEREE_001_20261113.md
- M15 ROT012 independent source formula mpmath45 plus hypothetical single-harmonic C1 shape knob: https://github.com/wmakiela-tech/Nash-iw-research/blob/e195953dc73f7d344f168a45c189eba27adddb33/research/m15/2026-11-13/IW_M15_ROT012_M13_ORIGINAL_OPERATOR_SCALAR_AMPLITUDE_VS_HYPOTHETICAL_FOURIER_SHAPE_RANK_GATE_001_20261113.md

ROT021's first new scientific issue is OBSERVABILITY/CONDITIONING: finite rank does not guarantee that alpha is estimated precisely if the common gain and three translation nuisance parameters are unknown. The result is SOURCE-TYPED and model-conditional: a HYPOTHETICAL independent equal-noise log-shell Gaussian observation model, NOT a physical device noise or legacy DTC0a producer statement.

## 1. Original immutable M13 operator and exact local data

Original M13 code source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-24/verify_m13_rot33_interval.py
Git blob c6377cfbc9a0070abc34ffedc5871e719f6a4679, 8970 original UTF8 bytes, SHA256 cd4aad089bf68e2e6155ff048d4d812943495dcf1770c8acbf0ff8111b1deb9c.

Original M13 direct B quartics:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json
Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0, 7501 bytes, SHA256 0295116e364e28e67f0129bda1fc298d6e4bfdcb7aa8a6314f02a9ea37edca5f.

Source N41 alpha=1/20, original B operator in mpmath.iv45, five fixed interior masks k2..6 with disjoint shell weights W=(7778,6938,6146,5402,24389). Introduce hypothetical common translation t of ALL C1,C2,h, observation masks fixed. From source Fourier covariance, at t=0:
 dB_m/dt_j = i*m_j*B_m;
 dB_m/dalpha = V_m+2*alpha*W_m, where B_m=U_m+alpha*V_m+alpha²*W_m from actually executed original M13 tensor_polys(N).

The original source M13 window-inner operator computes five masked energies and their 4 parameter derivatives; disjoint shell log derivatives form a rigorous directed 5x4 matrix D in five RAW log-shell measurements, columns (t_x,t_y,t_z,alpha), displayed only:

 row 1: (-0.0816386287,-0.00173771089,-0.0365310472,27.32524877)
 row 2: (-0.103962150,-0.001176? NOT USE approximate here; exact actual JSON contains +0.00117605461,-0.0380059993,27.18606893)
 row 3: (-0.0699311539,+0.00430569848,-0.0107639783,26.31542918)
 row 4: (-0.00471614460,+0.0139960326,+0.0403457246,24.36308078)
 row 5: (+0.0545257685,+0.00716607673,+0.0146315111,20.66121171).

For 45dps original-directed exact values, use complete local machine JSON inside attached ZIP, not rounded lines. The (possibly differing low significant digits) human matrix above is display-only; the computational source never hardcodes it.

## 2. Correct four-nuisance projection, no source/measurement confusion

Specify local measurement model (HYPOTHETICAL):
 y_i = b + log s_i(alpha,t) + e_i,
 b is one unknown common log-energy amplitude, t in R³ unknown small rigid field translation, and e_i independent N(0,sigma²), i=1..5.

The source nonlinear map is locally linearized at alpha=.05,t=0. Put X=[ones, D_t_x,D_t_y,D_t_z], the FIVE x FOUR nuisance Jacobian, and a=D_alpha, FIVE x ONE target score. Define five cofactors n_i=(-1)^i det(X with row i removed), i zero-based. Then n^T X=0 exactly by the alternating multilinear determinant identity. All five n_i have STRICT nonzero 45dps directed intervals:

 n1 ~= -9.649023239024407e-6;
 n2 ~= -3.3332593357871324e-6;
 n3 ~= +1.8493747494782042e-5;
 n4 ~= -7.757010281111686e-6;
 n5 ~= +2.2455453611411848e-6.

Therefore X rank4, and the one-dimensional nuisance orthocomplement is generated by n. The original FULL 5x5 Jacobian [X,a] has nonzero directed determinant n·a with strict NEGATIVE source interval approximately -1.0198255897224419e-5; independent previous ROT020 4x4 projective log-ratio determinant exactly same value to source interval. So a is NOT in nuisance span; inverse function theorem local alpha identifiability remains PASS.

The efficient alpha Fisher information after optimizing b,t is the classical Schur complement:
 I_alpha = sigma^-2 * [a^T(I-P_X)a]
         = sigma^-2*(n·a)²/(n·n).
From source original 45dps directed interval operations:
 I_alpha*sigma² lies strictly in an interval with midpoint 0.20335341746917431046305619... .
If t were KNOWN and only b unknown, the information is sigma^-2*SUM_i(a_i-mean(a))² with midpoint 31.0019294598589783107881566....

Thus **relative information**:
 0.0065593794003200510871...,
which equals roughly 0.65593794% of the alpha information under common gain alone, **information loss approx 99.34406206%**. The ratio of locally Fisher-limited alpha standard deviations is sqrt(31.00192945986/0.20335341746917) ~=12.347204016968868 (strict source interval positive).

For an illustrative HYPOTHETICAL log-error sigma=1e-4 per shell, the local Gaussian Cramer-Rao standard deviation scales:
 with unknown b and unknown t: at least about 2.2175543e-4 in alpha;
 with unknown b but known t: at least about 1.79599713e-5 in alpha.
These values are NOT empirical measurement precision, not finite nonlinear estimator error bounds and not source physical predictions. The strong reduction is an example of near-confounding nuisance geometry even though full rank remains positive.

## 3. Deterministic bounded-error local source gate

The SOURCE-local linear alpha displacement associated with arbitrary five RAW log-shell errors e is exactly
 d alpha_linear = SUM_i [n_i/(n·a)] e_i.

Its source interval coefficients display approximately
(+0.9461444522,+0.3268460185,-1.8134225775,+0.7606212630,-0.2201891562).

For a deterministic coordinatewise bound |e_i|<=epsilon, the EXACT first-order WORST CASE is epsilon times the source-certified L1 coefficient norm:
 |d alpha_linear| <= 4.06722346741028179... *epsilon.
This first-order bound is attainable by appropriate signs of the five errors in the linearized model, NOT a guaranteed nonlinear error bound at finite epsilon. It follows from the raw five log-shell error coordinates with their shared denominator shell, not from fictitiously independent errors on the FOUR ratios.

## 4. Strong five-channel necessity negative gate

Every one of the five 4x4 minors of X (delete one raw shell measurement) is strictly nonzero in source-directed iv45 intervals. Therefore after ANY ONE shell is dropped, the remaining FOUR measurements have an invertible FOUR-dimensional nuisance Jacobian X_{-i}. In their local linearization alpha's derivative a_{-i} belongs automatically to the span of these nuisance columns. Hence **alpha has ZERO efficient local Fisher information for every four-shell subset** when b plus all three independent translations remain unknown.

This is an exact source-specific local negative identifiability statement, not a global statement about nonlinear parameter uniqueness for a finite observational region. It reinforces that losing a single shell in this locally square five-measurement/five-parameter model removes the one nuisance-free scalar contrast. Claiming three shifts from a hypothetical source model is essential: if shifts are known or constrained, the conclusion changes.

## 5. Actually executed independent FFT cross-check and custody

NEW original author standalone Python code, mpmath 1.3.0 iv45 and NumPy, imported original unmodified M13 source ONLY AFTER Git blob verification, directly executed original calc(41,alpha) and tensor_polys(41), constructed source five disjoint shell logarithmic gradients, full source 5x5 determinant and cofactor null vector. The FULL 45dps directed source interval end points of alpha info, CRLB gains and 5 minors are in the deterministic local results JSON.

Independently authored direct SPATIAL FFT implementation places original 41 sparse complex Fourier tensor modes into full N41³ grid, inverse FFTs B and FOUR independently built derivative tensors, takes pointwise real Frobenius products, integrates over original five fixed spatial masks, and forms five disjoint shell gradients. All 20 log derivative entries match original m.inner Fourier window source numbers to MAX ABS difference 3.197442310920451e-14. The source 4x4 log-ratio Jacobian equals original ROT020 published result to max abs difference 1.7763568394002505e-15. These are NUMERICAL DOUBLE-PRECISION DIAGNOSTICS; strict information and 5 minor signs come from original source interval calculations and algebraic cofactor identity.

LOCAL USER reproducibility archive:
 Geeky_S12_ROT021_source_nuisance_profiled_alpha_information.zip.
 ZIP 23714 bytes, SHA256 b693accec39bebe2d95f0164105a4c2ca3f9b4ff313265a99d0aa68f4ae8da0a; ten files, ZIP CRC and exact ten-of-ten SHA256 byte-readback PASS.
 Includes actual executed original author Python source SHA256 fa528527a6896ff658fa7f8cdcb28ab705dd5845d9c9fa8bbd968f573b8e66bc, exact original 8970B M13 code and 7501B M13 B table, previous pinned ROT020 13624B result, full ACTUAL new 13868B iv45 source results JSON SHA256 91164578241f5167201bc235b5f272c1b8e124235e0bfb8ae383a27c129cdc8c, original console output, clean rerun/tamper script, actual control JSON, detailed README and SHA256 member manifest.
 Clean separate temporary-directory extraction and standalone Python result JSON byte-for-byte equal original PASS.
 Two negative source controls: deliberately change one byte in temporary copy of immutable M13 operator code and separately original B table: each must terminate nonzero with SOURCE_GIT_BLOB_MISMATCH BEFORE original source import/calculation. Both PASS, source originals preserved.
 The EXECUTED actual Python code plus original full exact endpoints are in this USER ZIP. This public report and a machine-readable summary are NOT falsely described as byte-for-byte mirrors of the actual executable Python.

## 6. Strict interpretation, no role collapse

ROT021 is original M13 PUBLIC AUXILIARY N41 B + ROT020 HYPOTHETICAL common input translations relative to fixed observer masks. The source() and calc() freeze original fields; no native translation parameter. Common amplitude is mathematically quotientable as in M13 source. The five log-shell independent equal-noise Gaussian model is explicitly new and synthetic: real mask/shell estimate errors may be correlated, heteroscedastic or distribution-free. Without source-legal measurement covariance, the numerical Fisher information ratio is conditional and cannot support a physical detector precision claim.

Neither local full-rank nor its noise sensitivity proves GLOBAL alpha uniqueness; ROT020 established a nonzero (pi,pi,pi) translation stabilizer. No source box eps1e-7 robustness of the NEW full translation Jacobian is claimed. Missing historical dtc0a_runtime_v0_3_1.py original bytes remain HOLD; no NASH K/J3/TPE/physical hardware transfer and no novel general Fisher/Schur mathematics assertion. Independent REC11/AUD2/M15 ROT021 referee remains PENDING; verified BW native ingest or M15 owner CANON acceptance absent. KN14 BW steward per REC11. Source original M13 FIRST, Geeky ROT020 translation source theorem FIRST, REC11/M15 ROT019 reviews FIRST, Geeky ROT021 first this explicit local information conditional test inside project.

No task cascade. No repeated epsilon/delta threshold factory.

FINAL:
 ORIGINAL_M13_PUBLIC_SOURCE_SHA_LOCKED_ACTUAL_N41_B_AND_DERIVATIVE_EXECUTION_PASS /
 FULL_FIVE_SHELL_FOUR_NUISANCE_COFAC_TANGENT_RANK_PASS /
 PROFILED_SOURCE_ALPHA_LOCAL_INFORMATION_PER_SIGMA2_0P203353_PASS /
 AMP_ONLY_31P001929_VS_SHIFT_NUISANCE_RETAINED_0P65594_PERCENT_PASS /
 GAUSSIAN_SD_INFLATION_12P3472_CONDITIONAL_PASS /
 ANY_ONE_SHELL_DELETION_ZERO_LOCAL_ALPHA_INFORMATION_PASS /
 FULL_SPATIAL_FFT_20_DERIVATIVES_CROSSCHECK_PASS /
 CLEAN_REPLAY_TWO_SOURCE_TAMPER_FAILCLOSED_PASS /
 INDEPENDENT_ROT021_REFEREE_PENDING / BW_PENDING /
 NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
