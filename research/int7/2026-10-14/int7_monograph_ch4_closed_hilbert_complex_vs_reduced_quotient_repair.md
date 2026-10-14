# INT7 — naprawa rozdziału 4: zamknięty kompleks Hilberta a zredukowany iloraz

## Werdykt

PASS_WITH_OBJECT_TYPING_REPAIR / NO THEOREM REMOVAL.

W §§4.2–4.5 operator
\[
d_k^f=T_{k+1}d_k,\qquad D(d_k^f)=D(d_k)
\]
spełnia \(d_{k+1}^f d_k^f=0\) i \(\ker d_k^f=\ker d_k\), lecz sam tekst słusznie zaznacza, że \(d_k^f\) nie musi być domknięty. Przy standardzie zadeklarowanym już w §4.1 i bibliografii [17] (Brüning–Lesch), „kompleks Hilberta” jest tu kompleksem z domkniętymi różniczkami. Przed uzyskaniem domkniętości nie należy więc bez kwalifikacji nazywać \((H^k,d_k^f)\) kompleksem Hilberta ani jego ilorazu standardową zredukowaną kohomologią kompleksu Hilberta.

Rdzeń matematyczny rozdziału pozostaje zachowany po rozdzieleniu:
1. gęsto określonego kompleksu różniczkowego na przestrzeniach Hilberta;
2. zredukowanego ilorazu tego kompleksu;
3. zamkniętego kompleksu Hilberta, uzyskanego dopiero po osobnym certyfikacie domkniętości.

## Dokładny obiekt przed domkniętością

Do czasu wykazania domkniętości wszystkich \(d_k^f\) wprowadzić notację
\[
\widetilde H_{\rm red}^k(d^f)
:=
\ker d_k^f/\overline{\operatorname{ran}d_{k-1}^f}.
\]

To jest **zredukowany iloraz zdeformowanego kompleksu różniczkowego**. Nie trzeba jeszcze nazywać go zredukowaną kohomologią kompleksu Hilberta.

Iloraz jest legalny. Z twierdzenia 4.1:
\[
\operatorname{ran}d_{k-1}^f\subseteq\ker d_k^f.
\]
Ponadto
\[
\ker d_k^f=\ker d_k,
\]
a \(d_k\) jest domknięty, więc \(\ker d_k\) jest domkniętą podprzestrzenią \(H^k\). Wobec tego
\[
\overline{\operatorname{ran}d_{k-1}^f}
\subseteq
\ker d_k^f.
\]

## Naprawa twierdzenia 4.2

Proponowana nazwa:

**Twierdzenie 4.2 (zachowanie zredukowanego ilorazu).**

Jeśli \(f(\Delta_k)\) jest ograniczone, iniektywne i zachowuje
\[
\overline B^k=\overline{\operatorname{ran}d_{k-1}}
\]
jako podprzestrzeń redukującą, to
\[
\overline{\operatorname{ran}d_{k-1}^f}=\overline B^k.
\]

W konsekwencji, przy hipotezach twierdzenia 4.1,
\[
\widetilde H_{\rm red}^k(d^f)=H_{\rm red}^k(d)
\]
przez naturalną identyfikację liczników i mianowników.

Jeżeli dodatkowo wszystkie \(d_k^f\) są domknięte, lewa strona jest standardową zredukowaną kohomologią kompleksu Hilberta i można pisać
\[
H_{\rm red}^k(d^f)=H_{\rm red}^k(d).
\]

Dotychczasowy dowód twierdzenia 4.2 można zachować. Nie używa on domkniętości \(d_k^f\); używa równania
\[
\operatorname{ran}d_{k-1}^f=T_k(B^k),
\]
gęstości \(B^k\) w \(\overline B^k\), własności \(T_k\) na redukującej podprzestrzeni oraz równości jąder.

## Twierdzenie 4.3 jako bramka domkniętości

Twierdzenie 4.3 jest dokładnym punktem przejścia do standardowego kompleksu Hilberta.

Dwustronne oszacowanie na \(\overline{\operatorname{ran}d_k}\),
\[
m_k\|v\|\le \|T_{k+1}v\|\le M_k\|v\|,
\]
daje równoważność norm grafowych i domkniętość \(d_k^f\) na \(D(d_k)\).

Jeżeli zachodzi ono we wszystkich stopniach, wtedy \((H^k,d_k^f)\) jest ponownie kompleksem Hilberta.

Gotowe zdanie po dowodzie twierdzenia 4.3:

> Jeżeli powyższe oszacowania zachodzą dla wszystkich stopni, to zdeformowana rodzina \((H^k,d_k^f)\) jest kompleksem Hilberta w standardowym sensie. Od tego miejsca \(\widetilde H_{\rm red}^k(d^f)\) można bez dodatkowej kwalifikacji oznaczać \(H_{\rm red}^k(d^f)\).

## Kontrprzykład 4.5 jako separator

Przykład
\[
d=\operatorname{diag}(n),\qquad f(z)=e^{-z}
\]
wzmacnia to rozróżnienie.

Na zachowanej dziedzinie \(D(d)\),
\[
d^f=\operatorname{diag}(ne^{-n^2})|_{D(d)}
\]
nie jest domknięty. Zdeformowany obiekt nie jest więc w tym miejscu kompleksem Hilberta w przyjętym sensie.

Jednocześnie
\[
\ker d^f=\{0\},\qquad
\overline{\operatorname{ran}d^f}=H^1,
\]
więc
\[
\widetilde H_{\rm red}^1(d^f)=0=H_{\rm red}^1(d),
\]
podczas gdy
\[
H_{\rm alg}^1(d^f)=H^1/\operatorname{ran}d^f\ne0.
\]

To rozdziela trzy własności:

- differential-complex property;
- closedness / Hilbert-complex status;
- algebraic versus reduced quotient.

## Ready-to-paste corrections

### §4.2
Po twierdzeniu 4.1 dodać:

> Rodzina \(d^f\) jest więc gęsto określonym kompleksem różniczkowym na przestrzeniach Hilberta. Nie musi być jeszcze kompleksem Hilberta w standardowym sensie, ponieważ domkniętość \(d_k^f\) nie została wykazana.

### §4.3
Pierwsze użycie \(H_{\rm red}^k(d^f)\) zastąpić przez \(\widetilde H_{\rm red}^k(d^f)\), dodać definicję zredukowanego ilorazu i zmienić nazwę twierdzenia 4.2 na „zachowanie zredukowanego ilorazu”.

### §4.4
Po dowodzie domkniętości dodać:

> Jeśli warunki twierdzenia zachodzą we wszystkich stopniach, \(d^f\) jest kompleksem Hilberta; wówczas \(\widetilde H_{\rm red}^k(d^f)\) jest standardową zredukowaną kohomologią i może być oznaczane \(H_{\rm red}^k(d^f)\).

### §4.5
Równanie (4.9) zapisać na etapie pierwotnej dziedziny jako
\[
\widetilde H_{\rm red}^1(d^f)=0=H_{\rm red}^1(d).
\]
Następnie pozostawić już istniejący komunikat, że domknięcie \(d^f\) jest inną realizacją dziedzinową.

## Firewalle

DIFFERENTIAL COMPLEX != CLOSED HILBERT COMPLEX.

REDUCED QUOTIENT != STANDARD HILBERT-COMPLEX COHOMOLOGY UNTIL CLOSEDNESS.

CLOSURE OF \(d^f\) != SAME DOMAIN REALIZATION.

SAME REDUCED QUOTIENT != SAME ALGEBRAIC COHOMOLOGY.

## Status

CHAPTER4_4.2_TO_4.5 = PASS_WITH_OBJECT_TYPING_REPAIR.

THEOREM_4.2_PROOF = RETAIN.

THEOREM_4.3 = CLOSEDNESS_PROMOTION_GATE.

COUNTEREXAMPLE_4.5 = RETAIN_AND_STRENGTHEN_AS_SEPARATOR.

BLOCKING_SCIENTIFIC_GAP = NONE.

NEW_RESEARCH_REQUIRED_NOW = NO.

NOVELTY = NONE.

NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
