# NASH–IW Research Infrastructure

Public, versioned infrastructure, archive and reproducibility surface for NASH/IW.

GitHub has several roles in the project at once: executable/reproducibility surface, public-safe archive/index, durable asynchronous bridge to external participants such as Grok, and a public orientation layer pointing authorized researchers toward the private current-state resolvers. It is not the sole source of scientific truth.

**Current publication default (Moderator, 2026-10-12):** complete public-safe scientific results belong in `research/<lineage>/<YYYY-MM-DD>/` on GitHub, with explicit BW ingestion/custody links. Google Drive is the private/restricted project-document home; a pointer-only GitHub file is not completed publication of a releasable scientific result. GitHub publication is not scientific acceptance. See [`docs/STORAGE_AND_SYNC_POLICY.md`](docs/STORAGE_AND_SYNC_POLICY.md).

## Start here

Active NASH/IW researchers should begin with:

1. [`docs/START_HERE_CURRENT.md`](docs/START_HERE_CURRENT.md) — resolves the current private project/scientific state without publishing it here.
2. [`docs/WORK_AND_REPRODUCIBILITY_PROTOCOL.md`](docs/WORK_AND_REPRODUCIBILITY_PROTOCOL.md) — current cell-rotation, artifact, fallback, naming and reproducibility contract.
3. [`docs/SURFACE_ARCHITECTURE.md`](docs/SURFACE_ARCHITECTURE.md) — explains how GitHub, Drive/BW, Slack and frozen stores divide responsibilities.
4. [`docs/RESEARCH_SCOPE.md`](docs/RESEARCH_SCOPE.md) — public-safe map of research domains and high-value research outputs.
5. [`docs/SOURCE_OF_TRUTH.md`](docs/SOURCE_OF_TRUTH.md) — explains which surface answers which kind of question.
6. [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md) — repository authority and claim boundaries.
7. [`docs/NAMING_AND_INDEXING.md`](docs/NAMING_AND_INDEXING.md) — canonical IDs, filenames, metadata and supersession direction.
8. [`docs/REPOSITORY_STRUCTURE.md`](docs/REPOSITORY_STRUCTURE.md) — canonical repository layout and legacy-path policy.
9. [`docs/STORAGE_AND_SYNC_POLICY.md`](docs/STORAGE_AND_SYNC_POLICY.md) — BW↔GitHub↔Drive custody and synchronization contract.
10. [`docs/PRIVATE_DRIVE_AND_SLACK_INFORMATION_ARCHITECTURE.md`](docs/PRIVATE_DRIVE_AND_SLACK_INFORMATION_ARCHITECTURE.md) — project-private Drive folder taxonomy and Slack channel/navigation contract (identifiers remain private).


## GitHub roles

### Public executable/reproducibility surface

Use for code, tests, schemas, small manifests, CI, public-safe fixtures and reproducible operator documentation. New load-bearing results follow the shared reproduction manifest or literature-search record linked from the work protocol.

### Public-safe research, archive and lineage

Use `research/<lineage>/<YYYY-MM-DD>/` for new full public-safe scientific bodies. Use `archive-index/` for pointer/hash/legacy records and compact historical entries. Existing historical paths remain valid provenance and are not mass-renamed.

### External model bridge

GitHub issues, PRs and stable files can carry self-contained public-safe tasks and returns for participants that can read GitHub but do not have private IW commons access. Grok is a natural example for technical audit, refactor and repository/implementation critique.

A GitHub-visible return is transport/evidence, not scientific adoption.

### Currentness orientation

Public navigation may identify the controlling private source family and staleness boundary. Exact unpublished scientific currentness remains in private qualified sources/BW.

## Other storage and communication roles

- **Private Google Drive / BW:** curated current scientific/project state, cross-cell research packets, lifecycle/currentness, private qualification and durable scientific custody.
- **Slack:** dispatch, alerts and low-friction bounded model↔model dialogue; not a truth store.
- **File Library / frozen bundles:** exact historical reports, payloads, data files and frozen artifacts.
- **Coda/Airtable-class surfaces:** experimental structured coordination/mailbox surfaces only when real retrieval/concurrency pressure justifies them.

## Archive modes

Public GitHub archival should be explicitly one of:

- `PUBLIC_ARTIFACT` — content itself is safe and useful to publish;
- `POINTER_ONLY` — public index entry points to a privately held artifact without publishing it;
- `HASH_ONLY` — public-safe identity/integrity witness without private storage coordinates;
- `EXECUTABLE_REPRODUCTION` — code + public-safe fixture/parameters/tests reproduce a declared result class.

See [`docs/SURFACE_ARCHITECTURE.md`](docs/SURFACE_ARCHITECTURE.md).

## BW ↔ GitHub integrity

Material public artifacts are expected to be mutually traceable with BW:

```text
GITHUB_ARTIFACT -> BW_INGESTION_OR_EXPLICIT_NOT_INGESTED
BW_PUBLIC_ARTIFACT -> GITHUB_COMMIT_OR_EXPLICIT_PUBLICATION_STATE
```

GitHub provides immutable public-safe custody and reproducibility; BW remains the private event/currentness ledger. Cross-surface projections live under `manifests/cross-surface/`.

## Claim boundary

Do not infer unpublished scientific currentness from repository contents. Code presence, issue state, merge state and green CI are not scientific-status signals.

```text
GITHUB_COMMIT != BW_EVENT
GITHUB_ISSUE != SCIENTIFIC_ADOPTION
GITHUB_MERGE != EXEC_SIGN
CI_PASS != SCIENTIFIC_VALIDATION
GITHUB_POINTER != DELIVERY
CURRENT_SUMMARY != SOURCE_OF_TRUTH
```

## Change path

```text
issue or bounded task → branch → draft pull request → checks/review → explicit disposition → merge
```

## Public/private safety

This repository is public. Never commit credentials, personal/private data, restricted source material, unpublished private cross-cell packets or unpublished scientific conclusions merely to improve discoverability or work around a connector failure.

`PUBLIC_FALLBACK != PRIVATE_DATA_BYPASS`.

Public executable work currently includes bounded infrastructure such as the TabPFN runtime gate under `runtime/tabpfn/`; its presence does not imply scientific validation.
