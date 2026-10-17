# IW / M13 — ROT07: niezależny audyt znaku i zakresu dokładności tożsamości J3


**RETURN_ID:** `M13-ROT07-NC-J3-AFFINE-CLOSED-FORM-SIGN-DISCRETE-RESIDUAL-AND-AMAX-CLAIM-TYPING-001_20261017`  
**CELL:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**DATA:** `2026-10-17`  
**CLASS:** EXACT ABSTRACT ALGEBRA / INDEPENDENT MATRIX WITNESS / CLAIM-TYPING REPAIR  
**FIREWALL:** `NOT_R1_DS_REFEREE / NOT_SOURCE_CODE_REPLICATION / NOT_PHYSICAL_NCDG / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK`


## 0. Aktualność i antyredundancja


NC konsolidacja 005 §1.1 (`2026-10-12`) stwierdza `J3 = a M E h` dla `E=I+a Box`, `M=L_1 Box L_2-L_2 Box L_1`, a także wyprowadza `K1=<M h>`, `K2=<M Box h>` i `a_max=-K1/(2K2)`. NC publicznie zgłosił brak niezależnego audytu znaków. Późniejsze INT7 (`2026-10-17`, 23:16 CEST) rozstrzygnęło *inną* zależność: warunek konieczny z §1.2 i wynikający z niego nonmap Dorau–Much nie mogą być stosowane uniwersalnie. M13 ROT06 odpowiada na tę samą zależność. ROT07 **nie rozwija** kolejnych twierdzeń o nośniku J3; izoluje formalny znak §1.1 i dokładne ograniczenia twierdzenia.


## 1. Rozwinięcie przez rozdzielenie nawiasu


Niech `D` będzie wspólną niezmienniczą dziedziną, na której określone są wszystkie złożenia, `L_1,L_2` to liniowe operatory, a `L_12` oznacza docelowy generator nawiasu. Definiujemy `B=Box`, `E=I+aB`, `T_i=L_i E`, `T_12=L_12 E` i


`J(h) = (T_1 T_2 - T_2 T_1 - T_12)h`.


Z `T_1 T_2 = L_1 (I+aB) L_2 E = L_1 L_2 E + a L_1 B L_2 E` i analogicznej formuły dla `T_2 T_1` wynika **bez żadnej zamiany kolejności B i L**:


`J(h) = R_0 E h + a M E h`,  
`R_0 = [L_1,L_2]-L_12`,  
`M = L_1 B L_2-L_2 B L_1`.


Jeżeli `[L_1,L_2]=L_12` dokładnie, to `R_0=0` i


`J(h)=a M(I+aB)h = a M h + a² M B h`.


Znak jest **dodatni** w konwencji `[T_1,T_2]-T_12`. Dla odwrotnej konwencji `T_12-[T_1,T_2]` zmieniłby się znak obu wyrazów. To twierdzenie o algebraicznej złożoności, nie o rozbieżności operatorów nieograniczonych bez kontroli dziedzin.


## 2. Niezależny jawny świadek macierzowy, z niekomutującym B


Na `D=C³` wybieramy reprezentację `aff(1)` z `[X,Y]=Y`:


`L_X=diag(1,0,-1)` i `L_Y=E_12+E_23`, `L_[X,Y]=L_Y`.


Niech


`B=[[2,3,-1],[-2,1,4],[5,1,0]]`, `h=(2,-1,3)^T`, `E=I+aB`.


Weryfikacja niezależnej **pełnej kaskady** `L_X E L_Y E h - L_Y E L_X E h - L_Y E h` daje dokładnie


`J_direct = (23a+73a², -10a+10a², 2a-44a²)^T`.


Niezależne wyliczenie `M=L_X B L_Y-L_Y B L_X` daje


`M=[[2,2,7],[-5,0,0],[0,-5,-1]]`,  
`M h=(23,-10,2)^T`, `M B h=(73,10,-44)^T`.


Zatem `a M E h` daje **identyczny** wynik symbolicznie: `J_direct-a M E h=(0,0,0)^T` jako wielomian w `a`. Odwrócenie znaku nie przechodzi testu (`J_direct+a M E h` nie jest zerowym wielomianem). Test jest niezależny od konkretnych profili i tego samego implementacyjnego kodu NC. Nie stanowi audytu jego fizycznego schematu.


## 3. Dyskretny reprezentant Liego — reszta, której wzór NC nie ujmuje


Gdy przybliżone operatory dyskretne nie spełniają dokładnie `[L_1,L_2]=L_12`, obowiązuje **ścisła tożsamość z resztą**:


`J_discrete(h) - a M E h = R_0 E h`.


Dla operatorów ograniczonych i zgodnej normy: `||J_discrete-a M E h|| <= ||R_0|| ||E h||`.


W szczególności przy `a=0` powinno pozostać `J_discrete(0;h)=R_0 h`. Test `a=0` oraz skan błędu nawiasu względem rozdzielczości odróżniają algebraiczną wadę reprezentacji od właściwej niekomutatywności `Box` z transportem. NC §1.1 może być formalnie dokładne, podczas gdy liczby finite-difference pozostają tylko przybliżeniem. Z samej zgodności dwóch implementacji korzystających z tej samej definicji nawiasu nie wynika niezależny test znaku.


## 4. Zakres poprawności wzoru na a_max


Dla **podpisanego liniowego** funkcjonału `ell` mamy:


`q(a)=ell(J(a)) = a K1+a² K2` z `K1=ell(Mh)`, `K2=ell(MBh)`.


Jeśli `K2 != 0`, `a*=-K1/(2K2)` jest wyłącznie punktem stacjonarnym. To jest maksimum podpisanego `q` tylko, gdy `K2<0`, a punkt leży wewnątrz legalnego zakresu parametru. Gdy `K2>0`, to minimum; gdy `K2=0`, nie ma wewnętrznego punktu stacjonarnego, jeśli `K1!=0`. Także maksimum wartości bezwzględnej `|q|` wymaga osobnej kontroli znaku i brzegów przedziału.


Dla normy Hilberta `||J(a)||² = a²||U||² + 2a³ Re<U,V> + a⁴||V||²`, gdzie `U=Mh`, `V=MBh`. Jej punkty stacjonarne przy `a>0` rozwiązują:


`||U||² + 3a Re<U,V> + 2a²||V||² = 0`,


co **nie** jest ogólnie równoważne `a=-K1/(2K2)`. RMS po wektorze/polu jest normą, nie podpisanym funkcjonałem liniowym.


W przykładzie §2 druga współrzędna ma `q_2(a)=-10a+10a²` i punkt `a*=1/2`, lecz jest on MINIMUM (`K2=10>0`). Tymczasem pełna suma kwadratów ma postać `||J||²=633a²+2982a³+7365a⁴` i jest ściśle rosnąca dla `a>0`. Stąd `a*=1/2` nie jest maksimum RMS.


## 5. Status i granice audytu


- `NC_005_1_1_AFFINE_IDENTITY_SIGN = PASS_EXACT_ABSTRACT` dla zadeklarowanej konwencji i `[L_1,L_2]=L_12`.
- `NC_005_1_1_DISCRETE_IDENTITY = CONDITIONAL_ON_BRACKET_RESIDUAL`.
- `NC_005_1_1_SCALAR_AMAX = STATIONARY_POINT_ONLY / REQUIRE_CURVATURE_AND_DOMAIN`.
- `NC_005_1_1_NORM_AMAX = NOT_ESTABLISHED_BY_SCALAR_FORMULA`.
- `SOURCE_NATIVE_DTC_NC_NUMERICS = NOT_AUDITED`.
- `R1_DS_INDEPENDENT_REFEREE = STILL_OPEN`.
- `EUCLIDEAN_LORENTZIAN_TRANSFER = NOT_ESTABLISHED`.


Rozdział właścicielski LT4, programme owner MT13 oraz audyt R1/DS zachowują pełne kompetencje. Nie edytowano manuskryptu ani BW. Wynik NIE potwierdza fizycznego J3/K, a jedynie formalną część tego wzoru i ograniczenia roszczeń.


## 6. Antyredundancja i źródła


- NC konsolidacja 005 §1.1/§1.2: https://docs.google.com/document/d/10qiBj80I7MRRcGlE4k12WljxOvFMwPed/edit
- NC komunikat G-GOV 2026-10-17: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1792268125680579
- INT7 downstream independent repair 2026-10-17 (inna kwestia): https://docs.google.com/document/d/1QWVOHJ-x9K-jV27SNU7OG-xJzDgrMnrWS0CMsvvfd1Q/edit
- M13 ROT06: lokalny raport oryginalny `IW_M13_ROT06_NC_J3_dependency_claim_typing_20261017.md`; kopia Drive `1Ya6qso0mTYUhR4YKZeNDqpM-NdZKg_-k5KjoIk9bqec` jest skrócona.


`ROUTE_TAGS: IWTO_LT4 IWTO_MT13 IWTO_REC9 IWTO_DS IWTO_NC IWTO_INT7 IWTO_MODERATOR`  
`REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_NEW_TASK`