---
artifact_id: IW_BADACZ_RUNLOG_20261112
exposure: PUBLIC
claim_ceiling: PROVENANCE_LOG / NO_RESULT_BEYOND_LINKED_REVIEWS / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-12
origin_cell: BADACZ (wątek Claude)
document_type: RUNLOG
---

# RUNLOG — PREREG_062 (12 XI 2026; zegar kontenera = CET)

**Środowisko:** Julia 1.12.3 (`wuxu_env`, ten sam Manifest co REVIEW_042–061), kod autorów `d395183`, 2 rdzenie; kontener uruchomiony ponownie o 11:08 (pliki zachowane).

| czas | przebieg | plik | uwagi |
|---|---|---|---|
| ~11:10 | PREREG_062 opublikowany (`d2838c2`, 11:10:44 push), przed przebiegiem | — | — |
| 11:11– | przebiegi A (4 warianty ROT022 + kontrola REVIEW_053) i B (p12 przy tolerancji domyślnej), dwie sekwencje na 2 rdzeniach | `rot022_smoke_*.csv`, `xcheck062a.csv`, `p12_default062b.csv` | skrypt analizy `code/wuxu_062_analysis.py` zatwierdzony w trakcie przebiegu, przed odczytem wyników |
| 11:11:18–11:11:20 | **S1 FAIL** we wszystkich 4 wariantach ROT022 (kod wyjścia 1, po ~2 s): bramka blobów autorów przeszła (linie 53–56), potem `ArgumentError: invalid base 10 digit '#' in "#"` w linii 66 sterownika — parser punktów pomija tylko puste linie, a plik punktów właściciela (`phaseA_smoke_v001.dat`, blob `6d5f3262`) ma 3 linie komentarza `#` | `ROT022_SMOKE_S1FAIL_STDERR_RECORD.md` (dosłowne stderr, 4 identyczne) | defekt interfejsu między dwoma plikami właściciela; Julia i model nie były jeszcze wywołane |
| ~11:13– | **odstępstwo D1 (post hoc, poza preregiem):** te same 4 punkty w pliku bez linii komentarza (`rot022_smoke_points_D1_nocomments.dat`, różnica wobec źródła = tylko usunięte komentarze), sterownik bez zmian; 4 warianty sekwencyjnie na trzecim procesie (chwilowo 3 procesy na 2 rdzeniach) | `rot022_smoke_<wariant>.csv` | wejście doprowadzone do udokumentowanego kontraktu sterownika („j log10beta” w linii) |
| 11:11:59–11:16:20 | D1 ukończone: `native` 11:13:04, `p13` 11:14:07, `native_sym` 11:15:12, `p13_sym` 11:16:20; wszystkie kod 0, `DONE`, po 4 punkty | `rot022_smoke_*.csv` | pliki utworzone po operacji `stash` (niżej), nienaruszone |
| ~11:12:30 | **incydent:** commit z `git stash -q -u` w trakcie działania kontroli krzyżowej i części B; nieśledzone pliki wyjściowe przeniesione i przywrócone puste, procesy pisały do usuniętych i-węzłów | `xcheck062a.csv`, `p12_default062b.csv` (0 B) | procesy zakończone kodem 0 (11:13:43, 11:18:02), wyniki utracone, nieodczytane |
| 13 XI 07:49:37–07:58 | powtórzenie kontroli krzyżowej i części B bez zmian konfiguracji (kontener po restarcie); pliki od startu w lokalnym `exclude`, bez `stash` | `xcheck062a.csv` (07:51:25), `p12_default062b.csv` | równolegle od 07:52 przebiegi PREREG_064 (3 procesy na 2 rdzeniach) |
| 13 XI ~08:00 | analiza skryptem z `69d987b`, bez zmian | `analysis062.json` | A: S1 FAIL (prereg), D1: S2–S4 PASS; B: T1, T2 PASS |
