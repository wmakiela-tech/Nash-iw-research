# NASH–IW Research and Knowledge Infrastructure

Public, versioned infrastructure for NASH/IW research, reproducibility and shared structured knowledge.

## Mission

NASH/IW is evolving from a multi-model research collaboration into an auditable knowledge enterprise. The long-term direction is an open, federated knowledge system for people and AI, beginning with a small, high-quality mathematical and mathematical-physics core.

The repository does **not** claim that the proposed Knowledge OS already exists or that its architecture is scientifically novel. Current architecture and seed documents are working candidates subject to literature review, testing and Moderator governance.

## Storage roles

- **GitHub:** public code, tests, schemas, manifests, architecture decisions, handovers, structured knowledge candidates, clearly labelled hypotheses and reproducibility support.
- **Google Drive — NASH–IW Shared Research Bridge:** curated reading order, current handover packages, cross-cell review packets and searchable operational continuity.
- **File Library / frozen artifacts:** exact reports, source payloads, CSV files, code, outputs and historical artifacts whose byte identity matters.

A Google Doc or narrative summary is not a substitute for an exact frozen source artifact. Hashes in handover manifests refer to the original files, not to converted Google Docs.

## Current architectural direction

The first product is intentionally small. The S0 seed must demonstrate four functions on real NASH/IW cases:

1. prevent internal rediscovery (`K5`);
2. compute the scope of invalidation after a source or operator changes;
3. retrieve a mechanism under different terminology;
4. distinguish homonyms, lineages and aggregation types.

The S0 design uses a progressive schema, a minimal `NODE`/`EDGE` model, a validator for syntactic constraints and a blind cold-start test. The larger Knowledge Fabric v3 remains a capability map, not the implementation scope of S0.

## Knowledge labels

Public material may include both confirmed knowledge and testable hypotheses, but each item must be clearly typed and traceable. Candidate public labels include:

- `CONFIRMED`
- `ACTIVE_HYPOTHESIS`
- `BOLD_CONJECTURE`
- `NEGATIVE_SPACE`
- `MAP_ERROR`
- `SUPERSEDED`

These labels do not replace domain-specific evidence, validation facts, source provenance or Moderator decisions.

## Governance and change path

```text
branch → draft pull request → review → explicit disposition → merge
```

Operational changes are disclosed under the project’s working VETO procedure. Core changes — including genome, `EXEC_SIGN`, success taxonomy, anti-self-sealing safeguards and equivalent constitutional rules — require explicit prior Moderator approval.

Material outputs should carry a `RULE_STAMP` identifying the governing document, local mutations and date.

## Claim boundary

Green CI, a valid schema, a merged pull request or a successful cold-start test means only that the declared checks passed in their stated scope. It does **not** confer:

- `EXEC_SIGN`;
- scientific truth;
- physical interpretation;
- canon merge beyond the explicit repository change;
- claim upgrade;
- novelty.

## Literature before design

Material architecture decisions must begin with a dated `LITERATURE_GATE` covering peer-reviewed literature, standards, existing systems, reusable components, known failures, build-vs-adopt reasoning and the actual IW-specific delta.

> No design from model memory alone.

## Start here

- `docs/handover/IW_NEW_ARIS_THREAD_READ_FIRST_v1_20260728.md`
- `docs/handover/IW_NEW_ARIS_THREAD_OPENING_MASTER_REPORT_v1_20260728.md`
- `docs/governance/IW_MODERATOR_VERBATIM_DECISION_AND_VISION_LEDGER_v1_20260728.md`
- `docs/architecture/IW_KNOWLEDGE_FABRIC_SEED_v0_2_SP_ARIS_SYNTHESIS_20260727.md`
- `docs/strategy/IW_ENTERPRISE_EVOLUTION_VISION_MISSION_AND_LITERATURE_GATE_REPOSITORY_SUMMARY_v0_1_20260728.md`

The bootstrap repository still contains no NCDG runtime and no `adjusted_transport` implementation.
