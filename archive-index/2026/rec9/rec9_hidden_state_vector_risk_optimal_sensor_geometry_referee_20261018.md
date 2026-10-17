# REC9 — hidden-state vector risk and optimal-sensor geometry referee

RETURN_ID: REC9-HIDDEN-STATE-VECTOR-RISK-AND-OPTIMAL-SENSOR-GEOMETRY-REFEREE-001_20261018
CELL: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_08 / Rec9
CLASS: CLAIM-LOCAL STRESS / TYPE / HARDEN
VERDICT: PASS_BOTH_WITH_DECISION-CLASS_SEPARATION
SEVERITY: MEDIUM/HIGH
AUTHORITY: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_NEW_TASK

## Objects reviewed

1. GEEKY-S10-LT4-VECTOR-TARGET-PREPARATION-MEMORY-EXACT-RISK-GEOMETRY-001
   GitHub blob at review: b77f6288d67bbd67ad3bb8ee6b2c869969fdc7d3

2. MT13-HIDDEN-STATE-TARGET-OPTIMAL-SENSORS-KWIDTH-001_20261018
   GitHub blob at review: 2346a90354bfcce26228d59b0552b4af15cee968

3. LT4 source:
   lt4_hidden_state_target_minimax_gramian_001.md
   GitHub blob at review: 2262252d38f07b22ca29866851ae35a0f749667b

## Executive result

Both mathematical returns are correct in their declared classes.

The main referee issue is not a false theorem but a decision-class boundary:

GEEKY raw vector risk
E_R(q,M)=sup_{||y||<=R} ||q+My||

and

MT13 sensor-assisted minimax risk
E(L)=inf_a sup_{||y||<=R} ||My-a(Ly)||

are NOT the same optimization problem.

When the estimator a is free and q is known, adding q to the target changes nothing: the estimator can be shifted by q. Therefore q-alignment geometry is relevant only when q is deliberately left uncorrected / the predictor is frozen, or when q is itself unknown/constrained.

This boundary must be explicit in LT4 integration.

---

# A. Geeky-S10 vector risk

## A1. Exact dual formula — PASS

For Hilbert spaces Y,Z,

E_R(q,M)
=
sup_{||y||<=R} ||q+My||

has the exact dual form

E_R(q,M)
=
sup_{||z||=1}
[
Re<z,q>
+
R ||M^* z||
].

Reason:

||v||=sup_{||z||=1} Re<z,v>

and the support function of the radius-R Hilbert ball is

sup_{||y||<=R} Re<M^*z,y>
=
R||M^*z||.

PASS EXACT.

## A2. Bounds and additive equality criterion — PASS

For q!=0, qhat=q/||q||,

||q|| + R||M^* qhat||
<= E_R
<= ||q|| + R||M||.

The upper bound is triangle inequality.
The lower bound is obtained by choosing z=qhat in the dual formula.

The criterion

E_R = ||q|| + R||M||

iff

||M^* qhat||=||M||

is also correct.

The reverse implication is immediate.
For the forward implication, any maximizing sequence for the sum must satisfy
Re<z_n,q> -> ||q||, hence z_n -> qhat in Hilbert norm; continuity of M^* then forces
||M^* qhat||=||M||.

No norm attainment of M is required.

## A3. Orthogonal channel theorem — PASS

If M^*q=0, then q is orthogonal to closure(Ran M), so

||q+My||^2 = ||q||^2 + ||My||^2.

Hence

E_R(q,M)
=
sqrt(||q||^2 + R^2||M||^2).

PASS EXACT.

Thus:

SCALAR ABSOLUTE-VALUE COMPOSITION
!=
VECTOR NORM COMPOSITION AUTOMATICALLY.

## A4. Small-R law — PASS

For q!=0,

E_R
=
||q||
+
R||M^*qhat||
+
o(R).

If M^*q=0, the exact Pythagorean formula yields

E_R
=
||q||
+
R^2||M||^2/(2||q||)
+
o(R^2).

PASS.

## A5. Interpretation guard

The alignment coefficient

alpha(q,M)=||M^*qhat||/||M||

is a property of the chosen target norm, the fixed systematic direction q, and M.

It is NOT:
- an intrinsic physical scalar,
- a parameter identifiability measure,
- a stochastic risk coefficient,
- or an experiment-independent observable.

TARGET-NORM / PREDICTOR-RELATIVE ONLY.

---

# B. MT13 fixed-sensor theorem

## B1. Fixed exact noiseless measurement — PASS

Let b=Ly and ||y||<=R.

Define

E(L)
=
inf_{a:ran L -> Z}
sup_{||y||<=R}
||My-a(Ly)||.

Then

E(L)
=
R ||M|_{ker L}||.

PASS EXACT in finite-dimensional Hilbert spaces.

Lower bound:
b=0 contains the symmetric pair y,-y in ker L, so one common estimate must miss one target by at least ||My||.

Upper bound:
for observed b, let y_b=L^dagger b be the minimum-norm lift.
Every feasible y has form y_b+v with v in ker L, v orthogonal y_b and

||v|| <= sqrt(R^2-||y_b||^2).

Choose a(b)=M y_b.
Then residual is Mv and is bounded by

R||M|ker L||.

Equality is attained in the worst-case fiber b=0.

Therefore the risk depends only on the unresolved fiber ker L.

## B2. Exact recovery condition — PASS

For fixed L:

E(L)=0
iff
ker L subset ker M.

This is the precise target-relative sufficiency condition.

FULL HIDDEN-STATE RECOVERY IS NOT REQUIRED.

## B3. Optimal unrestricted rank-k measurements — PASS

For rank(L)<=k,

inf E(L)
=
R sigma_{k+1}(M),

with singular values ordered decreasingly.

This is exactly the Courant-Fischer / optimal-recovery statement.

Measuring the top k right singular directions attains it.

PASS.

Guard:

UNRESTRICTED MATHEMATICAL SENSOR ORIENTATION
!=
PHYSICALLY ADMISSIBLE SENSOR.

## B4. Accessible channel C — PASS WITH BUDGET QUALIFIER

If L=HC, then

ker C subset ker L,

so

E(L) >= R||M|ker C||.

PASS.

Thus zero error is impossible unless

ker C subset ker M.

If that inclusion holds, M factors through C in finite dimension. Zero risk is achievable only when the admissible readout class H has enough dimension/orientation to preserve the target-relevant quotient.

Therefore retain MT13 wording "with enough accessible linear readouts."

Do NOT shorten it to:

ker C subset ker M => any sensor through C gives zero error.

---

# C. Cross-object decision-class separation

This is the main referee addition.

## C1. Free estimator removes known deterministic q

Consider the sensor-assisted problem with a known deterministic term q:

E_q(L)
=
inf_a
sup_{||y||<=R}
||q+My-a(Ly)||.

Set

a(b)=q+	ilde a(b).

Then

E_q(L)
=
inf_{	ilde a}
sup_{||y||<=R}
||My-	ilde a(Ly)||
=
R||M|ker L||.

Therefore:

KNOWN q + FREE ESTIMATOR
=> q DOES NOT AFFECT THE MINIMAX SENSOR RISK.

It is exactly removable by centering.

This is not a contradiction with Geeky.

Geeky studies a frozen RAW predictor that leaves q uncorrected:

E_R(q,M)
=
sup ||q+My||.

MT13 studies an optimized estimator after measurement.

Therefore:

RAW FIXED-PREDICTOR RISK
!=
SENSOR-ASSISTED OPTIMAL-ESTIMATOR RISK.

## C2. Consequence for sensor orientation

The SVD rule

"measure top right singular directions of M"

is optimal for the centered hidden-state minimax problem.

It need not describe the optimal orientation for a constrained policy that is forbidden to correct q and only removes measured hidden components.

Example of the distinction:

M=diag(3,1), R=1, q=(0,100).

If a correction-only policy measures y1, the unresolved kernel is e2 and the frozen-q residual worst case is

max_{|t|<=1} ||(0,100)+(0,t)|| = 101.

If it measures y2, the unresolved kernel is e1 and the frozen-q residual is

max_{|t|<=1} ||(3t,100)|| = sqrt(10009) approx 100.045.

Thus a q-relative constrained policy can prefer the lower-singular-value direction.

This does NOT refute MT13 because MT13 allows the estimator to center all known deterministic terms.

Guard:

SVD-OPTIMAL FOR CENTERED MINIMAX
!=
SVD-OPTIMAL FOR EVERY FROZEN-PREDICTOR POLICY.

## C3. LT4 integration rule

When combining these results, the manuscript must first declare which object is being optimized:

1. RAW predictor risk:
   predictor fixed, q left uncorrected.
   Use Geeky geometry.

2. Corrected hidden-preparation risk without extra measurement:
   q already removed / baseline known.
   Use R||M||.

3. Sensor-assisted optimal estimator:
   observation Ly available and estimator free.
   Use R||M|ker L||.

4. Optimal unrestricted k-sensor design:
   use R sigma_{k+1}(M).

5. Access-constrained sensors:
   use the legal C/H class and retain the ker C lower floor.

These are nested but distinct contracts.

---

# D. Claim ceiling

GEEKY_VECTOR_DUAL_FORMULA = PASS_EXACT
GEEKY_ADDITIVE_CRITERION = PASS_EXACT
GEEKY_ORTHOGONAL_PYTHAGOREAN = PASS_EXACT
GEEKY_SMALL_R_ALIGNMENT = PASS
GEEKY_ALPHA = TARGET/PREDICTOR/NORM_RELATIVE

MT13_FIXED_L_RISK = PASS_EXACT
MT13_EXACT_RECOVERY_IFF_KERL_SUBSET_KERM = PASS
MT13_UNRESTRICTED_K_SENSOR_SVD = PASS_EXACT
MT13_ACCESS_CHANNEL_LOWER_BOUND = PASS
MT13_ZERO_ERROR_THROUGH_C = CONDITIONAL_ON_SUFFICIENT_READOUT CLASS

CROSS_OBJECT:
KNOWN_Q_FREE_ESTIMATOR_RISK = R||M|ker L||
RAW_Q_PLUS_MY_RISK = DIFFERENT DECISION CLASS
SVD_SENSOR_RULE = NOT AUTOMATICALLY TRANSFERABLE TO FROZEN-RAW-PREDICTOR POLICY

NO STOCHASTIC / LE CAM CLAIM
NO PHYSICAL SENSOR ADMISSION
NO QUANTUM PROCESS TRANSFER
NO PBH ENDPOINT
NO CANON / NO EXEC_SIGN / NO NOVELTY / NO NEW TASK

STOP after LT4 integration unless:
- a noisy/finite-sample sensor theorem is promoted,
- a physical admissible sensor class is proposed,
- or q is retyped as unknown rather than known deterministic systematic.
