---
artifact_id: IW_BADACZ_B1_NOPBH_BACKGROUND_AND_GEC_REVIEW_120_20261123
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel przebiegów natywnych B1
created_at: 2026-11-23
document_type: REVIEW (wynik PREREG_119, commit c4c9842)
authorization: Moderator 23 XI 09:22 („Najpierw A”)
answers: DAX-S10 ROT003–005, AUD3 ROT025–026, REC14 ROT006–007 (tło bez PBH); EKS1 ROT024–027, REC14 ROT002 (G_EC+)
claim_ceiling: NUMERYCZNY w modelu kodu Wu–Xu [▷] / NO_PBH_BOUND / NO_AUTHOR_ERROR_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_120: natywne tło bez PBH w kodzie Wu–Xu i bramka G_EC+(a)

## 1. Wynik

- Bramki 5/5 PASS: G_RUN, G_AD, G_CONV, G_REP, P_G3.
- Predykcje: 6/7 PASS; P0d FAIL (§3).
- Powtórki: analiza bitowo identyczna; dwa przebiegi natywne (code/r9/j22, code/def/j62) bitowo identyczne w eksportach.
- Dane: `data/run119/`, SHA w manifeście.

### A. Tło bez PBH (β = 0)

| wielkość | code r9 (j22 / j62) | ad r9 (j22 / j62) | odniesienie | wynik |
|---|---|---|---|---|
| Q(T_nuc)/Q(10 MeV) | 1.146807 / 1.146797 | 1.000046 / 1.000030 | 1.146782 (DAX ROT003, AUD3 ROT025) | P1 PASS, G_AD PASS |
| Δt(10 MeV → T_nuc) | 214.951 / 214.953 s | 208.851 / 208.852 s | stosunek 1.029223 (DAX, AUD3) | P2 PASS: 1.029208 / 1.029214 |
| Y | 0.2447523 / 0.2447523 | 0.2478218 / 0.2478222 | 0.244893 / 0.247964 (REC14 ROT007) | P0 PASS |
| Y_ad − Y_code | +0.0030696 / +0.0030698 | | +0.0030704 (DAX ROT004, REC14 ROT007) | P3 PASS |

- Natywny kod odtwarza ustalenia źródłowe DAX i AUD3 (entropia, zegar) oraz ΔY z modeli zredukowanych do ~2e-5. Ustalenie i pierwszeństwo należą do nich; to natywne potwierdzenie z innej rodziny modeli.
- Wspólne przesunięcie: natywne Y jest niższe od modelu zredukowanego o 1.41e-4 w obu ramionach (X_n przy T_nuc niższe o 5.6e-5), więc ΔY się nie zmienia. Źródła nie identyfikowałem; kandydaci to interpolacja Y autorów, `from_ρ_to_T` albo zaokrąglenia w modelu zredukowanym.
- Solwer autorów (ustawienia skanu, 167–188 kroków):
  - Y_code = 0.244987 / 0.245178, czyli błąd względem r9 +2.4e-4 / +4.3e-4;
  - w ramieniu ad −9.5e-4 przy j62;
  - Q(T_nuc)/Q(10 MeV) w code = 1.14644 / 1.15309.
  Przy σ = 0.003 z χ² autorów błąd Y w code to 0.08–0.14σ.

Wartości eksportowane (code r9, j22; w nawiasie ad r9, j22):

| T [MeV] | t [s] | X_n | Q/Q(10 MeV) |
|---|---|---|---|
| 10 | 0.0074491 (0.0074242) | 0.467723 (0.467723) | 1 (1) |
| 1 | 0.74603 (0.74593) | 0.254614 (0.254619) | 1.000281 (1.000070) |
| 0.5 | 3.0786 (3.0753) | 0.184561 (0.184618) | 1.002677 (1.000079) |
| 0.25 | 13.757 (13.661) | 0.152623 (0.152858) | 1.019525 (1.000106) |
| 0.1 | 122.61 (119.21) | 0.122645 (0.123587) | 1.117137 (1.000071) |
| T_nuc = 0.078185 | 214.96 (208.86) | 0.109033 (0.110250) | 1.146807 (1.000046) |

ρ(T) jest w obu ramionach tą samą funkcją; różni się tylko a(T) i t(T). Pełne ślady (3000 punktów, T ≤ 30 MeV) są w `dense_*.csv.gz`. Kod ma jedną temperaturę, więc T_ν nie występuje.

### B. G_EC+(a): normalizacja utraty masy

- R(M) = f_BH/f_code = 0.58175, stałe do 1e-6 w całym oknie 1 g ≤ M ≤ 1e10 g (371 mas tablicy). W tym oknie obie normalizacje są nasycone wszystkimi stopniami swobody SM. P_G1 PASS.
- Czasy życia (całka ∫M²/f dM):

| | τ_BH / τ_407 | τ_BH / τ_code | τ_code(wzór) / τ_zrzut |
|---|---|---|---|
| j22 | 1.0038 | 1.7189 | 0.9978 |
| j62 | 1.0038 | 1.7189 | 0.9973 |

  BlackHawk v2.3 ma więc normalizację standardową (do 0.4%), a kod traci masę 1.719× szybciej. P_G3 PASS: ekstrakcja f_code zgadza się z natywnymi zrzutami do 0.3%.
- Moc niesiona przez widma pierwotne 090 (wejście tablic hadronowych): P_spec/P_fM = 0.988 przy maksymalnym odchyleniu 1.19% dla 46 mas w [2e9, 1e11] g. P_G2 PASS. Przy 1e9 g wynosi 0.960 z powodu obcięcia siatki przy 1e5 GeV (udział brzegowy 0.157).

**Odczyt [▷].** W kodzie szybkości hadronowe na jedną czarną dziurę i jednostkę czasu odpowiadają standardowej emisji BlackHawk, ale czarna dziura żyje 1.719× krócej. Całkowita liczba hadronów na jedną PBH wynosi więc 0.582 wartości zgodnej z bilansem energii, o ile tablica hadronowa jest energetycznie spójna z widmami pierwotnymi; to jest G_EC+(b), wciąż otwarta. Przesłanka EKS1 dla STD_A trzyma się po stronie normalizacji. Normalizacja z samego BlackHawk (N_BH × 0.58175) różni się od wersji „407 s” o 0.6%. To nie jest teza o błędzie granicy autorów: potrzebne są G_EC+(b) i natywny STD_A.

## 2. Ocena konfiguracji

- Ramiona precyzyjne (r8, r9) kosztowały ≤ 2 min na przebieg i były konieczne. Na solwerze autorów P1 przy j62 wyszedłby poza tolerancję (1.15309), a ΔY przy j62 wyniósłby 0.0017 zamiast 0.0031.
- Pilot tylko czasowy i ślepy test dymny eksportu zadziałały: liczby testowane predykcjami zobaczyłem dopiero po zamrożeniu.
- Wniosek dla STD_A: dodać ramię r8 obok solwera autorów, bo błąd numeryczny Y skanu (do ~4e-4 w code) jest tego samego rzędu co część badanych efektów.

## 3. Uczenie systemu

- **P0d FAIL; origin_failure_mode: NOISE_REFERENCE_FROM_DIFFERENT_SOLVER_PATH.** Odniesienie dla Y na solwerze autorów przy β = 0 wziąłem z przebiegów przy β = 1e-30 (0.24465–0.24479). Zakładałem, że błąd numeryczny nie zależy od ścieżki kroków. Gruby solwer adaptacyjny (~170 kroków na ~39 e-foldów) ma jednak błąd zależny od ścieżki: przy β = 0 wynosi on +2.4e-4 / +4.3e-4, przy β = 1e-30 około −1e-4…+0.4e-4. Łatka: odniesienia szumu brać tylko z identycznej konfiguracji, a gdy jej brak, dodawać ramię precyzyjne zamiast zgadywać.
- **Obserwacja (origin_observation).** Udokumentowany szum progów (~0.03 dex) pochodzi z replik przy PBH. Nie przenosi się automatycznie na przebiegi bez PBH ani na inne zmiany ścieżki solwera.

## 4. Dalej

- G_EC+(b): budżet energii tablicy hadronowej wobec widm pierwotnych (PYTHIA, wybór autorów).
- Potem PREREG natywnego STD_A: N_BH × 0.58175 przy j22, j62 i j16–j22, z ramieniem r8.
- Nowy wynik (B: R = 0.58175, τ_BH/τ_code = 1.7189, P_spec/P_fM) wymaga I1 spoza rodziny Claude, np. REC14 albo AUD3.
