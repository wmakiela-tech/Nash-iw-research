---
artifact_id: IW_BADACZ_LT6_ROT004_EVENT_CERTIFICATE_CROSS_FAMILY_CHECK_REVIEW_007_20261027
exposure: PUBLIC
claim_ceiling: CROSS_FAMILY_CHECK_[▷] / PROOF_VERIFIED_LINE_BY_LINE / NUMERICAL_FALSIFICATION_ATTEMPT_NO_HIT / CONSTRUCTIVE_REMARK_[▷]_NO_NOVELTY / NOT_A_REFEREE_VERDICT / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-27
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-002
selection: PREREG_006, pozycja 1 (research/badacz/2026-10-26/IW_BADACZ_GPT_CELL_INDEPENDENT_REVIEW_TARGET_SELECTION_PREREG_006_20261026.md, commit 93d0a3a, zatwierdzony przed lekturą celu)
target: research/lt6/2026-10-26/IW_LT6_ROT004_EVENT_ALIGNED_A_POSTERIORI_CERTIFICATE_001_20261026.md (autor LT6, commit 89d65ba; włączony do REV024 §6.9b i §6.15)
code: research/badacz/2026-10-27/code/lt6_rot004_event_certificate_check.py (sha256 7cb00a0fa4c94862c9aefb8dbe171edced8df19f074781915fb1d731d210f41a)
output_sha256: b1edbf3259fe47b945b58508ee958657a85aaaa6bb84064ede5c9fc8f2afcc48 (lt6_rot004_event_certificate_check.json)
---

# Recenzja międzyrodzinowa LT6 ROT004: certyfikat residuum–zdarzenie–obserwabla

**Status:** `[▷]`. Sprawdzenie przez Claude'a wyniku komórki GPT. Nie jest to werdykt REC10/SW.
Kod napisałem niezależnie; skryptu autora nie czytałem.

## Wynik w skrócie

1. **Matematyka jest poprawna.** Sprawdziłem wszystkie cztery twierdzenia krok po kroku:
   - ograniczenie Gronwalla przez residuum;
   - ograniczenie błędu chwili zdarzenia;
   - ograniczenie błędu obserwabli;
   - pochodna chwili zdarzenia z członem brzegowym.

   Przykład 1D i kontrprzykład styczności zgadzają się dokładnie (SymPy). Nie znalazłem błędu.
2. **Liczby autora odtwarzają się co do `1e-11`**, ale publiczny tekst ich nie wyznacza. Brakuje dwóch
   danych: prawego końca przedziału `I` (wychodzi `1`) i informacji, że w ograniczeniu
   Gronwalla stoi `sup‖r‖`, a nie całka z `‖r‖`. Oba wywnioskowałem z podanych liczb.
3. **Uwaga główna, konstruktywna `[▷]`.** Stałe `m` i `F` w twierdzeniu dotyczą **prawdziwej**
   trajektorii, której w zastosowaniu a posteriori nie znamy. W przykładzie syntetycznym `m`
   pochodzi z rozwiązania dokładnego (wyrocznia). Żeby certyfikat dał się obliczyć, trzeba dopisać
   jedną z dwóch dróg (§3).
   - Druga droga to orientacja wzoru (2.2) LT5, który jest już w monografii w §6.9a. W tej
     orientacji założenie o stałym znaku jest konieczne: daję dokładny kontrprzykład.
   - Do tego dochodzi obliczalny certyfikat pierwszego przecięcia. Na 296 przedziałach dał 0
     fałszywych przejść.
4. **Ograniczenie „specialised” dla `Q` w przykładzie nie jest instancją ogólnego wzoru.**
   Wykorzystuje to, że w 1D oba punkty leżą na powierzchni zdarzenia. Ogólny wzór daje dla tych
   samych danych `0.0179` zamiast `0.00591`. Oba ograniczenia są poprawne; wystarczy je nazwać.
5. **Opis jednego źródła literaturowego jest nieprecyzyjny** (§5).

## 1. Dowód — sprawdzenie krok po kroku

**Notacja.** Niech `e = x − x̂`, `H(t) = φ(t, x(t))` (prawdziwa) i `Ĥ(t) = φ(t, x̂(t))` (obliczalna).

- **Gronwall.** `e' = f(t,x) − f(t,x̂) − r`, więc `d‖e‖/dt ≤ L‖e‖ + ‖r‖` prawie wszędzie. Dla
  ciągłego, odcinkami `C¹` przybliżenia `x̂` funkcja `e` jest absolutnie ciągła, a stąd wynika
  `‖e(t)‖ ≤ κ(t)`. Poprawne.
- **Chwila zdarzenia.** `|H(τ̂)| ≤ |φ(τ̂,x̂(τ̂))| + L_φ‖e(τ̂)‖ ≤ r_ev + L_φ κ(τ̂)`. `H(τ) = 0`.
  Z twierdzenia o wartości średniej na `I`: `|H(τ̂)| ≥ m|τ̂ − τ|`. Poprawne.
  - Funkcja `κ` jest niemalejąca, więc `sup_I κ = κ(sup I)`.
  - Założenie „stały znak” jest tu zbędne. Prawdziwe `H` jest różniczkowalne, więc z tw. Darboux
    `|H'| ≥ m > 0` na przedziale już wymusza stały znak. Uwaga redakcyjna.
- **Obserwabla.** `|Q(τ̂,x̂(τ̂)) − Q(τ̂,x(τ̂))| ≤ L_Qx κ` oraz
  `|Q(τ̂,x(τ̂)) − Q(τ,x(τ))| ≤ (L_Qt + F L_Qx)|τ̂ − τ|`, bo `‖x'‖ = ‖f‖ ≤ F` między `τ` a `τ̂`.
  Poprawne.
- **Pochodna zdarzenia.** Różniczkujemy `φ(τ(ε), x(τ(ε);ε), ε) = 0` po `ε`. Wychodzi
  `τ' = −(φ_x z + φ_ε)/(φ_t + φ_x f)`, a dla `J = ∫₀^τ L dt` także człon brzegowy `L(τ)τ'`. Poprawne.
- **Przykład 1D** (SymPy, dokładnie):
  - `x = ε + (1−ε)e^{−t}`, `L = x`, `J = 1/2 + ετ`;
  - `J'(0) = log 2`;
  - część przy ustalonym czasie: `log 2 − 1/2`;
  - człon brzegowy: `1/2`;
  - `τ'(0) = 1` zarówno ze wzoru, jak i bezpośrednio.
- **Styczność.** `τ = 1 − √ε`, `dτ/dε = −1/(2√ε) → −∞` dla `ε → 0⁺`. Poprawne.

## 2. Odtworzenie liczb autora

| wielkość | autor | moje | uwaga |
|---|---|---|---|
| błąd chwili zdarzenia | `0.00644835308246` | `0.006448353082461` | |
| ograniczenie bezpośrednie (`κ = 0.004`) | `0.0118186166455` | `0.0118186166455` | wynika z niego `m = 0.338449`, czyli `I` kończy się w `t = 1` |
| ograniczenie residuum + Gronwall | `0.1035494310814` | `0.1035494310820` | tylko przy `‖r‖ ≤ sup‖r‖ = √(0.02²+0.004²)`; z całką wychodzi `0.0684` |
| błąd `Q` | `0.00322417654123` | `0.00322417654123` | |
| ograniczenie „specialised” dla `Q` | `0.00590930832274` | `0.00590930832275` | `= ½ ×` ograniczenie zdarzenia, zob. §4 |

**Prośba do autora:** dopisać w publicznym ciele przedział `I` i sposób ograniczenia `‖r‖`. Bez
tego odtworzenie wymaga zgadywania.

## 3. Uwaga główna: `m` i `F` z prawdziwej trajektorii nie dają się obliczyć

REV024 §6.9b wymienia warunki, które trzeba udowodnić, żeby uznać oszacowanie za źródłowo
poprawne: izolację pierwszego przecięcia i zakres transwersalności. Twierdzenie zakłada przy tym
`|H'| ≥ m` i `|f| ≤ F` na **prawdziwej** trajektorii. Proponuję dwie obliczalne drogi. Obie są
elementarne i standardowe w numeryce weryfikowanej; nowości nie zgłaszam.

- **(V1′) tuba.** `m ≥ inf_{t∈I} (|φ_t + φ_x f(t,x̂(t))| − Λ κ(t))`. Tu `Λ` jest stałą
  Lipschitza funkcji `y ↦ φ_t + φ_x f(t,y)`; dla liniowego `φ` wynosi ona `‖φ_x‖ L`. Podobnie
  `F ≤ sup_I ‖f(t,x̂)‖ + L sup_I κ`.
- **(V2) strona numeryczna.** To orientacja wzoru (2.2) LT5, już obecnego w monografii w §6.9a.
  Ten sam wzór obowiązuje z `m̂ = inf_I |Ĥ'|` oraz `F̂ = sup_I ‖x̂'‖`, które liczy się z samego
  `x̂`, ale pod dwoma warunkami: `Ĥ` jest ściśle monotoniczne na `I` i `τ ∈ I`. Drugi warunek
  certyfikuje się testem końców przedziału (niżej).
  - Dowód: `|Ĥ(τ)| ≤ L_φ κ(τ)` i `|Ĥ(τ̂)| = r_ev`, a z monotoniczności
    `|Ĥ(τ) − Ĥ(τ̂)| ≥ m̂|τ − τ̂|`.
  - **Tu założenie o stałym znaku jest konieczne**, bo dla odcinkami `C¹` przybliżenia `x̂`
    (np. interpolacji liniowej zapisanych kroków) tw. Darboux nie działa.
  - Dokładny kontrprzykład: `x = 1/2 − (t − 9/10)/10`, `x̂ = 1/2 + |t − 1| − 1/10`, `I = [9/10, 11/10]`.
    Wtedy `|x̂'| = 1` prawie wszędzie, a `τ̂ = 11/10` jest drugim pierwiastkiem `Ĥ`. Błąd `1/5`
    przekracza ograniczenie V2 bez warunku znaku (`9/100`). V1 z prawdziwym `m = 1/10` daje `9/10`
    i obowiązuje.
- **Certyfikat pierwszego przecięcia** (obliczalny z `f`, `x0`, `x̂`, `φ`). Na przedziale `I = [a,b]`
  sprawdzamy trzy warunki:
  1. `|Ĥ(t)| > L_φ κ(t)` na `[t0, a]` — przed `a` nie ma prawdziwego pierwiastka;
  2. `Ĥ(a)` i `Ĥ(b)` mają przeciwne znaki z marginesem `L_φ κ` — pierwiastek istnieje w `I`;
  3. warunek tuby z V1′ — pierwiastek jest jedyny.

  W §6.9b to wymagania słowne; tak zapisane dają się sprawdzić maszynowo.

W przykładzie autora wszystkie warianty ograniczają błąd `0.00645`:

| wariant | ograniczenie |
|---|---|
| wyrocznia, `κ = 0.004` | `0.01182` |
| V2, `κ = 0.004` | `0.01202` |
| tuba, `κ = 0.004` | `0.01210` |
| tuba, Gronwall `sup‖r‖` | `0.1170` |

**Propozycja dla LT6, nie edycja.** W §6.9b dopisać, że `m` i `F` dotyczą prawdziwej trajektorii,
i odesłać do orientacji z §6.9a jako obliczalnej. Przy gęstym wyjściu odcinkami `C¹` wymagać
ścisłej monotoniczności `Ĥ`.

## 4. Ograniczenie dla `Q` w przykładzie

`0.00591 = ½ × 0.01182` nie wynika z ogólnego wzoru `L_Qx κ + (L_Qt + F L_Qx)|τ̂−τ|`. Ten daje dla
tych samych danych `0.0179` (`L_Qx = 2 sup|x|`, `F = sup|x'|` na `I`). Autor wykorzystał to, że
w 1D przy `r_ev = 0` oba punkty `x̂(τ̂)` i `x(τ)` leżą na powierzchni `x = 1/2`, więc różnica `Q`
zależy tylko od czasu. Poprawne, ale to specjalizacja 1D. Proponuję nazwać ją „ograniczeniem na
powierzchni zdarzenia”.

## 5. Literatura (rekordy sprawdzone)

- **DOI 10.1007/s44207-024-00001-0** istnieje: Ranocha, Giesselmann, *Stability of step size
  control based on a posteriori error estimates*, Computational Science and Engineering 1, art. 1
  (2024). Praca dotyczy stabilności sterowania krokiem. Ograniczenie Gronwalla przez residuum
  (Lemat 1) jest w niej tłem, a nie metodą weryfikowaną. Opis autora („verified residual a
  posteriori ODE error”) jest więc nieprecyzyjny; proponuję „residual-based a posteriori bound
  (Lemma 1)”.
- **Kong, Payne, Zhu, Johnson**, Proc. IEEE 112(6):585–608 (2024), DOI 10.1109/JPROC.2024.3440211 —
  zgodne.
- **Khan, Barton**, IEEE TAC 62(7):3193–3208 (2017), DOI 10.1109/TAC.2016.2644759 — zgodne.
- **Dodatkowi klasyczni gospodarze** wzoru na pochodną chwili zdarzenia:
  - Galán, Feehery, Barton, Appl. Numer. Math. 31(1):17–47 (1999), DOI
    10.1016/S0168-9274(98)00125-1 (sprawdziłem rekord, tekstu nie otwierałem);
  - Hiskens, Pai, IEEE TCAS-I 47(2):204–220 (2000), DOI 10.1109/81.828574. Wzór (48) ma
    mianownik niezerowy przy transwersalności (38). Dokładnej postaci nie wydobyłem z PDF.

## 6. Próba falsyfikacji (seed `20261026`)

| test | wynik |
|---|---|
| 300 losowych ODE (`d ≤ 3`, `f = Ax + C tanh(Wx) + s(t)`, globalne `L`), zaburzone `x̂`, `τ̂` jako pierwiastek lub z przesunięciem (`r_ev > 0`) | V1 i V2, czas i `Q`: 0 naruszeń |
| najwyższy stosunek błąd/ograniczenie przy najostrzejszym legalnym `κ` | czas `0.996`, `Q` `0.917`: ograniczenie prawie ostre, test rozróżniający |
| `κ` Gronwalla z obliczalnego residuum | ≥ prawdziwego błędu we wszystkich instancjach |
| certyfikat pierwszego przecięcia | 296 przedziałów wybranych tylko z `x̂`, 188 przejść, 0 fałszywych przejść |
| pochodna zdarzenia i `J'` (60 instancji, różnice centralne `h = 1e-5`) | maks. błąd względny `6e-7`; człon brzegowy zawsze ≥ `0.5%` `|J'|`, więc jego pominięcie jest zawsze wykrywalne |

Kontrole na siatce nie są ścisłe przedziałowo. To próba falsyfikacji, nie dowód.

## Odtworzenie

```text
pip install numpy==2.1.3 scipy==1.14.1 sympy==1.13.3
python3 research/badacz/2026-10-27/code/lt6_rot004_event_certificate_check.py --out <katalog>
```

Około 2 minut. Wszystkie pola `verdict` mają wartość `true`. Dwa czyste uruchomienia dały
identyczny JSON.

## Czego nie sprawdziłem

- skryptu i ZIP autora;
- historycznego źródła Julia 10D;
- czegokolwiek fizycznego (PBH, Y_p, D/H) — autor też tego nie twierdzi.

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_CLAIM`. Audyt zewnętrzny wyniku
Claude'a: Grok (przez Moderatora).
