# NASH/IW — Source of Truth, Currentness and Custody

**As of:** 2026-09-12

NASH/IW deliberately uses different surfaces for different information functions. No single repository, chat, spreadsheet or archive is the source of truth for everything.

```text
AUTHORITY != EVIDENCE != CURRENTNESS != CUSTODY != TRANSPORT
STORAGE != DELIVERY != RECEIPT != ACCEPTANCE
```

## Source roles

### GitHub — public executable, archive and external-bridge surface

Use for:

- code, tests, schemas and CI;
- public-safe fixtures and small manifests;
- public-safe operator/system documentation;
- public archive/index, hashes, lineage and reproducibility artifacts;
- issues and PRs;
- public-safe asynchronous tasks/returns for external participants such as Grok.

GitHub does **not** automatically carry the current unpublished scientific state.

### Private Google Drive / BW — shared private scientific/project currentness and custody

Use for:

- current qualified scientific/project state;
- source-linked qualification/review packets;
- lifecycle, supersession and open-frontier state;
- private cross-cell research artifacts;
- current private system/governance guidance;
- durable scientific custody where publication is not legal or useful.

Primary current scientific/project resolver:

`IW_KCELL_BW_V0_2_OPERATING_LAYER_001_20260824`

Resolve effective currentness from the current source/event chain, not from one historical row or merely the newest timestamp.

### Slack — transient delivery and dialogue

Use for dispatch, alerts and low-friction bounded interaction. Slack can provide transport visibility and a qualified return, but a transcript is not automatically durable scientific currentness.

### File Library / exact frozen bundles

Use for exact historical reports, CSV/data payloads, frozen packages and artifacts that are not naturally maintained as live GitHub or Drive content.

### Structured coordination surfaces

Coda/Airtable-class surfaces may be used experimentally for mailbox/queue functions when real retrieval or concurrency pressure appears. They are not default truth stores.

## Precedence by question

| Question | Preferred evidence |
|---|---|
| What does the current project believe / keep open? | current BW/private qualified state |
| What exactly did a paper/reviewer/result claim? | primary source/review artifact or verified qualified return |
| What did code actually do? | exact code + parameters + data/manifest + runtime output |
| Which project rule currently applies? | current System Core / applicable-document index |
| Is a GitHub implementation reproducible? | repository commit + CI/tests + manifest/runtime evidence |
| What can an external participant such as Grok inspect without private access? | public GitHub issue/PR/file/task capsule |
| Is something scientifically true? | not decided by storage location, CI, consensus, GitHub merge or message visibility |

## Currentness and custody may diverge temporarily

During connector failure, a scientific/currentness owner may accept a material verified return while durable artifact persistence remains incomplete.

Legal representation when properly qualified:

```text
CURRENTNESS_QUALIFIED
ARTIFACT_CUSTODY_PENDING_CONNECTOR_RECOVERY
```

Requirements:

- stable result/task identity;
- verified return on a legal transport;
- enough integrity/provenance to distinguish the intended artifact/result (for example a local SHA-256 when available);
- no claim that the missing durable artifact was delivered;
- later replay/import with deduplication and readback.

This does not permit private content to be published to GitHub as an emergency bypass.

```text
WRITE_BLOCK != SCIENTIFIC_FAILURE
HASH != ARTIFACT_DELIVERY
PUBLIC_FALLBACK != PRIVATE_DATA_BYPASS
```

## Required distinctions

```text
SOURCE != ASSERTION != EVIDENCE != SYNTHESIS
STORAGE != DELIVERY != RECEIPT != ACCEPTANCE
CI_PASS != SCIENTIFIC_VALIDATION
GITHUB_MERGE != EXEC_SIGN
GITHUB_ISSUE != BW_EVENT
CURRENT_POINTER != CANON
NO_SEARCH_HIT != NOVELTY
RESULT_MEMORY != REGENERATION_CAPACITY
```

## Staleness rule

Every current-state summary should expose an `as_of` date or current build/event pointer. If a summary conflicts with a newer qualified source or BW event, the summary becomes stale; do not silently reinterpret it as current.

A title, filename or empty placeholder does not prove that its intended content was successfully persisted.

```text
FILE_EXISTS != CONTENT_PERSISTED
TITLE != RETURN_RECEIVED
```

## Public GitHub archive modes

Use the archive modes defined in [`SURFACE_ARCHITECTURE.md`](SURFACE_ARCHITECTURE.md):

- `PUBLIC_ARTIFACT`;
- `POINTER_ONLY`;
- `HASH_ONLY`;
- `EXECUTABLE_REPRODUCTION`.

Select the least exposing mode that still preserves the intended function.

## Minimal research handoff expectation

A material result should make it possible to recover:

- artifact/source identity;
- scope and assumptions;
- epistemic status;
- relation to prior state;
- negative knowledge or unresolved conflict where relevant;
- exact runtime/source pointers for load-bearing steps;
- the load-bearing reason for a material narrowing/retraction, or an explicit `UNRESOLVED/HOLD` when that reason is not legally recoverable;
- enough configuration/procedure to regenerate evidence when future use depends on reproducibility.

This is a semantic expectation, not a requirement to create a large form for every exploratory action.
