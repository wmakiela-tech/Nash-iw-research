---
artifact_id: IW_BADACZ_RUNLOG_20261115
exposure: PUBLIC
claim_ceiling: PROVENANCE_LOG / NO_RESULT_BEYOND_LINKED_DOCUMENTS / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-15
origin_cell: BADACZ (wątek Claude)
document_type: RUNLOG
---

# RUNLOG — PREREG_066 (15 XI 2026; zegar kontenera = CET)

| czas | krok | plik | uwagi |
|---|---|---|---|
| ~23:47 | statyczny odczyt `scanning.jld2` autorów (deflate, bez Julii) i porównanie z siatkami natywnymi REVIEW_065, post hoc | `data/archive_vs_native_j22.json` | `code/archive_vs_native_j22.py`; ekstrakcja walidowana statystykami Mech-S8 ROT020 |
| ~23:49 | sterownik `code/b1_calibration_066.jl` sprawdzony **tylko parserem Julii** (`Meta.parseall`, bez ładowania pakietów i bez `magic()`) | — | PARSE_OK |
| 23:51 | PREREG_066 i skrypt analizy zapisane; **przebieg natywny nieuruchomiony** (czeka na autoryzację Moderatora) | — | — |
| 00:05 (16 XI) | uzupełnienie r2 PREREG_066: szerszy zakres obciążenia `saveat` (od 31 X), statyczny odczyt OrdinaryDiffEqCore 3.33.1; **bez przebiegu** | — | kryteria bez zmian |
| 00:10 (16 XI) | **Moderator autoryzował PREREG_066** („Autoryzuję”, rozmowa z Badaczem) | — | autoryzacja jednego przebiegu wg PREREG_066 r1+r2 |
| 00:12–00:29 | kopia środowiska Julii (2.9 GB) z wycofanego katalogu roboczego do `/home/claude/julia066`; nowa ścieżka depot unieważniła cache → pełna prekompilacja (17 min). Wersje z tego samego Manifestu: DifferentialEquations 7.17.0, ArbNumerics 1.6.3 | — | kod natywny skompilowany od nowa; istotne przy interpretacji zgodności bitowej |
| 00:31 | **odstępstwo D1** (przed przebiegiem): w linii nagłówka sterownika wersje pakietów zawierały cudzysłowy, przez co JSON był niepoprawny; poprawiono escapowanie. Bez wpływu na obliczenia. Test pomocnika `s()`: `BigFloat(x; precision=100)` rozróżnia wartości różniące się o 1e−28 | `code/b1_calibration_066.jl` | — |
| 00:30:47–00:44:18 | **przebieg PREREG_066**: 8 ramion w dwóch kolejkach (`code/run066.sh`), wszystkie status 0 | `data/b1_066_raw_outputs.json` | wyjścia poza repo w trakcie, skopiowane po zakończeniu; bez `git stash` |
| 00:45 | analizę wykonał skrypt preregu (`code/b1_066_analysis.py`, zatwierdzony przed wynikami) | `data/analysis066.json` | A-STAT, C0a PASS, C0b FAIL, C0c NO_CONFOUND, S RELEASE, REP-BIT PASS |
| 00:47 | sprawdzono ostrzeżenie o `t0` w logach: kod autorów nie zawiera `t0` (grep), globalne `t0` to licznik czasu sterownika, `magic()` z niego nie korzysta | — | bez wpływu |
| 00:50 | post hoc `code/b1_066_posthoc.py`: ponowne przeliczenie analizy z surowych wyjść (bajtowo identyczne), wrażliwość bramki S na wybór odniesienia, tabele drabiny | `data/posthoc066.json` | oznaczone jako post hoc |
| 00:55 | REVIEW_067 | — | — |
