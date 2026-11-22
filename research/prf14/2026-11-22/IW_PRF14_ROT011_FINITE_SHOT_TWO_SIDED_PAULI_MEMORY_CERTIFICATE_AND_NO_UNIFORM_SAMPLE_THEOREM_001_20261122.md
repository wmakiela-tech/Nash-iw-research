---
artifact_id: IW_PRF14_ROT011_FINITE_SHOT_TWO_SIDED_PAULI_MEMORY_CERTIFICATE_AND_NO_UNIFORM_SAMPLE_THEOREM_001_20261122
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
created_at: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
type: ORIGINAL_SOURCE_RESTRICTED_FINITE_SAMPLE_STABILITY_AND_NONUNIFORM_LOWER_BOUND / EXACT_PAULI_COMB
status: AUTHOR_EXECUTED_SYMPY_EXACT_GEOMETRY_PASS / 1600_SEEDED_BOUNDED_PERTURBATION_TESTS_PASS / DETERMINISTIC_HOEFFDING_BOUND_PASS / EXTERNAL_REFEREE_PENDING
firstness: PRF13_ROT011_SIX_MEMORY_COORDINATES / PRF13_ROT012_CALIBRATED_GATE_MINIMAX / PRF14_ROT005_UNCALIBRATED_SINGLE_GATE_ALIAS / PRF14_ROT010_THREE_SETTING_EXACT_RECOVERY / PRF14_ROT011_FINITE_N_AND_NONUNIFORM_C_SOURCE_ONLY
claim_ceiling: NO_GENERAL_GST_NOVELTY / NO_UNRESTRICTED_PROCESS_TENSOR / NO_HARDWARE_VALIDATION / NO_REALISTIC_SHOT_BUDGET / NO_PHYSICAL_PBH_BRIDGE / NO_CANON / NO_EXEC_SIGN
---

# PRF14 ROT011 — Source-exact Pauli memory 13-configuration reconstruction: unconditional finite-N within a fixed source witness, and a nonuniform shot-complexity no-go

## 0. Why this is a science rotation, not a gate checklist

PRF13 ROT011 identified a six-dimensional Fourier fiber of hidden correlations for two-time exogenous classical Pauli-label noise, and ROT012 optimally accessed it with a KNOWN gate. PRF14 ROT005 found a physically legal alias between six source correlations and an UNKNOWN single intermediate gate. PRF14 ROT010 exhibited two known relative controls, one before and one after the unknown stable middle gate, with six plus six plus one expectations selecting one of four strictly positive source/gate worlds. Its weak point was explicit: 13 exact expectations had no finite-shot noise guarantee; a proposed 8034-shot bound applies ONLY to the last measurement after the first twelve expectations have magically been learned without error. ROT011 addresses the FULL thirteen-setting statistical reconstruction within precisely the ROT010 source, with genuine error propagation and explicit negative sample-complexity knowledge.

Original ROT010 complete source directly reopened, Git blob 2e10001d834781a93fed954ff635b5bd422ebdfb:
https://github.com/wmakiela-tech/Nash-iw-research/blob/2925adf3e8e436a0101d46a2edfdc7c00f59e621/research/prf14/2026-11-21/IW_PRF14_ROT010_RELATIVE_TWO_SIDED_CONTROL_13_EXPECTATION_PAULI_MEMORY_SELF_CALIBRATION_DISCRETE_GAUGE_AND_OPTIMAL_SINGLE_PROBE_001_20261121.md
The original executed local ROT010 symbolic full source and JSON were also reread, not merely remembered.

Actual November 22 currentness: Badacz native owner PREREG090/REVIEW091 has 260 modern generator Monte Carlo energy runs, 188 Wu-Xu Julia source evaluations, 193 PRyMordial BBN runs; reported 13/13 owner gates. Modern PYTHIA8.318-versus-Herwig7.3 table threshold offset now +.13...+.22 dex, rather than old BlackHawk PY/HER historical-table offset +.33...+.37 dex. Physically important correction, not owned or reenacted by PRF14. Source primary:
https://github.com/wmakiela-tech/Nash-iw-research/blob/9e5074866a40628e165a80956dfec2526ef94da2/research/badacz/2026-11-21/IW_BADACZ_B1_MODERN_GENERATOR_TABLES_REVIEW_091_20261121.md
Git blob b451f21a1620c3e6b01eadeb3e180e69cbcbadd3. An independent full BBN LINX engine run remains OPEN; no claimed PRF14 execution.

## 1. Physical source, three actually legal settings, 13 binary means

All claims are confined to exactly the PRF13 classical exogenous two-time Pauli noise: unknown joint p(v,w) for v,w in F2², each history first Pauli U_v, chosen intermediate unitary gate, second Pauli U_w; fixed independent known Pauli preparations and measurements. Interventions change neither p(v,w) nor the clock locations of the two Pauli noises. Repeat shots are IID. This is NOT an unrestricted process tensor, a self-consistent SPAM inference, or a model of gate-dependent environment memory.

Unknown stable middle Bloch rotation R = [[-3,-2,6],[6,-3,2],[2,6,3]]/7, not supplied to estimator. Known right control WR before R, Bloch [[-1,2,2],[2,-1,2],[2,2,-1]]/3. Known left control WL after R, Bloch [[0,1/sqrt(2),1/sqrt(2)],[1,0,0],[0,1/sqrt(2),-1/sqrt(2)]]. All are legal SO(3) Bloch rotations of SU(2) single-qubit gates.

Four physically distinct source/gate worlds d in {(+,+,+),(-,-,+),(-,+,-),(+,-,-)}, R_d=diag(d) R and each hidden off-diagonal Pauli Fourier coordinate C^d_(j,i)=d_i c with c=.1; ordinary first/second/idle channel coordinates identical. Each of 16 p_d(v,w) is strictly positive, between 1/20 and 1/10. The six off-diagonal expectation means at intermediate R and six at R WR are EXACTLY equal across four worlds; the one extra X-from-Y Pauli mean after WL R_d is one of +3sqrt(2)/140,-9sqrt(2)/140,+9sqrt(2)/140,-3sqrt(2)/140. Minimum pairwise gap Delta=3/(35sqrt(2))=0.060609152673..., entirely due to the left intervention.

## 2. New estimator: direct nullspace cross products avoid ratios of noisy small signals

Let a_ij = E[sigma_i | prepare +sigma_j, middle R] and b_ij for middle R WR, only for i != j (six of each). Each is the mean of an IID ±1 final Pauli outcome. The exact identity, with unknown hidden C_(j,i), is:
a_ij = R_ij C_(j,i),
b_ij = (R WR)_ij C_(j,i).

For fixed output row i and each of its two other input columns j, construct the KNOWN observed 3-vector
u_ij = a_ij * column_j(WR) - b_ij * e_j.
Then u_ij · r_i = 0, with r_i the ith row of R. So without EVER dividing by a noisy, potentially small observed mean, get row direction via n_i = u_i,j1 CROSS u_i,j2, r_i = ± n_i / ||n_i||. Resolve each row's orientation for this explicit witness by requiring its third component positive; the original three row third components are +6/7,+2/7,+3/7, and the four physical sign flips are enumerated later as candidates. The matrix of row directions need not be artificially projected onto SO(3) under noise. Four det-positive sign patterns give four predicted third-setting means; classify by the closest prediction to empirical thirteenth mean. After choosing sign, recover original hidden C estimates from a_ij / reconstructed R_ij, with their finite-sample accuracy requiring a separate division stability calculation. **The theorem below guarantees the correct discrete world label, NOT a uniform error guarantee on all six continuous correlation values.**

ACTUALLY run exact SymPy on source:
- cross-product row magnitudes H_i are 1/1575, 1/315, 11/1575, in X,Y,Z order, all strictly positive;
- for row i the squared norms of two u vectors are respectively
  X: 17/11025 and 97/11025;
  Y: 73/11025 and 17/11025;
  Z: 89/11025 and 97/11025.
Thus the source-specific estimator is locally identifiable with a computable nonzero conditioning margin.

## 3. New rigorous deterministic noise-to-decision bound

Assume EACH of the 13 observed scalar sample means differs from its exact physical expectation by at most eta. Because each u vector consists of a times a unit column WR minus b times a unit basis e_j, its perturbation has Euclidean norm <=2 eta. For two true vectors u1,u2 and error e1,e2:
|| (u1+e1) CROSS (u2+e2) - u1 CROSS u2 ||
 <= 2 eta (||u1||+||u2||) + 4 eta².

Let S_i=||u_i,j1||+||u_i,j2||, H_i=||u_i,j1 CROSS u_i,j2||. Provided the perturbed cross product is nonzero, normalized row error after choosing the same orientation is at most
rho_i = [4 eta S_i + 8 eta²]/H_i.

Set eta=7/100000=0.000070. Direct EXACT geometry plus safely rounded numerical evaluations gives
rho_X <= .058744, rho_Y <= .010653, rho_Z <= .007369.
Since rho_X < 2/7, no reconstructed row can cross zero in its third component, so sign orientation is stable.

For the left third probe X<-Y, the numerator uses only row Y and row Z with coefficients 1/sqrt2. Define d=|R_XY|=2/7, a=|a_XY|=1/35, M=9/(7sqrt2), and E_N=(rho_Y+rho_Z)/sqrt2. The exact candidate true numerator has absolute value <=M for all four sign worlds. Then each plug-in candidate third mean has absolute prediction error bounded by

E_pred <= eta*(M+E_N)/(d-rho_X) + a * [ E_N/(d-rho_X) + M*rho_X/(d*(d-rho_X)) ].

ACTUALLY evaluated with the above exact source geometry:
E_pred <=0.025418494.
Each experimental third mean is separately within eta of its true expectation. The nearest-candidate classifier is guaranteed correct if
2*(E_pred+eta) < Delta.

Here 2*(E_pred+eta) <=0.050976987 < Delta=0.060609153, leaving a strictly positive deterministic decision margin >=0.009632166. This is a constructive proof for ALL perturbations of the thirteen empirical means in the eta-box, not merely a Monte Carlo observation.

Limits: the row sign convention uses the specific source R with positive third entries, the exact offdiagonal structure and the known control reference frame. This is NOT a uniform global Lipschitz bound over arbitrary R,p nor a hardware calibration guarantee.

## 4. First actual all-thirteen-setting finite-shot confidence certificate

With independent ±1 terminal Pauli outcomes at each of 13 configurations and n IID repetitions per configuration, classical Hoeffding yields for each sample mean
P(|hat mean - true mean|>eta) <= 2 exp(-n eta²/2).
Union bound over all THIRTEEN configurations:
P(max_13 absolute mean errors >eta) <=26 exp(-n eta²/2).

For eta=0.000070 and requested joint failure probability alpha=.05 it SUFFICES to use
n = ceil[(2/eta²) ln(26/.05)] = **2,552,583,189 shots per configuration**,
N_total = 13n = **33,183,581,457 total binary measurement shots**.

The exact source-specific deterministic selection theorem then gives P(correct four-world label) >=.95, over all FOUR worlds, provided the stated stable source, calibrated controls and SPAM, and IID shots. This is a VALID but extremely conservative finite-sample UPPER BOUND FOR THIS FIXED EXPERIMENT, not an optimized protocol or evidence that the device can actually perform 33 billion shots. Numerically large sample requirement is negative knowledge: ideal exact identifiability and a 13-configuration count alone do NOT imply a practically useful experiment.

ACTUALLY executed 1600 adversarially bounded SEEDED random perturbation stress checks (4 legal worlds times 400 tests, each 13 errors drawn from [-eta,eta]), all passed the SOURCE-specific classifier. Largest observed recovered-row L2 deviation .012650 vs certified .058744 upper; smallest winning distance margin .057437. These tests SUPPORT implementation correctness; only the analytic eta-box proof provides all-errors guarantee. Stress perturbations were synthetic bounded noise, NOT actual quantum hardware experiments and NOT 33-billion-shot Monte Carlo simulation.

## 5. Independent negative theorem: no uniform finite-shot guarantee as hidden signal vanishes

Extend the original source family by replacing c=.1 by ANY 0<c<=.1. Every world p_d remains a strictly positive 16-label causal probability distribution, first/second/idle channel data are identical, and all SIX source hidden correlations are nonzero. The first 12 observable distributions at R and R WR are STILL exactly identical among all four worlds, for every c. For the third specified X-from-Y Pauli probe, the nearest pair of physically distinct worlds has opposite expectation values +/-m(c), where m(c)=3sqrt(2)c/14. Thus their one-shot Bernoulli distributions have KL

k(c) = m(c) * ln[(1+m(c))/(1-m(c))] = 2m(c)^2+O(c^4).

If n third-setting shots are observed, the first twelve settings carry ZERO information about which member of this pair is true. Pinsker and equal-prior binary testing require, for target average classification error <=alpha<1/2:
n >= 2 (1-2alpha)^2 / k(c).

For alpha=.05, actual evaluations (lower bounds, not achievable designs):
- c=.1: n>=882 third shots;
- c=.01: n>=88,200 third shots;
- c=.001: n>=8,820,000 third shots.

As c -> 0 this necessary n grows without bound like c^-2. Hence **there is NO finite sample count that uniformly guarantees recovery across ALL strictly positive source distributions with nonzero hidden Pauli correlations when the magnitude has no positive lower bound**. This is a precise and useful qualification of the ROT010 ideal identifiability claim and a source-specific two-point statistical obstruction, not a fundamental quantum-information novelty theorem. The proven NO-UNIFORM bound concerns the FIXED thirteen-setting observation class and world-pair above, not arbitrary adaptive intermediate instruments, collective strategies or independently characterized gates. Known W_L, W_R and SPAM still matter.

The enormous separation between a conservative SUFFICIENT upper bound of 33 billion total shots in this direct reconstruction scheme and the Pauli-pair NECESSARY lower bound of ~882 for third-stage world separation at c=.1 is scientifically important. The current experiment design is not demonstrated efficient; optimizing the right relative control, stabilizing simultaneous row inversion or adopting a likelihood estimator remain open, rather than declaring an efficient quantum protocol.

## 6. Prior art, external novelty and falsification protocol

The general notions of GST gauge, learnability, finite-sample concentration, two-point hypothesis-test lower bounds and robust process estimation are mature:
- Chen et al., Efficient Self-Consistent Learning of Gate Set Pauli Noise, PRX Quantum 7, 010305 (9 Jan 2026), https://doi.org/10.1103/1pnv-t9px — gate-set Pauli noise learnability/gauge mature.
- The learnability of Pauli noise (2023) primary https://pmc.ncbi.nlm.nih.gov/articles/PMC9813261/ — graph-cycle learnability/cut-space gauge.
- Shadow estimation of gate-set properties from random sequences (Nat Commun 2023) https://doi.org/10.1038/s41467-023-39382-9 — rigorous SPAM-robust gate-set learning bounds already.
- Context-aware gate set tomography leveraging non-Markovianity (2026), https://doi.org/10.1038/s41534-026-01313-z — context dependence is an active mature experimental issue.
- PRF13 Chiribella et al 2009, Pollock et al 2018, White et al 2022 and PRF14 ROT010 latest external guides all remain near hosts.
No general novelty is claimed. The source-specific exact cross-product condition number + finite-shot confidence and c->0 no-uniform bound are new results within this internal witness, no established external priority.

Suggested independent referee falsifiers:
1. Check the exact row cross magnitudes H_i and u_i squared norms against the source R,WR and actual first 12 means.
2. Check the model sign orientation and four candidate third predictions under all four positive source distributions.
3. Verify each step of the deterministic 13-mean eta-box bound; search for adversarial perturbations attaining worse than the stated envelope, without inferring physical solver error from these synthetic perturbations.
4. Verify the Pinsker necessary bound under the stipulated 13 binary measurement laws, and independently flag that it does not cover general instruments.

Owner native E4/B1 firstness and the MODERATOR science-governance status unchanged; PRF14 did not generate new PBH bounds or independently execute LINX.

## 7. Reproduction and exact state

ACTUALLY EXECUTED local Python/SymPy exact-matrix program, source and 1600 bounded perturbation tests: 
/mnt/data/prf14_rot011/prf14_rot011_noisy_two_sided_pauli_memory_exact_cert.py
SHA256 e0b7f51a31a09916ea4b563458b4050ccde484c05b9efe17e44d7d62052d64b8.
ACTUALLY CREATED resulting complete certificate JSON:
/mnt/data/prf14_rot011/prf14_rot011_finite_sample_certificate.json
SHA256 e8e0cb55b6bc2cbfe1c10848f5d4caac70aeef3d9e4b84f674901812b5b6cba0.
No external Python full rerun has been asserted; the linked files contain reproducible source and output. The source math uses exact SymPy for the geometry and Float64 for conservative evaluated numerical inequalities; no rigorous interval-float certification, but the numerical margins are >.0096 and exact radical expressions are supplied to replicate at arbitrary precision.

FINAL:
PRF14_ROT011 / DIRECT_ROT010_PRIMARY_SOURCE_OPENED / CROSS_PRODUCT_QUOTIENT_FREE_IDENTIFIABILITY / EXACT_ROW_GAPS_PASS / DETERMINISTIC_13_MEAN_ETA_BOX_PROOF_PASS / FULL_13_CONFIG_95PC_HOEFFDING_N_33183581457_CONSERVATIVE / 1600_BOUNDED_PERTURBATION_CHECKS_PASS / FOUR_C_POSITIVE_SOURCE_FAMILIES_NO_UNIFORM_N_AS_C_GOES_ZERO / B1_MODERN_HER_PY_OWNER_091_ADMITTED / NO_LINX_I1 / NO_HARDWARE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
