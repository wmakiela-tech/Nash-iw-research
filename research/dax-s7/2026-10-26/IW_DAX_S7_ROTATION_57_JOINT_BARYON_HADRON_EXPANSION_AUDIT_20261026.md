# IW/NASH — DAX-S7 — obrót 57: wspólna kontrola baryonów i ekspansji hadronów

**Data:** 2026-10-26  
**Status:** `SOURCE_EQUATION_PORT / FINITE_HADRON_EIGHT_ARM / FULL_JULIA_NOT_RUN / NO_CANON`.

## Pytanie falsyfikujące obrót 55

Czy różnica Xn wynikająca z poprawki nB z obrotu 54/55 przestaje występować po dodaniu brakującego w oryginalnym kodzie terminu rozcieńczania `-3H*n_h` do sześciu równań hadronów?

**Wynik: nie, w warunkowym porównaniu źródłowego podukładu.** Poprawka baryonowa pozostaje dominująca.

## Metoda i provenance

Źródła: [main-scan.jl](https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/main-scan.jl), [tool_script-parameters.jl](https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/tool_script-parameters.jl), trzy oryginalne tabele g*(T) i `data/out/hadrons_from_PBH.dat`. Blob SHA czterech plików podany w manifest. Dla M_init=9.6725e9 g i 10 wartości β (0, 1e-20, 5e-20, 1e-19, 2e-19, 3e-19, 5e-19, 1e-18, 3e-18, 1e-17) obliczono osiem wariantów: źródłowe nB kontra nB*a³=const; sześć populacji jawnych w czasie kontra kwazistacjonarne; z/bez terminu 3H w efektywnej szybkości zaniku. Razem 80 ramion Xn na pierwszym przekroczeniu Tnuc.

Tło: 10000 kroków pierwszego segmentu + 12000 końcowego, wspólne dla wariantów z danym β. Hadrony jawne: `n'=S-(D+optional_3H)*n`, kontrola podkroków metodą dokładnego wykładniczego update dla zamrożonych współczynników i midpoint dla Xn. Bariony w ramieniu konserwacji: normalizacja z tym samym nB przy **pierwszym** przejściu Tnuc; nie jest to fizycznie niezależne wyznaczenie ηB.

## Przykład: β=3e-19

| Ramiona jawnych sześciu hadronów | Xn |
|---|---:|
| nB źródłowe, bez 3H | 0.1251319493319071 |
| nB źródłowe, z 3H | 0.12513193729706112 |
| nB*a³ konserwowane, bez 3H | 0.1225598596447421 |
| nB*a³ konserwowane, z 3H | 0.12255985015911582 |

`ΔXn_baryon=-0.002572089687165005`; `ΔXn_expansion_source=-1.2034845980890552e-8`; `ΔXn_expansion_conserved=-9.485626284444493e-9`. Względna hierarchia: ~213720×. Interakcja poprawek ≈ +2.54922e-9 w Xn. Wariant quasi-stacjonarny potwierdził podobne różnice sparowane na tej samej siatce. Przy β=1e-17 bezwzględna różnica od samego 3H wynosi około 9.65e-8, a od samego nB około 0.02096.

**Algebraiczne wskaźniki tylko do porównania:** dla β=3e-19 zmiana `2Xn` wynosi -0.00514418, a zmiana `2Xn/(1-Xn)` wynosi -0.00670125. To nie są wyniki pełnej sieci reakcji BBN ani nowe fizyczne ograniczenia PBH.

## Granice wiedzy i przywracalność

- Nie uruchomiono oryginalnej Julii ani pełnej sieci nuklearnej. Nie wolno przyznawać statusu EXEC, kanonu lub prawa do nowych limitów PBH.
- Zmiana ekspansyjna rzędu 1e-8 to sparowana różnica na jednym zagęszczeniu kroków: **nie wykazano odrębnej zbieżności względem kroku dla pełnej macierzy**. Algebraiczna kontrola 3H/D w obrocie 56 oraz porównanie QS i skończonych populacji wspierają jedynie skalę efektu.
- Przy końcu parowania istnieje zależność od ekstrapolacji źródłowej tabeli hadronów poniżej 1e9 g.
- Przepis `nB*a³=const` wymaga modelowego założenia o baryonowym źródle/netto, a normalizacja przy Tnuc nie jest niezależną kalibracją BBN.

**Reprodukcja:** `IW_DAX_S7_ROTATIONS_56_57_EXPANSION_DILUTION_FULL_PORT_20261026.py` z `--download --batch-study --joint-audit` (źródłowe SHA sprawdzane). Plik `IW_DAX_S7_ROTATION_57_JOINT_BARYON_HADRON_EXPANSION_MATRIX_20261026.csv` zawiera pełną macierz 80 ramion. Skrypt przechodzi `py_compile` i `--selftest`; batch obliczono niezależnie w środowisku z dostępem do treści przez podłączone GitHub API.

**Werdykt:** `BARYON_EFFECT_PERSISTS / EXPANSION_DILUTION_SUBLEADING / FULL_JULIA_NOT_RUN / NO_CANON`.
