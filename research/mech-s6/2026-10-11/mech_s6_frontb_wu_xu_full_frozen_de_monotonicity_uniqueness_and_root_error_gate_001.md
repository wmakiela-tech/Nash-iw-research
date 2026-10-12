---
artifact_id: MECH-S6-FRONTB-WU-XU-FULL-FROZEN-DE-MONOTONICITY-UNIQUENESS-AND-ROOT-ERROR-GATE-001
bw_ingestion_event_id: ING-20261011-0022
bw_qualification_state: FRONTB_FROZEN_DE_UNIQUENESS
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SYNCED
source_surface: GOOGLE_DRIVE
source_revision: AHj4eMROcB8b-Kbi3mXGjeekDCYzdyZlS5eNLkuxh4xAvsDo6-8O32Y373PQppgfDZDV6Mr71eys6hkR_1IRcRBftnjT5gjv8sv6Cm4OC6U
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# MECH-S6-FRONTB-WU-XU-FULL-FROZEN-DE-MONOTONICITY-UNIQUENESS-AND-ROOT-ERROR-GATE-001

> Public-safe mirror of the BW-linked Drive source. BW controls lifecycle/currentness; this GitHub body does not upgrade scientific authority. Private provider locators were redacted during mirroring.

MECH-S6 — FRONT B WU–XU FULL FROZEN DE MONOTONICITY / UNIQUENESS / ROOT-ERROR GATE
RETURN_ID: MECH-S6-FRONTB-WU-XU-FULL-FROZEN-DE-MONOTONICITY-UNIQUENESS-AND-ROOT-ERROR-GATE-001
IN_REPLY_TO:
MECH-S6-FRONTB-WU-XU-TYPED-DIRECTIONAL-RATE-DESCRIPTOR-AND-DE-ERROR-BRIDGE-REPAIR-001
XH-S3-FRONTB-WU-XU-SOURCE-MATCHED-WATERFALL-MAP-HARVEST-019
SW-FRONTB-CHARGED-PION-INNER-EQUILIBRIUM-001
GEEKY-S10-DRAFT014-FRONTB-GLOBAL-FIXED-POINT-EXISTENCE-UNIQUENESS-CONDITIONING-GATE-001
RESULT_CLASS: SOURCE-NATIVE EXACT FROZEN-CLOSURE THEOREM / ALL PUBLIC WU–XU HADRON SPECIES / NO DYNAMIC OR BBN ENDPOINT CLAIM
STATUS: PASS_EXACT_FOR_CURRENT_PUBLIC_WU_XU_FROZEN_ALGEBRAIC_DE_MODEL
1. QUESTION
Given the current public Wu–Xu PBH hadronic system, replace each fast hadron population by its algebraic dynamical-equilibrium value
n_h^DE(X,t)=S_h(t)/D_h(X,t),
with background quantities and PBH source amplitudes frozen at one time.
Does the resulting reduced neutron-fraction vector field have:
existence;
uniqueness;
and a useful conditioning bound
for its instantaneous fixed point?
2. SOURCE-NATIVE SETUP
Write X for X_n in [0,1].
The reduced hadronic neutron term has the exact source-code form
F_had(X)
=
(1-X)A(X)-X B(X),
where A is aggregate p->n rate and B aggregate n->p rate.
Under algebraic DE, each source species contributes through n_h^DE=S_h/D_h(X).
Current public Wu–Xu species:
pi-;
pi+;
K-;
K0L;
pbar;
nbar.
All PBH source amplitudes S_h are nonnegative.
All source-code conversion/nonconversion coefficients used below are nonnegative; the published parameter file makes the load-bearing coefficients strictly positive in the active channels.
3. PI- CONTRIBUTION
Define:
S=S_pi >=0,
gamma=Gamma_pi- >0,
k=k_pi-_pn>0,
c=n_B k>0.
DE population:
n_pi- = S/[gamma+c(1-X)].
Hadronic neutron contribution:
F_pi-(X)
=
(1-X)n_pi- k
=
S k(1-X)/[gamma+c(1-X)].
Differentiate:
F_pi-'(X)
=
- S k gamma /
[gamma+c(1-X)]^2
<=0,
strictly <0 when S>0.
Thus the pi- DE contribution is monotone decreasing in X.
4. PI+ CONTRIBUTION
Define:
S=S_pi >=0,
gamma=Gamma_pi+ >0,
k=k_pi+_np>0,
c=n_B k>0.
DE population:
n_pi+ = S/[gamma+cX].
Contribution:
F_pi+(X)
=
- X n_pi+ k
=
- S k X/[gamma+cX].
Derivative:
F_pi+'(X)
=
- S k gamma /
[gamma+cX]^2
<=0,
strictly <0 when S>0.
5. K- CONTRIBUTION
Let
a = k_K-_pn >0,
b = k_K-_np >0,
u = k_K-_nTOn >0,
v = k_K-_pTOp >0,
gamma = Gamma_K- >0.
The source-code DE denominator is
D(X)
=
gamma
+
n_B X(u+b)
+
n_B(1-X)(a+v).
Population:
n_K-=S_K/D(X).
Contribution:
F_K-(X)
=
S_K
[a-(a+b)X]
/
D(X).
Direct differentiation gives
F_K-'(X)
=
-
S_K
[
(a+b)gamma
+
n_B(a u + b v + 2ab)
]
/
D(X)^2
<=0.
All bracketed terms are nonnegative and strictly positive for active source S_K>0.
Therefore the full K- DE contribution is strictly decreasing in X despite state-dependent depletion.
This is a source-specific positive result stronger than a generic local Picard criterion.
6. K0L CONTRIBUTION
The K0L equations have the same algebraic structure:
D(X)
=
gamma
+
n_B X(u+b)
+
n_B(1-X)(a+v),
F_K0L(X)
=
S_K0L
[a-(a+b)X]/D(X),
with current public coefficients:
a=k_pn>0,
b=k_np>0,
u=k_nTOn>0,
v=k_pTOp>0,
gamma=Gamma_K0L>0.
Hence identically:
F_K0L'(X)
=
-
S_K0L
[
(a+b)gamma
+
n_B(a u + b v + 2ab)
]
/
D(X)^2
<=0,
strictly negative for active source.
7. PBAR CONTRIBUTION
For antiprotons the public population sink is collision-controlled:
D_pbar(X)
=
n_B[
X b
+
(1-X)v
],
with:
b=k_pbar_np>0,
v=k_pbar_pTOp>0.
DE population:
n_pbar=S_pbar/D_pbar.
Neutron contribution:
F_pbar(X)
=
- X n_pbar b
=
-
S_pbar b X
/
[n_B(v+(b-v)X)].
Derivative:
F_pbar'(X)
=
-
S_pbar b v
/
[
n_B
(v+(b-v)X)^2
]
<=0,
strictly negative for active source.
The nonconversion pbar+p -> pbar-annihilation channel v is load-bearing for this simple strict derivative formula.
8. NBAR CONTRIBUTION
For antineutrons:
D_nbar(X)
=
n_B[
X u
+
(1-X)a
],
where:
u=k_nbar_nTOn>0,
a=k_nbar_pn>0.
DE population:
n_nbar=S_nbar/D_nbar.
Contribution:
F_nbar(X)
=
(1-X)n_nbar a
=
S_nbar a(1-X)
/
[n_B(a+(u-a)X)].
Derivative:
F_nbar'(X)
=
-
S_nbar a u
/
[
n_B
(a+(u-a)X)^2
]
<=0,
strictly negative for active source.
9. ALL-HADRON MONOTONICITY
The full frozen algebraic-DE hadronic term is the sum
F_had^DE
=
F_pi-
+
F_pi+
+
F_K-
+
F_K0L
+
F_pbar
+
F_nbar.
Each contribution is nonincreasing in X.
Therefore:
dF_had^DE/dX <=0.
It is strictly decreasing whenever at least one active hadronic source contributes with the current positive coefficients.
This result is exact for the current public Wu–Xu frozen algebraic closure.
10. STANDARD WEAK + NEUTRON DECAY BASELINE
The same public solver uses
F_SM(X)
=
-Gamma_n_SM
[
X-(1-X)e^{-Q/T}
]
and
F_decay(X)
=
-X/tau_n.
At frozen T:
dF_SM/dX
=
-Gamma_n_SM(1+e^{-Q/T}) <0,
dF_decay/dX
=
-1/tau_n <0.
Define
c0(t)
=
Gamma_n_SM(t)[1+e^{-Q/T(t)}]
+
1/tau_n
>0.
Then for the full frozen reduced DE vector field
G_DE(X,t)
=
F_SM+F_decay+F_had^DE,
one has
partial_X G_DE
<=
-c0(t)
<0.
Thus the total frozen vector field is uniformly strictly decreasing on X in [0,1].
11. EXISTENCE AND UNIQUENESS
At X=0:
F_SM(0)=Gamma_n_SM e^{-Q/T}>0,
F_decay(0)=0,
and every active p->n hadronic contribution is nonnegative.
Therefore:
G_DE(0)>0.
At X=1:
F_SM(1)=-Gamma_n_SM<0,
F_decay(1)=-1/tau_n<0,
and every n->p hadronic contribution is nonpositive.
Therefore:
G_DE(1)<0.
By continuity, at least one root exists in (0,1).
By strict monotonicity, exactly one root exists.
Hence:
FROZEN_WU_XU_DE_FIXED_POINT_EXISTENCE = PASS_EXACT.
FROZEN_WU_XU_DE_FIXED_POINT_UNIQUENESS = PASS_EXACT.
No Picard contraction assumption is needed.
12. RELATION TO GEEKY GLOBAL FIXED-POINT GATE
Geeky's generic scalar theorem correctly distinguishes:
existence;
uniqueness;
conditioning;
solver convergence.
The current result source-closes the first two for the reduced frozen Wu–Xu algebraic-DE neutron equation.
It also supplies a source-native regularity margin:
|partial_X G_DE|
>=
c0(t).
Therefore the physical fixed point remains regular even if a particular inner iteration is not contractive.
SOLVER CONVERGENCE != PHYSICAL UNIQUENESS.
13. FROZEN ROOT CONDITIONING AGAINST RHS ERROR
Let X_DE be the unique root of G_DE.
Let an alternative frozen reduced model have
G_ALT(X)
=
G_DE(X)
-
delta F(X),
and root X_ALT in [0,1].
Assume both roots exist.
Since G_DE is strictly decreasing with
|G_DE'(X)|>=c0,
the mean value theorem gives exactly:
|X_DE-X_ALT|
<=
sup_{X in [0,1]}
|delta F(X)|
/
c0(t).
Thus an independently certified source-matched error in the hadronic reduced vector field immediately gives a frozen-equilibrium neutron-fraction error bound.
14. COMPOSITION WITH THE POPULATION-ERROR BRIDGE
From the prior Mech repair, at common X:
delta F_had(X)
=
sum_h e_h(X)
[
(1-X)k_h^pn
-
X k_h^np
],
where
e_h=n_h^DE-n_h^FULL.
Hence:
|delta F_had(X)|
<=
sum_h |e_h(X)|
[
(1-X)k_h^pn
+
X k_h^np
].
Combining with the monotonicity margin:
|X_DE-X_ALT|
<=
1/c0
sup_X
sum_h |e_h(X)|
[
(1-X)k_h^pn+Xk_h^np
].
This is a fully typed bridge:
INDEPENDENT HADRON POPULATION ERROR
->
REDUCED RHS ERROR
->
FROZEN ROOT ERROR.
15. IMPORTANT LIMITATION — THIS IS NOT DYNAMIC TRACKING
The instantaneous unique root X_*(t) can move in time.
The physical X_n(t) need not equal X_*(t).
Therefore:
UNIQUE FROZEN ROOT
!=
DYNAMIC TRACKING OF THAT ROOT.
A separate timescale / moving-equilibrium analysis is required if one wants to replace the neutron ODE itself by an instantaneous equilibrium condition.
The present Front B use is narrower:
it certifies the internal source-native algebraic hadron closure and the uniqueness/conditioning of the reduced frozen neutron fixed point.
16. IMPORTANT LIMITATION — HADRON QSS STILL NEEDS VALIDATION
The theorem assumes the algebraic DE populations
n_h^DE=S_h/D_h(X,t).
It does not prove that the full time-dependent hadron populations satisfy
n_h^FULL approximately n_h^DE.
That remains the source-matched PBH transfer question.
Therefore:
ALGEBRAIC DE MAP WELL-POSED
!=
DE DYNAMIC ACCURACY.
17. SOURCE AMPLITUDE DOES NOT CREATE MULTIPLE FROZEN ROOTS HERE
Within the current public Wu–Xu algebraic structure, increasing a nonnegative PBH source amplitude scales one or more monotone species contributions but does not change their derivative sign.
Thus source amplitude alone cannot generate a fold/multiple frozen X roots inside this model.
This is source-specific.
It does NOT generalize to:
secondary source feedback S_h(X);
cross-species feed-down changing source terms;
new reaction channels;
or modified depletion laws.
SW already provided counterexamples showing positive state-dependent source feedback can create multiple roots.
Therefore:
CURRENT WU_XU PRIMARY-SOURCE STRUCTURE
= UNIQUE FROZEN ROOT.
POSITIVE SOURCE IN GENERAL
!=
UNIQUENESS.
18. CHEAPEST FALSIFIER OF THIS THEOREM UNDER MODEL EXTENSION
Any extension must be re-audited if it introduces:
S_h explicitly depending on X;
cross-species source feed-down;
negative effective source components;
new conversion/nonconversion channels with different state structure;
background variables solved simultaneously inside the frozen root;
or a source term depending on hadron populations.
Cheapest test:
differentiate the exact extended F_had(X) and check whether the total derivative can change sign on [0,1].
If yes:
the present uniqueness theorem no longer applies.
19. PRACTICAL VALIDATION ORDER
For source-matched PBH DE validation:
A. keep current exact algebraic DE map;
B. compare n_h^DE vs full n_h at common background/state;
C. convert population errors to delta A, delta B and delta F;
D. use the c0 margin to bound the frozen equilibrium displacement;
E. separately compare full dynamic X_n trajectories;
F. only then apply Y_p / D-H target-weighted validation.
This order prevents:
descriptor circularity;
solver-convergence overinterpretation;
and premature BBN endpoint claims.
20. CLAIM CEILING
PASS EXACT FOR CURRENT PUBLIC WU–XU FROZEN MODEL:
all six species DE contributions are nonincreasing in X;
full hadronic DE term is nonincreasing;
standard weak+decay makes total frozen reduced field strictly decreasing;
one and only one frozen neutron fixed point exists in (0,1);
regularity margin at least c0(t);
sup-norm reduced-field error gives root-displacement bound <= ||deltaF||_infty/c0.
NOT PASSED:
hadron DE dynamic tracking;
full-vs-DE PBH trajectory agreement;
moving-fixed-point tracking;
B2 population transfer;
Y_p / D-H target accuracy;
source-matched K_PBH;
numerical PBH bound.
21. STATUS
WU_XU_FULL_FROZEN_DE_MONOTONICITY = PASS_EXACT.
WU_XU_FROZEN_X_FIXED_POINT_EXISTENCE = PASS_EXACT.
WU_XU_FROZEN_X_FIXED_POINT_UNIQUENESS = PASS_EXACT.
WU_XU_FROZEN_ROOT_REGULARITY_MARGIN = PASS_EXACT.
WU_XU_FROZEN_ROOT_ERROR_BOUND = PASS_EXACT_CONDITIONAL_ON_DELTAF_BOUND.
PICARD_CONTRACTION_REQUIRED_FOR_PHYSICAL_UNIQUENESS = NO.
PBH_DE_DYNAMIC_ACCURACY = NOT_VALIDATED.
PBH_DE_VS_FULL_DESCRIPTOR_VALIDATION = NOT_RUN.
PBH_B2_WATERFALL_TRANSFER = OPEN.
SOURCE_MATCHED_K_PBH = UNDEFINED.
NO PBH BOUND / NO ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY.
REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD.
22. SOURCE BASIS
Wu & Xu, Primordial black holes evaporating before Big Bang nucleosynthesis, JCAP 02 (2026) 063, arXiv:2509.05618.
Public source:
https://github.com/Fenyutanchan/Primordial-Black-Hole
Current public:
arXiv-2509.05618/main-scan.jl
arXiv-2509.05618/tool_script-parameters.jl
SW-FRONTB-CHARGED-PION-INNER-EQUILIBRIUM-001.
GEEKY-S10-DRAFT014-FRONTB-GLOBAL-FIXED-POINT-EXISTENCE-UNIQUENESS-CONDITIONING-GATE-001.
MECH-S6-FRONTB-WU-XU-TYPED-DIRECTIONAL-RATE-DESCRIPTOR-AND-DE-ERROR-BRIDGE-REPAIR-001.
