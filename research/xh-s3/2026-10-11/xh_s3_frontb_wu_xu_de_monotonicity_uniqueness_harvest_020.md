---
artifact_id: XH-S3-FRONTB-WU-XU-DE-MONOTONICITY-UNIQUENESS-HARVEST-020
bw_ingestion_event_id: ING-20261011-0027
bw_qualification_state: FRONTB_WUXU_UNIQUENESS_HARVEST
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: EXTERNAL_EVIDENCE_NO_AUTHORITY
archive_mode: PUBLIC_ARTIFACT
sync_state: SYNCED
source_surface: GOOGLE_DRIVE
source_revision: AHj4eMSJzL2OxN-oaShkq8EDJJhJva8Efcj8XqsybdI7PXgkMahsLe-vKhB8muzee7xmPSQxsBMcJxkZ_TBXSWVwdx088vuAm3eMvpmQtpk
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# XH-S3-FRONTB-WU-XU-DE-MONOTONICITY-UNIQUENESS-HARVEST-020

> Public-safe mirror of the BW-linked Drive source. BW controls lifecycle/currentness; this GitHub body does not upgrade scientific authority. Private provider locators were redacted during mirroring.

XH-S3 / FRONT B — WU–XU DE MONOTONICITY / UNIQUENESS HARVEST 020
RETURN_ID
XH-S3-FRONTB-WU-XU-DE-MONOTONICITY-UNIQUENESS-HARVEST-020
RESULT
THE SOURCE-MATCHED WU–XU ALGEBRAIC DE NEUTRON-FRACTION FIELD IS STRICTLY DECREASING IN X_n UNDER THE PUBLIC POSITIVE-RATE CONTRACT.
FOR EVERY FROZEN PHYSICAL BACKGROUND/SOURCE STATE IT HAS EXACTLY ONE ROOT IN (0,1).
THIS DOES NOT REQUIRE A PICARD CONTRACTION ASSUMPTION.
THE RESULT EXTENDS STRUCTURALLY TO ANY NONNEGATIVE B2 AGGREGATE HADRON SOURCE USING THE SAME MICROPHYSICS.
PHYSICAL DE-vs-FULL ACCURACY REMAINS OPEN.
FIREWALL
UNIQUE INSTANTANEOUS DE ROOT != ACCURATE DE APPROXIMATION TO FULL TIME EVOLUTION.
UNIQUE ROOT != CONVERGENCE OF AN ARBITRARY FIXED-POINT ITERATION.
MONOTONE REDUCED X_n FIELD != FULL BBN TARGET VALIDATION.
STRUCTURAL B2 EXTENSION != SOURCE-VALIDATED B2 ENDPOINT.
NO CANON / NO EXEC_SIGN / NO NOVELTY / NO PBH BOUND.
1. SOURCE OBJECT
Primary source:
[Wu–Xu JCAP 2026]
[Wu–Xu public GitHub]
Public root solver:
arXiv-2509.05618/main-scan.jl
Public hadronic cross sections:
arXiv-2509.05618/tool_script-parameters.jl
019 established the source-matched algebraic DE candidate by setting each hadron population equation
dn_h/dt = S_h - D_h(X_n) n_h
to zero:
n_h^*(X_n)=S_h/D_h(X_n).
020 asks whether the resulting instantaneous reduced field in X_n can have multiple/no roots or pathological source-dependent branches.
2. GENERAL ONE-SPECIES FORM
For one injected hadronic species h, define nonnegative rates:
p = k_{p->n},
n = k_{n->p},
p0 = k_{p->p},
n0 = k_{n->n},
gamma = intrinsic decay/depletion rate independent of nucleon state,
B = n_B > 0,
S = source >= 0.
The DE population is
n_h^*(X)
=
S / D(X),
with
D(X)
=
gamma
+
B[(1-X)(p+p0)+X(n+n0)].
Its contribution to the neutron-fraction field is
F_h(X)
=
n_h^*(X)
[(1-X)p-X n]
=
S [p-X(p+n)] / D(X).
This form contains the Wu–Xu pion, kaon and antinucleon sectors as special cases.
3. EXACT DERIVATIVE
Differentiate F_h with respect to X.
A direct simplification gives
F_h'(X)
=
-S
[
gamma(p+n)
+
B(
2pn
+
n p0
+
n0 p
)
]
/
D(X)^2.
Every factor in the numerator is nonnegative.
Therefore:
F_h'(X) <= 0.
It is strictly negative whenever S>0 and the species has a conversion channel together with either:
- intrinsic decay;
- the opposite conversion direction;
- or an appropriate nonconversion depletion channel.
This is satisfied by every active hadron species in the public Wu–Xu microphysics.
Crucially:
THE SIGN IS INDEPENDENT OF X.
No elasticity heuristic is needed.
4. SPECIALIZATION TO WU–XU SPECIES
CHARGED PIONS
pi-:
n=0,
p>0,
gamma=Gamma_pi>0.
Thus
F_pi-'(X)
=
-S_pi Gamma_pi p / D_pi-(X)^2
<0
for S_pi>0.
pi+:
p=0,
n>0,
gamma=Gamma_pi>0.
Thus
F_pi+'(X)
=
-S_pi Gamma_pi n / D_pi+(X)^2
<0.
K-
p = sigma v_{K-,p->n},
n = sigma v_{K-,n->p},
p0 = sigma v_{K-,p->p},
n0 = sigma v_{K-,n->n},
gamma=Gamma_K>0.
All declared rates are positive.
Hence F_K-'(X)<0 whenever S_K>0.
K0L
Both conversion directions and both nonconversion channels are positive, with gamma=Gamma_K0L>0.
Hence F_K0L'(X)<0 whenever S_K0L>0.
ANTIPROTON
p=0,
n=sigma v_{p pbar,n->p}>0,
p0=sigma v_{p pbar,p->p}>0,
gamma=0.
Then
F_pbar'(X)
=
-S_p B n p0 / D_pbar(X)^2
<0.
ANTINEUTRON
n=0,
p=sigma v_{n nbar,p->n}>0,
n0=sigma v_{n nbar,n->n}>0,
gamma=0.
Then
F_nbar'(X)
=
-S_n B n0 p / D_nbar(X)^2
<0.
Thus every active source-native DE hadron contribution is monotone decreasing.
5. STANDARD WU–XU WEAK + NEUTRON-DECAY FIELD IS ALSO STRICTLY DECREASING
The public code uses
F_SM(X)
=
-Gamma_n^SM
[
X-(1-X)e^{-Q/T}
].
Therefore
F_SM'(X)
=
-Gamma_n^SM
(1+e^{-Q/T})
<0.
Free-neutron decay contributes
F_decay(X)=-X/tau_n,
so
F_decay'(X)=-1/tau_n<0.
Hence the COMPLETE instantaneous DE reduced field
G_DE(X)
=
F_SM(X)
+
F_decay(X)
+
sum_h F_h(X)
satisfies exactly:
G_DE'(X)<0
for all X in [0,1]
under the public positive-rate/background contract.
6. BOUNDARY SIGNS
At X=0:
F_SM(0)
=
Gamma_n^SM e^{-Q/T}
>0.
F_decay(0)=0.
Every hadronic p->n term is nonnegative.
Thus:
G_DE(0)>0.
At X=1:
F_SM(1)
=
-Gamma_n^SM
<0.
F_decay(1)
=
-1/tau_n
<0.
Every hadronic n->p term is nonpositive.
Thus:
G_DE(1)<0.
Since G_DE is continuous and strictly decreasing on [0,1]:
THERE EXISTS EXACTLY ONE X_* in (0,1)
such that
G_DE(X_*)=0.
This is an exact frozen-state uniqueness theorem for the source-matched Wu–Xu DE closure.
7. IMPORTANT CORRECTION TO ELASTICITY / PICARD LANGUAGE
Earlier project discussion correctly repaired:
|d ln Gamma / d ln n| < 1
as only a LOCAL CONTRACTION condition for a chosen fixed-point iteration.
020 shows that for the actual Wu–Xu reduced DE closure, ROOT UNIQUENESS can be established more directly and more strongly from monotonicity.
Therefore:
PICARD CONTRACTION
is NOT needed for root existence/uniqueness.
Also:
PICARD DIVERGENCE
does NOT imply root nonexistence.
For numerical implementation the safe source-native method is a bracketed scalar root solve on X in [0,1], because the signs at both endpoints and strict monotonicity are proven.
This is algorithmic guidance, not an execution result.
8. EXACT MONOTONICITY MARGIN
Define
c_DE(X)
=
-G_DE'(X)
>0.
Then explicitly:
c_DE(X)
=
Gamma_n^SM(1+e^{-Q/T})
+
1/tau_n
+
sum_h
S_h
[
gamma_h(p_h+n_h)
+
n_B(
2p_h n_h
+
n_h p0_h
+
n0_h p_h
)
]
/
D_h(X)^2.
This provides a source-native instantaneous monotonicity margin.
It is directly compatible with the M12 dynamic-X_n error framework, which assumes a negative partial derivative bound.
A conservative frozen-state lower bound can be obtained by bounding each positive term over X in [0,1].
No numerical bound is claimed here.
9. RELATION TO 019 REPLAY DESCRIPTOR
019 derived exactly:
dX_n/dt |_had
=
R_h(X_n)
[
X_n^{qs}(X_n)-X_n
].
020 proves that the COMPLETE DE RHS built from this state-dependent descriptor is strictly decreasing, despite multi-species feedback.
Therefore:
STATE-DEPENDENT BRANCHING
does NOT by itself create multiple instantaneous neutron-fraction equilibria in the declared Wu–Xu algebraic closure.
It remains load-bearing for:
- the location of the unique root;
- DE-vs-full descriptor mismatch;
- target error.
But not for root multiplicity under this microphysics.
10. B2 STRUCTURAL EXTENSION
Replace monochromatic Wu–Xu source amplitudes S_h(t) by nonnegative B2 population sources:
Q_h(t)
=
a(t)^-3
∫ chi(t;M_i,t_f)
R_h^emit(M(t;M_i,t_f))
dmu_B2(M_i,t_f).
The monotonicity proof uses S_h only as a nonnegative multiplicative factor.
Therefore the SAME instantaneous uniqueness theorem survives any such nonnegative aggregate source:
Q_h(t)>=0
for every hadronic species.
Thus:
B2_AGGREGATION
does NOT introduce instantaneous DE root multiplicity by itself.
This is a structural theorem for the algebraic closure.
It is NOT:
- validation of the B2 population source;
- validation of fast/slow DE accuracy;
- a BBN abundance certificate;
- a PBH constraint.
11. WHAT REMAINS OPEN AFTER 020
The fixed-point existence/uniqueness issue is substantially closed for this closure.
The remaining scientific uncertainties move to:
A DE POPULATION TRACKING
Does n_h^*(X_n,t) track the full Wu–Xu n_h(t) closely enough?
B SOURCE-MATCHED DESCRIPTOR ERROR
How large are:
delta X_n^{qs}(t),
delta R_h(t),
species directional-fraction errors?
C DYNAMIC X_n ERROR
Use the M12 monotone error-propagation host with a source-matched RHS discrepancy.
D FULL BBN TARGET ERROR
Y_p and D/H require the source-matched target-weighted / direct endpoint comparison.
E B2 CARRIER
The B2 aggregate source construction remains to be validated against its representation and background contract.
12. CHEAPEST NEXT SOURCE-NATIVE CHECK
No global PBH scan is justified.
A minimal validation benchmark needs only:
- one frozen monochromatic Wu–Xu source trajectory;
- original full six-hadron ODE;
- algebraic DE closure from 019;
- same background and initial conditions.
Compare:
1 n_h^*(t) vs n_h^FULL(t);
2 X_n^{qs,DE} vs X_n^{qs,FULL};
3 R_h^DE vs R_h^FULL;
4 X_n^DE vs X_n^FULL.
Because uniqueness is now exact, discrepancies cannot be blamed on choosing the wrong DE root.
Only after this comparison is target-level BBN work load-bearing.
This is a validation design, not execution authorization.
13. MODEL-USE DISCIPLINE
No external AI model invoked.
Reason:
the relevant question reduced to an exact algebraic property of the source code.
Direct derivation and source inspection have higher epistemic value than model voting.
An independent model becomes useful only after a concrete numerical/source-matched DE-vs-full result exists, for adversarial audit of:
- derivation;
- numerical stability;
- hidden channel omissions;
- transfer to B2.
14. STATUS
WU_XU_DE_FIELD_MONOTONICITY = PASS / EXACT.
WU_XU_DE_ROOT_EXISTENCE = PASS / EXACT.
WU_XU_DE_ROOT_UNIQUENESS = PASS / EXACT.
PICARD_CONTRACTION_REQUIRED_FOR_UNIQUENESS = NO.
BRACKETED_ROOT_SOLVE_LEGALITY = PASS DESIGN.
STATE_DEPENDENT_BRANCHING_CAUSES_ROOT_MULTIPLICITY = NO IN DECLARED CLOSURE.
B2_NONNEGATIVE_SOURCE_UNIQUENESS_EXTENSION = PASS STRUCTURAL.
DE_VS_FULL_POPULATION_TRACKING = OPEN.
PBH_Yp_DH_TARGET_VALIDATION = OPEN.
SOURCE_MATCHED_K_PBH = UNDEFINED.
NO PBH BOUND / NO ENDPOINT RELEASE.
NO CANON / NO EXEC_SIGN / NO NOVELTY / SCIENCE_FIRST.
SOURCES
[Wu–Xu JCAP 2026]
[Wu–Xu public GitHub]
