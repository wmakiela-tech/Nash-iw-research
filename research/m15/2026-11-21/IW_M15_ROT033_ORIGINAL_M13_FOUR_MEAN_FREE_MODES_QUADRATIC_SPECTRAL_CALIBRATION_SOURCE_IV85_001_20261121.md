---
artifact_id: IW_M15_ROT033_ORIGINAL_M13_FOUR_MEAN_FREE_MODES_QUADRATIC_SPECTRAL_CALIBRATION_SOURCE_IV85_001_20261121
return_id: IW_M15_ROT033_ORIGINAL_M13_QUADRATIC_COLORED_SPECTRAL_NOISE_THREE_MODE_NO_GO_FOUR_MEAN_FREE_MODE_RECOVERY_001_20261121
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-21
exposure: PUBLIC
class: ACTUALLY_EXECUTED_ORIGINAL_M13_NATIVE_SOURCE_IV85_PLUS_INDEPENDENT_41_CUBED_SPATIAL_SOURCE
sync: GITHUB_PENDING_BW_INGEST
ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_SENSOR / NO_FULL_DTC0A_PRODUCER / NO_TASK_CASCADE
---

# M15 ROT033 — Three unknown spectral-calibration parameters: exact three-mode failure and four mean-free mode recovery

## Decision, firstness, provenance

NEW source-conditional mathematical source result, not a physical experiment nor a general novel theorem. The M15 ROT032 three selected Fourier modes distinguish two fixed source-legal Gaussian site noise models A/B when the entire spectrum has just a freely unknown overall scale s and linear axial-color tilt gamma. M15 ROT033 FIRST tests an additional arbitrarily unknown quadratic spectral calibration lambda*a(k)^2. For those three PRESELECTED modes, the two composite Gaussian observation law families coincide EXACTLY, regardless of IID sample count. A fourth original-source mean-free mode k=(7,0,0) permits explicit cancellation of all three calibration nuisances and proves nonzero residual covariance-model discrimination with an IV85 source certificate.

Priority: ORIGINAL M13 FIRST original N=41 41-mode Fourier B auxiliary source; Geeky-S12 ROT034 FIRST five-parameter old-six mask covariance tomography; Geeky ROT035 FIRST two exactly rational legal RAW site Gaussian covariance hypotheses and six-mask KL negative; Geeky ROT036/037 FIRST distinct two-site symmetry-odd local-probe results, ROT038 FIRST its anisotropic site-covariance boundary result. M15 ROT030 FIRST known-scale globally optimal SINGLE raw Fourier Gaussian KL projection, ROT031 FIRST TWO frequency shared unknown-scale invariant, ROT032 FIRST THREE frequency linear-color tilt invariant. All firstness retained. This is new only as the bounded original M13 source-case polynomial-color diagnostic, not literature priority.

Original source M13 public Python Git original 8970 bytes, Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679, complete original-source SHA256 cd4aad089bf68e2e6155ff048d4d812943495dcf1770c8acbf0ff8111b1deb9c. Identity checked BEFORE original source import. ACTUALLY EXECUTED unchanged original tensor_polys(41)[1], calc(41,alpha=1/20)[1], and native inner(B,B,N41,k0) in both new programs; original q-support count 221 from 41 B modes ACTUALLY verified. Original helper:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py

Original prior M15 ROT032:
https://github.com/wmakiela-tech/Nash-iw-research/blob/a86ff6de3e9797a25280cb92d7704d1942561c44/research/m15/2026-11-21/IW_M15_ROT032_SOURCE_M13_UNKNOWN_TWO_PARAMETER_SPECTRAL_CALIBRATION_THREE_FREQUENCY_RECOVERY_001_20261121.md
Prior complete IV80 machine JSON SHA256 161500d8fe93c16b5bd385ba9a2e9b0dce1e3ef82ff03ef9cd7c4d6645ef232e, prior original M15 ROT029 exact two Gaussian rational witnesses machine JSON SHA256 00b8c93da96c9c92901555fd4c2db0af63978ecf735df3945e9ff42d218dee90. Both parents integrity-frozen and reused AS PRIOR inputs, not falsely claimed freshly recomputed; new original native support and spectral IV85 are recomputed.

## Statistical object and exact hypotheses

Public original M13 N=41 periodic site grid has 41^3=68921 points. Its deterministic B energy is an ORIGINAL auxiliary model source mean; it is not a recorded detector value. Two original Geeky-FIRST legal stationary Gaussian RAW SITE ENERGY noise spectra are v_X(k)=beta0_X*[1+theta_axis_X*a(k)+theta_face_X*f(k)+theta_body_X*h(k)], where a=(cx+cy+cz)/3, f=(cx cy+cx cz+cy cz)/3, h=cx cy cz and c_i=cos(2pi*k_i/41). Candidate A beta0=1 and theta=(3/25,1/10,2/25); B beta0=99779719687217/10^14 and theta=(316869474178226/2494492992180425,93110637627687/997797196872170,205860943554709/2494492992180425). Strict legal source cone ensures v_X(k)>0 everywhere. Their deterministic mean source is exactly the SAME original M13 field.

NEW hypothetical colored calibration: each candidate X has THREE freely fitted real nuisance coefficients log(s_X),gamma_X,lambda_X, s_X>0, multiplying each eigenvariance by s_X*exp(gamma_X*a(k)+lambda_X*a(k)^2). This more general spectral covariance is SPD but generally NONLOCAL in raw site space. It is NOT a measured source calibration or a native DTC0a noise mechanism.

## Negative result: selected old three frequencies cannot identify composite models

Old ROT032 selected k0=(20,20,20), k1=(20,20,0), k2=(20,0,0). These have three distinct axial a(k). At these three modes, each model produces centered independent cosine/sine Gaussian modes with log variance log(s_X)+gamma_X*a_i+lambda_X*a_i^2+log(v_X(k_i)). The three-by-three Vandermonde matrix for (1,a_i,a_i^2) has nonzero determinant. Thus for EVERY fitted A triple there is a unique B triple making ALL THREE variances exactly identical. The two composite distribution families on those three mode pairs are IDENTICAL, even over arbitrarily many IID repetitions. This is not a no-go for all possible triples of raw frequencies or nonlinear observers. It falsifies ONLY the extrapolation of ROT032 to a third, previously unrestricted nuisance.

## Positive result: source-fourth energy-mean-free mode and exact interpolation nullspace

Choose FOUR source frequencies:
k0=(20,20,20);
k1=(20,20,0);
k2=(20,0,0);
k3=(7,0,0).

The ORIGINAL native B source Fourier support coordinate ranges are x in [-3,3], y in [-2,2], z in [-1,1]; its energy support consists of 221 original mode DIFFERENCES. Each of four k_i and its modulo41 negative lies OUTSIDE that set. In particular, the x=7 fourth frequency is outside source B-energy x differences, whose max absolute coordinate is 6. Therefore all eight normalized REAL cosine/sine projections of the original deterministic B energy have EXACT mean zero for ALL alpha and for common phase translations/gains. This avoids the k=(0,0,0) nonzero-signal confounder and the need to assume extra temporal source-mean stability. The zero mean is exact support algebra; floating FFT amplitude ~1e-26 is ONLY a diagnostic.

For four DISTINCT axial spectral symbols a_i=a(k_i), define exact barycentric weights b_i=1/product_{j!=i}(a_i-a_j), w_i=b_i/b_2. Lagrange interpolation yields EXACTLY sum_i w_i*a_i^p=0 for p=0,1,2. This was ACTUALLY proved by SymPy rational functions in four free symbolic nodes, rather than testing only numeric cancellation. Approximate source weights:
w0=+0.26966683893956436;
w1=-0.84956724289906543;
w2=+1 EXACT;
w3=-0.42009959604049894.
All four weights retain these signs throughout native IV85 enclosure.

Let r_i=v_B(k_i)/v_A(k_i). The scale, linear tilt and quadratic tilt exponent contributions CANCEL ALGEBRAICALLY from the variance statistic q=product_i r_i^(w_i), even when the three nuisance coefficients are separately fitted under A and B. Actually executed original-native source IV85 outward bounds over exact M13 geometry and exact original Geeky rational covariance candidates:
q in [0.9943787634148084305991653335106472354260431696254894432471,0.9943787634148084305991653335106472354260431734790602201405] STRICT less 0.995;
log q in [-0.00563709519348059044293861555727131194845772994836785722,-0.00563709519348059044293861555727131194845772618306246211] STRICT negative.
Thus the two exact source-legal Gaussian site covariance hypotheses remain statistically different AFTER eliminating all THREE nuisance calibration parameters in THIS specifically chosen four-mode observation design.

## Constructive exact binary test and sufficient sample count

For n independent WHOLE 68921-site hypothetical Gaussian RAW energy snapshots, each observed mode supplies two orthogonal independent normalized cosine and sine errors. Let S_i be the sum of their squares over n snapshots at mode k_i. Define T=product_i (S_i/v_A(k_i))^(w_i). Under A T has distribution product_i U_i^(w_i), under B it has distribution q times product_i U_i^(w_i), where each U_i is independent chi-square with 2n degrees of freedom. The composite Gaussian law of T is independent of each model's unrestricted s,gamma,lambda because of the exact interpolation nullspace. Decide B iff T<sqrt(q), otherwise A.

Let delta=1/950, P=sum positive weights=-sum negative weights~1.26966683893956436. On event every U_i/(2n) in [1-delta,1+delta], T_A>=((1-delta)/(1+delta))^P>sqrt(q), whereas T_B<=q*((1+delta)/(1-delta))^P<sqrt(q). Original source directed IV85 strictly proves ((1-delta)/(1+delta))^(2P)-q >0.00028953322783450843. Chi-square concentration and union over four mode pairs give EACH candidate conditional error <=8exp(-n delta^2/4) UNIFORMLY in all common-per-candidate s,gamma,lambda.

Original IV85 verifies SUFFICIENT (not necessary) full RAW IID site snapshot counts:
n=13,000,000 => each-model correct rate >75%, error <0.218348;
n=17,000,000 => >90%, error <0.072101;
n=20,000,000 => >95%, error <0.031407;
n=25,000,000 => >99%, error <0.007862.
No real site measurement, independent repeat time series or instrument throughput is evidenced. These very large hypothetical n are NOT claims of practical experiment feasibility.

## Independently authored ORIGINAL M13 spatial Fourier/stencil validator

A SECOND new Python program independently imports and ACTUALLY runs unchanged native M13 to construct nine complex B tensors on all original 41^3 spatial sites by 3D inverse FFT, then eight normalized cosine/sine spatial weights. It computes original B energy and their eight source projections directly; their float64 means are 1e-26 or smaller. It builds FULL 8x8 Gaussian RAW-site spectral-observer covariance by actual spatial array rolls for ALL original 6 AXIAL, 12 FACE, 8 BODY signed neighbor displacements, followed by an independently implemented spatial Fourier filter exp(gamma*a+lambda*a^2). This does NOT import IV85 coefficients or primary score arrays. It independently derives four calibration-null weights from the numerical SVD of a 3x4 polynomial moment matrix, with moment residual <2e-15 and agreement with the symbolic weights.

THREE unlike entire-site calibration scenarios ACTUALLY CHECKED:
zero color A=B:(s,gamma,lambda)=(1,0,0) -> q=0.9943787634148079;
shared color A=B:(2.7,0.4,-0.25) -> q=0.9943787634148085;
different color A:(0.3,-0.7,0.6) and B:(2.7,0.4,-0.25) -> q=0.9943787634148078.
All three numeric values within declared relative 2e-10 diagnostic tolerance of original source IV85 result. All 8x8 covariances SPD, all offdiagonal cross-mode covariance residuals <3e-12. FLOAT64 does not prove the source IV85 interval.

## Actual reproducibility, nine named negative controls and custody

Two original newly written scientific scripts ACTUALLY executed and were then independently COLD rerun under python -I in newly created TEMP directories. Both COMPLETE resulting JSON artifacts were BYTE IDENTICAL: 2/2 PASS. NINE real disposable intentional mutations were checked for NONZERO exit AND the expected explicit fail-closed mathematical or source guard, all 9/9 rejected:
1-2 original M13 native one-byte tamper checked separately by both scripts;
3 parent ROT032 source IV80 JSON one-byte tamper;
4 original exact rational M15 ROT029 parent JSON one-byte tamper;
5 NEW source IV85 JSON one-byte tamper before the independent spatial program;
6 FALSE claim fourth k=(0,0,0) is mean-free;
7 FALSE source claim q<0.99;
8 FALSE 99% success with n=100;
9 FALSE exact cancellation of CUBIC a^3 tilt.
Thus quadratic color is specifically the claim ceiling; an unrestricted cubic/other per-mode calibration is NOT silently removed by these weights.

Complete user-conversation LOCAL self-contained original-source-and-executable ZIP:
IW_M15_ROT033_ORIGINAL_M13_QUADRATIC_SPECTRAL_CALIBRATION_FOUR_MEAN_FREE_MODES_IV85_REPRO_001_20261121.zip,
45,401 bytes, SHA256 de9a40e76b0a3c287893219ecdd55b9f9d0f40a090b6441da2a77dd1d9deac7a.
Archive 13 members: unchanged 8970B M13, two full SHA-locked independent prior source JSONs, NEW original-M13-source IV85 Python and complete actual JSON, NEW original 41^3 full spatial Python and complete actual JSON, actual cold replay+nine negatives Python and receipt JSON, complete full local scientific report, README, ZIP builder, SHA256 manifest. ZIP CRC PASS, ALL 12/12 SHA256 payload PASS, full 13/13 archived byte comparison PASS.

Native original IV85 executed script SHA256 af2b8fc8b734770d6f199f7dd1e7dc4aa2f2a9c6da6e3e85c411af8ffabf48ba.
Full actual primary IV85 JSON SHA256 dfbb9ac5bf50a6c772f6c4491d13c3d8d8cac504664f3dc3828ff86fafe86164.
New independent actual full 8x8 spatial original-site program SHA256 10425aae71649dec42579c4d3eda0e6ceb83c74ebcf03523374101ab77318f32.
Complete independent spatial JSON SHA256 f03fd7a02fb839cc336dacca11e8eea23e92eb83835d33012d8d0c4d8b0fc6d2.
Actual isolated cold replay/nine negative receipt SHA256 52b66bbb8fbd4115ee7708086c9e9c12d498562066973619b35502a7de6a4e8a.

Original full executable code is attached in USER-LOCAL ZIP, NOT falsely claimed public byte-identical GitHub mirroring through this report/curated JSON.

## Hard science boundary and handoff

All results are source-conditional mathematical Gaussian RAW spatial models on the ORIGINAL PUBLIC M13 AUXILIARY Fourier operator; the missing complete historical original dtc0a_runtime_v0_3_1.py remains unrecovered. The original M13 source has NO authenticated physical 68921-site raw energy sensor, no four Fourier cosine/sine pair hardware, no measured polynomial spectral calibration, no 13-25 million independent full-site Gaussian snapshots, no physical free gain/translation or actual NASH J3/K/TPE/GR/GW bridge. This is NOT global minimum four frequencies, NOT global alpha inversion, NOT a novel general statistical theorem and NOT physical NASH evidence.

M13 original source first and Geeky ROT034-038 original mathematical firstness fully protected. NEW M15 source result is internal nonblind I1-level, REC13/AUD3 different-cell acceptance not obtained, external blind I3 not obtained, KN15 native BW provider ingest receipt NOT verified. GitHub POST and Slack dispatch do not imply ACK, CANON or EXEC_SIGN. NO_TASK_CASCADE.

FINAL: ORIGINAL_M13_NATIVE_GIT_BLOB_EXECUTION_PASS / SELECTED_THREE_SOURCE_MODES_QUADRATIC_CALIBRATION_COMPOSITE_NO_GO_PASS / FOUR_ORIGINAL_M13_ENERGY_MEAN_FREE_FOURIER_MODES_PASS / EXACT_SYMBOLIC_QUADRATIC_NUISANCE_MOMENT_CANCELLATION_PASS / SOURCE_IV85_Q_STRICT_LT_0P995_PASS / FOUR_FINITE_N_CHI_SQUARED_SOURCE_GATES_PASS / INDEPENDENT_ORIGINAL_41_CUBED_8X8_SPATIAL_SOURCE_THREE_CALIBRATION_SCENARIOS_PASS / TWO_FULL_CLEAN_JSON_BYTE_IDENTICAL_PASS / NINE_REAL_NEGATIVE_FIXTURES_REJECTED / ZIP_CRC_SHA12OF12_PASS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE.
