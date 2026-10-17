# Geeky-S10 — Smooth positive moment matching does not control Le Cam deficiency

RETURN_ID: GEEKY-S10-PRF11-SMOOTH-POSITIVE-MOMENT-MATCHING-LE-CAM-OBSTRUCTION-001  
DATE: 2026-10-18  
STATUS: PASS_EXACT_MATURE-HOST / PRF11_MEASURE-CLASS_CAVEAT_SHARPENED / NO_SOURCE_NATIVE_DIFFUSION_CLAIM / NO_CANON / NO_EXEC_SIGN  
BW_INGESTION_STATUS: PENDING

Private Drive durable copy exists; private locator intentionally omitted from this public scientific body.

## Common carrier and analytic positive family

Let mu=dtheta/(2pi) be normalized Haar measure on S1 and let P=mu.

For n>=2 and kappa>0 define Q_{n,kappa} by the density

q_{n,kappa}(theta)
=
exp[kappa cos(n theta)] / I0(kappa)

with respect to mu.

This density is real-analytic and strictly positive.

## Exact finite Fourier-moment matching

Because q_{n,kappa} is invariant under theta -> theta+2pi/n,

E_Q[exp(i r theta)] = 0

for every integer r not divisible by n.

Hence for every 0<|r|<n,

E_Q[exp(i r theta)]
=
E_P[exp(i r theta)]
=
0.

So the first n-1 positive and negative Fourier moments match exactly.

More generally, any prescribed finite set of nonzero Fourier indices can be matched by taking n larger than every absolute index.

## TV separation does not shrink with matching order

The map theta -> n theta mod 2pi preserves Haar measure.

Therefore

TV(P,Q_{n,kappa})

depends on kappa but not on n.

Thus arbitrarily many exact matched moments can be added without reducing the total-variation gap at fixed kappa.

## TV can approach one

For 0<delta<pi let

A_delta={theta: distance(n theta,2pi Z)<delta}.

Then

P(A_delta)=delta/pi.

Moreover

Q(A_delta^c)
<=
(2pi/delta)
exp[-kappa(cos(delta/2)-cos(delta))].

Hence

TV(P,Q)
>=
1-delta/pi
-
(2pi/delta) exp[-kappa(cos(delta/2)-cos(delta))].

For every epsilon>0 choose delta small and then kappa large. Then

TV(P,Q)>1-epsilon.

So the gap can be arbitrarily close to maximal while both laws remain real-analytic, strictly positive, mutually absolutely continuous and defined on the same carrier.

## Experiment-level obstruction

Let Theta={0,1}.

Source experiment E:

P_0=P,
P_1=Q_{n,kappa}.

Compressed experiment F:

R_0=R_1=P.

Let d=TV(P,Q).

Every theta-independent kernel acting on F sees identical input laws, so both outputs equal one law M. Triangle inequality gives

delta(F,E)>=d/2.

The constant-output kernel

M=(P_0+P_1)/2

achieves equality, so exactly

delta(F,E)=d/2.

Conversely

delta(E,F)=0

by ignoring the source observation and outputting P.

Thus

Delta(E,F)=d/2.

Since d can exceed 1-epsilon,

Delta(E,F)>(1-epsilon)/2.

## Decision-risk witness

For equal prior and zero-one binary loss,

R_E^*=(1-d)/2,
R_F^*=1/2.

Thus the risk degradation is exactly

d/2,

and can be arbitrarily close to 1/2 despite exact matching of arbitrarily many declared Fourier moments.

FINITE MOMENT AGREEMENT != DECISION-RISK PRESERVATION.

## What the example does and does not kill

It shows that the discrete-versus-continuous measure-class change in PRF11 is not load-bearing.

Smoothness, positivity, common domination and analyticity alone do not repair the process-to-law first arrow.

What remains uncontrolled is quantitative regularity/high-frequency structure. The construction does NOT rule out positive theorems under:
- fixed finite-dimensional law families;
- uniform derivative/Sobolev/BV bounds;
- bounded likelihood ratios plus additional spectral control;
- fixed smoothing/noise channels;
- direct law or decision-risk bounds.

A common observation kernel may strongly damp the high-frequency modes, so latent TV separation need not survive at the observed level.

## Disposition

FINITE_FOURIER_MOMENTS_PLUS_ANALYTIC_POSITIVITY = INSUFFICIENT_FOR_TV_OR_DEFICIENCY_CONTROL.  
PRF11_MEASURE_CLASS_CAVEAT = SHARPENED: MEASURE-CLASS_CHANGE_NOT_LOAD_BEARING.  
QUANTITATIVE_REGULARITY_OR_DIRECT_LAW_BOUND = STILL_REQUIRED.  
OBSERVATION_SMOOTHING = SEPARATE_SOURCE-NATIVE_BRANCH.

Mature host: Fourier analysis on compact groups / von Mises densities / total variation / Blackwell-Le Cam comparison.

NO novelty / NO canon / NO EXEC_SIGN / NO NEW TASK.
