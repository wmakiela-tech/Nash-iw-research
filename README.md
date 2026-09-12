# NASH–IW Research Infrastructure

Public, versioned infrastructure, archive and reproducibility surface for NASH/IW.

GitHub has several roles in the project at once: executable/reproducibility surface, public-safe archive/index, durable asynchronous bridge to external participants such as Grok, and a public orientation layer pointing authorized researchers toward the private current-state resolvers. It is not the sole source of scientific truth.

## Start here

Active NASH/IW researchers should begin with:

1. [`docs/START_HERE_CURRENT.md`](docs/START_HERE_CURRENT.md) — resolves the current private project/scientific state without publishing it here.
2. [`docs/SURFACE_ARCHITECTURE.md`](docs/SURFACE_ARCHITECTURE.md) — explains how GitHub, Drive/BW, Slack and frozen stores divide responsibilities.
3. [`docs/RESEARCH_SCOPE.md`](docs/RESEARCH_SCOPE.md) — public-safe map of research domains and high-value research outputs.
4. [`docs/SOURCE_OF_TRUTH.md`](docs/SOURCE_OF_TRUTH.md) — explains which surface answers which kind of question.
5. [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md) — repository authority and claim boundaries.

## GitHub roles

### Public executable/reproducibility surface

Use for code, tests, schemas, small manifests, CI, public-safe fixtures and reproducible operator documentation.

### Public-safe archive and lineage

Use `archive-index/` and version history to preserve public artifacts, pointers, hashes, supersession and retrieval instructions without forcing large/private payloads into the repository.

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
