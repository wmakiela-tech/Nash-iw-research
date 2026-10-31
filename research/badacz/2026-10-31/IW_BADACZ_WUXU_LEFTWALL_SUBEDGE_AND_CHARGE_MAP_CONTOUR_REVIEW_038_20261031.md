---
artifact_id: IW_BADACZ_WUXU_LEFTWALL_SUBEDGE_AND_CHARGE_MAP_CONTOUR_REVIEW_038_20261031
exposure: PUBLIC
claim_ceiling: CONDITIONAL_SENSITIVITY_[▷] / AUTHOR_NATIVE_CODE_WITH_DECLARED_SOURCE_VARIANTS / NOT_A_PHYSICAL_SPECTRUM / NO_PBH_BOUND / NO_VERDICT_ON_PUBLISHED_FIGURE / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-31
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-FRONTB-SUBEDGE-STRESS-001; BADACZ-FRONTB-CHARGE-MAP-CONTOUR-001/002
prereg: PREREG_036 (commit 61bfd3f, E2), PREREG_037 (commit 52f597f, E5), PREREG_040 (commit 04cb097, E5b); każdy przed swoim przebiegiem
owner_of_physics: Mech-S7 (linia źródła i dynamiki Front B); kontrakt symetrii źródła: Rec9
code: research/badacz/2026-10-31/code/wuxu_subedge_variant_boundary.jl; wuxu_e2_e5_analysis.py; wuxu_leftwall_timing.jl
outputs: research/badacz/2026-10-31/data/native_audit/ (e2_*.csv, e5_*.csv, leftwall_timing.csv, e2_e5_analysis.json, MANIFEST_SHA256.md)
---

# Lewa ściana Fig. 5 i mapa ładunkowa: testy natywnym kodem (E2, E5, E5b)

**Status:** `[▷]`. Warianty źródła wstawione do kodu autorów to testy czułości, nie fizyczne widma ani
granice PBH. Wynik Claude'a, wymaga audytu spoza rodziny Claude.

## Wynik

1. **Lewą ścianę niesie w całości emisja ekstrapolowana poniżej tabeli (E2, V2).** Po wyzerowaniu źródła
   hadronów poniżej `1e9 g` masy `1.12–1.26e9 g` nie mają granicy aż do `β = 1e-15` (przesunięcie
   `> 2.2 dex`). Przy `1.33e9 g` granica przesuwa się o `+2.28 dex`. Efekt maleje z masą do `+0.01–0.02 dex`
   przy `5.8–7.7e9 g`.
2. **Kształt ekstrapolacji w rodzinie potęgowej ma mały wpływ (E2, V1).** Nachylenie OLS z 8 wierszy
   (Mech-S7 ROT036) zamiast z 2 wzmacnia ograniczenie o `0.017–0.041 dex` przy `m ≤ 1.58e9 g`. Dla cięższych
   mas wpływ jest w granicach szumu (`≤ 0.004 dex`).
3. **Mapa ładunkowa jest istotna dla konturu (E5).** `B_sym` (połowa czterech zagregowanych kolumn)
   przesuwa granicę o `+0.27…+0.30 dex` we wszystkich 12 masach, czyli osłabia ograniczenie `1.85–2.0`
   razy w `β`. To blisko `log₁₀ 2 = 0.30 dex`, czyli odpowiedzi liniowej.
4. **Część poparta źródłem (E5b, tylko nukleony).** Połowa źródła `p + p̄` i `n + n̄` (Rec9: poparta wprost
   tekstem autorów) przesuwa granicę o `+0.06` na lewej ścianie i rośnie do `+0.30 dex` przy `7.7e9 g`.
   - Przewidywanie z preregu, z liniowej superpozycji skanów v1 i v2 autorów, zgadza się do `≤ 0.005 dex`
     dla `m ≥ 1.45e9 g`; maksymalne odchylenie to `0.040` przy `1.12e9 g`.
   - Dla `m ≳ 3e9 g` sam podział nukleonów niesie 90–99% pełnego przesunięcia `B_sym`.

## E2: prawo emisji poniżej `1e9 g`

Granica `Y_C = 0.251` (`χ² = 4`, obserwabla autorów), bisekcja w `log₁₀ β` na `[−21, −15]`.
Przesunięcie to wariant minus natywny; plus oznacza słabsze ograniczenie.

| `m` [g] | `1e9 g/m` | natywna | kontrola: bisekcja − okno (REVIEW_035) | V1 (OLS-8) | V2 (zero) |
|---|---:|---:|---:|---:|---:|
| 1.121e9 | 0.89 | −17.227 | −0.007 | −0.029 | brak granicy (> +2.23) |
| 1.187e9 | 0.84 | −17.765 | +0.012 | −0.041 | brak granicy (> +2.77) |
| 1.256e9 | 0.80 | −18.110 | −0.013 | −0.024 | brak granicy (> +3.11) |
| 1.330e9 | 0.75 | −18.362 | +0.004 | −0.017 | +2.281 |
| 1.448e9 | 0.69 | −18.621 | +0.011 | −0.029 | +0.951 |
| 1.577e9 | 0.63 | −18.820 | +0.002 | −0.022 | +0.598 |
| 1.767e9 | 0.57 | −19.012 | +0.002 | −0.002 | +0.368 |
| 2.036e9 | 0.49 | −19.159 | −0.004 | −0.003 | +0.224 |
| 2.556e9 | 0.39 | −19.296 | −0.002 | −0.004 | +0.116 |
| 3.494e9 | 0.29 | −19.390 | +0.007 | −0.004 | +0.056 |
| 5.828e9 | 0.17 | −19.399 | −0.004 | −0.000 | +0.019 |
| 7.743e9 | 0.13 | −19.366 | −0.002 | −0.001 | +0.013 |

- **Werdykty:**
  - **V1:** nie sfalsyfikowany. Kierunek zgodny z oczekiwaniem, maksimum `0.041 dex < 0.1`.
  - **V2:** nie sfalsyfikowany. Przy `1.12e9 g` przesunięcie `> 2.2 dex` (falsyfikator: `< 0.1`). Dla
    `m ≥ 3.5e9 g`: `+0.019` i `+0.013`; z masą `3.494e9 g` także `+0.056`. Wszystkie `< 0.3`.
  - **Kontrola metody:** w 3 z 12 mas przekracza preregowany próg `0.01 dex` (maks. `0.013`). Próg leżał
    poniżej szumu, który już znałem (`0.006` rms, `0.020` maks., REVIEW_035). Szczegóły w punkcie
    „Uczenie systemu”.
- **Czy V1 wystaje ponad szum?** Przy `m ≤ 1.58e9 g` wszystkie 6 przesunięć mają ten sam znak, średnio
  `−0.027 dex`. Szum różnicy dwóch przebiegów to około `0.009 dex` rms, więc średnia z 6 ma
  `σ ≈ 0.004 dex`. Efekt jest więc realny, ale mały.
- **Dlaczego lewa ściana zależy od emisji poniżej krawędzi** (diagnostyka czasu, post hoc, `magic()` bez
  zmian, punkt na granicy natywnej):

| `m` [g] | `T` SM, gdy masa PBH przechodzi `1e9 g` [MeV] | `T` przy 99,9% wyparowania [MeV] |
|---|---:|---:|
| 1.121e9 | 2.76 | 1.49 |
| 1.256e9 | 1.78 | 1.26 |
| 1.448e9 | 1.24 | 1.02 |
| 1.767e9 | 0.84 | 0.76 |
| 2.556e9 | 0.46 | 0.44 |
| 3.494e9 | 0.29 | 0.29 |
| 7.743e9 | 0.105 | 0.104 |

  - Na lewej ścianie PBH przechodzi krawędź tabeli przy `T = 1.2–2.8 MeV`, przed zamrożeniem `n/p`
    (`~0.8 MeV`). Hadrony z tabeli trafiają w okres, gdy oddziaływania słabe jeszcze wymywają ich wpływ na
    `X_n`.
  - Przetrwa tylko końcowa emisja, poniżej krawędzi, kończąca się przy `T ≈ 1.0–1.5 MeV`. Stąd V2 usuwa
    ograniczenie.
  - Dla `m ≥ 2.5e9 g` krawędź i koniec parowania wypadają prawie jednocześnie, po zamrożeniu. Emisja poniżej
    krawędzi to wtedy krótki końcowy błysk, a efekt niesie tabela.
  - Wiersz kontrolny (`9.73e8 g`, poniżej tabeli od początku) nie ma przejścia krawędzi. Kolumna
    `frac_mass_below_edge = 1e9 g/m` jest tam bez znaczenia.

## E5: mapa ładunkowa `B_sym`

Łatka Mech-S6 nałożona bez zmian (`π±`, `K±`, `p + p̄`, `n + n̄` × ½; `K⁰_L` bez zmian), prawo poniżej
krawędzi natywne.

| `m` [g] | 1.121e9 | 1.187e9 | 1.256e9 | 1.330e9 | 1.448e9 | 1.577e9 | 1.767e9 | 2.036e9 | 2.556e9 | 3.494e9 | 5.828e9 | 7.743e9 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| przesunięcie [dex] | +0.279 | +0.266 | +0.274 | +0.268 | +0.266 | +0.270 | +0.281 | +0.285 | +0.287 | +0.295 | +0.300 | +0.301 |

- **Werdykt:** nie sfalsyfikowany. Wszystkie przesunięcia mieszczą się w przedziale `0.15–0.30` (maks.
  `0.301`, w granicach szumu `~0.01` od górnej krawędzi). Nie ma przesunięcia `< 0.05`, `< 0` ani `> 0.40`.
- **Odpowiedź jest prawie liniowa:** przesunięcie dąży do `log₁₀ 2 = 0.301` tam, gdzie dominują nukleony
  (cięższe masy). Na lewej ścianie jest mniejsze o `~0.03`. Hipoteza `[▷]`, niesprawdzona: nie zmieniony `K⁰_L` ma tam
  większy udział.
- **W czynniku `β`:** `B_sym` osłabia ograniczenie `1.85–2.0` razy na całej badanej długości konturu.

## E5b: połowa tylko dla nukleonów

Tylko linie `p̄` i `n̄` w `main-scan.jl` dostają `× ½`; `π`, `K` i `K⁰_L` zostają jak u autorów.
Przewidywanie z PREREG_040 (commit `04cb097`): `−log₁₀(1 − w/2)`, gdzie `w = 1 − 10^(b_v2 − b_v1)` to udział
nukleonów z różnicy granic skanów v1 i v2.

| `m` [g] | obserwowane | przewidywane | różnica | E5b / E5 |
|---|---:|---:|---:|---:|
| 1.121e9 | +0.063 | +0.023 | +0.040 | 0.23 |
| 1.187e9 | +0.064 | +0.053 | +0.011 | 0.24 |
| 1.256e9 | +0.087 | +0.067 | +0.020 | 0.32 |
| 1.330e9 | +0.096 | +0.079 | +0.017 | 0.36 |
| 1.448e9 | +0.099 | +0.100 | −0.001 | 0.37 |
| 1.577e9 | +0.121 | +0.123 | −0.002 | 0.45 |
| 1.767e9 | +0.156 | +0.155 | +0.001 | 0.56 |
| 2.036e9 | +0.190 | +0.185 | +0.005 | 0.67 |
| 2.556e9 | +0.231 | +0.230 | +0.001 | 0.80 |
| 3.494e9 | +0.268 | +0.269 | −0.001 | 0.91 |
| 5.828e9 | +0.292 | +0.292 | −0.000 | 0.97 |
| 7.743e9 | +0.299 | +0.296 | +0.003 | 0.99 |

- **Werdykt:** nie sfalsyfikowany. Maksymalne odchylenie `0.040 < 0.1`, porządek zachowany.
- **Zgodność bliska szumowi** dla `m ≥ 1.45e9 g` potwierdza liniowy model odpowiedzi przy granicy. Model
  przeniesiony między dwiema wersjami kodu autorów przewiduje wariant, którego nie było w żadnej z nich.
- Na lewej ścianie przewidywanie jest za niskie o `0.01–0.04`. Zgodne z zastrzeżeniem z preregu: v1 różni
  się od v2 nie tylko nukleonami. Nie rozstrzygam.

## Co z tego wynika dla Fig. 5 (warunkowo)

Warunkowo na tym, że `scanning.jld2` przy `d395183` odpowiada opublikowanej figurze (niesprawdzone;
MT14 ROT016–018):

- **Dla `m ≳ 3e9 g`** ograniczenie zależy prawie wyłącznie od antynukleonów.
  - Kod wpisuje całe agregaty `p + p̄` i `n + n̄` do populacji `p̄` i `n̄`.
  - Jeśli kolumny tabeli są sumami cząstek i antycząstek (tak piszą autorzy; Rec9), wstrzyknięcie
    antynukleonów jest podwojone, a ograniczenie Fig. 5 w tym zakresie mas jest za silne o czynnik `≈ 1.9–2.0`
    w `β` (`0.27–0.30 dex`).
  - To największa ze zmierzonych tu poprawek wynikających z kontraktu kodu, poza samym istnieniem emisji
    poniżej `1e9 g`.
- **Na lewej ścianie** podział nukleonów daje `+0.06–0.10 dex`. Reszta pełnego `B_sym` (`~0.2 dex`)
  pochodzi z podziału `π±` i `K±`, który jest założeniem symetrii, nie stwierdzeniem źródła.
- **Położenie lewej ściany w masie** wyznacza emisja poniżej tabeli (V2). Kształt tej emisji w rodzinie
  potęgowej zmienia granicę o setne części dex (V1). Bez walidacji fizycznego widma przy `T_BH > 10 TeV`
  (E4) lewa ściana pozostaje przewidywaniem ekstrapolacji.
- **Żadna z tych liczb nie jest granicą PBH.** To przesunięcia konturu w modelu autorów przy zmianach
  kontraktu źródła.

## Czego nie sprawdziłem

- Fizycznego widma hadronów poniżej `1e9 g`. Tablice hadronizacji BlackHawk sięgają do około 100 TeV
  energii cząstki pierwotnej (Arbey & Auffinger, arXiv:2108.02737). Przy `1e9 g` temperatura
  `T_BH ≈ 10.6 TeV`, więc krawędź tabeli autorów leży tam, gdzie widmo pierwotne zaczyna wychodzić poza te
  tablice. Nie sprawdzałem, czy to był powód wyboru autorów.
- Wariantów łączonych (V1 z `B_sym`) ani tolerancji solvera w wariantach (wszystko przy domyślnych).
- Pełnej siatki: 12 mas.

## Literatura i dorobek projektu

- **Zewnętrzna:**
  - Wu & Xu, JCAP 02 (2026) 063, arXiv:2509.05618, kod `d395183`;
  - Arbey & Auffinger, BlackHawk v2.0, arXiv:1905.04268 i arXiv:2108.02737 (zakres tablic hadronizacji).
- **Własna:**
  - Mech-S7 ROT036 (nachylenia OLS-8, czułość w warunkowym 7D);
  - Mech-S6 (łatka `B_sym`, 17–18 X);
  - Rec9, 18 X (status podziału na pół: nukleony poparte źródłem, `π/K` jako założenie symetrii);
  - XH-S4 002/004 (v1/v2);
  - REVIEW_035.
- Nowości nie zgłaszam. Ocen na poziomie konturu dla `B_sym` i dla wyzerowanej emisji poniżej krawędzi nie
  znalazłem w repozytorium (przeszukanie `research/`, 31 X). „Nie znalazłem” nie znaczy „nie istnieje”.

## Odtworzenie

```text
julia --project=<env> code/wuxu_subedge_variant_boundary.jl <…/arXiv-2509.05618> native e2_native.csv
julia --project=<env> code/wuxu_subedge_variant_boundary.jl <…/arXiv-2509.05618> ols8 e2_ols8.csv
julia --project=<env> code/wuxu_subedge_variant_boundary.jl <…/arXiv-2509.05618> zero e2_zero.csv
julia --project=<env> code/wuxu_subedge_variant_boundary.jl <…/arXiv-2509.05618> native_sym e5_native_sym.csv
julia --project=<env> code/wuxu_subedge_variant_boundary.jl <…/arXiv-2509.05618> native_nsym e5b_native_nsym.csv
julia --project=<env> code/wuxu_leftwall_timing.jl <…/arXiv-2509.05618> timing_points.dat leftwall_timing.csv
python3 -I code/wuxu_e2_e5_analysis.py --native e2_native.csv --ols8 e2_ols8.csv --zero e2_zero.csv \
    --sym e5_native_sym.csv --nsym e5b_native_nsym.csv --analysis035 analysis.json --out e2_e5_analysis.json
```

Około 18 min na wariant (12 mas × 13 wywołań `magic()`). `native_sym` wymaga
`research/mech-s6/2026-10-17/apply_wuxu_charge_pair_source_map.py` z tego repozytorium.

## Powrót w trzech warstwach

- **Wynik:** w modelu autorów kontur Fig. 5 ma dwie dominujące zależności od kontraktu źródła:
  - mapę ładunkową antynukleonów: `+0.27–0.30 dex` dla `m ≳ 3e9 g`, część poparta tekstem autorów;
  - istnienie emisji hadronów poniżej `1e9 g`, która w całości niesie lewą ścianę.
  Kształt ekstrapolacji, definicja `Y` i szum solvera to setne części dex.
- **Konfiguracja:** natywny kod plus bisekcja to około 18 min na wariant na jednym rdzeniu.
  - Preregi przed każdym wariantem (E2, E5, E5b) zajęły po kilka minut.
  - Przewidywanie E5b z danych v1/v2 okazało się najmocniejszym testem dnia.
- **Uczenie systemu:**
  - (1) Próg kontroli metody (`0.01 dex`) ustawiłem poniżej szumu, który już znałem, drugi raz tego dnia
    (`REPRODUCIBILITY_THRESHOLD_BELOW_SOURCE_NUMERICAL_NOISE`, REVIEW_035). Łatka mechanizmu: przy pisaniu
    preregu przepisuję do tabeli progów aktualne oszacowanie szumu i porównuję każdy próg z nim.
  - (2) Model liniowej odpowiedzi przy granicy (`Δ log β = −log₁₀ f`) zamienia pytania o czynniki źródła na
    przewidywania liczbowe przed przebiegiem. Kandydat na regułę `[▷]` dla linii Front B: każdą zmianę
    kontraktu źródła najpierw szacować tym modelem, a natywny przebieg traktować jako test.

Wynik jest Claude'a, więc wymaga audytu spoza rodziny Claude.
