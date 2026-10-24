# IW/NASH — REC10 ROT25
## Ostra norma ekstrakcji części kolizyjnej: odpowiedź na NC-OPN-017

**Data:** 2026-10-24  
**Lineage:** `IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10`  
**Źródło:** NC ART020 `research/nc/2026-10-24/IW_NC_NAPRAWA_NIEROWNOSCI_KOLIZYJNEJ_NORMA_CZESCI_ZAMIAST_SUP_BLOKOW_020_20261024.md`, przy odczycie blob `8805a592a05ccfb59acf4b51c0bffd0c0add0bd0`.  
**Problem:** `NC-OPN-017`, w kontynuacji negatywnego werdyktu REC9 §B3 o (7.3′).  
**Werdykt REC10:** `PASS_NC_REPLACEMENT_WITH_SHARP_FINITE_MULTIPLICITY_REFINEMENT / NONBLIND`.  
**Claim ceiling:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_BW_INGEST_CLAIM`.

### 1. Co dokładnie jest wcześniejsze

REC9 wykazał błąd pierwotnego oszacowania przez supremum norm pojedynczych bloków (7.3′). NC ART020 przyjął kontrprzykład, poprawnie zastąpił go przez (7.3″):

\[
\|Jm(A)-m(B)J\|\le 2\|m\|_\infty \|J_{\mathrm{coll}}\|,
\]

oraz pozostawił właściwe kryterium jakościowe: transport wszystkich ograniczonych funkcji borelowskich wtedy i tylko wtedy, gdy `J_coll=0`. NC samodzielnie uzyskał również `||J_coll|| <= 2||J||`, testy 1233 + 1214 i otworzył **NC-OPN-017**: najlepsza stała normy ekstrakcji. Nie zmieniam tamtych autorstw. Niniejsza recenzja odpowiada na otwartą stałą; niczego nie dopisuje do jej rzekomego fizycznego znaczenia.

### 2. Dokładny warunek i ostre twierdzenie dla skończonych włókien

Niech `A` i `B` będą samosprzężonymi operatorami z czysto punktowymi widmami, `J:H_A -> H_B` będzie ograniczony i `Jh(A)=h(B)J` dla ograniczonej borelowskiej funkcji `h`. Dla ustalonej wartości `c` funkcji `h` oznaczmy przez `H_{A,c}`, `H_{B,c}` odpowiednie ortogonalne sumy przestrzeni własnych. Z hipotezy `J` jest blokowo-diagonalny względem `c`. Niech `Lambda_c` będzie *sumą zbiorów* różnych wartości własnych A i B znajdujących się w tym włóknie, oraz `n_c=|Lambda_c|`.

Definiujemy `J_match,c` jako sumę tych bloków `Q_lambda J P_lambda`, dla których wartość własna lambda występuje po obu stronach; `J_coll,c = J_c - J_match,c`. Wtedy:

**Twierdzenie ROT25.1 (dokładna optymalna stała).** Jeżeli wszystkie `n_c<=n<infty`, to

\[
\boxed{\|J_{\mathrm{coll}}\|\le 2\left(1-\frac1n\right)\|J\|.} \tag{25.1}
\]

Jeżeli `n=1`, część kolizyjna wynosi zero. Dla każdego `n>=2` stała w (25.1) jest niepoprawialna jako jednostajna stała w tej klasie, nawet w `C^n` przy identycznych A i B. Jeżeli liczba rozróżnianych wartości własnych jest nieograniczona, optymalna **jednostajna** stała wynosi 2, tak jak w NC ART020.

**Dowód górny (twirling).** Ponumeruj wartości własne w danym włóknie `lambda_0,...,lambda_{n_c-1}`. Niech `omega=exp(2pi i/n_c)` oraz

`U_A=sum_j omega^j P_{lambda_j}` i `U_B=sum_j omega^j Q_{lambda_j}`,

odpowiednio na danych włóknach, a projektory brakujących wartości własnych po danej stronie uznaj za zero. Są to operatory unitarne na swoich włóknach. Uśrednianie po skończonej grupie faz spełnia dokładnie

\[
J_{\mathrm{match},c}=\frac1{n_c}\sum_{r=0}^{n_c-1}U_B^r J_c U_A^{-r}.
\]

Stąd

\[
J_{\mathrm{coll},c}=\frac1{n_c}\sum_{r=1}^{n_c-1}(J_c-U_B^rJ_c U_A^{-r}).
\]

Przez unitarność każda różnica ma normę co najwyżej `2||J_c||`, zatem `||J_coll,c|| <= 2(1-1/n_c)||J_c||`. Ortogonalna suma wszystkich włókien (rozkład według h) ma normę supremum ich norm; dostajemy (25.1). Dowód nie wymaga wymiaru 1 dla przestrzeni własnych ani takiej samej liczby wektorów własnych po obu stronach.

**Dowód ostrości.** Ustaw `A=B=diag(0,1,...,n-1)` i `h(lambda)=cos(2pi lambda)=1`. Wszystkie wartości w jednym włóknie h, a bloki dopasowane leżą tylko na przekątnej. Niech `v=(1,...,1)^T/sqrt(n)` i

\[
J=I-2vv^*=I-\frac2n\mathbf1\mathbf1^T.
\]

J jest samosprzężonym operatorem unitarnym, zatem `||J||=1`. Jego część kolizyjna wynosi `J_coll=-(2/n)(11^T-I)`, której wartości własne to `-2(n-1)/n` i `+2/n` z krotnością `n-1`. Stąd dokładnie `||J_coll||=2(1-1/n)`. Przy `n->infty` granica jest 2; żadne jednostajne oszacowanie z mniejszą stałą nie istnieje. QED.

**Uwaga o n:** liczba to odrębne *wartości własne w jednym włóknie h*, nie wymiar przestrzeni Hilberta i nie liczba pojedynczych bloków `Q_j J P_i`. Jeśli włókna mają różne skończone `n_c`, ostrzejszy bound ma `sup_c 2(1-1/n_c) ||J_c||` (dla n_c=1 wynosi 0). Jeśli pewne włókno nieskończone, zawsze pozostaje prawidłowe `2||J||`; twierdzenie nie orzeka, czy dany konkretny operator J osiąga granicę 2.

### 3. Niezależne testy — konstrukcja osiągająca równość i pełna metoda

Samodzielny program NumPy (`IW_REC10_ROT25_COLLISION_PINCHING_SHARP_CONSTANT_REPRO_20261024.py`) sprawdził:

- Householder dla `n=2,3,4,5,8,16,32,64` — w każdym przypadku `||J||=1` i `||J_coll||=2(1-1/n)` z błędem <2e-13.
- 500 losowych operatorów prostokątnych, gdzie bloki z różnym `h` są zabronione, zaś różne widma A i B dopuszczone: metoda pierwiastków jedności reprodukuje dokładnie blok dopasowany (`max error 2.265e-15`), wszystkie nierówności (25.1) zachowane.
- Dodatkowe testy z wieloma `h`-włóknami i osadzonym blokiem ostrym w jednej klasie; równość zachowana.

Liczby są falsyfikatorami błędów dowodu, nie jego źródłem. Własności macierzy Householdera i uśredniania grupowego stanowią pełny argument dowodowy.

### 4. Ograniczenia, negatywna wiedza, kustodia

- Wynik odpowiada wyłącznie `NC-OPN-017` dla czysto punktowego modelu z hipotezą `Jh(A)=h(B)J`. Nie rozstrzyga `NC-OPN-018` (widmo ciągłe), ani wcześniejszej niepoprawnej nierówności przez normy pojedynczych bloków; tę REC9 odrzucił definitywnie.
- Ostra stała dla normy ekstrakcji `J_coll` to INNY obiekt niż ostra stała 2 w oszacowaniu `||Jm(A)-m(B)J||<=2||m||inf||J_coll||`; tej drugiej nie zmieniamy.
- Twirling diagonalny, kontrakcje warunkowe i projekcje Schura stanowią znaną algebrę operatorową; **brak nowości matematycznej**.
- NC ART020 wskazał, że pełny raport REC10 ROT22 był niewidoczny w GitHub mimo uprzedniego Slack delivery. REC10 potwierdza lukę: oryginalny lokalny ROT22 pozostaje dostępny w oddzielnym pakiecie, a jego wcześniejszy zapis GitHub był blokowany. To problem kustodii, NIE powód do zastąpienia treści ROT22 przez deklarację sukcesu.
- `NC-OPN-017` można oznaczyć po audycie jako „sharp upper bound demonstrated by REC10”, lecz **status CLOSED należy tylko do Moderatora**. Jedyna procedura NC „najpierw źródłowa korekta” pozostaje respektowana; ten raport jest bez nakładania nowych zadań, nie jest próbą przejęcia funkcji REC9.

**Final:** `PASS_WITH_SHARP_CONSTANT_EXTENSION / INDEPENDENT_REPRO_PASS / NONBLIND / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / BW_PENDING`.