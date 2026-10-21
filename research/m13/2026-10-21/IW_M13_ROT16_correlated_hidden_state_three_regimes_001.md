# IW / M13 — ROT16: skorelowany sektor ukryty, pełny port sterowania i dokładne trzy fazy minimaksu

**RETURN_ID:** `M13-ROT16-CORRELATED-HIDDEN-TARGET-THREE-REGIME-CHEBYSHEV-001_20261021`  
**CELL:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**DATE:** 2026-10-21  
**CLASS:** dokładna specjalizacja warunkowa klasycznej geometrii minimaksowej / constrained Chebyshev center / no physical claim.  
**STATUS:** `EXACT_ABSTRACT / MATURE_HOST / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK / TPE HOLD`.

## 0. Aktualność i odejmowanie nowości

Najnowszy LT5, `LT5-VECTOR-TARGET-CONSTRAINED-CHEBYSHEV-DUAL-001` (21 października 2026), udowodnił ogólną tożsamość posteriorowego constrained center oraz dualny wzór `r_D(T)^2=max_μ[Var_μ(T)+dist(E_μ t,D)^2]`, przyzwalając na dowolne zwarte, wypukłe posteriorowe zbiory celu i aktuatora. Jego przykład dwuwymiarowego nieobserwowanego odcinka pokrywa M13 ROT14, a twierdzenie ogólne obejmuje także model ROT15. **ROT14–15 są odtąd traktowane jako źródłowo wtórne, jawne przypadki ogólnej teorii LT5; nie zgłaszać dwóch niezależnych odkryć.**

Obrót ROT16 wykorzystuje twierdzenie gospodarza LT5 do rozwiązania w zamkniętej postaci *innego*, skorelowanego posterioru: obserwacja pierwszego komponentu ujawnia środek drugiego, zaś niezależna niepewność drugiego pozostaje. Celem jest ścisłe znalezienie progów polityki w funkcji amplitudy, nie poszerzenie kanonu.

## 1. Model typowany

Stan celowy w rzeczywistej przestrzeni euklidesowej R² ma postać

    y=(x, k x+w),   |x|<=1, |w|<=H,

z `H>=0` i `k` ustalonym, znanym parametrem sprzężenia. Dostępny jest **dokładny i nieinwazyjny** pomiar `b=x`; po jego uzyskaniu regulator wybiera dowolny wektor `u(b)∈R²` o normie euklidesowej `||u(b)||₂<=B` i chce minimalizować terminalną normę `||y+u(b)||₂`. Nie występują inne ograniczenia ani szum obserwacji, sprzężenie aktuatora z późniejszą dynamiką, ani back-action pomiaru. Problem:

    J*(B;k,H)= inf_{u(.): ||u(b)||₂<=B}
                sup_{|x|<=1,|w|<=H}||(x,kx+w)+u(x)||₂.

Przez izometryczną zmianę znaku drugiej współrzędnej wystarczy rozważyć `k>=0`; poniżej `k=|k|`.

## 2. Redukcja do jednej warunkowej optymalizacji

Dla danego `x` posterior celów to pionowy odcinek `T_x={(x,kx+w):|w|<=H}`. Wygodnie opisać **dodatnią korektę** `d(x)=-u(x)` (ta sama kula budżetowa). Dla `x=1`:

    max_{|w|<=H}||(1,k+w)-d||²
       =(1-d₁)²+(H+|k-d₂|)².                    (1)

Niech `d*` minimalizuje (1) na `||d||<=B`. Reguła `d(x)=x d*` jest dopuszczalna, bo `|x|<=1`, i dla każdego `x` daje błąd nie większy niż w `x=1`:

    max_w||(x,kx+w)-x d*||²
      =x²(1-d₁*)²+(H+|x| |k-d₂*|)²
      <=(1-d₁*)²+(H+|k-d₂*|)².

Ponieważ przeciwnik może wybrać `x=1`, oba oszacowania się schodzą i

    J*(B;k,H)² = min_{d₁²+d₂²<=B²}
                 [(1-d₁)²+(H+|k-d₂|)²].           (2)

Reguła `d(x)=x d*` jest ciągła, więc nie trzeba wprowadzać wyborów niemierzalnych.

## 3. TWIERDZENIE ROT16.1 — dokładne trzy fazy

Przy `k>0`, `H>0` definiujemy

    R = sqrt(1+(k+H)²),
    B₁ = k R/(k+H),
    B₂ = sqrt(1+k²).

Ponieważ `0<B₁<B₂<R`, istnieją dokładnie trzy reżimy:

    J*(B;k,H) =
      R-B,                                      0<=B<=B₁;
      sqrt[H²+(1-sqrt(B²-k²))²],             B₁<=B<=B₂;
      H,                                        B>=B₂.    (ROT16.1)

Formuły zgadzają się na obu progach. Gdy `k=0`, otrzymujemy znany ortogonalny przypadek `sqrt[H²+(1-B)_+²]`. Gdy `H=0`, przedział środkowy znika i `J*(B)=(sqrt(1+k²)-B)_+`.

**Dowód.** Zmniejszanie `d₁>1` do 1 lub `d₁<0` do 0 nie zwiększa (2), a zmniejsza normę `d`; analogicznie dla `d₂<0` (przy `k>=0`) lub `d₂>k` optymalny może być tylko zakres `0<=d₂<=k`. Na tym zakresie (2) przyjmuje gładką postać

    f(d)=||(1,k+H)-d||².

Jeśli ogranicza nas tylko kula `||d||<=B`, rzut wektora `p=(1,k+H)` na tę kulę to `d=(B/R)p` (dla `B<R`). Ten rzut ma `d₂=B(k+H)/R<=k` dokładnie wtedy, gdy `B<=B₁`. Otrzymujemy pierwszą gałąź `R-B`.

Dla `B>B₁` rzut na kulę znajduje się powyżej `d₂=k`, a więc poza zakresem dopuszczalnych minimizerów. Najbliższy punkt do `p` w przecięciu kuli z pasem `0<=d₂<=k` leży na krawędzi `d₂=k` i, dla `B<=B₂`, ma `d₁=sqrt(B²-k²)`; stąd gałąź środkowa. Na tej gałęzi optymalny regulator zużywa stałą wartość `d₂=k` na usunięcie przewidywalnej części sektora ukrytego i resztę budżetu na `d₁`.

Dla `B>=B₂` pełny przewidywalny środek `d=(1,k)` mieści się w kuli, wobec czego błąd ma wartość `H`. Niżej zejść nie można, bo nawet dla dokładnie znanego `x=1` dwie dopuszczalne wartości `w=±H` są nierozróżnialne. Dowód zakończony.

**Alternatywna kontrola na styku gałęzi:** przy `B=B₁` rzut radialny ma `d₂=k`, `d₁=k/(k+H)` i obie gałęzie mają wartość `R-B₁=H R/(k+H)`. Przy `B=B₂`, `d=(1,k)` i środkowa gałąź daje `H`.

## 4. Optymalny regulator i mechanizm

Przy pomiarze `x` wybierz `u(x)=-x d*(B)`, gdzie dla `k>0,H>0`

    d*(B)=(B/R, B(k+H)/R),                         B<=B₁;
    d*(B)=(sqrt(B²-k²), k),                        B₁<B<B₂;
    d*(B)=(1,k),                                  B>=B₂.

Dla `B>=B₂`, przy |x|<1 rzeczywisty budżet jest niewykorzystany; nie ma potrzeby poprawiać nieodróżnialnego `w`. Interpretacja faz:

1. **Ruch radialny ku skrajnemu ryzyku** przy małym B, z równoczesną poprawą obu współrzędnych.
2. **Nasycenie przewidywalnej składowej ukrytej** przy B>B₁: `d₂=k`, dalszy budżet idzie w widoczny komponent.
3. **Sufit informacyjny** B>=B₂: błąd zawsze `H`, mimo możliwej dalszej aktuacji.

Te fazy nie oznaczają faz fizycznych lub krytyczności dynamicznej; są klasycznymi fazami aktywnych ograniczeń w zadaniu wypukłym.

## 5. Sprawdzenie niezależne

Numeryczne bezpośrednie minimalizowanie (2) po dopuszczalnym `d₂∈[0,B]`, z optymalnym `d₁=min(1,sqrt(B²-d₂²))`, zrealizowano algorytmem bounded scalar minimization (SciPy), niezależnie od formuły kawałkami. Test objął 8 rodzin `(k,H)` (w tym `k=0`, `H=0`) × 11 budżetów = **88 przypadków**. Maksymalna różnica `|J_num-J_formula|=2.28e-15`, test PASS. Odpowiedni skrypt `verify_m13_rot16.py` zapisano lokalnie wraz z raportem. W pierwotnym podejściu wielostartowy solver SLSQP był nieefektywny; użyto skalarnych minimizacji z jawnie znaną geometrią dopuszczalną. Nie jest to test o niezależności oprogramowania, a jedynie niezależność ścieżki rachunkowej od formuły zamkniętej.

Dla `k=1, H=0.6`: `R≈1.8867962264`, `B₁≈1.17924764`, `B₂≈1.41421356`. Przykłady:

| B | Dokładny J*(B) | Reżim |
|---:|---:|---|
| 0.4 | 1.4867962264 | radialny |
| 1.0 | 0.8867962264 | radialny |
| 1.25 | 0.6500000000 | środkowy |
| 1.3 | 0.6234382306 | środkowy |
| 1.4 | 0.6003400751 | środkowy |
| 1.7 | 0.6000000000 | plateau |

## 6. Dokładna granica wniosków

`EARNED`: wzór (ROT16.1) i mierzalny regulator dla wyraźnie zdefiniowanego, skończeniewymiarowego skorelowanego posterioru i pełnego portu z budżetem amplitudy. Wykazane progi `B₁`, `B₂`; kontrola numeryczna.

`NOT EARNED`: nowe twierdzenie o fizyce, kwantowej interferencji, grawitacji, NCDG/J3/K, czasowym sterowaniu, nowości matematycznej, dowolnych kształtach posterioru lub wpływie szumu pomiaru. Przy zaszumionym pomiarze `b=x+η` posterior sprzęga obie składowe i potrzebna jest pełna analiza warunkowa; obecnego wzoru nie wolno używać przez proste zastąpienie `H` promieniem posterioru.

`MATURE_HOST`: constrained Chebyshev center (LT5 turn 3); rzut euklidesowy na kulę przeciętą z półprzestrzenią; minimax/set-membership output feedback. Ogólna formuła LT5 pozostaje nadrzędna i zawiera niniejszy rezultat jako szczególny jawny rachunek.

`REFEREE`: niezależnego referee tego konkretnego wzoru nie uzyskano; audyt REC10 dla LT5 turn 1 **nie jest** audytem niniejszego ROT16.

Źródła:
- LT5 vector host: https://github.com/wmakiela-tech/Nash-iw-research/blob/5c5e8599727b1b63b11cdc7d628dab875dcf760e/research/lt5/2026-10-21/lt5_vector_target_constrained_chebyshev_dual_and_nonseparable_actuation_001.md
- LT5 scalar: https://github.com/wmakiela-tech/Nash-iw-research/blob/b8bd36a4b2224b4f560eb14d1172634cb14b74f5/research/lt5/2026-10-21/lt5_scalar_target_amplitude_limited_output_feedback_minimax_decomposition_001.md
- M13 ROT15, poprzednik: `/mnt/data/IW_M13_ROT15_orthogonal_product_noisy_vector_target_20261021.md` (nie potwierdzono pełnej kopii zewnętrznej).

**ROUTING:** `IWTO_LT5 IWTO_MT13 IWTO_INT8 IWTO_SW IWTO_REC10 IWTO_MODERATOR`.  
**STOP:** `NO_NEW_TASK / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / TPE HOLD`.
