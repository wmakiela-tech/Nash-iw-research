---
artifact_id: IW_INT8_ROT030_EXACT_NONTRANSLATIONAL_SHEAR_COMMUTANT_SUBMODULE_ORBITS_001_20261025
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_METRIC_NATURALITY_FILTER_OPERATOR_HOST_001
exposure: PUBLIC_SAFE
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT030 — exact dimension and explicit subgroup-orbital basis of full universal shear tensor commutant

## Mature host, first authorship, currentness
Current Slack checked on 2026-10-25. INT8 ROT029 ALREADY PROVED every arbitrary fixed SL3(Z) pullback-equivariant real linear operator on Sym2 tensor fields (no translation/locality assumptions) must be F=S tensor I6, with S purely spatial and invariant on diagonal pair-orbits. ROT018–019 previously classified the translation-invariant scalar convolution subclass by gcd-orbits, dimension tau(N). ROT023–028 addressed unrelated metric/raw-k alias TT projector spectral questions. MT13 FIRST found exactly metric-transported affine filter family E_g and raw-k TT alias. XH-S4 owns curved York; M13 historic source puretrace masked K_A; Geeky-S11 even matched TT; PRF11 Lie/TT collocation.

NEW ROT030 project-local question: What are ALL possible spatial S when translation invariance is DROPPED? Mathematical tools are established permutation centralizers and subgroup counting. Prior literature for subgroup formula: Hampejs, Holighaus, Toth, Wiesmeyr, Representing and counting subgroups of Z_m x Z_n, Journal of Numbers 2014 Article 491428, DOI 10.1155/2014/491428, arXiv:1211.1797. No mathematical novelty/prior-art priority or physical upgrading.

## Precise class and theorem

N>=1 arbitrary integer. R=Z/NZ, node set G=R^3, real symmetric tensor fields V_N={H:G -> Sym2(Real^3)}, dim=6N^3. For ALL A∈SL3(Z), U_A H(x)=A^T H(Ax mod N) A. ONE fixed real linear operator F, unchanged under pullbacks, with F U_A=U_A F; neither locality, translation invariance, positivity, orthogonality nor self-adjointness assumed. ROT029 already proves F=S tensor I6. Here S is an arbitrary real N^3 by N^3 matrix invariant under simultaneous A action on its two node indices.

For x,y∈G, construct subgroup of R^2:
 W(x,y)=span_R{(x_1,y_1),(x_2,y_2),(x_3,y_3)}.

THEOREM 030.1: Two ordered pairs (x,y),(x',y') are in the same diagonal SL3(Z) orbit if and ONLY IF W(x,y)=W(x',y'). Consequently ALL permitted S are precisely
  S(x,y)=c_[W(x,y)]
with independent arbitrary real coefficients indexed by additive subgroups W≤R^2.

This is an EXPLICIT ORBIT BASIS: for each W define
  (B_W H)(x)=sum over y satisfying W(x,y)=W of H(y);
all universal F are sum_W c_W B_W tensor I6.

PROOF of orbit iff: Any A performs invertible row operations on the 3x2 matrix [x|y], preserving its generated row module. Conversely, by CRT reduce to local principal ring Z/p^a. Any submodule of R_p^2 requires at most two generators (Smith form). By Nakayama's lemma any generating 3-tuple can be GL3-row-reduced to (u,v,0); any two minimal generating sets of the SAME module differ by an invertible GL2 change in generators. Hence two 3x2 matrices with the same row module are related by GL3(R_p). The unused zero third row allows determinant adjustment by diag(1,1,t) for every unit t, turning GL3 relation into SL3. CRT assembles the local relations, and elementary SL3 modulo N transformations lift to integral SL3(Z). Thus exact orbit equivalence for arbitrary composite N. Because every additive subgroup of R^2 is invariant under integer multiplication, it is automatically an R-submodule.

THEOREM 030.2, exact dimension:
 dim_R End_{SL3(Z)}(V_N)
 = #Sub((Z/NZ)^2)
 = sum_(d|N) sum_(e|N) gcd(d,e)
 = product_(p^a||N) sum_(i=0)^a sum_(j=0)^a p^min(i,j)
 = product_(p^a||N) sum_(j=0)^a [2(a-j)+1] p^j.

Proof: dimension of permutation commutant is number of diagonal orbits of ordered node pairs; previous theorem identifies these with additive subgroups. Hampejs et al's subgroup count is the already-known divisor-gcd formula. Chinese remainder gives prime-factor product, gcd(p^i,p^j)=p^min(i,j), and exactly 2(a-j)+1 index pairs have minimum j. N=1 correctly returns 1. For PRIME N=p exactly p+3 orbits: (0,0), p+1 nonzero dependent lines (including x=0,y!=0), and one independent-pair orbit. For p^2: p^2+3p+5.

THEOREM 030.3, proper convolution subalgebra and noncommutativity:
Additionally demanding translation-invariant S(x,y)=k(x-y) recovers exactly tau(N) scalar gcd-orbit convolution parameters from INT8 ROT019. This is generally a strict proper subset of the full algebra. Explicit nontranslation positive invariant examples are F0(H)(x)=1_(x=0)H(0) and Fmean(H)(x)=N^-3 sum_y H(y). Both commute with U_A for ALL A, but for N>1 F0 Fmean != Fmean F0: entire commutant algebra is noncommutative. Pointwise Euclidean tracefree map H -> H-tr(H)I/3 is an explicit NON-equivariant fiber control. Universality forces scalar tensor action, NOT a single global multiple of identity on all spatial nodes.

## Project-lattice census

N : full commutant dimension ; translation-convolution dimension:
31 : 34 ; 2
33 : 84 ; 4
35 : 80 ; 4
37 : 40 ; 2
39 : 96 ; 4
41 : 44 ; 2
Other values N4 15/3, N8 37/4, N9 23/3, N12 90/6, N15 48/4, N63 230/6, N81 237/5.

## Executed independent reproducibility and negative knowledge
ROUTE A: NumPy/Numba disjoint set union over all N^6 ordered lattice pairs and all SIX elementary shears Eij(1), no assumed subgroup formula. Exact orbit count for N=1,2,3,4,5,6,7,8,9,10,12: 11/11 PASS. In particular N12 has 2,985,984 node pairs and EXACT 90 orbits.
ROUTE B: independent brute bitmask enumeration of all 2-generated additive/R submodules of R^2, NO orbit use: same exact 11/11 counts.
ROUTE C: separate subgroup Hermite-normal-form enumeration with divisors a|N,b|N, g=gcd(a,N/b), generator pair (a,0),(t a/g,b) with 0<=t<g. For every actual orbit root representative, compute W from its THREE coordinate rows, compare fingerprints; bijection with HNF subgroups exactly 11/11 PASS (stronger than matching total counts).
ROUTE D: fully independent direct real 3x3 tensor field U_A on N=2,3,4,5,7, each with 18 explicit shears, random symmetric tensors: origin map and mean map commute; tracefree fails; origin and mean do not commute with each other. 5/5 grid tests PASS.

Initial rejected implementation used Python generator closure inside numba njit and DID NOT COMPILE. Fixed by returning orbit-root array from compiled function, counting with NumPy outside. First clean-run exposed nondeterministic last bits (~1e-15) in floated positive-control residual JSON, NOT in integer orbit data. Fixed byte-replay formatting to 12-decimal precision after checking ORIGINAL unrounded numerical tolerances; did NOT relax mathematical tests.

LOCAL Moderator reproducible 9-file ZIP:
iw_int8_rot030_complete_orbit_submodule_commutant_bundle.zip
SHA256 001817e12d6d8244d4645b2218160e3906e45d8f570f63fd3219c35b8f2aae6d.
It has full detailed Polish theorem/proof report, complete executed main Python, independent HNF and tensor-audit Python, THREE row-level JSON files, README, SHA256SUMS. Clean zip CRC PASS, 8/8 SHA256 manifest PASS. Clean extracted rerun of all three executables PASS and THREE output JSON files BYTE-IDENTICAL to ZIP snapshots. GitHub Python-code publication is NOT claimed here.

Original retained helper deepseek_python_20260627_a87249.py available with SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801; NO new DTC helper science computation in ROT030 because theorem is abstract orbital arithmetic. The historical production runtime is byte unavailable. NO BW ingestion or independent referee/owner/EXEC confirmation; no new task cascade.

STRICT NONMAP: One fixed metric-INDEPENDENT tensor operator. Does NOT forbid metric-indexed P_g or E_g families; NO nonflat York, physical gauge, Noether, Lorentzian Box, J3/K invariant, real GW field energy, historic masked KA or new NASH physics. Classical permutation/subgroup mathematics; NO NOVELTY / NO CANON / NO EXEC / NO PHYSICAL UPGRADE.
