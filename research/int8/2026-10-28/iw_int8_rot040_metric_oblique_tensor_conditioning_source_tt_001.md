---
artifact_id: IW_INT8_ROT040_METRIC_OBLIQUE_TT_COORDINATE_CONDITIONING_001_20261028
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_FLAT_AFFINE_METRIC_NUMERICAL_COORDINATE_VS_GEOMETRIC_NORM_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_FINITE_FLAT_METRIC_COORDINATE_CONDITIONING_DIAGNOSTIC / SOURCE_TYPED / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT040 — exact quartic fixed-coordinate conditioning of a geometrically orthogonal tensor projector

## Scientific lineage; external mature theorem
MT13 FIRST owns exact source-matched affine metric filter transport E_g and the naive target RAW-k TT alias defect. INT8 ROT033 ALREADY owns exact source-metric flat integer-orbit family P_g=U_A P_I U_A^-1 and its stabilizer criterion; ROT034–038 FIRST own separate full/mean-zero locality, projections and approximate idempotence; ROT039 FIRST distinguishes uniform FIXED COORDINATE stencil growth from invariant INTRINSIC metric shift distance. M14/M13 historic source h=fI, masks and K_A, Geeky even-grid RAW/cast defect, XH curved York, PRF different Lie/projection work are separate. Latest #iw-dispatch reviewed 2026-10-28 before this rotation.

MATURE MATH HOST, NO novelty: for complementary nontrivial oblique Hilbert-space idempotents T and I−T, their operator norms are equal. Daniel B. Szyld, The many proofs of an identity on the norm of oblique projections, Numerical Algorithms 42 (2006) 309–323, DOI 10.1007/s11075-006-9046-2. Valeria Simoncini and Daniel B. Szyld, On the field of values of oblique projections, Linear Algebra and Its Applications 433 (2010) 810–818, DOI 10.1016/j.laa.2010.04.004. The tensor-metric computation below is an explicit specialized application, NOT a new mathematical/physical discovery.

## Carrier, original code identity and the TWO essential norms
N odd, G_N=(Z/NZ)^3, V_N=real symmetric covariant 3x3 tensor fields. A∈SL3(Z) acts
  (U_A H)(x)=Aᵀ H(Ax mod N) A,
  g_A=Aᵀ A,
  P_g=U_A P_I U_A^-1.
U_A U_B=U_(BA), so the action is an anti-representation. The source P_I is the retained literal original helper apply_P_TT, with RAW signed k rank2 TT projection at k!=0, but SOURCE rank5 tracefree projection at k=0; historic full production dtc0a_runtime_v0_3_1.py remains byte-unavailable. ROT033 already proved metric-orbit representative independence, no new proof claimed here.

For tensors H=Hᵀ use ordinary fixed-coordinate ||H||_F²=tr(HᵀH), V_N spatial flat L2 built from this, and separately intrinsic metric ||H||_g²=tr(g^-1 H g^-1 H). U_A is an isometry (L2,I)→(L2,g_A); it generally is NOT an isometry if both frames are evaluated with the same fixed-component Frobenius norm.

## T040.1 exact pointwise norm formula, and no geometric defect
Integer shear A_t=I+t E12 has
  g_t=[[1,t,0],[t,1+t²,0],[0,0,1]],
  g_t^-1=[[1+t²,-t,0],[-t,1,0],[0,0,1]].
Define metric trace rank1 idempotent
  T_g H=g tr(g^-1 H)/3,
and metric tracefree rank5 idempotent
  Q_g H=H−T_g H.
Then exact identities for EVERY integer t:
  Q_g²=Q_g,
  tr(g^-1 Q_gH)=0,
  ||Q_(g_t)||_(g_t→g_t)=1,
  ||Q_(g_t)||_(F→F)=||T_(g_t)||_(F→F)=(t⁴+4t²+3)/3.    (T040.1)

PROOF: In the Hilbert–Schmidt/Frobenius tensor space T_g is the rank-one oblique projector H↦(g/3)<g^-1,H>_F. Therefore its operator norm equals ||g||_F||g^-1||_F/3. Direct exact computation yields
 tr(g_t²)=tr((g_t^-1)²)=t⁴+4t²+3, tr(g_t^-1 g_t)=3.
Classical equal complementary-idempotent norm gives ||Q_g||=||T_g||. Direct alternate 6D decomposition has Q_g singular values: (t⁴+4t²+3)/3 once, 1 four times and 0 once. In weighted metric tensor Hilbert space Q_g is an ORTHOGONAL projector and hence has exactly norm1. No contradiction: a geometrically orthogonal projector can be extremely oblique in fixed components. Growth ~t⁴/3 is exact.

| t | exact fixed Frobenius norm | true metric norm |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 8/3 | 1 |
| 3 | 40 | 1 |
| 5 | 728/3 | 1 |
| 10 | 10403/3 | 1 |
| 20 | 161603/3 | 1 |
| 31 | 927368/3 | 1 |
| 62 | 14791715/3 | 1 |

## T040.2 original source P_TT inherits a LOWER bound on the FULL carrier
On any ODD source N, the original literal apply_P_TT on a CONSTANT tensor field is its rank5 k=0 tracefree P_I(0)=Q_I. Conjugation to g=AᵀA gives
   P_g|_(constant spatial fields) = Q_g.
Therefore the full source P_g obeys
   ||P_(g_t)||_(full L2,F→L2,F) >= (t⁴+4t²+3)/3,    (T040.2)
   ||P_(g_t)||_(full L2,g_t→L2,g_t) = 1.             (T040.3)
CRITICAL: the first is ONLY a LOWER BOUND, not the exact global Euclidean norm. Other Fourier sectors could enlarge it. This specific k0 argument DOES NOT establish the same lower bound on a MEAN-ZERO-only carrier. No historical masked K_A claims are made.

## T040.3 congruence-kernel shear: SAME N³ NODES, growing tensor conditioning
For fixed N choose t=kN. A_t≡I mod N: spatial permutation is exactly the identity. Yet tensor congruence changes metric g_t and ||Q_g||_F~(kN)^4/3 without adding any spatial stencil offset. Thus large fixed-coordinate operator norm can coexist with a POINTWISE exact metric projection.

Original source E_lin is a componentwise SCALAR spatial convolution, hence when t multiple N and the node map is identity it commutes with the uniform tensor congruence:
  U_(A_t) E_lin U_(A_t)^-1 = E_lin.            (T040.4)
For original alpha=.05, its Fourier multiplier e(k)=1−4alpha ∑_j sin²(pi k_j/N) belongs to [0.4,1]; therefore in the fixed-coordinate Frobenius spatial L2, ||E_lin||=1 (attained at k0). This is a sharp distinction between two source-typed operators under EXACTLY the same shear, not proof of production numerical stability.

## Executed controls and falsification discipline
ROUTE A, standalone NumPy on the 6D ORTHONORMAL basis of real symmetric tensors: 10 exact-vs-SVD norm checks at t=0,1,2,3,5,7,10,20,31,62, each <3e-10 relative ERROR on UNROUNDED arrays. Literal unmodified original helper deepseek_python_20260627_a87249.py SHA256
 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801
was imported only after SHA check. Six TRUE original helper constant-field P_g tests: N3 with t0,3,6, and N5 with t0,5,10. Six direct source singular-maximizing constant test modes match the 6D lower bound. Six original E_lin random nonconstant full-field tests verify T040.4. Geometric contraction verified for six cases. Full native original helper for N31 or t62 was NOT run: those are exact formula and tiny 6D SVD checks, NOT claimed giant N³ native source simulations.

ROUTE B, wholly independent SymPy SOURCE-FREE (no NumPy, no Route A import) over symbolic integer t: exact g and inverse and determinant, rank1 projector P, Q idempotence, tr(g²), tr(g^-2), Frobenius norm product, metric weighted adjointness QᵀW=WQ, weighted idempotence QᵀWQ=WQ, exact tracefree tensor on a generic rational offdiagonal symmetric H, exact transport from source tracefree Q_I. Nine exact algebraic identity families PASS. Geometric Hilbert norm exact, not read off numerical roundoff.

NEGATIVE NUMERIC KNOWLEDGE: direct double precision multiplication Q@Q−Q has apparent absolute residual around 1e−8 at t20 and 1e−6 at t62 (platform-dependent); but independent exact rational SymPy proves Q²−Q=0. This demonstrates numerical representation sensitivity, not failure of a production algorithm. All assertions in Route A were performed BEFORE JSON rounding.

REPRO CUSTODY: complete Moderator-local ZIP iw_int8_rot040_metric_oblique_conditioning_repro_bundle.zip SHA256
 109756c0f2e01930e9547f45707cbc77c7ed46ca47860125383a0ba964a0b54d.
Eight entries: longer FULL Polish mathematical report, two independently runnable complete Python scripts, two JSON, README, RUNLOG, SHA256SUMS. ZIP CRC PASS, all 7/7 member SHA256 PASS. THREE isolated clean extractions: two WITH SHA-verified source helper produced two JSON outputs each BYTE IDENTICAL to archived; one WITHOUT source produced exact audit byte-identical and the same numerical math, correctly marked SOURCE_SKIPPED_NO_HELPER. Original helper not redistributed; code and JSON are in local Moderator package, not falsely claimed separately published on GitHub.

## Operational reading / strict stop
Report BOTH the correct metric-adapted L2(g) residual and fixed-coordinate Frobenius residual when diagnosing affine-covariant TT. Log Gram/inverse Gram condition and whether constant mode is present. A large Frobenius coordinate norm is NOT a physical loss of naturality. No general curved metric York, Lorentzian Box, masked historical h=fI K_A, original production runtime, even-N raw casting, J3/K physical invariance, GR gauge or real GW/experimental claim. No mathematical novelty claimed.

BW ingestion, independent referee, owner uptake and Moderator EXEC are unconfirmed and PENDING; no new task cascade.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
