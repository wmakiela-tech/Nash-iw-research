# NASH/IW — Bounded Scientific Connector Benchmark 001 (2026-10-13)

```yaml
artifact_id: IW_KN10_SCIENTIFIC_PLUGIN_BENCHMARK_001_20261013
origin_cell: KN10 / KCELL
kind: TOOLING_EVALUATION_WITH_SOURCE_NATIVE_SPOT_CHECK
authority: ADVISORY_ONLY
exposure: PUBLIC
status: BOUNDED_TEST_COMPLETED
subject: source discovery and exact-theorem eligibility (Mori-Zwanzig memory approximation)
claim_ceiling: ONE_CASE_WORKFLOW_VALIDATION_NOT_TOOL_ACCURACY_CERTIFICATION
no_change_to: [BW_QUALIFICATION, LT_HEAD, CANON, EXEC, HOLD, INDEPENDENT_REVIEWS]
related_guidance: docs/RESEARCH_PLUGIN_ROUTING_20261013.md
```

## Question and test protocol

Question: Can three connected discovery providers find the same *original* mathematical paper, separate preprint from peer-reviewed publication, and expose exact assumptions and transfer restrictions rather than return only abstract-level summaries?

This is a *known-source, low-cost calibration*: there is no new research hypothesis or claim of independent theorem validation.

Search on 2026-10-13, focused on:
- `Consensus.search`: exact title and authors, plus `Consensus.fetch` using the exact returned paper ID;
- `SciSpace.search_papers`: full natural-language question asking for rigorous error/convergence conditions for Mori-Zwanzig memory approximations;
- `Sider Scholar.search_open_access_works`: concise topic query `Mori Zwanzig memory integral`, OpenAlex source;
- direct source check: published manuscript text available on the author-posted ResearchGate page (original *Journal of Mathematical Physics* PDF rendered as searchable HTML), plus the arXiv preprint record;
- `WolframAlpha`: one ancillary scalar-integral sanity check; **not** verification of the operator theorem.

This is a specific, limited query set, not a measured recall/precision benchmark, complete literature review, or broad survey of all search-result positions.

## Actual identified source

Yuanran Zhu, Jason M. Dominy, Daniele Venturi, **“On the estimation of the Mori-Zwanzig memory integral”**, *Journal of Mathematical Physics* **59**, 103501 (published 21 September 2018), DOI **10.1063/1.5003467**.

Primary/public source references:
- arXiv preprint record: https://arxiv.org/abs/1708.02235
- Published-paper full-text rendering (author-hosted manuscript copy): https://www.researchgate.net/publication/327814463_On_the_estimation_of_the_Mori-Zwanzig_memory_integral
- DOI: https://doi.org/10.1063/1.5003467

The *preprint* existed in 2017; some discovery results label the work 2017, while the peer-reviewed publication is 2018. SciSpace returned separate records with arXiv DOI 10.48550/arXiv.1708.02235 and publisher DOI 10.1063/1.5003467, including inconsistent harvested date metadata. **Do not count these as distinct independent papers or infer bibliographic truth from an index's publication-year field alone.**

## Observed provider behavior (one case)

| Provider | Evidence observed | Useful role | Limits |
|---|---|---|---|
| Consensus | Exact source/title retrieved; explicit fetch record returned title, author metadata, abstract and 2017 index year | Candidate and subject discovery; fast abstract screen | Index year deviates from published 2018 version; fetched text was abstract, not section/theorem verification |
| SciSpace | Found same title with publisher DOI and distinct arXiv/preprint records; DOI 10.1063/1.5003467, abstract | DOI reconciliation and related-source discovery | Separate index items are not independent support; date metadata not authoritative without primary check |
| Sider Scholar / OpenAlex | Found exact source with OpenAlex work ID W2803336425, PDF path to arXiv, matched three authors | Stable paper seed + accessible original PDF | Metadata/PDF link discovery alone does not establish theorems have been read |
| WolframAlpha | Evaluated scalar integral `exp(-t)∫_0^t exp(s) ds = 1-exp(-t)` correctly | Small illustrative analytic checks where appropriate | This example does *not* test the paper's operator-semigroup theorem or source assumptions |
| Undermind | Connected tool available in prior readiness check, but zero active workspaces | Potential deep multi-hop search after workspace provision | No paper search performed in this pilot; not scored as a successful provider |
| Scite, Elicit | Prior 2026-10-13 account tests returned subscription/API entitlement restrictions | Potential paid adversarial citation/context analysis | Not active for this account; do not block work or infer lack of scholarship |

## Original theorem-level check

The author-hosted manuscript contains the actual assumptions and constraints:

1. **Theorem 3.2 (t-model):** the relevant evolution/orthogonal-dynamics operators must generate strongly continuous semigroups with specified norm-growth upper bounds. The norm error is bounded by the derived `M_1(t)`; the result `M_1(t) → 0` as `t → 0` establishes short-time convergence. This is not an unconditional all-time bound.
2. **Theorem 3.3 (short-memory truncation):** likewise specifies semigroup bounds and the memory-window length `Δt∈[0,t]`, and estimates the error when omitting earlier times. Choosing a short window is not automatically justified for arbitrary systems.
3. **Corollary 3.4.2 (hierarchical H-model):** asymptotic convergence at fixed finite time relies on a further bounded-sequence condition on the `α_j` controlling successive operator terms. It cannot be deduced merely from the existence of an MZ decomposition.

Text locations: *J. Math. Phys.* volume 59 (2018), source manuscript pages 103501-7–103501-8 (Theorems 3.2–3.3), ~103501-12 onward (hierarchical estimates). For exact application to an IW operator, check domains, semigroup generation, `Q`-projected evolution, norm type and whether required constants/bounded ratios exist.

```
MATURE_MZ_THEOREM != AUTOMATIC_APPLICATION_TO_IW_MODEL
SEMGROUP_BOUND + DOMAIN_CHECK != ESTABLISHED_FOR_EVERY_OPERATOR
SHORT_TIME_ERROR_TO_ZERO != UNIFORM_LONG_TIME_ACCURACY
INDEX_RECORD_2017 != PEER_REVIEWED_PUBLICATION_DATE_2018
SAME_PAPER_IN_THREE_DATABASES != THREE_INDEPENDENT_REPLICATIONS
```

The direct source check makes these caveats visible. None of the three metadata tools by itself proved the exact theorem's assumptions, nor were those assumptions validated for an IW-specific operator. No application to NCDG, LT, Front B or an empirical physical model is claimed.

## What this test justifies operationally

- Discovery/triage: use one suitable index by default; use a second if the DOI/version or coverage remains uncertain.
- Adversarial subtraction: if a source is load-bearing, **open and read the actual original text** at its theorem, proof or counterexample. The database summaries are only routing aids.
- Cross-index duplicates: normalize DOI, arXiv ID, authors, title and version; preserve separate *versions* under one work identity rather than counting duplicate hits as independent confirmations.
- Context-specific transfer: record each exact hypothesis, object type, domain, convergence horizon, non-map and proof status before a mature theorem is mapped into IW.
- Computational check: keep it explicitly `EXAMPLE_OR_SANITY_CHECK` unless code, exact transformations and premises truly verify the intended statement.
- Independence: protect the independent reviewer/NC pre-freeze stage; multiple connected applications in one agent do not create independent agents.

**Conclusion:** the available multi-index toolset is useful to increase source discoverability and locate version conflicts, but the best gain in this pilot came from *source-native eligibility checking*. This calibration warrants optional role-specific use, not a blanket mandate, new science, a scientific acceptance decision or an extra BW artifact.

## Provenance and reproducibility

Study observed date: **2026-10-13**. Exact query style and source anchors are given above. The underlying connected providers can reorder results or change coverage over time; reproduce on a new date with provenance and assess discrepancies. Tool result metadata is not frozen as a primary scientific source.

This advisory does not supersede project `docs/WORK_AND_REPRODUCIBILITY_PROTOCOL.md` or `docs/STORAGE_AND_SYNC_POLICY.md`; the current authoritative BW/LT scientific owners and governance retain all their roles. No private records, provider tokens or private Drive coordinates were copied to public GitHub.
