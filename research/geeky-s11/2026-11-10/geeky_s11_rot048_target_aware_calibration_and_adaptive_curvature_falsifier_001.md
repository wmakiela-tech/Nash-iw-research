---
artifact_id: GEEKY-S11-ROT048-TARGET-AWARE-CALIBRATION-ADAPTIVE-CURVATURE-FALSIFIER-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-11-10
exposure: PUBLIC
source_class: RETAINED_AUXILIARY_SOURCE_EXACT_RATIONAL_TIME_GRID_AND_CLASSICAL_INTERPOLATION
status: SOURCE_TYPED_REPRODUCIBLE_TESTS_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT048 — Celowana kalibracja przy znanym czasie pomiaru i niemożliwość samocertyfikacji krzywizny dryfu ze skończonych referencji

## 0. Pierwszeństwo i dokładny zakres nowej pracy

**Wyniki wcześniejsze pozostają przypisane ich autorom:** ROT015–017: źródłowy problem projekcji TT na parzystych siatkach (surowe `raw-k` realcast A kontra zgodne rzeczywiste `B=GA`); ROT027/029: źródłowy, uśredniony po wszystkich pozycjach pojedynczy pełny transport Liego i symbol Fouriera; ROT033: zmienne źródłowe filtry; ROT034: negatywny wynik dla nieograniczonych harmonogramów; ROT035–037: ograniczony sześciopoziomowy model i lokalne źródłowo dyskretne odwracanie; ROT038: nominalny dobór sześciu sond; ROT039–040: nieodporność tego wyboru i certyfikat przedziałowy; ROT041: dokładna algebraicznie kompresja blokowa; ROT042–043: jednostajny próg dużych siatek i lokalna odwracalność obejmująca załamania; ROT044: globalna odwracalność tylko w **ograniczonym** stożku sześciopoziomowym dla znanych względnych wzmocnień; ROT045: ślepa symetria nieznanych gainów i konieczność referencji, negatywna informacja o fałszywym Jacobianie float-knot; ROT046: gładki dryf niewidoczny dla dwóch referencji i ostre `H*gap²/8` przy *zewnętrznie znanym* `H`; ROT047: równomierne rozmieszczenie minimalizuje *jednostajny na całym czasie certyfikat* dla `K` referencji, ale skończone `K` nie usuwają niejednoznaczności; jawne ograniczenia szumu i budżet `K`.

**Nowy przyrost ROT048:** (a) matematycznie jawny, zależny od czasu pomiaru docelowego projekt referencji, który falsyfikuje bezwarunkowe przenoszenie „równomierny = najlepszy” z kryterium globalnego ROT047 do kryterium jednego celu; (b) konstrukcja `C^infty` z **dowolnie dużą** krzywizną, lecz dokładnie niewidoczna dla dowolnej *kończącej pracę deterministycznej adaptacyjnej* strategii referencji; (c) niezależne źródłowo dyskretne porównanie odwracania dla `K=4,7,9`, z osobnym negatywnym przykładem nierozróżnialnych historii; (d) prognoza certyfikatu `||z_hat-z||` przy skorelowanym deterministycznym błędzie referencji, bez mieszania wartości empirycznych z gwarancją.

Wszystkie nierówności interpolacyjne, funkcje gładkie o zwartym nośniku, otwartość obrazu i lokalne twierdzenia odwrotne należą do klasycznej analizy / optimal recovery. Literatura porównawcza, bez twierdzenia o pierwszeństwie: P.M. Morkisz, L. Plaskota, *Complexity of approximating Hölder classes from information with varying Gaussian noise*, Journal of Complexity 60 (2020), 101497, DOI `10.1016/j.jco.2020.101497`; S. Borodachov, T. Sorokina, *Optimal recovery of twice differentiable functions based on symmetric splines*, Journal of Approximation Theory 164 (2012), 1443–1459, DOI `10.1016/j.jat.2012.07.004`. Ich szczegółowe hipotezy nie są utożsamiane z niniejszym wąskim wynikiem.

Źródło: dosłownie zachowany **pomocniczy** `deepseek_python_20260627_a87249.py`, rzeczywisty SHA256 bajtów `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`. Historycznego produkcyjnego `dtc0a_runtime_v0_3_1.py` nie mamy. Matematyczny host: pełne niezamaskowane płaskie parzyste `N³`, rzeczywiste symetryczne TT z `B=GA`, źródłowe pełne trójczłonowe centered Lie przy `C=(0,cos x,0)`, `E_alpha=I+alpha*h²*Delta2`, legalne `0<=alpha<=1/6`. **Nie** jest to historyczny maskowany `h=fI/K_A`, twierdzenie NCDG o fizyce J3/K, GR, GW lub PBH.

## 1. Klasa eksperymentu odziedziczona po ROT044–047

Sześć wybranych odczytów `(H0+,H1-,H1+,H2-,H3+,H4-)`, znane poziomy dawki `x_j=j*.009/5`, znane pięć ramp z `v=.012`, nieznane dodatnie czasy sześciu plateau o sumie `.25` oraz nieznane wspólne wzmocnienie `t>0`. Zmienne `z=(t,td0,...,td4)` należą do otwartego wypukłego stożka `C`. Dla `N` parzystego `>=200000` i **znanych względnych** gainów sześciu kanałów korzystamy warunkowo z wcześniej przedstawionego, oczekującego niezależnej recenzji wyniku ROT044:

`||F_N(z)-F_N(z')||_2 > c||z-z'||_2`, `c=1.2e-5` na `C`.

Mapa `F_N` jest dokładną źródłowo dyskretną uśrednioną sumą Fourierowskich iloczynów `q_{in/out,j}=1-4alpha_j S_{in/out}`, `alpha_j=N²[a(j/m)-a((j-1)/m)]`, `m=round(.12N²)`. Dla bardzo dużych siatek wartości wyznacza kompresja blokowa z **dokładnymi wymiernymi granicami czasu** (`rot044_fraction_source_core.py`, `rot045_fraction_jacobian_core.py`), nie niedopuszczona już do certyfikacji wadliwa zmiennoprzecinkowa wersja Jacobianu ROT041. Pełnej tablicy `N³` przy wielkich N nie alokowano.

Dryf gainów relatywnych `g_i(tau)=exp(ell_i(tau))`, `sum ell_i=0`; każda referencja ma znane `d_ref` oraz dowolny nieznany bezwzględny gain. Centrowanie sześciu logarytmów ilorazów `Y_i_ref/Omega_i(d_ref)` odzyskuje wartości `ell_i` w referencjach, chyba że występują błędy referencyjne. **Cały pozytywny rachunek interpolacyjny zakłada odrębnie uzasadnioną normę krzywizny `|ell_i''|<=H`.**

## 2. R48.1 — projektowanie względem JEDNEGO znanego celu, nie całego przedziału

Niech jeden pomiar docelowy ma znany czas `tau in (0,T)`, a dwie sąsiadujące go referencje przypadają w chwilach `a<tau<b`. Dla lokalnej interpolacji liniowej log-gainu klasyczna reszta Peano daje dokładny, ostry dla **tego interpolatora** certyfikat:

`eta_target = H*(tau-a)*(b-tau)/2`.

Ostrość: `ell_1(s)=H*s*(T-s)/2`, `ell_2=-ell_1`, pozostałe zero. Po usunięciu części liniowej reszta kwadratowa w punkcie tau jest **dokładnie** `H*(tau-a)*(b-tau)/2` dla każdej pary `a,b`, także gdy pozostałe węzły referencyjne mierzą tę samą parabolę. Nie twierdzimy, że interpolacja liniowa jest minimaksowa wśród wszystkich możliwych algorytmów wykorzystujących wszystkie węzły.

Jeśli wymaga się **minimalnego odstępu stanowiska referencyjnego `s>0` od celu po obu stronach**, tj. `tau-a>=s`, `b-tau>=s`, to certyfikowana granica `eta_target` jest minimalna dla `a=tau-s`, `b=tau+s`, z minimum `H*s²/2`. Jeśli dozwolone jest wykonanie referencji dokładnie przy celu, ten składnik błędu jest zerowy. Jeśli nie ma dolnego odstępu `s` lub kosztu pomiaru, problem minimalizacji tej granicy ma infimum zero osiągane w granicy dwóch referencji zbliżających się do celu; nie ma dodatniej uniwersalnej optymalnej odległości. Dodatkowe referencje służą innym chwilom lub diagnostyce modelu, nie poprawiają *tej konkretnej* granicy najbliższej pary.

Dokładny przykład wymierny: `T=1,tau=47/100,s=1/20,H=4e-8`. Z zachowaniem końcowych referencji 0 i 1, cztery ukierunkowane węzły `(0,.42,.52,1)` dają `eta_target=5e-11`. Cztery równomierne `(0,1/3,2/3,1)` dają `eta=5.37555555...e-10` (gorszy certyfikat **10.7511111x**), siedem równomiernych `(j/6)_{j=0}^6` `eta=8.2e-11`, dziewięć `(j/8)_{j=0}^8` `eta=5.7e-11`. Istotny jest dokładnie jeden cel `tau=.47`, a nie globalny maksymalny błąd na `[0,1]`. Równomierność z ROT047 pozostaje poprawna dla **innego kryterium** `min max_gap`.

## 3. R48.2 — skończone ADAPTACYJNE referencje nie certyfikują H

Niech strategia deterministyczna próbuje badać globalne ograniczenie `sup_t |ell_i''(t)|<=H` przez kolejne adaptacyjnie wybierane, skończenie wiele dokładnych referencyjnych odczytów (także z pomiarem dowolnej skończonej liczby pochodnych we wskazanych chwilach). Rozważmy jej **ukończoną** trajektorię przy zerowym względnym dryfie `ell=0`. Zostaje przynajmniej jeden otwarty niepróbkowany przedział. Po zakończeniu strategii wybieramy punkt `c` i mały `w>0` tak, aby cały `(c-w,c+w)` leżał w tym przedziale. Definiujemy:

`b(t)=epsilon*exp(4 - 1/[u(1-u)])`, `u=(t-(c-w))/(2w)` dla `0<u<1`, a poza nośnikiem `b=0`; `ell=(b,-b,0,0,0,0)`.

To funkcja klasy `C^infty`, a jej wszystkie pochodne znikają poza zwartym nośnikiem oraz na jego brzegach. Zatem dla wszystkich zapytanych czasów `ell` i dowolne mierzone pochodne są identyczne ze scenariuszem zerowym. Algorytm adaptacyjny widzi **identyczną całą trajektorię odpowiedzi, więc wybiera identyczne dalsze czasy i kończy w identycznym stanie**. Ale

`b(c)=epsilon>0`, `b''(c)=-8epsilon/w²`.

Dla dowolnego z góry ustalonego `H<infinity` można zmniejszyć `w`, uzyskując `sup|ell_i''|>H` **bez zmiany danych w żadnej z referencji**, nawet przy arbitralnie małym `epsilon`. Dlatego nie istnieje ogólny algorytm, który na podstawie skończonych wartości (lub skończonych jetów) referencji wiarygodnie *potwierdzałby* globalne `H` w nieparametrycznej klasie `C^infty` bez dodatkowych założeń. To twierdzenie epistemiczne o informacjach skończonych, nie o braku rzeczywistego `H` w danym urządzeniu. Dowód obejmuje kończące pracę **deterministyczne** strategie adaptacyjne. Nie formułujemy bez dodatkowych argumentów identycznego probabilistycznego twierdzenia dla protokołów losowych ani tych, które wykonują referencję dokładnie w zapowiedzianym czasie docelowym: w tym ostatnim przypadku kalibracja względna w samej chwili jest bezpośrednio znana.

**Konsekwencja źródłowa:** jeżeli cel `tau` leży w niepróbkowanej przerwie, w której umieszczono nośnik, to względny gain w chwili celu jest niezerowy, mimo wszystkich idealnych referencji. Przy dowolnym wewnętrznym `z` i dostatecznie małym `epsilon`, otwartość obrazu źródłowo skończonego `F_N(C)` (warunkowy wynik ROT044 i twierdzenie o niezmienniczości wymiaru) zapewnia inne dopuszczalne `z' != z`, które przy stałym gainie dają **dokładnie** identyczne wszystkie obserwacje referencyjne i celowe jak pierwotne `z` przy niewidocznym dryfie. Nie należy mylić tego algebraiczno-topologicznego istnienia z małym numerycznym residuum FFT.

## 4. R48.3 — determinizm szumu i certyfikat odwrotności dla znanej chwili

Dla błędu multiplikatywnego każdej referencji `|e_i|<=eps_ref<1`, bez zakładania niezależności statystycznej, wynik ROT047 daje ostry sześciokanałowy błąd centrowanego logarytmu:

`eta_ref = (5/6)*log[(1+eps_ref)/(1-eps_ref)]`.

Lokalny łączny błąd log-kalibracji w chwili tau:

`eta = H*(tau-a)*(b-tau)/2 + eta_ref`.

Dodatkowy względny błąd celu `eps_target` daje `q=(1+eps_target)*exp(eta)-1`. Jeżeli dodatkowo niezależnie wiadomo, że `||F_N(z)||_2<=B`, i kandydat `z_hat` pozostaje w dopuszczalnym stożku `C`, przy reszcie skorygowanego dopasowania `r`, **warunkowo na ROT044**:

`||z_hat-z||_2 <= [r+q*B]/c`, `c=1.2e-5`, `N` parzyste `>=200000`.

Syntetyczne przykładowe ograniczenia: `B=1.01`, `eps_ref=1e-10`, `eps_target=5e-11`, `r=0`, cel dopuszczalnego błędu `delta_z=3e-5`. Dla 4 referencji ukierunkowanych `qB/c≈2.24444e-5` (certyfikat PASS), dla 4 równomiernych `≈6.34804e-5` (certyfikat FAIL), dla 7 równomiernych `≈2.51378e-5` (PASS), dla 9 równomiernych `≈2.30336e-5` (PASS). Mniejszy numer referencji może więc osiągnąć przy **jednej znanej chwili** tę samą warunkową tolerancję, mimo że byłby dużo gorszy dla globalnej, nieznanej w czasie chwili pomiaru.

Wartość `B` nie jest uniwersalna: przy nieograniczonym `t` wzrasta bez ograniczenia. Najważniejsze: **bez niezależnego certyfikatu rzeczywistego H w ogóle nie istnieje ważna ilościowa gwarancja z tego rozdziału**, nawet jeśli w testach ref-kalibracji nie wykryto dryfu. Żaden z użytych `H/eps/B` nie został wyznaczony na fizycznej aparaturze.

## 5. Wykonane odtworzenie dokładnego źródłowo dyskretnego modelu

Dla N parzystych `200000,300000,1000000`, matematycznie legalnego `z=(1.07,1.07*d0,...,1.07*d4)` i profilów testowych (np. `d_target=(.042013279,.041233731,.040822091,.045112967,.040733239)`) wygenerowano sześć źródłowych odczytów z wymiernymi granicami ramp, zmiennym nieznanym bezwzględnym gainem każdej referencji, normalizacją sześciu logarytmów i **niezależnym, poprawionym Jacobianem Fraction**. Funkcja wymiernych granic oblicza sumę uśrednionych pozycji jednego źródłowego Liego bez pełnego tensorowego N³ dla wielkich N. Zastosowano cel `tau=.47`, `H=4e-8`, syntetyczny log-dryf `(base+slope*(tau-.5)+H*tau*(1-tau)/2*(1,-1,0,...))`, potem odwrócono skorygowany pomiar Newtonem z celowo odległego punktu startowego. Przy N=300000:

| Projekt | eta_curv | numeryczny `||z_rec−z||` | konserwatywna granica tego konkretnego bezszumowego testu |
|---|---:|---:|---:|
| 4 ukierunkowane `(0,.42,.52,1)` | 5.0000e−11 | 1.29496616e−6 | 4.18540242e−6 |
| 4 równomierne | 5.3755556e−10 | 1.39222945e−5 | 4.49975334e−5 |
| 7 równomiernych | 8.2000e−11 | 2.12374147e−6 | 6.86404330e−6 |
| 9 równomiernych | 5.7000e−11 | 1.47625886e−6 | 4.77136634e−6 |

Dodatkowo przetestowano przy `eps_ref=1e−10`, `eps_target=5e−11` skorelowane skrajne błędy log-centrowania; poprawna nierówność `q` i pochodny błąd inverse przeszły. Tabela `bezszumowa` ma **inne** granice niż formalne budżety z punktu 4, gdzie dopuszcza się szum i używa `B=1.01`; nie utożsamiać tych liczb.

**Źródłowo dyskretny niewidoczny dryf:** skonstruowano bump `C^infty` z `epsilon=2e−9`, `w=.001`, celem `.47` niebędącym referencją w zestawach K=4/7/9. Jego rzeczywista wartość `|b''(.47)|=0.016`, czyli **400 000 razy** więcej niż przykładowa zakładana krzywizna `H=4e−8`, przy **dokładnie zerowych referencyjnych odczytach dryfu**. Alternatywne dodatnie, legalne `z'` przy `N=200000,300000,1000000` miały `||z'-z||≈5.17985e−5`, a wszystkie sześć odczytów w chwili celu dopasowano numerycznie z błędem `<=8.33e−16`. Matematyczna równość jest gwarantowana lokalnym istnieniem odwrotności, nie przez `float64`.

**Dosłowny audyt źródła:** osobno powtórzono odziedziczony `rot044_literal_aux_source_gain.py` dla małych pełnych `N³=12³,16³`, dosłownie używając niezmienionych `apply_P_TT`, `apply_E`, pełnego trójczłonowego Liego, max względna różnica Fouriera `2.6964379303e−16`. Nie twierdzimy, że wykonywano pełny tensor przy `N=1000000`. Nie jest to nowa walidacja historycznego kodu produkcyjnego.

## 6. Falsyfikatory, zakres i niezależna recenzja

- **R48.1:** NIE rozszerzać minimaksowego rozkładu dla całego `[0,T]` z ROT047 na znany czas pojedynczego celu. Projekt zależy od funkcji celu, minimalnego odstępu i danych fizycznych; sam `K` nie wystarcza.
- **R48.2:** NIE próbować wyznaczać bezwarunkowego certyfikatu `H` wyłącznie z dowolnej skończonej, również adaptacyjnej, liczby idealnych referencji. Bez zewnętrznej regularności można osadzić `C^infty` bump o dowolnej krzywiźnie i małej amplitudzie.
- **R48.3:** NIE przenosić błędu `z=(t,td)` na jednostajną dokładność `d=z_i/t` przy `t→0`; NIE porównywać budżetu bezszumowego z budżetem obejmującym błędy.
- **R48.4:** Wszystkie obliczenia są dla **ograniczonej sześciopoziomowej rodziny**. Wyniki ROT034 o nieidentyfikowalności dowolnych źródłowych harmonogramów oraz negatywne wyniki ROT039–040 pozostają w mocy. Certyfikat ROT044 jest nadal niezależnie niezweryfikowany.
- **R48.5:** Bump `C^infty` nie jest analityczny na granicy nośnika; dla dodatkowego wymogu globalnej analityczności lub znanego modelu skończenieparametrowego potrzeba osobnego rachunku; dla losowego, niekończącego się próbkowania również nie twierdzimy wyniku.

## 7. Programy, sumy i ponowny odczyt

SZEŚĆ odtwarzalnych programów:

1. `rot048_exact_target_design.py` — dokładne ułamki `Fraction`, porównanie układów K4/K7/K9, para-krańce i stand-off, **946 typowanych asercji PASS**.
2. `rot048_adaptive_curvature_falsifier.py` — niezależny adaptacyjny schemat wyboru węzłów, bump `C^infty`, 75-cyfrowe różnice pochodnych, **617 PASS**.
3. `rot048_source_finite_target_inverse.py` — oryginalne dokładnie dyskretne symbole uśrednionego transportu i poprawiony wymierny Jacobian, trzy duże N i ścisła syntetyczna norma błędu, **141 PASS**.
4. `rot048_source_finite_hidden_bump.py` — niezależny źródłowy kompensator niewidocznego gainu przy K4/K7/K9 i trzech N, **148 PASS**.
5. `rot048_highprecision_target_noise.py` — niezależne 100-cyfrowe oszacowania Peano, ostry sześciokanałowy szum i warunkowy limit rekonstrukcji, **34 PASS**.
6. `rot044_literal_aux_source_gain.py` — **29 PASS ODZIEDZICZONYCH** testów niezmienionego pełnego kodu pomocniczego na małych siatkach, nie nowy dowód historycznej realizacji.

**SUMA 1915/1915 rzeczywiście wykonanych typowanych asercji PASS.** Większość asercji to niezależnie wykonywane kontrole wymierne i syntetyczne, a nie 1915 niezależnych eksperymentów. W trakcie opracowania dwie pierwsze wersje pomocniczego testu szerokości bump nie przeszły testu; warunki sprawdzenia zmodyfikowano przed zaliczeniem i zamknięciem. Nie zmieniano niezmienionego kodu źródłowego. Ostateczny ZIP powinien przejść kontrolę CRC, SHA256 każdego pliku w manifeście, sześć czystych uruchomień i sześć bajtowo identycznych JSON.

**Sufit:** `NO_MATH_NOVELTY / REFEREE_PENDING / BW_PENDING / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_HISTORICAL_MASKED_K_A / NO_REAL_INSTRUMENT_CALIBRATION`. Wynik jest samodzielnym rozszerzeniem walidacji matematycznego modelu pomocniczego, nie akceptacją rozwiązań fizycznych IW/NASH.