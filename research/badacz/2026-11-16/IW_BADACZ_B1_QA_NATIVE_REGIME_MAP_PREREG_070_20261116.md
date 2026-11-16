---
artifact_id: IW_BADACZ_B1_QA_NATIVE_REGIME_MAP_PREREG_070_20261116
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel natywny B1
created_at: 2026-11-16
document_type: PREREGISTRATION (gotowy do wykonania; przebieg CZEKA na autoryzację Moderatora)
responds_to: decyzja Moderatora 16 XI 16:47 (Q-A i Q-B równolegle); EKS1 ROT011 (GAP-003); REVIEW_067 (próg szumu); PROPOSAL_068
code: code/b1_t2_contour_069.jl (ten sam sterownik co T2, ramię orig, tolerancja domyślna), code/cfg070_A_indomain.dat, code/cfg070_B_offscan.dat, code/b1_qa_070_analysis.py (zatwierdzone przed przebiegiem; analiza sprawdzona na danych syntetycznych)
claim_ceiling: NATIVE_DESCRIPTIVE_REGIME_MAP / NO_PHYSICS / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_070: B1 Q-A — natywna mapa reżimów (liniowy, pośredni, nasycenie)

**Rola:** Badacz. Przebieg wymaga osobnej autoryzacji Moderatora. Autoryzacja z 16 XI obejmuje tylko T1 i T2.

## Pytanie operacyjne

Dla mas j = 22, 28, 38, 51, 62, 90 i obserwabli X_n(T0) (pierwotnej, wg Mech-S9 ROT014; pomocniczo Y_code, porównywalnej z EKS1):
- czy natywny opis daje **stabilne** etykiety reżimu w domenie skanu autorów, czyli tam, gdzie numerycznie da się je rozróżnić;
- czy reżim nasycenia pojawia się po wyjściu poza domenę (opcja (a) z GAP-003)?

## Siatki

- **A, w domenie:** baza SBBN (log₁₀β = −30, jak w REVIEW_053/064) oraz log₁₀β od −20.0 do −17.0 co 0.1, czyli 6 × 32 = 192 wywołania.
- **B, OFF-SCAN:** j = 19, 22, 24 (1.03, 1.12, 1.19e9 g); baza SBBN oraz log₁₀β od −16.9 do −15.0 co 0.1, czyli 3 × 21 = 63 wywołania. Wartości β wychodzą do 100× ponad β_max skanu autorów i są oznaczone jako OFF-SCAN.
- **Koszt:** 255 wywołań po ok. 4.4 s, ok. 10 min na 2 rdzeniach.

## Metoda (zamrożona w `code/b1_qa_070_analysis.py`)

- **Definicje:** ΔX = X − X_SBBN. Lokalne nachylenie s to OLS ln ΔX na ln β w oknie 5 węzłów (0.4 dex).
- **Szum:** σ_X = 1.4e−5 na punkt, z REVIEW_067. Pomiar pochodzi z jednego punktu; przeniesienie na inne masy to jawne założenie.
- **Rozdzielczość:** węzeł jest rozdzielczy, jeśli ΔX ≥ 1e−3 w całym oknie; wtedy σ_s ≲ 0.05.
- **Etykiety:** LINEAR przy s ≥ 0.9, SATURATION przy s ≤ 0.3, pomiędzy INTERMEDIATE. Próg 0.3 jak u EKS1.

## Przewidywania (z analizy archiwum EKS1 ROT011)

Natywne dane to niezależna produkcja liczb, ale pomysł analizy pochodzi od EKS1.

| | kryterium |
|---|---|
| **P-A1** | siatka A: żaden rozdzielczy węzeł nie ma s_X ≤ 0.3 w żadnej z 6 mas, czyli w domenie nie ma nasycenia |
| **P-A2** | s_Y w węźle log₁₀β = −17.2 dla j = 22, 28, 38 mieści się w [0.35, 0.70] |
| **P-A3** | s_Y w węźle log₁₀β = −18.2 dla j = 22, 28, 38 mieści się w [0.75, 1.05] |
| **B** | eksploracyjnie, bez przewidywania: pierwszy rozdzielczy węzeł SATURATION, jeśli wystąpi |

## Granice i znaczenie

- Jakościowe przejście od reżimu liniowego do nasycenia w odpowiedzi BBN na wstrzyknięcie hadronów jest znane z literatury (m.in. astro-ph/9908160). Wkład Q-A to **stabilna natywna mapa z jawną niepewnością**: sufit to REPRODUCIBILITY albo MATURE-APPLICATION, nie nowość.
- **Pomost do Q-B:** niedobór przesunięcia E5 (T2) względem log₁₀2 mierzy udział efektów niehadronowych przy konturze. Zestawienie z mapą s idzie do REVIEW wspólnego, bez nowych przebiegów.
