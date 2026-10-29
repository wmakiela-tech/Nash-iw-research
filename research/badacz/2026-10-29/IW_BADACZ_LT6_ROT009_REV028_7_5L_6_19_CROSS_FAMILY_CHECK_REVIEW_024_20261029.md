---
artifact_id: IW_BADACZ_LT6_ROT009_REV028_7_5L_6_19_CROSS_FAMILY_CHECK_REVIEW_024_20261029
exposure: PUBLIC
claim_ceiling: CROSS_FAMILY_CHECK_[▷] / PROOFS_VERIFIED_LINE_BY_LINE / EXACT_RATIONAL_EXAMPLE_REPRODUCED / CONSTRUCTIVE_REMARK_[▷]_CLOSED_FORM_ROWS / NOT_A_REFEREE_VERDICT / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_CLAIM
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-29
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-006
selection: PREREG_023 (research/badacz/2026-10-29/IW_BADACZ_REVIEW_TARGET_SELECTION_PREREG_023_20261029.md, commit 9e8e8e1)
target: LT6 ROT009 (research/lt6/2026-10-29/IW_LT6_ROT009_EXACT_H_MOMENT_REPAIR_TARGET_PERSISTENCE_001_20261029.md) i wstawki REV028 §7.5l oraz §6.19 (Nash-Priv living-theory/2026-10-29/REV028, prywatne; tu cytuję tylko treść matematyczną)
code: research/badacz/2026-10-29/code/lt6_rot009_closed_form_rows_check.py (sha256 746416ca4ed959ab2fd78aad5dc2dc6cfeac2050850b4eb9e653aac492e45aa1)
output_sha256: e5dcacaf4f3f70b069acecb21637a52c5843668182c3a268b7e1a72d45584784 (lt6_rot009_closed_form_rows_check.json)
---

# Recenzja międzyrodzinowa LT6 ROT009 oraz REV028 §7.5l i §6.19

**Status:** `[▷]`. Sprawdzenie przez Claude'a wyniku komórki GPT. Nie jest to werdykt REC10/SW.
AUD1 ROT006 (wewnątrzrodzinowy) sprawdził już ten sam rzut. Ta recenzja jest pierwszą spoza
rodziny GPT. Mój doc 022 dotyczy tego samego frontu; porównanie z nim w §3 nie jest jego audytem.

## Wynik

1. **T009.1–T009.3 są poprawne.** Sprawdziłem dowody krok po kroku:
   - `Mp = 0` z `MJ_H = I`;
   - Pitagoras z `p ⊥_H q`, bo `Hq ∈ range Mᵀ`;
   - `‖q‖_H ≤ ‖e‖/s`, bo `‖q‖_H² = eᵀ(MH⁻¹Mᵀ)⁻¹e`;
   - dodatniość przez Cauchy'ego–Schwarza w `H⁻¹`;
   - przeniesienie luki celu z nierówności trójkąta;
   - T009.3: Weyl dla `σ_min`, potem drugi rzut.
2. **Przykład wymierny odtworzony dokładnie:** `q = (6/25, 3/50, 0)`, `p = (9/25, −9/25, 2/5)`,
   normy `54/25 = 261/125 + 9/125`, luka celu `2958/625`.
3. **Próba falsyfikacji: brak trafienia.** 400 losowych instancji: defekt Pitagorasa `≤ 2.4e-12`.
   Ograniczenia na `‖q‖_H`, na drugą korektę (T009.3) i na lukę celu nie zostały ani razu
   naruszone.
4. **Wzór na promień z szumem z ROT033 (cytowany w §6.19 przez liczby):**
   `ρ(η) = R[pη + q√(1 − η²)]` dla `η < p/√(p² + q²)`. Zgadza się z bezpośrednią maksymalizacją
   co do `5e-9` (300 przypadków).
5. **Uwaga konstruktywna `[▷]`: numeryczna część STOP z T009.3 da się usunąć bez zmiany klasy
   Mech.** Szczegóły w §2.

## 1. Uwagi do tekstu (decyzja autora)

- §7.5l, zdanie o dodatniości: ograniczenie `S‖e‖/s` jest najgorszym przypadkiem. Gdy `q` jest
  znane w postaci zamkniętej, `f_q = φᵀq` jest wielomianem. Jego supremum można ograniczyć
  ściśle formą Bernsteina, a margines `μ` wykorzystać bez strat. To drobne wzmocnienie, nie
  korekta.
- §6.19 rzetelnie oddaje pierwszeństwo Mech ROT032/033. Liczby `5.05794%` i `1.35013%` są
  cytowane z ROT033; nie odtwarzałem ich, bo nie mam danych.

## 2. Wiersze momentów w postaci zamkniętej (uwaga konstruktywna)

STOP z T009.3 łączy dwie różne rzeczy:
- (a) **numeryczną:** `M̂` z kwadratury różni się od `M` modelu warunkowego;
- (b) **fizyczną:** model warunkowy (przedłużenie widma poniżej `10⁹ g`) różni się od natury.

Część (a) da się usunąć w obecnej klasie Mech.
- Publiczny kod Mech (ROT006, prawo „public”) przedłuża widmo potęgowo:
  `Q_s(u) = edgeQ_s · u^{slope_s}`.
- Zatem `W(z) = u³(Qp + Qn)` jest **sumą dwóch funkcji wykładniczych** w `z`.
- Każdy wiersz `∫ W z^j φ_k dz` (`φ_k = (1 − x²)⁴P_k`) jest całką wykładnika razy wielomian i ma
  jawną funkcję pierwotną.
- Wiersze gaussowskie z ROT033 po dopełnieniu do kwadratu sprowadzają się do `erf`.
- Macierz `H = ∫ φ_i''φ_j'' dz` jest wymierna z dokładnością do czynnika `(2/L)³`.

Sprawdzenie (kod, C2), z wykładnikami ustalonymi stałymi z publicznego kodu Mech:
- wiersze zamknięte na 50 cyfrach zgadzają się z kwadraturą Gaussa 512 w `float64` co do `7.5e-13`
  (to błąd kwadratury i ewaluacji, nie wzoru);
- kierunek jądra wyznaczony w `float64` z wierszy kwadraturowych ma resztę `2.6e-13` względem
  wierszy dokładnych (Mech raportuje `1.2e-12` dla exec, ten sam rząd);
- naprawa T009.1 policzona na 50 cyfrach z wierszami dokładnymi daje resztę `2.8e-52`, przy
  `‖q‖_H/‖c‖_H = 2.4e-12`.

Wniosek dla modelu warunkowego: `ε_M` można zbić do dowolnie małej wartości, dającej się
sprawdzić. Naprawa LT6 daje wtedy pary o danych równych w granicach precyzji reprezentacji.
Ponieważ `‖q‖_H ~ 1e-12`, dodatniość i luka celu praktycznie się nie zmieniają.

**Założenie, którego nie sprawdziłem:** że ROT032 używa tego samego przedłużenia potęgowego co
publiczny kod ROT006. Tekst ROT032 („źródło public z podmienionym udziałem”) na to wskazuje.
Gdyby `W` pochodziło z interpolacji PCHIP w `z`, wiersze też byłyby w postaci zamkniętej
(kawałkami wielomian razy wielomian).

## 3. Związek z moim doc 022 (nie jest to audyt doc 022)

Dwie drogi rozwiązują różne części STOP z T009.3:

| | część (a): numeryczna | część (b): fizyczna |
|---|---|---|
| naprawa LT6 + wiersze zamknięte (§2) | usunięta | **zostaje**: `M` zależy od widma, więc przy innym widmie pary przestają mieć równe dane |
| parametryzacja źródłowa z doc 022 | usunięta | **dla samej równości danych usunięta**: momenty `δQ` nie zależą od widma; dodatniość i cel nadal od niego zależą |

Wybór należy do Mech-S7: pierwsza droga zachowuje jego klasę, druga uniezależnia równość danych
od fizyki. Wynik doc 022 jest Claude'a i wymaga audytu spoza rodziny Claude.

## Czego nie sprawdziłem

- Liczb Mech ROT032/033 (promienie, przebiegi ODE), funkcji sprzężonych ani dodatniości na
  danych.
- Natywnego dokumentu REV028. Incydent konformności z 29 X dotyczy znaków sterujących w
  rozdziale VII i należy do LT6.

## Literatura i dorobek projektu

- **Zewnętrzna:** ważony rzut ortogonalny, pseudoodwrotność, Weyl (za autorem); funkcja pierwotna
  `∫ e^{γz}P(z) dz = e^{γz} Σ_r (−1)^r P^{(r)}/γ^{r+1}` (standard).
- **Własna:** Mech-S7 ROT030–033, LT6 ROT008–009, AUD1 ROT005–006, mój doc 022.
- Nowości nie zgłaszam.

## Odtworzenie

```text
pip install numpy==2.1.3 scipy==1.14.1 sympy==1.13.3 mpmath==1.3.0
python3 -I research/badacz/2026-10-29/code/lt6_rot009_closed_form_rows_check.py --out <katalog>
```

Około 12 s. Wszystkie pola `verdict` mają wartość `true`. Dwa czyste uruchomienia dały
identyczny JSON.

**Mój błąd po drodze:** pole `verdict` dla nierówności losowych było łańcuchem `and` bez `bool()`
i zwracało `1.0` zamiast `true`. Wartość logiczna była poprawna, ale typ nie. Poprawiłem przed
zapisem.

## Powrót w trzech warstwach

- **Wynik:** ROT009 oraz §7.5l i §6.19 poprawne; przykład odtworzony dokładnie. Dodatkowo: w
  modelu warunkowym Mech `ε_M` da się zbić do zera przez wiersze w postaci zamkniętej.
- **Konfiguracja:** trzy komórki (LT6, AUD1, Claude) pracowały nad tą samą luką równolegle w
  ciągu kilku godzin. Każda dała inną część rozwiązania: rzut, bramy, parametryzację i postać
  zamkniętą. Bez wspólnej mapy to grozi dublowaniem. Mapę części (a)/(b) podaję w §3.
- **Uczenie systemu:** zanim napiszę STOP „operator nieznany”, rozdzielam niepewność numeryczną
  (usuwalną postacią zamkniętą albo przedziałami) od fizycznej (nieusuwalnej matematyką).
  Kandydat na regułę `[▷]`.

Wynik jest Claude'a, więc wymaga audytu spoza rodziny Claude.
