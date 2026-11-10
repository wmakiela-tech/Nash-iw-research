---
artifact_id: IW_DAX_S8_ROT005_CRPROPA_DPP_INPUT_SUPPORT_VS_ONSHELL_001_20261110
created_at: 2026-11-10
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
document_type: SCIENTIFIC_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: SOURCE_TYPED_INPUT_SUPPORT_KINEMATIC_COUNTERMODEL_AND_INTERPOLATION_GATE
claim_ceiling: NO_NATIVE_CRPROPA_EXECUTION / NO_STOCK_BACKGROUND_BUG_VERDICT / NO_FULL_QED_DIFFERENTIAL / NO_DEPOSITION / NO_PBH_BBN_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
independence: NONBLIND
---

# DAX-S8 ROT005 — input-support versus physical on-shell domain of the CRPropa DPP surrogate

Date 2026-11-10. **Conditional source-interface falsifier, not a native compiled C++ run, not a full QED differential operator, not a physical PBH/BBN result.**

## Precedence and currentness

DAX-S7 R67/R68 established the source-typed DPP-muon concern and the rate-versus-differential-kernel gap. DAX-S8 ROT001 provided an exact 4-lepton on-shell energy-redistribution witness; ROT002 separated first-event from eventual products; ROT003 first identified this CRPropa two-hard-lepton surrogate and the distinct scalar total-cross-section approximations; ROT004 first calculated the weighted-thinning variance and event-indicator bias. ROT005 adds an **input-support/source-runtime interface** and tests whether physical 2->4 production threshold implies the surrogate electron energy is on shell. It does not relabel those first results.

Bounded 2026-11-10 Slack/GitHub searches found no new direct DAX-S8 job, cell-specific new STOP, or source-valid full differential DPP QED operator. This is a bounded NO-MATCH, not a novelty or exhaustive nonexistence assertion. Wu–Xu/BBN studies remain with Badacz/Mech/MT owners.

## Exact pinned upstream source evidence

- CRPropa3 v3.3, src/module/EMDoublePairProduction.cpp, Git blob 682f001a264a741ba9615ed86490d9f216a52cfe:
  https://github.com/CRPropa/CRPropa3/blob/3.3/src/module/EMDoublePairProduction.cpp
  This code uses E=(1+z)*candidate energy and proxy Ee=(E-2*m_e*c^2)/2, deactivates primary photon, and, if haveElectrons and thinning samples allow, passes Ee/(1+z) to addSecondary for one e- and one e+. There is no local Ee>=m_e*c^2 guard. setInteractionRates permits user-specified rates; process tests particle ID, rate, and step, not proxy mass-shell admissibility.
- CRPropa3 v3.3 src/InteractionRates.cpp:
  https://github.com/CRPropa/CRPropa3/blob/3.3/src/InteractionRates.cpp
  Homogeneous rate lookup is global interpolate(E,tabEnergy,tabRate).
- CRPropa3 v3.3 src/Common.cpp, blob 876cdac7bd6b8ad65e7e910dc636d00a3abfafab:
  https://github.com/CRPropa/CRPropa3/blob/3.3/src/Common.cpp
  For E below first grid abscissa, interpolate returns Y.front(); above last grid, Y.back(). Thus **positive first rate clamps positive below support**, instead of imposing zero or a physical low-energy extrapolation.
- CRPropa3-data calc_electromagnetic.py, Git blob 030af585f62357e4522f64f7a7daa81c635b20d3:
  https://github.com/CRPropa/CRPropa3-data/blob/master/calc_electromagnetic.py
  Rate generator uses incoming-energy grid logspace(9,23) eV, then retains E>Emin, and the scalar DPP source cross section sigma=6.45e-34*(1-16*m_e^2/s)^6 above 2->4 threshold, zero below threshold (units in code). Actual installed default table files and compiled binary were not inspected.

## Exact positive physical 2->4 input but impossible proxy energy

Set c=1, m_e=1 for the four-vector witness. Head-on incident photons k1=(3,0,0,+3), k2=(2,0,0,-2) have total P=(5,0,0,1), s=P^2=24>16. A complete **on-shell** four-lepton final state is:

p1=(5/4,+sqrt(1/2),0,1/4);
p2=(5/4,-sqrt(1/2),0,1/4);
p3=(5/4,0,+sqrt(1/2),1/4);
p4=(5/4,0,-sqrt(1/2),1/4).

Charges can be e-,e+,e-,e+. Every individual p_i^2=25/16-1/2-1/16=1; sum_i p_i=P exactly. These exact phase-space points are not asserted to have any particular QED matrix-element weights.

When the 3m incoming photon is the primary in the CRPropa approximation, it assigns each of its TWO represented hard leptons energy Ee=(3-2)/2=1/2<m_e. Thus physical threshold s>=16 does **not** imply the surrogate's output per-lepton energy is on shell. Another input k1=(1,0,0,1), k2=(5,0,0,-5) has s=20>16 but proxy Ee=-1/2, a negative energy. This is a *static formula/call-path witness*, not proof of native runtime acceptance or propagation.

For the local two-hard-lepton formula to yield Ee>=m_e (units m_e=1), an exact **necessary** condition is E_primary>=4m_e. It is NOT sufficient for full 4-momentum conservation, accurate QED angular/spectral distribution, soft-pair tracking, EM deposition, or any astrophysical claim.

## Distinguish default cold backgrounds from custom hot tables

The checked generator starts its primary-energy table at 1 GeV (or higher if E>Emin filters it), far above 4m_e=2.0439958 MeV. The present witness does **not** establish that stock cold CMB/EBL tables have positive low-energy rates or give erroneous secondaries in their standard UHE use. Their actual installed rate rows were not fetched. In particular, negative-energy values would require below-valid-domain use plus a positive event hazard; do not claim a universal default CRPropa bug.

But if a **custom hot photon-field rate table** or user-supplied InteractionRates has E0=1 GeV, first rate R0>0, and is evaluated below E0, the verified interpolate source returns R0. A physically possible DPP event at E_primary=3m_e then can reach an invalid proxy sub-rest-mass input, provided the event fires and haveElectrons is true. A genuine physical rate should instead depend on input energy and bath distribution; a below-table constant rate is not a justified extrapolation. Native C++ behavior of addSecondary was not run.

## Fixed hot Planck bath quantitative check (not native CRPropa)

Use T_gamma=0.07818527068831995 MeV from DAX-S7 R68 and m_ec^2=0.51099895 MeV. Apply ONLY the published scalar CRPropa DPP cross-section surrogate sigma(s)=sigma0*(1-16m_e^2/s)^6 for s>=16m_e^2; no differential QED. With q=E_primary/(m_ec^2), chi=4m_ec^2/(q*T_gamma), the angle- and Planck-averaged hazard normalized by its ideal high-energy limit is

F(q) = [1/(2*zeta(3))] * integral_{chi}^infinity x^2/(exp(x)-1) * A(chi/x) dx,

where A(a)=2*integral_a^1 u*(1-a/u)^6 du for 0<a<1, zero for a>=1. Isotropic relative-flux (1-cos theta) is included. The common sigma0 and total thermal photon density cancel.

Source-typed numerical results at fixed bath:
q=1: 7.2353459e-17;
q=2: 4.8780917e-10;
q=3: 1.4976437e-7;
q=4: 3.1952164e-6;
q=6: 8.5783600e-5;
q=10: 0.00160164145;
q=20: 0.02064775584;
q=100: 0.3130461187;
E_primary=1 GeV (q about 1956.951): 0.9102940259.

So F(1 GeV)/F(3m_e)=6,078,174.98 for that mathematical scalar-rate model. IF a positive 1-GeV-first custom rate table for the specified hot field is clamped at 3m_e, it overstates this model's rate by that ratio. This is **conditional**, not an empirical bound or a finding on installed CRPropa tables. At q=3 the true scalar-model hazard is nonzero (hot Planck tail) but tiny; this does not make a quantitative PBH claim.

Reproduction: independent 8192/16384-panel stdlib Simpson quadratures of the above 1D integral, plus a separate SciPy adaptive quadrature. Across nine q values, Simpson self-convergence max relative difference <7e-7 and independent SciPy relative discrepancy <8.19e-7. The exact four-vector witness and interpolation clamp tests were checked with Python fractions. The complete original local report, full stdlib reproducer, JSON, SciPy independent-control JSON, manifest and ZIP are available within the originating ROT005 conversation. Do not confuse repeatability of scalar model with source QED validity.

## Typed result, self-falsification and STOP

FALSE GENERICALLY: 2->4 physical production threshold automatically guarantees on-shell CRPropa two-hard-lepton proxy for every incident-photon assignment. The k1=3m,k2=2m input falsifies this exactly.

TRUE UNDER X: local necessary surrogate energy guard E_primary>=4m_e; positive below-table clamp is exactly the source interpolation behavior; if a custom rate table R0>0 below its first E0, the source lookup returns R0. No claim that the local guard suffices for physical four-lepton transport.

DEFAULT CMB/EBL BUG: UNDETERMINED / NOT ESTABLISHED.
HOT-BATH CUSTOM-RATE PHYSICAL DEPOSITION: OPEN.
FULL QED FOUR-LEPTON DIFFERENTIAL: OPEN.
NATIVE C++ EXECUTION: NOT RUN.
BW private receipt/ingestion: PENDING, no invented ING or owner approval.

No new physics, no automatic code patch, no audit cascade, no claim promotion. STABLE_STOP / NO_AUTO_R69 / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.
