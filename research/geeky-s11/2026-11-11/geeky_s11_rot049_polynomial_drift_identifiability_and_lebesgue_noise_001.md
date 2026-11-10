---
artifact_id: GEEKY-S11-ROT049-POLYNOMIAL-DRIFT-IDENTIFIABILITY-LEBESGUE-NOISE-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-11-11
exposure: PUBLIC
status: SOURCE_FINITE_RESTRICTED_POSITIVE_AND_NEGATIVE_THEOREMS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# ROT049 — Wymierna granica liczby referencji dla wielomianowego dryfu, operator Lebesgue’a i ślepa weryfikacja modelu

## 0. Własność wyniku, historia i przegląd pierwszeństwa

W linii Geeky uprzednio wykazano: ROT015–017 – patologia surowego projektera TT na parzystej siatce i prawidłowy rzeczywisty ortoprojektor `B=GA`; ROT027/029 – dokładny jeden operator Liego uśredniany po wszystkich pozycjach filtracji i symbol Fouriera; ROT033 – filtr niestacjonarny; ROT034 – nieidentyfikowalność harmonogramów dowolnych; ROT035–037 – ograniczony model sześciopoziomowy i lokalna odwrotność dokładnego operatora; ROT038 – nominalny wybór sond; ROT039/040 – jego niejednostajna odporność; ROT041 – algebraiczna kompresja sumy filtracji; ROT042–043 – oszacowania jednostajne i rzeczywisty skok Jacobianu; ROT044 – globalna dwustronna stabilność na wypukłym stożku ograniczonej rodziny przy ZNANEJ kalibracji względnej, z `c=1.20e-5` dla parzystego `N>=200000`; ROT045 – algebraiczna symetria nieznanych wzmocnień, identyfikacja po jednej znanej referencji przy STACJONARNYCH wzmocnieniach i błąd starszego różniczkowania granic ramp w `float64`; ROT046 – nawet dwie referencje są niejednoznaczne przy nieznanym dryfie, ale `|ell''|<=H` daje ostrą granicę interpolacji; ROT047 – `K` referencji przy kontrolowanej krzywiźnie, nieusuwalny ślepy dryf `C²`, błąd kalibracji; ROT048 – referencje zorientowane na znany czas celu, brak możliwości certyfikacji globalnej krzywizny `H` samymi skończonymi odczytami.

**Wkład wyłącznie ROT049:** jawnie WĘŻSZA klasa: każdy ze znormalizowanych logarytmów sześciu względnych wzmocnień jest dokładnym wielomianem stopnia **co najwyżej znanego `q`**. W tej klasie wykazujemy dokładny próg liczby referencji, jego ostrość, szumową normę operatora interpolacji w zadanej chwili, porównanie dwóch określonych schematów węzłów i fałszywie uspokajające skończone sprawdzanie klasy modelu. Nie podważamy ROT046–048 dla dowolnych gładkich dryfów. Jest to klasyczna algebra interpolacji Lagrange’a oraz klasyczna teoria uwarunkowania; **brak roszczenia do nowej matematyki**. Literatura: Berrut–Trefethen, *Barycentric Lagrange Interpolation*, SIAM Review 46(3), 501–517 (2004), DOI `10.1137/S0036144502417715`; Higham, *The numerical stability of barycentric Lagrange interpolation*, IMA J. Numer. Anal. 24(4), 547–556 (2004), DOI `10.1093/imanum/24.4.547`.

**Provenance:** zachowany **niezmieniony pomocniczy** `deepseek_python_20260627_a87249.py`, rzeczywista suma bajtów SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`; historyczne produkcyjne `dtc0a_runtime_v0_3_1.py` niedostępne. Host: pełny niemaskowany parzysty torus `N³` rzeczywistych symetrycznych tensorów, poprawne `B=GA`, oryginalny pełny **trójskładnikowy** symetryczny Lie przy `C=(0,cos x,0)`, `Ealpha=I+alpha h² Δ2`; wyjściowe sześć niezerowych pasm `H0+`, `H1−`, `H1+`, `H2−`, `H3+`, `H4−`. Wielkie siatki testowane **tylko źródłowo dokładną formułą Fouriera i wymiernymi granicami czasu**, nie gęstą symulacją `N³`.

## 1. Model pomiarowy i osobne niezidentyfikowane amplitudy referencji

Znane poziomy dawki `x_j=j*0.009/5`, pięć znanych ramp o nachyleniu `v=0.012`; sześć dodatnich czasów plateau `d_j`, `sum d_j=0.25`. Nieznane parametry `z=(t,t d0,...,t d4)` należą do otwartego wypukłego stożka `C={z0>0, z1..z5>0, sum(z1..z5)<0.25*z0}`. Zgodnie z ROT044 dla **każdej parzystej N>=200000** źródłowo dyskretna mapa sześciu odczytów `F_N:C→R6` spełnia `||F_N(z)-F_N(z')||₂ > c||z-z'||₂`, gdzie `c=1.2e−5`. Nie jest to twierdzenie dla harmonogramów nieograniczonych.

Dla niezależnie znanych harmonogramów referencyjnych `d_ref,j`, z **osobną nieznaną dodatnią amplitudą bezwzględną** `t_ref,j`, odczyty w chwilach `s_j` to

`Y_ij = t_ref,j Ω_N,i(d_ref,j) exp(ell_i(s_j))`, `sum_i ell_i(s)=0`.

Wobec dodatniości `Ω_N,i` można obliczyć

`r_ij=log[Y_ij/Ω_N,i(d_ref,j)]`, `e_ij=r_ij-(1/6)sum_k r_kj=ell_i(s_j)`.

Ta konstrukcja nie wymaga znajomości `t_ref,j`, lecz wymaga poprawnego sześciokanałowego modelu, braku zerowych obserwacji, znanych harmonogramów referencyjnych oraz jednakowej semantyki kalibracji między wszystkimi odczytami. Jeżeli pomiary referencyjne są zaszumione, `e_ij` nie są dokładnymi próbkami wielomianów.

## 2. R49.1 — dokładny próg `K=q+1` i konstrukcja falsyfikująca `K<=q`

**DODATNIE, warunkowe twierdzenie.** Jeżeli każdy `ell_i` jest rzeczywistym wielomianem stopnia **≤q**, wówczas `q+1` różnych chwil znanych referencji `s0,...,sq` wyznacza `ell_i(τ)` w **dowolnej** chwili `τ` w przedziale, dokładnie i jednoznacznie, poprzez

`ell_i(τ)=sum_(j=0)^q L_j(τ)e_ij`, gdzie `L_j(τ)=prod_(k != j)(τ−s_k)/(s_j−s_k)`.

Dalej znana kalibracja względna w chwili celu pozwala zastosować jednoznaczną globalną odwrotność `F_N` z ROT044. Dowód: niezerowy wielomian stopnia ≤q nie może mieć `q+1` różnych pierwiastków, więc jądro mapy próbkowania jest trywialne. Dla `q=0` wystarcza jedna referencja, zgodnie z ROT045.

**OSTROŚĆ.** Przy `K<=q` różnych referencjach i celu `τ` niewystępującym wśród nich wielomian `P(τ')=a prod_(j=1)^K(τ'−s_j)` ma stopień `K<=q`, znika we wszystkich referencjach, ale `P(τ) != 0`. Wektor `ell=(P,−P,0,0,0,0)` zachowuje `sum_i ell_i=0` i dodatniość względnych wzmocnień. Dla dostatecznie małego `a` alternatywny legalny `z'` istnieje dokładnie dzięki lokalnej otwartości `F_N(C)` z ROT044: `F_N(z')=diag(exp(ell(τ)))F_N(z)`. Para `(z,ell)` i `(z',0)` daje **dokładnie te same wszystkie K referencji i pomiar docelowy**. Wynik dotyczy przypadku, gdy pomiar celu nie jest sam znaną referencją. Algebraiczny argument jest dokładny; reszty Newtona są kontrolą numeryczną, nie substytutem istnienia.

## 3. R49.2 — normy Lebesgue’a i jawne ograniczenia szumu referencji

Dla `K=q+1` węzłów interpolacji definiujemy punktową funkcję Lebesgue’a `Λ_q(τ)=sum_j |L_j(τ)|`. Dla referencyjnych błędów względnych `|δ_ij|<=eps_ref<1` w sześciu kanałach, `log(1+δ_ij)` mieści się w przedziale `[L,U]=[log(1−eps_ref),log(1+eps_ref)]`. Odejmowanie średniej z sześciu kanałów daje **ostrą** granicę bezwzględnego błędu pojedynczej znormalizowanej próbki `(5/6)(U−L)` (ROT047). Wobec tego, przy dokładnie wielomianowym dryfie,

`max_i |ellhat_i(τ)−ell_i(τ)| <= η = Λ_q(τ) * (5/6) log[(1+eps_ref)/(1−eps_ref)]`.

Jest to także **ostra punktowo granica samego kanału** przy dopuszczalnym adversarialnym wzorze błędów referencji zgodnym ze znakami `L_j(τ)`. Nie twierdzimy, że wszystkie sześć kanałów jednocześnie osiąga tę granicę.

Dla względnego błędu celu `eps_t` otrzymujemy `Q=(1+eps_t)exp(η)−1`. Jeśli odwrócony wynik `zhat` pozostaje dopuszczalny i ma resztę `r=||F_N(zhat)−y_corr||₂`, to przy `||F_N(z)||₂<=B`:

`||zhat−z||₂ <= [r+Q*B]/(1.2e−5)` dla każdej parzystej `N>=200000`.

Wymaga to niezależnego oszacowania `eps_ref,eps_t,B` i modelu stopnia `q`. Brak tłumienia błędów o dowolnej korelacji; nie ma tu twierdzenia o fizycznym szumie aparatury.

### Konkretny przykład stopnia 12: dwie jawne siatki 13 referencji

W zadanej chwili celu `τ=4879/5000=0.9758` porównano węzły `s_j=j/12` (**równomierne**) oraz `s_j=[1−cos(jπ/12)]/2` (**Czebyszew–Lobatto**). Niezależne 110-cyfrowe bezpośrednie wielomiany Lagrange’a oraz oddzielny algorytm barycentryczny `float64` zgadzają się co do punktowej normy:

| Węzły | `Λ_12(0.9758)` | Ostra granica błędu log kanału przy `eps_ref=1e-12` |
|---|---:|---:|
| Równomierne | 89.324209191805 | 1.4887e−10 |
| Czebyszewa–Lobatto | 1.520626597533 | 2.5344e−12 |

Stosunek wynosi **około 58.74**. Jest to **dokładnie wskazana chwila celu**, nie certyfikat globalnego maksimum funkcji Lebesgue’a ani dowód, że te węzły są optymalne we wszystkich zadaniach. Wystarczy stwierdzenie, że rozmieszczenie referencji jest istotne dla odporności nawet wtedy, kiedy liczba referencji osiągnęła próg dokładnej identyfikacji.

W oryginalnym pomocniczym modelu sześciu pasm z dokładnymi wymiernymi granicami czasu, przy `N=200000,300000,1000000`, każdy z dwóch układów z **bezszumowymi** referencjami odzyskuje rzeczywisty wielomianowy dryf stopnia 12 i źródłowe `z` z błędem poniżej `2e−8`. Przy błędach o module `eps_ref=1e−12`, których znaki dobrano przeciw interpolacji, otrzymano w `N=300000`:

| Węzły | Błąd `||zhat−z||₂` | Konserwatywny warunkowy certyfikat błędu `z` |
|---|---:|---:|
| Równomierne | 2.31288254e−6 | 1.24630107e−5 |
| Czebyszewa–Lobatto | 3.93735761e−8 | 2.12204120e−7 |

Błędy referencji mają ten sam limit, lecz ich znaki są wyznaczone dla **każdego z układów** przez jego wagi Lagrange’a; nie jest to ta sama jedna realizacja szumu w dwóch układach. Nie ma pomiarów fizycznych ani globalnego twierdzenia o zbieżności Newtona z dowolnego startu.

## 4. R49.3 — dodatkowa referencja jako test falsyfikujący, nie dowód prawdziwości klasy modelu

W klasie `deg ell<=q`, `K=q+1` dokładnych referencji wystarcza do odzyskania dryfu. Jeśli do tych danych dopiszemy **jedną dodatkową niezależną znaną referencję** w czasie `τ_h` i jej wartość odbiega od wartości przewidzianej przez wielomian interpolacyjny, model stopnia ≤q zostaje **sfalsyfikowany**. Szczególnie jawny przykład: dryf stopnia `q+1` równy `a prod_(j=0)^q (τ−s_j)` znika we wszystkich pierwszych `q+1` punktach, lecz nie w dodatkowym różnym `τ_h`.

Odwrotna implikacja **jest fałszywa**: zgodność z dodatkowymi finitely wieloma wartościami nie dowodzi, że pomiędzy nimi nie występuje wyższy wielomian z pierwiastkami w miejscach referencji lub gładki bump z ROT048. Przy szumie rozbieżność musi przekraczać uzasadnioną granicę błędu; sama niezerowa liczba zmiennoprzecinkowa nie falsyfikuje fizycznego modelu. Nie należy utożsamiać **warunkowej identyfikowalności** z **certyfikacją założeń** na podstawie tych samych danych.

## 5. Odrębne ścieżki obliczeń, falsyfikacje i ograniczenia

- `rot049_exact_degree_threshold.py`: dokładne `Fraction` sprawdzenia interpolacji monomów do stopnia 12, kontrprzykładu jądra dla `K=q`, sześciu wycentrowanych wielomianów i ostrości mnożnika `(5/6)Λ` – **183** kontrole.
- `rot049_highprecision_lebesgue.py`: niezależne 110-cyfrowe `mpmath` dla wielomianów Lagrange’a, punktowej normy w dwóch układach, ostrych wzorców szumu i pomocniczej siatki próbek (nie globalnej optymalności) – **237** kontroli.
- `rot049_source_finite_poly_calibration.py`: oryginalny pomocniczy symbol sześciu sond, wymierne granice ramp, poprawny Jacobian i odwracanie przy trzech siatkach, dwie siatki referencji, różne nieznane amplitudy referencji, syntetyczny noise gate – **133** kontrole.
- `rot049_degree_insufficient_source_falsifier.py`: dokładne wymierne wielomiany znikające w `K=q` referencjach (`q=3,6,12`), a następnie niezależne źródłowo dyskretne pary harmonogramów o identycznych odczytach – **418** kontroli.
- `rot049_heldout_degree_falsification.py`: dokładna negatywna/pozytywna semantyka jednej dodatkowej referencji i wyższego ukrytego stopnia (`q=1,3,6,12`) – **84** kontrole.
- `rot044_literal_aux_source_gain.py`: odziedziczone, ponownie wykonane wywołania **niezmienionego pomocniczego** pełnego tensora `N³`, `B/E` i **całego trójskładnikowego Liego**, tylko `N=12,16` – **29** kontroli. Nie są nowym, niezależnym eksperymentem; maksymalny modalny błąd względem kodu pomocniczego około `2.69644e−16`.

**ŁĄCZNIE 1084/1084 wykonane asercje** (w tym 29 dziedziczonych i wiele jednostkowych sprawdzeń wymiernych). Nie jest to 1084 niezależnych pomiarów naukowych. Rachunek numeryczny stanowi dowód odtwarzalności; ścisły próg `q+1` wynika z elementarnej algebry wielomianów, a globalna odwracalność źródłowego celu jest warunkowo przejęta z ROT044, które nadal oczekuje na niezależną recenzję.

## 6. Custody i sufit twierdzeń

Jedno archiwum lokalne rozmowy zawiera kompletny polski raport, sześć programów (pięć nowych i jeden odziedziczony), pomocniczy moduł wielomianowy, niezmienione źródło i niezmienione pomocnicze moduły, sześć oryginalnych JSON oraz sześć `stdout.txt`, `README.md` i `SHA256_MANIFEST.json`. Archiwum powinno zostać uznane za zweryfikowane **wyłącznie po faktycznym sprawdzeniu CRC, sum i niezależnego czystego replay**. Osobny publiczny zapis raportu GitHub, jeśli wykonany, należy weryfikować pełnym `fetch_file` przypiętego commitu i porównaniem bajtów. Komunikat Slack jest przekazaniem do recenzji, nie podpisem autoryzacyjnym.

**Sufit**: brak nowości matematycznej, twierdzeń o oryginalnym produkcyjnym `dtc0a_runtime_v0_3_1.py` i historycznym maskowanym `h=fI/K_A`, brak transferu do NCDG J3/K/GR/GW/PBH lub dowolnych harmonogramów, brak rzeczywistych specyfikacji aparatury, brak niezależnej recenzji, BW, CANON, EXEC. `NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE`.