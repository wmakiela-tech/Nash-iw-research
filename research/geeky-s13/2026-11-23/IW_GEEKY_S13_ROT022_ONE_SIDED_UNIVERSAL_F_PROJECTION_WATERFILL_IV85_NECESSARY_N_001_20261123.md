---
artifact_id: IW_GEEKY_S13_ROT022_ONE_SIDED_UNIVERSAL_F_PROJECTION_WATERFILL_IV85_NECESSARY_N_001_20261123
return_id: IW_GEEKY_S13_ROT022_SOURCE_CAUCHY_UNIVERSAL_ONE_SIDED_F_DIVERGENCE_PROJECTION_SHARP_TV_AND_STRONGER_HELLINGER_NECESSARY_RESOURCE_001_20261123
origin_cell: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
record_date: 2026-11-23 Europe/Warsaw
exposure: PUBLIC
source_type: ORIGINAL_M13_N41_FOURIER_B_AUXILIARY_CONTEXT / ROT038_SYNTHETIC_GAUSSIAN_A_B / ROT016_FOUR_MIRROR_RATIO_CAUCHY / ROT020_UNKNOWN_ETA_COMMON_Q_REFERENCE
status: AUTHOR_ANALYTIC_PROJECTION_PROOF_PASS / IV85_CERTIFIED / SAME_CELL_SCIPY_AND_DISCRETE_SLSQP_PASS / DIFFERENT_CELL_I1_PENDING
claim_ceiling: NO_GENERAL_MATHEMATICAL_NOVELTY / NO_GLOBAL_ALL_ETA_HELLINGER_MINIMAX / NO_NATIVE_ORIGINAL_M13_ROT022 / NO_HISTORICAL_FULL_DTC0A / NO_ACTUAL_RAW_SENSORS / BW_PENDING / NO_CANON / NO_EXEC_SIGN
---

# Geeky-S13 ROT022 — wspólny rozkład najmniej korzystny dla dywergencji wypukłych: ostrzejszy dolny koszt statystyczny poniżej progu aliasu

## 0. Pytanie naukowe, odpowiedź i zastrzeżenie pierwszeństwa

ROT020 udowodnił, że przy nieznanych udziałach skażenia `eta_A,eta_B∈[0,1/250]`, ze **wspólnym** rozkładem awarii `Q` dostępnym w niezależnym kanale referencyjnym, obie syntetyczne hipotezy Cauchy pozostają identyfikowalne. ROT021 wyznaczył **globalnie ostre minimum pojedynczopróbkowej TV** i jawnego świadka, a następnie uzyskał *konieczne* progi liczby roboczych próbek `41,560,213` (ponad 95%) i `80,804,683` (ponad 99%) przez konserwatywny Hellinger. ROT021 wyraźnie NIE twierdził, że jego rozkład minimalizujący TV jest najmniej korzystny dla Hellingera.

**Wynik ROT022:** dla pary BRZEGOWEJ `eta_A=h=1/250`, `eta_B=0`, konstruujemy inny wspólny `Q†`, którego prawo robocze jest **jedyną projekcją minimalizującą jednocześnie wszystkie różniczkowalne, ściśle wypukłe f-dywergencje względem `P_B`**. Konkretnie zmniejsza chi-kwadrat z `1.5981302213333546e−7` (świadek TV ROT021) do **`1.5143123202035386819052807e−7`**, czyli o **5.2447478942%**. Poprzez nowy, ścisły IV85 bound Hellingera zaostrza kontrprzykład zasobowy do **`n≥43,863,484` dla >95%** oraz **`n≥85,282,886` dla >99%**, przy dowolnie dużej niezależnej referencji Q†. To +2,303,271 i +4,478,203 *koniecznych* odczytów roboczych względem wcześniejszego wystarczającego do uzyskania dolnej granicy kontrprzykładu ROT021. Nie są to ani progi wystarczające, ani ostre globalne minima n.

**Ograniczenie najważniejsze:** optymalność dowodzona jest dla USTALONEJ konfiguracji `eta_A=h, eta_B=0`. Nie udowodniono globalnego minimum Hellingera po jednoczesnej swobodnej zmianie obu `eta_A,eta_B`. Konstrukcja jest jednak dopuszczalnym świadkiem w pełnej rodzinie ROT020, zatem dolna granica próbek obowiązuje dla **każdego testu mającego działać jednostajnie na pełnej rodzinie**.

### Źródła, prior art i pierwszeństwo

1. **M13 FIRST**: publiczne oryginalne pomocnicze źródło rzadkiego fourierowskiego tensora B, N41, `research/m13/2026-10-24/verify_m13_rot33_interval.py`, commit `30d8549b822ecec4d6939b01dbd1e76a98495f09`, blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`. Materiał źródłowy został uprzednio bezpośrednio przeczytany; tego historycznego modułu **nie uruchomiono natywnie w ROT022**.
2. **Geeky-S12 ROT038 FIRST**: dwie dokładne racjonalne, dodatnio określone, ale **SYNTETYCZNE** anizotropowe stacjonarne kowariancje skalarnego szumu przestrzennego A/B, blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`.
3. **Geeky-S13 ROT016 FIRST**: geometryczne cztery idealne czujniki odbite x i dokładny iloraz Cauchy'ego przy syntetycznych szumach, blob `cddc2636249e9bf032fff4de78afb30481401f9a`. ROT018 FIRST exact full-law TV, ROT019 reference Q known eta, ROT020 sharp unknown-eta same-Q alias plus two sentinels, ROT021 FIRST global minTV plus Hellinger resource bound, blob `37c7d58640958ab23d2b45e08dc4314b6fbd9a7a`.
4. **Dojrzałe wcześniejsze ujęcie**: Fauß i Zoubir, *Old Bands, New Tracks—Revisiting the Band Model for Robust Hypothesis Testing*, arXiv:1510.04524, https://arxiv.org/abs/1510.04524 (2015; DOI 10.1109/TSP.2016.2600505), z mechanizmem najmniej korzystnych gęstości w modelu pasmowym. Klasyczne: Huber (1965) oraz Huber–Strassen (1973). ROT022 nie rości sobie nowości ogólnego „water filling”, f-projekcji lub teorii least-favorable density.

## 1. Oryginalnie typowany eksperyment syntetyczny

Zachowujemy wyłącznie dystrybucje po hipotetycznym obserwatorze czteropunktowym:

`P_A=Cauchy(mu_A=1/84, s_A=sqrt(1-(1/84)^2))`,

`P_B=Cauchy(mu_B=4/585, s_B=sqrt(1-(4/585)^2))`,

`f_X(t)=s_X/[pi*(t²−2 mu_X t+1)]`.

W obrębie ROT020 rozważane są dopuszczalne światy:

`R_A=(1-eta_A)P_A+eta_A Q`, `R_B=(1-eta_B)P_B+eta_B Q`, gdzie `eta_A,eta_B∈[0,h]`, `h=1/250=.004`, a `Q` jest TEN SAM w obu światach, także w referencji. Wybieramy legalną podparę `eta_A=h`, `eta_B=0`, ale nie narzucamy jej rzeczywistym instrumentom.

Niech `a(t)=(1-h) f_A(t)`, `p(t)=f_B(t)`. Każdy dopuszczalny roboczy rozkład A w tej podparze ma gęstość `r=a+hq`, czyli `r>=a`, `∫r=1`. Drugi roboczy rozkład to p.

## 2. Twierdzenie o uniwersalnej wypukłej projekcji w tej podparze

Istnieje dokładnie jedna `c∈(0,1)` spełniająca

`∫_R max{a(t), c p(t)} dt=1`.

Połóż

`r†(t)=max{a(t),c p(t)}`;

`q†(t)=[r†(t)-a(t)]/h = [c f_B(t)-(1-h)f_A(t)]_+/h`.

Ponieważ `r†>=a`, a `∫r†=1`, q† jest nieujemną unormowaną gęstością. Jest to rzeczywisty, wspólny Q† pod A i B; niezależne próbki referencyjne pochodzą z Q† także w świecie B, mimo że w tym świecie `eta_B=0`.

**Twierdzenie (bounded/source-conditioned):** dla każdej różniczkowalnej, ściśle wypukłej funkcji `phi:(0,infinity)->R` minimum `∫ p(t) phi(r(t)/p(t)) dt` po wszystkich `r>=a, ∫r=1` osiąga **jednoznacznie** to samo `r†`. Obejmuje chi-kwadrat, KL, reverse-KL, Hellinger² i inne wypukłe dywergencje typu f. Dla TV (niedyferencjowalna phi) r† nadal realizuje globalne minimum TV w tej podparze, ale świadek nie musi być jednoznaczny.

**Dowód bez odwołania do eksperymentu numerycznego.** Niech `z=r/p`, `z†=r†/p=max(a/p,c)`. Z nierówności stycznej do phi:

`∫ p[phi(z)-phi(z†)] >= ∫ p phi'(z†)(z-z†)`.

Po odjęciu `phi'(c)*∫p(z-z†)=0` prawostronna całka redukuje się do obszaru aktywnego `a/p>c`:

`∫_{a/p>c} p[phi'(a/p)-phi'(c)](z-a/p) >=0`, bo `z>=a/p`, a phi' jest rosnąca. Przy ścisłej wypukłości równość zachodzi tylko dla z=z† prawie wszędzie. Unikalność c: funkcja normalizacji jest ciągła, rosnąca, przy c=0 ma całkę `1-h`, a przy c=1 ma całkę `1+gamma_A>1`, oraz na właściwym przedziale jest ściśle rosnąca. **To tylko projekcja wobec ustalonego czystego p i jednej skażonej strony.**

Ostra TV pozostaje identyczna jak ROT021: `TV(R†,P_B)=gamma_A=∫[(1-h)f_A-f_B]_+`. Powód: `r†-p>0` wtedy i tylko wtedy gdy `a-p>0`; w pozostałych punktach `c<1`, więc r†<=p. Jednak poprzedni TV-witness ROT021 ma większe chi² i Hellinger; TV sama nie wystarcza do identyfikacji statystycznie najbardziej podobnej pary.

## 3. Źródłowa normalizacja c: dokładny warunek i certyfikat IV85

`f_B/f_A` jest ilorazem kwadratowych funkcji t o jednostkowych wyrazach stałych. Równanie przejścia `(1-h)f_A=c f_B` ma dwa dodatnie pierwiastki, których iloczyn wynosi dokładnie 1. Region wiążący `I_c={t:(1-h)f_A(t)>c f_B(t)}` jest pojedynczym przedziałem `(u_c,v_c)`.

Warunek normalizacji jest skalarny i w pełni obliczalny przez funkcje CDF Cauchy'ego:

`c+(1-h)[F_A(v_c)-F_A(u_c)]-c[F_B(v_c)-F_B(u_c)]=1`.

Program `rot022_primary_waterfill_iv85.py`, rzeczywiście wykonany z mpmath.iv.dps=85 i dokładnymi racjonalnymi współczynnikami źródłowymi, metodą kierunkowej bisekcji uzyskał:

`c∈(0.99981230570814221153193686448878995972622654400120056881642316, 0.99981230570814221153193686448878995972622654400120056881642317)`;

`u_c≈0.45866100778143287769`, `v_c≈2.18025945749574822263`, `u_c*v_c=1` dokładnie.

Nie wykorzystano wyników TV wczytanych z ROT021, by odnaleźć c; nowszy program liczy oba świadki z dokładnych czystych parametrów Cauchy'ego.

## 4. Obliczenie chi², bez obcięcia ogonów, i poprawa wobec ROT021

Z uwagi na `r†=a` na I_c i `r†=c p` poza nim, dokładnie

`chi²(R†||P_B) = ∫_{I_c} [(1-h)f_A-f_B]^2/f_B dt + (1-c)^2 P_B(I_c^c)`.

Pierwsza całka redukuje się do trzech całek CDF:

`(1-h)^2∫_{I_c} f_A²/f_B -2(1-h)P_A(I_c)+P_B(I_c)`.

Całka `f_A²/f_B` ma elementarną funkcję pierwotną z arctan i funkcją wymierną, taką jak w skrypcie źródłowym ROT021. IV85 obejmuje tą metodą CAŁĄ prostą rzeczywistą, bez numerycznego obcinania dalekich ogonów Cauchy'ego. Otrzymujemy:

- `chi²(R†||P_B) ∈ [1.5143123202035386819052806559893,1.5143123202035386819052806559894]e-7`;
- `chi²(R_TV||P_B) ∈ [1.5981302213335460313737471412536,1.5981302213335460313737471412537]e-7` — poprzedni dopuszczalny TV-witness niezależnie odtworzony;
- redukcja `(chi²_TV−chi²_†)/chi²_TV ≈ 0.05244747894202653`, tj. **5.2447478942%**.

Niezależna (wewnątrz komórki) implementacja w zmiennej kątowej `theta=arctan t` z rozcięciem całek na trzy gładkie przedziały daje `chi²≈1.5143123202039247e-7` (diagnostyczne zaokrąglenie w SciPy), c≈0.9998123057081421 i Hellinger deficit≈`1.8922198749785772e-8`. Są one spójne z kierunkowym certyfikatem IV85. Dodatkowe trzy niezależne dyskretne optymalizacje SLSQP dla 64 koszyków (chi², KL, Hellinger) zgodziły się co do samej gęstości dyskretnej z błędem L∞ poniżej `3e−10` jednostki masy koszyka — jest to falsyfikator, **nie** dowód ciągły.

## 5. Certyfikowana dolna granica koniecznego n mimo nieskończonej referencji Q†

Niech `x(t)=r†(t)/p(t)-1`. W tej konstrukcji `1+x(t)>=c` dokładnie. Z tożsamości

`1−sqrt(1+x)+x/2 = x²/[2(1+sqrt(1+x))²]`,

oraz `∫p x=0`, wynika dla współczynnika afiniczności Hellingera `rho=∫sqrt(r†p)`:

`1-rho <= chi²(R†||P_B)/[2(1+sqrt(c))²] = H_up`.

Kierunkowy IV85:

`H_up ∈ [1.8930680634578175680339738508217,1.8930680634578175680339738508218]e-8`.

Przy n niezależnych próbkach roboczych i dowolnej liczbie m niezależnych referencji `Q†` pod OBU hipotezami łączna afiniczność równa się **dokładnie** `rho^n *rho(Q†,Q†)^m=rho^n`. Z klasycznego TV–Hellinger:

`BayesError_n >= (1-sqrt(1-rho^(2n)))/2 >= (1-sqrt(1-(1-H_up)^(2n)))/2`.

Autorski IV85 faktycznie sprawdził znaki błędów przy granicach:

| Założony wymagany poziom | Wszystkie n do tej wartości WYKLUCZONE jako wystarczające do przekroczenia celu | Pierwsze n nieodrzucone tą dolną granicą |
|---|---:|---:|
| Trafność >95% | `43,863,483` | **`43,863,484`** |
| Trafność >99% | `85,282,885` | **`85,282,886`** |

W punkcie 43,863,483 otrzymano `BayesError >= 0.0500000007766654...`, a w punkcie 85,282,885 `BayesError >=0.01000000011211146...`, z kierunkowymi otoczkami IV85. Są to *konieczne* budżety dla jakiegokolwiek klasyfikatora mającego działać jednostajnie na pełnej rodzinie modeli, nawet jeśli dostaje nieskończenie wiele obserwacji Q†. Nie są optymalnymi n testu Neymana–Pearsona, ani nawet dowodem globalnej najtrudniejszej pary po wszystkich eta.

W porównaniu z ROT021 (41,560,213 i 80,804,683) poprawa koniecznych n wynosi odpowiednio **+2,303,271** i **+4,478,203**. Równocześnie uzyskany w ROT020 bardzo wysoki budżet **wystarczający** nadal pozostaje obowiązującą wcześniejszą górną konstrukcją; nie ma sprzeczności.

## 6. Próby falsyfikacji i niezależna reprodukcja autorska

**Ścieżka I — IV85:** nowy program podstawowy, exact rational muA/muB, kierunkowa bisekcja jednoznacznego c, dokładne dwa pierwiastki przedziału wiążącego, CDF atan2 i racjonalno-atan pierwotna chi², niższa granica afiniczności oraz sprawdzenie n i n−1. Nie wczytuje wcześniejszego JSON ROT021.

**Ścieżka II — integralna SciPy:** osobno napisany kod w theta=arctan t, własne rozpoznanie dwóch punktów przecięcia, bezpośrednia kwadratura oddzielonych przedziałów dla c, normalizacji Q†, TV, chi² i nieujemnej postaci deficytu afiniczności Hellingera. Ta ścieżka nie stanowi matematycznego certyfikatu IV.

**Ścieżka III — 64-wymiarowe programowanie nieliniowe:** SLSQP z trzema osobno zapisanymi funkcjami celu dla chi², KL i Hellingera na masach 64 sektorów kąta, przy wspólnych ograniczeniach `R_i >= (1-h) P_A(I_i)`, `ΣR_i=1`. Wszystkie trzy numeryczne optima dają tę samą gęstość dyskretną. Celem jest sfalsyfikowanie uniwersalności projekcji, nie zastąpienie jej dowodu analitycznego.

**Ścieżka IV — świadomie ograniczony audyt globalnej hipotezy:** dodatkowy odrębny 48-koszykowy program SLSQP optymalizuje wspólne Q dla 14 wybranych par `(eta_A,eta_B)`. Najmniejsze wartości wystąpiły na przeciwstawnych krańcach `(0,.004)` lub `(.004,0)`, ale nie przypisujemy temu wyniku pełnej optymalności względem ciągłych eta ani wszystkich rozkładów. Różnicę liczbową obustronnych krańców można wyjaśnić dyskretyzacją i końcową tolerancją obliczenia; nie rozstrzyga ona kierunków w niezdyskretyzowanym eksperymencie.

Sprawdzane kontrprzykłady: inny niż źródłowy parametr mu, błędna wartość c, nieznormalizowane Q†, zawyżona chi², zmienione n, mylna etykieta GLOBAL_MINIMAX i niespójność niezależnej kwadratury. Kontroler porównuje nie tylko sumy SHA-256, lecz także niezależnie obliczone tożsamości naukowe. Raport i oryginalne skrypty w ZIP pozwalają odtworzyć protokół.

## 7. Czego wyniki nie dowodzą

- **Nie** znamy i nie wykonaliśmy historycznego kompletnego runtime `dtc0a_runtime_v0_3_1.py`. Źródło M13 jest pomocniczą implementacją B; nie należy utożsamiać syntetycznego szumu na skalarnej energii z nieliniowymi maskami tensora, oryginalną siatką pomiarową ani pełną fizyką NASH.
- **Nie** wykazaliśmy rzeczywistego istnienia 4 symultanicznych lokalnych czujników RAW ani osobnego trybu eksperymentalnego dostępu do rozkładu awarii Q†.
- **Nie** wykazaliśmy globalnej optymalności Hellingera po obu eta; rozwiązaliśmy dokładnie i ściśle jedną *dopuszczalną podparę*, co jest wystarczające dla dolnej granicy zasobowej całej rodziny.
- **Nie** wykazaliśmy nowości ogólnego rozwiązania f-projekcji; model pasma dolnego i konstrukcje least-favorable mają liczne wcześniejsze źródła.
- **Nie** wolno przenosić koniecznej liczby syntetycznych powtórzeń na czas rzeczywistego eksperymentu ani ogłaszać CANON / EXEC_SIGN / fizycznego odkrycia.

## 8. Zlecenie ograniczone dla niezależnego I1

Adresaci: `AUD3 / REC14 / M16` (nie jest to samoczynne przyjęcie zadania). Priorytet: (a) sprawdzenie dowodu wspólnego f-projektora dla wszystkich różniczkowalnych ściśle wypukłych phi przy jednostronnie skażonej stronie; (b) c monotoniczność i korzenie odwrotne; (c) poprawność elementarnej całki fA²/fB, IV85 i n/n−1; (d) niezależny falsyfikator optymalności globalnej po eta_A,eta_B; (e) rozdzielenie źródłowego syntetycznego Cauchy od rzeczywistych nieliniowych operatorów M13.

**Końcowy status:** `AUTHOR_UNIVERSAL_FIXED_EDGE_F_PROJECTION_PASS / IV85_PASS / SAME_CELL_INDEPENDENT_THETA_AND_SLSQP_PASS / EXTERNAL_I1_PENDING / BW_PENDING / NO_GENERAL_NOVELTY / NO_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN`.
