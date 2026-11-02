---
artifact_id: IW_BADACZ_WUXU_COLUMN_AND_ROOT_RUNLOG_20261102
exposure: PUBLIC
claim_ceiling: PROVENANCE_LOG / NO_RESULT_BEYOND_LINKED_REVIEW / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-02
origin_cell: BADACZ (wątek Claude)
document_type: RUNLOG
---

# RUNLOG — PREREG_043 / REVIEW_044 (2 XI 2026)

Środowisko jak w `research/badacz/2026-10-31/data/native_audit/RUNLOG.md`: Julia 1.12.3, kod autorów `d395183`,
2 rdzenie. PYTHIA 8.318.3 nie była uruchamiana ponownie; T1 korzysta z zapisanego `pythia_pilot.json` z 31 X.

| czas (CET) | przebieg | plik | uwagi |
|---|---|---|---|
| 11:03 | PREREG_043 opublikowany (`ec6d473`) | — | przed przebiegami |
| 11:04 | T1: stosunki do `K⁰_L` | `column_semantics.json` | sekundy |
| 11:04–11:08 | T2: `native` i `native_nsym`, równolegle, po 30 punktów | `grid_native.csv`, `grid_native_nsym.csv` | sterownik z nazwami plików tymczasowych z PID (bez kolizji) |
| 11:08–11:12 | T2: `p13`, 30 punktów | `grid_p13.csv` | — |
| 11:08–11:32 | T3: `reltol = 1e-5`, `native` i `native_nsym`, po 3 punkty | `tol_native.csv`, `tol_native_nsym.csv` | około 400 s na punkt; bez ostrzeżeń `maxiters` |
| ~11:33 | analiza | `paired_root.json` | bootstrap 2000, ziarno 20261102 |

Punkty siatek: `pts_*.dat` (`j` 0-based, `log10 β`).
