---
artifact_id: IW_BADACZ_RUNLOG_20261113
exposure: PUBLIC
claim_ceiling: PROVENANCE_LOG / NO_RESULT_BEYOND_LINKED_REVIEWS / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-13
origin_cell: BADACZ (wątek Claude)
document_type: RUNLOG
---

# RUNLOG — PREREG_064 (13 XI 2026; zegar kontenera = CET)

**Środowisko:** Julia 1.12.3 (`wuxu_env`), kod autorów `d395183`, 2 rdzenie; kontener uruchomiony ponownie 07:49 (pliki zachowane).

| czas | przebieg | plik | uwagi |
|---|---|---|---|
| 07:52 | PREREG_064, sterownik i konfiguracje zapisane przed przebiegiem | — | — |
| 07:53 | start PREREG_064: procesy 1–2 przy `1e−4:1e−7`, proces 3 (domyślna) po procesie 2; skrypt analizy zatwierdzony w trakcie, przed odczytem wyników | `yp064_tol_p1.csv`, `yp064_tol_p2.csv`, `yp064_default.csv` | równolegle kończy się powtórzenie części B PREREG_062 (3 procesy na 2 rdzeniach) |
| 07:52:58–08:13:42 | PREREG_064 ukończony: proces 2 (`1e−4`) 08:06:32, proces 3 (domyślna) 08:10:27, proces 1 (`1e−4`) 08:13:42; wszystkie kod 0; 25 + 15 + 31 punktów, bez braków | `yp064_tol_p1.csv`, `yp064_tol_p2.csv`, `yp064_default.csv` | kalibracja SBBN identyczna w obu procesach `1e−4` (X0s 0.10906943155, T1 0.099655548288) |
| ~08:15 | analiza preregu (skrypt z `f7b5407`, bez zmian) | `analysis064.json` | werdykt J0 |
| ~08:18 | post hoc: rozrzut tylko metod gęstych i zamiana kalibracji X0s między tolerancjami | `posthoc064_decomp.json` | `code/wuxu_064_posthoc_decomp.py`; poza preregiem |
