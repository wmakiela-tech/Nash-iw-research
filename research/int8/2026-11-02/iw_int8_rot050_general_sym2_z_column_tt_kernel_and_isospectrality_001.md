---
artifact_id: IW_INT8_ROT050_GENERAL_SYM2_Z_COLUMN_KERNEL_001_20261102
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_SOURCE_OPERATOR_COMPATIBILITY_AND_GAUGE_TYPE_GATE_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_SOURCE_AUXILIARY_GENERAL_HZ_ISOSPECTRAL_CANCELLATION_AND_CONSTANT_SYM2_THREE_COLUMN_KERNEL / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# INT8 ROT050 — all Sym² H(z) zero nonprojected commutator, full constant tensor K_A kernel and three singular values

Date 2026-11-02. Science-first direct test of original auxiliary user DTC0a; complete frozen reproducible ZIP in Moderator conversation. NOT historic production masked K_A.

## Prior owners FIRST and mature host

MT13 FIRST correct E_g/source RAW target-k alias; INT8 ROT016 FIRST Q Lie E P TT-input leakage; ROT046 FIRST single P_raw Lie_C I incompatible centered-derivative symbol; ROT047 FIRST commuting z shears and unmasked K_A nonclosure at Identity; ROT048 FIRST exactly equal E_lin eigenshell shear pair at constant H=I; ROT049 FIRST f(z)I robustness and planar f(x) negative gate. ROT050 extends NONPROJECTED cancellation from f(z)I to EVERY real symmetric tensor H(z), and calculates the COMPLETE source auxiliary inserted TT K_A_out operator restricted to constant real Sym²(R³): rank, kernel, singular values and exact all-node output for each constant S. M13/M14 historic masked h=fI K_A, Geeky even-RAW, PRF Lie and XH curved York remain separate owners. NO general mathematical novelty or physics priority.

Mature external geometry: James M Hyman and Mikhail Shashkov, The Orthogonal Decomposition Theorems for Mimetic Finite Difference Methods, SIAM J Numer Anal 36(3) (1999), 788-818, DOI 10.1137/S0036142996314044, https://epubs.siam.org/doi/10.1137/S0036142996314044 . This paper is general compatible discretization host, NOT the original source of these DTC0a formulas.

## Exact source and scope

The literal user-retained original auxiliary source deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801 was imported and executed byte-unchanged after SHA checking. Operators: original centered stencil derivative, original componentwise E_lin, original RAW-signed-FFT-k TT projector, literal compute_K_C, compute_K_B, compute_K_A_out. Historic complete dtc0a_runtime_v0_3_1.py BYTE UNAVAILABLE; historic masks and production h=fI K_A not run.

Odd N>=7, h=2pi/N, 3-torus. Shears C_a=e_z sin(x+2y), C_b=e_z sin(2x-y), independent of z, bracket zero. Original source E_mode Identity or E_lin with alpha=.05 in tests, theorem for 0<=alpha<=1/6. Set
  s1=sin(h)/h, s2=sin(2h)/h,
  d=2s1-s2, t=(s1+2s2)/5,
  e=1-4alpha*(sin(h/2)^2+sin(h)^2),
with e=1 in Identity. At N>=7 and stable alpha, d,t,e all strictly positive.

All norms: full-grid FULL 9-component tensor Frobenius RMS, not historical mask nor 6-component-normalized helper rms_norm.

## T050.1 — general Sym² H(z) nonprojected E_lin cancellation

Let H(z) be ANY real symmetric 3x3 tensor with arbitrary z profile, even anisotropic and indefinite. For z Fourier ell, first E_lin multiplies input by scalar e_(0,ell). Applying source Lie L_a or L_b gives only planar frequencies +/-a or +/-b with SAME ell. Second E_lin acts on their outputs by the same factor e_(a,ell)=e_(b,ell), because a=(1,2,0), b=(2,-1,0) have identical componentwise sum of sin²(h k_j/2). Both fields are z-shears with z-independent coefficients. Their source discrete Lie actions commute on ALL tensor fields, since L_g H=g D_zH+J_g^T H+H J_g with J_a J_b=J_b J_a=0 and both J commute with D_z; their vector-field bracket is also exactly zero. Thus on EVERY such H(z):
  **compute_K_C=0 and compute_K_B=0**
both at E=Identity and E=E_lin. This DOES NOT extend to arbitrary H(x,y,z); ROT049 has explicit E_lin planar f(x) counterexamples.

## T050.2 — exact entire constant Sym² input and rank3 kernel

Let S be an arbitrary CONSTANT real symmetric 3x3 matrix and set u=S_xz, v=S_yz, w=S_zz. The planar block entries S_xx,S_xy,S_yy do NOT enter the source auxiliary projected commutator. Set
  k+=(3,1,0), k-=(-1,3,0),
  n+=(1,-3,0)/sqrt10, n-=(3,1,0)/sqrt10,
  W_sigma=n_sigma tensor n_sigma - ez tensor ez,
  V_sigma=n_sigma tensor ez + ez tensor n_sigma,
  p=7s1-s2, q=s1+7s2.
Exact full-grid source result for every real x,y node is:
  KA_out(S)(x,y) =
    cos(k+.(x,y)) [A W+ + B+ V+]
   +cos(k-.(x,y)) [A W- + B- V-],
  A=-e*d*t*w/2,
  B+=e*d*sqrt10*(p*u-q*v)/100,
  B-=e*d*sqrt10*(q*u+p*v)/100.
This is a full tensor equality, not only RMS.

Reason: first Lie on constant S is sym(S ez,s_a) times cos a·x; after the RAW TT_k projection only S ez survives; second z-shear Lie creates two Fourier sidebands, final RAW TT gives the two displayed tensor polarizations. The S planar block is killed already at first step. The two sidebands are distinct unwrapped legal signed RAW k for odd N>=7. For each sideband, W and V have Frobenius squared norm2 and are orthogonal; the cosines have mean-square1/2 and are mutually orthogonal. Thus EXACT squared Frobenius RMS:
  **||KA_out(S)||^2 = e^2*d^2 [
       (t^2/2)*S_zz^2
      +(s1^2+s2^2)/20*(S_xz^2+S_yz^2) ].**

In particular at odd N>=7, stable alpha:
  **KER(KA_out restricted to CONSTANT Sym²)**
     = {S: S_xz=S_yz=S_zz=0}, dimension3.
  rank =3.
In orthonormal Frobenius domain basis, the 6 singular values are:
  |e*d*t|/sqrt2 (multiplicity1),
  |e*d|*sqrt((s1^2+s2^2)/40) (multiplicity2),
  0 (multiplicity3).
The coefficient map (u,v,w)->(A,B+,B-) has exact determinant:
  -e^3 (s1+2s2)(2s1-s2)^3(s1^2+s2^2)/200,
nonzero within the stated range.

## T050.3 — nonperturbative bound for general H(z) with nonzero z-column mean

Let S=mean_z H(z). All original source operators preserve z Fourier frequency, because coefficients depend on x,y only and E/P are translation invariant. Parseval ensures
  **||KA_out(H(z))||_RMS^2 >= ||KA_out(S)||_RMS^2.**
If ANY of mean S_xz,S_yz,S_zz is nonzero, then KA_out(H(z)) !=0, while KC=KB=0. This extends ROT049's sufficient condition mean f(z)!=0 for H=f(z)I. If all three mean components vanish, nothing is asserted about nonzero ell-sector visibility; this result is NOT a kernel classification of ALL H(z).

## Direct original-helper source execution and independently exact audit

Route A full source program reproduce_int8_rot050.py: 4 odd N=7,9,11,15 ×2 source E modes ×6 constant symmetric S (I, xy-only, zz, xz, yz, mixed), plus 8 GENERAL NONPURETRACE H(z) cases: **56 original native full-grid cases PASS**. Every full KA tensor field matches independently constructed exact sideband formula to max component error<2e-11, while source KC and KB are zero within roundoff. For general H(z) source output mean_z equals KA(S), source Parseval lower bound and KC/KB0 all PASS. Source file hash checked before import. N9 E_lin alpha=.05 native RMS: S=I 0.203813955148, xy-only0, zz-only (w=.85) 0.173241861876, xz-only (u=.5) 0.072535116270, yz-only(v=-.4) 0.058028093016, mixed (u=.31,v=-.21,w=.74) 0.160305756199, nonconstant anisotropic H(z) with SAME mean S RMS0.232905514205, KC/KB0.

Route B complete INDEPENDENT SymPy+stdlib, NO NumPy, NO original helper or Route A: TWO EXACT symbolic full 3x3 sideband matrix identities, exact norm, kernel determinant/spectrum, formal E eigenshell equality; 60 independent exact-rational rank controls and 360 exact-rational norm controls PASS. Independent exact formula determinant as displayed.

## Reproduction, errors, custody

Full 8-member Moderator-local ZIP iw_int8_rot050_three_column_tt_kernel_repro_bundle.zip SHA256 34cb196303d1d50dff7501602ef7806d8568293bacac8f7f06ce58611a6fc6e7: full Polish report, TWO full standalone runnable Python, TWO frozen JSON, README, RUNLOG, SHA256SUMS. CRC PASS, SHA7/7 PASS. CLEAN A, CLEAN B with SHA-matched unchanged helper BOTH frozen JSON BYTE IDENTICAL. CLEAN C without original helper: all analytic constant-S records identical, exact independent JSON BYTE IDENTICAL, original source status SOURCE_SKIPPED_NO_HELPER (zero native source runs). An initial batch of clean replays timed out while checking the original slow 360-case symbolic substituter; rational test loop was refactored to exact Fraction while retaining all 360 source-free cases and symbolic 3x3 identities. Final A/B/C replays PASS; C first comparison mistakenly compared boolean actual_original_helper_ran true versus false, corrected compare only mathematics and preserve the distinct source statuses. No native helper source redistributed.

STRICT STOP: ALL H(z) claim ONLY KC/KB and shear-isospectrality; rank/kernel ONLY constant S; lower bound on H(z) requires visible mean z column. Full-grid RMS, not original masked source RMS, no historic masked production KA, even-N realcast, physical GR gauge/J3/K/Noether/GW, curved York, experimental measurement, general math novelty or canon. BW ingest/referee/original owner approval/Moderator EXEC all PENDING. NO_NEW_TASK_CASCADE.
