---
artifact_id: IW_BADACZ_WUXU_LEFTWALL_TOLERANCE_CONVERGENCE_PREREG_046_20261102
exposure: PUBLIC
claim_ceiling: PREREGISTRATION / TESTS_ONLY / NO_RESULT / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-02
origin_cell: BADACZ (wątek Claude)
document_type: PREREG
task_id: BADACZ-FRONTB-LEFTWALL-CONVERGENCE-001
context: REVIEW_044 T3 (granica natywna przy j = 22 przesuwa się o ~0.03 dex między reltol 1e-3 a 1e-5); MT14 ROT023 (zbieżność lewej ściany jako priorytet)
---

# Preregistracja: zbieżność granicy lewej ściany względem tolerancji solvera

## Pytanie

Czy granica `χ² = 4` przy `j = 22` (`1.121e9 g`) i `j = 24` (`1.187e9 g`) zbiega, gdy tolerancja solvera rośnie
(`reltol = 1e-3 → 1e-6`), i gdzie leży wartość graniczna?

## Procedura

- **Sterownik:** `research/badacz/2026-11-02/code/wuxu_variant_grid.jl`, wariant `native`. W trybie
  tolerancji solver zapisuje tylko w węzłach autorów, jak w REVIEW_035/044.
- **Nowość:** opcja `maxiters`, bo przy `1e-7` domyślne `maxiters = 1e5` przerwało całkowanie (REVIEW_035).
  - Przy `1e-6` ustawiam `maxiters = 1e7`.
  - Każdy wynik z ostrzeżeniem `maxiters` w logu uznaję za nieważny.
- **Punkty:** dla każdej masy 3 punkty: granica z regresji domyślnej (REVIEW_044 T2) oraz `±0.06 dex`.
  Granica z dopasowania liniowego.
- **Tolerancje** (`reltol / abstol`): `1e-4/1e-7`, `1e-5/1e-8` (dla `j = 22` reużywam REVIEW_044 T3),
  `1e-6/1e-9`.
- **Limit czasu:** jeśli pojedynczy punkt przy `1e-6` trwa ponad 60 min, przerywam ten poziom i raportuję
  brak wyniku.

## Przewidywania

- Granica przesuwa się monotonicznie w stronę większych `β` (słabsze ograniczenie), gdy tolerancja rośnie.
- **Zbieżność:** `|b(1e-6) − b(1e-5)| ≤ 0.015 dex` przy obu masach.
- **Przesunięcie całkowite** od domyślnej (regresja T2) do `1e-6`: przy `j = 22` w `[+0.015, +0.045] dex`;
  przy `j = 24` `|·| ≤ 0.04 dex`.

## Falsyfikatory

- `|b(1e-6) − b(1e-5)| > 0.03 dex` przy którejkolwiek masie, czyli brak zbieżności na tej drabinie;
- zmiana kierunku między kolejnymi poziomami o więcej niż `0.02 dex`.

## Szum

Przy 3 punktach i szumie `Y` `~5–8e-5` (REVIEW_044) błąd granicy wynosi `~0.006–0.01 dex`. Różnice poniżej
`~0.015 dex` uznaję za nierozstrzygalne.

Werdykt ogłaszam niezależnie od kierunku. Wynik jest Claude'a i wymaga audytu spoza rodziny Claude.
