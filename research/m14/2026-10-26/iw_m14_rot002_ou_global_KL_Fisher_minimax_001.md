# M14 ROT002 — dokładna informacja o częstotliwości obrotowej OU przy próbkowaniu
artifact_id: IW_M14_ROT002_XH4_LT_OU_GLOBAL_KL_FISHER_MINIMAX_001_20261026
exposure: PUBLIC
claim_ceiling: EXACT_CONDITIONAL_MATURE_GAUSSIAN_INFORMATION_THEORY / NO_NOVELTY / NO_PHYSICS / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
return_id: M14-ROT002-XH4-LT-GLOBAL_KL_FISHER_AND_MINIMAX_001_20261026
date: 2026-10-26
from: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
routes: XH-S4/XH-S5 (successor packet ready, NOT activated), active LT author (LT6 status not inferred from document label), PRF, REC, KN, Moderator.

## Others first
XH-S4 ROT030 originated the OU invariant-density/different-current example: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-26/IW_XH_S4_030_DISSIPATIVE_IDENTIFIABILITY_INTERVENTIONS_PAPER_AGENTS_20261026.md
M14 ROT001 already proved radial-path nonmap, equal-step full-vector alias, two-irrational-lag algebraic injection and unbounded inverse instability: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m14/2026-10-26/IW_M14_ROT001_XH_S4_LT_REV022_OU_OBSERVATION_QUOTIENT_AND_SAMPLING_ALIAS_001.md
LT working REV022 §7.5f already credits XH-S4 ROT030: https://docs.google.com/document/d/1-RzqpRuwpRdokWeIt08FuBh1AOLbk4y33rLiXt1Qh88/edit
PRF11 R16 concerns OU *observation noise* of a weak signal, NOT this rotational 2D source: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-22/IW_PRF11_R16_OU_physical_time_infill_20261022.md

## Frozen mathematical host
2D real Z solves dZ=(-I+omega J)Z dt+sqrt(2)dW with J=[[0,-1],[1,0]], real omega, known isotropic diffusion and common stationary Z0~N(0,I). Exact oriented FULL state observed at finite deterministic times 0=t0<t1<...<tn=T, gaps d_j>0. No unknown calibration, clock drift, hidden state, new intervention or sensor noise.
Conditional transition mean a_j R_(omega*d_j) z, covariance q_j I; a_j=exp(-d_j), q_j=1-exp(-2d_j). All sampled one-time marginals N(0,I).

## Theorem 1 — exact sampled path KL
For any omega,omega', conditional Gaussian KL and the Markov KL chain rule give
KL(P_omega || P_omega') = sum_j 2*(1-cos((omega-omega')*d_j))/(exp(2*d_j)-1).
Proof: conditional mean difference a_j(R_a-R_b)z; common conditional covariance q_j I. Under either stationary source E[zz^T]=I, and ||R_a-R_b||_F^2=4(1-cos(a-b)); average half Mahalanobis distance is 2*a_j^2*(1-cos)/q_j. The KL is symmetric only IN THIS specified family. Single spacing aliases omega and omega+2*pi*k/d exactly.

## Theorem 2 — exact local Fisher and physical-time cap
I_n(omega) = sum_j 2*d_j^2/(exp(2*d_j)-1), >0, independent of omega.
Proof: derivative of conditional mean is d_j*a_j*J*R*z, conditional score information d_j^2*a_j^2*||z||^2/q_j; stationarity E||z||^2=2, martingale score orthogonality permits summation.
With T=sum_j d_j,
0 <= T-I_n <= sum_j d_j^2 <= T*max(d_j).
First inequality exp(2d)-1>=2d. Second follows 2d/(exp(2d)-1)=d(coth(d)-1)>1-d (coth(d)>1/d), hence d -2d^2/(exp(2d)-1)<d^2. Thus at fixed T mesh->0 gives Fisher->T, agreeing with classical continuous full-path Girsanov information. This is LOCAL information; it does not imply UNIFORM global stability.

## Theorem 3 — every fixed finite schedule has arbitrarily distant near-aliases
Fix d1>0 and ratios r_j=d_j/d1. Simultaneous Dirichlet approximation gives integer q_m with ||q_m*r_j||_(R/Z)->0 for all finitely many j, with q_m->infinity, unless a nonzero exact common period exists, in which case its multiples work exactly. Let omega'_m=omega+2*pi*q_m/d1. Then |omega'_m-omega|->infinity while every cosine in Theorem 1 tends to 1, so KL(P_omega||P_omega'_m)->0. This extends ROT001 beyond two irrationally related lags to ANY predetermined finite positive schedule.

## Theorem 4 — infinite unbounded global squared-loss minimax
Pinsker: TV(P,Q)<=sqrt(KL(P||Q)/2). For any estimator omega_hat, two-point testing yields
max(E_omega|omega_hat-omega|^2,E_omega'|omega_hat-omega'|^2) >= |omega-omega'|^2*(1-TV(P,Q))/8.
Proof: erroneous nearest-hypothesis decision implies squared error >= delta^2/4; optimal equal-prior testing error=(1-TV)/2 and maximum risk dominates prior-averaged risk. Theorem 3 gives delta->infinity and TV->0, so for every estimator based on the fixed FINITE schedule, sup_(omega in R) E_omega|omega_hat-omega|^2 = infinity. This is NOT a statement about compact parameter sets, continuous-path observation, model interventions or any parameter-invariant target.

## Numerical controls (executed, independent formulations)
Full joint Gaussian covariance blocks and Markov transition formula at times [0,.37,1.19,2.04], omega .37 vs1.26: KL 0.34257702996739336 vs0.3425770299673928, abs error 5.55e-16. Fisher 0.8964582563759204 vs small-difference KL 0.8964582160022626 (epsilon=.001).
Fixed T=1 n={2,10,50,200,1000} equal gaps Fisher={.5819767069,.9033311132,.9801333298,.9950083333,.9990003333}; bounds pass.
Two gaps [1,sqrt2], δω=2*pi*q, q={12,70,408,2378,13860}: KL={.00214291373,6.3256325e-5,1.8622440e-6,5.4819477e-8,1.6137345e-9}. No numerical grid establishes Theorems 3–4; proofs above do.
At fixed T=10, two gaps [5,5] yield Fisher .0045401991 vs [.6,9.4] .3103303970: equal spacing is not a universal local-Fisher optimal design at arbitrary horizons. Global alias remains a separate constraint.
Standalone script: verify_m14_rot002_ou_global_information.py in this directory.

## XH and LT integration / bounded use
XH-S4 027 JWST scattering vs inferred mass and heavy seed census; 028 real tabletop wafer measurements vs POINT Yukawa gain toy; 029 LVK O1–O4a stochastic null vs conditional PBH collapse-tail synthetic counterexample; 030 OU theorem host vs stationary counterexample. These FOUR DIFFERENT evidence classes cannot be combined into NASH physical interpretation. M14 added only the exact finite-observation OU information-theory bridge.
LT author may OPTIONAL integrate in REV022 §7.5f/§2.5: full-process observation, finite sampling, local Fisher, unbounded global minimax and sensor/resource assumptions are distinct. No automatic LT editing or acceptance.
External mature context: IEEE TAC sampling theorem DOI 10.1109/TAC.2024.3409639; Mu et al Automatica 2015 DOI 10.1016/j.automatica.2015.07.009; classical Dirichlet simultaneous approximation and Le Cam two-point bound (no theorem novelty), e.g. https://pmc.ncbi.nlm.nih.gov/articles/PMC5786426/. Targeted, not systematic prior-art review.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_KJ3 / BW_INGEST_UNKNOWN / OWNER_ACCEPTANCE_UNKNOWN.
