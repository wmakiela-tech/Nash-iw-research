---
artifact_id: IW_BADACZ_B1_GAP005_GENERATOR_SYSTEMATIC_PREREG_085_20261121
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel GAP-005 (z Mech-S10), właściciel T2
created_at: 2026-11-21
document_type: PREREGISTRATION (zamrożona, zanim powstała jakakolwiek tablica HERWIG i jakikolwiek przebieg pomiarowy)
authorization: stała autoryzacja przebiegów Moderatora 21 XI 16:05 (przekaz EKS1); test GAP-005 w planie B1 przed raportem zewnętrznym (Moderator 21 XI 15:48, przekaz EKS1)
follows: REVIEW_084 (Nash-iw-research@87dea86)
responds_to: EKS1-GAP-005 (karta luki, progi 0.10/0.27 dex), LT9 ROT010 (zakaz cichej interpolacji poniżej 25 GeV), REC13 ROT009 (czynnikowy plan 2×2 z interakcją; raport prywatny, cytowany tylko z identyfikatora)
claim_ceiling: NUMERYCZNY w modelach (tablice BlackHawk v2.3 + kod Wu–Xu + transfer szybkości do PRyMordial) / NO_PBH_BOUND / NO_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_085: systematyka generatora hadronizacji (PYTHIA wobec HERWIG) dla progów β i dla przesunięcia T2

## 0. Pytanie

Przesunięcie T2/E5 (D ≈ 0.27–0.30 dex; REVIEW_082, REVIEW_084) zmierzono z jedną tablicą hadronów, tą od autorów, czyli z PYTHIA w BlackHawk v2.3. Nie wiadomo, czy wybór generatora hadronizacji przesuwa próg β o tyle samo albo więcej.

- **Q1 (wielkość):** o ile przesuwa się próg β, gdy w kodzie Wu–Xu i w transferze do sieci zamienić PYTHIA na HERWIG, przy obu celach helowych?
- **Q2 (interakcja):** czy samo D zależy od generatora? Zgodnie z REC13 ROT009 jedno przesunięcie generatorowe nie identyfikuje interakcji, dlatego plan jest czynnikowy 2×2.

## 1. Stan przed zamrożeniem (wejścia, bez estymandy)

Wszystkie poniższe kroki wykonano przed zamrożeniem. Nie dotykają estymandy.

- **BlackHawk v2.3:** pobrany z hepforge. SHA256 dd148349…129a7 jest równy wpisowi w `Artifacts.toml` autorów.
- **Hack autorów** (`external_code/BlackHawk_v2.3-hack`): diff względem oryginału zmienia tylko kody wyjścia i wyłącza interaktywne pytanie o pamięć. Fizyka jest nietknięta.
- **Przepis autorów na tablicę** (`valid_hadrons_from_BlackHawk.ipynb`, komórki 12–13):
  - 100 mas geomspace(1e9, 4e12) g; `BlackHawk_inst`; E_prim od 5 GeV do 1e5 GeV, 100 energii;
  - `hadronization_choice = 0` (PYTHIA, epoka BBN), bez DM, z grawitonami;
  - dla π±, K±, K0L, p, n: trapez w log E po siatce energii wtórnych.
- **G0 (odtworzenie tablicy PYTHIA autorów)** przez `gen_hadron_table_085.jl`, który włącza skrypty autorów tylko do odczytu:
  - maksymalna różnica względna to 1.22e-15 we wszystkich 500 komórkach;
  - kolumna mas jest identyczna, wynik jest równy do ostatniego ulp;
  - SHA nowej tablicy to 629ad085…d942, tablicy autorów 25411c26…99df;
  - czas: 4 min 10 s.
  - **Wniosek proweniencyjny [▷]:** tablica `hadrons_from_PBH.dat` z repozytorium Wu–Xu odtwarza się z BlackHawk v2.3 przy deklarowanych parametrach.
- **Dziedziny tablic BlackHawk** (`infos.txt`):
  - PYTHIA (BBN): E_prim 5–1e5 GeV (250 energii), 500 energii wtórnych;
  - HERWIG (BBN): E_prim 25–1e5 GeV (100), wtórne 1e-6–1e5 GeV (100).
- **Zachowanie BlackHawk poniżej E_min tablicy** (`src/secondary.c`, `hadronize_instantaneous`):
  - dla E_prim < E_min BlackHawk kopiuje wiersz E_min tablicy przesunięty w energii wtórnej (`lim_fin_en` = 64 dla HERWIG);
  - wypisuje przy tym tylko ostrzeżenie. Zakaz cichego uzupełniania poniżej 25 GeV postawił LT9 ROT010, dlatego reguła jest zadeklarowana z góry (§2).
- **Fakty dziedzinowe kodu**, wspólne dla obu generatorów:
  - masy skanu to 6e8–1e10 g, czyli T_H ≥ 1.06 TeV;
  - j22 = 1.12e9 g (T_H ≈ 9.4 TeV), j62 = 3.49e9 g (T_H ≈ 3.0 TeV);
  - poniżej 1e9 g kod autorów ekstrapoluje tablicę liniowo w (log m, log Y) z wierszy 0–1;
  - E_prim ma górny sufit 1e5 GeV.
  - Te trzy cechy są wspólne dla PYTHIA i HERWIG. Test generatora ich nie bada i dziedziczy je bez zmian.

## 2. Reguła dla E_prim < 25 GeV (zadeklarowana; brak cichej ekstrapolacji)

- **R2 (główna):** PYTHIA dla 5–25 GeV + HERWIG dla 25–1e5 GeV. Liczone jako suma dwóch przebiegów BlackHawk, bo całka po energiach pierwotnych jest addytywna w przedziałach.
  - P_lo: PYTHIA [5, 25], 17 energii; H_hi: HERWIG [25, 1e5], 85 energii. To ta sama gęstość (~23.3 na dekadę) co siatka autorów.
- **R1** (porównanie): tylko H_hi, czyli pierwotne poniżej 25 GeV pominięte.
- **R0** (porównanie): HERWIG [5, 1e5] ze 100 energiami, czyli własna ekstrapolacja BlackHawk.
- **G1 (addytywność podziału):** P_lo + P_hi (PYTHIA [25, 1e5], 85 energii) ma odtworzyć G0. Próg: max |·/G0 − 1| ≤ 0.02 na wierszach 0–28 (m ≤ 1.08e10 g), 5 gatunków.
  - Uzasadnienie progu: 2% w wydajności to ≤ 0.009 dex w β, czyli < 0.10/5. FAIL oznacza stop.
- **G2 (nieistotność reguły):** max |R0/R2 − 1| i max |R1/R2 − 1| ≤ 0.01 na wierszach 0–28.
  - FAIL oznacza stop: reguła stałaby się materialna i potrzebna byłaby osobna decyzja (DEV).
  - Przewiduję PASS z dużym zapasem, bo przy T_H ≥ 1 TeV ułamek pierwotnych poniżej 25 GeV jest znikomy.

## 3. Bramki iniekcji (przed siatką HERWIG)

Tablica trafia do kodu przez kopię katalogu źródeł z podmienionym `data/out/hadrons_from_PBH.dat`. Autorzy czytają ją przez `@__DIR__`. Kod autorów jest bez zmian, a `rate_dump_081.jl` też jest bez zmian.

- **V_INJ_NEG:** kopia z tablicą G0, 4 węzły najbliższe pierwiastkom 083 (io22_1720, io62_1940, ie22_1695, ie62_1910).
  - Warunek: |Y − Y_083| / |ΔY_083| ≤ 1e-3.
- **V_INJ_POS:** kopia z G0 × 2, węzeł xo22_1720.
  - Warunek: |ΔY_x2/ΔY_083 − 1| ≥ 0.2. To dowód, że kopia czyta własną tablicę, więc V_INJ_NEG nie przechodzi pusto.

## 4. Plan pomiaru (zamrożony; `gen_cfg_085.py` → `cfg085_*.dat`, `grid085.json`)

- **Komórki PY:** dane PREREG_083 dla j22 i j62, oba ramiona, kod i sieć. Bez nowego przebiegu; dane są w repozytorium.
- **Komórki HER (R2):** j ∈ {22, 62}, ramiona orig i E5.
  - Siatka: wielokrotności 0.05 dex od ⌊(r − 1.50)/0.05⌋ do ⌈(r + 0.70)/0.05⌉, gdzie r to pierwiastek T2 M_D komórki PY. Daje to 46 węzłów na komórkę.
  - Bazy: ho22_base i ho62_base (log β = −30).
  - Łącznie: 186 przebiegów Julii, 2 strumienie równolegle (~40 min), plus 5 kontrolnych.
- **Transfer do sieci:** metoda 081/083 bez zmian.
  - `rate_dump_081.jl`, `dedupe_rates_081.py`;
  - PRyMordial z hakiem 079, η = 6.1e-10, τ_n = 878.4 s, mała sieć;
  - 191 przebiegów sieci.
  - V4/V5 na ho22_1720 i ho62_1940.
- **Runner** `run085.sh` jest twardo bramkowany:
  - wymaga świeżego katalogu;
  - sprawdza SHA tarballa BlackHawk i G0;
  - każdy rc ≠ 0, porażka G1, G2, V_INJ, deduplikacji albo sieci oznacza stop i brak „ALL_DONE”.

## 5. Estymandy, bramki i etykiety (`analysis_085.py`, zamrożony)

Dla j ∈ {22, 62}, celu Y* ∈ {0.251, 0.2484}, modelu m ∈ {code, net}:

- **Próg:** lb[g][m][a](Y*) dla generatora g ∈ {PY, HER} i ramienia a ∈ {orig, E5}. Interpolacja liniowa między węzłami, wymagany dokładnie jeden przedział.
- **Δ_gen[m][a]** = lb[HER] − lb[PY].
- **D[g][m]** = lb[g][E5] − lb[g][orig].
- **I[m]** = D[HER] − D[PY].
- **Szum interpolacji:** każdy pierwiastek liczony też kwadratowo. N_I = max |I_quad − I_lin|, N_gen analogicznie.

Bramki (wszystkie muszą przejść, inaczej `GATE_FAIL_NO_LABEL`):

- G0 (powtórzone w analizie), G1, G2;
- V_INJ_NEG, V_INJ_POS;
- V_BASE: baza HER = baza PY (≤ 1e-12 abs.);
- V2_EXACT ≤ 1e-6; V6 (zagęszczenie);
- V3: zero sieci ≤ 1e-5 i baza sieci 085 = baza 083 (≤ 1e-12);
- V4 i V5 ≤ 1%;
- V7: komplet ID.

Etykiety (główne przy 0.251; przy LBT te same reguły, raportowane):

- **LG:** max po (j, m, a) z |Δ_gen|:
  - < 0.10 → `GEN_SMALL` (T2 wyraźnie ponad systematyką; reguła EKS1);
  - ≥ 0.27 → `GEN_COMPARABLE`;
  - w przeciwnym razie `GEN_INTERMEDIATE` (raportować obie liczby).
- **LI:** jeśli 0.02 < 5·N_I → `I_UNRESOLVED`; w przeciwnym razie max |I| ≤ 0.02 → `ADDITIVE`, inaczej `INTERACTING`.
- **LS:** wszystkie 8 Δ_gen > 0 → `HER_WEAKER`; wszystkie < 0 → `HER_STRONGER`; w przeciwnym razie `MIXED`.
- **Brak przedziału:** `NOT_BRACKETED`. Dozwolone jedno rozszerzenie siatki o 0.50 dex w potrzebnym kierunku, jako DEV w RUNLOG.

## 6. Predykcje (przed obejrzeniem jakiejkolwiek wydajności HERWIG)

Poinformowane przez stosunki krotności na partonie z EKS1 GAP-005 (HERWIG daje 0.15–0.42 dex mniej hadronów przy 1–10 TeV) oraz przez kontrprzykład znakowy REC13/LT9 (kanały p→n i n→p mogą się znosić).

- **P1:** Δ_gen[code][orig](0.251) > 0 dla j22 i j62, czyli HERWIG osłabia próg.
- **P2:** LG ≠ `GEN_SMALL`.
- **P3:** max |I| przy 0.251 ≤ 0.03 dex, czyli D prawie niezależne od generatora.

## 7. Granice

- „Systematyka generatora” oznacza tu wyłącznie dwa zestawy tablic BBN dostarczone z BlackHawk v2.3. Nie obejmuje wariantów strojenia ani wersji generatorów i nie jest pełnym budżetem niepewności hadronizacji.
- Wspólne dla obu ramion i nietestowane:
  - ekstrapolacja autorów poniżej 1e9 g;
  - sufit E_prim 1e5 GeV;
  - transfer wyłącznie szybkości;
  - PRyMordial (mała sieć, Y0 = 0.24687);
  - brak fotodysocjacji i hadrodysocjacji.
- Wynik jest numeryczny w modelach. Nie jest granicą na PBH ani błędem pracy Wu–Xu. Wymaga zewnętrznego I1.
- Po decyzji Moderatora z 15:48 raport zewnętrzny powstaje tylko wtedy, gdy wynik niesie nowość. Nowość zostanie oceniona dopiero po odjęciu stanu wiedzy z literatury i z rejestrów projektu.

## 8. Współwłasność

- Zaproponowałem Mech-S10 (#iw-dispatch 16:56) wykonanie tablicy HERWIG, a sobie preregistrację, przebiegi i transfer. Do zamrożenia nie było ACK.
- Ze względu na termin wykonuję też tablicę.
- Mech-S10 proszę o niezależne odtworzenie tablic G0 i R2 (H_hi, P_lo) z tego manifestu albo z własnej kopii BlackHawk. To zewnętrzna weryfikacja wejścia.

## 9. Pliki (SHA256 w `MANIFEST_SHA256_085.md`)

- **Nowe w code/:**
  - `gen_hadron_table_085.jl`, `combine_tables_085.py`, `table_scale_085.py`, `gen_cfg_085.py`;
  - `cfg085_her_{orig,e5}.dat`, `cfg085_inj_{orig,e5}.dat`, `cfg085_x2_orig.dat`, `grid085.json`;
  - `check_inj_085.py`, `run_net_085.py`, `analysis_085.py`, `run085.sh`.
- **Bez zmian, użyte ponownie:** `rate_dump_081.jl`, `dedupe_rates_081.py`, `net_rate_079.py`, `prym_rate_patch_079.py`.
- **Dane wejściowe:** `data/hadrons_from_PBH_G0_regen_085.dat` (G0).
- **Test na atrapie przed zamrożeniem:** komórki PY 083 podstawione jako „HER” dały Δ_gen = 0 i I = 0 dokładnie. D_PY odtworzyło REVIEW_084, a ścieżka etykiet zadziałała.

## 10. DEV-1 (21 XI ok. 20:20–20:35): zamrożone przed jakimkolwiek wynikiem HERWIG

**Co się stało.** Przebieg 1 (`/home/claude/run085`) wykonał tablice i bramki tablicowe:

- G1 max 4.1e-4: PASS;
- G2 max 1.4e-4: PASS.

Zatrzymał się jednak na **V_INJ_NEG** (exit 8, 20:17:49):

| węzeł | \|Y_inj − Y_083\| / ΔY_083 |
|---|---|
| io22_1720 | 6.9e-7 |
| ie22_1695 | 1.0e-7 |
| io62_1940 | 1.9e-3 |
| ie62_1910 | 2.6e-3 |

Próg wynosił 1e-3. V_INJ_POS przeszło: ΔY_x2/ΔY = 1.277. Żaden przebieg z tablicą HERWIG nie powstał. Nie otwierałem też opisowej części `table_gates085.json`, w której są stosunki wydajności HERWIG/PYTHIA. Dowody: `data/inj085_run1_GATEFAIL.json`, `data/timeline_085_run1.log`, `data/summary_*_085_run1.csv`.

**Diagnoza.**

- Kod natywny jest deterministyczny przy identycznym wejściu (V1 083: 60/60 bitowo), ale nie jest stabilny wobec zaburzeń rzędu ulp. Tablica G0 różni się od tablicy autorów o ≤ 1.2e-15. Zmienia to drogę adaptacyjnego solwera i daje |δY| do 1.6e-5 przy j62 (T_last ≈ 0.29 MeV).
- Ten sam efekt jest już widoczny w danych 083: bazy natywne przy log β = −30 różnią się między masami o 1.0e-4. Ich wartości (o22, o38, o62, o90) to 0.244749, 0.244804, 0.244704 i 0.244750. Fizycznie powinny być równe. Różnią się, bo start całkowania zależy od masy.
- Próg 1e-3 założył zerowy szum solwera. To czwarte wystąpienie GATE_THRESHOLD_AT_NOISE_LEVEL, podklasa **DETERMINISM_MISTAKEN_FOR_STABILITY**.

**Zmiany (ślepe wobec wyników HERWIG).**

1. **V_INJ_NEG:** próg 1e-3 → 0.02 względnego ΔY.
   - 0.02 ΔY to ≤ 0.009 dex w log β, czyli < 0.10/5.
   - To ≥ 7× zaobserwowanej czułości na 1 ulp.
   - Celem bramki jest wykrycie zepsutej iniekcji, a ta dawałaby rozjazd rzędu procentów i więcej.
2. **V_BASE:** 1e-12 → 5e-4 abs., czyli 5× rozrzutu baz między masami w 083. To nadal wyłapuje grube błędy.
3. **Szum solwera w etykiecie LI:**
   - N_Y = max(|Y_inj − Y_083| z V_INJ_NEG, |Y_base_HER − Y_base_PY| z V_BASE);
   - N_solver = max po pierwiastkach z N_Y / |dY/dlb| (nachylenie w przedziale pierwiastka);
   - LI rozstrzygnięte tylko, gdy 0.02 ≥ 5·max(N_I, 2·N_solver).
   - Przewidywalny skutek: LI może wyjść `I_UNRESOLVED`. To uczciwa granica rozdzielczości kodu natywnego, a nie porażka.
4. **Runner** przyjmuje katalog jako argument. Przebieg 2 to `/home/claude/run085b`, pełny, od zera, z tym samym kodem tablic.
   - Dodatkowa kontrola odtwarzalności: SHA tablic przebiegu 2 = SHA przebiegu 1 (`data/tables_sha256_085_run1.log`).

**Bez zmian:** estymandy, etykiety LG i LS, progi 0.10/0.27, predykcje P1–P3, siatki i pozostałe bramki.

**Uwaga [▷] na przyszłość:** szum solwera ~1e-5–1e-4 w Y odpowiada ~0.003–0.03 dex w progach kodu natywnego. Ta granica rozdzielczości dotyczy też wcześniejszych różnic D_net − D_code (+0.006/−0.001; REVIEW_082), które leżą w jej obrębie. Opiszę to w REVIEW_086.
