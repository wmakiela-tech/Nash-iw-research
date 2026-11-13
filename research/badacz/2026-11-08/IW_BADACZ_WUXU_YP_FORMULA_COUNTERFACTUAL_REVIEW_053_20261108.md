---
artifact_id: IW_BADACZ_WUXU_YP_FORMULA_COUNTERFACTUAL_REVIEW_053_20261108
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude)
created_at: 2026-11-08
document_type: REVIEW
preregistration: IW_BADACZ_WUXU_YP_FORMULA_COUNTERFACTUAL_PREREG_051_20261108 (102e9d2, przed przebiegami)
responds_to: AUD1-ROT032-WUXU-FIG5-NOTEBOOK-YHE4-OWNER-DISPOSITION-001_20261108
code: code/wuxu_yp_formula_counterfactual.jl, code/wuxu_yp_formula_counterfactual_analysis.py
data: data/yp051/ (yp_a.csv, yp_b.csv, yp_c.csv, configs_*.dat, yp051_analysis.json)
claim_ceiling: MODEL_INTERNAL_COUNTERFACTUAL / NO_PBH_BOUND / NO_FIG5_IDENTITY / NO_OWNER_DISPOSITION / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
revision: r2 (13 XI 2026) — dodana sekcja „Erratum (13 XI)” na końcu; treść r1 bez zmian
---

# REVIEW_053: poprawiony wzór Y_P przesuwa natywny kontur o +0.03…+0.08 dex (V1) albo +0.09…+0.19 dex (V2) dla 1.1–3.5e9 g; przy 1e10 g warianty się rozchodzą

**Rola:** Badacz. To pomiar wspierający dyspozycję Mech-S8 jako właściciela. Wyboru poprawki za właściciela nie dokonuję.

## 1. Źródło: AUD1 ma rację co do wzoru

- **Co przechowuje X.** W `magic()` (`main-scan.jl`, commit autorów `d395183`) zmienna X to ułamek `n/(n+p)`:
  - wartość początkowa `1/(1+exp(Q/T))`;
  - człon rozpadu `−X/τ_n`.
- **Wzór.** Wiersz 210 zwraca `2X/(1−X) = 2n/p`. Ułamek masowy helu przy tej definicji to `≈ 2X`, tak jak w arXiv v3.
- **Kalibracja w moim środowisku** (β = 1e−30):
  - `Y_code,SBBN = 0.244765` (j = 22) i `0.244750` (j = 62);
  - `2X_SBBN(T_nuc) = 0.21808`.
  Kod jest więc skalibrowany na ≈ 0.245 przy błędnym wzorze, a poprawny wzór przy tym samym `T_nuc` daje SBBN ≈ 0.218. To zgadza się z mapowaniem AUD1 (0.245 → 0.218263).
- **Ponowna kalibracja.** Warunek `2X_SBBN(T1) = 0.245` wymaga `T1 = 0.099689 MeV` (wobec `T_nuc = 0.078185 MeV`). W przybliżeniu ery radiacji to czas krótszy o czynnik ≈ 0.62.

## 2. Wynik natywny

Wszystkie warianty pochodzą z tego samego, niezmienionego rozwiązania ODE autorów.

| j | m [g] | V0 (natywny) | V1: 2X(T1) = 0.251 | V2: 2X(T0) − 2X_SBBN = 0.006 | przesunięcie V1 | przesunięcie V2 | P1: V1 − V1p |
|---|---|---|---|---|---|---|---|
| 22 | 1.121e9 | −17.215 | −17.140 | −17.021 | **+0.075** | **+0.194** | +0.001 |
| 28 | 1.330e9 | −18.356 | −18.320 | −18.261 | +0.036 | +0.095 | −0.002 |
| 34 | 1.577e9 | −18.831 | −18.793 | −18.743 | +0.038 | +0.088 | +0.003 |
| 62 | 3.494e9 | −19.389 | −19.355 | −19.302 | +0.034 | +0.087 | −0.001 |
| 99 | 1.000e10 (eksploracja) | −19.224 | −18.884 | −19.139 | **+0.340** | +0.085 | **+0.306** |

**Niepewność.** Dodatkowa ocena post hoc, nieujęta w preregu: rozrzut punktów wokół gładkiej krzywej daje ±0.011–0.013 dex na korzeń przy j = 22, gdzie kontur jest płaski (nachylenie 0.0069 na dex). Dla pozostałych mas ±0.002–0.004 dex. Wkład numeryczny metody korzenia ≤ 0.004 dex.

## 3. Werdykty preregu

- **I0: PASS.** Tożsamość wyniku `magic()` z odtworzonym wzorem: błąd względny 0. Korzenie V0 zgadzają się z REVIEW_050 w granicach +0.003…+0.005 dex.
- **C1: FAIL formalny w jednym podpunkcie.** Spełnione: `Y_code,SBBN ∈ [0.244, 0.246]` oraz `T1 > T0`. Niespełnione: `X0s` przy j = 22 i 62 różni się o `5.9e−6` przy progu `1e−6`. To szum ścieżki solvera przy domyślnej tolerancji (inny moment startu dla innej masy). Wpływ na korzenie ≈ 0.001 dex. Próg był za ostry; przesłanka AUD1 o kalibracji do ≈ 0.245 zachodzi.
- **P1 (skalowanie „tylko rozpad”): PASS**, 4/4 masy, `|V1 − V1p| ≤ 0.003 dex`. Iloraz `X(T1)/X(T0)` mieści się w przedziale 1.1230–1.1240 we wszystkich 36 punktach j = 22–62; wartość SBBN to 1.1235.
- **P2: FAIL dla obu wariantów, tylko przez j = 22.**
  - V1 +0.075 przy oknie `[+0.08, +0.15]`; V2 +0.194 przy oknie `[+0.20, +0.30]`. Pozostałe trzy masy mieszczą się w oknach obu wariantów.
  - Przyczyna, ustalona post hoc: okna liczyłem przy nominalnym `X0s = 0.245/2.245`, a zmierzone SBBN daje 0.24476. To obniża progi.
  - Te same stare punkty REVIEW_050 przy zmierzonym `X0s` dają +0.055 (V1) i +0.210 (V2). Obie wartości różnią się od nowego pomiaru o mniej niż 2σ szumu przy j = 22. Werdykt zostaje FAIL.
- **E1 (j = 99, eksploracja): skalowanie zawodzi**, jak przewidywałem: +0.31 dex. Przy 1e10 g czas życia (≈ 238 s) jest porównywalny z czasem `T_nuc`. Iloraz `X(T1)/X(T0)` spada wraz z β od 1.123 do 0.82 (skan do β = 1e−17), bo hadrony wstrzykiwane po T1 liczą się w V0 i V2, a w V1 już nie.

## 4. Co z tego wynika dla dyspozycji właściciela

1. **Wada źródła jest realna**, ale rozłączność przedziałów `Y` (AUD1) nie przekłada się na duże przesunięcie konturu.
   - Po kalibracji test χ² działa w praktyce różnicowo.
   - Przy poprawnym wzorze zmienia się wymagane `ΔX` (mierzone przy T0). Względem V0 rośnie o czynnik 1.082 w V1 i 1.216 w V2. Przy odpowiedzi liniowej daje to `log10` z tych czynników: +0.034 i +0.085 dex. Zgadza się to z j = 28–62.
   - Dla mas wyparowujących dużo przed T_nuc daje to przesunięcie lewej części konturu w stronę słabszego ograniczenia: +0.03…+0.08 dex (V1) albo +0.09…+0.19 dex (V2). Największe jest przy j = 22, bo tam odpowiedź jest najbardziej nasycona.
2. **Skala wobec innych systematyk.** Mniej niż B_sym (+0.27…+0.30 dex), więcej niż tolerancja solvera (+0.01…+0.03 dex), porównywalnie z podmianą ekstrapolacji poniżej 1e9 g (−0.03…−0.055 dex, REVIEW_042). Kierunki są różne. Nie sumuję tego mechanicznie.
3. **Wybór poprawki ma znaczenie na ciężkim końcu.** Przy 1e10 g V1 daje +0.34 dex, a V2 +0.085 dex. V1 przesuwa „chwilę nukleosyntezy” na 0.0997 MeV i pomija hadrony wstrzyknięte między T1 a T0. To może być fizycznie wątpliwe dla mas, których wybuch nakłada się na BBN. To uwaga do decyzji, nie rozstrzygnięcie.
4. **Reguła praktyczna (sprawdzona przez P1).** Dla mas wyparowujących przed T1 kontur V1 nie wymaga nowego przebiegu. Wystarczy odczytać natywny kontur przy progu `Y_code* = 2x*/(1−x*)`, gdzie `x* = 0.1255·X0s/X1s`, czyli `Y_code* = 0.25151` dla mojego `X0s`. Kontur V2 odczytuje się wprost z `Y_code` przy `X* = X0s + 0.003` (`Y_code* = 0.25235`). Dla mas ciężkich, z wybuchem w trakcie BBN, ta reguła nie działa (E1).
5. **Pytanie do właściciela, nie teza.** `X_SBBN(T_nuc) = 0.109` w tym kodzie oznacza, że poprawność `Y ≈ 0.245` przy `T_nuc = 0.078 MeV` zależy od błędnego wzoru. Czy sama fizyka konwersji n↔p w `magic()` daje oczekiwany ułamek neutronów przy nukleosyntezie? Tego nie badałem.

## 5. Czego ten test nie robi

- Nie sprawdza oryginalnych macierzy JLD2 ani tożsamości wydania, które wygenerowało Fig. 5. To zadanie z prośby AUD1 do Mech-S8.
- Nie daje fizycznej granicy PBH.
- Nie wybiera wariantu poprawki.
- Działa tylko w kodzie v2 przy domyślnej tolerancji, mapie B_exec autorów i ich ekstrapolacji poniżej 1e9 g.

## 6. Odtworzenie

```text
julia --project=<env> code/wuxu_yp_formula_counterfactual.jl <arXiv-2509.05618 autorów @ d395183> data/yp051/yp_a.csv data/yp051/configs_a.dat   # oraz _b, _c
python3 -I code/wuxu_yp_formula_counterfactual_analysis.py data/yp051 data/kernel_analysis.json data/yp051/yp051_analysis.json
```

Około 4 minut na 2 rdzeniach.

## 7. Powrót w trzech warstwach

- **Wynik:**
  - wada wzoru potwierdzona w źródle;
  - natywny wpływ na kontur zmierzony: +0.03…+0.19 dex dla 1.1–3.5e9 g, zależnie od wariantu; przy 1e10 g +0.09 albo +0.34 dex;
  - skalowanie „tylko rozpad” potwierdzone dla mas lekkich i obalone dla 1e10 g;
  - P2 FAIL przy j = 22 przez założenie nominalnego SBBN.
- **Konfiguracja:**
  - kontrfaktyk liczy się z jednego rozwiązania ODE, więc był tani: 4 min wobec godzin przy jądrze pasm;
  - przewidywanie V2 było w pełni wyznaczone przez stare dane i powiedziałem to w preregu. Prawdziwym testem był P1.
- **Uczenie systemu:**
  - `origin_failure_mode: NOMINAL_CALIBRATION_IN_PREDICTION_WINDOW`: okna przewidywań oparte na wartości nominalnej (0.245) zamiast na wielkości mierzalnej przed testem (SBBN w tym samym środowisku). Łatka: kalibrację mierzyć przed preregiem, gdy nie ujawnia wyniku testu, albo wyrażać okna jawnie jako funkcję kalibracji.
  - Mój błąd uruchomienia (`&` w poleceniu tła) powtórzył się drugi raz dziś. Procesy zginęły przed zapisem danych, bez wpływu na wynik. Łatka: zawsze jedno polecenie tła z `wait`.
  - Przy okazji zauważyłem, że w łańcuchach `cmd | tail` kod wyjścia preflightu jest maskowany. Preflight dla preregu 051 powtórzyłem z jawnym kodem wyjścia: PASS.

## Erratum (13 XI 2026, po replice GPT i REVIEW_065)

- **Korzeń V2 przy j = 22 był obciążony metodą.** Korzeń −17.021 i przesunięcie V2 − V0 = +0.194 policzyłem kwadratową przez 4 punkty siatki o kroku 0.075 dex.
  - Na siatce gęstej (0.02 dex) przy tej samej, domyślnej tolerancji wychodzi −16.990 … −16.999 i +0.223 … +0.226.
  - Zgadza się to z natywną repliką GPT (L2: −16.9975 i +0.2266).
  - Przy `1e−4` wychodzi +0.244 … +0.253.
  - Aktualny przedział dla j = 22: V2 − V0 = **+0.22 … +0.25 dex**, V1 − V0 = **+0.07 … +0.095 dex**.
- **Niepewność.** Moja miara niepewności |kwadratowa − liniowa| na tych samych punktach nie mogła tego wykryć.
- **Inne masy.** j = 28 i 34 nie są ponownie sprawdzone (OTWARTE); j = 62 przeszło w L2.
- Szczegóły: `research/badacz/2026-11-13/IW_BADACZ_WUXU_REVIEW053_J22_ROOT_METHOD_TOLERANCE_REVIEW_065_20261113.md`.
- `origin_failure_mode: COARSE_GRID_ROOT_ON_CURVED_JAGGED_RESPONSE`.
