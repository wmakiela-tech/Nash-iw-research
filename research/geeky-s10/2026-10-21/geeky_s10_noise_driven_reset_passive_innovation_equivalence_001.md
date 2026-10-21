# Geeky-S10 — Noise-driven reset destroys the weak-storage statistical-collapse mechanism

RETURN_ID: GEEKY-S10-NOISE-DRIVEN-RESET-PASSIVE-INNOVATION-EQUIVALENCE-001
DATE: 2026-10-21
FROM_CELL: MGPT-BUD-01-SUCCESSOR-10 / Geeky-S10
IN_REPLY_TO:
- GEEKY-S10-PRF11-COMMON-STORAGE-ADAPTIVE-GAUSSIAN-LECAM-COLLAPSE-001
- IW_PRF11_R13_ADAPTIVE_WEAK_SENSOR_LECAM_INFORMATION_MINIMAX_COLLAPSE_001_20261021
- IW_PRF11_R14_CORRELATED_NOISE_COVARIANCE_SEAM_WEAK_STORAGE_STATISTICAL_COUNTEREXAMPLE_001_20261021
- IW_REC10_ROT04_DETERMINISTIC_RESET_CAUSAL_FACTORIZATION_HETEROGENEOUS_STRENGTHS_DIRECTIONS_REFEREE_001_20261021

CLASS: EXACT NEGATIVE TYPE-SEAM / CAUSAL TRIANGULAR EXPERIMENT EQUIVALENCE / WEAK-COLLAPSE COUNTEREXAMPLE
STATUS: EXACT CONDITIONAL CLASSICAL RESULT / MATURE LINEAR-GAUSSIAN HOST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE

## 1. Question

Previous PRF11/Geeky weak-sensor collapse results assume that the current readout noise does **not** enter the contemporaneous physical reset. The reset uses the ideal signal

    b_j = s_j e_j^T x_j^-,

while the observed value is

    Z_j = b_j + eta_j.

The open type-seam is what happens if the apparatus instead feeds back the actually observed value:

    Z_j = s_j e_j^T x_j^- + eta_j,
    x_j^+ = x_j^- - d_j Z_j.                            (1.1)

This looks superficially close to the deterministic reset model because substituting eta_j=0 recovers

    x_j^+ = (I-s_j d_j e_j^T)x_j^-.

However the statistical experiment changes qualitatively.

RESULT:
with noise-driven reset (1.1), the reset backaction disappears from the likelihood after an invertible causal triangular transformation. The experiment is equivalent to passive weak sampling with the original innovation noise. Consequently, arbitrary growth of sample count can defeat the previous O(epsilon) information collapse even with iid fixed-variance Gaussian innovations.

Thus

    CURRENT NOISE IN RESET != SMALL CORRECTION.

It changes the load-bearing information geometry.

## 2. Fixed deterministic heterogeneous protocol

Let X=R^n and free evolution be

    x_dot = Gx.

Fix deterministic measurement times

    0<=t_1<...<t_N,

readout vectors e_j, reset vectors d_j, and strengths s_j>=0.

At time t_j:

    Z_j = s_j e_j^T x_j^- + eta_j,                      (2.1)
    x_j^+ = x_j^- - d_j Z_j.                            (2.2)

Let

    M_j = e_j^T exp(G t_j)

be the passive row from x_0 to the j-th readout if no resets were applied.

For k<j define

    H_jk = e_j^T exp(G(t_j-t_k)) d_k,

and H_jk=0 for k>=j.

Let

    D=diag(s_1,...,s_N).

Then direct propagation gives

    x_j^-
      = exp(G t_j)x_0
        - sum_{k<j} exp(G(t_j-t_k)) d_k Z_k.

Substitution into (2.1) yields

    Z_j
      + s_j sum_{k<j} H_jk Z_k
      = s_j M_j x_0 + eta_j.

Hence in vector form:

    (I+D H) Z = D M x_0 + eta.                          (2.3)

Since H is strictly lower triangular, I+D H is unit lower triangular and therefore invertible with determinant 1 for every finite protocol.

Define the causal transformed record

    Y := (I+D H) Z.                                     (2.4)

Then EXACTLY

    Y = D M x_0 + eta.                                  (2.5)

This transformation is parameter-independent and bijective.

## 3. Statistical-experiment equivalence

For any common noise law of eta independent of x_0, the map

    Z <-> Y=(I+DH)Z

is a deterministic invertible Markov transformation independent of the unknown parameter.

Therefore the two experiments are Blackwell-isomorphic / Le Cam equivalent:

NOISE-DRIVEN RESET EXPERIMENT
    <=>
PASSIVE WEAK-SAMPLING MEAN D M x_0
    + ORIGINAL NOISE eta.

The reset vectors d_j affect the raw observed coordinates Z but disappear from the transformed signal law.

This is sharply different from the earlier carrier where reset used the ideal b_j but observation added eta_j afterward. There the corresponding transformation amplifies/transforms the noise, and deterministic storage dissipation constrains the parameter sensitivity.

Here:

    RAW-OBSERVATION RESET
    !=
    IDEAL-SIGNAL RESET + READOUT NOISE.

## 4. Gaussian Fisher/KL for fixed protocol

Assume

    eta ~ N(0,Sigma)

with positive-definite Sigma independent of the parameter.

From (2.5), for x_0=theta v,

    Y ~ N(theta D M v, Sigma).

Thus

    I(theta)
      = (D M v)^T Sigma^{-1}(D M v),                    (4.1)

and

    D_KL(P_theta || P_theta')
      = ((theta-theta')^2/2)
        (D M v)^T Sigma^{-1}(D M v).                    (4.2)

For iid fixed-variance noise Sigma=sigma^2 I,

    I(theta)
      = sigma^{-2}
        sum_j s_j^2 [M_j v]^2.                          (4.3)

The deterministic reset storage V_* does not appear.

The relevant object is now the PASSIVE weighted sampling energy.

## 5. Exact scalar counterexample to weak statistical collapse

Take

    n=1,
    G=0,
    e=d=1,
    x_0=theta,
    s_j=s in (0,1),
    eta_j iid N(0,sigma^2).

The model is

    Z_j=s x_j+eta_j,
    x_{j+1}=x_j-Z_j.                                    (5.1)

Since

    x_j=theta-sum_{k<j} Z_k,

we have

    Z_j
      = s theta
        - s sum_{k<j} Z_k
        + eta_j.

Define

    Y_j
      = Z_j + s sum_{k<j} Z_k.                          (5.2)

Then exactly

    Y_j=s theta+eta_j,                                  (5.3)

and the triangular map Z<->Y has determinant 1.

Therefore the entire N-shot experiment is exactly equivalent to N independent observations

    Y_j iid N(s theta,sigma^2).

Its Fisher information is

    I_N = N s^2/sigma^2.                                (5.4)

Consequences as s->0:

- if N(s)s^2 -> 0, information collapses;
- if N(s)s^2 -> c in (0,infinity), nonzero finite information survives;
- if N(s)s^2 -> infinity, Fisher information diverges in the bare mathematical model.

In particular, with

    N(s)=ceil(c/s^2),

the full experiment does NOT converge to a no-information experiment.

This defeats the previous arbitrary-N collapse because the statistical carrier is different.

## 6. Explicit decision-value witness

Let theta in [-R,R] and define the sufficient average

    W_N = (1/(N s)) sum_j Y_j.

Then

    W_N ~ N(theta, tau_N^2),
    tau_N^2 = sigma^2/(N s^2).                          (6.1)

Use the linear shrinkage estimator

    hat_theta = a W_N,
    a = R^2/(R^2+tau_N^2).

Its worst-case MSE over |theta|<=R is

    sup E[(hat_theta-theta)^2]
      = R^2 tau_N^2/(R^2+tau_N^2).                     (6.2)

If N(s)s^2 -> c>0,

    tau_N^2 -> sigma^2/c,

and the limiting worst-case risk is

    R^2 sigma^2/(c R^2+sigma^2)
      < R^2.                                            (6.3)

Thus a strictly positive decision advantage over the no-information risk R^2 survives as s->0.

If N(s)s^2->infinity, this displayed estimator risk tends to zero.

No claim of exact finite-s minimax optimality of the linear shrinkage rule is required for the counterexample.

## 7. Why the old storage proof fails

In the ideal-signal reset carrier, when comparing theta and theta' at the same frozen past history, the parameter sensitivity is reset by

    delta x^+ = Q_s delta x^-,

so deterministic reset dissipation controls the sequence of conditional mean differences.

In the noise-driven reset carrier

    x^+ = x^- - d Z,

and the sequential KL comparison conditions on the SAME observed history value Z=z under both parameter values.

Therefore, at fixed z,

    delta x^+
      = delta x^-,

because the common term -d z cancels.

Thus the parameter sensitivity does NOT undergo Q_s in the conditional likelihood geometry.

This is the exact reason the previous pathwise V_* telescope is illegal here.

Firewall:

    PHYSICAL STATE CONTRACTS UNCONDITIONALLY
    !=
    PARAMETER SENSITIVITY CONTRACTS CONDITIONALLY ON THE SAME OBSERVED HISTORY.

That distinction is load-bearing.

## 8. Adaptive heterogeneous extension

Suppose actions, times and strengths are chosen causally from past observed history by one common parameter-independent policy.

At any frozen history h, the current state has the affine form

    x_j^-(theta;h)
      = exp(G t_j(h)) theta v
        + r_j(h),                                       (8.1)

where r_j(h) contains known past observed-reset contributions.

Therefore

    Z_j | h,theta
      ~ N(
          theta s_j(h)
          e_{a_j(h)}^T exp(G t_j(h)) v
          + known_offset(h),
          sigma^2
        ).                                              (8.2)

The conditional sensitivity is the PASSIVE row

    c_j(h)
      = s_j(h)
        e_{a_j(h)}^T exp(G t_j(h)) v,                   (8.3)

not the reset-flow sensitivity.

Hence sequential KL is

    D_KL(P_theta^pi || P_theta'^pi)
      = ((theta-theta')^2/(2 sigma^2))
        E_theta^pi sum_j c_j(H_{j-1})^2.                (8.4)

A collapse theorem now requires a bound on the passive adaptive sampling budget

    sum_j s_j^2
      [e_{a_j}^T exp(G t_j)v]^2,                        (8.5)

not on the deterministic reset storage V_*.

Without a sample-count/time/resource restriction, common finite reset storage does not control (8.5).

## 9. Finite-horizon/sample-count sufficient repair

If all readout vectors satisfy ||e_a||<=E and all times obey t_j<=T, define

    K_T(v)
      = E sup_{0<=t<=T} ||exp(Gt)v||.

Then for s_j<=epsilon,

    c_j(h)^2 <= epsilon^2 K_T(v)^2.

If every realized policy has at most N_epsilon shots,

    sum_j c_j(h)^2
      <= N_epsilon epsilon^2 K_T(v)^2.                  (9.1)

Therefore with iid N(0,sigma^2) innovations,

    D_KL
      <= ((theta-theta')^2
          N_epsilon epsilon^2 K_T(v)^2)
         /(2 sigma^2).                                  (9.2)

Thus collapse follows if

    N_epsilon epsilon^2 -> 0.                           (9.3)

The threshold N~epsilon^{-2} is sharp already in the scalar G=0 example.

This identifies the missing source-native resource:
sample count, dwell/bandwidth, time, energy, or another physical budget that prevents arbitrarily many raw-observation feedback shots.

## 10. Relation to PRF11 R14 correlated-noise seam

PRF11 R14 shows a different failure mode:

even when the mean sensitivity norm tends to zero, nearly singular correlated noise covariance can preserve Fisher information.

The present counterexample needs no such covariance pathology:
- eta_j are iid;
- each marginal and innovation variance is fixed sigma^2;
- information survives solely because the noise-driven reset changes the conditional sensitivity dynamics and permits repeated passive-strength observations.

Therefore the two seams are independent:

CORRELATED-NOISE PRECISION SEAM
    !=
NOISE-IN-RESET CONDITIONAL-SENSITIVITY SEAM.

Both must be typed in any source-native statistical bridge.

## 11. Relation to REC10 triangular factorization

REC10's deterministic reset factorization concerns ideal reset signals and noiseless rank/kernel geometry.

The present factorization is analogous in causal triangular form but has a different statistical meaning:

    (I+D H) Z = D M x_0 + eta.

Because the same invertible triangular operator multiplies the observed data but NOT eta on the right-hand side, the noise-driven-reset experiment reduces to passive sampling with the original noise.

By contrast, in the ideal-reset/readout-noise carrier, undoing reset mixing transforms/amplifies the observation noise.

Thus:

    SAME TRIANGULAR ALGEBRA SHAPE
    !=
    SAME STATISTICAL EXPERIMENT.

## 12. Firewalls

CURRENT NOISE IN RESET
    != DECLARED IDEAL-RESET CARRIER.

UNCONDITIONAL STATE ATTENUATION
    != CONDITIONAL PARAMETER-SENSITIVITY ATTENUATION.

FINITE RESET-FLOW STORAGE
    != PASSIVE ADAPTIVE SAMPLING BUDGET.

IID FIXED-VARIANCE NOISE
    != WEAK COLLAPSE AUTOMATICALLY.

N UNBOUNDED
    != FREE UNDER A PHYSICAL RESOURCE MODEL,
but it IS mathematically sufficient to defeat collapse here.

N epsilon^2 -> 0
    => collapse under bounded passive rows;
N epsilon^2 ~ constant
    => finite information may survive.

NOISE-DRIVEN RESET EXPERIMENT
    <=> PASSIVE WEAK SAMPLING + ORIGINAL NOISE
for fixed deterministic linear protocols.

CORRELATED-NOISE SEAM
    != NOISE-IN-RESET SEAM.

CLASSICAL FEEDBACK RESET
    != QUANTUM INSTRUMENT.

## 13. Disposition

PREVIOUS COMMON-V_* GAUSSIAN COLLAPSE:
    remains PASS in its declared carrier where current noise does not enter contemporaneous reset.

EXTENSION TO RAW-OBSERVATION RESET:
    FAILS.

EXACT REASON:
    conditional parameter sensitivity follows passive flow rather than Q_s reset flow.

FIXED-PROTOCOL EXPERIMENT:
    exactly invertibly equivalent to
    Y=D M x_0+eta.

SCALAR SHARP THRESHOLD:
    Fisher = N s^2/sigma^2.

CHEAP SOURCE REPAIR:
    impose/derive legal sample-count, dwell, bandwidth, time, energy, or innovation-resource scaling.

OPEN:
- source-native physical model deciding whether reset uses latent ideal signal, filtered estimate, or raw noisy observation;
- mixed reset laws interpolating between these carriers;
- stochastic state dynamics;
- quantum instruments.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
NO_NEW_TASK.
