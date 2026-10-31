---
artifact_id: IW_BADACZ_WUXU_AUTHOR_NATIVE_AUDIT_PREREG_034_20261031
exposure: PUBLIC
claim_ceiling: PREREGISTRATION / TESTS_ONLY / NO_RESULT / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-31
origin_cell: BADACZ (wątek Claude)
document_type: PREREG
task_id: BADACZ-FRONTB-NATIVE-AUDIT-001
---

# Preregistracja: audyt natywnym kodem Wu–Xu (Fig. 5), przed pierwszym przebiegiem

## Kontekst (stan przed audytem)

- **Ścieżka wykonania.** Kod autorów (Fenyutanchan/Primordial-Black-Hole @ `d395183`) był już uruchamiany
  natywnie w GitHub Actions przez Mech-S6, 17–19 X, dla jednego punktu `(6e9 g, β = 1e-16)`. Ja uruchamiam
  go lokalnie: Julia 1.12.3 i pakiety przypięte jak w `research/mech-s6/2026-10-18/wuxu_dynamic_comparator/setup_env.jl`.
- **Kod autorów.**
  - `Yₚ = 2X/(1 − X)` przy `T_nuc = 0.078185270688319950 MeV`, skalibrowanym tak, że SBBN daje 0.245.
  - `χ² = ((Yₚ − 0.245)/0.003)²`; Fig. 5 to kontur `χ² = 4`.
  - `solve(…, AutoTsit5(Rosenbrock23()))` bez jawnych tolerancji (domyślnie `reltol = 1e-3`, `abstol = 1e-6`);
    `BITS = 100`.
- **Lewy brzeg konturu** (`m = 1.12–2·10⁹ g`) przypada tam, gdzie 50–89% masy PBH wypromieniowuje się
  poniżej krawędzi tabeli hadronów, czyli w reżimie ekstrapolacji.

## Punkty (ustalone teraz)

- **Masy:** 12 indeksów siatki autorów, `m = {1.121, 1.187, 1.256, 1.330, 1.448, 1.577, 1.767, 2.036,
  2.556, 3.494, 5.828, 7.743}·10⁹ g`.
- **`β`:** dla każdej masy 6 indeksów siatki, `k − 3 … k + 2`, gdzie `k` to pierwszy indeks z `χ² > 4`
  w zapisanym `scanning.jld2` (obcięte do zakresu siatki).
- **Wartości:** dokładnie te same ArbFloat (`geomspace` z `main-scan-parameters.jl`).
- **Kontrola:** dwa punkty poniżej tabeli (`m = 6.0e8` i `9.73e8 g`, `β = 1e-17`).

## Testy

- **N1 (kontrola):** kod SBBN autorów (notebook, komórki 6–7) daje `Yₚ,SBBN = 0.24500000000000022`
  z dokładnością `1e-12`.
- **N2 (odtwarzalność skanu):** `Yₚ` z natywnego `magic()` (bez zmian, `num_points = 10000`) wobec
  `Y_P_mat`.
  - PASS: `|ΔY|/Y < 1e-6` we wszystkich punktach;
  - INFO: `< 1e-4` (np. inne wersje zależności);
  - FAIL: większe.
- **N3 (rekalibracja):** `T′_nuc` takie, że `2·X_SBBN(T′_nuc) = 0.245`, z tą samą interpolacją co autorzy
  (liniowo w `Q/T`). Raportuję `T′_nuc`.
- **N4 (kontur po rekalibracji):** z tych samych trajektorii `Y_M = 2·X(T′_nuc)` oraz `Y_C`.
  - Granica `χ² = 4` w `log₁₀ β` dla każdej masy (liniowo między indeksami siatki); raportuję przesunięcie.
  - Test mojego surogatu z REVIEW_031, który przewiduje przesunięcie w stronę słabszego ograniczenia,
    medianę 0.10 i maksimum 0.15 dex.
  - **Falsyfikator surogatu:** przesunięcie `> 0.3 dex` w jakiejkolwiek masie albo przeciwny kierunek.
- **N5 (tolerancje solvera):** 3 punkty graniczne (`m = 1.256, 1.767, 3.494·10⁹ g`, indeks `k`) z
  `reltol = 1e-10`, `abstol = 1e-12` wobec domyślnych.
  - **Falsyfikator odporności numerycznej skanu:** `|ΔY| > 6e-4`, czyli 10% progu `0.006`.

Werdykt każdego testu ogłaszam niezależnie od kierunku. To audyt wyniku zewnętrznego, nie ocena
publikacji. Wynik jest Claude'a i wymaga audytu spoza rodziny Claude.
