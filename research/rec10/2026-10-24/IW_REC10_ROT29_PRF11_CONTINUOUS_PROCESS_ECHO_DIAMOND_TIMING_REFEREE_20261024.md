# IW/NASH — REC10 ROT29
## Niezależna recenzja PRF11 R29: ścisła norma diamentowa po spin-echo i odporność na błąd czasu impulsu

**Data:** 2026-10-24  
**Komórka:** `IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10`  
**Problem:** `LT4_MONOGRAPH_CH7_7_2_CONTINUOUS_TIME_PROCESS_ARITY_AND_INTERVENTION_FACTORING_GATE`  
**Werdykt:** `PASS_WITH_SHARP_DIAMOND_AND_TIMING_GUARD`  
**Tryb:** `NONBLIND / SOURCE_FIRST / INDEPENDENT_MATHEMATICAL_REFEREE`  
**Granica:** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_OWNER_TASK / BW_PENDING`

## 1. Poprzednicy i typ obiektu

Bezpośrednio odczytany raport źródłowy **PRF11 R29**: `research/prf11/2026-10-24/IW_PRF11_R29_CONTINUOUS_SEMIGROUP_PROCESS_ECHO_AND_QUOTIENT_CONTRACT_001_20261024.md`, Git blob `5d58bcda978b99f30c0edb017cf5f99347caf7e1`, data 2026-10-24; pełna treść 20 677 znaków. PRF11 jako właściciel ma pierwszeństwo: konstrukcja dwóch procesów klasycznego szumu fazowego, identycznej całoczasowej semigrupy CPTP, odróżnialności spin-echo, prawa wszystkich idealnych sekwencji impulsów X i dodatniego twierdzenia o globalnym ilorazie z instrumentami.

Poprzedzające dojrzałe źródła PRF11: Milz–Modi (PRX Quantum 2021), Milz–Kim–Pollock–Modi (PRL 2019), Kropf–Gneiting–Buchleitner (PRX 2016), spin echo i procesy kwantowe. NC ART015 poprawnie odróżnił dwuczasowego świadka od twierdzenia dla wszystkich t. **REC10 nie rości nowości mechanizmu ani twierdzenia o pełnej normie procesora wieloczasowego.** Dodatek wyłącznie: norma diamentowa *warunkowo wybranego* kanału po danej sekwencji interwencji, dowód braku korzyści ze splątanej ancilli i ostra tolerancja niedokładnego czasu impulsu.

## 2. Tożsame niezakłócone kanały, różne procesy

Układ S=C², Pauli Z,X. Dwa modele jednorazowo przygotowanej klasycznej fazy:

- **A**: jedna stała w całym eksperymencie częstość `ξ~Cauchy(0,γ)`.
- **B**: niezależne przyrosty symetrycznego procesu Lévy'ego typu Cauchy, przyrost na przedziale Δt ma skalę γΔt.

Bez interwencji oba dają dla wszystkich t≥0 i wszystkich ρ dokładnie ten sam kanał

\[
\Phi_t(\rho)=\mathcal D_{e^{-\gamma t}}(\rho),\qquad
\mathcal D_v=\frac{1+v}{2}\,\mathrm{id}+\frac{1-v}{2}\,\operatorname{Ad}_Z.
\]

Wskazana w R29 semigrupa ma więc identyczny marginalny przebieg CPTP. Nie implikuje to globalnego intertwiningu `rU_t=V_t r` na *wszystkich przygotowaniach pełnego układu* ani kontraktu instrumentalnego `r I_a=i_a r`; zgodnie z R29 oba warunki RAZEM dawałyby dodatnią równoważność wszystkich dozwolonych historii przez indukcję. Nie wolno używać świadka echo jako falsyfikatora takiego mocniejszego globalnego twierdzenia.

## 3. Nowe twierdzenie 29.1 — pełna operacyjna odległość diamentowa dla ustalonych impulsów

Ustal `T>0`, γ>0, dowolną skończoną sekwencję czasów `Δ_j>0`, sumę `T=ΣΔ_j`. Na granicach przedziałów wstawiamy idealne, deterministyczne impulsy Pauli X i na końcu wspólną znaną korektę ramy. Nie ma postselekcji. Niech `A=Σ(-1)^(j-1)Δ_j`. Wtedy na dowolnym stanie wejściowym układu oba procesy z ustaloną historią interwencji indukują kanały

\[
\Phi_A^\mathrm{echo}=\mathcal D_u,\quad u=e^{-\gamma|A|},\qquad
\Phi_B^\mathrm{echo}=\mathcal D_v,\quad v=e^{-\gamma T}.
\]

**Twierdzenie.** Dla normy diamentowej liniowych map na `M_2(C)`, z dowolną ancillą:

\[
\boxed{\|\Phi_A^\mathrm{echo}-\Phi_B^\mathrm{echo}\|_\diamond=e^{-\gamma|A|}-e^{-\gamma T}.}\tag{29.1}
\]

**Dowód bez optymalizatora SDP.** Ponieważ `|A|≤T`, `u≥v`. Algebra:

\[
\mathcal D_u-\mathcal D_v=\frac{u-v}{2}(\mathrm{id}-\operatorname{Ad}_Z).
\]

Mapy `id` i `Ad_Z` są kanałami unitarnymi i mają normę diamentową 1, więc z trójkąta `||id−Ad_Z||_diamond≤2`, stąd górna granica `u−v` dla różnicy. Przy wejściu **bez żadnej ancilli** `ρ=|+><+|`, `ρ−ZρZ=σ_x` ma normę śladową 2. Wynikowa różnica stanów ma normę śladową **dokładnie `u−v`**. Osiąga zatem górną granicę. QED.

**Wniosek operacyjny:** przy jednym użyciu tak ustalonego protokołu i równych apriorycznych prawdopodobieństwach A/B, optymalne prawdopodobieństwo poprawnego rozpoznania jest

\[
P_{\rm succ}=\frac12+\frac14(e^{-\gamma|A|}-e^{-\gamma T}).\tag{29.2}
\]

Żadna ancilla, splątany stan początkowy ani bardziej ogólny końcowy POVM nie poprawi **tego jednego, już ustalonego protokołu** względem stanu |+> i pomiaru Pauli X. To NIE jest normą diamentową pełnego procesora wieloczasowego zoptymalizowaną po wszystkich adaptacyjnych interwencjach i kanałach działania pośredniego. Priorytet PRF11 obejmuje systemowy optymalny świadek i `TV=(u-v)/2`; REC10 jedynie rozszerza kwantyfikator na ancille i dowodzi ostrości normy diamentowej.

Dla `γ=.7`, `T=2`, równomierne echo `A=0`:

`u=1`, `v=e^(−1.4)=0.2465969639416065`, `||difference||_diamond=0.7534030360583935`; `TV=0.37670151802919677`; `P_succ=0.6883507590145984`.

## 4. Nowe twierdzenie 29.2 — ostry kontrakt błędu czasu impulsu

Dla jednej idealnej inwersji X w chwili `s=T/2+δ`, z fizycznym warunkiem `|δ|≤T/2`, ekspozycja podpisana wynosi `A=2δ`. Stąd dokładnie

\[
D_\diamond(\delta)=e^{-2\gamma|\delta|}-e^{-\gamma T},\quad
D_{\max}=1-e^{-\gamma T}.\tag{29.3}
\]

Niech dopuszczalna względna strata rozróżnialności wynosi `η∈[0,1]`. Wtedy

\[
D_\diamond(\delta)\ge (1-\eta)D_{\max}
\iff
\boxed{|\delta|\le -\frac1{2\gamma}\ln\bigl(1-\eta(1-e^{-\gamma T})\bigr).}\tag{29.4}
\]

Ten warunek jest konieczny i wystarczający, ostry. Przy nieznanym deterministycznym rozrzucie `|δ−δ_0|≤ε` (z czasem impulsu pozostającym wewnątrz `[0,T]`), wybór nominalnego środka `δ_0=0` maksymalizuje gwarantowane minimalne D, a wartość gwarantowana wynosi `e^(−2γ ε)−e^(−γT)` dla `ε≤T/2`. To elementarne minimaksowe twierdzenie dla błędu wykonania impulsu w opisanym modelu; nie mówi nic o faktycznej stabilności lasera / kubitu / sprzętu ani realnej dokładności czasu.

Dla `γ=.7,T=2`: `η=.05` daje `|δ|≤.0274271496727`; `η=.10` daje `.0559496463929`; `η=.50` daje `.3376641218868` (te same jednostki czasu modelowego co T).

## 5. Wykonane niezależne kontrole

**Plik:** `rec10_rot29_diamond_echo_repro.py` (NumPy, niezależny od skryptu PRF11). Wykonano:

1. 800 bezpośrednich 2×2 kontroli złożenia impulsów `X` i fazowych unitarności, dla liczby odcinków 1..8 i losowych faz; wszystkie identyczne z naprzemienną sumą faz z błędem <`3e−14`.
2. 3 wartości γ × 5 różnych harmonogramów × 3 wymiary ancilli (1,2,3) × 25 losowych stanów mieszanych = **1125** niezależnych kontroli numerycznych górnej granicy normy śladowej; brak przekroczeń. Dowód dla dowolnego wymiaru ancilli jest ANALITYCZNY, losowe kontrole są tylko testem implementacji.
3. Dokładna dolna granica na |+>, równa górnej dla 15 zestawów; optymalny błąd Helstroma.
4. Siedem perturbacji czasu impulsu, sześć ostrych progów η i dokładna zgodność po podstawieniu do (29.3)-(29.4).

**PASS**, bez Monte Carlo źródłowego ξ i bez generowania szumu Lévy'ego; wykorzystano ich dokładnie określone funkcje charakterystyczne z R29. Oryginalnych testów PRF11 w sesji nie uruchamiano, niezależnie weryfikowano wyłącznie ścisłe nowe twierdzenia i ich matematyczny punkt wyjścia.

## 6. Claim ceiling, rozdział zobowiązań

- **EARNED:** różnica kanałów po ustalonej legalnej sekwencji impulsów ma ścisłą normę diamentową (29.1), osiągalną bez ancilli; dokładny minimalny błąd decyzji; ostry kontrakt przy niedokładnym czasie pojedynczego impulsu; niezależny kod i 1925 punktów kontrolnych.
- **NOT EARNED:** pełne normowanie i optymalizacja po wszystkich interwencjach procesora wieloczasowego, dowolna fizyczna kwantowa realizacja Cauchy Lévy, hardware/noise estimate, rzeczywista GR/grawitacja, nowy fenomen kwantowy, dosłowna unikalność źródła, nieuwarunkowany wynik dla dowolnego sprzężenia środowiska.
- **Źródła nauki:** NC ART015 §7.2 guard; PRF11 R29 oryginalna realizacja i świadek; Milz–Modi / Milz et al. / Kropf et al. dojrzały gospodarz. Nie awansować do kanonu ani zmieniać native LT5 bez decyzji właściciela.

**Końcowa dyspozycja:** `PASS_WITH_SHARP_DIAMOND_AND_TIMING_GUARD / NONBLIND / MATURE_HOST / NO_NEW_TASK / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / BW_NOT_VERIFIED`.