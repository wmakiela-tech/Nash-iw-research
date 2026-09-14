# IW Reproducible Literature Search Record

Controlling protocol: `IW_OW_CELL_WORK_ARTIFACT_AND_REPRODUCIBILITY_PROTOCOL_001_20260914`

```yaml
artifact_id: IW_<CELL-OR-LINEAGE>_<OBJECT>_LITERATURE_RECORD_<NNN>_<YYYYMMDD>
title:
origin_cell:
created_at:
as_of:
task_id:
exposure: PUBLIC | PRIVATE | RESTRICTED
status: DRAFT | CURRENT | FROZEN | HOLD | SUPERSEDED | RETRACTED
primary_location:
content_sha256:
research_question:
object_or_class:
claim_ceiling:
databases_and_tools: []
search_window:
languages: []
document_types: []
inclusion_rules: []
exclusion_rules: []
deduplication_rule:
stopping_rule:
primary_source_rule:
bibliography_export:
  format: BibTeX | RIS | CSL-JSON | CSV
  pointer:
  sha256:
currentness_trigger:
```

## 1. Frozen question and vocabulary

- Exact question:
- Source-native object/class:
- Synonyms and field-specific terms decided before searching:
- Known category-transfer risks:

## 2. Search execution log

Preserve queries in execution order. Add one row per executed query; do not normalize away failed or zero-result queries.

| Seq | Timestamp | Database/tool/version | Exact query | Filters | Result count | Export/raw result pointer | Notes |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| 001 | | | | | | | |

## 3. Screening and deduplication

- Inclusion rule applied:
- Exclusion rule applied:
- Deduplication key:
- Screening depth: title / abstract / full text / cited section:
- Stopping condition reached:
- Search limitations and inaccessible sources:

## 4. Load-bearing source ledger

| Source ID | DOI/arXiv/ISBN/patent/URL | Exact locator | Retrieval status | Primary/secondary | Source claim | Scout interpretation | IW application | Object/hypothesis match | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S001 | | | FULL_TEXT / ABSTRACT_ONLY / SNIPPET_ONLY / INACCESSIBLE / NOT_OPENED | | | | | | SUPPORT / TENSION / ABSORPTION / CONTRADICTION / ANALOGY_ONLY / NO_BRIDGE / UNRESOLVED |

## 5. Negative-search and transfer statement

- Search result: `MATCH_FOUND | NO_MATCH_IN_DECLARED_SEARCH | SEARCH_INCOMPLETE | CONTESTED_LITERATURE`.
- What the search does **not** establish:
- Category/object/hypothesis mismatch that blocks theorem transfer:
- Further query or primary-source verification needed:

`SEARCH_NO_MATCH != ESTABLISHED_ABSENCE != NOVELTY`  
`DONOR_THEOREM_AVAILABLE != PROJECT_OBJECT_CLASS_MEMBERSHIP`  
`MECHANISM_ANALOGY != OBJECT_IDENTITY`

## 6. Citation chaining and side harvest

Keep the frozen-question return separate from material side findings.

| Origin source/query | Exact pointer | Opening type | Material side finding | Why material | Proposed owner/question |
| --- | --- | --- | --- | --- | --- |
| | | OPEN_QUESTION / LOAD_BEARING_ASSUMPTION / METHOD_FAILURE / COMPETING_FORMULATION | | | |

## 7. Reproduction check

- Independent rerun status: `NOT_RUN | MATCHED | PARTIAL | FAILED_WITH_DIAGNOSTIC`.
- Query/result-count deviations:
- Bibliography export readback/checksum:
- Reviewer and date:

