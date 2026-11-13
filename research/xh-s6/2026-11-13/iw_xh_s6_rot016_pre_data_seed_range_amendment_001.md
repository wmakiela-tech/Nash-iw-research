artifact_id: IW_XH_S6_ROT016_PRE_DATA_NO_MODEL_EXECUTION_SEED_RANGE_AMENDMENT_001_20261113
exposure: PUBLIC
date: 2026-11-13
parent_preregister_commit: c3dd0dfbf30aa5191a8b9dc391efb042c3d0835f
parent_preregister_blob: 932b70a33357b3895845fa23193f404f739d2ad1
incident_failing_actions_run: 43464355933

# ROT016 explicit PRE-DATA source NumPy legacy RNG seed range amendment

Initial ROT016 preregistration froze mathematical seed key as:
key = 202611160000 + 500003*int(module=="DLPFC") + 3109*unit + 1009*block, block=0,...,23.

The FIRST actual GitHub Actions run failed immediately on first source model call, BEFORE ANY 72-trial source model batch could be computed, because the author's original source NumPy global RNG is seeded with np.random.seed(seed+171717), which REQUIRES seed+171717 in [0,2**32-1]. The 12-digit key is out of this legacy range. The log's sole fatal exception was ValueError "Seed must be between 0 and 2**32 - 1"; empty CSV header and error stdout are NOT scientific outcome data. Do not classify this engineering failure as a biological/model falsification.

Before generating ANY ROT016 source science outcomes, specify a deterministic, disjoint, fully reproducible mapping from unchanged preregistered key to the ORIGINAL source's admissible RNG integer:
source_seed = key % (2**32).
The mapped seeds for all 10 original selected units and 24 blocks are far below (2**32 - 171717), satisfying the source np.random.seed(source_seed+171717). The key formula itself and all scientific criteria, cutoff 5deg..65deg, reward_rel180, original sources, original weights, original 24 blocks/unit, ten units, all labels and unaltered source Task classes remain UNCHANGED. The original seed key and mapped source_seed may both be recorded in the output row. We do not choose seeds based on observed model outcomes.

No source model choice outcome existed before this amendment; the original author model failed at legacy seed initialization. Parent preregistration remains immutable. This amendment must be GitHub written and read back with commit/blob identity before re-execution. It is not a retroactive redefinition after seeing a scientific result.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE.
