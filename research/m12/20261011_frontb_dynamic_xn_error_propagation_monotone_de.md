# M12 — Front B dynamic X_n error propagation under monotone DE field

RESULT_CLASS: EXACT LOCAL CONTROL / DYNAMIC TRAJECTORY ERROR CERTIFICATE / NO PBH ENDPOINT / NO NOVELTY

## Setup
Let the reduced DE trajectory satisfy
X_DE' = G_DE(t,X_DE).

Let the comparison/full reduced trajectory satisfy
X_FULL' = G_FULL(t,X_FULL)
        = G_DE(t,X_FULL) + r(t,X_FULL).

Assume both remain in the declared physical interval [0,1].

Current Mech-S6 source-native result gives
partial_X G_DE(t,X) <= -c0(t) < 0
through the frozen/current public Wu-Xu DE model, with
c0(t)=Gamma_n_SM(t)(1+exp[-Q/T(t)]) + 1/tau_n
as a positive baseline; hadronic DE terms are nonincreasing in X.

Assume a residual bound
|r(t,X)| <= epsilon(t)
for all legal X, or at least along X_FULL(t).

## Exact contraction/error inequality
Let z=X_FULL-X_DE.
By the mean-value theorem and one-sided monotonicity,
sign(z)[G_DE(t,X_FULL)-G_DE(t,X_DE)] <= -c0(t)|z|.

Hence almost everywhere:
d|z|/dt <= -c0(t)|z| + epsilon(t).

Therefore:
|z(t)|
<= exp[-∫_{t0}^t c0(u)du] |z(t0)|
 + ∫_{t0}^t exp[-∫_s^t c0(u)du] epsilon(s) ds.

This is exact.

If c0(t)>=c_min>0:
|z(t)|
<= e^{-c_min(t-t0)}|z0|
 + (1-e^{-c_min(t-t0)}) sup epsilon / c_min.

Thus dynamic X_n error is damped by the same monotonicity margin that guarantees frozen uniqueness.

## Composition with population-error certificate
From M12 rotation 1, for each hadron species:
e_h'+D_h e_h=(n_h^DE)'.

Let E_h(t) be its exact tracking bound.
At common X:
|deltaF_had(t,X)|
<= sum_h E_h(t)[(1-X)k_h^pn + X k_h^np].

Therefore one legal choice is
epsilon(t)
=
sup_{X in [0,1]}
sum_h E_h(t,X)[(1-X)k_h^pn + X k_h^np].

Then:
source/depletion variation
-> E_h
-> epsilon(t)
-> dynamic |X_FULL-X_DE| bound.

This is the first fully noncircular analytical chain from population closure error to neutron-fraction trajectory error.

## Boundary robustness
Suppose the DE field has inward margins
m0(t)=G_DE(t,0)>0,
m1(t)=-G_DE(t,1)>0.

If
epsilon(t) < min{m0(t),m1(t)}
for the declared time interval,
then the perturbed/full field also satisfies
G_FULL(t,0)>0,
G_FULL(t,1)<0.

Hence [0,1] remains forward invariant for the perturbed comparison system.

So the same residual certificate can protect both trajectory accuracy and physical-domain invariance.

## Frozen root versus dynamic trajectory
Current Mech-S6 frozen theorem gives a unique instantaneous DE root and root-error bound.
The present theorem is different:
it controls the actual time-dependent trajectory under a time-dependent residual.

Therefore:
FROZEN ROOT ERROR != DYNAMIC TRAJECTORY ERROR.

Both are now available, but neither alone gives a BBN endpoint.

## Target propagation
For any target functional Lipschitz in the trajectory under norm ||.|| with constant L_T:
|T[X_FULL]-T[X_DE]|
<= L_T ||X_FULL-X_DE||.

This step requires a declared target norm/stability constant.
No universal Y_p or D/H claim follows without source-native target typing.

## Guards
If the residual bound is only available on a common reference path, not uniformly in X or along X_FULL, it cannot be inserted directly into the theorem.
State-feedback mismatch must first be bounded.

If c0 loses positivity in an extended model, the contraction result must be recomputed; current positivity is source/model specific.

## Status
DYNAMIC_X_TRAJECTORY_ERROR_CERTIFICATE=PASS_EXACT_CONDITIONAL_ON_epsilon.
BOUNDARY_INVARIANCE_ROBUSTNESS=PASS_EXACT_CONDITIONAL_ON_MARGIN.
POPULATION_TO_X_DYNAMIC_ERROR_CHAIN=PASS_EXACT_CONDITIONAL_ON_COMMON_PATH_OR_UNIFORM_BOUND.
PBH_DE_DYNAMIC_SOURCE_VALIDATION=OPEN.
BBN_ENDPOINT_ACCURACY=OPEN.
PBH_B2_WATERFALL_TRANSFER=OPEN.
SOURCE_MATCHED_K_PBH=UNDEFINED.
NO PBH BOUND / NO ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY.
