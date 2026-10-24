# IW / M13 — ROT33: ścisła kontrola przedziałowa znaku pochodnej modelu DTC0a

**RETURN_ID:** `M13-ROT33-DTC0A-DIRECTED-INTERVAL-SOURCE-OPERATOR-BERNSTEIN-MONOTONICITY-001_20261024`  
**PROBLEM_ID:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001` (kontynuacja ROT32, bez nowego zadania ownera)  
**DATE:** 2026-10-24  
**CELL:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**CLASS:** `SOURCE_HELPER_FORMULA_DIRECTED_INTERVAL_CERTIFICATE / 10_CASES_PASS / NO_HISTORICAL_RUNTIME_BYTE_EXACT / NO_PHYSICAL_UPGRADE`

## 1. Problem i odejmowanie wcześniejszego dorobku

M13 ROT23 odbudował pełne tensory z alternatywnego zachowanego helpera DTC0a i dopasował 99/99 historycznych norm. M13 ROT24–28 rozłożył wkład filtra, przestrzennej maski i projekcji TT, ROT29–31 podał kontrprzykłady nieidentyfikowalności dla **ogólnych** tensorów TT przy pomiarach pięciu RMS. ROT32 ograniczył problem do znanych generatorów i dwóch niewiadomych: `alpha` w [0,1/5] oraz wspólny dodatni mnożnik amplitudy `s`. Wtedy stwierdzono monotoniczność ilorazu kanałów A/C, ale obliczano współczynniki na zmiennoprzecinkowych tensorach. Dokładny certyfikat ROT32 dotyczył **już zapisanych dziesiętnych współczynników**, nie oryginalnych wartości funkcji trygonometrycznych.

**Nowa wartość ROT33:** bezpośrednio objąć obliczenia źródłowego modelu **arytmetyką przedziałową na każdym etapie**, otrzymać interwały współczynników w bazie Bernsteina i sprawdzić ich ujemny znak, bez zastępowania oryginalnych współczynników wielomianowymi wartościami obciętymi dziesiętnie. Jest to klasyczne zastosowanie arytmetyki przedziałowej i baz Bernsteina, **bez twierdzenia o nowości matematycznej**.

Wyniki INT8/Geeky-S11/XH-S4/PRF11 dotyczą innej funkcji: niezamknięcia algebraicznego, zgodności symbolu TT ze stencilem, aliasingu, kowariancji i domeny TT; nie wolno ich mieszać z prostą identyfikacją dwóch parametrów znanej rodziny.

## 2. Dokładnie określona rodzina

Rozpatrujemy torus [0,2pi)^3, nieparzyste N w {31,33,35,37,39,41}, `dx=2*pi/N`, operator różnicowania centralnego drugiego rzędu, filtr `E_lin=I+alpha dx² Delta_N`, stały spektralny projektor Fourier-TT oraz wewnętrzną maskę `[k:N-k]^3`. Zachowane pola wejściowe:

```
C1=(0.05 sin x, 0.05 cos y, 0)
C2=(0.04 cos z, 0, 0.04 sin x)
h = 0.1 sin x cos y * I_3
```

Dla niezerowego m, `P_m=I-mm^T/|m|²` i `P_TT(H)=P_m H P_m - P_m tr(P_m H)/2`; dla m=0 odejmowany ślad `tr(H) I/3`. Definiujemy `L_C=Lie_C∘E_lin`, `b=[C1,C2]`,

```
K_C = L_C1 L_C2 h - L_C2 L_C1 h - L_b h
K_B = P_TT K_C
K_A = P_TT L_C1 P_TT L_C2 h - P_TT L_C2 P_TT L_C1 h - P_TT L_b h.
```

Współczynniki wejściowe trygonometrii są konstruowane z ułamków wymiernych (`1/40`, `1/50`), a czynniki dla modalnego m liczone przedziałowo:

```
D_N(m_i) = i sin(2pi*m_i/N)/(2pi/N),
E_alpha(m) = 1 + 2 alpha sum_i (cos(2pi*m_i/N)-1).
```

Dla ustalonego N,k pole `K_j(alpha)=U_j+alpha V_j+alpha² W_j`, więc `g_j(alpha)=RMS_mask(K_j(alpha))²` jest wielomianem stopnia najwyżej 4. Rzeczywiste maskowane średnie iloczynów modalnych liczone są przez skończoną tożsamość sumy geometrycznej, również przy użyciu interwałów sin/cos; nie ma w verifierze FFT, siatek 3D ani zmiennoprzecinkowego Numpy. Projekcja TT na modach jest dokładnie wymierna.

## 3. Certyfikat monotoniczności

Niech `r(alpha)=sqrt(g_A(alpha)/g_C(alpha))` oraz

\[
p(\alpha)=g_A'(\alpha) g_C(\alpha)-g_A(\alpha)g_C'(\alpha).
\]

Wtedy

\[
\frac{d\log r}{d\alpha}=\frac{p(\alpha)}{2g_A(\alpha)g_C(\alpha)}.
\]

Na `alpha` z [0,1/5] przeliczamy współczynniki Bernsteina `beta_i` wielomianu `p`, bez aproksymacji samych funkcji; to algebraiczna zmiana bazy po ustaleniu przedziałowo obliczonych współczynników potęgowych. Jeśli każda górna granica `beta_i` jest ściśle ujemna, to **p(alpha)<0 dla każdego alpha w domkniętym przedziale**. Analogiczna dodatniość wszystkich dolnych granic współczynników Bernsteina `g_A,g_C` certyfikuje mianownik.

Użyto `mpmath==1.3.0`, `mpmath.iv`, 45 cyfr dziesiętnych. Każda poniższa górna granica ujemna jest zaokrągloną do prezentacji wartością z wyniku przedziałowego; sam test znaku w kodzie wykonywany jest **bez zamiany na float** (`interval.b < 0`).

| N | k | Najwyższa górna granica `beta_i/(g_A(0)g_C(0))` | Maksymalna szerokość interwału | Dolne ograniczenie `|d log r/d alpha|` |
|---:|---:|---:|---:|---:|
| 31 | 3 | -13.800162570 | 2.09e-40 | 0.882384795 |
| 33 | 3 | -13.840530950 | 2.34e-40 | 0.878336450 |
| 35 | 3 | -13.872244263 | 2.59e-40 | 0.875687675 |
| 37 | 3 | -13.897503134 | 2.16e-40 | 0.874086278 |
| 39 | 3 | -13.917874982 | 2.35e-40 | 0.873267067 |
| 41 | 2 | -13.856597044 | 2.59e-40 | 0.895462418 |
| 41 | 3 | -13.934492287 | 3.30e-40 | 0.873030095 |
| 41 | 4 | -13.991729978 | 3.78e-40 | 0.864886909 |
| 41 | 5 | -14.013097513 | 3.89e-40 | 0.869759533 |
| 41 | 6 | -13.998521755 | 3.88e-40 | 0.882826819 |

**Werdykt:** **10/10 PASS**; najmniej ujemny górny współczynnik (normalizowany) = `-13.800162570131`, największa szerokość = `3.889e-40`. Dla wszystkich 10 przypadków dolne granice wielomianów `g_A, g_C` w bazie Bernsteina są dodatnie. Zatem, w zadeklarowanych operatorach:

\[
\forall N,k\in\mathcal T,\quad\forall\alpha\in[0,0.2],\quad
\frac{d}{d\alpha}\frac{R_A(\alpha)}{R_C(\alpha)}<0,
\]

gdzie `T={(N,3):N=31,33,35,37,39,41} ∪ {(41,k):k=2,4,5,6}`.

## 4. Dodatkowy certyfikat odporności względnej

Biorąc najostrzejszą z dziesięciu dolnych granic z przedziałowego rachunku, otrzymujemy **jednolity certyfikat na badany skończony zestaw**

\[
\left|\frac{d}{d\alpha}\log\frac{R_A}{R_C}\right| \ge 0.864886909399.
\]

Przy jednym wspólnym nieznanym dodatnim skalowaniu obu kanałów `s` iloraz je usuwa. Jeśli oba RMS są mnożone niezależnie przez współczynniki w `[1-eps,1+eps]`, to obserwowany logarytm ilorazu zmienia się najwyżej o `log((1+eps)/(1-eps))`. Po odwróceniu monotonicznej funkcji, z obcięciem estymatora do [0,0.2], dostajemy globalną granicę:

\[
|\widehat\alpha-\alpha|\le\frac{\log((1+\epsilon)/(1-\epsilon))}{0.864886909399}.
\]

Dla `epsilon=0.005` daje to `0.011562301644`. Jest to konserwatywna gwarancja w modelu **błędu względnego i poprawnej klasy źródłowej**; nie rozwiązuje z ROT32 problemu wzrostu wrażliwości na błędy **absolutne** przy N→infinity (`K_C=O(N^-2)`). Nie dopuszcza niezależnych nieznanych amplitud kanałów A i C ani nieznanych zmian generatorów.

## 5. Kontrola z zamrożonymi wynikami

Verifier odczytuje dwie zachowane tabele użytkownika: serię sześciu N z `k=3` oraz dodatkowe maski `N=41,k=2,4,5,6` na alpha 0,.05,.2. Weryfikuje 10 konfiguracji ×3 alpha ×2 kanały = **60/60 source-matched scalar RMS PASS**. Maksymalny względny błąd obliczonych wartości środkowych względem historycznych CSV to `2.887e-15`. Jest to porównanie numeryczne historycznych norm, **nie ścisłe objęcie ich zaokrąglonych wartości w przedziałach**. Pozostałe kanały oraz 99/99 wcześniejszych testów ROT23 należą do osobnego audytu.

## 6. Status epistemiczny, nieprzekraczalne ograniczenia

1. **Dowód warunkowy, ale bezpośredni:** przy poprawności zadeklarowanych skończonych formuł, wsparciu modowym i implementacji `mpmath.iv`, testy ujemności/dodatniości są odporne na błędy zaokrągleń w obliczeniach funkcji trygonometrycznych. Nie jest to formalnie zweryfikowany proof assistant, ani niezależnie certyfikowana implementacja biblioteki arytmetyki przedziałowej.
2. **Źródło:** zachowany helper `deepseek_python_20260627_a87249.py` SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`, wcześniej 99/99 scalar functional replay. Nie odzyskano oryginalnego bajtowo `dtc0a_runtime_v0_3_1.py` (oczekiwany SHA256 `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084`). Nie utożsamiać tych plików.
3. **Domena i target:** `h=f I` jest śladowe; wynik dotyczy ambient `K_A`, nie komutatora ograniczonego do TT i nie gauge-invariant fizycznego sygnału. K_B i K_C są residualami określonymi przez model numeryczny.
4. **Odwracalność:** identyfikowalność `alpha,s` tylko dla wspólnego skalowania dodatniego oraz wiadomych C1,C2,h, E, stencil, N, maski, projektora. Nie obala nieidentyfikowalności ogólnych pól TT ROT29–31, ani nie rozstrzyga fold A/B ROT32.
5. **Granice:** nie twierdzimy globalnej odwracalności poza [0,0.2], jednorodnego uwarunkowania wobec szumu absolutnego przy N→infinity, limitu fizycznego, nowej matematyki czy odkrycia K/J3/TPE.
6. **Niezależne akceptacje:** brak potwierdzenia niezależnej recenzji, włączenia do BW i zgody owner/Moderator EXEC. `NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK / NO_NOVELTY / NO_PHYSICAL_UPGRADE / TPE HOLD`.

## 7. Odtwarzalność

Główny skrypt: `verify_m13_rot33_interval.py`, standard Python + `mpmath 1.3.0`, bez NumPy. Instrukcja: `python verify_m13_rot33_interval.py` (generuje `IW_M13_ROT33_directed_interval_certificates_20261024.json`). Rygorystyczne porównanie kodu i wyjścia z zamkniętym pakietem umożliwiają dołączone sumy SHA-256. Dołączono historyczne dwie tabele CSV, source helper oraz wcześniejsze skrypty ROT26/ROT32 **dla przejrzystości pochodzenia**, nie jako zależności runtime certyfikatora. Wpis data i log opisują zakres audytu, nie dowód niezależnej oryginalności.