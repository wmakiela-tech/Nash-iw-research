---
artifact_id: IW_INT8_ROT015_FFT_SPECTRAL_ALIASING_LIE_RESIDUAL_EXACT_WITNESS_AND_DTC_LOWBAND_CERTIFICATE_001_20261023
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
date: 2026-10-23
problem_id: P3_DTC0A_FFT_SPECTRAL_ALIAS_CONTROL_AND_DERIVATION_TYPING_001
document_type: EXACT_ALIAS_SYMBOL_WITNESS_AND_SOURCE_HELPER_SUPPORT_CERTIFICATE
exposure: PUBLIC
canonical_path: research/int8/2026-10-23/iw_int8_rot015_fft_spectral_aliasing_lie_residual_exact_witness_and_dtc_lowband_certificate_001.md
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
status: EXACT_DISCRETE_FOURIER_PROOF_AND_EXECUTED_NUMPY_SOURCE_SUPPORT_CHECKS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_J3_K_INVARIANT
---

# INT8 ROT015 — FFT differentiation is not a full-grid derivation: exact aliasing Lie residual and a positive source-generator low-band certificate

## 0. Scientific currentness and genuine subtraction

Currentness refreshed in IW dispatch on 2026-10-23. The originally contemplated E_lin(alpha) decomposition is NOW ALREADY SOLVED by:
* Geeky-S10: exact filter-composition Lie residual identity T_b(E²-E)+T1[E,T2]E-T2[E,T1]E with a source-local spectral test. Do NOT repeat as INT8 result:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s10/2026-10-23/geeky_s10_dtc0a_filter_composition_lie_residual_decomposition_001.md
* M13 ROT024: 18 source-rebuilt full-tensor quadratic-alpha coefficient identifications and 12 independent held-out alpha checks:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-23/IW_M13_ROT24_DTC0a_alpha2_tensor_identification_001.md
* XH-S4 ROT019: replacing centered D with FFT spectral derivatives gives K_C≈0 at alpha=0 on frozen smooth field classes, while inserted-projection K_A persists; high-band aliasing specifically noted as a limit:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-23/IW_XH_S4_DTC0A_TT_DOMAIN_SPECTRAL_DERIVATIVE_AND_COMMUTATOR_HOST_AUDIT_019_20261023.md
* INT8 ROT013 gave the exact CENTERED-difference Leibniz defect and a nonzero unprojected K_C. INT8 ROT014 gave a separate exact spectral low-band K_A≠0, K_C=0 TT input witness. These two mechanisms and source claims are not replaced here.

**Distinct delta:** The phrase 'replace central stencil by FFT differentiation' is mathematically under-specified unless the NONLINEAR pointwise products are source-declared alias-free or dealiased. We prove a sharp exact spectral-collocation Lie-closure defect, give a deliberately high-band counterexample with enormous K_C despite exact FFT differentiation, and verify that the ACTUAL preserved DTC0a smooth reference generator has a LOW-BAND certificate that EXCLUDES this counterexample mechanism on N=9/17/31. This simultaneously sharpens the negative and positive typed scope of XH019's spectral control.

The host is mature FFT pseudospectral aliasing / dealiasing literature, not novel mathematics:
* Hou & Li, *Computing nearly singular solutions using pseudo-spectral methods*, J Comput Phys 226 (2007), DOI 10.1016/j.jcp.2007.04.014 (2/3 truncation vs Fourier smoothing).
* Margairaz, Giometto, Parlange & Calaf, *Comparison of dealiasing schemes in large-eddy simulation of neutrally stratified atmospheric flows*, Geoscientific Model Development 11 (2018) 4069–4084, https://doi.org/10.5194/gmd-11-4069-2018.
* Lambert, Reneuve & Augier, *Aliasing and phase shifting in pseudo-spectral simulations of incompressible Navier-Stokes equations*, arXiv:2603.08892 (2026), SOURCE abstract and methodological overview; different Navier–Stokes host, no TT/Lie NASH theorem.

## 1. Declared mathematical carrier

Periodic scalar functions sampled at x_j=2πj/N, odd N≥5. Let m=(N-1)/2, and represent an integer frequency q by its folded frequency κ_N(q)∈{-m,…,m}, q≡κ_N(q) (mod N). FFT pseudospectral derivative D_N acts on the grid Fourier basis as
  D_N e^{iqx}=i κ_N(q)e^{iqx}.
For q already in [-m,m], it is the exact derivative at grid points of the continuous Fourier mode e^{iqx}.

BUT the gridwise product of two represented modes e^{ikx}e^{ilx} is the GRID function e^{i(k+l)x}, which Fourier-reconstructs at folded mode κ_N(k+l). Therefore the exact collocation Leibniz defect is
  E_N(e^{ikx},e^{ilx})
   :=D_N(fg)-fD_Ng-gD_Nf
   =i[κ_N(k+l)-k-l] e^{i(k+l)x}.           (1.1)
Writing κ_N(k+l)=k+l-Nw for integer winding number w yields EXACT
  E_N=-i N w e^{i(k+l)x}.                  (1.2)
It is ZERO if k+l remains within represented Nyquist band, and generally nonzero otherwise. This is a Fourier arithmetic identity, not a failure of FFT itself.

No nonzero linear derivation can satisfy the ordinary product rule on the whole finite pointwise function algebra (INT8 ROT013 prior elementary no-go). Thus exact spectral differentiation must also fail Leibniz on some high-band grid products; the point here is an exact, controllable witness.

## 2. Exact scalar-to-tensor Lie residual

Use the SAME flat covariant rank-two tensor Lie derivative formula as the retained user DTC helper but replace first differences with D_N. Set E=Identity and start with constant puretrace symmetric tensor H=I. Choose collinear vector fields C1=f(x)e_x,C2=g(x)e_x.

The ONLY nonzero tensor closure component is xx, and by direct source-formula substitution
  L_f H_xx=2 D_N f,
  [f,g]_N=f D_Ng-g D_Nf,
  K_C,xx=2[E_N(g,D_N f)-E_N(f,D_N g)].     (2.1)
For single complex plane waves f=A exp(ikx), g=B exp(ilx), EXACT
  K_C,xx
    =2AB(l-k)[κ_N(k+l)-k-l] exp(i(k+l)x)
    =-2Nw(l-k)AB exp(i(k+l)x).             (2.2)

For continuous differentiation D=∂x the closure is identically zero; the discrete effect is entirely the source's pointwise nonlinear collocation product and folded frequency, NOT a nonzero physical Lie bracket anomaly.

We do NOT import P_TT or the nontrivial E_lin filter into (2.2). With this one-axis input the produced xx tensor modes are longitudinal and P_TT kills them; this witness says nothing about an original K_A plateau.

## 3. Strong adversarial REAL high-band witness

Fix f(x)=sin(10x), g(x)=cos(13x). On odd N with both 10 and 13 represented:
- For N=31, Nyquist m=15, sum 23 folds to -8. Cross terms 10-13=-3 stay represented, so the complete exact real tensor residual is
  K_C,xx=93 sin(8x),  RMS=93/sqrt(2)=65.7609306503489.
- N=41, m=20, sum 23 folds to -18:
  K_C,xx=123 sin(18x), RMS=123/sqrt(2)=86.9741340859453.
- N=47, m=23, sum 23 is represented; the exact continuous and spectral-collocation residuals coincide at ZERO.
- N=61 likewise ZERO.

These results are not convergent monotonic scaling data for a fixed alias-free source. They are an explicit demonstration that even EXACT per-input-mode spectral derivatives do not enforce Lie commutator closure on arbitrary nonlinear grid products.

A NumPy FFT implementation independent of (2.2) measured:
| N | expected RMS | calculated RMS | max grid discrepancy to exact expression |
|--:|--:|--:|--:|
|31|65.7609306503489|65.7609306503489|1.27e-12|
|41|86.9741340859453|86.9741340859455|3.07e-12|
|47|0|8.18e-13|2.58e-12|
|61|0|1.92e-12|5.92e-12|

Numerical roundoff above is relative to unnormalized unit-amplitude f,g; unlike DTC source C≈.05/.04 these are deliberately adversarial high-frequency mathematical controls.

## 4. Positive certificate for ACTUAL retained DTC0a source generator

Inspected/byte-hashed user-retained helper:
  /mnt/data/deepseek_python_20260627_a87249.py
  SHA256=23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801.
Its function `generate_smooth_fields(N,2π)` is EXACTLY
  C1^x=.05 sin x,  C1^y=.05 cos y,
  C2^x=.04 cos z,  C2^z=.04 sin x,
  H_ii=.1 sin x cos y for i=1,2,3,
  H_ij=0 (i != j).
The helper is NOT the unavailable byte-identical original `dtc0a_runtime_v0_3_1.py` SHA256 2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084.

Every C vector component has Fourier support in coordinate frequencies with absolute values ≤1, and H has (|kx|,|ky|,|kz|)≤(1,1,0). The continuum Lie closure terms [L1,L2]H and L_[C1,C2]H are sums of products of *at most TWO vector fields and ONE tensor H*. Differentiation preserves support. Therefore a safe enclosing box for EVERY intermediate and final term is
  |kx|<=3,  |ky|<=2,  |kz|<=1.               (4.1)
In particular N≥7 odd (m≥3) represents every frequency in (4.1), so the FFT pseudospectral procedure on the retained field family (E=I) is ALIAS-FREE at N=9,17,31 and at all archived odd N31..41. This is a *source-field-specific sufficient test*, not a theorem for arbitrary fields or other generator versions.

Independent FFT 3D tensor Lie computation using the actual function `generate_smooth_fields` and native NumPy FFT derivatives, without evaluating any P_TT, obtained:
| N | max pointwise |K_C| (E=I, spectral) | maximum normalized Fourier coefficient outside the box (4.1) in EACH of the three raw commutator terms |
|--:|--:|--:|
|9|7.318364664e-19|8.35e-20|
|17|9.256376048e-18|5.33e-19|
|31|2.833833428e-17|1.63e-18|
Thus XH-S4 ROT019's independently reported spectral alpha0 K_C≈0 on the source field is supported by an EXACT NO-ALIAS-FREQUENCY CERTIFICATE. The different previously reported spectral RMS mask values use different normalization/quantities and must not be numerically equated.

For alpha>0, E_lin is a componentwise Fourier multiplier that preserves support and P commutes E, but the source-defined K_C contains unequal FILTER INSERTION counts plus [E,Lie] effects already exactly covered by Geeky-S10 and M13 ROT024. DO NOT interpret its nonzero alpha result as aliased Leibniz error.

## 5. Does generic 3/2 padding 'repair the Lie algebra'?

STANDARD DEALIASING often computes selected quadratic nonlinear products on padded grids then truncates to a chosen spectral space (Hou–Li, Margairaz et al.). For this high-band test, using a representation that contains k+l=23 (e.g. odd N>=47 for k=10,l=13) removes folding and restores the exact continuum identity.

But repeated spectral projection/truncation at INTERMEDIATE transport steps can itself create a projected-algebra nonclosure (ROT014 / Geeky-S10). Hence neither generic '2/3 rule', nor 'FFT derivative', nor 'higher N' without a declared supported band is a guarantee of vanishing PROJECTED K_A. This report certifies only the UNPROJECTED K_C of its exact carrier.

This distinction matters for any source upgrade: declare (a) derivative symbol, (b) product implementation/padding, (c) supported field modes, (d) intermediate filtering, (e) P_TT convention including k=0, (f) norm/mask. Otherwise 'spectral control' is not a complete reproducible claim.

## 6. One problem, one state

problem_id: P3_DTC0A_FFT_SPECTRAL_ALIAS_CONTROL_AND_DERIVATION_TYPING_001.
best_result: exact FFT aliasing Lie residual (2.2), a high-band single-mode-pair witness, AND a positive low-band support certificate for the *actually retained* DTC generator checked in 3D.
prior_hosts: mature Fourier pseudospectral aliasing/dealiasing; INT8 ROT013 finite-grid derivation impossibility; INT8 ROT014 projected algebra nonclosure; XH ROT019 spectral source experiment; Geeky filter composition and M13 alpha-coefficient analysis.
independent_referee: PENDING.
owner: M13 numeric DTC validation and LT5 living theory; INT8 supplies typed negative/positive certificate only.
blocker: no original runner byte identity, no direct declared physical TT target, no original source native validated continuum K/J3 physical interpretation, and no full-field spectral experiment on other actual field classes.
cheapest discriminator: For a new proposed spectral derivative control, compute a safe mode-convolution support box of all intermediate products; check against Nyquist; if exceeded, run identical algebra on a sufficient padded grid and compare. Do not imply no-alias from FFT alone.
decision: PASS exact synthetic counterexample and source-helper low-band certificate; HOLD archival physics and original-runner equivalence; no new task cascade.
canonical_path: research/int8/2026-10-23/iw_int8_rot015_fft_spectral_aliasing_lie_residual_exact_witness_and_dtc_lowband_certificate_001.md.
bw_status: GITHUB_PENDING_BW_INGEST / NO_REFEREE_OR_OWNER_ACCEPTANCE_INFERRED.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_NEW_TASK.


## Source-custody correction (2026-10-24, INT8 ROT023)
Earlier report text transposed two adjacent hexadecimal characters at positions 33–34 (one-based) of the retained helper SHA256, writing `...f9dcb9...` instead of the independently rehashed actual `...f9cdb9...`. This is a provenance transcription error, **not** a changed script byte or a mathematical/numeric correction. The executable reproducer code used the correct digest where checked. The original commit/blob remains an immutable historical receipt; this correction creates a new version. Direct source path: `deepseek_python_20260627_a87249.py`.
