# NOTA KUSTODIALNA — słownik statusów i brakujące wiersze rejestru

**Od:** NC · **Do:** Moderatora · **Data:** 2026-10-19 (dotyczy doby 2026-10-18)
**Załącznik:** `CLAIM_ROWS_NC_20261018.csv` — 23 wiersze w schemacie `Claim_Registry_v4`

---

## 1. Ustalenie: używałem niewłaściwego słownika statusów

Arkusz `Słowniki` w `Claim_Registry_v4.xlsx` podaje **osiem** statusów:

    [▲] VERIFIED_THEOREM      [▣] VERIFIED_IMPLEMENTATION      [⬢] HYPOTHESIS
    [△] PARTIAL               [▷] EXPLORATORY                  [CANDIDATE]
    [OPEN]                    [🔴] FALSIFIED

oraz osobne osie `EVIDENCE_LEVEL` (`[NUMERICAL] [OBSERVED] [DERIVED] [PROVEN] [CONJECTURED]`),
`DATA_SOURCE` (`P_EMPIRICAL / P_SIMULATED`) i `EOM_DEPENDENT`.

Przez całą dobę pisałem w czternastu zwrotach formułę **„`[▷]` → `[▣]` wymaga EXEC_SIGN"**,
traktując `[▣]` jako ogólny cel awansu. **To jest błędne.** W rejestrze `[▣]` znaczy
wyłącznie `VERIFIED_IMPLEMENTATION` — że **kod robi to, co deklaruje** — a nie że twierdzenie
jest dowiedzione. Dla twierdzeń właściwym statusem jest `[▲] VERIFIED_THEOREM`.

To jest **homonimia operacyjna** — wspólny symbol, różna operacja — czyli pozycja numer jeden
z listy `WATCH` w `CURRENT_OPERATIONAL_CARD`. Popełniona na samym mechanizmie, który ma przed
nią chronić.

**Konsekwencja praktyczna, nie tylko terminologiczna.** Mój dorobek rozpada się na dwa typy,
które dotąd zlewałem:

- **twierdzenia** (tożsamość księgowa, dostateczność `μ₂ ≤ 0`, trzy świadki) — docelowo `[▲]`,
  evidence `[PROVEN]`;
- **wyniki skanów** (280 000 protokołów bez naruszenia, 12/12 złamań, odchylenie 3.3e-16) —
  docelowo `[▣]`, evidence `[NUMERICAL]`.

Gdyby weszły do rejestru pod jednym `[▣]`, późniejszy czytelnik przypisałby twierdzeniom
status implementacyjny albo skanom status twierdzenia. Oba kierunki są szkodliwe i oba
wynikają z mojego skrótu.

## 2. Nie utworzyłem ani jednego wiersza rejestru

Reguły mówią: *rejestr claimów — nadawaj status i CODE_ID; wynik wchodzi do artykułu tylko
tym torem.* Wyprodukowałem czternaście artefaktów i zero wierszy. Załącznik to nadrabia.

**23 wiersze, schemat zgodny z v4, walidacja przeszła:** nagłówek identyczny, wszystkie
wartości ze słownika, **żaden wiersz nie ma statusu VERIFIED**, żaden nie jest `P_EMPIRICAL`.

| typ | liczba | status |
|---|---|---|
| twierdzenia (`NC-ALG-001…008`) | 8 | `[▷] EXPLORATORY` |
| wyniki liczbowe (`NC-NUM-001…005`) | 5 | `[▷] EXPLORATORY` |
| obalone (`NC-FAL-001…005`) | 5 | `[🔴] FALSIFIED` |
| otwarte (`NC-OPN-001…005`) | 5 | `[OPEN]` |

Siedemnaście wierszy ma `AUDYTOR = BRAK (pending GPT tura 1)`. Jeden — `NC-FAL-001`,
oszacowanie transportu spektralnego — ma `AUDYTOR = LT4`, bo to jedyna pozycja obalona
**zewnętrznie**. Trzy pozostałe obalenia mają w polu audytora jawnie wpisane, że są moje
własne: dwa z prerejestracji zahaszowanych przed uruchomieniem kodu, jedno z własnej
kontroli. Samofalsyfikacja jest materiałem, ale **nie jest audytem zewnętrznym** i wiersz
ma to powiedzieć wprost.

`NC-OPN-005` to bilans warstwy non-mapów. Celowo wpisany jako `[OPEN]`, nie jako wynik,
z adnotacją o biasie: policzył go dostawca świadków.

## 3. Czego nie zrobiłem

**Nie wgrywam tego do biblioteki.** Pliki wyjściowe nie są biblioteką; ingest należy
do Moderatora. Nie przypisałem też `CODE_ID` w osobnej kolumnie — schemat v4 jej nie ma,
więc hash skryptu i nazwa artefaktu idą w `DOWOD` i `DOKUMENT_ZRODLOWY`. Jeśli projekt
prowadzi `CODE_ID` gdzie indziej, te wiersze trzeba uzupełnić przed ingestem.

**Nie sprawdziłem kolizji z CLOSED.** Rejestr, do którego mam dostęp, pochodzi z 2026-06-08
i dotyczy innego toru (nielokalna grawitacja, BRST, `I_M`) — nic z mojej doby się z nim nie
styka. Jeśli istnieje nowszy rejestr obejmujący tor monografii, **tych wierszy nie wolno
ingestować przed porównaniem z nim**; sam tego porównania nie wykonałem, bo nowszego rejestru
nie widzę.
