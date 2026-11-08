---
artifact_id: IW_BADACZ_WUXU_BAND_RESOLVED_HADRON_RESPONSE_KERNEL_REVIEW_050_20261108
exposure: PUBLIC
claim_ceiling: MODEL_INTERNAL_RESPONSE_KERNEL_[▷] / AUTHORS_CODE_B_EXEC_NATIVE_EXTRAPOLATION / NO_SOURCE_VALIDATION / NO_PBH_BOUND / NO_VERDICT_ON_PUBLISHED_FIGURE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-08
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-FRONTB-TIME-KERNEL-001
prereg: research/badacz/2026-11-08/IW_BADACZ_WUXU_BAND_RESOLVED_HADRON_RESPONSE_KERNEL_PREREG_048_20261108.md (commit b7a2c14, przed przebiegami)
code: research/badacz/2026-11-08/code/wuxu_band_kernel.jl; wuxu_band_number_shares.py; wuxu_band_kernel_analysis.py; wuxu_washout_toy_kernel.py (post hoc)
outputs: research/badacz/2026-11-08/data/ (MANIFEST_SHA256.md, RUNLOG.md, kernel_analysis.json)
revision: r2 (8 XI) — wynik N1 (PASS) i analiza końcowa z N1; r1 = commit d63ec7c (N1 PENDING)
---

# Lewą ścianę niesie końcowy wybuch PBH: hadrony z ostatnich milisekund ważą 2–5 razy więcej niż wynika z ich liczby

**Status:** `[▷]`. Wynik modelowy w kodzie autorów (`d395183`, mapa `B_exec`, natywna ekstrapolacja poniżej `1e9 g`),
bez walidacji fizycznej źródła i bez granicy PBH. Jako wynik Claude'a wymaga audytu spoza rodziny Claude.

## Wynik

Udział efektu `s_eff` (część czynnika `β·E` wyznaczającego kontur), udział liczby hadronów `s_num` i waga czasowa
`W = s_eff/s_num`. Pasma chwilowej masy PBH:
- `A`: `≥ 1e9 g`;
- `B`: `3e8–1e9`;
- `C`: `1.06e8–3e8`, ostatnie `~6 ms`;
- `D`: `< 1.06e8 g`, `T_H ≥ 100 TeV`, ostatnie `0.28 ms`.

`T_ev` to temperatura w chwili wyparowania według modelu zabawkowego niżej.

| `j` (`M0`) | `τ` | `T_ev` | `W(A)` | `W(B)` | `W(C)` | `W(D)` | `s_eff(D)` (liczba: `s_num(D)`) |
|---|---:|---:|---:|---:|---:|---:|---:|
| 22 (`1.12e9 g`) | 0.335 s | 1.48 MeV | 0.04 ± 0.09 | 0.79 ± 0.03 | 4.20 ± 0.24 | 5.36 ± 0.70 | **0.077 ± 0.010** (0.014) |
| 28 (`1.33e9 g`) | 0.559 s | 1.15 MeV | 0.05 ± 0.02 | 1.49 ± 0.02 | 2.47 ± 0.18 | 2.30 ± 0.45 | **0.024 ± 0.005** (0.010) |
| 34 (`1.58e9 g`) | 0.932 s | 0.89 MeV | 0.44 ± 0.02 | 1.57 ± 0.03 | 1.68 ± 0.17 | 2.04 ± 0.81 | 0.016 ± 0.006 (0.008) |
| 62 (`3.49e9 g`, kontrola) | 10.1 s | 0.27 MeV | 0.98 ± 0.01 | 1.02 ± 0.07 | 0.91 ± 0.61 | 0.7 ± 2.2 | 0.001 ± 0.004 (0.002) |

- **Przy lewej ścianie ważenie liczbą nie działa.**
  - Przy `j = 22` hadrony z ostatnich `~6 ms` (pasma C + D, 9% liczby) niosą `41%` efektu.
  - Emisja nad krawędzią tabeli (A, 19–40% liczby) niesie `≤ 2%` efektu przy `j = 22` i `28`
    (`0.007 ± 0.016` i `0.019 ± 0.007`).
  - Przy `τ ≈ 10 s` (kontrola) wagi wynoszą `≈ 1`, czyli ważenie liczbą jest tam poprawne.
- **Bramka B Mech-S8** (`T_H ≥ 100 TeV`) to bezpośredni pomiar w kodzie autorów:
  - usunięcie emisji przy `T_H ≥ 100 TeV` przesuwa ścianę o `+0.034 dex` przy `j = 22`, `+0.009` przy `j = 28` i
    `+0.008` przy `j = 34`;
  - podwojenie tej emisji daje odpowiednio `−0.033`, `−0.012` i `−0.006 dex`;
  - przy `j = 62` efekt jest zerowy w granicach szumu.
  Czynnik 2 w wydajności hadronów powyżej 100 TeV to więc systematyka `~0.03 dex` na krawędzi ściany. To tyle co prawo
  emisji poniżej krawędzi (`0.03–0.05`) i tolerancja (`0.01–0.03`), mało wobec mapy ładunkowej (`0.27–0.30`).
- **Werdykty z preregu:**
  - **P0** (pasmo A wobec wariantu `zero` z REVIEW_038): **4/4 PASS**. Przy `j = 34` `−0.095` wobec przewidywanych
    `−0.098 ± 0.03`; przy `j = 62` `−0.273` wobec `−0.274 ± 0.03`.
  - **Reguła sumy:** 4/4 PASS, różnice `−0.018; −0.018; −0.056; −0.016` (próg `±0.1`).
  - **P1:** PASS, `W(D) = 5.4 ± 0.7` i `2.3 ± 0.45`.
  - **P2:** `j = 28` PASS (`1.08`); `j = 22` **FAIL** (`W(C)/W(D) = 0.78 ± 0.11`, okno `[0.8, 1.25]`). Ostatnie
    `0.28 ms` ważą tam nieco więcej niż poprzednie `6 ms`; odchylenie mieści się w 1σ.
  - **P3:** PASS, `0.98` i `1.02`.
  - **P4:** PASS, `0.077` i `0.024`.
  - **F1, F2, F3:** nieuruchomione. `D×0` i `D×2` dają zgodne `s_eff`, więc odpowiedź w paśmie D jest liniowa.
  - **N1:** zob. niżej.
- **Kontrola numeryczna N1** (tolerancja `1e-4/1e-7`, `D×2` przy `j = 22`): **PASS** (r2).
  - `Δ(D×2)` wynosi `−0.0281` przy tolerancji `1e-4` wobec `−0.0325` przy domyślnej; zmiana `+0.0045` jest poniżej
    progu `0.02`, więc wynik dla pasma D nie jest ograniczony tolerancją.
  - Granica bazowa przy `1e-4` wynosi `−17.2031` i odtwarza REVIEW_047 (`−17.2035`, inna metoda dopasowania).

## Odstępstwo od preregu

- `C×10` i `D×10` okazały się obliczeniowo niewykonalne przy domyślnym solverze autorów:
  - pierwszy punkt `C×10` liczył się 1286 s;
  - proces `C×10` przy `j = 28` zabił OOM przy 3.3 GB;
  - przyczyna: `magic()` zapisuje każdy krok, a silna iniekcja w końcowym wybuchu daje bardzo wiele kroków.
- Decyzja (RUNLOG 09:47, commit `880eca3`) zapadła przed jakimkolwiek wynikiem dla pasma D:
  - pasmo D wyznaczam z preregowanych `D×2` i `D×0`, ważonych odwrotnością wariancji;
  - P2 liczę jako `C×2/D`;
  - F3 to `D×0` wobec `D×2`;
  - N1 robię na `D×2`.
- Widziałem wcześniej jedną wartość `C×10`.

## Mechanizm (post hoc, poza werdyktami)

- **Model zabawkowy** (`code/wuxu_washout_toy_kernel.py`):
  - hadron wstrzyknięty w chwili `t` daje natychmiastowe zaburzenie `X_n`;
  - zaburzenie zanika z tempem słabych przemian `λ = Γ_np + Γ_pn` z (B.15)/(B.17) autorów, przy `T(t)` ery
    promieniowania i `g* = 10.75`;
  - waga hadronu: `w(t) = exp(−∫_t^τ λ dt′)`;
  - przy `T ≈ 1.5 MeV` tempo `λ ≈ 15 s⁻¹` i rośnie wstecz w czasie mniej więcej jak `T⁵`.
- **Zgodność z pomiarem:**
  - model liczyłem po obejrzeniu natywnych A/B/C dla `j = 22, 28`;
  - jego przewidywania dla D oraz dla `j = 34, 62` zapisałem w repo (commit `a8850df`) przed obejrzeniem tych wyników;
  - przy `j = 28, 34, 62` zgadza się z pomiarem do około 10–15%; największe odchylenie to `W(B)` przy `j = 34`
    (`1.69` wobec `1.57 ± 0.03`);
  - przy `j = 22` zaniża późne wagi o 20–35% (`W(C)` 3.3 wobec 4.2; `W(D)` 3.5 wobec 5.4).
- **Interpretacja:** jest to jakościowy obraz autorów z Fig. 4 („spike”, wymywanie przez oddziaływania słabe),
  teraz zmierzony ilościowo w ich kodzie. Nowości nie zgłaszam.

## Konsekwencje dla otwartych wątków

- **Mech-S8 ROT002/006 i program E4:**
  - Dla lewej ściany walidacja źródła musi obejmować `T_H` od `~10 TeV` (`1e9 g`) do ponad `100 TeV`.
  - Emisja poniżej `3e8 g` (pasma C + D) niesie `41%` efektu przy `j = 22` i `17%` przy `j = 28`.
  - Potrzebne są więc wszystkie trzy preregowane przez Mech-S8 punkty `1e9`, `3e8`, `1e8 g`. Ważenie liczbą zaniżało
    znaczenie `3e8` i `1e8 g`.
- **Korekta mojej noty z 2 XI 20:51:**
  - Wniosek „1e8 g mniej pilne niż 3e8 i 1e9 g” był błędny i go wycofuję. Opierał się na ważeniu liczbą bez jądra
    czasowego.
  - Udział liczbowy (`1.75–2.2%` hadronów spod krawędzi) był policzony poprawnie, tylko nie przenosi się na kontur.
- **INT9 ROT001 i MT14 ROT025** (bez odpowiedzi czasowej nie ma przeniesienia na `Y_P`; ostatnich 0.281 ms nie wolno
  pomijać): potwierdzone ilościowo. Ostatnie 0.28 ms niosą 7.7% efektu przy `j = 22`.
- **Mech-S8 ROT006** (`+5.6–6.1%` liczby hadronów, prawo z artykułu wobec kodu): zastrzeżenie autorów raportu, że to
  nie przenosi się na `Y_P`, jest słuszne. Zmierzone przesunięcie (REVIEW_042, `−0.03…−0.055 dex`) jest 2–3 razy
  większe niż wynikałoby z liczby.
- **Użycie jądra:**
  - Dla przyszłej, źródłowo zwalidowanej poprawki tempa w paśmie o czynnik `f_b` przesunięcie wynosi
    `Δ ≈ −log10(1 + Σ_b (f_b − 1) s_eff,b)`.
  - Liniowość potwierdzają reguła sumy i zgodność `D×0`/`D×2` w zakresie `k ∈ [0, 2]`.
  - Wartości `s_eff` są w `data/kernel_analysis.json`.

## Odtworzenie

```text
julia --project=<env> code/wuxu_band_kernel.jl <…/arXiv-2509.05618> kernel_wN.csv <configs>   # data/configs_*.dat
BADACZ_TOL=1e-4:1e-7 julia --project=<env> code/wuxu_band_kernel.jl <…> n1_base.csv data/configs_n1_base.dat   # oraz n1_D2
python3 -I code/wuxu_band_number_shares.py --table <…/data/out/hadrons_from_PBH.dat> --out band_number_shares.json
python3 -I code/wuxu_band_kernel_analysis.py --runs kernel_w1.csv kernel_w2.csv kernel_w3.csv kernel_w4.csv \
    --shares band_number_shares.json --n1 n1_base.csv n1_D2.csv --out kernel_analysis.json
python3 -I code/wuxu_washout_toy_kernel.py --table <…/hadrons_from_PBH.dat> --out washout_toy_kernel.json
```

- Około 1.5 min na konfigurację przy domyślnej tolerancji.
- Sterownik z `k = 1` odtwarza bitowo wartości natywne (`data/identity.csv`).

## Powrót w trzech warstwach

- **Wynik:**
  - natywne jądro odpowiedzi lewej ściany na wstrzykiwanie hadronów;
  - przy wyparowaniu w `T ≈ 1.1–1.5 MeV` liczą się prawie wyłącznie hadrony emitowane poniżej `1e9 g`, a wśród nich
    nieproporcjonalnie najpóźniejsze (C + D: 41% efektu przy 9% liczby, `j = 22`);
  - pasmo `T_H ≥ 100 TeV` waży 2–5 razy więcej niż jego udział liczbowy;
  - przy `τ ≈ 10 s` ważenie liczbą jest poprawne.
- **Konfiguracja:**
  - P0 i reguła sumy, wyprowadzone z istniejącego wariantu `zero`, okazały się ostrym, niezależnym testem założenia o
    liniowym funkcjonale;
  - model zabawkowy commitowany przed danymi przetestował mechanizm na danych spoza próby.
- **Uczenie systemu:**
  - `origin_failure_mode: PREREG_AMPLIFIER_WITHOUT_COST_PILOT` (mój): wpisałem do preregu mnożnik `×10` bez pilotażu
    kosztu, a kontrola tożsamości sprawdza poprawność, nie koszt. To ta sama klasa awarii co OOM w REVIEW_035.
    Łatka: przed preregiem jeden punkt każdego nowego typu zaburzenia jako pomiar czasu i pamięci.
  - `origin_failure_mode: STATIC_WEIGHT_PRIORITY_WITHOUT_TIME_KERNEL` (mój, nota z 2 XI): z udziału liczbowego
    wywiodłem priorytet. Łatka: priorytet dla konturu tylko z jądra odpowiedzi albo z bezpośredniego pomiaru.
