---
artifact_id: M12-FRONTB-DYNAMICAL-EQUILIBRIUM-ADMISSION-ERROR-IDENTITY-001
bw_ingestion_event_id: ING-20261010-0132
bw_qualification_state: FRONTB_DE_ADMISSION_ERROR_IDENTITY
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# M12-FRONTB-DYNAMICAL-EQUILIBRIUM-ADMISSION-ERROR-IDENTITY-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

CORRECTION / SUPERSESSION NOTE — 2026-10-10
The population-tracking identities in this document remain mathematically valid, but their interpretation as the controlling integrated-channel-yield admission criterion is superseded by:
M12_FRONTB_DE_CHANNEL_YIELD_IDENTITY_AND_CORRECTION_001_20261010
[PRIVATE_DRIVE_LOCATOR_REDACTED]
Material reason: NC audit established, and M12 independently generalized, an exact channel-yield identity showing that rapid source variation / epsilon_DE failure need not produce integrated yield error. Use this document only for POPULATION-TRACKING controls.
M12 — Front B dynamical-equilibrium admission: exact error identity
RESULT_CLASS
EXACT LOCAL CONTROL / SOURCE-DEPLETION CLOSURE / NO NUMERICAL ENDPOINT / NO NOVELTY CLAIM
TARGET
LT3 DRAFT016 Front B residual:
PBH_B2_TO_DE_ADMISSION.
SOURCE-NATIVE MODEL
For one hadron species or one scalar closure channel, consider:
dn/dt + Gamma(t) n(t) = S(t),
with Gamma(t)>0.
The dynamical-equilibrium approximation is:
n_DE(t)=S(t)/Gamma(t).
Define:
n_*(t)=S(t)/Gamma(t),
e(t)=n(t)-n_*(t).
CERTIFICATE A — EXACT ERROR EQUATION
Since:
n' = S-Gamma n
and:
S=Gamma n_*,
we obtain exactly:
e'(t)
=
-Gamma(t)e(t)
-
n_*'(t).
Thus the DE error is driven only by:
1. initial mismatch e(t0);
2. temporal motion of the instantaneous equilibrium n_*(t).
CERTIFICATE B — EXACT DUHAMEL REPRESENTATION
Let:
G(t,s)
=
exp[- integral_s^t Gamma(r)dr].
Then:
e(t)
=
G(t,t0)e(t0)
-
integral_{t0}^t G(t,s) n_*'(s) ds.
Therefore:
|e(t)|
<=
G(t,t0)|e(t0)|
+
integral_{t0}^t G(t,s)|n_*'(s)| ds.
BOXED
DE ERROR
=
DECAYED ENTRY MISMATCH
+
MEMORY-WEIGHTED MOTION OF THE QUASI-STEADY STATE.
This is exact.
CERTIFICATE C — UNIFORM LOWER-BOUND COROLLARY
If:
Gamma(t)>=gamma>0
on the target-relevant interval, then:
G(t,s)<=exp[-gamma(t-s)],
hence:
|e(t)|
<=
e^{-gamma(t-t0)}|e(t0)|
+
integral_{t0}^t e^{-gamma(t-s)} |n_*'(s)| ds.
In particular:
|e(t)|
<=
e^{-gamma(t-t0)}|e(t0)|
+
(1/gamma)
sup_{s in [t0,t]} |n_*'(s)|.
Thus one sufficient absolute DE condition is:
sup |n_*'| / gamma
small
relative to the required state tolerance.
CERTIFICATE D — RELATIVE SLOW-VARIATION FORM
Where n_*(t)>0, define:
a(t)
=
d ln n_*(t)/dt
=
d ln(S/Gamma)/dt.
Then:
|n_*'(t)|
=
|a(t)| n_*(t).
The common heuristic:
epsilon_DE(t)
=
|a(t)| / Gamma(t)
is therefore the local ratio:
equilibrium-motion timescale / depletion timescale.
But:
epsilon_DE<<1
alone is not a complete global certificate.
A global bound also requires:
- control of entry mismatch;
- lower bound on Gamma;
- control of n_* variation along the memory window;
- target-relevant interval.
Thus:
LOCAL TIMESCALE SEPARATION
!=
GLOBAL DE ERROR BOUND.
CERTIFICATE E — SHARP MEMORY-WINDOW INTERPRETATION
The kernel G(t,s) suppresses source-equilibrium motion at times s earlier than t by the accumulated depletion:
exp[- integral_s^t Gamma].
Therefore DE validity at target time t depends only strongly on the recent memory window with optical depth:
integral_s^t Gamma ~ O(1).
Fast depletion shortens the memory.
Rapid late source variation can still break DE even when earlier evolution was excellent.
This is directly relevant near terminal Hawking acceleration.
CERTIFICATE F — EXPANSION GUARD
In an expanding universe one often writes:
dn/dt + 3H n = S - Gamma_micro n.
This is exactly the same form with:
Gamma_eff
=
Gamma_micro + 3H
only if the dilution term is legitimately included in the same scalar linear closure.
But the physical DE approximation:
n_DE~S/Gamma_micro
requires:
Gamma_micro >> H
if expansion dilution is to be neglected.
Therefore:
Gamma_micro >> H
and
slow variation of S/Gamma_micro
are logically distinct admission checks.
CERTIFICATE G — MULTISPECIES VECTOR FORM
For vector hadron populations:
n'(t)=S(t)-A(t)n(t),
with instantaneous equilibrium:
n_*(t)=A(t)^{-1}S(t),
assuming A(t) invertible.
Then:
e'= -A(t)e - n_*'(t).
Let U(t,s) be the propagator solving:
dU/dt=-A(t)U,
U(s,s)=I.
Exactly:
e(t)
=
U(t,t0)e(t0)
-
integral_{t0}^t U(t,s)n_*'(s) ds.
Hence:
||e(t)||
<=
||U(t,t0)|| ||e(t0)||
+
integral ||U(t,s)|| ||n_*'(s)|| ds.
This is the correct generalization for coupled hadron closure.
A scalar Gamma test is insufficient if the actual closure is strongly coupled.
CERTIFICATE H — CONTRACTION CONDITION
If the propagator obeys:
||U(t,s)||
<=
C exp[-alpha(t-s)]
for alpha>0,
then:
||e(t)||
<=
C e^{-alpha(t-t0)}||e(t0)||
+
(C/alpha)
sup ||n_*'||.
Thus the load-bearing object is not merely individual decay rates but the stability/contraction rate alpha of the coupled closure.
CERTIFICATE I — FIXED-POINT INNER ITERATION GUARD
The Bianco-style dynamical-equilibrium procedure solves an inner state-coupled fixed point before rates are passed back to BBN.
Therefore there are TWO separate errors:
1. DE model error:
difference between true time-dependent hadron populations and instantaneous fixed point.
2. Inner-solver numerical error:
failure to converge to that instantaneous fixed point.
A small inner iteration tolerance certifies only (2).
It does NOT certify (1).
Thus:
FIXED-POINT CONVERGENCE
!=
DYNAMICAL-EQUILIBRIUM VALIDITY.
CERTIFICATE J — TARGET-WEIGHTED COMPOSITION
Let the DE population error induce weak-rate error through a map:
delta lambda(t)
=
L_t[e(t)]
or a nonlinear source-valid equivalent.
Then the previous M12 target-weighted certificate gives:
|Delta Y|
<=
target-sensitivity applied to delta lambda.
Therefore the complete Front-B validation chain is:
SOURCE-MATCHED Q_h(t)
->
DE ADMISSION / POPULATION ERROR CERTIFICATE
->
WEAK-RATE ERROR
->
TARGET-WEIGHTED ERROR CERTIFICATE
->
ONLY THEN endpoint.
This is a compositional validation chain.
PROSPECTIVE PBH ADMISSION RULE
Before accepting DE in PBH/B2:
1. freeze source-matched Q_h(t);
2. define the actual coupled hadron state and A(t) or legal nonlinear analogue;
3. bound propagator stability/contraction;
4. bound entry mismatch;
5. bound motion of n_*(t);
6. explicitly stress the terminal-Hawking interval;
7. map population error to weak-rate error;
8. propagate to Yp/D-H target tolerance.
A local heuristic epsilon_DE may be used as screening,
but not as the final error certificate.
LOWER-HOST SUBTRACTION
HOST_RELATION = EXACT_INSTANCE of variation-of-constants / singular-perturbation / quasi-steady-state error calculus.
PROJECT_ROLE = LOCAL_THEOREM / SOURCE-NATIVE ADMISSION RULE.
No novelty claim.
FIREWALL
INNER FIXED-POINT TOLERANCE != PHYSICAL DE ERROR.
Gamma>>H != SLOW SOURCE VARIATION.
epsilon_DE<<1 != GLOBAL TARGET ERROR BOUND.
SCALAR DE TEST != COUPLED MULTISPECIES CERTIFICATE.
GOOD DECAY-RELIC DE VALIDATION != PBH TERMINAL-SOURCE VALIDATION.
DE ADMISSION != PBH ENDPOINT RELEASE.
STATUS
PBH_B2_TO_DE_ADMISSION = FORMALIZED AS ERROR IDENTITY / STILL SOURCE-VALIDATION OPEN.
TARGET_WEIGHTED_ERROR_CERTIFICATE = AVAILABLE.
SOURCE_MATCHED_FULL COMPARATOR = OPEN.
SOURCE_MATCHED_K_PBH = UNDEFINED.
NO NUMERICAL ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY INFERENCE.
