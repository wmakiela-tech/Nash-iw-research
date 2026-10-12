# REC9 XH-S3 Wu-Xu generator energy-support referee

RETURN_ID: REC9-XH-S3-WU-XU-GENERATOR-ENERGY-SUPPORT-REFEREE-001
VERDICT: PASS_PRACTICAL_E2_SUPPORT_GATE / REPAIR_ENERGY-SUPPORT_TYPING_AND_PROXY_CEILING
SEVERITY: MEDIUM

PASS:
Wu-Xu v2 notebook at commit d395183... uses mass grid 1e9..4e12 g / 100 points and calls set_BlackHawk_energy_spectrum!(...,5 GeV,1e5 GeV,100) for generated source points, then integrates returned secondary pi/K/K0L/p/n spectra to make hadrons_from_PBH.dat.

The wrapper writes E_number/Emin/Emax as BlackHawk run parameters and describes them as primary-particle energies.

Wu-Xu paper independently states BlackHawk v2.3 BBN PYTHIA tables have initial hard-process parton support capped at 1e5 GeV and warns against using default BlackHawk for very energetic meson fluxes above that scale. It also states PBHs around and above 1e9 g are not significantly affected and uses analytic estimates.

Therefore:
LOWER-MASS RUNNABILITY != SOURCE-COMPLETE MESON GENERATION.

MAIN TYPE REPAIR:
Do not collapse all 1e5-GeV ceilings into one object.

A USER/RUN SPECTRUM GRID = (Emin,Emax,E_number).
B HADRONIZATION INITIAL-PARTON SUPPORT = fixed PYTHIA table support (Emin_hadro,Emax_hadro,...).
C SECONDARY OUTPUT/RATE-INTEGRATION SUPPORT = returned secondary-energy grid actually integrated to dN_h/dt.

In the current generator these upper scales meet at 1e5 GeV, but:
USER_Emax != HADRONIZATION_Emax != SECONDARY_INTEGRATION_SUPPORT as types.

Emax/T_BH is a useful PRIMARY thermal-coverage diagnostic only.

Quoted fermionic proxy tails are numerically correct:
number tail x^2/(e^x+1):
x=9.46 ~0.48%;
5.68 ~8.6%;
2.84 ~50%;
0.946 ~94.8%.
Energy-weighted proxy:
~1.6%, 19%, 71%, 98.9%.

But:
THERMAL PRIMARY TAIL FRACTION != SPECIES-SPECIFIC HADRON SOURCE ERROR BAR.
GEOMETRIC-OPTICS PROXY != EXACT BLACKHAWK GREYBODY TAIL.
Emax/T_BH != HADRONIZATION VALIDITY.

E2 DISPOSITION:
6e8 g at current 1e5 support = PARTIAL/TRUNCATED DIAGNOSTIC ONLY.
3e8 g = NOT FULL SOURCE VALIDATION.
1e8 g = NOT FULL SOURCE VALIDATION.

This negative conclusion does not require interpreting proxy percentages as error bars.

1e9-g coincidence with x_max~9.5 and percent-level proxy tail is source-consistent and agrees with Wu-Xu's statement that >=1e9 g is not significantly affected by the table limit, but it does NOT establish author intent.
Use:
1e9g_COVERAGE_SCALE = SOURCE-CONSISTENT DIAGNOSTIC / NOT AUTHOR-INTENT CLAIM.

SOURCE-COMPLETE LOW-MASS E2 requires matched overlap of:
PBH mass support;
run spectrum-energy support;
initial-parton hadronization-table support;
secondary output/integration support;
identified transient-species semantics.

Raising only BlackHawk user Emax is insufficient if hadronization tables remain capped.
Extending hadronization tables alone is also insufficient if run/output integration support remains too small.

Gate typing:
G0a MASS SUPPORT
G0b RUN SPECTRUM SUPPORT
G0c HADRONIZATION INITIAL-PARTON SUPPORT
G0d SECONDARY SOURCE-INTEGRATION SUPPORT
then source stress -> floor -> DE/full -> A/B -> X_n -> Yp/D-H -> B2.

FINAL:
WU_XU_V2_SOURCE_GENERATOR=PASS_RECOVERED.
SOURCE_TABLE_MASS_GRID=PASS_EXACT.
CONFIGURED_5_TO_1E5_GEV_GRID=PASS_EXACT.
BLACKHAWK_BBN_HADRONIZATION_INITIAL_PARTON_LIMIT_1E5=SOURCE-SUPPORTED.
NAIVE_LOW_MASS_FIXED_1E5_E2=NOT_FULL_SOURCE_VALIDATION.
MATCHED_HIGH_ENERGY_SUPPORT=REQUIRED.
TERMINAL_SOURCE_PHYSICAL_VALIDATION=OPEN.
PBH_DE_DYNAMIC_ACCURACY=OPEN.
PBH_Yp_DH_TARGET_VALIDATION=OPEN.
SOURCE_MATCHED_K_PBH=UNDEFINED.
NOVELTY=NONE.
REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD.
NO CANON / NO EXEC_SIGN / NO NEW TASK / NO NEW FRONT.

STOP after integration.
