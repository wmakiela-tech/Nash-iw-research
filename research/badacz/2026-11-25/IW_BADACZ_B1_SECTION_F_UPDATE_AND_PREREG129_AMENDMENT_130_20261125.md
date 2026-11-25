---
artifact_id: IW_BADACZ_B1_SECTION_F_UPDATE_AND_PREREG129_AMENDMENT_130_20261125
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel B1
created_at: 2026-11-25
document_type: DECISION_DRAFT_DELTA (do DRAFT_127, commit 74d04e0) + PREREG_AMENDMENT A1 (do PREREG_129, commit 15a4761; przed jakimkolwiek wynikiem)
responds_to: Mech-S11 ROT009, ROT012; AUD4 ROT007, ROT008; REC15 ROT001; PRF15 ROT007; INT11 ROT007; LT11 ROT006; M16 ROT028; EKS1 ROT029 (pozostałe raporty prywatne cytuję po ID)
claim_ceiling: PROPOSAL / MODEL_CONDITIONAL / NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# §F, delta 130: STD_A ma niezależne wykonanie i referee; poprawka A1 do PREREG_129

**Rola:** Badacz. Zmieniam tylko pola, które się zmieniły. Reszta DRAFT_127 z errata 128 obowiązuje dalej.

## 1. STD_A: zmienione pola §F

| pole | było (DRAFT_127/128) | jest |
|---|---|---|
| niezależne I1/I3 | pierwiastki liczyła tylko rodzina Claude | **H1:** natywne wykonanie Mech-S11 ROT009 (GPT), 56/56 wywołań, bramki 5/5 PASS, Δ(j22) = −1.3837963853 i Δ(j62) = −0.2437802072, zgodne co do bitu; ograniczony referee AUD4 ROT007 PASS, z przedziałami bez interpolacji: Δ(j22) ∈ [−1.4375, −1.3125], Δ(j62) ∈ [−0.3125, −0.1875]. Wykonanie nieślepe, na moim driverze, czyli weryfikacja wykonania, a nie niezależna fizyka. **H2:** natywny test prospektywny Mech-S11 ROT012 przy 3 zamrożonych masach daje 3/3 PASS punktowo i 2/3 dla pełnego przedziału; również nieślepy. |
| ważny null | (a) replika, (b) relabeling, (c) normalizacja q | (a) nie wystąpił; (b) nie wystąpił w 3 punktach. Pozostaje (c) oraz STOP A (test PREREG_129), STOP B i G_DEP. |
| rzeczywista nowa informacja | prawo post hoc std(M) ≈ base(M·R^(−1/3)) + c·log₁₀R | Natywne c przy masach testowych: 0.907 / 0.943 / 0.936 (z pierwiastków Mech-S11 i węzłów base REC14). Źródłowe c_eff z tablicy q (REC14 ROT016) leży w paśmie 0.900–0.938. Zgodność mieści się w szumie pierwiastków (σ_c ≈ σ_root/0.235, czyli 0.005–0.09). Porównanie wykonane po zobaczeniu wyników. **Wniosek [▷]:** w modelu autorów STD_A da się przewidzieć: to przeskalowanie zegara o R^(1/3) plus równoważność tempa wstrzykiwania. Mechanizm jest zrozumiały, więc potwierdza sufit MATURE-APPLICATION i nie wskazuje nowości. |
| zgodność między instrumentami | REVIEW_126: kontynuacja s = −1.3 daje −0.039 / −0.003 dex | M16 ROT028 (instrument liniowy, niezależny) przy ogonie z artykułu (M^−1.3) wobec kodu (M^−1.2) daje −0.0381 / −0.0027 dex. Skala zgodna. 88% różnicy powstaje poniżej 1e9 g, ale przy T_H < 100 TeV. |
| decyzja | sufit MATURE-APPLICATION; brak I1 spoza Claude i referee | Sufit bez zmian. Bramki SOURCE (wykonanie) i INDEPENDENT REFEREE (zakres: przesunięcie w modelu kodu) są spełnione dla przesunięcia Δ, nie dla progów bezwzględnych. Do briefu wchodzi wyłącznie przesunięcie w modelu i mechanizm. Progi bezwzględne i ściana masowa czekają na STOP A (PREREG_129), STOP B i G_DEP. |

**Q-B: bez zmian.** T3 nadal SEMANTICS_OPEN. AUD4 ROT008 zastrzega: dojrzały mechanizm nie dowodzi, że konkretny wynik ilościowy jest już znany. Utrzymuję więc brief odtwarzalnościowy MODEL_CONDITIONAL, bez promocji nowości. Zastrzeżenie to dotyczy także STD_A.

**Eliminacja (stan na teraz):** żaden kandydat nie został wyeliminowany.
- STD_A ma dziś więcej spełnionych bramek niż Q-B: semantykę zamyka tekst autorów, I1 i referee są PASS, mechanizm jest wyjaśniony.
- Q-B jest zablokowany przez T3, a T3 bez autorów się nie domknie.
- **Propozycja [▷] dla Moderatora:** STD_A jako główny brief B1, Q-B jako warunkowa sekcja odtwarzalnościowa. Decyzja należy do Moderatora.

## 2. PREREG_129: poprawka A1 (przed wynikiem; w repozytoriach i na Slacku nie ma jeszcze żadnego wyjścia PREREG_129)

Źródła: REC15 ROT001, PRF15 ROT007, INT11 ROT007, LT11 ROT006. Główna reguła decyzji z §4 PREREG_129 zostaje, ale z dwiema naprawami.

**A1.1 G_COV (naprawa znakowa).** Zamiast udziału netto liczymy udziały ze znakiem dla grup i binów poniżej M_cov:
- P = suma wkładów dodatnich, N = suma modułów ujemnych, oba znormalizowane do tego samego W0;
- pary pionów grupujemy przed wzięciem modułu.

**A1.2 Kryterium łączne (zastępuje „|Δ| ≤ 0.03 i G_COV ≤ 7%” jako warunek PASS).**
- Obszar dopuszczalnych mnożników ogona: [0.5, 2]. Stąd a = P/2 + N oraz b = P + N/2.
- PASS, gdy w każdym zegarze i każdym ramieniu: 10^(−0.03) + a ≤ 10^Δ_src ≤ 10^(0.03) − b.
- Raportujemy przedział [log₁₀(10^Δ − a), log₁₀(10^Δ + b)] oraz osobno stary warunek („PASS_PRIMARY”), dla przejrzystości.
- Dla orientacji (PRF15/REC15, wiersze 1e8 g): okno dla Δ to ok. [−0.018, +0.013] (f_BH) i [−0.014, +0.006] (GO).
- Moja predykcja P2 (+0.01…+0.07) zostaje bez zmian. Oznacza to, że **przy nowym kryterium spodziewam się raczej FAIL niż PASS**. Zapisuję to teraz, przed wynikiem.

**A1.3 Prośby do wykonawcy (raportowane wielkości, nie bramki):**
- liczniki tylko z zaakceptowanych zdarzeń: sprawdzić, czy przed odrzuceniem zdarzenia ze statusem −23 nie wyciekają liczby z prefiksu (INT11 ROT007);
- ΣN oraz ΣN·Nᵀ dla wszystkich grup i stanów, na każdy węzeł i ramię, żeby policzyć kowariancje.

Pozostałe elementy PREREG_129 (źródło, węzły, ramiona, G_E, G_Q, G_QS, G_OVL, splot) bez zmian.

**origin_failure_mode** (przyjęty od REC15 i LT11): `NET_SIGNED_SHARE_USED_AS_COVERAGE`, czyli udział netto ze znakiem użyty jako miara pokrycia. **Reguła:** bramka pokrycia dla odpowiedzi ze znakiem używa P i N oraz kryterium łącznego, a nie udziału netto.

NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
