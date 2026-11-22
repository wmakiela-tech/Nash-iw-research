---
artifact_id: IW_BADACZ_B1_HERWIG_TABLE_FACTORIAL_V_ARM_REVIEW_102_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel 099/100/101
created_at: 2026-11-22
document_type: REVIEW (wynik zamrożonej PREREG_101)
follows: PREREG_101 (Nash-iw-research@47414e2)
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_NOVELTY_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_102: układ 2×2 domknięty, interakcja etykieta × binowanie pomijalna (|I| ≤ 0.009 w 7/8 komórek); efekty główne: binowanie −0.047, etykieta √s −0.073 (j62) i −0.01…−0.03 (j22, ekstrapolacja Sa). Pr1–Pr3 PASS

## 1. Przebieg

- **Julia:** 105 przebiegów, 13:58:54–14:23:23, rc = 0.
- **PRyMordial:** 106 przebiegów, 14:23:55–14:32:41, 0 błędów; ALL_DONE.
- **Bramki 5/5 PASS:**
  - G_TABLES: V/L = 0.0456707 dex na wierszach 0–28;
  - G_REBUILD: L odtworzone bitowo;
  - G_DRIVER: k22_1720 i net_base bitowo równe 099;
  - G_COMPLETE, G_V2, G_BASE.
- Analizę powtórzyłem i wynik jest bitowo identyczny (SHA e3b7201d…).

## 2. Wynik według preregistracji: Pr1, Pr2 i Pr3 PASS

Wartości w dex.

| komórka | etykieta na starym bin. | etykieta na nowym bin. | **etykieta (główny)** | bin. na starej etyk. | bin. na nowej etyk. | **bin. (główny)** | I | dj |
|---|---|---|---|---|---|---|---|---|
| j22 code 0.251 | +0.008 | −0.031 | −0.012 | −0.019 | −0.058 | −0.039 | **−0.039** | **+0.034** |
| j22 code 0.2484 | −0.035 | −0.033 | −0.034 | −0.062 | −0.061 | −0.062 | +0.002 | −0.016 |
| j22 net 0.251 | −0.024 | −0.025 | −0.025 | −0.044 | −0.046 | −0.045 | −0.001 | +0.008 |
| j22 net 0.2484 | −0.027 | −0.035 | −0.031 | −0.045 | −0.053 | −0.049 | −0.008 | +0.001 |
| j62 code 0.251 | −0.074 | −0.073 | −0.073 | −0.048 | −0.047 | −0.047 | +0.001 | −0.005 |
| j62 code 0.2484 | −0.068 | −0.077 | −0.072 | −0.039 | −0.048 | −0.044 | −0.009 | +0.008 |
| j62 net 0.251 | −0.070 | −0.072 | −0.071 | −0.046 | −0.048 | −0.047 | −0.001 | +0.001 |
| j62 net 0.2484 | −0.076 | −0.077 | −0.077 | −0.044 | −0.045 | −0.044 | −0.001 | −0.002 |

**Predykcje:**

- **Pr1:** |I| ≤ 0.04 w 8/8 komórkach; poza jedną |I| ≤ 0.009.
- **Pr2:** efekt główny etykiety < 0 w 8/8.
- **Pr3:** szum dj ma medianę 0.0065 i maksimum 0.034 (próg 0.04).

## 3. Odczyt [▷]

**Interakcja jest pomijalna.**

- Kolejność poprawek nie ma znaczenia: oba wiersze etykiety, podobnie jak oba wiersze binowania, zgadzają się do ≤ 0.009 w 7/8 komórek.
- Zastrzeżenie Mech-S10 ROT014 i INT10 ROT018 jest zasadne co do metody, ale w praktyce nie zmienia wyniku. Udziały ze ścieżki z REVIEW_100 są bliskie Shapleyowi poza komórką j22 code 0.251.

**Wyjątek j22 code 0.251 to odchylenie pojedynczego pierwiastka r_L o ~−0.03.** Wskazują na to trzy niezależne objawy w tej samej komórce:

| objaw | źródło | wartość |
|---|---|---|
| d_ctrl = r_L − r_HERBH | REVIEW_100 | −0.031 |
| dj = r_E − r_L (+ log₁₀1.0001) | ten przebieg | +0.034 |
| I | ten przebieg | −0.039, zgodne z przesunięciem r_L o −0.03 w obu różnicach „na starym” |

Oszacowanie Shapleya, czyli średnia obu ścieżek, połowicznie tłumi to odchylenie.

**Efekty główne (Shapley):**

| składnik | wartość | uwaga |
|---|---|---|
| binowanie | −0.039…−0.062, średnio −0.047 przy obu masach | ≈ przesunięcie wejścia 0.0457 dex × elastyczność ~1 |
| etykieta √s, j62 | −0.071…−0.077 | |
| etykieta √s, j22 | −0.012…−0.034 | ekstrapolacja Sa; z Sb byłoby więcej (REVIEW_100) |

**Szum solwera (drugi pomiar):**

- Mediana 0.0065, maksimum 0.034, czyli odchylenia ~0.03 w pojedynczych komórkach się powtarzają.
- Dla każdej przyszłej bramki kontrolnej zakładam ≥ 0.04 na pojedynczy pierwiastek (patrz REVIEW_100, uczenie).

## 4. Granice

- Ekstrapolacja ponad 5e4 GeV jak w Sa (stała), więc etykieta przy j22 to dolna wartość z dwóch wariantów.
- Pojedyncze przebiegi; dj to diagnostyka szumu łącznie z nierównoważnością skali tablicy i β (REVIEW_095 r2).
- Wynik dotyczy progów w modelach, nie fizycznej granicy PBH. Nowość etykiety √s nadal nie jest ustalona.

## 5. Trzy warstwy

- **Wynik:**
  - układ 2×2 domknięty, interakcja pomijalna;
  - binowanie ~−0.047 dex; etykieta √s ~−0.073 (j62) i −0.01…−0.03 (j22, Sa);
  - szum pojedynczego pierwiastka do ~0.03, mediana ~0.007;
  - Pr1–Pr3 PASS.
- **Konfiguracja:** dodatkowe 35 minut obliczeń zamieniło zastrzeżenie metodyczne w pomiar. Przy okazji zidentyfikowało pojedynczy odchylony pierwiastek trzema niezależnymi objawami.
- **Uczenie systemu:** tolerancje wyprowadzone z udokumentowanego maksimum szumu (łatka z REVIEW_100) przeszły pierwszy test. Gdy ten sam pierwiastek jest bazą kilku różnic, jego pojedyncze odchylenie trzeba diagnozować łącznie (d_ctrl, dj, I), zanim się je zinterpretuje.

## 6. Dane

- `data/analysis101.json`, `tables101.json`, `hadrons_101_V.dat`, `hadrons_101_E_Lx10001.dat`, `summary_{k,v,e}_101.csv`, `net101_raw.jsonl`.
- Logi: `timeline_101.log`, `inputs_sha_101.log`, `tables_sha256_101.log`, `aux_logs_101.log`, `jl_logs_101.log`, `rate_dumps_101_sha256.log`.
- Surowe zrzuty usunąłem po zapisaniu SHA.
- SHA w `MANIFEST_SHA256_092.md` (sekcja 101).
