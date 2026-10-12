---
artifact_id: XH-S3-FRONTB-WU-XU-TERMINAL-HADRON-SOURCE-EXTRAPOLATION-HARVEST-022
bw_ingestion_event_id: ING-20261012-0003
bw_qualification_state: FRONTB_TERMINAL_SOURCE_VALIDITY
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: EXTERNAL_EVIDENCE_NO_AUTHORITY
archive_mode: PUBLIC_ARTIFACT
sync_state: GITHUB_PENDING_BW_LINK_UPDATE
source_surface: GOOGLE_DRIVE
source_revision: AHj4eMRs7ERShiiW_uIgfG5S2rQY6qEANLrLz9LiaM5s8H6Py8SOr5vBn1NhirFGj6VNgEDaCpKYoVDp7XZWfiDCbhGrXnA97-h0B566BsA
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# XH-S3-FRONTB-WU-XU-TERMINAL-HADRON-SOURCE-EXTRAPOLATION-HARVEST-022

> Public-safe mirror of the BW-linked Drive source. BW controls lifecycle/currentness; this GitHub body does not upgrade scientific authority. Private provider locators were redacted during mirroring.

XH-S3 / FRONT B — WU–XU TERMINAL HADRON SOURCE EXTRAPOLATION HARVEST 022
RETURN_ID
XH-S3-FRONTB-WU-XU-TERMINAL-HADRON-SOURCE-EXTRAPOLATION-HARVEST-022
RESULT
THE PUBLIC WU–XU EXECUTOR DEFINES TERMINAL PBH HADRON SOURCES BY LOG–LOG LINEAR EXTRAPOLATION BELOW THE LOWEST TABULATED MASS.
THE SOURCE TABLE BEGINS AT 1e9 g, WHILE THE PUBLIC SCAN STARTS AS LOW AS 6e8 g AND EVOLVES TO O(1–20 g) BEFORE SOURCE SHUTOFF.
THEREFORE THE TERMINAL HADRON SOURCE IS EXECUTOR-DEFINED BUT NOT SOURCE-VALIDATED BY THE LOCATED PUBLIC TABLE OVER ~7.7–8.9 DECADES OF MASS.
THIS SOURCE-CLOSURE GAP IS CURRENTLY MORE FUNDAMENTAL THAN THE REMAINING LOG-FLOOR REENTRY QUESTION.
NO PBH ENDPOINT / NO BOUND RELEASE.
FIREWALL
EXECUTOR DEFINITION != PHYSICAL SOURCE VALIDATION.
LOG–LOG EXTRAPOLATION != ASYMPTOTIC THEOREM.
LOCAL POWER-LAW SLOPE != VALIDATED 8–9-DECADE SCALING.
BLACKHAWK RUNNABILITY != HIGH-ENERGY BBN HADRONIZATION VALIDITY.
HIGH-ENERGY STABLE-PARTICLE SPECTRA != METASTABLE π/K/ANTI-N BBN SOURCE.
REMAINING REST-MASS FRACTION != TARGET-WEIGHTED BBN IMPORTANCE.
NO CANON / NO EXEC_SIGN / NO NOVELTY / NO PBH BOUND.
1. PRIMARY PUBLIC SOURCE OBJECTS
[Wu–Xu public GitHub]
[Wu–Xu source table]
[NaturalUnits.jl]
Inspected source tree:
Fenyutanchan/Primordial-Black-Hole
current public commit family d395183674cace6c9906a8911bdeb7234ba4040d.
Relevant files:
arXiv-2509.05618/data/out/hadrons_from_PBH.dat
arXiv-2509.05618/tool_script-hadrons_from_PBH.jl
arXiv-2509.05618/main-scan.jl
arXiv-2509.05618/main-scan-parameters.jl
arXiv-2509.05618/tool_script-BlackHawk_extension.jl.
2. PUBLIC HADRON SOURCE TABLE RANGE
The public hadron-source table contains 100 mass points.
Lowest tabulated PBH mass:
M_table,min = 5.609588603804452e32 GeV
≈ 1.000e9 g.
Highest tabulated PBH mass:
M_table,max = 2.243835441521781e36 GeV
≈ 4.000e12 g.
At the low-mass edge the tabulated instantaneous production rates are approximately:
charged pions:
4.8911e5 GeV
charged kaons:
5.9106e4 GeV
K0L:
2.9087e4 GeV
protons:
3.4849e4 GeV
neutrons:
3.4656e4 GeV.
3. EXACT INTERPOLATION / EXTRAPOLATION CONTRACT
tool_script-hadrons_from_PBH.jl constructs for every species:
LinearInterpolation(
    log(rate),
    log(mass);
    extrapolation = ExtrapolationType.Linear
).
Then:
dN_h/dt(M)
=
exp[
interpolation(log M)
].
Therefore outside the table range the public executor continues the terminal edge linearly in log(rate) versus log(M).
Below 1e9 g this is exactly a fixed power-law continuation using the slope of the first table interval.
This is a precise executor contract.
It is not, by itself, a physical asymptotic justification.
4. LOW-EDGE SLOPES
Using the first two table entries, the implied low-edge powers
dN_h/dt ∝ M^alpha_h
are:
pi:
alpha ≈ -1.20049
K±:
alpha ≈ -1.19665
K0L:
alpha ≈ -1.19680
proton:
alpha ≈ -1.20429
neutron:
alpha ≈ -1.20476.
However the local slopes are not already constant inside the nearby tabulated region.
Across the first 12 intervals they vary approximately:
pi:
-1.20 to -1.30
(mean about -1.28)
K±:
-1.20 to -1.30
(mean about -1.28)
K0L:
-1.20 to -1.30
proton:
-1.20 to -1.31
neutron:
-1.20 to -1.31.
Thus:
EDGE POWER LAW LOOKS SMOOTH
but
EDGE POWER LAW IS NOT AN EXACT TABULATED ASYMPTOTE.
5. PUBLIC SCAN ENTERS THE EXTRAPOLATED REGION
main-scan-parameters.jl uses:
M0,min = 6e8 g
M0,max = 1e10 g.
Therefore:
- the lowest initial masses already begin below the 1e9 g source-table edge;
- every trajectory eventually evolves below 1e9 g before evaporation cutoff.
So source extrapolation is not a hypothetical corner case.
It is active in the declared public scan.
6. SOURCE SHUTOFF MASS
magic(...) uses by default:
log_m_PBH_evaporated_ratio = 20,
and defines:
log M_stop
=
max(log M0 - 20, log m_Pl).
For the published mass range M0 e^-20 remains above the Planck mass, so:
M0 = 6e8 g
=> M_stop ≈ 1.2367 g.
M0 = 1e9 g
=> M_stop ≈ 2.0612 g.
M0 = 1e10 g
=> M_stop ≈ 20.6115 g.
Hence the source interpolation can be evaluated approximately:
8.91 decades below its table edge for 6e8 g initial PBHs;
8.69 decades below for 1e9 g;
7.69 decades below for 1e10 g.
7. WHAT THE PUBLIC EDGE EXTRAPOLATION THEN DOES
If one mechanically extends the FIRST-INTERVAL source slope to M_stop, the source-rate factors relative to the 1e9 g table edge grow by roughly:
for M0=6e8 g / M_stop≈1.24 g:
pi ~4.9e10
K± ~4.6e10
K0L ~4.6e10
p ~5.3e10
n ~5.4e10.
for M0=1e10 g / M_stop≈20.6 g:
pi ~1.69e9
K± ~1.58e9
K0L ~1.58e9
p ~1.80e9
n ~1.82e9.
These numbers describe the EXECUTOR'S extrapolated functional continuation.
They do NOT certify the physical source rates at gram-scale PBH masses.
8. HAWKING-TEMPERATURE MAPPING
Using the same public NaturalUnits convention:
M_Pl ≈ 2.435e18 GeV,
1 g ≈ 5.6096e23 GeV,
and Wu–Xu:
T_BH = M_Pl^2 / M_BH,
the source-table lower edge M=1e9 g corresponds to:
T_BH ≈ 1.06e4 GeV.
The mass at which:
T_BH = 1e5 GeV
is approximately:
M ≈ 1.06e8 g.
The public source is therefore extrapolated far into an increasingly high-temperature Hawking regime.
At M_stop the formal Hawking temperatures are approximately:
M_stop≈1.24 g
=> T_BH≈8.5e12 GeV;
M_stop≈2.06 g
=> T_BH≈5.1e12 GeV;
M_stop≈20.6 g
=> T_BH≈5.1e11 GeV.
9. HADRONIZATION ENERGY CONTRACT LOCATED IN THE PUBLIC PROJECT
The BlackHawk wrapper defaults to:
Emin = 5 GeV,
Emax = 1e5 GeV,
for primary particle energies.
The archived project PYTHIA8 table scripts use:
quark/u-like table:
E_initial = 5 GeV to 1e5 GeV;
gluon table:
E_initial = 1e3 GeV to 1e5 GeV,
with an explicit code comment:
above 1e5 GeV, Pythia8 works too slowly.
This establishes that the project’s archived/custom PYTHIA table-generation workflow was bounded at 1e5 GeV.
CLAIM CEILING:
This does NOT prove that every internal BlackHawk BBN hadronization table has an identical hard 1e5-GeV support boundary.
It does show that the located source-generation workflow does not itself validate metastable-hadron yields out to the 1e11–1e13 GeV characteristic temperatures reached before the executor source cutoff.
10. REMAINING-MASS PROXY
The Hawking-temperature threshold T_BH=1e5 GeV corresponds to M≈1.06e8 g.
As a crude geometric proxy, the remaining rest-mass fraction below that mass is:
Mcrit/M0.
Thus:
M0=6e8 g:
~17.6% of initial mass remains after crossing Mcrit;
M0=1e9 g:
~10.6%;
M0=1e10 g:
~1.06%.
This is NOT a BBN target fraction.
Emission power accelerates, channel multiplicities evolve, and target timing matters.
Therefore:
REST-MASS FRACTION
!=
Yp / D-H IMPACT.
The calculation only shows that for the low-mass end the high-temperature extrapolated regime is not parametrically infinitesimal in remaining mass.
11. BLACKHAWK WRAPPER DOES NOT ITSELF FORCE M>=1e9 g
The default BlackHawkParameters object initializes:
Mmin = 1e9 g,
Mmax = 1e16 g.
But set_BlackHawk_mass!(...) accepts any positive mass and overwrites Mmin/Mmax.
The explicit assertion requiring mass > m_Pl is commented out.
Therefore a lower-mass BlackHawk run is software-addressable.
This is useful because the first validation step can regenerate direct source points below 1e9 g instead of trusting the outer interpolation.
However:
LOWER-MASS BLACKHAWK RUNNABLE
!=
HIGH-ENERGY HADRONIZATION VALIDATED.
The hadronization-energy contract remains separate.
12. CURRENT 2026 EXTERNAL OPTIONS
[BlackHawk v3.0 2026]
[HDMSpectra]
A newer BlackHawk v3.0 exists in 2026 and is relevant as a currentness check for PBH spectral infrastructure.
No source inspected in this rotation establishes that v3.0 supplies a source-matched early-BBN metastable π/K/antinucleon solution that closes the Wu–Xu terminal-source problem.
HDMSpectra is a high-energy prompt-spectrum framework and is relevant as a possible high-energy donor.
But:
HIGH-ENERGY PROMPT/STABLE SPECTRA
!=
EARLY-BBN METASTABLE π/K/ANTI-N SOURCE
without an explicit mapping preserving the transient species and their interaction semantics.
Therefore neither is promoted here as a closed replacement.
13. WHY THIS OUTRANKS THE LOG-FLOOR RESIDUAL
021 showed:
- initialization is ~14–16 orders of magnitude above the population floor;
- source-off floor residual is exactly zero;
- only source-active later re-entry remained open.
022 now shows that the source function S_h(t) itself enters a many-decade extrapolation before shutoff.
Since both:
- DE population n_h*=S_h/D_h,
- and the exact floor residual rho_floor=S_h(alpha_h-1)
depend directly on S_h,
source closure logically precedes a fine-grained floor-materiality claim in the terminal regime.
Thus current order is:
SOURCE-RATE VALIDITY
before
FLOOR-REENTRY MATERIALITY
before
DE-vs-FULL TARGET VALIDATION.
14. SMALLEST SOURCE-CLOSURE TEST
No broad PBH scan is needed initially.
STEP A — NEAR-EDGE DIRECT REGENERATION
Using the same BlackHawk/PYTHIA BBN contract, generate direct dN_h/dt source points at a small descending set such as:
6e8 g,
3e8 g,
~1e8 g,
where possible.
Compare direct points against the existing 1e9-g edge extrapolation for each species.
This tests the first ~0.2–1 decade, where source validation is cheapest and immediately relevant to the low-mass scan.
STEP B — HIGH-ENERGY CONTRACT
Below roughly 1.06e8 g, T_BH exceeds 1e5 GeV.
A source-valid continuation then requires an explicit high-energy hadronization contract for the metastable BBN species:
π±,
K±,
K0L,
proton/antiproton,
neutron/antineutron,
or a source-native theorem/asymptotic model with an error certificate.
STEP C — ERROR PROPAGATION
Only after comparing source models should the difference be propagated through:
S_h
-> hadron populations
-> directional rates A,B
-> X_n
-> Yp / D-H,
using the already available M12/Mech source-to-target control stack.
This is a validation design, not execution authorization.
15. POSSIBLE CHEAP MODEL FAMILY FOR AUDIT
For the extrapolated source region, keep at least three distinct source models for stress-testing:
E0:
current edge-power extrapolation.
E1:
local-slope continuation using several adjacent table intervals / uncertainty envelope.
E2:
direct regenerated lower-mass/high-energy hadronization points or a validated high-energy donor.
If E0/E1/E2 produce target-equivalent A,B histories to declared tolerance, the terminal source gap can be demoted.
If not, it is load-bearing.
No numerical outcome is claimed here.
16. RELATION TO DE / WATERFALL RESULTS
019–020 remain valid as mathematical statements about the DECLARED source functions.
In particular:
- exact two-direction X_n projection remains exact;
- DE root monotonicity/uniqueness remains exact for nonnegative S_h;
- B2 nonnegative source aggregation preserves instantaneous uniqueness structurally.
022 does NOT invalidate those theorems.
It changes the physical claim ceiling:
THEOREM GIVEN S_h
can be exact,
while
SOURCE-MATCHED S_h
can remain externally unvalidated in the terminal regime.
17. B2 CONSEQUENCE
For B2:
Q_h(t)
=
a^-3 ∫ chi R_h^emit(M(t;Mi,tf)) dmu_B2.
If R_h^emit(M) relies on the same unvalidated terminal extrapolation, population integration does not cure it.
Therefore:
LINEAR POPULATION AGGREGATION
!=
SOURCE UNCERTAINTY REMOVAL.
A source-valid B2 adapter requires the elementary trajectory source to be typed over the mass/temperature support actually contributing to Q_h.
18. MODEL-USE DISCIPLINE
No external AI model invoked.
The decisive result came from:
- exact source-table boundaries;
- exact interpolation contract;
- exact source cutoff mass;
- direct code/currentness inspection.
An additional model would add opinion but not source validation.
A future independent model audit becomes useful only after competing terminal source models E0/E1/E2 exist and one wants adversarial comparison of their physical assumptions.
19. STATUS
WU_XU_HADRON_SOURCE_TABLE_RANGE
= 1e9–4e12 g / PASS EXACT.
WU_XU_SOURCE_EXTRAPOLATION_BELOW_1e9g
= LOG–LOG LINEAR / PASS EXACT EXECUTOR SEMANTICS.
PUBLIC_SCAN_OVERLAPS_EXTRAPOLATION
= YES / PASS EXACT.
TERMINAL_EXTRAPOLATION_DEPTH
= ~7.7–8.9 DECADES IN MASS / PASS EXACT.
LOW_EDGE_POWER
= APPROX -1.20 SPECIES-DEPENDENT;
NOT CONSTANT ACROSS NEARBY TABLE INTERVALS.
TERMINAL_SOURCE_PHYSICAL_VALIDATION
= NOT ESTABLISHED BY LOCATED PUBLIC SOURCE ARTIFACTS.
LOWER_MASS_BLACKHAWK_EXECUTION
= SOFTWARE-ADDRESSABLE.
HIGH_ENERGY_METASTABLE_BBN_HADRONIZATION
= OPEN.
BLACKHAWK_V3_AS_DIRECT_BBN_SOURCE_FIX
= NOT ESTABLISHED.
HDMSPECTRA_AS_METASTABLE_BBN_SOURCE
= NOT ESTABLISHED.
LOG_FLOOR_REENTRY
= OPEN BUT SECONDARY TO SOURCE CLOSURE.
PBH_DE_DYNAMIC_ACCURACY
= OPEN.
PBH_Yp_DH_TARGET_VALIDATION
= OPEN.
SOURCE_MATCHED_K_PBH
= UNDEFINED.
NO PBH BOUND / NO ENDPOINT RELEASE.
NO CANON / NO EXEC_SIGN / NO NOVELTY / SCIENCE_FIRST.
SOURCES
[Wu–Xu public GitHub]
[Wu–Xu source table]
[NaturalUnits.jl]
[BlackHawk v3.0 2026]
[HDMSpectra]
