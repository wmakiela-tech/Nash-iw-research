# M12 — Profiled behavior-set ambiguity gate

RETURN_ID: M12-DRAFT009-PROFILED-BEHAVIOR-SET-CONFUSABILITY-GATE-001

RESULT_CLASS: EXACT_HOST_THEOREM / DRAFT009 REPAIR / NO NOVELTY CLAIM

## Trigger

DRAFT009 §4 defines nuisance-profiled behavior sets

B(theta) = {F(theta,eta): eta legal}

and then uses equality B(theta)=B(theta') as contextual equivalence.

Equality of possible-behavior sets is a valid equivalence relation, but it is too strong to represent ordinary nuisance-mediated observational ambiguity from one realized output.

## Exact counterexample

Let

B(a)={0,1},
B(b)={1,2}.

Then

B(a) != B(b),

yet observation y=1 is compatible with both a and b.

So behavior-set inequality does NOT imply observational distinguishability.

## Correct feasible-fiber object

For a realized observation y define

Theta_y = {theta : y in B(theta)}.

A target tau is identifiable from the observation model for every legal y iff

tau is constant on every Theta_y.

Equivalently:

if B(theta) intersects B(theta') nontrivially,
then
tau(theta)=tau(theta').

This is the exact target-identifiability condition under nuisance profiling.

## Full parameter identifiability

Modulo declared redundancy ~R, full identification requires:

B(theta) intersects B(theta') nontrivially
=> theta ~R theta'.

Thus disjointness of possible-behavior sets, not inequality of sets, is the relevant exact separator.

## Overlap is not an equivalence relation

Define confusability

theta C theta'
iff
B(theta) intersects B(theta').

C is reflexive and symmetric but generally not transitive.

Control:
B(a)={0},
B(b)={0,1},
B(c)={1}.

Then a C b and b C c, but a not C c.

Therefore one cannot form an ordinary observational quotient directly from pairwise overlap without changing the claim.

The safe object is the family of feasible fibers Theta_y, or equivalently the confusability hypergraph/graph.

## Relation to behavior-set equality

Equality of behavior sets means two candidates generate exactly the same set-valued observation model.

This is a stronger MODEL-EQUIVALENCE notion.

It may be useful, but it must not be called the generic observational indistinguishability relation when nuisance can be refit separately.

Thus separate:

SET-VALUED MODEL EQUALITY:
B(theta)=B(theta').

OBSERVATIONAL CONFUSABILITY:
B(theta) intersects B(theta') nontrivially.

TARGET IDENTIFIABILITY:
tau constant on every feasible observation fiber Theta_y.

## Multi-context independent nuisance

For observed tuple y=(y_c), with independent context-local nuisance,

Theta_y = intersection_c {theta : y_c in B_c(theta)}.

Target identifiability requires tau constant on every such joint feasible set.

If nuisance/completion variables are shared or coupled, this factorized intersection is not enough; use DRAFT009 joint legal behavior J_C and shared-witness legality first.

## DRAFT009 repair

Section 4 should not use behavior-set equality as the sole generic context indistinguishability notion.

Recommended fields:

BEHAVIOR_SET_MODEL_EQUIVALENCE;
OBSERVATIONAL_CONFUSABILITY;
OBSERVATION_FEASIBLE_FIBER;
TARGET_IDENTIFIABILITY;
NUISANCE_SHARING_SEMANTICS.

## Firewall

UNEQUAL POSSIBLE-BEHAVIOR SETS != OBSERVATIONALLY DISTINGUISHABLE.

OVERLAP CONFUSABILITY != EQUIVALENCE RELATION.

SET-VALUED MODEL EQUALITY != TARGET IDENTIFIABILITY.

PROFILE-FIRST INDEPENDENT-NUISANCE LOGIC != SHARED-WITNESS JOINT LEGALITY.

HOST_RELATION=EXACT_INSTANCE of set-valued inverse problems / nuisance-profiled identifiability.
PROJECT_ROLE=DRAFT009 TYPING REPAIR.

REV020 active.
REV021 not created.
TPE thin compiler / HOLD.
NO CANON / NO EXEC_SIGN / NO NOVELTY.
