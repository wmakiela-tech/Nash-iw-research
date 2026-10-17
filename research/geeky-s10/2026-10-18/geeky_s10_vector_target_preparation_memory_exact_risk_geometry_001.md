# Geeky-S10 — Exact vector-target preparation-memory risk geometry

RETURN_ID: GEEKY-S10-LT4-VECTOR-TARGET-PREPARATION-MEMORY-EXACT-RISK-GEOMETRY-001  
DATE: 2026-10-18  
STATUS: PASS_EXACT_MATURE-HOST / MULTIDIMENSIONAL_GAP_CLOSED / NO_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN  
BW_INGESTION_STATUS: PENDING

Private Drive durable copy exists; private locator intentionally omitted from this public scientific body.

## Setup

Let Y,Z be Hilbert spaces. Let q in Z be the deterministic generated-memory error at a chosen time, M:Y->Z the hidden-preparation response operator, and ||y||<=R the admissible hidden initial-state ball.

Define

E_R(q,M)
=
sup_{||y||<=R} ||q+My||.

## Exact dual formula

For real or complex Hilbert spaces,

E_R(q,M)
=
sup_{||z||=1}
[
Re<z,q>
+
R||M^*z||
].

This follows from Hilbert norm duality and the support function of the radius-R ball.

## Sharp bounds

If q=0:

E_R=R||M||.

If q!=0 and qhat=q/||q||:

||q||+R||M^*qhat||
<=
E_R
<=
||q||+R||M||.

## Exact criterion for additive worst-case composition

For q!=0 and R>0,

E_R
=
||q||+R||M||

iff

||M^*qhat||=||M||.

Thus the scalar LT4 sum rule generalizes exactly only when the deterministic-memory direction is a norming left direction of M.

For dim Z=1 this condition holds automatically, recovering

E_R=|q|+R||M||.

## Orthogonal-channel theorem

If

M^*q=0,

equivalently q is orthogonal to closure(Ran M), then

E_R
=
sqrt(
||q||^2
+
R^2||M||^2
).

Hence orthogonal deterministic-memory and hidden-preparation channels combine Pythagoreanly, not additively.

Exact 2D witness:

Z=R^2,
Y=R,
q=(1,0),
My=(0,y).

Then

E_R=sqrt(1+R^2),

not 1+R.

## Small-uncertainty alignment law

For q!=0,

E_R
=
||q||
+
R||M^*qhat||
+
o(R)

as R->0.

If M^*q=0, the linear term vanishes and

E_R
=
||q||
+
R^2||M||^2/(2||q||)
+
o(R^2).

Define the target-relative alignment coefficient

alpha(q,M)
=
||M^*qhat||/||M||

for M!=0.

Then

||q||+R alpha||M||
<=
E_R
<=
||q||+R||M||.

alpha=1:
exact additive rule.

alpha=0:
exact Pythagorean composition.

## Corrected versus raw predictor

LT4's exact corrected predictor leaves residual minimax uncertainty

R||M||.

The RAW predictor omitting both generated memory and hidden preparation has exact combined risk

E_R(q,M).

These are distinct questions.

## Disposition

VECTOR_TARGET_RAW_RISK = EXACT_DUAL_FORMULA.  
SCALAR_SUM_RULE = SPECIAL_CASE_WITH_ALPHA_1.  
ORTHOGONAL_CHANNELS = PYTHAGOREAN_NOT_ADDITIVE.  
LT4_GENERAL_HILBERT_BOUNDS = SHARPENED_TO_EXACT_GEOMETRY.

Mature host: Hilbert-space duality / support functions / adjoint operators / minimax geometry.

NO novelty / NO canon / NO EXEC_SIGN / NO NEW TASK.
