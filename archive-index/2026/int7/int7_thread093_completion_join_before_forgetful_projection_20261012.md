# INT7 Thread093 — completion shared-witness join before forgetful projection

RETURN_ID: INT7-THREAD093-COMPLETION-SHARED-WITNESS-JOIN-BEFORE-FORGETFUL-PROJECTION-001
DATE: 2026-10-12

## Setup

Let Omega_plus be one legally completed carrier.
Let p:Omega_plus->Omega be the forgetful/completion projection.
Let A_c^+ subset Omega_plus be the legal feasible set in context c.

True joint completed feasibility:
A_joint^+ = intersection_c A_c^+.

Its old-carrier shadow is:
p(A_joint^+).

Tempting shortcut:
intersection_c p(A_c^+).

## Exact theorem

Always:
p(intersection_c A_c^+)
is a subset of
intersection_c p(A_c^+).

Equality holds iff every old-carrier value omega that survives each context separately has at least one COMMON completion u such that:
p(u)=omega
and
u belongs to every A_c^+.

Equivalently, for each omega in intersection_c p(A_c^+), the completion fibers

F_c(omega)=A_c^+ intersect p^{-1}(omega)

must have nonempty total intersection.

## Minimal exact counterexample

Let Omega_plus contain two distinct completions u_a,u_b with:
p(u_a)=p(u_b)=omega_0.

Take:
A_1^+={u_a},
A_2^+={u_b}.

Then:
p(A_1^+)=p(A_2^+)={omega_0},

so:
intersection_c p(A_c^+)={omega_0}.

But:
A_1^+ intersect A_2^+ is empty,

hence:
p(A_1^+ intersect A_2^+) is empty.

Therefore the reduced/old carrier reports apparent compatibility at omega_0 even though NO one shared completed realization exists.

## Scientific consequence

FORGETTING COMPLETION BEFORE GLOBAL JOIN
can erase cross-context incompatibility.

Correct order when the scientific claim requires one shared completed realization:

1. restrict to one legal completed carrier;
2. transport all context constraints there;
3. perform shared-witness intersection/join;
4. only then apply p if an old-carrier shadow is needed;
5. only then push forward to target.

Thus:

JOIN FIRST, FORGET SECOND.

## Relation to completion reopening

M12/Rec9 completion reopening says:
if a completed target varies inside a legal p-fiber and the inherited full observation law factors through p, inherited observations cannot identify that target.

Thread093 is different:
even when the target DESCENDS through p, contextwise projection through p can still create false joint compatibility because different contexts may require incompatible completions over the same old state.

Therefore:

TARGET DESCENT
does not imply
COMPLETION-WITNESS COMPATIBILITY.

No target-induced information reopening may occur, yet a shared-realization claim may still require completion-level joining.

## Target version

Let tau_plus = tau o p.

Then:
tau_plus(intersection_c A_c^+)
is a subset of
tau(intersection_c p(A_c^+)),

and strict inclusion can occur.

So even an old target value that is separately compatible in every projected context may have no one shared completed witness.

This is not target nonidentification by itself; it is a shared-realization legality failure.

## Partial shared-component reading

If only a component z=s(u) must be shared, replace p by the declared component map s.

The same theorem applies:
s(intersection A_c^+) subseteq intersection s(A_c^+).

Hence the required join level must match the actual claim:
FULL_SHARED_OBJECT,
SHARED_COMPONENT,
TRANSPORTABLE_QUERY,
or no legal bridge.

Do not demand full completion identity when only a legally declared component must be shared.

## Firewalls

PROJECTED CONTEXT COMPATIBILITY != SHARED COMPLETION.
SAME OLD STATE != SAME COMPLETED REALIZATION.
TARGET DESCENT != SHARED-COMPLETION COMPATIBILITY.
NO TARGET-INDUCED REOPENING != NO CROSS-CONTEXT COMPLETION OBLIGATION.
FORGET-THEN-JOIN != JOIN-THEN-FORGET in general.
FULL COMPLETION SHARING != SHARED-COMPONENT SHARING automatically.

## Compiler rule

Add:

COMPLETION_JOIN_LEVEL =
FULL_COMPLETION | SHARED_COMPONENT | TARGET_ONLY | TRANSPORTABLE_QUERY | UNRESOLVED

FORGETFUL_PROJECTION_ORDER =
JOIN_THEN_FORGET | FORGET_THEN_JOIN_UNSAFE | EQUALITY_CERTIFIED

Equality certificate:
for every surviving projected value, completion-fiber intersection is nonempty.

## Verdict

THREAD093_VERDICT =
COMPLETION_JOIN_BEFORE_FORGETFUL_PROJECTION_PASS /
PROJECTED_COMPATIBILITY_CAN_HIDE_COMPLETION_CONFLICT /
TARGET_DESCENT_DOES_NOT_REPAIR_SHARED_WITNESS_LOSS /
CLAIM_RELATIVE_JOIN_LEVEL_REQUIRED /
MATURE_IMAGE_INTERSECTION_MATHEMATICS /
NO_NEW_GENERAL_THEORY.

REV020 ACTIVE / TPE HOLD / REV021 NOT_CREATED / NO NOVELTY / NO CANON / NO EXEC_SIGN / NO NEW TASK.
