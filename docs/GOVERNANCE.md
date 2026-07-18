# Repository Governance

## Authority separation

- GitHub merge authority is not `EXEC_SIGN`.
- CI success is not a scientific claim upgrade.
- Documentation maturity and claim maturity are separate.
- Frozen artifacts are immutable within their declared lineage.

## Routing

Use GitHub for executable code, tests, schemas, small manifests, issues and CI. Use Google Drive for curated cross-cell packets. Use File Library for exact frozen reports and large historical artifacts.

## Intended workflow

```text
issue or gate → branch → draft PR → automated checks → review → disposition
```

Enable branch protection for `main` after the stable CI check name is known.
