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

## Slack-native scientific source recovery (risk-triggered)

Slack messages and **thread replies** can themselves contain the only complete scientific return when Drive/Docs or GitHub writes fail. Treat this as a source-loss risk, not as evidence of scientific failure. A delivered Slack message is a recoverable original carrier, but is not proof that its full body exists on another surface.

When there is a **concrete** loss signal (declared write failure, empty/placeholder Drive body, unavailable linked artifact, source-only thread reply, or material currentness discrepancy):

1. Resolve the original message's stable return/artifact ID, Slack message timestamp, channel/thread context, corrections and supersession. A plain channel-history read can omit thread replies; use bounded thread-aware retrieval for this source audit.
2. Search BW and existing Drive/GitHub custody **before** copying. Verify body presence and completeness, not just document existence, a pointer, or a `SYNCED` label.
3. If the original body lacks independent durable custody, copy its complete substantive text into a legally permitted **private** source artifact with source message ID/time, original locator, capture date, author/lineage if verified, and the unchanged original claim ceilings. Verify the new body by semantic readback against Slack. Record transport-normalization differences where relevant.
4. Link the recovered body in **private** BW custody, preserving the original Slack source as provenance. BW scientific qualification/owner currentness are unchanged. Public GitHub publication is optional and restricted to independently classified public-safe content; a sanitized pointer is not the body.
5. If writes are denied, retain an explicit unresolved risk and the original Slack reference. Do not call an empty object saved, and do not route around provider protection. Distinguish storage, delivery, receipt, ingestion and scientific acceptance.

This is an **event-triggered rescue**, not a universal Slack crawl, per-cell thread-reading ritual, mandatory duplication of every message, or synchronous GitHub mirror gate. Historical backfill is value-driven. A single complete, independently recoverable private body plus stable source/custody identity can be sufficient.

```text
CHANNEL_HISTORY != THREAD_SEARCH
DOCUMENT_EXISTS != NONEMPTY_SOURCE_BODY
SLACK_DELIVERY != EXTERNAL_BODY_PERSISTENCE
RECOVERABILITY_REQUIRED != EVERY_BODY_EVERYWHERE
TRACEABILITY_REQUIRED != SYNCHRONOUS_MIRRORING_REQUIRED
SOURCE_RECOVERY != SCIENTIFIC_PROMOTION
```

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
