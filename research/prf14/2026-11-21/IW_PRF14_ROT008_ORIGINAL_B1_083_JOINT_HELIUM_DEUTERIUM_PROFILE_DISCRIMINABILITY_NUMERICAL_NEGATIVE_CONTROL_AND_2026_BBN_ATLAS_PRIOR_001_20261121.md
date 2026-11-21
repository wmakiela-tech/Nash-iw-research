---
artifact_id: IW_PRF14_ROT008_ORIGINAL_B1_083_JOINT_HELIUM_DEUTERIUM_PROFILE_DISCRIMINABILITY_NUMERICAL_NEGATIVE_CONTROL_AND_2026_BBN_ATLAS_PRIOR_001_20261121
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
date: 2026-11-21 Europe/Warsaw
exposure: PUBLIC
class: SCIENCE_FIRST_PRIMARY_233_NETWORK_RAW_SOURCE / MATCHED_HELIUM_DEUTERIUM_PROFILE_IDENTIFIABILITY / SOURCE_NUMERICAL_NEGATIVE_CONTROL / MATURE_2026_BBN_ATLAS_PRIOR_ART
status: 224_PRIMARY_Y_HELIUM_SOURCE_RECORDS_EXACT / 8_PAIRED_D_H_SOURCE_REPLAY_PASS / DH_NUMERICAL_CONVERGENCE_HOLD / CONDITIONAL_GAUSSIAN_ONLY
claim_ceiling: NO_EXTERNAL_NOVELTY / NO_PHYSICAL_PBH_BOUND / NO_BBN_NATIVE_PRF_EXEC / NO_CANON / NO_EXEC_SIGN
---

# PRF14 ROT008 — Is the charge-source correction observable through deuterium once PBH beta is profiled against helium?

## 0. First: superseding evidence and new question

OWNER Badacz PREREG_083 / REVIEW_084 at 21 Nov 16:56 CET now ACTUALLY reports 228/228 Wu–Xu 10D Julia source calls, 233/233 PRyMordial network calls, seven frozen source-to-Yp gates PASS. Direct original report Git blob 60062f758838aa76e613a3dc2db69966b93192a5:
https://github.com/wmakiela-tech/Nash-iw-research/blob/87dea8624acbb8ad956a5db781f52deb5912be71/research/badacz/2026-11-21/IW_BADACZ_B1_NETWORK_THRESHOLD_TRANSFER_REVIEW_084_20261121.md

Owner FIRST results: D_net(E5−orig) at helium targets .251 and .2484 differs by <=.0135 dex over j22/38/62/90 (conditional SHIFT_ANCHOR_ROBUST); original absolute Wu–Xu-code-vs-network root shift at 2026 observational threshold is −.24 to −.59 dex (conditional TRANSFER_MATERIAL). Thus PRF14 ROT007 mathematical no-go against assuming target transport WITHOUT running a model remains true logically, while its numerical uncertainty is empirically resolved IN THIS OWNER RATE-ONLY PRyMordial MODEL. PRF14 recognizes this update without claiming ownership of native runs or physics firstness.

This new independent scientific test asks: when original Wu–Xu orig and E5 charge-split source models have SEPARATELY tuned unknown beta to predict IDENTICAL final helium, can a second independent light-element measurement D/H distinguish the source normalization? Existing owner REVIEW_084 analyzes Yp only; its raw network outputs preserve D/H. PRF14 makes an original read-only cross-observable analysis, POST-HOC, NOT a preregistered D/H owner endpoint.

## 1. Primary source identity and exact join audit

Directly fetched original Badacz output:
- 233 native PRyMordial source rows: research/badacz/2026-11-21/data/net083_raw.jsonl, Git blob 05f6f93eb4f53a95f5ad6fbe38609557bae04465;
- owner analysis: research/badacz/2026-11-21/data/analysis083.json, Git blob 236da6ba92113b4e461550ce3f8fbc4a72dd81bc;
- owner original manifest: research/badacz/2026-11-21/MANIFEST_SHA256_083.md, Git blob 01bdda5ed77b33b56affb6cffc364496b3db926a.

V8 live connected-source parsing actually executed: 233/233 unique IDs; 8 original curve groups x 28 points = 224 source-primary rows; every row's source Yp exactly matched owner analysis083 Y_net Float64 (224/224, max delta 0), all 224 raw D/H values finite and rc zero. The other nine rows are one no-rate baseline, four source-rate background controls and four network tolerance/stride controls. This validates correct source-data joins, NOT D/H numerical convergence.

Independent primary external literature: Anne-Katherine Burns, Inside the black box of Big Bang Nucleosynthesis: A comprehensive sensitivity atlas for the precision era, Physics Reports 1194 (2026) 1–40, DOI 10.1016/j.physrep.2026.07.001. Original author's GitHub README https://github.com/Anne-KatherineBurns/bbn-sensitivity-atlas (blob c7f8dbbc7ce970df40204cdecb4f616ef97e9b45) lists 2025 PDG D/H x1e5 = 2.508 ± 0.029, 2026 LBT Yp=.2458 ± .0013. Its response atlas covers 14 physics/cosmology parameters and 63 thermonuclear rates, two nuclear rate compilations and two weak normalizations. It is a MATURE nuisance-sensitivity host; critically it ALSO uses PRyMordial and is NOT an independent test of our network injections. The original README of its uncertainty budgets warns that the n(p,gamma)d impact on Yp can be ill-conditioned from cancellations; do NOT claim that this causes Badacz's present D/H variability.

## 2. New original-source matched Yp/DH result

For each j in {22,38,62,90}, each arm orig/E5, and each helium target y in {.2484,.251}, independently locate the UNIQUE upward original network Yp crossing along its 28 measured 0.05dex beta nodes. Interpolate the exact same bracketing SOURCE D/H linearly in log10(beta) with precisely the Yp crossing weight. This compares two DIFFERENT PBH beta parameter points that predict the SAME helium, not predictions at one fixed beta.

All D/H units in the table are D/H multiplied by 10^5:

| target Yp | mass index j | orig D/H x1e5 | E5 D/H x1e5 | E5-orig D/H x1e5 | diff / observed sigma=0.029 |
|---|---:|---:|---:|---:|---:|
| .2484 | 22 | 2.467493097 | 2.468094766 | +.000601669 | .02075 |
| .2484 | 38 | 2.471027518 | 2.468233890 | −.002793627 | .09633 |
| .2484 | 62 | 2.469447914 | 2.468614379 | −.000833535 | .02874 |
| .2484 | 90 | 2.465457288 | 2.467851434 | +.002394146 | .08256 |
| .251 | 22 | 2.480927838 | 2.482344325 | +.001416487 | .04884 |
| .251 | 38 | 2.481079295 | 2.481259198 | +.000179903 | .00620 |
| .251 | 62 | 2.482858311 | 2.482902698 | +.000044387 | .00153 |
| .251 | 90 | 2.480349093 | 2.482121896 | +.001772803 | .06113 |

Maximum source-interpolated D/H difference 0.0027936272037778487 units, merely 0.096332 of the 2025 PDG observational sigma. Four LBT matched Yp roots differ in beta by +.264499, +.276913, +.298441, +.301178 dex; sizable latent abundance shift does NOT imply independent composition observability.

FULL original-source derived 8-pair machine-readable witness (includes both original run IDs, exact Yp and D/H brackets and tolerance controls), created and provider readback PASS, commit a9eafdc2e79452cdbc6872af12db81e3a435121a, Git blob f5ba7df76763083f9d931575a94a42be6b9b9591:
https://github.com/wmakiela-tech/Nash-iw-research/blob/a9eafdc2e79452cdbc6872af12db81e3a435121a/research/prf14/2026-11-21/data/prf14_rot008_source_native_083_helium_deuterium_profile_8pairs_001.json

## 3. Exact conditional statistical discrimination lemma: with a profiled beta, two observables may be effectively one

Consider separately each pair of simple hypotheses H_orig: (beta_orig,j) and H_E5: (beta_E5,j), chosen to match one helium y. Only under an ADDITIONAL explicit hypothetical likelihood model: one aggregated, independent Gaussian D/H observation with common standard deviation sigma_D=.029 and mean equal to the EXACT source-interpolated model D/H (no theory error, no other distinguishing data), the equal-prior optimal classifier satisfies

KL(P_orig || P_E5) = (D_E5-D_orig)^2 / (2 sigma_D^2)

P_correct^optimal = Phi( |D_E5-D_orig|/(2 sigma_D) ), P_error^optimal = 1-P_correct^optimal.

For all EIGHT original-source matched pairs: KL <= .004640 and P_correct^optimal <= .5192081, so the two-point minimum error >=.4807919. The maximum separation case j38/LBT would require sigma_D <= .00084920 (in units D/H x1e5), an observational precision ~34.15 times stronger than .029 for 95% single-aggregate-observation equal-prior accuracy, EVEN IF the source D/H predictions were numerically exact.

This follows classical Gaussian signal detection and Le Cam two-point logic: under these conditional assumptions, one pair of sufficiently similar models bounds the worst-case discrimination of the larger composite orig/E5 families. Four different j are alternative PBH mass hypotheses, NOT four independent samples to aggregate. Observational helium error correlation, unknown nuclear input priors, additional observables, the PBH physical environment, and the true non-Gaussian likelihood are NOT included. Do not label the 51.9% figure as measured astrophysical power, a general no-go theorem for PBH, or a novel statistics result.

Mature sensitivity/covariance host: Burns 2026 PRyMordial atlas, which establishes large nuisance Jacobian directions. In an ideal Gaussian model with additional independent positive-semidefinite nuisance covariance C, information distance d^T(Sigma_obs+C)^(-1)d is <= d^T Sigma_obs^(-1)d, but this inequality does not prove our nuclear model or physical nuisance assumptions.

## 4. Strong independent source falsifier: D/H signal is below unvalidated numeric variations

The owner 7/7 PASS tested Yp and source-rate consistency, NOT separately D/H convergence. Original read-only network raw has:

A. No-rate baseline D/H x1e5 =2.460118924062718. The four beta=1e-30 source-rate native baselines returned:
- j22 2.461348886531145 (offset +.001229962);
- j38 2.462450378788216 (+.002331455);
- j62 2.4585064153000404 (−.001612509);
- j90 2.4568459808626417 (−.003272943).
Source rates are near zero at beta 1e-30, but a rigorous integral bound for their physical effect has not been supplied; the safe claim is the factual D/H null-control non-neutrality, NOT an attribution of all mismatch to solver error.

B. ACTUALLY EXECUTED owner tolerance / stride tests in the SAME source raw:
- Original j22 source run net_o22_1720 D/H=2.5049373990140715. Tightening the network solver tolerance changed Yp by +0.0000050042324 but D/H by **+0.0033598865852533**. Using every second rate point changed Yp by −0.00002609238 and D/H by +0.00239819010148.
- Original j62 source run net_o62_1940 D/H=2.4867574747557035. Tight tolerance changed Yp by −0.0000011054554 and D/H by +0.00191064781575; stride2 changed Yp by +0.000001940332 and D/H by −0.00010441709.

One actually measured same-model D/H tolerance perturbation .0033598866 EXCEEDS the largest source-arm matched-helium D/H separation .0027936272. Thus it is scientifically FALSE to infer a validated D/H discriminatory effect from helium PASS. Controls were at selected points near old threshold, not all eight LBT pairs; they cannot serve as uniform deterministic D/H error bounds. Result: SOURCE_EXPLORATORY_DH_NEAR_DEGENERACY_PASS / PHYSICAL_DH_SIGNAL_PRECISION_HOLD.

## 5. Source-first mature-host subtraction and experiment design

The broad phenomena — multi-observable nuisance identifiability, Gaussian two-point testing, BBN sensitivity Jacobians, ill-conditioned finite-difference response functions — are mature. PRF14 original contribution is only the new SOURCE-SPECIFIC cross-observable extraction and actual source numerical falsifier against overpromoting the unused raw D/H column. It is not a new cosmological physical law, PBH observed bound, author error, or external research novelty.

High-impact discriminating next scientific test: preserve exactly the original projected beta roots and actual source rate arrays and validate D/H independently at 2+ matched-root pairs (nuclear solver tolerance, rate grid, full BBN network). For a claim of resolving the E5 profile deuterium contrast, a proposed convergence goal is D/H x1e5 error much less than .0028, for example <.0005 at each of two roots; this is a DESIGN THRESHOLD, not a measured error bar. Then independent LINX or AlterBBN, with rate/weak-parameter matching, can decide if differences survive non-shared nuclear physics. PRF14 ROT007 already directly inspected LINX source and recorded tau_n=879.4 versus owner's 878.4 and eta_fac mapping; no LINX run was performed here because the complete libraries and data bundle are absent. The 21Nov 16:05 human Moderator general run authorization is now live, so no new per-run permission is required, but owner roles and claim signing remain unchanged.

Scientific priority for potential EXTERNAL novelty is GAP-005 generator systematic (HERWIG vs PYTHIA) and legitimate charge-resolved hadronic injection; OWNERS Badacz/Mech-S10. A systematic >=+0.27dex could mask or confound source split physically; the actual generator comparison is NOT performed here. PRF may independently study external source priors and conditional inference without appropriating native runs.

## 6. Reproduction levels and controls

ACTUALLY RUN inside connector V8: directly fetched 233 original JSONL rows and original source 8 x 28 Yp analysis; 224 exact source Yp matches; 8 matched-helium root and D/H calculations; four null baselines and two tolerance/stride controls. This is original-data independent analysis, not a re-execution of PRyMordial, Julia or BlackHawk.

ACTUALLY RUN local Python3 stdlib Gaussian arithmetic on the eight source-derived pairs, certificate PASS: /mnt/data/prf14_rot008/prf14_rot008_conditional_gaussian_certificate.py SHA256 0dfd41d0995255af593c3a1ae17dda2107dda61a6cf56d137f472b4167900671 and output /mnt/data/prf14_rot008/prf14_rot008_numeric_certificate.json SHA256 a1efad386abb850ecb5d50c8df322a84943fd5f30997f5cabf1b976ebc92887d.

Standalone Python full 233 file replay /mnt/data/prf14_rot008/prf14_rot008_joint_helium_deuterium_source_replay.py SHA256 f7a716756a495c6526129c78f7fec1d07f4e85a30cd6070f889e4a6e16a7c1d5, includes hard fail on original two Git blob identities. PY_COMPILE PASS; NOT EXECUTED ON ORIGINAL RAW LOCALLY due connector-only source availability. Original source processing DID run in V8. Distinguish these exact exposure and execution levels; there is no independent full BBN execution.

RETURN:
PRF14_ROT008 / OWNER_B1_228_NATIVE_AND_233_NETWORK_083_084_CURRENTNESS / 224_ORIGINAL_Yp_MATCH_EXACT / 8_MATCHED_Yp_DH_PAIR_PASS / MAX_MODEL_DH_DELTA_0P002794_LT_0P097_OBS_SIGMA / TOY_GAUSSIAN_MINIMAX_ACC_LE_0P51921 / OWNER_DH_TOL_DELTA_0P003360_EXCEEDS_MODEL_PAIR_SPLIT / DH_NUMERICAL_PRECISION_HOLD / LINX_I1_OPEN / GAP005_OWNER_ONLY / NO_NOVELTY / NO_PHYSICAL_PBH_BOUND / NO_CANON / NO_EXEC_SIGN.
