artifact_id: IW_XH_S6_ROT015_SOURCE_PREFERENCE_AXIS_PLACEBO_720_LABELS_AND_COVERAGE_NEGATIVE_CONTROL_001_20261113
date: 2026-11-13
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
return_id: IW_XH_S6_ROT015_SOURCE_PREFERENCE_AXIS_PLACEBO_720_LABELS_AND_COVERAGE_NEGATIVE_CONTROL_001_20261113
result_class: ORIGINAL_AUTHOR_NATIVE_MODEL_EXISTING_11520_OUTPUT_ROWS / EXACT_720_ALTERNATIVE_PREFERENCE_LABEL_CONTROLS / SOURCE_SHA_LOCKED_TWO_ALGORITHMS / COVERAGE_NEGATIVE_KNOWLEDGE
claim_ceiling: ORIGINAL_SOURCE_MODEL_FROZEN_FINITE_GEOMETRY_ONLY / NO_NEW_MODEL_EXECUTION_ROT015 / NO_ANIMAL_INFERENCE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN

# XH-S6 ROT015 — Can another angular label falsely reproduce the observed dlPFC preference gap?

## Scientific firstness and provenance

Original scientific host and FIRST: Douglas A. Ruff, Sol K. Markman, Jason Z. Kim and Marlene R. Cohen, Information formatting in neuronal populations predicts differential functional contributions to behavior, Nature Neuroscience, published November 10, 2026, DOI https://doi.org/10.1038/s41593-026-02514-7. The original publication had already described the qualitative dlPFC winner-take-all choice pattern and experimental monkey findings. There is no novelty claim for such behavior in ROT015.

Original author code https://github.com/solkm/formattingRNN at frozen commit 7889a81e298c01532a313e02971c11dbc9db8eb0. Original author-trained MT and dlPFC NPZ model source bytes were actually used by ROT013, with pinned source Task and PsychRNN simulator; source model execution GitHub Actions run https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43430223171 .

ACTUAL upstream author-source model data: 10 selected author units (5 MT, 5 dlPFC) x16 seeded blocks x72 shown motion directions, 11,520 stimulated/sham choice pairs, 23,040 source model executions in ROT013. ROT015 DID NOT REEXECUTE any trained neural model. The exact original-source-runner CSV SHA256 e6717506d9d2f1a7d65fd7b25741e01d54d3c75f53145e97541c98933274db84 and original-runner JSON SHA256 d55f5db10890f67435ea4b46b119d4aa53db78f367f66ee05cc791fdfa71b4ef were actually checked fail-closed before use.

## Test, explicit limits, self-sealing guards

ROT014 invalidated our own earlier self-sealing endpoint diagnostic: a no-op stimulated choice unchanged from sham falsely counts as passing the old sham-or-preference endpoint condition. ROT014 instead documented, among actual original model stim outputs for each of five dlPFC selected units, zero choices at nonzero circular distances 5 through 65 degrees from true original stimulated unit preference. This interval width was selected DATA-POSTHOC with full source outputs and is not an original author preregistered hypothesis.

ROT015 tests a negative coordinate labeling question. For EVERY one of original 10 source selected units, retain ALL actual original model output choices unchanged. Iterate a hypothetical preferred angle L over all 72 possible 5deg angular output bins. For each label L count actual stimulated outputs S with unsigned shortest circular distance in {5,10,...,65} degrees from L. Compare actual author source preferred unit P against all 71 incorrect angles. Also compare nonstimulated source sham choice outputs. These pseudo labels are NOT PHYSICALLY EXCHANGEABLE unit preferences; this is an exact finite angular placebo-control calculation, NOT a valid statistical label-permutation null. No permutation p-value or new causal effect estimate is claimed.

## Actual per-unit model-output results, n=1,152 original stimulated choices each

| Original source unit | True P | Stim gap 5–65° at P | Sham gap at P | Minimum stim gap at any of 71 WRONG labels |
|---|---:|---:|---:|---:|
| MT37 | 110° | 477 | 212 | 119 |
| MT4 | 255° | 414 | 210 | 72 |
| MT42 | 0° | 451 | 221 | 166 |
| MT25 | 205° | 482 | 202 | 45 |
| MT34 | 90° | 412 | 219 | 271 |
| dlPFC53 | 295° | 0 | 218 | 118 |
| dlPFC25 | 160° | 0 | 222 | 21 |
| dlPFC54 | 15° | 0 | 233 | 115 |
| dlPFC8 | 140° | 0 | 210 | 89 |
| dlPFC9 | 75° | 0 | 184 | 93 |

For EACH of 5 dlPFC source units, the ACTUAL original source preferred direction is the ONLY one of 72 tested labels with zero stimulated choice events in the 5–65deg annulus. All 71 incorrect labels have STRICTLY POSITIVE counts. None of five source MT units has even one such zero-annulus label, including its own actual preference. This is an exact finite source-sample property, not a general result for unselected trained units, other trained networks, other parameters or real monkey data.

## Internal seed-block and stimulus-support negative controls

The source data were also divided by seed-block index into early8 and late8 of the 16 original source blocks (each half n576 original source choices per selected model unit). The original preference is the only zero-annulus label in BOTH halves for all five dlPFC units. Leave-one-seed-block-out: all 16 of 16 leave-one-block-out partitions preserve the unique actual zero label in every dlPFC original unit.

However these are NOT fresh confirmatory holdout samples: ROT014 selected the 65deg width on the entire 16-block source set BEFORE ROT015. These splits are merely within-sample support/sensitivity checks and cannot assign a statistical significance level to the result.

A separate negative support test divided actual shown directions into first half 0–175deg and second half 180–355deg; each subset has 576 actual original source stimulated choices per unit. MULTIPLE pseudo-labels can then have zero stimulated-annulus count: number of zero candidates in first/second directional half is dlPFC53 3/2; dlPFC25 11/7; dlPFC54 9/8; dlPFC8 11/4; dlPFC9 1/19. Thus unique preference-axis identification by this finite gap requires adequate original full circle source stimulus-direction coverage; it is NOT a guarantee under arbitrary restricted stimulus support.

## Independent executed reproducibility and custody

ROT015 independent pure-standard-library Python source audit SCRIPT 1 rechecks original source CSV/JSON bytes SHA256, all 11,520 original rows, original unit/strength/preference/reward and random onset supports, output 5deg bin and previous source model result count identities. It recomputes 720 exhaustive original-source unit/candidate-angle placebo records, ten unit profiles, twenty seeded half-block records, 16 leave-one-block-out controls and full numerical JSON. A fresh clean directory second execution reproduced FOUR output files BYTE FOR BYTE IDENTICALLY.

An INDEPENDENT second Python calculation uses a discrete 72-bin circular frequency convolution rather than the first implementation's geometric distance/gap function. For each label it sums 13 left and 13 right adjacent output bins, independently verifying 720 unit/label rows x four source data subsets (stim, sham, early8, late8): all 2,880 integer results match exactly. Two material mutation tests: tampered original CSV and tampered original runner JSON were independently rejected before any analysis with SOURCE_IDENTITY_FAIL. Both negative integrity controls PASS. The code DOES NOT assert positive scientific hypothesis as a prerequisite for successful execution.

ACTUAL user-local complete reproducibility archive: IW_XH_S6_ROT015_SOURCE_PREFERENCE_PLACEBO_720_LABELS_REPRO_20261113.zip, 478494 bytes, SHA256 17def0f9fd208e32ac0cc6afaef0806501a1fc23f68ea352657764f5acef2afb, CRC PASS, all 12 archived member SHA256 PASS. Contains the REAL 11,520-row original-source-runner CSV and original JSON, both independently run Python scripts, 720 unit-label records, ten-unit and 20-split tables, directional-half coverage negative control, numerical summary, verification receipts, README and SHA manifest. The original author pretrained binary weights remain at pinned original author Git revision rather than being redistributed.

PUBLIC machine-readable exact per-unit certificate GitHub write/readback PASS:
https://github.com/wmakiela-tech/Nash-iw-research/blob/10ba2f4e489f230fb5f267b6a82ae41729925f47/research/xh-s6/2026-11-13/xh_s6_rot015_source_preference_placebo_720_labels_certificate_001.json
Original-source numerical CSV available in attached user artifact, not falsely claimed as an independently published GitHub CSV.

## Scope and scientific verdict

The finite source RNN data-conditioned 5–65deg angular gap from ROT014 is uniquely anchored at the author-source preference P of each selected dlPFC unit among 72 tested possible output-bin angles. This helps rule out an ARBITRARY angular coordinate label as an equally empty interval for these exact full-circle source outputs. It cannot support a permutation significance claim, because labels are not physically interchangeable, nor a prospective holdout claim, because interval width was tuned on the full same source data. If stimulus directions are restricted to half their original source support, the zero-gap label may not be unique.

The original author paper already had winner-take-all firstness; this new work is a bounded source-data geometry/provenance control, not new neuroscience or model training, not original published 250-repetition per direction experiment and not monkey data.

BW only GITHUB_PENDING_BW_INGEST. No external referee acceptance, moderator scientific adoption, CANON or EXEC_SIGN. No new task cascade or physics bridge.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE.
