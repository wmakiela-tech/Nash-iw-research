---
artifact_id: IW_INT8_ROT042_GENERAL_INTEGER_METRIC_TT_NORM_AND_ATTAINMENT_001_20261029
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_FLAT_AFFINE_METRIC_NUMERICAL_COORDINATE_VS_GEOMETRIC_NORM_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_SOURCE_TYPED_GENERAL_A_TT_NORM_AND_RATIONAL_FOURIER_CERTIFICATE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# INT8 ROT042 — general unimodular integer metric: exact TT norm, finite-grid equality gate and rational Fourier certificates

Date 2026-10-29. Mathematical SOURCE-TYPED finite-flat result; independent referee, BW ingestion, owner adoption, Moderator EXEC not confirmed.

## Scientific precedence; external mathematical host
MT13 FIRST owns exactly transported flat affine E_g and the naive raw TARGET-k TT alias. INT8 ROT033 FIRST in this lineage owns cubic stabilizer descent of metric-indexed P_g=U_A P_I U_A^-1. ROT034–039 FIRST own distinct source TT stencil locality and integral support. INT8 ROT040 FIRST proved (t^4+4t²+3)/3 for constant-tensor metric-tracefree Q_g for xy shear; INT8 ROT041 FIRST proved exact WHOLE TT norm (t^4+4t²+2)/2 for that SPECIAL shear. ROT042 extends to arbitrary A∈SL3(Z) and distinguishes a general BOUND from ACTUAL FINITE-N attainment. M14 historic masked h=fI/K_A, Geeky even-grid source RAW realcast, XH curved York, PRF other Lie/TT stay distinct.

Classical PRIOR ART: M. Lin and G. Sinnamon, The generalized Wielandt inequality in inner product spaces, 2012, https://www.math.uwo.ca/faculty/sinnamon/pdf/wielandt.pdf ; K. Gustafson, The geometrical meaning of the Kantorovich-Wielandt inequalities, LAA 296 (1999), 143–151. This is NOT a novelty or physics claim.

## Precise original source contract
ODD N>=3 and m=(N−1)/2. REAL symmetric rank2 tensor fields over (Z/N)^3; full input L² and mean-zero L² removing ONLY k=0. Unmodified user auxiliary DTC0a apply_P_TT from deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801. On each source signed RAW k≠0, P_kH=Q_k H Q_k−tr(Q_kH)Q_k/2, Q_k=I−kkᵀ/|k|², orthogonal rank2; at k0 ORIGINAL rank5 tracefree, not zero. Original historical full production dtc0a_runtime_v0_3_1.py BYTE-UNAVAILABLE; masked historic K_A NOT RUN.

For A∈SL3(Z), U_A H(x)=Aᵀ H(Ax mod N)A, g=AᵀA, P_g=U_A P_I U_A^-1. Anti-representation U_A U_B=U_(BA). This is correctly SOURCE TRANSPORTED TT, NOT naive recomputation with folded target raw k. U_A is an isometry in geometric tensor L²(g), so ||P_g||_g=1. All other norms here use fixed-coordinate Frobenius L².

## T042.1 exact general bound and finite 2x2 rational formula
Let D=AAᵀ, ordered positive eigenvalues λ+>=λ0>=λ−, product1. Define W(A)=(λ+/λ−+λ−/λ+)/2. Tensor congruence C_A(H)=Aᵀ H A has κ(C_A)=λ+/λ−. Classical Wielandt projection similarity bound yields
  ||C_A P_k C_A^-1|| <= W(A)
for EVERY source Fourier k, independent of N. A permutation of lattice nodes is an L² isometry, so the same global bound applies to P_g.

MEANZERO EXACT norm:
  M_N^0(A)=max_{k in signed cube [-m,m]^3, k!=0} M_A(k)
  M_A(k)=||C_A P_k C_A^-1||_F.
FULL EXACT norm:
  M_N(A)=max(M_N^0(A),sqrt(tr(D²)tr(D^-2))/3).
DO NOT replace either finite max automatically by W(A).

Computable RATIONAL 2x2 CERTIFICATE: Choose two rational linearly independent Frobenius TT polarizations H1,H2 for any nonzero integer k. Form
 G_ij=tr(H_i H_j), S_ij=tr(H_i D H_j D), T_ij=tr(H_i D^-1 H_j D^-1).
Then M_A(k)^2 is the largest eigenvalue of Z=G^-1 S G^-1 T, explicitly
  (tr Z+sqrt((tr Z)^2−4det Z))/2.
All G,S,T entries rational. This follows by factoring the rank2 source orthogonal projector B G^-1 B* and evaluating its two nonzero singular values after tensor congruence. It is independent of any 6N³ dense matrix.

## T042.2 exact equality gate
For NONORTHOGONAL INTEGER A∈SL3(Z), D=AAᵀ has three DISTINCT positive eigenvalues. Any repeated root of its integer cubic characteristic polynomial must be rational/integer; with det1 and positivity it would force D=I, contrary to hypothesis. Let v+,v0,v− denote orthonormal ordered eigenvectors.

Wielandt equality for the TT block occurs iff its source rank2 range contains the extremal tracefree bisector and its kernel contains the sum bisector of extremal rank1 singular tensors. For TT this is equivalent to the wavevector being perpendicular to BOTH v+ and v−, hence
  M_A(k)=W(A) IFF k is parallel to v0.

For integer nonzero k, this implies rational eigenvalue of integer D. By rational-root theorem and constant term−1 it must be 1. Conversely det(D−I)=0 yields primitive integral generator v of the 1D kernel; eigenvalue1 is the middle one because the other two are reciprocal positive values straddling1. Thus for nonorthogonal A and odd N=2m+1:
  M_N^0(A)=W(A) IFF det(AAᵀ−I)=0 AND m>=||v||infinity.
The original FULL source zero-mode rank5 cannot itself attain W for nonorthogonal A (its kernel is span I and incompatible with Wielandt extremal bisector), so the same criterion governs full-carrier equality. Orthogonal A gives W=1 trivially.

When det(D−I)!=0 all finite N have STRICT inequality but for fixed A the finite maxima approach W(A) as odd N→infinity by integer direction approximation to v0. No sampled finite grid establishes all-N equality.

## Three exact example families
A_xy=[[1,1,0],[0,1,0],[0,0,1]], middle primitive v=(0,0,1), W=7/2. Exact equality already N=3 and every larger odd grid (ROT041).

A_long=[[1,0,-1],[0,1,2],[0,0,1]], v=(2,1,0), W=47/2=23.5. N3 signed frequency cube cannot contain v: exact computed maximum ~21.4882836328355 at (1,1,0). From N5 the primitive vector is available and W attained EXACTLY. Hence det(D−I)=0 alone is insufficient without grid-size condition.

A_mix=[[1,1,0],[0,1,1],[0,0,1]], D=[[2,1,0],[1,2,1],[0,1,1]], char_D(z)=z³−5z²+6z−1 has neither ±1 as root; det(D−I)!=0. Hence strict gap at ALL finite N; W≈8.227365273468. Computed finite maxima N3 7.832304629194; N5 8.166644344073; N7 8.178561538499; N9 8.206899485230; N15 8.222221971196; N21 8.226027403388; N31 8.226872244484.

## Actually executed independent falsifiers and reproducibility
A) Standalone NumPy per-wavevector TT rational-Gram algorithm: 3 matrices × 7 grids N3/5/7/9/15/21/31 =21 cases, 65,466 half-grid signed wavevector instances, independent 6x6 SVD on maximal modes, zero W violations. SIX real cosine field checks invoking unmodified byte-SHA-verified original apply_P_TT after proper source→target transport, including A not congruent to identity mod N, discrepancy <3e−10 PASS. N31 via compressed 2x2 math, NOT an original full N31 helper run.
B) Independently authored SymPy+stdlib, no NumPy nor source helper: 225 exact rational 2x2 frequency cases at N3/N5, rational square-root interval comparisons of maxima, exact integer characteristic polynomials, primitive eigenvectors; ties accepted ONLY when exact trace and determinant agree. PASS.
Negative knowledge: first main run failed JSON serialization of numpy.bool_; cast to Python bool and rerun. Initial independent audit incorrectly required a unique maximizing wavevector despite equivalent collinear waves; repaired exact tie handling and full rerun. No scientific failing result falsely called PASS.

Complete Moderator-local 8-member ZIP: iw_int8_rot042_general_integer_metric_tt_norm_bundle.zip, SHA256 0fbfefce85760f7ee93f940af4419cadd0bd5ede594ff72857315dc7d85a2c2c; FULL Polish original report SHA256 2cf99bdfc31cfaec1b049c5a75961f054f1c64588575210bbfdc7a4e69a18380, two standalone runnable Python, two JSON outputs, README, RUNLOG, SHA256SUMS. ZIP CRC PASS, 7/7 member SHA256 PASS. Two fresh clean extractions with original helper: BOTH JSON byte-identical; third helper-absent independent exact JSON byte-identical and main math same, source status SOURCE_SKIPPED_NO_HELPER. Code/local ZIP retained for Moderator, original helper NOT redistributed.

## STOP and prior blocked-write provenance
ONLY odd finite source RAW TT, flat integer g=AᵀA, full and meanzero symmetric tensor carriers. No even-N Nyquist real-cast, original masked h=fI K_A, historical runtime, general curved York, physical J3/K/GR gauge/Noether/GW, experiment, scientific novelty, BW ING, referee or EXEC. NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK_CASCADE.

Historical GitHub write for ROT042 was blocked by tool safeguards earlier 2026-10-29; this re-submission is explicitly requested by the Moderator and requires a successful create/readback before any publication PASS claim.
