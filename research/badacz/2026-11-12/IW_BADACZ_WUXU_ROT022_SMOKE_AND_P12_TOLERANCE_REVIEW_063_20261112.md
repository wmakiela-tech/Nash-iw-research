---
artifact_id: IW_BADACZ_WUXU_ROT022_SMOKE_AND_P12_TOLERANCE_REVIEW_063_20261112
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude)
created_at: 2026-11-13
document_type: REVIEW
preregistration: IW_BADACZ_WUXU_ROT022_SMOKE_AND_P12_TOLERANCE_PREREG_062_20261112 (d2838c2, przed przebiegiem); skrypt analizy 69d987b (przed odczytem wyników)
responds_to: Mech-S8 ROT022 (prośba właściciela); Mech-S9 ROT001; Mech-S8 ROT019; INT9 ROT014; REC11 ROT021; LT8 ROT014
code: research/mech-s8/2026-11-12/mech_s8_rot022_C1_C4_calibrated_y2x_native_pilot_UNEXECUTED.jl (blob 0223f0c5, bez zmian); research/badacz/2026-11-08/code/wuxu_yp_formula_counterfactual.jl; research/badacz/2026-11-11/code/wuxu_subedge_ramp.jl; code/wuxu_062_analysis.py
data: data/ROT022_SMOKE_S1FAIL_STDERR_RECORD.md, data/rot022_smoke_points_D1_nocomments.dat, data/rot022_smoke_{native,p13,native_sym,p13_sym}.csv, data/xcheck062a.csv, data/p12_default062b.csv, data/analysis062.json, data/RUNLOG.md, data/MANIFEST_SHA256.md
claim_ceiling: MODEL_INTERNAL / SMOKE_AND_SELF_TEST / NO_ROOTS_FROM_SMOKE / NO_PBH_BOUND / NO_E4_UNBLOCK / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_063: smoke ROT022 — S1 FAIL na pliku punktów, po usunięciu komentarzy (D1) S2–S4 PASS; p12 przy tolerancji domyślnej — T1, T2 PASS

**Rola:** Badacz.

## Część A: smoke sterownika ROT022 (C1–C4)

- **S1, zgodnie z preregiem: FAIL** we wszystkich czterech wariantach, po ok. 2 s.
  - Bramka blobów autorów przeszła.
  - Linia 66 sterownika parsuje każdą niepustą linię pliku punktów jako `j log10beta`. Plik właściciela `phaseA_smoke_v001.dat` ma trzy linie komentarza `#`, stąd `ArgumentError: invalid base 10 digit '#'`.
  - Ani `magic()`, ani ODE nie zostały wywołane.
  - Dosłowne stderr: `data/ROT022_SMOKE_S1FAIL_STDERR_RECORD.md`.
  - To defekt interfejsu między dwoma plikami właściciela. Wystarczy pominąć linie zaczynające się od `#` w linii 66 albo usunąć komentarze z pliku.
- **Odstępstwo D1 (post hoc, poza preregiem).** Te same 4 punkty w pliku bez komentarzy, sterownik bez zmian. Wszystkie 4 warianty zakończyły się `DONE`, po 4 punkty każdy, w ok. 65 s na wariant.

| kryterium | wynik |
|---|---|
| S2: bramka SBBN sterownika (\|Y_P − 0.245\| ≤ 5e−5 przy β = 1e−30, j = 22) | PASS. C1 0.2449513, C2 0.2450188, C3 0.2450161, C4 0.2449956. C1 mieści się tylko o 1e−6 |
| S3: T1 w tym samym runtime | PASS, 0.099688851247 (identycznie jak REVIEW_053) |
| S4: \|Y_P(C1) − 2X_T1 (mój sterownik)\| ≤ 2e−4 | PASS: +7.1e−5, −3.9e−5 (j = 22); −9.7e−6, +4.5e−6 (j = 99) |

- **S2 i S4: skąd odchylenia.** Odchylenia mają rząd szarpania funkcji przy perturbacji wejścia (REVIEW_061: 3.2e−5 przy zmianie bitowej). β jest budowane inaczej: `ArbFloat(10)^ArbFloat(lb)` u Mech, `ArbFloat(10.0^lb)` u mnie.
  - Także przy β = 1e−30, gdzie PBH nie działa, C1 i C2 różnią się o 6.7e−5. To zmiana prawej strony ODE, która zmienia kroki solvera, a nie fizyka.
  - Próg 5e−5 w S2 jest więc tego samego rzędu co szum. Właścicielowi radzę go poszerzyć albo liczyć kalibrację tym samym wariantem i tą samą tolerancją co punkty.

**Opis (bez claimu, bez korzeni).** Różnice Y_P względem C1:

| punkt | C1 | C2 − C1 (p13) | C3 − C1 (B_sym) | C4 − C1 | interakcja (C4 − C3) − (C2 − C1) |
|---|---|---|---|---|---|
| j = 22, −17.15 | 0.250969 | +2.84e−4 | −1.73e−3 | −1.37e−3 | +7.5e−5 |
| j = 22, −16.95 | 0.251942 | +2.77e−4 | −1.41e−3 | −1.15e−3 | −1.8e−5 |
| j = 99, −19.10 | 0.248653 | 0 (dokładnie) | −1.82e−3 | −1.82e−3 | 0 |
| j = 99, −18.80 | 0.252282 | 0 (dokładnie) | −3.63e−3 | −3.63e−3 | 0 |

- **Kierunki zgodne z oczekiwaniem.**
  - p13 podnosi stopy poniżej 1e9 g, więc Y_P rośnie.
  - Przy j = 99 masa nie schodzi poniżej 1e9 g przed T1, więc p13 nie działa. Wynik jest bit w bit identyczny, co zgadza się z determinizmem z REVIEW_061.
  - B_sym obniża Y_P.
  - Interakcja przy j = 22 jest na poziomie szarpania.
- **Rząd wielkości.** Nachylenie C1 przy j = 22 między dwoma punktami wynosi ≈ 0.0049 na dex. Efekt p13 odpowiada więc rzędowo −0.06 dex korzenia, zgodnie z budżetem SYNTH_055 (−0.048). To szacunek z dwóch punktów, nie korzeń.
- **Odpowiedź właścicielowi (Mech-S8 ROT022, Mech-S9):**
  - Środowisko natywne v2 da się odtworzyć: Julia 1.12.3, rozwiązany `Manifest`, kod autorów zgodny z 13 blobami.
  - To nie jest historyczna budowa autorów, bo ich `Manifest` nie jest w repo.
  - Po poprawce parsera sterownik działa dla C1–C4. Decyzja o rozszerzonej fazie A należy do właściciela z Moderatorem.
  - Od 12 XI istnieje też natywny runtime GPT (Mech-S9 ROT005–008), który może to wykonać niezależnie ode mnie.

## Część B: p12 (REVIEW_061) przy tolerancji domyślnej

| j | Δ domyślna (SE dopasowania) | Δ przy `1e−4` (REVIEW_061) | różnica | T1 (≤ 0.010) | T2 (Δ < 0) |
|---|---|---|---|---|---|
| 22 | −0.0386 ± 0.0056 | −0.0362 | −0.0024 | PASS | PASS |
| 28 | −0.0300 ± 0.0018 | −0.0270 | −0.0031 | PASS | PASS |

- Zapas 0.010 dex przyjęty w PREREG_060 był wystarczający dla tej pary tolerancji. Luka wskazana przez Mech-S8 ROT019 i INT9 ROT014 jest zamknięta dla dwóch szczebli; `1e−5` nie było liczone.
- Rozrzut punktów przy tolerancji domyślnej wynosi 4.1–8.2e−5, wobec 2.8–6.5e−5 przy `1e−4`.

## Incydent: utrata pierwszych wyników kontroli krzyżowej i części B (12 XI)

- **Co się stało.** 12 XI o 11:12 zatwierdziłem commit z `git stash -u`, kiedy działały procesy zapisujące `xcheck062a.csv` i `p12_default062b.csv`.
  - `stash -u` przeniósł nieśledzone pliki, a procesy pisały dalej do usuniętych i-węzłów. Zakończyły się kodem 0 o 11:13:43 i 11:18:02, ale pliki zostały puste.
  - Wyniki D1 przetrwały, bo ich pliki powstały po tej operacji.
- **Naprawa.** Obie części powtórzyłem 13 XI o 07:49 bez zmian w konfiguracji.
  - Kod jest deterministyczny przy identycznym wejściu (REVIEW_061), więc to te same obliczenia.
  - Wartości wcześniejsze od powtórzenia nie istnieją, więc nie było z czym porównać.

## LT8 ROT014 (pytanie warunkowe)

**HOLD_NATIVE.** `magic()` zwraca tylko `(a, t, ρ_SM, m_PBH, n_PBH, X_n, Y_P)`. Gęstości logarytmiczne sześciu hadronów nie są zapisane w żadnym z moich przebiegów. Nie mogę więc stwierdzić, czy przekroczyły −100 po wyparowaniu, bez nowego, instrumentowanego przebiegu, a o taki LT8 wprost nie prosi.

## Powrót w trzech warstwach

- **Wynik:**
  - smoke ROT022: S1 FAIL (parser), po D1 S2–S4 PASS, kierunki C2–C4 sensowne;
  - p12: zapas tolerancji potwierdzony (różnice 0.002–0.003 dex).
- **Konfiguracja.** Sterownik napisany przez inną komórkę bez dostępu do Julii zawiódł na pierwszej linii wejścia. Taki 4-punktowy smoke kosztował 2 s i od razu to wykrył.
- **Uczenie systemu:**
  - `origin_failure_mode: GIT_STASH_UNTRACKED_DURING_ACTIVE_RUN` (moje). Łatka: w trakcie przebiegu żadnego `stash -u`; pliki wyjściowe od startu w lokalnym `exclude`; commit tylko jawnie wskazanych ścieżek.
  - `origin_failure_mode: INPUT_CONTRACT_UNTESTED_ACROSS_OWNER_FILES` (sterownik i plik punktów właściciela). Łatka: przed publikacją pliku konfiguracyjnego uruchomić sam parser.
  - `origin_failure_mode: GATE_THRESHOLD_AT_NOISE_LEVEL` (S2 5e−5 przy szarpaniu ~5e−5). Łatka: progi bramek kalibrować na zmierzonym szumie.
