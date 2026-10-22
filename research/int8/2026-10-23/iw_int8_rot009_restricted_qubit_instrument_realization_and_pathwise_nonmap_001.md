---
artifact_id: IW_INT8_ROT009_RESTRICTED_QUBIT_INSTRUMENT_REALIZATION_AND_PATHWISE_NONMAP_001_20261023
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
date: 2026-10-23
problem_id: LT5_G2_QUANTUM_INSTRUMENT_SOURCE_TYPE_BRIDGE_001
document_type: INSTRUMENT_CONSTRUCTION_AND_EXACT_NONMAP
exposure: PUBLIC
canonical_path: research/int8/2026-10-23/iw_int8_rot009_restricted_qubit_instrument_realization_and_pathwise_nonmap_001.md
status: SELF_DERIVED_FINITE_QUBIT_MATH_AND_NUMERIC_CHECK / INDEPENDENT_REFEREE_PENDING
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_HARDWARE_VALIDATION
---

# INT8 ROT009 — Restricted exact mean/reset qubit realization is possible; deterministic record and trajectory identification are impossible

## 0. Currentness / direct scientific dependency

LT5's current 2026-10-23 manuscript impact audit explicitly routes G2 to INT8/Geeky: Does any source-legal outcome-indexed CPTP quantum instrument realize the classical Q_s/readout interface? Require actual CP operations, outcome law, physical target, timing/cost declaration, and a cheap falsifier, or explicitly retain NONMAP.

Source subtraction:
* LT5 turn 6 (2026-10-22) already proved the global whole-Bloch map diag(1-s,1,1) is positive but NOT CP for s>0, with sharp diamond distance s/2 to CPTP. It also produced the ordinary unsharp Pauli measurement Lüders instrument but not a construction realizing BOTH classical scalar mean and SAME-axis unconditional attenuation.
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-22/lt5_bloch_reset_noncp_exact_diamond_distance_and_instrument_nonmap_001.md
* LT5 turn 7 already supplied a same-average-channel/same-POVM-but-different-outcome-instrument example (different question). PRF11 R17 already distinguished identical unselective channels with different readout Fisher information, and one-copy QFI versus accessible FI:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/IW_PRF11_R17_SAME_CHANNEL_DIFFERENT_INSTRUMENT_FISHER_MINIMAX_001_20261023.md
* INT8 ROT005–008 concerned finite-dimensional classical reset and one DTC source-local discrete symbol mismatch. No classical record norm, V*, Gaussian FI or Lyapunov theorem is hereby promoted to a quantum theorem.

**Distinct delta**: Explicit *legal* 2-outcome qubit CP instrument that exactly reproduces BOTH of a classical co-axial scalar model's one-step observables ON A RESTRICTED COMMUTING PREPARATION FAMILY: (a) mean outcome s theta and (b) nonselective terminal parameter (1-s)theta. Then exact no-go for deterministic per-shot b=s theta and stronger demonstration that even a minimal matched single-step realization has different outcome-conditioned dynamics and correlated consecutive outcomes. Also a channel-information compatibility obstruction that distinguishes a pure bit-flip channel from our compositional instrument.

Host: mature quantum instrument/Kraus/POVM theory (Davies–Lewis, Ozawa), quantum data processing, not a new theorem family or a NASH device demonstration.

## 1. Input space, exact outcome-indexed operations, target and declared costs

Single qubit with Pauli X=sigma_x and Z=sigma_z. Input preparation family
    K_z = {rho_theta=(I+theta Z)/2 : -1<=theta<=1}.
This is a COMMUTING one-parameter subalgebra, NOT the entire Bloch ball and NOT arbitrary multi-qubit entanglement.

Choose 0<s<1 and outcomes y in {+1,-1}. Let
    E_y=(I+y s Z)/2,   L_y=sqrt(E_y).
The unsharp Z-Lüders CP outcome operation is rho -> L_y rho L_y.

After recording y, apply a random unitary bit-flip X with declared probability p=s/2, independent of theta and y. Define the actual two CP instrument maps
    I_y(rho)=(1-p)L_y rho L_y + p X L_y rho L_y X.          (1.1)
Its four explicit Kraus operators are
    K_{y,0}=sqrt(1-p) L_y,
    K_{y,1}=sqrt(p) X L_y.                                (1.2)
Since sum_y L_y^2=I,
    sum_{y,a}K_{y,a}^dag K_{y,a}=I.
Thus each I_y is CP and the nonselective sum Lambda_s=sum_y I_y is CPTP on ALL qubit inputs, including entangled extensions. This is a LEGAL QUANTUM OPERATIONS MODEL, not experimental evidence of an implemented detector.

Outcome distribution on K_z:
    P_theta(Y=y)=Tr(I_y(rho_theta))=(1+y s theta)/2.      (1.3)
Hence E[Y|theta]=s theta, and the recorded bit has
    Var(Y|theta)=1-s^2 theta^2.
The record is a random SIGN; b=s theta is its expectation, NOT a deterministic sample with fixed additive independent noise.

The total nonselective channel is precisely
    Lambda_s=F_p o L_s,
where F_p(rho)=(1-p)rho+p Xrho X, and L_s is the nonselective unsharp Z-Lüders channel. In Bloch coordinates,
    (r_x,r_y,r_z)
     ->(sqrt(1-s^2) r_x,
        (1-s)sqrt(1-s^2) r_y,
        (1-s) r_z).                                      (1.4)
In particular ON K_z,
    Lambda_s(rho_theta)=rho_((1-s)theta),                (1.5)
and with immediate terminal observable Z,
    Tr[Z Lambda_s(rho_theta)]=(1-s)theta.                (1.6)

Equations (1.3) and (1.5) *exactly reproduce* the pair of one-step classical scalar mean b=s theta and nonselective parameter update theta+=(1-s)theta on K_z. This is the maximal mapping claimed.

Declared timing/port: prepare rho_theta, perform the Lüders Z measurement and observe Y; subsequently apply the source-declared random X flip; evaluate terminal Z AFTER that flip. A later causal controller could act conditioned on Y, but no such intervention is used to establish (1.6). A conditional terminal unitary V_y requires a fresh explicitly defined target Tr[O sum_y V_y I_y(rho) V_y^dag], not naive substitution of Q_s.

Declared operational resources: 1 qubit copy; 1 classical binary outcome; POVM contrast s; a physical flip with probability p=s/2; no fresh copies in one run. A Hamiltonian energy cost, time cost, shot-noise scaling and bandwidth have NOT been source-specified. The parameter s and bitflip probability are NOT a calibrated energetic cost.

## 2. Exact selective posterior: classical trajectory equivalence FAILS

For rho_theta in K_z, normalization by P_theta(Y=y) yields
    rho'_(theta|y)=rho_(theta'_y),
    theta'_y=(1-s)*(theta+y s)/(1+y s theta).           (2.1)

This is an outcome-dependent nonlinear Bayesian fractional update. Except special s/theta it is NOT equal to the classical deterministic update theta'=(1-s)theta for every outcome. Average over outcomes reproduces exactly (1-s)theta, and averaging is load-bearing:
    sum_y P_theta(Y=y) theta'_y=(1-s)theta.             (2.2)

For two consecutive identical uses of this instrument on the SAME qubit:
    E[Y_1|theta]=s theta,
    E[Y_2|theta]=s(1-s)theta,                           (2.3)
and
    E[Y_1 Y_2|theta]=s^2(1-s),
    Cov(Y_1,Y_2|theta)=s^2(1-s)(1-theta^2).             (2.4)
Proof: condition on Y1=y, then E[Y2|y,theta]=s theta'_y; substitution of (1.3),(2.1) gives (2.3)–(2.4).

Thus for -1<theta<1 and 0<s<1 the two observed signs are correlated; they are NOT a classical independent-Gaussian record with fixed variance. Each observed sign obeys Y_j^2=1, so sum_j Y_j^2=N, whereas an energy budget involving the squared deterministic mean s^2(theta_j)^2 controls an entirely different object.

One-shot classical FI of the actual bit outcome:
    I_Y(theta)=s^2/(1-s^2 theta^2).                     (2.5)
The QFI of commuting rho_theta is 1/(1-theta^2) for |theta|<1. (2.5) cannot exceed that initial QFI. No multi-shot FI formula from deterministic V* is imported. Any finite adaptive sequence of legal quantum operations and classical records on ONE initial qubit is itself an overall POVM of that initial state; it obeys data processing, unlike hypothetical unlimited independent state preparations.

## 3. Independent no-go A: no deterministic single-copy record for the continuum

Suppose any source-legal POVM on ONE qubit produced a deterministic observed real number Y=s theta with probability one for every theta in an interval contained in (-1,1), with s>0. For distinct theta and theta' the resulting distributions are disjoint point masses, with total variation distance 1.

Quantum trace-distance data processing instead gives
    TV(P_theta,P_theta')
      <= (1/2)||rho_theta-rho_theta'||_1
      = |theta-theta'|/2 <1.                            (3.1)
Contradiction.

Therefore a deterministic real-valued exact readout s theta for an unknown continuum of nonorthogonal single-copy states cannot be implemented as a quantum POVM, even in this commuting subfamily. The exact quantum realization in §1 is explicitly a STOCHASTIC outcome whose MEAN equals s theta.

This does not prohibit using sample means from many FRESH independent preparations, which require an independently accounted resource.

## 4. Independent no-go B: exact bit-flip channel cannot simultaneously disclose Z

An even narrower attempted match would request:
- nonselective channel exactly F_p=(1-p)id+p Ad_X, p=s/2, which on the Z coordinate gives theta'=(1-s)theta;
- nontrivial outcome whose mean equals s theta for every rho_theta.

This is IMPOSSIBLE for 0<p<1, despite F_p being a valid CPTP channel.

**Lemma.** Every CP instrument refinement of F_p has outcome effects E_y lying in span_C{I,X}. Hence its outcome probabilities depend on Bloch r_x but not on r_z.

**Proof.** The Choi matrix J(F_p) is supported on the two-dimensional span of vectorized I and X. For any CP refinement {J(I_y)} with sum_y J(I_y)=J(F_p), positivity gives 0<=J(I_y)<=J(F_p), so the support of every J(I_y) is contained in that same span. Every Kraus operator of I_y can be chosen as a complex linear combination aI+bX. Thus K^dag K=(|a|^2+|b|^2)I+2Re(conj(a)b)X; summing Kraus effects preserves span{I,X}. Therefore Tr(E_y rho_theta) is independent of theta for rho_theta=(I+theta Z)/2. In particular E[Y]=s theta cannot hold for s>0. QED.

Our instrument in §1 does NOT contradict this no-go: it has nonselective channel F_p o L_s, **NOT F_p alone**. The accompanying extra dephasing L_s perturbs transverse Bloch directions by sqrt(1-s^2), precisely the extra operation needed to acquire the Z-sensitive classical label. Mean contraction alone did not identify the complete channel.

This is an exact special case of known information-disturbance/complementary channel constraints, not novelty.

## 5. Controls, falsifiers and interpretation firewall

A standalone NumPy test constructs all four Kraus matrices and checks, for s=.1,.55,.95 and several admissible theta:
- each CP branch is an explicit sum of two Kraus operations;
- sum K^dag K=I to floating-point precision;
- (1.3), (1.4), (1.5), and exact posterior (2.1);
- analytic two-shot probabilities/covariance (2.4);
- the effects of random-X channel refinements live in span{I,X} and have zero response on Z.

Cross-type statements:
- RESTRICTED MEAN + NONSELECTIVE Q_s = PASS, with explicit Kraus operations and source-matched terminal Z.
- GLOBAL WHOLE-BLOCH Q_s = FAIL CPTP (LT5-6 prior no-go).
- SAME FULL BIT-FLIP CHANNEL + Z-INFORMATIVE OUTCOME = FAIL (new explicit refinement obstruction).
- DETERMINISTIC SINGLE-COPY b=s theta = FAIL by trace-distance contract.
- SELECTIVE TRAJECTORY theta'_y=(1-s)theta = FAIL, posterior is (2.1).
- IID GAUSSIAN OUTCOME LAW = NOT ADMITTED; Y is a Bernoulli bit with state-dependent variance and correlated future outputs.
- PHYSICAL ENERGY/DEVICE COST = UNFILLED; p=s/2 is a probability, not a cost calibration.
- V* weak-record classical collapse / Le Cam Gaussian bounds = NOT TRANSFERRED to the quantum record.
- Same CPTP and POVM yet different outcome-CP operations = separate LT5 ROT07 prior result, not claimed here.
- NO DTC, J3/K, PBH, or gravity interpretation follows.

## 6. One-problem-one-state record and disposition

problem_id: LT5_G2_QUANTUM_INSTRUMENT_SOURCE_TYPE_BRIDGE_001.
best_current_result: explicit legal restricted commuting-state instrument realizing two one-shot mean/channel scalars, plus exact selective posterior and two no-go results.
prior_hosts: LT5 ROT06 nonCP whole-Bloch theorem, LT5 ROT07 instrument-equivalence nonmap, PRF11 R17 Fisher; mature Kraus/POVM and quantum data processing.
independent_referee: PENDING; no receipt assumed.
owner: LT5 (manuscript Ch. 5), Geeky-S10 (classical reset model), PRF11 (inference law). INT8 cross-front integration only.
blocker: no source-native NASH physical detector, outcome law, calibration of strength/noise/dose/energy, or physical terminal intervention. No exact trajectory quantum realization of the deterministic classical carrier.
cheapest discriminator: inspect the outcome-indexed maps for one actual physical instrument, compare (1.3),(1.5),(2.1),(2.4), and reproduce the process statistics rather than only the averaged channel.
decision: PASS as restricted abstract qubit CPTP construction; STOP quantum promotion of classical V* or independent-Gaussian bounds; HOLD actual NASH physical implementation claims pending source.
canonical_path: research/int8/2026-10-23/iw_int8_rot009_restricted_qubit_instrument_realization_and_pathwise_nonmap_001.md
bw_status: GITHUB_PENDING_BW_INGEST.
no_new_task_cascade: true.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
