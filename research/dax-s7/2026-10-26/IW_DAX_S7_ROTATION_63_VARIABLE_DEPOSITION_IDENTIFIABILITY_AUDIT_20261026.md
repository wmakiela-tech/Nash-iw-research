# IW/NASH — DAX-S7 — obrót 63

**Data:** 2026-10-26  
**Temat:** źródłowa identyfikowalność energii Hawkinga i nieuniwersalność wykładnika szerokości okna potrójnych przecięć przy zmiennym podziale energii EM–ν.  
**Tryb:** INDEPENDENT_SOURCE_AUDIT / BOUNDED_TWO_SECTOR_COUNTERFACTUAL / SCIENCE_FIRST / NEGATIVE_KNOWLEDGE_PRESERVING.  
**Status:** NUMERICAL_CONTROL_SUPPORTED, **NO_EXEC / NO_CANON / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / NO_PBH_BOUND**.

## 1. Pytanie falsyfikacyjne

Obrót 62 wykazał w warunkowym dwusektorowym modelu EM–ν bardzo wąskie przedziały mas PBH, w których temperatura fotonów trzykrotnie przecina `T_nuc = 0.07818527068831995 MeV`, oraz dopasowanie szerokości tych przedziałów do `f_EM^(3/2)` przy **stałym** `f_EM`. W obrocie 63 pytamy, czy wynik ten można przenieść na **nieznaną funkcję** `f_EM(M,t)`, którą narzucałby rzeczywisty rozkład emisji pierwotnej, showering, rozpady i oddziaływanie z plazmą.

**Odpowiedź:** nie. Mechanizm potrójnego przejścia pozostaje w kilku warunkowych rodzinach funkcji, ale szerokość i wykładnik skalowania zależą zasadniczo od asymptotyki końcowego udziału EM. Publiczne dane Wu–Xu nie identyfikują tego udziału bez nowego obliczenia widm i transferu energii.

## 2. Audyt źródłowy — rozdzielenie dostępnych danych i brakujących wielkości

Odczytano bezpośrednio publiczne repozytorium `Fenyutanchan/Primordial-Black-Hole`, katalog `arXiv-2509.05618/`:

- `main-scan.jl` (Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`) ewoluuje gęstość promieniowania z **jednym łącznym** źródłem masy PBH, nie z funkcją partycji EM–ν.
- `tool_script-hadrons_from_PBH.jl` (blob `cc73432910f872d526113ce59b6204f38d0766a9`) interpoluje `hadrons_from_PBH.dat` jako **liczby emitowanych mezonów, protonów i neutronów**; nie jako podział mocy energetycznej EM/ν.
- `data/out/hadrons_from_PBH.dat` (blob `06d0883a27b108692720422294ba2baacd381a64`) zawiera 100 punktów mas i pięć strumieni liczbowych. Minimalna tablicowana masa to `1e9 g`; brak rozdzielczości energetycznej umożliwiającej pomiar energii depozycji.
- `tool_script-BlackHawk_extension.jl` (blob `16c5cb6f87dcd2e2b416b6664d3bdcb3c3c68818`) ma funkcję odczytu **dwóch** wyjść: `instantaneous_primary_spectra.txt` i `instantaneous_secondary_spectra.txt`. Publiczny `data/out` zawiera tabelę hadronów oraz `scanning.jld2`, ale **nie zawiera tych dwóch widm**. Pliku binarnego `scanning.jld2` nie analizowano jako zamiennika brakujących widm.
- Domyślna konfiguracja wrappera BlackHawk zawiera `grav=1` i `add_DM=1`, a istnieje pomocnicza funkcja wyłączająca DM. Przy własnym wykonaniu należy jawnie odnotować **faktyczną konfigurację** używaną do odtwarzania danych, a nie automatycznie stosować ustawienia domyślne.

Definicja wymaganego wielkościowo rozkładu jest silniejsza niż odczyt ilości hadronów: 

\[
P_i^{\rm prim}(M)=\int E\,\frac{d^2N_i^{\rm prim}}{dE\,dt}\,dE,\qquad
f_{\rm EM}^{\rm dep}(M,t)=\frac{P_{\rm deposited,EM}(M,t)}{P_{\rm total\ mass\ loss}(M,t)}.
\]

Depozycja wymaga propagacji i transferu energii; **nie wolno dodawać sum mocy pierwotnych i wtórnych jako niezależnych źródeł energii** (podwójne liczenie tej samej energii). W szczególności antynukleony, mezony i produkty rozpadów mogą przekazywać energię obu sektorom.

**Status f_EM(M,t): NOT_IDENTIFIED_FROM_PUBLISHED_OUTPUTS.** Nie jest to dowód, że prawdziwy udział maleje do zera; rozważane poniżej profile są wyłącznie kontrolami kontrfaktycznymi.

## 3. Model i rodzina testowa

Zachowano oryginalny, samodzielny model numeryczny obrotu 62: fotony i gaz elektronowo-pozytonowy z równaniem stanu liczonym z całek Fermiego–Diraca, osobna efektywna gęstość neutrin, pełny układ bilansów energii oraz tło PBH, bez sieci reakcji jądrowych i bez uruchomienia oryginalnej Julii. Ustalono:

`beta=1e-17`, `T_dec=2 MeV`, `y=M_PBH/M_f`, `T_nuc=0.07818527068831995 MeV`, `y_ref=0.1`.

Testowano funkcje:

\[
\boxed{f_{\rm EM}(y)=f_{\rm floor}+(f_0-f_{\rm floor})
\min[1,(y/y_{\rm ref})^p]},\qquad
0\le f_{\rm floor}\le f_0\le1.
\]

Standardowa seria używa `f_floor=0`, `p=0,0.5,1,1.5,2`, `f0=0.4,0.7,1`. Oznacza to, że dopiero przy PBH pozostałym z 10% początkowej masy udział zaczyna zmieniać się z `f0` do wartości końcowej. Próg masowy `y_ref M_f ≈ 9.58e8 g` przypada **tuż poniżej minimalnej masy tabeli hadronowej 1e9 g**: żaden z tych przebiegów nie jest wyznaczony z liczbowych danych `hadrons_from_PBH.dat`.

Warianty `f_floor>0` testują niezerową asymptotyczną depozycję w EM. Wszystkie funkcje zapewniają `0≤f≤1`, a pozostałą moc kierują do sektora neutrin, zakładając jego efektywny opis promieniowania. Emisja przed `T_dec` pozostaje poza bilansem testowym, zgodnie z obrotem 62.

## 4. Wyniki główne: zmiana wykładnika szerokości okna

Wyniki po bisekcji obu granic masowych i ponownym wyznaczeniu trzech przecięć:

| Profil końcowy | `f0=0.4` | `f0=0.7` | `f0=1` | Eksponent dopasowany | Prognoza lokalna |
|---|---:|---:|---:|---:|---:|
| `p=0` | 122 368 g | 282 555 g | 481 219 g | 1,49447 | 1,5 |
| `p=0.5` | 16 374 g | 49 961 g | 101 596 g | 1,99221 | 2 |
| `p=1` | 586 g | 3 124 g | 9 056 g | 2,98757 | 3 |
| `p=1.5` | wynik poniżej progu wiarygodnej kwantyfikacji | ~2,45 g (graniczne) | ~20,6 g (graniczne) | **nieprzyznany** | 6, asymptotycznie |
| `p=2` | bez rozpoznanego lokalnego końcowego minimum | jak obok | jak obok | nie dotyczy | brak generycznego fold w tej granicy |

Dopasowania `p=0,0.5,1` mają `R²>0.9999997`. Trzy przecięcia w tych trzech rodzinach potwierdzono przy trzech konfiguracjach tolerancji i maksymalnego kroku. Przy `p=1.5` wynik jest bardzo bliski precyzji całkowania, a liczba przecięć zależała od testowanej dokładności — **nie zaliczać do niezależnie potwierdzonych okien**. Dla `p=2` nie ustalono żadnego wiarygodnego lokalnego końcowego minimum przy `f0≤1`.

### Mechanizm analityczny

Równanie EM względem zmniejszającej się masy `y` ma w końcowej granicy postać:

\[
\frac{d\rho_{\rm EM}}{dy}\simeq A y^2-Bc y^p,
\qquad A,B>0,\quad c=f_0/y_{\rm ref}^{p}.
\]

Dla `0≤p<2` punkt minimum występuje przy:

\[
y_*=(Bc/A)^{1/(2-p)},\qquad
\rho_{\rm EM}(0)-\rho_{\rm EM}(y_*)\simeq
\frac{A(2-p)}{3(p+1)}y_*^3.
\]

O ile przejście przez `T_nuc` jest transwersalne względem masy początkowej, wynika stąd:

\[
\boxed{\Delta M_{\rm window}\propto f_0^{\,3/(2-p)}}.
\]

Gdy `f_EM(0)>0` i ten wyraz dominuje dostatecznie blisko końca, odzyskuje się wykładnik `3/2`. Gdy `f_EM(y)~y^p`, wykładnik zmienia się. Jest to lokalna zwykła analiza typu fold; **brak wniosku o nowości matematycznej lub fizycznej**.

## 5. Kontrola identyfikowalności przez bilans całkowitej energii

Uśredniony **przypisany** udział EM w energii wypromieniowanej po rozsprzęgnięciu neutrin jest równy średniej `f(y)` po traconej masie:

\[
\bar f_{\rm EM}=\frac{1}{y_{\rm dec}}\int_0^{y_{\rm dec}}f(y)\,dy
=f_0-(f_0-f_{\rm floor})\frac{y_{\rm ref}}{y_{\rm dec}}\frac{p}{p+1},
\quad y_{\rm dec}>y_{\rm ref}.
\]

Przy `f0=1, f_floor=0`:

| `p` | Średni przypisany udział EM | Szerokość okna |
|---:|---:|---:|
| 0 | 100% | 481 219 g |
| 0.5 | 96,666% | 101 596 g |
| 1 | 94,999% | 9 056 g |
| 1.5 | 93,998% | graniczne |
| 2 | 93,331% | nie wykryto końcowego fold |

**Wniosek identyfikacyjny:** niemal identyczny globalny budżet energii nie determinuje zdolności do wywołania potrójnego przecięcia. Kluczowy jest profil depozycji przy `y≈0.01–0.05`, a nie jedynie całkowity udział EM.

## 6. Kontrola udziału końcowego i momentu przejścia

Dla `f0=1,p=1,y_ref=.1`, ale z niezerowym udziałem asymptotycznym:

| `f_floor` | Szerokość okna |
|---:|---:|
| 0 | 9 056 g |
| 0.005 | 10 459 g |
| 0.02 | 14 824 g |
| 0.05 | 24 165 g |
| 0.10 | 41 185 g |
| 0.20 | 79 284 g |
| 0.50 | 214 541 g |
| 1.00 | 481 219 g |

Przy `p=1,f0=1,f_floor=0` zmiana `y_ref` daje: `0.05 -> 72 413 g`, `0.1 -> 9 056 g`, `0.2 -> 1 133 g`, zgodnie w przybliżeniu z lokalnym `y_ref^-3`.

## 7. Walidacja niezależna i ryzyka

- Rzeczywisty samodzielny kod Python/SciPy: kompilacja składni, uruchomienie `--quick` oraz osobnych przebiegów `--profiles-only` i `--floors-only`: **PASS**. Pełny skan nie mieścił się w jednym limitowanym uruchomieniu środowiska, dlatego jawnie rozdzielono etapy bez utraty wyników.
- Kontrola przecięć na trzech siatkach tolerancji dla `p=0,0.5,1`: 3/3 w wybranych punktach środkowych. Dla `p=1.5`: **NIE PASS**, ponieważ przy luźniejszej tolerancji liczba przecięć nie była stabilna.
- Niezależne różnice centralne bilansu EM+ν przeprowadzono w punktach z dala od załamania `y_ref=.1`; dla reprezentatywnych `y≥.02` reszty sumy bilansu są rzędu `10^-8` lub mniejsze. Należy osobno rozpoznawać lokalny błąd różniczkowania na punkcie nieróżniczkowalności przy `y_ref`.
- Model używa efektywnego `T_nu=(rho_nu/5.25)^(1/4)`; nie dowodzi termalizacji wstrzykiwanych wysokoenergetycznych neutrin.
- Brak oryginalnego solvera Julia i wykonania BlackHawk; brak źródłowych widm z energią, kerneli depozycji i pełnej sieci BBN.
- Powyższe masowe okna to **wyniki warunkowego modelu kontrolnego**, nie nowe przedziały dozwolone fizycznie ani ograniczenia PBH.

## 8. Jednoznaczny następny falsyfikator — specyfikacja do przekazania innym komórkom

**TO: XH / PRF / MECH / INT / BW.** Zweryfikować oddzielnie pochodzenie i konfigurację rzeczywistych widm BlackHawk. Wymagane są: snapshot źródła, pliki pierwotne i wtórne, definicje gatunków cząstek, spin, graviton, DM on/off, hadronization-choice, obszar energii i mas `M≈10^8–10^10 g` (ze szczególnym uwzględnieniem `M/M_f≈0.005–0.2`), wyniki integracji `∫E d²N_i/dEdt dE`, rozdzielenie energii neutrin finalnych od kanałów EM i pozostałych, sprawdzenie sumy mocy **bez podwójnego liczenia** źródeł wtórnych. Następnie przeprowadzić transfer/thermalizację energii i uzyskać *deposition* fraction `f_EM(M,t,T_plasma)`, nie tylko emitted fraction. Zastosować ją jako zewnętrzną tablicę do dwusektorowego modelu i powtórzyć test fold, a dopiero później obliczyć neutrony i BBN.

### Manifest podstawowych źródeł

- Publiczny kod i dane: https://github.com/Fenyutanchan/Primordial-Black-Hole/tree/master/arXiv-2509.05618
- Publikacja Wu–Xu: https://doi.org/10.1088/1475-7516/2026/02/063
- Reproducer lokalny: `IW_DAX_S7_ROTATION_63_VARIABLE_FEM_SELF_CONTAINED_20261026.py` (samodzielny; `numpy` + `scipy`).
- Zbiory wynikowe: macierz okien, warianty `f_floor`, kontrola granicy przełączenia, jawne próby zbieżności, testy bilansu oraz manifest SHA-256 w pakiecie ZIP.

**Końcowy werdykt:** `SOURCE_ENERGY_FRACTION_NOT_IDENTIFIED / VARIABLE_ENDPOINT_FOLD_EXPONENT_DEPENDENT / CONDITIONAL_NUMERICAL_PASS_P0_P05_P1 / P15_NEAR_PRECISION / NO_FULL_JULIA / NO_BLACKHAWK_EXEC / NO_EXEC / NO_CANON / NO_PBH_BOUND`.
