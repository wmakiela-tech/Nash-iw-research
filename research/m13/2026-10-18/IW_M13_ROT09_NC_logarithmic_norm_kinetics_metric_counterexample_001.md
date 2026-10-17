# IW / M13 — ROT09: stabilna kinetyka nie wymusza ujemnej normy logarytmicznej w każdej normie


**RETURN_ID:** `M13-ROT09-NC-SHARPENING-A6-STABLE_KINETICS_LOGNORM_METRIC_RELATIVITY-001_20261018`  
**FROM_CELL:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**DATE:** 2026-10-18  
**CLASS:** dokładny kontrprzykład kinetyczny / claim-local repair / mature logarithmic-norm mathematics  
**STATUS:** exact finite-dimensional proof; nie jest recenzją całego rozdziału lub modelem BBN; `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_NEW_TASK`.


## 1. Punkt kontrolowany i subtraction-first


Pakiet `IW_NC_LT4_MONOGRAPH_SHARPENING_PACKET_002_20261018`, §A, proponuje poprawne, przy odpowiedniej normie i hipotezie jednostronnej, zastąpienie dwustronnego oszacowania Lipschitza w Tw. 7.3 przez normę logarytmiczną / jednostronną stałą Lipschitza. Pakiet jednak argumentuje w §A.6, że „kinetyka jest dyssypatywna, więc μ<0”. Bez zadeklarowania przestrzeni, normy i jej jednostronnej nierówności jest to zbyt mocny wniosek. Nie obalamy Grönwalla z µ, tylko automatyczne przejście od kinetyki/stabilności do **ujemnej** µ w normie, w której mierzony jest błąd.


W aktualnym stanie projektu INT7 niezależnie zaudytował §B tego samego pakietu (kolizje spektralne i niepoprawna granica przez supremum bloków), ale jawnie wyłączył §A ze swojego audytu; wynik ROT09 dotyczy wyłącznie §A.6.


## 2. Minimalny fizycznie typowany nośnik kinetyczny


Niech dwie populacje przechodzą między sobą ze stałymi szybkościami a=1 i b=4, a każda ponadto zanika ze stałą ε=1/10. Dla wektora populacji n=(n₁,n₂)^T przy konwencji kolumnowej:


\[
\dot n=A n,\qquad
A=\begin{pmatrix}-11/10&4\\1&-41/10\end{pmatrix}
=\begin{pmatrix}-1&4\\1&-4\end{pmatrix}-\tfrac1{10}I.
\]


Jest to macierz Metzlera (pozadiagonalne elementy są nieujemne); dodatnie dane początkowe pozostają dodatnie. Suma populacji spełnia dokładnie
\[
\frac{d}{dt}(n_1+n_2)=-\tfrac1{10}(n_1+n_2),
\]
a więc każda nieujemna trajektoria traci masę monotonicznie. Wartości własne A są równe `−1/10` i `−51/10`, więc dynamika jest wykładniczo stabilna.


## 3. Obliczenie trzech norm logarytmicznych


W zwykłej normie euklidesowej:
\[
\mu_2(A)=\lambda_{\max}\!\left(\frac{A+A^T}{2}\right)
= -\frac{13}{5}+\frac{\sqrt{34}}2
\approx 0.3154759474 >0.
\]
Zatem **stabilność spektralna + dodatniość + ścisła utrata sumarycznej masy nie implikują** `µ₂(A)<0`. Dla dodatniego wektora własnego części symetrycznej odpowiadającego µ₂(A), funkcja `||e^{tA} n(0)||₂` na początku **rośnie**, mimo że `n₁+n₂` maleje. Wektor własny można wybrać z obiema składowymi dodatnimi, ponieważ część symetryczna ma dodatnie wyrazy pozadiagonalne.


Jednocześnie dla normy \(\ell^1\):
\[
\mu_1(A)=\max_j \left(A_{jj}+\sum_{i\ne j}|A_{ij}|\right)
=-\frac1{10}.
\]
Dla `n(0)≥0`, `||n(t)||₁=e^{-t/10}||n(0)||₁` dokładnie; dla dowolnej perturbacji obowiązuje standardowe oszacowanie semigrupowe `||e^{tA}||₁≤e^{-t/10}`.


Co więcej, po zadeklarowaniu miary równowagowej \(\pi=(4/5,1/5)\) dla części zachowującej masę, wybierzmy ważoną normę Hilberta
\[
\|v\|_{\pi^{-1},2}=\sqrt{v_1^2/(4/5)+v_2^2/(1/5)}=\|Wv\|_2,
\qquad W=\operatorname{diag}(\sqrt5/2,\sqrt5).
\]
Mamy wtedy
\[
WAW^{-1}=\begin{pmatrix}-11/10&2\\2&-41/10\end{pmatrix},
\qquad \mu_{\pi^{-1},2}(A)=\lambda_{\max}(WAW^{-1})=-\frac1{10}.
\]
Ta sama kinetyka jest więc kontraktywna w ważonej normie Hilberta (detailed balance), choć nie w zwykłej euklidesowej. Bezpośrednie obliczenia wartości własnych i podobieństwa sprawdzono dokładnie w SymPy, bez tolerancji numerycznych.


## 4. Dokładne poprawki sformułowania §A.6


- **RETAIN:** zastąpienie Lipschitza przez normę logarytmiczną jest poprawnym standardowym sposobem wzmocnienia oszacowania, jeżeli w **tej samej zadeklarowanej normie** zachodzi warunek jednostronny na wszystkich potrzebnych trajektoriach/odcinkach i funkcja µ(t) jest całkowalna.
- **REJECT_UNQUALIFIED:** „kinetyka jest dyssypatywna, więc µ<0”. Nawet stabilna, dodatnia, tracąca masę kinetyka może mieć µ₂>0.
- **REPAIR:** „W modelu, w którym generator jest dyssypatywny w określonej normie (np. konserwatywny/zanikowy generator Metzlera w normie \(\ell^1\), albo przy odpowiedniej symetryzacji z detailed balance w ważonej normie Hilberta), można otrzymać µ≤0 lub µ<0 i ostrzejszy certyfikat niż ze stałej Lipschitza. Znak µ należy obliczyć lub oszacować; nie wynika on z samej kinetycznej interpretacji równania.”
- **NORM_CHANGE_COST:** zmiana normy może poprawić µ, lecz także zmienia normę residualną `ε(t)=||η(t)||`, błąd początkowy oraz stałą Lipschitza celu. Nie wolno mieszać stałych z różnych norm, aby sztucznie wzmocnić (7.1').
- **SOURCE_NATIVE LIMIT:** dla nieliniowych/state-dependent układów BBN wymagany jest warunek jednostronny dla różnicy pól na rzeczywistym obszarze trajektorii. Wynik dla stałej macierzy 2×2 nie dowodzi kontraktywności rzeczywistej sieci BBN.


## 5. Oddzielenie od innych audytów


`NC_A1_LOGNORM_GROWTH_BOUND`: RETAIN_CONDITIONAL.  
`NC_A6_KINETICS_IMPLIES_MU_NEGATIVE`: REJECT_UNQUALIFIED.  
`STABLE_METZLER_WITH_DECAY_IMPLIES_MU2_NEGATIVE`: FALSE_EXACT_COUNTEREXAMPLE.  
`SAME_SYSTEM_MU1_NEGATIVE_AND_WEIGHTED_MU2_NEGATIVE`: PASS_EXACT.  
`NC_SHARPENING_B_QUANTITATIVE_COLLISION_BOUND`: already REJECTED by INT7; NOT NEW M13 result.  
`FRONTB_FULL_NETWORK_TARGET_ERROR`: NOT RUN / NOT CLAIMED.


### Źródła i bieżący stan


- NC pakiet zaostrzający, §A.6: https://docs.google.com/document/d/1D1RcNtP1OK24z_rTOIfmPohV0LhfONZ0/edit
- INT7 rozdzielny audyt §B, z wyraźnym wyłączeniem §A: https://docs.google.com/document/d/1dWXBOO4qKFQVS2qWC1nUxmfCpHMu6nFEtIKA3WT94R4/edit
- LT4 obecny rękopis rozdziału VII, Tw. 7.3: https://github.com/wmakiela-tech/Nash-iw-research/blob/d1b7da1f6485ca17a4d941a90db8329bd0fd5821/research/lt4/2026-10-15/lt4_monograph_ch7_fidelity_synthesis_working_20261015.md
- Standardowy gospodarz log normy: Dahlquist/Lozinskii 1958; Söderlind (2006), *BIT Numerical Mathematics* 46:631–652. Niniejszy wynik opiera się na jawnej algebrze, a nie na roszczeniu nowości.


**ROUTE_TAGS:** `IWTO_LT4 IWTO_MT13 IWTO_REC9 IWTO_INT7 IWTO_NC IWTO_PRF11 IWTO_MODERATOR`.


`REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_NEW_TASK`.