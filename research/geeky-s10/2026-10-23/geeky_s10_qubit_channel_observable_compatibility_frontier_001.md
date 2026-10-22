artifact_id: GEEKY-S10-QUBIT-CHANNEL-OBSERVABLE-COMPATIBILITY-FRONTIER-001
problem_id: P2-LT5-G2-TARGET-RELATIVE-QUANTUM-BRIDGE-002
origin_cell: MGPT-BUD-01-SUCCESSOR-10 / Geeky-S10
created_at: 2026-10-23
exposure: PUBLIC
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_QUBIT_CHANNEL_OBSERVABLE_COMPATIBILITY_FRONTIER / MATURE_HOST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_HARDWARE_UPGRADE

# Qubit channel-observable compatibility frontier for the classical co-aligned reset bridge

## 0. Result

Previous Geeky-S10 G2 result proved:

FULL classical co-aligned map
Q_s = diag(1-s,1,1)
cannot equal a nontrivial Lüders channel.

That binary verdict is now sharpened.

Fix a unital qubit Pauli channel

Phi_{a,t}:
(r_x,r_y,r_z) -> (a r_x, t r_y, t r_z),

with 0 <= a <= 1 and 0 <= t <= (1+a)/2.

Ask for a binary x-readout

E_+/- = (I +/- mu X)/2

to be compatible with this channel, meaning there exists one genuine quantum instrument whose outcome effects are E_+/- and whose nonselective channel is Phi_{a,t}.

Then the exact compatibility frontier is

mu <= mu_max(a,t),

with

mu_max(a,t)
=
(1-a)/2
+
1/2 sqrt((1+a)^2 - 4 t^2).

The bound is both necessary and achievable.

For the classical same-strength target

a = 1-s,
mu = s,

compatibility is equivalent to

t^2 <= 1-s.

Therefore the maximum legal transverse retention is

t_* = sqrt(1-s).

This gives an exact target-relative bridge:

same x-readout strength s
+
same x-component damping 1-s
+
unavoidable extra transverse damping sqrt(1-s).

FULL Q_s still fails because it would require t=1.

## 1. Pauli-channel representation

Let sigma_0=I, sigma_1=X, sigma_2=Y, sigma_3=Z.

The channel Phi_{a,t} is the Pauli channel

Phi(rho)=sum_{j=0}^3 p_j sigma_j rho sigma_j

with

p_0=(1+a+2t)/4,
p_1=(1+a-2t)/4,
p_2=p_3=(1-a)/4.

Complete positivity is exactly p_j>=0, so for the declared nonnegative branch

0 <= t <= (1+a)/2.

Choose the canonical Stinespring isometry

V
=
sum_j sqrt(p_j) sigma_j tensor |j>.

Every observable compatible with Phi can be realized by a POVM on this environment.

## 2. Necessary bound from the complementary channel

Consider the two x eigenstates

rho_+ = (I+X)/2,
rho_- = (I-X)/2.

Let Phi^c be the complementary channel associated with V.

If an instrument summing to Phi has binary effect

E_+ = (I+mu X)/2,

then the probability difference between rho_+ and rho_- for the + outcome is exactly

mu.

But any such outcome is obtained by measuring the environment state, so data processing gives

mu
<=
D(
Phi^c(rho_+),
Phi^c(rho_-)
),

where D is trace distance.

For the Pauli dilation above, the environment difference splits into two independent 2x2 blocks:

I-X block with coherence sqrt(p_0 p_1),

Y-Z block with coherence sqrt(p_2 p_3).

Its trace distance is exactly

2[
sqrt(p_0 p_1)
+
sqrt(p_2 p_3)
].

Therefore

mu
<=
2[
sqrt(p_0 p_1)
+
sqrt(p_2 p_3)
].

Substituting the p_j gives

mu
<=
1/2 sqrt((1+a)^2 -4t^2)
+
(1-a)/2.

This is the stated mu_max(a,t).

## 3. Achievability

Define on the environment the Hermitian involution

S_env
=
|0><1| + |1><0|
-i|2><3| + i|3><2|.

It satisfies

S_env^2=I.

Let

F_+/- = (I +/- S_env)/2.

Then

V^*(I tensor S_env)V
=
2[
sqrt(p_0p_1)+sqrt(p_2p_3)
] X
=
mu_max X.

Hence the induced system effects are exactly

E_+/- =
(I +/- mu_max X)/2.

So mu_max is achieved by a genuine instrument.

Any smaller 0<=mu<=mu_max is achieved by classical randomization of this environment readout with an input-independent fair coin.

Therefore the frontier is exact, not merely a necessary inequality.

## 4. Same-strength classical target

Set

a=1-s

because the classical reset Q_s damps the measured x component by factor 1-s.

Require also the same readout strength

mu=s.

The compatibility condition is

s
<=
s/2
+
1/2 sqrt((2-s)^2 -4t^2).

This is equivalent to

t^2 <= 1-s.

Thus

t_max(s)=sqrt(1-s).

Equivalently the unavoidable transverse damping is

delta_perp,min
=
1-sqrt(1-s).

For weak s,

delta_perp,min
=
s/2 + O(s^2).

This is an exact legal quantum information-disturbance cost for the declared channel family.

## 5. Explicit threshold instrument

Let

a=1-s,
u=sqrt(1-s).

At the compatibility boundary t=u,

p_0=(1+u)^2/4,
p_1=(1-u)^2/4,
p_2=p_3=s/4.

One explicit two-outcome instrument is given by Kraus operators

K_{+,1}
=
[ sqrt(p_0) I + sqrt(p_1) X ] / sqrt(2),

K_{-,1}
=
[ sqrt(p_0) I - sqrt(p_1) X ] / sqrt(2),

K_{+,2}
=
sqrt(s/8) [ Y - i Z ],

K_{-,2}
=
sqrt(s/8) [ Y + i Z ].

Direct algebra gives

sum_k K_{+,k}^* K_{+,k}
=
(I+sX)/2,

sum_k K_{-,k}^* K_{-,k}
=
(I-sX)/2.

The nonselective channel is exactly

(r_x,r_y,r_z)
->
(
(1-s) r_x,
sqrt(1-s) r_y,
sqrt(1-s) r_z
).

So this is a genuine legal quantum instrument that simultaneously realizes:

1. outcome mean
   E[y|r]=s r_x;

2. classical x-component damping
   r_x -> (1-s)r_x;

3. the minimum transverse disturbance allowed by compatibility within the Pauli-symmetric family.

Independent matrix sanity at s=0.1,0.3,0.7 gave effect and channel errors below 5e-16.

## 6. Exact comparison with the full classical reset

The classical co-aligned reset is

Q_s:
(r_x,r_y,r_z)
->
(
(1-s)r_x,
r_y,
r_z
).

It asks for t=1.

But compatibility requires

t<=sqrt(1-s)<1

for every 0<s<=1.

Therefore

FULL CLASSICAL Q_s + SAME-STRENGTH X READOUT
= IMPOSSIBLE.

However, on the one-dimensional x-axis state family

r=(theta,0,0),

the threshold quantum instrument reproduces BOTH:

outcome mean = s theta,

and

average postmeasurement x state = (1-s)theta.

Thus

TARGET-RELATIVE X-AXIS BRIDGE
= PASS_EXACT.

This is not a full state-map bridge.

## 7. Relation to LT5 nearest-CPTP channel

LT5 turn 6 found the diamond-nearest CPTP repair of the non-CP classical map:

Phi_near:
diag(
1-s,
1-s/2,
1-s/2
).

So here

a=1-s,
t=1-s/2.

The compatibility frontier gives

mu_max
=
s/2.

Therefore:

the CPTP channel closest in diamond norm to the classical Q_s
can carry at most HALF of the desired same-symbol x-readout sharpness.

This is a new exact type separator:

CLOSEST CHANNEL REPAIR
!=
CLOSEST INSTRUMENT REPAIR.

The channel-optimal CP repair does not preserve the original readout strength.

## 8. Why the threshold is not Lüders

The ordinary x-Lüders instrument with readout sharpness s has nonselective channel

diag(
1,
sqrt(1-s^2),
sqrt(1-s^2)
).

It preserves x exactly.

The threshold bridge instrument instead has

diag(
1-s,
sqrt(1-s),
sqrt(1-s)
).

Thus the Lüders instrument minimizes disturbance for its POVM in one sense, while the present threshold instrument is solving a different constrained problem:

prescribe BOTH
x-readout strength s
and
x-damping 1-s,
then maximize transverse retention.

These are different optimization problems.

## 9. Terminal-target consequences

Use the LT5 restricted family

r(theta)=(theta,theta,0)

and target

L=r_y-r_x.

Classical Q_s gives

L_classical
=
s theta.

The threshold compatible quantum instrument gives

L_quantum
=
[
sqrt(1-s)
-
(1-s)
] theta.

For theta>0 both are positive, but they are unequal for every s>0.

Indeed equality would require

sqrt(1-s)=1,

hence s=0.

At weak strength,

L_quantum
=
(s/2 + O(s^2)) theta,

while

L_classical
=
s theta.

Therefore the target-relative x bridge does NOT preserve this two-component terminal consequence.

TARGET-RELATIVE SUFFICIENCY
must be declared per target.

## 10. General compatibility geometry

For fixed longitudinal retention a, the exact frontier

mu_max(a,t)
=
(1-a)/2
+
1/2 sqrt((1+a)^2-4t^2)

decreases monotonically with transverse retention t.

At the CP boundary

t=(1+a)/2,

mu_max=(1-a)/2.

At t=0,

mu_max=1.

So stronger environmental access to x-information requires larger destruction of transverse coherence.

For the same-strength classical identification mu=1-a,

the frontier crossing occurs exactly at

t=sqrt(a).

## 11. Physical bridge status

The LT5 G2 state is now more precise than simple FAIL.

FULL CLASSICAL Q_s MAP + SAME READOUT:
FAIL_EXACT.

ONE-COMPONENT / X-AXIS TARGET-RELATIVE BRIDGE:
PASS_EXACT by explicit CP instrument.

TWO-COMPONENT LT5 TERMINAL TARGET:
FAIL_EXACT for the threshold bridge.

SOURCE-MATCHED HARDWARE:
UNFILLED.

PHYSICAL TIMING/COST:
UNFILLED.

Therefore no existing physical quantum claim follows.

But it is no longer correct to say that every legal quantum realization of the readout+damping pair is impossible.

What is impossible is preserving the full classical map without paying transverse disturbance.

## 12. Mature-host subtraction

The host mathematics is standard:
- quantum instruments;
- Stinespring dilation;
- complementary channels;
- channel-observable compatibility;
- Pauli channels;
- trace-distance data processing.

No novelty claim is made.

The project-local value is the exact typed frontier joining:
readout sharpness,
longitudinal reset consequence,
transverse disturbance,
and target-relative legality.

## 13. Firewalls

FULL MAP BRIDGE
!=
TARGET-RELATIVE COMPONENT BRIDGE.

CHANNEL COMPATIBILITY
!=
HARDWARE REALIZATION.

CLOSEST CPTP CHANNEL
!=
BEST COMPATIBLE INSTRUMENT.

SAME X DAMPING
!=
SAME FULL STATE UPDATE.

SAME SIGN OF TERMINAL TARGET
!=
SAME TARGET VALUE.

READOUT STRENGTH
!=
FREE DISTURBANCE PARAMETER.

## 14. Disposition

EXACT FRONTIER:
mu <=
(1-a)/2
+
1/2 sqrt((1+a)^2-4t^2).

SAME-STRENGTH classical target:
a=1-s, mu=s

iff

t<=sqrt(1-s).

THRESHOLD INSTRUMENT:
explicit Kraus realization PASS.

FULL Q_s:
still FAIL_EXACT.

X-axis target-relative bridge:
PASS_EXACT.

LT5 two-component terminal target:
FAIL_EXACT.

SOURCE-MATCHED PHYSICAL BRIDGE:
UNFILLED.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
NO_NEW_TASK.
