artifact_id: IW_XH_S6_ROT019_ORIGINAL_AUTHOR_SHA_TYPO_PRE_MODEL_REPAIR_001_20261113
date: 2026-11-13
exposure: PUBLIC
original_preregister_commit: 301c2b93f8b1e901ba9ef257cb948401e99b89d5
original_workflow_commit: e18c052f4b56d0ceca6b7a08d4f28e50202c0d0e
failed_before_any_model_data_run: 43519442977

# ROT019 — engineering correction to original author commit reference, before model outputs

The original scientific host is solkm/formattingRNN at EXISTING Git commit EXACT SHA:
7889a81e298c01532a313e02971c11dbc9db8eb0
The ROT019 preregister document and workflow final shell test erroneously typed
7889a81e298c01532a313e02971c11dbc9eb8eb0
with one omitted character, making the hash different from the real commit. The workflow correctly CLONED and CHECKED OUT the real source SHA; its final HEAD equality test compared that correct checked-out source against the incorrect string and exited 1 with no diagnostic because Git quiet and Bash test false. Run 43519442977 stopped at original SOURCE retrieval verification, BEFORE any original source Task or trained-RNN trial was generated. Original prereg and source runner code SHA remain immutable and auditable. Source runner already had the CORRECT real source git SHA value. This single typo is not a source-author fault and does not reflect science.

Fix only the final workflow HEAD equality comparison to the real original author SHA, explicitly echo expected and actual HEAD, without any change to frozen hypothesis, source model code, units, strengths, random seeds, Task schedule, number of trials, stochastic intervention, safety flags or source firstness. All original code/NPZ blob checks are still fail-closed in the runner. Full git checkout commit exists and was independently verified via original public repository GitHub API BEFORE this amendment.

No scientific outcomes existed before the correction, and no experimental threshold is adjusted. The old prereg remains as a provenance artifact; this correction is effective as a linked annex. BW GITHUB_PENDING_BW_INGEST; NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_OWNER_TASK_CASCADE.
