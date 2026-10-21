---
artifact_id: IW_INT8_FINITE_HORIZON_WEAK_READOUT_SHARP_CEILING_WITHOUT_GLOBAL_STORAGE_001_20261021
date: 2026-10-21
from_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
class: CROSS_FRONT_SCIENTIFIC_INTEGRATION / EXACT_FINITE_HORIZON_MATURE_HOST_COROLLARY
exposure: PUBLIC
status: DERIVED_AND_NUMERICALLY_SANITY_CHECKED / INDEPENDENT_REFEREE_NOT_DONE
authoritative_science_state: REV020 / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
source_bodies:
  - research/m13/2026-10-19/IW_M13_ROT12_stable_free_unbounded_measurement_gain_001.md
  - research/geeky-s10/2026-10-21/geeky_s10_int8_weak_measurement_accumulation_ceiling_001.md
  - research/geeky-s10/2026-10-21/geeky_s10_fixed_sensor_nonquadratic_weak_storage_ceiling_001.md
  - research/geeky-s10/2026-10-21/geeky_s10_heterogeneous_action_family_weak_storage_ceiling_001.md
  - research/int8/2026-10-21/iw_int8_nonquadratic_available_storage_weak_measurement_universal_ceiling_001.md
  - research/prf11/2026-10-21/IW_PRF11_R13_ADAPTIVE_WEAK_SENSOR_LECAM_INFORMATION_MINIMAX_COLLAPSE_001_20261021.md
  - research/lt5/2026-10-20/lt5_target_information_vs_actuation_bounded_feedback_exact_gate_001.md
bw_ingestion: NOT_VERIFIED
---

# INT8 — Finite-horizon weak-readout energy with no global available-storage assumption

## 0. Currentness, host subtraction and the actual cross-front delta

Geeky-S10, after INT8's nonquadratic available-storage result, independently recorded the same V_epsilon<=epsilon V_* theorem and broadened it to heterogeneous readout/reset actions, assuming the *whole action family* has finite common V_*. That closes the earlier nonquadratic mathematical question; it is not an open INT8 contribution.

M13 ROT12 had already proved a **finite-horizon** all-shot ceiling gamma||c||_2<=exp(mu_+ T) with mu_+=max(mu_2(G),0), without requiring free Hurwitz stability or a global storage certificate. M13 even recorded the precise per-shot identity relating output and Euclidean norm loss, but did not make the maximum-weak-strength scaling explicit.

The bounded novel-to-the-project **integration delta** here is the sharpened, exact weak-strength factor, a uniform aligned-variable-direction extension, a sharp unstable example with V_* infinite, and a carefully typed transfer of the resulting deterministic budget to PRF11's *hypothetical* fixed-variance Gaussian experiment.

No claim of mathematical originality. This is a direct, standard weighted energy-accounting refinement of M13's host result, not a new spectral or physical mechanism.

## 1. Typed classical carrier

Fix horizon 0<T<infinity, finite n, real matrix G in R^(n x n), and initial x_0 in R^n. Between events:

    x'(t)=Gx(t).

Choose ANY finite (possibly extremely large) number of events at

    0<=t_1<=...<=t_N<=T.

Each event j has its own unit direction e_j (||e_j||_2=1) and strength 0<=s_j<=epsilon<1, with **co-aligned readout and state reset**:

    a_j=e_j^T x(t_j^-),
    b_j=s_j a_j,
    x(t_j^+)=Q_j x(t_j^-),
    Q_j=I-s_j e_j e_j^T.

This is a deterministic classical state-update model. Directions, strengths, and waiting times may change from shot to shot. For fixed deterministic schedules the map C_pi:x_0->(b_1,...,b_N) is linear. For causally selected schedules the pathwise bound remains true, but the adaptive map is not in general linear.

Let S=(G+G^T)/2, mu=largest eigenvalue of S, and m=max(mu,0). No assumption on eigenvalue stability, all-horizon available storage V_*, or existence of any nontrivial Lyapunov P.

## 2. Exact weighted energy ledger and theorem

At event j the **Euclidean** energy drop is

    D_j=||x_j^-||_2^2-||x_j^+||_2^2
       =s_j(2-s_j)(e_j^T x_j^-)^2.

The squared normalized record is

    b_j^2=s_j^2(e_j^T x_j^-)^2
         =[s_j/(2-s_j)] D_j.

Because s/(2-s) increases on [0,1),

    b_j^2 <= [epsilon/(2-epsilon)] D_j.           (2.1)

The free dynamics satisfies

    d/dt ||x(t)||^2
        =2x(t)^T S x(t)
        <=2m ||x(t)||^2.

Therefore W(t)=exp(-2mt)||x(t)||^2 is nonincreasing between events and at events drops by exp(-2mt_j)D_j. Telescoping over the complete finite protocol gives the stronger **weighted** inequality

    sum_j exp(-2m t_j) D_j <= ||x_0||^2.

In particular

    sum_j exp(-2m t_j) [ (2-s_j)/s_j ] b_j^2
      <= ||x_0||^2,                                (2.2)

where events with s_j=0 have b_j=D_j=0 and are omitted from the displayed quotient.

Combining with (2.1), since t_j<=T:

    **sum_j b_j^2
       <= [epsilon/(2-epsilon)] exp(2mT)||x_0||^2.**  (THEOREM 2.3)

This is UNIFORM over:
- all finite counts N (even if N increases without bound as epsilon decreases);
- all times in [0,T], including arbitrarily close or coincident times;
- all aligned unit directions e_j, which may vary arbitrarily;
- all strength choices 0<=s_j<=epsilon;
- arbitrary, including unstable and nonnormal, real matrices G.

If a direction/strength/time is selected causally from the *exact* observed record, the same energy identity holds **along each realized path**. It does not imply that the resulting adaptive input-output map is linear. For time-varying G(t), replacing exp(2mT) with exp(2 integral_0^T max(0,mu_2(G(t))) dt) gives the same result under standard locally integrable generator hypotheses.

**Critical scope:** direction changes remain co-aligned within every action e_j=d_j. For arbitrary misaligned d_j not parallel to e_j, Euclidean reset need not be contractive, and this proof does not apply. Geeky-S10's distinct heterogeneous action-family V_* theorem can handle some misaligned cases **if finite common storage exists**.

## 3. Operator and exact inversion consequence

For every PREDETERMINED finite schedule pi, define C_pi x_0=b. Theorem 2.3 is equivalent to

    ||C_pi||_op
       <= exp(mT) sqrt(epsilon/(2-epsilon)).       (3.1)

This does NOT require the global supremum V_*(x) over all times to be finite.

If a fixed nonzero initial-target functional m_target^T x_0 is reconstructed EXACTLY by a linear estimator w^T C_pi x_0, then

    C_pi^T w=m_target,

so necessarily

    ||w|| >= ||m_target|| exp(-mT)
            sqrt((2-epsilon)/epsilon).             (3.2)

This is an Omega(epsilon^-1/2) absolute inverse-gain barrier uniformly across all finite measurements in a FIXED horizon. It is not a statement about the *relative condition number* or about arbitrary biased/risk-optimal estimation.

For LT5's distinct **static linear operator-gain** class, assume a physically source-matched post-reset scalar terminal target m_pi=Phi_pi^T ell, independent Euclidean state/noise balls of radii R,delta, and a separately declared actual terminal actuator port a_pi. Only then its exact conditional formula applies:

    J_kappa(pi)
      = min_{||w||<=kappa||a_pi||}
          { R||m_pi-C_pi^T w|| + delta||w|| }.

For every such fixed schedule:

    0 <= R||m_pi||-J_kappa(pi)
      <= R kappa||a_pi|| exp(mT)
         sqrt(epsilon/(2-epsilon)).                 (3.3)

If ||a_pi||<=A uniformly over considered protocols, then the right side is uniform in N/timing/direction as well. If m_pi shrinks because of destructive resets, that is TARGET ERASURE, not evidence of successful control.

This does not transfer to LT5's separate hard-amplitude nonlinear control class, or to a physical actuator whose effect is not yet typed.

## 4. SHARPNESS and indispensable role of a finite horizon

The coefficient **epsilon/(2-epsilon) exp(2mT)** is *globally sharp* over the declared class of real generators, unit co-aligned sensors and finite protocols.

Take the one-dimensional genuinely unstable free generator G=[g] with g>0, e=1, and initial x_0=1. Wait freely until time T, giving x(T^-)=exp(gT). Then take N immediately consecutive measurements of equal strength s=epsilon at T. For their finite record,

    sum_{j=1}^N b_j^2
      = [epsilon/(2-epsilon)]
        [1-(1-epsilon)^(2N)] exp(2gT).             (4.1)

Here m=g. As N increases through finite values the ratio of (4.1) to the upper bound in Theorem 2.3 tends to 1. If strict t_j<t_(j+1) is imposed, place the measurements in an arbitrarily short interval ending at T, with the same supremal result.

For the SAME scalar model and every epsilon>0, even a single measurement after a waiting time tau->infinity yields b^2=epsilon^2 exp(2g tau)->infinity. Hence the unrestricted all-horizon V_*(1) is INFINITE.

Thus finite-horizon weak collapse is fully compatible with globally infinite available storage. There is no hidden assumption that weak probing stabilizes the free dynamics or that the all-horizon response is bounded.

This also reconciles M13's separate Hurwitz-but-nonnormal unstable measurement cycle: its growth requires a growing total horizon kh. There is no contradiction with the current finite-T bound. M13's earlier T-ceiling can be sharpened by the additional epsilon/(2-epsilon) factor whenever the maximum event strength is known.

## 5. Statistical conditional port to PRF11 R13 (re-use, not priority claim)

PRF11 R13 independently proved that a PATHWISE deterministic squared sensitivity ceiling can be transported to a single-preparation, conditional sequential Gaussian experiment with *fixed* innovation variance sigma^2 and a shared policy. Its original proof used a global quadratic P-storage. The current theorem supplies a different donor budget that does NOT need P or finite V_*, provided the policy has a declared finite horizon T.

For a scalar unknown theta in [-R,R], set x_0=theta v. Assume each measurement's action/time/strength can be selected causally from past noisy observations but every path has <=T total elapsed time. At each frozen past-history h, the state responds linearly to theta; the conditional observation law is

    Z_j | h,theta ~ Normal(theta c_j(h), sigma^2),

with independent sigma>0 FIXED, deterministic reset driven by ideal (not noisy) pre-readout state, and the *same predictable policy* under all theta. Applying the pathwise weak-bound to v gives

    sum_j c_j(h)^2
        <= A_epsilon(T,v)
        := [epsilon/(2-epsilon)] exp(2mT)||v||^2.

The ordinary sequential Gaussian KL chain rule gives, for any two parameters,

    KL(P_theta || P_theta')
      <= (theta-theta')^2 A_epsilon/(2sigma^2).     (5.1)

For the parameter-free experiment P_0, Pinsker gives

    sup_|theta|<=R TV(P_theta,P_0)
      <= min{1, R sqrt(A_epsilon)/(2sigma)}.        (5.2)

Reusing PRF11's elementary two-point Bayes/information-radius argument (not a newly proved information-theoretic host result), every estimator of theta, INCLUDING BIASED, obeys the declared minimax MSE bound

    R^2[1-R^2 A_epsilon/sigma^2]_+
      <= inf_est sup_|theta|<=R E_theta(est-theta)^2
      <= R^2.                                      (5.3)

Consequently even arbitrary large finite N and causally chosen aligned directions cannot prevent the Gaussian statistical experiment from approaching no-information as epsilon->0 **for fixed T, fixed sigma, and this single-preparation source contract**, including cases with globally infinite V_*.

CRITICAL COUNTER-GUARDS:
- fixed variance sigma^2>0 is load-bearing; if it changes with strength, risk must be recomputed;
- noisy outcomes may select future actions but do not themselves drive the instant reset;
- variable number of fresh independent preparations is a different resource;
- genuinely quantum instrument backaction is not established;
- the Gaussian experiment is a hypothetical statistical overlay, not observational evidence of a Nash-IDG physical mechanism.

## 6. Synthetic numerical controls and reproducibility

Sanity control A: G=[[-1,4],[0,-1]], mu_2(G)=+1, T=2, epsilon=.06, x0=(.6,-.8), fixed RNG seed 20261021. Random 250 measurement times in [0,T], independent randomized unit aligned e_j and strengths in [0,epsilon]. Computing expm(G delta_t) exactly to double precision yields

    sum b_j^2=0.013484146
    RHS=1.688602578
    ASSERT PASS.

This validates one instance, not the theorem. Note the bound can be conservative for transiently nonnormal flows.

Sanity control B: scalar G=.7, T=1.3, epsilon=.04. A free wait until T followed by N equal-strength zero-wait shots gives exact ratio to theoretical bound

    N=10:  0.557997566
    N=100: 0.999715392
    N=500: 1.000000000 to displayed precision.

These ratios follow directly from 1-(1-epsilon)^(2N), confirming the sharpness witness independently of any numerical eigenanalysis.

## 7. Cross-front synthesis and failure map

| Branch | Global V_* | Finite T | e_j=d_j | Uniform weak-record ceiling |
|---|---|---|---|---|
| INT8/Geeky nonquadratic all-horizon | finite and common | unrestricted | not needed for Geeky's action-family theorem | <=epsilon V_* |
| Geeky P-ellipsoidal | P dissipative | unrestricted | fixed co-aligned e | <=epsilon/(2-epsilon)*x0^TPx0 |
| Current INT8/M13 strengthened finite horizon | may be infinite | required | yes, may vary j | <=epsilon/(2-epsilon)*exp(2mT)||x0||² |
| REC10 misaligned fixed non-dissipating witness | infinite | even T=0 permits arbitrary repeated shots | no | no common uniform count ceiling |
| M13 Hurwitz but nonnormal long cycle | infinite over long protocols | T->infinity | yes | no uniform *all-horizon* ceiling |

The distinctions are mathematical, not a universal physics theorem:

- FINITE_HORIZON_CEILING != ALL_HORIZON_VSTAR_FINITE.
- MANY_ALIGNED_WEAK_SHOTS != FREE_INFORMATION.
- G_HURWITZ != GLOBAL_STORAGE_FINITE.
- READOUT_RESET_MISALIGNMENT != AUTOMATIC_EUCLIDEAN_DISSIPATION.
- EXACT_NOISELESS_QUOTIENT_RANK != FINITE_UNIFORM_INVERSE_GAIN.
- DETERMINISTIC_L2_RECORD_CEILING != PHYSICAL_QUANTUM_FISHER_OR_MINIMAX_RESULT.
- GAUSSIAN_R13_PORT != SOURCE-VALID_SENSOR.
- TARGET_ERASURE != CONTROL_SUCCESS.

## 8. Scientific disposition

**EARNED, MATHEMATICAL ONLY:** exact, globally sharp, strength-sensitive finite-horizon aligned weak-readout energy bound; valid even for unstable G and infinite all-horizon V_*; uniform in finite sample count and varying aligned directions. Conditional transfer to LT5 gain-budget decisions and PRF11 fixed-noise sequential Gaussian risk (given exact matching of ports/model).

**MATHEMATICALLY MATURE HOSTS:** logarithmic matrix norm estimate, discrete energy dissipation, M13 ROT12 finite-T bound, scalar reset telescoping, ordinary Gaussian KL and two-point Bayesian lower bound. Novel theorem/physics claim is expressly denied.

**NOT EARNED:** all-horizon bound without finite V_* or other stability, misaligned reset extension without common storage, actual quantum apparatus, statistical claim without an explicit noise law, physical gravitational prediction, owner/independent referee acceptance.

Currentness: today's Slack dispatch reviewed; Geeky-S10 nonquadratic and action-family results already exist and are not counted as new work here. This note makes no request cascade. BW_INGESTION_UNKNOWN / OWNER_ACCEPTANCE_UNKNOWN.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
