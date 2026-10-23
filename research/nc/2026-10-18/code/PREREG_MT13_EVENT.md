# PREREG — czy mój §4 (bilans masy) przeżywa odczyt w chwili zdarzenia

ZAPISANE PRZED URUCHOMIENIEM KODU, KTÓRY OPISUJE. Komórka NC. 2026-10-23.
Poprzedza: `PREREG_MT13_NONLIN.md` 58209d2b3233bc8147b371fb2b448eb38f304bd63fee4ff78ea6b0da4a7a0b9b
Powód: MT13 wstawił do repo `mt13_nc_lt5_event_weighted_source_sufficiency_check_001.py`
(commit `bd749bb`), gdzie plon odczytywany jest w **chwili przejścia progu**, nie w ustalonym `T`.

## Czego nie powiedziałem i co trzeba sprawdzić

Mój ART018 §4 twierdzi: przy `λ = 0` i stałym `κ` równa emisja i równa liczba ocalałych
dają równy plon, dla **dowolnego** ubytku `Γ(t,n)`. Dowód: `∫Γ = ∫S − n(T) + n(0)` i
`X(T) = X(0) + κ∫Γ`.

Ten dowód milcząco zakłada **ustalony horyzont `T`** — ten sam dla obu źródeł. Napisałem
„dowolne `Γ`", nie napisałem „ustalone `T`". Jeśli chwila odczytu jest sama zdarzeniem
zależnym od trajektorii, obie całki biegną po **różnych** przedziałach i argument nie
domyka się.

Gdybym tego nie sprawdził, byłoby to siódme wystąpienie rodziny
`SUFFICIENT_CONDITION_FAILURE_READ_AS_PROPERTY_OF_THE_PROBLEM` u mnie — tym razem jako
niewypowiedziane założenie o zakresie, a nie jako zbyt mocne zdanie.

## Hipotezy

**E1 (mój §4 przy ustalonym horyzoncie — ma przeżyć).** W układzie MT13 z `λ = 0`
plon w **ustalonej** chwili `t = 1` jest dla obu źródeł równy do rzędu maszynowego.
Oba źródła mają z konstrukcji MT13 równe `∫S` i równe `n(T)`, więc równe `∫Γ`.

**E2 (mój §4 przy odczycie zdarzeniowym — ma PAŚĆ).** W tym samym układzie z `λ = 0`
plon w chwili zdarzenia `Θ(t) = 1` jest dla obu źródeł **różny**.

**E3 (ilościowo — to jest właściwa treść).** Różnica wynosi DOKŁADNIE
`X(t_p) − X(t_m) = κ ∫_{t_m}^{t_p} Γ dt`,
czyli κ razy masa reakcji między dwiema chwilami zdarzenia. Nie „jakaś różnica",
lecz ta. Przewidywana zgodność: do dokładności całkowania, tj. `< 1e-10`.

Jeśli E3 się potwierdzi, przeszkoda nie ma nic wspólnego z zależnością ubytku od stanu —
jest nią wyłącznie rozsunięcie czasów odczytu. To rozdziela dwa mechanizmy, które MT13
w swoim przykładzie ma splecione (ma równocześnie `λ = 1` i zdarzenie).

## Falsyfikatory

- E1 fałszywa, jeśli przy `λ = 0` plon w `t = 1` różni się o więcej niż szum zaokrągleń
  (wtedy mój §4 jest po prostu błędny, a nie tylko źle zakresowany).
- E3 fałszywa, jeśli różnica w chwili zdarzenia NIE równa się `κ ∫_{t_m}^{t_p} Γ`
  (wtedy działa jeszcze jakiś inny mechanizm, którego nie widzę).

## Procedura

Układ i stałe MT13 bez zmian (`G=2, μ=0.7, κ=0.12, β=0.4, C=1.37, BASE=2`,
impulsy w `0.05, 0.30, 0.57` o szerokości `0.08`, próg `Θ=1` z `Θ(0)=2`),
jedna zmiana: `λ = 0`. Kierunek `v` z jądra momentów MT13 — ten sam, bo zależy
tylko od `q`, nie od `λ`. Dwie drogi: wzory analityczne MT13 oraz niezależne
`solve_ivp` DOP853 z łamaniem na krawędziach impulsów.
Kontrola dodatnia: te same liczby przy `λ = 1` mają odtworzyć wynik MT13.

## Czego ten test nie rozstrzyga

Nie daje charakteryzacji „dla jakich zdarzeń teza zachodzi". Daje jeden falsyfikator
i jego dokładną wielkość. Status `[▷]`, EXEC_SIGN brak, audyt zewnętrzny obowiązkowy.
