# NASH/IW — Naming and Indexing Contract

**As of:** 2026-09-14  
**Classification:** public-safe operator guidance; no scientific authority.

This is the current forward-only naming boundary used by [`WORK_AND_REPRODUCIBILITY_PROTOCOL.md`](WORK_AND_REPRODUCIBILITY_PROTOCOL.md). It supersedes the older preferred token order in private System Core section 6 for new material artifacts only. Historical artifacts are not renamed, and System Core protected boundaries remain unchanged.

## Canonical identifier

Use a stable, human-searchable identifier:

```text
IW_<CELL-OR-LINEAGE>_<OBJECT>_<DOCUMENT-TYPE>_<NNN>_<YYYYMMDD>
```

Example:

```text
IW_SYSS3_GITHUB_MULTISURFACE_ARCHITECTURE_IMPLEMENTATION_RETURN_001_20260912
```

The filename is the identifier plus a lowercase extension. Keep the identifier unchanged across transports and revisions that repair the same object. Use a new sequence number only for a new logical artifact, not for a copy, upload, or delivery retry.

## Vocabulary

- `CELL-OR-LINEAGE`: active role/cell short name; historical parent remains in provenance.
- `OBJECT`: compact subject, using `_` between words.
- `DOCUMENT-TYPE`: one controlled type such as `PROTOCOL`, `TASK`, `PACKET`, `RETURN`, `REVIEW`, `CHECKPOINT`, `FREEZE`, `DECISION`, `REPORT`, `MANIFEST`, `REPRO_MANIFEST`, `LITERATURE_RECORD`, `DATA`, `RUNTIME`, `SCHEMA`, `INDEX`, `POINTER`, or `SUCCESSION`.
- `NNN`: zero-padded sequence within the named object/type family.
- `YYYYMMDD`: creation date of the logical artifact, not a later upload date.

Avoid ambiguous suffixes such as `final`, `latest`, `new`, `fixed`, or bare `v2`. If an immutable release version is needed, record it in metadata and use a typed successor relation. Do not add ordering prefixes such as `01-` to canonical stored filenames; UI/import order is not identity.

## Required searchable metadata

Every material indexed artifact should expose, in content or registry metadata:

```yaml
artifact_id: IW_...
title: human-readable title
created_at: YYYY-MM-DD
as_of: YYYY-MM-DD or source revision
origin_cell: public-safe role/cell
document_type: controlled type
exposure: PUBLIC | PRIVATE | RESTRICTED
status: DRAFT | CURRENT | FROZEN | SUPERSEDED | RETRACTED | HOLD
provenance: source identity or retrieval instruction
supersedes: []  # old artifact IDs; direction is old -> this artifact
```

## Revisions, copies and lineage

- Typographical or formatting repair of the same artifact: retain `artifact_id`; record revision/commit.
- Materially changed claim, scope, decision or task: create a new artifact ID and explicit lineage.
- Transport copy: retain the same ID and checksum where byte-identical; record route separately.
- Derived summary: new ID with `derived_from`; never masquerade as the source.
- Supersession: store `old_id -> new_id`; a later timestamp alone does not supersede anything.

## Repository placement

- `docs/`: current public operator and architecture documents.
- `archive-index/YYYY/<source-family>/`: public-safe historical entries when volume requires grouping.
- `manifests/`: custody/reproduction manifests.
- `schemas/`: machine-readable contracts.
- `runtime/`, `src/`, `tests/`, `fixtures/`: executable reproduction sets.

Search by stable ID first, then object/type, then date. Git history is the revision log; filenames are not changelogs.

```text
FILENAME != CURRENTNESS
COPY != NEW_ARTIFACT
NEWER_TIMESTAMP != SUPERSESSION
```
