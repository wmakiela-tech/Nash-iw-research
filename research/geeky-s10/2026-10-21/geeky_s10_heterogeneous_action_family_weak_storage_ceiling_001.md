# Geeky-S10 — Heterogeneous reset/readout action-family weak-storage theorem

RETURN_ID: GEEKY-S10-HETEROGENEOUS-ACTION-FAMILY-WEAK-STORAGE-CEILING-001
DATE: 2026-10-21
FROM_CELL: MGPT-BUD-01-SUCCESSOR-10 / Geeky-S10
IN_REPLY_TO:
- GEEKY-S10-FIXED-SENSOR-NONQUADRATIC-WEAK-STORAGE-CEILING-001
- IW_REC10_ROT04_DETERMINISTIC_RESET_CAUSAL_FACTORIZATION_HETEROGENEOUS_STRENGTHS_DIRECTIONS_REFEREE_001_20261021
- IW_INT8_NONQUADRATIC_AVAILABLE_STORAGE_WEAK_MEASUREMENT_UNIVERSAL_CEILING_001_20261021

CLASS: EXACT FINITE-DIMENSIONAL ACTION-FAMILY STORAGE THEOREM / HETEROGENEOUS READOUT-RESET DIRECTIONS / MISALIGNMENT SCOPE REPAIR
STATUS: EXACT CONDITIONAL RESULT / MATURE-HOST DISSIPATIVITY-CONVEXITY / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE

## 1. Trigger

REC10 proved an exact triangular factorization for predetermined heterogeneous measurement directions and reset directions, and supplied a decisive warning: the fixed-e quadratic weak-record ceiling cannot simply be exported to misaligned reset. Its exact falsifier uses

    G=0,
    e=(1,0)^T,
    d=(0,1)^T,

for which repeated measurements leave e^T x unchanged and therefore accumulate unbounded l2 record energy.

The question is whether **co-axiality itself** is the load-bearing hypothesis behind weak-measurement collapse.

It is not.

The correct abstract sufficient hypothesis is existence of a **finite common extremal storage for the whole admitted action family**. Under that hypothesis the previous nonquadratic weak-ceiling theorem extends verbatim to arbitrary predetermined heterogeneous readout/reset directions.

Thus:

    MISALIGNMENT != FAILURE OF WEAK CEILING AUTOMATICALLY.

The REC10 counterexample instead certifies that its admitted action family has

    V_* = infinity

for the chosen nonzero initial state.

## 2. Heterogeneous deterministic protocol class

Let X=R^n. Free evolution between measurement events is

    x_dot = Gx.

Let A be any prescribed family of measurement/reset actions. An action a in A carries:

    readout vector e_a in R^n,
    reset vector d_a in R^n.

At strength 0<=s<1, define

    b = s e_a^T x^-,
    x^+ = Q_{a,s} x^-,
    Q_{a,s} = I - s d_a e_a^T.

No co-axiality, orthogonality, normalization, or common direction is assumed unless separately stated.

A deterministic finite protocol pi consists of:
- finitely many nonnegative waiting times;
- a predetermined action sequence a_1,...,a_N in A;
- strengths s_1,...,s_N in [0,1).

For each frozen protocol pi, the record is linear in x_0. Let C_pi x_0 be the finite l2 record vector.

Define the common action-family extremal seminorm and storage

    N_*(x) = sup_pi ||C_pi x||_2,
    V_*(x) = N_*(x)^2,

where the supremum is over the entire admitted deterministic finite protocol family, including all legal action choices and strengths.

Assume

    V_*(x) < infinity for every x in R^n.                 (2.1)

Because every C_pi is linear, N_* is then a finite seminorm; in finite dimension it is continuous. Hence V_* is finite, continuous, convex, and 2-homogeneous.

For 0<epsilon<1 define V_epsilon by restricting to protocols satisfying

    s_j <= epsilon

for every shot.

## 3. Common Bellman inequalities

Because the full protocol family permits an arbitrary legal waiting segment before any future protocol,

    V_*(exp(G tau)x) <= V_*(x)                            (3.1)

for every tau>=0.

Likewise, for every fixed action a and every 0<=s<1,

    V_*(x)
      >= s^2 (e_a^T x)^2
         + V_*(Q_{a,s}x).                                (3.2)

The endpoint s=1 need not itself be legal. Since V_* is continuous and

    Q_{a,s}x -> Q_{a,1}x
    as s->1^-,

taking the limit in (3.2) gives

    V_*(x)
      >= (e_a^T x)^2
         + V_*(Q_{a,1}x)                                 (3.3)

for every admitted action a.

This endpoint inequality is common to the entire heterogeneous action family.

## 4. Convex interpolation for every action

For every action a,

    Q_{a,s}
      = (1-s) I + s Q_{a,1}.                             (4.1)

Therefore, by convexity of V_*,

    V_*(Q_{a,s}x)
      <= (1-s)V_*(x) + s V_*(Q_{a,1}x).

Using (3.3),

    V_*(Q_{a,s}x)
      <= V_*(x) - s (e_a^T x)^2.                         (4.2)

Hence the storage drop caused by this particular, possibly misaligned, reset satisfies

    D_{a,s}(x)
      := V_*(x)-V_*(Q_{a,s}x)
      >= s (e_a^T x)^2.                                  (4.3)

The actual squared record is

    b^2 = s^2 (e_a^T x)^2,

so

    b^2 <= s D_{a,s}(x).                                 (4.4)

If s<=epsilon,

    b^2 <= epsilon D_{a,s}(x).                           (4.5)

No alignment relation between e_a and d_a appears in the proof.

## 5. Heterogeneous arbitrary-sample theorem

**Theorem.** Under assumption (2.1), every deterministic finite protocol pi using arbitrary actions a_j in A, arbitrary waiting times, and arbitrary strengths s_j<=epsilon satisfies

    ||C_pi x_0||_2^2
      <= epsilon V_*(x_0).                               (5.1)

Consequently,

    V_epsilon(x)
      <= epsilon V_*(x),                                 (5.2)

and

    N_epsilon(x)
      <= sqrt(epsilon) N_*(x).                           (5.3)

**Proof.**
At shot j, (4.5) gives

    b_j^2 <= epsilon
             [V_*(x_j^-)-V_*(x_j^+)].

Between shots, (3.1) implies that free flow cannot increase V_*. Summing all reset drops therefore telescopes against a nonincreasing storage trajectory:

    sum_j [V_*(x_j^-)-V_*(x_j^+)]
      <= V_*(x_0).

Thus

    sum_j b_j^2 <= epsilon V_*(x_0).

Taking the supremum over all epsilon-weak deterministic finite protocols gives (5.2), and square roots give (5.3). QED.

## 6. Uniform operator consequence

Since N_* is a finite seminorm in finite dimension,

    C_* := sup_{||x||_2=1} N_*(x) < infinity.

Therefore every epsilon-weak heterogeneous protocol obeys

    ||C_pi||_op <= sqrt(epsilon) C_*.                    (6.1)

This uniform bound is independent of:
- sample count;
- sample times;
- action order;
- heterogeneity of readout directions;
- heterogeneity of reset directions.

What matters is the common finite-storage hypothesis (2.1).

## 7. Exact placement of the REC10 misalignment counterexample

REC10 uses

    G=0,
    e=(1,0)^T,
    d=(0,1)^T,
    x_0=(1,0)^T.

For any fixed s>0,

    e^T x_j^- = 1

for every repeated shot, because the reset changes only the second state coordinate. Thus

    b_j=s

and

    sum_{j=1}^N b_j^2 = N s^2 -> infinity.

Therefore

    V_*(x_0)=infinity.                                   (7.1)

This does NOT contradict the heterogeneous theorem. It falsifies its load-bearing hypothesis.

The correct seam is therefore:

    MISALIGNED RESET
    !=
    WEAK-CEILING FAILURE AUTOMATICALLY,

but

    UNBOUNDED COMMON ACTION-FAMILY STORAGE
    =>
    NO STORAGE-BASED UNIFORM WEAK CEILING.

REC10's witness is a direct certificate of the latter.

## 8. Relation to REC10 triangular equivalence

For frozen deterministic times/actions/strengths, REC10 proves

    C=(I+D H)^(-1) D M,

with unit lower-triangular I+D H, so nonzero shot strengths preserve the passive-sampling rank/kernel.

That theorem and the present theorem answer different questions:

REC10:
    algebraic identifiability / rank / kernel.

Present result:
    robust l2 size / conditioning under a common finite action-family storage.

Therefore:

    TRIANGULAR RANK EQUIVALENCE
    !=
    STORAGE FINITENESS,

and

    EXACT ALGEBRAIC IDENTIFIABILITY
    !=
    UNIFORM ROBUST INFORMATION.

A protocol family may preserve passive rank for every finite prefix while its all-protocol storage is infinite.

## 9. Exact recovery and LT5 bounded-gain consequences

If a nonzero linear target m^T x_0 is exactly reconstructed from a particular epsilon-weak heterogeneous protocol,

    C_pi^T w = m,

then from (6.1)

    ||w|| >= ||m||/(sqrt(epsilon) C_*).                  (9.1)

Thus exact inverse gain remains Omega(epsilon^-1/2) uniformly over arbitrary heterogeneous deterministic finite protocols.

For the LT5 source-matched bounded-gain decision class,

    J_kappa(pi)
      = min_{||w||<=kappa||a_pi||}
          [R||m_pi-C_pi^T w|| + delta||w||],

if ||a_pi||<=A uniformly then

    0 <= J_0(pi)-J_kappa(pi)
       <= R kappa A C_* sqrt(epsilon).                   (9.2)

Again, action-direction heterogeneity does not alter the conclusion once a finite common V_* exists.

## 10. Practical quadratic sufficient certificate for one action

The general theorem does not require a quadratic storage. It is nevertheless useful to identify the exact local algebra behind quadratic dissipativity for one reset/readout pair.

Let P>=0 and Q_s=I-s d e^T. Then

    x^T P x - (Q_s x)^T P(Q_s x)
      = 2s(e^T x)(d^T P x)
        - s^2(d^T P d)(e^T x)^2.                        (10.1)

For the first-order term to be nonnegative for every x, it is necessary and sufficient that

    P d = alpha e                                        (10.2)

for some alpha>=0.

If alpha>0, then d^T P d=alpha e^T d and

    Delta_P
      = alpha s [2-s(e^T d)] (e^T x)^2.                 (10.3)

Hence whenever the bracket is positive,

    b^2
      <= s/[alpha(2-s e^T d)] Delta_P.                  (10.4)

For a heterogeneous family, one common quadratic P with actionwise

    P d_a = alpha_a e_a,

and a positive uniform lower bound on the resulting dissipation coefficient supplies a convenient explicit sufficient certificate.

This quadratic condition is NOT claimed necessary for finite nonquadratic V_*.

## 11. Causal action selection: pathwise extension

REC10's triangular factorization is stated for fixed deterministic times/actions because it is an operator identity for one frozen protocol. The weak-storage bound is more robust.

The one-step inequality

    b^2 <= epsilon
           [V_*(x^-)-V_*(x^+)]

holds for **every current state and every currently chosen legal action**. Therefore the telescoping proof does not require the future action sequence to have been selected in advance.

Consequently, in the same noiseless deterministic reset-flow carrier, actions, strengths and waiting times may be chosen causally as arbitrary functions of the previous exact record history, provided:
- every realized protocol terminates after finitely many shots;
- every chosen action belongs to the same admitted family A;
- every realized strength obeys s_j<=epsilon.

Along every realized trajectory,

    sum_j b_j^2 <= epsilon V_*(x_0).                     (11.1)

This extension does not require the adaptive input-output map to remain linear. The storage V_* used in the proof is still the common supremum over legal finite open-loop continuations; its Bellman inequalities hold pointwise for every legal first action, so any causally selected realized sequence inherits them.

What is NOT covered:
- reset maps driven by noisy measured values rather than the declared exact b;
- stochastic state noise;
- expected-cost policies with a different observation model;
- genuinely quantum instruments.

Thus:

    CAUSAL ACTION SELECTION
    !=
    ESCAPE FROM THE STORAGE BUDGET

inside the declared deterministic carrier.

No quantum-instrument interpretation follows from the classical reset map.

## 12. Firewalls

MISALIGNMENT != WEAK-CEILING FAILURE AUTOMATICALLY.

FINITE COMMON ACTION-FAMILY STORAGE
    => sqrt(epsilon) WEAK-RECORD COLLAPSE.

TRIANGULAR RANK EQUIVALENCE
    != FINITE STORAGE.

EXACT IDENTIFIABILITY
    != UNIFORM CONDITIONING.

HETEROGENEOUS DIRECTIONS
    != FREE INFORMATION.

UNBOUNDED STORAGE WITNESS
    != FAILURE OF EVERY FIXED FINITE PROTOCOL.

COMMON QUADRATIC P
    != NECESSARY FOR FINITE V_*.

CAUSAL ACTION SELECTION
    != ESCAPE FROM FINITE COMMON STORAGE.

NOISY/STOCHASTIC ADAPTATION
    != DECLARED DETERMINISTIC ADAPTATION.

CLASSICAL RESET MAP
    != QUANTUM MEASUREMENT INSTRUMENT.

## 13. Disposition

HETEROGENEOUS_ACTION_FAMILY_EXTENSION = PASS_EXACT under finite common V_*.

COAXIALITY = NOT LOAD-BEARING for the abstract nonquadratic weak ceiling.

REC10 MISALIGNED G=0 WITNESS:
    reclassified as V_*=infinity witness, not as proof that all misalignment defeats weak collapse.

UNIVERSAL WEAK RATE:
    V_epsilon <= epsilon V_*,
    N_epsilon <= sqrt(epsilon) N_*.

CAUSAL EXACT-RECORD ADAPTATION:
    covered pathwise for every finite realized protocol.

OPEN:
- noisy/stochastic feedback in which the reset itself depends on corrupted observations;
- source-valid noise/cost scaling and quantum instruments remain separate branches.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
NO_NEW_TASK.
