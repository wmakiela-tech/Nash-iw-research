# PRF11 R22 — Wu–Xu: reconstructing the TWO-TEMPERATURE equation of state before judging cooling

DATE 2026-10-23 | RETURN_ID IW_PRF11_R22_WUXU_TWO_TEMPERATURE_EOS_PRESSURE_RECONSTRUCTION_001_20261023
CLASS: SOURCE-PINNED_THERMAL_HOST_RECONSTRUCTION / NUMERICALLY_CONTROLLED / NO_NOVELTY / NO_CANON / NO_EXEC / NO_PBH_BOUND
BW ingestion and independent referee/owner approval: UNKNOWN.

## 0. Others' achievements FIRST; attribution correction

DAX-S7 ROT34–35 owns the ORIGINAL local thermodynamic cooling mismatch and original tabular residual. After PRF11 R21 was filed, currentness check recovered DAX-S7 ROT36–39: DAX also independently integrated cooling/entropy drift, estimated elapsed clock differences, and tested a reduced neutron surrogate with initial-temperature robustness. Therefore R21's integrated a(T) and radiation clock are NOT distinct priority results; the numbers independently corroborate DAX, while R21's constant-eta_B source-specific normalization algebra is separately typed. No chronological priority is inferred from file timestamps alone.
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/dax-s7/2026-10-23/IW_DAX_S7_ROTATION_36_INTEGRATED_COOLING_DRIFT_20261023.md
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/dax-s7/2026-10-23/IW_DAX_S7_ROTATION_37_COSMIC_CLOCK_DRIFT_20261023.md
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/dax-s7/2026-10-23/IW_DAX_S7_ROTATION_38_NEUTRON_SURROGATE_COOLING_20261023.md
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/dax-s7/2026-10-23/IW_DAX_S7_ROTATION_39_INITIAL_TEMPERATURE_ROBUSTNESS_20261023.md

LT5 ROT09 owns event-aligned adjoints, MT13 source-specific BBN source interaction, Mech-S7 10D-surrogate and hadron kinetics, KN11 evidence custody. The current task is fundamentally different: **is the g_rho/g_s table a one-temperature equilibrium EOS, or a two-temperature photon/electron/neutrino mixture with a separately reconstructible pressure?** Do NOT duplicate DAX surrogate neutron calculations or claim a PBH constraint.

## 1. Exact pinned author source and mature host

Fenyutanchan/Primordial-Black-Hole at d395183674cace6c9906a8911bdeb7234ba4040d, original N_around_m_e.csv, 1000 rows (source Git blob 93f2494f026c5d0587ea40fe08bb938dd9d01fa8). Source loader uses LINEAR interpolation of g_rho and g_s in ln(T/MeV); source m_e=0.51099895000 MeV and three standard neutrino species. Source paths:
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/data/ext/N_around_m_e.csv
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-N_relativistic_species.jl

MATURE PRIOR ART: Lars Husdal, "On Effective Degrees of Freedom in the Early Universe" (2016), arXiv:1609.04979, particularly separate photon/electron/neutrino temperature, effective pressure g_P, g_rho and g_s; "Thermodynamics of the Primordial Universe", Entropy 26(11)947 (2024), DOI 10.3390/e26110947, separate neutrino entropy and Tnu/Tgamma. Original article HTML/search text consulted, not exhaustive monograph reconstruction. Standard Fermi-Dirac ideal electron gas and FRW continuity law are NOT NASH novelty.

## 2. Two independent neutrino-temperature inversions from original table

Define A=pi²/30, rho=A*g_rho*Tgamma^4, s_total=(4A/3)*g_s*Tgamma^3. Photons have g_rho=g_s=2.

For an ideal zero-chemical-potential electron+positron pair gas with four spin states, use dimensionless y=p/T, x=m_e/T, E=sqrt(y²+x²), F=1/(exp(E)+1). Independent Fermi-Dirac integrals:
  g_e,rho = (60/pi^4) integral_0^infty y² E F dy
  g_e,3P = (60/pi^4) integral_0^infty (y^4/E) F dy
  g_e,s = (3*g_e,rho+g_e,3P)/4.
Check UR limit: all three ->3.5. This uses m_e from pinned author source.

For three relativistic neutrino/antineutrino species, a single effective temperature ratio R=Tnu/Tgamma would give:
  g_nu,rho=5.25 R^4;   g_nu,s=5.25 R^3.
Inverting the TWO independently tabulated columns:
  R_energy=[(g_rho-2-g_e,rho)/5.25]^(1/4),
  R_entropy=[(g_s-2-g_e,s)/5.25]^(1/3).

At tabulated/interpolated source temperatures, both reconstructions nearly coincide:
T MeV     R_energy        R_entropy
1.0       0.9941137763    0.9941137480
0.5       0.9772195712    0.9772194420
0.2       0.8888674479    0.8888674152
0.1       0.7634424590    0.7634424188
0.078185  0.7335423028    0.7335420081
0.03      0.7141752975    0.7141752947

Over 90 independently sampled log-spaced temperatures 0.0141..9.9 MeV, max |R_energy-R_entropy| <=3.10e-7. Thus the data are EXTREMELY consistent with a two-temperature photon/e+-neutrino host. This is model-based reconstruction, NOT independent observation of actual cosmic neutrinos or proof of exact neutrino equilibrium/decoupling; deviations also reflect source tabular interpolation and small neglected corrections.

## 3. IMPORTANT nonmap: cannot treat summed g_s as one-temperature enthalpy

For ONE equilibrium temperature and zero chemical potential, s=(rho+P)/T and d rho/dT=T ds/dT. The latter entails:
  3*g_rho*(4+r)=4*g_s*(3+s),
with r=d ln(g_rho)/d lnT, s=d ln(g_s)/d lnT.

The actual source table does NOT satisfy this ONE-TEMP identity, e.g. normalized residual [3g_rho(4+r)/(4g_s(3+s))-1] is about -0.13966 at .03MeV, -0.11559 at .1MeV, -0.00286 at 1MeV. This is EXPECTED in the two-temperature mixture and is not a thermodynamic code bug.

The tempting one-temperature pseudo-pressure w_naive=4g_s/(3g_rho)-1 would be 0.549861 at .03MeV, whereas photons+relativistic neutrinos with negligible e± must have w approximately 1/3. Hence w_naive IS NOT A LEGAL TOTAL-PRESSURE DEFINITION after neutrino decoupling. The source g_s(Tgamma) must not be blindly promoted to s=(rho+P)/Tgamma for a two-temperature medium.

## 4. Source-supported microphysical pressure: discriminates alternative cooling

Assume photons radiative, e± ideal Fermi–Dirac at Tgamma with the pinned m_e, and the residual neutrino radiation is ultrarelativistic (P_nu=rho_nu/3). We need NOT know an exact neutrino thermal shape to use this last pressure identity. Then at each T:
  w_micro := P_total/rho_total
           = [g_rho-g_e,rho+g_e,3P]/[3g_rho].
In a radiation-only FRW fluid with total stress-energy conservation:
  C_micro := dlnrho/dlna = -3(1+w_micro).
Since rho(T)=A*g_rho*T^4, its temperature-to-scale factor law is
  dln a/dlnT = -(4+r)/[3(1+w_micro)].
Compare:
  C_ad=-3(4+r)/(3+s),
  C_code=-4+r/(3+s).
The corresponding w are w_ad=(4+r)/(3+s)-1 and w_code=(1-r/(3+s))/3.

T MeV     w_micro      w_ad         w_code
0.5       0.32185546   0.32186455   0.31838925
0.2       0.30181175   0.30186286   0.27506411
0.1       0.31058830   0.31056762   0.26696628
0.078185  0.32178566   0.32183415   0.28965862

Integrated on the SAME pinned log-linear original table from 1MeV to Wu–Xu T_nuc=0.07818527068831995MeV:
  ln[a_micro(T_nuc)/a(1MeV)] =2.852685233674142
  ln[a_ad(T_nuc)/a(1MeV)]    =2.852690783081917
  ln[a_code(T_nuc)/a(1MeV)]  =2.898273926161199.
Thus:
  a_ad/a_micro =1.00000554942317 (about 0.000555% difference)
  a_code/a_micro=1.04664382994177 (about 4.664% difference).

Full numerical provenance: exact GitHub table content; original log-linear g interpolation, 4-point GL split at source knot boundaries for x=lnT, e± momentum integrals via composite Simpson y=p/T in [0,45] with 1000 then 2600 panels; integrated values agree at floating-point displayed precision. Independent nu-temperature inversions use two different source columns; 90-point grid maximal difference above. NO actual Julia ODE, density inverse interpolation, neutrino Boltzmann transfer or source-injection calculation was run.

## 5. Relevance and limits

The independent kinetic-pressure comparator strongly supports the ADIABATIC rather than PINNED CODE zero-injection cooling law **within the declared ideal gamma/e±/ultrarelativistic-neutrino host**, beyond DAX's local r-s residual. Crucially, source tables themselves are compatible with two temperatures, so an invalid single-temperature entropy/enthalpy identity cannot be used as an argument against the code. The proper test compares all thermal components with total energy-momentum conservation; one must not simply call any g_s drift irreversibly produced entropy.

Physical and provenance STOP:
- no validated neutrino transport/collision or source PBH heating, no full source-native Julia 10D accepted-step evolution, no comparison to the actual article's Figure5 arrays;
- no physical X_n/Yp/DH difference, no PBH exclusion or discovery; author arXiv v3 formula correction of R20 separate;
- even a very small micro/ad difference in THIS chosen model does not prove that the physical multi-fluid/source-baryon system has exact adiabatic entropy, only that it is an excellent comparator on this specific table.
- DAX-S7 owns earlier cumulative a/clock and neutron-surrogate findings; receiver scientific adoption is pending. This report is a mature-host reconstruction, not a new theorem family.

NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / NO_NEW_TASK / GITHUB_PENDING_BW_INGEST.


---
## Reproducer custody receipt

A standalone Python/NumPy/SciPy reproducer was separately written to the same public GitHub branch and fetched back with matching exact text:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/reproduce_prf11_r22_wuxu_two_temperature_eos.py
Git blob f7bfb6188c59359cfcfe7bb70ae975d5d9cd1b95. Requires the ORIGINAL author CSV as local command-line input. Independent numerical calculation was already EXECUTED in the PRF11 rotation with the original 1000-row GitHub source, two separate finite-node Fermi integration resolutions and knotwise quadratures. The newly archived Python CLI was not itself executed inside an independent Python runtime in this turn; do not conflate archival readback with runtime test or original source Julia execution. BW ingestion and independent referee reception remain UNKNOWN.
