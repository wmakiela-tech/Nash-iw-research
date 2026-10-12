---
artifact_id: M12-FRONTB-TARGET-WEIGHTED-CHANNEL-COUNT-GATE-001
bw_ingestion_event_id: ING-20261010-0097
bw_qualification_state: FRONTB_TARGET_WEIGHTED_CHANNEL_COUNT
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: NO_AUTHORITY_UPGRADE
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# M12-FRONTB-TARGET-WEIGHTED-CHANNEL-COUNT-GATE-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

M12 - Front B target-weighted channel-count gate
RESULT_CLASS
EXACT LOCAL CONTROL / FRONT-B ADAPTER / TARGET PROPAGATION / NO ENDPOINT NUMERICS / NO NOVELTY CLAIM
TRIGGER
NC/MT13 currentness establishes an exact scalar fact:
for prescribed depletion rate Gamma and fixed branching b_c, integrated channel count can be exact even when the source varies rapidly.
That does NOT by itself imply equal final BBN target such as Y_p or D/H.
This return isolates the exact missing condition.
SETUP
Consider a linear time-varying downstream network:
dot x(t) = A(t)x(t) + sum_c B_c(t) u_c(t),
with fixed initial state x(0), and terminal linear target:
tau = ell^T x(T).
Let Phi(T,s) be the state-transition operator.
For two source histories u and u_tilde define:
delta u_c = u_c - u_tilde_c.
Then exactly:
delta tau
=
sum_c integral_0^T w_c(s) delta u_c(s) ds,
where:
w_c(s)
=
ell^T Phi(T,s) B_c(s).
Call w_c the TARGET SENSITIVITY KERNEL for channel c.
CERTIFICATE A - EXACT SUFFICIENCY CONDITION
Suppose the two histories have equal integrated count in each channel:
integral_0^T delta u_c(s) ds = 0.
Then equal channel counts imply equal terminal target for ALL such zero-integral perturbations iff each w_c(s) is constant in time on the legal support.
Proof:
if w_c is constant, the integral vanishes by zero total mass.
Conversely, if w_c is not constant, choose two legal time windows where w_c differs and shift equal source mass between them; the integrated count is unchanged but delta tau is nonzero.
Therefore:
EQUAL INTEGRATED CHANNEL COUNT
=> EQUAL FINAL TARGET
only under an additional target-sensitivity condition.
CERTIFICATE B - EXACT COUNTEREXAMPLE
Take one scalar downstream state:
dot x = -x + u(t),
x(0)=0,
target tau=x(2).
Compare two nonnegative source histories with the same integrated count 1:
u_1(t)=1 on [0,1], 0 on (1,2],
u_2(t)=0 on [0,1), 1 on [1,2].
Then:
integral u_1 dt
=
integral u_2 dt
=
1.
But:
tau_1
=
integral_0^1 exp[-(2-s)] ds
=
e^-1 - e^-2,
while:
tau_2
=
integral_1^2 exp[-(2-s)] ds
=
1 - e^-1.
They are unequal.
So:
SAME INTEGRATED INJECTION
!=
SAME TERMINAL TARGET.
The difference is entirely due to the time-dependent downstream sensitivity kernel:
w(s)=exp[-(2-s)].
CERTIFICATE C - EXACT OSCILLATION BOUND
For one scalar channel, let the signed measure:
dmu(s)=delta u(s) ds,
with zero total mass:
mu([0,T])=0.
Then for bounded sensitivity kernel w:
|delta tau|
=
|integral w dmu|
<=
(osc w / 2) ||mu||_TV,
where:
osc w = sup w - inf w,
and ||mu||_TV is total variation of the signed source difference.
Proof:
subtract any constant a from w because integral a dmu=0.
Choose a=(sup w+inf w)/2.
Therefore source-profile mismatch matters only through:
1. the source redistribution magnitude;
2. the variation of the target sensitivity kernel.
A rapidly varying source is harmless if w is effectively constant for the declared target.
A slowly varying source can matter if w changes strongly.
CERTIFICATE D - MULTI-CHANNEL VERSION
If each channel count is preserved:
integral delta u_c dt=0,
then:
|delta tau|
<=
sum_c
(osc w_c / 2)
||delta u_c dt||_TV.
Thus NC's exact count law plus a target-kernel bound gives a clean downstream error certificate.
This is more precise than using source timescale alone.
CERTIFICATE E - WHEN EXACT COUNT CONSERVATION IS ENOUGH
Integrated channel count is target-complete for the terminal target iff the input-to-target functional factors through the vector of total channel counts:
tau[u]
=
F(
integral u_1,
...,
integral u_m
)
on the declared legal source class.
For a linear terminal target, this happens exactly when each w_c is constant on the admissible support.
Therefore:
CHANNEL COUNT SUFFICIENCY
IS A TARGET FACTORIZATION PROPERTY.
It is not a generic property of the closure.
CERTIFICATE F - NONLINEAR NETWORK GUARD
For a nonlinear network:
dot x=f(t,x,u),
equal integrated channel counts do not generically imply equal final target.
Around a declared trajectory, first-order target sensitivity is governed by the adjoint kernel:
delta tau
approximately
sum_c integral lambda(s)^T B_c(s) delta u_c(s) ds,
with:
-dot lambda
=
(D_x f)^T lambda,
terminal lambda(T)=grad tau.
This is a FIRST-ORDER local certificate only.
It does not replace a nonlinear source-matched target propagation test.
Therefore:
the exact linear theorem is a control/diagnostic,
not a proof that full BBN abundance response is linear.
CERTIFICATE G - FRONT-B PLACEMENT
NC's result establishes:
prescribed-Gamma scalar channel-count exactness under fixed branching.
M12 placement:
this certifies the closure only at the channel-count layer.
To promote to final BBN target one must additionally establish at least one of:
1. exact target factorization through integrated channel counts;
2. a quantitative target-kernel bound;
3. a source-matched nonlinear target-propagation certificate.
Without one of these:
Y_p / D/H equality is not certified.
CERTIFICATE H - THRESHOLD INTERPRETATION
Branching thresholds can matter in two distinct ways:
A. they alter integrated channel counts;
B. even when channel counts remain matched, they shift injection timing into regions with different target sensitivity.
Thus:
BRANCHING-VARIATION ERROR
and
TARGET-TIME-WEIGHTING ERROR
are distinct.
NC's count-law certificate strongly constrains A.
It does not automatically eliminate B.
PROGRAMME CONSEQUENCE
Front B should separate three layers:
L1 CHANNEL POPULATION / DE CLOSURE
Does the reduced hadron population law reproduce channel counts?
L2 CHANNEL-COUNT CONTRACT
Are integrated counts preserved or quantitatively bounded?
L3 TARGET PROPAGATION
Does the final abundance target factor through those counts, or what is the sensitivity-weighted error?
The current blocker after NC is primarily L3 for the coupled BBN target, plus the already noted feedback/source-matching issue for non-prescribed Gamma.
FIREWALL
FAST SOURCE VARIATION
!=
TARGET ERROR.
SMALL epsilon_DE
!=
NECESSARY FOR CHANNEL-COUNT ACCURACY.
EXACT CHANNEL COUNT
!=
EXACT FINAL ABUNDANCE.
EQUAL TOTAL INJECTION
!=
EQUAL TIME-WEIGHTED RESPONSE.
TARGET PROPAGATION
!=
SOURCE-CLOSURE VALIDATION.
DISPOSITION
FRONT-B BOUNDED ADAPTER REOPEN remains scientifically justified,
but the correct next mathematical object is the target sensitivity kernel / source-to-target map, not another generic source-timescale diagnostic.
NO NUMERICAL BBN ENDPOINT.
NO PBH BOUND.
K_PBH remains undefined.
NO CANON / NO EXEC_SIGN / NO NOVELTY INFERENCE / SCIENCE_FIRST.
