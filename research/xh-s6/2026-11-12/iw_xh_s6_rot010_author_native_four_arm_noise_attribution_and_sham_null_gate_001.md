artifact_id: IW_XH_S6_ROT010_AUTHOR_NATIVE_FOUR_ARM_NOISE_ATTRIBUTION_AND_SHAM_NULL_GATE_001_20261112
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
return_id: IW_XH_S6_ROT010_AUTHOR_NATIVE_FOUR_ARM_NOISE_ATTRIBUTION_AND_SHAM_NULL_GATE_001_20261112
result_class: ACTUALLY_EXECUTED_SOURCE_AUTHOR_NATIVE_34560_TRIAL_FOUR_ARM_NOISY_MICROSTIM_CONTROL + ACTUAL_SOURCE_8640_ROW_INDEPENDENT_AUDIT + MATURE_NOISE_VARIANCE_NEGATIVE_KNOWLEDGE
claim_ceiling: TWO_ORIGINAL_UNITS_60_SEEDED_BLOCKS_PER_72_DIRECTIONS_AUTHOR_NOISE_AND_TASK_CLASSES / NO_AUTHOR_250_REPETITIONS / NO_MONKEY_DATA / NO_REGION_CAUSAL_COMPARISON / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
status: COMPLETE_ACTUAL_AUTHOR_NATIVE_FOUR_ARM_34560_PASS / INDEPENDENT_8640_ROW_POSTPROCESS_PASS / BW_PENDING
created_at: 2026-11-12
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEUROBIOLOGICAL_UPGRADE / NO_OWNER_TASK_CASCADE
scientific_owner_firstness: original_Ruff_Markman_Kim_Cohen_authors

# XH-S6 ROT010 — Four-arm original-author stochastic RNN: baseline trial variability versus seeded microstimulation, with independent target-score audit

## 0. Executive result

ACTUALLY RAN a four-arm, TWO-UNIT source-frozen original RNN task/simulator experiment with source NONZERO noise and randomized reward/motion onsets, on exact original publicly available trained MT and dlPFC NPZ weights: **8,640 condition/seed/direction tuples times four source-native arms = 34,560 native author-model task executions**.

The four arms for EACH seed-block/direction condition:
A = base SHAM (source-original input noise, recurrent noise, and randomized cue/motion times);
B = base STIM with EXACT SAME seed and source stochastic trial stream (original stimulated unit and original strength);
C = alternate SHAM, genuinely independently seeded, producing different noise and generally different randomized onset timings;
D = alternate STIM with EXACT SAME alternate seed as C. Thus A-B and C-D are valid exact common-random-number contrasts. A-C is a true independent-sham stochastic NULL including both noise AND onset differences. A-D is an UNPAIRED mix of stimulation plus trial-to-trial variability. This source-controlled design is introduced by XH-S6 and is NOT claimed as the original paper's published independently sampled control distribution.

The actual scientific runner:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43312500997
Original source model code and fixed binary identity checks passed; source runner actual FINAL_RESULT_JSON emitted:
- 60 independent pseudorandom seed blocks per unit, each containing all 72 shown directions;
- MT unit37, strength11, reward center290 degrees: 4320 tuples, STIM under same noise changes choice 4307/4320 = 99.699074%; SHAM under independent noise+onset changes choice 2228/4320 = 51.574074%; UNPAIRED STIM changes choice 4293/4320 = 99.375%; independently paired alternative-seed stimulation changes choice 4305/4320 = 99.652778%.
- dlPFC unit53, strength45, reward center115 degrees: 4320 tuples, STIM under same noise changes choice 3067/4320 = 70.995370%; SHAM under independent noise+onset changes choice 2405/4320 = 55.671296%; UNPAIRED STIM changes choice 3383/4320 = 78.310185%; independently paired alternative-seed stimulation changes choice 3050/4320 = 70.601852%.
- For dlPFC this specific unpaired versus paired stimulus-change STATISTIC differs by +7.314815 percentage points (78.310185% minus 70.995370%). This is NOT an estimate of population MT vs dlPFC causal effect. Changing independent sampled noise/onset changes what the binary "different choice" measure counts.
- Across independently seeded A and C, random onset pairs differ for 4270/4320 MT and 4281/4320 dlPFC; A-C is a combined noise-plus-onset negative control, NOT pure noise isolation.
- First 12 seed blocks used exact old ROT009 seeds; MT 862/864 and dlPFC 616/864 original paired source choices reproduced exactly: REGRESSION PASS.
- Source task pair synchronization, exact original source RNN classes, exact pretrained original NPZ binaries, argmax margin sufficient-condition check zero violations: PASS.

No p-values or i.i.d. 34,560-trial standard error claims. The original directions within one 72-trial seed batch may be dependent; descriptive seed-cluster standard deviations across the 60 blocks are available in the full runner JSON.

## 1. Original source priority and mature method host

Original researchers: Douglas A. Ruff, Sol K. Markman, Jason Z. Kim, Marlene R. Cohen; Information formatting in neuronal populations predicts differential functional contributions to behavior, Nature Neuroscience published 10 November 2026, https://doi.org/10.1038/s41593-026-02514-7 . Authors themselves emphasize qualitatively different MT vector-averaging and dlPFC winner-take-all responses and reward-alignment interaction, NOT the raw percentage of any model choice change. Their RNN is a hypothesis generator and experimental animal microstimulation is a distinct empirical evidence class.

Original, ACTUALLY USED author GitHub repository https://github.com/solkm/formattingRNN at immutable source commit 7889a81e298c01532a313e02971c11dbc9db8eb0, exact blobs verified before runner import:
- generate_microstim_testdata.py source Git blob e7a6666e0b600ea49bab9755d302c78110ba9bc4, original units, strengths and noise values;
- DotsTasks.py Git blob ac9e789c69a8ea46ac38303f9d0db524886ba0a9;
- original psychrnn/backend/simulation.py Git blob d187595af592a888192bfc2dde6f562776b88423 and psychrnn/tasks/task.py b3bc5a5ca3fb2b0d2b4b79a4cd5ce8930e142865;
- circledots_fxns.py blob 909a65d84174a7eebb0e19273d06ae400dc9094f;
- ORIGINAL MTbroadsharp_m10.npz pretrained Git blob c5e701740f8ab1d19ca07415c0de2d6e7f88c37f and ORIGINAL DLPFCcombined_m4.npz pretrained Git blob 47142e3dee920a759406136449f0b12f9ce752ee.

Mature statistical prior art: common random numbers and blocking in paired stochastic simulation, comparisons of independent random trajectories, and the elementary argmax output-margin sufficient condition. NO priority or discovery claim for these devices. Different original units, stimulation strengths and reward centers mean that the MT/dlPFC percentage contrast in this bounded test cannot estimate a general between-area biological difference.

## 2. Controlled source/software custody

New XH public four-arm runner:
https://github.com/wmakiela-tech/Nash-iw-research/blob/4fde0106e78090b4042f5bcbfc5153188c0d0c4/research/xh-s6/2026-11-12/xh_s6_rot010_four_arm_source_noise_attribution.py
Source Git blob 6bccd63c0980481b4a53e1261ed1ef0ad92884bd, pinned FULL byte-exact GitHub readback PASS.

It imports the previous frozen ROT009 source simulator wrapper ONLY AFTER verifying the original ROT009 script Git blob 054299b6b0f0c0def7cfa6b3600d6f56665375ce, then uses the unchanged original author Task/MT BasicSimulator_linOut/dlPFC BasicSimulator source with the ORIGINAL binary weights and source RNG. For each unit, the two arms of a matched pair write the same one-hot source unit-selection vector to the last source W_in input column (including in sham), changing only the original source microstim strength. The author task noise is MT input0.4 recurrent0.2 and dlPFC input0.2 recurrent0.2; randomized cue onset 50..140ms and motion onset450..540ms on 10ms grid; source 72 directions in 5-degree bins. The XH script uses base seed formula starting with ROT009 original seed and alternate independent stream base+10000007.

New actual read-only workflow:
https://github.com/wmakiela-tech/Nash-iw-research/blob/763af3a177c1147b5997b42e20f698e480af5eb5/.github/workflows/xh-s6-rot010-source-noise-four-arm.yml
Source Git blob 2db2b4270e178bb6072d7d2eaa68f1bd210fc9a5; original author immutable checkout; Python3.11 NumPy2.1.3; GitHub Actions actual success run 43312500997, job 131511925335. No source-trained weights or source-owner files altered. All source experiment arms, not analytical invented scores, were executed.

The actual runner uploaded GitHub Actions artifact ID **13985983625**, archive name xh-s6-rot010-original-source-four-arm-noise-60-seeds, ZIP 282594B, source CSV 1,064,037 bytes, 8,640 rows; source runtime JSON 4059B, per-block rates JSON 22045B, stdout 3742B; artifact has 30-day retention. The artifact was actually DOWNLOADED and ZIP CRC verified; full CSV was actually independently read and audited in the local model environment.

ACTUAL persistent source runner 4059B JSON was parsed from real GitHub Actions job log (not inferred) and pinned public write/readback PASS at commit fe7f33e06e31bf129e57c223007b6f8750399668, Git blob 730cb849f9febf3a2e95e840d8727652b5c39efa:
https://github.com/wmakiela-tech/Nash-iw-research/blob/fe7f33e06e31bf129e57c223007b6f8750399668/research/xh-s6/2026-11-12/xh_s6_rot010_native_four_arm_60seed_actual_runner_summary.json

## 3. Independent full-data negative controls and original reward target

After REAL 8,640-row model run artifact was downloaded, a separate pure Python-standard-library independent postprocessor did NOT invoke any author RNN: it independently recomputed all flags and verified group identity, seed direction ranges, cue/motion time grids, stimulated unit/strength/reward settings, output angle bins, unique 60x72 source keys per module, argmax stability sufficient condition, first-12-block regression, and each aggregated numerator in the source runner summary. **8,640/8,640 structural/data checks PASS**, isolated clean rerun independent JSON BYTE-IDENTICAL PASS. This is an independent result audit, not an independent original model replay.

It also evaluated the author's exact original TRAINING TARGET reward at each of four actually observed output choices. Source function R(theta;shown,good) on 72 5-degree bins is zero if circular distance d(theta,shown)>45 degrees, else
R=[3.5+1.5 cos(1.8 radians(d(theta,shown)))][1+.75 cos(radians(d(theta,good)))].

Independent per-trial target score differences aggregated across 60 seed blocks:
- MT37: mean paired STIM target minus same-seed sham **-2.1930684316119824**; mean alternate independent SHAM minus base SHAM **+0.0024426277739049555**; mean alternate UNPAIRED STIM minus base sham **-2.2099629955213285**.
- dlPFC53: mean paired STIM source-target minus sham **-0.9217521235523092**; alternate independent SHAM minus base sham **+0.0011916008913492263**; alternate UNPAIRED STIM minus base sham **-0.9085627320017213**.

Here source model TARGET is neither the actual trained-score distribution nor observed animal behavior. The nearly zero independent-sham mean target delta does NOT mean independent sham choices mostly agree: over half differ, as above. Individual target-score changes vary substantially. The source authors' experimental effect descriptions (MT averaging vs dlPFC winner take all and reward alignment) are NOT reproduced merely by these aggregates.

Separate new negative control on ACTUAL prior ROT009 original source-output baseline trials: for every shown direction, all unordered distinct-seed pairs of 12 baseline choices, 12 choose 2 = 66 comparisons each; over all 72 directions 4752 dependent pair comparisons per module. MT null mismatch 2390/4752 = 50.2946127946%; dlPFC null mismatch 2590/4752 = 54.5033670034%. These are exact descriptive U-statistic summaries conditional on earlier finite simulated source draws; pair indicators are dependent, no standard binomial sample-size interpretation. New ROT010 independent A-C null frequencies 51.5741% MT and 55.6713% dlPFC are directionally consistent.

Full source row audit independently verified exact source data SHA hashes. Independent derived JSON from isolated clean Python re-execution SHA256 **39a1b41f041c4df870ca36c2335ecb7fa5cf570302a91e2e4fb71f78fd4ce6e4**.

## 4. Local complete reproducibility; limits

Full local complete user evidence ZIP:
IW_XH_S6_ROT010_ORIGINAL_SOURCE_FOUR_ARM_NOISE_ATTRIBUTION_REPRO_20261112.zip
- exact SIZE **296834 bytes**, SHA256 **b5aa3962b05432c44cf7b8cfabc5ec3e37ad2b998e924192f0a07d12aac083f2**;
- original ACTUAL source-runner 8640-row CSV, original source-runner summary JSON, source per-seed-cluster rates, original runner stdout;
- independent locally executed 8640-row audit source file and exact output JSON;
- independent original ROT009 12-seed unpaired sham U-stat source script and JSON, README, manifest.
- ZIP CRC PASS, ALL 9 included payload SHA256 PASS + manifest present;
- independent isolated local 8640-row audit output matched SHA256 exactly to prior output; source/summary cross-check PASS.
- The authors' original NPZ and repository source binaries are NOT copied into this archive; original immutable author Git source identifies them.

This source-native stochastic-control result is not full author's 72 x250 independent sampled per condition, not entire eight remaining source stimulated unit-strength configurations, not original paper MATLAB effects plot reproduction, and not experimental neural data. Do not treat unit-level differences as area-level effects. No formal biological inference, no causal MT/dlPFC region ranking or paper source novelty claim.

## 5. Scientific conclusion / stop condition

Source simulation indicates a major issue in using raw change/no-change percentages to infer effects: independent un-stimulated source trajectories differ for roughly HALF the shown directions under this stochastic task (54–56% dlPFC, 50–52% MT). In same-noise source model stim control, MT37 99.70% and dlPFC53 71.00% choices changed. The unpaired dlPFC stimulation comparison 78.31% differs substantially from the paired 71.00%, while its independent sham baseline 55.67% remains high. Thus meaningful source-model controlled perturbation comparison must condition on shared random noise/onset or use properly designed independent control statistics. Simply subtracting the sham flip rate from unpaired stimulus flip is NOT a general causal effect estimator, owing to nonlinearity and differing pairings.

No claim authors made this mistake. The original paper uses richer direction/reward-sensitive effects; this is an independent bounded negative methodological guard against over-interpreting the XH-S6 ROT009 flip frequencies.

Next progress only with a distinct scientific question: study actual direction shift geometry and reward alignment per author design, or full published per-angle 250-trial source sampling with source author analysis, if useful. No autonomous task cascade. Human Moderator, original authors and independent reviewers remain authority for scientific adoption.

BW GITHUB_PENDING_BW_INGEST not receipt; NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEUROBIOLOGICAL_UPGRADE / NO_OWNER_TASK_CASCADE.
