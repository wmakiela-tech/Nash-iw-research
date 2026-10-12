---
artifact_id: M12-CAUSAL-ABSTRACTION-INTERVENTION-MAP-UNIQUENESS-GATE-001
bw_ingestion_event_id: ING-20261010-0077
bw_qualification_state: CAUSAL_INTERVENTION_MAP_UNIQUENESS
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# M12-CAUSAL-ABSTRACTION-INTERVENTION-MAP-UNIQUENESS-GATE-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

M12 - causal abstraction intervention-map uniqueness gate
RESULT_CLASS
EXACT CAUSAL-ABSTRACTION CONTROL / FAITHFUL-REDUCTION HARDENING / NO NOVELTY CLAIM
TRIGGER
Current XH/LT3:
causal abstraction requires state map tau, legal intervention families, an intervention map omega, and interventional commutation.
Missing exact point:
when is the induced high-level intervention uniquely determined?
SETUP
Let:
X = low-level state space,
Z = high-level state space,
tau:X->Z = abstraction map.
Let:
i:X->X
be one legal low-level intervention.
A high-level intervention j:Z->Z is compatible if:
tau o i
=
j o tau.
CERTIFICATE A - EXISTENCE
Such j exists on im(tau) iff:
tau(x)=tau(x')
=>
tau(i(x))=tau(i(x')).
Equivalently:
tau o i is constant on tau-fibers.
This is the exact intervention-descent criterion.
CERTIFICATE B - UNIQUENESS UNDER SURJECTIVITY
If tau is surjective onto the declared high-level state space Z and compatible j exists, then j is unique.
Proof:
for every z in Z choose x with tau(x)=z.
Then:
j(z)=tau(i(x)),
and fiber constancy guarantees well-definedness.
Therefore:
SURJECTIVE STATE ABSTRACTION
+
INTERVENTION DESCENT
=>
UNIQUE INDUCED HIGH-LEVEL STATE TRANSFORMATION.
CERTIFICATE C - NONUNIQUENESS OFF THE REACHABLE IMAGE
If tau is not surjective, compatibility determines j only on:
Z_reach = im(tau).
Outside Z_reach, j can be extended arbitrarily unless additional semantics constrain it.
Therefore multiple high-level interventions may satisfy the same commuting diagram on every low-level state.
Exact example:
X={a,b},
Z={0,1,2},
tau(a)=0,
tau(b)=1.
Take low intervention i=id_X.
Then induced map on reachable image must satisfy:
j(0)=0,
j(1)=1.
But both:
j_1:
0->0, 1->1, 2->2
and
j_2:
0->0, 1->1, 2->0
commute with tau on all low states.
They disagree only on unreachable high state 2.
Thus:
COMMUTATION ON CURRENT LOW MODEL
!=
FULL HIGH-LEVEL INTERVENTION IDENTIFICATION.
CERTIFICATE D - COMPLETION-INDUCED REOPENING
Suppose a later theory completion enlarges the low model so that abstract state z=2 becomes reachable.
Then the earlier intervention-map ambiguity becomes scientifically load-bearing.
What was previously an arbitrary extension now changes predictions on newly admitted states.
Therefore:
INTERVENTION MAP COMPLETENESS
is relative to the reachable abstract image of the current theory/model class.
A theory completion can reopen causal-abstraction obligations even when the old commuting diagram was exact.
CERTIFICATE E - HIGH-LEVEL INTERVENTION FAMILY RESTRICTION
Even if a unique mathematical induced state transformation exists, it may fail causal abstraction if that transformation is not a legal member of the declared high-level intervention family I_H.
Thus two gates are distinct:
1. DESCENT / MATHEMATICAL INDUCIBILITY:
does tau o i factor through tau?
2. INTERVENTION ADMISSION:
is the induced j legal in I_H with correct semantics?
MATHEMATICAL DESCENT
!=
PHYSICAL/CAUSAL INTERVENTION ADMISSION.
CERTIFICATE F - FAMILY MAP
For a low-level intervention family I_L, a causal abstraction map:
omega:I_L->I_H
can exist only if every admitted i in I_L descends and its induced high transformation is represented by an admitted high intervention.
If tau is surjective and the high intervention representation is extensional by state transformation, omega is unique pointwise.
If different high intervention labels implement the same state transformation but differ in mechanism/cost/resource semantics, state-level commutation does not identify intervention semantics.
Therefore:
INTERVENTION ACTION EQUALITY
!=
INTERVENTION SEMANTIC IDENTITY.
CERTIFICATE G - FAILURE EXAMPLE
Let:
X={a,b,c,d},
Z={0,1},
tau(a)=tau(b)=0,
tau(c)=tau(d)=1.
Define low intervention i by:
i(a)=c,
i(b)=b,
i(c)=c,
i(d)=d.
Then:
tau(a)=tau(b)=0,
but:
tau(i(a))=1,
tau(i(b))=0.
So tau o i is not constant on the tau-fiber {a,b}.
No high-level j:Z->Z can satisfy:
tau o i = j o tau.
Thus a reduction can be perfectly meaningful for passive state description while failing intervention descent exactly.
PASSIVE ABSTRACTION
!=
CAUSAL ABSTRACTION.
CERTIFICATE H - APPROXIMATE VERSION
If exact commutation fails but one wants an approximate causal abstraction, the claim must specify:
- metric/loss on high states or output laws;
- intervention family;
- reachable abstract domain;
- approximation tolerance;
- whether the tolerance is uniform over interventions.
Small passive error does not bound intervention error automatically.
CERTIFICATE I - POLICY / SEQUENTIAL GUARD
For sequential interventions, pointwise one-step descent is insufficient if future intervention legality depends on hidden history erased by tau.
Then the relevant object is a policy/history abstraction, not only a state transformation.
Thus:
ONE-STEP INTERVENTION DESCENT
!=
SEQUENTIAL POLICY DESCENT.
DRAFT010/011 PATCH
Record:
ABSTRACTION_STATE_MAP
ABSTRACT_REACHABLE_IMAGE
LOW_INTERVENTION_FAMILY
HIGH_INTERVENTION_FAMILY
INTERVENTION_DESCENT_STATUS
INDUCED_ACTION_UNIQUENESS={UNIQUE_ON_REACHABLE_IMAGE, UNIQUE_GLOBAL, NONUNIQUE_EXTENSION, FAIL}
INTERVENTION_ADMISSION_STATUS
INTERVENTION_SEMANTICS_STATUS
COMPLETION_REOPENING_RISK
SEQUENTIAL_POLICY_DESCENT
CLAIM_CEILING.
PROSPECTIVE FALSIFIER
Before claiming causal faithfulness:
1. freeze tau and legal intervention family;
2. find two low states in one tau-fiber;
3. apply each intervention;
4. compare abstract post-intervention states.
If any pair splits:
causal intervention descent fails immediately.
If all pass but tau is nonsurjective:
claim only uniqueness on im(tau), not global intervention semantics.
LOWER HOST
Causal abstraction / factor maps / quotient dynamics.
PROJECT ROLE
FAITHFULNESS_PROFILE COMPILER RULE.
FIREWALL
STATE ABSTRACTION != CAUSAL ABSTRACTION.
COMMUTING ON REACHABLE IMAGE != GLOBAL INTERVENTION IDENTIFICATION.
UNIQUE MATHEMATICAL ACTION != LEGAL PHYSICAL INTERVENTION.
PASSIVE EQUIVALENCE != INTERVENTIONAL EQUIVALENCE.
ONE-STEP DESCENT != POLICY DESCENT.
STATUS
Exact intervention-map uniqueness gate PASS.
No new physical result.
No CANON / NO EXEC_SIGN / NO NOVELTY.
