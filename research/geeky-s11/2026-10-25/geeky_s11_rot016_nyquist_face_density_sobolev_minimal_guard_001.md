---
artifact_id: GEEKY-S11-ROT016-SOURCE-RAW-EVEN-NYQUIST-FACE-DENSITY-SOBOLEV-AND-MINIMAL-GUARD-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-25
problem_id: P3_DTC0A_EVEN_RAW_REALCAST_TT_MINIMAL_SUPPORT_GUARD_AND_REGULARITY_001
exposure: PUBLIC_SAFE
class: EXACT_SOURCE-HELPER_FOURIER_SUPPORT_AND_HS_CENSUS_WITH_WHITE-NOISE_TRACE_CONTROL
status: MATHEMATICAL_PROOF_AND_43_EXECUTED_TYPED_CONTROLS_PASS / INDEPENDENT_REFEREE_PENDING
bw_ingestion_event_id: GITHUB_PENDING_BW_INGEST
claim_ceiling: FINITE_FOURIER_OPERATOR_HOST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT016 — wąski nośnik widmowy defektu raw-k, ostry próg Sobolewa i minimalny strażnik modów

## 0. Subtrakcja, aktualność i dokładny operator

ROT015 tej samej komórki **wcześniej** udowodnił, że na parzystych siatkach pomocniczy kod źródłowy DTC0a zwraca `A_N=Re(ifft(P_raw(k)*fft(.)))`, a nie rzeczywistą projekcję: `||A_N²-A_N||<=1/4`, z równością dla `10|N`, a minimalna odległość do dowolnego rzeczywistego rzutowania ortogonalnego wynosi wtedy `1/2`. ROT013/014 badają **nieparzyste** siatki i odmienne zagadnienia. PRF11 R25–R27 należy do źródłowego komutatora i błędów Sobolewa; INT8 do geometrii kątów głównych TT, M13 do historycznych pól `h=fI` i masek. ROT016 nie przywłaszcza żadnego z tych wyników. Obecny wkład to **osobno**: dokładna liczność wadliwych częstotliwości, ostry porządek regularności defektu idempotentności, ścisłe prawo średniej energii dla zadeklarowanego białego wejścia oraz minimalny częstotliwościowy strażnik przywracający dokładną projekcję *bez zmiany źródłowego mnożnika*.

Źródłowa podstawa: zachowany niezmodyfikowany plik `deepseek_python_20260627_a87249.py`, SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`. Pełne rzeczywiste symetryczne tensory rzędu 2 na płaskim okresowym `N³`, N parzyste N>=4, normy znormalizowanego niezamaskowanego `L²` z Frobenius. Historyczne `dtc0a_runtime_v0_3_1.py` nadal niedostępne bajtowo. Kod źródłowy pomocniczy ma przy k=0 rzutowanie na podprzestrzeń bezśladową rzędu 5 i przy k≠0 surowe `fftfreq` TT rzędu 2. Po odwrotnej FFT **jawnie** bierze część rzeczywistą.

## 1. Dokładny nośnik defektu i liczność (R16.1)

W podpisanej siatce Fourier `S_N={-N/2,-N/2+1,...,N/2-1}`, każdemu wektorowi k odpowiada sprzężony reprezentant `k*=signed(-k mod N)`. Współrzędna Nyquista `-N/2` zachowuje znak w obu, pozostałe zmieniają znak. Przed real-cast mnożnik P(k) to rzut TT. Po real-cast, na rzeczywistych polach: `A_k=(P(k)+P(k*))/2`.

Niech `a(k)=(N/2)²` razy liczba współrzędnych Nyquista, `b(k)=sum(k_j²)` po pozostałych współrzędnych. Wtedy dla `a+b>0`:

- `k·k*=a-b`, `|k|²=|k*|²=a+b`;
- `sin²(theta_k)=4ab/(a+b)²`;
- dokładny defekt na modzie: `||A_k²-A_k||=ab/(a+b)²`;
- dokładny współczynnik normy wyrzuconej części urojonej: `sqrt(ab)/(a+b)`.

**Wniosek IFF:** wada istnieje dokładnie tam, gdzie `a>0` oraz `b>0`. `a>0` oznacza co najmniej jedną współrzędną Nyquista, zaś `b>0` co najmniej jedną zwykłą niezerową. Na pozostałych częstotliwościach `P(k*)=P(k)` i `A` jest ścisłym ortogonalnym rzutowaniem. Liczymy unię trzech ścian Nyquista i odejmujemy 7 samosprzężonych modów niezerowych z koordynatami wyłącznie w `{0,-N/2}`:

**`M_N = [N³-(N-1)³]-7 = 3N²-3N-6`.**

Defect density `M_N/N³=3/N-3/N²-6/N³`, tj. maleje jak `3/N`. Liczność dotyczy **całych modów**, nie niezależnych par czy 6 tensorowych polaryzacji. Każdy z M_N jest w rzeczywistości wadliwą parą podlegającą sprzężeniu rzeczywistego pola; pełny zestaw wyłączanych modów jest automatycznie zamknięty na sprzężenie.

## 2. Ostre oszacowanie regularności (R16.2)

Na siatce użyj surowej okresowej normy Sobolewa `||H||_(H^s_N)²=sum_{k∈S_N³}(1+|k|²)^s ||Hhat(k)||_F²`, s>=0, z poprawną normalizacją Parsevala. Ponieważ każdy wadliwy mod ma `|k|²>=N²/4`, a `||A_k²-A_k||<=1/4`, dla **wszystkich parzystych N**:

**`||A_N²-A_N||_(H^s→L²) <= (1/4)(1+N²/4)^(-s/2)`**,

**`||Im B_N||_(H^s→L²) <= (1/2)(1+N²/4)^(-s/2)`**,

gdzie `B_N=ifft(P_raw fft(.))` jest operatorem przed wymuszeniem części rzeczywistej. Na podciągu N=10t wektor `k=(-5t,3t,4t)` ma `a=b=N²/4` i `|k|²=N²/2`. Testowe rzeczywiste polaryzacje w odpowiednich maksymalnych podprzestrzeniach dają **dolne granice**:

**`||A_N²-A_N||_(H^s→L²) >= (1/4)(1+N²/2)^(-s/2)`**,

**`||Im B_N||_(H^s→L²) >= (1/2)(1+N²/2)^(-s/2)`**.

Zatem obie normy są `Theta(N^(-s))` dla N→∞ **po wielokrotnościach 10** dla dowolnego s>=0, w szczególności **nie zanikają dla s=0**, a zanikają dla każdego s>0. Dla pojedynczego ustalonego gładkiego pola rezultat można odczytać jako oszacowanie operatorowe regularności, ale nie jest to porównanie z ciągłym projektorem ani wynik fizyczny.

## 3. Średnia energia przy białym tensorze (R16.3)

Zdefiniuj precyzyjnie losowe wejście `H(j)=sum_{a=1}^6 X_a(j) B_a`, gdzie `B_a` stanowią ortonormalną bazę rzeczywistych symetrycznych macierzy 3x3, a wszystkie `X_a(j)` są niezależnymi N(0,1). Nie chodzi o arbitralny stochastyczny proces fizyczny. Dzięki rotacyjnej niezmienniczości tej **tensorowej** kowariancji, oczekiwana energia wejścia na mod wynosi 6.

Niech `z_k=sin²(theta_k)`. Macierz przejścia `Im B_N` ma dla modów sprzężonych normę Frobeniusa do kwadratu `tr[((P(k)-P(k*))/2)^2] = z_k(8-z_k)/8`, co wynika z dwóch wartości głównych nakładania TT `c_k`, `(1+c_k²)/2`. Zatem **dokładna równość dla skończonej siatki**:

**`E||Im B_N H||² / E||H||² = [1/(48N³)] sum_(k∈S_N³) z_k(8-z_k)`**.

Suma ma tylko O(N²) niezerowych składników. Na trzech głównych ścianach Nyquista poza ich przecięciami, w skalowanych zwykłych współrzędnych x,y∈[-1/2,1/2],
`z(x,y)=(x²+y²)/(1/4+x²+y²)²`. Klasyczna suma Riemanna i marginalny O(N) wkład przecięć dają

**`E||Im B_N H||²/E||H||² ~ C/N`**, gdzie

`C=(1/16)*integral_{[-1/2,1/2]²} z(x,y)(8-z(x,y)) dx dy = 0.362975...`.

RMS ratio typowych białych wejść skaluje się zgodnie z `sqrt(C/N)≈0.6025/sqrt(N)`; to wskazówka o klasie rozkładu, nie deterministyczny bound dla każdego H. Co ważne: **iloraz oczekiwań energii** nie jest automatycznie tym samym co oczekiwanie z losowego ilorazu norm dla pojedynczej realizacji.

## 4. Minimalny strażnik modów i jego precyzyjny zakres (R16.4)

Wprowadź skalarny maskujący mnożnik Fourier `G_N(k)=0` wtedy i tylko wtedy, gdy `a(k)b(k)>0`, a `G_N(k)=1` w pozostałych punktach. Jest to **minimalny strażnik w klasie masek dopuszczających albo odrzucających cały 6-składnikowy tensorowy mod**: zachowuje dokładnie `N³-M_N=N³-3N²+3N+6` modów. Maska jest realna, samosprzężona i zgodna ze sprzężeniem FFT.

`G_N` komutuje z `A_N`. Ponieważ każdy zatrzymany mod ma `P(k)=P(k*)`, operator `A_N` na `ran(G_N)` jest **dokładną rzeczywistą projekcją ortogonalną**: dla wszystkich tensorów H zachodzi `A_N² G_N H=A_N G_N H`, a przed wymuszeniem realności `Im B_N G_N H=0` (równości analityczne). Usunięcie wyłącznie jednej z par wadliwych modów przy zachowaniu całych 6 polaryzacji nie daje takiej gwarancji — na modzie pozostaje niezerowy defekt operatorowy. Alternatywne strażniki mogą zachowywać wybrane polaryzacje, ale należą do innej, bogatszej klasy i nie podlegają temu minimalnemu twierdzeniu.

**Granica przenoszenia:** wstawienie `G_N` do obliczenia Lie/komutatora, źródłowej lokalnej maski RMS, oryginalnego historycznego K_A lub dynamiki samo w sobie NICZEGO nie dowodzi. Różne operacje mogą generować nowe wadliwe częstotliwości; konieczny jest osobny zamknięty protokół filtrowania i walidacji. Nie jest to autoryzowana zmiana historycznego operatora.

## 5. Niezależny test i odtwarzalność

Standalone NumPy `geeky_s11_rot016_nyquist_density_sobolev_verify.py`, napisany niezależnie od reproduktora ROT015, liczy dokładne trzy ściany Nyquista bez pętli po całym N³. Przeprowadzono 14 analiz częstotliwości dla N=8,10,12,16,20,24,32,40,60,80,120,160,240,320, po dwie klasy kontroli każda: dokładny całkowitoliczbowy census i granice Sobolewa, razem 28; trzy całki metodą midpoint z 300²/600²/1200² punktów; 4 testy rzeczywistej źródłowej funkcji `apply_P_TT` (N8,12,20,32), 4 grupy po 12 N(0,1) szerokopasmowych tensorów, 4 bezpośrednie testy dokładnego guardu. **RAZEM 43 typowane kontrole PASS.**

Granice liczbowe: asymptotyczna kwadratura C=0.3629749380188882, `N=320` iloczyn N razy skończona oczekiwana energia 0.3608930814351546; cztery stosunki średnich 12-próbkowych odchyleń względnych od wartości oczekiwanej to ok. 1.012665, 0.994702, 0.997556, 0.995286. Maksymalna rozbieżność źródłowego helpera z niezależną pełną projekcją w normie wejścia na czterech siatkach 2.05e-16. Pełny JSON zawiera skończone wartości dla s=0,1,2,3 na wszystkich N.

Pakiet lokalny dostarcza oryginalny skrypt, oryginalny JSON, dokładny raport, niezmodyfikowany pomocniczy kod z SHA, README, stdout, SHA256 manifest. Test wymaga tylko Python + NumPy. Kod źródłowy produkcyjny nadal niedostępny. Lokalny clean unzip + regeneracja JSON + SHA są osobnym testem archiwalnym, nie roszczeniem o autoryzowaną produkcyjną walidację DTC.

## 6. Negative knowledge

- Jądro i nośnik defektu są **real-linearne**; przed real-cast źródłowy surowy mnożnik Fourier jest idempotentny na ogólnych **zespolonych** tablicach, ale nie zachowuje rzeczywistości.
- Rzadkość wadliwych częstotliwości NIE oznacza małego błędu operatorowego L²: z ROT015 wartość 1/4 wciąż jest dokładna na N=10t.
- Zanik H^s jest o defekcie **jednej operacji projekcji** i części urojonej, NIE o błędzie komutatora, uogólnionej TT-kowariancji, ewolucji PDE czy fizyce.
- Brak roszczenia do nowości: Fourier, twierdzenie Parsevala, alias Nyquista, probabilistyczny rachunek śladowy i klasyczne oszacowania Sobolewa są dojrzałe.
- `NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / BW_PENDING / INDEPENDENT_REFEREE_PENDING / NO_ORIGINAL_RUNTIME_BYTE_EXACT`.
