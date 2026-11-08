---
artifact_id: IW_BADACZ_WUXU_LEFTWALL_BUDGET_AND_KERNEL_BRIDGE_SYNTH_055_20261108
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude)
created_at: 2026-11-08
document_type: SYNTHESIS
mandate: Moderator 8 XI 10:46 („synteza i porównanie, mosty, nowe badania w kluczowych obszarach”)
code: code/wuxu_kernel_p13_bridge_posthoc.py → data/kernel_p13_bridge_posthoc.json
claim_ceiling: MODEL_INTERNAL_SYNTHESIS / POST_HOC_BRIDGE / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# SYNTH_055: lewa ściana Wu–Xu w natywnym kodzie v2 — budżet systematyk i pierwszy most z jądra pasm

**Rola:** Badacz. Zestawiam wyłącznie natywne pomiary w kodzie autorów `d395183` (v2), które mają opublikowane ciało. Ciał innych komórek nie czytałem ponownie w całości w tej rotacji; cytuję je tylko tam, gdzie je sprawdziłem.

## 1. Budżet systematyk lewej ściany (przesunięcie konturu χ² = 4 w dex; znak + oznacza słabsze ograniczenie)

| zmiana w modelu | j = 22 (1.12e9 g) | j = 28 | j = 34 | j = 62 (3.49e9 g) | źródło |
|---|---|---|---|---|---|
| tolerancja solvera 1e−3 → 1e−5 | +0.025 | — | — | — | REVIEW_047 (j = 24: +0.012) |
| prawo z tekstu `T^1.3` poniżej 1e9 g (`p13`) | −0.048 | −0.030 | −0.028 | −0.005 | REVIEW_042 |
| mapa ładunkowa B_sym zamiast B_exec | +0.27…+0.30 (skan warunkowy) | | | | SYNTH_039 r4, REVIEW_044 |
| wzór `Y_P = 2X`, wariant V1 (ponowna kalibracja T_nuc) | +0.075 | +0.036 | +0.038 | +0.034 | REVIEW_053 |
| wzór `Y_P = 2X`, wariant V2 (kryterium różnicowe) | +0.194 | +0.095 | +0.088 | +0.087 | REVIEW_053 |

- **Wzór Y_P przy 1e10 g:** V1 +0.34, V2 +0.085 (REVIEW_053, eksploracja). To zgodne z MT14 ROT026, wg którego dwa najcięższe wiersze siatki nie wyparowują przed T_nuc.
- **Nie sumuję tych przesunięć.**
  - Korekty działają w różnych kierunkach i mogą być skorelowane.
  - Dla B_sym i wzoru Y_P o tym, który wariant jest właściwy, decyduje właściciel (Mech-S8).
  - Wszystko jest MODEL_INTERNAL.
- **Odczyt.** Dwa dyskretne wybory modelu (mapa ładunkowa i wzór Y_P) dominują nad wszystkimi numerycznymi i widmowymi. Przy j = 22 tolerancja i prawo poniżej krawędzi tabeli dają setne części dex, a wybory dyskretne od kilku setnych do trzech dziesiątych.

## 2. Most: jądro pasm przewiduje przesunięcie `p13` (post hoc, bez parametrów)

- **Pytanie.** Czy jądro odpowiedzi czasowej z REVIEW_050 (`s_eff` dla pasm B, C, D) przenosi się na zaburzenie innego typu: zmianę prawa widma poniżej krawędzi tabeli?
- **Metoda.**
  - Iloraz liczby hadronów `r_b` (p13 / natywne, pięć kanałów razem) w każdym paśmie: `r_B = 1.041`, `r_C = 1.170`, `r_D = 1.324`. Natywne nachylenia pierwszego przedziału tabeli wynoszą −1.197…−1.205.
  - Przewidywanie: `Δ = −log10(1 + Σ_b (r_b − 1)·s_b)`.
  - Oba pomiary wejściowe istniały wcześniej, więc to sprawdzenie spójności, nie przewidywanie. Nic nie było dopasowywane.

| j | jądro pasm | tylko liczba hadronów | zmierzone (REVIEW_042) | jądro − pomiar |
|---|---|---|---|---|
| 22 | −0.043 ± 0.002 | −0.020 | −0.048 | +0.005 |
| 28 | −0.027 ± 0.001 | −0.015 | −0.030 | +0.003 |
| 34 | −0.018 ± 0.001 | −0.011 | −0.028 | +0.010 |
| 62 | −0.003 ± 0.001 | −0.003 | −0.005 | +0.002 |

- **Wynik.** Jądro odtwarza zmierzone przesunięcia z różnicą ≤ 0.010 dex. To rząd rozdzielczości bisekcji REVIEW_042 (0.005 dex) i szumu solvera przy j = 22 (≈ 0.01 dex).
  - Ważenie liczbą hadronów zaniża efekt mniej więcej dwukrotnie przy ścianie (j = 22, 28). Przy j = 62 obie metody się zgadzają, bo późne pasma mają tam mały udział.
  - Jądro systematycznie zaniża wartość bezwzględną (4/4 różnice dodatnie). Przy tej rozdzielczości nie rozstrzygam, czy to efekt.
- **Zakres ważności.** Ilorazy `r_b ≤ 1.33` leżą w lokalnym reżimie, w którym REVIEW_054 potwierdził A1 (`k = 2`, błąd 0.013 dex). Przy usunięciu pasm (`k = 0`) A1 zawodzi o 0.053 dex. Most stosować tylko w tym zakresie.

## 3. Połączenia z Żywą Teorią (propozycje dla LT7, nie zapis)

- **§6.13 (sprzężone jądro W).** Pojęcie jądra odpowiedzi celu jest teraz zmierzone natywnie (REVIEW_050) i przeszło niezależne zaburzenie (§2 tutaj, post hoc). Propozycja jednej linii w aneksie, z sufitem MODEL_INTERNAL.
- **§7.5k (Tw. 7.18: promień liniowy a skończona amplituda).** REVIEW_054 to konkretny, natywny przykład ostrzeżenia z książki, że sam liniowy funkcjonał nie chroni przy dowolnej amplitudzie.
  - Przy `k = 2` liniowa mapa działa.
  - Przy `k = 0` błąd jest około czterokrotnie większy (0.053 wobec 0.013 dex). Przy `k = 2` A1 zawyża wartość bezwzględną przesunięcia, przy `k = 0` ją zaniża.
  - `[▷]` To odpowiednik roli `M₃` w Tw. 7.18. Książka przedstawia to jako matematykę; tu jest pomiar w modelu.
- **§7.5e.1 (certyfikat ekstremum).** Reguła V1/V2 z REVIEW_053 (kontur z natywnej krzywej przy przesuniętym progu) jest przykładem dobrze określonej obserwabli celu: daje się ją przenieść tylko wtedy, gdy założenie „tylko rozpad” jest sprawdzone (P1). Przy 1e10 g już nie jest.

## 4. Następne badania w tym obszarze (ranking)

1. **Decyzja właściciela o wzorze Y_P** (Mech-S8, AUD1 ROT032). Potem natywny przebieg wariantu „intencja autorów”: wzór `2X` + prawo `p13`, na pełnej siatce mas. Koszt jest mały: wzór nie wymaga nowego ODE, `p13` wymaga.
2. **Ciężki koniec (j ≥ 98).** Natywny zapis `t(T_nuc)`, `M(T_nuc)` i liczby hadronów wstrzykniętych po T1 przy β z konturu. To sprawdzenie, które MT14 ROT026 nazywa rozstrzygającym. `magic()` zwraca te listy, więc to tani pomiar opisowy.
3. **Krzywa odpowiedzi `s(k)` przy j = 22** (`k ∈ {0, 0.5, 1.5, 2, 4}` dla C+D). Daje zakres ważności A1, potrzebny każdemu mostowi z jądra.
4. **Audyt zewnętrzny.** REVIEW_050, 053, 054 i ten most są wynikami jednej rodziny modeli. Potrzebna komórka spoza rodziny Claude (Mech-S8, REC11 lub DS/Gemini), z natywnym przebiegiem, a nie tylko odczytem.

## 5. Powrót w trzech warstwach

- **Wynik:**
  - budżet lewej ściany: wybory dyskretne (B_sym, wzór Y_P) rzędu 0.03–0.3 dex; numeryczne i widmowe ≤ 0.05 dex;
  - jądro pasm przenosi się post hoc na zaburzenie `p13` (≤ 0.010 dex), ważenie liczbą zaniża ≈ 2×.
- **Konfiguracja:**
  - most wymagał tylko arytmetyki na istniejących danych; natywne przebiegi dnia (≈ 10 min łącznie) dostarczyły zakres jego ważności;
  - jedna rodzina modeli: wszystkie liczby w tabelach to pomiary Badacza.
- **Uczenie systemu:**
  - `origin_failure_mode: WEIGHT_PROXY_WITHOUT_RESPONSE_KERNEL` (powtórka klasy z REVIEW_050): ważenie liczbą hadronów było domyślnym przybliżeniem w kilku komórkach i zaniża efekt przy ścianie ≈ 2×.
  - Kandydat reguły `[▷]`: przed użyciem wag liczbowych w Front B sprawdzić je na jednym natywnym zaburzeniu.
