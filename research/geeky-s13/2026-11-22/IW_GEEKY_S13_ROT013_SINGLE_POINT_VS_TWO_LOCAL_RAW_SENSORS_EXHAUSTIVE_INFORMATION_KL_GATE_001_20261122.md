---
artifact_id: IW_GEEKY_S13_ROT013_SINGLE_POINT_VS_TWO_LOCAL_RAW_SENSORS_EXHAUSTIVE_INFORMATION_KL_GATE_001_20261122
return_id: IW_GEEKY_S13_ROT013_ORIGINAL_M13_SIX_MASK_SINGLE_POINT_SITE_EXHAUSTIVE_KL_AND_TWO_ADJACENT_SITE_INFORMATION_RESOURCE_ESCAPE_001_20261122
origin_cell: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-22 Europe/Warsaw
classification: ORIGINAL_M13_N41_MASK_GEOMETRY_PLUS_ROT038_FIXED_ANISOTROPIC_SYNTHETIC_GAUSSIAN_LINEARSITE_STATISTICAL_EXPERIMENT
original_firstness: M13_ORIGINAL / GEEKY_S12_ROT038_ORIGINAL_A_B_AND_NINE_ALIAS / GEEKY_S13_ROT012_SIX_MASK_OBSERVABILITY_NOGO / M16_ROT004_DIFFERENT_QUADRATIC_GAUSSIAN_MASK_ALIASES
result: SINGLE_RAW_SITE_104_EXACT_TYPE_KL_IV75_GLOBAL_OPTIMUM / 41289_EXACT_ALIAS_SITES / 32400000_NECESSARY_N_95 / TWO_RAW_ADJACENT_SITE_BHATTACHARYYA_957177_SUFFICIENT_95
proof_status: AUTHOR_FULL_N41_EXACT_INTEGER_AND_FRACTION_IV75 / INDEPENDENT_SAME_CELL_FULL_SPATIAL_FFT / COLD_REPRO / DIFFERENT_CELL_I1_PENDING
claim_ceiling: NO_GENERAL_MATH_NOVELTY / NO_AUTHENTIC_M13_RAW_SITE_SENSOR / NO_HISTORICAL_DTC0A / NO_PHYSICAL_NASH_CLAIM / NO_CANON / NO_EXEC_SIGN / BW_PENDING
---

# Geeky-S13 ROT013 — czy jeden nowy punkt wystarczy? Dokładna mapa informacji 68 921 lokalizacji i kontrast z dwiema sąsiednimi sondami

## 0. Najważniejszy wynik i rozróżnienie od wcześniejszego dorobku

**Problem.** Geeky-S13 ROT012 dowiódł nieodtwarzalności czteromodowego ilorazu Fouriera z sześciu oryginalnych średnich regionowych M13. Geeky-S12 ROT038 wcześniej pierwszy dowiódł dokładnego aliasu prawa starego obserwatora (nawet sześć plus trzy lokalne głębokie kontrasty) dla dwóch syntetycznych anizotropowych hipotez gaussowskich A/B. Czy **jeden dodatkowy surowy pomiar wartości pola na jednej konkretnej komórce** — zarejestrowany wspólnie z oryginalnymi sześcioma średnimi w każdej niezależnej próbie — może przełamać alias i czy ma to jakikolwiek sens statystyczny?

**Werdykt matematyczny.** Dla **41 289 spośród 68 921** położeń nowy punkt nadal daje *dokładnie identyczne całe siedmiowymiarowe gaussowskie prawa* A/B: brak informacji przy dowolnym n. Dla pozostałych **27 632** położeń modele są formalnie rozróżnialne. W ramach **wszystkich bez wyjątku 68 921 pojedynczych lokalizacji** maksimum źródłowego `KL(A||B)` osiąga położenie `(5,4,6)` (oraz klasa geometrycznie równoważnych miejsc); exact-class/IV75:

`KLmax(A||B)=0.0000000494423557252017319735963876757295999248834583671356042496706...`

Drugi, odwrócony `KLmax(B||A)≈0.00000004944201650267959...`. Wszystkie 104 odmienne źródłowe klasy są przedziałowo zweryfikowane, a następna najlepsza klasa ma ściśle niższy KL. W szczególności dla **każdego ustalonego miejsca** obie kierunkowe dywergencje są `KL<5×10^-8`. Zatem Pinsker daje dla **n≤32 400 000 IID pełnych siedmiokanałowych obserwacji** błąd średni *ściśle większy niż 5%*. Przy **n=1 000 000** żaden taki jednopunktowy eksperyment nie przekroczy średniej trafności **57.9057%**. To są **dolne granice koniecznego n**, a nie twierdzenie o wystarczającej liczbie pomiarów.

**Alternatywa — dwa odczyty sąsiednich komórek bez sześciu masek.** Znane, jednostkowo znormalizowane gaussowskie wartości dwóch sąsiednich punktów w osi x mają pod A korelację `r_A=1/50`, a pod B `r_B=1/40`. Ich dokładne dwuwymiarowe prawo daje `KL(A||B)=1.2520487569×10^-5`, czyli **253,23 razy większe** niż najlepszy pojedynczy punkt **wraz z sześcioma wcześniejszymi odczytami**. Dokładny analityczny współczynnik Bhattacharyyi ma wartość `rho≈0.999996870244981394499984...`; rygorystyczna ocena `rho^n<.05` daje **n=957 177 jako pierwszą liczbę spełniającą wyłącznie tę konkretną nierówność Chernoffa**. To jest ścisła liczba wystarczająca, ale **NIE minimalny koszt optymalnego testu dla dwóch punktów**.

**Pierwszeństwo.** M13 FIRST źródłowy pomocniczy tensor B `41³`, oryginalny blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`; Geeky-S12 ROT038 FIRST dokładne racjonalne anizotropowe dwa szumy i sześciu/dziewięciu obserwatorów alias, blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`; Geeky-S13 ROT012 FIRST no-go **rekonstrukcji czteromodowej statystyki** z sześciu masek, blob `16ea5df956eb51ff9b010f2e97e5845f4d614a7b`. M16 ROT004 bada **inną hipotezę**: quadratic mask of centered Gaussian field and swapped B/Bpi; nie utożsamiamy tych eksperymentów. ROT013 pierwszy wyczerpujący 104-typowy audyt *pojedynczego surowego punktu dołączonego do oryginalnego liniowego obserwatora* i niezależny kosztowy kontrprzykład dwupunktowy.

Bezpośrednio przeczytane źródła:
- M13: https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py
- ROT038: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s12/2026-11-21/IW_GEEKY_S12_ROT038_ORIGINAL_M13_ANISOTROPIC_DIRECTIONAL_EXACT_ALIAS_ONE_BOUNDARY_PROBE_ESCAPE_AND_NONGAUSSIAN_DEPENDENCE_001_20261121.md
- ROT012: https://github.com/wmakiela-tech/Nash-iw-research/blob/7d895f8b62a5058109e557ea0e3f4521849c469b/research/geeky-s13/2026-11-22/IW_GEEKY_S13_ROT012_ORIGINAL_M13_SIX_MASK_FOURIER_OBSERVABILITY_NOGO_001_20261122.md
- M16 ROT004: https://github.com/wmakiela-tech/Nash-iw-research/blob/cc4632fbad6065779bf5be137a251af6dfeb921d/research/m16/2026-11-22/IW_M16_ROT004_CUBIC_MASK_GAUSSIAN_ORBIT_ALIAS_AND_FOUR_MODE_DIRECTIONAL_ESCAPE_001_20261122.md

## 1. Dokładny kontrakt pomiarowy i operator M13

Niech lokalny, **syntetyczny skalar szumu wartości energii** na oryginalnym torusie `41³` ma warunkowo znane, identyczne pod A/B średnie oraz stacjonarną kowariancję z dokładnie tymi współczynnikami modelu ROT038, w kolejności `(beta0,beta_x,beta_y,beta_z,beta_xy,beta_xz,beta_yz,beta_body)`:

`A=(1,1/25,1/25,1/25,1/30,1/30,1/30,2/25)`,
`B=(1,1/20,3/100,1/25,1/30,13/300,7/300,2/25)`.

Każdy operator przesunięcia osiowego ± składa się z **dwóch** sąsiadów, operator przekątnej płaszczyznowej z **czterech**, a przestrzennej z **ośmiu**. Oba operatory kowariancji są SPD z dolną granicą widma `≥7/10`, bo suma dodatnich współczynników innych niż identity wynosi `3/10`. W oryginalnym schemacie sześć znormalizowanych liniowych średnich szumu `M=(M0,...,M5)` bierze się z rozłącznych regionów `R0=T\I2`, `R1=I2\I3`, ..., `R5=I6`, gdzie `Ik=[k,40-k]^3`. Liczności dokładnie `[18268,7778,6938,6146,5402,24389]`. Są one odwracalną liniową transformacją oryginalnego pełnego pomiaru `inner(k0)` i pięciu zagnieżdżonych `inner(k2...6)`, **gdy podstawowym obiektem obserwacji jest wartościowe pole energii na sites**, a nie kwadrat osobnego gaussowskiego pola tensorowego.

Zachowujemy pochodzący z ROT038 **dodatkowy wspólny dla A/B parametr kalibracji pełnej średniej** `beta_cal_raw=1/2500`, działający niezależnie na oryginalny odczyt pełny; po przejściu na sześć regionów dodaje `beta_cal_raw*(68921/18268)^2` **jedynie do `C_6[0,0]`**. Nie przypisujemy tej niezależnej kalibracji nowemu odczytowi punktowemu. Nowy hipotetyczny czujnik zwraca **jedną wartość** `Y_s=E_s`, ze znaną wariancją 1 i bez dodatkowego szumu czujnika. Szukamy po wszystkich `s∈{0,...,40}³`, a punkty wolno wybierać **przed próbą**, nie adaptacyjnie po zobaczeniu danego bieżącego M.

Wyniki są źródłowo warunkowe: nikt nie potwierdził RAW-site sensora, gaussowskich IID migawkowych energii, znanych średnich czy stałej normalizacji. Historyczny pełny program `dtc0a_runtime_v0_3_1.py` brak; w ROT013 oryginalny M13 helper **odczytano**, lecz nie uruchamiano jego ciężkiej funkcji `tensor_polys`.

## 2. Dokładny warunek lokalnego aliasu i liczba 41 289

Niech `w_r=|R_r|`. Definiuj `N_{x,r}(s)` jako liczbę dwóch osiowych ±x sąsiadów punktu s w regionie r; analogicznie `N_y`, a `N_{xz},N_{yz}` jako liczby czterech sąsiadów przekątnych. Oba modele mają te same `beta0`, `beta_z`, `beta_xy`, `beta_body` oraz dokładne różnice:

`beta_x(B)-beta_x(A)=+1/100`, `beta_y(B)-beta_y(A)=−1/100`, `beta_xz(B)-beta_xz(A)=+1/100`, `beta_yz(B)-beta_yz(A)=−1/100`.

W związku z tym źródłowo dokładnie:

`b_{B,r}(s)−b_{A,r}(s) = [2(N_{x,r}(s)−N_{y,r}(s))+(N_{xz,r}(s)−N_{yz,r}(s))] / (400 w_r)`.

Tu `b_X(s)=Cov_X(M,Y_s)∈R^6`. Oryginalne `C_6=Cov_A(M)=Cov_B(M)` są dokładnie identyczne jako 36 liczb wymiernych; wariancja pojedynczego punktu ma zawsze `Var(Y_s)=1` pod oboma modelami. Zatem *pełne* gaussowskie prawa 7-wymiarowe są identyczne **wtedy i tylko wtedy**, gdy `b_A(s)=b_B(s)`. Test wymaga wyłącznie integer neighbor counts; nie wystarcza numeryczne stwierdzenie prawie zera.

Wszystkie 68 921 site w 41³ rzeczywiście wyliczono i uzyskano **41 289 miejsc o dokładnym aliasie** oraz **27 632 miejsc informatywnych**. Przeważają miejsca lokalnie jednorodne i niewrażliwe na kierunkowe rozszczepienie. Mimo że inne agregaty mogą odróżniać hipotetyczne pola, *ten konkretny stary obserwator + jeden punkt* w 59,91% lokalizacji nadal nie zawiera **jakiejkolwiek** informacji o źródłowej parze A/B.

## 3. Wyczerpująca informacja KL i rachunek wymierny / IV75

Dla wybranej komórki s postuluje się IID siedmiowymiarowe obserwacje Gaussa. `M∼N(μ_M,C_6)` identycznie pod A/B, `Y_s∼N(μ_s,1)` marginalnie identycznie, jedynie `b_X` może się zmieniać. Wskutek Schura:

`Y_s|M, X ∼ N( μ_s + b_X(s)^T C_6^{-1} (M−μ_M), v_X(s) )`,
`v_X(s)=1−b_X(s)^T C_6^{-1}b_X(s)>0`.

Wybór praw A/B daje całkiem dokładny klasyczny wzór:

`D_KL(A||B;s)= (1/2){log[v_B(s)/v_A(s)] + [v_A(s)+(b_B(s)−b_A(s))^T C_6^{-1}(b_B(s)−b_A(s))]/v_B(s) − 1}`.

Drugi kierunek otrzymujemy przez wymianę A↔B. Wszystkie liczniki macierzy kierunkowych oraz wszystkie 6×6 elementy C wyznaczono jako **dokładne całkowite liczności i Fraction**. Lokalne sąsiedztwa dzielą siatkę na **104 unikatowe typy** 8×6 klas kierunkowych i regionów. Dla KAŻDEGO ze 104 typów obie dywergencje wyprowadzono z dokładnych wymiernych form Schura i objęto **75-cyfrowym skierowanym przedziałem IV** dla jedynego logarytmu.

Występuje jedno ściśle najlepsze *środowisko lokalne* (116 równoważnych punktów), reprezentant `s=(5,4,6)` należący do `R3`. Jego dokładne wektory:

`b_A=(0,0,7/520350,137/737520,13/1080400,0)`,
`b_B=(0,0,1/83256,697/3687600,11/1080400,0)`.

Dokładny przedział kierunku A||B:

`[0.000000049442355725201731973596387675729599924883458367135604249670555217260432149636222, 0.00000004944235572520173197359638767572959992488345836713560424967055521726112304312063]`.

Również kierunek B||A jest mniejszy od `5×10^-8` dla każdego typu. **Następny maksymalny KL_A||B jest mniejszy niż `4.944102×10^-8`**. Z certyfikatów wynika jednoznacznie:

`sup_{site s, X≠Y} KL(P_X^(M,Ys)||P_Y^(M,Ys)) < 5×10^-8.`

Należy wyraźnie odróżnić te *źródłowo predefiniowane* 7-obserwacyjne eksperymenty od optymalnych pomiarów liniowej kombinacji wielu punktów. ROT013 NIE dowodzi optimum wśród dowolnych 1-wymiarowych filtrów przestrzennych, czujników dwupunktowych czy eksperymentów adaptacyjnych na podstawie bieżących sześciu obserwacji.

## 4. Ostra w sensie rodzaju gwarancja negatywna dla n próbek

Dla IID eksperymentu n prób i dwóch prostych hipotez A/B przy równych wagach, klasyczna nierówność Pinsker–KL daje

`e_n^*(s) = (1−TV(P_A^n,P_B^n))/2 >= [1−sqrt(n KL(A||B;s)/2)]/2`.

Nie trzeba zakładać konkretnego algorytmu. Ponieważ 104 dokładne typy spełniają `KL<5e−8`, dla **każdego stałego punktu**, w tym optymalnego, oraz każdego `n≤32 400 000` mamy `TV<0.9`, a więc **średnia trafność ściśle mniejsza niż 95%**. Przy `n=1 000 000`: `TV<sqrt(0.025)=0.158113883...`, zatem średnia trafność **ściśle mniejsza niż 57.9056942%**. Jeśli wymaga się >95% trafności dla KAŻDEJ hipotezy, to także średnia trafność musiałaby przekroczyć 95%; jest to więc silny konieczny kontrprzykład dla tamtego wymogu.

Oszacowanie Pinsker jest konserwatywne, lecz wystarcza do udowodnienia poważnej bariery metrologicznej jednego czujnika. `n=32 400 000` nie jest ostrym progiem NP; przy dokładnym najlepszym KL samo oszacowanie pozwala zwiększyć tę konieczną liczbę do około **32 765 429**, ale konserwatywny, wygodny próg 32,4 miliona pozostaje niezależny od zwężania przedziałów IV.

## 5. Konstrukcyjny kontrprzykład: DWA sąsiednie surowe punkty

Zamiast zbierać sześć agregatów plus jeden nowy punkt, dopuszczamy **dwa hipotetyczne, jednocześnie odczytane i znormalizowane punkty** `Y_s,Y_(s+e_x)` (bez sześciu M). Dla czystego stacjonarnego szumu ROT038, znanych identycznych średnich, `Var(Y_s)=Var(Y_(s+ex))=1` pod A/B i **różne dokładne korelacje**:

`rho_A^(pair)=beta_x(A)/2=1/50`, `rho_B^(pair)=beta_x(B)/2=1/40`.

Ich macierze Σ_X są `[[1,r_X],[r_X,1]]`. Wyznaczamy dokładną dywergencję dwu-Gaussów:

`KL_pair(A||B)=(1/2)[tr(Σ_B^{-1}Σ_A)−2+log(detΣ_B/detΣ_A)]≈0.000012520487569307487`.

Stosunek do najlepszego jednopunktowego eksperymentu z sześcioma agregatami wynosi `≈253.234`; TO JEST PORÓWNANIE INFORMACJI NA JEDNĄ IID MIGAWKĘ, NIE CAŁKOWITEGO KOSZTU SENSORÓW ani odporności na zakłócenia kalibracyjne.

Dokładny współczynnik Hellingera/Bhattacharyyi:

`rho_Bh = [(1−r_A²)(1−r_B²)]^(1/4) / [1−((r_A+r_B)/2)²]^(1/2)`
`       =0.999996870244981394499984035616488577...`.

Dla log-LR prostej pary równych priorytetów, Markow `E_A[(dP_B/dP_A)^1/2]^n = rho_Bh^n` i analogicznie pod B zapewnia **każdy z dwóch błędów** `<=rho_Bh^n`. Faktycznie wykonany niezależny IV75:

- `rho_Bh^957176 > 0.0500000597955` — **ta konkretna granica Chernoffa nie gwarantuje jeszcze 95%**, ale test NP może je osiągać wcześniej;
- `rho_Bh^957177 < 0.0499999033077` — **konserwatywnie wystarcza do >95% pod KAŻDĄ hipotezą**;
- `rho_Bh^960000 < 0.0495600843797` — komfortowy margines.

Uwaga: stała korelacja w tej konstrukcji zakłada źródłowy, znany współczynnik wariancji i model gaussowski. Przy dowolnej nieznanej *multiplikatywnej kalibracji zależnej od próby*, latentnych niegaussowskich rozkładach lub nieznanych wspólnych wartościach oczekiwanych certyfikat **nie obowiązuje**. Nie przypisujemy parze punktów odporności na dowolną separowalną kalibrację ROT007–010.

## 6. Dwa niezależnie napisane programy, testy negatywne i zakres falsyfikacji

**Program pierwotny** rekonstruuje pełny oryginalny podział M13 68 921 punktów, dokładnie liczy 8 klas przesunięć i wszystkie 36 wariancji/kowariancji między sześcioma agregatami, włącza niezależną kalibrację βcal=1/2500, enumeruje **wszystkie** 68 921 położeń, dokładnie sprawdza 41 289 zero-δb przez liczności sąsiadów, kompresuje do 104 odmiennych całkowitych typów, dla KAŻDEGO niezależnie wylicza Schura dokładnymi liczbami wymiernymi i kierunkowe KL w IV75. Potwierdza jedno ściśle najlepsze lokalne środowisko i najbliższy drugi wynik. Wstępne porównanie typu zostało zatrzymane wskutek **błędnego wymogu zerowej arytmetycznej reszty float**; poprawka zastąpiła tę kontrolę **DOKŁADNYM testem liczników sąsiedztwa**. Poprzedniej próby nie zaliczono jako PASS.

**Drugi, niezależnie napisany program** tworzy bez importu pierwotnego kodu dokładnie oryginalną geometrię poprzez odległość od ścian szóstego sześcianu, następnie rekonstruuje oba przestrzenne operatory kowariancji metodą **pełnej periodycznej konwolucji FFT** na 41³, porównuje sześciowymiarowe macierze A/B (`max abs diff<9e−21`), samodzielnie optymalizuje KL, wskazuje `(5,4,6)` i tę samą liczbę 27 632 niezerowych site, oraz sprawdza parę punktową niezależnym rachunkiem IV75 Hellingera. Nie jest to odrębna komórka audytowa I1.

**Negatywna wiedza i granice:** (a) oryginalne `inner(k)` M13 są średnimi *wartości energii wyprowadzonymi z tensora*, a NIE z definicji kwadratami niezależnego prostego szumu Gaussa; osobny M16 ROT004 słusznie bada właśnie inny nieliniowy model, (b) gaussowskość szumu/odczytów punktowych nie jest faktem źródłowo-fizycznym, (c) dodatkowa kalibracja pełnej średniej βcal nie jest kalibracją nowych RAW punktów, (d) liczby n są hipotetyczne, (e) dwa punkty nie są lokalnym niezależnym Gaussowskim przyrządem w M13, (f) własna kombinatoryka nie wykonuje w ROT013 oryginalnego `tensor_polys` ani kompletnego historycznego DTC0a, (g) wynik stanowi metrologiczny i statystyczny kontrast w klasycznym modelu, NIE nową fizykę NASH.

**Bounded outside I1 dla AUD3/REC13/M16:** niezależnie sprawdzić tożsamość formuły `δb=.../(400w_r)`, dokładne 41 289/27 632 i 104 typy, wybór maksimum 5,4,6 dla obydwu KL i IV75 najwyższych dwóch typów, poprawność kalibracji pełnej średniej, klasyczną nierówność Pinsker, surowe dwa punkty plus Hellinger (pełny wynik per-hyp) i identyfikację źródłowego/hipotetycznego operatora. Szczególnie próbować sfalsyfikować granicę przy silniejszej, adaptacyjnej fizycznej kalibracji i nieliniowej energii z M16 ROT004 — nie rozszerzać tego dowodu bez nowego założenia.

**Ostateczny sufit**: `AUTHOR_ORIGINAL_M13_MASK_GEOMETRY_AND_ROT038_RATIONAL_SOURCE / EXHAUSTIVE_N68921_SITE / 104_EXACT_NEIGHBOR_TYPES / ALL104_KL_IV75 / CONDITIONAL_SINGLE_SITE_NECESSARY_N>32400000 / INDEPENDENT_SAME_CELL_FFT / TWO_SITE_BHATTACHARYYA_957177_SUFFICIENT / DIFFERENT_CELL_I1_PENDING / BW_PENDING / NO_PHYSICAL_RAW_SENSOR / NO_GENERAL_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`.
