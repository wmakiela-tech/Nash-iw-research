artifact_id: IW_XH_S6_ROT017_FROZEN_250_PER_DIRECTION_DLPFC25_VERSUS_DLPFC53_REPEAT_SOURCE_MODEL_PREREG_001_20261113
date: 2026-11-13
exposure: PUBLIC
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
status: PREMODEL_OUTCOME_FROZEN_BEFORE_NEW_TEST_EXECUTION
claim_ceiling: TWO_ORIGINAL_SOURCE_DLPFC_UNITS_AUTHOR_WEIGHTS_NATIVE_CLASSES_250_BLOCKS_X72_DIRECTIONS / NOT_AUTHOR_SINGLE_NBATCH18000_RNG_SEQUENCE / NO_MONKEY_TRIALS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN

# XH-S6 ROT017 — Preregistered source-native 250 repetitions per direction, dlPFC25 and dlPFC53

## 1. What is now known and what this DOES NOT rescue
Original host Ruff, Markman, Kim, Cohen, Nature Neuroscience published 10 Nov 2026, DOI 10.1038/s41593-026-02514-7, original publicly available trained model source solkm/formattingRNN immutable commit 7889a81e298c01532a313e02971c11dbc9db8eb0. The scientific firstness of dlPFC winner-take-all qualitative effects belongs to the original authors.

ROT014/015 found after-the-fact a gap of 5deg..65deg from the stimulated source unit's preferred direction in one prior 16-block source-model sample, but the cutoff was posthoc. ROT016 independently froze it before new source RNG and found ONE 65degree counterexample for original source unit dlPFC25 in 24x72 fresh pairs; therefore the universal exact-zero gap conjecture is already FALSIFIED. ROT017 must NOT report restored universal zero even if new sample has zero such events.

## 2. Exact fixed experimental design before data
Original trained MT and dlPFC NPZ source binaries, original DotsTasks MT_broadInSharpOut_withR and DLPFC_combined, vendored PsychRNN BasicSimulator_linOut and BasicSimulator, original source noise+random onset, original reward_rel180 and original source unit settings parsed from original frozen generate_microstim_testdata.py.

Two selected original source dlPFC units ONLY:
- dlPFC25, author source stimulation strength45, preference P160deg, reward center340deg (known near-boundary falsifier in ROT016);
- dlPFC53, author source stimulation strength45, preference P295deg, reward center115deg (comparator control from old source).
Original source input/recurrent noise MT .4/.2 and dlPFC .2/.2, coherence .6.

NEW RNG seeds, not reused: source_seed = 1800000000 + 300071*unit + 1009*seed_block where unit is 25 or53 and block=0,...,249. Seeds and source_seed+171717 are strictly less than 2**32; no modulo. The earlier ROT016 mapped seeds were ~748 million, ROT013 source seeds ~20 million; disjoint.

Run each original unit 250 distinct seeded 72-trial batches. Each contains the full 72 shown directions (0,5,...,355deg) exactly once; within each block execute SOURCE-NATIVE original sham and stim with exact common task onset and source input/recurrent noise streams. Total 2 units *250 blocks*72 directions = **36,000 paired trial outcomes** and 72,000 original source Task+Simulator model arms. This has the source generator's 250 repetitions PER DIRECTION, but NOT its one huge N_batch=18,000 batch or its specific original RNG draws, source order, trial sampling independence; does NOT claim full author generator replay or monkey dataset.

## 3. Frozen primary descriptive quantities, no posthoc rescue
Per selected unit report counts out of 18,000 source stimulated model winners with circular shortest distance from true source pref in EXACT set {5,10,15,20,25,30,35,40,45,50,55,60,65}deg. Report separately:
- exact d=65 boundary count;
- strictly internal 5..60 count;
- source sham null gap 5..65 count;
- exact stimulated preferred angle capture;
- actual changed choice count versus exactly paired sham.
- gap exceptions stratified by original shown direction and actual source random task times, with full row-level exact witness.
- 72 possible pseudo-preference labels counts; whether original P is unique minimum count, but DO NOT declare a permutation p-value because labels represent non-exchangeable unit identities. No universal original model gap claim.

All ZERO-event and NONZERO-event outcomes must be retained as actual data, with no science acceptance condition inside CI code. Report each unit and comparison; do not cherry pick. Distinct 250 seed blocks per unit, 72 linked direction trials per block. Descriptive block-resampling uncertainty is allowed, but no i.i.d. animal confidence interval or biological significance. Source-model results do not imply neuroscience novel discovery.

## 4. Source provenance and controls
Original author repository exact commit 7889a81e298c01532a313e02971c11dbc9db8eb0. Original generator git blob e7a6666e0b600ea49bab9755d302c78110ba9bc4; Task DotsTasks.py ac9e789c69a8ea46ac38303f9d0db524886ba0a9; simulator d187595af592a888192bfc2dde6f562776b88423; original MT weights c5e701740f8ab1d19ca07415c0de2d6e7f88c37f, original dlPFC weights 47142e3dee920a759406136449f0b12f9ce752ee. XH ROT013 unit parser exact Git blob 0cd2658ed6687380935ab5d8d6f2d9c4b591b0c8 and ROT009 original source simulator wrapper blob 054299b6b0f0c0def7cfa6b3600d6f56665375ce. All pins preflight checked before source model computation.

Source sham/stim paired RNG and onset digests same, one sham repeat per unit bitwise exact, original source task 72 directions all available, model output bins every5deg, model argmax sufficient margin theorem checked. No hardcoded expected science outcome as job PASS prerequisite. Preserve full source CSV, all 250 seed-block counts, 72 source-label counts and source-selected direction stratification, complete original model output JSON and stdout in actual runner artifact.

## 5. Negative knowledge / no automatic claim uplift
The old ROT016 one-event falsifier remains a permanent counterexample to exact universal zero gap, regardless of future trial results. ROT017 can only estimate a bounded, source model-specific *frequency* of the originally data-selected annulus exceptions with more original Task simulations, plus a limited within-trained-network comparison of two curated original source dlPFC units at equal source strength45. This is NOT an independent trained network, full paper neurophysiology, paper's one N_batch18000 trial draw, author manuscript reproduction, new equation or a neuroscience mechanism claim. No further owner tasks automatically created.

BW GITHUB_PENDING_BW_INGEST; NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE.
