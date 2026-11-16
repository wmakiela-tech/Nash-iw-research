---
artifact_id: IW_M15_ROT025_WITHIN_SHELL_SPATIAL_CORRELATION_NEGATIVE_SOURCE_THEOREM_001_20261116
return_id: IW_M15_ROT025_ORIGINAL_M13_SOURCE_TINY_CORRELATED_SITE_NOISE_BREAKS_INDEPENDENT_HETEROGENEITY_FISHER_FLOOR_001_20261116
origin_cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_10 / M15
date: 2026-11-16
exposure: PUBLIC
result_class: INTERNAL_SOURCE_CONDITIONAL_ORIGINAL_M13_BYTE_NATIVE_IV70_NEW_COVARIANCE_COUNTERMODEL_WITH_SEPARATE_41CUBED_FFT
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_SOURCE_NATIVE_PHYSICAL_SENSOR / NO_HISTORIC_DTC0A / NO_UNRESTRICTED_CORRELATION_THEOREM / NO_GLOBAL_INVERSE / NO_LITERATURE_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE
---

# M15 ROT025 — tiny within-shell spatial correlations break the independent-site Fisher floor

## Science result, firstness and explicit limits

NEW **SOURCE-CONDITIONAL NEGATIVE MODEL** with rigorous positive-definite Gaussian site covariance. Geeky-S12 ROT027 FIRST proposed the M13 auxiliary N41 Fourier B sixth full energy source channel; ROT029 FIRST developed exact shared-site old/full noise covariance and the 18,268-site outer equivalent; ROT030 FIRST source-certified a Gaussian Fisher lower bound for heterogeneous BUT INDEPENDENT per-site raw-energy errors with site variance factors in [0.5,2] and a separate independent Gaussian full-raw calibration noise. M15 ROT023/024 performed independent I1 nonblind source audits of those results. They are mathematically correct under their hypotheses. This work deliberately breaks per-site **independence**, without altering ANY per-site marginal variance. No claim that any physical M13 sensor has this noise.

Source original M13 public helper first:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py
Original exact 8970-byte code Git blob c6377cfbc9a0070abc34ffedc5871e719f6a4679, full SHA256 cd4aad089bf68e2e6155ff048d4d812943495dcf1770c8acbf0ff8111b1deb9c. The unchanged original module tensor_polys(41)[B] and original dot were ACTUALLY executed in both NEW checkers. The full native B quartic G(alpha) source calculation was freshly recomputed by outward mpmath.iv70; original source G overlaps the prior M15 native IV65 source G on BOTH original alpha brackets.

Independent PREVIOUS original source certs SHA-LOCKED and reused, not falsely asserted newly rebuilt:
- Original M15 ROT023 original-native IV65 five-window/outer nuisance derivatives, q0, delta_o and G,O; original full machine JSON SHA256 7ddfec37585f587289f6977239ef55514e0c413034e5b223af4131c0949bfa1e.
https://github.com/wmakiela-tech/Nash-iw-research/blob/6aee4744bbd6a4f9444a47abff54f177ac36e5fb/research/m15/2026-11-16/IW_M15_ROT023_INDEPENDENT_ORIGINAL_M13_CORRELATED_SITE_NOISE_OUTER_SHELL_AND_COMMON_ADD_BASELINE_RANK_001_20261116.md
- Original M15 ROT024 original-native IV70 independent-site stochastic calibration/heterogeneity source results; original full JSON SHA256 0debe136d5f8c77a991d426c826d994081bf17f9122feda8f4dc2e02c7d44265.
https://github.com/wmakiela-tech/Nash-iw-research/blob/7f5242eee8ce9cd8c3796370aefafc46e306327d/research/m15/2026-11-16/IW_M15_ROT024_DIFFERENT_CELL_ORIGINAL_M13_STOCHASTIC_CALIBRATION_LOEWNER_REFEREE_AND_TWO_EXACT_ALIAS_PAIR_GAUSSIAN_HYPOTHESIS_GATES_001_20261116.md

## Exact new Gaussian spatial covariance

Original N=41 source grid M=68,921 sites. Its original five disjoint fixed spatial cube mask shells k=2,3,4,5,6 contain w=(7778,6938,6146,5402,24389), total 50,653. The complementary SIXTH exterior region contains w0=18,268. For each site x in region r(x), choose independent unit Gaussian epsilon_x and six independent unit Gaussian Z_r; define the hypothetical RAW ENERGY site noise
  xi_x = eta [sqrt(1-rho) epsilon_x + sqrt(rho) Z_r(x)].
Here 0<=rho<1, eta>0, every site has EXACT Var(xi_x)=eta^2 (unchanged, h_x=1), covariance of distinct sites within each disjoint region is rho eta^2, and covariance across different regions is zero. Each region's exact source site-covariance eigenvalues are eta^2(1-rho) and eta^2[1+rho(w_r-1)], all STRICTLY POSITIVE for rho<1. This is a genuine positive-definite Gaussian model on all 68,921 source sites, not a singular degenerate common-mode shortcut.

Each region-average noise has exact variance eta^2[(1-rho)/w_r+rho] = eta^2 f_r/w_r, f_r=1+rho(w_r-1). Six disjoint region averages have independent noise. The full B original sixth measurement shares all 68,921 site errors with the old five, so its covariance in the old+full coordinates is NONDIAGONAL. The linear old-five+outer change of basis stays invertible. Add independent random RAW FULL calibration noise C with variance eta^2 kappa^2 if desired, as in original Geeky ROT030 (a finite-variance stochastic C, NOT the free unknown deterministic sixth-only log bias c from M15 ROT022). In the outer basis the calibration variance becomes eta^2(M/w0)^2 kappa^2.

For an exact source old five-channel alpha fold, original four nuisance columns X (hypothetical common log gain b and 3 rigid Fourier-field translations relative FIXED masks) have rank4, old alpha score belongs to X. Previous independent M15 ROT023 source-IV65 gives old weighted outer nuisance leverage q0>0, outer normalized raw-site variance n0=(G/O)^2/w0>0, outer directional alpha residual delta_o !=0, and K=M G/(w0 O)>0.

New source covariance makes
  epsilon^2 I_alpha(rho,kappa) =
     delta_o^2 / [f0*n0 + q(rho) + K^2*kappa^2],
epsilon=eta/G,
with q(rho)=xo (X^T diag(w_i(S_i/G)^2/f_i) X)^-1 xo^T. Positive-semidefinite Loewner ordering gives
  f_min*q0 <= q(rho) <= f_max*q0
where f_min=1+rho(5402-1), f_max=1+rho(24389-1). Consequently strict source mathematical bounds:
  delta_o^2/(f0*n0+f_max*q0+K^2*kappa^2)
  <= epsilon^2 I_alpha <=
  delta_o^2/(f0*n0+f_min*q0+K^2*kappa^2).   [025.1]

The source Gaussian efficient Fisher formula applies at the EXACT original old fold alpha root, not as a global continuous-alpha uniform rank theorem. The original rigorous narrow alpha BRACKETS are passed into IV70 to certify all quantities at those roots, whose existence prior M15 ROT015 established.

The previous Geeky ROT030 heterogeneous-independent site variance h_x∈[0.5,2] guarantees
  epsilon^2 I_independent >= delta_o^2/[2*(n0+q0)+K^2*kappa^2].
Define the NEW source threshold:
  rho_star = (n0+q0)/[(18268-1)*n0+(5402-1)*q0].  [025.2]
If rho>rho_star, then even UPPER bound [025.1] is STRICTLY BELOW the old independent-site guaranteed LOWER bound; delta_o^2 and K^2*kappa^2 cancel in this comparison, so this source threshold is INDEPENDENT of ANY fixed finite kappa.

## Original source rigorous directed IV70 certifications

- FIRST source alpha in [0.01861522133766,0.01861522134166]:
  rho_star strict outward interval [0.0001774728507232451387393,0.0001774731287881181562653].
  rho=0.001, kappa=.01: correlated epsilon^2 I_alpha **UPPER** < 3.098305630. Original independent h∈[.5,2] epsilon^2 I_alpha **LOWER** > 8.894422421. Strict disjoint.
- SECOND alpha in [0.05416739905600,0.05416739906000]:
  rho_star [0.0001839246315017551374050,0.0001839250280475069550359].
  rho=0.001, kappa=.01: correlated epsilon^2 I_alpha **UPPER** < 77.532047531. Original independent h∈[.5,2] epsilon^2 I_alpha **LOWER** >243.484672015. Strict disjoint.

All 16 original M15 ROT025 IV70 scenario enclosures for 2 folds × 4 rhos [0, 0.0001, 0.001, 0.01] × 2 kappas [0,.01] passed. The primitive Gaussian site covariance and old+full-to-outer transformation were independently checked as EXACT rational identities with Python Fraction at rho=1/1000. No single noisy Gaussian sample was required to prove the information decrease.

## Separate actual ORIGINAL native 41-cubed spatial FFT / GLs audit

A DIFFERENT original M13 source Python algorithm builds the 9 tensor components and four exact-mode derivative fields on the entire N41^3 spectral lattice, directly inverse-FFTs to source spatial fields, integrates ORIGINAL fixed cube shell masks, constructs raw 6×4 nuisance and 6×1 alpha score matrices, and performs direct Cholesky GLS for TWO independently coded covariances:
 (1) correct original five-old-plus-FULL NONDIAGONAL shared-site Gaussian covariance;
 (2) old five plus independent OUTER region noise after exact linear change of basis.
These source spatial algorithms DO NOT import the new original IV70 source q0/rho interval numeric arrays to compute GLS values, only check the strict IV70 intervals post-hoc. For all 16 cases both Gaussian GLS methods agree to relative < 1e-9 and their results lie inside independently certified new IV70 source bounds. This is a NUMERICAL independent source representation control, not substituted for the IV proof.

At rho=.001, kappa=.01:
 FIRST actual spatial GLS epsilon^2 I≈2.5047636107914646, incorrectly assuming iid sites would give 14.94616092646674, an overestimate **5.9670944×**.
 SECOND GLS ≈59.22680561866265, false iid case 470.46779895159614, overestimate **7.9434944×**.
Two model-negative tests PASS; original mean source operator/parameter values are unchanged.

## Actual reproducibility and source integrity

The user-local complete self-contained original-code ZIP is named
  IW_M15_ROT025_ORIGINAL_M13_CORRELATED_SITE_NOISE_FISHER_FALSIFIER_IV70_REPRO_001_20261116.zip
size **50,354 bytes** SHA256 **fab54c3afe64659b2898a0d6c8db69917a1c25b6898ec6eb2d1f55f5de767375**.
12 ZIP entries include UNMODIFIED original native 8970-byte M13 Python, both original independently source-produced parent M15 IV65/IV70 full JSON certificates, new actually executed IV70+FFT source Python, complete two original result JSONs, actual replay/tamper script and receipt, full local scientific report, README and SHA256 manifest. Archive ZIP CRC PASS, exactly **11/11 payload SHA256 PASS** and all member byte re-read PASS.

Source/code:
  new source iv70 actual script SHA256 c4d95dae18c3835a09ebf24084697663f4a55dddfb2c39bd27b3270e01ef3a1d;
  full new directed IV70 result JSON SHA256 5211ebea5e49de7f29892701d64caee15ff6911007225ad1be7f41b23f197eb5;
  new independent actual native FFT/GLS script SHA256 4752223b421b9d98545826b232690725642f5ced5f3e0a7be1574b70070ed1af;
  full new spatial source result JSON SHA256 a0e1a203bc6907a9d97946d2a3cb18bba388f699a28c00aefcdb9440e89bda13;
  actual cold replay/tamper receipt JSON SHA256 7973f669d8410b8b723927f3fa0d471acd9a72f0c470fe145fd08a98e0e07598.

Both original scientific scripts were ACTUALLY reexecuted in an empty independent temporary directory with unchanged original source files, and both complete resulting JSONs were BYTE IDENTICAL to original outputs: 2/2 PASS. FIVE source/data one-byte mutations each rejected BEFORE mathematical work, including original M13 corruption against BOTH scripts, prior M15 IV65 and IV70 source certificate corruption, and new IV70 result corruption against separate FFT verifier: 5/5 FAIL-CLOSED PASS. A scientific negative model check compares new rho=.001 versus false rho=0 interpretation of same covariance: both flag large false source Fisher positivity claims.

Complete actual source scripts/strict interval output live in user-local ZIP, NOT falsely claimed to have been separately byte-mirrored in GitHub. This public GitHub report and curated JSON are scientific source-custody publications.

## Hard boundary

M13 native calc exposes NO physically free rigid field translations, common log gain, calibrated sixth B full-energy detector or actual Gaussian site measurement. This is an auxiliary N41 source-MATH covariance countermodel. The complete historic dtc0a_runtime_v0_3_1.py was NOT recovered. The construction refutes an unlicensed extension of a prior GUARANTEE, NOT the true original Geeky independent-site theorem. No physical experimental NASH K/J3/TPE / sensor SNR inference. No global alpha inversion, external blind I3, general original mathematical novelty, KN14 native BW ingest ACK, CANON or EXEC_SIGN. Original M13 and Geeky FIRST provenance retained. NO_TASK_CASCADE.

FINAL:
M15_ROT025_SOURCE_CONDITIONAL_EXACT_68921_SITE_GAUSSIAN_POSITIVE_DEFINITE_COVARIANCE_PASS /
PER_SITE_MARGINAL_VARIANCE_IDENTICAL_BUT_IID_BROKEN /
TWO_RHO_STAR_FULL_SOURCE_BRACKET_DIRECTED_IV70_PASS /
TWO_CORRELATED_INFORMATION_UPPERS_BELOW_PRIOR_INDEPENDENT_HETEROGENEOUS_LOWERS_PASS /
ORIGINAL_NATIVE_M13_FULL_FOURIER_G_VS_PRIOR_NATIVE_SOURCE_IV65_PASS /
16_SPATIAL_41CUBED_TWO_GLS_NUMERIC_CHECKS_PASS /
TWO_FALSE_INDEPENDENCE_NEGATIVE_CONTROLS_PASS /
TWO_CLEAN_FULL_RESULT_JSON_BYTE_IDENTICAL /
FIVE_PRE_SCIENCE_ONEBYTE_TAMPER_FAIL_CLOSED /
ZIP_CRC_AND_11_OF_11_SHA256_PASS /
GEEKY_ROT030_FIRSTNESS_RETAINED / BW_PENDING /
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE.
