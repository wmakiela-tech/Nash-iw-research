---
artifact_id: IW_PRF14_ROT023_SINGLE_CONTEXT_SO3_ROW_ELLIPSOID_CAUSAL_BREAK_TRANSPORT_TV_LOWER_95PC_COMMON_MODE_FALSIFIER_AND_EXACT_GAUGE_NO_GO_001_20261122
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
science_class: TWO_TIME_CLASSICAL_PAULI_MEMORY / ONE_CONTEXT_UNKNOWN_SO3_ROW_FEASIBILITY / TWO_BELL_FOURIER_SOURCE_READOUT / DIRECT_INSTRUMENT_TRANSPORT_TV_LOWER_CONFIDENCE / COMMON_MODE_CAUSAL_BREAK_SOURCE_SHIFT / EXACT_SIX_FOURIER_PHYSICAL_UNKNOWN_GATE_NO_GO
status: ORIGINAL_ROT022_EXECUTED_SOURCE_REOPENED / AUTHOR_SYMPY_EXACT_PASS / INDEPENDENT_SAME_AUTHOR_DIRECT_16_PAULI_KRAUS_AND_4x4_BELL_BORN_PASS / ANALYTIC_95PC_LEVEL_POWER_PASS / 800_PHYSICAL_SO3_BLOCH_POVM_BELL_MULTINOMIAL_MODEL_TRIALS_PASS / SOURCE_REPEAT_BYTE_IDENTICAL / ZIP_7_ENTRIES_SHA256_CRC_FULL_BYTE_READBACK_PASS / DIFFERENT_CELL_REFEREE_PENDING
firstness: PRF13_ROT011_ORIGINAL_SIX_FOURIER_SOURCE / PRF14_ROT021_PAIRED_FULL_CLIFFORD_TV_SOURCE / PRF14_ROT022_TWO_BELL_FULL_SOURCE_CONTEXT_AND_UNITARY_VS_BREAKER_TWO_CONTEXT_TRIANGLE / PRF14_ROT023_NEW_SINGLE_CONTEXT_SO3_ROW_FEASIBILITY_AND_SOURCE_TV_LOWER_FOR_COMMON_MODE_INSTRUMENT_SHIFT_INTERNAL_ONLY / INT10_ROT020_SHARP_SIX_FOURIER_9_OVER_8_DIFFERENT_CELL_FIRST
claim_ceiling: NO_UNRESTRICTED_QUANTUM_PROCESS_TENSOR / NO_NOISE_GENERATOR_INVARIANCE_PROVEN_BY_NULL / NO_NONINVASIVE_BELL_MONITOR / NO_GATE_REFERENCE_FREE_SOURCE_TOMOGRAPHY / NO_REAL_QUANTUM_HARDWARE / NO_NEW_SO3_OR_TV_MATHEMATICAL_NOVELTY / NO_EXTERNAL_PRIORITY / NO_CANON / NO_EXEC_SIGN
---

# PRF14 ROT023 — A single-context rotation-row feasibility test directly falsifies instrument transport, including common-mode source changes invisible to previous two-context triangle comparisons

## Abstract and owner result

ROT021 exposed six source marginal Fourier directions unseen by any full terminal single-qubit channel. ROT022 proved exact recovery of every joint classical Pauli-error label probability p(v,w) from two temporally resolved Bell measurements placed around the two noise intervals, but only for the **measurement-and-repreparation breaker tester itself**. ROT022 then derived a hybrid TWO-CONTEXT transport falsifier: a LOWER TV comparison of two UNITARY-context sources minus an UPPER TV comparison of two BREAKER-context sources. That triangle is BLIND when the breaker instrument changes both contexts' sources in the SAME way, because both pairwise source distances can still equal zero.

ROT023 solves that specific blind case with a new, simpler, independently calibratable quantity. In ONE chosen control context, obtain TWO mixed Pauli Fourier source coefficients from jointly sampled Bell-break labels, and TWO corresponding terminal channel means from two uninterrupted Pauli preparations under ONE physical unknown target unitary. The physical SO3 row norm provides a **gate-independent, source-agnostic necessary inequality** for no instrument-induced source change. Its violation certifies a strictly positive unit-vs-break source total-variation distance, without comparing two unitary contexts and without knowing the numerical middle gate.

For the original physical six-offdiagonal Fourier Pauli source C0, a breaker with p_break=C0 and an uninterrupted experiment with p_unit=1.6*C0 (in Fourier coordinates) have each 16 strictly positive classical histories, preserve all ten ordinary Fourier source zeros, and have actual TV=513/8000=.064125. Their two output-X means from input Y/Z give squared normalized row length **576/245>1** if the breaker source is incorrectly assigned to the uninterrupted process. The exact data alone require source transport TV at least **.02498275485093171**, by a monotone one-dimensional feasibility inequality, with no knowledge of the actual physical SO3 gate. This detects a COMMON-MODE source change invisible to ROT022's old two-context pairwise TV-triangle witness.

With source-uniform Bell readout error beta≤.001, genuine Bloch preparation/POVM systematic bounds each≤.00005, two independent Pauli terminal settings with **101,504 shots EACH** and one breaker context with **125,313 joint two-Bell-readout trials**, the total is **328,321 full experimental protocol runs** and 250,626 individual Bell-basis readouts. The empirical row-feasibility root yields a ≥95%-COVERAGE LOWER confidence bound on the actual unit-versus-break source TV, even for ARBITRARY normalized 16-way classical Pauli sources. Under the specified source scale change and a separate source-specific power condition that the actual gate differs in operator norm by ≤.001 from the reference SO3, the 95% event guarantees a strictly positive numerical source-TV lower bound at least **.0005378777178775**. Thus a calibrated test achieves false-alarm probability≤5% for truly invariant source and detection probability≥95% for that exact noninvariant source.

Limit: the test remains a ONE-SIDED falsifier. A different unknown target rotation and adjusted positive six-offdiagonal source laws can give all original UNIT channels and all BREAK Bell data EXACTLY equal to a truly invariant model, even when actual source transport TV is **5997/25099975≈.00023892454>0**. No passing row test establishes general instrument independence; the exact physical gauge in ROT021/022 persists.

General Bell label tomography, source-conditioned measurement, SO3 row geometry, TV duality, and Hoeffding inequalities are mature external mathematical tools. This specific conditional Pauli-source application is only an INTERNAL construction, not a cleared external novelty claim.

## 1. Controlling original source and contemporary near-host prior art

Actually reopened the exact original executed ROT022 code rather than relying on summaries:
 /mnt/data/prf14_rot022/prf14_rot022_hybrid_tester_transport_95pc.py
 /mnt/data/prf14_rot022/prf14_rot022_two_bell_source_tomography_transport.py
and original public report immutable commit 1ea6242404f2e5d65298fd2199b3a12fbc689421:
https://github.com/wmakiela-tech/Nash-iw-research/blob/1ea6242404f2e5d65298fd2199b3a12fbc689421/research/prf14/2026-11-22/IW_PRF14_ROT022_TWO_BELL_TEMPORAL_PAULI_SOURCE_16_LABEL_FULL_RECOVERY_CAUSAL_BREAK_TRANSPORT_NO_GO_AND_HYBRID_95PC_TEST_001_20261122.md

PRF13 ROT011 retains the original six-hidden-correlated-Fourier source firstness. PRF14 ROT022 owns the two-Bell original full source sampling and two-context transport triangle. PRF14 ROT023 owns only the newly constructed single-context SO3 feasibility application to common-mode tester shifts and its finite-sample certificate. INT10's different-cell sharp 9/8 inverse six Fourier-to-TV norm is distinct and first owned by INT10 ROT020.

Current (22 November 2026) original journal / publisher abstract/excerpts actually searched:
- Taranto, Milz, Murao, Quintino, Modi, *A Guide to Higher-Order Quantum Operations*, PRX Quantum 7, 042001, 13 Nov 2026, https://doi.org/10.1103/92c4-g7qs — mature causal break, multi-time instruments and higher-order source operational distinctions; only relevant publisher snippets reviewed, NOT the full manuscript.
- *Non-Markovian Quantum Process Tomography*, PRX Quantum 3 020344 (2022), https://doi.org/10.1103/PRXQuantum.3.020344 — measurement/repreparation instruments mature.
- *Self-consistent noise characterization of quantum devices*, Phys Rev B 106, 155413 (2022), https://doi.org/10.1103/PhysRevB.106.155413 — self-consistent classical noise fitting across quantum operations mature; only search/publisher abstract checked, full paper NOT reviewed.
- Rudinger et al., *Probing Context-Dependent Errors in Quantum Processors*, PRX 9 021045 (2019), https://doi.org/10.1103/PhysRevX.9.021045 — mature context error hypothesis testing.

No source-level external firstness clearance or generic process tensor novelty claimed.

## 2. Physical model: exactly ONE fixed control context, TWO distinct protocols

Choose a physical proper SO3 middle target S (possibly unknown, far from any numerical nominal reference) for the uninterrupted UNIT protocol. The physical single-qubit channel is a convex mixture of 16 Pauli unitary histories:
 T_UNIT = Σ_(v,w) p_UNIT(v,w) D(w) S D(v),
 where v,w∈F2² and p_UNIT(v,w) is ANY legal 16-way classical joint law, independent of terminal Pauli preparation/readout within this same selected context. D(v), D(w) are proper Pauli sign-conjugation rotations. Define C_UNIT,ij=E_pUNIT[chi_j(v)chi_i(w)] for EVERY input j/output i including diagonal. Exactly:
 T_UNIT,ij=C_UNIT,ij S_ij.
This identity holds for ALL classical Pauli joint 16-source probabilities; it does NOT require other ten Fourier moments zero.

A different preannounced instrument BREAK uses temporally resolved Bell measurements and destructive resets to read both classical error labels. Provided the fixed joint pair (v,w) is sampled for THAT diagnostic protocol and two Bell devices have sufficiently calibrated label readout, its raw joint sixteen-category law is p_BREAK(v,w), NOT necessarily p_UNIT(v,w). Choose one output Pauli row i and a subset J of input Pauli axes; the breaker source character is c_j=C_BREAK,ij and the uninterrupted terminal mean for +j preparation/output i is a_j=T_UNIT,ij.

No single intervention-independent comb is implied by allowing p_UNIT!=p_BREAK: the entire protocol is announced before the first noise event, so each conditional experiment remains an ordinary causal CPTP mixture. These worlds are NOT claimed to satisfy every cross-tester constraint of a single fixed quantum multi-time process tensor. The Bell breaker is disruptive and the original coherent quantum trajectory is not preserved.

## 3. NEW deterministic theorem: SO3-row feasibility implies a SOURCE-TV LOWER bound

Set zeta=TV(p_UNIT,p_BREAK). Each mixed Pauli character chi_j(v)chi_i(w) takes values in {+1,−1}; elementary TV duality implies
 **|C_UNIT,ij−C_BREAK,ij|≤2zeta** for EVERY i,j, without restrictions on other fifteen source parameters.
Consequently for any j,
 |a_j|=|C_UNIT,ij S_ij|≤(|c_j|+2zeta)|S_ij|.
For any fixed output row i of physical S∈SO3, Σ_(j in J)|S_ij|²≤1. Hence:
 **F(zeta):=Σ_(j in J) [|a_j|/(|c_j|+2zeta)]²≤1.**
Treat the 0/0 case as zero if the numerator is also zero; a positive numerator with zero denominator is inconsistent with zeta=0.

The scalar function F(z) is monotonically nonincreasing for z≥0. If F(0)>1, the UNKNOWN source transport TV MUST exceed zero even though the gate is UNKNOWN. The unique positive root of F(z)=1 (or zero if F(0)≤1) is a gate-independent valid lower bound on zeta. This is an SO3 GEOMETRIC necessary condition only, not a sufficient characterization of the possible Pauli sources nor a claim of sharp global minimax source reconstruction.

An elementary closed-form but generally weaker corollary when min_(j∈J)|c_j|=m>0 is
 **zeta≥(m/2)[sqrt(F(0))−1]_+**
because the source uncertainty denominators obey |c_j|+2zeta≤|c_j|(1+2zeta/m), giving F(zeta)≥F(0)/(1+2zeta/m)². The root may be stronger. Neither expression requires numerical SO3 calibration for its VALIDITY.

The same argument works for any row i, any nonempty subset J of the three Pauli axes, and ANY sixteen-way legal classical source. This theorem is the core advance: a single-context unitary-vs-break source contrast, rather than ROT022's difference of TWO intercontext TV contrasts.

## 4. Exact original six-Fourier physical witness: a common-mode source perturbation invisible to ROT022's triangle

Original physical target:
 R0=[[-3,−2,6],[6,−3,2],[2,6,3]]/7,
 P=[[0,0,1],[1,0,0],[0,1,0]], so S0=P R0 with row X=(2/7,6/7,3/7).
Physical breaker correlated Fourier source, six independent offdiag C coefficients in matrix convention output row i,input col j:
 C0=[[0,9/100,11/100],[7/100,0,1/10],[8/100,12/100,0]].
All other TEN marginal and diagonal mixed Fourier source coefficients precisely ZERO. The 16-history inverse Walsh probability law is p_C(v,w)=[1+Σ_(i!=j) C_ij chi_j(v)chi_i(w)]/16, has 16 strictly positive entries and min p_C=73/1600.

Set BREAK source p_BREAK=p_C. Set UNIT source to Fourier C_UNIT=(8/5)C0 in the SAME physical source family: all other ten Fourier zeros unchanged. The 16 UNIT history probabilities remain strictly positive min71/2000=.0355; both normalized. Exact source-TV:
 **zeta_true=TV(p_(8/5)C,p_C)=513/8000=.064125.**

Measure input j=Y,Z and output i=X in the UNIT protocol:
 breaker c_Y=9/100, c_Z=11/100;
 UNIT ideal a_Y=(8/5)(9/100)(6/7)=**108/875**;
 UNIT ideal a_Z=(8/5)(11/100)(3/7)=**66/875**.
The supposed source-invariant row norm squared is
 F(0)=(a_Y/c_Y)²+(a_Z/c_Z)²
 = (8/5)²[(6/7)²+(3/7)²]
 = **576/245 ≈2.351020408>1**.
Thus the source-invariance hypothesis is falsified independently of numerical gate knowledge.

Exact numerically solved deterministic ROOT F(zeta*)=1 gives zeta*≈**.02498275485093171**, a VALID source-TV lower bound versus true .064125. The simple explicit closed-form corollary gives .02399866901999351. These are not asserted sharp globally over all classical source distributions; they are true lower witnesses.

The COMMON-MODE aspect:
Take TWO matched post-target physical Clifford UNIT contexts A=P R0 and B=D_X P R0 (D_X=diag(1,−1,−1)). Use the SAME UNIT source (8/5)C0 in BOTH, and SAME BREAK source C0 in BOTH. After known Pauli X-frame sign correction, all complete pair UNIT channel transfer entries coincide, so TV(p_UNIT,A,p_UNIT,B)=0. The two breaker Bell source laws also coincide exactly, TV(p_BREAK,A,p_BREAK,B)=0. Therefore ROT022's earlier pairwise triangle difference L_UNIT−U_BREAK is zero in the exact ideal limit even though zeta_A=zeta_B=.064125. New SINGLE-CONTEXT row test detects either individual shift, demonstrating genuinely new complementary coverage. Full terminal channels differ in magnitude between unit and break worlds, but the old **pairwise difference statistic** discarded that common-mode information.

## 5. NEW nonasymptotic 95% lower source-TV confidence from TWO Pauli means and ONE breaker Bell dataset

Within one context, prepare +Y and +Z separately under UNIT source p_UNIT; measure output X. Take n_u independent ±1 terminal readouts EACH, empirical \hat a_Y,\hat a_Z. Separately run the Bell-breaker protocol n_b times, obtaining one joint 16-label pair (v,w) per run, with TWO physical Bell basis readouts per run. From that SAME breaker sample compute both ±1 sample characters \hat c_Y=average chi_Y(v)chi_X(w) and \hat c_Z=average chi_Z(v)chi_X(w).

Assume physically calibrated source-uniform TV error of the BREAK Bell readout law to the actual BREAK label law ≤beta=.001. By ±1-character dual TV, this causes systematic |E(\hat c_j)−c_j|≤2beta, WITHOUT presuming the tester transports source unchanged.

Assume each true physical UNIT input preparation Bloch direction is within εprep=.00005 of its ideal Pauli eigenaxis, each binary POVM Bloch effect axis is within εmeas=.00005, and outcome bias ≤εbias=.00005. For every physical Pauli-mixture channel with transfer norm≤1, each UNIT mean's systematic ideal deviation is bounded by g=εprep+εmeas+εbias=.00015. A numerical calibration of UNKNOWN middle S is NOT required for the CI/null. IID runs within each configuration and stable source law across +Y/+Z preparations are crucial.

Preallocate failure αu=.025 for both UNIT means and αb=.025 for both Bell-character means. Hoeffding union:
 P(any two UNIT statistical errors>ηu)≤4exp(−nuηu²/2),
 P(any two Bell character statistical errors>ηb)≤4exp(−nbηb²/2).
The breaker character sample means are computed from SAME label runs; they need NOT be mutually independent, because the union bound only uses independence across runs. Select:
 ηu=.0100, ηb=.0090;
 nu=ceil[2ln(4/.025)/(.01)²]=**101,504** per UNIT Pauli setting;
 nb=ceil[2ln(4/.025)/(.009)²]=**125,313** breaker two-Bell-label joint runs.
Total distinct physical protocol runs **2nu+nb=328,321**, including 203,008 UNIT binary terminal readouts plus 125,313 breaker trials with TWO Bell readouts each (250,626 Bell basis readouts). Joint failure upper ≈.0499992782703519<.05.

On this ONE ≥95% event every ideal unit mean has |error|≤e_u=ηu+g=.01015 and every breaker source character |error|≤e_c=ηb+2beta=.011. Form DATA-DERIVED nonnegative numbers:
 N_j=[|\hat a_j|−e_u]_+,
 D_j=|\hat c_j|+e_c.
For any true zeta=TV(p_UNIT,p_BREAK), the deterministic SO3 theorem implies
 **Fhat(zeta)=Σ_(j=Y,Z) [N_j/(D_j+2zeta)]² ≤1** on the confidence event.
Define output \hat zeta_low=0 if Fhat(0)≤1; otherwise the unique nonnegative root Fhat(z)=1 (clipped to [0,1] for numerical robustness). Then
 **Pr[\hat zeta_low≤TV(p_UNIT,p_BREAK)]≥.95**,
 UNIFORMLY over arbitrary lawful sixteen-way classical Pauli sources, arbitrary unknown physical SO3 S, and any calibrated error effects inside those caps.

Reject the source-transport equality H0:p_UNIT=p_BREAK if Fhat(0)>1. Type I error≤.05, with NO assumption of numeric R calibration. This is an actual quantified lower-confidence estimand, not merely a zero/nonzero moment test.

Under the specified SIX-only source alternative p_UNIT=p_(8/5)C and p_BREAK=p_C, for source-SPECIFIC POWER additionally externally bound the actual physical UNIT rotation by ||S−P R0||op≤.001 (NOT required for general CI coverage). Then |a_Y|≥(8/5)(.09)(6/7−.001) and |a_Z|≥(8/5)(.11)(3/7−.001). On the same concentration event:
 Fhat(0)≥Σ_j [(|a_j|−2e_u)_+/(|c_j|+2e_c)]²
 ≥**1.0188014500925586>1**.
Moreover the same worst-case denominator comparison gives a strictly positive source-TV confidence lower value at least **.0005378777178775**. Therefore the test has ≥95% power against this specified physically positive shift under the stated calibration neighborhood, while retaining ≤5% Type-I probability for any true source invariant situation under the weaker setup assumptions.

This N is a sufficient resource upper, not a minimax lower or measured device shot count. It is lower than ROT022's 872,386 for the particular DIFFERENT transport-shift task, but comparing raw N does NOT show universal statistical dominance because ROT022 tested a different pairwise effect.

## 6. Independent physical execution and exact anti-self-sealing no-go

Main original source ACTUALLY EXECUTED TWICE byte-identically:
 /mnt/data/prf14_rot023/prf14_rot023_single_context_row_ellipse_transport.py,
 SHA256 3e1837a770c1597378e5cfcbd7b29e21867cb53feb3f5cba89acceed6754d229.
Native original machine JSON:
 /mnt/data/prf14_rot023/prf14_rot023_original_machine_certificate.json,
 SHA256 c94cf0e6b1c9693707166f90d4314e4fd335941d4189ee2d0c2335ae7363b7ae.
Both exact symbolic source positivity and ten zero ordinary Fourier moments and independent physical transfer checks executed. A simulation with genuinely physical randomized SO3 gates, Bloch prep vectors, biased legitimate binary POVM effects and FULL 16-category Bell readout-confusion distributions at 328,321 trials per model experiment:
- 400 NULL cases p_UNIT=p_BREAK, with arbitrary proper SO3 unit middle gate drawn over wide orientations: ZERO false source-transport positive declarations;
- 400 source-transport-alternative cases p_UNIT=1.6C, p_BREAK=C and actual S within .001 opnorm of frozen P R0: 400/400 detections.
- Minimum realized alternative positive confidence lower ≈.008020632, minimum empirical Fhat(0)≈1.323629. These finite simulation observations are only model sanity; theoretical guarantees above are distribution-free bounds under explicit assumptions.
- TOTAL 800 complete synthetic model experiments; NONE are quantum hardware samples.

An independently authored SECOND same-owner physical checker (does not import main):
 /mnt/data/prf14_rot023/prf14_rot023_independent_direct_bell_kraus_and_undetectable_alias.py,
 SHA256 f3d805681cc45df3c879cd76a29ffab55c02aeed99472904d68ed43544b06d04.
It directly builds 4×4 complex Bell Born projectors and verifies all four Pauli-error labels exactly, reconstructs all 16 histories for both positive source laws and two distinct UNIT Clifford contexts, and directly performs 16-term Pauli-history transfer summations. It reobtains exact 513/8000 TV, exact 576/245 row-squared contradiction, and the original model's ten ordinary source Fourier zeros. Same-author algorithmic independence is NOT external different-cell audit.

**Exact NO-GO despite ALL FULL observables:** World W0 uses p_UNIT=p_BREAK=p_C, unknown physical target R0. World W1 uses the SAME breaker p_BREAK=p_C, but unknown target R'=U_X(t=1/1000)R0 and alternative six-only UNIT source with offdiag Fourier
 C'_ij=C_ij [(P R0)_ij]/[(P R')_ij], i!=j,
 all ten other Fourier coordinates zero. Both sources are strictly positive and normalized. The original pair W0 has ζ=0; W1 has
 **ζ=TV(p'_UNIT,p_BREAK)=5997/25099975≈.000238924540761495>0**.
Yet W0 and W1 have EXACTLY THE SAME FULL 3×3 CPTP transfer matrices for BOTH matched Clifford UNIT contexts P R and D_X P R (2×9=18 exact physical channel entries), because known D_X left row signs cancel from the ratio. Both worlds also have EXACTLY the same BREAK source p_C and hence the SAME complete Bell label distributions. Therefore no amount of measurement of THESE channels and breaker labels can determine whether source transport is exactly zero. In both worlds the row-feasibility consistency test passes. This sharply separates ONE-SIDED FALSIFIABILITY from unwarranted full source-intervention invariance certification even within the original PRF13 six-only source family.

Both Python scripts pass compilation. Main full output and original machine JSON reproduce byte-identically on cold rerun; local archive:
 /mnt/data/prf14_rot023/prf14_rot023_reproducibility_bundle.zip
 SHA256 f25aa603d963e6f953c4770268c6dd8a9cc8adcdaf9881b03af70933b9248488.
Contains two original ACTUALLY EXECUTED PY, original JSON, first and second identical stdout, second independent stdout, SHA256 manifest (7 entries). ZIP CRC, full entry bytes and per-file hashes checked PASS. These numerical/physical checks do not constitute independent different-cell or hardware validation.

## 7. Additional possible directions, falsifiers, caveats

The new row test does NOT detect a change in first/second error marginals that leaves all mixed C_ij unchanged, as the p± source counterexample of ROT021 remains; it also does not detect all changes that can be absorbed into a different unknown SO3 gate. A zero result does not justify the Bell-source transport premise. A correct quantitative UPPER bound on ζ cannot generally be obtained by this source-restricted terminal channel geometry alone.

Experimental preconditions are significant: in the Bell-break setup the tester must have access to each noise interval to obtain both Pauli labels and must genuinely reset/reprepare the system, so the instrument necessarily differs from the original uninterrupted experiment. Independently established Bell readout error beta, physical Pauli state/POVM errors and causal source stability across preparations/settings are indispensable. For the general confidence theorem no calibration of numerical R or P is required except that the uninterrupted physical middle operation really is a stable SU2 unitary (SO3 Bloch matrix); a nonunitary unknown middle channel would invalidate the row-normalization proof. Power for the explicit source alternative additionally needs an independently established small SO3 neighborhood of R0.

Referee requests AUD3/REC13:
1. Recompute exact two-character SO3 row norm 576/245, source p_C vs p_(8/5)C 16 strictly positive histories, TV 513/8000, all ten ordinary Fourier zeros.
2. Independently derive total-variation source-character deviation |ΔC_ij|≤2ζ and monotone F(zeta)≤1 using only SO3 ROW normalization, without numerical unknown R.
3. Prove 95% source-TV LOWER CI from two Pauli IID settings and ONE Bell-label IID categorical sample (two characters from same samples), check Hoeffding alpha .025+.025, nu101504, nb125313, beta doubling, prep/POVM g=.00015, and correct 328321 resource.
4. Validate power-specific unknown-gate tolerance .001 and worst-box Fhat(0)≥1.01880145, min certified positive TV .0005378777, and distinguish this calibration from requirements for null/CI correctness.
5. Verify old ROT022 pairwise triangle is zero EXACT for TWO source contexts shifted together, despite each unit/Bell ζ=.064125; check new test detects common-mode.
6. Directly check physical W0/W1 18 full terminal entries identical with two matched proper Cliffords, same breaker sixteen labels, source ζ0 versus 5997/25099975, all original ten source Fourier zeros. Prevent any NO_GO overclaim beyond these physical contexts.
7. Contrast with latest PRX Quantum 2026 higher-order operations and 2022 self-consistent noise for external novelty; do NOT promote fundamental causal-break novelty without independent clearance.

FINAL:
PRF14_ROT023 / ORIGINAL_ROT022_ACTUAL_SOURCE_REOPENED / SINGLE_CONTEXT_TWO_PAULI_MEANS_PLUS_ONE_TWO_BELL_SOURCE_SAMPLE / GATE_UNKNOWN_SO3_ROW_ELLIPSOID_SOURCE_TRANSPORT_TEST / ARBITRARY_16_CLASSICAL_PAULI_LAW_VALID_SOURCE_TV_LOWER / SIX_ONLY_POSITIVE_EXACT_576_OVER_245_VIOLATION / EXACT_TRUE_TV_513_OVER_8000 / EXACT_IDEAL_LOWER_0P02498275 / 95PC_328321_PROTOCOL_RUNS / 95PC_SOURCE_SPECIFIC_DETECTION_WITH_MIN_TV_LOWER_0P00053788 / 800_PHYSICAL_MODEL_SYNTHETIC_EXPERIMENTS / COMMON_MODE_ROT022_TRIANGLE_BLIND / FULL_TWO_UNIT_CHANNEL_PLUS_BREAK_SOURCE_GAUGE_NO_GO_0P0002389245 / TWO_EXECUTED_SAME_AUTHOR_CODES / ZIP_7_ENTRY_CRC_SHA_PASS / NO_HARDWARE / NO_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN.
