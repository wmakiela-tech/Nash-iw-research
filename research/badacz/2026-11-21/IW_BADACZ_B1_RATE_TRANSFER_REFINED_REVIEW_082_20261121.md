---
artifact_id: IW_BADACZ_B1_RATE_TRANSFER_REFINED_REVIEW_082_20261121
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), autor PREREG_081
created_at: 2026-11-21
document_type: RESULT_REVIEW (wynik przebiegu zamrożonego PREREG_081; I1 zewnętrzne WYMAGANE)
prereg: IW_BADACZ_B1_RATE_TRANSFER_REFINED_PREREG_081_20261121 (Nash-iw-research@fbc91bf)
authorization: Moderator 21 XI 14:20 „Tak autoryzuję” (RUNLOG_20261121)
claim_type: NUMERYCZNY w modelach (przeniesienie natywnych szybkości kodu Wu–Xu do pełnej sieci PRyMordial) + INTERPRETACYJNY [▷] oddzielony
claim_ceiling: NO_PBH_BOUND / NO_PAPER_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN; status [▷] do zewnętrznego I1
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_082: wynik PREREG_081 — `SHIFT_TRANSFERS`

## 1. Wynik

- **Wszystkie 6 bramek PASS:**

| bramka | wynik |
|---|---|
| V1 | 38/38 natywnych Y = T2/qa_A |
| V2_EXACT | maks. błąd względny 1.8e-11 przy progu 1e-6; eksportowane szybkości są dokładnie członem hadronowym `evolution_system!` autorów |
| V3 | 6.2e-7 i 8.0e-7 przy progu 1e-5 |
| V4 | 0.03% i 0.10% |
| V5 | 0.23% i 0.19% przy progu 1%; w PREREG_079 było 10.1% i 1.95% |
| V6 | zagęszczenie zastosowane we wszystkich przebiegach |

- **Etykieta według zamrożonej reguły: `SHIFT_TRANSFERS`.**

| j | D_code (9 węzłów) | D_code (T2, OLS7) | D_net | D_net − D_code |
|---|---|---|---|---|
| 22 | 0.2643 | 0.2723 | 0.2706 | **+0.0063** |
| 62 | 0.2973 | 0.2981 | 0.2961 | **−0.0013** |

- **Odpowiedź na pytanie preregu:** przesunięcie progu z normalizacji ładunkowej (T2) przenosi się do pełnej sieci BBN z dokładnością lepszą niż 0.01 dex w obu masach. W tym modelu transferu korekta T2 nie zależy od problematycznego odwzorowania Y_C → Y_p.

## 2. Wielkość efektu: ρ = ΔY_net / ΔY_code

| przypadek | ρ (9 węzłów: zakres) | ρ w pierwiastku kodu orig |
|---|---|---|
| j22 orig | 1.308–1.349 | **1.316** |
| j22 E5 | 1.305–1.325 | — |
| j62 orig | 0.810–0.817 | **0.816** |
| j62 E5 | 0.806–0.821 | — |

- Przy tej samej historii konwersji pełna sieć daje dla j22 **~32% więcej**, a dla j62 **~18% mniej** nadmiaru helu niż odczyt Y_C kodu.
- Rozrzut między węzłami spadł po zagęszczeniu. Dla j22 max/min wynosi 1.031 (orig) i 1.015 (E5); w REVIEW_080 było 1.11 i 1.06.

**Kontrola krzyżowa dla j62 (diagnostyka liniowa z G z REVIEW_078):**
- ∫G_code·s dt = 0.00636 wobec natywnego ΔY_code 0.00642 (−0.9%);
- ∫G_net·s dt = 0.00542 wobec transferu 0.00524 (+3.5%).

Dwie niezależne metody, liniowa odpowiedź na kick i nieliniowy transfer szybkości, zgadzają się więc w granicach 1–4%. Dla j22 kontrola liniowa nie działa, bo G_code przy T ≥ 1.2 MeV to szum (REVIEW_078 §3).

## 3. Predykcje

| predykcja | wynik | status |
|---|---|---|
| P1: ρ(j62) ∈ [0.75, 0.95] | 0.816 | PASS |
| P3: `SHIFT_TRANSFERS` | tak | PASS |
| P4: rozrzut ρ j22 ≤ 1.04 | 1.031 / 1.015 | PASS |
| P5: ρ(j22) > 1.10 | 1.316 | PASS |

Zastrzeżenia:
- P1 i P3 nie były niezależnymi testami, bo widziałem liczby opisowe REVIEW_080 (ujawnione w preregu).
- P4 testowała moją diagnozę porażki V5 z PREREG_079 (niedorozdzielony błysk końcowy) i ją potwierdziła.
- Zgodność predykcji autora z wynikiem autora nie jest audytem.

## 4. Odchylenie techniczne DEV-1 (081)

- **Co się stało.** W pierwszym przebiegu sieci 8/43 zadań przerwała asercja „T not strictly monotone” w zamrożonym `net_rate_079.py`. W 7 z 38 plików szybkości (wszystkie o62 orig poza n04 i n06) siatka połączona zawierała jedną parę punktów o identycznej temperaturze Float64. To prawie pokrywający się punkt natywny i zagęszczony, które `unique()` na ArbFloat zachowało.
- **Poprawka.** `dedupe_rates_081.py` usuwa wiersz o T równym poprzedniemu, zastosowany jednolicie do wszystkich 38 plików: 7 plików, po 1 wierszu. Potem ponowiłem cały etap sieci: 43/43 rc = 0.
- Przed decyzją nie oglądałem wyników 35 udanych zadań. Zachowałem je jako `net081_raw_PREDEDUPE_8failed.jsonl`. Usunięty punkt jest fizycznie tym samym punktem, więc zmiana interpolacji jest pomijalna.
- Kod i dziennik są w `code/` i `data/`.

## 5. Interpretacja [▷] (do I1; nie zmienia sufitu)

1. **T2 jest odporne na odwzorowanie helu.** Względne przesunięcie β między normalizacją dosłowną kodu a normalizacją per stan (E5) jest takie samo w kodzie i w pełnej sieci, z dokładnością do 0.006 dex. Zastrzeżenie przyjęte przez LT9, KN15, INT10, PRF14 i AUD3, że „wzmocnienie k jest niezidentyfikowane”, nie dotyczy więc *względnego* wyniku T2. Dotyczy wartości bezwzględnych.
2. **Bezwzględny nadmiar helu jest w kodzie obciążony, zależnie od masy.** Dla j22 kod zaniża (ρ ≈ 1.32), dla j62 zawyża (ρ ≈ 0.82). Mechanizm jest spójny z REVIEW_078:
   - wczesne konwersje (j22 kończy parowanie przy ~1.49 MeV) kod wymazuje silniej niż sieć, czyli R < 1 przy wysokich T;
   - późne (j62, ~0.29 MeV) kod przelicza na hel przez 2X/(1−X) z nadmiarem, czyli R ≈ 1.1–1.3.
   - Wniosek, tylko kierunkowy: progi β w pełnej sieci byłyby dla j22 niższe, a dla j62 wyższe niż w kodzie. Liczby nie podaję, bo poziomy ρ·d0 wypadają poza 9-węzłowe siatki, a próg obserwacyjny i linia bazowa pozostają osobnymi problemami.
3. **Granice modelu transferu:**
   - gęstości hadronów pochodzą z trajektorii kodu, bez sprzężenia zwrotnego od X_sieci;
   - dopasowanie po T;
   - brak zmian ekspansji i entropii od PBH;
   - brak fotodysocjacji, hadrodysocjacji i E4;
   - jedna sieć (PRyMordial, mała sieć).
   - **To nie jest granica PBH ani twierdzenie o błędzie w artykule.**

## 6. Audyt (wymagany, zewnętrzny)

- **REC13 lub AUD3 (I1):** przeliczenie D i ρ z `data/` (podsumowania, `net081_raw.jsonl`), ocena DEV-1 i sprawdzenie, że bramki V2_EXACT i V5 mierzą to, co deklarują.
- **PRF14 (lub inna komórka z runtime, spoza rodziny Claude):** niezależny kod sieci (LINX lub AlterBBN) z tymi samymi szybkościami dla o22_n08 i o62_n08. Pliki są w `data/`, T ≤ 12 MeV. Cel: sprawdzić, czy ρ i ΔY_net nie są artefaktem PRyMordial.
- Audyt Claude nad Claude nie jest zewnętrzny. Do czasu I1 status [▷].

## 7. Proweniencja

- **Kod:** SHA-256 jak w PREREG_081 §1, zweryfikowany przed startem. Dodatkowo `dedupe_rates_081.py` (DEV-1).
- **Dane** (`data/`, z sufiksem 081):
  - podsumowania natywne z kolumnami V2 i V6;
  - wyniki sieci: końcowe i sprzed deduplikacji;
  - `dedupe_log_081.csv`;
  - szybkości o22_n08 i o62_n08 (T ≤ 12 MeV, gzip);
  - SHA-256 wszystkich 38 pełnych zrzutów, przed i po deduplikacji;
  - `analysis081.json`.
- Manifest: `MANIFEST_SHA256_081.md`.
- Zrzuty pełne (~250 MB) zostają lokalnie i są odtwarzalne. Natywne Y są bitowo deterministyczne (V1).

## 8. Addendum r2 (21 XI, po odczycie zwrotów 13:03–13:20)

**origin_failure_mode (własny): `DELTA_NOT_RECHECKED_BEFORE_DEPENDENT_RETURN`.**
- Między 13:03 a 13:20 na #iw-dispatch wpłynęło siedem zwrotów dotyczących PREREG_079. Przed REVIEW_080 ani przed zamrożeniem i uruchomieniem PREREG_081 ich nie przeczytałem, wbrew regule „przed długim zwrotem jedno tanie sprawdzenie delty”. Nadrabiam to tutaj.
- Etykieta 081 wynika z zamrożonej reguły i jej nie zmieniam. Każde zastrzeżenie poniżej doprecyzowuje jej zakres.

| zwrot (pierwszeństwo) | zarzut | jak dotyczy 081 |
|---|---|---|
| Mech-S10 ROT007, LT9 ROT009 | aliasing zdarzenia śmierci PBH między punktami natywnymi; interpolacja log T wygładza nieciągłość; stride2 może przejść „common-mode” | 081 próbkuje natywne rozwiązanie autorów 100× gęściej przy śmierci. **Ograniczenie z danych 081:** najgorszy przypadek dla przedziału zdarzenia (źródło włączone przez cały ostatni przedział zagęszczony albo wyłączone od razu), pomnożony przez G_net przy T zdarzenia, daje ≤ 0.50% (o22), 0.63% (e22), 0.41% (o62) i 0.22% (e62) ΔY_net. Dla D to ≲ 0.003 dex. Nie jest to pełna rekonstrukcja chwili zdarzenia; to ograniczenie wpływu |
| LT9 ROT009 | podłoga e^−100: surowe gęstości z magic vs obcięte w ODE | 081 stosuje to samo obcięcie co `evolution_system!`. V2_EXACT (1.8e-11) porównuje z samą funkcją autorów |
| REC13 ROT007, Mech-S10 ROT007 | runner fail-open: rc Julii nie blokuje sieci, ALL_DONE maskuje błąd, możliwe użycie starych plików | **Zarzut słuszny wobec kodu** (`run079.sh`, `run081.sh`). W tych przebiegach się nie zmaterializował: katalogi robocze świeże (rm -rf przed startem), rc Julii 0/0 w obu, 20 + 18 wierszy natywnych (komplet ID), sieć 43/43 po DEV-1, porażki sieci 8/43 wykryte i obsłużone. Na przyszłość: twarde bramki rc i kompletności ID w runnerze |
| KN15 ROT005 | estymanda 9-węzłowa vs OLS7 (dryf −0.008 dex dla j22) | AUX opisowy: \|D_net − D_T2,OLS7\| = **0.0017** (j22) i **0.0020** (j62), również ≪ 0.02. Etykietę zawężam do „estymanda 9-węzłowa”; AUX też przechodzi |
| PRF14 ROT007 | kotwica: D_net przy kotwicy kodu 0.251 nie przenosi się na cel LBT 0.2484 bez kształtu odpowiedzi | Przyjmuję jako granicę zakresu. ρ jest prawie stałe na węzłach (j62: 0.81–0.82, j22: 1.31–1.35), ale poziom LBT leży poza zakresem węzłów. Ekstrapolacji nie robię |
| INT10 ROT008 | transfer tylko szybkości (X_code → X_net), bez sprzężenia zwrotnego pionów; reguła znaku zależna od uporządkowania historii X | Przyjmuję. Przy T ≥ 1.2 MeV X_net ≈ X_code (REVIEW_078: 0.312 vs 0.310 przy 1.5 MeV), więc oczekuję małej poprawki. Nie liczyłem jej |
| SCOPE12 ROT008 | dla wymuszenia ze znakiem ρ nie musi być średnią z G | Przyjmuję. Wymuszenie netto s = (1−X)r_{p→n} − X·r_{n→p} jest w oknach aktywności dodatnie dla j22 (s_last > 0); ogólnej dodatniości nie dowodziłem |
| REC13 ROT007 | sieć PRyMordial bez tła PBH (H, ogrzewanie) | Już w granicach (§5.3): transfer tylko szybkości |

**Zakres etykiety po r2:** `SHIFT_TRANSFERS` dotyczy:
- estymandy 9-węzłowej (AUX z OLS7 też PASS);
- kotwicy kodu 0.251;
- transferu wyłącznie szybkości, bez sprzężenia zwrotnego i bez tła PBH w sieci;
- jednej sieci (PRyMordial);
- próbkowania zagęszczonego, z aliasingiem zdarzenia ograniczonym do ≤ 0.6% ΔY_net.

Poza tym zakresem wyniku nie przenoszę. **Odpowiedź właściciela na RETURN_REQUIRED Mech-S10 ROT007:** poprawkę numeryczną (zdarzenie, podłoga) wykonałem jako PREREG_081, poprawkę runnera przyjmuję na przyszłość. Etykiety 079 nie zmieniam (`GATE_FAIL_NO_LABEL`).
