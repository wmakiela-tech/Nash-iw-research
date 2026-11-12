artifact_id: IW_XH_S6_ROT004_AUTHOR_TRAINED_SCORE_VS_TARGET_AND_ONSET_GATE_001_20261112
exposure: PUBLIC
claim_ceiling: SOURCE_TYPED_ORIGINAL_WEIGHT_BOUNDED_ZERO_NOISE_FIXED_ONSET_SCORE_GATE__NO_ORIGINAL_PYTHON_WEIGHT_REPLAY_NO_MONKEY_DATA_NO_NOVELTY_NO_CANON_NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
task_id: IW_XH_S6_ROT004_AUTONOMOUS_EXTERNAL_SCIENCE_20261112
return_id: IW_XH_S6_ROT004_AUTHOR_TRAINED_SCORE_VS_TARGET_AND_ONSET_GATE_001_20261112
result_class: SOURCE_NATIVE_TARGET_VS_LEARNED_OUTPUT_DISCRIMINATOR + ORIGINAL_TRAINED_WEIGHT_BOUNDED_TEST + NEGATIVE_KNOWLEDGE
status: COMPLETE_WITH_CROSS_RUNTIME_ORIGINAL_WEIGHT_REPLAY_OPEN
created_at: 2026-11-12
acceptance_owner: Human Moderator; original research priority retained by source authors
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE

# XH-S6 ROT004 — Exact source-target ties do not imply trained-score ties; trained model can switch under allowed onset variation

## 0. Core result

The 18 EXACT TWO-WAY REWARD-TARGET ties identified in XH-S6 ROT003 have **no corresponding exactly tied output scores in an independent 18-condition calculation using the original public trained MT and dlPFC NPZ weights** at one explicitly fixed zero-noise source-allowed timing schedule.

For source target-tie trials good=0,20,...,340 degrees, shown=(good+180) modulo 360, the source target has equal top reward scores at shown±45 degrees. On the trained source-weight model, using t_ring=100ms, t_dots=500ms, noise=0, the 18 final top-two score margins are ALL strictly positive:
- minimum 0.0016968323606314506,
- median 0.04493284644658613,
- maximum 0.19728256680576362;
- only 6/18 source-target-tie conditions have trained margin <=0.02.

This means it was an INVALID transfer to treat the ROT003 TARGET-score small-margin frequency as a learned-model-output stability frequency. **The target and trained-output surfaces are distinct.** The authors never claimed their learned outputs equal the training targets exactly; the present observation does NOT establish an author error.

A second bounded check changed only source-allowed stimulus onset slots, running the same 18 trials at early (50,450ms), central (100,500ms) and late (140,540ms) [ring,dots]. There was a different chosen trained direction in EXACTLY ONE OF 18 source-target-tie conditions across these THREE FIXED onset schedules: good=80, shown=260; early and central choose 240deg, late chooses 225deg. Other 17/18 have the same winner for these three schedules, though margins vary. **This is a source-weight deterministic example, NOT a sampled stochastic onset effect rate.**

## 1. Original dated scientific hosts and source precedence

Original scientific authors: Douglas A. Ruff, Sol K. Markman, Jason Z. Kim, Marlene R. Cohen, *Information formatting in neuronal populations predicts differential functional contributions to behavior*, Nature Neuroscience, published 10 November 2026, https://doi.org/10.1038/s41593-026-02514-7 . Their separate actual monkey recording/microstimulation results are not reproduced; the present study addresses artificial trained RNN model input-output semantics only.

Author PUBLIC original code https://github.com/solkm/formattingRNN frozen commit 7889a81e298c01532a313e02971c11dbc9db8eb0 (2 Aug 2026). Source files actually read in XH-S6 ROT003 and reread as needed:
- python_code_data/DotsTasks.py original Git blob ac9e789c69a8ea46ac38303f9d0db524886ba0a9 (exact reward target at lines 72-84; natural random onset ring 50..140 and dots 450..540, 10ms increments).
- python_code_data/circledots_fxns.py blob 909a65d84174a7eebb0e19273d06ae400dc9094f (shortest circular degree distance).
- python_code_data/simulate_combined_model.py blob 0ccaadfd271c660a2a503b24f15b77ddede32962 (two-module connection, no-noise default, source test grid).
- python_code_data/psychrnn/backend/simulation.py blob d187595af592a888192bfc2dde6f562776b88423 (actual BasicSimulator and BasicSimulator_linOut equations).
- python_code_data/generate_microstim_testdata.py blob e7a6666e0b600ea49bab9755d302c78110ba9bc4 (source noisy stimulation; NOT replayed in ROT004).
- author ORIGINAL weights MTbroadsharp_m10.npz 908648 bytes, Git blob c5e701740f8ab1d19ca07415c0de2d6e7f88c37f; DLPFCcombined_m4.npz 903824 bytes, Git blob 47142e3dee920a759406136449f0b12f9ce752ee. Actually re-fetched via GitHub connector BASE64 and independently parsed ZIP stored NPY float arrays in connector V8. Original no-stimulation input last-column norm was exactly zero for both source weight files (verified).

Author README https://github.com/solkm/formattingRNN/blob/7889a81e298c01532a313e02971c11dbc9db8eb0/README.md points to model-test output data on Zenodo DOI https://doi.org/10.5281/zenodo.21764173. Original monkey microstimulation raw data are NOT included in repo and not accessed here. The 2025 bioRxiv version in README is not silently conflated with 2026 journal final publication.

Older host: winner-margin inequality Delta>2eps for unique argmax under sup-norm output score perturbation is elementary standard theory, XH-S6 ROT002 was a local explicit control but not a novelty claim. ROT003 original TARGET ties were source-native, not learned output ties. ROT004 resolves that evidence-level mismatch with original NPZ weights and timing variation.

## 2. Exact source target symmetry — independent local Python proof/replay

The author 72-output reward target for shown s and reward center g, angular circular shortest distance d, candidate angle theta=5i, i=0..71:
For d(theta,s)<=45:
R(theta)= [3.5+1.5 cos(1.8 d(theta,s) pi/180)] * [1+0.75 cos(d(theta,g) pi/180)];
otherwise R(theta)=0.

For g=s+180 mod360, theta=s-45 and theta=s+45 have identical source target rewards by circular reflection. Both are top scores (independent finite 72-bin check per condition). These EXACT 18 TARGET ties were rechecked by a fresh standalone NumPy Python script; max reflected double-precision numerical difference 0, target winner-runner margin 0 under standard selected angles. Source-target audit is reproducible locally without the original .npz and is NOT a trained-model computation.

## 3. ORIGINAL trained weights — bounded code-faithful model calculation in connector V8

Independent local-to-connector computational distinction is essential:

ACTUALLY EXECUTED:
- Retrieved original author binary NPZ weights through GitHub connector and parsed in V8 as matrices of float32 values elevated to float64 numerical computation.
- Propagated full original source two-module recurrence for 120 simulation steps, dt=10ms, tau=100ms, alpha=0.1:
  h_new=(1-alpha)h+alpha[W_rec ReLU(h) + W_in u + b_rec];
  MT output=W_out h_new+b_out (LINEAR);
  dlPFC output=W_out ReLU(h_new)+b_out.
  dlPFC input feeds 72 directional MT-output channels 2:74 on each step.
  MT reward cue if time>=ring, MT motion if time>=dots; dlPFC reward cue time>ring. Untrained stimulation input channel remains zero (no applied stimulation here).
- Original source uses random ring 50..140ms / dots 450..540ms, 10ms steps. The three chosen source-permitted pairings (50,450), (100,500), (140,540) are *deliberate deterministic probes*, not an empirical sample from random onset law.
- Set ALL input and recurrent noise=0. This isolates source dynamics and differs from author's noisy multi-trial stimulation model. This is NOT animal data.
- Ran 18 opposite s/g trial combinations at each of three schedules =54 independently computed SOURCE-WEIGHT final model outputs and their top-two margins. Repeated central reference cases previously computed in ROT003 reproduce exactly within displayed numeric precision: reward290,shown110 -> choice70, margin .1912541466; reward115,shown295 -> choice330, margin .0182282946. Both original source NPZ weight arrays are 150 recurrent units, correctly selected MT linear and dlPFC ReLU readouts.

NOT RUN:
- Original author's Python/PsychRNN modules on source weights. The independent numerical implementation uses the same mathematical recurrence, but not the actual author Python execution.
- A local Python cross-runtime replay on original NPZ, because the Python container could not access the original raw GitHub binary files. Author GitHub connector exposed the NPZ bytes only inside connector V8. A *complete optional* Python cross-replayer is provided in the reproduction package but its SOURCE-WEIGHT option HAS NOT BEEN EXECUTED.
- Any original noisy 18000-trial microstimulation simulation, training run, monkey activity or published scientific effect sizes.

Thus report precisely: independent V8 source-weight execution PASS, target Python source-math PASS, native Python source-weight cross-check PENDING.

## 4. Observed learned-output margins and time sensitivity

For central (100,500ms) among all 18 original source target-tie conditions:
- target exact tie count 18, independent learned output exact ties <=1e-12: 0;
- trained margin min 0.0016968323606314506; median 0.04493284644658613; max 0.19728256680576362;
- trained margin <=0.02: 6/18; source target margins: 18/18 exactly zero.

For all three timings, 18 conditions yield 54 trained-score margins: global min 0.0001767761240261123, global max 0.21282685392767187.

One source-permitted timing-dependent winner example:
- shown=260deg, good=80deg (a target exact tie):
- (ring50,dots450): learned choice240deg, margin 0.0487357590889701.
- (ring100,dots500): learned choice240deg, margin 0.014153417139922464.
- (ring140,dots540): learned choice225deg, margin 0.03085773842107198.

The other 17 target-tie input pairs did not change their winner across these three specifically chosen timing schedules; this is not a proof of immunity over all 100 source-allowed ring x dots combinations or under noise. No 1/18 chance or experimental frequency claim.

We observed no actual learned exact tie in the central 18. A margin bound calculated on the TARGET surface is NOT automatically a bound for this learned output. This is a material evidence-type downgrade/correction to any aggressive transfer inferred from ROT003. Neither this correction nor the timing witness falsifies authors' central formatting interpretation; their actual evidence uses recordings and interventions beyond a learned reward-target array.

## 5. Negative-knowledge / scientific discriminator

The only certified new XH result is that this public trained source-weight model in a bounded deterministic test does not preserve the exact reward-target ties, and an allowed onset shift can produce a different winner. Thus the proper experimental/model target is source-trained pre/post score margin stratified by actual condition, onset, stimulus unit and intervention-induced score delta. An actual physical neural-formatting claim requires real animal data and original code replay / validation; neither is authorized as inferred.

The toy latent gauge from ROT002 is NOT treated as a physical reparametrization of the authors' 150-unit Dale-constrained trained RNN. No novelty or full model nonidentifiability claim.

## 6. Local reproducibility package: what replay passes / remains open

Files:
1. xh_s6_rot004_original_source_weight_onset_gate.py (standalone independent Python source target math; optional original NPZ 54-case cross-check), 7730 bytes, SHA256 3269f97532b50ae9a7627acab54dd23f565fccadef0af0055d4d7e94a83e297b.
2. xh_s6_rot004_original_weights_18x3_observations.csv (54 numerical V8 independent source-weight observations), 1557 bytes, SHA256 ed3bd2e8713d7190ba5bc48fc1d6a0b4d725b934914567ec51ff902ee2a784dd.
3. xh_s6_rot004_summary.json (precise evidence and no-replay status), 1231 bytes, SHA256 1a33489368d7fccd890bac1691bc7fa131ccd1cbe6f0d51ae9130a9bafdd2374.
4. xh_s6_rot004_README.md, 2087 bytes, SHA256 c75cd3bbdee3dc8727b180095e006010c7dfa4eaaff92cff32bf09a8368e6796.
5. xh_s6_rot004_manifest.json (four payload hashes + original Git blob identities + status).

ZIP: IW_XH_S6_ROT004_AUTHOR_MODEL_MARGIN_TIMING_REPRO_20261112.zip, 7101 bytes, SHA256 af75a0d8ec54ab4d4319d6d0adda8866a9e874c4d0d5dd1d054396022988730f; ZIP CRC PASS, all four payload SHA PASS, manifest PASS. Fresh isolated Python run reproduces target-math and checks archived original-V8 observations, emitting summary JSON BYTE IDENTICAL PASS. IMPORTANT: this clean isolated run DID NOT re-run 54 original trained-weight outputs because the original .npz bytes are not present locally. This is explicitly documented, not hidden.

Optional next action, NOT yet executed: retrieve original author's frozen MT and dlPFC NPZ binaries to the same local Python runtime and run:
python xh_s6_rot004_original_source_weight_onset_gate.py --mt-weights MTbroadsharp_m10.npz --dlpfc-weights DLPFCcombined_m4.npz.
This checks both exact original Git blob SHA1 values and 54 learned winner/margin outputs with numeric tolerance 2e-5. No claim this currently passed.

## 7. Final scope

XH-S6 ROT004 COMPLETE SOURCE_TYPED_BOUNDED_ORIGINAL_WEIGHT_TEST, with full native Python cross-runtime verification still OPEN. Source paper authors retain firstness; no author bug alleged; no actual neural intervention/animal validation/clinical inference; no own novel theorem or scientific CANON. Cross-cell physical E4 remains BLOCK, no owner task cascade. BW state GITHUB_PENDING_BW_INGEST not an ingestion receipt.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_NEW_TASK_CASCADE.
