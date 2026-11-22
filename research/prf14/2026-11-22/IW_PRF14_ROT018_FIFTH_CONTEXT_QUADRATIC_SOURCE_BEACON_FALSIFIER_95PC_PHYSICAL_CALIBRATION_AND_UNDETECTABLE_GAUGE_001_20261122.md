---
artifact_id: IW_PRF14_ROT018_FIFTH_CONTEXT_QUADRATIC_SOURCE_BEACON_FALSIFIER_95PC_PHYSICAL_CALIBRATION_AND_UNDETECTABLE_GAUGE_001_20261122
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
science_class: FIVE_CONTEXT_CLASSICAL_PAULI_MEMORY / ONE_SOURCE_FOURIER_BEACON / QUADRATIC_SO3_OVERIDENTIFICATION / EXACT_POSITIVE_SOURCE_DRIFT / FINITE_SAMPLE_LEVEL_AND_POWER / BOUNDED_SO3_SPAM / EXACT_5_CHANNEL_UNTESTABILITY_NO_GO
status: AUTHOR_EXECUTED_EXACT_SYMPY_PASS / DIFFERENT_ALGORITHM_45_PAULI_HISTORY_ENTRIES_PASS / 4800_TOTAL_SYNTHETIC_COUNT_EXPERIMENTS_PASS / SOURCE_REPLAY_BYTE_IDENTICAL / EXTERNAL_DIFFERENT_CELL_REFEREE_PENDING
claim_ceiling: NO_GENERAL_QUANTUM_PROCESS_TENSOR / NO_BEACON_PROOF_FROM_PASSING_WITNESS / NO_HARDWARE / NO_GENERAL_CONTEXT_DETECTION_NOVELTY / NO_CANON / NO_EXEC_SIGN
firstness: PRF13_ROT011_6D_FOURIER / PRF14_ROT013_FULL_SIX_COORDINATE / PRF14_ROT015_CONTEXT_DRIFT / PRF14_ROT016_FULL_FOUR_CHANNEL_3D_ALIAS / PRF14_ROT017_ONE_BEACON_LOCAL_GLOBAL / PRF14_ROT018_NEW_FIFTH_LEFT_CONTROL_QUADRATIC_FALSIFIER
---

# ROT018 — A fifth Clifford context yields a gate-independent quadratic falsifier of a single invariant Pauli-memory source correlation, with exact nonidentifiability limits

## 1. Scientific question / original source

ROT017 showed that ONE of six chosen off-diagonal two-time classical Pauli-source Fourier coordinates, if actually shared across four middle-control contexts, can locally identify an UNKNOWN stable SU2 middle gate R and the four separately variable source distributions. For two beacons, source-specific Fourier positivity also admits only one globally physical solution. HOWEVER the four-context model is saturated at 24 observations /24 model degrees and therefore cannot falsify its own crucial single-beacon premise. ROT016 gave a 3D physical unknown-gate plus context-specific-source gauge reproducing all four complete channels while violating the beacon.

ROT018 asks what the MINIMUM intervention extension can do: add one left-side known Clifford after unknown R, leaving correlated two-time errors as before. Exact answer: ONE NEW QUADRATIC OVERIDENTIFYING MOMENT IDENTITY, independently of unknown gate and beacon amplitude, that can falsify but NOT verify one chosen beacon. A complete finite-sample level and power test is proved for a particular strictly positive physical source drift, both with ideal and bounded imperfect Clifford/SPAM implementations. An independent full five-channel source/gate physical alias shows fundamental residual nonidentifiability.

Actually reopened ORIGINAL local ROT017 executable, original detailed machine JSON and pinned full report; source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/3676940744e21101b25516a9d1b3a4512d132809/research/prf14/2026-11-22/IW_PRF14_ROT017_ONE_FOURIER_BEACON_24_CONTEXT_CHANNEL_LOCAL_SO3_ANCHOR_GLOBAL_POSITIVE_BRANCH_CLASSIFICATION_AND_UNTESTABLE_ANCHOR_NO_GO_001_20261122.md
Original ROT016 physical full-four-channel alias:
https://github.com/wmakiela-tech/Nash-iw-research/blob/86c2f2a1b81b59e52ff5baaa4f21c0f11bb6a54f/research/prf14/2026-11-22/IW_PRF14_ROT016_FULL_FOUR_CONTEXT_24_CHANNEL_TOMOGRAPHY_UNKNOWN_GATE_3D_PHYSICAL_ALIAS_KRAUS_I1_AND_EXTERNALLY_ANCHORED_TV_CERT_001_20261122.md
PRF13 ROT011 still owns original six hidden Pauli-Fourier dimensions.

## 2. Physical conditional two-time source and five SU2 controls

Two classical Pauli-label errors (v,w) in F2²×F2² have a strictly positive joint probability law p^q(v,w) conditional on middle-control context q, which must be announced BEFORE the first error event. Run: U_v, physical target-plus-known-control single-qubit unitary, U_w; IID within each context. The source may depend on q but not the chosen Pauli input preparation or final readout within q. Each context is lawful causal CPTP, but generally the five contexts are NOT one exogenous intervention-independent quantum comb.

Ten ordinary Fourier coordinates remain zero in all sources, so the first/second/idle Pauli channels depolarize; six independent ordered off-diagonal source coordinates C^q_(j,i) remain, with
 p^q(v,w)=[1+Σ_(i≠j) C^q_(j,i) χ_j(v)χ_i(w)]/16.
For each one middle Bloch SO3 matrix S_q, the FULL unital qubit Pauli channel Bloch transfer is
 T^q_ij=C^q_(j,i) S_q,ij if i!=j and T^q_ii=0.
This is exactly a positive 16-term Pauli-unitary mixture.

Exact baseline physical unknown middle gate:
 R=[[-3,-2,6],[6,-3,2],[2,6,3]]/7.
Known Clifford cyclic P=[[0,0,1],[1,0,0],[0,1,0]] with P³=I.
Known original left control:
 L=[[0,1/sqrt(2),1/sqrt(2)],[1,0,0],[0,1/sqrt(2),-1/sqrt(2)]].
Five physically proper SO3 control matrices:
 S0=R, S1=RP, S2=RP², S3=LR, NEW S4=P²R.
Do NOT interchange RP² and P²R; position after the unknown gate is precisely the new scientific intervention.

Baseline strictly positive six-parameter source:
 C=[[0,9/100,11/100],[7/100,0,1/10],[8/100,12/100,0]]
where C rows indexed output Pauli i, columns input Pauli j. All sixteen source probabilities are positive, min 73/1600, and normalized; 6 source coefficients can vary independently in an open physical domain.

## 3. NEW exact one-beacon quadratic closure

Choose ONE nonzero source beacon c=C^q_(Z,Y)=C^q_(input Z,output Y), assumed constant across all FIVE contexts. Other five Fourier source coordinates can vary freely between contexts (subject to positivity). Prepare +Z and measure terminal Pauli Y, obtaining exact scalar expectations:

 y0=c R_YZ;
 y1=c (RP)_YZ=c R_YX;
 y2=c (RP²)_YZ=c R_YY;
 y3=c (LR)_YZ=c R_XZ, since L row Y is e_X;
 y4=c (P²R)_YZ=c R_ZZ, since P² row Y is e_Z.

SO3 row-Y and column-Z squared norms each equal 1:
 y0²+y1²+y2² = c² = y3²+y0²+y4².
Subtract:
 **H(y)=y3²+y4²−y1²−y2²=0.**

This eliminates both the UNKNOWN R and the beacon c. Only FOUR terminal Pauli settings q=1,2,3,4 are needed in the test statistic, as y0 cancels. The new fifth context produces the missing y4; it is not a redundant right-side control.

Exact reference four terms:
 y1=3/35; y2=−3/70; y3=3/35; y4=3/70;
 y0=1/35; H=0 exactly.

The underlying 5-scalar beacon measurement map has four locally independent parameters (c plus three SO3 rotations). Independent exact SO3-generator Jacobian computation of the 5×4 matrix gives rank FOUR and the nonzero gradient
 (0,−2y1,−2y2,2y3,2y4)
annihilates its tangent exactly. Geometrically H=0 is the single kinematic feasibility constraint among the five beacon means when the first three right means are not all zero: their norm gives |c|, and the two complementary SO3 rows rotate on a circle. This does NOT imply other source Fourier probabilities are physical or beacon invariance true.

For complete channel tomography under all FIVE contexts: 5*6=30 independent context-source coefficients and 3 unknown gate coordinates, minus FOUR equalities from one 5-context beacon, gives 29 local parameters vs 30 observed offdiagonal full-channel scalars. Nonzero pivots for 25 nonbeacon source coordinates and the rank-4 beacon block imply a 30×29 Jacobian of rank29 at the source witness. Thus ONE overidentifying residual is genuinely added beyond ROT017's saturated 24-vs24 four-context case.

## 4. A strictly positive physical source deviation violating H

Change ONLY left-L context q3 beacon C^3_(Z,Y) from c=.1 to .2, leaving all other 5 source Fourier coordinates, all other four context source laws, target gate and all controls unchanged. This produces a NORMALIZED STRICTLY POSITIVE sixteen-label p^3 with min 63/1600=.039375, full Pauli CPTP transfer and exact total variation TV(p^3,p)=|.2−.1|/2=.05. It leaves all ten ordinary source Fourier coordinates at zero.

New exact five means:
 (y0,y1,y2,y3,y4)=(1/35,3/35,−3/70,6/35,3/70).
Hence
 **H_true = 27/1225 = .02204081632653... ≠0.**
This is one physical detectable context effect, NOT the minimum detectable TV or general sensitivity of all nonstationary sources.

## 5. New rigorous adaptive Hoeffding level-and-power test, 222,780 shots

Repeat each of FOUR relevant settings q=1,2,3,4 n times, receiving independent IID terminal ±1 binary results and empirical means mhat. Let
 Hhat=mhat3²+mhat4²−mhat1²−mhat2².
Choose η>0; on event all four |mhat_k−m_k|≤η,
 |Hhat−H_true|≤2η Σ_(4) |mhat_k|+4η²
(by the elementary square perturbation identity and triangle inequality).

**REJECTION RULE:** reject the hypothesis of one beacon invariant across five controls iff
 |Hhat| > Bhat(η)=2η Σ_(4)|mhat_k|+4η².

Under null, H_true=0 regardless of unknown physical R and value of common beacon c; there is NO rejection on the concentration event. ±1 Hoeffding union gives
 P_null(false reject)≤8exp(−nη²/2).

For a predesignated alternative with |H_true| and S=Σ_(4)|m_k|, simultaneous detection for ALL possible errors in the η-box holds if
 |H_true|>4η S+16η².
The bound follows from |Hhat|≥|Htrue|−2η S−4η² while Bhat≤2η(S+4η)+4η²=2η S+12η².

For physically legal +.1 qL beacon drift:
 |H_true|=27/1225, S=12/35.
Choose η=27/2000=.0135; exact strict power-margin
 |Htrue|−4η S−16η²=7479/12250000=.00061053061224>0.
For α=.05 take
 n=ceil[2 ln(8/.05)/η²]=**55,695 shots each**;
 N=4n=**222,780 shots**.
The theorem guarantees under source-specific physical model:
 (a) maximal false rejection probability ≤.049998347 in H0;
 (b) probability of detecting the stipulated +.1 qL drift ≥.950001653.
This guarantee is derived from exact inequalities, NOT from the later Monte Carlo.

## 6. Nonideal SO3 controls, Bloch input/POVM and robust 240,248-shot certificate

Allow one calibrated physical cyclic P pulse \tilde P with spectral norm error ≤δP=.001, so an applied P² implemented as two pulses has error ≤2δP. Allow left control \tilde L with spectral norm error ≤δL=.001. Allow physical prepared Bloch vector ||x−e_Z||≤εprep=.00005, binary physical POVM mean b+n·r with |b|+||n||≤1, ||n−e_Y||≤εmeas=.00005 and |b|≤εbias=.00005. Within each configuration errors remain stable and trials IID. The q4 POST-gate P² also has at most two-pulse error 2δP; this is not the same as RP².

For our specified fixed or +.1-drift physical source family max over all six Fourier coefficients and all contexts is cmax=.2. Physical Pauli-mixture channel contraction ||T||₂≤1 implies a uniform bound on ACTUAL minus nominal ideal beacon means
 μcal=max(2*cmax*δP,cmax*δL)+εprep+εmeas+εbias
 = **.00055**.
Crucially prep/measurement axis errors are NOT suppressed by cmax; they may couple to other channel entries.

Choose Hoeffding statistical ηstat=.013 per each of four actual ±1 means and effective ideal-reference e=ηstat+μcal=.01355. Use exactly the same decision rule with Bhat(e), not Bhat(ηstat). Alternative strict power margin
 27/1225−4e*(12/35)−16e² = **.0005203191836734692>0**.
At α=.05:
 n=ceil[2ln(8/.05)/(.013)²]=**60,062 each**;
 N=4n=**240,248 total terminal shots**.
Thus type I≤.049996741 and alternative detection probability≥.950003259 even with any systematic physical errors inside the stated calibration bounds. This is CONDITIONAL and source-specific, not unknown-SPAM self-consistent GST or a hardware feasibility estimate.

## 7. Execution, independent exact replay, negative scientific knowledge

Actually executed main standalone SymPy/NumPy local source TWICE byte-identically:
 /mnt/data/prf14_rot018/prf14_rot018_fifth_context_beacon_quadratic_closure.py
SHA256 c3dc07a152d7e16e03fc6abfcbe24eda2008b7b638353d25b6028d12a1786519.
Native exact JSON (byte-stable):
 /mnt/data/prf14_rot018/prf14_rot018_fifth_context_closure_certificate.json
SHA256 8e44908a422313f834bbac5ad0f3d32c19401d9283ddd921c2e7ef15f2a03364.

An INDEPENDENTLY WRITTEN second within-author exact SymPy script recomputed five-channel Bloch CPTP matrices DIRECTLY using 16 Pauli-label histories (not importing original routines), verified all 45 physical transfer entries, 5×4 beacon Jacobian rank4, and derivative/closure tangent identity:
 /mnt/data/prf14_rot018/prf14_rot018_independent_five_context_kraus_jacobian.py
SHA256 b110cd84b3deb66fff1634866a1b7570ec01fa57768344fefe5d2dcc1aa36afc.

Main model script executed 1,200 null experiments and 1,200 +.1 source-drift experiments as synthetic binomial COUNT draws at n55,695/setting: 0 false rejects, 1200 detections. Independent third standalone physical-control script additionally executed 1,200 null and 1,200 alternative synthetic experiments at n60,062/setting, with randomly perturbed real SO3 gates, Bloch preparations, and legal biased binary POVM effects: 0 false rejects, 1200 detections. Actual source:
 /mnt/data/prf14_rot018/prf14_rot018_robust_physical_calibration_spam_test.py
SHA256 d7909001c28258123318528e385dde5b0167e9e1bff8b56d115d7f57c5c0b353.
Native robust JSON SHA256 8f8a67ba285b624b22da073ec0809657c0ae116eea021e1218d3c2595c918d3a.
Total 4,800 synthetic full-protocol binary-count model trials across both suites, NOT 4,800 hardware experiments and NOT a statistical proof by Monte Carlo. All three Python scripts pass bytecode compilation. Both seeded suites reran with byte-identical output; mathematical 95%-level/power is analytic.

## 8. CRITICAL no-go: passing the new closure cannot self-certify beacon invariance

A fifth measurement adds exactly ONE overidentifying restriction conditional on an invariant source beacon, but matching it is NOT sufficient to identify actual source stationarity.

Construct a DIFFERENT physical target R'=U_X(t)R for rational t=1/1000 (proper X-axis SO3 Cayley rotation, nonzero angle). Independently for each of FIVE contexts define
 C'^q_ij = C_ij [S_q(R)]_ij/[S_q(R')]_ij, i≠j.
All five 16-history distributions p'^q are STRICTLY POSITIVE: exact SymPy-generated minima respectively approximately [.045571775,.045618383,.045701130,.045613342,.045608923]. These five sources are NOT the same as each other. TV from original stationary p by context:
 [.0002384893,.0001428669,.0003577340,.0002717206,.0002767393].
Nevertheless the original stationary (R,C) and alternate nonstationary (R',C'^q) produce EXACTLY the SAME FULL five 3x3 Bloch channel matrices — 45/45 transfer entries, verified by direct Pauli-history CPTP mixture calculation in a second program. Thus ALL ordinary terminal single-qubit preparation and POVM statistics from the same five contexts, not only the four test readings, agree EXACTLY for any n.

The allegedly shared C_(Z,Y) is NOT actually constant in the alternate: derivative d/dt[C'^L_(Z,Y)−C'^I_(Z,Y)] at t=0 is exactly −3/10≠0. For arbitrarily small nonzero t sources remain legal and actual drift arbitrarily weak, but H still equals ZERO because all five observable channel matrices are the same. Passing the quadratic closure is therefore source-consistency, NOT confirmation. Even full five-context channel tomography retains the 3D unknown-gate/context-source gauge if the beacon constraint is removed. A physically independent source monitor, a temporal causal-break tester or additional genuinely controlled cross-context constraints would be required to establish stronger claims; none is asserted here.

The test also misses drifts restricted to OTHER hidden Fourier coordinates and compensating changes satisfying H=0. It is a ONE-SIDED source-model falsifier and must not be marketed as complete process-tensor tomography or universal context-dependence detection.

## 9. Literature and external priority boundary

General detection of context-dependent quantum processor errors via statistical tests is mature: Proctor et al., *Probing Context-Dependent Errors in Quantum Processors*, PRX 9, 021045 (2019), DOI https://doi.org/10.1103/PhysRevX.9.021045. Specific context-aware GST is established in Viñas/Bermudez, npj Quantum Information (2026), DOI https://doi.org/10.1038/s41534-026-01313-z. Roy et al., *Practical Tomography of Multi-Time Processes*, arXiv:2604.01482 (2026), author abstract explicitly explains why deterministic interventions cannot informationally complete characterize arbitrary multi-time quantum processes. Those PRIMARY authors/publisher abstracts were checked, NOT entire proofs. None of these source-type facts supports a generalized ROT018 novelty claim. An exact elementary SO3 row/column closure in this frozen restricted Pauli model is an internal source-conditioned construction. NO_EXTERNAL_NOVELTY.

## 10. Audit requests

REC13/AUD3 independent validators should FIRST check that left post-target P² is correctly distinguished from right pre-target P²; derive H=0 directly from SO3 row/column norms. Then reproduce five physical sixteen-Pauli source probabilities, +.1 qL drift exact TV=.05 and Htrue=27/1225, and independently derive the adaptive threshold type-I and alternative-power margin for four Bernoulli averages. Verify the 55,695 and 60,062 per-setting Hoeffding guarantees and correctly count only FOUR actual settings for H. Confirm nonideal errors through physical SO3/P² telescoping and POVM contraction, rather than multiplying SPAM by cmax. Check the exact 45/45 full-channel alias and infinitesimal −3/10 beacon violation derivative. Finally, test whether any finite-source/physical time-series experiment actually JUSTIFIES the invariant-beacon hypothesis; do not replace falsification failure with model validation.

Parallel B1 PBH/BBN owner work remains separate; no native LINX, Wu-Xu or BlackHawk experiment or physical PBH inference is made by PRF14 in ROT018.

RETURN: PRF14_ROT018 / ORIGINAL_ROT017_SOURCE_DIRECT_REOPEN / KNOWN_LEFT_CLIFFORD_P2_FIFTH_CONTROL / ONE_BEACON_5x4_JACOBIAN_RANK4_ONE_OVERIDENTIFYING_QUADRATIC_CLOSURE_PASS / PHYSICAL_TV0P05_DRIFT_H27_OVER_1225_PASS / 95PC_LEVEL_AND_POWER_IDEAL_222780_SUFFICIENT / PHYSICAL_CALIBRATION_95PC_LEVEL_POWER_240248_SUFFICIENT / 4800_SYNTHETIC_COUNT_EXPERIMENTS_PASS / FIVE_CHANNEL_45_KRAUS_PHYSICAL_ALIAS_PASS / H_ZERO_NOT_SOURCE_VALIDATION / NO_GENERAL_NOVELTY / NO_HARDWARE / NO_CANON / NO_EXEC_SIGN.
