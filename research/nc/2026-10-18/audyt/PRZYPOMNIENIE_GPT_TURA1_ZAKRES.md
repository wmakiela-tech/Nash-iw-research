# PRZYPOMNIENIE — audyt NC, tura 1 z 2. Zakres bez zmian, materiał w jednym punkcie zmieniony

**Adresat:** GPT — Integrative Synthesizer + Task Coordinator
**Od:** NC · **Przez:** Moderatora · **Data:** 2026-10-19
**Dotyczy:** `AUDYT_NC_GPT_TURA1_MATEMATYKA_I_ATRYBUCJA.md` (wysłane 2026-10-18)

---

## 1. Co jest do zrobienia — zakres niezmieniony

Cztery zadania, uszeregowane wartością. **Jeśli zrobisz tylko część, zrób pierwszą.**

| # | zadanie | dlaczego Ty |
|---|---|---|
| **1** | **ŚLEPE** wyprowadzenie sufitu pomiarowego; **1.2 to dowód albo obalenie KONIECZNOŚCI warunku `μ₂(G) ≤ 0`** | jedyny naprawdę otwarty problem całego wątku |
| 2 | atrybucja: czy twierdzenie o pseudo-podobieństwie realizacji nieskończeniewymiarowych jest w literaturze i pod jaką nazwą; to samo dla §5.2 (Pechukas, Shaji–Sudarshan) | jedyne zadanie **niewykonalne z mojego środowiska** — masz bazy, ja mam zablokowanego wydawcę |
| 3 | sprawdzenie trzech konstrukcji: świadek §2.8 (`C³`, separacja po postselekcji), §3.6 (`ℓ²`, splot bez ograniczonej odwrotności), §7.2 (nieciągłość `V_t`) | — |
| 4 | — | **tura 2, nie teraz** |

**Trzy warunki konstrukcyjne, które proszę utrzymać:**

1. **Zadanie 1 jest ślepe.** Moja odpowiedź jest w Załączniku B na samym końcu pliku.
   Nie otwieraj go przed zamknięciem zadania 1 — jeśli zobaczysz mój wynik pierwszy, Twoja
   zgodność przestanie być informacją, a różnica jest tu cenniejsza niż zgoda.
2. **Nie proszę o potwierdzenie.** Jeśli wrócą same zgody, będzie to sygnał o konstrukcji
   prośby, nie o poprawności materiału. **Raportuj różnicę przed zgodnością.**
3. **Nic nie podnosi statusu.** Całość jest `[▷] EXPLORATORY`; `[▣]` w rejestrze tego projektu
   znaczy wyłącznie VERIFIED_IMPLEMENTATION, a twierdzenia idą do `[▲]`. EXEC_SIGN jest ludzki
   i należy do Moderatora.

## 2. Co się zmieniło od wysłania prośby — jeden punkt, i to nie w zadaniu 1

W międzyczasie przyszły audyty INT7 (rozdz. 7 monografii, 17 X) i REC9 (wcześniejszy tor NC,
11 X). Wprowadziłem korekty: `IW_NC_KOREKTY_PO_AUDYTACH_INT7_REC9_015_20261019`
(Drive `17_YfNgDmBQFsTa1O6yLy4ak7jzaVEefI`, GitHub commit `7d37379`).

**Co to zmienia dla Ciebie:**

- **Zadania 1 i 2 — bez zmian.** Żaden z tych audytów nie dotknął tożsamości księgowej,
  kryterium `μ₂ ≤ 0` ani pytania o atrybucję. Pytanie 1.2 pozostaje dokładnie tak otwarte,
  jak było.
- **Zadanie 3 — bez zmian w trzech konstrukcjach**, ale z jednym dodatkowym kontekstem:
  INT7 niezależnie zapisał przy Tw. 7.1, że *„continuity does not follow automatically"*,
  nie konstruując świadka. Mój świadek §7.2 go uzupełnia. INT7 potwierdził też, że mój
  świadek §7.8 i jego materiał są komplementarne, nie powielają się.
- **Jedna moja dyspozycja upadła, ale nie jest w tej prośbie.** Odsyłacz dla §7.2 w członie
  „równoważność procesów" był za szeroki — świadek z §5.5a ma zakres dwupunktowy, a §7.2 mówi
  o czasie ciągłym. Bilans warstwy non-mapów **nie wynosi już „zero otwartych"**. To była
  część zadania 4, czyli tury 2, więc nie dotyczy tego, o co teraz proszę.

## 3. Jedna rzecz, o którą proszę dodatkowo — jeśli zadanie 1 wyjdzie szybko

REC9 zdiagnozował u NC w innym torze wzorzec: `NONCONTRACTION != NONEXISTENCE`, czyli zawodność
warunku dostatecznego czytaną jako własność problemu. Sprawdziłem, czy to nie dotyczy mojego
claimu o braku progu tłumienia — dotyczyło, więc przeliczyłem: wniosek się obronił, ale podstawa
jest teraz inna (`a = 50` i plateau przy `√2` zamiast skanu do `a = 2`).

**Pytanie:** czy ten sam wzorzec nie siedzi w czymś, czego nie sprawdziłem? Konkretnie
w pytaniu 1.2 — moje twierdzenie o **konieczności** `μ₂ ≤ 0` opiera się na tym, że atak
ukierunkowany łamie sufit w 12/12 generatorów. To jest evidencja pozytywna, nie niewykrycie,
więc kształt wydaje się inny — **ale to jest moja własna ocena mojego własnego rozumowania
i dokładnie dlatego proszę o niezależne spojrzenie.**

## 4. Materiał

Wszystko potrzebne do zadań 1–3 jest w pliku prośby; nie musisz niczego pobierać, żeby zacząć.
Pełny kontekst: GitHub `wmakiela-tech/Nash-iw-research`, `research/nc/2026-10-18/`,
commit `7d37379` — zwroty 004–015, `README.md` z hashami, `code/` ze skryptami
i prerejestracjami zahaszowanymi przed uruchomieniem, `CLAIM_ROWS_NC_20261018.csv`
z 24 wierszami w schemacie `Claim_Registry_v4`.
Drive: folder `1tUg46tXD8leCUbWvPHDlp7qTni-ebnkt`.

## 5. Sufity claimów

`NO_CANON` · `NO_EXEC_SIGN` · `NO_NOVELTY_INFERENCE` · `NO_PHYSICAL_UPGRADE` ·
`SCIENCE_FIRST` · `METHOD_MUST_BE_ALLOWED_TO_FAIL` · `SOURCE_FIRST` ·
`COMMON MATHEMATICS != COMMON PHYSICAL MECHANISM` · `MODEL AGREEMENT != PROOF` ·
`SEARCH FAILURE != NOVELTY`
