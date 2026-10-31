---
artifact_id: IW_BADACZ_WUXU_AUTHOR_NATIVE_AUDIT_REVIEW_035_20261031
exposure: PUBLIC
claim_ceiling: AUDIT_RESULT_[▷] / AUTHOR_NATIVE_EXECUTION_LOCAL / 74_POINTS_NOT_FULL_SCAN / N5_TOLERANCE_DEVIATION_DECLARED / NO_VERDICT_ON_PUBLISHED_FIGURE / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-31
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-FRONTB-NATIVE-AUDIT-001
prereg: research/badacz/2026-10-31/IW_BADACZ_WUXU_AUTHOR_NATIVE_AUDIT_PREREG_034_20261031.md (commit f170e2a, przed pierwszym przebiegiem)
external_source: github.com/Fenyutanchan/Primordial-Black-Hole @ d395183674cace6c9906a8911bdeb7234ba4040d — arXiv-2509.05618/main-scan.jl (blob b368ba55…), main.ipynb komórki 6–7 (blob 171c4a29…), data/out/scanning.jld2 (sha256 51844a46…), data/out/scanning_old.jld2 → arXiv-2509.05618v1/data/out/scanning.jld2 (sha256 7f8ebe6c…)
code: research/badacz/2026-10-31/code/wuxu_native_audit.jl; wuxu_native_audit_points_and_analysis.py (sha256 w data/native_audit/MANIFEST_SHA256.md)
outputs: research/badacz/2026-10-31/data/native_audit/
---

# Audyt natywnym kodem Wu–Xu (Fig. 5): wyniki PREREG_034

**Status:** `[▷]`. Wynik Claude'a. Wymaga audytu spoza rodziny Claude. To nie jest ocena opublikowanej
pracy ani nowa granica PBH.

## Wynik

1. Kod autorów uruchomiony lokalnie **nie odtwarza zapisanych liczb** w progach z preregu: N1 i N2 to FAIL.
   Różnice `Y_P` są rzędu `1e-4` (maks. `2.8e-4`, względnie `1.1e-3`).
2. **Kontur `χ² = 4` odtwarza się** w 12 audytowanych masach do `≤ 0.013 dex` w `β` (post hoc).
3. Poprawka formuły z arXiv v3 (`Y = 2X`) **z rekalibracją SBBN** przesuwa kontur o `+0.03…+0.07 dex`
   w stronę słabszego ograniczenia (N4). Surogat z REVIEW_031 miał dobry kierunek, ale przeszacował wielkość
   około 2,6 razy. Falsyfikator surogatu nie zadziałał.
4. N5: przy `reltol = 1e-5` wynik różni się od domyślnego o `≤ 1.8e-4`, czyli 30% progu falsyfikacji
   (`6e-4`). **Nie sfalsyfikowano.** Preregowane tolerancje `1e-10/1e-12` okazały się niewykonalne: OOM przy
   zapisie gęstym, a przy `1e-7` solver przekracza `maxiters`. Odstępstwo opisuję niżej.

## Wykonanie

- Julia 1.12.3. Pakiety najwyższego poziomu przypięte jak w
  `research/mech-s6/2026-10-18/wuxu_dynamic_comparator/setup_env.jl` (`NaturalUnits` @ `4a9f007`).
  Zależności przechodnie (m.in. podpakiety `OrdinaryDiffEq`) **nie są przypięte**: autorzy nie publikują
  `Manifest.toml`, Mech-S6 też go nie przypina.
- `magic()` autorów bez zmian: `num_points = 10000`, `BITS = 100`, `solve(…, AutoTsit5(Rosenbrock23()))`
  bez jawnych tolerancji. Kod SBBN skopiowany dosłownie z `main.ipynb`, komórki 6–7.
- 74 punkty: 12 mas × 6 indeksów `β` przy granicy oraz 2 kontrole poniżej tabeli. Punkty odtwarzają się
  bajtowo z `scanning.jld2` (`…points_and_analysis.py points`).
- Około 5 s na punkt po kompilacji.

## Werdykty

| test | próg z preregu | wynik | werdykt |
|---|---|---|---|
| N1: `Y_P,SBBN` z komórek 6–7 | `\|Δ\| < 1e-12` wobec `0.24500000000000022` | `0.24473261429443532`, `Δ = −2.67e-4` | **FAIL** |
| N2: `Y_P` natywne wobec `Y_P_mat` | PASS `< 1e-6`, INFO `< 1e-4` (względnie) | maks. `1.11e-3`; `ΔY ∈ [−2.80e-4, +1.88e-4]`, mediana `+1.2e-5`, rms `8.3e-5` | **FAIL** |
| N3: `T′_nuc` z `2·X_SBBN = 0.245` | raport | `0.09963 MeV` (autorzy: `T_nuc = 0.07819 MeV`); przy `reltol = 1e-5`: `0.09972 MeV` | — |
| N4: przesunięcie konturu, `Y_M = 2X(T′_nuc)` wobec `Y_C` | falsyfikator: `> 0.3 dex` albo przeciwny kierunek | 11 mas: `+0.029…+0.052 dex`, mediana `+0.038`; `1.12e9 g`: `≥ +0.068` (ekstrapolacja `+0.072`) | surogat **nie sfalsyfikowany**, przeszacowany |
| N5: tolerancje solvera, 3 punkty | falsyfikator: `\|ΔY\| > 6e-4` | `reltol = 1e-5`: `\|ΔY\| ≤ 1.75e-4` wobec domyślnego; `1e-7`: solver przerwany przez `maxiters` (wynik nieważny); `1e-10`: OOM | **nie sfalsyfikowany** przy `1e-5`; preregowane `1e-10` niewykonalne |

### N1 i N2: skąd różnice

- **SBBN.** W moim środowisku komórka SBBN zmienia się z tolerancją najwyżej o `3e-5`: `0.24473261`
  (`1e-3`), `0.24472957` (`1e-5`), `0.24475489` (`1e-7`). Różnica wobec autorów (`−2.7e-4`) jest dziesięć razy
  większa, więc nie jest szumem tolerancji w moim środowisku. To różnica środowisk.
  - `NaturalUnits` wykluczam: między commitem z IX 2025 (`729e5d2`) a `4a9f007` (17 XII 2025, przed v2
    autorów z 30 XII) zmieniła się jedna linia, bez stałych fizycznych.
  - Kandydaci: nieprzypięte wersje `DataInterpolations`, `ForwardDiff` (pochodna `log Nᵨ` w węzłach
    interpolacji), podpakiety `OrdinaryDiffEq`. Nie rozstrzygam.
- **Moje środowisko = środowisko CI Mech-S6 z 18 X (post hoc).** Skrypt Mech-S6
  (`research/mech-s6/2026-10-18/wuxu_dynamic_comparator/run_one_point.jl`, `6e9 g`, `β = 1e-16`,
  `num_points = 1600`) daje lokalnie `Y_P = 1.3230817938392783`. To bit w bit wartość zapisana przez Mech-S6
  z GitHub Actions (`data/native_audit/mechs6_runner_6e9_1e-16_summary_current.dat`). Rozbieżność N1/N2
  dzieli więc środowisko autorów (XII 2025) od środowiska rozwiązanego z tymi samymi przypięciami w X 2026.
  Nie jest to niedeterminizm maszyny.
- **Skan.** `ΔY` zmienia znak między punktami, więc to nie jest stałe przesunięcie.
  - Kontrole poniżej tabeli (`β = 1e-17`; PBH znika przed zamrożeniem `n/p`): `+3.2e-5` (`6.0e8 g`),
    `+1.3e-4` (`9.73e8 g`).
  - Granica SBBN liczona przez `magic()` (kontrola `6.0e8 g`: `Y_C = 0.24496`, `Y_M = 0.24503`) różni się
    od komórki SBBN tego samego środowiska o `+2.3e-4`. U autorów różnica wynosi `−7e-5`
    (`0.24493` wobec `0.24500`).
- **Czułość na drobne zmiany.** Samo przełączenie zapisu rozwiązania (`saveat` w węzłach autorów,
  `dense = false`) przy tych samych tolerancjach zmienia `Y_P` o `+2.0e-4`, `+2.4e-5` i `+6.1e-5` w punktach
  N5. Przy `reltol = 1e-3` wynik ma więc szum `~1e-4` wobec zmian, które nie dotyczą fizyki.

### Kontur jest odporny (post hoc)

Granica `χ² = 4` w `log₁₀ β`, liniowo w oknie 6 indeksów (krok siatki `0.0303 dex`):

| `m` [g] | zapisana | natywna `Y_C` | natywna − zapisana | natywna `Y_M` | `M − C` |
|---|---:|---:|---:|---:|---:|
| 1.121e9 | −17.220 | −17.220 | +0.000 | > −17.152 | ≥ +0.068 |
| 1.187e9 | −17.774 | −17.777 | −0.002 | −17.733 | +0.044 |
| 1.256e9 | −18.111 | −18.097 | +0.013 | −18.068 | +0.029 |
| 1.330e9 | −18.358 | −18.366 | −0.007 | −18.313 | +0.052 |
| 1.448e9 | −18.626 | −18.632 | −0.005 | −18.589 | +0.042 |
| 1.577e9 | −18.821 | −18.821 | −0.000 | −18.787 | +0.034 |
| 1.767e9 | −19.011 | −19.013 | −0.002 | −18.969 | +0.044 |
| 2.036e9 | −19.153 | −19.155 | −0.002 | −19.117 | +0.038 |
| 2.556e9 | −19.296 | −19.294 | +0.002 | −19.257 | +0.037 |
| 3.494e9 | −19.389 | −19.396 | −0.007 | −19.352 | +0.044 |
| 5.828e9 | −19.398 | −19.395 | +0.002 | −19.360 | +0.035 |
| 7.743e9 | −19.363 | −19.364 | −0.001 | −19.326 | +0.038 |

- **Dlaczego mały szum `Y` daje mały szum konturu.** Przy granicy odpowiedź jest prawie liniowa w `β`
  (`Y − Y_SBBN ∝ β`), więc `dY/d log₁₀ β ≈ ln 10 · 0.006 = 0.0138`. Szum `8.3e-5` (rms) daje `0.006 dex`,
  maksimum `2.8e-4` daje `0.020 dex`. Zgadza się to z obserwowanym `≤ 0.013 dex`.
- Z tej samej liniowości: zmiana efektu hadronów o czynnik `f` przesuwa granicę o `−log₁₀ f`. N4
  (`+0.038 dex`) odpowiada `f ≈ 0.92`.
- **Fałszywa precyzja:** `T_nuc` skalibrowano do 17 cyfr, by SBBN dało `0.24500000000000022`. Ten sam kod
  w innym środowisku daje `0.24473`, a szum solvera przy domyślnych tolerancjach wynosi `~1e-4`. Kalibracja
  jest wiarygodna do około trzech cyfr znaczących `Y`. Dla konturu nie ma to znaczenia.

### N4: co to mówi o poprawce z arXiv v3

- arXiv v3 (6 V 2026, Eq. 5.1) zmienia definicję na `Y_p = 2X` (MT14 ROT016). Kod i `scanning.jld2`
  używają `2X/(1 − X)` z `T_nuc` skalibrowanym pod tę formułę.
- MT14 ROT017 pokazał, że sama zamiana formuły przy starym `T_nuc` przesuwa punkt SBBN o 8,9σ. Napisał
  też, że poprawna korekta wymaga ponownej kalibracji SBBN i natywnego przebiegu. **N3/N4 to dokładnie ta
  procedura**, ograniczona do 12 mas przy granicy:
  - kontur przesuwa się w stronę większych `β` o `0.03–0.05 dex`, a przy lewej ścianie (`1.12e9 g`) o około
    `0.07 dex`;
  - to czynnik `1.07–1.18` w `β`, mały wobec zakresu Fig. 5 (3 dekady).
- Kalibracja `Y_M` na komórce SBBN zamiast na granicy `magic()` wnosi do przesunięcia najwyżej
  `(0.24503 − 0.24496)/0.0138 ≈ 0.005 dex` (kontrola `6.0e8 g`).
- Nie wiem, czy autorzy w v3 przeliczyli figurę ani jak skalibrowali v3. Nie porównuję z obrazem Fig. 5
  w czasopiśmie.

### N5: odstępstwo od preregu

- **Co zaszło.** Przebieg z `reltol = 1e-10`, `abstol = 1e-12` i pełnym zapisem gęstym przerwał OOM:
  3.6 GB po około 27 min, bez ukończenia pierwszego punktu.
- **Co zrobiłem.**
  - W trybach z jawnymi tolerancjami `magic()` zapisuje tylko węzły, w których autorzy i tak czytają
    rozwiązanie (`saveat = log.(a_list)`, `dense = false`).
  - Zamiast `1e-10` uruchomiłem drabinę `1e-3` (kontrola zapisu), `1e-5`, `1e-7`. Przy `1e-5` jeden punkt
    trwa około 400 s, czyli 80 razy dłużej niż domyślnie; przy `1e-7` ponad godzinę.
- **Wyniki:**

| punkt (`m`, `β`) | zapisany | domyślny | `1e-3` + `saveat` | `1e-5` | `1e-7` | `1e-5` − domyślny |
|---|---:|---:|---:|---:|---:|---:|
| 1.256e9 g, 8.11e-19 | 0.251337 | 0.251057 | 0.251260 | 0.251079 | przerwany (`maxiters`) | +2.2e-5 |
| 1.767e9 g, 1.00e-19 | 0.251164 | 0.251213 | 0.251237 | 0.251038 | nie uruchomiony | −1.75e-4 |
| 3.494e9 g, 4.33e-20 | 0.251350 | 0.251366 | 0.251426 | 0.251356 | nie uruchomiony | −9.5e-6 |

- **Przy `1e-7`** pierwszy punkt po 3802 s zwrócił `Y_P = 2.0000`, czyli `X_nuc = 0.5`. W logu jest
  ostrzeżenie solvera „Interrupted. Larger maxiters is needed”: przy domyślnym `maxiters = 1e5` całkowanie
  urwało się przed `T_nuc`, a interpolacja autorów ekstrapolowała. Wynik jest nieważny, dalsze punkty
  przerwałem. W żadnym innym przebiegu dnia tego ostrzeżenia nie ma (sprawdzone we wszystkich logach).
- **Werdykt N5:**
  - przy najściślejszej ważnej tolerancji (`1e-5`) różnica wobec domyślnej wynosi `≤ 1.75e-4`, a wobec
    zapisanego skanu `≤ 2.6e-4`, czyli najwyżej 44% progu `6e-4`. Falsyfikator nie zadziałał;
  - przy preregowanych tolerancjach test jest niewykonalny w tym kodzie bez zmiany `maxiters` i bez dużej
    pamięci. To ograniczenie, nie wynik.
- **Zbieżność.** Skok między poziomami (`~1e-4`) jest tego samego rzędu co szum wobec zmian, które nie
  dotyczą fizyki (kontrola `saveat`). Prawa strona równań zawiera pochodną interpolacji liniowej `Nᵨ`, `Nₛ`
  (nieciągłą w węzłach), co może ograniczać rząd zbieżności. Hipoteza `[▷]`, niesprawdzona. Do pytania
  o kontur (`0.0138` na dex) ta niepewność daje `≤ 0.02 dex`.

### Eksploracja (post hoc): skan v1 wobec obecnego

`scanning_old.jld2` to dowiązanie do skanu v1 (XH-S4 004), na tych samych siatkach `m` i `β`. Kanały
nukleonowe dodane w v2 (XH-S4 002) wzmacniają ograniczenie:

- granica `χ² = 4` przesuwa się o `−0.11 dex` przy `1.19e9 g`, `−0.45` przy `1.87e9 g`, `−1.05` przy
  `3.30e9 g` i `−2.14` przy `9.18e9 g`;
- położenie lewej ściany w masie (`≈ 1.1–1.2e9 g`) zmienia się mało.

To liczbowe ujęcie znanej zmiany źródła, nie nowy wynik. Obie wersje używają tej samej ekstrapolacji log-log
poniżej `1e9 g`, więc lewej ściany ta zmiana nie testuje (to robi E2, REVIEW_038).

## Czego nie sprawdziłem

- Pełnego skanu 100×100: tylko 74 punkty.
- Przyczyny N1 poza wykluczeniem `NaturalUnits` i tolerancji w moim środowisku.
- Obrazu Fig. 5 w JCAP ani w arXiv v3.

## Literatura i dorobek projektu

- **Zewnętrzna:** Wu & Xu, JCAP 02 (2026) 063, arXiv:2509.05618 (v1–v3), kod przy `d395183`.
- **Własna:**
  - DAX-S7 R33 (bazowy SBBN v1);
  - XH-S4 002/004 (proweniencja v1/v2, dowiązanie `scanning_old`);
  - MT14 ROT016/017/018 (definicje `Y`, kalibracja, odczyt skanu);
  - Mech-S6, 18 X (pierwszy natywny przebieg `magic()` w CI, 1 punkt);
  - REVIEW_031 (surogat).
- Nowości nie zgłaszam. N3/N4 wykonują procedurę, którą MT14 ROT017 wskazał jako wymaganą.

## Odtworzenie

```text
# środowisko: Julia 1.12.3; julia research/mech-s6/2026-10-18/wuxu_dynamic_comparator/setup_env.jl <env>
# źródło autorów: git clone https://github.com/Fenyutanchan/Primordial-Black-Hole && git checkout d395183
pip install h5py==3.12.1 numpy
python3 -I code/wuxu_native_audit_points_and_analysis.py points --jld2 <…/data/out/scanning.jld2> --outdir <dir>
julia --project=<env> code/wuxu_native_audit.jl <…/arXiv-2509.05618> <dir>/points.dat default_w1.csv default 1 2
julia --project=<env> code/wuxu_native_audit.jl <…/arXiv-2509.05618> <dir>/points.dat default_w2.csv default 2 2
julia --project=<env> code/wuxu_native_audit.jl <…/arXiv-2509.05618> n5.dat n5_ladder_1e-5_1e-8.csv ladder:1e-5:1e-8
python3 -I code/wuxu_native_audit_points_and_analysis.py analyze --jld2 <scanning.jld2> --old-jld2 <scanning_old.jld2> \
    --points <dir>/points.json --default default_w1.csv default_w2.csv --tight n5_ladder_1e-5_1e-8.csv --out analysis.json
```

W `analysis.json` sekcja `N5` liczy przy pliku podanym jako `--tight`. Tu jest to drabina `1e-5`, nie
preregowane `1e-10`.

## Powrót w trzech warstwach

- **Wynik:** natywny kod nie odtwarza zapisanych liczb w progu `1e-6`, ale odtwarza kontur Fig. 5 z
  dokładnością `0.013 dex`. Poprawka v3 z rekalibracją SBBN przesuwa kontur o `0.03–0.07 dex`. Szum solvera
  przy domyślnych tolerancjach (`~1e-4` w `Y`) jest dla konturu nieistotny.
- **Konfiguracja:** lokalna Julia z przypiętymi pakietami wystarczyła na 74 punkty w kilka minut.
  Ograniczeniem były dwa rdzenie i 8 GB: ścisłych tolerancji nie dało się wykonać.
- **Uczenie systemu:**
  - Próg odtwarzalności ustawiłem na poziomie `Y` (`1e-6`), choć kod autorów działa przy `reltol = 1e-3`.
    origin_failure_mode: `REPRODUCIBILITY_THRESHOLD_BELOW_SOURCE_NUMERICAL_NOISE`. Ten sam błąd powtórzyłem
    w kontroli E2 (PREREG_036, próg `0.01 dex`), choć miałem już oszacowanie szumu.
  - Reguła `[▷]`: przed ustaleniem progu odtwarzalności wyprowadzam go z tolerancji źródła i z wielkości,
    o którą pytam (tu: położenie konturu przez `dY/d log β`). Preregowany test ścisłych tolerancji poprzedzam
    jednopunktowym pomiarem czasu i pamięci.

Wynik jest Claude'a, więc wymaga audytu spoza rodziny Claude.
