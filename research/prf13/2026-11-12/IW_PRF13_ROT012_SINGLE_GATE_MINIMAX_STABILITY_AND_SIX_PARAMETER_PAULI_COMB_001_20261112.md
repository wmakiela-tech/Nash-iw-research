---
artifact_id: IW_PRF13_ROT012_SINGLE_GATE_MINIMAX_STABILITY_AND_SIX_PARAMETER_PAULI_COMB_001_20261112
created_at: 2026-11-12
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_12 / PRF13
problem_id: PRF13_ROT011_SIX_DIMENSION_PAULI_MEMORY_COEFFICIENT_SINGLE_GATE_STABILITY
exposure: PUBLIC
source_type: TWO_TIME_CLASSICAL_PAULI_LABEL_QUANTUM_COMB_AND_EXACT_SO3_MINIMAX_THEOREM
sync_state: LOCAL_AUTHOR_ARCHIVE_GITHUB_PENDING_BW_PENDING
status: AUTHOR_EXACT_SYMBOLIC_REPRODUCED / INDEPENDENT_SAME_CELL_NUMERIC_FALSIFIER_PASS / EXTERNAL_REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_GENERAL_PROCESS_TENSOR_TOMOGRAPHY / NO_HARDWARE / NO_ALL_QUMULTI_TIME_MEMORY / NO_3Q_LOCC_CLOSURE / NO_CROSS_FIELD_PHYSICAL_BRIDGE / NO_CANON / NO_EXEC_SIGN
---

# PRF13 ROT012 — minimax stabilne odtwarzanie sześciu ukrytych korelacji dwuczasowego szumu Pauliego jedną bramką

**Data:** 12 listopada 2026 r. **Funkcja:** PRF13 — independent science rotation following LT8-THEORY-010-PRF. **Status:** wynik autorski, dokładnie reprodukowany, niezależna recenzja oczekuje. **Główna treść:** w wąskiej, zdefiniowanej już w ROT011 klasie dwóch kolejnych kanałów kubitowych z losowymi klasycznymi etykietami Pauliego istnieje jedna bramka unitarna osiągająca **globalnie optymalną (w klasie wszystkich pojedynczych bramek unitar­nych) minimalną czułość** przy sześciu współrzędnych pamięci niewidocznych dla kanałów pierwszego, drugiego i końcowego bez interwencji. To problem projektowania ograniczonej tomografii, nie oryginalny uniwersalny opis pamięci.

## 0. Źródła i prior-art subtraction

**Właściciel oryginalnej klasy:** PRF13 ROT009, dokładny falsyfikator LT8-THEORY-010-PRF dla pary przyczynowych dwuczasowych combs; publiczny raport: https://github.com/wmakiela-tech/Nash-iw-research/blob/4d8041e24962978d0aeba05029dae8a2f96abaf4/research/prf13/2026-11-12/IW_PRF13_LT8_THEORY_010_PRF_TWO_TIME_CAUSAL_COMB_INTERVENTION_FALSIFIER_001_20261112.md

**Bezpośrednie wejście:** PRF13 ROT011, exact 16→10+6 Fourier kernel, sześć pomiarów i bramka V_old: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf13/2026-11-12/IW_PRF13_ROT011_SIX_DIMENSION_PAULI_HIDDEN_MEMORY_TOMOGRAPHY_PUBLIC_RETURN_001_20261112.md ; źródłowy kod Python: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf13/2026-11-12/IW_PRF13_ROT011_FOURIER_KERNEL_AND_GENERIC_GATE_EXACT_PUBLIC_REPRO_001_20261112.py

**Kontekst dojrzalej teorii (konkurencyjny, bez pierwszeństwa):**
- Chiribella, D'Ariano, Perinotti, *Theoretical Framework for Quantum Networks*, Phys. Rev. A 80, 022339 (2009), DOI 10.1103/PhysRevA.80.022339 — kwantowe combs i warunki przyczynowe.
- Pollock et al., *Non-Markovian quantum processes: Complete framework and efficient characterization*, Phys. Rev. A 97, 012127 (2018), DOI 10.1103/PhysRevA.97.012127 — pełna operacyjna informacja w tensorze procesu.
- White et al., *Non-Markovian Quantum Process Tomography*, PRX Quantum 3, 020344 (2022), DOI 10.1103/PRXQuantum.3.020344 — restricted process tensors i tomografia ograniczona do przestrzeni interwencji; to ważny dojrzały HOST dla celu ROT012.
- Gazit, Ng, Suzuki, *Quantum process tomography via optimal design of experiments*, Phys. Rev. A 100, 012350 (2019), DOI 10.1103/PhysRevA.100.012350 — teoria projektowania eksperymentu przy ograniczonych zasobach i parametrach nuisance.
- Nunn et al., *Optimal experiment design for quantum state tomography*, Phys. Rev. A 81, 042109 (2010), DOI 10.1103/PhysRevA.81.042109 — dojrzałe kryteria jakości projektu. Problem ROT012 jest źródłowym przykładem elementarnej liniowej kondycjonowalności, nie twierdzeniem o ogólnym OED.
- Related but not identical SO(3) matrix extremum (minimum *maximum* absolute entry, not our maximum *minimum offdiagonal*): https://mathoverflow.net/questions/508520/for-which-n-is-the-minimum-max-entry-of-an-n-by-n-orthogonal-matrix-known-is-n3-already-an-open-problem . Macierz z równymi wartościami 1/3 i 2/3 pojawia się już w klasycznej algebrze ortogonalnej. **NO PRIORITY CLAIM.**

## 1. Zamrożony legalny fizycznie matematyczny model

Jedna realizacja składa się z dwóch czasowych zastosowań jednostkowych Pauliego na tym samym kubicie, z jednym legalnym kontrolnym CPTP pomiędzy nimi:

    rho -> U_v rho U_v† -> Ad_V -> U_w (...) U_w†,
    U_(a,b) = X^a Z^b, (v,w) ∈ G×G, G=F_2²,
    p(v,w)>=0, Σ_(v,w) p(v,w)=1.

Etykiety szumu p są zewnętrzne (exogenous), nie zależą od późniejszej interwencji; na kolejnych niezależnych realizacjach są ponownie losowane z tego samego p **tylko w części dotyczącej liczby prób statystycznych**. Dopuszczalne są korelacje v,w wewnątrz pojedynczej realizacji; każdy proces jest przyczynowy CP, bo jego Choi comb to dodatnia kombinacja J(U_v)⊗J(U_w), ze standardową normalizacją warunków przyczynowych. Nie jest to model dowolnego środowiska kwantowego ze sprzężeniem zwrotnym ani pełnej wieloczasowej fizyki.

Używamy czterech charakterów sprzężenia Pauliego χ_0=1, χ_X(a,b)=(-1)^b, χ_Y(a,b)=(-1)^(a+b), χ_Z(a,b)=(-1)^a. Fourierowskie współrzędne:

    C_(a,b)(p)=Σ_(v,w) p(v,w) χ_a(v)χ_b(w).

Z ROT011: pierwsza marginalna CPTP daje C_(a,0), druga daje C_(0,b), brak interwencji daje C_(a,a). Liczba niezależnych znanych współrzędnych =10 (wraz z C_00=1), więc *sześć pozostałych* to wszystkie C_(a,b) dla a,b∈{X,Y,Z}, a≠b. Konstrukcja p_ε=[1+ε χ_a(v)χ_b(w)]/16, |ε|≤1, pokazuje legalność sześciu niezależnych kierunków w pobliżu p0.

## 2. Dokładna macierz pomiaru dla jednej bramki

Niech V jest dowolną ustaloną bramką na jednym kubicie, a R(V)∈SO(3) jej rzeczywistą macierzą obrotu w bazie (X,Y,Z):

    V σ_j V† = Σ_i R_ij(V) σ_i.

Dla każdej pary i,j∈{X,Y,Z} przygotuj +1 eigenstate σ_j, wstaw V pomiędzy etapy szumu i wykonaj końcowy pomiar σ_i∈{±1}. Dokładna średnia eksperymentu wynosi:

    T_ij(p;V) = E[σ_i | prep +j, V] = R_ij(V) C_(j,i)(p).   (2.1)

**Dowód:** pierwszy Pauli U_v daje σ_j→χ_j(v)σ_j, sprzężenie przez V wprowadza R_ij, a ostatni U_w daje σ_i→χ_i(w)σ_i. Średnia po p równa się deklarowanemu iloczynowi. Dla i≠j każda z sześciu obserwacji zawiera tylko jedną z sześciu ukrytych korelacji; brak interferencji współrzędnych. Co ważne, (2.1) zachodzi dla **dowolnego p** w tej klasie — nie wymaga znanych pozostałych dziesięciu współrzędnych, choć do pełnej inwersji p te pozostałe dane są niezbędne.

Definiujemy source-typed kryterium projektowania jednej stałej bramki przy sześciu niezależnych ustawieniach wejście/wyjście i jednakowym bezwzględnym błędzie średniej:

    μ(V) = min_(i≠j) |R_ij(V)|,   κ∞(V) = 1/μ(V).

Gdy μ=0, jeden z sześciu parametrów jest niewidoczny. Gdy μ>0, ΔC_(j,i)=ΔT_ij/R_ij, a maksymalna amplifikacja jednostajnego błędu jest dokładnie κ∞. **Nie jest to pełna liczba uwarunkowania proces-tensor ani optymalność dowolnych strategii z wieloma bramkami, ancillami i kolektywnym POVM.**

## 3. Twierdzenie ROT012.1 — globalne minimax optimum wszystkich pojedynczych unitarnych V

Niech

    V* = -i (X+Y+Z)/sqrt(3),
    R* = R(V*) = (1/3) [ [-1, 2, 2], [2, -1, 2], [2, 2, -1] ].

**Twierdzenie:**

    max_(V unitary qubit) μ(V) = 2/3,   min_(V) κ∞(V) = 3/2.  (3.1)

Wszystkie sześć niewidocznych korelacji ma identyczną czułość 2/3. Matryca R* jest ortogonalna, det=1, a V* jest unitarną bramką SU(2), obrotem o π wokół osi (1,1,1)/sqrt(3).

**Krótki globalny dowód optymalności bez optymalizatora:** Przypuść, że pewna rzeczywista macierz ortogonalna O 3×3 ma |O_ij|>2/3 dla wszystkich i≠j. Z normalizacji każdego wiersza: |O_11|,|O_22|,|O_33|<1/3. Z kolei dopełnienie algebraiczne i O^-1=O^T, det O=±1, dają identyczność modułów

    |O_11| = |O_22 O_33 - O_23 O_32|.

Ponieważ |O_23 O_32|>4/9 i |O_22 O_33|<1/9, prawa strona jest >1/3, w sprzeczności z |O_11|<1/3. Wobec tego μ(O)≤2/3 dla każdego O∈O(3), a R* osiąga równość. QED.

Zatem twierdzenie obowiązuje nawet przy powiększeniu klasy z SO(3) do O(3) w sensie algebraicznym, ale fizyczna implementacja pojedynczą unitarną bramką ma SO(3). Nie twierdzimy o unikalności optymalnego R ani o nowości tego ekstremum.

**Porównanie z ROT011:** jego V_old=(I−i(X+Y+2Z))/sqrt7 ma R_old=(1/7)[[-3,-2,6],[6,-3,2],[2,6,3]], z μ_old=2/7 i κ∞_old=7/2. W ROT012 μ*=2/3, κ∞*=3/2, dokładna poprawa najgorszego wzmocnienia = (7/2)/(3/2)=7/3. Zmiana liczby sześciu ustawień: zero.

## 4. Stabilność względem szumu statystycznego i błędów bramki

**Model pomiarowy do części statystycznej:** Każdy z sześciu eksperymentów powtarza się niezależnie n razy z ponownym losowaniem v,w ze stałego p, znaną bramką V*, prawidłową preparacją wejścia i idealnym pomiarem Pauliego. Każdy wynik Y_ij,k ma wartości ±1 i średnią (2/3) C_(j,i). Definiuj średnią empiryczną T_hat i estymator C_hat=(3/2)T_hat.

Z nierówności Hoeffdinga dla zmiennej ±1, przy każdym ustawieniu P(|T_hat−T|>t)≤2 exp(−nt²/2). Po połączeniu sześciu nierówności (union bound), z prawdopodobieństwem ≥1−α jednocześnie:

    max_(i≠j)|C_hat_(j,i)−C_(j,i)| ≤ (3/2)sqrt(2 log(12/α)/n).  (4.1)

Dla dokładności absolutnej ε każdej współrzędnej wystarczy

    n≥ceil( [9/(2ε²)] log(12/α) )       (każde z sześciu ustawień). (4.2)

Przy ε=.05, α=.01: n*=12 763, razem 76 578 indywidualnych zarejestrowanych bitów; dla V_old najgorszy współczynnik 2/7 wymagałby na tej samej bazowej nierówności n_old=69 483, razem 416 898 bitów. Stosunek liczby prób w asymptotycznym górnym oszacowaniu = 49/9≈5.444. To porównanie **konserwatywnych wymaganych liczb prób przy tym samym prostym algorytmie**, nie twierdzenie o rzeczywistym optimum fizycznego kosztu czy przewadze nad wszystkimi strategiami kwantowymi. Dane i liczby są syntetyczne.

**Błędy bramki:** jeśli fizyczne sprzężenie odpowiada bramce V~ z macierzą R~ i niezależny gate-audit potwierdza max_ij |R~_ij−R*_ij|≤η, to rzeczywista najgorsza czułość ≥2/3−η. Jeśli używamy poprawnie zidentyfikowanego R~, uwarunkowanie wynosi co najwyżej 1/(2/3−η) przy η<2/3. Jeśli błędnie wstawiamy idealne R* bez rekalibracji, pojedynczy estymator może mieć systematyczny błąd ≤(3/2)η, ponieważ |C_(j,i)|≤1. Bez audytu dryfu bramki i kanału odczytowego nie wolno deklarować gwarancji sprzętowej.

**Inwersja do p:** jeśli dziesięć współrzędnych zwykłych kanałów jest dokładnie znanych, pełne p odzyskuje odwrócona transformata skończonej grupy:

    p(v,w) = (1/16) Σ_(a,b∈{0,X,Y,Z}) C_(a,b) χ_a(v) χ_b(w).   (4.3)

Dla błędów tylko sześciu nieznanych współrzędnych c∈R⁶, z ortogonalności charakterów:

    ||p_hat−p||_1/2 ≤ (1/2)||c_hat−c||_2 ≤ (sqrt6/2)ε.      (4.4)

Gdy estymator liniowy p_hat zawiera małe ujemne elementy, pierwsza wielkość pozostaje połową normy L1 *podpisanej różnicy*, a nie TV dwóch legalnych rozkładów; można następnie rozważyć legalną projekcję do simplex pod odpowiednimi ograniczeniami. Nie ogłaszamy gwarancji pomiarowej pełnego comb, jeśli zwykłe dziesięć współrzędnych są tylko przybliżone lub model Pauli nie obowiązuje.

## 5. Test falsyfikacyjny, negatywna wiedza i granica naukowa

- ROT011 A rank=10 i nullity=6 — ponownie odtworzona dokładnie; sześć niezależnych charakterów leży w ker A.
- Unitarność V*, SO(3), R*=2J/3−I oraz sześć odczytów dla dodatniego, niestacjonarnie nienaruszonego *wewnątrz pary* modelu p z rzeczywistymi niezerowymi sześcioma współczynnikami — dokładna arytmetyka SymPy PASS.
- Cały 16-elementowy rozkład p odtworzony odwróconą transformacją Fouriera, PASS.
- Niezależny NumPy test 16×16 Choi comb: eigenvalues PSD w tolerancji numerycznej, causal partial traces oraz legalne 2×2 macierze sprzężeń: PASS (drugie obliczenie autorskie tej samej komórki, NIE referee).
- Próba znalezienia kontrprzykładu w 100 000 losowo wygenerowanych SO(3): PASS diagnostic (najlepsze μ≈0.659216 < 2/3). Nie zastępuje dowodu §3.
- Symulowany z góry ustalony seed i n=12 763 prób w każdej z sześciu klas: maksymalny błąd współrzędnej <0.05; PASS diagnostic, a nie obserwacja aparatu.

**Falsyfikatory:** pojedyncza macierz O(3) z μ>2/3 obalałaby twierdzenie §3; dowolny dodatni rozkład Pauli p naruszający (2.1) obalałby model/test; zależność szumu od wyboru V, koherencja środowiska niedająca się reprezentować przez exogenous p(v,w), reset lub nieznany drift podważałaby transfer do aparatu. Nie wolno przenosić tego wyniku do ogólnych tensorów procesu, przypadków bez Pauli-kowariancji, NCDG, teorii unifikującej LT8 ani pełnego LOCC. Zamiast tego wynik stawia praktyczne źródłowo testowalne pytanie: **czy dana aparatura rzeczywiście realizuje klasyczny stacjonarny dwuczasowy Pauli-label comb z niezależną kalibracją V?** Jeśli nie, obowiązuje ABSTAIN dla fizycznej interpretacji parametrów C.

## 6. Powtarzalność i status

Źródło logiczne jest integralne bez optymalizatora. Dokładny kod: `IW_PRF13_ROT012_SINGLE_GATE_MINIMAX_STABLE_PAULI_MEMORY_TOMOGRAPHY_REPRO_001_20261112.py` — Python 3, SymPy; osobny `IW_PRF13_ROT012_INDEPENDENT_COMB_AND_SO3_FALSIFIER_AUDIT_001_20261112.py` — Python 3, NumPy, stały seed; dołączone bezpośrednie logi i manifest SHA-256. Weryfikacja GitHub musi zostać oznaczona dopiero po realnym readbacku; BW, LT8 i niezależny referee pozostają otwarte.

**RETURN:** `PRF13_ROT012 / SOURCE_RESTRICTED_TWO_TIME_PAULI_COMB / SIX_DIMENSION_HIDDEN_FIBER_REDERIVED / SINGLE_FIXED_GATE_MINIMAX_SENSITIVITY_MU_2_OVER_3 / EXPLICIT_SIX_SETTING_HOEFFDING_STABILITY / AUTHOR_REPRODUCED / NO_NOVELTY / NO_HARDWARE / NO_CANON / NO_EXEC_SIGN / INDEPENDENT_REFEREE_PENDING`.
