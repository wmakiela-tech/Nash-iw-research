# IW/NASH — DAX-S7 — obrót 47

## Czy źródłowa siatka skanu Wu–Xu zawiera wielokrotne przecięcia T_nuc? Test analityczny modelu kontrolnego

**Data:** 2026-10-23  
**Status:** `10000-SOURCE-GRID-POINTS / RADIATION-DOMINATED-SURROGATE / CONDITIONAL-GRID-NEGATIVE / CONTINUOUS-MASS-WINDOW-FOUND / FULL-JULIA-NOT-RUN / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE`

### 1. Źródła i zakres twierdzenia

Sprawdzono publiczne pliki repozytorium Wu–Xu `Fenyutanchan/Primordial-Black-Hole`, folder `arXiv-2509.05618`: `main-scan.jl`, `main-scan-parameters.jl`, `tool_script-parameters.jl`, `tool_script-N_relativistic_species.jl` oraz źródłowe tablice PDG2024. Zakres źródłowy: 100 mas początkowych z `[6e8,1e10] g`, 100 wartości `β` z `[1e-20,1e-17]`, oba ciągi `geomspace`. Kod oblicza `Xn(T_nuc)` poprzez `sortperm(Q ./ T_SM_list)` i `LinearInterpolation`, więc gdy T(a) nie jest różnowartościowa, odczyt wymaga testu gałęzi czasowej.

**Źródłowo zweryfikowane:** skan parametrów i interpolator, prawo `dM/dt=-N_BH m_Pl⁴/M²`, stały N_BH w skanie (dzięki stałej ekstrapolacji PDG przy Hawking T >~ 1 TeV), próg zaniku `M_f exp(-20)` i `T_nuc=0.07818527068831995 MeV`. Wartość `N_BH=0.007334382996056442`.

**Nieźródłowe przybliżenia:** promieniowanie dominuje, `a/a_f≈sqrt(t/t_f)`, `H≈1/(2t)`, stałe stopnie swobody i pełna termalizacja emisji, zaniedbany feedback PBH na H. Żadnego pełnego rozwiązania Julia, żadnej interpretacji ograniczeń PBH.

### 2. Konstrukcja falsyfikatora

Niech `y=M/M_f`, `τ=(M_f/m_Pl)³t_Pl/(3N_BH)`, `ε=β sqrt(τ/t_f)` i `t_f=M_f t_Pl/(γ m_Pl)`, gdzie `γ=1/(3sqrt(3))`. W granicy `t_f/τ -> 0` zachodzą

` t(y)=τ(1-y³)`, `F(y)=∫_y^1 sqrt(1-u³)du`, `F(0)=0.8413092631952722`,

` E_R(y)/E_R,f=1+εF(y)` i `ρ_R(t)/ρ_nuc = (t_ref/t)² [1+εF(y)]`.

Całka `F(y)` była obliczana bez aproksymacji małego y jako `F(0)*[1-I_(y³)(1/3,3/2)]` (`scipy.special.betainc`). Chwilowe ponowne ogrzewanie w tym modelu zaczyna się przy `I(y)=4`, gdzie

`I(y)=(2ε/3)*(1-y³)^(3/2)/[y²(1+εF(y))]`.

Dla pierwiastka `y_min` tego równania otrzymujemy

` t_ref,low=τ/sqrt[1+εF(0)]`,  `t_ref,high=τ(1-y_min³)/sqrt[1+εF(y_min)]`.

**Trzykrotne przecięcie T_nuc jest możliwe w modelu kontrolnym dokładnie wtedy, gdy** `t_ref,low < t_ref < t_ref,high`, przy wyjściu z temperatury początkowej większej od T_nuc. Na końcu parowania temperatura ma lokalne maksimum, na początku ponownego ogrzewania — minimum. Inne liczby przecięć i efekty oscylacyjne nie są wykluczane przez ten test w pełnej dynamice Julia.

Przyjęto `t_ref=1/(2 H(T_nuc))`, `H(T)=0.2066 sqrt(g_rho(T)) T_MeV² s^-1` i źródłowe `g_rho(T_nuc)=3.722254946361439`; daje to `t_ref=205.2044342176 s`. To **kalibracja modelu kontrolnego**, nie source-native czas BBN.

### 3. Wyniki pełnej 100 × 100 źródłowej siatki w modelu kontrolnym

| Wielkość | Wynik |
|---|---:|
| Punkty siatki | 10 000 |
| Punkty o trzykrotnym przejściu dla t_ref=205.2044 s | **0** |
| Punkty o trzykrotnym przejściu dla t_ref=208.8525 s | **0** |
| Punkty o trzykrotnym przejściu dla t_ref=214.9556 s | **0** |
| Maksymalna długość przedziału możliwego trzykrotnego przejścia w t_ref | **0.0501057 s** |
| Bezpieczna luka między pasmami wszystkich mas/β blisko T_nuc | **(200.407561, 217.041395) s** |
| Stosunek sąsiednich mas źródłowego skanu | 1.02882594 |

Zmienna `t_ref` może ulegać zmianie po uwzględnieniu zmiennych stopni swobody: dwa dodatkowe testy wykorzystują wcześniej obliczone w kontrolnym modelu zegary chłodzenia przy `T_nuc`: adiabatyczny `208.852533 s` i kodowy `214.955581 s` (oba od T0=5 MeV, z przybliżonym H). W **każdym** z trzech testów uzyskano zero przecięć wielokrotnych na źródłowej siatce. **Nie wynika z tego** zero w rzeczywistych trajektoriach PBH; wpływ zmiennego g* i sprzężenia dynamiki pozostaje otwarty.

Przy `β=1e-17` dwa najbliższe węzły mas dają:

| M_f [g] | τ [s] | Zakres t_ref potrzebny do trzech przecięć [s] |
|---:|---:|---:|
| 9.447484474e9 | 200.408642 | 199.335076 – 199.373921 |
| 9.719817115e9 | 218.243926 | 217.041395 – 217.085513 |

### 4. Nowy wynik: istnienie wąskiego okna między węzłami

Dla `β=1e−17` i `t_ref=205.204434 s`, rozwiązując warunek na **ciągłą**, a nie dyskretną masę, znaleziono:

`M_low = 9 538 850 832.437 g`, `M_high = 9 539 480 459.632 g`.

Szerokość `ΔM=629 627.196 g`, czyli `ΔM/M_low≈6.60066e−5=0.00660066%`. Przedział leży między sąsiednimi punktami źródłowymi 9.4475e9 i 9.7198e9 g. Jest to ścisły w zakresie przyjętych równań modelu kontrolnego **przykład okna, które skan może pominąć**. Nie wolno z tego wnioskować, że Wu–Xu faktycznie mają trzy przecięcia, błędny Yp lub nowy wynik fizyczny.

### 5. Kontrole jakości i falsyfikatory

- `F(y)` obliczono z niezupełnej funkcji beta, bez lokalnej aproksymacji szeregowej; `y_min` znaleziono przez Brent (`scipy.optimize.brentq`).
- Zbadano jawnie wszystkie 10 000 węzłów; wynik zapisano w CSV zawierającym `t_ref,low`, `t_ref,high`, `q_min`, `q_end` oraz trzy flagi przecięć.
- Próg źródłowego chłodzenia w punkcie T_nuc to `I_crit≈3.869`, a próg modelu o stałym g to `I_crit=4`. **Nie utożsamiać obu modeli**.
- Weryfikacja źródłowa wymaga pełnego Julia 100×100: monitorować `T(a)`, `I(a)`, liczyć wszystkie przecięcia `T_nuc`, odczyty `Xn` na każdej gałęzi, tolerancje adaptacyjnego solvera oraz `sortperm`-interpolację. Osobno wykonać gęstą siatkę między 9.4475e9 i 9.7198e9 g (oraz szerszy zakres, jeśli źródłowy zegar wskaże inną epokę).

### 6. Epistemic status i prior-art subtraction

Wnioski opar­te na prawie Hawkinga, dynamice FLRW i bilansie energii stanowią zastosowanie istniejącej fizyki, **nie propozycję nowej teorii IW/NASH**. `SOURCE-GRID-SURROGATE_NEGATIVE` nie jest równoznaczne z `SOURCE-NATIVE_JULIA_NEGATIVE` ani dowodem braku wielokrotnych przejść w continuum. `NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_PBH_BOUND`.

### 7. Artefakty odtwarzalności

- `IW_DAX_S7_ROTATION_47_REHEATING_GRID_SURROGATE_20261023.py` — pełen kod testu, wymaga Python, NumPy, SciPy.
- `IW_DAX_S7_ROTATION_47_REHEATING_SOURCE_GRID_10000_20261023.csv` — wszystkie 10 000 przypadków.
- `IW_DAX_S7_ROTATION_47_REHEATING_GRID_SUMMARY_20261023.json` — podsumowanie walidacyjne.

### 8. Źródła — repozytorium i blob SHA

`Fenyutanchan/Primordial-Black-Hole` (gałąź `master`):
- `arXiv-2509.05618/main-scan.jl` — `b368ba55d5a493f7bc185909730f7fe5691f10d6`
- `arXiv-2509.05618/main-scan-parameters.jl` — `53faee65beda383348580c28d0424188da69b660`
- `arXiv-2509.05618/tool_script-parameters.jl` — `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`
- `arXiv-2509.05618/tool_script-N_relativistic_species.jl` — `0437c032bdc4bafca6cb634c0db4cd2c46fb7efc`
- `arXiv-2509.05618/data/ext/N_s_from_PDG2024.csv` — `33aceb876fc36cb2486d36c690e6401d85d76b46`
- `arXiv-2509.05618/data/ext/N_rho_OVER_N_s_from_PDG2024.csv` — `28b0c13563d7b3bdeaee191a3a981197345d05b8`