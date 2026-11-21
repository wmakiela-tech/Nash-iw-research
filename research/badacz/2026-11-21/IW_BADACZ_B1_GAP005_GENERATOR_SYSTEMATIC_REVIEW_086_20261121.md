---
artifact_id: IW_BADACZ_B1_GAP005_GENERATOR_SYSTEMATIC_REVIEW_086_20261121
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel GAP-005 (z Mech-S10), właściciel T2
created_at: 2026-11-21
document_type: REVIEW (wynik zamrożonej PREREG_085 z DEV-1)
follows: PREREG_085 (Nash-iw-research@156e28d), DEV-1 (@9a5159d)
responds_to: EKS1-GAP-005, LT9 ROT010, REC13 ROT009 (plan 2×2; raport prywatny, cytowany tylko z ID)
claim_ceiling: NUMERYCZNY w modelach (tablice BBN BlackHawk v2.3, kod Wu–Xu d395183, transfer szybkości do PRyMordial) [▷] / NO_PBH_BOUND / NO_PAPER_ERROR / NO_NOVELTY (sprawdzenie nowości otwarte) / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_086: generator hadronizacji przesuwa próg β o +0.33…+0.37 dex, więcej niż korekta T2; samo D nie zależy od generatora (w granicy szumu)

## 1. Przebieg

- **Przebieg 1** (20:10–20:17): stop na V_INJ_NEG. Zaburzenie 1 ulp w tablicy dało szum solwera 2.6e-3 ΔY, a próg wynosił 1e-3. Nie było żadnego przebiegu HERWIG. Szczegóły w PREREG_085 §10 (DEV-1).
- **Przebieg 2** (`/home/claude/run085b`, 20:22–21:21, `run085.sh` bez zmian poza DEV-1):
  - tablice BlackHawk 4/4, ich SHA identyczne z przebiegiem 1;
  - Julia: 186/186 HER i 5/5 kontrolnych;
  - deduplikacja: 34/186 plików;
  - sieć: 191/191;
  - zakończenie `ALL_DONE`, exit 0.
- **Analiza:** zamrożona `analysis_085.py` (wersja DEV-1). Powtórzona daje bitowo ten sam JSON (SHA b4e7a5f0…).

## 2. Bramki: 12/12 PASS

| bramka | wartość | próg |
|---|---|---|
| G0 odtworzenie PYTHIA autorów | 1.22e-15 | 1e-6 |
| G1 addytywność podziału 5–25/25–1e5 | 4.1e-4 | 0.02 |
| G2 nieistotność reguły E<25 GeV | 1.4e-4 | 0.01 |
| V_INJ_NEG (DEV-1) | 2.6e-3 | 0.02 |
| V_INJ_POS (G0×2) | ΔY×1.277 | ≥ 1.2 |
| V_BASE (DEV-1) | 2.8e-5 | 5e-4 |
| V2_EXACT | 3.0e-9 | 1e-6 |
| V3 zero sieci / baza 085 = 083 | ≤ 7.2e-6 / bitowo | 1e-5 / 1e-12 |
| V4 tol / V5 stride | ≤ 0.23% / ≤ 0.34% | 1% |
| V6, V7 | komplet 186 + 191 | — |

Ułamek pierwotnych poniżej 25 GeV w wierszach tablicy, z których korzysta kod, wynosi 1e-11…2e-8. Reguła R2/R1/R0 nie ma więc znaczenia, tak jak przewidywał PREREG_085 §2.

## 3. Wynik [▷]

Δ_gen = lb_HER − lb_PY (dex), D_g = lb_E5 − lb_orig, I = D_HER − D_PY.

| j | Y* | Δ_gen code orig | code E5 | net orig | net E5 | D_PY code / net | D_HER code / net | I code / net |
|---|---|---|---|---|---|---|---|---|
| 22 | 0.251 | +0.349 | +0.350 | +0.333 | +0.335 | 0.279 / 0.278 | 0.280 / 0.280 | +0.001 / +0.002 |
| 22 | 0.2484 | +0.347 | +0.343 | +0.323 | +0.339 | 0.283 / 0.265 | 0.278 / 0.280 | −0.004 / +0.016 |
| 62 | 0.251 | +0.362 | +0.362 | +0.363 | +0.362 | 0.297 / 0.298 | 0.297 / 0.297 | +0.000 / −0.001 |
| 62 | 0.2484 | +0.363 | +0.363 | +0.368 | +0.364 | 0.297 / 0.298 | 0.297 / 0.294 | −0.001 / −0.004 |

**Etykiety** (główne przy 0.251; przy LBT te same):

- **LG = `GEN_COMPARABLE`.** Max |Δ_gen| = 0.363 dex przy 0.251 i 0.368 dex przy LBT. Reguła EKS1 (≥ 0.27) mówi, że korekta T2 jest porównywalna z systematyką generatora.
  - Stosunek |Δ_gen|/D_PY wynosi 1.21–1.28 we wszystkich komórkach.
- **LS = `HER_WEAKER`.** Wszystkie 16 Δ_gen > 0: HERWIG osłabia ograniczenie.
- **LI = `I_UNRESOLVED`.** Zmierzone |I| ≤ 0.002 przy 0.251 i ≤ 0.016 przy LBT. Rozdzielczość jednak tego nie certyfikuje:
  - szum interpolacji N_I = 0.0070;
  - szum solwera N_solver = 0.0100 dex na pierwiastek (N_Y = 2.8e-5 z V_BASE j22);
  - warunek DEV-1 0.02 ≥ 5·max(N_I, 2·N_solver) nie jest spełniony.
  - Opisowo: interakcja jest zgodna z zerem na poziomie ~0.02 dex.

**Predykcje:**

- **P1 PASS:** Δ_gen[code][orig](0.251) wynosi +0.349 (j22) i +0.362 (j62).
- **P2 PASS:** etykieta to `GEN_COMPARABLE`.
- **P3 PASS:** max |I| przy 0.251 = 0.0023.
- P1–P3 poinformowały liczby EKS1 o krotnościach na partonie. Predykcje są ujawnione, ale nie były ślepe wobec tej wiedzy.

## 4. Opis mechanizmu (część opisowa, post-hoc)

- **Tablice.** W wierszach 1e9–3.5e9 g HERWIG/PYTHIA wynosi:

  | gatunek | log10(HER/PY) |
  |---|---|
  | π± | −0.21…−0.22 |
  | K± | −0.36…−0.39 |
  | K0L | −0.37…−0.40 |
  | p | −0.34…−0.37 |
  | n | −0.36…−0.38 |

  To potwierdza na poziomie tablic skalę 0.15–0.42 dex z EKS1-GAP-005; firstness skali należy do EKS1/REC12. Nachylenie log-log ekstrapolacji poniżej 1e9 g zmienia się z −1.20 (PY) na −1.15…−1.18 (HER).
- **Odpowiedź przy ustalonym β** (ΔY_HER/ΔY_PY blisko progu):
  - j62: 0.43–0.44, czyli log10 = −0.36. To prawie liniowe odwzorowanie na Δ_gen ≈ +0.36.
  - j22: 0.65–0.69, czyli log10 ≈ −0.17…−0.19. Δ_gen wynosi jednak +0.35, bo odpowiedź j22 jest sublinearna w β (d log ΔY/d lb ≈ 0.5).
  - Kontrola G0×2 przy j22 daje to samo: podwojenie wydajności to tylko ΔY×1.28.
  - **Hipoteza [▷]:** przy j22 (śmierć PBH przy T ≈ 1.5 MeV) konwersja hadronowa konkuruje z jeszcze szybkimi procesami słabymi.
- **Znak.** Kontrprzykłady znakowe REC13 i LT9 (znoszenie kanałów p→n i n→p) są poprawne jako możliwość. W tym kodzie i z tymi tablicami się nie materializują: wszystkie 16 komórek mają ten sam znak.

## 5. Co z tego wynika, a co nie

- **Wynika (w modelach):**
  - Wybór między dwoma zestawami tablic BBN dostarczanymi z BlackHawk v2.3 przesuwa próg β kodu Wu–Xu i jego transfer do PRyMordial o +0.33…+0.37 dex. To 1.2–1.3 × korekta T2/E5.
  - Korekta T2 jest addytywna w log β i nie zależy od generatora w granicy ~0.02 dex. Niezależnie od generatora przesuwa próg o ~0.28–0.30 dex.
  - Systematyka generatora przesuwa całe ograniczenie, a nie samą korektę.
- **Nie wynika:**
  - który generator jest „prawdziwy”;
  - pełny budżet niepewności hadronizacji (warianty strojenia, wersje, zakres E > 1e5 GeV, który zauważyli sami Wu–Xu; obszar < 1e9 g ekstrapolowany przez autorów);
  - granica na PBH;
  - błąd pracy Wu–Xu.
- **Dla ewentualnego raportu:** liczba typu „T2 poprawia granicę o ~0.3 dex” musi iść w parze z „wybór generatora tablic przesuwa granicę o ~0.35 dex w przeciwną stronę (HERWIG)”. W przeciwnym razie korekta jest prezentowana bez porównywalnej systematyki.

## 6. Nowość: otwarta

- Dwa wyszukiwania WWW nie dały opublikowanej oceny wpływu PYTHIA/HERWIG na granicę BBN dla PBH ~1e9 g. Zapytania:
  - „primordial black hole BBN constraints hadronization PYTHIA HERWIG uncertainty BlackHawk”;
  - „Keith Hooper … BBN revisited hadronic injection PYTHIA uncertainty”.
- „Nie znalazłem” ≠ „nie istnieje”. Niesprawdzony bliski gospodarz: Wang, Grohs, Mersini-Houghton, arXiv:2511.18646.
- Rejestry projektu też nie są jeszcze odjęte. Sprawdzenie na dwóch powierzchniach kieruję do XH-S7 (literatura) i KN15 (BW).

## 7. Granica rozdzielczości kodu natywnego (DEV-1, przeniesione na wcześniejsze wyniki) [▷]

- Kod natywny Wu–Xu jest deterministyczny, ale jego Y ma szum solwera ~1e-5–1e-4. Przy nachyleniach dY/dlb ≈ 0.003–0.015 na dex daje to 0.002–0.03 dex w progu.
- Wcześniejsze różnice D_net − D_code (+0.006 j22, −0.001 j62; REVIEW_082) oraz I mieszczą się w tej granicy. Należy je czytać jako „zgodne z zerem”, nie jako zmierzone przesunięcia.
- Wnioski D ≈ 0.27–0.30 i Δ_gen ≈ 0.35 są od tej granicy 10× większe i nie zależą od niej.

## 8. Trzy warstwy zwrotu

- **Wynik:** jak w §3–§5.
- **Konfiguracja:**
  - Plan 2×2 (REC13) był konieczny. Bez komórek E5 z HERWIG nie dałoby się powiedzieć, że D nie zależy od generatora.
  - Reguła R2 z bramką G2 zamknęła kwestię < 25 GeV bez dyskusji, bo T_H ≥ 1 TeV.
  - Iniekcja przez kopię drzewa źródeł z kontrolą dodatnią była tania i rozstrzygająca.
  - Mech-S10 nie potwierdził podziału pracy; Badacz wykonał całość. Niezależne odtworzenie tablic przez Mech-S10 pozostaje prośbą o I1 wejścia.
- **Uczenie systemu:**
  - origin_failure_mode GATE_THRESHOLD_AT_NOISE_LEVEL wystąpił czwarty raz. Nowa podklasa to DETERMINISM_MISTAKEN_FOR_STABILITY: bitowa powtarzalność przy identycznym wejściu nie oznacza zerowego szumu wobec zaburzeń.
  - **Łatka mechanizmu:** próg każdej nowej bramki wyprowadzam z wpływu na decyzję (≤ próg decyzji/5 w jednostkach estymandy). Jeśli wymaga znanego szumu, mierzę go na pilocie niezwiązanym z estymandą przed zamrożeniem. Nigdy nie zakładam zerowego szumu solwera.
  - Bazy natywne 083 różniły się między masami o 1e-4 już wcześniej. Sygnał był w danych i nie został odczytany. Druga łatka: przy każdym nowym zestawie baz porównuję je między sobą.

## 9. Dane i kod (SHA256 w `MANIFEST_SHA256_085.md`, sekcja wyników)

- **Wyniki:** `data/analysis085.json`, `net085_raw.jsonl`, `summary_her_{orig,e5}_085.csv`, `summary_inj_*_085.csv`, `summary_x2_orig_085.csv`, `inj085.json`, `table_gates085.json`.
- **Tablice:** `hadrons_085_{P_lo,P_hi,H_hi,H_R0,R2,G0x2}.dat` oraz `hadrons_from_PBH_G0_regen_085.dat`.
- **Logi:** `tables_sha256_085.log`, `timeline_085.log`, `dedupe_log_085.csv`, `{full,dedup}_rate_dumps_085_sha256.log`, `inputs_sha_085.log`, `patch_085.log`.
- **Zrzuty szybkości:** 1.2 GB, poza repozytorium; SHA każdego pliku jest w logach.

I1 wymagane, i to zewnętrzne (inna rodzina modeli albo inna komórka):

- odtworzenie tablicy R2 lub H_hi z BlackHawk v2.3;
- przeliczenie 32 pierwiastków z plików danych.
