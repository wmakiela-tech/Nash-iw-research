---
artifact_id: IW_INT8_ROT039_FLAT_METRIC_UNIFORM_COORDINATE_STENCIL_ARITHMETIC_001_20261027
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_AFFINE_METRIC_TT_RAW_WAVEVECTOR_ALIAS_INTERFACE_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_FINITE_UNIFORM_STENCIL_ARITHMETIC / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT039 — sharp arithmetic of uniform coordinate stencils across a natural flat metric orbit

## Ownership, closest mathematical host, and delimiters
INT8 ROT033 FIRST established the metric-orbit source-stabilizer iff, with U_A H(x)=A^T H(Ax mod N)A, g_A=A^T A and F_g=U_A F_I U_A^-1. INT8 ROT029–032 FIRST owns ONE fixed all-shear-invariant tensor operator classification, which is a distinct requirement. ROT034–038 FIRST own RAW source TT finite/asymptotic locality/idempotence obstructions, using source zero/mean-zero carrier contracts. MT13 FIRST produced affine E_g and identified naive target raw-k TT alias. M14 historical puretrace and masked K_A; Geeky even-N RAW; XH curved York; PRF Lie/TT remain separately owned.

Standard external host: integer elementary group operations, orbit classification by gcd ideals over Z/N, finite abelian group Fourier decomposition, homogeneous-space stabilizer descent. Prior-art examples: Degenerations and orbits in finite abelian groups, JCTA 118 (2011), 1685–1694, DOI 10.1016/j.jcta.2011.02.002; https://math.stackexchange.com/questions/739059/orbits-of-action-of-sl-m-mathbbz-on-mathbbzm . Mathematical originality and physical significance are NOT claimed.

## Exactly defined mathematics
N>=3 is ODD. X_N=(Z/N)^3. V_N consists of real symmetric rank2 covariant tensor fields on X_N. A in SL3(Z) acts U_A H(x)=A^T H(Ax)A, satisfying U_A U_B=U_(BA). Flat, constant orbit metrics g_A=A^T A. A fixed TRANSLATION-INVARIANT real source operator F_I has convolution K_I(s), a general 6 by 6 tensor matrix per displacement s. For a metric-only well-defined natural family on all g_A, assume F_I commutes with 24 proper signed-coordinate rotations SO3(Z), per prior ROT033. No demand that F_I be the SAME operator equivariant under all nonorthogonal shears.

Conjugation gives the EXACT source support transport:
  supp K_(g_A) = A^-1(supp K_I) mod N.         (039.1)
The invertible tensor fiber congruence changes blocks, not their zero/nonzero status; A permutes displacements without collisions. The UNIFORM COORDINATE-CUBE stencil contract requires for every integer A:
  supp K_(g_A) is in [-R,R]^3,
where signed coordinates of residues are chosen in [-(N-1)/2,(N-1)/2]. This is deliberately coordinate-specific and should NOT be mistaken for intrinsic g-metric locality.

## T039.1 — precise all-A support permission from gcd vector orbits

For displacement s define delta(s)=gcd(N,s1,s2,s3), a divisor d of N. Elementary row operations modulo N, CRT over p^a and lift from elementary SL3(Z/N) give exactly ONE SL3(Z) orbit per gcd ideal:
  Omega_d = {s : gcd(N,s1,s2,s3)=d}.
Because coordinates of Omega_d are multiples of d and N/d is odd, the maximum possible signed coordinate radius in this orbit is
  r(d) = d floor((N/d)/2) = (N-d)/2.           (039.2)
Exact attainment: t=(N/d-1)/2 and C=[[t,-1,0],[1,0,0],[0,0,1]] has determinant 1, sending (d,0,0) to (d t,d,0), where signed coordinate radius is (N-d)/2 and gcd class remains d.

Therefore the ENTIRE classification of natural sources of UNIFORM coordinate radius at most R is
  supp K_I subset D_(N,R),
  D_(N,R)={0} union over d|N, d<N with (N-d)/2<=R of Omega_d.
This is an IFF after separately imposing 24-rotation source compatibility. Important: source support need only be a SUBSET of allowed gcd strata, not necessarily a union of full strata; the stronger SAME all-A invariant source would have full gcd-orbit support.

## T039.2 — SHARP minimum for any non-onsite all-flat-metric family

Write p=p_min(N), smallest prime divisor of N. Its largest proper divisor is d*=N/p. Hence
  R_*(N)=min_(proper d|N) r(d)=(N-N/p)/2.     (039.3)
Every natural translation-invariant family uniformly bounded by coordinate radius R<R_*(N) MUST be ONSITE. Conversely a genuine non-onsite natural family exists at R=R_*(N), even an exact orthogonal projection at every g, constructed below. For prime N, p=N and R_*=(N-1)/2, the full grid cube radius. For composite N proper gcd classes admit intermediate radii.

| N | p_min | largest proper d | first non-onsite R_* | full m |
|---:|---:|---:|---:|---:|
| 9 | 3 | 3 | 3 | 4 |
| 15 | 3 | 5 | 5 | 7 |
| 21 | 3 | 7 | 7 | 10 |
| 31 | 31 | 1 | 15 | 15 |
| 33 | 3 | 11 | 11 | 16 |
| 35 | 5 | 7 | 14 | 17 |
| 39 | 3 | 13 | 13 | 19 |
| 41 | 41 | 1 | 20 | 20 |
| 45 | 3 | 15 | 15 | 22 |

Examples of ALL possible gcd-stratum entry thresholds:
N35: d7 requires R14, d5 requires R15, d1 requires R17;
N33: d11 R11, d3 R15, d1 R16;
N39: d13 R13, d3 R18, d1 R19.

## T039.3 — explicit attaining constructions: six-shift convolution AND g-orthogonal projector

Let d=N/p with p=p_min(N).

Sparse example: T_I H(x)=(1/6) sum_{i=1}^3 (H(x+d e_i)+H(x-d e_i)). Its source seed is invariant under all proper signed coordinate rotations, so the natural transported family T_g exists, with 6 nonzero shift blocks, each of gcd d, uniformly r_coord(T_g)<=R_* and attaining R_* for a suitable A. It is generally NOT a projector.

Genuinely PROJECTIVE example: subgroup H_d=d X_N has p^3 shifts and is invariant as a set under ALL SL3Z grid automorphisms. Let S_d be spatial averaging over that subgroup:
  S_d H(x)=1/p^3 sum_{u∈(Z/p)^3} H(x+d u).
It is orthogonal, idempotent, translation-invariant and invariant under all SL3(Z) node permutations. Define pointwise tracefree tensor projector, geometrically:
  Q_g H(x)=H(x)-(1/3)g tr(g^-1 H(x)).
Then
  F_g=S_d Q_g                                          (039.4)
is a natural g-orthogonal IDEMPOTENT family, has EXACTLY the p^3 nonzero shift blocks of H_d, and uniform coordinate radius EXACTLY R_* at every g. Its Fourier multiplier keeps only modes k with each k_i divisible by p, giving d^3 spatial frequencies; Q_g rank5 fiber gives total real tensor rank 5d^3. E.g.
  N35: 125 shifts, 343 retained modes, rank 1715;
  N33: 27 shifts, 1331 modes, rank 6655;
  N39: 27 shifts, 2197 modes, rank 10985;
  N31 prime: full N^3 spatial average, only k=0 retained, tensor rank5.
This is tracefree, NOT transverse-traceless TT, NOT original E_g and NOT original historical masked K_A.

## T039.4 — preserved intrinsic metric radius versus changing fixed coordinates

True flat periodic metric distance for a displacement s is
  rho_g(s)=min_{z∈Z^3} [(s+Nz)^T g(s+Nz)]^(1/2).
For g_A=A^T A and t=A^-1 s, integer unimodular A bijects Z^3:
  rho_(g_A)(t)=min_z ||A(t+Nz)||=min_w||s+Nw||=rho_I(s).
Thus metric-transport preserves INTRINSIC geodesic support distances EXACTLY. The above obstruction arises solely from a common FIXED coordinate cube, which is not itself a geometric invariant.

Exact numerical illustration: N35, p5, d7. C=[[2,-1,0],[1,0,0],[0,0,1]], B=C^-1=[[0,1,0],[-1,2,0],[0,0,1]], g=B^T B. Source shift s=(7,0,0) transports under B to C s=(14,7,0); fixed coordinate radius rises 7→14 while rho_g((14,7,0))=rho_I((7,0,0))=7 EXACTLY. No physical locality has been lost.

## Independent executed validation and important negative control

ROUTE A independent Python BFS + NumPy: six elementary integer shears partition ALL N^3 spatial sites for EACH 12 grids N=3,5,7,9,15,21,31,33,35,39,41,45; all disjoint orbit counts match direct gcd counting, every orbit max coordinate radius is r(d), all nodes covered. Three random FULL real symmetric-tensor-field tests N9,d3; N15,d5; N35,d7: direct U_A S_d Q_I U_A^-1 and explicit S_d Q_g match within 2e-11, transported support set matches, projective idempotence PASS. Independent Fourier mask checks preserve exactly d^3 modes and agree with subgroup averages. No historical DTC0a helper was invoked; these results are pure operator mathematics.

ROUTE B separate source-free SymPy script, not importing NumPy or ROUTE A: 12/12 exact integer witnesses determinant1, correct gcd-class maximal coordinate shift, exact metric length rho squared d² for witness, exact rational tracefree-projection transport formula, exact closure of p³ subgroup shifts in the bounding cube, exact 5d³ rank arithmetic. Independent execution PASS.

Early exploratory FAIL correctly recorded: ROUTE A initially represented the ZERO orbit d=N by a FLAT array offset start=N (wrongly node (0,1,0)) rather than start=d mod N=0, triggering a gcd invariant assertion. Corrected before scientific acceptance; full 12-grid rerun PASS.

Moderator-local FULL reproducibility archive iw_int8_rot039_uniform_coordinate_metric_stencil_arithmetic_bundle.zip has SHA256
  039b6c5a73f3a05a01940b230f9d92d89116bbc311435984ec304e3c4d3715d2.
Eight members: full 12.6KB Polish source-faithful report (SHA256 dfff73f65b91f6dc9648f180559da2f5180f4a2fd399f24b58ba331c7429076f), two independent standalone runnable programs, two JSON outputs, README, runlog, SHA256SUMS. ZIP CRC PASS, SHA256 7/7 payloads PASS. TWO FRESH CLEAN independent extractions; both programs rerun; BOTH resulting JSON files BYTE IDENTICAL to archived in BOTH replays. Code not falsely claimed separately published to GitHub.

## Strict STOP
ONLY odd finite grids, constant flat positive-definite integer unimodular metric orbit, translation-invariant convolution kernels and ALL integral shears. Not physical full TT, not original K_A, not even Nyquist RAW, not arbitrary curved metrics, GR gauge, J3/K, Noether or experimental claims. Geodesic metric locality is exactly preserved; coordinate-cube cost is a coordinate choice, not geometry failure. No math novelty, no canon, no physical upgrade. BW ING, owner uptake, independent referee and Moderator EXEC pending. No new task cascade.
