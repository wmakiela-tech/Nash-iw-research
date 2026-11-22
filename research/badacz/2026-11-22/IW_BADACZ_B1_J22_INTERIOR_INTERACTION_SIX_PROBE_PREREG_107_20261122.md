---
artifact_id: IW_BADACZ_B1_J22_INTERIOR_INTERACTION_SIX_PROBE_PREREG_107_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel 083/084; wykonanie prośby właścicielskiej SCOPE12 ROT010 i AUD3 ROT015
created_at: 2026-11-22
document_type: PREREGISTRATION (zamrożona przed przebiegiem natywnym)
authorization: obrót „O” Moderatora 22 XI 18:33; zapowiedź w odpowiedzi z 18:24; stała autoryzacja przebiegów 21 XI 16:05
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_107: sześć celowanych przebiegów dla interakcji C (kod × sieć, orig × E5) przy j22 wewnątrz przedziału [0.2484, 0.251]

## 1. Prośba

**SCOPE12 ROT010** (potwierdzone przez AUD3 ROT015):
- Na danych 083 interakcja C(Y) = [b_NET,E5 − b_NET,orig] − [b_CODE,E5 − b_CODE,orig] przy j22 osiąga |C| = 0.0275 dex wewnątrz przedziału, przy Y* = 0.25027090 (dokładny węzeł CODE_e5, log β = −17.05). Wariant PCHIP daje 0.0301.
- Sześć przebiegów z przedziałami ±0.001 dex wokół trzech nieznanych pierwiastków miałoby warunkowo potwierdzić C ∈ (−0.0305, −0.0245).

Wykonuję ten projekt dokładnie tak, jak go zaprojektowano.

## 2. Przebiegi (`run107.sh`, drzewo autorów, kod bez zmian)

Pierwiastki liniowe z 083 przy Y* (`grid107.json`):

| pierwiastek | log β |
|---|---|
| CODE_orig | −17.339625 |
| NET_orig | −17.815349 |
| NET_e5 | −17.553222 |

- **Sondy:** pierwiastek ± 0.001 dex. Ramię orig: 4 przebiegi (CODE i NET), ramię e5: 2 przebiegi (NET).
- **Kontrola sterownika:** o22_1730 musi być bitowo równe 083 (kod i sieć).
- **Skala:** 7 przebiegów Julii i 8 PRyMordial, ~5 min.

## 3. Analiza (`analysis_107.py`, sprawdzona na atrapie)

**Bramki:**

| bramka | warunek |
|---|---|
| G_COMPLETE | komplet przebiegów |
| G_RUN | jak w poprzednich przebiegach |
| G_V2 | ≤ 1e−6 |
| G_DRIVER | kontrola bitowo równa 083 |

**Wielkości:**
- Przedział jest ważny tylko wtedy, gdy wartości sond leżą po obu stronach Y*. Poza przedziałem nie interpoluję.
- C_probe liczę z pierwiastków sond i dokładnego węzła CODE_e5.

**Etykiety:**

| etykieta | warunek |
|---|---|
| `CERTIFIED_WINDOW` | wszystkie 3 przedziały ważne i C_probe ∈ (−0.030498, −0.024498) |
| `OUTSIDE_WINDOW` | wszystkie 3 ważne, C_probe poza oknem |
| `BRACKET_FAIL` | którykolwiek przedział nieważny |

**Opisowo:** różnica dY między sondami każdego przedziału na tle oczekiwanej różnicy z nachylenia.

## 4. Predykcja (moja, zamrożona)

**Pr1:** wynik ≠ `CERTIFIED_WINDOW`.

**Uzasadnienie:**
- Nachylenie to 0.006–0.008 na dex, więc oczekiwana różnica dY między sondami wynosi tylko 1.2–1.6e−5.
- Udokumentowane wahanie solwera na pojedynczym węźle to rms 2–7e−5 (REVIEW_095, ramiona J i R).
- Wąskie przedziały rozdzielą więc wahanie solwera, a nie błąd interpolacji. Wyjątek: wahanie byłoby silnie skorelowane na odległości 0.002 dex, a to jest właściwie pytanie, na które ten przebieg odpowiada.

Przy niezależnym wahaniu oczekuję, że co najmniej jeden przedział będzie nieważny, a C_probe ustawi się z rozrzutem ~0.01 dex.

## 5. Granice

- Jedna masa, jeden Y*.
- Wynik dotyczy rozdzielczości solwera i interpolacji, a nie fizyki.
- Bez progu PBH.
