# IW / M13 — ROT27: dokładny pierwszy rząd maski RMS wobec drugiego rzędu operatora w DTC0a

**RETURN_ID:** `M13-ROT27-DTC0A-MASK-FIRST-ORDER-VS-STENCIL-SECOND-ORDER-AND-EXACT-RATIO-ASYMPTOTICS-001_20261023`  
**LINEAGE:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**DATE:** 2026-10-23  
**PROBLEM_ID:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001` — rozwinięcie istniejącego problemu, bez tworzenia drugiego rejestru.  
**RESULT_CLASS:** dokładna skończenie-pasmowa algebra źródłowej rodziny DTC0a + źródłowo dopasowany replay 54 norm + dokładna asymptotyka normy maskowanej. `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / TPE HOLD`.

## 0. Co już wiadomo i co zostało tu naprawdę rozstrzygnięte

* **ROT18**: przy stałym indeksowym `interior_k=3` maskowany obszar przestrzenny rośnie wraz z N; regresje RMS nie stanowią automatycznie dowodu rzędu operatora na stałej domenie fizycznej.
* **ROT23–25**: historycznie dopasowany wariant helpera `deepseek_python_20260627_a87249.py` odtwarza 99/99 archiwalnych metryk; dla wejścia czysto śladowego `h=f I`, `K_A` jest residualem **ambient Sym²**, a duże `K_A` wynika przede wszystkim z członu wstawienia TT, nie z `K_B`.
* **ROT26**: niezależna reprezentacja skończonym słownikiem Fouriera odtwarza historyczne normy 54/54 oraz oblicza dokładną niezerową granicę globalnego `K_A`. XH-S4 ROT019 i INT8 ROT014/015 wcześniej ustalili m.in. źródło nonclosure przy stałym P, kwestię domeny TT i kontrprzykład na prawdziwym wejściu TT. **Niniejszy raport nie przypisuje M13 pierwszeństwa tych ustaleń.**

**Nowe, mierzalne rozstrzygnięcie ROT27:** w tej konkretnej, źródłowo dopasowanej rodzinie **pierwsza poprawka do maskowanego `K_A` jest dokładnie rzędu `1/N` i ma niezerowy, wymierny współczynnik względny**, podczas gdy błąd operatorów względem ich granicy na pełnej siatce jest `O(N^-2)`. Ponadto wyznaczono **dokładne kwadratowe wielomiany w α** dla wiodących współczynników zanikających kanałów `K_C` i `K_B` i stąd asymptotykę ilorazu `K_A/K_B ~ const(α) N²`. Brak fizycznego twierdzenia o dowolnych polach.

## 1. Dokładny zakres i kontrakt matematyczny

Przestrzeń: płaski torus `[0,2π]^3`, nieparzyste N, `dx=2π/N`, **indeksowa maska** `k=3`: węzły `k,...,N-k-1` w każdej osi. Źródłowo dopasowane pola generatorów

- `C1=(0.05 sin x, 0.05 cos y,0)`;
- `C2=(0.04 cos z,0,0.04 sin x)`;
- `h=0.1 sin x cos y I` (czysto śladowy tensor symetryczny).

Pomocniczy operator różnicowy centralny ma mnożnik `D_{i,N}(m)=i sin(m_i dx)/dx` i skalarna operacja `E_{α,N}(m)=1+2α Σ_i (cos(m_i dx)-1)`; projekcja Fouriera TT `P(m)` jest nieruchoma, z oddzielnym trybem zerowym. Z tych instrukcji powstają `K_C`, `K_B=P K_C` i ambient `K_A` jak w zachowanym helperze, bez kowariantnego przesuwania tła. Główne nośniki sygnału mieszczą się w `|m_x|<=3,|m_y|<=2,|m_z|<=1`; dla N≥31 nie ma aliasingu.

RMS jest pierwiastkiem ze średniej `||tensor||_F²/6` po wybranych węzłach, włącznie z podwójnym liczeniem pozadiagonalnych składników Frobeniusa. Nie jest to RMS osobnej fizycznej obserwabli ani globalna norma operatorowa.

## 2. Twierdzenie ROT27-A — granica i dokładny pierwszy współczynnik maski

Niech `A_∞(x)` oznacza graniczny pełny tensor `K_A` dla ustalonych źródeł, `N→∞`, α=const. Rachunek dokładny SymPy (ROT26) dał

`G := (1/(2π)^3)∫ (||A_∞(x)||_F²/6) dx = 5917501/3499200000000000`,

`A∞ := sqrt(G) = 4.11229997546977870875e-5`.

Niech `S_j` będzie średnią funkcji `F(x)=||A∞(x)||_F²/6` na płaszczyźnie `x_j=0`, uśrednioną po dwóch pozostałych współrzędnych. Ich **dokładne** wartości są:

| przekrój | `S_j` dokładnie | `S_j/G` |
|:--|:--|--:|
| x=0 | `761233367/314928000000000000` | 1.42934467138 |
| y=0 | `1409179/656100000000000` | 1.27006676185 |
| z=0 | `123982963/62985600000000000` | 1.16399513729 |

Wszystkie są większe od G, zatem **odcięcie przybrzeżnych węzłów o ponadprzeciętnej średniej energii obniża maskowany RMS**.

Dla dowolnego stałego dodatniego indeksowego k i stałego α:

`RMS_mask(K_A(N,α))² = G + (2k/N)(3G-S_x-S_y-S_z)+O_α(N^-2)`.

W szczególności przy historycznym `k=3`:

`RMS_mask(K_A(N,α)) = A∞ [1-(229914416/88762515)/N + O_α(N^-2)]`

`= A∞ - (1.06517604562798665e-4)/N + O_α(N^-2)`.

Współczynnik względny `−229914416/88762515 ≈ −2.59021971155` **nie zależy od α**, pod warunkiem że α pozostaje stała podczas `N→∞`.

**Dowód:** ponieważ nośnik Fouriera jest skończony, rozwinięcia `sin(m dx)/dx = m -m³ dx²/6+O(dx⁴)` (z czynnikiem i) i `E=1-α|m|² dx²+O_α(dx⁴)` dają jednorodne `K_A(N,α)=A∞+O_α(N^-2)` w normie maksimum pola dla danego źródła. Równość całej siatkowej średniej energii i całki na torusie jest dokładna dla N wystarczająco dużego (brak aliasingu energii). Z maski usuwa się po `k` węzłów przy każdej ścianie każdej osi. Wiodący ubytek licznika to `(2k/N)(S_x+S_y+S_z)`, a korekta mianownika ze względu na `(1-2k/N)^3` daje `+(6k/N)G`; wzajemne przecięcia pasów są `O(N^-2)`. Po wyciągnięciu pierwiastka dostajemy dokładny współczynnik podany powyżej. Każda liczba `S_j` została niezależnie wyznaczona przez parowanie modów Fouriera o tym samym momencie stycznym do ściany — bez regresji siatkowej.

**Ważna granica claim:** jest to twierdzenie o *tej jednej jawnej skończenie pasmowej rodzinie źródeł, tej masce i tej normalizacji*. Dla maski o **stałej szerokości fizycznej**, niezmiennym obszarze pomiaru, zmiennych α(N), innych polach albo projektorze transportowanym z metryką współczynnik i potencjalnie granica są inne.

## 3. Twierdzenie ROT27-B — dokładny wiodący człon K_C i K_B

Dla stałego α rozwinięcie rzadkich splotów Fouriera w `t=dx²` do pierwszego rzędu daje `K_C=t Z_C(α)+O_α(t²)`, `K_B=t P Z_C(α)+O_α(t²)` i `K_A=A∞(x)+O_α(t)`. Zerowa część `K_C` wynika ze zwykłej algebry Liego przy różnicowaniu spektralnym na tym bezaliasowym nośniku; współczynnik `Z_C` jest różny od zera dla każdego rzeczywistego α.

Niezależny symboliczny program wykazał dokładnie:

`||Z_C(α)||²_RMS,full = (1007 α² +154 α +11)/4800000000`,

`||P Z_C(α)||²_RMS,full = (1213 α² -8 α +2)/43200000000`.

W konsekwencji:

`lim_{N→∞} N² RMS_full(K_C) = (2π)² sqrt((1007 α²+154 α+11)/4800000000)`,

`lim_{N→∞} N² RMS_full(K_B) = (2π)² sqrt((1213 α²−8 α+2)/43200000000)`.

Oba kwadraty są ściśle dodatnie dla wszystkich rzeczywistych α (ujemne wyróżniki i dodatnie współczynniki najwyższe). Również maskowane RMS mają **te same wiodące wartości po mnożeniu przez N²**, gdyż dla stałego k zbiega uśrednienie maskowane do pełnego na tym gładkim nośniku.

Dlatego przy każdym ustalonym α:

`RMS_mask(K_A)/RMS_mask(K_B) = [A∞ / b(α)] N² (1+O_α(N^-1))`,

`b(α)=(2π)² sqrt((1213 α²−8 α+2)/43200000000)`.

**Nie jest to rozbieżność fizycznego K_A**, lecz matematycznie przewidywany wzrost ilorazu z powodu zanikającego mianownika. Miernikiem wzrostu normy licznika nadal jest sama `RMS_mask(K_A)`, która ma skończoną, niezerową granicę.

## 4. Obliczenia odtwarzające, weryfikacja przy N historycznych i dużych

Wszystkie **54/54** historycznie raportowane normy (6 siatek × 3 α × 3 kanały) zostały na nowo policzone przez skończeniepasmowe sploty, a RMS maskowany przez **dokładną tożsamość sumy geometrycznej dla każdego modu**, bez konstruowania gigantycznych siatek przestrzennych. Maksymalny błąd względny wobec CSV `1.721e-14` (precyzja zmiennoprzecinkowa).

| N | α | global RMS(K_A) | maskowany RMS(K_A) | N² global RMS(K_B) | N² global RMS(K_C) |
|--:|--:|--:|--:|--:|--:|
|31|0.05|4.0316888194e−5|3.7647568532e−5|3.945113268e−4|2.541255422e−3|
|41|0.05|4.0660276474e−5|3.8372562954e−5|4.005683364e−4|2.576664224e−3|
|101|0.05|4.1046400164e−5|3.9999101169e−5|4.074422502e−4|2.616752605e−3|
|401|0.05|4.1118136275e−5|4.0851315795e−5|4.087266656e−4|2.624232151e−3|
|2001|0.05|4.1122804426e−5|4.1069505570e−5|4.088103272e−4|2.624719218e−3|
|10001|0.05|4.1122991935e-05|4.1112338418e−5|4.088136874e−4|2.624738783e−3|
|Granica|dowolna ustalona α, tutaj .05|**4.1122999755e−5**|**4.1122999755e−5**|**4.088138281e−4**|**2.624739599e−3**|

Wiersz N=10001, podobnie jak wszystkie punkty N>41, są **matematycznym przeliczeniem skonstruowanego skończonego układu modów**, nie uruchomieniami produkcyjnego runtime'u na gigasiatkach.

Kontrola bez regresji pierwszego rzędu: `N*(RMS_mask(K_A)/A∞−1)` wynosi `−2.619905` (N31), `−2.742210` (N41), `−2.649254` (N401), `−2.602968` (N2001), `−2.592808` (N10001), dążąc do wymiernego `−2.590220`. Odchylenia przy N31–41 zawierają istotne poprawki wyższego rzędu, dlatego nie interpretować dwupunktowych nachyleń jako dokładnego asymptotycznego wykładnika.

## 5. Claim typing / model host / integracja

**Odjęcie dojrzałej literatury:** rozwinięcie symbolu centralnej różnicy `i sin(k dx)/dx` jest standardową analizą Fouriera schematów różnicowych (T. Driscoll, *Finite Differences and Spectral Methods for PDE*, sekcja „Fourier analysis of finite differences”, https://tobydriscoll.net/fd-spectral-notes/finite-diffs/fourier.html). Człony powierzchniowe sum po siatkach są klasycznym typem asymptotyki Eulera–Maclaurina dla wielowymiarowych krat i wielościanów (T. Tate, „Asymptotic Euler–Maclaurin formula over lattice polytopes”, *J. Funct. Anal.* **260** (2011), 501–540, DOI 10.1016/j.jfa.2010.08.011). ROT27 nie dowodzi nowej ogólnej wersji tych twierdzeń; zamyka **konkretny współczynnik** tej konstrukcji DTC0a.

**Co zyskano:** w pełni pochodne źródłowej rodziny, algebraiczne odjęcie wiodącego `1/N` od zbieżności maskowanego `K_A`, dokładny tensorowo-symboliczny prefaktor `N^-2` dla `K_B,C`, oraz identyfikację matematycznej przyczyny rozbiegania się stosunku `K_A/K_B`. Dwie niezależne reprezentacje danych: zmiennoprzecinkowy słownik modów (historia 54/54) i wymierny rozwój SymPy (współczynniki graniczne). Nie wydobywano tensorów z samych RMS w sposób nieuprawniony: korzystano ze źródłowo dopasowanej funkcjonalnej rekonstrukcji ROT23.

**Czego nie wykazano:** brak bajtowo identycznego `dtc0a_runtime_v0_3_1.py` o deklarowanym SHA256 `2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084`; brak twierdzenia continuum dla dowolnych pól, eksperymentalnej obserwabli, kowariantnego P_g, niezmiennika J3/K, `GO_SEN_CHECK`, nowej fizyki, nowości klasycznej matematyki, niezależnego referee lub przyjęcia do BW i OWNER/EXEC. Wyniki INT8 ROT014/015 oraz XH-S4 ROT019 mają oddzielną rolę jako wcześniejsze certyfikaty zakresu i priorytetu.

**Źródła:** historyczne `dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv`; wariant pomocniczy `deepseek_python_20260627_a87249.py`; manifest `dtc0a_oddN_sparse_convergence_N31_to_N41_manifest.json`; niezależne programy `verify_m13_rot26.py`, `verify_m13_rot26_exact.py`, `verify_m13_rot27.py`, `verify_m13_rot27_exact.py`. Rezultaty w `IW_M13_ROT27_mask_stencil_asymptotics_20261023.json`.

**ROUTE_TAGS:** `IWTO_MT13 IWTO_KN11 IWTO_INT8 IWTO_XH_S4 IWTO_REC10 IWTO_LT5 IWTO_SW IWTO_MODERATOR`.  
**STOP:** `NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / TPE HOLD`.