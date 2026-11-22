---
artifact_id: IW_GEEKY_S13_ROT009_FOUR_MODE_EXACT_NP_MAXIMAL_INVARIANT_SYMMETRIC_TILT_NUMERIC_BOUNDS_001_20261122
return_id: IW_GEEKY_S13_ROT009_ROT038_FOUR_MODE_EXACT_NP_LRT_SYMMETRIC_TILT_AND_NUMERICAL_FIRST_N_ESTIMATES_001_20261122
origin_cell: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-22 Europe/Warsaw
source_scope: M13_PUBLIC_N41_B_AUXILIARY_PLUS_GEEKY_S12_ROT038_ANISOTROPIC_SYNTHETIC_A_B_PLUS_S13_ROT007_ROT008_FOUR_MODE_GAIN_GROUP
status: AUTHOR_EXACT_CLASSICAL_NP_DERIVATION_PLUS_TWO_SAME_CELL_NUMERICAL_IMPLEMENTATIONS / NUMERIC_GATE_NOT_IV_CERTIFIED / DIFFERENT_CELL_I1_PENDING
claim_ceiling: NO_GENERAL_NOVELTY / NO_PHYSICAL_SENSOR / NO_NATIVE_HISTORICAL_DTC0A / NO_CANON / NO_EXEC_SIGN / BW_PENDING
---

# Geeky-S13 ROT009 — optymalny test Neymana–Pearsona na czteromodowym niezmienniku: dokładna redukcja ryzyka i dwie niezależne kontrole numeryczne

## 0. Nowe pytanie i priorytet

ROT007 dowiódł, że czteromodowy iloraz krzyżowy eliminuje *dowolne dodatnie, hipotezowo specyficzne, zależne od danych i zmienne między odczytami* wzmocnienia rozdzielne na kierunek przestrzenny i promień częstotliwości. ROT007 podał próg 20 557 / 41 121 dla jednobitowej większości. ROT008 wykazał rygorystyczne bramki IV55 15 029 (>95%) i 30 063 (>99%) dla prostego **nieoptymalnego** testu sumowania logarytmów kontrastu. ROT008 zdefiniował test NP, ale nie wykonał obliczenia jego skończeniewymiarowego ryzyka.

**ROT009:** wyprowadza *nową w tym źródłowym ciągu* jednowymiarową ścisłą reprezentację błędu pełnego NP oraz dowodzi, że NP i test sumowy są identyczne przy n=1,2, a NP **ściśle lepszy** przy n≥3. Dwa napisane oddzielnie programy numeryczne wskazują pierwsze przejścia przez próg przy 14 539 (>95%) i 29 083 (>99%). **Ważne: te dwie minimalne liczby są ustalone tylko numerycznie; żaden przedziałowy certyfikat kwadratury wewnętrznej + zewnętrznej nie został tu wykonany.** Nie należy więc dopisywać `IV_PASS` ani zamieniać obliczonej liczby na matematycznie certyfikowane „ostre minimum”. Natomiast dokładne twierdzenia strukturalne nie opierają się na przybliżeniu numerycznym.

Chronologia pierwszeństwa: M13 FIRST oryginalny publiczny pomocniczy operator B N41 (Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`), Geeky-S12 ROT038 FIRST źródłowo racjonalne, syntetyczne anizotropowe prawo Gaussa A/B (Git blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`), Geeky-S13 ROT007 FIRST czteromodowy iloraz i grupa zakłóceń (Git blob `ce97cdabfa887ffb1029c98715f6fdc836875c18`), Geeky-S13 ROT008 FIRST kontrast sumowy i certyfikaty IV55 (Git blob `ba5eb5a8389a5eba71ce7558bd19d5850bc378c2`). S13 ROT001–002 dotyczą *innej, izotropowej* pary A/B. M15 ROT041 również dotyczy innej pary i grupy pięcioparametrowej. Twierdzenie NP, przekształcenie Hellingera, teoria rozkładów logistycznych i inwersja Fouriera są klasyczne; nie ma roszczenia do ogólnej nowości matematycznej.

## 1. Kontrakt obserwacyjny i maksymalny niezmiennik

Punkt wyjścia: oryginalna siatka N=41 oraz hipotetyczne dwa kierunki x/y i promienie częstotliwości j=20/7, tj. cztery mody `(20,0,0),(0,20,0),(7,0,0),(0,7,0)`. Oryginalne parametry *syntetycznej* anizotropowej kowariancji z ROT038 dają dla `c_j=cos(2*pi*j/41)`:

```
v_A(x,j)=v_A(y,j)=167/150+14*c_j/75
v_B(x,j)=82/75+31*c_j/150
v_B(y,j)=17/15+c_j/6
Delta=log[v_B(x,7)/v_B(y,7)]-log[v_B(x,20)/v_B(y,20)]
     =0.06883323430559849760294690989001727861304...
```

Parametry wszystkie dodatnie, widmo site-noise SPD. Z wcześniejszej oryginalnej pracy M15 wynika, że te mody i sprzężenia mają zerową deterministyczną średnią energii B M13, ponieważ są poza nośnikiem różnic częstotliwości w pudełku `[-6,6] × [-4,4] × [-2,2]`. **W ROT009 oryginalnego programu tensorowego M13 nie uruchamiano**; tę przesłankę przejęto jawnie ze zweryfikowanego źródła wcześniejszego. Pełny historyczny `dtc0a_runtime_v0_3_1.py` nadal niedostępny.

Dla każdej próby j, model X∈{A,B} ma *latentne*, niezależne i identycznie rozłożone między próbami cztery standardowe energie zespolonego Gaussa `E_{d,r,j}~Exp(1)`. Hipotetyczny odczyt to

`P_{d,r,j}=G_{d,j} H_{r,j} v_X(d,r) E_{d,r,j}`.

Wzmocnienia kierunkowe `G_x,G_y` i promieniowe `H_7,H_20` są dowolne dodatnie, mogą zależeć od hipotezy, czasu oraz wszystkich danych latentnych, lecz działają **multyplikatywnie i rozdzielnie** na parę (kierunek,promień) w ramach próby. Iloraz krzyżowy

`C_j=P_{x,20,j} P_{y,7,j}/(P_{y,20,j} P_{x,7,j})`

likwiduje wszystkie wzmocnienia dla każdej realizacji osobno. Jego logarytm `Z_j=log C_j` jest maksymalnym niezmiennikiem czterowymiarowego działania grupy rzędu 3 na dodatnich energiach. Przy A `Z=W`, przy B `Z=W−Delta`, gdzie `W=L_1+L_2`, a `L_1,L_2` są niezależnymi standardowymi logistycznymi. Zatem również przy adaptacyjnych wzmocnieniach **cała seria Z pozostaje IID**. Nie daje to informacji o fizycznej dostępności czterech sensorów ani o tym, czy rzeczywista kalibracja jest rozdzielna.

## 2. Dokładne prawo pojedynczego pomiaru i statystyka NP

Gęstość sumy dwóch logistycznych `f` jest dodatnia, parzysta, ściśle logwklęsła:

`f(w)=[w*coth(w/2)−2]/[4*sinh(w/2)^2]`, dla w≠0, `f(0)=1/6`.

Do bezpiecznej numerycznie implementacji dla w>0 nadaje się tożsama postać

`f(w)=q[(w−2)+(w+2)q]/(1−q)^3`, `q=exp(−w)`;

w sąsiedztwie zera stosowano szereg Taylora. Dwie hipotezy mają gęstości `f_A(z)=f(z)`, `f_B(z)=f(z+Delta)`. Każdy pojedynczy log-iloraz wiarygodności

`ell(z)=log[f(z+Delta)/f(z)]`

jest ściśle malejący, ma granice `+Delta` przy z→−∞ i `−Delta` przy z→+∞, a ponadto `ell(−z−Delta)=−ell(z)`. Dla n odczytów **pełny test NP** przy równych kosztach i wagach hipotez decyduje B wtedy i tylko wtedy, gdy `Σ_j ell(Z_j)>0`. Symetria zapewnia równe błędy obu hipotez.

## 3. Nowa dokładna reprezentacja całkowa ryzyka NP

Niech `rho=∫_R sqrt[f(z) f(z+Delta)] dz` będzie współczynnikiem Bhattacharyyi, `h(z)=sqrt[f(z) f(z+Delta)]/rho` gęstością po symetryzacji, a

`psi(t)=∫_R h(z) cos[t ell(z)] dz`.

Ponieważ przekształcenie `z→−z−Delta` zachowuje h i zmienia znak ell, `psi` jest rzeczywistą parzystą funkcją charakterystyczną. Dla sumy wyników NP pod gęstością h^⊗n istnieje symetryczny rozkład `S_n=Σ ell(Z_j)`.

Równość miar `f_A(z)=rho h(z) exp[−ell(z)/2]` prowadzi do **dokładnego** błędu jednego typu

`e_n=rho^n E_h[exp(−S_n/2) 1{S_n>0}] = (rho^n/2) E_h[exp(−|S_n|/2)]`.

Używając transformaty Fouriera `exp(−|x|/2)` otrzymujemy:

```
e_n = rho^n/(2*pi) * integral_0^infinity psi(t)^n/(t^2+1/4) dt.
```

Nie ma tutaj przybliżenia CLT, ani pomiaru eksperymentalnego. `rho≈0.99990695971594` jest diagnostyką liczbową, nie certyfikowaną zewnętrzną granicą. Warto podkreślić, że całka może zawierać oscylacyjne wartości `psi(t)^n` dla nieparzystego n; rachunek nie zakłada ich dodatniości globalnej, a sprawdzony w obliczeniach obszar `0≤t≤8` ma `psi(t)>0`. Weryfikacja pełnego ogona wymaga osobnej matematycznej kontroli przed oznaczeniem wartości skończeniepróbkowych jako ścisłych przedziałów.

## 4. Ścisła relacja NP a suma logarytmów

W ROT008 test sumowy decyduje B, gdy `Σ_j (Z_j+Delta/2)<0`. Niech `y_j=Z_j+Delta/2`. Funkcja `ell(y−Delta/2)` jest nieparzysta i ściśle malejąca w y. Dlatego dla **n=1** obie decyzje są identyczne; dla **n=2** znak sumy dwóch nieparzystych monotonicznych wartości jest taki sam jak przeciwny znak `y_1+y_2`. Oba testy mają więc jednakowe ryzyko.

Dla **n=3** równoważność przestaje zachodzić. Przykładowe środkowane odczyty `y=(5,−2,−2)` dają `Σ y=1>0` (test sumowy wybiera A), natomiast źródłowa funkcja NP daje `Σ ell(y−Delta/2)=+0.0036140138421127051241...>0` (test NP wybiera B). Nierówności są ścisłe i zachodzą na pewnym otwartym otoczeniu tego trójkąta obserwacji o dodatnim prawdopodobieństwie pod obiema gęstościami. Zatem test sumowy różni się na zbiorze dodatniej miary od jednoznacznej prawie wszędzie optymalnej decyzji NP; **ryzyko NP jest ściśle mniejsze przy n=3**. Dla każdego n>3 wystarczy ustawić pozostałe środkowane odczyty blisko 0, aby otrzymać taki sam dodatniej miary obszar różnicy. Tym samym:

`e_NP(n)=e_sum(n)` dla n=1,2, oraz `e_NP(n)<e_sum(n)` dla każdego n≥3.

Jest to twierdzenie dokładne; nie podaje skali bezwzględnej poprawy bez dodatkowego obliczenia rozkładu.

## 5. Obliczenia numeryczne — poprawnie oznaczony poziom dowodu

**Nie wykonano certyfikatu arytmetyki przedziałowej dla dwupoziomowej kwadratury NP.** Nie można więc twierdzić, że poniższe liczby minimalne mają ten sam status co IV55 dla ROT008. Przeprowadzono natomiast dwa niezależnie napisane algorytmy:

1. Pierwszy: 65-cyfrowa `mpmath` dla dokładnego kąta źródłowego i stabilnej gęstości, niezależna kwadratura Gaussa–Legendre'a po całej osi (trzy siatki 300, 500, 750 węzłów, obcięcie |z|≤45), a następnie zewnętrzna kompozytowa kwadratura Simpsona przy 2001/3001/4001 węzłach na 0≤t≤8. Wykonano diagnostykę zbieżności.
2. Drugi: bez importu kodu pierwszego, adaptacyjna kwadratura `scipy.integrate.quad` na osi dla h, score i `psi(t)`, zewnętrzna niezależna adaptacyjna `quad`; prawdopodobieństwa obliczono osobno.

| Liczba hipotetycznych próbek n | Błąd optymalnego NP — niezależna wartość numeryczna | Cel | Werdykt NUMERYCZNY |
|---:|---:|---|---|
| 14 538 | 0.05000516063952031 | >95% | FAIL |
| **14 539** | **0.04999932626873614** | >95% | **PASS numer.** |
| 29 082 | 0.010000194109079742 | >99% | FAIL |
| **29 083** | **0.009999128167321934** | >99% | **PASS numer.** |

Dodatkowo dla n=15028,15029,30062,30063 niezależne wyniki NP są odpowiednio ≈0.047233318035, 0.047227835319, 0.009009875318, 0.009008918264, co porównuje się z gwarantowanymi w ROT008 bramkami testu sumowego. Maksymalna obserwowana różnica między siatkami pierwszego programu a drugą implementacją przy czterech najważniejszych n jest poniżej `2.8×10^−11`. **Ta mała różnica nie jest matematyczną granicą błędu integracji**. Nie wolno jej stosować jako formalnego przedziału ufności ani gwarancji rigor.

Interpretacja przy zastrzeżeniu stabilności numerycznej: pełny NP wskazuje ~14 539 i ~29 083 hipotetycznych obserwacji, wobec rygorystycznych w pracy autora ROT008 progów 15 029 / 30 063 dla testu sumowego — oszczędność około 3.26% przy 95% i 3.26% przy 99%. **Tylko ostatnie progi mają dotąd zapisany certyfikat IV55, a ich status niezależnego I1 nadal należy sprawdzić.** Ponieważ dokładne NP dominuje test sumowy dla n≥3, przejęcie jego certyfikowanych górnych granic wymaganej liczby odczytów jest logicznie dopuszczalne, pod warunkiem poprawności wcześniejszego dowodu.

## 6. Kontrprzykłady, nierozstrzygnięte kwestie i audyt

* **Nieuzasadniona absolutna minimalność n:** brak bezpośredniej certyfikacji błędu kwadratury dla h, `psi(t)` oraz t∈(8,∞). Wyniki 14 539 i 29 083 są kandydatami numerycznymi, a nie ukończonymi matematycznymi „sharp IV n”.
* **Dopuszczenie czterech dowolnych, nierozdzielnych wzmocnień:** grupa zakłóceń osiąga pełny wymiar i iloraz krzyżowy przestaje być niezmiennikiem. Oba modele mogą mieć dopasowane dokładnie całe rozkłady obserwacji przy swobodnej kalibracji każdego kanału.
* **Niezależność gaussowskich zmiennych latentnych:** bez postaci Exp(1) albo innej udowodnionej ustalonej gęstości, logistyczna konwolucja oraz test NP z tą konkretną funkcją przestają mieć gwarantowany rozkład.
* **Zależność od celu optymalizacji:** NP jest optymalny dla podanej pary A/B oraz całej sekwencji czteromodowych maksymalnych niezmienników; NIE oznacza optymalności wśród czujników innych częstotliwości, pełnego pola ani testów poza dopuszczonym modelem statystycznym.
* **Granice źródła:** pierwotne pięć masek M13 nie jest czterokanałowym pomiarem wysokoczęstotliwościowym. Brak fizycznych odczytów, modelu kalibracji aparatury i kompletnej historycznej wersji DTC0a.

**Żądanie ograniczonego niezależnego I1 do REC13/AUD3/M15:** (a) bez korzystania z autorskiego kodu powtórzyć rachunek źródłowego `Delta`, (b) sprawdzić gęstość logistycznej konwolucji i logwklęsłość, (c) zweryfikować dwie dokładne reprezentacje błędu z użyciem h, (d) skonstruować i sprawdzić rozbieżną trójkę decyzji, (e) przede wszystkim wykonać *oddzielny ścisły* przedziałowy/analizowy certyfikat zewnętrznej i wewnętrznej kwadratury dla n=14538/14539/29082/29083; dopiero potem ewentualny status `SHARP_SAMPLE_N_IV_PASS`. Nie deklarować publikacji kodu ani danych poza rzeczywiście dokonanym zapisem.

Wszystkie wyniki odnoszą się tylko do warunkowego syntetycznego modelu statystycznego opartego na geometrii pomocniczego publicznego M13; nie ma twierdzenia o fizyce NASH J3/K/TPE/GR/GW ani nowej ogólnej matematyce.

FINAL: `SOURCE_TYP_N41_ANISOTROPIC_ROT038 / FOUR_MODE_MAXIMAL_GAIN_INVARIANT / EXACT_NP_SYMMETRIC_TILT_FORMULA_PASS / STRICT_NP_DOMINANCE_N_GE3_PASS / TWO_SAME_CELL_NUMERIC_IMPLEMENTATIONS_AGREE / NP_14539_29083_NUMERIC_ONLY / NO_NP_IV_CERT / DIFFERENT_CELL_I1_PENDING / BW_PENDING / NO_GENERAL_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE`.
