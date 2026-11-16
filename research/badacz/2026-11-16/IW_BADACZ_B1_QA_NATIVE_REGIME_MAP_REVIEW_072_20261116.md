---
artifact_id: IW_BADACZ_B1_QA_NATIVE_REGIME_MAP_REVIEW_072_20261116
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel natywny B1
created_at: 2026-11-16
document_type: REVIEW
responds_to: PREREG_070 (fd68539); REVIEW_071 (T2, 2390d0d); EKS1 ROT011 (GAP-003)
authorization: Moderator 16 XI 2026 17:39 („Autoryzuję”), zapis w RUNLOG przed przebiegiem (ed1910a)
data: data/qa_A.csv, data/qa_B.csv, data/analysis070.json (skrypt preregu), data/qa_run_record.json
claim_ceiling: NATIVE_DESCRIPTIVE_REGIME_MAP / NO_PHYSICS / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
external_audit: WYMAGANY (spoza rodziny Claude; zwłaszcza siatka B)
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_072: B1 Q-A — natywna mapa reżimów i pomost do T2

**Rola:** Badacz. Wnioski mają status [▷].

## Przebieg

- **Czas:** 16 XI, 17:40–17:57 (zegar kontenera). Siatki A (192 wywołania) i B (63) liczone równolegle, obie ze statusem 0.
- **Kod:** sterownik T2 bez zmian, ramię oryginalne, tolerancja domyślna. Odstępstw brak.

## Werdykty preregu

| werdykt | wynik |
|---|---|
| **P-A1** (w domenie żaden rozdzielczy węzeł nie ma s_X ≤ 0.3) | **PASS** |
| **P-A2** (s_Y przy −17.2 w [0.35, 0.70] dla j = 22, 28, 38) | **PASS** 3/3 (0.42, 0.45, 0.46) |
| **P-A3** (s_Y przy −18.2 w [0.75, 1.05]) | j28 **PASS** (0.92), j38 **PASS** (0.93), j22 **UNRESOLVED** (ΔX = 4.7e−4 < 1e−3) |
| **B**, eksploracyjnie | pierwszy rozdzielczy węzeł SATURATION: **log₁₀β = −16.7** dla j = 22 i j = 24; j = 19 bez etykiety (ΔX < 1e−3) |

## Mapa (s_X na węzłach rozdzielczych; pełne dane w `analysis070.json`)

| j | m [g] | korzeń konturu (T2) | s_X przy konturze | reżim przy konturze | pierwszy węzeł z s_X < 0.9 | D(E5) − log₁₀2 (T2) |
|---|---|---|---|---|---|---|
| 22 | 1.121e9 | −17.22 | 0.44 | pośredni | −17.6 | −0.029 |
| 28 | 1.330e9 | −18.36 | 0.95 | liniowy | −18.1 | −0.025 |
| 38 | 1.767e9 | −19.01 | 0.98 | liniowy | −18.1 | −0.025 |
| 51 | 2.556e9 | −19.30 | 0.99 | liniowy | −18.1 | −0.008 |
| 62 | 3.494e9 | −19.39 | 1.00 | liniowy | −18.1 | −0.003 |
| 90 | 7.743e9 | −19.37 | 0.99 | liniowy | −17.9 | −0.000 |

**Siatka B (OFF-SCAN, β do 1e−15):** ΔX dochodzi do plateau.

| j | m [g] | plateau ΔX | położenie maksimum | ΔX przy log₁₀β = −15.2 |
|---|---|---|---|---|
| 19 | 1.03e9 | 7.3e−4 | −15.6 | 7.2e−4 |
| 22 | 1.12e9 | 3.8e−3 | −16.0 | 3.7e−3 |
| 24 | 1.19e9 | 8.5e−3 | −16.0 | 8.3e−3 |

Nachylenie maleje do ok. 0, a powyżej plateau lekko spada (s_X ≈ −0.03).

## Co z tego wynika [▷]

1. **Brak nasycenia w domenie skanu autorów potwierdza się natywnie** (GAP-003 EKS1).
   - Dla lekkich mas nasycenie zaczyna się już ok. 0.3 dex powyżej β_max autorów.
   - Pełne rozróżnienie trzech reżimów wymaga więc wyjścia poza domenę (opcja (a) EKS1), co Moderator autoryzował dla trzech mas.
2. **Kontur autorów leży w reżimie liniowym dla m ≥ 1.33e9 g**, a w pośrednim tylko na lewej ścianie (j = 22, s ≈ 0.44).
3. **Pomost do Q-B:** j = 28 i 38 leżą w reżimie liniowym (s ≈ 0.95–0.98), a mimo to mają ten sam niedobór przesunięcia E5 (−0.025 dex) co j = 22 w reżimie pośrednim.
   - Niedobór względem log₁₀2 nie wynika więc głównie z nieliniowości odpowiedzi.
   - Wynika z części źródła, której E5 nie połowi: K⁰_L, pojedynczy stan bez partnera ładunkowego, albo z efektów niehadronowych. Udział tej części maleje z masą.
   - To wspiera hipotezę z REVIEW_038 o udziale K⁰_L. Nie jest testem tej hipotezy.
   - Przy T1-GROUPED nie zmienia to korekty: K⁰_L ma poprawną normalizację, więc zmierzone D jest właściwym przesunięciem.
4. **Plateau poza domeną:** lekkie PBH (≈ 1e9 g) wyparowują przy t ≈ 0.33 s, a poziom nasycenia rośnie stromo z masą (7e−4 → 8e−3 przy 1.03 → 1.19e9 g). Hipoteza [▷], niesprawdzona: wymuszona przez hadrony konwersja n↔p przed zamrożeniem oddziaływań słabych zostaje w dużej części wymazana, a pozostałość zależy od tego, jak blisko zamrożenia kończy się parowanie. Lekki spadek powyżej plateau może pochodzić z efektów tła (entropia, ekspansja). To wymaga osobnego pytania, nie interpretacji z tej siatki.

## Granice

- σ_X = 1.4e−5 zmierzono w jednym punkcie (REVIEW_067); przeniesienie na inne masy i na siatkę B jest założeniem.
- Siatka B leży do 2 dex poza zakresem skanu autorów. Kod liczy tam legalnie, ale autorzy tego obszaru nie walidowali.
- Odtworzyła to tylko rodzina Claude; potrzebny audyt zewnętrzny.
- Sufit: opis natywny, REPRODUCIBILITY albo MATURE-APPLICATION. Jakościowy obraz (liniowy → nasycenie) jest znany w literaturze.

## Powrót w trzech warstwach

- **Wynik:** P-A1 PASS, P-A2 PASS, P-A3 2/3 PASS i 1 UNRESOLVED. Nasycenie poza domeną od −16.7 (j = 22, 24). Kontur w reżimie liniowym dla m ≥ 1.33e9 g.
- **Konfiguracja:** równoległe Q-A i Q-B (decyzja Moderatora) dało pomost niedostępny osobno: niedobór E5 nie wynika z nieliniowości. Całość zajęła ok. 17 min obliczeń.
- **Uczenie:** próg rozdzielczości ΔX ≥ 1e−3 wykluczył j = 19 z etykiety mimo widocznego plateau. Ilustruje to koszt sztywnego progu, ale próg chronił przed przypisaniem etykiety szumowi, więc go nie zmieniam. Do przyszłych preregów: próg rozdzielczości wyprowadzać z σ_s, a nie z ΔX.
