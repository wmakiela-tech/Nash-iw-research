# IW / NASH — external-cell BW delta schema patch
### 2026-08-19

Status: `REAL_USE_INTERFACE_PATCH / NO_CANON / NO_EXEC_SIGN`.

Reason: the first material Grok BW delta correctly identified instrument defects but placed `NEGATIVE_KNOWLEDGE` records on P-plane. The simplified external-cell interface had not exposed the v0.1.1 core record-kind/plane allow-list. Preserve raw cell contributions; qualify/normalize separately rather than rewriting them.

## Core v0.1.1 record-kind / plane map

```yaml
SPINE:
  - SOURCE
  - SOURCE_ANCHOR
  - EVIDENCE

P:
  - PROJECT_OBJECT
  - PROJECT_OBLIGATION

S:
  - SCIENTIFIC_OBJECT
  - CLAIM
  - SCOPE
  - MECHANISM
  - RELATION
  - NEGATIVE_KNOWLEDGE
  - WARRANT_BOUNDARY
  - UNKNOWN
  - TENSION
  - PUZZLE
  - DISCRIMINATOR
  - FRONTIER
  - FIELD_MAP
  - ATTEMPT

CROSS:
  - BRIDGE
```

## External-cell rule

- A defect/limitation of the **BW instrument or project workflow** belongs in P-plane as a `PROJECT_OBJECT` (recommended subtype `INSTRUMENT_DEFECT` or `TEST_WEAKNESS`) plus a `PROJECT_OBLIGATION` when remediation is open.
- `NEGATIVE_KNOWLEDGE` in v0.1.1 is reserved for S-plane scientific knowledge; do not use it for a software/instrument defect merely because the finding is negative.
- Audit reports/sources and exact finding locators belong on SPINE as `SOURCE` / `SOURCE_ANCHOR`.
- Do not rewrite a contributor's raw delta to force compliance. Preserve it, then issue a separate qualification/normalization delta.

## Concurrency guard after Grok audit

Until MF1 is resolved:

`NO_AUTOMATIC_MULTIWRITER_CURRENT_STATE_RESOLUTION`

Independent cell-local numeric sequence values have no cross-cell authority. If independent cells produce competing writes to the same `(subject_id, facet)`, preserve the ambiguity/conflict rather than selecting the numerically larger sequence.

The candidate causal-DAG/MVR design is not implemented and remains under independent falsification.
