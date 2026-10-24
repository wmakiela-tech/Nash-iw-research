# PREREG — NC-OPN-002: czy przy μ₂ > 0 sufit ekstrakcji jest skończony, i czy równa się M(G)

ZAPISANE PRZED URUCHOMIENIEM KODU. Komórka NC, rola **Badacz**. 2026-10-24.
Wiersz: `NC-OPN-002`, otwarty od 2026-10-18 — najstarszy mój. Posuwam go, nie otwieram nowego.
PATRON: brak.

## 1. Co jest znane z LITERATURY — szukane, nie zakładane

Polecenie Moderatora: wiedza naukowa dostępna w sieci ma chronić przed odkrywaniem
zbadanego. Wykonałem przeszukanie przed postawieniem hipotez. Znalezione gospodarze:

- **`M(G) = sup_{t≥0}‖e^{tG}‖`** jest badanym obiektem: „maksymalny wzrost przejściowy".
  Literatura: twierdzenie macierzowe Kreissa i jego stała, Trefethen–Embree *Spectra and
  Pseudospectra*; optymalizacja stałej Kreissa — Apkarian–Noll.
- **`M(G) = 1 ⟺ μ₂(G) ≤ 0`** jest **klasyczne** (kontraktywność półgrupy ⟺ dyssypatywność),
  Dahlquist 1958 / Lozinskii 1958, nowocześnie Söderlind BIT 46(3) 2006.
- **Łańcuch Kreissa**: stała Kreissa `K(G)` i `M(G)` są równoważne z czynnikiem zależnym
  od wymiaru (Spijker), więc `M(G) < ∞` dla każdej macierzy, a dla Hurwitza `e^{tG} → 0`.
- **Gramian odczytu** mam z własnej linii, od M13 (audyt ROT11, zapisany w ART017):
  `L₁ = e^{Gt₁}`, `L_{j+1} = e^{G(t_{j+1}−t_j)}D_d(u_j)L_j`,
  `W = Σ_j (1−u_j)² L_jᵀ e eᵀ L_j`, i **`γ² sup_{‖v₀‖=1}‖c‖₂² = λ_max(W)`**.
  To jest właściwy obiekt optymalizacji i nie muszę go wyprowadzać.

**Czego NIE znalazłem:** żadnej pracy wiążącej funkcjonał **sekwencyjnej ekstrakcji
z odrzutem** z `M(G)`. Literatura pomiarów sekwencyjnych, którą znalazłem, jest kwantowa
(słabe pomiary, wartości słabe) i ma inny host; literatura obserwowalności/energii wyjścia
nie obejmuje impulsowych resetów stanu w tej postaci. `SEARCH FAILURE IS NOT NOVELTY` —
to brak trafienia w ograniczonym przeszukaniu, nie dowód nowości.

## 2. Dlaczego pytanie jest otwarte, i czym się różni od tego, co już obalono

Przy `μ₂ ≤ 0` sufit `γ‖c‖₂ ≤ 1` jest dowiedziony i ostry (ART011; konieczność — M13 ROT11).
Mechanizm: z tożsamości `(γc_j)² = (A_j² − A_{j+1}²)tanh(γs_j/2)`, sumowanie teleskopuje
i przy nierosnącym `A` daje `γ²‖c‖₂² ≤ tanh(γs/2) ≤ 1`.

Przy `μ₂ > 0` teleskopowanie **nie** jest ograniczone przez `A_1² ≤ 1`, bo swobodna ewolucja
**dolewa** do budżetu między pomiarami. `NC-FAL-006` zapisuje, że moje dawne „przy `μ₂ > 0`
sufit NIE istnieje" było **za mocne** — M13 wykazał, że `μ₂ > 0` obala konkretny sufit `1/γ`,
a nie implikuje `sup = ∞`. Pytanie, czy `sup` jest skończony, zostało wtedy **otwarte**.
To jest dokładnie `NC-OPN-002`.

## 3. Dwie KONKURENCYJNE hipotezy — stawiam obie, bo nie wiem którą

**H-A (jeden mocny pomiar jest optymalny).** `sup_{protokół, e, d} γ‖c‖₂ = M(G)`.
Argument za dolnym ograniczeniem jest pewny: jeden pomiar o sile `s → ∞` w chwili `t`,
z `e` wyrównanym do `e^{Gt}v₀/‖e^{Gt}v₀‖`, daje `γ|c| → ‖e^{Gt}v₀‖`, a supremum po `v₀` i `t`
to `M(G)`. Więc **`sup ≥ M(G)` jest dowiedzione**, niezależnie od tego, która hipoteza padnie.
H-A twierdzi dodatkowo, że powtarzanie nie bije jednego mocnego pomiaru.

**H-B (powtórne wejście w przejściowy wzrost akumuluje).** `sup > M(G)`, być może
nieograniczony. Mechanizm: po pomiarze stan jest skontraktowany wzdłuż `d`, ale nowy stan
może znów mieć kierunek rosnący, więc można **wejść w transient ponownie** i zsumować wiele
mniejszych ekstrakcji. Przy słabych pomiarach zysk z powtarzania w sektorze `μ₂ ≤ 0` wynosił
`1/√(1−e^{−2γs})` i rośnie bez ograniczenia przy `s → 0`; pytanie, czy przy `μ₂ > 0`
to pokonuje `M(G)`.

**Nie przewiduję, która jest prawdziwa.** Dane, które mam, są dwuznaczne: ART011 §3 zmierzył
dla macierzy Metzlera M13 `sup = 1,085788` przy `M(A) = 1,086613`, czyli **poniżej** `M(A)`
i blisko — co pasuje do H-A, ale było zamiataniem jednopomiarowym, więc nie testowało H-B.

## 4. Procedura

Maksymalizuję `λ_max(W)` z gramianu M13 po: liczbie pomiarów `m = 1…8`, czasach, siłach,
kierunku odczytu `e`, kierunku odrzutu `d`. Dla każdej macierzy porównuję z `M(G)` liczonym
niezależnie przez gęste próbkowanie `‖e^{Gt}‖` plus zagęszczenie wokół maksimum.

**Nauka z wczoraj (`NC-OPN-024`): mój optymalizator jest słaby** — Nelder–Mead nie znalazł
nawet świadka, którego sam podałem. Dlatego: (a) dokładam **kandydatów strukturalnych**
(pojedynczy mocny pomiar w argmax `‖e^{Gt}‖`; serie równoodstępowe; `e = d` i `e ⊥ d`),
(b) rosnące `m`, żeby zobaczyć trend, (c) wielokrotne restarty, (d) jawnie raportuję,
czy optymalizator odtwarza znane dolne ograniczenie `M(G)` — jeśli nie, jego wyniki powyżej
nie są dowodem niczego.

Macierze testowe: Metzler M13 `[[−1.1,4],[1,−4.1]]`; weryfikator Hurwitza `[[−1,4],[0,−1]]`;
separator INT7 `[[−1,100],[0,−1]]`; rodzina `[[−1,k],[0,−1]]` dla rosnącego `k`, gdzie
`M` rośnie, a widmo jest stałe.

## 5. Falsyfikatory

- **F1, PIERWSZY.** Jeśli optymalizator nie odtworzy `≥ M(G) − tol` dla żadnej macierzy,
  to jest zbyt słaby i **wstrzymuję wnioski** — tak jak wczoraj, gdy nie znalazł Householdera.
- **F2.** H-A fałszywa, jeśli jakikolwiek protokół da `γ‖c‖₂ > M(G) + tol`.
- **F3.** H-B fałszywa, jeśli przy rosnącym `m` maksimum **nie** przekracza `M(G)` i dąży
  do niego od dołu.
- **F4.** Jeśli maksimum rośnie z `m` bez widocznego nasycenia, to przesłanka za `sup = ∞`,
  ale **nie dowód** — zapiszę to jako przesłankę, nie wynik.
- **F5.** Kontrola spójności: przy `μ₂ ≤ 0` (np. `G = [[0,1],[−1,0]]`, `μ₂ = 0`) maksimum
  musi wyjść `≤ 1 + tol`, bo to przypadek już dowiedziony. Jeśli wyjdzie więcej, mój kod
  jest zły, a nie twierdzenie.

## 6. Czego nie twierdzę z góry

Nie twierdzę nowości: `M(G)`, stała Kreissa i norma logarytmiczna to dojrzała analiza
macierzowa; gramian odczytu dał M13. Nowy może być **tylko** związek między nimi, i to pod
warunkiem, że wyjdzie i że nie znajdę go w literaturze po fakcie. Status `[▷]`, brak
EXEC_SIGN, audyt zewnętrzny obowiązkowy.
