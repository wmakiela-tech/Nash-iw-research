from __future__ import annotations

import copy
import re
from collections.abc import Mapping, Sequence

TEST_SEMANTIC_CLASSES = {
    "HARD_INVARIANT",
    "CURRENT_POLICY",
    "HISTORICAL_BUG_FIXTURE",
    "SCIENTIFIC_FIXTURE",
    "EXPERIMENTAL_CONTRACT",
}

EXECUTION_REQUIRED_FIELDS = (
    "execution_id",
    "requesting_cell",
    "scientific_request_ref",
    "code_commit_sha",
    "entry_point",
    "environment_spec",
    "input_refs_and_hashes",
    "command",
    "expected_outputs",
    "actual_output_refs_and_hashes",
    "regression_command",
    "regression_result",
    "runtime_warnings",
    "claim_ceiling",
    "return_to",
    "status",
)

ACCESSION_REQUIRED_FIELDS = (
    "executor_identity",
    "exposure_state",
    "authority_ceiling",
    "mutation_boundary",
    "bounded_task_and_failure_outcomes",
)

_SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")
_COMMIT_RE = re.compile(r"^[0-9a-fA-F]{7,40}$")


class SystemContractError(ValueError):
    """Raised when a system-contract invariant is violated."""


def _is_nonempty(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (Sequence, Mapping)):
        return len(value) > 0
    return True


def _validate_hash_entries(value: object, field_name: str) -> list[str]:
    errors: list[str] = []
    if not isinstance(value, list):
        return [f"{field_name} must be a list"]
    for i, item in enumerate(value):
        if not isinstance(item, Mapping):
            errors.append(f"{field_name}[{i}] must be an object")
            continue
        if not _is_nonempty(item.get("ref")):
            errors.append(f"{field_name}[{i}].ref is required")
        sha256 = item.get("sha256")
        if not isinstance(sha256, str) or not _SHA256_RE.fullmatch(sha256):
            errors.append(f"{field_name}[{i}].sha256 must be 64 hex characters")
    return errors


def validate_execution_contract(contract: Mapping[str, object]) -> list[str]:
    """Validate the thin execution/reproducibility contract only.

    A PASS here means the execution return is structurally reproducible enough
    to inspect. It does not establish scientific validity, currentness, CANON,
    EXEC_SIGN, novelty, or adoption.
    """
    errors: list[str] = []
    for field in EXECUTION_REQUIRED_FIELDS:
        if field not in contract:
            errors.append(f"missing required field: {field}")
            continue
        if field not in {"runtime_warnings", "actual_output_refs_and_hashes"} and not _is_nonempty(contract[field]):
            errors.append(f"required field is empty: {field}")

    commit = contract.get("code_commit_sha")
    if isinstance(commit, str) and not _COMMIT_RE.fullmatch(commit):
        errors.append("code_commit_sha must be a 7-40 character hexadecimal git SHA")

    for field in ("input_refs_and_hashes", "actual_output_refs_and_hashes"):
        if field in contract:
            errors.extend(_validate_hash_entries(contract[field], field))

    return errors


def validate_accession_contract(contract: Mapping[str, object]) -> list[str]:
    """Validate the bounded Stage-A accession envelope.

    This is an EXPERIMENTAL_CONTRACT for comparable model/executor evaluation.
    Passing it grants only legal test entry under the declared ceiling. It does
    not adopt a model, transfer cell identity, establish scientific authority,
    or create project-wide status.
    """
    errors: list[str] = []
    for field in ACCESSION_REQUIRED_FIELDS:
        if field not in contract:
            errors.append(f"missing required accession field: {field}")
        elif not _is_nonempty(contract[field]):
            errors.append(f"required accession field is empty: {field}")

    identity = contract.get("executor_identity")
    if isinstance(identity, Mapping):
        for field in ("model_or_executor", "provider_or_runtime", "tool_surface", "persistent_memory_status"):
            if not _is_nonempty(identity.get(field)):
                errors.append(f"executor_identity.{field} is required")
    elif identity is not None:
        errors.append("executor_identity must be an object")

    exposure = contract.get("exposure_state")
    if isinstance(exposure, Mapping):
        if not _is_nonempty(exposure.get("state")):
            errors.append("exposure_state.state is required")
        if not isinstance(exposure.get("independence_claim_allowed"), bool):
            errors.append("exposure_state.independence_claim_allowed must be boolean")
    elif exposure is not None:
        errors.append("exposure_state must be an object")

    ceiling = contract.get("authority_ceiling")
    if isinstance(ceiling, Mapping):
        required_true = (
            "no_canon",
            "no_exec_sign",
            "no_automatic_cell_identity_inheritance",
            "no_automatic_project_adoption",
        )
        for field in required_true:
            if ceiling.get(field) is not True:
                errors.append(f"authority_ceiling.{field} must be true")
    elif ceiling is not None:
        errors.append("authority_ceiling must be an object")

    mutation = contract.get("mutation_boundary")
    if isinstance(mutation, Mapping):
        writes_allowed = mutation.get("writes_allowed")
        if not isinstance(writes_allowed, bool):
            errors.append("mutation_boundary.writes_allowed must be boolean")
        if writes_allowed:
            if not _is_nonempty(mutation.get("allowed_surfaces")):
                errors.append("mutation_boundary.allowed_surfaces is required when writes are allowed")
            if mutation.get("no_automatic_merge_or_adoption") is not True:
                errors.append("mutation_boundary.no_automatic_merge_or_adoption must be true when writes are allowed")
    elif mutation is not None:
        errors.append("mutation_boundary must be an object")

    task = contract.get("bounded_task_and_failure_outcomes")
    if isinstance(task, Mapping):
        if not _is_nonempty(task.get("task_ref_or_description")):
            errors.append("bounded_task_and_failure_outcomes.task_ref_or_description is required")
        if not _is_nonempty(task.get("legal_failure_outcomes")):
            errors.append("bounded_task_and_failure_outcomes.legal_failure_outcomes is required")
    elif task is not None:
        errors.append("bounded_task_and_failure_outcomes must be an object")

    return errors


def validate_regression_metadata(metadata: Mapping[str, object]) -> list[str]:
    """Prevent regression tests from silently becoming shadow governance."""
    errors: list[str] = []
    semantic_class = metadata.get("test_semantic_class")
    if semantic_class not in TEST_SEMANTIC_CLASSES:
        errors.append("test_semantic_class must be one of the declared semantic classes")

    if not _is_nonempty(metadata.get("human_readable_semantic")):
        errors.append("human_readable_semantic is required")
    if not _is_nonempty(metadata.get("what_pass_does_not_mean")):
        errors.append("what_pass_does_not_mean is required")

    if semantic_class != "HARD_INVARIANT" and not _is_nonempty(metadata.get("review_or_sunset_trigger")):
        errors.append("review_or_sunset_trigger is required for non-HARD_INVARIANT tests")
    return errors


def explicit_current(records: Sequence[Mapping[str, object]]) -> Mapping[str, object]:
    """Resolve CURRENT from an explicit marker, never from newest timestamp."""
    current = [record for record in records if record.get("current") is True]
    if len(current) != 1:
        raise SystemContractError(f"expected exactly one explicit current record, found {len(current)}")
    return current[0]


def assert_signal_only(
    before: Mapping[str, object],
    after: Mapping[str, object],
    *,
    protected_fields: Sequence[str] = ("scientific_status", "authority_state", "priority_state"),
) -> None:
    """Fail if a derived monitor/signal silently mutates protected state."""
    changed = [field for field in protected_fields if before.get(field) != after.get(field)]
    if changed:
        raise SystemContractError(
            "signal-only update mutated protected field(s): " + ", ".join(changed)
        )


def assert_witness_actor_preserved(
    before: Mapping[str, object],
    after: Mapping[str, object],
) -> None:
    """A transferred witness may travel; the upstream inspection actor may not be rewritten."""
    if before.get("witness_actor") != after.get("witness_actor"):
        raise SystemContractError("witness_actor changed during transfer")


def transferred_witness(
    witness: Mapping[str, object],
    *,
    recipient: str,
) -> dict[str, object]:
    """Create a recipient-side handoff view without self-attributing source inspection."""
    result = copy.deepcopy(dict(witness))
    result["knowledge_origin_current_participant"] = "LINEAGE_OR_PARTICIPANT_HANDOFF"
    result["current_participant"] = recipient
    result["current_participant_direct_source_inspection"] = False
    assert_witness_actor_preserved(witness, result)
    return result
