artifact_id: IW_XH_S6_ROT018_ORIGINAL_SOURCE_RANDOM_DIRECTION_ALLOCATION_250_BALANCED_PROTOCOL_CORRECTION_001_20261113
date: 2026-11-13
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
return_id: IW_XH_S6_ROT018_ORIGINAL_SOURCE_RANDOM_DIRECTION_ALLOCATION_250_BALANCED_PROTOCOL_CORRECTION_001_20261113
result_class: ACTUAL_ORIGINAL_AUTHOR_TASK_36000_SOURCE_NATIVE_INPUT_TRIALS / ORIGINAL_GENERATOR_RANDOM_DIRECTION_NOT_BALANCED / EXACT_FULL_SMALL_BATCH_RNG_AND_INPUT_CONTROLS / SOURCE_MODEL_PRIOR_36000_OUTPUT_ROWS_CONDITIONAL_PROJECTION_ONLY / MATERIAL_NEGATIVE_KNOWLEDGE
status: SOURCE_ORIGINAL_TASK_GEN_RUN_SUCCESS / REANALYSIS_SHA_PASS / ROT017_PRIOR_PROTOCOL_EQUIVALENCE_CLAIM_RETRACTED / NO_RNN_REEXECUTION_THIS_ROTATION
claim_ceiling: ORIGINAL_AUTHOR_TASK_SOURCE_RNG_AND_PARAMETER_DISTRIBUTION / PREVIOUS_ROT017_MODEL_SOURCE_OUTPUTS_ONLY / NOT_ORIGINAL_AUTHOR_FULL_NBATCH18000_RNN_REPLAY / NO_MONKEY_DATA / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE

# XH-S6 ROT018 — Correcting the claim that author N_batch=72*250 equals 250 samples per motion angle: it does not

## Executive material correction

ROT017 successfully executed the ORIGINAL author DotsTasks and PsychRNN model classes and trained weights, but built its own 250 separate source stochastic batches with EXACTLY the 72 different shown direction bins each. Therefore each shown direction was sampled exactly 250 times per model unit in ROT017.

The original author generator generate_microstim_testdata.py (exact original Git blob e7a6666e0b600ea49bab9755d302c78110ba9bc4, original author commit 7889a81e298c01532a313e02971c11dbc9eb8eb0) sets N_testbatch=72*250=18000, but passes fix_shown as all72 relative angles WITHOUT setting test1ofEach=True. In its MT Task constructor MT_broadInSharpOut_withR the ORIGINAL default is test1ofEach=False; consequently the original-source method generate_trial_params draws shown_deg = rng.choice(self.fix_shown) for EACH trial. This is an original-source random shown-angle protocol, NOT exact forced 250 per angle. The nominal count per angle has expected value 250 but its finite realized counts vary.

**WITHDRAW** the prior XH-S6 ROT017 description that 250 repetitions PER SOURCE ANGLE were native-author protocol equivalent to N_batch=72*250. Retain ROT017 36,000 actual trained-RNN data, genuine 17 and2 rare exceptions, pairing controls and qualitative model findings. ROT017 should be described as an independent **BALANCED DIRECTION STRATIFICATION** of original source classes, not a byte-identical author generator replication. This is an XH interpretation/protocol-comparison error, NOT an error of the authors.

## Original author firstness and exact method custody

The original scientific authors FIRST: Douglas A. Ruff, Sol K. Markman, Jason Z. Kim and Marlene R. Cohen, Information formatting in neuronal populations predicts differential functional contributions to behavior, Nature Neuroscience, published 10 November 2026, DOI https://doi.org/10.1038/s41593-026-02514-7 . Earlier MT microstimulation literature likewise predates XH. The original authors' simulation and monkey findings remain distinct and unaudited biologically here.

Original author public source https://github.com/solkm/formattingRNN/tree/7889a81e298c01532a313e02971c11dbc9eb8eb0. Source identified and exact Git blobs pinned before execution:
- python_code_data/generate_microstim_testdata.py git blob e7a6666e0b600ea49bab9755d302c78110ba9bc4, sets N_testbatch=72*250, original preference-relative shown set and original reward relative180;
- DotsTasks.py blob ac9e789c69a8ea46ac38303f9d0db524886ba0a9, source MT Task __init__ default test1ofEach=False and source generate_trial_params shown_deg=rng.choice(fix_shown);
- original psychrnn/tasks/task.py blob b3bc5a5ca3fb2b0d2b4b79a4cd5ce8930e142865: source per trial generate_trial_params() then generate_trial(), which consumes source MT time-step stimulus noise before moving to next trial;
- original circledots_fxns.py blob 909a65d84174a7eebb0e19273d06ae400dc9094f.

Crucial distinction: this ROT018 does NOT run original trained-network MT or dlPFC PsychRNN recurrent simulation. It runs the ORIGINAL source Task generator and per-step stimulus/noise generation as an executable input-scheduler audit, and uses genuine prior ROT017 trained-model outputs only for a separately labeled CONDITIONAL arithmetic projection. No original model weights are needed to sample original-source Task directions and RNG; original author model output and source Task stimulus distribution are not conflated.

## Prespecified and actually executed original source Task evidence

ROT018 preregistered source protocol before new Task execution at pinned GitHub commit 7a22a264f7cb1589270e6c220a9a38256a76dda7 Git blob 66171ec720d1ea3bd676ef21d336ae26fbfeaf4b:
https://github.com/wmakiela-tech/Nash-iw-research/blob/7a22a264f7cb1589270e6c220a9a38256a76dda7/research/xh-s6/2026-11-13/iw_xh_s6_rot018_original_source_random_direction_scheduler_vs_balanced_250_preregister_001.md

Original source Task tested for two source dlPFC-stimulation conditions: source unit25 preference160deg and reward center340deg, source Task pseudorandom seed1900000025; source unit53 preference295deg and reward115deg, source seed1900000053. Full source MT input/task noise MT in_noise0.4 and original coherence0.6 with source randomized ring/dots onset, N_batch18000, source shown=(pref+5deg step grid) mod360, original Task test1ofEach absent/default FALSE.

To preserve original RNG progression without holding multi-GB original x/y/m source input arrays, execute a source-equivalent stream, for every one of 18000 Task trials: p = original MT Task.generate_trial_params(1,i), then x,y,m = original MT Task.generate_trial(p), discard only returned arrays but retain p metadata. This consumes original source Task stochastic trial inputs and normal noise exactly in source order.

Before full source stream for EACH source condition, verified a 72-trial equivalence to the actual original Task.get_trial_batch: EVERY one of 72 parameter dicts exact, entire original source MT x/y/m arrays EXACT, and original DotsTasks.rng final state byte-identical. This identity holds for BOTH source conditions. Thus streaming is numerically faithful to the source's Task stimulus generation order; this is NOT a proof that the full RNN generator or its output would match when using a different batch shape.

First Actions run43474117898 failed after creating partial first-unit Task output because a local histogram variable named dots shadowed the imported original DotsTasks module alias needed by a final digest calculation. Failure marker AttributeError list has no attribute rng, NOT a source science failure. Original protocol and source RNG untouched. A separate public source non-scientific correction incident was pinned before rerun, GitHub commit4f60169310cb9b4c656e0b27c39d775443de625c:
https://github.com/wmakiela-tech/Nash-iw-research/blob/4f60169310cb9b4c656e0b27c39d775443de625c/research/xh-s6/2026-11-13/iw_xh_s6_rot018_source_task_variable_shadow_pre_report_correction_001.md
Corrected ONLY local histogram identifier dots->dots_bins; no experiment source model or prereg alteration.

ACTUALLY COMPLETED ORIGINAL TASK SOURCE GENERATION:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43474692921
job132055339621, COMPLETED SUCCESS, original 36000 Task input trial generations executed source default random direction selection and all original source MT task noise steps, original-source 18000 per condition. Stream native Task stage elapsed132.0257 seconds. Full original 36000 trial parameter CSV, native Task summary JSON, 144 angle occupancy CSV and true runner stdout retained GitHub Actions artifact14063415512 (30 day retention) and actually downloaded. Full Task source CSV 1,701,966 bytes SHA256 **7c597cdd8a2c17cafcb55f2e7ccdd10423cacc7893068322c22036f0c21078ca**; original-runner native result JSON 9,264 bytes SHA256 **f08fb5d2b0ecd8a37a2aae2b25ad2b3bd5d968f9f98b23e69411ad2d15c1c5cc**. Source Task stdout and 144-per-angle CSV separately SHA-locked in attached ZIP.

Public exact Task runner script after technical fix READBACK PASS commit66923caf42df70e5b8c1c6235da0be61b3e55763 Git blob302495da93b1c527020494177c21f72db55295ff:
https://github.com/wmakiela-tech/Nash-iw-research/blob/66923caf42df70e5b8c1c6235da0be61b3e55763/research/xh-s6/2026-11-13/xh_s6_rot018_original_author_native_task_direction_scheduler.py
Actual read-only workflow readback PASS commit672dd83da470137852081aaf626872327eba2607 blob7866e983b732edf0a31947e5d0cac19247dd7c99:
https://github.com/wmakiela-tech/Nash-iw-research/blob/672dd83da470137852081aaf626872327eba2607/.github/workflows/xh-s6-rot018-original-source-random-direction.yml

## Actual source 18000-trial result: NOT forced balanced, but all 72 source directions present

| Original source condition | Native source Task trials | Mean per direction | Min count | Max count | Number of 72 count bins not exactly250 | Standard deviation counts |
|---|---:|---:|---:|---:|---:|---:|
| source dlPFC25 P160deg | 18000 | 250 | **218** | **278** | **70/72** | 14.5840 |
| source dlPFC53 P295deg | 18000 | 250 | **222** | **287** | **69/72** | 14.9043 |

Total 139 of 144 per-source-unit angle-bin counts differ from the ROT017 forced250. All72 original source directions were sampled in both native Task generator runs, all source reward angles match original expected P+180, source ring onsets from50..140ms and dots from450..540ms in10ms steps, all100 paired onset grid cells accounted and original 36k source task row identities were audited independently.

These two empirical direction count histograms directly corroborate the source-code-level absence of forced per-angle balance. Do NOT claim unique figures guaranteed by source code or that author paper necessarily used these XH seeds; source original paper does not specify these XH seed values. Statistically, original source directions each have ideal generator marginal probability 1/72, hence E[count]=18000/72=250; ROT017's forced250 is a distinct stratified method despite matching the expected count, not the realized draw.

## Conditional source-data projection ONLY, independently audited

ACTUAL ROT017 original AUTHOR-TRAINED RNN run was GitHub Actions43467831511, 36000 genuine stimulated/sham source model final choice pairs under controlled source noise and EXACT250 samples per direction. Source data CSV SHA256 **29f9b48d60b60c031fdca8a37483a969c2b470086f30f3ec5ebcbbb77c65530f** and original full runner JSON SHA256 **083db441c66dfb3ed4124be2742b34a5fd8ea03474d7a25d221851f5a99157f4**. Source original dlPFC25 had17 selected final model choices in annulus5..65deg, in shown angles190/195/200/205/210/215, counts4/3/3/5/1/1; source dlPFC53 had2, shown angles275 and280, one each. Those original actual model choices remain unchanged and correctly evidenced, regardless of upstream direction scheduler mismatch.

ROT018 computes a purely HYPOTHETICAL direction-occupancy projection, NOT new original model outputs: n_theta is actually observed count from NEW native Task source generator 18000-trial random-schedule stream; k_theta is ACTUAL ROT017 original RNN model gap event count among its250 simulated source-model responses for shown theta. At fixed observed per-angle rate k_theta/250, the occupancy-projected EXPECTATION of total source-model gap cases is:

E_projected = sum_{theta in 72 source bins} n_theta*(k_theta/250).

- Source dlPFC25: original balanced ROT017 real model gap count17; conditional occupancy projection EXACT rational **33/2=16.50**; difference -0.50 expected gap events in hypothetical randomized full Task source schedule.
- Source dlPFC53: original balanced real gap count2; conditional occupancy projection EXACT rational **252/125=2.016**; difference +0.016 expected gap events.

The projection is exact arithmetic under a NON-CAUSAL transfer assumption that the previous experiment's per-angle source-model empirical gap propensity applies to another independently drawn Task source schedule. It is not a new source-network simulation, not an actual author one-batch RNN output and not a certified stochastic distribution beyond these observed source model data. It says only that for these particular new source source Task angle counts, reweighting makes a SMALL difference to the estimated total rare-gap event count. Other RNG seeds/batch arrangements could yield different source real counts and the actual original one-batch RNN stimulation could yield different responses.

More generally, if all 72 angles are equally likely, E[n_theta]=250, so averaging the above projected counts over ideal random source Task direction schedules yields the same weighted mean as the ROT017 balanced 250-per-angle source model outcome, conditional on fixed per-angle rates. This expectation identity is elementary, not a new theorem and NOT equality of finite distributions or of original author neural model outputs.

## Independent actual full-source input and prior neural-output audit

A separately written Python standard-library-only independent auditor executed locally on the ACTUAL source native Task-generated 36000-row CSV PLUS genuine prior ROT017 native neural-model 36000-row source CSV. It checks exact original file SHA256 identities before reading, verifies every source unit/seed/trial index/selected-angle/relative-angle/reward and onset parameter, unique 18000 trial IDs per source unit and complete original author 10x10 onset grid, recomputes all 144 source per-angle counts and source original Task summary mean/min/max/sd, independently confirms ROT017 exact 250 per angle and all source real model 17 and2 gap numerators, and derives conditional projection exactly with fractions.Fraction.

True independent local audit source:
analyze_rot018_independent.py (stdlib, actual execution).
Verified THREE generated output files via clean isolated rerun: 2 numeric CSV and 1 detailed JSON BYTE IDENTICAL to original analysis; exact original source images/models unused.
Three material negative mutation tests actually executed: truncating ORIGINAL source-task CSV, altering source-task original JSON, and truncating actual prior original model ROT017 CSV; all rejected BEFORE any science calculation by input SHA identity fail-closed. 3/3 PASS.

Full local user evidence ZIP ACTUALLY CREATED and VERIFIED:
IW_XH_S6_ROT018_ORIGINAL_AUTHOR_TASK_RANDOM_DIRECTION_CORRECTION_REPRO_20261113.zip
**1,403,799 bytes**, SHA256 **73f8df7dadb36b3d4fda50f82c3d50ab00eacbe74c1dc8accb9b383b128e7bd6**; ZIP CRC PASS, all **12/12** internal payload SHA256 PASS, independent auditor/source output and previous real RNN output both present, 3 output files exactly replayed AFTER CLEAN EXTRACT to another temporary directory; 3 separate corrupted original inputs failed closed; includes original stdout, actual Task-generated 36000 source trial CSV, original source summary JSON and 144 occupancy CSV, actual prior model ROT017 CSV+summary, analysis script+three outputs, independent replay receipt, README and SHA manifest. Original authors' NPZ weights intentionally not redistributed; original frozen source Git and original executed Task rerun workflow are publicly pinned.

Original science model is not re-executed by replay ZIP, only independently recomputed source Task/output arithmetic against unmodified underlying source datasets.

## Scientific judgment and explicit anti-overclaim

**MATERIAL ROT017 PROTOCOL COMPARISON CORRECTION:** Original author N_batch=18000 draws 18000 directions RANDOMLY from72 allowed inputs; ROT017 250 evenly balanced repetitions per each direction, so the earlier equivalence wording MUST be withdrawn. Actual source-native two generator streams confirm count imbalance (70/72 and69/72 bins not exactly250). The source model's rare gap numerical events 17 and2 are real as recorded under its own balanced XH experiment and are not invalidated, but not evidence that the authors' exact original single-batch generator would yield the same exact observations.

The projected expected rare-gap event counts under these source Task input frequencies are 16.50 and2.016, near their original balanced17 and2. This provides a limited finite source-input allocation sensitivity result, nothing more. No new authors' source RNN final choice simulations were performed in ROT018. No monkey trials, no biological causal claims, no new theorem or neuroscience priority. Source original paper authors retain firstness. No independent reviewer, Moderator CANON or EXEC_SIGN. BW GITHUB_PENDING_BW_INGEST only, not accepted custody.

STATE: ROT018_ORIGINAL_AUTHOR_NATIVE_TASK_36000_PASS / ORIGINAL_INPUT_RANDOM_DIRECTION_GT_BALANCED_CORRECTION / INDEPENDENT_NATIVE_TASK_AND_PRIOR_RNN_72000_ROW_AUDIT_PASS / SOURCE_RNG_72_INPUT_TARGET_MASK_BITWISE_EQUIV_PASS / CONDITIONAL_PROJECTION_ONLY / CLEAN_ZIP_12_SHA_PASS / PUBLIC_GITHUB_AND_BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
