# NASH/IW — Source of Truth and Currentness

**As of:** 2026-08-25

NASH/IW deliberately uses different storage surfaces for different information functions. No single repository is the source of truth for everything.

## Source roles

### GitHub — public executable/infrastructure surface

Use for:

- code;
- tests;
- schemas;
- small manifests;
- CI;
- public-safe operator documentation;
- issues and pull requests.

GitHub does **not** automatically carry the current unpublished scientific state.

### Private Google Drive / BW — shared current project/scientific state

Use for:

- current scientific/project knowledge views;
- source-linked qualification/review packets;
- lifecycle, supersession and open-frontier state;
- cross-cell research artifacts;
- current system/governance guidance.

Primary current scientific/project resolver (find by artifact ID/name in the private project Drive/current index):

`IW_KCELL_BW_V0_2_OPERATING_LAYER_001_20260824`

### File Library / exact frozen bundles

Use for exact historical reports, CSV/data payloads, frozen packages and artifacts that are not naturally maintained as live GitHub content.

## Precedence by question

| Question | Preferred evidence |
|---|---|
| What does the current project believe / keep open? | current BW/private qualified state |
| What exactly did a paper/reviewer/result claim? | primary source/review artifact |
| What did code actually do? | exact code + parameters + data/manifest + runtime output |
| Which project rule currently applies? | current System Core / applicable-document index |
| Is a GitHub implementation reproducible? | repository commit + CI/tests + manifest/runtime evidence |
| Is something scientifically true? | not decided by storage location, CI, consensus or GitHub merge |

## Required distinctions

```text
SOURCE != ASSERTION != EVIDENCE != SYNTHESIS
STORAGE != DELIVERY != RECEIPT != ACCEPTANCE
CI_PASS != SCIENTIFIC_VALIDATION
GITHUB_MERGE != EXEC_SIGN
CURRENT_POINTER != CANON
NO_SEARCH_HIT != NOVELTY
```

## Staleness rule

Every current-state summary should expose an `as_of` date or current build/event pointer. If a summary conflicts with a newer qualified source or BW event, the summary becomes stale; do not silently reinterpret it as current.

## Public/private safety

This repository is public. Do not copy unpublished scientific conclusions, private cross-cell packets or provider-specific private file IDs here merely to improve discoverability. Public GitHub should point authorized NASH/IW researchers toward the private current-state resolver and keep executable/public-safe material reproducible.

## Minimal research handoff expectation

A material result should make it possible to recover:

- the artifact/source identity;
- scope and assumptions;
- epistemic status;
- relation to prior state;
- negative knowledge or unresolved conflict where relevant;
- exact runtime/source pointers for load-bearing steps.

This is a semantic expectation, not a requirement to create a large form for every exploratory action.
