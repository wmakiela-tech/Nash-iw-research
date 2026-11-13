artifact_id: IW_XH_S6_ROT018_ORIGINAL_AUTHOR_STOCHASTIC_DIRECTION_SCHEDULER_VS_BALANCED_250X72_PREREG_001_20261113
date: 2026-11-13
exposure: PUBLIC
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
state: SCIENCE_PROTOCOL_FROZEN_BEFORE_NEW_SOURCE_TASK_EXECUTION

# XH-S6 ROT018 — Original Task trial-scheduler versus balanced ROT017 250-per-direction design

## Original scientific source and provenance
Ruff/Markman/Kim/Cohen, Nature Neuroscience Nov 10 2026 DOI 10.1038/s41593-026-02514-7, original public code solkm/formattingRNN@7889a81e298c01532a313e02971c11dbc9db8eb0. Original python_code_data/generate_microstim_testdata.py pinned Git blob e7a6666e0b600ea49bab9755d302c78110ba9bc4 sets N_testbatch=72*250, fix_shown=(preferred+np.arange(0,360,5))%360, fix_reward=[preferred+180] and calls MT_broadInSharpOut_withR with N_batch=N_testbatch/fix_shown/fix_reward WITHOUT test1ofEach=True.

Original DotsTasks.py pinned Git blob ac9e789c69a8ea46ac38303f9d0db524886ba0a9 MT_broadInSharpOut_withR.__init__ defaults test1ofEach=False; generate_trial_params under default executes shown_deg=rng.choice(self.fix_shown). Original Task base psychrnn/tasks/task.py Git blob b3bc5a5ca3fb2b0d2b4b79a4cd5ce8930e142865 executes generate_trial_params then generate_trial for each source input trial. Therefore original source N_batch18000 means 18000 RANDOM choices among72 allowed angle bins, not 250 forced for every bin. ROT017 instead ran 250 seeded 72-direction blocks with test1ofEach=True, exactly 250 each. Its earlier characterization as matching the authors' per-angle repeats is WRONG AS A PROTOCOL IDENTITY, although source generator E[count_per_angle]=18000/72=250.

## Frozen design before new source execution
Execute EXACT original-author source MT task and original vendored Task class, NO trained-network simulation for this narrow source-input-scheduler control. Select original author dlPFC-stim unit25 P160 and unit53 P295, original strength45 (no MT stimulation), source task input noise .4 coherence[.6], reward center P+180, random cue/motion onsets and fix_shown=(P+[0,5,..355])%360, test1ofEach left at default False, N_batch=18000.

Two fixed new XH source RNG seeds: unit25=1900000025 and unit53=1900000053, initialize DotsTasks.rng=np.random.default_rng(seed), legacy NumPy np.random.seed(seed+171717). Initial SMALL-batch identity controls for each source condition at N_batch=72:
(A) native Task.get_trial_batch();
(B) lower-memory streaming loop mirroring Task implementation: for trial0..71, p=task.generate_trial_params(1,trial) then x,y,m=task.generate_trial(p), no changes to source methods.
Require EVERY source trial parameter, EVERY MT source input+target+mask array byte-identical between methods, plus final exact source RNG state. If identity fails, no full-batch equivalence claim.
Then stream original source Task method on 18000 source trials for each source condition, generating the ORIGINAL MT source trial input/noise and discarding x/y/m after each trial, which consumes native source RNG exactly as original source Task generator but avoids storing all huge input/target/mask arrays. Record source-native 18000 trial parameters in CSV for each source selected condition, 72 shown-bin counts and randomized 10x10 onset grid.

PREDECLARED F_COUNT: if any source shown direction count not 250, the actual random source scheduler's finite count differs from ROT017's forced-balanced exactly250 per bin. Even accidental all-balanced counts would not change code-level random-selection semantics. Report min, max, number bins different250, source RNG and source timing frequency, missing bins (if any), actual numbers.

Conditional projection using prior ROT017 ACTUAL original-RNN outcomes, exact source CSV SHA256 29f9b48d60b60c031fdca8a37483a969c2b470086f30f3ec5ebcbbb77c65530f and source model runner JSON SHA256 083db441c66dfb3ed4124be2742b34a5fd8ea03474d7a25d221851f5a99157f4. Let k_i be exactly observed ROT017 model annulus event count among250 source stim model outputs for shown angle i, n_i source 18000 native Task scheduler generated shown-angle count. Compute ONLY a deterministic source-data occupancy projection: projected expected count E=sum_i n_i*(k_i/250), contrasted with original balanced observed count sum_i k_i. This is NOT a new trained model simulation and NOT an actual one-batch RNN result. No causal effect or animal inference. Its purpose is to quantify whether source input composition could change an already rare aggregate count if per-direction response frequencies were held fixed. Do not infer binomial p from alternative labels. Preserve complete per-direction k_i.

No original MT/dlPFC neural recurrence run this rotation; no original author one-shot 18000 Task+RNN run, no monkey trials. Both source classes and original model source identities pinned. Independent audit, clean replay and negative mutation as budget allows. Report code-level and actual-source generation truth separately from synthetic conditional projection.

BW GITHUB_PENDING_BW_INGEST. NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE.
