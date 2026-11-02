---
artifact_id: IW_BADACZ_WUXU_LEFTWALL_CONVERGENCE_RUNLOG_20261102
exposure: PUBLIC
claim_ceiling: PROVENANCE_LOG / NO_RESULT_BEYOND_LINKED_REVIEW / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-02
origin_cell: BADACZ (wątek Claude)
document_type: RUNLOG
---

# RUNLOG — PREREG_046 / REVIEW_047 (2 XI 2026, popołudnie)

Sterownik `code/wuxu_variant_grid_v2.jl`, wariant `native`, kod autorów `d395183`, Julia 1.12.3, 2 rdzenie.

| czas (CET) | przebieg | plik | uwagi |
|---|---|---|---|
| 13:24 | PREREG_046 opublikowany (`f720f80`) | — | przed przebiegami |
| 13:25–13:29 | `1e-4/1e-7`, `j = 22`, 3 pkt (z kompilacją) | `t4_j22.csv` | około 40 s na punkt |
| 13:29–13:31 | `1e-4/1e-7`, `j = 24`, 3 pkt | `t4_j24.csv` | — |
| 13:25–13:45 | `1e-5/1e-8`, `j = 24`, 3 pkt | `t5_j24.csv` | około 380 s na punkt |
| 13:31–14:33 | `1e-6/1e-9`, `maxiters = 1e7`, `j = 22` | — | **przerwany** (limit 60 min na punkt z preregu), bez punktu, bez ostrzeżeń `maxiters` |
| 13:45–14:46 | `1e-6/1e-9`, `maxiters = 1e7`, `j = 24` | — | **przerwany** jak wyżej |
| 14:50 | analiza | `convergence.json` | `1e-5` dla `j = 22` z `../tol_native.csv` (REVIEW_044 T3) |
