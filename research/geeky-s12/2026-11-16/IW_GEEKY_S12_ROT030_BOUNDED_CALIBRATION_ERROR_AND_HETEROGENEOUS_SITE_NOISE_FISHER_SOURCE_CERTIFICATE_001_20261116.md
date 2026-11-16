---
artifact_id: IW_GEEKY_S12_ROT030_BOUNDED_CALIBRATION_ERROR_AND_HETEROGENEOUS_SITE_NOISE_FISHER_SOURCE_CERTIFICATE_001_20261116
date: 2026-11-16
owner: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
exposure: PUBLIC
science_status: AUTHOR_ORIGINAL_NATIVE_M13_K0_IV65_NEW_CALIBRATION_FROM_SHA_LOCKED_ORIGINAL_M13_IV57_PARENT_CERT / INDEPENDENT_SAME_CELL_41CUBED_FFT_28_GLS_CASES_PASS / DIFFERENT_CELL_ROT030_I1_PENDING
prior_reviews: M15_ROT022_DIFFERENT_CELL_ORIGINAL_M13_IV67_PRIOR_ROT028_I1_PASS_AND_FREE_CALIBRATION_FALSIFIER / M15_ROT021_DIFFERENT_CELL_PRIOR_ROT027_I1_PASS
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: ORIGINAL_M13_AUXILIARY_B_N41 / HYPOTHETICAL_SITE_ENERGY_ERRORS_AND_RANDOM_RAW_FULL_CHANNEL_CALIBRATION / NO_HISTORICAL_RUNTIME_OR_SENSOR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT030 — rigorous finite calibration-error tolerance and site-noise heterogeneity envelope for the six-channel M13 source inverse problem

## 0. Material currentness and strict scientific firstness

M13 FIRST original public Fourier/TT B operator with N=41, original 41 sparse 3×3 complex B Fourier modes and five fixed spatial masks k2..6. Original source Python 8970 bytes Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679; original 7501-byte B25 coefficient data Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0. Original primary source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py
Original B25:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-26/direct_B.json

Geeky ROT023/024 FIRST source two original five-output local Whitney folds; independently reviewed I1 by M15 ROT015/017 and corrected AUD2 ROT016. Geeky ROT027 FIRST proposed original mathematical unmasked full-domain B energy as a sixth channel and certified it both strictly distinguishes its prior exact ROT026 source alias boxes and locally lifts both fold ranks. M15 ROT021 independently I1 confirmed the sixth-source mechanism on two DIFFERENT exact M15 original source pairs. Geeky ROT028 FIRST computed the conditional profiled alpha Fisher under *independent equal log-shell errors and independent sixth log error*, now independently I1 reviewed with separate original unchanged source iv67 Cauchy–Binet by M15 ROT022.

**Crucial additional M15 ROT022 falsifier and firstness, not attributed to ROT030**: if the sixth channel has a completely UNRESTRICTED FIXED, unknown, freely fitted independent log calibration offset, its new nuisance score exactly absorbs the sixth row: efficient alpha information is EXACTLY ZERO at both old folds and even known exact six-output source alias pairs return. M15 also proved bounded deterministic calibration/error overlap thresholds for its own source pairs. This countermodel is logically distinct from a finite-variance random calibration error with known distribution.
M15 source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/8ffad5472f32d9c1f58f6ce5af1ea70fd105f59b/research/m15/2026-11-16/IW_M15_ROT022_ORIGINAL_M13_SIXTH_CHANNEL_CALIBRATION_NUISANCE_EXACT_ALIAS_AND_CAUCHY_BINET_FISHER_REFEREE_001_20261116.md

Geeky ROT029 FIRST source-certified a DIFFERENT Gaussian RAW SITE ENERGY noise model, where all six old/global measurements are computed from the SAME noisy 41³ grid. This forces old/full observation correlations; the exact equivalent additional information comes from 18,268 previously omitted OUTER sites. ROT029's 57-digit original-source proof of outer energies, old five-score nuisance rank, outer score delta and weighted old noise propagation is a HASH-LOCKED mathematical input, not silently newly reconstructed here. Prior public source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/2ea3e12890c872f9f6a1e107eb9840dfcb96285d/research/geeky-s12/2026-11-16/IW_GEEKY_S12_ROT029_ORIGINAL_M13_SHARED_SITE_NOISE_CORRELATED_SIX_CHANNEL_OUTER_SHELL_FISHER_GATE_001_20261116.md

**NEW ROT030 target**: quantify how finite stochastic calibration uncertainty attenuates the correlated-site six-channel gain, while ALLOWING site measurement variances to be different at every point, constrained by positive known bounds. No physical sensor or observed error covariance is claimed. No general theorem novelty in familiar Gaussian GLS/Loewner information inequalities.

## 1. Explicit Gaussian RAW ENERGY observer; not a fixed freely fitted calibration nuisance

Original N41 grid M=41³=68921 sites. Original five fixed disjoint interior source shells counts w=(7778,6938,6146,5402,24389), total 50653; outer complementary region has w0=18268 sites. Let source positive shell means S_i(alpha,t), full original Parseval mean G(alpha), and outer mean O(alpha,t). Original mathematical identity:
  M G = Σ_i w_i S_i + w0 O.
The input relative rigid translation t of all C1,C2,h fields against FIXED original observation windows and single common positive gain exp(b) are HYPOTHETICAL source extensions; original source() and calc() do not expose free t or b.

Six observable RAW ENERGY means (not log-Gaussian claims) are sample means from the SAME original site energy field plus errors. Every site x has an independent additive centered Gaussian energy-density error ξ_x with FIXED parameter-independent variance η² h_x. Each site variance multiplier is strictly positive, possibly different: rho_min≤h_x≤rho_max. Here η>0 is the fixed per-site error std scale.

In addition, the **SIXTH RAW FULL-DOMAIN MEAN ONLY** has a separate independent centered Gaussian calibration error C with FIXED variance (κ η)², for known finite κ≥0. This is a *random* error of a specified probability law, not an unknown fixed deterministic calibration value adjusted independently per source configuration. A deterministic free offset would produce M15's exact zero-information countermodel instead.

Because the site and calibration errors are Gaussian, the six RAW ENERGY MEANS have an EXACT parameter-independent covariance, including nonzero old/full shared-site correlations. An invertible linear transformation replaces the raw full global sample mean by the raw OUTER complement sample mean. The old five raw shell errors become independent of the transformed outer measurement error. The outer measurement variance is:
 Var(eOuter) = η²[ hbar_outer/w0 + (M/w0)² κ² ],
where hbar_outer is the average site variance multiplier on the previously unobserved 18268 points. Old shell i raw mean variance is η²*hbar_i/w_i. This is an exact Gaussian RAW ENERGY covariance statement, not a delta-method assertion that logs of noisy energy are Gaussian.

At the NOMINAL b=0 source fold define ε=η/G, merely a dimensionless local noise scale; η stays fixed in the measurement law. Using log-source mean scores as an invertible local coordinate of the RAW Gaussian Fisher geometry, the old source nuisance score X (5×4, full rank at the two old folds), alpha score a∈range(X), outer nuisance row xO and outer target residual δO=aO−xOβ are defined as in original ROT029. Put
 W(h)=diag( w_i*(S_i/G)^2/hbar_i ),
 Q_site(h)=(G/O)^2 * hbar_outer/w0 + xO*(XᵀW(h)X)^(-1)*xOᵀ,
 K=M G/(w0 O).

Then **the exact local nuisance-profiled Gaussian mean information at either actual old fold** is:

  ε² Ialpha(κ,h) = δO² / [Q_site(h) + K² κ²].

The SOURCE fold rank and δO≠0 imply Ialpha>0 for every finite positive upper variance, provided the observer's calibration error really has the stated independent KNOWN stochastic distribution. The formula is not a proof of practical resolvability.

For homogeneous site noise h_x=1,
 Q0=qO+(G/O)^2/w0,
 ε² Ialpha(κ,1)=δO²/(Q0+K²κ²),
 and its ratio to zero-additional-calibration information is
  Ialpha(κ,1)/Ialpha(0,1)=Q0/(Q0+K²κ²).
The exact 50%-information threshold is:
  κ50 = sqrt(Q0)/K.
As κ→∞, Ialpha→0, consistent with the M15 freely fitted calibration falsifier but NOT equivalent to it for finite κ.

## 2. Uniform heterogeneous-noise robustness without a new 41³-site error dataset

For ANY independent per-site variances η²h_x with bounds 0<rho_min≤h_x≤rho_max<∞, the six independent RAW region-mean error covariance in the OLD+OUTER representation lies between rho_min and rho_max times the homogeneous six-region covariance, in positive-semidefinite Loewner order. Adding the same positive κ² calibration covariance to both sides preserves order. Gaussian nuisance-projected Fisher information is monotone in the inverse covariance, hence:

 δO²/[rho_max Q0 + K²κ²]
 ≤ ε² Ialpha(κ,h) ≤
 δO²/[rho_min Q0 + K²κ²].

This is an exact mathematically valid uncertainty-set envelope at each actual old fold, with no assumption of equal variances across the source grid beyond the specified numerical upper/lower bounds. For the bounded example rho_min=1/2, rho_max=2, the original source certified whole-fold intervals below supply strict positive robust information for ANY possible independent heterogeneous site variance pattern in those bounds. Cross-site error CORRELATIONS are not included; unrestricted spatial correlations can invalidate this envelope.

The κ at half of EACH heterogeneous pattern's own κ=0 information is sqrt(Q_site(h))/K, and thus lies between sqrt(rho_min)*κ50 and sqrt(rho_max)*κ50. These are a robust interval for the threshold, not one single exact threshold when variance pattern is unknown.

## 3. ACTUAL source M13 interval proof and strict quantitative data

The NEW executable original-source program first Git-blob locks original unchanged M13 public Python and original B25 source data and SHA256 locks the COMPLETE previous originally executed original-source M13 ROT029 57-digit JSON SHA256 d7595642433b0ecd4cc3771b5878e465fb635cb74652182f3b9e907d4e98aa42, BEFORE original M13 import. It ACTUALLY EXECUTES original M13 tensor_polys(41)[B] and native quartic(U,V,T,N41,k0) at outward mpmath.iv.dps65, verifying global energy overlaps with prior original-source directed G enclosures across EACH complete exact old fold bracket. NEW interval arithmetic then composes the earlier strict original source 57-digit interval bounds for G,O,δO,qO,outer noise into original M13 source 65-digit calibration K, κ50 and κ-grid information/Loewner bounds.

**IMPORTANT EXECUTION HONESTY:** The old entire-window twenty derivative scores and old weighted Gram determinant are the cryptographically source-locked original ROT029 iv57 SOURCE CERTIFICATE, reused as a rigorous proven input. They were NOT claimed freshly independently recalculated in ROT030. The native k0 tensor and global energy source function ARE freshly executed. This is a valid interval-composition certificate, not a new independent 57-digit source proof.

R1 original root α in (0.01861522133766,0.01861522134166):
- original source whole-interval K=M G/(w0O) strictly in (5.246183477390408,5.246183503845360).
- K² calibration variance coefficient in (27.52244107844411,27.52244135601918).
- **κ50 strictly in (0.0145505103665393,0.0145535306193543)**.
- Original homogeneous ε²I at κ=0 in (21.949503893709,22.058942132462).
- With κ=0.01 new homogeneous ε²I in **(14.9100124808765,14.9823575775729)**.
- With ANY heterogeneous independent site h_x∈[0.5,2] and κ=0.01, robust whole-interval ε²I lies within **(8.8787756648348,22.6867330979135)**.
- Pattern-dependent κ50 must lie within approx (0.01028876455,0.02058180039).

R2 original root α in (0.05416739905600,0.05416739906000):
- K strictly in (4.760334203583090,4.760334225198555).
- K² in (22.66078172980305,22.66078193559673).
- **κ50 strictly in (0.0370695278542513,0.0370736983766235)**.
- Homogeneous ε²I κ=0 in (504.588924345513,504.813001312706).
- With κ=.01 new homogeneous ε²I in **(470.366956117101,470.568654883892)**.
- With any heterogeneous h_x∈[0.5,2] and κ=.01, uniform source ε²I within **(243.438663421552,881.350290431533)**.
- Pattern κ50 bounds roughly (0.02621211452,0.05243012706).

ALL new strict endpoints, 2×7 calibration levels and all arbitrary-variance Loewner bounds are in FULL 27361-byte actual ROT030 source result JSON SHA256 791ac46d6cbf53d468123c5dbfb710576152db983ed6930e75086555c9de8b6e. Human-display rounded numbers are NOT proof endpoints. The source theorem applies at each exact old fold contained in its prior rational bracket; not every alpha in [0,.2] or to physical observations.

## 4. Independently programmed SPATIAL correlated GLS crosscheck, 28 scenarios

A separate newly authored program imports the original public M13 Fourier source but DOES NOT use original M13 inner/window_mode to calculate the observations. Instead it constructs original Fourier B and FOUR derivative complex tensor fields on N41³ periodic spectral grids and directly inverse FFTs into real-space energy density and gradients. It calculates the exact old five shell means, unmasked mean and outer mean with original site masks.

It then directly implements two DIFFERENT numerical Fisher algorithms:
(1) OLD FIVE plus independent OUTER shell under region-mean site errors, including FULL Gaussian raw-energy calibration covariance;
(2) OLD FIVE plus FULL global mean with the CORRECT NONDIAGONAL six-by-six shared-site covariance plus independent global calibration variance, whitened with Cholesky and nuisance-projected directly.

A deterministic genuinely HETEROGENEOUS variance pattern on the original grid, h(x,y,z)=1+0.5cos(2πx/41)cos(2πy/41), lies between 0.5 and 1.5 (well inside source-certified 0.5..2 arbitrary-pattern bounds). All 28 cases = TWO source folds × TWO noise patterns (homogeneous and this heterogeneous example) × SEVEN calibration κ∈{0,.002,.005,.01,.02,.04,.10}.

**28/28 comparisons agree** within relative tolerance 4×10^-9; all homoskedastic results lie STRICTLY in the original new source iv65 intervals and all heterogeneous values are inside the uniform new Loewner bounds. Example at κ=.01 homogeneous:
 R1 direct correlated GLS ε²I≈14.94616092648;
 R2 direct correlated GLS ε²I≈470.46779895158.
For κ=0 original same-source baseline:
 R1≈22.00418398287;
 R2≈504.70095497814.

**NEGATIVE CONTROL, incorrect independent OLD/GLOBAL errors:** If an analyst incorrectly discards original geometric cross-covariance and uses only the diagonal of the correct old/full 6×6 covariance, local ε²I at zero additional calibration becomes ≈19.29147 instead of ≈22.00418 (R1, ~12.33% undercount) and ≈492.54368 instead of ≈504.70095 (R2, ~2.41% undercount). The incorrect diagonal result is NOT the correct model and cannot be promoted as information. Independent 3D FFT is a same-cell DOUBLE-PRECISION DIAGNOSTIC, not a different-cell I1 review of the new source theorem.

## 5. Full actually run reproducibility, negative source checks

Complete full executable user ZIP:
 Geeky_S12_ROT030_calibration_heterogeneous_site_noise_Fisher.zip
 bytes 45230, SHA256
 62370bf945ebaa59bbf97c9a502423cd92aebb8d9aae86556ab9595bb6a254a7.
14 entries, 13 SHA256 manifest payloads, ZIP CRC PASS, all 14/14 archive members verified exact bytes, all 13/13 SHA256 checks PASS. Includes original immutable M13 helper and original B25 data; original author ROT029 SOURCE theorem code and full original 57-digit JSON; previous original independent spatial code and full output; new source-based calibration/heterogeneity program, new complete original interval result, separately authored new 3D FFT/GLS calibration program and full result; clean replay/tamper program and actual receipt; README and manifest.

Actual new source-composition Python SHA256 253e63320c9798797058635a2cdf78caa52cb068d842ec71df62c374630bc854; full new 65-digit source interval JSON SHA256 791ac46d6cbf53d468123c5dbfb710576152db983ed6930e75086555c9de8b6e. New separate spatial source FFT Python SHA256 e810505dd529768a652b49abf1d94cc0433658b0084b3d1aedee2ed0a037b641; full 28-case spatial result JSON SHA256 667dbfa86a6c3601e75e096cf24f7ca28e055d8558fd375addceabd250a9c94f.

Actually executed clean replay controller Python SHA256 5e4f279fcb000f1fc04b31da9f50dabf862804d1279acc3e7ae468a7b43cab22; full control receipt JSON SHA256 4936018e67f086902a004a91615b40f595cd776435b8a0fc609b43b7ae8e336d. Both programs were copied into SEPARATE temporary directories and ACTUALLY RUN by independent fresh Python -I subprocesses; both COMPLETE JSON outputs were byte-identical. SIX deliberate 1-byte corruptions of temporary copies of original M13 Python, original B25 data, prior ROT029 original source JSON and new ROT030 source JSON, as applicable to the two separate programs, each failed closed with SOURCE_IDENTITY_MISMATCH BEFORE scientific source import. Untouched originals preserved; SIX of SIX PASS. No timeout hidden or falsely counted PASS.

Full executable actual Python source, original full interval endpoints, verification receipts and integrity manifest are in user ZIP, not falsely claimed separately byte-mirrored in public GitHub. GitHub public text and curated machine JSON are separate provenance events only.

## 6. Interpretation and next bounded referee

The contrast between the M15 ROT022 unrestricted FIXED unknown calibration c and this ROT030 independent RANDOM raw-full-mean additive Gaussian C with known finite variance is ESSENTIAL. They cannot be conflated. Under the latter model and bounded independent per-site variance, the source old folds remain locally alpha identifiable; the amount of information has a finite, quantifiable calibration-noise budget. Under completely free unknown offset c, information is exactly ZERO, as M15 already FIRST established. If calibration error has unknown distribution, depends on parameters, is correlated with source/site errors or introduces a new freely fitted deterministic mean, new derivation is required.

No real field translation/gain knob, sixth physical sensor or noise/covariance distribution has been authenticated in historical DTC0a. Original full historical dtc0a_runtime_v0_3_1.py producer byte identity remains MISSING. Classical Fourier covariance, Gaussian mean Fisher/GLS and Loewner ordering are mature, NO general novelty; source-specific numerical gates are author same-cell pending independent REC12/AUD2/M15 I1.

Original source M13 FIRST; source sixth mechanism Geeky ROT027 FIRST with independent M15 ROT021 I1; original independent-log Fisher Geeky ROT028 FIRST with M15 ROT022 I1; M15 ROT022 FIRST free-calibration countermodel; correlated site noise Geeky ROT029 FIRST author; NEW calibration-vs-site heterogeneity combination Geeky ROT030 FIRST within chain, author only. KN14 BW native scientific ingest, owner M15 CANON and EXEC_SIGN remain UNVERIFIED/PENDING; GitHub publish and Slack dispatch do not constitute acceptance. No task cascade.

Recommended bounded different-cell audit: independently reconstruct the ORIGINAL M13 source and original site-partition covariance; independently check the Gaussian global raw-mean calibration offset transforms to K² κ² in the outer basis, and prove the Loewner sandwich for arbitrary independent bounded heterogeneous site variances. Reproduce both source whole-bracket κ50 enclosures without using this new source program. Do NOT treat a free unknown deterministic calibration offset as a finite-variance random error.

FINAL:
 M15_ROT022_PRIOR_ROT028_DIFFERENT_CELL_I1_PASS_AND_UNRESTRICTED_CALIBRATION_FALSIFIER_FIRST /
 ORIGINAL_M13_SOURCE_NATIVE_K0_IV65_CHECK_PASS /
 PRIOR_ORIGINAL_M13_IV57_SOURCE_SCORE_CERT_SHA_LOCKED_REUSED_NOT_CLAIMED_INDEPENDENT_RECALC /
 TWO_WHOLE_FOLD_BRACKETS_STRICT_NEW_CALIBRATION_INFORMATION_AND_HALFTOLERANCE_CERT_PASS /
 ALL_BOUNDED_HETEROGENEOUS_SITE_VARIANCE_LOEWNER_INFORMATION_BOUNDS_PASS /
 28_OF_28_INDEPENDENT_SPATIAL_FFT_CORRELATED_GLS_CHECKS_PASS /
 INCORRECT_DIAGONAL_COVARIANCE_NEGATIVE_CONTROL_PASS /
 TWO_CLEAN_BYTE_REPLAYS_SIX_SOURCE_TAMPERS_PASS /
 USER_ZIP_CRC_14OF14_BYTE_13OF13_SHA_PASS /
 ROT030_EXTERNAL_I1_PENDING / BW_PENDING /
 NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
