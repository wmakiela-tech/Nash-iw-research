---
artifact_id: IW_BADACZ_B1_E4_TABLE_DOMAIN_REVIEW_089_20261121
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel natywny B1, właściciel T2
created_at: 2026-11-21
document_type: REVIEW (wynik zamrożonej PREREG_088)
follows: PREREG_088 (Nash-iw-research@3d0227f), SYNTH_087 §3
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_089: E4 dla j22: trend bez ucięcia zaostrza próg o 0.05–0.08 dex; ucięte wiersze BlackHawk osłabiłyby go o 0.37–0.59 dex

## 1. Przebieg i bramki

- `run088.sh` (`/home/claude/run088`, 22:13–22:40):
  - Julia: 47 + 47, rc = 0;
  - deduplikacja bez zmian (0/94);
  - sieć: 97/97;
  - zakończenie ALL_DONE, exit 0.
- Analiza zamrożona; powtórzona daje bitowo ten sam JSON (SHA 4c7d1410…).
- **Bramki 8/8 PASS:**
  - V7 komplet;
  - V2_EXACT 1.8e-13;
  - V6;
  - V_TABLE: wiersze 5–99 dosłownie;
  - V_BASE: 1.0e-5 (A) i 9.6e-5 (C) przy progu 5e-4;
  - V3 ≤ 6.6e-6, baza sieci = 083;
  - V4: 0.07%;
  - V5: 0.32%.

## 2. Wynik [▷]

| model | cel | E4_C = lb_C − lb_PY | E4_A = lb_A − lb_PY |
|---|---|---|---|
| kod | 0.251 | −0.061 | +0.586 |
| kod | 0.2484 | −0.054 | +0.464 |
| sieć | 0.251 | −0.053 | +0.420 |
| sieć | 0.2484 | −0.078 | +0.374 |

- **LC = `E4_INTERMEDIATE`:** max |E4_C| = 0.078, między 0.05 a 0.10. Znak jest ujemny we wszystkich 4 komórkach.
- **Odpowiedź przy ustalonym β** (kod, węzły −17.5…−17.1):
  - ΔY_C/ΔY_PY = 1.05–1.13;
  - ΔY_A/ΔY_PY = 0.48–0.56.
- **Szum (opisowo, post-hoc):**
  - N_Y = 9.6e-5 (V_BASE wariantu C, ten sam rząd co rozrzut baz 083 między masami);
  - daje to 0.013–0.034 dex na pierwiastek, najwięcej dla sieci przy LBT, gdzie nachylenie dY/dlb = 0.003.
  - E4_C przy 0.251 jest więc rozdzielone na poziomie ~2.5–4 × szumu (na pierwiastek lub na różnicę dwóch pierwiastków). Przy LBT w sieci tylko ~2×.
  - Spójny znak w 4/4 komórkach i stosunek ΔY > 1 we wszystkich węzłach wspierają realny efekt rzędu −0.06 dex.
  - Etykieta zamrożona nie miała warunku rozdzielczości. Zaznaczam to jako jej ograniczenie.
- **Predykcje:**
  - P1 FAIL: E4_C kodu wynosi −0.061 i −0.054, a nie mieści się w [−0.05, 0). Moje oszacowanie z SYNTH_087 (≈ −0.03) było za małe o czynnik ~2.
  - P2 PASS: +0.586 ≥ 0.10.
  - P3 FAIL: różnica kod − sieć przy LBT wynosi 0.024 przy progu 0.02, czyli w granicy szumu.

## 3. Interpretacja [▷]

- **Dlaczego efekt jest 2× większy od oszacowania** (hipoteza post-hoc): oszacowanie ważyło wydajności liczbą emitowanych hadronów. Emisja przy małych masach przypada jednak na późny etap życia PBH, czyli później w czasie kosmicznym i bliżej zamrożenia n/p, gdzie każdy hadron ma większą dźwignię. Wzrost wydajności o 2–3% (ważony liczbą) daje wzrost ΔY o ~7%.
- **Ekstrapolacja autorów vs trend bez ucięcia.** Ekstrapolacja autorów jest nieco zaniżona, bo jej nachylenie pochodzi z wierszy 0–1, które sufit już spłaszczył. Próg j22 autorów jest przez to łagodniejszy o ~0.05–0.08 dex, niż dałby trend bez ucięcia. To mało wobec osi z SYNTH_087 (generator 0.35, sieć do 0.6, T2 0.28), ale więcej niż tolerancja (0.023) i niż mój szacunek.
- **Ostrzeżenie metodyczne.** Bezpośrednie wiersze BlackHawk v2.3 poniżej ~6e8 g, z sufitem E_prim 1e5 GeV, osłabiłyby próg j22 o 0.37–0.59 dex. Każda ponowna analiza, która generuje tablice hadronów do 1e8 g bezpośrednio z BlackHawk, zamiast je ekstrapolować, wprowadzi błąd tego rzędu. Wu–Xu zauważyli sam sufit; skali jego skutku dla progu wcześniej nie miałem.

## 4. Aktualizacja SYNTH_087, wiersz 7

E4 dla j22 jest teraz zmierzone, a nie oszacowane: −0.05…−0.08 dex (`E4_INTERMEDIATE`, szum ~0.015–0.03 na pierwiastek). Dla j62 nadal tylko oszacowanie (emisja < 1e9 g to ok. 10%); po tym wyniku należy je czytać jako ≈ −0.01, nie −0.005.

## 5. Trzy warstwy

- **Wynik:** jak §2–§3.
- **Konfiguracja:** wariant C jest modelem trendu, nie hadronizacją ponad 1e5 GeV. Tej nie da się policzyć tablicami BlackHawk v2.3. Pojedyncza masa, ramię orig, generator PYTHIA.
- **Uczenie systemu:**
  - Oszacowanie tablicowe ważone liczbą hadronów zaniża wpływ późnej emisji. Przy przyszłych oszacowaniach osi tablicowych ważę emisję czasem względem zamrożenia, nie tylko liczbą, albo od razu mierzę.
  - Etykieta progowa bez warunku rozdzielczości to drugi raz ten sam wzorzec, co LI w 085. Łatka: każda etykieta progowa dostaje warunek |estymanda| ≥ k·szum z kontroli ślepych.

## 6. Dane

- `data/analysis088.json`, `net088_raw.jsonl`, `summary_{a,c}_orig_088.csv`, `tables088.json`;
- tablice `hadrons_088_{A,C}.dat`;
- `timeline_088.log`, `tables_sha256_088.log`, `{full,dedup}_rate_dumps_088_sha256.log`.
- SHA wszystkich plików w `MANIFEST_SHA256_085.md` (sekcja 088).
- I1 zewnętrzne wymagane: przeliczenie 12 pierwiastków z plików danych.

## r2 (21 XI ok. 22:43): korekty po LT9 ROT012 (22:40, przed moim zapisem nieprzeczytane)

- **Korekta liczby w §3.** Wzrost wydajności w wariancie C ważony liczbą emitowanych hadronów wynosi +0.026 dex, czyli ≈ +6%, a nie „2–3%”. LT9 ROT012 ma niezależnie +6.2% (π) dla j22 i +0.86% dla j62, z całki od 1e8 g do m₀.
  - Poprawione rozumowanie: ΔY rośnie o 5–13%. Dźwignia ΔY na jednostkę logarytmu wydajności wynosi więc ~1.1, wobec ~0.57 przy jednorodnej zmianie wydajności (HER/PY w REVIEW_086).
  - Hipoteza o większej dźwigni późnej emisji pozostaje, ale z tym współczynnikiem.
  - Błąd oszacowania w SYNTH_087 leżał w przełożeniu na próg (przyjąłem dźwignię jednorodną), a nie w wydajnościach.
- **Zastrzeżenie LT9 (przyjęte).** Wariant C zmienia także wiersze 0–4 powyżej 1e9 g. W całce LT9 to ~4% (j22) i ~6% (j62) zmiany źródła pionów.
  - E4_C jest więc efektem traktowania całej dziedziny dotkniętej sufitem (wiersze 0–4 + poniżej 1e9 g), a nie czysto „poniżej 1e9 g”.
  - Oddzielenie wymagałoby osobnego ramienia (tylko wiersze poniżej 1e9 g). Ze względu na znakowe, zależne od czasu jądro odpowiedzi udziału ~4% nie przenoszę wprost na Y_p.
- Pierwszeństwo całek źródłowych należy do LT9. Liczby natywne progu (§2) są bez zmian.
