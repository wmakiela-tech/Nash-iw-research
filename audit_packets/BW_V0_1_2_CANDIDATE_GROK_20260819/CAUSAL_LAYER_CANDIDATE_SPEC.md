# BW/SKS v0.1.2 causal-layer candidate — implementation specification

Status: `CANDIDATE / NOT_LIVE_CONTRACT / NO_CANON / NO_EXEC_SIGN`.

Origin: Grok MF1 concurrency audit → AInstein causal DAG/MVR design → DS falsification → AInstein revised two-level design → GOVCELL disposition.

## Core invariant

`CAUSAL_HEAD != P_CURRENT != S_CURRENT`

Level C is causal topology only. Level D remains domain-specific P/S state semantics.

## Minimal schema delta

Add to events:

```json
"parents": []
```

`parents` contains explicit causal predecessor `event_id`s within one exact causal stream.

Existing `event_id` remains an opaque occurrence identifier. Do not replace it with payload/content hashing.

Existing `sequence` remains local integrity/order metadata only. Exact scope:

`(issuer_cell_id, plane, subject_id, facet)`.

Cross-issuer numeric sequence has **zero** causal or current-state authority. Gaps do not imply missing events.

## Valid parent edge

A parent edge may affect head calculation only after the complete child parent set passes validation.

Required:
- same `subject_id`;
- same `facet`;
- same `plane`;
- no self-parent;
- no duplicate parent IDs;
- no cycle;
- known parent or explicitly unresolved/missing-parent handling.

**Atomic validation rule:** if one edge of a child is invalid, none of that child's parent declarations may suppress a valid head.

Cross-plane semantics require typed bridge objects, not `parents`.

## Level C outputs

Minimum states:
- `SINGLE_CAUSAL_HEAD`
- `CONCURRENT_BRANCHES`
- `INCOMPLETE_CAUSAL_VIEW`
- `INVALID_CAUSAL_GRAPH`
- `EMPTY_GRAPH`

Payload equality never collapses head identity. Identical concurrent payloads may be rendered compactly by a view, but distinct head IDs/provenance remain preserved.

## Missing parent semantics

A valid-looking event with one or more locally missing parents is retained as pending/incomplete. The stream reports `INCOMPLETE_CAUSAL_VIEW` and provisional locally known heads.

No timeout converts transport absence into causal knowledge.

An incomplete/pending event must not erase a previously qualified P/S domain state. Domain views may expose the last qualified domain state together with a causal-completeness warning.

## Level D boundary

Level D must not consume *only* `active_heads` as if heads were legal current state. It needs event history/ancestry plus Level-C topology so that an unauthorized/unwarranted causal child cannot erase the last legally qualified domain state.

P-plane applies its existing authorization/adoption/obligation rules.

S-plane applies its existing evidence/warrant/scope/claim-boundary rules.

A sole causal head can therefore be rejected by P or S domain semantics without deleting qualified historical state.

## Legacy migration

Legacy v0.1.1 source artifacts are not rewritten. Missing `parents` is normalized in memory as no explicit causal edges.

Do not infer cross-issuer causality from numeric sequence.

Do not infer same-issuer causality merely from consecutive sequence unless an explicit historical stream contract proves linear successor semantics.

Where causality cannot be established, surface legacy ambiguity rather than inventing history.

This is structural ingestion compatibility, **not a guarantee of identical derived current state** relative to v0.1.1 numeric-LWW behavior.

## Reconciliation

If heads are `[A,B,C]` and event `R.parents=[A,B]`, then heads become `[R,C]` after valid ingestion.

No implicit `resolves_all` semantics.

New concurrent events after reconciliation remain active heads unless explicitly causally succeeded later.

## Non-goals

Do not choose a database/backend. Do not add vector clocks unless explicit predecessors prove insufficient. Do not add generic truth scores or generic authority booleans. Do not alter scientific claims. Do not collapse P/S semantics.
