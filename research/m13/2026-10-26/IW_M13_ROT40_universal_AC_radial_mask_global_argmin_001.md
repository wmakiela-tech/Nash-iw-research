# IW/NASH · M13 ROT40 · Źródłowy certyfikat dwuwymiarowy minimum globalnego pięciu masek dla A i C

**RETURN_ID:** `M13-ROT40-DTC0A-SOURCE-DIRECT-UNIVERSAL-AC-RADIAL-FIVE-MASK-ARGMIN-001_20261026`

**Problem:** `P3_DTC0A_TT_MASK_COMMUTATION_AND_LOCAL_RMS_TYPING_001`  
**Status:** wykonane; komputerowo wspomagany dowód warunkowy dla funkcjonalnie dopasowanego generatora, bez akceptacji właściciela/EXEC, bez nowej fizyki i bez deklaracji oryginalności matematycznej.

## 1. Motywacja, rozdział odpowiedzialności i postęp

ROT29–31: nieidentyfikowalność norm dowolnych pól niskopasmowych/TT. ROT32–33: identyfikacja parametru znanej źródłowej rodziny przy 2 kanałach. ROT34: monotoniczność i fałdy ilorazów wielu masek jednego kanału. ROT35: dokładna kowariancja wspólnych wokseli i algebra rozłącznych powłok. ROT36: numeryczna globalna separacja. ROT37: dowód globalnego minimum **dwumaskowego** przy α₀=.05. ROT38: dowód minimum globalnego **pięciomaskowego** przy α₀=.05. ROT39: ścisła izolacja przełączników między β=α±.01; to nie wystarczało jeszcze do twierdzenia o dowolnym β.

**Nowa funkcja ROT40:** dowód, że pełna pięciomaskowa odległość profilowana dla kanałów **A i C** jest ściśle malejąca przy zbliżaniu β do α z lewej i rosnąca przy oddalaniu w prawo — **dla każdej pary** α,β∈[0,.2]. W konsekwencji globalne minimum na zbiorze |β−α|≥δ występuje w najbliższych dopuszczalnych punktach brzegowych, dla każdego δ>0 (jeśli zbiór niepusty). **B jest osobnym NEGATIVE CONTROL:** globalna radialna monotoniczność nie zachodzi, chociaż gęsty skan numer. nie wykrył odstępstwa od brzegowego minimum dla δ=.01.

To jest wynik o wąskiej źródłowo klasie obserwacji, nie własność przestrzeni arbitralnych tensorów TT. MT13 zachowuje priorytet źródłowy ogólnej geometrii nieznanego wspólnego dodatniego wzmocnienia i testów stożkowych; nie przypisujemy go ROT40.

## 2. Host i typy

- Siatka **N=41**, maski interior `k∈{2,3,4,5,6}`, rozmiary `n_k=(N−2k)^3`: `[50653,42875,35937,29791,24389]`.
- Ciągi rozłącznych powłok o wielkościach `w=[7778,6938,6146,5402,24389]`.
- Fourierowy generator jak w `verify_m13_rot33_interval.py`: `C1=(.05 sin x,.05 cos y,0)`, `C2=(.04 cos z,0,.04 sin x)`, `h=.1 sin x cos y I` (czysto śladowe wejście AMBIENT), centralny stencil rzędu 2, `E_α=I+α dx² Δ_h`, stały płaski projektor Fourier-TT.
- `g_{c,k}(α)=RMS_mask(K_c(α))²` jest wielomianem ≤4. `s_{c,i}(α)` to średnia energii i-tej rozłącznej powłoki, obliczona dokładnie liniowym przejściem z `g_k`; wszystkie powłoki są ściśle dodatnie na [0,.2].
- Wspólna nieznana dodatnia **amplituda energii** `t=s²` dla pięciu masek danego kanału. Syntetyczny host niezależnych, jednakowo rozproszonych wokselowych błędów **energii** daje metrykę `W=diag(w_i)`. Nie oznacza pięciu niezależnych odczytów RMS ani zmierzonego szumu w rzeczywistym doświadczeniu.

## 3. Twierdzenie o geometrii profilu pięciu masek

Niech `a_i=s_i(α)`, `b_i=s_i(β)`, `p(α,β)=∑ w_i a_i b_i`, `q(β)=∑ w_i b_i²>0`. Ponieważ wszystkie energie powłok są dodatnie, `p>0`, a optymalny dodatni współczynnik t nie ulega obcięciu do zera.

Kwadrat odległości profilowanej (bez stałego dzielnika τ²) wynosi

`D²(α,β)=||a||_W²−p(α,β)²/q(β)`.

Pochodna względem β:

`∂_β D² = −p H/q²`, z `H=2 p_β q−p q_β`.

Tożsamość algebraiczna `H(α,α)=0` zachodzi dla **dowolnego** wielomianowego profilu (symetria p i definicja q), dlatego `H=(α−β)P(α,β)` dla pewnego wielomianu P. Jeśli `P>0` na `[0,.2]²`, wtedy

`sgn(∂_β D²)=sgn(β−α)`.

A więc dla dowolnego prawdziwego α₀ oraz δ>0 (z niepustym zbiorem alternatyw) minimum na `[0,.2] ∩ {β:|β−α₀|≥δ}` leży **wyłącznie** w zbiorze najbliższych dopuszczalnych punktów `α₀−δ` i `α₀+δ`. Unikatowość wynika, gdy tylko jeden jest dopuszczalny lub odległości w dwóch punktach są różne; przy równości oba minimalizują.

## 4. Źródłowy certyfikat przedziałowy, a nie tylko zaokrąglony model

Z zamrożonego implementacyjnie modelu trygonometrycznych operatorów ROT33 bezpośrednio otrzymano **15 × 5 przedziałowych współczynników** kwartycznych `g_{ch,k}`; precyzja `mpmath.iv` 45 cyfr. Każdy współczynnik został zachowany jako skierowanie zaokrąglony przedział końców w `direct_A.json`, `direct_B.json`, `direct_C.json`. Ponowne zaokrąglenie końców do przedziałów w certyfikatorze wyłącznie rozszerza otoczkę.

Z tych źródłowych przedziałów utworzono H oraz iloraz przez `(α−β)` **algebraicznym dzieleniem wielomianowym** w pierścieniu przedziałowym (tożsamość podzielności obowiązuje formalnie; współczynniki ilorazu mają przedziałowe otoczki). Wszystkie **165 × 2** współczynników Bernsteina (dwuwymiarowy stopień otrzymanej otoczki `[14,10]`) P na całym `α,β∈[0,.2]` mają dolną granicę >0:

- `A`: najniższa dolna granica `9.81548461444823e−31`;
- `C`: najniższa dolna granica `1.27346029263546e−40`.

W obydwu kanałach sprawdzono też wszystkie pięć wielomianów powłokowych jako ściśle dodatnie na całym przedziale. Porównanie 3 × 5 × 3 = **45** historycznych norm: największy błąd względny środków przedziałów `2.89e−15` (diagnostyczne dopasowanie źródła, nie dowód tożsamości z niedostępnym runtime’em).

**Negatywna kontrola B:** współczynniki Bernsteina P nie są wszystkie dodatnie. Co więcej, dla `α=.05,β=0` źródłowy przedział `H<0`, chociaż przy β<α wymagana byłaby nierówność H>0. Zatem pięciomaskowa funkcja D_B nie ma uniwersalnej radialnej monotoniczności, a nie tylko „brakuje nam certyfikatu”. To **nie** jest kontrprzykład do hipotezy, że globalny minimizator B dla δ=.01 leży na brzegu — takiego kontrprzykładu nie stwierdzono.

## 5. Corollarium dla δ=.01 i ROT39

W połączeniu z osobnym, źródłowo certyfikowanym porównaniem **dwóch** brzegów w ROT39 otrzymujemy pełną mapę globalnej trudniejszej alternatywy:

- Kanał A: dla `α∈[.01,.19]` wygrywa `β=α+.01`; dla `α<.01` jedyny dopuszczalny bliższy brzeg to prawa strona; dla `α>.19` — lewa.
- Kanał C: w `α∈[.01,.19]` istnieje jeden przełącznik `α_C≈.04366608423217492` z certyfikowanym przedziałem wymiernym w ROT39; dla `α<α_C` wygrywa lewa `β=α−.01`, powyżej wygrywa prawa. Przy samym przełączniku obie alternatywy równoważne. Poza `[.01,.19]` tylko jedna strona leży w `[0,.2]`.
- Kanał B: ROT39 klasyfikuje jedynie porównanie dwóch punktów `α±.01`; **nie** wolno z tego orzekać globalnej minimalności jednego z nich.

Wspólna dodatnia amplituda jest warunkiem nośnym. Osobne amplitudy na każdą maskę, nieznany generator, nieznana kowariancja lub inne źródło unieważniają ten konkretny wniosek.

## 6. Kontrole niezależne i wyniki punktowe

`verify_m13_rot40_exact.py` to **niezależny od źródła** program oparty wyłącznie na `fractions.Fraction`; wykonuje 40 faktoryzacji wielomianowych `H=(β−α)Q`, 200 kontroli dokładnej projekcji GLS/wedge i jej pochodnej. Wszystkie kontrole PASS. Główny certyfikator `verify_m13_rot40_interval.py` odtwarza 45 historycznych norm i certyfikuje dwuwymiarowy znak oraz siedem par punktowych na kanał: `α={0,.02,.05,.10,.15,.18,.20}` przy δ=.01 (spójność znaków sprawdzona skierowanymi, rozłącznymi przedziałami).

## 7. Reprodukcja, proveniencja i ograniczenia

Zawartość ZIP: raport, pełne 15 przedziałowych kwartycznych źródeł, program certyfikatora, niezależny program Fraction, generator bezpośrednich współczynników `source_snapshot_ch.py`, zamrożony operator `verify_m13_rot33_interval.py`, oryginalny funkcjonalnie dopasowany helper `deepseek_python_20260627_a87249.py`, historyczny N41 CSV, JSON wyników, logi i `SHA256SUMS`.

Odtworzenie szybsze, źródłowo zamrożone: `python verify_m13_rot40_exact.py && python verify_m13_rot40_interval.py && sha256sum -c SHA256SUMS_M13_ROT40.txt` (sumy kontrolne sprawdzać PRZED nadpisaniem wyników). Pełna regeneracja współczynników: `python source_snapshot_ch.py A`, analogicznie B/C (wolniejsze; wymaga `mpmath==1.3.0`). Program przy każdym uruchomieniu nadpisuje JSON wyniku; odtwarzalność byte-for-byte weryfikować przez SHA przed i po.

**Braki i zakazy eskalacji:** (1) brak bajtowo zgodnego `dtc0a_runtime_v0_3_1.py`; (2) wsparcie rachunkiem `mpmath.iv`, nie formalne sprawdzenie w Lean/Coq; (3) tylko N41, 5 masek, ustalone operatory i źródła oraz płaska Fourier-TT; (4) `K_A(h)` działa na ambientowym czysto śladowym h, nie jest nową fizyczną własnością działania na TT `P(h)`; (5) nie zmierzono szumu wokselowego, porównania w jednostkach szumu mają charakter wyłącznie warunkowy; (6) B globalne minimum dla wszystkich α nadal otwarte; (7) brak roszczenia do matematycznej nowości, niezależnej recenzji, kanonu, BW/EXEC signoff, K/J3/TPE czy interpretacji fizycznej.

**Gates:** `SOURCE_DIRECT_AC_GLOBAL_RADIAL_PASS / B_RADIAL_COUNTEREXAMPLE_PASS / NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / TPE HOLD`.