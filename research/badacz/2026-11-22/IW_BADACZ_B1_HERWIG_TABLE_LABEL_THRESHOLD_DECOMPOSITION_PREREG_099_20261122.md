---
artifact_id: IW_BADACZ_B1_HERWIG_TABLE_LABEL_THRESHOLD_DECOMPOSITION_PREREG_099_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel 085/090/098
created_at: 2026-11-22
document_type: PREREGISTRATION (zamrożona przed przebiegiem natywnym)
authorization: obrót „O” Moderatora 22 XI 12:33 (praca z funkcji; krok zapowiedziany w odpowiedzi po REVIEW_098); stała autoryzacja przebiegów 21 XI 16:05
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_NOVELTY_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_099: rozkład kontrastu „tablica HERWIG z BlackHawk względem Herwig 7.3” na progu β: etykieta √s, binowanie i reszta

## 1. Pytanie

REVIEW_098 rozłożył różnicę tablic na trzy składniki: binowanie (0.046 dex), etykietę √s (~0.1) i deficyt kaonów (do ~0.2). Ile każdy z nich daje na progu β? Kontrast dhold między historycznym HERBH a H73 wynosi +0.13…+0.22 dex (REVIEW_091/095, NOTE_096).

## 2. Tablice (`build_tables_099.py`, złożenie jak w 090)

Pod energią podziału tablice używają BH-PYTHIA, nad nią BH-HERWIG. Każda część jest dzielona przez własny czynnik binowania BlackHawk, tak jak w R2.

| tablica | zawartość | rola |
|---|---|---|
| **L** | HERWIG zgodnie z etykietą (wiersz E′ dla pierwotnego E′), podział 25 GeV | kontrola: odtwarza R2 do 1.4e−4 (G_CTRL, sprawdzone na próbie) |
| **Sa** | HERWIG przeetykietowany (wiersz E′ dla pierwotnego E′/2; kolumna `higgs` bez zmiany, bo pojedynczy pierwotny ma √s), podział 12.5 GeV; nad 5e4 GeV stała | poprawka √s |
| **Sb** | jak Sa, ale nad 5e4 kształt energetyczny z H73 | wariant ekstrapolacji |
| **Ua** | jak Sa, część HERWIG z konwencją binowania PY/H73 (÷1.0258 zamiast ÷1.1396) | poprawka √s i binowania |

Na poziomie tablic (próba) Sa/L wynosi +0.06…+0.08 dex, Sb/L +0.07…+0.08, a Ua/L +0.10…+0.13.

## 3. Przebiegi (`run099.sh`, kod natywny i sieciowy bez zmian)

- **Ramiona:** l, s, b, u. Każde ma 52 węzły: węzły siatki 0.05 dex w sumie przedziałów [root_H73 − 0.15, root_HERBH + 0.15] po 4 komórkach, plus bazy.
- **Kontrola k:** tablica R2, węzeł 22 −17.20 (085 ho22_1720).
- **Skala:** 209 przebiegów Julii (dwa procesy: k, l, s oraz u, b) i 210 PRyMordial; ~60 min.

## 4. Bramki i estymaty (`analysis_099.py`, sprawdzone na atrapie)

**Bramki:**

| bramka | warunek |
|---|---|
| G_TABLES | G_CTRL ≤ 1% i G_FINITE |
| G_COMPLETE | komplet identyfikatorów i przebiegów sieciowych |
| G_V2 | jak w 090/094 |
| G_DRIVER | k i net_base bitowo równe 085/090 |
| G_BASE | ≤ 5e−4 |

**Estymaty w każdej komórce:**

| estymata | definicja |
|---|---|
| d_ctrl | r_l − r_HERBH |
| d_label | r_s − r_l (oraz d_label_b = r_b − r_l) |
| d_bin | r_u − r_s |
| d_resid | r_H73 − r_u |
| total | r_H73 − r_l = d_label + d_bin + d_resid (tożsamość) |

- **G_LINK:** max |d_ctrl| ≤ 0.03. Bez tego rozkład odnoszę tylko do L, a nie do historycznego dhold.

## 5. Predykcje (moje, zamrożone)

- **Pr1:** d_label < 0 w 8/8 komórkach (więcej hadronów, więc niższy próg).
- **Pr2:** |d_label| ≥ 0.3·|total| w co najmniej 6/8.
- **Pr3:** d_resid < 0 w co najmniej 6/8 (po poprawkach H73 nadal silniejszy, przez kaony).
- **Pr4:** G_LINK PASS.

## 6. Granice

- Ponad 5e4 GeV nie ma danych HERWIG. Rozrzut Sa/Sb pokazuje wrażliwość na ekstrapolację, ale jej nie ogranicza.
- d_resid łączy rocznik generatora, strojenie i resztę różnic przepisu, czyli wszystko, co nie jest etykietą ani binowaniem.
- Każda komórka to pojedynczy przebieg. Szum solwera ~0.007 na pierwiastek (REVIEW_095) dotyczy też różnic.
- Wynik dotyczy progów w modelach, nie fizycznej granicy PBH.
