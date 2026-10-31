---
artifact_id: IW_BADACZ_WUXU_NATIVE_AUDIT_RUNLOG_20261031
exposure: PUBLIC
claim_ceiling: PROVENANCE_LOG / NO_RESULT_BEYOND_LINKED_REVIEWS / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-31
origin_cell: BADACZ (wątek Claude)
document_type: RUNLOG
---

# RUNLOG — przebiegi natywne Wu–Xu, 31 X 2026 (Badacz)

Środowisko: kontener Linux, 2 rdzenie, 8 GB RAM. Julia 1.12.3, pakiety najwyższego poziomu jak w
`research/mech-s6/2026-10-18/wuxu_dynamic_comparator/setup_env.jl`. Kod autorów: `d395183`.

## Chronologia (CET)

| czas | przebieg | plik wynikowy | uwagi |
|---|---|---|---|
| 14:53 | test dymny, 1 punkt (`default`) | — | wynik identyczny z wierszem `band,26,63` w `default_w2.csv` |
| 14:57–14:58 | N2, 74 punkty, 2 procesy (`default`) | `default_w1.csv`, `default_w2.csv` | — |
| 14:58–15:31 | N5, `tight` (`1e-10/1e-12`), zapis gęsty | — | **OOM** (`oom-kill`, anon-rss 3.6 GB), bez ukończonego punktu |
| 15:04–15:11 | drabina `1e-6/1e-8`, zapis gęsty | — | przerwana ręcznie (zwolnienie rdzenia dla E2), bez ukończonego punktu |
| 15:11–15:55 | E2: `native` (15:11–15:26), `ols8` (15:27–15:42), `zero` (15:42–15:55) | `e2_native.csv`, `e2_ols8.csv`, `e2_zero.csv` | — |
| 15:31–15:33 | drabina `1e-3/1e-6` + `saveat` (kontrola zapisu) | `n5_ladder_1e-3_1e-6.csv` | — |
| 15:33–15:53 | drabina `1e-5/1e-8` + `saveat` | `n5_ladder_1e-5_1e-8.csv` | około 400 s na punkt |
| 15:54–16:58 | drabina `1e-7/1e-10` + `saveat` | `n5_ladder_1e-7_1e-10_INVALID_maxiters.csv` | pierwszy punkt po 3802 s: `Y_P = 2.0`, w logu „Interrupted. Larger maxiters is needed” (wynik nieważny); dalsze punkty przerwane SIGINT 16:58 |
| 15:55–16:11 | E5: `native_sym` | `e5_native_sym.csv` | — |
| 16:11–16:22 | pełny ponowny przebieg `native` (kontrola determinizmu) | — | przerwany ręcznie, by zwolnić rdzeń; zastąpiony przebiegiem na 2 masach |
| 16:22–16:24 | diagnostyka czasu lewej ściany | `leftwall_timing.csv` | — |
| 16:24–16:40 | E5b: `native_nsym` | `e5b_native_nsym.csv` | — |
| 16:40–16:42 | kontrola determinizmu, `native`, masy 22 i 62 (wersja końcowa sterownika) | `e2_native_rerun2.csv` | wiersze identyczne bajtowo z `e2_native.csv` |
| 16:42–16:43 | kontrola determinizmu, `default`, 2 punkty (wersja końcowa `wuxu_native_audit.jl`) | `default_rerun2.csv` (punkty: `det2.dat`) | nagłówek i kolumny poza `seconds` identyczne z `default_w*.csv` |
| 16:56–16:57 | kontrola międzyśrodowiskowa: skrypt Mech-S6 `run_one_point.jl`, `6e9 g`, `β = 1e-16` | `mechs6_runner_6e9_1e-16_summary_current.dat` | `Y_P` identyczne bit w bit z wartością Mech-S6 z GitHub Actions (18 X) |

## Wersje skryptów

Skrypty w `../../code/` są w wersjach końcowych. W trakcie dnia dodawałem gałęzie:
- w `wuxu_native_audit.jl`: tryb `ladder` i `saveat`;
- w `wuxu_subedge_variant_boundary.jl`: `_sym`, `_nsym`.

Ścieżki `default`, `native`, `ols8` i `zero` nie zmieniły się od pierwszego użycia. Sprawdzają to
`e2_native_rerun2.csv` i `default_rerun2.csv` (wersje końcowe) wobec plików z pierwszych przebiegów.
Wyniki są deterministyczne.

Pliki `analysis.json` i `e2_e5_analysis.json` wygenerowano wersjami końcowymi skryptów analizy z tych CSV.
