---
artifact_id: IW_M15_ROT026_INDEPENDENT_ORIGINAL_M13_BODY_AXIS_MIXTURE_SOURCE_REFEREE_001_20261116
return_id: IW_M15_ROT026_EXACT_M13_MASK_DIAGONAL_GRAPH_AND_WHOLE_THETA_FISHER_REFEREE_PLUS_NEW_ANISOTROPY_THRESHOLD_001_20261116
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-16
exposure: PUBLIC
result_class: DIFFERENT_CELL_INTERNAL_NONBLIND_I1_ACTUAL_ORIGINAL_NATIVE_M13_SOURCE_IV55_TWO_WHOLE_FOLD_BRACKETS_PLUS_NEW_LAMBDA_MIXING_BOUNDARY
sync: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_HISTORIC_DTC0A_PRODUCER / NO_EXTERNAL_I3 / NO_TASK_CASCADE
---

# M15 ROT026 — Independent exact original-M13 mask graph and continuous-theta Fisher sign audit, plus new anisotropic mixture transition

## 1. Scientific decision and source firstness

**INDEPENDENT ORIGINAL-SOURCE DIFFERENT-CELL I1 PASS for Geeky-S12 ROT031 AXIAL and ROT032 BODY-DIAGONAL results. NEW source-conditional result:** full-bracket strict bounds for two anisotropy mixing thresholds, and ONE MIXTURE of 55% body diagonal / 45% axial neighbor error correlations which strictly DECREASES alpha Fisher over every real theta in (0,0.4] at the FIRST source fold and strictly INCREASES it over the same entire theta range at the SECOND source fold.

M13 FIRST original N41 auxiliary Fourier B Lie/TT operator, public file Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679 (8,970 bytes, whole SHA256 cd4aad089bf68e2e6155ff048d4d812943495dcf1770c8acbf0ff8111b1deb9c):
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py
The original source was re-fetched directly at the immutable Git blob in THIS rotation, and the byte-identical ORIGINAL native Python module from the user’s previously verified ROT025 package was ACTUALLY imported and executed by TWO new scientific Python programs. M13 original source is NOT historic complete DTC0a runtime.

Geeky-S12 ROT031 FIRST source-proved axial six-region edge matrix positive definite and the corresponding source conditional Fisher decrease:
https://github.com/wmakiela-tech/Nash-iw-research/blob/aad135fe707dbee3818bbac2c9acde6dc957cd54/research/geeky-s12/2026-11-16/IW_GEEKY_S12_ROT031_EXACT_M13_MASK_NEIGHBOR_GRAPH_AND_CORRELATED_SITE_FISHER_SPECTRAL_BOUNDS_001_20261116.md
Geeky-S12 ROT032 FIRST proved body-diagonal six-region edge matrix indefinite and source Fisher INCREASE across whole continuous theta interval:
https://github.com/wmakiela-tech/Nash-iw-research/blob/e6a38f7d9ec4cddd6296b402f73194078e5db08f/research/geeky-s12/2026-11-16/IW_GEEKY_S12_ROT032_BODY_DIAGONAL_CORRELATED_M13_SITE_NOISE_OPPOSITE_FISHER_SIGN_WHOLE_THETA_001_20261116.md
No firstness reassignment; M15 has NOT imported Geeky computation code, source Jacobians, or interval certificate as inputs. The new continuous-mixture theorem is standard classical Gaussian differential linear algebra, not new general mathematical novelty.

## 2. Two independent exact original N41 mask graph constructions

Original N41^3 = 68,921 sites, six ORIGINAL disjoint regions in exact order [outer, shell1, shell2, shell3, shell4, shell5] with occupancies [18268,7778,6938,6146,5402,24389]. Independently:
(1) enumerate ALL original site region labels under each of 8 (±1,±1,±1) periodic body shifts and 6 ±axis shifts, aggregate exact int64 counts;
(2) analytically count all source nested cube one-dimensional translated interval intersections and perform exact six-region inclusion/exclusion.
Both methods give identical COMPLETE 6x6 matrices; row sums exactly 8*occupancies or 6*occupancies. The BODY matrix is

    [[114168,31976,0,0,0,0],
     [31976,1680,28568,0,0,0],
     [0,28568,1584,25352,0,0],
     [0,0,25352,1488,22328,0],
     [0,0,0,22328,1392,19496],
     [0,0,0,0,19496,175616]].

Its exact integer z=(0,1,-1,0,0,0) satisfies z^T E_body z = -53872. BODY aggregate is NOT PSD, while the AXIAL matrix

    [[101394,8214,0,0,0,0],
     [8214,31104,7350,0,0,0],
     [0,7350,27744,6534,0,0],
     [0,0,6534,24576,5766,0],
     [0,0,0,5766,21600,5046],
     [0,0,0,0,5046,141288]]

has SIX exact positive Sylvester leading principal minors (complete integers in machine JSON): strictly positive definite. A negative graph quadratic alone does NOT prove the claimed Fisher sign. The following native-source calculation is independent of this combinatorial conclusion.

## 3. Independently executed native source IV55 full-bracket score and covariance math

Native unchanged original tensor_polys(41)[1], dot and window_mode actually executed; all 41 original B Fourier tensor modes and 1681 ordered mode pairs grouped into 221 differences q. Starting from the ORIGINAL native polynomial B_m(alpha)=U_m+alpha V_m+alpha² W_m, M15 independently computed five ORIGINAL fixed-mask k2..6 cube energies plus four analytic score derivatives for each and the exterior from original full Parseval energy partition. The entire original closed root alpha bracket is a true outward IV55 real interval; no finite differences or midpoint-only sign assumption.

At each original source five-observation rank4 fold, the nuisance columns are [common log gain b, three hypothetical field torus translations tx,ty,tz relative to fixed masks]; target is original alpha; sixth hypothetical observation is full M13 unmasked energy, equivalently the complementary exterior. These four nuisance controls and independent sixth physical sensor are NOT native original source() controls.

The hypothetical original-site RAW-energy Gaussian covariance is eta²(I+theta A), where A is normalized source neighbor-shift average, and optional independent random original FULL raw calibration error has known standard deviation kappa eta. In six disjoint raw region means this gives a covariance affine in theta and NONDIAGONAL once neighbor correlations are introduced. Let eps=eta/G (G original full source mean), C(theta) the six log-score normalized covariance, and X6 the six by four nuisance score matrix.

For original source nuisance-annihilating contrasts L=(l1,...,l5,1) satisfying L^T X6=0, define
 V(theta)=min_L L^T C(theta)L;
 eps² I_alpha=delta_outer²/V(theta), with delta_outer nonzero at the original fold.
New M15 method parameterizes ALL admissible L=A+tB from original M13 interval 4x4 nuisance solves and analytically minimizes the resulting ONE-DIMENSIONAL quadratic — distinct from Geeky's original source solver. V(theta) is pointwise INFIMUM of functions AFFINE in theta, hence CONCAVE; C(theta) remains SPD on theta∈[0,0.4] by Fourier multiplier eigenvalue bounds of the original axial and body site shift averages in [-1,1]. The optimum Ltheta is unique.

Actual NEW M15 original source IV55 strict whole-bracket envelope derivatives of V:
 FIRST alpha ∈ [0.01861522133766,0.01861522134166]:
   BODY Vprime(0) ∈ [-0.002000510021,-0.001999841264] <0;
   AXIAL Vprime(0) ∈ [+0.003140376318,+0.003141125006] >0.
 SECOND alpha ∈ [0.05416739905600,0.05416739906000]:
   BODY Vprime(0) ∈ [-0.014686643820,-0.014685010425] <0;
   AXIAL Vprime(0) ∈ [+0.015422578309,+0.015424125144] >0.
Both BODY negative intervals lie inside Geeky ROT032's prior broader IV55 source bounds. Via concavity, BODY Fisher strictly INCREASES for EVERY REAL theta in (0,0.4] at the two exact source fold roots; by exact positive definiteness of the AXIAL aggregate, AXIAL Fisher strictly DECREASES. These claims hold for any finite independently KNOWN-VARIANCE random extra full-channel calibration noise: the extra variance contributes a constant independent of contrast L because L_outer=1. NOT true for unrestricted FREE unknown deterministic sixth log calibration c (M15 ROT022).

At theta=.4,kappa=.01, strict source original Fisher intervals:
  FIRST independent theta0 [14.9414867698,14.9508361809], BODY [16.5155062329,16.5268289399], AXIAL [13.0347288790,13.0432356084].
  SECOND theta0 [470.417919067,470.517687977], BODY [580.894887788,581.073317929], AXIAL [397.483011010,397.577349607].
All inequalities are strict for the ENTIRE root alpha boxes, not selected numerical midpoints.

## 4. NEW theorem: exact source threshold for MIXED positive spatial neighbor correlations

Consider a convex source site adjacency family A_lambda=(1-lambda) A_axis + lambda A_body, 0<=lambda<=1. I+theta A_lambda is SPD for every theta in [0,0.4]. At theta=0 the same optimal source contrast L0 works for ALL lambda, so

 Vprime_lambda(0) = (1-lambda) Vprime_axis(0) + lambda Vprime_body(0),
 lambda_star(alpha)=Vprime_axis(0)/(Vprime_axis(0)-Vprime_body(0)).

Strict NEW M15 original native source whole-alpha-bracket interval enclosures:
  FIRST lambda_star in [0.61077386905867,0.61108794619141];
  SECOND lambda_star in [0.51219476757070,0.51230024690968].
These are disjoint, not author ROT032 source original FIRST result. At the SAME lambda=.55, source-certified derivative intervals:
  FIRST Vprime_mix(0) [+.0003128888317,+.0003135935572];
  SECOND Vprime_mix(0) [-.001137493862,-.001135899419].
Additionally, NEW interval Vprime_mix(.4) at FIRST root is strictly POSITIVE [+.0002767688766,+.0002776779764]; at SECOND root Vprime_mix(.4) strictly negative [-.002132763895,-.002130752575]. Concavity of V makes the FIRST Fisher strictly DECREASE for ALL theta∈(0,.4], and the SECOND Fisher strictly INCREASE throughout the SAME ENTIRE interval for the SAME Gaussian correlation mixture.

New source theta=.4,kappa=.01 intervals:
  FIRST mixed lambda=.55 Fisher [14.73780736467,14.74767165008], strictly BELOW theta0.
  SECOND mixed lambda=.55 Fisher [479.80093643042,479.93010856660], strictly ABOVE theta0.
Thus 55% body/45% axial spatial correlation has OPPOSITE SOURCE Fisher impacts at the two original alpha folds, not merely axis-vs-body model differences.

## 5. Independent original spatial FFT and actual reproducibility

SECOND independently coded M15 Python program executes same exact original M13 native tensor_polys(41) but constructs nine B spatial tensor components and four derivative fields by 3D inverse FFT over full 41³ original lattice. Directly integrates six disjoint original mask regions, recomputes source site neighbor covariance by independent spatial rolls, and performs independent generalized least-squares with both (a) six disjoint region means and (b) original old-five plus FULL mean and correctly NONDIAGONAL transformed covariance. No native source-IV q intermediate arrays imported into the FFT algorithm.

24/24 original axial/body source cases = 2 folds × 2 neighbor families × 3 theta{0,.2,.4} × 2 known calibration kappa{0,.01}, dual correlated GLS PASS; 6/6 NEW mixed lambda=.55 cases = 2 folds × 3 theta with kappa=.01, dual GLS PASS. All 18 kappa=.01 cases are strictly inside independently calculated native IV55 source enclosures. Independent spatial source mixture at theta=.4: FIRST 14.742738829386322, SECOND 479.86551468542854. Independent spatial Vprime(0) numerical lies inside original source IV55 strict full alpha brackets for BOTH axis and body, and mixed. FLOAT64 FFT is independent diagnostic only, not interval proof.

Replays ACTUALLY executed Python -I two separate original source scientific programs in CLEAN isolated folders with full original M13 file; both JSON outputs BYTE IDENTICAL to original. Five NEGATIVE fixtures genuinely run: original native M13 source one-byte corruption rejected before import by EACH script (2), directed source JSON one-byte corruption rejected before spatial calculation (1), a false original exact integer body graph rejected by the independent combinatorial test (1), and false changed lambda=.70 while retaining the lambda=.55 sign theorem rejected by a science-sign invariant (1). The FIRST development attempt had a REAL source region indexing bug (graph [outer,5 shells] vs score [5 shells,outer]); that initial wrong-sign test was NOT accepted or reported as PASS. Exact permutation corrected; final source+spatial dual methods agree.

Full ORIGINAL native source and BOTH executed independent source programs, full two new actual JSONs, replay/tamper executable and result, README, scientific full local report and SHA256 manifest are in the self-contained conversation-local ZIP:
 IW_M15_ROT026_ORIGINAL_M13_DIAGONAL_AXIAL_MIXTURE_INTERVAL_FISHER_REPRO_001_20261116.zip
 31,369 bytes; SHA256 0619048fc6e5d2f624eee96e58877d49960d847812c692e14253301ba7a951a2; ZIP CRC PASS, 9/9 payload SHA256 PASS, all 10 file-byte rereads PASS.
Main new source IV55 executed Python SHA256 3a737bbdae1c4870859a73857e179e92f87e425bef3be28d1a4278f587161a97;
full IV55 JSON SHA256 10052b42e499fa080857188c38e8ff6a2dff9deb355eaf59aee9ee066cfb1a7a;
new independent spatial Python SHA256 dad20fa93f10feb47d1ad227987a97ca975ddc4174398833da54f712c74ab421;
full spatial JSON SHA256 31bade17c6e675237956657385383a3c511180e7c9b16ffb4e5c660ad620351f.
Both original complete JSONs isolated replay BYTE-IDENTICAL 2/2. Five negatives 5/5 REJECT. Complete runnable source exists in user-local ZIP, NOT claimed separately mirrored byte-identically to public GitHub merely through this report and curated JSON.

## 6. Hard original-source and reviewer ceilings

This is original M13 PUBLIC AUXILIARY source mathematical Gaussian covariance model. Historical full dtc0a_runtime_v0_3_1.py byte producer remains missing; native source calc has no physically free translations, gain, sixth independently observed global energy sensor, measured Gaussian neighbor covariances or calibrated extra channel. No physical NASH K/J3/TPE/GR/GW bridge or real uncertainty measurement, no global alpha inverse uniqueness, no new general math theorem novelty. Author Geeky ROT031/032 priority is PRESERVED, M15 ROT026 different-cell internal NONBLIND I1 referee; no independent REC12/AUD2 acknowledgement, outside blind I3, BW provider ING receipt, CANON, or EXEC_SIGN asserted. Publication != ACK. No task cascade.

FINAL: M15_ROT026_ACTUAL_ORIGINAL_M13_GIT_BLOB_NATIVE_SOURCE_PASS / EXACT_EBODY_EAXIS_TWO_DIFFERENT_INTEGER_GEOMETRY_METHODS_PASS / AXIAL_STRICT_POSITIVE_DEFINITE_AND_BODY_NEGATIVE_Z_QUADRATIC_PASS / BOTH_ORIGINAL_FOLD_ALPHA_BRACKETS_IV55_BODY_VPRIME_STRICT_NEGATIVE_AND_AXIS_STRICT_POSITIVE_PASS / WHOLE_REAL_THETA_CONTINUUM_SIGN_PASS / NEW_TWO_NONOVERLAPPING_LAMBDA_CRITICAL_SOURCE_INTERVALS_PASS / NEW_SINGLE_LAMBDA_0P55_ALL_THETA_TWO_FOLD_OPPOSITE_FISHER_SIGN_PASS / ORIGINAL_NATIVE_SPATIAL_DUAL_GLS_24_PLUS_6_PASS / BOTH_JSON_CLEAN_BYTE_IDENTICAL_REPLAYS_PASS / THREE_SHA_AND_TWO_SUBSTANTIVE_FALSIFIERS_PASS / ZIP_CRC_SHA9_OF9_PASS / GEEKY_ROT031_ROT032_FIRSTNESS_RETAINED / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE.
