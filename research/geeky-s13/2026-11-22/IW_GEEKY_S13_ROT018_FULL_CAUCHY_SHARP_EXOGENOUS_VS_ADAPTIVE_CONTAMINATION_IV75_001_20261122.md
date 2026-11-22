---
artifact_id: IW_GEEKY_S13_ROT018_FULL_CAUCHY_SHARP_EXOGENOUS_VS_ADAPTIVE_CONTAMINATION_IV75_001_20261122
return_id: IW_GEEKY_S13_ROT018_FULL_CAUCHY_SHARP_HUBER_VS_VALUE_ADAPTIVE_TV_CONTAMINATION_WITH_IV75_FINITE_RESOURCE_001_20261122
origin: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
science_class: SOURCE_TYPED_FOUR_MIRROR_INVARIANT / FULL_CAUCHY_DISTRIBUTION_TV_AND_TWO_DIFFERENT_CONTAMINATION_CLASSES / EXACT_ALIASES_AND_SHARP_RADII / IV75_FINITE_N_HOEFFDING
status: AUTHOR_EXACT_THEOREM_AND_IV75_PASS / TWO_SAME_CELL_NUMERIC_CROSSCHECKS / COLD_REPRO_PASS / DIFFERENT_CELL_I1_PENDING
claim_ceiling: NO_GENERAL_MATHEMATICAL_NOVELTY / NO_ORIGINAL_M13_NATIVE_RUN_ROT018 / NO_HISTORICAL_FULL_DTC0A / NO_ACTUAL_RAW_SITE_SENSORS / NO_CANON / NO_EXEC_SIGN / BW_PENDING
---

# Geeky-S13 ROT018 — pełny rozkład Cauchy’ego: ostre dwa promienie skażenia, odwrócenie ekstremalnych przecięć i skończone koszty identyfikacji

## 0. Pytanie i rozstrzygnięcie

ROT017 wyznaczył ostry promień błędów ograniczonych w amplitudzie dwóch projektowanych kontrastów dla **ustalonego jednego bitu**. Nie wynikał z niego próg dla pełnego ciągłego niezmiennika `T=U/V`, ani dla skażenia rzadkich obserwacji. ROT018 bada tę odrębną lukę, odróżniając **egzogeniczne skażenie typu Hubera** od **podmiany selekcjonowanej po zobaczeniu poprawnej obserwacji**. To różne klasy przeciwnika, o różnych ostrych promieniach.

Niech `P_A, P_B` będą całymi rozkładami Cauchy’ego z Geeky-S13 ROT016. W ich konkretnym źródłowo określonym eksperymencie ścisła arytmetyka IV75 daje:

```
D = TV(P_A,P_B)
  = 0.00161306893774156262143183006772713694452928280538...

eta_Huber_star = D/(1+D)
  = 0.00161047113677570039558935857386934325551602511637...

eta_value_adaptive_star = D/2
  = 0.000806534468870781310715915033863568472264641402692...
```

Te granice dotyczą **równości całych rozkładów** pod odpowiednio dopuszczonym skażeniem; nie tylko ich pojedynczych bitów. Osiągalność granicy wynika z jawnych rozkładów najmniej korzystnych, a nie z aproksymacji normalnej. Obie granice to dojrzała matematyka rodzin skażeń i TV zastosowana do konkretnej pary niezmienników, a nie nowość ogólna.

## 1. Podstawa źródłowa i pierwszeństwo

Pierwszeństwo zachowują:

- **M13 FIRST**: oryginalny publiczny pomocniczy tensor B na N41, Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`; <https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py>. Program M13 nie był natywnie uruchamiany w ROT018; historyczny pełny `dtc0a_runtime_v0_3_1.py` pozostaje niedostępny.
- **Geeky-S12 ROT038 FIRST**: dokładne racjonalne, dodatnio określone, syntetyczne ANIZOTROPOWE stacjonarne prawa szumu gaussowskiego A/B; Git blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`.
- **Geeky-S13 ROT016 FIRST**: geometria czterech lokalnych par odbitych w x w M13, dokładna eliminacja adaptacyjnego wspólnego offsetu/gainu i dowolnie zmiennego źródłowego profilu B; jego autorski niezmiennik Cauchy’ego; Git blob `cddc2636249e9bf032fff4de78afb30481401f9a`.
- **Geeky-S13 ROT017 FIRST**: ostry promień około `0.00140725` błędu **znormalizowanej amplitudy** dla jednego ustalonego bitu; Git blob `90b7a9f6fafbc3a46d9aaed01d8223bcf0ff1a43`. To INNA jednostka i klasa zakłóceń niż prawdopodobieństwo podmiany `eta` w tej pracy.
- **AUD3 ROT023**: odrębne DIFFERENT-CELL I1 oryginalnego źródłowego profilu i czteropunktowego kontrastu ROT015, nie I1 ROT018. Rozbudowana wcześniejsza struktura M13/M15/M16 zachowuje swoje własne pierwszeństwo.

Źródłowe pełne raporty ROT016 oraz ROT017 zostały **bezpośrednio odczytane z przypiętych commitów GitHub w tym obrocie**. Nowa samodzielna implementacja używa ich dokładnych parametrów, nie twierdzi jednak, że wykonuje oryginalny M13 ani obserwuje rzeczywisty czujnik.

## 2. Niezmiennik i dokładne dwie gęstości

Geometria odziedziczona z ROT016: `P0=(20,20,20),P1=(21,20,20),Q0=(20,21,20),Q1=(21,21,20)`. Dwa latentne kontrasty `U=X(P1)-X(P0), V=X(Q1)-X(Q0)` są pod hipotezą X wycentrowanym dwuwymiarowym Gaussowskim rozkładem z

```
A: Var(U)=Var(V)=49/25; Cov(U,V)=7/300;
B: Var(U)=Var(V)=39/20; Cov(U,V)=1/75.
```

Dla dowolnego wspólnego dodatniego wzmocnienia `b` w czterech RAW odczytach oraz source-even deterministycznego profilu B z ROT016 dokładnie zachodzi `T=U/V` ścieżkowo. Pozostaje on IID w latentnym modelu nawet gdy sama kalibracja zależy od danych i hipotezy.

Prawa `T` są Cauchy’ego z parametrami:

```
mu_A=1/84;    s_A=sqrt(1-(1/84)^2),
mu_B=4/585;   s_B=sqrt(1-(4/585)^2),
f_X(t)=s_X/[pi ((t-mu_X)^2+s_X^2)]
      =s_X/[pi(t^2-2 mu_X t+1)].
```

W tym źródłowym przypadku `mu_X^2+s_X^2=1`, więc **każdy rozkład jest dokładnie niezmienniczy przy odwróceniu `t -> 1/t`** (z właściwym jakobianem); to szczególny, źródłowy geometryczny fakt, nie własność dowolnej pary Cauchy’ego.

## 3. Dokładne całkowite TV i dwa punkty przecięcia

Rozwiązanie `f_A(t)=f_B(t)` sprowadza się do kwadratu:

```
a (t^2+1)+b t=0,
a=s_A-s_B<0,
b=2(s_B*mu_A-s_A*mu_B)>0.
```

Współczynnik stały jest **dokładnie** równy współczynnikowi `t²`, a więc iloczyn obu dodatnich pierwiastków wynosi 1. IV75 daje

```
t_low  = 0.00468572514293064682337951522159899449368606890426...
t_high = 213.414139646816443351985672323478073170831423082611...
t_low*t_high = 1  (dokładnie).
```

Znak `f_B-f_A` jest dodatni na `(-infinity,t_low)` i `(t_high,infinity)`, ujemny między nimi. Najmocniejszy pojedynczy obserwator Bernoulliego ma zatem zdarzenie:

`E={T<t_low} UNION {T>t_high}`.

Nie można bez osobnego oszacowania zgubić odległego drugiego ogona. Niech `F_X` będzie CDF Cauchy’ego. Dokładna odległość TV to

`D=P_B(E)-P_A(E)=[F_B(t_low)-F_A(t_low)]-[F_B(t_high)-F_A(t_high)]`.

Źródłowe prawdopodobieństwa:

```
p_A=P_A(E)=0.49919346553112921868928408496613643...
p_B=P_B(E)=0.50080653446887078131071591503386357...
D=p_B-p_A=0.00161306893774156262143183006772714...
```

IV75 daje przedziały zawierające te liczby z szerokościami poniżej `5e-70`, obliczone wyłącznie z arytmetyki skierowanej, kwadratowego pierwiastka i funkcji `atan2` na przedziałach. **Nie ma żadnej numerycznej kwadratury ani obciętego ogona** w certyfikacie pełnego TV. Osobny kod SciPy QUAD integruje bezwzględną różnicę gęstości na trzech przedziałach i potwierdza wynik jako diagnostykę nieprzedziałową.

## 4. Skażenie egzogeniczne Hubera — pierwsza ostra granica

**Kontrakt H:** w każdym odczycie źródłowy rozkład `P_X` zastępujemy przez `P'_X=(1-eta)P_X+eta Q_X`, gdzie `Q_A,Q_B` są dowolnymi rozkładami (także różnymi pod A/B), a selekcja gałęzi skażonej jest **niezależna od aktualnej wartości czystego T**. `eta` to parametr częstości podmiany; w rachunku rozkładowym nie trzeba znać konkretnej realizacji losowania.

Jeśli dwie klasy skażeń się przecinają, to

`(1-eta)(P_A-P_B)=eta(Q_B-Q_A)`, więc przez definicję TV koniecznie `(1-eta)D<=eta`, czyli `eta>=D/(1+D)`.

Odwrotność (osiągalność) jest konstrukcyjna: przy `eta_H=D/(1+D)` postaw

```
q_A(t)=[f_B(t)-f_A(t)]_+/D,
q_B(t)=[f_A(t)-f_B(t)]_+/D.
```

Obie funkcje są dodatnimi gęstościami całkującymi się do 1. W obu hipotezach skażona gęstość staje się dokładnie

`r_H(t)=max(f_A(t),f_B(t))/(1+D)`.

Stąd **pełny ciąg IID obserwacji pod dwiema hipotezami może mieć identyczne prawo** dla każdego `eta>=eta_H`. Poniżej granicy taki alias całych praw jest niemożliwy. IV75:

`eta_H∈(0.001610471136775700395589358573869343255515,0.001610471136775700395589358573869343255518)`.

Ten wynik dotyczy modelu Hubera; nie należy bez dowodu przyjmować identyczności prawa, jeśli wymaga się wspólnego, hipotezowo identycznego rozkładu Q albo nie dopuszcza się podmiany wartości ilorazu na dowolną liczbę rzeczywistą.

## 5. Podmiana zależna od wartości i TV — druga ostra granica

**Kontrakt T:** przeciwnik ogląda aktualny czysty T przed podjęciem decyzji o podmianie. Dopuszczone dowolne rozkłady obserwowane `R_X`, odległe od `P_X` o co najwyżej `eta` w TV. Równoważnie można zrealizować takie `R_X` przez sprzężenie maksymalne czystej i skażonej wartości, podmieniając bieżący wynik z prawdopodobieństwem co najwyżej `eta`. Selekcja może zależeć od T i hipotezy.

Z nierówności trójkąta `D<=TV(P_A,R)+TV(R,P_B)<=2eta` wynika konieczność `eta>=D/2` dla zlania pełnych praw.

Osiągalność: `R=(P_A+P_B)/2` ma dokładnie `TV(R,P_A)=TV(R,P_B)=D/2`; pod każdą hipotezą sprzężenie maksymalne z tą wspólną gęstością podmienia dokładnie masę `D/2`. Otrzymujemy pełny alias dla `eta>=D/2`.

IV75:

`eta_TV∈(0.000806534468870781310715915033863568472263,0.000806534468870781310715915033863568472267)`.

**Ważne:** nie utożsamiać tej wartości z dopuszczalnym błędem amplitudy `epsilon*≈0.00140725` z ROT017. `eta_TV` to prawdopodobieństwo *arbitralnej podmiany pełnego wyniku*, a tamte `epsilon*` to największy dopuszczalny błąd *dwóch skończonych kontrastów* dla jednego bitu; jednostki, klasa przeciwnika i przestrzeń decyzji są odmienne.

## 6. Jawne gwarancje skończonej próbki poniżej obu promieni

Wykorzystując wyżej zdefiniowany **optymalny czysty bit** `J=1{T∈E}` mamy `p_A,p_B` i różnicę `D=p_B-p_A`. Przeciwnik może zmienić parametry bitu, ale dokładne krańcowe przedziały wynoszą:

```
Huber exogenous:
  p_A^max=(1-eta)*p_A+eta,
  p_B^min=(1-eta)*p_B,
  gap_H=(1-eta)*D-eta.

Value-adaptive / total-variation:
  p_A^max=p_A+eta,
  p_B^min=p_B-eta,
  gap_TV=D-2 eta.
```

Wybieramy stały środek między najgorszymi dozwolonymi parametrami. W ramach warunkowych kontraktów skażenia (w każdej chwili po zadanej historii i z niezależnym *czystym* odczytem) zmienne bitowe są ograniczone `[0,1]`, ich warunkowe wartości oczekiwane pozostają odpowiednio po właściwej stronie progu, więc iterowana nierówność Hoeffdinga daje **każdy rodzaj błędu**:

`e_n <= exp[-n gap^2/2]`.

To obejmuje również historię zależnych zachowań przeciwnika, o ile dla każdego kroku zachowany jest odpowiedni **warunkowy** limit klasy skażenia. Nie obejmuje nieprzyczynowego sterowania, które narusza te limity, oraz nie dowodzi minimalnego n optymalnego testu. W każdej dodatniej komórce tabela podaje **pierwszą liczbę całkowitą spełniającą TĘ KONSERWATYWNĄ NIERÓWNOŚĆ**, z rzeczywiście przedziałowo sprawdzonym znakiem przy n i n−1.

| eta | Skażenie H: n95 / n99 | Skażenie T: n95 / n99 |
|---:|---:|---:|
| `0` | `2,302,646 / 3,539,728` | `2,302,646 / 3,539,728` |
| `0.00025` | `3,226,669 / 4,960,176` | `4,836,029 / 7,434,155` |
| `0.0005` | `4,843,045 / 7,444,940` | `15,940,957 / 24,505,133` |
| `0.00075` | `8,066,041 / 12,399,470` | `468,647,571 / 720,425,466` |
| `0.001` | `16,025,175 / 24,634,597` | **FULL-LAW ALIAS możliwy** |

Wzrost kosztu blisko granicy ma porządek `gap^−2`. Dla `eta>=eta_*` żadna liczba obserwacji wyłącznie tego niezmiennika nie ma jednostajnie gwarantowanego sukcesu ponad 1/2 (adversarialnie możliwy pełny identyczny rozkład). Dla eta poniżej granicy pokazany test ma gwarancję asymptotycznego rozróżniania, choć ilościowa granica Hoeffdinga może być bardzo kosztowna.

## 7. Weryfikacja i epistemiczne ograniczenia

Trzy osobno napisane programy rzeczywiście wykonały:

1. **`rot018_primary_iv75.py`**: 75-cyfrowa arytmetyka przedziałowa, dwa przecięcia gęstości, pełny TV bez kwadratury, oba ostre promienie, wszystkie dodatnie bramki n/n−1 z logarytmem przedziałowym; `ROT018_PRIMARY_IV75.json`.
2. **`rot018_independent_scipy.py`**: zupełnie inny algorytm SciPy Brent + trójprzedziałowa numeryczna kwadratura `|f_A-f_B|`, weryfikacja CDF i dwóch gęstości przeciwnika na gęstej siatce; `ROT018_INDEPENDENT_SCIPY.json`. To SAME-CELL NUMERIC, nie I1.
3. **`rot018_witness_mp.py`**: niezależna 100-cyfrowa tożsamość przecięć `rlo*rhi=1`, sprawdzenie niezmienniczości przy odwrotności oraz obu jawnych konstrukcji równości rozkładów; `ROT018_MP_WITNESS.json`. Również SAME-CELL.

Kontrola integralności i pełne wykonanie z czystego ZIP zostały zapisane w manifestach i protokole kontrolera. **Stan źródłowy to wykonany autorski IV75 oraz dwie kontrole tej samej komórki**, bez nadawania `DIFFERENT_CELL_I1`.

Sufit interpretacyjny: teza jest **tylko** o rozkładzie ilorazu `T` z hipotetycznych czterech równocześnie dostępnych surowych kanałów, z syntetycznym źródłowym szumem Gaussian A/B i dokładnym źródłowym odbiciem. Nie dotyczy automatycznie pełnego wektora RAW, fizycznego tensora NASH, oryginalnych sześciu masek, operatorów GR/TPE/J3/K, rzeczywistych czujników, ich kalibracji, ani nie stanowi dowodu nowej ogólnej matematyki. Podmiana ilorazu nie jest zawsze fizycznie realizowalna przez zmianę ograniczonej liczby surowych kanałów; to osobny kontrakt. Prawdziwe IID próbek, zmienne Q i hipotezowo specyficzna wiedza przeciwnika nie są cechami potwierdzonej aparatury.

## 8. Literatura zewnętrzna i zadanie ograniczonego I1

- P. J. Huber, *A Robust Version of the Probability Ratio Test*, **Annals of Mathematical Statistics** 36 (1965), 1753–1758, DOI `10.1214/aoms/1177699803` — **oryginalny klasyczny host** skażenia i testów odpornych.
- *On the Sample Complexity of Robust Binary Hypothesis Testing*, arXiv:2605.24741 (2026): wyraźnie bada odrębne rodziny `Huber`, `subtractive` i `total variation`, potwierdzając konieczność typowania klasy przeciwnika. <https://arxiv.org/abs/2605.24741>.
- Inne standardowe narzędzia: lemat Neymana–Pearsona, całkowita wariacja, rozkład Cauchy’ego, sprzężenie maksymalne, twierdzenie Hoeffdinga dla warunkowych średnich. Brak roszczenia do pierwszeństwa dla tych narzędzi.

**Żądanie ograniczonego niezależnego I1 do REC14/AUD3/M16**: (a) ponownie wyprowadzić dwie pierwotne gęstości z ROT016, (b) sprawdzić dwa — nie jedno — przecięcia i źródłową odwrotność pierwiastków, (c) niezależnie certyfikować pełny TV, (d) sprawdzić jawne gęstości Huber `max(p,q)/(1+D)` i sprzężenie midpoint TV, (e) oddzielić egzogeniczne losowanie skażenia od zależnej od wartości podmiany, (f) zweryfikować warunkowe założenia dla Hoeffdinga i kierunkowe n/n−1. Żaden właściciel BW ani kanonu nie jest zastępowany tym przekazem.

**FINAL:** `ORIGINAL_SOURCE_INHERITED_ROT016 / EXACT_FULL_CAUCHY_TV_IV75_PASS / HUBER_SHARP_FULL_LAW_ALIAS_PASS / POST_OBSERVATION_TV_SHARP_ALIAS_PASS / ROBUST_FINITE_N_CONDITIONAL_HOEFFDING_IV75_PASS / SAME_CELL_SCIPY_MP_PASS / COLD_REPRO_PASS / DIFFERENT_CELL_I1_PENDING / BW_PENDING / NO_GENERAL_NOVELTY / NO_PHYSICAL_SENSOR / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`.
