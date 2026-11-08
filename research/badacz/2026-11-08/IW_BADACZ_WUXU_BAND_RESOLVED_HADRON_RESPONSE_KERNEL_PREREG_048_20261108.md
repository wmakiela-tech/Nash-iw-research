---
artifact_id: IW_BADACZ_WUXU_BAND_RESOLVED_HADRON_RESPONSE_KERNEL_PREREG_048_20261108
exposure: PUBLIC
claim_ceiling: PREREGISTRATION / TESTS_ONLY / NO_RESULT / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-08
origin_cell: BADACZ (wątek Claude)
document_type: PREREG
task_id: BADACZ-FRONTB-TIME-KERNEL-001
code: research/badacz/2026-11-08/code/wuxu_band_kernel.jl; wuxu_band_number_shares.py
context: Mech-S8 ROT002/005/006; MT14 ROT025; INT9 ROT001; Badacz REVIEW_038/042, nota z 2 XI 20:51
---

# Preregistracja: jądro odpowiedzi granicy χ² = 4 na wstrzykiwanie hadronów, rozdzielone na pasma masy PBH

## Po co

- **Stan wiedzy.** Mech-S8 ROT006 i moja nota z 2 XI ważyły hadrony spod krawędzi tabeli liczbą. INT9 ROT001,
  MT14 ROT025 i sam Mech-S8 ROT006 zastrzegają, że bez czasowej odpowiedzi n/p nie wolno przenosić liczby na `Y_P`.
  Mech-S8 ROT005/006 nazywa tę odpowiedź priorytetem właściciela i odradza kolejne globalne skany ×0/×2.
- **Ten pomiar nie jest globalnym skanem.** Mierzy jądro odpowiedzi natywnego układu n/p na wstrzykiwanie hadronów
  w funkcji chwilowej masy PBH, czyli czasu emisji.
  - Mnożnik dotyczy tylko tempa pięciu kanałów hadronowych w jednym paśmie masy.
  - Zegar masy (`N_BH`) i wstrzykiwanie energii zostają nietknięte.
- **Zysk wiedzy:**
  - Jądro przelicza każdą przyszłą, źródłowo zwalidowaną poprawkę tempa w paśmie na przesunięcie konturu bez nowych
    przebiegów.
  - Rozstrzyga, czy walidacja źródła dla lewej ściany musi sięgać `T_H ≥ 100 TeV` (bramka B Mech-S8).
  - Sprawdza, czy ważenie liczbą wolno stosować przy konturze.
- **Obserwacja post hoc z istniejących danych** (nie z preregu; REVIEW_038 wariant `zero`, REVIEW_042 wariant `p13`):
  - przy `τ ≲ 0.6 s` ważenie liczbą zaniża zmierzony efekt 3–6 razy (`zero`) i 2–3 razy (`p13`);
  - przy `τ ≳ 10 s` stosunek wynosi `≈ 1`.
  To motywuje przewidywania poniżej. Moja rekomendacja z 2 XI („1e8 g mniej pilne niż 3e8 i 1e9 g”) opierała się
  na ważeniu liczbą i jest zawieszona do wyniku.

## Procedura

- **Kod:**
  - Autorzy: `d395183`, `main-scan.jl` / `magic()`, domyślne tolerancje solvera, mapa `B_exec`, natywna ekstrapolacja
    log-liniowa poniżej `1e9 g`.
  - Mój sterownik: `code/wuxu_band_kernel.jl`. Mnoży tempa `dN_over_dt_{π,K,K⁰ᴸ,p,n}` przez `k`, gdy chwilowa masa
    PBH leży w `[lo, hi)`.
- **Kontrola tożsamości** (przed preregiem, wykonana): `k = 1` daje `Y_C` identyczne bitowo z `grid_native.csv`
  z 2 XI w dwóch punktach (`j = 22`).
- **Pasma** chwilowej masy:
  - `A = [1e9 g, ∞)` (tabela);
  - `B = [3e8, 1e9)`;
  - `C = [M_grid, 3e8)`;
  - `D = [0, M_grid)`, gdzie `M_grid = 1.05726e8 g` (`T_H = 100 TeV`, MT14 ROT025 / Mech-S8 ROT002).
- **Masy początkowe:**
  - `j = 22, 28, 34` (`τ = 0.335; 0.559; 0.932 s`, lewa ściana);
  - `j = 62` (`τ = 10.1 s`, kontrola).
- **Konfiguracje** dla każdej masy:
  - `base` (bez zmian);
  - `A×2`, `B×2`, `C×2`, `C×10`, `D×2`, `D×10`, `D×0`.
- **Granica:**
  - przedział startowy wokół granicy natywnej z REVIEW_038, rozszerzany w razie potrzeby;
  - bisekcja do `≤ 0.02 dex`;
  - dopasowanie liniowe `Y_C` na 7 punktach `r ± {0, 0.03, 0.06, 0.09}`;
  - pierwiastek przy `Y_C = 0.251`.
- **Wielkości:**
  - `Δ = root(konfiguracja) − root(base)`;
  - udział efektu `s_eff = (10^(−Δ) − 1)/(k − 1)`;
  - waga czasowa `W = s_eff / s_num`, gdzie `s_num` to udział liczby hadronów w paśmie
    (`code/wuxu_band_number_shares.py`, `data/band_number_shares.json`).
  - Przy `j = 22` `s_num` wynosi `A 0.186`, `B 0.721`, `C 0.079`, `D 0.0143`.
- **Kontrola numeryczna N1:** `base` i `D×10` przy `j = 22` dla `reltol/abstol = 1e-4/1e-7`.

## Założenie A1

`Y_C` zależy od `(β, k)` tylko przez iloczyn `β·E(k)`, gdzie `E` jest liniowym funkcjonałem wstrzykiwania hadronów.
Wtedy kontur spełnia `β·E = const` niezależnie od nieliniowości `Y_C(β·E)`. Wkład niehadronowy (gęstość energii PBH)
pomijam: po wyzerowaniu hadronów spod krawędzi przy `j = 22` ściany brak aż do `β = 1e-15` (REVIEW_038). A1 testują
P0, reguła sumy i F3.

## Przewidywania

- **P0** (spójność z wariantem `zero` z REVIEW_038 przy A1): `s_eff(A) = 10^(−Δ_zero)`, więc:
  - `Δ(A×2)` przy `j = 22` w `[−0.015, +0.005]`;
  - przy `j = 28` w `[−0.015, +0.005]`;
  - przy `j = 34` `−0.098 ± 0.03`;
  - przy `j = 62` `−0.274 ± 0.03`.
- **Reguła sumy:** `s_eff(B) + s_eff(C) + s_eff(D) = 1 − s_eff(A)` (z `k = 2`) z dokładnością `±0.1`.
- **P1** (późne hadrony ważą więcej): `W(D) ≥ 1.5` przy `j = 22` i `28` (z `D×10`).
- **P2** (C i D są emitowane w ostatnich milisekundach): `W(C)/W(D) ∈ [0.8, 1.25]` przy `j = 22` i `28`.
- **P3** (kontrola): przy `j = 62` `W(A)` i `W(B)` w `[0.7, 1.4]`.
- **P4** (bramka B): `s_eff(D)` przy `j = 22` i `28` w `[0.02, 0.10]`. Ważenie liczbą daje `0.014` i `0.010`.

## Falsyfikatory

- **F1:** `W(D) < 1` (ponad 2σ) przy `j = 22` lub `28`. Hipoteza późnego ważenia jest wtedy fałszywa dla pasma D.
- **F2:**
  - odchylenie `Δ(A×2)` od P0 o ponad `0.03 dex` przy dowolnej masie, albo
  - naruszenie reguły sumy o ponad `0.1`.
  A1 upada, a opis jądrem liniowym jest nieważny; raportuję nieliniowość.
- **F3:** `s_eff(D)` z `k = 0` i z `k = 10` różnią się o więcej niż `max(0.5·s_eff, 3σ)` (nieliniowość w paśmie D).
- **N1:** zmiana `Δ(D×10)` między tolerancją domyślną a `1e-4` o ponad `0.02 dex`. Wynik dla D oznaczam wtedy jako
  ograniczony tolerancją.

## Szum

- Z REVIEW_044 T2: `σ_Y ≈ 7–8e-5`, nachylenie `0.007–0.012` na dex.
- Pierwiastek z 7 punktów ma błąd `~0.004 dex`; różnica `Δ` ma `~0.006 dex`.
- Błędy `s_eff` z propagacji. Przy `D×2` sygnał leży na poziomie szumu, dlatego głównym pomiarem dla D jest `D×10`.

Werdykt ogłaszam niezależnie od kierunku. Wynik jest modelowy (kod autorów), bez walidacji fizycznej źródła i bez
granicy PBH. Jako wynik Claude'a wymaga audytu spoza rodziny Claude.
