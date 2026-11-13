artifact_id: IW_XH_S6_ROT016_PROSPECTIVE_HOLDOUT_GAP_SOURCE_PREREGISTRATION_001_20261113
date: 2026-11-13
exposure: PUBLIC
from_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_05 / XH-S6
status: FROZEN_BEFORE_NEW_SEED_SIMULATION

# ROT016 – Prospective frozen-gap holdout falsifier, committed before output exists

Scientific source and firstness: Ruff, Markman, Kim, Cohen, Nature Neuroscience (2026-11-10), DOI 10.1038/s41593-026-02514-7. This is a reproducibility/generalization exercise on their publicly available original trained artificial RNN and source Task/PsychRNN classes. Not a novel biological observation or an animal trial.

SOURCE frozen: original solkm/formattingRNN commit 7889a81e298c01532a313e02971c11dbc9db8eb0; original MT and dlPFC NPZ, author-selected all 5 MT and 5 dlPFC units/strengths/preferences extracted from source original generate_microstim_testdata.py SHA Git blob e7a6666e0b600ea49bab9755d302c78110ba9bc4, original reward relative 180 degrees and original nonzero input/recurrent noise. Source Task/Simulator called directly; NO rewritten recurrence.

Prior observed ROT014 empty dlPFC source output annulus of angles at d(stim,P) equal to 5,10,...65 degrees. The cutoff 65 was chosen posthoc using the old ROT013 16-block data. ROT015 showed true source preference P was the only one among 72 hypothetical angular labels with zero count for all 5 dlPFC source units, but this was still old data. The ROT016 holdout freezes that very same cutoff *before* collecting new original model output on fresh disjoint pseudorandom source streams.

PREDECLARED INPUTS: 24 new seeded blocks per all ten original source-selected units x72 original stimulus direction bins x2 arms (stim/sham) = 17,280 paired task records, 34,560 executed native original author-model Task+Simulator arm trials. Source classes original, original author strength, original source reward_rel180. Seed formula (integer):
seed=202611160000+500003*int(module==DLPFC)+3109*unit+1009*block_index, block_index=0..23. ROT013 old formula was 2026111300 +500003*int(module==DLPFC)+3109*unit+1009*block_index, 0..15. New seed streams thus disjoint from prior source model. Same original source nonzero input and recurrent noise and original onset within each stim/sham pair. All 72 source shown absolute 5deg directions per seed block.

PRIMARY FALSIFIER PER DLPFC UNIT (five units, old data never incorporated): count of stimulated selections with circular distance to source true P in 5deg..65deg MUST EQUAL ZERO. Any nonzero count is a PRESPECIFIED FAIL for that source unit (no cherry picking, not a run/code failure; preserve all data). SECONDARY (stronger) falsifier per DLPFC unit: among all 72 possible 5deg angular labels L, true P is the UNIQUE label with zero count in 5deg..65deg annulus. If false label also zero OR P nonzero, secondary claim fails. THIRD negative control per source MT unit: zero-count labels among all 72 should be NONE; any zero is a recorded falsification. FOURTH no-op vs stimulus sham negative: compare true P annulus sham count and stimulated count, and exact unit capture counts; do not infer p-value from alternative labels. The posthoc 65-cutoff from ROT014 is here FIXED BEFORE new data, which is a new *independent pseudorandom model-run holdout*, not independent subjects, models or biology.

INTEGRITY: source original author Git and frozen source utility commit SHA fail closed; paired RNG/time digests match; bitwise repeated no-stim one seed per unit; source target and margin controls; 10x24x72 exact input grid. A scientific falsification MUST be reported as source-model numerical finding, not interpreted as CI failure. Whole-seed-block 95-percentile bootstrap only descriptive; nominal 72 labels are not physically exchangeable neural preference and no permutation p-value.

Negative knowledge: all ten source-selected original units in the same ONE frozen MT+dlPFC trained source network pair, with curated original author stimulation strengths; NOT author 250 original repetitions per angle, original trial sequence or monkey observations. No medical claims, new neuronal mechanism, source author error claim or scientific firstness.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE.
