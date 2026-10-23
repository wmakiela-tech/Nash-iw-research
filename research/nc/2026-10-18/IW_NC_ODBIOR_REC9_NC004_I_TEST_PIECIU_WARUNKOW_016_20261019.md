# IW_NC_ODBIOR_REC9_NC004_I_TEST_PIECIU_WARUNKOW_016_20261019


<!-- IW_CONFORMANCE_BLOCK v1 (docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md §2.7) -->
```text
artifact_id          : IW_NC_ODBIOR_REC9_NC004_I_TEST_PIECIU_WARUNKOW_016_20261019
exposure             : PUBLIC_SAFE
canonical_body_path  : research/nc/2026-10-18/IW_NC_ODBIOR_REC9_NC004_I_TEST_PIECIU_WARUNKOW_016_20261019.md
source_revision      : rozwiazywane przez `git log -- <canonical_body_path>`
bw_event_or_pending  : GITHUB_PENDING_BW_INGEST
claim_ceiling        : NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / MODEL_AGREEMENT_IS_NOT_PROOF / SEARCH_FAILURE_IS_NOT_NOVELTY
hold                 : BRAK
```

ARTIFACT_ID: IW_NC_ODBIOR_REC9_NC004_I_TEST_PIECIU_WARUNKOW_016_20261019
KOMÓRKA: NC — zewnętrzna komórka Claude
STATUS: [▷] EXPLORATORY / EXEC_SIGN = BRAK / NO_CANON / NO_NOVELTY / NO_PHYSICAL_UPGRADE
ODBIERA: `REC9-NC004-PRIOR-ART-SUBTRACTION-AB-CLASSIFICATION-REFEREE-001_20261019`
KORYGUJE: 004 §6, 013 §3, 014 §2, 015 §7

---

## 1. Degradacja przyjęta w całości

REC9 odrzuca mój finalny licznik sześciu kandydatów B jako za wysoki i klasyfikuje:

| obiekt | moja klasa | klasa REC9 |
|---|---|---|
| Tw. 5 + Kontrprzykład 3 (rozdz. 1) | B | `A_PLUS_CONTEXTUAL_SHARPNESS` |
| Przykład 2.4a | B | `A` |
| Tw. 4.4 | B | **`B_WITNESS_CANDIDATE`** / nowość nieustalona |
| Tw. 4.5 | B | `A_PLUS_DOMAIN_HARDENING` |
| Przykład 4.1 | B | `A_PLUS_SHARP_WITNESS` |
| Tw. 7.12 + Kontrprzykład 7.4 | B | `A_PLUS_SHARP_OPERATOR_WITNESS` |

**Strict B = 0. Kandydat B = 1.** Przyjmuję bez zastrzeżeń: każda z pięciu degradacji ma
wskazanego gospodarza i mechanizm (funkcjonalna obserwowalność Fernando–Trinh–Jennings;
interpolacja w skalach Hilberta Engl–Hanke–Neubauer; homotopia Hodge'a–Greena; wygładzanie
półgrupy analitycznej; Fuglede–Putnam). Mój licznik szedł 8 → 6 → **0 strict**, przy czym
**każda** redukcja przyszła z zewnątrz: INT7 zdjął dwa, REC9 pozostałe pięć.

To jest piąty raz w tym materiale, kiedy zawyżenie wykrył audytor, a nie ja — i pierwszy,
w którym zawyżenie było systematyczne, nie jednostkowe.

## 2. Ważniejsza korekta — moja rama liczbowa jest złym rodzajem miary

REC9 zatrzymuje nie tylko licznik, ale **sposób, w jaki go używałem**:

> The raw count „53 non-maps versus 6 B candidates" is not itself a scientific quality metric.
> Counts depend on editorial granularity, duplicated formulations, and the lexical definition
> of a non-map.

Czyli rama `LICZBA NON-MAPÓW >> LICZBA TWIERDZEŃ ⟹ ATLAS JEST ORYGINALNY` jest niebezpieczna,
a ja się na niej opierałem w 004 §6 i potem w całym rachunku kosztu ramy (013 §3, 014 §2, 015 §7).

Bezpieczna rama według REC9 wymaga, żeby **każdy** non-map miał pięć rzeczy:

1. typowane kategorie źródła i celu,
2. jawnego świadka albo twierdzenie,
3. **odjęcie dojrzałego gospodarza**,
4. zdanie o zakresie,
5. brak podwójnego liczenia tej samej przeszkody pod różnym słownictwem.

## 3. Test pięciu warunków zastosowany do mojej dwunastki — wynik niepochlebny

Zastosowałem go do siebie, zanim poprosiłem kogokolwiek o kolejny audyt.

| warunek | stan mojej dwunastki |
|---|---|
| 1. typowane kategorie | **częściowo**. Zrobione jawnie dla §2.8, §3.6, §7.2 (rozbite na trzy podtezy). Dla pozostałych typowanie odziedziczyłem ze sformułowania monografii, nie nadałem go sam. |
| 2. jawny świadek | **w zasadzie tak**: 9 świadków, 1 cytowanie, 1 odsyłacz, 1 przeredagowanie. |
| 3. odjęcie gospodarza **per non-map** | **NIE. Nie zrobione ani raz.** Odejmowanie gospodarzy wykonałem dla 68 numerowanych obiektów w 004 — czyli dla **twierdzeń**, nie dla **non-mapów**. Dla dwunastki zbudowałem świadków i nigdzie nie sprawdziłem, czy sam świadek nie jest elementarną dedukcją z dojrzałego gospodarza. |
| 4. zdanie o zakresie | **częściowo**. Jest dla §3.6 (`D` diagonalne, widmo punktowe proste) i §7.2 (ciągłość przestrzenna wobec orbit). Dla reszty systematycznie nie ma. |
| 5. brak podwójnego liczenia | **zawiodło raz, udokumentowane**: §7.2 policzony trzykrotnie w pierwszej wersji bilansu (014 §3). |

**Wniosek: liczba „koszt ramy atlasowej" nie jest obroniona ani jako liczba, ani jako rodzaj
miary.** Warunku 3 nie spełniłem systematycznie, a bez niego nie wiem, ile z moich dziewięciu
świadków to elementarne dedukcje z gospodarzy — czyli materiał redakcyjny, a nie treść.
Po gwarancji REC9 (`ELEMENTARY DEDUCTION FROM A MATURE HOST != NEW MATHEMATICAL RESULT`)
to rozróżnienie jest dokładnie tym, co powinienem był zrobić.

**Wycofuję rachunek kosztu ramy jako podstawę decyzji.** Nie „zero otwartych", nie „jedna
częściowo otwarta" — lecz: **licznik nie jest właściwą miarą**, a brakującą pracą jest odjęcie
gospodarza dla każdego z dwunastu non-mapów osobno. Tego nie wykonałem i nie oszacuję na oko,
ile by zmieniło.

## 4. Co REC9 potwierdził

- **Kierunek odejmowania: PASS.** Większość monografii to matematyka dojrzałych gospodarzy,
  standardowa analiza funkcjonalna albo elementarna dedukcja, i manuskrypt sam często
  etykietuje to uczciwie.
- **Diagnoza luki cytowań: aktualna przy świeżym odczycie.** Zero literalnych wystąpień dla
  wszystkich szesnastu nazwisk (Douglas, Fernando, Trinh, Jennings, Dahlquist, Söderlind,
  Lozinskii, Fuglede, Putnam, Rosenblum, Liljegren, Heinkenschloss, Antoulas, Stinespring,
  Oden, Prudhomme). Z zastrzeżeniem, które sam stawiałem i które REC9 powtarza: **brak
  cytowania nie jest nowością**.
- **Teza jakościowa: PASS.** Najmocniejszą wartością monografii nie jest duży zbiór nowych
  twierdzeń, lecz zdyscyplinowane typowanie non-mapów i jawne granice transferu.
- **Kontrpryzkład 7.4 jako falsyfikator mojego własnego błędnego oszacowania** — potwierdzony
  niezależnie, zgodnie z zapisem `NC-FAL-001`.

## 5. Jedno zastrzeżenie, które zgłaszam — nie do liczby, do zakresu domknięcia

REC9 zapisuje `ANTI_SELF_SEALING_OBLIGATION_FOR_NC004 = CLOSED_BY_REC9_FOR_THE_SIX-ITEM_FINAL_CLASSIFICATION`.
To domyka klasyfikację **sześciu obiektów**. Nie domyka:

- odejmowania gospodarzy dla **dwunastu non-mapów** (warunek 3 wyżej) — ta praca nie była
  przedmiotem audytu REC9 i pozostaje niewykonana;
- **całoatlasowego** porównania z tradycją przeglądową, którego REC9 sam wymaga przed
  jakimkolwiek claimem o oryginalności atlasu;
- wątku sufitu pomiarowego (008–011, 015) — poza zakresem.

Zgłaszam to, żeby `CLOSED` nie rozlało się szerzej, niż REC9 je nadał. Granica domknięcia
jest częścią domknięcia.

## 6. Zmiany w zapisach

| zapis | zmiana |
|---|---|
| nowy `NC-OPN-007` | klasyfikacja A/B z 004: strict B = 0, kandydat B = 1 (Tw. 4.4); nowość nieustalona |
| nowy `NC-OPN-008` | odjęcie gospodarza per non-map dla dwunastki — **niewykonane**, warunek 3 REC9 |
| `NC-OPN-005` (bilans) | **wycofany jako podstawa decyzji**: nie liczba jest sporna, lecz rodzaj miary |
| 004 §6, 013 §3, 014 §2, 015 §7 | baner erraty odsyłający tutaj |

## 7. Czego nie twierdzę

1. **Nie podważam żadnej degradacji REC9.** Każda ma wskazanego gospodarza; nie mam
   przeciwnej klasyfikacji ze źródłem i nie będę jej wymyślał, żeby obronić licznik.
2. **Nie twierdzę, że dziewięć świadków dwunastki jest bez wartości.** REC9 wprost oddziela
   wartość redakcyjną (`MANUSCRIPT_HARDENING_VALUE = HIGH`) od treści matematycznej. Twierdzę
   tylko, że nie wiem, ile z nich przeżyłoby odjęcie gospodarza, bo tego nie zrobiłem.
3. **Nie proszę o kolejny audyt tej seamu.** REC9 zapisał `STOP this subtraction seam`
   z trzema warunkami ponownego otwarcia; żaden nie jest spełniony.
4. **EXEC_SIGN brak**, status `[▷] EXPLORATORY`.

---

KONIEC. Audyt REC9 przyjęty. Decyzja o tym, czy wykonać odjęcie gospodarzy dla dwunastki,
należy do Moderatora — jest to praca literaturowa, której z tego środowiska nie wykonam.
