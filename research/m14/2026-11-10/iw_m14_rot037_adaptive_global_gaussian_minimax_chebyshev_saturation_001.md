# M14 ROT037 — globalny adaptacyjny minimaks czasowy Czebyszewa

artifact_id: IW_M14_ROT037_ADAPTIVE_GLOBAL_GAUSSIAN_MINIMAX_CHEBYSHEV_SATURATION_001_20261110
return_id: M14-ROT037-CHEBYSHEV_GLOBAL_ADAPTIVE_MINIMAX_EXTRA_TIMES_THREE_VS_FOUR_AXES_001_20261110
cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
date: 2026-11-10; exposure: PUBLIC
ceiling: EXACT_CLASSICAL_CONDITIONAL_GAUSSIAN_MINIMAX / NO_NOVELTY / NO_PHYSICAL_NV_CLAIM / NO_CANON / NO_EXEC_SIGN / BW_PENDING / REFEREE_PENDING

## Pierwszeństwo i źródła

Zewnętrzne źródło Schall, Lindner, Rottstaedt et al., *Laser-enhanced quantum sensing boosts sensitivity and dynamic range*, Nature Communications **17** (2026), 10825, DOI https://doi.org/10.1038/s41467-026-78386-z, FIRST owned by XH-S5 ROT007. Rzeczywista praca NIE ustala hipotetycznej sparowanej gałęzi signed, wielomianowego dryftu per orientacja, homoscedastycznego niezależnego szumu Gaussa ani tej ekspozycji. 127 fT/sqrtHz to photon-shot-noise LIMIT, nie zmierzona techniczna czułość instrumentu. NO source-native raw data/time series. Wewnątrz: ROT031-033 najpierw geometria i ograniczony dryft, ROT034 iloraz czasowy, ROT035 optymalne węzły L-infinity oraz FIXED-EQUAL-SHOTS Gaussian negative control, ROT036 dokładna optymalizacja Fishera z minimalną liczbą p+2 czasów i rozdziałem ekspozycji. ROT037: NOWY SUFIT *globalny minimaks* przy dowolnej liczbie punktów, adaptacji i dowolnych estymatorach, plus 3-vs-4 axis. Klasyczne źródła metody: NIST DLMF §18.38 i §3.11, https://dlmf.nist.gov/18.38; https://dlmf.nist.gov/3.11. Brak nowości ogólnej.

## ZAMROŻONA KLASA

Dla m=p+1>=1 i [0,L], L>0: wektor pola b(t)=z*t^m+sum_{r<m} b_r*t^r **JEST WIELOMIANEM stopnia <=m**, ten sam współczynnik z ma być estymowany przy wszystkich harmonogramach. Cztery orientacje są wierszami A=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)), A^T A=4I3. Każda orientacja ma niezależny całkowicie nieznany dryft eta_i(t), wielomian stopnia <=m-1. Jeden odczyt Y=a_i dot b(t)+eta_i(t)+eps, niezależny eps~N(0,sigma²). Koszt każdego odczytu równy; total N. Osie i czasy mogą być wybierane ADAPTACYJNIE na podstawie wcześniejszych Y (nie antycypując przyszłego szumu). Estymator dowolny, w tym obciążony. Równość dla ciągłych ekspozycji lub integer N podzielnego przez 8m dla 4 osi / 6m dla 3; dla pozostałych integer N ogólna formuła pozostaje dolną granicą.

## R37.1 GLOBAL 4-AXIS MINIMAX, DOWÓD

C=2^(2m-1)/L^m, c=1/C i moniczny P_m(t)=T_m(2t/L-1)/C. Klasyczna ekstremalność: |P_m(t)|<=c dla każdego t w [0,L], a stopień P_m(t)-t^m <=m-1. Legalna podrodzina najmniej korzystna: dla dowolnego u in R³ wybierz b_u(t)=u*t^m, eta_{i,u}(t)=(a_i dot u)*(P_m(t)-t^m). Zatem FULL RAW mean na osi i w chwili t to (a_i dot u)*P_m(t), cel z=u. Rozważ proper prior u~N(0,tau² I3), dowolne tau>0. Przy ADAPTACYJNIE wybranej realizowanej historii posterior u jest dokładnie gaussowski, z precyzją
Q=tau^-2 I3 + sigma^-2 sum_{r=1}^N P_m(t_r)^2 * a_{i_r} a_{i_r}^T.
Reguła doboru kolejnych chwil zależy tylko od przeszłych danych, więc nie daje dodatkowego likelihoodu zależnego od u poza obserwacjami. Każda ścieżka spełnia tr Q <=3 tau^-2 +3 N c²/sigma², ponieważ ||a_i||²=3. Z tr Q^-1>=9/tr Q wynika dla KAŻDEGO estymatora (także obciążonego) Bayes MSE >=3/(tau^-2+Nc²/sigma²). Supremum ryzyka po pełnym modelu >= ryzyko bayesowskie na tej podrodzinie. Przejście tau→infinity daje DOLNĄ GRANICĘ GLOBALNEGO MINIMAKSU 3 sigma² C²/N, także po dopuszczeniu dowolnej liczby różnych czasów i adaptacji.

Jest OSIĄGANA na j=0..m węzłach Czebyszewa-Lobatto t_j=L(1-cos(j*pi/m))/2, kiedy każda z 4 orientacji dostaje N/(8m) odczytów na każdy koniec i N/(4m) na każdy węzeł wewnętrzny. Wagi najwyższego współczynnika lambda_j=1/prod_{k!=j}(t_j-t_k), S=sum|lambda|=C. Ilorazy y_i=sum lambda_j Y_i,j usuwają wszystkie nieznane stopnie <m; niezależny Var(y_i)=4 sigma² C²/N. zhat=A^T y/4 ma Cov= sigma² C²/N I3 dla WSZYSTKICH legalnych wielomianów. Tak więc w relaksacji i przy podzielnym N:
**R4*=3 sigma² 2^(4m-2)/(N L^(2m)).**
W szczególności NADMIAROWE PUNKTY, ADAPTACJA i OBCIĄŻONE estymatory nie mogą poprawić tego globalnego minimaksu w zamrożonej klasie. Nie twierdzi się tego dla niepolinomialnego pola.

## R37.2 GLOBAL 3-AXIS MINIMAX

A3=first 3 rows of A, invertible, A3 A3^T=4I3-11^T, a każda kolumna A3^-1 ma normę²=1/2. Ta sama najmniej korzystna podrodzina i prior dają pathwise Q <= tau^-2 I3 + c²/sigma² A3^T diag(n1,n2,n3) A3, sum n_i<=N. Funkcja f(n)=tr[(tau^-2 I3+c²/sigma² A3^T diag(n) A3)^-1] jest wypukła i symetryczna na permutacje n, ponieważ Gram A3 A3^T=4I-11^T. Z Jensen, f(n)>=f(N/3,N/3,N/3); tau→infinity daje globalną dolną granicę **R3*=(9/2) sigma² C²/N**. Osiąga ją równy budżet osi i temporalne węzły Czebyszewa (każda orientacja N/(6m) na każdy koniec, N/(3m) na każdy węzeł wewnętrzny). Dla tej samej waluty zasobów R3*/R4*=3/2: czwarte ramię zmniejsza całkowity wektorowy minimaks o dokładnie 1/3.

## Świadki, falsyfikatory, odtwarzalność

m=3, p=2, L=sigma²=1, N=144. P3=t³−(3/2)t²+(9/16)t−1/32, sup|P3|=1/32 i P3(1/2)=0 (midpoint shot ZERO signal in least-favorable submodel, NOT universal uselessness).
- 4 axes Chebyshev t=(0,1/4,3/4,1), shots per axis (6,12,12,6): exact full RAW 16x15 nuisance Fisher inverse Cov=(64/9)I3; total risk **64/3**.
- 3 axes same t, shots (8,16,16,8): exact RAW nuisance inverse Cov=(16/3)[[2,1,-1],[1,2,-1],[-1,-1,2]], total risk **32**.
- 4 axes, SIX TIMES t=(0,1/8,1/4,1/2,3/4,1), 6 shots at EACH of the 6 times per axis; total N144: full RAW 24x15 nuisance Fisher inverse trace **8197120/263871~31.0648764**, worse than 64/3. Illustrative negative only; global theorem above is analytical.
- Proper prior tau²=10000, Cheb Bayes risk exactly 120000/5629~21.31817, approaching minimax 64/3 as tau→infinity.

Local full Polish proof plus 3 runnable programs/2 JSON: ZIP **IW_M14_ROT037_ADAPTIVE_CHEBYSHEV_GLOBAL_MINIMAX_AND_EXTRA_TIME_SATURATION_FULL_REPRO_001_20261110.zip**, SHA256 **929ccfbf483d8edc3b4dfbca67897aa5f79a3b57f049b66687af35bca118b0d8**, 15,581 bytes. CRC PASS; 7/7 payload SHA PASS; TWO clean isolated execution JSON BYTE IDENTICAL; public pure-stdlib exact replay PASS. SymPy 67 exact checks including full nuisance Fisher; independent mpmath95 and NumPy 985 checks (360 random overcomplete designs, 520 genuinely adaptive simulated histories, m=1..12). Numeric experiments are checks, NOT mathematical proof. Full ZIP LOCAL ONLY, not presumed GitHub published.

STRICT HOLD: no source-native NV temporal data, true photon counts or instrument noise sigma, fT mapping, arbitrary nonpolynomial fields, correlated noise, variable switching costs, global Lorentz physical inverse, NASH J3/K GR GW PBH physics, general mathematical novelty, independent REC11/AUD1 verdict, LT/BW ingest, canon or EXEC sign. NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK_CASCADE.