# Geeky-S10 — NC GPT Turn-1 Mathematics and Attribution Audit

RETURN_ID: GEEKY-S10-NC-GPT-TURA1-MATH-ATTRIBUTION-AUDIT-001
DATE: 2026-10-19
STATUS: [▷] EXPLORATORY / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE
BW_INGESTION_STATUS: PENDING

Private Drive durable copy exists; private locator omitted from this public body.

## Blindness note

Task 1 was intended to be blind, but the retrieval response exposed NC Annex B together with the audit package before the derivation was fully closed. Agreement with Annex B is therefore not counted as blind corroboration. New proofs, counterexamples, quantifier repairs and differences below remain independent audit content.

## 1. Co-axial ceiling

Let d=e, P_e=e e^T, u=exp(-gamma s), and

Q_u=I-(1-u)P_e.

For pre-measurement state v and a=e^T v,

gamma c=(1-u)a,

while the feedback energy loss is

Delta=||v||^2-||Q_u v||^2=(1-u^2)a^2.

Hence exactly

(gamma c)^2
=
Delta (1-u)/(1+u)
=
Delta tanh(gamma s/2)
<=
Delta.

If

mu_2(G)=lambda_max((G+G^T)/2)<=0,

free evolution cannot increase Euclidean energy. Therefore for every finite protocol

gamma^2 sum_j c_j^2 <= 1,

so

||c||_2 <= 1/gamma.

The supremum is sharp.

## 2. Necessity: quantifier matters

### Universal over the sensor direction e

If the protocol designer may choose e, v0, waiting times and finite positive strengths, then a finite protocol-independent co-axial l2 ceiling exists **iff**

mu_2(G)<=0.

Proof of necessity: if mu_2(G)>0, choose unit x with

x^T (G+G^T)x/2 > 0.

For small tau, S=exp(G tau) satisfies

lambda=x^T Sx>1.

Write

Sx=lambda x+r,  r perp x.

If r!=0, choose e=r/||r||. In the projective-reset limit Q_0=I-ee^T,

Q_0 Sx=lambda x.

Repeated copies of the same free interval and reset produce geometric amplification. Any finite prefix is approximated arbitrarily closely by legal finite-strength resets u>0, so ||c||_2 has no finite bound.

If r=0, choose e=x and finite u with 1/lambda<u<1. One repeated cycle multiplies the amplitude by u lambda>1, again giving unbounded output energy.

Thus the universal-over-e theorem is exact:

FINITE CEILING iff mu_2(G)<=0,

with sharp finite supremum 1/gamma.

### Fixed apparatus direction e

Global mu_2(G)<=0 is not necessary.

Take

G=diag(a,-b), a,b>0,

with fixed e=e2. Then mu_2(G)=a>0, but the unstable first coordinate is invisible and uncoupled from the measured second coordinate. The measured component is contractive and still obeys

gamma^2 sum_j c_j^2 <= |v0,2|^2 <=1.

Firewall:

GLOBAL NUMERICAL ABSCISSA POSITIVE != FIXED-SENSOR OUTPUT-ENERGY UNBOUNDED AUTOMATICALLY.

## 3. Noncollinear readout and feedback

For sin(phi)!=0, already G=0 destroys any universal protocol-independent l2 ceiling.

Set

w=[e-(e·d)d]/|sin phi|.

Then w perp d, so every feedback step leaves w unchanged, while

e·w=|sin phi|.

Repeating any fixed finite strength s for k measurements gives

||c||_2
=
sqrt(k)|sin phi| sigma(s)
->
infinity.

Thus any nonzero line misalignment destroys the universal ceiling.

## 4. What replaces free transient gain

The free-flow norm sup_t||exp(Gt)|| is not sufficient because measurements reset the state.

For fixed e define reset-flow factors

A(tau,u)=Q_u^e exp(G tau).

The correct host is hybrid/switched output-energy geometry: products of reset-flow maps plus visibility of growing or persistent modes. Joint/generalized spectral-radius ideas describe asymptotic state growth, while a tight output ceiling also needs observability/dissipativity or storage-function control.

FREE SEMIGROUP TRANSIENT GAIN != RESET-FLOW OUTPUT-ENERGY CEILING.

## 5. Verification of NC witnesses

### C3 Blackwell/postselection witness

PASS EXACT.

The two density matrices have equal original measurement diagonal and equal survival probability 8/15, but different normalized postselection diagonals:

rho1: (17/48,11/48,20/48)
rho2: (29/48,11/48,8/48).

Therefore no stochastic garbling of the original fixed measurement can distinguish them, while postselected sector elimination can. Equal survival proves trace loss is not doing the separating work.

The stochastic scan is an implementation check, not the proof.

### l2 realization witness

PASS EXACT.

Matching products f_n c_n give equal Markov parameters; the meromorphic moment argument establishes approximate controllability/observability; the diagonal intertwiner is bounded, injective and dense-range but has unbounded inverse; simple spectrum makes it the unique bounded commuting intertwiner matching the input vector.

### Continuous-spectrum analogue

NC's suspicion that the mechanism might fail for continuous spectrum is false.

Take

H=L^2([0,1]),
D=M_x.

Use

(c1,f1)=(1,x),
(c2,f2)=(x,1).

For z outside [0,1], both transfer functions equal

integral_0^1 x/(z-x) dx.

Polynomial density gives approximate controllability and observability.

The intertwiner T=M_x satisfies

TD=DT,
Tc1=c2,
B2 T=B1.

T is bounded, injective and dense-range, but not bounded below. Unit vectors

h_n=sqrt(n) 1_[0,1/n]

satisfy

||T h_n||=1/(sqrt(3)n)->0.

If bounded S commutes with D and S1=x, polynomial density forces S=M_x. Hence no boundedly invertible similarity exists.

### Semigroup factorization witness

PASS EXACT WITH CONTINUITY-TYPE GUARD.

For

X=[0,2pi),
U_t(theta)=theta exp(-t),
r(theta)=exp(i theta),
V_t=r U_t r^(-1),

U is continuous and r is a continuous bijection but not a homeomorphism. For every t>0,

V_t(1)=1,

whereas theta->2pi- gives

V_t(exp(i theta))->exp(2pi i exp(-t)) !=1.

Spatial continuity fails; orbit continuity in t survives.

## 6. Literature attribution

### Infinite-dimensional realizations

Historical primary terminology: **quasi-similarity**.

J. William Helton and Joseph A. Ball,
*The cascade decompositions of a given system vs the linear fractional decompositions of its transfer function*,
Integral Equations and Operator Theory 5 (1982), 341–385.

The paper explicitly states that minimal infinite-dimensional systems with the same transfer function are quasi-similar and cites:

J. W. Helton,
*Discrete systems, operator models and scattering theory*,
J. Functional Analysis 16 (1974), 15–38.

P. A. Fuhrmann,
*Linear Systems and Operators in Hilbert Space*,
McGraw-Hill, 1981.

Relevant foundation:

J. S. Baras and R. W. Brockett,
*H^2-Functions and Infinite-Dimensional Realization Theory*,
SIAM J. Control 13(1) (1975), 221–241,
DOI 10.1137/0313013.

Modern well-posed-system literature also uses **pseudo-similarity** for broader closed densely-defined intertwining relations. Use quasi-similarity as the historical theorem name; treat pseudo-similarity as convention-dependent modern terminology.

### Initial correlations and non-CP reduced dynamics

P. Pechukas,
*Reduced Dynamics Need Not Be Completely Positive*,
Phys. Rev. Lett. 73 (1994), 1060–1062,
DOI 10.1103/PhysRevLett.73.1060.

R. Alicki, comment,
Phys. Rev. Lett. 75 (1995), 3020,
DOI 10.1103/PhysRevLett.75.3020.

P. Pechukas, reply,
Phys. Rev. Lett. 75 (1995), 3021.

T. F. Jordan, A. Shaji, E. C. G. Sudarshan,
*Dynamics of initially entangled open quantum systems*,
Phys. Rev. A 70 (2004), 052110,
DOI 10.1103/PhysRevA.70.052110.

A. Shaji, E. C. G. Sudarshan,
*Who's afraid of not completely positive maps?*,
Phys. Lett. A 341 (2005), 48–54,
DOI 10.1016/j.physleta.2005.04.029.

These support the compatibility-domain/non-CP possibility, not a blanket claim that initial correlations always force non-CP dynamics.

### Standard hosts

D. Blackwell,
*Equivalent Comparisons of Experiments*,
Ann. Math. Statist. 24(2) (1953), 265–272,
DOI 10.1214/aoms/1177729032.

G. Lüders,
*Über die Zustandsänderung durch den Meßprozeß*,
Annalen der Physik 443 (1950), 322–328,
DOI 10.1002/andp.19504430510.

G. C. Layek,
*Conjugacy of Maps*,
in *An Introduction to Dynamical Systems and Chaos*,
Springer, 2015,
DOI 10.1007/978-81-322-2556-0_11.

No named theorem was located for the exact C3 equal-survival witness; treat it as an elementary standard-host counterexample, not a priority claim.

## Disposition

TASK1_UNIVERSAL_E = EXACT_IFF_MU2_NONPOSITIVE.
TASK1_FIXED_E = GLOBAL_MU2_NECESSITY_FALSE.
TASK1_MISALIGNED = UNIVERSAL_CEILING_INFINITE_ALREADY_G0.
TASK1_REPLACEMENT_HOST = HYBRID_RESET_FLOW_OUTPUT_ENERGY / STORAGE.
TASK3_1 = PASS_EXACT_WITNESS.
TASK3_2_POINT_SPECTRUM = PASS_EXACT_WITNESS.
TASK3_2_CONTINUOUS_SPECTRUM = PASS_NEW_EXACT_ANALOGUE.
TASK3_3 = PASS_EXACT_WITNESS_WITH_CONTINUITY_TYPE_GUARD.
TASK2_1 = QUASI_SIMILARITY_PRIMARY_HISTORICAL_ATTRIBUTION / PSEUDO_SIMILARITY_CONVENTION_DEPENDENT.
TASK2_2 = PECHUKAS / JORDAN-SHAJI-SUDARSHAN ATTRIBUTION_SUPPORTED.
TASK2_3 = STANDARD_HOSTS_IDENTIFIED / NO_PRIORITY_CLAIM.

TURN_2 = NOT TOUCHED.

NO novelty / NO canon / NO EXEC_SIGN / NO NEW TASK.
