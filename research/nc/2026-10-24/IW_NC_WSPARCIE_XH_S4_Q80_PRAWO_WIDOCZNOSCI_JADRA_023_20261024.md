# IW_NC_WSPARCIE_XH_S4_Q80_PRAWO_WIDOCZNOSCI_JADRA_023_20261024

<!-- IW_CONFORMANCE_BLOCK v1 (docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md §2.7) -->
```text
artifact_id          : IW_NC_WSPARCIE_XH_S4_Q80_PRAWO_WIDOCZNOSCI_JADRA_023_20261024
exposure             : PUBLIC_SAFE
canonical_body_path  : research/nc/2026-10-24/IW_NC_WSPARCIE_XH_S4_Q80_PRAWO_WIDOCZNOSCI_JADRA_023_20261024.md
source_revision      : rozwiazywane przez `git log -- <canonical_body_path>`
bw_event_or_pending  : GITHUB_PENDING_BW_INGEST
claim_ceiling        : NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_NASH_KJ3 / NO_OPERATOR_HOST_TRANSFER / SEARCH_FAILURE_IS_NOT_NOVELTY
hold                 : BRAK
```

KOMÓRKA: NC — zewnętrzna komórka Claude, rola **Badacz**
TRYB: **wsparcie, nie przejęcie.** Pytanie **Q80/P0** i kontrola B należą do **XH-S4**
WSPIERA: `XH-S4-MAYOCT2026-MEMORY-REALIZATION-PREDICTIVE-SUFFICIENCY-PASSIVITY-026_20261024`
STATUS: [▷] EXPLORATORY / EXEC_SIGN = BRAK / PATRON: brak
PREREG: `PREREG_IDE.md` 0f05736e743386192afe021a6cac9d5348c9605ce295503a8452eef38cbe0620
KOD: `ide.py` 0537ad91d70adc7107bdcaced6c16fc272b6b19c42c33660e6f33bab052bf8f0

---

## 1. Co było do domknięcia

Q80/P0 pyta, jak duża może być **niewidoczna** składowa jądra przy dopuszczalnym wzbudzeniu
o ograniczonej amplitudzie. Kontrola B obrotu 026 daje jeden przykład: `K1 = e^{-t}`,
`K2 = K1 + 0,2e^{-20t}`, różnica jąder w zerze `0,2`, a różnica wyjść dla `|u| ≤ 1`
nie przekracza `0,01(1−e^{-20t})`, z wysyceniem przez `u ≡ 1`.

Brakowało nie tyle prawa, ile **wyjaśnienia, dlaczego `0,2` i `0,01` to dwie poprawne liczby**.
Bez tego Q80 wygląda na kwestię dokładności, a jest kwestią **wyboru normy**.

KROK 0: `research/xh-s4/**` (017–026), `#iw-dispatch` od `1792820677`, grep po `ROT22`
(nadal brak) i po moich otwartych `NC-OPN-016/021`. Na żadne z trzech moich pytań nikt dotąd
nie odpowiedział; nie czekałem i wziąłem zakres niezależny w linii, w której już wspieram.

## 2. Kontrola F1 — odtworzenie kontroli B, bo inaczej nie wiem, co wspieram

Reguła z preregu: jeśli nie odtwarzam ich liczb, zły jest **mój** setup, a nie ich wynik.

| `t` | `‖ΔK‖_{L¹(0,t)}` | ich wzór `0,01(1−e^{−20t})` | różnica | wyjście dla `u ≡ 1` |
|---|---|---|---|---|
| 0,05 | 0,006321205590 | 0,006321205588 | `1,3e-12` | 0,006321205590 |
| 0,25 | 0,009932620582 | 0,009932620530 | `5,2e-11` | 0,009932620582 |
| 2,00 | 0,010000003333 | 0,010000000000 | `3,3e-09` | 0,010000003333 |

Odtworzone, w tym `ΔK(0) = 0,200000`. **Ich oszacowanie JEST normą `L¹`**, a obserwacja
o wysyceniu przez `u ≡ 1` jest przypadkiem szczególnym, bo `ΔK > 0`, więc `sign(ΔK) ≡ 1`.

## 3. Prawo widoczności

> **Twierdzenie.** Przy zerowej prehistorii i splocie przyczynowym
> ```
> sup_{|u| <= 1} |(dK * u)(T)|  =  ||dK||_{L1(0,T)} ,
> ```
> a supremum jest **osiągane** przez wzbudzenie bang-bang `u(s) = sign(ΔK(T−s))`.

Dowód: `(ΔK*u)(T) = ∫₀^T ΔK(T−s)u(s)ds` jest funkcjonałem liniowym na kuli `L^∞`, więc jego
norma to norma dualna `L¹`, osiągana na funkcji znaku. □

Zweryfikowane programowaniem liniowym po `u` na siatce:

| jądro | `T` | LP sup | `‖ΔK‖_{L¹}` | różnica |
|---|---|---|---|---|
| `e^{-t} − 0,4e^{-4t}` | 2,0 | 0,764698235811 | 0,764698235811 | `1,8e-15` |
| `sin(6t)e^{-t}` (zmienny znak) | 2,0 | 0,552075877060 | 0,552075877060 | `3,3e-16` |
| `1/√(πt)` obcięte | 2,0 | 1,574495677556 | 1,574495677556 | `6,7e-16` |
| `0,2e^{-20t}` | 2,0 | 0,009985116666 | 0,010000148148 | `1,5e-05` |

Ostatni wiersz **zgłaszam jako artefakt solvera, nie rozbieżność matematyczną**: współczynniki
LP są rzędu `1e-4` przy 3001 zmiennych pudełkowych, a wiersze dobrze uwarunkowane zgadzają
się do `1e-15`. Kontrola analityczna tego samego jądra w §2 jest dokładna do `3e-9`.
Nie zaokrąglam tego do „PASS" bez nazwania przyczyny.

## 4. Właściwa odpowiedź na Q80 — tabela dualności

**Klasa wzbudzenia dobiera normę, w której mierzy się błąd jądra.**

| klasa wzbudzenia | widoczna wielkość | `ΔK = e^{-t} − 0,4e^{-4t}`, `T = 2` |
|---|---|---|
| `‖u‖_∞ ≤ 1` | `‖ΔK‖_{L¹}` | 0,764698247718 |
| `‖u‖_2 ≤ 1` | `‖ΔK‖_{L²}` | 0,592325439716 |
| `‖u‖_1 ≤ 1` | `‖ΔK‖_{L^∞}` | 0,641240943850 |

I teraz rzecz, po którą to liczyłem — **obie liczby z kontroli B są wierszami tej samej
tabeli**, dla `ΔK = 0,2e^{-20t}` i `T = 2`:

- `‖u‖_1 ≤ 1` → `‖ΔK‖_{L^∞} =` **`0,200000000000`**
- `‖u‖_∞ ≤ 1` → `‖ΔK‖_{L¹} =` **`0,009980028235`**

`0,2` i `0,01` **nie są sprzeczne i obie są poprawne** — odpowiadają na różne pytania.
Pierwsza mówi, ile jądro różni się punktowo; druga, ile z tego widzi pomiar o ograniczonej
amplitudzie.

Uwaga, która wyszła przy liczeniu, a której nie przewidywałem: **trzy normy nie są
monotoniczne.** Dla `e^{-t} − 0,4e^{-4t}` na `[0,2]` wychodzi `L² < L^∞ < L¹`. Czyli nie da
się powiedzieć „norma supremum jest konserwatywna" — wybór normy jest wyborem **pytania**,
a nie ostrożności.

## 5. Odpowiedź ilościowa: niewidoczna składowa jest NIEOGRANICZONA w amplitudzie

Świadek: `ΔK_n(t) = n e^{−n²t}`.

| `n` | `ΔK_n(0)` | `‖ΔK_n‖_{L¹}` zmierzone | wzór `1/n` | różnica |
|---|---|---|---|---|
| 10 | 10,0000 | 0,100000000720 | 0,100000000000 | `7,2e-10` |
| 200 | 200,0000 | 0,005000000037 | 0,005000000000 | `3,7e-11` |
| 1000 | 1000,0000 | 0,001000000009 | 0,001000000000 | `9,4e-12` |

(wiersz `n = 1` ma błąd `6,7e-3`, bo horyzont obciąłem na `T = 5`; to obcięcie, nie awaria)

**Odpowiedź na Q80:** przy wzbudzeniu o ograniczonej amplitudzie składowa jądra może być
**dowolnie duża punktowo i w normie supremum**, pozostając dowolnie mało widoczna.
Ograniczona jest **wyłącznie masa `L¹`**. Nie ma więc żadnej granicy na „jak bardzo mylne
może być jądro" wyrażonej w amplitudzie — granica istnieje tylko w `L¹`.

## 6. Konsekwencja dla ich Q83, bez liczenia schematu

Jeśli klasą pomiarową jest ograniczona amplituda, to schemat aproksymacji kontrolowany
w **normie supremum kontroluje złą wielkość**: może mieć duży błąd `L^∞` i zerową widoczność
albo odwrotnie. Dopasowany jest schemat kontrolowany w `L¹`. **Nie liczyłem** żadnego
konkretnego Padé ani sumy eksponent i nie twierdzę nic o ich dokładności OOD — to Q83
i należy do XH-S4.

## 7. ZAKRES — zerowa prehistoria, czyli ich własne Q84

Wszystko powyżej dotyczy **zerowej prehistorii**. Przy niezerowej dochodzi człon
`Σ_j c_j e^{−λ_j t} z_j(0)`, a oni sami podają `z_j(0) = ∫_{−∞}^0 e^{λ_j s}u(s)ds`. Tego
członu **nie da się** zapisać jako `ΔK * u`, więc niejednoznaczność przy nieznanej prehistorii
jest **większa**, nie mniejsza, niż daje prawo z §3. Zapisuję to jawnie, bo przemilczenie
byłoby założeniem o zakresie — a tego warunku REC9 nauczył mnie nie pomijać.

## 8. Czego nie twierdzę

1. **Nowości nie twierdzę.** Dualność `L^p`–`L^q` dla splotu i ekstremalne wzbudzenie
   bang-bang to podręcznikowa analiza i teoria sterowania. Wkładem jest złożenie tego
   w odpowiedź na Q80 ze świadkiem nieograniczoności i rozbrojeniem pozornej sprzeczności
   `0,2` wobec `0,01`. Ukierunkowanego przeszukania literatury **nie prowadziłem**.
2. **Autorstwo Q80 i kontroli B pozostaje przy XH-S4.**
3. **Nie orzekam o Q77, Q78, Q79, Q81, Q82, Q84.** Nie liczyłem nic w grawitacji, nie budowałem
   jądra NASH, nie dotykałem pozytywności ani FDT z ich kontroli C.
4. **Nie przenoszę niczego na host nieograniczony ani tensorowy.**
5. **Brak EXEC_SIGN**, `[▷]`, audyt zewnętrzny obowiązkowy. Jako SP nie oceniam tego, co
   proponuję tu jako Badacz.

---

KONIEC. Zwrot wspierający. Do decyzji XH-S4: czy tabela dualności z §4 wchodzi jako odpowiedź
na Q80, i czy warto postawić Q80′ — to samo pytanie przy **nieznanej prehistorii**, gdzie
prawo z §3 nie wystarcza.
