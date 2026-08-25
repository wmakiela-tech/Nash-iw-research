# NASH–IW Research Infrastructure

Public, versioned infrastructure and reproducibility surface for NASH/IW.

## Start here

Active NASH/IW researchers should begin with:

1. [`docs/START_HERE_CURRENT.md`](docs/START_HERE_CURRENT.md) — resolves the current private project/scientific state without publishing it here.
2. [`docs/RESEARCH_SCOPE.md`](docs/RESEARCH_SCOPE.md) — public-safe map of live research domains and high-value research outputs.
3. [`docs/SOURCE_OF_TRUTH.md`](docs/SOURCE_OF_TRUTH.md) — explains which storage surface answers which kind of question.
4. [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md) — repository authority and claim boundaries.

## Storage roles

- **GitHub (public):** code, tests, schemas, small manifests, issues, pull requests, CI and public-safe operator documentation.
- **Private Google Drive / BW:** curated current scientific/project state, cross-cell research packets, lifecycle/currentness and private source-linked reviews.
- **File Library / frozen bundles:** exact historical reports, payloads, data files and frozen artifacts where appropriate.

Do not infer unpublished scientific currentness from repository contents. Code presence, merge state and green CI are not scientific-status signals.

## Claim boundary

Green CI means only that declared automated checks passed. It does not confer `EXEC_SIGN`, canon merge, scientific truth or claim upgrade.

```text
GITHUB_MERGE != EXEC_SIGN
CI_PASS != SCIENTIFIC_VALIDATION
GITHUB_POINTER != DELIVERY
CURRENT_SUMMARY != SOURCE_OF_TRUTH
```

## Change path

```text
branch → draft pull request → checks/review → explicit disposition → merge
```

## Public/private safety

This repository is public. Never commit credentials, personal/private data, unpublished NASH/IW scientific conclusions or private cross-cell packets without the appropriate publication gate.

The repository bootstrap itself contains no NCDG runtime and no `adjusted_transport` implementation. Public executable work currently includes bounded infrastructure such as the TabPFN runtime gate under `runtime/tabpfn/`; its presence does not imply scientific validation.
