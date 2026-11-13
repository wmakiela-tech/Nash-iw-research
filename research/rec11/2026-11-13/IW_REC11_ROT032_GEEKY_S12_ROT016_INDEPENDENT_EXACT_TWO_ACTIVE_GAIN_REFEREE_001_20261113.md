---
artifact_id: IW_REC11_ROT032_GEEKY_S12_ROT016_INDEPENDENT_EXACT_TWO_ACTIVE_GAIN_REFEREE_001_20261113
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
created_at: 2026-11-13
review_type: I1_NONBLIND_EXACT_ORIGINAL_SOURCE_25D_INTERVAL_REFEREE
original_owner: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12 ROT016
scope: M13_N41_B_QUARTIC_FIVE_SHELL_POSITIVE_GLOBAL_GAIN_RELATIVE_PER_SHELL_NUISANCE
result: PASS_AUTHOR_2ACTIVE_KAPPA_0066 / NEW_COMPLETE_NEAR_CRITICAL_PIECEWISE_GAIN_RISK_LAW / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
bw_ingest: UNVERIFIED
owner_ack: UNVERIFIED
---

# REC11 ROT032 — niezależna recenzja Geeky-S12 ROT016 i dokładne prawo progowe dla kalibracji 5 powłok

## 0. Priorytet naukowy i źródła

**M13** jest właścicielem pierwotnych 25 kierunkowych przedziałów współczynników modelu B oraz definicji pięciu rozłącznych powłok dla N=41. **Geeky-S12 ROT015** jako pierwszy otrzymał ostry próg zerowej straty przy pięciu niezależnych kalibracjach względnych; **Geeky-S12 ROT016** jako pierwszy wyprowadził ścisłe dodatnie minimum przy κ=0,066 i przypisał je tylko powłokom 1 i 5. Dotychczasowe niezależne kontrole AUD2 ROT005 i M15 ROT006 potwierdzały _inne_ twierdzenie globalne z pojedynczym wspólnym zyskiem. REC11 ROT029 dowiódł _innego_ kontrprzykładu geometrycznego przy δ=0,02514. Nie zastępować tymi zatwierdzeniami recenzji ROT016.

Bezpośrednio odczytano GitHub właściciela: [Geeky ROT016](https://github.com/wmakiela-tech/Nash-iw-research/blob/4d3dc22eb387d52c9a061e401af908852fa75285/research/geeky-s12/2026-11-13/IW_GEEKY_S12_ROT016_EXACT_TWO_ACTIVE_SHELL_GAIN_RISK_FLOOR_AND_GLOBAL_REFEREE_INTEGRATION_001_20261113.md), blob `4d121722479cf99c27442162f9c1f569daf055c8`; [wynik maszynowy](https://github.com/wmakiela-tech/Nash-iw-research/blob/265c7ace31b4b855e2665148d276010b7ecb57fc/research/geeky-s12/2026-11-13/IW_GEEKY_S12_ROT016_TWO_ACTIVE_RISK_FLOOR_SOURCE_RESULTS_001_20261113.json), blob `45afeda2ff5b06b2fba06d64a494231715f2e1f8`. Oryginalny M13 `research/m13/2026-10-26/direct_B.json`, **Git blob `a6f50fbe5904e580e84c87ee87c5ad043cdec5d0`**, został ponownie odczytany. REC11 sprawdził dokładnie znak po znaku ekstrakcję 25 par `[lo,hi]` do pierwotnego [CSV](https://github.com/wmakiela-tech/Nash-iw-research/blob/66de5ee1b0ee6eca0f225195350668d4d34f284b/research/rec11/2026-11-13/rec11_rot029_original_m13_direct_B_25_endpoints_source_extract.csv), Git blob `09824281d5e4b3c87446be97b0e52ace3b33edae`. Ekstrakt (3377 bajtów) ma SHA256 `fb82f6d4b7554791836c026aacaad28040f0c92cbf211023b89011764632f8f2`. Nie podstawiono ogólnych własności innego modelu.

## 1. Kontrakt i profilowanie bez heurystyk

Maski `k=2,3,4,5,6`, liczby punktów kostek N_k=(41−2k)^3, wagi powłok W=(7778, 6938, 6146, 5402, 24389). Dla każdego j=0,…,4 współczynnik powłoki s_{i,j} uzyskuje się przez dokładne odjęcie sąsiednich zagregowanych masek, a s_i(t)=Σ_j s_{i,j} t^j. Parametry źródłowo zamrożone: α=1/20=.05, β=3/40=.075, ε=10^-7, wspólna dodatnia amplituda c>0, niezależne względne kalibracje η_i∈[−κ,κ] i κ∈[33/500,1) (tutaj dolna granica 0,066). Każdy z 25 współczynników źródłowych wybiera się niezależnie z `[lo−ε max(|lo|,|hi|), hi+ε max(|lo|,|hi|)]` i **ten sam wybór** stosuje się przy α i β.

Rozpatrywana strata jest dokładnie

    D²(κ) = min_{c>0, |η_i|≤κ} Σ_i W_i [s_i(α)−c(1+η_i)s_i(β)]².

Dla r_i=s_i(α)/s_i(β)>0, A_i=W_i s_i(β)^2>0, u=1−κ, v=1+κ, wykonanie minimum po η_i dla ustalonego c daje funkcję

    Φκ(c)=Σ_i A_i max{r_i−vc, uc−r_i, 0}².

Jest ona globalnie wypukła i odcinkami kwadratowa. Wniosek nie wymaga iteracyjnego lokalnego optymalizatora ani losowego skanowania współczynników.

## 2. PASS: niezależny certyfikat Geeky ROT016 przy κ=0,066

**W pełni niezależny skrypt 1 (Python3 stdlib Fraction)** tworzy współczynniki powłokowe i wykonuje _skierowaną arytmetykę przedziałową_ nad pełnym 25-wymiarowym pudełkiem. Nie importuje ROT016, ROT015, ROT029 ani jego wyniku. Obejmuje korelacje współczynnika pomiędzy wartościami α i β w tym sensie, że całe wyrażenie jest funkcją jednego zadanego wspólnego zbioru 25 parametrów; przedziałowa nadaproksymacja może być konserwatywna, ale nie gubi żadnej legalnej realizacji.

W każdej legalnej realizacji: `0<r1<r2<r3<r4<r5`, a dokładnie

    c*=[A1(1−κ)r1 + A5(1+κ)r5]/[A1(1−κ)² + A5(1+κ)²]

ma `r1<(1−κ)c*`, `r5>(1+κ)c*`, natomiast trzy pozostałe r_i leżą ściśle wewnątrz `[(1−κ)c*,(1+κ)c*]`. Zatem tylko **powłoki 1 i 5** mają nieznikający błąd. Pierwsza pochodna Φ jest tam równa zero; wypukłość daje globalne minimum.

Rygorystyczna całkowicie wymierna obwiednia, wyświetlana w zapisie dziesiętnym wyłącznie poglądowo:

    4.30499086735849683×10^-6 ≤ 10^24 D²(κ=.066) ≤ 4.41727764693762614×10^-6.

W pełni bezpieczny odczyt: `4.30×10^-6 < 10^24 D² < 4.42×10^-6`. Midpoint współczynników: c*=0.570342055892336441…, `10^24D²=4.36095353085121055×10^-6`. Wyniki niezależnej implementacji zgadzają się z danymi właściciela (z dokładnością do wyświetlonych cyfr), a w pakiecie znajdują się rzeczywiste granice **dokładnych ułamków** z licznikiem i mianownikiem.

## 3. NOWY WYNIK REC11: całkowita funkcja ryzyka w przedziale bliskokrytycznym

Niech dla dowolnej pojedynczej realizacji źródła

    κ_crit=(r5−r1)/(r5+r1),  t=(1+κ)/(1−κ).

Weryfikacja oryginalnych 25 przedziałów ścisłą arytmetyką wymierną daje dla **każdego** ich wyboru `r5<2r1` oraz poprawne uporządkowanie pięciu r_i. Z pierwszego certyfikatu przy κ0=0,066 wiadomo, że r2,r3,r4 leżą między L(κ0)=(1−κ0)c* i R(κ0)=(1+κ0)c*.

Dla κ∈[κ0,κcrit] t rośnie od t0 do tc=r5/r1. Dokładnie:

    L(t)=(A1 r1+A5 t r5)/(A1+A5 t²),    R(t)=tL(t).

Pochodne po t mają znaki (wspólny dodatni mianownik pominięty):

    L'(t) ∝ A5[A1(r5−2t r1)−A5r5 t²] < 0
    R'(t) ∝ A1[A1r1+A5t(2r5−t r1)] > 0.

Pierwsza ujemność wynika z `r5<2r1`, t≥1. Druga dodatniość wynika z t≤tc=r5/r1. Zatem przedział `[L,R]` **rozszerza się** przy wzroście κ; każda z trzech powłok środkowych nadal ma zerowy residual. Dla skrajnych:

    L−r1 = A5 t (r5−t r1)/(A1+A5 t²)>0,
    r5−R = A1 (r5−t r1)/(A1+A5 t²)>0

przed κcrit; w κcrit obie strony stają się równością. **To pełny dowód, że dwupowłokowy wzór działa dla całego continuum κ, nie tylko w punkcie 0,066.**

Oznaczając u=1−κ, v=1+κ:

    Dmin²(κ)=A1 A5 [u r5−v r1]²/[A1u²+A5v²]
            =A1 A5(r1+r5)² (κcrit−κ)²/[A1(1−κ)²+A5(1+κ)²]

przy `κ0≤κ<κcrit`. Dla `κcrit≤κ<1` wybór `c∈[r5/(1+κ), r1/(1−κ)]` dopuszcza η_i=r_i/c−1 i daje **dokładnie Dmin²=0** na wszystkich pięciu powłokach. Źródłowo zidentyfikowany próg:

    0.0662678476484445805… < κcrit < 0.0662713467554889718…

(dla całego pudełka; nierówności pochodzą z konserwatywnych skierowanych obwiedni ułamkowych). Bezpieczne przedziały w liczbach dziesiętnych:

    0.06626784 < κcrit < 0.06627135.

W szczególności każda realizacja ma dodatnią stratę dla `κ∈[.066,.06626784]`, każda ma zerową dla `κ∈[.06627135,1)`, a pomiędzy nimi konkretny próg zależy od współczynników. **Dla każdego ustalonego źródła kwadrat straty zanika kwadratowo** przy zbliżaniu się κ do κcrit od dołu; jest klasy C¹, ale nie C² w progu (dodatnia jednostronna druga pochodna z lewej, zerowa z prawej). Odległość D (bez kwadratu) zanika liniowo. Wynik jest klasyczną geometrią kalibracji/zbiorów dopuszczalnych, nie deklaracją odkrycia nowego prawa fizycznego.

## 4. Druga niezależna metoda obliczeniowa

**Skrypt 2** jest kodowo odrębny i nie importuje skryptu 1 ani kodu Geeky. Dla każdej zadanej realizacji źródła i κ enumeruje wszystkie dozwolone punkty zmiany aktywnych składników: `c=r_i/(1+κ)` i `c=r_i/(1−κ)`, a następnie sprawdza minima **wszystkich lokalnych dokładnych kwadratowych odcinków** oraz granice. To globalna minimizacja, nie dopasowanie przy użyciu wyprowadzonego dwupowłokowego wzoru.

Uruchomiono 7 wymiernych, w pełni źródłowo legalnych realizacji 25 współczynników (midpoint, wszystkie dolne, wszystkie górne i 4 niezależne wzory narożne) × 7 wartości κ na obu stronach progu, tj. **49/49 niezależnych testów globalnego minimum**, z czego 28 z dwoma aktywnymi powłokami i 21 z dokładnie zerową stratą. Weryfikacja dokładnej równości ułamków potwierdziła wzór dla każdego przypadku. Testy są kontrolami dyskretnymi; całe kontinuum i pełne pudełko zamyka dowód wymierny z §2–3.

**4 negatywne mutacje wejścia**, każda uruchomiona przeciw DWÓM niezależnym skryptom: zmiana cyfry, dopisany komentarz, usunięty końcowy znak nowej linii, usunięty wiersz. **8/8 prób** poprawnie przerwało się z powodu kontrolowanego SHA256 przed obliczeniami. Skrypty nie zastępują ani nie piszą do plików M13/Geeky.

## 5. Reprodukcja i granice

Oryginalny 25-wierszowy CSV ekstrakt pozostaje osobnym, zweryfikowanym odczytem oryginalnego M13. Pakiet lokalny zawiera dokładnie ten sam plik (SHA256 pin) plus **dwa wykonane niezależne skrypty**, wynik JSON z dokładnymi licznikami i mianownikami, 49-elementowy zbiór kontroli, skrypt i wynik mutacji, pełny raport oraz SHA manifest. Pakiet przeszedł następnie ZIP CRC, pełną kontrolę manifestu SHA-256 oraz czyste ponowne uruchomienie w oddzielnym katalogu: trzy pliki wynikowe JSON są bajtowo identyczne; osiem testów negatywnych pozostało fail-closed. Dane maszynowe i procedura znajdują się w README. Żadna pierwotna fizyczna implementacja `dtc0a_runtime_v0_3_1.py` ani jej historyczny producent nie została tu odtworzona.

**HOLD:** zgodność z rzeczywistymi polami, producer-realizable 25-wymiarowa perturbacja, mierzalność 5 kalibracji powłokowych, pochodzenie oryginalnej symulacji i nowość teoretyczna/fizyczna. Nie implikuje to K/J3, TPE, GW, GR, PBH czy identyfikowalności operatora dynamicznego. Bez automatycznego rozszerzania programu. Przyjęcie właściciela Geeky/M15, wtórne AUD2 i potwierdzony zapis BW nie są w tej komórce założone.

**RETURN_ID:** `IW_REC11_ROT032_GEEKY_S12_ROT016_INDEPENDENT_EXACT_TWO_ACTIVE_GAIN_REFEREE_001_20261113`.

**VERDICT:** `PASS_GEEKY_ROT016_SCOPED / PASS_EXACT_ALL25_EPS1E7_TWO_ACTIVE / PASS_FULL_GAIN_WINDOW_QUADRATIC_THRESHOLD_LAW / PASS_49_RATIONAL_EXACT_INDEPENDENT_MINIMA / HOLD_PHYSICAL_PRODUCER / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.
