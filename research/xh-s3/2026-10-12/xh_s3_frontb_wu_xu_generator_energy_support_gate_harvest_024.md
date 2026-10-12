---
artifact_id: XH-S3-FRONTB-WU-XU-GENERATOR-ENERGY-SUPPORT-GATE-HARVEST-024
bw_ingestion_event_id: ING-20261012-0026
bw_qualification_state: EXTERNAL_SOURCE_HARVEST
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: EXTERNAL_EVIDENCE
archive_mode: PUBLIC_ARTIFACT
sync_state: SYNCED
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# XH-S3-FRONTB-WU-XU-GENERATOR-ENERGY-SUPPORT-GATE-HARVEST-024

> Public-safe mirror of the BW-linked Drive source. BW controls lifecycle/currentness; this GitHub body does not upgrade scientific authority. Private provider locators were redacted during mirroring.

XH-S3 / FRONT B — WU–XU GENERATOR ENERGY-SUPPORT GATE HARVEST 024
RETURN_ID
XH-S3-FRONTB-WU-XU-GENERATOR-ENERGY-SUPPORT-GATE-HARVEST-024
RESULT
THE PUBLIC v2 HADRON-SOURCE GENERATOR HAS NOW BEEN RECOVERED EXACTLY.
THE 1e9 g LOWER SOURCE-TABLE EDGE IS AN EXPLICIT NOTEBOOK CHOICE, NOT A HARD MASS LIMIT IN set_BlackHawk_mass!.
BUT THE SAME GENERATOR FIXES THE PRIMARY ENERGY GRID TO 5–1e5 GeV.
THEREFORE LOWER-MASS SOURCE REGENERATION HAS A SECOND, INDEPENDENT ENERGY-SUPPORT GATE:
MASS SUPPORT AND HADRONIZATION-ENERGY SUPPORT MUST BOTH BE LEGAL.
A NAIVE RERUN AT 3e8–1e8 g WITH THE SAME Emax=1e5 GeV IS NOT A SOURCE-VALIDATED E2 TEST.
NO PBH ENDPOINT / NO BOUND RELEASE.
FIREWALL
LOWER-MASS BLACKHAWK RUNNABILITY != COMPLETE LOWER-MASS HAWKING SOURCE.
PRIMARY ENERGY-COVERAGE PROXY != SPECIES-SPECIFIC HADRON-YIELD ERROR BAR.
GEOMETRIC-OPTICS THERMAL TAIL != EXACT BLACKHAWK GREYBODY TAIL.
Emax/TBH COVERAGE != HIGH-ENERGY HADRONIZATION VALIDITY.
NOTEBOOK PARAMETER CHOICE != DOCUMENTED AUTHOR INTENT.
NO CANON / NO EXEC_SIGN / NO NOVELTY.
1. RECOVERED PUBLIC GENERATOR
PRIMARY PUBLIC ARTIFACTS
[Wu–Xu v2 commit]
[valid_hadrons_from_BlackHawk.ipynb]
[Wu–Xu public GitHub]
The v2 commit:
d395183674cace6c9906a8911bdeb7234ba4040d
adds:
arXiv-2509.05618/valid_hadrons_from_BlackHawk.ipynb
Blob SHA:
8a10396ae771b17059808fc2b91235dd194cba8d.
This notebook is the actual generator for:
data/out/hadrons_from_PBH.dat.
2. EXACT MASS GRID
Generator cell 12 sets:
m_PBH_list = geomspace(1e9, 4e12, 100) * g.
Therefore:
Mmin_source = 1e9 g
Mmax_source = 4e12 g
N_mass = 100.
No source-native justification for the 1e9-g lower endpoint is written in the surrounding notebook markdown.
The notebook headings are only:
Benchmark
and
Spectra.
Thus:
1e9 g LOWER EDGE
= EXPLICIT GENERATOR PARAMETER CHOICE.
It is not presented in the notebook as a theorem or hard BlackHawk mass-domain boundary.
3. EXACT ENERGY GRID
For the benchmark and for EVERY mass in the generator loop, the notebook applies:
set_BlackHawk_energy_spectrum!(
    params,
    GeV(5),
    GeV(1e5),
    100
).
So:
Emin_primary = 5 GeV
Emax_primary = 1e5 GeV
N_E = 100.
The notebook then runs:
run_BlackHawk_inst(params)
and reads:
instantaneous primary spectra
and
instantaneous secondary spectra.
4. HOW dN_h/dt IS BUILT
For each mass, the notebook integrates the returned secondary spectra in logarithmic energy.
For charged pions, schematically:
integrand(E)
=
E * d2N_pi/(dt dE).
With nearly uniform log-energy spacing h, the notebook computes a trapezoidal integral:
dN_pi/dt
≈
(h/2)
[
2 sum(E d2N_pi/dtdE)
-
endpoint terms
].
The same construction is used for:
K±,
K0L,
protons,
neutrons.
Then cell 13 writes the resulting five integrated source rates to:
hadrons_from_PBH.dat.
Therefore the source table is not an independent analytic fit.
It is a postprocessed set of BlackHawk instantaneous-secondary calculations under the declared finite primary-energy support.
5. MASS LOWER EDGE IS NOT A HARD WRAPPER LIMIT
The public wrapper:
set_BlackHawk_mass!(params,mass)
accepts a positive mass and overwrites:
Mmin,
Mmax.
The previous explicit assertion:
mass > m_Pl
is commented out.
Thus:
the software interface itself does not force M>=1e9 g.
This repairs an ambiguity left in 022:
TABLE MINIMUM
!=
WRAPPER MASS MINIMUM.
6. SECOND SUPPORT GATE: Emax/TBH
Using the public convention:
T_BH = M_Pl^2 / M,
with M_Pl≈2.435e18 GeV and
1 g≈5.6096e23 GeV,
the dimensionless upper spectral support is:
x_max(M)
=
Emax/T_BH.
For Emax=1e5 GeV:
M=1e9 g:
T_BH≈1.057e4 GeV,
x_max≈9.46.
M=6e8 g:
T_BH≈1.762e4 GeV,
x_max≈5.68.
M=3e8 g:
T_BH≈3.523e4 GeV,
x_max≈2.84.
M=1e8 g:
T_BH≈1.057e5 GeV,
x_max≈0.946.
Thus lowering PBH mass at fixed Emax progressively cuts deeper into the dimensionless Hawking spectrum.
7. GEOMETRIC-OPTICS THERMAL TAIL PROXY
This section is a DIAGNOSTIC PROXY only.
At high dimensionless energy x, a massless Schwarzschild Hawking number spectrum has geometric-optics structure approximately proportional to:
x^2/(exp(x) ± 1).
Using the fermionic + sign as a quark-like proxy, the fraction of this high-energy number spectrum above x_max is approximately:
x_max=9.46:
~0.48%.
x_max=5.68:
~8.6%.
x_max=2.84:
~50%.
x_max=0.946:
~94.8%.
For the corresponding energy-weighted x^3/(exp(x)+1) proxy:
x_max=9.46:
~1.6%.
x_max=5.68:
~19%.
x_max=2.84:
~71%.
x_max=0.946:
~98.9%.
Bosonic high-energy proxies are similar in ordering and somewhat smaller in number-tail fraction.
CLAIM CEILING:
These are NOT exact BlackHawk missing-flux fractions.
Greybody factors, species thresholds, finite masses, quark/gluon mixture and the exact low-x behavior are not represented by this simple proxy.
Their use is only to establish SUPPORT MATERIALITY.
8. WHY 1e9 g IS A NATURAL COVERAGE EDGE
In the same fermionic geometric-optics number proxy:
<1% high-energy number tail requires approximately:
x_max >= 8.54.
With Emax=1e5 GeV this corresponds to:
M >= ~9.0e8 g.
For <1% energy-weighted tail:
x_max >= ~10.12,
corresponding to:
M >= ~1.07e9 g.
Therefore the generator’s explicit lower edge at 1e9 g lies almost exactly at a natural ~percent-level coverage scale for the chosen Emax.
This is a PROJECT INFERENCE.
The notebook does not say:
“we chose 1e9 g because Emax/TBH~10”.
Do not convert this numerical alignment into a claim of author intent.
9. IMPORTANT CONSEQUENCE FOR PROPOSED E2 POINTS
022/023 proposed direct source regeneration near:
6e8 g,
3e8 g,
~1e8 g.
024 repairs that plan.
With unchanged Emax=1e5 GeV:
6e8 g
has a non-negligible high-energy primary tail.
3e8 g
has order-half of the simple quark-number proxy above Emax.
1e8 g
has most of the relevant high-T proxy above Emax.
Therefore:
DIRECT LOWER-MASS RUN
with unchanged energy support
!=
COMPLETE DIRECT SOURCE POINT.
It may still be useful as a truncated diagnostic, but not as E2 source validation.
10. REQUIRED ENERGY-SUPPORT SCALING
A simple support rule is to keep:
x_max = Emax/TBH
at least comparable to the original low-edge value.
To preserve x_max≈9.5–10:
M=6e8 g:
Emax should be approximately
1.7–1.8e5 GeV.
M=3e8 g:
Emax approximately
3.3–3.5e5 GeV.
M=1e8 g:
Emax approximately
1.0–1.1e6 GeV.
For stricter tail control the required Emax is larger.
11. HADRONIZATION SUPPORT THEN BECOMES THE NEXT GATE
The archived project PYTHIA table-generation scripts use initial-energy grids ending at:
1e5 GeV.
They also contain an explicit comment that Pythia8 becomes too slow above that energy in their generation workflow.
Thus:
raising BlackHawk Emax above 1e5 GeV
is not by itself sufficient.
One must also provide hadronization support for the higher primary energies.
Therefore the legal E2 requirement is:
PBH MASS SUPPORT
+
PRIMARY HAWKING ENERGY SUPPORT
+
HADRONIZATION TABLE SUPPORT.
All three must overlap.
12. WHY PRIMARY TAIL FRACTION IS NOT A HADRON-YIELD ERROR BAR
High-energy primary partons generally produce MORE secondaries per primary because QCD jet multiplicity grows with jet energy.
Therefore:
missing primary NUMBER fraction
does not upper-bound
missing secondary HADRON fraction.
A 9% primary-number tail can contribute more than 9% of secondary hadron count.
Similarly:
primary ENERGY tail
is not directly the relevant BBN hadron-count weight.
Hence 024 does not assign a source uncertainty percentage from the thermal proxy.
13. UPDATED E2 OPTIONS
E2a — TRUNCATED DIAGNOSTIC
Run lower masses with current Emax=1e5 GeV.
Use only to inspect the supported low-energy contribution.
Do NOT call this full source validation.
E2b — EXTENDED PYTHIA TABLES
Extend the BBN hadronization tables to primary energies sufficiently above the desired x_max threshold.
Then rerun BlackHawk with matched Emax.
E2c — HIGH-ENERGY DONOR / SPLICE
Use current BlackHawk/PYTHIA source where supported and a separately validated high-energy fragmentation donor above the table edge.
Requires continuity / overlap audit and transient-species semantics.
E2d — SOURCE-LEVEL ASYMPTOTIC MODEL
Use a QCD-curved tail with an explicit uncertainty envelope.
This is weaker than direct hadronization and remains a stress/closure model, not empirical validation.
14. UPDATED FRONT B SOURCE-ADMISSION ORDER
G0a
MASS source-table support.
G0b
PRIMARY-energy support Emax/TBH.
G0c
HADRONIZATION-energy support.
G1
source extrapolation / source-model stress.
G2
raw executor floor semantics.
G3
population DE-vs-full.
G4
A/B directional rates.
G5
dynamic X_n.
G6
Yp / D-H target validation.
G7
B2 carrier/background.
This is sharper than the source-only gate in 022–023.
15. INTERACTION WITH MECH-S6 98.2% RESULT
Mech-S6 showed that under current E0 executor semantics ~98.2% of the unweighted sub-edge hadron count lies in approximately 1.06e8–1e9 g.
024 shows that much of precisely this high-leverage near-edge interval cannot be source-validated merely by lowering the BlackHawk mass while keeping the existing energy grid.
Therefore the near-edge validation problem is not:
“run three cheap lower-mass points”.
It is:
“run lower-mass points under MATCHED expanded energy + hadronization support”.
This raises the cost of E2 but also makes the missing contract explicit.
16. RELATION TO 023 QCD PRIOR
023 showed:
E0 M^-1.20 is a plausible local effective slope but not an exact terminal QCD asymptote.
024 adds:
the exact public generator itself loses dimensionless spectral coverage as mass is lowered at fixed Emax.
Therefore source curvature below 1e9 g can arise from at least two distinct causes:
A
REAL QCD multiplicity / species-fraction evolution.
B
FINITE ENERGY-SUPPORT TRUNCATION if a lower-mass generator is rerun naively.
These must not be conflated.
17. NO EXTERNAL MODEL USE
No additional AI model was invoked.
The decisive evidence came from the exact public v2 notebook recovered through its Git blob and from transparent support calculations.
This is precisely a case where another model would add narrative rather than evidence.
18. STATUS
WU_XU_V2_SOURCE_GENERATOR
= RECOVERED / PASS EXACT.
SOURCE_TABLE_MASS_GRID
= 1e9–4e12 g / 100 POINTS / PASS EXACT.
GENERATOR_PRIMARY_ENERGY_GRID
= 5–1e5 GeV / 100 POINTS / PASS EXACT.
1e9g_AS_HARD_BLACKHAWK_MASS_LIMIT
= NO.
1e9g_AS_DOCUMENTED_PHYSICAL_BOUND
= NOT ESTABLISHED.
1e9g_AS_PERCENT_LEVEL_ENERGY_COVERAGE_SCALE
= STRONG PROJECT INFERENCE / NOT AUTHOR-INTENT CLAIM.
NAIVE_E2_AT_6e8g_FIXED_Emax
= PARTIAL / NONNEGLIGIBLE TAIL.
NAIVE_E2_AT_3e8g_FIXED_Emax
= NOT ADEQUATE FOR FULL SOURCE VALIDATION.
NAIVE_E2_AT_1e8g_FIXED_Emax
= NOT ADEQUATE FOR FULL SOURCE VALIDATION.
EXTENDED_HIGH_ENERGY_HADRONIZATION
= REQUIRED FOR SOURCE-COMPLETE LOW-MASS E2.
TERMINAL_SOURCE_PHYSICAL_VALIDATION
= OPEN.
LOG_FLOOR
= SECONDARY.
PBH_DE_DYNAMIC_ACCURACY
= OPEN.
PBH_Yp_DH_TARGET_VALIDATION
= OPEN.
SOURCE_MATCHED_K_PBH
= UNDEFINED.
NO PBH BOUND / NO ENDPOINT RELEASE.
NO CANON / NO EXEC_SIGN / NO NOVELTY / SCIENCE_FIRST.
SOURCES
[Wu–Xu v2 commit]
[valid_hadrons_from_BlackHawk.ipynb]
[Wu–Xu public GitHub]
[BlackHawk v2.3 embedded source]
[MacGibbon–Webber 1990]
