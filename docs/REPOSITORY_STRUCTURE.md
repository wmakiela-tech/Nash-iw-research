# NASH/IW — Canonical Repository Structure

**As of:** 2026-10-12  
**Status:** CURRENT / forward-only repository placement contract  
**Authority:** repository/custody organization only; no scientific authority.

This repository is a durable public-safe scientific archive, reproducibility surface and external bridge. It is not a dump of Google Drive and it is not a second BW.

## Canonical top-level layout

```text
README.md
CONTRIBUTING.md
docs/                    current public-safe system/operator contracts
research/                full public-safe scientific artifacts
archive-index/           pointer/hash/legacy archive entries and public-safe compact returns
succession/              public-safe succession pointers/manifests only
runtime/                 executable research/runtime code
src/                     reusable source code
tests/                   tests and deterministic controls
fixtures/                public-safe fixtures
schemas/                 machine-readable contracts
templates/               current reusable instruments
manifests/
  cross-surface/         BW↔GitHub custody/currentness projections
  reproduction/          reproducibility manifests
legacy/                  only when an old layout cannot remain safely in place
```

## Exact cross-surface placement prerequisite (2026-10-22)

The repository layout below governs **public** paths. For private material, the controlling directory trees and the complete mandatory write/read sequence are specified in [`IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md`](IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md): `NASH–IW Shared Research Bridge/04_PRIVATE_PROJECT_DOCUMENTS_CURRENT/` and its verified class/topic subfolders. Do not convert a private Drive-origin manuscript into public content merely to populate `research/`, and do not save public-safe science only in Drive with a GitHub `POINTER_ONLY` placeholder. Each material return must have one identifiable canonical body and matching BW custody.

## Canonical placement rules

### `docs/`
Only current operator/system contracts. A dated research result does not belong here.

### `research/<lineage>/<YYYY-MM-DD>/`
Full public-safe research bodies. Use lowercase lineage directory names going forward.

Examples:
```text
research/mt13/2026-10-12/<artifact>.md
research/m12/2026-10-12/<artifact>.md
research/xh-s3/2026-10-12/<artifact>.md
research/mech-s6/2026-10-12/<artifact>.md
```

Historical paths such as `research/LT4/`, `research/mt13/<file>`, or `research/prf11/2026-10-12/` remain valid provenance. Do not mass-rename them merely for cosmetics. New writes use the canonical layout.

### `archive-index/<YYYY>/<lineage>/`
Compact public-safe archive record, pointer, hash witness or legacy return. It is not the preferred location for new full research bodies when the content is publication-safe.

### `succession/<YYYY>/<lineage>/`
Public-safe succession identity/currentness records. Private succession packet bodies stay on private custody surfaces; GitHub stores only a safe pointer/hash/provenance record unless the packet is explicitly publication-safe.

### `manifests/cross-surface/`
Derived projection connecting GitHub artifacts to BW ingestion/currentness. The manifest is not a scientific registry and never overrides BW.

## One logical artifact, one canonical GitHub body

A logical artifact must not acquire multiple independent GitHub bodies merely because it crossed Drive, Slack or BW.

```text
COPY != NEW_ARTIFACT
MIRROR != SECOND_PRIMARY
POINTER != BODY
COMMIT != BW_ADOPTION
```

If a legacy copy already exists, add a manifest/lineage relation instead of another duplicate body.

## Path stability

Do not move a historical file solely to satisfy a newer aesthetic rule when BW or external citations already bind to an immutable commit/path. New structure is forward-only. When a path must change materially, preserve the old commit as provenance and add explicit `supersedes` / `derived_from` metadata.

## Public/private boundary

This repository is public. Full content is legal only for `PUBLIC_ARTIFACT` or `EXECUTABLE_REPRODUCTION`. Private/restricted material uses `POINTER_ONLY` or `HASH_ONLY` and must not expose private Drive/Slack coordinates.

See `STORAGE_AND_SYNC_POLICY.md`.

## Successor repository onboarding (2026-10-18)

Successors must review this structure, `START_HERE_CURRENT.md`, OW work/reproducibility protocol and storage/sync policy at the beginning of legal orientation before placing their first artifact. `docs/` is the canonical public-safe home for current operational rules; private succession contents remain private. Changes to rules require updating canonical source and relevant cross-links rather than creating duplicate competing `docs/` primaries. Read back the edited body, then reconcile BW/cross-surface metadata separately. Protected exposure constraints prevail.
