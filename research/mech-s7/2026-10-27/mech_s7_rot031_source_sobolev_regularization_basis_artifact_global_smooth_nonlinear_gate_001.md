artifact_id: MECH-S7-FRONTB-REGULARITY-BASIS-DEPENDENCE-DYNAMIC-GATE-031_20261027
exposure: PUBLIC
claim_ceiling: EXECUTED_CONDITIONAL_FINITE_BASIS_SOBLEV_IDENTITY_AND_NONLINEAR_REPLAY_NO_PHYSICAL_ADMISSION
sync_state: GITHUB_PENDING_BW_INGEST
return_id: MECH-S7-FRONTB-REGULARITY-BASIS-DEPENDENCE-DYNAMIC-GATE-031_20261027
owner_cell: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
problem_id: P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001
source_lock: Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d
status: CONDITIONAL_SCIENTIFIC_TEST_NO_EXEC

# MECH-S7 ROT031 — Regularity-basis confounder in finite source/target nullspace experiments

**27 października 2026.** Wykonawca: Mech-S7. Wynik obejmuje ścisły rachunek Sobolewa dla wybranej rodziny funkcji oraz rzeczywiście wykonane obliczenia źródła i warunkowej kinetyki ODE. Nie obejmuje oryginalnej symulacji Julia Wu–Xu, źródłowo zwalidowanych widm hadronowych M<10^9g, pełnej fizycznej prognozy BBN ani ograniczeń PBH.

## 0. Kontrola innych prac i punkt startowy

* Wu–Xu, kod oryginalny `Fenyutanchan/Primordial-Black-Hole`, commit `d395183674cace6c9906a8911bdeb7234ba4040d`. Oryginalna tabela `data/out/hadrons_from_PBH.dat` zaczyna się przy 10^9 g. Jej ekstrapolacja poniżej tego zakresu pozostaje niezwalidowana fizycznie.
* Mech-S7 ROT013 poprawił stan preedge; ROT020–022 ustaliły podatność znaku na stosunek antyproton/neutron i istotność aktywnego źródła; ROT023/024 badały momenty; ROT025–029 opisywały dopasowanie zależne od mapy i tła; ROT030 wykazał co najmniej 2-wymiarowe jądro dla 11 współczynników i 9 ograniczeń. Rachunek nie zastępuje oryginalnego 10D.
* Regularizacja Sobolewa, twierdzenie o rzędzie i jądrze macierzy, SVD i projektowanie funkcjonałów to dojrzała matematyka, nie oryginalne twierdzenia IW/NASH. Wynik ROT031 to specjalistyczny audyt konstrukcji źródła i jej skutków kinetycznych.

## 1. Ścisły defekt dyskryminacji gładkości w bazie ROT030

Niech `z=ln(M/10^9g)`, `L=ln(0.92/0.07)`, `h=L/N`. Na każdym z N rozłącznych, równych co do długości w z przedziałów rozważmy

`b_j(z)=sin^4(pi (z-z_j)/h)` wewnątrz j-tego przedziału, zero poza nim, `f(z)=sum_j c_j b_j(z)`.

Każdy `b_j` jest globalnie C³, funkcje mają rozłączne wnętrza nośników i tę samą normę po przeskalowaniu. Analiza całek na [0,pi] daje:

* `∫ sin^8 θ dθ = 35π/128`;
* `∫ [d(sin⁴θ)/dθ]² dθ = 5π/8`;
* `∫ [d²(sin⁴θ)/dθ²]² dθ = 4π`.

Stąd DOKŁADNIE dla każdego niezerowego wektora współczynników c przy danym N:

`||f'||₂/||f||₂ = 4π N/(sqrt(7) L)`;

`||f''||₂/||f||₂ = sqrt(512/35)*(πN/L)²`.

**Konsekwencja:** standardowe ilorazy regularności H¹/L² lub H²/L² są stałe we wszystkich kierunkach niezerowego jądra dla ustalonego N. Minimalizacja takich ilorazów NIE wyróżnia kierunku w rozłącznej bazie ROT030. Ich wzrost odpowiednio ∝N i ∝N² jest wymuszony przez zmniejszanie szerokości okien, nie przez zadane ograniczenia obserwacyjne.

Niezależny rachunek symboliczny powyżej i kwadratura Gaussa176 zgadzają się do względnej różnicy <6×10⁻¹⁵ dla N=10,11,13,15,21.

Dla N=11: `H¹/L²=20.2828120877`, `H²/L²=688.391263351`. Dla N=21: odpowiednio `38.7217321675`, `2508.93014163`. To **wynik ścisły tylko dla tej bazy**.

## 2. Alternatywa: globalnie gładka baza z tym samym zakresem i liczbą parametrów

Przy `x=2(z−z_mid)/L` w przedziale [-1,1] zbudowano 11 funkcji

`g_j(z)=(1−x²)^4 P_j(x)`, `j=0,...,10`,

gdzie P_j to wielomiany Legendre'a. Zarówno g_j, jak i ich pierwsze trzy pochodne zanikają na obu końcach, dzięki czemu rozbieżność źródła poza nośnikiem pozostaje C³ i dokładnie zerowa. Ta globalna baza ma 11 niezależnych współczynników.

Zbudowano 9-rowowy liniowy operator A z trzech momentów comoving emisji każdego gatunku (`j=0,1,2`) oraz sześciu funkcjonałów adjoint końcowego X_n dla χEM={0.25,0.5,0.75} × map={B_exec,B_sym}; wszystkie wiersze jednostkowo znormalizowano. Rząd A≤9 daje algebraicznie jądro o wymiarze co najmniej 2 przy 11 parametrach. W obrębie tego numerycznego jądra wybrano kierunek minimalizujący `||f''||²/||f||²` przez uogólnione zadanie wartości własnych. Żaden poziom tej procedury nie certyfikuje fizycznie funkcji adjoint.

**Wyniki dla N=11:**

| Norma | Lokalna sin⁴ ROT030 | Globalna (1−x²)^4·Legendre ROT031 |
|---|---:|---:|
| `||f'||₂/||f||₂` | 20.28281209 | 10.27215645 |
| `||f''||₂/||f||₂` | 688.39126335 | 111.30478343 |
| `||f||₂` (max|współczynniki/kształt| ~ 1) | 0.43199873 | 0.68496372 |
| RMS zmiany frakcji emisji przy eps=.15 | 0.04037486 | 0.06401712 |

Różnica ilorazów drugich pochodnych wynosi czynnik **6.1847** na korzyść globalnej bazy, mimo wyższej normy L². Przy zwiększaniu liczby globalnych modów N=10,11,13,15 zminimum `||f''||/||f||` spada ~112.97→111.30→107.17→104.19; w rozłącznej bazie rośnie N². Tym samym wzrost krzywizny z ROT030 NIE JEST nieuniknionym skutkiem liczby ograniczeń.

**Uwaga o certyfikacji:** 9×11 operator globalny ma najmniejszą wartość osobliwą około 2.79×10⁻¹³ i współczynnik uwarunkowania ~1.07×10¹³. Przy zastąpieniu czterech funkcji sprzężonych dokładniejszymi wariantami i zwiększeniu liczby węzłów maksymalny kąt główny między dwuwymiarowymi jądrami wynosi ~3.60°, a reszta wierszy normalizowanych dla kierunku pierwotnego ~2.76×10⁻¹¹. Są to silne ostrzeżenia przed nazywaniem orientacji jądra dokładnie wyznaczoną. Jądro ≥2 to osobne, ścisłe zdanie o dowolnej 9×11 macierzy.

## 3. Kontrola momentów i emisji

W obu konstrukcjach źródła stosujemy `Qpbar'=Qpbar+eps·(Qpbar+Qnbar)·f` i `Qnbar'=Qnbar−eps·(Qpbar+Qnbar)·f`.

Zatem **punktowa suma jest algebraicznie zachowana**. Przy eps=±.15 wszystkie próbkowane udziały pozostają dodatnie: najmniejszy udział źródła globalnego 0.34878953. Źródła pozostają niezmienione poza M∈[7×10⁷,9.2×10⁸]g, w szczególności dla M≥10⁹g; przy granicy nośnika zachowane są pochodne do rzędu 3.

Niezależna kwadratura 512-węzłowa daje dla GLOBALNEJ bazy względne reszty zachowania momentów `j=0,1,2`: `−6.81×10⁻¹²`, `+9.32×10⁻¹³`, `−3.26×10⁻¹⁴` (znakowane reszty dzielone przez całkę modułu zaburzenia). To **dokładność numeryczna**, nie ścisłe wyzerowanie dla wszystkich możliwych jąder, ponieważ kalibracyjny operator jest źle uwarunkowany. Dla lokalnej bazy niezależne całkowanie KAŻDEGO okna z osobna redukuje reszty do ≤1.22×10⁻¹⁶. Jedna niedostosowana kwadratura 512-punktowa na całym przedziale lokalnej bazy daje pozorne reszty ~5×10⁻⁸ — jest to wykryty artefakt kwadratury, nie fizyczna różnica.

## 4. Pełna nieliniowa warunkowa kinetyka

Zachowano odziedziczony poprawiony transport stanu source-active ROT013, warunkowy 7D subedge/postsource ROT024, oryginalne surowe cztery gałęzie archiwalne Wu–Xu oraz te same współczynniki T, barionów i interakcji, co w ROT030. Jedyną nową zmianą jest funkcja kształtu rozdziału emisji pbar/nbar.

Wykonano 30 stanów ODE (5 teł χEM={0,.25,.5,.75,1} × 2 mapy × eps={0,+.15,−.15}). Poniżej maksymalna wartość modułu zmiany X_n przy T_nuc dla każdego tła:

| χEM | B_exec GLOBAL ROT031 | B_sym GLOBAL ROT031 | Global/Local ROT030, exec | Global/Local ROT030, sym |
|---:|---:|---:|---:|---:|
| 0 | 3.542×10⁻¹⁰ | 1.086×10⁻¹⁰ | 5.69× | 4.45× |
| .25 | 3.528×10⁻¹⁰ | 1.092×10⁻¹⁰ | 5.53× | 4.44× |
| .5 | 3.509×10⁻¹⁰ | 1.071×10⁻¹⁰ | 5.64× | 4.38× |
| .75 | 3.466×10⁻¹⁰ | 1.066×10⁻¹⁰ | 5.71× | 4.33× |
| 1 | 3.446×10⁻¹⁰ | 1.061×10⁻¹⁰ | 5.62× | 4.40× |

Nowe źródło ma jednak większą normę L² (stosunek 0.685/0.432 ≈1.585), więc NIE należy interpretować powyższych stosunków jako efektu samej gładkości przy identycznej normie źródła. Także po podzieleniu wyniku przez RMS zmiany frakcji źródła różnica odpowiedzi pozostaje większa dla globalnej bazy (około 2.73–3.60×). **Dodatkowe wygładzenie zmniejsza krzywiznę, ale nie gwarantuje poprawy przybliżonej wystarczalności dla celu.**

W 12 stanach χEM=0,1 obu map przy rtol=3×10⁻¹⁰ zamiast 3×10⁻⁹ maksymalna różnica ΔX_n końcowego wyniosła `9.625×10⁻¹³`; reszty nieliniowe ~10⁻¹⁰ są wyraźne wobec tak przetestowanej zmiany tolerancji. Izolowane powtórzenie trzech stanów χ=0, B_exec (z pustego katalogu z wyłącznie wejściami i kodem) dało identyczne tekstowo wartości stanu Xnuc, Xcut, ΔXnuc, ΔXcut, liczby kroków i epsilon. Pozostałych 27 stanów nie nazywamy osobno odtworzonymi w pustym katalogu.

## 5. Decyzja naukowa, ograniczenia i falsyfikatory

**NEGATIVE KNOWLEDGE:** (A) metoda karania rozłącznych równych okien przez ilorazy H¹/H² nie wybiera kierunku; (B) rosnąca liczba okien niesie sztuczny koszt krzywizny ∝N²; (C) brak jądra w 7-binowej przestrzeni nie jest brakiem jądra dla bogatszych źródeł; (D) sama poprawa regularności widma nie oznacza mniejszej odpowiedzi końcowej; (E) numeryczna orientacja globalnego jądra jest niepewna przy źle uwarunkowanych gradientach.

**POSITIVE SCIENCE:** globalna C³ baza przy 11 parametrach daje >6× mniejszy iloraz drugiej pochodnej/L² przy zachowaniu bardzo małej odpowiedzi w badanych dziesięciu komórkach (5 teł × 2 mapy), ale reszta jest wielokrotnie większa niż w lokalnej bazie.

**FALSIFIERS / REQUIRED NEXT:** niezależne dokładne funkcje sprzężone w oryginalnej Julii i autentyczne hadronowe widma dla M<10⁹g, a następnie zestawienie rozdzielonego budżetu: regularność funkcji źródła, niepewność operatora, błąd liniowego dopasowania, reszta nieliniowa i zależność od tła. Nie twierdzić, że nowe gładkie widma są fizycznie bardziej prawdopodobne.

STOP: `ORIGINAL_JULIA_10D_NOT_EXECUTED / SOURCE_VALID_E2B_OPEN / BW_INGEST_PENDING / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_Yp_DH / NO_PBH_BOUND`.

## 6. Reproducibility and source typing

Pakiet `MECH_S7_ROTATION_031_REPRODUCIBILITY_20261027.zip` jest samowystarczalny: kod `audit_smoothness_and_basis_031.py`, `test_global_smooth_basis_031.py`, `validate_global_source_ode_031.py`, `independent_validation_031.py`, zależności `test_multibin_ode_030.py` i `reproduce_high_order_moment_gate_024.py` i wcześniejsze, surowe archiwa Mech-S6, kopie source-pinned źródeł danych i funkcji sprzężonych, pełne CSV, JSON i SHA256. Uruchomić z korzenia rozpakowanego katalogu przy zainstalowanych numpy, scipy. Skrypty 031 wymagają wejściowych archiwów i funkcji sprzężonych, nie wymagają prywatnego dostępu do GitHub/Drive ani repozytorium Julii. Nie obejmują samodzielnej fizycznej reprodukcji oryginalnego źródła hadronów.

GitHub public report != BW ingestion != owner acceptance != external referee PASS != EXEC. Wszelkie podniesienie statusu zastrzeżone przez Moderatora.