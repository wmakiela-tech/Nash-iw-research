---
artifact_id: IW_PRF12_R25_AFFINE_T1_AND_FAST_RESET_IDENTIFIABILITY_LIMIT_001_20261102
created_at: 2026-11-02
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R24_ASYMMETRIC_ASSIGNMENT_T1_AND_INTRA_EXPOSURE_RESETS
exposure: PUBLIC
canonical_body_path: research/prf12/2026-11-02/IW_PRF12_R25_AFFINE_T1_AND_FAST_RESET_IDENTIFIABILITY_LIMIT_001_20261102.md
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_AFFINE_CALIBRATION_IDENTITY / CONDITIONAL_HOEFFDING_CERTIFICATE / EXPLICIT_CALIBRATION_ERROR_CONTROL / CAUCHY_FAST_RESET_PROCESS_IDENTIFIABILITY_NO_GO / INDEPENDENT_MATRIX_REPRO_PASS / REFEREE_PENDING
claim_ceiling: NO_HARDWARE / NO_UNRESTRICTED_SINGLE_COPY_THREE_PROBE_LOCC_CLOSURE / NO_UNKNOWN_HARDWARE_T1_DURING_DRIVEN_PULSES / NO_NOVELTY_PRIORITY / NO_CANON / NO_EXEC
---

# PRF12 R25 — Niesymetryczny odczyt, T1 i granica identyfikowalności przy szybkim odświeżaniu Cauchy'ego

**Data:** 2 listopada 2026. **Funkcja:** PRF12. **Rezultat naukowy:** rozdzielono (A) dokładną, skalibrowaną mitygację błędów detektora oraz zachowanie rozróżnialności R23 przy kontrolowanym czasie życia źródła, od (B) matematycznego falsyfikatora identyfikowalności klas: coraz częściej odświeżane niezależne częstotliwości o rozkładzie Cauchy'ego upodabniają proces do źródła Lévy'ego, nawet przy stałym, ograniczonym, niekomutującym sterowaniu. Część B **opuszcza mrożony kontrakt** A z R23/R24 (jedna ξ w obu pełnych odczytach). Nie przenosić między tymi twierdzeniami kwantyfikatorów.

## 0. Provenance, stan wyjściowy i dojrzały gospodarz

Pierwszy właściciel modelu: PRF11 R35. Ścisły dostępny input: PRF12 R23, https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-01/IW_PRF12_R23_SOURCE_INDEX_AND_REPRO_MANIFEST_001_20261101.md , oraz R24, https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-01/IW_PRF12_R24_SOURCE_INDEX_AND_REPRO_MANIFEST_001_20261101.md . Niezmienione środowisko: jeden fizyczny sensor, dwie sekwencyjne destrukcyjne próby na parę, odtwarzanie sensora, wspólne prywatne losowanie osi X/Y/Z z wagami w=(.18,.20,.62), gamma=1, Omega_max=10, Delta=.5, t_pi/2=pi/20, aktywne źródło w przygotowaniu i analizie, końcowa projekcja Z. R23 daje **konserwatywne**, wcześniej zamknięte granice p_A^ideal(same|xi)>=a0=.576 dla każdej stałej xi w parze; p_B^ideal(same)<=b0=.526. Te granice są używane, nie przypisujemy sobie ich nowego dowodu. Fizyczny czas pary i jej hazardowy span z R24: L_pair=1.7783185307179588/gamma, T_pair,worst=1.8283185307179588/gamma.

Dojrzałe źródła zewnętrzne: IBM Quantum, [Measurement error mitigation](https://quantum.cloud.ibm.com/learning/en/courses/tools-for-quantum-advantage/error-mitigation) oraz [M3 readout error mitigation](https://quantum.cloud.ibm.com/docs/en/tutorials/readout-error-mitigation-sampler) — klasyczne macierze assignment i ograniczenia kalibracji; Nielsen & Chuang, *Quantum Computation and Quantum Information*, rozdział 8, model amplitude damping; literatura teorii procesów stabilnych, np. [Cauchy Distribution (LibreTexts)](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_%28Siegrist%29/05%3A_Special_Distributions/5.32%3A_The_Cauchy_Distribution) i [Cauchy Distribution in Information Theory](https://pmc.ncbi.nlm.nih.gov/articles/PMC9955388/). Mitygacja macierzy assignment i stabilność Cauchy'ego to znane metody/własności; R25 nie zgłasza pierwszeństwa.

## 1. Mrożony nowy detektor: T1 po analizie i asymetryczne etykiety

Po KAŻDYM ukończonym impulsie analizy (albo bez impulsu dla Z) czujnik czeka t_d=.05/gamma. Podczas tego oczekiwania: dowolny Hamiltonian proporcjonalny do Z, źródło dephasing Z i DODATKOWO niezależna od źródła relaksacja do |0> z intensywnością Gamma_1=1/T1; brak poprzecznego sterowania. Na końcu idealny projektor Z daje znak U=+ dla |0> i − dla |1>. Niezależny, klasyczny, stabilny kanał assignment zapisuje + jako − z prawdopodobieństwem eta_+, zaś − jako + z prawdopodobieństwem eta_-. Błędy assignment są niezależne dla dwóch odczytów i warunkowo niezależne od źródłowej historii, osi i wcześniejszych zapisów. Pomiary i ponowne przygotowania pozostają idealnie projektorowe; nie symulujemy fizycznej ciągłej integracji impulsu detektora ani T1 w trakcie sterowania. Reset sensora trwa t_r=.05/gamma i daje zawsze stan |0>.

Niech m=Tr(Z rho_pre_det) należy do [-1,1]. Kanał zero-temperaturowego amplitude damping o czasie t_d daje m_d=e^(−Gamma_1 t_d)m+[1−e^(−Gamma_1 t_d)]. Niech alpha=1−eta_+−eta_- oraz beta=eta_-−eta_+. Wtedy dla znaku R **zarejestrowanego**

  E[R|m] = c m+d,
  c=alpha e^(−Gamma_1 t_d),  d=alpha[1−e^(−Gamma_1 t_d)]+beta.     (R25.1)

To tożsamość dokładna, również przy ciągłej dephasingowej fazie Z podczas oczekiwania; Z-populacje są chronione przed tym Hamiltonianem/dephasingiem, ale **nie** przed T1. Wymagamy c≠0 oraz stałej kalibracji c,d. Para próbek może mieć różne parametry c_j,d_j, wówczas skorygować KAŻDĄ osobno. Dalsze liczby przyjmują wspólne c,d. Jeśli c=0, zarejestrowane pojedyncze znaki są niezależne od idealnych wartości m i ten zadeklarowany klasyczny detector nie zawiera żadnej informacji o źródle; żadna postprocessingowa statystyka nie może jej przywrócić.

## 2. Twierdzenie R25.1 — dokładny debias korelacji dwóch wyników

Przy znanych c,d i c≠0 zdefiniuj pojedynczy skorygowany znak t(R)=(R−d)/c, a skorygowany wynik pary

  Y=(1+t(R1)t(R2))/2.                                  (R25.2)

Warunkowo względem dwóch idealnych średnich znaków m1,m2 oraz wspólnej osi, gdy odczyty są niezależne,

  E[Y|m1,m2] = (1+m1 m2)/2.                            (R25.3)

Po losowaniu osi dokładnie otrzymujemy idealną, przed-detektorową statystykę zgodności R23/R24, także dla źródła A z różnymi xi(t) między/WEWNĄTRZ odczytów, o ile ostateczne dwa stany sensora pozostają rozdzielne po niezależnym przygotowaniu (brak kwantowego sprzężenia między próbami). W szczególności dla no-reset pełnej pary E_A Y>=a0=.576, E_B Y<=b0=.526. Korekta oddziela BŁĄD SYSTEMATYCZNY detektora od jego zwiększonej wariancji. **Y nie jest zmienną Bernoulliego** i może przekroczyć [0,1]; niedozwolone jest zastosowanie do niej dokładnego dwumianowego testu R24.

Dla c>0, |d|<1, Y osiąga trzy wartości zależne od znaków (++, --, +/-). Zakres tych wartości ma dokładną szerokość

  W=(1+|d|)/c².                                        (R25.4)

W szczególności dla eta_+=.01, eta_-=.03, Gamma_1/gamma=.5, t_d gamma=.05:

  e^(−Gamma_1 t_d)=0.9753099120283326,
  c=0.9362975155471993, d=0.043702484452800686,
  W=1.1905536622407509.                               (R25.5)

Kontrola niezależna: skrajne Krausy amplitude damping, asymetryczna macierz assignment, pełne sumowanie czterech par zapisanych znaków dla siedmiu wartości xi oraz jedno z dwóch źródeł B potwierdziły R25.1–R25.3 i p_B^ideal=.5252387409109164.

## 3. Twierdzenie R25.2 — resetowe hazardy i skończona próba BEZ iid xi

Rozpatrz proces A, dla którego warunkowo względem dowolnej wcześniejszej historii, bieżącej ukrytej wartości xi, wszystkich innych ukrytych zmiennych mogących wpływać na intensywność resetów oraz wylosowanej osi pomiarowej prawdopodobieństwo **braku zmiany** xi podczas pełnego przedziału pary jest co najmniej s=e^(−lambda L_pair). Wystarcza egzogeniczny zegar Poissona o intensywności lambda niezależny od aktualnej xi, bieżącej osi i historii, z użyciem najdłuższego możliwego czasu pary L_pair. Sam bound Pr(no reset|zaobserwowana przeszłość)>=s NIE wystarcza: selektywny względem bieżącej xi reset może zaburzać wagę średniej po losowanych osiach. Przy braku zmiany korzystamy z a0=.576; przy możliwej zmianie xi w środku impulsu albo ekspozycji używamy tylko bezpiecznego idealnego floor f=0. Jeżeli źródło może się zmienić WYŁĄCZNIE między dwoma kompletnymi odczytami i pozostaje statyczne podczas nich, zachowany analityczny dowód R24 daje f=.31. Dla Y z korekcją detektora zachodzi

  E_A[Y|past]>= a(s,f):=s a0+(1−s)f,
  E_B[Y|past]<=b0.                                     (R25.6)

Nie wolno stosować f=.31 do resetów wewnątrz pojedynczego odczytu. Źródło B ma niezależne przyrosty, a warunkowe E_B Y=b0_actual<=b0. Dowolna zależność xi między parami jest dozwolona, jeśli **warunkowy** hazard pozostaje ważny.

Niech D=a(s,f)−b0>0 i theta=[a(s,f)+b0]/2. Decyzja „A, jeśli średnia z N skorygowanych Y_j >=theta” przy użyciu warunkowej nierówności Hoeffdinga dla ograniczonych różnic martyngałowych daje OBA jednostronne błędy najwyżej

  Pr_A(B), Pr_B(A) <=exp[−N D²/(2W²)].                 (R25.7)

Jest to wystarczająca, a nie optymalna pod względem liczby prób, gwarancja. Dlatego wystarczy

  N=ceil(2W² log(1/alpha)/D²)                          (R25.8)

przy alpha=.05. To NIE jest test dwumianowy, ani dowód optymalnego testu przy nieznanym xi. Przy f=0 warunek D>0 odziedziczony z R24: s a0>b0; przy f=.31, s(a0−.31)+.31>b0.

### Przykłady w tym samym kontrakcie zegara R24

| lambda/gamma | miejsce resetu | dolna E_A Y | górna E_B Y | wystarczająca liczba par N | worst gamma*T_all |
|---:|---|---:|---:|---:|---:|
|0|bez resetów|.576000|.526000|3397|6210.80|
|.01|może także WEWNĄTRZ odczytu|.565847|.526000|5349|9779.68|
|.02|może także WEWNĄTRZ odczytu|.555874|.526000|9516|17398.28|
|.02|WYŁĄCZNIE między pełnymi odczytami|.566706|.526000|5126|9371.96|
|.04|może także WEWNĄTRZ odczytu|.536451|.526000|77756|142162.74|

Wiersze pokazują CIĘŻAR pewnej mitygacji; nie dowodzą, że surowy, poprawnie skalibrowany odczyt lub lepszy test nie mogą zużyć mniej pomiarów. Czas detekcji t_d i resetu t_r jest uwzględniony; nie doliczono nieudokumentowanego czasu przygotowania lub fizycznego czasu integracji pomiaru ponad zadeklarowany t_d.

### Stabilność przy niedokładnej kalibracji

Gdy szacujemy chat,dhat i dopuszczamy |c−chat|<=delta_c, |d−dhat|<=delta_d, definiujemy epsilon=(delta_c+delta_d)/|chat|. Wówczas każdy skorygowany znak spełnia |E[t_hat|m]−m|<=epsilon, a dla warunkowo niezależnych odczytów

 |E[Y_hat|m1,m2]−(1+m1m2)/2| <= epsilon+epsilon²/2=:b_cal.  (R25.9)

Należy więc zastąpić dolną granicę A przez a(s,f)−b_cal, górną B przez b0+b_cal, próg przez połowę tych liczb i W przez (1+|dhat|)/chat². Dla lambda/gamma=.02, f=0, delta_c=delta_d=.0005, chat=c,dhat=d: D_uncertain=.0277365861, N=11039. To kontrola deterministycznego błędu kalibracji; nie dowodzi, że dany zbiór próbek kalibracyjnych osiągnął owe delta-parametry z zadanym poziomem ufności.

## 4. Twierdzenie R25.3 — NEGATYWNY kontrakt: bardzo szybkie Cauchy resety są nierozróżnialne od Lévy B

**Uwaga typowania źródeł:** w tej sekcji rozpatrujemy A_h NIEBĘDĄCE statycznym źródłem A z R23. Dzielimy T na komórki długości h, w każdej trzymamy jedną częstotliwość xi_k~Cauchy(0,gamma), niezależną między kolejnymi komórkami. Marginalny rozkład xi(t) w każdej chwili jest Cauchy(0,gamma); czas życia xi wynosi co najwyżej h. B pozostaje dokładnym symetrycznym procesem Cauchy–Lévy o generatorze dephasingu D_gamma=(gamma/2)(Ad_Z−Id).

**R25.3a (dokładna równość, sterowanie na granicach komórek).** Charakterystyczna Cauchy'ego to E exp(i xi_k h)=exp(−gamma h). Zatem uśredniony kanał jednego swobodnego odcinka ma EXACTLY postać exp(h D_gamma). Niezależność xi_k daje EXACT zgodność całego dyskretnego procesu A_h i B na punktach siatki. Dowolne unitarne SWAP/pomiary wykonane natychmiast na granicach siatki i inne jawne kanały sprzęgane na tych samych granicach zachowują tę równość. Nie ma pomiaru potrafiącego rozróżnić dwa identyczne kanały.

**R25.3b (niekomutujące, OGRANICZONE sterowanie w trakcie komórek).** Niech na każdej komórce H_c będzie stałym, deterministycznym Hamiltonianem sterowania (dowolny skończony wymiar sensora i pamięci) o normie operatorowej <=Hmax, z szumem xi Z_S/2. Niech

 Phi_A,h = E_xi Ad_exp[−ih(H_c+xi Z_S/2)],
 Phi_B,h = exp[h(C_c+D_gamma)], C_c=−i ad(H_c).

Duhamel i niezmienniczość normy operatorowej przy sprzężeniach unitarnych dają warunkowo względem xi

 ||exp[−ih(H_c+xi Z/2)]−exp(−ihH_c)exp(−ihxi Z/2)||op
 <=min{h² |xi| Hmax/2, 2h Hmax}.

Następnie odległość diamond kanałów sprzężeń unitarnych jest <=2 razy normę operatorową różnicy unitarnych, więc

 ||Phi_A,h − Ad_exp(−ihH_c) o exp(h D_gamma)||diamond
 <= h Hmax E[min(h|xi|,4)].

Dla z=gamma h i dowolnego a>0:

 J_a(z)=E[min(h|xi|,a)]=(z/pi)ln[1+(a/z)²]+(2a/pi) arctan(z/a).

Komutator kontrola–szum spełnia ||[C_c,D_gamma]||diamond<=4 gamma Hmax, a standardowy wzór całkowy błędu Lie–Trottera między kanałami kontraktywnymi w diamond daje

 ||Ad_exp(−ihH_c) o exp(h D_gamma)−exp[h(C_c+D_gamma)]||diamond
 <=2 gamma Hmax h².

Sumowanie n=T/h komórek (oraz tych samych deterministycznych segmentów sterowania dopasowanych do siatki) daje

 \boxed{ ||Phi_A,h^(T)−Phi_B^(T)||diamond
 <= min{2, T Hmax [J_4(gamma h)+2gamma h]}. }   (R25.10)

Przy gamma,T,Hmax stałych: J_4(z)=O[z log(1/z)], więc prawa strona ->0. Równość dokładna w R25.3a NIE jest twierdzeniem dla skończonego h i ciągle aktywnego, niekomutującego Hamiltonianu; wtedy uzyskujemy tylko konwergencję normową. Wystarczy, że rozważana sekwencja komórek rafinuje skończony ustalony zestaw zmian H_c(t); nie ma twierdzenia dla sterowań rosnących jak 1/h albo dowolnie szybkiego adaptacyjnego feedbacku.

**Statystyczny skutek:** przy ustalonej skończonej liczbie N niezależnych powtórzeń protokołu z ustalonym Hmax,T, dystans śladowy jego wyników nie przewyższa sumy N powyższych granic kanału. Wyrównana średnia minimalnego błędu binarnego jest >=1/2−N eps(h)/4, gdzie eps(h) oznacza prawą stronę R25.10. Dlatego bez dodatniej informacji o minimalnym czasie współdzielenia xi źródła A_h można uczynić nierozróżnialnymi od B dla dowolnego stałego budżetu N,T,Hmax. To NIE obejmuje dynamicznie zwiększanego N(h),T(h),Hmax(h) ani starego mrożonego A ze stałym xi przez całą parę.

Przykładowe górne granice R25.10 przy gamma=T=1 i Hmax=5: h=.02 daje 0.600964; h=.001 daje 0.039584; h=.0001 daje 0.004691; h=.00001 daje 0.000542. Są to bezpieczne oszacowania (czasami bardzo luźne), a nie odległości rzeczywiste.

## 5. Niezależność falsyfikatorów i zakres dowodu

1. **Przesunięcie assignment** (eta_+ !=eta_-): zwykłe mnożenie kontrastu przez (1−2eta)² jest błędne; trzeba usuwać przesunięcie d lub osobno uwzględnić wyrazy liniowe.
2. **T1 podczas analizy/sterowania poprzecznego:** m_d=e^(−Gamma t_d)m+... nie opisuje pełnego kanału; R25 nie dowodzi jego korekcji.
3. **Korelacje odczytów:** niezależność dwóch klasycznych kanałów assignment i detektorowego T1 jest istotna dla mnożenia E[t1t2]; wspólny klasyczny dryf może dać nieusuwalny składnik kowariancji.
4. **Kalibracja bliska osobliwości:** gdy c zbliża się do zera, W=(1+|d|)/c² diverguje, a liczba wymaganych prób N ~W²/D² może rosnąć jak c^(−4). Przy c=0 w ogóle nie ma informacji w odczytanych bitach w tym kanale.
5. **Poisson tylko w sensie marginalnym albo tylko względem zaobserwowanej historii:** to NIE wystarcza. Konieczna jest dolna granica przeżycia również przy warunkowaniu na bieżącą xi, ustawienie osi i inne istotne zmienne ukryte, lub egzogeniczny zegar resetów niezależny od nich; inaczej nie wolno użyć a(s,f) z R25.6 ani testu R25.7.
6. **Wariant A_h z szybkimi resetami:** nie jest to kontrprzykład dla twierdzenia R23 o JEDNEJ xi na całą parę, lecz niezależny „information boundary” dla szerszej rodziny procesów.
7. **Nieustalone zasoby:** realny czas odczytu Z, leakage, bit-flip przez inne mechanizmy, pomyłka ponownego przygotowania, zmienność eta+/eta− z osią i widmem źródła oraz kalibracja empiryczna NIE są zweryfikowane.
8. **Nie wolno utożsamiać** żadnego wyniku R25 z nierozstrzygniętym domknięciem pełnego LOCC dla oryginalnego pojedynczego bloku trzech kubitów.

## 6. Reproducibility, custody i niezależny referee

Skrócone formuły i przykłady wprost odtwarza jeden plik Python 3+NumPy+SciPy: `IW_PRF12_R25_AFFINE_READOUT_T1_FAST_RESET_REPRO_001_20261102.py`. Drugi samodzielny skrypt `IW_PRF12_R25_INDEPENDENT_2X2_4X4_KRAUS_AUDIT_001_20261102.py` nie importuje pierwszego i sprawdza układ 2×2 A, generator Lindblada 4×4 B, dokładny kanał T1 Krausa, klasę asymetrycznych assignment, wszystkie kombinacje dwóch końcowych zapisanych bitów, a J4 dodatkowo przez niezależne całkowanie. Stan `PASS`, lecz brak formalnej arytmetyki przedziałowej dla wszystkich zmiennoprzecinkowych obliczeń i brak niezależnego zewnętrznego referee.

Osobna kontrola dowodu R25.10: poprosić DS/Grok/AInstein o przejście po stałych komutatora w normie diamond, o jawne źródłowe typowanie A_h≠A_static, o test rzeczywistego feedbacku i o sprawdzenie, czy błędy kalibracyjne zostały ujęte jako zakres parametryczny, a nie nieudowodniona empiryczna dokładność pomiaru. BW-ingest i niezależny review NIEPOTWIERDZONE.

RETURN: PRF12_R25 / ASYMMETRIC_READOUT_T1_AFFINE_INVERSION / EXACT_TWO_SHOT_DEBIASED_CORRELATION / CONDITIONAL_HOEFFDING_SOURCE_HAZARD_CERT / EXPLICIT_CALIBRATION_UNCERTAINTY / CAUCHY_STABLE_FAST_RESET_NO_IDENTIFIABILITY_AT_FIXED_RESOURCES / NUMPY_SCIPY_INDEPENDENT_MATRIX_PASS / REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / ORIGINAL_3Q_SINGLE_COPY_LOCC_CLOSURE_OPEN / GITHUB_PENDING_BW_INGEST.
