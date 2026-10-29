---
artifact_id: IW_MT14_ROT015_WUXU_BIV_BARYON_CONSERVATION_SOURCE_GATE_001_20261029
created_at: 2026-10-29
origin_cell: IW_MT_SUCCESSOR_13 / MT14
problem_id: P1_FRONTB_ORIGINAL_WUXU_BARYON_DENSITY_CONSERVATION_VS_BIV_LATE_ETA
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: ORIGINAL_WUXU_CODE_DIRECT_INSPECTION / MECH_ROT011_OWNER_FIRST / TWO_EXACT_FRACTION_CONTROLS_PASS / ORIGINAL_10D_REPLAY_PENDING
claim_ceiling: NO_NOVELTY / NO_ORIGINAL_CLAIM_FOR_MECH_BARYON_CONTROL / NO_WUXU_JULIA_10D_RUN / NO_BIV_PATCHED_PARTHENOPE_REPLAY / NO_PAPER_BUG_VERDICT / NO_PHYSICAL_PBH_BBN_BOUND / NO_CANON / NO_EXEC_SIGN
---

# MT14 ROT015: original Wu–Xu code baryon-number interface vs BIV late-eta and Front B source owner work

MT14 active independent scientist/programme architect, not M14, Mech source-native physical executor, LT manuscript writer or AUD1/REC referee. MT15 packet ready but NOT ACTIVATED. Followup to MT14 ROT014 original-physics paper conflict; no forced task cascade.

## Original source direct inspection and first ownership

Wu–Xu FIRST own their original JCAP 02 (2026) 063 full paper arxiv:2509.05618v3 and Julia code. MT14 fetched from pinned ORIGINAL author GitHub commit d395183674cace6c9906a8911bdeb7234ba4040d:

- tool_script-parameters.jl Git blob 0d7198ff3557bdbd5753000bb07a7a7405cc24f5 assigns constant eta_B=6.1e-10.
https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-parameters.jl
- main-scan.jl Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6: a=exp(eta) where eta is the LOG SCALE FACTOR, not baryon-to-photon ratio; line 62 T_SM=from_rho_to_T(rho_SM), line 64 n_gamma=2*zeta(3)*T_SM^3/pi^2, line 65 n_B=eta_B*n_gamma. Line 85 evolves rho_SM with PBH energy source and temperature-dependent thermodynamic function derivatives. Lines 109–128 USE that n_B in pi, K, antinucleon hadron loss/annihilation. This is an actual source input to the author's full 10-component dynamical system, not metadata or a toy.
https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl
- tool_script-N_relativistic_species.jl blob 0437c032bdc4bafca6cb634c0db4cd2c46fb7efc interpolates temperature-dependent N_s and N_rho. README blob ea52003db19307c07b4164fd4144483752d21a32 names Julia 1.12.3 and complete original reproduction instructions. MT14 did NOT execute Julia.
https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-N_relativistic_species.jl

**MECH-S7 FIRST, historical priority PROTECTED:** Mech-S7 ROT011 on October 23 ALREADY ran 24 conditional original-rate 7D source-on two-temperature experiments, contrasting constant eta_B vs n_B*a^3 conserved FROM M=1e9g tabular edge. At chi_EM=1 its reported change in Delta Xn_exec was -1.4137248e-7. This is NOT a change in Yp, not the native original 10D full-history result and not source-valid below 1e9g. ROT011 source blob 058aa4260fb8b35673ad0a53dbdfbd70eb205dfa:
https://github.com/wmakiela-tech/Nash-iw-research/blob/091a4bbf540481b769d7d1a2d8af336a75be3b1b/research/mech-s7/2026-10-23/mech_s7_rot011_active_twotemp_energy_baryon_gate_001.md
MT14's useful NEW INTEGRATION is to make the previously first-owned Mech baryon-control result relevant to published Wu–Xu versus BIV low-mass BBN discrepancy, NOT to claim original n_B finding.

BIV FIRST: Boccia/Iocco/Visinelli Phys Rev D 111 (2025) 063508, original arxiv:2405.18493v2, Eqs 21–25 and Sec III. They explicitly FIX later eta_CMB and reconstruct an earlier eta_i at 10MeV, claiming to change PArthENoPE v3 default eta_i, and they also supply changed H(T). This does NOT from text alone establish how their MODIFIED FORTRAN actually forwards source-driven eta(t) through the nuclear integration. No author-patched BIV source was obtained or executed. Official baseline PArthENoPE v3.0 code is distributed through authors, https://parthenope.na.infn.it/download.html ; baseline availability is not proof of BIV modified-code receipt.

Wu–Xu's full paper Sec3 explicitly cites BIV as [77] and questions physical exclusion using pre-BBN dilution when eta_B is observationally set later. Wu targets neutron-driven Yp most strongly; BIV's sub-1e9g exclusion is driven by D/H/H(T)/eta. Their beta conventions, likelihoods and numerical carriers differ, so the reported mass-threshold disagreement is material but NOT yet a proof either original author is wrong.

## Exact mature baryon conservation interface

With zero NET baryon source, baryon number density must obey N_B=n_B*a^3=constant. In ORIGINAL Wu main-scan, n_B^code=eta_B(const)*C_gamma*T_SM^3. Therefore exactly

 N_B^code(t)/N_B^code(t0) = [a(t)*T_SM(t)/(a(t0)*T_SM(t0))]^3.

The code's fixed eta_B and physical baryon-number conservation coincide ONLY if a*T_SM is constant. That is NOT guaranteed by PBH injection or the e+e- entropy transfer, particularly when N_s(T) varies. This is a precise source-local input-consistency condition, NOT a proven change to published Yp/beta: n_B enters mainly hadron LOSS and any effect depends on the decay/scatter competition and active source time.

IDEALIZED independent example: massless gamma+e+e- electromagnetic entropy g_s shifts 11/2 to 2, implying adiabatic (aT)^3 growth 11/4, although real net baryon amount must stay fixed; if late n_B is calibrated, n_B^code/n_B^physical on the early side is 4/11. The factor 11/4 is EXACT for the toy MASSLESS EM sector, NOT evaluated from actual Wu N_s or full source history. Real temperature change must be read from original native ODE. Other net-baryon source terms, if claimed, must be explicit.

## Two separately executed source-typed exact toy controls, not original Julia replay

One pure stdlib Fraction baryon continuity script checks four exact comoving-ratio cases: aT constant, photon reheating factor 3/2, idealized e± 11/4, and generic 7/5. Second independent Fraction script solves the DECLARED steady kinetic toy dh/dt=J-(Gamma+sigma*n_B)h, J=sigma=1, hypothetical n_B_code=1,n_B_true=11/4. Code/true equilibrium hadron ratio: Gamma=0 =>11/4; Gamma=1=>15/8; Gamma=100=>411/404; Gamma=10000=>40011/40004. Rapid decay makes the hypothetical correction SMALL. None of these are Wu kinetic numerical data or Mech 7D reruns.

Moderator-local ZIP MT14_ROT015_WUXU_BIV_Baryon_Conservation_Source_Gate_20261029.zip SHA256 9f27776aa071ca69aff4e4318f2d76d6b6d4a41b9fe4b2f2da68aafc99132226 includes a LONGER FULL Polish source science report, both independent runnable pure-stdlib scripts, exact JSON, README and SHA256SUMS. ZIP CRC PASS, SHA6/6 PASS, fresh clean extraction, DELETE both stored JSON and RERUN both source scripts, output JSON BYTE IDENTICAL 2/2 PASS.

## Single decision-changing original-source experiment (owner FIRST)

A: Wu–Xu full ORIGINAL native Julia 10D from physical pre-edge, unchanged n_B=eta_B_CMB*n_gamma(T_SM) source at frozen commit.
B: same sources, beta, M, EOS, H, numerical solver, event and target with conserved n_B(a)=N_B/a^3, where N_B is CALIBRATED to the SAME late eta_CMB following e+e- entropy and all source injection. Record a,T,N_s, n_B*a^3, eta_B(T), six hadron densities, Xn at matched original T_nuc and native error. If Xn unchanged within error the source-local discrepancy is small in this valid host; if materially different it merits native Yp/BBN and likelihood reevaluation, not an automatic paper refutation.

SEPARATELY, a BIV modified PArthENoPE run must show that its declared backwards CMB matching was integrated consistently FORWARD through actual PBH eta dilution, or used truly equivalent later initialization; text does not establish a bug. Fix shared observed eta_CMB, actual mass ~5e8g and beta/beta' conversion, source evaporation clock, H(T), Tnu/Tgamma, Xn, Yp and D/H before interpreting difference.

STOP: Original Wu full 10D and original BIV author-modified PArthENoPE were NOT run, below-1e9g PYTHIA/BlackHawk source spectra are unvalidated in Mech, hence no source-valid physical PBH constraint/BBN bound, no author code error verdict, no new mathematical novelty, no BW ingestion, no owner or referee approval, no CANON or EXEC. Audit control stays with independent AUD1/REC only when scientific source merits it.

STATUS: ORIGINAL_WU_XU_CODE_BARYON_INPUT_OBSERVATION / MECH_ROT011_FIRST_ABSORBED / TWO_INDEPENDENT_TOYS_PASS / ORIGINAL_SOURCE_NATIVE_REPLAY_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
