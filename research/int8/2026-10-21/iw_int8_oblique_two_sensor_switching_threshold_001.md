# INT8 ROT005 — Exact two-action oblique reset switching threshold (2026-10-21)

STATUS: CONDITIONAL CLASSICAL MATHEMATICS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
FROM: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
SOURCE TYPES: co-aligned finite-horizon INT8 theorem; heterogeneous-action finite-storage Geeky-S10 theorem; REC10 misalignment counterexample. Not a quantum instrument or physical detector.

## Model
On R^2 set G=0. For a,b>0 use unit readout vectors e1=(1,0), e2=(0,1) and reset vectors d1=(1,-a), d2=(-b,1). Strength 0<s<1. Reading i outputs r_i=s e_i^T x and updates x <- Q_i(s)x, Q_i=I-s d_i e_i^T. Thus e_i^T d_i=1 and each reading attenuates its OWN sensed scalar by exactly 1-s.

Q1=[[1-s,0],[as,1]], Q2=[[1,bs],[0,1-s]].
For alternating actions 1 then 2,
B=Q2 Q1=[[1-s+ab*s*s,b*s],[a*s*(1-s),1-s]].
tr B=2*(1-s)+ab*s*s; det B=(1-s)^2; det(I-B)=(1-ab)*s*s.

## Exact trichotomy and proof
For 0<s<1:
* ab<1: B Schur stable by the three 2D Jury inequalities:
1-det B=s(2-s)>0;
1-tr B+det B=(1-ab)s^2>0;
1+tr B+det B=(2-s)^2+ab*s^2>0.
* ab=1: B has eigenvalues 1 and (1-s)^2. Starting at v=(1,a*(1-s)), Q1 v=(1-s,a), Q2 Q1 v=v; each pair records (s,a*s). Hence energy after k pairs is k*s^2*(1+a^2), unbounded as k grows.
* ab>1: det(I-B)<0 implies a real root lambda_+>1. Since B has strictly positive entries, a positive eigenvector produces nonzero records growing as lambda_+^k; energy diverges geometrically.

G=0: any finite number of shots can occur inside any fixed T>0, even with strictly positive gaps. Each individual reset has eigenvalues 1 and 1-s; this is NOT a claim of Euclidean contraction.

## Positive common-storage certificate for arbitrary switching when ab<1
Let P=[[a,ab],[ab,b]], alpha1=a*(1-ab), alpha2=b*(1-ab), alpha_min=(1-ab)*min(a,b)>0.
P is positive definite (det P=ab*(1-ab)>0), P*d_i=alpha_i*e_i. Thus for every shot
V(x)-V(Q_i(s)x)=alpha_i*s*(2-s)*(e_i^T x)^2;
r_i^2=[s/(alpha_i*(2-s))]*(V(x)-V(Q_i(s)x)), V=x^T P x.
Any finite arbitrary-switching sequence with 0<=s_j<=epsilon<1 satisfies
sum_j r_j^2 <= epsilon/((2-epsilon)*alpha_min) * (x0^T P x0).
The bound is count- and time-independent because G=0. When a=b=q in (0,1), alpha1=alpha2 and repeated alternating shots with strength epsilon drive x to zero, hence the stated bound is attained as the supremum over finite prefixes.

Thus the all-action-family storage is finite for ab<1; for ab>=1 the explicit alternating protocol forces its infinity on a nonzero state. Own-channel attenuation e_i^T d_i=1 alone does not imply the co-aligned finite-horizon ceiling.

## Checks
SymPy verified the above determinant, trace, P, and dissipation identities. At s=0.12, 120 pairs, taking an initial unit Perron eigenvector:
a=b=0.8 -> rho(B)=0.9747817969922528, output energy=0.31752249727575177, P bound=0.31821512418741627.
a=b=1.0 -> rho(B)=1, output energy=1.9477006311992793.
a=b=1.2 -> rho(B)=1.0258492733332545, output energy=144.7995606203949.
Numerics illustrate, not prove, the exact results.

## Scientific integration and negative knowledge
INT8 finite-T theorem requires readout-reset co-alignment. Geeky-S10 heterogeneous-action theorem requires common finite V_*; this example identifies precisely when such storage exists in this two-action family. REC10's single-action counterexample had e^T d=0; here each action attenuates its sensed channel but alternating them still diverges when ab>=1. M13's instability used nonnormal FREE dynamics with long horizon; here G=0 and any finite horizon suffices. No Fisher/PRF11 transfer without a legal noise model; PRF11 R14 notes correlated readout noise is a separate precision seam.

Prior-art hosts: G.W. Stewart, On the Numerical Analysis of Oblique Projectors, SIAM JMAA 32 (2011), DOI 10.1137/100792093; established switched-systems common-quadratic Lyapunov literature, DOI 10.1109/TAC.2003.811274. This is a specific worked example and conditional project integration, not a priority or novelty assertion.

NO_NEW_TASK / BW_INGESTION_UNKNOWN / OWNER_ACCEPTANCE_UNKNOWN / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
