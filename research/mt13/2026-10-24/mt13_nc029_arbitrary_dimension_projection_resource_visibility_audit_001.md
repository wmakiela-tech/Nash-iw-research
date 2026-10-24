# MT13: NC-OPN-002 in arbitrary finite dimension — compression, amplification, visibility and resource budget
**DATE:** 2026-10-24
**RETURN_ID:** MT13-NC029-ARBITRARY-DIMENSION-BAE-PROJECTION-RESOURCE-AUDIT-001_20261024
**CLASS:** EXACT CLASSICAL FINITE-DIMENSIONAL THEOREMS / CONSTRUCTIVE SOURCE-LOCAL REFEREE CORRECTION / SYNTHETIC NUMERIC PASS
**CEILING:** NO NOVELTY / NO CANON / NO EXEC / NO HARDWARE / NO PHYSICAL NASH J3-K / NO BW OR OWNER ACCEPTANCE IMPLIED

## 0. Others first and direct NC question
NC ART029 explicitly asked MT13 whether its strong-backaction rank-one 2D reduction extends to n>2 and whether a closed optimal time interval is possible. NC ART031 subsequently subtracted its own earlier ART018/NC-NUM-003/004 and NC-ALG-005 scope. We preserve NC's priority for its Gramian, μ₂ threshold, its 2D mechanism and the honest failure NC-FAL-022.
- NC ART029: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-24/IW_NC_OPN002_DYCHOTOMIA_MU2_I_BRAK_SKONCZONEGO_SUFITU_029_20261024.md
- NC ART031 prior-art self-audit: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-24/IW_NC_KOREKTA_ART029_ODEJMOWANIE_WOBEC_WLASNEGO_REJESTRU_031_20261024.md
- LT5 ROT19 source-target information radius with native working REV021 uptake: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-24/lt5_rev021_rot19_exact_admissible_class_scalar_radius_vanishing_gain_and_interval_upgrade_001.md

## 1. General positive threshold witness for EVERY n>=2
Let G be a REAL n×n generator, M=exp(G Delta), and μ₂(G)=λmax((G+G^T)/2). NC source impulse at u=exp(-γs) approaches P=I-dd^T as u->0, with normalized REAL readout e and backaction vector d.
If μ₂(G)>0, choose unit w maximizing w^T sym(G)w and sufficiently small Delta>0, so
  rho=w^T M w=1+μ₂(G)Delta+O(Delta²)>1.
Set r=Mw-rho*w. Then r^T w=0. If r nonzero, choose d=r/||r||; otherwise any unit d⊥w. This yields EXACT
  P M w=rho w, e=w and d⊥w.
For a fixed repeated readout-impulse-evolve protocol, the post-impulse states are rho^j*w and pre-impulse recorded responses are proportional to rho^j. Therefore geometric amplification exists in ALL dimensions n>=2 when e,d,Delta are FREE and the strong impulse is legal. For sufficiently small FIXED finite u>0, the unstable eigenvalue of M D_d(u) survives by continuity.
Independent Hurwitz nonnormal witnesses:
 n=3 G=[[-1,12,1],[0,-1,8],[0,0,-1]], Delta=.12: μ₂=6.447976355880428, rho=1.8284805958103003.
 n=4 G=[[-1,4,0,0],[0,-1,5,0],[0,0,-1,3],[0,0,0,-1]], Delta=.2: μ₂=2.4253361951588532, rho=1.5028145397507875.
Both exact projector eigenvector checks and finite u=e^-20 unstable eigenspectrum PASS.
For μ₂(G)<=0, NC source theorem gamma*sup||c||₂<=sqrt(m) holds in every dimension since each factor is a contraction. Thus the EXISTENCE/CONTRACTION dichotomy survives n>=2; this does NOT say prescribed readout directions or impulse timings always attain the bound.

## 2. Critical spectral nonmap: the n=2 real Rayleigh RATE does NOT survive n>=3
In n=2 strong P has rank1, and the only nonzero eigenvalue of PMP is w^T M w with w⊥d. In n>=3 rank(P)=n-1; a compression can have COMPLEX eigenvalues.
Exact n=3 at fixed Delta=1:
 Grot=[[-0.1,-pi/2,0],[pi/2,-0.1,0],[0,0,-1]], d=(0,0,1).
 M=diag(exp(-.1)*rotation(pi/2),exp(-1)).
 For every REAL unit w, w^T M w=exp(-1)*w3²<=0.36787944117144233.
 But the eigenvalues on d^perp are +/- i exp(-.1), with spectral radius 0.9048374180359596.
So ρ(PMP) > max_REAL_w(w^T M w), even though this counterexample is wholly CONTRACTING and does not itself amplify >1.
General safe spectral inequality: if PMP v=lambda v with lambda≠0, v∈ran(P), so lambda=v*Mv. Hence
 rho(PMP) <= w_complex(M):=max_complex_unit_z |z*Mz| <= ||M||₂.
The construction in §1 yields a positive Rayleigh LOWER witness for appropriate d; it does NOT prove the exact maximized n-dimensional spectral rate or a universal closed-form optimum.

## 3. Closed-form source-specific timing for NC's Jordan separator
For the actual NC triangular family G=[[-a,b],[0,-a]], a>0,b!=0,
 max_REAL_unit_w w^T exp(G Delta)w = exp(-a Delta)*(1+|b|Delta/2).
If |b|<=2a, maximum over Delta>=0 is 1 at zero. If |b|>2a, UNIQUE optimal Delta:
 Delta*=1/a-2/|b| ; R*=(|b|/(2a))*exp(-1+2a/|b|).
For NC G=[[-1,100],[0,-1]], Delta*=.98 and R*=50exp(-.98)=18.765554942569977.
Derivative proves both branches. This is a CLOSED FORM in the named 2D Jordan host, not an nD universal formula or maximum over nonperiodic schedules.

## 4. NC ART029 T1a requires a REFEREE-LOCAL PATCH
NC's upper lambda_max(W)<=m for μ₂<=0 is valid. Its further statement that an isometric oscillator ATTAINS the bound for arbitrary times is too broad.
Counterexample using NC's own gramian:
 G=[[0,-1],[1,0]] is skew-symmetric (isometry). e=(1,0), d=(0,1), impulse u=0, m=2 shots t1=0, t2=pi/2. L1=I, L2=M P with M 90-degree rotation, P=diag(1,0).
 w1=L1^T e=e; w2=L2^T e=P M^T e=0.
 So W=diag(1,0) and lambda_max(W)=1, STRICTLY below m=2.
For arbitrary 0<u<1 and identical strength at both shots, largest W eigen=(1-u)^2<2(1-u)^2. Any positive t1 simply orthogonally conjugates the gramian.
Thus isometry of exp(Gt) ALONE does not imply saturation for arbitrary timings: the successive readout vectors must also stay aligned. This is NOT a refutation of NC T1, only of a too-broad sufficiency assertion in T1a. Exact 2D counterexample requires independent NC/REC10 owner/referee acceptance.

## 5. Fixed total time gives a different resource bound
NC's geometric cycle construction with fixed Delta spends total experiment time T≈m Delta. If all m shots instead lie inside an a priori fixed [0,T], with μ+=max(μ₂(G),0), contractions ||D_d(u)||<=1 and semigroup ||exp(Gt)||<=exp(μ₂(G)t) give EXACT
 gamma sup_||v0||=1 ||c||₂ <= sqrt(m)*exp(μ+ T).
No geometric amplification IN m for fixed T; nevertheless sqrt(m) remains legal. Verified in 300 random 3D/4D source-typed tests. Claims of experimental advantage must state T,m, impulse strength and noise/resource law.

## 6. Material NC -> LT5 science bridge: max amplification does NOT imply state identification
Set Ghidden=diag([[-1,100],[0,-1]],-2) (3D), Delta=.98, e=(1,1,0)/sqrt2, d=(1,-1,0)/sqrt2, u=0. Then
 rho=50 exp(-.98)=18.76555494257,
 W_m = [sum_{j=0}^{m-1}rho^(2j)] e e^T.
Hence rank W_m=ONE for ALL m despite geometric λmax growth; at m=6 λmax(W)=5.430616746829e12. The two allowed initial states v0=+e3 and -e3 give IDENTICAL ZERO m-shot histories, but the target T(v0)=v0_3 differs by 2. In the unit-ball initial state class the noiseless scalar minimax reconstruction radius is EXACTLY 1, by matching lower indistinguishable pair and upper constant-zero estimator. NC largest gain σmax and LT5 target information radius are DIFFERENT contracts; amplification does not identify an unobserved direction. This is classical observability / optimal recovery, not a quantum hardware claim.

## 7. Repro/custody and authorized route
Independent locally executed NumPy/SciPy:
 exact 3D/4D P M w=rho*w and eight-cycle records;
 finite u=e^-20 survival; 3D complex eigen nonmap;
 NC 2D 51/e baseline and optimization at Delta=.98;
 local T1a exact isometry counterexample;
 300 random fixed-time-horizon gramian checks; rank1 huge-gain vs scalar hidden-target ambiguity.
Clean ZIP extract, CRC, SHA manifest and standalone rerun regenerate the frozen JSON BYTE IDENTICAL.
Moderator download ZIP SHA256 2bc9326fcdbe5819eea3980c8d084fd86399f5ebf92701b2dadf709ef43cecf9; standalone complete POLISH report and script included. Separate NC/REC10 science receipt and LT5 authorial uptake remain PROPOSED, NOT ACCEPTED. No new task cascade. No source physical sensor or novel theory claim.
