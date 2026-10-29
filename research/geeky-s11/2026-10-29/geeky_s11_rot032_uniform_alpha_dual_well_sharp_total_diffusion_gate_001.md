---
artifact_id: GEEKY-S11-ROT032-UNIFORM-DUAL-WELL-TOTAL-DIFFUSION-STRENGTH-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-29
problem_id: P3_DTC0A_SOURCE_E_TT_UNIFORM_ALPHA_N_PARABOLIC_GATE_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
class: EXACT_STABLE_ALPHA_UNIFORM_TWO_WELL_L2_GATE_AND_FIXED_GENERATOR_NECESSITY_FALSIFIER
status: PROOF_PLUS_9948_EXECUTED_CHECKS_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# ROT032: uniform two-well smoothing in alpha and sharp total diffusion strength

## Prior art and exact source host

ROT015-017 FIRST established the even-grid non-idempotence of the realcast auxiliary raw-k TT operator and constructed real compatible orthoprojector B=GA. ROT027 first defined the exact average U_m of m+1 Lie-placement positions; ROT029 first evaluated it by polynomial divided differences; ROT030 first supplied a H1->L2 generator truncation certificate; ROT031 FIRST supplied a fixed positive alpha L2->L2 smoothing certificate, a special gamma branch at alpha=1/6, singular TT fibre blocks and a vanishing-alpha counterexample. ROT032 ONLY removes the spurious alpha->1/6- singularity of the previous bound and proves an all-alpha_N sharp diffusion-budget gate. Mature Fourier heat smoothing and Young/Daleckii-Krein mathematics; NO novelty/priority claim. Other owners M14 historical masked h=fI K_A, INT8 geometric TT, PRF12 process memory separate.

Original helper is retained UNCHANGED deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801, NOT historical unavailable production dtc0a_runtime_v0_3_1.py. Full unmasked even N³ periodic real symmetric tensors, h=2pi/N, strict orthogonal real raw TT B=GA (NOT source realcast A), source three-term centered tensor Lie L_C, source E_alpha=I+alpha h²Delta2 with symbol e_alpha(k)=1-4alpha S_N(k), S_N(k)=sum sin²(pi k_j/N), stable 0<=alpha<=1/6. U_(N,m,alpha)(C)=(m+1)^-1 sum_(ell=0)^m E^(m-ell) B L_C B E^ell.

## New R32.1: ONE spectral double-well inequality for ALL legal alpha

Define k in signed FFT cube [-N/2,N/2)^3 and r_N(k)=min(|k|, sqrt(sum_j(N/2-|k_j|)^2)), toroidal distance to zero or the triple-Nyquist corner. Then for ALL even N, ALL alpha in [0,1/6], ALL k:
 |e_alpha(k)| <= exp[-16 alpha r_N(k)^2/N²];
 |d_N(k)|<=r_N(k);
 r_N(k+s)>=(r_N(k)-|s|)_+, with d_N(k)_j=sin(hk_j)/h.

Proof: for x in [0,2], |1-x|<=exp[-min(x,2-x)]. Set x=4alpha*S, S in [0,3]. Exact inequality min(4alpha*S,2-4alpha*S)>=4alpha min(S,3-S) holds because alpha<=1/6. The sine/cosine chord inequalities give min(S,3-S)>=4r_N(k)^2/N². Derivative zero at triple Nyquist supplies |d|<=r; torus distance is 1-Lipschitz. Therefore the uniform gamma is simply gamma(alpha)=16alpha, continuous up to critical alpha=1/6 where gamma=8/3. ROT031 gamma for alpha<1/6 had artificial collapse as alpha approaches 1/6 FROM BELOW. It was a weaker proof, NOT a physical instability.

## New R32.2: sufficient TOTAL diffusion gate for varying alpha_N and m_N

If alpha_N in [0,1/6], m_N is nonnegative integer and tau_N=alpha_N*m_N/N² >= beta0>0, then for any real generator C and Fourier truncation C_S to a conjugate-paired subset of its DISCRETE sampled Fourier modes with vector coefficients c_s:
 ||U_(N,m_N,alpha_N)(C)-U_(N,m_N,alpha_N)(C_S)||_(L2->L2)
 <= sum_(s outside S) ||c_s|| [3|s|+(32*Euler_e*beta0)^(-1/2)].

Proof: for each exact ROT029 finite-dimensional Fourier transition k->k+s, |u_m(e(k+s),e(k))| <= exp[-16 tau_N (r_N(k)-|s|)_+²]. The full source three-term Lie symbol satisfies ||M_s(k)|| <= ||c_s|| (|d_N(k)|+2|d_N(s)|) <= ||c_s||(r_N(k)+2|s|); B and Fourier shifts are contractions. Max_(t>=0) t*exp(-16 beta0 t²) = (32 e beta0)^-1/2. Sum the omitted modes. The bound remains uniform for alpha_N ->1/6 from below and even alpha_N->0 if m_N compensates; fixed alpha is NOT required. Filter eigenvalues may be negative.

For the ANALYTIC source test generator C=(0,f(x),0), f(x)=sum_(r>=1)2^-r cos(rx), retain all sampled |s_x|<=L with aliased nonzero constant. For L<N/2:
 ||U(C)-U(C_L)||_(L2->L2)
 <= [3L+6+(32e beta0)^-1/2]*2^-L.
At beta0=.02 the universal addend is .7581633246407918 independent of proximity to alpha=1/6.

## New R32.3: sharp necessity for a class of smooth generators (not for every C)

Fix one smooth C=(0,epsilon*cos x,0), epsilon>0 constant. Let H_N=T*cos(K_N*y), T=diag(1,0,-1)/sqrt2, and K_N=max(2,floor(N/[8sqrt(1+alpha_N*m_N)])). If tau_N->0, then K_N->infinity while K_N<=N/8, so all source and target frequencies are ordinary, far from defective mixed Nyquist. H_N is true source B-TT, and gradient-on-C terms vanish exactly (T e_y=0). Let
 rK=1-1/[2(K²+1)],
 qin=1-4alpha sin²(pi K/N), qout=qin-4alpha sin²(pi/N),
 u_m(a,b)=(m+1)^-1 sum_(ell=0)^m a^(m-ell)b^ell.
The FULL real normalized exact result is:
 ||U_m(C)H_N||_2/||H_N||_2
  =epsilon [sin(2pi K/N)/(2pi/N)] rK u_m(qout,qin) /sqrt2.

For tau_N<=1/64 and sufficiently large N, qout^m>=exp(-pi²/4), rK>=.9, sin(hK)/h>=(2sqrt2/pi)K, K>=N/[16sqrt(1+alpha*m)]. Thus an explicit TRUE lower bound is
 ||U_m(C)||_(L2->L2) >= .0030368543776987202 * epsilon * N/sqrt(1+alpha*m),
which diverges whenever tau_N->0. For any sequence with liminf_(N->infinity) tau_N=0, choose a subsequence with N->infinity and tau_N->0; no UNIFORM asymptotic all-N bound over the source generator class is possible. This is NOT a counterexample using a fixed smooth input H or a statement that every C is unstable (C=0 is trivially stable). It is a sharp BUDGET gate for general uniform smooth-generator certification, not physical NCDG.

## Executed provenance and retention

Four independent standalone scripts:
1. 260 full 3D symbol checks through N64 including alpha=1/6-1e-8 and alpha1/6, no endpoint discontinuity;
2. 2188 adaptive Fourier TT witness and independent matrix projection checks through N8192;
3. 132 LITERAL unchanged helper real 3D source apply_E, apply_P_TT and full three-term lie_derivative_tensor, explicit U_m sum N8/12/16, max absolute discrepancy 1.66533453694e-16;
4. 7368 Python stdlib Fraction-only exact algebraic alpha/S and TT projector certificates, no false exact trigonometry.
TOTAL 9948/9948 TYPED ASSERTIONS PASS, NOT real physical datasets. Standalone LOCAL Moderator-conversation archive GEEKY_S11_ROT032_UNIFORM_ALPHA_DUAL_WELL_SHARP_DIFFUSION_GATE_REPRO_001.zip includes full 11KB Polish report, four standalone runnable scripts, four original JSON, four stdout logs, unchanged helper, README and SHA manifest. ZIP SHA256 1004babd90d8ebfc86ab536a10087a4c28e71cec0c3afdf435e6cbb6bf405ab3. CLEAN ZIP CRC PASS; all payload SHA256 15/15; delete all four JSON and rerun all four scripts in clean extraction produces four BYTE IDENTICAL JSON PASS. Source code/ZIP local, NOT claimed separately published on GitHub.

Limits: no original historical production runner, masked h=fI K_A, NASH K/J3, physical GR/GW/PBH, mathematical novelty, independent referee, BW, adoption or EXEC. NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
