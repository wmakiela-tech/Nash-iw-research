---
artifact_id: IW_PRF14_ROT012_CYCLIC_CLIFFORD_ROW_FLAT_PAULI_MEMORY_TEN_SETTING_STATISTICAL_RECOVERY_AND_MODEL_MISSPEC_FALSIFIER_001_20261122
date: 2026-11-22 Europe/Warsaw
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
exposure: PUBLIC
type: EXACT_CAUSAL_PAULI_COMB_SOURCE_RESTRICTED_EXPERIMENT_DESIGN / CLIFFORD_RELATIVE_CONTROL / FINITE_SAMPLE_CONFIDENCE / OFF_MANIFOLD_GUARD
status: ORIGINAL_SYMBOLIC_SOURCE_EXECUTED_PASS / 1200_SYNTHETIC_BERNOULLI_TRIALS_PASS / RIGOROUS_CONDITIONAL_HOEFFDING_PASS / EXTERNAL_REFEREE_OPEN
firstness: PRF13_ROT011_FIBER_AND_SIX_COORDS / PRF13_ROT012_KNOWN_GATE_MINIMAX / PRF14_ROT005_UNCALIBRATED_GATE_ALIAS / PRF14_ROT010_TWO_SIDED_EXACT_13_EXPECTATIONS / PRF14_ROT011_FINITE_N_33B_GENERAL_ESTIMATOR / PRF14_ROT012_NEW_CONDITIONAL_ROW_FLAT_CYCLIC_CLIFFORD_TEN_SETTING_SHORTCUT_ONLY
claim_ceiling: NO_GENERAL_QUANTUM_COMB_RECOVERY / NO_ARBITRARY_SIX_COEFFICIENT_ADAPTIVITY / NO_HARDWARE / NO_SPAM_SELF_CALIBRATION / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# PRF14 ROT012 — A cyclic Clifford control makes the restricted two-time Pauli memory source identifiable with 10 means; 95%-confidence source-witness label within 832,150 binary measurements

## 0. Exact scientific question and predecessor source firstness

ROT011 had a mathematical 95% finite-shot sufficient bound of 33,183,581,457 terminal Pauli binary shots (2,552,583,189 each of 13 settings). It used a valid but poorly conditioned cross-product inversion of the general six off-diagonal Pauli Fourier source correlations and an unknown middle unitary with two known relative controls. This huge bound was NOT a physical lower bound and left statistical efficiency open. The present turn asks if a physically natural, source-restricted class admits radically better measurement design.

I reread original actual PRF14 ROT011 local executable source and its JSON certificate as well as the exact source PRF14 ROT010:
https://github.com/wmakiela-tech/Nash-iw-research/blob/2925adf3e8e436a0101d46a2edfdc7c00f59e621/research/prf14/2026-11-21/IW_PRF14_ROT010_RELATIVE_TWO_SIDED_CONTROL_13_EXPECTATION_PAULI_MEMORY_SELF_CALIBRATION_DISCRETE_GAUGE_AND_OPTIMAL_SINGLE_PROBE_001_20261121.md (original blob 2e10001d834781a93fed954ff635b5bd422ebdfb).
https://github.com/wmakiela-tech/Nash-iw-research/blob/187ace16b1ba163e4c4d5f04b209950967741a4a/research/prf14/2026-11-22/IW_PRF14_ROT011_FINITE_SHOT_TWO_SIDED_PAULI_MEMORY_CERTIFICATE_AND_NO_UNIFORM_SAMPLE_THEOREM_001_20261122.md.

The 39,877-fold reduction in one sufficient bound below is REAL for the **restricted row-flat source family of the SAME four explicit worlds**, but MUST NOT be misrepresented as an improvement under exactly the same unknown-source guarantee as ROT011. ROT011 allowed general independent nonzero C_(j,i), i != j; this report explicitly ADDs a row-flat structural constraint. Indeed violating it is an experimental model falsifier. Shot complexity for an arbitrary six-parameter source or uncalibrated SPAM remains OPEN. No quantum hardware shots were carried out.

## 1. Legal source and sharpened source-model promise

Each independent run draws two classical Pauli labels (v,w) in F2² x F2² from a stable joint distribution p(v,w), applies U_v to one qubit, then exactly the chosen intermediate unitary, then U_w, and measures an output Pauli. The labels are exogenous, common to all intervening control choices, with IID runs and calibrated Pauli preparation/measurement reference.

Let chi_X, chi_Y, chi_Z be ordinary Pauli conjugation characters. All ten first-stage, second-stage and idle endpoint Fourier coordinates are fixed to the completely depolarizing source values, exactly as in PRF13 ROT011. Six hidden off-diagonal Fourier coefficients C_(j,i) (i != j) obey the **NEW ROW-FLAT STRUCTURAL PROMISE**:
C_(j,i)=c_i for each i, both j!=i, with |c_i|>0 and 2 Σ_i |c_i|<1.

The corresponding explicit legal physical source is
p(v,w)=1/16 [1+ Σ_i c_i Σ_(j!=i) chi_j(v)chi_i(w)].
The positivity sufficient condition is immediate by triangle inequality; the four main witness cases c_i=d_i/10 have all sixteen p positive with min 1/20, max 1/10. This is not an assumption derivable automatically from ordinary channel data; it is a falsifiable physical source ansatz. The original ROT010–011 FOUR legal worlds happen to satisfy this additional promise with common absolute amplitude c=1/10. The row-flat manifold has three hidden source coordinates, not the entire original six-dimensional fiber.

Unknown stable middle gate V has arbitrary SO(3) Bloch rotation R. The two control settings:
A: uncalibrated R;
B: apply independently calibrated W_C BEFORE unknown V, Bloch rotation R W_C,
where W_C is the proper cyclic Clifford SO(3) rotation
W_C = [[0,0,1],[1,0,0],[0,1,0]], W_C^3=I.
It is induced by a physical single-qubit SU(2) Clifford, e.g. V_C=(I-i(X+Y+Z))/2 up to convention/global phase. The two time-local noise events remain exactly the same. A known left-relative control W_L is used for ONE final resolving measurement as in ROT010:
W_L=[[0,1/sqrt2,1/sqrt2],[1,0,0],[0,1/sqrt2,-1/sqrt2]].

## 2. Conditional exact nine-scalar measurement theorem

For all i != j define original exact Pauli terminal expectations:
a_ij=C_(j,i) R_ij=c_i R_ij, for setting A;
b_ij=C_(j,i) (R W_C)_ij=c_i R_(i,j+1 mod3), for setting B.

Because the clockwise cyclic permutation maps column j to e_(j+1), the three B readouts with j=i-1 mod3 give the THREE MISSING diagonal entries c_i R_ii. The six A measurements contain the six off-diagonal entries. Therefore the 9 actually measured scalars assemble an entire 3x3 matrix
M_ij= a_ij for i!=j;
M_ii= b_(i,i-1 mod3);
and in exact arithmetic the IDENTIFIABLE COMPOSITE is simply
**M=diag(c_X,c_Y,c_Z) R.**

No ratio of small noisy expectations and no cross-product inversion is required. Each row norm identifies |c_i| exactly: a_i=||M_i,:||. The normalized row matrix U=diag(1/a_i) M is orthogonal, and sign(det U)=sign(∏c_i). There are exactly FOUR proper SO3 candidates R_s=diag(s_i) U for s_i∈±1 subject to ∏s_i=det U. Their source coordinates are c_s,i=s_i a_i. If all four candidate distributions remain nonnegative, they are physical, observationally indistinguishable in the first nine settings, and source/gate alias cannot be resolved from these nine alone.

These formulae apply algebraically even for unequal row amplitudes, provided the row-flat promise holds. ACTUALLY checked in SymPy for all four sign worlds in TWO source examples: (a_X,a_Y,a_Z)=(1/10,1/10,1/10) and (1/10,1/12,1/14). The simpler finite-N bound later is for the first EQUAL-magnitude witness only, not an assertion of a uniform bound for all unequal or vanishing c_i.

## 3. Exact four-world witness with 10 rather than 13 configurations

Fix unknown-to-estimator R0=[[-3,-2,6],[6,-3,2],[2,6,3]]/7, the original legal PRF13/14 middle gate, and c=1/10. Four physical source/gate worlds indexed by D=diag(d_X,d_Y,d_Z) in
(+,+,+),(-,-,+),(-,+,-),(+,-,-)
use R_D=D R0 and six C^D_(j,i)=d_i c. All four have strictly positive 16-label sources and completely depolarizing first-stage, second-stage and no-gate channels.

For ALL FOUR worlds, the original six A means and three new cyclic B means yield exactly the SAME nine-readout matrix M=c R0, and its rows each have exactly norm c. The remaining four sign possibilities cannot be identified by any number of repetitions of those nine measurements.

Set C: use calibrated W_L immediately AFTER unknown V, prepare +Y, measure terminal X. Write third expectation t_D=C^D_(Y,X) (W_L R_D)_(X,Y).
Under equal-|c_i| source promise it has an exceptionally well-conditioned expression in only TWO already measured source means:
**t_D = d_X [ d_Y b_(Y,X) + d_Z a_(Z,Y) ] / sqrt2.**
No inverse, row normalization or division is used, and the other seven measured first/second-setting means are needed only for full R and p reconstruction, not for the discrete world label.

In the original exact witness, b_(Y,X)=-3/70 and a_(Z,Y)=6/70, so the four t_D are precisely
(+3,-9,+9,-3) sqrt2/140,
whose pairwise minimum separation is Delta=3/(35 sqrt2)=0.06060915267313. This repeats the ROT010 optimal left-probe separation FIRST discovered there; ROT012 novelty is instead the NEW right cyclic control and NOISE-EFFICIENT reference prediction, not the third-probe gap.

Thus nine A/B scalar settings plus one C scalar setting, **10 settings SUFFICE** for exact joint reconstruction of the gate and the row-flat hidden source in this witness, assuming the other ten ordinary Fourier coordinates are already fixed/known. The source and gate have no generally unique interpretation before the C measurement, a genuine physical FOUR-world source/gate gauge.

## 4. FIRST complete all-10-setting 95% finite-shot theorem for this exact witness

All ten settings return independent IID terminal outcomes ±1. Let each empirical expectation be within eta of its correct mean. For sign candidate D the calculated third mean only needs a_(Z,Y) and b_(Y,X), so its error is at most sqrt2 eta, while the actual third empirical mean adds eta. Every candidate-prediction-to-observation distance is wrong by at most (1+sqrt2)eta. The four original exact means are Delta-separated, therefore the nearest-candidate classifier is provably correct for ALL such bounded perturbations when
**2(1+sqrt2)eta < Delta**.

Choose eta=3/250=.012 exactly. The left side is .05794112549695 < Delta=.06060915267313, leaving a positive deterministic model-selection gap >.00266802717618. This is not simulation, but a finite-dimensional worst-case inequality involving all admissible ten-measurement errors.

Hoeffding on each ±1 empirical mean gives P(|mhat-m|>eta)≤2exp(-n eta²/2). Union bound on ALL TEN settings:
P(any ten mean failures) ≤20 exp(-n eta²/2).
For 95% confidence (alpha=.05) it SUFFICES that
n=ceil[2 ln(20/.05)/(.012)^2] = **83,215 IID terminal shots per setting**, or **832,150 total shots across ten settings**.

Compare prior ROT011 rigorously sufficient 33,183,581,457 shots for its unrestricted-6-source-coordinate cross-product estimator: ratio **39,876.923**, more than four orders in these explicit sufficient upper bounds. NOT a hardware speedup measurement or a fair same-parameter-space complexity theorem: we deliberately add the row-flat source structural premise. This finite bound certifies correct DISCRETE four-world label; it does NOT certify small L2 error of the reconstructed continuous gate R.

Continuous physical parameter accuracy is separated. With ten mean errors <=eta, all nine M entries are within eta. Hence each M row error <=sqrt3 eta; estimated row amplitude |hat a_i-a_i|<=sqrt3 eta. If a_i>=a_min>0, normalized row L2 error <=2sqrt3 eta/a_min. For original a_i=.1, eta=.012 allows loose row error <=.4157. If a researcher wants a rigid **row error at most .03465** and amplitude error <=.001733 with the same 95% union guarantee, choose eta=.001 instead: n=11,982,930 per setting, 119,829,300 total. Still smaller than prior 33.18-billion conservative sufficiency, though this is not an optimized estimator or hardware-feasible proof.

## 5. Model-misspecification falsifier and a NEW robust certificate

A perfect equal-row source pattern is a scientific ASSUMPTION not a free gift. To measure its brittleness, allow the six hidden coefficients to vary separately within a small bounded source mismatch:
C^D_(j,i)=d_i (c+delta_(j,i)), c=.1, |delta_(j,i)|<=.003, other ten ordinary Fourier coordinates fixed at zero; all p remain strictly positive as 6*(.103)<1. The physical unknown gate remains R_D=D R0; known controls and SPAM exact and time-independent.

Now the nine source values need not assemble exactly c R0; the shortcut is misspecified. However the two reference means involved in the last prediction differ from their original exact values by at most |R_(Y,Y)|delta and |R_(Z,Y)|delta. Both the model's predicted third value and the actual third value separately differ from the corresponding original t_D by at most
K delta = (|R_(Y,Y)|+|R_(Z,Y)|)delta/sqrt2 = [9/(7sqrt2)]delta.

With each of the ten empirical means perturbed by at most eta, the nearest-candidate classifier remains correct if
**2(1+sqrt2)eta + 4[9/(7sqrt2)]delta < Delta**.

At eta=.010 and delta=.003, the left side is .05919391873 < .06060915267; deterministic margin ~.00141523 is POSITIVE. Therefore the same 95% confidence proof works even with this PRECISELY BOUNDED, 3%-of-c source-family violation using
n=ceil[2 ln(400)/(.01)^2]=**119,830 shots per each of ten settings**, i.e. **1,198,300 total shots**.

The robustness theorem does NOT make an arbitrary six-parameter source identifiable or guarantee correct reconstruction of the six individual off-manifold coefficients. It certifies the discrete D label within the specified perturbation family; full arbitrary-source tomography still needs independent controls and source manifold testing.

**Model diagnostics:** the three otherwise unused B readouts under cyclic control must satisfy b_(i,i+1)=M_(i,i+2) (indices mod3) for exact row-flat source, and M must have pairwise orthogonal rows. Row norm equality is a further check for common magnitude c. These are falsifiers of the strong model premise, NOT sufficient logical proofs of it. For zero-source limit c→0 the ROT011 no-uniform-shot theorem remains: the gap scales with c and n must diverge at least O(c^-2); there is no universal uniform finite-shot miracle.

## 6. Actually performed exact and statistical computations

Local Python 3.13 SymPy exact arithmetic:
- R0, W_C and W_L legal SO(3), W_C³=I: PASS;
- all 4x16 p_D entries, positivity 1/20..1/10, normalization and all ordinary first/second/idle channel Fourier coefficients zero: PASS;
- all nine source readouts equal for four different legal source/gate worlds and matrix M=cR0: PASS;
- exact unequal row-flat example (1/10,1/12,1/14), all four sign worlds physical, nine matrix identities and third row-norm formula: PASS;
- exact four terminal means and Delta: PASS;
- deterministic 95% eta-box bounds, equal source and 3% misspec model: PASS.

LOCAL statistical stress: 4 source/gate worlds x 300 trials = 1200 independent synthetic Bernoulli measurement experiments, each trial with six randomly assigned model-misspec delta coefficients bounded by .003 and 119,830 shots PER setting (sampled using exact Binomial count draws, not loop over every event). Source probabilities stay positive, independently sampled binomial laws are genuine for the restricted synthetic model, no device physics. All 1200 D-label classifications PASS, smallest observed correct-vs-next candidate distance margin ~.034603. These trials support implementation sanity; analytic deterministic eta-plus-delta bound supplies the general guarantee.

Executable local source:
 /mnt/data/prf14_rot012/prf14_rot012_cyclic_clifford_structural_promise.py
SHA256 ba4e686c7c50cad13ed6aadbfb4da3f339a3de75428f254f822a50374b87b7f6.
Original machine certificate:
 /mnt/data/prf14_rot012/prf14_rot012_cyclic_clifford_certificate.json
SHA256 adf44da257576c3105f6961f1dca309d1bcdfec6e37761f286f001fbebd67c11.
Independently generated Python/SciPy preliminary 7,000 random SO3 candidate right controls, followed by optimization / rational quaternion scan, also found significantly better conditioned right controls than old ROT011; it did NOT prove a global right-control optimum. The final simple CYCLIC CLIFFORD exactly works and avoids continuous numeric gate optimization and intricate calibration. The finite sample proof does not depend on that exploratory candidate search.

## 7. Mature context and comparison with other ongoing cells

General source-and-gate gauge freedoms, Clifford-based noise identification, self-consistent tomography and concentrated estimator bounds are all mature. Primary 2026 sources reviewed:
- Efficient Self-Consistent Learning of Gate Set Pauli Noise, PRX Quantum 7, 010305 (2026), https://doi.org/10.1103/1pnv-t9px.
- Disambiguating Pauli Noise in Quantum Computers, PRX Quantum 7, 033045 (3 Sep 2026), https://doi.org/10.1103/69wc-gzl6; experiment on IBM hardware up to 92 qubits under a different gate-set noise model. It is a very close mature host for LEARNABLE vs GAUGE in Clifford Pauli noise, not a reproduction of this explicit two-time row-flat comb.
- The Learnability of Pauli Noise, Nature Communications 14, 52 (2023), https://doi.org/10.1038/s41467-022-35759-4; characterizes gauge freedom with graph cuts/cycles.
- Process Tomography for Clifford Unitaries, Phys Rev A 113, 012414 (6 Jan 2026), https://doi.org/10.1103/zjfb-3jzb.
No prior-art clearance for external novelty. NASH ROT012 is an explicit INTERNAL source-specific construction, not a new general theory of quantum memory, no experiment on hardware, no physical NASH cross-domain link.

As of original 22 Nov 10:33/11:13 research currentness, owner B1 Badacz REVIEW095 actual 232 Julia and 233 network runs with 6/6 reported gates, modern generator dmod=(HER73-PY83) 24 values .1315.. .2283 dex over nominal, MC replicas, solver perturbation; last status LM_STABLE_IN_3_REALIZATIONS, expressly NOT a statistical confidence interval or PBH exclusion. Primary source Git blob 177d9df89dcb4f63acdeedd2879bc062dafa0f51:
https://github.com/wmakiela-tech/Nash-iw-research/blob/9a0220809f2c69aad0b7b245b701812d05b57263/research/badacz/2026-11-22/IW_BADACZ_B1_MODERN_GENERATOR_REPLICA_TRANSFER_REVIEW_095_20261122.md.
At 11:12 newer LT9/Mech/KN/INT B1 returns have also appeared, but none changes this PRF14's quantum source computation. No new LINX/AlterBBN native run claimed; PBH physical interpretation remains owner-driven and NO_PHYSICAL_PBH_BOUND.

## 8. Open falsification and next theory frontier

Independent referee should:
1. Challenge the row-flat promise: attempt a six-independent-Fourier coefficient legal source alias passing the nine or thirteen optional consistency tests while defeating claimed full parameter recovery; this would NOT refute the conditional theorem but quantify the model-identification limit.
2. Audit that the nine scalar settings really measure M=diag(c_i)R only because the cyclic Clifford maps each used column to the requested one and C_(j,i) is row-flat.
3. Audit all four d legal source distributions and post-V third expectation against completely independent finite group Fourier implementation.
4. Audit the 832,150- and 1,198,300-shot bounds and the 0.003 source-model perturbation inequality, including the distinction between D label and continuous parameters.
5. Optimize statistics under a less restrictive six-correlation model, or introduce a CHOICE of independently known additional Clifford right controls to reconstruct a general source without a row-flat promise. This would address ROT011's actual wider open problem; don't promote the narrower construction to the wider claim.

FINAL RETURN:
PRF14_ROT012 / ORIGINAL_PRF13_PRF14_SOURCE_REOPENED / EXACT_CYCLIC_CLIFFORD_10_SETTING_ROW_FLAT_INVERSE_PASS / FOUR_STRICT_POSITIVE_WORLD_IDENTITY_9_MEANS_PASS / 10TH_Pauli_SIGNAL_DISTINCT_PASS / MODEL_CONDITIONAL_832150_TOTAL_SHOT_95PC_CONFIDENCE_CERT_PASS / 3PCT_OFF_MANIFOLD_1198300_SHOT_95PC_ROBUSTNESS_PASS / 1200_SYNTHETIC_BERNOULLI_TRIALS_PASS / SOURCE_PROMISE_EXPLICIT_NOT_SILENT / NO_GENERAL_SIX_PARAMETER_REPLACEMENT / NO_NOVELTY / NO_HARDWARE / NO_CANON / NO_EXEC_SIGN.
