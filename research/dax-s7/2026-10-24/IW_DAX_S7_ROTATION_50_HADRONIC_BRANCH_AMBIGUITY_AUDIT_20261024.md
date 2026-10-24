# IW/NASH — DAX-S7 — obrót 50

## Hadronowy falsyfikator gałęzi temperatury: skończone czasy życia sześciu populacji w źródłowym oknie trzech przejść

**Data:** 2026-10-24  
**Status:** `SOURCE-MATCHED LOCAL HADRON SIX-CHANNEL TEST / FINITE-LIFETIME POPULATIONS / OFF-GRID BRANCH / BELOW-TABLE EMISSION EXTRAPOLATION / CONDITIONAL INITIAL_X / FULL_JULIA_NOT_RUN / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / NO_PBH_BOUND`

### 1. Cel, stan wejściowy i wynik

Obrót 49 odtworzył dla autonomicznego źródłowego podukładu tła `main-scan.jl` trzy przecięcia `T=T_nuc` przy `M_f=9.6725×10^9 g`, `beta=1e-17`, poza źródłową siatką mas. Obrót 48 oceniał neutronowy efekt gałęzi tylko od przemian słabych i rozpadu, pozostawiając hadrony jako `NOT_RUN`. Tutaj zbadano lokalnie **wszystkie sześć hadronowych populacji źródłowego kodu**, z produkcją z tablicy `hadrons_from_PBH.dat`, pełnym dla każdej populacji czasem zaniku/anihilacji (a nie wyłącznie quasi-stacjonarnym domknięciem), oraz sprzężeniem ich reakcji z `X_n`.

Dla **warunkowego**, niepochodzącego z pełnego skanu warunku `X_n(t_1)=0.11`, w lokalnym oknie trzech przejść:

- `t_1 = 215.05755469059486 s`, `t_2 = 215.07087213610447 s`, `t_3 = 215.08133566390094 s`, `tau_evap = 215.07211197892192 s`;
- `X_n(t_2) = 0.11146321503`, `X_n(t_3) = 0.11192640915`;
- **`ΔX_n(t_1→t_3) = +0.00192640915`** przy sześciu kanałach i skończonych czasach zaniku;
- identyczny lokalny test ze źródłowymi przemianami słabymi, lecz bez źródeł hadronowych: **`ΔX_n = −0.00000321397`**;
- dla *formuły użytej w implementacji*, `Y_code=2X_n/(1−X_n)`, czysto algebraiczny rozrzut między pierwszą a trzecią gałęzią wynosi `ΔY_code = +0.00487460654`; dla standardowego przybliżenia `2X_n`, `ΔY_std=+0.00385281830`. **Nie jest to błąd wyznaczonego przez publikację Yp**: nie wiadomo, które `X_n(t_1)` dostarczyłby pełny źródłowy solver, a przypadek jest poza oryginalną siatką.

### 2. Podstawa źródłowa i provenance

Repozytorium: `Fenyutanchan/Primordial-Black-Hole`, ścieżka `arXiv-2509.05618/` (publiczny kod pracy Wu–Xu). Podstawy:

- `main-scan.jl` — `dX_n/dt` sumuje standardowe przemiany słabe, rozpad neutronu oraz terminy `pi-`, `pi+`, `K-`, `K0L`, `pbar`, `nbar`. Hadronowe źródła mnożą `dN_over_dt_h(M_PBH) * n_PBH`. Każda populacja ma własne równanie `dn_h/dt=S_h−D_h n_h`; brak rozcieńczenia `3Hn_h` jest cechą oryginalnego kodu, nie poprawką niniejszego testu.
- `tool_script-parameters.jl` — `T_nuc=0.07818527068831995 MeV`, `tau_n=878.4 s`, `eta_B=6.1e−10`, przekroje `σv` w `mbarn`, wzmocnienia Coulomba `Fc_pi−`, `Fc_K−`, współczynniki zaniku hadronów.
- `tool_script-hadrons_from_PBH.jl` — **logarytmiczne interpolatory `dN/dt` z `ExtrapolationType.Linear`** w logarytmie masy PBH.
- `data/out/hadrons_from_PBH.dat`, Git blob SHA: `06d0883a27b108692720422294ba2baacd381a64`; tablica liczy 100 wierszy, a **najmniejsza tablicowana masa to dokładnie 10^9 g**.
- Odtworzenie tła i wartości gałęzi: obrót 49, `IW_DAX_S7_ROTATION_49_SOURCE_BACKGROUND_BRANCH_ALIASING_AUDIT_20261024.md`. To nie jest źródłowy pełny solver Julia.

### 3. Kluczowe ograniczenie empiryczne: cały badany epizod leży poniżej zakresu emisji

W pierwszym przejściu `y=M/M_f≈0.04075355`, więc `M≈3.9418873×10^8 g`, a w drugim `y≈0.01793057`, `M≈1.7343347×10^8 g`. Obie masy leżą poniżej najniższego węzła danych `10^9 g`; przez cały okres `t_1→tau_evap` użyta emisja wynika z **ekstrapolacji**.

Dlatego, w obrębie tego okna, dwa pierwsze wiersze danych źródłowych dają **dokładnie** ten sam przepis emisji, co wszystkie 100 wierszy przy interpolacji liniowej w `ln(M), ln(dN/dt)`. W kodzie odtwarzającym zapisano dosłownie te dwa wiersze; efektywne wykładniki `dN/dt ∝ M^p`: `p_pi=−1.200485626`, `p_K=−1.196651351`, `p_K0=−1.196804841`, `p_p=−1.204291429`, `p_n=−1.204763064`.

**To jest rekonstrukcja semantyki ekstrapolacji kodu, nie niezależne potwierdzenie zachowania fizycznego przy `M<10^9g`.** Kontrola ze sztucznie stałym `dN/dt(M≤10^9g)=dN/dt(10^9g)` daje `ΔX_n=+0.00037504106`, około pięciokrotnie mniejsze. Kontrola z emisją zerowaną poniżej tabeli zwraca wynik weak-only. Alternatywne reguły nie są roszczeniem do lepszego modelu: mają ujawnić zależność od ekstrapolacji.

### 4. Metoda: sześć populacji i reakcje neutronowe ze skończonymi czasami życia

Lokalnie ustalono `T=T_nuc` i `n_PBH` na wartości z pierwszego przejścia: w oknie zmiana `ln a` wynosi tylko `~5.8e−5`, więc sam względny ubytek `n_PBH∝a^-3` jest `~1.7e−4`; nie zastępuje to jednak sprzężonego całkowania całej historii tła. `n_B=eta_B*(2ζ(3)/π²)T³` zgodnie z kodem, `rho_SM=(π²/30)g_rho T⁴`. Stosowano jednostki naturalne `hbar=6.582119569e−25 GeV*s`, `1 mb=1/0.389379338 GeV^-2`, masy w `GeV`.

- Każda z 6 populacji: `dn_i/dt = S_i(t)−D_i(X_n,T)n_i`. Użyto źródłowych `S_i` i `D_i`; zanik/anihilację w pojedynczym kroku liczono dokładnym operatorem wykładniczym `n' = exp(−DΔt)n + (1−exp(−DΔt))S/D`, z wyznaczeniem punktu pośredniego dla `X_n`.
- Dla `t_1<t<tau_evap` zmienną niezależną jest `y=M/M_f`, z dokładną formułą `dt = −3τ y² dy`. Po zaniku PBH źródła hadronowe są zerowane i pozostają ich skończone czasy zaniku.
- Warunek `n_i(t_1)=S_i(t_1)/D_i(t_1)` jest **lokalnym przybliżeniem początkowym**, nie odczytem z pełnego solvera. W pierwszym przejściu tempa zaniku `pi±~3.84e7 s^-1`, `K−~8.10e7 s^-1`, `K0L~2.00e7 s^-1`, `pbar~9.98e3 s^-1`, `nbar~8.03e3 s^-1`. Integralna kontrola z tym założeniem jest znacznie silniejsza niż czysto quasi-stacjonarna, lecz nie dowodzi identyczności całej historii hadronów.
- Nie obejmuje się `−3Hn_h`, którego nie ma w źródłowej implementacji. Nie uwzględnia się sprzężenia zwrotnego `X_n` i hadronów do tła, którego źródłowy kod także nie przewiduje.

### 5. Wyniki wrażliwości na `X_n(t_1)`

| Warunkowy `X_n(t_1)` | `X_n(t_2)` | `X_n(t_3)` | `ΔX_n(t_1→t_3)` |
|---:|---:|---:|---:|
| 0.08 | 0.081579566 | 0.082079978 | +0.002079978 |
| **0.11** | **0.111463215** | **0.111926409** | **+0.001926409** |
| 0.20 | 0.201117594 | 0.201470342 | +0.001470342 |
| 0.40 | 0.400362431 | 0.400474269 | +0.000474269 |
| 0.60 | 0.599613806 | 0.599487035 | −0.000512965 |
| 0.80 | 0.798858236 | 0.798490433 | −0.001509567 |

**Ważne:** skala, a nawet znak zmiany, zależą od nieznanego faktycznego `X_n` w pierwszym przejściu. Wartość `0.11` jest testową kotwicą, nie wiążącą predykcją modelu PBH.

### 6. Falsyfikacja kanałów i ekstrapolacji przy kotwicy `X_n(t_1)=0.11`

| Aktywne źródła | Zmiana `X_n` |
|---|---:|
| Wszystkie sześć | +0.001926409 |
| Żadne — tylko weak + decay | −0.000003214 |
| Tylko piony | −0.000002638 |
| Tylko kaony | −0.000002150 |
| Tylko `pbar` i `nbar` | +0.001924776 |
| Tylko `nbar` | +0.002140853 |
| Tylko `pbar` | −0.000217482 |
| Wszystkie, emisja sztucznie stała poniżej tabeli | +0.000375041 |

Kontrole kanałowe nie są addytywną dekompozycją liniową, bo tempa i liczebności hadronów zależą od `X_n`. Pokazują jednak jednoznaczną dominację antynukleonów w tym lokalnym modelu, z częściową kompensacją wpływu `pbar` i `nbar`.

### 7. Zbieżność i czułość na czas przejść

Dla `X_n(t_1)=0.11` i całkowania populacji przez odpowiednio `3000, 6000, 12000, 24000, 48000` kroków w `y` uzyskano `ΔX_n = 0.00192641241, 0.00192640997, 0.00192640933, 0.00192640915, 0.00192640910`. Numeryczna zbieżność **lokalnego** integratora jest znacznie lepsza niż niepewność fizycznych i numerycznych warunków wejściowych.

Przy podstawieniu czterech zestawów czasów przejść z obrotu 49 otrzymano orientacyjny przedział `ΔX_n≈0.00191–0.00203` (przy skorygowaniu `n_PBH(t_1)` o odpowiadający mu `ln a`). Jest to próba wrażliwości, **nie formalny przedział ufności**, ponieważ błąd pełnego solvera Julia i dokładna dynamika tła nie zostały zweryfikowane.

### 8. Pozostające niewiadome i falsyfikator źródłowy

`NOT_RUN`: pełny oryginalny Julia executor z 10 zmiennymi stanu i adaptacyjnym algorytmem; faktyczne `X_n(t_1)`; źródłowe `n_h(t_1)`; dokładne sprzężenie `T(t)` w wąskim oknie; wpływ przejścia z `n_h` do wartości logarytmicznych na końcu parowania; porównanie `X_n` zwracanego przez sortowany interpolator `X_n(Q/T)` z `X_n` na trzech fizycznych przecięciach i oryginalnym opublikowanym skanem. `NOT_VALIDATED`: emisja poza zakresem tabeli; poprawność fizyczna ekstrapolacji potęgowej.

**Falsyfikatorem rozstrzygającym** jest test na pierwotnym `main-scan.jl` z parametrami `M_f=9.6725e9 g`, `beta=1e-17`, zdarzeniami `T−T_nuc=0`, rejestracją 6 `n_h` i `X_n` przy wszystkich 3 zdarzeniach, zmianą tolerancji, oraz osobnym ograniczeniem interpolacji źródeł hadronowych do zakresu danych. Następnie porównać wynik do `Y_p` z rutyny bazowej oraz do zagęszczonego skanu mas, nie ekstrapolując ustaleń off-grid na opublikowane granice.

### 9. Artefakty i kontrola wykonania

- `IW_DAX_S7_ROTATION_50_HADRON_FINITE_LIFETIME_20261024.py`: samowystarczalny skrypt Python (bez potrzeby pobierania tabel) **w obrębie lokalnego epizodu**, ponieważ umieszcza dokładnie dwa wystarczające wiersze źródłowej tablicy. Implementuje źródłowe przekroje, emisje, zanik 6 populacji i ewolucję `X_n`; `SELF-CHECK PASS`.
- `IW_DAX_S7_ROTATION_50_HADRON_FINITE_LIFETIME_20261024.json`: komplet danych liczbowych, kontrole kanałów i zbieżność.
- `IW_DAX_S7_ROTATION_50_RUN_LOG_20261024.txt`: rezultat faktycznego wykonania skryptu w bieżącym środowisku Python.

**Wniosek:** `LOCAL_SOURCE_HADRON_BRANCH_EFFECT_SUPPORTED / ANTINUCLEON_DOMINATED / QUANTITATIVE_VALUE_EXTRAPOLATION_DEPENDENT / FULL_JULIA_NOT_RUN / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_PBH_BOUND`.