# Geeky-S10 — Fixed-sensor available storage and observable quotient

RETURN_ID: GEEKY-S10-INT8-FIXED-SENSOR-AVAILABLE-STORAGE-001
DATE: 2026-10-19
STATUS: EXACT FINITE-DIMENSIONAL RESET-FLOW THEOREM / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY

IN_REPLY_TO:
INT8 target-selective storage bridge 001;
Geeky-S10 NC fixed-e quantifier repair;
M13 ROT11 finite-protocol Gramian.

## Setup

Fix unit e in R^n and gamma>0.

Between measurements:
x'=Gx.

At a measurement:
Q_u=I-(1-u)ee^T,
x^+=Q_u x^-,
y=gamma c=(1-u)e^T x^-,
with u in (0,1].

Every finite protocol pi defines a linear map
C_pi:R^n -> l2
with finite-support output vector, so

||C_pi x||_2^2 = x^T W_pi x

for a positive-semidefinite protocol Gramian W_pi.

## Exact extremal output seminorm

Define

N_*(x)=sup_pi ||C_pi x||_2

and

V_*(x)=N_*(x)^2
      =sup_pi x^T W_pi x.

Where finite, N_* is a seminorm:
N_*(alpha x)=|alpha|N_*(x)
and
N_*(x+z)<=N_*(x)+N_*(z).

V_* is therefore a 2-homogeneous convex available-storage value function, generally a supremum of quadratic forms rather than one quadratic form.

## Finite-ceiling equivalence

The following are equivalent in finite dimension:

1. a finite protocol-independent l2 ceiling exists;
2. N_*(x)<infinity for every x;
3. N_* is a finite continuous seminorm;
4. sup_{||x||=1} N_*(x)<infinity.

The sharp fixed-e ceiling is

C_*=(1/gamma) sup_{||x||=1} N_*(x).

Pointwise finiteness implies uniform finiteness because for a Euclidean basis {b_i},

N_*(x)<=sum_i |x_i| N_*(b_i).

## Exact Bellman identity

V_* satisfies

V_*(x)
=
sup_{tau>=0, u in (0,1]}
{
(1-u)^2 [e^T exp(G tau)x]^2
+
V_*(Q_u exp(G tau)x)
},

with the empty protocol contributing zero.

Consequences:

V_*(exp(G tau)x)<=V_*(x),

and

V_*(x)
>=
(1-u)^2(e^T x)^2
+
V_*(Q_u x).

## Minimality

If S>=0 satisfies for all tau,u,x

S(exp(G tau)x)<=S(x)

and

S(Q_u x)+(1-u)^2(e^T x)^2<=S(x),

then every finite protocol telescopes to

||C_pi x||_2^2<=S(x).

Hence

V_*(x)<=S(x).

So V_* is the least nonnegative storage compatible with all legal future protocols.

## Exact kernel

Let

N_e
=
{x: e^T exp(Gt)x=0 for every t>=0}.

In finite dimension,

N_e
=
intersection_{k=0}^{n-1} ker(e^T G^k).

Then exactly

ker N_* = N_e.

Proof:
if N_*(x)=0, a one-measurement protocol after any wait t gives e^T exp(Gt)x=0.
Conversely, if x is in N_e, every free state stays in e^perp, every measurement output is zero, and Q_u acts trivially on the state.

Thus N_* is a genuine norm on the observable quotient R^n/N_e.

## Relation to INT8 quadratic storage

INT8 assumes

P>=0,
Pe=e,
G^T P+PG<=0.

Then

V_*(x)<=x^T P x.

So INT8's P is an ellipsoidal upper storage for the exact minimal value V_*.

Moreover, suppose a quadratic storage x^T P x satisfies the exact measurement dissipation inequality for every x,u. Then necessarily

Pe=rho e

for some rho>=1.

After normalization P_tilde=P/rho,

P_tilde>=0,
P_tilde e=e,

and if the free-flow Lyapunov inequality holds for P, it also holds for P_tilde.

Hence, up to normalization, the INT8 condition is exactly the general quadratic/ellipsoidal storage form for this supply.

## Kernel structure of a quadratic certificate

If P>=0 and

G^T P+PG<=0,

then ker P is G-invariant.

Indeed, for x in ker P, equality of the quadratic form against the negative-semidefinite matrix G^TP+PG forces

(G^TP+PG)x=0,

and therefore PGx=0.

If also Pe=e, then ker P subset e^perp; G-invariance gives

ker P subset N_e.

Thus a singular quadratic certificate may ignore only dynamically unobservable directions.

## Structural interpretation

The exact hierarchy is:

FINITE FIXED-e CEILING
<=>
FINITE EXTREMAL OUTPUT SEMINORM N_*;

QUADRATIC P
=>
FINITE CEILING;

INT8 P
=
ELLIPSOIDAL SPECIALIZATION OF THE STORAGE GEOMETRY.

The necessity of one quadratic P for every finite-ceiling fixed-e model is NOT established here.

Equivalently, the exact minimal storage V_* may be non-Hilbertian.

This is consistent with mature available-storage and switched-system geometry.

## Disposition

FIXED_SENSOR_EXACT_STORAGE = V_* / N_*.
FINITE_CEILING = FINITE_EXTREMAL_OUTPUT_SEMINORM.
KERNEL = STANDARD_UNOBSERVABLE_SUBSPACE.
INT8_P = ELLIPSOIDAL_STORAGE_SUBCLASS_UP_TO_NORMALIZATION.
QUADRATIC_NECESSITY = OPEN.
OBSERVABLE_QUOTIENT = LOAD_BEARING STRUCTURAL HOST.

NO NEW TASK.
