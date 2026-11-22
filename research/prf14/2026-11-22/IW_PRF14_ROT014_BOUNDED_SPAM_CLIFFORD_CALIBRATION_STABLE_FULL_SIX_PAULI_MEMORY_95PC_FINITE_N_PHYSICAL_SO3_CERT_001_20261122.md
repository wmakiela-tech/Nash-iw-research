---
artifact_id: IW_PRF14_ROT014_BOUNDED_SPAM_CLIFFORD_CALIBRATION_STABLE_FULL_SIX_PAULI_MEMORY_95PC_FINITE_N_PHYSICAL_SO3_CERT_001_20261122
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
scientific_class: SOURCE_RESTRICTED_QUBIT_CAUSAL_PAULI_COMB / SIX_INDEPENDENT_HIDDEN_FOURIER_PARAMETERS / NONIDEAL_PREPOST_CONTROL / BOUNDED_PREP_AND_MEAS_SPAM / CONCENTRATION / CALIBRATION_STATISTICS_TRADEOFF
status: ORIGINAL_ROT013_SOURCE_CODE_REEXECUTED / NEW_ROT014_NATIVE_SO3_POVM_1600_BINOMIAL_STRESS_PASS / DETERMINISTIC_CALIBRATION_BOUND_DERIVED / PUBLIC_SOURCE_READBACK_PENDING
firstness: PRF13_ROT011_SIX_FOURIER_FIBER / PRF14_ROT010_EXACT_TWO_SIDED_GAUGE_BREAK / PRF14_ROT011_NO_UNIFORM_SAMPLE / PRF14_ROT012_ROW_FLAT_C3 / PRF14_ROT013_FULL_SIX_COORD_13_READOUT_FINITE_N / PRF14_ROT014_CALIBRATION_SPAM_BOUNDED_FOUR_WORLD_FINITE_N_EXTENSION
claim_ceiling: NOT_CALIBRATION_FREE / NOT_UNRESTRICTED_PROCESS_TENSOR / NOT_NEW_PHYSICAL_HARDWARE_RESULT / NOT_STATISTICAL_MINIMAX_OPTIMAL / NO_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# PRF14 ROT014 — A source-exact calibration-error budget for six-coordinate two-time Pauli-memory tomography

## 0. Scientific question, actually reopened sources and result

ROT013 recovered all six genuinely independent Pauli-Fourier correlation parameters and an UNKNOWN stable middle Bloch rotation (up to legal discrete gauge), by nine selected measurements under known cyclic Clifford relative controls I,P,P², three further source coefficient measurements, and ONE known post-gate left control that breaks a fourfold source/gate alias. At an exact physical witness source with C_(j,i)=0.07...0.12, it obtained a finite-sample 95%-confidence sufficient UPPER bound N=13,273,442 binary Pauli terminal shots over 13 settings, η=0.0035 per ideal mean. Crucially it assumed ideal known controls and SPAM.

ROT014 asks the experimentally meaningful NEXT question: can the whole 13-setting theorem, including discrete branch and all six physical Fourier source parameters, survive bounded systematic errors in the relative Clifford pulse, the left gauge-breaking pulse, prepared Pauli states and binary Pauli POVM effects, while preserving finite-sample coverage? This is NOT a self-consistent, reference-free or unknown-error-bound tomography claim.

ACTUALLY reopened and REEXECUTED the ORIGINAL complete local ROT013 SymPy/NumPy source:
 /mnt/data/prf14_rot013/prf14_rot013_six_independent_pauli_clifford_13_readouts.py
Executed exact physical validity/16 positive p, six unequal C, four physical worlds, 12 indistinguishable means, distinct 13th, six-parameter error and positivity bounds, 1,000 synthetic full-protocol binomial tests — PASS. The original Git report and code retained:
https://github.com/wmakiela-tech/Nash-iw-research/blob/f2157ccf525c5452e5368a62e4ee7644d429d959/research/prf14/2026-11-22/IW_PRF14_ROT013_FULL_SIX_INDEPENDENT_PAULI_FOURIER_MEMORY_THREE_CLIFFORD_POWERS_13_READOUT_NATIVE_STATISTICAL_RECOVERY_001_20261122.md
Original full report blob fae6ed5098b5e2fe6646ac0d8da4eb48538bf6f1.
Not merely inherited from a summary.

## 1. Fixed legal source/unknown target — no silent dimension reduction

The model has exogenous classical Pauli-label joint p(v,w) on G×G with G=F₂². At each shot a first U_v acts, then the chosen deterministic physical middle single-qubit unitary, then U_w, with the pair drawn before the intervention and held intervention-independent. IID across shots within each configuration. Pauli preparation/measuring reference assumed nominally known within error budgets specified below.

The entire 16-probability distribution is determined via finite Fourier inversion by ten ordinary first/second/idle coefficients (held fixed at completely depolarizing) and SIX independent hidden off-diagonal source coefficients C_(j,i), i≠j. The baseline source coefficient matrix in (output i,input j) order is

 C0 = [[0, .09, .11], [.07, 0, .10], [.08, .12, 0]].

All six numbers are independent, specifically NOT equal row-by-row; Σ|C0_ij|=.57<1. This defines a SIX-dimensional strictly-positive legal source neighborhood. Unknown stable middle SU2 has physical Bloch matrix
 R0 = [[-3,-2,6],[6,-3,2],[2,6,3]]/7.

The four legal worlds indexed by D=diag(d1,d2,d3) with d=(+++),(--+),(-+-),(+--) have underlying gate R_D=D R0 and source C_D=D C0. Each physical p_D(v,w) has 16 strictly positive entries min 73/1600=.045625 and max 157/1600=.098125. First, second and idle channels are identical across these worlds.

Physical intended pre-gate cyclic Clifford Bloch matrix
 P=[[0,0,1],[1,0,0],[0,1,0]], P^3=I, physical SO3.
Physical intended post-gate known L:
 L=[[0,1/√2,1/√2],[1,0,0],[0,1/√2,-1/√2]], physical SO3.
The 13-configuration protocol and source-independent inversion are precisely ROT013.

## 2. NEW physical error model, equations, and source-level error transfer

For each first twelve right-relative setting (0≤t≤2), real implementation is R_D * \widetilde P^t, where \widetilde P in SO3 is an *unknown to estimator but stable* physical perturbed Clifford pulse and satisfies
 ||\widetilde P-P||₂ ≤ δ_P.
Telescoping for products of norm-one rotations yields the EXACT operator inequality:
 ||\widetilde P^t-P^t||₂ ≤ t δ_P ≤2 δ_P.
This is an ERROR PER PHYSICAL PULSE, not necessarily error of the composite P²; P² can deviate by up to 2δ_P.

For the final LEFT-relative setting the implemented gate is \widetilde L R_D with \widetilde L∈SO3 and
 ||\widetilde L-L||₂ ≤δ_L.

For each selected Pauli +j preparation, true input Bloch vector x_j is physical |x|≤1, and ||x_j−e_j||₂≤ε_p. The actual binary POVM outcome ±1 has mean b+n_i·r, where its Bloch effect vector n_i and offset b are physical (|b|+||n_i||≤1), ||n_i−e_i||₂≤ε_m, and |b|≤ε_b. These calibration imperfections may vary by setting but MUST remain stable across repeated shots; no arbitrary interventions that change the source p(v,w), no uncontrolled time drift. An ideal source input-output Bloch transfer for one fixed middle rotation S is the exact matrix
 T_ij(S)=C_(j,i) S_ij
for the entire Pauli basis including diagonal entries, with diagonal C_(i,i)=0 in this particular source.
Because T(S) is a convex mixture of SO3 matrices D(w) S D(v), it is a physical unital channel transfer and ||T(S)||₂≤1.

One actual Pauli terminal expectation is
 m_actual = b + n_i^T T(S_actual) x_j.
Compare to ideal calibrated mean m_ideal=e_i^T T(S_ideal)e_j.
The source/channel contraction and triangle inequality imply the rigorous bound

 |m_actual−m_ideal| ≤
    |C_(j,i)| ||S_actual−S_ideal||₂
    + ε_p+ε_m+ε_b.

Crucial technical distinction: C_(j,i) multiplies ONLY the calibrated-axis GATE error term; preparation and measurement axis errors can couple to OTHER matrix elements of T, and therefore are bounded using ||T||₂≤1, NOT using the artificially smaller |C_(j,i)|. This avoids a physically invalid undercount of SPAM.

With c_max=max_ij |C_ji|=.12 across all four physical sources, a uniform all-thirteen-configuration bound is

 μ = max{2c_max δ_P,c_max δ_L} + ε_p+ε_m+ε_b,
 and  |m_actual^k−m_ideal^k|≤ μ for every k=1,...,13.

For empirical binary sample means \hat m_k and independent sampling event
 | \hat m_k−m_actual^k |≤η_stat all k,
we therefore have simultaneously | \hat m_k−m_ideal^k |≤e, where e=η_stat+μ.
No independence of the *systematic* errors is required, only their deterministic boundedness and their within-setting stability.

## 3. NEW right-only gauge invariant even under incorrectly realized right controls

ROT013 showed all twelve ideal right-relative mean distributions are identical for the four actual legal source/gate worlds. ROT014 strengthens this algebraically: for ANY real 3x3 matrix Q and all i,j,

 [D C0]_ij [D R0 Q]_ij = C0_ij [R0 Q]_ij,

because d_i²=1. The equality is entry-by-entry of the FULL Bloch channel matrix T, not only one projected ideal Pauli mean. It thus remains exact for any physical miscalibrated right-control \widetilde P^t, and even with a common imperfect preparation/measurement SPAM reference: all right-only 12 outcome laws are indistinguishable across the four physical source/gate worlds as long as controls/SPAM themselves are common across worlds. The left control still contains the only source/gate discriminating information in this source witness. This is NOT a claim that controls varying adversarially differently depending on unknown D remain uninformative.

SymPy ACTUALLY verified the full identity against a matrix of nine algebraically independent symbols Q_ij, for all four D and all nine channel matrix elements, plus source positivity.

## 4. NEW deterministic full-estimator calibration tolerance and exact decision radius

ROT013's proven estimator maps the first nine selected empirical means into three vectors z_i, with source a_i=||z_i||=(.09,.10,.12), normalizes the rows, uses three remaining measurements to infer the other independent source coefficients, and chooses one of the four D signs by comparing an empirically measured thirteenth left-control Pauli mean with four data-predicted candidates.

For ANY thirteen errors bounded by e, irrespective of which are statistical and which are systematic, the old source-exact proof gives normalized row error bounds

 ρ_i(e)=2√3 e/a_i.

Let G=9/(7√2), E_G(e)=(ρ_Y+ρ_Z)/√2, E_a(e)=√3 e. The final candidate prediction error obeys

 E_pred(e)=E_a(e)[G+E_G(e)]+a_X E_G(e).

True last-control four-world mean gap is Δ=27√2/700≈.05454823740581938.
Thus nearest candidate branch is rigorously right for EVERY such perturbation whenever

 F(e)=Δ−2[E_pred(e)+e] >0,

and the sign and denominator guards hold ρ_i(e)<(6/7,2/7,3/7)_i.
The exact F(e) here is a quadratic in e:
 E_pred(e)=A e+B e²,
 A=5.616330053095716, B=77.78174593052023.
So e is admissible if
 2B e²+2(1+A)e<Δ.

The unique positive boundary from this sufficient condition is
 e_crit=0.0039397683823995...
For e<ecrit, the row orientation tests and all three extra 6/7-pivot denominator tests also pass. IMPORTANT: this is a PROVEN SUFFICIENT RADIUS for this estimator and THESE FOUR sources. It is not the true minimax breakdown point of any tomography strategy and does not imply experimental impossibility for e>=ecrit.

For all four worlds, six correlation errors obey:
 selected i: |ΔC_i,selected|≤√3 e;
 remaining i: |ΔC_i,other| ≤ [e+|C_i,other|ρ_i(e)]/[6/7−ρ_i(e)].
Hence each Fourier-inverted source probability is within
 E_p(e)=[3√3 e+Σ_i E_other,i(e)]/16
of its true p_D, and thus is still a STRICTLY POSITIVE normalized physical source whenever E_p(e)<73/1600. Under the two explicit scenarios below it is.

An optional physically legal middle gate can be recovered by taking the nearest SO3 rotation (proper orthogonal Procrustes/SVD) of the raw candidate row matrix \hat R. Let R_*∈SO3 be the true gate: by nearest-point minimality, ||R_projected−R_*||_F≤2||\hat R−R_*||_F≤2 (Σ_iρ_i²)^(1/2). This gives a LEGAL gate estimate with a necessarily conservative quantitative error bound. It does not assert the projected gate and estimated source exactly reproduce all noisy observed means, or become SPAM self-calibrated.

## 5. TWO actually evaluated 95% finite-shot calibration scenarios

Given deterministic μ, choose a positive statistical tolerance η_stat with e=η_stat+μ<ecrit. Classical concentration for the ±1 outcomes of the actual imperfect but stable apparatus is
 Pr(max_k |hat m_k−m_actual^k|>η_stat)≤26 exp(−n η_stat²/2).
Thus all deterministic source/branch/positivity conclusions hold with ≥95% joint probability for
 n≥ceil[2 ln(26/.05)/η_stat²] repeated samples per each of the 13 settings.

Scenario A — NO EXTRA SHOTS versus ROT013 while ALLOWING nonzero calibration error:
- one right Clifford P physical pulse δP≤.001 in SO3 operator norm; post-gate L δL≤.001. P² generated by TWO real P pulses, composite bound .002;
- ε_p,ε_m,ε_b ≤0.00005 EACH;
- worst systematic μ=max(2*.12*.001,.12*.001)+3*.00005=.00039;
- same ROT013 sampling η_stat=.0035; effective e=.00389<ecrit.
- n=1,021,034 per setting and total N=**13,273,442 shots**, guaranteed joint misclassification probability ≤.05;
- deterministic margin F(e)=.0007191872775443>0;
- all six source coordinates bounded, each |ΔC|≤0.029 approximately and true source p stays positive, with certified reconstructed p_min≥.0403300166956;
- physical nearest SO3 gate Frobenius error upper ≤.461244097, admittedly loose.

Scenario B — TWICE as loose SPAM axis/bias error budgets, modest statistical cost:
- same δP=δL=.001;
- ε_p=ε_m=ε_b=.0001 EACH;
- μ=.00054; choose η_stat=.00296, so e=.0035, not merely below the exact critical ecrit;
- n=1,427,555 per setting, total N=**18,558,215 shots**;
- same source-exact branch-decision margin ROT013 F(e)=.0063282742588516;
- certified source p_min≥.0409280167479;
- physical nearest SO3 gate Frobenius error upper ≤.415001116.

Both scenarios are SOURCE-SPECIFIC 4-world confidence statements with all six independent coefficients, not generic six-dimensional parameter-space uniform inference. The actual shot costs are proof-derived sufficient UPPER bounds, not optimized statistical design. Both calibration budgets are exceptionally tight in practice (δP=.001 corresponds to about 0.057 degrees Bloch angle), with no device evidence establishing attainability.

A GENERAL source-specific calibration/statistics Pareto frontier follows algebraically:
 for 0≤μ<ecrit and any 0<η_stat<ecrit−μ,
 N_suff(μ,η_stat)=13 ceil[2ln(520)/η_stat²].
The strict inequality matters; at equality F=0 there is no positive decision margin. There is NO positive finite sample certificate from THIS proof when μ≥ecrit, but that is NOT an experimental impossibility theorem.

## 6. Actually executed physics-consistent synthetic error tests

Native independent extension, Python 3.13 SymPy/NumPy/SciPy, actually executed in the local container:
 /mnt/data/prf14_rot014/rot014.py
 SHA256: 3489087965baf09036706640b7039d5111733c40a5b921a6385b4156d08cab42.

Certificate actually created by this execution:
 /mnt/data/prf14_rot014/prf14_rot014_bounded_calibration_certificate.json
 SHA256: f887d0ce159bd7db437da1d384b2de217fd70129540a9ab4a3a150a889d0b5f1.

Actual program checks, not just claims:
- all three nominal SO3 matrices and all four 16-way positive p sources;
- 4×9 symbolic exact equality of FULL Bloch transfer channel T(D C, D R Q)=T(C,R Q) for arbitrary common right control Q with nine independent symbolic entries, including physical miscalibrated P^t;
- exact ROT013 four final left-control means and Δ;
- all deterministic numerical inequalities, ecrit, two 95% Hoeffding ceilings, source positivity and nearest physical SO3 gate error;
- TWO independently generated physically legitimate faulty apparatus ensembles: implemented Ptilde=E_P P and Ltilde=E_L L with true SO3 random rotations E; preparation vectors x physical unit Bloch vectors deviating ≤ε_p; measured binary POVM has bias b and effect Bloch n with |b|+||n||=1 and deviation ≤ε_m. For each 13 setting its actual physical mean is computed as b+n^T(C_D⊙R_actual)x; the source p and 2-time gate remain legal;
- 4 physical worlds ×200 independent full 13-setting synthetic binomial-count shots for each of TWO scenarios, 800+800=**1600** complete synthetic experiments; 0 model misclassifications in either scenario. Worst observed actual-vs-nominal mean bias .000135183 (A) and .000156532 (B), below respective worst-case upper caps μ=.00039 and μ=.00054. Max recovered source-coefficient errors .004199386(A), .004304216(B), source p estimated minimum .04504996(A), .04520819(B). They are ACTUAL RNG sampling from the model, not observations on a quantum computer. 0/1600 does not prove a 100% success rate.

Native execution stdout was captured and checks passed. The analytic deterministic/calibration plus Hoeffding proof, not just random stress, establishes the 95% conditional guarantee.

## 7. Current original literature and novelty/claim guard

Primary source near prior actually opened this rotation:
Zitai Xu, Guoding Liu, Senrui Chen, *SPAM-robust learnability of quantum dynamics*, arXiv:2611.05561v1, posted 3 November 2026,
https://arxiv.org/abs/2611.05561 .
Its abstract explicitly treats unknown SPAM gauge and shows coherent physical structure can reduce continuous freedom to discrete, with explicit protocols; **we used the ABSTRACT, not a line-by-line read of the entire paper**. ROT014 is NOT SPAM-robust in that stronger reference-free meaning: it ASSUMES externally known numerical upper bounds ε_p,ε_m,ε_b. Do not present this as a replacement for established gate-set tomography.

Other direct near host:
- *Efficient Self-Consistent Learning of Gate Set Pauli Noise*, PRX Quantum 7, 010305 (2026), DOI https://doi.org/10.1103/1pnv-t9px.
- *Disambiguating Pauli Noise in Quantum Computers*, PRX Quantum 7, 033045 (2026), DOI https://doi.org/10.1103/69wc-gzl6.
- *Quantum Process Tomography with Digital Twins of Error Matrices*, Phys. Rev. Lett. (2025), DOI https://doi.org/10.1103/dpgy-rtxr, mature SPAM-aware QPT design.
The present finite source-family error composition is a controlled inverse/perturbation problem, not a first discovery of SPAM error, calibration theory, finite-sample tomography, or quantum memory physics. NO_EXTERNAL_NOVELTY.

## 8. Current NASH B1 and coordination, different owner

Before theoretical work PRF14 consulted #iw-dispatch (22 Nov 12:39+) and noted Moderator's release of REVIEW091 original HOLD (r4), Badacz REVIEW098 of historically unspecified Herwig table provenance, Mech-S10 ROT013 90 source ratios, INT10 ROT017 full-mass extrapolation falsification, KN15 custody. No source change in those B1 entries changes this independent PRF14 qubit model. NO new independent LINX/BlackHawk/BBN native physics execution, no PBH physical bound and no B1 firstness claim.

## 9. High-priority independent referee falsifiers

1. Verify the source-gate right-only alias at the FULL transfer-matrix level for generic miscalibrated right control and common imperfect SPAM, not just twelve ideal Pauli axes.
2. Verify SPAM contraction argument, especially preparation/measurement error terms are NOT suppressed by cmax, physical POVM |b|+||n||≤1, and control P² inherits tδP rather than δP.
3. Verify the exact ecrit positive root and strict margin for A, B; redo η-stat and union Hoeffding ceilings 13,273,442 / 18,558,215; check all six C and source p positivity.
4. Independently rerun physical SO3/POVM synthetic ensemble from attached source and test adversarial bounded nonrandom errors saturating ecrit.
5. Challenge whether some unverified control-to-environment coupling, drift or SPAM condition makes the fixed exogenous p model fail. In that case these claims become inapplicable; a hardware falsifier would be source dependence on intervention, not a failure of the algebra.
6. Source-first novelty subtraction against full Xu/Liu/Chen preprint and 2026 self-consistent work must precede any novelty claim.

FINAL:
PRF14_ROT014 / ROT013_ORIGINAL_SOURCE_DIRECT_REEXEC_PASS / FULL_SIX_INDEPENDENT_PAULI_SOURCE / MIS-CALIBRATED_RIGHT_CONTROL_ARBITRARY_Q_FOUR_WORLD_ALIAS_PASS / PHYSICAL_PREP_POVM_OPERATOR_NORM_CALIBRATION_BOUND_PASS / CRITICAL_TOTAL_MEAN_ERROR_0P0039397683824 / NONZERO_CALIBRATION_SAME_13P27M_SHOT_95PC_CERT_PASS / LARGER_SPAM_18P558M_SHOT_95PC_CERT_PASS / FOURIERSOURCE_POSITIVE / NEAREST_PHYSICAL_SO3_BOUND / 1600_PHYSICAL_MODEL_BINOMIAL_SIM_PASS / NO_GENERAL_REFERENCE_FREE_SPAM_CLAIM / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
