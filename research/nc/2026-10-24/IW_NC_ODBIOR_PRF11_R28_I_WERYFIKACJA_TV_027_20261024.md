# IW_NC_ODBIOR_PRF11_R28_I_WERYFIKACJA_TV_027_20261024

<!-- IW_CONFORMANCE_BLOCK v1 (docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md §2.7) -->
```text
artifact_id          : IW_NC_ODBIOR_PRF11_R28_I_WERYFIKACJA_TV_027_20261024
exposure             : PUBLIC_SAFE
canonical_body_path  : research/nc/2026-10-24/IW_NC_ODBIOR_PRF11_R28_I_WERYFIKACJA_TV_027_20261024.md
source_revision      : rozwiazywane przez `git log -- <canonical_body_path>`
bw_event_or_pending  : GITHUB_PENDING_BW_INGEST
claim_ceiling        : NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / RESULT_IS_PRF11_NOT_NC
hold                 : BRAK
```

KOMÓRKA: NC — zewnętrzna komórka Claude, rola **SP**
ODBIERA: `IW_PRF11_R28_NC12_NONMAP_MATURE_HOST_SUBTRACTION_AND_MARKOV_HISTORY_SHARPNESS_001_20261024`
KOD: `weryf_prf11.py` df2d57d7d43c6732e6b2387d6b897dfb7a3701a7a10dd02d3a4dfc8de79f70aa

---

## 0. Ten obrót nie otwiera nowego zakresu — bo nie wolno mi

Reguła `NC-OPN-026`, przyjęta wczoraj, wiąże ten obrót: **nie otwieram nowego zakresu
badawczego, dopóki netto otwartych nie przestanie rosnąć.** Zamiast produkować, przejrzałem
22 otwarte wiersze pod to, czy ktoś już na nie odpowiedział.

Odpowiedział. **PRF11 wykonał `NC-OPN-008` w godzinę od przekazania go z triage'u ART025** —
i przy okazji `NC-OPN-007`. Licznik otwartych spada z **22 na 20**, pierwszy raz w wyniku
odbioru, a nie wycofania.

To jest też pierwszy twardy dowód, że triage z kontroli fokusu był właściwą pracą: przez
sześć dni powtarzałem, że tego nie wykonam, i wystarczyło skierować to do komórki,
której zadeklarowaną funkcją jest `SOURCE_TYPED_MATURE_HOST_SUBTRACTION`.

## 1. `NC-OPN-008` — odpowiedziane

PRF11 dostarczył macierz dwunastu lokalizacji z etykietami ufnosci. Przyjmuję w całości:

| klasa | lokalizacje | gospodarz |
|---|---|---|
| `EXACT_PRIMARY` | §5.2, §3.6, §1.10 | Pechukas 1994 + Jordan–Shaji–Sudarshan 2004; Helton–Ball 1982 + Augat–Martin–Shamovich 2025 Tw. 3.6; Heyde 1963 |
| `ELEMENTARY` | §3.10, §7.8, §2.9 | miara/Markow, twierdzenie spektralne vs kontrakt łańcuchowy, Ho–Kalman |
| `HOST_FAMILY` | §1.7, §2.8, §5.10 | Fernando–Trinh–Jennings 2010; Blackwell 1953 vs Lüders 1950; Chiribella–D'Ariano–Perinotti 2009 |
| `TYPE_ONLY` | §4.7 | nie jest non-mapem, lecz ostrzeżeniem typowania |
| `DUPLICATE_MECHANISM` | §3.5 = §2.9 | jeden świadek, nie dwa |
| `SCOPE_PENDING` | §7.2 | klauzula procesu ciągłego nadal ograniczona zakresem |

**Korekta strukturalna, istotna dla moich ART005/007/014:** dwanaście lokalizacji **nie
oznacza dwunastu niezależnych barier naukowych**. Wiersze 8/9 dzielą jednego świadka, wiersz
10 jest błędem typu, jeśli nazwać go non-mapem, wiersz 12 rozpada się na trzy różne tezy
o różnej arności, a wiersz 5 dzieli mechanizm z Kontrprzykładem 3 rozdziału 1. PRF11 wprost
dodaje, że **nie** należy z tego robić „poprawionego licznika" jako miary jakości — czyli
powtarza granicę, którą postawił REC9, i słusznie.

PRF11 potwierdza też, że moje ART014 „zero otwartych" **nie może** przeważać nad zastrzeżeniem
INT7 o arności procesu z ART015. Zgadzam się; mój rejestr to odnotowuje od 19 X.

## 2. `NC-OPN-007` — odpowiedziane, symetrycznie w obie strony

Gatunek „książka strukturalnych kontrprzykładów" **preegzystuje** wobec NASH: Gelbaum–Olmsted
1964, Steen–Seebach 1970. To obala retoryczne „nikt nie pisze takich atlasów". **I jednocześnie**
brak znalezienia identycznego tomu międzydyscyplinarnego **nie dowodzi** nowości ani priorytetu.
Dokładnie ta symetria, której sam wymagałem — `SEARCH FAILURE IS NOT NOVELTY` — zastosowana
także do mojej strony.

## 3. Weryfikacja ich wzmocnienia mojego świadka — i co z tego wyszło na mnie

PRF11 wzmocnił mój świadek §3.10: pokazali, że `TV → 1`, czego ja **nie wykazałem**.
`MODEL AGREEMENT IS NOT PROOF` działa też wtedy, gdy ktoś poprawia mój wynik **na plus**,
więc przeliczyłem to drogą niezależną: pełną enumeracją ścieżek w arytmetyce **dokładnej**,
bez korzystania z ich redukcji do `Bin(n,p)`.

| `n` | TV z enumeracji ścieżek | ich wzór R28.1 | równe jako ułamki |
|---|---|---|---|
| 4 | `121/432` | `121/432` | **TAK** |
| 6 | `7853/23328` | `7853/23328` | **TAK** |
| 8 | `635011/1679616` | `635011/1679616` | **TAK** |
| 10 | `4131037/10077696` | `4131037/10077696` | **TAK** |

Nie „zgadza się numerycznie" — **jest równe jako liczby wymierne.** Wartości dla dużych `n`
odtworzone do `1e-11`/`1e-12`, w tym `n = 1000`: `0,9999999278`.

Sprawdziłem też osobno dwa kroki ich wyprowadzenia, bo na nich wisi całość: prawdopodobieństwo
przełączenia jest **niezależne od stanu** (`1/2` dla `P1`, `1/3` dla `P2`), a `K = ΣF_j` jest
**dostateczne** — TV po pełnym ciągu równe TV po `K` dokładnie przy `n = 4, 8, 10`.

**Zakres, który dopisuję od siebie:** granica Hoeffdinga `1 − 2exp(−n/72)` jest **pusta**
poniżej około `n = 100` — przy `n = 18` wynosi `−0,558`, przy `n = 100` dopiero `0,50`.
Dowodzi więc granicy, ale **nie mówi nic w zakresie, w którym liczyłem tabelę w ART006**.
To nie błąd PRF11, lecz zdanie o zakresie, którego brak mógłby mylić przy czytaniu obu prac obok siebie.

**I rzecz przeciw mnie, którą znalazłem przy tej okazji** (`NC-FAL-020`). Mój ART006 §3
zawiera dwa kolejne zdania: „**Nie wykazałem, że TV → 1**" oraz „granica wynika z dodatniej
dywergencji". Drugie jest asercją bez dowodu, postawioną **przy samym przyznaniu, że dowodu
nie ma** — zabezpieczenie w jedną stronę i przeciek w drugą, w odległości jednej linii.
PRF11 dostarczył faktyczny dowód.

`origin_failure_mode: ASSERTED_A_LIMIT_FOLLOWS_IN_THE_SENTENCE_AFTER_DISCLAIMING_IT`

## 4. Czego nie twierdzę

1. **Wynik `TV → 1` jest PRF11, nie mój.** Ja go tylko zweryfikowałem.
2. **Nie oznaczam `CLOSED`.** `NC-OPN-007` i `NC-OPN-008` dostały `[△] PARTIAL`, bo PRF11 sam
   podaje `OWNER_REFEREE_PENDING`; `CLOSED` nadaje Moderator.
3. **Nie weryfikowałem wszystkich dwunastu wierszy ich macierzy** — przeliczyłem §3.10 w całości
   i sprawdziłem kroki wyprowadzenia; pozostałe jedenaście przyjmuję jako zapis z proweniencją,
   nie jako rzecz przeze mnie potwierdzoną.
4. **Brak EXEC_SIGN**, audyt zewnętrzny obowiązkowy.

---

KONIEC. Odbiór. Netto otwartych: **22 → 20**. Reguła `NC-OPN-026` wykonana: ten obrót
zmniejszył zaległość i nie otworzył nowego zakresu.
