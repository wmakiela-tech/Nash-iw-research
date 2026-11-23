---
artifact_id: IW_BADACZ_B1_J22_RESIDUAL_VINTAGE_VS_PROCESSING_REVIEW_113_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel 099–112
created_at: 2026-11-22
document_type: REVIEW (wynik zamrożonej PREREG_112)
follows: PREREG_112 (Nash-iw-research@2bf0b18)
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_NOVELTY_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_113: reszta przy j22 to rocznik generatora (Herwig 7.1.5 → 7.3: −0.064…−0.083 dex), a nie obróbka tablic BlackHawk (|proc| ≤ 0.010). Kontrast H73 wobec tablicy HERWIG z BlackHawk w pełni rozłożony; Pr1–Pr4 PASS

## 1. Przebieg

- **MC (Herwig 7.1.5, √s = 2E, 11 kanałów, energie, zdarzenia i ziarna z 090; top bez 1e5 GeV, zgodnie z deklaracją):** 20:36:17–20:42:01, wszystkie energie rc = 0.
- **Julia:** 5 procesów, 20:42:18–21:04:33, rc = 0. **PRyMordial:** 106/106, 0 błędów; ALL_DONE 21:12:24.
- **Bramki tablic 5/5 PASS:** G_MC, G_STAT (max 0.61%), G_REBUILD_H73 i G_REBUILD_SC (bitowo), G_FINITE.
- **Bramki natywne 5/5 PASS:** G_TABLES, G_COMPLETE, G_V2, G_DRIVER (k22_1720 w kodzie i w sieci oraz net_base bitowo równe 099), G_BASE (max |ΔY_base| = 1.4e−4).
- Analiza uruchomiona w skrypcie przebiegu i powtórzona ręcznie: wynik bitowo identyczny (SHA d8c1ba36…). Domknięcie ścieżki = 0 we wszystkich komórkach.

## 2. Wynik według preregistracji

Wartości w dex, ujemne znaczy niższy próg. Ścieżka względem L: label_c (REVIEW_110), bin_c = r_V − r_c, proc = r_W − r_V, vint = r_H73 − r_W; suma = total(099) = r_H73 − r_l.

| komórka | label_c | bin_c | proc | vint | total |
|---|---|---|---|---|---|
| j22 code 0.251 | −0.032 | −0.066 | +0.003 | −0.083 | −0.177 |
| j22 code 0.2484 | −0.087 | −0.061 | +0.010 | −0.079 | −0.217 |
| j22 net 0.251 | −0.075 | −0.044 | −0.001 | −0.077 | −0.197 |
| j22 net 0.2484 | −0.076 | −0.043 | −0.009 | −0.064 | −0.192 |
| j62 code 0.251 | −0.074 | −0.049 | −0.006 | −0.014 | −0.143 |
| j62 code 0.2484 | −0.066 | −0.048 | −0.005 | −0.010 | −0.130 |
| j62 net 0.251 | −0.080 | −0.040 | −0.009 | −0.012 | −0.141 |
| j62 net 0.2484 | −0.079 | −0.046 | −0.005 | −0.017 | −0.147 |

**Predykcje:**

| predykcja | wynik | szczegół |
|---|---|---|
| Pr1 (\|proc\| ≤ 0.03 w ≥ 6/8) | **PASS** | 8/8, max 0.010 |
| Pr2 (vint ≤ −0.03 w ≥ 3/4 j22) | **PASS** | 4/4, −0.064…−0.083 |
| Pr3 (\|vint\| ≤ 0.03 w ≥ 3/4 j62) | **PASS** | 4/4, −0.010…−0.017 |
| Pr4 (\|bin_c − d_bin(099)\| ≤ 0.03 w 8/8) | **PASS** | max 0.010 |

## 3. Odczyt [▷]

**Kontrast w pełni rozłożony.** Różnicę progów między tablicą HERWIG z BlackHawk a H73 (−0.13…−0.22 dex względem L) tworzą trzy składniki:

| składnik | j22 | j62 |
|---|---|---|
| artefakty tablic BlackHawk: etykieta √s | −0.075…−0.087 (−0.032 w komórce o największym szumie) | −0.066…−0.080 |
| artefakty tablic BlackHawk: binowanie | −0.043…−0.066 | −0.040…−0.049 |
| obróbka przy stałym roczniku (skrypty BlackHawk, siatka, próg łączenia z PYTHIA, higgs) | −0.009…+0.010 | −0.005…−0.009 |
| rocznik generatora 7.1.5 → 7.3 (przepis i fold stałe) | −0.064…−0.083 | −0.010…−0.017 |

Poza dwoma artefaktami tablice BlackHawk są wiernym zapisem Herwig 7.1.5 także po złożeniu z widmem i na progu: |proc| ≤ 0.010 dex w 8/8 komórkach.

**Rocznik działa przez kaony.** Na poziomie tablic (opisowo, `tables112.json`, wiersze 0–28) W (7.1.5) względem H73 (7.3) daje: kaony −0.15…−0.20 dex, piony +0.025…+0.041, nukleony −0.02…+0.02. Herwig 7.3 daje więc w tym przepisie o 40–60% więcej kaonów na pierwotną niż 7.1.5. Efekt rocznika na progu jest przy j22 4–8 razy większy niż przy j62. Zgadza się to z większą rolą kaonów przy j22, ale tego nie testowałem.

**Skutek dla GAP-005.** Składowa dhold (+0.13…+0.22) to:
- przy j22: artefakty tablic ~+0.12…+0.15 i rocznik ~+0.06…+0.08;
- przy j62: artefakty ~+0.11…+0.13 i rocznik ~+0.01…+0.02.

Część „rocznikowa” jest prawdziwą systematyką generatora, tej samej natury co dmod (REVIEW_091/095); część artefaktowa nie jest fizyką.

## 4. Granice

- vint łączy rocznik i domyślne strojenie (7.1.5 i 7.3 z ustawieniami domyślnymi); nie rozdziela zmian w modelu klastrowym od zmian parametrów.
- proc łączy kilka drobnych czynników bez rozdzielenia; ich suma jest mała.
- Top powyżej 51 200 GeV przycięty w W (zadeklarowane); ten sam zabieg po stronie 7.3 zmienia wydajności o ≤ 0.0013 dex.
- Pojedyncze przebiegi; szum pojedynczego pierwiastka do ~0.03 (komórka j22 code 0.251).
- Wynik dotyczy progów w natywnym modelu Wu–Xu, nie fizycznej granicy PBH. Nowość nie ustalona (NOTE_114).

## 5. Trzy warstwy

- **Wynik:** kontrast „tablica HERWIG z BlackHawk wobec Herwig 7.3” na progu β to artefakty tablic (etykieta i binowanie) plus rocznik generatora działający przez kaony. Pozostała obróbka BlackHawk jest pomijalna. Pr1–Pr4 PASS.
- **Konfiguracja:** MC zajęło 6 minut zamiast szacowanych 15–25, więc cały krok trwał 36 minut. Rozdzielenie na rocznik i obróbkę wymagało tylko jednego nowego ramienia generatora, bo przepis, fold i ziarna wziąłem bez zmian z 090.
- **Uczenie systemu:**
  - Sprawdzenie domknięcia w kodzie analizy wykryło przed przebiegiem błąd w REVIEW_110 §3 (DECOMPOSITION_REFERENCE_MIXED). Łatka działa: każdy rozkład ma teraz jawne domknięcie względem definicji total z kodu źródłowego.
  - Dysk był bliski zapełnienia (3.1 GB wolne przed przebiegiem wymagającym ~2 GB). Usunąłem lokalne kopie robocze (zduplikowane zrzuty po scaleniu, kopie katalogów źródłowych, katalogi robocze przerwanych przebiegów MC); nic, czego nie da się odtworzyć z repozytorium. origin_observation: przed każdym przebiegiem natywnym sprawdzać `df` wobec szacowanego rozmiaru zrzutów.

## 6. Dane

- `data/analysis112.json`, `tables112.json`, `hadrons_112_{W,V}.dat`, `summary_{w,v,k}_112.csv`, `net112_raw.jsonl`, `mc112/herwig71_*.json`.
- Logi: `timeline_112.log`, `inputs_sha_112.log`, `tables_sha256_112.log`, `spec_112.log`, `mc_logs_112.log`, `jl_logs_112.log`, `aux_logs_112.log`, `rate_dumps_112_sha256.log`.
- Surowe zrzuty usunąłem po zapisaniu SHA (zgoda Moderatora). SHA w `MANIFEST_SHA256_092.md` (sekcja 112/113).

## r2 (23 XI, 07:19, godzina z `date` przy zapisie): rola ekstrapolacji poniżej 1e9 g

j22 = 1.121e9 g, więc ~49% hadronowej konwersji n↔p przypada na masy poniżej najniższego wiersza tablicy, gdzie kod Wu–Xu ekstrapoluje nachylenie wierszy 0–1 (REVIEW_110 r3). Różnica nachyleń W i V daje przy 5e8 g ≤ 0.003 dex, a H73 i W ≤ 0.012 dex w kierunku przeciwnym do vint. Wnioski §3 bez zmian; „rocznik działa przez kaony” odnosi się do modelu z tą ekstrapolacją.
