# NASH/IW — current research method and BW interface
### Sanitized bootstrap edition — 2026-08-18

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

`FRONTIER_CANDIDATE != NOVEL`.