---
artifact_id: IW_PRF12_R18_FULL_THREE_QUBIT_ACTIVE_SWAP_DYNAMICS_CAUCHY_TAIL_CERTIFICATE_001_20261029
created_at: 2026-10-29
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R17_SOURCE_ACTIVE_FINITE_SWAP_DIRECT_DYNAMICS
exposure: PUBLIC
canonical_body_path: research/prf12/2026-10-29/IW_PRF12_R18_FULL_THREE_QUBIT_ACTIVE_SWAP_DYNAMICS_CAUCHY_TAIL_CERTIFICATE_001_20261029.md
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_FULL_MODEL_EVOLUTION_FORMULAE / NUMERICAL_SOURCE_TV_TEST_PASS / ANALYTIC_CAUCHY_TAIL_AND_LIPSCHITZ_ENCLOSURES / NONUNIFORM_STATIC_XI_COUNTERSEQUENCE / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_FULL_SINGLE_RUN_LOCC_CLOSURE_GAP / NO_EXPERIMENTAL_DEVICE / NO_GLOBAL_READOUT_OPTIMALITY / NO_FORMAL_INTERVAL_ARITHMETIC_FOR_MATRIX_EXP / NO_NOVELTY_OR_PRIORITY_CLAIM / NO_CANON / NO_EXEC_SIGN
---

# PRF12 R18 — Full active two-SWAP dynamics, controlled Cauchy-tail integration and source-memory countersequence

**Data:** 2026-10-29. **Właściciel/funkcja:** PRF12. **Wynik główny:** obliczyłem bezpośrednio cały fizycznie używany układ **trzech** kubitów: sensor S i dwie pamięci M1,M2. Trzy eksponowane próbki logiczne to kolejno M1, M2 i końcowy S. Nie dodaję fikcyjnego czwartego fizycznego kubitu: trzy próbki nie oznaczają trzech pamięci *plus* sensor. Rozwinięta dynamika ma rozmiar 8×8, a uśredniony kanał B podczas impulsów ma 64×64 superoperator. Wyniki nie są kolejną aproksymacją samego impulsu. Zbadany odczyt jest dokładnie **tym** lokalnym testem X/Y z R16, a nie arbitralnym wspólnym POVM.

## 0. Źródła i granice first-owner

First owner: PRF11 R35, model static shared Cauchy vs independent Cauchy–Lévy increments, https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md .
R02, nieprzemienność SWAP i źródła podczas impulsu, full micro-contract: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R02_FINITE_DURATION_SWAP_CAUCHY_ACTIVE_PULSES_AND_RESOURCE_GATE_001_20261026.md .
R16, idealnie reset-invariant randomized X/Y source test: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-29/IW_PRF12_R16_RESET_AGNOSTIC_SOURCE_TEST_AND_SEPARATE_LIFETIME_CALIBRATION_001_20261029.md .
R17, exact ideal-memory law and source-active perturbative Cauchy upper bound: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-29/IW_PRF12_R17_SOURCE_ACTIVE_SWAP_STORAGE_AND_AXIS_ROBUSTNESS_001_20261029.md .

Mature external hosts: Lindblad-controlled quantum channels and pure dephasing are standard, cf. https://www.nature.com/articles/s41534-019-0189-0 , https://qopt.readthedocs.io/en/latest/examples/t2_markovian_noise.html ; deterministic Cauchy integration and Duhamel stability are standard numerical and mathematical tools. No novelty or priority claim; no independent referee has reviewed this application.

## 1. Exact source and physical-clock contract

Input |+>_S⊗|+>_M1⊗|+>_M2, all three freshly prepared. Free sensing times Δ1=Δ2=Δ3=Δ=T_free/3. Schedule:
1. free source on S for Δ;
2. active Hamiltonian SWAP S↔M1 for τ;
3. free source on S for Δ;
4. active Hamiltonian SWAP S↔M2 for τ;
5. free source on S for Δ.

**Physical clock is T_phys=T_free+2τ, NOT T_free.** Keep Δ and τ separate. No secret overlap or zero-time SWAP.

A source: ONE hidden ξ~Cauchy(0,γ), fixed across ALL these five stages in one run. Free H_A=ξ Z_S/2; pulse Hamiltonian H_A,j=(π/(2τ)) SWAP_(S,Mj)+ξ Z_S/2. Condition on ξ before integrating its Cauchy density.

B source: symmetric independent Cauchy–Lévy increments. Free sensor density evolves by Dγ(ρ)=γ/2(Z_SρZ_S−ρ). During pulse j its full Lindblad generator is

 L_B,j(ρ)=−i[(π/(2τ))SWAP_(S,Mj),ρ]+γ/2(Z_SρZ_S−ρ).

This is **not** a model that redraws a phase once per driven SWAP. B has a continuous Markovian semigroup acting noncommutatively with the gate.

Storage aging: while completely parked, M1 dephases with off-diagonal rate κ from the END of SWAP1, for age 2Δ+τ; M2 from END SWAP2 for Δ. There is no storage dephasing applied to S during its active periods, and no M1 storage dephasing during SWAP1. M1 dephasing commutes with the subsequent sensor/M2 pulse and all free sensing terms. M2 dephasing commutes with the final sensor free period. Thus applying two independent local dephasing channels at the END with multipliers d1=exp(−κ(2Δ+τ)), d2=exp(−κΔ) is EXACT, not a Trotter approximation. This is one precisely chosen hardware/memory rule, not every physical memory model.

The locally implementable final event is Eε=1/2(E_X+E_Yε), with E_U=P_+(U)⊗3+P_−(U)⊗3, Uε=cos(π/2+ε)X+sin(π/2+ε)Y. A fresh fair common basis coin picks X or Yε in every run; outcomes are compared using classical communication only.

## 2. Exact conditional A and full B operators

Work in units T_free=1, so Δ=1/3, gamma=3q, r=τ/T_free, κT_free=k. Define 8×8 swaps S1,S2 between qubit indices (S,M1),(S,M2), the 8×8 sensor Z_S, and the normalized input vector ψ0=|+>⊗3.

For a fixed ξ:
 U_free(ξ)=exp(−i ξ Δ Z_S/2);
 U_j(ξ,r)=exp(−i[(π/2)S_j+(ξτ/2)Z_S]).

Then the **full**, nonperturbative conditional pre-memory pure output is

 ψ_A(ξ)=U_free U_2 U_free U_1 U_free ψ0,

and with exact parked-memory CPTP map M_(κ,r),

 ρ_A^(active)= ∫ dξ [γ/(π(γ²+ξ²))] M_(κ,r)(|ψ_A(ξ)><ψ_A(ξ)|).

Use ξ=γ tanθ, θ∈(−π/2,π/2), to integrate against dθ/π. No artificial finite-moment truncation.

For B use the 64×64 column/row vectorized Lindbladian exponential in every driven segment:
 ρ_B^(active)=M_(κ,r)∘D_free∘exp(τ L_B,2)∘D_free∘exp(τ L_B,1)∘D_free(ρ0).

No use of a random fixed B-phase during the pulse. In code the 64×64 exponent is computed from the DIMENSIONLESS pulse Liouvillian, using  z=γτ=3qr. A's pulse uses an 8×8 Hermitian eigensystem and is independently checked against scipy.linalg.expm; B's 64×64 expm is checked against an ODE solve_ivp. Commutation of memory dephasing with the second gate is independently checked.

The actual source distinguishability witness is p_A=Tr(Eε ρ_A), p_B=Tr(Eε ρ_B), contrast C=p_A−p_B. It is **not** Helstrom distance and not an unrestricted LOCC optimum.

## 3. Independent numerical full-model results, fixed FREE exposure clock

Use q=1/3, κT_free=.3, ε=.02 rad, so gamma*T_free=1. Both active SWAPs have ratio r=τ/T_free. Gauss–Legendre quadrature on θ with independent orders 144/288/576 is a convergence heuristic, **not a certified tail enclosure**. Numbers in the table are approximate at the displayed 4–6 significant figures.

| r | p_A approx | p_B exact 64×64 evolution | C approx | T_phys/T_free |
|---:|---:|---:|---:|---:|
| 0 | 0.55811155 | 0.40822052 | 0.14989103 | 1 |
| .001 | 0.55794464 | 0.40797964 | 0.14996500 | 1.002 |
| .01 | 0.55648570 | 0.40583023 | 0.15065547 | 1.02 |
| .05 | 0.54985311 | 0.39666856 | 0.15318454 | 1.10 |
| .15 | 0.53412912 | 0.37632906 | 0.15780006 | 1.30 |
| .30 | 0.51307988 | 0.35163576 | 0.16144412 | 1.60 |
| 1.00 | 0.44140677 | 0.29209947 | 0.14930730 | 3.00 |

**Important interpretation:** at fixed FREE exposure, slower gates may raise raw contrast because the TOTAL experiment also becomes longer. Do not describe it as better at fixed physical clock. The stronger result is that full active dynamics has not destroyed THIS measured contrast in the studied schedules. No monotonic claim for all q, κ, phase errors, or pulse lengths.

## 4. Theorem R18.1 — analytic Lipschitz/Cauchy-tail enclosure for averaged A

Let p_A(ξ) be the conditional event probability for fixed ξ including memory channel; 0≤p_A(ξ)≤1. The only ξ-dependent Hamiltonian term is ξ Z_S/2 in ALL free and driven stages. The Duhamel estimate for each stage and telescoping, even though SWAP and Z do not commute, gives

 \[
 |p_A(\xi)-p_A(\xi')| \le T_{\rm phys} |\xi-\xi'|.
 \tag{R18.1}
 \]

This remains valid after the final xi-independent CPTP memory dephasing. (Conservative Lipschitz constant; not claimed sharp.)

Fix truncation X>0, split [−X,X] into bins [a_j,b_j] with midpoint c_j and maximum width h. Integrate each bin's Cauchy probability EXACTLY,

 w_j=(1/π)(arctan(b_j/γ)−arctan(a_j/γ)),   W=Σw_j.

Compute S_mid=Σ_j w_j p_A(c_j) with exact conditional A matrix evolution. The unknown omitted tail probability is 1−W, and p_A in that tail is bounded between 0 and 1. The Lipschitz bound yields the independent analytic enclosure

 \[
 \boxed{
 S_{\rm mid} -\frac{T_{\rm phys} h}{2}\,W
 \le {\mathbb E}_{\rm Cauchy}\,p_A(\xi)
 \le S_{\rm mid}+\frac{T_{\rm phys}h}{2}\,W+1-W.
 } \tag{R18.2}
 \]

This derivation has NO reliance on agreement of two Gaussian quadrature grids. It remains valid for the actual Cauchy heavy tails. One must also bound floating-point evaluation of S_mid and p_B to make it a **fully formal interval-arithmetic certificate**; that has NOT been done. Here numerical margins are about 0.1, vastly exceeding observed matrix agreement errors (≤4×10^−11 for the independent B ODE test).

For X=20γ, bin width h=.02γ (2000 bins), the omitted Cauchy tail is 1−W=0.031804502512... . Direct results:

| τ/T_free | lower p_A from R18.2 | computed p_B | lower contrast C |
|---:|---:|---:|---:|
| .001 | .530605 | .407980 | **.122625** |
| .01 | .529867 | .405830 | **.124036** |
| .05 | .525583 | .396669 | **.128915** |
| .15 | .510636 | .376329 | **.134307** |
| .30 | .486751 | .351636 | **.135115** |
| 1.00 | .402197 | .292099 | **.110098** |

Thus the positive *averaged* contrast is supported by a source-specific explicit enclosure for pulse times far beyond the range where R17's purely perturbative coarse bound resolves the sign. R17 is not overturned; its safe norm bound becomes vacuous, while a direct dynamical computation plus tail-controlled integration answers this particular source and observable.

## 5. Theorem R18.2 — a NEGATIVE countersequence to uniform reset-history invariance

R16's exact ideal-SWAP reset invariance held for EVERY fixed ξ. It is not valid under the above finite source-active pulse Hamiltonian, even when the pulse duration tends to zero in the **nonuniform hidden-phase sense**.

For the same q=1/3, k=.3, ε=.02 set gamma=T_free=1, Δ=1/3. For positive integers N define

 \[
 \xi_N=6\pi N,\quad\tau_N=\frac{4}{6\pi N},\quad
 \xi_N\Delta=2\pi N,\quad \xi_N\tau_N=4,\quad\tau_N\to0.
 \]

Every FREE-stage propagator at ξ_N is ±I, while every driven pulse retains the NONZERO dimensionless detuning ξ_N τ_N=4. Consequently the conditional output tends to the fixed finite two-pulse unitary product

 ψ_* = exp(−i[(π/2)S2+2 Z_S])
       exp(−i[(π/2)S1+2 Z_S]) |+>⊗3.

At the same time, the B Liouvillian pulse noise tends to zero as gamma τ_N→0 and its output tends to the ideal-SWAP B state with memory ages (2Δ,Δ). Direct matrix evaluation gives

 p_A(ξ_N)→0.3777560954170059,
 p_B(τ_N)→0.4082205246558249,
 and C_conditional→−0.0304644292388190.

Sample finite N:
N=10, τ=.021220659, C_cond≈−.0261124;
N=100, τ=.002122066, C_cond≈−.0300211;
N=300, τ=.000707355, C_cond≈−.0303165.

The negative limiting value, with continuity in pulse areas, supplies a constructive source-typed **nonuniformity counterexample**: arbitrarily short nonzero pulses do not guarantee that A has a greater event probability than B for EVERY possible static hidden frequency. Indeed for every sufficiently small positive τ one may round N≈4/(6πτ); the residual pulse-area error tends to zero.

**Crucial caveat:** ξ_N diverges into the Cauchy tails, so these settings have vanishing prior probability as τ→0. This is entirely consistent with positive averaged contrast, the R17 high-probability tail controls, and convergence under Cauchy averaging. It is NOT a counterexample to averaging or a full LOCC impossibility theorem.

## 6. Fix the TOTAL clock before comparing hardware speed

Another resource control sets T_phys=1, gamma=1, kappa=.3; each pulse uses time τ, so T_free=1−2τ, Δ=(1−2τ)/3, q=(1−2τ)/3, k=.3(1−2τ), r=τ/(1−2τ).

| each τ/T_phys | numeric source contrast | conservative lower contrast from R18.2 |
|---:|---:|---:|
| 0 | .149891 | .149891 |
| .01 | .149060 | .122685 |
| .05 | .145817 | .122460 |
| .10 | .141698 | .120159 |
| .20 | .133769 | .112966 |
| .30 | .126057 | .105006 |

The apparent raw contrast advantage of making τ longer at FIXED FREE exposure disappears when total clock is fixed. These are comparisons within one chosen schedule, not optimization over arbitrary controls.

The required swap strength is Ω=π/(2τ). A longer pulse reduces the peak control amplitude but consumes time from the available free sensing budget. Simultaneously changing γ, κ, total T or drive model would be a DIFFERENT experiment.

## 7. Independent verification, failure modes and custody

Standalone extended Python 3 script with NumPy and SciPy reconstructs every 8×8 pulse and the 64×64 Lindblad channel, with no imported previous R17 code:
- full A per-ξ pulse eigenvector propagation versus independent scipy.linalg.expm at five pulse detunings, for both gates: max operator discrepancy <5e−14;
- full B 64×64 expm versus independent solve_ivp ODE propagation: discrepancy <4e−11;
- dephasing on the parked M1 DURING pulse2 versus a final commuting dephasing channel: discrepancy <8e−14;
- vanishing source γ=0 under active pulses gives identical A/B event probability for 3 pulse schedules;
- τ=0 reproduces the ideal R16/R17 joint source readout;
- Gauss–Legendre Cauchy integration for orders 144,288,576, with discrepancies of order 10^−4 (QUADRATURE AGREEMENT IS NOT A RIGOROUS INTEGRAL CERTIFICATE);
- separate Cauchy-tail/Lipschitz 2000-bin bounds for 6 pulse durations;
- analytic hidden-frequency countersequence and fixed total clock comparisons.

Important numerical/physical caveats: no finite-precision interval-arithmetic proof; no real-device readout; ideal free exposures; instantaneous preparation; no readout SPAM errors other than one specified basis-axis offset; dephasing only on fully parked memories; constant square SWAP Hamiltonian pulse; no phase-dependent control feedback; the sensor and TWO memories comprise the entire actively used 3-qubit Hilbert space; no classical process-norm claims; no optimal LOCC claim. The single-copy unrestricted asymptotic LOCC gap left open at R09 remains OPEN.

**NEXT R19:** derive tight and resource-aware confidence for repeated runs under persistent ξ using a uniform conditional model or an experimentally testable phase-randomization control; compare direct pulse unitary shapes, possibly alternative input/readout codes. Do not claim iid Bernoulli across runs under persistent ξ based solely on one-run Cauchy averaging.

RETURN: PRF12_R18 / FULL_THREE_QUBIT_SOURCE_ACTIVE_TWO_SWAPS / A_STATIC_CAUCHY_EXACT_UNITARY / B_LEVY_LINDBLAD_64X64 / EXACT_PARKED_MEMORY_DEPHASING / DIRECT_CONTRAST_POSITIVE / ANALYTIC_LIPSCHITZ_CAUCHY_TAIL_ENCLOSURE / R16_UNIFORM_RESET_INVARIANCE_FALSIFIED_FOR_NONZERO_PULSES / FIXED_PHYSICAL_CLOCK_AUDITED / REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / SINGLE_COPY_LOCC_CLOSURE_OPEN / GITHUB_PENDING_BW_INGEST.


## Subsequent PRF12 R19 source-control alternative (2026-10-29) — DO NOT MERGE RESOURCE CONTRACTS

PRF12 R19 introduces a DIFFERENT control/measurement instrument: one sensor qubit, two equal free exposure intervals and one central finite square X-axis Hahn-echo π pulse with static source A or Lévy source B both active DURING the pulse. This is not a repair by pulse shaping of the original S/M1/M2 **two-SWAP three-probe** architecture; it requires an additional active control resource and changes the output quantum states. Its exact one-run probabilities are p_A^-(xi)=[cos(h/2)sin(xi Δ)+(xi τ/h)sin(h/2)cos(xi Δ)]², h=sqrt(pi²+(xi τ)²), and p_B^-=(1-exp(-gamma T_phys))/2. Cauchy quantile plus an arbitrary-dependence union bound yields BOTH conditional errors <5% for eight runs at gamma*T_phys=1, tau/T_phys=.0008, with rectangular drive Ω*T_phys≈3927. A sequence tau_N=T_phys/N³ yields asymptotically consistent SOURCE discrimination with drive Ω_N*T_phys=πN³, **not** at fixed drive. For each fixed positive τ, arbitrarily far-tail static xi can make p_A^- near 1; NO phase-uniform finite-pulse guarantee. Internal source: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-29/IW_PRF12_R19_FINITE_HAHN_ECHO_RESET_ROBUST_CERTIFIED_SOURCE_DISCRIMINATION_001_20261029.md . External source first owner: E. L. Hahn, 1950. Neither R18 nor R19 proves original unrestricted single-copy LOCC closure gap. Referee pending, NO_CANON, NO_EXEC, BW ingestion pending.
