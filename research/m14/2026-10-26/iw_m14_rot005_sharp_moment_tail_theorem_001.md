# M14 ROT005 — exact sharp four-moment tail theorem
artifact_id: IW_M14_ROT005_SHARP_FOUR_MOMENT_TAIL_THEOREM_001_20261026
exposure: PUBLIC
claim_ceiling: EXACT_CLASSICAL_PROBABILITY / NO_NOVELTY / NO_PHYSICS / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
date: 2026-10-26

Let X be symmetric with E[X²]=v>0, E[X⁴]=m4>v² and threshold a>0 satisfying b=a²>m4/v. Then the sharp attainable one-sided probability interval is

0 <= Pr(X>=a) <= (m4-v²)/(2*((m4-v²)+(b-v)²)).

Proof: put Y=X². Its mean is v and variance s²=m4−v². Symmetry gives Pr(X>=a)=Pr(Y>=b)/2. For any y0<b, the pointwise inequality 1_{Y>=b}<=(Y−y0)²/(b−y0)² implies Pr(Y>=b)<=(s²+(v−y0)²)/(b−y0)². Optimize at y0=v−s²/(b−v)>=0. Equality: Y=y0 or b, upper-atom probability q=s²/(s²+(b−v)²); take equally likely signs of sqrt(Y). Lower extremizer: Y=0 or m4/v with probability v²/m4 for latter, also take equally likely signs. Since m4/v<b, tail is zero. Convex mixtures realize intermediate values, preserving all four moments.

At v=1/100, m4=3/10000 (Gaussian fourth moment), a=9/20, upper=16/5961=0.00268411340379131, lower=0. Gaussian N(0,v) tail=3.3976731247300615e−6, upper ratio 789.985765333.

Lower distribution: mass 2/3 at 0, mass 1/6 at each ±sqrt(3/100). Upper distribution: mass 16/5961 at each ±9/20; mass 5929/11922 at each ±sqrt(69/7700). Each law EXACTly shares mean 0, variance 1/100, third moment 0, fourth moment 3/10000. Upper threshold atom counted for >=; for > the bound is a supremum.

Original scientific host XH-S4 ROT029; Geeky-S9 earlier covariance-matched high-tail and cutoff. Mature Cantelli/moment-bound work Bertsimas–Popescu 2005, DOI 10.1137/S1052623401399903. LT REV023 Ch6–7 may use as optional mathematical counterexample, not as adopted science. Neither cosmological nor physical-source inference. NO_CANON / NO_EXEC_SIGN / NO_NOVELTY.
