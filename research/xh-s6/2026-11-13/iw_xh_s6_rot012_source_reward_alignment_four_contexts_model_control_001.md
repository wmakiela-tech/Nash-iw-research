artifact_id: IW_XH_S6_ROT012_SOURCE_REWARD_ALIGNMENT_FOUR_CONTEXTS_MODEL_CONTROL_001_20261113
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
to_cell_or_route: IWTO_MODERATOR
return_id: IW_XH_S6_ROT012_SOURCE_REWARD_ALIGNMENT_FOUR_CONTEXTS_MODEL_CONTROL_001_20261113
result_class: ACTUAL_AUTHOR_NATIVE_TRAINED_MODEL_REWARD_CONTEXT_INTERVENTION_27648_EXECUTIONS / INDEPENDENT_13824_ROW_FULL_AUDIT / TARGET_RELATIVE_QUALITATIVE_HOST_SUBTRACTION / NEGATIVE_KNOWLEDGE
status: COMPLETE_SOURCE_NATIVE_27648_PASS / INDEPENDENT_ALL_13824_PAIR_SOURCE_AUDIT_PASS / PUBLIC_GITHUB_SOURCE_READBACK_PASS
date: 2026-11-13
claim_ceiling: ORIGINAL_AUTHOR_RNN_TASK_CLASSES_AND_TRAINED_WEIGHTS_WITH_3_NEW_REWARD_PARAMETERS / NOT_ORIGINAL_250_PER_DIRECTION_PROTOCOL_FOR_180 / NOT_MONKEY_DATA / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
guards: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEUROBIOLOGICAL_UPGRADE / NO_OWNER_TASK_CASCADE

# XH-S6 ROT012 — Reward-alignment perturbation in original trained source RNN: 4 reward contexts at common noise, 27,648 original-model runs and independently verified 13,824 paired conditions

## 0. Scientific motivation, author-original result, essential subtraction

Original scientific host and priority FIRST: Douglas A. Ruff, Sol K. Markman, Jason Z. Kim, and Marlene R. Cohen, Information formatting in neuronal populations predicts differential functional contributions to behavior, Nature Neuroscience, published on 10 November 2026, DOI https://doi.org/10.1038/s41593-026-02514-7 . Original paper distinguishes the largely reward-independent bias of MT microstimulation on ANIMAL behavior from strongly reward-condition-dependent dlPFC microstimulation, interpreted through information formatting. No originality claim is made for reward interactions, MT/dlPFC interpretation, model structure, stimulation method, or this qualitative direction of comparison.

ROT009 and ROT010 source model had only author generator's reward_rel=180 degrees relative to the stimulated unit's preference. ROT011 correctly found source-model MT preference-directed intermediate choices and dlPFC occasional exact preferred-bin capture for that FIXED reward context. Source original generate_microstim_testdata.py (author frozen Git blob e7a6666e0b600ea49bab9755d302c78110ba9bc4) line64 sets reward_rel=180. Source DotsTasks.MT_broadInSharpOut_withR offers explicit fix_reward parameter that can accept other reward centers. **ROT012's 0,90,270 offset changes are NEW XH-S6 SOURCE-MODEL TASK PARAMETER INTERVENTIONS**, not execution of the author's published reward_rel=180 microstimulation design and not original monkey trials. The 180 offset arm is a NEW SEED replication of author-like source configuration with 24 blocks, not a full 250 original trials/direction.

## 1. Actual original source model execution: all original identities and stochastic controls

Original author repository solkm/formattingRNN at immutable Git commit 7889a81e298c01532a313e02971c11dbc9db8eb0. Source model original trained binary weights MTbroadsharp_m10.npz Git blob c5e701740f8ab1d19ca07415c0de2d6e7f88c37f and dlPFC DLPFCcombined_m4.npz blob 47142e3dee920a759406136449f0b12f9ce752ee. Original source DotsTasks.py blob ac9e789c69a8ea46ac38303f9d0db524886ba0a9 and vendored psychrnn simulation.py blob d187595af592a888192bfc2dde6f562776b88423, plus source task/circle files. ALL source binary and code SHA identities were checked before import by frozen ROT009 source wrapper, itself independently pinned to public Git blob 054299b6b0f0c0def7cfa6b3600d6f56665375ce. Original author DotsTasks and BasicSimulator_linOut/BasicSimulator classes executed, not reimplemented neural recurrence.

Selected author-source units/strengths, unchanged:
- MT unit37, preferred angle 110 degrees, strength 11.
- dlPFC unit53, preferred angle 295 degrees, strength 45.
- Source input noise MT .4 dlPFC .2; recurrence .2 each, random source task ring onset 50..140ms and dots onset 450..540ms in 10ms slots; coherence .6, 120x10ms steps, original original-trained weights frozen. Both sham and stimulation arms select same source W_in one-hot stimulation unit, changing only the source Task strength.

FOUR original-source-task valid fixed reward centers per unit: preference + offset 0,90,180,270 modulo360. For EACH of 2 original source units: 24 pseudorandom seed-blocks x72 shown directions x4 reward contexts x2 stimulation arms, totaling **27,648 ACTUALLY executed original model Task+Simulator arm trials**, 13,824 original source-model paired records (1,728 per reward context per unit, 8 groups).

Precise common randomness: baseline vs stimulated arm has same original RNG and timings. In addition, ALL FOUR reward contexts use same source RNG streams/times within the same unit/seed/direction; reward is the only deliberately varied Task input parameter across contexts. Runner PASS 192 within-context RNG/onset identity checks (2x24x4), PASS 144 across-context RNG/time identity checks (2x24x3), deterministic sham duplicate exact final scores under 180 context at first block. Every record original argmax perturbation sufficient-preservation theorem checked: no violation. New pseudorandom seed sequence distinct from ROT009/010; no per-trial binomial error inference, 72 direction bins share seed-block-level stochastic draws.

ACTUAL original source GitHub Actions run **43427747836**, job 131893268402, status COMPLETED SUCCESS, all steps success:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/43427747836
ACTUAL original runner ZIP artifact **14038328546**, ZIP CRC PASS, contains source 13,824-row original-model CSV exactly 2,377,025 bytes SHA256 c1059b9edbcae86de025905eac93b69c23aaccf9a4fb2f09e2d9d1deb3279cc9, source runtime summary JSON 7956 bytes SHA256 f939a563c7417fd2142d549decb0ac9670f027d899ce2f5ae6cde6d4ae98f04f, actual_stdout.txt 6493 bytes. GitHub artifact has 30-day retention; complete source-output data preserved in attached local user reproducibility ZIP below.

Source program actually run and PINNED READBACK PASS:
https://github.com/wmakiela-tech/Nash-iw-research/blob/2841c839d37c72321ea07d3e6c16bc359d86f84f/research/xh-s6/2026-11-13/xh_s6_rot012_author_native_four_reward_alignments.py
Git blob 1424cfb627537f28f21128fbaee52e8dc9631592.
Source original run read-only workflow PINNED READBACK PASS:
https://github.com/wmakiela-tech/Nash-iw-research/blob/e1e2b891b9db42e19d5b558eddd96ef9dca8567a/.github/workflows/xh-s6-rot012-original-model-reward-alignments.yml
Git blob 5d0af8922a497de51dd9ae55e79426c15e905f9a.

Original ACTUAL runner model result JSON parsed from job log and permanently published with full pinned readback:
https://github.com/wmakiela-tech/Nash-iw-research/blob/e245b48caf027754e72d3a859619087dd9194c91/research/xh-s6/2026-11-13/xh_s6_rot012_author_native_reward_contexts_actual_runner_summary.json
Git blob 33543734dcc4fe63bbeecb275ecad59ebce812fd.

## 2. Primary numerical science: reward alignment changes both modules, differently

For EACH row, independently calculate the unsigned circular distance d(a,b)=abs(((a-b+180) mod360)-180), source-stim source model choice relative to original module unit preference. The author source reward target is NOT the experimental animal reward nor the trained model output score. Directional preference bias is measured by d(stim,pref)-d(sham,pref), so NEGATIVE means closer to model unit preference.

Each result below is actual 1,728 source-model paired cases (24 seed-blocks x72 directions) at fixed unit and stimulation strength:

Reward offset relative to unit preference 0,90,180,270:
- MT37 mean preference-distance delta (degrees): **-32.265625, -46.4467592593, -39.2332175926, -41.0706018519**. Strict interior of the UNIQUE shorter circular arc between sham choice and preferred direction, with antipodal source baselines excluded: **1434/1728=82.99%, 1278/1721=74.26%, 1478/1696=87.15%, 1190/1717=69.31%**. Exact stimulated preference-bin capture (P=110deg) **0/1728, 51/1728, 0/1728, 0/1728**.
- dlPFC53 exact selected source trained output choice equal preferred angle P=295deg (same order): **927/1728=53.65%, 795/1728=46.01%, 541/1728=31.31%, 744/1728=43.06%**. Mean preference-distance delta (degrees): **-20.9230324074, -15.6192129630, -16.7216435185, -22.5954861111**. Unique strict arc interior: **88/1728=5.09%, 103/1665=6.19%, 151/1684=8.97%, 82/1724=4.76%**.

The original author-source reward-relative 180 context reproduces ROT011's qualitative source-model finite pattern under new RNG blocks: MT source choice usually an INTERMEDIATE shorter-arc movement (1478/1696); dlPFC preferred single-bin capture in 541/1728, with many exact baseline/pref endpoint outcomes. The other three new reward center contexts show the shape is reward-conditional: BOTH source units' magnitude/capture measures change with reward alignment.

**Material negative-knowledge upgrade to ROT011 ceiling**: ROT011 observed exactly 0/4320 MT stim choices equal preferred P=110deg with author-original reward offset180. That DOES NOT imply MT can never choose its exact preferred output in other source reward contexts. New offset90 has 51/1728 EXACT preferred choices for the same unit and strength. Any former broad "MT never chooses preferred" claim is FALSE beyond its originally measured 180 context. We preserve original ROT011 fact as historical true conditional claim and explicitly block generalized reading.

Similarly original authors' "largely independent reward condition" refers to original biological/qualitative impact, not an exact MT invariant across every artificial modified reward cue. Here MT mean magnitude changes by 14.18deg across the four deliberately varied reward settings at fixed unit and strength. No contradiction to author paper claimed; no full model population conclusion.

## 3. Independent source-output row audit, source target and block-level sensitivity

ACTUAL source-runner artifact was downloaded, ZIP CRC PASS. Independently executed a separate pure Python stdlib source-row auditor (not another RNN):
- All **13,824** rows and source model correct unit/strength/preference/reward offset/shown direction/seed identity/times; EXACT all 24x72x4x2 source pair keys and same onset times across all four contexts PASS.
- Recomputed EVERY raw preference-geometry field and original source task reward TRAINING TARGET for sham/stim output at chosen bin, plus per-row final-output score perturbation/margin inequality. Original target formula from DotsTasks.py: for d(theta,shown)<=45 degrees, R=[3.5+1.5cos(1.8 radians(d(theta,shown)))][1+.75cos(radians(d(theta,reward)))] else R=0. The TARGET is NOT observed monkey behavior, not direct final RNN output and not post-trial experimental reward.
- Re-aggregated eight original-source runtime result groups, ALL original numerator counts, summary mean source training target and mean direction-distance fields; 8/8 groups EXACT counts and means agree to floating point tolerance PASS.
- Excluded ambiguous antipodal sham-preference cases when calculating strict unique shorter-arc interior (same guard as corrected ROT011). Conditions at d(sham,pref)=180 have TWO equal semicircles; must not count them as uniquely shortest.
- SOURCE training target mean stimulated minus sham is NEGATIVE for all eight groups. MT 0/90/180/270: **-2.50102/-2.89812/-2.25929/-2.38974**, dlPFC **-1.83538/-1.17537/-0.86298/-0.87798**. A choice closer to P is NOT necessarily higher source task training target, which also depends on shown angle and reward distribution.

A descriptive paired 4000-replicate bootstrap resampled WHOLE 24 seed blocks in parallel across reward contexts, never individual 72 direction trial rows as i.i.d. Biological confidence intervals and p-values are NOT claimed:
- dlPFC exact preferred output frequency offset180 MINUS offset0 = **-0.2233796296** (-22.34 percentage points); 95% descriptive seed-block resampling interval **[-0.2361111111,-0.2118055556]**, or -23.61..-21.18 pp.
- MT preference-distance shift (180 minus 0) **-6.967592593deg**, descriptive block interval **[-7.676504630,-6.270254630]deg**. This emphasizes MT is NOT invariant under this synthetic reward-centre intervention.
- dlPFC preference-distance shift (180 minus 0) **+4.201388889deg**, block interval **[+2.873263889,+5.535300926]deg**.
- Source stochastic/direction coupling remains native; this bootstrap describes source-model sensitivity conditional on THESE TWO specific selected source units and the tested changed reward contexts.

Original source CSV 2,377,025B cryptographic SHA256 c1059b9edbcae86de025905eac93b69c23aaccf9a4fb2f09e2d9d1deb3279cc9. Independent auditor 11,473B SHA256 392eb4e283c815814269b8b8b8d400c44f40d2c2d4f0496f7fadbd5a2703dbc8; independent JSON summary SHA256 e56b649e34f1b37454cf9374c1902a842821f215057f8d5ff89e71515f80e366. Derived per-seed CSV SHA256 86f4575dea54919c65152fcae1849c43e7c7b1ee5395b4694ee99227dea064d7, per-shown-distance CSV SHA256 1ecc073d9f5d1d67682407fa9a31783ce39eb42b9664ad471cda157ecc6f6cd8. Actual execution of isolated clean audit PASS: all three derived files re-created BYTE IDENTICALLY.

## 4. Reproducibility archive and limits

Complete XH-S6 ROT012 LOCAL ZIP, actually created and verified:
IW_XH_S6_ROT012_AUTHOR_NATIVE_REWARD_ALIGNMENT_FOUR_CONTEXTS_REPRO_20261113.zip
635638 bytes, SHA256 **6416ed6fd3d6b6224fd2097e8ce771c1fb20f63207ba2ee9ce777b3ce9d137c9**. Contains ACTUAL original Task/Simulator output all 13824 paired rows, actual runner JSON, stdout, separately executed independent auditor and 3 exactly reproducible numerical derived files, README and manifest. ZIP CRC PASS, all EIGHT payload SHA-256 PASS, manifest PASS; isolated clean rerun of independent output three files byte-identical PASS. Author original NPZ weights and source code are referenced by pinned Git, not redistributed. Original code is available in the authors' public repo; run the public workflow to execute actual original Task/Simulator again.

All source proof is numerical and model-internal: TWO specially chosen original units at DIFFERENT source stimulation strength and preferred angles, trained in author's particular pretrained models. No direct original author 72x250 Monte Carlo repetition for each source condition, no 18k original per unit source generator, no monkey recording or monkey behavior, no paper original full figure replica, no new mathematical theorem or neural mechanism. Non-author reward offsets0/90/270 may probe beyond the author's trained/evaluated distribution. No inference that MT as a brain area is mathematically reward-dependent and no refutation of original paper. Source original authors retain firstness and scientific acceptance.

No source new owner task cascade, referee approval, or ingested BW event; status GITHUB_PENDING_BW_INGEST. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.

## 5. Scientifically bounded verdict

ROT012 original author trained-source RNN under common random streams: dlPFC selected-unit exact-preference choice capture depends materially on reward alignment, consistent in direction with original paper's established qualitative interpretation, while MT selected-unit preference-directed shift remains common but NOT exactly invariant under altered reward inputs. In reward-offset90 MT can occasionally choose exact preferred angle, correcting any broad ROT011 inference. Source task training target generally decreases after the strong model unit stimulation for these fixed strengths and source noise conditions, but that target is not animal behavior.

CLASS: SOURCE_NATIVE_MODEL_PARAMETER_INTERVENTION / INDEPENDENT_POSTPROCESS / NEGATIVE_KNOWLEDGE.
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEUROBIOLOGICAL_UPGRADE / NO_NEW_TASK_CASCADE.
