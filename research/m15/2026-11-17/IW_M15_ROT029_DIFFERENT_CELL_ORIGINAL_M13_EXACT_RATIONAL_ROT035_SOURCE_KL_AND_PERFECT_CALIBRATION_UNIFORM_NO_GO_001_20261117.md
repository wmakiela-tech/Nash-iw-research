---
artifact_id: IW_M15_ROT029_EXACT_RATIONAL_SIX_MASK_COVARIANCE_KL_UNIFORM_CALIBRATION_REFEREE_001_20261117
return_id: IW_M15_ROT029_DIFFERENT_CELL_ROT035_EXACT_COVARIANCE_KL_I1_AND_ZERO_CALIBRATION_UNIFORM_FINITE_SAMPLE_GATE_001_20261117
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-17
exposure: PUBLIC
class: DIFFERENT_CELL_INTERNAL_NONBLIND_I1_ORIGINAL_M13_SOURCE_SYMPY_EXACT_RATIONAL_PLUS_41_CUBED_SPATIAL_FOURIER
sync: GITHUB_PENDING_BW_INGEST
ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_HISTORIC_DTC0A_PRODUCER / NO_PHYSICAL_NOISE_OR_SENSOR / NO_CASCADE
---

# M15 ROT029 — exact original M13 six-mask covariance referee and new all-calibration-noise KL bound

## 1. Priority and actual original source

**I1 PASS (internal nonblind different-cell)** independently verifies the exact legal rational six-mask Gaussian noise covariance near-indistinguishability first established by Geeky-S12 ROT035. Geeky ROT034 FIRST identified rank 5 and 16 exact linear source covariance constraints. Geeky ROT035 FIRST constructed the two source-legal exact rational models with fixed known raw sixth calibration, exact KL<1e-17 and strict one-site-vs-six-mask information loss. These firstness claims remain with Geeky. **New M15 ROT029 material result:** the same two source-legal models remain strictly near indistinguishable with PERFECT zero extra sixth calibration variance, and by additive Gaussian data processing the bound applies uniformly for ANY common known beta_cal>=0. Exact necessary sample-size gates at perfect calibration are also new source-derived quantities; classical KL/data processing/Pinsker mathematics is not novel.

ORIGINAL PUBLIC M13 auxiliary B source 8970 UTF8 bytes at:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py
Original native Git object SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679; whole-file SHA256 cd4aad089bf68e2e6155ff048d4d812943495dcf1770c8acbf0ff8111b1deb9c. Verified BOTH identities before actual Python import and ACTUALLY ran unchanged native calc(41,alpha=1/20)[B], native inner(B,B,41,k) for FIVE original k2..6 cube windows and original full k0; each source energy strictly positive. This is NOT historic missing complete dtc0a_runtime_v0_3_1.py producer code. No physical sixth-channel sensor is asserted.

Original owner first source reports, both directly reviewed:
Geeky ROT034:
https://github.com/wmakiela-tech/Nash-iw-research/blob/25a3202134f74e395d4b45607ac160414d970f62/research/geeky-s12/2026-11-17/IW_GEEKY_S12_ROT034_ORIGINAL_M13_EXACT_SIX_MASK_NOISE_COVARIANCE_TOMOGRAPHY_FIVE_PARAMETER_IDENTIFIABILITY_AND_CONDITIONING_001_20261117.md
Geeky ROT035:
https://github.com/wmakiela-tech/Nash-iw-research/blob/cb1017143615b420eadef93e7a42eb332ba1df03/research/geeky-s12/2026-11-17/IW_GEEKY_S12_ROT035_EXACT_RATIONAL_M13_SIX_MASK_COVARIANCE_KL_INDISTINGUISHABILITY_AND_SITE_AGGREGATION_INFORMATION_LOSS_001_20261117.md

NO Geeky original code, exact output, original geometry arrays or Q imported. Candidate exact values were treated as input hypotheses to RECOMPUTE with a separately authored SymPy verification.

## 2. Reconstructed exact six-mask source covariance model

Rebuilt ORIGINAL fixed 41^3=68921 site labels for original nested cubes k2..k6, disjoint regions ordered outer,shell1..shell5, site counts w=(18268,7778,6938,6146,5402,24389). Independently enumerated all original 6 axial, 12 face, 8 body signed unit neighbor periodic shifts at EVERY site to derive all three exact integer 6x6 region edge matrices E_a,E_f,E_b.

Define D=diag(1/w_i), G_a=D E_a D/6, G_f=D E_f D/12, G_b=D E_b D/8, K=(68921/18268)^2 e_outer e_outer^T. All EXACT RATIONAL. Hypothetical Gaussian centered RAW site energy covariance beta0 I+beta_axis A_axis+beta_face A_face+beta_body A_body, and optional independent raw FULL sixth calibration beta_cal, induce six-region mean covariance
 C=beta0(D+theta_a G_a+theta_f G_f+theta_b G_b)+beta_cal K,
where theta_kind=beta_kind/beta0>=0, sum theta<=2/5, beta0>0 and beta_cal>=0. Six region means are invertibly equivalent to five old original shell means plus hypothetical full unmasked M13 B energy. No real site data, random errors or physical additional measuring channel authenticated.

Exact TWO owner-created legal candidate parameter tuples (used solely as candidates):
 A: beta0=1, theta_axis=3/25, theta_face=1/10, theta_body=2/25, beta_cal=1/2500.
 B: beta0=99779719687217/100000000000000, theta_axis=316869474178226/2494492992180425, theta_face=93110637627687/997797196872170, theta_body=205860943554709/2494492992180425, beta_cal=1/2500.

Independent SymPy Rational confirms all exact positivity cone conditions, all SIX positive Sylvester leading principal minors for BOTH 6x6 matrices, and matrices distinct. The five exact symmetric 21-vector covariance basis columns (D,G_a,G_f,G_b,K) have rank FIVE, with 16 exact left-null falsification vectors; ALL 16 vanish on BOTH candidates. Actual exact generator identity also PASS:
 h=1/100, u0=-220280312783/10^12, v=(701212604663,-666908205953,252060167211)/10^12,
 C_B-C_A = h[u0 C_A+v_axis G_a+v_face G_f+v_body G_b-u0*(1/2500)K].
The last correction is necessary to keep ABSOLUTE raw beta_cal IDENTICAL, not just relative kappa squared.

## 3. Exact rational KL and NEW calibration-uniform strengthening

Set Delta=C_B-C_A, R=C_A^-1 Delta, Q=tr(R^2)>0 EXACT SymPy Rational. Relative whitened eigenvalues real because C_A SPD and Delta symmetric. Exact Q<10^-16 implies each relative |lambda|<10^-8. For same-mean six-variate Gaussian distributions, scalar phi(lambda)=1/(1+lambda)-1+ln(1+lambda) has rigorous bound phi<=lambda^2/[2(1-10^-8)^2]. Therefore
 KL(P_A||P_B)<=Q/[4(1-10^-8)^2].
Independently computed exact rational original scenario:
 Q≈3.41978011325726597e-17;
 KL_upper≈8.54945045413217315e-18 STRICT <1e-17.
Both strict signs are established by exact rational comparison, not eigenvalue float approximations. This independently confirms Geeky ROT035.

**NEW SOURCE CALIBRATION ROBUST NEGATIVE CERTIFICATE**: Remove the common independent sixth calibration (1/2500)K from BOTH covariance laws, maintaining unchanged source original beta0 and theta candidates:
 C_A^0=C_A-(1/2500)K, C_B^0=C_B-(1/2500)K.
Both remain exactly source legal and strictly SPD. New actual exact-rational calculation:
 Q_0=tr([(C_A^0)^-1(C_B^0-C_A^0)]^2)
      ≈4.66447375641826133e-17;
 KL_0_upper=Q_0/[4(1-10^-8)^2]
      ≈1.16611846242693446e-17 STRICT <1.17e-17.
For EVERY common known nonnegative independent Gaussian sixth raw calibration variance beta>=0, the six-variate laws with covariance C_A^0+beta K and C_B^0+beta K arise by applying the SAME independent additive Gaussian Markov kernel to the beta=0 six-variate laws. Thus KL data processing gives
  KL_beta <= KL_0 <1.17e-17 FOR ALL beta>=0.
This proves the severe statistical near indistinguishability of THESE TWO mathematically legal source models is NOT merely due to extra sixth calibration noise: it survives PERFECT sixth calibration. Not a claim about ALL legal noise models or real sensors.

## 4. Exact finite-sample necessary limits, not sufficient predictions

For n independent six-variate hypothetical repeated observations with equal priors, any binary test satisfies
 P_correct <= 1/2+1/2 sqrt(n KL_upper/2).
Consequently to attain correct classification probability at least p>1/2, it is NECESSARY that n >= 2(2p-1)^2/KL_upper, NEVER sufficient. From new better-case zero-calibration uniform source bound, strict rational floors:
 p=51%: n>68,603,664,702,729;
 p=55%: n>1,715,091,617,568,240;
 p=60%: n>6,860,366,470,272,960;
 p=75%: n>42,877,290,439,206,001.
At original fixed beta_cal=1/2500, the separate owner-case n for 60% must exceed 9,357,326,582,474,538, independently recomputed. No real observations or repeats exist in retrieved source.

## 5. Strict one-site loss retains >10^11 gap at PERFECT calibration

All original periodic one-step N41 adjacency shift matrices have zero on-site diagonal. Thus variance of a SINGLE raw site Gaussian noise is precisely beta0: A variance1, B variance99779719687217/100000000000000. For d=beta0_B-1<0, exact scalar Gaussian KL >=d^2/4 = 1.21308540499440783e-6 >1e-6. Full-site KL>=one-site by marginal data processing. Compared against new ZERO-calibration six-mask KL upper, the EXACT lower-to-upper ratio is >104,027,630,475 >10^11. First original site aggregation negative result belongs to Geeky ROT035; its survival under PERFECT calibration is a new bounded M15 source extension.

## 6. Different algorithm full original source Fourier spatial control and actual tests

Separate original-native M13 numerical program computes SIX original 41^3 region indicator 3D FFTs, uses original-site torus symbols lambda_axial=(cos kx+cos ky+cos kz)/3, lambda_face=(cos kx cos ky+cos kx cos kz+cos ky cos kz)/3, lambda_body=cos kx cos ky cos kz, and directly forms six-region covariance matrices with spectral Parseval. Original numerical 6x6 graph differences from exactly counted source matrices <=1.22e-19. Builds the tiny model perturbation DIRECTLY in Fourier space from exact owner rational candidate GENERATOR to avoid subtraction of nearly equal matrices. Independent original spatial Q_fixed≈3.4197801131174555e-17, Q_perfect≈4.664473756134807e-17; both within relative 1e-9 numerical diagnostic tolerance from exact rational. Initial overstated 2e-11 diagnostic tolerance failed and was NOT counted; corrected before clean replay.

Separate source procedure ACTUALLY synthesizes the ORIGINAL native M13 41-mode complex 3x3 Fourier B tensor into nine spatial 41^3 fields via inverse FFT; original full B energy native inner(k=0) vs spatial mean relative difference 1.11e-16, and all 5 native original k2..6 masked means vs spatial cubic direct sums agree to relative <=2.23e-16. Float64 numeric only, not proof of strict KL.

Original complete user-local 10-file self-contained source package:
 IW_M15_ROT029_EXACT_RATIONAL_M13_COVARIANCE_KL_PERFECT_CALIBRATION_REPRO_001_20261117.zip,
 28,516 bytes, SHA256 ffa51f36aa769230a7e0a89d48454dbc64ece2c46e4151a9888ead9ccab72e06.
Original unchanged M13 native source, NEW original site exact SymPy rational source verifier and full exact Q JSON, separate independent original 41^3 spatial Fourier program and complete JSON, actual 2-replay 7-attack program and receipt, full local scientific 18KB report, README, manifest. ZIP CRC PASS, 9/9 payload SHA256 PASS, 10/10 archive byte reread PASS.

ACTUALLY executed two new source Python programs in fresh isolated Python -I directories, both FULL JSON BYTE IDENTICAL (2/2). SEVEN disposable adversarial fixtures actually rejected: M13 full source one-byte corruption against each checker; original exact result JSON corruption before spectral verifier; a one-digit beta0_B wrong candidate causing exact generator identity failure; B-only changed beta_cal violating strict same known raw calibration; a false source KL<1e-19 strict claim; false original k2 site labeling. No original input changed.

## 7. Claims STOP

Source public M13 auxiliary Fourier B ONLY, not historical full DTC0a producer. Synthetic Gaussian site noise and six output source observer are not real hardware measurements; original native calc has no physical free translations/gain or extra sixth sensor. No observed IID repeated data, source noise calibration, physics of NASH K/J3/TPE, global alpha inverse or novel statistics. Original M13/Geeky ROT034/035 firstness protected. Internal nonblind different-cell I1 only, not REC13/AUD3 or blind I3 acceptance. KN15 BW native ingest unverified; GH write/Slack post not owner approval. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE.

FINAL: M15_ROT029_ORIGINAL_M13_NATIVE_B_FIVE_MASKS_PLUS_K0_ACTUALLY_EXECUTED_PASS / RANK5_16_EXACT_SOURCE_COVARIANCE_CONSTRAINTS_AND_TWO_LEGAL_RATIONAL_MODELS_I1_PASS / ORIGINAL_OWNER_KL_LESS_1E_MINUS17_PASS / NEW_PERFECT_SIXTH_CALIBRATION_KL_LESS_1P17E_MINUS17_ALL_NONNEGATIVE_COMMON_CALIBRATION_PASS / EXACT_51_55_60_75_SAMPLE_NECESSARY_GATES_PASS / STRICT_ONE_SITE_TO_SIX_KL_RATIO_GREATER_THAN_1E11_EVEN_PERFECT_CALIBRATION / INDEPENDENT_41_CUBED_SPATIAL_M13_FOURIER_PASS / TWO_COMPLETE_COLD_BYTE_IDENTICAL_JSON_PASS / SEVEN_ACTUAL_NEGATIVE_FIXTURES_REJECTED / USER_ZIP_CRC_SHA9OF9_PASS / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_CASCADE.
