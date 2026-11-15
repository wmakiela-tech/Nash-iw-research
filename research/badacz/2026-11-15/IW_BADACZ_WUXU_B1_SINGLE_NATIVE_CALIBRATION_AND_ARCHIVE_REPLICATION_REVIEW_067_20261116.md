---
artifact_id: IW_BADACZ_WUXU_B1_SINGLE_NATIVE_CALIBRATION_AND_ARCHIVE_REPLICATION_REVIEW_067_20261116
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), współwłaściciel natywny B1 (z Mech-S9)
created_at: 2026-11-16
document_type: REVIEW
responds_to: PREREG_066 r1+r2 (ten katalog; fdc7db6, 76da037); odstępstwo D1 (3caa4d9)
authorization: Moderator, 16 XI 2026 00:10 („Autoryzuję”), jeden przebieg wg PREREG_066
data: data/b1_066_raw_outputs.json (surowe wyjścia 8 ramion), data/analysis066.json (skrypt preregu), data/posthoc066.json (post hoc)
code: code/b1_calibration_066.jl, code/run066.sh, code/b1_066_analysis.py (przed wynikami), code/b1_066_posthoc.py (po wynikach)
claim_ceiling: REPRODUCIBILITY_AND_NUMERIC_CALIBRATION_AT_ONE_POINT / NO_PHYSICS / NO_PBH_BOUND / NO_E4_UNBLOCK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
external_audit: WYMAGANY (Mech-S9 lub inna komórka spoza rodziny Claude); audyt Claude-nad-Claude nie jest zewnętrzny
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_067: wynik PREREG_066 — replikacja archiwum, kalibracja solvera w (j22, β_max), replika śladu Mech-S9

**Rola:** Badacz. Wszystkie wnioski mają status [▷].

## Przebieg

- **Autoryzacja i odstępstwo.** Moderator autoryzował przebieg 16 XI o 00:10. Jedyne odstępstwo, D1, to escapowanie JSON w nagłówku; nie wpływa na obliczenia.
- **Środowisko.** Julia 1.12.3, DifferentialEquations 7.17.0, ArbNumerics 1.6.3, OrdinaryDiffEqCore 3.33.1. Po przeniesieniu depot cały kod natywny skompilował się od nowa.
- **Wykonanie.** Osiem ramion uruchomionych w dwóch kolejkach, 00:30:47–00:44:18, wszystkie ze statusem 0. Kod autorów `d395183` bez zmian poza linią `solve` w ramionach A0–A4.
- **Ostrzeżenie o `t0` w logach** dotyczy mojego zegara. Kod autorów nie zawiera `t0`, więc nie wpływa na `magic()`.
- **Odtwarzalność analizy.** Ponowne przeliczenie z `b1_066_raw_outputs.json` daje bajtowo identyczny `analysis066.json`.

## Werdykty preregu

| test | kryterium | wynik | werdykt |
|---|---|---|---|
| A | 14 punktów j = 22 wobec `Y_P_mat` autorów | 0/14 bit w bit; średnia Δ = +1.04e−5; max \|Δ\| = 2.58e−4 (β_max); wszystkie \|Δ\| ≤ 3e−4 | **A-STAT** |
| C0a | przechwycenie `sol` neutralne bit w bit | Y(A0u) ≡ Y(A0) | **PASS** |
| C0b | jawne 1e−3/1e−6 ≡ domyślne bit w bit | ΔY = +3.55e−5, ΔX = +1.40e−5; naccept 1290 → 1284 | **FAIL** |
| C0c | \|Y(A2) − Y(A1)\| | **0**, bit w bit (te same 1284 kroki) | **NO_CONFOUND** |
| S | \|ΔX(A4 − A3)\| ≤ 1e−5 i ≤ 0.5·\|ΔX(A3 − A0)\| | 3.97e−6 ≤ 1e−5; 3.97e−6 ≤ 4.70e−6 | **RELEASE** (kruche, patrz niżej) |
| C | Y = 0.25239220435845267, indeks 8545, t = 0.33492735181 s | Y identyczne w 17 cyfrach; indeks 8545; t = 0.33492735181011263 s | **REP-BIT PASS** |

## Kalibracja w (j = 22, β = `β_PBH_list[100]`)

| ramię | tolerancja | Y | X_n(T0) | przyjęte / odrzucone kroki | rozrzut zegara M³ (kroki przyjęte) |
|---|---|---|---|---|---|
| A0 | domyślna (1//10³, 1//10⁶ w ArbFloat) | 0.25223220669121638 | 0.11199209652621654 | 1290 / 91 | 2.06e−3 |
| A1 | jawnie 1e−3, 1e−6 (Float64) | 0.25226766833356379 | 0.11200607808760793 | 1284 / 82 | 2.00e−3 |
| A2 | jak A1 + `saveat` | ≡ A1 | ≡ A1 | 1284 / 82 | — (próbki zapisane) |
| A3 | 1e−4, 1e−7 | 0.25225604899794413 | 0.11200149694799394 | 11 395 / 116 | 1.51e−4 |
| A4 | 1e−5, 1e−8 | 0.25224598094280276 | 0.11199752739139585 | 111 836 / 134 | 4.74e−6 |

- **Rozrzut X(T0)** w czterech ramionach tolerancji wynosi **1.40e−5**; w Y to 3.55e−5.
- **Najlepsze oszacowanie.** Wartość przy 1e−5 (A4) różni się od domyślnej o +5.4e−6 (A0) i −8.6e−6 (A1).
- **Wniosek [▷]:** w tym punkcie X_n(T0) przy tolerancji domyślnej jest określone numerycznie z dokładnością rzędu **1e−5**, w Y ok. 3e−5.

**C0b: mechanizm [▷].** Odczyt statyczny `OrdinaryDiffEqCore/src/solve.jl`, linie 320–357:
- przy braku argumentu wartość domyślna to `convert(uBottomEltype, oneunit · 1//10^3)`, czyli liczba wymierna przeliczona na ArbFloat;
- wartość podana jawnie zostaje Float64 (`real.(reltol)`).

Wartości nominalne są więc te same, co potwierdza w źródle udokumentowane domyślne (MT15 ROT021), ale reprezentacje różnią się o ok. 1e−17 względnie. Takie zaburzenie zmienia ciąg kroków i przesuwa X o 1.4e−5. To bezpośredni pomiar **progu szumu solvera przy tolerancji domyślnej**, zgodny z wcześniej obserwowanymi skokami ~3e−5 w Y przy zaburzeniach wejścia o 1 ulp. Mechanizmu nie testowałem przebiegiem. Testem byłoby jedno wywołanie z `reltol=1//1000, abstol=1//10^6`, które powinno dać bitową zgodność z A0. Wymaga to osobnej autoryzacji.

**Bramka S jest RELEASE formalnie, ale krucho (post hoc).**
- Warunek 1, \|ΔX(1e−5 − 1e−4)\| = 4.0e−6 < 1e−5, jest odporny.
- Warunek 2, czyli kontrakcja, ma mianownik \|ΔX(A3 − A0)\| = 9.4e−6. To mniej niż zmierzony szum samego odniesienia (1.4e−5, C0b).
- Gdy za odniesienie domyślne wziąć A1 (ta sama nominalna tolerancja), \|ΔX(A3 − A1)\| = 4.58e−6 i warunek 2 nie przechodzi.
- Werdykt zapisany w preregu stoi, ale interpretuję go wyłącznie przez warunek 1 i rozrzut drabiny.

**C0c.** Ramię z `saveat` daje te same kroki i bitowo ten sam wynik, co potwierdza oczekiwanie z odczytu statycznego (PREREG_066 r2). Porównania tolerancji w moich REVIEW_035/044/047/050/057/059/061/063/065 **nie są obciążone ścieżką próbkowania**. Zawierają natomiast składnik szumu reprezentacji, o tym samym rzędzie co C0b. Status „warunkowe” z 15 XI zdejmuję.

## Zatrzymanie i zegar na krokach przyjętych

Pytania dotyczą MT15 ROT020, KN14 ROT002 i Mech-S9 ROT022. M_stop = 2.31091 g, zgodnie z MT15 ROT020.

| ramię | ostatni krok przed progiem → pierwszy za progiem (M, g) | M_za / M_stop | czas zatrzymania (s) |
|---|---|---|---|
| A0 | 3005.5 → 1.797 | 0.778 | 0.3356997 |
| A1 | 16 082 → 0.1009 | 0.044 | 0.3356794 |
| A3 | 4.847 → 1.842 | 0.797 | 0.3350066 |
| A4 | 2.661 → 2.249 | 0.973 | 0.3349572 |

- **Niedociągnięcie progu** to kwantyzacja ostatniego kroku. Flaga jest sprawdzana w RHS i nie ma lokalizacji zdarzenia (por. Mech-S9 ROT022). Skala niedociągnięcia zależy od ostatniego kroku, nie monotonicznie od tolerancji, i maleje przy 1e−5.
- **Czas zatrzymania** przesuwa się między tolerancją domyślną a 1e−5 o **+0.22%**. Pierwszy zerowy indeks wyjścia `n_PBH` zmienia się z 8545 (A0, A1) na 8544 (A3, A4).
- **Rozrzut stałej zegara** K = (m₀³ − M³)/(t − t_f) na krokach przyjętych maleje z tolerancją: **2.1e−3 → 1.5e−4 → 4.7e−6**. Dryf zegara M³ przy tolerancji domyślnej jest więc **numeryczny i zbieżny**, a nie modelowy. Zgadza się to kierunkowo z KN14 ROT002, choć miara jest inna: tam sieczna na próbkach wyjścia, tu kroki przyjęte.
- Mimo przesunięcia zatrzymania o 0.22% X(T0) mieści się w rozrzucie drabiny, 1.4e−5.

## Archiwum autorów (A-STAT)

- **Zgodność bitowa: 0 z 14.** Środowisko z zamrożonymi dziś wersjami nie odtwarza `scanning.jld2` bit w bit.
- **Różnice** mają średnią +1.0e−5 i odchylenie standardowe **1.1e−4**; 9 z 14 jest dodatnich.
- **W β_max** archiwum minus Y(A4) wynosi **+2.44e−4**, ok. 7× więcej niż rozrzut Y całej drabiny tolerancji w tym punkcie (3.55e−5).
- **Hipoteza [▷]:** archiwum powstało w środowisku o innych wersjach pakietów; autorzy nie mają Manifestu. Rozbieżność w tym punkcie przekracza bowiem zmierzoną niepewność numeryczną naszego środowiska. Pomiar dotyczy jednego punktu, więc nie uogólniam go na całą siatkę.
- **Konsekwencja dla B1:** archiwum nie jest bitowym punktem odniesienia. Odniesienie B1 musi być przypięte do środowiska z Manifestem.

## Replika Mech-S9 ROT013 (rodzina Claude, ten kontener, kod skompilowany od nowa)

Y = 0.25239220435845267 jest identyczne we wszystkich 17 cyfrach Float64 z wynikiem Mech-S9 (GitHub Actions, rodzina GPT). Zgadzają się też pierwszy zerowy indeks (8545) i t ostatniej żywej próbki. Dowodzi to **bitowej odtwarzalności między maszynami i rodzinami modeli** przy tym samym kodzie, wejściu i wersjach pakietów.

Uwaga poboczna: punkt Mech-S9 (β + 0.586%) ma Y wyższe o 1.6e−4 niż β_max. Lokalnie to ok. 10× średnie nachylenie konturu (0.063 wobec 0.0064 na dex), czyli szarpanie.

## Konsekwencje dla B1 (propozycje, nie decyzje)

1. **Stan HOLD_SOLVER_CALIBRATION** (PRF13 ROT022) w punkcie (j22, β_max) można zawęzić. Efekty ≫ 1e−5 w X(T0), czyli ≫ 3e−5 w Y, są numerycznie rozróżnialne przy tolerancji domyślnej. Efekty ≲ 1e−5 nie są. Sygnały na poziomie podłogi hadronowej (~1e−15) leżą 10 rzędów poniżej progu szumu. Decyzja należy do Moderatora i właścicieli.
2. **Odniesienie B1** to środowisko z Manifestem (nasze; Mech-S9 jest z nim bitowo zgodne), a nie archiwum autorów.
3. **Wynik 30-dniowy** z tego testu sięga najwyżej **REPRODUCIBILITY**: pozytywna odtwarzalność natywna i jawna kalibracja w jednym punkcie. Fizyka (E4, hadronizacja poniżej 1e9 g) pozostaje HOLD.

## Granice

Wyniki dotyczą jednego punktu kalibracji i 14 punktów archiwum. Nie są fizyczną granicą PBH ani walidacją BlackHawk. Audyt merytoryczny musi być zewnętrzny wobec rodziny Claude; dane i skrypty do tego są w tym katalogu.

## Powrót w trzech warstwach

- **Wynik.** A-STAT, C0a PASS, C0b FAIL (próg szumu solvera zmierzony: 1.4e−5 w X), C0c NO_CONFOUND, S RELEASE (kruche), REP-BIT PASS. Dryf zegara M³ jest numeryczny i zbieżny.
- **Konfiguracja.** Prereg złożony z kontraktów PRF13, Mech-S9, MT15 i KN14 dał w jednym przebiegu odpowiedzi na cztery wątki B1. Koszt: 14 min obliczeń i 17 min prekompilacji.
- **Uczenie systemu:**
  - `GATE_THRESHOLD_AT_NOISE_LEVEL`, drugi raz po REVIEW_063. Kryterium kontrakcji z mianownikiem w postaci pojedynczej różnicy był porównywalny z szumem odniesienia. Łatka: każda bramka zbieżności porównuje różnice do **zmierzonego** progu szumu (para ramion o tej samej nominalnej tolerancji, jak A0/A1), a nie do jednej różnicy.
  - `TOLERANCE_REPRESENTATION_PERTURBATION` (nowa obserwacja). Jawne podanie „wartości domyślnej” nie jest wartością domyślną, bo zmienia typ i bity. Łatka: w porównaniach z kodem autorów albo nie podawać tolerancji, albo podawać ją w typie stanu (`1//1000`).
