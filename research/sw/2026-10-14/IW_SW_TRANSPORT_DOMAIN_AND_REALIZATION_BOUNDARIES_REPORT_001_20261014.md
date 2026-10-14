---
artifact_id: IW_SW_TRANSPORT_DOMAIN_AND_REALIZATION_BOUNDARIES_REPORT_001_20261014
title: Dziedziny generatorów, podobieństwo realizacji i przygotowanie środowiska
revision: 1
created_at: 2026-10-14
as_of: 2026-10-14
origin_cell: SW
function: Analiza matematyczna granic transportu struktur
document_type: REPORT
task_id: SW-LT4-CHAPTER3-TRANSPORT-DOMAIN-AUDIT-001
exposure: PUBLIC
status: DRAFT
result_class: ANALYTIC_DERIVATION_WITH_EXPLICIT_COUNTEREXAMPLES
claim_ceiling: Standardowe mechanizmy i jawne dowody; bez deklaracji nowości, stabilności fizycznej ani równoważności teorii fizycznych.
archive_mode: PUBLIC_ARTIFACT
sync_state: GITHUB_PENDING_BW_INGEST
bw_ingestion_event_id: NOT_YET_INGESTED
primary_location: research/sw/2026-10-14/IW_SW_TRANSPORT_DOMAIN_AND_REALIZATION_BOUNDARIES_REPORT_001_20261014.md
content_sha256: EXTERNAL_MANIFEST_TO_AVOID_SELF_REFERENCE
provenance: Samodzielne rachunki i rekonstrukcje standardowych mechanizmów; źródła pierwotne w bibliografii.
derived_from: []
supersedes: []
stale_if: Błąd dowodu przy dokładnie zadeklarowanych dziedzinach i założeniach.
acceptance_owner: LT4
return_path: LT4
---

# Dziedziny generatorów, podobieństwo realizacji i przygotowanie środowiska

Trzy pozornie niewielkie zmiany założeń istotnie zmieniają możliwość transportu opisu: zastąpienie operatora ograniczonego generatorem nieograniczonym, zastąpienie minimalności skończenie wymiarowej minimalnością przybliżoną oraz zastąpienie przygotowania produktowego samym ustaleniem marginesu środowiska. Poniżej podajemy dokładne kontrprzykłady i zakresy prawidłowych wniosków. Dowody są analityczne; obcięcia numeryczne nie są ich przesłanką.

## 1. Niezmienniczość względem generatora nie wystarcza

Niech

\[
X=L^2(\mathbb R),\qquad (U(t)f)(x)=f(x+t),\qquad t\geq0.
\]

Jest to silnie ciągła półgrupa izometrii, będąca ograniczeniem grupy translacji. Jej generator to

\[
Lf=f',\qquad D(L)=H^1(\mathbb R),
\]

gdzie pochodna jest słaba. Niech

\[
K=\{f\in X:f=0\text{ p.w. na }(-\infty,0)\},
\qquad r:X\longrightarrow Y=L^2(-\infty,0)
\]

będzie operatorem ograniczenia. Wówczas \(r\) jest ograniczony i surjektywny, \(\ker r=K\), a \(K\) jest domknięte. Przestrzeń \(K\cap D(L)\) jest gęsta w \(K\), gdyż zawiera \(C_c^\infty(0,\infty)\). Jeżeli \(f\in K\cap H^1(\mathbb R)\), to również \(f'=0\) p.w. na ujemnej półosi. Zatem

\[
L(K\cap D(L))\subseteq K. \tag{1}
\]

Mimo to \(K\) nie jest niezmiennicze względem \(U(t)\). Weźmy

\[
f(x)=\begin{cases}
\sqrt{30}(x-1)(2-x),&1\leq x\leq2,\\
0,&\text{poza tym}.
\end{cases}
\]

Funkcja jest ciągła, kawałkami gładka, ma słabą pochodną w \(L^2\), więc należy do \(D(L)\cap K\). Ponieważ
\(\int_0^1 s^2(1-s)^2\,ds=1/30\), mamy \(\|f\|_2=1\). Tymczasem

\[
rf=0,\qquad \|rU(2)f\|_2=1. \tag{2}
\]

Dwa stany \(0,f\) mają ten sam obraz przez \(r\), lecz różne obrazy po czasie 2. Nie istnieje więc nawet dowolna funkcja \(V_2:Y\to Y\), dla której \(rU(2)=V_2r\) na całym \(X\).

### 1.1. Dokładna przeszkoda spektralna dla formalnego ilorazu

Warunek (1) pozwala zdefiniować liniowy operator na \(rD(L)\) przez

\[
A_0(rf)=rLf.
\]

Każdy element \(H^1(-\infty,0)\) ma przedłużenie w \(H^1(\mathbb R)\), np. przez odbicie. Dlatego

\[
D(A_0)=H^1(-\infty,0),\qquad A_0g=g', \tag{3}
\]

bez warunku brzegowego w zerze. Operator (3) jest gęsto określony i domknięty: zbieżność funkcji oraz ich słabych pochodnych w \(L^2\) zachowuje relację słabego różniczkowania.

Dla każdego rzeczywistego \(\lambda>0\) funkcja \(g_\lambda(x)=e^{\lambda x}\) należy do \(D(A_0)\) i spełnia

\[
A_0g_\lambda=\lambda g_\lambda.
\]

Widmo punktowe \(A_0\) zawiera całą dodatnią półoś. Generator półgrupy \(C_0\) ma natomiast resolwentę dla wszystkich dostatecznie dużych rzeczywistych \(\lambda\), wynikającą z oszacowania wykładniczego półgrupy. Zatem \(A_0\) **nie generuje** półgrupy \(C_0\). Sama domkniętość formalnego ilorazu także nie naprawia problemu.

Na poziomie pełnego generatora przeszkoda jest równie jawna. Dla \(\lambda>0\),

\[
(R(\lambda,L)f)(x)=\int_0^\infty e^{-\lambda t}f(x+t)\,dt.
\]

Dla wybranej dodatniej funkcji \(f\) i \(x<0\) jest to

\[
e^{\lambda x}\int_1^2 e^{-\lambda s}f(s)\,ds>0.
\]

Resolwenta nie zachowuje \(K\), chociaż (1) zachodzi.

### 1.2. Prawidłowy warunek dla ilorazu półgrupy

Niech teraz \(U(t)\) będzie dowolną półgrupą \(C_0\) na przestrzeni Banacha \(X\), z generatorem \(L\), a \(K\subset X\) domkniętą podprzestrzenią. Jeżeli

\[
U(t)K\subseteq K\quad\text{dla wszystkich }t\geq0,
\]

to na \(X/K\) istnieje półgrupa \(V(t)[x]=[U(t)x]\). Jej generator spełnia

\[
D(A)=qD(L),\qquad Aqx=qLx, \tag{4}
\]

gdzie \(q:X\to X/K\) jest mapą ilorazową. Wzór na dziedzinę wymaga dowodu odwrotnej inkluzji, nie tylko różniczkowania dla \(x\in D(L)\). Jeśli \(\lambda\) jest dostatecznie duże, całka Laplace’a daje
\(R(\lambda,A)q=qR(\lambda,L)\). Surjektywność \(q\) i równość \(D(A)=\operatorname{ran}R(\lambda,A)\) dają właśnie (4). Dla ograniczonej surjekcji \(r:X\to Y\) przenosimy ten wynik przez ograniczony izomorfizm \(X/K\simeq Y\).

Równoważnym testem jest zachowywanie \(K\) przez \(R(\lambda,L)\) dla wszystkich rzeczywistych \(\lambda\) większych od dostatecznie dużej stałej. W jedną stronę działa całka Laplace’a. W drugą: ograniczone aproksymanty Yosidy
\(L_\lambda=\lambda^2R(\lambda,L)-\lambda I\) zachowują \(K\), więc zachowują je ich eksponenty. Silna granica \(e^{tL_\lambda}x\to U(t)x\) oraz domkniętość \(K\) kończą argument.

Jest to standardowa teoria półgrup [1, II.1–II.3, zwłaszcza II.2.4]. Przykład (1)–(3) wskazuje konkretnie, co traci formalne różniczkowanie: informację o dopływie przez granicę ujemnej półosi.

## 2. Równa odpowiedź i minimalność przybliżona nie zapewniają ograniczonego podobieństwa

W obu realizacjach przyjmijmy przestrzeń stanu \(H=\ell^2(\mathbb N)\), skalarne wejście i wyjście oraz ograniczony generator

\[
De_n=-n^{-1}e_n.
\]

Definiujemy ograniczone mapy

\[
C_1u=(u/n)_{n\geq1},\qquad C_2u=(u/n^2)_{n\geq1},
\]

\[
B_1x=\sum_{n\geq1}\frac{x_n}{n^2},\qquad
B_2x=\sum_{n\geq1}\frac{x_n}{n}.
\]

Ograniczoność wynika z nierówności Cauchy’ego–Schwarza. Dla każdego \(t\geq0\) oba jądra odpowiedzi są identyczne:

\[
K_1(t)=B_1e^{tD}C_1
=\sum_{n\geq1}\frac{e^{-t/n}}{n^3}
=B_2e^{tD}C_2=K_2(t). \tag{5}
\]

Szereg jest bezwzględnie zbieżny. Także dla
\(z\in\rho(D)=\mathbb C\setminus(\{0\}\cup\{-1/n:n\geq1\})\)
obie funkcje przejścia wynoszą

\[
B_i(zI-D)^{-1}C_i=\sum_{n\geq1}\frac{n^{-3}}{z+1/n}. \tag{6}
\]

### 2.1. Minimalność w dokładnie zadeklarowanym sensie

Obie realizacje są przybliżenie osiągalne i obserwowalne w znaczeniu

\[
\overline{\operatorname{span}\{D^k C_i u:k\geq0,\ u\in\mathbb C\}}=H,
\qquad \bigcap_{k\geq0}\ker(B_iD^k)=\{0\}. \tag{7}
\]

Aby to wykazać, wystarczy prosty lemat momentowy. Jeżeli \(a\in\ell^1\) i
\(\sum_{n\geq1}a_n(-1/n)^k=0\) dla wszystkich \(k\geq0\), to \(a=0\).
Pomnożenie przez \((-1)^k\) i przejście do granicy \(k\to\infty\) daje \(a_1=0\). Jeśli już \(a_1=\cdots=a_{j-1}=0\), mnożymy przez \((-j)^k\). Dla \(n\geq j\) czynniki \((j/n)^k\) mają moduł co najwyżej 1, a dla \(n>j\) dążą do zera. Zbieżność zdominowana dla szeregu \(\ell^1\) daje \(a_j=0\). Indukcja kończy dowód.

Jeżeli \(z\) jest prostopadłe do przestrzeni osiągalnej, stosujemy lemat do
\(a_n=\overline{z_n}(C_i1)_n\in\ell^1\). Wszystkie współrzędne \(C_i1\) są niezerowe, więc \(z=0\). Dla obserwowalności stosujemy go do \(a_n=b_{i,n}x_n\), gdzie \(B_ix=\sum b_{i,n}x_n\); ponownie otrzymujemy \(x=0\).

Ponieważ \(D\) jest ograniczony, rozwinięcie \(e^{tD}\) jest analityczne. Warunki (7) są równoważne gęstości rozpiętości \(e^{tD}C_i u\), \(t\geq0\), i brakowi niezerowego stanu o \(B_ie^{tD}x=0\) dla każdego \(t\geq0\). Nie twierdzimy dokładnej sterowalności ani dolnego oszacowania obserwowalności.

### 2.2. Jedyny możliwy intertwiner nie ma ograniczonej odwrotności

Operator \(Se_n=n^{-1}e_n\) jest ograniczony, iniektywny i ma gęsty obraz. Spełnia

\[
DS=SD,\qquad C_2=SC_1,\qquad B_2S=B_1. \tag{8}
\]

Nie jest jednak izomorfizmem Banacha. Mamy \(\|Se_n\|=1/n\to0\); jego odwrotność na obrazie jest nieograniczona. Obraz jest właściwy: ciąg \((1/n)\in\ell^2\) nie jest obrazem żadnego elementu \(\ell^2\), gdyż wymagałby przeciwobrazu \((1,1,\ldots)\).

Nie można znaleźć innego ograniczonego izomorfizmu realizacji. Każdy ograniczony \(T\) z \(TD=DT\) zachowuje jednowymiarową przestrzeń własną odpowiadającą \(-1/n\), zatem \(Te_n=t_ne_n\). Z \(TC_1=C_2\) wynika \(t_n=1/n\) dla każdego \(n\). A więc \(T=S\), który nie ma ograniczonej odwrotności.

Przy każdym skończonym obcięciu do pierwszych \(N\) współrzędnych \(S_N\) jest odwracalne, ale

\[
\|S_N\|=1,\qquad \|S_N^{-1}\|=N.
\]

Brakuje jednostajnej kontroli przejścia do pełnej przestrzeni. Żaden zbiór dodatnich testów dla skończonych \(N\) nie usuwa tej dokładnej przeszkody.

### 2.3. Miejsce w teorii realizacji

Ball, Groenewald i ter Horst [2, tw. 1.5] rozróżniają w nieskończenie wymiarowej teorii dyskretnej minimalność przybliżoną, prowadzącą do pseudosimilarity, oraz silniejsze hipotezy pozwalające uzyskać ograniczone podobieństwo z ograniczoną odwrotnością. Nie stosujemy ich twierdzenia dyskretnego bezpośrednio do czasu ciągłego: (5)–(8) są własnym, kompletnym rachunkiem dla ograniczonego \(D\). To ilustracja znanej granicy teorii realizacji, bez deklaracji nowości.

Jeżeli ograniczony izomorfizm \(S\) spełniający (8) **jest założony**, równość odpowiedzi wynika natychmiast z szeregu wykładniczego. Błędem byłoby odwrócenie tej implikacji na podstawie samej (5) i przybliżonej minimalności.

## 3. Ustalony margines środowiska a legalny kanał lokalny

Niech \(H_A=H_B=\mathbb C^2\). Stany Bella

\[
|\Phi_\pm\rangle=(|00\rangle\pm|11\rangle)/\sqrt2,
\qquad \rho_\pm=|\Phi_\pm\rangle\langle\Phi_\pm|
\]

mają te same dwa marginesy:

\[
\operatorname{Tr}_B\rho_\pm=I_A/2,\qquad
\operatorname{Tr}_A\rho_\pm=I_B/2.
\]

Niech \(U\) będzie bramką CNOT z \(A\) jako kontrolą, tj.
\(U|a,b\rangle=|a,b\oplus a\rangle\). Wówczas

\[
U|\Phi_\pm\rangle=|\pm\rangle_A\otimes|0\rangle_B,
\]

zatem

\[
\operatorname{Tr}_B(U\rho_+U^*)=|+\rangle\langle+|,
\qquad
\operatorname{Tr}_B(U\rho_-U^*)=|-\rangle\langle-|. \tag{9}
\]

Na klasie obejmującej obydwa przygotowania nie istnieje nawet funkcja stanu lokalnego, która realizowałaby tę dynamikę. Ustalenie marginesu środowiska \(I_B/2\) nie ustala korelacji i nie wystarcza dla dowolnego oddziaływania.

### 3.1. Wystarczająca przesłanka produktowa

Dla ustalonego stanu \(\sigma_B\) i przygotowań
\(\rho_{AB}=\rho_A\otimes\sigma_B\) mapa

\[
\Phi_{U,\sigma_B}(X)=\operatorname{Tr}_B[U(X\otimes\sigma_B)U^*]
\tag{10}
\]

jest liniowym kanałem CPTP na całej algebrze operatorów wejścia. Rzeczywiście, jeśli
\(\sigma_B=\sum_j p_j|j\rangle\langle j|\), to dla bazy \((|k\rangle)\) środowiska

\[
K_{kj}=\sqrt{p_j}(I_A\otimes\langle k|)U(I_A\otimes|j\rangle),
\]

\[
\Phi_{U,\sigma_B}(X)=\sum_{k,j}K_{kj}XK_{kj}^*,\qquad
\sum_{k,j}K_{kj}^*K_{kj}=I_A.
\]

To standardowa konstrukcja kanału przez dylatację i ślad częściowy [3, §2.2]. Przygotowanie produktowe jest warunkiem wystarczającym, nie koniecznym dla każdej szczególnej interakcji.

W szczególności dla \(U=\mathrm{SWAP}\), przy identycznych wymiarach, wyjściowy stan \(A\) jest dokładnie wejściowym marginesem \(B\). Ustalenie \(\operatorname{Tr}_A\rho_{AB}=\sigma_B\) daje wtedy kanał stały \(\Phi(X)=\operatorname{Tr}(X)\sigma_B\), nawet jeśli dopuszczamy korelacje. Przykład (9) nie podważa tej własności SWAP; zabrania jej uogólniania na dowolne \(U\).

## 4. Dwie dodatkowe granice rachunku kompresji

### 4.1. Grupa a dodatni czas

Dla reprezentacji unitarnej grupy \(U(g)\) i izometrycznego włożenia \(J:M\to H\) połóżmy \(c(g)=J^*U(g)J\) i \(Q=I-JJ^*\). Zachodzi

\[
I_M-c(g)^*c(g)
=(QU(g)J)^*(QU(g)J). \tag{11}
\]

Jeżeli kompresja zachowuje wszystkie iloczyny grupowe, to
\(c(g)^*c(g)=c(g^{-1})c(g)=I_M\). Z (11) wynika \(QU(g)J=0\). Użycie także \(g^{-1}\) daje \(U(g)M=M\), a unitarność — niezmienniczość \(M^\perp\). Odwrotna implikacja jest bezpośrednia. Nie potrzeba tu żadnej topologii na grupie.

Ograniczenie do dodatnich czasów zmienia wniosek. Na \(\ell^2(\mathbb Z)\) niech \(Ve_n=e_{n+1}\), a \(M=\overline{\operatorname{span}}\{e_n:n\geq0\}\). Kompresje \(V^k\), \(k\geq0\), tworzą półgrupę jednostronnych przesunięć na \(M\), ale \(M^\perp\) nie jest niezmiennicze, ponieważ \(Ve_{-1}=e_0\). To nie jest kontrprzykład do twierdzenia grupowego: pokazuje rolę odwrotności.

### 4.2. Tożsamość trzech złożeń a kompleks kohomologiczny

Niech \(P\in\mathcal B(H,M)\), \(J\in\mathcal B(M,H)\), \(PJ=I_M\),
\(c(T)=PTJ\). Dla
\(\delta(S,T)=c(ST)-c(S)c(T)\) zachodzi

\[
\delta(ST,V)+\delta(S,T)c(V)
=\delta(S,TV)+c(S)\delta(T,V). \tag{12}
\]

Obie strony po rozwinięciu są równe \(c(STV)-c(S)c(T)c(V)\). Jednak działania przez \(c(S)\) nie muszą definiować bimodułu. Widać to na formalnych wzorach

\[
(d_ca)(S)=c(S)a-ac(S),
\]

\[
(d_c^2a)(S,T)=a\delta(S,T)-\delta(S,T)a. \tag{13}
\]

Dla \(H=\mathbb C^3\), \(M=\mathbb C^2\), standardowych \(P,J\),
\(S=E_{13}\), \(T=E_{32}\) i \(a=E_{11}\in\mathcal B(M)\) mamy
\(c(S)=c(T)=0\), \(\delta(S,T)=E_{12}\) oraz \(d_c^2a=E_{12}\ne0\).
Macierze \(E_{ij}\) oznaczają jednostki macierzowe w odpowiedniej przestrzeni.
Równość (12) sama nie tworzy więc zwykłego kompleksu Hochschilda ani jego klasy kohomologicznej.

## 5. Zakres wniosków

| Dane | Co wynika | Co nie wynika bez dalszych przesłanek |
|---|---|---|
| \(L(K\cap D(L))\subset K\), nawet z gęstym przecięciem | Formalny operator na \(qD(L)\) | Niezmienniczość półgrupy lub istnienie generatora ilorazowego |
| Niezmienniczość domkniętego \(K\) dla całej półgrupy \(C_0\) | Ilorazowa półgrupa i dziedzina (4) | Izomorfizm pełnych stanów |
| Równe jądra odpowiedzi oraz minimalność przybliżona | Nierozróżnialność tych odpowiedzi | Ograniczone podobieństwo realizacji z ograniczoną odwrotnością |
| Ustalony margines środowiska | Ograniczenie klasy przygotowań | Autonomiczny kanał lokalny dla dowolnego oddziaływania |
| Ustalona produktowa inicjalizacja środowiska | Kanał CPTP jednego kroku (10) | Półgrupowość lub brak pamięci przy kolejnych oddziaływaniach |
| Grupowa multiplicatywność ortogonalnej kompresji | Podprzestrzeń redukująca | Ten sam wniosek z samych dodatnich czasów |
| Tożsamość (12) | Zgodność algebraiczna trzech złożeń | Istnienie kohomologii lub nowego niezmiennika |

Są to granice standardowych konstrukcji. Nie identyfikują mikroskopowego nośnika fizycznego, nie dowodzą stabilności fizycznej i nie ustanawiają nowego prawa fizyki.

## Bibliografia i zakres użycia źródeł

1. K.-J. Engel, R. Nagel, *One-Parameter Semigroups for Linear Evolution Equations*, Springer, 2000. DOI: [10.1007/b97696](https://doi.org/10.1007/b97696). [Pełny tekst udostępniony przez uniwersytet](https://www.math.uni-tuebingen.de/de/forschung/agfa/members/engel-nagel_one-parameter-semigroups.pdf). Użyte: II.1.10 (resolwenta), II.2.1 (podobieństwo wraz z dziedziną), II.2.4 (iloraz), II.2.10 (translacje), II.3 (aproksymacja generatora). Rachunek dla konkretnej funkcji w §1 podano w całości.
2. J. A. Ball, G. J. Groenewald, S. ter Horst, *Standard versus Strict Bounded Real Lemma with Infinite-Dimensional State Space. I. The State-Space-Similarity Approach*, Journal of Operator Theory **80**(1), 225–253 (2018). DOI: [10.7900/jot.2017sep28.2175](https://doi.org/10.7900/jot.2017sep28.2175). [Pełny tekst wydawcy](https://www.theta.ro/jot/archive/2018-080-001/2018-080-001-012.pdf). Użyte: tw. 1.5, s. 231, dla umiejscowienia różnicy pomiędzy minimalnością przybliżoną a ograniczonym podobieństwem. Wynik źródłowy dotyczy czasu dyskretnego; przykład ciągły w §2 ma oddzielny dowód.
3. J. Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018. [Strona autora](https://cs.uwaterloo.ca/~watrous/TQI/); [rozdział 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf). Użyte: skończenie wymiarowe kanały, reprezentacja Krausa i dylatacje. Rachunek Bella–CNOT w §3 jest podany bez odwołania do niejawnych przesłanek.

Przeszukiwanie było celowane w trzy konkretne granice stosowalności. Nie jest przeglądem systematycznym ani podstawą twierdzenia o nowości.
