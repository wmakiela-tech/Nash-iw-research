# IW/NASH — REC10 ROT13
## Dokładna globalna granica przybliżenia nie-CP resetu przez instrument o zadanym POVM

**Data:** 23 października 2026  
**Komórka:** `IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10`  
**Artifact ID:** `IW_REC10_ROT13_ALL_INSTRUMENT_POVM_COMPATIBLE_DIAMOND_REPAIR_EXACT_GATE_001_20261023`  
**Problem ID:** `P2-LT5-G2-TARGET-RELATIVE-QUANTUM-BRIDGE-002`  
**Werdykt:** `PASS_WITH_EXACT_SHARPENING`  
**Publikowalność:** publiczna recenzja matematyczna, bez danych prywatnych  
**Ograniczenia:** `NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_NEW_TASK`  
**BW:** `GITHUB_PENDING_BW_INGEST` — nie jest to zdarzenie BW.

### 1. Źródła i aktualność

Przeczytano: `research/geeky-s10/2026-10-23/geeky_s10_qubit_channel_observable_compatibility_frontier_001.md`, odczytany blob `423f3ee74bcf66d6922b0ea0ca56512cfad63e57`, oraz kod `reproduce_geeky_s10_qubit_channel_observable_compatibility_frontier_001.py`, blob `82b9e93de4e38d7228b1a556c08ce6ce1ffc48d6`. Kontekst: LT5 obrót 6 (nie-CP Bloch, optymalna odległość do CPTP `s/2`); Geeky-S10 wcześniejszy test Lüdersa; INT8 ROT009 legalne ograniczone instrumenty.

**PASS** dla źródłowego twierdzenia Geeky-S10: kanał Pauliego o macierzy Blocha `diag(a,t,t)` jest zgodny z binarnymi efektami `E_±=(I±μX)/2`, w deklarowanej klasie, wtedy i tylko wtedy gdy

\[
\mu\leq \frac{1-a}{2}+\frac12\sqrt{(1+a)^2-4t^2}.
\]

Dla `a=1−s`, `μ=s` najwyższe dopuszczalne `t` wynosi `√(1−s)`, osiągane przez jawne cztery operatory Krausa w raporcie źródłowym.

### 2. Nowe wzmocnienie: minimum wśród **wszystkich** instrumentów

Niech `Q_s` oznacza unitalną, zachowującą ślad mapę *liniową* na macierzach kubitu z macierzą Blocha `diag(1−s,1,1)`. Dla `s>0` nie jest ona CP. Niech `J_+`, `J_-` będą dowolnymi operacjami CP składającymi się na instrument o efektach **dokładnie**

\[
J_\pm^\dagger(I)=\frac{I\pm sX}{2},\qquad \Phi=J_++J_-\ \text{CPTP}.
\]

**Twierdzenie (R13.1).** Dla `0≤s≤1` zachodzi

\[
\boxed{\inf_{J_\pm}\lVert Q_s-(J_++J_-)\rVert_\diamond=1-\sqrt{1-s}.}
\]

Infimum jest osiągalne. W odróżnieniu od źródłowego wyniku nie zakładamy z góry, że `Φ` jest kanałem Pauliego, unitalnym lub poprzecznie izotropowym.

#### Dowód A — redukcja bez utraty ogólności przez symetryzację instrumentu

Rozważ skończoną grupę symetrii Blocha generowaną przez obrót o `π/2` wokół osi `x` oraz o `π` wokół osi `z`. Dla każdego odpowiadającego jej `U` istnieje `ξ_U∈{−1,+1}` z `UXU†=ξ_U X`. Przekształć **obie operacje**, nie tylko uśredniony kanał:

\[
J_y^{(U)}=\operatorname{Ad}_U\circ J_{\xi_U y}\circ\operatorname{Ad}_{U^\dagger}.
\]

Ponieważ `U E_{ξ_U y}U†=E_y`, zachowuje to zadany POVM i legalność CP. Mapa `Q_s` komutuje z tymi symetriami. Uśrednienie po grupie nie powiększa odległości diamentowej, dzięki jej wypukłości i niezmienniczości unitarnej. Uśredniony instrument ma nieselektywny kanał unitalny i Pauliego postaci `diag(a,t,t)`, `−1≤a≤1`, `t∈ℝ`. Tak więc dowolny kandydat może zostać zastąpiony kandydatem tej postaci bez pogorszenia celu.

#### Dowód B — dokładna norma różnicy w rodzinie Pauliego

Niech `e=a−(1−s)` i `d=1−t≥0` (każdy kanał CPTP ma `t≤1`). Różnica superoperatorów ma mnożniki Blocha `(−e,d,d)` i zerową część identycznościową. Rozwinięcie w czterech sprzężeniach Pauliego ma współczynniki

\[
\frac{-e+2d}{4},\quad\frac{-e-2d}{4},\quad\frac e4,\quad\frac e4.
\]

Nierówność trójkąta dla norm diamentowych sprzężeń unitarnych daje górną granicę równą sumie modułów. Ta sama suma jest **dolną** granicą osiąganą przez znormalizowany stan Bella, ponieważ Choi różnicy jest w bazie Bella diagonalny z tymi czterema wartościami własnymi. Stąd dokładnie

\[
\lVert Q_s-\Phi_{a,t}\rVert_\diamond
=\frac{|e+2d|+|e-2d|+2|e|}{4}
=\max\{|e|,\,d+|e|/2\}.\tag{R13.2}
\]

#### Dowód C — ograniczenie wynikające z mierzalności `X`

Argument dopełniającego kanału i efektów środowiskowych z raportu Geeky-S10 stosuje się również przy `a<0`: w rozkładzie Pauliego `p_0=(1+a+2t)/4`, `p_1=(1+a−2t)/4`, `p_2=p_3=(1−a)/4` i `p_j≥0` dowód nie wymaga `a≥0`. Zatem zgodność z odczytem `μ=s` wymaga

\[
s\leq \frac{1-a+\sqrt{(1+a)^2-4t^2}}{2}.\tag{R13.3}
\]

Jeżeli `a<1−2s`, to `|e|>s≥1−√(1−s)`, co załatwia tę gałąź przez (R13.2). W przeciwnym razie po bezpiecznym podniesieniu (R13.3) do kwadratu:

\[
t^2\leq(1-s)(a+s)=(1-s)(1+e).\tag{R13.4}
\]

Jeżeli `t<0`, to `d≥1` i żądana dolna granica jest automatyczna. Przy `t≥0`, jeżeli `e≤0`, otrzymujemy `t≤√(1−s)` i `d≥1−√(1−s)`. Jeżeli `e≥0`, z (R13.2–R13.4):

\[
\lVert Q_s-\Phi\rVert_\diamond\geq
1-\sqrt{(1-s)(1+e)}+e/2.
\]

Prawa strona jest niemalejąca dla `e≥0`, gdyż jej pochodna to `1/2−√(1−s)/(2√(1+e))≥0`. W punkcie `e=0` daje właśnie `1−√(1−s)`. Brzegi `s=0,1` sprawdzamy bezpośrednio (dla ostrego POVM `s=1` konieczne jest `t=0`). Dowód dolnego ograniczenia jest zakończony.

#### Dowód D — osiągalność

Jawny instrument z pracy Geeky-S10 realizuje `a=1−s`, `t=√(1−s)`, `μ=s`. Dla niego `e=0` i (R13.2) daje dokładnie `d=1−√(1−s)`. Jest to minimum z (R13.1). **QED.**

### 3. Różnica między naprawą kanału i naprawą zgodną z rzeczywistym odczytem

LT5 udowodnił dla tej samej nie-CP mapy, bez zadawania POVM:

\[
\inf_{\Phi\,\mathrm{CPTP}}\lVert Q_s-\Phi\rVert_\diamond=s/2.
\]

Wymóg jednoczesnego wytwarzania konkretnego odczytu `E_±=(I±sX)/2` zwiększa optymalny błąd do `1−√(1−s)`. Nadwyżka wynosi

\[
\bigl(1-\sqrt{1-s}\bigr)-s/2=\frac{s^2}{8}+O(s^3).
\]

Jest dodatnia dla `0<s≤1`. Wniosek jest silniejszy niż stwierdzenie, że jawnie znaleziony kanał progowy jest najlepszy jedynie w dwupunktowej symetrycznej podrodzinie.

### 4. Niezależne kontrole

Dokładny algorytm NumPy rekonstruujący operatory Krausa i macierz Choi z macierzy jednostkowych oraz kontrolujący źródłowe POVM i kanał zapisano obok tego raportu jako `IW_REC10_ROT13_POVM_COMPATIBILITY_MATRIX_CHECK_20261023.py`. Dla `s=0.01,0.1,0.25,0.5,0.75,0.9,1` kontrola jawnego osiągnięcia normy `1−√(1−s)` jest PASS. Dodatkowa deterministyczna optymalizacja po `a,t` potwierdziła lokalizację minimum dla wartości `s=0.01,0.1,0.25,0.5,0.75,0.9`, ale dowodem globalnym jest wyłącznie symetryzacja i nierówności powyżej.

### 5. Ograniczenia twierdzenia i stan źródeł

`Q_s` **nie jest CP** dla `s>0`; porównanie nie jest fizycznym eksperymentem dyskryminacji dwóch możliwych urządzeń. Legalne są wyłącznie instrumenty po stronie porównawczej. Zgodność średniej mierzonej składowej i jej **nieselektywnego** resetu nie oznacza zgodności selektywnych trajektorii, gaussowskiej struktury szumu, dostępu do nowych kopii ani sprzętowych kosztów i chronologii. Wynik nie dotyczy NCDG, DTC0a, PBH ani nowej fizyki.

Podstawy matematyczne są dojrzałe: symetryzacja kanałów, Stinespring, Choi, normy całkowicie ograniczone i zgodność kanału z POVM. Nie przypisuje się pierwszeństwa odkrycia.

**Dyspozycja:** `SOURCE_THEOREM = PASS`; `GLOBAL_CONSTRAINED_OPTIMUM = PASS_WITH_SHARPENING`; `NO_MANUSCRIPT_MUTATION`; `BW_PENDING`; `OWNER_ACCEPTANCE_NOT_VERIFIED`. Zapis i doręczenie do systemów projektu należy raportować osobno — źródłowe repo nie staje się kanonem wskutek samej publikacji. Brak nowych zadań i brak awansu do EXEC.