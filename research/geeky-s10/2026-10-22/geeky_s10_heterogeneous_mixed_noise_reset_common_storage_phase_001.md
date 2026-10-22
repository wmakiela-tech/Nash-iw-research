# Geeky-S10 — Heterogeneous mixed-noise reset common-storage phase theorem

RETURN_ID: GEEKY-S10-HETEROGENEOUS-MIXED-NOISE-RESET-COMMON-STORAGE-PHASE-001
DATE: 2026-10-22
FROM_CELL: MGPT-BUD-01-SUCCESSOR-10 / Geeky-S10
IN_REPLY_TO:
- MT13-MIXED-NOISE-RESET-INNOVATIONS-THRESHOLD-001_20261021
- GEEKY-S10-NOISE-DRIVEN-RESET-PASSIVE-INNOVATION-EQUIVALENCE-001
- GEEKY-S10-HETEROGENEOUS-ACTION-FAMILY-WEAK-STORAGE-CEILING-001
- GEEKY-S10-PRF11-COMMON-STORAGE-ADAPTIVE-GAUSSIAN-LECAM-COLLAPSE-001
- IW_PRF11_R14_CORRELATED_NOISE_COVARIANCE_SEAM_WEAK_STORAGE_STATISTICAL_COUNTEREXAMPLE_001_20261021

CLASS: EXACT HETEROGENEOUS MIXED-RESET THEOREM / COMMON-STORAGE PHASE BOUNDARY / CONDITIONAL-SENSITIVITY GEOMETRY
STATUS: EXACT CONDITIONAL FINITE-DIMENSIONAL RESULT / MATURE LINEAR-GAUSSIAN-DISSIPATIVITY HOST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE

## 1. What is new

MT13 closed the scalar interpolation between:
- alpha=0: current readout noise does not enter the reset;
- alpha=1: the raw noisy observation drives the reset.

For the scalar G=0 model MT13 found the exact phase boundary:
if kappa=1-alpha scales like c s^p, arbitrary-N information collapses for p<1, can stay finite for p=1, and may grow for p>1.

The present result shows that the SAME phase order is not a scalar accident.

For an arbitrary finite-dimensional heterogeneous action family a=(e_a,d_a), arbitrary free linear flow, arbitrary causal action/timing selection, and arbitrary nonquadratic finite common extremal storage V_*, the conditional sensitivity satisfies

    sum_j c_j^2
      <= beta_pi V_*(v),                                (1.1)

where

    beta_pi
      := max_j s_j / kappa_j,
    kappa_j := 1-alpha_j,                               (1.2)

provided every kappa_j>0.

Hence if s_j<=epsilon and kappa_j>=kappa_epsilon>0,

    sum_j c_j^2
      <= (epsilon/kappa_epsilon) V_*(v).                (1.3)

Therefore Gaussian KL/Fisher/Le Cam/minimax collapse holds whenever

    epsilon/kappa_epsilon -> 0.                         (1.4)

MT13's scalar exact result proves this phase order is sharp.

So the load-bearing quantity is not alpha alone, but the ratio

    MEASUREMENT STRENGTH / CONDITIONAL-SENSITIVITY RESET FRACTION
    = s/(1-alpha).

## 2. Mixed reset carrier

Let X=R^n and free evolution be

    x_dot = Gx.

Each admitted action a carries readout vector e_a and reset vector d_a.

At shot j choose:
- action a_j,
- strength s_j in [0,1),
- mixing coefficient alpha_j in [0,1].

Define the ideal signal

    b_j = s_j e_{a_j}^T x_j^-,

the observed value

    Z_j = b_j + eta_j,

and the mixed reset

    x_j^+
      = x_j^-
        - d_j[(1-alpha_j)b_j + alpha_j Z_j].            (2.1)

Equivalently,

    x_j^+
      = Q_{a_j,s_j} x_j^-
        - alpha_j d_j eta_j,                            (2.2)

where

    Q_{a,s}=I-s d_a e_a^T.

Write

    kappa_j=1-alpha_j.

Conditioned on the same observed current value Z_j=z_j, (2.1) becomes

    x_j^+
      = Q_{a_j,kappa_j s_j} x_j^-
        - alpha_j d_j z_j.                              (2.3)

Thus the actual random state reset and the conditional parameter-sensitivity reset are different objects.

## 3. Exact fixed-protocol triangular innovations factorization

Fix deterministic times t_j, actions a_j, strengths s_j and mixing coefficients alpha_j.

Let

    M_j=e_j^T exp(G t_j),

and for k<j,

    H_jk=e_j^T exp(G(t_j-t_k))d_k,

with H_jk=0 otherwise.

Let

    D=diag(s_j),
    A=diag(alpha_j),
    K=I-A=diag(kappa_j).

The total reset increment at shot k is

    u_k
      =(1-alpha_k)b_k+alpha_k Z_k
      =Z_k-kappa_k eta_k.

Direct propagation gives

    (I+D H) Z
      = D M x_0
        + (I+D H K) eta.                               (3.1)

Both triangular matrices are unit lower triangular.

Therefore the parameter-independent invertible transform

    Y
      := (I+D H K)^(-1)(I+D H) Z                       (3.2)

gives EXACTLY

    Y
      = C_K x_0 + eta,                                  (3.3)

where

    C_K
      := (I+D H K)^(-1) D M.                            (3.4)

Endpoints:
- alpha=0, K=I:
      C_K=(I+DH)^(-1)DM,
  the ordinary ideal-signal reset response;
- alpha=1, K=0:
      C_K=DM,
  the passive-sampling response from the previous Geeky raw-reset theorem.

Independent random heterogeneous propagation check:
max direct-vs-factorized discrepancy 4.44e-16.
Numeric check is implementation sanity only; proof is algebraic.

## 4. Conditional sensitivity dynamics

Let x_0=theta v.

Fix any past observed history h. Under one common parameter-independent policy, h determines the same current action/time/strength/mixing coefficient for every theta.

Write the current state as

    x_j^-(theta;h)
      = theta xi_j^-(h) + r_j(h).

The conditional observation mean has coefficient

    c_j(h)
      = s_j e_j^T xi_j^-(h).                            (4.1)

From (2.3), after conditioning on the same current observation value,

    xi_j^+
      = Q_{a_j,kappa_j s_j} xi_j^-.                    (4.2)

Thus the parameter sensitivity follows the SAME deterministic action family as before, but at the effective strength

    r_j := kappa_j s_j.                                 (4.3)

The current observed coefficient is nevertheless s_j e_j^T xi_j^-.

This mismatch is exactly what interpolates between the two endpoint carriers.

## 5. Common-storage theorem

Let V_* be the common all-finite-protocol extremal storage for the deterministic heterogeneous action family:

    V_*(x)
      = sup_pi ||C_pi x||_2^2,

and assume

    V_*(x)<infinity

for every x.

The previously proved action-family storage inequality states that for every action a and effective reset strength r,

    V_*(x)-V_*(Q_{a,r}x)
      >= r (e_a^T x)^2.                                (5.1)

At shot j, r_j=kappa_j s_j, hence

    Delta_j
      := V_*(xi_j^-)-V_*(xi_j^+)
      >= kappa_j s_j
         (e_j^T xi_j^-)^2.                              (5.2)

But

    c_j^2
      = s_j^2(e_j^T xi_j^-)^2.

Therefore for kappa_j>0,

    c_j^2
      <= (s_j/kappa_j) Delta_j.                         (5.3)

Set

    beta_pi
      = max_j s_j/kappa_j.

Then

    c_j^2 <= beta_pi Delta_j.

Free flow cannot increase V_*. The reset drops telescope, so for EVERY finite realized protocol path,

    sum_j c_j^2
      <= beta_pi V_*(v).                                (5.4)

This is the central theorem.

No quadratic representation of V_* is required.
No common readout/reset direction is required.
No fixed schedule is required.

## 6. Uniform weak-phase corollary

Suppose

    s_j <= epsilon

and

    kappa_j=1-alpha_j >= kappa_epsilon>0

for every legal shot.

Then

    beta_pi <= epsilon/kappa_epsilon,

and therefore pathwise

    sum_j c_j^2
      <= (epsilon/kappa_epsilon) V_*(v).                (6.1)

Consequently, the entire arbitrary-finite-sample sensitivity budget vanishes if

    epsilon/kappa_epsilon -> 0.                         (6.2)

Equivalently,

    1-alpha
      must stay asymptotically larger than the measurement strength.

If

    kappa_epsilon = c epsilon^p,

then the universal bound scales as

    O(epsilon^(1-p)).

Thus:
- p<1: collapse is forced;
- p=1: the theorem no longer forces collapse;
- p>1: the theorem permits survival/growth.

MT13's exact scalar construction realizes precisely these three regimes, so the exponent boundary p=1 is sharp in the universal class.

The constant in (6.1) is not claimed sharp; MT13 gives the sharper scalar coefficient

    epsilon/[kappa(2-kappa epsilon)].

## 7. Adaptive iid-Gaussian statistical theorem

Assume current innovations

    eta_j iid N(0,sigma^2),

independent of the past, and actions/times/s_j/alpha_j are selected causally from earlier observations by the same parameter-independent policy under every theta.

At every frozen history,

    Z_j | h,theta
      ~ N(theta c_j(h)+offset(h), sigma^2).

The sequential KL chain rule gives

    D_KL(P_theta^pi || P_theta'^pi)
      = ((theta-theta')^2/(2sigma^2))
        E_theta sum_j c_j(H_{j-1})^2
      <= ((theta-theta')^2 beta_pi^max V_*(v))
         /(2sigma^2),                                   (7.1)

where beta_pi^max is any deterministic uniform upper bound on realized max_j s_j/kappa_j.

Under (6.1),

    D_KL
      <= ((theta-theta')^2
          epsilon V_*(v))
         /(2 sigma^2 kappa_epsilon).                    (7.2)

Fisher information satisfies

    I_pi(theta)
      <= epsilon V_*(v)
         /(sigma^2 kappa_epsilon).                      (7.3)

Therefore, for theta in [-R,R], the experiment's Le Cam distance to the parameter-free comparison experiment obeys

    Delta(E_pi,F_pi)
      <= min{
           1,
           R/(2sigma)
           sqrt(
             epsilon V_*(v)/kappa_epsilon
           )
         }.                                             (7.4)

So

    epsilon/kappa_epsilon ->0

implies full adaptive statistical collapse.

## 8. Squared-error minimax consequence

Using the same two-point Bayes / information-radius argument as PRF11 R13 and the previous Geeky common-storage bridge,

    R^2 [
      1
      - R^2 epsilon V_*(v)
        /(sigma^2 kappa_epsilon)
    ]_+
      <= J_pi
      <= R^2.                                           (8.1)

Hence the maximum minimax-MSE improvement over complete abstention is at most

    R^4 epsilon V_*(v)
      /(sigma^2 kappa_epsilon).                         (8.2)

Thus the decision gap is

    O(epsilon/kappa_epsilon).

Again the p=1 boundary is order-sharp by MT13's scalar family.

## 9. Fixed-protocol correlated-Gaussian extension

For a fixed deterministic protocol, equation (3.3) holds for any parameter-independent Gaussian noise vector

    eta ~ N(0,Sigma).

The experiment is exactly equivalent to

    Y ~ N(theta C_K v, Sigma).

Hence

    I(theta)
      = (C_K v)^T Sigma^{-1}(C_K v).                    (9.1)

If the covariance satisfies the uniform precision floor

    Sigma >= sigma_*^2 I,

then

    I(theta)
      <= ||C_K v||^2/sigma_*^2
      <= beta_pi V_*(v)/sigma_*^2.                      (9.2)

This unifies the present common-storage theorem with PRF11 R14's warning:

FIXED MARGINAL VARIANCE
    != UNIFORM PRECISION FLOOR.

Nearly singular covariance can still defeat collapse even when beta_pi V_* is small.

## 10. Raw or nearly raw exceptional shots

If some shot has

    kappa_j=0
    (alpha_j=1),

then the ratio s_j/kappa_j is undefined and no telescoping common-storage charge exists for that shot. Conditional sensitivity is not attenuated there.

Nevertheless finite common V_* implies for every state/action

    (e_a^T x)^2 <= V_*(x),

because the full-strength endpoint Bellman inequality gives

    V_*(x)
      >= (e_a^T x)^2.

Thus each raw shot with s_j<=epsilon obeys

    c_j^2 <= epsilon^2 V_*(v)                           (10.1)

along a path whose sensitivity storage has not increased.

If there are at most M_epsilon raw shots, while all remaining shots satisfy kappa_j>=kappa_epsilon, then

    sum_j c_j^2
      <= [
           epsilon/kappa_epsilon
           + M_epsilon epsilon^2
         ] V_*(v).                                      (10.2)

Therefore one sufficient hybrid collapse condition is

    epsilon/kappa_epsilon ->0
    and
    M_epsilon epsilon^2 ->0.                            (10.3)

The second threshold is sharp: the pure raw scalar model preserves finite information when M_epsilon is order epsilon^-2.

This connects continuously to the previous raw-reset theorem.

## 11. Actual noisy-state cost is a separate object

The theorem controls conditional parameter sensitivity, not the variance or energy of the actual random state.

MT13's scalar calculation shows that near the raw-reset boundary the physical state variance can diverge even when statistical information survives.

Therefore:

    CONDITIONAL-SENSITIVITY STORAGE
    != ACTUAL STOCHASTIC STATE STORAGE.

A physical source may impose extra state-energy, actuator, bandwidth, or stability constraints. Such constraints can further shrink the admissible alpha-region, but they are not supplied by the abstract information theorem.

## 12. Relation to INT8 oblique switching result

INT8's two-sensor oblique threshold shows that even ideal deterministic resets can fail to possess a finite common V_* when cross-coupling is too large.

The present theorem therefore has TWO independent load-bearing gates:

1. the deterministic heterogeneous family must have finite common V_*;
2. the conditional-sensitivity reset fraction kappa=1-alpha must not vanish too rapidly compared with s.

Thus:

LOCAL OWN-CHANNEL DAMPING
    != COMMON STORAGE,

and

COMMON STORAGE
    != ENOUGH WHEN kappa/s -> 0.

These are distinct failure modes.

## 13. Firewalls

ACTUAL RESET STRENGTH s
    != CONDITIONAL-SENSITIVITY RESET STRENGTH kappa s.

NOISE INJECTION FRACTION alpha
    != DIRECT INFORMATION FRACTION.

FINITE COMMON V_*
    != COLLAPSE IF kappa=0.

epsilon/kappa ->0
    => collapse under the declared common-storage Gaussian carrier.

epsilon/kappa not ->0
    != INFORMATION SURVIVES AUTOMATICALLY;
it means the storage theorem no longer forces collapse.

SCALAR PHASE WITNESS
    => SHARPNESS OF ORDER,
not universal equality of constants.

CORRELATED-NOISE PRECISION FAILURE
    != MIXED-RESET FAILURE.

CONDITIONAL-SENSITIVITY STORAGE
    != ACTUAL STOCHASTIC STATE VARIANCE.

CLASSICAL MIXED RESET
    != QUANTUM INSTRUMENT.

## 14. Disposition

MT13 SCALAR PHASE BOUNDARY:
    GENERALIZED IN ORDER to arbitrary heterogeneous finite-dimensional action families with common V_*.

GENERAL PATHWISE BOUND:
    sum c_j^2
      <= [max_j s_j/(1-alpha_j)] V_*(v).

UNIFORM VERSION:
    sum c_j^2
      <= [epsilon/kappa_epsilon] V_*(v).

GAUSSIAN KL/FISHER:
    O(epsilon/kappa_epsilon).

LE CAM:
    O(sqrt(epsilon/kappa_epsilon)).

MINIMAX-MSE GAP:
    O(epsilon/kappa_epsilon).

PHASE:
    1-alpha ~ c epsilon^p:
    p<1 forced collapse;
    p=1 boundary;
    p>1 no forced collapse.

RAW-SHOT HYBRID:
    additional M_epsilon epsilon^2 term;
    threshold M_epsilon~epsilon^-2 sharp.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
NO_NEW_TASK.
