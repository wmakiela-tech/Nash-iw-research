---
artifact_id: IW_MECH_S8_ROT019_WUXU_REVIEW061_ROOT_EXTRACTION_METHOD_AND_LOO_CUSTODY_AUDIT_001_20261111
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_07 / Mech-S8
date: 2026-11-11
exposure: PUBLIC_SAFE
type: INDEPENDENT_METHOD_FALSIFIER_AND_PREREG_SOURCE_CUSTODY
source_author_code: Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d
source_badacz_review: IW_BADACZ_WUXU_SUBEDGE_EXTRAPOLATION_NATIVE_ROOT_REVIEW_061_20261111
source_badacz_commit: 47a8b457b90dd24886d2a5a96667aaf659dcccfd
claim_ceiling: ORIGINAL_CSV_ROOT_EXTRACTION_METHOD_ROBUSTNESS_ONLY / NO_NEW_NATIVE_JULIA / NO_SOLVER_TOLERANCE_PROOF / NO_E4_SOURCE_UNBLOCK / NO_PHYSICAL_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# Mech-S8 ROT019 — niezależny audyt ekstrakcji korzeni w natywnym teście Wu–Xu REVIEW061

## 1. Pierwszeństwo i aktualność

**Badacz REVIEW061 jest właścicielem pierwotnego natywnego eksperymentu** przy zmodyfikowanej ekstrapolacji pięciu stóp hadronów poniżej źródłowego progu M=10⁹g. Prerejestracja PREREG060 została zapisana jako commit
`bdd9df5ec5ca56d4558cba48e96b682b1b9066ea`, data w metadanych GitHub `2026-11-11T20:48:32Z`. Skrypt analizy jako osobny commit
`e9febb732a7406fbfc9d3740aa8426f6a66c0dd6`, `2026-11-11T20:53:02Z`; autor określił obie zmiany jako dokonane przed odczytem wyniku wariantu λ=1. **Nie zamieniam chronologii Git w pełny dowód ślepego preregu.** Rzeczywiste wyniki są w `research/badacz/2026-11-11/` pod commitem
`47a8b457b90dd24886d2a5a96667aaf659dcccfd`.

- [Oryginalna prerejestracja PREREG060](https://github.com/wmakiela-tech/Nash-iw-research/blob/bdd9df5ec5ca56d4558cba48e96b682b1b9066ea/research/badacz/2026-11-11/IW_BADACZ_WUXU_SUBEDGE_EXTRAPOLATION_NATIVE_ROOT_PREREG_060_20261111.md)
- [Pierwotny raport REVIEW061 Badacza](https://github.com/wmakiela-tech/Nash-iw-research/blob/47a8b457b90dd24886d2a5a96667aaf659dcccfd/research/badacz/2026-11-11/IW_BADACZ_WUXU_SUBEDGE_EXTRAPOLATION_NATIVE_ROOT_REVIEW_061_20261111.md)

Badacz jako pierwszy wyznaczył native Δlog₁₀β:
- j22: −0.03620301172933438 dex przy `1e−4:1e−7` (root-SE dopasowania Δ=0.00273549562229);
- j28: −0.026959232512879794 dex (root-SE dopasowania Δ=0.00216070859620).
Preregistrowane okna: j22 [−0.07513393682254521,−0.009736483991748484], j28 [−0.06231583371703794,+0.0022229058910954586]. Oba **PASS**. To **przesunięcie granicy modelu po zmianie ekstrapolacji**, NIE fizyczny błąd źródła, NIE granica PBH.

**Nowość ROT019:** test, czy znak i zakres tego wyniku zależy od arbitralnego wyboru regresji 7-punktowej.

## 2. Materiał pierwotny i kontrola źródła

Z publicznego GitHub API pobrałem dwa przypięte pliki CSV:
- `data/subedge060_p1.csv` blob `e8dc7702a4a4764fa8b3bffea64199b3258ffe0d`
- `data/subedge060_p2.csv` blob `99d5efca315e34ad77e2cfc602bff88785df548a`

Każdy zawiera bazę i ramp (`j=22` albo `28`), z serią `bracket`, `bisect` i siedmioma punktami `phase=fit`; **łącznie 4×7=28 oryginalnych wartości wejścia** dla niniejszego testu. Oryginalny skrypt Badacza `code/wuxu_subedge060_analysis.py`, blob `40cd07d8cdd1eebdc6148bbb5966c50cc9d247c7`, stosuje liniowe OLS `Y_C=a+b log10β` dla siedmiu punktów.

W reproduktorze ROT019 28 par `(x,Y_C)` jest transkrypcją z oryginalnych CSV, a obliczenia używają niezależnego, centrowanego OLS ze standardowej biblioteki Python, nie kodu NumPy autora. Odrębny bezpośredni odczyt tych samych źródeł i centrowane OLS wykonano w narzędziu GitHub/JS.

Odtworzono wszystkie cztery opublikowane korzenie i wszystkie cztery `SE(root)` z dokładnością lepszą niż 1e−10 (różnice korzeni ~1e−14). Wyliczenie root-SE wykorzystuje jawnie wariancję OLS
\[
\mathrm{SE}(r)^2=\frac{\sigma_r^2}{b^2}
\left[\frac1n+\frac{(r-\bar x)^2}{\sum_i(x_i-\bar x)^2}\right],
\]
a nie domniemany całkowity błąd solvera.

## 3. Cztery niezależne reguły ekstrakcji

| Metoda | Δ j=22 [dex] | Δ j=28 [dex] |
|---|---:|---:|
| OLS 7 (preregistered) | -0.036203012 | -0.026959233 |
| OLS central 5 | -0.035987994 | -0.028160686 |
| OLS central 3 | -0.036904800 | -0.028036296 |
| Neighbouring-value secant | -0.042551487 | -0.029208787 |

Wszystkie osiem wyników jest **ujemnych i mieści się w pierwotnie zadeklarowanych oknach falsyfikacyjnych P1/P2**.

Największa zmiana przesunięcia względem deklarowanego OLS7 wśród czterech metod:
- j22: **0.006348475706 dex**, występuje przy interpolacji sąsiedniej pary;
- j28: **0.002249554750 dex**.

To odrębny, empiryczny **error bar wyboru algorytmu wyznaczania granicy** (na tych samych punktach), nie rozrzut integratora, więc nie wolno dodawać/odejmować go mechanicznie od SE ani traktować jako ścisłego przedziału ufności.

## 4. Test usuwania danych: 49 par na masę początkową

Dla każdego `j` usunięto jeden spośród siedmiu punktów bazy i niezależnie jeden spośród siedmiu punktów wariantu, następnie ponownie dopasowano dwie proste na 6 punktach. **7×7=49 par na `j`, 98 alternatywnych kontrastów łącznie**.

| j | Minimum Δ [dex] | Maksimum Δ [dex] | Wszystkie 49 w oknie preregu? |
|---:|---:|---:|---|
| 22 | -0.039417598 | -0.033725566 | TAK |
| 28 | -0.029658492 | -0.025124603 | TAK |

Test obejmuje także siedem usunięć z tym samym indeksem punktu. Wszystkie wyniki zachowują znak. To kontrola diagnostyczna oparta na **tej samej próbie**; 49 wyników nie jest 49 niezależnymi wykonaniami modelu.

## 5. Falsyfikator nadmiernego twierdzenia o fizyce

Badacz REVIEW061 jawnie wykazał, że nawet różnica ~3.6×10⁻¹⁵ w zmiennej `log10β`, ukryta przez format drukowania CSV `%.6f`, potrafi zmienić `Y_C` o około 3.2×10⁻⁵. Przy nachyleniach OLS może to przekładać się na rozrzut na poziomie kilku tysięcznych dex, zależny od sposobu sterowania integratorem. W REVIEW059 badacz osobno zbadał tolerancję dla innego wariantu perturbacji źródła (D0/D2). **Nie przeprowadził dotąd porównania tolerancji dla dokładnie tego wariantu p12.**

Zatem PASS czterech metod ekstrakcji i wszystkich 49 par usunięć **nie certyfikuje powtarzalności natywnego przesunięcia pod zmianą tolerancji**. Nie wolno składać ±0.0027 dex z SE dopasowania jako pełnego błędu fizycznego. W dwóch badanych punktach przesunięcie i jego znak są odporne na wybór metody *ekstrakcji z zastanych 28 danych*, nie na nieprzetestowane warunki integratora.

**Aktualny priorytet E4:** fizycznie uzasadniona emisja BlackHawk/PYTHIA poniżej 10⁹g i na końcu parowania nadal **niedostępna**. Nie da się wyznaczyć rzeczywistego błędu PBH β z porównania `p2↔p12`, nawet gdy przesunięcie modelowe jest odporne numerycznie na zmianę algorytmu regresji.

## 6. Dyspozycja

`ROT019 METHOD_EXTRACTION_PASS / ORIGINAL_BADACZ_NATIVE_FIRST / PREREG_GIT_CHRONOLOGY_PASS / PHYSICAL_E4_SOURCE_BLOCK / NATIVE_p12_TOLERANCE_LADDER_PENDING / HISTORICAL_FIG5_PRODUCER_OPEN / ROT035_ODE_OPEN / BW_PENDING / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN`.

Nie kieruję ponownego zlecenia wykonania zakończonego natywnego testu Badacza. Ewentualna nowa drabina tolerancji dla p12 wymaga osobnej decyzji i budżetu właściciela. Brak postulatu pierwszeństwa fizycznego lub odkrycia prawa.
