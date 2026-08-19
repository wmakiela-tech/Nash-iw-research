# IW / Moderator → IW_DS_NEW_CELL_001_20260818
## BOUNDED FALSIFICATION MISSION

Mission ID: `IW_DS_BW_MULTIWRITER_CAUSALITY_FALSIFICATION_001_20260819`

Status: `BOUNDED / DISCLOSED_EXPOSURE / NO_CANON / NO_EXEC_SIGN`

## Target

Falsify or sharply qualify the AInstein candidate in:

`AINSTEIN_CAUSAL_DAG_MVR_CANDIDATE.md`

The motivating observed defect is already established by independent runtime audit: BW/SKS v0.1.1 uses numeric per-facet sequence semantics that is deterministic under replay but not multi-writer safe; independent writers can be hard-rejected on equal sequence or silently resolved by higher numeric sequence.

Do **not** reassess K12, N(rho), Košir, novelty, or scientific truth. This is a logical/semantic audit of the event/current-state model.

## Required attacks

### 1. Causality vs authority

Attack the implication:

`sole causal head => legally current project/scientific state`.

Ask whether an arbitrary cell can emit a child referencing all active heads and thereby become the sole head even when it lacks authority to resolve a P-plane authority/adoption state or lacks evidence/warrant to qualify an S-plane claim.

Determine what must remain separate between:

- causal supersession;
- project authorization/adoption;
- scientific qualification/currentness.

### 2. Parent validity

Try to break the model with:

- parent from another `subject_id`;
- parent from another `facet`;
- parent from another plane;
- self-parent;
- cycle;
- duplicate parent;
- nonexistent parent;
- malicious event claiming unrelated heads as parents.

State the minimum validity conditions required before an edge may affect head calculation.

### 3. Missing-parent / partial-view semantics

The AInstein return contains a tension between `PENDING_PARENT` for out-of-order delivery and rejecting unknown parents.

Determine the safe semantics for a federated asynchronous system. Test whether an incomplete local event set can incorrectly produce a single head or false closure.

Propose explicit states such as `INCOMPLETE_CAUSAL_VIEW` only if logically necessary.

### 4. Event identity

Current v0.1.1 already has `event_id`. Attack the proposal's suggestion that event identity may be either UUID or content hash.

Test whether a hash over only issuer/sequence/payload/parents is sufficient when subject/facet/event_type/provenance differ. Distinguish event identity from content identity if needed.

### 5. Local sequence scope

If legacy `sequence` is retained only for issuer-local integrity, determine its exact scope:

- per issuer globally;
- per issuer + subject;
- per issuer + subject + facet.

Test whether gaps/reuse across unrelated facets create false errors.

### 6. Legacy migration

Current v0.1.1 events already have event IDs but no causal parent field.

Attack any migration that invents cross-issuer causality from numeric sequence.

Determine when same-issuer sequence can safely imply a parent chain and when the correct result is `LEGACY_CAUSALITY_UNKNOWN` / concurrent roots.

### 7. Convergent duplicates

Attack `CONVERGENT_DUPLICATE`:

- identical payload but different evidence/provenance;
- identical payload but different event type;
- identical payload with one event invalid or unauthorized.

Determine whether payload equality is enough for a clean read rendering while still preserving epistemic/provenance differences.

### 8. Reconciliation completeness

Test partial reconciliation, stale reconciliation, and new concurrent writes after reconciliation.

A resolving event that references only a subset of heads must not erase the unreferenced heads.

### 9. Cross-plane guards

Confirm that adding causal metadata does not create an implicit bridge from P to S or S to P. A causal head in one plane must not enact state in the other.

## Required output

Return:

```yaml
DS_MULTIWRITER_FALSIFICATION_RETURN:
  overall_verdict: PASS | PASS_WITH_PATCHES | FAIL
  fatal_counterexamples: []
  material_qualifications: []
  minimum_validity_rules: []
  authority_vs_causality_rule: []
  missing_parent_semantics: []
  legacy_migration_rule: []
  event_identity_rule: []
  adversarial_tests_required: []
  smallest_safe_candidate_revision: []
  things_not_to_fix: []
  confidence_and_limits: []
  bw_delta: <material delta or NO_MATERIAL_BW_DELTA>
```

Core guard:

`WEAK_NEGATIVE != BROAD_HYPOTHESIS_KILL`

Do not reject the whole causal-DAG idea because one field or migration rule is defective if a smaller patch preserves the useful core.

## BW delta plane/type note

If the review produces material reusable knowledge, return a BW delta. For v0.1.1:

- `SPINE`: `SOURCE`, `SOURCE_ANCHOR`, `EVIDENCE`;
- `P`: `PROJECT_OBJECT`, `PROJECT_OBLIGATION`;
- `S`: scientific record kinds including `NEGATIVE_KNOWLEDGE`, `WARRANT_BOUNDARY`, `UNKNOWN`, `TENSION`, etc.;
- `CROSS`: `BRIDGE`.

A limitation of the BW reducer/architecture is a **P-plane instrument/project finding**, not S-plane scientific `NEGATIVE_KNOWLEDGE`. Represent it as `PROJECT_OBJECT` (e.g. subtype `INSTRUMENT_DEFECT` / `DESIGN_QUALIFICATION`) plus `PROJECT_OBLIGATION` where remediation remains open. Preserve source/audit location through SPINE anchors.

No implementation yet.

`NO_CANON / NO_EXEC_SIGN`.
