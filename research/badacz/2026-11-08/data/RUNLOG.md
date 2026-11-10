---
artifact_id: IW_BADACZ_WUXU_BAND_KERNEL_RUNLOG_20261108
exposure: PUBLIC
claim_ceiling: PROVENANCE_LOG / NO_RESULT_BEYOND_LINKED_REVIEWS / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-08
origin_cell: BADACZ (wątek Claude)
document_type: RUNLOG
---

# RUNLOG — PREREG_048 / REVIEW_050 oraz REVIEW_049 (8 XI 2026)

**Środowisko:** jak w `research/badacz/2026-10-31/data/native_audit/RUNLOG.md`.
- Julia 1.12.3, kod autorów `d395183`, 2 rdzenie, 8 GB RAM.
- Python 3, sympy 1.13.3, numpy 2.1.3.

| czas (CET) | przebieg | plik | uwagi |
|---|---|---|---|
| ~09:05 | kontrola tożsamości sterownika (`k = 1`, 3 punkty, `j = 22`) | `identity.csv` | `Y_C` identyczne bitowo z `research/badacz/2026-11-02/data/grid_native.csv` (2 punkty); przed preregiem |
| ~09:07 | udziały liczbowe pasm | `band_number_shares.json` | z tabeli autorów; przed preregiem |
| 09:08 | PREREG_048 opublikowany (`b7a2c14`) | — | przed przebiegami produkcyjnymi |
| 09:09– | produkcja: 32 konfiguracje, 2 procesy (`w1`: `j = 22, 62`; `w2`: `j = 28, 34`) | `kernel_w1.csv`, `kernel_w2.csv` | tolerancja domyślna |
| ~09:12 | REVIEW_049: ślady Diraca i sumy spinorowe | `appendixB_dirac_trace_check.json` | niezależne od przebiegów Julii |
| 09:09–09:47 | `w1`, `w2` ukończyły `base`, `A×2`, `B×2`, `C×2` dla `j = 22, 28` | `kernel_w1.csv`, `kernel_w2.csv` | po ~1.5 min na konfigurację |
| ~09:24 | `w2`, `C×10` przy `j = 28` | — | proces **zabity przez OOM** (anon-rss 3.3 GB), bez ukończonego punktu |
| 09:25–09:47 | `w1`, `C×10` przy `j = 22` | `kernel_w1.csv` (1 wiersz `bracket`) | pierwszy punkt trwał 1286 s; przerwany `kill -9` o 09:47 |
| 09:47 | **odstępstwo od PREREG_048**, przed jakimkolwiek wynikiem dla pasma D | — | szczegóły pod tabelą |
| 09:48– | `w3`: `D×2`, `D×0` (`j = 22`) i wszystkie konfiguracje bez ×10 dla `j = 62`; `w4`: to samo dla `j = 28` i `34` | `kernel_w3.csv`, `kernel_w4.csv` | pierwsza próba uruchomienia (`&`) przerwana po kilku sekundach i ponowiona jako zadanie w tle; pliki tymczasowe przerwanych procesów usunięte z klonu autorów |

| 09:50 | model zabawkowy wymywania, post hoc (`code/wuxu_washout_toy_kernel.py`) | `washout_toy_kernel.json` | liczony po obejrzeniu natywnych A/B/C dla `j = 22, 28`; przewidywania dla D oraz dla `j = 34, 62` commitowane przed obejrzeniem tych wyników (w chwili commitu `kernel_w3.csv` miał 15 wierszy, `kernel_w4.csv` 16; nie otwierałem ich) |

| ~09:51 | moje zadanie oczekiwania na koniec przebiegu wyszło od razu | — | warunek łapał stary wpis OOM z 09:24 w `dmesg`; bez wpływu na przebiegi (monitor liczył tylko nowe OOM) |
| 09:48–10:00 | `w3`, `w4` ukończone | `kernel_w3.csv`, `kernel_w4.csv` | bez OOM |
| 10:01– | N1: `base` i `D×2` przy `j = 22`, `BADACZ_TOL=1e-4:1e-7`, 2 procesy | `n1_base.csv`, `n1_D2.csv` | około 41 s na punkt |

| ~10:13 | N1 ukończone; analiza końcowa | `n1_base.csv`, `n1_D2.csv`, `kernel_analysis.json` | `Δ(D×2)` zmienia się o `+0.0045` dex (PASS) |

**Odstępstwo od PREREG_048 (09:47):**
- **Powód:** `C×10` i `D×10` są obliczeniowo niewykonalne przy domyślnym solverze autorów. Silna iniekcja w końcowym
  wybuchu wymusza bardzo wiele kroków, a `magic()` zapisuje każdy krok, co prowadzi do OOM. To ta sama klasa awarii co
  w REVIEW_035.
- **Co usunięte:** `C×10` i `D×10` przy wszystkich masach.
- **Czym zastąpione:**
  - pasmo D: łączę preregowane `D×2` i `D×0`, ważąc odwrotnością wariancji;
  - P2: `W(C×2)/W(D)`;
  - F3: `D×0` wobec `D×2`;
  - N1: `D×2` zamiast `D×10` (tolerancja `1e-4/1e-7`).
- **Co widziałem przed decyzją:** jedną wartość `C×10` przy `j = 22` (`Y_C = 0.25085` w `log10 β = −17.827`) oraz wyniki
  `base`, `A×2`, `B×2`, `C×2` dla `j = 22` i `28`. Żadnego wyniku dla pasma D.
- **Zmiany w kodzie:** skrypt analizy (`code/wuxu_band_kernel_analysis.py`) ma dodaną gałąź dla tego odstępstwa;
  definicje z preregu zostały bez zmian.

## PREREG_051 / REVIEW_052 — kontrfaktyk wzoru Y_P (8 XI 2026, po południu; czas zegara kontenera = CET)

| czas (CET) | przebieg | plik | uwagi |
|---|---|---|---|
| 14:08:30 | PREREG_051 i sterownik opublikowane (`102e9d2`) | — | sterownik wcześniej nieuruchamiany |
| 14:08:50 | pierwsze uruchomienie (`&` w poleceniu tła) | — | procesy osierocone i zabite po kilku sekundach, przed zapisaniem jakiegokolwiek wiersza (pliki CSV puste, usunięte razem z plikiem tymczasowym sterownika w klonie autorów); ten sam błąd uruchomienia co 8 XI rano |
| 14:09:07– | produkcja: 2 procesy (`a`: j = 22, 28; `b`: j = 34, 62 i skan j = 99), kalibracja SBBN w każdym procesie | `yp051/yp_a.csv`, `yp051/yp_b.csv` | tolerancja domyślna, kod autorów `d395183` bez zmian |
| 14:12:04– | PREREG_052 (`4281386`): `base22r`, `CD2_22`, `CD0_22` na zwolnionym rdzeniu | `kernel_cd052.csv` | sterownik `wuxu_band_kernel.jl` bez zmian; koniec 14:16:05 |
| 14:12:53 | PREREG_051 procesy `a`, `b` zakończone | `yp051/yp_a.csv`, `yp051/yp_b.csv` | 18 + 35 punktów |
| 14:13:03–14:14:25 | PREREG_051: siatka 9 punktów przy j = 99 wokół przejścia V0 ze skanu (−19.23) | `yp051/yp_c.csv`, `yp051/configs_c.dat` | zgodnie z preregiem (skan, potem siatka) |
| 14:16–14:17 | analizy końcowe | `yp051/yp051_analysis.json`, `cd052_analysis.json` | w analizie 051 dodana post hoc ocena szumu korzeni (rozrzut wokół krzywej 3. stopnia), oznaczona w kodzie i w REVIEW_053; główna metoda korzenia bez zmian; w skrypcie 052 poprawione serializowanie typu bool numpy (bez wpływu na liczby) |

## 11 XI 2026 — ścisły JSON (zgłoszenia Mech-S8 ROT010 i KN13 ROT008)

`data/kernel_analysis.json` zawiera cztery niestandardowe tokeny `Infinity` (`/configs/A2_*/hi_g`, górna granica pasma A). Plik oryginalny zostaje bez zmian (custody). Obok dodany ścisły odpowiednik `data/kernel_analysis.strict.json` (`Infinity → null` w czterech ścieżkach `/configs/A2_{22,28,34,62}/hi_g`), wygenerowany przez `code/json_strict_sibling.py`. Pozostałe pliki JSON w tym katalogu nie zawierają wartości nieskończonych.
