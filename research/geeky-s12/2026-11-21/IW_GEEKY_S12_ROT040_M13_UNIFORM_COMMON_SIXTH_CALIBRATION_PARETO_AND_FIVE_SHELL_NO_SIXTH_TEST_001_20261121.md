---
artifact_id: IW_GEEKY_S12_ROT040_M13_UNIFORM_COMMON_SIXTH_CALIBRATION_PARETO_AND_FIVE_SHELL_NO_SIXTH_TEST_001_20261121
date: 2026-11-21
origin: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
status: AUTHOR_EXACT_RATIONAL_ORIGINAL_M13_SOURCE_PROOF_PASS / SAME_CELL_41CUBED_INDEPENDENT_FOURIER_PASS / NEW_DIFFERENT_CELL_I1_PENDING
source: ORIGINAL_PUBLIC_M13_8970B_PYTHON_B25_7501B_EXACT_GIT_BLOBS_VERIFIED_AND_NATIVE_EXECUTED
sync: GITHUB_PENDING_NATIVE_BW_INGEST
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT040 — uniform source-local probe selection for any common independent sixth-only random calibration, and calibration-free five-original-shell discrimination

## 1. Original M13 source, firstness and new problem

M13 FIRST original public auxiliary N=41 B Fourier/TT operator with 41 sparse complex 3x3 tensor modes, five original fixed cubic masks k2..6 and mathematical unmasked full B-energy k0. Exact ORIGINAL unmodified public Python 8970B Git blob c6377cfbc9a0070abc34ffedc5871e719f6a4679 and B25 original JSON 7501B blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0. The new executable verifies both source bytes BEFORE scientific import, then ACTUALLY invokes native tensor_polys(41)[B], ORIGINAL inner for all five fixed windows and full k0, using outward mpmath.iv40 at alpha=1/20; all six original source energies strictly positive. The complete historical dtc0a_runtime_v0_3_1.py producer remains missing.

Prior source firstness retained: Geeky ROT034 exact five-parameter six-region noise covariance rank and 16 tests; ROT035 explicit near-KL-zero legal source Gaussian pair (M15 ROT029 different-cell native I1 PASS core); ROT036 one odd site-probe; ROT037 three local odd probes for four ISOTROPIC coefficients; ROT038 original 9-parameter ANISOTROPIC Gaussian old-nine exact alias plus boundary repair; ROT039 exhaustive exact 21,846-candidate LOCAL swap-pair optimization at fixed raw sixth calibration 1/2500 and separate KL-vs-rank9 winners. ROT038/039 new external independent I1 not verified. M15 ROT030 FIRST globally optimal single full-41cubed-site real Fourier contrast for another A/B task; M15 ROT031-033 FIRST spectral unknown-scale/linear/quadratic-color calibration no-go/recovery. The present original-source local SIXTH-ONLY rank-one perturbation is a distinct claim, not M15 global Fourier or spectral calibration firstness.

Current M15 independent prior:
https://github.com/wmakiela-tech/Nash-iw-research/blob/20217d3bbeee9335d549970e5dac83e3fd4e8dfa/research/m15/2026-11-21/IW_M15_ROT033_ORIGINAL_M13_FOUR_MEAN_FREE_MODES_QUADRATIC_SPECTRAL_CALIBRATION_SOURCE_IV85_001_20261121.md

NEW ROT040 question: do the TWO source-exact optimizers of ROT039 remain so when the independent sixth-only Gaussian RAW full-mean calibration variance is an arbitrary COMMON unknown c>=0? Can source A/B be discriminated without the sixth observation even if its calibration distribution is completely unknown? What exact full-parameter identifiability is lost if it is excluded?

## 2. Exact hypothesis and original source masks

Original N41^3=68921 site grid; six fixed source disjoint region occupancies [outer,shell1,shell2,shell3,shell4,shell5] W=[18268,7778,6938,6146,5402,24389]. Every original one-step directional x/y/z/xy/xz/yz/body region neighbor integer graph was freshly enumerated from original site labels and aggregated axis/face/body original integer E matrices independently checked against locked prior ORIGINAL M13 source results.

Two fixed original source site-noise models, HYPOTHETICAL centered Gaussian RAW SITE ENERGY-DENSITY errors, in order [beta0,beta_x,beta_y,beta_z,beta_xy,beta_xz,beta_yz,beta_body]:
A=[1,1/25,1/25,1/25,1/30,1/30,1/30,2/25];
B=[1,1/20,3/100,1/25,1/30,13/300,7/300,2/25].
All covariance operators are original normalized 2,4,8 neighbor periodic shifts; both Gaussian site covariance SPD with strict site eigen lower bound >=7/10. Both have the SAME original M13 deterministic source B mean. A/B exact original OLD NINE mask+three interior noise probe Gaussian covariances identical (ROT038). Their common independent Gaussian RAW FULL energy measurement calibration has variance c>=0. Previous source calculation fixed c=1/2500. Actual M13 provides no authenticated independently measured sixth hardware channel, RAW point sensors or empirical site-noise Gaussian covariance.

Local candidate class: signed original site-energy pair E(x,y,z)-E(y,x,z), x<y, both outside original innermost source region5, ensuring zero one-step noise covariance with earlier three deep probes. Exactly 21,846 original source candidate pairs and 78 exact integer neighbor-region histogram+point adjacency classes, reenumerated in this rotation. Source q and ranks are only optimized IN THIS CLASS, not all sensors or M15's global Fourier target.

## 3. NEW EXACT all-calibration source theorem

Let S0 be ORIGINAL 6x6 old six-region RAW energy mean error covariance for source noise A and NO sixth calibration; S0 is SPD. e is outer-region first basis vector, K=(68921/18268)^2. Add common independent Gaussian RAW full mean error c to A and B; in six disjoint region coordinates original covariance S(c)=S0+c*K*e*e^T. For any new original-source site contrast with identical noise variance v under both models and source cross-covariance difference h (A zero from source coordinate-swap symmetry), all OLD nine A/B mean covariances remain equal and the new contrast has no covariance with three deep probe fields. Consequently EXACT SAME-MEAN full ten-variate Gaussian

D_KL(B10(c)||A10(c)) = -(1/2) log(1-q(c)),
q(c)=h^T S(c)^(-1) h / v.

All observations and site errors are explicitly synthetic. The new source proof uses exact SymPy rational S0 generated from independently enumerated original M13 site regions, not float scans.

Put b=e^T S0^(-1)e>0, q0=h^T S0^(-1)h/v,
q_inf=q0-(h^T S0^(-1)e)^2/(v*b). Sherman-Morrison yields for EVERY REAL c>=0:

**q(c)=q_inf+(q0-q_inf)/(1+c*K*b).**

Thus q(c) is a convex interpolation between exactly q0 and q_inf with **the SAME lambda(c)=1/(1+cKb) for EVERY pair**. Winning at BOTH endpoints implies winning for EVERY c, without parameter-gridding. Original-source computation recalculates all 21,846 pairs and 78 exact classes, exact q0, q_inf, baseline q(1/2500) and proves all baseline values EQUAL exact previous source ROT039 q rational. It verifies directly the matrix inverse of S(1/2500), and EXACT rational class dominance at both endpoints in each of two decision tasks. There are TWO reflection-equivalent maximal classes in each problem, with positive exact gap to every nonmaximal class.

Result 1 (all source candidate classes, fixed-two-known-model KL optimal): E(4,5,6)-E(5,4,6) and its reflection. q0≈1.993453385064634e-7; q_inf≈**1.9934461532633352e-7**. Full-ten NINE-parameter covariance template rank8, not9.

Result 2 (full rank9 constraint): E(4,5,5)-E(5,4,5) and reflection. q0≈1.5183268350393814e-7; q_inf≈**1.5183198921470204e-7**. Full-ten NINE-parameter covariance rank9.

Their exact original prior calibration c=1/2500 source q respectively ≈1.9934462394908909e-7 and ≈1.5183199749298034e-7.

For BOTH winners exact rational tests certify (q0-q_inf)/q0<1/200000, i.e., a strictly <5 parts per million decrease in the specific Gaussian discrimination SCORE q for EVERY common independent c>=0. This does not imply all unknown calibrations, statistical estimators or real apparatus performance are robust.

## 4. Stronger calibration-free sub-observer; negative identifiability result

The limit q_inf equals the Gaussian discrimination score from **only five ORIGINAL disjoint shell means plus the hypothetical new site contrast**, with the sixth global/outer observation excluded:

**q_inf = h5^T S5^(-1) h5 / v**,

where S5 is the ORIGINAL source mask shell-mean 5x5 principal submatrix of S0 and h5 the source five-entry new-contrast crosscovariance. This is proved EXACT for ALL 78 source classes by a separate inverse of original 5x5 shell covariance, not simply inferred from a limit. The previous three deep probes are not required in this two-known-hypothesis test.

Since this five-shell+new site-probe observation omits sixth RAW full measurement entirely, its distribution is independent of the sixth-only calibration noise distribution, even if that unused calibration is non-Gaussian. The retained original SITE errors remain Gaussian and source A/B shapes FIXED; arbitrary non-Gaussian site errors are NOT licensed.

**Source negative knowledge:** dropping the sixth measurement also removes beta_cal from all observable covariance entries. New exact full original source covariance-basis construction gives rank7 of nine coefficients for five old shells+three deep probes+the unconstrained KL winner, and rank8 for the same five+three deep+the formerly full-rank9 winner. No claim of identifying the missing raw sixth calibration parameter with a five-only binary test is permitted. With the sixth measurement included the full-ten ranks remain8 and9 respectively. Also if A/B have DIFFERENT raw sixth calibration variances, original nine covariances cease to be equal and this exact ten-observation q(c) formula is not applicable. Correlated sixth measurement errors may likewise destroy the pure outer rank-one model.

For a purely HYPOTHETICAL n=400,000,000 independent Gaussian site-noise snapshots at stable but unknown fixed original M13 source energy means, pair successive samples to get m=200m independent centered Gaussian observations preserving covariance and cancelling deterministic means. The EXACT worst-case five-shell q_inf remains >199/10^9 for unconstrained pair and >151/10^9 for full-ten-rank9 pair. Classical centered Gaussian Hellinger rho=(1-q_inf)^(1/4)/(1-q_inf/4)^(1/2), log rho<=-q_inf/8, gives for optimal equal-prior simple A/B discrimination:

**P_correct > 1-exp(-4.975)/2 (~99.65457%)**, or
**P_correct > 1-exp(-3.775)/2 (~98.85315%)**, respectively.

They are mathematical lower bounds for this explicitly synthetic two-hypothesis 400m-snapshot example, NOT real samples, necessary sample sizes, source empirical precision or full-parameter estimation confidence.

## 5. Actually executed independent spatial-source corroboration

A separately authored new Python check DOES NOT import original-source class enumeration or regional integer E matrices. It Fourier transforms source FULL N41^3 six fixed mask indicator mean fields and three signed probe fields and evaluates EIGHT original anisotropic Gaussian site spectral symbols directly. For the two new winner sites and original ROT038 prior pair, it independently checks source spectral site covariance, source A cross-mean/new zero, same A/B new variances and Gaussian effective q for c=0,c=1/2500,c=7/3,c=1000 and the five-original-shell-only q_inf. All 3×4 cases match original exact rational rank-one formula within relative 2e-8 tolerance, and all q∞ checks match exact original source. This is a SAME-CELL independent algorithm, NOT a different-cell referee I1.

The separate program ACTUALLY imports unchanged M13 tensor_polys(41)[B], inverse Fourier synthesizes original 41 complex3x3 tensor modes across the entire 41^3 lattice, and checks native original source unmasked inner k0 against original source Fourier reconstructed raw-space energy (relative difference ~1.11e-16). No actual source site sensors or measured physical noise.

## 6. FULL original-source custody, runnable ZIP and negative tests

Self-contained user source ZIP:
**Geeky_S12_ROT040_unknown_sixth_calibration_uniform_local_pareto.zip**
57,325 bytes, SHA256 **241ab7232492c200c8126e5c344c0ae21801d283f33496f2ccbf4a9adfcb5bbd**.

16 archive members: exact M13 original module and original B25, SIX frozen full ORIGINAL ROT034-039 result JSONs, two NEW actually executed original source exact/Fourier Python scripts and two FULL science result JSON, new replay/negative attack controller and its FULL actual JSON receipt, scientific README, exact SHA256 manifest. ZIP CRC PASS, 16/16 original member complete byte readbacks PASS, 15/15 manifest SHA256 PASS.

Actually executed new original exact scientific script SHA256 **22cb9e0c49e309870a258e4b8d38d767438aa1ae5ee5f46b13518f37c3e031cd**; full exact original 78-class result JSON SHA256 **219a6c4fcf8475c9edabf2e656dac8f6c76d1a65a7ba5e62f86daa364c25523c**. Independently authored full original site Fourier Python SHA256 **e9d0f83bde594667194e35801ebb4cc1a7d9cba7c3fc9be122cf80f89cc16ae2**, full JSON SHA256 **50bddcf2a69aa08d482af58d13f28498efdc7c0641525d42fe8759b58b51c3ea**. Replay controller SHA256 **a676d6d13cbbc9f7fef819290b56f6a7836ad071fd2309b480017564c0b6ef16**, complete receipt SHA256 **07aa648542b98885f2b2b63354c90102958f8a3273d1a177a6ed2062c62bb5c9**.

Both scientific programs ACTUALLY rerun fresh isolated Python-I temp directory subprocesses, FULL source scientific JSON BYTE IDENTICAL 2/2 PASS. ELEVEN separate disposable source one-byte corruption tests of original M13, B25, previous ROT034-039 proofs or current main proof were rejected with SOURCE_IDENTITY_MISMATCH BEFORE scientific source import: 11/11 PASS, original source bytes unmodified. Completed user ZIP additionally actually unpacked in empty temp directory; all THREE independent script commands (two science plus replay controller) reexecuted, FULL regenerated JSON bytes matched ZIP originals: 3/3 PASS. Executable code and entire exact rational source outputs are in USER ZIP, not falsely called publicly byte-exact runnable GitHub mirrors.

## 7. Reviewer target, firstness and ceilings

Source-specific new result FIRST within this cell: all-c>=0 common independent sixth-only calibration EXACT endpoint-dominance of BOTH previous original source Pareto optima, strict <5ppm q loss, independent of unused sixth-only random error distribution in the FIVE original shell+new probe statistical subobserver, explicit mathematical 9-parameter template rank-loss when dropping sixth. Other cell M15 prior global Fourier/spectral calibration findings retain firstness. General Sherman-Morrison, Gaussian KL and Hellinger statistical theory is MATURE, not newly established mathematics.

This is original PUBLIC AUXILIARY M13 B N41 only; historic full DTC0a producer unavailable. No authenticated extra RAW site measurement, physical sixth detector, real site-noise Gaussian law, 400 million observed IID samples, adjustable original M13 field translations/gain, global alpha inverse, cosmological K/J3/TPE/GW/GR physics or new physical noise robustness. External different-cell REC13/AUD3/M15 new ROT040 I1 PENDING, KN15 BW native ingest receipt and owner CANON/EXEC_SIGN not verified; public GitHub and Slack dispatch are NOT owner ACK or science acceptance. Moderator standing authorization for calculations is not CANON approval. NO_TASK_CASCADE.

BOUNDED INDEPENDENT REFEREE: independently verify original M13 fixed source mask 6-region geometry and 8 directional E, derive exact q(c) via source Schur/Sherman-Morrison, compute all 78 q0/q∞ and verify exact same winners at both endpoints with no overlooked classes, test exact q∞ equals retained-original-five mean q for all 78, independently recompute reduced old5+three-deep+new probe source covariance basis rank7/8 and the strict positive q∞ 400m conditional test margin. Stop/falsify on a rival class with greater exact endpoint score, disagreement in source source SHA or unexpected nonzero beta_cal derivative in five-only observer.

FINAL: ORIGINAL_M13_SOURCE_NATIVE_EXEC_PASS / ALL_21846_SITE_PAIRS_78_EXACT_CALIBRATION_ENDPOINT_CLASSES_PASS / BOTH_SOURCE_OPTIMA_UNIFORM_ALL_C_GE_0_PASS / BOTH_WINNER_Q_LOSS_LT_5PPM_PASS / FIVE_SOURCE_SHELL_ONLY_ALL78_Q_INFINITY_PASS / LOST_BETA_CAL_RANK7_RANK8_GUARD_PASS / INDEPENDENT_FULL_N41_CUBED_FFT_12_CALIBRATION_CASES_PASS / 2_COMPLETE_CLEAN_JSON_REPLAYS_11_FAILCLOSED_MUTATIONS_PASS / ZIP_CRC_16OF16_BYTES_15OF15_SHA_3OF3_ZIP_SCRIPT_REPLAYS_PASS / NEW_DIFFERENT_CELL_I1_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
