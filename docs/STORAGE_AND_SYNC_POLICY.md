# NASH/IW — Storage and Cross-Surface Sync Policy

**As of:** 2026-10-12  
**Status:** CURRENT / forward-only custody policy  
**Scope:** GitHub ↔ BW ↔ Google Drive / frozen stores.

## Moderator routing clarification — public science first (2026-10-12)

**Controlling operational default, directly clarified by the Moderator:** scientific results that have been checked for public release belong as **full source-bearing research artifacts in public GitHub**, with BW ingestion and cross-surface custody pointing to the exact Git commit. Google Drive is the **private project document and restricted source store**, not the default final home for publishable scientific results. BW remains the private currentness/qualification/provenance ledger and does not become a duplicate public science-body repository.

This modifies **default placement and write completion criteria**, not scientific acceptance or permission for uncontrolled exposure. A scientific artifact can be a candidate, conditional theorem, falsifier, counterexample, negative result, prior-art subtraction or open-problem map; `NO_CANON` / `NO_EXEC_SIGN` is retained. Publication on GitHub does not imply novelty, external peer review, authority or correctness.

### Forward routing by source exposure

| Material | Primary durable body | Controlling link/status |
| --- | --- | --- |
| Explicitly classified public-safe scientific return and its public-safe code/data/test inputs | Full text under `research/<lineage>/<YYYY-MM-DD>/` and reproducibility folders on GitHub | BW `REGISTRY` event + private `CROSS_SURFACE_CUSTODY` GitHub path/commit/mode |
| Private/restricted research, unreleasable manuscript, private review, succession/cell state, private coordination and provider locators | Restricted Drive/frozen authorized store | BW private locator and restriction reason; no automatic public mirror |
| Mixed public scientific result + restricted provenance/appendices | Split: standalone public-safe scientific body to GitHub; restricted originals and appendices to private Drive | One stable logical artifact/relation with source identity and exposure/derived-from distinctions in BW |
| Slack thread/response | Transport only, except explicit documented source-only hold | Immutable original source identity in BW; legal durable body still required |

**Do not use "the document is on a private Drive" as proof its scientific *content* is permanently private.** Content exposure classification and actual release eligibility govern routing, not the storage container. Conversely, identifying a science topic does not automatically authorize publishing restricted raw documents. Validate source licenses, private locations, personal data, prohibited sharing and source completeness before publication.

### Publication-complete handshake for new scientific work

1. Preserve the complete load-bearing science body: object/theorem/counterexample, exact hypotheses, domain, method/source, boundary/caveats, negative knowledge and unresolved tests; don't replace it with a short pointer or promotional abstract.
2. For **PUBLIC** content, write to canonical GitHub `research/`, retaining stable artifact/return ID, `exposure: PUBLIC`, original claim ceiling and a BW event if known. Record the exact verified Git commit. Code and data required to reproduce the claim should be published if safe; otherwise state exactly which dependencies remain restricted/missing.
3. BW ingests the **same** source identity through normal owner/KN workflow and records qualification/lifecycle (not as an assistant-invented substitute), with a private cross-surface row binding Git path, immutable commit, publication mode and any private original provenance.
4. Read back GitHub science body + BW source row + custody record. Only then mark `PUBLIC_ARTIFACT / SYNCED` for a completed public scientific body. If GitHub text was saved but BW not yet ingested: `GITHUB_PENDING_BW_INGEST`; if BW exists but GitHub publication is legally pending: `BW_PENDING_GITHUB_PUBLICATION`; if truly restricted: `PRIVATE_ONLY` or allowed `POINTER_ONLY` with explicit restriction.
5. **A `POINTER_ONLY` file is not a public scientific-body delivery.** For a public-safe science result it is a *temporary migration/publication gap*, not completed publication. A permanent pointer is justified only by a verified restriction, an explicitly non-scientific metadata-only record, or a genuinely missing source body recorded as such.
6. On later source revision or public-science promotion from a private source, update the **same source identity** and custody mapping without generating a second BW scientific-ingestion event. Keep original private provenance; mark the old pointer as superseded rather than leaving two canonical bodies.
7. Do not force all project messages into GitHub or mandate byte-identical GitHub/Drive mirroring. Only **material, legally publishable scientific results** require the public source body. No bulk historical migration without a bounded eligibility/content review.

```text
PUBLIC_SCIENCE_BODY != POINTER_ONLY
PUBLICATION_COMPLETE = PUBLIC_BODY_READBACK + BW_INGESTION + CROSS_SURFACE_READBACK
PUBLICATION != SCIENTIFIC_ACCEPTANCE
PRIVATE_SOURCE_CARRIER != PRIVATE_SCIENCE_CONTENT_BY_DEFINITION
DRIVE_PRIVATE != GITHUB_UNSAFE_FALLBACK
```

### Exact-path rule for every cell — controlling addendum (2026-10-22)

All material-return writers must apply the exact route and retrieval matrix in [`IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md`](IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md). **Generic instruction to “save on GitHub/Drive” is insufficient.** Public science goes in `research/<lineage>/<YYYY-MM-DD>/` as a complete body; private packets in Drive `04_PRIVATE_PROJECT_DOCUMENTS_CURRENT/01_CELL_SUCCESSION_AND_HANDOFF_PACKETS/`, private science in `02_PRIVATE_SCIENTIFIC_SOURCE_AND_REVIEW/<topic>/`, books in `03_MONOGRAPHS_AND_LIVING_BOOKS/`, private reproducibility in `04_REPRODUCTION_DATA_CODE_PACKAGES/`, science-bearing Slack recoveries in `05_SLACK_SOURCE_RECOVERY/`, and true holds in `99_BLOCKED_HOLD_AND_EXCEPTION/` when permitted. Public policies modify existing `docs/`; BW remains in its pre-existing private operating location.

For every publication, preserve `artifact_id`, `exposure`, `canonical_path`, `git_commit/source_revision`, `bw_event_or_pending`, original qualification and claim ceiling. Check the final readback at both source and custody layers. Never use Slack dispatch, a Drive-root upload, or a GitHub pointer as a substitute for a complete durable result.

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

## Successor orientation and cross-surface rule propagation (2026-10-18)

Before writing or routing a new material artifact, a successor must consult the **current** storage/sync policy, repository structure, OW work protocol and communication playbook. Revisions are resolved from their primary source; inherited Drive excerpts do not supersede the public-safe GitHub primary. When any load-bearing rule changes, update its owning canonical body, review linked navigation/succession references, check corresponding private source orientation, and record which surfaces were actually synchronized; a GitHub commit alone is not BW ingestion or Slack delivery. Preserve private/protected data outside public GitHub. Scientific data existing only in Slack are evidence requiring provenance-safe private capture/reconciliation, not automatically empty because Drive lacks a copy. No blind mass-migration or fabricated synchronization status.
