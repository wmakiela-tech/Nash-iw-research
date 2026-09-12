# Repository Governance

## Authority separation

- GitHub merge authority is not `EXEC_SIGN`.
- CI success is not a scientific claim upgrade.
- Documentation maturity and claim maturity are separate.
- Frozen artifacts are immutable within their declared lineage.

## Routing

Use GitHub for public-safe code, tests, schemas, manifests, CI, archive/index entries, reproducible artifacts, operator guidance and asynchronous external/cross-cell tasks. Use private Google Drive/BW for qualified private currentness and custody, Slack for rapid dispatch/dialogue, and File Library/frozen bundles for exact historical payloads.

GitHub may be the durable fallback when the payload is already public-safe. It must not be used to bypass private exposure controls. Issues and PRs carry transport/evidence; they do not confer scientific acceptance.

Structured databases are searchable projections or coordination queues. Their records must point back to stable artifact/task identities and controlling sources; database recency alone does not establish effective currentness.

## Intended workflow

```text
issue or gate → branch → draft PR → automated checks → review → disposition
```

For asynchronous work, bind every return to the exact task identity, its `currentness_basis`, `stale_if` rule and `acceptance_owner`. A late return from a cancelled or superseded task may remain useful evidence, but is not fulfillment of the current task.

Repository naming and archive rules are defined in [`NAMING_AND_INDEXING.md`](NAMING_AND_INDEXING.md) and [`../archive-index/README.md`](../archive-index/README.md).

Enable branch protection for `main` after the stable CI check name is known.
