artifact_id: IW_XH_S6_ROT013_ALL_TEN_ORIGINAL_MODEL_UNITS_REWARD180_GEOMETRY_FALSIFIER_001_20261113
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
return_id: IW_XH_S6_ROT013_ALL_TEN_ORIGINAL_MODEL_UNITS_REWARD180_GEOMETRY_FALSIFIER_001_20261113
result_class: ACTUAL_ORIGINAL_AUTHOR_TRAINED_RNN_TEN_UNIT_SOURCE_23040_RUNS / INDEPENDENT_11520_CASE_AUDIT / SOURCE_METADATA_PARSED_FROM_AUTHOR_AST / UNIT_HETEROGENEITY_FALSIFIER / NEGATIVE_KNOWLEDGE
status: ACTUAL_SOURCE_MODEL_EXECUTION_COMPLETED_SUCCESS / PER_UNIT_FINITE_SAMPLE_FALSIFIERS_5_MT_AND_5_DLPFC_OBSERVED_PASS / DLPFC_UNIT9_BLOCK_SENSITIVITY_BORDERLINE / 11520_ROW_POSTPROCESS_AND_NEGATIVE_SHA_GUARDS_PASS
date: 2026-11-13
claim_ceiling: ORIGINAL_AUTHOR_TEN_SELECTED_SOURCE_UNITS_STRENGTHS_REWARD_REL180_16_BLOCKS / NO_AUTHOR_FULL_250_REPS / NO_MONKEY_DATA / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE

# XH-S6 ROT013 — Original 10-unit source-native trained RNN heterogeneity test, 23,040 executions

## 1. Original scientific priority, background and distinctive question

The original author SCIENTIFIC HOST and FIRST: Douglas A. Ruff, Sol K. Markman, Jason Z. Kim and Marlene R. Cohen, Information formatting in neuronal populations predicts differential functional contributions to behavior, Nature Neuroscience, published 10 November 2026, DOI https://doi.org/10.1038/s41593-026-02514-7 . Their published paper reports the experimentally observed MT microstimulation direction bias and dlPFC winner-take-all-like effects and uses a trained two-module RNN to generate qualitative predictions; the authors distinguish qualitative model agreement from quantitative experimental replication.

Much older independently established prior art: C. D. Salzman, K. H. Britten, W. T. Newsome, Cortical microstimulation influences perceptual judgements of motion direction, Nature 346,174-177 (1990), DOI https://doi.org/10.1038/346174a0; and C. D. Salzman et al., Microstimulation in visual area MT: effects on direction discrimination performance, J Neurosci 12(6),2331-2355 (1992), DOI https://doi.org/10.1523/JNEUROSCI.12-06-02331.1992. No scientific firstness claimed by XH.

XH-S6 ROT011/012 had controlled only selected original RNN MT unit37 and dlPFC unit53. A negative, falsifiable missing condition remained: do source-model discrete choice geometries persist across ALL five source-author selected units of EACH original trained module, or were prior observations special to the two selected units? ROT013 deliberately returns to ORIGINAL author's reward_rel=180, after ROT012 varied the reward cue outside the authors' microstimulation generator.

## 2. Original source native code and immutable provenance

ACTUALLY EXECUTED author-native DotsTasks.MT_broadInSharpOut_withR, DotsTasks.DLPFC_combined, psychrnn.backend.simulation.BasicSimulator_linOut and BasicSimulator with author's original trained MT/dlPFC weight matrices. Author repository https://github.com/solkm/formattingRNN, immutable commit 7889a81e298c01532a313e02971c11dbc9db8eb0. Original pretrained MTbroadsharp_m10.npz Git blob c5e701740f8ab1d19ca07415c0de2d6e7f88c37f, and DLPFCcombined_m4.npz Git blob 47142e3dee920a759406136449f0b12f9ce752ee. Original generator python_code_data/generate_microstim_testdata.py Git blob e7a6666e0b600ea49bab9755d302c78110ba9bc4, original DotsTasks.py Git blob ac9e789c69a8ea46ac38303f9d0db524886ba0a9, original PsychRNN simulation.py Git blob d187595af592a888192bfc2dde6f562776b88423. Full original author source identities, model weights and ROT009 source wrapper blob 054299b6b0f0c0def7cfa6b3600d6f56665375ce were checked before source execution.

Instead of manually transcribing original stimulated unit list, the ROT013 runner parses frozen author's generate_microstim_testdata.py abstract syntax tree for all original MT_mstim and DLPFC_mstim unit, preference and strength arrays. It checks original sham+stim pairs and original reward_rel=180 degrees, and executes EXACTLY:
MT unit37 preferred110 strength11; unit4 pref255 strength10; unit42 pref0 strength10; unit25 pref205 strength11; unit34 pref90 strength12.
dlPFC unit53 pref295 strength45; unit25 pref160 strength45; unit54 pref15 strength45; unit8 pref140 strength45; unit9 pref75 strength48.
All reward centers original preference +180 degrees mod360.

Source nonzero input/recurrent noise values MT input0.4, dlPFC input0.2, recurrent0.2 each. Original source random ring/dots onsets allowed. Same source MT/dlPFC trained network pair for ALL ten units, not multiple independently trained biological modules. Each unit has 16 independent seeded blocks, all 72 task shown directions 0,5,...355deg, and precisely paired SAME source-generated input/recurrent random draws and onsets for sham versus stimulation. Original author generator rotates shown directions relative to preferred angle, while XH uses the same complete set of 72 absolute directions in sorted order; direction ordering differs, but no angle bin is missing. Original Task and PsychRNN source classes were actually called, not a custom recurrent equation implementation.

Actual GitHub Actions run https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43430223171, job 131901564479, COMPLETED SUCCESS. 10 units x16 seed blocks x72 shown directions x2 arms = 23,040 original-source model executions, 11,520 matched sham-versus-stimulation records, n=1,152 per unit. Original output includes full task state score margins, choice bins, source target at those selected output bins, and original stimuli random times. 160 identical paired stream/onset checks PASS, ten sham original-class repeat bitwise checks PASS, no violation of source argmax margin sufficient preservation condition.

Original runner ZIP artifact id14039556815 was actually downloaded and tested CRC PASS. Original-source-runner CSV 2,018,806 bytes, SHA256 e6717506d9d2f1a7d65fd7b25741e01d54d3c75f53145e97541c98933274db84; FULL original source runner summary JSON 29,555 bytes, SHA256 d55f5db10890f67435ea4b46b119d4aa53db78f367f66ee05cc791fdfa71b4ef. Source data actually produced by author model, not synthetic winners.

Original-model executable script published GitHub pinned byte exact readback PASS: https://github.com/wmakiela-tech/Nash-iw-research/blob/074b73c47dc123caec2c29e004f0bc8a66a8a6ee/research/xh-s6/2026-11-13/xh_s6_rot013_source_native_all_ten_original_units_falsifier.py ; Git blob 0cd2658ed6687380935ab5d8d6f2d9c4b591b0c8.

Actually used read-only GitHub Actions workflow pinned byte exact readback PASS: https://github.com/wmakiela-tech/Nash-iw-research/blob/05dfd60e5448e8396bf21178a22cb7b137cfa7b6/.github/workflows/xh-s6-rot013-all-ten-author-units.yml ; Git blob 4cf687a5d1ace7709a153cfa60af6a313bba7c50.

Original-source runner's actual runtime numerical JSON parsed from observed job stdout markers, permanently published as a separate public machine file with pinned readback PASS:
https://github.com/wmakiela-tech/Nash-iw-research/blob/7730119495e394ed3bc50cbfa81ff11eeb0d8c87/research/xh-s6/2026-11-13/xh_s6_rot013_actual_source_runner_10unit_summary.json
Git blob 81cb589604a6d1a0e4d23a3abb2510ca73a314ab.

## 3. Predeclared source-model operational diagnostics and circular ambiguity guard

For source final model winner B (no stimulation) and source final winner S (same original RNG plus stimulation), with original unit preferred direction P, define circular unsigned angle distance d(x,y)=abs(((x-y+180) mod360)-180).

MT diagnostic: strict INTERIOR of the UNIQUE shortest circular arc from B to P requires 0<d(B,P)<180, 0<d(B,S)<d(B,P), and d(B,S)+d(S,P)=d(B,P). B=P (degenerate) and exactly antipodal B-P=180 (two equally short semicircles) MUST be removed from the eligible denominator; no false unique-arc geometry is inferred from these cases. Unit-level threshold XH predeclared: strictly more than half eligible source model choices are unique-geodesic intermediate.

dlPFC diagnostic: original model winner S exactly equals B OR exactly equals original unit-preferred P. Unit-level XH threshold predeclared: strictly more than half of its n=1152 stimulated final source-model choices are such exact endpoints. These are XH's bounded numerical diagnostics, not the authors' published operational definition of vector averaging or a theorem about the biological attractor.

## 4. Exactly measured original model results (independent full-row reconstruction)

| Unit | Source strength | Strict unique-geodesic interior | Exact B-or-P endpoint | Exactly preferred P |
|---|---:|---:|---:|---:|
| MT37 | 11 | 978/1134 = 86.24% | 2/1152 = 0.17% | 0/1152 |
| MT4 | 10 | 990/1151 = 86.01% | 82/1152 = 7.12% | 0/1152 |
| MT42 | 10 | 1075/1150 = 93.48% | 22/1152 = 1.91% | 0/1152 |
| MT25 | 11 | 993/1123 = 88.42% | 48/1152 = 4.17% | 17/1152 = 1.48% |
| MT34 | 12 | 937/1120 = 83.66% | 58/1152 = 5.03% | 0/1152 |
| dlPFC53 | 45 | 108/1119 = 9.65% | 686/1152 = 59.55% | 361/1152 = 31.34% |
| dlPFC25 | 45 | 74/1121 = 6.60% | 892/1152 = 77.43% | 561/1152 = 48.70% |
| dlPFC54 | 45 | 83/1137 = 7.30% | 954/1152 = 82.81% | 470/1152 = 40.80% |
| dlPFC8 | 45 | 65/1133 = 5.74% | 986/1152 = 85.59% | 480/1152 = 41.67% |
| dlPFC9 | 48 | 94/1136 = 8.27% | 593/1152 = 51.48% | 475/1152 = 41.23% |

PREDECLARED FINITE-source diagnostic: 5/5 original author-selected source MT units have unique-intermediate majority, and 5/5 source dlPFC units have exact-endpoint majority. There is clear heterogeneity, and this finite count does NOT imply a universal all-unit or brain region theorem.

Critical CONDITIONAL SEED-BLOCK SENSITIVITY: independently reran 4000 deterministic bootstrap resamples of the ENTIRE 16 pseudorandom blocks per source unit (not 1152 independent direction choices), obtaining descriptive 95%-percentile intervals:
MT strict unique geodesic: MT37 [84.87,87.49]%, MT4 [84.90,87.22]%, MT42 [92.43,94.53]%, MT25 [87.18,89.59]%, MT34 [82.44,84.87]% — all remain above 50%.
dlPFC exact endpoint: dlPFC53 [57.47,61.72]%, dlPFC25 [75.26,79.43]%, dlPFC54 [80.99,84.81]%, dlPFC8 [84.03,87.15]%, **dlPFC9 [49.65,53.30]%** — last overlaps 50% and is borderline. Thus a robust whole-block majority is NOT confirmed for the fifth dlPFC unit. These are descriptive model-simulation bootstrap percentiles, not population confidence intervals for monkeys.

Additional MATERIAL NEGATIVE SOURCE KNOWLEDGE: ROT011 found zero exact-P choices for MT37 with original reward offset180. That is a true source-UNIT37 fact, but not a general MT model fact. NEW MT25 SAME author reward_rel180 source config shows **17/1152** exact preferred output bin choices. Therefore any broad extrapolation "MT never chooses exact preference" fails even without changing reward context, by changing original source stimulated unit.

Stochastic SHAM-only negative control: for each original source unit we compared consecutive independently seeded sham source batches at matched shown direction (15 x72 =1080 pair comparisons per unit). Source model SHAM-only choice mismatch commonly 50–58%, despite ZERO stimulation, under changed noise and task onset. This is NOT 1080 i.i.d observations and does not measure a biological effect, but protects against treating any two unmatched source-model choice differences as an intervention.

All ten source model configurations yielded lower average original TRAINING TASK TARGET at final stimulated chosen bins compared with sham, but this target is not RNN output score or measured monkey reward and cannot identify biological performance impairment.

## 5. Independently executed second source-output audit and custody

Actual Actions artifact with full original 11,520-row output was DOWNLOADED to local container; ZIP original artifact CRC PASS. Independent Python standard-library auditor (NOT a model reexecution) actually executed and:
- fail-closed verified exact original runner CSV SHA256 e6717506d9d2f1a7d65fd7b25741e01d54d3c75f53145e97541c98933274db84 and actual full runner JSON SHA256 d55f5db10890f67435ea4b46b119d4aa53db78f367f66ee05cc791fdfa71b4ef;
- checked 10 original units, seed identity, 16x72 source directions for each, source unit/preference/strength/reward center, source allowed time grids, every final output 5deg bin, all actual source margin-preservation theorem assertions;
- re-evaluated source DotsTasks training target formula at EVERY SHAM and STIM final chosen bin and compared original runner result numerators, denominators, source-null mismatch figures and means for ALL ten units;
- reproduced 160 source seed-block profiles and original XH operational diagnostics, explicit exclusion of antipodal and degenerate choices;
- clean isolated reexecution of independent audit generated three output artifacts BYTE IDENTICAL to originals: 10-unit summary CSV SHA256 c39f9c35fc09e6a6523d3de210ef613b56506b2da0a97d79c5848c2550bd62a1; 160 seed-block summary CSV SHA256 dded0705c56e9151a2da8930d968ea9d668f826f1506b890edd72235f8cabb75; full independent JSON SHA256 19ff3f159b76ffd2a0c8076461291e52bf0f7aae8cd00cd7ac9b27e91441cc10.
- FALSIFIER guards: deliberately truncated/altered original CSV rejected with SOURCE_ORIGINAL_CSV_IDENTITY_FAIL; altered original runner JSON rejected with SOURCE_ORIGINAL_RUNNER_JSON_IDENTITY_FAIL, BOTH NEGATIVE CONTROLS PASS.

The actual local pure Python stdlib independent analyzer source SHA256 6db9284c574ec33c926ccdbad29e6cf0f0cd4f19da26eb542549cd2b49a40a7a. No unlicensed original author binaries redistributed. Full user-local original model evidence ZIP IW_XH_S6_ROT013_ALL_TEN_ORIGINAL_MODEL_UNITS_GEOMETRY_REPRO_20261113.zip, 471331 bytes SHA256 efe311fbfe5971985e5d5e701e95cf2a3b5f71a8cb72fbfdf804683d17397b9d, ZIP CRC PASS and 9/9 payload SHA256 PASS; contains actual model CSV and original runner JSON, own independent code, three derived results, README, stdout and manifest. Its full original source output remains accessible after transient GitHub Actions artifact 30-day retention as user-visible conversation artifact.

## 6. Scope and conditional stop

ROT013 is an original-author-source-model unit heterogeneity check on ONE frozen trained MT+dlPFC model pair, with ten author-selected stimulated units at their own original strengths, original reward_rel=180, 16 pseudorandom seed blocks. This is NOT the original author's 250 trials per direction and full MATLAB figure reconstruction. There are NO raw monkey trials, no independent causal biology evidence, no estimate of effect for biological cortical areas and no global mathematical or physical novelty.

The original source source-model structure qualitatively persists across curated author units, with a borderline unit9 and an MT25 exception preventing simplistic universal claims. Wider source-model robustness could be explored with further source-level original complete repetitions, but NO NEW TASK CASCADE is authorized. No independent referee approval, BW ingestion, Moderator adoption, or EXEC_SIGN inferred. Report remains GITHUB_PENDING_BW_INGEST.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE.
