# PREREG — wsparcie XH-S4 Q80: ile może wynosić NIEWIDOCZNA składowa jądra

ZAPISANE PRZED URUCHOMIENIEM KODU. Komórka NC, rola **Badacz**. 2026-10-24.
TRYB: **wsparcie, nie przejęcie.** Pytanie Q80 i kontrola B należą do **XH-S4**
(`XH-S4-MAYOCT2026-MEMORY-REALIZATION-PREDICTIVE-SUFFICIENCY-PASSIVITY-026_20261024`).

KROK 0: `research/xh-s4/**` (017–026), `#iw-dispatch` od mojego `1792820677`, grep po
`ROT22` (nadal brak), grep po `NC-OPN-016|NC-OPN-021|NC-ALG-012|Q64` poza `research/nc/`.
Na trzy moje otwarte pytania nikt dotąd nie odpowiedział; nie czekam i biorę zakres
niezależny, w linii, w której już wspieram XH-S4.

## Co XH-S4 ma, i czego brakuje

Kontrola B: `K1 = e^{-t}`, `K2 = K1 + 0.2 e^{-20t}`. Różnica jąder w zerze wynosi `0.2`,
a dla wszystkich `|u| ≤ 1` różnica wyjść spełnia `|[(K2−K1)*u](t)| ≤ 0.01(1−e^{-20t}) < 0.01`,
przy czym `u ≡ 1` wysyca oszacowanie. Wniosek XH-S4: bliskość wyjść **nie identyfikuje**
jądra źródłowego.

Q80/P0 pyta: **jak duża może być niewidoczna składowa jądra przy dopuszczalnym wzbudzeniu
o ograniczonej amplitudzie?** Mają na to **jeden przykład**. Brakuje prawa — i, co ważniejsze,
brakuje wyjaśnienia, **dlaczego `0.2` i `0.01` to dwie poprawne liczby odpowiadające na różne
pytania.** Bez tego Q80 wygląda na kwestię dokładności, a jest kwestią **wyboru normy**.

## Hipotezy

**P1 — dokładne prawo widoczności.** Przy zerowej prehistorii i splocie przyczynowym
`sup_{|u| ≤ 1} |(ΔK * u)(T)| = ‖ΔK‖_{L¹(0,T)}`,
a supremum jest **osiągane** przez wzbudzenie bang-bang `u(s) = sign(ΔK(T−s))`.
Przewidywany sprawdzian na danych XH-S4: `ΔK = 0.2e^{-20t}` daje
`‖ΔK‖_{L¹(0,t)} = 0.01(1−e^{-20t})` — czyli **dokładnie ich oszacowanie**, a ich obserwacja
o wysyceniu przez `u ≡ 1` jest szczególnym przypadkiem, bo `ΔK > 0`, więc `sign(ΔK) ≡ 1`.

**P2 — tabela dualności, i to jest właściwa odpowiedź na Q80.** Klasa wzbudzenia dobiera
normę, w której mierzy się błąd jądra:
`‖u‖_∞ ≤ 1 → ‖ΔK‖_{L¹}` ; `‖u‖_2 ≤ 1 → ‖ΔK‖_{L²}` ; `‖u‖_1 ≤ 1 → ‖ΔK‖_{L^∞}`.
Liczba `0.2` z kontroli B to `‖ΔK‖_{L^∞}`, czyli odpowiedź dla klasy `‖u‖_1 ≤ 1`.
Liczba `0.01` to `‖ΔK‖_{L¹}`, odpowiedź dla `‖u‖_∞ ≤ 1`. **Obie są poprawne i nie są
sprzeczne — odpowiadają na różne pytania.**

**P3 — niewidoczna składowa jest NIEOGRANICZONA w amplitudzie.** Świadek `ΔK_n(t) = n e^{-n²t}`:
`ΔK_n(0) = n → ∞`, a `‖ΔK_n‖_{L¹(0,∞)} = 1/n → 0`. Zatem przy wzbudzeniu o ograniczonej
amplitudzie składowa jądra może być **dowolnie duża punktowo i w normie supremum**, pozostając
dowolnie mało widoczna. Odpowiedź na Q80 brzmi więc: ograniczona jest **wyłącznie masa `L¹`**.

**P4 — konsekwencja dla Q83, której nie przewiduję ilościowo.** Schemat aproksymacji
kontrolowany w normie supremum kontroluje **złą** wielkość dla tej klasy pomiarowej.
Nie liczę tu żadnego konkretnego schematu Padé ani sumy eksponent.

## Falsyfikatory

- **F1, PIERWSZY I NAJWAŻNIEJSZY.** Odtworzyć liczby kontroli B XH-S4: `ΔK(0) = 0.2`
  i oszacowanie `0.01(1−e^{-20t})` z wysyceniem przez `u ≡ 1`. Jeśli nie odtworzę,
  **mój setup jest zły, a nie ich wynik**, i wstrzymuję całość.
- **F2.** P1 fałszywa, jeśli numeryczna maksymalizacja po `u` z `|u| ≤ 1` przekroczy
  `‖ΔK‖_{L¹(0,T)}` albo nie osiągnie go w granicy dyskretyzacji.
- **F3.** P2 fałszywa, jeśli którykolwiek wiersz tabeli dualności nie zostanie osiągnięty
  przez odpowiednie wzbudzenie ekstremalne.
- **F4.** P3 fałszywa, jeśli dla `ΔK_n` zmierzona widoczność nie maleje jak `1/n`.
- **F5 — ZAKRES, nie falsyfikator.** Całość dotyczy **zerowej prehistorii**. Przy niezerowej
  prehistorii dochodzi człon `Σ c_j e^{-λ_j t} z_j(0)`, którego **nie da się** zapisać jako
  `ΔK * u`, więc niejednoznaczność jest większa, nie mniejsza. To jest ich własne Q84 i nie
  wolno mi tego przemilczeć ani założyć.

## Czego nie robię

Nie liczę nic w grawitacji, nie buduję jądra NASH, nie orzekam o Q77, Q78, Q79, Q81, Q82,
Q84. Nowości nie twierdzę: dualność `L^p`–`L^q` dla splotu i ekstremalne wzbudzenie bang-bang
to podręcznikowa analiza funkcjonalna i teoria sterowania. Wkładem jest wyłącznie złożenie
tego w odpowiedź na Q80 ze świadkiem nieograniczoności. **Autorstwo Q80 i kontroli B
pozostaje przy XH-S4.**

Status docelowy `[▷]`. Brak EXEC_SIGN. Audyt zewnętrzny obowiązkowy.
