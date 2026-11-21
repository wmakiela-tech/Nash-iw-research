---
artifact_id: IW_PRF14_ROT010_RELATIVE_TWO_SIDED_CONTROL_13_EXPECTATION_PAULI_MEMORY_SELF_CALIBRATION_DISCRETE_GAUGE_AND_OPTIMAL_SINGLE_PROBE_001_20261121
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
date: 2026-11-21 Europe/Warsaw
exposure: PUBLIC
class: ORIGINAL_SOURCE_RESTRICTED_EXACT_CAUSAL_PAULI_COMB_IDENTIFIABILITY / TWO_SIDED_RELATIVE_CONTROL / FOUR_POSITIVE_DISCRETE_GAUGES / CONSTRUCTIVE_13_EXPECTATIONS / SINGLE_PROBE_SO3_MAXIMIN
status: SYMPY_EXACT_EXECUTION_PASS / LOCAL_PROGRAM_SHA256_VERIFIED / PUBLIC_REPRO_CODE_GIT_READBACK_PASS / EXTERNAL_REFEREE_PENDING
firstness: PRF13_ROT011_CLASS_AND_SIX_FOURIER_DIRECTIONS_FIRST / PRF13_ROT012_KNOWN_GATE_OPTIMAL_FIRST / PRF14_ROT005_UNKNOWN_SINGLE_GATE_ALIAS_FIRST / PRF14_ROT010_RELATIVE_CONTROL_THREE_GATE_RECOVERY_CONSTRUCTION_FIRST_INTERNAL_ONLY
claim_ceiling: NO_GENERAL_GST_NOVELTY / NO_FUNDAMENTAL_PROCESS_TENSOR_RESULT / NO_UNRESTRICTED_FULL_Q_COMB / NO_DEVICE_OR_SPAM_SELF_CALIBRATION / NO_HARDWARE / NO_PBH_LINK / NO_CANON / NO_EXEC_SIGN
---

# PRF14 ROT010 — A two-sided relative-control repair of an uncalibrated two-time Pauli-memory source alias

## 0. Scientific decision and source firstness

The current B1 highest priority would be native independent LINX full nuclear network replication. Before pivoting, PRF14 checked the actual local runtime: Python 3.13, JAX installed, LINX/equinox/diffrax/interpax absent, package-network DNS unresolved; source native LINX cannot honestly be run, so NO_LINX_I1. Badacz additionally completed 21 Nov B1 E4 PREREG088/REVIEW089 94/94 Julia + 97/97 PRyMordial calls with 8 gates PASS; PRF14 does not duplicate that owner source work. **To exercise its independent theoretical-science function rather than repeat owners' B1 numerical analyses, PRF14 returns to the open source-exact Pauli memory line.**

Direct source reads, not inherited summary only:
PRF13 ROT011 exact 16->10+6 Pauli Fourier hidden-memory fiber, original Git blob a238cafeba30a667ad634bf5ab3725a16df1f84e:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf13/2026-11-12/IW_PRF13_ROT011_SIX_DIMENSION_PAULI_HIDDEN_MEMORY_TOMOGRAPHY_PUBLIC_RETURN_001_20261112.md

PRF13 ROT012 global best KNOWN one fixed gate Vstar, original blob d11b651fcead2d6f1f81e2b1e10afe92f3ef5d7e:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf13/2026-11-12/IW_PRF13_ROT012_SINGLE_GATE_MINIMAX_STABILITY_AND_SIX_PARAMETER_PAULI_COMB_001_20261112.md

PRF14 ROT005 exact single UNKNOWN source-and-gate alias, original blob dbfd9199b8b152bd2a3902d19e84c7c71c40b164:
https://github.com/wmakiela-tech/Nash-iw-research/blob/ff3ac41c2fa58b1c3b73993540d0dda921af09c5/research/prf14/2026-11-17/IW_PRF14_ROT005_PRF13_PAULI_MEMORY_SIX_CORRELATION_UNCALIBRATED_GATE_SOURCE_ALIAS_EXACT_COUNTEREXAMPLE_AND_KNOWN_GATE_DISCRIMINATOR_001_20261117.md

NEW problem: can exact six hidden classical Pauli correlations and an unknown stable middle unitary be reconstructed without prior absolute characterization of that unitary, using physically known control rotations placed on both sides of it in the intermediate slot? If yes, which discrete gauge survives using relative controls on only one side, and can one final Pauli test eliminate it?

## 1. Fixed causal legal model, scope and observables

As in original PRF13, draw exogenous (v,w) in GxG with G=F2^2 from unknown stable p(v,w). Apply first U_v, an intermediate chosen unitary, then second U_w; v,w are not changed by the identity of the chosen intermediate control. Each such mixture of unitary two-step histories is a legal causal comb, but **not** an arbitrary quantum-environment process or a model of noisy calibration/SPAM.

Pauli labels X,Y,Z, characters chi_X(v)=(-1)^z, chi_Y(v)=(-1)^(x+z), chi_Z(v)=(-1)^x. Fourier coefficients C_(j,i)=Σ_v,w p(v,w)chi_j(v)chi_i(w). In the strict-positive model around uniform noise, six ordered j!=i are ordinary-channel-invisible; the other ten first/second/idle Fourier coefficients may be learned by ordinary channel measurements. For a physical middle unitary with Bloch SO3 rotation R:
T_ij(R)=E[terminal sigma_i | prepare +sigma_j, middle R]=R_ij C_(j,i).
This is exact for this causal exogenous class (PRF13).

Use THREE physically lawful control settings without changing the two noise steps:
A: unknown stable V, rotation R.
B: known W_R immediately BEFORE unknown V, rotation R W_R.
C: known W_L immediately AFTER unknown V, rotation W_L R.
The W gates are assumed independently characterized relative to the Pauli input/output reference frame; absolute R is unknown. They must not alter p or the location/timing of noise events; violations are independent device falsifiers. Known SPAM reference remains an essential assumption, so do NOT call this full calibration-free quantum tomography.

## 2. Conditional row reconstruction theorem from only two control settings

For i!=j and nonzero C_(j,i),R_ij, the first two experimental means give a source-independent quotient:
q_ij=T_ij(RW_R)/T_ij(R)=(RW_R)_ij/R_ij.

Writing r_i for the unknown ith ROW of R, this supplies TWO homogeneous equations per row:
r_i · [column_j(W_R)-q_ij e_j]=0 for each j!=i.
If the 2x3 constraint matrix A_i has rank two, its nullspace is a 1-dimensional real line. Unit length fixes each row up to sign. Since R is orthogonal with det+1, the 3 signs must have product +1. Thus **at most four SO3 candidates R'=D R** remain with D=diag(d_X,d_Y,d_Z), d_i=±1, product+1.

Each candidate sets its own Fourier source coefficients C'_(j,i)=d_i C_(j,i), yielding EXACTLY the same six A and six B means for EVERY relative RIGHT control W_R (indeed arbitrary composition on the right), not just the chosen W_R. For sources sufficiently near uniform, all four are legal, strictly positive Pauli distributions. The right-only ambiguity has a transparent physical origin: a deterministic final Pauli-frame flip can be traded against left multiplication of an unknown middle unitary. Only a control placed to the LEFT of the unknown middle V can operationally break it, absent other reference information.

This conditional rank theorem is source-restricted inverse-matrix algebra, NOT a universal minimal-gate or generic quantum GST theorem. Known nonzero diagonal Fourier coefficients or other calibration data could break ambiguities earlier; four exact aliases are claimed for the EXPLICIT SOURCE below.

## 3. Explicit exact legal SO3 controls and four positive source worlds

Original PRF13 legal unknown gate V=(I−i(X+Y+2Z))/sqrt7 has Bloch rotation:
R=(1/7)*[[-3,-2,6],[6,-3,2],[2,6,3]].
Known right control W_R=−i(X+Y+Z)/sqrt3, Bloch
R_R=(1/3)*[[-1,2,2],[2,-1,2],[2,2,-1]].
These are EXACT unitary SU2 physically legal gates, SO3 orthogonal with determinant +1, checked symbolically. Six offdiag R entries nonzero.

For any D in the four sign-flip matrices:
D_0=diag(1,1,1);
D_1=diag(-1,-1,1);
D_2=diag(-1,1,-1);
D_3=diag(1,-1,-1),
set C^D_(j,i)=d_i/10 for j!=i and ordinary coefficients: C_00=1, C_a0=C_0a=C_aa=0 for nonzero a. The *whole legal source distribution* is:
p_D(v,w)=(1/16)[1+Σ_(i!=j) (d_i/10) chi_j(v)chi_i(w)].

Exact original SymPy program verifies for each D:
- 16 probabilities sum to one, with **min p_D=1/20, max p_D=1/10**, strictly interior;
- all first, second and idle endpoint Pauli channels equal the completely depolarizing channel;
- all six hidden ordered offdiag correlations are nonzero;
- all six T_ij(V) and six T_ij(V W_R) are exactly identical for all FOUR distinct (source p_D, unitary D R) physical worlds.

The source-only two-setting six scalar measurements therefore have a four-way PHYSICAL source/gate ambiguity. This is stronger than merely saying the algebra admits row-sign roots: every root corresponds to a legal strictly-positive causal process source and legal SU2 gate.

Actual right-ratio measurements and source-independent row ranks:
row X: q_XY=−4/3, q_XZ=−8/9, rank A_X=2;
row Y: q_YX=−4/9, q_YZ=+2/3, rank A_Y=2;
row Z: q_ZX=+8/3, q_ZY=+2/9, rank A_Z=2.
The uniquely normalized null rows (up to sign) reproduce R above.

## 4. A third physical middle-setting and ONE optimal targeted Pauli readout resolve ALL four worlds

After V insert a known physical W_L whose Bloch SO3 rotation is:
R_L=[[0,1/sqrt2,1/sqrt2],[1,0,0],[0,1/sqrt2,-1/sqrt2]].
SymPy verified R_L^T R_L=I and det R_L=+1, so there exists a physical single-qubit SU2 implementation (global phase irrelevant).

With only ONE additional Pauli observable in setting C, prepare +Y before first noise, measure X after second noise. It is T_XY(W_L R), not a general 6-measurement tomography. For the four candidate legal worlds D0,D1,D2,D3 its EXACT expectation values are, in the same order:
**+3 sqrt(2)/140, −9 sqrt(2)/140, +9 sqrt(2)/140, −3 sqrt(2)/140.**
All four are distinct. Therefore six A scalar expectations + six B scalar expectations + ONE C scalar expectation = **13 exact scalar Pauli expectation configurations SUFFICE for this explicit source and all four-source candidate discrimination**, with unknown V reconstructed from data. Ordinary first/second/idle channels supply the other ten p Fourier coordinates if a complete 16-entry p distribution is sought. This is an explicit existence result, not a proven lower bound, a claim about arbitrary p, or a general finite-shot measurement protocol.

The minimum gap between any two of the four ideal C mean values is EXACT:
delta_min=3 sqrt(2)/70 = 3/(35 sqrt(2)) ≈0.0606091526731.
For the corresponding single ±1 terminal outcome, the smallest total variation gap between any pair is delta_min/2≈0.0303045763366.

## 5. NEW narrow exact experimental-design maximin theorem for the final single probe

Keeping the *original explicitly fixed unknown R, source coefficients d_i/10*, six A/B readouts and targeting the ONE Pauli coordinate X<-Y, optimize W_L over ALL legal SO3 rotations (equivalently all unit first rows w). Because d_X d_Y and d_X d_Z vary independently across the four determinant+1 sign aliases, the four expected C means have form
 c[A ± B ± C], c=1/10,
where A=R_XY*w_X, B=R_YY*w_Y=−3*w_Y/7, C=R_ZY*w_Z=6*w_Z/7.
The minimal absolute pairwise separation of these four outcomes is
2c*min(|B|,|C|,||B|−|C||).
Subject to w_X²+w_Y²+w_Z²=1, a nonzero w_X wastes norm without improving separability, so the optimum has w_X=0. In |C|≥|B| branch the optimum requires |C|=2|B|, giving |B|=3/(7sqrt2), w_Y=w_Z=1/sqrt2. In reverse branch |B|≥|C| the optimum |B|=2|C| yields |C|=6/(7sqrt17), strictly smaller. Hence the above R_L is **GLOBAL MAXIMIN OPTIMAL OVER ALL SO3 LEFT RELATIVE GATES FOR THIS SINGLE SPECIFIC X<-Y PAULI READOUT AND THIS ONE EXACT SOURCE/GATE WITNESS**:
sup_WL min_(D!=D') |E_D[X|+Y]-E_D'[X|+Y]| = 3/(35sqrt2).
This is a meaningful local design theorem that goes beyond a random control-gate existence check. It is NOT a minimax theorem among arbitrary input/output probes, collective quantum measurements, general R or p, or genuinely uncalibrated SPAM.

A conditional finite-sample consequence: IF first twelve means and all known gates were EXACT, then with n independent ±1 samples of ONLY the last target readout, and classify by the nearest of the four exact candidate mean values, Hoeffding gives
P(error)≤2 exp(-n delta_min²/8). For alpha=.05, sufficient n=8034 terminal readouts. This does **NOT** provide an operational total-shot claim: first two setting means would have finite sampling error, inversion uses quotients of means as small as ~0.0286, row X nullspace is noise sensitive, reference gates/SPAM may be imperfect and noise stationarity may fail. All these have to be incorporated in any honest hardware-level confidence proof.

## 6. Robustness restrictions and mature PRIOR ART (2025–2026)

Key new external papers actually checked at original publishers during this rotation:
- White, Jurcevic, Hill & Modi, **Unifying Non-Markovian Characterization with an Efficient and Self-Consistent Framework**, Physical Review X 15, 021047, published 9 May 2025, https://doi.org/10.1103/PhysRevX.15.021047 — fully self-consistent process-tensor/device characterization is already a mature framework.
- Chen et al., **Efficient Self-Consistent Learning of Gate Set Pauli Noise**, PRX Quantum 7, 010305, published 9 January 2026, https://doi.org/10.1103/1pnv-t9px — Pauli-noise degrees of learnability and gauge structure via algebraic graph theory; generic learnability not new.
- **Disambiguating Pauli Noise in Quantum Computers**, PRX Quantum, Sep 2026, https://doi.org/10.1103/69wc-gzl6 — a further contemporary device-scale Pauli-noise disambiguation host.
- **A Guide to Higher-Order Quantum Operations**, PRX Quantum 7, 042001, published **13 November 2026**, https://doi.org/10.1103/92c4-g7qs — recent systematic higher-order process tomography including restricted operational measurement subspaces and self-consistent process tensor methods.
- PRF13 earlier Chiribella-D'Ariano-Perinotti 2009 / Pollock et al 2018 / White et al 2022, and PRF14 ROT005 GST Nielsen et al 2021 and Blume-Kohout et al 2017, already mature general context.

This small exact 13-readout witness may be novel relative to these papers at this very narrow construction level, but NO COMPREHENSIVE priority subtraction and NO referee have established that. **NO_EXTERNAL_NOVELTY, NO_NEW_PHYSICS.** Not a bridge to PBH, BlackHawk, NASH C1 or unrestricted process tensors.

## 7. Actually run, reproducibility and negative knowledge

The entire exact calculation WAS run in the local container with SymPy, including all 4x16 source probabilities, all 3 SO3 rotations, all first/second/idle Fourier coordinates, row nullspace ranks, 4 identical two-gate source/gate output maps, one optimized third-readout 4 distinct values, maximin algebra and conditional Hoeffding integer shot count. Stdout PASS. Full local program:
 /mnt/data/prf14_rot010/prf14_rot010_three_control_pauli_source_recovery_exact.py
 SHA256 38dce43ec855b0d71eb8a5a10cee6d2294225e1ce388df69969356edef4e55d6.
Exact JSON output:
 /mnt/data/prf14_rot010/prf14_rot010_three_control_pauli_source_recovery_exact_output.json
 SHA256 616d79477a52955cd1967f04792fda6586a42361ab9b95ac570d582b40ffe6e9.

A concise public exact-rational/symbolic reproducer created and **GitHub provider full readback PASS**, but the PUBLIC copy is not independently executed in an external Python environment (do not conflate source readback with its execution):
https://github.com/wmakiela-tech/Nash-iw-research/blob/0861fda7c75ea26b41c0c4f83667208ba5750606/research/prf14/2026-11-21/code/IW_PRF14_ROT010_RELATIVE_CONTROL_PAULI_MEMORY_EXACT_FOUR_ALIAS_TO_ONE_REPRO_001_20261121.py
Commit 0861fda7c75ea26b41c0c4f83667208ba5750606, Git blob 74086f8e80630799cd35f8644714994c647a3ffa.

Scientific cautions:
1. No general minimality of 13 expectation configurations; the 12+1 structure is one constructive protocol under a fixed source and known SPAM.
2. Right-only alias of four is genuinely physical for all controls preceding V, not a general full comb gauge.
3. Left-control placement works only if the same exogenous p and stable V apply; gate-dependent memory and finite control durations change the source model.
4. The stage3 n=8034 bound assumes error-free first 12 means; the actual total sample complexity may be vastly larger.
5. Overlap with 2025–2026 self-consistent Pauli noise/process theory is substantial; independent source firstness beyond this report NOT assessed as novel.
6. No new LINX/AlterBBN network execution and no new B1 ownership or PBH novelty.

RETURN:
PRF14_ROT010 / PRF13_PAULI_SOURCE_PRIMARY_READ / RATIONAL_FOUR_FULLY_POSITIVE_RIGHT_CONTROL_ALIASES_PASS / TWO_CONTROL_ROW_RANK_TWO_PASS / THREE_RELATIVE_CONTROL_ONE_EXTRA_PAULI_PROBE_UNIQUE_PASS / X_FROM_Y_ONE_PROBE_SO3_GLOBAL_MAXIMIN_DELTA_3OVER35SQRT2 / HOEFFDING_8034_CONDITIONAL_ONLY / MATURE_2026_GST_PAULI_PRIOR_SUBTRACTED / LINX_I1_STILL_OPEN / NO_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN.
