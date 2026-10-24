# IW/NASH — DAX-S7 — obrót 53

**Tytuł:** Źródłowo dopasowany test rozdzielenia obszarów zgodności obserwacyjnej przez definicję helowego obserwabla.  
**Data:** 2026-10-25  
**Status:** `SOURCE-TABLE_RECONSTRUCTION / OBSERVABLE_MAPPING_TEST / BETA_SCAN_CONDITIONAL / MATURE_HOST_SUBTRACTION / NEGATIVE_KNOWLEDGE_PRESERVING / JULIA_NOT_RUN / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE`.

## 1. Pytanie falsyfikujące i znaczenie obrotu

Czy niejednoznaczność czasowego odczytu `X_n(T_nuc)` ujawniona w obrotach 45–52 zachodzi w części przestrzeni parametrów, która byłaby zgodna z użytym w publikacji testem `Y_p=0.245±0.003`? Czy obszar „zgodności obserwacyjnej” jest stabilny względem zamiany źródłowego wzoru `Yp_code=2X_n/(1-X_n)` na standardowe przybliżenie frakcji masowej helu `Yp_mass≈2X_n`?

**Odpowiedź w ściśle oznaczonym modelu kontrolnym:** przy stałej masie początkowej `M_f=9.6725×10^9 g` i odtworzonym źródłowym równaniu neutronów z quasi-stacjonarnymi populacjami sześciu hadronów 3σ przedziały `β` są rozłączne; w 19 badanych punktach potrójne przejście wystąpiło tylko przy `β=10^-17`, daleko od obu przedziałów. Nie jest to wynik pełnego programu Julia, pełnego skanu `(M,β)` ani rozwiązania sieci reakcji jądrowych.

## 2. Oryginalne źródła i provenance

Odczytano przez połączenie GitHub cztery **pełne tablice** Wu–Xu w `Fenyutanchan/Primordial-Black-Hole`, `arXiv-2509.05618` oraz zweryfikowano formuły `main-scan.jl`, `main-scan-parameters.jl`, `tool_script-parameters.jl` i `tool_script-N_relativistic_species.jl`. Aktualny identyfikator pliku źródłowego (Git blob SHA):

| Plik | Blob SHA |
|---|---|
| `main-scan.jl` | `b368ba55d5a493f7bc185909730f7fe5691f10d6` |
| `main-scan-parameters.jl` | `53faee65beda383348580c28d0424188da69b660` |
| `tool_script-parameters.jl` | `0d7198ff3557bdbd5753000bb07a7a7405cc24f5` |
| `data/ext/N_around_m_e.csv` | `93f2494f026c5d0587ea40fe08bb938dd9d01fa8` |
| `data/ext/N_s_from_PDG2024.csv` | `33aceb876fc36cb2486d36c690e6401d85d76b46` |
| `data/ext/N_rho_OVER_N_s_from_PDG2024.csv` | `28b0c13563d7b3bdeaee191a3a981197345d05b8` |
| `data/out/hadrons_from_PBH.dat` | `06d0883a27b108692720422294ba2baacd381a64` |

**Rola źródeł:** równania ewolucji, emisyjność, sześć kanałów hadronów i obserwabla pochodzi z ich publicznej implementacji. Wnioski algebraiczne dotyczące poprawnego liczenia frakcji masowej wynikają ze standardowej definicji `X_n=n_n/(n_n+n_p)` i założenia, że prawie wszystkie dostępne neutrony zostaną związane w hel-4; **to przybliżenie, a nie kompletna sieć BBN**. Równania fizyczne i obserwabla nie uzyskały niezależnej walidacji eksperymentalnej w tym obrocie.

## 3. Niezależny test matematyczny od modelu PBH

W źródle `X_n` oznacza **udział neutronów**, nie iloraz `n_n/n_p`, a kod do `χ²=((Yp−.245)/.003)^2` wykorzystuje `Yp_code=2X_n/(1-X_n)`. W powszechnym uproszczeniu „wszystkie neutrony w He-4” rzeczywista frakcja masowa wynosi natomiast `Yp_mass≈2X_n`.

Przy celu `μ=.245` odpowiadające wartości `X_n` to:

- `X_code=μ/(2+μ)=0.109131403118`;
- `X_mass=μ/2=0.1225`.

A zatem oba obserwable nakładają **różne wymagania nawet dla tej samej idealnie znanej trajektorii `X_n(t)`**. Przy `3σ`, akceptowane przedziały `X_n` są rozłączne:

- kod: `[.236/(2+.236), .254/(2+.254)] = [0.105545617174, 0.112688553682]`;
- standardowe przybliżenie: `[.236/2, .254/2] = [0.118, 0.127]`.

To rozdzielenie jest **ścisłą tożsamością algebraiczną**, nie nową hipotezą fizyczną ani dowodem o faktycznej dokładności modelu BBN.

## 4. Metoda obliczeniowa i zakres skanu

Dla `M_f=9.6725×10^9 g` (punkt **poza** publikowaną 100-punktową siatką mas) odtworzono ODE tła i rozkład źródłowej emisji hadronów od czasu formacji PBH. Wykorzystano `1000` punktów tablicy niskotemperaturowej, `89` dla `g_s` PDG2024, `82` dla `g_ρ/g_s`, `100` źródłowych węzłów emisji hadronów oraz źródłową regułę ekstrapolacji. Zmienna `X_n` była propagowana wykładniczo na krokach modelu z **quasi-stacjonarnymi** populacjami `n_h≈S_h/D_h`, a nie niezależnym pełnym Julia ODE wszystkich sześciu gęstości hadronów. Łącznie wypróbowano 19 wartości `β`: 11 w źródłowym `[10^-20,10^-17]`, 7 dodatnich poniżej tego zakresu oraz formalną kontrolę `β=0`. Gdy temperatura przekraczała `T_nuc`, liczono jej pierwsze przecięcie.

### Próbka reprezentatywna

| `β` | `X_n(T_nuc)` | `Yp_code` | `Yp_mass≈2X_n` | Przecięcia `T_nuc` |
|---:|---:|---:|---:|---:|
| `0` (kontrola) | 0.10903302 | 0.24475210 | 0.21806604 | 1 |
| `10^-20` | 0.10958184 | 0.24613567 | 0.21916367 | 1 |
| `5×10^-20` | 0.11176858 | 0.25166545 | 0.22353716 | 1 |
| `10^-19` | 0.11448294 | 0.25856744 | 0.22896588 | 1 |
| `2×10^-19` | 0.11984880 | 0.27233683 | 0.23969759 | 1 |
| `5×10^-19` | 0.13545601 | 0.31335828 | 0.27091201 | 1 |
| `10^-17` | 0.39317376 | 1.29583640 | 0.78634753 | 3 |

W przypadku `β=0` widać szczególnie przejrzyście różnicę: `χ²_code≈0.00683`, podczas gdy dla `2X_n` otrzymujemy `χ²_mass≈80.60`. Nie przesądza to, czy zastosowany uproszczony model neutronów sam jest fizycznie poprawny; ujawnia silną **zależność wniosków od definicji obserwabla**.

## 5. Wyniki przedziałów zgodności, warunkowe

Dla próbek źródłowego obszaru `β≥10^-20` wyznaczono granice przez monotoniczną interpolację PCHIP (`log10 β` jako funkcja `Yp`). Liczby są szacunkami interpolacyjnymi, nie wynikami adaptacyjnej lokalizacji dokładnego progu i nie boundami PBH.

| Kryterium | `Yp_code` | `Yp_mass≈2X_n` |
|---|---|---|
| Zgodność `1σ` | `[10^-20, 2.346×10^-20]` | `[2.202×10^-19, 2.756×10^-19]` |
| Zgodność `2σ` | `[10^-20, 4.531×10^-20]` | `[1.939×10^-19, 3.044×10^-19]` |
| **Zgodność `3σ`** | **`[10^-20, 6.661×10^-20]`** | **`[1.664×10^-19, 3.336×10^-19]`** |

Minimalna przerwa w β między przedziałami 3σ to iloraz `1.6636e-19/6.6607e-20≈2.50`. Przy dopasowaniu wartości centralnej model daje `β≈1.792×10^-21` dla `Yp_code` (**poza oryginalnym zakresem β**) i `β≈2.474×10^-19` dla `2X_n` (**wewnątrz zakresu**). Iloraz ≈138 jest wyłącznie ilustracją wrażliwości dopasowania na mapowanie obserwabla, **nie relacją pomiędzy fizycznymi ograniczeniami**.

**Rozdzielić:** (1) dokładną algebraiczną rozłączność przedziałów `X_n`, (2) przybliżone przedziały `β` z modelu źródłowo dopasowanego, (3) nieprzeprowadzoną fizyczną walidację za pomocą sieci nuklearnej i pełnego solvera. Tylko (1) jest niezależne od numerycznego modelu.

## 6. Ekstrapolacja emisji i brak dowodu o niejednoznaczności w części dopuszczonej

Przy tej masie i β rzędu `10^-20...10^-19` pierwsze `T_nuc` zachodzi około `t=214.962...214.964 s`, przed `τ≈215.07211 s`, a masa PBH wynosi około `0.77×10^9 g`, **poniżej dolnego węzła źródłowej tabeli emisji, 10^9 g**. Tabela w kodzie wykorzystuje wtedy ekstrapolację log-log, której adekwatność fizyczna nie została niezależnie ustalona.

W tej **pojedynczej** masie i 19-punktowym β-skanie tylko największy β (`10^-17`) dawał trzy przekroczenia `T_nuc`. W jego punkcie `X_n≈0.393`, zatem obydwa helowe testy zdecydowanie odrzucają punkt w modelu. **Nie wolno z tego wyciągać wniosku o nieistnieniu potrójnych przejść w całej dwuwymiarowej przestrzeni mas i β**: obroty 47–49 wyjaśniają, że odpowiednie okno mas może być nadzwyczaj wąskie i poza oryginalną siatką.

Dla kontrolnej oceny quasi-stacjonarności: zaniki antynukleonów przy `T_nuc` mają rząd `8×10³–10⁴ s^-1`, natomiast na tle `β≈2×10^-19` czasowa pochodna logarytmu źródłowej emisji (z lokalnym wykładnikiem masowym około `−1.20`) ma rząd `3.7 s^-1`. Sugeruje to małe opóźnienie populacji w lokalnym regionie, ale **nie jest dowodem globalnej zbieżności w całej historii**, szczególnie przy końcu parowania.

## 7. Protokół falsyfikacji, zależności i przekazanie

1. **Priorytet:** uruchomić `main-scan.jl` / `magic(M,β)` w oryginalnym Julia z event detector dla `T=T_nuc`, dla `β≈(1...4)×10^-19` i odpowiadających mas, porównując `Yp_code`, `2X_n` i interpolator na próbkowanych `a_list`.
2. Osobno uruchomić spójny model **pełnej sieci reakcji jądrowych BBN**, aby zastąpić przybliżenie `2X_n` wiarygodną masową obfitością `^4He`. Nie podstawiać żadnego wniosku numerycznego bez takiego kroku.
3. Zweryfikować źródłowe emisje dla `M_PBH<10^9 g` (włącznie z pochodzeniem tablicy i zasadnością ekstrapolacji). Porównać z kontrolą cenzurowaną i z rozszerzoną tablicą wyliczoną fizycznie.
4. Zbadać **dwuwymiarowy**, zagęszczony skan `(M,β)` w obszarze zgodności i policzyć liczbę przecięć na rozwiązaniu ODE, nie tylko `10k` węzłów wynikowych.
5. Oddzielnie uzyskać od właścicieli modelu definicję `Yp` w pracy opublikowanej (różna także od kodu, jak ustalił obrót 32), bez przypisywania intencji autorom.

**Ograniczenia i nie-wyniki:** brak wykonania oryginalnego solvera Julia; brak weryfikacji fizycznego `Yp`, brak wyprowadzenia granic PBH, brak dowodu błędu wyników opublikowanych, brak rozwiązania wielowartościowości dla całego skanu. Rola DAX pozostaje falsyfikacyjna i rozbieżna. Wynik wymaga przeglądu REC/KN oraz ewentualnej decyzji Moderatora `EXEC` przed jakąkolwiek kanonizacją.

## 8. Reprodukcyjność i artefakty

Artefakty zapisane obok raportu:

- `IW_DAX_S7_ROTATION_53_BETA_OBSERVABLE_SPLIT_20261025.csv`: 19 rzeczywistych wierszy z niezależnego źródłowo dopasowanego integratora JavaScript wykorzystującego cztery pełne tablice z konektora GitHub;
- `IW_DAX_S7_ROTATION_53_BETA_OBSERVABLE_SPLIT_ANALYSIS_20261025.py`: samodzielna analiza CSV, kontrole tożsamości i przedziały PCHIP; opcjonalny `--recompute` importuje wcześniejszy skrypt rotacji 52 i cztery pliki źródłowe, wymagające osobnego udostępnienia;
- `IW_DAX_S7_ROTATION_53_BETA_OBSERVABLE_SPLIT_SUMMARY_20261025.json`: obliczone wyniki i caveats.

**Wykonano** lokalnie analizator danych CSV w Python, z kontrolą równości `Yp_code=2X/(1-X)` i `Yp_mass=2X`, monotoniczności 19 wyników oraz estymacją przedziałów PCHIP. **Nie wykonano** lokalnie opcji `--recompute` z czterema oryginalnymi plikami, które obecne środowisko może odczytać przez konektor GitHub, lecz nie pobrać bezpośrednio do lokalnego systemu plików. Wartości 19 punktów uzyskano i zweryfikowano w tej sesji w niezależnym JS z pełnymi danymi źródłowymi.

**Werdykt:** `OBSERVABLE-DEFINED_ACCEPTANCE_DISJOINT_IN_CONDITIONAL_SOURCE_PORT / ALGEBRAIC_X_BANDS_DISJOINT / OFFGRID_BRANCHING_NOT_WITHIN_THE_TESTED_ACCEPTANCE_WINDOW / PHYSICAL_PBH_BOUNDS_UNDEFINED / JULIA_NOT_RUN / NO_CANON`.
