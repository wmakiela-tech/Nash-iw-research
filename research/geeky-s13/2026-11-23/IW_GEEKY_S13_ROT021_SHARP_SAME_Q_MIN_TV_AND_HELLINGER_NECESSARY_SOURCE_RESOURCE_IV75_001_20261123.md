---
artifact_id: IW_GEEKY_S13_ROT021_SHARP_SAME_Q_MIN_TV_AND_HELLINGER_NECESSARY_SOURCE_RESOURCE_IV75_001_20261123
return_id: IW_GEEKY_S13_ROT021_SHARP_COMMON_Q_COMPOSITE_MINIMUM_TV_AND_NECESSARY_N_WITH_INFINITE_FAULT_REFERENCE_001_20261123
origin: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-23 Europe/Warsaw
exposure: PUBLIC
scope: SOURCE_TYPED_ROT016_FOUR_MIRROR_CAUCHY_AND_ROT020_UNKNOWN_ETA_WITH_COMMON_FAULT_REFERENCE_SYNTHETIC_GAUSSIAN
status: AUTHOR_EXACT_MEASURE_PROOF_PASS / DIRECTED_IV75_CAUCHY_CHI2_HELLINGER_NECESSARY_CERT_PASS / INDEPENDENT_SAME_CELL_THETA_SCIPY_AND_DISCRETE_LP_PASS / DIFFERENT_CELL_I1_PENDING
claim_ceiling: NO_GENERAL_MATHEMATICAL_NOVELTY / NO_HISTORICAL_DTC0A_RUNTIME / NO_PHYSICAL_RAW_SENSOR / NO_CANON / NO_EXEC_SIGN / BW_PENDING
---

# Geeky-S13 ROT021 — najmniej odległe dwa światy z tym samym Q; ścisłe konieczne koszty pomiarowe nawet z idealną referencją

## 0. Pytanie, nowość względem własnych wyników i status

W ROT020 po raz pierwszy w tej linii dowiedziono ostrej granicy pełnego aliasu dla NIEZNANEGO udziału awarii eta∈[0,h] i tego SAMEGO, obserwowanego także referencyjnie Q: h*=1-589/sqrt(350455) ≈0.00505479226916489366. Przy h=1/250=0.004<h* ustalono dodatnie źródłowe separacje dwóch przedziałów oraz ostrożną wystarczającą gwarancję poprawności >95% z n=496 000 000 roboczych i m=12 500 000 odczytów fault-only, a dla >99% n=654 000 000 i m=16 500 000. Były to **górne, wystarczające** budżety dla wybranej konstrukcji; ROT020 nie zawierał dolnej, koniecznej granicy kosztu każdego możliwego testu.

**NOWY WYNIK 1, ostry w całej zadanej klasie:** dokładnie wyznaczamy najmniejszą ODLEGŁOŚĆ TV dwóch pełnych praw obserwacji roboczych, przy dowolnym Q WSPÓLNYM dla obu możliwych światów i eta_A,eta_B∈[0,h]. Nowy dowód wykazuje, że optimum globalne jest osiągane przy krańcowych udziałach awarii 0 i h; najmniej korzystny Q jest jawnie wyrażony przez ujemną część źródłowej miary podpisanej. Źródłowe liczby integralne gamma_± pochodziły już z ROT020 jako separacje dwóch sentinel-bins — nie są raportowane jako nowe FIRST wartości. Nowością względem ROT020 jest ich **dokładna interpretacja jako GLOBALNEGO MINIMAX TV i świadek osiągnięcia**.

**NOWY WYNIK 2, konieczny koszt informacji:** dla tego jawnego, dopuszczalnego Q* obliczamy źródłową skierowaną IV75 całkę chi-kwadrat dwóch pełnych gęstości, bez numerycznej kwadratury, oraz analityczną dolną granicę ich afiniczności Hellingera. Stąd KAŻDY możliwy test — także widzący cały ciągły T i DOWOLNIE WIELE referencyjnych próbek Q* — nie może uzyskać średniej trafności >95% przed n=41 560 213 obserwacjami roboczymi, ani >99% przed n=80 804 683. **Są to konieczne granice, nie wystarczające liczby próbek ani ostre globalne progi optymalnego NP testu.**

**Zakres krytyczny:** to jedynie hipotetyczne cztery jednoczesne RAW scalar site readings, dokładna x-reflection source m_alpha i syntetyczne gaussowskie kowariancje Geeky-S12 ROT038. Nie ma zweryfikowanej aparatury, fizycznego sygnału NASH, historycznego pełnego DTC0a runtime, ani różno-komórkowego I1 dla nowego ROT021. Ogólna teoria least-favorable measures, robust binary testing, Hellingera i TV jest klasyczna; źródłowa specjalizacja N41 nie uzasadnia claimu ogólnej nowości.

## 1. Źródła, rzeczywista ekspozycja i pierwszeństwo

**M13 FIRST** — oryginalny pomocniczy Fourier/TT B: `research/m13/2026-10-24/verify_m13_rot33_interval.py` @ `30d8549b822ecec4d6939b01dbd1e76a98495f09`, blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`, rzeczywiście ponownie odczytany poprzez GitHub; nie wykonano tego kodu native w ROT021. Geeky-S12 ROT038 pierwszy dostarczył źródłowe RACJONALNE syntetyczne anizotropowe Gaussian covariance A/B, blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`, rzeczywiście bezpośrednio odczytany.

Geeky-S13 ROT016 FIRST x-reflection M13 B i cztery hipotetyczne czujniki z dwoma dokładnymi Cauchy laws, blob `cddc2636249e9bf032fff4de78afb30481401f9a`. Geeky-S13 ROT018 FIRST pełne source TV dwóch czystych Cauchy, Huber/TV alias, blob `a7c4d7514fc1aa17a0b49c1c0a73d772ca8cf4ff`. Geeky-S13 ROT019 FIRST oddzielna Q-reference eksperymentalna ścieżka przy ZNANYM eta, blob `b3b0eaf5389adf6fe1831d68b8aa29ad9fa699f7`. Geeky-S13 ROT020 FIRST ostre unknown-eta full joint-law alias przy TYM SAMYM Q i dwie sentinel-bins dla eta≤.004, blob `1bf7856bc7658d223fa552b7df0c948603510b9e` — źródło to **rzeczywiście ponownie odczytano z przypiętego commitu**.

Klasyczne hosty/prior art: Huber–Strassen composite robust testing; przegląd metod najmniej korzystnych miar: https://www.ism.ac.jp/editsec/aism/pdf/036_2_0251.pdf ; współczesne badanie próbkowania dla skażeń: https://arxiv.org/abs/2605.24741 (Vallinayagam, Pensia, Jog, 2026); kompozytowe testy pomiarowe: https://pmc.ncbi.nlm.nih.gov/articles/PMC7514172/ . To kontekst metodologiczny, nie oryginalne twierdzenia NASH.

## 2. Dokładny eksperyment, wspólność Q i kwantyfikatory

W dwóch porównywanych światach dane robocze mają prawa

`R_A=(1-eta_A)P_A+eta_A Q`, `R_B=(1-eta_B)P_B+eta_B Q`,

gdzie `eta_A,eta_B∈[0,h]`, `h=1/250`, a **Q jest TEN SAM jako miara w obu światach**, a ponadto z Q można pobierać niezależne odczyty referencyjne. Q jest niezależne od pojedynczego poprawnego T przy wyborze gałęzi skażenia; nie ma post-selection TV z ROT018. `P_A,P_B` to pełne hipotetyczne, czyste Cauchy:

`a=1/84`, `b=4/585`, `s_a=sqrt(1-a²)`, `s_b=sqrt(1-b²)`,
`f_A(t)=s_a/[pi(t²-2at+1)]`, `f_B(t)=s_b/[pi(t²-2bt+1)]`.

Wynik dotyczy n niezależnych odczytów roboczych i m niezależnych odczytów Q, **nie** adaptacyjnych skażeń po obejrzeniu T. Model dopuszcza eta=0 i nadal odrębny eksperyment referencyjny fault-only Q; gdy mechanizm fizyczny nie umożliwia tego, wymagany jest nowy kontrakt.

## 3. NOWY OSTRY MINIMAX TV dla identycznego Q — pełny dowód

Niech `[S]_+`, `[S]_-` oznaczają dodatnią i ujemną część podpisanej miary. Jeśli `eta_A>=eta_B`, połóż `d=eta_A-eta_B>=0` oraz

`S=(1-eta_A)P_A-(1-eta_B)P_B`, tak że `S(ℝ)=-d`.

Dla KAŻDEJ miary prawdopodobieństwa Q:

`TV(R_A,R_B)=TV(S+dQ,0) >= S_+(ℝ)`,

bo na dodatniej części S dodanie nieujemnej miary dQ nie może usunąć istniejącej masy dodatniej, a całkowita masa S+dQ wynosi zero. Ta dolna granica jest OSIĄGANA przez

`Q=S_-/(d+S_+(ℝ))`,

ponieważ `S_-(ℝ)=d+S_+(ℝ)`; wtedy

`S+dQ = S_+ - [S_+(ℝ)/(d+S_+(ℝ))] S_-`.

Zatem minimum TV po Q wynosi dokładnie `S_+(ℝ)`. Jeśli przypadkowo d=0, Q znika, a wynik nadal jest równy TV((1-eta)P_A,(1-eta)P_B), bez dzielenia przez d.

Dalej dla 0≤eta_B≤eta_A≤h mamy **nierówność miar punkt po punkcie**

`(1-eta_A)f_A-(1-eta_B)f_B >= (1-h)f_A-f_B`, 

bo różnica to `(h-eta_A)f_A+eta_B f_B>=0`. Stąd najniższe S_+(ℝ) w tej gałęzi otrzymujemy przy `eta_A=h,eta_B=0`:

`gamma_A=integral [ (1-h)f_A-f_B ]_+ dt`.

Dla odwrotnego porządku eta_B>=eta_A analogicznie optymalna para to `eta_B=h,eta_A=0`, a wynik `gamma_B=integral [ (1-h)f_B-f_A ]_+ dt`.

**TWIERDZENIE ROT021:**

`inf_{eta_A,eta_B∈[0,h], Q wspólne} TV(R_A,R_B)=min(gamma_A,gamma_B)`.

Jest to ścisły OSTRY wynik dla PEŁNYCH rozkładów roboczych. Przy dowolnej liczbie m obserwacji Q, porównywane światy mają IDENTYCZNE prawo marginalne referencji, dlatego minimalna one-snapshot TV pełnego rozkładu łącznego również wynosi ten sam wynik. **Nie** oznacza to globalnej optymalności liczby próbek n+m — do tego potrzeba innej funkcji odległości dla miar produktowych.

### Osiągający, jawny rozkład Q*

Przy `eta_A=h,eta_B=0` oznacz `S(t)=(1-h)f_A(t)-f_B(t)`, `gamma=∫S_+`. Wówczas

`q_*(t)=[f_B(t)-(1-h)f_A(t)]_+/(h+gamma)`.

Jest gęstością normalizowaną: `∫S_-=h+gamma`. W obu światach referencja pozostaje dokładnie `Q*`. W pracy porównujemy `R_A=(1-h)P_A+h Q*` z `R_B=P_B`. Ich różnica gęstości wynosi

`r_A-f_B = S_+ - [gamma/(h+gamma)] S_-`,

zatem TV **dokładnie** gamma, a nie tylko ≤gamma. Odrębny, symetryczny świadek uzyskujemy po zamianie A/B. NIE importujemy rozkładu z ROT020 h*=0.005054..., który dotyczył pełnego zlania praw przy INNYM h.

## 4. Certyfikat TV z Cauchy IV75 i brak fałszywej symetrii

Dodatnia część S jest podparta na przedziale `(u,v)`, gdzie

`[(1-h)s_a-s_b](t²+1)+2[s_b a-(1-h)s_a b]t>0`.

IV75 certyfikuje `u=0.49420908467577088108...`, `v=2.02343508245312118041...`; drugie odwrócone zadanie ma dodatnią część na `(-2.0529929048447786444...,-0.4870937437923621812...)`. Oryginalne liczby γ jako sentinel-gaps wystąpiły już w ROT020. Tutaj autorski podstawowy program NIE używa plików wynikowych ROT020, tylko dokładnych racjonalnych a,b, mpmath.iv.dps75, dwóch pierwiastków kwadratu i oryginalnej Cauchy CDF:

`F_X(t)=1/2+(1/pi)atan2(t-mu_X,s_X)`.

Ostry globalny minimax TV jest zawarty w ścisłym skierowanym przedziale

`gamma_min ∈ [0.000146684095399580402770409829998390264237119928696895977083519427099393458039, 0.000146684095399580402770409829998390264237119928696895977083519427099393693773]`.

Oba osobne γ źródłowo zgadzają się w 75-cyfrowej precyzji, ale raport **nie deklaruje ich matematycznej równości** bez osobnego dowodu izomorfizmu. Gwarantuje `min(gamma_A,gamma_B)` przez obustronne przedziały. Niezależny, inaczej napisany SciPy z podstawieniem `theta=atan(T)` potwierdził oba γ z błędem <2e−14; dyskretna optymalizacja liniowa po Q w 160 równych bins θ potwierdziła w 10 przypadkach krańcowe eta, ale jest wyłącznie diagnostyką, a nie dowodem minimax na ciągłych rozkładach.

## 5. NOWE całkowanie chi-kwadrat i ścisła granica Hellingera bez obcinania ogonów

Wybieramy jawny kontrprzykład `eta_A=h, eta_B=0, Q=Q*`. Niech `λ=gamma/(h+gamma)`. W obszarze E=(u,v), gdzie S>0, `r_A-f_B=S`; poza E mamy `r_A-f_B=λ S` z S<0. Dokładnie zatem

`chi²(R_A || P_B)=I_+ + λ² I_-`,

`I_+=∫_E S²/f_B dt`, `I_-=∫_{E^c} S²/f_B dt`.

Korzystamy z **analitycznej** całki wymiernej, a nie metody Monte Carlo:

`S²/f_B = (1-h)² f_A²/f_B - 2(1-h)f_A + f_B`.

Dla źródłowych Cauchy (s_a²=1-a², s_b²=1-b²):

`∫_R f_A²/f_B dt = (1-ab)/(s_a s_b)`.

Co więcej, używając `w=t-a`, `D=w²+s_a²` i `theta=atan2(w,s_a)`, otrzymujemy pierwotną dla `f_A²/f_B`:

`K(t) = [s_a²/(pi*s_b)] * { theta/s_a + 2(a-b)[-1/(2D) + a(w/(2*s_a²*D)+theta/(2*s_a³))] }`.

Odejmujemy jej granicę przy `t→−∞` i obliczamy K(v)−K(u), wszystkie składniki za pomocą mpmath.iv.dps75. Stąd dokładne przedziały skierowane dla `I_+,I_-` i

`chi²(R_A||P_B) ∈ [1.598130221333546031373747... ×10^-7, 1.598130221333546031373747... ×10^-7]`,

wraz z rozróżnialnymi pełnymi granicami IV w pliku `ROT021_PRIMARY_IV75.json`. Niezależne `scipy.integrate.quad` w kącie θ potwierdza `1.59813022133357 ×10^-7` i bezpośrednią afiniczność Hellingera `rho≈0.9999999800297989` (DIAGNOSTYKA NUMERYCZNA, nie certyfikat IV).

Dla `x(t)=r_A(t)/f_B(t)-1` zachodzi `∫f_B x=0` i *ścieżkowo punktowo* ścisła dolna granica `x>=-β`, gdzie

`M = sqrt(350455)/589`,
`β= [gamma/(h+gamma)] * [1-(1-h)/M]`.

Źródłowo β≈`0.0003195874467452348`, więc β<1. Dokładna tożsamość

`1 - sqrt(1+x) + x/2 = x² / [2(1+sqrt(1+x))²]`

implikuje, po całkowaniu i zniknięciu liniowego terminu,

`1-rho(R_A,P_B) <= chi²(R_A||P_B) / [2(1+sqrt(1-β))²] =: Hupper`.

Rzeczywiście wykonany IV75 daje

`Hupper ∈ [1.997982054414813033415349862527... ×10^-8, 1.997982054414813033415349862527... ×10^-8]`.

To PRAWIDŁOWA, skierowana **górna granica Hellinger-one-minus-affinity**, nie estymator numeryczny rho. Jej szerokość i wszystkie cyfry są w JSON.

## 6. NOWE konieczne granice n, niezależne od liczby odczytów fault-only

Dla dowolnej liczby n IID odczytów roboczych i m IID odczytów Q* (m nieograniczone), w porównywanych najmniej korzystnych światach referencja Q* jest IDENTYCZNA. Zatem afiniczność Hellingera pełnych danych wynosi

`rho_joint = rho(R_A,P_B)^n * rho(Q*,Q*)^m = rho(R_A,P_B)^n`.

Z nierówności `TV(P,Q) <= sqrt(1-rho(P,Q)^2)` i ścisłego rho>=1−Hupper:

`BayesError(n,m) >= [1-sqrt(1-(1-Hupper)^(2n))]/2`,

przy równych a priori 1/2. Ta dolna granica obowiązuje DLA KAŻDEGO TESTU pełnego ciągłego T i pełnej, nieograniczonej referencji Q*. Rozstrzyga także niemożliwość równoczesnego błędu obu hipotez <e, bo oznaczałoby to średni błąd <e.

Warunek konieczny, by w ogóle MÓC osiągnąć średnią trafność >`1-e` w tym eksperymencie, to

`n > log(4e(1-e)) / [2 log(1-Hupper)]`.

Wszystkie wartości n i n−1 były skierowanie sprawdzone IV75 przy dwóch e:

| Cel | Każdy n nie większy niż | Konieczne n co najmniej | Dolna granica błędu Bayesa przy odcięciu |
|---|---:|---:|---:|
| **>95%** | **41,560,212** | **41,560,213** | `>0.05000000185553` |
| **>99%** | **80,804,682** | **80,804,683** | `>0.01000000037873` |

W rzeczywistym statystycznym eksperymencie n może potrzebować ZNACZNIE WIĘCEJ próbek: wyprowadzona liczba jest TYLKO NECESSARY, a nie poziomem poprawności NP dla tej pary. Źródłowy ROT020 podaje dla odrębnego, uniwersalnego dwuzdarzeniowego testu SUFFICIENT n=496 mln (z m=12.5 mln) dla 95% i n=654 mln (m=16.5 mln) dla 99%. **Nie należy mylić kierunków nierówności**. Obie bramki są spójne, pozostawiając lukę ilościową do niezależnego audytu i ewentualnej optymalizacji testu.

## 7. Rzeczywiście wykonane niezależne obliczenia i falsyfikatory

1. `rot021_primary_exact_iv75.py`: bez dostępu do liczb z ROT020, skierowane exact rational a,b i h=1/250, źródłowe przekroczenia Cauchy, gamma_A/B, analityczne K-CDF i chi², dokładny limit β, Hellinger oraz dwa n/n−1, plik `ROT021_PRIMARY_IV75.json`. Nie wykonuje oryginalnego M13.
2. `rot021_independent_theta_scipy.py`: osobny kod w innej parametryzacji, zastępuje `t` przez `theta=arctan t`, uzyskuje źródłowe gęstości `dP/dtheta=s/[pi(1-mu*sin(2theta))]`, liczy dwa plus-regions i q* przez bezpośrednią numeryczną kwadraturę, dokładną normalizację, TV, chi², rzeczywistą afiniczność. `ROT021_INDEPENDENT_THETA_SCIPY.json`.
3. `rot021_independent_discrete_lp.py`: kolejny napisany od zera program dyskretyzuje obie miary na 160 równych bins θ, buduje program LINIOWY minimalizujący TV po pełnym wektorze Q przy dziesięciu parach (etaA,etaB), a nie tylko odtwarza formułę świadków. `ROT021_INDEPENDENT_DISCRETE_LP.json`. Ponieważ discretization decreases TV, wartości grid są diagnostycznie nieco NIŻSZE niż ścisła gamma; nie wolno wykorzystywać ich jako dokładnego certyfikatu.
4. `rot021_integrity_guard.py` oraz `rot021_cold_replay.py` weryfikują SHA-256 i tożsamość matematycznych tez i mutacyjne testy z rzeczywistymi zmienionymi plikami, mimo przeliczenia sum. Archiwum zamyka pełen raport, poprzedni oryginalny ROT020 i manifest. Są to wszystkie programy SAME CELL, nie independent different-cell I1.

## 8. Nieprzenoszalność i następna bramka

- ROT021 nie stwierdza, że istnieją cztery rzeczywiste RAW site sensors M13 ani źródłowy, IID gaussowski szum A/B. Nie odnosi się do sześciu oryginalnych masek, rzeczywistych tensorowych RMS, ani fizyki NASH; historyczny kompletny `dtc0a_runtime_v0_3_1.py` pozostaje niedostępny.
- Q* jest TAKĄ SAMĄ miarą w obu porównywanych możliwych światach; różni się eta: h vs 0. Q* jest gęstością nierównomierną, z wyciętym przedziałem (u,v), a nie testem fizycznej wiarygodności awarii czujnika. Jeżeli Q musi mieć dodatnią wszędzie, analityczną lub ograniczoną wariancję aparaturową, optimum może się zmienić.
- Ustalono globalnie najniższe TV **jednej** obserwacji; świadek może, lecz NIE MUSI minimalizować globalnego Hellingera/KL i ryzyka dla n produktów. Dlatego liczby n w §6 są rzetelnymi granicami koniecznymi, nie ostrym rozwiązaniem minimax testu całego modelu.
- Twierdzenie dla `m=∞` wymaga, aby Q było referencyjnie dostępne mimo braku skażenia w jednym świecie (`eta_B=0`). Jeżeli żaden fault-only stream nie istnieje przy eta=0, konieczne jest sformułowanie odmiennego eksperymentu i ponowienie bramki.
- Rozwój syntetycznych progów bez ustalenia oryginalnego operatora pomiaru i fault-only channel ma ograniczoną wartość naukową; nie zachodzi upgrade dowodów do GR/TPE/GW czy obserwacji rzeczywistych.

**Zlecenie ograniczonego I1 do AUD3 / REC14 / M16:** zweryfikować (i) dowód wariacyjny minimum nad wspólnym Q, (ii) dokładną Cauchy K-prymitywną i przedziały chi², (iii) przejście do afiniczności Hellingera oraz nierówność min-sample, (iv) rolę niezależnych od n danych referencyjnych Q*, (v) źródłowe założenia A/B i no-physical. Nie przyznawać nowego ogólnego pierwszeństwa.

**Claim status:** `AUTHOR_EXACT_COMMON_Q_MINIMAX_TV_PASS / AUTHOR_DIRECTED_IV75_HELLINGER_NECESSARY_N_PASS / SAME_CELL_THETA_SCIPY_AND_DISCRETE_LP_PASS / EXTERNAL_DIFFERENT_CELL_I1_PENDING / BW_INGEST_PENDING / NO_GENERAL_NOVELTY / NO_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN`.
