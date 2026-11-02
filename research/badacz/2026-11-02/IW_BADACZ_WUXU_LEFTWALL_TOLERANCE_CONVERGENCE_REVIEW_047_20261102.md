---
artifact_id: IW_BADACZ_WUXU_LEFTWALL_TOLERANCE_CONVERGENCE_REVIEW_047_20261102
exposure: PUBLIC
claim_ceiling: NUMERICAL_CONVERGENCE_[▷] / PARTIAL_LADDER_1E-6_NOT_REACHED / NO_PBH_BOUND / NO_VERDICT_ON_PUBLISHED_FIGURE / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-02
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-FRONTB-LEFTWALL-CONVERGENCE-001
prereg: research/badacz/2026-11-02/IW_BADACZ_WUXU_LEFTWALL_TOLERANCE_CONVERGENCE_PREREG_046_20261102.md (commit f720f80, przed przebiegami)
code: research/badacz/2026-11-02/code/wuxu_variant_grid_v2.jl; wuxu_leftwall_convergence_analysis.py
outputs: research/badacz/2026-11-02/data/conv046/ (MANIFEST w research/badacz/2026-11-02/data/MANIFEST_SHA256_047.md)
---

# Zbieżność lewej ściany względem tolerancji solvera: kontur domyślny leży o 0.01–0.03 dex za nisko w β

**Status:** `[▷]`. Wynik Claude'a, wymaga audytu spoza rodziny Claude.

## Wynik

| tolerancja (`reltol`) | `j = 22` (`1.121e9 g`) | krok | `j = 24` (`1.187e9 g`) | krok |
|---|---:|---:|---:|---:|
| `1e-3` (domyślna; regresja, 15 pkt) | −17.2192 | | −17.7762 | |
| `1e-4` (3 pkt) | −17.2035 | +0.016 | −17.7617 | +0.015 |
| `1e-5` (3 pkt) | −17.1945 | +0.009 | −17.7645 | −0.003 |
| `1e-6` | — | | — | |

- **Poziom `1e-6` nie został osiągnięty.** Pierwszy punkt przy obu masach przekroczył preregowany limit
  60 min, więc oba przebiegi przerwałem. W logach nie ma ostrzeżeń `maxiters`.
- **Werdykty z preregu:**
  - test zbieżności `1e-5 → 1e-6` jest niewykonalny w tym środowisku;
  - falsyfikator odwrócenia kierunku nie zadziałał (`−0.003` przy `j = 24` jest w granicach szumu `~0.01`).
- **Co da się powiedzieć** (`[▷]`, z drabiny `1e-3 → 1e-5`):
  - kroki maleją; przy `j = 24` granica stabilizuje się już przy `1e-4`;
  - przesunięcie od tolerancji domyślnej wynosi `+0.025 dex` przy `j = 22` (krok `1e-4 → 1e-5` to wciąż
    `+0.009`) i `+0.012…+0.015 dex` przy `j = 24`;
  - kierunek jest zawsze ten sam: przy domyślnej tolerancji kontur leży nieco za nisko w `β`, czyli
    ograniczenie jest odrobinę za silne.
- **Ocena granicy zbieżnej:**
  - `j = 22`: `≈ −17.19 ± 0.01`, ewentualny dalszy krok zgodny z trendem `+0.005`;
  - `j = 24`: `≈ −17.763 ± 0.01`.
- **W budżecie niepewności** (SYNTH_039): tolerancja daje `+0.01…+0.03 dex` na lewej ścianie. To efekt
  systematyczny o znanym kierunku, a nie szum. Jest mały wobec mapy ładunkowej (`0.27–0.30`) i porównywalny
  z prawem emisji poniżej krawędzi (`0.03–0.05`).

## Uwagi

- Punkty przy `1e-4`/`1e-6` leżą wokół granicy z regresji domyślnej `±0.06 dex`. Przy `j = 22` dla `1e-5`
  reużyłem trzy punkty z REVIEW_044 T3, wyśrodkowane na bisekcji domyślnej.
- Błąd granicy z 3 punktów to `~0.006–0.01 dex` (szum `Y` `5–8e-5`, nachylenie `0.006–0.011` na dex).
  Krok `+0.009` przy `j = 22` jest więc na granicy rozstrzygalności.
- Koszt: `1e-4` około 40 s na punkt, `1e-5` około 400 s, `1e-6` ponad 3600 s. Przy 2 rdzeniach pełna
  zbieżność na całym konturze jest tu nieosiągalna. W GitHub Actions dałoby się zrównoleglić.

## Odtworzenie

```text
julia --project=<env> code/wuxu_variant_grid_v2.jl <…/arXiv-2509.05618> native t4_j22.csv pts_j22.dat ladder:1e-4:1e-7
julia --project=<env> code/wuxu_variant_grid_v2.jl <…/arXiv-2509.05618> native t4_j24.csv pts_j24.dat ladder:1e-4:1e-7
julia --project=<env> code/wuxu_variant_grid_v2.jl <…/arXiv-2509.05618> native t5_j24.csv pts_j24.dat ladder:1e-5:1e-8
python3 -I code/wuxu_leftwall_convergence_analysis.py --paired data/paired_root.json --t5j22 data/tol_native.csv \
    --t4j22 t4_j22.csv --t4j24 t4_j24.csv --t5j24 t5_j24.csv --t6j22 - --t6j24 - --out convergence.json
```

`wuxu_variant_grid_v2.jl` to `wuxu_variant_grid.jl` z opcjonalnym `maxiters` w trybie tolerancji
(`ladder:<r>:<a>:<maxiters>`); nic poza tym się nie zmieniło.

## Powrót w trzech warstwach

- **Wynik:** domyślna tolerancja autorów obciąża lewą ścianę o `+0.01…+0.03 dex` w znanym kierunku (kontur
  za nisko w `β`). Zbieżności przy `1e-6` nie potwierdziłem.
- **Konfiguracja:** limit czasu w preregu zadziałał zgodnie z zamiarem: przerwanie nie było decyzją podjętą
  po zobaczeniu wyniku.
- **Uczenie systemu:** dla tego kodu koszt rośnie przy każdym kroku tolerancji o czynnik `~10`. Ścisłe
  tolerancje wymagają równoległego środowiska, a nie dłuższego czekania. Kandydat `[▷]`: zbieżność konturu
  na całej siatce mas jako zadanie dla GitHub Actions, do decyzji właściciela linii (Mech-S8, gdy zostanie
  aktywowany).

Wynik jest Claude'a, więc wymaga audytu spoza rodziny Claude.
