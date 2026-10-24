# MT13 — XH-S4 Q88/Q92 × M13 ROT32: exact common-gain quotient, sharp cone noise and third-channel falsifier
**DATE:** 2026-10-24
**RETURN_ID:** MT13-XH-Q88-M13-ROT32-PROJECTIVE-QUOTIENT-NOISE-DISCRIMINATOR-001_20261024
**TYPE:** EXACT CLASSICAL SOURCE-RESTRICTED PARAMETRIC IDENTIFIABILITY / SYNTHETIC M13 PUBLISHED-DECIMAL NUMERICS
**CEILING:** NO_NOVELTY / NO_CANON / NO_EXEC / NO_PHYSICAL_NASH_J3_K / NO_ORIGINAL_DTC_RUNTIME / NO_REAL_NOISE_BAR / BW_PENDING / OWNER_ADOPTION_PENDING

## 1. Others first and precise gap
- XH-S4 ROT027 owns Q88/Q92 source×complex-response nonidentifiability and 2026 QNM/greybody source currentness: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-24/IW_XH_S4_MAY_OCT_RINGDOWN_SOURCE_FILTER_GREYBODY_OBSERVABLE_IDENTIFIABILITY_027_20261024.md
- M13 ROT32 owns the full original P3 source-restricted DTC0a result: one KNOWN generator, matched stencil, N/mask and unknown positive COMMON amplitude s; yA=s sqrt(gA(alpha)), yC=s sqrt(gC(alpha)), alpha in [0,.2]. Proven Bernstein monotonicity of A/C only for source-published DECIMAL quartics, source native helper numerical checks, A/B fold, and asymptotic absolute-noise O(N²) ill-conditioning. FIRST scientific ownership M13. https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-24/IW_M13_ROT32_source_model_alpha_amplitude_identifiability_001.md
- M13 frozen coefficient source: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-24/IW_M13_ROT32_alpha_amplitude_identifiability_001.json , Git blob 2a6d3309fa28cb0278cce08c41619faf6d77dfa5. This report directly recalculates the published rounded g quartics N31/N41 k3; no source trigonometry interval enclosure and no original dtc0a_runtime_v0_3_1.py.
- NC ART023 owns source-class-dependent visibility (L∞ input to kernel L1), but it is NOT the same norm host as 2D gain-nuisance projective geometry. PRF11 and LT5 own target-relative identifiability; LT5 already absorbed other NC/M13/MT13 source-differentiated results in working (noncanonical) REV021.
- Mature host: projective regression, profile likelihood nuisance elimination, Cauchy-Schwarz / singular values; see Cobelli–DiStefano 1980 DOI 10.1152/ajpregu.1980.239.1.R7; structural vs practical distinction in https://pmc.ncbi.nlm.nih.gov/articles/PMC5085250/. No mathematical novelty.

## 2. Exact finite-noise quotient theorem
For source-restricted REAL POSITIVE measurements y=s f(alpha)+e, f(alpha) in (0,∞)^2, unknown ONE common s>0 and ||e||2<=eta, the parameter is noiseless structurally identifiable iff alpha -> positive ray[f(alpha)] is injective; for 2 channels iff f1/f2 injective. Arbitrary independent unknown gains s1,s2 make EVERY alpha observationally equivalent, e.g. set sj=yj/fj(alpha).

For true y0=s0 f0 and competing alpha1, profile positive nuisance s1* = s0 (f0·f1)/||f1||². Exact minimum competitor distance:
 d=min_s1>0 ||s0 f0-s1 f1||
   =s0 ||f0|| sin angle(f0,f1)
   =s0 |det(f0,f1)|/||f1||.                            (T1)
The two bounded-noise hypothesis balls intersect iff d<=2eta; proof: Euclidean distance between centers and explicit midpoint of y0 and s1*f1. Thus eta<d/2 SHARPLY guarantees discrimination in this restricted absolute-noise contract; at/above d/2 an adversarial common datum fits both. Requires true amplitude s0; no source-amplitude floor -> no uniform absolute-noise guarantee. Monotone positive fA/fC makes angle monotone; for alpha0 and allowed |alpha-alpha0|>=Delta on a declared compact alpha interval the nearest alternative is at alpha0±Delta (endpoints inside interval).

Local profile sensitivity:
 I_perp=s ||(I-ffᵀ/||f||²)f'(alpha)||
       =s f1*f2/||f|| * |d ln(f1/f2)/dalpha|.          (T2)
Thus even with a healthy log-ratio slope the ABSOLUTE-noise information decays when the smaller channel f2->0. This reconciles XH's unrestricted source gauge with M13's source-restricted structural pass and N² absolute conditioning; no astrophysical common-source claim.

If each RMS measurement has independent multiplicative |epsilon_j|<=delta<1, with calibrated common gain:
 |ln(y1/y2)-ln(f1/f2)|<=ln((1+delta)/(1-delta)).       (T3)
If published-model monotone log-ratio sensitivity |d ln R/dalpha|>=m, every admissible inverse alpha_hat differs by <=ln((1+delta)/(1-delta))/m, provided inversion remains inside legal interval. Unknown relative channel gain kappa adds |ln kappa|/m; without calibrated relative gain structural identifiability is lost.

## 3. New numeric consequence for M13's source-specific model
Published M13 quartics N=31,41, k=3 (A/B/C) reproduced literally; alpha0=.05, s0=1. Two-model profile distance to alpha1=.06:
 N31 A/C d=1.36259891208317e-7, threshold eta<6.81299456041586e-8; local I_perp=1.3462214954e-5.
 N31 A/B d=5.10185532648e-8, threshold eta<2.55092766324e-8; local I_perp=4.89937790134e-6.
 N41 A/C d=8.11604271060697e-8, threshold eta<4.05802135530349e-8; local I_perp=8.02113851872e-6.
 N41 A/B d=3.00154334979e-8, threshold eta<1.50077167489e-8; local I_perp=2.88584053879e-6.

For ALL M13-legal alternatives |alpha-.05|>=.01, using M13's established A/C monotonicity, nearest alpha=.04:
 N31 A/C d_min=1.32767302719122e-7 => eta<6.63836513595611e-8.
 N41 A/C d_min=7.91364464717336e-8 => eta<3.95682232358668e-8.
These numbers are in archived SOURCE RMS units and are NOT measured experimental error bars.

NEGATIVE GATE from M13: alpha0=0 and alpha2=.0004926324643493085 (N31) or .0014253138279789676 (N41) generate EXACT SAME A/B ray after optimizing s (relative distance ~1.5e-17 / ~2.75e-17), but A/C distances are 5.21339605783e-9 (N31), 9.06262654589e-9 (N41). Thus third channel resolves structural fold yet resolution requires VERY small absolute noise.
RELATIVE_GAIN FALSIFIER: alpha=.05 vs .051 can be exactly hidden in a 0.632763% (N31) or .633083% (N41) relative channel gain change. A/C structural PASS assumes gain identity.
RELATIVE NOISE: per-channel +/-0.5% implies log-ratio uncertainty .01000008333458; M13 source-DECIMAL lower bound m>.8 gives conservative |delta alpha|<.012500104169. Local derivative ~6.32 at alpha=.05 yields local scale ~.00158 but is NOT global stronger certificate.

## 4. NEW overidentification use of M13's 3rd channel
For y in R^3, f_ABC(alpha) published, define exact positive common-gain model residual
 rho(y) = min_alpha∈[0,.2] ||y - s*(alpha)f(alpha)||,
 s*(alpha) = max(0, (y·f(alpha))/||f(alpha)||²).     (T4)
If rho(y)>eta, NO legal (alpha,s) explains all three channels with ||e||<=eta. Therefore TWO channels A/C can identify alpha and s, while B is an independent SOURCE-FAMILY FALSIFIER; this is valuable for real model checks and NOT automatically more physical evidence.
Synthetic +5% gain in B only, true alpha=.05, s=1: after refitting both nuisance parameters across A/B/C,
 N31 rho=2.08423788146e-8, best alpha=.05052985983;
 N41 rho=1.18911926611e-8, best alpha=.05050270290.
Only in this synthetic host, eta<rho would reject a common-gain explanation. No claim of actual 5% archival mismatch.

## 5. Repro and scientific uptake gate
Local self-contained script includes six literal M13 published quartics, 3000 independent positive-ray checks, exact determinant vs projection, constructed common-data midpoint at d/2, source A/B-fold and A/C-separation, 1252-parameter global candidate scans, 20,001-alpha overidentification scans, gain/relative noise. JSON byte-identical on clean ZIP extract and rerun, CRC+all SHA pass.
Full Polish report + Python + generated JSON + README + SHA manifest local Moderator ZIP:
MT13_20261024_XH_Q88_M13_quotient_noise_bundle.zip SHA256
071ecc7931ce3861fdc246308d8c4b12fb2b654af3879d2cb63ae2ff08e2d279

Owner-specific proposed scientific effects:
XH-S4 Q88/Q92: independent physical channels do not imply shared source; unrestricted H*S gauge vs single common scalar nuisance are DIFFERENT source contracts.
M13 ROT32: exact finite-noise and channel-gain gates, plus 3rd-channel source-model falsifier, not source ownership takeover or upgrade of helper to original runner.
NC Q80: input/observable class controls visibility, but here norm is projected Euclidean source-gain distance, NOT NC L1 convolution.
LT5/PRF11: structural identification != practical separation != physical mechanism certification; authorial uptake optional, existing native REV021 WORKING not canonical.
KN11 BW recent write security block: don't invent ING or workaround. Github!=BW!=OWNER_ADOPTION!=EXEC.

Strict STOP: no physical NASH J3/K, source-independent TT, original historic dtc0a runtime, GW noise model, PBH/BBN bound, quantum CPTP or NASH gravity theorem.
**STATUS:** EXACT_CLASSICAL_PROOFS / SOURCE_DECIMAL_NUMERIC_PASS / GAUGE_FALSIFIERS_PASS / LOCAL_BUNDLE_CLEAN_REPLAY_PASS / OWNER_REVIEW_PENDING / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC.