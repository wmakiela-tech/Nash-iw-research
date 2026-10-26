---
artifact_id: IW_INT8_ROT032_SQUAREFREE_REAL_WEDDERBURN_CHIRAL_PROJECTORS_001_20261026
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_METRIC_NATURALITY_FILTER_OPERATOR_HOST_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_FINITE_ALGEBRA_AND_SOURCE_TYPED_MATH_ONLY / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT032 — squarefree real commutant product and nonseparable N35 chiral projectors

## Currentness and two-surface subtraction
Fresh #iw-dispatch checked 26 October 2026 (KN11, SYSS5 metadata, MT13→MT14 planned succession, PRF11). **INT8 ROT029 already** proved every ONE fixed all-integral SL3(Z) tensor-pullback equivariant real linear F on V_N=Sym²(R³)-valued lattice fields is F=S tensor I6, without translation/locality hypotheses. **INT8 ROT030 already** enumerated pair-node orbit/submodule basis and dimension for all N; **ROT031 already** supplied the real prime-grid Wedderburn blocks. **MT13 first** developed exactly metric-transported affine E_g and found raw-k metric TT alias fault. XH-S4 owns curved York; M13 historical h=fI, K_A and masks; Geeky-S11 even raw-vs-matched projectors; PRF11 distinct Lie/TT operators. No owner discovery reattributed.

Mature MATH HOST: finite group permutation commutants, CRT, real Maschke/Schur/Artin–Wedderburn, elementary C tensor_R C = C direct_sum C. External background: M. Bardoe and P. Sin, *The permutation modules for GL(n+1,q) acting on projective n-space and nonzero vectors*, J. London Math. Soc. 61 (2000), 58–80, DOI 10.1112/S002461079900839X; A. Prasad, MathOverflow 2013, https://mathoverflow.net/questions/152726/decomposing-representations-of-gln-f-q-induced-from-certain-kinds-of-parabolic ; Artin–Wedderburn lecture reference https://math.ucla.edu/~sharifi/notes/algebra-ch13.html. The **project-local** extension is the precise N33/35/39 real algebra decomposition and an executed nonfactorizable N35 projector witness; NO math novelty/priority or physical-meaning claim.

## Declared finite mathematical host
Take SQUAREFREE integer N=product of DISTINCT primes p_i, G_N=(Z/NZ)^3, V_N=all real symmetric covariant tensors H:G_N→Sym²(R³), dim 6N³. ALL A∈SL3(Z) act by U_A H(x)=A^T H(Ax modulo N) A, using REAL tensor indices and MODULAR node coordinates. One fixed, metric-INDEPENDENT F commutes with all these U_A, including congruence-kernel lifts. By ROT029 F=S tensor I6 and S belongs to real spatial algebra A_N=End_SL3(Z/NZ)(R^{G_N}). No assumption of translation, locality, selfadjointness, physical admissibility or filter source equations.

CRT yields Z/NZ=product F_pi, SL3(Z/NZ)=product SL3(F_pi), node space R^{G_N}=tensor_R R^{F_pi^3}. Since factors act independently, exact real associative *-algebra identity:
 A_N = tensor_R over i A_pi.                                 (032.1)
The tensor FIBER I6 occurs ONCE globally, NOT once per local prime.

ROT031 prime p ODD:
 A_p = M2(R) direct_sum R^2 direct_sum C^((p−3)/2);
 p=2: A_2=M2(R) direct_sum R.
The local isotypic spatial real dimensions are: T=M2(R) dim2; P=R dim L_p−1; Q=R dim L_p, with L_p=p²+p+1; each C type dim2L_p. For p2 only T and P.

## Exact theorem 032.1: full squarefree real block and projection rank recipe

Choose one simple summand from each prime's algebra. Let t=# of T=M2(R) choices and c=# of C choices (all other choices are R). Then the complete REAL Wedderburn resolution of that tensor product is:

  c=0: ONE M_(2^t)(R) block;
  c>=1: 2^(c−1) copies of M_(2^t)(C).                    (032.2)

Proof: matrix tensor factors multiply their sizes; tensor_R C with no prior C changes the division algebra from R to C, and EACH further C splits via C tensor_R C ≅ C direct_sum C, twice as many complex blocks. No H/Quaternion algebra appears in this source-defined class. The multiplicities and real algebra dimensions are exact for every squarefree N, not just the tested cases.

If d_i is real spatial dimension of each chosen local isotypic factor (T=2,P=L−1,Q=L,C=2L), let D=product d_i, m=2^t and b=1 if c=0 else b=2^(c−1). The decomposition gives b orthogonal isotypic components of size D/b. Each M_m(R) or M_m(C) block permits equivariant ORTHOGONAL projectors of spatial ranks r D/(b m) for r=0,1,…,m. Thus the theorem classifies possible projector ranks, including continuous Grassmann families for m>=2. Full Sym²-tensor projector rank is 6 times spatial rank, not a physical two-polarization rank.

## Fully determined N33/35/39 block census

| Simple real algebra | N33=3*11 | N35=5*7 | N39=3*13 |
|:--|--:|--:|--:|
| M4(R) | 1 | 1 | 1 |
| M2(R) | 4 | 4 | 4 |
| R | 4 | 4 | 4 |
| M2(C) | 4 | 3 | 5 |
| C | 8 | 10 | 10 |
| Total simple factors | 21 | 22 | 24 |
| Real algebra dimension | 84 | 80 | 96 |
| Spatial dimension N³ | 35937 | 42875 | 59319 |

All real dimensions sum as m² for each M_m(R) and 2m² for each M_m(C), matching product(p+3) from ROT030. Spatial isotypic dimensions sum to N³. Additional directly executed N6,10,15,21,77 also satisfy BOTH exact integer closure checks. N35 differs conceptually: p5 has 1 nonreal-character C sector and p7 has 2, so TWO source C×C combinations each split into TWO distinct complex simple blocks. There are 4 such chiral blocks among the listed 10 C blocks. N33 and N39 have p3 with NO C sector, so no C×C splits.

## Exact theorem 032.2: new allowed N35 nonseparable projector pair

Let E5 be one p5 radial nonreal-character real sector (dim 2L5=62, L5=31), E7 a chosen nonreal-character p7 sector (dim2L7=114, L7=57). Let P5,P7 be orthogonal projectors onto E5,E7. Their real equivariant complex structures J5,J7 satisfy J_p²=−P_p, J_p^T=−J_p and J_pP_p=J_p. They commute with every local SL3(F_p) node permutation. Define on the CRT-identified FULL N35 spatial Hilbert space:

  Pi_plus  = (P5 tensor P7 + J5 tensor J7)/2,
  Pi_minus = (P5 tensor P7 − J5 tensor J7)/2.           (032.3)

Because (J5⊗J7)²=P5⊗P7 and the product of two skew-adjoint factors is selfadjoint, Pi_± are two EXACT orthogonal selfadjoint idempotents, mutually annihilating, summing to P5⊗P7. Both commute with all integral SL3 shears. Zero traces of J5,J7 give:
 rank_R Pi_plus = rank_R Pi_minus = (62*114)/2 = 3534.
Tensor field F_±=Pi_± tensor I6 has exact rank **21204** in the real 6*(35³) field space.

They are NOT product of two local equivariant orthogonal projections: locally the complex scalar commutant C has only idempotents 0 and1, which yield zero or full rank7068 on E5⊗E7, not rank3534. Stronger decomposability witness: if c5,c7 are normalized cosine bases and s5=J5 c5, s7=J7 c7, then
 Pi_plus(c5⊗c7)=.5(c5⊗c7 + s5⊗s7).
This is a 125×343 matrix of rank TWO with nonzero singular values exactly .5 and .5 (verified independent SVD, third ~3.76e−17). Any SINGLE factorizable local linear map B5⊗B7 sends a simple input to a simple output, so it cannot equal this Pi_plus.

Here 'chiral' labels the ±1 eigenspaces of real involution J5⊗J7, NOT chirality/spin of a physical wave or a Lorentzian parity invariant.

## Executed independent audit, negative knowledge, clean reproducibility
A) Completely standalone Python/NumPy prime-sector bookkeeping over N=6,10,15,21,33,35,39,77, both integer global dimension closures PASS. Explicit cos/sin radial bases for p5 and p7, exact tensor projector algebra and six integer shear generators on both prime factors. The full CRT permutation of all **35³=42875** original nodes was additionally explicitly assembled; on ALL six shears in ORIGINAL grid order, both routes agree. Idempotence, mutual annihilation, complementarity, projector ranks, non-product witness tested. Numerical errors below 1e−10, SVD witness .5,.5,3.76e−17. Does not import original DTC0a helper.
B) INDEPENDENT Python+SymPy verifier with NO import of A): EVERY ONE of 6^6=46656 ordered node pairs and 10^6=1,000,000 node pairs given direct orbit labels, checked under ALL six full shear permutations. Exactly 30 orbit classes for N6 and 40 for N10, same as predicted factor dimensions. Independently, EXACT rational J=[[0,-1],[1,0]], K=J⊗J yields (I±K)/2 orthogonal rank2 projections on R4, so 31*57 blocks yield rank3534 each. Independently solves local real C idempotents as {0,I}. These are genuine tests, not re-statements.
C) Recorded initial FAILED test: first standalone program accidentally assigned local trivial M2(R) a one-dimensional spatial carrier instead of its correct dimension TWO. The sum-of-spatial-dimensions assert rejected the run. Corrected input factor tuple, no claim accepted before rerun. Subsequent 8/8 carrier exact dimensions and checks pass.
D) Local 8-member Moderator/owner ZIP **iw_int8_rot032_squarefree_chiral_projector_repro_bundle.zip** SHA256 **2fd151b9189e1fd86887fec0278fe42c0949bea8740bcce48c8ebba789cf0315**: complete original Polish report SHA256 **1afb72b1ddbb79a66d7c008913ad9cb55d60ba125df9aa9b4690ae0fef5c493a**, full main executable Python SHA256 **e759930c438818cc61dbfa0322ca8643b747e36abe04a43994f6e059b3a63341**, full independent audit SHA256 **ac70648596c8aa18c5f1d6b53a35442818d4b0cbb98b4a1c73883922d08bc6fa**, two JSON result files, log, README, SHA256SUMS. ZIP CRC PASS, 7/7 manifest hashes PASS. TWO clean fresh-directory reruns executed with OPENBLAS_NUM_THREADS=1; BOTH scripts generated BOTH JSONs BYTE-IDENTICAL to frozen archive. All mathematics self-contained with NumPy+SymPy; code not claimed uploaded to GitHub.

## Source/physical boundaries and custody
No original dtc0a_runtime_v0_3_1.py, no historical h=fI/K_A masks, no original-source E_alpha rerun in ROT032. This is ONLY fixed metric-independent all-integral SL3(Z) F=S tensor I6 finite representation algebra on SQUAREFREE grids, not metric-transported F_g, curved York, Noether/gauge covariance, gravitational-wave polarizations, J3/K physics, physically chiral excitations or novelty. Maturity does not imply NASH physical improvement. Independent referee, BW ING, owner uptake and Moderator EXEC all PENDING; no task cascade.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
