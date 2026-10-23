# IW/NASH — DAX-S7 — obrót 49

## Źródłowy podukład tła PBH: rzeczywiste potrójne przejście poza siatką oraz niewystarczające próbkowanie `Y_p`

**Data:** 2026-10-24  
**Status:** `SOURCE-EQUATION-MATCHED_BACKGROUND_PORT / ORIGINAL_SOURCE_TABLES / OFF_GRID_THREE_CROSSINGS_REPRODUCED_AT_MULTIPLE_RESOLUTIONS / SOURCE_OUTPUT_ALIASING_RISK / FULL_JULIA_NOT_RUN / HADRONIC_CHANNEL_NOT_EVALUATED / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / NO_PBH_BOUND`

### 1. Pytanie, motywacja i najważniejsza korekta

Obroty 45–48 przewidywały możliwą niejednoznaczność `X_n(T_nuc)` przy krótkotrwałym ponownym ogrzewaniu PBH, lecz na uproszczonym modelu promieniowania. Obecny obrót wykonuje **niezależny port numeryczny dokładnie tego podukładu tła, który w `main-scan.jl` jest autonomiczny względem neutronów i hadronów**: `t`, `rho_SM`, `M_PBH`, `a`. Uwzględnia oba źródłowe interpolatory `g_rho(T)` i `g_s(T)`, zależność H od rho_PBH i rho_SM, używany w kodzie wzór chłodzenia oraz 1000-węzłowy interpolator odwrotny `rho_SM -> T`.

**Wynik jakościowy:** punkt `M_f=9.6725×10^9 g`, `beta=10^-17`, leżący **między** węzłami mas pierwotnego skanu, daje **trzy przecięcia** `T(t)=T_nuc` w reprodukowanym podukładzie tła. Efekt utrzymuje się przy czterech rozdzielczościach niezależnej integracji. Sam pierwotny kod `main-scan.jl` nie został uruchomiony; wyniku nie wolno utożsamiać z numerycznym potwierdzeniem dla środowiska Julia ani z błędem opublikowanego `Y_p`.

### 2. Audyt źródła (facts versus reconstruction)

Źródłowy `main-scan.jl`:

- stan ewolucji: `log_t_in_EU`, `log_rho_SM_in_EU`, `log_m_PBH_in_EU`, `log_X_n` i sześć populacji hadronów;
- `rho_total=rho_SM + m_PBH*n_PBH`, `n_PBH=n_PBH_ini*(a_ini/a)^3` do chwili odcięcia;
- `H=sqrt(rho_total/(3*M_Pl^2))`, `dlogt/deta=1/(H*t)`;
- `dlogrho_SM/deta=-4+r/(3+s)-dotM*n_PBH/(H*rho_SM)`, gdzie `r=dln g_rho/dlnT`, `s=dln g_s/dlnT`;
- `dotM=-N_BH(T_BH)*m_Pl^4/M^2` i `T_BH=M_Pl^2/M`;
- końcowe `Y_p` wyznaczane przez `sortperm(Q ./ T_SM_list)`, interpolację `X_n` względem `Q/T`, bez jawnego wyboru przejścia chronologicznego;
- domyślne `num_points=10000`; `a_end=10*cbrt(g_rho(T_f)*T_f^3/[g_rho(T_nuc)*T_nuc^3])` dla `a_f=1`.

Tablice źródłowe: `N_around_m_e.csv`, `N_s_from_PDG2024.csv`, `N_rho_OVER_N_s_from_PDG2024.csv`. Interpolacja stała na krańcach funkcji stopni swobody, w skali `ln T`; `from_rho_to_T` osobno jako 1000 węzłów geometrycznych między `0.01 MeV` a `10^6 MeV`, liniowe wartości w `ln rho` i `ln T`, ekstrapolacja liniowa. W obrębie badanych mas `T_BH > 1 TeV`, więc źródłowy `N_BH` jest stały: około `0.007334382996056442`.

Autonomiczność tła oznacza, że **usunięcie równań hadronowych i neutronowych nie zmienia równań tła tej konkretnej implementacji**. Nie oznacza to, że wynik tła jest pełnym wynikiem fizycznym ani że pominięte hadrony nie wpływają na sam `X_n`.

### 3. Niezależna parametryzacja masy i równania

Dla stałego `N_BH`, masa spełnia w czasie fizycznym `M(t)=M_f[1-(t-t_f)/tau]^(1/3)`, gdzie `tau=M_f^3/(3N_BH m_Pl^4)`; `y=M/M_f`. Pozwala to usunąć sztywną osobliwość równania `dlogM` w pobliżu końca parowania. Użyto stanu `L=ln[g_rho(T)T^4]` (pomijalny stały mnożnik `pi²/30`) i `A=ln(a/a_f)`. Definiujemy `B=beta*exp(L_f-L-3A)`, wtedy `rho_PBH/rho_SM=B*y`, a `H=H_0*exp(L/2)*sqrt(1+B*y)` z `H_0=0.20658852676118475 s^-1 MeV^-2`, uzyskanym ze stałych SI/CODATA.

Dla `C_0=-4+r/(3+s)` otrzymujemy dokładnie odpowiadające źródłowemu podukładowi tła równania:

- `dL/dt = H*C_0 + B/(3*tau*y²)`;
- `dA/dt=H`;
- w końcowej fazie z czasem zastąpionym przez `y`: `dL/dy=-3*tau*y²*H*C_0-B`, `dA/dy=-3*tau*y²*H`.

Integracja trójfazowa: `ln(t/t_f)` do `y=0.5`; następnie `y=0.5->0` i `ln(t/t_evap)` po zaniku PBH. Dla źródła Julia masę zeruje się dopiero przy `max(M_f exp(-20),m_Pl)`, nie dosłownie przy zerze; odpowiadający temu błąd czasu pod koniec parowania przy obecnej masie jest ekstremalnie mały, ale pozostaje formalną różnicą portu. Różnice stałych jednostkowych NaturalUnits vs CODATA i zachowanie solverów również wymagają walidacji source-native.

### 4. Nowy wynik: trzy przejścia w podukładzie tła

Parametry: `M_f=9,672,500,000 g`, `beta=1e-17`, `T_nuc=0.07818527068831995 MeV`; szacowane `tau=215.0721119789 s`. Korzystając z oryginalnych trzech tablic źródłowych, otrzymano:

| Liczba kroków w `ln t` / `y` | Pierwsze przejście [s] | Drugie [s] | Trzecie [s] | Wynik |
|---|---:|---:|---:|---|
| 4 000 / 4 000 | 215.057695 | 215.070835 | 215.081403 | 3 przecięcia |
| 7 000 / 8 000 | 215.056195 | 215.071181 | 215.080691 | 3 przecięcia |
| 13 000 / 16 000 | 215.057768 | 215.070818 | 215.081432 | 3 przecięcia |
| 25 000 / 25 000 | **215.057555** | **215.070872** | **215.081336** | **3 przecięcia** |

Kierunki czasowe: **chłodzenie → ogrzewanie → chłodzenie**. Rozpiętość pomiędzy pierwszym i ostatnim przejściem w najgęstszym teście to `0.02378097 s`. Dla kontrolnego `beta=0` i tej samej masy zanotowano **jedno** przejście, około `214.96214 s`. Jakościowa trzykrotność jest odporna na rozdzielczość, ale czasy przejść zmieniają się w granicach około `0.0016 s`, zatem nie podajemy ich jako dokładnych wyników pierwotnego solvera.

**Istotna korekta względem obrotów 47–48:** poprzedni model stałych stopni swobody przewidywał położenie takiego okna mas przy innej masie zależnej od kalibracji zegara. Po uwzględnieniu źródłowej funkcji `g_*`, sprzężenia z PBH i źródłowego równania chłodzenia podukład tła wciąż generuje potrójne przejście, lecz jego położenia nie należy przejmować z uproszczonego modelu.

### 5. Nowy, silniejszy falsyfikator: aliasing źródłowych 10 000 próbek

Dla parametru testowego źródłowy wzór `a_end` prowadzi do `ln(a_end/a_f)=37.36121495`. Ponieważ generowanych jest 10 000 węzłów `a_list=geomspace(a_f,a_end,10000)`, odstęp w `ln a` wynosi **`0.00373649514`**. Najgęstsza integracja dała dla trzech przecięć:

- pierwsze: `ln(a/a_f)=35.07113747`;
- drugie: `35.07116992`;
- trzecie: `35.07119542`;
- całe okno: `Delta ln a≈0.00005794`, około **64,49 razy węższe** niż odstęp zapisu!

Każde z trzech przecięć przypada w przedziale **między tymi samymi dwoma punktami** `a_list`, indeks węzła (indeksacja od zera) `9386`, co wprost pokazuje, że **żaden z 10 000 zapisanych punktów nie znajduje się między pierwszym a ostatnim przecięciem**. Badana trajektoria temperatury, nawet jeśli solver całkował ją poprawnie, nie jest rozdzielana przez siatkę późniejszego odczytu `Y_p`. Zwiększenie liczby zapisanych węzłów do rzędu co najmniej `~6.5×10^5` dawałoby średnio jeden krok na szerokość tego okna (bez gwarancji odtworzenia wszystkich trzech gałęzi); rozwiązanie praktyczne to **event-driven crossing extraction**, nie brutalne zwiększanie `num_points`.

Nie jest to dowód, że opublikowane `Y_p` jest liczone błędnie na źródłowych 10 000 węzłach: badana masa leży między węzłami opublikowanego skanu, a sam stan neutronów może się zmieniać mało. Jest to **warunkowa, konkretna luka rozdzielczości na trajektorii off-grid**, wykazana względem oryginalnej procedury próbkowania.

### 6. Wpływ na neutrony: ograniczenie i niewiedza

Jeżeli dla orientacji założyć na pierwszym przejściu `X_n=0.11` i pozostawić wyłącznie źródłowe słabe przemiany neutronów i rozpad, w lokalnym otoczeniu `T_nuc` uzyskujemy `dX_n/dt≈−1.3515×10^-4 s^-1`, więc na `0.02378 s` różnica `Delta X_n≈−3.2×10^-6` i `Delta(2X_n)≈−6.4×10^-6`. **To nie jest wynik pełnej ewolucji X_n w źródle ani ograniczenie pełnego błędu Y_p**: promieniowanie PBH produkuje również hadrony, które w źródłowym modelu sprzęgają się bezpośrednio z przemianami `n↔p`. Ich wpływ w krótkim końcowym impulsie pozostaje **NOT_RUN**.

Niezależnie obowiązuje wcześniejsza identyfikacja niezgodności formuły `Y_p`: źródłowy wzór `2X_n/(1−X_n)` nie jest standardowym wzorem `Y_p≈2X_n`; nie należy mieszać tej różnicy definicyjnej z nową niejednoznacznością gałęzi temperatury.

### 7. Falsyfikator i granice wnioskowania

Należy wykonać na oryginalnym `main-scan.jl` w Julia **off-grid** `M_f=9.6725e9 g`, `beta=1e-17`:

1. W `evolution_solution` znaleźć wszystkie zera `T_SM(a)−T_nuc` na gęstej siatce lub event callback, rejestrując `a,t,X_n`; sprawdzić rozwiązywanie masy i próg jej zaniku.
2. Sprawdzić zbieżność przy solver tolerances i `num_points=10000` vs event-driven odbiór, porównać sortowaną interpolację `X_n(Q/T)`.
3. Powtórzyć kontrolę z włączonymi i wyłączonymi hadronami; nie wymaga to modyfikacji podukładu tła w aktualnym źródle, ale zmienia wynik `X_n`.
4. Zweryfikować precyzyjne jednostki `NaturalUnits` i źródłowy mechanizm `from_rho_to_T`; dopiero to pozwoli stwierdzić identyczność portu z oryginalnym Julia.
5. Oddzielnie sprawdzić obie sąsiednie masy oryginalnej siatki, a nie przenosić przykładu off-grid na publikowany skan.

Żadna z tych czynności nie została przedstawiona jako wykonana w pełnym Julia. **Nie wykazano błędnego ograniczenia PBH, przełomu fizycznego ani nowej niezależnej teorii.**

### 8. Reprodukcja i pochodzenie

Skrypt: `IW_DAX_S7_ROTATION_49_SOURCE_BACKGROUND_TRIPLE_CROSSING_20261024.py` — NumPy/SciPy, osobne etapy integracji, `--selftest` z analitycznym bez-PBH modelem promieniowania: **PASS**; `--fetch-source` pobiera trzy źródłowe CSV i weryfikuje dokładne Git blob SHA. Skrypt jest niezależną implementacją o adaptacyjnym solverze SciPy, podczas gdy serie liczbowe raportu powstały w osobnej implementacji JavaScript z oryginalnymi tabelami: to dwa **różne** instrumenty, przy czym raportowanych trzech przejść nie potwierdzono jeszcze przez wykonanie skryptu SciPy na pełnych CSV w bieżącym środowisku. Nie twierdzimy inaczej.

Source-native public repo: `Fenyutanchan/Primordial-Black-Hole`, gałąź `master`; wejściowe audytowane blob SHA:

- `arXiv-2509.05618/main-scan.jl`: `b368ba55d5a493f7bc185909730f7fe5691f10d6`;
- `tool_script-parameters.jl`: `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`;
- `tool_script-N_relativistic_species.jl`: `0437c032bdc4bafca6cb634c0db4cd2c46fb7efc`;
- `data/ext/N_around_m_e.csv`: `93f2494f026c5d0587ea40fe08bb938dd9d01fa8`;
- `data/ext/N_s_from_PDG2024.csv`: `33aceb876fc36cb2486d36c690e6401d85d76b46`;
- `data/ext/N_rho_OVER_N_s_from_PDG2024.csv`: `28b0c13563d7b3bdeaee191a3a981197345d05b8`.

**Prior-art subtraction:** Zmienne tła FLRW, bilans energii promieniowania, równanie Hawkinga, interpolacja tablic i wykrywanie przecięć są znanymi narzędziami. Nowe w obrocie jest **konkretne, falsyfikowalne zastosowanie do implementacji i jej rozdzielczości**, nie roszczenie do odkrycia fizycznego.

**WERDYKT:** `SOURCE-BACKGROUND OFF-GRID TRIPLE CROSSINGS SUPPORTED / OUTPUT SAMPLING FAILS TO RESOLVE BRANCH INTERVAL / ORIGINAL JULIA EXECUTOR NOT RUN / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_PBH_BOUND`.
