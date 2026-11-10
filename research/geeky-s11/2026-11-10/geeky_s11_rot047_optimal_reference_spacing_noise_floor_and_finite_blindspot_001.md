---
artifact_id: GEEKY-S11-ROT047-MULTIREFERENCE-DESIGN-DRIFT-NOISE-FLOOR-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-11-10
exposure: PUBLIC
provenance_class: RETAINED_AUXILIARY_FOURIER_SOURCE_PLUS_CLASSICAL_INTERPOLATION_AND_EXACT_RATIONAL_CERTIFICATES
science_status: ANALYTIC_INTERPOLATION_GUARANTEE_AND_FINITE_REFERENCE_BLINDSPOT / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT047 — Ile referencji potrzebujemy? Projektowanie kalibracji w czasie, dolna granica nieidentyfikowalności i szum wspólny

## 0. Pochodzenie i pierwszeństwo

ROT015–017: problem rzeczywistego projektera TT surowego k na parzystej siatce i prawidłowy rzeczywisty ortoprojektor `B=GA`. ROT027 i ROT029: wstawienie pojedynczego pełnego trójczłonowego transportu Liego równomiernie po pozycjach filtrów i dokładne symbole Fouriera. ROT033: sekwencje filtrów o zmiennym `alpha_j`. ROT034: nieidentyfikowalność dowolnych harmonogramów z dwóch pełnych pól TT. ROT035–036: ograniczona sześciopoziomowa rodzina, pięć/sześć kanałów, wzmocnienie. ROT037–044: dokładna dyskretna mapa, projekt sond, lokalna i globalna w ograniczonej rodzinie odwracalność; w ROT044 dla znanych względnych kalibracji sześciu kanałów, dla każdej parzystej `N>=200000`, `||F_N(z)-F_N(z')||>c||z-z'||` na otwartym wypukłym stożku `C`, z `c=1.2e-5`, `z=(t,td0,...,td4)`. ROT045: **PIERWSZY** nieznany gain per kanał prowadzi do ślepej symetrii, a jedna znana referencja usuwa ją wyłącznie dla kalibracji stacjonarnej. ROT046: **PIERWSZY** dwie referencje na końcach nie dają dokładnej identyfikacji przy nieznanym dryfie; założenie `|ell_i''|<=H` daje ostrą lokalną interpolacyjną granicę `H*Delta²/8` i warunkowy błąd rekonstrukcji; w pełni wyjaśniono niebezpieczny float-knot Jacobian. ROT047 nie przypisuje sobie tych wyników. **Nowe**: jednolity projekt `K` referencji dla całego przedziału, konstrukcja gładkiego (`C²`) ukrytego dryfu o dolnej granicy skali `1/(K-1)²`, ostry współczynnik centrowania szumu względnego dla sześciu kanałów, jawna minimalna liczba referencji dla konkretnego konserwatywnego certyfikatu oraz źródłowo dyskretne porównanie 2/3/5/9 referencji.

Przywoływane twierdzenia i rachunki są klasycznymi nierównościami interpolacji (`Peano kernel`), funkcją wypukłą maksymalnej przerwy, prostą arytmetyką log-gain oraz standardową stabilnością odwrotności. **NO MATHEMATICAL NOVELTY / NO PRIORITY CLAIM.**

Źródło: **niezmieniony pomocniczy** `deepseek_python_20260627_a87249.py` z rzeczywistym bajtowym SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`, nieosiągalny historyczny właściwy `dtc0a_runtime_v0_3_1.py`. Model: płaska pełna niezamaskowana parzysta siatka `N³`, rzeczywiste symetryczne tensory TT z `B=GA`, źródłowy pełny trójczłonowy centered Lie z `C=(0,cos x,0)`, legalne `E_alpha=I+alpha h² Delta2`, `0<=alpha<=1/6`. Model identyfikacji, nie wyniki fizyki J3/K, GR/GW/PBH ani historycznego maskowanego `h=fI/K_A`.

## 1. Klasa danych i odniesienie do ROT044/046

Sześć kanałów: `H0+`, `H1-`, `H1+`, `H2-`, `H3+`, `H4-`. Znanych jest sześć poziomów skumulowanej dawki `x_j=j*.009/5`, pięć ramp o prędkości `.012`, dodatnie czasy sześciu plateau o sumie `.25` i nieznany wspólny gain `t>0`, który wchodzi do `z=(t,t*d0,...,t*d4)`. Dla każdej skończonej siatki dokładne uśrednienie wstawienia Liego po wszystkich filtrach daje mapę `F_N:C->R^6` (poprzednia semantyka). Matematyczny certyfikat ROT044 przyjmujemy jako ustalone, nadal podlegające niezależnemu audytowi założenie dla warunkowych zastosowań odwrotności.

Nieznane dodatnie **względne** wzmocnienia kanałów to `g_i(tau)=exp(ell_i(tau))`, `sum_i ell_i(tau)=0`. Bezwzględna skala każdego pomiaru referencyjnego może być inna i nieznana. `K>=2` znanych referencji wykonujemy w czasach `0=tau0<tau1<...<tau_(K-1)=T`. Każda ma **znany profil sześciu plateau** i obliczalny niezerowy wzorzec `Omega_N(d_ref)`; nieznany jest jej bezwzględny `t_ref,j`. Referencje i pomiar docelowy korzystają z tych samych kanałów, których znormalizowane gainy mogą dryfować. Dla gwarancji całoprzestrzennej przyjmujemy `ell_i in C²([0,T])`, `|ell_i''|<=H`; **H jest znanym zewnętrznym ograniczeniem, nie estymatą odtworzoną z referencji**. Interpolujemy logarytm gain kanału liniowo między kolejnymi referencjami.

## 2. R47.1 — górna granica i optymalne rozmieszczenie dla tego certyfikatu

Dla jednej przerwy `[a,b]`, `h=b-a`, standardowy wzór na resztę interpolacji daje:

`|ell_i(tau)-ellhat_i(tau)| <= H*(tau-a)*(b-tau)/2 <= H*h²/8`.

Stała `1/8` jest ostra dla **odcinkowo liniowego interpolatora na danej przerwie**: globalna parabola `ell_1(t)=H*t*(T-t)/2`, `ell_2=-ell_1`, inne 0, spełnia całe ograniczenie i daje dokładnie `Hh²/8` w środku każdej przerwy. Większa liczba innych znanych referencji mogłaby umożliwiać inny (np. wyższego rzędu) interpolator, dlatego NIE twierdzimy, że jest to nieusuwalna minimaksowa stała dla dowolnych algorytmów i dowolnych referencji.

Jednolita granica to `eta_curv <= H*hmax²/8`, gdzie `hmax=max_j(tau_(j+1)-tau_j)`. Ponieważ suma `K-1` przerw to `T`, zawsze `hmax>=T/(K-1)`, z równością tylko przy równomiernej siatce. **Równomierne rozmieszczenie minimalizuje tę certyfikowaną najgorszą górną granicę**: `eta_curv=HT²/[8(K-1)²]`. Nie jest to twierdzenie o kosztach pomiaru, praktycznym szumie heteroskedastycznym, przydziale adaptacyjnym ani znanym z góry pojedynczym czasie celu; zakłada pomiary referencyjne na obu końcach, a cel może wystąpić w dowolnym miejscu.

## 3. R47.2 — nieusuwalna ślepota DLA KAŻDEJ skończonej liczby referencji

Weźmy dowolną największą przerwę `[a,b]` o `h>0`. Zdefiniujmy `phi(s)=s³(1-s)³` dla `0<=s<=1`, a `0` poza tym przedziałem. Funkcja, jej pierwsza i druga pochodna znikają na brzegach, więc po sklejeniu jest `C²`. Dla `u=s(1-s)` dokładnie `phi''=6u-30u²`, `0<=u<=1/4`, stąd `sup|phi''|=3/8`; `phi(1/2)=1/64`. Wybierzmy:

`b(tau)=(8Hh²/3)*phi((tau-a)/h)`, `ell=(b,-b,0,0,0,0)`.

Wtedy `sum ell_i=0`, `max |ell_i''|<=H`, `ell_i(tau_j)=0` **we wszystkich chwilach referencyjnych**, ale w środku tej przerwy `b=Hh²/24>0`. Znak można odwrócić. Daje to **referencyjną nieoznaczoność log-gainu o co najmniej tej skali** w klasie `C²`; dolna granica ma rząd `Theta(Hh²)`. Nie oznacza, że na każdej pozycji docelowego parametru `z` istnieje alternatywne `z'` o zadanej z góry odległości proporcjonalnej do `Hh²` — zależy to od odległości `F_N(z)` od brzegu obrazu. Wystarcza jednak niezerowa, odpowiednio mała amplituda bump, by dzięki **otwartości `F_N(C)`** (ROT044 + invariance of domain) otrzymać drugie dopuszczalne `z'` z **dokładnie** tymi samymi wszystkimi danymi referencji i docelowymi po kompensacji gainu. Niejednoznaczność jest twierdzeniem algebraiczno-topologicznym, a residua numeryczne jedynie odtwarzają przykład.

Po równomiernym rozłożeniu `K` referencji dolna skala niewidocznego bump to `HT²/[24(K-1)²]`, podczas gdy górna granica interpolacji wynosi `HT²/[8(K-1)²]`. W tej klasie optymalna gwarantowana skala niepewności nie może maleć szybciej niż `1/(K-1)²` bez dodatkowej struktury. Nie utożsamiamy referencyjnej dolnej granicy z uniwersalnym dolnym błędem konkretnego fizycznego estymatora `z`.

## 4. R47.3 — ostry sześcio-kanałowy współczynnik szumu referencji

Niech jeden znany pomiar referencyjny ma per-channel mnożnik `1+e_i`, `|e_i|<=eps_ref<1`. Dzielimy odczyty przez znany niezerowy kształt źródłowy `Omega_ref_i`, logarytmujemy, a następnie **odejmujemy średnią z sześciu logarytmów**, usuwając nieznane `log t_ref` i zachowując normalizację `sum ell_i=0`.

Błąd każdego logarytmu przed centrowaniem to `delta_i=log(1+e_i)` w przedziale `[L,U]=[log(1-eps_ref),log(1+eps_ref)]`. Dla sześciu kanałów dokładnie:

`|delta_i-(sum delta)/6| <= (5/6)*(U-L) = (5/6)*log[(1+eps_ref)/(1-eps_ref)]`.

Stała `5/6` **jest ostra**: jeden kanał ma `e=+eps_ref`, pięć kanałów `e=-eps_ref`. Dla dowolnej interpolacji będącej wypukłą kombinacją dwóch sąsiadujących referencji ten sam bound pozostaje poprawny. Powtórzenie skorelowanego skrajnego błędu na KAŻDEJ referencji sprawia, że nie maleje on przy wzroście `K`. Żadne probabilistyczne uśrednianie nie jest tu założone. Jest to ostrzejszy o `1/6` deterministyczny współczynnik niż konserwatywny `log[(1+eps_ref)/(1-eps_ref)]` z ROT046; nie unieważnia dawnej granicy.

Ostateczny logarytmiczny błąd kalibracji:

`eta_K = H*T²/(8*(K-1)²) + (5/6)*log[(1+eps_ref)/(1-eps_ref)]`.

Dla niezależnie ograniczonego (niekoniecznie statystycznie niezależnego) błędu względnego pomiaru celu `|e_target_i|<=eps_target`, skorygowany odczyt ma deterministyczny błąd względny najwyżej

`q_K=(1+eps_target)*exp(eta_K)-1`.

## 5. R47.4 — liczba referencji potrzebna do ŚCIŚLE WARUNKOWEJ tolerancji odwrotnej

Dla N parzystego `>=200000` bierzemy stałą `c=1.20e-5` z ROT044 na stożku `C`, dowolne dopuszczalne prawdziwe `z` i dopuszczalną kandydaturę `z_hat`, resztę dopasowania `r` do skorygowanych danych oraz **niezależną** granicę normy sygnału `||F_N(z)||<=B`. Wówczas:

`||z_hat-z||₂ <= [r+q_K*B]/c`.

Jeżeli użytkownik chce `||z_hat-z||<=delta_z` i ma pewne `r<=r0`, to **wystarczająca certyfikowana** liczba K jest minimalną liczbą całkowitą spełniającą

`r0 + B*((1+eps_target)*exp[HT²/(8(K-1)²)+eta_ref]-1) <= c*delta_z`, 

z `eta_ref=(5/6)log((1+eps_ref)/(1-eps_ref))`.

Można ją obliczyć wprost. Jeśli

`D=log[(1+(c*delta_z-r0)/B)/(1+eps_target)]-eta_ref <=0`,

**żadna skończona liczba K nie spełni tej deterministycznej gwarancji**: występuje sufit narzucony przez dopuszczony szum. Jeśli `D>0`, wystarcza

`K >= 1 + ceil[T sqrt(H/(8D))]`, z dodatkowym wymogiem `K>=2`.

Podkreślamy: to najmniejsze K **w tej regule certyfikacyjnej**, a nie dowód optymalnej liczby fizycznych pomiarów. Przy `T=1,H=4e-8,eps_ref=1e-10,eps_target=5e-11,B=1.01,r0=0,c=1.2e-5,delta_z=3e-5`: `K=7`. Dla `K=6` konserwatywna granica błędu wynosi `3.5069447346e-5`, dla `K=7` `2.9925928402e-5`. Dla `delta_z=1e-5` przy tym samym szumie żadna liczba K nie wystarcza; dla obu szumów równych zeru wystarcza K=5. `B=1.01` rzeczywiście przewyższa obliczoną normę odczytów kontrolnego `N=300000` (~1.00449), ale nie jest uniwersalną granicą dla dowolnego `t` (z może mieć dowolne wzmocnienie). Tolerancja dotyczy `z`, nie jednostajnie `d=z_i/t` przy `t->0`.

## 6. Wyniki wykonane i negative knowledge

**Źródłowo-dyskretny przykład:** te same sześć kanałów ROT038, ten sam docelowy `z=(1.07,1.07*d0,...,1.07*d4)`, znana referencja o innym profilu i zmienne nieznane absolutne wzmocnienia każdej referencji, log-gain z częścią liniową i jedną parą kwadratowej krzywizny `H=4e-8`. Dla każdej K sprawdzono dokładną symetrię centrowania, parametr docelowy odzyskiwano Newtonem z **celowo innego punktu startowego**, używając poprawnej siatki czasowej `Fraction`, NIE starszego uszkodzonego float-knot Jacobianu. Przy N=300000:

| K | h_max | ścisły wzór na eta_curv | numer. ||z_rec−z||₂ | konserwatywna granica ||z_rec−z||₂ |
|---:|---:|---:|---:|---:|
| 2 | 1 | 5.0000e-9 | 1.2949632e-4 | 4.1853817e-4 |
| 3 | 1/2 | 1.2500e-9 | 3.2374077e-5 | 1.0463453e-4 |
| 5 | 1/4 | 3.1250e-10 | 8.0935189e-6 | 2.6158652e-5 |
| 9 | 1/8 | 7.8125e-11 | 2.0233794e-6 | 6.5396824e-6 |

Przy 5 referencjach i `eps_ref=1e-10,eps_target=5e-11` zastosowanie ostrzejszego centrowania daje `eta≈4.7916668e-10`, syntetyczny błąd z ~`8.90e-6` poniżej certyfikatu ~`4.43e-5`. To nie jest estymata szumu urządzenia.

**Jawne dyskretne ślepe pary:** dla K=2/3/5/9 i N=200000/300000/1000000 skonstruowano dwie dodatnie różne historie z identycznymi idealnymi odczytami w każdej referencji, z niezerowym kompensującym gainem w środku jednej przerwy. Odtworzone normy różnicy z są większe niż `6.74e-7`, a wszystkie sześć docelowych odczytów zgadzają się numerycznie z residuum `<1e-13`. Ścisła niejednoznaczność jest udowodniona przez konstrukcję `C²` i otwartość obrazu, nie przez małe residua jako rzekomy dowód dokładnej równości arytmetyki zmiennoprzecinkowej.

**Failure semantics:** dodatkowe idealne referencje nie gwarantują ścisłej identyfikacji nieznanego dryfu; ograniczenie krzywizny musi pochodzić z zewnątrz, bo same węzły go nie certyfikują; skorelowany szum odniesienia daje niezerową granicę certyfikatu nawet dla K→∞; brak ograniczenia wzmocnienia t uniemożliwia uniwersalną bezwzględną granicę B; wynik nie obejmuje dowolnych profili `alpha` i historycznego produkcyjnego K_A.

## 7. Kontrole, odtwarzalność, status

SZEŚĆ programów i walidacji: `rot047_exact_multireference_design.py` — **1056** wykonywanych dokładnych sprawdzeń Fraction dla przerw/`C²` bump i ostrego `q-1/q`; `rot047_highprecision_lognoise_floor.py` — **222** testy `mpmath` na 105 cyfrach, niezerowy szum skorelowany; `rot047_multireference_source_finite_inverse.py` — **126** asercji pełnej źródłowo dyskretnej rekonstrukcji dla trzech wielkich N i K=2/3/5/9, wymierne węzły; `rot047_finite_reference_blindspot.py` — **177** niezależnych konstrukcji source-finite ślepej pary i idealnych referencji; `rot047_reference_budget_gate.py` — **84** wysokoprecyzyjne kontrole warunkowego minimalnego K/noise-floor; **RETAINED** `rot044_literal_aux_source_gain.py` — **29** dosłownych wywołań niezmienionej pomocniczej implementacji pełnego TT `N=12/16` oraz `E`, pełnego trójczłonowego Lie i projekcji, maks. względny błąd Fouriera `2.69644e-16` (dziedziczone, nie nowy eksperyment). SUMA **1694/1694 wykonanych, typowanych asercji PASS**. Tysiące asercji wymiernych i powtarzane dane syntetyczne nie są niezależnymi pomiarami fizycznymi.

Pakiet lokalny użytkownika: `GEEKY_S11_ROT047_MULTIREFERENCE_SPACING_NOISE_FLOOR_REPRO_001.zip`, rozbudowany niniejszy polski raport, sześć uruchamialnych testów, sześć oryginalnych JSON oraz logów, oryginalny niezmieniony plik pomocniczy i trzy moduły pomocnicze, `README.md`, jawny manifest SHA256. Wymagane sprawdzenia: CRC ZIP, sumy wszystkich plików manifestu i czyste uruchomienie sześciu programów z porównaniem wyników bajt po bajcie. Nie twierdzimy, że pliki ZIP lub programy zostały zamieszczone w GitHub, jeśli zapisano tam tylko raport.

**Sufit:** `NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / REFEREE_PENDING / BW_PENDING`. Bez historycznego produkcyjnego `dtc0a_runtime_v0_3_1.py`, bez maski `h=fI`/`K_A`, bez fizycznych claimów NCDG, bez prawdziwych danych o krzywiźnie dryfu i szumie aparatury. `NO_NEW_TASK`.