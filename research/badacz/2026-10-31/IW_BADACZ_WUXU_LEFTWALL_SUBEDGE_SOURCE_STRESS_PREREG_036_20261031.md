---
artifact_id: IW_BADACZ_WUXU_LEFTWALL_SUBEDGE_SOURCE_STRESS_PREREG_036_20261031
exposure: PUBLIC
claim_ceiling: PREREGISTRATION / TESTS_ONLY / NO_RESULT / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-31
origin_cell: BADACZ (wątek Claude)
document_type: PREREG
task_id: BADACZ-FRONTB-SUBEDGE-STRESS-001
owner_of_physics: Mech-S7 (źródło i dynamika Front B); ten test jest wsparciem krzyżowym, nie przejęciem linii
---

# Preregistracja E2: czułość lewej ściany Fig. 5 na prawo emisji hadronów poniżej 1e9 g (kod natywny)

## Pytanie

- Tabela hadronów autorów zaczyna się przy `1e9 g`. Poniżej kod ekstrapoluje log-log nachyleniem z dwóch
  pierwszych wierszy (`s ≈ −1.20`).
- Na lewej ścianie konturu (`m ≈ 1.1–2·10⁹ g`) poniżej krawędzi wypromieniowuje się ułamek `1e9 g/m`
  masy, czyli 50–89%. Ta emisja przypada na koniec parowania, blisko zamrożenia `n/p`, kiedy wstrzyknięte
  hadrony najtrudniej wymyć.
- Mech-S7 ROT036 pokazał w warunkowym modelu 7D przy `6e9 g`, że inne nachylenie (OLS z 8 wierszy) zmienia
  `X_nuc` o `~2e-5`. Pytanie: **o ile przesuwa się kontur `χ² = 4` w natywnym kodzie 10D, zwłaszcza na lewej
  ścianie?**

## Warianty źródła (tylko poniżej pierwszego wiersza tabeli, `m < m₁ = 1e9 g`)

- **V0 (natywny):** kod autorów bez zmian.
- **V1 (OLS-8, jak Mech-S7 ROT036):** `Q_i(m) = Q_i(m₁)·(m/m₁)^{s_i⁽⁸⁾}`, gdzie `s_i⁽⁸⁾` to nachylenie OLS
  `log Q` wobec `log m` z pierwszych 8 wierszy. Sprawdzam zgodność `s_i⁽⁸⁾` z tabelą Mech-S7 do `1e-6`.
- **V2 (zero poniżej krawędzi):** `Q_i(m) = 0` dla `m < m₁`. To nie jest wariant fizyczny, tylko miara,
  jaką część ograniczenia niesie emisja ekstrapolowana.

Powyżej `m₁` wszystkie warianty są identyczne z autorami. Ewolucja masy PBH się nie zmienia.

## Procedura

- 12 mas z PREREG_034 (`m = 1.121 … 7.743·10⁹ g`).
- Granica `Y_C = 0.251` (`χ² = 4`, obserwabla autorów `2X/(1 − X)` przy ich `T_nuc`), wyznaczana bisekcją
  w `log₁₀ β` na przedziale `[−21, −15]` do `0.005 dex`. Domyślne tolerancje solvera, `num_points = 10000`.
- Kontrola metody: V0 z bisekcji ma się zgadzać z granicą natywną z REVIEW_035 (interpolacja w oknie)
  do `0.01 dex`.
- Poziom szumu numerycznego: granica natywna różni się od zapisanej o `≤ 0.013 dex` (REVIEW_035). Za
  rozstrzygalne uznaję przesunięcia `> 0.03 dex`.

## Oczekiwania i falsyfikatory

- **V1:** bardziej strome nachylenie daje więcej hadronów poniżej krawędzi (całka `∝ 1/(3 + s)`,
  `+4%`), więc ograniczenie się wzmacnia (granica w stronę mniejszych `β`). Spodziewam się
  `|przesunięcie| ≤ 0.05 dex` wszędzie.
  - **Falsyfikator:** przeciwny kierunek przy przesunięciu `> 0.03 dex` w którejkolwiek masie albo
    `|przesunięcie| > 0.1 dex`.
- **V2:** ograniczenie słabnie najsilniej na lewej ścianie. Spodziewam się przesunięcia `> 0.3 dex`
  (albo braku granicy w `[−21, −15]`) przy `1.12e9 g` i malejącego z masą, `< 0.1 dex` dla
  `m ≥ 3.5·10⁹ g`.
  - **Falsyfikator:** przesunięcie `< 0.1 dex` przy `1.12e9 g` (wtedy emisja ekstrapolowana nie niesie
    lewej ściany) albo `> 0.3 dex` przy `m ≥ 3.5·10⁹ g`.
- **Diagnostyka czasu (post hoc, bez progów):** temperatura SM, gdy masa PBH przekracza `1e9 g`, i gdy
  zostaje `0.1%` masy, dla 12 mas na granicy natywnej.

Werdykt każdego testu ogłaszam niezależnie od kierunku. Wynik nie jest granicą fizyczną: fizyczne widmo
hadronów poniżej `1e9 g` pozostaje nieznane (Mech-S7 ROT036, E4). Wynik jest Claude'a i wymaga audytu spoza
rodziny Claude.
