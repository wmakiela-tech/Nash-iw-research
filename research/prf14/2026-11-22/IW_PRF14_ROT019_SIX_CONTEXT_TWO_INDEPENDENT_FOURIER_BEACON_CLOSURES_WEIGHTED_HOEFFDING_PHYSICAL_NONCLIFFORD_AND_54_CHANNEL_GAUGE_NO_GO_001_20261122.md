---
artifact_id: IW_PRF14_ROT019_SIX_CONTEXT_TWO_INDEPENDENT_FOURIER_BEACON_CLOSURES_WEIGHTED_HOEFFDING_PHYSICAL_NONCLIFFORD_AND_54_CHANNEL_GAUGE_NO_GO_001_20261122
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
science_class: SOURCE_RESTRICTED_SIX_CONTEXT_TWO_TIME_CLASSICAL_PAULI_CORRELATION / TWO_INDEPENDENT_BEACON_FALSIFIERS / PHYSICAL_POST_GATE_NONCLIFFORD_CONTROL / WEIGHTED_HOEFFDING_CONCENTRATION / LEVEL_POWER_CALIBRATED_FIVE_SETTING_FAMILYWISE_TEST / FULL_54_CHANNEL_UNKNOWN_GATE_GAUGE
status: ACTUAL_EXACT_SYMPY_PROOF_PASS / ACTUAL_INDEPENDENT_DIRECT_16_PAULI_HISTORY_SIX_CONTEXT_54_CHANNEL_REPLAY_PASS / ACTUAL_PHYSICAL_SO3_BLOCH_POVM_3000_BINOMIAL_TESTS_PASS / BYTE_IDENTICAL_REPEAT / DIFFERENT_CELL_AUDIT_PENDING
firstness: PRF13_ROT011_SIX_FOURIER_FIRST / PRF14_ROT013_SIX_PARAM_13_SETTINGS / PRF14_ROT015_CONTEXT_GAUGE / PRF14_ROT016_FOUR_FULL_CHANNEL_3D_ALIAS / PRF14_ROT017_ONE_BEACON / PRF14_ROT018_FIFTH_CONTROL_H_QUADRATIC_FALSIFIER / PRF14_ROT019_NEW_SIXTH_NONCLIFFORD_G_LINEAR_AND_TWO_RESIDUALS / INT10_ROT020_SHARP_SIX_FOURIER_TV_OPERATOR_FIRST / AUD3_ROT011_SHARP_ROW_INTERVAL_FIRST
ceiling: NO_GENERAL_QUANTUM_PROCESS_TENSOR / NO_BEACON_VERIFICATION_FROM_PASSING_TEST / NO_UNCALIBRATED_SPAM / NO_CLIFFORD_CLAIM_FOR_Q / NO_HARDWARE / NO_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# ROT019: A sixth physical control makes two independent source-beacon falsifiers; a calibrated three-setting linear test detects a specified drift with 27,669 binary shots

## Executive result and scientific restraint

PRF14 ROT018 introduced a FIFTH physical known post-target Clifford control \(P^2R\) and one quadratic identity \(H=0\) which is a necessary but not sufficient condition for one selected hidden classical two-time Pauli Fourier source correlation to remain identical across five middle intervention contexts. It delivered a conservative 95% level AND alternative-detection-power sufficient resource of 222,780 (ideal) or 240,248 (bounded calibration) shots, across four Pauli settings, for a strictly positive +.1 drift in the left-L context.

**NEW ROT019** adds one further known LEFT gate \(QR\), where Q is a LEGAL proper SO3 single-qubit rotation, **NOT a Clifford**:
 Q=[[-4/5,0,3/5],[3/5,0,4/5],[0,1,0]], QᵀQ=I and det Q=+1.
Crucially its output-Y row is \((3e_X+4e_Z)/5\). In the same one-beacon model there is now a SECOND, LINEAR overidentification witness
 G = y_(QR) −(3/5)y_(LR)−(4/5)y_(P²R)=0.
The original H and new G have LINEARLY INDEPENDENT normal covectors, and their gradients jointly span the two-dimensional left nullspace of the six-beacon-data /four-source-gate-coordinate Jacobian, which has exact rank 4. This is a genuine information uplift rather than a change of notation or a duplicate of ROT018.

Two STRICTLY PHYSICAL independent negative examples:
1) q5=QR source beacon drifts from .1→.2 while everything else stays at .1: H=0 EXACT but G=3/35 ≠0; TV(source_q5,stationary)=.05; p positive min63/1600.
2) q3=LR beacon .1→.2 and simultaneously q5=QR beacon .1→.16: H=27/1225≠0 but G=0 EXACT; both changed sources have all sixteen p positive (smallest63/1600); TV respective .05,.03.
The second is not detected by G, showing independent falsification, while the first was ENTIRELY INVISIBLE to the prior quadratic H.

A calibrated, independent **three-setting** test using G detects example 1 with type-I error at most 5% AND source-specific power at least 95% after **9,223 ±1 measurements per setting, N=27,669 total**. For the *same q3=LR source perturbation as ROT018*, new G yields both bounds with **25,618 per setting, N=76,854**, vs ROT018's earlier conservative 240,248 sufficient upper bound, a 3.13x reduction in two sufficient upper bounds. The proofs exploit concentrated *weighted means* rather than a union bound across 3 or 4 individual mean errors.

A simultaneous two-witness familywise 95%-valid H-or-G test across FIVE actual configurations has a straightforward conservative N=529,835 sufficient bound and ≥95% detection probability separately for all three physically constructed drift families. This joint bound is NOT statistically optimal.

**NONIDENTIFIABILITY REMAINS:** Without independently establishing the common beacon premise, there exist TWO distinct legal physical target gates together with SIX different strictly positive control-conditioned sources that reproduce ALL SIX complete qubit channels exactly, including **54/54 Bloch transfer matrix entries**. They pass BOTH closures H=G=0 with no information on the true beacon invariance. Adding finitely many deterministic unitary control contexts in this particular unconstrained conditional-source model does not automatically establish stationarity or a general process-tensor reconstruction theorem.

## 1. Original firstness and current source checked

The original ROT018 pinned full 17,852-character source was actually reopened through immutable GitHub and its ORIGINAL exact local Python file and certificate inspected and hashed:
https://github.com/wmakiela-tech/Nash-iw-research/blob/5c0c48ad110f1f10ed2b0b173930cbd4186f9b92/research/prf14/2026-11-22/IW_PRF14_ROT018_FIFTH_CONTEXT_QUADRATIC_SOURCE_BEACON_FALSIFIER_95PC_PHYSICAL_CALIBRATION_AND_UNDETECTABLE_GAUGE_001_20261122.md
local ROT018 original Python SHA256 c3dc07a152d7e16e03fc6abfcbe24eda2008b7b638353d25b6028d12a1786519.
The PRF13 original six-dimensional hidden Fourier source and PRF14 ROT015–017 retain exact lineage and firstness; no new generic source identity claim here.

Different-cell INT10 ROT020 original PRIVATE report (14,321 characters, original Git blob138debb4751be385b855c33311a1cc71946b7674) was directly reopened. INT10 independently derived the SHARP six-character Fourier-to-TV L∞ operator norm 9/8 and improved PRF14 ROT016's conditional 95% known-gate source-TV upper sample bound 7.716-fold to 131,845,119,072. That is INT10's distinct first result, NOT part of ROT019's new moment tests. Original INT10 source:
https://github.com/wmakiela-tech/Nash-Priv/blob/481a6a299ef5dc23ed52f150f2ba61e435af44a9/research/int10/2026-11-22/IW_INT10_ROT020_PRF14_SHARP_PAULI_SIX_CHARACTER_TV_OPERATOR_NORM_AND_CONDITIONAL_95PC_RESOURCE_REDUCTION_001_20261122.md

Primary external mature prior:
Kenneth Rudinger, Timothy Proctor et al., *Probing Context-Dependent Errors in Quantum Processors*, Physical Review X 9 021045 (3 June 2019), https://doi.org/10.1103/PhysRevX.9.021045, authors explicitly develop rigorous context/drift tests; and P. Viñas/A. Bermudez, *A context-aware gate set tomography*, npj Quantum Information (2026), https://doi.org/10.1038/s41534-026-01313-z. Roy et al *Practical Tomography of Multi-Time Processes* arxiv 2604.01482 (2026) explicitly addresses the informational incompleteness of deterministic intermediate controls for unrestricted process tensors. None of the above establishes external firstness for the particular restricted-source H,G construction. No 2026 literature priority clearance claimed.

## 2. Exact source and six physical controls

Two jointly correlated classical Pauli labels (v,w)∈F₂²×F₂² are drawn at a preannounced fixed intervention context q; apply U_v, physical single-qubit target-and-relative-control gate S_q, U_w, then an independently chosen Pauli eigenpreparation/terminal ±1 measurement. Each q has its own strictly positive sixteen-entry joint source p^q(v,w) if context dependence is allowed. Within q, source does NOT depend on the Pauli preparation, measurement, or shot number; runs are independent and identically distributed. Context q is announced before FIRST error, so there is no retrocausal inference. However such a family need not be a SINGLE exogenous intervention-independent process tensor/comb.

All ten ordinary Fourier coordinates fixed at zero and SIX offdiagonal hidden source coefficients C^q_(j,i) (Pauli input j, output i) may independently vary between q. The entire physical source is
 p^q(v,w) = [1+Σ_(i!=j)C^q_(j,i) χ_j(v)χ_i(w)]/16.
Each full unital CPTP qubit transfer channel is
 T^q_(i,j)=C^q_(j,i) S_q(R)_(i,j) for i!=j; diagonal transfer entries zero.
This follows exactly from the convex mixture of sixteen proper Pauli SO3 conjugations, not an unphysical signed transfer ansatz.

Original physical test witness:
 R=[[-3,-2,6],[6,-3,2],[2,6,3]]/7;
 P=[[0,0,1],[1,0,0],[0,1,0]], P³=I;
 L=[[0,1/√2,1/√2],[1,0,0],[0,1/√2,-1/√2]];
 C=[[0,.09,.11],[.07,0,.10],[.08,.12,0]], with all six free positive-domain coefficients, ordinary marginal and idle channels depolarized and min original p=73/1600.

NEW sixth left control is
 Q=[[-4/5,0,3/5],[3/5,0,4/5],[0,1,0]],
 QᵀQ=I, det Q=+1, and Q_Y,:=(3e_X+4e_Z)/5.
**Q IS NON-CLIFFORD**; unlike earlier P/P², its successful use requires separate trusted calibration of a non-Clifford single-qubit gate. Every proper SO3 Q has an SU2 lift, so it is a physically allowed coherent control. The actual six context middle rotations:
 S0=R, S1=RP, S2=RP², S3=LR, S4=P²R, S5=QR.
RIGHT/LEFT placement is NOT interchangeable. In the exact witness all 6×6 offdiagonal rotation pivots are nonzero, though the worst |pivot|=1/35 in q5; this is relevant to reconstruction conditioning, not directly to the beacon test, which only uses (output Y,input Z) where the q5 pivot is 6/7.

Choose beacon c=C^q_(Z,Y)=C^q_[output row Y,input column Z], hypothesized invariant across all SIX q; the remaining five source coefficients in each context remain free.

## 3. Two algebraically independent unknown-gate-independent beacon closures

Prepare +Z, measure output Pauli Y under six contexts. If the same unknown beacon c applies, the ideal scalar means are
 y0=c R_YZ,
 y1=c R_YX,
 y2=c R_YY,
 y3=c R_XZ,
 y4=c R_ZZ,
 y5=c[(3/5)R_XZ+(4/5)R_ZZ].
The two independent identities are:
 **H=y3²+y4²−y1²−y2²=0** (ROT018 firstness, SO3 row Y/column Z norms);
 **G=y5−(3/5)y3−(4/5)y4=0** (NEW ROT019, calibrated linear left-control combination).

These are NECESSARY, not SUFFICIENT, for invariant beacon. Neither requires knowing the middle R or the common beacon c when calculated from the four/five measured means.

Exact reference source c=.1 gives
(y0,y1,y2,y3,y4,y5)=(1/35,3/35,−3/70,3/35,3/70,3/35), H=G=0.

For the gate/source parameter block with one beacon c and three SO3 infinitesimal axes, its full 6×4 Jacobian J has exact rank FOUR. The two gradients with respect to six scalar data are
 ∇H=(0,−2y1,−2y2,2y3,2y4,0),
 ∇G=(0,0,0,−3/5,−4/5,1).
Independently executed SymPy establishes ∇H J=0 and ∇G J=0, with rank([∇H;∇G])=TWO; hence these form a basis for the TWO-DIMENSIONAL left-null tangent space. No numerical singular value substitution is used to establish the exact rank.

Full six-context channel tomography has 6×6=36 nonzero terminal Pauli transfer scalar means. With arbitrary context-conditioned sources, the source domain has 36 independently variable hidden Fourier C coordinates plus dim(SO3)=3 target-gate parameters, total 39. One beacon equality across six contexts imposes FIVE independent source conditions, yielding 34 model degrees of freedom. As the 30 nonbeacon conditional source coordinates enter their channel means via nonzero direct pivots, the full map has local differential rank 30+4=34, leaving EXACT TWO overidentifying dimensions among 36 terminal channel means. Thus the sixth context genuinely upgrades ROT018's 1 closure to 2, but both apply only to one selected beacon; they do NOT comprehensively inspect all six source correlations.

## 4. Two disjoint physical drift alternatives: independence is operational, not merely differential

Each alternate experiment changes ONLY the selected hidden beacon coefficient C^q_(Z,Y), with all other five source coefficients unchanged from baseline C in that context. Fourier inversion exactly checks all 16 probabilities positive/normalized and all ordinary source Fourier coefficients zero.

(A) **H-BLIND / G-VISIBLE:** Only context q5=QR changes beacon c5=.10→.20. Result:
 y5=6/35, while y1,2,3,4 retain baseline;
 H=0 EXACT,
 G=3/35≈.0857142857.
Source TV(p^q5,p_original)=.05; new min source probability 63/1600=.039375.

(B) **G-BLIND / H-VISIBLE:** q3=LR beacon .10→.20 and q5=QR beacon .10→.16 (c5=4/25). This gives y3=6/35, y5=24/175, y4=3/70 and
 H=27/1225≈.0220408163 ≠0,
 G=0 EXACT.
The two affected source TV distances are .05 and .03, and minima 63/1600 and 67/1600, respectively. Both sources genuine physical positive classical Pauli histories, NOT negative formal Fourier distributions.

(C) **ORIGINAL ROT018 q3-only physical drift:** q3 beacon .10→.20, q5 remains .10; then H=27/1225 but G=−9/175≈−.0514285714. This permits an equal-alternative sample cost comparison against the previous ROT018 four-setting test.

By construction no test of only H can detect (A), and no test only of G can detect (B), even at infinite sampling with ideal calibration. BOTH tests together have strictly broader falsification power.

## 5. NEW direct weighted-Hoeffding theorem for three-setting G-test, nonideal controls

For the G test one measures ONLY q3=LR, q4=P²R and q5=QR; the old right controls and q0 do not enter. At each of three configurations take n INDEPENDENT IID ±1 Pauli outcomes. Define
 \hat G = \hat y5−(3/5)\hat y3−(4/5)\hat y4,
 weights w=(−3/5,−4/5,+1) with exactly Σw²=9/25+16/25+1=2.
Weighted Hoeffding for independent bounded ±1 mean samples yields
 **Pr(|\hat G−E\hat G|>t) ≤2 exp[−n t²/4]**,
 uniform in arbitrary unknown binary outcome probabilities. This avoids a coordinatewise union bound and is NOT an appeal to Gaussian statistics.

A legal calibration error model must also be included: physical P,L,Q pulse implementations all proper SO3 and separately externally guaranteed ||Ptilde−P||₂,||Ltilde−L||₂,||Qtilde−Q||₂≤.001 PER pulse; P² uses TWO physical P pulses and can deviate by ≤.002, including when placed after target. True Pauli Bloch eigenpreparation differs from ideal by norm≤5e−5, physical binary two-outcome POVM Bloch effect axis by≤5e−5 and bias |b|≤5e−5, with |b|+||n||≤1. All systematic errors stable within a setting. Physical source Fourier coefficients in these witness families satisfy |C^q_ij|≤.2; ||T||₂≤1 as a CPTP Pauli mixture.

As justified first in ROT014/018, this produces uniform per-mean systematic bound
 μ=max{.2×.002,.2×.001} +3×.00005 = **.00055**,
 with prep/measurement errors NOT spuriously multiplied by cmax.
Therefore the measured linear G's expected value differs from ideal by at most
 B=(1+3/5+4/5)μ=(12/5)μ=**.00132**.

**Predeclared two-sided source-invariance test:** REJECT if
 |\hat G|>B+t,
 for fixed t>0 and n chosen. Under the invariant-beacon null, Gideal=0, and false rejection rate at most 2 exp(−n t²/4), for ANY unknown R and any physically valid source in this declared |C|≤.2 calibrated apparatus class. Under an actual DRIFT alternative with ideal |G|=Δ, the same exponential bound controls missed detection provided the STRICT deterministic margin
 **Δ>2(B+t)**,
 because on |\hat G−E\hat G|≤t one has |\hat G|≥Δ−B−t>B+t.

Set α=β=.05 with n=ceil[4 ln(40)/t²]:
- H-blind q5-only .1→.2: Δ=3/35, t=.04. n=9,223 per configuration (three configurations), total **27,669**; tail bound .0499839753, strict power margin Δ−2(B+t)=.003074285714>0.
- Original q3-only .1→.2 (ROT018 physical alternative): Δ=9/175, t=.024. n=25,618 each, total **76,854**; tail bound .0499943730, strict margin .000788571429>0.
This is a true level-α and source-specific power≥1−β sufficient UPPER bound, NOT actual device data, a statistical lower bound, or a proof of general source-stability identification. Compared to ROT018 bounded H test 240,248, G's same q3 alternative bound is about 3.126-fold lower in these conservative source-conditional upper bounds.

## 6. NEW joint two-witness familywise 95% certificate

To avoid interpreting separate 95% controls as one aggregate 95% familywise guarantee, use FIVE settings q1,q2,q3,q4,q5 (q0 cancels both witnesses) and a SHARED deterministic concentration event:
 max_{k=1..5} |\hat y_k−y_k^actual|≤η_stat=.01.
With calibrated μ=.00055 per mean, all five observed means differ from their nominal ideal reference by at most e=η_stat+μ=.01055.

Define the adaptive H decision inherited from ROT018:
 REJECT_H iff |\hat H| > 2e Σ_{k=1..4}|\hat y_k|+4e².
Define G decision:
 REJECT_G iff |\hat G|>(12/5)e.
Overall REJECT H0 ("one common beacon") if EITHER witness rejects.

Under H0, simultaneously H=G=0 and neither test rejects on this ONE five-coordinate error event, so there is NO unaccounted multiple-testing inflation. Joint ±1 Hoeffding union:
 **Pr(false rejection by H or G) ≤10 exp(−n η_stat²/2)**.
For 95% choose n=ceil[2ln(200)/(.01)²] = **105,967 each of 5 settings**, total **529,835** binary shots. Actual conservative tail upper ~.04999837.

For each exact physical alternative (A),(B),(C) in §4, the SAME event yields detection by at least one witness:
- A q5-only: |G_true|−2(12/5)e = .035074285714 >0;
- B q3+.1 & q5+.06: H_true−4e Σ_{q1..q4}|true y_q|−16e²=.005791404898 >0 (Gtrue=0);
- C q3-only: both previous H margin >0 and |G_true|−2(12/5)e=.000788571429>0.
Thus the overall five-setting H-or-G test has familywise false positive probability≤.05 under the null and detection probability≥.95 for EACH of these three specific strictly-positive physical alternatives, under the stated uniform calibration class. NO universal ≥95% power against arbitrarily small drift; ROT015/016 counterexamples prohibit it.

## 7. Explicit negative: even six full 3×3 CPTP channels do not VERIFY one beacon

One can increase observations indefinitely without validating an assumption that is not identified by the observable model.

Construct original fully stationary (R,C) and different proper SO3 target
 R'=U_X(t)R, t=1/1000,
 where U_X(t)=[[1,0,0],[0,(1−t²)/(1+t²),−2t/(1+t²)],[0,2t/(1+t²),(1−t²)/(1+t²)]], proper SO3.
Independently for EACH q=0..5 set alternative context-source Fourier coordinates
 C'^q_(j,i)=C_(j,i) [S_q(R)]_(i,j)/[S_q(R')]_(i,j) for all i!=j,
 and Fourier-invert each into 16 joint Pauli probabilities.
All six resulting sources are STRICTLY POSITIVE (minimum among their 16 probabilities over q >.04557). Their TV from common original source by q:
 [0.0002384893,0.0001428669,0.0003577340,0.0002717206,0.0002767393,**0.0017640861**].
They are genuinely context-dependent; the beacon C_(Z,Y) is not the same across q.

**FIRST direct author's exact source check** proves all SIX full transfer matrices equal componentwise by the source-gate product identity.
**SECOND independently authored local algorithm**, with ZERO imports from first, forms the actual CPTP Bloch transfer by **literal summation of all 16 Pauli history terms**,
 T_q = Σ_{v,w} p^q(v,w) D(w) S_q(R) D(v).
It finds exact equality of **54/54 entries** (six contexts×3×3 full Bloch matrices, including zero diagonal entries), and verifies 6×16 positive normalized probabilities. Therefore the two physically different six-context source/gate systems have EXACTLY identical terminal single-qubit outcome laws for any preparations/POVM within these six gate-control contexts. Both H and G are identically zero in both worlds. Nothing in this turn shows that all physically possible interventions have identical process response, or that the alternate contextual sources form one global exogenous comb.

For arbitrarily small nonzero t, this physical gauge deformation remains possible and context-dependent source TV→0, so passing both tests does NOT establish the common beacon premise. This is anti-self-sealing scientific negative knowledge.

## 8. Actually executed mathematical and model sampling tests

Author original local executable actually run TWICE with BYTE-IDENTICAL stdout and JSON:
 /mnt/data/prf14_rot019/prf14_rot019_dual_beacon_closures.py,
 SHA256 de24a615b656478f612fa04dd567dd142e7e6c3ad94c0466e74405dc10d0dfd1.
Exact physical, statistical, synthetic data JSON:
 /mnt/data/prf14_rot019/prf14_rot019_dual_closure_certificate.json,
 SHA256 c4662a65c823139a5fa4d442202945bd0f2c6bf6f4a3aec5944ad9a88c744dfa.

INDEPENDENTLY WRITTEN same-author direct 16-Pauli-histories/54-exact-transfer source (actually run and verified):
 /mnt/data/prf14_rot019/prf14_rot019_independent_six_context_kraus_rank.py,
 SHA256 024b0839b4c2d4146def1e0852643874897a3bf1cf9ee2d0d2e8c528895d6119.
Both Python sources pass bytecode compile. No tool used artificial source probabilities or unphysical SO3, and no actual quantum hardware executed.

Actually executed physically perturbed synthetic experiments:
- For weighted G at 9,223 shots/setting: 500 null trials → **1 false rejection**; 500 q5-only true alternatives → 500 detections.
- At 25,618 shots/setting: 500 null trials → zero false rejections; 500 q3-only true alternatives → 500 detections.
- For combined five-setting H-or-G at 105,967 shots/setting: 250 null trials → zero either-witness rejections; 250 q5-only alternatives → 250 G detections and zero H; 250 q3+.1,q5+.06 alternatives → 250 H detections and zero G; 250 q3-only alternatives → 250 H AND G detections.
TOTAL **3,000 complete synthetic binomial-count experiments** with independently perturbed SO3 P,L,Q physical gates, physically admissible qubit Bloch states and biased two-outcome POVMs (|b|+||n||≤1), stable within each setting. These are model samples, not real hardware. The one false alarm in 500 is NOT concealed: the mathematical type-I ceiling is ≤5%, not zero. The rigorous error control comes from weighted Hoeffding and deterministic margin, NOT from the empirical percentages.

## 9. Consequences, limitations, audit falsifiers and science next

CORE ADVANCE: an extra calibrated proper rotation with one output row mixing two formerly tested columns supplies a *new linear overidentification*. In this source-witness it detects a physically positive H-invisible context drift at a moderate finite-shot sufficient cost, while the original H independently detects a compensated G-invisible drift.

Costs: Q is NON-CLIFFORD, so the laboratory control reference becomes more demanding than for Clifford-only interventions. Q has a 1/35 small offdiagonal Bloch pivot elsewhere, potentially damaging full-source tomography conditioning; the LINEAR selected beacon q5 pivot 6/7 is large. Additional controls can be optimized for reference fidelity, signal, other-source pivots or sparsity, but no global optimization or general noise model is solved here. The tests do NOT detect arbitrary other five Fourier source coefficients or all compensated correlated drifts. One common-source beacon across six contexts remains a premise that can be falsified but not verified from this finite deterministic-control design.

Bounded independent AUD3/REC13 referee tasks:
1. Verify QᵀQ=I, det+1, Q is indeed NON-CLIFFORD; check physical insertion Q after R, not RQ.
2. Derive H and G independently from SO3 row/column identities, and independently verify 6×4 rank4 and both independent left-null gradients (plus 36 vs34 model dimensions).
3. Check four exact 16-probability source witness worlds (H-blind G-only, G-blind H-only, q3-only, null), TV, exact H/G and all source positivity.
4. Derive weighted Hoeffding 2exp(−n t²/4) for three INDEPENDENT ±1 means, systematic B=.00132, robust n=9223/25618, type-I and source-specific power without assuming Gaussianity.
5. Verify the combined FIVE-setting union concentration and familywise α, 529,835 shots, all three alternatives with positive margins and no hidden repeated-testing alpha inflation.
6. Recompute independently 6×16 Pauli history probabilities and all 54 CPTP Bloch transfer entries for the physical stationary vs nonstationary R' alias. Establish this is NOT a single fixed unrestricted quantum process-comb identity.
7. Compare mature 2019+2026 context-aware and non-Markovian tomography literature before novelty claims.

Parallel PRF B1 science is separate: Badacz REVIEW102r2/104, EKS1/KN16, etc; no native BBN/Wu-Xu/PBH experiments or physical bound in PRF14 ROT019.

FINAL STATUS:
PRF14_ROT019 / ORIGINAL_ROT018_REOPENED / SIXTH_CALIBRATED_NONCLIFFORD_POST_TARGET_Q / TWO_INDEPENDENT_H_AND_G_SOURCE_BEACON_CLOSURES_EXACT / 6x4_JAC_RANK4_TWO_RESIDUALS / TWO_STRICT_POSITIVE_MUTUALLY_BLIND_CONTEXT_DRIFT_WITNESSES / WEIGHTED_HOEFFDING_NONIDEAL_95PC_LEVEL_AND_POWER_27669_AND_76854_SHOTS / JOINT_5_SETTING_FAMILYWISE_95PC_529835 / 3000_PHYSICAL_MODEL_BINOMIAL_SYNTHETIC_TRIALS_WITH_ONE_NULL_FALSE_REJECTION / SIX_CONTEXT_54_CPTP_MATRIX_ENTRIES_NONSTATIONARY_ALIAS_EXACT / NO_HARDWARE / NO_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN.
