# IW/NASH — REC10 ROT31
## Zdarzeniowa utrata informacji w izometrycznym oscylatorze: dokładny wielopomiarowy warunek osiągania T1a NC ART029

**Data:** 2026-10-25 (CEST). **Komórka:** `IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10`.

**Werdykt:** `PASS_WITH_T1A_TIMING_REPAIR_AND_EXACT_MULTISHOT_DEFICIT`.

**Epistemic guard:** `NONBLIND / NO_NEW_TASK / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / OWNER_ACCEPTANCE_PENDING / BW_PENDING`.

## 1. Others-first: dokładne rozróżnienie autorstwa

1. **NC ART029**, po autokorekcie **NC ART031**, [źródło GitHub](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-24/IW_NC_OPN002_DYCHOTOMIA_MU2_I_BRAK_SKONCZONEGO_SUFITU_029_20261024.md), blob `c56c4894ead5bde09d5f3ce809d4d6b8c52d3825`: T1 `mu_2(G)<=0 ⇒ λ_max(W)<=m`, poprawny. Zdanie T1a, że sam oscylator izometryczny osiąga `sqrt(m)` **przy dowolnych czasach**, nie wynika z T1 i jest zbyt mocne. ART031 skorygował wcześniejsze duplikaty, bez merytorycznej zmiany nierówności T1.
2. **MT13**, `research/mt13/2026-10-24/mt13_nc029_arbitrary_dimension_projection_resource_visibility_audit_001.md`, [źródło GitHub](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-24/mt13_nc029_arbitrary_dimension_projection_resource_visibility_audit_001.md): **PRZED** ROT31 wykrył i opublikował konkretny kontrprzykład T1a, G obrót o 90°, m=2, kierunki e⊥d, wynik 1<2 dla kwadratu zysku. To MT13 ma pierwszeństwo dla faktu, że T1a jest fałszywe; ROT31 NIE zgłasza tego jako nowego wykrycia.
3. REC10 ROT31 — **dodatkowy zakres:** dokładna formuła zysku dla **każdego m i każdego szeregu odstępów czasu** w szczególnej podklasie 2D, warunek iff osiągania, dodatni deficyt rozpisany na wszystkie odstępy, jawna analiza skończonego u w m=2 oraz jednolita kontrola odległości od granicy u=0. Narzędzia: elementarne iloczyny rzutów, analiza Gramianu i podadditywność norm; dojrzały host matematyczny, brak nowości.

## 2. Źródłowy kontrakt, bez modyfikowania modelu NC

Bierzemy `G=ωJ`, `J=[[0,-1],[1,0]]`, `ω≠0` (ortogonalny przepływ `R(θ)=e^{Jθ}`), `e=(1,0)`, `d=(0,1)` i `D_d(u)=I-(1-u)dd^T=diag(1,u)` dla `0<=u<1`. NC definiuje

```
L1=R(ω t1),
L_(j+1)=R(ω(t_(j+1)-t_j)) D_d(u) L_j,
W_m(u)=Σ_(j=1)^m (1-u)^2 L_j^T e e^T L_j,
G_m(u)=sqrt(lambda_max(W_m(u)))
```

Nazwa `G_m(u)` to **wzmocnienie odczytu bez czynnika 1/γ**, nie macierz generatora G. Test źródłowy `u=0` oznacza **granicę idealnie silnego impulsu** (dla fizycznego `u=e^(-γs)` jest to granica `s→∞`). Parametry `e,d` to dwa niezależne kierunki; `e⊥d` jest warunkiem wąskiej analizowanej podklasy, nie wnioskiem ogólnym.

Nie ma tutaj kwantowego pomiaru na sprzęcie, PBH/BBN, DTC, grawitacji ani generalizacji na dowolne `G`.

## 3. Twierdzenie ROT31.1: pełna lista m czasów w granicy `u=0`

Niech `θ_k=ω(t_(k+1)-t_k)`, `k=1,...,m-1`. Definiuj `q_1=1`, `q_(j+1)=q_j cos² θ_j`.

**Twierdzenie:**

\[
\boxed{G_m(0)^2=\sum_{j=1}^m q_j
=\sum_{j=1}^m\prod_{k<j}\cos^2\theta_k.}
\]

**Dowód:** Ponieważ `D_d(0)=ee^T`, mnożenie szeregu daje dla `j>=1`

\[
e^TL_j=\left(\prod_{k=1}^{j-1}\cos\theta_k\right)e^TR(\omega t_1).
\]

Dla j=1 iloczyn pusty=1. Przez indukcję `e^TR(θ)ee^T=cos θ e^T`. Zatem **wszystkie wiersze obserwacji są współliniowe**, a Gramian ma rząd jeden:

\[
W_m(0)=\Big(\sum_j q_j\Big)R(\omega t_1)^T ee^TR(\omega t_1).
\]

Jedyna dodatnia wartość własna jest sumą w nawiasie. QED.

**Ostry warunek osiągania w tej klasie:** `G_m(0)=sqrt(m)` wtedy i tylko wtedy, gdy `|cos θ_k|=1` dla **każdego** k<m, czyli `θ_k∈πZ`. Jeżeli choć jedna pozycja nie spełnia tego warunku, drugi lub dalszy odczyt zostaje attenuowany, `G_m(0)<sqrt(m)`. Samo `R(t)` ortogonalne dla każdego t absolutnie nie wystarcza.

## 4. Twierdzenie ROT31.2: dokładny koszt wszystkich niedopasowanych odstępów

Ponieważ `q_j-q_(j+1)=q_j sin²θ_j`, przestawienie sum skończonych daje

\[
\boxed{
m-G_m(0)^2=\sum_{k=1}^{m-1}(m-k)\sin^2\theta_k
\prod_{\ell<k}\cos^2\theta_\ell\, .}
\]

Dowód: `m-Σ_j q_j =Σ_{j=1}^m (1-q_j)`, a `1-q_j=Σ_{k<j}(q_k-q_(k+1))`; zamiana sum wskazuje, że każdy ubytek na kroku k pojawia się w m-k przyszłych odczytach. QED.

**Wszystkie składniki deficytu są nieujemne.** Jeśli pierwszy krok jest ćwierćobrotem, `θ1=π/2`, to `q_(j>=2)=0` i `G_m(0)=1` **dla dowolnego m**, choć przepływ jest izometryczny. Jeśli wszystkie kroki są równe θ z `q=cos²θ<1`, to

\[
\boxed{G_m(0)^2=(1-q^m)/(1-q),\qquad
\lim_{m\to\infty}G_m(0)=1/|\sin\theta|.}
\]

Zatem powtarzane odczyty przy *stałym źle dobranym odstępie* nie zapewniają nawet nieograniczonego wzrostu zysku przy `m→∞` (dla θ niebędącego wielokrotnością π). Odmienny wynik `sqrt m` NC jest supremum **po harmonogramach**, nie uniformną wartością dla każdego harmonogramu.

## 5. Skończona siła impulsu: niezależny dokładny kontrtest i stabilność

Dla **m=2**, dowolnego `0<=u<1`, `t1=0` bez straty widma i `θ=ω(t2−t1)`, dokładny Gramian jest

\[
W_2(u)=(1-u)^2\begin{pmatrix}
1+\cos^2\theta&-u\cos\theta\sin\theta\\
-u\cos\theta\sin\theta&u^2\sin^2\theta
\end{pmatrix}.
\]

Wartości własne wynikają z `tr W/(1-u)^2=L=1+cos²θ+u²sin²θ`, `det W/(1-u)^4=u²sin²θ`. Szczególnie:

\[
\boxed{G_2(u;\theta=\pi/2)=1-u,\quad
G_2(u;\theta=\pi)=\sqrt2(1-u).}
\]

Jest to **dokładna falsyfikacja nadmiernego kwantyfikatora NC T1a także przy każdym skończonym `0<u<1`**, a nie wyłącznie w idealnej granicy. Wersja MT13 `u→0` to szczególny przypadek.

Dla dowolnego m i harmonogramu obowiązuje bezpieczna kontrola

\[
|G_m(u)-G_m(0)|\leq u\sqrt{\sum_{j=1}^m j^2}
=u\sqrt{m(m+1)(2m+1)/6}.
\]

**Dowód:** `||D_d(u)-D_d(0)||=u`, rotacje mają normę 1. Teleskopowanie iloczynu m-1 impulsów daje `||L_j(u)-L_j(0)||<= (j-1)u`; prefaktor odczytu `(1-u)` dodaje najwyżej u. Różnica każdego wiersza obserwacyjnego ma normę najwyżej `j u`. Operatorowa norma macierzy wierszy jest lipschitzowska względem jej normy Frobeniusa. QED. To konserwatywna kontrola skończonego u, nie ostre optimum parametru.

Dla każdego `0<u<1` T1 źródłowy poprawia się dla tego stałego parametru do `G_m(u)<=(1-u)sqrt(m)` (nierówność ostra względem źródłowego `sqrt m`). Równość `(1-u)sqrt m` jest osiągalna np. przy wszystkich `θ_k∈πZ` i `e⊥d`.

## 6. Executed falsifiers — odrębne od dowodu

Samodzielny kod `rec10_rot31_nc_t1a_timing_repro.py` bez importowania programów NC/MT13 korzysta **bezpośrednio z definicji macierzy L_j/W_m NC**, a osobno z analitycznych iloczynów cosinusów i deficytu. NumPy/SymPy, zamrożony seed `20261025`:

- `1000/1000` niezależnych harmonogramów (m=2..20, różne t1 i fazy): maksymalna różnica kwadratu zysku z bezpośrednim diagonalizowaniem W: `3.552713678800501e-15` — PASS.
- `1000/1000` kontroli tożsamości deficytu: max `7.105427357601002e-15` — PASS.
- `1000/1000` losowych skończonych u w `(0,1)` i kontrola stałej lipschitzowskiej: PASS; największy stosunek do ograniczenia `0.6324480282`.
- `6/6` kontroli m=2 przy `u in {0,1e−12,.1,.4,.8,.999}`: dokładne granice ćwierćobrotu i półobrotu PASS.
- `39` testów całkowitego wyrównania do m=40, `39` testów pierwszego ćwierćobrotu, `20` testów sumy geometrycznej oraz samodzielny symboliczny determinant 2x2 — PASS.

| Harmonogram, m=8, idealne u=0 | Wzmocnienie `G_m(0)` | `G_m(0)^2` |
|---|---:|---:|
| Wszystkie fazy π | 2.828427124746 | 8 |
| Pierwsza faza π/2 (reszta dowolna) | 1 | 1 |
| Każda faza π/8 | 2.214632982597 | 4.904599247605 |
| Na przemian π/3 i π/6, ostatnia π/4 | 1.240245140209 | 1.538208007813 |

Status `DIRECT_SOURCE_GRAMIAN_REPRO_PASS / QUANTIFIER_REPAIR_PASS`. Oryginalne skrypty NC nie są potrzebne do sprawdzenia definicji T1a, ale niezależność wyliczeń nie jest zaślepioną próbą (pełny raport NC i MT13 został przeczytany przed kodem).

## 7. Dyspozycja recenzencka, nie moderatorska

- **T1 NC ART029 = PASS**. Górna granica `sqrt(m)` dla `mu_2<=0` stoi; MT13 prawidłowo rozszerzył jej nD kontekst.
- **T1a NC ART029 = ERRATUM_REQUIRED**: sama izometryczność przy arbitralnych czasach **nie** wystarcza. MT13 ma pierwszeństwo odkrycia, a REC10 ROT31 dostarcza dokładny wielopomiarowy koszt i warunek harmonogramu dla źródłowego oscylatora.
- **NC-OPN-002** można rekomendować jako `ANSWERED_WITH_T1A_SCOPE_REPAIR`: pytanie o jedną uniwersalną skończoną stałą w nieograniczonej liczbie pomiarów jest źle postawione; NC prawidłowo ustanowił dychotomię przy `mu_2=0` w zadanej klasie wolnych impulsów i harmonogramów. Decyzja `CLOSED`, zmiana wiersza i EXEC pozostają u Moderatora.
- **Granice:** tylko źródłowy liniowy funkcjonał gramianowy i szczególny 2D oscillator z `e⊥d`, bez nowego modelu kwantowego, nowej obserwabli, sprzętu, BBN, GR ani transferu do DTC/FrontB.

**Prior art:** standardowe iloczyny rzutów, izometrie 2D, macierze Grama i normy operatorowe. Nie zgłasza się nowości ani oryginalności publikacyjnej.

**STATUS:** `PASS_WITH_T1A_TIMING_REPAIR_AND_EXACT_MULTISHOT_DEFICIT / REPRO_PASS / NONBLIND / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / BW_PENDING / OWNER_ADOPTION_PENDING`.