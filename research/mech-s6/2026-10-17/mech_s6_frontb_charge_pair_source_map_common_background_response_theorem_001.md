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

[
Q=(Q_{pi^pm},Q_{K^pm},Q_{K_L^0},Q_{p+ar p},Q_{n+ar n})^T
]

and required an explicit source-to-reaction map (R=BQ), because BlackHawk source columns are not automatically identical to the reaction-species populations used by the BBN executor.

This return sharpens that repair using the source's declared particle/antiparticle symmetry and derives the exact common-background consequence.

## 2. Public source semantics

The BlackHawk BBN PYTHIA table generators count charge-conjugate final states into single output channels:

- PDG (+211) or (-211) -> `pipm`,
- PDG (+321) or (-321) -> `Kpm`,
- PDG (+2212) or (-2212) -> `proton`,
- PDG (+2112) or (-2112) -> `neutron`.

Thus the corresponding final-state source objects are pair aggregates:

[
Q_{pi^pm}=Q_{pi^+}+Q_{pi^-},
]
[
Q_{K^pm}=Q_{K^+}+Q_{K^-},
]
[
Q_{p+ar p}=Q_p+Q_{ar p},
]
[
Q_{n+ar n}=Q_n+Q_{ar n}.
]

The BlackHawk formatter divides most table yields by 2 because the Monte-Carlo event contains two **initial** particles such as (qar q) or (gg). The source code explicitly exempts the single-Higgs initial state from that division.

Therefore:

[
	ext{INITIAL-PAIR NORMALIZATION}
eq	ext{FINAL-CHARGE SPLIT}.
]

BlackHawk then writes one instantaneous-secondary column each for:

`pipm, K0L, Kpm, proton, neutron`.

The Wu–Xu generator notebook integrates those same columns to (dN_h/dt).

The Wu–Xu paper additionally states that the quoted hadron multiplicities include both particles and antiparticles and that the PBH hadronization treatment produces equal numbers of nucleons and antinucleons.

## 3. Current downstream map

The current public Wu–Xu v2 solver uses the integrated aggregate source rates as follows:

- full (Q_{pi^pm}) is used as the source of (n_{pi^-}),
- the same full (Q_{pi^pm}) is also used as the source of (n_{pi^+}),
- full (Q_{K^pm}) is used as the source of (n_{K^-}),
- full (Q_{p+ar p}) is used as the source of (n_{ar p}),
- full (Q_{n+ar n}) is used as the source of (n_{ar n}),
- (Q_{K_L^0}) is used as the source of (n_{K_L^0}).

No final charge-conjugate split is applied at those assignments.

Hence the present source-to-tracked-population map is not the identity on scientific objects.

## 4. Exact reaction map under the declared charge-conjugation symmetry

Let

[
Q=
egin{pmatrix}
Q_{pi^pm}\
Q_{K^pm}\
Q_{K_L^0}\
Q_{p+ar p}\
Q_{n+ar n}
end{pmatrix},
qquad
S=
egin{pmatrix}
S_{pi^-}\
S_{pi^+}\
S_{K^-}\
S_{K_L^0}\
S_{ar p}\
S_{ar n}
end{pmatrix}.
]

The current executor map is

[
B_{m current}=
egin{pmatrix}
1&0&0&0&0\
1&0&0&0&0\
0&1&0&0&0\
0&0&1&0&0\
0&0&0&1&0\
0&0&0&0&1
end{pmatrix}.
]

Under the declared charge-conjugation-symmetric source convention, the source-native split is

[
B_{m sym}=
egin{pmatrix}
1/2&0&0&0&0\
1/2&0&0&0&0\
0&1/2&0&0&0\
0&0&1&0&0\
0&0&0&1/2&0\
0&0&0&0&1/2
end{pmatrix}.
]

Therefore

[
S_{pi^-}=S_{pi^+}=rac12 Q_{pi^pm},
]
[
S_{K^-}=rac12 Q_{K^pm},
]
[
S_{ar p}=rac12 Q_{p+ar p},
qquad
S_{ar n}=rac12 Q_{n+ar n},
]
while
[
S_{K_L^0}=Q_{K_L^0}.
]

This is an exact object-map consequence **conditional on the source's declared charge-conjugation symmetry**.

A future charge-resolved hadronization donor should replace the (1/2) entries with directly resolved source components while preserving the aggregate sum identities.

## 5. Pair-sum consistency check

For the pion pair, the current map gives

[
S_{pi^-}^{m current}+S_{pi^+}^{m current}
=
2Q_{pi^pm},
]

whereas (Q_{pi^pm}) already denotes the pair sum.

The symmetric repaired map gives

[
S_{pi^-}^{m sym}+S_{pi^+}^{m sym}
=
Q_{pi^pm}.
]

This is the sharpest algebraic witness of the source-object mismatch.

## 6. Common-background population response

Freeze a prescribed common background/state history

[
X_n(t),quad T(t),quad n_B(t)
]

and consider an affected hadron population with intended source-sink law

[
dot n_h=S_h(t)-D_h(t)n_h.
]

Let (U_h(t,	au)) be the scalar evolution operator

[
U_h(t,	au)=
expleft[-int_	au^tD_h(s),dsight].
]

With initial population (n_{h,0}),

[
n_h(t)
=
U_h(t,t_0)n_{h,0}
+
int_{t_0}^tU_h(t,	au)S_h(	au),d	au.
]

Define

[
n_h^{m hom}(t)=U_h(t,t_0)n_{h,0}
]

and the source-driven part

[
n_h^{m src}=n_h-n_h^{m hom}.
]

If the source is rescaled by a constant (c), with the same prescribed background and same initial population, then exactly

[
n_h^{(c)}
=
n_h^{m hom}+c,n_h^{m src}.
]

For the charge-pair repair, (c=1/2) for
(pi^-,pi^+,K^-,ar p,ar n), while (K_L^0) has (c=1).

Therefore

[
n_h^{m repaired}
=
rac12 n_h^{m current}
+
rac12 n_h^{m hom}
]

for each affected species in the intended floor-inactive common-background equation.

If (n_{h,0}=0), this reduces to the familiar exact half-response

[
n_h^{m repaired}=rac12n_h^{m current}.
]

## 7. Important executor-floor narrowing

The actual public Wu–Xu code initializes every hadron population with a tiny positive seed,

[
n_{h,0}=10^{-60}n_gamma(T_f),
]

and represents the population in log form with a floor at (y=-100).

For the raw executor, if (n=e^y), (epsilon=e^{-100}), and

[
ar n=max(n,epsilon),
]

the implemented equation is

[
dot n=
alpha(n)S-Dn,
qquad
alpha(n)=min(1,n/epsilon).
]

Thus the raw floor-active executor is not globally linear in the source amplitude.

Consequently:

[
	ext{SOURCE HALF-SPLIT}

eq
	ext{RAW EXECUTOR POPULATION HALF-SPLIT AUTOMATICALLY}.
]

The exact linear response in Sections 6–10 applies when the intended source-sink equation is used, or on intervals where the relevant executor populations are floor inactive.

Floor-active intervals require the previously derived exact residual

[
ho_h^{m floor}
=
S_h[alpha_h-1].
]

## 8. Directional-rate decomposition

At common supplied background, define the exact reduced directional rates

[
A=Lambda_{p	o n},
qquad
B=Lambda_{n	o p}.
]

Decompose them as

[
A=A_0+A_{m aff},
qquad
B=B_0+B_{m aff},
]

where the base (0) contains the unaffected (K_L^0) contribution plus, if nonzero initial seeds are retained, the homogeneous affected-species contribution.

Equivalently, define

[
A_0=A_{K_L^0}+A_{m aff}^{m hom},
]
[
B_0=B_{K_L^0}+B_{m aff}^{m hom}.
]

Then in the floor-inactive common-background model, the charge-pair repair gives exactly

[
A_{m new}
=
A_0+rac12(A_{m old}-A_0)
=
rac12(A_{m old}+A_0),
]

[
B_{m new}
=
B_0+rac12(B_{m old}-B_0)
=
rac12(B_{m old}+B_0).
]

Hence

[
Delta A
=
A_{m new}-A_{m old}
=
-rac12(A_{m old}-A_0),
]

[
Delta B
=
-rac12(B_{m old}-B_0).
]

This is stronger than a generic error bound: it is the exact common-background response of the intended linear population block to the source-map repair.

## 9. Exact forcing relation

The reduced hadronic neutron forcing is

[
F_{m had}(X,t)=(1-X)A-XB.
]

Define the base forcing

[
F_0=(1-X)A_0-XB_0.
]

Then exactly

[
F_{m new}
=
F_0+rac12(F_{m old}-F_0)
=
rac12(F_{m old}+F_0),
]

so

[
Delta F
=
F_{m new}-F_{m old}
=
-rac12(F_{m old}-F_0).
]

If the affected homogeneous seeds are negligible/zero, (F_0) is simply the (K_L^0) forcing at that common background.

Therefore the correct exact statement is:

> the charge-pair repair halves the **source-driven affected contribution** to the common-background hadronic forcing; it does not generically halve the total hadronic forcing because (K_L^0) is unchanged.

## 10. Exact (R,q) chart transformation

Where

[
R=A+B>0,
qquad
q=A/R,
]

define

[
R_0=A_0+B_0.
]

From Section 8,

[
R_{m new}
=
rac12(R_{m old}+R_0).
]

Also

[
q_{m new}
=
rac{A_{m old}+A_0}{R_{m old}+R_0}.
]

If (R_0>0), write (q_0=A_0/R_0). Then

[
q_{m new}-q_{m old}
=
rac{R_0}{R_{m old}+R_0}
(q_0-q_{m old}).
]

Thus the repaired (q) moves toward the base-channel directional ratio (q_0); it is not generally invariant.

Special case: if (R_0=0), then

[
R_{m new}=R_{m old}/2,
qquad
q_{m new}=q_{m old},
qquad
F_{m new}=F_{m old}/2.
]

This special case must not be promoted to the general Front-B claim because (K_L^0) is present.

## 11. Relation to the Rec9 (Qmapsto BQ) repair

Rec9's controlling Front-B repair is:

[
R=BQ
]

with aggregate source vector

[
Q=(Q_{pi^pm},Q_{K^pm},Q_{K_L^0},Q_{p+ar p},Q_{n+ar n}).
]

This return supplies the source-native matrix (B_{m sym}) under the explicit Wu–Xu charge-conjugation symmetry.

Therefore:

[
	ext{DONOR SOURCE COLUMN}

eq
	ext{REACTION-SPECIES INDEX},
]

but the mapping is not arbitrary once the source symmetry is fixed.

## 12. Consequence for source uncertainty

A single aggregate column must not be assigned independent uncertainties to its two downstream charge branches.

For example, (Q_{pi^pm}) is one source object feeding two reaction populations through one constrained map.

Hence:

[
	ext{ONE SOURCE COLUMN}	o	ext{MULTIPLE REACTION POPULATIONS}
]

does not imply independent source errors.

Any donor covariance/uncertainty object must be pushed through the same (B) map before target propagation.

## 13. Consequence for E2c high-energy splice

A high-energy donor returning only

[
{pi^pm,K^pm,K_L^0,p+ar p,n+ar n}
]

may be matched at the aggregate (Q) interface, but it still requires an explicit reaction map (B).

A richer charge-separated donor may instead replace both (Q) and (B), but then it is not a drop-in replacement unless its species definitions, normalization, primary convolution, support and transient-state semantics are validated together.

Thus:

[
	ext{RICHER DONOR}

eq
	ext{DROP-IN SOURCE REPLACEMENT}.
]

## 14. Cheapest decisive numerical comparator

Before any terminal lower-mass E2 extension, compare inside the already supported BlackHawk source-table domain.

Suggested PBH masses:

[
10^9,{m g},qquad
2	imes10^9,{m g},qquad
6	imes10^9,{m g}.
]

Comparator A:
current aggregate-to-single-species source map.

Comparator B:
charge-pair-symmetric map (B_{m sym}).

Record:

1. floor-active/source-active intervals for every hadron population;
2. (pi^-,pi^+,K^-,K_L^0,ar p,ar n) populations;
3. common-state (A(t),B(t));
4. (R(t),q(t));
5. (F_{m had}(t));
6. dynamic (X_n(t));
7. the code's reduced (Y_p) proxy.

Only after this source-map comparator is understood should the correction be propagated into a full modern (Y_p)/D/H endpoint.

## 15. Claim ceiling and firewalls

Exact / source-supported:

- BlackHawk BBN `pipm`, `Kpm`, `proton`, `neutron` are charge-conjugate aggregate source columns.
- formatter division by 2 is initial-particle normalization, not final-charge splitting.
- current Wu–Xu source map sends aggregate columns into single reaction populations.
- (B_{m sym}) follows from the declared charge-conjugation-symmetric source convention.
- Sections 6–10 are exact for the intended floor-inactive common-background linear population equations.

Not run / not established:

- floor materiality for the repaired source map,
- full coupled (A/B) response,
- full coupled (X_n) response,
- modern (Y_p/D/H) response,
- PBH abundance-bound response,
- source-valid low-mass E2b.

Firewalls:

[
	ext{PAIR-AGGREGATED SOURCE}

eq
	ext{SINGLE-CHARGE SOURCE}
]

[
	ext{INITIAL-PAIR NORMALIZATION}

eq
	ext{FINAL-CHARGE SPLIT}
]

[
	ext{SOURCE HALF-SPLIT}

eq
	ext{TARGET HALF-SPLIT}
]

[
	ext{COMMON-BACKGROUND EXACT RESPONSE}

eq
	ext{FULL COUPLED TRAJECTORY RESPONSE}
]

[
	ext{FLOOR-INACTIVE LINEARITY}

eq
	ext{RAW FLOOR-ACTIVE EXECUTOR LINEARITY}
]

[
	ext{AGGREGATE SOURCE AGREEMENT}

eq
	ext{CHARGE-RESOLVED SOURCE AGREEMENT}
]

## 16. Source basis

Public Wu–Xu repository:

https://github.com/Fenyutanchan/Primordial-Black-Hole

Inspected v2 commit:

`d395183674cace6c9906a8911bdeb7234ba4040d`

Relevant Wu–Xu paths:

- `arXiv-2509.05618/main-scan.jl`
- `arXiv-2509.05618/valid_hadrons_from_BlackHawk.ipynb`
- `arXiv-2509.05618/tool_script-hadrons_from_PBH.jl`

BlackHawk v2-family public source paths independently inspected:

- `scripts/pythia_scripts/table_up.cc`
- `scripts/pythia_scripts/table_gluon.cc`
- `scripts/pythia_scripts/formatting.c`
- `src/secondary.c`

Publication:

Quan-feng Wu and Xun-Jie Xu, *Primordial black holes evaporating before Big Bang nucleosynthesis*, JCAP 02 (2026) 063, arXiv:2509.05618.

Project-level controlling repairs used only for placement:

- REC9-XH-S3-HIGH-ENERGY-TRANSIENT-HADRON-DONOR-MATRIX-REFEREE-001
- REC9-INT7-THREAD095-SPECIES-VECTOR-TARGET-BUDGET-REFEREE-001
- MECH-S6-FRONTB-WU-XU-LOG-POPULATION-FLOOR-SOURCE-INJECTION-RESIDUAL-GATE-001

## 17. Status

`CHARGE_PAIR_AGGREGATE_SEMANTICS = PASS_EXACT`

`CURRENT_AGGREGATE_TO_SINGLE_SPECIES_MAP = HIGH_OBJECT_MAP_MISMATCH`

`B_SYM_SOURCE_MAP = PASS_EXACT_UNDER_DECLARED_SOURCE_SYMMETRY`

`COMMON_BACKGROUND_SOURCE_DRIVEN_HALF_RESPONSE = PASS_EXACT_FLOOR_INACTIVE`

`COMMON_BACKGROUND_A_B_F_TRANSFORM = PASS_EXACT_FLOOR_INACTIVE`

`RQ_CHART_TRANSFORM = PASS_EXACT_WHERE_R_POSITIVE`

`RAW_FLOOR_ACTIVE_HALF_RESPONSE = NOT_CLAIMED`

`SOURCE_CORRECTED_SUPPORTED_DOMAIN_RERUN = NOT_RUN`

`FULL_COUPLED_TARGET_IMPACT = NOT_RUN`

`SOURCE_VALID_E2B = OPEN`

`SOURCE_MATCHED_K_PBH = UNDEFINED`

`NO PBH BOUND / NO ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY CLAIM`


## 18. Exact supported-domain source-table audit

The public Wu–Xu executor evaluates the hadron source table with log-linear interpolation in both PBH mass and source rate:

[
log q_h(M)
]

is linearly interpolated as a function of

[
log M.
]

Using that exact interpolation contract, the aggregate source rates and the charge-symmetric single-species rates are:

| (M_{m PBH}) [g] | source column | current downstream single-species source | charge-symmetric repaired single-species source |
|---:|---|---:|---:|
| (1.0	imes10^9) | (Q_{pi^pm}) | (4.891055	imes10^5) into each of (pi^-), (pi^+) | (2.445528	imes10^5) into each |
| (1.0	imes10^9) | (Q_{K^pm}) | (5.910594	imes10^4) into (K^-) | (2.955297	imes10^4) |
| (1.0	imes10^9) | (Q_{p+ar p}) | (3.484908	imes10^4) into (ar p) | (1.742454	imes10^4) |
| (1.0	imes10^9) | (Q_{n+ar n}) | (3.465618	imes10^4) into (ar n) | (1.732809	imes10^4) |
| (2.0	imes10^9) | (Q_{pi^pm}) | (2.024939	imes10^5) into each of (pi^-), (pi^+) | (1.012470	imes10^5) into each |
| (2.0	imes10^9) | (Q_{K^pm}) | (2.455090	imes10^4) into (K^-) | (1.227545	imes10^4) |
| (2.0	imes10^9) | (Q_{p+ar p}) | (1.438015	imes10^4) into (ar p) | (7.190076	imes10^3) |
| (2.0	imes10^9) | (Q_{n+ar n}) | (1.429513	imes10^4) into (ar n) | (7.147567	imes10^3) |
| (6.0	imes10^9) | (Q_{pi^pm}) | (4.822826	imes10^4) into each of (pi^-), (pi^+) | (2.411413	imes10^4) into each |
| (6.0	imes10^9) | (Q_{K^pm}) | (5.889788	imes10^3) into (K^-) | (2.944894	imes10^3) |
| (6.0	imes10^9) | (Q_{p+ar p}) | (3.400408	imes10^3) into (ar p) | (1.700204	imes10^3) |
| (6.0	imes10^9) | (Q_{n+ar n}) | (3.376389	imes10^3) into (ar n) | (1.688194	imes10^3) |

The (K_L^0) aggregate is unchanged:

- (2.908677	imes10^4) at (10^9) g,
- (1.207953	imes10^4) at (2	imes10^9) g,
- (2.896186	imes10^3) at (6	imes10^9) g.

These are source-interface numbers only.

They do **not** imply a factor-two change in (A), (B), (F_{m had}), (X_n), (Y_p), D/H, or any PBH abundance bound.

The table establishes only that the source correction is numerically material at the injection interface and is not a machine-precision or tiny-tail effect.
