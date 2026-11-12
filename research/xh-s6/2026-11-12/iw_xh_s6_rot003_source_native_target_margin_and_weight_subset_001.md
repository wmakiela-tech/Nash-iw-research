artifact_id: IW_XH_S6_ROT003_SOURCE_NATIVE_TARGET_MARGIN_AND_WEIGHT_SUBSET_001_20261112
exposure: PUBLIC
claim_ceiling: SOURCE_NATIVE_AUTHOR_TARGET_1296_GRID_AND_ORIGINAL_NPZ_WEIGHT_BOUNDED_ZERO_NOISE_CONTROL__NO_AUTHOR_PYTHON_REPLAY_NO_MONKEY_DATA_NO_NOVELTY_NO_CANON_NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
task_id: IW_XH_S6_ROT003_AUTONOMOUS_EXTERNAL_SCIENCE_20261112
return_id: IW_XH_S6_ROT003_SOURCE_NATIVE_TARGET_MARGIN_AND_WEIGHT_SUBSET_001_20261112
result_class: SOURCE_NATIVE_MATHEMATICAL_RESULT + BOUNDED_ORIGINAL_TRAINED_WEIGHT_REIMPLEMENTATION + NEGATIVE_KNOWLEDGE
status: COMPLETE_WITH_EXPLICIT_NATIVE_PYTHON_REPLAY_BLOCK
created_at: 2026-11-12
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_MONKEY_DATA / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE
acceptance_owner: MODERATOR; original scientific priority and causal interpretation remain authors'

# XH-S6 ROT003 — Exact author 1296-condition reward-target margin audit and bounded original-trained-weight control

## 0. Result and hard distinctions

The 72-bin reward TARGET programmed by Ruff et al. has exactly 18 structurally tied conditions in the complete 72-motion × 18-reward grid specified by the authors' original code. These occur when the reward center and motion direction are opposite; two reflected choices at ±45° have equal maximal target reward. The winner–runner-up target margin median across 1296 conditions is 0.021655289095978247. For 522/1296 (40.2778%), that margin is <=0.02. Consequently the sharp argmax stability theorem (XH-S6 ROT002) does NOT certify unchanged choice for all score perturbations of infinity norm eps=.01 in those 522 cases. NON-CERTIFICATION IS NOT ACTUAL CHOICE CHANGE. These are author TRAINING TARGETS, not trained-network output scores or monkey choices.

In a separate bounded exercise, actual original trained source NPZ files WERE retrieved in base64 from GitHub, decoded to float arrays and propagated by an independent V8 implementation of source recurrences. For ten deliberately selected, fixed-onset, ZERO-NOISE control conditions, actual source-weight model winner changed after selected-unit input drive. Ten hand-selected changes must never be generalized to frequencies in the full 72 × many-trial noisy model or to animal experiments. This exercise is ORIGINAL-WEIGHT REIMPLEMENTATION, NOT original author Python/NumPy replay.

## 1. Original firstness and source evidence

Douglas A. Ruff, Sol K. Markman, Jason Z. Kim, Marlene R. Cohen, Information formatting in neuronal populations predicts differential functional contributions to behavior, Nature Neuroscience (10 November 2026), https://doi.org/10.1038/s41593-026-02514-7 . The authors' monkey MT/dlPFC intervention data and their artificial two-module RNN are distinct evidence surfaces. We preserve their priority and do not allege an error.

Author original repository https://github.com/solkm/formattingRNN pinned commit 7889a81e298c01532a313e02971c11dbc9db8eb0, 2026-08-02.
Actually read author Git blobs:
- python_code_data/DotsTasks.py ac9e789c69a8ea46ac38303f9d0db524886ba0a9; reward formula lines 72-84 and source trial generator lines 190-195.
- python_code_data/circledots_fxns.py 909a65d84174a7eebb0e19273d06ae400dc9094f; circular shortest distance.
- python_code_data/simulate_combined_model.py 0ccaadfd271c660a2a503b24f15b77ddede32962; 72 x 18 grid and zero-noise defaults.
- python_code_data/generate_microstim_testdata.py e7a6666e0b600ea49bab9755d302c78110ba9bc4; original selected units and nonzero-noise multi-trial stimulation settings.
- python_code_data/psychrnn/backend/simulation.py d187595af592a888192bfc2dde6f562776b88423; recurrent equations and MT linear versus dlPFC ReLU outputs.
- ORIGINAL MTbroadsharp_m10.npz SHA1 Git blob c5e701740f8ab1d19ca07415c0de2d6e7f88c37f (908648 bytes); DLPFCcombined_m4.npz Git blob 47142e3dee920a759406136449f0b12f9ce752ee (903824 bytes). Both 2 binary source files were obtained via GitHub fetch_file base64 and parsed as ZIP_STORED NumPy arrays in connector V8 context. They are NOT attached to local reproducer bundle.
Source README distinguishes model-test data on Zenodo (https://doi.org/10.5281/zenodo.21764173) and unavailable raw monkey source data. Those datasets were NOT obtained.

## 2. Source training-target formula and exact symmetry

Author DLPFC_combined.generate_trial_params builds score R(theta;shown,good), with theta in {0,5,...355} degrees. Let circular distance d be the shortest unsigned angular separation in degrees. For d(theta,shown)<=45:
R = [3.5+1.5 cos(1.8*d(theta,shown)*pi/180)] [1+0.75 cos(d(theta,good)*pi/180)].
For d(theta,shown)>45 the target R=0.

All 1296 source conditions (shown multiples of 5 degrees, good multiples of 20 degrees) were reimplemented by TWO independent local Python code paths: scalar math-based direct source expressions and vectorized NumPy. Across all 1296x72 scores their maximum difference was exactly zero in the tested runtime. Additional checks asserted:
- Exactly 18 two-way maxima at numerical tolerance 1e-12, all corresponding to good=shown+180 mod 360; the reflected maxima theta=shown ±45 are equal by exact mathematical reflection symmetry.
- Median winning margin Delta=.021655289095978247, mean .028657726061133683, max .07567043954047303.
- Delta<=.002: 90/1296 (eps .001 target-score non-certification);
  Delta<=.02: 522/1296 (eps .01);
  Delta<=.04: 990/1296 (eps .02).
- 378/1296 source TARGET maximizers lie exactly at the ±45-degree accuracy-window boundary (with source-style first-index selection for tied maxima).
A clean isolated local rerun regenerates 1296-row CSV and summary JSON byte for byte: PASS.

The target-score non-certification is NOT a claim that trained output-score perturbations have eps=.01 or that any neural stimulation changed behavior. The original RNN task reward function is the object audited here, not actual trained DLPFC outputs.

## 3. Bounded numerical control on ORIGINAL trained source weights

In connector V8, two source NPZ archives were read from exact original Git blob identities. Source original model weights have MT W_rec=(150,150), W_in=(150,75), W_out=(74,150); dlPFC W_rec=(150,150), W_in=(150,75), W_out=(72,150). Extracted float32 weights were used as numeric float64 for deterministic recurrence.

Independent implementation of original BasicSimulator and BasicSimulator_linOut equations:
h_new = (1-alpha) h + alpha [W_rec ReLU(h) + W_in input + b_rec], alpha=.1.
For MT output = W_out h_new + b_out (LINEAR); for dlPFC output = W_out ReLU(h_new) + b_out.
Original source stimulated-unit input last-column overwrite with a unit basis vector was implemented as an additive alpha*stimulation_strength drive into precisely that unit. MT stimulus time t>=t_dots; dlPFC stimulus t>t_dots. MT reward cue time t>=t_ring; dlPFC reward cue t>t_ring. At every step dlPFC receives the 72 MT output direction channels. T=1200ms, dt=10ms, tau=100ms, coherence=.6, input and recurrent noise BOTH ZERO, fixed t_ring=100ms, t_dots=500ms. Fixed values fall within source time ranges, but are not the author's randomly generated trial onset. The actual published multi-trial source stimulation generator uses NONZERO noise and many trials: not reproduced here.

Two original source selected units with exact original strengths:
MT unit 37, original preferred direction 110 deg, stimulation strength 11, good center 290 deg; chosen shown directions 110,125,150,200,290.
dlPFC unit 53, source preferred direction 295 deg, stimulation strength 45, good center 115 deg; chosen shown directions 295,310,335,25,115.

Ten output samples (module | shown | good | baseline choice -> stimulated choice | baseline top-two margin | actual sup final-score difference):
MT | 110 | 290 | 70 -> 125 | .191254147 | 2.98619696
MT | 125 | 290 | 155 -> 80 | .107826332 | 3.67747924
MT | 150 | 290 | 185 -> 145 | .139994319 | 3.41993552
MT | 200 | 290 | 225 -> 185 | .0570821127 | 6.27313498
MT | 290 | 290 | 285 -> 315 | .126786727 | 8.27373464
dlPFC | 295 | 115 | 330 -> 295 | .0182282946 | 3.47337147
dlPFC | 310 | 115 | 345 -> 295 | .0628451898 | 3.89567446
dlPFC | 335 | 115 | 10 -> 295 | .0746549204 | 5.76576334
dlPFC | 25 | 115 | 50 -> 45 | .0185652925 | 6.66945652
dlPFC | 115 | 115 | 110 -> 115 | .0162567543 | .456233629

In each selected example the final score change exceeds original Delta/2; the margin theorem correctly does not CERTIFY invariance and actual chosen bin changes. The ten are deliberately hand-selected, so 10/10 switching is NOT an empirical switch rate. Three dlPFC controls with reward 115 converge to 295, but the other two do not. It is not a population-level winner-take-all mechanism proof.

Precisely: ORIGINAL AUTHOR WEIGHTS read and V8 independent recurrence RUN. Original AUTHOR PYTHON CODE NOT RUN; cross-runtime native Python weight replay NOT RUN. Local Python reproducer HAS an optional mode accepting the two original NPZ files with original Git-blob verification and expected ten-case numeric checks. It ran locally without the weights to reproduce target grid only. Do not describe it as completed source Python replay.

## 4. Reproducibility custody

Standalone local Python reproducer xh_s6_rot003_author_task_margin_and_weight_replay.py, 10438 bytes, SHA256 693ab9b8a3d0706d2a9ccf3980630b8a9e72f47705354cff2bc7b34c8dde7aa3.
Original full source-TARGET 1296-row CSV xh_s6_rot003_author_task_1296_conditions.csv, 95655 bytes, SHA256 022039e25663b1166ac090dc74a45c9008d58c20f9e6a096df684dbc8b4901b4.
Target summary JSON xh_s6_rot003_author_task_summary.json, 1366 bytes, SHA256 3e2b712dcf05dd1804eca0f2723ca007f20ba14ed719ab54ce4dcbc52df4b28c.
Connector-JS original-weight ten-sample record xh_s6_rot003_remote_source_weights10_results.json, 2109 bytes, SHA256 ab81743e84cd514f4407524a0e93d09f578087cb1db69ccd3a7832c59d4c5ad7.
Manifest xh_s6_rot003_manifest.json with original Git source-blob provenance and four SHA-256 payload hashes.

Local ZIP IW_XH_S6_ROT003_AUTHOR_TARGET_AND_WEIGHT_CONTROL_REPRO_20261112.zip, 18182 bytes SHA256 46f845d6220b1a9d944f7418b362a88e87e8cb26ee5640f177e3f187c9c3e0ba. ZIP CRC PASS; four source SHA-256 checks PASS; manifest PASS; clean isolated source-TARGET Python rerun full CSV and JSON BYTE-IDENTICAL PASS. No fake original monkey-data or native-weight Python replay.

## 5. Ceiling and next discriminator

The exact degeneracy and small target margins add source specificity to ROT002's established elementary score-margin theorem. They do NOT show the same margin distribution for actual trained score outputs. Next scientifically decisive source-native test would download two verified original NPZ files into a Python environment, run the optional cross-runtime replay and then expand to paired stimulated/unperturbed actual TRAINED output scores under source nonzero noise, stratifying by base margin, unit, shown and good directions. Any inference about monkey outcomes requires separate experimental data.

The original authors already describe different coding and intervention effects; this does NOT claim they overlooked margins, discovered a new neural mechanism, or made an error. No NEW physical/canonical/owner task is authorized.

STATUS: ROT003_SOURCE_TARGET_GRID_PASS / ORIGINAL_WEIGHT_V8_BOUNDED_CONTROL_PASS / SOURCE_PYTHON_WEIGHT_REPLAY_NOT_RUN / MONKEY_DATA_NOT_OBTAINED / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_OWNER_TASK_CASCADE.
