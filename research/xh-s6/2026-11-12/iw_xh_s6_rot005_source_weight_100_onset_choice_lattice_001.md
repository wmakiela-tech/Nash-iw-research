artifact_id: IW_XH_S6_ROT005_SOURCE_WEIGHT_100_ONSET_CHOICE_LATTICE_001_20261112
exposure: PUBLIC
claim_ceiling: SOURCE_ORIGINAL_WEIGHT_V8_100_FIXED_ZERO_NOISE_ONSET_GRID__NO_ORIGINAL_PYTHON_REPLAY_NO_MONKEY_DATA_NO_NOVELTY_NO_CANON_NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
task_id: IW_XH_S6_ROT005_AUTONOMOUS_EXTERNAL_SCIENCE_20261112
return_id: IW_XH_S6_ROT005_SOURCE_WEIGHT_100_ONSET_CHOICE_LATTICE_001_20261112
result_class: SOURCE_NATIVE_FINITE_ONSET_LATTICE + BOUNDED_ORIGINAL_WEIGHT_INDEPENDENT_NUMERICAL_TEST + NEGATIVE_KNOWLEDGE
status: SOURCE_WEIGHT_V8_ONSET_GRID_PASS / SOURCE_WEIGHT_PYTHON_LOCAL_REPLAY_OPEN
created_at: 2026-11-12
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE

# XH-S6 ROT005: full original source 100-onset lattice in one trained-RNN condition

## 0. Tested result

At fixed motion direction shown=260 degrees and reward-center direction good=80 degrees, in the original authors' trained two-module RNN, independent deterministic propagation with original binary weights and ZERO input/recurrent noise produces:
- final output argmax = 240 degrees for 78 of the exact 100 permitted onset configurations;
- final output argmax = 225 degrees for 22 of the 100 configurations;
- no third chosen output direction in this finite set.

Author DotsTasks.py samples ring onset with 10*rng.integers(5,15), giving 50,60,...140ms, and dots onset with 10*rng.integers(45,55), giving 450,460,...540ms. The two separate RNG calls are uniform and independent in this source construction. Therefore 78/100 and 22/100 are exact finite-lattice fractions **CONDITIONAL ON THIS ONE INPUT, ORIGINAL TRAINED WEIGHTS, ZERO NOISE AND UNIFORM INDEPENDENT ONSETS ONLY**. They are not animal choice probabilities, published RNN microstimulation response frequencies, or neuroscience population generalizations.

Breakdown by dots onset:
- 450, 460, 470, 480, 490, 500, 510 ms: 10/10 cases choose 240 degrees;
- 520 ms: 5 choose 240 and 5 choose 225;
- 530 ms: 3 choose 240 and 7 choose 225;
- 540 ms: 10/10 choose 225.

Equivalent threshold by ring onset: ring 50/60/70 -> choice 225 first at dots 540; ring 80/90 -> choice 225 first at dots 530; ring 100/110/120/130/140 -> choice 225 first at dots 520. Hence exact 225 count 3*1+2*2+5*3=22.

Selected original-weight output margins:
- ring 50,dots 450: chosen 240, top-two margin .0487357590889701;
- ring 100,dots 500: chosen 240, top-two margin .014153417139922464;
- ring 140,dots 540: chosen 225, top-two margin .03085773842107198;
- ring 80,dots 530: chosen 225, margin .0005168025944715104, full score225=1.539334991151509 and score240=1.5388181885570376;
- ring 100,dots 520: chosen 225, margin .0009735252658837901;
- ring 130,dots 510: chosen 240, margin .0014092333212580854.

This extends XH-S6 ROT004's THREE selected schedules to complete source-permitted 100-slot onset support for exactly ONE source condition. It does not extend to other motion/reward pairs without new computations or to arbitrary continuous onset times.

## 1. Original article and exact source lineage

Original authors retain full scientific priority: Douglas A. Ruff, Sol K. Markman, Jason Z. Kim, Marlene R. Cohen, Information formatting in neuronal populations predicts differential functional contributions to behavior, Nature Neuroscience 10 Nov 2026, DOI https://doi.org/10.1038/s41593-026-02514-7.

Author repository https://github.com/solkm/formattingRNN at pinned commit 7889a81e298c01532a313e02971c11dbc9db8eb0.

Source Git blobs actually inspected:
- python_code_data/DotsTasks.py: ac9e789c69a8ea46ac38303f9d0db524886ba0a9, exact reward target and independent integer onset calls.
- python_code_data/circledots_fxns.py: 909a65d84174a7eebb0e19273d06ae400dc9094f, circular angles.
- python_code_data/simulate_combined_model.py: 0ccaadfd271c660a2a503b24f15b77ddede32962, test configuration and two-module connections.
- python_code_data/psychrnn/backend/simulation.py: d187595af592a888192bfc2dde6f562776b88423, original BasicSimulator and BasicSimulator_linOut mathematics.
- python_code_data/generate_microstim_testdata.py: e7a6666e0b600ea49bab9755d302c78110ba9bc4, source authors' different NOISY stimulation experiment, NOT reproduced here.
- SOURCE TRAINED MODEL: original MTbroadsharp_m10.npz, 908648 bytes, Git blob c5e701740f8ab1d19ca07415c0de2d6e7f88c37f; DLPFCcombined_m4.npz, 903824 bytes, Git blob 47142e3dee920a759406136449f0b12f9ce752ee. Both were directly fetched via connected GitHub in base64 and parsed as ZIP-stored NumPy matrices in the connector V8 environment. Both contain 150-unit recurrent weights.

The authors' original README refers to Zenodo https://doi.org/10.5281/zenodo.21764173 for model test data; monkey experimental data are not stored in this repo. Neither external data archive nor monkey data was obtained by ROT005.

## 2. Source-faithful bounded experiment — what was and was not run

ACTUALLY RUN:
- Decoded original author trained weight binaries in connector V8; original Git blob SHAs and matrix shapes reported.
- Independently implemented equations h_new=(1-alpha)h+alpha*(W_rec ReLU(h)+W_in u+b_rec), with alpha=.1, dt=10ms, tau=100ms, 120 steps.
- MT readout linear W_out*h_new+b_out, dlPFC readout W_out*ReLU(h_new)+b_out. Two source reward-cue onset inequalities (MT >=ring and dlPFC >ring), source MT motion onset >=dots, 72-channel MT-to-dlPFC input interface, directional coherence 0.6. Source unused stimulation columns zero and not activated.
- Forced both input noise and recurrent noise to zero, and executed exactly 10 ring starts by 10 dots starts for shown=260,good=80.
- The three ROT004 source-weight control cases match exactly within displayed precision.
- Compiled all 100 chosen bins into an immutable public CSV.

SOURCE TARGET VS LEARNED SCORES: at shown=260 and good=80, the original training target has two exactly equal global reward maxima at theta=215 and 305 degrees (reflective ±45 degree symmetry). This is independently validated in local Python using the original source mathematical formula. Trained output choices under this 100-grid were 225 and 240 degrees; consequently the observed change is **NOT** a switch between the two target maxima branches. Treating it as such would be a false scientific inference.

NOT RUN:
- Authors' own Python/PsychRNN code, model training, stochastic microstimulation model, any animal recording or perturbation experiment.
- The optional local NumPy source-weight 100-case replayer, due to original NPZ binary absent in local Python container (despite GitHub connector access). Network transfer from raw GitHub to the Python container failed. NO original-weight Python local PASS claimed.
- No source-wide 1296-condition target-to-trained-output comparison or full statistical confidence interval.

The user-facing 22% is only the exhaustive conditional count under the stated original-source onset law and imposed zero noise. It is not an empirical biological frequency.

## 3. Verifiable public and local output custody

Public exact 100-choice CSV GitHub WRITE + PINNED byte-exact READBACK PASS:
https://github.com/wmakiela-tech/Nash-iw-research/blob/561845d635f943d355eeada5b37f07a0b5b406d3/research/xh-s6/2026-11-12/xh_s6_rot005_100_onset_choice_grid.csv
Git blob 6efa0f2e34fbc6feca1a55d79bd9faf14204d88e matched local actual git hash-object. Source CSV 1278 bytes, SHA256 83fdfbff8a96ef3914635ac5ebf36114943a0e6e96428b9a708b65fdc8df7cbf. The public CSV holds all 100 chosen bins, not all individual scores or per-case margins.

Local independent Python verifier: xh_s6_rot005_optional_author_npz_replay.py, 5462 bytes, SHA256 449ddfa2655d90be5acaadbdc49243596a1dd6b5b2cfe4d6d4f0dacc9f1b3383. It has TWO distinct modes:
- no binary: actually run locally; exact 100-row receipt and original author reward-target symmetry PASS; source-weight calculation NOT_RUN_NO_NPZ.
- with both original source NPZ: checks true original Git SHA-1 blob identities, then independently calculates all 100 source trained outcomes in NumPy, verifies winners and selected margins within 2e-5. THIS MODE WAS NOT EXECUTED and must not be counted as PASS.
A separate fake NPZ test confirms incorrect original Git blob is correctly rejected (fail-closed PASS).

Local supplementary boundary receipts JSON: 1945 bytes SHA256 5aed83b4c01fb401e8dfdc9c0db17d8a01c2de9c760d450511f163a91225d9d7.
Local README.md: 3791 bytes SHA256 a4b2bb4448eb6a52630c29de8ede78c153874e2d858015a81e045b4b187a89bc.
Local manifest lists four payload SHA256 identities.
Local full reproducibility ZIP IW_XH_S6_ROT005_SOURCE_WEIGHT_100_ONSET_LATTICE_REPRO_20261112.zip: 6925 bytes, SHA256 745838935e2c03b181c72ad3c35cb6dbc473e006da4591bbab0466dae839c1e2. CRC PASS, 4 payload SHA PASS, manifest PASS; clean standalone no-binary receipt/target replay PASS. This ZIP does NOT contain original NPZ source binaries.

## 4. Claim ceiling

This is an independent bounded original-trained-RNN conditional numerical finding, not an original-source Python replay, neuron science claim, priority claim, physical upgrade, nor evidence for or against the actual authors' experimental results. It is a useful readout and timing confound guard. BW ingest, external referee, owner adoption, CANON or EXEC_SIGN not presumed.

STATUS: XH-S6_ACTIVE / ROT005_SOURCE_WEIGHT_V8_100GRID_PASS / SOURCE_TARGET_PYTHON_PASS / FULL_ORIGINAL_WEIGHT_PYTHON_CROSSREPLAY_OPEN / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_OWNER_TASK_CASCADE.
