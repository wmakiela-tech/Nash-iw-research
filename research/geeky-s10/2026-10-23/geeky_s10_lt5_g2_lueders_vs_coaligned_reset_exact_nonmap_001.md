artifact_id: GEEKY-S10-LT5-G2-LUEDERS-VS-COALIGNED-RESET-EXACT-NONMAP-001
problem_id: P2-LT5-G2-CLASSICAL-TO-QUANTUM-TYPE-BRIDGE-001
origin_cell: MGPT-BUD-01-SUCCESSOR-10 / Geeky-S10
created_at: 2026-10-23
exposure: PUBLIC
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_QUBIT_CLASSICAL_TYPE_NONMAP / MATURE_HOST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE

# LT5-G2: Lüders readout versus co-aligned classical reset — exact nonmap

## Question

LT5 G2 asks whether an actual legal CPTP quantum instrument can realize the consequences of the classical carrier used by Geeky/INT8:

classical readout:
b = s e^T x,

classical co-aligned reset:
Q_s = I - s e e^T.

The same scalar s controls both readout strength and damping of the readout direction.

We test the most natural genuine qubit information-bearing candidate: an unsharp Lüders measurement.

## Legal qubit instrument

Let n be a unit Bloch direction and let 0<mu<1.

Effects:
E_y = (I + y mu n·sigma)/2, y=+/-1.

Lüders maps:
I_y(rho) = sqrt(E_y) rho sqrt(E_y).

For Bloch vector r, outcome mean is

E[y|r] = mu n·r.

The nonselective channel is

Lambda_{n,mu}(r)
=
P_n r + gamma (I-P_n) r,

where

P_n = n n^T,
gamma = sqrt(1-mu^2).

Thus the measured Bloch component is preserved and both transverse components are damped.

## Theorem 1: no exact global map equality for any nonzero strength

A classical co-aligned rank-one reset along unit e has Bloch-linear form

Q_{e,s}
=
I - s P_e.

Its spectrum is

{1-s,1,1}.

A nontrivial Lüders channel has spectrum

{1,gamma,gamma},
with 0<gamma<1.

If Q_{e,s}=Lambda_{n,mu}, the spectra must agree.

For 0<s<1 and 0<mu<1 this is impossible because the multiplicities of the damped eigenspaces differ:
- classical Q_s damps one direction and preserves two;
- Lüders dephasing preserves one direction and damps two.

The only equality point is the trivial identity:
s=0 and mu=0.

Therefore

NONTRIVIAL CLASSICAL RANK-ONE RESET
!=
NONTRIVIAL LÜDERS CHANNEL

for every choice of axes.

This is stronger than a same-axis mismatch and does not depend on a strength convention.

## Theorem 2: readout-matched same-axis carrier is maximally type-opposed

Set e=n and require the quantum and classical outcome means to match for every state.

Then necessarily

mu=s.

Classical:
Q_{n,s} acts on the measured component as
r_parallel -> (1-s) r_parallel,
while leaving r_perp unchanged.

Lüders:
Lambda_{n,s} acts as
r_parallel -> r_parallel,
r_perp -> sqrt(1-s^2) r_perp.

So the same readout direction is:
- the ONLY damped direction in the classical co-aligned reset;
- the ONLY preserved direction in the Lüders QND instrument.

Hence no nonzero readout-matched strength can make the state updates agree.

## Theorem 3: no first-order tangent bridge

For weak mu,

Lambda_{n,mu}
=
I
-
(mu^2/2)(I-P_n)
+
O(mu^4).

Classical weak reset:

Q_{e,s}
=
I
-
s P_e.

Therefore if one identifies measurement amplitudes s=mu,

classical disturbance is O(s) along the measured direction,

whereas Lüders disturbance is O(s^2) in the orthogonal plane.

No scalar reparameterization s=f(mu) can repair the global generator geometry:
P_e has rank one while I-P_n has rank two in Bloch space.

Thus the mismatch is not merely a different small parameter; the tangent cones are different.

## Exact strength-law separator

For Lüders sharpness mu define transverse damping amount

delta(mu)
=
1-sqrt(1-mu^2).

Then

delta(mu)
=
mu^2/2 + O(mu^4).

If one insists on matching readout amplitude to a classical strength:
s_readout=mu,

then quantum disturbance is only

delta = 1-sqrt(1-s_readout^2)
      ~ s_readout^2/2.

If instead one matches a classical damping amount s_reset=delta, then

mu
=
sqrt(2 s_reset - s_reset^2)
=
sqrt(2 s_reset)+O(s_reset^(3/2)).

So the quantum readout amplitude is square-root order in the matched disturbance.

The two weak-resource clocks are inequivalent.

## Restricted two-dimensional carrier: map match forces readout-axis mismatch

Take the plane span{n,m}, with m perpendicular to n.

Lüders on this plane acts as

diag(1,gamma)

in coordinates (n,m).

This can equal a classical rank-one reset

diag(1,1-s_reset)

only if the classical damped/readout axis is m, with

s_reset=1-gamma.

But the Lüders outcome law reads n·r, not m·r.

Therefore even on the minimal 2D plane:

MAP MATCH
forces
READOUT DIRECTION MISMATCH.

Conversely, READOUT MATCH along n forces MAP MISMATCH.

So a restricted-state exact bridge still does not realize the original co-aligned classical carrier.

## Concrete terminal-observable sign separator

Use the LT5 restricted family

r(theta)=(theta,theta,0).

Classical Q_s with e=x gives

r' = ((1-s)theta, theta, 0).

For terminal functional
L = r_y-r_x,

L_classical = +s theta.

A sigma_x Lüders instrument with readout sharpness mu gives

r' = (theta, gamma theta, 0),

so

L_Lueders = (gamma-1)theta
          = -delta(mu) theta.

Thus for theta>0 and nonzero strengths, the source-matched sigma_x information-bearing Lüders instrument produces the opposite sign from the classical co-aligned reset on this terminal target.

This is an exact falsifier of a naive consequence transfer.

## Relation to LT5 turn 6

LT5 turn 6 already proved the stronger global CP obstruction:

the naive Bloch lift diag(1-s,1,1) is not CP for s>0,

and its best CPTP diamond distance is s/2.

The present result adds a different type statement:

even a genuine information-bearing Lüders instrument does not repair the classical carrier.

Its legal state disturbance has different eigenspace geometry and different weak-strength scaling.

So:

NONCP NAIVE LIFT
and
LEGAL LÜDERS NONMAP

are distinct obstructions.

## Relation to PRF11 R17 and Geeky Lüders latent-bit phase

PRF11 R17 and the Geeky latent-bit theorem show that one-copy repeated Lüders records are legal and statistically meaningful.

This does NOT imply they instantiate the classical reset-flow theorem.

The one-copy Lüders history is governed by:
- a latent sharp eigenvalue;
- Bernoulli outcome law;
- instrument-specific Bayesian state update;
- one-copy QFI ceiling.

The classical reset carrier is governed by:
- a real state vector;
- analog linear readout;
- co-aligned rank-one state damping;
- potentially different noise and resource scaling.

LEGAL QUANTUM MEASUREMENT
!=
LEGAL TRANSFER OF CLASSICAL RESET THEOREMS.

## Physical bridge status for LT5 G2

1. ACTUAL LEGAL ABSTRACT CPTP INSTRUMENT:
YES — unsharp Lüders sigma_n instrument.

2. DOES IT REALIZE THE CLASSICAL Q_s/readout carrier:
NO — exact NONMAP above.

3. OUTCOME CP MAPS:
specified exactly.

4. OUTCOME LAW:
specified exactly.

5. TERMINAL OBSERVABLE:
can be specified; the r_y-r_x witness gives opposite-sign consequence on the LT5 restricted family.

6. INTERVENTION TIMING:
mathematically defined sequentially, but no source-matched hardware timing contract is established.

7. PHYSICAL COST / HARDWARE:
UNFILLED.

Therefore current project status is

ABSTRACT_LEGAL_QUANTUM_INSTRUMENT = PASS

CLASSICAL_Q_s_TO_LUEDERS_TYPE_BRIDGE = FAIL_EXACT

SOURCE_MATCHED_PHYSICAL_QUANTUM_BRIDGE = UNFILLED.

No classical V*, mixed-noise reset, dose or raw-reset consequence may be promoted to a qubit claim through this Lüders carrier without a new theorem.

## Mature-host subtraction

Ingredients are standard:
- qubit unsharp POVMs;
- Lüders instruments;
- dephasing channels;
- Bloch representation;
- CP legality and QND measurement.

No novelty claim.

Project-local value is the exact bridge verdict required by LT5 G2 and the explicit separation:
readout strength, disturbance strength, and disturbance eigenspace are three different typed objects.

## Firewalls

READOUT STRENGTH
!=
DISTURBANCE STRENGTH.

SAME SYMBOL s
!=
SAME RESOURCE.

INFORMATION-BEARING INSTRUMENT
!=
CLASSICAL CO-ALIGNED RESET.

RESTRICTED MAP MATCH
!=
READOUT MATCH.

LEGAL CPTP
!=
SOURCE-MATCHED HARDWARE.

ABSTRACT SEQUENTIAL TIMING
!=
PHYSICAL TIMING CONTRACT.

## Disposition

LT5 G2 current answer:

CLASSICAL_Q_s / READOUT -> LEGAL LÜDERS INSTRUMENT
= EXACT NONMAP.

A genuine physical type bridge remains UNFILLED.

STOP this bridge unless:
- a different explicit instrument matches both readout and target state-update consequences;
- a source-native device provides outcome maps, timing and cost;
- or referee finds an algebraic error.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
NO_NEW_TASK.
