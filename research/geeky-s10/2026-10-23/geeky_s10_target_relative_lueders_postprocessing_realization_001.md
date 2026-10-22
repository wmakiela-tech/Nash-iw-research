artifact_id: GEEKY-S10-TARGET-RELATIVE-LUEDERS-POSTPROCESSING-REALIZATION-001
problem_id: P2-LT5-G2-TARGET-RELATIVE-QUANTUM-BRIDGE-003
origin_cell: MGPT-BUD-01-SUCCESSOR-10 / Geeky-S10
created_at: 2026-10-23
exposure: PUBLIC
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_TARGET_RELATIVE_QUBIT_REALIZATION / MATURE_HOST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_HARDWARE_UPGRADE
supersedes_scoped_statement: GEEKY-S10-QUBIT-CHANNEL-OBSERVABLE-COMPATIBILITY-FRONTIER-001 / TWO_COMPONENT_TERMINAL_TARGET=FAIL_EXACT interpreted globally

# Target-relative Lüders + CPTP postprocessing realization

## 0. Material correction

The previous compatibility-frontier result proved correctly that:

1. the FULL classical co-aligned map
   Q_s=diag(1-s,1,1)
   cannot be a legal nontrivial qubit channel carrying the same x-readout;

2. within the Pauli-diagonal family with fixed longitudinal damping a=1-s and readout sharpness mu=s, maximal transverse retention is constrained;

3. one particular symmetric threshold channel does not reproduce the LT5 terminal target.

However, the dispatch summary over-compressed item 3 as

TWO_COMPONENT_TERMINAL_TARGET = FAIL_EXACT.

That wording is too broad.

Once arbitrary legal CPTP postprocessing after the Lüders instrument is admitted, a restricted preparation family can reproduce the complete CLASSICAL AVERAGED OUTPUT STATE exactly, while preserving the same POVM/readout law.

Therefore the corrected status is:

FULL GLOBAL MAP BRIDGE = FAIL_EXACT.

RESTRICTED-FAMILY AVERAGED-STATE BRIDGE = PASS_EXACT.

SOURCE-MATCHED PHYSICAL HARDWARE BRIDGE = UNFILLED.

## 1. General one-dimensional realization lemma

Fix an unsharp x-Lüders instrument with sharpness s:

E_y=(I+y s X)/2.

Its nonselective Bloch map is

A_s = diag(1,b,b),

where

b=sqrt(1-s^2).

Let the admitted preparation family be one-dimensional:

r_theta = theta v,

for theta in an interval for which all states are physical.

After the Lüders instrument, the averaged Bloch vector is

theta w,

where

w=A_s v.

Let a desired target-relative averaged output be

theta q.

Assume

||q|| <= ||w||.

Then there exists a fixed CPTP postprocessing channel C such that

C(theta w)=theta q

for every admitted theta.

Construction:

if q=0, use the completely depolarizing channel.

Otherwise define

lambda = ||q||/||w|| in [0,1].

Choose an SO(3) rotation R satisfying

R(w/||w||)=q/||q||.

Let U_R be any qubit unitary inducing R.

Let D_lambda be the isotropic depolarizing channel

r -> lambda r.

Then

C = U_R o D_lambda

is CPTP and

C(theta w)
=
theta lambda Rw
=
theta q.

Apply C AFTER every outcome branch of the Lüders instrument.

Because C is trace preserving and outcome independent, the POVM effects remain exactly E_y.

Therefore:

SAME OUTCOME LAW
+
EXACT TARGET-FAMILY AVERAGED STATE

can be realized whenever the desired target vector q is no longer than the Lüders averaged vector w.

This is a target-relative realization theorem, not a global map theorem.

## 2. Application to the LT5 restricted family

Use

v=(1,1,0),

so

r_theta=(theta,theta,0).

The classical co-aligned reset with e=x is

Q_s=diag(1-s,1,1).

Its desired output on this family is

q
=
Q_s v
=
(1-s,1,0).

The x-Lüders averaged vector is

w
=
A_s v
=
(1,sqrt(1-s^2),0).

Compare norms:

||w||^2
=
2-s^2,

||q||^2
=
(1-s)^2+1
=
2-2s+s^2.

Their difference is

||w||^2-||q||^2
=
2s(1-s)
>=0

for every s in [0,1].

Hence the realization lemma applies for ALL s in [0,1].

Define

lambda_s
=
sqrt[
(2-2s+s^2)/(2-s^2)
].

Choose a rotation R_s in the xy plane mapping

w/||w||

to

q/||q||.

Then the postprocessed instrument

J_y
=
C_s o I_y^Lueders

has exactly:

1. effects
   E_y=(I+y s X)/2;

2. outcome mean on every qubit state
   E[y|r]=s r_x;

3. averaged output on the LT5 family
   r_theta -> theta(1-s,1,0),

which is EXACTLY the classical Q_s output on that family.

Therefore both components x and y, and every terminal functional of them, are reproduced exactly on this family.

In particular

L=r_y-r_x

satisfies

L_quantum
=
s theta
=
L_classical.

## 3. Explicit rotation

Let

u=w/||w||,
vhat=q/||q||.

Both lie in the xy plane.

Write their polar angles

phi_w=atan2(sqrt(1-s^2),1),

phi_q=atan2(1,1-s).

Choose

Delta_s=phi_q-phi_w.

Then a z-axis unitary

U_s=exp[-i Delta_s Z/2]

induces the required xy rotation.

The complete postprocessing is:

first isotropic depolarization by lambda_s,

then unitary U_s.

No outcome dependence is needed.

## 4. Why this does not contradict the global nonmap

The global classical map is

Q_s=diag(1-s,1,1).

The realized quantum nonselective map is

Phi_s
=
R_z(Delta_s)
lambda_s
diag(1,sqrt(1-s^2),sqrt(1-s^2)).

These two 3x3 Bloch maps are NOT equal for s>0.

They agree only on the one-dimensional carrier span{v}:

Phi_s v
=
Q_s v.

Thus

FULL MAP EQUALITY = FAIL.

RESTRICTED CARRIER EQUALITY = PASS.

This is exactly the distinction between global realization and target-relative sufficiency.

## 5. Stronger general consequence

The lemma is not special to Q_s.

For one declared preparation direction v and one declared target vector q, an unsharp Lüders instrument can be followed by legal CPTP processing to realize q exactly whenever

||q||
<=
||A_s v||.

So the target-relative feasibility question is not:

does the global quantum channel equal the classical map?

It is:

does the desired restricted image fit inside the contraction radius available after the legal instrument?

For one-dimensional carriers, isotropic depolarization plus a unitary is already sufficient.

This is mature qubit-channel geometry.

## 6. Resource scaling of the postprocessing

For the LT5 family,

lambda_s
=
sqrt[
(2-2s+s^2)/(2-s^2)
].

At weak s,

lambda_s
=
1 - s/2 + O(s^2).

The rotation angle satisfies

Delta_s
=
atan2(1,1-s)
-
atan2(sqrt(1-s^2),1).

Expanding at small s,

Delta_s
=
s/2 + O(s^2).

So the exact target-relative repair requires:
- O(s) isotropic contraction;
- O(s) unitary rotation.

It does not require the O(sqrt(s)) hidden excursion that appears if one insists on unitary-only postprocessing.

## 7. Unit-only versus general CPTP postprocessing

If postprocessing is restricted to a unitary only, norm must be preserved.

Then matching x and y classical coordinates forces an additional z component

z_s
=
sqrt[
||w||^2-||q||^2
]
=
sqrt[2s(1-s)].

So unitary-only target matching yields a hidden orthogonal state mismatch of order sqrt(s).

Allowing depolarization removes this mismatch and matches the complete restricted output state.

Therefore:

UNITARY POSTPROCESSING CONSTRAINT
!=
GENERAL CPTP POSTPROCESSING.

## 8. Relation to the channel-observable compatibility frontier

The prior frontier fixed a GLOBAL Pauli-diagonal averaged channel:

diag(a,t,t)

and optimized compatible readout.

The present theorem fixes instead:
- one legal Lüders POVM/instrument;
- one restricted input carrier;
- one desired target-relative output.

These are different optimization problems.

The prior exact statements remain valid within their declared global channel class.

What is superseded is only the over-broad summary statement that the LT5 two-component terminal target is globally impossible.

Correct replacement:

PAULI-DIAGONAL SAME-AXIS/SAME-LONGITUDINAL GLOBAL CHANNEL TARGET:
constrained by compatibility frontier.

ARBITRARY CPTP POSTPROCESSING ON THE DECLARED 1D FAMILY:
exact averaged-state target realization is possible.

## 9. Statistical history remains quantum-instrument specific

The postprocessing occurs after the Lüders outcome is generated.

Therefore the one-shot outcome law remains

P(y|rho)
=
Tr(E_y rho).

For repeated use, however, the postprocessed state becomes the input to the next instrument.

Thus the multitime record law is generally NOT the latent-bit repeated-Lüders law derived previously.

Consequently:

ONE-SHOT TARGET-RELATIVE STATE MATCH
!=
MULTITIME PROCESS MATCH.

A repeated-protocol transfer would require a fresh theorem for the composed instrument J_y.

This is an important STOP boundary.

## 10. Physical bridge status

The abstract type bridge is now sharply stratified:

A. FULL GLOBAL classical Q_s channel:
FAIL_EXACT.

B. One-dimensional declared preparation family, one-step averaged output:
PASS_EXACT.

C. Same one-shot outcome law:
PASS_EXACT.

D. Same repeated multitime history:
NOT ESTABLISHED.

E. Same intervention timing/cost:
UNFILLED.

F. Source-matched hardware realization:
UNFILLED.

Therefore no physical quantum promotion follows.

## 11. Mature-host subtraction

Ingredients:
- Lüders instruments;
- postprocessing of instruments;
- isotropic depolarizing channels;
- unitary Bloch rotations;
- target-relative channel interpolation.

All are standard quantum-information constructions.

NO NOVELTY.

Project-local value:
the exact repair of G2 from an overly global nonmap statement to a target-relative hierarchy.

## 12. Firewalls

GLOBAL CHANNEL NONMAP
!=
RESTRICTED-FAMILY NONREALIZABILITY.

ONE-STEP AVERAGED-STATE MATCH
!=
MULTITIME INSTRUMENT MATCH.

SAME POVM
+
SAME RESTRICTED OUTPUT
!=
SAME GLOBAL CHANNEL.

ABSTRACT CPTP CONSTRUCTION
!=
SOURCE-MATCHED DEVICE.

TARGET-RELATIVE SUFFICIENCY
!=
FULL THEORY EQUIVALENCE.

## 13. Disposition

MATERIAL REPAIR:

Prior broad summary
TWO_COMPONENT_TERMINAL_TARGET = FAIL_EXACT

is superseded.

Correct status:

FULL_MAP_BRIDGE = FAIL_EXACT.

LT5_RESTRICTED_FAMILY_ONE_STEP_AVERAGED_STATE_BRIDGE = PASS_EXACT.

LT5_TERMINAL_L_ON_THAT_FAMILY = PASS_EXACT.

MULTITIME_HISTORY_BRIDGE = NOT_ESTABLISHED.

SOURCE_MATCHED_HARDWARE/TIMING/COST = UNFILLED.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
NO_NEW_TASK.
