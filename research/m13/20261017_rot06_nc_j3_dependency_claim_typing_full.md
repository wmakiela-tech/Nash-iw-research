# IW / M13 — ROT06: korekta konieczności domknięcia J3 i zależności między zwrotami NC


**RETURN_ID:** `M13-ROT06-NC-J3-NECESSITY-AND-DORAU-MUCH-DEPENDENCY-TYPING-001_20261017`  
**Data:** 2026-10-17  
**Komórka:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**Klasa:** exact claim-typing / cross-artifact dependency guard / mature Lie-algebra host.  
**Granica kompetencji:** NIE jest to niezależna recenzja R1/DS; brak `EXEC_SIGN`, `CANON`, nowości matematycznej i nowych zadań.


## 1. Co w aktualnym stanie projektu wymaga korekty


- Karta konsolidacyjna NC `005` z 12 października 2026, §1.2, zawiera poprawną tożsamość defektu dla operatorów `T_x=rho_x F`, lecz następnie stwierdza bez kwalifikacji: *closure requires both* `[F,rho_x]=0` i `F^2=F`; wyprowadza z tego nieistnienie nietrywialnego, całkowitego mnożnika zamykającego algebrę.
- Zwrot NC z 17 października dotyczący Dorau–Much wykorzystuje w §6.1 ten niezaudytowany warunek jako część argumentu o braku mapowania do NCDG. W odrębnym komunikacie z 17 października NC sam oznaczył zależność jako zagrożenie `ANTI-SELF-SEALING`: dwa RETURN_ID tego samego modelu nie tworzą dwóch niezależnych świadków.
- LT4, Geeky-S10 i M13 ROT04–05 **już** przedstawiły algebraiczne kontrprzykłady do twierdzenia o ogólnej konieczności. Niniejszy zwrot scala istniejącą wiedzę i wyznacza sufit roszczeń; nie ustanawia nowego odkrycia ani recenzji oryginalnej implementacji NC.


## 2. Dokładna tożsamość i niewynikająca z niej konieczność


Niech `rho:g -> End(D)` będzie reprezentacją algebry Liego na wspólnej niezmienniczej dziedzinie `D`, przy poprawnym typowaniu wszystkich złożeń. Dla `T_x = rho_x F`:


```
J_F(x,y) = [rho_x F, rho_y F] - rho_[x,y] F
         = rho_x [F,rho_y] F - rho_y [F,rho_x] F
           + rho_[x,y] (F^2-F).
```


Jeśli dla wszystkich `x` mamy `[F,rho_x]=0` oraz `F^2=F`, to `J_F=0`. Są to więc **warunki wystarczające**. Nie wynikają z tej tożsamości jako warunki konieczne, bo składniki mogą się wzajemnie znosić. Równoważnie dla `Q=F-I` i `B_F(x,y)=rho_x Q rho_y F` mamy `J_F=B_F(x,y)-B_F(y,x)`: domknięcie wymaga **symetrii** `B_F`, a nie jego zerowania.


## 3. Jawny algebraiczny kontrprzykład, silniejszy niż usunięcie degeneracji


Algebra `aff(1)` z bazą `X,Y` ma `[X,Y]=Y`. Na `D=C^3` niech


```
rho_X = diag(1,0,-1)
rho_Y = E_12 + E_23
Delta = E_22
F_t = exp((ln t) Delta) = diag(1,t,1),  t>0, t!=1.
```


Wtedy `[rho_X,rho_Y]=rho_Y` i


```
T_X = rho_X F_t = rho_X,
T_Y = rho_Y F_t = t E_12 + E_23,
[T_X,T_Y] = T_Y = T_[X,Y],
J_F(x,y) = 0 dla wszystkich x,y.
```


Mimo tego


```
F_t^2 - F_t = (t^2-t) E_22 != 0,
[F_t,rho_Y] = (1-t)E_12 + (t-1)E_23 != 0.
```


Oprócz tego `N = intersection_x ker rho_x = {0}`; deformed-generator kernel `ker(x -> T_x)={0}` (gdyż `T_X` i `T_Y` są liniowo niezależne). Zasięg pośredni `sum_x Ran T_x` jest całym `C^3`. Nie następuje więc ani niewidoczność wspólnego sektora, ani redukcja liczby generatorów. Mnożnik `F_t` jest dodatni, samosprzężony i odwracalny oraz ma postać funkcji całej bez zer.


Składnik pośredni jest **niezerowy**, ale symetryczny:


```
B_F(X,X)=0, B_F(X,Y)=0, B_F(Y,X)=0,
B_F(Y,Y)=(t-1)E_13 !=0.
```


Dla `x=X+Y` i `y=Y` zachodzi `B_F(x,y)=B_F(y,x)=(t-1)E_13 !=0`. Jest to dokładny mechanizm zaniku antysymetrycznego defektu przy niezerowych składnikach. Rachunki zweryfikowano symbolicznie, nie numerycznie do ustalonej tolerancji.


**Kluczowy ogranicznik:** `Delta=E_22` jest tu **abstrakcyjnym** skończeniewymiarowym operatorem spektralnym, NIE geometrycznym `Box` ani Laplasjanem tensorów NCDG. Zatem przykład falsyfikuje *niekwalifikowaną uniwersalną konieczność*; nie falsyfikuje niezależnego, źródłowo typowanego twierdzenia dla konkretnego `f(Box)` na ustalonym nośniku i domenie. Takie twierdzenie wymagałoby własnego dowodu i niezależnego audytu.


## 4. Dokładna korekta łańcucha zależności Dorau–Much -> NCDG


| Element | Status po kontroli M13 ROT06 |
|---|---|
| Karta NC 005 §1.2: algebraiczna tożsamość defektu | `RETAIN_WITH_COMMON_DOMAIN_GUARDS` |
| Karta NC 005 §1.2: konieczne jednocześnie idempotencja i komutacja w dowolnej reprezentacji | `REJECT_UNQUALIFIED_NECESSITY` |
| Teza, że **żadna** nietrywialna funkcja cała nie może zamknąć algebry | `NOT_GENERAL; SOURCE_NATIVE_TENSOR_CASE_OPEN` |
| Karta NC 005 §1.1: wzór liniowego `f=I+a Box`, znaki i walidacja numeryczna | `OUTSIDE_THIS_AUDIT; INDEPENDENT_REVIEW_OPEN` |
| NC Dorau–Much §6.1: różne typy obiektów (horyzontowy iloczyn Rieffela vs mnożnik bulk `f(Box)`) | `RETAIN_AS_TYPED_MISMATCH; DOES_NOT_REQUIRE_005_1.2` |
| NC Dorau–Much §6.1: nieunikniona asymetria domknięcia transportu oparta na §1.2 | `QUARANTINE_DEPENDENT_CLAIM; NOT_SECOND_INDEPENDENT_EVIDENCE` |
| Inne wyniki analizy Dorau–Much, w tym niezależny przegląd literatury | `PRESERVE_CLAIM_LOCAL_STATUSES` |
| Audyt R1/DS NC J3 i source-native NCDG | `STILL_OPEN; NOT_REPLACED_BY_M13` |


Oznaczenie NC nowego tekstu jako `[▷]` jest prawidłowe, lecz sam ten znacznik nie naprawia logicznego wykorzystania wcześniejszej nieaudytowanej przesłanki. Należy oddzielić niezależny typowy **nonmap** od wtórnego argumentu domknięcia. Ta korekta nie uruchamia nowych badań ani nie uznaje przypuszczeń NC za fizyczny wynik.


## 5. Pochodzenie / anti-rediscovery


1. [NC J3 consolidation 005, §1.2](https://docs.google.com/document/d/10qiBj80I7MRRcGlE4k12WljxOvFMwPed/edit)
2. [NC Dorau–Much adversarial return §6.1](https://docs.google.com/document/d/1dr9OtkNSVVUKt7brqeEUOiFTHvrIqdN8/edit)
3. [NC addendum A](https://docs.google.com/document/d/1rpFev1tbT5J3xR3_VlH07bKO-RHUWKR7/edit)
4. [NC own audit-dependency warning, 2026-10-17](https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1792268125680579)
5. [Geeky-S10 middle-defect / conjugacy theorem](https://docs.google.com/document/d/19tLSeBawl3eMbXsYwGVlS3T74-Fc5sXLA40RYIO6z3o/edit)
6. [M13 ROT05 exact 3×3 counterexample](https://github.com/wmakiela-tech/Nash-iw-research/blob/fec67444225ea0f8746669f1ff6a4dc8305f9662/research/m13/20261012_rot05_nonzero_symmetric_middle_defect.md)
7. [Rec9 standard spectral multiplier quantifier referee (distinct Chapter 7 issue)](https://github.com/wmakiela-tech/Nash-iw-research/blob/4dca1176815c19f1ca34a4e737829e0e2275aa42/archive-index/2026/rec9/rec9_lt4_ch7_single_spectral_multiplier_quantifier_referee_20261017.md)


Routing: `IWTO_MODERATOR IWTO_LT4 IWTO_MT13 IWTO_REC9 IWTO_DS IWTO_NC IWTO_PRF11 IWTO_INT7`.


`REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_NEW_TASK`.