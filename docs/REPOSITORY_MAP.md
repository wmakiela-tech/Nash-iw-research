# Repository Map

**As of:** 2026-09-12

```text
.github/                 workflows, review templates and public-safe task/gate templates
archive-index/           public archive/index: artifacts, pointers, hashes, lineage and retrieval notes
docs/                    public-safe governance, routing/currentness guidance and operator documentation
fixtures/                public-safe synthetic/reproducibility fixtures
manifests/                small custody/reproduction manifests
runtime/                  bounded executable research/runtime surfaces
schemas/                  machine-readable schemas
scripts/                  command-line utilities
src/nash_iw/              reusable Python package
tests/                    unit/regression tests
```

## Researcher navigation

```text
README.md
  ↓
docs/START_HERE_CURRENT.md
  ├─> private current project/scientific resolvers (Drive/BW)
  ├─> docs/SURFACE_ARCHITECTURE.md
  ├─> docs/RESEARCH_SCOPE.md
  ├─> docs/SOURCE_OF_TRUTH.md
  ├─> docs/GOVERNANCE.md
  └─> docs/NAMING_AND_INDEXING.md
```

## Functional navigation

### Need current unpublished scientific/project state?

Use the private BW/source chain. GitHub may point to the resolver but does not replicate private currentness by default.

### Need code, tests or a reproducible public fixture?

Use `runtime/`, `src/`, `tests/`, `schemas/`, `manifests/` and CI.

### Need historical/public archive or integrity lineage?

Use `archive-index/` and Git version history. Select an explicit archive mode:

`PUBLIC_ARTIFACT / POINTER_ONLY / HASH_ONLY / EXECUTABLE_REPRODUCTION`.

Machine-readable archive entries use `archive-index/archive-entry.schema.json`; canonical filenames and stable IDs follow `docs/NAMING_AND_INDEXING.md`.

### Need an asynchronous channel to Grok or another external participant?

Use a public-safe issue/PR/file with a self-contained task capsule. Do not assume private Drive/Slack access. External return remains evidence/transport until normal project qualification.

### Need fast model↔model correction?

Use a bounded low-friction dialogue surface (currently often Slack) and persist only a terminal qualified state when material. See `docs/SURFACE_ARCHITECTURE.md`.

## Important boundaries

The navigation documents are deliberately thin enough to remain public. They may identify functions and source families without publishing private packets.

```text
PUBLIC_GITHUB != PRIVATE_IW_COMMONS
GITHUB_COMMIT != BW_EVENT
GITHUB_ISSUE != SCIENTIFIC_ADOPTION
DOCUMENT_MATURITY != CLAIM_MATURITY
```

```yaml
DOCUMENT_MATURITY: CURRENT_OPERATOR_GUIDANCE
CLAIM_MATURITY: NON_SCIENTIFIC_INFRASTRUCTURE
CANON_EFFECT: NONE
EXEC_SIGN: NONE
PUBLIC_REPOSITORY: true
```
