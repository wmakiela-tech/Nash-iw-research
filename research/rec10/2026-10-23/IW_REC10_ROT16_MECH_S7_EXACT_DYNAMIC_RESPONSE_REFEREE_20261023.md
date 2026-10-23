# IW/NASH — REC10 ROT16
## Dokładna odpowiedź różnicowa modelu 7D: emisja → populacje → neutrony

**Data:** 2026-10-23  
**Komórka:** `IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10`  
**Związek:** `MECH-S7-FRONTB-EXACT-MASS-7D-DYNAMIC-SOURCE-AMPLITUDE-AND-MEMORY-GATE-006_20261023`  
**Problem:** `P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001`  
**Werdykt:** `PASS_WITH_EXACT_STRENGTHENING`  
**Typ:** matematyczny model warunkowy i syntetyczny test różnicowego układu 7D.  
**Granice:** `NO_SOURCE_VALID_E2B / NO_10D_JULIA_REPLAY / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE`.

## 1. Źródła i zakres kontroli

Przeczytano:
- pełny raport Mech-S7 `research/mech-s7/2026-10-23/mech_s7_frontb_exact_mass_7d_dynamic_source_amplitude_gate_006.md`, Git blob `3f6b0cc169e83e8c90470923afda9e37694571e8`;
- wykonywalny skrypt `terminal_7d_exact_mass_common_background_006.py`, Git blob `f2c0ea34d3a6a379bc8b3477ef25673f01ae2412`;
- oryginalny `main-scan.jl`, `tool_script-parameters.jl` i `tool_script-hadrons_from_PBH.jl` w `Fenyutanchan/Primordial-Black-Hole` przy commit `d395183674cace6c9906a8911bdeb7234ba4040d`.

Niezależnie porównano: przemiany słabe neutronów, dodatnie/ujemne kierunki sześciu reakcji, utratę populacji π⁻,π⁺,K⁻,K0L,pbar,nbar, temperaturę i przeliczniki mbarn·c, a także wzór wymuszenia źródłowego i rozdzielenie emisji PBH od istniejących populacji hadronów. Na tym poziomie **PASS**.

Nie przeprowadzono nowych obliczeń z surowych archiwów Actions ani nowego całkowania oryginalnego modelu 10D w Julii. Przytoczone wielkości źródłowego testu amplitudy Mech-S7 są zatem **danymi Mech-S7**, nie niezależnie odtworzonym wynikiem REC10.

## 2. Dokładna struktura dla modelu na wspólnym tle

Dla każdej gałęzi \(r\in\{p,u\}\), gdzie \(p=\mathrm{paper}\), \(u=\mathrm{public}\), mamy
\[
\dot X_r = U(t)-\lambda(t)X_r
+\sum_{i=1}^6[a_i(t)-(a_i(t)+b_i(t))X_r]n_{i,r},
\]
\[
\dot n_{i,r}=S_{i,r}(t)-[d_i(t)+\xi_i(t)X_r]\,n_{i,r}.
\]
Tu \(a_i,b_i\geq0\) to kierunkowe przekroje reakcji pomnożone przez właściwe czynniki jednostkowe; \(d_i+\xi_i X\geq0\) to całkowita strata populacji; \(\xi_i\) może być **ujemne**. \(U,\lambda,a_i,b_i,d_i,\xi_i\) są wspólne między gałęziami wyłącznie dzięki deklarowanemu zamrożonemu tłu.

Zdefiniujmy \(\delta X=X_p-X_u\), \(\delta n_i=n_{i,p}-n_{i,u}\), \(\delta S_i=S_{i,p}-S_{i,u}\), \(c_i(X)=a_i-(a_i+b_i)X\). Odjęcie równań (bez żadnego rozwinięcia perturbacyjnego) daje:
\[
\boxed{\delta\dot X
=-\left[\lambda+\sum_i(a_i+b_i)n_{i,p}\right]\delta X
+\sum_i c_i(X_u)\delta n_i.}\tag{16.1}
\]
\[
\boxed{\delta\dot n_i
=\delta S_i-[d_i+\xi_i X_p]\delta n_i
-\xi_i n_{i,u}\delta X.}\tag{16.2}
\]
W (16.1) wykorzystano dokładnie tożsamość
\(c_i(X_p)n_{i,p}-c_i(X_u)n_{i,u}
=c_i(X_u)\delta n_i-(a_i+b_i)n_{i,p}\delta X\).
W (16.2) wykorzystano
\(D_i(X_p)n_{i,p}-D_i(X_u)n_{i,u}
=D_i(X_p)\delta n_i+\xi_i n_{i,u}\delta X\).

Wektor \(\delta y=(\delta X,\delta n_1,\ldots,\delta n_6)^T\) spełnia **dokładny, nieautonomiczny liniowy układ wymuszony**, którego macierz współczynników jest funkcją faktycznie wyliczonych obu trajektorii:
\[
A_{00}=-\lambda-\sum_i(a_i+b_i)n_{i,p},\quad
A_{0i}=c_i(X_u),\quad
A_{i0}=-\xi_i n_{i,u},\quad
A_{ij}=-\delta_{ij}[d_i+\xi_i X_p].
\]
Przy macierzy fundamentalnej \(\Phi(T,t)\) otrzymujemy:
\[
\boxed{
\delta X(T)=[\Phi(T,t_0)\delta y(t_0)]_0+
\sum_{i=1}^6\int_{t_0}^{T}\Phi_{0i}(T,t)\delta S_i(t)\,dt.
}\tag{16.3}
\]

**Ważne:** dokładność równania (16.3) nie oznacza, że jądro \(\Phi\) jest niezależne od prawa emisji ani że układ jest globalnie liniowy w amplitudzie źródła. Współczynniki \(A(t)\) wykorzystują obie nieliniowe trajektorie.

## 3. Warunkowy certyfikat znaku, a nie deklaracja mechanizmu

Gdy początkowe warunki porównywanych praw emisji są wspólne, pierwszy składnik w (16.3) znika. W badanym subedge modelu, dla \(M<M_0\), publiczne potęgi są około \(-1{,}2\), a papierowa \(-1{,}3\); przy jednakowej dodatniej normalizacji i \(M/M_0<1\) każda różnica \(\delta S_i(t)\) jest nieujemna.

Mimo to \(\Phi_{0i}\) nie musi być nieujemna. Jeżeli z autentycznej trajektorii obliczymy wkłady
\[
J_i(T)=\int_{t_0}^T\Phi_{0i}(T,t)\delta S_i(t)dt,
\]
to znak sumy można poświadczyć przez dominację \(|\sum_{J_i>0}J_i|>|\sum_{J_i<0}J_i|\) (albo odwrotnie), z odpowiednim certyfikatem błędu numerycznego. **Same końcowe wartości \(X(T)\), czy nawet sam znak \(\delta S_i\), nie dostarczają tych sześciu wkładów.**

Dla temperatury \(T=0{,}1447372646\,\mathrm{MeV}\) i źródłowego \(X=0{,}497967914\), sam lokalny współczynnik \(c_i(X)\) w jednostkach podstawowego `mbarn·c` ma orientacyjnie:
- \(\pi^-\): \(+1{,}20505\);
- \(\pi^+\): \(-0{,}846545\);
- \(K^-\): \(+17{,}6981\);
- \(K_L^0\): \(+0{,}0284492\);
- \(\bar p\): \(-13{,}9431\);
- \(\bar n\): \(+14{,}0569\).

Wyniki pokazują silne przeciwnie skierowane wkłady, zwłaszcza antynukleonów, ale **to nie są pełne jądra odpowiedzi \(\Phi_{0i}\)**. Nawet chwilowo dodatni \(c_i\) nie wystarcza do dowodu dodatniego oddziaływania końcowego, ponieważ \(n_i\) jest sprzężone zwrotnie z \(X\).

## 4. Źródłowa próba amplitudy: dokładny status

Mech-S7 ROT006 podaje przy tej samej zastępczej inicjalizacji i tle:
| Mnożnik źródła | \(\delta X_{\rm exec}(T_{\rm nuc})\) | \(\delta X_{\rm sym}(T_{\rm nuc})\) |
|---:|---:|---:|
| 0,5 | \(+1{,}05428492\cdot10^{-6}\) | \(+1{,}54120471\cdot10^{-5}\) |
| 1,0 | \(-6{,}87283267\cdot10^{-6}\) | \(+2{,}24563488\cdot10^{-5}\) |
| 2,0 | \(-3{,}05906073\cdot10^{-5}\) | \(+2{,}09457543\cdot10^{-5}\) |

Przy ciągłej zależności rozwiązań gładkiego modelu ODE od mnożnika źródła, *jeżeli dokładne znaki podanych wartości są utrzymane*, twierdzenie o wartości pośredniej zapewnia **co najmniej jedno zero** kontrastu `B_exec` w \((0{,}5,1)\). **Nie** zapewnia jego jednoznaczności. Mech-S7 podaje numerycznie zero w okolicy \(0{,}5970\); nie jest ono fizycznym progiem \(\beta\).

Secant między punktami \(0{,}5\) i 1 dawałby zero \(0{,}56650\), a nie \(0{,}5970\). Różnica potwierdza znaczenie nieliniowej zależności od amplitudy; secant **nie** jest certyfikowaną lokalizacją korzenia. Nachylenia secant to około \(-1{,}5854\cdot10^{-5}\) i \(-2{,}3718\cdot10^{-5}\) dla przedziałów \([0{,}5,1]\), \([1,2]\). Przekłada się to na niezerową krzywiznę wymuszenia i odpowiedzi. Brak gwarancji dokładnego błędu globalnego Radau jest odrębnym ograniczeniem.

## 5. Niezależny syntetyczny test ścisłej tożsamości

Zbudowano abstrakcyjny 7D układ z sześcioma populacjami, dodatnimi źródłami, dodatnimi stratami zależnymi afinicznie od \(X\) i słabą przemianą \(U-\lambda X\). Rozwiązano *dwa* nieliniowe układy oraz *oddzielnie* dokładny różnicowy układ (16.1)–(16.2) z macierzą utworzoną z obu rzeczywistych rozwiązań.

SciPy DOP853, `rtol=2e-13`, `atol=2e-15`, 151 czasów kontrolnych. Maksimum normy \(\ell_\infty\) błędu rekonstrukcji \(1{,}43081206605\cdot10^{-12}\). Test jest **syntetyczny**: nie odtwarza archiwów Actions, rzeczywistych funkcji hadronizacji ani fizycznego X(T) Wu–Xu. Weryfikuje rachunek matematyczny.

## 6. Granice źródłowe i dyspozycja REC10

**Potwierdzone źródłowo:** struktura słabego źródła neutronów, wszystkie kierunkowe kanały hadronowe w publicznym Wu–Xu i sześć równań populacji; użyte wzory 7D odpowiadają zadeklarowanemu uproszczeniu.

**Niepotwierdzone niezależnie:** pełne dane ZIP Actions, ściśle 7D wyniki liczbowe Mech-S7, numeryczne położenie korzenia w dokładnej trajektorii, rygorystyczne przedziały błędu integratora, pełny 10D Julia.

**Obciążająca granica naukowa:** stany \(X\) i \(n_i\) z archiwalnego ostatniego aktywnego punktu \(M\approx1{,}836\cdot10^9\) g przeniesiono zastępczo na \(M=10^9\) g. To nie jest legalna identyfikacja stanu na zdarzeniu. Równocześnie emisja poniżej \(10^9\) g pozostaje ekstrapolowana bez walidacji hadronizacji E2b. Zatem powrót przeciwnych znaków w tym modelu to **warunkowa zgodność mechanizmu**, a nie odtworzenie fizycznego wyniku ani dowód niezawodności znaku prawdziwego modelu.

**Nauka i prior art:** wrażliwość modeli ODE, równania różnicowe stanów, wariacja stałych, równania fundamentalne, sign/cancellation response analysis — dojrzałe metody; brak roszczenia nowości. REC10 nie nadpisuje raportu Mech-S7 i nie uruchamia nowych zadań.

**Werdykt:** `PASS_WITH_EXACT_STRENGTHENING / CONDITIONAL_7D_SOURCE_MATH / FULL_JULIA_PENDING / BW_PENDING / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE`.