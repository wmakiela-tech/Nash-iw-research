# IW / M13 — ROT15: ortogonalny iloczyn niepewności, zaszumione pomiary i dokładna dekompozycja kwadratowa błędu wektorowego

**RETURN_ID:** `M13-ROT15-LT5-ORTHOGONAL-PRODUCT-NOISY-VECTOR-MINIMAX-001_20261021`  
**Linia:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**Data:** 2026-10-21  
**Klasa:** ścisłe twierdzenie warunkowe w klasycznym skończeniewymiarowym *optimal recovery* i *set-membership output feedback*.  
**Status:** `[▷] EXACT_ABSTRACT / HOST_ABSORBED / INDEPENDENT_REFEREE_NOT_OBTAINED / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK`.

## 0. Dlaczego ROT15, a nie ponowne ROT14

LT5 2026-10-21 (obrót 2) wykazał dokładną tożsamość dla skalarnego celu i twardego ograniczenia amplitudy aktuatora: `J_scalar*(B)=max(E,A-B)` przy konkretnych warunkach dotyczących zwartych, wypukłych, centralnie symetrycznych zbiorów niepewności, niezależnego szumu, pomiaru bez back-action i skalarnego portu wyjściowego. ROT14 M13 z tego samego dnia skonstruował pełnorankowy dwuwymiarowy aktuator i pokazał, że na kwadratowym zbiorze celów wektorowych proste przeniesienie formuły skalarnej jest fałszywe, mimo braku rank-deficiency portu.

ROT15 wyprowadza ogólny **warunkowy wzór dokładny** dla niezależnego sektora ukrytego i obserwowanego, w tym przy zaszumionym, niekoniecznie doskonałym pomiarze. Jest rozszerzeniem mechanizmu ROT14, a nie nową rodziną praw fizycznych. Bieżący korpus 2026-10-21: Rec10 `PASS_WITH_GUARDS` dla wcześniejszego LT5 wyniku o ograniczonym wzmocnieniu; INT8/Geeky-S10 opracowały osobne twierdzenia o wielokrotnych słabych pomiarach, nie utożsamiane tu z twardym ograniczeniem amplitudy.

## 1. Dokładny model typowany

Niech `V`, `W` będą rzeczywistymi skończeniewymiarowymi przestrzeniami euklidesowymi, a przestrzeń celu będzie ich ortogonalną sumą `V ⊕ W` z normą

    ||(v,w)||² = ||v||² + ||w||².

Stan `(x,z)` należy do *iloczynu kartezjańskiego* `K=X×Z`, gdzie `X⊂V` jest niepusty zwarty, a `Z⊂W` jest niepusty, zwarty i **centralnie symetryczny względem 0** (`Z=-Z`). W szczególności `X` nie musi być wypukły ani symetryczny, a `Z` nie musi być wypukły. Sektor ukryty ma promień

    H = max_{z∈Z} ||z||.

Pomiar może być zaszumiony i nieliniowy, lecz nie może zależeć od `z`:

    b = q(x,η),

z niezależnym, jawnie określonym zakresem szumu `η∈N`; zbiór możliwych `z` po obserwacji pozostaje całym `Z`. Reguła po obserwacji wybiera **pełny wektor** korekty `u(b)=(u_V(b),u_W(b))∈V⊕W`, z ograniczeniem

    ||u(b)|| ≤ B,

oraz celem terminalnym `(x,z)+u(b)`. Nie ma innych oddziaływań na stan, nie ma pomiarowego back-action i nie ma ograniczeń trajektorii aktuatora. Reguły są mierzalne na przestrzeni obserwacji, na której ma to sens; wartości minimaksowe zapisujemy jako infimum, bez dodatkowego twierdzenia o istnieniu selekcji optymalnej w pełnej ogólności.

Niech

    J_full(B) = inf_{u:||u(b)||≤B} sup_{x∈X,z∈Z,η∈N} ||(x,z)+u(q(x,η))||,

    J_vis(B)  = inf_{v:||v(b)||≤B} sup_{x∈X,η∈N} ||x+v(q(x,η))||.

## 2. Twierdzenie ROT15.1 — dokładny rozkład pitagorejski

**Twierdzenie:** Dla każdego `B≥0`, pod powyższymi założeniami,

    J_full(B) = sqrt( H² + J_vis(B)² ).                       (ROT15.1)

**Dowód.** Wybierzmy dowolną legalną regułę `u=(u_V,u_W)`, ustalmy wynik `b` i zbiór dopuszczalnych `x` z tym wynikiem. Dzięki pełnej niezależności `Z` maksymalny kwadrat błędu przy ustalonym `b` rozdziela się na sumę:

    sup_{x,z zgodnych z b} ||(x,z)+(u_V(b),u_W(b))||²
      = sup_{x zgodnych z b} ||x+u_V(b)||²
        + max_{z∈Z} ||z+u_W(b)||².

Niech `z_*∈Z` ma normę `H`. Z symetrii `z_*, -z_*∈Z`. Równoległobok daje

    max_{z∈Z} ||z+u_W(b)||²
      ≥ max( ||z_*+u_W(b)||², ||-z_*+u_W(b)||² )
      ≥ H² + ||u_W(b)||²
      ≥ H².

Zatem zastąpienie każdej legalnej reguły `u(b)` przez `\tilde u(b)=(u_V(b),0)` zachowuje legalność (`||u_V(b)||≤||u(b)||≤B`) i nie zwiększa błędu dla żadnego `b`. Wystarczy więc optymalizować nad politykami bez aktuacji w sektorze ukrytym. Dla każdej takiej polityki

    sup_{x,z,η} ||(x,z)+(u_V(q(x,η)),0)||²
      = H² + sup_{x,η} ||x+u_V(q(x,η))||².

Funkcja `r↦sqrt(H²+r²)` jest ciągła i rosnąca na `r≥0`, więc można przenieść ją przez infimum. Otrzymujemy dokładnie (ROT15.1). QED.

**Znaczenie:** pełnorankowy aktuator pozostawia nieredukowalny błąd sektora niezidentyfikowanego, gdy pomiar nie mówi o tym sektorze nic i sektor jest centralnie symetryczny. Pozostała korekta jest zadaniem optymalnego odzyskiwania komponentu widocznego. Te dwa błędy sumują się geometrycznie, nie przez maksimum.

## 3. Twierdzenie ROT15.2 — przykład zaszumiony i pełna formuła zamknięta

Weźmy `V=W=R`, `X=[-1,1]`, `Z=[-H,H]`, `H≥0`. Pomiar i niepewność:

    b = x + η,      |η|≤δ,  δ≥0.

Aktuator dopuszcza dowolny wektor `u(b)=(u_x,u_z)` o `sqrt(u_x²+u_z²)≤B`, `B≥0`.

Problem widoczny jest dokładnie skalarnym problemem LT5 z `A=1`, pasywnym promieniem informacji `E=min(1,δ)`. Jego rozwiązanie można wyprowadzić bez fizycznego modelu:

    J_vis(B) = max{ min(1,δ), 1-B }.

Równość wynika z dolnych ograniczeń: przy `b=0` stany `x=±min(1,δ)` są nierozróżnialne; przy `x=1` jedna korekta o wielkości `≤B` nie może zmniejszyć błędu poniżej `1-B`. Górne ograniczenie daje obcięcie środka przedziału zgodności dla każdego `b`: jeśli `X_b=[l(b),h(b)]`, wybieramy `u_x(b)=-clip((l+h)/2,-B,B)`; największy błąd to promień tego przedziału plus dodatnia część niedoboru budżetu, ograniczone przez `max(E,1-B)`.

Z ROT15.1 otrzymujemy:

    J_full(B,δ,H) = sqrt( H² + max{min(1,δ),1-B}² ).        (ROT15.2)

**Przykład liczbowy:** `H=0.6`, `δ=0.2`, `B=0.5`:

    J_vis=0.5;  J_full=sqrt(0.36+0.25)=sqrt(0.61)
                      = 0.7810249675906654.

Pasywny promień wektorowy to `sqrt(0.36+0.04)=sqrt(0.40)=0.6324555320`, a doskonale-znanostanowy dolny próg braku amplitudy to `max(sqrt(1+0.36)-0.5,0)≈0.66619`. Ich proste maksimum jest mniejsze od prawdziwego `0.78102`: błędy nie mogą być traktowane jako alternatywne zdarzenia.

Próg nasycenia sterowania ma postać `B_sat=1-min(1,δ)`. Dla `B≥B_sat` zwiększanie maksymalnej amplitudy nie poprawia gwarancji, dopóki ograniczeniem pozostaje szum pomiarowy i całkowicie nieobserwowalny sektor. W przeciwieństwie do przypadków skalarnego `max(E,A-B)` zależność błędu wektorowego jest kwadratowa w składnikach.

## 4. Silniejsze granice i przypadki wymagające osobnego kontraktu

1. **Brak założenia pełnej wypukłości:** dowód (ROT15.1) wymaga zwartości i symetrii `Z`, nie wypukłości. `X` może być dowolnym niepustym zbiorem zwartym. Gdy `Z` nie jest symetryczny, aktuacja w części ukrytej może przesunąć jego środek Chebysheva i wzór może zawieść.
2. **Niezależność sektorów:** jeśli zbiór stanów nie jest iloczynowy (`Z` zależy od obserwowanego `x`), pomiar ogranicza także ukrytą niepewność i nie da się wyciągnąć stałego `H²` przed suprema.
3. **Port aktuatora:** konieczna jest całkowita możliwość wyboru korekty w widocznym sektorze bez obowiązku korygowania ukrytego. Anizotropowy port / port sprzężony, stanowo zależny budżet lub ograniczenie sterowania o innym typie mogą zmieniać wartość.
4. **Norma i geometria:** twierdzenie korzysta ze wzoru Pitagorasa w ortogonalnej sumie euklidesowej. Norma niesepatrowalna lub geometria niehilbertowska wymaga nowego dowodu. Nie zastępować automatycznie przez `max` ani `sum`.
5. **Czasy/interwencje:** to jedna jednorazowa korekta po obserwacji. Wynik nie mówi nic o wieloczasowych testerach kwantowych, back-action, wyjściowej sterowalności w innej dynamice, NCDG J3/K czy fizycznej grawitacji.
6. **Skalar LT5 nie jest kwestionowany:** (ROT15.2) używa dokładnie jego prawidłowego problemu widocznego, po czym dodaje niezależny sektor wektorowy. Rec10 audytował wcześniejszy wynik LT5 z ograniczeniem wzmocnienia, a nie nowy wektorowy wzór.

## 5. Kontrole obliczeniowe i własne ograniczenia

- `verify_m13_rot15.py` skanuje 481 wartości pomiaru `b` w przedziale `[-1.2,1.2]` dla powyższego przykładu i wyznacza dokładne przedziały stanów zgodnych. Maksimum równe `sqrt(0.61)`.
- Niezależne numeryczne minimalizacje SLSQP w dwuwymiarowej kuli aktuatora dla 9 wyników `b` zgadzają się z rozwiązaniem analitycznym do `1e-5`. Optima mają niewykorzystywany kanał ukryty (`u_z≈0`). `PASS`.
- Test numeryczny nie dowodzi ogólnego twierdzenia, którego dowód jest w §2.
- **Subtraction-first:** geometryczne twierdzenia o promieniu Chebysheva dla zbiorów symetrycznych i *optimal recovery* są klasycznymi gospodarzami; nie przeprowadzono pełnego przeglądu priorytetu wszystkich specjalizacji tego wzoru. `NOVELTY=NONE`.

## 6. Właściciele, źródła i proponowany zapis do wiedzy negatywnej

LT5 skalar / nowe twierdzenie: https://github.com/wmakiela-tech/Nash-iw-research/blob/b8bd36a4b2224b4f560eb14d1172634cb14b74f5/research/lt5/2026-10-21/lt5_scalar_target_amplitude_limited_output_feedback_minimax_decomposition_001.md

LT5 wcześniejszy wynik o ograniczonym wzmocnieniu: https://github.com/wmakiela-tech/Nash-iw-research/blob/ee4a54651106ca2e150e6795f5d258b3842e9d2c/research/lt5/2026-10-20/lt5_target_information_vs_actuation_bounded_feedback_exact_gate_001.md

REC10 audyt LT5 pierwszego obrotu: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/rec10/2026-10-21/IW_REC10_ROT03_LT5_INFORMATION_VS_ACTUATION_EXACT_GATE_REFEREE_001_20261021.md

M13 ROT14 lokalny poprzednik: `IW_M13_ROT14_full_port_vector_target_chebyshev_20261021.md`; jego kopie Drive/GitHub **nie zostały potwierdzone**. Niniejszy raport nie pozoruje pełnej archiwizacji tamtego wyniku.

Trwała reguła merytoryczna, o ile właściwy owner ją przyjmie:

    INDEPENDENT_ORTHOGONAL_HIDDEN_SECTOR_WITH_SYMMETRY
    => EXACT_QUADRATURE_OF_HIDDEN_RADIUS_AND_VISIBLE_MINIMAX_ERROR;
    SCALAR_MAXIMUM_DECOMPOSITION
    != GENERAL_VECTOR_OUTPUT_DECOMPOSITION.

**ROUTE_TAGS:** `IWTO_LT5 IWTO_MT13 IWTO_INT8 IWTO_SW IWTO_REC10 IWTO_MODERATOR`.
**STOP/CEILING:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_NEW_TASK / TPE HOLD`; nie zgłaszać niezależnego audytu ani zapisu zewnętrznego bez weryfikacji readback.
