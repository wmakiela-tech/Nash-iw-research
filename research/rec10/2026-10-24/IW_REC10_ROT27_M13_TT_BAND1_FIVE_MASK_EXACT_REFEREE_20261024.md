# IW/NASH — REC10 ROT27
## Niezależny certyfikat 3D Fourier-TT: pięć masek nie identyfikuje normy globalnej już dla pasma 1

**Data:** 2026-10-24  
**Komórka:** `IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10`  
**Problem:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001`  
**Werdykt:** `PASS_EXACT_FINITE_FIELD_CERTIFICATE / PASS_SOURCE_HELPER_DIRECT_SIXMODE_REPLAY`  
**Zakres:** źródłowo typowany model płaskich tensorów TT w siatce N=41, nie fizyczny model NCDG.  
**Ceiling:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / BW_PENDING`.

### 1. Pierwszeństwo wyników i źródło

**M13 ROT29** wykazał już nieidentyfikowalność pełnego RMS z pięciu masek przy paśmie 5 samej *gęstości energii* (niekoniecznie pasmowego tensora). **M13 ROT30** wykazał dokładny próg pasma tensorowego **2/3** dla pól zależnych wyłącznie od jednej współrzędnej. **REC10 ROT24 i ROT26** niezależnie recenzowały tamtą jednowymiarową klasę; nie wolno przenosić ich dodatniego progu 2 na pełną przestrzeń 3D. **M13 ROT31** (pierwszeństwo twierdzenia, niezależnie przeczytane źródło): `research/m13/2026-10-24/IW_M13_ROT31_full3D_TT_band1_mask_nonmap_001.md`, Git blob `db0effc7c45f2328c6f3db55df4224380442c507`. Wykazuje ostry próg **0/1** w ogólnej trójwymiarowej klasie Fourier-TT, wykorzystując sześciomodowy wyznacznik cyklotomiczny, i osobny lepiej uwarunkowany przykład 26-modowy.

Recenzja REC10 sprawdza dokładną algebrę **niezależnym kodem**, liczy dodatkowy wymierny gap dla konkretnej sześciomodowej normalizacji i uruchamia niezmieniony helper źródłowy na *zrekonstruowanej rzeczywistej parze*, zamiast opierać się tylko na wnioskowaniu z wyznacznika. Nie twierdzi nowości matematycznej.

### 2. Algebra dokładna: niezależny certyfikat modulo 821

Niech `k0=(-1,-1,0)`, `k1=(-1,-1,-1)`, `k2=(0,0,-1)`, `k3=(-1,1,-1)`, `k4=(-1,0,1)`, `k5=(-1,1,0)`. Dla `A=diag(0,1,-1)` definiujemy `B0=Pi_k0(A)` oraz `Bi=Pi_ki(B0)`, gdzie `Pi` jest **płaskim, euklidesowym projektorem Fourier-TT** na symetrycznych kowariantnych tensorach. Wszystkie składowe polaryzacji są wymierne, ślady i dywergencje znikają dokładnie.

Weź sześć realnych kosinusowych pól `bi(r)=Bi cos(2*pi*ki·r/41)`, `r=j-(20,20,20)` i zdefiniuj `D_(s,i)=<b0,bi>_Omega_s` dla s=0,2,3,4,5,6 oraz `Omega_s={s,...,40-s}^3`. Wpis macierzy jest iloczynem dokładnego Frobenius `B0:Bi` i symetrycznego iloczynu sum Dirichleta (kosinus-kosinus). Przesłanie pierwiastka 41. stopnia `ζ41` w `Q(ζ41)` do **159 modulo 821** jest poprawnym homomorfizmem na elementach, których mianowniki są jednostkami modulo 821: `159^41 ≡ 1 (mod 821)`, `159 != 1`, a 41 jest pierwsze. Wszelkie mianowniki `n_s=41-2s`, 2, 3 itd. są niezerowe w tym ciele.

Wynik niezależnego programu **bez importowania skryptu M13**:

```
       b0   b1   b2   b3   b4   b5
s=0    565    0    0    0    0    0
s=2    706  236  130  337  278   86
s=3     37  283  478  568  425  644
s=4    737  367  255  506  372  643
s=5    585  647   19  192  488  297
s=6     78   57  803  300  153  146

 det(D_full_6x6) (mod 821) = 247
 det(D_masks_5x5, cols b1..b5) (mod 821) = 804
```

Oba wyznaczniki są niezerowe. Zatem pięć równań `Σ_(i>=1)c_i D_(s,i)=-D_(s,0)` posiada jednoznaczne **rzeczywiste** rozwiązanie, ponieważ odpowiadająca macierz nad ciałem cyklotomicznym nie może mieć zerowego wyznacznika. Pola `u=b0`, `v=b0+Σc_i bi` mają `<u,v>_Omega_s=0` dla wszystkich pięciu masek, lecz `<u,v>_full=<u,u>_full>0` dzięki ortogonalności różnych modów pełnego okresu. W konsekwencji `Tplus=u+v`, `Tminus=u-v` mają identyczne wszystkie pięć RMS, ale różne globalne RMS.

**Niezależna korekta implementacyjna:** Pierwsza wersja *skryptu REC10* błędnie indeksowała polaryzacje w obliczaniu iloczynu Frobeniusa (zamieniona kolumna tensora z indeksem modu); jej wyznaczniki 434 i 738 były niezgodne ze źródłem. Po sprawdzeniu wzoru Frobeniusa poprawiono indeksowanie; pełna 6×6 tablica i oba wyznaczniki powróciły do zgodności bez zmiany źródła M13. Poprawiony wykonywalny skrypt jest artefaktem kanonicznym tej niezależnej kontroli; początkowej wersji NIE wolno używać jako falsyfikatora M13.

### 3. Nowa zamknięta kontrola wielkości kontrastu norm

Z algebry dokładnej otrzymano

```
 B0 = [[3/8,-3/8,0],[-3/8,3/8,0],[0,0,-3/4]]
 ||B0||_F^2 = 9/8.
```

Dla kosinusa niezerowego modu `<u,u>_full = (1/2)||B0||_F²=9/16` (znormalizowana średnia 3D). Ponieważ `R0(T)^2=(1/6)mean(|T|_F²)` i `T±=u±v`,

```
 R0(T+)² - R0(T-)² = (4/6)*<u,v>_full
                         = (4/6)*(9/16)
                         = 3/8.
```

To **różnica kwadratów** z konkretnej normalizacji; jej skala nie jest względną różnicą RMS. Jest dokładna i niezależna od wartości rozwiązania liniowego `c` (ale NIE od arbitralnego przeskalowania całej pary). Jest to wniosek/rozliczenie istniejącej konstrukcji M13, nie nowe twierdzenie dziedzinowe.

### 4. Drugi niezależny test na rzeczywistych siatkach i zachowanym helperze

W drugim skrypcie rozwiązano rzeczywisty układ 5×5 z 90-cyfrową precyzją mpmath, bez używania współczynników wygenerowanych wcześniej przez M13. Otrzymano:

```
 c1 = -832.9316332733830208734
 c2 = 3745.938861041417447937
 c3 = -11110.16212174182893961
 c4 = -1441.05296166593881296
 c5 = -1103.192965918771522809
 cond_2(D_masks) approx 239443.18
```

Zrekonstruowano pełne rzeczywiste macierze tensorów `T±` w siatce **41×41×41** i wywołano dosłownie niezmodyfikowane `rms_norm` i `apply_P_TT` z zachowanego helpera `deepseek_python_20260627_a87249.py`, którego SHA256 zweryfikowano jako `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`.

| maska | RMS(T+) | RMS(T−) |
|:--:|--:|--:|
| 2 | 867.7876422209903 | 867.7876422209903 |
| 3 | 864.1837156920045 | 864.1837156920045 |
| 4 | 863.7911454648555 | 863.7911454648555 |
| 5 | 867.6120008208525 | 867.6120008208525 |
| 6 | 876.5271145730466 | 876.5271145730466 |
| 0 | **880.754688251821** | **880.7544753661842** |

`R0(T+)²−R0(T−)²=0.375` z podwójną arytmetyką, zgodnie z dokładnym `3/8` w granicach podanej tolerancji; względne residua `apply_P_TT` rzędu `3.20×10^-16` i `2.90×10^-16` (oba TT). **Ważne:** ten sześciomodowy świadek jest źle uwarunkowany: wartości RMS ~881, a ich względna różnica wynosi około `2.42×10^-7` (czyli ~0.0000242%). Osobny NUMERYCZNY świadek M13 z 26 modów ma lepszą wykrywalność (`0.2706%`) i pozostaje jego wynikiem. Nie wolno sprzedawać wartości `3/8` jako dużego względnego efektu pomiarowego ani jako fizycznego kontrastu.

### 5. Werdykt, teoria gospodarz i ograniczenia

Werdykt wobec M13 ROT31: **PASS** dla twierdzenia, dokładności wyznaczników i istnienia rzeczywistej pary TT o zadanym paśmie. Podstawa: (i) dowód finite-field, (ii) 90-cyfrowy niezależny liniowy model, (iii) bezpośrednia kontrola zachowaną implementacją pełnosieciową.

Mature host: Fourier Gram matrices, finite-dimensional quadratic measurements, trigonometric polynomials, cyclotomic-field reduction and exact finite-field nonzero determinant certificates. Nie ma roszczenia nowości ani uprawnienia do modyfikacji kanonu.

**Nie wynika:** (a) analogiczna nieidentyfikowalność dla *konkretnej* rodziny tensorów residualnych historycznego generatora (`C1,C2,h,alpha`), (b) tensor TT oparty na ruchomej metryce/York, (c) efekt fizyczny NCDG, (d) błąd rzeczywistego `K_A` lub `J3/K` ani (e) byte-exact oryginalnego runtime `dtc0a_runtime_v0_3_1.py`. Nie mylić historycznej rekonstrukcji 99 norm M13 ROT23–27 z abstrakcyjnym ograniczeniem pięciu skalarnych danych.

Status: `INDEPENDENT_EXACT_CERTIFICATE_PASS / SOURCE_HELPER_PASS / NONBLIND / M13_OWNER / BW_PENDING / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE`. Żadnych nowych zadań dla innych komórek.