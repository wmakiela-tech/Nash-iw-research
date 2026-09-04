# Experimental Stage-A accession contract

This is a small, model-independent envelope for bounded executor/model-family testing.

It is an `EXPERIMENTAL_CONTRACT`, not project governance or model adoption policy.

`ACCESSION != SCOPED_EXECUTOR_ADOPTION != CELL_SUCCESSION != SCIENTIFIC_AUTHORITY != PROJECT_ADOPTION`

A structurally valid accession record grants no CANON, EXEC_SIGN, cell identity, scientific truth, or project-wide adoption.

## Five required surfaces

1. `executor_identity`
   - model/executor identity;
   - provider/runtime;
   - tool surface;
   - persistent-memory status.
2. `exposure_state`
   - declared exposure state;
   - whether an independence claim is legal.
3. `authority_ceiling`
   - `no_canon=true`;
   - `no_exec_sign=true`;
   - `no_automatic_cell_identity_inheritance=true`;
   - `no_automatic_project_adoption=true`.
4. `mutation_boundary`
   - whether writes are allowed;
   - if allowed, exact surfaces plus `no_automatic_merge_or_adoption=true`.
5. `bounded_task_and_failure_outcomes`
   - bounded task reference/description;
   - explicit legal failure/non-adoption outcomes.

The validator intentionally does not rank models or impose a global score. It exists only to make real-use comparisons comparable and reversible.

Review/sunset trigger: revise or remove this contract if real accession runs show that a field is non-discriminating, burdensome, or hides a material failure mode.
