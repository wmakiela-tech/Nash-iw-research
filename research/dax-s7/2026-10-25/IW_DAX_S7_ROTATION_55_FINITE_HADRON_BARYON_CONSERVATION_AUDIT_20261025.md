# IW/NASH — DAX-S7 — obrót 55

## Weryfikacja wrażliwości na zachowanie liczby barionowej po uwzględnieniu skończonych czasów życia sześciu populacji hadronowych

**Data:** 2026-10-25  
**Werdykt:** `BARYON_SENSITIVITY_SURVIVES_FINITE_HADRON_DYNAMICS / FINITE_VS_QS_DIFFERENCE_SMALL_IN_TESTED_RANGE / SOURCE-TABLE_NUMERICAL_PORT / FULL_JULIA_NOT_RUN / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_NOVELTY_INFERENCE`

### 1. Cel i przewidywanie podlegające falsyfikacji

Obrót 54 wykazał niezgodność przepisu `n_B=η_B n_gamma(T)` przy stałym η_B z zachowaniem współporuszającej liczby barionów i oszacował wpływ zamiany `n_B` przy użyciu przybliżenia `n_h=S_h/D_h`. Pozostała możliwość, że wcześniejszy wynik ~20-procentowego przesunięcia przedziału akceptacji był w znacznym stopniu artefaktem przybliżenia quasi-stacjonarnych hadronów. Obrót 55 porównuje ten model z niezależnym, dodatniość zachowującym krokiem ewolucji każdej z sześciu populacji hadronowych. **Nie zmienia się źródłowego tła ani prawa emisji PBH.**

### 2. Materiał i niezmienne reguły źródła

Źródłowe repozytorium: `Fenyutanchan/Primordial-Black-Hole`, folder `arXiv-2509.05618`:

- `main-scan.jl`, blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`: `n_γ=2 ζ₃ T_SM³/π²`, `n_B=η_B n_γ`, sześć równań populacji hadronów z emisją, rozpadem i anihilacją, bez `−3H n_h`; wykorzystuje `X_n`, nie definiuje źródłowo pełnej sieci nuklearnej.
- `tool_script-parameters.jl`, blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`: parametry słabych i hadronowych reakcji oraz `η_B=6.1e−10`.
- `data/ext/N_around_m_e.csv`, blob `93f2494f026c5d0587ea40fe08bb938dd9d01fa8`, 1000 wierszy.
- `data/ext/N_s_from_PDG2024.csv`, blob `33aceb876fc36cb2486d36c690e6401d85d76b46`, 89 wierszy.
- `data/ext/N_rho_OVER_N_s_from_PDG2024.csv`, blob `28b0c13563d7b3bdeaee191a3a981197345d05b8`, 82 wiersze.
- `data/out/hadrons_from_PBH.dat`, blob `06d0883a27b108692720422294ba2baacd381a64`, 100 wierszy.

Cztery kompletne źródłowe tablice pobrano przez połączony GitHub i użyto bezpośrednio w **wykonanym** niezależnym porcie numerycznym JavaScript. Stosowano logarytmiczną interpolację lub ekstrapolację emisji zgodną z konstrukcją interpolatora źródła. Nie wykonywano oryginalnego solvera Julia.

### 3. Model i procedura

- Masa początkowa `M_f=9.6725×10⁹ g` (poza węzłami opublikowanego skanu). Dziesięć wartości `β`: `0`, `1e−20`, `5e−20`, `1e−19`, `2e−19`, `3e−19`, `5e−19`, `1e−18`, `3e−18`, `1e−17`.
- Tło: źródłowa postać `dln ρ_SM/dln a`, ekspansja `H(ρ_SM+ρ_PBH)`, prawo `M³(t)`, 1000-punktowy odwrotny interpolator `ρ↦T`. `14000` kroków RK4 w pierwszej fazie i `18000` w zmiennej `y=M/M_f` blisko parowania; przerwanie na pierwszym przecięciu `T=T_nuc`.
- Dwa przepisy na liczbę barionów: `source: n_B=η_B 2ζ₃T³/π²`; `conserved: n_B=η_B n_γ(T_nuc) exp[3(A_nuc−A)]`, gdzie `A=ln a`, `A_nuc` niezależnie ustalono na **tym samym tle** dla danego β. W obu przypadkach jest identyczne `n_B` w `T_nuc`.
- Dwa przepisy na hadrony: `QS` to `n_h=S_h/D_h`; `FINITE` całkuje każde `dn_h/dt=S_h−D_h n_h` na kroku zamrożonych współczynników **dokładną dodatniość zachowującą funkcją** `n_h(t+Δt)=n_h e^(−D_h Δt)+(S_h/D_h)(1−e^(−D_hΔt))`. Dla zależności `D_h(X_n)` i `dX_n/dt` wykonano iterację środka kroku i dokładny subkrok liniowego równania `X_n` przy zamrożonych populacjach. Wspólne tło wyklucza możliwość podmiany czasu kosmologicznego przy zmienianiu `n_B`.
- **Wierne ograniczenie źródła:** brak ekspansyjnego terminu `−3H n_h` w hadronowych równaniach — nie dodawano go arbitralnie. Przepis na baryony jest testem kontrfaktycznym, nie twierdzeniem, że kod autorów deklaruje ich zachowanie.

### 4. Wyniki: jawną ewolucję sześciu populacji porównano z QS

| β | X_n przy `n_B` źródłowym — FINITE | X_n przy `n_Ba³=const` — FINITE | ΔX_n [conserved−source] | FINITE−QS przy `n_B` źródłowym |
|---:|---:|---:|---:|---:|
| 0 | 0.109032993 | 0.109032993 | 0 | 0 |
| 1e−20 | 0.109581816 | 0.109492300 | −0.000089516 | −2.64e−9 |
| 5e−20 | 0.111768588 | 0.111323664 | −0.000444924 | −1.31e−8 |
| 1e−19 | 0.114482976 | 0.113599727 | −0.000883249 | −2.61e−8 |
| 2e−19 | 0.119848897 | 0.118108481 | −0.001740415 | −5.17e−8 |
| 3e−19 | 0.125132177 | 0.122560062 | **−0.002572115** | **−7.68e−8** |
| 5e−19 | 0.135455959 | 0.131294488 | −0.004161471 | −1.25e−7 |
| 1e−18 | 0.159913665 | 0.152184197 | −0.007729468 | −2.38e−7 |
| 3e−18 | 0.241037932 | 0.223744746 | −0.017293186 | −5.97e−7 |
| 1e−17 | 0.393171954 | 0.372210336 | −0.020961619 | −2.13e−6 |

Największa różnica FINITE−QS w `X_n` dla całego zakresu 10 β jest poniżej `2.6e−6`. W obszarze analizowanym w obrocie 54, np. `β=3e−19`, bezwzględna różnica FINITE−QS jest **ok. 33 000 razy mniejsza** niż przesunięcie wynikające z zamiany `n_B`. ΔX_n(FINITE) i ΔX_n(QS) różnią się dla tego punktu o zaledwie `5.65e−10`.

Dla `β=3e−19`: `Y_code=2X/(1−X)` zmienia się z `0.286059617` do `0.279358294` (`Δ≈−0.0067013`), zaś `2X` z `0.250264354` do `0.245120124` (`Δ≈−0.00514423`). W **tym samym warunkowym modelu** efekt `n_B` nie jest artefaktem quasi-stacjonarnych hadronów.

Kontrola `β=0`: oba modele baryonowe i oba schematy hadronowe zwracają identyczne `X_n=0.109032993`, ponieważ nie istnieje hadronowe źródło od PBH. Model FINITE ma dodatnie gęstości hadronów dzięki stabilnej formule wykładniczej. Macierz zawiera 10×2×2=40 obliczeń; pełne liczby zapisano w CSV i JSON.

### 5. Ograniczenia i negatywna wiedza

1. **Brak pełnego solvera Julia** i niezależnej sieci BBN. Nie ma prawa wnioskować o poprawce do opublikowanych granic PBH ani o anomalii obserwacyjnej.
2. Pełne tablice źródłowe zostały wykorzystane przez uruchomiony port JS. Samodzielny dołączony Python jest przygotowany do ponownego uruchomienia i sprawdzony składniowo oraz self-testem, lecz jego pełne przebiegi wymagają udostępnienia czterech tablic lokalnie lub użycia `--download`. **Nie oznaczać tych przebiegów Python jako wykonanych.**
3. Przy późnym parowaniu masa PBH schodzi poniżej 10⁹ g; źródłowa emisja używa wówczas logarytmicznej **ekstrapolacji**. Różnic baryonowych nie ekstrapolować na inne modele hadronizacji bez osobnego testu.
4. Zachowanie liczby barionów wymaga uzgodnienia znaczenia `η_B` (referencja późna przy `T_nuc`). Ewentualne wstrzyknięcie energii, zmiany entropii i przyszłe porównanie z pełną siecią BBN należy rozwiązywać w spójnym modelu, nie przez ręczne dodawanie przesunięć.
5. Brak terminu `−3H n_h` oraz źródłowe prawo chłodzenia i mapowanie `Yp` to **osobne** ścieżki walidacji. Nie sumować ich niesprawdzonych korekt.
6. Rezultat nie jest ścisłym dowodem zbieżności oryginalnego solvera. Porównanie z rotacją 54 dla quasi-stacjonarnych trajektorii pokazuje niewielkie różnice między niezależnymi siatkami całkowania (rzędu ~10⁻⁶ dla `X_n` w przykładowych punktach), ale potrzebny pozostaje test zagęszczenia dla każdej implementacji.

### 6. Falsyfikator dla następnego etapu

Wykonać w oryginalnej Julii dokładnie to samo 2×2 przy wybranych `(M_f,β)`:
`source n_B` vs `conserved n_B` × oryginalne 6 ODE populacji vs kontrolne wymuszenie `n_h=S_h/D_h`, na wspólnym tle i z tą samą kontrolą `T_nuc`. Zapisać `X_n` bez przeliczenia na `Y_p`, a także gęstości antyprotonów i antyneutronów, błąd solvera i liczbę przecięć temperatury. Przy rozbieżności powyżej `10⁻⁴` dla β w warunkowym oknie zgodności diagnozować solver, interpolator źródłowy i ekstrapolację emisji przed interpretacją.

### 7. Reprodukcja i zapis

- `IW_DAX_S7_ROTATION_55_FINITE_HADRON_BARYON_CONSERVATION_20261025.csv` — 10 wierszy, wszystkie 4 ramiona i dane pochodne.
- `IW_DAX_S7_ROTATION_55_FINITE_HADRON_BARYON_CONSERVATION_20261025.json` — identyczna macierz, statusy i provenance.
- `IW_DAX_S7_ROTATION_55_FINITE_HADRON_BARYON_CONSERVATION_20261025.py` — samodzielny skrypt bazujący na porcie r54, dodatkowy tryb `--batch-study`, kontrola Git blob SHA czterech źródeł, reprodukcja obu wariantów barionowych i obu schematów hadronowych. Self-test i kompilacja składniowa **PASS**. Przykład użycia: `python <script>.py --batch-study --source-dir ./arXiv-2509.05618/data --download --betas 0 1e-20 3e-19 1e-17 --csv out.csv --json out.json`.

**ROLA / CLAIM CEILING:** DAX-S7 niezależna komórka wyszukiwania odchyleń; tylko diagnoza źródłowa i warunkowy eksperyment reprodukcyjny. `NO_CANON`, `NO_EXEC_SIGN`, `NO_PHYSICAL_UPGRADE`, `NO_NOVELTY_INFERENCE`.