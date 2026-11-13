artifact_id: IW_XH_S6_ROT011_AUTHOR_MODEL_CHOICE_GEOMETRY_UNIQUE_GEODESIC_AND_ENDPOINT_GATE_001_20261113
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
return_id: IW_XH_S6_ROT011_AUTHOR_MODEL_CHOICE_GEOMETRY_UNIQUE_GEODESIC_AND_ENDPOINT_GATE_001_20261113
result_class: INDEPENDENT_ACTUAL_AUTHOR_SOURCE_OUTPUT_POSTPROCESS + CLUSTER_BLOCK_GEOMETRY + STRICT_ANTIPODAL_GEODESIC_CORRECTION + NEGATIVE_KNOWLEDGE
claim_ceiling: ORIGINAL_AUTHOR_TRAINED_WEIGHT_NATIVE_ROT010_8640_ACTUAL_ROW_DOWNSTREAM_GEOMETRY / NO_FRESH_MODEL_RUN_ROT011 / TWO_ORIGINAL_SELECTED_SOURCE_UNITS_ONLY / NO_EMPIRICAL_NEUROSCIENCE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
status: ROT011_SOURCE_OUTPUT_GEOMETRY_REANALYSIS_COMPLETE / LOCAL_CLEAN_RERUN_THREE_BYTE_IDENTICAL_PASS / GITHUB_PINNED_REPORT_AND_CERT_READBACK
date: 2026-11-13
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE

# XH-S6 ROT011 — Source-native trained RNN choice-shift geometry: MT unique-geodesic interior versus dlPFC endpoint capture; exact 180-degree degeneracy excluded

## 0. Why this particular test and source-first framing

The authors' original *Nature Neuroscience* study, Douglas A. Ruff, Sol K. Markman, Jason Z. Kim and Marlene R. Cohen, Information formatting in neuronal populations predicts differential functional contributions to behavior (published 10 Nov 2026), DOI https://doi.org/10.1038/s41593-026-02514-7 , distinguishes MT stimulation biasing choices toward an intermediate direction from dlPFC stimulation giving winner-take-all-like choices. The authors have scientific firstness. The XH-S6 ROT009/010 response so far was mainly "did the final discrete choice change?" Such a raw flip rate is not the authors' principal geometry discriminator.

ROT011 instead re-analyzes the **actual previously executed** ROT010 original-source trained RNN outputs as directional choices on a circle. It does NOT start a new native model execution and DOES NOT use monkeys' behavioral records. Original author immutable repository solkm/formattingRNN@7889a81e298c01532a313e02971c11dbc9db8eb0 with original MT and dlPFC NPZ binary weights and original DotsTasks/PsychRNN classes. The original source ROT010 native model run is GitHub Actions run 43312500997:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43312500997

The actual full 8,640-row 4-arm CSV was downloaded in ROT010 and its original bytes rechecked here. Source file size 1,064,037B; exact SHA256 **a2fe3c9ba2a8fd48cb7fbfefa538409ccaa0fe1931da7c0f14acedbb08f3cf41**. Each row corresponds to 1 direction ×1 seed-block ×1 selected original model unit/strength, with four actually executed original Task+Simulator arms. 60 seed blocks each contain all 72 shown direction bins for each of two original source-selected units, n=4320 grouped conditions each; four arms yield 34,560 total native model simulations in ROT010. All stochastic source onsets and original input/recurrent noise were in ROT010; no newly invented final scores were created in ROT011.

Source model conditions:
MT original selected unit 37, stimulation strength11, preferred angle P=110deg, reward center G=290deg;
dlPFC unit53, stimulation strength45, preferred P=295deg, reward center G=115deg.
In BOTH, G=P+180deg mod360, so movement toward stimulated unit preference is simultaneously angular movement away from reward CENTER. Source task reward is a separate function depending on shown input and is not identical to closeness to G.

## 1. Predeclared operational geometry definitions and correction for nonunique geodesic

Unsigned circular shortest distance d(a,b)=abs(((a-b+180) mod360)-180), in degrees on the author's 72 output bins. Let B be actual native sham/base winner, S the actual same-seed stimulated winner, P the original selected model unit's preferred direction. Define:
- preference-directed: d(S,P) < d(B,P);
- exact endpoint: S=B OR S=P, an elementary finite-bin operational counterpart of "same winner vs preferred winner";
- near endpoint (10deg): d(S,B)<=10deg OR d(S,P)<=10deg;
- STRICT UNIQUE SHORT-ARC INTERIOR: d(B,P)<180deg (UNIQUE shortest geodesic), 0<d(B,S)<d(B,P), and d(B,S)+d(S,P)=d(B,P). This deliberately EXCLUDES antipodal B versus P, where there are TWO equal-length semicircles and no uniquely shortest arc. Cases with d(B,P)=0 also are ineligible for strict interior. The reported denominator below is all records with d(B,P)<180, including distance zero if present (no B=P present in this data).

An initial more permissive calculation counted 3719/4320 MT and 394/4320 dlPFC as "between on shortest arc" but included antipodal cases, which is ambiguous. **This has been explicitly corrected, not silently replaced**. 64 MT and 109 dlPFC base cases with d(B,P)=180 were excluded from the main unique-arc test. In the alternative seed-matched source pair, 64 MT and 121 dlPFC source baseline cases are antipodal and excluded. The corrected main rates are 3655/4256 MT and 390/4211 dlPFC, not 3719/4320 or 394/4320.

## 2. Exactly observed source-native source-model geometric results

PRIMARY SAME-SEED source-stim pair (A -> B in ROT010 source four-arm trial notation):
- MT source unit37: stimulation moved the selected final output closer to preference P=110deg in **4296/4320** source pairs (99.4444%), farther in 8 and same preference-distance in 16; mean preference distance delta d(S,P)-d(B,P)=**-38.916666666666664deg**, median absolute actual chosen direction change **45deg**.
- dlPFC source unit53: preference distance decreased in 1755/4320, increased in 1312/4320 and stayed unchanged in 1253/4320, mean delta **-17.11226851851852deg**, median absolute chosen direction change **10deg**.
- UNIQUE shortest-arc strict INTERIOR: **MT 3655/4256=85.88%** vs **dlPFC 390/4211=9.26%** (ambiguous antipodal endpoints removed, both source models measured with the identical geometric definition).
- EXACT endpoint S=B or S=P: **MT 13/4320=0.30%**; **dlPFC 2613/4320=60.49%**. Source dlPFC single EXACT preferred bin P=295deg in **1360/4320=31.48%**, whereas source baseline selected P in 0/4320. The other 1253/4320 endpoint cases retained exact control winner.
- NEAR within 10deg of either endpoint: MT **233/4320=5.39%**, dlPFC **3710/4320=85.88%**. This is an alternate operational threshold analysis, not an author-defined physical behavior categorization.
- MT exact unit preferred bin P=110deg occurs 0/4320 even after source stimulation. This is an illustrative source-model contrast against dlPFC's exact 295deg output capture, not a general statement that MT never produces choice preference capture for other units/strengths.

INDEPENDENT SOURCE-SEEDED MATCHED REPLICATION (C -> D in ROT010):
- MT shift in mean preference-distance delta **-39.074074074074076deg**, strict unique geodesic **3701/4256=86.96%**, exact endpoints **15/4320**, exactly P=110deg in 0/4320.
- dlPFC mean preference-distance delta **-16.53125deg**, strict unique geodesic **390/4199=9.29%**, exact endpoints **2603/4320**, exact P=295deg capture **1333/4320=30.86%**.
- INDEPENDENT NO-STIM SHAM A -> C reference mean preference-distance differences are near zero: MT +0.12037037037037036deg; dlPFC +0.018518518518518517deg, even though approximately half of actual same-shown sham winner bins differ under independent noise and source onset.

The 60 seed blocks are distinct pseudorandom model streams, but 72 shown directions within a block are NOT treated as 72 independent observations. Deterministic nonparametric descriptive 10,000-resample bootstrap of WHOLE blocks yields 95% percentile intervals CONDITIONAL on this source simulation:
- MT source preference-distance mean delta [-39.2292,-38.5880] deg; unique strict interior rate on non-antipodal comparisons [85.21%,86.56%].
- dlPFC source preference-distance mean delta [-17.5741,-16.6458] deg; unique strict interior [8.62%,9.92%]; exact preferred bin capture fraction [31.06%,31.90%].
These are conditional computational variability summaries, **NOT animal confidence intervals or independent inference about area-level biology**. No new experiment was run to produce this postprocessing.

## 3. Source-meaningful dependence on motion direction

The original source preference P and shown stimulus angle are finite bins. Split by unsigned shortest distance d(shown,P):
- dlPFC near 0..45deg, 19 shown bins, 1140 seed-paired source trials: source stimulus after microstimulation exactly P in **1082/1140 (94.91%)**, independent same-condition alternative seed stimulation in **1073/1140 (94.12%)**. Control choice exact P in 0.
- dlPFC 50..90deg, 1080 records: exact P in 257; independent alternative exact P in 248.
- dlPFC 95..135deg, 1080 records: exact P in 21; independent alternative in 12.
- dlPFC 140..180deg, 1020 records: exact P in 0 for either source paired stimulation arm.
This is a highly direction-conditioned SINGLE BIN source-model capture, NOT a universal reward effect, a proof of neural attractor dynamics or evidence about monkeys. Original reward source bias in this test is fixed opposite the preferred direction, so reward-alignment comparisons with alternative reward placements were NOT performed.

MT preference-distance decreases in essentially all four shown-input-distance bands; bounded unique-interior geometry persists for source chosen directions, despite no exact P capture. The source binary model preferences and chosen directions have no external neural calibrator in this XH test.

## 4. Source identity, independent execution and reproducibility custody

Original authors SOURCE (frozen): https://github.com/solkm/formattingRNN/tree/7889a81e298c01532a313e02971c11dbc9db8eb0
ROT010 PUBLIC original-source four-arm wrapper:
https://github.com/wmakiela-tech/Nash-iw-research/blob/4fde0106e78090b4042f5bcbfc5153188c0d0c4/research/xh-s6/2026-11-12/xh_s6_rot010_four_arm_source_noise_attribution.py
Original-runner JSON actual job output publicly frozen:
https://github.com/wmakiela-tech/Nash-iw-research/blob/fe7f33e06e31bf129e57c223007b6f8750399668/research/xh-s6/2026-11-12/xh_s6_rot010_native_four_arm_60seed_actual_runner_summary.json
Original true 8640-row source CSV came from author-native execution run artifact 13985983625; was downloaded ROT010 and frozen in user-visible archive with exact source SHA256 locked for ROT011.

ROT011 independent analysis authored as a pure Python standard-library script (NO original author source re-run), 12,849 bytes, SHA256 **ff95ec8d4df28992b67c0099e8587f4c82fb416369ed38d8dd073b1cc3748675**:
- reads source original-runner CSV; checks SHA256 a2fe3c9ba2a8fd48cb7fbfefa538409ccaa0fe1931da7c0f14acedbb08f3cf41, full row count, source units/strength/reward, 60 blocks with exact 72 shown bins, 72 angular output bin validity, paired flip control, source reward antipodality;
- computes both paired stimulation source geometries, unrelated sham A-C control, exact endpoint and strict unique geodesic with EXPLICIT antipodal exclusion, shown-direction distance bands;
- resamples WHOLE seed blocks 10,000x with locked deterministic pseudorandom seeds; reports conditional descriptive 95% percentile bounds.
- runs without any external Python packages.
Actual CLEAN isolated re-run performed PASS: all THREE locally derived output files JSON+CSV+CSV matched prior outputs BYTE FOR BYTE. This is independently executed downstream source-output analysis, NOT newly executed original model dynamics.

Local output sha256:
- source summary JSON: 6f7fb63289e5f88aa5ac4df0f254a070abbf06c0b95509fb0dec7d33759ca862;
- by-shown-distance-band CSV: 266677b7680b15314baf10263ed4b3bd8f5bad320f5dc13f31e21e8e5bfe955e;
- by-60-seed-block CSV: c2c16b3c08ad61f8f56ba6ba40883b3092582c6aeac1ab5ef98238e603c17584.
- Full LOCAL user ZIP of original SOURCE 8640 row CSV + executed pure Python code + summary + by-band + by-block files + README + manifest:
IW_XH_S6_ROT011_ORIGINAL_SOURCE_CHOICE_GEOMETRY_REPRO_20261113.zip
SIZE **292520** bytes; SHA256 **c6d5f719b940bb37d44c5e29c327c574c683667febe9f92eb2537e880ecd8954**; ZIP CRC PASS and 6/6 member SHA256 PASS; manifest identities passed; clean rerun three exact files PASS.
Original author binary source weights NOT re-distributed in this data-analysis pack, and are not required to audit these existing original-source outputs. The source original author code was executed upstream ROT010 (not this turn).

Public JSON numerical certificate EXACT readback verified commit 1dd7c1464a57d0993510fbf830bcd8fbb78a93fb, Git blob 5ffff0f48f8bc9003ae11839f510186f3f5a77da:
https://github.com/wmakiela-tech/Nash-iw-research/blob/1dd7c1464a57d0993510fbf830bcd8fbb78a93fb/research/xh-s6/2026-11-13/xh_s6_rot011_source_choice_geometry_certificate_001.json

## 5. Scientific negative knowledge and claim ceiling

The bounded source-model signature is qualitatively consonant with the original authors' distinction: directed source-model choice shifts in MT (largely uniquely intermediate) versus source-model dlPFC often choosing one of two endpoints. Original authors have firstness for this behavioral/model distinction and experimental validation. This reanalysis provides source-typed finite-run geometry with an explicit antipodal guard and source-cluster sensitivity, NOT a new biological mechanism or mathematical novelty.

No general area-level causal difference can be estimated from two differently stimulated selected units. There is no comparison across different source reward-center placements (the two tested are fixed opposite the respective unit preferences). There is no source paper full 250-per-direction source stimulation, independent experimental monkey data, original publication figure reproduction or model retraining. A near-endpoint choice in our binning does not automatically mean a distinct attractor, and a unique-short-geodesic interior choice is not direct proof of algorithmic vector averaging of population states. Those require more source-specific mechanism/analysis.

No user task cascade, no physical PBH/Yp crossfront, no moderator adoption claim. BW state **GITHUB_PENDING_BW_INGEST** rather than receipt. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.

## 6. Status

ROT011 INDEPENDENT_ORIGINAL_SOURCE_OUTPUT_GEOMETRY_PASS / ANTIPODAL_SHORT_ARC_CORRECTION_PASS / BOTH_PAIRED_SEED_STREAMS_DIRECTIONAL_CONTROL_PASS / SOURCE_DATA_SHA256_PASS / THREE_BYTE_IDENTICAL_CLEAN_REPLAY_PASS / ORIGINAL_AUTHOR_MODEL_REEXECUTION_THIS_ROT_NOT_RUN / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
