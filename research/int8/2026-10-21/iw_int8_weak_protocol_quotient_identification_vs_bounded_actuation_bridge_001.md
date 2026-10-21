---
artifact_id: IW_INT8_WEAK_PROTOCOL_QUOTIENT_IDENTIFICATION_VS_BOUNDED_ACTUATION_BRIDGE_001_20261021
date: 2026-10-21
from: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
function: CROSS_FRONT_SCIENTIFIC_INTEGRATION / SPIDER
type: CONDITIONAL_MATHEMATICAL_BRIDGE / POSITIVE_CONSTRUCTION / CHEAP_FALSIFIER
exposure: PUBLIC
status: EXACT_FINITE_DIMENSIONAL_DERIVATION / MATURE_HOST_SPECIALIZATION / NOT_INDEPENDENTLY_REVIEWED
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE
derived_from:
  - research/geeky-s10/2026-10-19/geeky_s10_fixed_sensor_available_storage_001.md
  - research/int8/2026-10-19/iw_int8_target_selective_storage_bridge_001.md
  - research/lt5/2026-10-20/lt5_target_information_vs_actuation_bounded_feedback_exact_gate_001.md
source_currentness: SLACK_DISPATCH_READ_2026-10-21 / NO_NEW_DIRECT_INT8_EXECUTION_TASK_VERIFIED
bw_ingestion: NOT_VERIFIED
---

# INT8 — Finite weak-sensor quotient identification is not bounded actuation

## 0. Question and type of the bridge

Geeky-S10 proves that the exact all-protocol indistinguishability kernel of the classical fixed-sensor reset-flow model is the ordinary unobservable space N_e. LT5 establishes a separate exact minimax gate for a *fixed* linear observation matrix C, a *declared* terminal target m and actuation port a. The cross-front question is whether the all-protocol quotient can be distinguished by **one weak finite protocol**, and what that does and does not buy in LT5's bounded-gain decision class.

**BRIDGE TYPE:** finite-dimensional quotient embedding by a protocol, followed by a **conditional** target-risk/actuation factorization. Neither physical-system equivalence nor a theorem about general quantum measurement.

The scientific contribution relative to the project record is a typed *combination* of familiar sample-based observability, reset maps and robust optimal recovery. No mathematical novelty is claimed. In particular, the 2025 work of Krauss, Lopez and Müller on sample-based functional observability is a mature prior-art host; details of the reset/backaction case must be distinguished from generic passive sampling.

## 1. Exact model

Work on X=R^n with generator G in R^{n x n} and fixed ||e||=1. Let Q_s=I-s e e^T, with **measurement strength** 0<s<1 and Geeky notation u=1-s in (0,1). Between measurements, x(t+tau)=exp(G tau)x(t). The normalized j-th noiseless observed scalar is

  b_j = s e^T x(t_j^-)= gamma*c_j,

where all measurements use the same strength s and same e. The resets Q_s act on the state and are part of the exact forward operator. Choose a deterministic finite protocol with strictly ordered times 0<t_1<...<t_r<T; no adaptation or measurement-outcome-dependent control.

Define its *single-protocol* initial-state observation matrix C_s by b=C_s x_0. If t_0=0 and Delta_j=t_j-t_{j-1}, its j-th row is

  (C_s)_{j,:} = s e^T exp(G Delta_j) Q_s exp(G Delta_{j-1}) ... Q_s exp(G Delta_1),

with the obvious omission of reset factors for j=1. Since Q_s tends to I as s tends to zero, C_s/s tends entrywise to the passive sample matrix M whose j-th row is e^T exp(G t_j).

The common unobservable subspace is

  N_e = intersection_{k=0}^{n-1} ker(e^T G^k)
      = {x: e^T exp(Gt)x=0 for every t>=0}.

Write r=n-dim N_e and O=N_e^perp. The target quotient X/N_e is naturally identified with O after fixing Euclidean geometry.

## 2. Positive finite-protocol theorem

**Proposition.** If r>0, then for *every* T>0 there exist r distinct measurement times in (0,T) and s_0>0 such that for every 0<s<s_0 the corresponding finite non-adaptive protocol satisfies

  ker C_s = N_e,  rank C_s=r,

so a single legal finite weak protocol exactly separates all observable equivalence classes. On O, its smallest singular value obeys

  sigma_min(C_s|_O) = s sigma_min(M|_O)+O(s^2),

where sigma_min(M|_O)>0, and ||C_s||=O(s).

**Proof.** Since t -> e^T exp(Gt)x is real analytic, any x annihilated by every row e^T exp(Gt) for t in an open interval (0,T) annihilates that analytic function for all t, hence x belongs to N_e. Therefore the span of passive sampling rows over (0,T) is O^* and, by finite-dimensionality, admits r linearly independent rows at distinct ordered times. For these choices M|_O has rank r. The map s -> C_s/s extends analytically to s=0 and equals M there; the rank-r determinant of its restriction to O is nonzero at s=0 and stays nonzero for all sufficiently small positive s.

For x in N_e, the free flow preserves N_e, e^T x=0, and Q_s x=x; every protocol output is zero, so N_e is contained in ker C_s. Rank r then implies equality. Finally C_s=s(M+O(s)); singular-value perturbation gives the asserted first-order scaling on O and norm upper bound. QED.

**Important quantifier:** this is existence of ONE jointly separating finite protocol with sufficiently small **positive** strength, not a uniform lower singular-value bound as s->0; at s=0 the map is zero. Nor does finite separation imply finite all-protocol available storage V_* for an unstable or noncontractive G.

## 3. Minimal recovery gain for a declared functional

Fix a nonzero target m in O and assume exact noiseless record b=C_s x_0. Since ker C_s=N_e, there exists w_s in R^r with C_s^T w_s=m. Hence m^T x_0=w_s^T b, i.e. target reconstruction is **algebraically exact**.

But its measurement-to-target gain must diverge as strength vanishes:

  ||w_s|| >= ||m||/||C_s|| = Omega(1/s),

and the pseudoinverse solution satisfies

  min_{C_s^T w=m} ||w|| = O(1/s).

Thus the minimal exact linear recovery gain is Theta(1/s), for fixed m !=0 and the frozen sampling times. With deterministic additive observation error ||eta||<=delta, exact-unbiased target reconstruction has worst-case error delta||w_s||, which is of order delta/s. This is a constraint on the **exact-cancellation choice** w_s, NOT a claim that optimal bounded-risk recovery diverges: choosing w=0 keeps the error at R||m||.

## 4. Legal port to LT5: include the backaction in the target

LT5 assumes observations b=C y+eta and a scalar terminal expression z=m^T y-a^T F b with ||F||<=kappa. A naive use of the **no-backaction** terminal m together with the **reset-flow** C_s is illegal: Geeky's Q_s changes the path.

For an actual terminal observable ell^T x(T), after all r reset measurements and **before** any independently declared actuator, define the source-matched terminal map Phi_s from x_0 to x(T). The correct target row is m_s^T=ell^T Phi_s. If a terminal actuator u is separately installed with known sensitivity a_s and linear correction u=-F(b+eta), and the actuator intervention does not retroactively change the recorded outputs, then the target residual is

  z = m_s^T x_0 - a_s^T F (C_s x_0+eta).

Only for this **declared classical actuation contract**, with independent Euclidean uncertainty balls ||x_0||<=R, ||eta||<=delta, does LT5's exact formula apply:

  J_kappa(s)
  = min_{||w||<=kappa||a_s||}
    [ R||m_s-C_s^T w|| + delta||w|| ]              for a_s !=0,

and J_kappa(s)=R||m_s|| if a_s=0.

A target on the original preparation m^T x_0 is likewise meaningful as a **decision/estimation** target, but is not by itself a physical terminal observable. This is the earliest type break for claims identifying Geeky's readout with LT5's physical terminal control.

## 5. Exact weak-sensor/finite-actuator mismatch

Suppose the source-matched terminal target m_s -> m_0 !=0, a_s stays bounded, and the number of samples/times are fixed as above. Because ||C_s||=O(s), for every fixed finite controller gain kappa:

  R ( ||m_s|| - kappa||a_s|| ||C_s|| )_+
  <= J_kappa(s) <= R||m_s||.

(The lower bound drops the nonnegative noise penalty and uses the reverse triangle inequality. The upper bound chooses F=0.)

Therefore:

  lim_{s->0+} J_kappa(s) = R||m_0||.

So **even though every sufficiently small nonzero s gives exact algebraic identifiability of the observable quotient**, a bounded-gain correction cannot produce a nonvanishing guaranteed improvement over doing nothing as the measurement strength tends to zero, for a fixed nonzero terminal target. This holds already at delta=0. Under nonzero delta, exact recovery generally amplifies the declared readout disturbance.

The limit statement presumes a fixed number of samples and one specified protocol family; it does not extend to an arbitrary number of measurements scaled with s, adaptive choices, joint continuous-time feedback, unlimited independent preparations, or different physical cost rules.

## 6. Explicit two-state falsifier with source-matched physical target

Let

  G=[[-1,1],[0,-1]],  e=(1,0)^T,  gamma=1.

Use a first reset reading at t_1=0 and a second at t_2=1; this endpoint-time choice is immaterial to the existence statement, which can instead choose times strictly within (0,T). Let u=1-s. Then

  C_s = s [[1,0],[exp(-1)*u,exp(-1)]].

Its determinant is s^2 exp(-1)>0 for all s>0, so one two-reading protocol is exactly injective on R^2. Yet both singular values tend to zero proportional to s. (For this explicit variant, a reading is permitted at t=0.)

For the physical terminal target x_2(1^+) after both Q_s resets, the exact source-matched row is

  m_s^T=(0,exp(-1))

because free flow and e_1 resets leave x_2 unaffected. Install a **separate** scalar terminal control u_ctrl that adds to x_2(1^+) with a=1, and use the static feedback u_ctrl=-w^T(b+eta). Then exact cancellation at delta=0 requires

  C_s^T w = m_s,

whose unique solution is

  w_2=1/s,  w_1=-(1-s)exp(-1)/s,

with exact gain

  ||w|| = sqrt(1+(1-s)^2 exp(-2))/s.

At s=0.1, the gain is approximately 10.534, so kappa=1 cannot cancel the target although both initial-state coordinates are noiselessly identifiable. At nonzero delta, insisting on exact cancellation incurs worst-case noise penalty delta||w||; this is not the minimax optimum when regularization/abstention is preferable.

This explicit finite-dimensional witness respects the earlier-port prohibition: the measured trajectory **does** contain resets, the physical terminal target is computed **after** the resets, and the actuator is a separately declared terminal intervention.

## 7. Cross-front disposition and falsification

POSITIVE_BRIDGE:
- Geeky all-protocol observational equivalence -> ONE finite weak protocol quotient embedding (under finite-dimensional analytic LTI and fixed e assumptions).
- LT5 target-relative control formula -> exact source-matched per-protocol decision gate with Q_s reset effects folded into m_s.
- Exact identification and arbitrarily weak reset do not produce a finite **uniform** inverse gain or physical actuation capability.

NEGATIVE KNOWLEDGE:
- ALL_PROTOCOL_KERNEL_EQUAL_N_e != ONE_ARBITRARY_PROTOCOL_KERNEL_EQUAL_N_e.
- ONE_FINITE_PROTOCOL_FULL_RANK != UNIFORM_CONDITIONING_AS_STRENGTH_GOES_TO_ZERO.
- FIXED_SENSOR_DATA_SUFFICIENCY != BOUNDED_GAIN_TARGET_CORRECTION.
- MINIMAL_EXACT_RECOVERY_NOISE_PENALTY != OPTIMAL_MINIMAX_RISK.
- CLASSICAL_RESET_BACKACTION != SOURCE-VALID_QUANTUM_INSTRUMENT.
- ORIGINAL_PREPARATION_TARGET != PHYSICAL_TERMINAL_TARGET_WITHOUT_Phi_s.
- MEASUREMENT_STRENGTH != AUTOMATICALLY_KAPPA_OR_ACTUATOR_COST.

CHEAPEST REOPEN/DIFFERENTIATOR:
- If a target protocol claims escape, explicitly specify how sample number, measurement strength, total horizon, noise scaling, available actuator port or control policy class depends on s and recompute the correct forward/terminal maps. If these parameters are fixed as here, the limit obstruction above applies. For genuinely adaptive or quantum instruments, this note supplies no theorem.

PRIOR-ART SUBTRACTION:
- Ordinary finite-dimensional observability and finite-sampling/functional observability are established control-theory hosts. I. Krauss, V. G. Lopez, M. A. Müller, *On Sample-Based Functional Observability of Linear Systems*, IEEE Control Systems Letters 9 (2025), 1393–1398, DOI 10.1109/LCSYS.2025.3582512, https://arxiv.org/abs/2506.23744.
- Willems dissipativity/available storage and LT5's cited optimal-recovery/robust-output-feedback hosts absorb the decision/control layer. No independent mathematical novelty is established by combining them.
- Geeky-S10's exact fixed-sensor reset-flow characterization and INT8's selective P certificate remain independent source-typed project results. Their mathematical/external-review authority is unchanged.

OWNER_ACCEPTANCE: UNKNOWN.
BW_INGESTION: UNKNOWN.
NO_NEW_TASK_CASCADE.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE.
