---
artifact_id: IW_INT8_ROT031_PRIME_GRID_REAL_WEDDERBURN_AND_SHARP_TT_MINIMAX_001_20261026
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_METRIC_NATURALITY_FILTER_OPERATOR_HOST_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_FINITE_ALGEBRA_AND_SOURCE_TYPED_MATHEMATICAL_NOGO / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT031 — Real Wedderburn structure on prime grids; sharp 1/2 versus 1 approximation of source TT

## Other owners, prior art, currentness

Source dispatch currentness checked 2026-10-26. INT8 ROT029 ALREADY established for arbitrary N and no locality/translation requirement: each ONE fixed, metric-independent all-integral-SL3 tensor-pullback-equivariant real linear map is F=S tensor I_6, with S acting on spatial nodes only. ROT030 ALREADY classified permitted S via pair-orbits and subgroups, with dimension p+3 at N=p prime. ROT018–022 previously settled smaller translation-invariant convolution class; ROT023–028 analysed metric/raw-k Fourier TT alias, sharp singular norm, rank and repair. MT13 FIRST exhibited metric-indexed affine stencil covariance E_g U=U E and the raw-k alias defect. XH-S4 owns genuinely curved York; M13 owns historical h=fI/masks/K_A; Geeky-S11 owns RAW/matched-symbol and even-grid convention differences; PRF11 owns Lie/TT collocation. These are not reattributed.

**External mature host FIRST:** Amritanshu Prasad, mathematical discussion on the GL_n(F_q) nonzero-vector permutation representation, 24 December 2013, https://mathoverflow.net/questions/152726/decomposing-representations-of-gln-f-q-induced-from-certain-kinds-of-parabolic : the nonzero pair orbital algebra has q scalar relative-position classes and is COMMUTATIVE, hence multiplicity-free. Broader peer-reviewed host: Matthew Bardoe and Peter Sin, The permutation modules for GL(n+1,q) acting on projective n-space and nonzero vectors, J. London Math. Soc. 61 (2000), pp. 58–80, DOI 10.1112/S002461079900839X. Standard Schur/Maschke real representation theory and basic orthogonal projection gaps are mature. ROT031 claims only a project-local explicit specialization and two source-typed minimax certificates, NO original mathematical or physical novelty.

## Strong mathematical assumptions / coordinates

For p prime, X=F_p^3; V_p=all real symmetric covariant 3x3 tensors over X, dimension 6p^3. For every A in SL3(Z), U_A H(x)=A^T H(Ax mod p) A; tensor fiber action uses real, NOT modular, matrices. A single F fixed and independent of metric commutes with ALL U_A, including all lifts A congruent to I mod p. ROT029 therefore enforces F=S tensor I_6. Spatial S commutes with the permutation action of SL3(F_p). No translation, convolution, locality, orthogonality or positivity assumption on S unless explicitly stated. Distinguish this FIXED operator contract from covariance of a METRIC-TRANSPORTED family F_g, which is permitted.

Put X*=X\{0}; M=p^3−1, L=(p^3−1)/(p−1)=p^2+p+1. Let e0=delta_0 and u=M^(−1/2)1_X* be the two orthonormal invariant spatial vectors.

## T031.1 — EXACT real *-algebra structure

For every ODD prime p:
  A_p=End_SL3(F_p)(R^X) is isomorphic as real *-algebra to
    M_2(R) direct_sum R direct_sum R direct_sum C^((p−3)/2).
Its real dimension is 4+1+1+(p−3)=p+3. For p=2, A_2=M_2(R) direct_sum R, dimension 5.

**Independent elementary proof, not relying only on dimensions.**
- Nonzero x,y have exactly p orbitals: y=lambda*x for each lambda in F_p* (p−1 orbitals), or independent x,y (one). On X*, the orbit algebra has basis scalar multiplications R_lambda f(x)=f(lambda*x), along with constant averaging J. Since R_lambda R_mu=R_(lambda*mu) and J commutes with each R_lambda, this whole algebra is commutative; multiplicity one for each of its p complex irreducible summands.
- Adding the zero node creates TWO copies of the trivial module, span(e0,u). Their 4-dimensional real endomorphism algebra is the full M_2(R), including offdiagonal maps between zero and nonzero mean.
- The trivial scalar-character sector on X* is the L-dimensional space of functions constant on each projective line. Remove u to obtain the projective mean-zero real irreducible sector of dimension L−1 and real commutant R.
- F_p* has one additional REAL quadratic character for odd p, giving an irreducible real sector of dimension L with scalar endomorphisms R.
- The other p−3 characters occur in (p−3)/2 complex-conjugate pairs. Every pair forms a real irreducible sector of dimension 2L with real commutant C (selfadjoint part the real scalars).
- All these components are exhausted because 2+(L−1)+L+((p−3)/2)*2L=p^3 and the algebra's 4+1+1+(p−3)=p+3 equals the ROT030 independently established orbital dimension. No hidden equivalent multiplicities can remain.
For p=2 there is no quadratic or nonreal character.

## T031.2 — ALL equivariant orthogonal projections, their legal ranks

The commuting spatial ORTHOGONAL projectors S have independent pieces:
(a) any real orthogonal 2x2 projection on span(e0,u), ranks r0 in {0,1,2}; rank-one choices have a continuous angle theta, image span(cos(theta)e0+sin(theta)u);
(b) either whole projective-mean-zero sector L−1 or zero, bit a;
(c) whole quadratic sector L or zero, bit b;
(d) each 2L-dimensional conjugate-character sector or zero, bits c_j.
Thus for odd p:
  rank S = r0 + a(L−1)+b L + 2L sum_(j=1)^((p−3)/2)c_j,
  r0=0,1,2 and a,b,c_j in {0,1}.
On full symmetric tensor fields F=S tensor I6, rank(F)=6 rank(S), always divisible by six. The *algebra* includes continuous families of NONTRANSLATIONAL projections; universal tensor equivariance does NOT force global scalar operators on all spatial nodes.

Examples: p=5, L=31, sectors have spatial dimensions 2+30+31+62=125 and algebra M2(R)+R+R+C (real dimension 8). Mixed rank-one trivial plus projective plus quadratic projector has spatial rank 1+30+31=62, tensor rank372. p=31, L=993, decomposition 2+992+993+14*1986=29791, algebra dimension34, example mixed-plus-projective-plus-quadratic spatial rank1986, tensor rank11916.

## T031.3 — TWO exact, attained distance-to-original-TT minima

For ALL odd N (not merely prime), use the unchanged retained SOURCE raw-k Fourier TT projector P=P_TT on real symmetric tensors with flat-Frobenius L2. It is orthogonal for ODD N with nonzero-mode TT fiber rank2 and original k=0 TRACEFREE rank5, hence
   rank(P)=2(N^3−1)+5=2N^3+3.
Let C_N be the full real space of fixed all-integral-SL3-equivariant maps, i.e. F=S tensor I6 by ROT029.

**Without requiring F to be a projector:**
  inf_(F in C_N) ||P−F||_(L2→L2) = 1/2.
Proof LOWER: on a common normalized constant spatial mode choose normalized tracefree tensor T and normalized pure-trace tensor I/sqrt3. P(T)=T, P(I/sqrt3)=0, while the projection of ANY S tensor I6 to the constant spatial component is the SAME scalar c=<1,S1>/<1,1> on both tensor polarizations. The operator norm is therefore at least max(|1−c|,|c|)>=1/2. Proof UPPER: F=I/2 is universal and ||P−I/2||=1/2 since P is an orthogonal projector. No translated-metric family or source-typed input restriction is hidden.

**Requiring F^2=F, even permitting NONORTHOGONAL idempotents:**
  inf_(F in C_N,F²=F) ||P−F||_(L2→L2) = 1.
Proof LOWER: all such F=S tensor I6 have rank divisible by six. But 2N^3+3 for odd N is never divisible by six. Two finite-dimensional idempotents with UNEQUAL ranks differ in operator norm by at least 1: whichever has greater rank has a nonzero range vector in the other's kernel, giving difference equal to ±the vector. Proof UPPER: the zero projector F=0 has ||P||=1. For UNIVERSAL ORTHOGONAL projectors the operator distance to P is exactly 1; for oblique idempotents it may exceed 1. A source-TT-only admissible subspace, removal of k0, or changing the metric-indexed operator family defines a DIFFERENT minimax problem and is not covered by these sharp constants.

## Fully executed independent checks and clean replay

Route 1 (original standalone NumPy code): finite projective-line + primitive-root radial character Fourier decomposition for p=2,3,5,7,11,31; exhausts all p^3 components, orthogonal idempotence, commutation with all six elementary shear matrices on random source spatial vectors, continuous angle mixed rank-one projection, exact derived rank lists. All 6/6 prime grids PASS. p=31: expected algebra dim34 and projective L=993 PASS.

Route 2 (DIFFERENT code, no Fourier-character decomposition): constructs all exact p+3 pair-orbital indicator matrices, checks disjoint complete basis and invariance under six shears for p=2,3,5,7; direct closure under multiplication of EVERY orbital pair p<=5, not only count. Additionally builds fully dense real radial/projective/quadratic matrices for p<=5 and checks symmetry, P²=P and eigenvalue-counted ranks (p5: projective30, quadratic31, mixed1). All PASS. This is independent of Route 1.

Literal source route: user-retained UNMODIFIED helper deepseek_python_20260627_a87249.py SHA256
 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801
imported unchanged; original apply_P_TT returns orthogonal projector and preserves constant tracefree tensor while killing constant puretrace on odd N=3,5,7; original apply_E(E_lin) preserves constants. Native tests PASS; the historical original production dtc0a_runtime_v0_3_1.py remains BYTE UNAVAILABLE.

Complete LOCAL Moderator ZIP: iw_int8_rot031_prime_wedderburn_tt_minimax_bundle.zip; SHA256 **744723f49a8bfd89c6f9f91aa2df46e641319d486fb2f69a81121810d568dad3**, 8 members: full 11.7KB Polish report, two executed stand-alone Python scripts, two detailed JSONs, log, README, SHA256SUMS. ZIP CRC PASS, SHA256 **7/7 PASS**. Two independent clean extracted directories rerun all math; with source helper literal SHA-check PASS and both JSON files BYTE IDENTICAL; without source helper math PASS and source marked SKIPPED, not falsely claimed source validation. CODE lives in the complete Moderator local ZIP, not falsely claimed uploaded to GitHub.

## Strict stop
This result is FINITE representation/operator algebra, does NOT prove physical metric-covariance/gauge, background independence, true curved York, gravitational wave conservation, J3/K, Noether, curved Lorentzian Box, historical masked K_A, or a new mathematical discovery. BW source ingest, independent referee, owner acceptance and Moderator EXEC remain PENDING. No new task cascade. NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
