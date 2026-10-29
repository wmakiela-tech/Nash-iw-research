---
artifact_id: IW_PRF12_R19_FINITE_HAHN_ECHO_RESET_ROBUST_CERTIFIED_SOURCE_DISCRIMINATION_001_20261029
created_at: 2026-10-29
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R18_PERSISTENT_XI_NONUNIFORM_ACTIVE_SWAPS_REMEDIATION
exposure: PUBLIC
canonical_body_path: research/prf12/2026-10-29/IW_PRF12_R19_FINITE_HAHN_ECHO_RESET_ROBUST_CERTIFIED_SOURCE_DISCRIMINATION_001_20261029.md
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_FINITE_PULSE_SINGLE_SENSOR_ECHO_LAW / ARBITRARILY_DEPENDENT_CAUCHY_RESET_HISTORY_EIGHT_RUN_RISK_CERTIFICATE / EXPLICIT_ASYMPTOTIC_CONTROL_COST / INDEPENDENT_2X2_4X4_REPRO_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NEW_CONTROL_CONTRACT_NOT_ORIGINAL_3PROBE_SWAPS / NO_UNRESTRICTED_SINGLE_COPY_LOCC_CLOSURE_GAP / NO_FIXED_DRIVE_CONSISTENCY_THEOREM / NO_ARBITRARY_ADVERSARIAL_XI / NO_NOVELTY_OR_PRIORITY_CLAIM / NO_EXPERIMENTAL_HARDWARE / NO_CANON / NO_EXEC_SIGN
---

# PRF12 R19 — Controlled Hahn echo with SOURCE ACTIVE during finite π pulse: reset-robust risk and explicit drive-amplitude law

**Data:** 2026-10-29. **Function:** PRF12. **Core achievement:** a source-typed, **distinct controlled experiment** differentiates static-Cauchy A from Lévy-B using only ONE sensor qubit per run. With a finite, SOURCE-ACTIVE square π pulse it gives a source-reset-history-agnostic eight-run risk certificate *under marginal Cauchy laws*. An explicit sequence of pulse strengths produces asymptotically vanishing decision errors while allowing ARBITRARY statistical dependence among the run-level hidden ξ values. Neither conclusion is about asymptotic closure of three-laboratory LOCC for the original passive three-probe states.

## 0. Source, prior art, and experimental-geometry subtraction

Internal first owner: PRF11 R35, same two source CLASSES (shared hidden static Cauchy versus independent Cauchy–Lévy increments): https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md .

R02's source-active noncommuting-gate control caveat: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R02_FINITE_DURATION_SWAP_CAUCHY_ACTIVE_PULSES_AND_RESOURCE_GATE_001_20261026.md . R16 ideal SWAP/X-Y source reset invariant test and R17 finite-SWAP perturbative resources: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-29/IW_PRF12_R16_RESET_AGNOSTIC_SOURCE_TEST_AND_SEPARATE_LIFETIME_CALIBRATION_001_20261029.md . R18 direct nonperturbative active SWAP and far-tail counterexample: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-29/IW_PRF12_R18_FULL_THREE_QUBIT_ACTIVE_SWAP_DYNAMICS_CAUCHY_TAIL_CERTIFICATE_001_20261029.md .

**Crucial subtraction:** R19 uses ONE SENSOR, ONE controllable π pulse, NO SWAP, NO memory qubits and NO spatially distributed three-probe state. It is an additional source-characterization CONTROL, not a replacement theorem for the passive three-probe LOCC resource gap. A shorter number of controlled trials is NOT a claim of superior intrinsic measurement optimality of those earlier, differently controlled protocols.

**Mature external first-owner method:** E. L. Hahn, *Spin Echoes*, Phys. Rev. 80, 580 (1950), DOI https://doi.org/10.1103/PhysRev.80.580 . Refocusing of quasi-static detuning and difference from memoryless dephasing is a standard principle; finite pulse detuning and Rabi rotations are also standard: *The Spin Echo, Entropy, and Experimental Design* (2019), https://www.mdpi.com/2504-3900/33/1/34 . The model-specific finite-pulse **quantile/error/resource certificate** below is an application in this project, with NO publication priority or claim of original echo invention.

## 1. Exact clock and source contract

Each run initializes ONE qubit in |+>=(|0>+|1>)/sqrt(2). Fix a physical clock T>0 and one finite π pulse of length 0<τ<T at the midpoint. There are free intervals Δ=(T−τ)/2 before and after the pulse; **T_phys=2Δ+τ=T**. Final measurement is X on the same qubit, and event "-" is evidence for Lévy-B. The pulse has rectangular drive Hamiltonian H_ctrl=πX/(2τ) (Rabi rate Ω=π/τ and spectral Hamiltonian norm π/(2τ)). No finite-period overlaps, free extra time or fictitious perfect gates.

A (static): within EACH run a single ξ is held fixed throughout both free intervals AND the **entire pulse**. Each run-indexed ξ_j has a marginal symmetric Cauchy(0,γ) law. Their JOINT distribution may be arbitrarily dependent (perfect persistence, independent resets, known/unknown reset grouping, other exogenous dependence); what is NOT allowed is changing ξ in the middle of a run or adapting the hidden source to the pulse/measurement outcomes in a way that destroys the Cauchy marginal contract. Conditional on the full ξ history, fresh qubit preparations and measurement shots are independent.

B (Lévy): independent symmetric Cauchy–Lévy increments on the sensor, during free AND controlled intervals, modeled by the Lindblad generator
 Dγ(ρ)=(γ/2)(ZρZ−ρ).
Noise increments are independent between runs. The B source does NOT sample one constant unknown detuning during a pulse; no illicit quasi-static B substitution.

No unknown memory loss, SPAM error, calibration drift, imperfect X projection, X-control amplitude noise, additional qubits, or decoherence beyond declared sources. The high-drive requirement is retained explicitly; an arbitrary fixed Ω_max would change the achievable pulse durations.

## 2. Exact single-run laws, INCLUDING finite active pulse

Write a=ξΔ, u=ξτ, h=sqrt(π²+u²). Conditional source-A propagators are

 U_f(ξ)=exp(−i ξΔ Z/2),
 U_p(ξ)=exp[−(i/2)(π X+ξτ Z)],
 U_A(ξ)=U_f U_p U_f.

Compute ⟨−|U_A(ξ)|+⟩ by using the X eigenbasis, in which Z swaps |+> and |−>. Elementary Pauli algebra yields EXACTLY

 \[
 \boxed{
 p_A^-(\xi;\tau,T)=
 \left[
 \cos(h/2)\sin(\xi\Delta)
 +(u/h)\sin(h/2)\cos(\xi\Delta)
 \right]^2.
 } \tag{R19.1}
 \]

This has been independently checked against the FULL 2×2 matrix exponential for 435 (ξ,τ) pairs, including ξ as large as 1e5, with absolute differences below 2e−10. At τ→0 with ξ fixed, h→π and the probability vanishes for every ξ, reproducing ideal echo.

For B, the Bloch equation during the X control is
 \dot r_x=−γ r_x,
regardless of the instantaneous Ω(t) around X; the X Hamiltonian commutes with the X expectation, and dephasing always damps it with rate γ. This holds also in both free intervals. Thus for the ENTIRE physical clock,

 \[
 \boxed{p_B^-=(1-e^{-\gamma T})/2.} \tag{R19.2}
 \]

This is EXACT for finite τ, not a perturbative lower bound, and it counts dephasing during the pulse. Verified against an independent explicit 4×4 Liouvillian expm for fifteen (γ,τ) settings. At γT=1 it equals 0.316060279414279.

**Ideal-pulse consequence (known Hahn-echo host):** p_A^-(ξ)=0 for EVERY ξ, no matter how long the hidden frequency survives between runs, while p_B^->0. The event "-" is then one-sided unambiguous evidence for B, with source reset schedule irrelevant. This does not contradict R14's original three-probe passive-output SEP no-go because the controlled output states are DIFFERENT.

## 3. Exact source-A finite-pulse error envelope; the Cauchy tail is essential

For h=sqrt(π²+u²)≥π,

 |cos(h/2)|=|sin((h−π)/2)|≤(h−π)/2=u²/[2(h+π)]≤u²/(4π),
 |u/h sin(h/2)|≤|u|/π.

Therefore for every |ξ|≤M,

 \[
 \boxed{
 p_A^-(\xi)\le \epsilon(M\tau):=
 \min\{1,[(M\tau)/\pi+(M\tau)^2/(4\pi)]^2\}.
 } \tag{R19.3}
 \]

No assumption of ξ having a finite first moment is used. For any δ∈(0,1), define the exact Cauchy quantile

 Mδ=γ cot(πδ/2),   Pr(|ξ|>Mδ)=δ.            (R19.4)

For N run-level hidden variables ξ_1,...,ξ_N with ARBITRARY statistical dependence but **each** having this marginal Cauchy distribution,

 Pr(there exists j with |ξ_j|>Mδ)≤Nδ.

If all |ξ_j|≤Mδ, independent fresh measurements conditional on the phase HISTORY have per-run "-" probabilities at most ε(Mδτ). Our decision is B if ANY of N local X measurements equals "-", else A. The resulting full source-A false-positive risk satisfies the quantitative, dependence-agnostic upper bound

 \[
 \boxed{
 P_A(\text{false B})
 \le \min\{1,N\delta+1-[1-\epsilon(M_\delta\tau)]^N\}.
 } \tag{R19.5}
 \]

Even without conditional independence, 1−(1−ε)^N can be replaced by Nε. Source B is i.i.d. between runs by source contract, so its exact miss risk is

 \[
 \boxed{
 P_B(\text{miss B})=
 [(1+e^{-\gamma T})/2]^N.
 } \tag{R19.6}
 \]

Important: arbitrary DEPENDENCE of Cauchy marginals across runs is NOT equivalent to arbitrary adversarial fixed ξ. The Cauchy tail control is a prior-distribution assumption, and the finite-pulse statement MUST NOT be represented as phase-uniform.

## 4. Explicit FINITE-PULSE, arbitrary reset dependence, BOTH-errors-below-5% witness

Choose source strength γT=1, one pulse τ/T=.0008, N=8 independent qubit preparations and measurements, and an audit quantile parameter δ=.004, with Mδ=γ cot(.002π). Then:

 - γ Mδ τ/γ = Mδ τ ≈0.127322278953 (in T=γ=1 units);
 - exact Cauchy cut Mδ/γ=159.1528486912807;
 - per-good-phase P_A^-≤ε≈0.00174874240972896;
 - A false-positive (B declared on ANY "-" among eight runs), even for arbitrary dependence/reset histories: **≤0.045904611302107** (4.5905%);
 - B missed: **0.047878728992407** (4.7879%);
 - B single-run event: p_B=0.316060279414279;
 - rectangular pulse drive: ΩT=πT/τ=**3926.99081698724** (Hamiltonian norm T=1963.495...).

Hence both conditional errors of this FINITE-WIDTH protocol are below 5% in the exactly described classical source family, including a single ξ persisting for all eight runs. There is no external entanglement, no memory qubits, no SWAP. The resource cost of strong X drive cannot be removed by rhetoric.

**Pulse-amplitude frontier is certified only SUFFICIENT, not exact:** optimize δ in R19.5 at fixed N=8. The largest τ/T allowed by THIS conservative inequality at γT=1 is ≈0.00091041815; it would require ΩT≈3450.714. No proof that a longer pulse cannot work with a sharper method. An easy nonoptimized choice .0008 and δ=.004 is preferred for an auditable comfortable margin.

Comparison under a DIFFERENT source-control resource budget: the passive ideal three-probe R16 randomized X/Y test used 80 runs/240 local qubit readings for average equal-prior error below 5%, with no echo drive, while here eight runs/eight readings with strong drive meet both conditional 5% errors. This is a SOURCE-CONTROL versus MEASUREMENT-RESOURCE tradeoff, NOT a superiority assertion for same task resources or physical implementability.

## 5. Theorem R19.2 — an asymptotically consistent reset-history-agnostic CONTROL schedule, with honest unbounded drive

For each N≥2 runs with γT=a>0 FIXED, choose

 \[
 \delta_N=N^{-2},\qquad\tau_N=T/N^3,\qquad
 \Omega_N T=\pi N^3.
 \]

Since cot z≤1/z on (0,π/2),

 Mδ_N τ_N = a N^{-3}cot(π/(2N²)) ≤2a/(πN).

Therefore by R19.3,

 ε_N≤[2a/(π²N)+a²/(π³N²)]²≤C(a)/N²,

where C(a)=[2a/π²+a²/π³]². Inserting into R19.5 and using Bernoulli inequality:

 \[
 \boxed{
 P_A(\text{false B})\le [1+C(a)]/N,\qquad
 P_B(\text{miss B})=[(1+e^{-a})/2]^N.
 } \tag{R19.7}
 \]

Both errors vanish for any sequence of Cauchy-marginal hidden run frequencies, with ANY dependence across runs, given the stated conditional preparation/measurement assumptions. At a=1, C(a)=0.05517514506425, so the simple A bound is 1.0551751451/N. The B miss decreases exponentially with N. The A risk bound is only O(1/N) because a union bound protects against arbitrary reset history.

**Cost ceiling:** Ω_N T~N³ diverges, and N physical runs consume N T total time and N one-qubit preparations. This is NOT an asymptotic theorem at fixed maximum drive, not original three-probe passive LOCC attainability, not a computational claim about process tensor testers, and no physical fixed-hardware device guarantee.

## 6. Negative knowledge R19.3 — phase-uniformity fails for every fixed nonzero pulse

For any fixed τ∈(0,T), take ξ_k=(2k+1)π/T and let k→∞. In R19.1, u=ξ_kτ→∞, h=|u|+O(1/|u|), u/h→sign(ξ). Therefore the conditional finite-pulse echo probability asymptotically becomes

 p_A^-(ξ_k)→ sin²(ξ_k T/2)=1.

Thus

 \[
 \sup_{\xi\in\mathbb R}p_A^-(\xi;\tau,T)=1
 \quad\text{for EACH }\tau>0.
 \]

A finite pulse has NO worst-case, all-real-ξ unambiguous guarantee. This does not harm the bounded-prior R19.5 certificate because those ξ_k move into increasingly remote Cauchy tails. Independent numeric checks at τ/T=.0008 and ξ≈6.28×10^5, 6.28×10^6, 6.28×10^7 yield false event probabilities ≈0.9999759, 0.99999976, 0.999999998, respectively.

This is the one-qubit controlled analogue of R18's nonuniform active SWAP warning, and a constraint any source-memory experiment must preserve.

## 7. Reproducibility, governance, falsifiers

Full local executable Python 3+NumPy+SciPy, fully independent:
\`IW_PRF12_R19_FINITE_HAHN_ECHO_REPRO_001_20261029.py\` under conversation local bundle. It runs:
1. **435** independent conditional-source-A 2×2 matrix-exponential comparisons, including very high detunings;
2. **15** independent source-B full 4×4 Lindblad channel comparisons;
3. ideal-echo limit and minimum N=8 for <5% B miss at γT=1;
4. finite τ=.0008, δ=.004 exact tail and both-condition risk certificate;
5. six τ values and optimized δ for sufficient bound, including τ≈.0009104 frontier;
6. three far-tail counterexample frequencies;
7. N=8,20,50,100,1000 verification of explicit O(1/N) bound and exponentially decreasing B miss.
A self-contained abbreviated GitHub mirror includes all analytic formulas and essential tests. Full code, run log, report and SHA-256 manifest packaged in local ZIP and cited separately.

Referee check-list:
- Confirm Pauli conventions and minus outcome, exact A pulse amplitude and full B master equation.
- Check no unmodeled source reset INSIDE any run, and source-A run-wise marginals Cauchy(0,γ) even when dependent.
- Check conditional independent measurement shots given full latent history; otherwise use weaker nε union bound.
- Check \(\sup_\xi p_A=1\) and that no phase-uniform claim slips into R19.5.
- Check fixed physical clock T, no FREE time erroneously added for τ.
- Check drive requirement, 8-run vs 80-run apples/oranges caveat and control-first prior-art subtraction.
- Check cross-references with R14 finite-fresh-block SEP no-go and R09 asymptotic LOCC closure OPEN: distinct quantum state/controls, no contradiction.
- Independently replay 2×2/4×4 matrices, exact Cauchy quantile and 8-run probability bounds.

**BW ingestion and independent referee pending; NO_CANON/EXEC/novelty.**

RETURN: PRF12_R19 / SOURCE_TYPED_NEW_HAHN_ECHO_CONTROL / EXACT_A_FINITE_PULSE_PROBABILITY / EXACT_B_ACTIVE_LINDBLAD_PROBABILITY / EIGHT_RUN_RESET_DEPENDENCE_AGNOSTIC_BOTH_5PCT_CERTIFICATE / EXPLICIT_NCUBED_DRIVE_SCALING_ASYMPTOTIC_CONSISTENCY / FAR_TAIL_PHASE_UNIFORMITY_NO_GO / INDEPENDENT_2X2_4X4_REPRO_PASS / REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / ORIGINAL_SINGLE_COPY_LOCC_CLOSURE_GAP_OPEN / GITHUB_PENDING_BW_INGEST.
