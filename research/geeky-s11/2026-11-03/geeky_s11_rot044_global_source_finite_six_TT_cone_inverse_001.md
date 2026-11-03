---
artifact_id: GEEKY-S11-ROT044-GLOBAL-SOURCE-FINITE-SIX-TT-CONE-INVERSE-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-11-03
exposure: PUBLIC
provenance_class: RETAINED_AUXILIARY_SOURCE_PLUS_EXACT_RATIONAL_AND_INTERVAL_CERTIFICATE
science_status: ANALYTIC_GLOBAL_BILIPSCHITZ_IN_RESTRICTED_MODEL / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT044 — Globalne odwracanie sześciu pasm TT w źródłowo dyskretnym modelu sześciopoziomowym

## 0. Pierwszeństwo wyników, korpus i nowość tego obrotu

Geeky ROT015–017: wadliwy realcast surowego projektera TT na parzystych siatkach i poprawny ortogonalny rzeczywisty projektor `B=GA`. ROT027 i ROT029: dokładny operator transportu Liego wstawiany po wszystkich pozycjach w ciągu filtrów i jego symbol Fouriera. ROT033: zmienne filtry. ROT034: ścisła nieidentyfikowalność **dowolnych** harmonogramów na podstawie dwóch całych pól TT oraz jawna kolizja momentów w granicy ciągłej. ROT035–036: warunkowe odwracanie sześciopoziomowego modelu ciągłego, bramka nieznanego gain i błąd modelu dyskretnego. ROT037: lokalne źródłowo dyskretne odwracanie. ROT038: nominalny dobór sześciu sond. ROT039 i ROT040: rzeczywista porażka tego zestawu w innym dopuszczalnym harmonogramie N64, certyfikowana przedziałowo w otoczeniu. ROT041: dokładna algebraicznie kompresja po stałych blokach. ROT042: jednolity błąd Jacobianu względem granicy ciągłej O(N^-2), dla stałego zestawu modów i wszystkich legalnych profili; certyfikat dużego N dla konkretnego trudnego profilu. ROT043: lokalna dwupunktowa odwracalność w kuli oraz rzeczywisty skok Jacobianu rangi 1.

**Nowy wkład ROT044** to globalne w całej określonej rodzinie sześciopoziomowej, ale NIE wśród dowolnych filtracji, twierdzenie o dwustronnej stabilności mapy odczytów: zmiana na zmienne iloczynowe `z=(t,t d0,...,t d4)` pozwala ograniczyć cały dyskretny Jacobian względem **stałej** odwracalnej macierzy granicznej. Wykorzystuje matematycznie klasyczne oszacowania iloczynów Eulera, wariacji całkowitej, nierówności Weyla i odwracalność funkcji bliskiej liniowej. Bez roszczeń do nowego twierdzenia ogólnomatematycznego.

Host źródłowy: **niezmieniony plik pomocniczy** `deepseek_python_20260627_a87249.py`, bajtowy SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`. Historyczny produkcyjny `dtc0a_runtime_v0_3_1.py` jest niedostępny. Geometria: pełna niemaskowana okresowa siatka N³, N parzyste, rzeczywiste symetryczne tensory, ścisły rzeczywisty B=GA, źródłowy pełny trzyczłonowy Lie dla `C=(0,cos x,0)` i stabilny `E_alpha=I+alpha h² Delta_2`. **Nie** orzekamy o historycznym maskowanym `h=fI`, `K_A`, NCDG J3/K ani fizyce GR/GW/PBH.

## 1. Dokładna rodzina i mapa odczytów

Ustalone: łączna dawka `A=9/1000`, nachylenie pięciu znanych ramp `v=3/250`, poziomy skumulowanej dawki `x_j=jA/5` dla j=0,...,5, długość ramp łącznie `A/v=3/4`, suma dodatnich czasów plateau `D=1/4`. Wszystkie `d_j>0`, j=0,...,5, i `sum_j d_j=D`; wzmocnienie `t>0` jest **nieznane bez żadnego odgórnego ograniczenia**.

Każdy profil odpowiada jednoznacznie niemalejącej, odcinkowo liniowej funkcji dawki `a_d(u)` na u∈[0,1]: na plateau stała, na rampach nachylenie v. Dla dowolnego parzystego N niech `m=round((3/25)N²)` i

```
alpha_j = N² [a_d(j/m)-a_d((j-1)/m)],  j=1,...,m.
```

Dla N≥200000, `m≥.119N²`, stąd `0≤alpha_j≤v/.119<1/6` i `sum alpha_j=N² A`. Żaden parametr nie przekracza stabilnego przedziału oryginalnego źródłowego E. Dla dwóch modów input/output (`p,1,0` i `p+s,1,0`) definiujemy

```
S_in = sin²(pi p/N)+sin²(pi/N),  S_out=sin²(pi (p+s)/N)+sin²(pi/N),
Omega_N(p,s;d) = [sum_{ell=0}^m prod_{j≤ell}(1−4 alpha_j S_in) prod_{j>ell}(1−4 alpha_j S_out)]/(m+1).
```

Sześć sond ROT038: `[(0,+1),(1,−1),(1,+1),(2,−1),(3,+1),(4,−1)]`. Są to skalarne, znormalizowane względem znanej polaryzacji TT odczyty bocznych pasm z pełnych pól tensorowych (nie surowe 6 niezależnych pikseli).

Wprost `F_N(t,d)=t*(Omega_N(p,s;d))_{6 sond}`. Nie wolno zamieniać jej na model cieplny przy skończonym N.

## 2. Współrzędne wypukłego stożka i stała macierz graniczna

Zdefiniuj

```
z=(z0,z1,...,z5)=(t,t d0,...,t d4)
C={z∈R^6: z0>0, z1..z5>0, sum_{i=1}^5 z_i < D z0}.
```

Jest to **otwarty wypukły stożek**. Odwrotnie `t=z0`, `d_i=z_(i+1)/z0`, `d5=D−sum_i d_i`. Nie ma już osobnej nieliniowej dziedziny dla `z` poza tymi nierównościami.

Granica ciągła ROT034–036 jest **liniowa** w z:

```
F_infty(z)=M z,     M=[b | W] ∈R^(6x6),
lambda_ps=4pi²((p+s)²−p²),  kout=(p+s)²+1,
scale_ps=exp(−4pi² kout A),
b_ps=scale_ps [(exp(lambda_ps A)−1)/(lambda_ps v) + D exp(lambda_ps x5)],
W_(ps,i)=scale_ps [exp(lambda_ps x_i)−exp(lambda_ps x5)], i=0,...,4.
```

Wszystkie lambda są niezerowe. Niezależna 120-cyfrowa arytmetyka skierowanych przedziałów (`mpmath.iv`) tworzy M bez czytania Jacobianu źródła i dowodzi, sześcioma ściśle dodatnimi pivotami rozkładu LDLᵀ macierzy `MᵀM−(1.50e−5)²I`, że

**(A) `sigma_min(M)>1.50·10^-5`.**

W osobnym sprawdzeniu przedziałowym wyznacznik M z 720 permutacji jest ściśle dodatni, około `5.34105382238e−13`. Oba te certyfikaty są wspomagane przez eksperymentalną implementację `mpmath.iv`, **nie** stanowią dowodu w Lean/Coq.

## 3. Nowy jednolity błąd całego Jacobianu w współrzędnych z

Na każdym obszarze gładkim zmiennych plateau źródłowa mapa ma pochodne

```
∂F_N/∂z_i = ∂Omega_N/∂d_(i−1),                 i=1,...,5;
∂F_N/∂z0  = Omega_N − sum_(j=0)^4 d_j ∂Omega_N/∂d_j.
```

Zależność od wzmocnienia t **znika** z tych wzorów. Równości identyczne dla modelu granicznego dają `DF_infty(z)=M`.

Przeniesione i ponownie rozliczone z ROT042 **jednolite** dla wszystkich dodatnich plateau, N≥64 i wszystkich sześciu modów źródłowych nierówności skalarne:

```
|Omega_N−Omega_infty| < 1415/N²,
|∂_(d_j)Omega_N−∂_(d_j)Omega_infty| < 52326/N², j=0,...,4.
```

**Dlaczego stałe nie zależą od d?** Niezależnie od położenia załamań skumulowana dawka ma całkowitą dawkę A, Lipschitz≤v; jej pochodne `g_j(u)=∂a_d(u)/∂d_j` są na rampach 0 lub −v i na plateau 0, więc `||g_j||∞≤v` i `TV(g_j)≤10v`. Na każdej siatce `m≥.119N²`; dla niskich modów `lambda_N<1027`, `|lambda_N−4pi²K|<82000/N²`, `lambda_N Δa<1/20`. Nierówność log Eulera `−log(1−x)−x≤x²/[2(1−x)]`, kontrola pochodnych i kwadratura funkcji o skończonej wariacji daje wyżej podane oszacowania. Rozwinięcie i sprawdzenie ściśle wymiernych stałych zawiera `rot044_global_rational_bound.py`; pełne szczegóły lematów w raportach ROT042/043. Przy próbkowanych załamaniach są to granice pochodnych z komór parametrów, a następnie ich wypukłe kombinacje w sensie Clarke’a.

Ponieważ `sum_(j=0)^4 d_j<D=1/4`, pierwsza kolumna błędu `DF_N−M` ma każdą współrzędną mniejszą niż

`(1415+(1/4)*52326)/N² = (28993/2)/N²`.

Pozostałych pięć kolumn ma elementy mniejsze niż `52326/N²`. Zatem z normy Frobeniusa:

```
||DF_N(z)−M||2 ≤ ||DF_N(z)−M||F
 < sqrt( (28993/2)² + 5*(52326)² )/N²
 < 120000/N².                                   (B)
```

To obowiązuje na **całym stożku C dla dowolnego t>0** i wszystkich N≥64, także dla wszystkich jednostronnych i uogólnionych Jacobianów. Nie jest potrzebna osobna lokalna kontrola `||W||F` z ROT043.

## 4. Główne twierdzenie R44.1 — globalna bi-Lipschitzowość w stożku

Dla każdego parzystego `N≥200000`:

`120000/N²≤3.0·10^-6 < sigma_min(M)−1.20·10^-5`.

Niech `z,z'∈C`. Stożek jest wypukły, więc odcinek między z i z' pozostaje w C. Źródłowa mapą `F_N` jest lokalnie Lipschitzowska i odcinkami gładka; całkując pochodną wzdłuż odcinka dostajemy

```
F_N(z)−F_N(z') = M(z−z') + R,
||R||2 ≤ (120000/N²) ||z−z'||2.
```

Stąd przez (A) i (B):

**`||F_N(z)−F_N(z')||2 > 1.20·10^-5 ||z−z'||2` dla wszystkich z≠z' w C.**

Konsekwencje: (i) `F_N` jest **globalnie różnowartościowa** w tej sześciopoziomowej rodzinie, przy nieznanym i nieograniczonym dodatnim wzmocnieniu; (ii) odwrotność z obrazu `F_N(C)` do C jest Lipschitzowska z czynnikiem mniejszym niż `1/(1.20e−5)=83 333.333...`; (iii) jeśli rzeczywisty odczyt jest zaszumiony nie więcej niż η, a kandydat w C ma residual nie większy niż η, to oba dopuszczalne parametry z różnicy odczytów różnią się w normie z co najwyżej `2η/(1.20e−5)`; (iv) węzły załamań ramp nie tworzą wyjątków od dwupunktowej nierówności.

Wynik **nie** mówi, że metoda Newtona z każdego startu znajduje rozwiązanie, że minimum błędów na **otwartym** C jest zawsze osiągane ani że każda zaszumiona obserwacja należy do obrazu F_N. Nie jest wynikiem o wszystkich możliwych harmonogramach lub o wszystkich sondach.

## 5. Bramki falsyfikacyjne i ograniczenia wzmocnienia

Brak górnego ograniczenia t jest poprawny **tylko dla zmiennych z** i skalarnych odczytów linearnych w t. Odtworzenie czasów `d_j=z_(j+1)/z0` przy `t→0` ma niejednostajną wrażliwość; by kontrolować bezwzględny błąd d, potrzebna jest dolna granica `t≥t_min>0`. W przybliżeniu `||d−d'||2 ≤ sqrt(1+D²)/t_min ||z−z'||2` dla dwóch dodatnich wzmocnień ≥t_min. Nie występuje jednostajna fizyczna odporność przy zaniku amplitudy.

Stary negatywny wynik ROT034 dla **dowolnych m-wymiarowych** harmonogramów pozostaje w mocy — tam dziedzina ma wymiar większy niż liczba niezależnych danych. Globalna odwracalność tutaj jest możliwa wyłącznie dzięki silnemu sześciopoziomowemu ograniczeniu modelu i sześciu właściwym odczytom.

Próg `N≥200000` jest bardzo zachowawczy; **nie** dowiedziono najmniejszego progu. Nie wolno uznawać obliczeń Fouriera przy N200000 lub N1000000 za pełne obliczenia źródłowej siatki N³.

## 6. Niezależne wykonanie i wyniki

Pięć ścieżek, niezależne audyty różnych części rozumowania:

1. `rot044_global_rational_bound.py`: dokładne ułamki stałych z ROT042, nowa zmiana na z, nowa norma Frobeniusa i próg N0=200000 — **10 asercji PASS**.
2. `rot044_interval_global_matrix.py`: **niezależna** stała M z sześciu wykładniczych momentów; mpmath.iv 120 cyfr, sześć dodatnich pivotów LDLᵀ, pełny 720-składnikowy certyfikat det>0; porównanie pomocniczego SVD — **15 PASS**.
3. `rot044_finite_cone_stress.py`: 84 prawdziwe dodatnie rozkłady plateau, wzmocnienia od .002 do 4000; model źródłowo dyskretny obliczony blokowo przy N=32/64/128/200000/300000/1000000; niezależne Jacobiany w z i 1414 typowane kontrole, w tym wszystkie pary w tym samym N. Jest to **stres numeryczny**, nie dowód wszystkich parametrów.
4. `rot044_adversarial_singular_direction.py` z osobnym `rot044_fraction_source_core.py`: **dokładna arytmetyka wymierna** czasowych przekrojów plateau/ramp i niezależne sumy geometryczne, 25 PASS, test kierunku najmniejszej wartości singularnej M na N24/64/200000/300000/1000000; przy dużym N iloraz bliski 1.536466e−5. Nie jest to dokładny rachunek wymierny funkcji trygonometrycznych.
5. `rot044_literal_aux_source_gain.py`: dosłownie niezmienione pomocnicze `apply_E`, `apply_P_TT`, `lie_derivative_tensor` na rzeczywistych pełnych siatkach N12/16, jawne wszystkie m+1 pozycje Lie, cztery różne amplitudy t=.003/1.07/11/100 i niezależna implementacja Fraction okresów; **29 PASS**, największa względna rozbieżność Fourierowa `2.69644e−16`.

**SUMA 1493/1493 wykonanych typowanych asercji PASS** (=10+15+1414+25+29). Nie oznacza 1493 niezależnych eksperymentów naukowych. W rozwoju niezależnej implementacji Fraction wykryto błąd obsługi komórki zero przecinającej koniec pierwszego plateau; został usunięty przed wynikiem PASS. Odrębne dwa nieudane testy wstępne nie są liczone.

Jeden pakiet lokalny dla Moderatora: pełny raport, 5 wykonywalnych programów, niezależny helper wymierny, zachowane pomocnicze moduły, oryginalny bajtowo niezmieniony source helper, pięć rzeczywistych JSON i stdout, README, manifest SHA256. Niezależna recenzja matematyczna nie została wykonana. Odtwarzalność i SHA ZIP opisane w końcowym README/komunikacie.

**FIREWALL:** `NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / REFEREE_PENDING / BW_PENDING / NO_NEW_TASK`. Żadnych historycznych maskowanych wyników `K_A`, danych fizycznych NCDG ani empirycznej kalibracji szumu.