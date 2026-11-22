---
artifact_id: IW_PRF14_ROT013_FULL_SIX_INDEPENDENT_PAULI_FOURIER_MEMORY_THREE_CLIFFORD_POWERS_13_READOUT_NATIVE_STATISTICAL_RECOVERY_001_20261122
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
science: ORIGINAL_SOURCE_RESTRICTED_CAUSAL_TWO_TIME_PAULI_COMB / SIX_INDEPENDENT_FOURIER_COORDINATES / UNKNOWN_MIDDLE_SU2 / THREE_CYCLIC_RIGHT_CLIFFORD_POWERS / ONE_LEFT_GAUGE_BREAK / 13_BINARY_EXPECTATIONS
status: EXACT_SYMPY_SOURCE_PHYSICALITY_AND_INVERSION_PASS / LOCAL_1000_ACTUAL_BINOMIAL_COUNT_SIMULATIONS_PASS / DETERMINISTIC_AND_HOEFFDING_FINITE_N_CERT_PASS / EXTERNAL_REFEREE_PENDING
firstness: PRF13_ROT011_SIX_FOURIER_FIBER / PRF13_ROT012_KNOWN_GATE_OPTIMAL / PRF14_ROT005_UNKNOWN_GATE_ALIAS / PRF14_ROT010_TWO_SIDED_CONTROL_EXACT / PRF14_ROT011_FULL_13_FINITE_N_CONSERVATIVE / PRF14_ROT012_ROW_FLAT_CYCLIC_CLIFFORD / PRF14_ROT013_GENERAL_SIX_COORDINATE_THREE_POWER_EXTENSION
claim_ceiling: NO_UNRESTRICTED_QUANTUM_PROCESS_TENSOR / NO_SPAM_SELF_CALIBRATION / NO_ADAPTIVE_OR_GLOBAL_SAMPLE_COMPLEXITY_OPTIMALITY / NO_HARDWARE / NO_PRIOR_ART_CLEARED_NOVELTY / NO_PBH_BRIDGE / NO_CANON / NO_EXEC_SIGN
---

# PRF14 ROT013 — Six independent Pauli-memory correlations: three powers of one known cyclic Clifford and thirteen scalar tests recover an unknown middle gate and the whole invisible six-dimensional source

## Executive finding and novelty discipline

PRF14 ROT012 found a radically better, ten-setting, 832150-shot *conditional row-flat* two-time Pauli-source experiment, but fixed the strong assumption C_(j,i)=c_i for both j≠i; that source has only three hidden Fourier degrees of freedom. ROT013 removes that extra promise. For an original source with SIX INDEPENDENT nonzero off-diagonal coefficients and an unknown stable physical middle SU2 gate, use the three **known** right-relative control choices I, P, P² (one cyclic Clifford P³=I), and one known left-relative control L. NINE source measurements acquire one chosen off-diagonal Pauli label per output row across the three cyclic settings, reconstructing a scaled full row of unknown R. THREE additional scalar settings recover the other three independent coefficients. A final THIRTEENTH Pauli expectation removes the last fourfold source/gate sign ambiguity for the explicitly constructed source.

The complete data comprise 13 IID binary Pauli expectation configurations. In the source-specific constructed six-independent-parameter physical witness, the first twelve binary laws are exactly indistinguishable among FOUR different valid source/gate worlds, while the thirteenth yields FOUR different means. A rigorous uniform-over-all-thirteen-empirical-mean-errors η=0.0035 box, combined with a classical Hoeffding union bound, certifies **95% success with 1,021,034 trials per setting; 13,273,442 trials total**. On the same concentration event, it bounds all six recovered correlations and guarantees the Fourier-inverted 16-entry source probability distribution remains positive. 1000 independently seeded binomial-count synthetic whole-protocol simulations all passed. THESE ARE MATHEMATICAL AND SYNTHETIC RESULTS, NOT DEVICE EXECUTION.

ROT011's earlier 33,183,581,457 sufficient-shot number was a very conservative bound for another 13-setting cross-product estimator. The ratio of two SUFFICIENT upper bounds is approximately 2500; neither number is a quantum information lower bound, and the present source-specific finite-n estimate is not uniform over ALL R,C. ROT012's more favorable 832150-shot certificate still required the stronger row-flat model. No source-free physical novelty or general GST priority is claimed.

## 1. Primary internal source and firstness

The exact source PRF13 ROT011 original Git blob a238cafeba30a667ad634bf5ab3725a16df1f84e, actually reopened for this scientific line:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf13/2026-11-12/IW_PRF13_ROT011_SIX_DIMENSION_PAULI_HIDDEN_MEMORY_TOMOGRAPHY_PUBLIC_RETURN_001_20261112.md

PRF14 ROT010 original exact physical fourfold known-right-control alias with 13 precise expectations (blob 2e10001d834781a93fed954ff635b5bd422ebdfb):
https://github.com/wmakiela-tech/Nash-iw-research/blob/2925adf3e8e436a0101d46a2edfdc7c00f59e621/research/prf14/2026-11-21/IW_PRF14_ROT010_RELATIVE_TWO_SIDED_CONTROL_13_EXPECTATION_PAULI_MEMORY_SELF_CALIBRATION_DISCRETE_GAUGE_AND_OPTIMAL_SINGLE_PROBE_001_20261121.md

PRF14 ROT011 full 13-setting finite sample but poor conditioning:
https://github.com/wmakiela-tech/Nash-iw-research/blob/187ace16b1ba163e4c4d5f04b209950967741a4a/research/prf14/2026-11-22/IW_PRF14_ROT011_FINITE_SHOT_TWO_SIDED_PAULI_MEMORY_CERTIFICATE_AND_NO_UNIFORM_SAMPLE_THEOREM_001_20261122.md

PRF14 ROT012 row-flat source-only shortcut, ORIGINAL DIRECTLY REOPENED local SymPy code and machine certificate:
https://github.com/wmakiela-tech/Nash-iw-research/blob/579065c091824081ff14fd262614053774fec994/research/prf14/2026-11-22/IW_PRF14_ROT012_CYCLIC_CLIFFORD_ROW_FLAT_PAULI_MEMORY_TEN_SETTING_STATISTICAL_RECOVERY_AND_MODEL_MISSPEC_FALSIFIER_001_20261122.md

This turn uses genuine six-independent-source mathematics, not another ROT012 row-flat rephrasing. It does NOT take internal priority over PRF13's original causal Pauli comb model, six-dimensional Fourier fiber, or ROT010's four-source unknown gate alias.

## 2. Exact legal two-time Pauli source and observation law

For two Pauli labels v,w in G=F2², with U_v=X^x Z^z, independently initialize each run according to a stable joint classical probability p(v,w). Apply first U_v, then chosen deterministic middle unitary V with physical Bloch R(V) in SO3, then U_w, and terminal binary ±1 Pauli measurement after Pauli eigenstate preparation. The joint distribution p is exogenous and independent of the chosen middle intervention; runs are IID. This is a legitimate CP causally ordered two-time source comb, but not any general environment-quantum-memory comb and not a SPAM-free implementation.

With Pauli-conjugation signs χ_X(x,z)=(-1)^z, χ_Y(x,z)=(-1)^(x+z), χ_Z(x,z)=(-1)^x, define C_(j,i)=Σ_v,w p(v,w)χ_j(v)χ_i(w). When first, second, and idle endpoint channels are all equal to completely depolarizing, all ten ordinary Fourier coordinates are fixed and **exactly six** off-diagonal C_(j,i) (i≠j) remain. Their source distribution is given by Fourier inversion:
p(v,w) = [1+Σ_(i≠j) C_(j,i)χ_j(v)χ_i(w)] /16.
Any six real coordinates with Σ|C_(j,i)|<1 provide a legal STRICTLY POSITIVE source; this open six-dimensional coefficient region is not row-flat, three-dimensional or otherwise frozen.

For a deterministic middle rotation R, prepare +Pauli_j, measure terminal Pauli_i:
T_ij(R) = C_(j,i) R_ij, i≠j.
This law is exact, source-restricted, and inherited with firstness from PRF13 ROT011.

## 3. NEW generic six-coordinate constructive inversion theorem: 3 cyclic Clifford powers

Let P be the known proper SO3 Pauli-coordinate cycle
P=[[0,0,1],[1,0,0],[0,1,0]], with P³=I, det P=+1, PᵀP=I.
Every P^t, t=0,1,2, is a physical single-qubit Clifford gate (up to global phase). The laboratory control is placed immediately BEFORE the unknown stable V, so the middle physical Bloch matrix is R P^t, not P^t R. The two noise events remain at their original places.

For each Pauli output i∈{X,Y,Z}, select one DIFFERENT input j_i≠i for which C_(j_i,i)≠0. At all t=0,1,2, measure the three means
m_i(t)=C_(j_i,i) (R P^t)_(i,j_i).
As t runs over 0,1,2, the columns P^t e_(j_i) visit ALL THREE basis vectors e_k once. Hence merely rearranging the three measured scalars gives a genuine FULL 3D ROW VECTOR
z_i = C_(j_i,i) (R_iX,R_iY,R_iZ).
Then a_i=||z_i||=|C_(j_i,i)|>0, u_i=z_i/a_i is an oriented-or-reflected row of R. Let U have these three u rows. Since R∈SO3 and all source selected coefficients are nonzero, U∈O3 exactly, with det U=±1. The physical unknown R must be R_D=D U where D is a diagonal sign matrix with det D=det U. There are EXACTLY FOUR algebraic sign candidates; sign-flipped sources C^D_(j,i) are correspondingly redefined. Whether all four are legal depends on source positivity. Inside the open region Σ|C|<1, all four are strictly positive legal source histories, so the fourfold right-control-only alias is PHYSICAL, not a calibration convention to ignore.

One extra observed Pauli mean for EACH of the three remaining off-diagonal source coefficients (i,j≠j_i) suffices to recover that coefficient as m_(i,j,t)/[R_D P^t]_(i,j), provided the chosen matrix element is nonzero. Because an SO3 row has at least one nonzero component and the cyclic powers traverse all 3, one may choose a nonzero pivot. No equality of the two source coefficients in a row is assumed. This gives 3*3+3=TWELVE scalar observable configurations for recovery of the gate/source modulo four sign choices.

ALL right-relative interventions RQ, no matter how many, retain the exact fourfold alias R→D R, C_(j,i)→d_i C_(j,i), because RQ has the same row signs. To break the alias, a known LEFT-relative control L after unknown V is necessary in this set-up if no other calibrated/known independent information is available. A single chosen left-probe may or may not split all four candidates; a nonzero distinct-mean condition is required for that specific left-probe. This is not a claim that ONE final probe works for every physical source and R.

## 4. Explicit original strict-positive source, six genuinely independent coordinates, four legal worlds

Take baseline physical unknown unitary Bloch rotation
R0=(1/7)*[[-3,-2,6],[6,-3,2],[2,6,3]].

The original six independent Fourier source coefficients are:
C_(Y,X)=9/100, C_(Z,X)=11/100,
C_(X,Y)=7/100, C_(Z,Y)=10/100,
C_(X,Z)=8/100, C_(Y,Z)=12/100.
They are DIFFERENT in EVERY source row: C_(Y,X)≠C_(Z,X), C_(X,Y)≠C_(Z,Y), and C_(X,Z)≠C_(Y,Z). The sum of their absolute values is 57/100<1, proving an open legal neighborhood with six freely variable coefficients.

Define D0=diag(+,+,+), D1=diag(−,−,+), D2=diag(−,+,−), D3=diag(+,−,−), each det+1. Physical world D has unknown R_D=D R0 and SIX Fourier coefficients C^D_(j,i)=d_i C^0_(j,i). For each world, exhaustive exact SymPy inversion of all 16 p_D(v,w) gives:
minimum p_D = 73/1600 = 0.045625,
maximum p_D =157/1600=0.098125,
sum p_D=1, and ALL first/second/idle nonzero Pauli Fourier values are exactly zero.
Thus four fully physical stable unitary+noise source worlds with identical ordinary channels are demonstrated. They are distinguished by the legal later intervention, so not asserted to be physically equivalent.

Take the selected input per row (j_X,j_Y,j_Z)=(Y,Z,Y). For each selected j, run t=0,1,2 controls P^t. This gives nine source readouts. Choose three extra configurations:
- output X, input Z, t=0: pivot R0_XZ=6/7, coefficient C_(Z,X)=11/100;
- output Y, input X, t=0: pivot R0_YX=6/7, coefficient C_(X,Y)=7/100;
- output Z, input X, t=1: pivot R0_ZY=6/7, coefficient C_(X,Z)=8/100.
All three omitted independent source coordinates use large stable 6/7 pivots rather than weak matrix elements.

The TWELVE common exact means of the four distinct worlds, in measurement order (first three X row, next three Y, next three Z, three omitted coefficients):
-9/350, 27/350, -27/700,
1/35, 3/35, -3/70,
18/175, 9/175, 6/175,
33/350, 3/50, 12/175.
SymPy verified bit-for-bit exact equality for all four world families. No finite number of repetitions of precisely those twelve configurations can classify D.

Known left-relative control L after unknown V:
L=[[0,1/sqrt2,1/sqrt2],[1,0,0],[0,1/sqrt2,-1/sqrt2]].
A real proper orthogonal rotation, therefore physical SU2. Thirteenth measurement: input +Y and final output X, middle L R_D. Exact means across D0,D1,D2,D3:
+27 sqrt2 /1400, -81 sqrt2 /1400, +81 sqrt2 /1400, -27 sqrt2 /1400.
The minimum pairwise mean gap is exactly Δ=27 sqrt2/700=0.05454823740581938. The four distinct positive physical worlds are now fully identified at the level of exact scalar expectations.

## 5. NEW 13-setting full-six-coordinate finite-shot theorem, without the ROT012 row-flat promise

Each scalar configuration yields IID Bernoulli ±1 output with independently repeated preparations. For the explicitly fixed six-coordinate source and four legal D-worlds, assume all THIRTEEN empirical expectations lie within absolute η=0.0035 of their true values. We prove that a concrete continuous-source-and-discrete-gate estimator then recovers (i) correct D and (ii) every one of the six source coefficients with a numerical nonasymptotic upper error bound.

Rearrange nine selected mean estimates into \hat z_i. The Euclidean vector error obeys ||\hat z_i−z_i||≤sqrt3 η. Their true nonzero row norms are a=(0.09,0.10,0.12), giving \hat a_i=||\hat z_i|| and
|\hat a_i−a_i|≤sqrt3 η=0.006062178...
For each normalized row, with proper canonical row sign (the original R0 has positive third entry 6/7,2/7,3/7), the standard normalization triangle bound gives
||\hat r_i−r_i||₂≤ρ_i=2sqrt3 η/a_i.
Explicitly:
ρ_X ≤0.134715063,
ρ_Y ≤0.121243557,
ρ_Z ≤0.101036298.
These are less than the relevant positive third-row entries, hence the canonical-sign convention is stable; these estimates do NOT say the raw noisy row matrix is EXACTLY SO3. A physical nearest-SO3 projection is a separate, optional continuous estimate, not needed for the source coefficient and branch results.

For the final left X-from-Y probe use only the selected row-X source amplitude \hat a_X plus canonical row-Y and row-Z column Y:
\hat t_D=d_X \hat a_X [d_Y \hat r_(Y,Y)+d_Z \hat r_(Z,Y)]/sqrt2.
For the actual source, G=(|R0_(Y,Y)|+|R0_(Z,Y)|)/sqrt2=9/(7sqrt2), E_G=(ρ_Y+ρ_Z)/sqrt2, E_a=sqrt3 η. For each D, by triangle inequality:
|\hat t_D−t_D|≤E_a (G+E_G)+a_X E_G = E_pred ≤0.020609982.
The observed final measurement is independently η-close to t_D; thus nearest-four-candidate classification is GUARANTEED correct for all such thirteen errors if
2(E_pred+η)<Δ.
Here 2(E_pred+η)=0.048219963 < Δ=0.054548237, with positive margin **0.006328274**.

For each of the three additionally observed coefficients, use their physically chosen pivot |R0_i,k|=6/7 and the same estimated row. A direct ratio stability bound after the correct D sign classification gives
|\hat C_other−C_other|≤[η+|C_other|ρ_i]/[(6/7)−ρ_i].
For the extra three:
C_(Z,X): error ≤0.025357077;
C_(X,Y): error ≤0.016288980;
C_(X,Z): error ≤0.015319143.
The three selected coordinates each have error ≤0.006062178. Thus **ALL SIX INDEPENDENT hidden Fourier coefficients are estimated with deterministic individual absolute errors ≤0.025358** under the event. This is a source-specific quantitative error bound, not just correct categorical choice.

The exact 16-valued Fourier inversion is linear. With all six coefficient errors bounded, each resulting source probability error is ≤(sum of six abs coefficient error bounds)/16=0.004696984. Since the smallest true p among four worlds is 73/1600=0.045625, the reconstructed p distribution has strictly positive minimum >0.040928. Normalization Σp=1 is automatic by character orthogonality; the estimated finite-shot source is therefore still a legal classical probability distribution on this event. Under noise, the raw row estimates may need an SO3 projection for a strictly physical point estimate of the gate, without changing the discrete classification and source Fourier bounds proved here.

By Hoeffding for ±1 mean outcomes:
Pr(|hat m_i−m_i|>η)≤2exp(−n η²/2).
Union over all 13 settings:
Pr(any abs mean error >η)≤26 exp(−n η²/2).
Taking n=ceil[(2/η²)ln(26/0.05)] = **1,021,034 repetitions per setting** makes this ≤0.05 (actual bound approximately 0.049999778). So at least 95% model-conditional confidence is certified for:
N_total=13n=**13,273,442 binary terminal Pauli shots**,
with correct sign branch, all six source coefficient error bounds, and legal positive reconstructed source.

The comparison ROT011 33,183,581,457 / 13,273,442 ≈ 2500 times reflects two explicit Hoeffding sufficient upper bounds on different estimators. ROT013 does NOT assume row-flat C, unlike ROT012, and thus closes its immediate mathematical source-dimension restriction. Still there is NO uniform finite-n over arbitrary R or arbitrarily weak C: the ROT011 c→0 nonuniform no-go survives. No global experimental optimality, no realistic preparation/measurement overhead and no uncalibrated SPAM model are claimed.

## 6. Actually executed science and tests

Original reproducible LOCAL Python3.13 SymPy exact / NumPy script, ACTUALLY EXECUTED to completion:
 /mnt/data/prf14_rot013/prf14_rot013_six_independent_pauli_clifford_13_readouts.py
SHA256 db8b818a840d793657afd2c7072fe3258da31f7173fa68ab193e652897cbf7aa.
Its actual stdout file:
 /mnt/data/prf14_rot013/prf14_rot013_native_stdout.txt
SHA256 353b8b84dde9ec051cb9afb757551e4ea13192f615139ff6e920bde144ebe618.

Original exact and finite-n machine certificate:
 /mnt/data/prf14_rot013/prf14_rot013_six_independent_pauli_finite_sample_certificate.json
SHA256 a9f11bc102c8b33d5c87d0d2bb49a3f055aaedb1407f2c5846b386f1bd131ca6.

ACTUAL executed program checks:
- all three physical SO3 rotations legal and proper, cyclic P³=I;
- six independent row-unequal Fourier coordinates, all four 16-source distributions strictly positive;
- complete first/second/idle channel equality in all worlds;
- exact twelve identical scalar means, exact four thirteenth means, four distinct pairwise gaps;
- exact inverse of all six source coefficients and physical R for all four zero-noise worlds;
- deterministic η=0.0035 row, coefficient, gate-choice, source positivity and Hoeffding numerical inequalities;
- independent NumPy seeded 4*250=1000 complete 13-measurement synthetic BINOMIAL-COUNT trials, n=1,021,034 per configuration, all 1000 correct classifications. Observed worst source-coefficient absolute error .004984, observed worst physical row L2 error .041146, smallest correct-vs-next candidate distance margin .046635.
These synthetic binomial draws are efficient equivalent-count simulations, NOT 13.27 billion or million actual quantum device trials, NOT independent physical I1, and no quantum hardware access was used. The mathematical proof, not the 1000 simulations, establishes the whole η-box guarantee.

## 7. Independent external prior art currentness: CRITICAL November 2026 source

Generic qubit Pauli noise learnability, SPAM/gauge freedom, Clifford experimental design and concentration inequalities are mature and do not receive a priority claim from this report.

New especially close contemporary source FIRST VERIFIED this rotation:
Zitai Xu, Guoding Liu, Senrui Chen, **SPAM-robust learnability of quantum dynamics**, arXiv:2611.05561v1, submitted **3 November 2026**, https://arxiv.org/abs/2611.05561 . The directly verified author preprint abstract says coherent structure reduces continuous SPAM gauge freedom to discrete or trivial choices; it develops more general channel/Lindbladian learnability and explicit protocols. This is a highly relevant near host to our different, earlier PRF13 specialized two-time correlated-exogenous Pauli source/gate reconstruction. Only ABSTRACT and metadata verified; its full 81-page proof was NOT reviewed line by line in this turn. Consequently do not claim its theorem includes, excludes, or anticipates this particular 13-readout comb witness; source comparison demands external specialized review. BUT it definitively defeats a broad generic novelty statement such as "first use of coherent unitary constraints to break a continuous Pauli/SPAM ambiguity."

Verified journal primary sources:
- Senrui Chen et al., **Efficient Self-Consistent Learning of Gate Set Pauli Noise**, PRX Quantum 7, 010305, 9 January 2026, https://doi.org/10.1103/1pnv-t9px. General Pauli gate-set gauge and learnability graph framework mature.
- **Disambiguating Pauli Noise in Quantum Computers**, PRX Quantum 7, 033045, 3 September 2026, https://doi.org/10.1103/69wc-gzl6. Gate-set Pauli noise characterization on processors up to 92 qubits, source/model distinct from our two-time comb, but experimental Clifford gauge and sample overhead mature.
- **The Learnability of Pauli Noise**, Nature Communications 14, 52 (2023), https://doi.org/10.1038/s41467-022-35759-4. Gauge learnability from Clifford graph cycle/cut space mature.

The specific finite group Fourier inversion and calibration geometry in ROT013 are elementary source calculations. Even if this exact 13-setting witness is not recorded verbatim in previous papers, this does NOT establish external novelty.

## 8. Parallel currentness and scientific governance

B1 remains a distinct owner research program; source firstness and execution to Badacz/Mech/other cells. At 22 Nov 10:33 CET, owner Badacz REVIEW095 real 232 Julia +233 network native results with modern PYTHIA8.318 / Herwig7.3 produced dmod .1315... .2283 dex over three replicates/solver tests. Source actually reopened Git blob 177d9df89dcb4f63acdeedd2879bc062dafa0f51:
https://github.com/wmakiela-tech/Nash-iw-research/blob/9a0220809f2c69aad0b7b245b701812d05b57263/research/badacz/2026-11-22/IW_BADACZ_B1_MODERN_GENERATOR_REPLICA_TRANSFER_REVIEW_095_20261122.md
22 Nov 11:58 owner newer REVIEW098 message: historical Herwig table vintage provenance still unverified, Moderator releases original REVIEW091 HOLD but not physical PBH limit. This PRF14 rotation did not run original BlackHawk or LINX and does not create a PBH bound.

## 9. Required independent falsification and remaining limits

Referee should first verify exact source/gate legal causality, source-positive 4-world distributions, all 12 identical ±1 laws and one distinct left-control statistic. Next independently verify source-dimensional recovery (all SIX row-unequal C), correct t=0/1/2 Clifford column routing, and the last three source pivots 6/7. Statistically challenge the normalization bound, exact 95%-Hoeffding ceiling, all six C bounds, source positivity and separate gate-projection caveat. Seek adversarial 13-mean perturbations saturating η-box, rather than viewing 1000 friendly simulations as proof.

Further open:
1. Compare with FULL 81-page Xu–Liu–Chen November 2026 theorem; abstract-only is not sufficient to assign novelty.
2. SPAM reference error and control-dependent source p(v,w): current claim does not cover.
3. For generic R with some row pivot zero, preselect or adapt Clifford input and relative control; no global fixed 13-setting claim.
4. Unbounded tiny signal c→0 remains a no-uniform-n obstruction.
5. Find truly sample-efficient statistical estimator/protocol under finite calibration budgets and actual device noise; the current 13.27 million guarantee is conservative.

RETURN:
PRF14_ROT013 / FULL_SIX_INDEPENDENT_PAULI_MEMORY_FOURIER_DIMENSIONS_RESTORED / THREE_KNOWN_RIGHT_CLIFFORD_POWERS_9_ROW_MEANS / THREE_EXTRA_SOURCE_MEANS / ONE_LEFT_MEAN_FOUR_WORLD_SEPARATION / FOUR_STRICTLY_POSITIVE_SOURCE_UNITS_EXACT_PASS / 95PC_ALL_13_HOEFFDING_SHOTS_13273442 / SIX_COEFFICIENT_ABS_ERROR_MAX_0P025358 / RECONSTRUCTED_SOURCE_POSITIVE / 1000_BINOMIAL_COMPLETE_TRIALS_PASS / NOV2026_SPAM_NEAR_PRIOR_ART_VERIFIED_ABSTRACT_ONLY / NO_GENERAL_GST_NOVELTY / NO_HARDWARE / NO_PBH / NO_CANON / NO_EXEC_SIGN.
