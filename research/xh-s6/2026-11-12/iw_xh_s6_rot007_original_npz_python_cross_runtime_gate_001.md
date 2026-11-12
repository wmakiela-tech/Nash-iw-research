artifact_id: IW_XH_S6_ROT007_ORIGINAL_NPZ_PYTHON_CROSS_RUNTIME_GATE_001_20261112
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
return_id: IW_XH_S6_ROT007_ORIGINAL_NPZ_PYTHON_CROSS_RUNTIME_GATE_001_20261112
result_class: ACTUAL_NATIVE_NUMPY_ORIGINAL_WEIGHT_CROSS_RUNTIME_REPLAY_PASS / SOURCE_TYPED_NUMERICAL_CONTROL
claim_ceiling: VERIFIED_360_CASE_PYTHON_NUMPY_VS_V8_SAME_AUTHOR_SOURCE_EQUATIONS_ZERO_NOISE / NO_ORIGINAL_PSYCHRNN_RUNTIME / NO_MONKEY_DATA / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
status: PYTHON_WEIGHT_CROSS_REPLAY_CLOSED_PASS_FOR_ROT006_360_ONLY
created_at: 2026-11-12

# XH-S6 ROT007: actual original-NPZ Python/NumPy replication of the 360 ROT006 source-model results

## Primary result

**ACTUAL 2026-11-12 GitHub Actions native Python 3.11.18 and NumPy 2.1.3 execution: 360/360 matched; failed 0; maximum absolute learned-output margin error 4.884981308350689e-15.** Exact model choice winner matched for all 360 cases. The Python calculation compared actual final output score margins to independent V8 output data; comparison tolerance was the pre-specified 2e-5, while observed discrepancy was ~5e-15.

Result is logged in actual GitHub Actions run 43305078746, job 131486083055, which completed SUCCESS with every step completed successfully, including clone, frozen source identity check, scientific execution, and artifact upload:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43305078746

The actual job returned:
- compared=360, passed=360, failed=0, failures=[];
- full_python_cross_runtime_weight_replay=PASS;
- max_margin_abs_error=4.884981308350689e-15;
- source_numpy=2.1.3;
- script elapsed_s=1.5858028429999997 (not entire runner wall time).

Independent original author model NPZ source weights were actually checked out by Git on the runner. Both original Git blob SHA1 values were checked in Git job logs and independently checked in Python before arrays were loaded. The two prior ROT006 V8 reference CSV SHA1 values also were checked inside the Python code. Wrong input identity fails closed: a separate local test with deliberately corrupted NPZ bytes produced SOURCE_IDENTITY_FAIL, not a false PASS.

## Original author firstness and source provenance

Original researchers: Douglas A. Ruff, Sol K. Markman, Jason Z. Kim and Marlene R. Cohen, Information formatting in neuronal populations predicts differential functional contributions to behavior, Nature Neuroscience, publication 10 November 2026, DOI https://doi.org/10.1038/s41593-026-02514-7. Their actual monkey recordings, stimulations and behavioral findings are separate and are not replicated here. This source-weight control does not claim novelty or identify a bug in the paper.

Frozen source: https://github.com/solkm/formattingRNN at EXACT commit 7889a81e298c01532a313e02971c11dbc9db8eb0. Both original trained weights:
- python_code_data/model_weights/MTbroadsharp_m10.npz, Git blob c5e701740f8ab1d19ca07415c0de2d6e7f88c37f;
- python_code_data/model_weights/DLPFCcombined_m4.npz, Git blob 47142e3dee920a759406136449f0b12f9ce752ee.

Original author mathematical model code: python_code_data/psychrnn/backend/simulation.py Git blob d187595af592a888192bfc2dde6f562776b88423 (MT linear output, dlPFC ReLU); task source python_code_data/DotsTasks.py blob ac9e789c69a8ea46ac38303f9d0db524886ba0a9. The independently implemented frozen update is 150-unit + 150-unit recurrent state with dt=10ms, tau=100ms, alpha=0.1, 120 steps, original MT-to-dlPFC 72 directional channels, source-allowed fixed event onsets, ZERO input/recurrent noise, no stimulated unit. It is not original author software package execution or an experiment.

## Exact prior comparisons — two 180-case axes, not a 1,800-case grid

ROT006 frozen V8 reference motion-onset source trained-score CSV: 18 reward-antipode conditions x10 dots slots 450..540ms, ring=100ms, immutable commit f5e0d00624dc5b6996cb05c6816563dba3a05754, Git blob 88bd42f4ce793c823faf5bc8e804b466ce643624:
https://github.com/wmakiela-tech/Nash-iw-research/blob/f5e0d00624dc5b6996cb05c6816563dba3a05754/research/xh-s6/2026-11-12/xh_s6_rot006_original_weight_18x10_dots_onset_grid.csv

ROT006 frozen V8 reference reward-onset source trained-score CSV: 18 conditions x10 ring slots 50..140ms, dots=500ms, immutable commit ebdd2ceec848076bc17656b558c0c44adb875b35, Git blob f8a4e12e7fd706112bbe273bd437675ec55ebc3a:
https://github.com/wmakiela-tech/Nash-iw-research/blob/ebdd2ceec848076bc17656b558c0c44adb875b35/research/xh-s6/2026-11-12/xh_s6_rot006_original_weight_18x10_ring_onset_grid.csv

The two cuts contain 360 computed results and 342 unique onset/condition inputs because the central source point is present in both cuts. **ROT007 verifies those 360 outputs only**. It does not independently rerun the complete ROT005 single-condition 100-point time grid, selected stimulations in ROT003, or the full 18x100 cross product.

## Actual runnable source and evidence

Native Python NumPy source code published with byte-exact pinned readback and independent matching local Git SHA:
https://github.com/wmakiela-tech/Nash-iw-research/blob/e96fb8dca2dec8554567730f18f13482afbc29db/research/xh-s6/2026-11-12/xh_s6_rot007_native_npz_360_cross_runtime_replay.py
Git blob c28241ae2bae4bf7473307b3519f5331c1434176; local SHA256 4e67ebd47da542bff349eb71ae8edd70fcb5d5113e85cfa3513cc29dc8221070.

Scoped self-triggered GitHub Actions workflow with no write permission, bounded 25min job, pinned original source and NumPy version, results artifact retention 30 days, also byte-exact GitHub readback:
https://github.com/wmakiela-tech/Nash-iw-research/blob/fa46c5e1b9cedb07f3b3006d761f007f96c0666e/.github/workflows/xh-s6-rot007-native-weight-replay.yml
Git blob e04e55a9f8eec8c7ca45c90185f246e4018825f9.

Actual runner emitted 360 detailed row records as CSV and summary JSON. GitHub Actions artifact ID 13982288843, artifact name xh-s6-rot007-native-python-360-control, size 8626B, 30-day retention, attached to run 43305078746. The summary JSON was also parsed from actual GitHub job log and written as persistent public GitHub text at:
https://github.com/wmakiela-tech/Nash-iw-research/blob/13fa5c32d53fd2421d6007f6ae9e2c85c57d1992/research/xh-s6/2026-11-12/xh_s6_rot007_native_python_360_summary_from_runner_log.json
Git blob 4ae449ee7b0ac24a2186e9ea9d831c8be32c9af9; exact pinned readback PASS.

## Scientific interpretation and strict ceiling

ROT006 findings (17/18 conditions stable across 10 motion slots, one with a switch; 18/18 stable across 10 reward slots with fixed motion onset; source target ties do NOT imply trained-score ties) now have a genuinely independent implementation- and runtime-level numerical check on the *same exact author trained NPZ data*. Neither implementation used original PsychRNN's own Python classes. Independent agreement strongly reduces concern about arithmetic and implementation-specific numerical artifacts in those cuts, but shared interpretation of source equations remains a common dependency.

No original full published noisy microstimulation procedure, 18,000-trial generator, network retraining, monkey experiment, source paper figures, physiological mechanism, or scientific discovery was reproduced. No full generic robustness or causality conclusion. Authors retain original results and priority.

Previous XH S6 PYTHON_WEIGHT_CROSS_REPLAY_OPEN for ROT006's 360 numerics is NOW PYTHON_WEIGHT_CROSS_REPLAY_CLOSED_PASS for exactly those records. Native original author PsychRNN execution and broader empirical controls remain OPEN. No IW/NASH physical-front E4 claim, no BW ingest receipt, no independent referee decision, no scientific CANON or EXEC_SIGN.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE.
