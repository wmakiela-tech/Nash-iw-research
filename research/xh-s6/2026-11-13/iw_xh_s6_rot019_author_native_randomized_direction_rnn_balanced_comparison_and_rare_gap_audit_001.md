artifact_id: IW_XH_S6_ROT019_AUTHOR_NATIVE_RANDOMIZED_DIRECTION_RNN_BALANCED_COMPARISON_AND_RARE_GAP_AUDIT_001_20261113
date: 2026-11-13
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
return_id: IW_XH_S6_ROT019_AUTHOR_NATIVE_RANDOMIZED_DIRECTION_RNN_BALANCED_COMPARISON_AND_RARE_GAP_AUDIT_001_20261113
result_class: ACTUALLY_EXECUTED_ORIGINAL_AUTHOR_TASK_PSYCHRNN_TRAINED_MODEL_72000_RNN_ARMS / TWO_SOURCE_UNITS_36000_PAIRED_RANDOM_DIRECTION_TRIALS / ALTERNATIVE_SOURCE_SCHEDULER_COMPARE / ORIGINAL_SOURCE_SHA_LOCKED_INDEPENDENT_36000_ROW_AUDIT / NEGATIVE_KNOWLEDGE
status: NEW_ORIGINAL_SOURCE_MODEL_EXECUTION_SUCCESS / ORIGINAL_RANDOM_ANGLE_SCHEDULER_CONFIRMED / MODEL_GAP_EVENTS_DLPFC25_13_DLPFC53_0 / ALL_ACTUAL_ROW_AND_REPLAY_CONTROLS_PASS
claim_ceiling: TWO_AUTHOR_SELECTED_DLPFC_SOURCE_MODEL_UNITS_SINGLE_PRETRAINED_MT_DLPFC_PAIR / ORIGINAL_SOURCE_TASK_SCHEDULER_IN_250_BLOCKS_NOT_ONE_18000_BATCH / NO_MONKEY_DATA / NO_NEUROSCIENCE_NOVELTY / NO_CANON / NO_EXEC_SIGN
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE

# XH-S6 ROT019 — New native original-author RNN outputs under RANDOM shown-direction sampling: 13 gap exceptions in dlPFC25, zero in dlPFC53

## 1. Original scientific priority and a deliberately bounded model question

Original authors FIRST: Douglas A. Ruff, Sol K. Markman, Jason Z. Kim, Marlene R. Cohen, Information formatting in neuronal populations predicts differential functional contributions to behavior, Nature Neuroscience, published 10 November 2026, DOI https://doi.org/10.1038/s41593-026-02514-7. The authors already experimentally and computationally characterized MT source directional bias and dlPFC winner-take-all-like choices. This XH experiment does NOT claim new biology or source-model mechanism.

Original model source, immutable Git revision:
https://github.com/solkm/formattingRNN/tree/7889a81e298c01532a313e02971c11dbc9db8eb0
Original MT/DLPFC Task classes and original vendored PsychRNN simulator were ACTUALLY EXECUTED with their original pretrained model NPZ files. Author original source Git blobs checked before model execution include DotsTasks.py ac9e789c69a8ea46ac38303f9d0db524886ba0a9, psychrnn/backend/simulation.py d187595af592a888192bfc2dde6f562776b88423, psychrnn/tasks/task.py b3bc5a5ca3fb2b0d2b4b79a4cd5ce8930e142865, original generator e7a6666e0b600ea49bab9755d302c78110ba9bc4, original trained MT weights c5e701740f8ab1d19ca07415c0de2d6e7f88c37f and dlPFC weights 47142e3dee920a759406136449f0b12f9ce752ee.

Source original generator sets N_testbatch=72*250 but uses default test1ofEach=False in original MT Task, which RANDOMLY samples shown motion direction from fix_shown on each source trial. ROT018 actually verified this original source scheduling rule by 36,000 author-native Task input trials. The previous ROT017 real trained RNN instead imposed exactly balanced shown directions with source Task test1ofEach=True and found source gap exceptions 17/18000 for dlPFC25 and2/18000 for dlPFC53. ROT018's alternative actual Task source frequencies yielded only HYPOTHETICAL model occupancy projected counts16.5 and2.016 under a different random seed, NOT new source RNN outcomes.

ROT019 is the first XH trial here to execute new ACTUAL original frozen author RNN with the ORIGINAL SOURCE RANDOM-SHOWN-DIRECTION rule, retaining the convenient 250 separately seeded 72-trial source batches. Exact source Task function random direction sampling is restored; the original author's single enormous N_batch18000 Task+RNN invocation is NOT replicated. This distinction is central: source batching, RNG sequence and selected models remain different from the paper's full generator.

## 2. Frozen scientific design and technical premodel repair

Original independently published pre-data preregistration commit301c2b93f8b1e901ba9ef257cb948401e99b89d5, immutable Git blob143b2a5de2481abbc96c1f89a4a1478350c17674:
https://github.com/wmakiela-tech/Nash-iw-research/blob/301c2b93f8b1e901ba9ef257cb948401e99b89d5/research/xh-s6/2026-11-13/iw_xh_s6_rot019_randomized_direction_author_native_rnn_preregister_001.md

Source-selected units originally authored in generate_microstim_testdata.py and parsed from source immutable AST:
- dlPFC unit25, source preferred160deg, source strength45, source reward center340deg.
- dlPFC unit53, preferred295deg, source strength45, reward center115deg.
Original source MT input noise0.4/recurrent0.2, dlPFC input noise0.2/recurrent0.2, coherence0.6, dt10ms tau100ms, original randomized source cue ring onset50..140ms and dots onset450..540ms. Model weights copied from exact pinned source files; selected one-hot dlPFC source unit W_in final channel set in BOTH sham and stim, strength0 versus45. Both arms share original source task RNG, recurrent Gaussian RNG, identical source shown angle and randomized onset.

New pseudorandom seed formula fixed BEFORE model output:
seed=2000000000 + 300071*unit + 1009*seed_block, source unit25 or53, block0..249, 32-bit NumPy legacy original source generator admissible including +171717 offset. Unused source seeds relative to ROT013/016/017/018. Exactly 250 separately seeded original Task source batches x72 RANDOM directions x2 stimulated/sham arms for each of two original units, i.e. **36,000 paired original model final choices and 72,000 actual Task/Simulator executions**. Per each unit total 18,000 source pairs, direction histogram now stochastic rather than 250 forced per direction.

Predeclared numerical measurements: genuinely randomized shown counts; true original unit-preference circular output gap count in inclusive 5,10,...65 degrees; separate d=5, d=65 and interior; actual stimulated versus identical-source-noise sham output choice changes; all72 possible pseudo-preference-label gap counts; prior ROT017 balanced real exceptions versus arithmetic conditional occupancy projection from ACTUAL new shown-angle histogram and prior real per-angle ROT017 source model gap rate; seed-block descriptive uncertainty; preservation of every counterexample and no threshold rescue. No acceptance of alternative labels as physically exchangeable null.

Engineering provenance negative control: first workflow run43519442977 FAILED before any source model trial, due a typo in FINAL shell test of original author Git HEAD. The original source was cloned and checked out at valid source SHA, but the test compared it against an incorrect truncated 40-hex reference in prereg/workflow prose. Public distinct PRE-DATA source identity correction: Git commit ee1c6cf21faef53a7482a268d69c4f4084ef728b, original Git blob2ab1da8b557761a0d620bcafea0d61c5bdb2a3f8:
https://github.com/wmakiela-tech/Nash-iw-research/blob/ee1c6cf21faef53a7482a268d69c4f4084ef728b/research/xh-s6/2026-11-13/iw_xh_s6_rot019_predata_author_git_sha_typo_correction_001.md
Fix changed ONLY HEAD equality comparison, no scientific thresholds/seeds/Task/model source. Source actual code already had exact real original author SHA. Metadata-only subsequent public source guard edits to prereg/engineering note added claim ceilings and GITHUB_PENDING_BW_INGEST, without changing the ORIGINAL frozen prereg Git blob. For reproducibility consult exact original run checkout commit, NOT assume current repo HEAD is the frozen experiment.

## 3. ACTUAL original-source trained-RNN execution and raw result custody

Successful GitHub Actions original SOURCE model run:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43519685618
Job132210545363 COMPLETED SUCCESS, original model 72,000 Task+PsychRNN arm executions and paired choice count36,000, runtime373.6864 sec. Author source exact original code, trained model NPZ Git identity and task parser passed before simulation. All **500/500** source sham-stim paired RNG consumption, task shown angle and onsets matched; **2/2** source sham output exact bitwise repeat; zero mathematical argmax margin theorem contradictions.

Actual source output archive GitHub Actions artifact ID14082757371 was ACTUALLY downloaded, ZIP CRC PASS. Its raw numerical files:
- FULL source model pair trial CSV 36,000 rows, 4,377,248 bytes SHA256 **0e1f904444cd35a656b52b56044f5d04b11165d60001b888b0e8195383f0630a**.
- FULL original native runner source result JSON 21,409 bytes SHA256 **ecbcbad9d19ba315393938a4784a3b0ace2a0e8a247773c413e4e51c2ddb0b1e**.
- Original native runner 500-block profile CSV SHA256 1add25199ad7eba5594582173d659360f1082f45ccdd99dd0b94f409ab7df3c5.
- Original source 144 candidate label counts CSV SHA256 6d3705c00a9f139a1f7574b34ae87ed824b206b87e53e742b0041c19cfbcf825.
- Original source runner stdout log SHA256 4499a6f8b2744c27dbd5a8834a7553348652136f6911465e9035791cb1969f3e.

Original source trained-RNN script published pinned GitHub readback PASS, commit d244d20c4400f4ea1d12c5b483106b75d40b4a12 Git blob11f79e7c56529a7f30a168e7fcc9ed53bc31f455:
https://github.com/wmakiela-tech/Nash-iw-research/blob/d244d20c4400f4ea1d12c5b483106b75d40b4a12/research/xh-s6/2026-11-13/xh_s6_rot019_original_author_random_direction_native_rnn.py
Actual executed workflow after pre-data source SHA correction Git commit8a855544b8356856f6d6270318530eb51ff49ca8 Git blob a0e1179b075ddc4efea08afc11d43f5ad0cd52b4:
https://github.com/wmakiela-tech/Nash-iw-research/blob/8a855544b8356856f6d6270318530eb51ff49ca8/.github/workflows/xh-s6-rot019-native-random-scheduler-rnn.yml

## 4. NEW real source model outcomes, not occupancy projections

Both source original dlPFC units were tested n=18,000 source random-direction input trials, same strength45, different unit preference and source reward reference. The selected model output winner S is the 5deg-bin argmax at the final timestep; sham B is exact same task/noise stream with zero stimulation. Exclusion gap is the previously retrospectively defined 5deg-65deg circular angular distance to true source unit preference P, NOT a novel biological sensory threshold.

| Original selected dlPFC unit | Old ROT017 balanced REAL model gap events | New ROT019 RANDOM source Task REAL model gap events | Strict d5..60 | Upper boundary d65 | Source sham choices in d5..65 |
|---|---:|---:|---:|---:|---:|
| dlPFC25 P160deg | 17/18000 | **13/18000 = 0.07222%** | 0 | **13** | 3475/18000 |
| dlPFC53 P295deg | 2/18000 | **0/18000** | 0 | 0 | 3359/18000 |

New source direction occupancy:
- unit25 72-bin trial counts minimum214, maximum283, 69/72 bins !=250; source actual stimulated choice changed vs matched sham in 12,827/18,000 pairs.
- unit53 72-bin trial counts minimum215, maximum309, 71/72 bins !=250; changed choices12,713/18,000.
Thus actual ORIGINAL source random shown-direction scheduling is active, rather than 72 fixed bins per batch.

All THIRTEEN source dlPFC25 forbidden-gap events select EXACTLY source model choice S225deg, d(225, original source P160)=65deg. They arise for original shown directions 185,190,195,200,205,210,215 degrees; among these 13 events **8/13 genuinely alter the matched sham final chosen bin** and **5/13 remain unchanged relative to sham**. Representative actual original-source counterexample: unit25, seed block12, source seed2007513883, trial26, shown215deg, ring onset100ms, dots onset490ms, sham choice240deg, stimulated choice225deg, d65deg. No new science inferred from these two scalar events.

New unit53 stimulated source selections had NO choices at nonzero circular d5..65. This does NOT restore an absolute empty-gap source-model property: the actual PRIOR ROT017 original model produced two DLPFC53 d5 choices and ROT016 produced a DLPFC25 d65 choice. All genuine model observations are retained. With zero events this particular finite sample, the simple 4000 whole-seed-block empirical bootstrap interval is [0,0], which CANNOT be interpreted as an upper bound on probability of an exception in future samples.

Neither unit25 nor unit53 true preference is an arbitrary coordinate: it is the UNIQUE MINIMUM gap-count angular test label among all 72 5deg pseudo preference labels for this particular source model sample:
- DLPFC25 actual label P160: gap13; the best WRONG 71 labels have at least325 events.
- DLPFC53 actual P295: gap0; the best WRONG 71 labels have at least1863 events.
These pseudo angle labels are not physically exchangeable stimulated-unit tuning curves. Do NOT attach 1/72 significance or infer a universal winner-take-all biology from them. Original source paper already described qualitatively analogous behavior.

## 5. ACTUAL model counts versus prior balanced source and new Task-occupancy arithmetic projection

ROT017 genuine balanced original-source trained RNN output CSV 36,000 pairs GitHub Actions run43467831511, SHA256 **29f9b48d60b60c031fdca8a37483a969c2b470086f30f3ec5ebcbbb77c65530f**.

An INDEPENDENT analyzer recomputed old k(theta) source gap events among EXACT250 model pairs at each shown theta. Given ACTUAL new ROT019 native random Task direction count n(theta), the conditional occupancy-projected COUNT is E=sum n(theta)*k(theta)/250, exact rational arithmetic:

| Source unit | Previous REAL ROT017 balanced count | Conditional projected count using NEW ROT019 shown-frequency | NEW REAL ROT019 RNN count |
|---|---:|---:|---:|
| DLPFC25 | 17 | **2109/125=16.872** | **13** |
| DLPFC53 | 2 | **49/25=1.960** | **0** |

ROT018 earlier projections 16.50 and2.016 applied to DIFFERENT actual source Task RNG draws in ROT018, and are not the ROT019 schedule-specific numbers. The projected model counts here do NOT constitute actual repeated experimental RNN decisions: they extrapolate old balanced model gap occurrence rates across different new random shown-direction occupancies. The new REAL source RNN results use independent stochastic source Task/recurrent noise draws and differ from projection by -3.872 and -1.96 respectively. Cannot isolate the causal effect of schedule vs random noise across two such unpaired source run families. Also source original one-batch RNN could differ further from both.

Descriptive seed-block bootstrap (4000 resamples of COMPLETE 72-trial original-source seed blocks, not individual choices) returns gap event fraction 95th percentile range unit25 [0.00033333,0.00116667] (0.0333%-0.1167%). Unit53 returns [0,0] due to all-zero observed 250 block counts; this is NOT a biological CI, nonzero probability bound, or proof of future absence.

## 6. Independent full source-output audit and negative controls

Actual original-source output archive downloaded and hashed before any model-output arithmetic. A SEPARATE executed Python stdlib-only source-output auditor inspected all **36,000 new actual model paired rows**, original two selected unit IDs/source strengths/source pref/reward, exact 250 source seed blocks x72 unique trial-index keys for each, original randomized source shown inputs and valid original-source ring/dots onsets, exact source sham/stim selected output bin and angular distances, every source row geometry and selected source-output argmax numerical certificate.

The same independent auditor read **36,000 OLD actual ROT017 real model source rows** from immutable prior evidence and verified those are EXACTLY250 per shown direction, and their true source gap events17 and2. It performed an alternative **72-bin circular histogram convolution** to independently reconstruct all 144 original unit x candidate-label gap counts and original source native runner summary counts. Every native source total, per-direction profile, all 13 true witness rows, every source block count and original runner's 72-label minima PASS. Scientific outcome was NOT hardcoded as a PASS condition; real counterexamples are conserved.

An initial independent audit-code draft compared CSV textual fields to native JSON integer fields for the original witness list and raised a TYPE mismatch without indicating a model data discrepancy. It was corrected before publishing final analysis by parsing only these witness fields as integers, with NO change to true model output data, source runner, stochastic seeds or threshold. The fully independent audit then passed all 36,000 actual source rows.

Independent executed result files generated, SHA256:
- full numerical JSON bdb572aa60039e1a325e364a9636c78d48aced0355e589e23d5aa102fb26b12f.
- source two-unit CSV 5926a871c7292df4df856040d689f000b51554df6d55475d05c670b5ecb66de0.
- 500 source-block independent CSV 6d255fb8eba731b2dddc8211130d194638adbc98981ea193a6e5c7fa2ea3f506.
- 144 circular label convolution CSV c9432db3fceb577e16f6f6b205f8b5100b675fc1b1a1619be08963ab88defcd5.
- 144 source stimulus direction/old model gap profile CSV 84611029d3f5a81d3d5631d99ef763b77c2e2aab754330a1ea30b5a183a60367.

Independent standard-library Python script SHA256 dd4f8ba71c1e455b36cfc5fb2b94600c5a62b6d85dcb756a4ba7436c175a3f32, independent offline package clean+mutation verifier script SHA256 686cf719889af14a3ada7a185ed2d12f7d3632fb56e55dde4324face19aeca6f.

Actual user-local source reproduction/archive zip generated:
IW_XH_S6_ROT019_ORIGINAL_AUTHOR_RANDOM_DIRECTION_RNN_REPRO_20261113.zip, **2,281,022 bytes** SHA256 **908b259c693e9c6b9bfb18be560126264c2eda2734549369ca46e7ea7be50c38**, with all five original native runner output files, prior unmodified real ROT017 model CSV, independent script and all five derived outputs, offline verifier, numerical execution receipt, source-first README and manifest. ZIP CRC PASS, **15/15** archived payload SHA256 PASS, clean EXTRACTED isolated execution reproduced FIVE independent files BYTE-IDENTICALLY, and three deliberately corrupted original inputs (new source RNN CSV, new source runner JSON, prior original RNN ROT017 CSV) each failed closed on original SHA identity, **3/3** NEGATIVE tests PASS. User ZIP contains real original model SOURCE output choices but does NOT redistribute trained source binary models or claim full reproducibility of trained RNN calculation without original author repo.

## 7. Public source custody, correction and scientific STOP

Machine-readable genuine original GitHub Actions runner source summary plus original raw source SHA, independent controls and limits has permanent GitHub WRITE+PINNED BYTE EXACT readback PASS:
https://github.com/wmakiela-tech/Nash-iw-research/blob/1fbbefef3e0a869346712d9d777112fa8e1f7696/research/xh-s6/2026-11-13/xh_s6_rot019_author_native_random_scheduler_actual_rnn_and_independent_audit_001.json
Commit1fbbefef3e0a869346712d9d777112fa8e1f7696, Git blob d33da4bae50f0d72be72016f84f0fb1fbd2099e5.

The full 36,000-row original Task+PsychRNN source RNN CSV is in the actual user-local ZIP and original temporary GitHub Actions artifact, NOT falsely claimed as a separately committed public GitHub CSV. The original authors' trained binary models remain at their pinned source repo.

Final source interpretation: both selected source dlPFC original units show a strong preference-centered lower-density region in their final MODEL chosen direction distributions, but exact universal emptiness of any 5..65 degree interval was falsified by earlier real author-model source runs and remains false. The actual new source RNN random scheduler yields 13 (all boundary65) and zero (finite sample) source gap events, respectively. Source angle allocation materially differs between balanced and random designs; effect of this allocation alone cannot be isolated from stochastic source sample differences. No independent biological neural effect inference, no novel attractor mechanism or paper priority claim, no full original single batch, no monkey data, no MT/dlPFC multi-area causal generalization.

Custody remains GITHUB_PENDING_BW_INGEST, not BW readback. No independent AUD2 or REC11 positive review, Moderator CANON, EXEC_SIGN or cross-cell task cascade. No physics transfer.

STATE: XH_S6_ROT019_ORIGINAL_AUTHOR_NATIVE_RNN_72000_SUCCESS / RANDOM_SOURCE_DIRECTION_ACTIVE / TRUE_RNN_GAP_DLPFC25_13_DLPFC53_0 / CONDITIONAL_NEW_OCCUPANCY_PROJECTION_16_872_AND_1_96_NOT_REAL / INDEPENDENT_NEW_36000_AND_OLD_36000_SOURCE_ROW_AUDIT_PASS / CLEAN_REPLAY5_AND_MUTATION3_PASS / ZIP15_SHA_PASS / BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
