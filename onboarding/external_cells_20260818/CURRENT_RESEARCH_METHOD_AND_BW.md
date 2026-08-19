# NASH/IW — current research method and BW interface
### Sanitized bootstrap edition — updated 2026-08-19 after SP BW audit

Status: `INTERIM_REAL_USE / TEST_REQUIRED / NO_CANON / NO_EXEC_SIGN / REVERSIBLE`.

## 1. Research method

The method is intentionally problem-dependent and may be disabled or changed when it harms research.

Core rules:

- `SCIENCE_FIRST`
- `METHOD_MUST_BE_ALLOWED_TO_FAIL`
- `METHOD_MUST_BE_ALLOWED_TO_CHANGE`
- `PROCEDURE != PERMANENT_LAW`
- `HEURISTIC != CANON`
- `PAST_SUCCESS != FUTURE_OBLIGATION`
- `MULTIMODEL_TEAM` is not default.

Research scale may be `LIGHT / BOUNDED / FULL`.

Choose roles by proof obligation and expected decision value, not model count or prestige. Preserve material divergence until a discriminator exists.

Prior-art pressure should appear before **material engaged effort** when the problem has a recognizable theorem/mechanism/known-field shape.

`NO_MATCH_FOUND != NOVELTY`

Prefer:

`BEST_EXPECTED_DECISION_RELEVANT_VALUE_PER_TOTAL_COST`

where total cost includes scientific work, compute, coordination, Moderator attention, access/infrastructure and downstream work.

## 2. Failure typing

A negative-looking outcome should not update science until the failure is typed where material:

- `SCIENTIFIC_NEGATIVE`
- `INSTRUMENT_FAILURE`
- `IMPLEMENTATION_FAILURE`
- `INFRASTRUCTURE_FAILURE`
- `CUSTODY_PROVENANCE_FAILURE`
- `INSUFFICIENT_POWER`
- `UNSUPPORTED_CONFIGURATION`
- `UNKNOWN`

`INSTRUMENT_VALIDATION != RESULT_VALIDATION`

`RUNNABLE != VALID_SCIENTIFIC_OBJECT`

Legal research transitions include:

`CONTINUE / REFRAME / KILL / HOLD / UNKNOWN / INSUFFICIENT_POWER / ASSIMILATE_PRIOR_ART / CLOSE_IN_SCOPE / HANDOFF / CLEAN_RESTART / TRANSFERRED`

`NONE_OF_CURRENT_HYPOTHESES_IS_TRUE` is legal.

## 3. Completion guard

The project is actively testing a completion-drift hypothesis:

`LOCAL_OUTPUT_READY != TURN_ACCOUNTED != PUZZLE_CLOSED`

Runtime completion, report completion, reviewer PASS or checklist completion must not silently substitute for the scientific target.

For LIGHT work, formal completion accounting is normally OFF. For BOUNDED/FULL work, minimal accounting may be used only when it adds value.

## 4. Independence

Different model names are not automatically independent evidence. Independence also depends on:

- source exposure;
- prompt framing;
- persona/role prompt;
- shared code/oracle;
- shared project history;
- analysis path;
- implementation path.

If a blind pass is required, use the separate blind launcher and freeze before exposing current answers or other returns.

## 5. BW / Scientific Knowledge Base

The live BW currently resides on private project storage. External cells without Drive access participate by returning append-only contribution deltas in-thread or as files.

Current prototype state after independent SP epistemic audit: `BW/SKS v0.1.1 / LIVE_USE_WITH_PATCHES / NO_CANON / NO_EXEC_SIGN`.

Semantic architecture:

```text
         SHARED EVIDENCE / PROVENANCE SPINE
                    |
          +---------+---------+
          |                   |
      P-PLANE             S-PLANE
 Project Knowledge     Scientific Knowledge
          |                   |
          +--- typed bridges -+
                    |
              DERIVED VIEWS
```

Load-bearing invariants:

- `SOURCE != ASSERTION != EVIDENCE != MECHANISM != SYNTHESIS`
- `AUTHORITY_STATE != EVIDENCE_STATE`
- `PROJECT_CURRENT != SCIENTIFICALLY_BEST_SUPPORTED`
- `PROJECT_CLOSED != SCIENTIFICALLY_RESOLVED`
- `PROJECT_ADOPTION_DOES_NOT_UPGRADE_SCIENCE`
- `S_EVIDENCE_DOES_NOT_ENACT_PROJECT_POLICY`
- `MODEL_AGREEMENT_NOT_EVIDENCE`
- `NO_MATCH_FOUND_NOT_NOVELTY`
- negative/no-go knowledge is first-class and scope-bound
- conflict is preserved
- supersession is append-only
- `AI_EXTRACTION_IS_CANDIDATE_UNTIL_QUALIFIED`
- current state is derived from events
- `OPEN_WORLD_BY_DEFAULT`
- `HASH_IDENTITY != SCIENTIFIC_VALIDITY`

### 5.1 v0.1.1 provenance and retrieval guards

The SP audit found that an early prototype relied too heavily on a single synthesis document and that some conformance tests were vacuous. v0.1.1 therefore adds these guards:

- load-bearing provenance should include a `SOURCE_ANCHOR` locating the relevant section/theorem/result inside a source, not only a pointer to the whole document;
- for a formal-mathematics claim, `SUPPORTED_CURRENT` requires evidence of class `PROOF`; otherwise a legal state is `ASSERTED_IN_SYNTHESIS_PROOF_NOT_LOCATED`;
- `WARRANT_BOUNDARY` is distinct from durable `NEGATIVE_KNOWLEDGE`; a warrant boundary should state what gate can lift it;
- an exact prior-art absorption or source-dependent `CLOSED_IN_SCOPE` must not be treated as unconditional when the external source/theorem location has not been verified;
- bounded retrieval is asymmetric: it may omit some support before it omits an active boundary. Active `WARRANT_BOUNDARY`, relevant `UNKNOWN`, current claim boundary and terminal completion debt must not disappear merely because a neighborhood is truncated;
- conformance tests must include adversarial fixtures that actually attempt P→S or S→P status leakage; a correct seed alone is not a discriminating test;
- event `issuer` identifies the responsible cell/participant; the document belongs in provenance;
- synthetic conformance fixtures must remain separate from live scientific knowledge.

## 6. External-cell BW delta

When your work creates a material reusable change, return:

```json
{
  "contribution_id": "BW_DELTA_<CELL>_<TOPIC>_<SEQ>_<DATE>",
  "contributor": "<cell>",
  "cell_id": "<cell id>",
  "target_plane": "SPINE|S|P|CROSS|MIXED",
  "material_delta": true,
  "records": [],
  "events": [],
  "relations": [],
  "bridges": [],
  "source_anchors": [],
  "dissent_or_unknown": [],
  "completion_debt": [],
  "notes": []
}
```

Rules:

- no overwrite: correction is a new event;
- scope negative knowledge;
- preserve UNKNOWN and dissent;
- source pointer alone does not imply SUPPORTS;
- reviewer PASS does not close a scientific puzzle;
- if there is no material delta, report `NO_MATERIAL_BW_DELTA` rather than an empty compliance artifact.

Field/frontier maps from scientific scouting may enter as candidate S-plane objects, but:

`FRONTIER_CANDIDATE != NOVEL`

For imported frontier candidates, preserve at least `framework_activity_state` and `last_verified_active` where those fields are material. A stale open problem or a question open only inside an abandoned framework must not silently become a current field frontier.
