---
artifact_id: IW_M16_ROT016_BLACKHAWK_V23_100TEV_TERMINAL_CLOCK_AND_FUBINI_THERMAL_MASS_INTEGRAL_SOURCE_AUDIT_001_20261123
date: 2026-11-23 Europe/Warsaw
cell: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_11 / M16
authorization: Moderator "Sam prowadź prace zamiast czekać na badacza"
class: ORIGINAL_SOURCE_MASS_CLOCK_AND_EXPLICITLY_IDEAL_THERMAL_TWO_INTEGRATION_ORDER_NUMERIC_STRESS
status: BLACKHAWK_V23_FULL_1000_ROW_A0_SOURCE_READ / WUXU_PRIMARY_ENDPOINT_SOURCE_READ / INDEPENDENT_PYTHON_TWO_ISOLATED_RUNS_BYTE_IDENTICAL / MODEL_ONLY
claim_ceiling: NOT_ACTUAL_BLACKHAWK_GREYBODY / NOT_ACTUAL_HADRONS / NOT_G_DEP_DEPOSITION / NO_NATIVE_BBN / NO_PHYSICAL_BETA_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_NOT_WRITTEN
---

# M16 ROT016: BlackHawk source mass clock versus fixed 100TeV Wu-Xu primary generator endpoint

## Original sources and strict firstness

**PRIORITY:** Mech-S8 ROT015 (11 Nov) first ideal massless Bose/Fermi pointwise E>100TeV tail and PRIMARY-not-secondary original Wu-Xu endpoint; Mech-S10 ROT020 (22 Nov) first actual PRIMARY 100x100x16 BlackHawk sampled source mass-integral for missing upper energy and conditional mass interpolation; REC14 ROT009 (23 Nov) first full-mass j22/j62 G_PG2 mass coverage; DAX-S10 ROT007 first independent full original v2.3 fM byte-identity mirror, DAX ROT009 first source 16-channel graviton deposition guard; BADACZ REVIEW122 first native secondary hadron energy G_EC+(b) result. M16 does NOT claim these as first discovery. Distinct M16 target is total-mass integral of an EXPLICIT IDEAL thermal control (not true greybody) with two independent integration methods and the real BlackHawk source terminal time after TH=100TeV.

Original Wu-Xu author commit d395183674cace6c9906a8911bdeb7234ba4040d, full producer notebook Git blob 8a10396ae771b17059808fc2b91235dd194cba8d, direct source read: cells8/9/12/13 BlackHawk BBN PYTHIA choice0, PRIMARY energy grid E∈[5,100000] GeV, 100 energies; 100 masses from 1e9 to4e12g and five INTEGRATED HADRON NUMBER rates, no individual final-hadron energy spectra in resulting five-rate table.
https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/valid_hadrons_from_BlackHawk.ipynb
Original author wrapper tool_script-BlackHawk_extension.jl blob 16c5cb6f87dcd2e2b416b6664d3bdcb3c3c68818 calls Emax primary, not a final hadron kinetic ceiling. Original author tool_script-parameters.jl blob0d7198ff3557bdbd5753000bb07a7a7405cc24f5 defines TH=M_Pl²/M and N_BH code mass rate. Original author main-scan.jl blobb368ba55d5a493f7bc185909730f7fe5691f10d6 has stop mass Mstop=M0exp(-20) in j22/j62. Code plateau fcode=1.6295583423315782e74GeV4 source I1 first M16 ROT011.

Full historical BlackHawk v2.3 fM ORIGINAL mirror bytes independently DIRECT READ by M16 from external source cewasiuk/Spin-and-Charge-BH-Evolution@0bd531eb948bd11549535a563b55f0d23671589b, path src/tables/fM_tables/Standard_tables/fM.txt Git blob 98f1f6afbffc39f7eca84c8365d78a7c7c85aed7: complete 767767 bytes, 1000 mass rows x 50 spin cols plus mass column, a*=0 original fBH=9.47999e73GeV4 CONSTANT in both original Mstop..M0 domains. Earlier DAX-S10 proved this mirror file SHA256 5baaac375e5848584ec6cc852aeacc28edc4de3528c796f6aee1dd460ad943cc matches owner genuine v2.3 native fM source: firstness DAX.
https://github.com/cewasiuk/Spin-and-Charge-BH-Evolution/blob/0bd531eb948bd11549535a563b55f0d23671589b/src/tables/fM_tables/Standard_tables/fM.txt
Author original native starting masses from independently REOPENED REC14 ROT009 source report blob b5e4d28c0fb4b249f482f6e0dad5a343335af38a: j22 M0=1121174456.4709601g, j62 M0=3494213660.2848945g, stops 2.3109127923407g and 7.2021111434705g. Do not conflate original fM clock calculation with re-running native Julia or BlackHawk spectral production.

## Source mass/time exact identities

Hawking k_B TH(M)=hbar*c^3/(8pi*G*M). CODATA T_H at M=1e9g = 10572.611958GeV. At fixed author input Emax=100000GeV, source crossover k_B TH=Emax occurs when M*=105726119.58058049g.

Total energy emitted in monotone mass interval (Mlow,Mhigh) is (Mhigh-Mlow)c², independent of mass-loss speed and particle channel. After crossover M* to original Mstop, the total mass-energy emitted equals 9.4299435% original M0 for j22 and 3.0257484% for j62. THIS IS NOT fraction in E_primary>Emax.

Original a*=0 source fBH mass clock yields remaining lifetime from M* down to stops 0.000482810324s=0.482810324ms for BOTH PBHs; Wu-Xu code GO fcode yields 0.000280875924s=0.280875924ms. Full lifetimes from M0 to stops: source BlackHawk j22 0.5757702935s, j62 17.429223596s; GO code j22 0.3349555817s, j62 10.139487559s. Source original full 1000-row fM piecewise log-rate integration conducted in connected JS (0.575770293476 and 17.42922359423s) cross-checked with independently executed Python constant-source-plateau integral. No physical Yp/beta effect inferred.

Original hadron table below 1e9g share initial emitted mass-energy 89.1921854% j22 and 28.6187421% j62 — first REC14; M16 independently checks. Fraction of GO code lifetime spent below original hadron mass-grid floor: 70.9545771% j22, only 2.3439677% j62. The contrast reveals temporal concentration; it does not validate subgrid q_h source.

## EXPLICIT IDEAL massless Bose/Fermi whole-trajectory CONTROL ONLY

wB(x)=x^3/[(exp(x)-1)*(pi^4/15)], wF(x)=x^3/[(exp(x)+1)*(7*pi^4/120)], x=E/(k_B TH), no greybody and no spin-dependent thresholds or primary species composition. Define S_eta(x)=integral_x^infty w_eta(y)dy. For total PBH mass decrease, R_eta=1/(M0-Mstop)*integral_Mstop^M0 S_eta(Emax/(kB TH(M))) dM.

Fubini exact standard identity: let A_eta=pi^4/15 for B, 7pi^4/120 for F. Define J_eta(x)=[integral_0^x y^4/(exp(y)±1)dy + x*integral_x^infty y^3/(exp(y)±1)dy]/A_eta. Then R_eta=[J_eta(x0)-J_eta(xstop)]/(x0-xstop), x=a*M. Different independently executed integration orders: direct 80-node Gauss-Legendre on full finite Mstop..M0 and QUADPACK exact energy-tail at each point, versus Fubini-reordered QUADPACK y^3/y^4 integrals. Four original j22/j62 Bose/Fermi results agree max abs 1.1102230246251565e-16.

RESULTS, EACH IS MODEL-ONLY, NEVER ACTUAL BLACKHAWK SPECTRAL FRACTION:
- j22: ideal Bose 36.0627130%, Fermi 38.6332651% of total emitted initial rest-mass energy as primary E>100TeV; of that modelled high-E fraction 99.7123944% Bose and 99.6931912% Fermi occurs at M<1e9g outside author original FIVE-RATE generator mass grid.
- j62: ideal Bose 11.5953627%, Fermi 12.4236029%; 99.5054654% Bose and 99.4725116% Fermi of the MODELLED high-E fraction occurs at M<1e9g.
- Fixed-point ideal Bose/Fermi tails at kB TH=Emax: 96.5382%/98.6315%, previously Mech-S8 first. These B/F models are alternative physical toy curves, NOT confidence bounds or rigorous lower/upper physical greybody envelope.

Real full spin-dependent BlackHawk primary spectra may depart materially; temperature-dependent SM degrees of freedom, hadronization, Eprimary→Esecondary cascade, neutrino decoupling and G_DEP thermal deposited-sector fractions are omitted. In particular the 36–39% figure is NOT "missing energy" in actual Wu-Xu computation, NOT an error bar, NOT percent extra hadrons, NOT a physical beta change. Data below original mass 1e9g must be generated to adjudicate actual effects. Prior Mech-S10 full real spectra mass support firstness retained.

## Reproduction and independent exact custody

Original isolated CPython3 NumPy/SciPy code locally ACTUALLY executed TWO times as python -I. Repeated stdout bytes identical and equal numeric JSON. Original standalone Python SHA256 5eb55259fa752674c280cd40c3ee7f1efd7cd8086872e5cd694bef5bfe4f4354 (6982 bytes); original JSON SHA256 1476393aae9cd48d31a9130464449163ee10cf027c2df566fcc43225cd9105b3 (5420 bytes). Packaged full standalone report+script+JSON+2 replays+README+SHA manifest in 16909-byte ZIP, SHA256 34b0504ca507d08e27571a150e8a7eb6fa2f32ccf4024647c903e8d5fffb0574, ZIP CRC and full 6/6 SHA manifest readback PASS. ZIP belongs to this conversation container path /mnt/data/m16_rot016/m16_rot016_repro_bundle.zip, NOT falsely claimed uploaded to GitHub. Full original fM 767767-byte table read by connected GitHub but not included in ZIP; Python reproducer evaluates its directly confirmed mass plateau and physical source constants.

STRICT: REAL SOURCE TIME/MASS IDENTITIES PASS; MASSLESS IDEAL THERMAL TWO_ORDER MODEL INTEGRATION PASS; REAL BLACKHAWK SPECTRAL FRACTION UNKNOWN; PHYSICAL_HADRON_BBN_G_EC_PLUS_B_PARTIAL; G_DEP OPEN; NO_NATIVE_JULIA; NO_NEW_PBH_BOUND; NO_AUTHOR_ERROR; NO_NOVELTY; NO_CANON; NO_EXEC_SIGN; NO_BW_NATIVE_WRITE.
