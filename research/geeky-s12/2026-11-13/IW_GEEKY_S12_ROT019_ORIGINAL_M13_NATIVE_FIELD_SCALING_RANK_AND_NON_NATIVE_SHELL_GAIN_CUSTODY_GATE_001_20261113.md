---
artifact_id: IW_GEEKY_S12_ROT019_ORIGINAL_M13_NATIVE_FIELD_SCALING_RANK_AND_NON_NATIVE_SHELL_GAIN_CUSTODY_GATE_001_20261113
date: 2026-11-13
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
exposure: PUBLIC
science_status: ACTUAL_ORIGINAL_M13_NATIVE_OPERATOR_FULL_N41_25_COEFFICIENT_HOMOGENEITY_REPLAY_PASS / FIVE_RELATIVE_GAINS_NOT_NATIVE_SOURCE_KNOBS / AUTHOR_ONLY
source_first: M13_PUBLIC_SOURCE_ROT33 / N41_B_25_DIRECTED_SOURCE_QUARTICS
review: M15_ROT009_I1_PASS_FOR_PRIOR_ROT017 / REC11_ROT032_I1_PASS_FOR_PRIOR_ROT016_AND_INDEPENDENT_NEAR_CRITICAL_CONTINUOUS_TUBE / ROT019_NOT_INDEPENDENTLY_REFEREED
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_HISTORIC_DTC0A_RUNTIME_IDENTITY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT019 — source-native three field amplitudes collapse to one shell gain; independent five-gain nuisance not supplied by original M13 operator

## 0. Science-first and reviewer-currentness

The previous Geeky ROT015-018 explored an extended N41 B auxiliary model with a FREE common positive gain c and FIVE independent bounded relative shell gains eta_i. That was explicitly a coefficient/nuisance STRESS MODEL, not a claim that the historical producer exposes five independently adjustable instrument or field-calibration gains.

New independent different-cell science status on pre-existing results:
- M15 ROT009, public original independently authored exact JS BigInt, I1 nonblind PASS for ALL FOUR Geeky ROT017 active-set configurations at kappa=1%,4%,6%,6.6% over ALL 25 original M13 B coefficients independently widened eps=1e-7. Its alternative wedge source risk enclosures are tighter than the original author's generic intervals for the first three cases. M15 report: https://github.com/wmakiela-tech/Nash-iw-research/blob/7ce1f923dd98e080af245f7ded9550abd7bff30d/research/m15/2026-11-13/IW_M15_ROT009_INDEPENDENT_FOUR_M13_B25_SOURCE_ACTIVE_SET_RISK_REFEREE_001_20261113.md
- REC11 ROT032, public original two separate Python Fraction approaches, I1 nonblind PASS for Geeky ROT016 fixed kappa=.066 two-extreme global risk. REC11 independently also derived the continuous near-zero-fit law for every k in [.066,kcrit) and the zero-fit plateau above kcrit, convergent with the ROT018 source claim. Independent REC11 FIRST for its derivation; Geeky ROT018 FIRST for its own proof; no independent reviewer of the generic reentry synthetic counterexample is asserted. REC11 report: https://github.com/wmakiela-tech/Nash-iw-research/blob/ca01ac31aea16176de56513b9c167b50e98f9b92/research/rec11/2026-11-13/IW_REC11_ROT032_GEEKY_S12_ROT016_INDEPENDENT_EXACT_TWO_ACTIVE_GAIN_REFEREE_001_20261113.md

ROT019 intentionally stops optimizing arbitrary kappa/delta/epsilon thresholds. It asks whether the EXTENDED relative shell gains themselves represent parameters actually present in the original auxiliary M13 source operator.

## 1. Exact native source and mathematical homogeneity

Original public M13 source from the ROT011 byte-exact verified original 8970B UTF8 code, Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-24/verify_m13_rot33_interval.py

Original M13 25 directed coefficients B for five nested masks N41, 7501 bytes, Git blob SHA1 a6f50fbe5904e580e84c87ee87c5ad043cdec5d0:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json

Read original functions source(), bracket(), lie(), proj(), em(), calc(), tensor_polys(), quartic(). In the frozen code source() hardcodes trigonometric C1,C2,h, and calc(N,alpha) exposes alpha (plus integer grid size N) to act through E_lin; it has NO 5-dimensional free shell gain vector and NO native five per-mask/per-shell relative gain controls.

As a HYPOTHETICAL controlled extension, introduce any positive scalar amplitudes lambda1, lambda2, mu multiplying whole source fields C1, C2, h respectively, leaving their shapes, N, alpha and tensor operations intact. The original B expression is exactly multilinear with one C1, one C2 and one h in every term. Bilinearity of bracket, linearity of lie in each argument, linear E_alpha, TT projection, sum and source derivative imply the EXACT OPERATOR IDENTITY for all alpha:

 B_alpha(lambda1*C1, lambda2*C2, mu*h) = (lambda1*lambda2*mu)*B_alpha(C1,C2,h).

It follows from the squared Fourier B norm and every nested mask average that for k=2,..,6:

 g_k(alpha;rescaled inputs) = (lambda1*lambda2*mu)^2 * g_k(alpha;original).
 s_i(alpha;rescaled inputs) = (lambda1*lambda2*mu)^2 * s_i(alpha;original) for i=1,..,5.

All 25 polynomial coefficients of all five source quartics scale by this ONE COMMON POSITIVE scalar, as do all five disjoint shell energies. Thus three independently selectable source FIELD SCALAR AMPLITUDES offer only ONE identifiable shell-gain dimension. Their separate changes cannot generate independent relative shell factors. No conclusion about general non-scalar SHAPE perturbations is implied.

Analytic differential statement for shell energy vector s=(s1,...,s5):
  partial_(log lambda1) s = partial_(log lambda2) s = partial_(log mu) s = 2s.
Hence the 5 x 3 amplitude Jacobian has rank EXACTLY ONE at positive shells. After quotienting by common gain, native field-scalar perturbations have rank ZERO. In contrast independently allowed relative shell gain eta_i modulo common c spans FOUR projective tangent degrees and can, if unconstrained, absorb source alpha shape changes. They do NOT come from three independent amplitudes of whole C1,C2,h.

## 2. Actual ORIGINAL unmodified M13 source native simulation and bounds

A new standalone Python3 (mpmath 1.3.0, iv.dps=45) directly imported the UNMODIFIED original M13 module only AFTER full 8970B Git blob hash verification, alongside a separate pre-verified original 7501B source table. Source field reweighting applied ONLY as an IN-MEMORY source() return patch; original on-disk source file was never modified.

Exact dyadic scaling fixture:
  lambda_C1 = 2; lambda_C2 = 1/2; mu_h = 2.
Consequently exact B operator factor = 2 and exact squared norm / shell-energy / quartic coefficient factor = 4.

ACTUALLY RUN original M13 calc at N41 and alpha=1/20 (.05), and then native original tensor_polys(41) using alpha=0,+1,-1 to generate quartic B coefficient enclosures from scratch in TWO independent source() states (baseline and dyadic rescaled).

Actual source-matched results:
- 41 B complex Fourier modes, each a 3x3 tensor = 369 complex components, 738 real/imag interval differences; every directed difference of rescaled tensor minus twice original contained zero, no Float64 decisions.
- all FIVE mask B squared-energy source outputs at alpha=.05 had ratio exactly 4 at float readout and interval difference from 4 times original contained zero.
- all 25 original B quartic polynomial coefficients over masks k=2..6 had ratio exactly 4 at float midpoint readout and independent directed intervals difference from four times original contained zero.
- exact operator multilinearity is the PROOF; interval zero inclusion alone is ONLY a native-code replay consistency control, not a proof of a universal symbolic identity.

A second data surface, the RETAINED user historical N31 amplitude-scaling CSV, was independently parsed and verified: 14/14 recorded C_scale, h_scale, and combined_scale K_B RMS ratios equal C_scale^2 * h_scale to numerical reporting precision. Historical original CSV SHA256 0b15581b8a49d7507bf0dc72899efd7a4a8932736f7801838824eacb012a0e11. This is supplementary historical functional corroboration ONLY: it does not prove that the missing original historical dtc0a_runtime_v0_3_1.py has been recovered or has the exact same bytes/field implementation.

## 3. Exact native alpha shape rank versus mathematical shell-gain rank

The source-locked original 25 quartic interval MIDPOINTS were converted from decimal text to EXACT fractions.Fraction inputs. Four differences of nested mask occupancies produce the disjoint five-shell quartics with weights (7778,6938,6146,5402,24389). At alpha=1/20, all five shell energies are positive. The exact Fraction minor

 H(alpha)=s4'(alpha)*s5(alpha)-s4(alpha)*s5'(alpha)>0

is STRICTLY POSITIVE at alpha=1/20, displayed after multiplication by 10^24 as +0.016527459284881606. Therefore s(alpha) and s'(alpha) are linearly independent: varying source-native alpha genuinely changes projective shell SHAPE and cannot be hidden by an overall scalar amplitude in this fixed source family. Source-native amplitude (one ray) plus source alpha derivative span rank TWO at the fixed point. The M15 independent stronger full-domain log(s4/s5) monotonicity source theorem ROT007 supports global projective injectivity on [0,.2], but we do not claim to have re-proved that full nine-Bernstein result in ROT019.

At alpha=.05 beta=.075, exact source quartic midpoint shell ratios s_i(alpha)/s_i(beta), human display:
 [0.5324476894350468,0.5367749896668135,0.5477284929053287,0.5688466880904144,0.6080264513647456].
They are unequal; common field amplitudes cannot give the five independent ratios needed to perfectly impersonate an alpha difference. The exact sharp free-common-gain relative nuisance threshold is about 6.626959720164886%, as FIRST derived by Geeky ROT015 and independently reviewed M15 ROT007. Here the numerical value is merely a sanity check, not a new kappa threshold discovery.

A simple exact nonnative relative gain perturbation eta=(0,0,0,0,1/100) changes s5 alone; it changes the s4/s5 ratio and cannot be produced by the scalar-amplitude class because any member multiplies all five s_i by the SAME factor. This is a **structural non-realizability proof for scalar field amplitudes**. It is NOT proof that no more general field-shape perturbation could yield comparable shell distortions; to make a physical gain claim, one must specify an independently sourced producer-legal SHAPE or calibration mechanism and independently verify its differential image.

## 4. Reproduction, isolation and negative tests

Actual new source code in the LOCAL user ZIP:
  Geeky_S12_ROT019_native_multilinearity_vs_free_shell_gain.zip
  ZIP size 16149 bytes; SHA256 8fca3009e51295bd237aaed23a6fa9a70f9150b169a286a48172f15620f509f7.
Contains 8 files; ZIP CRC and exact 8/8 SHA256/byte readback PASS.

- Actual executed author Python module source SHA256 a182b90aae66a2c4e336b110b4bd385609ca46a85ec574499cdb9aba7f13d70f.
- Original byte-exact M13 public ROT33 operator source SHA256 cd4aad089bf68e2e6155ff048d4d812943495dcf1770c8acbf0ff8111b1deb9c.
- Original M13 source B JSON SHA256 0295116e364e28e67f0129bda1fc298d6e4bfdcb7aa8a6314f02a9ea37edca5f.
- Original user historical N31 amplitude CSV SHA256 0b15581b8a49d7507bf0dc72899efd7a4a8932736f7801838824eacb012a0e11.
- Full executed result JSON SHA256 2610ee73f233b48adc69d64c2a518a2b10c99319a5b787078b3c411eca626dca.
- Two fail-closed test records, README, full member SHA manifest.

Independent CLEAN folder extraction and rerun produced the SAME full output JSON BYTE-FOR-BYTE (SHA256 above). Two negative controls: corrupt EXACTLY one byte in temporary copy of original M13 module or original M13 B table; ORIGINAL SOURCE GIT BLOB MISMATCH raised BEFORE source import, nonzero exit code in BOTH cases, original files untouched. No independent external reviewer of ROT019 exists yet. No public GitHub mirror of the local full original executed Python source is claimed; this report and public machine summary are new public outputs.

## 5. Scientific impact, no overclaim and next gate

The native-shape versus arbitrary-gain distinction prevents an unsupported claim migration:
- Original M13 source producer has a fixed field triple, finite N, scalar alpha and five evaluation masks; it DOES NOT provide five scalar gains.
- Hypothetical independent positive WHOLE-FIELD scalar amplitudes offer only one common scaling of source B, all 25 quartic coefficients and all five shells; they do not instantiate independent shell eta.
- The earlier Geeky ROT013 box of 25 independent coefficients and ROT015-018 shell gains are legitimate, source-typed mathematical adversarial/tolerance families. But they are not source-native or guaranteed physically achievable in the frozen M13 producer by changing scalar field amplitudes alone.
- New field-shape classes, imperfect masking, independent shell channel calibration or altered operators may have their own projective tangent directions; absent an actual sourced mechanism they remain unverified. Historical custom-Gaussian class controls in user attachments are NOT proof of a five-gain calibration mechanism.
- Native historical dtc0a_runtime_v0_3_1.py byte identity still MISSING. No empirical validation, K/J3/TPE observable transfer, physics novelty, instrument tolerance or BW owner approval follows.
- M15/REC11 review upgraded ORIGINAL ROT016/017 mathematical source evidence to bounded I1; ROT018 generic reentry and new ROT019 field-scaling custody theorem remain AUTHOR_ONLY pending external independent review. No task cascade, no new threshold microgrid.

FINAL:
ORIGINAL_M13_PUBLIC_CODE_UNMODIFIED_NATIVE_B_N41_REPLAY_PASS /
369_COMPLEX_COMPONENTS_AND_5_MASK_ENERGIES_AND_25_QUARTIC_COEFF_SCALAR_HOMOGENEITY_PASS /
14_HISTORIC_N31_AMPLITUDE_ROWS_FUNCTIONALLY_CORROBORATE_PASS /
EXACT_NATIVE_FIELD_SCALAR_JACOBIAN_RANK_1_AND_ALPHA_PLUS_GAIN_RANK_2_AT_0P05_PASS /
FIVE_INDEPENDENT_SHELL_GAINS_NOT_NATIVE_SOURCE_SCALAR_PARAMETERS_PASS /
M15_ROT009_I1_REVIEW_ROT017_PASS / REC11_ROT032_I1_ROT016_AND_NEAR_CRITICAL_PASS /
ROT019_REFEREE_PENDING / BW_PENDING /
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
