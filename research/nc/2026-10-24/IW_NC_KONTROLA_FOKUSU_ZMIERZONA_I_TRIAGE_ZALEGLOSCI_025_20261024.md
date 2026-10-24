# IW_NC_KONTROLA_FOKUSU_ZMIERZONA_I_TRIAGE_ZALEGLOSCI_025_20261024

<!-- IW_CONFORMANCE_BLOCK v1 (docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md §2.7) -->
```text
artifact_id          : IW_NC_KONTROLA_FOKUSU_ZMIERZONA_I_TRIAGE_ZALEGLOSCI_025_20261024
exposure             : PUBLIC_SAFE
canonical_body_path  : research/nc/2026-10-24/IW_NC_KONTROLA_FOKUSU_ZMIERZONA_I_TRIAGE_ZALEGLOSCI_025_20261024.md
source_revision      : rozwiazywane przez `git log -- <canonical_body_path>`
bw_event_or_pending  : GITHUB_PENDING_BW_INGEST
claim_ceiling        : NO_CANON / NO_EXEC_SIGN / GOVERNANCE_ONLY_NO_SCIENCE_CLAIM / SELF_ADMINISTERED_CONTROL_IS_NOT_INDEPENDENT_AUDIT
hold                 : BRAK
```

KOMÓRKA: NC — zewnętrzna komórka Claude, rola **SP**
ZLECENIE: Moderator, 2026-10-24 — „zrób kontrolę" w odpowiedzi na `NC-OPN-025`
KLASA: **wyłącznie governance. Żadnego claimu naukowego.**
KOD: liczone z `research/nc/2026-10-18/CLAIM_ROWS_NC_20261018.csv` i z gita

---

## 1. Zmierzone, nie opowiedziane

### Bilans zobowiązań — netto otwartych narastająco

| data | `[OPEN]` | `[▷]` | `[🔴]` | razem | netto OPEN narastająco |
|---|---|---|---|---|---|
| 2026-10-18 | 3 | 13 | 12 | 28 | 3 |
| 2026-10-19 | 3 | 0 | 0 | 3 | 6 |
| 2026-10-22 | 1 | 0 | 2 | 3 | 7 |
| 2026-10-23 | 5 | 4 | 3 | 12 | 12 |
| **2026-10-24** | **10** | 10 | 4 | 24 | **22** |

Otwartych ogółem **22**; z odnotowanym postępem **7**; **bez żadnego postępu 15**;
zalegających ≥2 dni pracy **7**.

### Kto wykrywa moje błędy

| | liczba |
|---|---|
| falsyfikacje wykryte moimi kontrolami | 11 |
| falsyfikacje wykryte zewnętrznie | 10 |
| udział własnych | **52,4%** |

Rosnący udział własnych jest dobry, ale **nie zastępuje audytu** — ANTI-SELF-SEALING.

### Rozkład pracy

| kategoria | wiersze | udział |
|---|---|---|
| własna nauka NC | 56 | **80%** |
| custody / rejestr | 8 | 11% |
| wsparcie innej komórki | 6 | **9%** |

## 2. Wynik kontroli: zdiagnozowałem złą os

W ART024 §0 nałożyłem sygnał „gravity well" na **serię zwrotów wsparcia dla XH-S4**.
Pomiar mówi, że ta seria to **9% rejestru**. Nałożyłem sygnał na os, na której właśnie
pracowałem, zamiast ją zmierzyć.

Zmierzone wypieranie jest gdzie indziej i jest wyraźne: **netto otwartych zobowiązań rośnie
monotonicznie `3 → 6 → 7 → 12 → 22`**, a 24 października otworzyłem **dziesięć** nowych
wierszy `OPEN` w jednym dniu. Piętnaście wierszy nie ma żadnego odnotowanego postępu.

Czyli gravity well nie polegał na powtarzaniu ruchu, lecz na **produkowaniu nowego przy
zaleganiu ze starym** — i to jest definicja, którą sam zapisałem w preregu, a potem
zastosowałem do złej zmiennej.

`origin_failure_mode: DIAGNOSED_A_GRAVITY_WELL_ON_THE_AXIS_I_HAD_JUST_WORKED_ON_INSTEAD_OF_MEASURING`

## 3. Triage siedmiu zaległych wierszy — z dyspozycją, nie z opisem

| wiersz | dyspozycja | podstawa |
|---|---|---|
| `NC-OPN-002` | **zostaje przy NC** | realne otwarte pytanie matematyczne; ciasna stała przy `μ₂ > 0` nierozstrzygnięta |
| `NC-OPN-005` | **wniosek o wycofanie** | rachunek kosztu ramy wycofany jako podstawa decyzji już w ART016 §3 — wiersz nie ma przedmiotu. **NC nie wycofuje sam**: zmianę statusu nadaje Moderator |
| `NC-OPN-006` | **do LT4** | pytanie redakcyjne o odsyłacz w §7.2; właściciel i autorstwo przy LT4 |
| `NC-OPN-007` | **do PRF11** | całoatlasowe porównanie z tradycją przeglądową = praca literaturowa |
| `NC-OPN-008` | **do PRF11** | odjęcie gospodarza dla dwunastu non-mapów = dosłownie ich zadeklarowana funkcja |
| `NC-OPN-009` | **rozdzielone** | część NC (nagłówki) wykonana 2026-10-23; część BW należy do KN11 i jest już `NC-OPN-021` |
| `NC-OPN-014` | **do LT4** | INT7 §10 podaje dwie legalne drogi i stwierdza, że Söderlind 2006 to pokrywa — materiał gospodarza, praca redakcyjna |

Routing odczytany **u źródła, nie z pamięci**: PRF11 deklaruje w nagłówkach własnych zwrotów
`origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10` oraz
`function: FOUNDATION_FIRST / OTHERS_FIRST / FALSIFICATION_FIRST / SOURCE_TYPED_MATURE_HOST_SUBTRACTION`.
Ostatni człon jest literalnie treścią `NC-OPN-008`.

**Najdotkliwsze ustalenie triage'u.** Powtarzałem przez sześć dni, że odjęcia gospodarza
dla dwunastki „z tego środowiska nie wykonam" — i **ani razu nie przekazałem tego komórce,
której zadeklarowaną funkcją to jest**. To nie był brak wiedzy, lecz brak routingu.

`origin_failure_mode: REPEATEDLY_DECLARED_A_TASK_UNEXECUTABLE_WITHOUT_ROUTING_IT_TO_THE_CELL_WHOSE_DECLARED_FUNCTION_IT_IS`

## 4. Reguła, egzekwowalna z zewnątrz

`NC-OPN-026`:

1. **Przed otwarciem nowego zakresu badawczego** każdy wiersz `OPEN` starszy niż dwa dni
   pracy musi być albo posunięty, albo przekazany komórce o zadeklarowanej funkcji, albo
   zgłoszony do wycofania z uzasadnieniem.
2. **Netto otwartych nie rośnie dwa dni pracy z rzędu** bez podanej przyczyny.

Reguła liczy się z publicznego `CLAIM_ROWS_NC`, więc **jest egzekwowalna z zewnątrz** —
zgodnie z zasadą projektu, że każda reguła claim-relevant musi mieć odpowiednik obserwowalny
w zachowaniu, a nie samą deklarację postawy. Każdy uczestnik może ją na mnie wymusić bez
mojej zgody.

## 5. Czego ta kontrola nie jest

1. **Nie jest audytem niezależnym.** Zaprojektowałem ją i wykonałem na sobie. **Pomiary** są
   sprawdzalne z zewnątrz, bo liczą się z publicznego CSV i z gita; **interpretacja nie jest
   niezależna** i podlega audytowi jak każdy mój wynik.
2. **Nie zmienia statusu żadnego wiersza na `CLOSED`** ani nie wycofuje `NC-OPN-005` — to
   decyzje Moderatora.
3. **Nie zawiera claimu naukowego.** Żadna liczba tutaj nie dotyczy matematyki ani fizyki.
4. **Nie przesądza, czy 80% udziału własnej nauki jest złe.** Pomiar mówi tylko, że sygnał
   nałożyłem na niewłaściwą os; czy koncentracja na własnej linii wymaga korekty, jest
   decyzją Moderatora, nie wnioskiem z tej tabeli.

---

KONIEC. Kontrola wykonana na zlecenie. Do Moderatora dwie decyzje: wycofanie `NC-OPN-005`
oraz czy przyjąć regułę `NC-OPN-026` jako obowiązującą dla NC. Do PRF11 i LT4 — cztery
przekazane wiersze; to zgłoszenia, nie zadania.
