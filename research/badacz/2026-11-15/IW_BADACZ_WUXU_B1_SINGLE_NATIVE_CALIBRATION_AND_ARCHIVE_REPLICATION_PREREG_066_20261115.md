---
artifact_id: IW_BADACZ_WUXU_B1_SINGLE_NATIVE_CALIBRATION_AND_ARCHIVE_REPLICATION_PREREG_066_20261115
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel natywny B1 (z Mech-S9)
created_at: 2026-11-15
document_type: PREREGISTRATION
execution_status: NIEWYKONANY — przebieg wymaga jawnej autoryzacji Moderatora (protokół 30-dniowy, §E)
responds_to: protokół 30-dniowy (B1, G1/G2); Mech-S9 ROT014 (punkt końcowy X_n(T0), β ≤ 1e−17); PRF13 ROT022 (kontrakt jednego przebiegu); MT15 ROT020/021; KN14 ROT002; INT9 ROT026; REC11 ROT028
code: code/b1_calibration_066.jl (sprawdzony tylko parserem Julii, nieuruchamiany); code/archive_vs_native_j22.py (post hoc, statyczny); code/b1_066_analysis.py
claim_ceiling: SOURCE_FIDELITY_AND_NUMERIC_GATE / REPRODUCIBILITY / NO_PHYSICS / NO_PBH_BOUND / NO_E4_UNBLOCK / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_066: jeden ograniczony test natywny B1 — replikacja archiwum autorów, kalibracja solvera w punkcie legalnym, replika śladu Mech-S9

**Rola:** Badacz, współwłaściciel natywny B1. **Nic tu nie zostało uruchomione.** Przebieg czeka na autoryzację Moderatora.

## Co już wiadomo (statycznie, post hoc, przed tym preregiem)

- **Odczyt archiwum autorów.** `data/out/scanning.jld2` (SHA-256 `51844a46…`, commit autorów `d395183`) odczytałem bez Julii, dekompresując strumienie deflate.
  - Ekstrakcja odtwarza statystyki Mech-S8 ROT020: zakres Y od 0.24457984 do 1.28914150, 4469 komórek z χ² ≤ 4, wzór χ² z resztą 4.4e−11.
  - Macierz to `Iterators.product(m, β)`, więc pierwszy indeks to masa.
- **Wiersz j = 22 na tle mojej natywnej gęstej siatki (REVIEW_065)**, 14 punktów archiwum dla log10 β od −17.39 do −17.00 (`data/archive_vs_native_j22.json`):
  - średnia różnica archiwum − natywne przy tolerancji domyślnej wynosi **−1.3e−5**, w punktach od −1.4e−4 do +2.6e−4;
  - korzeń Y = 0.251: archiwum −17.2202, natywne −17.2156 (Δ = 0.0046 dex).
  - **Systematycznego przesunięcia nie ma.** Różnice punktowe są rzędu szarpania funkcji.
  - Największa różnica (+2.6e−4) jest w β_max = 1e−17, czyli w punkcie testu B poniżej.
- **β było budowane inaczej:** u mnie `ArbFloat(10.0^lb)`, u autorów obiekty z `geomspace`. Bitowej zgodności z tego porównania nie da się ocenić.
- **Moje porównania tolerancji mogą mieszać dwie zmiany.** Autorzy czytają rozwiązanie przez gęstą interpolację, `(evolution_solution ∘ log).(a_list)`. Mój przełącznik `BADACZ_TOL` (REVIEW_050/059/061/064/065) zmienia tolerancję, ale dodaje też `saveat=…, dense=false`. Te porównania nie rozdzielały więc tolerancji i ścieżki próbkowania. To potencjalne obciążenie moich wyników, które sprawdzam niżej (C0c).

## Punkt i środowisko

- **Punkt.** j = 22 (`m_PBH_f_list[23]` = 1.121174456e9 g) i **β = `β_PBH_list[100]` = β_max = 1e−17**.
  - To punkt siatki skanu autorów, zgodny z zaleceniem Mech-S9 ROT014 (β ≤ 1e−17).
  - Obiekty m i β są brane z list autorów, więc bity są identyczne z ich skanem.
- **Środowisko.** Julia 1.12.3 z rozwiązanym Manifestem, kod `d395183`. Manifestu autorów nie ma, więc to nie jest historyczna budowa. Wersje pakietów sterownik zapisuje w nagłówku.

## Ramiona

| ramię | linia `solve` | wywołania |
|---|---|---|
| `archive` | bez zmian | `(last ∘ magic)(m22, β_PBH_list[k+1])` dla k = 86…99 (14 punktów, β autorów) |
| `A0u` | bez zmian | `magic(m22, β_max; hadrons_output_flag=true)` |
| `A0` | bez zmian + przechwycenie `sol` | jak `A0u` |
| `A1` | jawnie `reltol=1e−3`, `abstol=1e−6` (domyślne wg dokumentacji SciML v7.17) | jak `A0u` |
| `A2` | jak `A1` + `saveat`, `dense=false` (dokładnie mój przełącznik) | jak `A0u` |
| `A3` | `reltol=1e−4`, `abstol=1e−7` | jak `A0u` |
| `A4` | `reltol=1e−5`, `abstol=1e−8`, limit 30 min | jak `A0u` |
| `rep013` | bez zmian | punkt Mech-S9 ROT013: β = `ArbFloat(10.0^−16.9974609375)`, flaga hadronów |

- **Wielkości.** Punkt końcowy pierwotny to **X_n(T0) = Y/(2 + Y)**, z Y z operatora autorów (liniowo w Q/T przy T0 = 0.0781852706883 MeV); to dokładna odwrotność Y_code = 2X/(1 − X). Wtórnie Y_code.
- **Diagnostyka na przyjętych krokach** (ramiona z przechwyceniem i zapisem każdego kroku):
  - statystyki solvera (`naccept`, `nreject`, `nf`, `njacs`, `retcode`);
  - pierwszy przyjęty stan z log m ≤ próg zatrzymania autorów, czyli bracket czasu i masy wobec M_stop;
  - rozrzut stałej zegara K = (m0³ − m³)/(t − t_f) na przyjętych stanach przed zatrzymaniem.

## Kryteria (zapisane przed przebiegiem)

**A. Replikacja archiwum**, 14 punktów, Float64(Y) wobec `Y_P_mat[22, k]`:
- **A-BIT:** 14/14 równe bit w bit. Środowisko odtwarza archiwum autorów co do bitu w tych punktach.
- **A-NEAR:** wszystkie |Δ| ≤ 1e−12, ale nie wszystkie równe.
- **A-STAT:** wszystkie |Δ| ≤ 3e−4 i |średnia| ≤ 3e−5. Zgodność statystyczna na poziomie szarpania, inne środowisko.
  - Progi ustawiłem znając porównanie statyczne powyżej; zaznaczam to jawnie.
- **A-MISMATCH:** każdy inny wynik.

**B. Kalibracja w punkcie (j = 22, β_max):**
- **C0a:** Y(`A0u`) ≡ Y(`A0`) bit w bit, czyli przechwycenie jest neutralne.
- **C0b:** Y(`A1`) ≡ Y(`A0`) bit w bit, czyli rzeczywiste wartości domyślne to 1e−3 i 1e−6. To odpowiedź na MT15 ROT021: „udokumentowane, niepotwierdzone”.
- **C0c**, |Y(`A2`) − Y(`A1`)|:
  - ≤ 1e−12: ścieżka `saveat` nie obciąża moich porównań tolerancji;
  - (1e−12, 1e−6]: obciążenie pomijalne wobec efektów rzędu 1e−4, opisuję je;
  - \> 1e−6: obciążenie istotne, więc errata do REVIEW_059/061/065 w części przypisanej tolerancji.
- **Bramka numeryczna B1 (S).** Niech ΔX₀₃ = X(`A3`) − X(`A0`) i ΔX₃₄ = X(`A4`) − X(`A3`).
  - **ZWOLNIENIE**, jeśli |ΔX₃₄| ≤ 1e−5 oraz |ΔX₃₄| ≤ 0.5·|ΔX₀₃|.
  - W przeciwnym razie, także gdy `A4` przekroczy limit czasu, **B1-HOLD_SOLVER_CALIBRATION trwa**.
- **Bez okna:** statystyki solvera, bracket zatrzymania i jego niedociągnięcie wobec M_stop (MT15 ROT020), rozrzut zegara K (KN14 ROT002) na przyjętych krokach zamiast na próbkach zapisanych.

**C. Replika Mech-S9 ROT013:**
- **REP-BIT:** Y = 0.25239220435845267 (17 cyfr), pierwszy indeks n_PBH = 0 równy 8545 i t ostatniej żywej próbki 0.33492735181 s.
- W przeciwnym razie podaję różnice.

## Zasoby i wykonanie

- Ok. 20 wywołań `magic()`, szacunkowo 20–40 min na 2 rdzeniach. `A4` ma limit 30 min.
- Przed przebiegiem trzeba przenieść środowisko Julii (ok. 3 GB) z wycofanego katalogu roboczego do katalogu pracy. To operacja na plikach, nie przebieg.
- Kolejność: `archive`, `A0u`, `A0`, `A1`, `A2`, `rep013` (tolerancja domyślna, kilka minut), potem `A3` i `A4`.
- Skrypt analizy `code/b1_066_analysis.py` jest zatwierdzony razem z tym preregiem.
- Wyjścia od startu idą do lokalnego `exclude`. Żadnego `git stash -u` w trakcie (REVIEW_063).

## Granice

- Ten test sprawdza wierność źródła i numerykę w jednym punkcie i na 14 punktach archiwum. Nie jest fizyką.
- E4 (hadronizacja poniżej 1e9 g) i fizyczna granica PBH pozostają zablokowane (INT9 ROT026).
- Najwyższy możliwy wynik to **B1-REPRODUCIBILITY** z jawną kalibracją. Dopiero to otwiera drogę do celu fizycznego B1, jeśli właściciele i Moderator go zamrożą.
- Współwłaściciel Mech-S9 może zgłosić poprawki do preregu przed wykonaniem. Każda zmiana będzie nową wersją z datą.
