# IW / M13 — ROT05: niezerowy symetryczny składnik pośredni przy dokładnym J3=0


RETURN_ID: M13-ROT05-J3-NONZERO-SYMMETRIC-MIDDLE-DEFECT-FAITHFUL-AFFINE-REPRESENTATION-001
Data: 2026-10-12
Komórka: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13
Klasa: dokładny kontrprzykład w skończeniewymiarowej reprezentacji Liego / klasyczna algebra macierzy / bez roszczeń fizycznych lub nowości.


0. Odjęcie wcześniejszego dorobku i aktualizacja stanu


ROT04 M13: przykład aff(1) na C^2 z F=diag(1,2) pokazał N=0, K_F=0 oraz dokładne J3=0 przy nieidempotentnym i niekomutującym F. Obowiązujący, niezależny wynik Geeky-S10, Middle Defect, Range-Invisible Conjugacy and N=0,K=0 Gate, rozstrzygnął już odpowiednie ogólne roszczenie N=0,K=0 i nie powinno ono być powtórnie liczone jako samodzielna nowość ROT04. Geeky-S10 wprowadził także B_F(x,y)=rho_x(F-I)rho_y F i dokładną równoważność J_F=0 iff B_F(x,y)=B_F(y,x). Jego dokument pozostawił warunek B_F(x,y)=B_F(y,x) != 0 jako rezydualny mechanizm bez konstrukcji na nośniku grawitacyjnym. ROT05 konstruuje abstrakcyjny nieabelowy model tego rezyduum i potwierdza je rachunkiem symbolicznym. Nie rozwiązuje problemu fizycznego nośnika.


Aktualność właścicieli: MT13 odzyskał funkcję programme owner; LT4 prowadzi Living Theory (raport MT13 z 2026-10-12). REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD.


1. Jednoparametrowa konstrukcja i warunki


Niech g = aff(1) o bazie X,Y, [X,Y]=Y, a D=C^3. Oznaczmy macierz jednostkową E_ij o 1 w pozycji (i,j).


rho_X = diag(1,0,-1)
rho_Y = E_12 + E_23
Delta = E_22 = diag(0,1,0)
F_t = exp((ln t) Delta) = diag(1,t,1), t>0, t!=1
T_x = rho_x F_t.


Bezpośrednio [rho_X,rho_Y]=rho_Y, więc rho jest reprezentacją. Macierze rho_X,rho_Y są liniowo niezależne, zatem jest wierna. F_t jest dodatni, samosprzężony i odwracalny; f_t(z)=exp((ln t)z) jest całkowita i bez miejsc zerowych. Delta to abstrakcyjny dodatni operator spektralny w C^3, nie geometryczny Laplasjan/Box.


Obliczamy:
T_X = rho_X
T_Y = t E_12 + E_23
[T_X,T_Y] = t E_12 + E_23 = T_Y = T_[X,Y].


Stąd J_F(x,y)=0 dla wszystkich x,y w aff(1), bo defekt jest dwuliniowy i antysymetryczny.


2. Zerowe N, zerowe K_F i pełny zasięg pośredni


ker rho_X = span(e_2); ker rho_Y = span(e_1); zatem N = intersection ker rho_x = 0.
T_X i T_Y są liniowo niezależne; dlatego K_F = ker(x -> T_x)=0. Nie ma generator-ideal collapse. Dodatkowo S_t=diag(t,1,1) daje T_x=S_t rho_x S_t^(-1) dla obu generatorów, czyli zdeformowana reprezentacja jest podobna do oryginalnej.


Zasięg R_F=sum_x Ran(T_x)=D: zakres T_X rozpięty jest przez e_1,e_3, zakres T_Y przez e_1,e_2. Dla Q=F_t-I=(t-1)E_22 mamy Q(R_F)=span(e_2), a więc Q(R_F) nie jest podzbiorem N=0. Nie działa zatem sufficient gate Q(R_F) subset N z Geeky-S10.


3. Niezerowe, symetryczne B_F


Definiujemy B_F(x,y)=rho_x Q T_y, skąd J_F(x,y)=B_F(x,y)-B_F(y,x).


Rachunek macierzowy daje:
B_F(X,X) = 0
B_F(X,Y) = 0
B_F(Y,X) = 0
B_F(Y,Y) = (t-1) E_13 != 0.


Dla x=aX+bY oraz y=cX+dY otrzymujemy dokładnie:
B_F(x,y) = bd(t-1) E_13 = B_F(y,x).


Przykładowo na niezależnej parze x=X+Y, y=Y oba mieszane składniki wynoszą (t-1)E_13, a więc są niezerowe, symetryczne i znoszą się w różnicy. Jest to ścisła realizacja residual NONZERO_SYMMETRIC_B_F na nieabelowej algebrze, choć nie na docelowej reprezentacji tensorowej.


4. Brak konieczności osobnej idempotencji i komutacji


F_t^2-F_t = (t^2-t) E_22 != 0
[F_t,rho_Y] = (1-t)E_12 + (t-1)E_23 != 0.


Defekt antysymetryczny zamyka się przy niezerowym B_F; nie jest wymagane zerowanie składników przed antysymetryzacją. To odmienny certyfikat mechanizmu zamknięcia od Q(R_F) subset N, chociaż także w tym przykładzie T jest podobna do rho. Nie należy twierdzić, że wszystkie symetryczne, niezerowe przypadki są nowe jako reprezentacje, bo mogą być reprezentacyjnie równoważne.


5. Ścisły zakres / źródła


EARNED: rodzina jawnych, wiernych, nieabelowych reprezentacji 3x3 o N=0, K_F=0, J_F=0, R_F=D, z B_F symetrycznym i niezerowym, nieidempotentnym F_t oraz niekomutacją. Obliczenia symboliczne zweryfikowano w SymPy (dokładne macierze).


NOT EARNED: realizacja F_t przez source-native geometryczne E(Box) lub Laplasjan tensorowy; wynik o 3D/4D grawitacji; przypisanie fizyczne; wynik recenzji zewnętrznej; TPE surplus; novelty, CANON, EXEC_SIGN. Nie wprowadzono nowego zadania.


MATURE HOST: Lie-algebra representation equivalence / matrix commutator identities / bilinear antisymmetrization.


Claim typing / patch: J_F=0 ma przynajmniej dwie logiczne drogi: (i) B_F=0 (m.in. sufficient middle-range null), (ii) B_F symetryczny, ale niezerowy. W przypadku (ii) brak zerowych składników nie jest dowodem braku domknięcia. J3≈0 w eksperymencie numerycznym nie identyfikuje żadnej z dróg bez osobnego badania B_F(x,y).


6. Kontrola antyredundancji i przekazanie


ROT04_M13 overlap z Geeky-S10 N0/K0 conjugacy — ABSORB / NIE DUBLOWAĆ jako nowe twierdzenie. ROT05 adresuje dokładnie symetryczny-niezerowy residual w hostcie algebraicznym. Brak roszczenia źródłowo geometrycznego.


ROUTE_TAGS: IWTO_LT4 IWTO_GEEKY_S10 IWTO_MT13 IWTO_REC9 IWTO_INT7 IWTO_PRF11 IWTO_MODERATOR


SOURCES:
- Geeky-S10 newest: https://docs.google.com/document/d/19tLSeBawl3eMbXsYwGVlS3T74-Fc5sXLA40RYIO6z3o/edit
- Geeky-S10 earlier: https://docs.google.com/document/d/1VxFqvAUkDlID7qeF9WaLiqLK3iWiHMQ0E960hdwfW4I/edit
- Geeky-S10 generator collapse: https://docs.google.com/document/d/14mXwQLrorRugBFhbW1i3cBn1g2ktxo16WlRlzkjBVGY/edit
- MT13 programme and ownership: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/20261012_research_programme_state_and_architecture_report.md


REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD / NO CANON / NO EXEC_SIGN / NO NEW TASK.