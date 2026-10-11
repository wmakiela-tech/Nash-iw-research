# M12 — Front B contraction-weighted target error certificate

RESULT_CLASS: EXACT LOCAL CONTROL / TARGET-WEIGHTED ERROR BRIDGE / NO PBH OR BBN ENDPOINT CLAIM / NO NOVELTY

## Input from preceding M12 rotations
Assume
X_DE'=G_DE(t,X_DE),
X_FULL'=G_DE(t,X_FULL)+r(t,X_FULL),

with
partial_X G_DE(t,X) <= -c(t) < 0

and
|r(t,X)| <= epsilon(t)
on the declared legal interval.

Then for z=X_FULL-X_DE:
|z(t)|
<= E0(t)|z0| + ∫_{t0}^t E(s,t) epsilon(s) ds,

where
E(s,t)=exp[-∫_s^t c(u)du],
E0(t)=E(t0,t).

## General target
Let the declared trajectory target be

J[X]
=
Phi(X(T))
+
∫_{t0}^T L(t,X(t)) dt.

Assume on the declared domain:
|Phi(x)-Phi(y)| <= L_T |x-y|,
|L(t,x)-L(t,y)| <= ell(t)|x-y|.

Then exactly:

|J[X_FULL]-J[X_DE]|
<=
L_T |z(T)|
+
∫_{t0}^T ell(t)|z(t)| dt.

Substituting the dynamic contraction bound and exchanging integration order gives:

|Delta J|
<=
K0 |z0|
+
∫_{t0}^T K(s) epsilon(s) ds,

with

K0
=
L_T E(t0,T)
+
∫_{t0}^T ell(t)E(t0,t) dt,

and the contraction-weighted target kernel

K(s)
=
L_T E(s,T)
+
∫_s^T ell(t)E(s,t) dt.

This is the exact target-error propagation formula under the declared Lipschitz constants.

## Interpretation
K(s) answers:
how much can a unit RHS error injected at time s affect the final declared target after dynamical contraction?

Thus target relevance is not determined by raw epsilon(s) alone.

A large early RHS error can be strongly forgotten if c is large afterward.
A small late error can dominate if the target is late-weighted and little contraction remains.

Therefore:
RAW RHS ERROR != TARGET ERROR.

## Pure endpoint target
If J[X]=Phi(X(T)) only, then ell=0 and

|Delta J|
<=
L_T E(t0,T)|z0|
+
L_T ∫_{t0}^T E(s,T) epsilon(s) ds.

This is a direct dynamic analogue of an adjoint/sensitivity weighting.

## Linear weighted trajectory target
If
J[X]=a X(T)+∫ w(t)X(t)dt,

then take
L_T=|a|,
ell(t)=|w(t)|,

so
K(s)
=
|a|E(s,T)
+
∫_s^T |w(t)|E(s,t)dt.

This provides a source-native target-weighted error envelope without assuming a universal endpoint kernel.

## Composition with Front B population certificate
From rotation 1:
e_h'+D_h e_h=(n_h^DE)'.

Let E_h(t,X) bound |e_h|.

Then at common state:
epsilon(t)
can be taken as
sup_X sum_h E_h(t,X)[(1-X)k_h^pn + X k_h^np].

Therefore:

source/depletion variation
-> hadron population tracking bounds
-> epsilon(t) for neutron RHS
-> contraction kernel E(s,t)
-> target kernel K(s)
-> |Delta J| bound.

This is a complete noncircular analytical error chain, conditional on source-matched inputs and declared target stability.

## Relation to MT13 boundary-term law
MT13 derived, for a source-sink population target of the form integral q(t)D(t)n(t)dt, the exact integration-by-parts identity containing boundary terms:
DeltaT = -[q n] + ∫ q' n
inside its legal setup.

The present result is complementary:
- MT13 identity is target-structure specific and retains exact boundary terms;
- this M12 theorem propagates a general RHS/trajectory perturbation through a contractive reduced dynamics.

Neither permits dropping boundary terms or replacing a time-sensitive target by total channel count without a separate proof.

## Source-matched admission rule
A prospective PBH/BBN validation can now be staged:

1. Build S_h,D_h and n_h^DE on one legal source/background path.
2. Bound E_h from the exact population tracking formula.
3. Convert E_h to epsilon(t) for the neutron RHS.
4. Use current c(t) monotonicity margin to construct E(s,t).
5. Specify the actual target functional and its Lipschitz/weight structure.
6. Compute K(s).
7. Evaluate the bound ∫K epsilon plus initial-state term.
8. Compare against the target tolerance.

Only after step 7 is a target-safe DE claim available.

## Guards
If target dependence is discontinuous/non-Lipschitz, this certificate does not apply directly.
If the full-vs-DE residual bound is not uniform or not valid along X_FULL, state-feedback mismatch must be bounded first.
If c(t) loses positivity under model extension, the contractive kernel must be replaced.

## Status
TARGET_WEIGHTED_DYNAMIC_ERROR_CERTIFICATE=PASS_EXACT_CONDITIONAL_ON_LIPSCHITZ_TARGET_AND_epsilon.
FULL_NONCIRCULAR_CHAIN_FROM_S_D_TO_TARGET_ERROR=PASS_FORMAL_EXACT_CONDITIONAL_ON_SOURCE_MATCHED_INPUTS.
PBH_B2_WATERFALL_TRANSFER=OPEN.
SOURCE_MATCHED_TARGET_TOLERANCE=NOT_EVALUATED.
SOURCE_MATCHED_K_PBH=UNDEFINED.
NO PBH BOUND / NO BBN ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY.
