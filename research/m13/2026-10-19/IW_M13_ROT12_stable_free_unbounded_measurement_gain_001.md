# IW / M13 — ROT12: Nieograniczony zysk pomiarowy mimo asymptotycznie stabilnego generatora swobodnego
RETURN_ID: M13-ROT12-NC011-STABLE-FREE-DYNAMICS-PERIODIC-MEASUREMENT-UNBOUNDED-GAIN-001_20261019
CELL: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13
DATE: 2026-10-19
CLASS: EXACT ABSTRACT CLASSICAL IMPULSIVE/SWITCHED LINEAR SYSTEMS; NO CLAIM TO NOVELTY.
AUTHORITY: [▷] EXPLORATORY, NOT CANON / EXEC_SIGN / SOURCE-NATIVE PHYSICS.


## Context and precise result
M13 ROT11 proved NC-011's conjectured equivalence for the specific UNIVERSAL UNIT measurement ceiling: for aligned readout/backaction and all unit preparations, directions, and protocols, gamma||c||_2<=1 holds iff mu_2(G)<=0. When mu_2(G)>0, some protocol violates 1/gamma, but this fact alone does NOT imply all finite ceilings fail. NC-011 already knew via counterexamples that sup_t||exp(Gt)|| was not an exact general replacement. ROT12 provides an exact real Hurwitz matrix for which sup_t||exp(Gt)|| is finite but the supremum over arbitrarily long repeated-measurement protocols is INFINITE, in both l2 and linfinity gain. The result is elementary host mathematics, no novelty or physical quantum backaction.


## Measurement contract
v in R^n; unit initial v0, freely evolving v'=Gv between measurements. Fixed unit direction e=d, gamma>0, strength s>0; a=exp(-gamma*s) in (0,1); measurement map M_a=I-(1-a)ee^T. Measurement j reads c_j=(1-a)(e^T w_j)/gamma from its pre-measurement state w_j and leaves M_a w_j. Equal gap h>0 yields one-cycle B_a(h)=M_a exp(Gh), with w_j=exp(Gh)B_a(h)^(j-1)v0. Direction e, strength s, gap h are all FIXED; only k (and horizon T=kh) grow.


## Exact 2x2 example
G=[[-1,4],[0,-1]], eigenvalues -1 and -1 (Hurwitz), mu_2(G)=1.
exp(Gt)=exp(-t)*[[1,4t],[0,1]], hence its free semigroup is bounded and tends to 0.
Take u=(1,1)/sqrt(2), e=d=(1,-1)/sqrt(2), and orthogonal Q=(u,e).
H=Q^T G Q=[[1,-2],[2,-3]].
Choose h=1/4 and a=1/2, equivalently gamma*s=ln 2.
E=exp(Hh)=exp(-1/4)*[[3/2,-1/2],[1/2,1/2]].
B=diag(1,1/2) E=exp(-1/4)*[[3/2,-1/2],[1/4,1/4]].
Eigenvalues lambda_plus/minus=exp(-1/4)*(7 +/- sqrt(17))/8.
lambda_plus=1.082835421427118... > 1.
Let r=(5-sqrt(17))/4 and v0=(u+r e)/sqrt(1+r^2), exact eigenvector of B for lambda_plus.
Exact first coefficient gamma*c_1=C=exp(-1/4)*(1+r)/(4 sqrt(1+r^2))=0.231876578747721...
Then gamma*c_j=C*lambda_plus^(j-1), so for finite k:
gamma||c_1:k||_infinity=C*lambda_plus^(k-1);
gamma||c_1:k||_2=C*sqrt((lambda_plus^(2k)-1)/(lambda_plus^2-1)).
Both diverge as k grows. At k=10: 0.4745904213 and 1.1041166518; k=30: 2.331138332 and 6.051386056; k=100: 612.2655385 and 1596.1243482 (linfinity and l2 respectively).
This is an unstable discrete CYCLE formed by individually contractive measurements and a decaying but non-normal free semigroup. No unstable eigenvalue of free G, no quantum claim.


## Elementary general sufficient class in R^2
Theorem: For EVERY real 2x2 Hurwitz G with mu_2(G)>0, there EXISTS one fixed aligned direction e, one fixed 0<a<1, positive spacing h, and unit preparation v0 such that measurement gains diverge in both linfinity and l2 as k->infinity, T=kh->infinity.
Proof: Let u be unit top-eigenvector of S=(G+G^T)/2; q=u^T G u=mu_2(G)>0. Choose orthogonal unit e, yielding G_basis=[[q,b],[c,d]]. Necessarily c!=0; if c=0, Gu=q u with q>0 contradicts Hurwitz. Fix any a∈(0,1). B_a(h)=diag(1,a)exp(G_basis h). At h=0 eigenvalue 1 is simple, eigenvectors u; analytic perturbation gives lambda'(0)=q>0. Thus lambda(h)>1 for sufficiently small h>0. Its normalized eigenvector v(h)=u+[a c/(1-a)] h e+O(h^2). The premeasurement coefficient e^T exp(Gh)v(h)=c h/(1-a)+O(h^2) is nonzero. Repeated readouts then grow as lambda(h)^(j-1). QED.
Do NOT generalize to all n, non-Hurwitz, capped total time, source-native or quantum instruments without separate argument.


## Finite-horizon quantitative guard
Let mu_plus=max(mu_2(G),0), and all observations lie within a FINITE horizon T. For each aligned measurement, the squared amplitude loss D_j=||w_j||²-||M_a w_j||²=(1-a_j²)(e_j^T w_j)² >=0.
Exact ledger: (gamma*c_j)²=D_j*(1-a_j)/(1+a_j)=D_j*tanh(gamma*s_j/2)<=D_j.
On each free interval derivative of ||v||²<=2mu_plus||v||²; measurement steps are contractions.
Summing free positive increments and measurement losses yields ΣD_j<=exp(2mu_plus T)||v0||².
Hence gamma||c_1:k||_2 <= exp(mu_plus T) for all k while T is fixed. No contradiction with k->infinity and T=kh->infinity in the witness.


## Distinguish statuses
EXACT MATHEMATICAL WITNESS: yes.
RUNTIME check: SymPy eigenpair + closed form for k=1,5,10,30,100 PASS.
SOURCE VALIDATED PHYSICAL MEASUREMENT/QUANTUM BACKACTION: no.
GENERAL SHARP CAP IN R^n: open, NOT inferred.
CLAIM TO MATHEMATICAL NOVELTY: no. Standard switched/impulsive stability mechanism.
ORIGINAL REPORT LOCAL: /mnt/data/IW_M13_ROT12_HURWITZ_MEASUREMENT_INDUCED_UNBOUNDED_GAIN_20261019.md
CHECK SCRIPT LOCAL: /mnt/data/m13_rot12/verify_rot12.py
LOCAL FULL MARKDOWN SHA256: 060b7a57c9b873198327c76437623c296a263a7893c1cce48365e0efa4832358


## Sources in project
NC-011: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-18/IW_NC_MEASUREMENT_CEILING_IS_THE_LOGARITHMIC_NORM_011_20261018.md
M13-ROT11: https://github.com/wmakiela-tech/Nash-iw-research/blob/f8edceb256a551f8bad59eacee24dae8a4ac5575/research/m13/2026-10-19/IW_M13_ROT11_NC_GPT_tura1_necessity_and_source_referee_001.md
REC9 NC-004 subtraction: https://github.com/wmakiela-tech/Nash-iw-research/blob/d4797f5d2bb75a1cd78dca1660133084373232fb/archive-index/2026/rec9/rec9_nc004_prior_art_subtraction_ab_classification_referee_20261019.md


ROUTE_TAGS: IWTO_NC IWTO_MT13 IWTO_LT4 IWTO_REC9 IWTO_REC10 IWTO_INT7 IWTO_MODERATOR.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_NEW_TASK / REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD.