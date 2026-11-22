---
artifact_id: IW_GEEKY_S13_ROT012_ORIGINAL_M13_SIX_MASK_FOURIER_OBSERVABILITY_NOGO_001_20261122
return_id: IW_GEEKY_S13_ROT012_SIX_ORIGINAL_M13_MASK_OBSERVABILITY_NO_GO_AND_FOUR_MODE_INFORMATION_GAP_001_20261122
origin: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-22 Europe/Warsaw
science_class: ORIGINAL_M13_N41_GEOMETRIC_MASK_OBSERVABILITY_FALSIFIER / SOURCE_ANISOTROPIC_ROT038_GAUSSIAN_CONDITIONAL_NONRECOVERABILITY
status: AUTHOR_EXACT_SYMMETRY_PROOF / EXACT_RATIONAL_6X6_COVARIANCE_CHECK / POSITIVE_FIELD_EXPLICIT_WITNESS / SAME_CELL_TWO_INDEPENDENT_IMPLEMENTATIONS / DIFFERENT_CELL_I1_PENDING
claim_ceiling: NO_GENERAL_MATH_NOVELTY / NO_ACTUAL_RAW_SITE_SENSOR / NO_HISTORICAL_DTC0A_RUNTIME / NO_CANON / NO_EXEC_SIGN / BW_PENDING
---

# Geeky-S13 ROT012 — granica obserwowalności: sześć oryginalnych agregatów M13 nie wyznacza czteromodowego niezmiennika

## 1. Rozstrzygnięty problem, zakres oraz źródła rzeczywiście przeczytane

ROT007–011 konstruują i rygorystycznie analizują czteromodowy iloraz krzyżowy na źródłowej siatce M13 `N=41` i na hipotetycznej rodzinie innych `N`. ROT010 daje autorski certyfikat IV75: przy dokładnych dwóch racjonalnych, **syntetycznych** gaussowskich prawach szumu Geeky-S12 ROT038 cztery hipotetyczne pomiary mocy Fouriera w pełnych migawkach umożliwiają ponad 95% rozróżniania przy 14 539 migawkach, ponad 99% przy 29 083. ROT011 przenosi *matematyczną* konstrukcję na wszystkie całkowite N>=17.

**Pytanie o most do oryginalnego obserwatora:** czy czteromodowy iloraz da się policzyć z *rzeczywistych w sensie oryginalnego kodu pomocniczego* sześciu wyników regionalnych (pełny pomiar + pięć sześciennych masek k=2,...,6), bez dodawania hipotetycznych kanałów RAW-site? **Werdykt: NIE**, już na poziomie dokładnej algebry. Dodatkowo w modelach gaussowskich ROT038 kontrast nie jest funkcją oryginalnych sześciu agregatów nawet prawie na pewno; zachowuje dodatnią losową nieoznaczoność warunkową.

**Zachowane pierwszeństwo:** M13 FIRST publiczna pomocnicza implementacja B Fourier/TT, *rzeczywiście bezpośrednio odczytana* Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`:
https://github.com/wmakiela-tech/Nash-iw-research/blob/30d8549b822ecec4d6939b01dbd1e76a98495f09/research/m13/2026-10-24/verify_m13_rot33_interval.py

Geeky-S12 ROT038 FIRST oryginalne, dokładne racjonalne anizotropowe prawne źródłowo dwa modele szumu Gaussa oraz **dokładna identyczność prawa sześciu (a nawet dziewięciu) starych obserwacji**, Git blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s12/2026-11-21/IW_GEEKY_S12_ROT038_ORIGINAL_M13_ANISOTROPIC_DIRECTIONAL_EXACT_ALIAS_ONE_BOUNDARY_PROBE_ESCAPE_AND_NONGAUSSIAN_DEPENDENCE_001_20261121.md

Geeky-S13 ROT007 FIRST czteromodowa grupa rozdzielnych kalibracji i maksymalny niezmiennik; ROT009 FIRST dokładne ryzyko NP; ROT010 FIRST autorski IV75 koszt próbek; ROT011 FIRST matematyczna przenośność N. M16 ROT001 FIRST osobny dowód ścisłej monotoniczności Bayesowskiego ryzyka; M16 ROT002 FIRST dowód granicy nierozdzielnej kalibracji. Nowy ROT012 NIE przypisuje sobie pierwszeństwa dla aliasu sześciu wyników, który wykazał ROT038. Własny wkład ROT012 to źródłowo ostry **no-go odtworzenia samego czteromodowego kontrastu z sześciu masek**, jego dodatni przestrzenny kontrprzykład i ciągła warunkowa nieobserwowalność z czterech sinusowych modów.

Ogólna koncepcja utraty informacji wskutek agregacji jest klasyczna (porządek doświadczeń/Blackwell; por. https://python.quantecon.org/blackwell_kihlstrom i https://www.stat.berkeley.edu/~wfithian/courses/stat210a/sufficiency.html). **Nie ma roszczenia do nowego ogólnego twierdzenia matematycznego**. Oryginalny moduł M13 ODCZYTANO, ale go w ROT012 NIE wykonano; pełny historyczny `dtc0a_runtime_v0_3_1.py` niedostępny.

## 2. Dokładna geometria sześciu źródłowych masek

Na torusie `(Z/41Z)^3` niech `I_k = {k,k+1,...,40-k}^3`, dla k=2,...,6; liczność `|I_k|=(41−2k)^3`. Oryginalne sześć danych `inner(0)` oraz `inner(k=2,...,6)` generuje tę samą przestrzeń liniową obserwacji co sześć rozłącznych obszarów:

`R0 = T \ I2`, `R1=I2 \ I3`, ..., `R4=I5 \ I6`, `R5=I6`.

Ich **dokładne** liczności są `[18268,7778,6938,6146,5402,24389]`, suma 68921. Każdy region jest niezmienniczy na wszystkie permutacje osi przestrzennych, a ponadto na odrębne odbicia współrzędnych `u -> 40−u` (czyli odwzorowanie `u+1/2 -> -(u+1/2)` modulo 41). Geometria k odpowiada wprost oryginalnej formule `window_mode` z zachowanego pomocniczego programu M13 (k=2..6, odcięcie 2k współrzędnych z każdej osi). Jest to wyraźnie **model źródłowej matematyki masek**, nie twierdzenie o istniejącym urządzeniu.

Dla pola skalarnego `F:T->R` niech `M_r(F)=|R_r|^-1 Σ_{u∈R_r} F(u)`. Wektor `M(F)` jest liniowo równoważny sześciu oryginalnym obserwacjom źródłowym.

## 3. Dokładny dodatni kontrprzykład: stare obserwacje te same, nowy kontrast 1 vs 9

Wybieramy cztery źródłowo użyte w ROT007–011 mody:

`k_xH=(20,0,0)`, `k_yH=(0,20,0)`, `k_xL=(7,0,0)`, `k_yL=(0,7,0)`.

Niech `c_{d,j}(u)=cos(2π j u_d/41)` i `eta=1/25`. Definiujemy DWA RZECZYWISTE, ŚCIŚLE DODATNIE POLA:

```
F1(u)=1+eta*[c_x,20+c_y,20+c_x,7+c_y,7](u)
F2(u)=1+eta*[(3/2)c_x,20+(1/2)c_y,20+c_x,7+c_y,7](u).
```

Oba spełniają `F_i(u)>=1−4/25=21/25>0` w każdym z 68921 punktów. Różnica `F2−F1=eta/2*[c_x,20−c_y,20]` jest **antysymetryczna** przy zamianie x↔y. Wszystkie sześć masek jest symetrycznych przy tej zamianie, więc `M_r(F1)=M_r(F2)` **DOKŁADNIE dla każdego r**. Wartość ta zachodzi również dla oryginalnych pięciu masek zagnieżdżonych i maski pełnej, ponieważ są one odwracalnymi kombinacjami sześciu średnich regionów.

Jednocześnie ortogonalność DFT na siatce 41 zapewnia, że moc mode j dla dodatniej/ujemnej pary wynosi (wspólny czynnik) razy kwadrat zapisanej amplitudy; żaden ze wskazanych modów nie jest Nyquistem. Dla ilorazu

`C(F)=|FFT(F)(k_xH)|² |FFT(F)(k_yL)|² / [|FFT(F)(k_yH)|² |FFT(F)(k_xL)|²]`

otrzymujemy źródłowo **DOKŁADNIE** `C(F1)=1`, `C(F2)=9`. Skoro istnieją dwa pola z tym samym M i różnym C, **nie istnieje żadna funkcja** `g:R^6->(0,∞)` taka, że `C(F)=g(M(F))` dla wszystkich dodatnich pól tej siatki.

Dla kontroli wykonany faktycznie program NumPy przejrzał całą siatkę N41 i uzyskał minima pól ~0.842339102, różnicę sześciu średnich `2.22×10^-16`, a wartości kontrastu odpowiednio ~1.0000000000000013 i ~9.000000000000004. Nie są to błędy tezy dokładnej, lecz normalne zaokrąglenia FFT. Druga, niezależnie napisana implementacja wyprowadziła te same równości bez 3D FFT, z dokładnych sum amplitud i geometrycznych 1D sum Fouriera dla każdego I_k.

**Uwaga epistemiczna:** F1 i F2 są skonstruowanymi dopuszczalnymi dodatnimi POLAMI skalarnej energii, nie dwoma oryginalnymi rozwiązaniami deterministycznego operatora M13 i nie empirycznymi obserwacjami. Ich zadaniem jest falsyfikacja odwracalności mapy masek, a nie zmiana pierwotnej dynamiki pola B.

## 4. Silniejsze no-go niemal pewnej rekonstrukcji pod każdym stacjonarnym gaussowskim modelem ROT038

ROT038 wprowadza dokładnie racjonalne współczynniki `beta0, beta_x, beta_y, beta_z, beta_xy, beta_xz, beta_yz, beta_body`:

`A=(1,1/25,1/25,1/25,1/30,1/30,1/30,2/25)`;
`B=(1,1/20,3/100,1/25,1/30,13/300,7/300,2/25)`.

Kowariancja szumu na pełnych 68921 źródłowych węzłach ma postać kombinacji identyczności i siedmiu symetrycznych operatorów przesunięcia ±1 (axial, face, body). Dla obu modeli suma nieidentycznościowych wag wynosi dokładnie `3/10`, więc **wszystkie** wartości własne przestrzennej kowariancji spełniają `lambda>=7/10`.

Każdy operator jest jednocześnie niezmienniczy względem indywidualnych odbić współrzędnych `u->40−u` oraz diagonalizowany przez pełne dyskretne mody Fouriera. Dla każdego z czterech osiowych k wybieramy **znormalizowaną rzeczywistą składową sinusową**:

`S_{d,j}(u)=sqrt(2/41³)*sin(2π j (u_d+1/2)/41)`.

(Przesunięcie o pół komórki odpowiada centrum źródłowych masek; nie zmienia energii modu Fouriera.) Każda taka funkcja jest antysymetryczna względem odpowiedniego odbicia, zatem dokładnie `M_r(S_{d,j})=0` dla wszystkich r. Ponadto jest wektorem własnym stacjonarnej kowariancji z dodatnią wartością własną `lambda_X(d,j)>=0.7`. Stąd dla gaussowskiego wektora szumu Y:

`Cov_X(M_r(Y),<Y,S_{d,j}>) = lambda_X(d,j) <M_r,S_{d,j}> = 0`.

Wektor czterech składowych sinusowych ma dodatnio określoną diagonalną macierz kowariancji (różne niezerowe pary częstotliwości), jest więc **niezależny** od WSZYSTKICH sześciu średnich regionalnych i od czterech ortogonalnych cosinusowych składowych w każdym z modeli A/B — przez wspólną gaussowskość. Jeśli dodano oryginalną niezależną losową globalną kalibrację średnich, ta niezależność pozostaje, pod warunkiem niezależności kalibracji od Fourierowego szumu.

Zatem nawet po warunkowaniu na pełny wektor oryginalnych sześciu agregatów (a nawet dodatkowo na czterech cosinusowych amplitudach), cztery sinusowe amplitudy pozostają niezależnymi rozkładami normalnymi o dodatniej wariancji, pełnym nośniku `R`. Każda moc Fourierowa jest proporcjonalna do sumy kwadratów pary cos+sin. W konsekwencji **dla prawie każdego ustalonego zestawu agregatów rozkład warunkowy C ma pełen nośnik `(0,∞)`**: sinusowa energia w liczniku może dowolnie zwiększać iloraz, a sinusowa energia w mianowniku może go dowolnie zmniejszać, każdorazowo na zdarzeniu o dodatnim prawdopodobieństwie.

W szczególności `C` nie jest niemal na pewno funkcją sześciu starych agregatów nawet **dla jednego ustalonego X**, a więc nie można odzyskać statystyki NP z ROT010 z takich danych ani na poziomie osobnego odczytu, ani przez „dokładniejszą estymację” tych samych sześciu liczb.

**Sześć maskowych obserwacji nie identyfikuje też A/B w tym źródłowym, syntetycznym modelu**: dokładne kowariancje 6×6 są identyczne, ponieważ original mask adjacency liczniki dla axial x/y/z są takie same, podobnie dla face xy/xz/yz, a źródłowe zsumowane wagi A/B to identycznie `beta0=1`, axial `3/25`, face `1/10`, body `2/25`. Przy tej samej deterministycznej średniej M13 i gaussowskim szumie oba wektory masek mają IDENTYCZNE pełne rozkłady. Zatem ich optymalny błąd klasyfikacji A/B pozostaje `1/2` dla dowolnego n. **To ostatnie pierwszeństwo należy do Geeky-S12 ROT038**, a obecny program odtworzył wynik dokładną arytmetyką liczb wymiernych z 6×6 macierzy obliczonych z liczników 26 kierunkowych przesunięć.

## 5. Operacyjny sens i ściśle ograniczona rekomendacja

To nie jest sprzeczność pomiędzy ROT010 i ROT012: tam rozpatrywano hipotetyczny obserwator wyposażony w 4 RAW Fourier power channels na każdą migawkę, tutaj źródłowo oryginalne 6 maskowanych średnich. Są to **dwa różne doświadczenia statystyczne**. Pierwsze może odróżniać postulowaną parę A/B po odpowiedniej liczbie niezależnych odczytów, drugie nie, ponieważ zawiera mniej informacji istotnej dla konkretnych kanałów. Nie można przeliczyć jednego w drugie bez niejawnego dodania czujników.

Nie należy jednak twierdzić, że fizyczny instrument koniecznie musi posiadać cztery RAW Fourier channels. Geeky-S12 ROT038 wykazał, że **jeden dodatkowy hipotetyczny pomiar lokalny na granicy skorup** `Z3=E(3,4,3)-E(4,3,3)` połączony z wcześniejszymi trzema głębokimi kontrastami i sześcioma regionami podnosi rangę wybranej 9-parametrowej mapy kowariancji do 9. To jest **inna, potencjalna ścieżka projektowania obserwatora**; ranga nie jest jednak dowodem użyteczności lub dostępności fizycznych sensorów ani ograniczonego kosztu próbkowania.

**Praktyczny wymagany krok przed wszelkimi dalszymi progami n:** uzyskać źródłową specyfikację rzeczywistych dostępnych danych/urządzenia: czy istnieją odczyty pełnego pola, dwa rozróżnialne kierunki przy co najmniej dwóch częstotliwościach, niezerowa przepustowość i odpowiednio stacjonarny pomiar? Jeśli nie, prace matematyczne ROT007–011 zachowują wartość modelową, ale nie mogą być prezentowane jako empirycznie realizowalny test M13.

## 6. Kontrole, ograniczenia, żądanie I1

Rzeczywiście wykonany `rot012_operational_observability.py`: oryginalna 6-regionowa geometria z N41, 6/6 regionów i ich liczności, 6 symetrii permutacji osi i 3 odbicia centrowane, **dokładny** (Fraction) rachunek regionalnych kowariancji A/B z zliczonymi na 41³ siatce kierunkowymi przesunięciami; rzeczywista pełna FFT 3D obu dodatnich pól; ortogonalność czterech 68 921-długich funkcji sinusowych, `M*S=0`; dodatnie cztery wariancje pod każdym syntetycznym modelem oraz niezależne przestrzenne FFT ośmiu składowych operatora kowariancji. Podano jawne zakresy i maksima błędów float. Ten kod nie wykonuje oryginalnego programu M13 — rekonstruuje potrzebną geometrię z jego bezpośrednio odczytanej formuły.

Drugi, osobno napisany `rot012_independent_analytic_referee.py` nie importuje głównego kodu. Z geometrycznych sum 1D i dokładnych ułamków odtwarza liczności, równość amplitud obserwowanych przez maski, kontrast 1/9 oraz z niezależnej postaci symbolu oryginalnego szumu wszystkie cztery dodatnie wariancje i antysymetrię sinusów względem odbicia. Jest to SAME-CELL niezależność algorytmiczna, NIE different-cell I1.

**Ograniczenia:** (i) dowód warunkowej niezależności sinusów wymaga pełnoprzestrzennego, translacyjnie stacjonarnego GAUSSOWSKIEGO szumu ze źródłowym operatorem SPD; przy nieliniowych, adaptacyjnych wzmocnieniach działa tylko konstrukcyjny no-go deterministycznej agregacji, nie automatycznie niezależność warunkowa; (ii) wartości mocy FFT i ich ilorazy nie są odczytami historycznego instrumentu M13; (iii) skonstruowane pola nie są nowymi rozwiązaniami deterministycznej dynamiki B; (iv) nie przeprowadzono oryginalnego M13 native-helper, historyczny pełny DTC0a wciąż niedostępny; (v) nie wykazano ogólnej nowości matematycznej lub fizycznej.

**Żądanie bounded different-cell I1:** bez importowania autorskich wyników najpierw sprawdzić źródłową definicję okna `inner(k)` i odwracalność sześciu sum zagnieżdżonych do sześciu skorup, dokładną dodatnią parę pól oraz kontrast 1/9, następnie niezależnie sprawdzić w gaussowskim modelu odbicia, zerowe kowariancje sinus–maska, dodatniość wariancji i wynik nieodtwarzalności niemal na pewno. Oddzielić stare pierwszeństwo aliasu 6/9 od nowego twierdzenia o nieodtwarzalności C. Nie interpretować tego jako uniwersalnej niemożności pomiaru różnic kierunkowych ani fizycznego no-go NASH.

FINAL: `ORIGINAL_M13_MASK_GEOMETRY_RECONSTRUCTED / SIX_REGION_COUNTS_PASS / A_B_SIX_MEAN_COVARIANCE_EXACT_FRACTION_PASS / POSITIVE_FIELDS_MASK_IDENTICAL_C_1_VS_9_PASS / GAUSSIAN_SINE_CONDITIONAL_NONRECOVERABILITY_PROOF / SAME_CELL_TWO_INDEPENDENT_CHECKS_PASS / ORIGINAL_M13_NATIVE_NOT_EXECUTED / DIFFERENT_CELL_I1_PENDING / BW_PENDING / NO_GENERAL_NOVELTY / NO_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`.
