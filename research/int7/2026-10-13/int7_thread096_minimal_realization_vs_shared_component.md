# INT7 Thread096 — Minimal realization equivalence versus shared-component legality

RETURN_ID: INT7-THREAD096-MINIMAL-REALIZATION-EQUIVALENCE-VS-SHARED-COMPONENT-LEGALITY-001
DATE: 2026-10-13
BW_STATUS: ING-20261013-0001 / CURRENT_REPRESENTED_SOURCE_ONLY
EXPOSURE: PUBLIC
BW_INGESTION_EVENT: ING-20261013-0001
CLASS: EXACT REALIZATION-THEORY / CROSS-CONTEXT INTEGRATION
STATUS: REV020 ACTIVE / TPE HOLD / REV021 NOT_CREATED / NO NOVELTY CLAIM

## 1. Setup

Consider two finite-dimensional minimal realizations of the same transfer function

Sigma(z)=B_1(zI-D_1)^(-1)C_1
       =B_2(zI-D_2)^(-1)C_2.

Classical realization theory gives an invertible similarity T:Y_1->Y_2 such that

D_2 T = T D_1,
C_2 = T C_1,
B_2 T = B_1.

Thus the two realizations are response-equivalent.

Let s_i:Y_i->Z be the source-native maps extracting the scientific component claimed to be shared across the two contexts.

## 2. Exact shared-component criterion

The realization equivalence induces a legal shared-component identification through T iff

s_2 T = s_1

on the legally reachable subspace relevant to the claim.

If the claim ranges over the full minimal realization, the condition is simply

s_2 T = s_1 on Y_1.

Proof:
A state y in realization 1 corresponds to Ty in realization 2 under the response-preserving similarity. The two contexts assign the same declared component exactly when

s_1(y)=s_2(Ty)

for every legally relevant y.

Therefore:

SAME TRANSFER FUNCTION
+
MINIMALITY
+
SIMILARITY

DOES NOT BY ITSELF imply

SHARED COMPONENT.

A component must descend through the similarity relation.

## 3. Minimal exact counterexample

Let

D_1=D_2=-1,
C_1=1,
B_1=1.

Choose similarity T=2. Then an equivalent minimal realization is

D_2=-1,
C_2=2,
B_2=1/2.

Both realize

Sigma(z)=1/(z+1).

Take the naive coordinate readouts

s_1(y)=y,
s_2(y)=y.

Then

s_2(Ty)=2y != y=s_1(y)

for y!=0.

So the realizations have identical input-output response and are classically similar, but the raw internal coordinate is NOT one shared component.

If instead

s_2(y)=y/2,

then

s_2(Ty)=y=s_1(y),

and the component is legally transported.

Hence:

COORDINATE EQUALITY != COMPONENT IDENTITY.
SIMILARITY EQUIVALENCE != SHARED-COMPONENT EQUIVALENCE.

## 4. Fiber-product placement

Thread094 says a shared-component claim is represented by the fiber product

P_Z={(y_1,y_2): s_1(y_1)=s_2(y_2)}.

Realization theory supplies a distinguished response-equivalence graph

G_T={(y,Ty): y in Y_1}.

The two contexts possess a shared component along the realization equivalence iff

G_T subseteq P_Z,

equivalently iff

s_2 T=s_1.

This is the exact bridge between classical minimal-realization equivalence and claim-relative shared-component legality.

## 5. Target-only corollary

Let target maps be tau_i:Y_i->Q.

Even if s_2 T != s_1, target transport can still hold when

tau_2 T = tau_1.

Therefore:

SHARED COMPONENT FAILURE
!=
TARGET-ONLY TRANSPORT FAILURE.

Conversely, equal transfer functions do not guarantee target equality for arbitrary internal targets; the target must itself be invariant/transported under the similarity.

## 6. Full-shared-object ceiling

Similarity T is an isomorphism between realizations, not literal identity of full carriers.

Thus even when

s_2 T=s_1,

one may conclude shared-component compatibility, not one identical full hidden realization.

FULL SHARED OBJECT requires a stronger source-native identification than realization equivalence.

## 7. Monograph consequence

The SW minimal-realization theorem and Thread094 should be connected by one explicit bridge lemma:

minimal response realizations are unique only up to similarity;
scientific components are meaningful across realizations only if their extraction maps are similarity-compatible.

This prevents a common category error:

UNIQUENESS UP TO SIMILARITY
!=
UNIQUENESS OF PHYSICAL INTERNAL VARIABLES.

## 8. Firewalls

MINIMAL REALIZATION UNIQUENESS != PHYSICAL STATE UNIQUENESS.
SIMILARITY != LITERAL STATE IDENTITY.
SAME TRANSFER FUNCTION != SAME INTERNAL COMPONENT.
SHARED COMPONENT REQUIRES s_2 T=s_1.
SHARED COMPONENT != FULL SHARED OBJECT.
SHARED COMPONENT FAILURE != TARGET-ONLY FAILURE.
TARGET TRANSPORT REQUIRES tau_2 T=tau_1, not raw coordinate equality.

## 9. Verdict

THREAD096_VERDICT =
MINIMAL_REALIZATION_TO_SHARED_COMPONENT_BRIDGE_PASS /
SIMILARITY_COMPATIBILITY_CONDITION_s2T_EQ_s1_PASS /
RAW_COORDINATE_SHAREDNESS_COUNTEREXAMPLE_PASS /
THREAD094_FIBER_PRODUCT_LINK_PASS /
TARGET_ONLY_LEVEL_REMAINS_DISTINCT /
NO_NEW_GENERAL_THEORY.

NO CANON / NO EXEC_SIGN / NO NOVELTY INFERENCE / NO PHYSICAL ONTOLOGY CLAIM / NO NEW TASK.
