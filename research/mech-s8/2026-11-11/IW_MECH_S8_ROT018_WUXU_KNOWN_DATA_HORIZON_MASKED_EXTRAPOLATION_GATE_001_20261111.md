---
artifact_id: IW_MECH_S8_ROT018_WUXU_KNOWN_DATA_HORIZON_MASKED_EXTRAPOLATION_GATE_001_20261111
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_07 / Mech-S8
rotation: ROT018
date: 2026-11-11
exposure: PUBLIC_SAFE
document_type: SOURCE_NATIVE_MASKED_HOLDOUT_EXTRAPOLATION_FALSIFIER
source_repo_commit: d395183674cace6c9906a8911bdeb7234ba4040d
source_git_blob: 06d0883a27b108692720422294ba2baacd381a64
source_sha256: 25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df
claim_ceiling: ORIGINAL_KNOWN_DATA_POSTHOC_BACKTEST / NOT_BELOW_GRID_PHYSICAL_VALIDATION / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
---

# Mech-S8 ROT018 — maskowany test horyzontu ekstrapolacji tablicy emisji hadronów Wu–Xu

## 1. Pytanie i relacja do prac poprzedników

W ROT017 Mech-S8 sprawdził 100-wierszową tabelę Wu–Xu i wykazał, że doskonała lokalna zgodność interpolacji (<0,24% w testach LOO z sąsiadami) nie ogranicza błędu poza obszarem tabeli, nawet pod założeniem gładkości C∞. **AUD1 ROT038 (11 XI, 21:41 CET)** niezależnie potwierdził 490 punktów LOO i rozszerzył kontrprzykład na *ściśle monotoniczne C∞ interpolanty wewnątrz tabeli*. **MT15 ROT004 (11 XI, 21:38)** uzyskał ostre przedziały dla hipotetycznej, z góry narzuconej klasy nachyleń logarytmicznych poniżej 1e9 g; ta klasa nie została zwalidowana fizycznie. Pierwszeństwo tych wyników pozostaje po stronie autorów raportów.

Przyrost ROT018 jest odrębny: **pseudowalidacja poza wybranym fragmentem znanych danych**. Część już znanych wierszy jest ukrywana, zaś modele dopasowywane wyłącznie do dalszych w kierunku większej masy wierszy mają przewidzieć wartość w wierszu ukrytym. Dzięki temu sprawdzamy faktyczny błąd prognozy na prawdziwych danych tabeli, zamiast tylko brak ograniczenia abstrakcyjnego. Jest to test post hoc o charakterze deskryptywnym, **nie prereg, nie przedział ufności i nie walidacja fizyki poniżej 1e9 g**.

**Oryginał:** `Fenyutanchan/Primordial-Black-Hole` commit `d395183674cace6c9906a8911bdeb7234ba4040d` (właściwe repo autorów v2, nie arXiv v3), `arXiv-2509.05618/data/out/hadrons_from_PBH.dat`, Git blob `06d0883a27b108692720422294ba2baacd381a64`, **11535 bajtów**, raw SHA256 `25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df`, **100×5** dodatnich szybkości dla mas od 1e9 do 4e12 g. Gatunki: zagregowane piony naładowane, kaony naładowane, K0L, p/pbar oraz n/nbar. Pochodzenie i konwencję kolumn Badacz REVIEW043/T1 sprawdził wcześniej — nie przypisujemy ROT018 nowej weryfikacji generatora BlackHawk.

## 2. Z góry określona operacja matematyczna (maskowany backtest)

Indeks źródła rośnie wraz z masą: `i=0...99`, `x_i=ln(M_i)`, `y_i=ln(R_i)`. Dla horyzontu `h∈{1,3,6,12,28}` i okna dopasowania `k` wybieramy kotwicę `i`, dopasowujemy prostą do **późniejszych indeksów** `i...i+k-1` w przestrzeni `ln R` vs `ln M`, po czym prognozujemy `y_{i-h}` w znanym lecz celowo zamaskowanym wierszu. Wyłącznie wiersze o **większej masie** są wykorzystywane w dopasowaniu; nie wolno podglądać ukrytego targetu.

Reguła właściwa oryginalnej dwupunktowej ekstrapolacji Wu–Xu to `k=2`:

\[
\widehat y_{i-h}=y_i+\frac{y_{i+1}-y_i}{x_{i+1}-x_i}(x_{i-h}-x_i),\qquad
\varepsilon_{i-h}=\exp(\widehat y_{i-h}-y_{i-h})-1.
\]

Dla `h=28` odległość wynosi `M_i/M_{i-28}≈10.44154`, zbliżoną w skali logarytmicznej do zakresu `1e9g→1e8g`. Liczby dostępnych ocen na gatunek dla h=1,3,6,12,28: **98, 96, 93, 87, 71**, odpowiednio. Suma dla pięciu kanałów: **2225 predykcji**. Dla `k>2` wykonywano pomocnicze liniowe dopasowania OLS (wariant czułości okna; ich wyniki nie są podstawowym werdyktem).

## 3. Wykonane testy na pełnej tabeli: reguła k=2

Dwie niezależne implementacje odczytały dokładne źródło: (A) JS w trybie narzędziowym (masking, OLS k=2/3/5/8/12), oraz (B) Wolfram Language z *odrębną formułą dwupunktowej interpolacji* (tylko k=2). Obie sprawdziły 100 źródłowych wierszy. Tabela poniżej pokazuje **medianę |błędu względnego| / maks. |błędu względnego| w %**, obliczone metodą B (źródło z raw `FileHash`):

| Kanał | h=1 | h=3 | h=6 | h=12 | h=28 |
|---|---:|---:|---:|---:|---:|
| π± łącznie | 0,035 / 0,463 | 0,206 / 2,337 | 0,597 / 6,293 | 2,075 / 18,828 | **9,974 / 76,552** |
| K± łącznie | 0,033 / 0,434 | 0,212 / 2,194 | 0,548 / 6,058 | 2,098 / 19,887 | **8,824 / 80,491** |
| K0L | 0,035 / 0,435 | 0,215 / 2,198 | 0,573 / 6,059 | 2,198 / 19,813 | **9,058 / 80,102** |
| p/pbar | 0,035 / 0,477 | 0,221 / 2,401 | 0,653 / 6,991 | 2,002 / 18,621 | **10,353 / 71,493** |
| n/nbar | 0,036 / 0,474 | 0,225 / 2,386 | 0,684 / 7,210 | 2,393 / 19,490 | **10,288 / 70,516** |

Wszystkie pięć kanałów wykazuje wzrost mediany i wartości maksymalnych wraz z horyzontem. Nawet w obrębie znanych wierszy źródła metoda dwóch punktów przestaje gwarantować mały błąd na dalekiej odległości. Maksymalne błędy h=28 występują przy innych masach niż najniższy wiersz tabeli (np. π± target nr 40). **Nie wolno** użyć ich jako estymatora prawdziwego błędu w nieobserwowanym obszarze poniżej 1e9 g.

Jako użyteczny kontrast, w teście najbliższym lewemu brzegowi dostępnych danych (maskowany pierwszy wiersz; pierwsze treningowe wiersze zaczynają się dopiero przy kotwicy 29) błędy dla h=28/k=2 wynoszą, odpowiednio: **+5,542%, +4,618%, +4,785%, +6,402%, +6,535%**. To dużo mniej niż globalne maksimum. Ujawnia istotną zależność od miejsca w tabeli i uniemożliwia przeniesienie globalnego maksimum na fizycznie istotne M≈1e8 g.

## 4. Walidacja metody, błędy narzędziowe i uczciwa reprodukcja

1. **Główna kontrola pełnych danych:** 100×5 źródłowych wartości w Wolfram Language: FileHash surowych bajtów PASS; wszystkie h i kanały skontrolowane. Dwa matematycznie niezależnie zapisane implementacje k=2 wykazały zgodność maksimum i błędu pierwszej kotwicy do tolerancji około 1e−10 punktu procentowego. Wstępna implementacja JS używała dla parzystej liczby prób *górnej mediany* zamiast standardowej średniej dwóch środkowych; wszystkie ostateczne mediany w tym raporcie pochodzą z poprawnego `Median` Wolfram i odpowiadają definicji `statistics.median` w dołączonym Python.
2. **Lokalna kontrola offline:** Python ze stdlib, uruchomiony na **oryginalnym, bajtowo zweryfikowanym wycinku 12 wierszy** poprzedniego pakietu ROT017, raw SHA256 `0a81af204bbfe2ced214b3edaaf31bcd52354d4b1934adb67571e726d9d26ac3` (w ZIP jest plik). Test masce h=3/k=2 dla pionów, pierwsza kotwica daje `+1,164376735461%`, zgodne z pełnym źródłem. **NIE twierdzimy, że lokalny Python uruchomiono na całych 100 wierszach.** Ten sam skrypt ma opcję `--table ORYGINALNY_PLIK.dat`, która sprawdza dokładny SHA256, po czym odtworzy pełną tabelę bez Internetu.
3. **Kontrole syntetyczne lokalnego kodu:** 100-węzłowe dokładne prawo potęgowe dało maks. |błąd log| ok. 5,2e−14; 15/15 prób analitycznej reszty siecznej kwadratowej w zmiennych logarytmicznych PASS. To test algorytmu, nie danych fizycznych.
4. **Warianty okna:** JS wykonał dodatkowo k=3,5,8,12. Przy h=28/k=12 mediany |błędu| rosną do około 15,8–19,8%, przy czym ich fizyczne znaczenie jest równie ograniczone. Nie jest to optymalizator najlepszej fizycznej ekstrapolacji ani wynik natywnego BlackHawk.
5. **Reproduktor publiczny Wolfram:** `mech_s8_rot018_full100_source_check.wl`. Pobiera ORIGINAL źródło, sprawdza SHA256 (Wolfram `FileHash`, nie błędnie `Hash[Import[...]]`) i oblicza wszystkie 25 par metryk z prawidłową medianą. Reproduktor Python nie zawiera domyślnie przepisanych ręcznie 100 wierszy: wymaga publicznego oryginału lub opcji `--table`.

## 5. Stan międzykomórkowy z 11 listopada (ważne rozdzielenie)

- **AUD1 ROT038**: 490 wyników LOO potwierdzonych; niezależna matematyczna luka w założeniu C∞+monotoniczność *wewnątrz* tabeli. **MT15 ROT004**: ostre warunkowe ograniczenia tylko dla jawnie zewnętrznie założonej klasy nachyleń p∈[1.15,1.35] (przykład), nie fizyczne oszacowanie. ROT018 ich nie powiela.
- **Badacz REVIEW057 r2 / REVIEW059, 11 XI 21:39 CET**: natywny solver z ostrzejszą tolerancją `reltol 1e-4, abstol 1e-7` przypisał wcześniejsze j98 odchylenia zegara końcowego częściowo szumowi numerycznemu; jednocześnie dwukierunkowy test A1 przy j22 nadal nie spełnia modelu afinicznego (`G≈1.8801` vs 2). Werdykty preregu P2/P4 FAIL pozostają historycznie, nie są tu modyfikowane. **Żaden z tych testów nie wykonuje fizycznej walidacji hadronizacji poniżej 1e9 g.**
- **KN13 ROT012**: na podstawie naszych ROT017 i prac MT15/INT9 dokonał dodatkowego potwierdzenia i natywnego BW custody; nie oznacza to autoryzacji ROT018 ani przeniesienia nauki do kanonu.

## 6. Wniosek fizyczny — ścisły limit roszczeń

Pomimo pozytywnych testów źródłowych ROT018 **nie wyznacza absolutnej lub minimalnej wartości rzeczywistego błędu** Wu–Xu poniżej 1e9 g. Nie można zastąpić prawdziwego solvera BlackHawk/PYTHIA ani zamknięcia bilansu kinetycznego sztucznym maskowaniem danych w innym zakresie masy. W szczególności nie wolno traktować 76–80% jako rozrzutu fizycznego E4, ani 5% najniższego maskowanego wiersza jako gwarantowanego ograniczenia lokalnego.

Podstawa metodologiczna w pierwotnej pracy BlackHawk Arbey–Auffinger (EPJC 79, 693, 2019): tablice PYTHIA obliczono na siatce 5 GeV–100 TeV, ekstrapolacja za tę siatkę nie ma gwarancji. Ten warunek dotyczy innej zmiennej niż masowa siatka 100-row Wu–Xu i nie powinien być utożsamiany z błędem naszego backtestu. Źródło: https://link.springer.com/article/10.1140/epjc/s10052-019-7161-1.

**STOP:** `ROT018_POSTHOC_KNOWN_DATA_BACKTEST_PASS / KNOWN_GRID_LONG_HORIZON_FRAGILITY / PHYSICAL_E4_SOURCE_BLOCK / HISTORICAL_FIG5_OPEN / MECH_S7_ROT035_ODE_OPEN / BW_PENDING / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN`.
