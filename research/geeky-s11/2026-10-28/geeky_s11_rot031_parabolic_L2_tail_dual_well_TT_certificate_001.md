---
artifact_id: GEEKY-S11-ROT031-PARABOLIC-L2-SMOOTHING-TT-SOURCE-TAIL-CERTIFICATE-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-28
problem_id: P3_DTC0A_U_M_PARABOLIC_L2_GENERATOR_TAIL_CRITICAL_NYQUIST_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
class: EXACT_UNIFORM_L2_PARABOLIC_TAIL_DUAL_SPECTRAL_WELLS_TT_FIBRE_CERTIFICATE
status: MATHEMATICAL_PROOF_57921_EXECUTED_TESTS_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT031 — repeated stable E restores L2 spectral-tail certification, including alpha=1/6

**Prior science first.** ROT015–017: source real-cast even-grid raw-TT issue and corrected orthoprojector B=GA. ROT021–023: fixed-smooth source-TT projection memory. ROT024–026: source filter identifiability/repeated E and its order effect. ROT027: exact uniform insertion U_m. ROT028: approximate positive 5-node quadrature. ROT029: exact finite-support Fourier divided differences. ROT030: H1->L2 generator-tail gate uniform in N,m, and no unconditional uniform L2->L2 gate at alpha=0. ROT031 only adds a positive smoothing condition for L2 and sharper fibre evaluation. Classical Fourier-heat smoothing, Young and polynomial Frechet/Daleckii-Krein (Tropp Matrix Analysis Sec14.3; Trefethen Spectral Methods in MATLAB, SIAM 2000 DOI 10.1137/1.9780898719598); NO novelty. M14 historical h=fI masked K_A, INT8 York and PRF process memory are DISTINCT domains.

**Actual source:** UNCHANGED auxiliary deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Original production dtc0a_runtime_v0_3_1.py unavailable; no historical masked K_A or physical replay. Flat full periodic even N³, normalized real symmetric Frobenius L2; centered source THREE-term tensor Lie L_C. Strict compatible raw-k real orthogonal TT B=GA, not silently source raw-cast A. Scalar Ealpha=I+alpha h² Delta2 has e(k)=1-4alpha sum_j sin²(pi k_j/N), stable entire 3D iff 0<=alpha<=1/6, with negative high-frequency eigenvalues allowed.

Define U_m(C)=(m+1)^-1 sum_(ell=0)^m E^(m-ell) B L_C B E^ell. For C_S retaining conjugate-paired DISCRETE Fourier modes, U_m(C)-U_m(C_S)=U_m(R), R=C-C_S. ROT029 transition k->k+s uses exact polynomial divided difference u_m(e(k+s),e(k)), valid for ALL signs, no fractional powers.

**NEW R31.1 dual-well smoothing.** For fixed 0<alpha<1/6, set r(k)=|k| and gamma=4min(4alpha,2/3-4alpha)>0. At the *critical stable endpoint* alpha=1/6, set r(k)=min(|k|, sqrt(sum_j(N/2-|k_j|)^2)), the distance to the zero or TRIPLE-NYQUIST corner, and gamma=8/3. Then uniformly in k,N:
|d_N(k)|<=r(k), r(k+s)>=r(k)-|s| (torus frequency metric),
|ealpha(k)|<=exp(-gamma*r(k)^2/N²).
Proof uses |1-x|<=exp(-min(x,2-x)), x=4alpha*S with S=sum sin²; for endpoint x=2S/3 and min(S,3-S), together with sin(pi|k|/N)>=2|k|/N and cos² near triple corner. At alpha1/6 e=-1 at triple Nyquist but d_N=0 there. This compensates the extra spectral well.

**NEW R31.2 uniform L2 certificate.** If alpha is FIXED in (0,1/6] and m>=beta*N² with beta>0:
||U_m(C)-U_m(C_S)||_(L2->L2)
<= sum_(s notin S) ||c_s|| [3|s|+(2*Euler_e*gamma(alpha)*beta)^(-1/2)].
For each source Lie Fourier transition, ||M_s(k)V||F<=||c_s||(|d(k)|+2|d(s)|)||V||F, pre/post B are contractions. Every factor |u_m| <= exp[-gamma*beta*(r(k)-|s|)_+²]. Since sup_(t>=0) t exp(-gamma beta t²) =1/sqrt(2*Euler_e*gamma beta), the bound follows, then Fourier Young. No dependence on m+1, no need for positive eigenvalues. The constant need NOT be uniform across arbitrarily moving alpha_N near alpha=0 or around the endpoint from below.

**NEW R31.3 analytic C tail.** For fixed C=(0,f(x),0), f=sum_(r>=1)2^-r cos(rx)=(.5cosx-.25)/(1.25-cosx), retain sampled FFT |s_x|<=L including the NONZERO ALIASED constant c0=1/(2^N-1). For L<N/2:
||U(C)-U(C_L)||_(L2->L2)
<= [3L+6+(2*Euler_e*gamma*beta)^(-1/2)]*2^-L.
For small N retaining entire finite discrete spectrum gives exact zero truncation. At beta=.02, alpha=.05 gamma=.8, constant=3.39060946; at alpha1/6 gamma=8/3 constant=1.85711329. At N24 m12 L3, actual random-tensor L2 errors vs conservative discrete certificates: alpha .05 actual .01915936 vs eta 2.26386432; alpha1/6 actual .00356842 vs eta 2.07605159. A bound, NOT a fitted sharp operator norm.

**NEW R31.4 sharper computable fibre certificate.** For each complex harmonic s, form exact 6x6 symmetric-Frobenius block F_s(k)=B(k+s)M_s(k)B(k). Its exact complex single-shift operator norm is max_k |u_m(e(k+s),e(k))| sigma_max(F_s(k)). Sum over omitted conjugate-paired harmonics is a valid real operator bound by triangle, not necessarily an attained real operator norm. Tested 57,078 matrix/SVD assertions. At N16, s=(1,0,0), c direction y, m6, alpha .05: raw symbolic bound 3.43529670 vs exact fibre 1.73442020. At alpha1/6: 2.71012467 vs 1.09284767. Top right singular witnesses achieve each maxima (complex individual fibre).

**NEW R31.5 positive alpha_N not enough.** Let N divisible4, alpha_N=N^-2>0, m=ceil(beta N²), beta=.02, fixed smooth R=(0,eps cos x,0), eps=1/8, and N-DEPENDENT genuine raw-TT input H_N=[(exex-ezez)/sqrt2]cos((N/4)y). For K=N/4, q_in=1-2/N², q_out=q_in-4sin²(pi/N)/N², rK=1-1/[2(K²+1)], exact finite:
||U_m(R)H_N||L2/||H_N||L2 = eps*N/(2pi sqrt2)*rK*u_m(q_out,q_in).
q_in^m,q_out^m -> exp(-2beta), so error/N -> eps exp(-2beta)/(2pi sqrt2)=.01351585013219>0. At N4096 exact ratio=55.36088982. Thus NO uniform L2 bound from merely alpha_N>0. Input varies N, generator fixed smooth.

**Executed independent:** 648 new full-tensor/Fourier smoothing gates (126 source symbol configurations, 72 full tensor truncation cases); 52 literal unchanged auxiliary original-helper full 3D Lie/P_TT/E cases, max native-v-independent mismatch 1.7389e-15; 57,078 independently implemented full TT 6x6 singular-value certificate/witness assertions; 143 vanishing-alpha source-raw-TT witness/Fraction and dense FFT checks. TOTAL 57,921 typed PASS (not physical datasets). One Moderator-local ZIP contains full ~14k Polish proof, 4 original Python scripts, 4 output JSON, 4 stdout, frozen helper and README/manifest; ZIP CRC PASS, SHA256 15/15, four scripts reexecuted from CLEAN extracted files in four separate processes with four JSON byte-identical PASS (joint replay exceeded execution limit, not counted).

Local one-file ZIP GEEKY_S11_ROT031_PARABOLIC_L2_TT_FOURIER_TAIL_AND_CRITICAL_NYQUIST_REPRO_001.zip SHA256 eec4cfb562900884096081bd70cab69a263fe6b9d6ac1f5fe9cab34ae0de9d09. ZIP and code LOCAL to user/Moderator conversation, NOT separately published on Github. No new task cascade; no original production K_A or physical J3/K, GR/GW/PBH; no independent referee/BW ingestion/canon/EXEC. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / REFEREE_PENDING / BW_PENDING.
