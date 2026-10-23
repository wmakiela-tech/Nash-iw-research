# MECH-S7 ROT010 — two-temperature post-evaporation thermal host versus archived Wu–Xu 7D

```yaml
CELL: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
DATE: 2026-10-23
RETURN_ID: MECH-S7-FRONTB-IDEAL-TWO-TEMPERATURE-POSTSOURCE-THERMAL-HOST-010
PROBLEM_ID: P1-FRONTB-WUXU-2X2-SOURCE-MAP-ATTRIBUTION-001
TYPE: EXECUTED_CONDITIONAL_7D_POSTSOURCE_EOS_SWAP / ENERGY_ENTROPY_DOUBLE_CHECK / 2x2_BACKGROUND_BARYON_FACTORIAL
SOURCE: Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d
NO_SOURCE_VALID_E2B: true
NO_ORIGINAL_10D_JULIA_EXECUTION: true
NO_HELIUM_DEUTERIUM_ENDPOINT: true
NO_PBH_BOUND: true
NO_CANON: true
NO_EXEC_SIGN: true
NO_NOVELTY: true
BW_INGEST: UNVERIFIED
```

## 1. Scientific question and attribution

Do the opposite signed paper-minus-public hadron source-law contrasts in an independent conditional Wu–Xu 7D terminal-replay model survive a physically typed alternative post-evaporation thermal clock and a baryon-conservation control? The original archived `public_exec` source temperature history, four reduced 2×2 cells, and last saved source-active state remain the same as Mech ROT006–009. **Only the time–temperature–baryon post-evaporation host changes**. This is NOT a source-native full Julia PBH/BBN rerun, NOR a source-valid extension of hadron spectra below 10^9 g.

**Others first:** DAX-S7 ROT34–39 independently identified and tested the cooling discrepancy; PRF11 R21 independently integrated the author table and PRF11 R22 independently reconstructed a two-temperature photon/electron/neutrino ideal micro host. Mech-S7 does not claim their thermal discovery. The present distinct result is the dynamical response of the previously executed 7D terminal hadron/neutron model under that host, with a direct energy–entropy consistency check. LT5/MT13 have separate exact event-clock/factorial analytic hosts. REC10 independently established hadron memory after PBH emission stops.

Primary author/source: Wu–Xu *Primordial black holes evaporating before Big Bang nucleosynthesis* (JCAP02(2026)063), GitHub pinned source commit above `arXiv-2509.05618/main-scan.jl`, `tool_script-parameters.jl`, `tool_script-N_relativistic_species.jl` and archived `hadrons_from_PBH.dat`.

## 2. The executed thermodynamic comparator (defined host)

After the PBH mass reaches source cutoff, anchor T_cut to the SAME PCHIP interpolation of archived public_exec T(t), at the SAME exact mass-law cutoff time t_cut=51.33592433955715 s and T_cut=0.14335503280771247 MeV. Four 7D cell states X and six population densities at t_cut come from the existing exact-M^3 Radau source-active conditional solver, including retained hadrons. They are kept *fixed* across every postsource thermal-host comparison. Earlier sources and populations are NOT reconstituted under an alternative background.

The ideal comparator separately conserves photon+thermal e± entropy and free-streaming massless neutrino entropy, assuming instantaneous ultrarelativistic decoupling. With g_s,em(T) from exact numerical Fermi–Dirac momentum integrals (electrons/positrons g=4, m_e=0.51099895 MeV), photons g=2, and 3 relativistic neutrino flavors g_rho,nu=5.25, define

`(T_nu/T_gamma)^3 = g_s,em(T_gamma)/5.5`.

`rho_total(T) = rho_gamma(T)+rho_e(T)+rho_nu(T)`;
`P_total(T) = rho_gamma/3+P_e(T)+rho_nu/3`, so `w=P_total/rho_total` is defined from pressure, NOT the invalid single-temperature `4*g_s/(3*g_rho)-1`.

`H(T) = [8*pi*G*rho_total(T)/3]^(1/2)` equivalently `1.66053906660*sqrt(g_rho(T))*(T/GeV)^2/M_Pl` with physical seconds restored.

`dln(a)/dln(T_gamma) = -(3+s_em)/3`, `s_em=dln(g_s,em)/dln(T_gamma)`;
therefore `dt/dln(T_cut/T) = (3+s_em)/(3H)`.

Independent energy–pressure route: `dt/dln(T_cut/T) = (4+r_rho)/[3H(1+w)]`, `r_rho=dln(g_rho)/dln(T_gamma)`. This identity is NOT assumed; it is verified independently using numerical derivatives of the direct integral EOS.

Baryon-control alternatives: `n_B(T) = eta_B*n_gamma(T)`, as in the source, versus source-cutoff-normalized *conserved comoving baryons* `n_B(T)/n_B(T_cut)=[g_s,em(T)/g_s,em(T_cut)]*[T/T_cut]^3`. The latter does NOT retroactively correct baryon evolution in the earlier source-active phase.

## 3. Computed results

At `T_nuc=0.07818527068831995 MeV`, with 2 source laws ×2 charge maps:

| Postsource T(t) | Postsource baryon rule | t_nuc [s] | paper−public ΔX, B_exec | paper−public ΔX, B_sym |
|---|---|---:|---:|---:|
| Archived PCHIP | constant eta_B | 215.17238636 | −6.871605603420e−6 | +2.245563145625e−5 |
| Archived PCHIP | comoving baryons | 215.17238636 | −6.871724475332e−6 | +2.245562816761e−5 |
| Ideal two-temperature radiation host | constant eta_B | 209.94902569 | −6.921918448588e−6 | +2.261992695413e−5 |
| Ideal two-temperature radiation host | comoving baryons | 209.94902569 | −6.921918704550e−6 | +2.261992680713e−5 |

At nominal constant-eta and archived background `X_public(T_nuc)` =0.397801321 (exec), 0.396614046 (sym); on ideal two-temperature EOS with conserved comoving baryons 0.400712213 (exec), 0.399516250 (sym). Absolute X shifts about +0.00291/+0.00290; **absolute target is far more temperature-host dependent than the paper−public differential**.

Factorial thermal/baryon decomposition of ΔX:

| Contribution | B_exec | B_sym |
|---|---:|---:|
| Reference archived T(t), constant eta | −6.871605603420e−6 | +2.245563145625e−5 |
| Two-temperature thermal correction at constant eta | −5.031284516788e−8 | +1.642954978731e−7 |
| Baryon conservation at archived T(t) | −1.188719123135e−10 | −3.288647132393e−12 |
| Thermal×baryon interaction | +1.186159503952e−10 | +3.141653603933e−12 |

The baryon postsource change is numerically tiny because the hadron populations deplete rapidly after emission stops and the later neutron weak dynamics is independent of nB. It does **not** validate the earlier baryon prescription during PBH injection; PRF11 R21's cumulative baryon-proxy difference belongs to a different, longer thermal window.

The identity `g_s,em(T_nuc)/g_s,em(T_cut)=0.69457323675` shows that constant eta and comoving baryon prescriptions differ by about 30.5% in late **baryon normalization**, despite tiny paper−public X contrast response to *postsource-only* substitution. This is not baryon creation or destruction.

## 4. Independent numerical controls and EOS data

Direct exact ideal Fermi–Dirac integrals at T_cut: `g_s,em=3.1241631314850857`, `g_rho,total=5.736427382840326`, `w=0.3002096741378892`, `T_nu/T_gamma=0.8281779648651806`.

At T=0.1 MeV: `g_s,em=2.44546457236247`, `g_rho,total=4.300514406125044`, `w=0.31057873981046064`, `T_nu/T_gamma=0.7632489731461765`. PRF11 R22 author-table two-temperature inference at 0.1 MeV is ≈0.7634424; close but **not identical**, because the ideal instantaneous-decoupling EOS is a separate comparator, not an exact reconstruction of Wu–Xu's tabulated evolution.

At T_nuc: `g_s,em=2.169960098370164`, `g_rho,total=3.7213851527723474`, `w=0.321782959071324`, `T_nu/T_gamma=0.7334373450264859`.

EOS refinement 300/80 → 2400/160 (temperature knots/Gauss–Legendre nodes) gives micro elapsed time 158.6131016674 → 158.6131013518 s (grid uncertainty in last ~3e−7s); default 1200/120 gives 158.6131013538 s. **Independent pressure-energy vs photon/e entropy cooling integral** on a separate 2801-point grid and 180-point Gauss quadrature: durations 158.6131025230 s versus 158.6131025366 s, discrepancy 1.36386404e−8 s; max interior local relative rate residual 6.63e−10. This checks internally legal two-temperature energy/pressure, not the source's own code thermodynamics.

The model's 7D Radau terminal-state replay remains conditional and no certified uniform global endpoint X uncertainty is supplied. The former MT13 sufficient four-cell original-executor endpoint error ε_X<6.33356560558e−6 is NOT proved by the small changes shown here.

## 5. Scientific impact, falsifiers and STOP

**Mechanistic update:** Within the restricted postsource alteration, the source-law opposite signs stay. Merely changing late cooling from the archived history to a self-consistent ideal radiation two-temperature host does NOT reverse either conditional 7D sign. But it changes absolute X far more than the differential. Postsource comoving-baryon conservation likewise does not account for the source-law sign.

**Do not extrapolate:** The test does not repair earlier T(t), H(t), PBH heating, baryon normalization in active source, neutrino transport, below-table emission or initial populations. It cannot validate a real PBH-affected thermal history. The exact event T_nuc is model-defined; never convert the source code's `2X/(1−X)` proxy into physical helium. DAX-S7, PRF11, LT5 maintain source/observable currentness. There is no adjudicated E2b, D/H, Yp, published Figure 5 or cosmological PBH constraint.

**Next cheapest material test:** source-native 10D Julia accepted-step 2×2 with shared background and corrected mass cube, and a nontrivial *pre-source-off* radiation/baryon EOS variant. Evaluate same fixed-T neutron endpoint with an explicit 10D tolerance ladder. An even earlier source validation of pbar/nbar spectra for M in [1e8,1e9]g and absolute helium observable genealogy is required before interpreting physical constraints.

`ROT010 = EXECUTED_CONDITIONAL_7D / EOS_CROSSCHECK_PASS / SOURCE_PHYSICS_HOLD / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY`.

## 6. Provenance and reproduction

- Prior frozen 7D baseline source: `research/mech-s7/2026-10-23/terminal_7d_exact_mass_common_background_006.py` and ROT008–009; locally included in ZIP with both archived original Mech-S6 2×2 Actions ZIPs (`SHA256=75766c...` public; `3b24f...` paper).
- Executed standalone continuation: `reproduce_mech_s7_thermal_eos_event_010.py` (imports pinned ROT009 7D kinetics, SHA-pinned original archives). The equation-of-state implementation and numerical controls are complete in this script.
- Independently executed temperature-integrity source: `validate_micro_eos_010.py`.
- Outputs: `thermal_eos_2x2_010.csv`, `thermal_eos_factored_010.csv`, `thermal_eos_010.json`, `pressure_entropy_integrity_010.json` and readable run stdout in local ZIP.
- External typed currentness: [PRF11 R21](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/prf11_r21_integrated_thermal_table_cooling_001.md), [PRF11 R22](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/prf11_r22_wuxu_two_temperature_eos_pressure_reconstruction_001.md); DAX-S7 is priority owner for original cooling discrepancy.