---
artifact_id: IW_PRF14_ROT024_TWO_ROW_SO3_ORTHOGONALITY_SOURCE_TRANSPORT_FOUR_CHARACTER_95PC_TV_LOWER_AND_PHYSICAL_NO_GO_001_20261122
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
class: TWO_TIME_CLASSICAL_PAULI_MEMORY / FOUR_MIXED_CHARACTERS / TWO_ROW_SO3_ORTHOGONALITY / BELL_BREAK_TESTER_TRANSPORT / FINITE_95PC_SOURCE_TV_LOWER / EXACT_GATE_SOURCE_ALIAS
status: ROT023_ORIGINAL_EXECUTABLE_REOPENED / OWNER_EXACT_SYMPY_AND_DIRECT_16_KRAUS_BELL_BORN_INDEPENDENT_PASS / THIRD_EXACT_INTEGER_RATIONAL_95PC_POWER_REFEREE_PASS / 800_PHYSICAL_MODEL_ONLY_EXPERIMENTS_PASS / LOCAL_ZIP_TEN_ENTRIES_CRC_SHA256_PASS / DIFFERENT_CELL_REVIEW_PENDING
firstness: PRF13_ROT011_SIX_FOURIER_SOURCE / PRF14_ROT021_FULL_TERMINAL_CHANNEL_TV / PRF14_ROT022_BELL_BREAK_SOURCE_PROVENANCE / PRF14_ROT023_SO3_ONE_ROW_TEST / PRF14_ROT024_NEW_TWO_ROW_TESTER_FALSIFIER_INTERNAL / INT10_ROT020_SHARP_9_OVER_8_FOURIER_INVERSE_UNTOUCHED
ceiling: NO_GENERAL_QUANTUM_PROCESS_TENSOR / NO_NONINVASIVE_BELL_PROBE / NO_UNCONDITIONAL_SOURCE_TRANSPORT_INVARIANCE / NO_HARDWARE / NO_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# PRF14 ROT024 — Two-row SO(3) orthogonality detects a source change that passes all six single-row and single-column tests

## Original scientific source, scope and question

ROT023 proved that, in one physical classical Pauli-memory source context, the known source Fourier correlations from a destructive two-time Bell instrument and terminal ±1 Pauli means in an uninterrupted experiment must be compatible with a physical UNKNOWN middle SO(3) gate if the source is invariant across these two instruments. Its one-row necessary norm feasibility permits many changes that a FULL SO(3) matrix cannot accommodate.

ROT024 tests whether cross-row orthogonality supplies new genuinely independent discriminatory information rather than collecting extra measurements without new constraints.

The ORIGINAL ROT023 executed owner source and machine JSON were reopened in /mnt/data/prf14_rot023; pinned primary report:
https://github.com/wmakiela-tech/Nash-iw-research/blob/8bbd8efa383dd300b789b06b266559dfa5c77c72/research/prf14/2026-11-22/IW_PRF14_ROT023_SINGLE_CONTEXT_SO3_ROW_ELLIPSOID_CAUSAL_BREAK_TRANSPORT_TV_LOWER_95PC_COMMON_MODE_FALSIFIER_AND_EXACT_GAUGE_NO_GO_001_20261122.md

Main finding: FOUR selected UNIT Pauli terminal means plus FOUR corresponding Bell-source Fourier characters from ONE joint sixteen-label breaker sample yield an SO(3) cross-row orthogonality obstruction, even if all SIX existing row/column two-coordinate norm tests pass. In a strictly positive original SIX-only Fourier classical source, a uniform 4% source Fourier amplification generates this obstruction, with actual source TV=171/40000=.004275. A second scaled but still strictly positive six-only source gives a valid source-specific analytic 95%-level and ≥95%-power test with 38,842,306 binary/Bell protocol runs, including a strictly positive gate-free lower confidence on source TV. This is a coverage improvement, emphatically NOT an efficiency advantage over ROT023 for different, much larger source perturbations.

General SO(3) orthogonality, causal breaks, Bell labels, Pauli noise and TV concentration are mathematically and experimentally mature. No external novelty or unrestricted process tensor priority claimed.

## 1. Legal physical causal model

For each PREANNOUNCED experiment e=UNIT or BREAK, classical joint Pauli errors v,w∈F2² are drawn with normalized sixteen-label probability p_e(v,w)≥0, stable across Pauli input preparation and terminal readout within e and IID across shots. UNIT applies U_v, the SAME unknown proper SU2 middle gate with Bloch S∈SO(3), and U_w. Its full unital qubit channel is the legal 16-unitary mixture:
 T_UNIT = sum_(v,w) p_UNIT(v,w) D(w) S D(v).
Write C_UNIT,ij=E[chi_j(v)chi_i(w)] for input axis j and output i, then ALL nine transfer coefficients satisfy
 a_ij=T_UNIT,ij=C_UNIT,ij S_ij.
This product identity holds for any sixteen-way classical joint Pauli source and does not require the earlier source to have ten zero Fourier coefficients.

The BREAK experiment instead inserts TWO temporally resolved Bell pair measurements with destructive intermediate reset around the two error intervals. The joint Bell syndrome pair (v,w) samples p_BREAK for THAT diagnostic tester. It is NOT noninvasive, and an experiment-dependent source may differ from p_UNIT without retrocausality because the whole protocol is announced before errors occur. These conditional devices are not claimed to constitute a single globally intervention-independent quantum process tensor. Bell readout error and preparation/measurement errors need explicit physical limits.

Define source transport estimand zeta=TV(p_UNIT,p_BREAK). Every mixed Pauli character is ±1, hence classical total-variation duality gives:
 |C_UNIT,ij-C_BREAK,ij|≤2 zeta.
The Bell data estimate c_ij=C_BREAK,ij and UNIT data estimate a_ij. The UNKNOWN S is constrained to SO(3); no independent numerical estimate of it is needed to establish the null test or TV lower confidence.

## 2. NEW four-character two-row SO(3) obstruction

Choose four offdiagonal input-output pairs J={(0,1),(0,2),(1,0),(1,2)}, with 0=X, 1=Y, 2=Z. Under exact source equality and c_ij≠0, x_ij=a_ij/c_ij must equal the corresponding entries S_ij of ONE proper rotation S.

Unknown diagonal completion entries d0=S_00,d1=S_11 obey:
 d0²=1−x_01²−x_02²,
 d1²=1−x_10²−x_12².
The TWO unknown rows must additionally satisfy dot(row0,row1)=0:
 d0 x_10+x_01 d1+x_02 x_12=0.

Irrespective of both unknown diagonal SIGNS, the necessary cross-row triangle inequality is
 |x_02 x_12| ≤ |x_10| sqrt(1−x_01²−x_02²) + |x_01| sqrt(1−x_10²−x_12²),
provided both radicands nonnegative. This strictly strengthens testing two individual row lengths alone. It is NECESSARY, not a sufficient characterization of a valid full SO(3) completion or all source probabilities.

An exact independent polynomial elimination provides a second falsifier. Put
 A=x_10²(1−x_01²−x_02²),
 B=x_01²(1−x_10²−x_12²),
 W=x_02 x_12.
Every compatible completion necessarily satisfies
 (W²−A−B)²−4AB=0.
Squaring may add spurious formal solutions, so polynomial zeros are NOT automatically physically valid.

## 3. Strictly positive exact source witnesses: ALL six elementary norm tests PASS

Use the original proper rotation
 R0=(1/7)[[-3,-2,6],[6,-3,2],[2,6,3]]
and the existing cyclic proper Clifford
 P=[[0,0,1],[1,0,0],[0,1,0]],
so S0=P R0=(1/7)[[2,6,3],[-3,-2,6],[6,-3,2]].
Original six-offdiagonal hidden Fourier matrix, output rows/input columns:
 C0=[[0,9/100,11/100],[7/100,0,1/10],[8/100,12/100,0]];
all SIX single-label marginal Fourier and THREE diagonal mixed Fourier coordinates are precisely ZERO in both compared source laws; ten ordinary coordinates zero includes normalization-excluded one-time/mixed diagonal class as in original source.

MILD exact example p_BREAK=p_(C0), p_UNIT=p_((26/25)C0). Both are strictly positive physical 16-error-history Pauli laws, their total source variation
 TV=171/40000=.004275.
Under the INCORRECT no-instrument-source-effect null, all six apparent offdiagonal SO(3) elements would be
 x_ij=(26/25)(S0)_ij.
Each of THREE row and THREE column sums of squares of their two offdiagonal entries is EXACTLY
 6084/6125<1.
Every single-entry bound |x_ij|≤1 also PASSES. Hence old ROT023 row/column norm tests are EXACTLY BLIND.

But for the first two rows:
 |x02*x12|=12168/30625,
 |x10|sqrt(d0²)+|x01|sqrt(d1²)=234 sqrt(205)/30625,
 and their difference is EXACTLY
 (12168−234 sqrt(205))/30625≈.287922608038966>0.
No SO(3) completion exists. Another independent direct implementation enumerated ALL FOUR allowed sign pairs for d0,d1 and none satisfies zero dot product.

When a symbolic positive uniform scaling k is applied to this S0, the polynomial from §2 reduces to
 729*k^4*(k^2−1)*(81*k^2−49)/117649=0.
At k=26/25 its EXACT value is
 409983535198224/17951812744140625>0.
For positive k with individually feasible two-entry row norms k²45/49≤1, the simpler cross-row necessary inequality reduces to k²≤1. Thus arbitrarily weak uniform positive amplification k>1 is ALGEBRAICALLY DETECTABLE at ideal infinite precision, for k up to 7/sqrt45 while old row/col tests all pass. It is not uniformly detectable at finite n without signal/noise qualifications.

SEPARATE finite-sample-calibratable physical example retains relative k=26/25 and identical geometric SO(3) contradiction but uses strictly positive stronger source Fourier magnitudes:
 C_BREAK=(7/2)C0 and C_UNIT=(91/25)C0=(26/25)C_BREAK.
All other ten Fourier coordinates remain exactly ZERO; all 16 probabilities physical and normalized:
 min p_BREAK=11/3200=.0034375,
 min p_UNIT=43/40000=.001075,
 true TV=1197/80000=.0149625.
Do not confuse this separate actual TV with the earlier mild .004275 example. The six apparent SO(3) offdiagonal ratios remain x=kS0, all six row/column norm tests still pass and cross-row violation remains .2879226.

## 4. Uniform source-TV LOWER confidence for arbitrary legal 16-way classical Pauli source

The numerical gate S is NOT assumed known for the lower confidence.

For the FOUR UNIT Pauli ±1 means ahat_e and FOUR Bell source characters chat_e extracted from ONE joint sixteen-label Bell trial stream, suppose a common confidence event yields simultaneous bounds
 |ahat_e−a_true,e|≤e_u,
 |chat_e−c_BREAK,e|≤e_c.
On the event, for actual zeta=TV(p_UNIT,p_BREAK) and unknown S∈SO3:
 |ahat_e−chat_e S_e|≤ e_u+(e_c+2zeta)|S_e|.
Define candidate z≥0 lower and upper compatible magnitudes:
 l_e(z)=[|ahat_e|−e_u]_+/(|chat_e|+e_c+2z),
 u_e(z)=min(1,(|ahat_e|+e_u)/(|chat_e|−e_c−2z)) if denominator positive, otherwise 1.
Use conservative zero-denominator conventions: if numerator zero, l=0; if positive numerator and denominator zero, infeasible.

If z=zeta_true, all physical |S_e| lie in intervals [l_e(z),u_e(z)]. Necessary norm and cross-row feasibility therefore imply:
 l01²+l02²≤1,
 l10²+l12²≤1,
 l02*l12 ≤ u10 sqrt(1−l01²−l02²)+u01 sqrt(1−l10²−l12²).
The l values decrease with z and u values increase; the relaxed feasible region is monotone. Define empirical source-TV LOWER CI zeta_L as smallest z∈[0,1] satisfying these constraints (or 0 if feasible at 0). Then, on the joint confidence event:
 zeta_L≤actual TV(p_UNIT,p_BREAK).
This holds for ANY lawful 16-way classical Pauli p_UNIT,p_BREAK, not just the original six-coordinate source. It gives an unknown-gate-independent ONE-SIDED source-TV lower confidence, NOT an upper confidence or proof of source invariance when zeta_L=0.

In the IDEAL exact-data scaled source example, the scalar feasibility root gives
 zeta_ideal_lower≈.005627169793709 <true TV .0149625.
An independent integer/rational square-root referee certifies the strict safe exact-data statement zeta_ideal_lower>.0056.

## 5. Explicit nonasymptotic 95% test and sample/power costs

Use FOUR distinct UNIT Pauli preparation+readout settings e∈J, with n_u independent ±1 terminal shots EACH. Also use ONE BREAK Bell two-time 16-category source sample of n_b independent full label-pair trials, TWO Bell basis readouts per trial. Compute all four source ±1 characters from the SAME breaker label sample; they may be correlated and DO NOT require four separate breaker sources. Source conditional stability within context and legal physical two-outcome POVMs are assumed.

Calibration assumptions (NOT measured by this research):
- Each UNIT Pauli input Bloch direction error≤.00005,
- UNIT final binary POVM effect-axis error≤.00005 and bias≤.00005, with |bias|+||axis||≤1,
- hence per UNIT terminal mean systematic g=.00015 using CPTP channel norm≤1.
- The full BREAK Bell 16-label outcome law differs from the latent source p_BREAK by TV≤beta=.001. This implies each mixed ±1 Fourier character systematic bias≤2 beta=.002.
- IID trials and fixed unknown physical S within all four UNIT settings.

Allocate α_UNIT=.025 and α_BREAK=.025. Choose statistical per-mean deviations eta_u=.0013, eta_b=.001. Four-unit and four-break-character simultaneous union-Hoeffding tails:
 8 exp(−n_u eta_u²/2)+8 exp(−n_b eta_b²/2).
With
 n_u=ceil[2log(8/.025)/(.0013)²]=6,826,416 per UNIT setting,
 n_b=ceil[2log(8/.025)/(.001)²]=11,536,642 two-Bell-label BREAKER trials,
 total **N=4n_u+n_b=38,842,306 distinct protocol runs**,
 including 27,305,664 UNIT terminal binary measurements and 23,073,284 Bell-basis readings embedded in breaker trials.
The joint failure probability bound is .0499999868<.05. Set e_u=.0013+.00015=.00145 and e_c=.001+2(.001)=.003. Then §4 zeta_L satisfies uniform ≥95% COVERAGE, and the source transport null p_UNIT=p_BREAK has false positive probability≤.05.

SOURCE-SPECIFIC ALTERNATIVE POWER: for the strictly positive strong source pair C_UNIT=(91/25)C0 vs C_BREAK=(7/2)C0, assume ADDITIONALLY that the actual unknown physical middle S is within spectral/operator norm δ_gate=.001 of the reference P R0. This gate-neighborhood premise is needed ONLY to guarantee POWER for this explicit alternative, NOT for null validity or the general TV lower CI. The gate induces per-coefficient reference perturbation ≤|C_UNIT,e|δ_gate. Worst-case all 95% sample/calibration errors and this gate perturbation yield a strictly positive two-row violation margin at z=0 of about .00944935 and even at z=.00026 of over **.00005095**. A THIRD separate pure rational/integer-square-root program proves that the latter strictly positive sign does NOT rely on floating-point rounding: it encloses each square root from above by an exact rational bound and confirms a lower margin >.00005. Therefore on the entire ≥95%-joint confidence event,
 **zeta_L>.00026>0**.
The specified physical source drift is detected with probability≥.95; the test has level≤.05. This is a very large conservative sufficient budget, NOT an optimum, device shot measurement or general improvement over ROT023.

Notably, using the mild original C0 source with k=1.04 under beta=.001, the same crude independent interval propagation cannot guarantee this source-specific detection at any n without better readout calibration or stronger source signal. This is a limitation of this chosen conservative certificate, not a proof of general experimental impossibility.

## 6. Original physical validation, simulations and irreducible negative case

ACTUALLY executed main original source, twice with BYTE-IDENTICAL stdout:
 /mnt/data/prf14_rot024/prf14_rot024_two_row_SO3_source_transport.py
 SHA256 3380b05ab89492438086587787f42f68fc9c074eddc48c81a9e74c88c7264e6e.
Generated exact full machine original JSON:
 /mnt/data/prf14_rot024/prf14_rot024_original_machine_certificate.json
 SHA256 1cd5976a464235a8fa523f56dad751da4730651fdfa9d5b090105fdafef3b3f5.
Main script uses exact SymPy source, proper SO3 random gates, legal Bloch state/POVM errors, full sixteen-label Bell readout confusion and actual binomial/multinomial count simulation.

Independently authored SAME-CELL literal sixteen-Pauli-history Kraus and complex Bell Born control, with ZERO import from main:
 /mnt/data/prf14_rot024/prf14_rot024_independent_four_row_bell_born_kraus.py
 SHA256 263a2e2f31335654c39c2c2dba1a3cb09ab65d7fd9ca44aa0e5104d3c04b6816.
It verifies ALL sixteen source histories, ten ordinary Fourier zeros, physically proper SO3 gates, exact full source/channel transfer and all four failed diagonal-sign SO3 completions.

THIRD independent exact rational/integer-square-root test of ideal zeta>.0056 and worst-box calibrated 95% alternative zeta>.00026:
 /mnt/data/prf14_rot024/prf14_rot024_exact_integer_interval_power_referee.py
 SHA256 7fa9ff2b4d7e3c8f6056773aecea56f348fb2f06de1a70a52e28f643e0e8d795.
This source uses only rational fractions and guaranteed upper square-root intervals to prove the strict power margin, no optimizer and no import of other local functions.

Physical MODEL-ONLY synthetic count experiments:
- 400 complete NULL tests with random arbitrary physical SO3 target and truly unchanged source: 0 false source-transport declarations;
- 400 specified SOURCE-change tests with target within δ_gate=.001 reference: 400 positive detections;
- minimum observed alternate TV lower ≈.002727 (descriptive only).
All 800 are synthetic NumPy experiments, **ZERO real quantum hardware trials**; proof of coverage/power is analytical, not from empirical simulation frequency.

**Exact fundamental NO-GO:** W0 has p_UNIT=p_BREAK=p_(7/2 C0), original proper unknown R0, hence source transport ζ=0. W1 has the SAME Bell BREAK source p_(7/2 C0), but different proper R'=U_X(t=1/1000)R0 and UNIT six-only Fourier coefficients
 C'_ij=(7/2) C0,ij [(P R0)_ij]/[(P R')_ij] for i≠j, ten others zero.
All 16 source probabilities remain strictly positive. FULL UNIT channels for TWO different matched proper post-target Clifford controls P R and D_X P R are EXACTLY the same between W0 and W1: **18/18 Bloch transfer entries**, and all Bell-break source labels are also EXACTLY identical. Yet:
 ζ_W0=0,
 ζ_W1=41979/50199950≈.000836235893>0.
Thus even fully passing four-coordinate tests AND complete two-unit-channel tomography plus complete Bell-label source readout CANNOT prove zero tester source backaction; the unknown-gate/source physical alias remains. These are separately conditional source models, NOT asserted to be one single fixed quantum comb across arbitrary interventions.

## 7. Provenance, referee tasks and next science

All THREE scripts compile, exact owner runs and repetition checked, physical source probabilities all positive. Local reproducibility ZIP:
 /mnt/data/prf14_rot024/prf14_rot024_reproducibility_bundle.zip,
 SHA256 87ea806712dd10ef95bbef1db496d99ea2e02821a6fe473267793af5f2642471.
TEN files include original three Python sources, original machine JSON, main stdout and repeated identical stdout, independent physical stdout, rational interval stdout, README and per-file SHA256 manifest. ZIP CRC PASS, all ten entries complete byte-for-byte readback and SHA256 PASS. Same-cell independence is not equivalent to independent different-cell audit.

External near-host background consulted (original publisher abstracts/excerpts, NOT full articles):
- Taranto et al., A Guide to Higher-Order Quantum Operations, PRX Quantum 7 042001 (13 Nov 2026), https://doi.org/10.1103/92c4-g7qs.
- Non-Markovian Quantum Process Tomography, PRX Quantum 3 020344 (2022), https://doi.org/10.1103/PRXQuantum.3.020344.
- Quantum Stochastic Processes and Quantum non-Markovian Phenomena, PRX Quantum 2 030201 (2021), https://doi.org/10.1103/PRXQuantum.2.030201.
- Microscopic parametrizations for gate set tomography under coloured noise, npj Quantum Information (2025), https://www.nature.com/articles/s41534-025-00976-4.
These mature sources prevent generic Bell/gate/process/statistical novelty overclaim.

Request bounded different-cell REC13/AUD3 independent falsification:
1. Reconstruct both physical source pairs and exact 16 label probabilities; verify distinction TV .004275 vs .0149625; no hidden change of ten Fourier zeros.
2. Derive cross-row triangle inequality and quartic elimination; inspect all four unknown diagonal sign assignments; verify all six individual row/column norm constraints pass while strict cross-row failure occurs.
3. Derive four-character source-TV lower CI from |ΔC|≤2TV, including zero-denominator, monotonicity and correlated Bell characters from SAME breaker runs.
4. Check 95% alpha split: four UNIT and four breaker Fourier character means, nu=6,826,416 each x4, nb=11,536,642 x1, SPAM eu=.00145, Bell e_c=.003 and correct counting of TWO Bell readings per breaker run.
5. Independently establish strict positive worst-case power at ζ=.00026 with physical target norm tolerance .001, using exact rational sqrt upper bounds or interval arithmetic.
6. Challenge the no-go by direct full 18-entry physical Kraus and sixteen-label Bell replay, strict positivity of all altered sources and correct exact TV 41979/50199950.
7. Distinguish math detection power from device practicality and check mature prior art before any promotion.

RETURN: PRF14_ROT024 / ORIGINAL_ROT023_SOURCE_REOPENED / TWO_ROW_SO3_4_CHARACTER_STRICT_CROSS_ORTHOGONALITY / ALL_SIX_ROW_COLUMN_NORMS_PASS / QUARTIC_IDENTITY_EXACT_NONZERO / POSITIVE_FOURIER_MILD_TV0P004275 / SCALED_POSITIVE_POWER_TV0P0149625 / GATE_FREE_TV_LOWER_CI / IDEAL_TV_LOWER_GT0P0056 / ANALYTIC_95PC_38842306_RUNS / RATIONAL_POWER_TV_LOWER_GT0P00026 / 800_SYNTHETIC_MODEL_EXPERIMENTS / EXACT_18_CHANNEL_PLUS_ALL_BELL_LABEL_SOURCE_GAUGE_NO_GO_0P000836 / THREE_INDEPENDENT_SAME_CELL_EXECUTABLES / TEN_FILE_ZIP_CRC_SHA_PASS / NO_HARDWARE / NO_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN.
