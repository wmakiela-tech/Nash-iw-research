---
artifact_id: IW_M15_ROT034_ORIGINAL_M13_FIVE_MEAN_FREE_MODES_CUBIC_SPECTRAL_CALIBRATION_IV90_001_20261121
return_id: IW_M15_ROT034_FOUR_MODE_CUBIC_CALIBRATION_NO_GO_AND_FIVE_MEAN_FREE_FOURIER_RECOVERY_001_20261121
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-21
exposure: PUBLIC
class: NEW_SOURCE_CONDITIONAL_ORIGINAL_M13_NATIVE_IV90_PLUS_INDEPENDENT_FULL_41CUBED_SITE_SPATIAL
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_HISTORIC_DTC0A_PRODUCER / NO_PHYSICAL_SENSORS / NO_TASK_CASCADE
---

# M15 ROT034: Four-mode cubic spectral-calibration no-go, five-mode source recovery

## The new bounded mathematical result

**PASS.** M15 ROT033 proved a four-mode invariant under three freely fitted spectral-calibration coefficients (one log scale, one linear log-slope, one quadratic log-curvature). ROT034 introduces a fourth coefficient multiplying the CUBIC power of the axial spectral frequency symbol. The specific previously selected four source mean-free modes now have EXACTLY IDENTICAL composite zero-mean Gaussian output law families under candidate noise hypotheses A and B, because four unrestricted coefficients can match their four Gaussian variances by Vandermonde interpolation. This is a true no-go for those four selected modes at arbitrarily many independent snapshots, but NOT a universal no-go for all four-mode designs.

**NEW positive result:** add a fifth original M13 energy-mean-free Fourier mode (12,12,13). EXACT five-node barycentric weights cancel all four calibration coefficients. A 90-decimal outward interval evaluation on unchanged original public M13 source and original rational Geeky covariance witnesses certifies a nonunit remaining source covariance-shape ratio:
 q in [0.99444900986983392090649914731939148900305251011308418757706461914057524157623831734187675071379482806112458263,
       0.99444900986983392090649914731939148900305251326600573230790302871896680397854961272246611993595531451452822138],
 hence STRICT q<0.995<1.

The new fifth frequency was selected after exploratory float-based candidate examination; this is NOT an original-site globally optimal design claim or a new general theorem of mathematics.

### Original source identity and firstness

M13 FIRST native original N41 sparse Fourier B tensor source at immutable 2026-10-24 commit:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py

Original complete 8970-byte module SHA256 cd4aad089bf68e2e6155ff048d4d812943495dcf1770c8acbf0ff8111b1deb9c, original Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679. Both source identities checked before original Python import. ORIGINAL native tensor_polys(41)[1], calc(41,alpha=1/20)[1], inner(B,B,41,0,{}) were ACTUALLY executed independently in the TWO new scientific programs. Original tensor B has 41 Fourier modes and B energy has EXACTLY 221 Fourier mode differences. Historical complete dtc0a_runtime_v0_3_1.py code was NOT recovered.

Geeky-S12 ROT034 FIRST five-parameter six-mean noise covariance tomography and 16 exact constraints; Geeky ROT035 FIRST two original-source legal exact rational Gaussian RAW site covariance hypotheses; Geeky ROT036–039 FIRST distinct two-site symmetry-odd and anisotropic covariance probe design. M15 ROT030 FIRST known-scale single Fourier KL source optimum, ROT031 FIRST two-mode unknown common scale recovery, ROT032 FIRST three-mode unknown linear spectral calibration recovery, ROT033 FIRST four-mode unknown quadratic spectral calibration recovery. M15 ROT034 now supplies a NEW bounded cubic spectral stress-test for those fixed Geeky source noise witnesses. These firstness assignments remain intact. No general literature novelty or physics claim.

Two original independently produced previous M15 data certificates were SHA-locked as PARENTS, NOT falsely said freshly recomputed here:
- ROT033 full IV85 source JSON SHA256 dfbb9ac5bf50a6c772f6c4491d13c3d8d8cac504664f3dc3828ff86fafe86164;
- ROT029 exact rational original noise law JSON SHA256 00b8c93da96c9c92901555fd4c2db0af63978ecf735df3945e9ff42d218dee90.
Both complete bytes are included with the user-local runnable ZIP.

### The strictly hypothetical Gaussian covariance model

Original source grid N=41^3=68,921 raw energy lattice sites. Gaussian site-noise stationary BASE eigenvariance for source hypothesis X is

  v_X(k)=beta0_X*(1+theta_axis_X*a(k)+theta_face_X*f(k)+theta_body_X*h(k)),

where for c_j=cos(2pi*k_j/41), a=(c1+c2+c3)/3, f=(c1*c2+c1*c3+c2*c3)/3, h=c1*c2*c3.

A exact beta0=1, theta=(3/25,1/10,2/25).
B exact beta0=99779719687217/10^14, theta=(316869474178226/2494492992180425,93110637627687/997797196872170,205860943554709/2494492992180425).
Both original candidate laws are legal, strictly positive definite synthetic stationary Gaussian RAW site covariance shapes. They have the SAME deterministic original M13 mean field, no physical data.

NEW calibration eigenvariance:
 V_X(k;s,gamma,lambda,mu)=s*exp(gamma*a(k)+lambda*a(k)^2+mu*a(k)^3)*v_X(k),
 with ONE common s>0, gamma/lambda/mu arbitrary REAL shared across all selected modes WITHIN that hypothesis; each A and B hypothesis may fit DIFFERENT nuisance coefficients. It remains SPD, but generally NONLOCAL. This arbitrary source calibration shape is NOT documented native hardware or measured noise.

### Exact four-frequency no-go and exact five-frequency source recovery

Previous selected four frequencies: k0=(20,20,20),k1=(20,20,0),k2=(20,0,0),k3=(7,0,0), with four distinct a_i. The four-by-four Vandermonde basis (1,a,a²,a³) has nonzero determinant: for ANY A fitted variance quadruple there is a B nuisance quadruple matching every observed variance EXACTLY. Four modes cannot discriminate those two freely calibrated composite families, regardless of independent snapshot count.

Add k4=(12,12,13). Every one of the FIVE selected k (and its negative modulo41) is OUTSIDE the 221 original M13 B-energy Fourier differences: B tensor frequency coordinates x[-3,3],y[-2,2],z[-1,1], energy differences at most 6,4,2; all five k have an out-of-range component. Therefore deterministic mean of every normalized original energy Fourier cosine/sine projection is EXACT ZERO for every original alpha and a common torus translation or gain.

Define exact barycentric weights b_i=1/prod_(j!=i)(a_i-a_j), w_i=b_i/b_4; w4=1 EXACT. Approximate weights:
  w=(+0.008380890568890344, −0.983380364217605392, −0.032842293431916338, +0.007841767080631386, +1).
ACTUAL generic SymPy five-node proof:
 sum_i b_i*a_i^p=0 EXACT for p=0,1,2,3;
 sum_i b_i*a_i^4=1 EXACT.
Thus the calibrated log-variance sum cancels source log(s), gamma*a, lambda*a², mu*a³ for EACH hypothesis, but NOT an unconstrained quartic calibration. The strict q_IV90 interval above is from ORIGINAL M13 source and source exact rational Gaussian A/B shapes, not arbitrary site model or actual physical noise. Its log lies in strict negative IV90 around -0.00556645412943441942057.

### Achievable Gaussian binary test, strictly conditional

Assume n IID FULL RAW SITE 41³ spatial Gaussian observations (or exactly measured five orthonormal Fourier cosine/sine pairs) from one of the TWO fixed noise-shape hypotheses. Each of five pairs is independent within a candidate. Let S_i be its cosine-square-plus-sine-square sum across the n snapshots. Let

  T=prod_i (S_i/v_A(k_i))^w_i.

Under A, T is distributed as prod_i U_i^w_i; under B it equals in distribution q*prod_i U_i^w_i, where U_i are independent chi-square_(2n). These laws are EXACTLY invariant to the arbitrary four fitted spectral-calibration nuisance coefficients. Select B iff T<sqrt(q).

With delta=1/850, P=sum positive w_i≈1.01622265764952, the ORIGINAL strict source-IV90 checks:
  ((1-delta)/(1+delta))^(2P)-q > 0.0007801802913477323.
On a simultaneous 1±delta chi-square concentration event the A and B T ranges are strictly disjoint at sqrt(q). Chi-square Chernoff/union gives per-candidate error:
  P(error|X) <= 10 exp(-n*delta²/4).

Actual strict IV90 finite-N sufficient (NOT necessary and NOT physical):
  n=12,000,000 -> each candidate correct >75%, bound error<0.157291;
  n=14,000,000 -> >90%, error<0.078733;
  n=16,000,000 -> >95%, error<0.039410;
  n=21,000,000 -> >99%, error<0.006986.

The design having better conservative numbers than a different four-mode quadratic example ROT033 does NOT imply that estimation with a cubic nuisance is uniformly easier. The observation frequencies changed, and no cross-design optimality theorem is asserted.

### Independent spatial original M13 FFT/GLS controls

SECOND new source Python program ACTUALLY imported and executed unchanged original M13, synthesized all N41³ spatial values of nine complex tensor B field components with full 3D inverse FFT, and constructed TEN normalized original-site real cos/sin projector arrays for selected frequencies. Its original deterministic B energy has projected means |Z|~1e-26 on the five chosen frequencies (FLOAT numeric support-zero control). It independently computed complete 10×10 Gaussian projected covariance matrices with ACTUAL 6 axial,12 face,8 body signed neighbor SITE ROLLS and a separate FFT convolution filter exp(gamma*a+lambda*a²+mu*a³). This second algorithm does NOT import new IV90 eigenvalue rows as inputs. Its 4×5 calibration moment null weights came from independent floating SVD, not the primary symbolic barycentric weights.

THREE CALIBRATION SCENARIOS actually checked in source space:
 - A=B fitted (s,gamma,lambda,mu)=(1,0,0,0) -> q_spatial≈0.9944490098698339;
 - A=B fitted (2.1,.3,-.2,.1) -> q≈0.9944490098698338;
 - A fitted (.35,-.6,.5,-.3), B fitted (2.1,.3,-.2,.1) -> q≈0.9944490098698339.

All six projected 10x10 covariance matrices numerically SPD, off-diagonal abs <5e-12, SVD null moment residual <2e-15, independent q values meet predeclared float diagnostic relative tolerance 3e-10 against strict source IV90. FLOAT64 FFT and SVD are independent diagnostics, NOT proof of the interval bounds.

### Actual independently reproducible source code, replay and nine falsifiers

User-local COMPLETE reproducibility ZIP:
 IW_M15_ROT034_ORIGINAL_M13_CUBIC_SPECTRAL_CALIBRATION_FIVE_MEAN_FREE_MODES_IV90_REPRO_001_20261121.zip
 Actual ZIP 45,885 bytes; SHA256 a7c50c851e62ed2faf5bf5983ed2eb968a825a612dff3aad2f987532c7925ed5.
 Contains 13 archived files: unchanged M13 native source, two locked prior machine source certificates, two newly authored ACTUALLY executed source math programs and both COMPLETE full JSONs, executable cold replay with NINE real adversarial fixtures and resulting receipt, detailed local science report, README, archive builder and SHA256 manifest. ZIP CRC PASS; 12/12 individual payload SHA256 PASS; 13/13 full archive byte re-read PASS.

Main new source IV90 executable SHA256 a236c7bf81fc042a209fe03b7a62b1d055fa933d242732a8ad0b8afaf765a109; full actual directed IV90 JSON SHA256 bae8a0810893cfe2a67af9c90a0e263f7cd710445f53663938f7e909be1c3870.
Separate original spatial 10×10 executable SHA256 2feacfd9c78846753f7d0705b62aeec31d64ce45ca41f0363ca6c2af6997c108; complete actual spatial JSON SHA256 a4291d3fddfaa1b4207ae5b18e715c264aea3dea02f27401d3e541c5db6c252f.
Actual cold replay and negative receipt SHA256 b51bf0f549a5ae76b31aa435c689563e5910d6403800eeea3703b1eccc36126e.

BOTH complete scientific result JSONs genuinely regenerated BYTE-IDENTICAL by isolated Python -I reruns in clean folders: 2/2 PASS. NINE actual disposably modified negative fixtures 9/9 REJECTED with expected named guards:
 - original M13 one-byte tampering against BOTH programs;
 - parent ROT033 IV85 data tamper;
 - original parent ROT029 exact-rational data tamper;
 - new IV90 result one-byte tamper before spatial checker;
 - false original source mode k=(0,0,0) claimed mean-free;
 - false source q<0.99 claim;
 - false 99% success with n=100 claim;
 - false fourth-degree spectral-calibration cancellation.
No original files were mutated in source custody. An earlier overlong replay invocation was interrupted without a success claim; subsequently the full replay completed with 2/2 and 9/9.

### Scope ceiling and handoff

Only ORIGINAL M13 publicly visible AUXILIARY mathematical Fourier field, not complete historic dtc0a runtime. No authenticated physical M13 RAW spatial energy recorder with 68,921 sites, five Fourier mode sensors, real Gaussian stochastic noise, full unrestricted cubic spectral calibration, instrument readout rates, actual IID 12–21 million snapshots, general inverse uniqueness or NASH K/J3/TPE/GR/GW physics. No literature novelty, general optimal sample count, global minimum number of modes or external blind I3. Geeky ROT034–039 original scientific firstness preserved. Internal source-level result, independent REC13/AUD3 acceptance and KN15 native BW provider ING receipt NOT verified. GitHub publication and Slack dispatch do not constitute owner ACK or CANON. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE.

FINAL:
 M15_ROT034_ORIGINAL_M13_NATIVE_GIT_SHA_LOCK_EXECUTED_PASS /
 CUBIC_COLORED_OLD_FOUR_SELECTED_MODES_EXACT_COMPOSITE_NO_GO_PASS /
 FIVE_ORIGINAL_B_ENERGY_MEAN_FREE_MODES_PASS /
 EXACT_FIVE_NODE_SYMBOLIC_POLYNOMIAL_DEGREE_0_TO_3_NULL_PASS /
 NEW_SOURCE_IV90_FIVE_MODE_Q_STRICTLY_BELOW_0P995_PASS /
 FOUR_STRICT_FINITE_N_SOURCE_GATES_PASS /
 INDEPENDENT_41CUBED_FULL_10X10_SPATIAL_THREE_CALIBRATIONS_PASS /
 TWO_FULL_JSON_BYTE_IDENTICAL_CLEAN_REPLAYS_PASS /
 NINE_REAL_SOURCE_AND_SCIENCE_NEGATIVE_FIXTURES_REJECTED /
 ZIP_CRC_SHA12_OF12_PASS /
 BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE.
