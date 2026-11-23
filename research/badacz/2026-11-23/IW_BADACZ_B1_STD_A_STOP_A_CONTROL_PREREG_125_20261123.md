---
artifact_id: IW_BADACZ_B1_STD_A_STOP_A_CONTROL_PREREG_125_20261123
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel przebiegów natywnych B1
created_at: 2026-11-23
document_type: PREREGISTRATION (zamrożona przed przebiegami)
authorization: rotacja „O” 22:51; pytanie o kolejność (1)/(2)/(3) z 14:04 bez odpowiedzi, więc przyjmuję rekomendowane (1); stała autoryzacja 21 XI 16:05
answers: REC14 ROT011/ROT014 (STOP A), EKS1 ROT028 (IDEA-A)
claim_ceiling: NUMERYCZNY w modelu kodu Wu–Xu [▷] / MODEL_CONDITIONAL / NO_PBH_BOUND / NO_AUTHOR_ERROR_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_125: kontrola STOP A, czyli czy przesunięcie STD_A przetrwa zmianę kontynuacji q_h poniżej 1e9 g

## 1. Cel

REVIEW_124: STD_A przesuwa próg Y_code = 0.251 o −1.384 dex przy j22 i o −0.244 przy j62.

STOP A (REC14 ROT011/014) mówi, że tego nie da się promować fizycznie. Przy j22 81% hadronów pochodzi z ekstrapolacji tablicy poniżej 1e9 g, której bilansu energii nie sprawdzono (G_EC+(b) obejmuje tylko 2e9–1e11 g).

Ten PREREG nie zamyka STOP A. Sprawdza, czy przesunięcie STD_A zależy od tej ekstrapolacji w fizycznie dopuszczalnym przedziale.

**Postać kontynuacji.** q_h = P_BH × n_E, gdzie:
- P_BH ∝ M⁻², bo f_BH jest stałe poniżej 1e10 g (REVIEW_120);
- liczba hadronów na GeV n_E ∝ E^(α−1) ∝ M^(1−α), przy stałym ułamku energii w hadronach i średniej krotności N(E) ∝ E^α.

Stąd q_h ∝ M^s, gdzie s = −(1+α). Przy stałym ułamku energii każde α daje energetycznie spójną kontynuację. Niepewne jest samo α, więc obejmuję je przedziałem:

| ramię | s | α | znaczenie |
|---|---|---|---|
| m10 | −1.0 | 0 | stała krotność |
| (kod, run123) | −1.197…−1.205 | ~0.2 | ekstrapolacja wierszy 0–1 w kodzie autorów |
| m13 | −1.3 | 0.3 | recepta z artykułu (T^1.3) |
| m15 | −1.5 | 0.5 | skrajna |

Tablice budowane są tak samo jak w PREREG_116: 20 wierszy dopisanych przy M0·10^(−k/2), k = 1…20. Nagłówek i 100 wierszy autorów pozostają bajtowo te same (bramka G_TAB). Dodatkowo raportuję bez progu α_PY, czyli lokalny wykładnik krotności hadronów w tablicach PYTHIA przy E′ = 1e4–1e5 GeV.

## 2. Ramiona i przebiegi

- Sterownik `std_a_123.jl` bez zmian: base albo std (dM/dt × 0.5817518), solwer autorów, siatka A, 4 bisekcje.
- Masy j22, j62 i j20 (lewa ściana) × 3 tablice × 2 ramiona = 18 procesów.
- Kopie drzewa autorów różnią się wyłącznie tablicą (sprawdzane przez `diff -rq`).
- Odniesienie dla kontynuacji kodu stanowią pierwiastki z run123 (REVIEW_124).
- Pilotów nie ma; czas jednego procesu jest znany z run123 (~2 min).

## 3. Bramki i predykcje (`code/analysis_125.py`)

**Bramki:**
- G_TAB: wiersze autorów zachowane bajtowo.
- G_RUN: 18/18 pierwiastków, wszystkie ewaluacje z retcode Success.

**Predykcje.** Hipoteza H_robust: przesunięcie STD_A wynika głównie z czasu życia i obu ramionom zmienia się podobnie, więc wolno pozostaje odporne na kontynuację. Uzasadnienie: liczba hadronów poniżej 1e9 g skaluje się jak M0^(s+3)/(s+3) i zmienia o −10% (s = −1.0) do +20% (s = −1.5) względem kodu w obu ramionach.

| id | wielkość | odniesienie | tolerancja |
|---|---|---|---|
| P_A1 | Δ_s(j22) = r_std − r_base, dla każdego s | −1.384 (kod) | ±0.15 |
| P_A2 | Δ_s(j62) | −0.244 (kod) | ±0.05 |
| P_A3 | pierwiastek std przy j20 istnieje dla każdego s | REVIEW_124 | — |

Raportowane: pierwiastki bezwzględne base i std w zależności od s (czułość d r/d s) oraz α_PY. Tolerancje są ≥ udokumentowanego szumu 0.03 dex.

## 4. Interpretacja (ustalona przed przebiegiem)

- **P_A1–P_A3 PASS.** Przesunięcie STD_A jest odporne na kształt energetycznie spójnej kontynuacji w przedziale α ∈ [0, 0.5].
  - Część STOP A dotycząca nachylenia jest wtedy zamknięta dla przesunięcia (nie dla bezwzględnego progu).
  - Otwarte zostają: normalizacja przy 1e9 g (obcięcie E′ ≤ 1e5 GeV, ~4% mocy), samo istnienie jednego α dla jetów > 100 TeV, G_DEP, STOP B i brak sieci.
- **FAIL.** Przesunięcie zależy od nieweryfikowanej ekstrapolacji; raportuję zakres i przy j22 nie promuję go nawet jako wyniku zależnego od modelu bez dodatkowego zastrzeżenia.
