# NASH/IW — Cell Work, Artifact and Reproducibility Protocol

```yaml
artifact_id: IW_OW_CELL_WORK_ARTIFACT_AND_REPRODUCIBILITY_PROTOCOL_001_20260914
title: NASH/IW Cell Work, Artifact and Reproducibility Protocol
created_at: 2026-09-14
as_of: 2026-09-14
origin_cell: IW_ORGANISATION_WORK_01 / OW
document_type: PROTOCOL
applicability: PROJECT_GUIDANCE_ACTIVE / FORWARD_ONLY_PROJECT_DEFAULT
authority_basis: Human Moderator direct instruction, 2026-09-14
operational_owner: OW
scientific_interface: SW
shared_publication_interface: SCOPE
exposure: PUBLIC
status: CURRENT
stale_if:
  - a later explicitly applicable protocol supersedes this artifact_id
  - SYSTEM CORE changes any protected boundary used here
  - the designated primary GitHub path no longer resolves to this artifact_id
supersedes:
  - older forward naming default in IW_SYSTEM_CORE_v0_1_20260822 section 6 only
does_not_supersede:
  - protected boundaries or authority rules in SYSTEM CORE
  - BW or LT scientific currentness
  - domain-specific scientific methods
guards: [NO_CANON, NO_EXEC_SIGN, NO_SCIENTIFIC_ADJUDICATION, SCIENCE_FIRST]
```

This is the single current operational profile for normal cell rotations, material work returns, artifact persistence, public-safe GitHub fallback, naming, and reproducibility. The templates and schema linked at the end are instruments of this protocol, not competing procedures.

## 1. Controlling distinctions

```text
INBOUND_TASK_PRIORITY != INBOUND_TASK_MONOPOLY
NO_INBOUND != NO_FUNCTIONAL_WORK
ARTIFACT_CREATED != CONTENT_PERSISTED != READBACK_VERIFIED
STORAGE != DELIVERY != RECEIPT != ACCEPTANCE != SCIENTIFIC_VALIDATION
CHANNEL_CHANGE != NEW_TASK
GITHUB_FALLBACK != PRIVATE_DATA_BYPASS
RESULT_REPORTED != RESULT_REGENERABLE
SEARCH_NO_MATCH != NOVELTY
```

This protocol standardizes the shared boundary. Cells may retain different internal workflows if their returns translate back to this boundary and preserve protected exposure, currentness, provenance, and authority distinctions.

## 2. Required rotation contract

Every material rotation follows this bounded sequence:

1. **Refresh controls and currentness.** Read the relevant global control surface, direct inbound delta, current task state, and applicable currentness sources. A read error is `UNKNOWN`, not an empty delta. Protected first-pass routing remains an exception to broad pre-freeze reads.
2. **Resolve current obligations.** Identify current inbound tasks, wait gates, holds, supersessions, and accepted unfinished work. Handle legal, role-appropriate inbound work first.
3. **Perform function-derived work.** If useful budget remains, select one bounded high-value action inherent in the cell's assigned function. A cell must not end merely because no new message arrived. It may return `NO_MATERIAL_FUNCTIONAL_ACTION` only after recording the function scan and the reason no valuable legal action existed.
4. **Classify the result.** Use `RESULT`, `NEGATIVE_KNOWLEDGE`, `BLOCKER`, `ANTI_REDISCOVERY_CORRECTION`, `CURRENTNESS_CORRECTION`, `PENDING_REVIEW`, or `NO_MATERIAL_DELTA`. State the claim ceiling and unresolved dependencies.
5. **Persist material work.** Store a material body or checkpoint on a legal durable surface. Record artifact identity, content identity or checksum, primary location, custody state, and readback state. Transient tool calls and cheap scratch work need no project artifact.
6. **Route actionably.** If another participant must act, send a bounded message with the same `task_id`, exact recipient, artifact pointer or inline legal minimum, requested action, return path, and delivery state. Use a legal fallback when the preferred channel fails.
7. **Recheck before return.** For long or material turns, refresh relevant interrupts/currentness once more before a load-bearing return. Do not silently repeat already committed work.
8. **Return a stable stop.** State what changed, what did not change, where the evidence is, whether readback and delivery occurred, and the next single step or legal hold.

Legal reasons not to perform additional function-derived work include: inbound work exhausted the useful budget; an explicit scarce-resource mode; protected exposure; a current stop/HOLD; a conflicting WIP cap; or no valuable role-consistent action. `FUNCTION_DERIVED_WORK != BUSYWORK` and does not authorize a new campaign or role expansion.

## 3. Function scan

The cell uses its current role/founding/succession profile as the source of function. Examples are illustrative:

| Function family | Typical bounded function-derived action |
| --- | --- |
| SW / scientific coordination | select or refine one typed scientific dependency; package a reproducible test; route a result for appropriate review without adjudicating by transport |
| Scientific generator / integrator | derive, calculate, formalize, build a counterexample, run a discriminating test, or integrate a source-native object |
| Referee / adversarial review | attack assumptions, types, provenance, controls, reproduction, or claim ceiling of a current candidate |
| DAX / distant-field exploration | test a bounded orthogonal model or donor mechanism while preserving object-identity guards |
| M / literature and prior art | execute a reproducible targeted search, verify primary sources, record absorption/no-match/transfer limits, and preserve material side harvest separately |
| KN / knowledge currentness | resolve currentness, provenance, supersession, custody, discoverability, or negative-knowledge retention |
| MT / Living Theory | maintain authored synthesis and exact head/materialization distinctions without inventing a revision |
| OW / system organization | remove one routing, artifact, naming, reproducibility, tooling, dependency, or multi-surface integrity blocker |
| GOV / EAI / EV / IDEA | perform one role-native governance, interface, evolutionary, or ideation pressure action without taking scientific authority |
| SCOPE | integrate publication structure, audience language, field boundaries, and accepted scientific modules without replacing source ownership |

## 4. Materiality and persistence states

Create a durable artifact when loss would cause material rework, erase evidence or negative knowledge, break provenance, impair review/reproduction, or misstate currentness. Otherwise keep the step transient.

Use explicit states:

```text
LOCAL_ONLY
WRITE_ATTEMPTED
STORED
READBACK_VERIFIED
CUSTODY_PENDING
DELIVERY_BLOCKED
DELIVERED
RECEIVED
ACCEPTED
SUPERSEDED
```

- A file shell, returned ID, or local hash does not prove content persistence.
- After a write, read back the stored content or checksum when the result is material.
- On a pre-mutation block, do not claim storage and do not blind-retry the same payload. Preserve a local/checksummed recovery copy when legal and switch to a legal surface or mark `CUSTODY_PENDING`.
- One logical artifact has one designated primary location. A mirror retains the same `artifact_id`; a byte-identical mirror retains the same checksum and is labeled `MIRROR`, not a second primary.
- A new material claim, scope, task, or decision receives a new artifact ID and an explicit lineage edge. A formatting repair may keep the same artifact ID with a new revision/commit.

## 5. Channel selection and fallback

| Need | Preferred surface | Legal fallback | Never infer |
| --- | --- | --- | --- |
| Fast private routing/interrupt | Slack route-tag or authorized cell surface | accessible private Drive packet or Moderator/intermediary relay | posted = received |
| Private material body/currentness | role-appropriate private Drive/BW/LT surface | frozen local recovery bundle pending healthy custody; authorized private relay | custody failure = scientific failure |
| Public-safe async task or return | GitHub Issue/PR with stable task ID | Slack or relay carrying the same public-safe packet | GitHub state = BW/LT state |
| Public code/data/schema/reproduction | GitHub commit/PR/release/archive entry | verified public bundle with checksum and GitHub reintegration pending | hash = delivery |
| Protected/blind first pass | exact protected input route | authorized protected inbound/relay | shared channel = protected boundary |

Each material rotation records one GitHub disposition:

```text
GITHUB_CHECK = CHECKED_NO_RELEVANT_DELTA
             | USED_AS_PUBLIC_SAFE_PRIMARY
             | USED_AS_PUBLIC_SAFE_FALLBACK
             | NOT_APPLICABLE_PRIVATE_OR_PROTECTED
             | ACCESS_BLOCKED
```

This is a small boundary field, not a demand to browse the entire repository. Check the assigned Issue/PR, active public-safe task ID, or current operator entry point when relevant. If Slack or Drive delivery fails and the payload is public-safe, use or prepare GitHub fallback with the same `task_id`, `artifact_id`, privacy class, and return path. Private conclusions, unpublished packets, credentials, personal data, private storage coordinates, and exposure-restricted material must not be moved to public GitHub as a workaround.

## 6. Canonical naming and metadata

For every new material artifact use:

```text
IW_<CELL-OR-LINEAGE>_<OBJECT>_<DOCUMENT-TYPE>_<NNN>_<YYYYMMDD>
```

The filename is the identifier plus a lowercase extension. Do not add upload-order prefixes. Do not use `final`, `latest`, `new`, `fixed`, or a bare `v2` as identity. Historical artifacts are not mass-renamed. A stable domain convention may continue only as an explicit compatible deviation with unambiguous identity and searchability.

Minimum metadata for a material artifact:

```yaml
artifact_id: IW_...
title: human-readable title
revision: immutable content revision, commit, or provider revision
created_at: ISO-8601 timestamp
as_of: source/currentness basis
origin_cell: active cell or lineage
function: role-derived purpose
document_type: controlled type
task_id: stable cross-surface task identifier or NOT_APPLICABLE
exposure: PUBLIC | PRIVATE | RESTRICTED
status: DRAFT | CURRENT | FROZEN | HOLD | SUPERSEDED | RETRACTED
primary_location: durable pointer or CUSTODY_PENDING
content_sha256: checksum or NOT_AVAILABLE with reason
provenance: exact sources, inputs, or parent artifacts
derived_from: []
supersedes: []
stale_if: invalidation condition
acceptance_owner: cell/role able to accept this work
return_path: target for requested follow-up
```

Forward-only controlled document types include `PROTOCOL`, `TASK`, `PACKET`, `RETURN`, `REVIEW`, `CHECKPOINT`, `FREEZE`, `DECISION`, `REPORT`, `MANIFEST`, `REPRO_MANIFEST`, `LITERATURE_RECORD`, `DATA`, `RUNTIME`, `SCHEMA`, `INDEX`, `POINTER`, and `SUCCESSION`.

## 7. Common material return

Every material return must expose, inline or through the common template:

```yaml
from_cell:
to_cell_or_route:
task_id:
return_id:
artifact_id:
function_action:
currentness_basis:
result_class:
status: COMPLETE | PARTIAL | BLOCKED | HOLD | FAILED_NO_STATE_CHANGE
material_delta:
claim_ceiling_or_scope:
artifact_pointer:
content_sha256:
persistence_state:
readback_state:
delivery_state:
github_check:
dependencies_or_blockers: []
next_single_step:
return_path:
```

If the full body is durable and accessible, the transport message stays short. If access is unknown, include the minimum legal context needed to act. `RETURN_DRAFTED` and `RETURN_DELIVERED` remain different states.

## 8. Computational and empirical reproducibility

A load-bearing computational or empirical result is publication-ready only when an independent capable participant can regenerate or decisively diagnose it from the bundle. The minimum bundle contains:

1. exact research question, object, claim, scope, and claim ceiling;
2. code identity: repository/path, commit or immutable content hash, and license when external;
3. environment identity: OS/architecture where material, language/runtime and package lock or exact versions;
4. exact entry point and command sequence from a clean checkout or declared starting state;
5. all load-bearing inputs with source, schema, units/conventions, checksums, and exposure class;
6. parameters, seeds, masks, tolerances, stopping rules, numerical precision, and hardware dependence where material;
7. raw outputs and derived outputs with an explicit transformation chain;
8. expected key values, tolerances, plots/tables, and pass/fail interpretation;
9. negative controls, sensitivity checks, known failures, warnings, and limitations;
10. provenance links between narrative, code, data, manifest, tests, and runtime output;
11. reproduction status: `NOT_RUN`, `AUTHOR_REPRODUCED`, `INDEPENDENTLY_REPRODUCED`, `PARTIAL`, or `FAILED_WITH_DIAGNOSTIC`;
12. exact discrepancies and platform deviations; failure remains evidence and must not be cosmetically removed.

Use the reproduction manifest template and validate it against `schemas/research-reproduction-manifest.schema.json`. A narrative result without the load-bearing bundle is `EVIDENCE_INCOMPLETE_FOR_REPRODUCTION`, not necessarily scientifically false.

## 9. Literature-search reproducibility

A load-bearing literature result must allow another scout to rerun the search and audit theorem transfer. Record:

1. frozen research question and object/class vocabulary before the search;
2. database, index, browser, API, local library, or model/tool used, including access date and version when material;
3. exact query strings in execution order, with field syntax and language variants;
4. date ranges, subject filters, languages, document types, citation thresholds, and other constraints;
5. inclusion, exclusion, deduplication, stopping, and primary-source verification rules;
6. result counts where available and a raw export or stable list of returned identifiers;
7. exact identifiers and locators: DOI, arXiv, ISBN, patent, standard, repository, theorem/section/equation/page;
8. retrieval status for each load-bearing source: full text, abstract only, snippet/search summary, inaccessible, or not independently opened;
9. distinction between source text, scout interpretation, IW application, and unresolved transfer condition;
10. object/category/hypothesis match before claiming absorption, contradiction, or theorem import;
11. negative-search semantics and limitations: `SEARCH_NO_MATCH != ESTABLISHED_ABSENCE != NOVELTY`;
12. citation chaining, author/open-problem/limitation harvest, and material side harvest as separate records;
13. export format for the bibliography (`BibTeX`, `RIS`, `CSL-JSON`, or structured CSV) plus file checksum;
14. currentness/update trigger for live, disputed, or preprint-dependent claims.

Use the literature-search record template. A source list without reproducible queries and inclusion logic is a bibliography, not a reproducible literature result.

## 10. Verification and acceptance

Before calling a material artifact complete, verify:

- the stored object contains the intended non-empty body;
- the `artifact_id`, filename, metadata, and message pointer agree;
- checksum/revision and primary/mirror roles are explicit;
- all linked load-bearing files resolve for the intended recipient or have an honest access state;
- reproduction instructions begin from a declared clean state and include expected outputs/tolerances;
- literature records preserve exact queries and retrieval limits;
- currentness was refreshed and `stale_if` is meaningful;
- no private or protected content was exposed through a public fallback;
- the return states delivery, receipt, and acceptance separately;
- the next action has an owner/route, or the result closes without inventing work.

Acceptance outcomes are `ACCEPT`, `ACCEPT_WITH_LIMITS`, `PARTIAL`, `HOLD`, `REJECT_WITH_REASON`, or `BLOCKED`. A schema/format PASS is not scientific validation.

## 11. Lightweight compliance and repair

- This protocol applies forward-only to new material rotations and artifacts after its adoption. It does not invalidate historical evidence solely for old names or formats.
- Existing active artifacts are upgraded only when they become load-bearing for a new publication, reproduction, review, currentness change, or cross-cell handoff.
- A local deviation is legal when it preserves the shared boundary and is declared where collaboration is affected.
- Repeated purely reactive turns, repeated unverified writes, missing reproducibility bundles, or skipped legal fallback are material conformance issues; one harmless omission is repaired proportionally.
- No per-turn quota, utilization score, acknowledgment ritual, universal duplicate storage, new global scheduler, or pre-work approval gate is created.

## 12. Current source chain

This profile operationalizes, without replacing protected boundaries in:

- private `IW_SYSTEM_CORE_v0_1_20260822`, especially provenance, communication, turn-start, function-derived work, and small-step persistence;
- private `IW_SYSTEM_COMMUNICATION_PLAYBOOK_001_20260823`;
- private `IW_GOVCELL_20260816_INDEX_IW_CURRENT_APPLICABLE_DOCUMENTS_001`;
- public `docs/SURFACE_ARCHITECTURE.md`;
- public `docs/NAMING_AND_INDEXING.md`;
- public `docs/SOURCE_OF_TRUTH.md`.

The private current-applicable index remains the resolver for private project applicability and must receive an append-only pointer to this artifact. GitHub remains the primary public-safe copy and revision history for this protocol. Neither surface creates scientific truth.

## 13. Controlled instruments

- Common return: `templates/IW_MATERIAL_WORK_RETURN_TEMPLATE.md`
- Computational/empirical manifest: `templates/IW_RESEARCH_REPRODUCTION_MANIFEST_TEMPLATE.json`
- Literature record: `templates/IW_LITERATURE_SEARCH_RECORD_TEMPLATE.md`
- Machine-readable validation: `schemas/research-reproduction-manifest.schema.json`
- Public-safe fallback form: GitHub Issue template `IW material work return`

```text
PROTOCOL_CONFORMANCE != SCIENTIFIC_CORRECTNESS
REPRODUCTION_FAILURE_MUST_REMAIN_REPORTABLE
METHOD_MUST_BE_ALLOWED_TO_FAIL
```
