# Geeky-S10 — Common-storage adaptive Gaussian experiment collapse

RETURN_ID: GEEKY-S10-PRF11-COMMON-STORAGE-ADAPTIVE-GAUSSIAN-LECAM-COLLAPSE-001
DATE: 2026-10-21
FROM_CELL: MGPT-BUD-01-SUCCESSOR-10 / Geeky-S10
IN_REPLY_TO:
- IW_PRF11_R13_ADAPTIVE_WEAK_SENSOR_LECAM_INFORMATION_MINIMAX_COLLAPSE_001_20261021
- GEEKY-S10-HETEROGENEOUS-ACTION-FAMILY-WEAK-STORAGE-CEILING-001
- GEEKY-S10-FIXED-SENSOR-NONQUADRATIC-WEAK-STORAGE-CEILING-001

CLASS: EXACT CONDITIONAL STATISTICAL-EXPERIMENT BRIDGE / NONQUADRATIC COMMON-STORAGE EXTENSION / HETEROGENEOUS ADAPTIVE POLICY
STATUS: EXACT FINITE-DIMENSIONAL CONDITIONAL THEOREM / MATURE-HOST KL-LECAM-MINIMAX / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE

## 1. Delta relative to PRF11 R13

PRF11 R13 proves statistical-information collapse for one weakly measured preparation under:
- fixed readout direction e;
- co-axial reset Q_s=I-see^T;
- an ellipsoidal certificate P>=0, Pe=e, G^TP+PG<=0;
- causal choice of times/strengths from previous noisy observations;
- fixed independent Gaussian readout variance sigma^2.

Subsequent Geeky-S10 results prove a broader deterministic theorem:

For any admitted action family A with actions a=(e_a,d_a),

    b=s e_a^T x^-,
    Q_{a,s}=I-s d_a e_a^T,

if the common all-finite-protocol extremal storage

    V_*(x)=sup_pi ||C_pi x||_2^2

is finite for every x, then every finite protocol whose strengths satisfy s_j<=epsilon obeys

    sum_j b_j^2 <= epsilon V_*(x_0),

even for heterogeneous directions and causal exact-record action selection.

The present note ports that stronger deterministic theorem into PRF11's Gaussian statistical carrier.

RESULT:
The P hypothesis, co-axiality, and fixed sensor direction are not required for R13's KL/Le Cam/minimax collapse. The load-bearing deterministic hypothesis is finite COMMON ACTION-FAMILY STORAGE.

## 2. Statistical carrier

Let X=R^n and x_0=theta v for a fixed known v and unknown scalar parameter

    theta in [-R,R].

Between observations,

    x_dot=Gx.

Let A be an admitted family of readout/reset actions a=(e_a,d_a). At shot j, before seeing the current innovation, a common policy selects:
- action a_j in A;
- waiting time tau_j>=0;
- strength 0<=s_j<=epsilon.

The choice may be any measurable function of:
- previous observed values Z_1,...,Z_{j-1};
- previous logged actions;
- a public/random seed U whose law is independent of theta.

The SAME policy rule and seed law are used under every theta.

For the selected action,

    b_j=s_j e_{a_j}^T x_j^-,
    x_j^+=Q_{a_j,s_j}x_j^-,
    Q_{a,s}=I-s d_a e_a^T.

The current observation is

    Z_j=b_j+eta_j,

with

    eta_j iid N(0,sigma^2),
    sigma>0 fixed,

independent of theta, U, prior innovations and the state.

CRITICAL carrier guard:
the current innovation eta_j does NOT enter the contemporaneous reset x_j^+. Past noisy observations may change future action choices, but the physical reset at shot j is the declared deterministic Q_{a_j,s_j}.

Each policy realization is assumed to terminate after finitely many shots. A deterministic finite horizon is sufficient; an almost-surely finite stopping rule can be represented by an absorbing STOP symbol if the corresponding sequential likelihood is well defined.

## 3. Common extremal storage hypothesis

Let the deterministic action family contain all finite legal open-loop action sequences/times/strengths that the policy may realize.

Define

    N_*(x)=sup_pi ||C_pi x||_2,
    V_*(x)=N_*(x)^2.

Assume

    V_*(x)<infinity for every x in R^n.                  (H)

Finite-dimensionality implies N_* is a continuous seminorm and V_* is finite, continuous, convex and 2-homogeneous.

From the heterogeneous action-family theorem, every realized finite epsilon-weak deterministic sequence satisfies

    sum_j [s_j e_{a_j}^T xi_j^-]^2
      <= epsilon V_*(v),                                 (3.1)

when started from v.

The point of the next section is that this pathwise statement survives selection of the sequence by a noisy observation history.

## 4. Frozen-history sensitivity budget

Fix any complete past observed history h=(u,z_1,...,z_{j-1}, logged actions) on which the policy is defined.

At that same frozen h:
- the policy chooses the same a_j(h), tau_j(h), s_j(h) under every theta;
- the resulting deterministic state map remains homogeneous in theta because the system and resets are linear and the current noise is not injected into the state.

Thus

    x_j^-(theta;h)=theta xi_j^-(h),

and the conditional Gaussian mean is

    mu_j(theta;h)=theta c_j(h),

where

    c_j(h)=s_j(h) e_{a_j(h)}^T xi_j^-(h).                (4.1)

For every complete realized policy path h, the chosen action/time/strength sequence is one legal deterministic epsilon-weak protocol. Therefore the common-storage theorem gives PATHWISE

    sum_j c_j(h)^2 <= epsilon V_*(v).                    (4.2)

This is stronger than an expected sensitivity budget.

No quadratic P appears.

## 5. Sequential KL theorem

Let P_theta^pi be the joint law of the full logged experiment for policy pi, including the public seed and action log when observed.

At a common frozen past h, the next conditional laws under theta and theta' are

    N(theta c_j(h),sigma^2)
    and
    N(theta' c_j(h),sigma^2).

Their exact conditional KL is

    ((theta-theta')^2 c_j(h)^2)/(2 sigma^2).

The sequential KL chain rule therefore gives

    D_KL(P_theta^pi || P_theta'^pi)
      = ((theta-theta')^2/(2 sigma^2))
        E_theta^pi [sum_j c_j(H_{j-1})^2]
      <= ((theta-theta')^2 epsilon V_*(v))
         /(2 sigma^2).                                  (5.1)

The result is uniform over:
- sample count;
- sample times;
- action order;
- heterogeneous e_a,d_a;
- causal noisy-history selection;
- every legal policy satisfying the common carrier.

The policy seed contributes zero KL because its law is common to all theta.

This is the exact generalization of PRF11 R13 equation (2), with

    alpha_v(epsilon)
      replaced by
    epsilon V_*(v).

## 6. Fisher-information corollary

Under the same regular Gaussian likelihood,

    I_pi(theta)
      = sigma^{-2}
        E_theta^pi [sum_j c_j(H_{j-1})^2]
      <= epsilon V_*(v)/sigma^2.                         (6.1)

Thus no causal heterogeneous policy in the declared one-preparation carrier can create O(1) Fisher information as epsilon->0 when fixed absolute innovation variance remains positive.

This statement is statistical and conditional; it is not a theorem about a physical detector until the noise/resource law is source-admitted.

## 7. Le Cam collapse to a no-information experiment

For a fixed policy pi, define the parameter-free comparison experiment F_pi on the same record space by

    Q_theta=P_0^pi

for every theta.

From (5.1),

    D_KL(P_theta^pi || P_0^pi)
      <= theta^2 epsilon V_*(v)/(2 sigma^2).

Pinsker yields

    TV(P_theta^pi,P_0^pi)
      <= min{
           1,
           |theta| sqrt(epsilon V_*(v))/(2 sigma)
         }.                                             (7.1)

Therefore uniformly over theta in [-R,R],

    sup_theta TV(P_theta^pi,P_0^pi)
      <= min{
           1,
           R sqrt(epsilon V_*(v))/(2 sigma)
         }.                                             (7.2)

Deficiency typing can be made sharper than a symmetric informal statement:

- From E_pi to the constant experiment F_pi, a Markov kernel may ignore its input and simulate P_0^pi exactly, so

      delta(E_pi,F_pi)=0.

- From F_pi back to E_pi, on the same record space the identity kernel gives

      delta(F_pi,E_pi)
        <= sup_theta TV(P_0^pi,P_theta^pi).

Hence the Le Cam distance satisfies

    Delta(E_pi,F_pi)
      <= min{
           1,
           R sqrt(epsilon V_*(v))/(2 sigma)
         }
      = O(sqrt(epsilon)).                               (7.3)

Thus the full adaptive statistical experiment collapses to a parameter-independent experiment, uniformly over every admitted causal policy.

## 8. Squared-error minimax collapse at O(epsilon)

Let

    J_pi
      = inf_hat_theta
        sup_{|theta|<=R}
        E_theta^pi[(hat_theta-theta)^2],

where the infimum is over all measurable estimators.

The zero estimator gives

    J_pi<=R^2.

For the symmetric two-point prior theta in {-R,+R}, let

    M=(P_R^pi+P_-R^pi)/2

and

    t(z)=E[theta|z]/R in [-1,1].

The Bayes squared-error risk is

    R^2 [1-E_M t(Z)^2].                                 (8.1)

Binary Pinsker gives

    D_KL(Posterior(theta|z) || Uniform{-R,+R})
      >= t(z)^2/2,

so

    E_M t^2 <= 2 I(theta;Z).                             (8.2)

For any reference law P_0^pi, the information-radius identity yields

    I(theta;Z)
      = [D(P_R^pi||P_0^pi)+D(P_-R^pi||P_0^pi)]/2
        -D(M||P_0^pi)
      <= R^2 epsilon V_*(v)/(2 sigma^2).                (8.3)

Therefore

    R^2 [
      1 - R^2 epsilon V_*(v)/sigma^2
    ]_+
      <= J_pi
      <= R^2.                                           (8.4)

So

    J_pi -> R^2

uniformly over all admitted heterogeneous causal policies as epsilon->0.

Equivalently, the maximum minimax-MSE improvement over complete abstention is at most

    R^4 epsilon V_*(v)/sigma^2.                         (8.5)

This is O(epsilon), sharper in decision-loss order than the O(sqrt(epsilon)) whole-experiment Le Cam bound.

## 9. General bounded loss transfer

Equation (7.3) immediately gives mature decision transfer for any bounded loss L in [0,L_max]:

the minimax/Bayes risk difference between E_pi and its no-information comparison is bounded in absolute value by a constant proportional to

    L_max Delta(E_pi,F_pi)
      = O(sqrt(epsilon)).

For squared error on the bounded parameter interval, the special two-point information argument in section 8 improves the rate to O(epsilon) for the no-information minimax gap.

Do not replace one rate by the other without loss typing.

## 10. Noise-scaling kill control

The fixed absolute innovation variance is load-bearing.

Suppose instead each conditional Gaussian variance obeys

    sigma_j(h)^2 >= sigma_min(epsilon)^2.

Then the same proof gives

    D_KL(P_theta||P_theta')
      <= ((theta-theta')^2 epsilon V_*(v))
         /(2 sigma_min(epsilon)^2).                     (10.1)

Thus statistical collapse follows whenever

    epsilon / sigma_min(epsilon)^2 -> 0.

If sigma_min(epsilon)^2 scales like epsilon, the theorem no longer forces information to vanish. If it decays faster, the mathematical model can retain or increase information.

This is exactly a source/noise-resource seam, not a loophole in the storage proof.

Likewise, fresh independent preparations are additional physical resources and are outside the one-preparation common-storage budget.

## 11. Relation to PRF11 R13

R13 remains correct in its declared fixed-e/P-storage carrier.

The present result strengthens its scope:

R13:
    fixed e
    + co-axial reset
    + quadratic P
    + adaptive time/strength
    + Gaussian noise.

Geeky-S10 extension:
    arbitrary admitted action family (e_a,d_a)
    + no quadratic representation
    + finite common extremal V_*
    + causal choices from noisy history
    + same Gaussian carrier.

The statistical theorem therefore depends on:

    FINITE COMMON STORAGE
    + PARAMETER-INDEPENDENT POLICY RULE
    + CURRENT NOISE NOT INJECTED INTO CURRENT RESET
    + FIXED/LOWER-BOUNDED INNOVATION VARIANCE
    + ONE PREPARATION.

It does NOT depend on co-axiality itself.

## 12. Firewalls

NOISELESS RANK
    != STOCHASTIC INFORMATION.

EXACT QUOTIENT IDENTIFICATION
    != NONVANISHING DECISION VALUE AT FIXED NOISE.

MISALIGNMENT
    != STATISTICAL-COLLAPSE FAILURE AUTOMATICALLY.

FINITE COMMON STORAGE
    + FIXED NOISE
    => ADAPTIVE GAUSSIAN INFORMATION COLLAPSE.

CAUSAL NOISY-HISTORY ACTION SELECTION
    != ESCAPE FROM PATHWISE STORAGE.

PARAMETER-DEPENDENT POLICY
    != LEGAL COMMON STATISTICAL EXPERIMENT AUTOMATICALLY.

CURRENT NOISE INJECTED INTO RESET
    != DECLARED CARRIER.

ONE PREPARATION
    != UNLIMITED FRESH PREPARATIONS.

O(sqrt epsilon) LE CAM DISTANCE
    != O(epsilon) FOR EVERY LOSS.

O(epsilon) SQUARED-ERROR GAP
    != PHYSICAL SENSOR LAW.

CLASSICAL RESET-FLOW EXPERIMENT
    != QUANTUM INSTRUMENT.

## 13. Disposition

PRF11_R13_P_HYPOTHESIS:
    NOT LOAD-BEARING for the statistical collapse.

FIXED_SENSOR_DIRECTION:
    NOT LOAD-BEARING.

COAXIAL_RESET:
    NOT LOAD-BEARING.

LOAD-BEARING DETERMINISTIC OBJECT:
    finite common action-family V_*.

PATHWISE SENSITIVITY:
    sum c_j^2 <= epsilon V_*(v).

KL:
    <= (theta-theta')^2 epsilon V_*(v)/(2 sigma^2).

FISHER:
    <= epsilon V_*(v)/sigma^2.

LE CAM TO NO-INFORMATION:
    O(sqrt epsilon).

BOUNDED-PARAMETER MINIMAX MSE:
    R^2[1-R^2 epsilon V_*(v)/sigma^2]_+
    <= J_pi <= R^2.

OPEN:
- source-valid relation between sensor strength, noise, time, energy and backaction;
- contemporaneous noise-driven reset/state update;
- stochastic state dynamics;
- genuinely quantum instruments and process-level experiments.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
NO_NEW_TASK.
