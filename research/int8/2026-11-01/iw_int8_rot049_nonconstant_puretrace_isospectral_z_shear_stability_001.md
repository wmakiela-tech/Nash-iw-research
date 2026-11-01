---
artifact_id: IW_INT8_ROT049_NONCONSTANT_PURETRACE_ISOSPECTRAL_Z_SHEAR_STABILITY_001_20261101
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_SOURCE_OPERATOR_COMPATIBILITY_AND_GAUGE_TYPE_GATE_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_SOURCE_AUXILIARY_NONCONSTANT_PURETRACE_Z_FOURIER_ROBUSTNESS / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT049 — exact robustness of equal-filter-eigenshell projected TT nonclosure on nonconstant puretrace h=f(z)I

Date 2026-11-01. This is a mathematical **source-auxiliary** result with direct tests of the unchanged retained DTC0a helper. No claim is made about the unavailable original production runtime, historical masked K_A, physical gravity, canon or EXEC. Actual BW ingestion, independent referee and source-owner review unconfirmed.

## Provenance / mature outside host

MT13 FIRST owns original affine E_g / naive raw target-k alias. INT8 ROT016 FIRST owns source Q Lie E P with TT input; ROT046 FIRST showed single source projected_T(C,I) central-derivative versus RAW-k TT mismatch. ROT047 FIRST owns commuting z-shears, unmasked auxiliary K_C=K_B=0 but K_A_out nonzero for E_mode Identity. ROT048 FIRST owns the stronger exactly equal E_lin eigenshell pair a=(1,2,0), b=(2,-1,0), with constant H=I and K_C=K_B=0 but K_A_out!=0. ROT049 extends **only this source pair** to nonconstant h=f(z)I, proves an all-tensor Identity commutation lemma and supplies a planar-varying f(x) countercontrol. M13/M14 historic masked h=fI K_A, Geeky even-N original RAW cast, XH curved York and PRF theoretical work remain other owners.

External mature theory: compatible/mimetic discrete vector differential operators, Hyman–Shashkov, "The Orthogonal Decomposition Theorems for Mimetic Finite Difference Methods", SIAM Journal on Numerical Analysis 36(3), 788–818 (1999), DOI 10.1137/S0036142996314044. That paper is general background; the source-specific result below is not attributed to its authors. NO general mathematical novelty claimed.

## Original helper and precise carrier

Original retained user file deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801, byte checked BEFORE import. Its literal apply_T(C,H)=lie_derivative_tensor(C,apply_E(H)); compute_K_C, compute_K_B=P_RAW compute_K_C, and compute_K_A_out using inserted projected_T were used unmodified. Historical complete dtc0a_runtime_v0_3_1.py is BYTE-UNAVAILABLE; no original five-mask source RMS was executed. Original helper not redistributed.

Odd N>=7, spacing h=2pi/N, 3-torus, **full 9-component Frobenius RMS over every grid node**, not historic masked/6-component-normalized RMS. Real symmetric 3x3 tensor carrier. Two z-independent z-shear vector fields:
 C_a=e_z sin(x+2y), C_b=e_z sin(2x-y).
Source centered 2nd-order difference D_z; E_mode Identity or componentwise E_lin=I+alpha*h²*Laplacian2, alpha=.05 for native tests. Source RAW signed-k TT P_RAW is NOT the matched centered-wavevector projector. Input H=f(z)I where f is ANY real periodic scalar z-profile.

## T049.1 — EXACT SOURCE Identity-mode commutation on ALL tensor fields

Write g_a=sin(x+2y),g_b=sin(2x-y), J_g the Jacobian matrix of C=e_z g, with ONLY its z row and x,y columns nonzero. Exact source tensor Lie action for ANY tensor field H is
  L_g H = g D_z H+J_g^T H+H J_g.
Since g,J_g have NO z dependence, they commute with D_z. Since both J matrices have only z row with J_zz=0, J_a J_b=J_b J_a=0. Consequently the two Lie operators commute EXACTLY on ANY H:
  [L_a,L_b]H=0.
The source vector-field Lie bracket [C_a,C_b]=0 as well. Therefore E_mode=Identity implies compute_K_C=compute_K_B=0 for every H, not only h=I or a special scalar f. This is a special commuting shear subalgebra, NOT a general discrete Leibniz rule, and NOT a claim about all Lie vector fields.

## T049.2 — EXACT E_lin commutator cancellation for every f(z)I

On each z Fourier frequency ell, E_lin acts on f_ell(z)I with a scalar eigenvalue e_ell. First applying L_a or L_b produces only transverse planar wavevectors ±a or ±b, respectively, while preserving ell. Subsequent E_lin acts on these intermediates by the same scalar factor, because
  e_(a,ell)=e_(b,ell)
 =1−4alpha[sin²(h/2)+sin²(h)+sin²(ell*h/2)].
The source bracket of C_a,C_b remains zero. Thus the two orders of the complete source T_i=L_i E have exactly the same common scalar factor TIMES the already commuting L_a,L_b, separately for each ell. By linearity:
  **K_C(C_a,C_b,f(z)I,E_lin)=0, K_B=P_RAW K_C=0**
for ANY real periodic f(z). No smallness or smoothness assumption. This does NOT hold for generic dependence f(x,y,z).

## T049.3 — NONPERTURBATIVE positive lower bound after intermediate RAW TT projection

All source operators in compute_K_A_out preserve z Fourier frequency because both C_a,C_b are independent of z, E_lin and original RAW-k TT are translation invariant, and centered D_z preserves each ell. Therefore for fbar=mean_z f, Parseval gives
  ||K_A_out(f(z)I)||_RMS²
    = |fbar|² ||K_A_out(I)||_RMS²
       + sum_(ell!=0) ||K_A_out(fhat_ell exp(i ell z)I)||_RMS²
    >= |fbar|² ||K_A_out(I)||_RMS².

For this pair, the ROT048 exact all-grid constant-puretrace baseline is:
  ||K_A_out(I)||_RMS
   = |e0 (2s1−s2)(s1+2s2)|/(5 sqrt2)
where s1=sin(h)/h, s2=sin(2h)/h, e0=1−4alpha(sin²(h/2)+sin²h); e0=1 in Identity.
For N>=7 and stable alpha in [0,1/6], all factors are positive; hence if fbar !=0, **K_A_out(f(z)I) !=0 even though K_C=K_B=0**.

For explicitly positive f=1+eps cos z+delta sin(2z), |eps|+|delta|<1, sectors ell=0,±1,±2 are mutually orthogonal. The exact real-field Pythagorean identity is
 ||K_A_out(fI)||² =
 ||K_A_out(I)||² +eps²||K_A_out(cos z I)||² +delta²||K_A_out(sin2z I)||².
No additional perturbative constant is required. This is the FULL PERIODIC-grid L2/RMS identity and is NOT asserted for cropped/interior masks.

## T049.4 — scoped negative controls: planar f can restore nonzero K_C and K_B for E_lin

For Identity, T049.1 still forces K_C=K_B=0 on ALL H, including f(x)I or a random symmetric tensor. With E_lin and planar f=1+0.3 cos x, the first-stage modes ±a±(1,0,0) and ±b±(1,0,0) do NOT necessarily share the same spectral multiplier. Literal native source returns nonzero K_C and K_B; therefore the zero nonprojected commutator theorem is NOT transferable to arbitrary f(x,y,z), even if original shear modes a,b themselves lie on an equal E eigenshell. This is a material condition, not a source error in E_lin.

## Source-executed finite witnesses (all numerical values use full tensor Frobenius RMS)

| N | Mode | K_A(I) | K_A(f(z)I) | K_C(f(z)I) | K_C([1+.3cos x]I) | K_B([1+.3cos x]I) |
|---:|---|---:|---:|---:|---:|---:|
| 7 | Identity | .282294372013 | .395194506518 | 0 | 0 | 0 |
| 7 | E_lin alpha=.05 | .237154623087 | .310176433722 | 0 | .028755561546 | .012583961045 |
| 9 | Identity | .227987654379 | .454373954132 | 0 | 0 | 0 |
| 9 | E_lin alpha=.05 | .203813955148 | .377037692991 | 0 | .031946683340 | .013596410504 |
| 11 | Identity | .175581199794 | .502648899032 | 0 | 0 | 0 |
| 11 | E_lin alpha=.05 | .162529696937 | .436972822732 | 0 | .029184546819 | .012328969828 |
| 15 | Identity | .107306378337 | .568150540291 | 0 | 0 | 0 |
| 15 | E_lin alpha=.05 | .102828226321 | .523562072163 | 0 | .020998335517 | .008857711754 |

Here f(z)=1+.35 cos z+.20 sin(2z), positive with f>=.45 and mean1. Source KC and KB for f(z) are zero to floating roundoff, NOT claimed exact in floating point. Every numerical field identity, z-sector orthogonality, Pythagorean norm equality and exact source f=I baseline was asserted BEFORE JSON rounding.

## Independent executed audit and FULL reproducibility custody

ROUTE A standalone NumPy imports literal original user source ONLY after byte SHA check: eight full native (N=7,9,11,15 × Identity/E_lin) case suites using K_C, K_B, K_A_out for constant, z cos/sin/mixed positive, planar x control, and two N7/N9 random symmetric full H for Identity; all PASS. Nine analytic odd-N constant baselines up to N241; no full-grid original native run for N>15. No source can be imported if bytes do not match.

ROUTE B completely INDEPENDENT source-FREE stdlib Fractions, NO NumPy and NO Route A import, reproduces centered-difference cyclic 3³ exact rational grid and E=I+alpha Delta at alpha=1/20. Five different tensor inputs × Identity/E_lin =10 EXACT full 27-node 3x3 tensor cases: constant f, z-varying f(z), planar f(x), f(x+y), and a deterministic general tensor. Both same-spectral planar shear functions are exact Laplacian eigenfunctions with eigenvalue -6 on N3. Identity KC zero in ALL cases; E_lin KC zero for constant and z-varying, nonzero for planar and general tensor. PASS, including exact nonzero rational sums of squares. N3 is a standalone **algebraic consistency audit**; NOT claimed to be a source-original N>=7 RAW-k TT test.

NEGATIVE KNOWLEDGE: the initial hypothesis that arbitrary nonconstant f would produce a centered-difference Leibniz commutator defect was FALSE in this special z-shear Identity subalgebra. The actual E_lin boundary is **transverse** dependence of input f, which breaks the equal-eigenvalue first-stage relation. Do NOT claim source projector insertion is the only contributor for generic f(x,y,z).

Complete Moderator-local 8-member ZIP iw_int8_rot049_nonconstant_puretrace_isospectral_robustness_bundle.zip SHA256 **a4e44f89f816b0ed44c3589c5866b940c0701f82596e88584ec528c652087aae**, contains full longer Polish report, both full standalone Python, both frozen JSON, README, RUNLOG, SHA256SUMS. CRC PASS; 7/7 SHA256 member PASS. CLEAN A/B separate fresh extractions WITH unchanged SHA-verified helper: BOTH JSON BYTE IDENTICAL to frozen. CLEAN C without helper: exact Fraction JSON byte-identical and main analytic values identical, original native source correctly SOURCE_SKIPPED_NO_HELPER; no claim of native source execution in clean C. Original source not redistributed.

STRICT STOP: nonconstant f(z)I only for E_lin theorem; arbitrary H only for Identity lemma. Full periodic Frobenius RMS, not original five-mask study and NOT historical production h=fI calibration. No even-N RAW Nyquist casting, curved York, GR gauge, J3/K, Noether/GW physical claim, novelty, canon or EXEC. Independent referee, BW actual ING and source owner uptake PENDING. NO_NEW_TASK_CASCADE.
