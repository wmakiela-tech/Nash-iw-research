# M12 — Front B coupled-path floor residual small-gain gate

RETURN_ID: M12-FRONTB-COUPLED-PATH-FLOOR-RESIDUAL-SMALL-GAIN-GATE-001
RESULT_CLASS: EXACT CONDITIONAL CONTROL / COUPLED FEEDBACK ERROR CERTIFICATE / NO PBH ENDPOINT

## Purpose

Previous M12 results control the floor residual on a common prescribed source/background/X path.
The remaining mathematical guard is feedback:
population error changes X_n, and X_n error can change source/depletion rates and hence population error.

This return gives a sufficient exact coupled-path stability certificate.

## Coupled error variables

Let

Z(t)=|X_tilde(t)-X(t)|,

and let E(t) be a nonnegative aggregate population-error envelope, for example

E(t)=sum_h |n_tilde_h(t)-n_h(t)|

after any declared species weighting.

Assume the source-native equations and declared regime provide constants or time-local bounds

c(t)>0,
d(t)>0,
a(t)>=0,
b(t)>=0,

such that

Z' <= -c Z + a E,

E' <= b Z - d E + F_floor,

where F_floor(t)>=0 is the direct floor-source forcing envelope.

Interpretation:

c = X_n contraction margin,
d = population relaxation/depletion margin,
a = sensitivity of X_n dynamics to population error,
b = sensitivity of population dynamics to X_n/background mismatch.

All four must be established on one declared common regime.
They are not inferred from the floor algebra alone.

## Exact positive-system comparison

Define v=(Z,E)^T and

M(t)=
[[-c(t), a(t)],
 [ b(t),-d(t)]].

Then componentwise

v' <= M(t)v + (0,F_floor)^T.

Because M(t) is Metzler, the comparison system is order preserving.
If Psi(t,s) is its positive state-transition matrix, then

v(t)
<=
Psi(t,t0)v(t0)
+
int_{t0}^t
Psi(t,s)(0,F_floor(s))^T ds

componentwise.

This is the exact coupled analogue of the prior scalar contraction bounds.

## Constant-margin small-gain certificate

Suppose on the declared regime

c(t)>=c>0,
d(t)>=d>0,
a(t)<=a,
b(t)<=b,

with

c d > a b.

Then the constant comparison matrix

M=
[[-c,a],
 [ b,-d]]

is Hurwitz.

Equivalently the dimensionless feedback gain

kappa = ab/(cd)

satisfies

kappa < 1.

Therefore bounded floor forcing produces bounded coupled population/X_n error.

This is a genuine small-gain condition:
the X-to-population feedback and population-to-X feedback cannot overcome the two contraction margins.

## Uniform forcing bound

If

0 <= F_floor(t) <= F_max

and initial errors are zero, then the rectangle

0 <= Z <= Z_bar,
0 <= E <= E_bar

with

Z_bar = a F_max/(cd-ab),

E_bar = c F_max/(cd-ab)

is forward invariant for the comparison system.

Hence

Z(t) <= a F_max/(cd-ab),

E(t) <= c F_max/(cd-ab)

for all times in the declared regime.

This converts a source-floor forcing ceiling into a coupled-path error ceiling.

## Time-dependent integral version

Without replacing coefficients by constants, the exact comparison remains

v(t)
<=
Psi(t,t0)v0
+
int Psi(t,s)(0,F_floor(s)) ds.

Thus a sharper computation can use the actual time-dependent Jacobian/Lipschitz margins instead of the constant small-gain envelope.

The constant condition cd>ab is only a sufficient uniform certificate.

## How to obtain b

For one species with intended law

n'=S(X,t)-D(X,t)n,

and floor executor

n_tilde'
=
alpha(n_tilde)S(X_tilde,t)
-
D(X_tilde,t)n_tilde,

the path-mismatch part can be bounded by

|S(X_tilde)-S(X)|
+
|D(X_tilde)-D(X)| |n|

plus the direct floor forcing and the ordinary -D e relaxation term.

If

|partial_X S|<=L_S,
|partial_X D|<=L_D,
|n|<=N_max,

then one legal choice is

b_h <= L_S + N_max L_D,

with aggregation across species according to the chosen E norm.

This shows precisely what source-native information is still required.

## How to obtain a

For

F_had(X,n)
=
(1-X)A(n)-X B(n),

population derivatives are

partial_{n_h}F_had
=
(1-X)k_h^pn - X k_h^np.

A conservative absolute Lipschitz bound is

a
<=
sum_h
[(1-X)k_h^pn + X k_h^np]

after matching the chosen aggregate norm and adding any other population-dependent terms.

Again this is a bound to verify on the declared regime, not a universal constant.

## Failure interpretation

If

cd <= ab,

the certificate fails.

This does NOT prove physical instability or DE failure.
It means this coarse two-variable contraction argument cannot guarantee that feedback stays controlled.

Possible next actions are only:
- use sharper time-dependent Psi;
- use species-resolved matrix comparison;
- shrink the regime;
- establish stronger source-native derivative bounds;
- or perform direct coupled validation.

No higher-structure or endpoint inference follows.

## Relation to the prior common-path result

Setting b=0 removes X-to-population feedback.
Then the system becomes triangular and reduces to the earlier common-path chain.

Therefore the common-path theorem is an exact special case of this coupled comparison architecture.

## Firewalls

COMMON-PATH PASS != COUPLED-PATH PASS.
SMALL-GAIN FAILURE != PHYSICAL INSTABILITY.
SMALL-GAIN PASS != Yp/DH ENDPOINT VALIDATION.
LIPSCHITZ BOUNDS != SOURCE VALIDATION.
AGGREGATED TWO-VARIABLE CERTIFICATE != SPECIES-RESOLVED EXACT DYNAMICS.
NO PBH BOUND FOLLOWS.

## Status

COUPLED_PATH_COMPARISON_SYSTEM = PASS_EXACT_CONDITIONAL.
SMALL_GAIN_SUFFICIENT_CERTIFICATE = PASS_EXACT.
UNIFORM_FLOOR_TO_XN_BOUND = PASS_EXACT_CONDITIONAL.
SOURCE_NATIVE_CONSTANTS_a_b_c_d = NOT YET EVALUATED FOR CURRENT RUN.
PBH_DE_DYNAMIC_ACCURACY = OPEN.
PBH_Yp_DH_TARGET_VALIDATION = OPEN.
SOURCE_MATCHED_K_PBH = UNDEFINED.

NO PBH BOUND / NO ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY.
