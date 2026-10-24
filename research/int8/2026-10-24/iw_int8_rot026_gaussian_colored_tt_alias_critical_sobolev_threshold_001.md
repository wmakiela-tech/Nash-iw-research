---
artifact_id: IW_INT8_ROT026_COLORED_GAUSSIAN_TT_ALIAS_CRITICAL_SOBOLEV_THRESHOLD_001_20261024
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_AFFINE_METRIC_TT_RAW_WAVEVECTOR_ALIAS_INTERFACE_001
exposure: PUBLIC_SAFE
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
science_status: EXACT_GAUSSIAN_TRACE / SHARP_ASYMPTOTICS / NATIVE_HELPER_REPRO_PASS
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT026 — colored Gaussian Fourier input: sharp absolute TT alias threshold at s=3/2

## New to this lineage versus existing operator hosts

**INT8 ROT023** owns affine TT nofold spectrum and near-unit high-frequency witness, **ROT024** exact worst-case Sobolev norm Theta(N^-s), **ROT025** full 6x6 principal-angle singular spectrum, unweighted HS trace and *WHITE* synthetic Gaussian typical response. **MT13 FIRST** constructed metric-transported flat-affine local E_g and FIRST identified naive raw-k target P_g alias defect. **XH-S4** owns curved York; **PRF11** owns a DISTINCT first-order source Lie/TT commutator Sobolev question; **M13** owns actual historical DTC0a h=fI, K_A and masks; **Geeky-S11** owns matched-symbol even-grid TT issues. This adds only the EXACT spectral-class dependence of typical error to ROT025; mathematical host is mature Gaussian Fourier trace/integrability, NOT novelty nor NASH physical theory.

## Precisely fixed source, projectors and random input

N=2m+1 odd >=9, signed Fourier cube B_N=[-m,m]^3, symmetric REAL tensor arrays H with orthonormal 6-component Frobenius coordinates in **unitary discrete Fourier normalization**. Choose the centered isotropic Gaussian covariance

  Cov(Hhat(k))=w_s(k) I_6, w_s(k)=(1+|k|²)^(-s),  s>=0,

and Hhat(-k)=conj(Hhat(k)). This is an ARTIFICIAL **colored** Gaussian source prior (unit covariance per Fourier tensor coordinate at k=0), not actual DTC/NCDG data. The TT-projected random variant is P H, with source Fourier TT rank2 except k=0 rank5 tracefree (original retained helper convention). It is NOT an independently physically sampled TT distribution.

Shear phi(x,y,z)=(x+y,y,z), metric g=A^T A FLAT, geometric target Frobenius L2. Define D_N=P_g^raw E_g U_A-U_A P E_alpha, with source E_alpha=I+alpha sum_j(tau_ej+tau_-ej-2I) and affine-transported local E_g U_A=U_A E_alpha. The latter equality is MT13-owned, not original raw P naturality. Source helper deepseek_python_20260627_a87249.py SHA256 **23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801** literally checked and executed. Original historic production dtc0a_runtime_v0_3_1.py remains BYTE UNAVAILABLE. Numerical alpha=.05.

For folded source k (|kx+ky|>m) define sigma=sign(kx+ky), ell=(kx,ky−sigma N,kz), c=|k·ell|/(|k||ell|), e(k)=1−4alpha sum sin²(pi ki/N) and
  F(k)=e(k)²(7−6c²−c⁴)/2.
For nofold k set F(k)=0. This is exactly the ROT025 SIX-dimensional squared-HS trace per block; TT-restricted trace F/2.

## T026.1 EXACT FINITE-N GAUSSIAN TRACE IDENTITIES

Write Q_N,s=sum_(k∈B_N) w_s(k)F(k), S_N,s=sum_(k∈B_N)w_s(k).
Then EXACT:
 E||D_N H||²=Q_N,s, E||H||²=6 S_N,s;
 E||D_N P H||²=Q_N,s/2, E||P H||²=2 S_N,s+3.

Proof: Gaussian covariance trace identity, Fourier block orthogonality and ROT025 singular values. Signed ±k reality is correctly counted ONCE per lattice frequency; plus3 follows the rank5 k=0 source convention. Relative ensemble RMS =sqrt(Q/(6S)) and sqrt(Q/[2(2S+3)]) respectively. These are ratios of expectations of squared norms, NOT the mean of individual relative norms.

## T026.2 SHARP ABSOLUTE ERROR PHASE TRANSITION

For u∈C=[-1/2,1/2]^3 define folded Fset={|ux+uy|>1/2}, v=(ux,uy−sign(ux+uy),uz), c(u)=|u·v|/(|u||v|), e(u)=1−4alpha sum sin²(pi ui) and

  I_s(alpha)=integral_(Fset) |u|^(-2s)e(u)²(7−6c(u)²−c(u)^4)/2 d³u >0.

This is FINITE for every fixed s>=0 because Fset stays away from origin; strictly positive at alpha=.05 where e>=.4 on C. Standard dominated Riemann sum on folded frequencies yields the EXACT sharp ASYMPTOTIC equivalence:

  Q_N,s ~ I_s(alpha) N^(3−2s)   for EVERY fixed s>=0 and alpha=.05.

Therefore absolute full and TT Gaussian RMS aliases obey:
  0<=s<3/2: diverge Θ(N^(3/2−s));
  s=3/2: tend positive sqrt(I_3/2) (full) or sqrt(I_3/2/2) (TT);
  s>3/2: decay Θ(N^(3/2−s)).
The critical value s=3/2 is dimension/2. It does NOT contradict INT8 ROT024 unit-H^s operator norm Θ(N^-s); this prior's expected H^s source norm itself grows with N.

## T026.3 RELATIVE RMS: A DIFFERENT THREE-WAY PHASE DIAGRAM

If 0<=s<3/2, J_s=integral_C |u|^(-2s) du<infinity and S_N,s~J_s N^(3−2s):
 relative FULL ->sqrt(I_s/(6J_s))>0; TT ->sqrt(I_s/(4J_s))>0.

At s=3/2, S_N,s=4pi log N+O(1):
 relative FULL ~sqrt(I_3/2/(24pi log N));
 relative TT ~sqrt(I_3/2/(16pi log N)).
Thus relative RMS vanishes LOGARITHMICALLY even while ABSOLUTE alias RMS stays nonzero.

If s>3/2, Z_s=sum_(k∈Z³)(1+|k|²)^(-s)<infinity and S_N,s->Z_s:
 relative FULL ~sqrt(I_s/(6 Z_s)) N^(3/2−s);
 relative TT ~sqrt(I_s/[2(2Z_s+3)]) N^(3/2−s).
No unearned universal factor sqrt(3/2) for TT versus FULL with colored s>3/2: k0 rank5 +3 matters.

## T026.4 CONCENTRATION / TYPICAL INPUT QUANTIFIER

For the independent centered Gaussian on the REAL tensor Hilbert space, the quadratic form Y_N=||D_NH||² has
 Var(Y_N)=2 tr[(DΣD*)²] <=2||DΣD*||op tr(DΣD*).
Every folded k has |k|>=cN, e and projector bounded; hence ||DΣD*||op=O(N^-2s), but tr(DΣD*)~I_s N^(3−2s). Consequently
 Var(Y_N)/(E Y_N)²=O(N^-3), ALL fixed s>=0.
Therefore Y_N/N^(3−2s)->I_s in probability. At s=3/2, the ABSOLUTE RMS error of a typical sample ->sqrt(I_3/2), not zero.
For s>3/2, the same infinite Gaussian Fourier sequence can be coupled across grids and is almost surely square-summable; D_N kills |k|<cN and is uniformly L² bounded, giving ||D_N H_N||->0 almost surely. None of these is a physical stochastic measure asserted for NASH.

## Fully executed source-typed numbers (alpha=.05)

|N|relative full s1|absolute RMS full s1|relative full s1.5|absolute RMS full s1.5|relative full s2|absolute RMS full s2|
|--:|--:|--:|--:|--:|--:|--:|
|9|.171364371|3.022268|.133948606|1.388496|.094549958|.644445|
|17|.163501129|4.240044|.115492198|1.432423|.067474040|.489726|
|31|.158893070|5.758775|.102520094|1.445075|.049083072|.367166|
|41|.157455674|6.629882|.097657000|1.447440|.042408099|.320001|
|61|.155962818|8.093185|.091731588|1.449178|.034524856|.262792|
|101|.154728088|10.418227|.085511930|1.450091|.026668353|.204410|
|201|.153778237|14.699679|.078728339|1.450483|.018812873|.144954|
|401|.153295620|20.763540|.073311210|1.450582|.013285818|.102635|

Unit variance is a declared artificial normalization; limiting number ~1.4506 is NOT a physical universal constant.

NUMERIC: full 48 matrix-free Fourier sums for N9,17,31,41,61,101,201,401 and s=0,.5,1,1.5,2,3; source original SHA-checked helper apply_E+apply_P_TT and independent actual real full 3D FFT for N9,17,31 and s1/2 (6 cases) with max error 1.16e-16; independent explicit REAL Frobenius 6×6 TT projector matrix second-route 12 cases N7,9,11 times s=0,1,1.5,2 with max sum discrepancy 2.27e-13. All PASS. No historical KA or original production DTC run.

Full LOCAL reproducible scientific report, standalone Python, row-level JSON, execution log, README+SHA256 manifest packaged as:
 iw_int8_rot026_gaussian_alias_spectral_threshold_bundle.zip
 ZIP SHA256 **4d13d03765573c980b8c14ad79550b570eaa7f4066efd7cd0a868b8a4be65c96**.
Zipfile CRC PASS, SHA256 5/5 PASS, TWO independent clean-directory executions: no helper present math PASS and source SKIPPED; SHA-verified helper-present all PASS, JSON exactly byte-identical to original. Full code exists inside Moderator-local ZIP; GitHub publication of executable code is not claimed from THIS report.

No BW receipt, independent referee, scientific owner adoption or Moderator EXEC claimed. No physical J3/K, Lorentzian Box, nonflat gauge, GW energy, astrophysical signal or historical masked K_A inference. Mature prior-art mathematics, NO NOVELTY / NO CANON / NO EXEC / NO PHYSICAL UPGRADE / NO TASK CASCADE.
