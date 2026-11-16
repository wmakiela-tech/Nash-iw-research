---
artifact_id: IW_GEEKY_S12_ROT029_ORIGINAL_M13_SHARED_SITE_NOISE_CORRELATED_SIX_CHANNEL_OUTER_SHELL_FISHER_GATE_001_20261116
date: 2026-11-16
origin: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
science_status: AUTHOR_ACTUAL_ORIGINAL_M13_IV57_SOURCE_TWO_FOLD_BRACKETS_PASS / SAME_CELL_INDEPENDENT_41_CUBED_SPATIAL_CORRELATED_GLS_PASS / EXTERNAL_I1_ROT029_PENDING
prior_review: M15_ROT021_DIFFERENT_CELL_I1_PRIOR_GEEKY_ROT027_SIXTH_GLOBAL_SOURCE_CHANNEL_PASS
sync_state: GITHUB_PENDING_BW_INGEST
ceilings: HYPOTHETICAL_FIELD_SHIFT_AND_FIXED_SITE_GAUSSIAN_ENERGY_MEASUREMENT_NOISE / ORIGINAL_PUBLIC_M13_AUXILIARY_B_N41_ONLY / NO_HISTORIC_DTC0A_RUNTIME_IDENTITY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT029 — shared-site Gaussian energy noise forces shell/global correlations; exact outer-shell observation equivalence; source-certified Fisher recovery at two folds

## 0. Independent source reviews and firstness

M13 FIRST original public source B Fourier–TT N41 operator (original 8,970 bytes, immutable Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679) and directed original B25 table (7,501 bytes, Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0).

Original:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py
Original B25:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-26/direct_B.json

Geeky ROT023–024 FIRST identified two rank4 source Whitney folds, independently reviewed by M15 ROT017 and corrected AUD2 ROT016. Geeky ROT027 FIRST source-mathematically proposed unmasked full-domain B energy as sixth observable; it lifts both old folds locally and separates two Geeky ROT026 rigorously exact five-shell inverse pair boxes. M15 ROT021 NOW independently verified the sixth source channel on TWO DIFFERENT original M15 exact source inverse boxes and separately confirmed full local 6×5 rank at both old folds using actually executed original M13 native module at iv72, plus new deterministic error bounds. M15's different-pair results and deterministic thresholds are M15 firstness, and Geeky's prior sixth-channel source idea firstness is preserved. This is different-cell I1 for shared PRIOR ROT027 mathematics, not new ROT029.
M15 primary:
https://github.com/wmakiela-tech/Nash-iw-research/blob/f49727807c1e09e5214c82276189e8012563ec28/research/m15/2026-11-16/IW_M15_ROT021_INDEPENDENT_SIXTH_UNMASKED_NATIVE_M13_CHANNEL_ON_TWO_DIFFERENT_EXACT_ALIAS_PAIRS_AND_NOISE_GATE_001_20261116.md

Geeky ROT028 author-only derived conditional sixth Fisher information under FIVE independent equal raw-log noise variances sigma² and an INDEPENDENT new sixth raw-log variance tau². In ROT029 we instead model all six readings as generated from the SAME NOISY SPATIAL GRID. This mandates a different covariance and cannot silently inherit the ROT028 independent-output error assumption. No general statistical or Fourier mathematics novelty asserted.

## 1. Exact original M13 partition and mandatory correlations

Original N=41 side-length, M=41³=68921 sites. Five old source disjoint fixed k=2,..,6 shells occupy w=(7778,6938,6146,5402,24389), total 50653 sites. Missing outer complement w0=18268. For true original source shell means s_i(alpha,t)>0, full mean g(alpha)>0, and complementary outer mean o(alpha,t), the exact source spatial partition obeys

  M*g = Σ_i w_i*s_i + w0*o,
  o = (M*g−Σ_i w_i*s_i)/w0.

Hypothetical Gaussian measurement model, NOT actual physical DTC0a: an additive independent centered N(0,eta²) error on EACH measured spatial source energy density, with eta FIXED independent of source parameters. Observe five old shell sample means and full sample mean calculated from the SAME underlying site observations. The six raw ENERGY means are jointly Gaussian with parameter-independent covariance.

At positive source means, for the local log-score coordinates used by the original fold analysis, the exact Gaussian ENERGY-mean Fisher metric is obtained from induced tangent noise:

 Var(e_i)=eta²/(w_i*s_i²)
 Var(e_full)=eta²/(M*g²)
 Cov(e_i,e_full)=eta²/(M*s_i*g)
 Corr(e_i,e_full)=sqrt(w_i/M).

There is NO Gaussian logarithm-of-noisy-means claim; logarithmic derivatives are only invertible local tangent coordinates for the exact raw ENERGY Gaussian mean Fisher. The five correlations equal approximately

 (0.3359372667007052, 0.3172790252916493, 0.2986211013640649, 0.2799635583927755, 0.5948688278851081).

Their norm² is exactly 50653/68921, norm ≈0.8572881112237556; independence of old/full errors would be FALSE under this shared-site model. The covariance is strictly positive definite because

 Var(e_full | old e_i)=eta²*w0/(M²*g²)>0.

The ORIGINAL six observations are an invertible local representation of FIVE old disjoint shell means PLUS the OUTER mean o. In this latter representation all SIX energy-mean measurement errors are independent, variances eta²/w1,...,eta²/w5,eta²/w0. The ONLY genuinely added spatial information comes from the 18268 OUTER grid sites. A pseudo-sixth observation recombining only the five old shell readings is redundant and cannot restore an old fold.

## 2. Exact local source theorem at the two old rank4 folds

As since ROT020, t is a HYPOTHETICAL common spatial torus translation of original three Fourier input fields C1,C2,h RELATIVE TO FIXED observation windows, and b is a free common log energy gain. Original M13 source()/calc() expose NEITHER free t nor free b.

At exact old fold root, the five-old-log-source nuisance Jacobian X=[ones, D_tx log s,D_ty log s,D_tz log s] has full rank4, old alpha target score a belongs to range X. Let beta be unique a=X beta. Define outer shell nuisance score x_o=(1,D_tx log o,D_ty log o,D_tz log o) and alpha score a_o=D_alpha log o. Let delta_o=a_o−x_o beta.

Define the dimensionless noise at the nominal point epsilon=eta/g, where eta is the FIXED energy-density Gaussian noise standard deviation (epsilon is NOT a parameter-dependent physical noise mechanism). Put W=diag(w_i (s_i/g)^2). Then exactly for the Gaussian RAW ENERGY mean measurement model at the old fold,

  epsilon² * I_alpha =
  delta_o² / [ (g/o)^2/w0 + x_o (X^T W X)^−1 x_o^T ].

This is the classic nuisance-profiled Gaussian mean information in the equivalent outer-independent basis. It uses the EXACT local Gaussian ENERGY mean metric; no delta-method claim about the full distribution of logarithms. The old source full-domain directional score delta_full=vb+g'/g satisfies at the EXACT old fold

 delta_o = (M*g)/(w0*o) * delta_full

by differentiating the exact spatial energy partition while all five old outputs have zero derivative along the kernel. This equality is NOT falsely asserted at arbitrary nonroot alpha values in the containing root interval.

No global injectivity or statistical confidence interval follows. These are local Fisher metrics, not actual hardware noise estimates.

## 3. ACTUALLY EXECUTED ORIGINAL M13 source whole-bracket 57-digit enclosures

New independently authored source Python directly SHA-1 blob locks both original M13 files and SHA256 locks previous ROT027 exact source result JSON bb279334e39cbaabfdeae07085434ab10df6b1a5a9facc0b1eb370e34592e362 and ROT028 result JSON fbd42c3c75d1c1a6b0c3c7c2eaca60ed68a25be12ee1efd90f842498028d015e BEFORE original source import. It then ACTUALLY EXECUTES UNMODIFIED M13 tensor_polys(41), original inner/window_mode for all five nested shell energies, FOUR analytic source gradients, and full unmasked k0 energy. Strict outward mpmath.iv.dps57 signs are certified on TWO ENTIRE prior source alpha-fold brackets, not just midpoint guesses.

R1 alpha in (0.01861522133766,0.01861522134166):
- outer mean o strictly (2.028159664299e−14,2.028159674318e−14), POSITIVE;
- delta_o strictly (−0.358520542490,−0.357704326954), NEGATIVE;
- weighted old-noise nuisance q_o=x_o (X^T W X)^−1 x_o^T strictly (0.0057211323140,0.0057235515198), POSITIVE;
- normalized outer noise (g/o)^2/w0≈0.000105846089;
- epsilon² * I_alpha STRICTLY in (21.9495038937091,22.0589421324620).

R2 alpha in (0.05416739905600,0.05416739906000):
- outer mean o strictly (4.974143621413e−14,4.974143643467e−14), POSITIVE;
- delta_o strictly (−3.964786136459,−3.964352034779), NEGATIVE;
- q_o strictly (0.0310521620563,0.0310591688488), POSITIVE;
- outer noise normalized≈0.0000871490691;
- epsilon² * I_alpha STRICTLY in (504.588924345513,504.813001312706).

Both original source 4x4 old nuisance minors and NEW 4x4 weighted Gram determinants are strictly nonzero/positive across BOTH entire alpha brackets. Their full exact original outward interval endpoints and all source energies are retained in original actually executed complete source JSON SHA256 d7595642433b0ecd4cc3771b5878e465fb635cb74652182f3b9e907d4e98aa42.

**SOURCE NEGATIVE CONTROL ACTUALLY EXECUTED:** If proposed sixth energy is computed ONLY as weighted union of the five old shells, its derivative along the old fold kernel is exactly zero at each fold. Original directed source interval over each WHOLE alpha bracket correctly CONTAINS ZERO and refuses a false extra-information/rank-lift claim. Mathematically the outer complement is essential.

Not comparable directly with ROT028's sigma² I or tau² because their noise unit and independence structure differ from site-energy eta. The new source numerical coefficients carry no observed physical precision.

## 4. Independent observational route: 41³ spatial FFT and NONDIAGONAL GLS

A separate NEW NumPy Python program rebuilds original 41 complex 3x3 Fourier source mode fields and FOUR derivative fields directly into the entire 41³ Fourier grid, executes spatial inverse FFT, computes pointwise tensor Frobenius norm squared/6, and averages the original five FIXED cube masks and full space. It does NOT use M13 native inner/window_mode to obtain those measured means or their gradients.

It checks two mathematically equivalent, separately implemented Gaussian Fisher calculations:
(a) five old disjoint shell means + independent outer complement mean with heteroscedastic site-mean variance;
(b) five old means + full-domain mean, whitened under the correct NONDIAGONAL 6×6 covariance, then direct weighted nuisance-projected source information of the 6×5 Jacobian.

R1 direct correlated 6×6 GLS epsilon² I=22.00418398286927; outer independent version 22.004183982862532, relative discrepancy 3.063e−13.
R2 direct correlated GLS=504.70095497813816; outer independent version 504.7009549780999, discrepancy 7.58e−14.
Both numeric values lie STRICTLY inside original source IV57 whole-bracket enclosures. Source site geometry correlations are reconstructed from the independently built 6×6 covariance to better than 5e−15. Spatial FFT / NumPy are DOUBLE-PRECISION NUMERIC DIAGNOSTICS, NOT the directed proof, and NOT a different-cell I1 review.

## 5. Actually executed full custody and source-mutation controls

USER LOCAL SELF-CONTAINED 12-file executable ZIP:
 Geeky_S12_ROT029_correlated_pixel_noise_outer_shell_Fisher.zip
 33384 bytes
 SHA256 211f6ba8ebebfe0ae29e497bb75a6aaa2e5bbbf0bb4412f58c09ee2fe0d5ae09.

CRC PASS, exact byte readback of ALL 12 members PASS, all 11 manifest SHA256 payloads PASS. Contains UNMODIFIED original M13 helper and B25 table, prior original actual ROT027 and ROT028 source JSON proof inputs, NEW actually executed original source IV57 script SHA256 10223675b25a1436bc03b6d32d1e23cd03676760380362666eda3e105b624590, original full source result JSON SHA256 d7595642433b0ecd4cc3771b5878e465fb635cb74652182f3b9e907d4e98aa42, independent FFT/GLS Python SHA256 fe2bbc32f26825384591e7bd530b9ff92d6bca69105da7ef9d26986a9ca34a97, complete independent result SHA256 298706eb4d4237b7b9e8b2ed551f58fc2fb46026558db7219c92ba5a9942b33d, clean replay/tamper Python and ACTUALLY executed receipt SHA256 f31554b00187c11b32f9326007e8d1b78c93585fa84ff2b0aad4703eb49be2d4, detailed README and manifest.

The replay controller ACTUALLY extracted TWO separate fresh temp directories, independently ran the original source verifier and FFT verifier as fresh Python subprocesses, and verified COMPLETE resulting JSON files BYTE IDENTICAL to original archive. BOTH PASS. SEVEN separate one-byte input mutations of original M13 module, original B25, prior ROT027, prior ROT028 and new ROT029 proof JSON (as relevant for each script) were rejected BEFORE SCIENTIFIC IMPORT with SOURCE_IDENTITY_MISMATCH and nonzero exit, 7/7 PASS. Untouched originals preserved. NO timeout counted PASS. Full executable byte strings and complete original source interval results are in user ZIP; no false claim of exact script byte mirror in public GitHub.

## 6. Limits, review and custody status

Original public M13 B N41 AUXILIARY source ONLY; NOT a reconstruction of missing historic dtc0a_runtime_v0_3_1.py. Translation t, gain b and per-site independent fixed-variance Gaussian energy measurement errors are explicitly HYPOTHETICAL mathematical observer/model assumptions, NOT source-established sensor/hardware calibration or real noise covariance. Additional six-channel data do not exist as authenticated historic observations. No finite-sample nonlinear confidence or global injectivity theorem, no K/J3/TPE/GR/GW physical result and NO general novelty of classical Gaussian statistics.

M13 original FIRST, Geeky ROT027 new full-domain sixth channel FIRST, M15 ROT021 independent different-cell review of prior sixth-source idea on other exact pairs FIRST, Geeky ROT028 IID raw-log conditional information FIRST within chain, Geeky ROT029 new shared-site noise correlated model/source-specific Fisher intervals AUTHOR SAME CELL only. DIFFERENT-CELL ROT029 I1 PENDING. KN14 BW native source ingest and M15 owner CANON not verified; GITHUB_WRITE and SLACK_POST do not confer signoff.

Recommended bounded external referee: independently reconstruct the exact 5+outer partition, compute 6×6 covariance from IID site errors and verify its positive Schur complement; source-run original M13 at BOTH full root brackets and derive positive outer-source information and inner-only control, without importing the author's interval verifier. No new task cascade.

FINAL:
 M15_ROT021_PRIOR_ROT027_SOURCE_I1_DIFFERENT_CELL_PASS /
 ORIGINAL_SOURCE_M13_SHARED_SITE_CORRELATION_AND_OUTER_SHELL_EQUIVALENCE_PASS /
 TWO_WHOLE_BRACKETS_SOURCE_IV57_POSITIVE_OUTER_ENERGY_AND_GAUSSIAN_MEAN_INFORMATION_PASS /
 SOURCE_INNER_ONLY_FAKE_SIXTH_NULL_NEGATIVE_CONTROL_PASS /
 SAME_CELL_INDEPENDENT_SPATIAL_6BY6_CORRELATED_GLS_MATCHES_OUTER_INFORMATION_PASS /
 TWO_COMPLETE_BYTE_IDENTICAL_COLD_REPLAYS_AND_SEVEN_ONEBYTE_FAILCLOSED_ATTACKS_PASS /
 USER_ZIP_CRC_12OF12_BYTE_11OF11_SHA_PASS /
 ROT029_EXTERNAL_REFEREE_PENDING / BW_PENDING /
 NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
