# IW / M13 ROT11 — Audyt matematyczny NC GPT tura 1: sufit pomiarowy, świadkowie, źródła


**RETURN_ID:** `M13-ROT11-NC-GPT-TURA1-EXACT-NECESSITY-NONCOLLINEAR-AND-SOURCE-SUBTRACTION-001_20261019`  
**Data:** 2026-10-19  
**Komórka:** IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13  
**Klasa:** exact classical mathematical referee / partial source-native literature audit / anti-rediscovery.  
**Status:** `[▷]` REVIEW_RETURN; NO_CANON; NO_EXEC_SIGN; NO_NOVELTY_INFERENCE; NO_PHYSICAL_UPGRADE; NO_NEW_TASK.  
**Protokół niezależności:** NIE JEST TO PRAWIDŁOWY BLIND G1: przed otwarciem pakietu audytu widziałem treść NC-011 z deklarowanym „iff”, jej dowodem wystarczalności i otwartą koniecznością, a potem Załącznik B. Własny dowód 1.2 jest matematycznie samodzielny, lecz wynik nie jest ślepą predykcją. Materiał należy oceniać jako jawny referee proof; nie liczyć jako blinded independent confirmation.


## 0. Currentness i źródła kontrolujące


Pakiet audytowy NC: `research/nc/2026-10-18/audyt/AUDYT_NC_GPT_TURA1_MATEMATYKA_I_ATRYBUCJA.md`, aktualizujący reminder z 19 X w tym samym folderze. NC-015 jest erratą do innych ustaleń i wprost pozostawia pytania 1.1/1.2 bez nowego dowodu. Istotne obiekty to NC-009, -010, -011, -013 oraz własny `README.md`. Osobny audyt INT7 fragmentów monografii nie stanowi audytu modelu czujnika NC. Moderator zachowuje wyłączną władzę akceptacji.


## 1. Model, bez dopisywania fizyki


Stan v(t) w R^n, v'=Gv pomiędzy impulsami, ||v(0)||_2=1. Jednostkowy kierunek odczytu e i tłumienia d, gamma>0; impuls o sile s>0 ma u=exp(-gamma s), D_d(u)=I-(1-u)dd^T. W chwili j stan tuż przed impulsem v_j^-; odczyt c_j=(1-u_j)/gamma * e^T v_j^-; stan po v_j^+=D_d(u_j)v_j^-. Protokoły to dowolne skończone ciągi czasów i sił, bez ograniczenia maksymalnej siły, minimalnej przerwy, kierunku lub przygotowania. Dla wniosków o próbkowaniu zakładamy, że pierwszy pomiar może poprzedzać dodatni odcinek swobodnej ewolucji. To model klasyczny i fenomenologiczny, nie kwantowa zasada informacji–zakłócenia.


## 2. Zadanie 1.1/1.2 — TWIERDZENIE DOKŁADNE (konieczność i wystarczalność)


Niech S=(G+G^T)/2 i mu_2(G)=lambda_max(S). Przy d=e i wyżej zadeklarowanej klasie protokołów:


  dla wszystkich jednostkowych v0, e i protokołów zachodzi gamma ||c||_2 <= 1
  wtedy i tylko wtedy, gdy mu_2(G) <= 0.


**Wystarczalność:** dla v^-=v i z=e^Tv, gamma c=(1-u)z. Dokładny ubytek energii impulsu wynosi ||v||²-||D_e(u)v||²=(1-u²)z². Stąd


    (gamma c)^2 = [||v||²-||D_e(u)v||²] (1-u)/(1+u)
                <= ||v||²-||D_e(u)v||².


Jeśli mu_2(G)<=0, to d/dt ||v||²=2v^T S v<=0 podczas każdej swobodnej ewolucji. Sumowanie strat impulsowych oraz ubytków swobodnych teleskopuje: gamma² sum_j c_j²<=||v0||²=1. Granica jest ostra jako supremum: pomiar bez oczekiwania, e=v0, s->infty daje gamma |c| ->1 (dla skończonej s niekoniecznie osiąga 1).


**KONIECZNOŚĆ (nowy dowód do luki NC):** gdy mu_2(G)=lambda>0, wybierz jednostkowy v0 będący wektorem własnym S z wartością lambda. Funkcja m(t)^2=||exp(Gt)v0||² ma pochodną w zerze równą 2 lambda>0. Istnieje zatem skończone t>0 z m=||exp(Gt)v0||>1. Wybierz e=exp(Gt)v0/m, d=e i jeden impuls z u=exp(-gamma s) mniejszym od 1-1/m (s jest dodatnie i skończone). Wtedy gamma ||c||_2=(1-u)m>1. Kontrprzykład wymaga TYLKO JEDNEGO pomiaru. Bez założeń o stabilności długoczasowej; argument działa także dla generatorów Hurwitza nie-normalnych.


**Weryfikator Hurwitza:** G=[[-1,4],[0,-1]], oba eigenvalues=-1, ale mu_2(G)=1. Dla v0=(0,1), t=1/4 mamy exp(Gt)v0=exp(-1/4)(1,1), m=sqrt(2)*exp(-1/4)>1. Ustaw e=d=(1,1)/sqrt(2), u=1/20 (gamma s=ln 20):


    gamma |c| = 19 sqrt(2) exp(-1/4) / 20 = 1.0463210983160491 > 1.


Macierz jest wykładniczo stabilna, zatem „generator stabilny” nie zastępuje wymaganego mu_2<=0.


**WAŻNY CLAIM-CEILING:** mu_2>0 obala *konkretny sufit* 1/gamma. Nie oznacza, że sup po wszystkich protokołach jest nieskończone dla każdego generatora Hurwitza. To osobne, nierozstrzygnięte pytanie w przypadku d=e.


## 3. Zadanie 1.3 — niewspółliniowość i brak ograniczenia na normę 2


Niech e,d będą jednostkowe, |e^T d|<1. Wybierz jednostkowy v0 prostopadły do d z |e^T v0|=sqrt(1-(e^T d)^2)=|sin phi|>0. W pomiarach wykonywanych w tej samej chwili t=0 impuls D_d(u) pozostawia v0 bez zmian. Dla k takich impulsów o ustalonej sile s:


    gamma ||c||_2 = sqrt(k) (1-u) |sin phi| -> infinity.


Gdy wymagane są ściśle rosnące chwile, dla każdego skończonego k wybierz dostatecznie małe dodatnie odstępy; przez ciągłość skończonego iloczynu propagatorów i impulsów każdy sygnał pozostaje np. powyżej połowy wartości przy zerowym odstępie. W rezultacie brak protokołowo jednostajnego sufitu przy dowolnym G, także G=-aI. Nie wymaga okresowego oscylatora ani zerokosztowych powrotów po okresie, lecz zakłada brak minimalnego odstępu między pomiarami.


Jeśli d=-e, projektor dd^T=ee^T i jest to TEN SAM model współosiowy; poprawny warunek jest d=+/-e, a niewspółliniowość to |sin phi|>0. Zapis NC „d!=e” trzeba doprecyzować modulo znak. Dla normy c_infinity powtarzanie wielu odczytów z tym samym c nie powoduje divergens; nie wolno rozszerzać wniosku o ||c||_2 na figura adwersarialnego modelu per-shot infinity.


## 4. Zadanie 1.4 — obiekt ilościowy dla zadeklarowanego protokołu


Dla ustalonego k, czasów, sił, e,d definiuj L_j przez v_j^-=L_j v0, gdzie


    L_1 = exp(G t_1),
    L_{j+1} = exp(G(t_{j+1}-t_j)) D_d(u_j) L_j.


Wtedy dokładna figura optymalizacji po ||v0||=1 to


    gamma^2 sup_{||v0||=1} ||c||_2^2 = lambda_max(W),
    W = sum_{j=1}^k (1-u_j)^2 L_j^T e e^T L_j.


Jest to protokołowo zależny gramian odczytu impulsowego, wywiedziony wprost z liniowości, nie uniwersalna zamknięta funkcja generatora. Globalna figura to sup po legalnych protokołach sqrt(lambda_max W)/gamma. W szczególności nie wolno zastępować jej jedynie sup_t||e^{Gt}|| ani ujemną normą logarytmiczną. W przypadku d=e i mu<=0 globalne supremum wynosi 1/gamma. Przypadek d=e, mu>0 może mieć różne zachowania globalne; brak klasyfikacji w niniejszym audycie.


## 5. Zadanie 3.1 — garbling vs postselektor: PASS_EXACT dla podanych dwóch macierzy


Wariant NC ma P=I-(1/3)11^T na C³, rho1=[[1/2,1/5,0],[1/5,3/10,0],[0,0,1/5]], rho2=[[1/2,0,0],[0,3/10,1/5],[0,1/5,1/5]]. Oba operatory hermitowskie, dodatnio określone i tr=1. Ich diagonale są identyczne: (1/2,3/10,1/5), zatem żaden stochastyczny postprocessing ustalonego standardowego pomiaru diagonalnego nie może ich odróżnić. Dokładne obliczenie daje tr(P rho_i P)=8/15 w obu przypadkach. Po postselekcji odczyt diagonalny to odpowiednio (17,11,20)/48 i (29,11,8)/48; różnica dwóch komponentów wynosi 1/4. Separacja NIE używa utraty śladu, bo prawdopodobieństwo przeżycia jest identyczne. Dowód korzysta z dwóch stanów i jednego zadeklarowanego pomiaru; nie rości uniwersalnej przewagi projekcji nad każdym garblingiem w wszystkich eksperymentach.


## 6. Zadanie 3.2 i 3.3 — scoped checks


3.2. Dla λ_n=1/(n+2), c_n=2^-n, f_n=2^-n, c'_n=4^-n(n+1), f'_n=1/(n+1), iloczyny f_nc_n=f'_nc'_n=4^-n dla każdego n. D jest ograniczonym samosprzężonym operatorem z prostymi, parami różnymi wartościami własnymi, których jedyny punkt akumulacji to 0. Każdy niezerowy współczynnik wejścia/wyjścia daje cykliczność (argument przez przybliżenie ciągłych selektorów funkcjami wielomianowymi w widmie / Stone-Weierstrass albo izolowane bieguny funkcji generującej). S=diag(2^-n(n+1)) ma normę 1 (n>=0), gęsty obraz, jest różnowartościowy, lecz inf_n |S_n|=0, więc S^-1 jest nieograniczony. Ze względu na proste widmo każdy ograniczony splatacz SD=DS musi być diagonalny; warunek Sc=c' determinuje S. PASS w zadanej klasie. Wersja NC o operatorze z widmem ciągłym nie wynika z tego dowodu; NOT ESTABLISHED. Konwencja indeksowania n>=0 jest niezbędna do deklarowanych norm; gdy n zaczyna się od 1, liczby norm zmieniają się, ale mechanizm pozostaje.


3.3. Dla X=[0,2π), U_t(θ)=e^-t θ, r(θ)=e^{iθ}, V_t=rU_tr^-1, zachodzi algebraiczna półgrupa i ciągłość orbit. Dla t>0 przestrzenna ciągłość V_t w y=1 zawodzi: limit z θ->2π^- ma e^{2πi e^-t} !=1, gdyż 0<e^-t<1, podczas gdy V_t(1)=1. Rozbieżność wynosi 2|sin(π e^-t)|, maksimum 2 przy t=ln2. PASS w dokładnej klasie topologicznej; nie dowodzi nieciągłości orbit ani związków z przyczynowością.


## 7. Zadanie 2 — bibliografia: VERIFIED TYPE HOSTS versus unresolved inclusion


**2.1 REALIZACJE:** zidentyfikowane źródło pierwotne Méric L. Augat, Robert T. W. Martin, Eli Shamovich, *Operator realizations of non-commutative analytic functions*, Forum of Mathematics, Sigma 13 (2025), e137, DOI 10.1017/fms.2025.10038, Theorem 3.6: minimalne realizacje tej samej funkcji są jednoznaczne z dokładnością do *pseudo-similarity* (zamknięty, gęsto określony, iniektywny splatacz o gęstym obrazie, bez wymagania ograniczonej odwrotności). Samo twierdzenie oraz definicja są dostępne w pełnym tekście wydawcy. Univariate case obejmuje zwykłe funkcje holomorficzne; dokładne utożsamienie konstrukcji diagonalnej NC z ich szczególną klasą następuje przez powyższe sprawdzenie minimalności. To mocne PRIOR-ART SUBTRACTION / słownictwo „pseudo-similarity”, nie nowy rezultat. Poprzednik: J. S. Baras, R. W. Brockett, P. A. Fuhrmann, *State-Space Models for Infinite-Dimensional Systems*, IEEE Trans. Automatic Control 19(6), 693–700 (1974), DOI 10.1109/TAC.1974.1100709, potwierdzono metadane i abstrakt, ale NIE twierdzę, że zawiera identyczny wariant splatacza. J. S. Baras, R. W. Brockett, *H²-Functions and Infinite-Dimensional Realization Theory*, SIAM J. Control 13(1), 221–241 (1975), DOI 10.1137/0313013, abstrakt mówi o relacjach między realizacjami tego samego systemu, ale dokładne twierdzenie bez pełnej lektury pozostaje UNVERIFIED.


**2.2 KWANTOWE KORELACJE:** Philip Pechukas, *Reduced Dynamics Need Not Be Completely Positive*, Phys. Rev. Lett. 73, 1060–1062 (1994), DOI 10.1103/PhysRevLett.73.1060, źródłowo potwierdzone twierdzenie: w obecności początkowych korelacji mapa może być określona jedynie na kompatybilnej klasie stanów, a liniowe przedłużenie poza nią nie musi być dodatnie/CP. Thomas F. Jordan, Anil Shaji, E. C. G. Sudarshan, *Dynamics of initially entangled open quantum systems*, Phys. Rev. A 70, 052110 (2004), DOI 10.1103/PhysRevA.70.052110, źródłowo potwierdzone: dynamiczne mapy dla początkowo splątanych stanów nie muszą być CP; przykład dwóch kubitów. Rozróżnić od wywodzenia uniwersalnego „każde skorelowane przygotowanie daje nie-CP”, co jest nieprawdą.


**2.3:** Dla §3.3 przypadek stanów quotient/nonquotient stanowi standardowy kontrprzykład w topologii ilorazowej; brak wykonanego kompletnego poszukiwania pierwotnego precedensu. Dla §2.8 odróżnienie klasycznych postprocessingów Blackwella od postselekcji operatorowej wynika z definicji klas działań; nie przypisuję pierwszeństwa bez źródła rozstrzygającego tak konkretną parę.


Linki źródłowe:
- NC GPT audit: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-18/audyt/AUDYT_NC_GPT_TURA1_MATEMATYKA_I_ATRYBUCJA.md
- NC reminder 19 X: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-18/audyt/PRZYPOMNIENIE_GPT_TURA1_ZAKRES.md
- NC-011: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-18/IW_NC_MEASUREMENT_CEILING_IS_THE_LOGARITHMIC_NORM_011_20261018.md
- NC-015: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-18/IW_NC_KOREKTY_PO_AUDYTACH_INT7_REC9_015_20261019.md
- Augat/Martin/Shamovich 2025: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/operator-realizations-of-noncommutative-analytic-functions/AC0391ED346031CC3A1BD86C498C515F
- Baras/Brockett/Fuhrmann 1974: https://doi.org/10.1109/TAC.1974.1100709
- Baras/Brockett 1975: https://doi.org/10.1137/0313013
- Pechukas 1994: https://doi.org/10.1103/PhysRevLett.73.1060
- Jordan/Shaji/Sudarshan 2004: https://doi.org/10.1103/PhysRevA.70.052110


## 8. Dispositions, status and claim ceiling


NC_TASK_1P1_SUFFICIENCY = PASS_EXACT; NC_TASK_1P2_NECESSITY = PROVED under declared unrestricted protocols; NC_TASK_1P3_NONCOLLINEAR = PASS with e and d collinearity modulo sign and unbounded sampling cadence; NC_TASK_1P4_GLOBAL_CONST = OPEN, exact finite-protocol gramian given. NC_TASK_2P1_PSEUDOSIMILARITY = SOURCE_MATCH_FOR_HOST / no novelty; NC_TASK_2P2_INITIAL_CORR = VERIFIED_PRIMARY_HOST; NC_TASK_2P3 = PARTIAL, no primary exact witness match. NC_TASK_3P1_3P2_3P3 = PASS at declared abstract carriers (numeric/symbolic or exact proofs). Not a blinded G1; return qualifies as M13 nonblind referee, independent mathematical proof not independent outcome exposure.


All analyses here are classical/abstract: no quantum measurement backaction, no physical gravitation, no BBN endpoints, no EXEC_SIGN and no CANON. Need human approval for claim registry status `[▲] VERIFIED_THEOREM`; not `[▣] VERIFIED_IMPLEMENTATION` merely because identities were checked. Programme state REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD; no new cross-cell tasks created. ROUTE_TAGS: IWTO_MODERATOR IWTO_NC IWTO_LT4 IWTO_MT13 IWTO_REC9 IWTO_INT7 IWTO_DS IWTO_PRF11.