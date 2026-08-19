# IW / NASH — AInstein BW multi-writer causality candidate
### 2026-08-19

Status: `CANDIDATE_DESIGN / NOT_IMPLEMENTED / NEEDS_INDEPENDENT_FALSIFICATION / NO_CANON / NO_EXEC_SIGN`

Source: return from `IW_AINSTEIN_NEW_CELL_001_20260818` for mission `IW_AINSTEIN_BW_MULTIWRITER_CAUSALITY_DESIGN_001_20260819`.

## Core assessment

BW/SKS v0.1.1 cannot safely infer current state for multi-writer facets without causal metadata. Integer sequence numbers cannot establish causal precedence across independent writers without degenerating into numeric LWW or hard-fail collisions.

## A. Minimal semantic model proposed

A **causal DAG multi-value register (MVR)** with explicit predecessor edges.

Each event explicitly references event IDs it observed and intends to supersede/reconcile through `parents`.

For a fixed `(subject_id, facet)` the current causal state is the set of causal heads: events not referenced as parents by another accepted event for the same facet.

- one head → `SINGLE_HEAD`;
- multiple heads with identical payloads → `CONVERGENT_DUPLICATE`, preserving all head IDs;
- multiple heads with differing payloads → `CONCURRENT_BRANCHES`, preserving all values and provenance.

Conflict reconciliation occurs through a new event whose `parents` contains all heads being reconciled.

## B. Event schema proposal

AInstein proposed:

- `event_id: string` — unique event identity, UUID or deterministic hash;
- `parents: list[string]` — explicit causal predecessor event IDs, empty for roots;
- retain a cell-local sequence number only for local log integrity, never for cross-cell precedence.

## C. Proposed deterministic reducer

```python
def reduce_facet(events):
    event_by_id = {e["event_id"]: e for e in events}
    all_parents = {p for e in events for p in e.get("parents", [])}
    heads = [e for e in events if e["event_id"] not in all_parents]
    heads.sort(key=lambda e: e["event_id"])

    if not heads:
        return {"status": "EMPTY", "value": None}
    if len(heads) == 1:
        return {
            "status": "SINGLE_HEAD",
            "active_heads": [heads[0]["event_id"]],
            "value": heads[0]["payload"],
        }

    first = heads[0]["payload"]
    if all(h["payload"] == first for h in heads):
        return {
            "status": "CONVERGENT_DUPLICATE",
            "active_heads": [h["event_id"] for h in heads],
            "value": first,
        }

    return {
        "status": "CONCURRENT_BRANCHES",
        "active_heads": [h["event_id"] for h in heads],
        "conflicting_values": [
            {"head_id": h["event_id"], "issuer": h.get("issuer_cell_id") or h.get("issuer"), "payload": h["payload"]}
            for h in heads
        ],
    }
```

The intended invariant is replay-order independence: current state depends on graph topology, not arrival order.

## D. Conflict resolution

No automatic winner by timestamp, sequence number, cell identity, rank, hash order, or arrival order.

A resolving event must explicitly reference the conflicting heads it is reconciling.

Example:

```json
{
  "event_id": "evt_recon_999",
  "issuer_cell_id": "IW_AINSTEIN_NEW_CELL_001_20260818",
  "parents": ["evt_a_100", "evt_b_101"],
  "subject_id": "SUBJ_01",
  "facet": "project_lifecycle",
  "payload": {"value": "RESOLVED_VALUE"}
}
```

## E. Backward compatibility proposal

For v0.1.1 legacy events lacking causal parents:

- preserve/generate stable event IDs;
- infer a linear parent chain only within a single issuer and same `(subject_id, facet)` when legacy ordering is unambiguous;
- if multiple issuers wrote the same facet without recoverable causal metadata, treat issuer chains as concurrent rather than imposing numeric cross-issuer order;
- historical ambiguity should surface rather than be silently resolved.

## F. Adversarial test matrix proposed

1. shuffled replay → identical head set/state;
2. different independent issuer sequence numbers → `CONCURRENT_BRANCHES`, not LWW;
3. equal independent issuer sequence numbers → `CONCURRENT_BRANCHES`, not collision hard-fail;
4. partial reconciliation of only some heads leaves unresolved heads active;
5. identical concurrent payloads → `CONVERGENT_DUPLICATE`, preserving provenance.

## G. Failure modes acknowledged by AInstein

- missing parent / out-of-order transport;
- unresolved branch accumulation;
- malformed/random parent references.

Suggested handling included pending-parent state and ingestion validation, though the original return contained a tension between allowing `PENDING_PARENT` and rejecting unknown parents outright. This remains for independent review.

## H. Smallest recommended direction

Add explicit causal predecessor metadata and compute active heads from causal topology; do not introduce a global sequencer, production backend, database choice, or a large CRDT framework.

## Important review boundary

This file records the AInstein candidate, not an accepted design. In particular, independent review must test whether causal precedence alone is sufficient to determine **authorized project current state** or **qualified scientific current state**, and whether a causal join can ever imply authority/epistemic resolution without separate domain guards.
