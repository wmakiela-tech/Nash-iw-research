---
artifact_id: IW_BADACZ_WUXU_COLUMN_SEMANTICS_AND_PAIRED_ROOT_REVIEW_044_20261102
exposure: PUBLIC
claim_ceiling: RESULT_[▷] / TABLE_SEMANTICS_FROM_MODEL_RATIO / CONDITIONAL_ON_FIGURE_PROVENANCE / NO_PBH_BOUND / NO_VERDICT_ON_PUBLISHED_FIGURE / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-02
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-FRONTB-COLUMN-AND-ROOT-001
prereg: research/badacz/2026-11-02/IW_BADACZ_WUXU_COLUMN_SEMANTICS_AND_PAIRED_ROOT_PREREG_043_20261102.md (commit ec6d473, przed przebiegami)
responds_to: MT14 ROT022; SCOPE9 TOPDOWN016/017; Mech-S7 ROT036/037 (dyspozycja z 1 XI)
owner_of_physics: Mech-S7; werdykt o kontrakcie źródła: REC10; audyt: AUD1
code: research/badacz/2026-11-02/code/wuxu_column_semantics_k0l.py; wuxu_variant_grid.jl; wuxu_paired_root_analysis.py
outputs: research/badacz/2026-11-02/data/ (MANIFEST_SHA256.md)
---

# Kolumny tabeli Wu–Xu to sumy cząstka + antycząstka; przesunięcia granicy są odporne na szum

**Status:** `[▷]`. Wynik Claude'a, wymaga audytu spoza rodziny Claude. Żadna liczba tu nie jest granicą
PBH ani werdyktem o opublikowanej figurze.

## Wynik

1. **T1: kolumny `π`, `K`, `p`, `n` w tabeli autorów są sumami po stanach sprzężonych ładunkowo**
   (`π⁺ + π⁻`, `K⁺ + K⁻`, `p + p̄`, `n + n̄`).
   - Kotwicą jest `K⁰_L`, jeden stan bez osobnej antycząstki.
   - Stosunki do `K⁰_L` w głębi tabeli (`T = 3.9–6.4 TeV`) zgadzają się z modelem PYTHIA liczącym sumy do
     `1%`: mediana `r = 0.999` (`π`), `0.999` (`K`), `1.009` (`p`), `1.008` (`n`).
   - Alternatywa „jeden stan ładunkowy” wymagałaby `r ≈ 0.5`, więc jest wykluczona.
   - Przewidywanie (`r ∈ [0.75, 1.33]`) trafione dla wszystkich czterech kolumn; falsyfikator nie zadziałał.
2. **Wniosek dla mapy ładunkowej (warunkowy):**
   - Kod autorów wpisuje każdą sumę w całości do populacji jednego stanu: `π±` do `π⁻` i do `π⁺`, `K±` do
     `K⁻`, `p + p̄` do `p̄`, `n + n̄` do `n̄`.
   - Neutralna, nierotująca czarna dziura emituje cząstki i antycząstki symetrycznie, więc na każdy stan
     przypada połowa sumy. To jest `B_sym` z E5.
   - Po T1 podział dla `π/K` nie jest już dowolnym założeniem symetrii (typ z Rec9, 18 X): wynika z
     semantyki tabeli i z symetrii C emisji Hawkinga.
   - Warunki, które zostają:
     - że populacje w ODE autorów oznaczają pojedyncze stany (tak je nazwano w kodzie);
     - że figura w JCAP pochodzi z tego kodu (proweniencja niesprawdzona; MT14 ROT016–018).
   - Przy tych warunkach przesunięcie z E5 (`+0.27…+0.30 dex`, ograniczenie słabsze `~2` razy w `β`) jest
     oczekiwaną poprawką kodu. Werdykt o kontrakcie należy do REC10.
3. **T2: przesunięcia z REVIEW_038/042 są odporne na szum.** To odpowiedź na SCOPE9 FD78–FD86.
   - Rozrzut reszt `Y` wokół lokalnej prostej wynosi `5–8e-5` w jednym środowisku, nie `2.8e-4`.
     Wartość `2.8e-4` to różnica między środowiskami (REVIEW_035), nie szum w obrębie jednego.
   - Regresja na 15 punktach daje błąd granicy `0.001–0.003 dex`.
   - Przesunięcia z regresji zgadzają się z bisekcją do `≤ 0.011 dex` i mają `|przesunięcie|/SE = 16–41`.
   - Przewidywania trafione, falsyfikatory nie zadziałały.
4. **T3: tolerancja solvera przy `j = 22`.**
   - Przesunięcie `nsym − native` przy `reltol = 1e-5` wynosi `+0.051` wobec `+0.063` przy domyślnych.
     Różnica `0.012` mieści się w przewidywanych `0.02`.
   - **Nowe:** sama granica natywna przy `1e-5` przesuwa się o `+0.032 dex` wobec bisekcji domyślnej
     (`+0.025` wobec regresji domyślnej).
   - Na lewej ścianie, gdzie nachylenie `Y` wobec `log β` jest najmniejsze (`0.006` na dex), tolerancja
     solvera przesuwa kontur o `~0.03 dex`. To więcej niż `≤ 0.013 dex` podane w REVIEW_035 (to były różnice
     między środowiskami przy tej samej tolerancji).
   - Przesunięcia między wariantami częściowo się znoszą (`0.012`).

## T1: tabela

Stosunek do `K⁰_L`: tabela / model (`r`).

| wiersz | `T` [TeV] | `π±/K⁰_L` | `K±/K⁰_L` | `(p+p̄)/K⁰_L` | `(n+n̄)/K⁰_L` |
|---|---:|---|---|---|---|
| 6 | 6.40 | 16.779 / 16.798 (0.999) | 2.032 / 2.037 (0.997) | 1.193 / 1.179 (1.012) | 1.186 / 1.177 (1.007) |
| 7 | 5.89 | 16.772 / 16.791 (0.999) | 2.032 / 2.036 (0.998) | 1.192 / 1.179 (1.011) | 1.185 / 1.176 (1.008) |
| 12 | 3.87 | 16.736 / 16.751 (0.999) | 2.033 / 2.032 (1.001) | 1.186 / 1.180 (1.005) | 1.179 / 1.169 (1.009) |

- Post hoc, poza regułą decyzji: w wierszu brzegowym (`T = 10.6 TeV`) `r = 0.99–1.02`, przy `T = 69 GeV`
  `r = 0.97–1.03`. Zgodność utrzymuje się w całym zakresie tabeli.
- Zgodność do `1%` sugeruje, że stosunki gatunków w tabeli to w praktyce stosunki krotności PYTHIA
  (BlackHawk liczy z tablic PYTHIA). Stosunki znoszą współczynniki szarości i normalizację.
- **Ograniczenie:** to semantyka tabeli Wu–Xu, nie tożsamość bajtowa z tablicami BlackHawk v2.3. Ten test
  pozostaje u MT14 (ROT021/022).

## T2: siatka sparowana (15 punktów, `±0.12 dex`, jedno środowisko, domyślne tolerancje)

| wariant, masa | granica (regresja) | `SE` | nachylenie `Y`/dex | `σ` reszt | kwadratowa − liniowa |
|---|---:|---:|---:|---:|---:|
| native, `j = 22` | −17.2192 | 0.0029 | 0.0067 | 8.1e-5 | −0.0046 |
| native, `j = 24` | −17.7762 | 0.0014 | 0.0115 | 6.8e-5 | +0.0043 |
| nsym, `j = 22` | −17.1587 | 0.0019 | 0.0066 | 5.1e-5 | −0.0008 |
| nsym, `j = 24` | −17.7026 | 0.0011 | 0.0109 | 5.3e-5 | −0.0006 |
| p13, `j = 22` | −17.2783 | 0.0023 | 0.0068 | 6.5e-5 | +0.0025 |
| p13, `j = 24` | −17.8211 | 0.0013 | 0.0116 | 6.2e-5 | +0.0040 |

| przesunięcie | regresja | bisekcja | różnica |
|---|---:|---:|---:|
| nsym, `j = 22` | +0.0606 ± 0.0035 | +0.0628 | −0.0022 |
| nsym, `j = 24` | +0.0737 ± 0.0018 | +0.0639 | +0.0098 |
| p13, `j = 22` | −0.0591 ± 0.0037 | −0.0485 | −0.0106 |
| p13, `j = 24` | −0.0449 ± 0.0019 | −0.0545 | +0.0096 |

- **Uwaga SCOPE9 była trafna w tym, co dotyczy pojedynczych punktów bisekcji.** Przy `j = 22` tylko
  11 z 14 sąsiednich przyrostów `Y` na siatce `0.017 dex` jest dodatnich. Szum (`~8e-5`) jest tam
  porównywalny z przyrostem na krok (`0.0067 × 0.017 ≈ 1.1e-4`), więc znaki końców bisekcji nie są
  pojedynczo wiarygodne.
- Granica z bisekcji ma przez to rozrzut `~0.01 dex`. Regresja po siatce go usuwa, a wnioski o
  przesunięciach się nie zmieniają.
- Wierność różnicy przy różnych kształtach odpowiedzi (FD86): nachylenia wariantów przy tej samej masie
  różnią się o `≤ 6%`, a przesunięcia mierzę na wspólnym progu `Y = 0.251`. Stała kalibracja wspólna dla
  wariantów zmieniłaby przesunięcie najwyżej o `6%` swojej wielkości.

## T3: tolerancja `reltol = 1e-5` (3 punkty na wariant, `j = 22`)

| | granica | nachylenie |
|---|---:|---:|
| native, `1e-5` | −17.1945 | 0.0060 |
| nsym, `1e-5` | −17.1437 | 0.0068 |
| przesunięcie, `1e-5` | +0.051 | |
| przesunięcie, domyślne (bisekcja) | +0.063 | |

Granica natywna przy `1e-5` leży o `+0.032 dex` od bisekcji domyślnej. Budżet niepewności w SYNTH_039
poprawiam: tolerancja solvera daje do `~0.03 dex` na lewej ścianie.

## Czego nie sprawdziłem

- Tożsamości tabeli Wu–Xu z tablicami BlackHawk v2.3 (MT14).
- Semantyki populacji w ODE autorów poza nazwami i równaniami w `main-scan.jl`.
- Tolerancji `1e-5` dla pozostałych mas i dla `p13` (koszt: około 400 s na punkt).
- Proweniencji figury JCAP.
- Nowości nie zgłaszam: konwencja sum cząstka + antycząstka jest opisana w źródłach (Arbey–Auffinger,
  BlackHawk; za MT14 ROT022). T1 sprawdza ją na danych autorów.

## Odtworzenie

```text
python3 -I code/wuxu_column_semantics_k0l.py --table <hadrons_from_PBH.dat> \
    --pilot research/badacz/2026-10-31/data/subedge_pilot/pythia_pilot.json --out column_semantics.json
julia --project=<env> code/wuxu_variant_grid.jl <…/arXiv-2509.05618> native grid_native.csv pts_native.dat
julia --project=<env> code/wuxu_variant_grid.jl <…/arXiv-2509.05618> native_nsym grid_native_nsym.csv pts_native_nsym.dat
julia --project=<env> code/wuxu_variant_grid.jl <…/arXiv-2509.05618> p13 grid_p13.csv pts_p13.dat
julia --project=<env> code/wuxu_variant_grid.jl <…/arXiv-2509.05618> native tol_native.csv pts_tol_native.dat ladder:1e-5:1e-8
julia --project=<env> code/wuxu_variant_grid.jl <…/arXiv-2509.05618> native_nsym tol_native_nsym.csv pts_tol_native_nsym.dat ladder:1e-5:1e-8
python3 -I code/wuxu_paired_root_analysis.py --grid-native grid_native.csv --grid-nsym grid_native_nsym.csv --grid-p13 grid_p13.csv \
    --bis-native <…/2026-10-31/data/native_audit/e2_native.csv> --bis-nsym <…/e5b_native_nsym.csv> \
    --bis-p13 <…/2026-10-31/data/subedge_pilot/e2_p13.csv> --tol-native tol_native.csv --tol-nsym tol_native_nsym.csv --out paired_root.json
```

`wuxu_variant_grid.jl` to sterownik v2 z 31 X z inną pętlą główną (lista punktów zamiast bisekcji) i opcją
tolerancji. Definicje wariantów są bez zmian.

## Powrót w trzech warstwach

- **Wynik:**
  - kolumny tabeli autorów to sumy po stanach ładunkowych (zgodność `1%`), więc mapa ładunkowa w kodzie
    podwaja wstrzykiwanie każdego stanu;
  - przesunięcia granicy z wariantów są odporne na szum;
  - tolerancja solvera przesuwa lewą ścianę o `~0.03 dex`.
- **Konfiguracja:** krytyka SCOPE9 (bez Julii, z publicznych CSV) wskazała słabość, którą jedna sparowana
  siatka rozstrzygnęła w 10 min. Podział pracy (krytyka z danych → test natywny) zadziałał.
- **Uczenie systemu:**
  - Wartość `2.8e-4` z REVIEW_035 trafiła do innej komórki jako błąd „na punkt”, choć była różnicą
    środowisk. Moje dokumenty nie rozdzielały wyraźnie trzech rodzajów szumu: między środowiskami,
    w obrębie środowiska, od tolerancji. origin_failure_mode: `NOISE_TYPE_CONFLATION_IN_REPORTED_ERROR`.
  - Reguła `[▷]`: podając błąd numeryczny, nazywam jego typ i zakres zastosowania.
  - Kotwica bez niejednoznaczności (`K⁰_L`) zamieniła spór o konwencję w test stosunku z czynnikiem 2 jako
    rozdzielczością.

Wynik jest Claude'a, więc wymaga audytu spoza rodziny Claude.
