---
artifact_id: IW_BADACZ_B1_SECTION_F_ONE_PAGE_DRAFT_140_20261126
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel B1
created_at: 2026-11-26
document_type: SECTION_F_ONE_PAGE_DRAFT (protokół 30-dniowy IW_NASH_30_DAY_EXTERNAL_RESULT_DECISION_PROTOCOL_001_20261113, §F; termin 13 XII)
decision_basis: Moderator 25 XI 14:57 („tak przyjmuję”): STD_A jako główny brief B1, Q-B jako sekcja warunkowa
claim_ceiling: PROPOSAL / labels and CLOSED are Moderator decisions / NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# B1 §F: jedna strona (projekt na 13 XII)

| pole | STD_A (wynik główny) | Q-B (sekcja warunkowa) |
|---|---|---|
| dokładne pytanie | O ile przesuwa się próg β(M) w publicznym kodzie Wu–Xu, gdy zegar parowania (geometryczna optyka, Eq. 2.10) zrównać z normalizacją widm greybody (BlackHawk f(M)), przy niezmienionym źródle hadronów? | O ile przesuwa się próg, gdy grupową stawkę hadronów rozdzielić na stany ładunkowe zamiast wstrzykiwać ją do każdego stanu? |
| źródło niezmienne | Wu–Xu d395183, `main-scan.jl` l. 80; BlackHawk v2.3 `fM.txt`; arXiv:2509.05618v3 | to samo; `hadrons_from_PBH.dat`; tablice BBN PYTHIA |
| data zamrożenia | PREREG_123 (40c6423, 23 XI) | G1: PROPOSAL_068 / PREREG_069 (16 XI) |
| pierwszeństwo | kierunek EKS1 (DIR-010); pomiar natywny Badacz (REVIEW_120–126) | E5 Badacz (31 X); grupowanie Mech-S9 |
| prereg | PREREG_123, PREREG_125, DRAFT_127 §3 (H2) | PREREG_069, T1 Mech-S9 |
| wykonywalność | natywna Julia, Manifest autorów | to samo |
| dane | research/badacz/2026-11-23, research/mech-s11/2026-11-25 | research/badacz/2026-11-16 |
| poprawność | Δ(j22) = −1.384 i Δ(j62) = −0.244 dex; pierwiastki std przy 9.45e8–1.08e9 g, gdzie base nie ma pierwiastka w siatce; wynik odporny na kontynuację źródła (s ∈ [−1.5, −1.0]) | +0.272…+0.301 dex w 6 masach; po przeniesieniu na sieć +0.26…+0.30 |
| niepewność | szum pierwiastków 0.001–0.021 dex; progi bezwzględne objęte STOP A (źródło poniżej 1e9 g), STOP B (mapa Y_P), G_DEP | przesunięcie względne odporne; progi bezwzględne nie (SYNTH_087) |
| dojrzały gospodarz | Page 1976; MacGibbon 1991; Baldes et al. 2020, dod. A (czynnik ok. 2); Cheek et al. 2022; Boccia et al. 2025 (zegar greybody, bez hadronów) | Reno–Seckel 1988; Bianco et al. 2026 (wydajności per stan) |
| niezależne I1/I3 | H1: Mech-S11 ROT009 (natywnie, 56/56) + AUD4 ROT007 i REC15 ROT011 PASS. H2: Mech-S11 ROT012, 3/3 punktowo i 2/3 przedziały. Brief v2: REC15 ROT012 | T2R Mech-S10, 68/68 bitowo; semantyka (T3) OPEN |
| ważny null | replika (nie wystąpił); relabeling (nie wystąpił); normalizacja q zgodna z geometryczną optyką (sprzeczna z Fig. 2 autorów) | T3: konwencja grupowa zamierzona razem z przekrojami grupowymi, a więc spójna |
| rzeczywista nowa informacja | W modelu autorów przesunięcie jest przewidywalne: przeskalowanie zegara M′ = 1.198·M oraz czynnik R^c w β, gdzie c ≈ 0.92 wynika z tablicy źródła. Wyjaśnia to dużą wartość Δ przy stromej ścianie. | W kodzie siedzi konwencja czynnika 2 warta ok. +0.3 dex; jej status zależy od semantyki |
| alternatywne wyjaśnienie | świadome przybliżenie autorów; wtedy niespójność zegara i widm pozostaje, ale wymaga ich potwierdzenia | konwencja odziedziczona po Kohri 2001 z przekrojami grupowymi |
| produkt | brief v3 (IW_BADACZ_B1_RESULT_BRIEF_STD_A_V3_139_20261126), poziom modelu | sekcja 6 briefu |
| decyzja i stop | **Proponowana etykieta: B1-SOURCE-VALIDATED-MATURE-APPLICATION**, z zakresem: przesunięcie i mechanizm w modelu kodu. ORIGINAL-SCIENCE nie wchodzi w grę, bo dojrzały gospodarz zna czynnik. STOP A pozostaje HOLD (test generatora niedopuszczalny, REVIEW_132). Do 13 XII żadnych dalszych przebiegów B1. | **B1-HOLD_SOURCE** dla interpretacji, **B1-REPRODUCIBILITY-ONLY** dla pomiaru. T3 nie da się zamknąć bez autorów (kontakt wstrzymany). |

**Decyzja zbiorcza według §D protokołu, propozycja:** wariant (2), czyli wynik użyteczny, ale nie nowy. Zachowujemy wkład odtwarzalnościowy i wstrzymujemy wydatki na twierdzenia teoretyczne w B1. Etykiety, zamknięcie i EXEC_SIGN należą do Moderatora.

**Otwarte do 13 XII (bez przebiegów):** ewentualne potwierdzenie briefu v3 przez REC15 oraz odczyt BW przez następcę KN.

NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
