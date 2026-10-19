# IW / M13 — ROT13: dokładny próg stabilności cyklu i rozdzielenie figur zysku ℓ² / ℓ∞


**RETURN_ID:** `M13-ROT13-NC011-FIXED-CYCLE-SCHUR-THRESHOLD-AND-NOISE-NORM-SPLIT-001_20261019`  
**CELL:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**DATE:** 2026-10-19  
**CLASS:** Dokładny wynik algebry liniowej dla stałego protokołu. Twierdzenia gospodarza: kryterium Schura/Jury'ego, gramian obserwowalności, systemy impulsowe.  
**CLAIM CEILING:** no CANON, EXEC_SIGN, novelty, physical quantum measurement, or new task.


## 0. Kontekst i subtraction


M13 ROT11 rozstrzygnął konieczność `μ₂(G)≤0` dla uniwersalnego sufitu `γ||c||₂≤1` w modelu pomiaru współosiowego. M13 ROT12 podał stabilny swobodny generator o niestabilnym cyklu pomiarowym i wykazał nieograniczenie obu norm zysku na horyzoncie nieograniczonym. W ROT12 wybrano tylko jedną siłę pomiaru (`a=1/2`). Obecny obrót znajduje **dokładną granicę stabilności** przy zmienianiu tylko siły, bez zmiany generatora, kierunku ani odstępu. Pozwala odróżnić wymagania modeli szumu z NC-010/011: `ℓ²` (wspólny budżet / niezależny szum gaussowski) oraz `ℓ∞` (adwersarialny szum ograniczony na każdy pomiar).


Nie jest to nowa teoria ani walidacja realizacji pomiarowej; to instancja kryterium Schura i obserwowalności. Priorytet ma poprawne typowanie i ograniczenie kwantyfikatorów.


## 1. Dokładna rodzina cykli


Z ROT12: `G=[[-1,4],[0,-1]]`, swobodnie Hurwitz, `μ₂(G)=1`, `u=(1,1)/√2`, `e=d=(1,-1)/√2`. W bazie `(u,e)`, `H=[[1,-2],[2,-3]]`. Ustalamy odstęp **h=1/4** i jednakowy kierunek, ale pozwalamy zmieniać `a=exp(-γs)` dla `0<a<1`.


Niech `z=exp(-1/4)`. Legalny jednocykliczny operator w bazie `(u,e)` to


```
B(a) = diag(1,a) exp(H/4)
     = z [[3/2, -1/2],
          [a/2,  a/2]].


trace B(a) = z(3+a)/2,
det B(a) = a z²,
p_a(1) = det(I-B(a)) = 1 - z(3+a)/2 + a z².
```


Wyraz `a/2` w dolnym wierszu jest istotny: w pierwotnym roboczym skrypcie błędnie wstawiono `a/4`, co dało niedopuszczalną wartość graniczną `a>1`; błąd usunięto przed zamrożeniem wyniku. Poprawny skrypt weryfikacyjny przechodzi równości symboliczne i wartości własne.


## 2. Granica jest jawna i ostra


Dla `z=e^(-1/4)` mamy `z²-z/2>0` oraz `3z/2-1>0`. Zatem równanie `p_a(1)=0` ma dokładnie jedno rozwiązanie w `(0,1)`:


```
a_c = (3z/2 - 1)/(z² - z/2)
    = 0.7746555835782724...


gamma*s_c = -ln(a_c) = 0.255336756693519...
```


Ponieważ `0<det B=a z²<1`, `trace B>0`, oraz `p_a(-1)=1+trace B+det B>0`, kryterium Jury'ego dla macierzy rzeczywistej 2×2 daje:


- `0<a<a_c`: `p_a(1)<0`, więc istnieje rzeczywista wartość własna `λ_+(a)>1` (druga jest dodatnia i mniejsza od 1). **Niestabilny cykl**.
- `a=a_c`: `λ_1=1`, `λ_2=a_c z²=0.4698523621578046...`, obie proste. **Cykl neutralny**.
- `a_c<a<1`: obie wartości własne są ściśle wewnątrz okręgu jednostkowego. **Cykl Schura**.


W szczególności `a=0.5` (mocniejszy pomiar, `γs=ln 2`) ma `λ_+=1.0828354214>1`, a `a=0.9` (słabszy pomiar) ma promień spektralny `≈0.93456094<1`. To jest efekt nieprzemienności tłumienia i nie-normalnej ewolucji; samo tłumienie jest kontrakcją.


## 3. Ścisłe rozdzielenie norm i kontraktów szumu


Niech `C(a)=(1-a) [0,1] exp(H/4)` będzie wierszem odczytu znormalizowanego przez `γ`, zaś `v_0` jest początkowym stanem jednostkowym w bazie `(u,e)`. Wtedy dla `j>=1`


```
gamma*c_j = C(a) B(a)^(j-1) v_0.
```


Dla `a<a_c` wybieramy własny wektor niestabilny; jego składowa odczytu jest **niezerowa**. Gdyby `C(a)v=0`, to `e^T exp(H/4)v=0`, zatem `Bv=exp(H/4)v=λv`. Sprzeczność: wszystkie wartości własne `exp(H/4)` są równe `z<1`, podczas gdy `λ>1`. W konsekwencji dla tego przygotowania `||c_1:k||∞` i `||c_1:k||₂` rosną wykładniczo.


**Na dokładnym progu** `a=a_c` to samo rozumowanie potwierdza niezerowość odczytu własnego wektora `λ=1`. Znormalizowany wektor ma w bazie `(u,e)` postać `(1,r_c)/√(1+r_c²)` z `r_c=3-2/z=0.43194916662452...`. Daje stały w każdym cyklu sygnał `γ*c_j = C_c`, gdzie `C_c=0.11535123786625...` (dodatni). Stąd:


```
gamma ||c_1:k||∞ = C_c,
gamma ||c_1:k||₂ = C_c sqrt(k) -> infinity.
```


A zatem **granica dla kontraktu ℓ² nie jest tą samą granicą co dla ℓ∞**. Przy neutralnym cyklu wielokrotne odczyty zwiększają normę zbiorczą, choć największy pojedynczy współczynnik pozostaje ograniczony. Wzrost `√k` nie oznacza automatycznej poprawy precyzji przy skorelowanym szumie; zależy od kontraktu informacyjnego.


Dla `a>a_c` macierz `B(a)` jest Schura, więc `||B(a)^j|| -> 0` geometrycznie (dla tego ustalonego `a`, `e` i `h`). Wtedy dla każdego znormalizowanego `v_0` i dowolnej liczby pomiarów `k`, zarówno `||c_1:k||∞`, jak i `||c_1:k||₂` są jednostajnie ograniczone. Nie twierdzimy, że ograniczenie jest jednolite po wszystkich `a>a_c` ani po wszystkich protokołach.


## 4. Granice i warunek decyzyjny


1. **Stały protokół:** jedna macierz `G`, jeden odstęp `h=1/4`, jeden kierunek `e=d`, stała siła `s`; całkowity horyzont rośnie `T=kh`.
2. **Niezerowy odczyt mody krytycznej:** to obok wartości własnej decyduje o zysku celu. Promień spektralny sam nie wystarczy dla dowolnego sensora; kryteria są *obserwowalnościowe*. Przy ustalonym `B,C`, bounded `ℓ²` dla wszystkich stanów równoważne zbieżności gramianu `Σ (B^T)^j C^T C B^j`. Dla obserwowalnych modów `|λ|>=1` gramian się rozbiega.
3. **Modele szumu:** `ℓ²` jest figurą dla wspólnego budżetu energii szumu lub niezależnego szumu gaussowskiego, natomiast `ℓ∞` występuje przy adwersarialnym ograniczeniu per odczyt. Nie utożsamiać norm i ich konsekwencji.
4. **Skończony horyzont:** dla każdej zadanej skończonej `T` wcześniejsze oszacowanie `γ||c||₂<=exp(max(μ₂(G),0)T)` z ROT12 nadal działa.
5. **Host/prior-art:** kryterium Schura, discrete-time observability Gramian, impulsive systems. Nie wystawiam nowego twierdzenia matematycznego ani nowego mechanizmu kwantowego.


## 5. Weryfikacja i zapis


`verify_rot13.py` oblicza symbolicznie `B(a)`, ślad, wyznacznik, próg i wektor własny przy `λ=1`; odtwarza wartości własne dla `a=0.5`, `a=a_c`, `a=0.9`; PASS. Źródła programu: NC-011, M13 ROT11, ROT12. Pierwsza robocza omyłka `a/4` została **jawnie zapisana jako negative knowledge** i poprawiona przed wydaniem.


NC-011: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-18/IW_NC_MEASUREMENT_CEILING_IS_THE_LOGARITHMIC_NORM_011_20261018.md


M13 ROT12: https://github.com/wmakiela-tech/Nash-iw-research/blob/84394a78910649e83cc3c28118fe057670903dcd/research/m13/2026-10-19/IW_M13_ROT12_stable_free_unbounded_measurement_gain_001.md


RETURN ROUTING: `IWTO_NC IWTO_MT13 IWTO_LT4 IWTO_REC9 IWTO_REC10 IWTO_INT7 IWTO_MODERATOR`.


**STATE:** `[▷] EXACT_ABSTRACT / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_NEW_TASK / REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD`.