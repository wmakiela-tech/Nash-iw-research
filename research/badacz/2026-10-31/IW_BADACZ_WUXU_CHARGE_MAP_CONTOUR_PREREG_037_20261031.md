---
artifact_id: IW_BADACZ_WUXU_CHARGE_MAP_CONTOUR_PREREG_037_20261031
exposure: PUBLIC
claim_ceiling: PREREGISTRATION / TESTS_ONLY / NO_RESULT / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-31
origin_cell: BADACZ (wątek Claude)
document_type: PREREG
task_id: BADACZ-FRONTB-CHARGE-MAP-CONTOUR-001
owner_of_physics: Mech-S7 (linia Mech-S6/S7: mapa ładunkowa B_exec/B_sym); ten test jest wsparciem krzyżowym
---

# Preregistracja E5: wpływ mapy ładunkowej `B_sym` na kontur Fig. 5 (kod natywny)

## Pytanie

- Kod autorów wpisuje każdą zagregowaną kolumnę źródła (`π±`, `K±`, `p + p̄`, `n + n̄`) bez zmian do obu
  populacji jednoładunkowych (`B_exec`; XH-S4 002, Rec9).
- Mech-S6 przygotował łatkę `B_sym` (`research/mech-s6/2026-10-17/apply_wuxu_charge_pair_source_map.py`):
  mnoży te cztery kolumny przez `1/2`, a `K⁰_L` zostawia bez zmian.
- W jedynym zbadanym punkcie (`6e9 g`, `β = 1e-16`, głęboko w obszarze wykluczonym) zmiana `Y_P` wynosi
  `−0.4%`. Nie znalazłem w repozytorium oceny na poziomie konturu `χ² = 4` (przeszukanie nazw `B_sym`/`Bsym`
  w `research/`, 31 X).
- Pytanie: **o ile `B_sym` przesuwa granicę `χ² = 4`** w 12 masach z PREREG_034?

## Procedura

- Ten sam sterownik co E2 (`code/wuxu_subedge_variant_boundary.jl`, wariant źródła poniżej krawędzi:
  `native`), z dodatkową łatką Mech-S6 nałożoną bez zmian na `main-scan.jl`. Łatka sama odmawia działania,
  jeśli kontrakt źródła nie jest dokładnie taki, jak audytowany.
- Granica `Y_C = 0.251` (obserwabla autorów), bisekcja w `log₁₀ β` na `[−21, −15]` do `0.005 dex`,
  domyślne tolerancje. Porównanie z `B_exec` = wariant `native` z E2.

## Oczekiwania i falsyfikatory

- Jeśli odpowiedź `Y − Y_SBBN` jest blisko liniowa w liczbie wstrzykniętych hadronów, połowa źródła daje
  przesunięcie bliskie `log₁₀ 2 = 0.30 dex`. `K⁰_L` bez zmian oraz nieliniowość zmniejszają tę wartość.
- Spodziewam się przesunięcia w stronę słabszego ograniczenia o `0.15–0.30 dex` we wszystkich 12 masach.
- **Falsyfikatory:**
  - przesunięcie `< 0.05 dex` w którejkolwiek masie (wtedy mapa ładunkowa jest dla konturu nieistotna);
  - przeciwny kierunek;
  - przesunięcie `> 0.40 dex`.

Werdykt ogłaszam niezależnie od kierunku. To nie rozstrzyga, która mapa jest fizycznie poprawna (to kontrakt
symetrii źródła, Rec9/KN10). Wynik jest Claude'a i wymaga audytu spoza rodziny Claude.
