---
artifact_id: XH-S3-FRONTB-BBN-TARGET-SENSITIVITY-WINDOW-HARVEST-016
bw_ingestion_event_id: ING-20261010-0118
bw_qualification_state: FRONTB_BBN_TARGET_SENSITIVITY_WINDOW
bw_lifecycle_state: CURRENT_REPRESENTED
bw_authority_state: EXTERNAL_EVIDENCE_NO_AUTHORITY
archive_mode: PUBLIC_ARTIFACT
sync_state: SEE_BW_CROSS_SURFACE_CUSTODY
source_surface: GOOGLE_DRIVE
source_revision: PRIVATE_SOURCE_REVISION_RECORDED_IN_BW
mirror_note: PUBLIC_SAFE_SANITIZED_MIRROR_PRIVATE_PROVIDER_LOCATORS_REDACTED
---

# XH-S3-FRONTB-BBN-TARGET-SENSITIVITY-WINDOW-HARVEST-016

> Public-safe mirror of the BW-linked private source. BW controls lifecycle/currentness; GitHub does not upgrade scientific authority.

XH-S3 / FRONT B — BBN TARGET-SENSITIVITY WINDOW HARVEST 016
RETURN_ID
XH-S3-FRONTB-BBN-TARGET-SENSITIVITY-WINDOW-HARVEST-016
RESULT
TIME/TEMPERATURE-RESOLVED HADRONIC n↔p TARGET KERNEL = NOT LOCATED AS READY-MADE PUBLIC OBJECT
CUMULATIVE WEAK-RATE SENSITIVITY WINDOW = MATURE DONOR
GLOBAL PARAMETER/RATE SENSITIVITIES = MATURE / PUBLIC
PUBLIC SOFTWARE SEAM FOR CONSTRUCTING LOCAL KERNEL = AVAILABLE
FRONT B NEXT VALIDATION OBJECT = TARGET-WEIGHTED DE-vs-FULL-HISTORY RATE ERROR
FIREWALL
External source/provenance harvest only.
GLOBAL PARAMETER DERIVATIVE != TIME-LOCAL RESPONSE KERNEL.
LATE-WEAK-RATE SENSITIVITY != HADRONIC CLOSURE ERROR BOUND.
Yp SENSITIVITY != D/H SENSITIVITY.
QUALITATIVE WINDOW != SOURCE-MATCHED PBH TARGET CERTIFICATE.
NO_CANON / NO_EXEC_SIGN / NO_NUMERICAL_ENDPOINT / NO_NOVELTY.
1. QUESTION
After 015, the relevant issue is no longer whether the dynamical-equilibrium approximation reproduces hadron densities pointwise.
The scientific target is:
does DE-vs-full-history error in hadronic p↔n rates matter where final BBN observables are sensitive?
Need an object of the form, locally around a frozen baseline:
δY
≈
∫ dlnT [
W_Y^{n→p}(T) δlnΓ_{n→p}(T)
+
W_Y^{p→n}(T) δlnΓ_{p→n}(T)
]
for Y ∈ {Yp, D/H, ...},
or an equivalent finite-bin response matrix.
2. MATURE DONOR A — GROHS–FULLER 2016 GIVES A CUMULATIVE TEMPERATURE WINDOW
SOURCE
[Grohs–Fuller 2016]
The paper “The surprising influence of late charged current weak interactions on Big Bang Nucleosynthesis” explicitly tests the common instantaneous weak-freeze-out intuition.
It modifies / turns off charged-current n↔p processes below a user-selected T_WFO and follows the resulting abundance evolution.
SOURCE-NATIVE RESULT:
weak n↔p processes remain important well below the conventional T~0.7 MeV “freeze-out” scale, down toward the alpha-particle formation epoch near T~0.1 MeV.
Thus the target-relevant weak-rate support is broad in temperature.
For extreme cutoff experiments, final Yp changes strongly; D and He3 also move, although less directly than helium.
This gives a CUMULATIVE WINDOW statement:
the integrated effect of weak-rate changes below a cutoff remains non-negligible to much lower T than a one-time freeze-out picture suggests.
IMPORTANT:
the T_WFO scan is not itself the local functional derivative W_Y(T).
It is closer to an integrated / cumulative sensitivity experiment.
3. MATURE DONOR B — 2026 BBN SENSITIVITY ATLAS
SOURCE
[Burns 2026 sensitivity atlas]
[bbn-sensitivity-atlas public repository]
The 2026 atlas provides:
- local sensitivities of final Yp, D/H, Li/H and Neff to 14 fundamental/cosmological parameters;
- sensitivities to 63 thermonuclear reaction rates;
- public response curves and uncertainty budgets;
- PRyMordial-based calculations with multiple weak-rate normalization schemes.
This is strong target-level sensitivity infrastructure.
But the public atlas varies:
GLOBAL physical parameters
or
WHOLE reaction rates / normalization parameters.
It does not expose a published bin-by-bin Gateaux derivative of final Yp/D-H with respect to an arbitrary local-in-T perturbation of Γ_{n→p}(T), Γ_{p→n}(T).
Therefore:
GLOBAL RATE/PARAMETER SENSITIVITY
!=
TIME-LOCAL WEAK-RATE KERNEL.
4. PUBLIC SOFTWARE SEAM — PRIMAT
SOURCE
[PRIMAT custom Background interface]
PRIMAT’s Python Background interface requires user-provided:
weak_nTOp(T_K)
weak_pTOn(T_K)
and supports full BBN network integration.
This gives a direct numerical route for constructing the missing response kernel:
take baseline Γ_±(T);
choose localized basis functions b_j(lnT);
perturb one direction at a time:
Γ_±^{(j,±ε)}(T)
=
Γ_±(T) exp(± ε b_j(lnT));
run the SAME frozen full BBN problem;
estimate centered finite difference:
W_{Y,j}^{±}
≈
[Y(Γ_± e^{+εb_j}) - Y(Γ_± e^{-εb_j})] / (2ε).
If b_j approximates a normalized bin in lnT, this yields a discrete approximation to δY/δlnΓ_±(T).
This finite-difference construction is a PROJECT INFERENCE from the public software contract and standard numerical differentiation.
It is not claimed as a published new BBN result.
5. WHY THIS IS THE CORRECT VALIDATION OBJECT FOR 015
Let the full-time and dynamical-equilibrium donor produce two rate histories:
Γ_full,±(T)
and
Γ_DE,±(T).
Define:
δlnΓ_±(T)
=
ln[Γ_DE,±(T)/Γ_full,±(T)].
Then, in the local-response regime:
δY_target
≈
∫ W_Y^+(T) δlnΓ_+(T) dlnT
+
∫ W_Y^-(T) δlnΓ_-(T) dlnT.
Therefore:
POINTWISE HADRON ERROR
is not the final criterion.
Nor is:
UNWEIGHTED INTEGRATED HADRON YIELD ERROR.
The relevant object is:
TARGET-WEIGHTED RATE-HISTORY ERROR.
6. LATE-TIME SUPPORT IS LOAD-BEARING
Grohs–Fuller establishes that the target window does not stop sharply at conventional weak freeze-out.
Consequently:
a closure error localized around T~0.2–0.1 MeV cannot be dismissed solely because Γ_weak < H or because “freeze-out already happened”.
For Yp, residual n↔p processing near onset of nuclear assembly can still matter.
This is particularly relevant for PBH terminal evaporation:
the Hawking source can become most rapidly varying late in a PBH trajectory,
exactly where a naive fast/slow source approximation may become least controlled.
Thus:
TERMINAL SOURCE RAPIDITY
×
LATE BBN WEAK SENSITIVITY
is the key overlap region to test.
7. Yp AND D/H MUST REMAIN SEPARATE TARGETS
Yp is especially sensitive to the neutron inventory / n:p history.
D/H additionally depends strongly on the nuclear network and destruction/production reactions after the deuterium bottleneck.
Therefore:
a closure that preserves Yp to tolerance does not automatically preserve D/H.
Need distinct:
W_Yp^{np}(T)
and
W_DH^{np}(T),
and, if hadronic injection also produces nonthermal nuclear effects, separate nuclear-response channels.
8. TWO DIFFERENT LINEARIZATIONS MUST NOT BE CONFUSED
A. BACKGROUND / FUNDAMENTAL PARAMETER RESPONSE
δp modifies multiple parts of the calculation coherently.
B. DIRECT RATE-HISTORY RESPONSE
δΓ_np(T) is inserted as a controlled local perturbation.
The Burns atlas mainly supplies A and whole-rate variations.
Front B requires B for transfer-validation of the DE approximation.
Hence one cannot substitute:
dlnY/dlnτ_n
for
δY/δlnΓ_np(T).
9. SOURCE-NATIVE BOUNDED VALIDATION DESIGN
No production endpoint is needed initially.
Freeze:
- one PBH/B2 source history Q_h(t);
- one cosmological background;
- one hadronic microphysics set;
- one full-time reference;
- one DE closure;
- one BBN network.
Step V1:
obtain Γ_full,n→p(T), Γ_full,p→n(T).
Step V2:
obtain Γ_DE,n→p(T), Γ_DE,p→n(T).
Step V3:
construct local BBN response kernels by narrow lnT perturbations of the SAME weak-rate receiver.
Step V4:
compute target-weighted predicted error from rate-history difference.
Step V5:
directly run full BBN with full-history and DE histories and compare final Yp/D-H.
V4 vs V5 checks the local-response approximation itself.
This is a VALIDATION DESIGN only, not an execution authorization.
10. STRONGEST CHEAP NEGATIVE TEST
Before any expensive B2 scan, choose a source that maximizes overlap between:
A rapid DE/full-history discrepancy
and
the late weak-sensitive window.
Candidate scientific stress class:
sharp terminal source increase around T~0.3–0.1 MeV.
If DE remains target-accurate there, transfer confidence rises substantially.
If not:
the donor closure can still be valid elsewhere, but PBH terminal-evaporation transfer fails or needs a hybrid full-time patch.
11. POSSIBLE HYBRID ADAPTER IF CLOSURE FAILS ONLY LOCALLY
If DE is accurate except in a bounded terminal/threshold epoch:
use
DE closure outside the bad window
+
full-time hadron evolution inside the identified sensitive overlap window.
This is a logically weaker intervention than replacing the whole BBN calculation with a monolithic all-state solver.
STATUS:
HYBRID_ROUTE = ARCHITECTURALLY PLAUSIBLE / NOT SOURCE-VALIDATED.
12. CURRENT CLAIM CEILING
READY-MADE TIME-LOCAL W_Y(T)
= NOT LOCATED.
CUMULATIVE LATE-WEAK TARGET WINDOW
= PASS / MATURE DONOR via Grohs–Fuller.
GLOBAL BBN TARGET SENSITIVITIES
= PASS / MATURE + PUBLIC via Burns atlas.
PUBLIC NUMERICAL SEAM FOR LOCALIZED Γ_np(T) PERTURBATIONS
= PASS via PRIMAT custom Background.
FRONT B NEXT SCIENTIFIC OBJECT
= TARGET-WEIGHTED DE-vs-FULL RATE-HISTORY VALIDATION.
PBH/B2 NUMERICAL BOUND
= NOT READY.
SOURCE_MATCHED_K_PBH
= UNDEFINED.
BIS_PBH_MODEL_SPECIFIC_BOUND
= NONE.
NO endpoint release.
13. ANTI-OVERCLAIM
Do NOT say:
- Grohs–Fuller provides the desired W(T) directly;
- the Burns atlas is a time-local weak-rate kernel;
- a 1% hadron-density difference implies a 1% Yp difference;
- conventional freeze-out makes late closure error irrelevant;
- Yp validation automatically validates D/H;
- finite-difference kernel around one baseline is globally valid for large PBH perturbations.
14. MODEL-USE DISCIPLINE
No external AI model used.
This rotation required source comparison, not divergent ideation.
Expected marginal benefit from another model did not exceed coordination cost.
External model use remains reserved for:
- independent audit of a concrete derived kernel;
- divergent stress cases after one kernel exists;
- unresolved literature ambiguity not closed by source-first search.
STATUS
TARGET_SENSITIVITY_WINDOW_HARVEST = PASS.
TIME_LOCAL_KERNEL_SOURCE = GAP CONFIRMED.
CONSTRUCTION_PATH = PUBLICLY ENABLED.
FRONT_B_BLOCKER = FURTHER SHARPENED.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / SCIENCE_FIRST.
SOURCES
[Grohs–Fuller 2016]
[Burns 2026 sensitivity atlas]
[bbn-sensitivity-atlas public repository]
[PRIMAT custom Background interface]
