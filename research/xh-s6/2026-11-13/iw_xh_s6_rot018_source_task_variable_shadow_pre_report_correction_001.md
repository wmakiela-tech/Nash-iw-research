artifact_id: IW_XH_S6_ROT018_SOURCE_TASK_METADATA_RUNNER_NONSCIENTIFIC_VARIABLE_SHADOW_AMENDMENT_001_20261113
exposure: PUBLIC
date: 2026-11-13
parent_preregister_commit: 7a22a264f7cb1589270e6c220a9a38256a76dda7
failed_first_actions_run: 43474117898
failed_first_job: 132053332916
kind: CODE_IMPLEMENTATION_INTEGRITY_REPAIR_ONLY

# ROT018 original source scheduler script correction, science protocol unchanged

First actual Actions run 43474117898 invoked the original frozen Task classes and generated the first one-unit source 18000-trial CSV. Before it could publish any source numerical summary, it aborted with AttributeError (list object has no attribute rng) in function source_rng_state(dots). The script local per-source-unit histogram variable named dots=[0]*10 had inadvertently SHADOWED the imported original DotsTasks module alias dots in the same function scope. This exception arose during digest/summary assembly after the first source unit Task-stream loop, NOT during original trial generator. It is not a scientific outcome/falsifier.

Fix ONLY local histogram variable identifier dots -> dots_bins in assignment, increment and result dict. DO NOT alter original source Task code, frozen RNG seed, prereg, native class methods, N_batch=18000, unit preferences or source trial sequence. Preserve failed run/action and archive. The repaired workflow will rerun same source stochastic seeds.

No scientific outcome was used to choose thresholds or alter design. The first run is an engineering failure, not proof of original source direction frequency statistics.

NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE.
