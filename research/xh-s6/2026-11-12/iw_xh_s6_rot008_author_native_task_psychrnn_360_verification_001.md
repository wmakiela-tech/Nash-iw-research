artifact_id: IW_XH_S6_ROT008_AUTHOR_NATIVE_TASK_PSYCHRNN_360_VERIFICATION_001_20261112
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
return_id: IW_XH_S6_ROT008_AUTHOR_NATIVE_TASK_PSYCHRNN_360_VERIFICATION_001_20261112
result_class: EXECUTED_AUTHOR_NATIVE_DOTSTASKS_AND_VENDORED_PSYCHRNN_REPLAY_360_OF_360_PASS
claim_ceiling: AUTHOR_NATIVE_CLASSES_WITH_FROZEN_ORIGINAL_WEIGHT_ZERO_NOISE_EXPLICIT_FIXED_ONSET_REPLAY / NO_FULL_ORIGINAL_NOISY_GENERATOR / NO_MONKEY_DATA / NO_NEW_NEUROSCIENCE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
status: AUTHOR_NATIVE_TASK_SIMULATOR_BOUNDED_360_PASS
created_at: 2026-11-12
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_OWNER_TASK_CASCADE / NO_PHYSICAL_UPGRADE

# XH-S6 ROT008 — Actual original author DotsTasks and vendored PsychRNN classes, 360/360 frozen author-weight model outputs reproduced

## 0. New experimental-simulation status: source-native classes executed, not just reimplemented equations

ROT007 independently reproduced 360 deterministic model outputs in Python/NumPy against previous V8, using the authors' MATHEMATICAL EQUATIONS but *not* their source classes.

ROT008 explicitly closes that remaining source-software question FOR THOSE 360 CONDITIONS: an actual GitHub Actions runner imported and executed all FOUR original author repository classes without modifying them:
- DotsTasks.MT_broadInSharpOut_withR (task generator for MT);
- DotsTasks.DLPFC_combined (task generator feeds MT simulator into dlPFC input);
- psychrnn.backend.simulation.BasicSimulator_linOut (MT, linear output);
- psychrnn.backend.simulation.BasicSimulator (dlPFC, ReLU output).

Each original MT task generated exact input and trial parameters with fixed, author-source-permitted ring and dots onset. Original DLPFC task itself invoked the MT simulator; the runner then invoked original dlPFC simulator on that generated input. Neither task nor simulator was replaced by our recurrence reimplementation. Source inputs differ only by controlled freezing of randomized onset, ZERO input/recurrent noise and no stimulation; author code itself executes. N_batch=1 per case rather than authors' larger batch generator. Original trained weight matrices and original 72-output readout are unchanged.

Actual full result from GitHub Actions run **43308934497**, job **131499521302**:
- status=completed, conclusion=SUCCESS; all steps SUCCESS;
- original exact author files and two original NPZ binaries checked by SHA1 Git blob before imports;
- compared=360, expected_total=360, passed=360, failed=0, failures=[];
- native_task_classes = [MT_broadInSharpOut_withR, DLPFC_combined];
- native_simulator_classes = [BasicSimulator_linOut, BasicSimulator];
- max_margin_abs_error = 1.5973260492074814e-9 versus pinned ROT006 V8 output margins;
- max_author_target_tie_difference = 0.0 (source original reward TARGET symmetric maxima, 18 antipodal conditions);
- execution elapsed_s = 6.568502909999999 for 360 author-source test cases only, not full workflow;
- no monkey data, no novelty, no CANON, no EXEC_SIGN.
- 360 winners identical to prior ROT006 original-weight V8 output. Difference is much smaller than preregistered tolerance 2e-5; this is also independent corroboration of all 360 prior ROT007 NumPy result labels.

GitHub Actions source:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43308934497
Job id 131499521302, artifact id 13983944647, name xh-s6-rot008-author-native-psychrnn-360, size 13022 bytes; contains per-row 360-case CSV, runtime JSON and stdout JSON; 30-day retention. All source-dependent results were actually computed in native Python 3.11 and pinned NumPy2.1.3, not inferred from CI signal alone. Full log was directly read for result JSON.

## 1. Firstness and author source chain (immutable)

Original firstness: Douglas A. Ruff, Sol K. Markman, Jason Z. Kim and Marlene R. Cohen, Information formatting in neuronal populations predicts differential functional contributions to behavior, Nature Neuroscience (10 November 2026), DOI https://doi.org/10.1038/s41593-026-02514-7. The biological findings and artificial two-module RNN results are distinct evidence; this paper is source HOST, not a novelty result of XH-S6.

Author public repository https://github.com/solkm/formattingRNN frozen at original commit **7889a81e298c01532a313e02971c11dbc9db8eb0**.
Every file was read and its original Git blob identity checked by the ACTUAL executable before using it:
- DotsTasks.py blob ac9e789c69a8ea46ac38303f9d0db524886ba0a9;
- psychrnn/backend/simulation.py blob d187595af592a888192bfc2dde6f562776b88423;
- psychrnn/tasks/task.py blob b3bc5a5ca3fb2b0d2b4b79a4cd5ce8930e142865;
- circledots_fxns.py blob 909a65d84174a7eebb0e19273d06ae400dc9094f;
- original pretrained MTbroadsharp_m10.npz blob c5e701740f8ab1d19ca07415c0de2d6e7f88c37f;
- original pretrained DLPFCcombined_m4.npz blob 47142e3dee920a759406136449f0b12f9ce752ee.

Two previous source-score CSVs, immutable authors' source-weight V8 numerical observations:
- ROT006 180-row motion-onset CSV Git blob 88bd42f4ce793c823faf5bc8e804b466ce643624, pinned Git commit f5e0d00624dc5b6996cb05c6816563dba3a05754;
- ROT006 180-row reward-onset CSV Git blob f8a4e12e7fd706112bbe273bd437675ec55ebc3a, pinned Git commit ebdd2ceec848076bc17656b558c0c44adb875b35.
Runner's original task/simulator outputs compare to BOTH CSV sources row-by-row; CSV input checks fail closed.

## 2. Exactly which 360 task configurations were executed

All use original source task and pretrained model class defaults N_rec=150 per module, N_batch=1, dt=10ms, tau=100ms, T=1200ms, alpha=.1, 72 circular angle bins, MT coherence 0.6, k_in=0.3, k_out=0.8, source trial task target and masks. Input noise 0, recurrent noise 0, microstimulation 0. Original task's fixed onset options are used; no stochastic times.

For each reward bias good=0,20,40,...340 degrees (18 conditions), shown=(good+180) mod 360, making reward TARGET two-way exactly tied by original source mirrored ±45 target maxima:
- 180 trials: t_ring=100ms fixed, t_dots=450,460,..540ms;
- 180 trials: t_dots=500ms fixed, t_ring=50,60,..140ms.
These are 360 total author-source executions but 342 UNIQUE input configurations due to overlap of central (100,500ms) between the cuts, NOT a complete 1800-condition 18x100 timing grid.

Original source class chain for every case:
1. MT_broadInSharpOut_withR(... fix_shown=[shown], fix_reward=[good], fix_onset=[ring,dots], test1ofEach=True, N_batch=1) constructs original time series and original source target;
2. BasicSimulator_linOut(weights=original MT NPZ, rec_noise=0) computes MT output;
3. DLPFC_combined(... MT_task, MT_simulator, D_mstim_strength=0, N_batch=1) calls ORIGINAL MT task/runner and receives original MT output channels;
4. BasicSimulator(weights=original dlPFC NPZ, rec_noise=0) computes DLPFC model final scores; argmax chosen direction 5 times index.
Source target equality is tested separately for all 360 cases using target rewards in ORIGINAL Task parameters, with maximum absolute top-two target reward difference exactly zero.

This is a genuine ORIGINAL AUTHOR SOURCE-CODE CLASS REPLAY for those fixed source task parameters, not merely custom mathematical recurrence. HOWEVER this does NOT rerun the authors' original top-level experiment script as published, which sets different noise, randomized trial onsets and 18,000 tests per unit. Neither the experimental real monkey data nor author full paper figures have been obtained.

## 3. Distinguishing three evidence levels achieved by successive rotations

ROT006: independent connector-V8 reproduction with exact original trained author NPZ files, 360 SOURCE-WEIGHT recurrence rows, published CSV and checks.

ROT007: independent Python3.11/NumPy2.1.3 mathematical recurrence on exact source weights re-executed, 360/360 exact labels, max margin difference 4.884981308350689e-15, runner execution confirmed. This is CROSS-RUNTIME equation replication.

ROT008: authors' exact original source Task and PsychRNN simulator classes executed (source source ID verified), source-generated input streams, original reward target R and masks, same 360/360 labels, max margin error 1.5973260492074814e-9. This closes an additional SOURCE-IMPLEMENTATION validity question. It does NOT imply real-world experimental replication and does NOT automatically transfer findings outside 360 fixed zero-noise cases.

The 18 SOURCE-TARGET-tie conditions retain exact target equalities while learned output scores generally do not; learned small score margin alone does not imply a change of output under a particular fixed timing. One good=80/shown=260 witness changes from selected direction 240° to 225° upon delaying dots onset at ring100; these specific fixed-source-weight results are now supported by both independent V8/Python recurrence AND author-original Task/Simulator.

## 4. Reproducibility and custody

New PUBLIC exact original-task/simulator replayer:
https://github.com/wmakiela-tech/Nash-iw-research/blob/17246497aa443f351f9ff53bab51bc3d680f6aca/research/xh-s6/2026-11-12/xh_s6_rot008_author_native_task_psychrnn_replay.py
Git blob 4295152f433f24a037b7ea6ce1f5b7d144a1d9c9; pinned full byte-identical readback PASS.

New GitHub Actions YAML:
https://github.com/wmakiela-tech/Nash-iw-research/blob/48294d00710740be18168ed3b48ebb05a88f30aa/.github/workflows/xh-s6-rot008-author-native-psychrnn-replay.yml
Git blob 4eb85e70bdcda1f8e2ef672ade4091f2f30240f5; pinned full byte-identical readback PASS; run commit 48294d00710740be18168ed3b48ebb05a88f30aa, CI SUCCESS and Public source locator guard SUCCESS independently checked.

Actual source-native task/simulator result JSON extracted programmatically from real job logs and permanently published, with pinned exact readback PASS:
https://github.com/wmakiela-tech/Nash-iw-research/blob/6cba43095a9505d589bafb9f8d2921afa19dcce5/research/xh-s6/2026-11-12/xh_s6_rot008_author_native_psychrnn_360_actual_runner_summary.json
Git blob 078e8b4e42b63d87a8a0afebc403abdec3c98e2c.

GitHub Actions run 43308934497 COMPLETED SUCCESS; artifact ID 13983944647 (30-day GitHub retention). Additional provenance in actual output records Python version, source file commit, 8 source/file pins, chosen original class names and exact discrepancy.

## 5. Scientific judgment and negative knowledge

This is a source/software and model-control positive result, NOT evidence of a new neural mechanism. It strengthens numerical method confidence, not paper-level causal inference. The authors are source-first, and their real experiments require separately reproduced inputs, stochastic protocols and raw animal data. Source target and learned score remain different epistemic objects; no transfer of reward target margin distribution onto trained scores; no general frequency claims based on 18 source-tie conditions.

NO full author 18,000-trial per-unit noisy generator or entire published microstimulation suite, NO article figure reproduction, NO retraining, NO monkeys, NO original main simulation script executed verbatim (it has absolute local path), NO statistical hypothesis of human/animal causal mechanism proved, NO scientific novelty, NO CANON, NO EXEC_SIGN.

No XH ownership of unrelated PBH/BBN E4, DAX hadronic/QED, M14 or source owner tasks. BW only GITHUB_PENDING_BW_INGEST; no KN ingest or referee acceptance inferred.

## 6. Outcome

ROT008 COMPLETE AUTHOR_NATIVE_DOTSTASKS_AND_PSYCHRNN_360_OF_360_PASS. Numerical source-code class fidelity for these 360 source-allowed fixed no-noise trials is verified. Further scientific improvement requires a *different evidence class*: author noisy generator, actual animal data and precise statistical target; not repeated deterministic arithmetic.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE.
