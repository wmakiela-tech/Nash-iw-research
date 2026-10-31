---
artifact_id: IW_BADACZ_WUXU_SUBEDGE_PAPER_LAW_AND_PYTHIA_PILOT_REVIEW_042_20261031
exposure: PUBLIC
claim_ceiling: CONDITIONAL_SENSITIVITY_[▷] / SM_FRAGMENTATION_PILOT_ONLY / NOT_A_PHYSICAL_SPECTRUM_VALIDATION / NO_PBH_BOUND / NO_VERDICT_ON_PUBLISHED_FIGURE / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-31
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-FRONTB-SUBEDGE-STRESS-002
prereg: research/badacz/2026-10-31/IW_BADACZ_WUXU_SUBEDGE_PAPER_LAW_AND_PYTHIA_PILOT_PREREG_041_20261031.md (commit ad6ab99, przed przebiegami)
owner_of_physics: Mech-S7 (E4); to pilotaż wspierający jego decyzję
code: research/badacz/2026-10-31/code/wuxu_subedge_variant_boundary_v2.jl; wuxu_pythia_multiplicity_pilot.py; wuxu_table_edge_slope_posthoc.py; wuxu_prereg041_analysis.py
outputs: research/badacz/2026-10-31/data/subedge_pilot/ (CSV, JSON, RUNLOG.md, MANIFEST_SHA256.md)
---

# Prawo emisji poniżej `1e9 g`: tekst autorów, kod autorów i pilotaż PYTHIA

**Status:** `[▷]`. Pilotaż obejmuje tylko fragmentację SM, bez współczynników szarości, bez pierwotnych
`t/W/Z/H` i bez fizyki spoza SM. Wynik Claude'a, wymaga audytu spoza rodziny Claude.

## Wynik

1. **Nachylenie, którym kod autorów ekstrapoluje poniżej `1e9 g` (`−1.20`), to artefakt brzegu tabeli**
   (post hoc).
   - W głębi tabeli (`T = 3.7–6.7 TeV`) lokalne nachylenie wynosi `−1.295…−1.304` dla `π±`. Spłaszcza się
     dopiero w ostatnich 4–5 wierszach, do `−1.20` przy krawędzi.
   - Model z pilotażu PYTHIA zgadza się z głębią tabeli do `≤ 0.016` i przy krawędzi daje `−1.304`.
   - Tekst autorów deklaruje `T^{1.3}`, które uzyskali własnym przebiegiem PYTHIA.
   - Zgodne jest to z limitem energii partonu w BlackHawk (`1e5 GeV`), który autorzy wskazują jako powód
     nieużywania BlackHawk poniżej `1e9 g`. Przy krawędzi ucina on już ogon widma pierwotnego. To hipoteza
     mechanizmu `[▷]`, niesprawdzona bezpośrednio.
2. **Skutek na konturze (A, prawo z tekstu `T^{1.3}`):** ograniczenie wzmacnia się o `0.028–0.055 dex` przy
   `m ≤ 1.58e9 g` i o `≤ 0.012 dex` dla cięższych mas. Kod i tekst autorów różnią się więc na lewej ścianie o
   kilka setnych dex. To mierzy, na konturze, rozbieżność kodu i tekstu opisaną przez Rec9.
3. **Pilotaż PYTHIA (B):** wykładnik krotności `δ = d ln n/d ln E` dżetu kwarkowego:
   - `0.37` przy 1–3 TeV, `0.30` przy 10–100 TeV (autorzy: `0.3`), `0.27` przy 3–30 PeV;
   - maleje z energią, zgodnie z przewidywaniem;
   - model tempa daje nachylenie `−1.30` przy krawędzi i `−1.27` przy `T = 1 PeV`.
4. **Bramka B2 nie przeszła:** `|−1.304 − (−1.200)| = 0.104 > 0.10`. Zgodnie z preregiem nie uruchomiłem
   wariantu C (`pyt`). Post hoc widać, że punkt odniesienia bramki (nachylenie przy krawędzi) sam był
   obciążony. Nachylenia `pyt` (`−1.30 → −1.27`) leżą jednak między `p13` (`−1.3`) a OLS-8 (`−1.27`), więc
   C dałoby wynik pomiędzy nimi. To wniosek z interpolacji, nie z przebiegu.

**Dla lewej ściany:** w obrębie fragmentacji SM prawo emisji poniżej `1e9 g` jest ustalone do kilku setnych
dex konturu. Otwarte pozostają współczynniki szarości, pierwotne bozony ciężkie i fizyka spoza SM (E4 u Mech-S7).

## A: wariant `p13`

| `m` [g] | 1.121e9 | 1.187e9 | 1.256e9 | 1.330e9 | 1.448e9 | 1.577e9 | 1.767e9 | 2.036e9 | 2.556e9 | 3.494e9 | 5.828e9 | 7.743e9 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `p13` [dex] | −0.048 | −0.055 | −0.035 | −0.030 | −0.038 | −0.028 | −0.011 | −0.009 | −0.012 | −0.005 | −0.001 | +0.000 |
| OLS-8 (REVIEW_038) | −0.029 | −0.041 | −0.024 | −0.017 | −0.029 | −0.022 | −0.002 | −0.003 | −0.004 | −0.004 | −0.000 | −0.001 |

- **Werdykt:** nie sfalsyfikowany: brak dodatniego przesunięcia `> 0.03` i brak `|·| > 0.1`.
- **Przewidywania:**
  - dla `m ≤ 1.58e9 g` trafione (`[−0.06, −0.02]`);
  - dla `m ≥ 2.0e9 g` chybione o `0.002` przy `2.556e9 g` (`−0.012` wobec progu `0.01`), w granicach szumu
    metody (`~0.01`).

## B: pilotaż PYTHIA 8.318

| `E` na parton [TeV] | 1 | 3 | 10 | 30 | 100 | 300 | 1000 | 3000 | 10⁴ | 3·10⁴ |
|---|---|---|---|---|---|---|---|---|---|---|
| `n_π±` dżet kwarkowy | 26.6 | 40.1 | 60.2 | 84.0 | 119.9 | 163.2 | 234.0 | 309.2 | 427.9 | 575.3 |
| `n_π±` dżet gluonowy | 48.1 | 71.3 | 107.4 | 148.0 | 219.3 | 305.9 | 434.1 | 573.7 | 829.1 | 1097.6 |

- `δ` (wszystkie hadrony, kwarki) w kolejnych przedziałach: `0.375, 0.332, 0.304, 0.295, 0.282, 0.300, 0.254,
  0.271, 0.268`. Gluony: `0.361 … 0.255`.
- **Bramka:**
  - B1 przeszła: `δ_q = 0.304` (10–30 TeV) i `0.295` (30–100 TeV);
  - B2 nie przeszła (`0.104 > 0.10`).
- **Przewidywania:** obie trafione (`δ` maleje; `|s(1 PeV)| = 1.27 < |s(10 TeV)| = 1.30`).
- **Falsyfikator B:** nie zadziałał; wszystkie `δ` mieszczą się w `[0.1, 0.5]`.
- **Nieudane zdarzenia:** 69 z 8000, wszystkie przy `E ≥ 3000 TeV` (do 7,5% przy 30 PeV). Możliwe obciążenie
  `δ` na samej górze siatki. Dla konturu nieistotne: przy `s ≈ −1.3` masy poniżej `1e7 g` (`T > 1 PeV`) niosą
  `(1e7/1e9)^{1.7} ≈ 4e-4` liczby hadronów emitowanych poniżej krawędzi.

## Post hoc: profil nachylenia tabeli autorów

| `T` [TeV] (środek pary wierszy) | 10.1 | 9.3 | 8.6 | 7.9 | 7.3 | 6.7 | 6.1 | 5.6 | 5.2 | 4.8 | 4.4 | 4.0 | 3.7 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| tabela, `s_π` | −1.200 | −1.239 | −1.266 | −1.281 | −1.291 | −1.295 | −1.298 | −1.299 | −1.300 | −1.301 | −1.302 | −1.303 | −1.304 |
| model PYTHIA, `s_π` | −1.304 | −1.304 | −1.305 | −1.305 | −1.306 | −1.306 | −1.307 | −1.308 | −1.310 | −1.311 | −1.313 | −1.315 | −1.317 |

- Fizyka QCD daje powolną zmianę (`~0.01` na czynnik 3 w `T`). Tabela zmienia się o `0.10` na ostatnim
  czynniku `~1.4`, co wskazuje na artefakt brzegu.
- **Wartość w wierszu brzegowym** leży około 2% poniżej ekstrapolacji nachylenia z głębi tabeli (wiersze
  6–12), dla wszystkich pięciu kolumn (`ln Δ ≈ −0.019…−0.020`). Wpływ na kontur w modelu liniowym:
  `≲ 0.01 dex`.

## Czego nie sprawdziłem

- Współczynników szarości zależnych od spinu, emisji pierwotnych `t/W/Z/H`, stopni swobody spoza SM.
- Bezpośrednio mechanizmu spłaszczenia (limit `1e5 GeV` w BlackHawk). Wymagałoby to BlackHawk, którego tu nie
  ma.
- Wariantu C (zablokowany przez bramkę).
- Nowości nie zgłaszam: `N(E) ∝ E^{0.3}` to wynik autorów, który odtwarzam; zgodność nachylenia `−1.3`
  z głębią tabeli autorów jest obserwacją, nie nowym wynikiem.

## Odtworzenie

```text
pip install pythia8mc==8.318.3 numpy
python3 -I code/wuxu_pythia_multiplicity_pilot.py --csv pythia_multiplicities.csv --json pythia_pilot.json --table pythia_rate_table.csv
python3 -I code/wuxu_table_edge_slope_posthoc.py --table <…/data/out/hadrons_from_PBH.dat> --pilot pythia_pilot.json --out table_edge_posthoc.json
julia --project=<env> code/wuxu_subedge_variant_boundary_v2.jl <…/arXiv-2509.05618> p13 e2_p13.csv
python3 -I code/wuxu_prereg041_analysis.py --native data/native_audit/e2_native.csv --p13 e2_p13.csv \
    --ols8 data/native_audit/e2_ols8.csv --pilot pythia_pilot.json --posthoc table_edge_posthoc.json --out prereg041_analysis.json
```

Pilotaż trwa około 8 min (ziarno ustalone), wariant `p13` około 16 min.

## Powrót w trzech warstwach

- **Wynik:** nachylenie ekstrapolacji w kodzie autorów jest artefaktem brzegu tabeli. Prawo z tekstu autorów,
  głąb tabeli i PYTHIA zgadzają się na `≈ −1.30`. Różnica dla konturu: kilka setnych dex na lewej ścianie.
- **Konfiguracja:** PYTHIA z PyPI działa w kontenerze; pilotaż był tani (8 min). Bez BlackHawk nie da się
  sprawdzić mechanizmu ani współczynników szarości.
- **Uczenie systemu:** punkt odniesienia bramki walidacyjnej wybrałem tam, gdzie dane źródła są najbardziej
  podejrzane: na brzegu obszaru ważności tabeli.
  - origin_failure_mode: `VALIDATION_REFERENCE_AT_ARTEFACT_BOUNDARY`.
  - Reguła `[▷]`: model waliduję na danych referencyjnych z głębi ich obszaru ważności. Wartość przy brzegu
    traktuję jako osobny test, nie jako wzorzec.
  - Drugi błąd mechanizmu: sterownik v1 miał wspólną nazwę pliku tymczasowego (RUNLOG). Przebiegi produkcyjne
    nie były dotknięte, w v2 jest to poprawione.
  - Trzeci, mój: w SYNTH_039 r1 napisałem, że E4 „nie da się zrobić w tym kontenerze”, nie sprawdzając
    `pip`. To ten sam `NEGATIVE_KNOWLEDGE_SCOPE_DRIFT`, który tego samego dnia przypisałem innym komórkom.
    Poprawione w SYNTH_039 r2. Reguła z SYNTH_039 dotyczy też mnie: przed zdaniem „nie da się” jedna tania
    próba (tu: `pip install`).

Wynik jest Claude'a, więc wymaga audytu spoza rodziny Claude.
