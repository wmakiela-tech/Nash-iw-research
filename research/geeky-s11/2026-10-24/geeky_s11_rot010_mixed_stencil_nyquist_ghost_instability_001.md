---
artifact_id: GEEKY-S11-ROT010-MIXED-ORDER4-STENCIL-NYQUIST-TT-GHOST-INSTABILITY-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-24
problem_id: P3_DTC0A_STENCIL_PARITY_GHOST_TT_STRUCTURAL_STABILITY_001
exposure: PUBLIC_SAFE
status: EXACT_FOURIER_PROOF_PLUS_200_CASE_NUMPY_PASS / INDEPENDENT_REFEREE_PENDING
class: EXACT_TWO_WITNESS_ALL_ALPHA_SCHEME_PERTURBATION_NOGO
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: MATURE_FOURIER_TT / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT010 — order-four stencil admixture destroys exact full-checkerboard TT preservation

## Others-first, question, fixed carrier

S11 ROT007 obtained all-alpha two-witness nonclosure for the standard order-four centered stencil. ROT008 constructed an odd-offset-only order-four stencil with exact checkerboard preservation; ROT009 established its full six-dimensional preserving kernel K6 for all alpha. ROT010 asks an actually separate question: is the preserving ghost action **stable under arbitrarily small perturbation inside the same order-four accuracy class**? INT8 filter invariance, PRF11 raw-k collocation, M13 historic pure-trace/mask, XH-S4 metric York remain separately owned. This result is a source-typed *mathematical* test, not recovered historical runtime or a novelty claim.

On an even N³ periodic grid with N divisible by 8, h=2pi/N, define two order-four real centered first derivatives by their dimensionless Fourier symbols:

O(theta)=sin(theta)*(1+sin(theta)^2/6) [odd offsets ±1,±3],
S(theta)=(4/3)*sin(theta)-(1/6)*sin(2theta) [standard offsets ±1,±2].

The mixture is d_lambda(theta)=((1-lambda)*O(theta)+lambda*S(theta))/h for 0<=lambda<=1. Both endpoints and EVERY mixture are fourth-order consistent: truncation error -(9-5lambda)*h^4*f^(5)/120.

P_lambda is the orthogonal symmetric rank-2 TT projector matched to the vector Fourier symbol delta=(d_lambda(kx*h),d_lambda(ky*h),d_lambda(kz*h)); pi=I-delta*delta^T/|delta|², P(F)=pi F pi-(pi/2)tr(pi F), and P=0 at zero-symbol corners. Q=I-P. The scalar source-style filter stays E_alpha=I+alpha*h²*Delta_2; alpha arbitrary real. Lie_C^(lambda) F=C^m D_m^(lambda)F+F_mj D_i^(lambda)C^m+F_im D_j^(lambda)C^m. We do NOT use the archived even-N raw-wavevector production P_TT.

The generator C_N(j)=(-1)^(jx+jy+jz) e_x is nonconstant and depends on N. Every derivative in this class annihilates it. Its Lie action is therefore multiplication by the full checkerboard times D_x^(lambda).

## Exact zero at lambda=0

O(theta+pi)=-O(theta) for all theta. Thus the full checkerboard shift maps delta_0(k) -> -delta_0(k), keeps P_0 unchanged, and commutes with all TT tests. Since D, E and P are diagonal Fourier multipliers, Q_0 Lie_C^(0) E_alpha P_0=0 for ALL real alpha. This uses a fixed *matched-symbol* mathematical projector, not a coordinate-covariant physical field.

## Two exact genuine TT witnesses for lambda>0

Use k_A=(N/8,N/4,0), k_B=(N/8,3N/8,0). Their dimensionless input symbol directions are d_A=(p,y_A), d_B=(p,y_B), with p=u_lambda(pi/4), y_A=u_lambda(pi/2), y_B=u_lambda(3pi/4), and u_lambda=(1-lambda)O+lambda S. Let v_j=(-y_j,p,0)/sqrt(p²+y_j²), w=e_z and T_j=v_j v_j^T-w w^T. Set H_j=T_j cos(k_j*x); both are EXACT P_lambda-TT and have normalized Frobenius L2 norm 1.

The full checkerboard shifts wavevectors by Nyquist in every coordinate. Write p'=u_lambda(5pi/4) and y'_j=u_lambda(ty_j+pi). Define angular sine

s_j=abs(p*y'_j-y_j*p')/[sqrt(p²+y_j²)*sqrt(p'²+y'_j²)].

The exact fraction of T_j output rejected by the shifted TT projection is rho_j=s_j*sqrt(4-s_j²)/2 (rank-two TT principal-angle identity). Crucially the determinants are EXACT:

abs(p*y'_A-y_A*p')=lambda*y_A/3>0,
abs(p*y'_B-y_B*p')=lambda*(p+y_B)/3>0,

for every lambda∈(0,1]. Consequently rho_A,rho_B>0; no accidental angular cancellation is possible. Define A(lambda)=p*rho_A/(2pi), B(lambda)=p*rho_B/(2pi). E_alpha acts on these modes by 1-(4-sqrt2)*alpha and 1-4*alpha respectively. Therefore

||Q_lambda Lie_C^(lambda) E_alpha P_lambda H_A||/||H_A|| = N*A(lambda)*abs(1-(4-sqrt2)*alpha),
||Q_lambda Lie_C^(lambda) E_alpha P_lambda H_B||/||H_B|| = N*B(lambda)*abs(1-4*alpha).

These are exact real finite-grid equalities, not asymptotic data fits. The alpha roots differ. Let a=4-sqrt2,b=4. The sharp minimax over alpha of the two witnesses is attained at alpha_star=(A+B)/(a*A+b*B), with value

m(lambda)=A*B*(b-a)/(a*A+b*B)=sqrt2*A*B/((4-sqrt2)*A+4*B)>0.

Hence for EVERY real alpha, including alpha_N depending on grid size and lambda,

||Q_lambda Lie_C^(lambda) E_alpha P_lambda||_(L2->L2) >= N*m(lambda)>0  (0<lambda<=1; 8 divides N).

"Sharp" describes only this TWO-WITNESS minimax, NEVER the complete operator norm.

## Exact small-admixture slope

At lambda=0, p0=13sqrt2/24, y_A0=7/6 and y_B0=p0. Direct Taylor expansions give

A(lambda)=[91sqrt2/(1683pi)]*lambda+O(lambda²),
B(lambda)=[1/(6pi)]*lambda+O(lambda²),
m(lambda)=[91/(12pi*(91sqrt2+235))]*lambda+O(lambda²)
        =0.006637045773719633*lambda+O(lambda²).

Selected m(lambda) (nonsharp full-operator lower coefficient divided by N):
lambda=.001: 0.000006635780707;
lambda=.01: 0.0000662440268918;
lambda=.1: 0.000651142124638;
lambda=.5: 0.00301543223419;
lambda=1: 0.00548944011456.

Thus exact preservation at lambda=0 is structurally fragile even within fourth-order schemes: ANY positive admixture suffices. This does not prove that the standard scheme is physically worse, only different.

## Independent executed reproducer and custody

Full, standalone local NumPy reproducer implements real-space odd4/std4 mixed D, original scalar second-order E, full source-style tensor Lie with both derivative-of-C terms, FFT P_lambda rebuilt per lambda, and two genuine TT polarization carriers.

200 full real-grid FFT tests: N=8,16,24,32; lambda=0,.01,.1,.5,1; alpha=0,.05,1/(4-sqrt2),1/4,alpha_star(lambda); carrier=A,B. All 200 PASS. Max exact analytic/direct FFT ratio discrepancy 1.0382599834526928e-14; max TT-input projection mismatch 2.869944777217271e-15; max generator centered derivative 0 exactly. Alpha at either individual root kills one witness but NOT the other. Local complete executed report, code, JSON and SHA256 manifest were clean-unzipped, independently re-executed and results JSON byte matched.

SHA256:
report 8b7ce96dda9e82cca87dd38320b585e741fdd6e4a4ca0eaaacb0a687f68756e1
code fe39b9c3f7ff2924f9ffb42045df02863b39794a6a79301155f4f61d42d5e3f2
JSON 4e3a38d31a549b6975306fbab6ff02b11b4bf10573ab6d9c9a454f6687d77b35
ZIP 363233910d845ca8d5c9a52d99243ca27f7c555d9ef9a552e1a0c7f4c3f69ac5

The standalone executed code/JSON is saved in the current conversation local ZIP and is NOT implicitly claimed uploaded to GitHub by this report; GitHub code custody requires separate successful write+readback. Prior production dtc0a_runtime v0.3.1 byte exact remains unavailable.

## Guard / decision

N varies and the checkerboard vector itself varies at grid frequency; it is **not a single fixed-smooth continuum vector field**. Full-grid matched-symbol TT operator leakage does NOT become physical gauge noninvariance, a NASH K/J3 invariant, historical puretrace K_A, gravity, GW, BBN, PBH or other physical endpoint. No theorem novelty or scientific canon claimed. STOP extrapolating K6 discrete Nyquist preserving behavior from one stencil to all order-four derivatives. Independent referee, scientific owner uptake, BW integration and Moderator EXEC PENDING. NO_NEW_TASK.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / REFEREE_PENDING / BW_PENDING.
