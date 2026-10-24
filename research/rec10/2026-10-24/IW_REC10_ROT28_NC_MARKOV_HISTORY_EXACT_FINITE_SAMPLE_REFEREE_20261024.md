# IW/NASH — REC10 ROT28
## Dokładny przyrost odległości TV i minimalna liczba obserwacji dla dwóch historii Markowa NC §3.10

**Data:** 2026-10-24  
**Komórka:** `IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10`  
**Werdykt:** `PASS_WITH_EXACT_STRICT_INCREMENT_AND_FINITE_SAMPLE_CERTIFICATE`  
**Status:** `NONBLIND_MATURE_PROBABILITY_REFEREE / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / BW_PENDING`.

## 1. Currentness i prior art subtraction

**Autorstwo obiektu:** NC ART006 skonstruował dwie dodatnie, dwustanowe, stacjonarnie symetryczne macierze przejścia, obie z równomiernym rozkładem początkowym. **PRF11 R28** pierwszy w bieżącej rodzinie podał dokładną redukcję miary TV historii do TV dwumianów i dowiódł zbieżności do 1 oraz wzajemnej osobliwości praw nieskończonych ścieżek. **KN11** podał optymalny test Neymana–Pearsona `K>nθ`, stałą `θ=log_2(4/3)` i wykładnik Chernoffa `C=0.014507546248081996...`. Te wyniki są PIERWSZE i nie są przypisywane REC10.

Wykorzystane raporty odczytane źródłowo:

- PRF11 R28: `research/prf11/2026-10-24/IW_PRF11_R28_NC12_NONMAP_MATURE_HOST_SUBTRACTION_AND_MARKOV_HISTORY_SHARPNESS_001_20261024.md`, Git blob `866450c97a40a626b8dce3b312a2aed3aeb18045`.
- KN11: `research/kn11/2026-10-24/iw_kn11_rot_source_currentness_markov_chernoff_and_frontb_conditional_001.md`, Git blob `cc8a3b4eace79e0fc552e28a138932a8903e08b6`.
- NC ART006, §3.10: obie macierze i pierwotny przykład pochodzą od NC; nie przedstawia się audytu jako nowego oryginalnego modelu Markowa.

**Nowy, ściśle ograniczony krok ROT28:** udowodnienie dodatniego przyrostu TV przy KAŻDYM dodatkowym przejściu (nie tylko `TV_n→1`), dwugałęziowego dokładnego wzoru na ten przyrost oraz ścisłej *minimalnej* długości historii dla siedmiu docelowych progów TV przy całkowitoliczbowej certyfikacji bez błędu zaokrągleń.

## 2. Źródłowy nośnik i dokładne TV

Niech 

\[
P_1=\begin{pmatrix}1/2&1/2\\1/2&1/2\end{pmatrix},\qquad
P_2=\begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix},
\qquad X_0\sim(1/2,1/2).
\]

Dla `n` *przejść* (ścieżka ma `n+1` stanów) `F_j=1{X_j≠X_{j-1}}` są niezależnymi zmiennymi Bernoulliego z prawdopodobieństwem `p=1/2` lub `p=1/3`; `K_n=ΣF_j`. Transformacja `(X_0,F_1,...,F_n)↔(X_0,...,X_n)` jest bijekcją. Rozkłady `X_0` są identyczne. Stąd dokładnie

\[
V_n:=\mathrm{TV}(\mathbb P_1^{(n)},\mathbb P_2^{(n)})
=\mathrm{TV}(\mathrm{Bin}(n,1/2),\mathrm{Bin}(n,1/3)).
\]

Iloraz wiarygodności w ścieżce z `K_n=k` wynosi `L_n(k)=(3/4)^n 2^k`. Niech

\[
\theta=\frac{\ln(4/3)}{\ln2}\approx0.41503749927884,
\quad t_n=\lfloor n\theta\rfloor+1.
\]

Brak remisu dla `n≥1`: równość `L_n(k)=1` oznaczałaby `3^n 2^k=4^n`, sprzeczne z jednoznacznością rozkładu na czynniki pierwsze. `t_n` można więc znaleźć bez żadnych obliczeń na liczbach zmiennoprzecinkowych jako *najmniejsze* całkowite `k` spełniające `3^n2^k>4^n`.

**Dokładny przepis całkowitoliczbowy:**

\[
\boxed{
V_n=\frac1{6^n}\sum_{k=t_n}^n\binom{n}{k}\left(3^n-2^{2n-k}\right),\qquad V_0=0.
}
\tag{28.1}
\]

Nie jest to estymator ani ograniczenie Chernoffa: liczba jest dokładnym ułamkiem wymiernym dla każdego skończonego `n`.

## 3. Nowe twierdzenie: ścisły wzrost TV dla każdej długości

Niech `t=t_{n-1}`. Ponieważ `0<θ<1`, przy przejściu `n-1→n` zachodzi albo `t_n=t`, albo `t_n=t+1`.

**Przypadek A: próg pozostaje ten sam, `t_n=t`.** Z tożsamości ogona Bernoulliego
`P_p(Bin(n,p)≥t)=P_p(Bin(n−1,p)≥t)+p P_p(Bin(n−1,p)=t−1)` wynika

\[
\boxed{
V_n-V_{n-1}=\binom{n-1}{t-1}
\left[2^{-n}-3^{-t}\left(\frac23\right)^{n-t}\right]>0.
}
\tag{28.2A}
\]

Nierówność jest ścisła, gdyż `t=t_n>nθ`, a nawias to różnica dwóch mas elementarnych dodatnia dokładnie po dodatniej stronie progu ilorazu wiarygodności `L_n(t)>1`.

**Przypadek B: próg wzrasta o 1, `t_n=t+1`.** Analogicznie
`P_p(Bin(n,p)≥t+1)=P_p(Bin(n−1,p)≥t)−(1−p)P_p(Bin(n−1,p)=t)` i

\[
\boxed{
V_n-V_{n-1}=\binom{n-1}{t}
\left[3^{-t}\left(\frac23\right)^{n-t}-2^{-n}\right]>0.
}
\tag{28.2B}
\]

Tutaj `t≤nθ`, więc `L_n(t)<1`; masa drugiego modelu jest większa. To kończy algebraiczny dowód

\[
\boxed{V_n>V_{n-1}\quad\text{dla KAŻDEGO całkowitego }n\ge1.}
\tag{28.3}
\]

W szczególności dodatkowa obserwacja zawsze poprawia optymalną rozróżnialność dla tej wybranej pary łańcuchów, choć przyrost może być bardzo mały i nie jest monotoniczny względem `n`. Nie przenosić (28.3) na każdą parę różnych procesów; dla ogólnej pary TV po wydłużeniu historii jest niezmniejszające, ale może być stałe.

## 4. Dokładne skończone progi i ich niezależna walidacja

Każde minimalne `n` sprawdzono **całkowitoliczbowo**, nie z interpolacji czy Chernoffa: testy nierówności `V_{n-1}<q≤V_n` sprowadzają się do porównań liczb całkowitych o mianowniku `6^n`.

| Wymagana TV q | Minimalne n przejść | TV dla n−1 | TV dla n | Najlepszy błąd Bayesa przy równych priors w n |
|---:|---:|---:|---:|---:|
| 0.50 | 16 | 0.493341665995942 | 0.510182167785481 | 0.244908916107259 |
| 0.75 | 46 | 0.748840876698292 | 0.751115505663230 | 0.124442247168385 |
| 0.90 | 93 | 0.897884190978637 | 0.900411326620433 | 0.049794336689784 |
| 0.95 | 133 | 0.949810434523972 | 0.950638813520630 | 0.024680593239685 |
| 0.99 | 230 | 0.989997060971982 | 0.990294190233314 | 0.004852904883343 |
| 0.999 | 374 | 0.998999171861475 | 0.999015944126666 | 0.000492027936667 |
| 0.9999 | 522 | 0.999899283640769 | 0.999901123624848 | 0.000049438187576 |

Liczba `n` z tabeli oznacza liczbę *przejść*; liczba obserwowanych stanów w pełnej ścieżce wynosi `n+1` (przy znanym wspólnym rozkładzie początkowym). Test Neymana–Pearsona osiąga te odległości; bez dostępu do liczby zmian stanów albo dla innego protokołu obserwacji wartości muszą zostać przeliczone. Tabela dotyczy matematycznego rozróżniania dwóch zadanych hipotez, nie obiektywnej „ilości informacji fizycznej” ani poziomu pewności bez modelu obserwacji.

## 5. Wykonanie reprodukcji

Skrypt standard-library-only `IW_REC10_ROT28_NC_MARKOV_EXACT_TV_INCREMENT_REPRO_20261024.py` wykonuje:

1. `n=1..1000`: dokładne wymierne porównanie obu niezależnych formuł `V_n−V_{n−1}` oraz kontrolę `>0`, bez błędu float;
2. `n≤10`: wyliczenie **wszystkich** `2^n` wektorów zmian stanów i zsumowanie pełnych absolutnych różnic prawdopodobieństw — bez użycia progowego wzoru na TV;
3. dla siedmiu progów: dokładną minimalność `V_{n−1}<q≤V_n` przez Fraction;
4. opcjonalne niezależne SciPy `binom.sf` dla 12 wielkości `n`, maksymalna różnica do dokładnej arytmetyki `1.11e−16`.

Wynik wykonania: `EXACT 1..1000 STRICT_MONOTONICITY + INCREMENT RECURSION: PASS`, `DIRECT FULL-PATH EXHAUSTIVE n<=10: PASS`, `SCIPY CROSSCHECK: PASS 1.110e−16`, `PASS ROT28`. Poziom rzetelności: dokładny dowód + niezależne obliczenie skończone; nie symulacja fizyczna.

## 6. Odejmowanie znaczenia i decyzja

- KN11 podał już θ i wykładnik Chernoffa, PRF11 R28 wyprowadził dokładną formułę TV i jej granicę. ROT28 NIE ma pierwszeństwa dla żadnego z tych wyników.
- ROT28 dodaje **lokalnie użyteczną tablicę minimalnej liczby obserwacji** i dowód, że `V_n` rośnie ściśle w każdym kroku dla tej pary. To klasyczna teoria decyzji, rachunek dwumianowy i monotoniczność informacji; nie roszczenie matematycznej nowości.
- Nie wynika stąd nowość atlasu LT4, transfer na inne łańcuchy Markowa, zmienne parametry, modele nie-Markowowskie, kwantowe instrumenty ani wspomniane w osobnych obratach fizyczne twierdzenia NASH.
- Źródłowy nieobecny REC10 ROT22 i jego procedura `NC-ALG-011` są odrębnym problemem custody; nie przypisuję ich naprawy wynikowi probabilistycznemu ROT28.
- Status `BW_INGESTED`, `NC_ACCEPTED`, `LT4_REVISION_ACCEPTED`, `EXEC_SIGN` nie jest znany; żaden z nich nie został tutaj przyznany.

**Werdykt końcowy:** `PASS_WITH_EXACT_STRICT_INCREMENT_AND_FINITE_SAMPLE_CERTIFICATE / SOURCE_FIRST / NONBLIND / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK_CASCADE`.