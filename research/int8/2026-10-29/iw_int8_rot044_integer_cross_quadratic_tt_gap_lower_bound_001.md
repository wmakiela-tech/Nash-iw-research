---
artifact_id: IW_INT8_ROT044_INTEGER_CROSS_QUADRATIC_LOWER_TT_GAP_001_20261029
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_FLAT_AFFINE_METRIC_NUMERICAL_COORDINATE_VS_GEOMETRIC_NORM_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_POSITIVE_ARITHMETIC_LOWER_BOUND_WITH_IMPLICIT_CONSTANT / SOURCE_TYPED / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# INT8 ROT044 — quadratic nondegeneracy and integer cross-product lower bound for TT norm gap

**Date:** 2026-10-29. **Scientific scope:** finite ODD grids, auxiliary original DTC0a RAW-k TT, real Sym2(R3) fibers, meanzero fixed-component Frobenius operator norm, constant flat integer metric transports. Historic production masked K_A BYTE UNAVAILABLE and NOT RUN. Independent referee, BW ingestion, owner adoption and Moderator EXEC PENDING.

## First scientific owners and mature mathematical foundations

MT13 first owned source-correct flat affine E_g and naive folded target raw-k TT alias. INT8 ROT033 first owned metric-indexed natural P_g via cubic stabilizer descent; ROT034–039 already own different stencil questions; ROT040–041 first computed constant-mode and whole-operator xy shear norms; ROT042 first gave general A Wielandt bound, rational 2x2 TT norm formula, and equality criterion. ROT043 first proved O_A(N^-2) uniform angular convergence and O_A(N^-3) Dirichlet subsequence. This ROT044 is ONLY a complementary positive lower bound for irrational middle eigendirections. M14 owns historic h=fI masked K_A, Geeky even rawcast, PRF Lie-TT and XH curved York.

Mature references: Lin and Sinnamon (2012), The generalized Wielandt inequality in inner product spaces, Eurasian Mathematical Journal 3(1):72–85, https://www.math.uwo.ca/faculty/sinnamon/pdf/wielandt.pdf ; classical rational root theorem for integer monic polynomials; integer cross products and elementary compactness. No mathematical priority, physics or experimental claim.

## Source contract and constants

Let odd N=2m+1>=3. For integer A in SL3(Z), D=A A^T has eigenvalues a>b>c>0, product abc=1, with orthonormal eigenvectors v_plus, v_mid, v_minus. Define C_A(H)=A^T H A and source-RAW TT_k the orthogonal rank2 real tensor projector at signed nonzero integer Fourier k. Let M_A(k)=||C_A TT_k C_A^-1|| and finite meanzero maximum M_N^0=max_(k in [-m,m]^3, k!=0) M_A(k); W(A)=(a/c+c/a)/2. The exact metric-transported projector P_g with g=A^T A is geometrically orthogonal, norm1 in metric L2(g); all gaps below use ordinary fixed-coordinate Frobenius L2 on meanzero fields. Properly SOURCE transported, NOT naively recomputed target RAW-k.

## Theorem T044.1 — strictly positive directional Hessian

Use local normal coordinates (x,z) near the middle eigendirection v_mid, in the tangent directions v_plus and v_minus. Then:
  W(A)-M_A(n)=alpha_plus*x^2+alpha_minus*z^2+o(x^2+z^2),
  alpha_plus=(a-b)*(a*b-c*c)/(2*a*b*c)>0,
  alpha_minus=(a*a-b*c)*(b-c)/(2*a*b*c)>0.

**Exact proof:** diagonalize D in its orthonormal eigenbasis. Tilt wavevector n toward v_plus through angle theta; choose TT basis H_d=(uu^T-vv^T)/sqrt(2), H_o=(uv^T+vu^T)/sqrt(2), u=(cos(theta),-sin(theta),0), v=e_minus. The maximal squared singular branch near theta0 is
  1/4*[(a cos^2 theta+b sin^2 theta)^2+c^2]*[(a^-1 cos^2 theta+b^-1 sin^2 theta)^2+c^-2].
The corresponding tilt toward v_minus has branch
  1/4*[a^2+(c cos^2 theta+b sin^2 theta)^2]*[a^-2+(c^-1 cos^2 theta+b^-1 sin^2 theta)^2].
Differentiate with respect to sin^2(theta) at theta0 and divide by 2W. Mixed xz Hessian vanishes by orthogonal coordinate reflections commuting with diagonal D. Both displayed curvature coefficients are strictly positive for a>b>c>0. Independently proved symbolically using exact SymPy.

## Theorem T044.2 — positive global angular constant

By the equality condition already established in ROT042, the only continuous wave directions giving M_A(n)=W are +/-v_mid. Define
  c_A=inf_(||n||=1, n!=+/-v_mid) (W-M_A(n))/(1-(n.v_mid)^2).
Then **c_A>0**: near either maximizing direction, T044.1 gives strictly positive liminf at least min(alpha_plus,alpha_minus); on the compact complement the ratio is continuous and strictly positive. Consequently for ALL nonzero n:
  W(A)-M_A(n) >= c_A*sin^2(angle(n,v_mid)).
IMPORTANT: c_A is an implicit strictly positive fixed-A constant from a 2D compact optimization. NO specific certified numerical c_A value is claimed.

## Theorem T044.3 — arithmetically forced positive finite-grid norm gap

Assume det(D-I)!=0. For any nonzero integer wavevector k, k cross Dk cannot vanish: an integral eigenvector of integer D would yield a rational eigenvalue, hence by the monic degree3 rational root theorem and det D=1, the positive eigenvalue must equal1, which is excluded. Therefore k cross Dk is NONZERO INTEGER vector and
  ||k cross Dk|| >= 1.
Write k=beta*v_mid+w, w perpendicular v_mid, ||w||=||k|| sin theta. Then
  ||k cross Dk||=||k cross (D-bI)w||
     <= (a-c)*||k||^2*sin theta.
Since signed k on odd grid has ||k||^2<=3m^2,
  sin theta >= 1/[3(a-c)m^2].
Together with T044.2 this yields for EVERY odd N:
  **c_A/[9(a-c)^2*m^4] <= W(A)-M_N^0(A) <= 8(a/c)/m^2.**
The UPPER belongs to ROT043. Further along an infinite subsequence ROT043 gives O_A(N^-3) upper. No optimality of exponent 4 or global O(N^-3) asserted. When det(D-I)=0, a rational middle eigendirection eventually fits the grid and gap becomes exactly zero (ROT042); T044.3 must NOT be used then.

## Executed independent controls; negative knowledge

NumPy standalone: 4 integral A (3 irrational and 1 rational control), 32 nonzero-angle local curvature checks, 35,688 explicit integer wavevector tests of cross product nonzero and angle lower bound on bounded finite cubes, plus three ORIGINAL byte-SHA-checked helper apply_P_TT real cosine fields at N=3,5,7. All PASS. Auxiliary helper SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. Source helper NOT redistributed; historic original production runtime NOT run.

Independent SymPy/stdlib script (NO NumPy, NO source code import): symbolic alpha_plus and alpha_minus coefficient identities, 9188 exact integer cross-product checks across 20 matrix/grid cases, rational k TT projector idempotence on two independent inputs. ALL PASS. For A_mix=[[1,1,0],[0,1,1],[0,0,1]]: det(D-I)=-1; a,b,c approximately 3.24698,1.55496,0.19806; W=8.227365273468; alpha_plus=4.238250405546, alpha_minus=6.943845414860. The m=15 rounded witness q=(15,-7,-12) has sin theta=0.015319829876 and integer-cross lower angle certificate 0.000485904115, not a full optimal mode claim.

Negative control: first finite-angle numerical curvature test at theta=.1 rejected valid theta^2 coefficient due to neglected finite theta^4 term. Tolerance changed ONLY for finite-angle asymptotic approximation, then entire main script reexecuted PASS. Exact SymPy tests and unrounded source assertions NOT weakened.

## Reproduction and epistemic STOP

Complete Moderator-local 7-member ZIP iw_int8_rot044_arithmetic_lower_tt_gap_bundle.zip, SHA256 9d4fa5ac14892e4aa4129d63a5081a97fd175a9769941776fc1aa54b763291d3; full Polish report + two independent executable Python scripts + two JSON + README + SHA256SUMS. ZIP CRC PASS, manifest SHA256 6/6 PASS. CLEAN A and CLEAN B extraction with original helper BOTH JSON BYTE_IDENTICAL to originals. CLEAN C without helper: exact SymPy JSON BYTE_IDENTICAL, all mathematical main fields equal, source correctly SOURCE_SKIPPED_NO_HELPER.

ONLY odd finite signed auxiliary TT, meanzero full 6D tensor carrier, correctly transported flat integer metrics. No even source realcast, historic masked h=fI K_A, curved York, GR gauge, J3/K, Noether, gravitational wave physical observables, experiments, new mathematical theorem priority, CANON or EXEC. BW ING and independent referee UNVERIFIED. NO_NEW_TASK_CASCADE.
