# Geeky-S10 — Hidden-state endpoint-zero rigidity and early-time separation

RETURN_ID: GEEKY-S10-LT4-HIDDEN-STATE-ENDPOINT-ZERO-RIGIDITY-AND-EARLY-TIME-SEPARATION-001  
DATE: 2026-10-18  
STATUS: PASS_EXACT_FOR_BOUNDED_GENERATOR / MATURE-HOST_ABSORBED / NO_UNBOUNDED_C0_EXTENSION / NO_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN  
BW_INGESTION_STATUS: PENDING

Private Drive durable copy exists; private locator intentionally omitted from this public scientific body.

## Setup

For the LT4 hidden-state model let

M_T = G P exp(TL) J_Y

be the endpoint influence operator of the unknown initial hidden sector. For bounded L,

M(z)=G P exp(zL)J_Y

is an entire operator-valued function.

Its Taylor coefficients are

M_k=G P L^k J_Y.

In the direct-sum setup M_0=GPJ_Y=0.

## Endpoint-zero rigidity theorem

Suppose distinct real times t_n>=0 satisfy

M(t_n)=0

and t_n -> t_* for a finite real t_*.

Then

M(z)=0

for every complex z.

Proof: for arbitrary y in Y and zeta in Z,

f_{y,zeta}(z)=<zeta,M(z)y>

is scalar entire and vanishes on a set with finite accumulation point. By the identity theorem it vanishes identically. Hence M is identically zero.

Therefore, if M is nontrivial, its exact endpoint-zero set has no finite accumulation point and intersects every compact real-time interval in only finitely many points.

## Exact counterexample: infinitely many isolated zeros

Take

L=[[0,1],[-1,0]],

with X=span(e1), Y=span(e2), P selecting the first component and G=identity.

Then

M_t=sin(t).

Thus M_{n pi}=0 for all integers n, but M_t is nonzero between those times.

So:

INFINITELY MANY ENDPOINT-ZERO TIMES
!=
FULL-HISTORY INVISIBILITY

unless the zero times have a finite accumulation point.

## Gramian rigidity

For

W_T = integral_0^T M_t^* M_t dt,

LT4 proved W_T=0 iff M_t=0 on [0,T].

For bounded L, analyticity strengthens this:

W_T=0 for any one T>0
=>
M is identically zero
=>
W_S=0 for every S>0.

Thus one exact zero history Gramian at any positive horizon certifies all-time target invisibility of the hidden initial sector within this bounded-generator model.

## Quantitative early-time noncancellation

Assume M is not identically zero and let m>=1 be the first index with

M_m=G P L^m J_Y !=0.

Then

M_t=t^m M_m/m! + R_{m+1}(t).

Let

K=||GP|| ||J_Y||,
ell=||L||.

For t>=0,

||R_{m+1}(t)||
<=
K exp(t ell) (t ell)^(m+1)/(m+1)!.

Therefore

||M_t||
>=
t^m/m! [
||M_m||
-
K exp(t ell) t ell^(m+1)/(m+1)
].

If ell>0 define

delta =
min(
1/ell,
(m+1)||M_m|| / [2 e K ell^(m+1)]
).

Then for every 0<t<=delta,

||M_t||
>=
t^m ||M_m||/(2m!)
>0.

Hence no exact recancellation can occur arbitrarily close to t=0 after the first nonzero leakage moment.

## Endpoint-history small-time bridge

LT4 gives

E_end(T)
~
R ||M_m|| T^m/m!,

and

E_hist(T)
~
R ||M_m|| T^(m+1/2) / [m! sqrt(2m+1)].

Therefore

lim_{T->0}
E_hist(T) / [sqrt(T) E_end(T)]
=
1/sqrt(2m+1).

## Finite sampling guard

A finite family of exact endpoint zeros does not certify history invisibility. Even an infinite discrete family with no finite accumulation does not certify it.

Thus:

FINITE ENDPOINT AGREEMENT
!=
HISTORY AGREEMENT.

Approximate small endpoint residuals also do not imply a small history Gramian without additional derivative/bandwidth/analyticity control.

## Disposition

ENDPOINT_ZERO_ACCUMULATION = GLOBAL_INVISIBILITY_FOR_BOUNDED_GENERATOR.  
FINITE_ENDPOINT_ZERO_SET = NONCERTIFYING_IN_GENERAL.  
ONE_ZERO_HISTORY_GRAMIAN = GLOBAL_INVISIBILITY_FOR_BOUNDED_GENERATOR.  
EARLY_TIME_RECANCELLATION = EXCLUDED_BELOW_EXPLICIT_DELTA_AFTER_FIRST_NONZERO_MOMENT.  
UNBOUNDED_GENERATOR_EXTENSION = OPEN_NOT_ASSUMED.

Mature host: operator-valued entire functions / identity theorem / semigroup power series / observability Gramian.

NO novelty / NO canon / NO EXEC_SIGN / NO NEW TASK.
