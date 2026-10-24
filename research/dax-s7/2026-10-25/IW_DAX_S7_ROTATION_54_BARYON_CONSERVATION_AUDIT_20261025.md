# IW/NASH — DAX-S7 — obrót 54

**Tytuł:** Stały stosunek barionów do fotonów a zachowanie liczby barionowej — niezależny audyt źródłowy, rachunek całkowy i kontrola wpływu na mapowanie obserwacyjne

**Data:** 2026-10-25  
**Status:** `SOURCE_FORMULA_VERIFIED / EXACT_COMOVING_BARYON_CONSISTENCY_TEST / SOURCE-TABLE_NUMERICAL_PORT / CONDITIONAL_ACCEPTANCE_SENSITIVITY / FULL_JULIA_NOT_RUN / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_NOVELTY_INFERENCE`.

## 1. Cel

Po obrotach 52–53, które odtworzyły skan `X_n(T_nuc)` w przybliżeniu quasi-stacjonarnym, zbadać *niezależną* od wzoru helowego zależność tych rezultatów od normalizacji liczby barionów. Nie zakładać, że poprzednie wyniki stanowią fizyczne ograniczenia PBH.

## 2. Niezmienione źródła

Repozytorium [Fenyutanchan/Primordial-Black-Hole](https://github.com/Fenyutanchan/Primordial-Black-Hole), folder `arXiv-2509.05618`:

- `main-scan.jl`, blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`: kod zawiera **dosłownie** `n_γ = 2 * ζ₃ * T_SM^3 / π^2` i `n_B = η_B * n_γ`; `n_B` występuje w stratach hadronów przez rozpraszanie i anihilację. Osobno PBH są rozcieńczane jako `n_PBH = n_PBH_ini*(a_ini/a)^3`.
- `tool_script-parameters.jl`, blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`: `η_B=6.1e-10`, `T_nuc=0.078185270688319950 MeV`, parametry reakcji.
- `data/ext/N_around_m_e.csv`, blob `93f2494f026c5d0587ea40fe08bb938dd9d01fa8`, 1000 wierszy.
- `data/ext/N_s_from_PDG2024.csv`, blob `33aceb876fc36cb2486d36c690e6401d85d76b46`, 89 wierszy.
- `data/ext/N_rho_OVER_N_s_from_PDG2024.csv`, blob `28b0c13563d7b3bdeaee191a3a981197345d05b8`, 82 wiersze.
- `data/out/hadrons_from_PBH.dat`, blob `06d0883a27b108692720422294ba2baacd381a64`, 100 wierszy emisji.

Wszystkie cztery tablice obliczeniowe odczytano z repozytorium źródłowego poprzez GitHub; obliczenia pełnego skanu porównawczego wykonano w niezależnym JavaScript z oryginalnymi wierszami danych. Lokalny skrypt Python stanowi przygotowaną reimplementację do ponownego uruchomienia na czterech tabelach, ale w tej rotacji *nie wykonano* nim pełnego numerycznego odtworzenia, gdyż oryginalne tablice nie zostały zamontowane w jego lokalnym katalogu.

## 3. Ścisła diagnoza zachowania liczby barionowej

Źródło zadaje `n_B=η_B*(2 ζ(3)/π²)T³` z *jednym stałym* `η_B`, dlatego w dowolnej historii ekspansji

\[
\frac{d\ln(n_Ba^3)}{d\ln a}=3+3\frac{d\ln T}{d\ln a}.
\]

Wybierając reżim kontrolny bez PBH, oznaczmy `r=dln g_rho/dlnT`, `s=dln g_s/dlnT`. Źródłowe chłodzenie ma

\[
C_{\rm code}=\frac{d\ln\rho_{\rm SM}}{d\ln a}=-4+\frac{r}{3+s}, \qquad \frac{d\ln T}{d\ln a}=\frac{C_{\rm code}}{4+r}.
\]

Stąd **dokładnie dla źródłowego prawa chłodzenia**:

\[
\boxed{\frac{d\ln(n_Ba^3)}{d\ln a}=\frac{3r(4+s)}{(3+s)(4+r)}}.
\]

Fizyczny warunek zachowania netto liczby barionowej to zero prawej strony, jeżeli nie ma baryogenezy i barionowego źródła netto. **Stały `η_B` nie wystarcza do jego spełnienia.** Przy adiabatycznej ewolucji całkowitej entropii analogiczna pochodna wynosi `3s/(3+s)` i także jest zazwyczaj niezerowa dla wymuszonego `η_B=const`. Te dwa testy różnią się co do wielkości, ale wskazują ten sam problem definicyjny. Jest to standardowa konsekwencja rozcieńczania barionów i ogrzewania fotonów, nie twierdzenie o nowym efekcie fizycznym.

### Test ilościowy bez PBH

Obydwie definicje `n_B` znormalizowano identycznie w `T_nuc`. Referencyjna gęstość o zachowanej liczbie współporuszającej to:

\[
n_B^{\rm cons}(a)=\eta_B n_\gamma(T_{\rm nuc})\left(\frac{a_{\rm nuc}}a\right)^3.
\]

`a(T)` odtworzono przez całkowanie źródłowych funkcji `g_rho(T)`, `g_s(T)` i `C_code` na 1000-węzłowej tablicy z rachunkiem Simpsona w segmentach liniowych w `ln T`. Otrzymano `n_B^code/n_B^cons`:

| `T` [MeV] | `n_B^code/n_B^cons` | `n_B^cons/n_B^code` |
|---:|---:|---:|
| `0.07818527` | `1.000000` | `1.000` |
| `0.10` | `0.864205` | `1.157` |
| `0.15` | `0.622819` | `1.606` |
| `0.30` | `0.416396` | `2.402` |
| `0.50` | `0.369704` | `2.705` |
| `1.00` | `0.350358` | `2.854` |
| `10.0` | `0.344143` | `2.906` |

Kontrola niezależna: przy adiabatycznym `g_sT³a³=const` analogiczny stosunek wynosi `g_s(T_nuc)/g_s(T)`; dla `T=10 MeV` około `0.394657`. Odrębność `0.344143` i `0.394657` pokazuje wkład wcześniejszej rozbieżności praw chłodzenia; brak zachowania `n_Ba³` nie jest wyłącznie jej artefaktem.

**Ważna normalizacja:** przyjmujemy, że `η_B=6.1e-10` odnosi się do późnej epoki `T_nuc`. Przy innej konwencji dla definicji parametru `η_B` potrzebna byłaby osobna kalibracja; nie wprowadzono tu dowolnego parametru barionowego do oryginalnej przestrzeni skanu.

## 4. Test numeryczny z PBH: jeden background, dwie definicje `n_B`

- Stała masa PBH `M_f=9.6725e9 g` **spoza** oryginalnej 100-punktowej siatki mas, `β` od `0` do `1e-17`.
- Tło: źródłowe równanie `dln rho_SM/dln a`, `H(rho_SM+rho_PBH)`, `M³(t)`; te same tabele efektywnych stopni swobody i odwrotnego interpolatora `rho -> T`.
- Sześć hadronów: źródłowe emisje, przekroje czynne i **przybliżenie quasi-stacjonarne** `n_h=S_h/D_h` (nie pełna ewolucja sześciu gęstości).
- Dla każdej wartości `β` oba warianty neutronów biegną na **tej samej** numerycznej trajektorii tła (`12000` kroków przed przejściem do zmiennej masowej oraz `16000` kroków w końcowym etapie), mają to samo początkowe `X_n` i tę samą emisję PBH; zmienia się wyłącznie `n_B` w zaniku/reakcjach hadronów.
- Referencję `a_nuc` wyznaczono z **pierwszego** przecięcia `T=T_nuc`. Nie jest to dodatkowa niezależna zmienna fizyczna. Dla `β=0` identyczność obu neutronowych rozwiązań jest kontrolą zerowego wkładu hadronowego.

| `β` | `X_n` źródło | `X_n` z `n_Ba³=const` | `ΔX_n` |
|---:|---:|---:|---:|
| `1e-20` | `0.10958180` | `0.10949228` | `−0.00008952` |
| `5e-20` | `0.11176874` | `0.11132379` | `−0.00044495` |
| `1e-19` | `0.11448334` | `0.11360003` | `−0.00088330` |
| `2e-19` | `0.11984967` | `0.11810915` | `−0.00174052` |
| `3e-19` | `0.12513332` | `0.12256106` | `−0.00257226` |
| `5e-19` | `0.13545804` | `0.13129633` | `−0.00416171` |
| `1e-18` | `0.15991758` | `0.15218773` | `−0.00772985` |

Wartość `X_n` przy `β=0` w obu modelach jest taka sama (`0.10903294`); porównanie ze skanem w obrocie 53 dla pierwotnego `n_B` odpowiada zgodności rzędu `10^-6` przy porównywalnej, lecz nieidentycznej siatce kroku. Ta zgodność nie zastępuje ścisłego testu zbieżności nowego wariantu ani oryginalnego rozwiązania Julia.

Dla `β=3e-19`: `Yp_mass≈2X_n` przesuwa się z `0.25026663` do `0.24512211`, czyli o `−0.00514452` (około `1.71σ` dla obserwacyjnego `σ=0.003`). Dla tej samej próbki kodowa obserwabla `2X/(1-X)` zmienia się z `0.28606259` do `0.27936087` (również warunkowo).

## 5. Test przesunięcia przybliżonych przedziałów akceptacji

Na podstawie 14 wyników skanu i monotonicznej PCHIP (`log10 β` jako funkcja obserwabli), stosując `Yp=0.245±3×0.003` oraz ograniczając `β` do źródłowego `[1e-20,1e-17]`:

| Obserwabla | Źródłowe `n_B` — 3σ | `n_Ba³=const` — 3σ |
|---|---:|---:|
| `Yp_code=2X/(1-X)` | `[1e-20, 6.694e-20]` | `[1e-20, 8.003e-20]` |
| `Yp_mass≈2X` | `[1.645e-19, 3.352e-19]` | `[1.975e-19, 4.014e-19]` |

Przesunięcia granic wynoszą około **20% w β**. Nadal zachodzi rozłączność obydwu przedziałów 3σ; poprawa samej liczby barionowej **nie usuwa** niezależnego problemu mapowania `Yp` wskazanego w obrocie 53.

Przedziały są **warunkowymi zakresami zgodności surrogate**, nie granicami na PBH w publikacji; interpolator PCHIP nie daje certyfikowanych granic bifurkacji, a `2X_n` nie jest pełną siecią nuklearną.

## 6. Zastrzeżenia i ryzyka nadinterpretacji

1. Źródłowe `n_B` może być świadomym uproszczeniem fenomenologicznym; stwierdzono **niespełnienie testu zachowania liczby barionowej przy przyjętej interpretacji `η_B`**, nie wykazano zamiarów autorów ani błędu opublikowanych figurek.
2. Poprawka normalizuje `η_B` przy pierwszym `T_nuc`; pełna walidacja wymaga uzgodnienia z obserwowanym stosunkiem baryon/foton po zmianach entropii, w szczególności dla silnego PBH reheating.
3. Źródłowy hadronowy kod ma także niezależny problem braku terminu `−3Hn_h` w równaniu liczby hadronów (obrót 28). Tego elementu nie zmieniano, aby wyizolować jedną zmienną.
4. Hadronowe strumienie niskoenergetyczne są **ekstrapolowane** poniżej `M=1e9 g`; przy części akceptowanych β pierwotna masa PBH w chwili `T_nuc` także jest mniejsza od granicy tablicy. Test nie waliduje tego obszaru fizycznie.
5. Nadal nierozstrzygnięte: poprawność źródłowej termodynamiki chłodzenia, mapping helu z obrotów 29–33, stabilność solvera na zakręcie temperatury, rzeczywista sieć BBN. Nie sumować dowolnie przesunięć 20% z niezależnymi błędami.
6. **Nie uruchomiono pełnego `main-scan.jl` w Julia ani pełnego source-equation wariantu Python dla korekty na lokalnych czterech tablicach.** Liczby skanu pochodzą z pełnotabelarycznego JS-portu, niezależnie od kodu reprodukcyjnego w Python.

## 7. Reprodukcja i falsyfikatory

W pakiecie znajdują się:

- `IW_DAX_S7_ROTATION_54_BARYON_DENSITY_SENSITIVITY_20261025.csv` — wszystkie 14 numerycznych przypadków, `X_n` i obydwa obserwable;
- `IW_DAX_S7_ROTATION_54_BARYON_DENSITY_SENSITIVITY_20261025.json` — wyniki PCHIP i provenance;
- `IW_DAX_S7_ROTATION_54_BARYON_CONSERVATION_RECOMPUTE_20261025.py` — samodzielny skrypt bazujący na reimplementacji r52, pobierający/verifikujący cztery oryginalne tablice i wykonujący dwukrotną rekonstrukcję (pierwszy przebieg ustala `a_nuc` z tła, kolejne badają `source` i `conserved`). `--selftest` i kontrola składni: **PASS**; pełne `--download` i przebieg solvera Python na oryginalnych tabelach: **NOT RUN** w tym środowisku.

**Bezwzględny falsyfikator:** uruchomić oryginalną Julię przy tych samych punktach `(M,β)` w dwóch ramionach, modyfikując jedynie `n_B`: raz `η_B n_gamma(T)`, raz `η_B n_gamma(T_nuc)*(a_nuc/a)^3`; obliczyć poprawnie `a_nuc` z pierwszego niezależnego przebiegu tła. Zmiany ocenić po porównaniu pełnych populacji sześciu hadronów i dwóch surowych trajektorii `X_n`, **bez** wprowadzania `Yp` do równania. Rozdzielić znane terminy `−3H n_h`, wpływ reheat i niezależną sieć reakcji BBN.

**Próg roszczenia:** `SOURCE-NATIVE CONSERVATION-DIAGNOSTIC + CONDITIONAL NUMERICAL SENSITIVITY`, bez upgrade do opublikowanych ograniczeń PBH, `NO_CANON / NO_EXEC_SIGN`.
