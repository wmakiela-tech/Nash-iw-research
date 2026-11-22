---
artifact_id: IW_PRF14_ROT021_FULL_MATCHED_CLIFFORD_NINE_CHANNEL_SOURCE_TV_SHARP_2SQRT2_RELATIVE_CALIBRATION_TWO_SIDED_CONFIDENCE_AND_SIX_MARGINAL_BLINDNESS_001_20261122
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
class: TWO_TIME_CLASSICAL_JOINT_PAULI_SOURCE / FULL_NINE_TRANSFER_MATCHED_POST_CLIFFORD_PAIR / SHARP_SO3_FROBENIUS_DIAMETER_TV_LOWER / RELATIVE_ONLY_CONTROL_CALIBRATION / SIX_FOURIER_SOURCE_UPPER_CONFIDENCE / GENERAL_SOURCE_SIX_INVISIBLE_MARGINAL_DIRECTIONS
status: ORIGINAL_PRF14_ROT020_SOURCE_REOPENED / AUTHOR_ACTUALLY_EXECUTED_ORIGINAL_EXACT_SYMPY_NUMPY_SCIPY / INDEPENDENT_SAME_AUTHOR_120_PHYSICAL_PAULI_HISTORIES_EXACT / 600_PHYSICAL_SO3_POVM_BINOMIAL_MODEL_TRIALS / ZIP_SHA256_CRC_FULL_READBACK / EXTERNAL_DIFFERENT_CELL_REVIEW_PENDING
firstness: PRF13_ROT011_SIX_SOURCE_FOURIER / PRF14_ROT015_CONTROL_DEPENDENT_SOURCE / PRF14_ROT020_PAIRED_SINGLE_CHARACTER_TV_LOWER / INT10_ROT020_SHARP_SIX_CHARACTER_FOURIER_INVERSE_9_OVER_8 / PRF14_ROT021_FULL_TRANSFER_MATCHED_PAULI_FRAME_AND_UNKNOWN_GATE_TV_BOTH_SIDED_SOURCE_CONDITIONAL_CERT_INTERNAL_ONLY
claim_ceiling: NO_GENERAL_QUANTUM_COMB / NO_BLIND_SOURCE_PROOF_FOR_ARBITRARY_16_WAY_PAULI_P / NO_UNCALIBRATED_RELATIVE_FRAME / NO_HARDWARE / NO_NEW_FUNDAMENTAL_TV_NORM_NOVELTY / NO_EXTERNAL_PRIORITY / NO_CANON / NO_EXEC_SIGN
---

# PRF14 ROT021 — Full matched-Clifford channel comparison: a sharp source-TV lower bound without knowing the middle gate, and a source-conditional upper bound despite arbitrary common gate calibration error

## Executive result

ROT020 found a matched-Pauli-output-row two-setting comparison for ONE selected Fourier correlation of two classical two-time Pauli-error source distributions, independent of an unknown stable physical target gate R. It provided a 95%-valid source-TV lower confidence bound and a two-setting level/power test with an honest bounded physical SPAM/control model.

ROT021 upgrades to NINE Pauli transfer entries under TWO physical post-target Clifford contexts, while carefully distinguishing TWO DIFFERENT source classes:

**Unrestricted sixteen-way CLASSICAL Pauli joint sources:** if the two physical post-target Cliffords differ by a Pauli sign rotation D_X, their complete channel matrices align by this known output frame whenever p_A=p_B. The mismatch E after frame correction gives a source total-variation lower bound that requires NO numerical calibration of the unknown target R:
 TV(p_A,p_B) ≥ ||E||_F/(2sqrt(2)).
The coefficient 2sqrt(2) is **exactly sharp** uniformly over all valid 16-way source distributions and all target SO3 gates, attained even with STRICTLY POSITIVE 16-way source probabilities. Other valid dual lower witnesses include ||E||_2/2 and max_ij|E_ij|/2. These are ordinary classical data-processing/rotation geometry bounds, NOT generalized new physical law or a discovery of TV itself.

**Restricted PRF13 original SIX-offdiagonal-Fourier-only source family:** with all ten other Fourier coordinates held fixed to zero in BOTH conditional sources, full matched Pauli-channel equality for six measured offdiagonal transfer entries IMPLIES equality of the two source distributions at every witness where six relevant unknown gate pivots are nonzero. Hence a finite-data TV UPPER confidence certificate becomes possible WITHOUT independent knowledge of middle R, by using measured source-channel entries to lower-bound the unknown gate pivots. The exact 9/8 six-Fourier inversion operator norm in this upper confidence certificate is FIRST OWNED BY INT10 ROT020 and was directly reread/independently reenumbered here. This is a narrow pairwise source comparison, NOT a proof of source stationarity across all six ROT019 gate contexts.

**No-go:** in general p(v,w) has 15 real Fourier parameters, of which ordinary complete terminal qubit tomography of the two-noise-channel protocol sees only NINE cross-character coefficients. The remaining SIX single-error marginal characters can vary. Two strictly positive sources can differ in TV by .99 and nevertheless produce EXACTLY the SAME full transfer channel for every target R and every chosen middle control. Thus observing E=0 does NOT certify p_A=p_B in arbitrary sixteen-way Pauli source models.

## 1. Actually reopened source and different-cell firstness

Directly read the original actual ROT020 local Python program and its original machine certificate, not only a summary:
 /mnt/data/prf14_rot020/prf14_rot020_clifford_pair_context_falsifier.py
 /mnt/data/prf14_rot020/prf14_rot020_exact_physical_and_sampling_certificate.json
Pinned full ROT020 public source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/5e67f81c9d4a773c802dee496fb4a937426976ef/research/prf14/2026-11-22/IW_PRF14_ROT020_MATCHED_LEFT_FRAME_CLIFFORD_PAIR_SOURCE_TV_LOWER_CONFIDENCE_AND_TWO_SETTING_WEIGHTED_HOEFFDING_FALSIFIER_001_20261122.md
PRF13 ROT011 owns the six independent hidden source coordinates. PRF14 ROT020 owns the one-selected-character matched frame contrast and TV lower witness.

Different-cell original INT10 ROT020 PRIVATE scientific report was ACTUALLY reopened by connected GitHub immutable commit 481a6a299ef5dc23ed52f150f2ba61e435af44a9, blob 138debb4751be385b855c33311a1cc71946b7674:
https://github.com/wmakiela-tech/Nash-Priv/blob/481a6a299ef5dc23ed52f150f2ba61e435af44a9/research/int10/2026-11-22/IW_INT10_ROT020_PRF14_SHARP_PAULI_SIX_CHARACTER_TV_OPERATOR_NORM_AND_CONDITIONAL_95PC_RESOURCE_REDUCTION_001_20261122.md
It first established the SHARP six-character Fourier cube L_infinity to total-variation inversion norm 9/8 through all 64 sign vertices; improved the independently known-gate source-TV certificate from PRF14 ROT016. ROT021 independently repeated 64 vertices in source but DOES NOT claim ownership or publish private INT10 full text.

## 2. Completely physical frame-matched Clifford pair, not a virtual-label trick

Define actual unknown middle SU2 gate R with physical proper Bloch rotation R∈SO3, the original cyclic proper Clifford
 P=[[0,0,1],[1,0,0],[0,1,0]],
and known Pauli-X half-turn
 D_X=diag(+1,−1,−1).
Both proper SO3. The NEW second physically applied proper Clifford is
 B=D_X P=[[0,0,1],[-1,0,0],[0,-1,0]].
It is DISTINCT from P. Both controls are applied AFTER the unknown middle gate and BEFORE the second Pauli noise operation. Their physical channel rotations are S_A=P R and S_B=B R=D_X P R. The order P R vs R P is important. The experiment must actually distinguish contexts at the apparatus, e.g. a physical D_X operation; a purely virtual frame relabel with NO change to physical error generation does NOT constitute evidence for source-context effects.

For each q=A,B, a joint classical source p_q(v,w)≥0 on all 16 Pauli-label pairs v,w∈F2² is chosen conditional on control q ANNOUNCED BEFORE FIRST noise event. The source must be stable across Pauli state input and readout and IID terminal repetitions within q. The same physical unknown middle R is used in both contexts; if it drifts, the theorem only applies if the difference is included in the relative-control calibration mismatch below. Each q individually yields a CPTP unital channel (convex mixture of 16 Pauli-unitary histories). These context-conditioned sources are NOT automatically one intervention-independent process comb.

Define for all input Pauli j and output Pauli i the cross-source Fourier coefficient
 C^q_ij=Σ_(v,w) p_q(v,w) χ_j(v)χ_i(w), |C^q_ij|≤1.
There are NINE such cross coefficients for any unrestricted 16-way p, including diagonal C_ii. The complete Bloch transfer is exactly:
 T_A=C_A ⊙ (P R);
 T_B=C_B ⊙ (D_X P R).
Because D_X is a diagonal sign rotation, the known output-frame correction aligns:
 D_X T_B = C_B ⊙ (P R).
Therefore the full 3×3 matched-frame difference
 **E=D_X T_B−T_A=(C_B−C_A) ⊙ (P R)**.
If p_B=p_A then all NINE E_ij are zero for ANY unknown physical R, even if R has zero pivots. Under that source equality, COMPLETE CHANNEL equality T_A=D_XT_B follows. Each individual Pauli scalar is obtained by preparing +j and reading i, yielding 18 binary configurations in all.

Unlike ROT020's P/B pair sharing only one output row, this PAULI SIGN-FRAME pair aligns ALL THREE rows simultaneously, up to correct known signs. It is a genuine physical experiment only to the extent that the two controls are genuinely different physically. A laboratory may realize B by physically applying D_X after a common P pulse; its extra calibration error must be accounted for.

## 3. Sharp source-TV lower bound from full channel distance, and its proof

Let M_(v,w)=D(w)(P R)D(v)∈SO3 be the nine-component real Bloch transfer matrix of one specific pair of Pauli errors. Both frame-aligned channels are convex mixtures of the SAME sixteen M_(v,w) matrices, with source mixing probabilities p_A and p_B.

For any two proper SO3 matrices U,V:
 ||U−V||_F² = ||I−UᵀV||_F² = 8 sin²(θ/2) ≤8,
since a proper 3D rotation UᵀV has eigenvalues 1,e^{+iθ},e^{−iθ}. Thus the exact Frobenius DIAMETER of SO3 is 2sqrt(2). Couple two draws of the labels (v,w) from p_A and p_B maximally so the probability of disagreement is exactly TV(p_A,p_B). On matched draws the M matrices are equal; on mismatched draws their Frobenius separation is ≤2sqrt2. Convexity of norm yields:
 **||E||_F ≤2sqrt(2) TV(p_A,p_B)**.
Hence
 **TV(p_A,p_B)≥||E||_F/(2sqrt2)**.

This bound is SHARP EVEN WHEN EVERY SOURCE PROBABILITY IS STRICTLY POSITIVE. With ε=1/100, take p_A=(1−ε)δ_(v=0,w=0)+ε uniform16, and p_B=(1−ε)δ_(v=0,w=X)+ε uniform16. Both full-support with p_min=ε/16=1/1600. Their source TV exactly 1−ε=.99. Since the Pauli X final error yields D_X, their aligned channel difference is
 E=(1−ε)(D_X−I)(P R),
 with ||E||_F=2sqrt2(1−ε), exactly attaining equality. The original independent direct-history verifier computed all 120 unordered pairs of pure Pauli histories and verified each squared transfer separation ≤8, maximum exactly8 attained by 48 history pairs.

More conservative/equally valid alternatives:
 ||E||_2 ≤2TV because two SO3 rotations have spectral distance≤2;
 max_ij|E_ij| ≤2TV because every cross Pauli character is ±1 and |(P R)_ij|≤1.
Combine the three nonnegative lower witnesses using their MAXIMUM. These are simple classical channel-mixture contractivity facts, not newly discovered mathematical norms or minimax-optimal joint statistical tests.

## 4. Exact negative: 6 unconstrained source-marginal degrees remain invisible despite full nine channel entries

On a normalized sixteen-way joint classical Pauli source, the full Walsh–Fourier expansion has 15 nonconstant coefficients: 3 first-error marginals χ_j(v), 3 second-error marginals χ_i(w), and 9 cross-character coefficients χ_j(v)χ_i(w). Even full single-qubit channel tomography under ANY ONE deterministic middle rotation measures only the last NINE cross-character coefficients, multiplied by R-derived pivots.

Original author SymPy obtained exact rank10 of the 10×16 matrix whose rows are the normalization condition plus all nine cross characters: after fixing normalization, the source map rank9 and 6-dimensional blind space. Thus this is a 6D null source family for arbitrary p; DO NOT confuse it with PRF13's original DIFFERENT 6D hidden offdiagonal memory fiber under fixed one-time channels.

A PHYSICAL extremal visibility failure:
 p_±(v,w)=[1±(99/100)χ_X(v)]/16.
Both normalized, all probabilities min1/1600>0, and
 TV(p_+,p_−)=99/100=.99.
Yet every cross Pauli coefficient C_ij=0 for both, because w is uniformly random. Thus each of their FULL qubit transfer channels is EXACTLY the completely depolarizing map, for every middle R and every physical control, including our P/B matched pair. Both sources can have arbitrarily different first-error marginals without any possible terminal-channel evidence. There is NO two-sided interval on total SOURCE TV from the full transfer data in this GENERAL source family; an apparent zero channel difference can coexist with TV arbitrarily close to1.

A temporal first-error marginal probe or independent source-monitor restriction, beyond the present terminal channels, is necessary to remove this blind freedom. This does not disprove process tensor tomography using genuine nonunitary interventions.

## 5. Narrow positive: source TV upper confidence from 12 Pauli means and unknown R, given PRF13 six-Fourier restrictions

Suppose BOTH conditional source laws belong to exactly the original SIX-offdiagonal family, with ALL six single-error marginal Fourier coordinates and three diagonal cross-source coordinates separately fixed ZERO:
 p_q(v,w)=[1+Σ_(i!=j) C^q_ij χ_j(v)χ_i(w)]/16.
This is a STRONG physical model promise. In this six-coordinate class, the six offdiagonal C determine every p exactly. At the frozen source C0 and target R0, all six offdiagonal entries of S=P R0 are nonzero (min absolute S pivot 2/7), and the six ideal reference transfer values have min absolute
 min_(i!=j)|T_A,ij|=3/100=.03.

For an EXACT actual common middle S with all six necessary pivots nonzero,
 E_ij=(C_B,ij−C_A,ij) S_ij.
Thus equality E_ij=0 across the six offdiagonal channels forces all C_B=C_A and p_B=p_A — even though S is unknown numerically. The ratio depends on S, but the truth of an EXACT zero does not. This is pairwise identifiability only for matched P and D_XP contexts with strong six-Fourier model constraints. It does NOT certify common source across earlier unmatched contexts R,RP,RP²,LR.

Under finite shots and calibration errors, let the true common physical A rotation be \tilde S∈SO3 and the true B physical rotation \tilde S_B satisfy
 ||\tilde S_B−D_X\tilde S||_2 ≤δ_rel.
Absolute unknown R, and even a LARGE common error in \tilde S relative to ideal P R0, need NOT be known to state the confidence formula.

For each of twelve offdiagonal configurations (six Pauli input/output axes per each physical context), take n IID ±1 terminal shots. Let \hat T_A and \hat T_B be empirical mean matrices, with the same output sign correction D_X; and set \hat E=D_X\hat T_B−\hat T_A.

Assume physical state-preparation Bloch deviation≤εprep, physical binary POVM effect axis error≤εmeas and absolute offset/bias≤εbias. Set g=εprep+εmeas+εbias. For simultaneous sample-mean error η on all 12 means, standard physical unital channel contraction implies:
 |hat T_A,ij−C_A,ij \tilde S_ij|≤η+g;
 |hat E_ij−(C_B,ij−C_A,ij)\tilde S_ij|≤q,
 q=2(η+g)+cmax δ_rel,
 where cmax is externally known upper bound on magnitudes of source Fourier coefficients in these contexts. The gate error contribution is multiplied by cmax but prep/meas/POVM bias errors are NOT.

Without ever knowing \tilde S numerically, the physical source |C_A,ij|≤1 implies
 |\tilde S_ij|≥|C_A,ij\tilde S_ij|≥[|hat T_A,ij|−(η+g)]_+.
Hence each source difference is bounded with confidence by
 u_ij = min(2, [|hat E_ij|+q]/[|hat T_A,ij|−(η+g)]) when denominator>0; otherwise u_ij=2.

With all six source marginals/diagonal cross coefficients zero, the real 16-history Fourier inversion bounds source TV as
 **TV(p_B,p_A) ≤ U = min{1, (1/2)Σ_6 u_ij, (9/8)max_6 u_ij}.**
The SHARP coefficient 9/8 is INT10 ROT020's prior different-cell original result, not PRF14 ROT021's firstness; the primary author independently replayed 64 ±1 sign vertices (32 sums=36, 32 sums=24; max 36/32=9/8).

This U is a bona fide upper confidence bound on source TV for ANY six-dimensional legal paired sources satisfying external restrictions, under the concentration event. An exact SOURCE positivity check remains necessary if a numerical algorithm attempts to output reconstructed p; the upper inequality itself uses only legal actual p.

CONSERVATIVE 95%-CERTIFIABLE STATIONARY WITNESS EXAMPLE, not feasible device claim:
- Each physical p is the original strictly-positive C0 source; source is really stationary between P and D_XP.
- Each relevant physical Fourier |C_ij|≤cmax=.2; relative physical gate mismatch δ_rel≤.0002; SPAM εprep=εmeas=εbias=.00005 ⇒g=.00015.
- To provide a numerical ex ante guarantee that the upper bound U will be smaller than 0.1 even under finite sampling, assume the actual shared physical P relative control differs from nominal P by no more than .001 opnorm; then min true reference transfer≥.03−.2×.001=.0298. This COMMON calibration constraint is needed for this EX-ANTE small-denominator witness, NOT for the general validity of the data-dependent U bound.
- Choose statistical η=.00045 per mean, giving q=2(.00045+.00015)+.2(.0002)=.00124.
- In stationary truth on the joint concentration event, each |hat Eij|≤q, and lower data-derived gate pivot is at least .03−.2(.001)−2(.00045+.00015)=**.0286**.
- Each difference coefficient u_ij≤2q/.0286=.0867133, and INT10 sharp 9/8 gives
 **TV(p_B,p_A) ≤ U≤.09755244755244756 <.1** (when the source is in truth stationary).
- Hoeffding union over 12 independent ±1 means:
 P(any sampling |mhat−m_actual|>η)≤24exp(−nη²/2);
 choose n=ceil[2ln(24/.05)/(.00045)²] = **60,975,666** shots PER each of 12 offdiagonal configs, **N=731,707,992** total; failure upper .0499999961.
This is a very large SUFFICIENT resource upper, NOT sample-complexity lower or realistic hardware recommendation. It explicitly accounts for the matched-pair calibration requirement and is a source-specific power guarantee for a truthful stationary restricted family. A higher observed U or failure to reject does NOT prove source equality. The unknown gate is not numerically calibrated in the U formula.

## 6. Arbitrary 16-way source: 18-setting finite-shot source-TV LOWER confidence and drift detection

For arbitrary sixteen-way classical Pauli sources, use 9 input/output Pauli combinations under EACH of the two physical Clifford contexts: 18 independent scalar mean configurations. All Fourier coefficients |C|≤1, so no source magnitude calibration needed. Relative physical control mismatch δ_rel≤.0002, state preparation, physical POVM axis and bias each≤.00005, hence g=.00015.

Let each observed terminal mean differ from its own actual expectation by at most η=.02 simultaneously. Define nine-component empirical matched Ehat=D_X \hat T_B−\hat T_A. The true ideal matched source-contrast E0=(C_B−C_A)⊙\tilde S has for each entry
 |\hat Eij−E0ij|≤q=2(η+g)+δ_rel=.0405.
This implies ||\hat E−E0||_F≤3q=.1215, so with joint confidence
 **TV ≥ max{0, [||Ehat||F−3q]/(2sqrt2), [||Ehat||op−3q]/2, [max_ij|Ehatij|−q]/2}.**
The entrywise term uses the SHARPER q, not 3q. Because the norms and maxima are computed from the SAME empirical matrix and the coverage comes from ONE simultaneous event, taking the maximum does NOT introduce multiple-testing alpha inflation.

Hoeffding union over 18 ±1 mean settings:
 Pr(failure)≤36exp(−nη²/2).
At α=.05, n=ceil[2ln(36/.05)/(.02)²]=**32,897** per setting, total **N=592,146**, failure bound .0499925612.
The test rejecting source equality if max_ij|Ehatij|>q has false positive ≤.05 for ALL arbitrary 16-way classical Pauli source pairs with equal p, and calibrated physical devices as above.

Physical nontrivial source alternative VISIBLE HERE but INVISIBLE to ROT020's previous single Y-from-Z setting: in context B=D_X P R change ONLY coefficient C_B_(input Y, output X) by +.1, leaving A source C0 and all other B parameters unchanged. New source law p_B is strictly positive with TV=1/20=.05. One exact aligned entry E_(output X,input Y)=3/35=.0857142857, while old selected Y-from-Z E_(output Y,input Z)=0 EXACT. At the original target R0, if the common actual physical A pulse is within .001 opnorm of P R0, the magnitude of its relevant pivot is at least 6/7−.001, so the ideal true contrast is at least .1(6/7−.001)>.08561. This exceeds the worst-case two-sided detection requirement 2q=.081 by a strict margin >.00461. Thus this 18-setting familywise 95%-level test has ≥95% POWER for THIS source alternative under that additional target-control-pivot neighborhood assumption. The null coverage/lower source-TV confidence does NOT require absolute calibration of common P.

The source-TV lower confidence may be modest for one-character alternatives because its calibration/sampling error is larger than the ideal TV signal; it remains mathematically valid and is not claimed minimax optimal. The prior ROT020 targeted two-setting test is far cheaper for a PREIDENTIFIED single source coordinate.

## 7. Actually executed native exact physics, independent code, simulated binary counts

PRF14 executed original full local Python3.13 SymPy/NumPy/SciPy program (no hardware):
 /mnt/data/prf14_rot021/prf14_rot021_full_matched_clifford_source_tv.py
 SHA256 21d0ecdb10360fc2f4f3c7e0f7c8f5f1a1329a792f5b0cef7f446914a2165e58.
Original machine certificate:
 /mnt/data/prf14_rot021/prf14_rot021_exact_source_tv_machine_certificate.json
 SHA256 e1e7ebce81007c5a0acfb4354d28f048f2277fbc1c8bf02db5b3828e63002369.

Source was ACTUALLY run TWICE with byte-identical stdout, SHA256 of each stdout:
9e9201345a1ee41350d6e65b7a45a73dc3563dbed55781b6a3bd9042a9ad5311.
Both Python files pass compile. Main program EXACT SymPy source physicality and source-model checks, 64 integer Walsh cube vertices, sharp physical channel equality, rank10/6 blind, and all finite-shot ceilings. Actual 18-configuration model trials at n32,897 each: **300 null full experiments, 0 false rejections; 300 off-beacon +.1 alternative full experiments, 300 detections**. Every trial randomized a real proper SO3 common pulse with small perturbation; a different proper SO3 relative D_X control mismatch within δ_rel=.0002; physically valid qubit Bloch preparation and biased two-outcome POVM (|b|+||n||≤1); then drew actual independent binomial counts. Max realized relative SO3 operator norm error .000179697; max actual SPAM mean deviation approx .000056776. These are MODEL SYNTHETIC data, NOT quantum hardware observations, and no Monte Carlo zero error is interpreted as 100% guaranteed accuracy.

A SECOND, INDEPENDENTLY AUTHORED same-owner exact 16-Pauli-history script:
 /mnt/data/prf14_rot021/prf14_rot021_independent_pauli_history_extremal_and_blind.py
 SHA256 8b6e839d5ecc34d11052451af5a2390b114ef8f16280771e1a289cfabfcfd18c.
It does NOT import first script. It formed 16 physical Pauli unitary transfer rotations, checked ALL 120 unordered history-pair squared Frobenius distances≤8 with max8 attained by 48 pairs; recomputed the full-support sharp source pair, the p_± source blind example TV=.99 and exact depolarizing full channels, and the off-beacon full Pauli physical contrast E_XY=3/35 by explicit sum of all sixteen history matrices.

A local reproducibility archive containing BOTH executed scripts, original JSON, two identical stdout runs, direct-history second stdout and SHA-256 manifest was created, checked with ZIP CRC and complete byte-wise archive-entry readback:
 /mnt/data/prf14_rot021/prf14_rot021_reproducibility_bundle.zip
 SHA256 cc6886c84a7f9d68134a07057833b6fad770391d666fa637c3db381e64677f48.
Same-owner second implementation is NOT an independent different-cell I2 referee.

## 8. Literature / novelty / actual physics boundary

Original near-host external source actually opened:
He Wang, *Continuous-Process Randomized Compilation for Quantum Process Tensors*, arXiv:2610.01521, submitted 1 Oct 2026:
https://arxiv.org/abs/2610.01521 .
This manuscript discusses correlated classical Pauli error labels retained by memory-bearing environments, Pauli-frame covariance, bounded total variation for full adaptive records, and continuous physical implementation of controls. Its abstract and relevant original introduction were actually READ, not a complete full-manuscript priority audit. General twirling, source-to-output TV data processing and Pauli frame physics are mature. The present two-matched-Clifford inverse inequality cannot be claimed generally novel without deeper overlap comparison. Crucially He Wang's full adaptive record TV bound uses a DIFFERENT framework and premises from this restricted two-time classical source/channel inverse lower witness; do not conflate.

Further original mature references:
- Rudinger et al. *Probing Context-Dependent Errors in Quantum Processors*, Physical Review X 9, 021045 (2019), https://doi.org/10.1103/PhysRevX.9.021045: context-dependent circuit tests already mature.
- *Experimental Characterization of Crosstalk Errors with Simultaneous Gate Set Tomography*, PRX Quantum 2, 040338 (2021), https://doi.org/10.1103/PRXQuantum.2.040338: mature context-conditioned CPTP models and significance testing.
- *Optimal learning of quantum channels in diamond distance*, Nature Physics (2026), https://www.nature.com/articles/s41567-026-03499-7: channel distance learning is a developed field; only published abstract/search content checked, NO complete text review or transfer of quantitative theorems.
Neither generic channel norm inequalities nor controlled Pauli-frame comparison should be advertised as established external new science.

## 9. Exact bounded independent referee falsifiers

1. Check source class rigorously: controls announced before first error, same unknown stable target R, both conditional p_q fixed across all preparation/measurement choices; NO single comb automatically claimed.
2. Verify B=D_X P and correct position AFTER R. Distinguish physically applied different Clifford versus virtual Pauli frame.
3. Independently derive sharp Frobenius diameter 2sqrt2 for SO3 and coupling TV inequality, confirm full-support p_min1/1600 equality, and check stronger operator/max-entry alternate lower bounds.
4. Confirm rank9 cross-character map plus 1 normalization leaves EXACT six unconstrained one-error marginal Fourier directions; replay p± with TV=.99 and both full transfer channels exactly zero. This matters more than another positive bound.
5. Independently derive relative-only calibration formula and strict separation: common absolute P pulse error CANCELS from null, relative B−D A error does NOT. Check prep/POVM errors are not multiplied by cmax.
6. Verify all 18 source-agnostic two-sided confidence formulas; n=32,897/setting, full N=592,146, event tail .04999256, and source-specific off-beacon drift detection strict >2q signal. Check that upper TV for arbitrary p is IMPOSSIBLE from these data, but lower TV still valid.
7. For six-Fourier-only model verify independent source-structure premise (ten other Fourier moments precisely zero), data-derived pivot denominator, the 12-reading 95% upper interval with external cmax=.2, delta_rel=.0002, g=.00015 and common drift for power .001, sample N=731,707,992. Firstness INT10 sharp norm 9/8 must remain protected.
8. Contrast 2026 He Wang CPRC source against matched Pauli-frame experiment. Do not promote external novelty/hardware readiness.

FINAL:
PRF14_ROT021 / FULL_MATCHED_LEFT_CLIFFORD_PAIR_P_AND_DX_P / NINE_TRANSFER_UNKNOWN_R_SOURCE_CONTRAST_PASS / SHARP_FROBENIUS_2SQRT2_TV_LOWER_PASS_FULL_SUPPORT / SOURCE_ARBITRARY_16_WAY_6_MARGINAL_BLIND_TV0P99_PASS / COMMON_MODE_CONTROL_ERROR_CANCELLATION_RELATIVE_CALIBRATION_PASS / 95PC_18_SETTINGS_SOURCE_TV_LOWER_592146_SHOTS_SUFFICIENT / SIX_FOURIER_RESTRICTED_12_SETTING_TV_UPPER_LT0P1_731707992_SHOTS_SUFFICIENT / INT10_9OVER8_FIRSTNESS_RETAINED / 600_PHYSICAL_SO3_POVM_BINOMIAL_SIMULATED_TESTS / SECOND_EXACT_120_HISTORY_PAIR_REFEREE_WITHIN_OWNER / NO_HARDWARE / NO_GENERAL_COMB / NO_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN.
