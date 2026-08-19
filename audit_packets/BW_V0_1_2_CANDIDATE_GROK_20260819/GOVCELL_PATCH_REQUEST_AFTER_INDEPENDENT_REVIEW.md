# IW / GOVCELL → IW_GROK_NEW_CELL_001_20260818
## Minimal patch request after independent review

Mission: `IW_GROK_BW_SKS_V0_1_2_CANDIDATE_MINIMAL_PATCH_001_20260819`

Status: `PATCH_REQUIRED_BEFORE_PROMOTION / NO_CANON / NO_EXEC_SIGN`

Keep the Level C causal-layer architecture. Do not redesign.

## Required fixes

### 1. Domain promotion — HIGH / terminal for promotion
`derive_domain_state()` currently promotes every causally non-invalid event and then selects the last one by `(recorded_at,event_id)`.

This violates:
`CAUSAL_HEAD != P_CURRENT != S_CURRENT`.

Patch requirement:
- P-plane domain promotion must obey explicit legal P-plane transition/authority/adoption semantics already represented by the facet/event contract; do not invent a global authority system.
- S-plane domain promotion must obey existing epistemic/evidence/warrant semantics; an arbitrary later ASSERTED event must not replace a prior qualified state merely because it is later.
- At minimum, the supplied rogue fixture must preserve the prior qualified domain value unless the later event is independently domain-qualified.

### 2. Event plane must match subject record plane
Before an event can affect domain state require:
`event.plane == record.plane`.

A mismatched event must be rejected/quarantined and must not mutate the record's domain facets.

Add a real adversarial P↔S fixture where `event.plane` disagrees with the target record plane.

### 3. Parent-set validation must be atomic and order-invariant
Do not return classification based on whichever invalid parent appears first.

Evaluate the full parent set, collect structural/missing errors, then classify deterministically with an explicit precedence independent of list ordering.

Add a test using the same parent set in reversed order.

### 4. Propagate incomplete ancestry
If a locally known parent is itself causally incomplete because one of its ancestors is missing, its descendants must not silently become fully complete heads.

Add a chain test:
`A -> missing`, `B.parents=[A]`, `C.parents=[B]`.
The stream remains incomplete until ancestry is complete.

### 5. Semantic guards on all public derived-state entry points
`build_views()` runs `validate_semantic_guards()`, but `derive_current_state()` / `compile_neighborhood()` currently allow bypass.

Ensure public paths that expose current/domain state cannot bypass load-bearing semantic guards.

### 6. Native v0.1.2 parents must be explicit
Legacy v0.1.1 ingestion may accept absent `parents` and normalize to `[]`.
Native v0.1.2 events must explicitly contain `parents`, including `parents: []` for a causal root.

Do not rewrite legacy events.

## Harness corrections

The current 46 assertions are real, but two load-bearing fixture intents are not executed:

- `FIX:ROGUE_CAUSAL_HEAD`: current harness explicitly accepts that the rogue becomes domain value and only checks metadata/history. Replace with an assertion that the prior qualified domain value remains current unless the rogue event satisfies domain qualification.
- `FIX:MISSING_PARENT`: assert the actual domain value remains `LOCAL`; causal metadata alone is insufficient.

Also add tests for:
- event-plane vs record-plane mismatch;
- reversed parent-set order invariance;
- transitive incomplete ancestry;
- semantic-guard API bypass;
- native v0.1.2 event missing explicit `parents`.

## Return

Return complete patched candidate files plus:

```yaml
GROK_V0_1_2_MINIMAL_PATCH_RETURN:
  files_changed: []
  original_46_result:
  strengthened_suite_result:
  rogue_domain_result:
  missing_parent_domain_result:
  event_plane_record_plane_result:
  parent_order_invariance_result:
  transitive_incomplete_result:
  semantic_guard_entrypoint_result:
  native_parents_result:
  new_counterexamples: []
  remaining_blockers: []
  recommendation: KEEP_CANDIDATE | PROMOTE_CANDIDATE_TO_NEXT_REVIEW | FAIL
```

Do not merge to main.
Do not change scientific claims.
Do not choose production backend.
Do not add vector clocks unless a new demonstrated blocker requires them.

`NO_CANON / NO_EXEC_SIGN`.
