# IW/NASH — DAX-S7 — obrót 46

## Stałość źródłowego współczynnika parowania, analityczna trajektoria masy i górny rząd wielkości końcowego impulsu ogrzewania

**Data:** 2026-10-23  
**Status:** `SOURCE-NATIVE CONSTANT-N VERIFIED / CONTROLLED RADIATION-DOMINATED ENVELOPE / PBH COUPLED SOLVER NOT RUN / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE`

### 1. Źródła, które faktycznie sprawdzono

Publiczny kod Wu–Xu: `Fenyutanchan/Primordial-Black-Hole`, pliki `arXiv-2509.05618/main-scan.jl`, `main-scan-parameters.jl`, `tool_script-parameters.jl`, `tool_script-N_relativistic_species.jl`, tablice `data/ext/N_s_from_PDG2024.csv` i `data/ext/N_rho_OVER_N_s_from_PDG2024.csv`. Źródłowe zakresy: masa początkowa `6e8–1e10 g` (100 węzłów logarytmicznych), beta `1e-20–1e-17` (100 węzłów). Źródłowe prawo: `dM/dt=−N_BH(T_BH) m_Pl^4/M^2`, `N_BH=(27/4)*N_rho(T_BH)/(30720*pi)`, `T_BH=M_Pl^2/M`.

### 2. Nowy wynik źródłowy: N_BH jest stałe w całym skanie

Najwyższe węzły danych: `N_s(279783.067 MeV)=104.896439` i `N_rho/N_s(275903.656 MeV)=0.999701056`. Oba źródłowe interpolatory mają `ExtrapolationType.Constant`. Zatem dla T_BH przekraczającej około 280 GeV źródłowy `N_rho=104.86508083894`, `N_BH=0.00733438299605644`.

Stosując zwykłą konwersję Hawkinga `T_H[GeV]≈1.0579e13/(M[g])`, już największy M_f=1e10 g ma T_H≈1057.9 GeV, a najmniejszy ≈17631.7 GeV. Ponieważ M maleje, T_H tylko rośnie. Tak więc w implementacji dla tego skanu N_BH pozostaje stałe, a równanie masy można scałkować analitycznie:

`M(t)^3=M_f^3−3*N_BH*m_Pl^4*(t−t_f)`, aż do źródłowego progu wyłączenia. Używając `m_Pl≈2.176434e−5 g` i `t_Pl≈5.391247e−44 s`, charakterystyczny czas do M=0 wynosi `tau=(M_f/m_Pl)^3*t_Pl/(3*N_BH)`. Jest to skala z modelu, nie symulowany czas dokładnego wyłączenia solvera.

| M_f | T_H,f | tau | t_f (źródłowe gamma=1/(3sqrt3)) |
|---:|---:|---:|---:|
| 6e8 g | 17.63 TeV | 0.051336 s | 7.72e−30 s |
| 1e9 g | 10.58 TeV | 0.237666 s | 1.287e−29 s |
| 1e10 g | 1.058 TeV | 237.666 s | 1.287e−28 s |

**Istotny detal:** w `main-scan.jl` `log_m_PBH_evaporated_ratio=20` i próg jest `max(log(M_f)−20,log(m_Pl))`. Przy wskazanych masach dominuje pierwszy składnik; kod przestaje zasilać promieniowanie przy `M/M_f≈exp(−20)=2.061e−9`, czyli przy około 1.24–20.61 g, a nie dopiero przy masie Plancka. Dla ocenianego tu impulsu to próg bardzo późny.

### 3. Jawnie przybliżony model kontrolny

Przyjęto dominację promieniowania, w przybliżeniu stałe efektywne stopnie swobody, `a/a_f≈sqrt(t/t_f)`, `H≈1/(2t)` oraz termalizację całej energii parowania w promieniowaniu. Nie jest to dokładna ewolucja kosmologiczna Wu–Xu: pomija zmienność g*, feedback energii PBH na H, hadrony i sektor neutrin. Maksymalny stosunek rho_PBH/rho_SM poniżej 1% wspiera przybliżenie dominacji promieniowania, lecz nie usuwa tych ograniczeń.

Definicje: `y=M/M_f`, `gamma=1/(3sqrt3)`, `A=sqrt(tau/t_f)=sqrt(gamma/(3*N_BH))*(M_f/m_Pl)`, `epsilon=beta*A`. W granicy `tau/t_f >> 1`, `t≈tau(1−y^3)` oraz `a/a_f≈A sqrt(1−y^3)`.

Współporuszająca energia promieniowania rośnie względem wartości początkowej zgodnie z

`E_R(y)/E_R,f≈1+epsilon*F(y)`, gdzie `F(y)=integral_y^1 sqrt(1−u^3)du`, `F(0)=0.841309263195272`.

W konsekwencji

`R(y)=rho_PBH/rho_R≈epsilon*y*sqrt(1−y^3)/(1+epsilon*F(y))`,

`I(y)=−dot(M)*n_PBH/(H*rho_R)≈(2*epsilon/3)*(1−y^3)^(3/2)/(y^2*(1+epsilon*F(y)))`.

W kontrolnym wariancie o stałym g próg zmiany znaku `dT/dt` to `I=4`. Dokładny próg z kodu przy `T_nuc`, wykorzystujący źródłowe pochodne tabeli, wynosi około 3.869 (obrót 45). Te progi nie zostały utożsamione.

### 4. Wyniki liczbowe modelu kontrolnego

| M_f, beta | epsilon | y przy I=4 | R przy progu | czas do końca od progu | wzrost T od minimum do końca |
|---|---:|---:|---:|---:|---:|
| 6e8 g, 1e−20 | 8.153e−7 | 0.0003686 | 3.005e−10 | 2.57e−12 s | 5.01e−11 |
| 6e8 g, 1e−17 | 8.153e−4 | 0.011653 | 9.494e−6 | 8.12e−8 s | 1.582e−6 |
| 1e9 g, 1e−17 | 1.359e−3 | 0.015041 | 2.041e−5 | 8.09e−7 s | 3.402e−6 |
| 1e10 g, 1e−17 | 1.359e−2 | 0.047331 | 6.363e−4 | 0.02520 s | 1.060e−4 |

Końcowy wzrost T obliczono z `T(0)/T(y_crit)≈sqrt(1−y_crit^3)*[(1+epsilon F(0))/(1+epsilon F(y_crit))]^(1/4)`. Maksymalny testowany impuls to **0.0106%**, nie 0.0106 w wartościach bezwzględnych.

Dla `M_f=1e10 g`, `beta=1e−17`: maksimum R≈0.007740 (0.774%), przy `y≈0.738`; cały wzrost współporuszającej energii promieniowania to `epsilon F(0)≈0.011432` (1.143%), co odpowiada wzrostowi T o około **0.285%** przy tym samym a względem braku zasilania. Ten skumulowany wpływ jest znacznie większy niż późny impuls temperatury po przekroczeniu I=4. Nie należy ich mylić.

### 5. Warunek wielokrotnego przejścia przez T_nuc

Przekroczenie progu I>4 oznacza lokalny wzrost T, ale **nie dowodzi drugiego przecięcia poziomu T_nuc**. Konieczna jest zgodność temperatury lokalnego minimum i późniejszego maksimum z T_nuc. W modelu kontrolnym dla skrajnego przypadku lokalna amplituda impulsu to około 1.06e−4 względnie, więc takie przejście wymaga szczególnego zestrojenia epoki parowania z osiągnięciem T_nuc. Dla rzeczywistej tablicy g*(T) i dokładnego H amplituda oraz próg mogą się zmienić.

Masy źródłowe są rozmieszczone logarytmicznie: stosunek sąsiednich mas ≈1.028826, charakterystycznych czasów parowania ≈1.088995. Najwyższe trzy masy to około 9.4475e9, 9.7198e9 i 1.0000e10 g, a ich charakterystyczne czasy ~200.41, 218.24 i 237.67 s. Rozdzielczość skanu może więc być niewystarczająca, aby *automatycznie* trafić w bardzo wąski warunek ponownego przecięcia, ale nie dowodzi to jego nieobecności.

### 6. Falsyfikator w oryginalnym Julia — READY TO EXECUTE

Dla wszystkich 100×100 przypadków i osobno gęstszego wycinka mas w pobliżu chwili T_nuc: zapisywać `M/M_f`, `I`, `4−r/(3+s)`, `T(t)`, `X_n(t)`; liczyć przedziały I>I_crit i liczbę przecięć T=T_nuc; dla każdego przecięcia zapisać czas i X_n; porównać źródłowy sortowany interpolator z regułą ostatniego przecięcia, oraz z odczytem po pełnym zaniku PBH; kontrolować tolerancje solvera i flagę zakończenia. Jeśli brak drugiego przecięcia, zamknąć hipotezę branch-ambiguity dla skanu. Jeśli istnieje, ocenić różnicę X_n przed jakąkolwiek interpretacją Y_p i PBH.

**Granice roszczeń:** źródłowo wykazano stałość N_BH i dokładne prawo M³. Wszystkie oszacowania R, amplitud oraz warunku wielokrotnego przecięcia są modelem kontrolnym; nie uruchomiono pełnego Julia ani nie uzyskano nowych ograniczeń PBH. Host-theory subtraction: równanie Hawkinga, FLRW i budżet energii nie są nowym wkładem IW/NASH.