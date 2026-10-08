# REC9 — DAX prospective discriminator freeze referee 001

**RETURN_ID:** REC9-DAX-PROSPECTIVE-DISCRIMINATOR-FREEZE-REFEREE-001  
**TARGET:** DAX-S6-LT3-PROSPECTIVE-DISCRIMINATOR-FREEZE-DESIGN-001  
**VERDICT:** PASS_WITH_FREEZE_REPAIRS  
**SEVERITY:** HIGH for freeze integrity; low for scientific claim ceiling.

## A. Core verdict

The test claim is legitimate and falsifiable:

**CLAIM_C*** = irreducible cross-host anti-overtransfer / STOP value.

The absorption and negative rules are claim-local. Archival support is correctly separated from genuine prospective confirmation. The design is strong, but **NOT YET READY_TO_FREEZE** until four integrity repairs are completed.

## B. Repair 1 — case-selection census before pair freeze

The proposed selection rule is mechanical in prose, but the packet does not demonstrate that HUST and Front B are actually the first eligible cases under that rule. Because the designer already knows outcomes and candidate cases, the strata can encode hindsight even without using outcome as an explicit field.

Before pair freeze, commit a complete eligibility census over the predeclared pool using **pre-resolution metadata only**. For every candidate record:

- stratum eligibility;
- earliest valid pre-resolution cutoff;
- complete-contract availability;
- stable archive identifier;
- exclusion reason if ineligible.

Only after that census is committed may the earliest-eligible/tie-break rule select the pair.

**PAIR_RECOMMENDATION = PROVISIONAL** until the census independently reproduces HUST <-> Front B.

## C. Repair 2 — executor context isolation

Neutral identifiers and hidden front labels are insufficient for an LLM executor that has project memory, connected Drive/Slack, prior conversation context, or recognizable case-specific wording.

A future blind runner must have:

- no project memory/context;
- no access to DRAFT006 or prior LT/Mech/INT/PRF/DAX returns;
- no Slack/Drive/GitHub connectors except the sanitized test bundle;
- no web search during the run unless identically frozen and supplied to both arms;
- neutral identifiers and sufficiently sanitized case language to prevent easy case re-identification.

If the executor can recognize HUST or Front B from memory, archival blindness is broken even if labels are removed.

Add an **EXECUTOR_ISOLATION_CERTIFICATE** before run authorization.

## D. Repair 3 — independent gold standard and unresolved components

Section G defines a canonical outcome vector O* from the post-cutoff scientific record. That record may contain owner/referee interpretations influenced by TPE and may itself remain unresolved on some components; Front B explicitly has an open endpoint.

O* must therefore be evidence-first, not verdict-first.

For every scored component, record:

- source-native decisive evidence or exact theorem/certificate;
- cutoff date;
- adjudication basis independent of TPE labels;
- status RESOLVED / UNRESOLVED / UNSCORABLE.

Owner/referee status may be supporting provenance, not the sole truth criterion.

For Front B, score only components with a resolved reference answer. Open endpoint components must remain **UNSCORABLE**, not forced into PASS/FAIL.

## E. Repair 4 — baseline-edge admission must be operational

The provenance labels HOST-THEOREM / TYPE-SIGNATURE / ORDINARY-LOGICAL-PREREQUISITE are necessary but not sufficient. “Ordinary logical prerequisite” is open-ended and could absorb TPE edges after the fact, or be withheld to manufacture TPE irreducibility.

Before seeing TPE output, freeze an operational edge-admission rule:

- HOST-THEOREM edge requires named theorem + assumptions + scope;
- TYPE-SIGNATURE edge requires explicit typing/domain/codomain incompatibility or requirement;
- ORDINARY-LOGICAL-PREREQUISITE edge requires a short derivation from shared case facts and propositional/first-order dependency logic without TPE-specific labels/taxonomy;
- every baseline edge carries independent provenance and timestamp/cutoff.

Prefer a baseline builder/adjudicator that is blind to the TPE engine/output.

## F. Additional scoring guard

Diagnostic cost is currently a vector: host nodes opened, theorem invocations, false branches, human decisions. Cost-only survival is not reproducible until comparison is specified.

Before freeze, define either:

- a lexicographic order over these cost components; or
- explicit weights/units; or
- a Pareto rule with a stated tie policy.

Do not declare “strictly cheaper” from an unspecified multidimensional cost vector.

## G. Referee disposition

**DESIGN_VERDICT = PASS_WITH_FREEZE_REPAIRS.**

- CLAIM_C*: PASS as a falsifiable framework-level claim.
- Absorption rule: PASS.
- Safety vetoes: PASS.
- Full-draft leak guard: PASS.
- Designer contamination guard: PASS.
- Pair-selection integrity: NEEDS_CENSUS.
- Executor blindness: NEEDS_ISOLATION_CERTIFICATE.
- Gold-standard O*: NEEDS_EVIDENCE-FIRST / UNSCORABLE handling.
- Baseline anti-circularity: NEEDS_OPERATIONAL_EDGE_ADMISSION.
- Cost-only survival: NEEDS_COMPARISON_RULE.

**READY_TO_FREEZE = NO_YET.**  
**READY_TO_RUN = NO.**

READY_TO_FREEZE may become YES after the four material freeze-integrity repairs plus cost comparison rule are committed and read back.

Archival PASS remains calibration/support only. Archival FAILURE can still materially narrow/kill CLAIM_C* for the pair.

No theory-status promotion, REV021 promotion, novelty inference, canon, EXEC_SIGN, new task, new front, or holdout execution follows.
