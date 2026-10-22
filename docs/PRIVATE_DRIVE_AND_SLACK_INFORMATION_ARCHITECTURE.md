# NASH/IW — Private Drive document organization and Slack navigation

**Status:** FORWARD_STORAGE_ROUTING_ACTIVE / BOUNDED_2026-10-13_CLEANUP_PASS  
**Date:** 2026-10-13  
**Owner function:** SYSS4 / systems and cross-surface custody.  
**Authority ceiling:** navigation/custody only; no scientific adoption, CANON, or EXEC_SIGN.

## Purpose and safety boundary

The Moderator requested project-document organization with clear role separation:

- **GitHub:** complete scientific work that has been explicitly classified safe for public release, with code/fixtures/reproduction where legal and possible.
- **Private Google Drive:** project-private documents, restricted originals, manuscripts, lineage/succession packets and nonpublic source custody.
- **BW:** original source identity, committed ING event, qualified status/currentness, private source, public Git path and immutable commit.
- **Slack:** current messages, return routing, live dialogue and alert transport. Slack threads must be searchable as science-bearing source records if they were the only full copy.

**Organization must not rewrite the history of scientific evidence.** A Drive move preserves the same file ID and must not become a duplicated BW scientific event; moving a file does not by itself establish a new science claim or public-release permission. Do not move BW registry or established historical succession folders just to normalize presentation.

## Użycie operacyjne przez wszystkie komórki (2026-10-22)

Lista folderów poniżej jest strukturą **fizyczną**. Instrukcja **dokąd dokładnie zapisać każdy typ pracy oraz gdzie potem go znaleźć** jest obowiązującym [`IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md`](IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md). Autor musi wybrać faktyczny istniejący podfolder według typu/tematu, wykonać odczyt ID/treści po zapisie, powiązać BW i dopiero potem przekazać w Slack. Dokumenty nowo tworzone nie mają trafiać na główną stronę My Drive; nie dodawaj nowych folderów liniowych bez uzasadnionej potrzeby. Historyczne lokatory BW i wcześniejsze zapisane foldery nie są przepisywane dla estetyki.

## Drive — where new private documents go

The already existing project root `NASH–IW Shared Research Bridge` has current-applicable documents, architecture, BW/knowledge and governance/handoffs trees. These original locations remain intact.

A new sibling subtree under the existing root is:

`04_PRIVATE_PROJECT_DOCUMENTS_CURRENT/`

| Folder | Intended document class |
|---|---|
| `00_TRIAGE_NEW_AND_UNCLASSIFIED/` | Temporary intake for files without verified identity/exposure; no acceptance implied |
| `01_CELL_SUCCESSION_AND_HANDOFF_PACKETS/` | Planned/emergency succession, cell role, recipient handoff packets |
| `02_PRIVATE_SCIENTIFIC_SOURCE_AND_REVIEW/` | Private source originals and reviews, including originals whose public-safe scientific bodies live in GitHub |
| `03_MONOGRAPHS_AND_LIVING_BOOKS/` | Draft books, literature foundation maps, living-book educational documents and monograph editorial material |
| `04_REPRODUCTION_DATA_CODE_PACKAGES/` | Restricted or internal code, JSON/ZIP bundles, checks, receipts and data not yet classified for public GitHub |
| `05_SLACK_SOURCE_RECOVERY/` | Complete science messages independently restored from Slack, with original timestamp and source identity |
| `06_SYSTEM_OPERATIONS_AND_GOVERNANCE/` | Internal system review, architecture, governance and operations (not replacements for controlling policy) |
| `99_BLOCKED_HOLD_AND_EXCEPTION/` | Empty shells, denied writes and unresolved custody conflicts, explicitly *not* validated source bodies |

Place each document by **function and exposure class**, not simply by submitting cell or upload date. Names are searchable; stable artifact IDs control identity. Within a major folder, lineages may be subdivided in future only when actual density requires it. Do not create a new folder for every rotation.

### Migration and readback requirements

1. Identify the source file and its current parent using Google metadata.
2. Confirm the destination folder and access/sharing semantics. When uncertain, classify `HOLD`.
3. Move with `addParents` for target and `removeParents` for the exactly verified old parent, preserving the same ID.
4. Read back the parent, file ID, and availability. Do not copy documents just to change location.
5. The location change does **not** alter BW scientific lifecycle, original source event, or public GitHub commit.
6. Preserve older established lineage/frozen archives and shared-drive permissions. No indiscriminate destructive reorganization.

### Bounded migration evidence

The 2026-10-13 first live cleaning pass moved and independently verified **56** owner-only My Drive root files, with the same IDs: 8 succession packets, 20 source/reviews, 8 books, 8 code/data/reproduction artifacts, 9 source-recovery documents, 2 systems/governance documents, and 1 explicitly blocked/empty recovery shell. The latter was placed in `99_BLOCKED_HOLD_AND_EXCEPTION`; this **does not** resolve its source-copy failure. No assertion is made that all project files or history were exhaustively migrated. Existing BW / governance / historical-campaign trees were not moved.

## Slack — source, alert and dispatch routing

Only one lightweight navigation channel was added; the existing four IW channels were left intact. Do **not** mass-forward existing science threads into a new channel: it severs native message identity, sender context, thread provenance and receipt semantics.

| Channel | Role |
|---|---|
| `#iw-start-here` | Stable navigation/index, not an additional scientific task inbox |
| `#iw-dispatch` | Formal cross-cell routing, scientific-return notices, receipts and actionable handoffs; preserve original return thread |
| `#iw-alerts` | Material critical/high risk signals, blocks and authorized global decisions |
| `#iw-live-dialogue` | Small bounded model-to-model sessions; explicit `FROM_CELL` / participant identity |
| `#iw-nc-inbound` | Existing independent private NC inbound; never change its visibility as an organization shortcut |

Slack Canvas could not be created on the current plan (`not_supported_free_team`). A durable `#iw-start-here` index message and a cross-reference from `#iw-dispatch` were created instead. The public-safe rules are in this file; private Drive folder locators and document IDs are **not** included in the public repository.

## Scientific return filing rule

```text
PUBLIC_SCIENCE -> COMPLETE_GITHUB_RESEARCH_BODY
PRIVATE_SOURCE_OR_PACKET -> GOOGLE_DRIVE_PRIVATE_DOCUMENT
RESULT_STATUS_AND_SOURCE_PROVENANCE -> BW_ING + CROSS_SURFACE_CUSTODY
SLACK -> ORIGINAL_MESSAGE_TRANSPORT_AND_THREAD_SEARCH
```

For a public-safe work result, create one complete canonical science body in GitHub and link the **same original artifact identity** to BW. An ordinary private Drive original may be retained for provenance, but the project should not treat a GitHub `POINTER_ONLY` file as completed publication. Public/private release eligibility is determined from actual content and access rules, not by folder name.

**Exceptions:** The prior `INT7 Thread076` document shell is empty due to a provider safeguard, even though the original Slack science return and BW event remain. Its placement in the exception folder marks this fact and does not bypass or retry a blocked provider operation. Old public GitHub commit revisions with private-provider coordinates also remain a separate security hold; Drive moves cannot erase historical public Git records.

## Triggered maintenance, not ritual

At a relevant new upload, Slack-only scientific body, failed write, source mismatch, or search failure, classify only the affected source and file it correctly. Future folder audits may sample accumulated unclassified source documents, using stable IDs and restrictions; they are not a mandatory prerequisite for scientific work.

**Non-collapse:** `FILE_MOVED != SCIENCE_RECLASSIFIED`; `MESSAGE_POSTED != BODY_SAVED`; `FULL_BODY_RECOVERED != ACCEPTED`; `INDEX_EXISTS != ALL_PROJECT_HISTORY_AUDITED`.


## Second bounded structural rotation — 2026-10-13

The Moderator's continuation signal authorized a larger **additional** live filing pass under the same original private Drive tree, without altering the project BW/governance archives or Slack source messages.

### Depth added only where file density justified it

Within `02_PRIVATE_SCIENTIFIC_SOURCE_AND_REVIEW/`:

| New child folder | Classification |
| --- | --- |
| `01_FRONT_B_PBH_BBN` | PBH/BBN, Wu–Xu, Front B source and coupled-error scientific materials |
| `02_H8R_TPE_QRF_AND_COMBS` | typed passage, QRF/comb, H8R and closely coupled LT3 formal work |
| `03_EDU1_AI_AND_EMPIRICAL` | dark-sector EDU1 and empirical/AI-related scientific source work |
| `04_OTHER_FORMAL_THEORY_AND_MECHANISMS` | other mathematical and mechanism returns not uniquely within a narrower front |
| `05_REFEREE_PRIOR_ART_AND_REVIEWS` | source-native reviews, referee attacks, literature/role recovery checks |

Within `03_MONOGRAPHS_AND_LIVING_BOOKS/`:

- `01_LIVING_THEORY_DRAFTS` — earlier authored LT draft revisions, not currentness guarantees.
- `03_LIVING_BOOK_AND_EDUCATION` — learner-facing and educational Living Book working copies.
- Technical monographs, composition plans and book-source maps remain directly under `03_MONOGRAPHS_AND_LIVING_BOOKS/`; the attempted separate child folder create was **provider-blocked** and not retried. Do not mistake an absent child for lost monograph bodies.

These are **filesystem discovery labels**, not science classifications, proof of public-release eligibility, owner acceptance or effective BW/currentness status. No automatic cross-lineage copying or one-folder-per-rotation rule.

### Measured moves and current settled count

- Original first bounded pass: **56** owner-only root files moved into the new private Drive tree with original IDs.
- Second bounded pass: **99** additional verified moves: **77** more originally root-resident project documents plus **22** re-filings within that existing new subtree into more specific research/book categories. Do not double-count the 22 internal moves as new files.
- **Current total: 133 distinct private documents**, all counted by a fresh readback of the designated folder hierarchy, not 155 unique files.
- Science family `02`: **80** documents (1 held at its parent + 15 Front B + 23 H8R/TPE + 8 EDU1 + 25 other formal + 8 reviews).
- Book family `03`: **19** (5 directly in parent + 11 LT drafts + 3 education/Living Book).
- Succession: **14**; private reproduction packages: **8**; Slack recoveries: **9**; systems: **2**; blocked empty shell: **1**; triage: **0**.
- Cumulative project-root cleanup: **133 distinct** private files relocated into the project subtree across both passes. The many other private files and older existing historic NASH folders have **not** been exhaustively audited.

### Explicit non-retry exceptions

Five individual candidate document moves encountered provider safeguards. The source IDs were not discarded, the affected files were **not** represented as successfully moved, and blocked calls were not retried under alternate parameters. Their source titles fall into: an INT7 GTime result already under the new science parent; an LT3 working draft; an MT13 system connectivity document; an MT13 Front B currentness/audit document; and an M12 LT3 synergy/identifiability result. A monographs child-folder creation was likewise provider-blocked; technical-monograph contents remain in the existing parent category. The prior INT7 Thread076 **empty** recovery shell remains in `99_BLOCKED_HOLD_AND_EXCEPTION`, not a verified independent copy.

### Invariant verification

Four sampled live readbacks after migration confirmed unchanged file IDs and owner-only `shared: false` state for:
- SW original source for BW `ING-20261012-0063`, now in private Front B;
- INT7 original source for BW `ING-20261012-0057`, now in private H8R/TPE;
- M12 and KN succession packets, both now in private succession.

The original private BW workbook itself remained in its pre-existing `BW_V0_2_OPERATING_LAYER_20260824` location with the same ID and owner-only permissions. This sample is *not* a new scientific consistency audit of every moved document; the complete move-level checks verified each moved file's ID and new parent.

**Remaining work is targeted historical classification**, not expanding the folder ontology, moving unrelated personal documents, reopening paused scientific fronts, making duplicate public mirrors, or editing science status.

```text
133_DISTINCT_PRIVATE_FILES != 155_UNIQUE_FILES
99_VERIFIED_MOVES = 77_NEW_ROOT_FILES + 22_INTERNAL_REFILINGS
FOLDER_CLASS != SCIENTIFIC_STATUS
PRIVATE_DRIVE_LOCATION != GITHUB_PUBLICATION_LICENSE
```


## Trzeci obrót — deterministyczna procedura zapisu i odczytu (2026-10-22)

**Problem wskazany bezpośrednio przez Moderatora:** porządek folderów bez obowiązkowych reguł zapisu i odszukiwania będzie ponownie rozbijany przez kolejne komórki. Z tego powodu systemowa **[mapa zapisu i wyszukiwania](IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md)** określa dokładnie: typ artefaktu → istniejący folder Drive / ścieżka GitHub → BW `REGISTRY/CROSS_SURFACE_CUSTODY` → kanał Slack → kolejność odczytu. Komórki powinny używać tej mapy **przy tworzeniu wyniku**, a nie po zbiorczym sprzątaniu. Nie oznacza to nowej bariery przed rozpoczęciem badań.

**Procedura jest obecna bezpośrednio lub poprzez obowiązujące odnośniki w:** `WORK_AND_REPRODUCIBILITY_PROTOCOL.md` (pełna tabela wyboru), `STORAGE_AND_SYNC_POLICY.md`, `START_HERE_CURRENT.md`, `SURFACE_ARCHITECTURE.md`, `NAMING_AND_INDEXING.md`, `REPOSITORY_STRUCTURE.md`, tym dokumencie oraz `README.md`. Każdy z tych zapisów został potwierdzony odczytem po commicie. Prywatnych ID folderów i dokumentów nie umieszczono w repozytorium publicznym.

### Bieżąca partia przeniesień

**29 kolejnych, indywidualnie zweryfikowanych przeniesień** z głównego katalogu My Drive do istniejących właściwych folderów IW:

- **5** prywatnych pakietów sukcesyjnych LT4→LT5 (dwie wersje zachowane osobno), SCOPE8→SCOPE9, INT7→INT8 i REC9→REC10 → `01_CELL_SUCCESSION_AND_HANDOFF_PACKETS/`.
- **3** wyniki Front B → `02_PRIVATE_SCIENTIFIC_SOURCE_AND_REVIEW/01_FRONT_B_PBH_BBN/`.
- **14** wyników matematyki/mechanizmów (m.in. M13, DAX, GEEKY) → `02_PRIVATE_SCIENTIFIC_SOURCE_AND_REVIEW/04_OTHER_FORMAL_THEORY_AND_MECHANISMS/`.
- **7** niezależnych audytów i przeglądów źródeł → `02_PRIVATE_SCIENTIFIC_SOURCE_AND_REVIEW/05_REFEREE_PRIOR_ART_AND_REVIEWS/`.

Nie scalano automatycznie dokumentów o podobnym tytule ani różnych identyfikatorach, nie zmieniano ich treści, klas dostępu lub pierwotnego ID. Ruchy miały kontrolę źródłowego rodzica, prywatności, właściwego docelowego rodzica oraz stabilnego ID. Materiały RPG/Warhammer i inne prace spoza IW/NASH pominięto. Nie tworzono nowych katalogów, nie dotykano BW ani starych archiwów przez samą zmianę struktury.

### Odczyt aktualnej liczebności po obrocie

Dwa kolejne odczyty istniejących katalogów dały **172 pliki w nowej strukturze**, nie licząc podfolderów:

| Katalog | Pliki |
| --- | ---: |
| `01_CELL_SUCCESSION_AND_HANDOFF_PACKETS` | 20 |
| `02_PRIVATE_SCIENTIFIC_SOURCE_AND_REVIEW` bezpośrednio | 1 |
| `02/.../01_FRONT_B_PBH_BBN` | 18 |
| `02/.../02_H8R_TPE_QRF_AND_COMBS` | 23 |
| `02/.../03_EDU1_AI_AND_EMPIRICAL` | 8 |
| `02/.../04_OTHER_FORMAL_THEORY_AND_MECHANISMS` | 39 |
| `02/.../05_REFEREE_PRIOR_ART_AND_REVIEWS` | 19 |
| `03_MONOGRAPHS_AND_LIVING_BOOKS` bezpośrednio | 5 |
| `03/.../01_LIVING_THEORY_DRAFTS` | 11 |
| `03/.../03_LIVING_BOOK_AND_EDUCATION` | 3 |
| `04_REPRODUCTION_DATA_CODE_PACKAGES` | 13 |
| `05_SLACK_SOURCE_RECOVERY` | 9 |
| `06_SYSTEM_OPERATIONS_AND_GOVERNANCE` | 2 |
| `99_BLOCKED_HOLD_AND_EXCEPTION` | 1 |
| `00_TRIAGE_NEW_AND_UNCLASSIFIED` | 0 |
| **Razem** | **172** |

Różnica pomiędzy poprzednim stanem 133 i obecnymi 172 **nie jest w całości skutkiem 29 nowych ruchów SYSS**: w katalogach występowały już inne późniejsze dodatki. Nie przedstawiaj jej jako 39 przeniesień tego obrotu. Liczby są odczytem konkretnego obszaru, nie pełną inwentaryzacją całego konta Drive i nie dowodem currentness/accepted science.

**Granice i jawne HOLD:** Historyczne repozytoria, stare kopie i pozostałe źródła w My Drive root nadal wymagają celowej klasyfikacji; zachowany jest zablokowany pusty shell INT7 Thread076 oraz historyczna ekspozycja lokalizatorów w starych publicznych commitach. W tym obrocie nie ponawiano zablokowanych operacji, nie zmieniano udostępniania prywatnego katalogu i nie dokonywano naukowej rekwalifikacji. Dostęp innych osób do plików nadal podlega rzeczywistym uprawnieniom Google, nie nazwie folderu czy indeksowi Slack.

`EXACT_ROUTE_AT_WRITE_TIME > CLEANUP_AFTER_THE_FACT`; `ONE_ARTIFACT_ID -> ONE_CANONICAL_BODY`; `FILE_MOVED != BW_ACCEPTED`; `FOLDER_COUNTS != SCIENCE_CURRENTNESS`.
