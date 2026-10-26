---
artifact_id: IW_INT8_ROT036_ZERO_MODE_RANK_EXTENSION_AND_GEOMETRIC_STABILIZER_GUARD_001_20261026
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_SOURCE_TYPED_MEAN_ZERO_TT_LOCALITY_AND_STABILIZER_INTERFACE_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_FINITE_RANK_EXTENSION_ALTERNATIVE / EXPLICIT_FINITE_COUNTEREXAMPLE / STABILIZER_NO_GO / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# INT8 ROT036 — Zero-mode extension is the exact finite-grid locality hinge; geometric stabilizer removes the onsite loophole

## Attribution, mature host, scope

**MT13 first** developed source-matched metric-transported affine E_g and identified naive raw-wavevector target TT aliasing. **INT8 ROT033** already proved flat integer metric-orbit naturality iff the seed commutes with the 24-element SO(3,Z) stabilizer. **INT8 ROT034** first proved ALL N³ shifts are needed for full-source idempotent TT approximation <1, using *source* rank5 at k0 and rank2 at other modes. **INT8 ROT035** removed k0 from the error norm and first proved SHARP asymptotic sublinear-stencil locality gaps 1 for projectors, 1/2 for linear maps. This ROT036 does NOT silently promote ROT034 to the mean-zero carrier; instead identifies its exact zero-mode-extension condition and shows a real finite-N counterexample when it is absent. Geeky-S11 owns even-grid RAW real-cast; M14 historical h=fI/KA masks; XH curved York; PRF12 separate Lie/TT. External mathematics is classical DFT, transversality of finite-dimensional subspaces, rank of nearby idempotents and octahedral representation decomposition (trace dimension1, diagonal tracefree dimension2, offdiagonal dimension3), not mathematical novelty. Cubic-character/table descriptions: https://www.wiredchemist.com/chemistry/data/cubic-groups .

## Carrier and essential distinction

For ODD N>=3, G_N=(Z/NZ)^3. V_N denotes ALL real symmetric 3x3 tensor fields, V_N^0 ONLY MEAN-ZERO tensor fields. The **retained unchanged user helper** deepseek_python_20260627_a87249.py, SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801, defines source raw Fourier TT projector P with rank 5 at k0 (tracefree) and rank2 at every k!=0. Historical byte-exact original production dtc0a_runtime_v0_3_1.py remains unavailable, so no historic masked K_A is tested.

F is a REAL translation-invariant IDEMPOTENT on the FULL V_N, not merely an abstract map defined on V_N^0, so F has a unique kernel K_F(d) and a WELL-DEFINED zero-frequency symbol Fhat(0). But approximation is measured ONLY on V_N^0:
 eps = ||(F-P)|_(V_N^0)||_(L2->L2).
F need NOT be local, orthogonal, or stabilizer equivariant unless explicitly stated. Let r0=rank(Fhat(0)) in {0,...,6}.

## T036.1 — exact finite-N zero-mode-rank/support alternative

If eps<1, rank stability of idempotents applied SEPARATELY at each nonzero Fourier mode forces rank Fhat(k)=rank Phat(k)=2 for ALL k!=0. Therefore
 tr Fhat(k) = 2+(r0-2) 1[k=0].
The INVERSE 3D discrete Fourier transform gives the exact identity for EVERY spatial displacement d:
   tr K_F(d) = 2 1[d=0] + (r0-2)/N³.           (T036.1)

- If **r0 != 2**, every nonzero d has nonzero block trace, so every K_F(d)!=0. At d=0, trace 2+(r0−2)/N³>0 for N>=3. Consequently supp(K_F)=ALL N³ offsets, finite-N EXACT.
- If **r0=2**, trace K_F(d)=2 1[d=0]; the trace proof imposes NO nonzero kernel at distant d. This is not an existence claim by itself, but T036.2 supplies genuine onsite counterexamples.

Additional modelling distinction: a convolution automatically maps mean-zero fields into mean-zero fields; requiring only **mean-zero preservation** therefore does NOT fix r0. If one imposes **annihilation of all constant fields** Fhat(0)=0, then r0=0 and exact full N³ support follows whenever eps<1. A map specified ONLY on V_N^0 with no full-kernel extension has no defined r0, so T036.1 cannot be invoked there.

## T036.2 — every FIXED finite odd N admits an onsite projector with eps<1

Fix ANY finite odd N. For each nonzero k, Pk is a real orthogonal rank2 projector on the six-dimensional symmetric tensor fiber. Let Q=(H1,H2) be two linearly independent real symmetric tensors and E the orthogonal projector onto their span, applied POINTWISE at every lattice node. Thus Ehat(k)=E for all frequencies, rank(E)=2 even at k0 and spatial kernel has ONLY K_E(0)=E.

For each particular k, the condition
  det [<Hi,Pk Hj>_F]_(i,j=1,2)>0                 (T036.2)
is equivalent to transverse 2-planes / both TT principal angles <pi/2 and to ||E-Pk||op<1. The determinant is a polynomial in the 12 real coefficients of H1,H2 and is NOT identically zero (take the two tensors as an orthonormal basis of range Pk). A FINITE union of proper polynomial-zero sets cannot cover the real coefficient space; rationals are dense in the resulting nonempty open set. Hence two rational tensors can be selected satisfying (T036.2) SIMULTANEOUSLY for all finitely many nonzero k. Therefore at each FIXED odd N there exists an onsite real orthogonal rank2 E_N with:
  ||(E_N-P)|_(V_N^0)|| < 1.
No claim that the same E works for all N. This DOES NOT contradict ROT035: for any sequence of such radius0 projectors the optimal approximation error still tends to 1 as N->infinity.

### Literal integer-tensor example, exact cubic certificate, verified N<=201

One specific pair:
 H1=[[-4,-2,-1],[-2,1,-1],[-1,-1,4]]
 H2=[[2,-3,-3],[-3,-4,3],[-3,3,-3]].
Its Frobenius Gram matrix G=[[45,-12],[-12,83]], detG=3591.

Independently from the source helper, original definition of Pk applied to this pair yields EXACTLY:
 det [<Hi,Pk Hj>] = f(x,y,z)^2/(x²+y²+z²)^3,    (T036.3)
where k=(x,y,z)≠0 and
 f=10x³−10x²y+19x²z+13xy²+23xyz−15xz²+29y³−22y²z+3yz²−27z³.

A SEPARATE rational SymPy audit proves this polynomial identity symbolically, not by floating fitting. The actual main Python enumerated **ALL 9,254,204 nonzero signed integer frequency vectors** across N=3,5,7,9,15,31,41,101,201, and f had ZERO nonzero-k roots throughout; min abs f=3 at N3 and 1 at each other tested N. Second independent Python-integer loop verified N3/5/9/15/31/41. It is NOT asserted that this particular cubic has no integer roots for all arbitrarily large k.

For all tested modes f²>=1. The normalized compression eigenvalues 0<lambda1<=lambda2<=1 obey
 lambda1 lambda2 = f²/(3591 |k|^6).
Hence lambda1>=f²/(3591|k|^6). With m=(N−1)/2 and |k|²<=3m²:
 max_(k!=0)||E-Pk|| <= sqrt(1−1/[3591(3m²)^3]) < 1.
The bound is conservative but rigorously STRICT. Independent 6D numerical eigen scan gives for this particular E:
 N3 .99963974194028; N5 .99999326156456; N9 .99999462087380;
 N15 .99999983194188; N31 .99999999753151.
These values are NOT optima over all onsite E, only the one explicit witness. This E is NOT stabilizer equivariant. On the FULL source carrier (including original rank5 P(0)), rank E(0)=2 conflicts with rank P(0)=5, forcing full-L2 error>=1 (ROT034).

## T036.3 — onsite loophole eliminated by the exact geometric stabilizer contract

The ROT033 metric-indexed natural family on integer-flat orbit needs E_I to commute with SO(3,Z), the 24 proper signed coordinate permutations. On the real six-dimensional symmetric tensor fiber their action decomposes into 1-dimensional trace, 2-dimensional diagonal-tracefree, and 3-dimensional offdiagonal irreducible spaces. Their commutant has exactly dimension3. Independent SymPy constructs all 24 real 6x6 representation matrices and 24*36=864 linear commutator equations in 36 unknown coefficients; the exact rational equation matrix has **rank 33**, so its kernel dimension is **3**. Three explicit commuting projectors with ranks1,2,3 span that kernel. Therefore the ONLY idempotent commuting with all 24 rotations and having rank2 is
 E_diag(H)=diag(H11−tr(H)/3,H22−tr(H)/3,H33−tr(H)/3).

For k=e1, the normalized offdiagonal yz tensor is a TRUE TT polarization: P_(e1)H_yz=H_yz, but E_diag H_yz=0. Thus at every odd N>=3:
 inf_(E²=E, onsite, all-24-stabilizer-equivariant)
 ||(E-P)|_(V_N^0)|| = 1.
Upper bound is attained by E_diag itself, since differences of orthogonal projectors have norm <=1. This is a FINITE-N EXACT result for onsite stabilizer-equivariant projections only. No conclusion for radius R>0 without a separate proof.

Consequently: (i) mean-zero alone permits finite-N local projections <1, (ii) additional zero-mode annihilation makes ALL-shift support obligatory, and (iii) geometric SO3(Z) seed naturality already excludes an onsite <1 projector even with r0=2. Do not combine distinct assumptions.

## Executed controls, reproducibility, negative knowledge

MAIN NumPy standalone checks: exact integer cubic scan all 9 N, 9,254,204 nonzero wavevectors, full Frobenius Gram, numerical principal angles p3/5/9/15/31, algebraic r0 table, optional byte-SHA-verified retained source apply_P_TT on nine genuine mean-zero cosine fields N5/9/15 (all max elementwise deviations <3e−13). Original helper is NEVER included in ZIP and absent helper gives explicit SOURCE SKIPPED.

SEPARATE independent SymPy/stdlib source-free script: exact symbolic squared-cubic determinant identity; 24 group actions and 864 exact linear constraints of rank33; unique rank2 diagonal-tracefree invariant projector; exact offdiagonal yz witness; independent pure-Python integer grid tests N3/5/9/15/31/41. It imports no functions from main script.

NEGATIVE KNOWLEDGE: An initial exploratory test mistakenly performed invalid NumPy matrix multiplication on tensor-shaped 2x3x3 arrays and stopped with ValueError; removed this unused operation BEFORE accepting outputs. The exploratory rounded-Frobenius tensor pair was replaced with a SEPARATELY derived exact integer-tensor witness and rational re-audit. The existence theorem is NOT inflated into a claim that the displayed cubic is anisotropic over Q for all integer k.

COMPLETE Moderator-local ZIP:
 iw_int8_rot036_zero_mode_rank_stabilizer_repro_bundle.zip
 SHA256 **d2d976d76c4ab452c75b1fd98281cd4357d20fd6f270163b8802031beb12e110**.
Eight members: full 11KB Polish mathematical report, two standalone Python scripts, two detailed JSONs, runlog, README and SHA256SUMS. ZIP CRC PASS, SHA256 7/7 PASS. TWO independent clean extractions/replays: original helper PRESENT both JSON BYTE IDENTICAL to frozen source, helper ABSENT math and independent SymPy unchanged, source explicitly SKIPPED.

## Strict physical/scientific STOP

ONLY finite odd signed-RAW-k DTC0a-helper TT, full tensor input mean-zero L2, fixed flat Euclidean frame, explicit r0 extension and finite 24 stabilizer. No historic masked K_A, no original production runtime byte proof, no even-grid real-cast, arbitrary curved York, Noether/GR gauge, physical GW energy, NCDG J3/K, no mathematical originality claim. BW ING / external referee / original scientific owner / Moderator EXEC all PENDING. NO_NEW_TASK.
