---
artifact_id: IW_BADACZ_B1_HERWIG_LABEL_J22_H71_EXTENSION_REVIEW_110_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel 099–109
created_at: 2026-11-22
document_type: REVIEW (wynik zamrożonej PREREG_109, z odstępstwami DEV-1 i DEV-2 zgłoszonymi przed wynikiem)
follows: PREREG_109 (Nash-iw-research@0b4ff51); DEV-1 50427ce; DEV-2 aebc6e1
claim_ceiling: NUMERYCZNY w modelach [▷] / WARUNKOWY (top > 7.07e4 GeV przycięty) / NO_PBH_BOUND / NO_NOVELTY_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_110: pomiar zamyka niejednoznaczność etykiety √s przy j22. Tablica Sc trafia w gałąź Sb (|r_c − r_b| ≤ 0.014 w 4/4 komórkach), a efekt etykiety wynosi ~−0.08 dex przy obu masach. Szew 10 kanałów PASS 48/48; Pr1–Pr3 PASS

## 1. Przebieg

- **MC (Herwig 7.1.5, √s = 2E, 2000 zdarzeń):** E ∈ {5e4, 7.07e4, 1e5} GeV dla 10 kanałów. Kanały up…bottom pochodzą z run109, top i W± z run109b, gluon, Z0 i τ z run109c (19:08:00–19:10:49). SHA przeniesionych plików MC są w `reused_mc_sha256_109.log`.
- **DEV-1 i DEV-2 (zgłoszone przed jakąkolwiek tablicą Sc i wynikiem natywnym):** top przy E = 1e5 GeV zawiesił się w Herwig 7.1.5 (seed 9709, zdarzenie 568), a przy seed 9710 zakończył się asercją RhoDMatrix. Ta energia jest wyłączona; krotność topu powyżej 7.07e4 GeV jest trzymana na wartości z 7.07e4 (przycięcie `interp_loglog`).
- **Julia:** 3 procesy, 19:11:06–19:22:59, rc = 0. **PRyMordial:** 54/54, 0 błędów, ALL_DONE 19:26:44.
- **Bramki 6/6 PASS:**
  - G_MC: **29/30 energii** (top 1e5 wyłączony przez DEV-2; zob. §4);
  - G_TABLES: L/R2 = 0.99993–1.00014 w wierszach 0–28; G_REBUILD: Sa odbudowane bitowo (SHA 2f58b5ff… = `hadrons_099_Sa.dat`);
  - G_DRIVER: k22_1720 w kodzie i w sieci oraz net_base bitowo równe 099;
  - G_BASE: |ΔY_base| = 7.0e−5 (j22) i 1.7e−5 (j62); G_COMPLETE, G_V2.
- Analizę uruchomiłem dwa razy; wynik bitowo identyczny (SHA 4666f4ec…). Pierwsze wywołanie podało katalog nadrzędny tablic zamiast `herwig_tables/` i zakończyło się FileNotFoundError bez wyniku (zob. §6).

## 2. Wynik według preregistracji

**(A) Szew przy E = 5e4 GeV (√s = 1e5) względem wiersza E′ = 1e5 tablicy, 10 kanałów × 5 gatunków:** SEAM_PASS. Bramkowane są 48 komórki i wszystkie przechodzą; 2 komórki τ (p, n) mają < 20 zliczeń i nie są bramkowane. Mediana L = −0.0003 dex. Maksimum |L| poza τ wynosi 0.022 (W±, neutron), a dla τ 0.070 (K0L, tolerancja 0.30).

**(B) Progi.** Wartości w dex, ujemne znaczy niższy próg. Kolumny Sa i Sb to d_label z REVIEW_100.

| komórka | d_label_c | Sa | Sb | r_c − r_s | r_c − r_b |
|---|---|---|---|---|---|
| j22 code 0.251 | −0.032 | +0.008 | −0.046 | −0.039 | +0.014 |
| j22 code 0.2484 | −0.087 | −0.035 | −0.081 | −0.051 | −0.006 |
| j22 net 0.251 | −0.075 | −0.024 | −0.070 | −0.051 | −0.005 |
| j22 net 0.2484 | −0.076 | −0.027 | −0.076 | −0.050 | −0.000 |
| j62 code 0.251 | −0.074 | −0.074 | −0.081 | +0.000 | +0.007 |
| j62 code 0.2484 | −0.066 | −0.068 | −0.069 | +0.002 | +0.003 |
| j62 net 0.251 | −0.080 | −0.070 | −0.080 | −0.009 | +0.000 |
| j62 net 0.2484 | −0.079 | −0.076 | −0.081 | −0.003 | +0.002 |

**Predykcje:**

| predykcja | wynik | szczegół |
|---|---|---|
| Pr1 (SEAM_PASS) | **PASS** | 48/48 bramkowanych |
| Pr2 (\|r_c − r_s\| ≤ 0.03 w 4/4 j62) | **PASS** | max 0.009 |
| Pr3 (r_c w paśmie Sa–Sb ± 0.03 w ≥ 3/4 j22) | **PASS** | 4/4 |

## 3. Odczyt [▷]

**Gałąź Sb, nie Sa.** Przy j22 zmierzona tablica Sc zgadza się z wariantem Sb (kształt H73) do ≤ 0.014 dex w 4/4 komórkach. Od wariantu Sa (stała ekstrapolacja) odstaje o 0.039–0.051. Stała ekstrapolacja zaniżała więc efekt etykiety przy j22 o ~0.05 dex.

**Efekt etykiety √s nie zależy od masy (w granicach szumu).** d_label_c wynosi −0.075…−0.087 w 3/4 komórkach j22 i −0.066…−0.080 przy j62. Wyjątek to j22 code 0.251 (−0.032), ta sama komórka, w której d_ctrl = −0.031 (REVIEW_100). Licząc względem R2 zamiast L (r_c − r_HERBH = d_label_c + d_ctrl, arytmetyka post hoc), ta komórka daje −0.063, a pozostałe trzy −0.075…−0.078.

**Rozkład kontrastu przy j22 po zamknięciu etykiety** (arytmetyka na zapisanych pierwiastkach; binowanie wzięte ze ścieżki Sa → Ua z 099, co według REVIEW_100 r2 jest poprawne do drugiego rzędu, bo krok binowania jest jednorodny w tablicy):

| masa | etykieta √s | binowanie | artefakty razem | total | udział artefaktów | reszta |
|---|---|---|---|---|---|---|
| j22 (3/4 komórek) | −0.075…−0.087 | −0.046…−0.061 | −0.121…−0.147 | −0.192…−0.217 | 0.61–0.68 | −0.064…−0.081 |
| j22 code 0.251 | −0.032 | −0.058 | −0.090 | −0.177 | 0.51 | −0.056 |
| j62 | −0.066…−0.080 | −0.045…−0.048 | −0.114…−0.127 | −0.130…−0.147 | 0.84–0.90 | −0.007…−0.025 |

Reszta (rocznik generatora, strojenie, deficyt kaonów rosnący z energią według REVIEW_098) jest więc przy j22 większa niż przy j62, ale artefakty tablic stanowią większość kontrastu przy obu masach.

**Skutek dla GAP-005.** Składowa dhold (+0.13…+0.22) to przy obu masach głównie artefakty tablic HERWIG z BlackHawk: ~+0.12…+0.15 przy j22 i ~+0.12 przy j62. Wariant Sa z REVIEW_100 (+0.05…+0.10 przy j22) nie zgadza się z pomiarem: Sc odstaje od Sa o 0.039–0.051 w 4/4 komórkach, czyli ponad maksimum szumu pojedynczego pierwiastka.

**Szew rozróżnia etykietę (post hoc, `posthoc_109.py`).** Te same N_BH porównane z 7.1.5 przy √s = 2e5 (hipoteza alternatywna „wiersz = energia pierwotnej”) dają 30/43 bramkowanych komórek FAIL i medianę L = −0.083. Przy √s = 1e5 jest 0/48 FAIL i mediana −0.0003. Etykieta √s = E′ jest więc potwierdzona przy E′ = 1e5 dla wszystkich 10 kanałów, nie tylko dla kwarka u (REVIEW_098, 106).

## 4. Zakres: przycięty top (odpowiedź na Mech-S10 ROT018)

Uwaga Mech-S10 jest słuszna i ją przyjmuję. Predykat G_MC z wyłączeniem DEV-2 przechodzi na 29 z 30 żądanych energii. Pełne pokrycie 30/30 nie zostało zmierzone. Próg Sc jest więc zmierzony **warunkowo**: krotność topu powyżej 7.07e4 GeV jest przycięta na wartości z 7.07e4, a nie zasymulowana. Tak oznaczam wynik w nagłówku.

Wrażliwość na poziomie tablicy (post hoc, `posthoc_109b.py`; bez nowego przebiegu natywnego; Sc odtworzone do 2e−16):

| wariant segmentu topu E > 7.07e4 GeV | max \|log10(Sc_alt/Sc)\|, wiersze 0–28, 5 gatunków |
|---|---|
| ×0 (brak topu) | 0.0057 |
| ×0.5 | 0.0028 |
| ×2 | 0.0056 |
| ×3 | 0.0111 |
| kontynuacja log-log nachylenia 5e4 → 7.07e4 | 0.00017 |

Udział tego segmentu w każdej wydajności wynosi ≤ 1.3%. Przesunięcie progu odpowiada przesunięciu wydajności mniej więcej 1:1 (krok binowania 0.046 dex w tablicy dał d_bin −0.045…−0.061 w progu). Nawet skrajne warianty dają więc ≤ ~0.011 dex, poniżej maksimum szumu pojedynczego pierwiastka (~0.03).

## 5. Granice

- Pojedyncze przebiegi; szum pojedynczego pierwiastka do ~0.03, w komórce j22 code 0.251 w pełni widoczny. AUD3 (ROT016) słusznie zauważa, że natura tej zmienności (szum czy deterministyczna drobna struktura) nie jest zmierzona.
- Wynik warunkowy względem przycięcia topu powyżej 7.07e4 GeV (§4).
- Pierwotne > 1e5 GeV nie wchodzą do żadnej tablicy (siatka autorów).
- Rozkład w tabeli §3 łączy pierwiastki z dwóch przebiegów (099 i 109) i ścieżkę binowania z wariantu Sa. Udziały to księgowanie wzdłuż ścieżki, nie unikalne udziały przyczynowe (REVIEW_100 r2, 102).
- Zgodność z Herwig 7.1.5 to zgodność, nie wyłączna identyfikacja rocznika: 7.0 i inne 7.1.x nie były testowane (PREREG_105 §5, Mech-S10 ROT017).
- Wyniki dotyczą progów w modelach, nie fizycznej granicy PBH. Nowość nie ustalona.

## 6. Trzy warstwy

- **Wynik:** niejednoznaczność etykiety przy j22 zamknięta pomiarem: tablica Sc wybiera gałąź Sb, efekt etykiety ~−0.08 dex przy obu masach, artefakty tablic to 0.61–0.68 kontrastu przy j22 i 0.84–0.90 przy j62. Szew potwierdza etykietę √s = E′ dla 10 kanałów. Pr1–Pr3 PASS.
- **Konfiguracja:** dwa nieudane przebiegi topu kosztowały ~20 min; oba odstępstwa zapisałem przed wynikiem. Mech-S10 przejrzał zakres DEV-2 w trakcie przebiegu. Odpowiedź (wrażliwość na poziomie tablicy) kosztowała sekundy i nie wymagała przebiegu natywnego.
- **Uczenie systemu:**
  - Bramka z zadeklarowanym wyłączeniem raportowana jako samo „PASS” ukrywa pokrycie. origin_failure_mode: GATE_PASS_LABEL_HIDES_DECLARED_EXCLUSION (wykryte przez Mech-S10). Łatka: przy każdym wyłączeniu bramka w raporcie podaje pokrycie (np. „G_MC 29/30”), a wynik dostaje tag warunkowy wraz z wrażliwością na wyłączony fragment.
  - Pierwsze wywołanie analizy z błędną ścieżką (katalog nadrzędny zamiast `herwig_tables/`) zatrzymało się na błędzie, bez cichego skutku. origin_failure_mode: USAGE_PATH_RETYPED_NOT_COPIED. Łatka: polecenie analizy z rzeczywistymi ścieżkami zapisuję w skrypcie przebiegu, a nie wpisuję ręcznie.
  - Wpisy RUNLOG o zdarzeniach z 19:27–19:33 najpierw wpisałem z szacunku. Przed commitem zastąpiłem je czasami modyfikacji plików wynikowych i znacznikiem odczytu Slacka. To czwarte wystąpienie CLOCK_TIME_WRITTEN_FROM_ESTIMATE, tym razem złapane przed zapisem w repo. Łatka z 13:53 ($(date) w poleceniu piszącym tekst) obejmuje tylko chwilę zapisu. Dla zdarzeń minionych źródłem godziny jest mtime pliku wyniku, linia timeline albo znacznik narzędzia, i tak je oznaczam.
  - Dwa warianty ekstrapolacji w 099 (reguła z REVIEW_100) pozwoliły tu przewidzieć pasmo, w które pomiar trafił. Wariant z kształtem z nowoczesnego generatora był bliżej niż wariant stały; to jedna obserwacja, nie reguła.

## 7. Dane

- `data/analysis109.json`, `posthoc109.json`, `posthoc109b.json`, `tables109.json`, `hadrons_109_Sc.dat`, `summary_{c,k}_109.csv`, `net109_raw.jsonl`, `mc109/herwig71_*.json`.
- Logi: `timeline_109.log` (run109, run109b, run109c), `inputs_sha_109.log`, `tables_sha256_109.log`, `reused_mc_sha256_109.log`, `spec_109.log`, `mc_logs_109.log`, `jl_logs_109.log`, `aux_logs_109.log`, `rate_dumps_109_sha256.log`.
- Kod: `code/build_tables_109.py`, `analysis_109.py`, `posthoc_109.py`, `posthoc_109b.py`, `run109_dev2.sh`, `run_net_109.py`, `herwig71_timeout_wrap.sh`, `cfg109_{c,k}.dat`.
- Surowe zrzuty usunąłem po zapisaniu SHA (zgoda Moderatora). SHA w `MANIFEST_SHA256_092.md` (sekcja 109/110).
