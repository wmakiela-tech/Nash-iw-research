---
artifact_id: XH-S3-FRONTB-WU-XU-LOG-FLOOR-INITIALIZATION-MATERIALITY-HARVEST-021
created_at: 2026-10-12
as_of: 2026-10-12
origin_cell: XH-S3
document_type: RETURN
exposure: PUBLIC
archive_mode: PUBLIC_ARTIFACT
bw_ingestion_event_id: ING-20261012-0061
bw_qualification_state: SOURCE_INITIAL_SEED_FLOOR_MATERIALITY_NARROWED
bw_lifecycle_state: CURRENT_REPRESENTED
scientific_claim_ceiling: EXTERNAL_HARVEST_NO_OWNER_AUTHORITY
source_revision: PRIVATE_ORIGINAL_BW_ROW_1388
no_canon: true
no_exec_sign: true
---

> Full public scientific return, published from the pre-existing verified BW source. Original scientific body below is preserved without intentional modification. Public release is not scientific acceptance, novelty or physical validation.

﻿XH-S3 / FRONT B — WU–XU LOG-FLOOR INITIALIZATION MATERIALITY HARVEST 021


RETURN_ID
XH-S3-FRONTB-WU-XU-LOG-FLOOR-INITIALIZATION-MATERIALITY-HARVEST-021


RESULT
THE PUBLIC WU–XU INITIAL HADRON SEED IS FAR ABOVE THE exp(-100) LOG-POPULATION FLOOR THROUGHOUT THE PUBLISHED 6e8–1e10 g SCAN RANGE.
THEREFORE THE FLOOR IS NOT AN INITIALIZATION ARTIFACT IN THE DECLARED SCAN.
THE ONLY MATERIAL FLOOR RISK IS LATER RE-ENTRY BELOW THE FLOOR WHILE A NONZERO PBH HADRON SOURCE IS STILL ACTIVE.
SOURCE-OFF TAILS ARE EXACTLY UNAFFECTED BY THE FLOOR RESIDUAL.
NO PBH ENDPOINT / NO BOUND RELEASE.


FIREWALL
INITIAL FLOOR INACTIVITY != FLOOR NEVER ACTIVE LATER.
APPROXIMATE FORMATION-TEMPERATURE ESTIMATE != EXECUTOR TRACE.
FLOOR BELOW POPULATION != PHYSICAL IRRELEVANCE unless source-weighted residual is small.
NO CANON / NO EXEC_SIGN / NO NOVELTY.


1. PUBLIC EXECUTOR SEMANTICS


Sources:
[Wu–Xu public GitHub]
[NaturalUnits.jl public GitHub]


The public code sets:
EU = GeV.


Hadron number densities are therefore represented internally in GeV^3.


The log-population clamp reconstructs each hadron density using:
n_bar = exp(max(log n, -100)) GeV^3.


Thus the floor is exactly:


n_floor = exp(-100) GeV^3
≈ 3.7201e-44 GeV^3.


Mech-S6 already derived the exact floor-active executor equation:
n' = min(1,n/n_floor) S - D n.


021 asks whether the INITIAL public seed starts above or below this floor.


2. PUBLIC INITIAL SEED


Wu–Xu initialize every hadronic density as:


n_seed
=
1e-60 * 2*zeta(3)*T_f^3/pi^2
=
1e-60 * n_gamma(T_f).


Set n_seed = n_floor.


This gives an exact temperature threshold in the code’s GeV convention:


T_floor-seed
=
[
exp(-100)
/
(1e-60 * 2*zeta(3)/pi^2)
]^(1/3)


≈ 5.345e5 GeV.


Therefore:


T_f > 5.35e5 GeV
=> initial hadron seed ABOVE floor.


T_f < 5.35e5 GeV
=> initial seed BELOW floor.


This threshold does not depend on PBH beta or hadron microphysics.


3. PUBLISHED SCAN RANGE


The public main-scan-parameters.jl uses:


m_PBH,min = 6e8 g
m_PBH,max = 1e10 g.


The code forms PBHs with:


t_f = m_PBH / (gamma_PBH m_Pl^2),
gamma_PBH = 1/(3 sqrt(3)),


and initializes radiation through:


H_f = 1/(2 t_f),
rho_SM,f = 3 M_Pl^2 H_f^2,
T_f = from_rho_to_T(rho_SM,f).


NaturalUnits.jl identifies:
M_Pl ≈ 2.435e18 GeV (reduced Planck mass),
m_Pl ≈ 1.221e19 GeV (Planck mass).


4. HIGH-T ESTIMATE OF THE FORMATION TEMPERATURE


At these formation scales the standard high-T radiation relation gives, for g_*≈106.75:


rho = (pi^2/30) g_* T^4.


Combining this with the exact formation-time convention above gives approximately:


T_f(1e10 g)
≈ 4.3e10 GeV,


T_f(6e8 g)
≈ 1.7e11 GeV.


These are about 8e4–3e5 times ABOVE the 5.35e5 GeV seed/floor threshold.


Correspondingly:


ln(n_seed/n_floor)
≈ 33.9 at 1e10 g,
≈ 38.1 at 6e8 g,


so:


n_seed/n_floor
≈ 5e14
to
≈ 3e16.


Hence the published scan starts with an enormous margin above the log floor.


IMPORTANT:
These temperature numbers use the high-T constant-g_* approximation to interpret the public formation convention.
The conclusion is robust because the margin is 14–16 orders of magnitude in density, so O(1) uncertainty in g_* cannot change floor activity at initialization.


5. CHECK ON from_rho_to_T EXTRAPOLATION


The public from_rho_to_T inversion is tabulated from 1e-5 to 1e3 GeV and uses LINEAR extrapolation in log10 rho -> log10 T.


The N_rho and N_s interpolators themselves use CONSTANT extrapolation outside the tabulated PDG ranges.


Thus, once the relativistic degrees of freedom have saturated at high temperature, the sampled relation becomes:


log rho = const + 4 log T,


and the linear log-log extrapolation preserves the expected T proportional to rho^(1/4) behavior.


021 does NOT treat “T_f above 1e3 GeV table maximum” as an error by itself.


A separate exact data-file endpoint audit would be needed to certify the last-tabulated g_* plateau numerically, but no material floor conclusion depends on that audit because the seed/floor margin is enormous.


6. REPAIR OF THE CURRENT FLOOR BLOCKER


OLD OPEN QUESTION:
Could the exp(-100) clamp already distort the initial hadron population and therefore contaminate the whole run?


ANSWER FOR THE PUBLISHED SCAN:
NO.


The initial seed is safely above floor.


Therefore the only material executor-level question is:


DOES ANY HADRON POPULATION LATER CROSS BELOW n_floor WHILE S_h(t)>0?


If NO:
floor residual is identically absent over the source-active interval.


If YES:
the exact source-injection residual from Mech-S6 applies:


rho_floor,h
=
S_h [min(1,n_h/n_floor)-1].


7. SOURCE-OFF TAIL


When the PBH source turns off:


S_h=0.


Then exactly:


rho_floor,h=0,


even if n_h<n_floor.


Therefore the clamp does not alter the post-source depletion law n'=-D n.


This means:
late numerical floor occupancy AFTER source shutoff is not itself a physical model error in the population equation.


The material overlap is only:


FLOOR ACTIVE
AND
SOURCE ACTIVE.


8. CHEAPEST CURRENT-RUN DIAGNOSTIC


No new full PBH scan is required.


For any existing or future full Wu–Xu trajectory, record for each hadron species:


A
first downward crossing of n_h=n_floor;


B
first upward exit/re-entry if any;


C
whether S_h>0 during the floor-active interval;


D
integrated exact source residual:


E_floor,h
=
∫_{n_h<n_floor, S_h>0}
S_h(t) [1-n_h/n_floor] dt;


E
overlap with the BBN target-sensitive epoch.


Strong sufficient pass:


n_h(t) >= n_floor
for all t with S_h(t)>0.


Weaker target-relative pass:
E_floor,h propagated through the existing M12 source->population->X_n->target error chain lies below declared tolerance.


9. RELATION TO 020


The floor rescales each source by a nonnegative factor alpha_h=min(1,n_h/n_floor).


Therefore the 020 monotonicity and unique-root theorem survives structurally:
the source amplitudes remain nonnegative.


What the floor can change is:
- source magnitude/history;
- species composition;
- DE-vs-FULL population tracking;
- directional rates.


It does NOT introduce instantaneous DE root multiplicity.


10. CURRENT CLAIM CEILING


WU_XU_FLOOR_VALUE
= exp(-100) GeV^3 / exact from code.


PUBLIC_INITIAL_SEED
= 1e-60 n_gamma(T_f) / exact from code.


SEED_FLOOR_TEMPERATURE_THRESHOLD
= 5.345e5 GeV / derived exactly from those two code definitions.


PUBLISHED_SCAN_RANGE
= 6e8–1e10 g / exact from public scan parameters.


INITIAL_FLOOR_ACTIVITY_IN_PUBLISHED_SCAN
= NO / robust high-T source-convention assessment.


LATE_SOURCE_ACTIVE_FLOOR_REENTRY
= NOT EVALUATED.


SOURCE_OFF_FLOOR_RESIDUAL
= ZERO / exact.


CURRENT_RUN_FLOOR_MATERIALITY
= NARROWED TO LATE SOURCE-ACTIVE REENTRY.


PBH_DE_DYNAMIC_ACCURACY
= OPEN.


PBH_Yp_DH_TARGET_VALIDATION
= OPEN.


SOURCE_MATCHED_K_PBH
= UNDEFINED.


NO PBH BOUND / NO ENDPOINT / NO CANON / NO EXEC_SIGN / NO NOVELTY / SCIENCE_FIRST.


11. MODEL-USE DISCIPLINE


No external AI model invoked.


The question was an exact executor/unit/initial-condition audit.
Direct source-code inspection plus transparent algebra had higher evidential value and lower Moderator cost.


SOURCES
[Wu–Xu public GitHub]
[NaturalUnits.jl public GitHub]