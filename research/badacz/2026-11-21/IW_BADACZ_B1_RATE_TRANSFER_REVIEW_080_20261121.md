---
artifact_id: IW_BADACZ_B1_RATE_TRANSFER_REVIEW_080_20261121
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), autor PREREG_079
created_at: 2026-11-21
document_type: RESULT_REVIEW (wynik przebiegu zamrożonego PREREG_079; I1 zewnętrzne wymagane)
prereg: IW_BADACZ_B1_RATE_TRANSFER_PREREG_079_20261121 (Nash-iw-research@acb4567)
authorization: Moderator 21 XI 13:02 „Autoryzuję” (RUNLOG_20261121)
claim_type: NUMERYCZNY w modelach; etykieta NIE PRZYZNANA; liczby opisowe [▷]
claim_ceiling: NO_LABEL / NO_PBH_BOUND / NO_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_080: wynik PREREG_079 — `GATE_FAIL_NO_LABEL`

## 1. Wynik

- **Wykonanie:** 38/38 wywołań Julii (rc = 0), 43/43 przebiegów sieci (rc = 0), w 7 minut.
- **Etykieta według zamrożonej reguły: `GATE_FAIL_NO_LABEL`.** Trzy bramki nie przeszły (§2). Jedna z nich wykryła realne ograniczenie metody, dwie miały progi poniżej poziomu szumu. Ani `SHIFT_TRANSFERS`, ani `SHIFT_MODIFIED` nie zostają przyznane. Liczby w §3 są opisowe.

## 2. Bramki

| bramka | wynik | diagnoza |
|---|---|---|
| V1_NATIVE_REPRO | **PASS**, 38/38 bitowo | flaga hadronów nie zmienia solve; wszystkie natywne Y = T2 / qa_A |
| V2_RATE_CONSISTENCY | FAIL: o22 1.9% (PASS), e22 2.2% (> 2%); j62 nie dotyczy | **próg poniżej szumu metody kontrolnej.** Różnica wsteczna vs przednia na tych samych punktach daje rozrzut 5% (mediana). Mediana znakowana −1.5% mieści się w szumie. Nie świadczy o błędnych szybkościach, ale też ich nie potwierdza na poziomie 2% |
| V3_NET_ZERO | FAIL: \|ΔY\| = 6.2e-7 (j22) i 8.0e-7 (j62) przy szybkościach bazowych ~1e-12 s⁻¹ | **próg 1e-10 poniżej szumu solvera sieci.** Każda niezerowa funkcja dodana do RHS zmienia sekwencję kroków adaptacyjnych. Neutralność przy braku haka była bitowa (§7 preregu), ale z „prawie zerowymi” szybkościami bitowa już nie jest. 8e-7 to około 1.5e-4 sygnału |
| V4_NET_TOL | **PASS** (0.07%, 0.24%) | |
| V5_INTERP | **FAIL:** o22_n08 10.1%, o62_n08 1.95% | **realne ograniczenie metody (§4)** |

## 3. Liczby opisowe [▷] (bez etykiety; nie do cytowania jako wynik)

- **ρ = ΔY_net / ΔY_code (mediana z 9 węzłów; rozrzut):**
  - j22: orig 1.32 (1.25–1.39), E5 1.30 (1.26–1.34);
  - j62: orig 0.79 (0.78–0.86), E5 0.83 (0.80–0.94).
- **Przesunięcia:**

| j | D_code (9 węzłów) | D_code (T2, OLS7) | D_net | D_net − D_code |
|---|---|---|---|---|
| 22 | 0.264 | 0.272 | 0.324 | +0.060 |
| 62 | 0.297 | 0.298 | 0.284 | −0.013 |

- **Diagnostyka splotu liniowego** (G z REVIEW_078), węzeł n08:
  - **j62:** ∫G_code·s dt = 0.00610 wobec natywnego ΔY_code 0.00642 (−5%); ∫G_net·s dt = 0.00521 wobec transferu 0.00502 (+4%). Dla E5: −0.5% i +3.5%.
    - Dla j62 dwie niezależne metody, liniowy splot i nieliniowy transfer szybkości, zgadzają się więc w granicach 4–5%.
  - **j22:** ∫G_code·s = 0.029 wobec natywnego 0.0062. Liniowy splot zawodzi, bo G_code przy T ≥ 1.2 MeV to szum (REVIEW_078 §3).

**Interpretacja [▷], wyłącznie jako hipoteza do następnego preregu:**
- Dla j62 pełna sieć daje około **20% mniej** nadmiaru helu niż kod. Wynik jest spójny dwiema metodami, a przesunięcie D wygląda na przenośne (−0.013 dex).
- Dla j22 pełna sieć daje około **30% więcej** niż kod. Kierunek pasuje do trendu z REVIEW_078: R maleje ku wysokim T, więc kod wymazuje wczesne zaburzenia mocniej niż sieć. Wartość jest jednak niewiarygodna na poziomie ~10% z powodu V5. Przesunięcie +0.06 dex dla j22 może być w części artefaktem rozdzielczości.

## 4. Przyczyna realnej porażki V5: niedorozdzielony błysk końcowy

- Przy końcu parowania j22 szybkości rosną gwałtownie: r_{p→n} z 26 s⁻¹ w przedostatnim do 57 s⁻¹ w ostatnim żywym punkcie wyjściowym (T = 1.4878 MeV). W następnym punkcie (T = 1.4822 MeV) PBH już nie żyje.
- Ostatni przedział niesie tylko ~1.5% całki |s|·dt. Ponieważ jednak G rośnie stromo ku niższym T, jego wkład w ΔY_net jest rzędu 10%: usunięcie co drugiego punktu gubi szczyt błysku.
- Natywna siatka autorów (10000 punktów, Δln a ≈ 0.0035) nie rozdziela więc chwili śmierci PBH na potrzeby transferu.
- Rozrzut ρ między węzłami (±5% dla j22) ma prawdopodobnie to samo źródło: faza ostatniego żywego punktu względem chwili śmierci jest w każdym przebiegu inna (hipoteza; ostatni żywy punkt o22_n08 ma indeks nieparzysty, więc w kontroli co drugiego punktu wypada).
- W samym kodzie błysk całkuje jego solver, więc problem dotyczy tylko eksportu szybkości.

## 5. origin_failure_mode i reguły

- **`GATE_THRESHOLD_AT_NOISE_LEVEL` (trzecie wystąpienie po bramce S w PREREG_066).** Dotyczy V2 i V3.
  - **Reguła:** każdy próg numeryczny bramki ustalam a priori na ≥ 5× zmierzony lub oszacowany szum samej kontroli i zapisuję to oszacowanie w preregu.
  - Bramkę neutralności testuję tą samą ścieżką, którą idzie pomiar: z szybkościami bazowymi, a nie bez haka.
- **`SOURCE_EVENT_UNDER_RESOLVED_BY_OUTPUT_GRID`** (V5).
  - **Reguła:** przy transferze źródła z kodu natywnego sprawdzam z góry, jaki ułamek efektu przypada na najwęższą strukturę źródła (tu chwilę śmierci PBH), i dobieram próbkowanie tak, żeby kontrola co drugiego punktu zmieniała wynik o ≤ 1%.
- **Pozytywnie:** bramki zrobiły swoje. Wynik z niedorozdzielonym błyskiem nie dostał etykiety.

## 6. Następny krok (propozycja, wymaga decyzji Moderatora)

**PREREG_081:** te same 4 przypadki i ten sam plan, z trzema zmianami:
- **(a)** Eksport szybkości z próbkowaniem zagęszczonym przy śmierci PBH. Minimalna ingerencja w kod autorów: magic dodatkowo zwraca obiekt rozwiązania (zmiana tylko wyjścia). W ostatnich ~2% ln a przed śmiercią dodaję ≥ 20000 punktów.
- **(b)** Progi V2 i V3 ustalone a priori ponad zmierzony szum: V3 ≤ 1e-5 (≥ 12× szum 8e-7, < 0.2% sygnału); V2 zastąpione kontrolą całkową ΔX po przedziale aktywności, z progiem ≥ 5× szum.
- **(c)** V5 bez zmian (≤ 1%), na nowej siatce.

## 7. Audyt i proweniencja

- **I1 zewnętrzne:** REC13 lub AUD3, do danych i diagnozy bramek.
- **Kod:** `code/` z SHA-256 jak w PREREG_079 §3 (zweryfikowane 8/8 przed startem).
- **Dane w `data/`:**
  - podsumowania natywne;
  - wyniki sieci (`net079_raw.jsonl`);
  - szybkości przypadków kontrolnych (T ≤ 20 MeV, gzip);
  - SHA-256 wszystkich 38 pełnych zrzutów (91 MB, lokalnie; odtwarzalne bitowo, V1);
  - `analysis079.json`.
- **Środowisko:** Julia 1.12.3 (pakiety jak w T2), PRyMordial @725d8a8 z łatkami 077+079 (SHA wyniku b6bb5636…).
