---
artifact_id: IW_PRF14_ROT017_ONE_FOURIER_BEACON_24_CONTEXT_CHANNEL_LOCAL_SO3_ANCHOR_GLOBAL_POSITIVE_BRANCH_CLASSIFICATION_AND_UNTESTABLE_ANCHOR_NO_GO_001_20261122
date: 2026-11-22 Europe/Warsaw
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
exposure: PUBLIC
scientific_class: SOURCE_RESTRICTED_FOUR_CONTEXT_SINGLE_QUBIT_Pauli_CHANNEL / ONE_CONTEXT_INVARIANT_FOURIER_BEACON / SIX_EXACT_LOCAL_GATE_JACOBIANS / FOUR_GLOBAL_ALGEBRAIC_BRANCHES / PHYSICAL_PROBABILITY_FILTER / TWO_POSITIVE_ALIAS_KRAUS / SATURATED_ANCHOR_UNTESTABILITY
status: ORIGINAL_ROT016_REPORT_REOPENED / AUTHOR_EXACT_SYMPY_6_BEACONS_TIMES_4_ALGEBRAIC_BRANCHES_PASS / SECOND_INDEPENDENT_16_KRAUS_4X9_PASS / DOUBLE_COLD_LOCAL_EXECUTION_PASS / EXTERNAL_REFEREE_PENDING
firstness: PRF13_ROT011_6D_HIDDEN_FOURIER_FIRST / PRF14_ROT013_13_SETTING_UNKNOWN_GATE_FIRST / PRF14_ROT015_CONTROL_DEPENDENT_SOURCE_11D_FIRST / PRF14_ROT016_FULL_24_CHANNEL_3D_ALIAS_FIRST / PRF14_ROT017_ONE_BEACON_LOCAL_IDENTIFIABILITY_AND_GLOBAL_PHYSICAL_BRANCH_CLASSIFICATION_INTERNAL_ONLY
claim_ceiling: NO_UNRESTRICTED_PROCESS_TENSOR / NO_NO_CALIBRATION_SPAM_CLAIM / NO_BEACON_VALIDATION_FROM_SAME_CHANNEL_DATA / NO_FINITE_SHOT_CONFIDENCE_CERT_FOR_NEW_ONE_BEACON_ESTIMATOR / NO_EXTERNAL_NOVELTY / NO_HARDWARE / NO_CANON / NO_EXEC_SIGN
---

# PRF14 ROT017 — A single control-invariant source Fourier coordinate locally anchors an unknown SO(3) gate; positivity yields source-specific global uniqueness for two choices, but the anchor itself is untestable from the same four channels

## 0. Scientific question, motivation and controlling original

ROT016 PROVED that complete ordinary single-qubit channel tomography in four middle-control contexts (six nonzero transfer coefficients each, 24 scalar means) does NOT identify the unknown middle SU2 gate or the 24 context-conditioned classical Pauli-source Fourier coefficients. The 24-observable / 27-unknown inverse has an exact 3-dimensional physical local fiber; even arbitrarily small, genuinely context-dependent sources can replicate the complete four-channel data from a stationary source. The previously recommended solution required THREE EXTERNALLY measured gate parameters.

ROT017 asks whether a WEAKER and potentially source-side scientific assumption can replace three gate anchors: suppose exactly ONE nonzero source Fourier correlation, but NOT the other five in each context, remains invariant under all four known control contexts. Can this ONE 'beacon' close the 3D gate fiber, does it ensure GLOBAL physical uniqueness, and can the experiment self-certify the beacon assumption?

Answer with exact source evidence:
(A) All SIX possible nonzero source Fourier coordinates independently serve as LOCAL single-beacon SO3 gate anchors at the frozen PRF14 witness (six nonzero exact 4x4 Jacobian determinants).
(B) At the exact 24-channel dataset, exactly FOUR algebraic gate/source branches exist for EACH chosen beacon. Fourier positivity filters these to ONE physically legal branch for the two beacons with OUTPUT Y (C_(X,Y), C_(Z,Y)), and TWO legal branches for the other four beacons. Therefore some individual beacons give GLOBAL unique exact reconstruction in THIS witness, but not every beacon does.
(C) A SECOND beacon in the SAME output row does NOT necessarily resolve the global ambiguity: two genuinely distinct physical source/gate models with the entire OUTPUT X row of Fourier coefficients invariant across the four contexts produce exactly the SAME all-four full CPTP channels. A second beacon in a different output row can separate these two candidate branches IF independently justified as invariant.
(D) Local inverse-map parameter counting itself is a WARNING: one four-context beacon imposes precisely 3 constraints, reducing 27 unknowns to exactly the same 24 as the measured full-channel parameters; the model is locally SATURATED and has no goodness-of-fit residual. Infinitesimally small beacon VIOLATIONS can be exactly hidden by the original ROT016 source/gate family. Thus neither 24 channels nor arbitrarily many repeat shots validate the beacon premise. Source-invariance is a MODEL input, not an observational conclusion.

This is a source-specific mathematical calibration design and exact nonidentification result, not general quantum process tensor/GST novelty. Unlike the previous PRF14 statistical rotations, ROT017 intentionally DOES NOT invent an unproved new finite-shot confidence resource for this nonlinear globally constrained estimator.

Primary source ROT016 ACTUALLY REOPENED by GitHub immutable blob c0427b20c0e13f0ae84806042f2b9ad9b0c299f3, plus local original executed source and output:
https://github.com/wmakiela-tech/Nash-iw-research/blob/5e2d97d73851421ebb388d9752a8f572d41027ca/research/prf14/2026-11-22/IW_PRF14_ROT016_FULL_FOUR_CONTEXT_24_CHANNEL_TOMOGRAPHY_UNKNOWN_GATE_3D_PHYSICAL_ALIAS_KRAUS_I1_AND_EXTERNALLY_ANCHORED_TV_CERT_001_20261122.md
PRF13 ROT011 retains firstness for the full 6-dimensional hidden classical Pauli memory Fourier source. The exact 4-world construction and control-P gate-relative design developed in PRF14 ROT010–016 retain their owner sequence.

## 1. Precise physical 4-context model

Fix two classical Pauli-label errors (v,w)∈F2²×F2²; conditionally on preannounced control-context q, choose one STRICTLY POSITIVE normalized 16-component source p^q(v,w), stable across Pauli state preparations and final readouts and across IID repetitions. Apply first Pauli U_v, physical chosen single-qubit middle unitary S_q(R), second Pauli U_w, and read the final Pauli ±1 response.

The source is permitted to depend on q, announced BEFORE the first noise event. Thus each experimental channel is causal/CPTP, but in general the four processes are NOT one intervention-independent exogenous comb. All ten ordinary Fourier coordinates are fixed to zero for every context; six independent hidden offdiagonal C^q_(j,i), i≠j, remain. Fourier inversion is
 p^q(v,w)=1/16[1+Σ_(i≠j) C^q_(j,i) χ_j(v)χ_i(w)].
The full single-qubit Bloch transfer matrix is unital, diagonal elements zero, and for i≠j:
 T^q_(i,j)=C^q_(j,i)[S_q(R)]_(i,j).
It is literally a mixture of sixteen physical U_w S_q U_v histories, and all 16 probabilities must remain nonnegative; the present witness uses STRICTLY POSITIVE ones.

Baseline target proper SO3 R:
 R0=(1/7)[[-3,-2,6],[6,-3,2],[2,6,3]].
Known proper SO3 right-pre Clifford P:
 P=[[0,0,1],[1,0,0],[0,1,0]], P³=I.
Known proper SO3 post-target left control:
 L=[[0,1/sqrt2,1/sqrt2],[1,0,0],[0,1/sqrt2,-1/sqrt2]].
The four contexts are S_q(R)=(R, RP, RP², LR). Every one of 24 offdiagonal entries [S_q(R0)]_ij is nonzero (min absolute pivot κ=2/7); all 24 measured means are nonzero.

Baseline source held equal across q only as the data-generating REFERENCE (not as an estimator promise):
 C^0=[[0,9/100,11/100],[7/100,0,10/100],[8/100,12/100,0]]
with entries indexed by output row i,input column j. All six source C values are unequal rowwise and independent within an open six-dimensional source family; 16 original probabilities p(v,w) have min73/1600, max157/1600, sum1. This is NOT the row-flat restriction used in the unrelated ROT012 shortcut.

## 2. Definition of the one-beacon promise and first LOCAL theorem

Choose one nonzero offdiagonal pair (i,j), i!=j, called the 'beacon'. Promise ONE and only ONE cross-context source equality:
 C^0_(j,i)=C^1_(j,i)=C^2_(j,i)=C^L_(j,i)=c≠0.
All other 20 context-source coefficients are free and independent; no other source stationarity, joint-source common history, or calibrated unknown target R is assumed.

Four exact observed Pauli expectations for this SAME input j/output i under four controls then are
 y_q=c [S_q(R)]_(i,j), q∈{I,P,P²,L}.
Let R(ω)=exp(ω_X J_X+ω_Y J_Y+ω_Z J_Z)R0. The 4×4 Jacobian H_(i,j) of the four y_q with respect to (c,ω_X,ω_Y,ω_Z) is
 H_(q,0)=[S_q(R0)]_(i,j);
 H_(q,k)=c [S_q(J_k R0)]_(i,j), k∈{X,Y,Z},
where J_k are the standard SO3 generators acting on R from the LEFT. This is a directly physical local gate orientation parametrization, not a free unconstrained 3x3 matrix.

ACTUALLY calculated EXACT SymPy rational/surd determinants (output row, input column) in this original source:

| Beacon C_(input,output) | exact det H_(i,j) | physically valid global branches |
|:--|:--|--:|
| C_(Y,X) | −6561sqrt2/14,000,000 | 2 |
| C_(Z,X) | −1331sqrt2/14,000,000 | 2 |
| C_(X,Y) | +49/500,000 | 1 |
| C_(Z,Y) | +3/7,000 | 1 |
| C_(X,Z) | −12sqrt2/109,375 | 2 |
| C_(Y,Z) | −27sqrt2/109,375 | 2 |

ALL SIX Jacobians are nonzero: the pair (one unknown c, three unknown SO3 parameters) is locally identifiable from just these FOUR scalar beacon expectations. The remaining 20 nonbeacon source parameters enter the other 20 observables with nonzero independent pivots. Thus the full 24-data / 24-model-parameter source+gate Jacobian is invertible (after permutation of coordinates, a 20×20 nonzero diagonal source block and the above 4×4 beacon block). This explicitly closes the former 3D local ROT016 fiber.

Numerical SVD used ONLY as an exploratory conditioning diagnostic, not a rigorous interval-based statistical confidence theorem: in the two exactly globally unique source-beacon choices, H for C_(Z,Y)=.10 has smallest singular value≈0.0317139016 and condition≈41.54, while C_(X,Y)=.07 has smallest singular value≈0.0143204737 and condition≈75.99. Thus the C_(Z,Y) beacon is better locally conditioned in this frozen source among the two global-unique choices; no global optimality claim.

## 3. Complete GLOBAL exact enumeration, not mere local Jacobian evidence

The three RIGHT controls P^0,P^1,P² cycle an individual output row across all three input coordinates, so equality of their three beacon means forces
 c' r'_i = c r_i
as full 3-vectors. Orthogonality ||r_i||=1 gives c'=±|c| and r'_i=±r_i, linked by the product. For each sign one row of SO3 is fixed; the remaining two rows can be rotated by one angle φ. Parameterize that remaining one-dimensional subgroup by t=tan(φ/2), including the φ=π point t=∞. The single LEFT beacon measurement is a trigonometric equation, reducible after the tangent-half-angle substitution to a polynomial of degree≤2. At this exact physical witness each sign gives exactly TWO solutions (including infinity where appropriate), so there are exactly FOUR algebraic complete-channel gate/source candidates per beacon.

For each candidate R', the full 24 measured channel entries fix all four complete source matrices uniquely:
 C'^q_(j,i)=C_(j,i)[S_q(R0)]_(i,j)/[S_q(R')]_(i,j), i≠j.
Every candidate's six-by-four Fourier coefficients were inverted to EACH of 4×16 probabilities and tested EXACTLY for strict physical positivity. A separate 16-history Pauli Kraus sum confirmed all 4×9 complete channel transfer entries in each legal constructed alias.

Source-specific GLOBAL branch counts, not merely linearized rank:
 C_(Y,X): two positive sources/gates; C_(Z,X): two;
 C_(X,Y): ONE; C_(Z,Y): ONE;
 C_(X,Z): two; C_(Y,Z): two.
These counts exhaust ALL algebraic candidates from the physical SO3 row geometry for the exact 24-observation baseline data, provided the one beacon is indeed context-invariant and every conditional source retains its 10 ordinary Fourier zeros. They do NOT imply the same result for any arbitrary source, gate, or different controls.

Example: beacon C_(Z,Y)=1/10 (output Y/input Z). The exact half-angle roots:
- c' positive: t=0 (physical original), t=1/2 (NOT physical; p^P minimum = −49/832).
- c' negative: t=2 (NOT physical; p^P minimum = −49/832), t=∞ (NOT physical; p^L minimum = −9/1600).
The ONLY branch with all 4×16 nonnegative probabilities is the original R0 and its baseline four source distributions. This is a FULL source-specific exact global physicality filter, not an assumption that formal signed Fourier distributions are valid sources. Equivalent global-uniqueness holds for the other output-Y beacon C_(X,Y), but with weaker local conditioning.

## 4. NEW exact negative: even TWO invariant beacons in the same output row can leave two physical models

For the beacon C_(Y,X)=9/100, exact enumeration leaves TWO genuine physically legal target-gate/source candidates with all FOUR complete channel transfer matrices equal, even after the single-beacon promise. One is the baseline R0 with the same C source in all four controls. The other gate is the proper rotation
 R_alt=(1/7)[[3,2,-6],[-2,-6,-3],[-6,3,-2]],
which is NOT equal to R0.

The alternate FOUR context-specific Fourier source matrices are, by rows (output i,input j):

q0:
[[0,-9/100,-11/100],[-21/100,0,-1/15],[-2/75,6/25,0]].

q1:
[[0,-9/100,-11/100],[7/200,0,-3/10],[4/25,-9/50,0]].

q2:
[[0,-9/100,-11/100],[-7/150,0,1/20],[-3/25,-1/25,0]].

qL:
[[0,-9/100,-11/100],[-7/100,0,-1/10],[2/25,3/25,0]].

Each of FOUR 16-entry joint-source distributions is strictly positive, with minima
 q0 143/4800; q1 3/128; q2 193/4800; qL 73/1600,
all exactly normalized with completely depolarizing first/second/idle channels. The maximum source variation relative to the alternate q0 distribution is TV=77/320=.240625; other q2 TV=91/600≈.151667 and qL=11/120≈.091667. The two models produce exactly the same FOUR full 3×3 physical CPTP Bloch channel matrices (all 36 entries), verified by independently coded direct sixteen-Pauli-history Kraus sums.

Crucial point: the alternative keeps BOTH output-X hidden source coordinates fixed across ALL FOUR contexts:
 C^q_(Y,X)≡−9/100 and C^q_(Z,X)≡−11/100.
Thus TWO beacon invariances in the SAME output row do not globally identify the gate or source in this physical witness. Two source promises need to be geometrically independent, not just numerically distinct.

A conditional second equality from a DIFFERENT output row would separate this exact pair. E.g. if C^0_(X,Y)=C^1_(X,Y) also held, then the alternate has
 C^0_alt,(X,Y)=−21/100 while C^1_alt,(X,Y)=+7/200,
giving exact discrepancy −49/200=−.245. This excludes the alternate under that ADDITIONAL INVARIANCE PROMISE, but such a promise must itself be justified independently; it is NOT validated solely because one branch is excluded mathematically.

## 5. The fundamental caveat: locally saturated self-calibration cannot validate its own beacon assumption

Before imposing a beacon, the model contains 24 source coefficients plus 3 SO3 gate coordinates=27 local unknown real parameters and 24 measured full-channel means. ONE beacon common across 4 contexts adds 3 independent source-equality constraints. Hence model dimension becomes 24=number of observed scalar channel means.

At the witness, the complete 24×24 Jacobian is NONSINGULAR by §2. The inverse-function theorem states the fixed-beacon model's data image contains an OPEN NEIGHBORHOOD of the observed 24-dimensional data: every sufficiently small perturbation of the four measured channels can be explained by some locally unique model SATISFYING the beacon, even if the true process in fact has a slightly context-dependent beacon. There is no local overidentification residual or model specification test in those same four channels.

More strongly, ROT016's fully physical alternative construction supplies EXACT same 24 complete channels with a DIFFERENT gate and control-dependent source:
 R'(t)=U_X(t)R0, with U_X(t) physical rational X rotation and t arbitrarily small nonzero;
 C'^q_(j,i)=C_(j,i)[S_q(R0)]_(i,j)/[S_q(R'(t))]_(i,j).
Every 16-entry source p'^q stays strictly positive for sufficiently small |t|, and all four full channel matrices are exactly identical to the baseline, while source beacon C_(Z,Y) ceases to be invariant. The explicit derivative at zero is
 d/dt [C'^L_(Z,Y)−C'^I_(Z,Y)]|_(t=0)=**−3/10≠0**.
Therefore arbitrarily weak nonzero violations of the crucial beacon assumption yield EXACT the same 24-channel probability laws (not just an approximation). No number of repetitions, even n→∞, distinguishes the true stationary beacon from these unanchored alternatives using the four channels alone.

This is a structural anti-self-sealing guard: a sufficient identifiability premise is NOT thereby identified or verified by the data to which it is applied. The original source's 16-label classical histories might be monitored using a genuinely independent physical signal, or a fifth well-characterized intervention/correlation bridge could provide new constraints; neither was implemented or certified in this turn.

In particular, GLOBAL uniqueness for the C_(Z,Y) beacon is CONDITIONAL ON THAT BEACON BEING TRULY INVARIANT. It is NOT an unconditional theorem that full four-channel tomography identifies the gate.

## 6. Actually executed exact source computation and separate physical validation

Primary new ORIGINAL local Python3.13 SymPy/NumPy program:
 /mnt/data/prf14_rot017/prf14_rot017_single_beacon_global_classification.py
 SHA256 cae03d0d9659c981cb479b32d433635bf2e32cdf38fa0698859431e4da806ed8.
Full source-specific machine certificate generated by actual execution:
 /mnt/data/prf14_rot017/prf14_rot017_beacon_exact_certificate.json
 SHA256 d0502d322d07a97bfede9f7d7711e818f51fba0db96d77e87240960cf4fb5c8d.
Original stdout:
 /mnt/data/prf14_rot017/rot017_stdout.txt
 SHA256 5e05be02e318dddfeb26f0dfc5ffcb6df7395c49daa7f0082c317ec69f1ed4b9.

Primary full source was executed TWICE with EXACT same report summary and hash, and checked:
- original three SO3 gates proper; all four contextual probability laws physical;
- all SIX possible 4x4 source beacon Jacobian determinants exact and nonzero;
- all SIX chosen beacon finite algebraic branch enumerations, exactly 4 per beacon, including tangent-half-angle infinity;
- all 6×4=24 gate branches and their 4×16 Fourier probability inversions exact, negative probabilities correctly FAIL-CLOSED;
- complete 4×9 physical channel identity for each putative branch from direct sixteen-history Pauli source sums, including the failing nonphysical formal branches as algebraic checks distinct from physical admission;
- globally unique output-Y beacons C_(X,Y), C_(Z,Y), each one legal branch;
- two legal output-X-beacon gates and all conditional source p minima, both same-row beacon invariances;
- exact cross-output second-invariance discrepancy −49/200;
- context-beacon C_(Z,Y) violation derivative −3/10 with arbitrarily small physical U_X(t) gate variation reproducing all four complete channels.

SECOND INDEPENDENTLY AUTHORED direct sixteen-Kraus/Pauli-history script (does not import primary program or use its generic formula to assert channel equality):
 /mnt/data/prf14_rot017/prf14_rot017_independent_physical_kraus_4x9_check.py
 SHA256 90b41156307d853d5ef0fa531404098a80ece4ad71704c98692c5eb51b00ee84.
Executed stdout SHA256 6615c6553069f7473e9a407f15f33fe69d338f6e5044da2304f5839d6b9bd537.
Checks all FOUR contexts exact physical source positivity and exact equality of ALL 36 channel entries for stationary R0 and alternate R_alt with TWO same-output-row conserved beacons. This is an independent within-author algorithm, NOT an external different-cell referee or quantum hardware observation.

No claims of n-shot source estimation in ROT017. Even though nonzero local Jacobians and strict alternative positivity margins imply a local continuity neighborhood of stable conditional inversion, a NUMERIC finite-sample confidence/accuracy theorem is not derived and should not be fabricated. The exploratory condition-number figures are not exact interval-certified confidence results.

## 7. Contemporary prior art and scope subtraction

The general mathematical ideas of local inverse-function identifiability, discrete global aliases, gauge freedom, Jacobian/Fisher information rank, and context-aware quantum process characterization are MATURE; no scientific novelty/firstness is assigned externally from this exact source witness.

Current original external source directly inspected for this turn:
Athira Kalavampara Raghunadhan et al., *Identifiability in Quantum State, Process, and Network Tomography*, arXiv:2609.13584, submitted 11 September 2026,
https://arxiv.org/abs/2609.13584 .
Its author text explicitly uses Fisher Information Matrix rank for local identifiability and establishes local↔global coincidence in a DIFFERENT quantum-network incidence-matrix problem. Do not transfer their local/global coincidence to this Pauli source-gate four-context model; here the exactly derived positive discrete aliases are a counterexample to such an unjustified transfer, not to their actual theorem.

P. Viñas and A. Bermudez, *A context-aware gate set tomography: Improving the self-consistent characterization of trapped-ion universal gate sets by leveraging non-Markovianity*, npj Quantum Information (26 June 2026), primary publisher:
https://doi.org/10.1038/s41534-026-01313-z .
Source abstract specifically reports context-dependent coherent and drift errors in physically microscopic parametrizations. Our beacon premise is a deliberately narrower modeling assumption, not equivalent to microscopic dynamics modeling or unknown-SPAM GST.

Roy, Srivastava, Giarmatzi and Gilchrist, *Practical Tomography of Multi-Time Processes*, arXiv:2604.01482v1, 1 April 2026:
https://arxiv.org/abs/2604.01482 .
Author abstract explicitly distinguishes informationally complete non-deterministic multi-time probes from restricted deterministic/unitary operations and demonstrates ancillary-qubit completeness. ROT017 is therefore NOT a general full quantum comb tomography method.

The exact global branch classification for this frozen classical Pauli 4-context source is INTERNAL original mathematical computation, no established external priority claim.

## 8. Referee falsifiers and final status

Independent REC/AUD referees should:
1. Replay six exact 4×4 beacon Jacobians and independently check 20 nonbeacon pivots in the 24×24 local observation Jacobian.
2. Enumerate complete SO3 sign/angle branches, including infinity, and exact 4×16 Fourier probabilities; challenge global uniqueness for C_(Z,Y) by finding any fifth admissible branch or positive probabilities in three rejected roots.
3. Recompute R_alt and all 4×16 alternative sources for C_(Y,X), verify two preserved same-output-row beacons and 36 exact physical Kraus channel entries.
4. Check that the global conditional uniqueness is not confused with the impossibility of testing beacon invariance from the same complete-channel data.
5. Recompute derivative −3/10 of the arbitrary-small exact nonstationary R'(t) alternative and ensure p'^q remains positive for an explicit nonzero t.
6. Assess whether source-context invariance of a single Fourier coordinate is externally physically plausible on actual hardware rather than just algebraically useful. No such independent source monitoring was performed.
7. Verify external literature novelty ceilings (2026 FIM rank, context-aware GST, ancillary multi-time process tomography) before any promotion.

Parallel NASH program B1 has other owners, latest 22 November native BlackHawk/Wu–Xu/hadronic work including Badacz REVIEW102/104 and EKS1/XH-S8. PRF14 neither reran LINX/BBN nor claimed a physical PBH bound. This report is independent restricted-source mathematical science.

FINAL:
PRF14_ROT017 / ORIGINAL_ROT016_GITHUB_REPORT_REOPEN / ONE_SOURCE_FOURIER_BEACON_REMOVES_UNKNOWN_GATE_3D_LOCAL_FIBER / SIX_EXACT_NONZERO_4X4_DETERMINANTS / ALL_SIX_TIMES_FOUR_GLOBAL_PHYSICALITY_CLASSIFICATIONS_PASS / TWO_OUTPUT_Y_BEACONS_EXACT_GLOBAL_UNIQUENESS_FROZEN_SOURCE / OUTPUT_X_TWO_POSITIVE_GATE_SOURCE_ALIASES_WITH_36_PAULI_CHANNEL_ENTRIES_EQUAL / SAME_ROW_TWO_BEACONS_NOT_SUFFICIENT / LOCAL_BEACON_MODEL_SATURATED_CANNOT_SELF_TEST / ARBITRARILY_WEAK_BEACON_VIOLATION_24_LAWS_EQUAL / INDEPENDENT_SECOND_16_KRAUS_SOURCE_PASS / NO_NEW_FINITE_N_CERT / NO_HARDWARE / NO_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN.
