# Rozdział 7. Wierność opisu efektywnego: twierdzenia łączące i granice równoważności

## 7.1. Zakres wspólnego problemu

Projekcja na sektor zachowany, iloraz przestrzeni stanów, filtracja spektralna, kanał kwantowy, proces wieloczasowy i redukcja kinetyczna należą do różnych kategorii matematycznych. Nie istnieje automatyczne utożsamienie ich nośników. Uzasadnione wspólne pytanie brzmi: jaka informacja oraz jaka struktura są zachowane przez *konkretną, prawidłowo typowaną mapę* i dla której klasy obserwabli?

Niech (U_t:X	o X) będzie pełną ewolucją, (r:X	o Y) surjektywną redukcją, a (	au:X	o Z) obserwablą. Istnienie (V_t:Y	o Y) z (rU_t=V_tr) oznacza autonomię zredukowanego opisu. Słabsze wymaganie dotyczy jedynie przyszłej wartości celu: istnienia (g_t:Y	o Z), dla którego (	au U_t=g_tr). Ani pierwsza, ani druga własność nie certyfikuje fizycznej realizowalności redukcji; wymaga ona oddzielnego określenia przygotowań, pomiarów i interwencji.

## 7.2. Rozdzielające obserwable a projektowalność ewolucji

Rodzina funkcji (mathcal F={arphi_a:Y	o Z_a}_{ain A}) **rozdziela punkty**, jeżeli dla każdych (y
e y') istnieje (a) takie, że (arphi_a(y)
earphi_a(y')).

**Twierdzenie 7.1 (rozpoznawalność pełnej rodziny celów).** Przy ustalonym (tge0) i surjektywnym (r) następujące warunki są równoważne:

(a) istnieje mapa (V_t:Y	o Y) z (rU_t=V_tr);

(b) dla każdej (arphi_ainmathcal F) istnieje (g_{a,t}:Y	o Z_a), dla którego (arphi_a rU_t=g_{a,t}r).

*Dowód.* Z (a) otrzymujemy (b), wybierając (g_{a,t}=arphi_a V_t). Jeśli zachodzi (b) i (r(x)=r(x')), to dla wszystkich (a) mamy
[
arphi_a(rU_tx)=g_{a,t}(r x)=g_{a,t}(r x')=arphi_a(rU_tx').
]
Rozdzielanie punktów daje (rU_tx=rU_tx'). Zatem (rU_t) jest stała na włóknach (r); surjektywność pozwala określić jednoznaczne (V_t) przez (V_t(r x)=rU_tx). (square)

Jeśli własność zachodzi dla wszystkich (t), a (U_t) jest półgrupą, również (V_t) jest półgrupą algebraiczną. Twierdzenie nie daje ciągłości (V_t), dodatniości całkowitej ani równoważności procesowej. Dla zredukowanych operatorów gęstości informacyjnie kompletna rodzina wartości oczekiwanych może rozdzielać stany, lecz jej wyniki nie muszą być osiągalne jednocześnie w pojedynczym doświadczeniu.

## 7.3. Cel autonomiczny bez autonomicznego stanu

Niech pełny układ spełnia
[
dot a=-a,qquad dot b=h,qquaddot h=0,
]
a (r(a,b,h)=(a,b)). Przy tych samych (a,b) i różnych (h) przyszłe wartości (b(t)) są różne. Redukcja nie jest autonomiczna. Jednak cel (	au(a,b,h)=a) spełnia (	au(U_t(a,b,h))=e^{-t}a), niezależnie od ukrytej zmiennej.

Jest to ścisły kontrprzykład do przejścia „brak autonomii stanu (Rightarrow) brak przewidywalności każdej obserwabli”. W modelach kinetycznych analogiczną możliwość wyraża dokładność pewnej całki ważonej mimo niezgodności historii populacji. Nie wynika stąd dokładność innego funkcjonału.

## 7.4. Złożenie etapów redukcji

Niech (X,Y,Z) będą przestrzeniami Banacha, (rinmathcal B(X,Y)), (sinmathcal B(Y,Z)), a (U_t,V_t,W_t) — odpowiednio typowanymi ewolucjami, niekoniecznie liniowymi. Definiujemy defekty
[
D_r(t,x)=rU_tx-V_trx,qquad
D_s(t,y)=sV_ty-W_tsy.
]

**Twierdzenie 7.2 (dokładna tożsamość złożenia defektów).** Dla (D_{sr}(t,x)=srU_tx-W_tsrx) zachodzi
[
D_{sr}(t,x)=sD_r(t,x)+D_s(t,rx).
]

*Dowód.* Dodajemy i odejmujemy (sV_t rx). Ograniczona liniowość (s) pozwala przenieść ją przed różnicę pierwszego składnika. (square)

**Wniosek.**
[
|D_{sr}(t,x)|le |s|,|D_r(t,x)|+|D_s(t,rx)|.
]
Dokładność obu interfejsów wystarcza dla dokładności złożenia. Odwrotność zawodzi: błędy mogą się znosić, a niezerowy (D_r) może należeć do (ker s).

Ta algebraiczna tożsamość nie utożsamia kolejnych redukcji z dwiema operacjami fizycznie legalnymi. Na przykład złożenie ogólnej mapy liniowej na macierzach gęstości z kanałem CPTP nie musi być kanałem CPTP.

## 7.5. Residuum generatora a błąd obserwabli

Niech (x:[t_0,T]	o X) oraz (y:[t_0,T]	o Y) będą klasycznymi rozwiązaniami
[
dot x=f(x,t),qquad dot y=g(y,t)
]
w przestrzeniach Banacha. Niech (r:X	o Y) będzie różniczkowalna wzdłuż trajektorii (x), a (g) lokalnie lipschitzowska w drugim opisie z mierzalną stałą (L(t)ge0), dla której zachodzi oszacowanie na odcinku łączącym (r(x(t))) i (y(t)). Zakładamy całkowalność wszystkich wyrażeń poniżej. Definiujemy źródłowy defekt równania
[
eta(t)=Dr(x(t)),f(x(t),t)-g(r(x(t)),t),qquad
arepsilon(t)=|eta(t)|.
]

**Twierdzenie 7.3 (oszacowanie wierności trajektorii).** Dla (e(t)=r(x(t))-y(t)) zachodzi
[
|e(T)|le
e^{int_{t_0}^T L}|e(t_0)|
+int_{t_0}^{T}
e^{int_s^T L(u),du}arepsilon(s),ds. 	ag{7.1}
]
Jeśli (psi:Y	omathbb R) jest (K)-lipschitzowska na zakresie obu trajektorii, prawa strona przemnożona przez (K) ogranicza błąd celu (|psi(r(x(T)))-psi(y(T))|).

*Dowód.* Różniczkując (e), otrzymujemy
[
dot e=eta(t)+g(r(x(t)),t)-g(y(t),t).
]
Z nierówności dla normy i hipotezy Lipschitza wynika nierówność całkowa
[
|e(t)|le |e(t_0)|+int_{t_0}^tig(arepsilon(s)+L(s)|e(s)|ig),ds.
]
Postać nierówności Grönwalla z czynnikiem całkującym daje (7.1). Oszacowanie celu wynika z Lipschitzowskości (psi). (square)

Wzór (7.1) jest twierdzeniem dla zadeklarowanych równań i mapy (r). Nie można bez zmian podstawiać do niego nieograniczonego operatora spektralnego, wieloczasowej supermapy kwantowej ani relacji między przestrzeniami historii. Tam trzeba udowodnić odpowiedni analog reguły łańcuchowej, domeny i normy.

## 7.6. Obserwable, normy i niejednostajność odtwarzania

W poprzednim rozdziale cele były stabilne w zadanej normie tylko wtedy, gdy istniały odpowiednie ograniczenia. Dla ogólnej obserwabli o module jednostajnej ciągłości (omega_psi) zamiast wniosku lipschitzowskiego otrzymujemy
[
|psi(r(x(T)))-psi(y(T))|
le omega_psi!left(
e^{int L}|e(t_0)|+
int e^{int_s^T L}arepsilon(s),ds
ight),
]
o ile moduł jest niemalejący i poprawnie określony na rozważanej klasie. Bez jednostajnej ciągłości wniosek globalny może zawodzić, mimo jednoznaczności odtworzenia obserwabli.

Przykład diagonalny na (ell^2) z rozdziału 2 rozdziela jednoznaczność od ograniczonej faktoryzacji, a przykład spektralny z rozdziału 4 rozdziela zachowanie zredukowanego ilorazu od zachowania dokładnego obrazu operatora. Te różnice nie są jedną nową „zasadą utraty informacji”: wynikają z innych norm, innych przestrzeni ilorazowych i innych hipotez.

## 7.7. Granica między opisem stanowym i procesowym

Przypadki kwantowe pokazują jeszcze mocniejszą nierównoważność. Równość kanałów dla każdej początkowej macierzy gęstości w dwóch ustalonych chwilach nie determinuje wszystkich praw sekwencji z pośrednimi interwencjami. Kontrprzykład ze środowiskiem dwóch kubitów z §5.5a daje dwie identyczne mapy redukcji bez interwencji, lecz po legalnym resecie stanów i pomiarze w bazie (X) ich rozkłady wyników są rozłączne. Dla tych praw odległość całkowitej wariacji wynosi (1).

Zatem klasy równoważności stanów według odczytów końcowych mogą być ściśle większe od klas równoważności procesów według pełnego zestawu testerów. Konkretny zakres twierdzenia wymaga ustalenia czasu, przygotowań i zbioru interwencji.

Przy różnych rodzinach testerów (mathcal E_1,mathcal E_2) nie wolno nawet zapisać równości praw bez określenia transportu (F:mathcal E_1	omathcal E_2). Stałość prawa pierwszego procesu na włóknach (F) zapewnia jedynie faktoryzację na (F(mathcal E_1)), nie legalność fizycznego przedłużenia jako supermapy CPTP ani jego przyczynowość.

## 7.8. Porównanie z dojrzałymi teoriami

W teorii Mori–Zwanziga/Schura eliminuje się zmienne z ewolucji liniowej lub właściwie przygotowanej projekcji i uzyskuje jądro pamięci. W teorii Hodge’a i kompleksów Hilberta filtracja spektralna wpływa na dokładny obraz różniczkowania, jego domknięcie i działanie na kohomologii. W teorii kwantowych sieci sekwencyjnych pamięć określają wieloczasowe prawa interwencji i ograniczenia całkowitej dodatniości. W kinetyce reakcji źródło, relaksacja i odpowiedź końcowa rozdzielają chwilową dokładność zmiennych od dokładności celu.

Nie istnieje na podstawie samych tych analogii twierdzenie, które przenosiłoby defekt kompresji Schura w klasę kohomologii, kwantową miarę pamięci procesu lub fizyczny błąd obfitości jądrowych. Każda taka identyfikacja wymagałaby wspólnego nośnika i jawnego, zachowującego właściwą strukturę odwzorowania. Dojrzałe wyniki tych teorii są więc **gospodarzami** dla odpowiednich fragmentów monografii, a nie szczególnymi przypadkami bez uprzednio dowiedzionego nowego prawa.

### 7.8.1. Transport spektralny, transport łańcuchowy i rozdzielanie widma

Projektowalność \(rU_t=V_tr\) nie określa jeszcze operatora samosprzężonego ani jego miary spektralnej. Aby porównywać rachunki funkcyjne dwóch nośników Hilberta, potrzebujemy ograniczonego operatora splatającego \(J:H_1\to H_2\). Dla nieujemnych samosprzężonych \(A\) na \(H_1\) i \(B\) na \(H_2\) istnieje jednak zaskakująco silne kryterium, w którym **jedna odpowiednio rozdzielająca funkcja** wystarcza.

**Twierdzenie 7.4 (pojedynczy rozdzielający mnożnik spektralny).** Niech \(A,B\ge0\) będą samosprzężone, \(J\in\mathcal B(H_1,H_2)\) oraz \(t_*>0\). Jeżeli
\[
J e^{-t_*A}=e^{-t_*B}J, \tag{7.2}
\]
to dla każdej ograniczonej funkcji borelowskiej \(m:[0,\infty)\to\mathbb C\) mamy
\[
Jm(A)=m(B)J. \tag{7.3}
\]

*Dowód.* Połóżmy \(T=e^{-t_*A}\), \(S=e^{-t_*B}\). Są to ograniczone samosprzężone kontrakcje o nieujemnym widmie i zerowym jądrze. Z \(JT=SJ\), przy pomocy wielomianów i aproksymacji ciągłej, otrzymujemy \(Jg(T)=g(S)J\) dla ciągłych \(g:[0,1]\to\mathbb C\). Twierdzenie spektralne i przejście przez funkcje proste/borelowskie (np. metodą monotoniczną dla projekcji spektralnych) rozszerzają to na ograniczone \(g\) borelowskie. Dla danego \(m\) kładziemy \(g(u)=m(-\log u/t_*)\) na \((0,1]\), a \(g(0)\) definiujemy dowolnie. Jądra \(T,S\) są zerowe, więc ich projekcje spektralne na \(\{0\}\) znikają. Z rachunku funkcyjnego wynika \(g(T)=m(A)\), \(g(S)=m(B)\), co dowodzi (7.3). \(\square\)

W szczególności pojedynczy dodatni czas \(t_*\) wystarcza dla całej półgrupy cieplnej, ponieważ \(e^{-t_*\lambda}\) rozdziela punkty \([0,\infty)\). Istotny jest warunek różnowartościowości na **wspólnym zbiorze zawierającym oba widma** oraz dostępność wspólnego odwrotnego mnożnika borelowskiego. Różnowartościowość osobno na każdym widmie nie wyklucza kolizji między widmami.

*Kontrprzykład 7.2 (mnożnik nierozdzielający).* Na \(\mathbb C^2\) wybierzmy \(A=\operatorname{diag}(0,1)\), \(B=\operatorname{diag}(0,3)\), \(J=I\) oraz \(h(\lambda)=\cos(\pi\lambda)\). Mamy \(Jh(A)=h(B)J=\operatorname{diag}(1,-1)\), ale \(A\ne B\), a ich widma są odmienne. Zatem równość dla **dowolnego jednego** mnożnika nie wystarcza; twierdzenie 7.4 nie przeczy temu przykładowi, bo \(h\) nie rozdziela wspólnego widma.

Transport widmowy nie przenosi automatycznie *dokładnych brzegów* kompleksu Hilberta. W tym celu trzeba dodatkowo transportować różniczkowanie.

**Twierdzenie 7.5 (transport filtrowanych dokładnych obrazów).** Niech \((H_i^\bullet,d_i)\), \(i=1,2\), będą kompleksami Hilberta o laplasjanach \(\Delta_i^k\). Załóżmy, że dla każdego \(k\) operator \(J_k:H_1^k\to H_2^k\) jest ograniczoną bijekcją, przenosi dokładnie dziedziny
\[
J_k D(d_1^k)=D(d_2^k),
\]
spełnia zgodność łańcuchową \(d_2^kJ_k=J_{k+1}d_1^k\) na tej dziedzinie oraz dla ograniczonego borelowskiego \(f\) ma własność
\[
J_k f(\Delta_1^k)=f(\Delta_2^k)J_k.
\]
Dla \(B_i^k=\operatorname{ran}d_i^{k-1}\) zachodzi wtedy
\[
J_k(B_1^k)=B_2^k,\qquad
J_k\!\left(f(\Delta_1^k)B_1^k\right)
=f(\Delta_2^k)B_2^k. \tag{7.4}
\]

*Dowód.* Z przeniesienia dziedzin, bijektywności \(J_{k-1}\) i splatania różniczek dostajemy \(J_k\operatorname{ran}d_1^{k-1}=\operatorname{ran}d_2^{k-1}\). Następnie przenosimy \(J_k\) przez \(f(\Delta_1^k)\) i stosujemy pierwszą równość. \(\square\)

Bez surjektywności odpowiedniej mapy na przestrzeni brzegów otrzymujemy na ogół jedynie inkluzję. Transport samych domknięć \(\overline B_i^k\) nie identyfikuje dokładnych obrazów \(B_i^k\). Również to samo *wyrażenie różniczkowe* przy innych warunkach brzegowych może określać inne domknięte operatory.

Twierdzenia 7.4 i 7.5 rozdzielają dwa wymagania: **splatanie rachunku funkcyjnego** oraz **splatanie różniczek i ich dziedzin**. Pierwsze nie daje drugiego. Oba łącznie nie określają praw wieloczasowych interwencji kwantowych ani mikroskopowej identyczności dwóch fizycznych realizacji.

## 7.9. Ściśle postawione problemy otwarte

**Problem A (wspólna realizacja).** Dla dwóch konkretnych teorii z różnymi typami przygotowań i interwencji ustalić minimalne warunki istnienia jednej realizacji i map zachowujących całą zadaną rodzinę obserwabli oraz odpowiednie prawa złożenia. Równość wybranych obserwabli nie wystarcza.

**Problem B (transport spektralny i łańcuchowy).** Dla dwóch określonych kompleksów Hilberta na różnych metrykach lub warunkach brzegowych skonstruować jawne operatory J_k. Nie wystarcza zastosowanie tej samej funkcji f w f(Δ₁) i f(Δ₂). Należy osobno wykazać: (i) transport dziedzin i zgodność łańcuchową d₂J=Jd₁; (ii) splatanie odpowiednich operatorów samosprzężonych, np. przez rozdzielający mnożnik lub zgodność resolwent; (iii) surjektywność na rzeczywistych przestrzeniach brzegów, jeżeli zachować mamy dokładne obrazy, a nie tylko ich domknięcia. Gdy któregokolwiek warunku brak, należy określić najmocniejszą pozostającą relację oraz wskazać kontrprzykład.

**Problem C (świadectwo celu fizycznego).** Dla konkretnego modelu hadronowego źródła kosmologicznego z zależnością zaniku od aktualnego składu plazmy zbudować certyfikat błędu końcowej obserwabli na podstawie legalnego błędu obu skierowanych szybkości. Tożsamość sieczna i oszacowania (7.1) są narzędziami, ale bez danych o źródle i stabilności sieci nie stanowią jeszcze takiego certyfikatu.

**Problem D (równoważność procesu).** Dla ustalonej pary procesów kwantowych o różnych rodzinach testerów znaleźć kryterium istnienia jednej legalnej transformacji wyższego rzędu. Rozdzielić niewykonalność na poziomie włókien, relacji liniowych, dodatniości całkowitej, normalizacji i przyczynowości.

Powyższe są pytaniami dla konkretnych nośników matematycznych. Nie formułują postulatu jednej uniwersalnej teorii fizycznej.

## Literatura powiązana z wywodem

Engel i Nagel, *One-Parameter Semigroups for Linear Evolution Equations* (2000) — półgrupy, przestrzenie ilorazowe i generatory.

Brüning i Lesch, *Hilbert complexes*, *J. Functional Analysis* 108 (1992) — domknięte różniczki i słaby rozkład Hodge’a.

Arnold, Falk i Winther, *Finite element exterior calculus: from Hodge theory to numerical stability*, *Bull. Amer. Math. Soc.* 47 (2010), 281–354 — stabilność strukturalna i domknięte obrazy.

Watrous, *The Theory of Quantum Information* (2018) — kanały, operatory Choi, obserwable i ślad częściowy.

Chiribella, D’Ariano i Perinotti, *Theoretical framework for quantum networks*, *Phys. Rev. A* 80, 022339 (2009) — procesy sekwencyjne i normalizacja wyższego rzędu.

Blackwell, *Equivalent Comparisons of Experiments*, *Ann. Math. Stat.* 24, 265–272 (1953) — porządek informacji w eksperymentach.

Opisane twierdzenia wymagają swoich zadeklarowanych przestrzeni, dziedzin i klas dopuszczalnych map. Sama wspólna postać diagramu nie ustanawia wspólnego mechanizmu fizycznego.