# IW / NASH — AInstein / Gemini BW audit request

Status: `PROJECT_RESEARCH_AUDIT / PUBLIC_SANITIZED_PACKET / TEST_REQUIRED / NO_CANON / NO_EXEC_SIGN`

## Independence guard

This is an independent architecture/testability audit. Do not read the SP return or any later BW audit return before freezing your own pass.

## Object under audit

NASH/IW BW / Scientific Knowledge Base prototype v0.1. The public packet is intentionally sanitized: private Google Drive locators and custody identifiers are omitted. Their absence in this packet is not itself a BW defect.

The prototype tests a two-plane representation:

`Shared Evidence/Provenance Spine + P-plane Project Knowledge + S-plane Scientific Knowledge + explicit typed cross-plane bridges + append-only events + derived views`.

Do **not** select a production backend and do **not** redesign the entire system. Attack the minimal representation and executable semantics.

## Questions

1. Can the schema enforce `PROJECT_ADOPTION != SCIENTIFIC_SUPPORT`, or are there hidden propagation paths?
2. Can append-only events deterministically reconstruct current state under concurrent/multi-cell contribution?
3. Are event identity, ordering and conflict semantics adequate, or can legitimate parallel events become ambiguous?
4. Does the reducer incorrectly assume one linear event sequence per subject/facet?
5. Are relation objects and bridge objects sufficiently referentially validated?
6. Can a source/evidence object be referenced without silently treating source presence as evidential support?
7. Does open-world neighborhood truncation reliably prevent false closure? Attack `BOUNDARY_STUB` and `explicit_omissions`.
8. Can a receiver lose a load-bearing negative claim, UNKNOWN, dissent, supersession, or claim boundary under a small node budget?
9. Can `FIELD_MAP` ingestion from independent scouting remain candidate knowledge rather than truth/novelty promotion?
10. Can multi-cell deltas create silent last-write-wins, curator capture, duplicate identities or unrecoverable current state?
11. What deterministic checks are missing before live scaling?
12. Which schema elements are unnecessary overhead at v0.1?

## Required adversarial tests

- **P→S non-propagation:** add P adoption/authority events for a contested S object; S epistemic state must not change.
- **S→P non-propagation:** add strong S support; P adoption/authority must not change.
- **Parallel event attack:** create two same-subject/same-facet events from independent cells without a shared total ordering. Determine whether the current contract can represent this without arbitrary winner selection.
- **Supersession attack:** supersede a claim while retaining old source/provenance and reconstruct both current and historical views.
- **False-closure retrieval attack:** truncate before a live alternative/UNKNOWN/negative branch and test whether the packet sufficiently warns the receiver.
- **Prior-art absorption attack:** preserve project lineage while removing/narrowing novelty after exact prior art is found.
- **Bad synthesis anchor attack:** assume one high-level synthesis source is wrong; test whether local correction can occur without rewriting unrelated history.
- **Schema gaming attack:** produce a structurally valid but epistemically vacuous delta and determine which machine checks can reject/quarantine it without pretending to judge scientific truth.

## Return

```yaml
AINSTEIN_BW_AUDIT_RETURN:
  overall_verdict: PASS | PASS_WITH_PATCHES | MATERIAL_REDESIGN_REQUIRED | INSUFFICIENT_EVIDENCE
  load_bearing_strengths: []
  material_failures: []
  deterministic_invariant_failures: []
  concurrency_or_identity_failures: []
  retrieval_false_closure_risks: []
  required_contract_patches: []
  required_reducer_patches: []
  required_tests: []
  optional_simplifications: []
  field_map_ingestion_findings: []
  real_use_recommendation: CONTINUE | CONTINUE_WITH_PATCHES | PAUSE_LIVE_INGEST | KILL_OR_REDESIGN
  confidence_and_limits: []
```

Prefer concrete counterexamples and minimal patches. Do not infer scientific truth or novelty. No mandatory new governance layer.
