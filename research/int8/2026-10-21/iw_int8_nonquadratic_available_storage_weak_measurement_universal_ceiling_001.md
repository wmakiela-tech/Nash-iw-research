---
artifact_id: IW_INT8_NONQUADRATIC_AVAILABLE_STORAGE_WEAK_MEASUREMENT_UNIVERSAL_CEILING_001_20261021
date: 2026-10-21
from_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
class: CROSS_FRONT_EXACT_CONDITIONAL_BRIDGE / UNRESOLVED_DEPENDENCY_CLOSURE / NO_NOVELTY
status: DERIVATION_CHECKED_IN_DECLARED_MODEL / INDEPENDENT_REFEREE_NOT_PERFORMED
exposure: PUBLIC
source_artifacts:
  - research/geeky-s10/2026-10-19/geeky_s10_fixed_sensor_available_storage_001.md
  - research/geeky-s10/2026-10-21/geeky_s10_int8_weak_measurement_accumulation_ceiling_001.md
  - research/geeky-s10/2026-10-21/geeky_s10_fixed_time_reset_passive_sample_triangular_equivalence_001.md
  - research/int8/2026-10-21/iw_int8_weak_protocol_quotient_identification_vs_bounded_actuation_bridge_001.md
  - research/lt5/2026-10-20/lt5_target_information_vs_actuation_bounded_feedback_exact_gate_001.md
claim_ceiling: EXACT_CONDITIONAL_MATH / CLASSICAL_FINITE_DIMENSIONAL / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
bw_ingestion: UNKNOWN
---

# INT8 / Rotation 003 — Uniform weak-shot ceiling from finite *nonquadratic* available storage

## 0. Material cross-front delta

Geeky-S10's 2026-10-21 accumulation theorem established an all-finite-sample bound for weak fixed-e reset measurements **conditional on a quadratic ellipsoidal certificate** P>=0, Pe=e, G^T P+PG<=0:

    sum b_j^2 <= [epsilon/(2-epsilon)] x_0^T P x_0.

Its explicit remaining question was whether **finiteness of the general extremal storage V_***, even when no quadratic P is known, suffices to make the maximum weak-protocol output energy vanish as the per-shot strength epsilon tends to zero.

**Result:** YES, for this exact finite-dimensional deterministic classical fixed-e reset-flow model. The weaker but still order-sharp coefficient epsilon follows directly from convexity of V_* and its Bellman inequality, without a quadratic P.

This is a mathematical cross-front closure of a local question, not a novelty claim: convex-storage/dissipativity arguments are mature host mathematics. The result does NOT prove that a quadratic P is necessary or construct a quantum instrument.

## 1. Definitions, exact quantifiers

Let X=R^n, G a fixed real n x n matrix, e a fixed Euclidean unit vector, and E_tau=exp(G tau) for tau>=0.

At any measurement of strength s in [0,1), write

    Q_s = I - s e e^T,
    b=s e^T x^-,
    x^+=Q_s x^-.

Measurements are finite in number; wait intervals are nonnegative. For any deterministic protocol pi, its entire record is a linear map C_pi x_0. Let the **unrestricted-strength** available storage be

    V_*(x) = sup_{finite legal protocols pi} ||C_pi x||_2^2,

where strengths in each candidate pi may range over the whole [0,1) and the empty protocol is admitted.

ASSUMPTION F: V_*(x)<infinity for every x in R^n. From Geeky-S10 this is equivalent in finite dimension to a finite protocol-independent l2 ceiling; V_* is continuous, convex, 2-homogeneous, nonnegative, and is the supremum of quadratic protocol Gramians.

Define

    M_* = max_{||x||=1} V_*(x) < infinity.

Unless the sensor output is identically zero, M_*>0.

For 0<=epsilon<1, a **restricted weak protocol** is any finite pi with every strength 0<=s_j<=epsilon. The count, times and individual strengths are arbitrary but the sensor e and generator G are fixed.

## 2. Fundamental convex-storage inequality

**Lemma (strong-reset limit and convex interpolation).** Under F, for every x and s in [0,1):

    V_*(Q_s x) <= V_*(x) - s(e^T x)^2.                 (L1)

**Proof.** For every 0<=t<1, prepend an immediate measurement of strength t to an arbitrary continuation. Taking the supremum over continuations gives the Bellman inequality

    V_*(x) >= t^2(e^T x)^2+V_*(Q_t x).                 (2.1)

Although a full reset t=1 is not admitted by the strict-strength convention, Q_t x->Q_1 x and V_* is continuous by F. Let t increase to 1:

    V_*(x) >= (e^T x)^2+V_*(Q_1 x).                    (2.2)

The affine reset identity

    Q_s x=(1-s)x+s Q_1 x

and convexity of V_* imply

    V_*(Q_s x)
      <=(1-s)V_*(x)+s V_*(Q_1 x)
      <=V_*(x)-s(e^T x)^2.

That is (L1). QED.

**Scope:** the conclusion uses *exactly* the convex value function for all future legal protocols. It need not be an ellipsoid or differentiable; no P, gradient or Lyapunov matrix is assumed.

## 3. Universal arbitrary-sample weak bound

**Theorem.** Under F, for every finite restricted weak protocol pi with max_j s_j<=epsilon and every initial x_0,

    ||C_pi x_0||_2^2 = sum_j b_j^2 <= epsilon V_*(x_0).  (T1)

Consequently,

    ||C_pi||_op <= sqrt(epsilon M_*),                   (T2)

UNIFORMLY over arbitrary finite number of measurements, waiting times, and legal choices of strengths bounded by epsilon.

**Proof.** For the j-th measurement write a_j=e^T x_j^-. Then b_j=s_j a_j. From Lemma (L1),

    V_*(x_j^-) - V_*(x_j^+) >= s_j a_j^2.

Hence

    b_j^2=s_j^2 a_j^2
          <=epsilon s_j a_j^2
          <=epsilon [V_*(x_j^-)-V_*(x_j^+)].          (3.1)

The ability to prepend arbitrary free waiting implies the other Bellman inequality

    V_*(E_tau x)<=V_*(x)                              (3.2)

for every tau>=0. Therefore the sum of all nonnegative measurement drops, including the nonnegative free-flow storage drops between measurements, is at most V_*(x_0), because V_*>=0 at the final state. Sum (3.1) to obtain (T1). Supremizing over ||x_0||=1 gives (T2). QED.

**Logical contribution:** the existence of one quadratic dissipativity matrix P is NOT necessary for *this implication*. The assumption is the finite nonquadratic V_* itself. No converse, characterization of finite V_*, or quadratic necessity is claimed.

## 4. Relation to and distinction from Geeky-S10's ellipsoidal theorem

When an admissible quadratic P exists, Geeky-S10 proves the **stronger constant**:

    sum b_j^2 <= epsilon/(2-epsilon) * x_0^T P x_0.   (4.1)

Since its certificate also implies V_*(x)<=x^T P x, our universal estimate

    sum b_j^2 <= epsilon V_*(x_0)

is generally weaker in the certified quadratic subclass and is not a replacement for (4.1). At small epsilon the difference in coefficient is of order 2, but both imply the same sqrt(epsilon) record-norm scale.

An improved universal epsilon/(2-epsilon) coefficient with V_* replacing P is **NOT proved** here. Doing so would require extra geometry/inequalities beyond the convex Bellman argument.

**Sharpness in *order*.** In the scalar G=0,e=1 model, for all-strength available storage V_*(x)=x^2 (as a one-shot strength approaches 1). For N repeated shots of strength epsilon and zero waiting,

    sum_{j=1}^N b_j^2
      = [epsilon/(2-epsilon)]
        [1-(1-epsilon)^(2N)] x_0^2.

The supremum over finite N approaches epsilon/(2-epsilon)*V_*(x_0). Hence an o(epsilon) uniform energy bound would fail already for this scalar member. The O(sqrt(epsilon)) restricted readout norm is therefore universally order-sharp, although the constant epsilon in (T1) need not be optimal.

**Independent arithmetic sanity control:** at epsilon=0.17, the scalar all-finite-N limit is 0.17/(2-0.17)=0.09289617 times x_0^2, below the generic upper bound 0.17*x_0^2.

## 5. Recovery and LT5 bounded-gain consequences (typed)

For a specified nonzero initial-state target m and a protocol satisfying C_pi^T w=m, exact linear recovery must have

    ||w|| >= ||m|| / sqrt(epsilon M_*)                 (5.1)

if M_*>0. In particular no fixed finite gain can recover an unchanged nonzero target exactly for all sufficiently weak strengths, even when measurement count scales arbitrarily with epsilon. This is an **absolute inverse-gain** statement, not a claim of diverging relative matrix condition number.

For **separately declared** classical LT5 terminal actuation, use the post-reset forward map Phi_pi to define the physically source-matched target m_pi=Phi_pi^T ell and the actual terminal actuation port a_pi. Only with this matched source model and independent l2 uncertainty balls

    ||x_0||<=R, ||eta||<=delta

and static linear feedback ||F||<=kappa is LT5's formula legal:

    J_kappa(pi)
      =min_{||w||<=kappa||a_pi||}
         [R||m_pi-C_pi^T w||+delta||w||].

Combining (T2) with the reverse triangle inequality and the do-nothing controller yields

    0<=R||m_pi||-J_kappa(pi)
      <= R kappa ||a_pi|| sqrt(epsilon M_*).          (5.2)

If ||a_pi||<=A uniformly over protocols, the maximum guaranteed *improvement over do nothing for that same protocol and physical target* is O(sqrt(epsilon)), uniformly over all finite shot counts and times. If the physical target itself tends to zero because the measurements erase it, that is TARGET ERASURE, not a demonstration of successful actuation.

The argument does NOT cover LT5's separate nonlinear hard-amplitude control class, nor do deterministic inverse-gain inequalities by themselves establish a Gaussian minimax risk bound.

## 6. New negative knowledge and boundary conditions

CLOSED CONDITIONAL QUESTION:
    GENERAL_FINITE_VSTAR_PLUS_FIXED_e_RESET
    => UNIFORM_WEAK_RECORD_ENERGY_O(epsilon)
       WITHOUT_QUADRATIC_STORAGE.

NOT CONCLUDED:
    FINITE_VSTAR => EXISTS_P (quadratic necessity remains OPEN).
    VSTAR_IS_HILBERTIAN.
    SHARP_UNIVERSAL_COEFFICIENT epsilon/(2-epsilon) * VSTAR.
    INFORMATION_GAIN_TO_PHYSICAL_CONTROL_WITHOUT_PORTS.
    GENERAL_ADAPTIVE/QUANTUM_INSTRUMENT OR PHYSICAL INTERPRETATION.
    L2_CEILING => PER_SHOT_NOISE_LINFINITY DECISION CEILING.

Explicit scope of failure / retyping:
- V_* must be finite for every initial state; a nonnormal stable free flow can still have unbounded all-protocol storage, so free Hurwitz stability alone is insufficient.
- e and G fixed; scalar normalized output equals the very same rank-one state component removed by the reset.
- finite deterministic protocols and their linear outputs; outcome-dependent stochastic state laws are not modeled.
- all-strength comparison 0<=s<1 must be legal when defining V_*; an externally strength-restricted V_{*,epsilon} cannot be substituted in the strong-reset-limit step.
- the target/actuator limit requires source-matched m_pi and uniformly bounded gain/port; hard-amplitude control, continuously resupplied state, repeated *independent preparations*, and variable gamma/noise scaling are distinct problems.
- no DTC/NCDG, pseudospectral, PBH, or quantum physical transfer is claimed.

## 7. Mature-host subtraction and disposition

The proof is the convex-storage/Bellman/dissipativity calculus of standard control and available-storage theory; it should be treated as a specialized comparison inequality, not a novel theorem family. Relevant project hosts are the Geeky-S10 V_* characterization, classical dissipativity (Willems, 1972), set-membership optimal recovery and LT5 robust output-feedback. No exhaustive prior-art survey or independent referee approval was performed.

**Project-specific delta:** Geeky-S10's explicit OPEN clause "does finite nonquadratic V_* alone imply a vanishing restricted-strength ceiling?" receives a POSITIVE exact answer within the frozen fixed-e classical model. It strengthens the scientific integration chain from the INT8 weak-protocol quotient proof through Geeky-S10's exact triangular factorization and quadratic dissipation theorem, without modifying any physical claim.

GITHUB_STORED does not imply BW_INGESTED or OWNER_ACCEPTED.
NO_NEW_TASK_CASCADE.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
