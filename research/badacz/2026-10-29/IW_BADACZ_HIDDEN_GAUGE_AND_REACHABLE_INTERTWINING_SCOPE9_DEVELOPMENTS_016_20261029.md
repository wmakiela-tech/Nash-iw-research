---
artifact_id: IW_BADACZ_HIDDEN_GAUGE_AND_REACHABLE_INTERTWINING_SCOPE9_DEVELOPMENTS_016_20261029
exposure: PUBLIC
claim_ceiling: DEVELOPMENTS_[▷]_ELEMENTARY / MATURE_HOSTS_KALMAN_ZAMES_LUMPABILITY_BISIMULATION / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_CLAIM
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-29
origin_cell: BADACZ (wątek Claude)
document_type: RESEARCH_NOTE
result_class: RESULT
task_id: BADACZ-SCOPE9-ANALYSIS-001 (publikacja za zgodą Moderatora z 29 X 00:25)
builds_on: notatki SCOPE9 TOPDOWN 001, 002, 005, 006, 007 (prywatne); pełna wersja z weryfikacją notatek SCOPE9 i propozycjami dla monografii LT: Nash-Priv research/badacz/2026-10-28/IW_BADACZ_SCOPE9_TOPDOWN_ANALYSIS_AND_DEVELOPMENTS_014_20261028.md (r2, commit 136c9de)
code: research/badacz/2026-10-29/code/hidden_gauge_reachable_intertwining_check.py (sha256 1a2b8919858f5d6bb614a1b8e43d599ab37cbb69e3e2f685d12dae43f1ad0efa)
output_sha256: a62b33940eb861e21aecb0ebfb17bb6ccc4cefe8a4a43067f62e3939439f4caa (hidden_gauge_reachable_intertwining_check.json)
---

# Ukryte cechowanie i splatanie na zbiorze osiągalnym: rozwinięcia propozycji SCOPE9

**Status:** `[▷]`. Dwa elementarne rozwinięcia propozycji komórki SCOPE9 (rodzina GPT), napisane
przez Claude'a. Publikuję je za zgodą Moderatora. Prywatna wersja 014 zawiera dodatkowo
weryfikację notatek SCOPE9 i propozycje dla monografii LT. Tutaj są tylko wyniki matematyczne i
ich kod. Nowości nie zgłaszam. Wymagają audytu spoza rodziny Claude.

## 0. Wynik w skrócie

- **A. Ukryte cechowanie.** Gdy część stanu `y` jest ukryta, podobieństwo `y → Ty` nie zmienia
  niczego obserwowalnego. Zmienia natomiast normy, wzrost przejściowy, dysypatywność i każde
  oszacowanie zbudowane z norm bloków.
  - Rodzina `A_K, B_K` z SCOPE9 TOPDOWN 007 to jedna orbita takiego podobieństwa.
  - Świadectwa pamięci i wierności muszą być niezmiennicze albo mieć cechowanie ustalone przez
    źródło.
  - Podaję niezmiennicze kryterium małego wzmocnienia `ℓk < 1`, ostre na rodzinie SCOPE9.
- **B. Splatanie na zbiorze osiągalnym (Twierdzenie W).** Redukcja jest dokładna dla wszystkich
  historii interwencji z danej klasy przygotowań wtedy i tylko wtedy, gdy splatanie zachodzi na
  przestrzeni osiągalnej `W`.
  - Obejmuje to słabą i silną łączalność oraz przykłady SCOPE9 002 i 005.
  - Rodziny zgodnych instrumentów nie są zamknięte na sumę.
  - Pierwszeństwo idei (wersja automatowa, iloraz bisymulacyjny) ma SCOPE9 TOPDOWN 001 FD01.

## 1. Rozwinięcie A: ukryte cechowanie i niezmiennicze świadectwa pamięci

**Ustawienie.** `ℒ = [[A, B], [C, D]]` na `X ⊕ Y`, gdzie `x` jest widoczne, a `y` ukryte. Dla
`T ∈ GL(Y)` niech `S_T = diag(I, T)`. Wtedy
`ℒ_T = S_T ℒ S_T⁻¹ = [[A, BT⁻¹], [TC, TDT⁻¹]]`, a przygotowanie `y₀ = Rx₀` przechodzi w `TR`.

**G1 (niezmienniki).** Od `T` nie zależą:
- odpowiedź widoczna `P e^{tℒ}(x₀, Rx₀)`;
- jądro pamięci `K(t) = B e^{tD} C`;
- transmitancja widoczna `A + B(s − D)⁻¹C` i parametry Markowa.

Dowód: `S_T` działa tożsamościowo na `X`. (To klasyczna teoria realizacji z dokładnością do
podobieństwa.)

**G2 (wielkości nieniezmiennicze).** Każdą z nich można na orbicie uczynić dowolnie dużą lub małą
bez zmiany czegokolwiek obserwowalnego:
- `‖B‖`, `‖C‖`, `‖ℒ‖`, `‖ℒ − ℒ′‖`;
- `sup_t ‖e^{tℒ}‖` i `‖(z − ℒ)⁻¹‖` na całej przestrzeni;
- dysypatywność w ustalonym iloczynie skalarnym;
- oszacowania splotowe z rozdzieloną normą dla celu `q(t) = G(x(t) − x_M(t))`, gdzie
  `x_M = e^{tA}x₀` i `y(0) = 0`: z wzoru Duhamela
  `‖q(t)‖ ≤ ∫ ‖M(t − s)‖ ‖C e^{sA}x₀‖ ds` z `M(u) = G P e^{uℒ}|_Y`, gdy `dim Y ≥ 2`;
- stałe typu Gronwalla `‖ℒ‖ e^{T‖ℒ‖}`.

**G3 (rodzina SCOPE9 TOPDOWN 007 to jedna orbita).** `A_K = S A₁ S⁻¹` i `B_K = S B₁ S⁻¹` przy
`S = diag(1, 1/K)`, `c = 0.81`; sprawdzone dokładnie.

| `K` | błąd celu `t = 3` | `K(1)` | `‖B_K − A_K‖` | `‖ℒ‖` | max `‖e^{tA_K}‖` | max wartość własna `sym(A_K)` |
|---|---|---|---|---|---|---|
| 1 | `0.32229502` | `0.29798` | `0.81` | `1.91` | `1.00` | `−0.5` |
| 10 | `0.32229502` | `0.29798` | `0.081` | `10.1` | `3.72` | `4` |
| 100 | `0.32229502` | `0.29798` | `0.0081` | `100.0` | `36.8` | `49` |
| 1000 | `0.32229502` | `0.29798` | `0.00081` | `1000.0` | `367.9` | `499` |

- Niezależność odpowiedzi od `K` (SCOPE9 FD33–34) to niezmienniczość.
- W cechowaniu `K = 1` nie ma paradoksu: defekt generatora `0.81` jest duży, a błąd celu `0.32`
  mu odpowiada. Do tego `A₁` jest dysypatywna i nie ma wzrostu przejściowego.
- Znikające `‖B_K − A_K‖` i wzrost przejściowy mierzą wybór jednostki ukrytej współrzędnej, nie
  fizykę pamięci.
- W języku niezmienniczym odległość od progu stabilności to `1 − c = 0.19`, a nie `1/K`.

Stała Gronwalla na tej orbicie przy `T = 3`: `log₁₀(‖ℒ‖e^{3‖ℒ‖}) = 2.8 / 14.2 / 132`
dla `K = 1 / 10 / 100`, przy tej samej obserwowalnej rzeczywistości.

Oszacowanie splotowe z rozdzieloną normą (G2):
- na 60 losowych układach z losowym ukrytym `T` ten sam lewy bok miał prawą stronę
  zmieniającą się do `105×` (mediana `3.9×`);
- postać niezmiennicza `∫ ‖M(t − s) C e^{sA}x₀‖ ds` (nierówność trójkąta przed rozdzieleniem
  normy) nigdy nie jest gorsza i była w medianie `1.8×` ostrzejsza;
- odpowiedź widoczna i jądro pamięci były niezmiennicze z dokładnością `4e-11`.

**G4 (niezmiennicze kryterium małego wzmocnienia `[▷]`; gospodarz Zames 1966).** Oznaczam
`ℓ = ∫₀^∞ ‖e^{tA}‖ dt` oraz `k = ∫₀^∞ ‖B e^{tD} C‖ dt` (normy operatorowe na `X`; obie
wielkości są niezmiennicze). Przy `y(0) = 0` i `x_M = e^{tA}x₀`, jeśli `ℓk < 1`, to

  `‖x‖_{L¹} ≤ ℓ‖x₀‖/(1 − ℓk)`,   `‖x − x_M‖_{L¹} ≤ ℓ²k‖x₀‖/(1 − ℓk)`.

*Dowód.*
- `x = e^{·A}x₀ + e^{·A} * (K * x)`.
- Nierówność Younga na obcięciach `[0, T]` daje `‖x‖_{L¹(0,T)} ≤ ℓ‖x₀‖ + ℓk‖x‖_{L¹(0,T)}`; lewa
  strona jest skończona, bo `x` jest ciągłe.
- Teza zachodzi jednostajnie w `T`. Drugą nierówność dostajemy z `x − x_M = e^{·A} * (K * x)`. ∎

Przy przygotowaniu `y₀ = Rx₀` dochodzi wymuszenie `B e^{tD} R x₀`, które też jest niezmiennicze.

*Ostrość.*
- Na rodzinie SCOPE9 `ℓ = 1`, `k = c`, więc `‖x − x_M‖_{L¹} = c/(1 − c) = 4.2631578947` dokładnie.
  To różnica wzmocnień DC z SCOPE9 FD35.
- Pełny układ traci stabilność dokładnie przy `ℓk = c = 1`: odcięta widma to `−1 + √c`.
- Na 151 losowych układach z `ℓk < 0.95` nie było naruszeń. Maksymalny stosunek błędu do
  ograniczenia to `1 + 1.1e-11` (ograniczenie bywa osiągane; reszta to błąd kwadratury),
  mediana `0.62`.

**Propozycja dla bram SCOPE9 („Brama 0”).** Przed bramami wierności ustalić cechowanie ukryte
(normę na `Y` ze źródła) albo używać wyłącznie niezmienników: `K(t)`, transmitancji, wartości
Hankela, `ℓ` i `k`. Pseudospektrum ma sens fizyczny dopiero przy ustalonym cechowaniu albo dla
zaburzeń zdefiniowanych niezmienniczo, na przykład zaburzeń jądra.

## 2. Rozwinięcie B: splatanie na zbiorze osiągalnym

**Ustawienie.**
- `𝒳` to przestrzeń liniowa: wektory stanu, miary ze znakiem albo operatory.
- `{Φ_a}` to liniowe operacje dopuszczalne: odcinki ewolucji i nieunormowane gałęzie instrumentów.
- `𝒫 ⊂ 𝒳` to przygotowania, `r: 𝒳 → 𝒴` liniowa redukcja, `{φ_a}` operacje zredukowane.
- `W` to najmniejsza podprzestrzeń zawierająca `𝒫` i niezmiennicza względem wszystkich `Φ_a`.

**Twierdzenie W `[▷]`.**
- (i) `r Φ_{a_m}⋯Φ_{a_1} p = φ_{a_m}⋯φ_{a_1} r p` dla każdego `p ∈ 𝒫`, każdego `m` i każdej
  historii ⇔ `r Φ_a w = φ_a r w` dla każdego `w ∈ W` i każdego `a`.
- (ii) Takie `φ_a` istnieją ⇔ `Φ_a(W ∩ ker r) ⊂ ker r` dla każdego `a`; są wtedy jednoznaczne na
  `r(W)`.
- (iii) Dwa modele ze wspólnym `𝒫` i z odczytem tomograficznie pełnym dają te same statystyki
  wszystkich historii ⇔ ich operacje zgadzają się na `W`.

*Dowód (i).*
- ⇐: indukcja po długości historii, bo `Φ_h p ∈ W`.
- ⇒: dla `w = Φ_h p` porównujemy historię `(h, a)` z historią `h`, po czym stosujemy `φ_a` do
  obu stron. Warunek jest liniowy w `w`, więc przechodzi na `span = W`.
- (ii) i (iii) analogicznie. Strategie adaptacyjne obsługujemy po gałęziach. ∎

**Precedens.** SCOPE9 TOPDOWN 001 FD01 ma wersję skończoną, automatową.
- Minimalny iloraz względny wobec zbioru interwencji to najmniejsza kongruencja akcji
  (bisymulacja), z gospodarzem Larsen–Skou 1991.
- Konstruktywna definicja mostu `F_(I,T)(R, K)` mówi, że zawężenie zbioru interwencji nie może
  zwiększyć supremum.
- Twierdzenie W to liniowy odpowiednik FD01 z warunkiem koniecznym. Pierwszeństwo idei ma SCOPE9.

**Wnioski.**
- **W1 (warunek globalny a warunek na `W`).** Splatanie dla każdego pełnego stanu, czyli warunek
  typu Li–Rabitz, wystarcza. Konieczne i wystarczające jest splatanie na `W`.
  - Przykład (kod DB1): `dim W = 4` w `𝒳 = ℝ⁶`.
  - Splatanie na `W` jest dokładne (`0`), splatanie globalne jest naruszone o
    `3.04`, a wszystkie historie do długości 6 są dokładne (`8.9e-16`).
  - Jeden instrument wyprowadzający poza `W` zwiększa `dim W` do `6` i daje błąd
    `0.43`.
- **W2 (słaba i silna łączalność).**
  - Silna łączalność odpowiada `𝒫` złożonemu ze wszystkich mikrostanów, czyli `W = 𝒳`. To SCOPE9
    002 FD04.
  - Słaba łączalność to klasa przygotowań. Łańcuch z DB2 nie jest silnie łączny, a jednak od
    przygotowań z `W` (`dim 2`) prawo ścieżek makro zgadza się dokładnie (`TV ≈ 1e-16` przy
    `n = 4`). Od `(0, 1, 0)` daje `TV = 0.2`.
- **W3 (osłabienie hipotezy SCOPE9 002 FD06).**
  - Wystarcza, by jednokrokowy defekt był jednostajny po osiągalnych przekonaniach (rozkładach
    ukrytych przy danej historii widocznej), a nie po wszystkich mikrostanach.
  - W DB2 defekt mikrostanowy na włóknie to `0.2`, a ograniczenie FD06 to `1 − 0.8⁴ = 0.59`.
  - Defekt na osiągalnych przekonaniach wynosi `0`, co daje dokładność tam, gdzie FD06 nic nie
    mówi.
- **W4 (SCOPE9 005 w języku `W`).**
  - Dla kanału defazującego `D₀` mamy `W_passive = range D₀ = span{I, Z}` i tam `V_A = V_B`.
  - Interwencja Hadamarda daje `W ⊇ span{I, X}`, gdzie `V_A ≠ V_B`.
  - Uwarunkowanie identyfikacji przy `ε > 0` wynosi `1/ε`.
- **W5 (rodziny instrumentów nie są zamknięte na sumę).**
  - Rodziny zgodne z daną redukcją są zamknięte na podrodziny, bo `W` maleje.
  - Na sumę zamknięte nie są. Dokładny przykład: `r(x, y) = x`, przygotowanie `y = 0`,
    `I₁(x, y) = (x, y + x)`, `I₂(x, y) = (x + y, y)`. Każdy z nich osobno jest zgodny. Historia
    `I₁`, potem `I₂`, daje `r = 2x`, a model zredukowany daje `x`.
  - Wynika to też z FD01, bo dodanie akcji rozdrabnia najgrubszą kongruencję. Wkładem jest tylko
    jawny liniowy świadek.
  - Wniosek: nie ma jednej maksymalnej dopuszczalnej rodziny instrumentów dla danej redukcji.
    Pytanie o „minimalną legalną rodzinę” trzeba stawiać względem rodziny zadanej przez źródło.

## 3. Uwaga C: SCOPE9 TOPDOWN 006 w tym samym języku

Włókno FD31 `(θ, b₀, d) ~ (θ′, b₀ + θ² − θ′², d − 2θ + 2θ′)` to orbita grupy przekształceń
parametrów zachowującej prawo danych. Klasa równoważności obserwacyjnej jest orbitą, tak jak w §1.
Świadectwo identyfikowalności musi być niezmiennikiem orbity, a niezależna referencja kalibracji
działa jak ustalenie cechowania. To porównanie strukturalne, nie fizyczne.

## 4. Gospodarze, odtworzenie, ograniczenia

**Gospodarze.**
- Teoria realizacji z dokładnością do podobieństwa; przestrzenie osiągalne (Kalman).
- G. Zames, *IEEE Trans. Automat. Control* 11(2):228–238 (1966), twierdzenie o małym wzmocnieniu.
- Łączalność: Kemeny–Snell (silna); Rubino–Sericola 1989 (słaba).
- Li–Rabitz 1989: dokładne skupianie, warunek globalny.
- Bisymulacja: Larsen–Skou 1991, za SCOPE9 TOPDOWN 001; samego artykułu nie otwierałem.

**Odtworzenie.**

```text
pip install numpy==2.1.3 scipy==1.14.1
python3 -I research/badacz/2026-10-29/code/hidden_gauge_reachable_intertwining_check.py --out <katalog>
```

Około 5 minut. Wszystkie pola `verdict` mają wartość `true`. Dwa czyste uruchomienia dały
identyczny JSON.

- Kod publiczny ma osobne strumienie losowe dla części A i B. Statystyki z prób losowych różnią się
  więc od wersji prywatnej 014; wnioski są te same.
- Wszystkie przykłady są syntetyczne, bez fizyki NASH.

**Moje błędy po drodze** (w testach wersji prywatnej, naprawione przed zapisem):
1. Całka do `∞` z `cosh` dała `NaN`; zastąpiłem ją postacią stabilną.
2. Baza `W` z QR była błędna przy zerowych kolumnach; zastąpiłem ją SVD.
3. Pozorne naruszenia małego wzmocnienia wynikały z błędu kwadratury trapezów przy ograniczeniu
   osiąganym dokładnie; zastąpiłem ją wzorem Simpsona na gęstszej siatce.

## 5. Powrót w trzech warstwach

- **Wynik:** dwa rozwinięcia `[▷]` i uwaga strukturalna; pierwszeństwo idei z B przypisane SCOPE9.
- **Konfiguracja:** recenzja międzyrodzinowa była tu bardziej syntezą niż szukaniem błędów:
  wspólna struktura (orbita w 006 i 007, `W` w 002 i 005).
- **Uczenie systemu:**
  - reguła „świadectwo ma być niezmiennikiem relacji równoważności obserwacyjnej albo mieć
    cechowanie ustalone przez źródło” jest kandydatem na stałą bramę przeglądu (`[▷]`, decyzja
    Moderatora);
  - origin_failure_mode `OWN_SURFACE_PRIOR_ART_CHECKED_AFTER_WRITING` (TOPDOWN 001 znaleziony po
    pierwszej wersji); łatka: czytam całą serię źródłową przed rozwijaniem.
