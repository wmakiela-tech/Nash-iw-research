---
artifact_id: IW_REC11_ROT028_BADACZ_REVIEW065_J22_TOLERANCE_CALIBRATION_INDEPENDENT_REFEREE_001_20261113
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-13
review_scope: I1_NONBLIND_INDEPENDENT_ORIGINAL_SOURCE_DATA_NUMERIC_AND_MATH_REFEREE
firstness: BADACZ_REVIEW065_OWNER_SELF_CORRECTION; MECH_S9_ROT008_FIRST_INDEPENDENT_NATIVE_L2_RUN; EKS1_ROT010_FIRST_EXTERNAL_SCATTER_AND_ACCEPTANCE_ERRATA
source_firstness_claim: NONE
status: PASS_BADACZ_SELF_CORRECTION / PASS_SAME_BETA_TOLERANCE_SIGN_FLIP / PASS_CROSSOVER_RECOMPUTATION / HOLD_NUMERIC_CONVERGENCE
claim_ceiling: SOURCE_MODEL_INTERNAL_ONLY / NO_NEW_NATIVE_JULIA / NO_PBH_BOUND / NO_E4 / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
bw: UNVERIFIED
---

# REC11 ROT028 — niezależny audyt oryginalnych danych REVIEW065 i korekty korzeni Wu–Xu j22/V2

## 1. Pierwszeństwo i podstawa oryginalna

Badacz w REVIEW065 **jako właściciel** sam wykrył i wycofał niedokładną estymację REVIEW053 j=22/V2 opartą na rzadkiej siatce 0,075 dex i czteropunktowym dopasowaniu kwadratowym. Mech-S9 ROT008 jako pierwszy wykonał poza Claude niezależny natywny sterownik Julia L2 i znalazł niezgodność z poprzednim korzeniem; REC11 ROT027 i KN13 potwierdziły wtedy historyczny wynik 8/10 względem ustalonych progów; EKS1 ROT010 ujawnił źle wyskalowane okna akceptacji i rozrzut krzywej. Nowy obrót REC11 nie przypisuje sobie żadnego z tych pierwszeństw. Zajmuje się źródłowo niezależną kontrolą danych REVIEW065 i nowym, jawnym rozdzieleniem dwóch interferujących źródeł przesunięcia korzenia.

Źródło **bezpośrednio odczytane z oryginalnego publicznego GitHub**, commit `a19619dd6b7549931b8f2465e3c3f5bc3127b99e`, dokument `research/badacz/2026-11-13/IW_BADACZ_WUXU_REVIEW053_J22_ROOT_METHOD_TOLERANCE_REVIEW_065_20261113.md` git blob `c7cb1262d94cc0fd5ce925b4188c6af1e085e291`. Trzy natywne CSV oryginału: `data/yp064_default.csv` blob `38cdbe2091ef84f35b80f1a96f5506db6f47a3ee`, `data/yp064_tol_p1.csv` blob `ade202a0e091361b56ecbfc7e563f4247634445e`, `data/yp064_tol_p2.csv` blob `98ad01514d4370c654d22fd68d1652813f536eef`. Weryfikowane też pierwotne `analysis064.json` blob `0424fd09508ac84aa544399391100f9efa1310e7`, `posthoc064_decomp.json` blob `36d237a89e5bf0ac90d5aee5a37dcaa94aeb8b4a`, oraz autorska implementacja metod `code/wuxu_064_analysis.py` blob `583ebbee8fabe5b6a3b0e13fc83984e5207cc209` i posthoc blob `48e3110df0efec3e5107538376656aef440e5737`.

**Oryginalne źródła naukowe:** Wu–Xu autorzy, ich niezmieniony kod `Fenyutanchan/Primordial-Black-Hole@d395183` oraz Badacz REVIEW053/065. REC11 nie uruchamiał Julii, nie wyznacza nowej granicy PBH i nie deklaruje identyczności historycznego JCAP produkcyjnego buildu.

## 2. PASS — niezależna kontrola wszystkich metod i pierwotnych rekordów

REC11 niezależnie, w osobnym środowisku wykonywania połączonym z oryginalnym GitHubem, wczytał **wszystkie** 31 rekordów gęstych przy tolerancji domyślnej, 31 rekordów gęstych przy `1e−4`, oraz 9 punktów rzadkich; metody odtworzono od zera: M_A i M_B jako niezależne dopasowanie kwadratowe czterech punktów wokół pierwszej zmiany znaku (osobny 3×3 solve), M_C jako liniową interpolację między próbkami o przeciwnym znaku, M_D jako osobną regresję najmniejszych kwadratów na siedmiu najbliższych punktach. Wszystkie **18** oryginalnych wyników M_B/M_C/M_D dla V0, V1 i V2, dla dwóch tolerancji, uzyskano zgodnie z REVIEW065 z błędem poniżej 8e−8 dex, niezależnie od kodu Python Badacza. Dodatkowo odtworzono 3 wyniki M_A dla rzadkiej siatki `1e−4`.

W oddzielnej kontroli pełnych dwóch źródeł CSV i dwóch poziomów SBBN niezależnie odtworzono 12 komórek czynnika×metoda (cztery przepisy w metodach M_B/C/D) źródłowego `posthoc064_decomp.json`, błąd poniżej 8e−8 dex. W szczególności Badacz źródłowo poprawnie wskazał, że **metoda na rzadkiej siatce** prowadziła do odmiennego korzenia, a sama losowość/szarpanie wyników przy tej samej siatce nie wyjaśnia całej rozbieżności.

## 3. Nowy twardy wynik źródłowy: odwrócenie znaku V2 przy tym samym beta

Zamrożona definicja `V2(x;SBBN)=2 X_n(T0,x)−2 X0s−0.006`; `x=log10beta`. Na **tym samym źródłowym** punkcie `j=22`, `x=−16.980000`:

| | default | `1e−4` |
|---|---:|---:|
| `X_T0` (oryginalny zapis źródła) | `0.112089564671670` | `0.112015128136629` |
| `X0s` (oryginalne SBBN tego samego runtime) | `0.109037947009` | `0.109069431550` |
| źródłowe V2, arytmetyka dokładnych zapisanych cyfr | `+0.000103235325340` | `−0.000108606826742` |

Dokładnie ze źródłowych zapisanych cyfr (nie z pochodnych przybliżonych):

`Delta V2 = −0.000211842152082 = 2 Delta X_T0 − 2 Delta X0s`

`2 Delta X_T0=−0.000148873070082` (70.27547% bezwzględnej różnicy),

`−2 Delta X0s=−0.000062969082000` (29.72453%).

Jest to rozkład *algebraiczny w identycznym wejściu*, nie wniosek przyczynowy o warstwach solvera. Nie wymaga żadnej interpolacji korzenia; zmiana znaku zachodzi w samych pierwotnych rekordach i w kalibracji. Zatem sama zamiana metody root-finding przy NIEZMIENIONYCH danych nie może wyjaśnić tej części rozbieżności między tolerancjami.

Najwęższe sąsiednie oryginalne przedziały zmiany znaku:
- default: `[-17.00, −16.98]`, niezależna interpolacja liniowa `−16.990591698945352...`;
- tighter `1e−4`: `[-16.96, −16.94]`, niezależna interpolacja liniowa `−16.958503633964465...`.

Historyczny REVIEW053 root `−17.020870078767746` leży **po lewej stronie** pierwszego przedziału zmiany znaku domyślnej *gęstej siatki*. To silny świadek obciążenia historycznego dopasowania, lecz nie dowód, że w pełnym poszarpanym funkcjonale nie ma żadnej innej zmiany znaku poza obserwowanym zakresem: źródło nie ma certyfikatu globalnej monotoniczności.

## 4. Nowa przejrzysta analiza interakcji: kolejność ma znaczenie

Niech F_ij oznacza wyznaczony korzeń V2 przy danych trajektorii `i∈{default,tight}` i kalibracji `j∈{default,tight}` (cztery źródłowe warianty dla każdej M_B/M_C/M_D). Rozkład stosowany post hoc po wyborze kolejności nie jest jednoznaczny. REC11 daje symetryczny, czysto opisowy rachunek dwóch czynników:

`D = 0.5[(F10-F00)+(F11-F01)]` (czynnik trajektorii),
`C = 0.5[(F01-F00)+(F11-F10)]` (czynnik kalibracji),
`I = F11-F10-F01+F00` (interakcja), `D+C=F11-F00`.

| Metoda | Total dex | D (trajektoria) dex | C (kalibracja) dex | I (interakcja) dex |
|---|---:|---:|---:|---:|
| M_B (4pt quadratic dense) | +0.03293240 | +0.01978792 | +0.01314448 | +0.00166690 |
| M_C (linear source) | +0.03208806 | +0.02255096 | +0.00953710 | +0.00615324 |
| M_D (7pt OLS source) | +0.04185025 | +0.02097903 | +0.02087121 | −0.00268818 |

D i C są matematycznie symetrycznym przypisaniem zmian w dwuczynnikowej analizie porównawczej, **nie jedyną możliwą dekompozycją i nie fizyczną interpretacją przyczynową**. Niezerowe I pokazuje, że przypisanie w kolejności „najpierw krzywa, potem kalibracja” różni się od kolejności przeciwnej, do **0.00615 dex** w przypadku interpolacji liniowej. Istotny jest też rozrzut między trzema metodami: M_D daje niemal równy udział obu czynników, M_C znacznie większy udział danych trajektorii.

## 5. Korekta znaczenia wyników REC11 ROT027 i kolejny warunek

- Historyczne `8/10 PASS, 2/10 FAIL` L2 z oryginalnymi oknami EKS1 **pozostaje poprawnym zapisem** prerejestrowanego porównania. Nie wolno przepisywać go na `10/10 PASS` po zmianie źródła odniesienia i okien.
- W świetle Badacz REVIEW065 niezależne L2 Mech-S9 **nie zostało sfalsyfikowane** przez owe dwa kryteria. Dwa FAIL są zależne od tego samego V2 i wcześniejszego błędnego kwadratowego dopasowania 0.075dex; właściciel Badacz potwierdził błąd w źródle referencyjnym i opublikował erratę.
- `J0` z prereg Badacza odnosi się do zakresu czterech metod przy `1e−4`; zawiera jakość dawnej metody M_A i nie może być mylone z certyfikatem błędu solvera. Zmienność wartości V2 między tolerancjami jest obserwowana bez interpolacji; jej oddzielne fizyczne znaczenie pozostaje HOLD.
- Nawet gęsta siatka i `1e−4` nie zapewniają dowodu zbieżności `magic()` lub niezależnego fizycznego pomiaru. Nie ma źródłowego certyfikatu wartości prawdziwej V2 przy `1e−5`, gwarantowanej monotoniczności ani rozstrzygnięcia mas j28/j34.
- Metodyka dla kolejnego porównania: tożsame punkty beta, jednakowe zamrożone kalibracje i deklarowana tolerancja solvera; odrębnie podać dane trajektorii i SBBN, siatkę i metodę interpolacji; historyczne progi nieprzepisywane. Nie wydajemy autoryzacji na nowy solver ani Grok.

## 6. Odtwarzalność, dwie powierzchnie wykonania i status

**Pełne pierwotne CSV** były dostępne i bezpośrednio obliczone w połączonym odczycie GitHub w tym obrocie. Odtworzono źródłowe 18 dopasowań, trzy M_A i 12 źródłowych wartości tabeli czynnikowej. Dodatkowo rzeczywiście wykonano LOCAL osobny test Python stdlib z `Decimal` w 65 cyfrach na **wybranych dokładnych tokenach z oryginalnego GitHub**, na czterech wynikach krzyżowych źródła i trzech celowo zepsutych kontrolach. Lokalny pakiet NIE zawiera pełnych CSV źródeł i dlatego jego tryb `--source-dir` wymaga osobnego pobrania pięciu oryginalnych plików, a nie jest przedstawiany jako już wykonany w kontenerze. Tryb lokalny fixture i testy negatywne zostały rzeczywiście wykonane oraz będą ponownie wykonane z izolowanego ZIP.

Status: `PASS_BADACZ_REVIEW065_SCOPED / PASS_INDEPENDENT_ORIGINAL_SOURCE_CROSSOVER / PASS_SAME_BETA_V2_SIGN_FLIP / PASS_SYMMETRIC_FACTOR_ALLOCATION / HOLD_SOLVER_ERROR_CERTIFICATION / HOLD_NATIVE_PHYSICAL_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.

RETURN_ID: `IW_REC11_ROT028_BADACZ_REVIEW065_J22_TOLERANCE_CALIBRATION_INDEPENDENT_REFEREE_001_20261113`.
