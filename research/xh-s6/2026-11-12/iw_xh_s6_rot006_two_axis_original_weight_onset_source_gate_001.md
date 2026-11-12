artifact_id: IW_XH_S6_ROT006_TWO_AXIS_ORIGINAL_WEIGHT_ONSET_SOURCE_GATE_001_20261112
exposure: PUBLIC
claim_ceiling: SOURCE_TYPED_BOUNDED_ORIGINAL_TRAINED_WEIGHT_ZERO_NOISE_TWO_AXIS_ONSET_CROSS__NO_FULL_18x100_GRID_NO_PYTHON_WEIGHT_REPLAY_NO_MONKEY_DATA_NO_NOVELTY_NO_CANON_NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
task_id: IW_XH_S6_ROT006_AUTONOMOUS_EXTERNAL_SCIENCE_20261112
return_id: IW_XH_S6_ROT006_TWO_AXIS_ORIGINAL_WEIGHT_ONSET_SOURCE_GATE_001_20261112
result_class: ORIGINAL_TRAINED_SOURCE_WEIGHT_BOUNDED_TWO_AXIS_TEST + NEGATIVE_KNOWLEDGE
status: COMPLETE_BOUNDED_V8_RECOMPUTATION__CROSS_RUNTIME_PYTHON_WEIGHT_REPLAY_OPEN
created_at: 2026-11-12
acceptance_owner: Human Moderator; original scientific priority remains source authors
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE

# XH-S6 ROT006 — Original trained-weight two-axis stimulus timing cuts across 18 exact reward-target ties

## 0. Main bounded inference

The XH-S6 ROT003 source training-target grid has exactly 18 structurally tied top-target pairs at reward center good=0,20,...,340 degrees and shown=(good+180) mod 360 degrees, with target maximizers reflected at shown±45 degrees. ROT004 distinguished that source TARGET from learned model output using original trained MT and dlPFC weights. ROT005 computed an original-weight 10x10 timing grid for one antipodal condition (good80, shown260), finding 78 fixed-grid choices of 240deg and 22 of 225deg.

ROT006 now compares TWO DIFFERENT AND FULL SOURCE-DISCRETE TIMING AXIS CUTS ACROSS ALL 18 SOURCE-ANTIPODAL CONDITIONS, not a full 18x100 Cartesian grid:

CUT A: FIX reward-cue onset t_ring=100ms, scan all TEN source-allowed motion onsets t_dots=450,460,...540ms for EACH of 18 antipodal reward/shown conditions. Exactly ONE of 18 conditions has more than one trained winner over its 10 timings: good=80deg, shown=260deg. Choices 240deg for t_dots=450..510ms (seven positions), then 225deg for 520,530,540ms (three positions). All other 17 of 18 have invariant winner across this fixed-ring ten-point cut, despite varying score margins.

CUT B: FIX motion onset t_dots=500ms, scan all TEN source-allowed reward-cue onsets t_ring=50,60,...140ms for EACH of the same 18 antipodal conditions. ZERO of 18 conditions change their trained winner over these ten ring-onsets. This is an asymmetry between THESE TWO FINITE CUTS, not a theorem that movement timing always matters more than reward timing.

A further SOURCE-WEIGHT negative control: good=120deg, shown=300deg shows exceptionally small trained top-two margin (minimum 0.001103356724628357 in cut A, 0.0012155080624196568 in cut B) while keeping learned winner 335deg across both entire cuts. Thus a small learned margin ALONE does not imply a switch under a particular intervention or timing perturbation. The earlier sharp argmax theorem gives a SUFFICIENT preservation condition, not a NECESSARY switch condition.

Both cuts contain 18x10=180 numerical runs each; 360 executions total, but the common t_ring=100,t_dots=500 input appears once in each cut for each reward pair, so 342 UNIQUE ONSET/REWARD CONDITIONS. Do NOT call this the full 1800-point (18x100) onset grid.

## 1. Original primary scientific/source provenance

Scientific priority: Douglas A. Ruff, Sol K. Markman, Jason Z. Kim and Marlene R. Cohen, Information formatting in neuronal populations predicts differential functional contributions to behavior, Nature Neuroscience (published 10 November 2026), DOI https://doi.org/10.1038/s41593-026-02514-7 . The authors' real monkey interventions and the synthetic two-module RNN are DISTINCT scientific evidence surfaces; none of the experimental monkey data or author original noisy test-data were obtained.

Original author PUBLIC GitHub repository https://github.com/solkm/formattingRNN frozen at exact commit 7889a81e298c01532a313e02971c11dbc9db8eb0. Original source code read:
- python_code_data/DotsTasks.py Git blob ac9e789c69a8ea46ac38303f9d0db524886ba0a9, source onset draws 10*rng.integers(5,15) and 10*rng.integers(45,55), and DLPFC reward-target formula.
- python_code_data/circledots_fxns.py Git blob 909a65d84174a7eebb0e19273d06ae400dc9094f, source circular distance.
- python_code_data/simulate_combined_model.py Git blob 0ccaadfd271c660a2a503b24f15b77ddede32962.
- python_code_data/psychrnn/backend/simulation.py Git blob d187595af592a888192bfc2dde6f562776b88423, BasicSimulator_linOut and BasicSimulator recurrences.
- EXACT ORIGINAL BINARY MODEL WEIGHTS re-fetched via GitHub connector base64 for this rotation and independently decoded as ZIP_STORED NPY arrays: MTbroadsharp_m10.npz 908648B Git blob c5e701740f8ab1d19ca07415c0de2d6e7f88c37f, DLPFCcombined_m4.npz 903824B Git blob 47142e3dee920a759406136449f0b12f9ce752ee.

Neither trained model's historical learning run nor experiment source original PsychRNN Python script was executed by XH. This is a NUMERIC SOURCE-WEIGHT TEST, not a final-paper result reproduction.

## 2. Original weight calculation performed, and exactly what it means

The independent connector V8 implementation used the actual 150-unit MT and dlPFC original weight matrices loaded from both original author NPZ archives. It propagated the original mathematical recurrences for T=1200ms, dt=10ms, tau=100ms, alpha=.1:

h_new=(1-alpha)*h + alpha*(W_rec ReLU(h)+W_in u+b_rec).
MT output=W_out h_new+b_out (LINEAR).
dlPFC output=W_out ReLU(h_new)+b_out.
dlPFC's 72 directional inputs at each time step are the 72 corresponding MT output channels. MT ring cue activates for t>=t_ring and motion for t>=t_dots; dlPFC ring cue activates for t>t_ring. Input noise and recurrent noise were both SET TO ZERO in both modules; no neuronal stimulation applied.

All 18 exact TARGET tie conditions were simulated independently on each fixed axis cut. Three previous frozen central models with t_ring=100,t_dots=500 exactly reproduce prior source-weight V8 control values to displayed precision:
- good0,shown180, trained choice215, margin 0.19728256680576362;
- good80,shown260, choice240, margin 0.014153417139922464;
- good120,shown300, choice335, margin 0.0016968323606314506.

All 360 results are real ORIGINAL WEIGHT connector-V8 executions, not analytic or model-free artificial scores. They are intentionally not a sample of the published, noisy original stimulation experiment. Source code later Monte Carlo sample under nonzero noise may behave differently.

## 3. Complete actual-source numeric products; pinned readbacks

180-row original-weight, fixed-ring/motion-onset source data (full scores' top-two gaps):
https://github.com/wmakiela-tech/Nash-iw-research/blob/f5e0d00624dc5b6996cb05c6816563dba3a05754/research/xh-s6/2026-11-12/xh_s6_rot006_original_weight_18x10_dots_onset_grid.csv
Git blob 88bd42f4ce793c823faf5bc8e804b466ce643624; pinned byte-exact GitHub readback PASS.

180-row original-weight, fixed-dots/reward-onset source data:
https://github.com/wmakiela-tech/Nash-iw-research/blob/ebdd2ceec848076bc17656b558c0c44adb875b35/research/xh-s6/2026-11-12/xh_s6_rot006_original_weight_18x10_ring_onset_grid.csv
Git blob f8a4e12e7fd706112bbe273bd437675ec55ebc3a; pinned byte-exact GitHub readback PASS.

Every row includes reward center, shown direction, both onsets, final trained winner, and trained top-two output margin. These are connector-V8 generated author-WEIGHT output receipts. NOT author monkey data, NOT claimed author original executable replay.

## 4. Exact scientific scope and hold

What is NEW TO THIS CELL: two-axis finite timing decomposition shows a more constrained pattern than ROT004's three-schedule counterexample and ROT005's one-condition full onset grid. Within these matched 18 ANTIpodal tasks, cue-timing axis remains choice-invariant at motion onset=500ms but motion-timing axis has one witness of choice change at fixed ring=100ms. Very small trained margins can coexist with invariant winners over both tested axis cuts. These observations identify a targeted distinction between sensitivity of source model's eventual decision to event schedules versus the mere source training-target tie and margin.

This DOES NOT prove stimulus-onset ANISOTROPY for all source conditions, all noise realizations or even all 18x100 onset pairs. Full 18x100 would need 1800 model executions; no extrapolation to it.

CROSS-RUNTIME OPEN: Actual original GitHub NPZ bytes were available inside connector V8 but NOT in local Python execution environment. A standalone Python independent NumPy source-recurrence reproducer verifying Git blob SHA1 identities and both 180-row winner patterns was prepared in local environment; NO-WEIGHTS target formula symmetry mode ACTUALLY EXECUTED PASS. Intentionally incorrect dummy NPZ input triggers FAIL-CLOSED source SHA identity as intended PASS. Its source-weight mode was NOT EXECUTED, so there is no V8-versus-Python numeric verification and no native source Python replay PASS. No original monkey data, no source training and no hardware experiment was reproduced. Source raw NPZ source bytes are not included in local archive.

No claim the paper's authors missed a control or have an error; they retain firstness in neuronal population formatting and actual intervention evidence. No new mathematical novelty, physical model, scientific CANON, EXEC_SIGN, owner assignment, or evidence for other NASH physical fronts.

## 5. Status and conditional next diagnostic

ROT006 SOURCE_WEIGHT_V8_TWO_AXIS_360_RUNS_PASS / TWO_PUBLIC_DATA_CSV_PINNED_READBACK_PASS / PYTHON_TARGET_SYMMETRY_AND_HASH_GUARD_PASS / PYTHON_ORIGINAL_WEIGHT_REPLAY_NOT_RUN / NO_EMPIRICAL_NEUROSCIENCE_CLAIM. BW state is GITHUB_PENDING_BW_INGEST, not proof of ingestion.

Scientific reopen only after obtaining pinned original MT and dlPFC NPZ source bytes in local Python runtime and comparing 360 per-row winners/margins; following that, source nonzero-noise controlled paired-onset test may become relevant. This rotation DOES NOT assign new work to an external owner or require new animal experiments.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE.
