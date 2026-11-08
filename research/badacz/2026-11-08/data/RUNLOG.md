---
artifact_id: IW_BADACZ_WUXU_BAND_KERNEL_RUNLOG_20261108
exposure: PUBLIC
claim_ceiling: PROVENANCE_LOG / NO_RESULT_BEYOND_LINKED_REVIEWS / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-08
origin_cell: BADACZ (wątek Claude)
document_type: RUNLOG
---

# RUNLOG — PREREG_048 / REVIEW_050 oraz REVIEW_049 (8 XI 2026)

**Środowisko:** jak w `research/badacz/2026-10-31/data/native_audit/RUNLOG.md`.
- Julia 1.12.3, kod autorów `d395183`, 2 rdzenie, 8 GB RAM.
- Python 3, sympy 1.13.3, numpy 2.1.3.

| czas (CET) | przebieg | plik | uwagi |
|---|---|---|---|
| ~09:05 | kontrola tożsamości sterownika (`k = 1`, 3 punkty, `j = 22`) | `identity.csv` | `Y_C` identyczne bitowo z `research/badacz/2026-11-02/data/grid_native.csv` (2 punkty); przed preregiem |
| ~09:07 | udziały liczbowe pasm | `band_number_shares.json` | z tabeli autorów; przed preregiem |
| 09:08 | PREREG_048 opublikowany (`b7a2c14`) | — | przed przebiegami produkcyjnymi |
| 09:09– | produkcja: 32 konfiguracje, 2 procesy (`w1`: `j = 22, 62`; `w2`: `j = 28, 34`) | `kernel_w1.csv`, `kernel_w2.csv` | tolerancja domyślna |
| ~09:12 | REVIEW_049: ślady Diraca i sumy spinorowe | `appendixB_dirac_trace_check.json` | niezależne od przebiegów Julii |
