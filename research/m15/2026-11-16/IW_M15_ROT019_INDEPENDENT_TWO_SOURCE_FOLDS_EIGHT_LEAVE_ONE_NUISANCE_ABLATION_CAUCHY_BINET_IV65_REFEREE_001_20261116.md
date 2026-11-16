---
artifact_id: IW_M15_ROT019_SOURCE_TWO_FOLDS_LEAVE_ONE_NUISANCE_ABLATION_INFORMATION_POSITIVITY_001_20261116
return_id: IW_M15_ROT019_TWO_SOURCE_FOLDS_FOUR_NUISANCE_CODIMENSION_ONE_IDENTIFIABILITY_RESTORATION_8_OF_8_EXACT_IV65_001_20261116
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-16
exposure: PUBLIC
result_class: DIFFERENT_CELL_INTERNAL_NONBLIND_I1_ORIGINAL_SOURCE_FORMULA_IV65_FISHER_STRUCTURAL_ABLATION_AND_NUMERIC_SVD_CONTROL
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: ORIGINAL_M13_AUXILIARY_FORMULAE_REIMPLEMENTED / TWO_LOCAL_SOURCE_BRACKETS_ONLY / HYPOTHETICAL_COMMON_GAIN_AND_SOURCE_FIELD_TRANSLATIONS_VS_FIVE_FIXED_MASKS / NO_ORIGINAL_M13_MODULE_BYTE_EXECUTION / NO_HISTORIC_DTC0A_PRODUCER / NO_PHYSICAL_NUISANCE_OR_SENSOR_NOISE / NO_MATH_NOVELTY / NO_EXTERNAL_BLIND_I3 / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE / NO_TASK_CASCADE
---

# M15 ROT019 — source-conditional proof: pinning ANY ONE nuisance restores local alpha information at BOTH nonlinear folds

## 0. Main new result and strict owner firstness

**NEW CONDITIONAL STRUCTURAL RESULT WITH EIGHT STRICT OUTWARD INTERVAL CERTIFICATES: PASS.**

Original Geeky-S12 ROT023 FIRST showed two interior alpha values of loss of first-order information when the source M13 N41 five-shell observation model is expanded by ONE unknown common gain and THREE independent common Fourier field shifts versus FIXED masks; Geeky-S12 ROT024 FIRST established these are nonlinear Whitney folds. M15 ROT015, ROT016, ROT017 independently reviewed the original source first-order singularities, alpha0 boundary and fold Hessians, and M15 ROT018 FIRST delivered two exact source-conditional explicit alpha inverse pairs with two rigorous Krawczyk second-solution boxes. Geeky-S12 ROT025 additionally FIRST produced independent original-owner explicit near-fold numerical source-coordinate pairs, with native original operator diagnostics. None of that firstness is reassigned.

**Different question, answered NOW:** at EACH of the TWO original source singular root intervals, pin exactly one of the four nuisance coordinates b,tx,ty,tz to a KNOWN common value in an inverse problem, while retaining the other THREE nuisance coordinates free. Is the remaining alpha target still singular? The answer is rigorously **NO for all four omissions in each root bracket**: every reduced source score matrix has a strictly positive efficient alpha-information lower interval throughout the entire short alpha bracket, and a full 4-column rank. The original 5x5 full nuisance Jacobian has a right kernel whose normalized alpha component equals 1 and ALL FOUR nuisance components are provably NONZERO throughout both brackets. Thus the full four-dimensional nuisance freedom is necessary for these two specific local fold tangencies; restricting even one such coordinate removes their first-order alpha degeneracy.

This is NOT global injectivity, not uniqueness of a full nonlinear inverse for all source points or a physical sensor calibration claim. It does NOT say that three different unknown nuisance parameters suffice at other alpha values or globally. It applies only to these two source-conditional local original roots and their entire short predeclared root neighborhoods. The method is standard Cauchy–Binet and interval linear algebra; **NO_NOVELTY**.

## 1. Original source and precise hypothetical model

Original M13 source B Fourier Lie/bracket/TT mathematical operator firstness:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py
Original Git blob c6377cfbc9a0070abc34ffedc5871e719f6a4679.
Original source 25 directed quartic B coefficients firstness:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-26/direct_B.json
Original Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0.
BOTH original source blobs were DIRECTLY fetched and verified as matching the immutable Git blobs in this ROT019.

First original owner fold source:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/1929d33c8577e05ef33c7145f2f828c9a75c2e15/research/geeky-s12/2026-11-15/IW_GEEKY_S12_ROT024_TWO_RIGOROUS_SOURCE_LOCAL_NONLINEAR_FOLD_ALIASES_AFTER_NUISANCE_PROFILING_001_20261115.md
Earlier independent full-root second-order review M15 ROT017:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/5c6f4874311c053664249018b89f9a6b7fee1ca8/research/m15/2026-11-15/IW_M15_ROT017_INDEPENDENT_TWO_M13_NONLINEAR_SOURCE_WHITNEY_FOLDS_IV55_SECOND_ORDER_REFEREE_001_20261115.md
Previous explicit exactly certified source pairs M15 ROT018:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/9e15aa9231797ecd0be3930f4a5e5619a8891afe/research/m15/2026-11-15/IW_M15_ROT018_TWO_CONSTRUCTIVE_EXACT_LOCAL_ALPHA_ALIASES_INTERVAL_KRAWCZYK_SOURCE_REFEREE_001_20261115.md

Original native M13 program does NOT expose translation or amplitude settings used below as freely adjustable nuisance parameters. The source B tensor is reimplemented using the previous independently written M15 ROT012 public-formula Python, SHA256 4e2e316e58dec6831e4f633e13081ff53737e69da6020fb158ab88574a263c9e, not the original author M13 native Python or historical dtc0a_runtime_v0_3_1.py. This dependency is SHA-locked BEFORE any original source formula computation. No Geeky ROT023/024/025 scientific certifier or source array is imported.

Frozen N=41, alpha in (0,1/5), 41 sparse source Fourier B tensor modes with exact polynomial B_m(alpha)=U_m+alpha V_m+alpha² W_m, Fourier-difference window kernels from 1681 mode pairs grouped into 221 distinct integer q. Five original fixed spatial cubic mask energies k=2,3,4,5,6 yield positive disjoint shell energies s_i. A mathematical common input translation t=(tx,ty,tz) relative to those FIXED masks changes mode phases exp(i m·t). One common unknown positive gain exp(b) multiplies shell energies. Five log-energy source observations:
   F_i(b,t,alpha) = b + log(s_i(alpha,t)), i=1..5.
Target alpha; four hypothetical nuisance coordinates (b,tx,ty,tz). At t=0, the original five-by-four nuisance score matrix is X=[ones, Dtx log s, Dty log s, Dtz log s], with alpha score a=Dalpha log s.

Two frozen source-typed alpha root brackets, first Geeky ROT023, independently verified in M15 ROT015–017:
  FIRST [0.01861522133766,0.01861522134166],
  SECOND [0.05416739905600,0.05416739906000].
For each, actual full J=[X,a] has a singular root in the bracket, while X has rank exactly four through the WHOLE bracket. Outside those roots, full J may be full rank. This audit does not assume J singular at every point of a bracket.

## 2. New precise theorem and independent interval calculation

For each choice j among the four nuisance columns, impose that nuisance coordinate j is pinned to its KNOWN value (it must not be re-estimated separately in the two inverse solutions). Denote the retained five-by-three nuisance matrix N3(j) and augmented five-by-four matrix M4(j)=[N3(j),a]. For any fixed five-observation covariance Sigma=sigma² I (a HYPOTHETICAL iid log-energy Gaussian noise model) and whenever N3(j) has rank 3:
   sigma² * I_eff(alpha | other 3 nuisance)
     = ||(I - P_N3) a||²
     = [sum over ALL 5 choose 4 row sets A of det(M4(j)_A)^2]
       / [sum over ALL 5 choose 3 row sets B of det(N3(j)_B)^2].  (019.1)

This follows directly from the classical Cauchy–Binet formula for the Gram determinant quotient and does not require computing an inverse of an ill-conditioned Gram matrix. The new independently authored verifier computes all 5+10 necessary minors by exhaustive exact 4! and 3! permutation formulas, then evaluates **true directed interval squares with mpmath.iv x**2**, whose lower bound is ZERO whenever a signed minor interval crosses zero. It does not use binary float approximations for positivity decisions or squaring. At iv.dps=65 the verifier builds full 5x5 interval source Jacobian on each ENTIRE real closed alpha bracket, with positive shell values rigorously checked first, and computes all EIGHT source-dependent numerator/denominator quotients. Every numerator and denominator has a STRICTLY positive lower directed endpoint, and each resulting information interval has a STRICTLY positive lower endpoint.

At each actual rank4 singular root, the normalized right-kernel vector v=(v_b,v_tx,v_ty,v_tz,1) is computed from a strictly nonsingular original X 4x4 minor by independent Cramer's rule; all four nuisance coordinate intervals have a constant nonzero sign throughout each root bracket:
  FIRST: v_b negative ~ -15.9004, v_tx positive ~ +19.4556,
         v_ty positive ~ +69.1383, v_tz negative ~ -37.4915.
  SECOND: v_b negative ~ -24.6672, v_tx positive ~ +80.7898,
          v_ty positive ~ +353.648, v_tz negative ~ -124.297.

This supports the structural theorem without the iid assumption: at a singular root, if a were inside the span of the remaining three nuisance columns after omission j, there would be a normalized kernel with v_j=0, contradicting the unique normalized full J kernel whose v_j has strict sign. Hence the four-column reduced augmented Jacobian is rank4 at each fold, and efficient alpha information is strictly positive for **ANY fixed positive-definite Sigma**, although the actual numeric values of its Fisher information depend on Sigma. This proof does NOT infer a physical Sigma from the source.

## 3. Eight exact rational-decimal-directed source results

Each range is an OUTWARD interval for sigma² I_eff using Sigma=sigma² I, at every real alpha in the given Geeky first root bracket, with N41 source formula at t=0. Decimal displays are rounded conservatively, and exact original full directed endpoints are in the local executable machine output. Every original decision uses directed endpoint comparisons prior to human decimal formatting.

| fixed known nuisance | FIRST root bracket, sigma² I_eff | SECOND root bracket, sigma² I_eff |
|---|---|---|
| b, free tx ty tz | [222.568099325286,222.568512163543] | [78.3875268465782,78.3876723704250] |
| tx, free b ty tz | [20.5851175862376,20.5852649935872] | [2.46439302730201,2.46441192520173] |
| ty, free b tx tz | [0.251716776845987,0.251718544706392] | [0.366972473973119,0.366975318682925] |
| tz, free b tx ty | [0.201148645268775,0.201150464500889] | [0.611119825265706,0.611127525130438] |

All displayed outer intervals fully contain the original exact iv65 output intervals. The eight STRICT lower endpoints remain positive even at the interval corners, and all four null-vector nuisance components exclude zero in both whole-root brackets.

**Interpretation:** In this 5-observation auxiliary inverse model, pinning b is the numerically strongest of the four constraints at BOTH folds under the chosen iid log-energy observation metric, and pinning ty/tz leaves relatively weak but still strictly positive local information. These magnitude comparisons are conditional on the specific parameter units and hypothetical covariance: do NOT claim a physical measurement-precision ranking. The structural result of local rank restoration does not depend on these magnitudes.

A single phase coordinate being fixed is enough to break either particular local corank-one alpha fold. It is NOT a claim that only three source-field translation controls exist in real original source, nor that any arbitrary physical or historical signal loses these degeneracies. No proof that the full parameter map is globally injective on any domain follows from a local rank result.

## 4. Independent method cross-check, falsifiers, reproducibility

**Second algorithm, separate diagnostic:** A NEW independent NumPy SVD checker applies standard orthogonal projection (not the Cauchy–Binet minor formula) to the approximate midpoints of all 5x5 score entries published in the directed source output, using the selected remaining 3 nuisance columns. The eight projected residual norms squared independently fall STRICTLY inside the respective original iv65 information intervals:
 FIRST fixed b ~222.568305744, tx ~20.585191290, ty ~0.251717660775, tz ~0.201149554883;
 SECOND fixed b ~78.387599609, tx ~2.464402476, ty ~0.366973896, tz ~0.611123675.
That SVD calculation is numerical-only and is NOT the source of the proof of strict positivity.

**Two meaningful negative controls actually executed:**
  - Change one byte in the ORIGINAL independent M15 source-formula dependency while leaving its expected SHA lock untouched; the verifier rejects with PRE_SCIENCE_ORIGINAL_FORMULA_SHA256_MISMATCH BEFORE original source mathematical computation, fail closed.
  - Replace the native source alpha score column with the nuisance common-gain all-ones score in a deliberately MODIFIED disposable script fixture. In that synthetic false model the efficient alpha information must be ZERO when the gain remains free. The original program now correctly REJECTS the all-positive claim with REDUCED_FISHER_NOT_STRICTLY_POSITIVE_FIRST_1. This is a falsification of inappropriate universal positivity, not merely an integrity checksum test.

The code and BOTH JSON outputs were ACTUALLY EXECUTED on the exact previously independently reconstructed M13 source formula, re-executed once each in a CLEAN isolated new directory, and both original full JSON files matched BYTE FOR BYTE with the existing computed outputs. No source original file modified.

Exact program source SHA256:
  c3cefd157cdd5d14bba7b7e7502c9bcba703e8776f980f5910d7104cb17201b6
Original complete directed JSON:
  064b820f1e9551ac453b24113390e01532e7c76c9333f0f3fff2421178740b4e
Separate SVD diagnostic program SHA256:
  b4178335c965f7687a56661b6f2cef7b05f728f6e17b8a3fdbd935d98cae4139
Separate 8-case SVD JSON SHA256:
  dd086f20e3f09d798ca5dec99fc2756b50f71e0aa7fb5e4eb546d9fd82ff32b2

USER-CONVERSATION original full reproduction ZIP, NOT claimed mirrored byte-identically into public GitHub:
  IW_M15_ROT019_LEAVE_ONE_NUISANCE_ABLATION_SOURCE_IV65_REPRO_001_20261116.zip
  24,314 bytes, SHA256 08e937c4eafcd0cd5904360db92773655115d2bbec467fa0c94462d4843ba14a.
It contains original M15-source FORMULA file, new full iv65 checker, independent SVD code, actual two machine JSON outputs, replay/negative test code and outputs, complete README, byte identity checks and manifest. ZIP CRC PASS; 12/12 manifest payload SHA256 PASS; exact archive member byte re-read PASS; clean original core and SVD replay both BYTE IDENTICAL PASS; both negative fixtures rejected as intended. No original author M13 unchanged program or historical DTC0a producer bytes are in the ZIP or claimed to have been executed.

## 5. Ceiling and science integration

The source-original five mask energies are functions of the hypothetical common rigid translation t of ALL original source fields versus fixed observer windows, plus an unknown common scale. These are NOT documented native source controls in original M13 source(), NOT measured nuisance parameters and NOT a real Fourier apparatus. The independence of five shell observations and hypothetical Gaussian covariance is entirely an auxiliary mathematical observer class. No transfer to physical NASH K/J3/TPE, Schall optical sensing, Wu-Xu PBH/BBN, animal neurons or real-world physical inversion.

This source-mathematical ROT019 is independent reviewer/research I1 INTERNAL NONBLIND, not blind external I3. Original M13, Geeky-S12 ROT023/024 and M15 ROT018 firstness retained. The quantitative local information intervals do not establish global nonlinearity resolution, a uniform source alpha-noise error guarantee or true physical feasibility. The historical complete dtc0a_runtime_v0_3_1.py remains byte-unrecovered. REC12/AUD2 independent review of THIS newly derived ablation result has not been obtained. KN14 owns BW; GitHub commit plus Slack dispatch do NOT confirm native BW ingestion and no ING_ID or ACK is invented.

FINAL:
M15_ROT019_FULL_TWO_SOURCE_FOLD_BRACKET_IV65_RECOMPUTATION_PASS /
FOUR_SINGLE_NUISANCE_ABLATIONS_TIMES_TWO_ROOTS = 8_OF_8 STRICT_POSITIVE_FISHER_PASS /
EIGHT_FULL_BRACKET_5x4_AUGMENTED_RANK4_PASS /
EIGHT_INDEPENDENT_SVD_MIDPOINTS_INSIDE_STRICT_CERTIFICATES_PASS /
EIGHT_NUISANCE_KERNEL_COMPONENT_EXCLUSIONS_8_OF_8_PASS /
TWO_NEGATIVE_FIXTURES_FAIL_CLOSED /
ISOLATED_TWO_MACHINE_JSON_REPLAYS_BYTE_IDENTICAL /
SOURCE_M13_AND_INDEPENDENT_FORMULA_SHA_LOCKS_PASS /
ZIP_CRC_SHA12_OF12_PASS /
LOCAL_IDENTIFIABILITY_WITH_ONE_KNOWN_NUISANCE_PINNED /
GLOBAL_INVERSION_AND_PHYSICAL_CONTROLS_UNRESOLVED /
BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE.
