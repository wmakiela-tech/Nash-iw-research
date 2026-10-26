---
artifact_id: IW_BADACZ_REVIEW_FAMILY_CONCENTRATION_INSTRUMENT_FAILURE_RETURN_002_20261026
exposure: PUBLIC
claim_ceiling: NEGATIVE_KNOWLEDGE_ABOUT_A_MEASUREMENT_INSTRUMENT / NO_RANKING_PUBLISHED / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-26
origin_cell: BADACZ (wątek Claude)
document_type: RETURN
result_class: NEGATIVE_KNOWLEDGE
task_id: BADACZ-FRONT-WEAKEST-POINT-001
derived_from: IW_BADACZ_REVIEW_FAMILY_CONCENTRATION_PREREG_001_20261026 (commit 829aee3298c972baa6f87cff202260364ba2308f)
code: research/badacz/2026-10-26/code/review_family_concentration.py (sha256 aece498f70c9ba6a064c1ced959c02ebb6cb9ebb0137040571883a413cb94a8d)
corpus_pin: 921360060946b0ed7bdfad2ef5e6b52e2b7e6dd1
---

# Instrument C_REVIEW z odwołań leksykalnych nie przechodzi walidacji — STOP wykonany

## 1. Wynik

Preregestracja (§5) przewidywała STOP przy recall < 0,70. **Recall wyszedł 0,69 dla
wszystkich odwołań i 0,43 dla odwołań do innej linii** — a te drugie są tymi, od których zależy
miara kontaktu międzyrodzinowego. Zgodnie z preregestracją **nie publikuję rankingu słabych
korzeni ani rozstrzygnięcia H1.**

Kod uruchomiony na przypiętym korpusie daje liczby, ale są **nieinterpretowalne**. Instrument
gubi ponad połowę odwołań międzyliniowych, a każda zgubiona krawędź przesuwa wynik w stronę
„brak kontaktu", czyli w stronę H1. Liczby da się odtworzyć poleceniem z §5. Nie przytaczam
ich, żeby nie wędrowały jako wynik.

## 2. Walidacja — dokładnie

Próbka: 12 plików `research/nc/`, `random.Random(20261026).sample` na posortowanej liście
ścieżek (lista w `recall_sample.json` wygenerowanym przez kod). Wzmianki wyłowione liberalnym
wyrażeniem rozstrzygnąłem ręcznie. Liczą się tylko wzmianki wskazujące węzeł istniejący w
korpusie.

| plik próbki | rozstrzygnięty cel w korpusie | wykryty? |
|---|---|---|
| `nc/2026-10-24/code/PREREG_SAT.md` | `rec10/…/IW_REC10_ROT21_NC_VARIABLE_COEFFICIENT_MASS_BALANCE_REFEREE_20261023.md` („REC10 ROT21") | tak |
| `nc/2026-10-24/IW_NC_OPN002_…_029_20261024.md` | `m13/…/IW_M13_ROT11_NC_GPT_tura1_…` („funkcjonal M13 (ROT11)") | **nie** — nawias między komórką a numerem |
| tamże | `nc/…/IW_NC_KOREKTA_ART029_…_031_…` (nazwa pliku) | tak |
| `nc/2026-10-18/IW_NC_LT4_PRIOR_ART_SUBTRACTION_FULL_MANUSCRIPT_004_…` | `mt13/20261013_book_first_chapters_editorial_scientific_review.md` („zwrot MT13 z 13 X") | **nie** — odwołanie przez datę |
| tamże | `nc/…/IW_NC_ODBIOR_REC9_NC004_…_016_…` (nazwa pliku) | tak |
| `nc/2026-10-18/code/PREREG_MT13_EVENT.md` | `mt13/2026-10-23/mt13_nc_lt5_event_weighted_source_sufficiency_gate_001.md` (przez nazwę towarzyszącego `…_check_001.py`) | **nie** — odwołanie do pliku kodu, nie do `.md` |
| tamże | `nc/…/PREREG_MT13_NONLIN.md` | tak |
| `nc/2026-10-18/IW_NC_APPROXIMATE_MINIMALITY_WITNESS_…_013_…` | M13 ROT11 („audytach M13 ROT11") | tak |
| tamże | `geeky-s10/2026-10-19/geeky_s10_nc_gpt_tura1_math_attribution_audit_001.md` („audytach … GEEKY-S10") | **nie** — bez numeru |
| tamże | trzy pliki NC przez nazwę | tak, 3/3 |
| `nc/2026-10-24/code/PREREG_KREISS.md` | M13 ROT11 („M13 (audyt ROT11", „M13 ROT11") | tak |

Pozostałe sześć plików próbki nie odwołuje się do żadnego węzła korpusu. Wzmianki INT7 (audyt
NC z 19 X, separator `[[−1,100],[0,−1]]`) i REC9 (audyt NC004) wskazują dokumenty, których nie
ma w publicznym korpusie, więc nie wchodzą do mianownika.

- Recall ogółem: **9/13 = 0,692**.
- Recall międzyliniowy: **3/7 = 0,43**.

To szacunki **górne**: liczę tylko wzmianki, które wyłapało liberalne wyrażenie (komórka +
liczba). Odwołania czysto opisowe („separator INT7") nie wchodzą nawet do mianownika.

## 3. Klasa błędu — mechanizm, nie objaw

Trzy zgubione formy — nawias, data zamiast numeru, plik kodu zamiast dokumentu — mają jedną
przyczynę. **Komórki odwołują się do siebie przez rolę i treść** („audyt M13", „zwrot MT13 z 13
X", „separator INT7"), a nie przez trwały identyfikator. Łatanie wyrażeń regularnych pod każdą
z tych form byłoby skrojeniem reguły pod ostatnie przeoczenie (START, bramka f). Graf odwołań
publicznego korpusu **nie jest czytelny maszynowo z samego tekstu.** Zakres: publiczny korpus.
BW prowadzi własne, ręcznie typowane relacje (GENEALOGY, MECHANISM_GRAPH) — tego nie
sprawdzałem i nie twierdzę, że brakuje ich w projekcie.

Typ claimu: definicyjno-pomiarowy o instrumencie. Nie mówi nic o jakości nauki w korpusie.

## 4. Własne błędy wykryte po zamrożeniu — wpisane, nie wygładzone

1. **Odjęcie na powierzchni własnej było niepełne.** Preregestracja §2 przeoczyła najbliższego
   gospodarza w dorobku projektu: badanie LT5 nad korektą claimów
   (`research/lt5/nonmonograph/2026-10-23/lt5_nash_claim_correction_study_protocol_and_five_case_pilot_001.md`
   oraz `lt5_nash_claim_correction_research_direction_accepted_stage1_001.md`). Jest to
   przyjęty kierunek badań. Ma ramiona: autorecenzja / recenzja tekstowa innego modelu /
   niezależna weryfikacja wykonywalna, oraz rozdzielenie S/E/R/I. Moje zapytanie leksykalne
   szukało słów „family", „C_REVIEW", „cross-family", a nie „other model referee" — i dlatego
   go nie znalazło. To dokładnie wzorzec bramki (a) startu Badacza. Wniosek dla dalszej pracy:
   pytanie o różnorodność recenzji należy do programu LT5, a nie do równoległego instrumentu.
2. **Kontrola symetrii jest rozwinięciem definicji, nie wynikiem.** W mapie rodzin jest tylko
   jedna linia nie-GPT (`nc`). Każde odwołanie innej linii do NC jest więc z definicji
   międzyrodzinowe, a „kontakt międzyrodzinowy wyniku GPT" znaczy dokładnie „NC się do niego
   odwołał". Tak wyliczona miara mierzy pokrycie korpusu GPT przez jedną komórkę Claude, nie
   ogólną różnorodność (bramka h).
3. **Literatura podważa samą oś pomiaru.** Według Kim i in. (ICML 2025) duże modele różnych
   dostawców mają silnie skorelowane błędy. Nawet poprawny instrument mierzyłby tylko słabą
   różnorodność. Zgadza się to z hipotezą H1 badania LT5: o jakości decyduje modalność
   weryfikacji (wykonanie, źródło), nie etykieta rodziny.

## 5. Odtworzenie

Z korzenia repozytorium, w dowolnym stanie roboczym (kod czyta korpus z gita):

```text
python3 research/badacz/2026-10-26/code/review_family_concentration.py \
  --pin 921360060946b0ed7bdfad2ef5e6b52e2b7e6dd1 --out <katalog>
```

Środowisko autora: Python 3.13.17, git 2.43.0, tylko biblioteka standardowa. Oczekiwane
wartości kontrolne: 519 węzłów, 1105 krawędzi (82 z niejednoznaczną etykietą krótką), 308 węzłów
z etykietą krótką, rodziny CLAUDE 57 / GPT 140 / GPT_ASSUMED 322. Status reprodukcji:
`AUTHOR_REPRODUCED` (jeden przebieg autora), niezależnie nieodtworzone.

## 6. Co dalej

Zamiast łatać instrument zawężam pytanie do zbioru, który jest jawnie nośny i daje się
sprawdzić ręcznie: 15 wyników zintegrowanych przez LT5 w roboczym REV021 Żywej Teorii (lista ze
źródłowego rejestru LT5 z 24 X). Dla każdego ustalam, kto i jaką modalnością go sprawdził. Ma to
osobną preregestrację (`…_PREREG_003_…`).

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM`. Audyt zewnętrzny: Grok.
