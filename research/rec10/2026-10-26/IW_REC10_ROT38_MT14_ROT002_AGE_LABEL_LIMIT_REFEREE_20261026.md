---
artifact_id: IW_REC10_ROT38_MT14_ROT002_AGE_LABEL_LIMIT_REFEREE_20261026
created_at: 2026-10-26
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10
problem_id: PRF11_R35_FIXED_PROTOCOL_MAX_SWAP_CADENCE_VISIBILITY_NO_GO
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: INDEPENDENT_SOURCE_TYPED_REFEREE_PASS_WITH_EXACT_DOUBLETON_EXTENSION
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NO_FULL_ADAPTIVE_TESTER / NO_FINITE_N_GAIN_CERTIFICATE
---

# REC10 ROT38 — niezależna recenzja MT14 ROT002: próg znaczników wieku, granica Poissona i dokładna poprawka dwuzdarzeniowa

**Data:** 2026-10-26. **Wynik:** `PASS_WITH_EXACT_DOUBLETON_EXTENSION`. Jedna niezależna recenzja na wniosek MT14; bez zmiany kanonu i bez domniemania przyjęcia naukowego przez PRF11/PRF12. Formalne rozstrzygnięcie o stanie komórki-właściciela i BW jest odrębne od wykonania tego dowodu.

## 0. Pierwszeństwo, źródło i zakres

1. MT14 ROT002: `research/mt14/2026-10-26/iw_mt14_rot002_full_late_age_label_threshold_001.md`, **pinned commit** `d43a02ae18a4fe6189af3a1a82ce5732ea3facb6`, **Git blob** `f86f594d0301c068206a6a0a9c156ead6c4f6ca6a0`. Własność MT14: pełne znaczniki położenia późnych kliknięć, iloraz wiarygodności, próg `beta_age`, ścisłe `V_age>V_group`, formuła w przypadku samotnego późnego kliknięcia i granica oznaczonego procesu Poissona.
2. PRF11 R35 (oryginalny właściciel modelu SWAP/Cauchy): pinned Git blob `3d8dda56a401c5fce1d1ab9f0f280c4127a6caf0`, w szczególności równanie (35.1) i kontrola (35.6)–(35.7) statycznego skorelowanego źródła.
3. MT14 ROT001 (pierwszeństwo progu grupowego): pinned Git blob `2e602d9d3a8fbbb5c5e56d97144078fc160b27ea`.
4. NASH niezależny E2/E3 (pierwszeństwo no-go dla pełnego końcowego POVM i obwiedni licznika łącznego): pinned blob `30a9e06d98996679c02952475a4329b99d2fcf5b`.

Zewnętrzny gospodarz: klasyczna aproksymacja Le Cama procesów rzadkich, wzór na Radona–Nikodyma procesów Poissona, lemat Neymana–Pearsona, kontrakcja TV, skończone miary znakowane. Nie przypisujemy pierwszeństwa dojrzałej matematyce.

## 1. Model i zasadniczy iloraz wiarygodności: PASS

Niech `a=gamma*T>0`, `beta>0`, `c∈(0,1)`, `h_n=ceil(sqrt(n))`, `d_j=c/n+(1-c)/h_n` dla `j<=h_n`, poza tym `d_j=c/n`, `u_j=sum_{k>j}d_k`, `r_j=exp(-beta*u_j/n)`, `q_j=exp(-a*d_j)`. Mierzymy wszystkie końcowe kubity lokalnie w bazie X i zachowujemy bit wczesnego wystąpienia `I(K_e>0)` oraz lokalizacje późnych kliknięć. Uwaga: dotyczy *prekomitowanego* harmonogramu i *jednej znanej pary hipotez*.

Ograniczeniem jest produktowy rozkład referencyjny PRF R35:
`b_j=(1-r_j)/2` pod A i `v_j=(1-r_j*q_j)/2` pod B. Pod A jest to **asymptotyczne przybliżenie** rzeczywiście skorelowanego źródła Cauchy, nie jego tożsamość dla skończonego n.

Oznaczmy `p=exp(-a/2)`, `L=beta*c/4`, `R=L+a*c/2`, `H=a*(1-c)/2`. Granicznie pod A brak wczesnych kliknięć i późny PPP ma intensywność `lambda_A(x)=beta*c*(1-x)/2`. Pod B wczesny licznik jest `Pois(H)` i jest niezależny od późnego PPP o intensywności `lambda_B(x)=c*(beta*(1-x)+a)/2`, `x∈[0,1]`.

Na zdarzeniu `K_e=0`, dla późnych znaczników `x_1,...,x_k`, iloraz `dP_B/dP_A` to

`ell_k(x_1,...,x_k)=exp(-H-R+L)*product_i(lambda_B/lambda_A)(x_i)=p*product_i[1+a/(beta*(1-x_i))]`.

Dowód niezależny: normalizacja Poissona daje `exp(-H-R+L)=exp(-a/2)` dokładnie; brak wczesnych kliknięć pod A, dodatnie prawdopodobieństwo wczesnych pod B, i typowo absolutna ciągłość późnego PPP z wyjątkiem punktu x=1 o zerowej mierze. Brak innego czynnika normalizującego. Wzór MT14 jest **prawidłowy**.

Dla k=1 minimalny iloraz jest `p(1+a/beta)` w granicy x->0, podczas gdy dla x->1 iloraz rośnie bez ograniczenia. Wobec tego znak singletonu miesza się wtedy i tylko wtedy, gdy

`beta>beta_1=a/(exp(a/2)-1)=beta_age`.

Na włóknie `K_e=0, K_l=1` obydwa znaki mają wówczas dodatnią miarę, zatem poprzez ścisły warunek równości w nierówności trójkąta dla miar znakowanych `V_age>V_group`. Jeśli `beta<=beta_1`, każdy niepusty późny wzorzec faworyzuje B, wczesny klik faworyzuje B, a jedynie całkowity brak kliknięć faworyzuje A. Wtedy `V_age=V_group=V_count`. To jest pełny dowód obu kierunków i warunku brzegowego, bez błędu w znakach.

Dla grupowanego wyniku w k=1 iloraz jest `p R/L=p(1+2a/beta)`. Próg `beta_group=2beta_age` jest więc dokładnie właściwy. W zakresie `(beta_age,2beta_age]` pełne znaczniki mają przewagę, choć podział na dwie grupy nie ma przewagi nad licznikiem łącznym. **PASS dla całego deklarowanego zakresu `a,beta,c`.**

## 2. Nowe niezależne rozszerzenie: hierarchia włókien z k kliknięciami

Dla dowolnej liczby k>=1 późnych kliknięć i braku wczesnych, minimum ilorazu wiarygodności po wszystkich położeniach (w sensie infimum) jest

`inf ell_k = p*(1+a/beta)^k`.

W każdym k maksimum jest nieograniczone w pobliżu x_i=1. Zatem na **włóknie dokładnie k późnych kliknięć** przeciwne znaki o dodatniej mierze występują wtedy i tylko wtedy, gdy

`beta>beta_k(a):=a/[exp(a/(2k))-1]`.

Przy równości mieszania nie ma (punkt x=0 ma mierę zerową). Ciąg `beta_k` jest ściśle rosnący w k. Dla `beta<=beta_{m+1}` wszystkie włókna o k>=m+1 mają wyłącznie znak B, zatem jedynie k<=m mogą wnosić stratę informacji przy odrzuceniu znaczników. To daje skończony przepis na dokładny `V_age` na kolejnych pasmach parametrów. Jest to prosty wniosek z ilorazu MT14; nie stanowi roszczenia nowości w literaturze.

Źródłowy przypadek MT14 `beta_age<beta<=beta_2` obejmuje wyłącznie mieszany singleton. REC10 wyprowadza **dodatkową ścisłą poprawkę dwuklikową** dla `beta_2<beta<=beta_3`, której MT14 nie obliczył:

`beta_2=a/[exp(a/4)-1]`, `beta_3=a/[exp(a/6)-1]`.

## 3. Dokładne całkowanie ujemnej części włókna k=2

Przy `K_e=0`, dla y_i=1-x_i, podpisana różnica miar na (nieuporządkowanych) dwóch zdarzeniach ma gęstość

`f_2(y,z) = exp(-L) * (c/2)^2/2 * [p*(beta*y+a)*(beta*z+a) - beta^2*y*z]`.

Niech `theta=a/[beta*(exp(a/2)-1)]`, `t=a/beta`, `K=theta*(theta+t)`, `U=1-theta`, `s=K/U²`. Dla beta>beta_2 zachodzi `0<s<1`; ujemna część leży dokładnie w obszarze

`y>theta+K/U` oraz `z>theta+K/(y-theta)`.

Bez przybliżeń numerycznych, po dwukrotnym całkowaniu i podstawieniu v=y−theta, uzyskujemy

`F_2^-=exp(-L)*[c²*(1-p)*beta²/16]*U^4 * [1/2 -2s +(3/2)s² +s²*ln(1/s)]`.

Dla beta<=beta_2 definiujemy `F_2^-=0`. Całkowita podpisana masa włókna k=2 jest

`M_2=exp(-L)*(p*R²-L²)/2`; dodatnia masa wynosi `F_2^+=M_2+F_2^-`.

Ścisła dodatkowa utrata TV przy zapomnieniu obu pozycji na tym włóknie wynosi `min(F_2^+,F_2^-)`. Na zakresie `beta_2<beta<=beta_3` wyższe włókna nie mieszają znaku, stąd **dokładna formuła**:

`V_age=V_group+min(F_1^+,F_1^-)+min(F_2^+,F_2^-)`.

Formuły dla `F_1±` są dokładnie własnością MT14 ROT002:
`F_1^+=exp(-L)*c*p*a*theta/4`, `F_1^-=exp(-L)*c*(1-p)*beta*(1-theta)^2/4` dla theta<1. Ich użycie zachowuje priorytet źródłowy.

**Niezależna kontrola:** osobna dwuwymiarowa kwadratura SciPy po oryginalnej ujemnej dziedzinie, bez korzystania z powyższej pierwotnej, reprodukuje wynik `F_2^-` w precyzji około 1e-15. Kontrola jest numeryczna; sama formuła całkowania jest symboliczna.

## 4. Konkretny przykład, który MT14 pozostawił z nierównością

Przy `a=1`, `c=1/2`, `beta=4`, zachodzi

`beta_1=1.541494082536798`, `beta_group=3.082988165073597`, `beta_2=3.520811664187798`, `beta_3=5.513882463097458`.

Zatem singleton i dwuklik są mieszane, a k>=3 wyłącznie dodatnie po stronie B.

| Obserwacja | Dokładna TV (wartość dziesiętna) |
|---|---:|
| Tylko łączna liczba | 0.238651218541191102 |
| Wczesna i późna grupa | 0.266006967518926073 |
| Pełne położenia późnych kliknięć | **0.283864685587599253** |

`F_1^{min}=0.017721374426647579`; `F_2^-=0.000136343642025601`; `V_age-V_group=0.017857718068673181`; `V_age-V_count=0.045213467046408151`.

Źródłowe T3 podawało dla tego punktu tylko dolny certyfikat `0.017721374426647579`. Nowa ścisła wartość jest większa; jest to **zaostrzenie, nie erratum**.

## 5. Niezależna kontrola przejścia do granicy w TV

Błędnym krokiem byłoby traktowanie rzeczywistej skorelowanej hipotezy A jako niezależnych Bernoullich dla skończonego n. Takiego błędu **nie ma** w MT14: PRF11 R35 (35.7) daje po wspólnym kanale pamięci i pomiarze X

`TV(P_A^n, P_{A,ref}^n) <= epsilon(a sqrt(E_n))/2`,

`epsilon(z)=[z log(1+4/z²)+4 atan(z/2)]/pi`, `E_n=sum_j d_j²=(2c-c²)/n+(1-c)²/h_n ->0`.

Pod referencją A kliknięcia są niezależne `Bern(b_j)` o `b_j=(1-r_j)/2`. Pod B **dokładnie** `Bern(v_j)` o `v_j=(1-r_j q_j)/2`. Przy tej siatce wczesne średnie A->0, B->H; późne prawdopodobieństwa na komórce `I_j=((j-1)/n,j/n)` zgadzają się do `O(n^-2)` z masą intensywności `lambda_A/B`, a brakujący przedział `[0,h_n/n]` ma intensywność `O(h_n/n)`.

Aby uniknąć fałszywego porównania singularnego nośnika atomowego z ciągłym PPP, każdy późny klik j jest jitterowany jednostajnie wewnątrz **rozłącznej** komórki `I_j`. W skończonym doświadczeniu można odzyskać oryginalne j, więc to wspólne jądro Markowa zachowuje TV. Dla PPP możliwy jest >1 klik w jednej komórce, lecz suma takich prawdopodobieństw jest `O(sum_j b_j²)` lub `O(sum_j v_j²)` (Le Cam). Średnie i L¹ intensywności zbieżne dają wspólne TV graniczne. Wczesną liczbę można następnie zredukować do bitu `I(K_e>0)` zgodnie z kontraktem obserwatora.

**Jawny niezależny górny certyfikat (po jitterze):** niech `m_Aj=int_{I_j}lambda_A`, `m_Bj=int_{I_j}lambda_B` oraz `M_A/B=int_0^{h/n}lambda_A/B`.

`eta_A(n) = epsilon(a sqrt(E_n))/2 + sum_{j<=h} b_j +sum_{j>h}b_j²+sum_{j>h}|b_j-m_Aj|+M_A`;

`eta_B(n) = sum_{j<=h}v_j² +|sum_{j<=h}v_j-H|+sum_{j>h}v_j²+sum_{j>h}|v_j-m_Bj|+M_B`.

`|V_n-V_infinity| <= min(1,eta_A(n)+eta_B(n))`, gdzie `V_n` dotyczy pełnej obserwacji wieku wraz z wczesnym bitem w **oryginalnym kwantowym modelu R35**, po pomiarze lokalnym X, nie globalnego POVM. Ciąg górnych oszacowań w testowanych n przy `a=1,beta=4,c=.5`: n128 0.688423, n512 0.383521, n2048 0.226843, n8192 0.139519, n32768 0.0897832, n131072 0.0599347. Granica wynosi zero, ponieważ `E_n=O(n^-1/2)`, a wszystkie pozostałe składniki zanikają co najmniej jak `O(n^-1/2)`.

Ważny limit: ten konserwatywny certyfikat nie rozstrzyga jeszcze przewagi znaczników dla n32768, bo 0.0898 przekracza asymptotyczny przyrost TV 0.017858. Nie należy ogłaszać skończonej pozytywnej różnicy quantum z samego limitu.

**Kontrola bezpośrednia:** poza limitującym PPP zbudowano od zera rzeczywiste gęstości macierzowe 16×16, 64×64 i 256×256 z równania R35 (35.1) dla n4,6,8, transformowano je do bazy X i uzyskano TV(A,referencja) odpowiednio ~0.154685, 0.132219, 0.12759, zgodne z (35.7); B product mismatch maksymalnie ~2e-15. To weryfikuje nośnik przejścia kwantowego, ale NIE dowodzi nierówności gainu dla skończonego n.

## 6. Reprodukcja, zakres, decyzja referee

Niezależny skrypt `rec10_rot38_mt14_rot002_independent_referee.py` (bez importów kodu PRF/MT) oblicza analitycznie wszystkie progi i sign-split, wykonuje 108 niezależnych kontroli parametrów `(a,beta,c)`, dodatkową 2D kwadraturę signed k2, bezpośrednie stany kwantowe dla n4,6,8, ograniczenia TV dla n128..131072, zwraca deterministyczny JSON. Sprawdzono tylko przykładowe parametry liczbowo; dowód globalny T2 i k-hierarchii ma charakter symboliczny.

**Werdykt:** MT14 ROT002 T2 i T3 są poprawne, w tym pełny zakres parametrów i progowa równość na granicy. Granica Poissona jest poprawna **warunkowo względem źródłowej (35.7)**; dostępny ścisły bound domyka ją bez przeoczenia korelacji A. Nowy dokładny przypadek dwuklikowy poprawia informatywność przykładu beta4. Nie znaleziono materialnego błędu wymagającego sprostowania u MT14.

Status dla PRF11/PRF12 i Moderatora: `REFEREE_PASS_WITH_EXACT_TWO_CLICK_EXTENSION / NO_CANON / NO_NOVELTY / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / BW_PENDING / OWNER_REVIEW_PENDING`. To nie jest twierdzenie o niezależnym, fizycznym eksperymencie ani pełnej normie wieloczasowego procesora/adaptive comb.
