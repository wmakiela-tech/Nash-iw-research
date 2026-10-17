# Literature execution record: relative entropy and geometry

artifact_id: IW_SW_RELATIVE_ENTROPY_LITERATURE_RECORD_001_20261017
origin_cell: IW_SCIENCE_WORK_01 / SW
exposure: PUBLIC
archive_mode: PUBLIC_ARTIFACT
bw_ingestion_event_id: NOT_YET_INGESTED
sync_state: GITHUB_PENDING_BW_INGEST
status: FROZEN / SELECTIVE_DEPENDENCY_SEARCH
claim_ceiling: PRIMARY_SOURCE_GENEALOGY_AND_SCOPE_AUDIT; NOT_EXHAUSTIVE; NO_NOVELTY

## Frozen question and vocabulary

Which contracts make relative entropy -> energy flux -> geometric response legal, and what survives deformation and AdS3 specialization? The pre-analysis map froze the area ansatz, all-null/localization conditions, state class, deformation domain and perturbation order as possible failure points. Vocabulary: Araki relative entropy, coherent Weyl/Virasoro states, modular flow, local Rindler horizons, Raychaudhuri, Rieffel deformation, Schwarzian, Bañados, RT, canonical energy, recovery.

Scope: literature through 2026-10-17; English primary papers and mathematical sources. Include proof-bearing hosts of the three identified papers and direct counterexample machinery. Exclude news, social media, citation-count arguments and unrelated search hits. Deduplicate by DOI/arXiv identity; record actual version separately. No NC return was read. Scientific metadata appear in `relative_entropy_search_record.json`.

## Executed queries

| Seq | Date/time record | Tool/engine | Exact query | Filters | Result count | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-10-17; individual time not captured | web/system1 | `"Dorau" "Much" "Relative Entropy" "091602"` | Domain words as written; no recency filter | NOT_EXPOSED_PER_QUERY | Mostly irrelevant; excluded |
| 2 | 2026-10-17; individual time not captured | web/system1 | `"2606.27915"` | Domain words as written; no recency filter | NOT_EXPOSED_PER_QUERY | Primary results screened and citation-chained |
| 3 | 2026-10-17; individual time not captured | system2 | `site.arxiv.org Hollands relative entropy coherent states chiral CFT 2019` | Domain words as written; no recency filter | NOT_EXPOSED_PER_QUERY | Primary results screened and citation-chained |
| 4 | 2026-10-17; individual time not captured | system2 | `site.arxiv.org Banados geometries entanglement entropy conformal transformations interval descendants` | Domain words as written; no recency filter | NOT_EXPOSED_PER_QUERY | Primary results screened and citation-chained |
| 5 | 2026-10-17; individual time not captured | system2 | `site.arxiv.org canonical energy quantum Fisher information Lashkari Van Raamsdonk relative entropy` | Domain words as written; no recency filter | NOT_EXPOSED_PER_QUERY | Primary results screened and citation-chained |
| 6 | 2026-10-17; individual time not captured | system2 | `site.arxiv.org Jacobson thermodynamics spacetime Einstein equation state 1995` | Domain words as written; no recency filter | NOT_EXPOSED_PER_QUERY | Primary results screened and citation-chained |
| 7 | 2026-10-17; individual time not captured | system1 | `site.arxiv.org "Roberts" "Time evolution of entanglement entropy from a pulse"` | Domain words as written; no recency filter | NOT_EXPOSED_PER_QUERY | Primary results screened and citation-chained |
| 8 | 2026-10-17; individual time not captured | system1 | `site.arxiv.org "Relative entropy and the Bekenstein bound"` | Domain words as written; no recency filter | NOT_EXPOSED_PER_QUERY | Primary results screened and citation-chained |
| 9 | 2026-10-17; individual time not captured | system1 | `site.arxiv.org "Relative entropy equals bulk relative entropy"` | Domain words as written; no recency filter | NOT_EXPOSED_PER_QUERY | Primary results screened and citation-chained |
| 10 | 2026-10-17; individual time not captured | system1 | `site.arxiv.org "Entanglement equilibrium and the Einstein equation"` | Domain words as written; no recency filter | NOT_EXPOSED_PER_QUERY | Primary results screened and citation-chained |
| 11 | 2026-10-17; individual time not captured | system2 | `site.arxiv.org "Araki formula" "coherent states" Casini Grillo Pontello` | Domain words as written; no recency filter | NOT_EXPOSED_PER_QUERY | Primary results screened and citation-chained |
| 12 | 2026-10-17; individual time not captured | system2 | `site.arxiv.org "Temperature and entropy-area" Kurpicz Pinamonti Verch` | Domain words as written; no recency filter | NOT_EXPOSED_PER_QUERY | Primary results screened and citation-chained |
| 13 | 2026-10-17; individual time not captured | system2 | `"Araki" "Relative entropy of states of von Neumann algebras" 1976` | Domain words as written; no recency filter | NOT_EXPOSED_PER_QUERY | Primary results screened and citation-chained |
| 14 | 2026-10-17; individual time not captured | system2 | `site.arxiv.org "Gravitation from Entanglement in Holographic CFTs"` | Domain words as written; no recency filter | NOT_EXPOSED_PER_QUERY | Primary results screened and citation-chained |

Search results were returned in aggregated batches; a separate count for each query was not exposed. Do not infer zero results from omitted items. The first author-name query was poor; direct arXiv identifiers supplied the reliable entry points.

## Direct retrieval and screening

The three 2026 papers were opened by exact identifiers, then version-pinned HTML. DM v3 main derivation, MDSV v1 main text and DMV v2 sections 3–5 were inspected. The full proofs in DMV's appendices were not independently reconstructed. Hollands HTML failed; the PDF supplied the ordered-pair formulas. JLMS HTML failed; the abstract URL returned a readable full-text section. The Bisognano–Wichmann publisher link failed; its bibliographic origin is retained with corroboration through primary later authors, not claimed as a full original-paper read.

| ID | DOI/arXiv/pointer | Retrieval depth | Load-bearing locator or limited use |
| --- | --- | --- | --- |
| DM | 2510.24491v3 | MAIN_TEXT | Equations 10-28 and conclusions |
| DMV | 2603.13029v2 | CITED_SECTIONS | Sections 3-5; Corollaries 3.7, 5.2; Theorem 3.10; Definitions 4.1-4.5 |
| MDSV | 2606.27915v1 | MAIN_TEXT | Equations 7-38 |
| A | https://ems.press/journals/prims/articles/2800 | PRIMARY_PUBLISHER_SEARCH_EXCERPT | General definition; no independent proof reconstruction |
| U | 10.1007/BF01609834 | PUBLISHER_METADATA | Genealogy only |
| BW | DM reference 37 | PRIMARY_INACCESSIBLE | Primary bibliographic pointer DM ref37; theorem corroboration C,H |
| J95 | gr-qc/9504004v2 | CITED_SECTIONS | Local horizon and entropy-area contracts |
| J16 | 1505.04753 | ABSTRACT | Distinct small-ball equilibrium route |
| C | 0804.2182v3 | CITED_SECTIONS | Section 3; modular energy and state restriction |
| L | 1901.02366 | ABSTRACT | Coherent-state genealogy only |
| CGP | 1903.00109 | ABSTRACT | AQFT coherent-state host |
| H | 1903.07508v2 | CITED_SECTIONS | PDF pages 5-8; equations 3.22-4.32 |
| P | 1911.10136v3 | CITED_SECTIONS | Lemma 3; Section 5, equations 29-31 |
| KPV | 2102.11547v2 | ABSTRACT | Scaling-limit and area genealogy |
| RT | 10.1103/PhysRevLett.96.181602 | PUBLISHER_METADATA | RT origin |
| R | 1204.1982v1 | CITED_SECTIONS | Equations 13-16; endpoint and regulator transformation |
| FGHMR | 1312.7856 | ABSTRACT | Holographic first-law constraints |
| FLM | 1307.2892 | ABSTRACT | Quantum entropy corrections |
| JLMS | 1512.06431 | CITED_SECTIONS | Sections 1-2 returned as full text; html/v2 failed |
| LV | 1508.00897v2 | CITED_SECTIONS | Sections 1-2, quadratic perturbation order and canonical energy |
| FHSW | 2006.08002v1 | ABSTRACT | No quantitative bound transferred without full theorem audit |

The detailed bibliography includes all primary URLs. The 21 entries have unequal reading depth; abstract-only hosts support genealogy, not newly transferred quantitative estimates. Formula-bearing arguments use the inspected sections of Jacobson, Casini, Hollands, Panebianco, Roberts and Lashkari–Van Raamsdonk.

## Stopping and negative-search statement

Stop reached: the typed chain and assumptions are reconstructed; the deformed version boundary is located; the AdS order discriminator is analytically resolved at the stated scope; implementation options have explicit failure gates. This is MATCH_FOUND / SELECTIVE_SEARCH, not evidence that no other theorem exists. No novelty search was completed. No public dataset, Zotero collection or project literature register was mutated.

## Citation chaining and side harvest

| Origin | Finding | Disposition |
| --- | --- | --- |
| Chiral relative-entropy search -> Panebianco 1911.10136v3 | Bounded intervals and reversed state order supply a direct host for the audit; convexity claims depend on state order. | Used; side lesson retained without creating a new task. |
| Roberts endpoint formula + compact interior flow | Exact length can be unchanged while relative entropy is positive. | Core discriminator; original calculation in report section 5. |
| FHSW 2006.08002 | General von Neumann recovery is a more precise bridge from finite quantum-information work than importing a horizon geometry. | Host candidate; abstract-level screening, quantitative theorem audit still required before reuse. |
| Incidental search result, arXiv:2607.07810, purported interacting-field Rindler relative-entropy paper | Potential follow-up outside the three-paper seed. | Primary abstract retrieval failed (DisabledError); UNVERIFIED_CANDIDATE, not included in bibliography or used to assert a result. |

## Reproduction

Exact search strings and engine selection are preserved. Search rankings/counts are time-dependent and were not independently rerun. Bibliography: BibTeX, `relative_entropy_sources.bib`, checksum in the reproduction manifest. Analytical controls: 12 exact rational checks, AUTHOR_REPRODUCED. Independent literature replication: NOT_RUN. No author was contacted and no peer review was claimed.

