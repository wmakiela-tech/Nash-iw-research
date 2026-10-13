---
artifact_id: IW_SW_TARGET_FACTORIZATION_AND_CONDITIONAL_STABILITY_REPORT_001_20261013
title: Faktoryzacja obserwabli i stabilność warunkowa na dopuszczalnej klasie stanów
revision: 1
created_at: 2026-10-13T10:41:00Z
as_of: 2026-10-13
origin_cell: SW
function: Samodzielna analiza matematyczna granic odtwarzania obserwabli
document_type: REPORT
task_id: SW-LT4-CHAPTER2-TARGET-FACTOR-CONTINUITY-REVIEW-001
exposure: PUBLIC
status: DRAFT
result_class: ANALYTIC_DERIVATION_WITH_EXPLICIT_DOMAIN
claim_ceiling: Standardowa matematyka i jawne przykłady; bez twierdzenia o nowości, stabilności fizycznej ani równoważności modeli fizycznych.
archive_mode: PUBLIC_ARTIFACT
sync_state: GITHUB_PENDING_BW_INGEST
bw_ingestion_event_id: NOT_YET_INGESTED
primary_location: research/sw/2026-10-13/IW_SW_TARGET_FACTORIZATION_AND_CONDITIONAL_STABILITY_REPORT_001_20261013.md
content_sha256: EXTERNAL_MANIFEST_TO_AVOID_SELF_REFERENCE
provenance: Własne wyprowadzenia analityczne; standardowe podstawy wskazane w bibliografii.
derived_from: []
supersedes: []
stale_if: Kontrprzykład do podanych tez przy tych samych założeniach.
acceptance_owner: LT4
return_path: LT4
---

# Faktoryzacja obserwabli i stabilność warunkowa

Jednoznaczność celu na włóknach pomiaru, ciągłość jego odtworzenia i odporność na błąd danych są różnymi własnościami. Poniższe wyprowadzenia określają dokładne warunki ich rozdzielenia. Najbardziej pouczający przykład wykorzystuje tę samą parę operatorów na dwóch klasach źródeł: globalnie każde dodatnie zaburzenie danych dopuszcza nieograniczony błąd celu, a na ustalonej kuli źródeł odtworzenie celu ma optymalny wykładnik Höldera \(1/2\).

Wynik jest analityczny. Nie zależy od dyskretyzacji ani od testów numerycznych. Opisuje klasyczny mechanizm stabilności warunkowej; nie jest deklaracją odkrycia nowej teorii.

## 1. Faktoryzacja przez obraz pomiaru

Niech \(X\ne\varnothing\) będzie zbiorem, a \(r:X\to Y\) i \(\tau:X\to Z\) odwzorowaniami. Istnieje jednoznaczna mapa \(\bar\tau:r(X)\to Z\) taka, że \(\tau=\bar\tau r\), dokładnie wtedy, gdy

\[
r(x)=r(x')\ \Longrightarrow\ \tau(x)=\tau(x').
\]

Dowód polega na definicji \(\bar\tau(r(x))=\tau(x)\). Warunek zapewnia niezależność od reprezentanta. Nie ustanawia ciągłości. Jeśli przestrzenie są topologiczne, \(r:X\to r(X)\) jest mapą ilorazową, a \(\tau\) ciągłą, to definicja topologii ilorazowej daje ciągłość \(\bar\tau\). Topologia na obrazie musi być zadeklarowana; nie wolno automatycznie zastępować jej inną topologią.

Ta sama zasada działa dla półgrupy algebraicznej \((U_t)_{t\ge0}\) na \(X\). Istnieje półgrupa \((V_t)\) na \(r(X)\) spełniająca \(rU_t=V_tr\), jeżeli i tylko jeżeli każde \(rU_t\) jest stałe na włóknach \(r\). Istotnie,

\[
V_{t+s}(r(x))=r(U_tU_sx)=V_tV_s(r(x)),\qquad V_0=\mathrm{id}.
\]

Nie potrzeba do tego liniowości ani topologii. Ciągłość każdej mapy \(V_t\) nie jest jeszcze wspólną ciągłością \((t,y)\mapsto V_t(y)\). Odtwarzalność \(\tau U_t=g_tr\) dla poszczególnych czasów również nie czyni \(g_t:r(X)\to Z\) półgrupą. Autonomia samego celu wymaga stałości \(\tau U_t\) na włóknach \(\tau\).

## 2. Dokładne kryterium ograniczonej faktoryzacji

Niech \(X,Y,Z\) będą przestrzeniami Banacha, \(P\in\mathcal B(X,Y)\), \(T\in\mathcal B(X,Z)\). Domknięcie obrazu liczymy w normie \(Y\).

**Twierdzenie.** Istnieje ograniczony operator liniowy

\[
S:\overline{\operatorname{ran}P}\longrightarrow Z,\qquad T=SP,
\]

wtedy i tylko wtedy, gdy istnieje \(C<\infty\) takie, że

\[
\|Tx\|_Z\le C\|Px\|_Y\quad\text{dla wszystkich }x\in X. \tag{1}
\]

Taki \(S\) jest jednoznaczny. Jeżeli \(\operatorname{ran}P\) jest domknięty, wystarcza \(\ker P\subseteq\ker T\).

**Dowód.** Z \(T=SP\) wynika (1) z \(C=\|S\|\). Odwrotnie (1) implikuje zawieranie jąder. Definicja \(S_0(Px)=Tx\) jest więc jednoznaczna, liniowa i ograniczona na \(\operatorname{ran}P\). Jeżeli \(y_n\in\operatorname{ran}P\) zbiega do \(y\) w normie \(Y\), to

\[
\|S_0y_n-S_0y_m\|_Z\le C\|y_n-y_m\|_Y.
\]

Zupełność **przeciwdziedziny \(Z\)** zapewnia granicę \(S_0y_n\). Ta sama nierówność dowodzi niezależności granicy od przybliżającego ciągu oraz ograniczoności przedłużenia. Jednoznaczność wynika z gęstości obrazu.

W przypadku domkniętego obrazu połóżmy \(N=\ker P\). Jest to domknięta podprzestrzeń, a \(X/N\) ma normę

\[
\|[x]\|_{X/N}=\inf_{n\in N}\|x+n\|_X.
\]

Operatory indukowane

\[
\widetilde P[x]=Px,\qquad \widetilde T[x]=Tx
\]

są dobrze określone. Dla każdego \(n\in N\), \(T(x+n)=Tx\), zatem

\[
\|\widetilde T[x]\|\le\|T\|\inf_{n\in N}\|x+n\|
=\|T\|\|[x]\|_{X/N}.
\]

Analogicznie \(\widetilde P\) jest ograniczony. Jest bijekcją z Banacha \(X/N\) na Banacha \(\operatorname{ran}P\). Twierdzenie o ograniczonym operatorze odwrotnym daje ograniczoność \(\widetilde P^{-1}\) [1, 2]. W konsekwencji

\[
S_0=\widetilde T\widetilde P^{-1},\qquad
\|S_0\|\le\|T\|\,\|\widetilde P^{-1}\|.
\]

To kończy dowód. \(\square\)

Dziedziną twierdzenia jest **domknięcie obrazu**, nie całe \(Y\). Nie ma tu kroku przedłużającego dowolny operator o wartościach w Banachu na całe \(Y\). Jeśli domknięcie obrazu ma ograniczoną projekcję \(\Pi\), można użyć \(S\Pi\); w szczególności jest tak dla przestrzeni Hilberta \(Y\). Poza domknięciem obrazu przedłużenie nie musi być jednoznaczne. Gdy \(X,Y,Z\) są Hilbertami, (1) jest po prostu równoważne \(T^*T\le C^2P^*P\), ponieważ obie nierówności mają identyczne formy kwadratowe.

## 3. Para diagonalna: trzy różne odpowiedzi na pytanie o stabilność

Weźmy \(X=Y=Z=\ell^2(\mathbb N)\), z indeksami \(n=1,2,\ldots\), oraz

\[
Pe_n=n^{-1}e_n,\qquad Te_n=n^{-1/2}e_n. \tag{2}
\]

Oba operatory są ograniczone i różnowartościowe. Obraz \(P\) zawiera wszystkie ciągi o skończonym nośniku, więc jest gęsty. Nie jest domknięty: ciąg \(y=(1/n)\) należy do \(\ell^2\), ale jego jedyny formalny przeciwobraz to \((1,1,\ldots)\notin\ell^2\).

### 3.1. Cel jest jednoznaczny, lecz jego liniowy transport nieograniczony

Na \(\operatorname{ran}P\) istnieje jednoznaczny liniowy czynnik \(S_0(Px)=Tx\), dany współrzędnie przez \((S_0y)_n=\sqrt n\,y_n\). Dla \(x_n=\sqrt n\,e_n\) zachodzi

\[
\|Px_n\|=n^{-1/2}\longrightarrow0,\qquad \|Tx_n\|=1.
\]

Nie istnieje ograniczony czynnik na \(\overline{\operatorname{ran}P}=\ell^2\). To dokładny kontrprzykład dla implikacji „zawieranie jąder daje ograniczoną faktoryzację” bez warunku domkniętego obrazu albo oszacowania (1).

### 3.2. Globalny moduł celu jest nieskończony

Dla dowolnej klasy źródeł \(K\subseteq\ell^2\), \(K\ne\varnothing\), definiujemy

\[
\omega_K(\delta)=\sup\{\|T(x-x')\|:
x,x'\in K,\ \|P(x-x')\|\le\delta\},\qquad\delta\ge0.
\]

Na całej przestrzeni \(\omega_{\ell^2}(0)=0\), natomiast

\[
\omega_{\ell^2}(\delta)=+\infty\quad\text{dla każdego }\delta>0. \tag{3}
\]

Wystarczy wybrać \(x=\delta n e_n\), \(x'=0\). Każdy z tych stanów należy do \(\ell^2\), \(\|P(x-x')\|=\delta\), a \(\|T(x-x')\|=\delta\sqrt n\to\infty\). Rosnące normy źródeł są legalne w tej nieograniczonej klasie. Nie wolno używać tego ciągu jako kontrprzykładu na ustalonej kuli.

### 3.3. Na kuli źródeł cel ma ostry wykładnik Höldera

Ustalmy \(R>0\) i \(K_R=\{x:\|x\|\le R\}\). Dla \(h=x-x'\) nierówność Cauchy’ego–Schwarza daje

\[
\|Th\|^2=\sum_{n\ge1}\frac{|h_n|^2}{n}
\le\left(\sum_{n\ge1}|h_n|^2\right)^{1/2}
\left(\sum_{n\ge1}\frac{|h_n|^2}{n^2}\right)^{1/2}
=\|h\|\,\|Ph\|.
\]

Stąd

\[
\boxed{\omega_{K_R}(\delta)\le
\min\{2R,\sqrt{2R\delta}\}.} \tag{4}
\]

Dla \(x=Re_n\), \(x'=-Re_n\) i \(\delta_n=2R/n\) otrzymujemy dokładnie

\[
\omega_{K_R}(\delta_n)=\frac{2R}{\sqrt n}
=\sqrt{2R\delta_n}. \tag{5}
\]

Stała w (4) jest więc optymalna, a wykładnika \(1/2\) nie można zastąpić żadnym \(\alpha>1/2\) z jedną skończoną stałą dla wszystkich dostatecznie małych \(\delta\): iloraz wzdłuż (5) wynosi \((2R)^{1-\alpha}n^{\alpha-1/2}\to\infty\). Nie twierdzimy, że (4) jest równością dla każdego \(0<\delta<2R\); ostrość została wykazana na podanym ciągu. Dla \(\delta\ge2R\) równość \(\omega_{K_R}(\delta)=2R\) osiąga para \(\pm Re_1\).

Kula \(K_R\) nie jest zwarta w normie \(\ell^2\); ciąg \(Re_n\) ma wzajemne odległości \(R\sqrt2\). Stabilność wynika tutaj z jawnej nierówności interpolacyjnej, a nie ze zwartości tej kuli. Mechanizm należy do klasycznej stabilności warunkowej [3].

Co więcej, stabilny jest **wybrany cel \(Tx\)**. Odtworzenie całego \(x\) na tej samej kuli nie jest jednostajnie ciągłe. Dla celu \(T=I\) te same pary \(\pm Re_n\) dają odległość celu \(2R\), choć odległość danych dąży do zera. W istocie moduł odtwarzania pełnego stanu na \(K_R\) wynosi \(2R\) dla każdego \(\delta>0\). Jest to dokładne rozdzielenie stabilności obserwabli i stabilności pełnego stanu.

## 4. Moduł, średnica i rola zwartości

Niech teraz \(X\ne\varnothing,Y,Z\) będą metryczne. Dla dowolnych \(r,\tau\) definiujemy

\[
\omega(\delta)=\sup\{d_Z(\tau x,\tau x'):
d_Y(rx,rx')\le\delta\}.
\]

Możliwa jest wartość \(+\infty\). Ponieważ pary \(x=x'\) są dopuszczalne, supremum jest nieujemne. Zachodzą trzy osobne fakty:

1. \(\omega(0)=0\) jest równoważne dokładnej faktoryzacji przez \(r(X)\).
2. \(\omega(\delta)\to0\) przy \(\delta\downarrow0\) jest równoważne istnieniu jednostajnie ciągłego czynnika \(\bar\tau\) na \(r(X)\) z metryką odziedziczoną z \(Y\). Dla kierunku odwrotnego, przy danym błędzie celu \(\eta>0\), wybieramy tolerancję jednostajnej ciągłości dla błędu \(\eta/2\), a następnie bierzemy połowę tej tolerancji w definicji \(\omega\). To usuwa ewentualną różnicę między znakami \(<\) i \(\le\).
3. Jeśli \(I_\tau(y;\varepsilon)=\{\tau x:d_Y(rx,y)\le\varepsilon\}\ne\varnothing\), to
   \[
   \operatorname{diam}I_\tau(y;\varepsilon)\le\omega(2\varepsilon).
   \]
   Wynika to z nierówności trójkąta. Jest to górne ograniczenie, nie automatyczna równość dla ustalonego odczytu ani twierdzenie o istnieniu estymatora osiągającego połowę tej średnicy w dowolnej przestrzeni \(Z\).

Jeżeli \(X\) jest zwarta, \(r,\tau\) są ciągłe i \(\tau\) jest stała na włóknach \(r\), to \(\omega(\delta)\to0\). Gdyby nie, można dobrać \(\eta>0\), \(\delta_n\downarrow0\) i pary \(x_n,x'_n\) o odległości danych co najwyżej \(\delta_n\), lecz odległości celów większej od \(\eta\). Użycie połowy dodatniego dolnego ograniczenia supremów wystarcza, nawet bez powoływania się na osiąganie supremum. Podciąg w zwartej \(X\times X\) zbiega do \((x,x')\). Ciągłość daje \(r(x)=r(x')\) i jednocześnie \(d_Z(\tau x,\tau x')\ge\eta\), sprzecznie ze stałością na włóknach.

Zwartość jest wystarczająca, ale nie konieczna: pokazuje to (4). Sama ograniczoność klasy również nie wystarcza: pokazuje to przypadek \(T=I\) na \(K_R\).

Jako kontrolę stałej w przykładzie skalarnym weźmy \(X=[-1,1]\), \(r(x)=x^3\), \(\tau(x)=x\). Tożsamość

\[
x^2+xx'+x'^2-\frac{(x-x')^2}{4}
=\frac{3(x+x')^2}{4}\ge0
\]

daje \(|x^3-x'^3|\ge|x-x'|^3/4\). Para \(x=-s,x'=s\), \(s=(\delta/2)^{1/3}\), osiąga ograniczenie dla \(0\le\delta\le2\). Dla większych \(\delta\) wystarczają końce przedziału. Dokładny moduł dla wszystkich \(\delta\ge0\) to

\[
\omega(\delta)=\min\{2,(4\delta)^{1/3}\}. \tag{6}
\]

## 5. Zakres wyniku i zastosowanie

Przed oceną odporności należy określić **pomiar, cel, klasę dopuszczalnych źródeł oraz normy i metryki**. W przykładzie (2) zmiana wyłącznie klasy źródeł przekształca (3) w (4), a zmiana wyłącznie celu z \(T\) na \(I\) ponownie niszczy stabilność na kuli. Dlatego nie istnieje jedna bezwarunkowa etykieta „stabilny model” wynikająca z samej iniektywności pomiaru.

Dowiedzione są wszystkie implikacje i przykłady zapisane powyżej przy ich jawnych hipotezach. Nie skonstruowano algorytmu regularyzacji dla zaszumionych danych poza obrazem pomiaru; oszacowanie średnicy nie jest takim algorytmem. Nie ustalono identyfikowalności żadnej konkretnej teorii fizycznej, ani nowości względem pełnej literatury. Materiał nadaje się na precyzyjne ogniwo między algebraicznym opisem utraty informacji a ilościową analizą odtwarzania obserwabli.

## Bibliografia i granice sprawdzenia prior art

1. Casey Rodriguez, notatki Andrew Lina, *Introduction to Functional Analysis*, MIT 18.102 (2021), Lecture 3: Quotient Spaces. [Pełny PDF](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/f168e97ce4839083e546555a6a994697_MIT18_102s21_lec3.pdf). Standardowy kontekst norm ilorazowych; odczytano źródło.
2. Casey Rodriguez, notatki Andrew Lina, ten sam kurs, Lecture 4: The Open Mapping Theorem and the Closed Graph Theorem, Corollary 38. [Pełny PDF](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/038fc32ab9c1bb63a4f29bd9d7c97961_MIT18_102s21_lec4.pdf). Sprawdzono twierdzenie o ograniczonym operatorze odwrotnym; dowód faktoryzacji powyżej podano samodzielnie.
3. Ulrich Tautenhahn, Uno Hämarik, Bernd Hofmann, Yuanyuan Shao, *Conditional Stability Estimates for Ill-Posed PDE Problems by Using Interpolation*, preprint TU Chemnitz 2011-16, 25 lipca 2011, szczególnie §§1–2. [Pełny tekst](https://d-nb.info/1213905117/34). Publikacja czasopismowa: DOI [10.1080/01630563.2013.819515](https://doi.org/10.1080/01630563.2013.819515), 2013. Odczytano pełny preprint w zakresie definicji modułu i metody interpolacji; nie zweryfikowano osobno treści wersji wydawcy, której pobranie zwróciło 403. To umiejscowienie mechanizmu, nie dowód nowości ani przypisanie autorom dokładnie przykładu (2).

Sprawdzenie literatury było ograniczone do podstaw potrzebnych w tej analizie. Nie był to systematyczny przegląd pola. Bibliografia maszynowa to plik `IW_SW_TARGET_FACTORIZATION_AND_CONDITIONAL_STABILITY_BIBLIOGRAPHY_001_20261013.bib` w tym samym katalogu; zawiera trzy odczytane źródła. Nie znaleziono powodu do deklarowania nowego formalizmu.

**Ślad wyszukiwania, 13 października 2026.** Użyto dwóch wyszukiwarek internetowych, bez filtra czasu. Podstawowe kwerendy: `site.math.ethz.ch bounded linear operators quotient space closed range open mapping theorem pdf`; `site.math.uni-bremen.de regularization inverse problems conditional stability interpolation diagonal operators`; `Douglas 1966 On majorization factorization range inclusion operators Hilbert space original AMS`; `site.ocw.mit.edu 18.102 2021 quotient spaces open mapping lecture 4`; `"Conditional Stability Estimates for Ill-Posed PDE Problems by Using Interpolation" authors`; `"Douglas" "1966" "737" "factorization"` z filtrem ams.org; `"On Majorization, Factorization, and Range Inclusion" "Douglas" "1966"`. Liczba 737 w jednej kwerendzie była nietrafionym parametrem wyszukiwania i nie jest daną bibliograficzną. Wyniki przesiano do źródeł pierwotnych i oficjalnych notatek. Następnie otwarto stronę kursu MIT i oba podlinkowane PDF-y, odczytano Corollary 38, a w preprincie [3] definicję modułu i §2.1. Źródła wtórne służyły wyłącznie znalezieniu adresów. Próby otwarcia artykułu Douglasa w AMS nie dostarczyły treści, więc nie jest podstawą tego audytu. Nie wyciągamy żadnego wniosku o braku prior art z nieudanego wyszukiwania.
