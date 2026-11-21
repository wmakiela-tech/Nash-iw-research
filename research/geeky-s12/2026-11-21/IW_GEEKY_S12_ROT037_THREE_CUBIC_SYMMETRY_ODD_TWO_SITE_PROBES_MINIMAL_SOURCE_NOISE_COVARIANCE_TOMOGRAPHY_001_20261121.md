---
artifact_id: IW_GEEKY_S12_ROT037_THREE_CUBIC_SYMMETRY_ODD_TWO_SITE_PROBES_MINIMAL_SOURCE_NOISE_COVARIANCE_TOMOGRAPHY_001_20261121
date: 2026-11-21
origin: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
exposure: PUBLIC
source_first: ORIGINAL_M13_PUBLIC_B_N41_NATIVE_PY_AND_B25_GIT_BLOBS_VERIFIED_AND_ACTUALLY_EXECUTED
new_science_status: AUTHOR_ORIGINAL_M13_EXACT_SYMMETRY_THREE_2SITE_CONTRAST_COVARIANCE_RANK4_PASS / SOURCE_GAUSSIAN_WISHART_EXACT_RATIONAL_POSITIVE_PROFILE_PASS / INDEPENDENT_SAME_CELL_FULL_41_CUBED_9X9_FFT_PASS / DIFFERENT_CELL_I1_PENDING
review_currentness: M15_ROT029_PRIOR_GEEKY_ROT035_INDEPENDENT_I1_PASS / M15_ROT030_GLOBAL_SINGLE_REAL_RAW_SITE_FOURIER_KL_OPTIMUM_FIRST
sync_status: GITHUB_PENDING_NATIVE_BW_INGEST
claim_ceiling: ORIGINAL_PUBLIC_AUXILIARY_M13_B_N41_ONLY / HYPOTHETICAL_6_POINT_READOUTS_GAUSSIAN_ERRORS_AND_40M_IID_REPEATS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT037 — three minimal symmetry-odd two-site probes exactly identify four source site-noise mechanisms independently of all six original M13 mask averages

## 0. Original source, author priority, current independent review

M13 FIRST authored the public original N41 B Fourier/TT auxiliary operator and the five fixed observation cube masks. Its unmodified Python original (8,970 bytes, Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679) and original B25 JSON data (7,501 bytes, blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0) are verified byte-exact BEFORE original M13 scientific import. Both new science programs actually execute unmodified original M13 tensor_polys(41)[B]; the primary source executes ORIGINAL inner on all five k2..6 masks and unmasked full k0 with outward mpmath.iv.dps40 at exact alpha=1/20, all source energies strictly positive. Secondary source independently spatially synthesizes original 41 complex 3x3 B Fourier tensors on 41 cubed sites by 3D inverse FFT and checks original native k0 at ~1.11e-16 relative (double-precision diagnostic).

Original module:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py

Prior Geeky ROT034 FIRST demonstrated exact formal rank5 5-parameter covariance tomography from the six original mask means and 16 exact falsification constraints, with very severe covariance-boundary conditioning. Geeky ROT035 FIRST supplied two distinct legal EXACT rational synthetic Gaussian raw-site covariance models A/B that are nearly indistinguishable from six mask observations, even with identical fixed raw sixth calibration. **NEW independent M15 ROT029 (2026-11-17) independently source-native I1 PASS reviewed that ROT035 original core theorem**, and M15 FIRST independently extended its no-go uniformly over all common known nonnegative raw sixth calibration variances, including perfect zero calibration:
https://github.com/wmakiela-tech/Nash-iw-research/blob/8d060d5f20cef196e00b71618b15a859247facaa/research/m15/2026-11-17/IW_M15_ROT029_DIFFERENT_CELL_ORIGINAL_M13_EXACT_RATIONAL_ROT035_SOURCE_KL_AND_PERFECT_CALIBRATION_UNIFORM_NO_GO_001_20261117.md

Geeky ROT036 FIRST demonstrated a *single* two-site coordinate-swap-odd contrast whose Gaussian error is independent of the six old mask-average errors, and a separate hypothetical finite-sample two-known-hypothesis testing bound. Geeky ROT036 different-cell external I1 not independently verified. **M15 ROT030 (2026-11-19) already FIRST proved the globally optimal single RAW full-lattice real linear Fourier contrast for separating the same A/B hypotheses**, stronger globally in its distinct ONE-HYPOTHESIS-DISCRIMINATION task; M15 also supplied an independent two-quadrature sample bound. Its ORIGINAL firstness must not be assigned to ROT037:
https://github.com/wmakiela-tech/Nash-iw-research/blob/6f1681b99fc194c41354e5a65158fb6fed0addad/research/m15/2026-11-19/IW_M15_ROT030_ORIGINAL_M13_OPTIMAL_RAW_SITE_FOURIER_GAUSSIAN_LINEAR_CONTRAST_SOURCE_IV70_001_20261119.md

**NEW DIFFERENT QUESTION ROT037**: Find a MINIMAL cardinality collection of local coordinate-swap-odd two-site contrasts whose *own exact 3x3 covariance*, WITHOUT reading the six old region observations, determines **ALL FOUR** parameters beta0, beta_axis, beta_face and beta_body of the declared synthetic spatial site-error family. This is not optimum single KL discrimination and does not infer alpha.

## 1. Explicit source-mask geometry and hypothetical 6-point observer

ORIGINAL N41 periodic cube has M=41^3=68,921 points. Five original fixed disjoint cubic observation masks k2..6 partition the inner 50,653 sites in shell counts (7778,6938,6146,5402,24389), plus original OUTER complement 18,268. Region order [outer,shell1,...,shell5], occupancy vector w=(18268,7778,6938,6146,5402,24389).

The original region indicators are invariant under the coordinate permutation P:(x,y,z) -> (y,x,z). Select three precisely grounded site pairs, each wholly within original innermost region label5:

 Z0=E(9,19,20)-E(19,9,20).
 Z1=E(10,19,20)-E(19,10,20).
 Z2=E(9,20,21)-E(20,9,21).

Each signed site vector d_i=e_ai-e_P(ai) is P-ODD, while all six original coarse mask indicators are P-EVEN. Distances between the first endpoints a0,a1 give one AXIAL one-step link, a0,a2 one FACE two-coordinate one-step link, and a1,a2 one BODY three-coordinate one-step link. The nine cross-branch connections between any ai and any swapped bj are neither the same site nor one-step neighbors in ANY of those classes: this is ACTUALLY asserted from exact lattice integer positions in new executable code. The original M13 B SIGNAL energy need NOT be P-invariant: the following independence concerns Gaussian errors, not deterministic source means.

Entire error observer is HYPOTHETICAL: additive centered Gaussian RAW SITE ENERGY DENSITY noise with parameter-independent covariance
 Sigma_site=beta0 I+beta_axis A_axis+beta_face A_face+beta_body A_body,
where A_axis, A_face, A_body are normalized original N41 periodic operators averaging 6,12,8 signed one-site neighbor displacements, respectively. beta0>0, each beta_kind>=0 and sum beta_kind/beta0<=0.4 ensure strict site-covariance positivity. Additional independent random raw-full-sixth calibration variance beta_cal affects the old global/outer reading only; it does not affect Z. There is NO authenticated DTC0a raw pixel measurement hardware, source process noise, independent temporal replicates, actual Gaussian law or physical sixth sensor.

Because each site covariance generator commutes with P, the old six source indicator vectors are P-even, and the three contrasts are P-odd, their covariance is EXACT ZERO for all parameter choices in this source family:
 Cov(Z_i,old_region_j)=0,
 for i=0,1,2, j=0,...,5 and EACH of four basis generators I,A_axis,A_face,A_body.
New original-source verifier explicitly counts EXACT neighbor label memberships at each of the six source sites, obtaining **72 of 72 ZERO cross-covariance generator coefficients**, not just a heuristic symmetry argument. Full 9x9 Gaussian error covariance of (old6,new3) is therefore EXACT BLOCK DIAGONAL, including independently added sixth calibration. Since the joint error law is Gaussian, the entire new 3-vector is **STATISTICALLY INDEPENDENT** of the original six means. This fails for an arbitrary non-Gaussian site noise law even if zero covariance survives.

## 2. NEW exact three-by-three mechanism tomography, constructive inverse, minimality

With the stated original finite-support neighbor covariance, a contrast's two swapped sites are nonadjacent, giving Var(Z_i)=2 beta0 for every i. The three first endpoint pairs are, respectively, precisely axial, face and body linked, and the cross branches carry zero adjacency. Consequently EXACTLY:

 Sigma_Z =
 [[2 beta0,       beta_axis/3, beta_face/6],
  [beta_axis/3,   2 beta0,     beta_body/4],
  [beta_face/6,   beta_body/4, 2 beta0]].

All entries are RAW Gaussian site-energy-error covariances of three NEW mathematical observations; no noisy log-Gaussian assumption is needed.

An exact constructive rational inverse recovers each of the FOUR site covariance parameters from four matrix entries:
 beta0=Sigma_Z[0,0]/2,
 beta_axis=3 Sigma_Z[0,1],
 beta_face=6 Sigma_Z[0,2],
 beta_body=4 Sigma_Z[1,2].

New SymPy source constructs exact 6 upper-triangle elements by 4 parameter columns, verifies SOURCE EXACT rank4, and checks the explicit 4x6 left inverse on that matrix. In four specific RAW covariance coordinates [S00,S01,S02,S12] the forward linear diagonal scaling factors have magnitudes (2,1/3,1/6,1/4), so its elementary RAW-coordinate 2-norm condition number is exactly 12. This is NOT a universal empirical sampling condition, NOT a directly unit-matched comparison to ROT034 old five boundary-moment design 2.7888748e6, and NOT a Gaussian Fisher eigenvalue certificate.

**MINIMALITY restricted to this task:** A stand-alone 2-vector of any two scalar new contrasts can produce at most 3 independent entries in its symmetric 2x2 covariance, so a continuous four-parameter site covariance law cannot be fully locally identifiable from those new observations ALONE. Three contrasts have 6 independent covariance entries, and the explicit construction achieves exact rank4. Therefore three is minimal *for new-probe-only four-site-parameter covariance tomography*. With the original old-six theoretical ideal covariance included, the latter already had rank5; no claim about globally minimal total sensor cost.

**Important fifth parameter guard:** the independent raw-full-sixth calibration variance beta_cal does NOT occur in Sigma_Z, hence these three new probes alone cannot identify beta_cal. Its separate recovery still needs a model with a sixth full/outer observation or other independent calibration information.

A strict new negative control holds beta0=1 and raw beta_cal fixed while changing theta from A=(.12,.10,.08) to legal A'=(.13,.09,.08), maintaining sum theta=.30: ROT036's SINGLE Z0 marginal distribution is IDENTICAL across A/A' (variance exactly 2), but NEW three-probe matrix offdiagonal entries differ in the AXIAL and FACE slots. Thus ROT037 is not just a repetition of the ROT036 single-probe beta0 readout. All FOUR beta components for both earlier exact rational ROT035 A/B models are recovered EXACTLY, source firstness preserved.

## 3. Strong same-coordinate Gaussian parameter Fisher and 95 percent finite-sample recovery

At original legal baseline model A beta0=1, theta=(.12,.10,.08), raw beta_cal exactly 1/2500 KNOWN, take four statistical covariance parameters (log beta0,theta_axis,theta_face,theta_body). For independent centered Gaussian raw multivariate observations, exact classical covariance information is Fij=(1/2)tr(C^-1 Ci C^-1 Cj). New source code derives ALL Fisher matrix entries as EXACT SymPy Rational and profiles unknown log beta0 using exact Schur complement. New three-probe theta-Fisher block has exact rank3, positive determinant, and high precision numeric eigenvalues:
 (0.0069431065417195705, 0.015638577254367338, 0.027811394910822813),
 numeric condition ~4.00561258043649.

The SAME primary source code independently reconstructs the old SIX source mask 6x6 Gaussian covariance from all three ORIGINAL integer E adjacency graphs (locked complete ROT034 output), holds the raw calibration fixed and correctly uses derivative dC/dlogbeta0=C-beta_cal K. Its source exact old-six profiled theta-Fisher block rank3 has high precision NUMERIC minimum eigenvalue ~1.7098900565479104e-13. Ratio of minimal per complete-sample profiled eigenvalues NEW three vs OLD six ~=**40,605,572,944**. For independent old six+new three readings, sum their unprofiled Gaussian Fisher contributions FIRST, then profile common logbeta0, giving numeric weakest theta eigenvalue ~0.011861479102294668. The exact rank and positive determinant tests are mathematical source certificates; high precision numerical eigenvalues are **diagnostics, NOT rigorous outward interval eigenvalue bounds**. This comparison concerns distinct hypothetical measurement designs, not an improvement of any historical physical experiment or a ratio of real sample sizes.

NEW nonasymptotic simultaneous uncertainty guarantee even with UNKNOWN but STABLE original M13 signal means: assume purely hypothetically n=40,000,000 independent site Gaussian noise snapshots of three additional contrast measurements with a fixed source state. Form m=20,000,000 independent 3-vectors Y_i=(Z_(2i)-Z_(2i-1))/sqrt(2), thereby exactly canceling unknown deterministic original site signal means; covariance remains Sigma_Z. Reconstruct four beta using sample covariance S of Y. Apply classical Laurent-Massart chi-square tail to nine real Gaussian variance projections Y0,Y1,Y2,Y0±Y1,Y0±Y2,Y1±Y2, and union bound. Set t=log(360), r=2sqrt(t/m)+2t/m≈0.00108558667781618. With probability at least 0.95, ALL FOUR errors satisfy SIMULTANEOUSLY:

 |beta0_hat-beta0| <= 0.001085587 beta0;
 |beta_axis_hat-beta_axis| <= 0.006513521 beta0;
 |beta_face_hat-beta_face| <= 0.013027041 beta0;
 |beta_body_hat-beta_body| <= 0.008684694 beta0.

These are conservative normalized absolute error bounds conditional on 40M **unobserved hypothetical IID snapshots**, not actual reported performance. Exact source proof: each sample quadratic variance / its true variance is chi-square_m/m; each two-sided error exceeds r with prob<=2 exp(-t), nine event union failure<=.05. Covariance Sij is [sampleVar(Yi+Yj)-sampleVar(Yi-Yj)]/4 and original diagonal variances are each 2 beta0, giving coefficients 6,12,8. Unknown but fixed source mean is removed by temporal pairing. Source drift, non-IID time noise or non-Gaussian site errors remove this guarantee.

## 4. Two separately authored original-source execution paths

**PRIMARY source exact** rot037_exact_three_probe_tomography.py: before importing original M13, Git blob verifies exact unmodified original module and original B25, SHA256 locks COMPLETE original source ROT034, ROT035 and ROT036 proof result JSON. Executes ORIGINAL M13 tensor_polys(41)[B] and five actual original source masks+full k0 via mpmath.iv40. Independently checks all nine site cross branches, 72 original source region zero covariance generator coefficients, exact original site adjacency covariance matrices for three probes and exact inverse/rank4/minimality, exact legal A/B model recovery, negative single-probe A/A', exact old-six and new-three Gaussian Schur information matrix and synthetic finite-sample confidence.

**SEPARATE SPATIAL** rot037_independent_three_probe_fourier.py: verifies original M13/B25 Git blobs, original ROT035 proof source and new exact ROT037 result SHA before import. Does NOT import new primary algebra or original integer E source matrices. Fourier-transforms SIX original 41 cubed mask-indicator averaging fields and THREE signed site-delta vectors, directly aggregates raw site Gaussian spectral covariance from original axial/face/body symbols. Under BOTH legal original ROT035 A/B models full 9x9 Gaussian covariance has cross-six-by-three block zero within binary64 noise, and new three-by-three block equals original rational law; four beta values reconstructed numerically, full 9x9 covariance SPD. It independently reconstructs actual M13 41 complex 3x3 Fourier B modes on full N41 cubed tensor grid, original full k0 relative difference ~1.1114e-16. Original deterministic M13 signal means at swapped pairs are generally NONZERO: all inference is noise covariance, not a source field symmetry claim.

Separate FFT implementation is an **independent same-cell algorithm**, NOT an external REC13/AUD3/M15 I1 reviewer.

## 5. Full source custody and actual archive proof

Full self-contained USER local executable artifact:
 **Geeky_S12_ROT037_minimal_three_symmetry_odd_noise_covariance_tomography.zip**,
 **42,393 bytes SHA256 56ff15232edd00129eeeda579e9ad8f55fce7fcbd451f44993a2e895a9ffa936**,
 13 entries, 12 SHA256 manifest payload entries. ZIP CRC PASS, all 13 archive members exact full-byte readback PASS, all 12 payload SHA256 PASS.

Actually executed new original exact Python SHA256 6997a239cd6aeadc8231346d8930cf77e2e26a494518a99242450f20be16748c; full source JSON SHA256 5a24ace3355edbd40beb4f55194b4d5c0359e7f760c42bc39664274e95d95329. Separate full-site FFT Python SHA256 63969e7d85bb633987fa5e46369ee0dc29fd39caafa90e250ed7b8810712051c; full FFT JSON SHA256 3df2894cfa7ee48337a388248f3233d0c8df02c879398def66e407ebedd6eb49. Clean replay controller SHA256 509d392f1ede63c27041caaa998aad4856875789777e61e27e0e6316d6f995a3; full receipt JSON SHA256 2b52977e7cba38e0782a842fd9d8fdc9f9ceda7be11c10cdb5ed733863aea2d9.

CONTROLLER actually copied new source programs and all original locked inputs into TWO different fresh temp directories, ran each under new Python -I process, and compared both newly regenerated COMPLETE JSON outputs BYTE-FOR-BYTE: 2/2 PASS. EIGHT deliberate one-byte mutations of disposable original M13 helper, B25 data, full parent ROT034/035/036 exact proof input and new ROT037 exact result as applicable: ALL 8/8 REJECTED with SOURCE_IDENTITY_MISMATCH before original scientific source import, sources unmodified. **ADDITIONAL END-TO-END archive test** extracted the actual final ZIP into a fresh temporary directory and ACTUALLY RAN all three programs (two science scripts+clean replay/tamper controller); ALL resulting full JSON bytes matched the archive source outputs; 3/3 PASS. No false statement that Python executed source is mirrored byte-identically on public GitHub: complete executed Python and all original exact results are in the verified user ZIP.

## 6. Hard ceilings and bounded independent reviewer

This is only original PUBLIC AUXILIARY M13 B/N41 source, not the missing byte-exact historical full dtc0a_runtime_v0_3_1.py. Original source has NO authenticated ability to acquire 6 pointwise energy readings, 40 million independent site Gaussian repetitions, physically verified noise correlation law, original physical independent sixth full energy detector or native relative field translations/common gain. All observations added here are synthetic mathematical stress-test extensions. No inference about actual alpha, original physical K/J3/TPE/GW/GR, global inverse uniqueness, physical new detector precision or newly discovered general mathematical method. The Gaussian group-symmetry, Wishart Fisher and chi-square tail tools are classical.

M13 original source FIRST. Geeky ROT034 exact source six-mask tomography FIRST, Geeky ROT035 exact A/B source covariance near-KL first, now independently M15 ROT029 I1. Geeky ROT036 one symmetry-odd source-site probe FIRST. M15 ROT030 global optimal **single full spatial Fourier** summary FIRST in its own task. NEW Geeky ROT037 source FIRST within this lineage the MINIMAL THREE new symmetry-odd local contrasts for FOUR site-noise coefficients independently of all old mask means and its exact noise-parameter Fisher conditioning and finite sample guarantee. NEW ROT037 is AUTHOR/SAME CELL ONLY; independent different-cell M15/REC13/AUD3 I1 PENDING; KN15 BW provider native ingest and M15 owner CANON/EXEC_SIGN NOT VERIFIED. GitHub and Slack posted events are not acceptance. No automatic follow-up task cascade.

Bounded external source referee: independently reconstruct the original M13 cube mask coordinate-swap group invariance and the 3 new site pairs, source-exact all four generator cross covariance zeros; verify source exact 3x3 entries, 4x4 recovery and two-probe impossibility *for new-only four-parameter covariance tomography*; independently rebuild correct raw-calibration-fixed original six theta Fisher and new three Fisher, then prove conditional 95% finite-sample error constants via temporal pair chi-square and union. Preserve M15 firstness, synthetic-observer scope, source-vs-noise symmetry and potential non-Gaussian/drift falsifiers.

FINAL:
 ORIGINAL_M13_UNCHANGED_GIT_BLOBS_NATIVE_EXEC_PASS /
 SOURCE_3_SWAPPED_PAIRS_EXACT_72_CROSS_GAUSSIAN_COVARIANCE_ZEROS_PASS /
 THREE_PROBES_EXACT_FOUR_SITE_NOISE_PARAM_RANK4_RECOVERY_AND_MINIMALITY_PASS /
 PRIOR_TWO_RATIONAL_A_B_MODELS_EXACTLY_RECOVERED_NEGATIVE_SAME_BASELINE_CONTROL_PASS /
 SAME_PARAMETERIZATION_OLD_SIX_VS_NEW_THREE_EXACT_FISHER_PROFILES_AND_NUMERIC_DIAGNOSTICS_PASS /
 SYNTHETIC_40M_FINITE_SAMPLE_95PCT_FOUR_PARAMETER_ERROR_BOUNDS_PASS /
 SEPARATE_9X9_FULL_N41_CUBED_SITE_FOURIER_PASS /
 TWO_CLEAN_COMPLETE_BYTE_REPLAYS_EIGHT_ONEBYTE_TAMPERS_PASS /
 FINAL_ZIP_CRC_13OF13_BYTES_12OF12_SHA_AND_3OF3_EXTRACTED_PROGRAMS_PASS /
 EXTERNAL_I1_PENDING / BW_PENDING /
 NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
