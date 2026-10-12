---
artifact_id: M12-LT3-SHARED-NUISANCE-INFORMATION-GATE-001
bw_ingestion_event_id: ING-20261012-0009
bw_qualification_state: SHARED_NUISANCE_INFORMATION_GATE
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SYNCED
source_surface: GOOGLE_DRIVE
source_revision: AHj4eMTximizscr0CsFQIzHGX3IAFuhIVA6deekBbktpz3IAB-BPAnJqcDCjCcSXqbdiP8cIxC1GbFe_7syJvForFcp_TzzyIL_6wsWk9Uo
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# M12-LT3-SHARED-NUISANCE-INFORMATION-GATE-001

> Public-safe mirror of the BW-linked Drive source. BW controls lifecycle/currentness; this GitHub body does not upgrade scientific authority. Private provider locators were redacted during mirroring.

M12 - LT3 shared nuisance: exact information gate
RESULT_CLASS
EXACT LOCAL CONTROL / MULTI-CONTEXT IDENTIFIABILITY / MATURE-HOST SUBTRACTION / NO NOVELTY CLAIM
TRIGGER
Current LT3 compiler requires nuisance profiling before claiming cross-context information gain.
The load-bearing question is whether nuisance is truly independent across contexts or shared.
SETUP
Linearized joint model:
y = J_theta v + J_eta w.
A shared-parameter direction v is locally unidentifiable modulo nuisance iff:
J_theta v in Ran(J_eta).
Equivalently:
P_(Ran J_eta)^perp J_theta v = 0.
CERTIFICATE A - SHARED VS INDEPENDENT NUISANCE MONOTONICITY
Let N_shared and N_indep be two nuisance models with:
Ran(J_eta_shared)
subseteq
Ran(J_eta_indep).
This is the situation when one physically shared nuisance is incorrectly duplicated into independent context nuisances.
Then:
ker(P_shared J_theta)
subseteq
ker(P_indep J_theta).
Therefore allowing extra independent nuisance freedom can only preserve or DESTROY shared-parameter information.
It cannot create genuine new information.
So:
TREATING A SHARED NUISANCE AS INDEPENDENT
CAN CREATE FALSE NONIDENTIFIABILITY.
Conversely, forcing actually independent nuisances to be shared can create false identifiability.
CERTIFICATE B - EXACT TWO-CONTEXT SEPARATOR
Take one shared parameter theta and one shared nuisance eta:
y1 = theta + eta,
y2 = theta - eta.
Joint Jacobians:
J_theta = (1,1)^T,
J_eta_shared = (1,-1)^T.
These directions are linearly independent.
Hence theta is locally identifiable jointly.
Indeed:
theta = (y1+y2)/2,
eta = (y1-y2)/2.
But each context alone is completely confounded.
Now incorrectly replace the shared eta by independent eta1,eta2:
y1 = theta + eta1,
y2 = theta - eta2.
Then nuisance Jacobian spans all R^2.
Therefore:
P_(Ran J_eta_indep)^perp J_theta = 0.
Theta becomes structurally unidentifiable.
Thus the SAME two measurement equations support opposite identifiability conclusions depending only on nuisance-sharing semantics.
BOXED
NUISANCE SHARING TOPOLOGY
IS PART OF THE SCIENTIFIC MODEL,
NOT A TECHNICAL DETAIL.
CERTIFICATE C - TARGET VERSION
For target tau(theta) with differential L=D tau,
the target is locally identifiable modulo nuisance iff:
J_theta v in Ran(J_eta)
=>
L v = 0.
Thus full theta may remain unidentifiable while a target is identifiable.
CERTIFICATE D - INFORMATION MATRIX FORM
Under a regular Gaussian/least-squares metric with covariance W^-1,
profiled information for theta is the Schur-complement form:
I_eff
=
J_theta^T W J_theta
-
J_theta^T W J_eta
(J_eta^T W J_eta)^dagger
J_eta^T W J_theta,
with the usual range/regularity guards.
Changing nuisance-sharing structure changes J_eta and therefore changes I_eff even when raw J_theta and raw observations are unchanged.
Hence:
RAW STACKED INFORMATION
!=
SHARED-PARAMETER INFORMATION.
CERTIFICATE E - CROSS-CONTEXT GAIN CRITERION
A new context adds first-order information about shared theta exactly when it removes at least one v from the nuisance-profiled blind space.
Equivalently, after stacking the new context:
ker(J_eff,new)
is a strict subset of
ker(J_eff,old).
This is a claim-local statement.
Rank increase in raw stacked Jacobian is insufficient.
PROJECT READINGS
Calibration:
shared gain/offset across sensors can be identified jointly even when each sensor alone is confounded.
Front B:
a nuisance or completion variable may be shared across endpoints/times rather than freely refit at each endpoint; independent refits can erase real cross-endpoint constraints.
Multi-environment inference:
environment-specific nuisance and invariant mechanism parameters must be separated before interpreting context gain.
LOWER-HOST SUBTRACTION
HOST_RELATION = EXACT_INSTANCE of linear inverse problems / nuisance profiling / Schur complement / observability.
PROJECT_ROLE = source-legality + compiler rule.
No new mathematics or theory.
FIREWALL
MORE CONTEXTS != MORE SHARED-PARAMETER INFORMATION.
RAW RANK GAIN != PROFILED INFORMATION GAIN.
SHARED NUISANCE != INDEPENDENT NUISANCES.
SEPARATE REFITS != JOINT IDENTIFIABILITY.
TARGET IDENTIFIABILITY != FULL PARAMETER IDENTIFIABILITY.
DISPOSITION
KEEP nuisance-sharing semantics as a mandatory source-native field.
ABSORB theorem in mature linear/statistical hosts.
SCIENTIFIC_SURPLUS = NONE demonstrated.
REV020 active / REV021 not created.
NO CANON / NO EXEC_SIGN / NO NOVELTY / SCIENCE_FIRST.
