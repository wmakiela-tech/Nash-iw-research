---
artifact_id: IW_BADACZ_B1_QB_T2_NATIVE_CHARGE_NORMALIZATION_CONTOUR_PREREG_069_20261116
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel natywny B1
created_at: 2026-11-16
document_type: PREREGISTRATION
authorization: Moderator, 16 XI 2026 16:47 („Autoryzuję t1 i t2”; Q-A i Q-B równolegle); zakres T2 zgodnie z PROPOSAL_068 §3, włącznie z β do ok. 2e−17 przy j = 22 (OFF-SCAN)
responds_to: PROPOSAL_068 (07211d6); REVIEW_038 (E5); REVIEW_067 (kalibracja); Mech-S9 ROT025 (grupowanie w v2.3)
code: code/b1_t2_contour_069.jl, code/cfg069_*.dat, code/b1_t2_069_analysis.py (wszystko zatwierdzone przed przebiegiem; sterownik sprawdzony parserem, analiza próbą na danych syntetycznych)
claim_ceiling: NATIVE_CONDITIONAL_SHIFT / INTERPRETATION_CONDITIONAL_ON_T1 / NO_PAPER_ERROR_CLAIM / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_069: B1 Q-B, test T2 — natywny kontur przy połówkowej normalizacji ładunkowej (E5) wobec oryginału

**Rola:** Badacz. Przebieg jest autoryzowany. Interpretacja wyniku zależy od T1 (semantyka tabeli 100×5; wykonawca Mech-S9). Przy T1-PERSTATE przesunięcie T2 opisuje wariant niefizyczny.

## Ramiona i siatki

- **Kod.** Autorów, `d395183`, `(last ∘ magic)`; obserwabla Y_C przy T_nuc, próg 0.251 (χ² = 4).
  - `orig`: bez zmian.
  - `e5`: łatka Mech-S6 bez zmian (π±, K±, p+p̄, n+n̄ × ½; K⁰_L bez zmian), czyli wariant E5 z REVIEW_038.
- **Masy.** j = 22, 28, 38, 51, 62, 90 (1.121, 1.330, 1.767, 2.556, 3.494, 7.743e9 g); obiekty mas z listy autorów. β = `ArbFloat(10.0^lb)`, lb zaokrąglone do 6 miejsc.
- **Siatki przy tolerancji domyślnej** (`code/cfg069_*_default.dat`): 17 punktów co 0.02 dex, ±0.16 dex.
  - Środek dla `orig`: korzeń archiwum autorów.
  - Środek dla `e5`: korzeń archiwum plus przesunięcie z REVIEW_038.
  - Razem 204 wywołania.
- **Kontrola tolerancji** (`code/cfg069_*_1e-4.dat`): j = 22 i 62, oba ramiona, 7 punktów co 0.04 dex, `reltol=1e-4`, `abstol=1e-7`. Razem 28 wywołań.
- **Jedno dozwolone rozszerzenie:** jeśli w oknie nie ma przejścia przez próg, okno tej serii poszerza się raz o ±0.16 dex. Fakt odnotowuje się w RUNLOG.

## Metody i kryteria (zamrożone)

Korzeń liczę metodami z REVIEW_065, skopiowanymi bez zmian: M_B (kwadratowa, 4 punkty), M_C (liniowa) i **M_D (prosta OLS z 7 punktów; główna)**. Przesunięcie D_j = korzeń(e5) − korzeń(orig), metodą M_D przy tolerancji domyślnej.

| werdykt | kryterium |
|---|---|
| **W** | wszystkie 6 wartości D_j ∈ [+0.20, +0.35] dex: W-PASS; w przeciwnym razie W-FAIL; brak korzenia: W-INCOMPLETE |
| **ORD** | D_90 ≥ D_22: ORD-PASS, w przeciwnym razie ORD-FAIL |
| **TOL** | \|D_j(1e−4) − D_j(domyślna)\| ≤ 0.03 dla j = 22 i 62: TOL-STABLE, w przeciwnym razie TOL-UNSTABLE |

**Opisowo:**
- rozrzut metod i błąd standardowy OLS;
- liczba zmian znaku w serii, czyli szarpanie;
- D_j − przesunięcie z REVIEW_038;
- D_j − log₁₀2;
- korzeń `orig` minus korzeń archiwum autorów.

Niedobór względem log₁₀2 jest miarą udziału efektów niehadronowych. To pomost do pytania Q-A, bez nowych przebiegów.

## Granice

- Wynik W-PASS potwierdza natywnie i w skalibrowanym środowisku pomiar z REVIEW_038. Nie dowodzi, że normalizacja autorów jest błędna; to rozstrzyga T1 plus T3.
- To nie jest fizyczna granica PBH, bo E4 (hadronizacja poniżej 1e9 g) pozostaje HOLD.
- Wyjścia powstają poza repozytorium i są kopiowane po zakończeniu. Bez `git stash`.
