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
