---
artifact_id: IW_INT8_ROT035_MEAN_ZERO_ANGULAR_TT_LOCALITY_GAP_001_20261026
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_SOURCE_TYPED_RAW_TT_PROJECTOR_LOCALITY_AND_METRIC_ORBIT_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_SHARP_ASYMPTOTIC_MEAN_ZERO_LOCALITY_GAPS / SOURCE_TYPED / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT035 — mean-zero angular TT nonlocality: sharp asymptotic gap 1 for projections versus 1/2 for linear filters

## Source and previous owners; mature host

Current Slack #iw-dispatch read 2026-10-26. MT13 FIRST owns metric-transported affine E_g and first raw-target-k TT alias fault. INT8 ROT023–028 previously own the angular alias singular spectrum and repairs. INT8 ROT029–032 own the strong FIXED metric-independent full SL3 tensor commutant; ROT033 owns natural metric-indexed P_g on a flat integer orbit. INT8 ROT034 ALREADY PROVED exact ALL N^3 shift support for <1-accurate translation-invariant idempotent projectors when the original FULL SOURCE has rank P(0)=5, rank P(k)=2 at all k!=0; and linear sublinear-stencil full-L2 asymptotic 1/2. Geeky-S11 owns RAW-vs-matched and EVEN real-cast differences. M14 owns historical masked puretrace h=fI K_A; XH curved York; PRF12 different Lie/TT. NO OWNER reattribution.

THIS ROT035 removes k=0 ENTIRELY from the admissible input norm. Therefore ROT034's source trace jump and all-offset kernel support proof CANNOT be reused. Narrow independent lineage result: nevertheless there is a sharp ASYMPTOTIC locality dichotomy, driven by direction-dependent TT rather than zero-mode rank. External mature host: Fourier interpolation; rank of nearby idempotents; classical Bernstein trigonometric derivative estimate (V. Totik, Bernstein-type inequalities, J Approx Theory 164 (2012), DOI 10.1016/j.jat.2012.03.002); real traceless symmetric eigenvalues; odd determinant. NO mathematical priority/novelty or physical claim.

## Exact carrier, NO hidden zero-mode norm

N=2m+1 odd tending to infinity, G_N=(Z/NZ)^3. Hilbert mean-zero real symmetric covariant tensor fields H^0_N={H:G_N→Sym2(R³):sum_x H(x)=0}. Full tensor Frobenius L2 restricted ONLY to k!=0, no polarization restriction. Source P_N at every k!=0 is the ORIGINAL retained helper RAW signed-wavevector rank2 Frobenius-orthogonal TT:
 Pi_k(H)=Q_k H Q_k -(tr(Q_k H)/2)Q_k,
 Q_k=I−kk^T/|k|².
No assumption, constraint or claim about source P_N(0) is used for the error.

F_N is any REAL translation-invariant full-symmetric-tensor map with convolution kernel K(d) supported in the signed coordinate cube [-R_N,R_N]^3, 0<=R_N<m. It can be otherwise arbitrary 6x6 matrix-valued and not shear-equivariant. Its complex Fourier symbol is a 3D trigonometric matrix polynomial f_N(theta)=sum_d K(d) exp(i d·theta), coordinate degrees <=R_N. Approximation error is
 epsilon_N(F)= max over k!=0 ||f_N(2pi k/N)−Pi_k||op,
equal to the norm of the real mean-zero field operator. Distinguish (P) F_N²=F_N on the full grid, including nonorthogonal idempotents; (L) ANY linear F_N without idempotence. No source E_alpha filtering or Hs weighted norms are imposed.

## EXACT THEOREM T035.P — even after deleting k0, local idempotents have sharp limiting error 1

For EVERY odd sequence N→infinity and EVERY radius sequence R_N=o(N):
 lim_N inf_{F_N²=F_N, radius<=R_N} epsilon_N(F_N)=1.   (T035.P)
Upper exact 1: F=0.

SELF-CONTAINED PROOF:

A. For sufficiently large N, 4R_N<N. If F²=F at the N³ discrete Fourier points, f(theta)^2−f(theta) has trigonometric degree<=2R_N in each coordinate and vanishes at every frequency-grid point. By uniqueness of the discrete Fourier coefficients because 4R_N<N, it vanishes IDENTICALLY for all continuous theta. Thus f(theta) is a continuous matrix-idempotent on the connected 3-torus, with CONSTANT rank.

B. If epsilon_N<1, idempotents f(k) and source Pi_k have the same rank 2 at EVERY k!=0. Hence f(0) is a REAL 6x6 idempotent of rank 2 too. This f(0) is the CANDIDATE'S polynomial value; NOT the source raw TT zero-mode projector, which is not tested.

C. For ANY REAL rank2 idempotent E on Sym2(R³), ker(E) dimension4 meets the real traceless 5D tensor subspace in dimension>=3. On the 2-sphere of any 3D linear subspace of this intersection, cubic determinant det(T) is continuous and odd. Hence exists normalized T!=0 with E T=0, trace(T)=0 and det(T)=0. Its eigenvalues are (lambda,−lambda,0), lambda!=0. For unit null eigenvector n, source directional Pi_n(T)=T. Consequently ||(Pi_n−E)T||=1. No orthogonality of E, topology, physics or assumptions about k0.

D. Round Kn to integer q for K>=4: q_i=nearest integer K n_i, ||q−Kn||2<=sqrt3/2. Its direction satisfies ||Pi_q−Pi_n||op<=32/K (conservative bound via Q_n=I−nnT and TT formula). For K+1<=m, q is a genuine nonzero signed source frequency.

E. Bernstein: for matrix-valued trig polynomial f, define M=sup_theta||f(theta)||op; each coordinate derivative is bounded by R M, using scalar unit matrix elements. EVERY theta has some NONZERO grid frequency within l1 distance 5pi/N; when nearest grid is k0 choose an adjacent nonzero one. At observed k!=0, ||f(k)||<=1+epsilon. Thus if 5piR/N<1/2 and epsilon<1,
 M<=(1+epsilon)/(1−5piR/N)<=4.
Then ||f(2pi q/N)−E||<=6pi R(K+1)M/N<=24pi R(K+1)/N.

F. Evaluate error on source T at nonzero k=q:
 epsilon >= ||(Pi_q−f(q))T||
 >= 1−||Pi_q−Pi_n||−||f(q)−E||.
So whenever N>4R, 5piR/N<1/2, K>=4 and K+1<=m,
 epsilon_N >= max(0, 1−32/K−24pi R(K+1)/N).   (C035.P)
If epsilon>=1 this inequality is trivially true. Choose K=floor(sqrt(N/max(R,1))), truncated only if needed by m−1. For R_N=o(N), K→∞, R_N K/N→0. Therefore liminf epsilon>=1. With zero operator upper bound the theorem is sharp. Constants in (C035.P) are conservative NOT optimal.

## EXACT THEOREM T035.L — without projection restriction sharp limit is 1/2

For the SAME odd mean-zero host and R_N=o(N), dropping F²=F:
 lim_N inf_{F_N linear, radius<=R_N} epsilon_N(F_N) = 1/2. (T035.L)

Upper: onsite F=I6/2 gives EXACT epsilon=1/2 at all nonzero wavevectors since Pi_k is orthogonal.

Lower: independent exact six-dimensional projector calculation yields ||Pi_e1−Pi_e2||op=1, with TT principal-angle cosines (1/2,0). Thus
 1<=2epsilon+||f(2pi e1/N)−f(2pi e2/N)||.
The same matrix Bernstein grid-bound (no idempotence needed) gives
 ||f(e1)−f(e2)||<=4pi R M/N,
 M<=(1+epsilon)/(1−5piR/N)<2/(1−5piR/N) if epsilon<1.
Therefore
 epsilon_N >= max(0, [1−8pi R/(N(1−5pi R/N))]/2).  (C035.L)
For R_N=o(N) this tends to 1/2. If epsilon>=1 the inequality is automatic. Upper/lower coincide. No finite-N exact minimum claimed at every positive R.

## Executed independent controls and exact source contract

NUMPY main: full six-dimensional symmetric Frobenius projectors, two coordinate directions (norm difference 1; principal cos .5/0). FOUR independently generated real rank2 idempotents E (2 orthogonal, 2 oblique): their real ker(E)∩traceless >=3 computed by SVD; a continuous determinant sign-change finds singular traceless normalized T, eigenvector n, verifies ET≈0 and Pi_n T≈T to residual ~1e-16. Integer-rounded q witnesses for K5/9/17/33 checked against directional bounds. No physical fields in these algebraic witnesses.

EXACT independent SYMPY, no NumPy/no original source: rational Frobenius matrices Pi_e1,Pi_e2, rank2/idempotency, (Pi_e1−Pi_e2)^2 eigenvalues among {0,3/4,1}, ||Pi_e1−Pi_e2||=1; 3 exact real tracefree det0 tensors and appropriate direction normals, plus 4(P−I/2)^2=I on 3 nonzero carrier modes.

SOURCE MATCH: UNMODIFIED user-retained deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Original source functions apply_P_TT and apply_E directly invoked on REAL mean-zero cosine fields at k=e1,e2,e1+e2, N5/9/15: 9 checks against separate TT matrix formula, component discrepancy <2e−13; direct TT preservation plus E_lin(alpha=.05) scalar factor PASS. HISTORICAL production dtc0a_runtime_v0_3_1.py byte unavailable; no masked KA re-run. Clean helper-absent run explicitly says SOURCE SKIPPED.

EVALUATED FORMULA ONLY: e.g. N1000001 R1 gives certified projector error lower 0.892526453564 and general linear lower 0.499987433445, with upper 1 and 0.5; N100001 R1 gives 0.659724198230 and 0.499874317809. These N are scalar arithmetic TESTS OF THE BOUND, NOT actual N^3 numerical lattice executions or measured physical error.

NEGATIVE KNOWLEDGE: preliminary main determinant bisection mistakenly reused its initial direction vector as both independent directions, FAILED its assertion and was corrected to an independent random b, followed by COMPLETE rerun. No false initial PASS. Scoped distinction from ROT034: source zero-mode removal INVALIDATES previous full-support trace argument; new theorem provides ASYMPTOTIC, not every finite-N, locality no-go from angular TT geometry.

## Reproducibility custody

Complete Moderator-local ZIP iw_int8_rot035_mean_zero_directional_locality_repro_bundle.zip SHA256 **5a4de9c0adf77cc6a215a17a482dee876cdc3a54eb3a524a4060fe3fe6d714ea**, 8 entries (complete longer Polish proof, independent NumPy and SymPy scripts, TWO detailed frozen JSONs, run log, README, SHA256SUMS). ZIP CRC PASS, SHA256 7/7 PASS. TWO independently CLEAN extracted replays: SHA-checked literal source-present BOTH JSON byte-identical, source-absent independent SymPy byte-identical and mathematical main output equal with source correctly marked SKIPPED. Source original helper NOT redistributed; GitHub report only, code publication not asserted.

## Nonmaps, status

Strict finite ODD signed-RAW-k Fourier DTC0a helper. Full symmetric tensor MEAN-ZERO L2. Does NOT transfer to even raw-cast (Geeky-S11), special source-only TT input spaces, Hs bounds, different zero-mode conventions insofar as mean-zero, arbitrarily curved York, metric changing local stencil without transport, original masked KA, NCDG physical J3/K, Noether, GR gauge, wave energy, other experiments. This is standard Fourier approximation and symmetric-matrix algebra, NOT a new mathematical or physical discovery. BW ING, independent referee, owner acceptance and Moderator EXEC pending; no task cascade.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
