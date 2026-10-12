# NASH/IW — Storage and Cross-Surface Sync Policy

**As of:** 2026-10-12  
**Status:** CURRENT / forward-only custody policy  
**Scope:** GitHub ↔ BW ↔ Google Drive / frozen stores.

## Core invariant

GitHub and BW must be mutually traceable without becoming competing truth stores.

```text
GITHUB_ARTIFACT -> BW_INGESTION_OR_EXPLICIT_NOT_INGESTED
BW_PUBLIC_ARTIFACT -> GITHUB_COMMIT_OR_EXPLICIT_PUBLICATION_STATE
BW_PRIVATE_ARTIFACT -> PRIVATE_CUSTODY + OPTIONAL_PUBLIC_POINTER/HASH
```

The BW `REGISTRY` remains the private event/currentness ledger. GitHub provides immutable public-safe content, code, history and external inspection.

## Required cross-surface identity

For every material public GitHub artifact preserve:

- stable `artifact_id` / contribution identity;
- `bw_ingestion_event_id` when ingested;
- GitHub canonical path;
- immutable commit SHA;
- archive mode;
- source revision/provenance;
- epistemic status copied from BW as a projection, never upgraded by GitHub.

For every material BW entry whose public content is stored on GitHub preserve privately in BW:

- Drive/private source locator when applicable;
- GitHub canonical path;
- immutable GitHub commit;
- mirror/archive mode;
- cross-surface sync state.

## Archive modes

- `PUBLIC_ARTIFACT` — public-safe body stored on GitHub.
- `EXECUTABLE_REPRODUCTION` — code + public-safe fixture/manifest/test.
- `POINTER_ONLY` — GitHub stores identity/status/BW event, not private body or private locator.
- `HASH_ONLY` — only public-safe integrity witness.
- `PRIVATE_ONLY` — no GitHub record required when even existence/metadata is restricted.

## Sync states

```text
SYNCED
GITHUB_PENDING_BW_INGEST
BW_PENDING_GITHUB_PUBLICATION
DRIVE_PRIVATE_POINTER_ONLY
GITHUB_ARCHIVE_ONLY_NOT_INGESTED
CONFLICT_HOLD
SUPERSEDED
```

`SYNCED` means the identity and locations agree. It does not mean scientific acceptance.

## Write rule

### New public-safe research
1. Create/persist the public body on GitHub under the canonical path.
2. Record immutable commit.
3. Ingest/qualify through BW.
4. Record BW event + GitHub commit/path in the private cross-surface custody projection.
5. Read back both sides.

### New private/restricted research
1. Persist on Drive/private/frozen custody.
2. Ingest through BW.
3. If public discoverability is useful, create only a sanitized pointer/hash record on GitHub.
4. Never publish private Drive/Slack coordinates.

### Connector failure
If Drive write fails and the content is public-safe, GitHub may become the temporary durable primary. Mark `GITHUB_PENDING_BW_INGEST` until BW is updated. If content is private, do not bypass exposure controls; use `CUSTODY_PENDING`/frozen private fallback.

## Reconciliation rule

At bounded currentness/repository maintenance time compare by stable artifact identity, not filename similarity alone.

Detect at least:
- BW row with public-safe Drive-only body and no GitHub representation;
- GitHub artifact with no BW ingestion/status;
- BW row pointing to an old Drive locator after an immutable GitHub mirror exists;
- duplicate GitHub bodies for one artifact;
- GitHub path whose content is newer than the BW-qualified source revision;
- superseded artifacts still presented as current.

No silent last-write-wins. Any material contradiction becomes `CONFLICT_HOLD`.

## Public manifest rule

`manifests/cross-surface/` may publish artifact IDs, BW ingestion IDs, GitHub paths/commits, archive mode and public-safe status. It must not publish private provider coordinates.

## Non-collapse guards

```text
GITHUB_COMMIT != BW_EVENT
BW_INGESTION != SCIENTIFIC_ACCEPTANCE
MIRROR_SYNC != CLAIM_VALIDATION
DRIVE_WRITE_FAILURE != SCIENTIFIC_FAILURE
PUBLIC_GITHUB != PRIVATE_IW_COMMONS
```
