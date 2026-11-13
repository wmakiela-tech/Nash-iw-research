artifact_id: IW_XH_S6_ROT017_ORIGINAL_AUTHOR_DLPFC_250_PER_DIRECTION_RARE_GAP_SOURCE_RATE_AUDIT_001_20261113
date: 2026-11-13
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
return_id: IW_XH_S6_ROT017_ORIGINAL_AUTHOR_DLPFC_250_PER_DIRECTION_RARE_GAP_SOURCE_RATE_AUDIT_001_20261113
result_class: ACTUAL_ORIGINAL_AUTHOR_TASK_AND_PSYCHRNN_72000_RNN_ARM_TRIALS / 36000_SOURCE_MATCHED_SHAM_STIM_ROWS / FROZEN_RARE_GAP_RATE_AND_DIRECTION_CLUSTER_DIAGNOSTIC / TWO_UNIT_COMPARATOR / INDEPENDENT_SOURCE_SHA_AUDIT
status: COMPLETED_SOURCE_MODEL_EXECUTION_SUCCESS / FROZEN_EXACT_GAP_ZERO_DISPROVED_BOTH_UNIT_SAMPLES / INDEPENDENT_ALL_36000_ROW_AUDIT_PASS / CLEAN_EXTRACT_REPLAY_PASS
claim_ceiling: SOURCE_NATIVE_ONE_TRAINED_MODEL_TWO_DLPFC_AUTHOR_SELECTED_UNITS / NOT_AUTHOR_ORIGINAL_18000_SINGLE_BATCH_RNG / NOT_ALL_TEN_SOURCE_STIM_UNITS / NOT_MONKEY_DATA / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEUROBIOLOGICAL_UPGRADE / NO_OWNER_TASK_CASCADE

# XH-S6 ROT017 — Source-native 250 repetitions per motion direction: original dlPFC25 shows 17 boundary exceptions, original dlPFC53 shows 2 near-preference 5-degree exceptions

## 0. Original scientific host, firstness and why this test matters

Original author scientific firstness: Douglas A. Ruff, Sol K. Markman, Jason Z. Kim, Marlene R. Cohen, Information formatting in neuronal populations predicts differential functional contributions to behavior, Nature Neuroscience, published November 10, 2026, DOI https://doi.org/10.1038/s41593-026-02514-7 . The author's original published science differentiates sensory MT preference-driven direction bias from dlPFC winner-take-all-like behavior, including experiments on monkeys and their pretrained RNN model. No priority or novel neuroscience discovery is claimed by XH-S6.

XH-S6 ROT014 retrospectively discovered an exact empty dlPFC source-output angular annulus d(stim-choice, stimulated-unit preference) in 5,10,...65 degrees based on an earlier sixteen-source-seed-block numerical sample. ROT015's all-72-label negative control was still on those SAME source data. ROT016 genuinely preregistered this inclusive 65degree boundary before running a new source-model holdout and FALSIFIED all-five-source-unit universal emptiness by a REAL dlPFC25 choice at 65 degrees. Thus the strict universal source-model zero-gap conjecture was already FALSE before ROT017, and ROT017 does not try to reinstate it.

**Distinct ROT017 science question:** In a new substantially larger source-model sample for original stimulated dlPFC25 and one author-source comparator dlPFC53, using 250 repetitions per each of the 72 shown motion directions, how rare and how direction/geometry-specific are source-model output choices inside the previously FROZEN 5..65degree interval? Both original-source units have original source strength45, and different original unit preference / source reward centers. The results describe one original author-trained neural network pair; these are not independent biological experiments.

Pre-execution frozen public scientific preregistration, GitHub CREATE+PINNED READBACK PASS at commit b81936dd06b83b44060b2b4db1d45ba2c7267d9d, Git blob 72a22b3b90831ff29674a8273068b24f97f5416d:
https://github.com/wmakiela-tech/Nash-iw-research/blob/b81936dd06b83b44060b2b4db1d45ba2c7267d9d/research/xh-s6/2026-11-13/iw_xh_s6_rot017_dlpfc25_53_full250perdirection_source_preregister_001.md

## 1. Source actual code and frozen data identity

Original author GitHub repository https://github.com/solkm/formattingRNN frozen exact commit 7889a81e298c01532a313e02971c11dbc9db8eb0. The ACTUAL code run invokes original author Task DotsTasks.MT_broadInSharpOut_withR and DotsTasks.DLPFC_combined with vendored original PsychRNN BasicSimulator_linOut and BasicSimulator, original author trained binary weights MTbroadsharp_m10.npz (Git blob c5e701740f8ab1d19ca07415c0de2d6e7f88c37f) and DLPFCcombined_m4.npz (Git blob 47142e3dee920a759406136449f0b12f9ce752ee). Original author DotsTasks.py blob ac9e789c69a8ea46ac38303f9d0db524886ba0a9 and original psychrnn backend simulation.py blob d187595af592a888192bfc2dde6f562776b88423. All original author source and weights Git identity checks performed BEFORE the model source simulation by pinned XH original-source wrapper, itself locked to Git blob 054299b6b0f0c0def7cfa6b3600d6f56665375ce. Original source generator generate_microstim_testdata.py blob e7a6666e0b600ea49bab9755d302c78110ba9bc4 parsed by original-source ROT013 AST parser pinned blob 0cd2658ed6687380935ab5d8d6f2d9c4b591b0c8; selected original-source units and strengths are not invented.

Original author source conditions:
- dlPFC unit25, preferred160deg, source reward center340deg, source stimulated-unit strength45.
- dlPFC unit53, preferred295deg, source reward center115deg, same original-source strength45.
- Original source relative reward alignment 180deg, source input noise MT0.4 / dlPFC0.2, recurrent noise0.2 each, original source randomized ring onset 50..140ms and dots onset 450..540ms, source coherence0.6 and frozen original weights.
- Source trial S is stimulated final choice bin; B is matched same-original-noise sham choice, P is ORIGINAL author selected source preference. Original selected neural model stimulation input column one-hot unit is identical in both sham/stim arms, with strength0 vs strength45 inserted through original source Task input.

**Protocol distinction of source priority:** Original author generator has N_testbatch=72*250 and a one-partial-source-batch invocation per tested stimulation condition, with its specific source random number progression and shown ordering. This XH experiment executes 250 separately seeded ORIGINAL 72-angle Task+Simulator batches, each with shown0,5,...355 once; sham and stimulation are paired with the same source original noise streams and random onsets. Thus it matches 250 measurements per shown angle, but is NOT a full exact original source-generator N_batch18000/RNG reproduction, even though it invokes ORIGINAL source Task, ORIGINAL PsychRNN and ORIGINAL trained NPZ. It also tests 2/5 dlPFC source selected units, NOT all 10 original stimulation conditions across MT/dlPFC.

New frozen RNG seeds per dlPFC original unit: source_seed = 1800000000 +300071*unit+1009*block, block0..249. All fit the original author's NumPy legacy seed range; they are distinct from prior source test seeds. Same random streams and original onsets within sham/stim source pairs, 250 full direction blocks/unit.

## 2. Actual model execution and source evidence

ACTUAL GitHub Actions source experiment run **43467831511**, job **132031592740**, COMPLETED SUCCESS:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43467831511

250 independent original-source seeded 72-direction batches x2 original selected source dlPFC units x2 stimulated and sham arms = **72,000 original Task+Simulator RNN arm trials**, **36,000 matched paired source task outcomes**, 18,000 each original source unit. Full original source code and binary pretrained Git blob identities PASS, 500/500 identical paired source input/recurrent noise and Task randomized onset checks PASS, 2/2 exact bitwise sham repeat controls PASS. No source chosen-bin argmax perturbation stability theorem violations. Actual runner elapsed model computation 362.983 seconds, one bounded actual Actions run, not a plan. Scientific exception events were recorded rather than treated as CI failure.

Actual source runner GitHub Actions artifact ID **14060275350**, downloaded and ZIP-CRC verified in local environment. Six genuine original-runner files:
- ORIGINAL 36,000-row source model sham/stim choices CSV, 4,750,376 bytes, SHA256 **29f9b48d60b60c031fdca8a37483a969c2b470086f30f3ec5ebcbbb77c65530f**;
- full actual source-runner native JSON, 24,136 bytes, SHA256 **083db441c66dfb3ed4124be2742b34a5fd8ea03474d7a25d221851f5a99157f4**;
- 500 original source seed block profiles CSV, 18,928 bytes SHA256 **1be72ed42340d60caa4a009b9248000d82c050bfd2936e1bd668951b6c5bf4c0**;
- full source 72 alternative angular label count CSV for unit25 and unit53 SHA256 **4c31fd73306d9c0c607b5378709604e5bae4dcc9676b589f0d69a4e9d46c9600** and **e562c89fac5b2e0f7e98d2ebf2fe4b06e95a3aaa7895f9bbdda855a6750c1a79**;
- original runner stdout log 2953 bytes.
Artifact has finite GitHub Actions retention. Original full source outputs preserved in attached user-local reproducibility ZIP, NOT claimed as a separate public GitHub CSV blob.

PUBLIC actual original-source experiment runner script pin/write/readback PASS, commit 18b4edb43a2350c9651c6426d6c7e34c692a731a Git blob bdf68a9fbc1c3ab721aea343d4334e03ae8230fe:
https://github.com/wmakiela-tech/Nash-iw-research/blob/18b4edb43a2350c9651c6426d6c7e34c692a731a/research/xh-s6/2026-11-13/xh_s6_rot017_author_native_250_per_angle_2units.py
Actual executed workflow GitHub readback PASS commit 09dc28e27823b3389ca7d14630021ce4d52ce23b blob e69479d940e3d555c74f6068ffc9d2f6d8c9009b:
https://github.com/wmakiela-tech/Nash-iw-research/blob/09dc28e27823b3389ca7d14630021ce4d52ce23b/.github/workflows/xh-s6-rot017-author-250-per-angle.yml

## 3. New original model numerical result — both units have nonzero source output annulus exceptions

Preregistered/source-frozen annulus: d(S,P) exactly one of 5,10,..65 degrees (inclusive). Every original output direction is a 5-degree bin. Fraction denominators 18,000 per original selected unit, correlated across shown conditions within original-source seed blocks:

| Original dlPFC unit | Stim gap d=5..65 | Strict interior d=5..60 | Upper boundary d=65 | Matched no-stimulation sham gap | Exact P after source stim |
|---|---:|---:|---:|---:|---:|
| 25, source P160deg | **17/18000 =0.094444%** | **0** | **17** | **3439/18000=19.106%** | 8752/18000=48.622% |
| 53, source P295deg | **2/18000=0.011111%** | **2** | **0** | **3291/18000=18.283%** | 5642/18000=31.344% |

**Critical negative knowledge beyond ROT016:** dlPFC25 exceptions are ALL precisely selected source-model output **225deg**, exactly d(225,160)=65deg; among the 17 source-model cases, ten have identical sham and stimulated selected final angle 225deg (not an intervention-induced *changed-choice* in that pair), while seven really changed relative to source matched sham. Source shown input angles for all 17 events are only 190,195,200,205,210,215 degrees; original author random task onset remains in valid source grid. This is a concentrated boundary signature.

For dlPFC53, the TWO exceptions are source-model selected output **300deg**, exactly **5deg** away from original preferred P295deg, under shown stimuli 275deg and 280deg, with source randomized ring/dots onsets valid. Both actually DIFFER from their same-noise matched original sham selected direction (240deg and245deg respectively). This is a near-preference neighboring output-bin exception, NOT a numerous collection of source choices at intermediate angular offsets of 20-60deg. It nevertheless independently FALSIFIES even the weaker *universal* exact-empty d=5..60 interval extrapolation. No retrospective cutoff shift to exclude 5deg or 65deg is admissible as a retained strict theorem.

Unit25 exactly changed choices 12,974/18,000, of which seven lie in frozen annulus; unit53 changed choices12,674/18,000, of which two lie in annulus. A COUNT OF ALL STIMULATED OUTPUTS with small distance is not identical to a stimulation-induced changed-choice rate. Under original-source independent sham-seed/null comparisons, source no-stim winners differ across 9,507/17,928 unit25 pairs and 9,922/17,928 unit53 pairs due to changed stochastic source noise/onset, independent of stimulation. These adjacent-seed comparisons are NOT independent animal observations.

Source choice preference-axis specificity remained strong descriptively: on the full original source 72-angle chosen-output grid, the source TRUE P has the UNIQUE lowest number of stim-gap choices among all possible 72 hypothesized 5deg angular labels, although it has NONZERO counts. For unit25 actual source P160deg has count17, while the next-lowest WRONG source angle label has count **298**. For unit53 actual P295deg count2 while next-lowest wrong angle label count **1836**. Those alternative labels are NOT exchangeable neuronal preferences, thus no permutation p-value, no causal mechanism deduction, no statistical novelty inference from label rank. ROT015's old assertion of unique ZERO must remain withdrawn for these new source samples.

Whole seed-block descriptive bootstrap, 4,000 prespecified re-samplings of complete 72-direction seed blocks (not 18,000 independent monkey trials): source unit25 95% percentile simulated event fraction interval **[0.0005000,0.00144444]** (0.0500-0.1444%); source unit53 **[0,0.000277778]** (0-0.02778%). The intervals are conditional model-repetition sensitivity, not i.i.d. biological confidence limits. A zero-event bootstrap resample does NOT repair ROT016 or ROT017 real counterexamples.

## 4. Independent actually executed 36,000-row source output audit, double geometry and mutation controls

ACTUAL runner archive DOWNLOADED and source files cryptographically pinned. An independently authored Python standard-library-only numerical auditor (NOT trained neural network reexecution) read and verified **ALL 36,000 actual original-source CSV rows**, matching original-source 2 selected units/strength/preference/reward, 250 exact blocks of 72 directions per unit, new original-source seed formula and range, source original allowed onset times, output discrete bins, source training target output value formula, every gap/count/argmax-preservation flag, original per-source-unit runtime numerical output summary counts, original source shown-direction and distance histograms.

It then independently recomputed full 72 angular label counts for BOTH selected original-source units using a **72-bin discrete circular histogram convolution**, mathematically different from the source executable script's per-angle shortest-distance implementation. All 144 labels' model stim and sham counts matched source runner 72-label CSVs; complete per-unit seed and shown-direction aggregations matched actual runner. The science outcome was not hardcoded to PASS.

An initial first audit-code draft omitted aggregate counting for the argmax-preservation certificate, resulting in an explicit audit-vs-source numerator mismatch. That **auditor aggregation bug** was fixed BEFORE publication and without modifying raw source model data or scientific thresholds, and the full independent auditor then passed all 36,000 rows. The auditable local re-execution source code preserves the final corrected check.

A fresh CLEAN isolated directory execution generated **FIVE derived artifacts BYTE FOR BYTE IDENTICALLY**:
- complete independently verified full JSON SHA256 **d2b4273af02486243fb20fdeb569b98eadca5a3d8df7d99daf5edd0b3eb1f216**;
- two-source-unit detailed CSV SHA256 **f65cb5e31bfff5765570a2a96f9499918c100668c230abc9f54434f1c4d65435**;
- 500 independently checked seed-block CSV SHA256 **60ad7c2a387f093d3dd423b03d8f81f6e87db511caf859419b3b86f01471f69b**;
- 144 shown-direction model rate CSV SHA256 **e107e31809b86385ae0267f21e061f83bbb18569d8be891b19082facee4bc54f**;
- 144 candidate label circular-convolution CSV SHA256 **b22dc1fe52db980125abfdeb8722bce023b17afe363ad944188fdf777dd02b7c**.

Two independent deliberately malformed input controls actually executed and correctly failed closed BEFORE numerical calculations: altered original-source CSV -> SOURCE_ORIGINAL_CSV_SHA_IDENTITY_FAIL; altered original-source-runner JSON -> SOURCE_ORIGINAL_JSON_SHA_IDENTITY_FAIL. The complete independent auditor source SHA256 **eafd0ae004027b5e3c70919a11b41db7b73d323835548a1b2536b44a112e18bb**; independently executed clean+mutation checker source SHA256 **24cbca0aeb28ccdc22fd7a05a677db5c5ff6661082f34597e652fcd62cdf5292**.

## 5. Reproducibility custody

Full ACTUALLY CREATED AND VERIFIED user-local original-model-output reproducibility ZIP:
IW_XH_S6_ROT017_ORIGINAL_MODEL_250_PER_ANGLE_RARE_GAP_REPRO_20261113.zip

**1,196,668 bytes**, SHA256 **66607c232aca82971731321810a3f81d00bb3abaa48aa9e5103b2f0176a3abdc**, verified ZIP CRC PASS, all **15/15** archived file payload SHA256 PASS, SHA manifest JSON SHA256 **962a683f53b8e7c0b0da0ca34347681f0316095f399698bceb0d44a4d72fcc6a**. The package contains the 36,000 REAL source model output CSV, full actual source runner JSON, 500 original model source-block profiles, actual 144 source labels and stdout, an independently executed no-dependency Python auditor, its five exactly reproducible outputs, another independent clean+mutation verification script, original run/audit receipt, detailed README and manifest. Source original trained NPZ and code are not redistributed; public commit-locked model replayer and workflow are linked for full original Task/Simulator regeneration.

The ZIP was extracted into a fresh temporary directory and its verification script ACTUALLY run: again confirmed all FIVE original-source-output audit files byte-identical and both deliberately tampered source files rejected, without any Internet connection or original trained NPZ binaries. This is proof of reproduceable independent downstream source-output audit, not proof that neural/monkey data are independently reproduced in this archive.

Original GitHub Actions artifact 14060275350 is transient (~30-day retention); the local ZIP is a user-visible conversation artifact. Public permanent GitHub report and machine source runner receipt are separately pinned, but the original full 36,000-row CSV is NOT falsely claimed to have been separately committed to GitHub.

PUBLIC permanent ACTUAL GitHub Actions model numerical summary extracted from original runner stdout, with original source CSV and JSON SHA and verified independent controls, pinned WRITE+READBACK PASS, commit9c12388db13e42dbf8a92ae573c05b5929b33b24 Git blob23c7422255be6ff28617b96e8e281c7440884db9:
https://github.com/wmakiela-tech/Nash-iw-research/blob/9c12388db13e42dbf8a92ae573c05b5929b33b24/research/xh-s6/2026-11-13/xh_s6_rot017_actual_native_250x72_two_dlpfc_units_runner_result_and_audit_001.json

## 6. Scientific verdict, anti-overclaim and stop rule

A SOURCE-SPECIFIC near-preference angular gap is numerically very strong in both original selected pretrained dlPFC RNN units under original-source stochastic inputs, but it is emphatically NOT exactly empty: 17/18,000 unit25 (all at d65) and 2/18,000 unit53 (both at d5). The hard bound 5..65 was already preregistered-and-falsified in ROT016; ROT017 reinforces that falsification rather than allowing a soft posthoc redefinition of the source cutoff. The selected angle P remains an unusual minimum-count axis among all 72 labels, but the source model itself is frozen and the source result is bounded, known neural architecture RNN artificial choice behavior, not a novel biological mechanism or universal attractor claim.

The original paper authors retain firstness, there is NO source-original single N_batch18000 trial batch replay, original experimental 250-per-direction random sequencing, all ten original units, independent trained network or monkey trial dataset in this ROT017 experiment. Descriptive seed bootstrap does not confer animal inference. No effect of intervention across biological areas, no new neuroscience theory, no mathematical innovation or physics/BBN/PBH bridge. BW GITHUB_PENDING_BW_INGEST is not proof of BW ingestion; no AUD/REC acceptance or Moderator scientific adoption, no CANON or EXEC_SIGN and no owner cascade.

STATE: XH_S6_ROT017_SOURCE_NATIVE_72000_MODEL_ARMS_SUCCESS / FROZEN_GAP_EXCEPTION_25_17_AT_65DEG_AND_53_2_AT_5DEG / TWO_TRUE_P_MINIMA_NOT_ZEROS / INDEPENDENT_36000_SOURCE_AUDIT_PASS / EXTRACTED_PACKAGE_15_SHA_PASS / CLEAN_REPLAY_AND_MUTATION_NEGATIVE_PASS / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
