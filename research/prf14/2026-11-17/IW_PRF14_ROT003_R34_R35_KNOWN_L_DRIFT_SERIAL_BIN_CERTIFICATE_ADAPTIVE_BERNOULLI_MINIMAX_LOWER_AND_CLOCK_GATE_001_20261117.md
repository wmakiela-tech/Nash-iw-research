---
artifact_id: IW_PRF14_ROT003_R34_R35_KNOWN_L_DRIFT_SERIAL_BIN_CERTIFICATE_ADAPTIVE_BERNOULLI_MINIMAX_LOWER_AND_CLOCK_GATE_001_20261117
created_at: 2026-11-17
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
exposure: PUBLIC
document_type: ORIGINAL_SOURCE_TYPED_CONDITIONAL_UPPER_LOWER_MATHEMATICAL_REPORT
status: TWO_MATHEMATICAL_PROOFS / CONDITIONAL_STATISTICAL_SOURCE_PASS / NUMERICAL_SCRIPT_BYTE_IDENTICAL_EXECUTED_PASS / PHYSICAL_SCHEDULING_FAIL_IN_EXAMPLE
priority: PRF12_R33_R34_QUANTUM_CALIBRATION_FIRST / PRF14_ROT002_R35_DATA_ONLY_NO_GO_FIRST / PRF14_ROT003_SOURCE_SPECIFIC_BERNOULLI_KNOWN_L_UPPER_LOWER_FIRST_INTERNAL_ONLY / GENERAL_MATURE_MINIMAX_METHOD
claim_ceiling: NO_FOUNDATIONAL_NOVELTY / NO_UNCONDITIONAL_DRIFT_INFERENCE / NO_HARDWARE / NO_NATIVE_QUANTUM / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE / NO_NEW_NATIVE_B1_RUN
---

# PRF14 ROT003 — R34/R35 known-L drift: honest serial-bin upper certificate and adaptive Bernoulli minimax lower bound, with physical clock failure

## 0. Question and exact inherited firstness

PRF14's previous ROT002 supplied a source-specific constructive nonidentifiability obstruction: observing only finite/earlier calibrations cannot establish an *unknown* future Lipschitz bound, even for C1 detector histories. The inherited R34 certificate is **correctly conditional** on a *separately supplied* exogenous pathwise detector drift rate; its statistical reference CS does not estimate that rate. ROT003 tests the minimal positive *conditional* counterpart: **if** a known pathwise rate L is supplied independently and reference observations are legal, can the whole science-window detector be certified, and what finite sampling cost is unavoidable?

Original direct full readbacks:
- PRF12 R33 original (2026-11-08), Git blob SHA1 \`95b894b89780a0fe3d1ad3a9723d3f62e47d3e22\`:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-08/IW_PRF12_R33_DRIFT_INTERLEAVED_LOCAL_REFERENCES_AND_NONIID_SOURCE_GUARD_001_20261108.md
- PRF12 R34 original (2026-11-10), blob \`f959f57db8059b4bd42866e4784caf214a05c69c\`:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-10/IW_PRF12_R34_VARIANCE_ADAPTIVE_NONSTATIONARY_REFERENCE_ANYTIME_CERTIFICATE_001_20261110.md
- PRF14 ROT002 original, blob \`8dbb117cc9526072ff7aef9d6ca00ff4e496de8b\`:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf14/2026-11-17/IW_PRF14_ROT002_PRF12_R34_R35_FUTURE_DRIFT_SOURCE_IDENTIFIABILITY_NO_GO_RANDOM_INTERLEAVING_LOWER_BOUND_AND_MATURE_HOST_001_20261117.md
- PRF13 ROT003 original paired-readout reference, blob \`c31b9759ffa6614fe70ab19e52ce64f15b619965\` (read in immediately previous PRF14 rotation):
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf13/2026-11-11/IW_PRF13_ROT003_MINIMAL_PAIRED_REFERENCE_AND_FOUR_CORNER_B_GATE_001_20261111.md

Latest dispatch snapshot (2026-11-17 after 00:28 CET): T3 belongs to LT9, official v2.3 current-table comparison/recurrence belongs to REC13/KN15; Mech-S10 native T2R status \`SOURCE_PREFLIGHT_PASS / NATIVE_EXEC_UNKNOWN_AND_HOLD\`; INT10, LT9, SCOPE12 and Mech-S10 independently advance B1 source lift/charge model. No B1 new program authorized in this report. This turn does **not** co-opt their results, does not certify published PBH limits and does not assign their work.

## 1. Frozen R34 scientific contract and separate hypothetical sampling abstraction

Original R34:
- Terminal detector arm \`i=0\` represents the ideal+ input; \`i=1\` represents ideal− input.
- Nominal comparator \`q0 = .99\`, \`q1 = 3705/69000 = 247/4600\`.
- Quantum/source comparison constants **inherited, NOT newly reproduced**: \`A0=0.3106993896688963\`, \`B0=0.27161358975207756\`, signed score sensitivity \`S=.59514\`.
- Target score bounds \`a=.2995, b=.2828\`. R34 Eq. 34.7 numerically gives \`delta*=.009398133420642572\`. It suffices that EVERY science shot in the window has per-arm deviation \`|p_i(t)-q_i|<=delta*\`, and that all other conditional-quantum hazard, pair-readout independence, private axis and nonanticipation conditions of R33/R34 hold.
- In original R34, \`|p_i(t)-p_i(s)|<=nu_i |t-s|\` is an **externally supplied pathwise assumption**, not inferred from data.
- Each legal reference outcome \`X_{i,k}\` is Bernoulli conditional on full relevant past with conditional mean \`p_i(t_{i,k})\`. Reference times and arm choices are predictable; the clock and available preparable reference states are physical constraints.

For the conditional upper theorem below, take any **fixed planned future science interval** \`[0,T]\`, a **known** \`L>0\` satisfying each arm's *pathwise* \`L\`-Lipschitz bound throughout \`[0,T]\`, and a device schedule that can put exactly \`m\` legal references for EACH of the two arms in each of \`J\` consecutive time bins. These controls must be source-independent and satisfy the original conditional-Bernoulli law. This is an abstract time-slot and bandwidth requirement, **not established for the original single detector**. If the schedule cannot fit those references without altering the source model, the upper certificate is not executable, even if the algebra is valid.

## 2. Theorem U — finite serial-bin *uniform* confidence certificate with arbitrary predictable within-bin times

Let \`0<delta<1\`, \`0<alpha<1\`, \`L,T>0\`. Partition \`[0,T]\` into \`J=max{1,ceil(2LT/delta)}\` consecutive equal time bins \`I_j\`, each of length \`h=T/J <=delta/(2L)\` whenever \`J>1\`; if \`J=1\` because \`2LT/delta<=1\`, also \`LT<=delta/2\`, hence \`Lh<=delta/2\`. At each bin \`j\` and reference arm \`i=0,1\`, collect **exactly** \`m\` outcomes \`X_{i,j,k}∈{0,1}\` at predictable times \`tau_{i,j,k}∈I_j\`. Let \`hat p_{i,j}=m^{-1} Σ_k X_{i,j,k}\` and \`bar p_{i,j}=m^{-1} Σ_k p_i(tau_{i,j,k})\`.

Take \`epsilon=delta/4\` and

\`m >= ceil[ log(4J/alpha) / (2 epsilon^2) ] = ceil[ 8 delta^{-2} log(4J/alpha) ]\`.

Conditional Hoeffding/Azuma for bounded Bernoulli martingale differences gives, even under arbitrary non-iid means and adaptive predictable timing,

\`P( exists (i,j): |hat p_{i,j}-bar p_{i,j}| >epsilon ) <= 4J exp(-2m epsilon^2) <=alpha.\`

For any science time \`t∈I_j\`, pathwise Lipschitz and times in SAME bin give

\`|p_i(t)-bar p_{i,j}| <= (L/m) Σ_k |t-tau_{i,j,k}| <= Lh.\`

Consequently the fully DATA-COMPUTABLE decision rule

**CERTIFY** iff \`max_{i,j} |hat p_{i,j}-q_i| + epsilon + Lh <= delta\`; otherwise **ABSTAIN**

has BOTH:
1. Honest soundness for every legal path \`p=(p0,p1)\`: \`P_p(CERTIFY and exists i,t: |p_i(t)-q_i|>delta) <=alpha\`.
2. Uniform stable-world power: if \`p_i(t)=q_i\` for all t, then \`P_p(CERTIFY)>=1-alpha\`.

Proof: on the simultaneous concentration event, the displayed triangle bound certifies all t. In stable world, \`|hat p_{i,j}-q_i|<=epsilon\` simultaneously, and \`2epsilon+Lh <=delta\`, therefore CERTIFY. Done.

**No i.i.d. assumption is used** in this argument, just the fully history-conditional Bernoulli mean and predictable time/arm selection. Conditional source-measurement independence and proper qubit reference preparation remain mandatory when importing the certificate back to R34; this statistical theorem alone certifies neither. No optional stopping *within m*: the schedule must fix m per bin; optional-stopping upgrade requires R34-style e-process/error spending.

Total reference observations in this explicit construction:
\`n_U=2Jm = O( (1+LT/delta) delta^{-2} log[(1+LT/delta)/alpha] )\`.
For \`LT/delta\` large and alpha fixed, this is \`O(LT delta^{-3} log(LT/delta))\`; do NOT drop \`+1\` outside that regime. This conservative fixed-m Hoeffding upper method is NOT R34's variance-adaptive 46,055 fixture.

## 3. Theorem L — lower bound for ALL adaptive reference-only calibration testers in the Lipschitz class

Define the test objective carefully. A reference-only procedure may select times and arms adaptively, use private randomness, and stop at random count N. It must (i) \`CERTIFY\` the fixed stable detector \`p0=q0,p1=q1\` with probability \`>=1-alpha\`, and (ii) \`CERTIFY\` any alternative path that violates \`sup_{t,i}|p_i(t)-q_i|<=delta\` with probability \`<=beta\`, where \`0<alpha,beta<1\` and \`1-alpha>beta\`. If it always abstains, the lower bound does NOT apply.

Freeze original R34 lower reference probability \`q=q1=247/4600\`, with \`0<delta< (1/2-q)/2\`. For \`L,T>0\` define \`ell=4delta/L\`, \`K=floor(T/ell)=floor(LT/(4delta))\`. If \`K=0\` this construction yields no positive lower bound. Otherwise choose \`K\` pairwise disjoint intervals \`I_k\` each of width \`ell\`, within \`[0,T]\`, and define alternatives:
- \`p0^k(t)=q0\` for every k and t,
- \`p1^k(t)=q + 2delta [1-|t-c_k|/(2delta/L)]_+\`, where \`c_k\` is center of \`I_k\`.

Each alternative is admissible \`L\`-Lipschitz, takes values in (0,1/2) for the chosen delta, equals stable \`q\` outside \`I_k\`, and violates the \`delta\` safety constraint at its center by reaching \`q+2delta\`. The reference observations under a deterministic conditional-Bernoulli path are a legal subclass of the R33/R34 abstract experiment.

Let \`P_0\` be the complete adaptively observed data/schedule/stopping law under stable \`q\`; \`P_k\` that under the k-th bumped path. Even adaptive decision kernels for next arm/time add zero conditional KL because the same decision mechanism is used under both worlds. By KL chain rule for sequential observations and data processing for the CERTIFY event \`A\`,

\`D(P_0||P_k) >= kl(P_0(A),P_k(A)) >= kl(1-alpha,beta)\`,

where \`kl(u,v)=u log(u/v)+(1-u)log((1-u)/(1-v))\`, and the last inequality requires \`1-alpha>beta\`.

For \`q<=v<=q+2delta<=1/2\`, Bernoulli relative entropy obeys the mature elementary chi-squared bound

\`D(Bern(q)||Bern(v)) <= (v-q)^2/[v(1-v)] <= 4delta^2/[q(1-q)]\`.

Thus chain rule bounds

\`D(P_0||P_k) <= [4delta^2/(q(1-q))] E_0[N_1(I_k)]\`,

where \`N_1(I_k)\` counts arm-1 observations at times inside \`I_k\`. Rearrangement and summation over K disjoint supports yield the explicit adaptive-sequential lower bound

\`E_0[N] >= K q(1-q) kl(1-alpha,beta)/(4delta^2)\`.

For fixed \`alpha,beta\`, original source q away 0 and 1, and \`LT/delta →∞\`, the bound scales as \`Omega(LT/delta^3)\`. This does NOT claim a tight constant; it does establish the same delta-exponent as Theorem U, up to its logarithm, for this exact controlled Bernoulli worst-case certification task.

**Scope:** This bound applies to reference observations ONLY, without auxiliary continuous device sensors, known dynamics stronger than Lipschitz, external clock-state information, or side-channel science data. Source-A/B quantum outcomes and their feedback are not used. The triangular bumps are Lipschitz (not globally C1); our *declared target class here is Lipschitz*. ROT002's C1 no-go remains a separate theorem and does not need reproof here.

## 4. R34 original-number exercise — decisive clock/resource separation

Take the numeric comparator \`q0=.99\`, \`q1=247/4600\`, \`delta=0.009398133420642572\` (frozen rounded R34 tolerance), and *illustrative hypothetical* \`L=10^{-4}\` per R34 dimensionless clock unit, \`T=10^4\`, \`alpha=beta=.05\`. These L/T values are **not measured hardware parameters** and are not R34's stated \`nu=10^{-8}\` fixture.

Independent stdlib local executable calculates and actually PASS-checks:
- \`J=ceil(2LT/delta)=213\`, \`h=T/J=46.948356807511736\`;
- \`epsilon=delta/4\`;
- \`m=882,498\` observations **per arm and bin**, total \`n_U=375,944,148\` references;
- \`K=floor(LT/(4delta))=26\` disjoint lower-bound bumps; each width \`4delta/L=375.92533682570286\`;
- binary information threshold \`kl(.95,.05)=.9 log(19)=2.6499950812497963\`;
- adaptive expected-reference **lower bound** \`E_0[N]>=9909.350025014457\`; if N is integer with finite expectation, this is an expectation bound, **not** a deterministic guarantee of \`N>=9910\` each run.

The U/L gap is large in constants; saying the *rate* is near-matched up to log factors as \`delta→0\` does NOT mean the numerical method is nearly optimal here.

**Crucial PHYSICAL CLOCK FAIL for this particular upper construction**: original R34 says one reference read consumes \`gamma*t_ref=0.1\`. To collect \`2m\` serial readings inside ONE bin would take \`2m×0.1=176,499.6\` dimensionless time units, whereas a bin has only \`h=46.948...\` units. Thus the upper method is **NOT EXECUTABLE on one such sequential instrument** at these hypothetical parameters. This is not a proof that no superior/variance-adaptive scheme is executable, not a measured detector limitation, and not evidence against R34's different adaptive calibration. It is an explicit throughput falsifier of over-interpreting this otherwise valid mathematical upper bound as an experimental protocol.

A physically honest reopening must prove availability of time slots, no reference/science cross-disturbance, the exact detector conditional-mean law, and exogenous L. Otherwise ABSTAIN; no proposed physical source decision.

## 5. Nearest mature scientific host, original firstness and limits

Direct outside-source lookup this turn:
- T. T. Cai, M. Low, Z. Ma, *Adaptive confidence bands for nonparametric regression functions*, **JASA** 109(507), 1054–1070 (2014), DOI https://doi.org/10.1080/01621459.2013.879260 . The accessible author/publisher full text discusses Lipschitz/Hölder classes and uniform confidence band width scaling \`(log n/n)^{beta/(2beta+1)}\`, giving the familiar \`beta=1\`, rate \`(log n/n)^{1/3}\`. Different model (generally Gaussian regression), same mature mathematical host. Direct web hit: https://pmc.ncbi.nlm.nih.gov/articles/PMC4531001/ .
- P.-Y. Massé and W. Meiniel, *Adaptive confidence bands in the nonparametric fixed design regression model* (2012), original arXiv https://arxiv.org/abs/1207.3975 . Background to known/unknown smoothness and honest sup-norm bands; no claim of exact equivalence to the source R34 binary sequential task.
- Genovese and Wasserman, *Adaptive Confidence Bands* (2007), https://arxiv.org/abs/math/0701513 . Source-specific ROT002 already matched this honest bands/no-uniform-adaptivity theme.
- Ariel Avital, Klim Efremenko, Aryeh Kontorovich, David Tolpin, Bo Waggoner (2026), *Non-parametric binary regression in metric spaces with logarithmic loss*, open publisher HTML https://link.springer.com/article/10.1007/s10472-025-09995-5 . Provides mature contemporary Lipschitz Bernoulli setting but **its objective is logarithmic loss**, different from our pointwise honesty and sequential safe-certification objective. It is neither an exact source claim nor our firstness.
- KL/data processing, conditional Hoeffding, Le Cam/Fano bump alternatives are old standard methods. This report proposes no mathematical novelty beyond the source-specific assembly and its concrete constants/clock gate. The lower bound does not use unreviewed PRF13 source data or outside physical measurements.

**Firstness guards**: PRF12 R33 already derived fixed-n nonstationary conditional Hoeffding and the source drift transfer; R34 already derived predictable time-uniform e-processes; PRF12 R34 F3 already observed unrestricted drift destroys the source contrast; PRF13 ROT003 first studied paired-latch calibration for restricted joint readout; PRF14 ROT002 first explicitly proved our source-specific indistinguishable future/∞-confidence and randomized-hole negative result. ROT003 adds a bounded statistical *known-L quantification* and particular adaptive KL lower bound, no fundamental statistical invention or new quantum conclusion.

## 6. Code and integrity controls

Deterministic Python 3 stdlib checker:
https://github.com/wmakiela-tech/Nash-iw-research/blob/37203994ae88c753847dd426ba4d0be1b415b5aa/research/prf14/2026-11-17/code/prf14_rot003_source_typed_sampling_math.py

Local bytes and archived source verified identical by Git blob SHA comparison:
\`ede520711ae4b58677bdb6e110cb6ef1a87f16b3\` for both original local \`git hash-object\` and direct GitHub readback; local executable bytes = 2,081; SHA-256 = \`32571c1ab499276b4203bfb6db677ce454d72c7c0580ae2ee57ccc747ed727e3\`.

Actual original local execution in isolated runtime: **PASS** (exact fractional q and decimal tolerance, float-precision logarithmic sample budgeting, dense sampled chi-square/KL sanity and time-capacity guard). A single original source-code comment was corrected from "sample covariance" to "KL divergence" via a second Git commit, with exact readback; computational behavior unchanged. This is a mathematical arithmetic smoke test and not a formal proof assistant, rigorous interval verifier for exp/log, or experimental readout. Actual theorems are proved algebraically above.

No native quantum Hamiltonian/Lindblad solver, BlackHawk/Julia, data collection or physical source simulation performed. No claim that R35 had a real pre-experiment derivative bound. GitHub code/report custody is not BW science ingestion, external independent review, CANON or EXEC_SIGN.

## 7. Stop, reopen and deliver

**R35_DATA_ONLY_UNKNOWN_L: STOP** as ROT002.
**R35_KNOWN_L_ABSTRACT_UNIFORM_CERTIFICATE: CONDITIONAL_MATH_PASS** (Theorem U).
**R35_REFERENCE_ONLY_ADAPTIVE_MINIMAX_LOWER: CONDITIONAL_MATH_PASS** (Theorem L).
**R35_SINGLE_DETECTOR_BANDWIDTH_AT_EXAMPLE: FAIL** for this U construction only.
**ORIGINAL_R34_PHYSICAL_CONTRAST: HOLD** until externally sourced physical L, measured detector readout transfer, operational clock, and shotwise joint independence. No auto adoption.

Reopen scientifically if (i) independently grounded physical slew model bounds L and permits reference schedule, OR (ii) owner predeclares an integrated/random-time target and proves fresh source error inequality, OR (iii) a proposed variance-adaptive time-local R34 schedule passes all timing and conditional mean checks. No delegation; Moderators own science priorities and reviewer queues.

REPORT RETURN: \`PRF14_ROT003 / R34_R35_KNOWN_L_SERIAL_BIN_SUP_NORM_CERTIFICATE / ADAPTIVE_BERNOULLI_KL_BUMP_INFORMATION_LOWER / DELTA_MINUS3_RATE_WITH_LOG_GUARD / SERIAL_REFERENCE_THROUGHPUT_FAIL_NUMERIC / PRF12_R33_R34_ORIGINAL_FIRSTNESS_PRESERVED / MATURE_STATISTICS / ACTUALLY_EXECUTED_BYTE_IDENTICAL_ARITHMETIC_CHECKER_PASS / SOURCE_ONLY_NO_NATIVE_QUANTUM / NO_NOVELTY_NO_CANON_NO_EXEC_SIGN_NO_TASK_CASCADE\`.
