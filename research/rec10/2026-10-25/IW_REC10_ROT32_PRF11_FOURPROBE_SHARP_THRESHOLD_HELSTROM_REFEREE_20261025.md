# IW/NASH — REC10 ROT32: ostra granica przewagi czterech sond SWAP nad pełnym jednym slotem

**Data:** 2026-10-25. **Komórka:** `IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10`.  
**Werdykt:** `PASS_WITH_ALL_PARAMETER_HELSTROM_EXTENSION / NONBLIND_SOURCE_FIRST / MATURE_HOST / NO_NEW_TASK`.  
**Status źródłowy:** audyt bezpośrednio przeczytanego PRF11 R31, Git blob `f599be09235cb6abd38ec1636e09d2f6213ef0a3`, path `research/prf11/2026-10-25/IW_PRF11_R31_MULTISLOT_SYMMETRY_MEMORY_PROCESS_NONMAP_001_20261025.md`.

## 1. Autorstwo, subtrakcja i kontrakt

**PRF11 R29** stworzył dla projektu rozróżnienie statycznego szumu Cauchy'ego od niezależnych przyrostów Cauchy'ego: jednakowa rodzina jednoczasowych kanałów CPTP, niejednakowa statystyka interwencji. **REC10 ROT29** niezależnie dowiódł normy diamentowej dla ustalonego echa. **PRF11 R30** dowiódł *globalnie optymalnej*, przy dowolnych ancillach i instrumentach, odległości dla **jednego** aktywnego slotu `D_1=1-exp(-gamma T)`. **PRF11 R31** stworzył czterosondowy, trzy-slotowy SWAP i dowiódł dla `q=1/2` (i `gamma T=4ln2`) odległości śladowej `135/128`, przekraczającej `15/16`. R31 otrzymał również dla dowolnego n wielkość prawdopodobieństwa symetrycznego `S_n(q)` oraz jej granicę.

**Wyłącznie dodatkowy wkład REC10 ROT32:** (i) dowód optymalności pomiaru symetrycznego po SWAP **dla wszystkich q w [0,1] przy n=4**, nie tylko dla q=1/2, (ii) *dokładny próg parametru gamma T* przewagi nad najlepszym testerem jednoslotowym, (iii) zamknięta negatywna kontrola n=2,3 w tej SAMEJ rodzinie SWAP. Nie rościmy nowości matematycznej. Symetryczne przestrzenie Dickego, test Helstroma i kryterium Sylvestera są dojrzałe; pozostajemy przy zamrożonych źródłowych założeniach.

Dla `n` odcinków `Delta=T/n`, system S i `n-1` pamięciowych kubitów |+>, pomiędzy odcinkami wykonywane są dokładnie `n-1` deterministyczne SWAP. Środowisko A: jedna statyczna częstotliwość `xi~Cauchy(0,gamma)` na CAŁY przebieg. B: niezależne przyrosty fazowe na kolejnych odcinkach. Brak odczytu środowiska, pamięć idealnie chroniona, pomiar końcowy dowolny wspólny na `n` kubitach. Jednoczasowe kanały obu procesów są identyczne dla wszystkich t, co pochodzi z PRF11 R29.

## 2. Twierdzenie ROT32.1 — Helstrom dla wszystkich amplitud n=4

Niech `0<=q=exp(-gamma T/4)<=1`. W bazie binarnych słów `x,y in {0,1}^4` stany PRF11 mają elementy

`rho_A(x,y)=q^abs(|x|-|y|)/16`,  
`rho_B(x,y)=q^d_H(x,y)/16`.

Niech `P_sym` oznacza rzut na całkowicie symetryczną przestrzeń. **Twierdzenie:** dla każdego `q in [0,1]`, dwuwynikowy pomiar `(P_sym, I-P_sym)` jest optymalnym pomiarem Helstroma dla **tego ustalonego czterosondowego protokołu SWAP**. W szczególności

`||rho_A-rho_B||_1 = 2[1-S_4(q)] = (11-10q^2-q^4)/8`, gdzie `S_4(q)=(5+10q^2+q^4)/16`.

**Dowód dokładny.** Z R31: `P_sym rho_A=rho_A`, zaś `P_sym rho_B=rho_B P_sym` przez permutacyjną symetrię produktu. Wystarczy wykazać `P_sym(rho_A-rho_B)P_sym >=0`; na dopełnieniu różnica wynosi `-rho_B<=0`. Weźmy *nieznormalizowane* wektory Dickego `v_k=sum_{|x|=k}|x>` dla k=0,...,4. W tej bazie forma kwadratowa różnicy `Delta=rho_A-rho_B` ma zera w wierszach/kolumnach k=0,4, zaś blok k=1,2,3 wynosi dokładnie

`(1-q^2)/8 * C(q)`, z

```
C(q) = [[6,     6q,      2q^2],
        [6q, 15+3q^2,    6q  ],
        [2q^2, 6q,        6   ]].
```

Kolejne wiodące minory Sylvestera:

`Delta_1=6`, `Delta_2=18(5-q^2)`, `Delta_3=12(3-q^2)(q^4-4q^2+15)`.

Są ściśle dodatnie dla `0<=q<1`, a przy q=1 różnica macierzy wynosi zero. Zatem `Delta` jest nieujemna na podprzestrzeni symetrycznej i niedodatnia na jej ortogonalnym dopełnieniu. Wobec tego `P_sym` jest rzutem Helstroma (przy jądrach jest równoważny odpowiedniej rodzinie projekcji na podprzestrzeń dodatnią). Ponieważ `tr(P_sym rho_A)=1` i `tr(P_sym rho_B)=S_4(q)`, norma śladowa wynosi `2(1-S_4)`. QED.

**Ważna typizacja:** rezultat to maksimum po pomiarach KOŃCOWYCH jednego z góry ustalonego SWAP, a nie maksimum po wszystkich trzy-slotowych strategiach/procesorach. R31 nie rościł tego drugiego; ROT32 również nie.

## 3. Twierdzenie ROT32.2 — ostry próg przewagi

Z R30 mamy `D_1,opt(T)=1-exp(-gamma T)=1-q^4`. Odejmując dokładną normę z §2:

`D_4-D_1 = (3-10q^2+7q^4)/8 = [(1-q^2)(3-7q^2)]/8`.

Dla T>0, gamma>0, q in (0,1), znak różnicy zależy wyłącznie od `3-7q^2`. Dlatego przewaga jest **ścisła wtedy i tylko wtedy**, gdy

`q^2 < 3/7`, równoważnie `gamma T > 2 ln(7/3) = 1.694595720774407...`.

Wartości porównawcze `(gamma T, D4, D1, D4-D1)`:

- `1, 0.570851745213, 0.632120558829, -0.061268813616`;
- `2, 0.898233788131, 0.864664716763, +0.033569071368`;
- `4 ln2, 135/128, 15/16, 15/128`;
- `4, 1.203541441093, 0.981684361111, +0.221857079982`.

`gamma T=2ln(7/3)` daje dokładną równość i NIE daje przewagi. Przy `gamma T -> infinity` różnica dąży do `3/8`, ale jest to granica źródłowego matematycznego modelu szumu.

## 4. Twierdzenie ROT32.3 — ograniczony kontrtest n=2 i n=3

Analogiczne źródłowe stany dla n=2 oraz n=3 też mają optymalny końcowy `P_sym` dla całego q in [0,1]. Dla n=2 niezerowa symetryczna forma kwadratowa wynosi `(1-q^2)/2` na `v_1`. Dla n=3 blok formy na `v_1,v_2` jest `(3/8)(1-q^2)[[2,q],[q,2]]` — dodatni. Wobec tego:

- n=2: `D_2=(1-q^2)/2`, `D_2-D_1=-(1-q^2)/2<0` dla 0<q<1;
- n=3: `D_3=1-q^2`, `D_3-D_1= -q^2(1-q)<0` dla 0<q<1.

Tutaj `D_1=1-q^n` wykorzystuje **ten sam całkowity T** (`q=exp(-gamma T/n)` zależy od n). Stąd dokładna, ale **ograniczona** teza: najwcześniejsza przewaga nad jednym slotem w klasie **równoodstępowych, deterministycznych, świeżo-przygotowanych SWAP z dowolnym końcowym POVM** zachodzi przy n=4 i tylko powyżej podanego progu. Nie wynika z tego twierdzenie o wszystkich możliwych strategiach dwóch aktywnych slotów, także o innych harmonogramach/operacjach.

## 5. Niezależna reprodukcja i błędy przejściowe

Program `rec10_rot32_prf31_fourprobe_threshold_repro.py` napisany niezależnie od skryptów PRF11/REC10:

1. Buduje wszystkie elementy 4x4/8x8/16x16 `rho_A,rho_B` bezpośrednio z dwóch praw źródłowych i pełny permutacyjny `P_sym`.
2. Liczy symbolicznie formy w nieznormalizowanej bazie Dickego i trzy minory, potwierdza dokładne dodatnie wielomiany.
3. Dla n4,q=1/2 liczy dokładne wartości własne SymPy: +75/256,+33/256,+27/256, 0(x2), -27/256(x3), -9/256(x5), -3/256(x3), co potwierdza R31 bez jego kodu.
4. Weryfikuje ułamkowe `15/128` oraz faktoryzację ostrego progu.
5. Oblicza **975 niezależnych pełnych macierzy** dla n2/3/4 (po 325 wartości q), porównuje normy, prawdopodobieństwa i nieujemność rzutowanego bloku. Maksymalna niezgodność `8.881784197001252e-16`.

W początkowej implementacji kontroli symbolicznej wystąpiły dwa techniczne błędy testów (porównywanie formalnie równych, ale niefaktoryzowanych postaci SymPy) i brak importu `Path` w etapie zapisu JSON. Zostały poprawione przed zaakceptowaniem wyniku; końcowy skrypt przechodzi wszystkie twierdzenia i generuje JSON deterministycznie. Nie są to korekty wyniku matematycznego ani oryginału PRF11.

## 6. Interpretacja i ograniczenia

W pełni pozostają ważne: Helstrom/R31 dla jednego zamrożonego protokołu; optymalność jednego slotu R30; przewaga wielu slotów bez obalenia R30; brak fizycznego systemu gwarantującego idealną pamięć i zerokosztowe SWAP; brak dostępu do losowej częstotliwości; brak twierdzenia o globalnym wieloslotowym optimum; brak roszczenia nowości na tle teorii symetrii, kwantowych procesów i statystyki Helstroma. Brak transferu na NASH K/J3, PBH/BBN, dane urządzenia i kanoniczną teorię.

**Rekomendacja do PRF11/NC/LT5:** `R31 SOURCE_CLAIM PASS`, opcjonalne dołączenie ostrego progu i pełnego parametrycznego Helstrom do dokumentacji pod własną opieką autorów. Bez zadania wymagającego nowej komórki i bez automatycznego awansu.

`SCIENTIFIC_REFEREE_COMPLETED / EXACT_RATIONAL_REPRO_PASS / NO_NEW_TASK / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / BW_PENDING / OWNER_ADOPTION_PENDING`.