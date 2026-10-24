---
artifact_id: IW_INT8_ROT029_UNIVERSAL_INTEGER_SHEAR_TENSOR_COMMUTANT_COLLAPSE_001_20261025
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_METRIC_NATURALITY_FILTER_OPERATOR_HOST_001
exposure: PUBLIC_SAFE
science_status: EXACT_THEOREM / SYMPY_RATIONAL_AND_RET_N_SOURCE_EXEC_PASS
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT029 — complete fixed universal integral-shear tensor operator commutant

## Others first and claim scope
INT8 ROT018–019 previously classified scalar TRANSLATION-INVARIANT SL3(Z) convolution using gcd frequency orbits, ROT020–022 optimized its E_lin approximation. INT8 ROT023–028 gave alias and principal-angle TT projector tests. MT13 FIRST constructed metric-transported affine-flat E_g family and FIRST identified raw-k metric TT alias failure. XH-S4 owns curved York and metric naturality; Geeky-S11 owns separate raw vs matched-symbol TT and even-grid stencil rigidity; M13 historical source puretrace h=fI and masked K_A, PRF11 distinct Lie/TT commutator. The NEW, narrow scientific contribution of this lineage: classification of ALL real linear fixed SAME-operator SL3-equivariant maps, not only translation-invariant scalar convolutions. Underlying Sym2 representation theory is standard mature mathematics, NO novelty or physics claimed.

## Theorem: general arbitrary linear operators (any N>=1)
Let G_N=(Z/NZ)^3, V_N={H:G_N->Sym2(R^3)}, dim=6N^3. For ANY integral A in SL3(Z), act on covariant tensors by
  (U_A H)(x)= A^T H(Ax mod N) A.
One FIXED metric-independent real linear F:V_N->V_N commutes with EVERY U_A if and only if
  (F H)(x)=sum_(y in G_N) s(x,y) H(y),
  s(Ax,Ay)=s(x,y) for ALL A,x,y.
Equivalently F=S tensor I_6 where S commutes with the finite SL3(Z/NZ) permutation action. Neither locality NOR translation invariance is assumed.

### Elementary full proof
For every i!=j and integer q, A=I+qN E_ij acts as IDENTITY on lattice sites x mod N, but the real symmetric-tensor fiber transforms R_A H=A^T H A. Write ANY F in 6x6 fiber blocks F_xy. Commutation with U_A forces [F_xy,R_(I+qN Eij)]=0 for each x,y. Each matrix entry of the commutator is a polynomial of degree <=2 in qN, vanishing at all integer q; hence it vanishes for all real t in I+t Eij. Elementary transvections generate SL3(R).

The commutant of Sym2 R^3 under SL3(R) is exactly scalars, proved WITHOUT invoking an unverified irreducibility assertion: commuting with all diagonal diag(a,b,(ab)^-1) implies F_xy is diagonal in tensor basis xx,yy,zz,xy,xz,yz, whose characters a²,b²,(ab)^-2,ab,b^-1,a^-1 are all distinct. The elementary derivative of the congruence action Eij maps ii -> ij -> 2jj, forcing diagonal coefficients ii,ij,jj identical for every i!=j. Their graph is connected, so F_xy=s(x,y) I_6. General A commutation yields s(Ax,Ay)=s(x,y); converse direct.

**Positive nontranslation controls:** spatial projection H(x)->1_(x=0)H(0) and global mean H(x)->N^-3 sum_y H(y) both commute with all U_A, despite first being nontranslation invariant. This is NOT a claim that all F=cI on entire V_N, only that all F are tensor-FIBER blind.

## Corollaries to arbitrary 6x6 tensor-coupled convolutions and TT
If F also commutes with translations, Fourier symbol is t(k)I_6; all SL3Z action forces t(A^T k mod N)=t(k). INT8 ROT019 already proved frequency orbits indexed exactly by gcd(kx,ky,kz,N). Thus arbitrary tensor-coupled translation-invariant kernels collapse EXACTLY onto old scalar orbit class with tau(N) real parameters; allowing 6x6 coupling cannot evade old fixed-kernel bounds. If F²=F, then t_d∈{0,1}; exactly 2^tau(N) translation-invariant fixed fully equivariant projectors exist (N31,41: 4; N33,35,39:16), each passing all six tensor components of an orbit or rejecting all.

Even WITHOUT translation invariance, any equivariant projector F=S tensor I_6 has rank 6 rank(S), a multiple of six. The UNMODIFIED source raw-k P_TT has Fourier rank2 at each nonzero k and rank5 at zero k (tracefree), total rank=2(N^3-1)+5=2N^3+3, NEVER divisible by six. Therefore NO fixed metric-independent all-integer-shear equivariant F (even arbitrary nonlocal/nonsymmetric/non-translation invariant) can have the SAME RANGE as source raw P_TT. This does NOT prevent metric-INDEXED natural families P_g, where g is transported with A, nor a theory selecting only one fixed metric coordinate frame.

## Exact retained DTC helper falsifier
Let H(j)=cos(2pi j_x/N) diag(0,1,-1), true source raw-k TT at k=(1,0,0). Pick A=I+N E_21: all spatial sites are fixed mod N, but fiber A^T H A differs. The source P_TT projects A^T H A back to H, while A^T P_TT(H) A=A^T H A. Therefore exactly
  ||(P_TT U_A-U_A P_TT)H||_L2 / ||H||_L2 = sqrt[(N^4+2N^2)/2].
E_lin is scalar in tensor indices, DOES commute with U_A for A≡I mod N; its eigenvalue on k=(1,0,0) is e(k)=1-4alpha sin²(pi/N). Thus the filtered P_TT-E_lin commutator on this carrier has exactly abs(e(k)) times the above ratio.

N and (unfiltered, alpha=.05 filtered) numerical:
 N5 (18.371173070874,17.101756232337);
 N9 (57.978444270263,56.622006348629);
 N31 (680.236355982242,678.843908165328);
 N41 (1189.353395757543,1187.959523980175).
The huge ratios arise from NONORTHOGONAL shears in a FIXED Euclidean tensor norm, NOT geometric isometric loss or historic K_A; never compare directly to ROT023–028 metric-relative defect numbers.

## Independently executed verification
Standalone exact SymPy rational constraints from six kernel transvections yield 216 linear equations for 36 unknown tensor-block entries; rank EXACTLY 35 for N1,3,5,31,41; nullspace generated by I_6. Independent proof checks elementary graph ii->ij->2jj and symbolic raw P_e1 rank2 and P_zero rank5 noncommutation.

Second separate script on FULL integer-valued symmetric tensor fields for N3,5,9 tested 12 integral shears per N: origin projector and spatial global sum commute in all 24 per-N positive cases, pointwise tracefree selection violates at least six shear tests, independently confirming correct theorem quantifiers. Unmodified retained helper apply_P_TT and apply_E in 4 original-source grids N5,9,31,41 reproduced the exact formulas above, relative ratio error <3e-13. Source SHA256 independently verified **23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801**. Original historical production dtc0a_runtime_v0_3_1.py byte copy remains UNAVAILABLE, and no physical diagnostic K_A is re-run.

Moderator local 8-member ZIP: iw_int8_rot029_tensor_commutant_exact_repro_bundle.zip. SHA256 **fec0209e159b95d992a7d5ed4c3446a0539816cac422b52acdf1267a0be88cc5**. It includes full 10KB Polish report, two separately executed Python proofs/auditors, exact symbolic/native JSON, independent lattice JSON, log, README and seven-entry SHA256SUMS. CLEAN unzip CRC PASS, SHA manifest 7/7 PASS. Two separate clean extracted reruns: absent helper -> exact symbolic and independent spatial tests PASS, helper SKIPPED; source-byte-SHA-checked helper PRESENT -> complete source math PASS, TWO output JSONs BYTE-IDENTICAL to archives. Source helper not bundled or redistributed. GitHub Python publication NOT claimed.

## Strict limitations
This is a stronger-than-physical FIXED KERNEL / FIXED FIBER operator requirement. Exact geometric naturality is a relation between DIFFERENT P_g objects; it is NOT forbidden by this theorem. No Noether/J3/K, metric-independent GR gauge, curved York, Lorentzian box, physically identified graviton sectors, new theory or universal measured energy follows. No independent referee, BW ingest, project owner adoption or EXEC asserted. NO_NEW_TASK.
