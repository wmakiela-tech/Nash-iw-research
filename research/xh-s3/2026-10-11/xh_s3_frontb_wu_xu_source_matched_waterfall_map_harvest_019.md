---
artifact_id: XH-S3-FRONTB-WU-XU-SOURCE-MATCHED-WATERFALL-MAP-HARVEST-019
bw_ingestion_event_id: ING-20261011-0015
bw_qualification_state: FRONTB_WUXU_SOURCE_MATCHED_WATERFALL
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: EXTERNAL_EVIDENCE_NO_AUTHORITY
archive_mode: PUBLIC_ARTIFACT
sync_state: SYNCED
source_surface: GOOGLE_DRIVE
source_revision: AHj4eMT3XC-ykX7gFKJrT9cBiLvxX7pyLH1cnxLUH-Q48qVQ29ACii8pXSIW-K00sxIUuF4srDuAe0nMsDR6DiVqWnFC6K7wgjA9jDaFHMs
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# XH-S3-FRONTB-WU-XU-SOURCE-MATCHED-WATERFALL-MAP-HARVEST-019

> Public-safe mirror of the BW-linked Drive source. BW controls lifecycle/currentness; this GitHub body does not upgrade scientific authority. Private provider locators were redacted during mirroring.

XH-S3 / FRONT B — WU–XU SOURCE-MATCHED WATERFALL MAP HARVEST 019
RETURN_ID
XH-S3-FRONTB-WU-XU-SOURCE-MATCHED-WATERFALL-MAP-HARVEST-019
RESULT
WU–XU PUBLIC PBH SOLVER ADMITS AN EXACT TWO-RATE PROJECTION FOR HADRONIC n↔p.
A SOURCE-MATCHED PBH DYNAMICAL-EQUILIBRIUM CLOSURE CAN BE WRITTEN DIRECTLY FROM THE PUBLIC ODEs.
THE REDUCED WATERFALL DESCRIPTOR IS EXACTLY REPLAY-SUFFICIENT FOR THE HADRONIC X_n RHS ONCE THE HADRON DENSITIES ARE GIVEN.
THE REMAINING GAP IS NOT FORMULATION BUT SOURCE-MATCHED VALIDATION OF THE ALGEBRAIC CLOSURE AGAINST THE FULL HADRON ODE + FINAL BBN TARGET.
NO PBH ENDPOINT / NO BOUND RELEASE.
FIREWALL
Exact projection of an existing full state != exact closure of the full state.
Source-matched algebraic fixed point != validated physical approximation.
Replay sufficiency for X_n != sufficiency for Y_p or D/H.
Monochromatic Wu–Xu source != B2 joint-carrier validation.
No canon / no EXEC sign / no novelty.
1. PRIMARY PUBLIC OBJECT
Sources:
[Wu–Xu JCAP 2026]
[Wu–Xu public GitHub]
Inspected current public paper tree:
Fenyutanchan/Primordial-Black-Hole
commit family d395183674cace6c9906a8911bdeb7234ba4040d.
Relevant files:
arXiv-2509.05618/main-scan.jl
arXiv-2509.05618/tool_script-parameters.jl
arXiv-2509.05618/tool_script-hadrons_from_PBH.jl
The full hadronic state evolved by the root code is:
X_n,
n_{pi-},
n_{pi+},
n_{K-},
n_{K0L},
n_{pbar},
n_{nbar},
plus cosmological/PBH variables.
2. EXACT TWO-DIRECTION RATE PROJECTION
The public Wu–Xu X_n equation can be grouped exactly as
dX_n/dt |_had
=
(1-X_n) Lambda_{p->n}
-
X_n Lambda_{n->p},
with
Lambda_{p->n}
=
n_{pi-} sigma v_{pi-,p->n}
+
n_{K-} sigma v_{K-,p->n}
+
n_{K0L} sigma v_{K0L,p->n}
+
n_{nbar} sigma v_{n nbar,p->n},
and
Lambda_{n->p}
=
n_{pi+} sigma v_{pi+,n->p}
+
n_{K-} sigma v_{K-,n->p}
+
n_{K0L} sigma v_{K0L,n->p}
+
n_{pbar} sigma v_{p pbar,n->p}.
Therefore define
R_h
=
Lambda_{p->n}+Lambda_{n->p},
X_n^{qs}
=
Lambda_{p->n}/R_h
when R_h>0.
Then exactly:
dX_n/dt |_had
=
R_h (X_n^{qs}-X_n).
This is not an approximation.
It is an algebraic refactorization of the source code’s hadronic contribution.
CONSEQUENCE:
{X_n^{qs}(t), R_h(t)}
is EXACTLY replay-sufficient for the hadronic contribution to the reduced neutron-fraction equation, provided the same background/weak terms are supplied.
This independently confirms the INT7/NC descriptor interpretation using the actual PBH solver rather than a donor model.
3. SOURCE-NATIVE PBH DYNAMICAL-EQUILIBRIUM MAP
The public hadron equations have the generic form
dn_h/dt = S_h - L_h(X_n,T,n_B) n_h.
Setting dn_h/dt=0 gives explicit state-aware algebraic populations.
For charged pions:
n_{pi-}^*
=
S_pi /
[Gamma_pi + sigma v_{pi-,p->n}(T)(1-X_n)n_B],
n_{pi+}^*
=
S_pi /
[Gamma_pi + sigma v_{pi+,n->p}(T)X_n n_B].
For K-:
n_{K-}^*
=
S_K /
[
Gamma_K
+
n_B X_n (sigma v_{K-,n->n}+sigma v_{K-,n->p})
+
n_B (1-X_n)(sigma v_{K-,p->n}+sigma v_{K-,p->p})
].
For K0L:
n_{K0L}^*
=
S_{K0L} /
[
Gamma_{K0L}
+
n_B X_n (sigma v_{K0L,n->n}+sigma v_{K0L,n->p})
+
n_B (1-X_n)(sigma v_{K0L,p->n}+sigma v_{K0L,p->p})
].
For antiprotons:
n_{pbar}^*
=
S_p /
[
n_B X_n sigma v_{p pbar,n->p}
+
n_B(1-X_n) sigma v_{p pbar,p->p}
].
For antineutrons:
n_{nbar}^*
=
S_n /
[
n_B X_n sigma v_{n nbar,n->n}
+
n_B(1-X_n) sigma v_{n nbar,p->n}
].
Here the PBH source functions in the public code are
S_pi
=
dN_pi/dt(m_PBH) n_PBH,
S_K
=
dN_K/dt(m_PBH) n_PBH,
S_K0L
=
dN_K0L/dt(m_PBH) n_PBH,
S_p
=
dN_p/dt(m_PBH) n_PBH,
S_n
=
dN_n/dt(m_PBH) n_PBH.
These five injection functions are read/interpolated from the public hadronization output as functions of current PBH mass.
4. PBH-SPECIFIC FIXED-POINT CLOSURE
Substitute the six algebraic populations n_h^*(X_n,T,n_B,m_PBH,n_PBH) into the exact rate projection.
This gives:
Lambda_{p->n}^*(X_n; state),
Lambda_{n->p}^*(X_n; state),
and therefore
X_{n,DE}^{qs}(X_n; state)
=
Lambda_{p->n}^*/
(Lambda_{p->n}^*+Lambda_{n->p}^*).
The hadron-dominated instantaneous fixed point solves
X_n
=
X_{n,DE}^{qs}(X_n; state).
More generally, with standard weak rates retained, the reduced X_n equation is:
dX_n/dt
=
(dX_n/dt)_SM
-
X_n/tau_n
+
R_h^*(X_n;state)
[
X_{n,DE}^{qs}(X_n;state)-X_n
].
This is a directly source-matched PBH DE candidate constructed from the public Wu–Xu equations.
IMPORTANT:
This has not been numerically validated here against the original six-hadron ODE.
It is a candidate closure, not a released adapter.
5. WHY MULTI-SPECIES IS THE REAL FEEDBACK GATE
For one prescribed dominant species with externally given branching,
X_n^{qs} can be treated as a prescribed directional ratio.
In the Wu–Xu multi-species system:
- each n_h^* has a different X_n dependence in its denominator;
- pion Coulomb enhancement depends on T;
- K- has both conversion and non-conversion depletion channels;
- K0L has different directional coefficients;
- pbar and nbar depletion are asymmetric;
- species injection ratios change with m_PBH through Hawking/hadronization evolution.
Therefore X_n^{qs} itself becomes an implicit function of X_n and of the evolving source composition.
This precisely realizes the NC/DRAFT017 distinction:
BRANCHING_PRESCRIBED
vs
BRANCHING_STATE_DEPENDENT.
The multi-species gate is not abstract.
It is present explicitly in the source-native PBH equations.
6. DIRECTIONAL CROSS-SECTION STRUCTURE IN THE PUBLIC CODE
The public parameter file uses, among others:
pi+ n->p: 1.7 mbarn
pi- p->n: 1.5 mbarn × Coulomb factor
K- n->p: 26 mbarn
K- n->n: 34 mbarn
K- p->n: 31 mbarn × Coulomb factor
K- p->p: 14.5 mbarn × Coulomb factor
K0L n->p: 7 mbarn
K0L n->n: 10 mbarn
K0L p->n: 7 mbarn
K0L p->p: 10 mbarn
n nbar p->n: 28 mbarn
p pbar n->p: 28 mbarn,
with corresponding nonconversion annihilation channels 37 mbarn.
Thus:
K0L conversion is directionally symmetric at the quoted conversion-cross-section level,
whereas charged pion/K- contributions carry T/state asymmetry,
and pbar/nbar contributions split by species abundance.
This reinforces that the source-matched directional ratio cannot be inferred from total hadron multiplicity alone.
7. EXACT REDUCED DESCRIPTOR MAP FROM FULL WU–XU TRAJECTORY
Given any full Wu–Xu trajectory, no approximation is needed to compute:
D1
Lambda_{p->n}(t),
D2
Lambda_{n->p}(t),
D3
R_h(t)=Lambda_{p->n}+Lambda_{n->p},
D4
X_n^{qs}(t)=Lambda_{p->n}/R_h,
D5
A_h(t)=
(Lambda_{p->n}-Lambda_{n->p})/R_h
=
2X_n^{qs}-1,
D6
species contribution fractions to Lambda_{p->n} and Lambda_{n->p}.
Hence the reduced descriptor can be extracted as a diagnostic from existing source-native full solutions without changing the physical model.
8. EXACT REPLAY-SUFFICIENCY CLAIM
For the neutron-fraction equation only:
{X_n^{qs}(t),R_h(t)}
+
the same standard weak/decay terms
+
the same initial X_n
reconstructs exactly the same X_n(t) as the full model if the descriptor trajectory was extracted from that full model.
This is a REPLAY statement.
It does NOT imply:
- the descriptor can be generated independently without full hadron state;
- it is source-family predictive;
- it preserves full nuclear abundances;
- it is sufficient under a changed PBH/B2 source.
Therefore:
TRAJECTORY DESCRIPTOR SUFFICIENCY
!=
CONSTITUTIVE CLOSURE SUFFICIENCY.
9. THE NEW SOURCE-NATIVE ADMISSION TEST
The source-matched DE candidate supplies its own predicted descriptor:
{X_{n,DE}^{qs}(t), R_{h,DE}(t)}.
The full Wu–Xu ODE supplies:
{X_{n,FULL}^{qs}(t), R_{h,FULL}(t)}.
The cheapest PBH-specific closure test is therefore not initially a full Yp likelihood.
Compare, on the same frozen source:
A
X_n^{qs,DE}(t)
vs
X_n^{qs,FULL}(t),
B
R_h^{DE}(t)
vs
R_h^{FULL}(t),
C
species directional fractions,
D
the reconstructed X_n(t) under each descriptor.
This directly tests whether the algebraic DE constitutive law reproduces the full PBH hadron dynamics at the reduced level relevant to n/p.
Only after passing this should the target-weighted Yp/D-H validation be activated.
10. SOURCE-MATCHED FAILURE MODES
F1 FIXED-POINT NONUNIQUENESS / POOR CONDITIONING
The implicit X_n closure may have multiple/no stable numerical fixed points or poor local contraction.
F2 COMPOSITION ERROR
DE may reproduce total R_h but mispredict species weights, shifting X_n^{qs}.
F3 DIRECTIONAL ERROR
Common source amplitude can be accurate while p->n:n->p ratio is wrong.
F4 THRESHOLD/HADRONIZATION ERROR
m_PBH evolution changes hadron species ratios; interpolation/threshold epochs may stress the reduced map.
F5 ANTINUCLEON SECTOR
No intrinsic decay term appears in the public pbar/nbar number equations; depletion is interaction-controlled and may have a different fast/slow hierarchy from mesons.
F6 BACKGROUND COUPLING
n_B, T and the PBH background evolve simultaneously; a closure test must use the same source/background history.
11. B2 EXTENSION
For a legal B2 carrier dmu(M_i,t_f), replace each monochromatic source S_h by the total population source:
Q_h(t)
=
a(t)^-3
∫ chi(t;M_i,t_f)
R_h^{emit}(M(t;M_i,t_f))
dmu(M_i,t_f).
Then the SAME source-matched algebraic hadron closure can be formally evaluated with Q_h in place of S_h.
This yields a clean architecture:
dmu_B2
-> five total hadron source functions Q_h(t)
-> algebraic state-aware hadron populations
-> {X_n^{qs},R_h}
-> reduced X_n/BBN receiver.
This is structural compatibility only.
No B2 numerical validation is supplied by Wu–Xu.
12. IMPORTANT SOURCE SEMANTICS
The public Wu–Xu root executor remains monochromatic:
magic(m_PBH,beta_PBH)
with formation time tied to mass.
Therefore:
the derived algebraic closure is SOURCE-MATCHED to the Wu–Xu hadronic microphysics,
but B2 carrier generalization remains a project-side extension.
Do not call the B2 closure public-source validated until:
- the population source construction is validated;
- the DE/full descriptor comparison passes on representative B2 histories;
- target-relative Yp/D-H error is controlled.
13. RELATION TO 015–018
015:
decaying-relic literature proves state-aware DE can work and validates it against full Boltzmann evolution.
016–017:
target-weighted weak-rate response is the correct final certification layer; functional-kernel method is mature prior art.
018:
waterfall reduction suggests directional ratio + relaxation strength may be cheaper than dense kernels.
019:
the exact PBH equations themselves provide:
- the two-direction descriptor map;
- an explicit PBH algebraic DE candidate;
- the exact multi-species feedback gate.
Thus the next Front B problem is no longer:
“Can one formulate a PBH DE closure?”
Answer:
YES, directly from the public equations.
The remaining question is:
“Does this source-matched closure reproduce the full PBH hadron dynamics and final BBN target to declared tolerance?”
14. NO EXTERNAL MODEL USE
No additional AI model was invoked.
The question was source-code-native and could be resolved exactly from the public solver.
A second-model opinion would add less evidence than direct code inspection and would increase Moderator coordination cost.
15. STATUS
WU_XU_TWO_DIRECTION_RATE_PROJECTION = PASS / EXACT.
WU_XU_REDUCED_DESCRIPTOR_REPLAY_SUFFICIENCY_FOR_XN = PASS / EXACT.
WU_XU_SOURCE_MATCHED_ALGEBRAIC_DE_CANDIDATE = CONSTRUCTED FROM PUBLIC EQUATIONS.
MULTI_SPECIES_STATE_DEPENDENT_BRANCHING_GATE = SOURCE-NATIVE / PASS.
PBH_DE_VS_FULL_DESCRIPTOR_VALIDATION = NOT RUN.
PBH_Yp_DH_TARGET_VALIDATION = NOT RUN.
B2_POPULATION_TRANSFER = STRUCTURALLY DEFINED / NOT VALIDATED.
READY_MADE_PBH_REDUCED_ADAPTER = NOT YET VALIDATED.
SOURCE_MATCHED_K_PBH = UNDEFINED.
NO PBH BOUND / NO ENDPOINT RELEASE.
NO CANON / NO EXEC_SIGN / NO NOVELTY / SCIENCE_FIRST.
SOURCES
[Wu–Xu JCAP 2026]
[Wu–Xu public GitHub]
[Kohri 2001 hadronic cross sections]
[Kohri 1999 K0L cross sections]
