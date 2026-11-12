artifact_id: IW_XH_S6_ROT009_AUTHOR_NATIVE_NOISY_PAIRED_MICROSTIM_SOURCE_GATE_001_20261112
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
return_id: IW_XH_S6_ROT009_AUTHOR_NATIVE_NOISY_PAIRED_MICROSTIM_SOURCE_GATE_001_20261112
result_class: EXECUTED_AUTHOR_NATIVE_NOISY_MICROSTIM_1728_COMMON_RANDOM_NUMBER_PAIRED_SOURCE_CONTROL_AND_INDEPENDENT_TARGET_POSTPROCESS
claim_ceiling: TWO_ORIGINAL_SELECTED_UNITS_AND_STRENGTHS_12_SEEDS_PER_72_DIRECTIONS__NO_FULL_SOURCE_18000_TRIALS_NO_ANIMAL_DATA_NO_NEUROBIOLOGICAL_EFFECT_SIZE_NO_NOVELTY_NO_CANON_NO_EXEC_SIGN
status: COMPLETE_BOUNDED_ACTUAL_ORIGINAL_SOURCE_NOISY_MICROSTIM_1728_PASS
created_at: 2026-11-12
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE

# XH-S6 ROT009 — Original source noisy MT/dlPFC microstimulation using exactly paired noise; 1,728 paired author-model task observations

## 1. Actual executed science and original firstness

Source FIRST: Douglas A. Ruff, Sol K. Markman, Jason Z. Kim, Marlene R. Cohen, Information formatting in neuronal populations predicts differential functional contributions to behavior, Nature Neuroscience (10 Nov 2026), DOI https://doi.org/10.1038/s41593-026-02514-7. Original behavioral experiments and source artificial two-module RNN are different evidentiary objects. Only the source RNN was executed by XH-S6, never animal experiments.

Original author source https://github.com/solkm/formattingRNN pinned commit 7889a81e298c01532a313e02971c11dbc9db8eb0. Original author git-file blobs ACTUALLY verified inside scientific runner BEFORE import and use:
- generate_microstim_testdata.py e7a6666e0b600ea49bab9755d302c78110ba9bc4 (author stimulated units/strengths, source noise and 72x250 per condition);
- DotsTasks.py ac9e789c69a8ea46ac38303f9d0db524886ba0a9, original task MT_broadInSharpOut_withR and DLPFC_combined with real input noise and randomly drawn onset;
- psychrnn/backend/simulation.py d187595af592a888192bfc2dde6f562776b88423, original BasicSimulator_linOut MT and BasicSimulator dlPFC recurrent-noise software;
- psychrnn/tasks/task.py b3bc5a5ca3fb2b0d2b4b79a4cd5ce8930e142865;
- circledots_fxns.py 909a65d84174a7eebb0e19273d06ae400dc9094f;
- original trained MTbroadsharp_m10.npz c5e701740f8ab1d19ca07415c0de2d6e7f88c37f;
- original trained DLPFCcombined_m4.npz 47142e3dee920a759406136449f0b12f9ce752ee.

New-to-XH ROT009 compared with ROT008: BOTH input and recurrence noise actually ON per original source, original task randomly draws ring onset among 50-140ms in 10ms increments and motion onset among 450-540ms; original source task and simulator classes actually executed, with original MT and dlPFC trained 150-unit matrices. Original noise magnitudes MT input 0.4 recurrent 0.2; dlPFC input 0.2 recurrent 0.2. Network dt=10ms, tau=100ms, T=1200ms, coherence=0.6.

## 2. Additional bounded common-noise pairing; actual source microstimulation

Original source specified units, strengths and reward bias +180°:
- MT unit 37, preferred 110°, reward center 290°, source strength 11.
- dlPFC unit 53, preferred 295°, reward center 115°, source strength 45.

For EACH unit: all 72 shown directions 0..355° by 5°, repeated at 12 fixed pseudorandom seeds = 864 paired task trials. Every pair compares stimulated vs non-stimulated final choice of original DLPFC model with exactly matched onset and both input/recurrent noise stream realizations, because the additional XH control resets original DotsTasks module random generator AND NumPy recurrent random generator identically per arm. Both arms overwrite original source W_in last channel with SAME one-hot unit column (as actual author microstim generator does); difference is source Task injected strength. This avoids a source-inconsistent artificial final-score perturbation or omitting the last-channel baseline noise. Original source code itself is unchanged; common-random-number PAIRING is our additional test design, NOT an assumption that original authors paired these 18k-trial blocks.

Actually executed pairs:
- MT 37: changed final chosen output bin in **862/864 = 99.7685185%**, unchanged 2.
- dlPFC 53: changed final chosen bin in **616/864 = 71.2962963%**, unchanged 248.
- ALL 1728 pairs share exactly matched original drawn time parameters and entire input/recurrent RNG consumption. Source RNG final state hash matches control and stimulated arms, PASS. One sham repeat of 72 trials per module reproduced exactly identical 72x72 final DLPFC output score matrices, BITWISE PASS. For dlPFC stimulation source input time series excluding stimulating last channel is exactly equal across arms, PASS.
- Original argmax margin sufficient condition: NO violation. Two invariant dlPFC cases certified by actual eps<Delta/2, no MT cases positively certified. A changed winner NEVER passed a false stability certificate.

These are not MT versus dlPFC neural area contrasts. Units, source strengths, reward biases and sample selection differ; only two selected original source units tested and 12 seeds per direction compared to authors' 250. No i.i.d. confidence interval or p-value inferred; no original 18,000-per-condition noisy output reproduction.

## 3. Independently evaluated ORIGINAL SOURCE target-reward at actual observed chosen bins

The actual GitHub Actions run artifact containing 1,728 original-source output pairs was downloaded and inspected. A DIFFERENT standalone local pure-standard-library Python postprocessor evaluated the author DotsTasks original reward TRAINING TARGET at observed final chosen bins. For candidate theta, shown s, reward center g, unsigned circular distance d:
R(theta;s,g)=0 if d(theta,s)>45°; otherwise
R=[3.5+1.5cos(1.8*pi*d(theta,s)/180)]*[1+0.75cos(pi*d(theta,g)/180)].
This source TASK training target is NOT a monkey-received reward or empirical choice accuracy.

MT 37 original-source chosen-bin target:
- mean baseline 5.672412324978108, stimulated 3.4393817137483156, paired average delta **-2.2330306112297924**;
- of 864, target decreases 859, increases 3, equals 2;
- observed chosen bin within source ±45° window baseline 864, stimulated 783; median circular shift 45°.

dlPFC 53 original-source chosen-bin target:
- mean baseline 5.681360759304704, stimulated 4.804894124900252, paired average delta **-0.8764666344044522**;
- of 864, target decreases 515, increases 101, equals 248;
- observed chosen bin within source ±45° window baseline 864, stimulated 785; median circular shift 10°.

This is a FUNCTIONAL model diagnostic: source stimulus-induced choice changes do NOT imply target-score improvement. No claim about improved or impaired real animal reward or physical neural causes.

Postprocessor checked 1728 unique module/seed/direction tuples, original source unit and strength per module, reward bias, allowed onset grids, noise source identity, paired random control declarations, all output bin grid values, recomputed changed flag, and every applicable sharp argmax margin bound; fail closed if inconsistent. Fresh isolated clean subprocess replay emitted BOTH full 1728-row derived CSV and summary JSON BYTE-IDENTICALLY, PASS.

## 4. Custody and actual output

ACTUALLY EXECUTED source script PUBLIC git commit 4c926527d96eb4a2b6301805eefa395351181abf, blob 054299b6b0f0c0def7cfa6b3600d6f56665375ce; original source native:
https://github.com/wmakiela-tech/Nash-iw-research/blob/4c926527d96eb4a2b6301805eefa395351181abf/research/xh-s6/2026-11-12/xh_s6_rot009_author_native_paired_noisy_microstim.py

Workflow PUBLIC commit 8bdd3eda8be5952bcd6a38ce36f6f0c0358239f9, blob 3c1488dfe2366660b5ffe4b9d3addeb72d302908, readback PASS:
https://github.com/wmakiela-tech/Nash-iw-research/blob/8bdd3eda8be5952bcd6a38ce36f6f0c0358239f9/.github/workflows/xh-s6-rot009-author-native-noisy-paired.yml

ACTUAL native source runner GitHub Actions run 43310690236 job 131505685579 COMPLETED SUCCESS, all steps PASS:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43310690236
Source ZIP artifact 13986326464, ~50KB, 30-day retention:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43310690236/artifacts/13986326464

ACTUAL runner output JSON was programmatically extracted from real GitHub Actions log and persisted GitHub CREATE + PINNED BYTE-IDENTICAL READBACK PASS, commit 4fcf089daf653ffc77b9b0ad277fe17e9b54a21a, blob 5ea39307185f21b1b18d68f1cf432a8dd2effe63:
https://github.com/wmakiela-tech/Nash-iw-research/blob/4fcf089daf653ffc77b9b0ad277fe17e9b54a21a/research/xh-s6/2026-11-12/xh_s6_rot009_original_native_noisy_paired_actual_runner_summary.json

The ACTUAL artifact downloaded to local environment, ZIP CRC PASS. Original source-native output CSV exactly 1728 rows, 157231 bytes SHA256 c713c76b039fa9ac0176804e91a3d5d5951e44c88a3a9484c7b44363344398e7. Actual runner JSON 2502B SHA256 a5e1ae091280df6f470b8fb3ab414ec7d3f7f42dfa7a5f68fd56af15440f29dd, runner stdout JSON BYTE-IDENTICAL.

Local COMPLETE source-evidence and postprocessing reproducibility bundle:
IW_XH_S6_ROT009_NATIVE_NOISY_PAIRED_1728_SOURCE_REPRO_20261112.zip, **125980 bytes**, SHA256 **23822daed6b1ba93c189f340a9e79fa16356f1fc1c821dfdd68099bedbbfdc4b**. Includes original 1728-row source-runner CSV, exact runner JSON, independently derived source-target 1728-row CSV SHA256 98e06fc7a45c2483cc62f16471aaafbcbb807f526b14aefd138f00e3fe31e19b, independently derived summary JSON SHA256 f151bcf53683447c5eecd5ed8de19b200bbfa3d77fad576903be4ca7cc19debe, standalone reproducible postprocessor SHA256 dead62551122a5e009f8c6af105eab37fa222c74fe73f0815307ab4b927e4ab9, README and manifest. ZIP CRC PASS, all six payload SHA256 PASS, manifest PASS, independent isolated clean postprocessor CSV+JSON BYTE EXACT PASS. Author trained weight binaries remain at original author Git immutable commit, NOT bundled.

## 5. Mature prior art, ceiling, next discriminant

Classical host: paired common random numbers for variance reduction in stochastic simulation, winner margin/argmax stability, authors' original neural simulation. No new mathematical theorem, mechanism, novelty or author software bug alleged. The published nature neurosciences study addresses MT/dlPFC population format and actual animal microstimulation; this bounded model exercise neither replicates nor refutes animal findings. Contrasting 99.77% and 71.30% from differently scaled source units does not establish region causality.

Meaningful future discriminant IF separately authorized: check additional original stimulated units/strengths, full source 250 trials per angle with original independent seeds and source MATLAB/figure analysis, and compare to actual original animal data where available. No automatic task cascade. BW GITHUB_PENDING_BW_INGEST, not verified KN ingestion; no AUD/REC referee or Moderator adoption/EXEC signature.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEUROBIOLOGICAL_UPGRADE / NO_NEW_TASK_CASCADE.
