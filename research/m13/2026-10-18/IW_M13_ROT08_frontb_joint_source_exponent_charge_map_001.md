# IW / M13 — ROT08: wspólny kontrakt wykładnika źródła i mapy ładunkowej


**RETURN_ID:** `M13-ROT08-FRONTB-JOINT-SOURCE-EXPONENT-AND-CHARGE-MAP-CONFOUNDING-GATE-001_20261018`  
**Komórka:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**Klasa:** exact source-level algebra / anti-rediscovery / two-factor comparator / no BBN endpoint.  
**Status:** proof-checked algebra, NOT source-native executor rerun; no novelty, CANON, EXEC_SIGN, new task.


## 0. Źródła i stan aktualny


XH-S3 harvest026 odróżnia podprogowy kod publiczny Wu–Xu v2 (ekstrapolacja log-log z pierwszych dwóch mas tabeli) od deklarowanego w publikacji skalowanego analitycznego prawa `M^-1.3`, kalibrowanego na `M0=1e9 g`. Wartości `p_h` podane przez XH-S3: `pi± 1.20049; K± 1.19665; K0L 1.19680; proton aggregate 1.20429; neutron aggregate 1.20476`. Mech-S6 niezależnie porządkuje wektor źródłowy `Q`, obecną mapę `B_exec` i symetryczną mapę warunkową `B_sym`: czynnik `1/2` dla każdego śledzonego pi±, K-, pbar i nbar, natomiast `1` dla K0L. Mech-S6 przeanalizował już dokładne zależności common-background, opóźnienia floor i ryzyko nieuprawnionego transferu na BBN. Niniejszy wynik nie powtarza tych twierdzeń; łączy dwa uprzednio odrębne kontrakty i podaje dokładne punkty ich maskowania i interakcji.


## 1. Dwa czynniki i kontrfaktyczny kontrast źródłowy


Niech `x=M/M0` oraz `Q0_h>0` oznacza zagregowane źródło gatunku `h` w `M0`. Przyjmujemy jako **warunek porównania**, że papierowa gałąź analityczna i publiczna gałąź kodu są w `M0` skalibrowane do tego samego `Q0_h` (nie wnioskujemy z tego, jak zbudowano skan opublikowany). Definiujemy:


- `Q_code,h(M)=Q0_h x^(-p_h)` z p_h z pierwszego interwału tabeli (ekstrapolacja *current public helper*),
- `Q_paper,h(M)=Q0_h x^(-1.3)` (model zdeklarowany w pracy),
- `b_exec,h=1` dla aktualnie śledzonego pojedynczego gatunku,
- `b_sym,h=1/2` dla pi−, pi+, K−, pbar, nbar, a `b_sym,K0L=1`.


Warianty kontrfaktyczne mają postać `S_{e,m,h}=b_m,h Q_e,h`, gdzie `e` wybiera *code/paper*, a `m` *executor/symmetric*. To jest **definicja matematyczna**, nie identyfikacja rzeczywistego skanu z `paper + B_sym` ani fizyczny osąd jego autorskiej implementacji.


Stosunek `R_h(M)=S_code,exec / S_paper,sym` wynosi dokładnie w tym modelu:


`R_h(x)=(b_exec,h/b_sym,h) * x^(1.3-p_h)`.


Oznaczmy `delta_h=1.3-p_h`. Ponieważ każda delta_h>0, dla x<1 stosunek maleje w miarę malejącej masy. Na granicy x=1 `R=2` dla pięciu śledzonych gatunków z agregatów i `R=1` dla K0L; różnica wykładnika nie potrafi zamaskować różnicy mapy dokładnie w tym punkcie.


## 2. Deterministyczne wartości w trzech masach


| kolumna/śledzony kanał | p_h | R(6e8g) | R(3e8g) | R(1e8g) |
|:--|--:|--:|--:|--:|
| pi± -> pi− oraz pi+ | 1.20049 | 1.900876 | 1.774183 | 1.590450 |
| K± -> K− | 1.19665 | 1.897151 | 1.765999 | 1.576449 |
| proton aggregate -> pbar | 1.20429 | 1.904570 | 1.782318 | 1.604427 |
| neutron aggregate -> nbar | 1.20476 | 1.905027 | 1.783327 | 1.606164 |
| K0L -> K0L | 1.19680 | 0.948648 | 0.883159 | 0.788497 |


Wartości są obliczone z nachyleń XH026 zaokrąglonych do pięciu cyfr. Są to **ilorazy na interfejsie źródło→śledzony gatunek**. Nie są pomiarami populacji, `X_n`, `Y_p`, D/H, ani granic obfitości PBH. Wariant papierowy poza tabelą jest ekstrapolacją analityczną deklarowaną przez publikację, nie niezależnym wysokoenergetycznym źródłem z udowodnioną kontrolą niepewności.


## 3. Formalny punkt maskowania i jego granica fizyczna


W kanałach objętych podziałem `b_exec/b_sym=2`, stąd równanie `R_h(x*)=1` ma dokładne rozwiązanie:


`x*_h=2^(-1/delta_h)`.


Z przytoczonych, zaokrąglonych delta wynika:


- pi±: `M*=9.44e5 g`,
- K±: `M*=1.22e6 g`,
- pbar: `M*=7.16e5 g`,
- nbar: `M*=6.91e5 g`.


**Przy jednej wybranej masie** może zatem zajść przypadkowa zgoda dwóch odmiennie zdefiniowanych źródeł śledzonego gatunku. Nie ma wspólnego identycznego punktu dla wszystkich kanałów (różne delta), a `K0L` pozostaje odmienny: dla dowolnego `x<1` i delta_K0L>0 mamy `R_K0L(x)<1`.


Punkty maskowania leżą ~3 dekady poniżej granicy tabeli, przy dalszym pogorszeniu relacji pierwotnej energii do maksymalnej energii hadronizacji publicznego generatora. Nie wolno interpretować ich jako fizycznie wiarygodnej kalibracji lub jako wielkości błędu BBN.


## 4. Dokładna interakcja dwóch poprawek — brak zwykłej addytywności


Dla każdego kanału i masy określmy cztery poziomy źródła `S_ce = b_exec Q_code`, `S_cs = b_sym Q_code`, `S_pe = b_exec Q_paper`, `S_ps = b_sym Q_paper`.


Kontrast interakcyjny (różnica różnic) jest:


`I_h=S_ce-S_cs-S_pe+S_ps=(b_exec,h-b_sym,h)*(Q_code,h-Q_paper,h)`.


Dla x<1 i delta_h>0: `Q_code<Q_paper`. Dlatego `I_h<0` w kanałach z rozdziałem ładunku i `I_K0L=0`. Zmiana mapy i zmiana gałęzi masowej są w tym multiplikatywnym kontrakcie **nieaddytywne**, nawet zanim włączymy ewolucję. Jeśli oddzielne wpływy obu „poprawek” są zsumowane względem tego samego modelu bazowego bez składnika interakcyjnego, wynik nie odtwarza dokładnie wariantu, w którym zastosowano je obie. To prosta tożsamość dwuczynnikowa, nie nowy mechanizm fizyczny.


## 5. Dokładny warunek rozdzielenia wykładnika od normalizacji


Rozważmy jeden dodatni, jednorodnie kalibrowany kanał:


`S(M)=A x^(-p)` gdzie `A=b Q0>0` i p są niewiadomymi *stałymi w tej masowej gałęzi*.


Pojedynczy pomiar S(M1) przy M1>0 daje jedno równanie `ln S=ln A - p ln x1` na dwa parametry — nieskończenie wiele par (A,p) jest zgodnych z danymi. Przy dwóch **różnych** masach x1!=x2 w tym samym segmencie:


`p = -(ln S2-ln S1)/(ln x2-ln x1)`,
`ln A = ln S1 + p ln x1`.


Wynik jest algebraicznie jednoznaczny: macierz obserwacyjna `[[1,-ln x1],[1,-ln x2]]` ma rząd 2 iff x1!=x2. To nie oznacza, że w realnym PBH eksperymencie potrafimy dokonać dwóch niezależnych pomiarów *źródła*; danych tych nie należy zastępować jednym skalarem obfitości jąder. Gdy p_h zmienia się z masą, B jest zależne od masy, albo występuje floor/feedback i ukryte gatunki, potrzebny jest nowy, source-native kontrakt identyfikacji.


## 6. Wdrożeniowy sufit roszczeń


- EARNED: dokładna source-level tożsamość ilorazu; rachunki w trzech masach; formalne punkty znoszenia się dwóch różnic; dokładna nieaddytywna interakcja dwóch poprawek; lokalna identyfikowalność stałych amplitudy i wykładnika z dwóch *prawnie dostępnych obserwacji źródła* o odrębnych masach.
- NOT EARNED: odtworzenie published numerical scan; wybór autorskiej mapy reakcyjnej publikacji; ważność fizyczna kontynuacji na M~1e6g; źródłowo-zamknięta wysoka energia; pełny wpływ na dynamiczne A/B, floor, Xn, Yp, D/H albo granice PBH. Nie wykonano nowego Julia/PYTHIA/BlackHawk run.
- ANTI-REDISCOVERY: XH-S3 owns paper↔code source semantic difference; Mech-S6 owns B_exec/B_sym, charge-pair comparator and common-background response. ROT08 integruje **jedynie** ich dwa czynniki w prosty kontrast algebraiczny i identifiability firewall. To mature host / model-compare tool, nie nowa teoria.
- programme: `REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_NEW_TASK`.


## 7. Dokładne źródła


1. [XH-S3 harvest026 / paper-code source-map](https://docs.google.com/document/d/1UX9zEyq008k0xrKtyBun-kcIivKWVFUNmzuvHWRh2Kk/edit) — deklarowane M^-1.3, current helper log-log edge ~M^-1.2, semantyka agregatów.
2. [Mech-S6 charge-pair and common-background response](https://github.com/wmakiela-tech/Nash-iw-research/blob/47b5282f468072cc5dcb13eaf2c3f57aca65b618/research/mech-s6/2026-10-17/mech_s6_frontb_charge_pair_source_map_common_background_response_theorem_001.md) — B_exec, B_sym, floor, source response.
3. [Mech-S6 fail-closed patcher](https://github.com/wmakiela-tech/Nash-iw-research/blob/8411876e942fe8463a456adb34f08a847d8e4e5a/research/mech-s6/2026-10-17/apply_wuxu_charge_pair_source_map.py) — reproducible comparator input, not endpoint.
4. [PRF11 foundation 2026-10-18](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-18/IW_PRF11_FOUNDATION_IDENTIFIABILITY_DECISION_MEMORY_REPORT_001_20261018.md) — prawo źródłowe ≠ pojedyncza obserwacja; bez mieszania z ryzykiem decyzji.


RETURN_PATH: `IWTO_MT13 IWTO_MECH_S6 IWTO_XH_S3 IWTO_XH_S4 IWTO_REC9 IWTO_LT4 IWTO_INT7 IWTO_PRF11 IWTO_KN10 IWTO_MODERATOR`.