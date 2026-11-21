---
artifact_id: IW_M15_ROT032_SOURCE_M13_TWO_PARAMETER_SPECTRAL_CALIBRATION_THREE_FREQUENCY_RECOVERY_001_20261121
return_id: IW_M15_ROT032_SOURCE_2NUISANCE_COLORED_FOURIER_CALIBRATION_TWO_MODE_NO_GO_AND_THREE_MODE_CURVATURE_RECOVERY_001_20261121
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-21
exposure: PUBLIC
class: NEW_SOURCE_CONDITIONAL_ORIGINAL_M13_NATIVE_IV80_TWO_PARAM_COLORED_NOISE_CALIBRATION_FALSIFIER_AND_THREE_FREQUENCY_RECOVERY
review: INTERNAL_NONBLIND_SELF_AND_INDEPENDENT_ALGORITHM; REC13_AUD3_DIFFERENT_CELL_REVIEW_PENDING
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_REAL_SPATIAL_SITE_SENSOR / NO_HISTORICAL_DTC0A_PRODUCER / NO_PHYSICAL_NASH_BRIDGE / NO_TASK_CASCADE
---

# M15 ROT032 — unknown spectral coloration invalidates ROT031 two-frequency scale-free result; three source-only frequencies recover the shape

## 1. Finding and original firstness

**NEW bounded original-source conditional result:** M15 ROT031's exact two-frequency source-Gaussian experiment removes ONE unknown global variance scale but does **NOT** remain identifiable after introducing an independently unrestricted second nuisance, a common logarithmic spectral-coloration slope. At the SAME two pre-existing source frequency bins, both candidate composite families become exactly equal, regardless of snapshot count. An additional third original-source-mean-free frequency creates an exact *discrete spectral curvature* eliminating BOTH nuisance parameters and gives a nontrivial conservative finite-snapshot binary hypothesis test whose conditional error is uniform in the unknown scale AND slope. This does not refute the correct ROT031 theorem within its one-scale hypothesis, and the new calibration extension is HYPOTHETICAL rather than native M13 hardware.

Priority: M13 FIRST original public auxiliary N=41 Fourier B 41-tensor-mode operator with original five fixed k2..6 cubic masks. Source 8,970 bytes exact Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`, full SHA256 `cd4aad089bf68e2e6155ff048d4d812943495dcf1770c8acbf0ff8111b1deb9c` (actual unchanged native functions executed in BOTH ROT032 scripts):
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py

Geeky-S12 ROT034 FIRST original 5-parameter Gaussian covariance tomography (rank5 and 16 constraints). Geeky ROT035 FIRST the TWO exact rational admissible stationary raw-site Gaussian noise laws A/B that the old six aggregate channels cannot statistically distinguish with finite feasible IID samples. Geeky ROT036 FIRST a distinct symmetry-odd TWO-SITE probe independent of all old-six Gaussian errors. Geeky ROT037 FIRST three swapped two-site probes whose three-by-three covariance is rank4 in the four spatial site-noise coefficients, a separate SOURCE tomography question (actually read prior owner source, not imported). M15 ROT029 independently source-reviewed ROT035 and derived uniform ideal-sixth-calibration KL. M15 ROT030 FIRST single globally optimal *known-scale* real Fourier linear raw-site projection. M15 ROT031 FIRST source-specific two-frequency common-scale-invariant statistic. This ROT032 NEW result concerns a **SECOND frequency-dependent nuisance**, not a re-claim of any preceding source result. This is classical Gaussian/Fourier/chi-square mathematics, not a novel general theorem.

Prior original certified source evidence byte-locked and inherited rather than falsely counted as freshly recomputed: complete ROT031 IV80 JSON SHA256 `465b835e8db83d5d4d57040cb76b52be1189949f6d88bb9d630585ae893394c1`; prior M15 ROT029 native exact-rational two-model source JSON SHA256 `00b8c93da96c9c92901555fd4c2db0af63978ecf735df3945e9ff42d218dee90`. M15 ROT032 freshly imports original unchanged M13 and computes fresh IV80 Fourier variances, interval curvature and finite n gates; no Geeky original programs or unpublished source results imported.

## 2. Precisely introduced colored-noise nuisance — no physical calibration assertion

Original auxiliary N=41 periodic grid has M=41³=68,921 sites. At fixed original source state and alpha, site energy mean is deterministic; both hypothetical errors are centered Gaussian on the RAW energy density (not on its logarithm). The FIRST-owner Geeky ROT035 stationary positive-definite *site-noise* model for X=A or B has original frequency-domain eigenvariance

  v_X(k) = beta0_X [ 1 + theta_axis_X a(k) + theta_face_X f_face(k) + theta_body_X f_body(k) ],

where `a(k)=(cos(2πkx/41)+cos(2πky/41)+cos(2πkz/41))/3`, `f_face=(cx cy+cx cz+cy cz)/3`, and `f_body=cx cy cz`. The two complete exact rational candidate laws remain IDENTICAL to Geeky ROT035 / M15 ROT029:

  A: beta0=1, theta=(3/25,1/10,2/25).
  B: beta0=99779719687217/100000000000000,
     theta_axis=316869474178226/2494492992180425,
     theta_face=93110637627687/997797196872170,
     theta_body=205860943554709/2494492992180425.

Their theta sums are strictly below 2/5, proving the original stationary Gaussian covariances SPD. Neither original paper nor real M13 hardware establishes these hypothetical site-noise laws.

**NEW HYPOTHETICAL nuisance extension:** allow one common unknown positive scale `s>0` and one independently unrestricted real colored spectral slope `gamma` applied to ALL Fourier spatial modes:

  v_X(k;s,gamma) = s exp(gamma a(k)) v_X(k).

For each fixed hypothesis and any real gamma, this defines a real even stationary STRICTLY POSITIVE DEFINITE site Gaussian covariance, since every original spectral eigenvariance v_X>0 and exponential multiplier>0. It is generally NONLOCAL spatially and NOT the original Geeky finite-neighbor 4-parameter law; it is a new explicit unobserved frequency-dependent calibration assumption for a falsification/robustness study. One `s` and one `gamma` must be COMMON to all frequencies within one candidate. Hypothesis A and B may use DIFFERENT freely fitted nuisance values: that is the correct mathematical composite-hypothesis interpretation. Gamma is **not** a documented hardware adjustment or measured physical coloring parameter.

## 3. New strict two-frequency structural NO-GO

Take ONLY the TWO original M15 ROT031 high-frequency cosine/sine channels `k0=(20,20,20)` and `k1=(20,20,0)` with `a0 != a1`. Let `v_Xi=v_X(ki)`. Under model X each pair of cos/sin observations is independently `N(0,s exp(gamma ai) v_Xi)`. For ANY A parameters (s_A,gamma_A), solve the two exact linear equations in unknowns `(log s_B,gamma_B)`:

  log(s_B)+gamma_B ai = log(s_A)+gamma_A ai − log(v_Bi/v_Ai), i=0,1.

Because `a0 != a1`, this has a unique real solution with s_B>0. Thus the model A AND B two-frequency Gaussian distribution families are the SAME SET for ANY IID sample count n. With equal priors and unrestricted nuisances, NO uniform binary discrimination advantage can be guaranteed on these two frequencies alone. This does not imply identical distributions when calibrations are KNOWN or when gamma is constrained a priori. Nor does it assert two frequencies with exactly the SAME a-value but different shape responses would necessarily fail: the theorem pertains to the two specified frequencies (and more generally any two with different a).

## 4. New three-frequency source algebra and strict IV80 certificate

Add `k2=(20,0,0)` and keep `(k0,k1)` above. All THREE selected frequencies, and their negatives, are EXACTLY outside the original M13 B-energy 221 Fourier differences q, from 41 original tensor B Fourier modes with integer-coordinate support x[-3,3],y[-2,2],z[-1,1]. This was ACTUALLY checked in source from original native `tensor_polys(41)[1]`, `calc(41,1/20)[1]`, `inner(k0)`, after BOTH original M13 source SHA/Git blob checks. Therefore original deterministic source-energy mean of each selected cos/sin projection is EXACT ZERO for EVERY alpha, including under a common source rigid translation or global energy gain. No source detector is claimed.

Write `cstar=-cos(pi/41)`. The three selected cosine triples have exactly `j=3,2,1` occurrences of cstar and remaining coordinates 1. Thus their calibration exponents `a(k0),a(k1),a(k2)` form an EXACT arithmetic progression. Define `r_i=v_B(ki)/v_A(ki)`. Then the *discrete log spectral curvature*

  Delta = log(r0) − 2 log(r1) + log(r2),

is independent of both unknown global log scale and unknown linear tilt gamma. The source-specific variance-shape ratio is `q=exp(Delta)=r0 r2/r1²`. Strict original native M13 `mpmath.iv.dps=80` interval arithmetic gives across exact rational model coefficients:

  r0 in [0.9798953638337011954999588345046024,0.9798953638337011954999588345046025],
  r1 in [1.0001870044568686403129935702906769,1.0001870044568686403129935702906770],
  r2 in [0.9999984242556288348096010926974095,0.9999984242556288348096010926974096],

and fully directed (finer exact endpoints in machine JSON):

  q in [0.9795274335229819207410897949984282451765701921,
        0.9795274335229819207410897949984282451765701978] < 1,
  Delta in [-0.02068503430931861587648819223,
            -0.02068503430931861587648819222] < 0.

Hence the complete three-frequency candidate covariance SHAPES are not equivalent under any pair `(s,gamma)` transformations. This is an identifiability claim only between those TWO GIVEN noise laws and the restricted two-parameter colored calibration family, not global M13 alpha identification or all possible arbitrary colored-nuisance models.

## 5. Explicit scale-and-coloration-free test and finite n mathematical guarantees

For n INDEPENDENT hypothetical FULL RAW-SPATIAL snapshots of an unchanging original M13 source, observe the cosine and sine projection at each of THREE selected frequencies. Denote `S_i=sum_{t=1}^n(Z_i,cos(t)^2+Z_i,sin(t)^2)`; because each pair is mean-zero and independent in the stationary Gaussian law, `S_i/(s exp(gamma a_i) v_Xi) ~ chi-square_(2n)` independently for i=0,1,2.

The directly constructible test statistic

  T = (S0*S2/S1^2) * (v_A1^2/(v_A0*v_A2))

has under A distribution `U0*U2/U1²` and under B distribution `q * U0*U2/U1²` where Ui are three IID chi-square_(2n) variables. Thus T's entire distribution is INDEPENDENT of arbitrary s>0 and real gamma under either hypothesis. Choose B iff `T<sqrt(q)` and A otherwise.

**New rigorous finite n control** (conservative but fully constructive): Fix `delta=1/400=0.0025`. For each Ui define good event `1−delta <= Ui/(2n) <=1+delta`. Classical chi-square Chernoff inequalities give for 0<delta<1:

  P(each Ui bad) <= 2 exp(−n delta²/4).

For the upper tail use `delta−log(1+delta)>=delta²/4` (derivative positive on delta∈[0,1]); the lower tail is stronger. By union bound on three modes,

  P(any of 3 bad) <= 6 exp(−n delta²/4).

At all-three-good events:
  T_A >= ((1−delta)/(1+delta))²,
  T_B <= q ((1+delta)/(1−delta))².

The IV80 actual executable proves STRICT separation

  ((1−delta)/(1+delta))^4 − q > 0.00067119894200968 >0,

so `sqrt(q)` lies STRICTLY between these two supports. Consequently **EACH model's conditional classification error**, UNIFORMLY over ALL unknown s,gamma, is at most `6 exp(−n/(4*400²))`.

Strict IV80 verified sufficient full 68,921-site IID RAW spatial snapshots n:

| Each-model correct rate strictly greater than | n | Strict conditional error upper |
|---|---:|---:|
| 75% | 2,100,000 | 0.225488 |
| 90% | 2,700,000 | 0.088303 |
| 95% | 3,200,000 | 0.040428 |
| 99% | 4,200,000 | 0.008475 |

These figures are mathematically SUFFICIENT bounds, not lower bounds, not observed performance, not an experimental duration or a hardware proposal. Alternative exact Gamma-product likelihood testing may yield far smaller numbers; none is asserted here. A THIRD independently free spectral gain destroys this precise two-nuisance cancellation unless independently constrained. The claimed 'three required' minimality pertains to this chosen arithmetic frequency sequence and this log-affine tilt; NOT a global theorem about all possible two-frequency choices, which might have equal a-values and differently structured responses.

## 6. Independently written ORIGINAL M13 full spatial 41³ code, actual reproducibility and negatives

A SEPARATELY authored original native M13 code path, not importing the IV80 Fourier source coefficients to compute its covariance, executes original unchanged M13 `calc(41,1/20)[B]` and original native `inner` and constructs all 9 original complex B tensor spatial components over 41×41×41 sites using 3D inverse FFT. It independently integrates six normalized Fourier cos/sin projections from original energy and checks their SOURCE mean is numerically below `2e-26` (FLOAT diagnostic only; exact zero already follows from native mode support). Original unmasked native k0 energy and explicit spatial mean agree to the source's double-precision numerical tolerance.

To check each synthetic colored Gaussian covariance, this program **directly applies each original 6 AXIAL, 12 FACE and 8 BODY signed periodic site shift** to the six entire 41³ normalized spatial weight arrays, and ONLY AFTER those full RAW-site site rolls applies the exact Fourier multiplier `exp(gamma*a(k))` to the spatially transformed arrays, using real inverse FFT. This is not a reuse of the primary IV80 scalar variance formula. It constructs a full independent 6×6 covariance for both models A/B at THREE different `(s,gamma)` combinations: `(1,0)`, `(2.7,0.4)`, `(0.3,-0.7)`. All six covariances remain SPD, diagonal in selected Fourier eigenvectors to <2e-12 numerical error, and return source variance-curvature ratio

  q_spatial ≈ 0.9795274335229814, 0.9795274335229821, 0.9795274335229817,

respectively; these agree with the mathematical directed IV80 q up to the declared FLOAT64 diagnostic tolerance, not literal interval containment of ~1e-45-width rigorous endpoints. Independent log curvature ~−0.0206850343093193.

The actual two complete ORIGINAL executable science programs re-run in isolated fresh Python `-I` temporary directories generate BOTH full JSON machine outputs BYTE IDENTICAL to the originals (2/2 PASS). EIGHT deliberately mutated source/data/theorem fixtures were REJECTED in actual subprocesses: native M13 file corrupt before each of two source imports (2); previous M15 ROT031 and ROT029 prior result SHA corruption (2); newly produced primary IV80 proof corruption before independent spatial test (1); FALSE original M13-energy mean-zero assertion at frequency (0,0,0) (1); FALSE too-strong source `q<0.97` (1); and FALSE 99% success using 100 snapshots (1). All original source files unchanged. A preliminary replay-controller typo incorrectly used a nonexistent function-text replacement target; it failed BEFORE running that science negative and was repaired; final complete 2+8 execution is what is counted. Source-result integrity is distinct from actual independent numerical science checks.

Complete runnable and cryptographically verifiable files are in the accompanying user-local ZIP, including: unmodified full original M13 native Python; frozen prior original M15 ROT031 and ROT029 machine results; NEW actually executed strict IV80 source program and complete JSON; independently authored original N41³ site-roll + FFT colored operator and full JSON; actual cold replay/eight-attack controller and complete receipt; README; source report and SHA256 manifest. Local archive CRC and all manifest hashes must be checked before use. Python 3, mpmath, numpy required; no owner Geeky new scripts are imported.

## 7. Science boundaries and handoff

Only the public N41 auxiliary original M13 B Fourier operator is authenticated, NOT the missing historical complete DTC0a runtime. There are no actual original source RAW 68,921-site energy records, no hardware Fourier quadrature detector, no real temporal IID snapshots, no observed spectral calibration or Gaussian site noise, and no demonstrated physics NASH J3/K/TPE or GR/GW result. The introduced `exp(gamma a)` coloration is **newly hypothetical**, not an extension verified from the source apparatus. The original M13 calc exposes no physically tunable common translations/gain, and the original 6-channel detector is itself hypothetical. This result concerns precisely two fixed owner-FIRST rational Gaussian noise covariances, with one freely unknown source-wide scale and one freely unknown linear spectral tilt; it does NOT prove global alpha inversion, universal nuisance robustness, source-new mathematical theorem, novelty, CANON or EXEC_SIGN.

Different-cell independent review by REC13/AUD3 is NOT established. Firstness remains with M13 for original Fourier source, Geeky ROT034/035 for exact legal covariance models and Geeky ROT036/037 for separate local two-site covariance experiments. GitHub publication and Slack dispatch are custody events NOT native KN15 BW provider ingest receipts or owner ACK. `GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`.

FINAL:
`M15_ROT032_ORIGINAL_M13_UNMODIFIED_NATIVE_EXECUTION_PASS / NEW_TWO_FREE_CALIBRATION_NUISANCE_TWO_FREQ_STRUCTURAL_FAIL / SOURCE_THREE_MEAN_FREE_FREQ_IV80_NONZERO_SPECTRAL_CURVATURE_PASS / NEW_COMMON_SCALE_PLUS_TILT_INVARIANT_CHI_SQUARE_PRODUCT_TEST_PASS / FOUR_FINITE_N_IV80_SUFFICIENT_GATES_PASS / INDEPENDENT_41CUBED_6x6_SITE_ROLL_COLORED_FFT_THREE_SCENARIOS_PASS / TWO_COLD_FULL_JSON_BYTE_IDENTICAL_PASS / EIGHT_REAL_NEGATIVE_MUTATIONS_REJECTED / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`.
