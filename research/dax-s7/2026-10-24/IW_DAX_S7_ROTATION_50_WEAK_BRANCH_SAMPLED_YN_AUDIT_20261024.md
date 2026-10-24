# IW/NASH — DAX-S7 — obrót 50

## Wielokrotny odczyt neutronów: źródłowy podukład tła, reakcje słabe oraz aliasing wyjścia `Y_p`

**Data:** 2026-10-24  
**Status:** `SOURCE-BACKGROUND-EQUATION-BASED / SOURCE-TABLES / WEAK-ONLY_NEUTRON_PORT / OFF-GRID_INTERPOLATION_BIAS_POSITIVE / ORIGINAL_JULIA_NOT_RUN / HADRONIC_EFFECT_NOT_RUN / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / NO_PBH_BOUND`

### 1. Pytanie i wynik

Obrót 49 wykazał, że podukład tła Wu–Xu dopuszcza trzy przejścia temperatury fotonowej przez `T_nuc=0.07818527068831995 MeV` dla masy spoza siatki skanu `M_f=9.6725e9 g`, `beta=1e-17`, a standardowa siatka 10000 wartości czynnika skali nie rozdziela tego krótkiego epizodu. Obrót 50 testuje silniejszą hipotezę: czy zapisany przez źródłową procedurę *wynik interpolowany* `X_n(T_nuc)` może znaleźć się **poza wartościami fizycznych przejść czasowych** nawet wtedy, gdy rozważamy jedynie reakcje słabe i rozpad neutronów.

**Odpowiedź w kontrolowanym porcie numerycznym:** tak. Dla trzech zagęszczeń całkowania źródłowy interpolator symulowany na 10000 równomiernych w `ln a` węzłach zwrócił `X_n` większe niż przy którymkolwiek z trzech przejść. W najgęstszym teście: `X_sparse=0.10905206494`, podczas gdy wartości gałęzi wynoszą `[0.10905037478, 0.10904866245, 0.10904721961]`. Różnica względem ostatniego przejścia `4.84533e-6`. Odpowiada to źródłowemu przekształceniu `Y_code=2X/(1-X)` rzędu `1.2208e-5`, tj. `0.00407 sigma` przy źródłowym błędzie obserwacyjnym `0.003`. **Nie jest to fizyczny błąd Yp ani oszacowanie pełnego programu PBH**: hadrony nie były liczone, a samo użycie `2X/(1-X)` ma niezależną wadę definicyjną (obroty 29–33).

### 2. Fakty z kodu i ograniczenia

Repozytorium źródłowe: `Fenyutanchan/Primordial-Black-Hole`, pliki `arXiv-2509.05618/main-scan.jl`, `tool_script-N_relativistic_species.jl`, `tool_script-parameters.jl`, `main-scan-parameters.jl`. W kodzie `Y_p` jest wyznaczane na podstawie `a_list = geomspace(a_f,a_end,num_points)` (domyślnie `num_points=10000`) oraz `sortperm(Q ./ T_SM_list)` i interpolacji `X_n_list` jako funkcji `Q/T_SM_list`. Nie ma jawnego wyboru pierwszego lub ostatniego chronologicznego przejścia przez `T_nuc`.

Source-native podukład tła i jednostki zostały odtworzone zgodnie z obrotem 49. Pochodzenie danych tablicowych jest określone przez Git blob SHA: `N_around_m_e.csv` `93f2494f026c5d0587ea40fe08bb938dd9d01fa8`; `N_s_from_PDG2024.csv` `33aceb876fc36cb2486d36c690e6401d85d76b46`; `N_rho_OVER_N_s_from_PDG2024.csv` `28b0c13563d7b3bdeaee191a3a981197345d05b8`. Użyto implementacji interpolatorów opisanych w obrocie 49 (łącznie z 1000 węzłami `rho -> T`).

Równanie neutronów w wariancie bez hadronów:

`dX/dt = -Gamma(T) [X - (1-X) exp(-Q/T)] - X/tau_n`, z `Gamma(T) = (255/tau_n)(12+6x+x²)/x⁵`, `x=Q/T`, `Q=1.29333234 MeV`, `tau_n=878.4 s`. Do integracji użyto dokładnej ewolucji liniowego równania o współczynnikach zamrożonych na temperaturze środkowej każdego małego kroku:

`X_{i+1}=X_*(T_mid)+(X_i-X_*(T_mid)) exp[-lambda(T_mid) delta_t]`, `lambda=Gamma(1+exp(-x))+1/tau_n`, `X_*=Gamma exp(-x)/lambda`.

**Kontrola przybliżenia:** począwszy od `T=5 MeV` użyto neutronów w równowadze słabej jako warunku początkowego. Przed tym punktem `X_n` ustawiono w przybliżeniu równowagowym, a nie integrowano pełnej sztywnej ewolucji startującej przy `T_f~4.36e13 MeV`. Wyniku NIE należy utożsamiać z dokładnym pierwotnym rozwiązaniem źródłowym. Model nie zawiera reakcji neutronów z hadronami PBH. Parametry termodynamiczne i grawitacyjne są zgodne z wartościami zastosowanymi w porcie, nie są bitowo tożsame z `NaturalUnits.jl`.

### 3. Wyniki i zbieżność

| Siatka tła: `n_pre/n_evap/n_post` | Pierwsze przejście `Xn` | Drugie `Xn` | Trzecie `Xn` | `Xn` z 10000 próbek | `X_sparse-X_last` |
|---|---:|---:|---:|---:|---:|
| 5500 / 6000 / 6500 | 0.1090505095 | 0.1090487972 | 0.1090473548 | 0.1090526226 | +0.0000052678 |
| 10000 / 12000 / 10000 | 0.1090505386 | 0.1090486586 | 0.1090473107 | 0.1090523946 | +0.0000050838 |
| 20000 / 24000 / 15000 | 0.1090503748 | 0.1090486624 | 0.1090472196 | 0.1090520649 | **+0.0000048453** |

W najwyższej rozdzielczości czas przejść: `215.05798`, `215.07076`, `215.08153 s`, w kierunkach chłodzenie–ogrzewanie–chłodzenie. Nie podajemy tej sekwencji jako converged do pojedynczych mikrosekund: subtelny przebieg zależy od numeryki. Stabilna jest jakościowa trzykrotność i znak nadwyżki interpolatora. Różnice `Xn` i wniosek o błędzie rzędu `10^-6`–`10^-5` pozostają kontrolną estymacją wymagającą uruchomienia Julii.

Źródłowy interpolator pomiędzy sąsiednimi zapisanymi próbkami (przykład najgęstszy) wykorzystuje przybliżone punkty w skali `ln(a/a_f)`:
- pierwszy `35.07099047`, `t≈215.01801 s`, `X_n≈0.1090557302`;
- drugi `35.07472779`, `t≈216.55699 s`, `X_n≈0.1088497917`.

Odczyt `X_sparse` wypada poza przedziałem trzech rzeczywistych `X_n(T_nuc)`; dlatego **nie jest równoważny żadnemu wybieranemu jawnie przecięciu**. Zgodnie z definicją wejściowego x, interpolacja jest jednak algebraicznie poprawna dla zapisanych próbek: nie ma tu sprzeczności algorytmicznej, lecz **błąd reprezentacji trajektorii przez zbyt rzadkie próbkowanie** w przykładzie off-grid.

### 4. Znaczenie naukowe i falsyfikatory

1. **Artefakt źródłowego odczytu (kontrolny):** dla danych parametrów pokazano numerycznie `X_sparse > max(X_crossings)`. Błąd wynika ze współistnienia niejednoznacznej temperatury z niereprezentatywnymi dwoma próbkami; pierwotny solver może zachować gładką trajektorię, lecz jego późniejszy sampling traci informacje o gałęziach.
2. **Błąd mały w wariancie słabym:** różnica `Y_code` około `1.22e-5`, poniżej `0.5%` jednostki przyjętego błędu obserwacyjnego `sigma=0.003`; nie należy tej wartości nieprawidłowo nazywać `0.4 sigma` (to `0.004 sigma`).
3. **Nie wynika stąd ograniczenie pełnego wpływu:** źródłowe odziaływania hadronów mogą znacznie zmienić `X_n` podczas okresu parowania. To główny otwarty falsyfikator, bez pozytywnego wyniku lub negatywnego dowodu.
4. **Priorytet dla oryginalnego Julia:** (a) odczyt `X_n` przy każdym `T(a)=T_nuc` przez root finding, (b) oryginalny output z `num_points=10000`, (c) dodatkowo `num_points=100000` i niezależny event-based extraction, (d) test z hadronami włączonymi i wyłączonymi. Sprawdzać ten sam off-grid punkt oraz sąsiednie masy ze źródłowej siatki.
5. **Zastrzeżenia:** przyjęta granica zaniku PBH `y→0` różni się od progu masy w kodzie Julia; związek z opublikowanymi wynikami przy punktach siatki pozostaje `OPEN`. Brak claimu o nowości fizycznej; matematyka tła, bilans i poszukiwanie zer są standardowe.

### 5. Reprodukcja i chain of custody

Skrypt `IW_DAX_S7_ROTATION_50_WEAK_BRANCH_SAMPLED_YN_20261024.py` zawiera deterministyczny RK4 tła, propagację liniowej dynamiki neutronów, odtworzenie 10000 węzłów `ln a` oraz sortowaną interpolację. Zależy od skryptu obrotu 49 (w tym od loadera danych) oraz oryginalnych trzech tabel z kontrolą SHA. Lokalnie wykonano `--selftest` **PASS** dla modelu stałego `g*` i `beta=0`. **Nie wykonano jeszcze tego skryptu w bieżącym kontenerze z kompletem oryginalnych CSV** (ich bajty są dostępne przez konektor GitHub, a numeryczne wiersze sprawdzono w niezależnej implementacji JavaScript uruchomionej w narzędziu konektorów). Raportowane wyniki pochodzą z niezależnej implementacji JS, a nie ze skryptu Python. Pełne Julia: `NOT_RUN`.

**Końcowy werdykt:** `SOURCE-SAMPLED_XN_OFF_BRANCH_VERIFIED_IN_WEAK_ONLY_PORT / MAGNITUDE_SMALL / HADRONIC_TEST_OPEN / JULIA_TEST_OPEN / NO_CANON / NO_EXEC_SIGN / NO_PBH_BOUND`.

### 6. Niezależna kontrola: czy wynik jest tylko zwykłym błędem interpolacji?

Po przygotowaniu pierwszego raportu wykonano kontrolę **`beta=0`** z tą samą masą początkową, oryginalnymi tablicami, tą samą procedurą propagacji neutronów i rekonstrukcją odczytu, ale przy monotonicznym chłodzeniu bez zasilania PBH. Przy takim samym zagęszczeniu implementacji JavaScript (`n_pre=12000`, `n_evap=15000`, `n_post=12000`):

| Model | Zdarzenie(a) `T=T_nuc`: `Xn` | Z 10000 próbek | Z 100000 próbek |
|---|---|---:|---:|
| `beta=0`, jedno przejście | `0.10903292507` | `0.10903289689` | `0.10903292474` |
| `beta=1e-17`, trzy przejścia | `[0.10905052619, 0.10904868297, 0.10904731401]` | `0.10905216345` | `0.10904864915` |

Zwykły błąd interpolacji w monotonicznym wariancie wyniósł przy 10000 próbkach `-2.8183e-8`. Wariant z ponownym ogrzewaniem różnił się względem *ostatniego* przejścia o `+4.8494e-6` (około 172 razy więcej co do wartości bezwzględnej). Jest to dowód numeryczny, że efekt nie jest po prostu tą samą skalą zwykłego błędu interpolacji w wariancie bez PBH. **Porównanie dwóch różnych trajektorii nie stanowi ścisłego rozkładu błędu na czynniki przyczynowe.**

Co istotne, interpolacja przy 100000 zapisanych próbkach daje `0.10904864915`, blisko drugiego przejścia `0.10904868297`, chociaż **nadal żadna próbka nie leży między pierwszym a ostatnim przejściem**. Sama przypadkowa zgodność wartości nie dowodzi rekonstrukcji wszystkich gałęzi. Właściwym falsyfikatorem jest nadal jawne wykrywanie zdarzeń `T=T_nuc` na gęstej trajektorii i porównanie wartości przy każdym przecięciu.

Osobne dane tej kontroli zapisano w `IW_DAX_S7_ROTATION_50_MONOTONIC_VS_REHEATING_SAMPLING_CONTROL_20261024.csv`. Dotychczasowy werdykt obrotu pozostaje warunkowy; tę kontrolę dodano, aby zapobiec nadinterpretacji artefaktu samplingowego.
