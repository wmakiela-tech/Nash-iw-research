---
artifact_id: IW_BADACZ_WUXU_HEAVY_END_CLOCK_RUNLOG_20261111
exposure: PUBLIC
claim_ceiling: PROVENANCE_LOG / NO_RESULT_BEYOND_LINKED_REVIEWS / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-11
origin_cell: BADACZ (wątek Claude)
document_type: RUNLOG
---

# RUNLOG — PREREG_056 / REVIEW_057 (11 XI 2026; zegar kontenera = CET)

**Środowisko:** Julia 1.12.3, kod autorów `d395183` bez zmian, 2 rdzenie; Python 3 (stdlib) do analizy.

| czas | przebieg | plik | uwagi |
|---|---|---|---|
| 00:03:26 | PREREG_056 i sterownik opublikowane (`bdc8906`) | — | sterownik wcześniej nieuruchamiany |
| 00:03:37–00:05:50 | produkcja: j = 62, 97, 98, 99 × log10 β = −30, −19.2; tolerancja domyślna | `heavy_end_clock.csv` | jedno polecenie tła, bez `&` |
| ~00:06 | analiza preregu | `heavy_end_clock_analysis.json` | P2 i P4 FAIL (szczegóły w REVIEW_057) |
| 00:06:37– | **post hoc** (nie w preregu): te same rekordy przy `reltol = 1e−6`, `abstol = 1e−9` dla j = 62, 98, 99 | `heavy_end_clock_tol1e-6.csv` | dodany przełącznik `BADACZ_TOL` w sterowniku (ścieżka domyślna bez zmian, jak w `2026-11-08/code/wuxu_band_kernel.jl`); cel: rozdzielić szum solvera od prawa masy |
| ~00:10 | analiza r1 ponownie wygenerowana: dodane udziały hadronów po T0 oraz `τ_eff` (diagnostyka, bez zmiany kryteriów preregu) | `heavy_end_clock_analysis.json` | przebieg post hoc nadal trwa; plik `heavy_end_clock_tol1e-6.csv` nie jest w r1 |
| 00:06:37–00:39 | przebieg post hoc przy `reltol = 1e−6`, `abstol = 1e−9` **przerwany** | — (plik usunięty) | po 32 min nie ukończył pierwszego punktu (j = 62, β = 1e−30); żadnego wyniku nie widziałem; zastąpiony tolerancją `1e−4 : 1e−7`, tą samą co N1 w REVIEW_050 |
| 00:39:11– | przebieg post hoc przy `reltol = 1e−4`, `abstol = 1e−7` (j = 62, 98, 99 × oba β) | `heavy_end_clock_tol1e-4.csv` | jedno polecenie tła |
| 00:41 | PREREG_058 opublikowany (`3559a17`), przed przebiegiem | — | test samofalsyfikacji REVIEW_054 |
| 00:41– | PREREG_058: `base22t`, `CD2_22t`, `CD0_22t` przy `BADACZ_TOL = 1e−4:1e−7` (sterownik `2026-11-08/code/wuxu_band_kernel.jl` bez zmian) | `kernel_a1tol058.csv` | równolegle z diagnostyką 056 (2 rdzenie) |
| 00:39:11–00:42 | diagnostyka 056 przy `1e−4` ukończona (6 punktów, 26–48 s każdy) | `heavy_end_clock_tol1e-4.csv` | — |
| 00:40:41–01:09 | PREREG_058 ukończony (3 konfiguracje, po 15 punktów, ok. 35–40 s każdy) | `kernel_a1tol058.csv` | log kończy się `DONE` |
| — | kontener sesji odzyskany przez platformę po bezczynności; pliki danych zachowane, procesy już zakończone | — | żaden przebieg nie został przerwany przez odzyskanie |
| 21:3x | analizy r2 (056) i 058 | `heavy_end_clock_analysis.json`, `a1tol058_analysis.json` | `code/wuxu_a1tol058_analysis.py` |
| ~21:45 | PREREG_060: przewidywanie z jądra pasm policzone przed przebiegiem | `subedge_ramp060_prediction.json` | `code/wuxu_subedge_ramp_prediction.py` |
| ~21:47–21:52 | kontrola tożsamości λ = 0, j = 22, log10 β = −17.828, `1e−4` (tylko λ = 0) | brak pliku w repo (scratchpad) | nowy sterownik = stary sterownik = powtórzenie w procesie: `Y_C = 0.24718420969015406`; ten sam punkt w 058 (inna maszyna, przed odzyskaniem kontenera): `0.24715182815744363`. Determinizm jest w obrębie maszyny, nie między maszynami |
| po commicie PREREG_060 | produkcja PREREG_060: proces 1 `configs_subedge060_p1.dat` (j = 22), proces 2 `configs_subedge060_p2.dat` (j = 28), `BADACZ_TOL = 1e−4:1e−7` | `subedge060_p1.csv`, `subedge060_p2.csv` | podział pliku `configs_subedge060.dat` na dwa procesy |
