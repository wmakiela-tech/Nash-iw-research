# Proposed book insertion — Section 71A

RETURN_ID: INT7-BOOK-PATCH-071A-MINIMAL-REALIZATION-AND-SHARED-COMPONENT-001
DATE: 2026-10-13
TARGET_BOOK: Living Theory working book, after section 71 and before section 72
BW_STATUS: PENDING_INGEST
CLASS: BOOK_INTEGRATION / READY-TO-PASTE SCIENTIFIC TEXT
STATUS: NO NOVELTY CLAIM / MATURE REALIZATION THEORY + CLAIM-RELATIVE LEGALITY

## 71A. MINIMALNA REALIZACJA NIE USTANAWIA WSPÓLNEJ ZMIENNEJ FIZYCZNEJ

Równość funkcji przenoszenia jest silnym twierdzeniem o odpowiedzi wejście–wyjście, lecz nie ustala automatycznie tożsamości zmiennych wewnętrznych. Dla skończenie wymiarowych minimalnych realizacji tej samej funkcji

\[
\Sigma(z)=B_1(zI-D_1)^{-1}C_1
        =B_2(zI-D_2)^{-1}C_2
\]

klasyczna teoria realizacji daje odwracalną transformację podobieństwa \(T:Y_1\to Y_2\), dla której

\[
D_2T=TD_1,\qquad C_2=TC_1,\qquad B_2T=B_1.
\]

Oznacza to równoważność realizacji względem zadanej odpowiedzi. Nie oznacza jednak, że surowe współrzędne stanów w \(Y_1\) i \(Y_2\) są tymi samymi wielkościami fizycznymi.

Niech

\[
s_i:Y_i\to Z
\]

będzie mapą wybierającą tę składową wewnętrzną, którą w obu opisach chcemy interpretować jako wspólną wielkość. Wtedy podobieństwo realizacji przenosi tę składową poprawnie dokładnie wtedy, gdy

\[
\boxed{s_2T=s_1}
\tag{71A.1}
\]

na podprzestrzeni stanów istotnej dla rozpatrywanego problemu.

Rzeczywiście, stanowi \(y\in Y_1\) odpowiada w drugiej realizacji stan \(Ty\). Obie reprezentacje przypisują mu tę samą deklarowaną składową wtedy i tylko wtedy, gdy

\[
s_1(y)=s_2(Ty).
\]

Warunek (71A.1) jest więc zwykłym warunkiem zgodności mapy obserwowanej składowej z transformacją podobieństwa.

### Przykład

Weźmy skalarne realizacje

\[
D_1=D_2=-1,\qquad C_1=1,\qquad B_1=1.
\]

Dla transformacji \(T=2\) równoważna minimalna realizacja ma

\[
C_2=2,\qquad B_2=\frac12.
\]

Obie realizują tę samą funkcję

\[
\Sigma(z)=\frac{1}{z+1}.
\]

Jeżeli jednak w obu opisach nazwiemy „wspólną zmienną” po prostu współrzędną stanu,

\[
s_1(y)=y,\qquad s_2(y)=y,
\]

to

\[
s_2(Ty)=2y\neq y=s_1(y)
\]

dla \(y\neq0\). Identyczna odpowiedź wejście–wyjście i minimalność nie czynią więc z surowej współrzędnej stanu jednej wspólnej wielkości.

Jeśli natomiast druga mapa składowej zostanie zdefiniowana zgodnie z podobieństwem,

\[
s_2(y)=\frac{y}{2},
\]

to

\[
s_2(Ty)=s_1(y),
\]

i wspólna składowa jest dobrze określona.

### Związek z legalnym łączeniem modeli

Jeżeli dwa konteksty mają lokalne przestrzenie stanów \(Y_1,Y_2\), a deklarowaną wspólną składową opisują mapy \(s_1,s_2\), to zgodne pary stanów tworzą iloczyn włóknisty

\[
P_Z=\{(y_1,y_2):s_1(y_1)=s_2(y_2)\}.
\]

Podobieństwo \(T\) wyznacza graf

\[
G_T=\{(y,Ty):y\in Y_1\}.
\]

Wspólna składowa jest zachowana wzdłuż równoważności realizacji dokładnie wtedy, gdy

\[
G_T\subseteq P_Z,
\]

czyli ponownie wtedy, gdy \(s_2T=s_1\).

Nawet ten warunek nie ustanawia jednego identycznego pełnego nośnika. Podobieństwo jest izomorfizmem dwóch realizacji, a nie literalną identycznością ich stanów. Dlatego trzeba odróżnić trzy poziomy:

\[
\text{ta sama odpowiedź wejście–wyjście}
\;\not\Rightarrow\;
\text{ta sama składowa wewnętrzna}
\;\not\Rightarrow\;
\text{ten sam pełny stan fizyczny}.
\]

Możliwa jest również sytuacja, w której składowa wewnętrzna nie jest wspólna, lecz zachowany jest tylko konkretny cel. Dla map celu \(\tau_i:Y_i\to Q\) wystarczy wtedy

\[
\tau_2T=\tau_1.
\]

Jest to słabszy wymóg niż wspólność całej składowej \(s_i\).

### Wniosek

Minimalna realizacja jest unikalna z dokładnością do podobieństwa w sensie zadanej odpowiedzi. Nie wynika z tego unikalność ani ontologiczna tożsamość zmiennych wewnętrznych. Każde twierdzenie, że dwa modele „mają tę samą ukrytą zmienną”, wymaga dodatkowej mapy identyfikującej tę składową i sprawdzenia jej zgodności z podobieństwem.

\[
\boxed{\text{unikalność do podobieństwa}\neq\text{unikalność zmiennej fizycznej}}
\]

To rozróżnienie pozwala korzystać z teorii realizacji bez nadawania jej silniejszej interpretacji niż ta, którą rzeczywiście dowodzi.
