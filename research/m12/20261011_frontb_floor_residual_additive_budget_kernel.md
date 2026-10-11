# M12 — Front B additive residual budget and floor-to-Xn source kernel

RETURN_ID: M12-FRONTB-FLOOR-RESIDUAL-ADDITIVE-BUDGET-KERNEL-001
RESULT_CLASS: EXACT LOCAL CONTROL / COMPUTABLE RESIDUAL TUBE / NO PBH ENDPOINT

## Setup

Use the prior M12 dynamic contraction certificate:

|z(t)| <= K_X(t,t0)|z0| + int_{t0}^t K_X(t,u) epsilon(u) du,

where z=X_full-X_DE and

K_X(t,u)=exp[-int_u^t c0(v)dv].

Let the total RHS mismatch split additively:

epsilon(u) <= epsilon_other(u) + epsilon_floor(u).

Then the bound splits exactly into additive budget contributions:

B_total(t) <= B_init(t)+B_other(t)+B_floor(t),

with

B_floor(t)=int K_X(t,u) epsilon_floor(u)du.

Thus the floor can be audited independently inside the same residual tube.

## Floor-to-population contribution

For species h, define the nonnegative floor forcing magnitude

f_h(s)=S_h(s)[1-alpha_h(s)],

and the population relaxation kernel

Phi_h(u,s)=exp[-int_s^u D_h(v)dv].

From the previous M12 floor result:

E_h(u)=int_{t0}^u Phi_h(u,s) f_h(s) ds

bounds the magnitude of the floor-induced population deficit.

At common X path,

epsilon_floor(u)
<=
sum_h w_h(u) E_h(u),

where

w_h(u)=(1-X(u))k_h^pn(u)+X(u)k_h^np(u).

Therefore

B_floor(t)
<=
sum_h int_{t0}^t K_X(t,u) w_h(u)
       [int_{t0}^u Phi_h(u,s) f_h(s) ds] du.

All terms are nonnegative, so Tonelli/Fubini gives

B_floor(t)
<=
sum_h int_{t0}^t W_h(t,s) f_h(s) ds,

with the exact source-time influence kernel

W_h(t,s)
=
int_s^t
K_X(t,u) w_h(u) Phi_h(u,s) du.

This is the direct floor-source-injection -> X_n error budget.

## Interpretation

The raw quantity int f_h(s)ds is not the scientifically relevant error by itself.

Each source-time floor deficit is weighted twice:

1. by population relaxation Phi_h between source time s and rate time u;
2. by X_n contraction K_X between rate time u and target time t.

Thus early floor activity can be strongly forgotten even when the unweighted integrated floor residual is not tiny.

Conversely, floor activity close to a target-sensitive epoch can be load-bearing.

## Constant-margin closed form

If

c0(t)>=c>0,
D_h(t)>=d_h>0,
w_h(t)<=w_h^max,

then

W_h(t,s)
<=
w_h^max J_{c,d_h}(t-s),

where for tau>=0

J_{c,d}(tau)
=
(e^{-d tau}-e^{-c tau})/(c-d),  c!=d,

and

J_{c,c}(tau)
=
tau e^{-c tau}.

Hence

B_floor(t)
<=
sum_h w_h^max
int_{t0}^t
J_{c,d_h}(t-s) f_h(s) ds.

This is a computable sufficient certificate using only source-floor activity and lower contraction margins.

## Additive budget admission

Suppose an allowed dynamic-X error budget at target time t is Delta_X(t).

If

B_init(t)+B_other(t)+B_floor(t) <= Delta_X(t),

then the declared X_n trajectory tolerance is certified.

If the non-floor contributions already satisfy

B_init+B_other <= Delta_X - margin,

then it is enough to prove

B_floor <= margin.

Therefore the floor can be admitted or rejected without rerunning the entire conceptual error analysis.

## Species prioritization

Because B_floor is a sum of nonnegative species contributions,

B_floor = sum_h B_h^floor,

with

B_h^floor
=
int W_h f_h,

one can rank species by certified upper-bound contribution.

A species with large raw floor activity can still be negligible after W_h weighting.
A species with modest floor activity can dominate if its rates and timing make W_h large.

Therefore:

RAW FLOOR ACTIVITY != TARGET-TIME IMPORTANCE.

## Source-off corollary

If f_h(s)=0 after source turn-off t_off, then for t>t_off

B_h^floor(t)
=
int_{t0}^{t_off} W_h(t,s)f_h(s)ds.

No new floor contribution is created after t_off.
Under positive c and d_h the kernel decays, so the certified contribution is forgotten.

## Firewalls

ADDITIVE RHS RESIDUALS => ADDITIVE ERROR-BUDGET UPPER BOUNDS.
ERROR-BUDGET ADDITIVITY != PHYSICAL INDEPENDENCE.
RAW INTEGRATED FLOOR RESIDUAL != X_n ERROR.
X_n ERROR BOUND != Yp/DH ENDPOINT BOUND.
SPECIES CONTRIBUTION RANKING != PHYSICAL DOMINANCE OUTSIDE THE DECLARED TARGET.
COMMON-PATH CERTIFICATE != FULL COUPLED VALIDATION.

## Status

FLOOR_RESIDUAL_BUDGET_DECOMPOSITION = PASS_EXACT.
SOURCE_TIME_TO_XN_KERNEL = PASS_EXACT.
CONSTANT_MARGIN_CLOSED_FORM = PASS_EXACT.
SPECIES_LEVEL_BUDGETING = PASS_EXACT.
CURRENT_RUN_NUMERICAL_MATERIALITY = NOT_EVALUATED.
PBH_Yp_DH_TARGET_VALIDATION = OPEN.
SOURCE_MATCHED_K_PBH = UNDEFINED.

NO PBH BOUND / NO ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY.
