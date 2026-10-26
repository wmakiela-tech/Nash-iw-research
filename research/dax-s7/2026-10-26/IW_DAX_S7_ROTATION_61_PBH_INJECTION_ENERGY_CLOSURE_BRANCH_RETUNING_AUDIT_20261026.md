# IW/NASH — DAX-S7 — obrót 61

**Tytuł:** Emisja PBH nie znosi reszty równania energii; rozbieżne progi ogrzewania i przesunięcie wąskiej gałęzi potrójnego przejścia \(T_{\rm nuc}\)  
**Data:** 2026-10-26  
**Tryb:** SCIENCE_FIRST / INDEPENDENT_FALSIFIER / SOURCE_TYPED / NO_EXEC / NO_CANON  
**Status:** `INJECTION_CONTINUITY_CANCELLATION_EXACT / HEATING_THRESHOLD_DISAGREEMENT / CONDITIONAL_BRANCH_RETUNING_CONFIRMED / FULL_JULIA_NOT_RUN / NO_PBH_BOUND / NO_CANON`

## 1. Pytanie i falsyfikator

Obroty 59–60 wykazały przy braku PBH rozbieżność między równaniem \(d\ln\rho_{\rm SM}/d\ln a\) w `main-scan.jl` oraz bilansem energii opartym na niezależnie wyliczonym ciśnieniu fermionów. Pytanie R61: czy jawne włączenie źródła Hawkinga tę resztę znosi, czy zmienia progowy znak \(\dot T\), oraz czy wąskie potrójne przecięcie \(T_{\rm nuc}\) znika, czy przesuwa się po zmianie termodynamicznego członu równania?

Odpowiedź złożona:

1. **Algebraicznie, przy identycznym źródle energii po obu stronach bilansu, emisja PBH znosi się z reszty.** Niespójność istnieje także dla \(\beta>0\) przy ustalonym T.
2. **Próg lokalnego przejścia chłodzenie→ogrzewanie zależy od wyboru zamknięcia termodynamicznego**; przy \(T_{\rm nuc}\) szerokość przedziału przeciwnych znaków wynosi 0.096381 w \(I\).
3. **Potrójne przejście nie znika jako topologia w porównawczym jednoparametrowym modelu:** na oryginalnym punkcie dostrojenia zmienia się z 3 na 1, ale po dostrojeniu masy o około −0.95% wraca do 3. To **nie** test pełnej, fizycznie poprawnej ewolucji dwóch sektorów.

## 2. Źródła i zakres zgodności

- Publikacja Wu–Xu, *Primordial Black Holes Evaporating before Big Bang Nucleosynthesis*, `arXiv:2509.05618v3`, https://arxiv.org/html/2509.05618v3, równania (2.7), (2.9)–(2.10), (3.3) oraz §3 o oddzielnych sektorach EM i neutrin; w (2.7) autorzy deklarują zachowanie entropii współporuszającej w scenariuszu standardowym.
- `Fenyutanchan/Primordial-Black-Hole/arXiv-2509.05618/main-scan.jl`, Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`: `d_log_ρ_SM_dη = -4 + r/(3+s) - (dm/dt)nPBH/(HρSM)`.
- `tool_script-N_relativistic_species.jl`, blob `0437c032bdc4bafca6cb634c0db4cd2c46fb7efc` — sposób generacji \(g_\rho,g_s\) oraz 1000-punktowego odwrotnego interpolatora \(\rho\to T\).
- Źródłowe tablice: `data/ext/N_around_m_e.csv` blob `93f2494f026c5d0587ea40fe08bb938dd9d01fa8`; `N_s_from_PDG2024.csv` blob `33aceb876fc36cb2486d36c690e6401d85d76b46`; `N_rho_OVER_N_s_from_PDG2024.csv` blob `28b0c13563d7b3bdeaee191a3a981197345d05b8`.
- Wejście lokalnego programu Python: **13 próbek interpolacji źródłowych** z R59 (`...ROTATION_59_PAPER_CODE_NEUTRINO_ENTROPY_COMPARISON...csv`, blob `a1934e09b02d797a7b759510da99b10e1facfa97`), kontrolowane niezależnymi całkami Fermiego–Diraca; punkty R60 blob `37e9220244840d7a2d122db38115ab6d54a60419`. Pełne trzy tabele źródłowe pobrano i przetworzono **odrębnie w połączonym środowisku narzędziowym** do testu trajektorii; nie pobrano ich do lokalnego kontenera Pythona z uwagi na brak sieci.

Zadeklarowane wyżej SHAs zweryfikowano wobec bieżących plików publicznego repozytorium w R61.

## 3. Dokładna tożsamość bilansu z wtryskiem

Zdefiniujmy \(I\equiv-\dot M_{\rm PBH}n_{\rm PBH}/(H\rho_{\rm SM})\geq0\). Kod stosuje

\[
C_{\rm src}(T)=-4+\frac{r}{3+s},\qquad
\frac{d\ln\rho_{\rm SM}}{d\ln a}=C_{\rm src}(T)+I,\quad
r=\frac{d\ln g_\rho}{d\ln T},\ s=\frac{d\ln g_s}{d\ln T}.
\]

W jednoparametrowym zamknięciu termodynamicznym z \(\rho(T)\) oraz ciśnieniem \(p(T)\), pełne równanie energii z **tym samym** źródłem jest

\[
\dot\rho_{\rm SM}+3H(\rho_{\rm SM}+p_{\rm SM})=I H\rho_{\rm SM},\quad
C_{\rm EOS}(T)=-3\left(1+\frac{p}{\rho}\right).
\]

Po wstawieniu kodowego \(d\ln\rho/d\ln a\), znormalizowana reszta wynosi **dokładnie**

\[
\boxed{\mathcal R_E=\frac{\dot\rho+3H(\rho+p)-I H\rho}{H\rho}
=C_{\rm src}(T)-C_{\rm EOS}(T)},
\]

czyli **nie zależy jawnie od \(I\)** przy zadanym \(T\). Jest to tożsamość algebraiczna, nie numeryczna korelacja. Jeśli dla formalnego testu tylko ułamek \(f\) nominalnego źródła zasila śledzony sektor, wówczas \(\mathcal R_E=C_{\rm src}-C_{\rm EOS}+(1-f)I\). **Parametr \(f\) jest wyłącznie zmienną rachunkową**, nie znaną frakcją depozycji rzeczywistego Hawkinga.

Tablica R60 dostarcza \(C_{\rm EOS}\) z fizycznego \(\rho,p\): energia/ciśnienie e± z niezależnych całek Fermiego–Diraca, fotony, bezmasowe rozsprzęgnięte neutrina, ich stosunek temperatur rekonstruowany z tablicy. Równanie z entropii użyte jako drugi kontrolny kontrakt: \(C_{\rm paper}=-3(4+r)/(3+s)\). Są zgodne na poziomie reszty interpolacji tablic, a nie algebraicznie identyczne w każdej temperaturze.

## 4. Próg zmiany znaku pochodnej temperatury

Ponieważ \(\rho\propto g_\rho(T)T^4\), to

\[
\frac{d\ln T}{d\ln a}=\frac{C(T)+I}{4+r(T)},\qquad
\text{grzanie: }I>-C(T).
\]

W punkcie \(T_{\rm nuc}=0.07818527068831995\ \mathrm{MeV}\), z 13 zweryfikowanych próbek i ponownie obliczonych całek EOS:

| Parametr | Wartość |
|---|---:|
| \(r=d\ln g_\rho/d\ln T\) | 0.44011773576 |
| \(s=d\ln g_s/d\ln T\) | 0.35905813093 |
| \(C_{\rm src}\) | −3.86897585019 |
| \(C_{\rm EOS}\) z niezależnego ciśnienia | −3.96535697427 |
| \(C_{\rm paper}\) z entropii | −3.96550243791 |
| **\(\mathcal R_E=C_{\rm src}-C_{\rm EOS}\)** | **+0.09638112408** |
| **Lokalny przedział przeciwnych znaków \(\dot T\)** | **3.86897585 < I < 3.96535697** |
| Przedział względem progu EOS | 2.4306% |

Np. dla **formalnego** \(I=3.900\) otrzymujemy \(d\ln T/d\ln a=+0.00698724\) w kodzie, ale \(−0.01471965\) z bilansem energii. W obu wariantach przyjęto **identyczny** dodatni wkład \(I\), więc przeciwny znak nie pochodzi z modyfikacji emisyjności PBH.

Przy \(T=0.100\ \mathrm{MeV}\) kodowy i EOS-owy próg grzania wynoszą odpowiednio 3.8008988 i 3.9317649, stąd **szerszy** przedział przeciwnych znaków (szerokość 0.1308661).

**Uwaga:** wartości \(I\) z tej tabeli są wymuszonymi parametrami kontrolnymi. Tabela *nie* twierdzi, że dokładnie taki \(I\) występuje w dowolnym fizycznym punkcie skanu.

## 5. Przesunięcie gałęzi przy podmienionym chłodzeniu — odrębny test numeryczny

Przetworzono wszystkie oryginalne 1000 wierszy \(g_\rho,g_s\), tablice PDG oraz zdefiniowany w kodzie 1000-punktowy interpolator \(\rho\mapsto T\). W niezależnym implementacyjnym porcie JS rozwiązywano równania tła dla dwóch zamknięć:

- **`source`:** źródłowe \(C_{\rm src}\) i źródłowe \(I\).
- **`paper_entropy_baseline_plus_same_PBH`:** tylko podstawienie \(C_{\rm paper}\) zamiast \(C_{\rm src}\), **przy tym samym** \(I\), prawie \(M(t)\), \(H(\rho_{\rm SM}+\rho_{\rm PBH})\) i tablicach. To *kontrola strukturalna*, nie pełne rozwiązanie fizyczne \(T_\gamma,T_\nu\) z rzeczywistymi frakcjami depozycji.

Parametry: \(\beta=10^{-17}\). Trzy niezależne zagęszczenia \(N_x/N_y=(6000/10000,9000/15000,13000/22000)\), \(x=\ln(t/t_f)\) do \(y=M/M_f=1/2\), następnie RK4 po \(y\) do parowania i krótki odcinek poparowy. Testowe masy:

| Masa początkowa PBH | Zamknięcie | Przejścia przez \(T_{\rm nuc}\) | Orientacyjne czasy przecięć [s] |
|---|---|---:|---|
| \(9.6725\times10^9\) g | źródłowe | **3** | 215.0578; 215.0708; 215.0814 |
| \(9.6725\times10^9\) g | papierowy człon chłodzenia | **1** | 208.8052 |
| \(9.58055228\times10^9\) g | papierowy człon chłodzenia | **3** | 208.9702; 208.9965; 209.0033 |

Trójprzejściowość była stabilna **jako liczba zdarzeń** we wszystkich trzech rozdzielczościach dla obu dostrojonych przypadków. Dokładne czasy zmieniały się o rząd \(10^{-4}\)–\(10^{-3}\) s; nie należy podawać ich z pozornie większą precyzją.

Zmiana masy między zademonstrowanymi przykładami wynosi \(91\,947\,720\ \mathrm{g}\), tj. ok. **0.9506%** wyjściowej masy. **To nie jest uniwersalny ani dokładnie wyznaczony shift granicy zjawiska**: porównuje dwa jawne punkty potrójnych przecięć, a nie pozycje identycznie zdefiniowanych granic przedziału. Wartość \(9.58055228\times10^9\ \mathrm{g}\) jest punktem w wąskim oknie i nie reprezentuje nowej fizycznej granicy.

**Krytyczna autokorekta:** W jednym pomocniczym teście tło źródłowe przy niższej masie nie przecięło \(T_{\rm nuc}\) podczas zbyt krótkiego **0.15 s** odcinka po parowaniu. Nie należy traktować tego wyniku jako braku przecięcia w całym czasie — źródłowe tło może przeciąć próg kilka sekund później. Skrypt lokalny zawiera dodatkowy długi odcinek kontrolny, jeśli nie wystąpiło żadne przecięcie.

## 6. Granica odpowiedniości modelu przy emisji do różnych sektorów

Sama publikacja w §3 rozpoznaje, że po rozsprzęgnięciu neutrin promieniowanie PBH rozdziela się między sektor EM i sektor neutrin. Jeżeli \(Q_{\rm EM}\) oraz \(Q_\nu\) oznaczają ich objętościowe dopływy energii, poprawna struktura bilansu wymaga co najmniej

\[
\dot\rho_{\rm EM}+3H(\rho_{\rm EM}+p_{\rm EM})=Q_{\rm EM},\qquad
\dot\rho_\nu+4H\rho_\nu=Q_\nu,
\]

oraz ewolucji \(T_\gamma,T_\nu\) lub funkcji rozkładu po wtrysku, uwzględniającej odpowiedni transfer międzysektorowy. Funkcja \(g_\rho(T_\gamma)\) ze źródłowej tabeli koduje **konkretny** przebieg \(T_\nu/T_\gamma\) przy standardowym chłodzeniu; nie jest automatycznie poprawnym jednoparametrowym EOS po arbitralnym oddaniu energii przez PBH do obu sektorów. Stąd prosta zamiana \(C_{\rm src}\mapsto C_{\rm paper}+I\) **nie jest gotową poprawką publikacji** ani uzasadnionym nowym ograniczeniem na \(\beta\).

## 7. Wykonane kontrole, negatywna wiedza i dalsze zadanie

**Wykonane:**

- Zweryfikowano aktualne blob SHA trzech oryginalnych tablic i obu źródłowych plików Julia.
- W lokalnym Python/SciPy **ponownie uruchomiono 13 całek Fermiego–Diraca** i porównano uzyskane \(C_{\rm EOS},\mathcal R_E\) z wynikami R60 przy tolerancji \(10^{-11}\).
- Dla 18 wartości \(I\) i trzech formalnych udziałów źródła \(f\) zweryfikowano dokładną tożsamość reszty i znaki temperatury — 54 testowane warianty; plus 13 temperatur w tabeli progów.
- W niezależnym porcie JS na **pełnych źródłowych tablicach** wykonano warunkowy test trajektorii \(\beta>0\) na trzech siatkach dla trzech kombinacji masy/zamknięcia (9 przypadków w CSV). Dostępny skrypt Python ma tryb `--background` pobierający **lokalnie dostarczone oryginalne CSV** i sprawdzający SHA; ten tryb nie został uruchomiony w tym środowisku z powodu braku lokalnych źródeł.
- Lokalne testy Pythona: składnia, limity Fermiego–Diraca, `--selftest`, algebra oraz syntetyczny test modułu trajektorii dla stałego \(g_*\) — PASS.

**Niewykonane:** oryginalny solver Julia, fizyczny transport EM–neutrina, sieć jąder BBN, skan granic \(\beta\), publikacyjny EXEC. Nie używać oznaczeń `discovery`, `PBH_BOUND`, `CANON`, `EXEC_SIGN`.

**Najbliższy falsyfikator:** w Julii uruchomić na tych samych dwóch masach `(β=0, 1e−17)` z pomiarem `I, C, ρ,p, ln(a), Tgamma, Tnu` i jednoczesnym zastąpieniem jednoparametrowego `g*(T)` przez ewolucję sektorową; sprawdzić czy trzy przecięcia istnieją, gdzie są, i czy wpływają na rzeczywiste \(X_n\). Priorytetem nie jest kolejna zmiana parametrów w modelu warunkowym, lecz **domknięcie fizyczne depozycji energii**.

**Werdykt:** `SOURCE_ENERGY_RESIDUAL_SURVIVES_EQUAL_PBH_INJECTION / CONDITIONAL_HEATING_SIGN_DISAGREEMENT / TRIPLE_CROSSING_RELOCATED_NOT_ELIMINATED_IN_TOY_CLOSURE / TWO_SECTOR_OPEN / FULL_JULIA_NOT_RUN / NO_EXEC / NO_CANON`.
