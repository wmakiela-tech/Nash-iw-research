---
artifact_id: IW_BADACZ_WUXU_SUBEDGE_PILOT_RUNLOG_20261031
exposure: PUBLIC
claim_ceiling: PROVENANCE_LOG / NO_RESULT_BEYOND_LINKED_REVIEW / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-31
origin_cell: BADACZ (wątek Claude)
document_type: RUNLOG
---

# RUNLOG — PREREG_041: prawo `T^{1.3}` i pilotaż PYTHIA (31 X 2026, wieczór)

Środowisko jak w `../native_audit/RUNLOG.md`. PYTHIA 8.318.3 (`pythia8mc` z PyPI), numpy, Python 3.13.

| czas (CET) | przebieg | plik | uwagi |
|---|---|---|---|
| 19:51 | test dymny PYTHIA (5 zdarzeń `uū`, `1e4 GeV`) | — | tylko mechanika i czas; przed preregiem |
| 19:52 | PREREG_041 opublikowany (`ad6ab99`) | — | przed przebiegami A i B |
| 19:53–20:09 | A: wariant `p13`, 12 mas | `e2_p13.csv` | sterownik w wersji, która stała się `wuxu_subedge_variant_boundary_v2.jl` |
| 19:54 | test funkcjonalny skryptu pilotażu (2/4 zdarzenia na konfigurację) | — | sprawdzenie kodu; wyniki odrzucone |
| 19:55–20:03 | B: pilotaż PYTHIA, 8000 zdarzeń | `pythia_multiplicities.csv`, `pythia_pilot.json`, `pythia_rate_table.csv` | 69 nieudanych `next()` (wszystkie przy `≥ 3000 TeV`) |
| ~20:05 | POST HOC: profil nachylenia tabeli wobec modelu | `table_edge_posthoc.json` | po niezaliczonej bramce B2 |
| ~20:09 | werdykty | `prereg041_analysis.json` | C nie uruchomione (B2 niezaliczone) |
| 20:10–20:14 | kontrola v2 (`native`, `p13`, masa 22) równolegle | — | `native` przerwany: oba procesy współdzieliły jedną nazwę pliku tymczasowego |
| 20:14–20:17 | ta sama kontrola po nadaniu plikom tymczasowym unikalnych nazw (PID) | `v2check2_native.csv`, `v2check2_p13.csv` | wiersze identyczne bajtowo z `../native_audit/e2_native.csv` i `e2_p13.csv` |

## Uwaga o współdzielonej nazwie pliku tymczasowego (v1)

- `wuxu_subedge_variant_boundary.jl` (v1, commit `16db2b1`) zapisuje wariant źródła do jednego pliku
  tymczasowego o stałej nazwie w katalogu autorów. Jest więc bezpieczny tylko przy przebiegach sekwencyjnych.
- Wszystkie przebiegi produkcyjne E2, E5 i E5b były sekwencyjne (chronologia w `../native_audit/RUNLOG.md`).
  Równolegle szły tylko przebiegi innych skryptów o innych nazwach plików.
- `v2` nadaje nazwy z PID.
