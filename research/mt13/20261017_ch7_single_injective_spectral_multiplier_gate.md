# MT13 — monograph Ch7 spectral intertwiners: one injective multiplier can suffice
Date: 2026-10-17. Scoped independent mathematical audit. NO NOVELTY / NO CANON / NO EXEC.

## Controlling context
LT4 Chapter VII: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt4/2026-10-15/lt4_monograph_ch7_fidelity_synthesis_working_20261015.md
INT7 audit 2026-10-17 reports semigroup intertwining J exp(-t A)=exp(-t B)J for all t>=0 implies bounded Borel spectral intertwining; warns that **one spectral multiplier does not in general imply full functional calculus intertwining**. This note adds the precise injective-multiplier qualification; it does not challenge the valid semigroup proof.

## Proposition (single spectrally separating witness)
Let A and B be nonnegative (possibly unbounded) self-adjoint operators on Hilbert spaces H1 and H2, J:H1->H2 bounded, and t_*>0. If J exp(-t_* A)=exp(-t_* B) J, then J m(A)=m(B) J for every bounded Borel m:[0,infinity)->C.

Proof: T=exp(-t_*A), S=exp(-t_*B) are bounded self-adjoint contractions. JT=SJ. By polynomial approximation and the spectral theorem, J f(T)=f(S)J for all bounded Borel functions f on [0,1] (first continuous functions, then spectral projections by bounded monotone approximation, then bounded Borel). Since h(lambda)=exp(-t_*lambda) is injective on [0,infinity), for any bounded Borel m there is a bounded Borel f on [0,1] such that f(h(lambda))=m(lambda) for lambda>=0 (set f(0) arbitrarily, f(u)=m(-log u/t_*) for u>0). Hence m(A)=f(T) and m(B)=f(S), proving the claim. The potential spectral projection at zero for S/T is null because exponential of a self-adjoint operator has trivial kernel; f(0) is immaterial. QED.

More generally a bounded real-valued Borel h that is injective on a Borel set containing both spectra permits the same conclusion by Borel inverse (standard Borel measurable injective-image theorem). For continuous strictly monotone h, this is elementary. One-point intertwining of a non-injective h can fail dramatically: H1=H2=C, A=0, B=2, h(lambda)=cos(pi*lambda) gives h(A)=h(B)=1 and J=1, yet m(lambda)=lambda/(1+lambda) distinguishes A and B.

IMPORTANT LIMITS:
- A single multiplier witness works only with explicit spectral separation, compatible operator classes and bounded J. The statement does not apply to arbitrary semiconjugation of nonlinear spaces, nor to unbounded J without domains.
- Full bounded Borel functional-calculus intertwining of generator operators still does NOT imply equality of multi-time quantum process laws, physical intervention equivalence, microcarrier identification or CPTP extension.
- This is standard spectral theorem content, not novel mathematical physics.

Suggested optional editorial addendum near Chapter VII §7.8: 'Nie każdy pojedynczy mnożnik wystarcza; jednak jeden mnożnik różnowartościowy na odpowiednim widmie (np. exp(-t lambda), t>0, dla nieujemnych operatorów samosprzężonych) już wyznacza pełny ograniczony borelowski rachunek funkcyjny przy ograniczonym splataczu. Kryterium jest separacja widma, nie liczba sprawdzonych funkcji.'
Placement is recommendation to LT4 owner; no manuscript mutation or automatic status advancement. REV020 / P2 unchanged. No new task cascade.
