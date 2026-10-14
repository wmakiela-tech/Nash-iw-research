# MT13 — Obrót książkowy: identyczne kanały w dwóch chwilach, nierównoważne procesy

**Data:** 2026-10-14
**Funkcja:** MT13 / programme scientific integration, book-first.
**RETURN_ID:** MT13-BOOK-ROT22-CH5-INTERVENTION-COMPLETE-TWO-ENDPOINT-NONIDENTIFIABILITY-001_20261014
**Klasa:** exact finite-dimensional textbook counterexample / manuscript-local addition / NO_NOVELTY / NO_CANON / NO_EXEC.

## Stan źródłowy i modyfikacja
Aktualny rękopis LT4: https://docs.google.com/document/d/1cn97_kO65BcJRRWQrvrL9fKlEYBT3PHg6BJItn1Q4FQ/edit . Aktualnie zawiera rozdziały I–VI, w tym rozdział V „Kanały kwantowe, pamięć i struktura procesów wieloczasowych”. Istniejący §5.5 dawał przykład zgodności jednego kroku, z rozróżnialnością przy kolejnym kroku. Dodano do dokumentu za nim i przed §5.6 **§5.5a „Identyczne kanały w obu chwilach nie wyznaczają procesu”** (~2704 znaki); wykonano zapis na podstawie aktualnej rewizji i zweryfikowano odczyt natywnego Google Docs. Zachowano oryginalne twierdzenia i ich numerację oraz istniejący rozdział VI. Fragment nie jest nowym prawem; wynika ze znanej teorii procesów wieloczasowych / process tensors.

## Dokładna konstrukcja i dowód
Weź dwa kubity S,E; środowisko początkowo w `sigma_E=I/2`. Pierwszy unitarny etap w obu modelach to `U_0=SWAP`, dlatego dla każdego stanu `rho`:
`U_0 (rho tensor I/2) U_0^† = (I/2) tensor rho`.

Drugi etap:
- model A: `U_1^A=I_SE`;
- model B: `U_1^B=I_S tensor |0><0|_E + Z_S tensor |1><1|_E` (kontrolowane Z, kontrola w E).

Przy braku interwencji pośredniej `Tr_E((I/2) tensor rho)=I/2`, a nawet po kontrolowanym Z:
`Tr_E[U_1^B ((I/2) tensor rho) U_1^{B†}]=rho_00 I/2+rho_11 Z(I/2)Z=I/2`.
Zatem **dla KAŻDEGO rho oba pełne kanały od czasu 0 do czasu 1 i od czasu 0 do czasu 2 są identyczne**: `Phi_1^A=Phi_1^B=Phi_2^A=Phi_2^B:rho→I/2`. Różnica jest niewidoczna nawet dla tomografii obu kanałów bez interwencji.

Przygotuj pomiędzy etapami system w `|+>=(|0>+|1>)/sqrt(2)` za pomocą legalnego CPTP resetu `R(X)=Tr(X)|+><+|` (bez resetu E). Po SWAP E przechowuje `rho`, więc po resecie wspólny stan to `|+><+| tensor rho`. Ostatecznie:
- A: `rho_out^A=|+><+|`;
- B: `rho_out^B=rho_00 |+><+| + rho_11 |-><-|`, `|->=(|0>-|1>)/sqrt(2)`.
Dla `rho=|1><1|` wynik A jest `|+><+|`, wynik B to `|-><-|`. Końcowy pomiar X rozstrzyga model **z pewnością jeden w idealnym opisie**, a odległość TV rozkładów =1.

Stan E w A też przechowuje wejście, ale jest operacyjnie niedostępny przez tę przyszłą dynamikę. W B zawartość E staje się dostępna po odpowiednim resecie S. Jest to dokładny przykład różnicy między **mikroskopową obecnością informacji** a **operacyjną możliwością jej odzyskania**.

### Warunkowe uogólnienie ilościowe (poza tekstem monografii)
Jeśli model wykonuje drugi etap B z prawdopodobieństwem lambda∈[0,1] i A z prawdopodobieństwem (1−lambda), przy tych samych U0/sigma, wszystkie dwuchwilowe mapy bez interwencji nadal wynoszą depolaryzację. Dla ustalonego testu wejście |1>, pośredni reset |+>, końcowy pomiar X: `Pr(-)=lambda`. W tej *zamrożonej rodzinie* kontrastu parametr lambda jest identyfikowalny na podstawie prawa procesowego, chociaż całkowicie niewidoczny w kanałach jedno- i dwuetapowych bez interwencji. Nie jest to uniwersalny monotoniczny miernik niemarkowowskości.

## Kontrola algebraiczna/numerystyczna
Niezależne lokalne obliczenie macierzowe `SWAP`, kontrolowane `Z` i ślad częściowy na czterech wejściach (`|0>, |1>, |+>, (|0>+i|1>)/sqrt2`) dało:
- różnice no-intervention `Phi_1, Phi_2` względem `I/2` ≤ 1.2e−16;
- po resecie prawdopodobieństwo końcowego `+` w modelu B: odpowiednio 1,0,1/2,1/2.
Dokładny dowód jest elementarną algebrą macierzy i nie zależy od obliczenia.

## Ograniczenia i prior art
Pokazano identyczność *dwóch przygotowanych map krańcowych* w dyskretnej dynamice dwukrokowej, nie pełnej ciągłej rodziny `Phi_t`, a także nie równość procesów przy wszystkich interwencjach. Wszystkie użyte bramki, reset i pomiar są legalne w skończonych wymiarach. Przywoływana dojrzała teoria quantum combs / process tensor: Chiribella, D'Ariano, Perinotti, PRA 80 022339 (2009), DOI 10.1103/PhysRevA.80.022339; Pollock et al., PRL 120 040405 (2018), DOI 10.1103/PhysRevLett.120.040405. Nowość matematyczna/empiryczna NASH: brak.

## Currentness/owners
LT4 prowadzi monografię. SW i INT7 dostarczyły już odrębne recenzje Ch3/4 z poprawkami dziedzinowymi; nie powielano ich ani nie uznano za zaimplementowane przez LT4. Nowy Ch6 „Redukcja kinetyczna i dokładność obserwabli końcowej” jest widoczny i został zachowany. Niedokonywano innych zmian. Posterior acceptance/canon/EXEC należy do właściwych ownerów i Moderatora.

**Return to:** LT4, INT7, SW, SCOPE8, Moderator. No new tasks issued.
