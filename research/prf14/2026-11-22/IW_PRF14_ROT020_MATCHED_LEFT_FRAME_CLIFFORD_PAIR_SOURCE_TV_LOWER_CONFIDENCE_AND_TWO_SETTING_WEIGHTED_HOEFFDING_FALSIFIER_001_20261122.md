---
artifact_id: IW_PRF14_ROT020_MATCHED_LEFT_FRAME_CLIFFORD_PAIR_SOURCE_TV_LOWER_CONFIDENCE_AND_TWO_SETTING_WEIGHTED_HOEFFDING_FALSIFIER_001_20261122
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
science_class: EXACT_PHYSICAL_MATCHED_FRAME_CLIFFORD_CONTROL / TWO_SETTING_CONTEXT_CONTRAST / UNKNOWN_TARGET_GATE_INDEPENDENT_CLASSICAL_PAULI_SOURCE_TV_LOWER_CONFIDENCE_BOUND / NONIDEAL_SO3_AND_SPAM_LEVEL_POWER / SOURCE_RESTRICTED_SIX_CHANNEL_GAUGE
status: ACTUAL_SYMPY_EXACT_AND_NUMPY_SCIPY_PHYSICAL_SIM_PASS / INDEPENDENT_WITHIN_AUTHOR_DIRECT_16_PAULI_HISTORY_54_TRANSFER_PASS / 2600_SYNTHETIC_TESTS_PASS_WITH_REPORTED_ERRORS / LOCAL_BUNDLE_CRC_AND_SHA256_READBACK_PASS / EXTERNAL_AUD3_REC13_REVIEW_PENDING
firstness: PRF13_ROT011_SIX_HIDDEN_FOURIER_SOURCE / PRF14_ROT015_CONTEXT_SOURCE_DRIFT / PRF14_ROT016_FULL_CHANNEL_UNKNOWN_R_GAUGE / PRF14_ROT017_SINGLE_BEACON / PRF14_ROT018_QUADRATIC_H / PRF14_ROT019_NONCLIFFORD_Q_NEW_LINEAR_G_WEIGHTED_HOEFFDING / INT10_ROT020_SHARP_9_OVER_8_TV_INVERSE_64_VERTICES / PRF14_ROT020_MATCHED_CLIFFORD_PAIR_TWO_SETTING_SOURCE_TV_LOWER_BOUND_IN_THIS_FROZEN_LINE
claim_ceiling: NO_SOURCE_INVARIANCE_PROVEN_FROM_ACCEPTANCE / NO_GENERAL_QUANTUM_PROCESS_TENSOR / NO_REFERENCE_FREE_SPAM / NO_HARDWARE / NO_STATISTICAL_MINIMAX / NO_GENERAL_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# PRF14 ROT020 — A matched Pauli readout frame replaces an extra non-Clifford gate: two-setting Clifford context comparison and an unknown-gate-independent source total-variation lower confidence bound

## 0. Research target and principal findings

PRF14 ROT019 added a sixth calibrated post-target NON-CLIFFORD rotation Q after unknown target SU2 Bloch rotation R, generating a new linear source-beacon test G and retaining the independent quadratic H from ROT018. The G test used three calibrated scalar terminal Pauli measurements and had a 95%-sufficient upper shot count 27,669 for one legal positive Pauli-source context perturbation, with bounded controls/SPAM.

ROT020 makes a conceptually narrower and experimentally cheaper discovery: **a known physical Clifford P already used before R can also be placed AFTER R, creating a new distinct control context P R.** Its chosen measured Pauli output row coincides exactly with the previously calibrated L R context. The resulting pairwise comparison has TWO measured settings instead of THREE, and it needs NO NEW type of non-Clifford pulse (although the inherited L remains non-Clifford in the integrated design).

Moreover, the simple source contrast is not just a yes/no moment witness: **its magnitude gives a lower bound on TOTAL VARIATION between arbitrary sixteen-way joint classical Pauli error source distributions, even if the unknown target R is entirely uncalibrated and even if the ten ordinary Fourier source moments do not vanish**. With bounded SO3/SPAM errors and finite binary sampling it provides an honest simultaneous confidence lower bound on source TV.

Under source-restricted ROT013–019 witness max |hidden Fourier C|≤0.2, calibrated controls norm error≤0.001 and limited physical SPAM, 95% type-I level and ≥95% power against the specified source-beacon change .10→.20 are guaranteed with **n=8,365 binary shots for EACH of TWO settings, N=16,730 total**, versus ROT019's previous N=27,669 for an analogous changed context using the new Q. The deterministic alternative margin is small but strictly positive: .000314285714..., so no device feasibility is inferred.

Under **ARBITRARY strictly positive or nonnegative 16-way classical joint Pauli sources** (not just six hidden coordinates), max |the relevant correlation|≤1 automatically; with the same bounded apparatus errors a 95%-level/power source-specific certificate remains available at n=9,223 per setting, **N=18,446 total**, provided the alternative has the stated exact contrast 3/35. This is a genuine source-model scope widening relative to ROT013's six-param amplitude promise, but still assumes two-time CLASSICAL PAULI histories, one shared unknown middle R, and bounded calibrated controls/SPAM. There is NO unrestricted environmental quantum memory/process tensor claim.

An OPTIONAL one-sided test predeclaring the sign of the **observed effect** (not retroactively selecting it from data) lowers the source-restricted sufficient upper to n=6,794 each, **N=13,588**, but its guarantee does not apply when the source shift's measured sign is unknown (R_XZ can change sign).

Additional result: for a stand-alone source comparison, one can replace inherited non-Clifford L entirely by TWO DISTINCT proper Clifford controls P and B applied after R, with the same measured row. Both must be realized as genuinely distinct physical interventions; a virtual Pauli-frame relabeling alone is NOT evidence of context-dependent physical source behavior.

NEGATIVE: Passing this test cannot verify equality of conditional sources; it is only a one-sided falsifier. All 54 full Pauli transfer entries in six preannounced contexts still admit an EXACT source/gate physical alias under allowed context-conditioned Pauli source, proved with an independently written literal 16-history Kraus sum.

## 1. Sources, scientific firstness and mature near-host

Original PRF14 ROT019 current pinned full 24,571-character report directly reopened:
https://github.com/wmakiela-tech/Nash-iw-research/blob/52fa28861ee21b79c0adb5c71df92f7ece417a96/research/prf14/2026-11-22/IW_PRF14_ROT019_SIX_CONTEXT_TWO_INDEPENDENT_FOURIER_BEACON_CLOSURES_WEIGHTED_HOEFFDING_PHYSICAL_NONCLIFFORD_AND_54_CHANNEL_GAUGE_NO_GO_001_20261122.md
Original local executed ROT019 source actually read:
 /mnt/data/prf14_rot019/prf14_rot019_dual_beacon_closures.py
and original certificate:
 /mnt/data/prf14_rot019/prf14_rot019_dual_closure_certificate.json.
PRF14 ROT018 original retained new H source identity firstness, and PRF13 ROT011 retains original six hidden source Fourier dimensions.

Separate INT10 ROT020 private original 14,321-character report (actually reopened, Git blob138debb4751be385b855c33311a1cc71946b7674) owns NEW SHARP Fourier-to-TV L∞ inverse norm 9/8 over 64 sign vertices, improving ROT016's known-R TV cert from 1.017 trillion to 131.845 billion sufficient shots. ROT020 here does NOT subsume or claim INT10's inverse-map norm; it proves a DIFFERENT, lower-direction TV witness using one measured Fourier contrast and two matched-frame channels. Original INT10 private URL:
https://github.com/wmakiela-tech/Nash-Priv/blob/481a6a299ef5dc23ed52f150f2ba61e435af44a9/research/int10/2026-11-22/IW_INT10_ROT020_PRF14_SHARP_PAULI_SIX_CHARACTER_TV_OPERATOR_NORM_AND_CONDITIONAL_95PC_RESOURCE_REDUCTION_001_20261122.md

Public primary external currentness checked in this turn:
Kenneth Rudinger et al., *Probing Context-Dependent Errors in Quantum Processors*, Physical Review X 9, 021045, published 3 June 2019, https://doi.org/10.1103/PhysRevX.9.021045 — matched-circuit context comparison and rigorous statistical context testing are MATURE GENERAL METHODS.
P. Viñas/A. Bermudez, *A context-aware gate set tomography*, npj Quantum Information, 26 June 2026, https://doi.org/10.1038/s41534-026-01313-z — physically modeled context dependence and coherent drift mature.
*Experimental Pauli-frame randomization on a superconducting qubit*, Physical Review A 103, 042604 (2021), https://doi.org/10.1103/PhysRevA.103.042604 — an important reminder that physically changing Pauli controls and changing virtual logical Pauli descriptions are not equivalent experimental interventions. Do not claim this paper establishes our specific source bound or source model.
General exact TV duality, matched Pauli-frame design, and two-sample concentration are elementary established tools. This report asserts ONLY an internal source-specific construction and its reproducibility, NO external novelty.

## 2. Valid physical source class and matched post-target control design

Let v,w∈F₂² label the two classical Pauli errors U_v before, U_w after a selected middle SU2 unitary. In each *preannounced* context q a joint source law p^q(v,w) is chosen, stable across terminal Pauli preparation/measurement and IID repeated runs. The q-dependent source models are separately causal/CPTP; in general they are NOT one fixed intervention-independent exogenous comb. For every i,j Pauli axis pair, the full unital Bloch channel transfer satisfies

 T^q_ij = C^q_(j,i) [S_q(R)]_ij,

 where C^q_(j,i)=Σ_v,w p^q(v,w) χ_j(v)χ_i(w).
This entrywise exact law HOLDS FOR ANY 16-WAY classical Pauli joint law, not only the earlier special subclass whose ten ordinary Fourier coefficients were zero. For a physical probability law |C^q_(j,i)|≤1. Unitary Pauli mixtures imply the full channel Bloch contraction ||T^q||₂≤1 even when ordinary moments are nonzero.

Freeze the exact previous target test rotation and original six-hidden-correlation source witness only when explicit numeric costs are required:
 R0=[[-3,-2,6],[6,-3,2],[2,6,3]]/7;
 P=[[0,0,1],[1,0,0],[0,1,0]], P³=I, signed axis-permutation Clifford, det+1;
 L=[[0,1/√2,1/√2],[1,0,0],[0,1/√2,-1/√2]], det+1, non-Clifford;
 C=[[0,.09,.11],[.07,0,.10],[.08,.12,0]],
 all 16 original p strictly positive min 73/1600=.045625.
The sixth intervention now uses **P AFTER R**, namely S5=P R, instead of ROT019's former Q R. Importantly S1=R P already exists as a DIFFERENT physical context; P R and R P do not commute generically.

For output Pauli i=Y and input j=Z:
 row_Y(L)=row_Y(P)=e_X^T,
 so (L R)_YZ=(P R)_YZ=R_XZ.
For the same source correlation c=C_(Z,Y) across q3=LR and q5=PR,
 y_L=cR_XZ, y_P=cR_XZ,
 and the NEW two-setting matched-frame linear closure is
 **G_C = y_(P R)−y_(L R)=0**.
This is valid for EVERY physical SO3 target R and arbitrary (possibly different) other Fourier source moments.

The general matched-frame principle: two known proper controls A,B placed after unknown R, with identical output Pauli row e_i^T A=e_i^T B, produce the SAME terminal i-from-j mean under equality of the one source correlation C_(j,i) across those two controls. Conversely, if the same equality is to hold for ALL R∈SO3 and for an arbitrary nonzero common source correlation, the selected output rows MUST coincide (up to sign for a signed-sum identity), since R e_j ranges over the unit sphere. This shows precisely why sharing the measured row is a sufficient and (within the stated all-R linear contrast class) necessary design principle; it is NOT a global quantum test optimality theorem.

### Stand-alone TWO-CLIFFORD version

Choose a SECOND known proper signed-axis-permutation Clifford
 B=[[0,1,0],[1,0,0],[0,0,−1]],
 BᵀB=I, det B=+1, B≠P.
Then row_Y(B)=row_Y(P)=e_X^T, and for the two separately implemented post-target contexts P R and B R,
 y_(P R)=C^(P R)_(Z,Y) R_XZ,
 y_(B R)=C^(B R)_(Z,Y) R_XZ.
Thus exact G_Cliff=y_BR−y_PR=0 if the respective source correlations match. NO non-Clifford gate is required by THIS STAND-ALONE two-context test. Direct physical 16-label Kraus replay proves the full channels P R and B R are DIFFERENT in the other transfer matrix entries even though the chosen Y-from-Z expectation is the same under an invariant source. Hence the experiment is not merely replotting exactly the same full channel.

The experimental condition is material: B must be a DISTINCT physical intervention capable of changing the hypothetical source, not a purely virtual change of Pauli-frame bookkeeping or an algebraic convention. If B is synthesized from more than one physical pulse, its **composite** norm calibration error, not one arbitrary per-pulse error, must meet the advertised δ≤.001; otherwise recalibrate the B systematic budget. The stand-alone two-Clifford test is NOT a drop-in replacement for L's role in earlier four-world global gate/source disambiguation; it solves specifically the source-context contrast task.

## 3. Exact physical positive source alternatives and independence from H

Within the previous six-source-coordinate positive witness the original source has min p=73/1600, while shifting ONLY one conditional source's beacon from c=.10 to c=.20 leaves all its 16 history probabilities STRICTLY positive with min p=63/1600=.039375 and TV from original source exactly .05. The other five hidden Fourier coefficients and all ten ordinary coordinates can be held unchanged.

Under six controls (R,RP,RP²,LR,P²R,PR), exact baseline means:
 (y0,y1,y2,y3,y4,y5)=(1/35,3/35,−3/70,3/35,3/70,3/35).
Old H=y3²+y4²−y1²−y2²; new G_C=y5−y3.

For four physically legal scenarios:
* Null all six same source: H=0, G_C=0.
* Only PR beacon .1→.2: H=0 EXACT, G_C=+3/35. This is invisible to old H and detected by G_C.
* Only LR beacon .1→.2: H=27/1225, G_C=−3/35. Both detect; this is same exact original LR drift as ROT018/019.
* BOTH LR and PR beacons .1→.2: H=27/1225, G_C=0 EXACT. The new G_C misses the source change but H detects it.

SymPy independently checked proper physical R,P,L,B gates, exact source positivity, exact TV=.05, all four H/G identities and 6×4 beacon Jacobian rank4. Its two H/G normal covectors are linearly independent and annihilate the 6×4 gate-plus-common-beacon Jacobian, so ROT019's TWO overidentifying source-model conditions persist even after replacing Q by a Clifford. There is no reduction to one duplicate algebraic identity.

Note the null for G_C is only **PAIRWISE equality** C^(PR)_(Z,Y)=C^(LR)_(Z,Y), not a claim that all six source coordinates are unchanged in all contexts. H has its separately stated larger source-beacon invariance premise.

## 4. Stronger new source-model-independent TV lower bound, including finite-sample confidence

For ANY arbitrary classical joint law p(v,w) on sixteen pairs, the source correlation c=E_p[χ_Z(v)χ_Y(w)] is the expectation of a ±1-valued character. For two source laws a,b, the total variation dual norm gives
 |c_a−c_b|≤2 TV(p_a,p_b).
Combined with exact matched post-control row:
 G_C=(c_(PR)−c_(LR))R_XZ.
Because any proper R has |R_XZ|≤1, obtain the GATE-INDEPENDENT LOWER BOUND:
 **TV(p^PR,p^LR) ≥ |G_C|/2.**
If R_XZ is known and nonzero from a genuinely independent gate reference, a sharper bound is
 TV ≥ |G_C|/(2|R_XZ|).
For the original specific single Fourier-character perturbation, |G_C|=3/35, |R_XZ|=6/7, so sharp known-R lower bound TV≥.05 is attained EXACTLY by the legal source change. Without gate calibration the universal valid lower is only 3/70≈.0428571; do not imply equality in the generic bound.

This is source-agnostic WITHIN the classical two-time Pauli model: none of the other 15 source degrees of freedom need be held fixed or equal. It does not automatically apply to arbitrary non-Pauli quantum environment histories. The conservative nonnegativity [x]_+ denotes max(0,x).

With actual bounded systematic calibration and binary sampling, let \hat G_C=\hat y_PR−\hat y_LR. If, with confidence 1−α, 
 | \hat G_C − G_C | ≤ B+t,
the rigorous confidence lower bound follows by triangle inequality:
 **TV(p^PR,p^LR) ≥ [|\hat G_C|−B−t]_+/2.**
The test rejecting equality at |\hat G_C|>B+t is simultaneously a source-TV>0 certificate at stated coverage, conditional on one stable middle R, actual controls within calibration caps, and classical Pauli source histories.

The paired-control frame source TV fact and general total-variation dual norm are mathematically classical; no claim of new operator theory or external novelty is made.

## 5. Physical calibration, binary Hoeffding, level/power and exact costs

Both pair settings use ONE known control AFTER target (either L/P integrated or P/B all-Clifford), so no P² double-pulse error is incurred in the pair test. Suppose each implemented physical SO3 control has externally guaranteed operator-norm error ≤δ=.001 from its nominal R-relative control, independently bounded per setting. Prepared +Z physical Bloch input error≤εprep=.00005, final binary Y-POVM effect Bloch axis error≤εmeas=.00005, bias |b|≤εbias=.00005, with |b|+||n||≤1. Source law stable within each setting and independent across shots; middle unknown R stable across contexts. These are nontrivial verified-device requirements, NOT calibration results measured by PRF14.

At each setting the terminal source-dependent Bloch channel has norm≤1, and the selected Pauli-axis gate error term is multiplied by the magnitude |c^q_(Z,Y)|. Consequently
 μ_q ≤ |c^q_(Z,Y)|δ + εprep+εmeas+εbias.
If the relevant source correlation is capped at cmax, each mean has μ≤cmaxδ+.00015, and the paired difference has worst-case systematics
 **B=2(cmaxδ+.00015).**
The SPAM terms are NOT multiplied by cmax because an axis error can couple to other channel coefficients.

Take n independent ±1 observations at each of the TWO settings. Difference \hat G is a weighted sum of two independent sample means with weights (+1,−1) and sum of squared weights=2. Hoeffding gives the exact distribution-free sufficient tail:
 P(|\hat G−E\hat G|>t) ≤2 exp(−n t²/4).
The TWO-SIDED decision rule rejects pairwise source-beacon equality if
 **|\hat G|>B+t.**
Under pair equality and apparatus assumptions, type-I ≤2exp(−n t²/4). For a predesignated physical alternate with exact ideal magnitude Δ=|G_C|, detection is certain on the same ±t concentration event if
 **Δ>2(B+t)**, implying alternative-specific power ≥1−2exp(−n t²/4). This is a true joint level/power sufficient guarantee, not a Gaussian approximation.

### Tier A: frozen restricted source family cmax=.2
δ=.001, SPAM three eps each .00005:
 μ=.00035, B=.00070.
Choose t=.042 (conservative meaningful positive strict margin Δ−2(B+t)=.000314285714... for Δ=3/35).
At α=.05, n=ceil[4ln(40)/(.042)²]=**8,365 shots EACH**, total **N=16,730**.
The Hoeffding tail is .04999572289<.05. Same guarantee for qPR-only increase and for qLR-only increase, but the source contrast's SIGN flips accordingly. Compared with ROT019's earlier n=9,223 THREE-setting Q test N=27,669, the new sufficient upper is 1.65× lower, with no new non-Clifford pulse.

### Tier B: arbitrary 16-entry classical Pauli joint source cmax=1
For every such legal p, |c|≤1 automatically. Same physical calibration δ and SPAM bounds:
 μ=.00115, B=.00230.
Choose t=.040, strict margin Δ−2(B+t)=.001114285714..., n=ceil[4ln40/(.040)²]=**9,223 shots EACH**, **N=18,446**.
Two-sided Hoeffding tail .04998397527<.05, so level≤.05 for ANY stable lawful classical Pauli source pair with same relevant correlation and specified model apparatus, power≥.95 for the PARTICULAR alternative whose ideal contrast is |G_C|=3/35. No assumption about the other 15 Fourier coordinates enters the pairwise TV conclusion.

### Optional predeclared direction
If the SIGN of the expected observable G_C is independently preregistered before data, one-sided Hoeffding uses exp(−n t²/4) and the same strict alternative margin. With cmax=.2, t=.042, n=6,794 EACH, total **13,588**; this is NOT valid for unconstrained alternative direction, especially because sign(R_XZ) is unknown in general. The PRIMARY result remains TWO-SIDED N=16,730.

Finite-sample source-TV confidence lower bound in each tier:
 TV≥max(0,|\hat G|−B−t)/2 with ≥95% coverage on joint sampling event.
This certificate can be numerically weak (e.g. at ideal observed |G|=3/35, Tier A bound≈.021507) but is valid without knowing target gate. No minimax optimality claim or guarantee for arbitrarily weak source drift.

## 6. Independent exact physics, honest synthetic execution statistics and no-go

The native main source was ACTUALLY run twice with byte-identical stdout and JSON; it computes exact proper SO3 gates, Fourier positivity of two physical source histories, the exact 6×4 rank4 and two independent H/G gradients, all exact H/G counterexamples, the two-tier Hoeffding plan and calibration margins. It also runs PHYSICALLY LEGAL synthetic Bernoulli counts under perturbed SO3 controls, perturbed actual Bloch input vectors and biased physical binary POVM effects.

Local executable:
 /mnt/data/prf14_rot020/prf14_rot020_clifford_pair_context_falsifier.py
SHA256 8a3bc58667c9cb1fb3be8ee5d4d2a49c5a48f5b48a4bcea273c4539ab2f488a3.
Original executed JSON:
 /mnt/data/prf14_rot020/prf14_rot020_exact_physical_and_sampling_certificate.json
SHA256 1df8f176df7a592678c3d80c0cbad06f8b6b2f615f4bd564518b614d95770229.

Actual model sampling results are reported IN FULL, without concealing expected statistical errors:
- Tier A restricted (n=8365 each), 700 NULL experiments yielded **3 false positive decisions**, 700 qPR drift experiments yielded **698 detections, 2 misses**.
- Tier B full classical Pauli bound (n=9223 each), 300 NULL experiments yielded **1 false positive**, 300 qPR drift experiments yielded **300 detections**.
- Stand-alone Clifford-only P/B at n=8365 each, 300 NULL experiments yielded **0 false positives**, 300 B-context drift experiments yielded **298 detections, 2 misses**.
TOTAL **2,600 complete two-setting synthetic experiments**, counted using actual binomial random number generation with valid physical SO3/POVM apparatus. They are NOT experimental quantum hardware shots. A 95% *guarantee* does NOT mean zero false alarms or 100% Monte Carlo detection. The analytic theorem, not the simulation counts, establishes the advertised conditional coverage.

SEPARATE INDEPENDENTLY AUTHORED SAME-CELL direct 16-Pauli-history Kraus programme:
 /mnt/data/prf14_rot020/prf14_rot020_independent_direct_16_history_kraus.py
SHA256 d665ae3ace8c75c584745e768159b6d7df8b028ab462dc021474034c6d9337d7.
This program DOES NOT import main-code routines. It computes 16 probabilities, the channel matrix as literal Σ_(v,w) p(v,w)D(w)S_qD(v), checks:
- L R, P R, B R have exactly the SAME target Y-from-Z Pauli expectation under stationary source;
- P R and B R are physically DIFFERENT CPTP channel matrices on other axes, so a new q is a real intended control;
- all 6 source-conditioned contexts for proper alternate target R'=U_X(1/1000)R and adjusted C'^q_ij=C_ij[S_q(R)]_ij/[S_q(R')]_ij remain strictly positive and yield EXACT the SAME **54 full Bloch transfer entries** as the stationary original six-context source/gate;
- thus even perfect full six-channel tomography and both H=G_C=0 cannot demonstrate source-control invariance in the enlarged context-dependent source model. An altered source can hide inside the gate/source gauge, and a drift in any of the other five Fourier coordinates may be entirely invisible to this pair test.

Reproducibility ZIP:
 /mnt/data/prf14_rot020/prf14_rot020_reproducibility_bundle.zip
SHA256 8b0b27b8ae966e8ff492f84a37328bc8ed46a7081f40e1e24bd84f1a64e0d66a.
Includes actual executable primary and separate Kraus check, original detailed JSON, two stdout records, individual SHA256 manifest. ZIP testzip CRC and complete byte-wise entry readback PASS. A complete repeated source execution produced byte-identical stdout and certificate. Independent different-cell referee has NOT yet been performed; within-author two implementations do not count as independent I2.

## 7. Scientific limitations, falsifiers and recommended next experiments

- No outcome of the two-setting test validates common-source correlation if G_C=0. Equality may arise from a true shared beacon, a blind R_XZ=0, compensated drift, control miscalibration or a physical gate/source gauge. Claim only consistency; reject on statistically significant |G_C|.
- Source-TV lower confidence requires SAME stable unknown R across the compared contexts, the PAULI CLASSICAL history law and independently justified control/SPAM error limits. If target R itself changes across q, difference can be a gate effect, not necessarily source TV; the source-TV inference fails outside its model.
- The all-Clifford P/B test needs truly distinct calibrated physical interventions, not merely virtual Pauli frame redefinitions. Unconstrained experimental drift correlated with time ordering can mimic context dependence unless context trials are randomized/interleaved and run-block effects audited.
- With B synthesized from a gate sequence, the full composite B-pulse calibration norm is the correct error budget; “Clifford” does not imply perfect hardware calibration.
- For the original six-hidden-Fourier class the G_C pair test ignores the other five source coefficients. H is independently nonredundant and captures selected compensated changes; still no source invariance confirmation.
- Do not compare N=16,730 vs ROT019 N=27,669 as measured hardware performance or information-theoretic optimum. These are conservative SUFFICIENT Hoeffding upper bounds for similar but different sixth intervention contexts and specified witness drifts. The same qLR-only original physical drift can be tested by the new pair, giving a closer comparative basis.
- To obtain device-relevant results, calibrate P/L or P/B independently, randomize intervention order, pre-register alternatives, perform actual paired contrast and compare against mature context-dependence tests; such hardware data were NOT produced.

REFEREE TASKS AUD3/REC13: independently verify rowY P=L=B=eX, proper Clifford B and distinct full P R/B R channels; exact 6×4 rank and H/G independence; source TV dual bound without six-Fourier restrictions; calibrated per-mean µ=.00035/.00115, pair B=.0007/.0023, strict power condition and 8365/9223 two-setting n; truthful simulation 3/700 false and 698/700 detection; direct 54 Kraus physical source/gate alias and ordinary-10-Fourier-zero scope of that *negative* witness; test virtual control caveat. Preserve INT10 TV inverse firstness. External novelty/general multi-time tensor not cleared.

RETURN:
PRF14_ROT020 / ORIGINAL_ROT019_SOURCE_REOPENED / Q_NONCLIFFORD_REPLACED_BY_EXISTING_POST_TARGET_P_CLIFFORD / MATCHED_FRAME_TWO_SETTINGS_IDENTICAL_NULL / STANDALONE_PAIR_TWO_DIFFERENT_CLIFFORDS / ALL_CLASSICAL_16_SOURCE_TV_GATE_INDEPENDENT_LOWER_CONFIDENCE / SOURCE_RESTRICTED_TWO_SIDED_95PC_16730 / FULL_CLASSICAL_PAULI_95PC_18446 / OPTIONAL_PREREGISTERED_ONE_SIDED_13588 / TWO_INDEPENDENT_H_G_6X4_JAC_PASS / 2600_MODEL_SIMULATIONS_WITH_REPORTED_FALSE_ALARMS_AND_MISSES / 54_COMPLETE_CHANNEL_UNKNOWN_GATE_CONTEXT_SOURCE_GAUGE_PASS / ZIP_SHA256_CRC_READBACK_PASS / NO_HARDWARE / NO_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN.
