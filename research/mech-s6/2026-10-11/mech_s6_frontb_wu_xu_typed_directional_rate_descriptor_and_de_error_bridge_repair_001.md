---
artifact_id: MECH-S6-FRONTB-WU-XU-TYPED-DIRECTIONAL-RATE-DESCRIPTOR-AND-DE-ERROR-BRIDGE-REPAIR-001
bw_ingestion_event_id: ING-20261011-0018
bw_qualification_state: FRONTB_WUXU_TYPED_DIRECTIONAL_REPAIR
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SYNCED
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# MECH-S6-FRONTB-WU-XU-TYPED-DIRECTIONAL-RATE-DESCRIPTOR-AND-DE-ERROR-BRIDGE-REPAIR-001

> Public-safe mirror of the BW-linked Drive source. BW controls lifecycle/currentness; this GitHub body does not upgrade scientific authority. Private provider locators were redacted during mirroring.

MECH-S6 — FRONT B WU–XU TYPED DIRECTIONAL-RATE DESCRIPTOR / DE ERROR-BRIDGE REPAIR
RETURN_ID: MECH-S6-FRONTB-WU-XU-TYPED-DIRECTIONAL-RATE-DESCRIPTOR-AND-DE-ERROR-BRIDGE-REPAIR-001
IN_REPLY_TO:
REC9-NC-WATERFALL-DESCRIPTOR-ERROR-LAW-REFEREE-001
NC-REC9-WATERFALL-REFEREE-ACCEPTANCE-AND-REPAIR-001
XH-S3-FRONTB-WU-XU-SOURCE-MATCHED-WATERFALL-MAP-HARVEST-019
LT3 DRAFT017 §§91–95
RESULT_CLASS: HIGH-SEVERITY OBJECT-MAP REPAIR / SOURCE-NATIVE EXACT ALGEBRA / NO NUMERICAL PBH BOUND
STATUS: PRIMARY DIRECTIONAL-RATE OBJECT PASS / WATERFALL (R,q) CHART CONDITIONAL / NC BRANCH-FRACTION REPAIR NARROWED
1. EXECUTIVE REPAIR
Rec9 is correct that the previous map
hadron depletion D_h
=
nucleon interconversion strength R_h
is false.
Direct inspection of the current public Wu–Xu source sharpens the repair further:
the safest PRIMARY reduced object is not {X_n^qs,R_h} itself, but the pair of directional nucleon-conversion rates
A(t,X) = Lambda_pn(t,X),
B(t,X) = Lambda_np(t,X).
Then, only where
R=A+B > 0,
define the derived chart
R = A+B,
q = X_n^qs = A/(A+B).
The hadronic neutron-fraction RHS is exactly
F_had(X,t)
=
(1-X)A - X B
=
R(q-X).
Thus:
(A,B) = PRIMARY TYPED OBJECT.
(R,q) = DERIVED COORDINATE CHART ON R>0.
This avoids both the hadron-depletion object mismatch and the q singularity when R -> 0.
2. DIRECT PUBLIC SOURCE EQUATIONS
Current Wu–Xu public main-scan code evolves:
dX_n/dt|had
=
dX_n/dt|pi
+
dX_n/dt|K-
+
dX_n/dt|K0L
+
dX_n/dt|pbar
+
dX_n/dt|nbar.
The terms are exactly of the form
dX_n/dt|had
=
(1-X_n) A
-
X_n B,
where
A =
n_pi- k_pi-_pn
+
n_K- k_K-_pn
+
n_K0L k_K0L_pn
+
n_nbar k_nbar_pn,
B =
n_pi+ k_pi+_np
+
n_K- k_K-_np
+
n_K0L k_K0L_np
+
n_pbar k_pbar_np.
Here k denotes the corresponding source-code sigma-v conversion coefficient.
Therefore XH019's exact replay statement is correct:
if A(t),B(t) are extracted from a full trajectory, they reproduce the hadronic contribution to the reduced neutron equation exactly.
3. WHY HADRON DEPLETION IS A DIFFERENT OBJECT
The same source evolves each injected hadron population by
dn_h/dt
=
S_h
-
D_h(X,T,n_B) n_h.
But D_h contains more than nucleon conversion.
Examples from the public code:
pi-:
D_pi-
=
Gamma_pi-
+
n_B(1-X) k_pi-_pn.
pi+:
D_pi+
=
Gamma_pi+
+
n_B X k_pi+_np.
K-:
D_K-
=
Gamma_K-
+
n_B X(k_K-_nTOn + k_K-_np)
+
n_B(1-X)(k_K-_pn + k_K-_pTOp).
K0L has the analogous structure.
For antinucleons the population sink contains conversion AND nonconversion annihilation channels.
Thus D_h includes:
decay;
conversion collisions;
nonconversion collisions.
Meanwhile A,B contain only the directional nucleon-conversion contributions.
Therefore:
HADRON POPULATION DEPLETION RATE != NUCLEON INTERCONVERSION RATE.
This is not merely a notation issue; the channel sets and physical units of the intermediate hazards differ.
4. FURTHER REPAIR TO NC'S ACCEPTANCE MESSAGE
NC proposes as a repair:
X_n^qs = b_pn/(b_pn+b_np),
where b_pn,b_np are described as branches of the hadron destruction rate D_h.
That equality is NOT generic if b refers to actual depletion-hazard branch fractions.
For a single species that can convert in both directions:
D_pn
=
n_B(1-X) k_pn,
D_np
=
n_B X k_np.
The corresponding conditional fraction among conversion destructions is
D_pn/(D_pn+D_np)
=
(1-X)k_pn /
[(1-X)k_pn + X k_np].
But the nucleon-RHS equilibrium coordinate is
q
=
k_pn/(k_pn+k_np)
for that same single-species population.
These are generally different.
For k_pn,k_np > 0 they coincide only under an additional special condition such as X=1/2, not merely because the total conversion fraction D_conv/D_h is time-independent.
For the pion sector the situation is even less reducible:
pi- and pi+ are separate populations with separate depletion denominators, while q uses their aggregate directional rates.
Therefore DRAFT017 must NOT repair the old identity by simply replacing it with a destruction-branch ratio identity.
Correct bridge:
population states n_h
+
directional conversion coefficients k_h^pn,k_h^np
->
A,B
->
R,q.
5. SOURCE-MATCHED ALGEBRAIC DE MAP
The Wu–Xu equations directly supply a PBH-specific dynamical-equilibrium candidate.
For each species h:
n_h^DE(X,t)
=
S_h(t)/D_h(X,t)
when the algebraic QSS equation is admitted.
Then define
A_DE(X,t)
=
sum_h n_h^DE(X,t) k_h^pn(T),
B_DE(X,t)
=
sum_h n_h^DE(X,t) k_h^np(T),
using zero coefficient where a direction is absent.
Only after these are constructed define
R_DE=A_DE+B_DE,
q_DE=A_DE/R_DE
when R_DE>0.
This is the source-native route.
It does not import a hadron-depletion branching fraction as a nucleon descriptor.
6. EXACT POPULATION-ERROR TO NEUTRON-RHS BRIDGE
Let full hadron populations be n_h and DE populations n_h^DE.
At one common neutron state X and common background define
e_h
=
n_h^DE - n_h.
Then exactly:
delta A
=
A_DE-A_FULL
=
sum_h e_h k_h^pn,
delta B
=
B_DE-B_FULL
=
sum_h e_h k_h^np.
Therefore the hadronic neutron-RHS discrepancy is exactly
delta F_had(X,t)
=
F_DE-F_FULL
=
(1-X) delta A
-
X delta B
=
sum_h e_h
[(1-X)k_h^pn - X k_h^np].
This is the missing typed bridge from independent hadron-population closure error to the reduced neutron equation.
7. SAFE INDEPENDENT BOUND
Because all physical rate coefficients are nonnegative:
|delta F_had|
<=
sum_h |e_h|
[(1-X)k_h^pn + X k_h^np].
This certificate is NONCIRCULAR only if |e_h| is bounded independently of the DE substitution being tested.
Legal sources of e_h control include:
exact solution of a prescribed linear source-sink equation;
variation-of-constants tracking bound;
direct full-vs-DE source-matched comparison;
or another independently validated finite-error theorem.
Using n_h^DE itself as proof that e_h is small remains circular.
8. DESCRIPTOR ERROR DECOMPOSITION
Where R_FULL>0 and R_DE>0:
q_FULL=A/R,
q_DE=A_DE/R_DE.
The exact magnitude error is
delta R
=
delta A + delta B.
The exact ratio error is
q_DE-q_FULL
=
(B delta A - A delta B)/
(R_FULL R_DE).
Hence q can become numerically ill-conditioned when R is small even while the physical hadronic forcing F_had is negligible.
Therefore:
Q-RATIO INSTABILITY NEAR R=0
!=
LARGE PHYSICAL RHS ERROR.
This is another reason to retain (A,B) as the primary object and treat (R,q) as a derived chart.
9. EXACT RATIO/MAGNITUDE FORCE DECOMPOSITION
At a common state X:
F_DE-F_FULL
=
R_DE(q_DE-q_FULL)
+
(R_DE-R_FULL)(q_FULL-X).
Equivalently:
=
R_FULL(q_DE-q_FULL)
+
(R_DE-R_FULL)(q_DE-X).
Thus the descriptor comparison has a precise meaning when R>0.
A simple bound is:
|delta F|
<=
R_DE |delta q|
+
|delta R| |q_FULL-X|
<=
R_DE |delta q| + |delta R|.
But the (A,B) bound in §7 remains better conditioned at small R.
10. FULL-TRAJECTORY VERSUS COMMON-STATE COMPARISON
A major comparison guard:
A_FULL(t),B_FULL(t)
are normally evaluated along X_FULL(t).
A_DE(t),B_DE(t)
are normally evaluated along X_DE(t).
Directly subtracting those time series conflates:
CLOSURE ERROR
with
STATE-MISMATCH FEEDBACK.
For a constitutive validation one should first compare
A_DE(X,t) vs A_FULL(X,t),
B_DE(X,t) vs B_FULL(X,t)
at a COMMON supplied state/background where possible.
If only two self-consistent trajectories are available, the error decomposition must include the state mismatch explicitly.
COMMON-TIME != COMMON-STATE.
11. TRAJECTORY ERROR BRIDGE
Write the common baseline weak/decay dynamics as f_0(X,t).
Full:
Xdot
=
f_0(X,t)
+
F_FULL(X,t).
DE:
Xtilde_dot
=
f_0(Xtilde,t)
+
F_DE(Xtilde,t).
Let e_X=Xtilde-X.
Add and subtract the DE vector field at X:
e_Xdot
=
[g_DE(Xtilde,t)-g_DE(X,t)]
+
delta F(X,t),
where
g_DE=f_0+F_DE,
delta F(X,t)=F_DE(X,t)-F_FULL(X,t).
If g_DE is Lipschitz in X with coefficient L(t), then:
|e_X(T)|
<=
exp(Integral L)
[
|e_X(t0)|
+
Integral exp(-Integral_to_s L)
|delta F(s)| ds
]
in the standard Gronwall form.
Thus an independent species-population bound can be propagated:
e_h
->
delta A,delta B
->
delta F
->
delta X_n
->
later Y_p/D-H target validation.
No descriptor-only shortcut is needed.
12. MULTI-SPECIES CORRECTION
INT7 is correct:
MULTI_SPECIES alone does not invalidate the reduced descriptor.
No matter how many species contribute, the instantaneous reduced neutron RHS depends on them only through the two aggregates A and B.
Thus:
MULTI_SPECIES COMPOSITION
->
(A,B)
is an exact compression for the reduced X_n RHS at that instant.
But:
REPLAY SUFFICIENCY
!=
PREDICTIVE CLOSURE SUFFICIENCY.
The DE must still predict the correct A,B from source/background/state.
The real gate is not species count.
It is whether the source-native constitutive map
(S_h, X, T, n_B, ...)
->
n_h
->
(A,B)
is accurately closed.
13. BRANCHING_PRESCRIBED VS STATE_DEPENDENT — RETYPED
The phrase remains useful only after the object is specified.
For hadron population destruction:
branching means partition of D_h.
For neutron conversion:
directional ratio means A/(A+B).
These are different.
State dependence may enter through:
n_h(X,t);
Coulomb factors;
target availability factors in D_h;
PBH source composition;
background density;
and possibly cross-species feed-down in a richer model.
Therefore record separately:
POPULATION_DEPLETION_BRANCHING_STATUS
and
NUCLEON_DIRECTIONAL_RATIO_STATUS.
Do not use one as a synonym for the other.
14. MINIMUM WATERFALL RECORD — REPAIRED
PRIMARY:
A(t,X)=Lambda_pn.
B(t,X)=Lambda_np.
DERIVED WHEN R>0:
R=A+B.
q=A/R.
POPULATION LAYER:
for each h:
S_h;
D_h;
n_h_FULL;
n_h_DE;
e_h.
COEFFICIENT LAYER:
k_h^pn;
k_h^np;
nonconversion coefficients;
decay coefficients.
ERROR LAYER:
delta A;
delta B;
delta F;
common-state vs two-trajectory flag;
independent e_h certificate.
TARGET LAYER:
X_n trajectory discrepancy;
later Y_p/D-H target-weighted discrepancy.
15. DRAFT017 REPAIR RECOMMENDATION
The controlling sentence
"Gamma_h = R_h, b_pn = X_n^qs. Thus {X_n^qs,R_h} are exactly the ratio/magnitude objects"
should be removed/retyped.
Recommended replacement:
"At the reduced nucleon-equation level, the exact source-native directional objects are
A=Lambda_pn and B=Lambda_np.
Where R=A+B>0, define q=A/R, giving
F_had=R(q-X_n).
The pair {q,R} is therefore an exact replay chart for the reduced hadronic X_n RHS when extracted from a trajectory.
It is NOT identical to the hadron-population depletion coefficient or its destruction-branch fractions.
A predictive DE claim requires a separate source-native map from S_h,D_h to n_h and then to A,B, with independent population-error control."
16. CLAIM CEILING
PASS EXACT:
Wu–Xu source-code reduced RHS refactorization.
(A,B) replay sufficiency for the hadronic X_n term.
(R,q) replay sufficiency on R>0.
source-native algebraic DE candidate n_h=S_h/D_h.
exact e_h -> deltaA/deltaB -> deltaF bridge.
multi-species compression to A,B for the reduced instantaneous neutron RHS.
NOT PASSED:
PBH DE-vs-full population accuracy.
PBH DE-vs-full A,B accuracy.
B2 population transfer validation.
Y_p / D-H target accuracy.
source-matched K_PBH.
numerical PBH bound.
REJECT / RETYPE:
D_h=R_h.
hadron-destruction b_pn=X_n^qs generically.
descriptor-only admission using DE populations as its own certificate.
multi-species=>failure automatically.
elasticity>=1=>no equilibrium.
17. STATUS
DRAFT017_OBJECT_MAP_REPAIR = URGENT.
WU_XU_DIRECTIONAL_RATE_OBJECT = PASS_EXACT.
WU_XU_RQ_REPLAY_CHART = PASS_EXACT_CONDITIONAL_R_GT_0.
HADRON_DEPLETION_TO_RQ_DIRECT_IDENTITY = REJECTED.
NC_BRANCH_FRACTION_REPAIR = NARROWED / NOT GENERIC.
INDEPENDENT_POPULATION_ERROR_BRIDGE = PASS_EXACT.
PBH_DE_VS_FULL_DESCRIPTOR_VALIDATION = NOT_RUN.
PBH_B2_WATERFALL_TRANSFER = OPEN.
REDUCED_WATERFALL_DESCRIPTOR = REPLAY_VALIDATED / PREDICTIVE_CLOSURE_NOT_VALIDATED.
SOURCE_MATCHED_K_PBH = UNDEFINED.
NO PBH BOUND / NO ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY.
REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD.
18. SOURCE BASIS
Wu & Xu, Primordial black holes evaporating before Big Bang nucleosynthesis, JCAP 02 (2026) 063, arXiv:2509.05618.
Public source:
https://github.com/Fenyutanchan/Primordial-Black-Hole
Current public main-scan.jl directly inspected.
XH-S3-FRONTB-WU-XU-SOURCE-MATCHED-WATERFALL-MAP-HARVEST-019.
REC9-NC-WATERFALL-DESCRIPTOR-ERROR-LAW-REFEREE-001.
NC-REC9-WATERFALL-REFEREE-ACCEPTANCE-AND-REPAIR-001.
