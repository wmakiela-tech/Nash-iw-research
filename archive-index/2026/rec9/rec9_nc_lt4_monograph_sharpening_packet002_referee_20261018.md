# REC9 — NC LT4 monograph sharpening packet 002 referee

RETURN_ID: REC9-NC-LT4-MONOGRAPH-SHARPENING-PACKET002-REFEREE-001_20261018
CELL: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_08 / Rec9
CLASS: CLAIM-LOCAL STRESS / TYPE / HARDEN
VERDICT: A_PASS_HILBERT_WITH_BANACH_REPAIR / B_QUALITATIVE_PASS / B_QUANTITATIVE_BOUND_REJECT_AND_REPLACE
SEVERITY: HIGH
AUTHORITY: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_NEW_TASK

## Objects reviewed

Primary:
NC-LT4-MONOGRAPH-SHARPENING-PACKET-002
Drive: 1D1RcNtP1OK24z_rTOIfmPohV0LhfONZ0

Current LT4 monograph:
"Opisy efektywne w układach fizycznych — monografia robocza — rozdziały 1–7"
Drive: 1cn97_kO65BcJRRWQrvrL9fKlEYBT3PHg6BJItn1Q4FQ

Relevant current results:
- Theorem 7.3 is explicitly stated for Banach spaces.
- Theorem 7.4 uses the injective fixed-time multiplier exp(-t*lambda) on [0,infinity).

## Executive disposition

NC has found a real sharpening of both seams, but §B.2 contains one material mathematical error.

A. Replacing a two-sided Lipschitz growth rate by a one-sided/logarithmic growth rate is mathematically sound in Hilbert/Euclidean form and is a genuine strengthening of Theorem 7.3. However the monograph theorem is Banach-typed, while NC's displayed hypothesis uses an inner product. It therefore cannot replace Theorem 7.3 globally without a Banach-space duality/semi-inner-product formulation.

B. The qualitative collision insight is correct and materially sharpens Rec9's previous wording:
SPECTRAL SEPARATION IS SUFFICIENT, NOT NECESSARY.
For a fixed intertwiner J, a nonseparating h can still yield full Borel spectral transport if J carries no off-diagonal coupling across h-collisions.

But NC's proposed quantitative inequality

||J m(A)-m(B)J|| <= 2 ||m||_inf kappa_h(J),

with

kappa_h(J)=sup ||Q_j J P_i||

over individual collision blocks, is FALSE in general.

The norm of a sum of many collision blocks is not controlled by the largest individual block norm without a multiplicity/geometry factor.

The qualitative iff at kappa=0 survives in finite pure-point spectrum.
The claimed sharp quantitative bound does not.

---

# A. Theorem 7.3 sharpening

## A1. Current typing

Current Theorem 7.3 is stated for Banach spaces X,Y,Z and uses a norm-Lipschitz constant L(t).

NC proposes the Hilbert-style one-sided condition

<g(u,t)-g(v,t),u-v> <= mu(t)||u-v||^2.

Under this condition, with e=r(x)-y and residual eta,

e' = eta + g(r(x),t)-g(y,t),

one obtains for e!=0

d/dt ||e||
<= mu(t)||e|| + ||eta||,

hence the integrating-factor bound

||e(T)||
<= exp(int mu)||e(t0)||
 + int exp(int_s^T mu) epsilon(s) ds.

This is exact in the Hilbert/Euclidean setting under the declared regularity assumptions.

## A2. Banach repair required

The displayed inner-product condition is not typed on a general Banach space.

Therefore:

HILBERT / EUCLIDEAN VERSION = PASS.

GLOBAL REPLACEMENT OF CURRENT BANACH THEOREM BY THE DISPLAYED INNER-PRODUCT FORM = REJECT_AS_UNTYPED.

A Banach-legal version can be stated using the upper right Dini derivative of the norm and a norming functional / semi-inner-product, i.e. a one-sided logarithmic Lipschitz constant M(t) satisfying

D^+ ||e(t)|| <= M(t)||e(t)|| + epsilon(t).

Then the same integrating-factor estimate follows.

The exact choice of semi-inner-product/duality map must be frozen with the Banach norm.

Guard:

LOGARITHMIC NORM WITHOUT DECLARED NORM / DUALITY CONTRACT
!=
BANACH-SPACE THEOREM.

## A3. "mu<0 gives decreasing bound" needs wording repair

If epsilon=0, mu<0 gives contractive decay.

If epsilon is nonzero, the homogeneous kernel decays, but the total forced error bound need not decrease; it can increase toward or saturate at a forcing-controlled level.

NC's own dissipative example exhibits saturation near 0.5.

Therefore prefer:

NEGATIVE ONE-SIDED RATE => DECAYING MEMORY KERNEL / CONTRACTIVE HOMOGENEOUS ERROR,

not:

NEGATIVE ONE-SIDED RATE => TOTAL ERROR BOUND DECREASES AUTOMATICALLY.

## A4. Cross-chapter use

The logarithmic-norm idea can be a legitimate common mathematical host only after all three chapters use:
- the same declared norm class,
- compatible generator/domain assumptions,
- and the appropriate linear/nonlinear one-sided growth object.

In particular:

"DISSIPATIVE KINETICS" alone does not automatically imply mu<0 in every chosen norm or after every reduction.

Possible conservation directions, nonnormality, state dependence, and norm choice can give mu=0 or mu>0.

Thus the Chapter 6 bridge is promising but must remain host-relative, not automatic.

A_FINAL:
THEOREM_7_3_LOG_NORM_SHARPENING = PASS_HILBERT / STANDARD_HOST
BANACH_GENERALITY = REPAIR_REQUIRED
CROSS_CHAPTER_ONE_OBJECT = CONDITIONAL_ON_SHARED_NORM_AND_DOMAIN_CONTRACT
NOVELTY = NONE

---

# B. Theorem 7.4 collision sharpening

## B1. Exact block identity — PASS

For finite pure-point self-adjoint operators

A = sum_i lambda_i P_i,
B = sum_j mu_j Q_j,

for any bounded Borel f,

Q_j [J f(A)-f(B)J] P_i
=
[f(lambda_i)-f(mu_j)] Q_j J P_i.

PASS EXACT.

Therefore Jh(A)=h(B)J iff

Q_j J P_i=0

for every pair with h(lambda_i) != h(mu_j).

## B2. Qualitative collision criterion — PASS in finite pure-point case

Assume Jh(A)=h(B)J.

For lambda_i=mu_j, every m gives m(lambda_i)-m(mu_j)=0.

For unequal eigenvalues with h(lambda_i)!=h(mu_j), the block already vanishes by h-intertwining.

Thus the only possible obstruction to full Borel transport is an unequal spectral pair satisfying

h(lambda_i)=h(mu_j).

Call these off-diagonal collision pairs.

Then, in finite pure-point spectrum:

Jm(A)=m(B)J for every bounded Borel m

iff

Q_j J P_i=0

for every off-diagonal h-collision pair.

This proves the main conceptual repair:

SPECTRAL SEPARATION OF h ON sigma(A) union sigma(B)
IS SUFFICIENT,
BUT NOT NECESSARY.

A nonseparating multiplier may still give full transport relative to a specific J if J does not couple the colliding fibers.

Therefore Rec9's previous phrase

"SPECTRAL SEPARATION, NOT MULTIPLIER COUNT, IS THE CONTROLLING DISTINCTION"

must be narrowed to:

"MULTIPLIER COUNT IS NOT CONTROLLING.
SPECTRAL SEPARATION IS A J-INDEPENDENT SUFFICIENT CONDITION.
FOR A FIXED J, THE SHARP PURE-POINT CONDITION IS ABSENCE OF J-COUPLING ACROSS OFF-DIAGONAL h-COLLISIONS."

Current Theorem 7.4 itself is unaffected because exp(-t lambda) is injective on [0,infinity), so its collision set is empty.

## B3. NC quantitative inequality (7.3') — REJECT

NC defines

kappa_h(J)
=
sup { ||Q_j J P_i|| : lambda_i != mu_j, h(lambda_i)=h(mu_j) }

and claims

||Jm(A)-m(B)J||
<=
2 ||m||_inf kappa_h(J).

This does not follow from blockwise bounds.

A collection of many small collision blocks can add coherently to an operator with much larger norm.

### Exact 2x2 counterexample

Let H1=H2=C^2,

A=diag(0,1),
B=diag(2,3),

h(lambda)=cos(2 pi lambda).

Then

h(A)=I,
h(B)=I,

so Jh(A)=h(B)J for every J.

Take

J = (1/2) [[1,1],[1,1]].

Its operator norm is 1.

Every rank-one collision block Q_j J P_i has norm 1/2.

Hence

kappa_h(J)=1/2.

Choose a bounded Borel m with

m(0)=m(1)=1,
m(2)=m(3)=-1,

and ||m||_inf=1.

Then

m(A)=I,
m(B)=-I,

so

Jm(A)-m(B)J
=
2J.

Therefore

||Jm(A)-m(B)J||=2.

But NC's claimed right-hand side is

2 * 1 * (1/2) = 1.

Thus:

2 <= 1

would be required.

Contradiction.

Therefore the proposed quantitative inequality is FALSE already in dimension 2.

## B4. Why the multiplication-operator example did not detect the defect

In NC §B.5, J itself is a multiplication operator.

That representation is pointwise diagonal: collision contributions do not accumulate across multiple spectral blocks.

There the L-infinity collision amplitude can indeed control the defect pointwise, and the factor 2 can be attained.

But:

BOUND TRUE IN A DIAGONAL MULTIPLICATION MODEL
!=
BOUND TRUE FOR GENERAL INTERTWINERS.

The finite-dimensional block example exposes the missing accumulation geometry.

## B5. Correct finite pure-point quantitative replacement

Define the full off-diagonal collision operator

J_col
=
sum_{lambda_i != mu_j, h(lambda_i)=h(mu_j)}
Q_j J P_i.

Because h-intertwining kills all noncollision unequal blocks, and equal-eigenvalue blocks contribute zero to every m-defect,

Jm(A)-m(B)J
=
J_col m(A)-m(B) J_col.

Therefore exactly:

||Jm(A)-m(B)J||
<=
2 ||m||_inf ||J_col||.

This is a valid operator-level bound in finite pure-point spectrum.

Also:

FULL BOREL TRANSPORT
iff
J_col=0.

This is the sharp structural criterion.

It is not equivalent to controlling only the largest individual block unless additional orthogonality/multiplicity assumptions are imposed.

A weaker block-max estimate may include an explicit multiplicity factor, but such a factor depends on the collision graph/block geometry and should not be hidden.

Guard:

MAX SINGLE COLLISION BLOCK
!=
NORM OF TOTAL COLLISION COUPLING.

## B6. Continuous spectrum

NC correctly labels the fully general continuous-spectrum statement as unproved.

Rec9 agrees.

The multiplication-operator model is a valid special case, but a general statement for arbitrary normal/self-adjoint A,B and arbitrary bounded J requires spectral-measure / double-operator-integral care.

Do not promote the finite pure-point collision-block sum or the multiplication-operator L-infinity formula to the general continuous-spectrum theorem without that work.

The safe general exact statement already available is:

FULL BOUNDED BOREL INTERTWINING
iff
J E_A(Delta)=E_B(Delta) J

for all Borel Delta,

with domain/type assumptions as appropriate.

How a single noninjective h-intertwining reduces this condition fiberwise in full generality is a separate theorem.

## B7. Nonbijective J

NC is right that Rec9's earlier nonbijective-J caution is naturally explained by the collision/fiber picture.

A noninjective J can simply annihilate spectral sectors on which A and B differ.

Therefore:

FULL SPECTRAL INTERTWINING THROUGH J
!=
GENERATOR EQUALITY OR BIJECTIVE EQUIVALENCE.

This guard remains.

---

# Final claim ceiling

NC_A_LOG_NORM_IDEA = PASS_STANDARD_HOST
NC_A_HILBERT_FORM = PASS
NC_A_AS_GLOBAL_BANACH_REPLACEMENT = REPAIR_REQUIRED
NC_A_NEGATIVE_MU_TOTAL_BOUND_DECREASES = NARROW_TO_DECAYING_KERNEL / FORCED_BOUND_MAY_SATURATE
NC_A_CROSS_CHAPTER_UNIFICATION = CONDITIONAL

NC_B_BLOCK_IDENTITY = PASS_EXACT
NC_B_SEPARATION_NOT_NECESSARY = PASS_EXACT_FINITE_PURE_POINT
NC_B_FIXED_J_COLLISION_COUPLING_CRITERION = PASS_EXACT_FINITE_PURE_POINT
NC_B_KAPPA_BLOCK_MAX_QUANTITATIVE_BOUND = REJECT
NC_B_MULTIPLICATION_OPERATOR_SPECIAL_CASE = PASS_SPECIAL_MODEL
NC_B_GENERAL_CONTINUOUS_SPECTRUM = OPEN
REPLACEMENT_FINITE_POINT_BOUND = 2 ||m||_inf ||J_col||

REC9_PREVIOUS_SEPARATION_WORDING = REPAIR:
separation is a J-independent sufficient condition, not the necessary-and-sufficient criterion.

CURRENT_THEOREM_7_4_EXPONENTIAL = UNAFFECTED / PASS.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_NEW_TASK.

STOP this packet after LT4 integration unless a repaired general continuous-spectrum theorem or a different quantitative collision norm is proposed.
