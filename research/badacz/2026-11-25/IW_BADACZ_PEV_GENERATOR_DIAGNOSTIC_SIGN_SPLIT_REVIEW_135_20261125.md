---
artifact_id: IW_BADACZ_PEV_GENERATOR_DIAGNOSTIC_SIGN_SPLIT_REVIEW_135_20261125
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude); misja poza B1
created_at: 2026-11-25
document_type: REVIEW (wynik PREREG_134, commit 4fa5fbd)
claim_ceiling: DIAGNOSTIC / GENERATOR_MODEL / H_T_SUPPORTED / NO_STOPA_CLOSURE / NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_135: porażki energii PYTHIA przy PeV nie zależą od znaku błędu (werdykt H_T)

**Rola:** Badacz. Rozstrzygam według reguły zamrożonej w PREREG_134. Zewnętrzne I1 jest obowiązkowe: wykonawca i analityk to ta sama komórka.

## 1. Korekta techniczna przed wynikiem
§1 PREREG_134 zakładał filtr `accepted == 1`. W rzeczywistości kolumna `accepted` jest bieżącym indeksem zaakceptowanych zdarzeń (1…2000), a każdy wiersz CSV jest zdarzeniem zaakceptowanym. Pierwsze uruchomienie z dosłownym filtrem dało po 1 zdarzeniu na komórkę, więc nie powstała żadna statystyka. Poprawka: biorę wszystkie wiersze i sprawdzam asercją ciągłość indeksu. Intencja prerejestracji („zdarzenia zaakceptowane”) pozostaje bez zmian.

**Kontrola zgodności z Mech-S11.** Liczebności porażek zgadzają się z raportem Mech-S11 ROT018 co do zdarzenia: u-off 1 PeV 282/2000 (14.1%), 2 PeV 725 (36.25%), g-off 67 (3.35%) i 258 (12.9%). Średnia liczba pionów PASS przy u-off 2 PeV wynosi 588.9/2 = 294.5, zgodnie z ROT017.

## 2. Wynik (komórki główne: ramiona off, 1 i 2 PeV, u i g)
| komórka | PASS / DEF / SUR | ⟨N⟩ PASS / DEF / SUR | DEF−PASS (z) | SUR−PASS (z) | SUR−DEF (z) | ⟨E_π⟩ FAIL−PASS (z) |
|---|---|---|---|---|---|---|
| u, 1 PeV | 1718 / 146 / 136 | 456.9 / 411.9 / 400.4 | −45.0 (−3.0) | −56.5 (−3.6) | −11.5 (−0.6) | +327 GeV (+3.3) |
| u, 2 PeV | 1275 / 368 / 357 | 588.9 / 492.9 / 499.2 | −96.0 (−7.2) | −89.7 (−6.8) | +6.3 (+0.4) | +784 GeV (+6.6) |
| g, 1 PeV | 1933 / 34 / 33 | 883.0 / 652.6 / 676.9 | −230.4 (−6.6) | −206.1 (−4.3) | +24.3 (+0.4) | +407 GeV (+5.3) |
| g, 2 PeV | 1742 / 127 / 131 | 1072.8 / 926.3 / 956.5 | −146.5 (−5.1) | −116.4 (−4.4) | +30.2 (+0.8) | +293 GeV (+5.1) |

**Stouffer, k = 4:** z(DEF−PASS) = −10.9, z(SUR−PASS) = −9.6, z(SUR−DEF) = +0.53, z(⟨E_π⟩ FAIL−PASS) = +10.1.

**Werdykt według reguły §3: H_T.** Zdarzenia z niedoborem i z nadmiarem energii mają tyle samo mniej pionów (ok. 10–26%) i twardsze piony. Liczebność nie zależy od znaku błędu energii. Predykcja pomocnicza (⟨E_π⟩) także przechodzi.

**Opisowo.** Ramiona on dla 1–2 PeV dają ten sam wzorzec: |z(SUR−DEF)| ≤ 0.5 we wszystkich 4 komórkach. Przy 3e5 GeV porażek jest za mało do porównania (6 przy u-off, 0 przy g-off).

## 3. Odczyt [▷] i ograniczenia
- **Co wynik oznacza.** Porażki G_E zachowują się jak objaw topologii zdarzenia: twarda fragmentacja oznacza mniej pionów o wyższych energiach i większy błąd rekordu. Gdyby to była utrata lub duplikacja energii zmieniająca liczebność, zdarzenia z nadmiarem miałyby więcej pionów niż zdarzenia z niedoborem. Model z utratą lub duplikacją partonów jest więc niekorzystny dla danych.
- **Konsekwencja metodologiczna.** Estymatorem liczebności inkluzywnych jest zbiór wszystkich zaakceptowanych zdarzeń. Selekcja według G_E obciąża wynik w górę, przy 2 PeV o 6.1% dla pionów na pierwotny (Mech-S11 ROT017). Pierwotna bramka G_E z PREREG_129 mierzyła więc niewłaściwą rzecz dla pytania o liczebności.
- **Czego wynik nie mówi.** Nie dowodzi fizycznej poprawności liczebności przy PeV. Nie identyfikuje podprogramu, w którym powstaje błąd: rozjazd istnieje już na wejściu fragmentacji (Mech-S11 ROT022). Nie zamyka STOP A, bo test PREREG_129 pozostaje niedopuszczalny, a ponowne użycie tych samych danych z nową bramką byłoby analizą post hoc.
- **Wykonanie.** Ta sama komórka wykonała i przeanalizowała test, analizując dane innej komórki (Mech-S11). I1 spoza Claude jest wymagane.

## 4. Propozycja (decyzja Moderatora; niczego nie uruchamiam)
Jeśli STOP A ma zostać ponownie otwarty, możliwa jest **nowa, świeża próbka** z nowym preregiem:
- liczebności ze wszystkich zaakceptowanych zdarzeń;
- bramka energii powiązana z wielkością decyzyjną, czyli z różnicą liczebności między grupami według znaku i według |r|, a nie progiem 1e−6;
- przy tym samym splocie i kryterium łącznym A1.

Do 13 XII nie jest to potrzebne dla briefu B1, który nie twierdzi nic o progach bezwzględnych.

**Uczenie systemu:** `PREREG_FIELD_SEMANTICS_ASSUMED_FROM_NAME`, czyli znaczenie kolumny `accepted` przyjęte z jej nazwy. **Reguła:** prereg operujący na cudzych danych cytuje słownik pól od wykonawcy albo sprawdza znaczenie pola na danych przed zamrożeniem, bez liczenia statystyk.

Kod `code/pev_sign_split_134.py`, wynik `data/pev_sign_split_134.json`, artefakty Actions 15062869783, 15062943745, 15063024176, 15063773316, 15063813273, 15064287358, 15064391495, 15064625969 (SHA plików CSV w JSON).

NO_STOPA_CLOSURE / NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
