---
artifact_id: IW_INT8_ROT046_NATIVE_CENTERED_LIE_RAW_TT_COMPATIBILITY_001_20261029
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_SOURCE_OPERATOR_COMPATIBILITY_AND_GAUGE_TYPE_GATE_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_SOURCE_DIRECT_CENTERED_DERIVATIVE_RAW_TT_SYMBOL_MISMATCH / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# INT8 ROT046 — source-native central Lie derivative versus raw-k TT projection: exact compatibility gate

Scientific date: 2026-10-29. Full independent mathematical proof and unchanged original auxiliary source tests. The historic complete dtc0a_runtime_v0_3_1.py source is BYTE UNAVAILABLE; no historic masked K_A or physical experiment is claimed. Source-owner adoption, BW ingest, external referee and Moderator EXEC are PENDING.

## Previous owners and classical host

MT13 FIRST identified naive target raw-k TT alias and exact flat metric E_g transport; INT8 ROT016 FIRST established source-native **Q Lie_C E P** leakage for nonzero frequency TT tensor inputs; INT8 ROT017 FIRST investigated E-filter affine covariance, ROT033 metric-indexed TT naturality, ROT034–045 other finite TT locality/norm questions. THIS ROT046 investigates a distinct source operator order and input: P_raw Lie_C^(centered) I with **spatially CONSTANT puretrace input h=I**, not ROT016's TT input and Q-output. M14/M13 own original h=fI masks and historical K_A; Geeky even-grid realcast/full Lie, XH curved York and PRF theoretical process studies are separate. No credit displacement.

Classical compatible/mimetic discrete operator host, NOT a new general theorem: J. M. Hyman and M. Shashkov, *The Orthogonal Decomposition Theorems for Mimetic Finite Difference Methods*, SIAM J Numer Anal 36 (1999) 788–818 DOI 10.1137/S0036142996314044; K. A. Trapp, *Inner products in covolume and mimetic methods*, ESAIM:M2AN 42 (2008) 941–959 DOI 10.1051/m2an:2008030. This is a source-defined mathematical falsifier, NOT GR gauge physics.

## Exact retained source, tensor carrier and distinction

The user-retained unchanged auxiliary DTC0a file deepseek_python_20260627_a87249.py has SHA256:
  23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801.
Use its literal routines derivative, lie_derivative_tensor, apply_E, apply_P_TT, projected_T. Odd N>=5 source grid (Z/N)^3 with lattice step h=2*pi/N, real Sym²(R³) fields, raw-signed-k Fourier TT projection P_k=I-kk^T/|k|² at nonzero k. The central second-order derivative on a wave exp(i k·x) has modified Fourier wavevector
  s_N(k)_j=sin(2*pi*k_j/N)/(2*pi/N).
That differs from raw signed FFT k in general.

Choose h_tensor(x)=I3, CONSTANT and puretrace; vector field C(x)=e_z sin(k·x) at signed nonzero source k=(p,q,0). Here coordinate x=2*pi*j/N. The source lie_derivative_tensor(C,I) has convective term zero, so its EXACT tensor value on every grid node is
  H(x)=cos(k·x) [s_N(k) tensor e_z + e_z tensor s_N(k)].
This statement is source-specific to the SINGLE Lie derivative and should NOT be carried to compute_K_A_out or historical masks.

## Exact source mathematical theorem T046.1 — a nonzero TT component from incompatible symbols

Let Q_k=I−kk^T/|k|² and s_perp=Q_k s_N(k). Both k and s are in the xy-plane and e_z is transverse to each. Source raw-k TT projects the above H to
  P_TT H(x)=cos(k·x) [s_perp tensor e_z + e_z tensor s_perp].
Its real grid Frobenius RMS (mean over nodes, full 9 tensor components summed BEFORE square root) equals EXACTLY
  **L_N(p,q) = |s_perp|
    = |q*sin(2*pi*p/N)/h − p*sin(2*pi*q/N)/h| / sqrt(p²+q²)**,
where h=2*pi/N.
Reason: mean cos(k·x)^2=1/2 for any odd N nonzero k; squared Frobenius norm of the symmetric tensor is 2|s_perp|². Thus no asymptotic continuum approximation is involved.

Consequently P_raw Lie_C I=0 for this fixed e_z-polarization IFF s_N(k) is parallel to k. Axis k=(p,0,0) or equal-magnitude k=(p,p,0) provide EXACT zero controls. A generic unequal two-coordinate k produces NONZERO TT. This is NOT a coding fault of either individual function; they realize incompatible but internally defined discrete symbols.

## T046.2 — frequency-controlled asymptotic falsifiers

(1) FIXED SMOOTH k=(1,2,0). Let h=2*pi/N. Exact
  L_N(1,2)=2*sin(h)*(1−cos(h))/(h*sqrt(5)).
Therefore N² L_N(1,2)→4*pi²/sqrt(5) ≈17.6553. Source leakage for this chosen fixed smooth mode is O(N^-2).

(2) LEGAL HIGH k=(1,m,0), m=(N-1)/2 on odd N. L_N(1,m)→1. No uniform disappearance of this compatibility residual over all legal frequencies.

(3) STRONGER HIGH k=(2r,r,0) at N=4r+1, r>=1. Exact
  L_N(2r,r)=|s_N(2r)−2 s_N(r)|/sqrt(5).
Since s_N(2r)→1/2 and s_N(r)~N/(2*pi), one has
  **L_N(2r,r)/N→1/(pi sqrt(5)).**
This is a lower bound showing a centered-derivative L2-to-L2 operator mismatch whose norm can grow linearly with N on high frequencies; it is NOT a physical instability because derivatives themselves are unbounded as L2→L2 in the continuum.

## T046.3 — strictly separate compatible reference, NOT authorized source repair

For any odd N and any nonzero source k, s_N(k)!=0. An alternative, hypothetical TT projector based on the ACTUAL centered difference symbol s_N(k) (as opposed to raw k) satisfies
  P_TT[s_N(k)] [s_N(k) tensor u+u tensor s_N(k)] =0
for any u in R³. This is a formal mimetic consistency reference ONLY. Substituting the s-based projection in the historical helper would change the claimed source operator and requires source owner approval; NOT done or recommended as an unreviewed fix. This doesn't solve full Lie algebra, original masked K_A, or GR gauge.

## Actually executed independent checks, exact math and negative knowledge

ROOT A standalone NumPy plus original SHA-pinned auxiliary DTC0a:
 - TEN distinct finite signed k analytic source-polarization cases; exact 3x3 symmetric TT_k projection compared with the s_perp closed form; compatible hypothetical TT_s kills the SAME tensors, including two exact zero-controls;
 - EIGHT ORIGINAL literally executed projected_T(C,I,E_mode=Identity/E_lin,order=2,alpha=.05,dx=2*pi/N) on odd N=5/9/15/21/31. Every direct source Lie derivative, original E-mode(I)=I, and final source TT output matches full-grid analytic tensor to component infinity error <8e−12 on UNROUNDED arrays. Source helper SHA verified before import. Examples (RMS):
    N5 k(1,2,0) .467744641894;
    N9 k(1,4,0) .774414782869;
    N15 k(1,7,0) .891058187032;
    N21 k(1,10,0) .930691015827;
    N31 k(1,15,0) .957764976489;
    N31 smooth k(1,2,0) .018183877210;
    k(1,1,0) at N9 EXACT ZERO.
 - Eight analytical HIGH mode N=4r+1 samples to N1025 support L_N/N→1/(pi sqrt5); eight SMOOTH mode samples to N1025 support N²L_N→4pi²/sqrt5. Large N are JUST SCALAR analytic checks, not N1025 original helper runs.

ROOT B wholly independent SOURCE-FREE SymPy/stdlib, no NumPy or source/helper import:
 - five symbolic real 3×3 identities for k=(1,2,0) with independent s_x,s_y variables: TT projector closed form; squared Frobenius norm=2|s_perp|²; s_perp²=(2s_x-s_y)²/5; continuum-compatible sym(k,e_z) projects exactly0;
 - **240 EXACT rational** cases with (k=(a,b,0),s=(c,d,0)), including **104 ZERO** controls; hypothetical TT_s always kills gradient tensor where s!=0.
 - exact rational counterexample k=(1,2,0), s=(1,3,0) yields TT squared Frobenius norm 2/5.
All PASS.

No native full masked K_A run, no all-N physical model claim, no even-N Nyquist rawcast claim. The original helper file is not redistributed. NO_NEW_TASK_CASCADE.

## Reproducibility and limits

Moderator-local complete 8-member ZIP:
  iw_int8_rot046_native_centered_derivative_raw_tt_mismatch_bundle.zip
SHA256 **04aae7443d4ed8166057db14c3067dbbbdf0b31c6b296cac15742729328d5b1d**
ZIP CRC PASS, SHA256 payload 7/7 PASS. Two CLEAN extractions with SHA-pinned helper reproduce BOTH JSON files BYTE IDENTICAL. Third CLEAN extraction without helper: EXACT independent SymPy JSON byte-identical, numerical math fields unchanged and source marked SOURCE_SKIPPED_NO_HELPER. Includes complete longer Polish report, two standalone executable Python scripts, frozen main and exact JSON, README, RUNLOG and SHA256SUMS.

The data h=I are a special constant puretrace member of the historic broader h=fI class, but result is solely on one projected_T module. P_raw I=0 does not entail P_raw Lie_C I=0. No original runtime, source masks, physical covariance, conformal gauge, gravitational-wave output, J3/K, Noether, novel general mathematics or owner adoption. Referee/owner/Moderator EXEC and actual BW ING all unverified.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
