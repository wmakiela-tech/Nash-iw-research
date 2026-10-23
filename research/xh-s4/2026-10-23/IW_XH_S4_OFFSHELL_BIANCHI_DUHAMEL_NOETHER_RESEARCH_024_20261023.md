# XH-S4 — obrót 024, 23 października 2026
RETURN_ID: XH-S4-OFFSHELL-BIANCHI-DUHAMEL-NOETHER-024
ROLE: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03
MODE: PRIMARY_FULLTEXT_SOURCES / EXACT_SYMBOLIC_CONTROL / FINITE_FRECHET_TEST / RESEARCH_QUESTIONS
CLAIM: NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_NASH_KJ3 / NO_NOVELTY_PRIORITY / NO_BW_INGESTION / NO_TASK_DELEGATION.
Period of source review: May 1–October 23, 2026.

## Mathematical host: exact off-shell linearized Bianchi identity
Take 3D Riemannian T³, g=e^{2u(y)}delta, u=epsilon*cos(y). Direct symbolic Christoffel/Ricci computation yields
  G_cov=Ric−R*g/2=diag(u'',(u')²,u'').
With A=e^(−2u)u'', B=e^(−2u)(u')², the mixed G^i_j=diag(A,B,A) obeys exactly
  div_y G = B'+2u'(B−A)=0.
Pure coordinate flow X=partial_y gives h=Lie_X g and delta_X G=Lie_X G=partial_y G, NONZERO on this off-shell non-Einstein vacuum background. The naive test div(delta G_mixed) is NOT a valid standalone linearized Bianchi test:
  div_y deltaG = B''+2u'(B'−A')=−2u''(B−A).
Variation of metric connection contributes precisely +2u''(B−A), so the FULL identity
  nabla_i deltaG^i_j + deltaGamma^i_ik G^k_j − deltaGamma^k_ij G^i_k =0
holds EXACTLY for arbitrary smooth u. Numeric eps=.12, y=pi/3: scalar curvature .193703423379, naive divergence +.00753527603034897, connection term −.00753527603034897, total 0. Lie_XG_cov_xx=.10392304845, yy=.01247076581. These are XH exact calculations, not a new physics theorem.
An on-shell matter completion E=G−8piT=0 would also require Lie_X T. No model T was built here, so only the algebraic dependency is established.

## New 2026 primary source #1: action-level auxiliary memory consistency
G. M. Rhythm, *A covariant curvature-history field formulation for state-dependent infinite-derivative gravity*, Annals of Physics 492 (September 2026) 170585, DOI 10.1016/j.aop.2026.170585; full https://arxiv.org/html/2608.20625 .
Its host is 4D Lorentzian metric, tensor memory Delta, scalar curvature-history C (hyperbolic equation sourced by Kretschmann) and auxiliary chi. State-dependent form factor fixes ORDER:
  A_C=B(C)Box_Delta; F_C=exp[A_C].
Its on-shell Noether identities with source Sigma_Delta=(1/sqrt−g)delta S_Delta/delta C:
  nabla T_(Delta) = +Sigma_Delta grad C,
  nabla T_(C) = −Sigma_Delta grad C;
their SUM is conserved only using Delta, C, chi field equations and complete source action. Sect VI explicitly uses Duhamel variation for noncommuting A_C and deltaA_C; formal adjoint reverses B(C)Box order to Box B(C). Retarded meaning is imposed via history-field boundary data, not by replacing C inside action before variation.
THE AUTHOR DOES NOT PROVE ghost freedom, black-hole collapse dynamics, Page curve, Hawking transfer or general retarded wellposedness.

## Independent finite ordered-operator derivative control
D=[[-2,1,1],[1,-2,1],[1,1,-2]], B=diag(b), A=BD, deltaA=diag(db)D; SciPy expm_frechet vs centered finite difference tau=1e−6.
Variable b=[.15,.30,.42], db=[.01,−.018,.012]:
  ||[A,deltaA]||=0.040626336286;
  ||Dexp(A)[deltaA]||=0.032470731485;
  ||finite_difference−Dexp||=6.10379249e−11;
  ||exp(A)deltaA−Dexp||=0.013382194757, RELATIVE ERROR=41.2131%.
Constant b=.2I, db=.015I control: commutator zero, naive derivative error ~6.5e−18. Thus the source's Duhamel requirement is mathematically meaningful, but our 3x3 control is NOT Lorentzian gravity or NASH E_g. The Duhamel identity itself is mature prior art.

## New 2026 primary source #2: essential on-shell vs off-shell gauge
Falls, Ferrero, Oglialoro, *Towards gauge independence in asymptotically safe quantum gravity*, arXiv:2607.06657v1 July7, JHEP09(2026)194; https://arxiv.org/html/2607.06657 .
The authors separate inessential off-shell gauge contributions using field redefinitions, and exhibit cancellation on shell when full fluctuation and ghost sectors are included in stated approximations. REGULATOR choices are material. NOT a proof of general nonperturbative gauge independence; different mathematical host from XH classical 3D Bianchi and the Rhythm auxiliary-memory action.

## New 2026 primary source #3: Ward/BRST, distinct quantum host
Frenkel, Martins-Filho, *Quantum Gravity in the Landau background gauge*, arXiv:2610.06564v1 Oct5, PRD Oct21 DOI 10.1103/77r5-31gd; https://arxiv.org/html/2610.06564 .
Their background Ward and BRST constraints govern 1-loop effective action; higher-loop finiteness suggestion is unproved. Do not conflate a quantum Ward identity or a one-loop self-energy with a classical tensor TT or an explicit conserved NASH stress source.

## Typed research links and questions
1. XH023 non-Einstein TT leakage vs XH024 Noether conservation: DIFFERENT TEST TARGETS. Preservation of a spatial TT subspace is neither necessary nor sufficient for full action-level diffeomorphism invariance.
2. Rhythm on-shell two-sector exchange vs XH offshell deltaGamma cancellation: SAME BOOKKEEPING MOTIF (missing terms matter), DIFFERENT PHYSICAL/MATHEMATICAL HOST.
3. Rhythm ordered B(C)Box vs 3x3 SciPy Frechet: SAME ALGEBRAIC DERIVATIVE, DIFFERENT FIELD, CAUSAL AND UNBOUNDED-OPERATOR HOST.
4. Falls essential gauge and Frenkel Ward: BOTH quantum, different control conditions; neither gives gauge-invariant interpretation of source fixed P_TT finite residual.
5. DTC E_lin=I+alpha dx²Delta_center is NOT e^{B(C)Box}, not automatically action-derived or causal. No direct theorem transfer.

Q62/P0: For any candidate NASH background, test full linearized Bianchi including deltaGamma, metric and source variations. A naive div(deltaG) fails exact counterexample.
Q63/P0: Define ON-SHELL contract: full equations E[g,fields]=0, gauge/background, tensor domains, source and boundary. Otherwise do not interpret pure-gauge deltaG.
Q64/P0: Noncommuting operator variation must use Duhamel/Frechet and fixed ordering; false scalar differentiation is falsified by 41% toy error.
Q65/P0: Include all memory/auxiliary equations and stress tensors before judging conservation, rather than asking separate-sector divergence to vanish.
Q66/P1: Which NASH claims could become genuine gauge-quotient/on-shell observables rather than regulator/field-choice effects? Requires appropriate quantum or classical host, not these sources alone.
Q67/P0: Conservation/Noether is independent of pole positivity, ghosts, causality/wellposedness and observational evidence. Audit each separately.
Q68/P1: What experiment could distinguish a real curvature-history mechanism from a model-conditioned latent quantity? Link PRF11 identifiability with a lawful observable carrier; no physical NASH result yet.

## Local reproduction and limitation
ZIP: IW_XH_S4_024_BIANCHI_DUHAMEL_REPRODUCIBILITY.zip, SHA256 7cd1c34879f00aeba368b9a44cf061930feb3c5294d05e5317a3abcd35c8427e.
Contents standalone SymPy/SciPy Python (SHA256 9306890b42ad373f7d475a56e726ab50fd53bf1df67e60faa7bc4a231712d8e4), JSON result (SHA256 b76a16963cb29aecfaddcd75809b9c1b6b7fb003b4e592c0b582db6a67f8b610), README, manifest.
CRC PASS, fresh extraction, script rerun exit0 and JSON byte hash equals original: CLEAN_REPLAY_PASS.
No Lorentzian equation solve, no simulation of Rhythm C/chi/Delta, no NASH DTC calculations, no universal operator norm bound, no physical K/J3 invariant. Repo write/readback and Slack receipts must be checked separately.
