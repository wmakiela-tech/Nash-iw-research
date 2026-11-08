---
artifact_id: IW_BADACZ_WUXU_YP_FORMULA_COUNTERFACTUAL_PREREG_051_20261108
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude)
created_at: 2026-11-08
document_type: PREREGISTRATION
responds_to: AUD1-ROT032-WUXU-FIG5-NOTEBOOK-YHE4-OWNER-DISPOSITION-001_20261108 (prośba do Mech-S8 jako właściciela, z udziałem Badacza, REC11 i MT14)
code: research/badacz/2026-11-08/code/wuxu_yp_formula_counterfactual.jl (commitowany razem z tym preregiem, przed przebiegami)
claim_ceiling: MODEL_INTERNAL_COUNTERFACTUAL / NO_PBH_BOUND / NO_FIG5_IDENTITY / NO_OWNER_DISPOSITION / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_051: o ile przesuwa się kontur Y_P w natywnym kodzie Wu–Xu po poprawieniu wzoru Y_P = 2X_n

**Rola:** Badacz. To pomiar wspierający dyspozycję właściciela (Mech-S8), a nie sama dyspozycja.

## Teza AUD1 i co już sprawdziłem w źródle

- **Wiersz 210 w `main-scan.jl`** (commit autorów `d395183`, v2) liczy `Y_P = 2X/(1−X)`.
- **Co przechowuje X.** W `magic()` zmienna X to ułamek neutronów `n/(n+p)`:
  - wartość początkowa `1/(1+exp(Q/T))`;
  - człon rozpadu `−X/τ_n`.
  Przy tej definicji poprawny ułamek masowy helu to `Y_P ≈ 2X`, tak jak w arXiv v3. Wyrażenie `2X/(1−X)` daje `2n/p`.
- **Kalibracja.** `T_nuc = 0.078185270688319950 MeV` ma 17 cyfr, więc wygląda na dobraną tak, by SBBN dawało `Y = 0.245` właśnie przy błędnym wzorze. Sprawdzi to kalibracja C1.

## Warianty (wszystkie z jednego, niezmienionego rozwiązania ODE)

Sterownik wywołuje `magic()` bez zmian, a z jej wyniku buduje tę samą interpolację `X(Q/T)` co autorzy.

- **V0 (natywny):** `Y_code = 2X(T0)/(1−X(T0))`, kontur `Y_code = 0.251`, gdzie `T0 = T_nuc`.
- **V1 (poprawiony wzór, ponowna kalibracja):** `T1` spełnia `2X_SBBN(T1) = 0.245`; kontur `2X(T1) = 0.251`.
- **V2 (poprawiony wzór, kryterium różnicowe przy stałym T0):** kontur `2X(T0) − 2X_SBBN(T0) = 0.006`.

V1 i V2 to dwie z możliwych korekt. Która jest właściwa fizycznie, rozstrzyga właściciel, nie ten test.

## Masy i siatka

- **Masy.** Indeksy z siatki autorów (0-based):
  - j = 22, 28, 34, 62 (1.121e9, 1.330e9, 1.577e9, 3.494e9 g; czas życia 0.33–10 s, czyli wybuch kończy się dużo przed T_nuc);
  - j = 99 (1e10 g; czas życia ≈ 238 s, porównywalny z czasem T_nuc) jako mierzenie **eksploracyjne**.
- **Siatka β.** Dla j = 22–62: `log10 β = r₀ + {−0.15, −0.075, …, +0.45}` (9 punktów), gdzie `r₀` to korzeń bazowy z REVIEW_050. Dla j = 99: skan od −21 do −17 co 0.25, potem siatka 9 punktów wokół przejścia V0.
- **Kalibracja SBBN.** `β = 1e−30` przy j = 22 i j = 62.
- **Korzenie.** Dopasowanie kwadratowe do 4 punktów otaczających przejście. Niepewność numeryczna = różnica względem interpolacji liniowej.

## Kontrole i przewidywania (zapisane przed przebiegami)

- **I0 (tożsamość):**
  - `2X(T0)/(1−X(T0))` z mojej interpolacji równa się wynikowi `magic()` z dokładnością względną ≤ 1e−12;
  - korzenie V0 zgadzają się z korzeniami bazowymi REVIEW_050 w granicach 0.01 dex (j = 22–62).
- **C1 (kalibracja):**
  - `Y_code,SBBN ∈ [0.244, 0.246]`;
  - `T1 > T0`;
  - SBBN takie samo przy j = 22 i 62 (`|ΔX0s| < 1e−6`).
- **P1 (skalowanie „tylko rozpad”).** Dotyczy tylko V1, j = 22–62.
  - Założenie: między T1 a T0 neutrony tylko się rozpadają (słabe konwersje zamrożone, wstrzykiwanie hadronów skończone). Wtedy `X(T1)/X(T0)` jest takie samo z PBH i bez, więc
    `X_T1(β) = X_T0(β)·X1s/X0s`.
  - Przewidywany korzeń V1p leży tam, gdzie natywne `X_T0(β) = 0.1255·X0s/X1s`, przy czym `X1s = 0.1225` z konstrukcji T1.
  - **PASS**, gdy `|root_V1 − root_V1p| ≤ 0.02 dex` dla wszystkich czterech mas.
- **P2 (wielkość przesunięć, przy nominalnym `X0s = 0.245/2.245`):**
  - V1: j = 22 w `[+0.08, +0.15]` dex, j = 28–62 w `[+0.03, +0.07]`;
  - V2: j = 22 w `[+0.20, +0.30]`, j = 28–62 w `[+0.07, +0.13]`.
  Uwaga uczciwości: V2 jest w pełni wyznaczony przez istniejące natywne punkty REVIEW_050, bo `X(T0) = Y/(2+Y)`. Wstępnie policzone stamtąd wartości to +0.252, +0.100, +0.091, +0.093. Okno V2 jest więc kontrolą numeryczną, nie przewidywaniem. Okno V1 korzysta z tych samych punktów przez P1.
- **E1 (j = 99, eksploracja):** bez okna. Oczekuję, że skalowanie P1 zawiedzie (`|root_V1 − root_V1p| > 0.02 dex`), bo wstrzykiwanie trwa jeszcze w okolicy T_nuc. Raportuję wynik takim, jaki wyjdzie.
- **Falsyfikatory:**
  - F1: P1 FAIL przy którejkolwiek masie z j = 22–62. Wtedy obraz „tylko rozpad między T1 a T0” jest fałszywy w kodzie natywnym.
  - F2: C1 FAIL. Wtedy przesłanka AUD1 o kalibracji do 0.245 nie zachodzi w moim środowisku.

## Granice

- Wynik będzie MODEL_INTERNAL, w kodzie v2 przy domyślnej tolerancji solvera, przy mapie B_exec autorów i z ich ekstrapolacją poniżej 1e9 g.
- Nie dotyczy tożsamości figury JCAP ani macierzy JLD2 autorów; tego nie mam.
- Nie daje fizycznej granicy PBH.
- Systematyki z wcześniejszych prac nie sumuję z wynikiem: B_sym +0.27…+0.30 dex, tolerancja solvera +0.01…+0.03 dex.

## Środowisko

- Julia 1.12.3, kod autorów `d395183`, 2 procesy.
- Przed commitem tego preregu sterownik nie był uruchamiany. Poprawki błędów mechaniki po uruchomieniu (bez zmiany definicji) zapiszę w RUNLOG jako odstępstwa.
