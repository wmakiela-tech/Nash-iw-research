# IW / Moderator → IW_GROK_NEW_CELL_001_20260818
## BW/SKS v0.1.2-candidate implementation + adversarial runtime mission

Mission ID: `IW_GROK_BW_SKS_V0_1_2_CANDIDATE_IMPLEMENT_AND_ATTACK_001_20260819`

Status: `BOUNDED / IMPLEMENTATION_CANDIDATE / NO_CANON / NO_EXEC_SIGN`.

## Objective

Implement the smallest backend-neutral v0.1.2 candidate that fixes MF1 multi-writer semantics while preserving v0.1.1 history and P/S separation.

Read `CAUSAL_LAYER_CANDIDATE_SPEC.md` first.

Base files inherited on this branch from the v0.1.1 audit packet:
- `audit_packets/BW_GROK_V0_1_1_20260819/sks_reference_contract_v0_1_1.json`
- `audit_packets/BW_GROK_V0_1_1_20260819/sks_seed_slices_v0_1_1.json`
- `audit_packets/BW_GROK_V0_1_1_20260819/sks_conformance_fixtures_v0_1_1.json`
- `audit_packets/BW_GROK_V0_1_1_20260819/sks_reducer_v0_1_1.py`
- `audit_packets/BW_GROK_V0_1_1_20260819/test_sks_conformance_v0_1_1.py`

Do not modify the v0.1.1 files. Create new candidate files.

## Required implementation outputs

Create locally and return full contents or patch for:
- `sks_reference_contract_v0_1_2_candidate.json`
- `sks_reducer_v0_1_2_candidate.py`
- `sks_conformance_fixtures_v0_1_2_candidate.json`
- `test_sks_conformance_v0_1_2_candidate.py`

Optional migration helper only if necessary:
- `sks_legacy_v0_1_1_adapter_v0_1_2_candidate.py`

## Required semantic behavior

### 1. Level C causal reduction

Group exact causal streams by:

`(plane, subject_id, facet)`.

Use explicit `parents` only for causal precedence. Numeric `sequence` across issuers must never select a winner.

Parent suppression must be atomic: validate all parent edges of a child before adding any of them to the suppressed-parent set.

### 2. Structural attacks

Test and reject/quarantine correctly:
- cross-subject parent;
- cross-facet parent;
- cross-plane parent;
- self-parent;
- duplicate parent;
- cycle;
- child with `[VALID_PARENT, INVALID_PARENT]` where the valid parent MUST remain a head if the child is invalid.

### 3. Multi-writer tests

Required:
- same sequence, different issuers → no hard fail merely because sequence equal;
- different sequence, different issuers → no numeric LWW;
- two writers from same observed parent → `CONCURRENT_BRANCHES`;
- partial reconciliation `[A,B,C]` with R.parents=`[A,B]` → heads `[R,C]`;
- shuffled replay → identical causal state.

### 4. Causality vs P/S current state

Add an adversarial `rogue child` fixture:
- authoritative/warranted prior event H;
- rogue E with `parents=[H]`;
- E becomes sole causal head;
- E must NOT automatically become `P_CURRENT` or `S_CURRENT` merely due to topology.

The domain reducer must have enough history/topology to preserve or report the last legally qualified domain state rather than blindly consuming only the new active head.

Do not invent a universal authority or truth score.

### 5. Missing parents

A missing-parent event must produce `INCOMPLETE_CAUSAL_VIEW` or equivalent explicit incompleteness.

No timeout-based causal inference.

Return provisional locally known heads if useful, but do not label the causal view complete.

A missing-parent event must not itself erase a previously qualified P/S state.

### 6. Legacy v0.1.1

Do not rewrite source artifacts or existing event IDs.

No cross-issuer causality inferred from numeric sequence.

No same-issuer chain inferred unless an explicit legacy stream contract is supplied to the adapter.

Test that legacy ingestion is structurally possible while documenting that derived causal/current state may differ from old numeric-LWW output.

### 7. Preserve earlier Grok findings

Also patch and test, if independent and small enough in the same candidate:
- MF2 `max_nodes=0` safety preservation;
- MF3 formal-math PROOF requires a located source anchor/support qualification;
- safety companions through typed `APPLIES_BOUNDARY_TO` / `APPLIES_UNKNOWN_TO` relations;
- replace weak P/S absence checks with actual adversarial leakage fixtures.

If combining these with MF1 materially complicates the candidate, keep them as separate clearly marked patches in the same test suite rather than coupling semantics.

## Required return

```yaml
GROK_V0_1_2_CANDIDATE_RETURN:
  implementation_status: PASS | PASS_WITH_PATCHES | FAIL
  files_created: []
  v0_1_1_regression_result: []
  v0_1_2_candidate_test_result: []
  causal_states_implemented: []
  domain_boundary_result: []
  legacy_migration_result: []
  mf2_mf3_related_result: []
  new_counterexamples: []
  remaining_blockers: []
  recommendation: KEEP_CANDIDATE | REVISE | REJECT
  bw_delta: <material delta or NO_MATERIAL_BW_DELTA>
```

Harness PASS is not sufficient. Add your own runtime attacks after the candidate suite passes.

Do not merge to main. Do not create production backend. Do not update scientific S-plane claims.

`NO_CANON / NO_EXEC_SIGN`.
