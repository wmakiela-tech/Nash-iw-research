\[
L_{\rm pair}=2(\Delta+2t_{\pi/2}+t_d)+t_r
 =1.7783185307179588/\gamma.\tag{R24.6}
\]

Pełny budżet czasu na parę, razem z resetem sensora także *po* drugim pomiarze, to

\[
T_{\rm pair,worst}=2(\Delta+2t_{\pi/2}+t_d+t_r)
=1.8283185307179588/\gamma.\tag{R24.7}
\]

Jeżeli trit X/Y/Z rozkłada się według wag R23, oczekiwany całkowity czas na parę wynosi 2[Δ+tπ/2(1+w_X+w_Y)+t_d+t_r]=1.6335397861953915/γ. Podawany czas najgorszy używa dłuższej analizy w obu odczytach; nie jest średnią.

**A source hazard contract H:** założenie, że *warunkowo względem dowolnej historii przed parą* prawdopodobieństwo braku zmiany ξ przez tę parę wynosi co najmniej s=e^(−λ L_pair), np. dla procesu Poissona z intensywnością λ niezależnego od prywatnego losowania osi. Nie wystarczy sama bezwarunkowa wartość Pr(no reset)=s, jeżeli silna zależność między parami może skupić wszystkie resety w jednym podzbiorze eksperymentów.

Ponieważ przy braku resetu p_A≥a0=.576 i przy jakimkolwiek resecie w środku odczytu wolno przyjąć tylko p_A≥0, zachodzi przy każdym warunkowym stanie historii

\[
\boxed{a(\lambda,\eta)
=\tfrac12+(1-2\eta)^2\left[a_0e^{-\lambda L_{\rm pair}}-\tfrac12\right]
\le \Pr_A(\mathrm{same}|\text{past}),}\tag{R24.8}
\]

\[
\boxed{\Pr_B(\mathrm{same}|\text{past})\le
 b(\eta)=\tfrac12+(1-2\eta)^2(b_0-\tfrac12).}\tag{R24.9}
\]

Dodatni certyfikowany kontrast wymaga e^(−λ L_pair) a0>b0, czyli

\[
\boxed{\lambda/\gamma<\frac{\log(.576/.526)}{1.7783185307179588}
 \approx0.0510630949347.}\tag{R24.10}
\]

Gdy kontrakt H ogranicza zmiany ξ tylko do przerwy MIĘDZY dwoma pełnymi odczytami (nie w ich wnętrzu), można użyć (R24.5) w gałęzi z resetem, uzyskując a0 s+.31(1−s). Przy konserwatywnie tym samym ograniczeniu L_pair wystarcza

\[
\boxed{\lambda/\gamma < \frac{\log[(.576-.31)/(.526-.31)]}{1.7783185307179588}
\approx 0.1170869546152.}\tag{R24.11}
\]

Ostatnia wartość jest konserwatywna: realne okno dopuszczalnego resetu w modelu 'only between shots' jest krótsze od L_pair. Nie należy mieszać (R24.10) i (R24.11) bez deklaracji *kiedy* ξ może skoczyć.

**Dominacja stochastyczna i błędy.** Niech Z_j=1 oznacza zgodne zapisane odczyty pary j, a K=Σ Z_j. Przy założeniu warunkowego po każdym przebiegu bound Pr_A(Z_j=1|history)≥a oraz Pr_B(Z_j=1|history)≤b, sprzężenie poprzez świeże jednostajne zmienne U_j daje Z_j^A≥1[U_j≤a] i Z_j^B≤1[U_j≤b]. Dlatego bez iid historii ξ, dla decyzji 'A iff K≥k':

\[
\Pr_A(K<k)\le \operatorname{BinomCDF}(k-1;N,a),\qquad
\Pr_B(K\ge k)\le \operatorname{BinomSF}(k-1;N,b).\tag{R24.12}
\]

