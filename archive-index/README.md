# Archive Index

This directory is the public-safe archive catalogue. An entry uses exactly one mode: `PUBLIC_ARTIFACT`, `POINTER_ONLY`, `HASH_ONLY`, or `EXECUTABLE_REPRODUCTION`.

Record the stable artifact ID, canonical filename, mode, artifact type, date, originating cell/owner, epistemic and lifecycle status, public-safe source/retrieval instruction, SHA-256 when available, and explicit lineage. Write supersession as `old_id -> new_id`; never rely on an untyped `superseded_by` field whose direction is unclear.

Do not publish credentials, private payloads, unpublished conclusions, or provider-specific private storage coordinates. A `POINTER_ONLY` entry may name a private source family or authorized resolver without exposing its URL/ID. A `HASH_ONLY` entry witnesses identity/integrity, not delivery or availability.

Use [`archive-entry.schema.json`](archive-entry.schema.json) for machine-readable entries. Group entries by year and source family when volume warrants it; do not create empty directory hierarchies in advance. Follow [`../docs/NAMING_AND_INDEXING.md`](../docs/NAMING_AND_INDEXING.md).

```text
ARCHIVED != CURRENT
HASH_RECORDED != ARTIFACT_DELIVERED
POINTER_EXISTS != ACCESS_CONFIRMED
```
