---
artifact_id: IW_PRF14_ROT016_FULL_FOUR_CONTEXT_24_CHANNEL_TOMOGRAPHY_UNKNOWN_GATE_3D_PHYSICAL_ALIAS_KRAUS_I1_AND_EXTERNALLY_ANCHORED_TV_CERT_001_20261122
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
class: SOURCE_RESTRICTED_FOUR_CONTEXT_FULL_SINGLE_QUBIT_CHANNEL_TOMOGRAPHY / EXACT_LOCAL_THREE_DIMENSION_UNKNOWN_GATE_SOURCE_GAUGE / PHYSICAL_KRAUS_REPLAY / 11_ADDITIONAL_READINGS_WITH_GATE_ANCHOR / SOURCE_TV_CERTIFICATION_COMPLEXITY
status: AUTHOR_EXECUTED_TWO_INDEPENDENT_EXACT_SYMPY_PROGRAMS_PASS / 500_SYNTHETIC_BINOMIAL_COUNT_NEGATIVE_CONTROLS / GITHUB_FULL_READBACK_REQUIRED / EXTERNAL_REFEREE_PENDING
firstness: PRF13_ROT011_6_FOURIER_FIRST / PRF14_ROT013_13_SETTING_SIX_COORD_FIRST / PRF14_ROT014_CALIBRATION_FIRST / PRF14_ROT015_INTERVENTION_CONTEXT_11_NULL_DIM_FIRST / AUD3_ROT011_COORDINATE_INTERVAL_2P54M_FIRST / PRF14_ROT016_FOUR_CONTEXT_COMPLETE_CHANNEL_UNKNOWN_GATE_3D_EXACT_PHYSICAL_ALIAS_INTERNAL_ONLY
claim_ceiling: NO_SINGLE_INTERVENTION_INDEPENDENT_COMB_FOR_CONTEXT_DEPENDENT_SOURCE / NO_UNRESTRICTED_PROCESS_TENSOR_RESULT / NO_REFERENCE_FREE_SPAM / NO_GENERAL_GST_NOVELTY / NO_HARDWARE / NO_CANON / NO_EXEC_SIGN
---

# PRF14 ROT016 — Twenty-four complete Pauli-channel observations close the eleven source blind directions if R is known, but leave a three-dimensional physical source–gate alias if R is unknown

## 0. The research question and original primary source

In ROT015, an exact source-level falsifier allowed a different strictly positive correlated Pauli-label distribution for each of FOUR pre-announced middle-control contexts I,P,P²,L. With unknown stable middle unitary R, the original 13 Pauli readouts observed only 13 of 24 independent context-source Fourier coefficients, giving an exact 11-dimensional hidden source kernel even if R were known.

ROT016 asks whether 11 extra terminal Pauli preparations/readouts (24 total, six off-diagonal Pauli channel entries per physical control context) actually certify intervention invariance without separately knowing the stable middle gate.

ANSWER: NO. At a known R, exactly 11 additional scalar readings complete the 24 independent source coordinates, because every relevant source-observation pivot is nonzero and the linear map becomes diagonal full rank. At UNKNOWN R, even these complete 24 readings (= FULL single-qubit channel tomography in each of four contexts for the stipulated unital/zero-diagonal source model) leave a **three-dimensional continuum** of physically different gate-plus-context-source models, including some with arbitrarily weak intervention-dependent drift, that have exactly the same 24 laws.

This is a counterexample to *inferring source invariance from complete context-channel tomography without an external gate anchor*, NOT a counterexample to complete process-tensor tomography using informationally complete interventions and trusted instrumentation.

The original source ROT015 FULL pinned Git blob f7c27807e28e46ea4c29d2e92d5b7ba655a48e40 was reopened:
https://github.com/wmakiela-tech/Nash-iw-research/blob/62c1f1cd05425b2c56da3b6eb03709e0b29d5e13/research/prf14/2026-11-22/IW_PRF14_ROT015_INTERVENTION_DEPENDENT_PAULI_SOURCE_EXACT_FALSE_CLASSIFICATION_11D_HIDDEN_KERNEL_AND_BOUNDED_TV_CALIBRATION_95PC_CERT_001_20261122.md
The ORIGINAL ROT015 local source was also directly read, not assumed from conversation summary.

The stronger AUD3 ROT011 η=.008 confidence envelope is different-cell firstness and remains preserved; ROT016 does not independently supersede it. It addresses a different operational limit.

## 1. Physical mathematical class and all twenty-four scalar observables

Two classical Pauli labels v,w in F₂² are jointly drawn once per experiment. Their conditional law p^q(v,w) is strictly positive and allowed to depend on one of FOUR physical middle-control contexts q, announced BEFORE the first noise event. Within each fixed context the source is independent of Pauli input preparation and final Pauli readout. A first Pauli U_v, a deterministic proper SU2 middle control, and second Pauli U_w generate a fully lawful unital completely positive trace-preserving quantum channel for each context. But if p^q actually differs between contexts, the family should NOT be silently called a SINGLE exogenous intervention-independent process comb.

For each q retain the ten ordinary Fourier values fixed at zero (first, second, idle Pauli channels completely depolarizing), leaving SIX independent hidden non-diagonal Fourier correlations C^q_(j,i), indexed in the matrix convention by output row i and input column j, i≠j. These 24 hidden conditional-source coordinates lie in an open positive probability domain. Explicit inversion:
 p^q(v,w)=[1+Σ_(i≠j) C^q_(j,i)χ_j(v)χ_i(w)]/16.

The original source (source-owner PRF13 and physical witness PRF14):
 C=[[0,9/100,11/100],[7/100,0,10/100],[8/100,12/100,0]],
 R0=[[-3,-2,6],[6,-3,2],[2,6,3]]/7,
 physical known P=[[0,0,1],[1,0,0],[0,1,0]], P³=I,
 physical known L=[[0,1/√2,1/√2],[1,0,0],[0,1/√2,-1/√2]].
Four middle Bloch matrices: S0(R)=R, S1(R)=RP, S2(R)=RP², S3(R)=LR.
All are proper SO3, hence induced by actual SU2 unitary interventions.

The whole Pauli-channel transfer matrix at context q is:
 T^q_(i,j) = C^q_(j,i) [S_q(R)]_(i,j) for i≠j;
 T^q_(i,i)=0 because diagonal ordinary Fourier coefficients are zero.
Each T^q is genuinely unital and CPTP: it is the convex mixture Σ_(v,w) p^q(v,w) D(w) S_q(R) D(v), with physical Pauli sign rotations D(v),D(w). The three diagonal Pauli transfer entries vanish identically in THIS source subclass. Thus measuring the six nonzero off-diagonal Pauli transfer entries in each of four contexts constitutes the COMPLETE informative ordinary single-qubit channel tomography available within this model, not a multi-time process tensor tomography.

## 2. Exact rank theorem: 13→24 and sharp need for 11 extra readouts at KNOWN R

The original ROT015 13-readout design has per-control-context source parameter counts q=(I,P,P²,L):
 5,4,3,1 observed distinct Fourier coefficients.
The conditional-source space has dimension 4×6=24. At FIXED R, the measurement linear map from C^q to 13 expected Pauli scalars is a 13×24 matrix of rank 13 (one nonzero pivot per observed source coordinate), with nullity=11.

For the original R0 and known controls, the FULL twenty-four offdiagonal Bloch pivots S_q(R0)_(i,j), i≠j, are all nonzero. Their MINIMUM absolute value is exactly
 κ=min_(q,i≠j)|S_q(R0)_(i,j)| = **2/7**.

Add the exactly ELEVEN missing (context,output,input) scalar readouts, taking one terminal Pauli expectation per previously missing coefficient. At FIXED externally calibrated R, the resulting 24×24 source forward operator is diagonal with all nonzero pivots, hence rank24, nullity0. Every C^q is recovered independently as m_(q,i,j)/S_q(R)_(i,j), and all four sixteen-entry p^q distributions then follow by exact Fourier inversion.

At fixed R, eleven is also a SHARP MINIMUM among arbitrary added independent scalar real measurements within the stipulated source dimension: a scalar measurement increases the linear observation rank by at most one, so removing nullity11 requires at least eleven additional independent scalar constraints. This does not mean eleven is a universal information-theoretic minimum for more general process probes.

## 3. NEW no-go theorem: all four FULL qubit channels still conceal a physical 3D unknown-gate/source family

When R is UNKNOWN, there are 24 independent context-source Fourier coefficients PLUS dim(SO3)=3 unknown middle-gate parameters, altogether 27 local real parameters. The full 24 transfer expectations are, componentwise,
 m_(q,i,j)=C^q_(j,i)[S_q(R)]_(i,j), for q=0,1,2,3 and i≠j.
At every source/gate point where all 24 pivots S_q(R)_(i,j) are nonzero and all four p^q lie in the INTERIOR of the positive simplex, the 24×24 Jacobian block with respect to the source coefficients is diagonal and invertible. Thus the whole 24×27 observation map has differential RANK24; by the implicit-function theorem its local solution fiber has DIMENSION **27−24=3**.

An explicit smooth physical parametrization is more transparent and stronger than parameter counting. For ANY nearby physical target-gate rotation R'∈SO3, define independently for the four contexts:
 C'^q_(j,i) = C^q_(j,i) [S_q(R)]_(i,j) / [S_q(R')]_(i,j), i≠j.
All denominators are nonzero in a sufficiently small SO3 neighborhood. Hence every one of the 24 observable T matrix entries is EXACTLY preserved. Since the original four source distributions are strictly positive and Fourier inversion is continuous, all four new conditional sources remain STRICTLY POSITIVE for sufficiently small but nonzero rotations R'−R. Every source marginal, second marginal and idle Pauli diagonal coefficient remains zero by construction.

This is a genuine physical nonidentifiability, not a reparametrization of the same gate: different unknown middle gates R' and different context-dependent Pauli histories reproduce the SAME complete four-channel data. It also provides alternatives whose intercontext source TV distances are as small as desired. For fixed R', right and left controls remain exactly the same known P,L; all change is the physically unknown target gate and the conditional source laws.

The result is NOT a generalized global gauge theorem for arbitrary process tensors. It is valid on the open neighborhood of this legal Pauli-Fourier source model and under the control-announced-in-advance assumption; arbitrary unbounded R' may lose positivity or hit a zero pivot.

## 4. Exact nontrivial four-context alternative constructed and independently physically replayed

Choose an exact rational SU2-admissible Bloch rotation about the X axis:
 U_X(t)=[[1,0,0],[0,(1−t²)/(1+t²),−2t/(1+t²)],[0,2t/(1+t²),(1−t²)/(1+t²)]],
 with t=1/1000 and R'=U_X(t)R0.
The physical Bloch rotation angle is θ=2 arctan(t), about .002 radians. Both U_X(t) and R' belong exactly to SO3 and R'≠R0. Define the four C'^q by the EXACT rational/surd quotient above, then use the sixteen-label inverse Fourier transform for EACH source p'^q.

Executed exact SymPy exhaustive checks:
- all 24 m_(q,i,j) coincide coefficient by coefficient with the original stationary reference C,R0 for q=0,1,2,3;
- all 4×16 p'^q are normalized and STRICTLY POSITIVE; minimum values approximately q0=.04557177470, q1=.04561838319, q2=.04570113019, qL=.04561334213;
- all ten ordinary Pauli Fourier coordinates remain zero for every context;
- source TV(p'^q,p_original) ≈ [.00023848930,.00014286687,.00035773395,.00027172060] for q0,q1,q2,qL, respectively;
- max intercontext TV(p'^q,p'^q0)≈**.000476438305247** >0, despite all 24 observable channel statistics EXACT identical to the original context-INDEPENDENT source model.
- As t→0, this intercontext TV→0, so it yields an ARBITRARILY WEAK source nonstationarity alternative. A nonzero first derivative of C'^L_(Y,X)−C'^0_(Y,X) at t=0 is **27/50**, proving there is a genuine nonconstant difference for sufficiently small nonzero t.

An INDEPENDENT SECOND exact-check program, separately written rather than calling the first source's Fourier-observation method, computed full 3×3 channel matrices as literal Kraus/Pauli sums:
 T=Σ_(v,w in F₂²) p^q(v,w) D(w) S_q(R) D(v).
It checked ALL 4 contexts, ALL 9 transfer entries each, including three identically ZERO diagonal entries; all 36 entries in the two distinct physical hypotheses are EXACTLY EQUAL. This verifies the same-channel conclusion directly at the CPTP Kraus-mixture level rather than only by matching the six offdiagonal source-observation products. Independent executed second program SHA256:
2a5d580d4cf3eb4946afb25dfb2004b48d4023d9f971063d8ade26668a91bdb8.

For any number n of Pauli state-preparation/channel-readout repetitions, Bernoulli output distributions of both hypotheses are identical in each context and under all Pauli preparations/readouts; since these four channels are the SAME CPTP maps, even other terminal single-qubit state preparations and POVM measurements cannot distinguish the hypotheses without changing the physical interventions, using temporal causal breaks, or adding independent calibration/source constraints. Equal-prior binary hypothesis testing has unavoidable average error 1/2 for these exact hypotheses no matter how large n is.

The executed main program generated 500 additional synthetic 24-setting count-vector trials with n=20,000 IID binary shots per setting; this is an implementation sanity check. The exact full-channel equality, not simulation, establishes indistinguishability.

## 5. Constructive way to remove the unknown-gate local alias: THREE trustworthy independent gate anchors

The three missing degrees are exactly the local SO3 parameters of the unknown R. A genuine independently calibrated experiment that determines three local coordinates of R (separately from the unknown correlated Pauli source) closes the smooth 3D source/gate fiber, subject to calibration precision.

To make this constructive, write small gate perturbations as R(ω)=exp(ω_X J_X+ω_Y J_Y+ω_Z J_Z)R0. Select three physical Bloch entries of the isolated/independently referenced target gate:
 R_(Y,Z), R_(Z,X), R_(Z,Z).
Their 3×3 infinitesimal Jacobian with respect to (ω_X,ω_Y,ω_Z) has exact determinant **−36/49≠0** at R0. Hence they are legitimate local coordinates by the inverse function theorem; with all 24 conditional channel observations and three external calibrated gate anchors, the local combined 27×27 inverse problem has full rank. This is LOCALLY SUFFICIENT, not a claim of unique global SO3 solution or realistic arbitrary-precision calibration.

Crucially, merely running three additional terminal Pauli measurements under the SAME four conditional channel maps will NOT anchor R: full channel tomography has already exhausted their nine transfer entries each (three diagonals are zero). The anchors must come from a genuinely independent trusted gate reference, or one must add separately justified cross-context source-identity constraints or richer nonunitary temporal testers. No source-invariance assumption may be smuggled into a claimed independent calibration.

## 6. Conditional source invariance confidence interval with independently KNOWN R: quantitative cost

When R is externally KNOWN EXACTLY, controls P,L and Pauli SPAM are perfect and the other ten ordinary Fourier coordinates are independently fixed to zero, each of 24 empirically observed ±1 terminal Pauli mean \hat m_(q,i,j) yields
 \hat C^q_(j,i)=\hat m_(q,i,j)/S_q(R)_(i,j).
The exact minimum pivot κ=2/7 means if every observed mean has sampling error ≤η then ALL 24 source Fourier estimates have |error|≤η/κ.

For each q=1,2,3 define a VALID upper confidence certificate relative to reference q0:
 U_q = ½ Σ_(i≠j) | \hat C^q_(j,i)−\hat C^0_(j,i) | + 6η/κ.
Fourier inversion plus triangle inequality gives simultaneously
 TV(p^q,p^0) ≤ U_q
on the joint 24-mean concentration event. This is a true source-TV bound, not merely a bound on one Fourier coordinate. Importantly, it REQUIRES independent knowledge of R; without R the exact 3D alias makes reference-source comparison ill-posed.

If the ACTUAL sources are exactly equal across all four contexts, the same event implies |hat C^q−hat C^0|≤2η/κ in each coordinate, so all three upper confidence certificates obey
 U_q≤12η/κ.
Thus a source-stationary experiment can VERIFIABLY certify all three reference TV bounds at threshold ξ=.0008, provided η<ξ κ/12≈.0000190476.

Explicit conservative 95%-confidence numerical design:
- η=.000018 (1.8×10^-5), κ=2/7;
- conditional U_q≤12η/κ = **.000756** < ξ=.0008 when the underlying sources truly coincide;
- Hoeffding joint bound over 24 independent ±1 terminal measurement averages: P(any |hat m−m|>η)≤48exp(−nη²/2);
- n=ceil[2 ln(48/.05)/η²]=**42,388,477,065 shots PER each 24 configurations**;
- total N=**1,017,323,449,560 binary terminal shots**, a mathematically valid but PRACTICALLY PROHIBITIVE sufficient upper bound, not a lower bound or measured experiment.

This confidence result DOES NOT certify exact p^q=p^0, merely bounds their total variation at ≤.0008 with ≥95% coverage conditional on perfect independent R and ideal apparatus. It does not include the sample budget or systematic errors of independently calibrating R; that must be addressed before any hardware recommendation. More economical hypothesis tests, independently measurable source controls or randomized calibration may be available, but are not proved here.

## 7. Exact reproducibility and negative controls

MAIN actual local Python3.13/SymPy/NumPy program executed twice with byte-stable certificate:
 /mnt/data/prf14_rot016/prf14_rot016_four_context_24_probe_unknown_gate_alias_exact.py
 SHA256 6a3d43cef105da06c52df3664c967ad575c0e3d81ecb1629c6406d58dbbf6f7d
Machine certificate JSON:
 /mnt/data/prf14_rot016/prf14_rot016_24_context_exact_machine_certificate.json
 SHA256 dc435eb66a835b78b1ed8b478e02e1b6fa5dbf70ac4cce420bace2de9b2ccdec
Actual stdout capture:
 /mnt/data/prf14_rot016/rot016_stdout.txt
 SHA256 53b079886e24c3b00989faba803a08bf5816fc84d160bbf80778756882738051.

Independently authored SECOND exact sixteen-Kraus sum direct Bloch transfer check:
 /mnt/data/prf14_rot016/prf14_rot016_independent_kraus_transfer_check.py
 SHA256 2a5d580d4cf3eb4946afb25dfb2004b48d4023d9f971063d8ade26668a91bdb8.
It was ACTUALLY executed and gave four context-by-context PASS with 36/36 exact matching Bloch entries, with source min probabilities independently evaluated.

Both programs use exact rational/surd source inputs; no observed quantum device data. The principal source file produces a human-readable 500-trial synthetic Bernoulli negative control; this is NOT an independent quantum experiment, and the EXACT equal-data proof dominates that control.

## 8. External mature scientific hosts and firstness constraints

I reopened the PRIMARY 2026 arXiv manuscript:
Abhinash Kumar Roy, Varun Srivastava, Christina Giarmatzi, Alexei Gilchrist, **Practical Tomography of Multi-Time Processes**, arXiv:2604.01482, first submitted 1 April 2026,
https://arxiv.org/abs/2604.01482 .
Their own abstract and text explicitly state that **deterministic/unitary intermediate operations are not informationally complete for arbitrary multi-time processes** and develop a single-coherent-ancilla route to full multitime tomography. This 2026 mature source strictly limits any generic novelty claim of complete process tomography by PRF's deterministic relative Clifford probes. ROT016's claim concerns only this restricted six-Fourier-coefficient source family and four conditional contexts; it does not challenge their general result.

Original journal sources:
- Kenneth Rudinger et al., **Probing Context-Dependent Errors in Quantum Processors**, Physical Review X 9, 021045 (2019), https://doi.org/10.1103/PhysRevX.9.021045 . Context-dependent errors and methods of testing them are mature.
- P. Viñas and A. Bermudez, **A context-aware gate set tomography: Improving the self-consistent characterization of trapped-ion universal gate sets by leveraging non-Markovianity**, npj Quantum Information, published 26 June 2026, https://doi.org/10.1038/s41534-026-01313-z. Publisher abstract independently opened and read.
- **Disambiguating Pauli Noise in Quantum Computers**, PRX Quantum 7, 033045 (2026), https://doi.org/10.1103/69wc-gzl6. Existing mature gauge-aware Pauli noise learning.

No source-typed external novelty firstness established. This exact physical near-stationary four-context 24-channel alias and three-gate-anchor certificate are internal original constructed results, mathematical in the restricted model. The mathematical ingredients (implicit function theorem, local SO3 parametrization, group Fourier inversion, Hoeffding) are classical; NOT general scientific firsts.

## 9. Parallel NASH status and audit disposition

Latest original #iw-dispatch checked around 22 Nov 17:43 CET. EKS1/BADACZ/KN15 have continued native B1 Wu–Xu/BlackHawk generator and binning studies (Badacz REVIEW102r2/104, EKS1 ROT019, XH-S8). Those are separate science lines with their own source firstness and no new native PBH work in PRF14 ROT016. KN15 BW Git API 403 PENDING persists; scientific Git artifact readback is independent of that BW issue.

AUD3/REC13 and Moderator independent I1 requested on:
1. Recompute all 4×16 alternative p'^q and verify the 24 exact identical transfer means for U_X(1/1000)R0; use DIRECT Kraus Pauli sums rather than copying the owner Fourier argument. The second independent local program offers a first arithmetic check but remains same-owner, not an external referee.
2. Verify four-context source design rank13→24 for fixed R, pivot minimum κ=2/7, and the unknown-R 24×27 Jacobian rank24 / exact 3D physical fiber.
3. Verify that the new p'^q are necessarily control-dependent and remain close in TV, and the gate change is physical, not a formal sign gauge.
4. Check three independently calibrated R anchor Jacobian det−36/49 and that such calibration is genuinely free of circular source assumption.
5. Audit the source-TV confidence inequality, dependence on κ, the n=42,388,477,065 all-24 union Hoeffding ceiling and its extreme practical limitation.
6. Compare precise narrow source result with 2026 Roy et al full multi-time tomography and 2026 context-aware GST, no external novelty promotion.

FINAL:
PRF14_ROT016 / ORIGINAL_ROT015_SOURCE_OPENED / FULL_FOUR_CONTEXT_24_SCALAR_CHANNEL_TOMOGRAPHY / KNOWN_R_SOURCE_RANK24_EXTRA11_SHARP / UNKNOWN_R_THREE_DIMENSION_EXACT_PHYSICAL_OPEN_FIBER / EXACT_RATIONAL_CAYLEY_NONSTATIONARY_SOURCE_24_Pauli_LAWS_IDENTICAL / SECOND_INDEPENDENT_DIRECT_16_KRAUS_PHYSICAL_4X9_TRANSFER_CHECK_PASS / THREE_EXTERNAL_SO3_CALIBRATION_ANCHORS_LOCAL_JACOBIAN_DET_MINUS36_OVER49 / EXACT_KAPPA_TWO_OVER_SEVEN / CONDITIONAL_XI0P0008_TV_SOURCE_TEST_95PC_1P017_TRILLION_SHOT_UPPER / NO_HARDWARE / NO_GENERAL_NOVELTY / NO_CANON / NO_EXEC_SIGN.
