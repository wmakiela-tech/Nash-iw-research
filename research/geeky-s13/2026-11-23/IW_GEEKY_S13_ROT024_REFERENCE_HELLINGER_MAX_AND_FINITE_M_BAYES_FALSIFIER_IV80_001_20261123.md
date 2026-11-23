---
artifact_id: IW_GEEKY_S13_ROT024_EXACT_REFERENCE_ONLY_HELLINGER_FLOOR_AND_FINITE_M_NONUNIVERSALITY_IV80_001_20261123
return_id: IW_GEEKY_S13_ROT024_KNOWN_ETA_UNKNOWN_Q_EXACT_WORK_ALIAS_MAX_HELLINGER_REFERENCE_SAMPLE_FLOOR_AND_FINITE_BAYES_FALSIFIER_001_20261123
origin_cell: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-23 Europe/Warsaw
exposure: PUBLIC
science_class: SOURCE_TYPED_ROT038_SYNTHETIC_GAUSSIAN / ORIGINAL_M13_GEOMETRY_ROT016 / KNOWN_ETA_UNKNOWN_Q_NO_REFERENCE_ALIAS_ROT019 / REFERENCE_ONLY_EXACT_HELLINGER_MAX / IV80_RESOURCE_NECESSITY / FINITE_M_NP_NONUNIVERSALITY
status: AUTHOR_ANALYTIC_PROOF_AND_IV80_PASS / THREE_SAME_CELL_INDEPENDENT_IMPLEMENTATIONS_PASS / EXTERNAL_DIFFERENT_CELL_I1_PENDING
claim_ceiling: NO_GENERAL_MATHEMATICAL_NOVELTY / NO_UNIVERSAL_FINITE_M_BAYES_MINIMAX / NO_HARDWARE / NO_PHYSICAL_NASH / NO_NATIVE_DTC0A / BW_PENDING / NO_CANON / NO_EXEC_SIGN
---

# Geeky-S13 ROT024 — Ostry koszt referencji przy całkowitym aliasie danych roboczych; maksimum Hellingera oraz kontrprzykład przeciw skończeniepróbkowej uniwersalności

## 0. Nowe pytanie i rozstrzygnięcie

ROT023 zamknął GLOBALNE minimum Hellingera w **innym** kontrakcie — ten sam Q w dwóch porównywanych możliwych światach, ale nieznane eta_A,eta_B∈[0,.004], z dowolną ilością Q-reference; uzyskał KONIECZNE liczby odczytów ROBOCZYCH. ROT024 bada komplementarny i precyzyjnie inny kontrakt ROT019: **eta jest ZNANE i stałe; Q jest nieznaną wartością parametru zakłócającego i może BYĆ INNE w dwóch alternatywnych możliwych światach**; w każdym osobnym świecie Q to samo dla roboczych i jego własnych prób referencyjnych.

NOWY WYNIK 1: dla eta≥delta/(1+delta), istnieją Q_A,Q_B dające IDEALNIE IDENTYCZNE, IID pełne odczyty robocze. Wszystkie takie pary mają dTV(Q_A,Q_B)=c=(1-eta)delta/eta. Dokładne największe możliwe powinowactwo Hellingera ich praw referencyjnych jest osiągalne i wynosi sqrt(1−c²).

NOWY WYNIK 2: uzyskujemy źródłowo wyznaczoną **KONIECZNĄ** liczbę niezależnych obserwacji referencyjnych m, niezależnie od n (n nawet nieskończone) i od testu. Dla eta=.1: m≥7879 dla >95%, m≥15319 dla >99%. Dla eta=.5: ≥638254 oraz ≥1240943. To NIE są wystarczające budżety dowolnego Q.

NOWY WYNIK 3 (krytyczny falsyfikator): para maksymalizująca Hellingera nie musi być najtrudniejsza pod względem dokładnego błędu Bayesa przy skończonym m. Przy eta=.01,m=3 istnieje legalna niesymetryczna para o większym błędzie niż para symetryczna, certyfikowana IV80. Wobec tego NIE claimujemy globalnego optymalnego NP budżetu referencji.

## 1. Źródła, rzeczywiste odczyty, pierwszeństwo i prior art

- **M13 FIRST**: oryginalny publiczny pomocniczy kod źródłowy B na torusie N=41, <https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py>, blob Git `c6377cfbc9a0070abc34ffedc5871e719f6a4679`. ROT024 NIE uruchamia oryginalnego programu M13. Pełny historyczny runtime DTC0a nie jest tym programem.
- **Geeky-S12 ROT038 FIRST**: oryginalny dla linii NASH syntetyczny model anizotropowej, racjonalnej stacjonarnej kowariancji Gaussowskiej A/B, Git blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`, <https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s12/2026-11-21/IW_GEEKY_S12_ROT038_ORIGINAL_M13_ANISOTROPIC_DIRECTIONAL_EXACT_ALIAS_ONE_BOUNDARY_PROBE_ESCAPE_AND_NONGAUSSIAN_DEPENDENCE_001_20261121.md>.
- **Geeky-S13 ROT016 FIRST**: geometryczne odbicie x oryginalnego B, cztery hipotetyczne równoczesne lokalne RAW kanały i dokładna redukcja do dwóch Cauchy'ego; pinned Git blob `cddc2636249e9bf032fff4de78afb30481401f9a`.
- **Geeky-S13 ROT018 FIRST**: dokładne dTV źródłowego pełnego Cauchy'ego, Huber/TV progi, Git blob `a7c4d7514fc1aa17a0b49c1c0a73d772ca8cf4ff`.
- **Geeky-S13 ROT019 FIRST**: zjawisko aliasu nieznanego Q przy ZNANYM eta i konstrukcja referencji Q-only, Git blob `b3b0eaf5389adf6fe1831d68b8aa29ad9fa699f7`. ROT024 nie przypisuje sobie tego aliasu.
- **Geeky-S13 ROT023 FIRST**: GLOBALNE minimum Hellingera dla SAME-Q w porównywanych możliwych światach przy NIEZNANYM eta, Git blob `23d72f95df580daaf52572aa7568ce7611fb5a9b`. ROT024 to INNY kwantyfikator/eksperyment.
- Klasyczna teoria odpornego testowania: P. Huber (1965), *A Robust Version of the Probability Ratio Test*, Ann. Math. Stat. 36:1753–1758; Huber (1964) *Robust Estimation of a Location Parameter*, doi:10.1214/aoms/1177703732. Standardowa zależność TV–affinity, np. J. Watrous *The Theory of Quantum Information*, Thm 3.33 (wersja klasyczna bezpośrednio z Cauchy–Schwarz), <https://cs.uwaterloo.ca/~watrous/TQI/TQI.double.pdf>. Wyraźnie NIE twierdzimy ogólnego pierwszeństwa tych nierówności, rozkładów najmniej korzystnych ani testów dwumianowych. Literatura przejrzana na poziomie dostępnej strony/fragmentu źródła, bez deklaracji globalnego przeszukania prior art.

Założenia EMPIRYCZNE pozostają NIEDOWIEDZIONE: rzeczywiste cztery niezależnie dostępne surowe kanały, wspólny gain, Gaussowskie i niezależne w czasie lokalne zaburzenia energii, faktyczna obserwowalność rozkładu awarii Q i proporcji eta. Całe zadanie dotyczy **HIPOTETYCZNEGO** modelu źródłowego N41 z ROT038, NIE oryginalnego nonlinear RMS tensora ani wykrycia nowej fizyki.

## 2. Źródłowe dokładne prawo T i jego rozkład Jordana

Źródłowe dwa rozkłady pełnego lokalnego niezmiennika T=U/V (ROT016) mają gęstości

`f_X(t)=s_X/[pi*(t^2−2 mu_X t+1)]`, gdzie:

`mu_A=1/84, s_A=sqrt(1−(1/84)^2)`;
`mu_B=4/585, s_B=sqrt(1−(4/585)^2)`.

Przecięcia `f_A=f_B` są dokładnie odwrotne: `rlo≈.00468572514293064682337951522`, `rhi=1/rlo≈213.41413964681644335198567`. Zdarzenie `E={t<rlo}∪{t>rhi}` jest dodatnią częścią `P_B−P_A`. Definiuj

`delta=TV(P_A,P_B)=∫[f_B−f_A]_+ dt`;
`nu_plus(dt)=[f_B−f_A]_+/delta dt`, `nu_minus(dt)=[f_A−f_B]_+/delta dt`.

Oba nu są prawami o **ROZŁĄCZNYCH PODPORACH** E/E^c. Z certyfikatu pełnej Cauchy IV80 (RECOMPUTED from exact source, no input from previous δ):

`delta∈[0.00161306893774156262143183006772713694452928280538462486081643570649024645255974606787, 0.001613068937741562621431830067727136944529282805384624860816435706490246452562582973337]`.

## 3. Alias wszystkich obserwacji roboczych pod A/B, lecz nie alias referencji

Przy ZNANYM i tym samym udziale eta∈(0,1):

`R_A=(1−eta)P_A+eta Q_A`;
`R_B=(1−eta)P_B+eta Q_B`.

W każdym z dwóch porównywanych możliwych światów źródłowe Q jest JEDNYM ustalonym rozkładem, wspólnym dla tego świata i jego kanału referencyjnego. Ponieważ Q jest nieznanym parametrem, wartości Q_A i Q_B między tymi światami mogą się różnić. To kontrakt ROT019, NIE kontrakt ROT020–023 wymagający tego samego Q w obu porównywanych światach.

R_A=R_B dokładnie wtedy, gdy jako miary podpisane

`Q_A−Q_B=((1−eta)/eta)(P_B−P_A)=c*(nu_plus−nu_minus)`,

z `c=((1−eta)/eta)*delta`. Istnienie dwóch praw Q_A,Q_B wymaga c≤1, czyli `eta≥eta_H=delta/(1+delta)≈0.0016104711367757` — próg ROT018/019, NIE nowy wynik ROT024.

Równość miar dowodzi jednocześnie, że **KAŻDA** taka para aliasująca ma `TV(Q_A,Q_B)=c` (nie jest to tylko słabsze ograniczenie), natomiast wszystkie n odczytów roboczych mają tę samą całkowitą dystrybucję, także przy n→∞.

## 4. Dokładne maksimum affinity dla dopuszczonych referencji

Definiuj powinowactwo `rho(P,Q)=∫sqrt(dP dQ)`. Klasyczna nierówność Cauchy'ego–Schwarza daje

`TV(P,Q)≤sqrt(1−rho(P,Q)^2)`.

Skoro TV(Q_A,Q_B)=c, każda aliasująca para spełnia `rho(Q_A,Q_B)≤sqrt(1−c²)`.

**Konstrukcja osiągająca:**

`Q_A†=((1+c)/2)*nu_plus + ((1−c)/2)*nu_minus`,

`Q_B†=((1−c)/2)*nu_plus + ((1+c)/2)*nu_minus`.

Współczynniki są nieujemne i sumują się do 1 dla 0≤c≤1; rozłączne podparcia nu dają dokładnie

`Q_A†−Q_B†=c(nu_plus−nu_minus)`;
`TV(Q_A†,Q_B†)=c`;
`rho(Q_A†,Q_B†)=sqrt(1−c²)`.

Przez to obie pełne mieszanki robocze są identyczne pod A/B, zaś referencja jest **dwuklasowym doświadczeniem binarnym**: po kondycjonowaniu na E lub E^c rozkład samej wartości T jest taki sam pod obydwiema hipotezami. Cała informacja referencyjna skupia się w bicie `1_E(Z)`. A ma prawdopodobieństwo `(1+c)/2`, B ma `(1−c)/2`.

To jest osiągalne maksimum affinity spośród WSZYSTKICH par aliasujących ROBÓCZE prawa przy ustalonym eta, bez dodatkowego ograniczenia rozkładu Q. Dowód jest kombinacją rozkładu Jordana i klasycznej nierówności TV–Hellinger; nie rościmy nowego twierdzenia ogólnego.

## 5. Konieczne próbkowanie referencyjne z IV80

Jeżeli obserwator ma dowolne `n` odczytów roboczych i `m` IID referencyjnych z Q, w skonstruowanej podparze mamy

`rho( R_A^n×(Q_A†)^m, R_B^n×(Q_B†)^m )=(1−c²)^(m/2)`.

Wskutek `TV(P,Q)≤sqrt(1−rho²)` oraz równoprawdopodobnego testowania:

`BayesError_(n,m)≥[1−sqrt(1−(1−c²)^m)]/2`.

**Aby JAKIKOLWIEK test mógł przekroczyć trafność 1−alpha_err** przy równym priorze, warunkiem koniecznym jest

`(1−c²)^m < 4*alpha_err*(1−alpha_err)`, czyli

`m > ln[4*alpha_err*(1−alpha_err)]/ln(1−c²)`.

Niech `m_H=floor[ln(4alpha(1−alpha))/ln(1−c²)]+1`. Obliczenie IV80 potwierdza wszystkie źródłowe całkowite m_H i sprawdza **zarówno m_H−1, jak i m_H**, z kierunkiem nierówności. Są to pierwsze m, których NIE WYKLUCZA ta szczególna dolna granica Bayesa, **NIE liczby wystarczające dla testu i NIE dokładne optimum minimax próbek**.

| Udział eta | c źródłowe | Konieczne m_H >95% | Konieczne m_H >99% | NUMERYCZNE pierwsze m optymalnego testu dla SAMEJ Q† (95%) | NUMERYCZNE pierwsze m dla SAMEJ Q† (99%) |
|---:|---:|---:|---:|---:|---:|
| 0.2% | 0.80492139993304 | **2** | **4** | 3 | 5 |
| 1% | 0.159693824836415 | **65** | **125** | 105 | 209 |
| 10% | 0.0145176204396741 | **7 879** | **15 319** | 12 837 | 25 675 |
| 50% | 0.00161306893774156 | **638 254** | **1 240 943** | 1 039 797 | 2 079 903 |
| 90% | 0.000179229881971285 | **51 698 567** | **100 516 480** | 84 223 575 | 168 472 287 |

Kolumny m_H są certyfikowane IV80. Dwie ostatnie są **diagnostyką SciPy**, a nie niezależną certyfikacją arytmetyczną i nie globalnym minimax Q. Dla wybranych przypadków eta=.002,.01,.1 konkretne progi dwumianowe zostały dodatkowo certyfikowane IV80 (sekcja 6).

Dla porównania: ROT019 oferował w ramach swojego testu w 95% przy eta=.1 referencję m=312706 (z n=3127051 roboczymi), eta=.5 m=6907938, eta=.9 m=393752432. To WYSTARCZAJĄCE, konserwatywne budżety dla określonej konstrukcji; nie przeczą obecnym koniecznym m. Nie porównujemy ich jako cen tej samej optymalnej procedury.

## 6. Dokładny dwumianowy eksperyment Q† i ścisły falsyfikator NP

Dla jawnej Q† pełna próbka referencyjna redukuje się do `K=Σ1_E(Z_i)`. Pod A: `K~Binom(m,p)`; pod B: `K~Binom(m,1−p)`, `p=(1+c)/2>1/2`. Dokładny test Neymana–Pearsona z równymi priorami wybiera A, jeśli K>m/2, B jeśli K<m/2, a przy remisie losuje. Zatem

`BayesErr_m(Q†)=Pr_p[K<m/2]+(1/2) Pr_p[K=m/2]` (drugi składnik tylko dla parzystego m).

Dla m=2k i 2k−1 błędy są identyczne (tożsamość dwumianowa). Dlatego pierwsze m przekraczające dany ścisły próg to liczby nieparzyste. Osobny program IV80 nie aproksymuje normalnie rozkładu: oblicza skończony sumowany ogon dwumianowy metodą kierunkową, odtwarzając dokładny log(n!) lub wykorzystując naprzemienne ograniczenie reszty Stirlinga i dodatnie oszacowanie nieobliczonego ogona geometrycznego. Również `m−2` zostało sprawdzone kierunkowo.

| eta | Cel błędu | PIERWSZE m dla SAMEJ Q† (IV80) | BayesErr(m−2), IV80 | BayesErr(m), IV80 |
|---:|---:|---:|---:|---:|
| 0.2% | 0.05 | 3 | 0.0975393000335 | 0.0266857839238 |
| 0.2% | 0.01 | 5 | 0.0266857839238 | 0.007975059825 |
| 1% | 0.05 | 105 | 0.0510071352663 | 0.0493806716913 |
| 1% | 0.01 | 209 | 0.0102996600659 | 0.00999915063791 |
| 10% | 0.05 | 12 837 | 0.0500009914538 | 0.0499877765235 |
| 10% | 0.01 | 25 675 | 0.0100019696949 | 0.00999955463256 |

**KONTRPRZYKŁAD DLA SKRÓTU 'maksymalna affinity ⇒ globalnie największy BayesErr_m':** Dla eta=.01 źródłowe `c≈0.1596938248364147`, zamiast masy symetrycznej `x_sym=(1+c)/2≈0.5798469124182` weź `x=5/12` i zdefiniuj inne, legalne:

`Q_A(x)=x nu_plus+(1−x)nu_minus`;
`Q_B(x)=(x−c)nu_plus+(1−x+c)nu_minus`.

Nadal `R_A=R_B` (DALEJ alias roboczy), ale Q-reference ma inną pozycję pary Bernoulliego. IV80 sprawdza k=0,1 jako obszar preferujący B i k=2,3 jako preferujący A, zatem błąd dla m=3 to dokładna suma czterech elementów (nie przybliżenie). Niezależna algebra SymPy daje w tym przedziale źródłowym:

`BayesErr3(x_sym)=(c−1)^2(c+2)/4`;
`BayesErr3(5/12)=(48c^3+12c²−35c+24)/48`;

`BayesErr3(5/12)−BayesErr3(x_sym)=c(6c+1)^2/48 >0`.

Ścisłe IV80:

- symetryczna Q†: `BayesErr3 ∈ [0.3812477640515603709117330687932590809714622325227666184150331760906391753322123157128, 0.3812477640515603709117330687932590809714622325227666184150331760906391753329203323622]`;
- niesymetryczna Q(x=5/12): `BayesErr3 ∈ [0.3940046461949874055606926679602181368727490390564551133332331692962679973542301102263, 0.3940046461949874055606926679602181368727490390564551133332331692962679973544466306317]`.

To FALSYFIKUJE rozciągnięcie Hellinger-maksimum na *każde skończone m*. Nie dowodzi też, że x=5/12 jest globalnym najtrudniejszym wyborem dla m=3; jest jedynie wystarczającym ścisłym kontrprzykładem.

## 7. Rzeczywiste obliczenia, niezależne kontrole i bramki falsyfikacji

Programy wykonane na aktualnej, literalnie wyprowadzonej z poprzednich źródeł parze Cauchy'ego:

1. `rot024_primary_iv80.py`: kierunkowe `mpmath.iv.dps=80`, obliczenie dwóch punktów przecięcia gęstości ze źródłowych racjonalnych mu, δ i eta_H, pięć c i afiniczności, 10 par progów m_H oraz obustronny znak przy m_H−1 i m_H; sześć binomialnych punktów n/n−2 metodą skończonej sumy z konserwatywnym otoczeniem Stirlinga; ścisły 3-próbkowy kontrprzykład.
2. `rot024_independent_scipy.py`: napisany oddzielnie, źródłowe gęstości i pełna całka różnicy po całej osi, numeryczne kontrole jawnych QA/QB oraz integralnej afiniczności, SciPy binom CDF i testy progu dla pięciu eta; to diagnoza same-cell, NIE IV80 ani I1.
3. `rot024_independent_symbolic.py`: niezależna algebra SymPy potwierdzająca równość R_A−R_B dokładnie i dodatni czynnik `c(6c+1)^2/48`; tożsamość i kontrprzykład skończeniepróbkowy.
4. `rot024_semantic_guard.py`: niezależne kontrole źródłowych parametrów, warunku całkowitej równości roboczych miar i wniosków m_H/bayesa, bez polegania wyłącznie na sumach SHA.

Pełny pakiet weryfikujemy przez ZIP CRC/full members, manifest SHA-256, ponowne uruchomienie trzech programów w izolowanym katalogu Python -I, bajtowe porównanie generowanych JSON i kontrolne zmiany naukowych wartości (z ponownie obliczonymi SHA).

## 8. Granice i zadanie dla innej komórki I1

- To eksperyment o **nieznanym Q w dwóch porównywanych możliwych światach** i ZNANYM eta, nie zaś ROT020–023, w których Q miało identyczną wartość w obu światach. Nie wolno przenosić wyników pomiędzy tymi kwantyfikatorami.
- Model Hubera jest egzogeniczny; jeśli Q dobierane jest po obejrzeniu obecnego surowego odczytu, nie korzystamy z tego dowodu.
- BayesError liczony przy równych priorach. Warunek konieczny dla *obu* błędów <alpha wynika stąd, ale dolna granica średniego ryzyka nie jest odpowiednikiem precyzyjnego wymiarowania m dla obu błędów.
- Wynik IV80 pierwszego m dotyczy wyłącznie podanej nierówności Hellingera; certyfikowany binomialny m dotyczy wyłącznie JAWNEJ pary Q†. Kontrprzykład m=3 zabrania nadawania im globalnego statusu NP.
- Rejestr fałszywych uproszczeń: FM-PREMISE-ETA-SWAP; FM-UNKNOWN-Q-EQUAL-ACROSS-WORLDS; FM-HELLINGER-AS-NP-MINIMAX; FM-REPLAY-AS-DIFFERENT-CELL-I1; FM-SYNTHETIC-AS-PHYSICS.
- Przekazanie do AUD3/REC14/M16: niezależnie odtworzyć δ z oryginalnego ROT038 i geometrii ROT016, dystrybucyjną rozkład Jordana i limit rho, sześć IV80 binomialnych znaków, ścisły m3 kontrprzykład; zbadać, czy można zidentyfikować rzeczywiste źródło Q i udział eta. Ograniczenie NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE, brak niezależnego I1 i potwierdzenia native BW.

## 9. Werdykt

`AUTHOR_SIGNED_MEASURE_ALIAS_PROOF_PASS / AUTHOR_REFERENCE_HELLINGER_MAX_PASS / IV80_NECESSARY_M_PASS / IV80_SELECTED_SYMMETRIC_NP_PASS / FINITE_M_NONUNIVERSALITY_FALSIFIER_PASS / SAME_CELL_SCIPY_SYMPY_PASS / EXTERNAL_DIFFERENT_CELL_I1_PENDING / BW_INGEST_PENDING / NO_GENERAL_NOVELTY / NO_HARDWARE / NO_CANON / NO_EXEC_SIGN`.
