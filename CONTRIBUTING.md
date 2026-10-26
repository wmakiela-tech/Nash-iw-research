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

**Weryfikacja CI od 2026-10-26:** workflow `Public source locator guard` zachowuje dotychczasowy lint `check_public_science_writeback.py` dla nowo dodanych plików (`--diff-filter=A`) oraz dodatkowo automatycznie uruchamia `preflight_public_science_writeback.py` z `--diff-filter=AM` i jego testy regresyjne. Obejmuje to zmodyfikowane istniejące publiczne teksty badawcze; przy commitach bez takich plików preflight prawidłowo zwraca `PASS: 0`. **Starsze** zielone runy, sprzed tej zmiany, nie dowodzą naprawy historycznych plików. Preflight na ścieżce umożliwia nadal jawne sprawdzenie pojedynczego dokumentu. Nie używaj rerun starego SHA jako dowodu korekty. Zmiana nie tworzy zdarzenia BW ani nie zmienia statusu naukowego.

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

## Public publication release gate — author + PR (2026-10-26)

For **any public-safe** change, use a feature branch and open a pull request
instead of publishing directly on `main`. After making and locally committing
the candidate change, check the full branch diff **before pushing**:

```bash
git fetch origin main
python scripts/prepublish_public_science.py --base origin/main --head HEAD
# Only if PASS:
git push -u origin <feature-branch>
# Open a PR into main, wait for both checks.
```

This unified author-side check is fail-closed for unreadable/detached Git
history, reports **categories** rather than private provider coordinates, and
checks newly added lines for direct Drive/Slack coordinates and added or
modified full public `research/**/*.md/.rst/.txt` bodies for the required
`artifact_id`, `exposure: PUBLIC`, claim ceiling and BW event/pending state.

The same script runs in the `Public source locator guard` workflow for PRs
and as a post-push audit of `main`. The stable check job is
`Public source locator guard / newly-added-public-locators`. The ordinary
`CI / unit-tests` job remains independent. This is **not** a BW write,
publication-rights review or proof of scientific correctness.

**Repository-owner setting required to make this fail-closed server-side:**
in GitHub Settings → Branches → add a protection rule for `main`.
Require a pull request and the two successful status checks listed above,
disable force pushes and deletion, and apply the rule to administrators
(where available). Confirm a deliberately failing synthetic PR cannot merge.
Without this protection a direct push can land before a failed Actions audit;
a green check on a later commit never repairs prior public disclosure.

Historical offending commits and links require separate risk-reviewed
remediation (removing a link from HEAD does not purge Git history). Do not
force-rewrite shared `main` or remove scientific source artifacts merely
to make a check green. For private or restricted content, use the authorized
private surface and only public-safe, ID-typed source descriptions here.
