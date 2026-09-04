# NASH/IW system-contract regressions

This repository is public. The system-contract surface here is intentionally small and sanitized.

## Repository boundary

The repository may contain reusable code, generic validators, synthetic fixtures, manifests, and public reproducibility packages.

It must not be treated as the private IW commons or as a scientific ledger.

`GIT_COMMIT != BW_EVENT != SCIENTIFIC_ADOPTION`

`PR_MERGED != SCIENTIFICALLY_ACCEPTED`

Do not place private BW extracts, Living Theory content, unpublished scientific artifacts, succession packets, private source full text, hidden accession material, credentials, or internal deliberation in this public repository.

## Thin execution contract

The validator in `nash_iw.system_contracts` checks a small reproducibility contract containing:

- execution identity and requesting cell;
- scientific request reference;
- code commit SHA and entry point;
- environment and exact command;
- input/output references with hashes;
- regression command/result;
- runtime warnings;
- claim ceiling;
- return path and status.

A structurally valid execution contract does **not** establish scientific truth, currentness, novelty, CANON, EXEC_SIGN, or adoption.

## Regression semantic classes

Every nontrivial regression should declare one of:

- `HARD_INVARIANT`
- `CURRENT_POLICY`
- `HISTORICAL_BUG_FIXTURE`
- `SCIENTIFIC_FIXTURE`
- `EXPERIMENTAL_CONTRACT`

Non-hard tests should carry a review or sunset trigger. This prevents temporary procedures or historical bug fixes from silently fossilizing into shadow governance.

## Initial synthetic regression surface

The first suite covers only previously declared system distinctions:

- `CURRENT != NEWEST`;
- `UNKNOWN != FALSE`;
- monitor/review signals do not mutate scientific or authority state;
- transferred source witness preserves the original witness actor and does not self-attribute direct inspection;
- execution returns carry an explicit claim ceiling;
- versioned/non-hard regression semantics require review/sunset metadata.

These are representation/system-contract checks, not scientific theorem tests.

## Single-file first

Scientific handoffs should remain single-file-first where that is the more robust execution form. Package/framework extraction should follow measured reuse, not software elegance alone.
