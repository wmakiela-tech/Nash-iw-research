---
artifact_id: REC9-EAI-S3-SELECTION-PROVENANCE-REFEREE-001
bw_ingestion_event_id: ING-20261010-0129
bw_qualification_state: SELECTION_PROVENANCE_REFEREE
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: REFEREE_NO_OWNER_AUTHORITY
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# REC9-EAI-S3-SELECTION-PROVENANCE-REFEREE-001

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

REC9 / EAI-S3 SELECTION PROVENANCE REFEREE
RETURN_ID: REC9-EAI-S3-SELECTION-PROVENANCE-REFEREE-001
TARGET: EAI-S3-SELECTION-PROVENANCE-EPISTEMIC-SUPPLY-CHAIN-001
VERDICT: PASS_WITH_ADAPTIVITY_DAG_AND_CLAIM-TYPE_REPAIR
SEVERITY: MEDIUM.
CORE PASS:
SOURCE PROVENANCE, SELECTION PROVENANCE, EXPOSURE PROVENANCE and ADJUDICATION PROVENANCE answer genuinely different questions and should be separately recorded when claim-bearing.
Executor blindness does not retroactively make an outcome-informed case-selection process outcome-blind.
Purposive/stress selection can be scientifically valid with a correspondingly narrow claim ceiling
REPAIR 1 — DISTINCT != ORTHOGONAL
The four provenance classes are non-equivalent and separately auditable, but not generally statistically or causally independent. Selection can depend on source metadata; exposure can depend on selection; adjudication may influence later adaptive selection.
Use:
PROVENANCE_AXES = DISTINCT / POTENTIALLY_COUPLED.
Do not infer orthogonality merely from semantic separation.
REPAIR 2 — PIPELINE != UNIVERSAL TEMPORAL ORDER
SOURCE->ELIGIBILITY->SELECTION->TRANSFORMATION->DELIVERY->EXECUTION->COMMIT->SCORING->REVEAL is a useful nonadaptive template, not a universal process law.
Adaptive/sequential designs can legally interleave execution, outcomes and later selection.
Represent claim-bearing adaptivity by an event-history/filtration DAG with timestamps and allowed-information sets.
REPAIR 3 — ADAPTIVITY
Outcome-blind curation is a strong design, but not a necessary condition for prospective validity. A predeclared adaptive design may use earlier observed outcomes to choose later cases and remain valid when that dependence is part of the declared design and analysis.
Thus:
OUTCOME_INFORMED_SELECTION != INVALID_SELECTION.
OUTCOME_INFORMED_SELECTION != OUTCOME_BLIND_SELECTION.
A clean executor cannot restore an outcome-blind claim, but a valid adaptive evidence claim may still exist.
Recommended fields:
SELECTION_MODE = FIXED_OUTCOME_BLIND / PURPOSEFUL_PREDECLARED / ADAPTIVE_PREDECLARED / POST_HOC_OUTCOME_INFORMED / UNRESOLVED.
INFERENCE_ACCOUNTS_FOR_SELECTION = PASS / FAIL / NA / UNRESOLVED.
REPAIR 4 — CLAIM TYPE BEFORE TRANSPORT
EAI's 'no transport certificate => claim stays on selected stratum' is correct for population-frequency, average-performance and representative-universe claims. It is too broad as a universal rule.
A deliberately selected valid counterexample can refute a universal claim without representative sampling. A theorem proved for all eligible cases also does not require sampling transport. Worst-case/stress claims have their own semantics.
Therefore freeze CLAIM_TYPE before applying selection-transport logic.
Suggested types: SELECTED_STRATUM_DESCRIPTIVE / POPULATION_FREQUENCY / AVERAGE_PERFORMANCE / EXISTENCE_COUNTEREXAMPLE / UNIVERSAL_PROPERTY / WORST_CASE_STRESS / CAUSAL_EFFECT / OTHER.
REPAIR 5 — CURRENTNESS TYPING
Pre-resolution metadata must be judged relative to the event time of each case and the frozen claim. The same metadata can be pre-resolution for one item and post-resolution leakage for another.
In open-ended research, record a declared eligible candidate frame rather than claiming the full source universe is complete.
REPAIR 6 — EXPLORATION VS CONFIRMATION
Post-hoc case or representation choice after seeing a failure breaks a predeclared confirmatory claim, but may remain legitimate exploratory science. Retype it and seek later independent confirmation.
EXPLORATORY_ADAPTATION != CONFIRMATORY_EVIDENCE.
FINAL STATUS
SELECTION_PROVENANCE_DISTINCTION=PASS.
EPISTEMIC_SUPPLY_CHAIN=PASS AS NONADAPTIVE TEMPLATE.
ADAPTIVE_DESIGN_SUPPORT=REPAIR REQUIRED.
OUTCOME_BLINDNESS=STRONG DESIGN, NOT UNIVERSAL VALIDITY CONDITION.
CLAIM_TYPE_BEFORE_SELECTION_TRANSPORT=REQUIRED.
PURPOSIVE_SELECTION=PASS WITH CLAIM TYPING.
EXPLORATORY_POST_HOC_SELECTION=LEGAL AS EXPLORATION / NOT CONFIRMATION.
SOURCE_UNIVERSE_COMPLETENESS=DO NOT ASSUME.
DRAFT015_SELECTION_LAYER=SUPPORTED WITH THESE REPAIRS.
NO NOVELTY / NO CANON / NO EXEC_SIGN / NO NEW TASK / NO NEW FRONT.
STOP after integration. Reopen only if DRAFT015 promotes outcome-blindness to a universal validity condition, if an adaptive protocol is proposed, or if a universe-level performance claim is made from selected cases without a legal bridge.
.
