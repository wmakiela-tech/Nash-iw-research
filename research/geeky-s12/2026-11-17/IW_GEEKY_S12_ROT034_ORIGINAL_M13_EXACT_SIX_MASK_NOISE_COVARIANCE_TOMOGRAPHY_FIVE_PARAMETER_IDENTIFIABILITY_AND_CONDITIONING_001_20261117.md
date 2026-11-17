---
artifact_id: IW_GEEKY_S12_ROT034_ORIGINAL_M13_EXACT_SIX_MASK_NOISE_COVARIANCE_TOMOGRAPHY_FIVE_PARAMETER_IDENTIFIABILITY_AND_CONDITIONING_001_20261117
date: 2026-11-17
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
exposure: PUBLIC
source_first: M13_ORIGINAL_PUBLIC_N41_B_FOURIER_TT_CODE_AND_B25
science_status: AUTHOR_NEW_SYMPY_EXACT_RATIONAL_FIVE_PARAMETER_NOISE_COVARIANCE_TOMOGRAPHY_PASS / 16_LINEAR_FALSIFICATION_CONSTRAINTS_PASS / SEVERE_NUMERICAL_ILL_CONDITIONING_PASS / INDEPENDENT_N41_CUBED_FULL_FOURIER_COVARIANCE_CHECK_PASS / EXTERNAL_I1_PENDING
prior_reviews: M15_ROT026_PRIOR_GEEKY_ROT031_AND_ROT032_I1_PASS / M15_ROT026_FIRST_AXIS_BODY_ANISOTROPY_MIXING / M15_ROT027_FIRST_TWO_MIXED_U_SHAPED_FISHER_CURVES_AND_BASELINE_CROSSINGS
sync_status: GITHUB_PENDING_NATIVE_BW_INGEST
claims: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT034 — exact five-parameter noise covariance tomography on M13's original six spatial regions; 16 falsifiable equalities and a severe conditioning obstruction

## 0. Source and scientific novelty boundary

M13 FIRST original public N41 Fourier/TT B operator and fixed nested observation cube masks. ORIGINAL native public Python is 8,970 bytes, immutable Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679; ORIGINAL source B25 JSON is 7,501 bytes, blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0.
Original source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py
Original coefficients:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-26/direct_B.json

Geeky ROT031 FIRST original six AXIAL-neighbor mask geometry, with a specific correlated-noise Fisher decrease. Geeky ROT032 FIRST original BODY-diagonal mask geometry and strict Fisher increase across two independently reviewed original source folds. NEW M15 ROT026 independently reviewed BOTH previous findings nonblind I1 using ACTUALLY executed unchanged original M13 and FIRST derived mixed AXIAL/BODY anisotropy thresholds. M15 ROT027 then FIRST independently proved TWO distinct U-shaped Fisher curves and two baseline crossings for appropriately chosen fixed axis/body mixtures. This work does NOT claim any of those earlier discoveries.
M15 source precedent:
https://github.com/wmakiela-tech/Nash-iw-research/blob/5a6d814efbf26a658bbc5bb0a004c82ca01de745/research/m15/2026-11-17/IW_M15_ROT027_ORIGINAL_M13_NONMONOTONE_MIXED_SITE_FISHER_IV55_TWO_UTURNS_REFEREE_001_20261117.md

Geeky ROT033 FIRST independently source certified the third elementary FACE-diagonal 12-neighbor geometry and one strict interior alpha-Fisher information minimum at the second fold. ROT034 shifts focus FROM local alpha Fisher TO an independent mathematical question: given an *ideal exact* full covariance of six source mask region means, can one identify the three elementary spatial correlation mechanisms themselves, the common site variance, and an independent new sixth-channel calibration variance? Are there exact covariance-data falsifiers? What is the numerical cost of inversion? The covariance statements below are hypothetical model math, not a claim of observed repeated experiments or actual noise.

## 1. Explicit synthetic site-noise class and six source regions

The ORIGINAL source N=41 periodic cube has 41^3=68,921 sites. Original fixed interior cube masks k=2,3,4,5,6 partition into five disjoint shells with site weights (7778,6938,6146,5402,24389). The previously unobserved OUTER complement has 18268 sites. Exact six disjoint region order is [OUTER, shell1, shell2, shell3, shell4, shell5], with
 w=(18268,7778,6938,6146,5402,24389), D=diag(w), e0=(1,0,0,0,0,0).

HYPOTHETICAL additive centered RAW SITE ENERGY-DENSITY Gaussian measurement noise has source-parameter-independent covariance
 Sigma_site = beta0*I + beta_axis*A_axis + beta_face*A_face + beta_body*A_body,
where each A is the normalized sum of respectively 6 axial, 12 face-diagonal, or 8 body-diagonal periodic nearest-neighbor shifts. Parameterize beta0=eta^2>0 and beta_i=eta^2*theta_i≥0; the sufficient declared source stress-test guard theta_axis+theta_face+theta_body≤0.4 ensures strictly positive site covariance by Fourier spectral eigenvalues in [-1,1]. A separate independent Gaussian RAW FULL-DOMAIN ENERGY-MEAN calibration error, with FIXED KNOWN MODEL family but UNKNOWN nonnegative variance beta_cal, affects only the mathematical sixth full-domain observation. This is a stochastic calibration variance parameter, NOT M15's freely fitted fixed unknown SIXTH mean calibration offset which annihilates alpha information.

Let E_axis,E_face,E_body be six-by-six exact ORIGINAL mask directed neighbor-count integer matrices and let C be the covariance of SIX DISJOINT region-mean raw energy readings. The exact five-parameter covariance template is
 C = beta0*D^(-1)
   + D^(-1)*(beta_axis*E_axis/6 + beta_face*E_face/12 + beta_body*E_body/8)*D^(-1)
   + beta_cal*(68921/18268)^2*e0*e0^T.

Here the raw SIX DISJOINT readings are simply an invertible linear transformation of the original five fixed shells plus the mathematical full-domain energy mean. Full global RAW energy is an original M13 mathematical helper observable, but **NO authenticated independent historical DTC0a physical sixth sensor or repeated noisy observations have been established**. Therefore the above is a structural identifiability theorem under assumed known covariance-family structure, NOT a demonstrated practical inverse experiment.

## 2. Exact source geometry: a three-basis polynomial structure at five region boundaries

A newly authored program actually reconstructs the ORIGINAL six M13 masks at ALL 68,921 sites and enumerates ALL 6, 12 and 8 directed one-step periodic shifts. It also INDEPENDENTLY rederives each FULL six-by-six integer E matrix from exact algebraic overlaps of centered k2..6 cube windows, with one, two or three shifted axes respectively. Both algorithms give exactly the same entire three E integer matrices. All three full matrices are in the actually generated machine result JSON inside the user ZIP.

For five adjacent-region pairs i,i+1, set
 y_i = w_i w_(i+1) C_(i,i+1),
 radii r_i=(37,35,33,31,29).

EXACT original M13 mask geometry yields:
 y(r)=beta_axis*r^2+beta_face*(2r^2-r)+beta_body*(3r^2-3r+1).
This expression is independent of beta0 AND beta_cal because neither produces any distinct-region cross-covariances. The exact 5×3 integer coefficient design matrix is

 [[1369,2701,3997],
  [1225,2415,3571],
  [1089,2145,3169],
  [ 961,1891,2791],
  [ 841,1653,2437]].

Original exact SymPy rational calculations:
 - rank of this 5×3 matrix is THREE;
 - determinant using original consecutive boundary rows 0,1,2 is EXACTLY -16;
 - among its ten three-boundary subsets, largest absolute determinant is 128, for rows (0,2,4), determinant -128;
 - because y(r) is a quadratic and r steps down by exactly 2, THIRD FORWARD FINITE DIFFERENCES must vanish in BOTH independent positions:
   y3-3*y2+3*y1-y0=0,
   y4-3*y3+3*y2-y1=0.

The last two identities are exact falsifiers of this THREE canonical neighbor-correlation covariance subfamily, not mere goodness-of-fit suggestions. The three beta coefficients are uniquely recovered from the quadratic polynomial coefficients A, B, C:
 beta_body=C, beta_face=-B-3C, beta_axis=A+2B+3C
for y(r)=Ar²+Br+C.

## 3. Five covariance parameters, 21 independent symmetric entries, 16 exact linear constraints

An actual EXACT SymPy rational basis computation constructs the 21×5 matrix of the upper triangular entries of the FIVE independent six-by-six covariance templates:
 D^-1, D^-1 E_axis D^-1/6, D^-1 E_face D^-1/12, D^-1 E_body D^-1/8, (68921/18268)^2 e0e0^T.
Its rank is EXACTLY FIVE. Therefore a full ideal SIX-region covariance identifies all FIVE parameters:

 1. Extract beta_axis,beta_face,beta_body using three independent scaled adjacent cross-covariances (5 give two redundant falsifiers).
 2. Recover beta0 independently from EACH of the five original shell diagonal variances; all five recovered values must agree.
 3. Recover beta_cal from the OUTER diagonal covariance after subtracting its beta0 and neighbor contributions.

The full SIX-by-SIX symmetric covariance has 21 independent entries and the 5D linear family has codimension SIXTEEN, with an explicit independent constraint decomposition:
 - TEN nonadjacent-region covariance entries are EXACTLY ZERO.
 - TWO exact third-difference identities for the five adjacent-region covariance moments.
 - FOUR equalities requiring the FIVE original shell diagonals to reconstruct the SAME beta0.

The five OLD-SHELL-ONLY covariance, consisting of 15 symmetric entries, has full template rank just FOUR: the fifth template beta_cal is ZERO there. Thus a distinct additional global/outer observation is necessary to recover its own calibration variance in this model. The 16 conditions are **necessary and sufficient for membership in the FIVE-DIMENSIONAL LINEAR SPAN**, NOT alone sufficient for the restricted physically interpretable cone beta0>0, nonnegative beta_i and beta_cal, theta sum ≤0.4 or positive covariance observations. Those inequalities must also be checked.

Exact full six-by-six rational source witness:
 beta0=1, beta_axis=3/25, beta_face=1/10, beta_body=2/25, beta_cal=1/2500.
Then original five adjacent scaled y are
 (37707/50,33709/50,5987/10,5277/10,23059/50).
The program EXACTLY constructs full rational C and recovers ALL FIVE inputs, confirms ALL sixteen constraints, and separately falsifies the model by injecting (i) a nonadjacent covariance, and (ii) a single adjacent boundary perturbation causing a nonzero third difference. This is an exact algebraic non-empirical synthetic test.

## 4. Crucial negative knowledge: exact identifiability is severely ill-conditioned

The 5×3 integer design's actual binary64 2-norm singular values are approximately
 (9095.47470373591, 7.135382927126389, 0.003261342062901448).
Its two-norm condition number is approximately **2,788,874.80317**, even though every three-row determinant needed for identifiability is nonzero. The nearly linearly dependent neighbor mechanisms are NOT reliably separable without extraordinarily precise covariance observations.

Using exact input beta=(.12,.10,.08) and only perturbing the FIRST of five scaled adjacent covariance moments by a *relative* 1e-8, the recovered input beta weights are:
 - first THREE CONSECUTIVE boundaries: (.12313910777,.09679773300,.08108878963), maximum component relative error ~**3.2023%**;
 - best available determinant-separated triple boundaries (0,2,4): (.12064761772,.09933800649,.08022553499), maximum relative error ~**0.6620%**;
 - all five boundaries, ordinary unweighted least squares: (.12076954599,.09921370133,.08026777356), maximum relative error ~**0.7863%**.

This is one precisely declared synthetic perturbation, NOT a confidence interval and NOT a universal ranking of statistical estimators: empirical covariance errors have a structured sampling covariance, generally non-isotropic and dependent on signal. These quantities explicitly bar the overclaim that exact 5-parameter rank implies practically robust estimator identifiability.

## 5. Actually executed original M13 and different-algorithm 41³ Fourier checks

The ACTUAL original M13 native module bytes and B25 bytes are verified at source Git blob level, along with preserved SHA256 exact prior original ROT031, ROT032 and ROT033 source result JSON inputs. After verification, ROT034 ACTUALLY IMPORTS and RUNS original unchanged M13 tensor_polys(41), all 41 original 3×3 tensor Fourier modes, ORIGINAL inner for each of FIVE fixed nested source masks and original unmasked k0. At alpha EXACT 1/20 with mpmath.iv.dps=38, the full B norm, all five disjoint shell energies and independent outer mean are STRICTLY POSITIVE. This verifies the original mathematical observation functions on which the mask geometry is defined. It does NOT claim that original M13 source has free t/b controls or experimental noise.

A SEPARATELY AUTHORED diagnostic does NOT import the primary geometry/tomography verifier and does NOT build neighbor graph by original-roll counting. It forms the FULL 41³ Fourier transforms of the six original spatial indicator masks, multiplies them by the three independent Gaussian site-noise Fourier power-spectrum symbols, and integrates back the region mean covariance. Five synthetic scenarios:
 pure axis, pure face, pure body, full mixture, same mixture with a distinct extra calibration variance.
All FIVE independent Fourier route 6×6 covariance matrices agree with exact integer-geometry source representation to maximum absolute difference of order 5.42e-20 in the declared test units; all five recover their synthetic five noise parameters within correct binary64 tolerance, including negligible residuals for weights that are exactly zero, and reproduce old5+global / six-disjoint covariance equivalence. The first preliminary check correctly FAILED a too strict 1e-10 absolute tolerance on near-zero coefficients of about 2e-10 generated by ill-conditioning; the final declared 5e-10 absolute tolerance was chosen and the entire program rerun successfully. The initial failed run is NOT a PASS.

This independent algorithm also reconstructs the original 41 mode M13 B tensor's nine matrix components on all 41³ original lattice sites by three-dimensional inverse FFT, and compares the spatial energy average with original UNMODIFIED M13 inner(k0): relative error about 1.1114e-16 (FLOAT diagnostic, not a proof of high-precision noise parameters). The full spatial original source energy equals the site-count-weighted sum of all six original region energies.

The original exact algebraic SymPy rank / polynomial constraints are the proof. Source-native outward intervals prove only original B observation positivity; independent binary64 Fourier results are same-cell diagnostics, NOT independent external I1.

## 6. Actually executed clean replay, source mutation and local full custody

User SELF-CONTAINED reproducibility ZIP:
 **Geeky_S12_ROT034_exact_M13_mask_covariance_tomography_and_ill_conditioning.zip**
 **50,245 bytes**, SHA256
 **2c287f4fdf57db25aaafe252cd2e6cdd1aee562fc605fbf4100b68d26b6af99e**.

13 archive entries, 12 manifest-pinned payload SHA256. ZIP CRC PASS, exact byte readback ALL 13/13 archive members PASS, all 12/12 SHA256 payload PASS. Contains UNMODIFIED ORIGINAL M13 Python and B25, frozen full original ROT031/ROT032/ROT033 source result JSON, new actually executed exact SymPy/original-M13 verifier Python and full exact JSON, new separate 41³ site-noise Fourier verifier and full numeric JSON, separate actual replay/tamper controller and receipt, comprehensive README, and SHA manifest.

The replay controller actually ran TWO fresh isolated clean Python -I subprocesses after copying each executable with exactly needed source bytes to separate TEMP directories. BOTH COMPLETE result JSON files were BYTE IDENTICAL to the original science results. EIGHT deliberately corrupted original source byte tests in disposable copies (the original M13 Python, B25 and previous entire source result JSON inputs; also new current theorem JSON for the independent check) each failed closed with SOURCE_IDENTITY_MISMATCH BEFORE original M13 scientific import; 8/8 PASS. Original inputs never modified.

The full actual runnable sources and complete exact rational/spectral results are in USER ZIP; this public Markdown and a separately created curated public JSON do NOT falsely claim the executable code was identically mirrored to public GitHub.

## 7. Hard stop and suggested bounded new referee

The mathematical sigma covariance family and exact five-parameter tomography are conditional on the original N41 MASK GEOMETRY and on an explicitly HYPOTHETICAL stationary normalized 6+12+8-site-neighbor Gaussian RAW energy measurement model with independent sixth RAW full-mean calibration variance. It requires knowing/estimating an actual full covariance of SIX observations across repeated measurements. NO such observations, covariance estimates or calibrated repeated measurement noise are authenticated in the project. The historical complete original dtc0a_runtime_v0_3_1.py byte-identical producer is MISSING; free source translations t, adjustable gain b and independently measured sixth energy are NONNATIVE. No actual alpha Fisher performance, physical K/J3/TPE/GW/GR, source hardware, global inverse uniqueness or general mathematics literature novelty.

M13 original code FIRST. Geeky ROT031/032/033 original noise-geometry FIRST as specified. M15 ROT026 FIRST axis/body mixture thresholds and their independent previous I1; M15 ROT027 FIRST two axis/body mixture U-shaped Fisher curves and baseline crossings. NEW ROT034 FIRST within lineage exact full six-region FIVE-PARAMETER covariance identifiability, 16 linear falsification guards, severe near-nonidentifiability estimate. **AUTHOR ONLY**; REC13/AUD3/M15 independent new ROT034 referee I1 PENDING. KN15 BW native ingested receipt not verified. M15 owner CANON and EXEC_SIGN not verified; GitHub writes and Slack dispatch are not receipts of scientific acceptance. NO automatic task cascade. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.

Bounded reviewer challenge: independently reconstruct all 3 original source mask E graphs, verify five adjacent 3-neighbor polynomial coefficient rows and EXACT det=-16 / rank3; prove 21×5 rank5, old-shell-only rank4 and exactly 16 independent linear covariance constraints; falsify at least one by independently perturbed exact rational covariance; independently assess near-collinearity and no real-data covariance overclaim.

FINAL:
 ORIGINAL_M13_GIT_BLOB_SOURCE_ACTUALLY_EXECUTED_K0_AND_FIVE_MASKS_PASS /
 THREE_SOURCE_GRAPH_EXACT_DIRECT_ENUMERATION_VS_SHIFTED_CUBE_PASS /
 EXACT_FIVE_BY_THREE_QUADRATIC_BOUNDARY_TOMOGRAPHY_RANK3_PASS /
 FULL_SYMMETRIC_SIX_COVARIANCE_TEMPLATE_21_BY_5_RANK5_PASS /
 ORIGINAL_OLD_FIVE_ONLY_RANK4_AND_16_INDEPENDENT_LINEAR_FALSIFIERS_PASS /
 EXACT_RATIONAL_FIVE_PARAMETER_CONSTRUCTIVE_RECOVERY_AND_NEGATIVE_CONTROLS_PASS /
 SEVERE_CONDITION_NUMBER_2p788874E6_AND_PERTURBATION_COUNTEREXAMPLE_PASS /
 FIVE_OF_FIVE_SEPARATE_FULL_41CUBED_SITE_SPECTRAL_COVARIANCE_REPRESENTATIONS_PASS /
 ORIGINAL_M13_41_MODE_FULL_FIELD_SPATIAL_FFT_CROSSCHECK_PASS /
 TWO_OF_TWO_CLEAN_FULL_JSON_BYTE_REPLAYS_EIGHT_ONE_BYTE_TAMPERS_PASS /
 USER_ZIP_CRC_13_OF_13_BYTES_12_OF_12_SHA_PASS /
 NEW_ROT034_DIFFERENT_CELL_I1_PENDING / BW_PENDING /
 NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
