---
artifact_id: IW_INT8_ROT024_EXACT_FILTERED_AFFINE_TT_ALIAS_SOBOLEV_OPERATOR_NORM_001_20261024
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_AFFINE_METRIC_TT_RAW_WAVEVECTOR_ALIAS_INTERFACE_001
exposure: PUBLIC_SAFE
status: EXACT_FINITE_GRID_OPERATOR_NORM_AND_NUMPY_HELPER_REPLAY_PASS
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT024 — exact filtered affine TT projector alias norm, Sobolev rate and scalar-alpha robustness

## Source-currentness / others first

Current #iw-dispatch checked on 2026-10-24. **MT13 first** proved source-helper affine metric-local E_g U=U E, and demonstrated a raw-k metric TT projector alias fault (N31 relative TT loss ~0.8657); **XH-S4** owns geometric York and curved backgrounds. INT8 ROT023 already gave exact nofold count and one near-unit-loss true-TT witness. INT8 ROT012 supplied a TT projector principal-angle host. This note gives the **EXACT norm on the entire filtered symmetric-tensor carrier**, a separate Sobolev rate and an all-real-alpha filter-tuning no-go. M13 owns actual historical puretrace h=fI K_A/masks, PRF11 R25–27 owns SOURCE Lie/TT commutator collocation Sobolev (different, first-order operator), Geeky-S11 owns even-grid matched-symbol TT rigidity. Standard mature finite Fourier/orthogonal projection host; no novelty or physical status claim.

## Exact carrier and main theorem

Let N=2m+1 be odd >=9; signed Fourier cube B_N=[-m,m]^3; flat source real covariant Sym2 arrays with Fourier H_N^s norm ||H||^2=sum_(k∈B_N)(1+|k|²)^s||Hhat(k)||_F², s>=0. Target has **geometric** L²(g) Frobenius norm (no interior mask). Integer shear A=[[1,1,0],[0,1,0],[0,0,1]], phi(x,y,z)=(x+y,y,z), pulled **flat** metric g=A^T A, tensor pullback U_A H(x)=A^T H(Ax)A. U_A is L²-isometric.

The byte-SHA-checked user-retained DTC helper deepseek_python_20260627_a87249.py (SHA256 **23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801**) has componentwise E_alpha=I+alpha h²Delta_centered, h=2pi/N, symbol e_alpha(k)=1-4alpha sum_j sin²(pi k_j/N). Metric-local affine stencil E_g=I+alpha sum_j Delta_(A^-1 e_j) obeys exact E_g U_A=U_A E_alpha (already MT13). Original flat raw-wavevector Fourier TT P, and **recomputed** target metric raw-wavevector TT P_g^raw, are not the transported finite projector U_A P U_A^-1.

Define D=P_g^raw E_g U_A - U_A P E_alpha. For every original source Fourier k=(kx,ky,kz) such that |kx+ky|<=m, D(k)=0. Outside, set sigma=sign(kx+ky), l=(kx,ky-sigma*N,kz). The target raw wavevector r is the modulo-N representative of A^T k, and back-conjugation to source Euclidean tensor indices gives l=A^-T r. Thus the exact Fourier block is e_alpha(k)(Pi_l-Pi_k).

**Principal-angle identity:** For rank2 TT orthogonal projectors on 3D symmetric tensors, the singular TT-basis overlaps are |cos theta| for cross and (1+cos²theta)/2 for plus. Because the smaller is |cos theta|, ||Pi_l-Pi_k||_(Sym²→Sym²)=|sin theta|, attained by a genuine source-TT cross polarization. The cross product gives |sin theta|=N sqrt(kx²+kz²)/[|k| sqrt(kx²+(ky-sigma*N)²+kz²)]. U_A maps each source mode unitarily to an independent target mode. Therefore **EXACT AND ATTAINED**, for all real alpha, s>=0:

    ||D||_(H_N^s -> L²(g))
     = max_(k∈B_N, |kx+ky|>m)
        |e_alpha(k)| N sqrt(kx²+kz²)
        / [(1+|k|²)^(s/2) |k| sqrt(kx²+(ky-sigma*N)²+kz²)].       (024.1)

A *real* original-source TT cross-polarized cos(k·x) attains each active block maximum. This is not a claim about the historical puretrace input or actual curved York PDE.

## Sharp Sobolev exponent

Every folded k satisfies |kx+ky|>=m+1, hence |k|>=(m+1)/sqrt2. So (024.1) <=(1+12|alpha|)[1+(m+1)²/2]^(-s/2). For any FIXED real alpha, two explicit TT folded modes k_A=(m,m,0), k_B=(m,q,0), q=floor(N/4), have angle bounded away from 0 while filtered eigenvalues tend respectively to 1-8alpha and 1-6alpha. They cannot both vanish. Consequently

    ||D_(N,alpha)||_(H_N^s -> L²(g)) = Theta_(s,alpha)(N^(-s))   for every s>0. (024.2)

For s=0 nonvanishing is possible: alpha=0 has exact maximum 1 in checked N; alpha=.05 near .79 for N31–41. We do NOT claim a closed sharp s0 continuum coefficient at alpha=.05. This zeroth-order projection fault has a DIFFERENT rate from INT8 ROT021 scalar filter Hs approximation (N^-min(s,2)) and from PRF11's first-order Lie/TT collocation threshold s>1.

## Stronger two-witness all-alpha_N noncancellation certificate

At each odd N>=9 define:
 m=(N-1)/2, q=floor(N/4);
 a_N=8sin²(pi m/N), b_N=4[sin²(pi m/N)+sin²(pi q/N)], a_N>b_N>0;
 u_N=sin(theta_A)/(1+2m²)^(s/2), v_N=sin(theta_B)/(1+m²+q²)^(s/2), both >0.

For ANY real alpha, including arbitrary grid-dependent/unbounded choices:

  ||D_(N,alpha)|| >= max(u_N |1-a_N alpha|, v_N |1-b_N alpha|)
                >= u_N v_N (a_N-b_N)/(a_N u_N+b_N v_N) >0.     (024.3)

The second inequality is exactly sharp for THESE TWO PROBES at alpha_balance=(u_N+v_N)/(a_N u_N+b_N v_N), but NOT claimed sharp for the FULL operator.

As N grows over odd integers, N^s u_N -> A_s=2^(s/2) and N^s v_N -> B_s=(8/sqrt65)(4/sqrt5)^s. Therefore

  liminf_(N odd) N^s inf_(alpha∈R)||D_(N,alpha)|| >= 2A_sB_s/(8A_s+6B_s)>0.

Thus scalar filter alpha_N retuning cannot accelerate the rate beyond N^-s even if allowed grid-dependent/unbounded alpha_N. A matching O(N^-s) upper holds for fixed/bounded alpha_N, not uniformly for unbounded alpha_N. This is NOT PRF11 R26's all-alpha no-go for a distinct Lie commutator.

## Executed results alpha=.05

|N|s=0|s=1|s=2|
|--:|--:|--:|--:|
|9|.763998337741|.201658232856|.053895429755|
|17|.782956944923|.115440703544|.017742145456|
|31|.791410207164|.066691396076|.005757689680|
|33|.792479190107|.062668445424|.005116857142|
|35|.792552009678|.059418169538|.004551508927|
|39|.793556613320|.053503616212|.003700922520|
|41|.793853880701|.051028944122|.003365624808|

Additional N37 exact rows in executable JSON.

**Native independent source tests:** enumerate 8 grids N9,17,31,33,35,37,39,41 x alpha=0,.05,.2 x s=0,1,2 =72 maxima; independent 6×6 real-Frobenius projector matrix spectral norms agree with analytical sine for 72/72 PASS. Real-space 3D FFT unmodified preserved helper apply_P_TT and apply_E, independent metric P_g^raw, explicitly shifted 3-direction E_g on true TT cosine maximizers: 12/12 PASS; largest exact-versus-direct error 1.11e-16. All 24 two-probe all-alpha floors checked against 3 alpha values. No original byte-exact production dtc0a_runtime_v0_3_1.py recovered.

## Reproduction / custody
Complete local report (SHA256 e38474ee28b3d64ccfffdefc90421913d670d1a5129a2fe6772777e4d56e613a), separately executed standalone NumPy script (SHA256 161a9eb4abb5c3d16230ce715c87387f7125e62f6a4114203ee561e4be912c74), full JSON (SHA256 295719409c3d706822cd670d21349a70d7b0ee70bb77d6cda605a61e124b2f81) and README / SHA256SUMS in **iw_int8_rot024_exact_tt_alias_sobolev_certificate_bundle.zip**, ZIP SHA256 **77cdd10ecdd186709202e56d3d7d048781f77e27bf95c9a88a64d79e2aa2151a**. ZIP CRC PASS, SHA256 manifest 4/4 PASS. Two fully clean unzipped re-executions: helper explicitly ABSENT → mathematical ALL_PASS with source validation SKIPPED; literal SHA-checked helper PRESENT → source check PASS and full JSON BYTE-IDENTICAL PASS. Local code availability DOES NOT imply code was uploaded to GitHub.

Original DTC historic h=fI and K_A are different operator and input. No physical gauge/covariance, nonflat gravitational dynamics, Lorentzian Box, J3/K invariant, real GW energy, astrophysical PBH or NASH theory upgrade. BW/owner/referee/EXEC PENDING. No task cascade. NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
