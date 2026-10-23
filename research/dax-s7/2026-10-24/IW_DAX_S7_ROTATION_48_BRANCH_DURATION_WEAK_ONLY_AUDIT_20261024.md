# IW/NASH — DAX-S7 — obrót 48

## Długość wielokrotnego przejścia przez T_nuc i kontrola wpływu na X_n (wyłącznie przemiany słabe)

**Data:** 2026-10-24  
**Status:** `ANALYTIC_RADIATION_DOMINATED_SURROGATE / OFF_GRID_THREE_CROSSINGS / SOURCE_WEAK_RATE_ONLY / MAX_BRANCH_GAP_QUANTIFIED / HADRONIC_CHANNEL_OPEN / FULL_JULIA_NOT_RUN / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_PBH_BOUND`

### 1. Pytanie falsyfikacyjne

Obrót 47 wykazał zero trzykrotnych przecięć temperatury nukleosyntezy w 10 000 punktach źródłowej siatki mas PBH × beta, a zarazem wąski warunkowy przedział mas **pomiędzy** tymi punktami, w którym kontrolny model przewiduje trzy przecięcia. Obrót 48 mierzy odstęp czasowy między pierwszym i ostatnim przecięciem, następnie wylicza, jaki wpływ może mieć niejednoznaczność wyboru gałęzi na samą ewolucję neutronów przy **wyłączonych reakcjach hadronowych**.

Źródłowe elementy: `main-scan.jl` (`sortperm(Q ./ T_SM_list)` i interpolacja `X_n(Q/T_nuc)`, wzór `Γ_n_SM`, rozpad `−X_n/τ_n`); `main-scan-parameters.jl` (100 × 100 geometrycznych węzłów), `tool_script-parameters.jl` (`τ_n=878.4 s`, `Q=m_n−m_p`, `T_nuc=0.07818527068831995 MeV`), `tool_script-N_relativistic_species.jl` i PDG2024 (`N_BH` stałe w zakresie skanu). Status source-native dotyczy tych elementów, **nie** całego wykonanego eksperymentu.

### 2. Założenia i algebra modelu kontrolnego

Model: dominacja promieniowania, a(t)/a_f≈(t/t_f)^(1/2), stałe g_* dla ewolucji temperatury, idealna termalizacja masy emitowanej przez PBH w plazmie, bez reakcji hadronowych na neutrony, bez sprzężenia zwrotnego PBH na H. Zgodne ze źródłem prawo masy, z `N_BH=0.007334382996056442`:

- y=M/M_f, τ=(M_f/m_Pl)^3 t_Pl/(3N_BH), t_f=(M_f/m_Pl)t_Pl/γ, γ=1/(3√3).
- ε=β√(τ/t_f), F(y)=∫_y^1 √(1−u³) du, F(0)=0.8413092631952722.
- Przed końcem parowania: t=τ(1−y³), [T(t)/T_nuc]^4=(t_ref/t)²[1+εF(y)]. Po parowaniu składnik F pozostaje F(0).
- T ma minimum dla y=y_min wyznaczonego przez `(2ε/3)(1−y³)^(3/2)/(y²[1+εF(y)])=4`.
- Trzy przecięcia występują, gdy `t_ref,lo=τ/√[1+εF(0)] < t_ref < t_ref,hi=τ(1−y_min³)/√[1+εF(y_min)]`.

Wynik nowy, małe ε: `y_min²≈ ε/[6(1+εF(0))]`; stąd szerokość pasma mas w przybliżeniu

`ΔM/M ≈ (2/3) (ε/6)^(3/2) ∝ β^(3/2)`.

Dodatkowo przy górnej krawędzi pasma mas ostatnie dwa przejścia zlewają się w końcu parowania. Niezerowy korzeń y_edge równania

`1+εF(y_edge) = [1+εF(0)](1−y_edge³)²`

daje **graniczny** odstęp czasowy `Δt_edge = τ y_edge³`, asymptotycznie `τ [ε/(2(1+εF(0)))]^(3/2)`. Dla mas we wnętrzu pasma są trzy odrębne przejścia; na granicy dwa z nich się zlewają. Numeryczna optymalizacja potwierdza zbliżanie się rozpiętości czasowej do tego limitu, ale nie jest to dowód pełnej dynamiki PBH.

### 3. Wyniki: beta=10^−17 (górna granica źródłowego skanu)

| Kalibracja t_ref | Pasmo mas warunkujących trzy przejścia [g] | Graniczny odstęp od pierwszego do ostatniego [s] | ΔX_n dla X_n(t1)=0.11 (przemiany słabe + rozpad) | Δ(2X_n) |
|---|---|---:|---:|---:|
| t_ref=205.204434 s, stałe g | 9.538850832e9–9.539480460e9 | 0.105949858 | −1.43180e−5 | −2.86361e−5 |
| t_ref=208.852533 s, zegar adiabatyczny | 9.595142212e9–9.595781117e9 | 0.108782805 | −1.47009e−5 | −2.94017e−5 |
| t_ref=214.955581 s, zegar kodowy | 9.687868826e9–9.688523192e9 | 0.113577259 | −1.53487e−5 | −3.06975e−5 |

W tabeli `ΔX_n` odpowiada punktowi bardzo bliskiemu górnej krawędzi pasma (nie matematycznie dokładnie krawędzi, gdzie znika środkowa gałąź); rozpiętości czasowe podano z równania granicznego. Przy `t_ref=214.955581 s` i `β=10^−17` wynik `Y_code=2X/(1−X)` zmienia się o około `−3.87539e−5`. Wzór ten jest wcześniej zakwestionowany w audycie obrotów 29–32; podano go wyłącznie dla porównania ze źródłową implementacją, **nie jako poprawną definicję masowego udziału helu**.

### 4. Prawo skali okna i odporność numeryczna

Przy `t_ref=205.204434 s` szerokość przedziału mas wynosi:

| beta | ΔM [g] | Graniczny odstęp czasu [s] |
|---:|---:|---:|
| 1e−17 | 629627.196 | 0.105949858 |
| 1e−18 | 20084.366 | 0.003374096 |
| 1e−19 | 635.689 | 0.000106776 |
| 1e−20 | 20.104 | 0.000003377 |

Dopasowanie log ΔM do log β daje wykładnik ≈1.4987 (w trzech kalibracjach 1.49868–1.49870), zgodny z asymptotyką 3/2. Test `F(y)` niezależną kwadraturą numeryczną w pięciu punktach: maksymalna różnica poniżej 4e−16. Dla środkowej masy każdego pasma temperatury we wszystkich trzech wyznaczonych przecięciach odtwarzają `T_nuc` z błędem względnym poniżej 3e−16. Zapisany skrypt wykonuje test trzech kalibracji × czterech β i neutronową ewolucję dla początkowych X_n=0, 0.11 oraz 1.

### 5. Kontrola oszacowania ΔX_n

Źródłowa przemiana słaba (przy x=Q/T) i rozpad:

`dX/dt = −Γ_SM[T] (X−(1−X)e^(−x)) −X/τ_n`, `Γ_SM = (255/τ_n)(12+6x+x²)/x⁵`.

W temperaturze `T_nuc`, `x≈16.54189`, `Γ_SM≈9.02098e−5 s^−1`, `τ_n^(−1)≈1.13843e−3 s^−1`. Dla `0≤X≤1` i temperatur w obrębie małego impulsu można ograniczyć `|dX/dt|≤Γ_SM(T_max)[1+exp(−Q/T_max)]+1/τ_n`. Przy największej zbadanej rozpiętości `0.113577 s` otrzymano **warunkowe ograniczenie dla samego procesu słabego** `|ΔX|≤1.39546e−4`, bez założenia X(t1)=0.11. Dla rzeczywistej trajektorii warunek X(t1)=0.11 **nie był obliczany przez pełny solver**, lecz stanowi jawnie zadany warunek testowy.

Wynik zmiany `2X_n≈−3.07e−5` to około 1.02% cytowanej w kodzie obserwacyjnej niepewności Y_p równej 0.003. Nie należy jednak utożsamiać tej proporcji z poprawnością lub błędem opublikowanego ograniczenia PBH.

### 6. Granice logiczne i istotny otwarty kanał

**To nie jest oszacowanie wpływu pełnej niejednoznaczności na Y_p**: pominięte tutaj hadrony z emisji PBH mogą indukować szybkie przemiany protonów i neutronów nawet podczas krótkiego końca parowania. Nie wolno dodawać powyższego ograniczenia tylko słabych procesów do pełnej interpretacji fizycznej. Zmiany temperatury i g_* w źródłowym kodzie również nie zostały zintegrowane w tym modelu; trzy wartości `t_ref` są kalibracjami z wcześniejszych eksperymentów, nie source-native predykcjami przy PBH.

W obrębie jawnego modelu kontrolnego: pasma trzykrotnych przejść są niepuste między punktami siatki; w 10 000 punktach skanu z obrotu 47 przejścia potrójne nie wystąpiły. W pełnym Julia liczba przecięć i różnice między gałęziami nadal mają status **NOT_RUN**.

### 7. Weryfikowalny falsyfikator i dalszy test

W oryginalnym solverze Julia należy rejestrować: wszystkie przecięcia `T(a)=T_nuc`, odpowiadający im czas `t` oraz `X_n`, chwilowy impuls w członie hadronowym `dX_n/dt_had`, wynik źródłowej interpolacji sortowanej, stabilność przy zagęszczeniu mas do rozdzielczości poniżej ~1e−5 względnej, tolerancje solvera i warunek końca parowania. Rozdzielić eksperyment z hadronami i bez hadronów. Dopiero na tej podstawie można orzekać o skanie Wu–Xu.

### 8. Reprodukcja i źródła

Pliki towarzyszące:
- `IW_DAX_S7_ROTATION_48_BRANCH_DURATION_WEAK_ONLY_20261024.py` (samodzielny Python, NumPy/SciPy, 3×4 konfiguracje, równanie neutronowe);
- `IW_DAX_S7_ROTATION_48_BRANCH_DURATION_WEAK_ONLY_20261024.csv` (12 wierszy szczegółowych wyników);
- `IW_DAX_S7_ROTATION_48_BRANCH_DURATION_WEAK_ONLY_20261024.json` (podsumowanie i wykładniki).

Źródłowy kod Wu–Xu (repo `Fenyutanchan/Primordial-Black-Hole`, `master`, audytowane w poprzednim obrocie):
- `arXiv-2509.05618/main-scan.jl` — blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`;
- `arXiv-2509.05618/main-scan-parameters.jl` — blob `53faee65beda383348580c28d0424188da69b660`;
- `arXiv-2509.05618/tool_script-parameters.jl` — blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`;
- `arXiv-2509.05618/tool_script-N_relativistic_species.jl` — blob `0437c032bdc4bafca6cb634c0db4cd2c46fb7efc`.

**Prior art subtraction:** Model Hawkinga, FLRW, rachunek czasów reakcji oraz kontrola numeryczna są znanymi narzędziami; nie stanowią odkrycia nowej fizyki. **`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / NO_PBH_BOUND`**.
