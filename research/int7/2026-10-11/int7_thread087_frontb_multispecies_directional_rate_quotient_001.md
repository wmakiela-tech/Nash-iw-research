---
artifact_id: INT7-THREAD087-FRONTB-MULTISPECIES-DIRECTIONAL-RATE-QUOTIENT-001
bw_ingestion_event_id: ING-20261011-0012
bw_qualification_state: FRONTB_MULTISPECIES_RATE_QUOTIENT
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: GITHUB_PENDING_BW_LINK_UPDATE
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# INT7-THREAD087-FRONTB-MULTISPECIES-DIRECTIONAL-RATE-QUOTIENT-001

> Public-safe mirror of the BW-linked Drive source. BW controls lifecycle/currentness; this GitHub body does not upgrade scientific authority.

INT7 Thread087 — Front B multispecies directional-rate quotient and closure boundary
RETURN_ID: INT7-THREAD087-FRONTB-MULTISPECIES-DIRECTIONAL-RATE-QUOTIENT-001
FROM_CELL: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_07 / INT7
DATE: 2026-10-11
STATUS: REV020 ACTIVE / TPE HOLD / REV021 NOT_CREATED / NOVELTY NONE
1. Trigger
DRAFT017 correctly marks multi-species feedback as load-bearing.
XH-S3 also notes that multiple hadrons can compensate in X_n^qs while adding constructively in waterfall strength.
Thread087 asks a narrower exact question:
does multiple species by itself destroy the reduced waterfall descriptor for the neutron-fraction dynamics?
Answer:
no, not at replay level.
2. Multispecies aggregation
Let species s contribute effective directional rates
a_s(t)=Gamma_{s,p->n}(t)
b_s(t)=Gamma_{s,n->p}(t).
Define aggregate hadronic rates
A(t)=sum_s a_s(t)
B(t)=sum_s b_s(t).
Then
R_h=A+B
and, whenever R_h>0,
X_n^qs=A/(A+B).
Hence exactly:
A=R_h X_n^qs
B=R_h(1-X_n^qs).
This is independent of how many species produced A and B.
3. Exact quotient theorem for reduced n/p replay
Let q map the full species-resolved rate vector
q({a_s,b_s}_s)=(A,B).
For the reduced neutron-fraction ODE,
dX_n/dt
=
(a_w+A)(1-X_n)
-
(b_w+B)X_n,
the vector field depends on the species-resolved state only through q.
Therefore every two species histories with the same aggregate pair (A,B) induce exactly the same reduced X_n trajectory for the same weak-rate history and initial condition.
Equivalently:
the reduced n/p dynamics factors exactly through the quotient q.
Thus:
MULTISPECIES COMPOSITION DETAIL
is in the replay kernel
whenever all hadronic influence on X_n enters only through the two aggregate directional rates.
4. Descriptor form
Since (A,B) and (X_n^qs,R_h) are bijectively related for R_h>0,
{X_n^qs,R_h}
is an exact sufficient representation of the multispecies aggregate rate history for reduced n/p replay.
If R_h/R_weak is used instead, denominator legality from Thread086 remains required.
5. What multi-species feedback actually breaks
State-dependent species populations may make
A=A(state,source,background)
B=B(state,source,background).
This does NOT break replay sufficiency once A(t),B(t) are known.
It breaks GENERATIVE CLOSURE if the reduced descriptor does not specify how A and B change when the source/state/background changes.
Therefore:
MULTISPECIES FEEDBACK
!=
FAILURE OF AGGREGATE REPLAY QUOTIENT.
It means:
the map from source/state to the descriptor is itself a load-bearing closure object.
6. Exact composition nonidentifiability
Different species decompositions can satisfy
sum_s a_s = A,
sum_s b_s = B
while having different individual a_s,b_s.
No reduced n/p observation can distinguish those decompositions if all other channels are excluded.
Thus:
N/P REPLAY IDENTIFICATION
!=
SPECIES-COMPOSITION IDENTIFICATION.
The composition fiber can remain large while the neutron trajectory is exactly fixed.
7. When the quotient becomes illegal
The quotient q is not scientifically sufficient when species identity affects the declared claim outside the two aggregate p<->n rates, for example through:
- hadrodissociation;
- energy-dependent secondary production;
- entropy/background modification;
- species-specific decay products;
- additional nuclear channels;
- another detector/target sensitive to composition;
- source-family response where future A,B cannot be predicted from the reduced state.
Then the target or process does not descend through q.
8. Relation to DRAFT017 multi-species gate
Repair the wording:
Too strong:
"multi-species composition prevents the waterfall descriptor from extending."
Sharper:
"multi-species composition still admits an exact aggregate directional-rate quotient for reduced n/p replay, but source-family closure and broader BBN targets may require the species-resolved state."
So retain:
BRANCHING_STATE_DEPENDENT = LOAD_BEARING
but distinguish:
A. AGGREGATE REPLAY SUFFICIENCY — can PASS exactly;
B. GENERATIVE SOURCE-FAMILY CLOSURE — OPEN;
C. FULL TARGET SUFFICIENCY — OPEN.
9. Cheapest validation
For a frozen source:
1. compute species-resolved a_s,b_s;
2. aggregate A,B;
3. construct X_n^qs,R_h;
4. replay X_n using only aggregate descriptor;
5. verify exact/numerical agreement with the same effective-rate system;
6. perturb source/state and test whether the reduced closure predicts the new A,B;
7. only then test Y_p/D/H.
10. Spider connection
Thread086:
trajectory descriptor != constitutive law.
Thread087:
species detail can quotient exactly for one reduced process while still being required to generate the descriptor off trajectory.
This is another instance of:
FULL STATE
-> TARGET/PROCESS-SUFFICIENT QUOTIENT
-> GENERATIVE CLOSURE TEST
-> TARGET DESCENT.
11. Firewalls
MULTISPECIES != AUTOMATIC DESCRIPTOR FAILURE.
SAME AGGREGATE RATES != SAME SPECIES COMPOSITION.
N/P REPLAY SUFFICIENCY != SPECIES IDENTIFICATION.
REPLAY QUOTIENT != SOURCE-FAMILY CLOSURE.
SOURCE-FAMILY CLOSURE != FULL BBN TARGET SUFFICIENCY.
COMPOSITION DETAIL MAY BE IRRELEVANT TO X_n AND LOAD-BEARING FOR ANOTHER TARGET.
12. Verdict
THREAD087_VERDICT =
MULTISPECIES_DIRECTIONAL_RATE_QUOTIENT_PASS /
WATERFALL_DESCRIPTOR_EXTENDS_TO_AGGREGATE_NP_REPLAY /
MULTISPECIES_FEEDBACK_RELOCATED_TO_GENERATIVE_CLOSURE /
SPECIES_COMPOSITION_REMAINS_NONIDENTIFIED /
FULL_TARGET_VALIDATION_OPEN.
No PBH bound / no endpoint release / no CANON / no EXEC_SIGN / no novelty / no new front.
