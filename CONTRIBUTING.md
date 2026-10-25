# Contributing

Before research-related or claim-heavy work, read [`docs/START_HERE_CURRENT.md`](docs/START_HERE_CURRENT.md), follow [`docs/WORK_AND_REPRODUCIBILITY_PROTOCOL.md`](docs/WORK_AND_REPRODUCIBILITY_PROTOCOL.md), resolve current BW/source state, and follow [`docs/REPOSITORY_STRUCTURE.md`](docs/REPOSITORY_STRUCTURE.md) plus [`docs/STORAGE_AND_SYNC_POLICY.md`](docs/STORAGE_AND_SYNC_POLICY.md).

GitHub code or an old report is not sufficient evidence of scientific currentness.

## Working sequence

1. Resolve current role/function, BW currentness and applicable STOP/HOLD.
2. Reuse the stable `artifact_id`; a transport copy is not a new artifact.
3. Classify exposure: `PUBLIC`, `PRIVATE`, or `RESTRICTED`.
4. Choose the canonical repository class.
5. Make the smallest coherent change.
6. Add/update tests when executable behavior changes.
7. Persist material work and read it back.
8. Complete the BW↔GitHub handshake for material public artifacts.
9. Record provenance, claim ceiling and supersession.
10. Use review/PR when the change needs independent repository review.

## Canonical placement

- current operator/system contract → `docs/`
- public-safe scientific body → `research/<lineage>/<YYYY-MM-DD>/`
- compact pointer/hash/legacy record → `archive-index/<YYYY>/<lineage>/`
- public-safe succession pointer → `succession/<YYYY>/<lineage>/`
- executable code → `runtime/` or `src/`, with tests/fixtures/manifests
- cross-surface projection → `manifests/cross-surface/`

Do not create new ad-hoc top-level folders.

Historical paths are provenance. Do not mass-rename them solely to fit the current layout.

## Public research preflight — metadata gate (2026-10-25)

Dla każdego nowego **public-safe** pełnego tekstu `research/**/*.md` / `.rst` / `.txt` przed publikacją zastosuj [wspólny szablon](templates/IW_MATERIAL_WORK_RETURN_TEMPLATE.md), a następnie uruchom:

```bash
python scripts/preflight_public_science_writeback.py research/<lineage>/<YYYY-MM-DD>/<file>.md
# dla wszystkich nowo dodanych i zmodyfikowanych research docs w danym zakresie
python scripts/preflight_public_science_writeback.py --base <BASE_SHA> --head <HEAD_SHA>
```

W pierwszych **3500 znakach pliku**, od początku wierszy bez wcięć, muszą wystąpić rzeczywiste (nie opisowe) wartości:
- `artifact_id: <real-artifact-id>`;
- `exposure: PUBLIC` — tylko po zgodzie na publiczną ekspozycję, inaczej nie publikuj w tym repo;
- jedna z rozpoznawanych nazw: `scientific_claim_ceiling`, `claim_ceiling`, `result_class`, `status`, z niepustą wartością (preferuj jawny `claim_ceiling` i uczciwą kategorię wyniku);
- **albo** `bw_ingestion_event_id: ING-YYYYMMDD-NNNN` (prawdziwy istniejący ING), **albo** `sync_state: GITHUB_PENDING_BW_INGEST` (gdy KN/BW jeszcze nie dokonał ingestii).

Nazwy `RETURN_ID`, `CLASS`, `CEILING`, `BW_PENDING`, `bw_event_or_pending` i `exposure: PUBLIC_SAFE` **nie** zastępują rozpoznawanych pól. Nie wymyślaj ING i nie deklaruj `SYNCED` na podstawie samego publikowania. Całe źródło musi być pełnym body, nie `POINTER_ONLY/HASH_ONLY`, i spełniać istniejące wymagania linta długości.

**Istotna luka CI:** workflow `Public source locator guard` uruchamia drugą kontrolę `check_public_science_writeback.py` z `--diff-filter=A`. Zielony run po poprawieniu istniejących plików **nie poświadcza** poprawności ich metadanych; użyj jawnego preflight na pełnej treści (lub `--base/--head` z `A+M`). Nie uruchamiaj rerun starego SHA jako testu korekty.

**Odnajdywanie runów:** domyślne `fetch_commit_workflow_runs` konektora filtruje tylko `pull_request`; dla `push` podaj istniejący `run_id` z alertu lub wykonaj GitHub API `GET /repos/wmakiela-tech/Nash-iw-research/actions/runs?head_sha=<FULL_SHA>&event=push` (dobierz `workflow_id=382571550` z odpowiedzi). Zero wyników z wyszukiwania `pull_request` **nie oznacza**, że run nie istnieje. Nie zmieniaj triggerów workflow tylko w celu naprawienia wyszukiwarki.

## BW handshake

A material GitHub commit is not complete project custody by itself.

```text
COMMIT -> BW INGESTION/STATUS -> CROSS-SURFACE READBACK
```

If BW cannot be updated immediately, label the state `GITHUB_PENDING_BW_INGEST`; do not claim `SYNCED`.

For a public-safe BW/Drive artifact that lacks GitHub custody, use `BW_PENDING_GITHUB_PUBLICATION` until a canonical immutable GitHub commit exists.

## Required provenance for material public artifacts

Include or make recoverable:
- artifact/contribution ID;
- source revision;
- origin cell/lineage;
- BW ingestion event when known;
- epistemic status / claim ceiling;
- archive mode;
- `derived_from` / `supersedes` where applicable;
- canonical GitHub path + immutable commit after publication.

## Pull-request minimum

State purpose, changed files, source artifacts or hashes, tests, resource cost, claim boundary, current BW relation, exact next step and Moderator action only where genuinely required.

## Reproducibility minimum

A load-bearing computational or empirical result must include a validated `schemas/research-reproduction-manifest.schema.json` instance, exact code/environment/commands/inputs/outputs/checksums, controls, tolerances and an honest reproduction state. A load-bearing literature result must preserve exact queries, databases/tools, filters, screening logic, source locators, retrieval depth/limits and a checksummed bibliography export using the current literature template.

A narrative claim without its load-bearing bundle is `EVIDENCE_INCOMPLETE_FOR_REPRODUCTION`; this is not automatically a scientific-failure verdict.

## Public repository boundary

This repository is public.

Never commit credentials, tokens, passwords, private keys, personal/family data, restricted source material, private cross-cell packets, private Drive/Slack coordinates or unapproved unpublished scientific conclusions.

Private/restricted artifacts use `POINTER_ONLY`, `HASH_ONLY`, or `PRIVATE_ONLY`. Public-safe pointers must use artifact/BW identity rather than exposing private provider coordinates.

Do not rewrite frozen checkpoints. Use a new version, superseding artifact or authorized append-only addendum.

```text
GITHUB_COMMIT != BW_EVENT
MIRROR_SYNC != SCIENTIFIC_VALIDATION
PUBLIC_GITHUB != PRIVATE_IW_COMMONS
```
