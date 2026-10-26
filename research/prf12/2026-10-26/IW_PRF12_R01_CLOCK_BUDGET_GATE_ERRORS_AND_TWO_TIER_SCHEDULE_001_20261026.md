---
artifact_id: IW_PRF12_R01_CLOCK_BUDGET_GATE_ERRORS_AND_TWO_TIER_SCHEDULE_001_20261026
created_at: 2026-10-26
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF11_R35_MINIMUM_SWAPPING_INTERVAL_AND_PER_GATE_FAULT_BUDGET
exposure: PUBLIC
canonical_body_path: research/prf12/2026-10-26/IW_PRF12_R01_CLOCK_BUDGET_GATE_ERRORS_AND_TWO_TIER_SCHEDULE_001_20261026.md
sync_state: GITHUB_PENDING_BW_INGEST
status: SOURCE_DERIVED_ANALYTIC_PROOF / POSITIVE_FOURIER_FINITE_NUMERIC_REPRO / DENSE_SMALL_N_CROSSCHECK / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_DEVICE_CLAIM / NO_GLOBAL_OPTIMALITY / NO_FIXED_KAPPA_RECOVERY / NO_FULL_SUCCESSION_PACKET_READBACK
function: SCIENCE_FIRST / FOUNDATION_FIRST / TWO_SURFACE_PRIOR_ART / NEGATIVE_KNOWLEDGE_PRESERVING / SOURCE_TYPED / FALSIFIER_FIRST
---

# PRF12 R01 — Minimum clock budget, imperfect SWAP gates, and a sharper two-tier schedule for PRF11 R35

Date: 26 October 2026. Language of working report: Polish. Research owner: PRF12, acting after moderator activation with *limited rehydration*: the 59 KB PRF11→PRF12 handoff ZIP itself has not been read. This report relies on source-read PRF11 R34/R35 and external literature. Scientific classification: elementary consequence and optimized construction **within the frozen synthetic PRF11 SWAP experiment**, not new physics or a hardware prescription.

## 0. SOURCE MAP / host subtraction / currentness

INTERNAL PRIMARY OWNER:
- PRF11 R35 (2026-10-25), original proof of source states, the two-tier schedule, sufficient conditions E_n→0, A_n→0, and ideal-memory endpoint discrimination limit; own positive Fourier formula and finite quantum tests. https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md ; exact GitHub blob read for this rotation: 3d8dda56a401c5fce1d1ab9f0f280c4127a6caf0.
- PRF11 R34 (2026-10-25), age-dependent equal-grid memory threshold, marked Poisson limit and non-sufficiency of unlabeled count: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R34_AGED_MEMORY_SHARP_VISIBILITY_POINT_PROCESS_AND_LABEL_SUFFICIENCY_001_20261025.md ; read blob 531ef738cb98ec5438a3c1f2ba555456d968b4c4.
- PRF11 R29–R33 remain first-owner host for correlated Cauchy vs Lévy increments, one-slot bound and uniform SWAP sequence, not PRF12 claims. The existing R35 report contains source links.

EXTERNAL MATURE HOSTS (relevant but not identical experiments):
- Pirandola et al., "Fundamental limits to quantum channel discrimination", npj Quantum Information (2019), CPTP/diamond-norm peeling bound for adaptive channel protocols: https://www.nature.com/articles/s41534-019-0162-y
- "Practical Introduction to Benchmarking and Characterization of Quantum Computers", PRX Quantum 6, 030202 (2025), diamond-norm subadditivity and its conservative nature for circuit errors: https://doi.org/10.1103/PRXQuantum.6.030202
- Uhrig and Lidar, "Rigorous bounds for optimal dynamical decoupling", Phys. Rev. A 82, 012301 (2010); finite minimum spacing matters, but theirs is a different pulse-control problem: https://doi.org/10.1103/PhysRevA.82.012301
- Uhrig and Pasini, "Efficient coherent control by sequences of pulses of finite duration", New J. Phys. 12, 045001 (2010); finite-duration pulse modeling: https://doi.org/10.1088/1367-2630/12/4/045001
- Lancaster et al., "Quantum sensing in the presence of pulse errors and qubit leakage", Phys. Rev. Research 8, 043034, published 13 October 2026, shows that sensing and coherence can respond differently to pulse faults: https://doi.org/10.1103/lb3n-qply

PRIOR-ART SUBTRACTION: nonuniform clock scheduling, diamond-norm telescoping, optimized pulse timing, and error-budget arguments have mature precedents. No publication priority or new general theorem is asserted. R01 supplies a specific exact algebraic gate and an independently calculated finite example **for the existing R35 source-typed model**.

## 1. Frozen contract: do not silently change R35

Fix a=γT>0, β≥0, n qubit probes, a strict partition d_j=(t_j−t_{j−1})/T>0, Σ d_j=1, ideal instantaneous SWAP at n−1 boundaries, the same shared Cauchy draw under A and independent Cauchy increments under B. Age u_j=(T−t_j)/T and r_j=exp(−β u_j/n). Critically, this is κ_n T=β/n, **not fixed physical κ**. Define

 E_n=Σ d_j²,    A_n=(1/n)Σ u_j,
 z_n=a sqrt(E_n),
 ε(z)=(z/π)log(1+4/z²)+(4/π)atan(z/2),
 P_n=∏_j (1+exp(−a d_j))/2.

PRF11 R35 established for the frozen perfect-gate two-output distance D_n=||ρ_A−ρ_B||_1:

 2(1−P_n)−ε(z_n)−2β A_n ≤ D_n ≤ 2(1−P_n)+ε(z_n).     (1)

If E_n→0 and A_n→0 then D_n→2(1−exp(−a/2)); the local X-basis OR witness K≥1 asymptotically achieves total variation TV→1−exp(−a/2). These are **fixed-SWAP-program endpoint statements**; no universal process norm or optimum across other controls is claimed.

## 2. Theorem R01.1 — minimum dwell/clock gate for R35 sufficient conditions

Impose an abstract minimum normalized exposure interval d_j≥1/B_n, where B_n≥n is a dimensionless **maximum allowed scheduling cadence**. Actual maximum switching frequency for these instantaneous switching points is B_n/T. This is a control-timing constraint, **not yet** a finite-duration Hamiltonian model of SWAP.

Then:

(a) Every feasible partition has A_n≥(n−1)/(2 B_n). Consequently, existence of partitions with E_n→0 AND A_n→0 requires B_n/n→∞.

(b) Conversely, if B_n/n→∞, there exist such partitions respecting d_j≥1/B_n: take m_n=ceil(sqrt(n)) for n sufficiently large, set late intervals d_j=1/B_n for all j>m_n and distribute the remaining fraction equally among the first m_n intervals. Let δ_n=(n−m_n)/B_n. Then d_early=(1−δ_n)/m_n≥1/B_n because B_n≥n, and

 E_n=(1−δ_n)²/m_n + (n−m_n)/B_n²→0,
 A_n=(m_n−1)/(2n)+δ_n/2→0.

Thus **B_n/n→∞ is necessary and sufficient for the existence of a grid meeting the particular R35 sufficient conditions** under this abstract minimum-interval constraint.

Proof (a): u_j=Σ_{i=j+1}^n d_i. Interchanging summations gives n A_n=Σ_{i=2}^n (i−1)d_i≥(1/B_n)Σ_{i=2}^n (i−1)=n(n−1)/(2B_n). If B_n/n fails to diverge, it has a subsequence bounded above, along which A_n is bounded away from zero. Proof (b) is the explicit construction and the exact E_n,A_n formulas above; δ_n→0, m_n→∞, m_n/n→0.

CRUCIAL QUANTIFIER: failure of A_n→0 is NOT a full quantum no-go for the R35 discrimination target; it only prevents the age-erasure proof route (1). This does NOT contradict R34's equal-grid results.

## 3. Theorem R01.2 — a less demanding, better asymptotic two-tier clock

For n≥16 choose

 m_n=ceil(n^(2/3)),     B_n=ceil(n^(4/3)),
 δ_n=(n−m_n)/B_n,
 d_early=(1−δ_n)/m_n, d_late=1/B_n.

There are m_n early intervals and n−m_n late intervals. Since B_n≥n, d_early≥1/B_n and d_late=1/B_n. EXACT finite-n quantities:

 E_n=(1−δ_n)²/m_n + (n−m_n)/B_n²,
 A_n=(m_n−1)/(2n)+δ_n/2.

Thus E_n=Θ(n^(−2/3)), A_n=Θ(n^(−1/3)), and z_n=Θ(n^(−1/3)). Equation (1) and the explicit Cauchy tail bound imply a conservative full-quantum trace-distance approach rate O(n^(−1/3) log n)+O(β n^(−1/3)), at fixed a,β. The maximum clock B_n/T is Θ(n^(4/3)/T), compared with the source R35 two-tier example Θ(n^(3/2)/T) and its weaker conservative O(n^(−1/4) log n)+O(β n^(−1/2)) bound.

This is a change to R35's **choice of time partition**; NOT a refutation of R35. This analytical rate is for the bound, not an exact numerical convergence exponent or globally optimal clock design. The log term comes from the Cauchy truncated-absolute-moment estimate, not a proven sharp lower rate.

For a generic B_n=ceil(n^(1+q)) with q>0, the same construction with m_n=ceil(n^(2/3)) yields the bound O(n^(−1/3) log n)+O(β[n^(−1/3)+n^(−q)]). This gives a clock-dependent sufficient error budget without asserting optimality beyond this construction.

## 4. Theorem R01.3 — diamond fault budget for imperfect instantaneous SWAP

Model the real gate at each of the n−1 prescribed boundaries by a CPTP map G_{n,j}, replacing ideal SWAP unitary channel U_{n,j}, with ε_{n,j}=||G_{n,j}−U_{n,j}||_diamond. Assume the same external source trajectories and storage stages as R35, with each faulty gate acting at the **same ideal boundary time**; the map G_{n,j} must be well defined independently of inaccessible source/history, or its uniform conditional diamond guarantee must apply. Let g_n=Σ_{j=1}^{n−1} ε_{n,j}. By telescoping/peeling and trace norm contraction, for H=A,B:

 ||rho_H^fault−rho_H^ideal||_1≤g_n,

hence |D_n^fault−D_n|≤2g_n, and

 2(1−P_n)−ε(z_n)−2β A_n−2g_n
 ≤D_n^fault≤
 2(1−P_n)+ε(z_n)+2g_n.                                  (2)

For the **fixed local X OR statistic**, the probability of any one outcome changes by at most g_n/2 under either hypothesis; therefore the signed A-vs-B event contrast changes by at most g_n. If g_n→0 along with E_n→0,A_n→0, the same ideal limit is recovered under these modeled faulty gates, even for the final optimized POVM.

Uniform per-gate error bound ε_{n,j}≤η_n implies g_n≤(n−1)η_n. Therefore η_n=o(1/n) is a sufficient robust scaling, NOT a necessary physical gate-noise threshold. Diamond-norm estimates can be pessimistic; systematic coherent, correlated, or gate-state-dependent errors demand an explicitly validated model.

HARD MODEL BOUNDARY: no pulse duration, exposure during gates, leakage outside the qubit model, coupling of gate control to ξ, jitter, shared faults, pulse energy, or fixed-rate hardware is modeled. No statement of experimental feasibility.

## 5. Positive finite Fourier checks (NOT independent referee)

Numerical fixture: a=1, β=2. For BOTH schedules below use the SAME n, a, β, total T, n−1 ideal SWAPs and individual final X readouts with OR decision. "R35 source" has m=ceil(sqrt(n)), δ=n^(−1/2). "R01" has m=ceil(n^(2/3)), B=ceil(n^(4/3)), δ=(n−m)/B.

The maximum normalized cadence below is 1/min_j d_j (i.e. multiply by 1/T for frequency). Values were independently calculated here with NONNEGATIVE coefficient convolution of (r_j e^(−iθ)+2+r_j e^(iθ))/4 within the two exposure groups. P_A(K=0)=Σ_{k,l} C_early(k)C_late(l) exp(−a|k d_early+l d_late|); P_B(K=0)=∏_j(1+r_j exp(−a d_j))/2. Reported TV is P_A(K=0)−P_B(K=0)>0. Double precision, not interval arithmetic.

| n | source clock T f_max | R01 clock T f_max | source A_n | R01 A_n | source X-OR TV | R01 X-OR TV | R01 gain |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 64 | 448 | 256 | 0.117188 | 0.210938 | 0.206736631 | 0.228812218 | 0.022075587 |
| 256 | 3840 | 1626 | 0.060547 | 0.144238 | 0.254086812 | 0.276422895 | 0.022336083 |
| 1024 | 31744 | 10322 | 0.030762 | 0.093978 | 0.292569076 | 0.312951233 | 0.020382157 |
| 4096 | 258048 | 65536 | 0.015503 | 0.060425 | 0.321584623 | 0.339664551 | 0.018079928 |

The source R35 columns independently reproduce its printed a=1,β=2 witness table to shown precision. Crucially, R01 achieves **higher computed TV in these four selected tests despite a lower maximum cadence**, but it has HIGHER mean sample age A_n; no componentwise dominance or all-n advantage is claimed. No optimization over all grids; no real-device clock trial.

Independent second formulation check: full (x,y) bitword summation of P_A(K=0)=4^(−n)Σ_{x,y} exp[−a|Σ_j d_j(x_j−y_j)|]∏_{j:x_j≠y_j}r_j for n=4,6,8 matched positive Fourier convolution for BOTH grids within 4×10^(−16). This second test is an algebraically separate small-n exact finite formula in floating arithmetic, not an independent researcher review.

At n=4096, even the ideal R01 local X OR witness advantage against R35 source's PERFECT-gate local X witness is ~0.018079928 TV. From (2), under the single aggregate worst-case guarantee g_n<0.018079928 the faulty R01 X-OR witness remains strictly above the old perfect-gate X-OR figure, PROVIDED all other frozen assumptions hold. Uniform diamond η_n <0.018079928/4095≈4.4151×10^(−6) suffices; this is an illustrative conservative bound, **not** a calibrated gate requirement or an achievable hardware specification.

## 6. Falsifiers, stop conditions, negative knowledge

F1. Enforce B_n≤C n for constant C: theorem R01.1 shows A_n cannot vanish. But do NOT conclude that every endpoint quantum discriminator fails.
F2. Put a fixed nonzero minimal gate/pulse duration τ>0 inside a fixed total T: n−1 such sequential nonoverlapping gates cannot grow unbounded; R01 limit is then inapplicable.
F3. Fixed physical κ>0 does not obey κ_n T=β/n. R34 and R35/R01 cannot be conflated under this change.
F4. Gate errors measured only in average fidelity do not automatically provide the same η_n diamond guarantee; dimension, coherent accumulation and correlations matter.
F5. Non-Markovian control-dependent source/gate coupling is NOT modeled by adding per-gate CPTP faults to the frozen R35 trajectories.
F6. Selected finite n TV comparisons do NOT imply dominance for all n nor prove an optimal clock design.
F7. No universal quantum tester norm, no physical sensor, no LT monograph mutation, no NCDG J3/K admission, no BW sync certification, no EXEC_SIGN.

## 7. Practical continuation / referee checklist

Referee should verify: (i) minimum interval A_n lower bound under the exact normalization; (ii) timing-feasibility of the two-tier construction including n small; (iii) explicit formulas for E_n and A_n; (iv) the diamond peeling quantifiers when source history is common or hidden; (v) signed OR probability error bound g_n; (vi) positivity and normalization factors in the exact characteristic-function convolution; (vii) numerical table by an independent code path; (viii) distinction between abstract clock floor and finite-duration SWAP.

Suggested next branch: model a *specific* finite-duration SWAP Hamiltonian or leakage channel with source acting during gates and a fixed energy/slew-rate budget. Do not pretend its output is covered by R01.3.

## 8. RETURN STATUS

MATHEMATICAL_DERIVATION_LOCAL / TWO_SURFACE_PRIOR_ART_SCOUT_COMPLETE_WITH_LIMITS / SELECTED_FINITE_NUMERIC_POSITIVE / DENSE_N4_N6_N8_CROSSCHECK / INDEPENDENT_REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / GITHUB_PENDING_BW_INGEST / HANDOFF_PACKAGE_UNREAD.
