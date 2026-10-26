---
artifact_id: IW_PRF12_R04_THREE_PROBE_FINITE_SWAP_EXACT_X_READOUT_GAP_AND_SECTOR_DECOMPOSITION_001_20261026
created_at: 2026-10-26
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R03_N3_TWO_FINITE_SWAPS_PARITY_SUFFICIENCY_STRESS
exposure: PUBLIC
canonical_body_path: research/prf12/2026-10-26/IW_PRF12_R04_THREE_PROBE_FINITE_SWAP_EXACT_X_READOUT_GAP_AND_SECTOR_DECOMPOSITION_001_20261026.md
sync_state: GITHUB_PENDING_BW_INGEST
status: ANALYTIC_FINITE_N_COUNTEREXAMPLE_LOCAL / ACTIVE_PULSE_NUMERICAL_REPRO_PASS / FINITE_TAIL_STRESS_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_DEVICE / NO_GLOBAL_MULTISLOT_OPTIMUM / NO_FIXED_KAPPA_ASYMPTOTIC_RECOVERY / NO_FULL_SUCCESSION_ZIP_READBACK
function: SCIENCE_FIRST / FOUNDATION_FIRST / TWO_SURFACE_PRIOR_ART / NEGATIVE_KNOWLEDGE_PRESERVING / FALSIFIER_FIRST
---

# PRF12 R04 — Trzy próbki, dwa skończone SWAP: dokładny kontrprzykład dla wystarczalności lokalnego pomiaru X i kontrola aktywnych impulsów

**Autor/funkcja:** PRF12. **Data:** 2026-10-26. **Werdykt:** twierdzenie R03.2 (local X parity = Helstrom dla n=2) NIE rozszerza się w sposób automatyczny na n=3. Istnieje dokładny kontrprzykład przy 3 idealnych równych ekspozycjach, nawet dla κ=0. Analogiczna ściśle dodatnia luka występuje w wybranych przykładach z DWOMA czasowo skończonymi SWAP i źródłem aktywnym podczas bramek.

## 0. Source-first, host subtraction, two-surface knowledge

**Wewnętrzne źródła pierwszeństwa / zakres:**
- PRF11 R29–R35, zwłaszcza źródłowo zdefiniowany rozdział static Cauchy ξ vs independent Cauchy–Lévy, stan końcowy SWAP, idealny X-OR i krytyczna pamięć. PRF11 R35: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md .
- PRF12 R01 timing/gate-error bound: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R01_CLOCK_BUDGET_GATE_ERRORS_AND_TWO_TIER_SCHEDULE_001_20261026.md .
- PRF12 R02 finite-duration SWAP with active A and Lindblad B: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R02_FINITE_DURATION_SWAP_CAUCHY_ACTIVE_PULSES_AND_RESOURCE_GATE_001_20261026.md .
- PRF12 R03 exact n=2 support and local X parity: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R03_FINITE_TWO_PROBE_SWAP_CAUCHY_SECTOR_PARITY_HELSTROM_001_20261026.md .

**Mature external prior art**, all source-reviewed by title/abstract, not evidence of priority of R04:
- Zambon, *Process tensor distinguishability measures*, Physical Review A 110, 042210 (10 October 2024), https://doi.org/10.1103/PhysRevA.110.042210. Process tensors/quantum combs have multiple distinguishability notions and admissible data processing conditions. Here R04 computes **only the endpoint Helstrom distance for a fixed control sequence**.
- Zambon and Soares-Pinto, *Relations between Markovian and non-Markovian correlations in multitime quantum processes*, Physical Review A 109, 062401 (3 June 2024), https://doi.org/10.1103/PhysRevA.109.062401.
- Butler et al., *Optimizing Performance of Quantum Operations with Non-Markovian Decoherence: The Tortoise or the Hare?*, Physical Review Letters 132, 060401 (9 Feb 2024), https://doi.org/10.1103/PhysRevLett.132.060401.
- Ortega-Taberner et al., *Unifying methods for optimal control in non-Markovian quantum systems via process tensors*, J. Chem. Phys. 161, 124119 (28 Sep 2024), https://doi.org/10.1063/5.0226031.
- Garbellini et al., *Uniform process tensor approach for the calculation of multi-time correlation functions of non-Markovian open systems*, J. Chem. Phys. 164, 184104 (May 2026), https://doi.org/10.1063/5.0331783.
**Subtraction:** accessible local POVM vs Helstrom, three-bit Fourier statistics, excitation-conserving SWAP, correlated random-unitary dephasing and restriction-induced information loss are mature techniques; R04 only supplies an exact source-typed counterexample and computed 3-probe fixture. NO NOVELTY claim.

## 1. Frozen ideal-SWAP model and the three separate readouts

Each of n=3 probes starts in |+>. Model A has ONE common static ξ~Cauchy(0,γ), model B independent Cauchy–Lévy increments, exactly as in PRF11 R35. Ideal SWAPs swap the active sensor and a fresh memory qubit between exposures \(\Delta_j>0,\sum_{j=1}^3\Delta_j=T\). At time T the three qubits are jointly accessible. With independent post-SWAP memory aging factor \(e^{-\kappa(T-t_j)}\), the endpoint computational-basis density matrices are

 \(\rho_A(x,y)=\tfrac18\exp[-\gamma|\sum_j\Delta_j(x_j-y_j)|]\prod_{j:x_j\ne y_j}\exp[-\kappa(T-t_j)],\)

 \(\rho_B(x,y)=\tfrac18\exp[-\gamma\sum_j\Delta_j|x_j-y_j|]\prod_{j:x_j\ne y_j}\exp[-\kappa(T-t_j)].\)

Do NOT assume fixed κ asymptotic n→∞ recovery: n here is exactly THREE.

We compare four different, increasingly lossy readouts: (i) arbitrary endpoint POVM/Helstrom, \(\mathrm{TV}_{H}=\tfrac12\|\rho_A-\rho_B\|_1\); (ii) all 8 full outcomes of measuring X on EVERY qubit and then using the optimal classical likelihood decision, \(\mathrm{TV}_{X{\rm-full}}=\tfrac12\sum_{s\in\{\pm1\}^3}|p_A(s)-p_B(s)|\); (iii) binary parity from the product of three X outcomes; (iv) binary X-OR, “at least one minus”.

The data-processing hierarchy is \(\mathrm{TV}_{H}\ge\mathrm{TV}_{X{\rm-full}}\ge\max(\mathrm{TV}_{X{\rm-par}},\mathrm{TV}_{X{\rm-OR}})\). There is NO general ordering between parity and OR.

## 2. Theorem R04.1 — exact no-aging counterexample, all q>0

Set κ=0, equal exposures Δ1=Δ2=Δ3=T/3, \(q=\gamma T/3>0\), \(x=e^{-q}\in(0,1)\), \(b=1-x^2>0\), \(a=x\,b=x-x^3\).

Let \(D=\rho_A-\rho_B\). In the computational-basis ordering [000; 3 strings of weight 1; 3 strings of weight 2; 111], D vanishes in rows/columns 000 and 111. Identify each weight-2 string with the bitwise complement of a weight-1 string. Then the only nonzero 6×6 block is:

 \(D|_{N=1,2}=\tfrac18\begin{pmatrix}b(J_3-I_3)&aI_3\\aI_3&b(J_3-I_3)\end{pmatrix}.\)

Explanation: two-bit flips swapping a 1 and a 0 generate the b entries within fixed-weight sectors, and complementary three-bit flips generate the a entries across sectors. Pair 000↔111 has differences all of one sign, so it cancels exactly.

Eigenvalues: \(\tfrac b8(2+x)\), \(\tfrac b8(2-x)\), \(-\tfrac b8(1-x)\) twice, \(-\tfrac b8(1+x)\) twice, and two zeros. Therefore

 \(\boxed{\mathrm{TV}_{H}=b/2=(1-e^{-2q})/2.}\)          (R04.1)

Write local X outcome signs as \(s_i\in\{\pm1\}\). Its signed probability difference is exactly:

 \(p_A(s)-p_B(s)=\frac b{16}(s_1s_2+s_1s_3+s_2s_3)+\frac{3a}{32}s_1s_2s_3.\)    (R04.2)

Summing eight absolute values yields:

 \(\mathrm{TV}_{X{\rm-full}}=\begin{cases}\frac{b(6+9x)}{32},& x\ge2/3,\\[2pt]\frac{3b}{8},&0<x\le2/3.\end{cases}\) (R04.3)

The two binary compressed statistics are:

 \(\mathrm{TV}_{X{\rm-parity}}=3a/8=3xb/8,\quad
 \mathrm{TV}_{X{\rm-OR}}=3(2b+a)/32=3b(2+x)/32.\)    (R04.4)

Most importantly:
 \[
 \boxed{\mathrm{TV}_{H}-\mathrm{TV}_{X{\rm-full}}=
 \begin{cases}b(10-9x)/32,& x\ge2/3,\\ b/8,&0<x\le2/3,\end{cases} >0.}
 \]          (R04.5)

For every q>0 the strict gap is positive. It vanishes only in the trivial zero-signal limit q→0 or scales towards zero as the entire differential signal disappears. Hence not even KEEPING ALL LOCAL X OUTCOMES is sufficient for Helstrom at n=3 in this source model. The n=2 R03 parity sufficiency was a small-sector special case.

At q=1/3 (γT=1) numerical closed-form verification:
| Measurement | Exact evaluated TV |
|---|---:|
| Helstrom | 0.243291440484 |
| full X joint distribution | 0.189292628451 |
| X parity | 0.130744451026 |
| X OR | 0.123920402938 |
| Helstrom − full X | 0.053998812033 |

Direct 8×8 matrix diagonalization and Hadamard-basis probabilities agree with all four closed forms at q=0.05, 1/3, 0.7, 1.4 to <3×10^−16. No fitting.

## 3. Frozen physically timed *synthetic* n=3 active SWAP protocol

Choose physical constants T=1, γ=1, Ω=8, and fixed κ either 0.3 or 5. Two SEQUENTIAL SWAP pulses, \(\tau=\pi/(2\Omega)=\pi/16\approx0.19634954\) each, total active-pulse length \(L=2\tau\approx0.39269908\), free fraction \(F=T-2\tau\approx0.60730092\).

Choose normalized free-exposure weights (d1,d2,d3), Σd=1. Actual free exposures are \(\Delta_j=F\,d_j\). Sequence: free Δ1 / SWAP(S,M1) pulse τ / free Δ2 / SWAP(S,M2) pulse τ / free Δ3. During EVERY interval source acts on S. Post-SWAP M1 is dephased for \(\Delta_2+\tau+\Delta_3\), M2 for \(\Delta_3\), each at fixed rate κ; all three qubits are initially |+>.

A: one static hidden ξ~Cauchy(0,γ) throughout, during pulses \(H_{A,j}=\Omega{\rm SWAP}(S,M_j)+\xi Z_S/2\). B: independent Cauchy–Lévy increments throughout, during pulses Lindblad \(\dot\rho=-i[\Omega{\rm SWAP},\rho]+(\gamma/2)(Z_S\rho Z_S-\rho)\). This is NOT an independent static ξ_B per pulse.

The 8×8 conditional A state vectors can be propagated EXACTLY for each fixed ξ by invariant 1×1 or 2×2 SWAP blocks, and then integrated over ξ. The B channel uses explicit matrix exponential on a 64×64 Liouville generator for each pulse. Later M1 aging commutes with subsequent S–M2 operations and can be applied at the end. This avoids the source-typing error of substituting quasi-static B.

## 4. Independent finite-parameter observations / SOURCE-TYPED numerical controls

Computed locally using Python NumPy/SciPy. Static A integral is truncated symmetrically and integrated by trapezoid; removed Cauchy mass \(m_X=(2/\pi)\arctan(\gamma/X)\) is filled with a positive normalized comparison state. This guarantees from the *tail replacement only*:
 \( \|\rho_A^{true}-\rho_A^{cut+fill}\|_1\le 2 m_X\),
 and each of Helstrom TV and full-X TV has tail-induced error ≤m_X; the **gap** error ≤2m_X. Finite-interval quadrature error is independently probed by step refinement, not interval-certified.

Selected results at cutoff X=30000 and step=.3 (numbers are diagnostic approximations, not exact):

| free (d1,d2,d3) | κ | active Helstrom TV | active full X TV | active X parity | active X OR | Helstrom−X |
|---|---:|---:|---:|---:|---:|---:|
| (1/3,1/3,1/3) | 0.3 | 0.181377 | 0.146888 | 0.104357 | 0.092892 | 0.034488 |
| (0.55,0.30,0.15) | 0.3 | 0.167197 | 0.147218 | 0.117667 | 0.086442 | 0.019979 |
| (1/3,1/3,1/3) | 5 | 0.041395 | 0.037955 | 0.002388 | 0.011695 | 0.003440 |
| (0.55,0.30,0.15) | 5 | 0.046894 | 0.041347 | 0.008435 | 0.015728 | 0.005547 |

At X=30000, \(m_X≈2.1221\times10^{-5}\), so the gap margin 2m_X≈4.2441×10^−5 is smaller than EVERY observed gap (even κ=5). This does not certify trapezoid quadrature error but makes the Cauchy-tail component non-diagnostic for the qualitative sign.

A selected hard refinement for equal weights κ=.3:
| cut X | step Δξ | TV_H | TV_Xfull | difference |
|---:|---:|---:|---:|---:|
| 10000 | .30 | 0.1813917013 | 0.1469048352 | 0.0344868661 |
| 30000 | .30 | 0.1813766611 | 0.1468881625 | 0.0344884986 |
| 30000 | .15 | 0.1813766604 | 0.1468881617 | 0.0344884987 |
| 100000 | .25 | 0.1813713973 | 0.1468823258 | 0.0344890715 |

At X=100000 the Cauchy tail TV bound is 6.3662×10^−6. The evidence is numerically stable to precision shown for **the gap**. Values themselves vary within expected conservative tail budgets. Norms, positivity, Hermiticity, normalized traces and the data-processing inequality were examined as sanity conditions. No hardware measured.

**Mechanism:** Already in the ideal n=3 model \(D\) has a 6×6 nonzero block involving weights 1 and 2; the rank-2 support used in R03 no longer applies. Some off-diagonal elements between weights 1 and 2, such as |001><110|, are nonzero. Under finite source-active SWAPs the pattern is altered but the loss under the prescribed X readout is robust.

**Negative knowledge:** The loss of Helstrom information under local X does NOT imply *all local POVMs* or *adaptive local measurements* must fail. We have not optimized over local measurement bases, LOCC, entangled POVM hardware, or controls. The numerical values for any one finite schedule are NOT global optima, nor a general n=3 process-tensor norm. No independent referee has audited this source-typing argument.

## 5. Reproducible code + review checklist

Committed runnable source: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R04_THREE_PROBE_ACTIVE_SWAP_AND_X_MEASUREMENT_REPRO_001_20261026.py
Requires Python 3, numpy, scipy. It prints all four metrics for the exact no-memory ideal control and for four active finite-pulse configurations. It asserts analytic-vs-matrix agreement at q=1/3 and that computed active gap exceeds twice the Cauchy tail bound; additional local independent code path checked exact formulas at q=.05,1/3,.7,1.4 and refined grids.

**Referee tasks:** (i) independently derive the 6×6 block and confirm all entries and multiplicities; (ii) inspect exact sign regions for x=2/3 when absolute values of X probabilities switch; (iii) compare to independently written 3-qubit A/B solver (e.g. Gauss-Jacobi transformed quadrature) with a quadrature error certificate; (iv) check memory age while second SWAP occurs; (v) test failure of rank-2 support for source-active n=3 and search for possible 3-qubit LOCC readout attaining Helstrom; (vi) distinguish fixed-endpoint measurement from unrestricted process discrimination and preserve first-owner provenance.

Suggested R05: optimize restricted product basis measurements or add a single entangling premeasurement circuit, then test whether the 0.03449 TV gap at κ=.3 can be closed without changing source. Before experimental rhetoric, add control pulses with finite bandwidth and cross-talk.

## 6. RETURN

PRF12_R04 / EXACT_N3_EQUAL_GRID_X_READOUT_GAP_PROOF_LOCAL / N3_IDEAL_DIAGONALIZATION_PASS / TWO_FINITE_SWAPS_CAUCHY_VS_LEVY_NUMERIC_CONTROL_PASS / CUTOFF_STRESS_PASS / NO_LOCAL_LOCC_OPTIMUM_CLAIM / INDEPENDENT_REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / GITHUB_PENDING_BW_INGEST / SUCCESSION_ZIP_UNREAD.
