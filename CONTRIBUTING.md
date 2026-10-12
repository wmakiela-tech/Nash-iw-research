# Contributing

Before research-related or claim-heavy work, read [`docs/START_HERE_CURRENT.md`](docs/START_HERE_CURRENT.md), follow [`docs/WORK_AND_REPRODUCIBILITY_PROTOCOL.md`](docs/WORK_AND_REPRODUCIBILITY_PROTOCOL.md), resolve current BW/source state, and follow [`docs/REPOSITORY_STRUCTURE.md`](docs/REPOSITORY_STRUCTURE.md) plus [`docs/STORAGE_AND_SYNC_POLICY.md`](docs/STORAGE_AND_SYNC_POLICY.md).

GitHub code or an old report is not sufficient evidence of scientific currentness.

## Working sequence

1. Resolve current role/function, BW currentness and applicable STOP/HOLD.
2. Reuse the stable `artifact_id`; a transport copy is not a new artifact.
3. Classify exposure: `PUBLIC`, `PRIVATE`, or `RESTRICTED`.
4. Choose the canonical repository class.
5. Make the smallest coherent change.
6. Add/update tests when executable behavior changes.
7. Persist material work and read it back.
8. Complete the BW↔GitHub handshake for material public artifacts.
9. Record provenance, claim ceiling and supersession.
10. Use review/PR when the change needs independent repository review.

## Canonical placement

- current operator/system contract → `docs/`
- public-safe scientific body → `research/<lineage>/<YYYY-MM-DD>/`
- compact pointer/hash/legacy record → `archive-index/<YYYY>/<lineage>/`
- public-safe succession pointer → `succession/<YYYY>/<lineage>/`
- executable code → `runtime/` or `src/`, with tests/fixtures/manifests
- cross-surface projection → `manifests/cross-surface/`

Do not create new ad-hoc top-level folders.

Historical paths are provenance. Do not mass-rename them solely to fit the current layout.

## BW handshake

A material GitHub commit is not complete project custody by itself.

```text
COMMIT -> BW INGESTION/STATUS -> CROSS-SURFACE READBACK
```

If BW cannot be updated immediately, label the state `GITHUB_PENDING_BW_INGEST`; do not claim `SYNCED`.

For a public-safe BW/Drive artifact that lacks GitHub custody, use `BW_PENDING_GITHUB_PUBLICATION` until a canonical immutable GitHub commit exists.

## Required provenance for material public artifacts

Include or make recoverable:
- artifact/contribution ID;
- source revision;
- origin cell/lineage;
- BW ingestion event when known;
- epistemic status / claim ceiling;
- archive mode;
- `derived_from` / `supersedes` where applicable;
- canonical GitHub path + immutable commit after publication.

## Pull-request minimum

State purpose, changed files, source artifacts or hashes, tests, resource cost, claim boundary, current BW relation, exact next step and Moderator action only where genuinely required.

## Reproducibility minimum

A load-bearing computational or empirical result must include a validated `schemas/research-reproduction-manifest.schema.json` instance, exact code/environment/commands/inputs/outputs/checksums, controls, tolerances and an honest reproduction state. A load-bearing literature result must preserve exact queries, databases/tools, filters, screening logic, source locators, retrieval depth/limits and a checksummed bibliography export using the current literature template.

A narrative claim without its load-bearing bundle is `EVIDENCE_INCOMPLETE_FOR_REPRODUCTION`; this is not automatically a scientific-failure verdict.

## Public repository boundary

This repository is public.

Never commit credentials, tokens, passwords, private keys, personal/family data, restricted source material, private cross-cell packets, private Drive/Slack coordinates or unapproved unpublished scientific conclusions.

Private/restricted artifacts use `POINTER_ONLY`, `HASH_ONLY`, or `PRIVATE_ONLY`. Public-safe pointers must use artifact/BW identity rather than exposing private provider coordinates.

Do not rewrite frozen checkpoints. Use a new version, superseding artifact or authorized append-only addendum.

```text
GITHUB_COMMIT != BW_EVENT
MIRROR_SYNC != SCIENTIFIC_VALIDATION
PUBLIC_GITHUB != PRIVATE_IW_COMMONS
```
