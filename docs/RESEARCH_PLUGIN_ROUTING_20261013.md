# NASH/IW — Research Plugin Routing and Evidence Interface (13 October 2026)

```yaml
artifact_id: IW_KN10_RESEARCH_PLUGIN_ROUTING_ADVISORY_001_20261013
origin_cell: KN10 / KCELL
status: ADVISORY_CURRENT_CAPABILITY_REVIEW
exposure: PUBLIC
authority: TOOLING_GUIDANCE_ONLY
does_not_supersede:
  - docs/WORK_AND_REPRODUCIBILITY_PROTOCOL.md
  - docs/STORAGE_AND_SYNC_POLICY.md
  - project SYSTEM CORE, independent-review rules, BW or LT owners
guards: [NO_CANON, NO_EXEC_SIGN, NO_AUTOMATIC_NEW_FRONT, PRIVATE_SOURCE_PROTECTION]
```

## Purpose and boundary

This is an optional, role-sensitive connector playbook for IW cells, not a mandatory common workflow or a declaration that a plugin is available in every model/thread/account. Check access *in the invoking participant's own context* before making a plan dependent on it. Tool presence does not guarantee authorization, account entitlement, adequate text access, completeness, accuracy or scientific status.

Never confuse a tool answer, AI-written synthesis or search result with a theorem, independent replication, a licensed source, or a BW-accepted result. Keep distinct:

```
TOOL_AVAILABLE != TOOL_SUBSCRIPTION_ACTIVE != SOURCE_ACCESSED
SEARCH_HIT != PRIMARY_TEXT_READ != APPLICABILITY_VERIFIED
CITATION_COUNT != SUPPORT_FOR_SPECIFIC_CLAIM
NO_SEARCH_MATCH != NOVELTY
COMPUTATIONAL_CHECK != MATHEMATICAL_PROOF
SCIENTIFIC_ARTIFACT_PUBLISHED != BW_INGESTED != OWNER_ACCEPTED
```

## Role-sensitive tool routing

| Cell / function | Suitable tools | Exact purpose | Guard / alternative |
|---|---|---|---|
| PRF / deep foundational knowledge | Consensus, SciSpace, Sider Scholar/OpenAlex, Undermind; conditional Elicit | Build mature theorem-family maps, seminal works, monographs, current frontier, non-map and counterexample searches; inspect actual primary text | Source-native hypotheses; original version/DOI; no novelty from database silence; Elicit may be inaccessible by subscription |
| XH / external science harvest | Sider Scholar, Consensus, SciSpace, Undermind; web/arXiv primary endpoints | Harvest externally verifiable candidates and freeze citations/queries/exposure; compare overlapping databases | XH preserves source and independence provenance, does **not** decide scientific novelty or correctness |
| Geeky, DAX / branch exploration | Wolfram for exact symbolic or finite probes; primary articles discovered through Scholar/Consensus | Independent falsifiers, examples, narrow theorem donors, reproducible symbolic controls | Computer output is a diagnostic; preserve protected blind runs/NC independence; no automatic donor transfer |
| Rec / referee, NC / independent critic | Independent search paths + original primary text; Wolfram on bounded test cases; conditional Scite citation-context audit | Challenge assumptions, domains, source mapping and claimed prior-art originality | Avoid common-source evidence inflation; protected review must not receive prejudicial results before freeze; Scite may require paid access |
| SW, INT, Mech / scientific integration and mechanism | Undermind or targeted bibliographic discovery; Wolfram; cited source-native theory | Compare operator/projection, realization, hidden-return, transport and observable semantics; derive falsifiable bridge vs non-map | Explicit typed maps and counterexamples; mature-host absorption before a cross-field claim |
| MT, LT / Living Theory | Primary papers/monographs resolved through search tools; source-grounded comparison; exact computation as needed | Integrate *reviewed* results, negative knowledge and theorem chains in an authored synthesis | No automated LT revision/head update on plugin output; no replacement of owner/editorial decisions |
| SCOPE / scientific book and education | Primary bibliographies via Sider Scholar, Consensus, SciSpace; Zotero/BibTeX **only where locally available** | Traceable bibliography and chapter reading lists, checked DOI/versions, exact citations | Do not fabricate full-text inspection or treat Zotero-local skill as a shared remote connection |
| EAI / contemporary AI evolution | Acumen/Talarion as currentness question generator followed by dated source verification | Find late-breaking AI developments and test unusual technology hypotheses | Acumen is not a replacement for source verification; not suitable for pure timeless mathematics |
| KN, SYSS, OW / currentness, custody and infrastructure | Google Drive/Sheets, GitHub, Slack; optional established databases *only if adopted* | Maintain durable source/BW/commit/thread provenance, deduplicate exact identities, find missing body and write failures | Do not establish Notion/Airtable/Coda as a competing BW or automatic mirror; app connector safety protections are binding |

**Tool selection is deliberately plural.** Source independence, model independence and genuinely different mathematical methods matter more than tool count. The same article found in four catalogs is **one** source, not four confirmations.

## Evidence contract for a material research return

A literature-dependent scientific return should carry only the minimum needed for audit:

1. **Question and scope:** exact claim, type, model, host theory, assumptions, exclusions.
2. **Discovery:** tool/provider, query or author/DOI seed, filters, queried date, bounded search depth/coverage; report negative searches as searched subsets only.
3. **Primary evidence:** bibliographic title/author/year/DOI/version; opened paper/full text vs abstract/metadata; source-native passage, theorem or counterexample with section/page where possible; known correction/retraction.
4. **Scientific relation:** `EXACT_MATCH | MATURE_HOST_ABSORBS | CONDITIONAL_TRANSFER | ANALOGY_ONLY | NON_MAP | UNKNOWN`; show precise assumption mismatch, not just keywords or text similarity.
5. **Independent challenge:** a legal counterexample or specific nontrivial verification when a result depends on it; separate numerical witness from exact theorem.
6. **Custody and authority:** stable return ID, scientific claim ceiling, exposure class, public-safe full source GitHub commit where applicable, private original locator only in authorized BW/Drive, BW event if present, and explicit publication/ingestion/currentness states.

If no material research result is produced, do **not** create ceremonial database rows or extra copied documents for each search.

## Tool economics and bounded research strategy

- Start with **one** targeted database appropriate to the question. Add a **genuinely different** index/source only if the first is insufficient or an adversarial citation sweep is load-bearing.
- Prefer metadata/DOI discovery → source-native paper/monograph reading → mature-host subtraction → exact falsifier. Deep Undermind search is for complex multi-hop corpus gaps, not routine one-title lookup.
- Bibliographic extraction tools may have subscription/trial limits. If blocked, record `TOOL_UNAVAILABLE_SUBSCRIPTION` and continue only with permitted alternatives; do not reinterpret it as lack of science.
- Avoid making dependent steps contingent on unverified access, automatic broad "research reports", or a source-count quota.
- A first-pass independent model stays blind to other cells' prior responses until its own frozen return; the user or governing protocol may define exceptions.

## Cross-surface and privacy contract

Controlling project architecture is unchanged:
- **Public-safe scientific body:** GitHub `research/<lineage>/<date>/` with complete scientific contents and exact immutable commit.
- **Private/restricted origins and participant state:** restricted Drive (or authorized private frozen store), not indiscriminate GitHub copies.
- **BW:** controlling private ingestion/currentness/qualification/custody, not an automatically synchronized search cache.
- **Slack:** delivery and searchable original threads; read thread replies when required; message delivery is not durable independent science-body custody.
- **Notion/Airtable/Coda or individual bibliographic workspaces:** optional *auxiliary* surfaces only after a specific project use case has been accepted and a single custody/return path is stated.
- **External plugins:** no automatic export of private BW, reviews, unpublished manuscripts or personal workspace documents. Validate exposure and permission case by case.
- Provider/connector write denials remain denials: no proxy, alternate plugin or unrequested public posting used as a workaround.

## Bounded evaluation before expanding tool use

For one representative known mathematical result, perform an inexpensive cross-source test with:
- a targeted primary-source search;
- a distinct-index search / original-paper readback;
- a simple symbolic/numerical verification *only where mathematically appropriate*;
- classification of exact theorem, weaker analogy, or counterexample;
- DOI/author/edition and search provenance retained once.

Score **useful source-native corrections, exact source availability, counterexample discovery and reproducibility**, not raw counts of tools used, papers returned or tokens consumed. Stop the pilot if it adds only duplicate evidence or administrative load.

## Orientation for participants

This file is **guidance** supplied by KN10, not an owner/science/operational authority event. Participants should choose tools only when their original function and the current accepted task warrant them. Do not manufacture extra tasks or new research fronts because additional plugins exist. Report a material tooling failure once to the appropriate operational recipient, not as a recurring Moderator burden.

Authoritative project work and storage rules remain in the existing protocols; any promotion of this proposal to a required system-wide rule belongs to authorized project governance.
