---
artifact_id: IW_GEEKY_S13_ROT023_GLOBAL_SAME_Q_HELLINGER_DUAL_MOBIUS_IV85_001_20261123
return_id: IW_GEEKY_S13_ROT023_GLOBAL_SAME_Q_HELLINGER_MINIMAX_DUAL_TRIANGLE_MOBIUS_AND_EXACT_RESOURCE_IV85_001_20261123
origin: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-23 Europe/Warsaw
exposure: PUBLIC
status: AUTHOR_GLOBAL_SOURCE_CONDITIONAL_ANALYTIC_PROOF_PASS / IV85_DUAL_VERTEX_CERT_PASS / EXACT_SYMPY_MOBIUS_PASS / IV85_VALIDATED_SIMPSON_PASS / SAME_CELL_INDEPENDENT_SCIPY_AND_DISCRETE_Q_PASS / DIFFERENT_CELL_I1_PENDING
claim_ceiling: NO_GENERAL_MATHEMATICAL_NOVELTY / NO_GENERAL_ALL_F_DIVERGENCE_GLOBAL_MINIMAX / NO_SHARP_MINIMAX_NP_N / NO_NATIVE_HISTORICAL_DTC0A / NO_ACTUAL_RAW_SENSORS / NO_PHYSICAL_UPGRADE / BW_PENDING / NO_CANON / NO_EXEC_SIGN
---

# Geeky-S13 ROT023 — globalne minimum Hellingera dla dwóch syntetycznych rozkładów Cauchy'ego z tym samym nieznanym Q i obu nieznanych udziałach skażenia

## 0. Pytanie, rozstrzygnięcie, nowość ograniczona

ROT022 (oryginalny stan źródłowy) udowodnił uniwersalną projekcję dla **jednej** pary udziałów skażenia `eta_A=h=1/250`, `eta_B=0`: `r†(t)=max((1-h)f_A(t),c f_B(t))`, przy `c` określonym przez normalizację. Otrzymał `chi²=1.51431232020353868e−7` oraz warunki konieczne dla liczby roboczych odczytów 43,863,484 / 85,282,886. **Nie** dowodził, że ta sama para jest najmniej korzystna Hellingerowsko po wszystkich `eta_A,eta_B∈[0,h]`. Oddzielnie ROT021 dowiódł globalnie ostrego minimum jednoobserwacyjnej całkowitej wariacji i tylko potem skonstruował nieoptymalny w Hellingerze kontrprzykład zasobowy.

**WYNIK ROT023 (oryginalna, wąsko źródłowa kombinacja klasycznych narzędzi):** dla dokładnie tej pary Cauchy'ego oraz **tego samego Q w porównywanych światach** udowodniono

`sup_{eta_A,eta_B∈[0,h], Q} Aff( (1−eta_A)P_A+eta_AQ, (1−eta_B)P_B+eta_BQ ) = Aff(r†,P_B)`,

`Aff(P,R)=∫sqrt(dP*dR)`.

Maksimum osiąga `(eta_A,eta_B,Q)=(h,0,Q†)` oraz po zamianie hipotez odpowiadający mu obraz Möbiusa `(0,h,T_#Q†)`. Jest to **globalne minimum deficytu Hellingera** `H=1−Aff`, a nie tylko optimum jednostronnej podpary. Nie wykazano globalnego minimum dla wszystkich pozostałych, asymetrycznych f-dywergencji, ani optymalnego testu skończonej próbki.

Kierunkowy certyfikat IV85 sprawdza wszystkie źródłowe nierówności, które nie są czysto algebraicznymi tożsamościami. Dodatkowy IV85 z kompleksowym ograniczeniem pochodnej i 8192-panelową metodą Simpsona zawęża **dokładny** globalny deficyt afiniczności do

`H∈[0.0000000189221987311248044426100866825553017611141671, 0.0000000189221987684375348764074335174916055624409543]`.

W konsekwencji `n >= 43,883,146` jest konieczne, aby **móc** przekroczyć 95% równej-priorowej średniej trafności, a `n >= 85,321,114`, aby móc przekroczyć 99%, nawet przy arbitralnie dużej liczbie niezależnych odczytów referencyjnych Q†. Są to n niewykluczone przez konkretną ścisłą nierówność Hellingera, **nie** dowiedzione ostre minima n ani bramki wystarczające. Wzrost względem ROT022 wynosi +19,662/+38,228.

## 1. Źródła pierwotne, artefakty uprzednie i granice dostępu

1. **M13 FIRST:** oryginalny publiczny pomocniczy tensor B (Fourier/TT, N=41), `research/m13/2026-10-24/verify_m13_rot33_interval.py` @ commit `30d8549b822ecec4d6939b01dbd1e76a98495f09`, Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`. Materiał **bezpośrednio ponownie odczytany** przez GitHub. Nie wykonano natywnie niezmienionego programu M13 w ROT023, nie ma kompletnego historycznego `dtc0a_runtime_v0_3_1.py`.
2. **Geeky-S12 ROT038 FIRST:** dokładne dodatnio określone, anizotropowe, **syntetyczne** skalarnoprzestrzenne kowariancje gaussowskie A/B na oryginalnej siatce M13. Publiczny raport źródłowy Git blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`, ponownie bezpośrednio odczytany. Prawa sztucznego szumu NIE są natywną nieliniową energią tensora B.
3. **Geeky-S13 ROT016 FIRST:** cztery idealne surowe czujniki w dwóch x-odbitych parach i dokładny iloraz Cauchy'ego, Git blob `cddc2636249e9bf032fff4de78afb30481401f9a`. ROT018 FIRST — czysta TV i Huber/TV, ROT019 FIRST — eksperyment z referencją Q przy znanym eta, ROT020 FIRST — nieznane eta, sharp alias z TYM SAMYM Q i 2 sentinele, ROT021 FIRST — globalne minimum TV, ROT022 FIRST — jednostronny wspólny f-projektor i konieczne n. Bez zmiany własności wyników tych komórek.
4. **ROT022, oryginalny pełny raport i wykonane skrypty:** commit `1b46077be84fc3d27d3d2ebf8175ae9952958758`, blob `92b02050de4d0812b61af8759f4c04d2f7e85136`. Oryginał przeczytany w całości wraz z niezależnym numerycznym skanem udziałów skażenia, który sam zastrzegał brak globalnego dowodu. ROT023 nie traktuje tego skanu jako dowodu.

Przykładowe **uprzednie podstawy matematyczne**: F. Nielsen i K. Okamura, *On f-divergences between Cauchy distributions*, arXiv:2101.12459 / IEEE Transactions on Information Theory, 2022, https://arxiv.org/abs/2101.12459 (symetria dywergencji i geometria Cauchy); M. Fauß i A. M. Zoubir, *Old Bands, New Tracks—Revisiting the Band Model for Robust Hypothesis Testing*, arXiv:1510.04524, IEEE TSP 2016, https://arxiv.org/abs/1510.04524 (density bands i najmniej korzystne rozkłady); literatura Huber–Strassen. Te prace sprawdzono na poziomie stron artykułów i abstraktów; **nie** deklarujemy pełnego przeczytania ich wszystkich dowodów. Nie ma roszczenia, że osobne użyte twierdzenia (Möbius, nierówność dualna, Hellinger, Cauchy) są nowe.

## 2. Źródłowo warunkowy eksperyment — dokładne parametry

Zgodnie z ROT016 wybieramy źródłowe punkty hipotetycznych równoczesnych surowych odczytów:

`P0=(20,20,20), P1=(21,20,20), Q0=(20,21,20), Q1=(21,21,20)`.

Przy dokładnej osiowej symetrii pierwotnego pola B, wspólnych arbitralnych adaptacyjnych offsetach i dodatnich wzmocnieniach oraz syntetycznym wycentrowanym gaussowskim szumie ROT038, niezmiennik `T=(Y_P1−Y_P0)/(Y_Q1−Y_Q0)` ma czyste rozkłady:

`P_A = Cauchy(mu_A=1/84, s_A=sqrt(1−mu_A²))`,

`P_B = Cauchy(mu_B=4/585, s_B=sqrt(1−mu_B²))`,

`f_X(t)=s_X/[pi*(t²−2mu_X*t+1)]`.

W tym obrocie rozważamy **wyłącznie hipotetyczne IID obserwacje T**, następnie skażone egzogenicznie:

`R_A=(1−a)P_A+aQ`, `R_B=(1−b)P_B+bQ`, `0<=a,b<=h=1/250`.

Parametry a,b mogą być różne pod A i B, rozkład Q jest dowolny, lecz **identyczny w obu porównywanych światach** i w niezależnej referencji. Zmienność sekwencyjna a,b,Q lub wartościozależna podmiana całego T to INNE kontrakty, nieudowodnione tutaj. Wynik nie obejmuje pełnego RAW czterokanałowego wektora.

## 3. Wspólna projekcja jednostronna — punkt odniesienia z ROT022

Niech `p=f_A`, `s=f_B`, `l(t)=(1−h)p(t)/s(t)`.

Dla jednostronnej podpary `(a,b)=(h,0)` rozwiązanie ROT022 brzmi

`r†(t)=s(t) max{l(t),c}=max{(1−h)p(t),c s(t)}`,

`q†(t)=[r†(t)−(1−h)p(t)]/h`.

Stała `c∈(0,1)` jest jedynym rozwiązaniem `∫max((1−h)p,c s)=1`. Kierunkowy nowo wykonany IV85 otrzymuje

`c=0.9998123057081422115319368644887899597262...`.

Zbiór wiążący, w którym `l(t)>c`, jest pojedynczym przedziałem `(u,v)`, przy

`u≈0.45866100778143287769`, `v≈2.18025945749574822263`, `u*v=1` dokładnie.

Q† jest nieujemny i całkuje się do 1. Jednostronny argument styczny ROT022 daje unikalne minimum dla wszystkich różniczkowalnych ściśle wypukłych f-dywergencji na tej ustalonej podparze. ROT023 nie przypisuje sobie tego wcześniejszego wyniku; używa jego konstrukcji do globalnego dowodu **tylko Hellingera**.

## 4. Dowód globalny I: dualne ograniczenie afiniczności na trójkącie a>=b

Wprowadź dodatnią funkcję

`z(t)=sqrt(s(t)/r†(t))=1/sqrt(max(l(t),c))`.

Dla dowolnych gęstości r,s i dowolnej dodatniej funkcji z nierówność AM–GM jest punktowa:

`sqrt(r(t)s(t)) <= [r(t) z(t)+s(t)/z(t)]/2`.

W konsekwencji dla każdej dopuszczalnej trójki `(a,b,Q)`:

`Aff(R_A,R_B) <= F(a,b)`,

`F(a,b) = 1/2 * [(1−a) E_A z + (1−b) E_B(z^−1) + sup_t {a z(t)+b z(t)^−1}]`.

**Najważniejsza własność:** `F` jest wypukła w `(a,b)` jako supremum funkcji afinicznych. Na trójkącie `0<=b<=a<=h` maksimum wypukłej `F` musi występować wśród trzech wierzchołków `(0,0)`, `(h,0)`, `(h,h)`. Wystarczy sprawdzić te trzy przypadki; to nie jest przybliżenie przez dyskretną siatkę.

Niech `M=sup_t f_A/f_B = sqrt(595/589) = sqrt(350455)/589`, co wynika z bezpośredniego źródłowego rachunku Cauchy'ego. Pochodna ilorazu ma znak `sign(1−t²)`, a maksimum fA/fB występuje w t=+1. Stąd dokładny zakres funkcji z:

`z_min = 1/sqrt((1−h)M) = 0.99947034554172957894...`,

`z_max = 1/sqrt(c) = 1.00009386035892577897...`.

**Wierzchołek (h,0)**: `F(h,0)=Aff(r†,s)`. Równość AM–GM zachodzi dla `R_A=r†,R_B=s`; Q† jest podparte tam, gdzie `z=z_max`, więc supremum Q w F jest faktycznie osiągnięte przez Q†.

**Wierzchołek (0,0)**:

`F(h,0)−F(0,0)=h/2 [z_max−E_A z]>0`.

Nierówność jest ścisła, ponieważ na przedziale wiążącym o dodatniej masie P_A mamy `z<z_max`.

**Wierzchołek (h,h)**:

`F(h,0)−F(h,h) = h/2 [E_B(z^−1)+z_max−max(z_min+z_min^−1,z_max+z_max^−1)]`.

To jedyna materialna, niezależna nierówność źródłowa potrzebna do globalizacji. Zamiast polegać na zaokrąglonej kwadraturze, wyprowadź dolne oszacowanie oczekiwania z małego przedziału `J=[4/5,6/5]`. Iloraz `l(t)=(1−h)f_A/f_B` rośnie do t=1 i maleje po t=1, więc jego minimum na J jest minimum dokładnych wartości na końcach. Dla każdego t∈J mamy `l(t)>c`; stąd

`E_B(z^−1) >= sqrt(c) + P_B(J) [sqrt(min_J l)−sqrt(c)]`.

IV85 źródłowo i kierunkowo certyfikuje `P_B(J)>0.0645178139958364`, a oba potencjalnie decydujące odstępy

`E_B(z^−1) + z_max −(z_min+1/z_min) > 0.00003590972930870`,

`E_B(z^−1) + z_max −(z_max+1/z_max) > 0.00003618160287844`.

To są **konserwatywne ściśle dodatnie zapasy** przy użyciu podanego dolnego oszacowania oczekiwania, nie wynik numerycznej siatki. Tym samym `F(h,h)<F(h,0)`.

Ponieważ pozostałe dwa wierzchołki dają mniejsze F, dla wszystkich `a>=b` i dowolnego wspólnego Q zachodzi

`Aff(R_A,R_B) <= Aff(r†,P_B)`.

Wynik jest osiągany przez `(a,b,Q)=(h,0,Q†)`; stąd w tym trójkącie znamy dokładny globalny ekstremum Hellingera.

## 5. Dowód globalny II: dokładna inwolucja Möbiusa zamienia A i B

Dla szczególnej pary źródłowych rozkładów Cauchy'ego ustaw

`k=(mu_A+mu_B)/(1+mu_A mu_B+s_A s_B)`.

Parametry spełniają `mu_X²+s_X²=1`, a k ma zamkniętą postać symboliczną

`k=(49144−83 sqrt(350455))/921≈0.0093712445306278757311961`.

Rozważ przekształcenie rozszerzonej prostej rzeczywistej:

`T(t)=(k t−1)/(t−k)`.

Zachodzi **dokładnie**: `T(T(t))=t`, `T'(t)=(1−k²)/(t−k)²>0` poza biegunem, i

`T_#P_A=P_B`, `T_#P_B=P_A`.

Ostatnie tożsamości wynikają z działania rzeczywistych przekształceń Möbiusa na parametrze Cauchy'ego `z_X=mu_X+i s_X` w górnej półpłaszczyźnie. Dla tej konkretnej liczby k mamy algebraicznie `T(z_A)=z_B`, `T(z_B)=z_A`, a po uwzględnieniu jakobianu spełnione są obie identyczności gęstości. **Niezależny SymPy wykonał i potwierdził dokładne tożsamości, nie tylko ich przybliżenia dziesiętne.**

Dla każdego `a<=b`, wspólnego Q i rozkładów roboczych `(R_A,R_B)`, przekształcenie obu obserwacji przez T, a następnie zamiana nazw hipotez daje dopuszczalną trójkę `(b,a,T_#Q)` w poprzednim trójkącie `a>=b`. Afiniczność Hellingera jest niezmiennicza przy tej bijektywnej zmianie zmiennej i symetryczna w kolejności hipotez. Dlatego

`Aff(R_A,R_B) <= Aff(r†,P_B)`

także dla **wszystkich** `a<=b`. Równość uzyskujemy w obrazie `(a,b,Q)=(0,h,T_#Q†)`.

**Wniosek globalny:** minimum Hellingera na CAŁYM kwadracie `(a,b)∈[0,h]²` i przy dowolnym wspólnym Q jest osiągnięte w przeciwstawnych narożnikach, a wniosek nie opiera się na siatce optymalizacyjnej. Z tej samej inwolucji i transformacyjnej niezmienniczości TV wynika dodatkowo **dokładna** równość `gamma_A=gamma_B`, której ROT021 z samych zachodzących na siebie otoczek liczbowych słusznie nie ogłaszał. Jej pierwszeństwo analityczne pochodzi z tej symetrii, nie z wcześniejszego zaokrąglenia wartości gamma.

## 6. Kierunkowo certyfikowany DOKŁADNY globalny deficyt Hellingera

Nie wystarcza sam ogólny bound ROT022 `H<=chi²/[2(1+sqrt(c))²]≈1.89306806346e−8`. Możemy kierunkowo ograniczyć bezpośrednio rzeczywistą wartość H dla **globalnie** najtrudniejszej pary.

Na przedziale wiążącym I=(u,v) mamy `r†=(1-h)f_A`, poza nim `r†=c f_B`. Z tożsamości bez odejmowania dwóch bliskich 1 liczb:

`H=1−∫sqrt(r† f_B) = ∫ f_B [(1−sqrt(r†/f_B))²/2]`

wynika

`H = ∫_u^v g(t) dt + [1−P_B(I)] (1−sqrt(c))²/2`,

`g(t)=f_B(t) [1−sqrt(l(t))]²/2`.

**Ogon całej prostej poza I jest ujęty dokładnie przez CDF Cauchy'ego**, bez obcięcia zakresu t ani próbkowania ogonowego.

Program `rot023_validated_simpson_iv85.py` stosuje 8192-panelową złożoną metodę Simpsona w arytmetyce skierowanej IV85. Remainder Simpsona jest ścisły dzięki niezależnemu analitycznemu oszacowaniu czwartej pochodnej. Dla każdego realnego t∈[u,v] i zespolonego z z `|z−t|<=2/5` zachodzi:

- `|z|<2.6`, `|D_A(z)|,|D_B(z)|>(0.99−0.4)²=0.3481`, gdzie `D_X(z)=z²−2mu_X z+1`;
- `C=(1-h)s_A/s_B∈(0,1)`, `1−C<0.005`, `2(mu_A−mu_B)<0.011`; użycie `l(z)=C[1+2(mu_A−mu_B)z/D_A(z)]` daje `|l(z)−1|<0.09`;
- główna gałąź sqrt(l(z)) jest analityczna, `|g(z)|<0.001`, zaś oszacowanie Cauchy'ego daje `sup_{t∈[u,v]}|g⁽⁴⁾(t)|<4!*0.001/0.4⁴=0.9375<1`.

Rygorystyczny błąd kwadratury zatem nie przekracza

`(v−u)^5/(180*8192^4) < 1.866e−17`.

Po dodaniu arytmetycznie kierunkowych błędów oceny węzłów i dokładnej składowej ogona mamy

`H_global ∈ [1.8922198731124804442610086682555e−8, 1.8922198768437534876407433517492e−8]`.

Program IV85 potwierdził nie tylko dodatniość, ale i **jednoznaczną identyfikację części całkowitej** progów opisanych poniżej przy wykorzystaniu obu końców H. Całkowity próg wynikający z tej konkretnej nierówności nie zmienia się wewnątrz certyfikowanego przedziału H.

## 7. Dolna granica koniecznych n — teraz dla globalnie najmniej korzystnej pary

Niech `rho*=Aff(r†,P_B)=1−H_global`. Ponieważ dla obu kontrfaktycznych światów rozkład referencji jest TEN SAM Q†, dla n niezależnych odczytów roboczych i dowolnych m niezależnych referencji mamy dokładnie

`Aff(R_A^n⊗(Q†)^m, R_B^n⊗(Q†)^m)=rho*^n`.

Przez standardową nierówność TV–Hellinger:

`TV(P_n,R_n) <= sqrt(1−rho*^(2n))`,

`BayesError_n >= [1−sqrt(1−rho*^(2n))]/2`.

Wykonana kierunkowa arytmetyka IV85 sprawdziła dolną granicę błędu przy n−1 i obie strony dokładnego otoczenia globalnego H:

| Warunek na trafność przy równych priorach | Wszelkie n do tej wartości wykluczone | Pierwsze n niewykluczone przez TEN bound | ROT022 |
|---|---:|---:|---:|
| >95% | 43,883,145 | **43,883,146** | 43,863,484 |
| >99% | 85,321,113 | **85,321,114** | 85,282,886 |

W granicznym n−1 matematyczna dolna granica błędu wynosi odpowiednio **powyżej 0.05000000034627** i **powyżej 0.01000000011629**. Wartości są **konieczne**, a nie wystarczające, i nie dowodzą ostrego fizycznego limitu sprzętu ani liczby próbek NP. Są jednak teraz wsparte globalnym dowodem minimalizacji H dla źródłowo określonej rodziny same-Q, nie jedynie przez dopuszczalną podparę.

## 8. Faktyczne reprodukcje i próby falsyfikacji

1. **Nowa pierwotna implementacja IV85** `rot023_primary_global_hellinger_iv85.py`: przelicza od źródłowych racjonalnych µ obie skale i M, c, korzenie wiążące, dualne zmin/zmax, wszystkie trzy wierzchołki, certyfikat na J bez kwadratury, symbolicznie uzasadniony Möbius z IV85 kontrolą dwóch składowych zespolonych, historyczny chi² i konserwatywne progi. Nie importuje danych JSON ROT022.
2. **Odrębna symboliczna implementacja** `rot023_independent_mobius_sympy.py`: exact algebra obu gęstości z jakobianem, `T²=identity`, `T(z_A)=z_B`, `T(z_B)=z_A`, `M²=595/589`, znak pochodnej ilorazu. Nie opiera się na zaokrąglonym M ani na obrazie wykresu.
3. **Odrębna integracja SciPy** `rot023_independent_dual_scipy.py`: samodzielne θ=arctan(t) na całej osi, optymalizacja c z integralnej normalizacji, numerycznie nieujemna całka H, wszystkie trzy wartości dualne i test punktowy z jakobianem. Niezależny numeryczny H≈`1.8922198759e−8`, zgodny z IV85.
4. **Osobny certyfikat wartości H** `rot023_validated_simpson_iv85.py`: c odtworzone samodzielnie; IV85 węzłów i ogona; ścisłe globalne ograniczenie Cauchy'ego na czwartą pochodną; N=8192; n/n−1; brak numerycznych niekontrolowanych tail cutoffs.
5. **Falsyfikat numeryczny całej przestrzeni η** `rot023_independent_discrete_eta_falsifier.py`: 72 koszyki θ, 17 kombinacji a,b, osobno optymalizowane q simplex przy Hellingerze; najlepsza wybrana para `(h,0)` zgodnie z twierdzeniem. Użyte SLSQP jest jedynie diagnostyką — ścisły globalny dowód wynika z punktów 4–5, nie z 17 prób.

Wykonane testy semantyczne obejmują podmianę źródłowego µ, zerwanie Möbiusa, obniżenie lub podwyższenie progów, fałszywą równość dla wszystkich f-dywergencji, naruszenie wierzchołkowego zapasu, przypadek `Q_A≠Q_B`, niekontrolowaną podmianę postselekcyjną, oraz dostosowanie raportu do fizycznych czujników bez dowodu. Po zmianie danych kontroler ma ponownie OBLICZYĆ tożsamości, nie tylko potwierdzać sumy SHA. Faktyczny test z ZIP i wykaz mutacji znajdują się w protokole odtwarzania.

## 9. Czego twierdzenie NIE obejmuje i co należy zlecić do I1

- **Ostrość tylko Hellingera:** globalne minimum deficytu Hellingera przy wspólnym Q i ustalonym h=.004 **nie implikuje** globalnej minimalizacji każdej innej dywergencji f na pełnym kwadracie udziałów, ani ostrego minimaksowego testu Neymana–Pearsona.
- **Kwantyfikatory Q:** Q jest dosłownie identyczne w obu porównywanych światach. Przy różnych nieznanych Q, jeżeli ich oddzielne referencje nie są nieskończone, źródłowa cała rodzina statystyczna jest inna.
- **Brak fizycznej walidacji:** żadnego potwierdzenia rzeczywistych równoczesnych 4 lokalnych kanałów RAW, losowego pola gaussowskiego ROT038 w prawdziwym tensorze, stacjonarnego wspólnego Q z dostępnego fault-only channel, ani ograniczenia udziału skażenia h na urządzeniu M13. M13 tensor B Fourier/TT i DTC0a historyczne wyniki nie są tym samym, co hipotetyczny nowy rozkład odczytu.
- **Brak pełnego oryginalnego runtime:** źródła M13 czytano, nie natywnie wykonano w tym obrocie. Czyste odtworzenia własnego kodu nie zastępują niezależnego eksperymentu i audytu innej komórki.
- **Nie twierdzić, że całe ogólne twierdzenie jest nowe:** klasyczne Möbius/Cauchy oraz density-band least-favorable stanowią istotne wcześniejsze hosty; bez dalszego bibliograficznego dowodu pierwszeństwa wolno mówić jedynie o nowej lokalnej kompozycji źródłowych narzędzi.

**Zlecenie bounded I1 dla AUD3/REC14/M16:** niezależnie sprawdzić (a) poprawność globalnego przejścia przez wypukłą dualną F i trzy wierzchołki, (b) ścisłą nierówność na J oraz stacjonarność warunku M, (c) symboliczną inwolucję T i mapowanie obu gęstości, (d) kierunkowy błąd Simpsona z ograniczeniem zespolonym g⁽⁴⁾, (e) część całkowitą progów n/n−1, (f) niefizyczny sufit eksperymentu i brak globalnego f-minimax.

**Stan:** `AUTHOR_GLOBAL_SAME_Q_HELLINGER_MINIMAX_ANALYTIC_PASS / SOURCE_DUAL_IV85_STRICT_VERTEX_PASS / EXACT_MOBIUS_SYMPY_PASS / IV85_SIMPSON_SOURCE_BOUND_PASS / SAME_CELL_SCIPY_AND_DISCRETE_FALSIFIERS_PASS / COLD_REPRO_PASS / DIFFERENT_CELL_I1_PENDING / BW_PENDING / NO_GENERAL_NOVELTY / NO_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN`.
