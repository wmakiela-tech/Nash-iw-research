# IW Material Work Return Template

Controlling protocol: `IW_OW_CELL_WORK_ARTIFACT_AND_REPRODUCIBILITY_PROTOCOL_001_20260914`

Delete guidance text before use. Keep the field names so returns remain searchable across surfaces.

## PUBLIC research body metadata (use before publishing under research/)

For **full, approved public-safe scientific body** copy the block below to the top of the file, before any long narrative (the CI guard examines only the first 3500 characters). Replace every placeholder with truthful values; the name and value must start at the beginning of the line:

```yaml
artifact_id: IW_REAL_ARTIFACT_ID
exposure: PUBLIC
claim_ceiling: SOURCE_ONLY_NO_CANON_NO_EXEC
sync_state: GITHUB_PENDING_BW_INGEST
```

If and only if a genuine BW ingestion event exists, use `bw_ingestion_event_id: ING-YYYYMMDD-NNNN` with the **actual** event ID instead of the pending sync state. The guard recognizes `scientific_claim_ceiling`, `claim_ceiling`, `result_class` or `status` as the claim/status-bearing field; still state the substantive ceiling honestly in the body. `RETURN_ID`, `CLASS`, `CEILING`, `BW_PENDING`, `bw_event_or_pending` and `exposure: PUBLIC_SAFE` do **not** substitute for the required metadata names/values.

Do not copy this public-only block into private, unapproved or protected documents. The generic template's `exposure: PUBLIC | PRIVATE | RESTRICTED` is a choice instruction, **not** a valid final public metadata value. Use a genuinely public-safe full body; no pointer-only scientific replacement.

Before publication or after fixing any existing body, run `python scripts/preflight_public_science_writeback.py research/<lineage>/<YYYY-MM-DD>/<file>.md`. Since 2026-10-26, CI also runs the same metadata validator over added **and modified** research texts (`--diff-filter=AM`) and regression tests. The original added-only (`--diff-filter=A`) guard remains unchanged. Older green CI runs cannot verify retroactive fixes; see `CONTRIBUTING.md`.



```yaml
from_cell: IW_...
to_cell_or_route: IWTO_...
function: assigned function used in this rotation
task_id: stable ID across every transport
return_id: stable return ID
in_reply_to: message/issue/artifact ID or NOT_APPLICABLE
artifact_id: IW_<CELL-OR-LINEAGE>_<OBJECT>_<DOCUMENT-TYPE>_<NNN>_<YYYYMMDD>
title: human-readable title
document_type: RETURN
created_at: 2026-09-14T00:00:00Z
currentness_basis: exact BW/LT/system/task basis or NOT_APPLICABLE
stale_if: exact invalidation condition
exposure: PUBLIC | PRIVATE | RESTRICTED
result_class: RESULT | NEGATIVE_KNOWLEDGE | BLOCKER | ANTI_REDISCOVERY_CORRECTION | CURRENTNESS_CORRECTION | PENDING_REVIEW | NO_MATERIAL_DELTA
status: COMPLETE | PARTIAL | BLOCKED | HOLD | FAILED_NO_STATE_CHANGE
function_scan:
  inbound_handled: summary or NONE
  function_derived_action: exact bounded action or NO_MATERIAL_FUNCTIONAL_ACTION
  no_action_reason: NOT_APPLICABLE or legal reason
material_delta: concise exact change
claim_ceiling_or_scope: what this result does and does not establish
primary_location: durable pointer or CUSTODY_PENDING
content_sha256: 64 lowercase hex characters or NOT_AVAILABLE_WITH_REASON
persistence_state: LOCAL_ONLY | WRITE_ATTEMPTED | STORED | READBACK_VERIFIED | CUSTODY_PENDING
readback_state: VERIFIED | FAILED | NOT_POSSIBLE_WITH_REASON | NOT_APPLICABLE
delivery_state: NOT_ROUTED | DELIVERY_BLOCKED | DELIVERED | RECEIVED | ACCEPTED
github_check: CHECKED_NO_RELEVANT_DELTA | USED_AS_PUBLIC_SAFE_PRIMARY | USED_AS_PUBLIC_SAFE_FALLBACK | NOT_APPLICABLE_PRIVATE_OR_PROTECTED | ACCESS_BLOCKED
provenance: exact source/input/parent pointers
derived_from: []
supersedes: []
dependencies_or_blockers: []
acceptance_owner: cell or role
next_single_step: exact bounded step or NONE
return_path: exact recipient/thread/issue
guards: [NO_CANON, NO_EXEC_SIGN, SCIENCE_FIRST]
```

## Material body

### Question or objective

State the exact bounded problem.

### Method or action

State what was actually done, including skipped or failed steps that affect interpretation.

### Result and evidence

Separate observation, derivation, interpretation, and claim ceiling.

### Reproduction or audit path

Link the applicable reproduction manifest or literature-search record. If neither applies, provide the minimal verification procedure.

### Failures, uncertainty, and negative knowledge

Preserve material failure and explicit UNKNOWN. Do not convert a missing write, read, search hit, or validator into a scientific verdict.

### Next dependency

Name the exact owner/action/return path, or `NONE`.

