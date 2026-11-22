---
artifact_id: IW_GEEKY_S13_ROT019_UNKNOWN_SHARED_FAULT_REFERENCE_CALIBRATION_SHARP_COMPOSITE_ALIAS_IV75_001_20261122
return_id: IW_GEEKY_S13_ROT019_UNKNOWN_SHARED_Q_COMPOSITE_ALIAS_REFERENCE_M_N_EQUAL_ETA_SOURCE_IV75_001_20261122
origin_cell: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
result_class: SOURCE_CONDITIONAL_SYNTHETIC_FOUR_MIRROR_CAUCHY / COMPOSITE_UNKNOWN_COMMON_Q_IDENTIFIABILITY_GAP / REFERENCE_BIT_EXPERIMENT / IV75_FINITE_N_OPTIMAL_ALLOCATION_WITHIN_HOEFFDING
status: AUTHOR_ANALYTIC_PROOF / SOURCE_IV75_CERTIFIED_BOUND / INDEPENDENT_SAME_CELL_SCIPY_WITNESS / DIFFERENT_CELL_I1_PENDING
claim_ceiling: NO_GENERAL_MATH_NOVELTY / NO_ACTUAL_FAULT_REFERENCE_CHANNEL / NO_PHYSICAL_SENSOR / NO_CANON / NO_EXEC_SIGN / BW_PENDING
---

# Geeky-S13 ROT019 — wspólna, ale nieznana awaria Q: para rozkładów różni się dla każdego eta<1, jednak obserwator pozostaje nieidentyfikowalny bez referencji; dokładna naprawa przez bit referencyjny

## 0. Pytanie, odpowiedź i chronologia pierwszeństwa

ROT018 rozróżnił egzogeniczne skażenie Hubera oraz podmianę po obejrzeniu wyniku, i wyznaczył dokładną źródłową odległość TV dwóch **syntetycznych** rozkładów Cauchy'ego po projekcji oryginalnej symetrii M13. ROT019 bada naturalny, ale niebezpieczny skrót: „wspólne urządzenie = ten sam rozkład awarii Q pod A i B; więc nawet bardzo częsta awaria nie szkodzi rozpoznawaniu”. To rozumowanie jest poprawne dla pary ze ZNANYM, utrzymanym stałym Q, ale NIE jest ogólnym twierdzeniem o rozpoznawaniu A/B przy nieznanym Q. Różnią się kolejności kwantyfikatorów i zbiory hipotez z nuisance.

Wynik 1: dla każdego ustalonego Q: TV((1−eta)P_A+eta Q,(1−eta)P_B+eta Q)=(1−eta)*delta. To jest ostra równość dla dwóch warunkowych praw, NIE dowód jednostajnej klasyfikowalności przy nieznanym Q. Bez odniesienia do Q zbiory dopuszczalnych praw pod A i B nadal się PRZECINAJĄ dla eta>=delta/(1+delta), nawet gdy Q w każdym pojedynczym modelu jest „to samo” dla A/B.

Wynik 2: JEŚLI dysponujemy m niezależnymi próbkami z samego Q i znamy eta, poprawny kontrast jednego bitu źródłowego E (czysty obszar NP ROT018) jest identyfikowalny dla KAŻDEGO eta<1, niezależnie od kształtu Q. Wystarczy test sum dwóch częstości bez rekonstrukcji gęstości awarii. Dostajemy jawny skończeniepróbkowy rozkład kosztu: m/n=eta w ciągłym optimum określonej nierówności Hoeffdinga. To nie jest optimum wszystkich testów ani nowych urządzeń.

Źródłowe pierwszeństwo pozostaje: M13 FIRST oryginalna publiczna pomocnicza implementacja 41-modowego tensora B (source Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`); Geeky-S12 ROT038 FIRST racjonalne syntetyczne anizotropowe gaussowskie prawa szumu A/B (Git blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`); Geeky-S13 ROT016 FIRST czwórka odbitych punktów i dokładny iloraz Cauchy'ego (blob `cddc2636249e9bf032fff4de78afb30481401f9a`); Geeky-S13 ROT017 FIRST skończony promień odporności jednobitowej na BŁĄD AMPLITUDY kontrastu (blob `90b7a9f6fafbc3a46d9aaed01d8223bcf0ff1a43`); Geeky-S13 ROT018 FIRST source full-TV i różne ostre wartości eta_H/eta_TV (blob `a7c4d7514fc1aa17a0b49c1c0a73d772ca8cf4ff`). M16/AUD3 mają własne odrębne oryginalne prace. NOWOŚĆ ROT019 to tylko źródłowa analiza operacyjnego EKSPERYMENTU z niezależną próbką awarii Q, nie nowy ogólny wynik matematyczny ani ustalenie pierwszeństwa w statystyce.

## 1. Dokładna rodzina źródłowa i zewnętrzne prior art

Zachowujemy N=41 i cztery idealne lokalne kanały odbite ROT016, których istnienie w rzeczywistym torze M13 NIE zostało dowiedzione. Po usunięciu arbitralnych wspólnych przesunięć, dodatnich wzmocnień i dokładnie symetrycznego deterministycznego profilu B otrzymujemy hipotetyczne niezależne T_j=U_j/V_j, gdzie:

`P_A=Cauchy(mu_A=1/84, s_A=sqrt[1−(1/84)^2])`;
`P_B=Cauchy(mu_B=4/585, s_B=sqrt[1−(4/585)^2])`.

Oba rozkłady zależą od **syntetycznych** gaussowskich kowariancji ROT038. Gęstości mają postać `f_X(t)=s_X/(pi*(t²−2*mu_X*t+1))`. Oryginalne ROT018 daje czysty obszar NP `E={t<rlo OR t>rhi}` z dwoma dodatnimi wzajemnie odwrotnymi miejscami przecięcia, `rlo=0.0046857251429306468...`, `rhi=213.414139646816443...`; 75-cyfrowa arytmetyka przedziałowa ROT019 oblicza je OD NOWA z dokładnych racjonalnych mu, NIE wczytując wyników ROT018.

Czyste prawdopodobieństwa E: `pA=0.499193465531129218689284084966...`, `pB=0.500806534468870781310715915033...`, zatem:

`delta = pB − pA = TV(P_A,P_B) = 0.001613068937741562621431830067727136944... >0`.

Główne zewnętrzne hosty klasyczne: Peter J. Huber, „A Robust Version of the Probability Ratio Test” (1965), Annals of Mathematical Statistics 36, 1753–1758, https://encyclopediaofmath.org/wiki/Robust_inference ; Chen, Gao, Ren „A General Decision Theory for Huber's epsilon-Contamination Model” (2015), https://arxiv.org/abs/1511.04144 ; Vallinayagam, Pensia, Jog, „On the Sample Complexity of Robust Binary Hypothesis Testing” (2026), https://arxiv.org/abs/2605.24741. Nie twierdzimy, że konstrukcje mieszanin, nierówność Hoeffdinga lub alokacja prób to nowe ogólne twierdzenia.

## 2. Niebezpieczna zamiana kwantyfikatorów — brak testu jednostajnego bez prób z Q

Rozważmy jeden eksperyment z nieznanym parametrem zakłócającym Q:

`R_(X,Q)=(1−eta)P_X+eta Q`, `X∈{A,B}`, `eta∈[0,1]` znane, `Q` dowolny rozkład prawdopodobieństwa niezależny od wartości bieżącej CZYSTEJ próbki. Parametr Q jest wspólny dla obu potencjalnych modeli w każdej zadanej parze R_(A,Q),R_(B,Q), ale NIE jest znany w analizie statystycznej, zatem musimy rozróżnić DWIE RODZINY możliwych praw `{R_(A,Q):Q∈P}` i `{R_(B,Q):Q∈P}`. Test ma działać jednostajnie dla wszystkich Q, nie znając go.

Dla KAŻDEGO ustalonego Q:

`TV(R_(A,Q),R_(B,Q))=(1−eta)*delta` dokładnie; jest dodatnie dla eta<1. To NIE oznacza rozłączności obu rodzin (patrz warunkowy kwantyfikator).

Niech `nu_plus=(P_B−P_A)_+/delta` i `nu_minus=(P_A−P_B)_+/delta` — dwa znormalizowane do masy 1 prawa, każde z podparciem po swojej stronie E. Dla `eta>=etaH=delta/(1+delta)` zdefiniuj `c=(1−eta)*delta/eta`, więc `0<=c<=1`; dla dowolnego wspólnego pomocniczego rozkładu H:

`Q_A=c nu_plus+(1−c)H`, `Q_B=c nu_minus+(1−c)H`.

Wówczas **dokładnie jako miary**:

`(1−eta)P_A+eta Q_A = (1−eta)P_B+eta Q_B`.

Są to DWA możliwe stany nieznanej awarii. W jednym świecie Q jest stałe i takie samo wobec obu hipotez kontrfaktycznych; w drugim świecie też jest stałe, lecz jego NIEZNANA wartość jest inna. Przy analizie wielu próbek R^n prawo danych pozostaje identyczne, zatem żaden test bez dodatkowych danych o Q nie może zapewnić trafności ponad 1/2 w sensie minimax przy równych priorach.

Próg pełnego aliasu NO-REFERENCE jest dokładnie ten sam co ROT018:

`etaH=delta/(1+delta)=0.0016104711367757003955893585738693432555...`.

Dla eta<etaH rodziny Huberowskie są rozdzielone: na czystym E najmniejszy osiągalny odstęp prawdopodobieństw wynosi `(1−eta)*delta−eta>0`. Jego dodatniość daje jednostajną identyfikowalność bez prób z Q. Dla eta>=etaH warunki przecięcia są konieczne i wystarczające, a powyższy świadek je realizuje.

**Ważne:** gdy Q ma ZNANĄ postać albo jest wspierane wiarygodnym, dostępnym eksperymentem referencyjnym, sytuacja zmienia się. Sama deklaracja „Q jest fizycznie wspólne” bez identyfikującego źródła danych NIE wystarcza.

## 3. Jednobitowy eksperyment referencyjny — dokładna korekcja Q

Dodajemy drugi, NIEPOTWIERDZONY EMPIRYCZNIE kanał referencyjny: `Z_1,...,Z_m IID~Q`, niezależny od głównych odczytów `Y_1,...,Y_n IID~(1−eta)P_X+eta Q`. W każdym teście zachowujemy tylko bit `J_E(y)=1{y∈E}`. Zakładamy, że skażenie jest egzogeniczne — samo wystąpienie awarii nie zależy od bieżącej czystej wartości. Proporcja eta jest ZNANA, taka sama w próbach roboczych pod A/B, a Q w ich obrębie oraz w referencji jest TEN SAM.

Definiujemy:

`S_(n,m)=(1/n) sum_i J_E(Y_i) − eta*(1/m) sum_k J_E(Z_k)`.

Dla każdej, nawet patologicznej gęstości/wielkości punktowej Q, z `q=Q(E)`:

`E_X S=(1−eta) p_X +eta q−eta q=(1−eta)p_X`.

Klasyfikujemy jako B wtedy, gdy `S > (1−eta)(pA+pB)/2`, inaczej A. Różnica średnich wynosi `(1−eta)*delta`. Z niezależności głównej próby i referencji i dwustronnego rozkładu Bernoulli dostajemy z ważonej Hoeffdinga dla KAŻDEGO kierunku błędu:

`P_X(error) <= exp[- (1−eta)^2 delta² / {2(1/n+eta²/m)}]`.

Jest to FINITE-N gwarancja jednostajna po Q, nie aproksymacja CLT. Niewymagające modelowania Q(E) pomiary referencyjne naprawdę dodają osobną informację; ich istnienia nie dowiedziono dla NASH.

**Znamienny kontrast:** przy choćby jednej referencyjnej obserwacji (`m>=1`) rodziny *pełnych rozkładów łącznych* `(R_(X,Q),Q)` są rozłączne dla eta<1: równość drugiego marginesu wymusza Q_A=Q_B, wtedy różnica pierwszego marginesu równa `(1−eta)(P_B−P_A)≠0`. Jednak `m=1` nie daje jednostajnego zaniku prawdopodobieństwa błędu, gdy n→∞; do gwarantowanej dokładności obie wielkości prób muszą rosnąć, o ile eta>0.

## 4. Optymalna alokacja w obrębie konkretnej nierówności koncentracji

W powyższej NIERÓWNOŚCI Hoeffdinga czynnik wariancyjny to `V(n,m)=1/n+eta²/m`. Dla ustalonej łącznej liczby odczytów `N_tot=n+m`, Cauchy–Schwarz daje

`(n+m)*(1/n+eta²/m) >= (1+eta)^2`,

z równością przy `m/n=eta` (eta>0). To **nie** dowodzi optymalności statystycznej całego eksperymentu, tylko alokacji dla tego konkretnego konserwatywnego ograniczenia i równych kosztów jednostkowych odczytów. Jeśli referencja kosztuje inaczej, optimum zmienia się.

Dla wymaganego poziomu `alpha_err` warunek wystarczający brzmi:

`n > 2(1+eta)*log(1/alpha_err) / [(1−eta)^2 delta²]`, `m=ceil(eta*n)`.

Program wskazuje konserwatywne zaokrąglenie `floor(n_cont)+2` i **każde** `n,m` sprawdza osobno w przedziałowym IV75, nie zgadując wyniku z dziesiętnego delta. Należy je czytać jako *udowodnione wystarczające budżety*, NIE pierwsze n, a tym bardziej nie optymalne pełnodystrybucyjne n.

| Skażenie eta | n robocze >95% | m referencyjne >95% | n robocze >99% | m referencyjne >99% | Bez referencji: jednostajnie rozróżnialne? |
|---:|---:|---:|---:|---:|:---|
| `0` | 2,302,647 | 0 | 3,539,729 | 0 | YES |
| `.0005` | 2,306,104 | 1,154 | 3,545,043 | 1,773 | YES |
| `.002` | 2,316,509 | 4,634 | 3,561,038 | 7,123 | NO — ALIAS POSSIBLE |
| `.01` | 2,372,894 | 23,729 | 3,647,716 | 36,478 | NO — ALIAS POSSIBLE |
| `.1` | 3,127,051 | 312,706 | 4,807,039 | 480,704 | NO — ALIAS POSSIBLE |
| `.5` | 13,815,876 | 6,907,938 | 21,238,366 | 10,619,183 | NO — ALIAS POSSIBLE |
| `.9` | 437,502,702 | 393,752,432 | 672,548,217 | 605,293,396 | NO — ALIAS POSSIBLE |

Przykład: przy eta=0.1 budżet >95% wynosi `n=3,127,051` roboczych i `m=312,706` referencyjnych; bez referencji istnieje dokładny alias pełnego R dla dwóch różnych Q, choć dla każdego USTALONEGO Q obie hipotezy nadal mają odległość `(1−eta)delta`. Dla eta=0.5 wystarczający łączny budżet rośnie do ok. 20.72 mln odczytów przy >95% — nie można utożsamiać go z kosztem samego czujnika.

## 5. Inne możliwe błędy interpretacyjne / falsyfikatory

1. **Q nie jest znane ani obserwowalne:** brak referencji => nie wolno użyć testu z sekcji 3 ani błędnie zakładać testowania przy znanym Q.
2. **Eta nie jest znane:** przy podstawieniu błędnego `eta_tilde` błąd wartości oczekiwanej korekcji wynosi `(eta−eta_tilde)*Q(E)`; zmienia się również próg decyzyjny. Wymagana jest osobna kontrola udziału awarii.
3. **Zmienny Q bez dopasowanej referencji:** jeśli Q w kanale roboczym i Q w referencji nie są identyczne albo próbki zależą od siebie, odejmowanie przestaje dokładnie usuwać awarię. Proste rozumowanie IID z sekcji 3 nie działa automatycznie dla polityk post-selekcyjnych.
4. **Adaptacyjne skażenie po obejrzeniu T:** to TV-model z ROT018, NIE egzogeniczny model mieszaninowy. Zaprezentowany eksperyment referencyjny ma wtedy inną strukturę i wymaga nowego dowodu.
5. **Złe koszty jednostkowe:** `m/n=eta` minimalizuje liczbę *odczytów* przy jednakowym koszcie, nie czas sprzętowy, objętość danych czy koszt laboratoryjny.
6. **Brak surowych instrumentów:** cztery kierunkowe kanały RAW, dostęp do trybu awaryjnego Q i statystyka Cauchy'ego pozostają hipotezami pomiarowymi, nie udokumentowanym stanem fizycznego M13/DTC0a. Nie przenosić do GR/TPE/GW/J3/K ani do rzeczywistego wykrycia NASH.

## 6. Faktycznie wykonane reprodukcje i pierwotność źródeł

Program autorski `rot019_primary_iv75.py` odtworzył od dokładnych mu i skal, skierowanie IV75 dwóch pierwiastków przecięcia, oba prawdopodobieństwa E, delta i etaH, a także 7 poziomów eta × 2 progi trafności × n,m z certyfikatem znaku wykładnika Hoeffdinga. Nie importuje kodu ROT018. Osobno napisany program `rot019_independent_scipy.py` odtworzył TV bezpośrednią kwadraturą na całej osi i sprawdził jawne pary rozkładów Q_A,Q_B przy eta=0.002/0.01/0.1/0.5, z równością gęstości mieszaniny w reprezentatywnych punktach oraz małym testem Monte Carlo korekcji bitu Q(E). To jest SAMODZIELNA druga implementacja tej samej komórki, nie different-cell I1.

Kontroler `rot019_semantic_guard.py` niezależnie oblicza wybrane tożsamości ze źródłowych wymiernych mu, sprawdza wszystkie budżety oraz wykonuje rzeczywiste pięć prób zmiany fałszywych twierdzeń w plikach JSON na dysku, po przeliczeniu SHA-256 tych zmienionych plików. Każdy musi zostać ODRZUCONY semantycznie. Pakiet ZIP jest odtwarzalny w osobnym katalogu, a manifest wiąże pełne bajty kodu, raportu i certyfikatów.

Dodatkowe wyniki/numery z ROT018 i ROT016 są odczytane z lokalnego pełnego raportu poprzednika i z potwierdzonych publicznych blobów GitHub, a nie traktowane jako dowód fizycznej aparatury. Wszystkie source-inputs i literalne priorytety podano powyżej. Nie uruchamiano nieistniejącego pełnego oryginalnego historycznego DTC0a ani oryginalnego natywnego pomocniczego skryptu M13.

### Wniosek do niezależnego, wąskiego I1

AUD3/REC14/M16 powinni niezależnie przeprowadzić: (i) równość TV dla tego SAMEGO ustalonego Q, (ii) alternatywne globalne Q_A,Q_B i alias przy etaH bez referencji, (iii) korektę przez referencyjny bit i weighted Hoeffding z poprawną alokacją, (iv) pełne sprawdzenie IV75 i bramek przy eta>=etaH, (v) falsyfikator nieznanego eta i braku realnego kanału fault-mode. Nie audytować tej pracy jako nowe ogólne twierdzenie odpornej statystyki ani jako dowód wykrycia fizycznego.

**FINAL:** `SOURCE_ROT016_CAUCHY / UNKNOWN_SHARED_Q_FIXED_PAIR_TV_EQUIVALENCE / COMPOSITE_ALIAS_AT_HUBER_THRESHOLD / REFERENCE_ONE_BIT_RECOVERY_FOR_ETA_LT1 / IV75_FINITE_SAMPLE_ALLOC_M_OVER_N_EQ_ETA / INDEPENDENT_SAME_CELL_SCIPY / DIFFERENT_CELL_I1_PENDING / BW_PENDING / NO_GENERAL_MATH_NOVELTY / NO_HARDWARE / NO_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`.
