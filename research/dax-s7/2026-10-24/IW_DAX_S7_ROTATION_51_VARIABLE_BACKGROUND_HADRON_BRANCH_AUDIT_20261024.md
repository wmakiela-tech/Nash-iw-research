# IW/NASH — DAX-S7 — obrót 51

## Źródłowe hadrony na zmiennym tle: falsyfikator uproszczeń obrotu 50

**Data:** 2026-10-24  
**Status:** `LOCAL_SOURCE-EQUATION-MATCHED / VARIABLE_T_A_NPBH / SIX_FINITE_LIFETIME_HADRON_CHANNELS / OFF_GRID_TRIPLE_CROSSING / CONDITIONAL_INITIAL_STATES / BELOW-TABLE_EXTRAPOLATION / FULL_JULIA_NOT_RUN / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / NO_PBH_BOUND`

### 1. Pytanie i rozstrzygnięcie

W obrocie 50 otrzymano dla **warunkowego** udziału neutronów `X_n(t1)=0.11` zmianę `ΔX_n=+0.00192640915` w trakcie trzech przejść temperatury plazmy przez `T_nuc`, przy założeniu stałych `T` i `n_PBH` w wąskim oknie. Obecny obrót usuwa te dwa zamrożenia: razem z sześcioma źródłowymi populacjami hadronów całkuje `L=ln[g_ρ(T)T⁴]` i `A=ln(a/a_f)`, a zatem **temperaturę, ekspansję, H, g_* i n_PBH(a)**. Równania tła są autonomiczne względem neutronów i hadronów w oryginalnym `main-scan.jl`, co pozwala na lokalny test bez pełnej integracji poprzedniej historii X_n.

**Wynik:** dla `M_f=9.6725×10^9 g`, `β=10^-17`, `X_n(t1)=0.11`, startujących lokalnie populacji `n_i(t1)=S_i(t1)/D_i(t1)`:

| Zdarzenie / wynik | Wartość |
|---|---:|
| Pierwsze przecięcie, dane z obrotu 49 | `t1 = 215.05755469059486 s`, `X_n=0.110000000` |
| Drugie przecięcie, ponowne ogrzewanie | `t2 = 215.07109822431892 s`, `X_n=0.11151097115237` |
| Trzecie przecięcie, późniejsze chłodzenie | `t3 = 215.08056476659510 s`, `X_n=0.11192653033308` |
| Koniec parowania, model M→0 | `t_evap = 215.07211197892192 s`, `X_n=0.11182743741539` |
| **Łączna zmiana** | **`ΔX_n(t1→t3)=+0.00192653033308`** |
| Kodowe odwzorowanie `Δ[2X/(1−X)]` | `+0.00487491383905` |
| Standardowe przybliżenie `Δ(2X)` | `+0.00385306066617` |

Różnica względem liczby obrotu 50 wynosi `+1.2118×10^-7` dla odpowiadających sobie *własnych* czasów trzeciego przejścia. Aby uniknąć przypadkowej kompensacji przesunięcia czasu, **ponownie wywołano obrót 50 z tymi samymi czasami `t2,t3` co obrót 51**: daje on `ΔX_n=+0.00192653689195`. Pozostała różnica z wyłączenia zamrożonego tła to zaledwie `−6.56×10^-9` dla tej konkretnej próbki. **Nie jest to globalna granica błędu**, lecz precyzyjne porównanie dwóch kontrolowanych implementacji.

### 2. Źródła i semantyka — nie uproszczenie do jednej fikcyjnej populacji

Źródło: publiczne repozytorium `Fenyutanchan/Primordial-Black-Hole`, podfolder `arXiv-2509.05618`. Wykorzystane struktury:

- `main-scan.jl`, blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`: równania `dlnρ_SM/dln a`, neutronów oraz sześciu populacji hadronów. Równania populacji dokładnie w tej implementacji nie mają `−3Hn_i`, toteż **nie dodawano** tego członu jako „poprawki”.
- `tool_script-N_relativistic_species.jl`, blob `0437c032bdc4bafca6cb634c0db4cd2c46fb7efc` i `data/ext/N_around_m_e.csv`, blob `93f2494f026c5d0587ea40fe08bb938dd9d01fa8`: interpolacja liniowa wartości `g_ρ,g_s` względem `ln T` z `ForwardDiff` dla lokalnych pochodnych.
- `tool_script-parameters.jl`, blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`: `T_nuc`, `Q`, `η_B`, zanik pionów i kaonów, przekroje oraz korekcje Coulomba.
- `data/out/hadrons_from_PBH.dat`, blob `06d0883a27b108692720422294ba2baacd381a64`, i `tool_script-hadrons_from_PBH.jl`: pięć niezależnych kolumn źródeł emisji; `π−,π+` współdzielą kolumnę piona, zaś każda z sześciu populacji ma osobną ewolucję. Pod granicą mas tablicy, `10^9 g`, źródłowy `LinearInterpolation` ekstrapoluje liniowo w **logarytmach**.

Lokalna temperatura pozostaje w zakresie `0.07818482549`–`0.07818667380 MeV`. Dlatego do **identycznego odtworzenia wartości i pochodnych oryginalnej tabeli w tym wąskim przedziale** wystarcza sześć oryginalnych sąsiadujących wierszy danych termodynamicznych. Niezależny interpolator odwrotny odtwarzany jest z dokładnie dwóch sąsiadujących węzłów **1000-węzłowej** siatki logarytmicznej źródła, o indeksach 111–112 (zero-based). Początkowe `L(t1)` wyznaczono przez **odwrócenie samego interpolatora odwrotnego**, żeby `T_from_ρ(L(t1))=T_nuc` dokładnie; zwykłe podstawienie `L=ln(gρ(T_nuc)T_nuc⁴)` dałoby małą, ale istotną przy tak wąskim sygnale, różnicę temperatury. Ten szczegół eliminuje dodatkowy artefakt z wcześniejszego testu.

W całym epizodzie `M_PBH<10^9g`, więc pierwsze **dwa** wiersze oryginalnej tabeli emisji wystarczają do dokładnego odtworzenia *kodowej* ekstrapolacji `dN_h/dt∝M^{p_h}`. Nie zapewnia to poprawności fizycznej poza tabelą.

### 3. Równania tła i aktualizator hadronów

Użyto `y=M/M_f`, `A=ln(a/a_f)`, `L=ln[g_ρ(T)T⁴]` i źródłowego `C=-4+r/(3+s)` z `r=d ln gρ/d lnT`, `s=d ln gs/d lnT`. Przy stałym dla badanych mas źródłowym `N_BH` i `τ_evap`:

`dL/dy = −3τ y² H C − B`, `dA/dy=−3τ y² H`,

`B = β exp(L_f−L−3A)`, `H=Hcoeff exp(L/2) sqrt(1+B y)`, `n_PBH=n_PBH,f exp(−3A)`, `dt=−3τ y² dy`.

Integracja tła w `y` metodą RK4; źródłowe równanie neutronów `dX/dt = weak + decay + hadron channels`; sześć równań `dn_i/dt=S_i−D_i n_i` aktualizowanych analitycznym operatorem `n' = e^{−DΔt}n + (1−e^{−DΔt})S/D`, z punktami pośrednimi i sprzężeniem do zmiennego `X_n`. Po zaniku PBH hadrony zanikają z własnymi czasami, bez nowych źródeł; tło ewoluuje bez wkładu PBH. **Nie uruchamiano oryginalnego solvera Julia** i nie symulowano pełnego okresu przed `t1`.

Zastosowano źródłową semantykę `n_B=η_B (2ζ(3)/π²)T³` i pełny zestaw przekrojów dla `π±`, `K−`, `K0L`, `pbar`, `nbar`. Początkowe liczebności hadronów są przybliżone quasi-stacjonarnie; ich niezależną kontrolę przedstawiono w punkcie 5. Skończony graniczny człon z całkowania `y→0` zastępuje źródłowy cutoff do masy Plancka; jest to modelowe przedłużenie o zaniedbywalnym czasie, nie dosłowne wykonanie `log_m_PBH_evaporated` w Julia.

### 4. Kontrola termiczna, liczby PBH i punktów przejścia

Dla `X_n(t1)=0.11`:

- `T_min≈0.07818482549 MeV` przed końcem parowania; `T_evap≈0.07818667380 MeV`;
- na całym badanym epizodzie względna zmiana `n_PBH(a)` wynosi około **−0.01682%**; różnica temperatur względem T_nuc jest rzędu najwyżej `0.0018%`;
- rozdzielenie kolejnych przecięć wynosi `t2−t1=0.01354353 s`, `t3−t2=0.00946654 s`;
- podukład tła w źródle nie ma sprzężenia zwrotnego od `X_n,n_h`, dlatego zmiana `X_n(t1)` ani skalowanie źródeł hadronów w lokalnym teście nie zmienia chwil trzech przecięć.

Czasy drugiego i trzeciego przejścia różnią się od obrotu 49, który odtwarzał całą historię tła od formowania PBH. Obecny test startuje dokładnie na pierwszej gałęzi i używa lokalnych danych `A(t1),t1` z tamtej rekonstrukcji. Weryfikacja zgodności całego odcinka i oryginalnego kodu Julia nadal pozostaje otwarta. **Nie interpretować ułamków milisekundy jako pewności źródłowego rozwiązania.**

### 5. Kontrole falsyfikujące: 31 odtwarzalnych eksperymentów

#### Zbieżność w `y`, `X_n(t1)=0.11`

| Kroki | `ΔX_n` |
|---:|---:|
| 3 000 | +0.001926533413 |
| 6 000 | +0.001926530980 |
| 12 000 | +0.001926530333 |
| 24 000 | +0.001926530158 |
| 48 000 | +0.001926530110 |

Różnica między 24 000 a 48 000 kroków `4.86×10^-11`. To zbieżność **lokalnego numerycznego integratora**, nie pełna walidacja fizyczna.

#### Warunkowe `X_n(t1)`

| Pierwsza gałąź | `ΔX_n` do trzeciej |
|---:|---:|
| 0.08 | +0.002080071 |
| 0.11 | +0.001926530 |
| 0.20 | +0.001470545 |
| 0.40 | +0.000474653 |
| 0.60 | −0.000512401 |
| 0.80 | −0.001508823 |

Znak wpływu zależy od stanu przy pierwszej gałęzi; źródłowe `X_n(t1)` z pełnego modelu jest nadal **NOT_RUN**.

#### Skala hadronowego źródła / kontrola negatywna

| Względna skala źródeł | `ΔX_n` |
|---:|---:|
| 0 — weak only | −0.000003110 |
| 0.10 | +0.000190295 |
| 0.25 | +0.000480219 |
| 0.50 | +0.000962935 |
| 1.00 — kod Wu–Xu | +0.001926530 |
| 1.50 | +0.002887683 |
| 2.00 | +0.003846401 |

To **diagnostyka zależności od ekstrapolacji emisji**, nie przedział niepewności fizycznej lub nowy niezależny parametr źródłowego skanu.

#### Sztuczna kontrola początkowej liczebności hadronów

Mnożnik `n_i(t1)/(S_i/D_i)` ustawiony na `0, 0.25, 0.5, 1, 2, 5` daje odpowiednio `ΔX=0.001916528, 0.001919029, 0.001921529, 0.001926530, 0.001936532, 0.001966537`. Zatem zerowy stan początkowy zamiast równowagi zmienia rezultat o `~1.00×10^-5`, ale sam efekt nie zanika. To test zależności od warunku początkowego, nie dowód quasi-równowagi rzeczywistej historii.

#### Kontrola niepewności `A(t1)`

Zmiana `A(t1)` o `±0.0002` utrzymuje trzy przejścia i zmienia `ΔX` w granicach `0.001925378`–`0.001927684`. Dokładność **rzeczywistego** stanu startowego może być gorsza, ponieważ wymaga niezależnego source-native readback.

### 6. Co jest nowe, co pozostaje otwarte

**Nowe i odporne w obrębie modelu:** wąski epizod potrójnego przecięcia można objąć zmiennym źródłowym tłem oraz sześcioma hadronami bez jakościowego zaniku efektu neutronowego. Stałość `T` i `n_PBH` w obrocie 50 nie była dominującym błędem liczbowym w tym przykładzie. Silniejsza od niej pozostaje zależność od ekstrapolacji emisji **poniżej 10^9g**, warunkowego wejściowego `X_n` i nieznanej wcześniejszej historii hadronów. Zidentyfikowano także konieczność ścisłego zsynchronizowania *dwóch różnych interpolatorów temperatury*: tablicowego `gρ(T)` i odwrotnego `ρ→T`.

**Nie wykazano:** wartości `X_n` na pierwszej gałęzi w pełnym programie; pełnych odejść od pierwotnej trajektorii w Julia; realnego błędu oryginalnego `Y_p`; wpływu na obserwacyjne ograniczenia PBH; fizycznej poprawności modelu antynukleonów poza zakresem danych. `Δ[2X/(1−X)]` jest jedynie **warunkowym algebraicznym rozrzutem między gałęziami** i nie jest zweryfikowaną zmianą wyniku z publikacji. Odrębny spór o definicję `Y_p` z obrotów 29–33 nie jest tu rozstrzygany.

**Rozstrzygający falsyfikator:** w oryginalnym środowisku Julia, w pełnym stanie 10-zmiennowym, uruchomić `M_f=9.6725e9g`, `β=1e-17` z narzędziem zdarzeń `T(a)=T_nuc`, odczytując na wszystkich trzech gałęziach `t,a,T,M,X_n,n_{π−},n_{π+},n_{K−},n_{K0L},n_{pbar},n_{nbar}`. Przetestować zbieżność solvera i odczytu `sortperm(Q/T)`, źródłowy cutoff masy i pełną historię sprzed `t1`. Osobno skonfrontować emisję poniżej zakresu tablicy z niezależnym generatorem hadronów. Dla zwykłego skanu `100×100` nie wnioskować z przypadku off-grid.

### 7. Artefakty, wykonanie i strażniki

- `IW_DAX_S7_ROTATION_51_LOCAL_VARIABLE_BACKGROUND_20261024.py`: samodzielny, bez zależności pip, zapisuje dokładnie konieczne 6 wierszy źródłowej tabeli `g_*` i 2 wiersze tabeli hadronowej; test `--selftest`; `--suite-prefix` generuje 31 kontroli w CSV i JSON.
- `IW_DAX_S7_ROTATION_51_LOCAL_VARIABLE_BACKGROUND_20261024.json`: wynik referencyjny.
- `IW_DAX_S7_ROTATION_51_VALIDATION_MATRIX_20261024.csv`: macierz kontroli `n=31`.
- `IW_DAX_S7_ROTATION_51_VALIDATION_MATRIX_20261024.json`: pełny zestaw wyników ze statusem, kontrolą pochodzenia i konfiguracjami.
- `IW_DAX_S7_ROTATION_51_RUN_LOG_20261024.txt`: log rzeczywistego wykonania w środowisku Python.

**Poziomy dowodu:** `SOURCE_CODE_VERIFIED` (audyt równań i danych) → `LOCAL_NUMERIC_REPRODUCED` (wyniki i zbieżność) → `FULL_JULIA_NOT_RUN` → `PHYSICAL_UPGRADE_FORBIDDEN`.

**Werdykt:** `LOCAL_VARIABLE_BACKGROUND_HADRON_BRANCH_EFFECT_SUPPORTED / X_INITIAL_CONDITIONAL / BELOW_TABLE_EXTRAPOLATION_DEPENDENT / BRANCH_ALIASING_OPEN_FOR_FULL_JULIA / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_PBH_BOUND`.