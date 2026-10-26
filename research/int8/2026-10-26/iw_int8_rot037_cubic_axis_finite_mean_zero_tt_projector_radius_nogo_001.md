---
artifact_id: IW_INT8_ROT037_CUBIC_HIGH_SYMMETRY_AXIS_EXACT_MEANZERO_TT_LOCALITY_001_20261026
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_SOURCE_TYPED_MEAN_ZERO_TT_LOCALITY_AND_STABILIZER_INTERFACE_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_FINITE_SYMMETRY_PROTECTED_RADIUS_NO_GO / SOURCE_TYPED / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT037 — exact finite-grid TT locality no-go after removing zero mode, with cubic seed symmetry

## Others first; prior art, exact carrier

MT13 FIRST established precisely transported flat-affine E_g filters and noted alias of the naive target raw-k TT projector. INT8 ROT033 ALREADY established the metric-indexed natural operator family iff its source seed commutes with the 24 proper signed coordinate rotations H=SO(3,Z). ROT034 FIRST proved exact all-N^3-shift locality for FULL original source P_raw using its zero-mode rank5 versus rank2 away from zero. ROT035 FIRST established only the asymptotic (N→∞, R=o(N)) mean-zero projector-versus-linear norm gaps 1 versus 1/2. ROT036 FIRST demonstrated genuine finite-N ON-SITE approximate TT projectors with error <1 WITHOUT cubic seed equivariance, AND an onsite obstruction WITH it; all positive radii R>0 remained OPEN. This result closes that precise finite-radius question. M14 owns original historic h=fI masked K_A; Geeky even raw realcast; XH curved York; PRF12 separate Lie/TT. No credit transfer.

Classical mathematical hosts: finite-group eigenspace projectors, representation compatibility along high-symmetry momentum lines, discrete Fourier inversion. Relevant prior-art analogy: Barry Bradlyn et al., Phys Rev X 7 041069 (2017), DOI 10.1103/PhysRevX.7.041069, "Topological Quantum Chemistry" band-structure high-symmetry compatibility relations. That is NOT physical applicability of crystalline band topology to NASH. No novel general mathematics or physics claimed.

Odd N=2m+1>=3. Real full symmetric 3x3 tensor fields V_N on (Z/NZ)^3 and their MEAN-ZERO subspace V_N^0. User's unchanged original helper deepseek_python_20260627_a87249.py (SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801) defines source raw-signed-k TT orthogonal projector P. At k!=0, rank(P_hat(k))=2; at k=0 historic source rank5, BUT k=0 is NEVER used in the approximation norm. Historical full dtc0a_runtime_v0_3_1.py byte-unavailable and masked K_A not run.

F:V_N→V_N is ANY REAL translation-invariant finite convolution with arbitrary 6x6 tensor-coupled spatial kernel K_F(d), idempotent F^2=F, even non-selfadjoint. It COMMUTES WITH ONLY THE FINITE H group of proper signed-coordinate rotations acting jointly on nodes and tensor fiber, as required of the seed for ROT033 metric-transported naturality. This is NOT all integer shears acting on one fixed metric, a strictly stronger and separate ROT029 setting. For norm epsilon = ||(F-P)|_(V_N^0)||_(L2→L2), no restriction to only TT source inputs and NO k0 data is measured. Cubical signed stencil radius R means K_F(d)=0 unless all signed coordinates lie in [-R,R]. Two 90-degree quarter turns O_x and O_y already GENERATE all 24 cubic rotations, so checking just those two is sufficient.

## T037.1 — entire nonzero axial spectrum forced exactly

Let O_x=90-degree rotation around x and denote by C_x: Sym²(R³)→Sym²(R³) the fiber congruence H→O_x^T H O_x. Its order is four. Its -1 eigenspace projection is
  P_x = 1/4 (I-C_x+C_x^2-C_x^3),
with rank 2 and image span{E_yy−E_zz, E_yz+E_zy}. This is EXACTLY the original rank-two Fourier TT projector at every nonzero axial signed wavevector (j,0,0), j=1,...,N−1. Under C_x, the remaining fiber eigenspaces have eigenvalues +1 (rank2) and ±i (total rank2).

The O_x-equivariance of F implies F_hat(j,0,0) commutes with C_x, hence preserves each C_x eigenblock. For every j≠0, if epsilon<1:
 - on the 2-dimensional (-1) block, F_hat differs by <1 from I and is itself idempotent; hence it MUST BE I because I−F_hat would be an idempotent with operator norm <1;
 - on all other blocks, F_hat differs by <1 from zero and is idempotent, hence MUST BE ZERO.
Therefore
  F_hat(j,0,0) = P_x for ALL j!=0.                 (T037.1)
This proves whole-MATRIX equality, not just rank equality; also valid for oblique/non-normal idempotents.

At j=0 define E0=F_hat(0,0,0), unrestricted by the error norm. The FULL cubic equivariance forces E0 to commute with C_y (90-degree rotation around y). However P_x does NOT commute with C_y. Thus E0!=P_x, EVEN if rank(E0)=2.

Take the axial margin of the full 3D spatial kernel:
  M_x(d_x) := sum_{d_y,d_z∈Z/NZ} K_F(d_x,d_y,d_z).
Fourier inversion along the axis of F_hat(j,0,0), which is E0 at j=0 and P_x at all nonzero j, gives the EXACT group-ring identity
  M_x(d_x) = P_x 1[d_x=0] + (E0−P_x)/N.          (T037.2)
Hence for every d_x!=0:
  M_x(d_x) = (E0−P_x)/N != 0.                    (T037.3)

Every one of the N−1 nonzero x-layers of spatial shifts contains at least one nonzero convolution kernel block. By cubic axis rotations, the same holds independently for every y-layer and every z-layer. This DOES NOT assert that all N³ individual blocks are nonzero.

**Stronger exact norm:** The 24-rotation real six-dimensional tensor fiber decomposes as 1(trace)⊕2(diagonal tracefree)⊕3(offdiagonal), three inequivalent irreducibles each occurring once. Thus its real commutant has dimension3, generated by the three orthogonal central projectors. Any E0 idempotent in it is the sum of a subset of these central projectors (8 possibilities), each commutes with P_x and none equals P_x. Therefore ||E0−P_x||_(Frobenius operator)=1 EXACTLY and
  ||M_x(d_x)||op=1/N  for EVERY d_x!=0.           (T037.4)
This is an exact nonzero layer-marginal amplitude, not a sum of scalar traces.

## T037.2 — SHARP FINITE N radius threshold on mean-zero only

If K_F(d) is contained in [-R,R]^3 and R<m, at least one nonzero d_x is absent in the support, so M_x(d_x)=0; this contradicts (T037.3) whenever epsilon<1. Thus the best projector approximation error is >=1 for any non-full cubic radius.

Upper bound 1 is ATTAINED by F=0, which is translationally invariant, idempotent and H-equivariant. At R=m the source P itself is a finite whole-grid convolution of signed radius m, H-equivariant on odd N, idempotent and gives mean-zero error0. Consequently for EVERY odd N:
  inf_(F²=F, translation invariant, H-equivariant, radius<=R)
    ||(F−P)|_(V_N^0)|| =
  1 if R<m; 0 if R=m.                               (T037.5)

This is NOT merely ROT035's asymptotic result, and does NOT use k0 source rank5 or assume an arbitrary real continuous-frequency polynomial projection. It is a purely DISCRETE exact spectral-sector argument.

**Crucial prior negative control:** ROT036 permits a radius-zero projector E_N with strict error <1 for EACH fixed N when H equivariance is REMOVED. That counterexample is unaltered. Without idempotence, onsite F=I/2 commutes with H and has error exactly1/2. So neither symmetry alone nor locality alone suffices for T037.5: BOTH idempotence and H source seed symmetry are load-bearing.

**Invisible-to-trace layer witness r0=2:** Define a synthetic F by F_hat(k)=P_hat(k) for k!=0 and F_hat(0)=P_diag, the cubic-invariant rank-two projection onto diagonal tracefree tensor fiber. This F has ZERO error on mean-zero fields and is H-equivariant and idempotent. Since rank of the symbol is2 at ALL modes, tr K_F(d)=2*1[d=0], so every offsite kernel trace is ZERO. Nevertheless (T037.4) forces every nonzero axis layer to have operator norm1/N. This shows exactly why ROT036's rank-trace test is insufficient in the r0=2 case, without falsely asserting full individual-shift support.

## Source and independent exact executions

A) Entirely standalone SymPy RATIONAL, NO original helper and NO NumPy. Builds the 6x6 congruence action C_x and computes P_x exactly, verifies the (-1) eigensector rank2, remaining sectors 2+2; 24 cubic rotations; generators O_x,O_y generate group of order24; [P_x,C_y] !=0. Independent centralizer of 24 six-dimensional matrices: **864 rational commutator equations, rank33, dim3**. 1+2+3 central idempotents and all 8 sums checked. Exact discrete group-ring Fourier coefficient identities for N3,5,9,15,31,35,41. FIRST exploratory symbolic attempt used unsimplified exp-of-root-of-unity sums and FAILED an assertion; repaired by exact RATIONAL group-ring coefficient arithmetic. This failure is retained as negative knowledge, not reported as an accepted theorem falsifier.

B) Different standalone NumPy/FFT implementation. **24 axis-symbol tests**: N3,5,9,15,31,41 times zero-mode seed E0=0, P_diag(rank2), tracefree(rank5), identity(rank6). In EVERY case ifft along axial frequencies agrees with (T037.2), all nonzero layer operator norms =1/N. For N3,5,9 additionally constructed full 3D 6x6-valued inverse FFT kernels with synthetic E0=P_diag and all nonzero source P_raw(k), then checked EVERY offsite coefficient's trace=0, EVERY axis layer nonzero, and 24 group actions × four frequencies =96 checks per N, 288 PASS. These are synthetic pure-source TT operators, not original masked K_A.

C) Literal unchanged retained source-helper apply_P_TT after SHA-check N5,9,15, axial j1,2, four true tensor polarizations: yy−zz and yz retained exactly, xx and xy rejected exactly, **24 real cosine source cases PASS** (unrounded component error <2e−12). Historic source helper NOT REDISTRIBUTED or imported for exact audit.

D) Fully reproduced Moderator-local 8-member ZIP:
  iw_int8_rot037_symmetry_protected_mean_zero_tt_radius_bundle.zip
  ZIP SHA256 **0f3bf2d7dbbaa29b122ec064eadf2ce96df405b05ba8ee49937084310570059e**.
Archive includes complete longer Polish report, TWO distinct executable programs, independently produced exact JSON and numerical/source JSON, README, log, SHA256SUMS. ZIP CRC PASS; SHA256 **7/7**. TWO clean isolated extraction executions with OPENBLAS_NUM_THREADS=1:
- retained-helper PRESENT byte-SHA verified, BOTH JSON files BYTE-IDENTICAL to archived;
- helper ABSENT: exact JSON byte-identical, numerical mathematical result equal, source explicitly SOURCE_SKIPPED_NO_HELPER (not false SOURCE PASS).

## Strict STOP / status
Only finite ODD raw-signed-k user-helper source, FULL real symmetric tensor carrier but approximation MEAN-ZERO L2, spatially translation-invariant idempotents with cubic stabilizer seed symmetry. Correctly transported metric-indexed families remain possible but nonlocal at the required radius. No claim about entire individual-shift support for meanzero, arbitrary NONtranslation-invariant operators, even rawcast, exact masked historical K_A, arbitrary curved York, physical diffeomorphism/gauge, J3/K, Noether, gravitational-wave energy, mathematical novelty or new NASH physics. BW ING, independent referee, source owner adoption and Moderator EXEC ALL PENDING. NO NEW TASK CASCADE.
