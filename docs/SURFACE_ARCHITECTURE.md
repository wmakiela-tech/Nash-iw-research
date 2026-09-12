# NASH/IW — Multi-Surface Architecture

**As of:** 2026-09-12  
**Classification:** public-safe system/operator guidance.  
**Authority:** descriptive routing contract only; no `CANON`, no `EXEC_SIGN`, no scientific claim upgrade.

NASH/IW deliberately uses several communication and storage surfaces because the project has several materially different needs. The goal is not to force all work into one backend. The goal is to preserve the function that each surface performs best while keeping authority, evidence, currentness, custody and transport distinct.

```text
AUTHORITY != EVIDENCE != CURRENTNESS != CUSTODY != TRANSPORT
STORAGE != DELIVERY != RECEIPT != ACCEPTANCE
```

## 1. Surface roles

### GitHub — public durable archive + executable surface + external bridge

GitHub has several legitimate roles at once:

1. **Executable/reproducibility surface** — code, tests, schemas, manifests, CI, reproducible public fixtures.
2. **Public archive/index** — durable public-safe historical artifacts, archive pointers, checksums and lineage records.
3. **External model bridge** — issues/PRs and stable files that can be read by participants such as Grok without requiring access to the private IW commons.
4. **Public orientation/currentness resolver** — enough navigation to find the controlling private source family without copying unpublished private state into this repository.

GitHub is not automatically the current scientific truth store. A commit, issue, PR or green CI run may carry evidence or provenance without carrying scientific authority.

```text
GITHUB_COMMIT != BW_EVENT
GITHUB_ISSUE != SCIENTIFIC_ADOPTION
GITHUB_MERGE != EXEC_SIGN
CI_PASS != SCIENTIFIC_VALIDATION
PUBLIC_ARCHIVE != PRIVATE_CURRENTNESS
```

### Private Google Drive / BW — private scientific currentness and custody

Use for:

- current qualified scientific/project state;
- source-linked review and qualification artifacts;
- supersession/currentness and open-frontier resolution;
- private cross-cell artifacts;
- current private system/governance documents;
- durable scientific custody when material is not publication-safe.

BW is a currentness/custody substrate, not a live-chat surface.

### Slack — low-friction live coordination and bounded dialogue

Use for:

- dispatch and alerts;
- short model↔model hypothesis → attack/counterexample → repair loops;
- receipt-visible routing;
- compact terminal qualified returns when appropriate.

Do not treat a Slack transcript as scientific currentness by itself.

```text
LIVE_DIALOGUE != DURABLE_SCIENTIFIC_CUSTODY
POSTED != RECEIVED != ACCEPTED
```

### File Library / frozen bundles — exact historical payloads

Use for:

- frozen reports;
- exact data payloads;
- archived CSV/JSON/PDF/package material;
- artifacts whose value is exact preservation rather than live editing.

### Coda / Airtable / similar structured surfaces — experimental coordination surfaces

These may be useful for structured mailbox/queue functions when selective retrieval, concurrency or multi-session coordination creates real pressure. They are not default truth stores and should not be adopted merely because they support richer schemas.

## 2. Communication routes and fallback

Every material task has one stable `task_id` across transports. Moving from Slack to GitHub or Drive is a relay of the same task, not a new task. Record the attempted route and delivery state; never infer receipt from a successful write.

| Communication need | Primary route | Safe fallback | Durable terminal record |
|---|---|---|---|
| rapid internal dispatch/correction | Slack thread | private Drive task packet or Moderator relay | qualified BW/Drive artifact when material |
| public-safe asynchronous external task | GitHub Issue | GitHub PR/discussion on the same `task_id` | issue disposition + linked commit/artifact |
| private cross-cell packet | private Drive/BW | File Library/frozen bundle + legal relay | private qualified source chain |
| code/reproduction review | GitHub Issue/PR | public-safe archive entry | merged/disposed PR + manifest/tests |
| connector outage | alternate route permitted by exposure class | local integrity witness pending custody | replay/import with deduplication and readback |

Fallback sequence:

```text
CLASSIFY_EXPOSURE -> BIND_TASK_ID -> TRY_PRIMARY_ROUTE
-> RECORD_DELIVERY_STATE -> USE_SAFE_FALLBACK_IF_NEEDED
-> REVALIDATE_CURRENTNESS -> ACCEPT_OR_RETYPE_RETURN
-> PERSIST_TERMINAL_STATE_IF_MATERIAL
```

Required delivery states are `DRAFT`, `POSTED`, `RECEIVED`, `ACCEPTED`, `REJECTED`, `SUPERSEDED`, `CANCELLED`, `DELIVERY_BLOCKED`, and `CUSTODY_PENDING`. Only the authorized acceptance owner may set acceptance.

## 3. GitHub archive modes

Public GitHub archival should use one of four explicit modes.

### `PUBLIC_ARTIFACT`

The artifact itself is safe to publish and useful to preserve verbatim or nearly verbatim.

Use when the content contains no restricted/private scientific material, credentials, personal data or unpublished source material.

### `POINTER_ONLY`

GitHub stores identity, status, role, retrieval instruction and optionally checksum, while the artifact remains in a private or frozen store.

Use when discoverability matters but publication would broaden exposure.

### `HASH_ONLY`

GitHub records a public-safe artifact identity and checksum/provenance statement without a private location or content.

Use when existence/integrity should be externally attestable but neither content nor private storage coordinates should be published.

### `EXECUTABLE_REPRODUCTION`

GitHub stores code + public-safe fixture/parameters + manifest/tests sufficient to reproduce a declared public result class.

This is stronger than a pointer but still does not confer scientific adoption.

## 4. Databases and registries

IW may use several structured stores because they answer different questions:

| Store | Function | Controlling for |
|---|---|---|
| BW/private registry | event/currentness ledger and private custody references | effective private project/scientific state, subject to resolver semantics |
| Living Theory | authored explanatory synthesis | current theory narrative, not raw evidence custody |
| GitHub archive index | public-safe artifact/task/reproduction catalogue | public discoverability and repository lineage only |
| GitHub Issues/Projects | public-safe task/return queue | workflow state only |
| Airtable/Coda-class database | optional searchable mailbox/projection | no authority unless explicitly adopted for a bounded function |

All database rows must use stable object/task/artifact IDs, expose `as_of` or source revision when representing currentness, and retain a pointer to the controlling source. Synchronization is projection/import, not silent last-write-wins. Conflicts resolve to `CURRENTNESS_UNRESOLVED/HOLD` until the owner or controlling source resolves them.

Minimal cross-store keys are `object_id`, `record_type`, `source_revision`, `as_of`, `status`, `owner`, `exposure`, `provenance`, and optional `supersedes` (`old -> new`). This is a boundary contract, not a requirement that every exploratory note become a database row.

## 5. Currentness under connector failure

A storage failure must not collapse scientific currentness into custody.

If a material result is otherwise qualified from a verified transport return and has a stable identity and integrity witness (for example a local SHA-256), the project may represent:

```text
CURRENTNESS_QUALIFIED
ARTIFACT_CUSTODY_PENDING_CONNECTOR_RECOVERY
```

provided the private/currentness owner accepts the return and no source/exposure rule requires the missing artifact before qualification.

Never invent a Drive pointer. Never downgrade a scientific result merely because a connector write was blocked. Replay/import later with deduplication and readback.

For public-safe material, GitHub may be a legitimate fallback durable surface. For private material, GitHub must **not** be used as an emergency bypass around exposure controls.

```text
WRITE_BLOCK != SCIENTIFIC_FAILURE
HASH != ARTIFACT_DELIVERY
PUBLIC_FALLBACK != PRIVATE_DATA_BYPASS
```

## 6. Model-to-model communication

The current low-cost candidate pattern is transport-agnostic:

```text
PRE_SESSION_CURRENTNESS
→ BOUNDED_DIALECTIC_SESSION
→ PRE_ACCEPTANCE_REVALIDATION
→ [IF MATERIAL] TERMINAL_QUALIFIED_STATE
```

The transient session should carry deltas rather than repeatedly restating full project context. The durable/current path must still be able to recover the load-bearing reason for a material narrowing/retraction, or return explicit `UNRESOLVED/HOLD` and escape to the controlling source family.

Preserve the correction capacity, not a particular chat mechanism.

## 7. Selection rule

Choose a surface by the function needed, not by institutional habit.

| Need | Preferred surface |
|---|---|
| rapid bounded dialogue | Slack thread or equivalent low-friction transient transport |
| private scientific currentness | BW / private Drive |
| exact frozen historical payload | File Library / frozen bundle |
| public code/reproduction | GitHub |
| public-safe archive / lineage | GitHub |
| Grok/external participant readable task or artifact | GitHub issue/file/PR |
| structured multi-session mailbox pressure | Coda/Airtable-class surface, only after demonstrated need |

A surface may perform more than one role, but role boundaries must remain explicit.

## 8. Naming and retrieval

Use one canonical artifact filename and stable ID across GitHub, Drive/BW, Slack references and database projections. Do not prepend upload-order numbers or rename an artifact merely because it crossed a transport boundary. Full rules: [`NAMING_AND_INDEXING.md`](NAMING_AND_INDEXING.md).

## 9. Architecture principle

```text
PRESERVE_FUNCTION > PRESERVE_MECHANISM
PRESERVE_OPTIONALITY > PRESERVE_RESEMBLANCE
ARCHITECTURE_MUST_BE_ALLOWED_TO_EVOLVE
```

A useful new transport can become an episodic organ without becoming permanent architecture. Repeated natural value is evidence for preserving the capability; it is not evidence that the current backend must be frozen forever.
