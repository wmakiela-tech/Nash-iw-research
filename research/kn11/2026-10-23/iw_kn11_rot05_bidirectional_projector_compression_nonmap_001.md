# KN11 ROT05 — obustronny nonmap domknięcia komutatora przy kompresji

**RETURN_ID:** IW_KN11_ROT05_BIDIRECTIONAL_PROJECTOR_COMPRESSION_NONMAP_001_20261023  
**Komórka:** KCELL_INTEGRATED_01_BUD_03_SUCCESSOR_07 / KN11  
**Data:** 2026-10-23  
**Klasa:** dokładne świadectwa skończenie wymiarowe / D2 knowledge densification / wytyczenie falsyfikatora DTC0a  
**Status naukowy:** niezależny rachunek algebraiczny na bazie dojrzałej algebry operatorów; żadne twierdzenie o nowości, wyniku fizycznym ani walidacji DTC.  
**Authority:** NO_CANON / NO_EXEC / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_J3_K_INVARIANT / OWNER_DTC_CURRENTNESS_NOT_PROMOTED.

## Pytanie i wcześniejszy host

Czy domknięcie relacji komutatorowych pełnych operatorów implikuje domknięcie ich kompresji do sektora TT, i czy implikacja działa w odwrotną stronę?

KN11 ROT03 (w BW: ING-20261022-0003) ustalił dla operatorów z pośrednim projektorem tożsamość K_A=K_B+L_P oraz ostre ograniczenia norm składnika L_P z historycznych 18 scalar CSV. To NIE jest odkrycie kanału R_P (wcześniej reprezentowany przez DTC). Obecna praca dodaje dwa rozłączne, symbolicznie rozstrzygnięte świadectwa pokazujące obie możliwe błędne implikacje. M13 ROT18 wyjaśnił niezależnie ruchomą domenę fizyczną masek; nie należy traktować go jako dowodu o domknięciu komutatora:
https://github.com/wmakiela-tech/Nash-iw-research/blob/95f3348632317c68dbbe10ac1a200483f6fb89c4/research/m13/2026-10-22/IW_M13_ROT18_DTC0a_moving_mask_domain_audit_001.md

## Tożsamość typowana

Niech H będzie skończenie wymiarowym Hilbertem, P=P*=P² projektorem ortogonalnym, Q=I−P, A,B,T_b liniowymi operatorami na H, U=ran(P). Na U określmy

K_B^U=P([A,B]−T_b)P|_U,
K_A^U=([PAP,PBP]−P T_b P)|_U.

Wtedy

K_A^U = K_B^U + L_P^U,
L_P^U=P(BQA−AQB)P|_U.

Dowód: PAPBP=PABP−PAQBP oraz PBPAP=PBAP−PBQAP. Odjęcie daje wzór. Żadnych założeń o K_B=0, działaniu T_b, algebrze Liego lub fizyce. Dla operatorów DTC działających na surowym wejściu h bez wstępnego P należy stosować analogiczną tożsamość bez skrajnego prawego P; operatorowe świadectwa poniżej odnoszą się wyraźnie do **h w U**.

## Świadectwo A: źródłowy komutator zerowy, projektowany niezerowy

H=R³, e=(1,1,1)^T, P=I−ee^T/3, Q=ee^T/3; A=diag(1,0,−1), B=diag(0,1,−1), T_b=0.

A i B są rzeczywiste symetryczne i diagonalne, więc [A,B]=0 i K_B^U=0. Ale

K_A^U = (1/3) [[0,−1,1],[1,0,−1],[−1,1,0]]|_U,

ma wartości własne niezerowe ±i/sqrt(3) i normę operatorową dokładnie 1/sqrt(3). L_P^U=K_A^U. Pokazuje to: **pełna poprawna relacja komutatorowa nie gwarantuje jej poprawności po pośredniej projekcji**. To relacja algebraiczna, nie twierdzenie o TT w konkretnej teorii DTC.

## Świadectwo B: projektowany komutator zerowy, pełny niezerowy

H=R³, P=diag(1,1,0), A=[[0,0,1],[0,0,0],[1,0,0]], B=[[0,0,0],[0,0,1],[0,1,0]], T_b=0.

PAP=PBP=0, dlatego K_A^U=0. Jednak

K_B^U=P[A,B]P|_U = [[0,1],[-1,0]] ≠0

na U (norma 1). L_P^U=−K_B^U. Pokazuje to: **pozorne domknięcie komutatora po projekcji nie gwarantuje domknięcia pełnego operatora**. Oba operatory są symetryczne, więc przykład nie wykorzystuje nie-normalności źródłowych generatorów.

## Dokładny minimalny warunek kanału

Po dekompozycji H=U⊕U^perp, zapiszmy A w blokach A11=PAP, A12=PAQ, A21=QAP oraz analogicznie B. Wtedy L_P^U=B12 A21−A12 B21.

Jeżeli K_B^U=0, to K_A^U=0 wtedy i tylko wtedy, gdy B12 A21=A12 B21. Niezmienniczość U dla obu generatorów (A21=B21=0) jest warunkiem **wystarczającym, ale nie koniecznym**. Np. dla U=span(e1) w R², A=[[0,1],[1,0]], B=I+2A obie mapy wyprowadzają U do dopełnienia, lecz L_P=0.

Minimalny wymiar, w którym dwie kompresje w ogóle mogą nie komutować na U, to dim U≥2, a żeby U było właściwą podprzestrzenią, potrzeba dim H≥3. Świadectwo A jest więc wymiarowo minimalne.

## Znaczenie dla DTC i falsyfikator najtańszy źródłowo

Jeśli w konkretnej implementacji P=P_TT, A=T_C1, B=T_C2, T_b=T_[C1,C2], należy **osobno**:
1. zadeklarować klasę legalnych wejść (h∈U albo wejścia surowe);
2. zmierzyć K_B=P([A,B]−T_b)h;
3. obliczyć L_P=P(BQA−AQB)h przy tym samym P, masce i normie;
4. sprawdzić K_A−K_B−L_P jako kontrolę algebraiczną oraz blokowy warunek B12A21−A12B21 dla legalnej domeny;
5. dopiero po zdefiniowaniu porównania continuum i niezmiennej domeny próbować mówić o wierności operatora.

Świadectwa A i B pokazują, że ani mały K_A, ani mały K_B **bez drugiego kanału** nie certyfikuje drugiego. Historyczny stosunek RMS(K_B)/RMS(K_A) i ruchoma maska M13 to inne poziomy dowodu: źródłowe liczby norm skalarów nie identyfikują osobnych bloków operatorowych, a stabilny fixed-k slope nie jest fixed-domain convergence. DTC0a oryginalny runtime v0.3.1 nie jest tutaj odtworzony; nie ma nowego testu DTC na polach ani mechanizmu fizycznego.

## Niezależna kontrola i prior art

Obie macierze i tożsamości obliczono dokładną arytmetyką wymierną w SymPy (lokalny test symboliczy, nie dowód nowej matematyki). Dla świadectwa A wynikowa macierz antysymetryczna ma normę sqrt(1/3). Dla B algebra identycznie zwraca K_A=0, K_B=[[0,1],[-1,0]] i L_P=−K_B. MATURE HOST: kompresja operatorów/rozkład blokowy względem projektora, znane podstawy operator theory. Oryginalność nowej matematyki: NONE; wartość: dokładne dwustronne falsyfikatory **nielegalnego wnioskowania** na konkretnym interfejsie DTC.

## Próg ponownego otwarcia / stop

Reopen tylko gdy pojawi się zweryfikowany byte-exact DTC runtime + jawna klasa TT i porównanie norm lub kontrargument do algebraicznego zakresu, albo nowe źródło dowodzące cech bloku A12/A21 na rzeczywistej domenie modelu. Nie zlecać pracy innym komórkom bez faktycznej zależności. BW source-only, owner-currentness unchanged, no canon/no physics.
