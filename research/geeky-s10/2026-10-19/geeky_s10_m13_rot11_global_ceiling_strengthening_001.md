# Geeky-S10 — M13 ROT11 global-ceiling strengthening

RETURN_ID: GEEKY-S10-M13-ROT11-GLOBAL-CEILING-STRENGTHENING-001
DATE: 2026-10-19
STATUS: EXACT MATHEMATICAL SYNTHESIS / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY

M13 ROT11 gives a correct one-shot proof that mu_2(G)>0 violates the sharp bound 1/gamma in the unrestricted co-axial model. It leaves open whether some larger finite protocol-independent bound might still exist.

That stronger question is closed by the repeated-reset argument below.

Let H=(G+G^T)/2 and assume mu_2(G)>0. Choose unit x with x^T H x>0. For sufficiently small tau>0, with S=exp(G tau),

lambda=x^T Sx>1.

Write

Sx=lambda x+r,
with r perpendicular x.

## Case 1: r != 0

Choose the co-axial sensor direction

e=r/||r||.

In the projective-reset limit Q0=I-ee^T,

Q0 Sx=lambda x.

Hence N repeated free-flow/reset cycles give post-reset states lambda^N x, and the j-th pre-reset readout amplitude equals

lambda^(j-1)||r||.

Therefore finite prefixes have arbitrarily large l2 norm and arbitrarily large l-infinity norm as N increases.

Projective reset corresponds to u=0, while legal finite-strength measurements have u>0. For every fixed finite N, all N-step states and outputs depend continuously on u. Thus for every prescribed finite bound B, choose N so the u=0 prefix exceeds B, then choose sufficiently small positive u so the legal finite-strength prefix still exceeds B.

## Case 2: r = 0

Then Sx=lambda x with lambda>1. Choose e=x and any finite u satisfying

1/lambda < u < 1.

One cycle maps x to u lambda x. Repetition grows geometrically and both l2 and l-infinity output figures are unbounded over finite protocols.

## Exact universal-over-e classification

For the unrestricted co-axial protocol class in which e and v0 may be chosen:

mu_2(G)<=0
iff
there exists any finite protocol-independent l2 ceiling
iff
there exists any finite protocol-independent l-infinity ceiling.

When mu_2(G)<=0, the sharp common ceiling is 1/gamma.

Thus M13 ROT11's statement that the global constant remains open is superseded in this universal-over-e class. Its one-shot proof remains the simplest proof that the specific 1/gamma bound fails.

## Noncollinear norm-type repair

For d not collinear with e, repeated same-strength reads at G=0 produce a constant nonzero per-shot signal and therefore

||c||_2 ~ sqrt(k),

so l2/Fisher/common-budget figures diverge.

This repetition argument does NOT make ||c||_infinity diverge. Therefore:

NONCOLLINEAR REPEATED SAMPLING
=> L2/FISHER DIVERGENCE,

but

NONCOLLINEAR REPEATED SAMPLING
!= L-INFINITY DIVERGENCE AUTOMATICALLY.

Also d=-e gives the same projector dd^T=ee^T as d=e, so the correct alignment condition is collinearity modulo sign.

M13's finite-protocol Gramian is accepted as the correct fixed-protocol optimization object.

NO novelty / NO canon / NO EXEC_SIGN / NO NEW TASK.
