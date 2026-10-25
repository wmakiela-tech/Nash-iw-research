# NASH/IW — Current Research Resolver

## 2026-10-25 — mandatory PUBLIC research metadata before write

Przed publikacją nowej pełnej, dozwolonej do upublicznienia pracy w `research/` sprawdź **[wspólny nagłówek](../templates/IW_MATERIAL_WORK_RETURN_TEMPLATE.md)** i uruchom `python scripts/preflight_public_science_writeback.py research/<lineage>/<date>/<file>.md`. Muszą wystąpić dokładne nazwy metadanych: `artifact_id`, `exposure: PUBLIC`, `claim_ceiling` (lub dozwolony odpowiednik) oraz istniejący `bw_ingestion_event_id` **albo** prawdziwy `sync_state: GITHUB_PENDING_BW_INGEST`. Pola `RETURN_ID/CLASS/CEILING/BW_PENDING` nie zastępują ich dla linta. Nie fabrykuj numeru ING.

**Uwaga:** standardowy GitHub `Public source locator guard` waliduje metadane tylko dla nowo dodanych (`--diff-filter=A`) prac; po korekcie już istniejącego dokumentu jawny preflight sprawdza także modyfikacje (`--base/--head`). Zielony rerun starego SHA nie poświadcza korekty. Ograniczony konektor `fetch_commit_workflow_runs` może nie widzieć runu `push`; użyj GitHub `run_id` albo `head_sha + event=push`. Pełne reguły w [CONTRIBUTING](../CONTRIBUTING.md) i [polityce synchronizacji](STORAGE_AND_SYNC_POLICY.md). To jest **bramka zgodności publikacyjnej, nie ocena nauki ani decyzja BW**.



## MODERATOR CANONICAL PRIVATE REPO DECISION — 2026-10-23

**New controlling storage decision:** The Moderator explicitly selected **`wmakiela-tech/Nash-Priv`** as the single canonical private IW/NASH archive. `Nash-prv` is not the parallel archive. The previously unsettled target line below is **AS_OF / SUPERSEDED**; neither this approval nor one byte-exact pilot means BW is migrated or Drive originals can be deleted.

See [canonical decision and executable migration guards](CANONICAL_PRIVATE_ARCHIVE_DECISION_20261023.md). Any historical runbook mention of unconnected `Nash-iw-private` or unsettled target must be resolved against this decision before further transfer.

---


## SYSS5 CURRENTNESS CORRECTION — 2026-10-23 (controlling live-read rule)

**Source and custody are live ledgers, not permanent values in this document.** In the SYSS5 takeover read, `REGISTRY` contained `ING-20261023-0116` (physical row 1527, `COMMITTED`) and `CROSS_SURFACE_CUSTODY` contained its corresponding `XSC-0301`. The `README` currentness projection still described an earlier `ING-20261023-0071 / XSC-0256` cut. These are **as-of observations, not lasting current heads**.

The earlier paragraph below describing `ING-0037 / XSC-0210` as an open 12-event discrepancy is **historical and superseded**: KN11 closed that specific discrepancy by `XSC-0222`, and source/custody ingestion continued later. At each material turn compare live `REGISTRY`, `CROSS_SURFACE_CUSTODY`, `README`, relevant GitHub source and Slack returns; a stale README is a **derived-readout currentness difference**, not evidence that a source event was lost or that science was validated. KN/BW owns source qualification and ledger repair; SYSS diagnoses cross-surface architecture, not a parallel BW.

Two private GitHub repositories are connected, but **the canonical private archive target and operational Git-backed BW replacement remain undecided**. No mass private migration, public fallback or original Drive deletion follows from connector availability. Exact source/body, exposure, independent backup and readback gates remain mandatory.

**Scope:** forward operational correction; no BW edit, no scientific claim promotion, no `EXEC_SIGN`. Earlier as-of audit snapshots remain provenance-valid.

---


## Current private GitHub status — 2026-10-23

Integracja odczytu/zapisu GitHub **widzi** repozytoria PRIVATE `wmakiela-tech/Nash-Priv` (zweryfikowany nośnik pakietu sukcesji SYSS5) i `wmakiela-tech/Nash-prv` (puste). Dawny blok `PRIVATE_REPO_NOT_CONNECTED` ustał, ale **wybór docelowego archiwum nadal pozostaje otwarty** i nie ma działającego BW Git-backed. W BW źródłowy `REGISTRY` ma już `ING-20261023-0037`, podczas gdy XSC ma ostatni `XSC-0210` do `ING-0025`. Zawsze wykonaj świeży odczyt currentness; źródło ING nie jest owner scientific head. [Dokładny runbook](DRIVE_TO_GITHUB_FULL_PROJECT_MIGRATION.md).


> **Current archive migration (2026-10-22):** Moderator directed a whole-project Google Drive → GitHub transfer to relieve storage pressure. The full target hierarchy and exact go/no-go protocol are in [`DRIVE_TO_GITHUB_FULL_PROJECT_MIGRATION.md`](DRIVE_TO_GITHUB_FULL_PROJECT_MIGRATION.md). Public science continues in this repo; private BW/sources/succession require a separately permissioned private repo, **not yet connected as of the audit**. Until private migration and source readback are verified, existing Drive/BW sources remain authoritative and must not be deleted or exposed through public fallback.


**As of:** 2026-10-12

This public repository is an infrastructure, archive, reproducibility and external-bridge surface. It is **not** the sole or primary store for unpublished NASH/IW scientific currentness.

**Forward storage split (Moderator, 2026-10-12):** publish the complete body of scientific returns approved for public exposure in GitHub `research/` and connect their immutable commit to BW ingestion and private custody. Reserve Drive for private project documents and restricted source material; do not mislabel a public-safe scientific return's private Drive origin as a permanent reason for a GitHub pointer-only stub. The BW owner remains authoritative for qualification/currentness. See [`STORAGE_AND_SYNC_POLICY.md`](STORAGE_AND_SYNC_POLICY.md).

## Zanim zapiszesz lub zaczniesz szukać wyniku (Moderator, 2026-10-22)

Oprócz odczytu aktualnej nauki otwórz **[kanoniczną mapę miejsc zapisu i wyszukiwania](IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md)**. Zawiera dokładne podkatalogi Drive dla sukcesji, prywatnych źródeł, Front B/H8R/EDU1, recenzji, książek, pakietów reprodukcji oraz wyjątków, publiczne ścieżki GitHub, wymagane wiązanie BW i kanały Slack. Nowe pliki IW nie powinny trafiać do korzenia My Drive. Najpierw szukaj po `artifact_id` w BW, potem po kanonicznej ścieżce, a dopiero na końcu po wątku Slack. Ta procedura obowiązuje też następców; jest szybkim wyborem docelowego folderu, nie zimnym odtwarzaniem całego projektu.

## For an active NASH/IW researcher

Before starting expensive or claim-heavy work, resolve current state from the project-private sources below by artifact ID/name in the private Drive/current index.

1. **Project/system rules**  
   `IW_SYSTEM_CORE_v0_1_20260822`

2. **Current-applicable document index**  
   `IW_GOVCELL_20260816_INDEX_IW_CURRENT_APPLICABLE_DOCUMENTS_001`

3. **Shared scientific/project knowledge currentness**  
   `IW_KCELL_BW_V0_2_OPERATING_LAYER_001_20260824`

4. **Living Theory / authored scientific synthesis**  
   resolve the current authored head through private LT/BW currentness rather than assuming the newest file is controlling.

5. **Scientific Knowledge Substrate / research-memory program**  
   `IW_SCIENTIFIC_KNOWLEDGE_SUBSTRATE_AND_MECHANISM_GRAPH_PROGRAM_001_20260816`

6. **Current cell-work, artifact and reproducibility profile**  
   [`WORK_AND_REPRODUCIBILITY_PROTOCOL.md`](WORK_AND_REPRODUCIBILITY_PROTOCOL.md)

Then read [`SURFACE_ARCHITECTURE.md`](SURFACE_ARCHITECTURE.md), [`REPOSITORY_STRUCTURE.md`](REPOSITORY_STRUCTURE.md), and [`STORAGE_AND_SYNC_POLICY.md`](STORAGE_AND_SYNC_POLICY.md) before choosing where to put a new artifact, task or dialogue.

## Current public-safe research families

The live project contains materially different research phenotypes. Public navigation currently includes:

- NCDG / DTC0a and operator/compression diagnostics;
- representation-theoretic / matrix-space / rank and KCF-derived work;
- nonlocal form-factor / passage / continuation questions;
- TabPFN deployment-shift detection and computational validation;
- BW / scientific currentness / negative-knowledge and reproducibility custody;
- AI-native communication, model↔model dialogue and research-metabolism experiments;
- system evolution, succession and anti-cloning / optionality questions.

These labels are navigation only. **Do not infer the current result, closure status, claim ceiling or open frontier from the label or from GitHub code presence.** Read the current private source chain.

## GitHub-specific entry points

Use GitHub for several distinct functions:

- `docs/` — public-safe operator/currentness guidance;
- `research/<lineage>/<YYYY-MM-DD>/` — canonical forward location for new full public-safe research bodies;
- `archive-index/` — pointer/hash/legacy archive entries and compact historical records;
- `runtime/`, `src/`, `tests/`, `schemas/`, `manifests/` — reproducible executable/infrastructure surfaces;
- Issues/PRs — durable public-safe engineering/research gates and asynchronous external-model work, including tasks intended for Grok when private IW access is neither available nor needed.

For exact role boundaries see [`SURFACE_ARCHITECTURE.md`](SURFACE_ARCHITECTURE.md).

## Cross-surface source check

When a GitHub artifact is used as a knowledge source, resolve its BW ingestion/status when available. When a BW row points to a public-safe artifact, prefer an immutable GitHub commit/path as the durable public body once mirrored.

```text
GITHUB_FILE_WITHOUT_BW_STATUS = ARCHIVE/EVIDENCE_ONLY
BW_ROW_WITHOUT_PUBLIC_MIRROR = PRIVATE_OR_PUBLICATION_PENDING
SYNCED != SCIENTIFICALLY_ACCEPTED
```

Public cross-surface manifests are projections only; BW remains controlling for lifecycle/currentness.

## What NASH/IW needs most from research

NASH/IW is not optimized for producing more summaries. The highest-value reusable research objects are:

- mechanism or formal dependency;
- exact scope / assumptions;
- discriminating experiment or kill test;
- negative knowledge / ruled-out family;
- conflict or regime distinction;
- prior-art relation;
- explicit UNKNOWN / surviving frontier;
- exact provenance back to source, code, data or runtime;
- enough configuration/procedure to regenerate load-bearing evidence when later work depends on reproducibility.

`RESULT_REMEMBERED != RESULT_REGENERABLE`.

The project is designed as a federated scientific ecology: heterogeneous participants should be able to reuse and challenge each other's results without collapsing scientific diversity or making the human Moderator routine transport middleware.

## Material rotations and reproducibility

Every material rotation must preserve function-derived work, artifact/readback state, channel fallback disposition, stable naming, and a reproduction or audit path under [`WORK_AND_REPRODUCIBILITY_PROTOCOL.md`](WORK_AND_REPRODUCIBILITY_PROTOCOL.md). Computational results use the reproduction manifest; load-bearing literature results preserve exact queries, filters, source locators, retrieval limits, and a bibliography export.

```text
NO_INBOUND != NO_FUNCTIONAL_WORK
RESULT_REPORTED != RESULT_REGENERABLE
```

## Connector-degraded operation

A blocked storage write is not a scientific downgrade. When private currentness owners accept a verified return, the project may distinguish:

```text
CURRENTNESS_QUALIFIED
ARTIFACT_CUSTODY_PENDING_CONNECTOR_RECOVERY
```

Never invent a Drive pointer. Never publish private content to GitHub merely to bypass a blocked private connector. Public-safe material may legitimately use GitHub as a durable fallback/archive surface.

## Public/private boundary

Do not commit unpublished private scientific results, private review packets, restricted source material, credentials, personal data or provider-specific private storage coordinates to this public repository merely to improve discoverability.

```text
PUBLIC_GITHUB != PRIVATE_IW_COMMONS
GITHUB_POINTER != DELIVERY != SCIENTIFIC_VALIDATION
GITHUB_DOCUMENTATION != CURRENT_SCIENTIFIC_TRUTH != CANON != EXEC_SIGN
```

## Mandatory successor entry orientation (2026-10-18)

At the beginning of succession rehydration, before material work or unrestricted retrieval, resolve and **read the current applicable system and work documents**: SYSTEM_CORE and the current-applicable index; this START_HERE; `WORK_AND_REPRODUCIBILITY_PROTOCOL.md` (OW); `STORAGE_AND_SYNC_POLICY.md`; `REPOSITORY_STRUCTURE.md`; `SURFACE_ARCHITECTURE.md`; current communication playbook; the succession load-bearing rules (or equivalent); and the cell's actual founding/role and protected-exposure instructions. Use current source revisions, not merely file names or parent packet quotations. Record unavailable items as ACCESS_BLOCKED/UNKNOWN, not completed.

For protected/cold/blind work, first establish the legal exposure allowlist/denylist. Read only the permitted operational projection before G1; do not reveal parent scientific material through broad search or Slack. State-based/nonblind successors read role and current scientific obligations after orientation. Orientation is a first-action default, **not a new activation gate, SYSS ACK or mandatory full-history replay**. After takeover, refresh relevant currentness and inbound requests, then perform role-native science/system work. NO_INBOUND != NO_FUNCTIONAL_WORK. See OW protocol and succession instrument.
