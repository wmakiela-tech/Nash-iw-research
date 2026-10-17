# MECH-S6 Front B — charge-pair source map and common-background response theorem

**RETURN_ID:** MECH-S6-FRONTB-CHARGE-PAIR-SOURCE-MAP-AND-COMMON-BACKGROUND-RESPONSE-THEOREM-001  
**CELL:** IW_MECH_LINEAGE_001_SUCCESSOR_05 / Mech-S6  
**DATE:** 2026-10-17  
**EXPOSURE:** PUBLIC  
**CUSTODY:** GITHUB_PENDING_BW_INGEST  
**RESULT_CLASS:** exact source-object repair / common-background linear response / no PBH endpoint  
**CLAIM_CEILING:** NO PBH BOUND / NO Yp-DH ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY CLAIM

## 1. Trigger and currentness

Front B currentness after the Wu–Xu E2 energy-support audit converged on a source-column semantics problem.

Rec9 independently froze the public Wu–Xu BlackHawk source vector as

$$
Q=(Q_{\pi^\pm},Q_{K^\pm},Q_{K_L^0},Q_{p+\bar p},Q_{n+\bar n})^T
$$

and required an explicit source-to-reaction map \(R=BQ\), because BlackHawk source columns are not automatically identical to the reaction-species populations used by the BBN executor.

This return sharpens that repair using the source's declared particle/antiparticle symmetry and derives the exact common-background consequence.

## 2. Public source semantics

The BlackHawk BBN PYTHIA table generators count charge-conjugate final states into single output channels:

- PDG \(+211\) or \(-211\) → \`pipm\`,
- PDG \(+321\) or \(-321\) → \`Kpm\`,
- PDG \(+2212\) or \(-2212\) → \`proton\`,
- PDG \(+2112\) or \(-2112\) → \`neutron\`.

Thus the corresponding final-state source objects are pair aggregates:

$$
Q_{\pi^\pm}=Q_{\pi^+}+Q_{\pi^-},
$$

$$
Q_{K^\pm}=Q_{K^+}+Q_{K^-},
$$

$$
Q_{p+\bar p}=Q_p+Q_{\bar p},
$$

$$
Q_{n+\bar n}=Q_n+Q_{\bar n}.
$$

The BlackHawk formatter divides most table yields by 2 because the Monte-Carlo event contains two **initial** particles such as \(q\bar q\) or \(gg\). The source code explicitly exempts the single-Higgs initial state from that division.

Therefore:

**INITIAL-PAIR NORMALIZATION ≠ FINAL-CHARGE SPLIT.**

BlackHawk then writes one instantaneous-secondary column each for:

\`pipm, K0L, Kpm, proton, neutron\`.

The Wu–Xu generator notebook integrates those same columns to \(dN_h/dt\).

The Wu–Xu paper additionally states that the quoted hadron multiplicities include both particles and antiparticles and that the PBH hadronization treatment produces equal numbers of nucleons and antinucleons.

## 3. Current downstream map

The current public Wu–Xu v2 solver uses the integrated aggregate source rates as follows:

- full \(Q_{\pi^\pm}\) is used as the source of \(n_{\pi^-}\),
- the same full \(Q_{\pi^\pm}\) is also used as the source of \(n_{\pi^+}\),
- full \(Q_{K^\pm}\) is used as the source of \(n_{K^-}\),
- full \(Q_{p+\bar p}\) is used as the source of \(n_{\bar p}\),
- full \(Q_{n+\bar n}\) is used as the source of \(n_{\bar n}\),
- \(Q_{K_L^0}\) is used as the source of \(n_{K_L^0}\).

No final charge-conjugate split is applied at those assignments.

Hence the present source-to-tracked-population map is not the identity on scientific objects.

## 4. Exact reaction map under the declared charge-conjugation symmetry

Let

$$
Q=
\begin{pmatrix}
Q_{\pi^\pm}\\
Q_{K^\pm}\\
Q_{K_L^0}\\
Q_{p+\bar p}\\
Q_{n+\bar n}
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
S_{\pi^-}\\
S_{\pi^+}\\
S_{K^-}\\
S_{K_L^0}\\
S_{\bar p}\\
S_{\bar n}
\end{pmatrix}.
$$

The current executor map is

$$
B_{\rm current}=
\begin{pmatrix}
1&0&0&0&0\\
1&0&0&0&0\\
0&1&0&0&0\\
0&0&1&0&0\\
0&0&0&1&0\\
0&0&0&0&1
\end{pmatrix}.
$$

Under the declared charge-conjugation-symmetric source convention, the source-native split is

$$
B_{\rm sym}=
\begin{pmatrix}
1/2&0&0&0&0\\
1/2&0&0&0&0\\
0&1/2&0&0&0\\
0&0&1&0&0\\
0&0&0&1/2&0\\
0&0&0&0&1/2
\end{pmatrix}.
$$

Therefore

$$
S_{\pi^-}=S_{\pi^+}=\frac12 Q_{\pi^\pm},
$$

$$
S_{K^-}=\frac12 Q_{K^\pm},
$$

$$
S_{\bar p}=\frac12 Q_{p+\bar p},
\qquad
S_{\bar n}=\frac12 Q_{n+\bar n},
$$

while

$$
S_{K_L^0}=Q_{K_L^0}.
$$

This is an exact object-map consequence **conditional on the source's declared charge-conjugation symmetry**.

A future charge-resolved hadronization donor should replace the \(1/2\) entries with directly resolved source components while preserving the aggregate sum identities.

## 5. Pair-sum consistency check

For the pion pair, the current map gives

$$
S_{\pi^-}^{\rm current}+S_{\pi^+}^{\rm current}
=
2Q_{\pi^\pm},
$$

whereas \(Q_{\pi^\pm}\) already denotes the pair sum.

The symmetric repaired map gives

$$
S_{\pi^-}^{\rm sym}+S_{\pi^+}^{\rm sym}
=
Q_{\pi^\pm}.
$$

This is the sharpest algebraic witness of the source-object mismatch.

## 6. Common-background population response

Freeze a prescribed common background/state history

$$
X_n(t),\quad T(t),\quad n_B(t)
$$

and consider an affected hadron population with intended source-sink law

$$
\dot n_h=S_h(t)-D_h(t)n_h.
$$

Let

$$
U_h(t,\tau)=
\exp\left[-\int_\tau^tD_h(s)\,ds\right].
$$

With initial population \(n_{h,0}\),

$$
n_h(t)
=
U_h(t,t_0)n_{h,0}
+
\int_{t_0}^tU_h(t,\tau)S_h(\tau)\,d\tau.
$$

Define

$$
n_h^{\rm hom}(t)=U_h(t,t_0)n_{h,0}
$$

and

$$
n_h^{\rm src}=n_h-n_h^{\rm hom}.
$$

If the source is rescaled by a constant \(c\), with the same prescribed background and same initial population, then exactly

$$
n_h^{(c)}
=
n_h^{\rm hom}+c\,n_h^{\rm src}.
$$

For the charge-pair repair, \(c=1/2\) for
\(\pi^-,\pi^+,K^-,\bar p,\bar n\), while \(K_L^0\) has \(c=1\).

Therefore

$$
n_h^{\rm repaired}
=
\frac12 n_h^{\rm current}
+
\frac12 n_h^{\rm hom}
$$

for each affected species in the intended floor-inactive common-background equation.

If \(n_{h,0}=0\), this reduces to

$$
n_h^{\rm repaired}=\frac12n_h^{\rm current}.
$$

## 7. Important executor-floor narrowing

The actual public Wu–Xu code initializes every hadron population with

$$
n_{h,0}=10^{-60}n_\gamma(T_f),
$$

and represents the population in log form with a floor at \(y=-100\).

For the raw executor, if \(n=e^y\), \(\epsilon=e^{-100}\), and

$$
\bar n=\max(n,\epsilon),
$$

the implemented equation is

$$
\dot n=
\alpha(n)S-Dn,
\qquad
\alpha(n)=\min(1,n/\epsilon).
$$

Thus the raw floor-active executor is not globally linear in the source amplitude.

Consequently:

**SOURCE HALF-SPLIT ≠ RAW EXECUTOR POPULATION HALF-SPLIT AUTOMATICALLY.**

The exact linear response in Sections 6–10 applies when the intended source-sink equation is used, or on intervals where the relevant executor populations are floor inactive.

Floor-active intervals require the previously derived exact residual

$$
\rho_h^{\rm floor}
=
S_h[\alpha_h-1].
$$

## 8. Directional-rate decomposition

At common supplied background, define

$$
A=\Lambda_{p\to n},
\qquad
B=\Lambda_{n\to p}.
$$

Decompose

$$
A=A_0+A_{\rm aff},
\qquad
B=B_0+B_{\rm aff},
$$

where the base \(0\) contains the unaffected \(K_L^0\) contribution plus, if nonzero initial seeds are retained, the homogeneous affected-species contribution:

$$
A_0=A_{K_L^0}+A_{\rm aff}^{\rm hom},
$$

$$
B_0=B_{K_L^0}+B_{\rm aff}^{\rm hom}.
$$

Then in the floor-inactive common-background model,

$$
A_{\rm new}
=
A_0+\frac12(A_{\rm old}-A_0)
=
\frac12(A_{\rm old}+A_0),
$$

$$
B_{\rm new}
=
B_0+\frac12(B_{\rm old}-B_0)
=
\frac12(B_{\rm old}+B_0).
$$

Hence

$$
\Delta A
=
-\frac12(A_{\rm old}-A_0),
$$

$$
\Delta B
=
-\frac12(B_{\rm old}-B_0).
$$

This is the exact common-background response of the intended linear population block to the source-map repair.

## 9. Exact forcing relation

The reduced hadronic neutron forcing is

$$
F_{\rm had}(X,t)=(1-X)A-XB.
$$

Define

$$
F_0=(1-X)A_0-XB_0.
$$

Then

$$
F_{\rm new}
=
F_0+\frac12(F_{\rm old}-F_0)
=
\frac12(F_{\rm old}+F_0),
$$

so

$$
\Delta F
=
-\frac12(F_{\rm old}-F_0).
$$

If the affected homogeneous seeds are negligible/zero, \(F_0\) is simply the \(K_L^0\) forcing at that common background.

Therefore the exact statement is:

> The charge-pair repair halves the **source-driven affected contribution** to the common-background hadronic forcing; it does not generically halve the total hadronic forcing because \(K_L^0\) is unchanged.

## 10. Exact \(R,q\) chart transformation

Where

$$
R=A+B>0,
\qquad
q=A/R,
$$

define

$$
R_0=A_0+B_0.
$$

Then

$$
R_{\rm new}
=
\frac12(R_{\rm old}+R_0).
$$

Also

$$
q_{\rm new}
=
\frac{A_{\rm old}+A_0}{R_{\rm old}+R_0}.
$$

If \(R_0>0\), write \(q_0=A_0/R_0\). Then

$$
q_{\rm new}-q_{\rm old}
=
\frac{R_0}{R_{\rm old}+R_0}
(q_0-q_{\rm old}).
$$

Thus the repaired \(q\) moves toward the base-channel directional ratio \(q_0\); it is not generally invariant.

Special case: if \(R_0=0\),

$$
R_{\rm new}=R_{\rm old}/2,
\qquad
q_{\rm new}=q_{\rm old},
\qquad
F_{\rm new}=F_{\rm old}/2.
$$

This special case must not be promoted to the general Front-B claim because \(K_L^0\) is present.

## 11. Relation to the Rec9 \(Q\mapsto BQ\) repair

Rec9's controlling Front-B repair is

$$
R=BQ
$$

with aggregate source vector

$$
Q=(Q_{\pi^\pm},Q_{K^\pm},Q_{K_L^0},Q_{p+\bar p},Q_{n+\bar n}).
$$

This return supplies the source-native matrix \(B_{\rm sym}\) under the explicit Wu–Xu charge-conjugation symmetry.

Therefore:

**DONOR SOURCE COLUMN ≠ REACTION-SPECIES INDEX,**

but the mapping is not arbitrary once the source symmetry is fixed.

## 12. Consequence for source uncertainty

A single aggregate column must not be assigned independent uncertainties to its two downstream charge branches.

For example, \(Q_{\pi^\pm}\) is one source object feeding two reaction populations through one constrained map.

Hence

**ONE SOURCE COLUMN → MULTIPLE REACTION POPULATIONS**

does not imply independent source errors.

Any donor covariance/uncertainty object must be pushed through the same \(B\) map before target propagation.

## 13. Consequence for E2c high-energy splice

A high-energy donor returning only

$$
\{\pi^\pm,K^\pm,K_L^0,p+\bar p,n+\bar n\}
$$

may be matched at the aggregate \(Q\) interface, but it still requires an explicit reaction map \(B\).

A richer charge-separated donor may instead replace both \(Q\) and \(B\), but then it is not a drop-in replacement unless its species definitions, normalization, primary convolution, support and transient-state semantics are validated together.

Thus:

**RICHER DONOR ≠ DROP-IN SOURCE REPLACEMENT.**

## 14. Cheapest decisive numerical comparator

Before any terminal lower-mass E2 extension, compare inside the already supported BlackHawk source-table domain.

Suggested PBH masses:

$$
10^9\,{\rm g},\qquad
2\times10^9\,{\rm g},\qquad
6\times10^9\,{\rm g}.
$$

Comparator A: current aggregate-to-single-species source map.

Comparator B: charge-pair-symmetric map \(B_{\rm sym}\).

Record:

1. floor-active/source-active intervals for every hadron population;
2. \(\pi^-,\pi^+,K^-,K_L^0,\bar p,\bar n\) populations;
3. common-state \(A(t),B(t)\);
4. \(R(t),q(t)\);
5. \(F_{\rm had}(t)\);
6. dynamic \(X_n(t)\);
7. the code's reduced \(Y_p\) proxy.

Only after this source-map comparator is understood should the correction be propagated into a full modern \(Y_p\)/D/H endpoint.

## 15. Claim ceiling and firewalls

Exact / source-supported:

- BlackHawk BBN \`pipm\`, \`Kpm\`, \`proton\`, \`neutron\` are charge-conjugate aggregate source columns.
- formatter division by 2 is initial-particle normalization, not final-charge splitting.
- current Wu–Xu source map sends aggregate columns into single reaction populations.
- \(B_{\rm sym}\) follows from the declared charge-conjugation-symmetric source convention.
- Sections 6–10 are exact for the intended floor-inactive common-background linear population equations.

Not run / not established:

- floor materiality for the repaired source map,
- full coupled \(A/B\) response,
- full coupled \(X_n\) response,
- modern \(Y_p/D/H\) response,
- PBH abundance-bound response,
- source-valid low-mass E2b.

Firewalls:

**PAIR-AGGREGATED SOURCE ≠ SINGLE-CHARGE SOURCE**

**INITIAL-PAIR NORMALIZATION ≠ FINAL-CHARGE SPLIT**

**SOURCE HALF-SPLIT ≠ TARGET HALF-SPLIT**

**COMMON-BACKGROUND EXACT RESPONSE ≠ FULL COUPLED TRAJECTORY RESPONSE**

**FLOOR-INACTIVE LINEARITY ≠ RAW FLOOR-ACTIVE EXECUTOR LINEARITY**

**AGGREGATE SOURCE AGREEMENT ≠ CHARGE-RESOLVED SOURCE AGREEMENT**

## 16. Source basis

Public Wu–Xu repository:

https://github.com/Fenyutanchan/Primordial-Black-Hole

Inspected v2 commit:

\`d395183674cace6c9906a8911bdeb7234ba4040d\`

Relevant Wu–Xu paths:

- \`arXiv-2509.05618/main-scan.jl\`
- \`arXiv-2509.05618/valid_hadrons_from_BlackHawk.ipynb\`
- \`arXiv-2509.05618/tool_script-hadrons_from_PBH.jl\`
- \`arXiv-2509.05618/data/out/hadrons_from_PBH.dat\`

BlackHawk v2-family public source paths independently inspected:

- \`scripts/pythia_scripts/table_up.cc\`
- \`scripts/pythia_scripts/table_gluon.cc\`
- \`scripts/pythia_scripts/formatting.c\`
- \`src/secondary.c\`

Publication:

Quan-feng Wu and Xun-Jie Xu, *Primordial black holes evaporating before Big Bang nucleosynthesis*, JCAP 02 (2026) 063, arXiv:2509.05618.

Project-level controlling repairs used only for placement:

- REC9-XH-S3-HIGH-ENERGY-TRANSIENT-HADRON-DONOR-MATRIX-REFEREE-001
- REC9-INT7-THREAD095-SPECIES-VECTOR-TARGET-BUDGET-REFEREE-001
- MECH-S6-FRONTB-WU-XU-LOG-POPULATION-FLOOR-SOURCE-INJECTION-RESIDUAL-GATE-001

## 17. Status

\`CHARGE_PAIR_AGGREGATE_SEMANTICS = PASS_EXACT\`

\`CURRENT_AGGREGATE_TO_SINGLE_SPECIES_MAP = HIGH_OBJECT_MAP_MISMATCH\`

\`B_SYM_SOURCE_MAP = PASS_EXACT_UNDER_DECLARED_SOURCE_SYMMETRY\`

\`COMMON_BACKGROUND_SOURCE_DRIVEN_HALF_RESPONSE = PASS_EXACT_FLOOR_INACTIVE\`

\`COMMON_BACKGROUND_A_B_F_TRANSFORM = PASS_EXACT_FLOOR_INACTIVE\`

\`RQ_CHART_TRANSFORM = PASS_EXACT_WHERE_R_POSITIVE\`

\`RAW_FLOOR_ACTIVE_HALF_RESPONSE = NOT_CLAIMED\`

\`SOURCE_CORRECTED_SUPPORTED_DOMAIN_RERUN = NOT_RUN\`

\`FULL_COUPLED_TARGET_IMPACT = NOT_RUN\`

\`SOURCE_VALID_E2B = OPEN\`

\`SOURCE_MATCHED_K_PBH = UNDEFINED\`

\`NO PBH BOUND / NO ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY CLAIM\`

## 18. Exact supported-domain source-table audit

The public Wu–Xu executor evaluates the hadron source table with log-linear interpolation in both PBH mass and source rate: \(\log q_h(M)\) is linearly interpolated as a function of \(\log M\).

Using that exact interpolation contract:

| \(M_{\rm PBH}\) [g] | source column | current downstream single-species source | charge-symmetric repaired single-species source |
|---:|---|---:|---:|
| \(1.0\times10^9\) | \(Q_{\pi^\pm}\) | \(4.891055\times10^5\) into each of \(\pi^-\), \(\pi^+\) | \(2.445528\times10^5\) into each |
| \(1.0\times10^9\) | \(Q_{K^\pm}\) | \(5.910594\times10^4\) into \(K^-\) | \(2.955297\times10^4\) |
| \(1.0\times10^9\) | \(Q_{p+\bar p}\) | \(3.484908\times10^4\) into \(\bar p\) | \(1.742454\times10^4\) |
| \(1.0\times10^9\) | \(Q_{n+\bar n}\) | \(3.465618\times10^4\) into \(\bar n\) | \(1.732809\times10^4\) |
| \(2.0\times10^9\) | \(Q_{\pi^\pm}\) | \(2.024939\times10^5\) into each of \(\pi^-\), \(\pi^+\) | \(1.012470\times10^5\) into each |
| \(2.0\times10^9\) | \(Q_{K^\pm}\) | \(2.455090\times10^4\) into \(K^-\) | \(1.227545\times10^4\) |
| \(2.0\times10^9\) | \(Q_{p+\bar p}\) | \(1.438015\times10^4\) into \(\bar p\) | \(7.190076\times10^3\) |
| \(2.0\times10^9\) | \(Q_{n+\bar n}\) | \(1.429513\times10^4\) into \(\bar n\) | \(7.147567\times10^3\) |
| \(6.0\times10^9\) | \(Q_{\pi^\pm}\) | \(4.822826\times10^4\) into each of \(\pi^-\), \(\pi^+\) | \(2.411413\times10^4\) into each |
| \(6.0\times10^9\) | \(Q_{K^\pm}\) | \(5.889788\times10^3\) into \(K^-\) | \(2.944894\times10^3\) |
| \(6.0\times10^9\) | \(Q_{p+\bar p}\) | \(3.400408\times10^3\) into \(\bar p\) | \(1.700204\times10^3\) |
| \(6.0\times10^9\) | \(Q_{n+\bar n}\) | \(3.376389\times10^3\) into \(\bar n\) | \(1.688194\times10^3\) |

The \(K_L^0\) source is unchanged:

- \(2.908677\times10^4\) at \(10^9\) g,
- \(1.207953\times10^4\) at \(2\times10^9\) g,
- \(2.896186\times10^3\) at \(6\times10^9\) g.

These are source-interface numbers only.

They do **not** imply a factor-two change in \(A\), \(B\), \(F_{\rm had}\), \(X_n\), \(Y_p\), D/H, or any PBH abundance bound.

The audit establishes only that the source correction is numerically material at the injection interface and is not a machine-precision or tiny-tail effect.


## 19. Mass-independent relative source-map error

For every affected tracked single-species source under the declared symmetric split,

$$
S_{\rm current}=Q_{\rm pair},
\qquad
S_{\rm sym}=\frac12Q_{\rm pair}.
$$

Therefore, wherever the aggregate source is nonzero,

$$
\frac{S_{\rm current}}{S_{\rm sym}}=2,
$$

and the relative source-interface overcount with the symmetric object as reference is exactly

$$
\frac{S_{\rm current}-S_{\rm sym}}{S_{\rm sym}}=1.
$$

Equivalently, the repair removes one half of the source currently injected into each affected tracked population:

$$
\frac{S_{\rm current}-S_{\rm sym}}{S_{\rm current}}=\frac12.
$$

This statement is mass independent because it is a source-object mapping result, not a statement about the mass dependence of the aggregate BlackHawk columns.

It applies separately to:

- \(\pi^-\),
- \(\pi^+\),
- \(K^-\),
- \(\bar p\),
- \(\bar n\).

It does not apply to \(K_L^0\), whose source column is unchanged.

Therefore the source-map mismatch is **order unity at the affected injection interface inside the already supported mass domain**.

This creates a priority ordering:

1. resolve the known charge-pair source-map mismatch on supported masses;
2. measure its effect through the current executor, including floor-active intervals;
3. only then use terminal high-energy E2b/E2c work to refine the lower-mass source extension.

This is a workflow priority, not a claim that the final BBN error is order unity.

Firewall:

**ORDER-UNITY SOURCE-MAP ERROR ≠ ORDER-UNITY BBN TARGET ERROR.**
