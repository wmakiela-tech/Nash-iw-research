---
artifact_id: IW_BADACZ_B1_QB_T2_NATIVE_CHARGE_NORMALIZATION_CONTOUR_REVIEW_071_20261116
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel natywny B1
created_at: 2026-11-16
document_type: REVIEW
responds_to: PREREG_069 (f1e16c0); PROPOSAL_068 (07211d6)
authorization: Moderator 16 XI 2026 16:47 („Autoryzuję t1 i t2”)
data: data/t2_{orig,e5}_{default,1e-4}.csv, data/analysis069.json (skrypt preregu), data/t2_run_record.json (statusy, oś czasu, logi)
claim_ceiling: NATIVE_CONDITIONAL_SHIFT / INTERPRETATION_CONDITIONAL_ON_T1_AND_T3 / NO_PAPER_ERROR_CLAIM / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
external_audit: WYMAGANY (replika z rodziny GPT na podzbiorze; recenzja REC12/AUD2)
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_071: B1 Q-B, T2 — natywne przesunięcie konturu przy połówkowej normalizacji ładunkowej

**Rola:** Badacz. Wnioski mają status [▷]. Interpretacja fizyczna zależy od T1 (Mech-S9) i T3.

## Przebieg

- **Czas i zakres:** 16 XI, 16:51–17:11 (zegar kontenera); 4 serie, wszystkie ze statusem 0; 232 wywołania `(last ∘ magic)`.
- **Kod:** autorów, `d395183`, bez zmian poza łatką E5 (Mech-S6) w ramieniu `e5` i linią `solve` w serii 1e−4.
- **Odstępstwa:** brak, także brak rozszerzeń okien. Każda z 16 serii ma dokładnie jedną zmianę znaku Y − 0.251.

## Werdykty preregu

| werdykt | wynik |
|---|---|
| **W** (wszystkie D_j ∈ [+0.20, +0.35]) | **W-PASS** |
| **ORD** (D_90 ≥ D_22) | **ORD-PASS** (0.301 ≥ 0.272) |
| **TOL** (\|ΔD\| ≤ 0.03 przy 1e−4, j = 22 i 62) | **TOL-STABLE** (+0.0029; −0.0027) |

## Przesunięcie D_j = korzeń(E5) − korzeń(orig), metoda M_D, tolerancja domyślna

| j | m [g] | D [dex] | czynnik w β | rozrzut metod | błąd stand. | D − REVIEW_038 | D − log₁₀2 | korzeń orig − archiwum |
|---|---|---|---|---|---|---|---|---|
| 22 | 1.121e9 | 0.2723 | 1.87 | 0.003 | 0.004 | −0.007 | −0.029 | −0.001 |
| 28 | 1.330e9 | 0.2756 | 1.89 | 0.010 | 0.004 | +0.008 | −0.025 | −0.002 |
| 38 | 1.767e9 | 0.2758 | 1.89 | 0.011 | 0.003 | −0.005 | −0.025 | +0.003 |
| 51 | 2.556e9 | 0.2926 | 1.96 | 0.003 | 0.003 | +0.006 | −0.008 | −0.004 |
| 62 | 3.494e9 | 0.2981 | 1.99 | 0.002 | 0.002 | +0.003 | −0.003 | −0.002 |
| 90 | 7.743e9 | 0.3007 | 2.00 | 0.001 | 0.001 | −0.000 | −0.000 | −0.004 |

## Co z tego wynika [▷]

1. **Pomiar z REVIEW_038 potwierdza się natywnie** w skalibrowanym środowisku: zgodność ≤ 0.008 dex w każdej z 6 mas. To odtworzenie przez tę samą komórkę, więc audyt Claude-nad-Claude nie jest zewnętrzny.
2. **Korzenie oryginału zgadzają się z archiwum autorów** do 0.004 dex. Siatka i metoda nie wprowadzają przesunięcia względem opublikowanego konturu.
3. **Przesunięcie dąży do log₁₀2** wraz z masą (niedobór 0.029 → 0.000 dex). Interpretacja:
   - przy ciężkich masach kontur zależy wyłącznie od kanału hadronowego, a odpowiedź jest w nim liniowa;
   - na lewej ścianie przesunięcie wynosi ok. 90% log₁₀2 (0.272/0.301), więc ok. 10% zależy od czegoś, czego połowienie źródła nie skaluje: efektów niehadronowych albo nieliniowości.

   Pomost do Q-A: mapa s z PREREG_070 rozróżni te dwie możliwości.
4. **Tolerancja:** korzeń oryginału przy j = 22 przesuwa się pod 1e−4 o +0.023 dex, zgodnie z dryfem z REVIEW_044. Przesunięcie D zmienia się jednak tylko o 0.003 dex. Błąd numeryczny konturu znosi się w różnicy ramion.

**Warunkowo:** jeśli T1 da T1-GROUPED (tabela 100×5 autorów jest sumą stanów ładunkowych) i T3 nie znajdzie wcześniejszej korekty, ograniczenie Wu–Xu w paśmie 1.1–7.7e9 g byłoby za mocne o czynnik **1.87–2.00 w β**. Bez T1 i T3 nie twierdzę tego. Przy T1-PERSTATE tabela opisuje wariant niefizyczny, a hipoteza normalizacji jest zamknięta.

## Granice

- Wariant E5 traktuje K⁰_L bez zmian i połowi K± tylko w kanale K⁻, tak jak łatka Mech-S6. Inne rozdziały (np. tylko nukleony, E5b) nie są tu testowane.
- E4 (hadronizacja poniżej 1e9 g) pozostaje HOLD. To nie jest fizyczna granica PBH.
- Dla j = 22 korzeń E5 leży przy log₁₀β ≈ −16.95, czyli OFF-SCAN; zgoda obejmowała β do ok. 2e−17.

## Powrót w trzech warstwach

- **Wynik:** W-PASS, ORD-PASS, TOL-STABLE. D = 0.272–0.301 dex; zbieżność do log₁₀2 przy ciężkich masach.
- **Konfiguracja:**
  - 20 min obliczeń dzięki wywołaniom bez flagi hadronów (4.4 s zamiast 30 s);
  - most na żywo z Mech-S9 otwarty (sesja `B1-BADACZ-MECHS9-LIVE-001`), na razie bez odpowiedzi;
  - T1 po stronie Mech-S9.
- **Uczenie:** różnica ramion na tej samej siatce i w tym samym środowisku znosi szum numeryczny konturu, tu z 0.023 do 0.003 dex. Dla wielkości różnicowych lepiej projektować testy jako pary ramion niż jako bezwzględne korzenie. To obserwacja do wykorzystania w Q-A (origin_observation, nie failure mode).
