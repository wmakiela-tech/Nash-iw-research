# Contributing

Before research-related or claim-heavy work, read [`docs/START_HERE_CURRENT.md`](docs/START_HERE_CURRENT.md), follow [`docs/WORK_AND_REPRODUCIBILITY_PROTOCOL.md`](docs/WORK_AND_REPRODUCIBILITY_PROTOCOL.md), and resolve the current private BW/source state. GitHub code or an old report is not sufficient evidence of scientific currentness.

1. Work on a focused branch.
2. Make the smallest coherent change.
3. Add or update tests where executable behavior changes.
4. Open a draft pull request.
5. Record provenance and claim boundaries.
6. Merge only after explicit review disposition.

## Pull-request minimum

State purpose, changed files, source artifacts or hashes, tests, resource cost, claim boundary, exact next step and Moderator action where one is genuinely required.

For scientific/research-related changes also state:

- relation to current BW/private state;
- whether the change is runtime, evidence, candidate claim, review or publication-ready material;
- any negative knowledge or prior-art relation that prevents rediscovery.

## Reproducibility minimum

A load-bearing computational or empirical result must include a validated `schemas/research-reproduction-manifest.schema.json` instance, exact code/environment/commands/inputs/outputs/checksums, controls, tolerances and an honest reproduction state. A load-bearing literature result must preserve exact queries, databases/tools, filters, screening logic, exact source locators, retrieval depth/limits and a checksummed bibliography export using the current literature template.

A narrative claim without its load-bearing bundle is `EVIDENCE_INCOMPLETE_FOR_REPRODUCTION`; this is not automatically a scientific-failure verdict.

## Public repository boundary

This repository is public.

Never commit API keys, tokens, passwords, private keys, personal/family data, restricted source material, private cross-cell packets or unapproved unpublished scientific conclusions.

Public-safe pointers to private current-state resolvers are allowed; pointer publication does not publish or validate the underlying scientific content.

Do not rewrite frozen checkpoints. Use a new version, superseding artifact or authorized append-only addendum.
