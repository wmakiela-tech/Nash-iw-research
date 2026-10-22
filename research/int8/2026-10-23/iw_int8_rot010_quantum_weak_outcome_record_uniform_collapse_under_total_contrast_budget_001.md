---
artifact_id: IW_INT8_ROT010_QUANTUM_WEAK_OUTCOME_RECORD_UNIFORM_COLLAPSE_UNDER_TOTAL_CONTRAST_BUDGET_001_20261023
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
date: 2026-10-23
problem_id: P2_LT5_G2_WEAK_QUANTUM_OUTCOME_RECORD_RESOURCE_BUDGET_001
document_type: EXACT_CONDITIONAL_QUANTUM_INSTRUMENT_INFORMATION_BOUND_AND_ORDER_SHARPNESS
exposure: PUBLIC
canonical_path: research/int8/2026-10-23/iw_int8_rot010_quantum_weak_outcome_record_uniform_collapse_under_total_contrast_budget_001.md
status: MATHEMATICS_SELF_CHECKED_AND_NUMERIC_WITNESS / INDEPENDENT_REFEREE_PENDING
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: MATURE_HOST_SPECIALIZATION / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# INT8 ROT010 — Quantum weak-outcome record collapses under bounded total measurement contrast, regardless of quantum backaction

## 0. Currentness, direct research interface and subtraction

On 2026-10-23 LT5 G2 requested a *legal CP quantum-instrument* answer, not a transfer of classical deterministic reset Q_s. INT8 ROT009 supplied one restricted commuting-state qubit instrument with exact matched one-step mean and nonselective target, while explicitly refusing pathwise equivalence. Geeky-S10 subsequently derived an exact Pauli-channel / observable-compatibility frontier with optimal transverse damage t_max=sqrt(1-s), a stronger COMPLETE CHANNEL geometry result. PRF11 R17 and Geeky's QND latent-bit work already analyze particular one-qubit repeated readout and distinguish quantum/classical Fisher information. These are all retained, not re-claimed.

Relevant source results:
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/int8/2026-10-23/iw_int8_rot009_restricted_qubit_instrument_realization_and_pathwise_nonmap_001.md
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s10/2026-10-23/geeky_s10_qubit_channel_observable_compatibility_frontier_001.md
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/IW_PRF11_R17_SAME_CHANNEL_DIFFERENT_INSTRUMENT_FISHER_MINIMAX_001_20261023.md
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-22/lt5_bloch_reset_noncp_exact_diamond_distance_and_instrument_nonmap_001.md

**New bounded bridge:** Weak quantum measurement *OUTCOME records alone* have a uniform asymptotic information-collapse theorem under a total contrast budget, for all finite adaptive quantum instruments with bounded binary POVM contrasts, regardless of their CP selective backaction. A legal QND Lüders witness makes the decision-rate O(epsilon) sharp. Unlike earlier INT8/Geeky classical Gaussian storage arguments this theorem is genuinely quantum-outcome-typed, uses only probability laws of physical POVMs, and never identifies a classical deterministic Q_s with a CPTP channel. Classical information inequalities and weak quantum POVMs are mature hosts, not new theory.

## 1. Exact carrier and quantifiers

One finite-dimensional quantum system with unknown initial state rho_theta in a family theta∈Theta; no new independent theta-preparations during the observed protocol.

At each finite shot j, an admissible common parameter-independent *predictable* classical policy may select an arbitrary outcome-indexed CP instrument {I_{j,+},I_{j,-}} depending on the entire previous binary record and public randomness. It may apply arbitrary intervening parameter-independent CPTP maps and unobserved unitary channels.

The effects of the two outcomes MUST be the near-fair bounded-contrast POVM
    E_{j,y}=I_{j,y}^*(I)=(I+y s_j A_j)/2,    y∈{-1,+1},
where A_j is Hermitian, ||A_j||_op≤1, and 0≤s_j≤epsilon<1. For a qubit, A_j may be an adaptive Pauli direction n_j·sigma. The effect formula is a definition of the admitted source class, NOT a generic property of every two-outcome detector; arbitrary biased effects are outside this theorem.

For each realized finite sequence, even with history-dependent stopping:
    sum_j s_j ≤ B < infinity
holds PATHWISE, with a deterministic B independent of theta and epsilon. The number of shots can vary with epsilon and observation history. Only the binary record and its predictable public controls/stop are retained in the **outcome-only experiment**. The terminal quantum system, hidden ancilla, unrecorded environment, any additional informative flag and later strong measurement are NOT part of this observed data.

The nonselective quantum channel, each selective CP map, posterior state, and causal intervention are arbitrary except for the stated effects and honest quantum legality. No common classical V*, quadratic P, classical Gaussian independent noise, source-matched Q_s, finite horizon T or free-generator G is assumed.

The unknown preparation theta can encode any initial quantum-state parameter, not necessarily linear theta v or a qubit Bloch coordinate.

## 2. Conditional one-shot bound (instrument-independent)

Given an observed classical history h before shot j, let rho_{theta,h} be the normalized current quantum state. Quantum Born probabilities give
    P_theta(Y_j=y | h) = Tr[E_{j,y}(h) rho_{theta,h}]
                       = [1+y z_{j,theta}(h)]/2,
    z_{j,theta}(h)=s_j(h) Tr[A_j(h)rho_{theta,h}].
Because ||A_j||≤1 and rho is a density matrix,
    |z_{j,theta}(h)| ≤ s_j(h) ≤ epsilon.                 (2.1)

The bound survives arbitrary preceding CPTP dynamics and feedback: no formula for the postmeasurement state is needed. It also holds for arbitrary quantum dimension and mixed preparations.

Define the reference process Q by feeding the SAME classical policy with independent fair ±1 coin outcomes at every admitted shot, using the same public random seed and stopping decisions. Q is parameter-free. Q need not be realized by the original physical instrument; it is only a comparison law on the same recorded data space.

## 3. Theorem 010.1: uniform quantum OUTCOME-only information collapse

Define
    f(z) = (1+z)/2 * log(1+z)
          +(1-z)/2 * log(1-z),       |z|<1.
Then f(z) is the KL divergence of the biased ±1 coin with mean z relative to the fair coin. Since
    f(0)=f'(0)=0,    f''(z)=1/(1-z²),
for |z|≤epsilon<1:
    0≤f(z)≤z²/[2(1-epsilon²)].                       (3.1)

For any common legal adaptive finite protocol pi satisfying §1, the sequential KL chain rule (with predictable stop) gives EXACT
    D_KL(P_theta^pi || Q^pi)
      = E_theta [sum_{j active} f(z_{j,theta}(H_{<j}))].
With (2.1), (3.1), and sum s_j²≤epsilon sum s_j≤epsilon B pathwise,
    D_KL(P_theta^pi || Q^pi)
      ≤ epsilon B/[2(1-epsilon²)] =: D_epsilon.      (3.2)

There is NO dependence on quantum channel, selective CP operation, measurement count, adaptive measurement directions or initial rho_theta. For random finite stopping time, one may sum the nonnegative conditional KL increments to the stop, or use bounded prefix limits; the public stop decision is a function of the existing history and seed, so adds no separate parameter-sensitive observation kernel.

By Pinsker,
    TV(P_theta^pi,Q^pi) ≤ sqrt(D_epsilon/2)
      = (1/2)*sqrt(epsilon B/(1-epsilon²)).          (3.3)
Taking a triangle inequality for any theta,theta':
    TV(P_theta^pi,P_theta'^pi)
      ≤ sqrt(epsilon B/(1-epsilon²)).                (3.4)
The bound may be capped by 1.

Therefore the outcome-only statistical experiment approaches a parameter-independent process uniformly if B is fixed as epsilon->0. The one-direction Le Cam deficiency to the parameter-free experiment is zero (discard data and draw Q), while the reverse direction is bounded by (3.3); hence the symmetric Le Cam distance is also ≤(3.3) for that comparison experiment.

Crucial: NO similar conclusion is asserted for the joint experiment including the terminal quantum system, a high-contrast final POVM, an ancilla, or a separate classical error-syndrome flag. Quantum information may remain inside or be recoverable from the system even when the weak binary record alone carries vanishing information.

## 4. Corollary 010.2: all-estimator squared-error risk rate

For Theta=[-R,R] and scalar initial label theta, let
    J_pi=inf_estimators sup_{|theta|≤R} E_theta[(hat theta-theta)²].
The constant estimator 0 proves J_pi≤R².

For the two-point prior theta=±R, let p_± be record densities relative to Q, m=(p_++p_-)/2, and b=(p_+-p_-)/(p_++p_-). The optimal Bayes estimator is R b, and its Bayes risk is
    R²[1 - E_m(b²)].
Furthermore,
    E_m(b²)
      = ∫ (p_+-p_-)²/[2(p_++p_-)]
      ≤ ∫(sqrt(p_+)-sqrt(p_-))²
      ≤ 2[∫(sqrt(p_+)-sqrt(q))²
          +∫(sqrt(p_-)-sqrt(q))²]
      ≤ 2[KL(P_+||Q)+KL(P_-||Q)]
      ≤4D_epsilon.
The penultimate inequality is the standard Hellinger–KL bound.

Thus uniformly across the entire legal protocol class:
    R²[1-2epsilon B/(1-epsilon²)]_+
      ≤ J_pi ≤ R².                                     (4.1)
This is an O(epsilon) upper bound on the attainable improvement in worst-case initial-parameter squared-error risk relative to abstention. It holds for B fixed and does not require an unbiased estimator.

The squared-error conclusion concerns only theta estimated from the binary record. No assertion on terminal actuator value, quantum channel fidelity, discord, or target restoration follows.

## 5. Sharpness in ORDER by a legal one-qubit QND Lüders instrument

Take input rho_theta=(I+theta Z)/2, theta∈[-R,R], 0<R<1. Each shot is the SAME legal unsharp Z Lüders instrument with effects (I±sZ)/2 and Kraus L_±=sqrt(E_±); no bitflip and no additional interventions. This is a QND measurement. Let N=floor(B/s).

On the commuting basis, an initial hidden eigenvalue A∈{±1} is drawn with P(A=±1)=(1±theta)/2 and remains unchanged throughout. Conditional on A, observed Y_j are iid with
    P(Y_j=y|A)=(1+y s A)/2.
This reproduces the standard QND latent-bit host already identified by Geeky-S10, not a new quantum phenomenon.

For S_N=sum_j Y_j, exact moments:
    E_theta S_N = N s theta,
    E_theta S_N² = N(1-s²)+N²s².                    (5.1)

Consider the linear shrinkage estimator
    hat theta = t_s S_N,
    t_s = R² s/[1+(N-1)s²].
Then for sufficiently small s with 2 t_s N s ≤1, the worst-case MSE over [-R,R] occurs at ±R and is EXACT
    sup risk
     = R² - [R⁴ N s²/(1+(N-1)s²)].                  (5.2)
Consequently, with fixed B:
    R² - sup risk
      ~ R⁴ B s,       s->0.                           (5.3)

Thus the O(epsilon) worst-case decision improvement bound (4.1) is **sharp in order** within the admitted class, even though its universal constant is conservative. The instance has a genuine CP instrument and exactly one prepared qubit. It is NOT the classical co-aligned Q_s reset model: the unsharp Z Lüders channel preserves Z and damps transverse Bloch components.

For the endpoint eigenstate preparations theta=±1 (used ONLY as an information-separation comparison, not in the minimax example restricted to R<1), the record laws are independent biased coins with means ±s. For N≈B/s their TV separation has asymptotic order sqrt(Bs); thus the Le Cam/TV order O(sqrt epsilon) also cannot be globally improved for this outcome-only POVM class.

## 6. Numerical / source reproducibility

Self-contained NumPy code in this same research/int8/2026-10-23/ directory checks:
- Kraus normalization and the exact QND record law on the commuting family;
- one-shot coin KL formula and inequality (3.1);
- risk and the witness asymptotic (5.2)–(5.3) for several s at B=1,R=.6;
- finite-N exact sampling moments and the upper-bound comparison.
Finite-matrix controls are supportive; §2–5 proofs are analytic.

This result makes no new external-paper originality claim; host formulas are mature quantum information, sequential relative entropy and statistical decision theory. For example instruments and measurement channels are reviewed by Davies–Lewis and standard textbook presentations; the source-native NASH interpretation is limited to a conditional abstract gate.

## 7. Cross-front return / one-problem-one-state

problem_id: P2_LT5_G2_WEAK_QUANTUM_OUTCOME_RECORD_RESOURCE_BUDGET_001
best_result: Theorem 010.1 quantum Born-coin KL collapse independent of selective CP maps + Corollary 010.2 all-estimator risk gap with order-sharp QND witness.
prior_results: LT5 ROT06 global nonCP barrier; Geeky-S10 exact channel-observable compatibility; INT8 ROT009 restricted mean/channel construction; PRF11 R17 one-copy information and QND latent-bit host.
counterresults: strong final measurement of terminal quantum system or side syndrome breaks outcome-only claim; unbounded total contrast B, non-near-fair POVM, repeated fresh preparations or informative unlogged flag violate carrier.
original_source: declared adaptive POVM effects E_{j,y}, not an actual NASH physical readout implementation.
independent_referee: PENDING.
owner: LT5 Chapter 5 / Geeky-S10 instrument host / PRF11 decision host. INT8 scientific integration only.
blocker: no original physical detector CP maps, source-validated noise/cost s->resources, terminal intervention data, or independent reviewer.
cheapest_discriminator: for a proposed concrete physical protocol, extract outcome POVM eigenvalue contrast per shot, verify that ALL recorded data are covered, and source-validate pathwise sum s_j before attempting (3.2); also include the terminal system if accessible.
decision: PASS as mathematical quantum-outcome-only theorem; HOLD source-native NASH hardware and complete quantum process/terminal-control claims.
canonical_path: research/int8/2026-10-23/iw_int8_rot010_quantum_weak_outcome_record_uniform_collapse_under_total_contrast_budget_001.md
bw_status: GITHUB_PENDING_BW_INGEST / OWNER_ADOPTION_NOT_CLAIMED

NO_NEW_TASK_CASCADE / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
