# IW / M13 — ROT37: globalna separacja projektowa przy skorelowanych maskach — certyfikat źródłowy

**Return ID:** `M13-ROT37-DTC0A-INTERVAL-CERTIFIED-NONLOCAL-SHELL-SEPARATION-001_20261025`  
**Target:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001`  
**Klasa:** `EXACT_CLASSICAL_SHELL_GEOMETRY / OUTWARD_INTERVAL_SOURCE_SPECIFIC_GLOBAL_BOUND / NO_NEW_PHYSICS`  
**Status:** `NUMERICAL_SOURCE_FORMULA_CERT_PASS / HISTORIC_RUNTIME_BYTE_EXACT_UNAVAILABLE / NO_CANON / NO_EXEC_SIGN / TPE HOLD`.

## 1. Prior-art subtraction i rzeczywisty przyrost

M13 ROT23–27 odtwarzał historyczne przypadki z zachowanego pomocniczego źródła i rozdzielił maskę, projekcję TT oraz stencil. M13 ROT29–31 wykazał ograniczenia identyfikacji dowolnych pól tensorowych. ROT32–33 certyfikował identyfikację (α, wspólna amplituda) przez dwa kanały A/C w konkretnej rodzinie. ROT34 udowodnił źródłowo monotoniczność 18 i złożenie 12 par różnych masek *jednego* kanału; ROT35 wyprowadził dokładną kowariancję zagnieżdżonych masek. ROT36 zbadał nie-lokalne minimum po nieznanej amplitudzie wyłącznie przez optymalizację numeryczną. MT13 ma pierwszeństwo do ogólnej geometrii projective quotient/gain-nuisance oraz progów dla kul szumu.

**Nowy, ograniczony przyrost ROT37:** (i) źródłowy certyfikat przedziałowy **dodatniej globalnej dolnej granicy** dla dowolnych α,β w [0,0.2] z |α−β|≥0.01; (ii) ścisły **teoremat o argmin dla dwóch maskowanych średnich z dodatnimi powłokami** — minimum nie-lokalne zawsze na najbliższym dopuszczalnym krańcu, bez globalnego optymalizatora; (iii) weryfikacja tego twierdzenia bezpośrednią arytmetyką przedziałową dla trzech konkretnych par i α_true=0.05.

## 2. Źródło i typ obiektu

* `N=41`, `k∈{2,3,4,5,6}`, α∈[0,1/5]. Pola wejściowe: `C1=(0.05sin x,0.05cos y,0)`, `C2=(0.04cos z,0,0.04sin x)`, `h=0.1sin x cos y·I`.
* Stały płaski projektor Fourier TT, skończona druga różnica centralna, `Eα=I+α dx² Δ_h`, przestrzenne średnie energii `g_{c,k}(α)=RMS_mask(K_c)^2`, `c=A,B,C`, wrażliwe na środkową projekcję P.
* Rodzina źródłowo/funkcjonalnie dopasowana do pomocniczego `deepseek_python_20260627_a87249.py`; **oryginalnego historycznego produkcyjnego `dtc0a_runtime_v0_3_1.py` nie odnaleziono bajtowo**. Stare `h` jest **PURE TRACE**, a więc historyczne `K_A(h)` jest diagnostyką na przestrzeni ambient, nie operatorem ograniczonym do TT ani fizycznym niezmiennikiem.
* Jedna nieznana wspólna dodatnia amplituda `t=s²>0` skaluje **energię** obydwu masek tego samego kanału. Brak osobnych gainów maski, nieznanych generatorów, niezależnej kalibracji rzeczywistego szumu.

## 3. Dokładna algebra GLS i geometria promienia

Dla `k_i<k_j` oznaczmy `n_i=(N−2k_i)^3`, `n_j=(N−2k_j)^3`, `v=n_i−n_j`, `a(α)=(g_i(α),g_j(α))`. Dla niezależnego addytywnego szumu energii na voxelach o wariancji τ²:

\[
\Sigma=\tau^2\begin{pmatrix} 1/n_i&1/n_i\\1/n_i&1/n_j\end{pmatrix},\qquad
W=\tau^2\Sigma^{-1},\quad\det W=\frac{n_i^2 n_j}{v}.
\]

Przekształcenie do niezależnej zewnętrznej powłoki i rdzenia:

\[
L a=\left(\sqrt v\,\frac{n_i g_i-n_jg_j}{v},\,\sqrt{n_j}\,g_j\right),
\quad \|La\|_2^2=a^TWa.
\]

W przyjętej rodzinie wyprowadzone z wielomianów źródłowych **energię powłoki i rdzenia ograniczono poniżej przez wartości dodatnie** na całym przedziale α. Zatem `La` należy do pierwszej ćwiartki, a optymalne skalowanie dodatniego wzorca na inną dodatnią wiązkę promieni spełnia `t*>0`. Dla β:

\[
d(\alpha,\beta)=\min_{t\ge0}\|a(\alpha)-t a(\beta)\|_W
=\frac{|\det(a(\alpha),a(\beta))|\sqrt{\det W}}{\sqrt{a(\beta)^TWa(\beta)}}
=\|La(\alpha)\|_2 |\sin(\theta(\beta)-\theta(\alpha))|.
\]

Przy stałej dodatniej składowej `g_j`, kąt obrazu `(sqrt(v)*(n_i*r−n_j)/v,sqrt(n_j))` zależy monotonicznie od `r=g_i/g_j`: w pierwszej ćwiartce `θ=atan2(sqrt(n_j),sqrt(v)*(n_i*r−n_j)/v)` i `dθ/dr<0`. Dla `r(α)` ściśle monotonicznego `θ(α)` też jest ściśle monotoniczny. Ponieważ oba kąty leżą w `(0,π/2)`, `|sin(θβ−θα)|` wzrasta przy oddalaniu β od α w jedną stronę. **Stąd** dla ustalonej `α0` i `Δ>0` minimum nad `{β∈[0,0.2]: |β−α0|≥Δ}` występuje na jednym z legalnych `α0−Δ`, `α0+Δ`; nie potrzeba search/optimizera. Jest to klasyczna geometria promieni, nie nowe twierdzenie ogólnomatematyczne.

Dowód arytmetyki macierzy/czynników ilorazowych w niezależnym `verify_m13_rot37_exact_geometry.py` (standard library `Fraction`, 360/360 testów losowych z wymiernymi wartościami, jawna algebra powyżej).

## 4. Certyfikacja źródłowa: wszystkie α i porównanie ROT36

Program `verify_m13_rot37.py` rekonstruuje rzadkie tensory Fouriera przez `verify_m13_rot33_interval.py` i `mpmath.iv` (45 cyfr dziesiętnych). Dokładne wymierne źródła i symbol TT, przedziałowe π/sin/cos, okna i normy. Liczy wszystkie 15 wielomianów stopnia 4 dla trzech kanałów i pięciu masek, certyfikuje 45/45 historycznych odczytów RMS. Certyfikuje ściśle ujemne/dodatnie znaki wielomianu `g_i'g_j−g_i g_j'` (w zależności od pary), dodatniość `g_i,g_j,g_shell`, oraz podprzedziałami dodatnią granicę `γ≤|d log(R_i/R_j)/dα|`.

Z monotoniczności wynika dla dowolnych α,β oddalonych o co najmniej Δ:

\[
|\det(a(\alpha),a(\beta))|\ \ge
(\min g_i)(\min g_j)(e^{2\gamma\Delta}-1),
\]

zaś `a(β)^T W a(β)≤v(s_{shell,max})²+n_j (g_{j,max})²`. Wszystkie minima i maksima energii są ograniczone zewnętrznymi przedziałami współczynników Bernsteina. Daje to globalny **dodatni** dolny certyfikat (zwykle luźny), niezależny od numerycznej minimalizacji.

Wyniki w jednostkach syntetycznego `τ=0.01 g_{c,k=2}(0.05)` na voxel energii (źródłowo różne τ dla różnych kanałów):

| kanał / maski | ścisła granica min |dolna separacja dla **dowolnego** α,β z odstępem 0.01 | certyfikowany inf po β dla α0=0.05 | ROT36 numeryczny inf |
|:--|:--|--:|--:|--:|
| A, 2/5 | θ monotoniczny | >1.26724192 | 1.38826656075285 | 1.38826656075135 |
| B, 5/6 | θ monotoniczny | >0.27217934 | 231.521939344254 | 231.521939344268 |
| C, 2/4 | θ monotoniczny | >2.18872311 | 90.521697443341 | 90.521697443342 |

**Kandydaci globalni dla α0=0.05, Δ=0.01:** β∈{0.04,0.06}; we wszystkich trzech certyfikowane przedziały wyników rozróżniają kandydatów i dają **β*=0.06**. Dokładne wartości liczb rzeczywistych określają arytmetyczne przedziały, nie literalne przedstawione liczby zmiennoprzecinkowe. Zakres obejmuje całe legalne β, nie 4097 losowych lub równomiernie rozłożonych punktów.

**Pięć masek:** z własności GLS (obserwacja pełna zawiera parę) wynika `d_full5(α,β)≥d_pair(α,β)` dla ustalonego modelu szumu. Przy α0=.05 i Δ=.01 minimalna pięciowymiarowa odległość jest więc co najmniej wartością podaną w kolumnie par. Dla syntetycznego 5D Gaussa 95% promień wynosi `sqrt(chi2_5(0.95))≈3.32724`, a dostateczny próg rozłączności dwóch takich kul to `2*3.32724≈6.65447`: kanały B5/6 i C2/4 go przekraczają, A2/5 nie. Nie jest to stwierdzenie o rzeczywistym błędzie pomiaru ani o dokładnym infimum pięciu masek.

## 5. Kontrole i ograniczenia

- Drugi niezależny skrypt `verify_m13_rot37_exact_geometry.py` dowodzi tożsamości macierzy kowariancji, determinantów i projekcji na promień w `fractions.Fraction`. Nic nie importuje z operatora DTC0a.
- Bezpośrednio odtworzono 45 historycznych liczb RMS dla N41 × trzech α × pięciu masek × trzech kanałów z maksymalnym błędem względnym mniejszym niż `3e−15`.
- Wyniki ze ścisłych końców 0.04/0.06 są zgodne z wcześniejszymi 3 minimami ROT36 do `1.5e−11` w jednostkach τ. To *kontrola zgodności*, nie element certyfikatu.
- Sprawdzono dodatniość energii w zewnętrznej powłoce i środku na całym przedziale przez przedziałowe otoczki Bernsteina; inne kształty masek lub modele szumu nie są objęte.
- Certyfikat z `mpmath.iv` zależy od poprawności arytmetyki przedziałowej i zgodności implementacji formuł z zachowanym źródłem; nie jest formalnym dowodem w systemie proof assistant. Plik produkcyjny `dtc0a_runtime_v0_3_1.py` nie jest dostępny do bajtowej weryfikacji.
- Nie dowiedziono *dokładnego* globalnego minimum dla pełnej przestrzeni pięciu masek ani przypadków jednego kanału i dowolnie zmiennej amplitudy po maskach. Brak empirycznej kowariancji, niezależnej recenzji, ingest BW i podpisu EXEC.
- Nie wolno interpretować `K_A(h)` (h jest czysto śladowy), różnic TT i wyników źródłowych jako fizyki J3/K, efektu grawitacyjnego, przełomu matematycznego czy potwierdzenia TPE.

## 6. Odtwarzanie i archiwizacja

Uruchom w katalogu rozpakowanego ZIP: `python verify_m13_rot37_exact_geometry.py`, potem `python verify_m13_rot37.py`. Wymagane `mpmath==1.3.0`, `numpy` użyty wyłącznie jako niecertyfikowana kontrola numeryczna, nie w dowodzie. Wejściowy zestaw zawiera: powtórzony, niezmodyfikowany certyfikator operatorowy ROT33, JSON ROT36 do porównania oraz historyczne CSV. Wynik `IW_M13_ROT37_interval_global_lower_20261025.json` powstaje deterministycznie. SHA256SUMS obejmuje pozostałe pliki.

**Scientific gates:** `PASS (source-conditional mathematical); NO_NEW_TASK; NO_NOVELTY; NO_CANON; NO_EXEC_SIGN; NO_PHYSICAL_UPGRADE; TPE HOLD`.
