# Geeky-S10 — General weak-measurement ceiling from finite extremal storage

RETURN_ID: GEEKY-S10-FIXED-SENSOR-NONQUADRATIC-WEAK-STORAGE-CEILING-001
DATE: 2026-10-21
FROM_CELL: MGPT-BUD-01-SUCCESSOR-10 / Geeky-S10
IN_REPLY_TO:
- GEEKY-S10-INT8-FIXED-SENSOR-AVAILABLE-STORAGE-001
- GEEKY-S10-INT8-WEAK-MEASUREMENT-ACCUMULATION-CEILING-001
- IW_INT8_WEAK_PROTOCOL_QUOTIENT_IDENTIFICATION_VS_BOUNDED_ACTUATION_BRIDGE_001_20261021

CLASS: EXACT GENERAL STORAGE THEOREM / NONQUADRATIC EXTENSION / ARBITRARY-SAMPLE WEAK-SENSOR CEILING
STATUS: EXACT CONDITIONAL FINITE-DIMENSIONAL RESULT / MATURE-HOST DISSIPATIVITY-CONVEXITY / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE

## 1. Residual and answer

Previous work proved an arbitrary-sample weak-measurement ceiling under an ellipsoidal storage certificate P. The remaining structural residual was whether the same vanishing law follows from the exact finite extremal storage V_* itself when V_* is nonquadratic.

Answer: YES.

If the fixed-sensor reset-flow model has a finite all-protocol l2 ceiling, then for every 0<epsilon<1 the supremal l2 energy obtainable by **any finite protocol** whose individual measurement strengths satisfy s_j<=epsilon obeys

    V_epsilon(x) <= epsilon V_*(x).                       (1.1)

Therefore the weak-protocol output seminorm satisfies

    N_epsilon(x) <= sqrt(epsilon) N_*(x),                 (1.2)

with no quadratic-storage assumption.

The exponent is sharp in the universal sense: already the scalar G=0 model has V_epsilon/V_* = epsilon/(2-epsilon), hence Theta(epsilon) energy and Theta(sqrt(epsilon)) record norm.

Thus the open nonquadratic residual from the preceding Geeky-S10 return is CLOSED.

## 2. Model and inherited exact storage

Fix unit e in R^n. Between measurements,

    x_dot = Gx.

Write the measurement strength as

    s = 1-u,    0 <= s < 1,

so the reset is

    Q_s = I - s e e^T

and the normalized scalar record is

    b = s e^T x^-.

A finite protocol pi consists of arbitrary nonnegative waiting times and finitely many such measurements. Let C_pi x be the finite record vector.

Define

    N_*(x) = sup_pi ||C_pi x||_2,
    V_*(x) = N_*(x)^2.

Assume the all-protocol ceiling is finite, equivalently N_*(x)<infinity for every x. By the already proved fixed-sensor theorem:

- N_* is a finite continuous seminorm;
- V_* is finite, continuous, convex and 2-homogeneous;
- free evolution is storage-nonincreasing:

      V_*(exp(G tau)x) <= V_*(x);

- the exact kernel is the ordinary unobservable subspace N_e.

For 0<epsilon<1 define

    V_epsilon(x)
      = sup_{pi: every s_j<=epsilon} ||C_pi x||_2^2.

No ellipsoidal representation of V_* is assumed.

## 3. Projective endpoint inequality

Let

    Q_1 = I - e e^T.

Although the legal protocol class uses s<1, one may take s->1^- in the Bellman inequality because V_* is finite and continuous.

For every x, writing a=e^T x,

    V_*(x) >= a^2 + V_*(Q_1 x).                          (3.1)

This is a limiting storage inequality for the projective reset. It is not an assertion that s=1 is itself a physically admitted measurement.

## 4. Convex interpolation lemma

For any legal 0<=s<1,

    Q_s x = (1-s)x + s Q_1 x.

By convexity of V_*,

    V_*(Q_s x)
      <= (1-s)V_*(x) + s V_*(Q_1 x).

Using (3.1),

    V_*(Q_s x)
      <= V_*(x) - s a^2.                                 (4.1)

Therefore the storage drop D_s(x)=V_*(x)-V_*(Q_s x) satisfies

    D_s(x) >= s (e^T x)^2.                               (4.2)

But the squared record is

    b^2 = s^2 (e^T x)^2.

Hence exactly,

    b^2 <= s D_s(x).                                     (4.3)

If s<=epsilon,

    b^2 <= epsilon D_s(x).                               (4.4)

This is the key step. It uses only finiteness/continuity of V_*, convexity, the projective endpoint inequality, and the affine identity for Q_s.

## 5. Arbitrary-sample theorem

**Theorem.** Assume V_* is finite. Then for every finite protocol pi with all measurement strengths s_j<=epsilon,

    ||C_pi x_0||_2^2 <= epsilon V_*(x_0).                (5.1)

Consequently,

    V_epsilon(x_0) <= epsilon V_*(x_0),                  (5.2)

and

    N_epsilon(x_0) <= sqrt(epsilon) N_*(x_0).            (5.3)

**Proof.**
Let z_j denote the state immediately before measurement j and x_j^+=Q_{s_j}z_j. Define

    D_j = V_*(z_j)-V_*(x_j^+).

By (4.4),

    b_j^2 <= epsilon D_j.

Between measurements, free flow cannot increase V_*. Thus the sum of all reset drops is bounded by the initial storage:

    sum_j D_j <= V_*(x_0)-V_*(x_N^+) <= V_*(x_0).

Therefore

    sum_j b_j^2
      <= epsilon sum_j D_j
      <= epsilon V_*(x_0).

Taking the supremum over all finite epsilon-weak protocols gives (5.2), and square roots give (5.3). QED.

## 6. Uniform operator ceiling

Finite-dimensionality and finiteness of N_* imply

    C_* := sup_{||x||_2=1} N_*(x) < infinity.

For every epsilon-weak finite protocol,

    ||C_pi||_op <= sqrt(epsilon) C_*.                    (6.1)

Thus arbitrary growth of the number of measurements cannot create an O(1) record operator from individually vanishing-strength measurements whenever the full fixed-e protocol family has a finite ceiling.

This is strictly more general than the preceding ellipsoidal result. If an ellipsoidal certificate P exists, the earlier sharper subclass-specific coefficient

    epsilon/(2-epsilon)

may improve the numerical constant. The present theorem sacrifices that coefficient in exchange for eliminating the quadratic-storage hypothesis.

## 7. Sharpness of the exponent

Take the scalar model

    n=1, G=0, e=1.

For repeated zero-wait measurements of common strength s=epsilon,

    b_j = s(1-s)^{j-1}x_0.

Hence

    sup_N sum_{j=1}^N b_j^2
      = [s/(2-s)] x_0^2.

The unrestricted all-protocol value is

    V_*(x_0)=x_0^2.

Therefore

    V_epsilon(x_0)/V_*(x_0)
      = epsilon/(2-epsilon)
      ~ epsilon/2.

So no universal replacement of (5.2) by o(epsilon)V_*(x) is possible. Correspondingly, the universal weak-record norm scale Theta(sqrt(epsilon)) is sharp.

The constant 1 in (5.2) is not claimed sharp for the full nonquadratic class.

## 8. Exact recovery conditioning

Let a declared nonzero linear target m^T x_0 be exactly reconstructed from a particular epsilon-weak record by a linear rule w^T C_pi x_0, i.e.

    C_pi^T w = m.

Then, whenever such exact reconstruction exists,

    ||m||
      <= ||C_pi|| ||w||
      <= sqrt(epsilon) C_* ||w||,

so

    ||w|| >= ||m|| / (sqrt(epsilon) C_*).                (8.1)

Thus exact inverse gain is necessarily Omega(epsilon^{-1/2}), uniformly over arbitrary finite sample count and timing.

If deterministic record error obeys ||eta||_2<=delta, exact-unbiased recovery carries worst-case error at least

    delta ||m|| / (sqrt(epsilon) C_*).                   (8.2)

This is a statement about exact inversion, not minimax risk: abstention or regularized recovery can remain bounded.

## 9. LT5 bounded-gain consequence

For a source-matched terminal target m_pi and a separately declared actuator sensitivity a_pi, LT5's bounded-gain class gives

    J_kappa(pi)
      = min_{||w||<=kappa||a_pi||}
          [ R||m_pi-C_pi^T w|| + delta||w|| ].

Using (6.1),

    J_kappa(pi)
      >= R [ ||m_pi||
             - kappa||a_pi|| C_* sqrt(epsilon) ]_+.       (9.1)

If ||a_pi||<=A uniformly, then relative to the do-nothing value J_0(pi)=R||m_pi||,

    0 <= J_0(pi)-J_kappa(pi)
       <= R kappa A C_* sqrt(epsilon).                   (9.2)

This holds uniformly over every finite epsilon-weak protocol.

Hence, within this decision class,

    ARBITRARILY MANY WEAK MEASUREMENTS
    + FIXED BOUNDED ACTUATOR GAIN
    !=
    NONVANISHING GUARANTEED TARGET IMPROVEMENT

unless another quantity such as actuator sensitivity, allowed gain, noise model or physical cost is itself permitted to scale with epsilon.

## 10. Firewalls

FINITE ALL-PROTOCOL STORAGE
    => VANISHING WEAK-PROTOCOL L2 ENERGY.

MANY WEAK MEASUREMENTS
    != O(1) ROBUST INFORMATION AUTOMATICALLY.

EXACT QUOTIENT SEPARATION
    != UNIFORM CONDITIONING.

N->INFINITY THROUGH FINITE PROTOCOLS
    != FREE INFORMATION.

NONQUADRATIC V_*
    != FAILURE OF THE WEAK CEILING.

TARGET ERASURE BY BACKACTION
    != ACTUATOR CONTROL SUCCESS.

L2 RECORD CEILING
    != L_INFINITY CEILING.

CLASSICAL FIXED-e RESET FLOW
    != QUANTUM INSTRUMENT.

BOUNDED OPERATOR GAIN
    != HARD AMPLITUDE / ENERGY CONSTRAINT.

The result does not establish a quantum realization, a DTC/IDG transfer, or a physical law.

## 11. Mature-host subtraction

The argument is a short dissipativity/available-storage plus convexity theorem. Its ingredients are mature: extremal storage, convex seminorm geometry, telescoping dissipation, and elementary optimal-recovery conditioning.

No novelty claim is made. The material value is claim-local: it removes an unnecessary ellipsoidal hypothesis from the project's fixed-sensor weak-measurement obstruction and closes a previously explicit residual.

## 12. Disposition

NONQUADRATIC_WEAK_STORAGE_RESIDUAL = CLOSED.

If V_* is finite:

    V_epsilon <= epsilon V_*,
    N_epsilon <= sqrt(epsilon) N_*.

UNIVERSAL RATE:
    energy Theta(epsilon) is sharp in order;
    record norm Theta(sqrt(epsilon)) is sharp in order.

ELLIPSOIDAL P RESULT:
    retained as a sharper coefficient subclass, not required for vanishing.

EXACT RECOVERY:
    gain >= Omega(epsilon^{-1/2}).

LT5 FIXED BOUNDED GAIN:
    guaranteed improvement over do-nothing <= O(sqrt(epsilon)).

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
NO_NEW_TASK.
