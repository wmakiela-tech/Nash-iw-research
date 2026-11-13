---
artifact_id: IW_GEEKY_S12_ROT022_M13_B_FIXED_MASK_ENERGY_SYMMETRY_ENHANCEMENT_ALPHA_ZERO_UNIFORM_POSITIVE_BERNSTEIN_001_20261113
cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
date: 2026-11-13
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
science_status: AUTHOR_SOURCE_SYMMETRY_GROUP_I1_PREFLIGHT_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: M13_PUBLIC_B_N41_AUXILIARY_FIXED_MASK_HYPOTHETICAL_TRANSLATIONS_ONLY / NO_HISTORIC_DTC0A_RUNTIME / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT022 — grupa okresów pięciu energii M13: dokładnie 16 przy alpha=0, dokładnie 2 dla wszystkich 0<alpha<=1/5

## 0. Firstness and current independent review

M13 FIRST source: original N41 B Fourier TT code research/m13/2026-10-24/verify_m13_rot33_interval.py, immutable Git blob c6377cfbc9a0070abc34ffedc5871e719f6a4679 (8970 bytes); original 25 quartic coefficients research/m13/2026-10-26/direct_B.json Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0 (7501 bytes). Actually executed originals, locked before importing.

Geeky ROT020 FIRST proposed a source-covariant COMMON shift of C1,C2,h against FIXED observer masks; obtained local 4x4 alpha-plus-three-translations rank and exhibited exact period (pi,pi,pi). M15 ROT013 independently recreated at iv50 the local rank proof and classified exact two-element PERIOD GROUP of the FULL TENSOR B at the SINGLE source point alpha=1/20=.05, based on an original 3-mode wavevector lattice of index2. That source I1 reviewer result belongs to M15, not ROT022:
https://github.com/wmakiela-tech/Nash-iw-research/blob/2613b178cfac6c1ede7f551bcbe6c3707bfbf17a/research/m15/2026-11-13/IW_M15_ROT013_INDEPENDENT_SOURCE_FOURIER_TRANSLATION_RANK_AND_EXACT_TENSOR_STABILIZER_001_20261113.md

M15 explicitly did NOT classify the possibly LARGER period group of five MASKED ENERGIES, or the exceptional alpha=0 boundary. ROT022 now closes both on source-typed real alpha entire [0,1/5]. Standard Fourier period-lattice and Bernstein polynomial tools, NO general mathematical novelty.

## 1. Exactly defined result, including ALL-t quantifier

For fixed alpha, original common Fourier translation is B_alpha,t(m)=exp(i m.dot(t))*B_alpha,0(m), due to convolution Lie/bracket and diagonal E_lin, centered stencil and TT projection. All five original observation windows k=2,3,4,5,6 remain spatially FIXED. This is a HYPOTHETICAL in-memory extension: source()/calc() original M13 do NOT expose a translation knob.

Define S_i(alpha,t) as the five disjoint shell energies, with weights W=(7778,6938,6146,5402,24389), and their common translation PERIOD GROUP

 G_alpha={u modulo 2pi Z^3: S_i(alpha,t+u)=S_i(alpha,t) for ALL t in T^3 and ALL i=1,..,5}.

THIS IS NOT the set of accidental pointwise coincidences for two individual t, NOT common-gain/projective-ratio aliases, and NOT a global injectivity theorem.

Innermost shell S5 equals original mask k=6 average g6. It has a finite Fourier expansion as a function of shift t:

 g6(alpha,t)=SUM_d C_d(alpha)*exp(i d.dot(t)),
 C_d(alpha)= W6(d) SUM_{m-n=d} <B_alpha(m),B_alpha(n)>_F / 6.

Here W6(d) is the exact original window_mode product. By uniqueness of the torus Fourier series, each nonzero C_d enforces exp(i d.dot(u))=1 on any period u. Three integer frequencies with index2 or index16 yield sharp finite group upper bounds.

## 2. alpha=0: independent exact SymPy source reconstruction, EIGHT tensor modes

ROT022 independently wrote a SymPy transcription of the original source field triple, Fourier bracket, nested Lie tensor actions and trace-free TT projector with the alpha=0 E_lin identically equal to one. The source stencil factors d1,d2,d3,d4 for Fourier modes 1..4 are retained as FOUR ALGEBRAICALLY INDEPENDENT real indeterminates, not numerical trigonometric approximations.

Of the original 41 candidate B output wavevectors, EXACTLY 33 have all 3x3 matrix entries equal to the zero polynomial in d1,d2,d3,d4, and EXACTLY EIGHT are nonzero:

 m=(±2,±1,±1).

Every nonzero symbolic tensor entry is a nonzero rational multiple of d1*(2*d1-d2). With theta=2*pi/41, original centered stencil d1=sin(theta)/theta and d2=sin(2*theta)/theta, so d1*(2*d1-d2)=2*sin(theta)^2*(1-cos(theta))/theta^2>0. Hence these eight modes are genuinely nonzero at original N41, not just formally generic.

All 41*9=369 complex entries of the independently reconstructed symbolic tensor were numerically re-evaluated through original source-directed mpmath.iv45 stencil factors and compared against ACTUALLY EXECUTED, UNMODIFIED original M13 calc(41,0)[B]; all 369 complex component difference intervals include zero. The symbolic identically-zero support theorem is algebraic, not inferred from those zero inclusions.

Integer HNF of eight wavevectors B0:
 [[4,0,2],[0,2,1],[0,0,1]], index8.
Therefore full TENSOR period group at alpha=0 has 8 elements.

Any energy Fourier difference m-n from those modes lies in 4Z x 2Z x 2Z. Its integer HNF is diag(4,2,2), index16. Thus all FIVE shell energy functions share AT LEAST the 16 periods
  (a*pi/2,b*pi,c*pi) with a modulo4, b,c modulo2:
all eight B modes receive a common sign (-1)^(a+b+c), leaving every fixed-window energy invariant.

Sharpness: three ACTUALLY RECOMPUTED original M13 B0 innermost mask6 Fourier coefficients have STRICT positive directed real parts:
 C_(4,0,0): lower 3.8728432378766406*1e-16;
 C_(0,2,0): lower 16.47001243704962*1e-16;
 C_(0,0,2): lower 16.47001243704962*1e-16.
Their 3x3 integer determinant is16, so even the innermost fifth energy has NO other global periods. Consequently:

  G_0 = {(a*pi/2,b*pi,c*pi):a mod4,b,c mod2}, exactly 16 elements.

The FULL B0 tensor group has 8, the raw FIVE ENERGY group 16 — their difference is genuine and mathematically sourced.

## 3. Uniform 0<alpha<=1/5: exact 12 directed Bernstein signs, no alpha scan

Source B is quadratic in alpha by original E_lin: B_alpha=U+alpha V+alpha^2 T from original tensor_polys(41). Every masked Fourier energy coefficient C_d(alpha) is quartic at most.

Original C1 odd total Fourier parity, C2 odd total parity, h even total parity imply every B output mode has EVEN total wavevector parity for ANY alpha; hence (pi,pi,pi) and identity are always tensor periods and thus five-energy periods.

To PROVE no additional FIVE-ENERGY periods for ANY real positive alpha up to 1/5, use these original innermost mask6 shift-frequency coefficients:
  dA=(-2,0,0), dB=(-1,1,-2), dC=(-3,0,1).

All three are absent from the exact alpha0 eight-mode difference support. Therefore their constant polynomial terms C_d(0) are EXACTLY zero; the source mpmath.iv zero-inclusion of raw coefficient a0 is a crosscheck, not the reason. Factor exactly
  C_d(alpha)=alpha*q_d(alpha)
with q_d cubic. The new code actually executes source-locked original tensor_polys(41) at iv.dps45 and original window_mode, reconstructs each quartic, and transforms REAL q_d to 4 Bernstein coefficients on the FULL interval alpha in [0,1/5].

All 12 rigorously directed lower bounds are STRICT POSITIVE; numbers displayed scaled by 1e16:
 dA: [646.822306618676,917.9860240804702,1184.0082057412537,1444.9614260848207].
 dB: [1.1550289035432877,0.8942261626180719,0.6382122873264195,0.3869204054552744].
 dC: [2.8574865376889993,6.199358708915106,9.478315177445339,12.695241935224683].

All 12 sign decisions were made using ACTUAL directed mpmath.iv45 interval lower endpoints, not displayed floats. All full string endpoints are in the executed JSON inside user ZIP. Therefore C_d(alpha) nonzero for EVERY alpha>0 in [0,1/5].

The integer 3x3 determinant of dA,dB,dC equals -2. They generate the entire index2 even-total-parity lattice in Z^3, so the innermost energy permits at most its TWO annihilator periods. Those TWO actually fix the FULL source tensor by parity. Hence uniformly, without sampling:

  G_alpha = {0,(pi,pi,pi)} for EVERY real 0<alpha<=1/5.

The full tensor period group is a subgroup of the energy group and contains the two parity periods, so it likewise has exactly two elements on the ENTIRE positive-alpha interval. This extends M15's fixed-alpha=.05 source result without claiming M15's first result.

## 4. Near-boundary first-order symmetry splitting and fixed-mask guard

At alpha0 the extra period u=(pi/2,0,0) preserves all shell energies. For dA=(-2,0,0), exp(i dA.dot(u))=-1, so the Fourier coefficient of
 Delta_alpha(t)=g6(alpha,t+u)-g6(alpha,t)
at frequency dA equals -2*alpha*q_dA(alpha). Its REAL q part has STRICT source Bernstein lower bound >6.46822306618e-14 throughout alpha in [0,1/5]. The ±dA conjugate terms and Parseval on normalized torus Haar measure yield a RIGOROUS source L2 lower bound:
  ||Delta_alpha||_L2(T3) > (1.82948e-13)*alpha, all 0<alpha<=1/5.

All coefficients of Delta vanish at alpha=0 algebraically, are source polynomials in alpha, so norm is also O(alpha). Thus the nontrivial extra alpha0 energy period is broken by Theta(alpha) in the ALL-t L2 sense near zero. Not a pointwise lower bound, not a measured noise tolerance. Exact group drops 16->2 at alpha0, but approximate distinction becomes arbitrarily ill-conditioned as alpha->0+.

Source original actual iv45 at t=0 quarter-x shift: at alpha=0 original mask6 difference contains zero within ~5.8e-55; at alpha=.05 strictly NEGATIVE ~-1.8325778429169984e-14. A separately authored NumPy FULL N41^3 spatial inverse FFT mask evaluator confirms alpha0 ALL five energies invariant under quarter-x shift and alpha=.05 mask6 change -1.8325778429169993e-14 (approx -26.45%). FFT diagnostic only; proof rests on symbolic source and directed Bernstein.

## 5. Executed artifacts, repeatability, strict controls

Full actual user ZIP name:
  Geeky_S12_ROT022_exact_mask_energy_symmetry_transition.zip
19182 bytes; SHA256 5495d8f5fb5e3ad28f9a2ef111a33f11581cdaa9455b4cd5ca8502c54344c6ba.
10 members including both BYTE-IDENTICAL original M13 source operator + quartic table, executed SymPy+mpmath.iv code, independent FFT code, clean replay/tamper script, three actual output JSON, README, SHA256 manifest. ZIP CRC, ALL 10/10 member SHA256 and full byte readback PASS.

Actual executed main Python SHA256 f0ba423d460839c8276ebfe34c863cbbce31d14ff59f440b3ac40097d7be7d94.
Actual 8309B full source result JSON SHA256 eadc03105b4f2158386dbb750511cff9fe0a553991f883c53f044b2162d32e8c.
Actual independent FFT script SHA256 b75dc6c3c9bb098dc8fcc3427e6c98c034397183a3d632f14c47809a0312b9aa; actual FFT JSON SHA256 8647398a8d8a5733b08ba6e1677f0833bf60e6450dcdefda0d4a06e2001f048f.
A clean isolated temporary-folder NEW Python3 subprocess reran the main code and produced a BYTE-IDENTICAL full result JSON. Deliberate one-file mutation separately to original M13 operator and original direct_B.json in temporary COPIES both caused nonzero exit ORIGINAL SOURCE GIT BLOB MISMATCH BEFORE original source import. Original M13 files untouched, fail-closed 2/2 PASS.

The actual executable source, all exact interval endpoints and full output are IN USER ZIP, not claimed as separate public GitHub original-code mirrors. Only report and curated results are on public GitHub.

## 6. Scope / no physics / pending referee

The defined group consists of uniform periods of the WHOLE raw five-energy translation response functions, NOT accidental individual t coincidences and NOT the period group of normalized projective ratios under unknown gain. The 16->2 statement is on the original PUBLIC M13 N41 B helper, at alpha restricted [0,1/5], with HYPOTHETICAL common field translations and FIXED observation windows. If masks co-translate, the result changes. The source() and calc() original signature has NO t knob; not physical calibration. No original historical dtc0a_runtime_v0_3_1.py bytes recovered, no physical NASH K/J3/TPE/GW/GR inference or source-new general Fourier mathematics.

M15 ROT013 independent reviewer accepted previous ROT020 tensor pointwise alpha=.05. ROT022's new alpha-boundary energy group and uniform positive-alpha theorem are AUTHOR-ONLY, independent REC11/AUD2/M15 mathematical referee PENDING; BW KN14 ingest and owner CANON adoption NOT VERIFIED. No task cascade or unnecessary decimal threshold optimization.

FINAL:
 ORIGINAL_M13_PUBLIC_SOURCE_GIT_BLOB_AND_N41_EXECUTION_PASS /
 SYMPY_33_EXACT_ZERO_EIGHT_NONZERO_SOURCE_MODES_ALPHA0_PASS /
 369_ORIGINAL_B_COMPONENTS_CROSSCHECK_PASS /
 EXACT_ALPHA0_ENERGY_PERIOD_GROUP_16_FULL_TENSOR_GROUP_8_PASS /
 ALL_12_ALPHA_POSITIVE_SOURCE_IV45_BERNSTEIN_SIGN_PASS /
 ALL_0_LESS_ALPHA_LE_0P2_ENERGY_PERIOD_GROUP_2_FULL_TENSOR_GROUP_2_PASS /
 ALPHA0_EXTRA_PERIOD_FIRST_ORDER_L2_BREAKING_PASS /
 INDEPENDENT_FFT_AND_CLEAN_REPLAY_AND_2_TAMPER_PASS /
 INDEPENDENT_REFEREE_PENDING / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
