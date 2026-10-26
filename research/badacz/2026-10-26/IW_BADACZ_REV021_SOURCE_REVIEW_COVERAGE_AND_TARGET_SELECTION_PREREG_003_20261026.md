---
artifact_id: IW_BADACZ_REV021_SOURCE_REVIEW_COVERAGE_AND_TARGET_SELECTION_PREREG_003_20261026
exposure: PUBLIC
claim_ceiling: PREREGISTRATION_AND_DESCRIPTIVE_COVERAGE_MAP / NO_VERDICT_ON_ANY_SOURCE / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-26
origin_cell: BADACZ (wątek Claude)
document_type: PROTOCOL
task_id: BADACZ-FRONT-WEAKEST-POINT-001
supersedes_scope_of: IW_BADACZ_REVIEW_FAMILY_CONCENTRATION_PREREG_001_20261026 (instrument zatrzymany, zob. RETURN_002)
corpus_head: wmakiela-tech/Nash-iw-research d0d3cbf2837f2dca8be1ba3b2640d54c55cf57d1
---

# Pokrycie recenzją źródeł zintegrowanych w REV021 i reguła wyboru celu ataku

## 1. Zmiany wobec PREREG_001 (jawnie)

1. **Zbiór badany:** zamiast całego korpusu — 15 źródeł wymienionych przez LT5 jako
   zintegrowane w roboczym REV021. Źródło listy:
   `research/lt5/2026-10-24/lt5_rev021_native_living_theory_cross_cell_science_integration_source_ledger_001.md`
   §3 (ścieżki `research/…`, bez `nonmonograph`). To definicja nośności nadana przez
   właściciela, a nie moja miara centralności.
2. **Instrument:** wyszukiwanie ręcznie nadzorowane zamiast grafu leksykalnego. Dla każdego
   źródła szukam po rdzeniu nazwy pliku, po 12-znakowym skrócie bloba przy `corpus_head` i po
   wzorcu etykiety lub słowach z tytułu (wzorce w §4). Każde trafienie klasyfikuję po
   przeczytaniu kontekstu.
3. **Oś:** nie rodzina modelu jako taka, tylko **czy istnieje recenzja innej komórki** i jaką
   modalnością. Etykieta rodziny jest drugorzędna; uzasadnienie w RETURN_002 §4 pkt 3.
4. **Gospodarz w dorobku projektu:** LT5 sam oznaczył REV021 jako
   `NOT_YET_PUBLISHED_CANONICAL_HEAD / REQUIRES_CLAIM_LOCAL_REVIEW`, a przy części źródeł
   zapisał „Mathematical referee still pending" (publiczny rejestr z §1 pkt 1). Pełna mapa
   proweniencji claim po claimie należy do linii LT. Ta mapa nie jest jej zastępstwem. Jest
   wąskim przeglądem: „czy ktokolwiek spoza autora sprawdził źródło".

## 2. Klasy trafień

- `REVIEW_EXEC` — inna komórka przeliczyła lub odtworzyła nośny claim źródła (kod, dokładna
  algebra symboliczna) i podała werdykt.
- `REVIEW_TEXT` — inna komórka wydała werdykt o źródle bez własnego przeliczenia.
- `USE` — inna komórka buduje na źródle albo je cytuje jako podstawę, bez werdyktu.
- `MENTION` — wzmianka opisowa, w tym streszczenia integracyjne KN11, o ile nie deklarują
  niezależnego sprawdzenia konkretnego claimu.
- Pliki tej samej linii co źródło nie są recenzją.

## 3. Reguła wyboru celu ataku (zamrożona przed lekturą treści kandydatów)

Kandydaci: źródła bez żadnego `REVIEW_*` innej komórki w publicznym korpusie. Spośród nich
wykluczam źródła, których centralnym claimem nie jest dokładne twierdzenie matematyczne
(zbiory literatury). Wybieram:

1. źródło zintegrowane w **najwcześniejszym rozdziale** REV021 (fundament, na którym budują
   rozdziały dalsze);
2. przy remisie — źródło deklarujące ostrość albo optymalność (najłatwiej falsyfikowalne);
3. przy dalszym remisie — kolejność alfabetyczna ścieżki.

Atak to recenzja spoza rodziny GPT: sprawdzenie typów, założeń i dowodu, próba kontrprzykładu,
kod dla każdej liczby. **Nie jest to werdykt zamykający.** Właścicielem pozostaje autor źródła,
o integracji decyduje LT, a recenzję formalną prowadzą REC10/SW. Mój wynik ma status [▷]
i idzie do audytu zewnętrznego (Grok).

## 4. Wzorce wyszukiwania (wykonane przy `corpus_head`)

Dla każdego źródła: `git grep -F <rdzeń>`, `git grep -F <blob[:12]>` oraz `git grep -iP <wzorzec>`
z poniższej tabeli. Z wyników usuwam samo źródło i rejestr LT5.

| źródło | wzorzec |
|---|---|
| int8 ROT022 | `INT8[-_ (]*ROT[-_ ]*0*22(?![0-9])\|unital locality` |
| lt5 correlated preparation | `correlated[_ ]preparation\|skorelowan\w* przygotowan` |
| lt5 knapsack | `knapsack\|cost[_ -]constrained` |
| lt5 event-aligned adjoint | `event[_ -]aligned\|fixed[_ -]temperature` |
| lt5 same channel same POVM | `same[_ ]channel[_ ]same[_ ]povm\|same POVM` |
| m13 ROT30 | `M13[-_ (]*ROT[-_ ]*0*30(?![0-9])` |
| mech-s7 ROT013 | `Mech[-_ ]?S7[-_ (]*ROT[-_ ]*0*13(?![0-9])\|pre-?edge` |
| mt13 two-excitation | `two[_ -]excitation\|directional[_ ]rate[_ ]nonidentifiab` |
| mt13 metric-adapted stencil | `metric[_ -]adapted\|six[- ]shift` |
| nc ART017 | `NC[-_ ]*ART[-_ ]*0*17(?![0-9])\|NC[-_ ]0*17(?![0-9])\|KWANTYFIKATOR_017` |
| prf11 R19 | `PRF11[-_ (]*R[-_ ]*0*19(?![0-9])` |
| prf11 R20 | `PRF11[-_ (]*R[-_ ]*0*20(?![0-9])` |
| prf11 R27 | `PRF11[-_ (]*R[-_ ]*0*27(?![0-9])\|C2[_ ]minimal[_ ]face` |
| rec10 ROT07 | `REC10[-_ (]*ROT[-_ ]*0*7(?![0-9])\|causal[_ ]timing` |
| xh-s4 026 | `XH[-_ ]?S4[-_ (]*0*26(?![0-9])\|memory realization` |

## 5. Granice

Publiczny korpus. Recenzje prywatne (Drive, Nash-Priv poza pakietem LT, BW, Slack) mogą
istnieć, a ich brak tutaj nie jest brakiem w projekcie. Klasyfikacja jest moją lekturą, nie
werdyktem autora ani recenzenta.
