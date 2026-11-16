---
artifact_id: IW_GEEKY_S12_ROT033_FACE_DIAGONAL_TWELVE_NEIGHBOR_UNIQUE_FISHER_MINIMUM_001_20261117
date: 2026-11-17
origin: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
source: ORIGINAL_PUBLIC_M13_B_N41_BYTE_LOCKED_MODULE_AND_B25
status: AUTHOR_IV55_WHOLE_TWO_SOURCE_FOLD_BRACKETS_PASS / SAME_CELL_INDEPENDENT_36_SPATIAL_GLS_PASS / NEW_EXTERNAL_I1_PENDING
review_currentness: M15_ROT026_I1_PRIOR_GEEKY_ROT031_AND_ROT032_PASS / M15_ROT026_FIRST_AXIS_BODY_MIXING_THRESHOLDS
sync: GITHUB_PENDING_BW_INGEST
claims: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# ROT033 — third canonical nearest-neighbor geometry gives one unique interior information minimum

## I. Original source and priority

Original M13 FIRST public N41 sparse Fourier/TT B source 8970-byte Python module, Git blob c6377cfbc9a0070abc34ffedc5871e719f6a4679, and original 7501-byte B25 coefficient data Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0. Both input Git blobs verified byte-exact BEFORE actual original-module scientific import.

Original helper: https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py

Geeky ROT023–024 FIRST two original-source five-shell alpha rank-four Whitney folds independently reviewed by M15/AUD2; Geeky ROT027 FIRST mathematical sixth unmasked full B energy reviewed I1 M15 ROT021; Geeky ROT028 original six-channel independent log-noise Fisher reviewed I1 M15 ROT022; Geeky ROT029 source shared-grid Gaussian RAW energy noise reviewed I1 M15 ROT023; Geeky ROT030 random sixth full-mean calibration and independent bounded heteroscedastic errors independently reviewed I1 M15 ROT024.

Geeky ROT031 FIRST original SIX AXIAL-neighbor mask graph and strictly declining Fisher under positive axial correlation; Geeky ROT032 FIRST original EIGHT BODY-diagonal neighbor graph and strictly rising Fisher under positive body-diagonal correlation. M15 ROT026 17 Nov 2026 00:08 CET independently source-IV55 NONBLIND I1 PASS reviewed BOTH results, with ORIGINAL FIRSTNESS preserved; moreover M15 FIRST derived independent AXIS/BODY MIXED covariance critical mixing fractions and opposite-fold sign at lambda=.55. ROT033 does NOT repeat nor claim that mixed-axis/body firstness.
https://github.com/wmakiela-tech/Nash-iw-research/blob/ee136d5fc0fa7a02459ea7e5c03e69786d8d20b1/research/m15/2026-11-16/IW_M15_ROT026_ORIGINAL_M13_DIAGONAL_AXIAL_MIXTURE_CONTINUOUS_FISHER_SIGN_REFEREE_001_20261116.md

NEW ROT033 addresses the third geometrically primitive nearest-neighbor class: TWELVE FACE-diagonal shifts (two signed one-step coordinates, the remaining coordinate unchanged). This is NOT any axis/body mixture. Its new source result is not a constant opposite-fold sign but a genuine UNIQUE information turning point within a continuous correlation family.

## II. Exact original six-region face graph

Original N=41 periodic cube 68921 sites. Region order outer plus original fixed mask disjoint shells k=2..6, exact occupancies W=(18268,7778,6938,6146,5402,24389). Count all twelve directed face-diagonal periodic lattice shifts at EVERY original site, then independently verify every count by analytic inclusion-exclusion of translated two shifted dimensions times one unchanged dimension for ORIGINAL nested cubes. Both independent exact INTEGER procedures agree on full 6x6 E_face:

[[186804,32412,0,0,0,0],
 [32412,31944,28980,0,0,0],
 [0,28980,28536,25740,0,0],
 [0,0,25740,25320,22692,0],
 [0,0,0,22692,22296,19836],
 [0,0,0,0,19836,272832]].

E_face is symmetric, rows sum exactly 12 W_i. Primitive source integer contrast z=(0,1,-1,1,0,0) gives z^T E_face z = -23640, strictly negative. The actual executable also finds equivalent scaled contrast (0,-2,2,-2,0,0), value -94560. Thus original region face E is INDEFINITE; however this fact alone does NOT prove any Fisher sign.

## III. HYPOTHETICAL mathematical noise and observer

Actual original M13 public native tensor_polys(41) yields original sparse B Fourier tensor polynomial with 41 complex 3x3 modes. Five old positive original fixed-mask shell energies S_i are original source; original unmasked full-domain k0 B energy is an additional MATHEMATICAL SIXTH observer. Common torus translation t of all C1,C2,h fields relative to original FIXED masks plus free common log energy gain b have been explicitly HYPOTHETICAL stress-test extensions; original M13 source()/calc() does NOT offer those native parameter knobs or historical independent sixth sensor. All four nuisances b,tx,ty,tz remain unknown; alpha is target.

Six RAW energy region mean observations are five old disjoint means plus mathematical outer mean O=(68921*G-sum_i w_i S_i)/18268, an invertible observation transformation of old-five-plus-unmasked full mean G. Assume entirely synthetic centered Gaussian additive RAW SITE ENERGY DENSITY errors with covariance eta²(I+theta A_face), theta in [0,2/5], eta>0 fixed, A_face=average of the twelve one-step face-diagonal shifts. Its original periodic Fourier eigenvalues are (cos kx cos ky+cos kx cos kz+cos ky cos kz)/3 in [-1,1], so site covariance is SPD for all declared theta. For D=diag(W), the exact regional RAW ENERGY mean covariance is eta²[D^-1+(theta/12)D^-1 E_face D^-1]; its OFFDIAGONALS are essential. Positive source log-scores are only coordinates for EXACT Gaussian RAW ENERGY mean Fisher, not a claim that logged noisy energies are Gaussian.

Optionally add independent centered Gaussian RAW FULL-domain-mean random calibration error with KNOWN finite std kappa*eta. This becomes an OUTER-only covariance term eta²*(68921/18268)^2*kappa². It is NOT the wholly unrestricted fixed unknown sixth-channel log offset that M15 ROT022 FIRST proved annihilates recovered alpha information.

## IV. New analytic one-dimensional Fisher theorem

At any old true five-output source rank-four fold, fix six-output linear contrasts L with outer coefficient 1 annihilating the four nuisance columns. There remains ONE free real coordinate t, so L=L0+t H. Source Gaussian covariance is affine in theta, and minimizing variance over t gives EXACTLY:

 a(theta)=a0+a1*theta=H^T C(theta) H>0;
 b(theta)=b0+b1*theta=H^T C(theta) L0;
 c(theta)=c0+c1*theta=L0^T C(theta) L0;
 K=68921 G/(18268 O).

 V(theta,kappa)=c0+c1*theta+K²*kappa²−(b0+b1*theta)^2/(a0+a1*theta);
 epsilon² I_alpha(theta,kappa)=delta_outer²/V(theta,kappa), epsilon=eta/G.

The exact second derivative is
 V_second(theta)=−2*(a0*b1−a1*b0)^2/(a0+a1*theta)^3,
strictly NEGATIVE because the source-IV55 nonzero numerator and positive denominator are certified. Thus V is strictly concave across the whole theta range; Vprime is strictly decreasing, and the Fisher information can have at most one inner stationary point, necessarily a strict MINIMUM. Added independent finite known random calibration contributes a theta-independent CONSTANT to V and does not move that stationary theta. All general algebra is CLASSICAL, no math novelty claimed.

## V. Actually executed original M13 source IV55 whole-alpha proofs

New source program actually SHA locks original M13 and B25 blobs plus prior original ROT031 and ROT032 complete source/spatial evidence JSON, then imports UNMODIFIED original M13 and ACTUALLY RUNS tensor_polys(41), inner/window_mode on all FIVE source masks, recomputes ALL TWENTY original analytic source scores (3 shifts plus alpha times five shells), and original full k0 energy at mpmath.iv.dps=55 over BOTH ENTIRE prior independently reviewed alpha-root intervals. This is fresh original source work, NOT just a hash reread of earlier scores.

Fold1 alpha in (.01861522133766,.01861522134166):
 Vprime(theta=0) in [0.000531452477175918,0.000532687557140022] >0.
 Vprime(theta=.4) in [0.000499440887436203,0.000500840016404081] >0.
Strictly decreasing Vprime remains positive across ALL real theta in [0,.4]. Therefore source Fisher is STRICTLY DECREASING for the entire theta continuum.

Fold2 alpha in (.05416739905600,.05416739906000):
 Vprime(0) in [0.000143904130967350,0.000158874900016567] >0.
 Vprime(.4) in [-0.000753875320689732,-0.000738915537185787] <0.
More strongly, source IV55 entire root-bracket Vprime(.062)>0 and Vprime(.070)<0. Together with STRICT V_second<0, exactly ONE theta_star exists, with **0.062 < theta_star < 0.070**, such that V(theta) has a UNIQUE STRICT MAXIMUM and the Fisher information has a UNIQUE STRICT MINIMUM. Independent spatial midpoint estimate theta_star≈0.065690574095827 (NUMERIC DIAGNOSTIC, not a strict decimal enclosure itself).

At kappa=.01, actual source strict Fisher intervals:
 fold1 theta0 [14.9436396055,14.9486826329], theta.4 [14.5919853240,14.5973643953];
 fold2 theta0 [470.334747849,470.600921492], theta.4 [472.008389877,472.344785055].
At fold2 the actual midpoint Fisher falls to ~470.39791 near the single minimum and then rises to ~472.17653 at theta=.4. Rigorous theorem uses strict source derivative signs and curvature across WHOLE alpha intervals, not a low-precision scan of theta.

Complete actual original source IV55 results including 6 quadratic coefficient intervals, all grid test intervals and exact E face: rot033_original_source_face_results.json (55372 bytes), SHA256 e7cc34aa760b1b6936f581cc9f73eb4987ce862076edd4e88dafe870e5884bcf.
Actual source native new Python SHA256 923041c708ff1c664bdd163f40629eab2b267d7e44e0a4372b3a78df47983252.

## VI. Separately authored spatial 41 cubed crosscheck, ALL 36 cases

New independent-algorithm same-cell Python reconstructs actual original 41 complex 3x3 Fourier B mode tensors and four derivative tensor fields in 41 cubed spectral arrays, evaluates full spatial 3D inverse FFT and original cube region averages, not the original M13 inner/window_mode observation path. It independently counts face directed-region neighbors from SIX canonical half-shifts and transposes, different from the source program's twelve rolls/analytic nested cube checks.

2 folds × 3 geometries (axis, face, body) × 3 theta levels (0,.2,.4) × 2 known random calibration levels (0,.01) = **36 actual scenarios**. In each, the correct NONDIAGONAL six-disjoint-region Gaussian GLS and independently transformed original old-five-plus-global GLS agree to <2e-8 relative and ALL 36 lie within appropriate original-source rigorous IV intervals (new face IV55 or frozen parent axial/body IV55). With kappa=.01, new FACE spatial information:
 fold1 theta0,.2,.4 = (14.946160926470,14.765614831583,14.594674612500);
 fold2 = (470.467798951711,470.687109943981,472.176529591197).
Independently numerically locating the unique fold2 derivative root gives theta_star≈0.065690574095827, inside original-source entire-alpha strict (0.062,0.070).
All these FFT checks are SAME-CELL numeric diagnostics, NOT independent external I1 new ROT033 review.
New independent spatial executable SHA256 3e68dca002e849b2cd7a2461afbb81e4d20ebce199eae8d4eaacc92adba2d1a6; full output rot033_spatial_face_GLS_results.json SHA256 29f284320992de655fe61111c3de59c016ab24a306d93d743f72ec1c09889506.

## VII. Actual replay and complete archive integrity

FULL USER-LOCAL self-contained ZIP:
 Geeky_S12_ROT033_face_diagonal_unique_Fisher_information_minimum.zip,
 53338 bytes, SHA256 **555f4a597346d180d559d72a7509bd644fb8601d9d54c698804e2370315b0e82**.
14 members including original unmodified M13 source and B25, four immutable original ROT031/032 scientific source and spatial proof JSON, new source and spatial executable Python, both full actual JSON outputs, replay/tamper script with receipt, complete scientific README and SHA manifest. ZIP CRC PASS, **14/14 exact member byte readback PASS, 13/13 payload SHA256 PASS**.

New replay controller source SHA256 9a505c7407af1f88bae9c8b0797723ae4746857469f75f38923bee2fbcf11586, actual full receipt SHA256 8adf76136418e2b53b7a24bdfc637db036132ee6d7ffe905e0b831ce4d9fb9b8. Both new science programs actually executed again in separate fresh isolated Python -I temporary directories; full complete original source and spatial JSON result reproduced BYTE FOR BYTE, 2/2 PASS. Eight separate one-byte mutations on disposable original M13/B25/prior results/new original source JSON all rejected BEFORE M13 scientific import with SOURCE_IDENTITY_MISMATCH, 8/8 PASS. Original evidence unchanged. Full executable original Python and 55-digit directed endpoints in LOCAL ZIP; this public report and separately curated JSON are not false exact-byte public GitHub runnable code mirrors.

## VIII. Hard guards, next bounded reviewer

Original public M13 auxiliary B N41 ONLY; the full historical byte-identical dtc0a_runtime_v0_3_1.py remains MISSING. No verified historical original field translation, free gain, independently measured sixth channel, observed per-site Gaussian correlation law, actual calibration variance, measured source noise SNR, global 6-output inverse theorem, physical NASH K/J3/TPE/GW/GR or general mathematics novelty.

M13 original firstness, Geeky ROT031/032 original respective mask noise results, and M15 ROT026 independent reviews and FIRST axis/body anisotropy thresholds all preserved. NEW ROT033 SOURCE FACE orientation and UNIQUE strict turning point are AUTHOR-ONLY, external REC12/M15/AUD2 new ROT033 I1 PENDING. KN14 BW native ingestion and owner M15 CANON/EXEC_SIGN UNVERIFIED. GitHub/Slack posted events are not approval or BW receipt.

Bounded external referee: independently fetch original M13 at pinned Git blob, rebuild source original six region mask labels and exact twelve face shifts; independently prove Eface and strict negative primitive quadratic; rederive full original five window-mode scores and outer nuisance residual over both original alpha fold intervals; certify Vprime first fold(.4)>0, second fold Vprime(.062)>0 and Vprime(.07)<0, V_second<0, including finite random calibration independence. No auto task cascade.

FINAL: PRIOR_ROT031_ROT032_M15_ROT026_DIFFERENT_CELL_I1_PASS / ORIGINAL_M13_SOURCE_AND_FOUR_PRIOR_FULL_RESULT_HASH_GATES_PASS / NEW_EXACT_FACE12_MASK_INTEGER_GRAPH_AND_NEGATIVE_QUADRATIC_PASS / ORIGINAL_NATIVE_M13_IV55_BOTH_FULL_SOURCE_FOLD_BRACKETS_ALL_SCORES_PASS / FOLD1_STRICT_INFORMATION_MONOTONE_DECREASE_ALL_REAL_THETA_PASS / FOLD2_ONE_AND_ONLY_ONE_INTERIOR_FISHER_MINIMUM_THETA_STAR_IN_0p062_TO_0p070_PASS / ALL_FINITE_KAPPA_RANDOM_CALIBRATION_POINT_INVARIANCE_PASS / 36_OF_36_DIFFERENT_SPATIAL_GLS_SCENARIOS_PASS / TWO_CLEAN_COMPLETE_BYTE_REPLAYS_EIGHT_TAMPER_FAILCLOSED_PASS / ZIP_CRC_14OF14_BYTES_13OF13_SHA_PASS / NEW_ROT033_EXTERNAL_DIFFERENT_CELL_I1_PENDING / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
