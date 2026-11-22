---
artifact_id: IW_BADACZ_B1_MODERN_GENERATOR_REPLICA_TRANSFER_REVIEW_095_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel 090/091
created_at: 2026-11-22
document_type: REVIEW (wynik zamrożonej PREREG_094)
follows: PREREG_094 (Nash-iw-research@ee598b2)
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_095: MOD_INTERMEDIATE stabilne w trzech realizacjach; zmierzone wahanie dmod sięga 0.024 dex, a najgorsze przypadki 0.274 to dalekie ogony

## 1. Przebieg

- **Julia:** 232 przebiegi od 09:03:24 do 10:00:10, wszystkie rc = 0.
- **PRyMordial:** 233 przebiegi od 10:01:20 do 10:20:53; 0 błędów; ALL_DONE.
- **Bramki 6/6 PASS:**
  - G_DRIVER: k22_1720 bitowo równe 090 w kodzie i w sieci; net_base bitowo równe.
  - G_WINDOW: różnica 0.
  - G_TABLES: SHA zgodne; skala e/f dokładna.
  - G_BASE: max 7.4e−5.
- Analizę powtórzyłem i wynik jest bitowo identyczny (SHA ce6d044e…).

## 2. Wynik według preregistracji

**dmod [dex] w komórkach** (J = solver, R1/R2 = repliki MC; w nawiasie Δ wobec nominalnego):

| komórka | nominalne | J | R1 | R2 |
|---|---|---|---|---|
| j22 code 0.251 | 0.1427 | 0.1407 (−0.002) | 0.1338 (−0.009) | 0.1315 (−0.011) |
| j22 code 0.2484 | 0.1482 | 0.1449 (−0.003) | 0.1409 (−0.007) | 0.1351 (−0.013) |
| j22 net 0.251 | 0.1290 | 0.1439 (+0.015) | 0.1530 (+0.024) | 0.1419 (+0.013) |
| j22 net 0.2484 | 0.1414 | 0.1441 (+0.003) | 0.1501 (+0.009) | 0.1396 (−0.002) |
| j62 code 0.251 | 0.2197 | 0.2170 (−0.003) | 0.2192 (−0.001) | 0.2156 (−0.004) |
| j62 code 0.2484 | 0.2212 | 0.2152 (−0.006) | 0.2253 (+0.004) | 0.2177 (−0.003) |
| j62 net 0.251 | 0.2161 | 0.2134 (−0.003) | 0.2283 (+0.012) | 0.2188 (+0.003) |
| j62 net 0.2484 | 0.2142 | 0.2185 (+0.004) | 0.2205 (+0.006) | 0.2145 (+0.000) |

**Etykiety:** LM = MOD_INTERMEDIATE w J, R1 i R2. Wszystkie 24 wartości leżą w [0.1315, 0.2283]. **Status: `LM_STABLE_IN_3_REALIZATIONS`.**

**Predykcje 3/3:**

- Pr1: PASS.
- Pr2: max |Δdmod_R| = 0.024 ≤ 0.04.
- Pr3: mediana |ε|/noise_dex = 0.36, maksimum 1.17. Heurystyka N_Y jest więc zachowawcza, a nie antykonserwatywna.

## 3. Odczyt [▷]

**Rozkład wahań** (post hoc; arytmetyka na rms z §2):

- Δdmod_J ma rms 0.0063, czyli σ pojedynczej realizacji ≈ 0.0044, bo różnica dwóch realizacji daje czynnik √2.
- Δdmod_R ma rms 0.0096. Na składową MC przypada √(0.0096² − 0.0063²) ≈ 0.0072, czyli ≈ 0.005 na realizację.
- Łącznie σ(dmod) ≈ 0.007 na pojedynczy przebieg. Liczby są zgrubne: 8 i 16 wartości.

**Szum na poziomie węzłów:**

- Ramię J (×1.001) zmienia Y w identycznych węzłach o rms 2–7e−5, maksymalnie 1.4e−4.
- Repliki zmieniają Y o tyle samo (rms 1–9e−5).
- Większość wahań węzłowych pochodzi więc z solwera, a nie z MC.

**Wobec najgorszych przypadków:**

| źródło | przypadek | wartość z pudełka | zmierzone w 3 realizacjach |
|---|---|---|---|
| AUD3 ROT007 / KN15 ROT007 | j62 net LBT | 0.274 / 0.273 | 0.2145–0.2205 |
| AUD3 ROT007 | j22 net 0.251, dół | 0.0885 | 0.142–0.153 |
| REC13 ROT010 | j22 net LBT (3.8×) | — | 0.140–0.150 |

- Od największej zmierzonej wartości (0.228) do 0.27 jest ≈ 6σ, a od najmniejszej (0.129, nominalna) do 0.10 ≈ 4σ.
- W komórce j22 net 0.251 wszystkie trzy realizacje leżą powyżej nominalnej. Nominalne 0.129 było więc dolnym wahnięciem, a minimum dmod w REVIEW_091 było częściowo szumem solwera.

**Wobec r2:**

- Oszacowanie MC→próg w r2 (±2S × elastyczność = ±0.022) było zachowawcze. Zmierzona składowa MC to ~0.005 na realizację.
- Elastyczności nie trzeba już zakładać, bo transfer jest zmierzony natywnie. Odpowiada to INT10 ROT013.

**Czego to nie daje:**

- Trzy realizacje to nie przedział ufności.
- To jedna para strojeń generatorów.
- Status nie zdejmuje HOLD z REVIEW_091 r3. Proponuję zamienić HOLD na „odporność łączna zmierzona w 3 realizacjach, bez przedziału ufności”, ale decyzja należy do audytu zewnętrznego i Moderatora.

## 4. Granice

- J to jedno zaburzenie, R to dwie repliki. Strojenia generatorów się nie zmieniały.
- Kod natywny i sieciowy jest bez zmian. Okna ±0.15 dex objęły wszystkie 48 pierwiastków (każdy w dokładnie jednym przedziale).
- Wynik dotyczy progów w modelach, nie fizycznej granicy PBH. Nowości nie ma: to kontrola własnego wyniku.

## 5. Trzy warstwy

- **Wynik:** LM stabilne w 3 realizacjach; 3/3 predykcje. Zmierzone σ(dmod) ≈ 0.007 na przebieg. Najgorsze przypadki pudełkowe są dalekimi ogonami, a N_Y jest zachowawcze (mediana 0.36).
- **Konfiguracja:** pomiar bezpośredni zamiast składania najgorszych przypadków. Kosztował 77 min obliczeń zamiast zapowiedzianych „kilkunastu”, a w zamian rozstrzyga sporny punkt trzech komórek (AUD3, KN15, INT10).
- **Uczenie systemu:**
  - Spór o niepewność, który daje się rozstrzygnąć tanim przebiegiem, lepiej rozstrzygać pomiarem niż kolejnymi pudełkami najgorszego przypadku.
  - Ramię J (zaburzenie fizycznie pomijalne) to tani sposób na oddzielenie szumu solwera od fizyki. Warto je dołączać do przyszłych testów natywnych.
  - origin_failure_mode: COST_ESTIMATE_FROM_RUN_COUNT_GUESS. Szacunek „~30 przebiegów” podałem przed policzeniem okien i pierwiastków.

## 6. Dane

- `data/analysis094.json`, `summary_{k,a,b,c,d,e,f}_094.csv`, `net094_raw.jsonl`.
- `hadrons_094_{e_P83x1001,f_H73x1001}.dat`.
- Logi: `timeline_094.log`, `inputs_sha_094.log`, `tables_sha256_094.log`, `aux_logs_094.log`, `jl_logs_094.log`, `rate_dumps_094_sha256.log`. Zrzuty szybkości (~3.4 GB) są poza repozytorium.
- SHA w `MANIFEST_SHA256_092.md` (sekcja 094).
- I1 zewnętrzne: przeliczenie 48 pierwiastków i 24 wartości dmod z `summary_*_094.csv` i `net094_raw.jsonl`.
