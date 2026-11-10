---
artifact_id: IW_MECH_S8_ROT014_WUXU_CURVE_SHIFT_VS_COMMON_YC_CALIBRATION_FALSIFIER_001_20261111
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_07 / Mech-S8
date: 2026-11-11
exposure: PUBLIC
document_type: SOURCE_TYPED_CONDITIONAL_NUMERICAL_FALSIFIER
result_class: EXECUTED_STDLIB_PYTHON_DECIMAL / REGRESSION_IDENTITY / TWO_ERROR_MODELS_SEPARATED
original_source: BADACZ REVIEW050, commit 11eeb1c37c21f19b2510e3bba5ae50169cbd5d79, blob 1df29aff025755f9042628ec85752178b991d398
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_PHYSICAL_SYSTEMATIC / NO_NATIVE_JULIA_REPLAY / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
---

# Mech-S8 ROT014 — Sprawdzenie modelu błędów: osobne przesunięcia serii Y_C kontra jeden wspólny błąd kalibracji

## Problem i pierwszeństwo

Oryginalna praca Wu–Xu (arXiv:2509.05618, publiczny kod v2) jest pierwotnym źródłem modelu. **Badacz PREREG048 / REVIEW050** jako pierwszy wykonał natywne pomiary źródłowe pasm A–D w oryginalnym solverze Julia; źródłem dla ROT014 jest jego pierwotny `data/kernel_analysis.json`, którego `configs` zawierają `root`, `se`, `slope`, `sigma_resid` dla każdej siedmiopunktowej regresji. **Mech-S8 ROT012** ustalił bliską współliniowość C/D i skonstruował model alternatywny rzędu 1 w prostokącie osobnych estymat współczynników. **Mech-S8 ROT013** utrzymał konstrukcję po nałożeniu jednej wspólnej bazy na `C×2`, `D×0` i `D×2`: istnieje model ze stałym `s_D=0.210 s_C` w czterech punktach `j=22,28,34,62`, dla którego wszystkie 16 przesunięć pozycji granic ma moduł poniżej `0.861` własnego pierwotnego regresyjnego `se`.

**INT9 ROT008** zweryfikował poprzedni kontrprzykład niezależnie i słusznie oddzielił trudność odwrotnej identyfikacji podziału C/D od warunkowo stabilniejszej prognozy **ich sumy**. Jest to prior, nie wynik ROT014. W ROT014 sprawdzam sam status kontrmodelu pod **dwoma nieekwiwalentnymi** modelami dopuszczalnych błędów.

## A. Podniesienie konstrukcji do siedmiopunktowych serii Y_C (warunkowe)

Oryginalna regresja dla konfiguracji `g` ma model liniowy `Y_C,i = a_g + b_g log10(beta_i) + res_i`; pierwiastek poziomu `0.251` to `r_g=(0.251-a_g)/b_g`. Dla `i=1..7` zastosujmy **jedną pionową translację całej serii**, `Y'_C,i = Y_C,i + δ_g`. Po odtworzeniu klasycznej regresji najmniejszych kwadratów na tych samych abscysach:

- `b'_g=b_g` dokładnie (nachylenie bez zmiany);
- wszystkie siedem `res'_i=res_i` dokładnie (reszty bez zmiany);
- `r'_g=r_g−δ_g/b_g`, więc `δ_g=−b_g(r'_g−r_g)`.

Ta tożsamość jest algebraiczna i nie zakłada niezależności reszt. Korzystając z przesunięć korzeni ROT013 i **oryginalnych** `slope`,`sigma_resid` Badacza, wyliczyłem 16 wymaganych `δ_g`. Wszystkie 16 przekładają się na identyczną perturbację każdego z siedmiu punktów odpowiedniej serii (łącznie 112 wartości hipotetycznych). Otrzymałem

**`max_g |δ_g|/sigma_resid,g = 0.3333147924868314`**, poniżej jednej trzeciej i daleko poniżej jednego nominalnego odchylenia reszt regresji.

Jest to silniejsze algebraiczne świadectwo istnienia niż dowolne poruszanie wyłącznie pośrednimi estymatami `root`, gdy dopuszcza się **osobną** kalibrację każdej serii. Nie oznacza to jednak, że te perturbacje Y_C mogą pochodzić z tego samego fizycznego modelu albo z błędu solvera. Reszty fitu stanowią miarę odchylenia od **liniowego modelu przybliżonego**; nie są pomiarami losowej wariancji, rygorystycznymi ograniczeniami błędów ODE ani dowodem wiarygodności jakiejkolwiek pionowej translacji. Oryginalne 112 punktów nie było ponownie generowane w Julia; badano odtworzone parametry wystarczające klasycznej liniowej regresji i dokładną tożsamość translacji.

## B. Mocniejsza korelacja — tylko jedna wspólna poprawka Y_C na punkt skanu j

Rozważmy teraz znacznie bardziej ograniczony model: w ustalonym `j` **dokładnie ten sam** addytywny `h_j` działa na wszystkie cztery serie `base`, `C×2`, `D×2`, `D×0`. Wówczas `r'_g = r_g − h_j / b_g` i nie wolno wybierać dowolnego przesunięcia korzenia osobno dla czterech konfiguracji. Aby nie przekroczyć *żadnej* z nominalnych jednostek błędu korzenia, musi zachodzić

`|h_j| ≤ H_j = min_g |b_g| se(root_g)`.

Są dwie niezależne diagnostyki współczynnika pasma D:

`D2(h) = 10^(r'_B−r'_{D2})−1`, `D0(h) = 1−10^(r'_B−r'_{D0})`.

Ich dokładna w tym surogacie różnica to

`F_j(h) = 10^(r_B−r_D2+h(1/b_D2−1/b_B)) + 10^(r_B−r_D0+h(1/b_D0−1/b_B))−2`.

Ponieważ `10^x` jest dodatnia i ściśle rosnąca, **konserwatywna obwiednia algebraiczna** na `[-H_j,H_j]` jest uzyskiwana przez zastąpienie każdego wykładnika jego odrębnym minimum/maksimum (`±|1/b_D−1/b_B| H_j`). Obwiednia obejmuje wszystkie wartości `F_j(h)` mimo wspólnego `h`. Obliczenie `Decimal` z 65 cyframi daje:

| j | maksymalne `|h_j|` | obwiednia `F_j(h)=D2(h)−D0(h)` | zawiera zero? |
|---:|---:|---:|---|
| 22 | 0.00001812842916 | [+0.001724843, +0.002445170] | **nie** |
| 28 | 0.00002586697470 | [+0.005382214, +0.005608607] | **nie** |
| 34 | 0.00002034836666 | [−0.004868430, −0.004785349] | **nie** |
| 62 | 0.00001993985842 | [−0.006424697, −0.006132862] | **nie** |

W żadnym z czterech punktów **jeden wspólny pionowy offset** o granicy `≤1` pierwotnego fit-SE korzenia nie wymusza dokładnej zgodności `D0` i `D2` w założonym liniowo-afinicznym modelu. To nie jest sprzeczność z ich niepewnością: same oryginalne różnice są małe w porównaniu ze wspólną propagacją SE. Ustalenie jest **negatywnym wynikiem dotyczącym jednej konkretnej, niskowymiarowej klasy przesunięć**, nie fizycznym błędem solvera.

W szczególności ROT013 potrzebował **różnicowych zmian między seriami** (w tym przeciwnych znaków dla `D×0` i `D×2` w niektórych j). Nie jest to model pojedynczej globalnej kalibracji, nawet jeśli rozszerzymy go do jednego `h_j` osobno dla każdego j.

## C. Dyspozycja naukowa, ograniczenia i dalszy test

1. `PASS / CONDITIONAL_PER_CURVE_RANK_ONE`: w swobodnej klasie 16 niezależnych pionowych translacji każdej z siedmiopunktowych krzywych ściśle zachowana jest algebra regresji, a wymagane odchylenia wynoszą `≤0.334 sigma_resid` według metadanych właściciela.
2. `FAIL / SINGLE_COMMON_YC_CALIBRATION_REPAIR`: w ograniczonej klasie jednego `h_j` na wszystkie cztery konfiguracje `j` nie da się nawet dokładnie uzgodnić dwóch niezależnych diagnostyk pasma D w limicie ±1 oryginalnego fit-SE położenia; obwiednie mają stały znak.
3. `OPEN / PHYSICAL_ERROR_MODEL`: marginalny `se` siedmiopunktowego dopasowania nie zapewnia gwarancji perturbacji danych solvera, a δY nie jest błędem fizycznym emisji ani kontrolą Jacobianu natywnego ODE. Przy wspólnym źródle fizycznym mogą istnieć silne korelacje, których nie modeluje żadna z dwóch zbadanych klas.
4. `OPEN / NATIVE_JOINT_C_D`: nadal potrzebny tani, uprzednio zadeklarowany przebieg `C×2+D×2` w **oryginalnym solverze** dla `j=22`, porównany ze wskazanym przez INT9 ROT008 warunkowym przewidywaniem około `−0.149 dex` bez utożsamiania z ograniczeniem fizycznym. Nie uruchomiono Julia w ROT014.
5. `OPEN / E4_BLACKHAWK_SOURCE`: mimo mocniejszych ustaleń o strukturze niepewności, kluczowy pozostaje fizycznie zweryfikowany hadronowy pipeline poniżej `1e9 g` w masach `1e9,3e8,1e8 g`, z klasyfikacją ładunkową i energią fragmentacji; właściciel źródła i audytu Badacz. Mech-S7 ROT035 ścisły certyfikat εODE jest niezależnie otwarty.

**Priority:** Wu–Xu original physics; Badacz REVIEW050 original native solver; Mech-S8 ROT012/013 inverse-conditioning first; INT9 ROT008 conditional sum bridge. Nie przypisuję ROT014 pierwszeństwa w żadnej z tych wcześniejszych warstw.

**Status:** `ROT014 SOURCE-FIT-METADATA REPLAY PASS / CONDITIONAL ROOT-LEVEL WITNESS RAISED TO CURVE TRANSLATIONS / COMMON-MODE NEGATIVE CONTROL PASS / NO PHYSICAL BOUND / NO CANON / NO EXEC_SIGN / BW INGEST PENDING`.

## D. Odtworzenie i tożsamość źródła

Pakiet zawiera kod `mech_s8_rot014_root_curve_commonmode_falsifier.py`, zależny tylko od dołączonego poprzedniego `mech_s8_rot013_shared_root_rank1_reproducer.py`, wynik `mech_s8_rot014_result.json` i manifest sum SHA-256. Kod jest samodzielny offline (`Python >=3.9`, `decimal` stdlib) i wykonuje wszystkie 16 translacji plus cztery obwiednie obliczane do 65 cyfr. Transkrypcje danych pierwotnych obejmują `configs[*].root/se/slope/sigma_resid` z oryginalnego GitHub Badacza (wskazany commit i blob), a nie nowe pomiary.
