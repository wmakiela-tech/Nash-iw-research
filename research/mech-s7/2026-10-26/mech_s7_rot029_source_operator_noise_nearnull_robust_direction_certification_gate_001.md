artifact_id: MECH-S7-FRONTB-NOISE-STABILITY-AND-NEARNULL-CERTIFICATION-GATE-029_20261026
exposure: PUBLIC
claim_ceiling: EXECUTED_CONDITIONAL_SOURCE_OPERATOR_AND_FINITE_7D_ODE_SENSITIVITY_NO_PHYSICAL_ADMISSION
sync_state: GITHUB_PENDING_BW_INGEST

# MECH-S7 / ROT029 — odporność kierunku wielotłowego na niepewność operatora

**Data:** 2026-10-26  
**Problem:** P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001  
**Jednostka:** `IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7`  
**Status:** warunkowy wynik numeryczny i dokładna warunkowa nierówność wartości osobliwych; bez uznania fizycznego, kanonu i EXEC.

## 1. Stan zastany i odejmowanie poprzednich wyników

Oryginalne źródło Wu–Xu: repo `Fenyutanchan/Primordial-Black-Hole`, commit `d395183674cace6c9906a8911bdeb7234ba4040d`, kod `arXiv-2509.05618/main-scan.jl`, tabela `data/out/hadrons_from_PBH.dat`. Tabela zawiera wyłącznie M≥1e9 g; cała emisja pod progiem jest źródłowo **niezwalidowana**. ROT013 naprawił dziedziczenie stanu przed granicą 1e9 g. ROT020 wykazał nieliniową możliwość zmiany znaku odpowiedzi wskutek redystrybucji antynukleonów przy stałej sumie; ROT021 wyznaczył funkcje sprzężone; ROT023–024 wykazały niewystarczalność kilku momentów; ROT025–027 zidentyfikowały nieprzenoszalność i niemal kolinearność gradientów; ROT028 skonstruował wektor minimum normy w siedmiu oknach źródła przy trzech tłach (χEM=0.25,.50,.75), mapach `B_exec/B_sym`, oraz sprawdził EM=0,1 w kinetyce. Matematyczny host: klasyczna analiza SVD, perturbacje wartości osobliwych Weyla / subspace perturbation i problem identyfikowalności celu — **bez roszczenia o nowość teoretyczną**; naukowy przyrost ROT029 dotyczy nowej, wykonanej kontroli kalibracji.

## 2. Pytanie, którego ROT028 nie rozstrzygnął

Czy współczynnik uwarunkowania κ≈938803 oznacza zawodność konkretnego kierunku już na poziomie zmian solvera, czy tylko ryzyko dla błędów strukturalnych nieznanych operatorów? Odróżniamy:

- (A) **obserwowaną niepewność numeryczną** zmiany 96→160→256 punktów Gaussa oraz ostrzejszego rozwiązania adjoint (bez zmiany fizyki),
- (B) **sztucznie postulowaną niepewność współczynników sześciu wierszy operatora** zdefiniowaną tu jawnie jako addytywny iid Gauss N(0,σ²) w każdym współrzędnym znormalizowanego wiersza 4D, przed jego renormalizacją,
- (C) **rzeczywistą niepewność fizyczną** subtablicowego źródła hadronów: tej NIE znamy i żadna liczba (B) jej nie zastępuje.

## 3. Wykonane obliczenie macierzowe

W siedmiu oknach mas zachowano 3 współporuszające się momenty źródła (j=0,1,2); jądro macierzy momentów ma wymiar 4. Niech `W` będzie ortonormalną bazą jądra, a `A` macierzą 6×4 składającą się z wierszy *(gχ,map W)/||gχ,map W||*. Wektor `c=Wv`, `||c||∞=1`, jest prawym wektorem osobliwym odpowiadającym σ4. To dokładnie rodzina parametrów użyta w ROT028; brak zmiany dynamiki.

ROT028: σ=[2.44750857, 0.0984976246, 9.18266112e-05, 2.60705148e-06], κ=938803.31453.

| Wariant obliczenia | σ4 | Obrót `c` od wariantu 96/base | Największa zmiana współczynnika |
|---|---:|---:|---:|
| `96_base` | 2.60705148e-06 | 0° | 0 |
| `96_tight` | 2.60684898e-06 | 0.000243387° | 5.00543e-06 |
| `160_base` | 2.61014093e-06 | 0.00812333° | 0.000168268 |
| `160_tight` | 2.60993837e-06 | 0.00836652° | 0.000173272 |
| `256_base` | 2.60805439e-06 | 0.00199189° | 4.17238e-05 |
| `256_tight` | 2.60785166e-06 | 0.00223487° | 4.67284e-05 |

Zmiany zaobserwowane w wykonanych wariantach numerycznych są niewielkie: maksymalny obrót 0.00836652°. Są to **porównania rozdzielczości**, nie rygorystyczne granice błędu prawdziwych gradientów. W szczególności bardzo małe wartości σ4 i rzadkie wiersze wymuszają kontrolę stabilności osobno od formalnego kryterium rzędu.

## 4. Dokładny warunek perturbacyjny i ograniczenie certyfikacji rzędu

Jeżeli każdy **znormalizowany wiersz macierzy A po projekcji momentowej** ma nieznany błąd E_i o normie euklidesowej ≤η, wtedy z definicji normy Frobeniusa `||E||₂ ≤ ||E||F ≤ √6 η`. Z nierówności Weyla wynika:

`σ4(A+E) ≥ σ4(A) − √6 η`.

**Warunkowy wystarczający próg potwierdzenia numerycznego rzędu 4:** `η < σ4/√6 = 1.06432431e-06`. Aby zagwarantować zmianę σ4 nie większą niż 10% nominalnej z tego samego oszacowania wystarcza `η ≤ 1.06432431e-07`. To prognoza warunkowa: nie dysponujemy niezależną górną granicą η dla operatora fizycznego.

Sama duża κ nie świadczy o błędzie numerycznym aktualnego kierunku; oznacza, że małe błędy operatora mogą być istotne w zadaniach rozpoznawania słabo wzbudzonych kierunków.

## 5. Monte Carlo — jawnie sztuczne perturbacje

2400 realizacji z deterministycznym ziarnem generatora (8 poziomów × 300). Każdy zaburzony operator ponownie znormalizowany wierszowo; wybrano najmniejszy prawy wektor osobliwy z niezmienionego jądra momentów. Wyniki:

| SD błędu składnika w znormalizowanym wierszu | Mediana kąta | P95 kąta | P95 normy odpowiedzi dla pierwotnego A |
|---|---:|---:|---:|
| 1e-08 | 0.004° | 0.012° | 3.9201e-06 |
| 1e-07 | 0.036° | 0.111° | 3.9428e-06 |
| 1e-06 | 0.447° | 1.313° | 6.1229e-06 |
| 3e-06 | 1.398° | 3.815° | 1.2795e-05 |
| 1e-05 | 4.690° | 13.414° | 4.1062e-05 |
| 3e-05 | 15.407° | 58.338° | 0.00012982 |
| 1e-04 | 40.236° | 84.827° | 0.00038018 |
| 1e-03 | 41.054° | 85.630° | 0.0038568 |

To **test scenariuszy, nie przedział ufności błędu Wu–Xu**. Wiele realizacji świadomie przekracza możliwość perturbacyjnego zachowania najmniejszej pary osobliwej. Wybrano dwa reprodukowalne kierunki bliskie 95. percentylowi w osobnym losowaniu (seed 292605): σ=1e−5 (kąt 14.40165°) oraz σ=1e−4 (kąt 82.11501°).

### Leave-one-host-out bez retuningu w źródłowym ODE

Wykonałem dodatkowo sześć analitycznych rekonstrukcji z usunięciem jednego z sześciu wierszy; pokazuje to, które tła wnoszą stabilizującą informację w tej rodzinie:

| Pominięte χEM | Pominięta mapa | Obrót c | Odpowiedź liniowa pominiętego wiersza (znormalizowana) |
|---|---|---:|---:|
| 0.25 | `exec` | 1.202° | -4.9048e-06 |
| 0.25 | `sym` | 0.6983° | +4.437e-06 |
| 0.5 | `exec` | 0.0001104° | +1.9777e-08 |
| 0.5 | `sym` | 5.12e-05° | -1.9401e-08 |
| 0.75 | `exec` | 1.195° | +4.7749e-06 |
| 0.75 | `sym` | 0.6565° | -4.402e-06 |

Pominięcie środkowego tła 0.5 powoduje prawie zerowy obrót; skrajne tła kalibracyjne 0.25 i 0.75 są istotniejsze. To obserwacja **w obrębie zbioru sześciu wybranych wierszy**, nie przenoszalność na wszystkie χEM.

## 6. Weryfikacja nową pełną integracją ODE

Następnie wektory uzyskane przy dwóch sztucznych poziomach szumu wstawiono do dotychczasowego warunkowego układu (oryginalne archiwum źródłowe, poprawiony most 10-składnikowy z ROT013, transport pod progiem i późniejszy model 7D). Dla χEM=0,1, obu map i amplitud źródła ε=0,±0.15 wykonano **8 nowych trójek trajektorii (24 stany)** przy Radau `rtol=3e-9`. Jedno zbiorcze uruchomienie przekroczyło limit po wykonaniu siedmiu trójek; brakującą ósmą trójkę wykonano oddzielnie. Wszystkie osiem posiada zapisane wyniki. Numery ROT028 w kolumnie bazowej są odziedziczone, a nie w tym obrocie ponownie integrowane.

| χEM | mapa | ROT028 bazowa: max|δXnuc| | Operator zaszumiony 1e−5: max|δXnuc| (×bazowa) | Zaszumiony 1e−4: max|δXnuc| (×bazowa) |
|---|---|---:|---:|---:|
| 0% | `exec` | 2.56429e-10 | 2.82970e-09 (11.04×) | 1.38079e-08 (53.85×) |
| 0% | `sym` | 1.37171e-10 | 8.28839e-10 (6.04×) | 2.16276e-09 (15.77×) |
| 100% | `exec` | 2.33827e-10 | 2.62741e-09 (11.24×) | 8.62175e-09 (36.87×) |
| 100% | `sym` | 1.48780e-10 | 2.17637e-10 (1.46×) | 3.23163e-09 (21.72×) |

Wynik: przy zadanym stresie σ=1e−5 efekt rośnie w testowanych komórkach o 1.46–11.24×, a dla σ=1e−4 o 15.77–53.85×. **Nie oznacza to, że tyle wynosi faktyczna niepewność źródłowego modelu**. Przykłady pokazują granicę odporności kierunku wybranego za pomocą niedokładnych gradientów.

### Kontrole

* Inna kwadratura 256-punktowa: dla wszystkich trzech kierunków warunki momentowe j=0–2 mają znormalizowaną resztę ≤1.073×10−15. Obydwa widma pozostają dodatnie, minimalna frakcja pojedynczego kanału ≥0.34877. Suma Qpbar+Qnbar jest zachowana punktowo do 2.22e−16.
* Wyniki ODE pochodzą z ponownej integracji, a nie tylko iloczynu adjoint. Osobno zaostrzonych ODE dla kierunków zaszumionych nie wykonano. Dlatego bardzo małe efekty ≤2e−10 zachowują ostrożność numeryczną; wcześniejsze kontrolne porównania rtol wykonano w ROT028, lecz nie stanowią osobnego certyfikatu dla nowego źródła.
* Odtwarzalność: dwa ziarna pseudolosowe zapisane w kodzie; wyniki `geometry_029.json`, `source_constraints_029.csv`, `noisy_transfer_029.csv`; źródłowy pakiet ROT028 jest w archiwum ROT029 pod `deps_028/`, łącznie z oryginalnymi trajektoriami i kodem. Wersja 029 nie zmienia upstream.

## 7. Wniosek i rekomendacja naukowa

**Cechę trzeba opisać jako NUMERICALLY-STABLE-IN-TESTED-SOLVER-VARIANTS, BUT NOT CERTIFIED-UNDER-UNKNOWN-OPERATOR-ERROR.** Wcześniejsze `HELDOUT_PASS` z ROT028 odnosi się do fixed-kernel source family; nie oznacza niezmienniczości wyboru kierunku względem błędu gradientu. Do dalszej fizycznej interpretacji wymagane: walidacja subedge pbar/nbar widm w zakresie mas, określenie niepewności źródła, niezależna kontrola operatora kinetycznego, natywny kod Julia 10D accepted-step/event diagnostics. Bez tych etapów nie wolno wyprowadzać Yp, D/H, ograniczeń PBH, identyfikacji nowej fizyki lub EXEC.

## 8. Status i źródła

`EXECUTED_TESTED_MATRIX_RESOLUTION=PASS`  
`EXECUTED_2400_SYNTHETIC_KERNEL_PERTURBATIONS=PASS`  
`EXECUTED_24_NEW_CONDITIONAL_ODE_STATES=PASS`  
`SOURCE_POSITIVITY_AND_MOMENTS=PASS`  
`PHYSICAL_KERNEL_ERROR_BOUND=UNKNOWN`  
`ORIGINAL_AUTHOR_NATIVE_JULIA_10D=NOT_EXECUTED`  
`SOURCE_VALID_E2B=OPEN`  
`BW_INGEST=GITHUB_PENDING_BW_INGEST`  
`NO_CANON/NO_EXEC_SIGN/NO_NOVELTY/NO_PBH_BOUND`.

**Pierwsza powierzchnia prior art:** Wu–Xu source commit powyżej; host perturbacji operatorów SVD (Weyl/Wedin), modelowanie wrażliwości metodą adjoint. **Druga powierzchnia (wewnętrzna IW):** Mech-S7 ROT013, 020, 021, 023–028; MT/NC/LT target-relative sufficiency i warunki niewystarczalności (bez przypisywania tym wynikom oryginalności). Zapis PUBLIC ≠ ingest BW ≠ aprobata REC/owner ≠ EXEC. Ostateczna decyzja należy do Moderatora.