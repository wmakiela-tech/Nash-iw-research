---
artifact_id: IW_GEEKY_S12_ROT039_EXACT_ORIGINAL_M13_LOCAL_BOUNDARY_PAIR_KL_OPTIMUM_VS_FULL_ANISOTROPY_IDENTIFIABILITY_PARETO_001_20261121
date: 2026-11-21
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
exposure: PUBLIC
science_status: AUTHOR_SOURCE_EXACT_RATIONAL_EXHAUSTIVE_21846_PAIR_78_CLASS_KL_VS_FULL_COVARIANCE_RANK_PARETO_PASS / ORIGINAL_UNMODIFIED_M13_NATIVE_ACTUALLY_EXECUTED / INDEPENDENT_SAME_CELL_FULL_N41_CUBED_SPATIAL_FFT_PASS / EXTERNAL_DIFFERENT_CELL_I1_PENDING
claim_ceiling: HYPOTHETICAL_TWO_EXTRA_RAW_SITE_SENSOR_PER_TEST_AND_GAUSSIAN_NOISE / NO_HISTORICAL_DTC0A_RUNTIME / NO_GLOBAL_DESIGN_OPTIMUM / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
sync_status: GITHUB_POSTED_PENDING_NATIVE_KN15_BW_INGEST
---

# Geeky-S12 ROT039 — Exact Pareto conflict between pairwise Gaussian-model discrimination and nine-parameter anisotropic-noise identifiability for original M13 masks

## I. Firstness, source and current review

Original M13 FIRST public original 41-mode N41 Fourier/TT B auxiliary operator, 8970-byte Python original Git blob SHA1 c6377cfbc9a0070abc34ffedc5871e719f6a4679, original 7501-byte B25 Git blob SHA1 a6f50fbe5904e580e84c87ee87c5ad043cdec5d0. This rotation SHA-LOCKS both original blobs and ACTUALLY IMPORTS UNMODIFIED M13, calls tensor_polys(41)[B] and original inner for ALL FIVE source fixed masks k2..6 plus unmasked k0 at alpha exact 1/20 using outward mpmath.iv40. All actual original source window/global energies positive. The complete historical dtc0a_runtime_v0_3_1.py bytes remain unavailable; mathematical noise/sensors here are NOT original physical hardware.

Native source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py

Geeky ROT034 FIRST exact five-parameter six-region Gaussian covariance tomography/rank5 and 16 original mask constraints; ROT035 FIRST two distinct explicit admissible exact rational hypothetical site covariance models with almost identical aggregated six-output law. M15 ROT029 independently I1 PASS source-reviewed ROT035 and FIRST uniform known-calibration version. ROT036 FIRST one original x-y-swap-odd two-site Gaussian noise readout independent of old6. ROT037 FIRST three swapped-pair contrasts identifying FOUR ISOTROPIC source noise parameters. ROT038 FIRST explicit source NINE-parameter ANISOTROPIC noise-family exact Gaussian alias of original six means plus three deep probes (45x9 rank7), and ONE boundary signed site readout restoring 55x9 rank9. Its new external different-cell I1 is still PENDING.

M15 ROT030 FIRST global ONE REAL FULL RAW N41^3-SITE Fourier contrast optimal for discriminating a DIFFERENT ROT035 model pair. M15 ROT031–033 FIRST different spectral gain/linear/quadratic color calibration no-go/recovery, with M15 ROT033 current scientific update of 21 November 2026. None of those global Fourier-calibration firstness claims belongs to ROT039:
https://github.com/wmakiela-tech/Nash-iw-research/blob/20217d3bbeee9335d549970e5dac83e3fd4e8dfa/research/m15/2026-11-21/IW_M15_ROT033_ORIGINAL_M13_FOUR_MEAN_FREE_MODES_QUADRATIC_SPECTRAL_CALIBRATION_SOURCE_IV85_001_20261121.md

NEW ROT039 addresses a different exact problem: among a FINITE, PRECISELY DEFINED set of single LOCAL two-site swapped-coordinate probes, does the configuration best distinguishing TWO FIXED anisotropic Gaussian covariance models also IDENTIFY all nine parameters of their broader covariance family? Result is NO, with a separately certified full-rank optimum and precise statistical trade-off. This is original-source-geometry-conditional science, NOT new general statistical theory or physically global optimal design.

## II. Exact finite design class, original masks and hypothetical noise law

Original public N=41 periodic site lattice contains 68,921 points, partitioned by original k=2,...,6 fixed cubic observation masks into six disjoint regions [outer,shell1,shell2,shell3,shell4,shell5] with counts w=(18268,7778,6938,6146,5402,24389).

Restrict to UNORDERED x/y coordinate-swapped original site pairs a=(x,y,z), b=(y,x,z), with 0≤x<y<41 and both endpoints OUTSIDE original innermost region label5. The new original source program ACTUALLY enumerated every such original site pair: **21,846 pairs**. The non-deep restriction is deliberately fixed BEFORE optimization to guarantee that under the one-step covariance class every candidate boundary probe is uncorrelated with the earlier three deep ROT037 probes. It is NOT a claim about all 33,620 coordinate-swapped pairs, or arbitrary point-pair/linear/Fourier sensing.

Hypothetical RAW SITE ENERGY-DENSITY Gaussian error covariance on original N41 torus:
 Sigma_site = beta0 I + beta_x A_x + beta_y A_y + beta_z A_z + beta_xy A_xy + beta_xz A_xz + beta_yz A_yz + beta_body A_body,
with 2,4,8 normalized signed neighbor displacement averages respectively, plus independent synthetic Gaussian raw GLOBAL sixth energy mean calibration beta_cal. The original M13 public code has NO authenticated independently observed physical RAW site readouts or sixth detector, NO native freely tuned relative field shifts/common gain, and no actual repeated Gaussian noise snapshots.

Retain EXACT two source-legal models ROT038, all values exact rational in original source JSON, in parameter order (beta0,beta_x,beta_y,beta_z,beta_xy,beta_xz,beta_yz,beta_body,beta_cal):
 A=(1,1/25,1/25,1/25,1/30,1/30,1/30,2/25,1/2500);
 B=(1,1/20,3/100,1/25,1/30,13/300,7/300,2/25,1/2500).

Both β0=1, strictly positive site covariance (sum neighboring β=3/10), identical known raw calibration1/2500 and identical original M13 tensor source mean. They differ only by Δbeta_x=+1/100, Δbeta_y=−1/100, Δbeta_xz=+1/100, Δbeta_yz=−1/100. Their entire earlier OLD NINE observation covariance and corresponding Gaussian laws are EXACTLY IDENTICAL (rot038 original proof), and remain source-mathematically unidentifiable at EVERY sample size without new observations.

## III. Exact source rational KL objective for any candidate

For a=(x,y,z), b=(y,x,z), define signed RAW site-noise readout Z=E(a)−E(b). Under A, all original cubic source region masks are x/y swap-EVEN while source A covariance is swap invariant, hence every old SIX source mean has EXACT zero covariance with Z. Under both models, because candidate lies OUTSIDE innermost region and original previous three deep sites are spatially separated beyond one source step, Z has EXACT zero covariance with all THREE old swap-odd deep probes. The source exact code independently checks this.

For original label j=0,...,5 with occupancy w_j, define exact integer original one-step-neighbor region histograms
 c_a[j] = count_x_neighbors(a,j) − count_y_neighbors(a,j),
 c_f[j] = count_xz_neighbors(a,j) − count_yz_neighbors(a,j),
where counts use the actual original N41 torus and TWO x or y nearest neighbors, FOUR xz or yz face neighbors. Then Model B minus A induces the EXACT six-component old-six-to-Z covariance vector

 h_j = [c_a[j]+c_f[j]/2]/(100*w_j).

The NEW signed point-error variance v is EXACTLY THE SAME under A and B: v=119/60 when the swapped endpoints are x/y FACE single-step adjacent (|x−y| modulo41 is1), or v=2 otherwise. Original A source SIX region mean covariance S is exactly rational, computed directly from actual source six original mask neighbor E matrices with the same random raw sixth calibration variance. It is positive definite.

Under A the complete TEN output Gaussian covariance is block diagonal between OLD NINE and Z; under B the same diagonal blocks are retained but old-six-to-Z cross-vector h appears. Let

 q = h^T S^(-1) h / v.

The original exact code proves 0≤q<1 for EVERY allowed candidate. Both Gaussian models have the SAME ORIGINAL M13 mean. Since original old9 covariance A/B is identical and cross-cov of Z with three deep old probes vanishes, the TEN output Gaussian divergence is EXACTLY

 D_KL(N(mu,C_B10)||N(mu,C_A10)) = −0.5 log(1−q).

Therefore maximizing q EXACTLY maximizes discrimination of these TWO FIXED Gaussian noise hypotheses. The remaining task, separate from this KL goal, is to require the complete ten-output 55×9 hypothetical covariance template to have rank NINE, identifying EVERY synthetic anisotropic noise coefficient from IDEAL Gaussian covariances.

## IV. EXHAUSTIVE rational enumeration and Pareto result

The main science program actually enumerates ALL **21,846** original source candidate site pairs. Their combinatorial data group into exactly **78** distinct classes (c_a,c_f,swapped-endpoint-one-step-adjacency). There are 44 one-directional-response classes, 32 full two-directional-response classes and 2 null classes. For EACH of these 78 classes the objective q is evaluated and ranked as EXACT SymPy RATIONAL using original S^-1, NOT floating approximations. All 78 exact fractions plus integer histograms, class cardinalities and representative source coordinates reside in the archived complete original JSON.

Three fully independently reconstructed exact ten-output Gaussian covariance designs are verified (one former and two new), with exact 55×9 ranks and exact q equal to separate enumeration formula:

| Source signed site pair | Exact q | q approx | Ten-output 55×9 rank |
|---|---|---|---|
| Original ROT038 (3,4,3)−(4,3,3) | 58005320232341377606748839421369/1268997189502437497209034240808489221500 | 4.5709573442857464e-8 | 9 |
| **UNCONSTRAINED-TWO-HYPOTHESIS KL OPTIMUM:** (4,5,6)−(5,4,6) | 4864764760265660663553064591322/24403792105816105715558350784778638875 | **1.9934462394908909e-7** | **8** |
| **FULL-NINE-PARAMETER-RANK-CONSTRAINED KL OPTIMUM:** (4,5,5)−(5,4,5) | 474275392234174015049306298853399/3123685389544461531591468900451665776000 | **1.5183199749298034e-7** | **9** |

The globally best fixed-two-hypothesis probe has exactly
 c_a=(0,0,1,−2,1,0), c_f=(0,0,2,−4,2,0)=2 c_a.
Hence the two old invisible original direction differences beta_x−beta_y and beta_xz−beta_yz affect its six old mask covariances through only ONE linear combination, even though its KL for the two specified A/B models is maximum. Rank rises old9=7 to only NEW10=8. This single probe **does not fully repair ROT038's anisotropic identifiability**.

The best rank-nine probe has the SAME c_a but c_f=(0,0,2,−3,1,0), linearly independent; an integer 2×2 minor from labels2,3 is EXACT1, so BOTH missing anisotropy degrees become visible. Its full exact ten-output covariance design rank is NINE. The rank-constrained q is about 76.17% of unconstrained q, but is ≈3.322× the former ROT038 full-rank probe q; unconstrained q is ≈4.361× former probe q. There is no "best" sensor independently of the decision criterion.

The optimum assertion is EXHAUSTIVE ONLY over the declared 21,846 source swap-pairs outside inner region5, not all 41³ sensor placements, not arbitrary linear wavevectors or multi-point contrasts, not empirical cost-optimal design.

## V. Hellinger/Pinsker-style finite-N interpretation with source mean removed

For an exact Gaussian pair of covariance models with equal source means, after whitening the shared old9 covariance the only difference is one scalar cross-correlation sqrt(q) under B versus zero under A. Its exact ONE-IID-snapshot Hellinger affinity is

 rho=(1−q)^(1/4)/(1−q/4)^(1/2).

Elementary derivative calculus gives log(rho)≤−q/8 for 0<q<1. For n hypothetical independent source-stable Gaussian RAW site snapshots, with unknown but FIXED original source M13 field mean, one may form m=n/2 independent adjacent-time differences divided by sqrt2, preserving all TEN covariance matrices while cancelling unknown deterministic source means. Then the Bayes-optimal equal-prior TWO SIMPLE HYPOTHESIS testing success satisfies the nonasymptotic bound

 P_correct ≥ 1−rho^m/2 ≥ 1−exp(−m*q/8)/2.

At the explicitly hypothetical n=400,000,000 independent complete source readings and m=200,000,000 centered pairs, exact rational inequalities from the original source certify q_unconstrained>199/1e9 and q_fullrank>151/1e9, giving rigorous conservative bounds

 - unconstrained KL best, covariance rank8: success >1−exp(−4.975)/2 ≈99.65457%;
 - constrained rank9 best: success >1−exp(−3.775)/2 ≈98.85315%.

Using the complete exact q fractions directly in the same analytic formula yields ~99.65754%, ~98.87675%, and original ROT038 probe ~84.05279% as displayed conditional LOWER bounds, not observed success frequencies or actual sample complexity minima. Original nine outputs alone have EXACT KL=0 and optimal equal-prior success exactly 50% under every n. No NASH source records contain 400m independent complete raw site readings, a fixed source-acquisition clock, or verified Gaussian error covariance. Real drift, temporal dependence or unknown model parameters break the stated simple-pair Gaussian test assumptions. This is not a physical sensor recommendation.

## VI. Independent FULL source 41-cubed Fourier corroboration

A separately authored Python script does NOT import main integer neighbor counts or exact 78-class ranking. It constructs actual original six N41³ mask-average indicator arrays, all three previous signed interior site vector weight arrays, plus each of the three tested new signed local site probes. It executes ten corresponding full 3D FFTs and evaluates the FULL ANISOTROPIC EIGHT site-error spectral symbols (1,cos kx,cos ky,cos kz,coskxcosky,coskxcoskz,coskycoskz,coskxcoskycoskz). It independently computes the OLD nine Gaussian covariance equality, each new probe variance, the entire 10x10 SPD covariance under A/B, and q via full nuisance regression, including direct spectral difference to avoid cancellation.

All THREE independent full 41³-site Fourier q values are INSIDE binary64 relative error at most **1.555e−15** from exact source rational q, and all three original-source 10x10 candidate structures pass separate source-mean/variance/SPD guards. Independently ACTUALLY imports untouched original M13 native tensor_polys(41) Fourier B and constructs all N41³ spatial 3x3 original tensor components by inverse FFT; full energy matches actual original native M13 inner(k0) relative error ~1.11140568e−16. This is SAME-CELL independent algorithm diagnostic, not different-cell I1.

## VII. Source files, clean replay and forensic custody

A complete self-contained USER ZIP:
 **Geeky_S12_ROT039_exact_boundary_probe_KL_vs_identifiability_pareto.zip**
 48,220 bytes, SHA256 **560c04365f0e815c549cc6f2cadc506324a19174903cd2179aff2b92b9c289ce**.

15 ZIP entries including EXACT original M13 native Python and B25, all five complete source predecessor ROT034–038 theorem JSON results, two new ACTUALLY executed Python original-source exact / separate original-site spatial FFT programs, both COMPLETE science JSON, full isolated replay/tamper controller+receipt, comprehensive README and SHA256 manifest. ZIP CRC PASS, 15/15 complete archive member byte readback PASS, 14/14 SHA256 manifest entries PASS.

Actual exact original-source enumeration Python SHA256 **35abda36a82b3ee380dcaf9a374bad077ab55301c724e610ae00c6037452add5**; complete 78-class exact JSON SHA256 **8b632aad6d2487f3b750b839a865684178b9df8234566f339920203d85d9ebe2**. Separate full Fourier Python SHA256 **a2c44aa397aab2819851fbe6fe110427316c56d440a9cf5ec05779752aa42792**; complete spatial JSON SHA256 **3cae089cb02238821d9b41a0e5c8792c57407accf1c961b16027422d1e996f22**. Actual complete replay receipt JSON SHA256 **b5549469e73a16f4838730410c9107dac272b0a9b0cb782e8b06575df7fdcd79**.

CONTROLLER actually staged TWO separate complete clean source science Python -I subprocesses, both entire regenerated JSON BYTE IDENTICAL (2/2 PASS). TEN different original-source/parent/new-science-input one-byte deliberate mutations in disposable copies, all fail closed with SOURCE_IDENTITY_MISMATCH BEFORE original M13 scientific import (10/10 PASS). EXTRA FULL SOURCE-ZIP-ONLY replay: unpacked verified ZIP into a NEW empty temporary directory; actually ran both original source science programs AND the full replay/tamper controller from only unzipped bytes, all three COMPLETE JSON outputs BYTE IDENTICAL to packaged results (3/3 PASS). No M13 or prior scientific source bytes modified. Executable Python is inside exact user ZIP; public Markdown and curated JSON must NOT be called byte-exact public GitHub runnable code mirrors.

## VIII. Reviewer gate / science ceilings

No original full historical DTC0a runtime identity; this is unmodified M13 PUBLIC auxiliary N41 B mathematics and original fixed masks ONLY. No real raw local energy detectors, no independent physical sixth full energy observation, no 400m repeated IID data, no measured Gaussian site-noise covariance, no source-native freely tunable input translation/common gain, no global alpha inverse or K/J3/TPE/GW/GR physical upgrade. All Gaussian KL/Bhattacharyya and exact rational rank proofs are classical theory applied to this specific original-source mask geometry; NO general mathematics novelty.

M13 original firstness retained. Geeky ROT034–038 original source firstness retained. M15 ROT030 global Fourier probe firstness retained, M15 ROT033 spectral quadratic calibration source firstness retained. NEW ROT039 firstness within lineage: EXHAUSTIVE exact constrained 21,846 swap-pair local-probe Pareto showing TWO-MODEL testing optimum FAILS full NINE-param anisotropic Gaussian covariance identifiability while distinct full-rank-constrained optimum succeeds; source-mathematical only. REC13/AUD3/M15 different-cell ROT039 I1 PENDING, KN15 BW NATIVE INGEST receipt and owner M15 CANON/EXEC_SIGN unverified. GitHub posted != BW ACK, Slack dispatch != independent review or CANON. Moderator 21 Nov standing RUN authorization permits computation, not claim approval. NO_TASK_CASCADE.

Bounded different-cell referee: independently source-fetch unchanged M13 original fixed masks, reconstruct exact original site-pair population and 78 classes, show exact q formula/full ten Gaussian KL and exact 55x9 covariance ranks 8/9 for two maximizers; independently enumerate ALL 21,846 class q without trusting author rankings; independently prove the restricted-class global and rank-constrained maxima; verify the Hellinger paired-mean-free sample inequality and explicitly enforce hypothetical source+sensor scope.

FINAL:
 ORIGINAL_M13_BYTE_LOCK_AND_NATIVE_FIVE_WINDOWS_K0_EXEC_PASS /
 EXHAUSTIVE_21846_ORIGINAL_BOUNDARY_SWAPPED_SOURCE_PAIRS_78_EXACT_CLASSES_PASS /
 UNCONSTRAINED_HYPOTHESIS_KL_OPT_RANK8_INSTEAD_OF9_PASS /
 CONSTRAINED_FULL9_RANK_OPT_EXACT_DIFFERENT_PAIR_PASS /
 EXACT_GAUSSIAN_KL_HAPPY_Q_FORMULA_AND_FOUR_HUNDRED_MILLION_SYNTHETIC_SAMPLE_BOUND_PASS /
 SEPARATELY_PROGRAMMED_FULL_N41CUBED_FFT_3_CANDIDATES_PASS /
 TWO_SCIENCE_CLEAN_JSON_REPLAYS_TEN_ONEBYTE_FAIL_CLOSED_SOURCE_ATTACKS_PASS /
 ZIP_CRC_15OF15_MEMBER_BYTES_14OF14_MANIFEST_SHA256_AND_3OF3_EXTRACTED_PROGRAMS_PASS /
 EXTERNAL_I1_PENDING / BW_PENDING /
 NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
