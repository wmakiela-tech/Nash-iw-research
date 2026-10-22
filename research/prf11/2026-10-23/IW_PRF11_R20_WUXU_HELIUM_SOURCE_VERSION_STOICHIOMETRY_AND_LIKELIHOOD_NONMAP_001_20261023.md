---
artifact_id: IW_PRF11_R20_WUXU_HELIUM_SOURCE_VERSION_STOICHIOMETRY_AND_LIKELIHOOD_NONMAP_001_20261023
created_at: 2026-10-23
as_of: 2026-10-23
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
document_type: REPORT
function: FOUNDATION_FIRST / OTHERS_FIRST / SOURCE_VERSION_RECONCILIATION / PRIOR_ART_SUBTRACTION
exposure: PUBLIC_SAFE
status: EXACT_SOURCE_VERSION_TRIANGULATION / STOICHIOMETRIC_HOST / INDEPENDENT_REFEREE_PENDING
problem_id: FRONTB_WUXU_HELIUM_OBSERVABLE_SOURCE_VERSION_001
primary_location: GitHub research/prf11/2026-10-23/IW_PRF11_R20_WUXU_HELIUM_SOURCE_VERSION_STOICHIOMETRY_AND_LIKELIHOOD_NONMAP_001_20261023.md
derived_from:
  - DAX-S7 rotations 29–33, 2026-10-23
  - MECH-S7 rotation 004, 2026-10-23
  - MT13 exact four-cell dynamic-interaction ledger, 2026-10-23
acceptance_owner: MECH-S7 executor; DAX-S7 provenance; LT5 manuscript; SW/REC10 review; Moderator EXEC
claim_ceiling: NO_NEW_PBH_BOUND / NO_CANON / NO_EXEC / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE
cross_surface_sync: GITHUB_PENDING_BW_INGEST
---

# PRF11 R20 — Wu–Xu: paper formula corrected in May 2026 but public code not updated

## 0. Others first and scientific question coevolution

DAX-S7 R29–R33 ALREADY established that the authors' published JCAP equation, public code and standard BBN mass fraction use three incompatible formulas. DAX ALREADY derived code-to-standard remapping and 3-sigma disjoint intervals; it also located the historical v1 SBBN baseline. CREDIT DAX, NOT PRF11.
Sources:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/dax-s7/2026-10-23/IW_DAX_S7_ROTATION_29_WUXU_HELIUM_OBSERVABLE_AUDIT_20261023.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/dax-s7/2026-10-23/IW_DAX_S7_ROTATION_30_HELIUM_CHISQUARE_REMAP_20261023.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/dax-s7/2026-10-23/IW_DAX_S7_ROTATION_31_HELIUM_ACCEPTANCE_DISJOINTNESS_20261023.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/dax-s7/2026-10-23/IW_DAX_S7_ROTATION_32_PAPER_CODE_HELIUM_TRIANGULATION_20261023.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/dax-s7/2026-10-23/IW_DAX_S7_ROTATION_33_V1_SBBN_BASELINE_PROVENANCE_20261023.md

MECH-S7 ROT004 ALREADY found an exact mass-cube invariant of the pinned Wu–Xu source, a roughly 2.20–2.33% archived mass discrepancy, and an undersampled 0.237666s subedge time interval. MT13 ALREADY established that a 2x2 endpoint interaction and sign reversal can arise from ODE propagation with zero instantaneous mixed directional-rate interaction. Their problems are related evidence gates, but NOT this helium observable.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-23/mech_s7_frontb_exact_mass_cube_and_subedge_fluence_gate_004.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-23/mt13_frontb_exact_dynamic_factorial_interaction_ledger_001.md

R20 CHANGE OF QUESTION after reading mature source: Not "are authors' published and code formulas wrong?" (the original DAX result), but "**Was the journal formula subsequently corrected in a newer author version, and which experimental/observational quantity does each historical formula actually calculate?**"

## 1. Version-controlled SOURCE MATRIX: verified directly

A. AUTHOR PUBLISHED JOURNAL. Wu and Xu, Primordial black holes evaporating before Big Bang nucleosynthesis, JCAP02(2026)063, published **2026-02-17**, DOI 10.1088/1475-7516/2026/02/063. In the actual published PDF Eq(2.4), PDF page index 3, X_n=n_n/(n_n+n_p). Eq(5.1), PDF page index 13, states
   Y_p approximately 2 X_n/(1-2 X_n).
Text labels this the He4 mass fraction and compares to observed Y_p=0.245+-0.003 in Figure 5. It reports a parallel BBN-simple nuclear network comparison, not independently reproduced by PRF.
https://inspirehep.net/files/9adbfbb35c345cc510bed18e66a36b55
https://doi.org/10.1088/1475-7516/2026/02/063

B. AUTHOR ARXIV v2, arXiv:2509.05618v2, dated **2025-12-30**: Eq(5.1) uses the SAME 2X_n/(1-2X_n) formula as JCAP.
https://arxiv.org/pdf/2509.05618v2

C. AUTHOR ARXIV v3, arXiv:2509.05618v3, dated **2026-05-06**, posted AFTER the published journal version: Eq(5.1) NOW reads
   Y_p approximately 2 X_n(T_nuc),
no denominator. Authors' arXiv history explicitly says v3 and notes "a few typos in equations fixed". This is a VERIFIED AUTHOR TEXT CORRECTION. No separate publisher correction notice was established. The printed Feb2026 JCAP and the corrected May2026 author text are DIFFERENT historical records.
https://arxiv.org/abs/2509.05618
https://arxiv.org/pdf/2509.05618

D. AUTHOR PUBLIC SOURCE REPOSITORY. GitHub default branch is actually MASTER, NOT main. Its inspected HEAD/last commit is d395183674cace6c9906a8911bdeb7234ba4040d, 2025-12-30T15:29:31Z, "2509.05618: update to v2". GitHub API commit history contains six commits through 2025-12-30 and NO later May2026 v3 synchronization. At the exact pinned source path arXiv-2509.05618/main-scan.jl:
    X_n_nuc interpolated at T_nuc
    Y_code = 2 * X_n_nuc / (1-X_n_nuc)
    chi2 = ((Y_code-0.245)/0.003)^2
    Y_P_mat, chi2_mat saved in scanning.jld2.
Thus code remains DIFFERENT from BOTH v2/JCAP and the corrected v3 formula. The code was read using the connected original GitHub source at a commit pinned by the NASH MECH chain, NOT a guessed branch.
https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl
https://api.github.com/repos/Fenyutanchan/Primordial-Black-Hole/commits?per_page=30

SCIENCE STATUS: v3 fixing a printed equation does NOT certify which formula or computation generated journal Figure 5; no original figure data ancestry or solver/network replay was established.

## 2. Mature BBN foundation and exact interpretation of each formula

Particle Data Group, Big Bang Nucleosynthesis review, revised August2025, Sec 24.2 Eq(24.1), says the primordial He4 mass/nucleon fraction is approximately Y_p=2(n/p)/(1+n/p). Since X_n=n_n/(n_n+n_p), that is Y_p approximately 2X_n. Binding-energy effects induce a small mass-vs-baryon-count difference. The 2018 Pitrou, Coc, Uzan and Vangioni precision BBN review defines isotopic pseudo-mass fractions X_i=A_i n_i/n_b and Y_p=X_He4; genuine high precision uses a nuclear reaction network.
https://pdg.lbl.gov/2025/reviews/rpp2025-rev-bbang-nucleosynthesis.pdf
https://www2.iap.fr/users/pitrou/publi/PhysReptBBN.pdf

EXACT TWO-SPECIES DERIVATION. At T_nuc before nuclear fusion define n_b=n_n+n_p, x=n_n/n_b in [0,1/2). Assume all neutrons bind into helium-4, no other nuclei, no late neutron decay/production and conserved baryon number, ignoring nuclear binding mass corrections.

Then:
    n_He4 = n_n/2 = x*n_b/2,
    n_H_after = n_p-n_n=(1-2x)*n_b,
    n_proton_before=(1-x)*n_b.

Hence three mathematically valid but DIFFERENT observables:
    Y_mass = 4 n_He4/n_b =2x.                         (2.1)
    R_He/H_mass=4 n_He4/n_H_after=2x/(1-2x).         (2.2)
    R_He/preProton_mass=4 n_He4/n_proton_before
                     =2x/(1-x).                     (2.3)
The conventional He/H number ratio is
    y_He/H=n_He4/n_H_after=x/[2(1-2x)].            (2.4)

So the older journal and v2 formula is precisely the helium-to-remaining-hydrogen **MASS RATIO**, not the mass fraction of helium in TOTAL baryonic matter. The public code formula is a helium-mass-to-ORIGINAL-PROTON-pool ratio, not the mass fraction. The authors' May2026 v3 formula is consistent with PDG.

Within those same assumptions the proper conversions are
    Y_mass = R_He/H_mass/(1+R_He/H_mass),           (2.5)
    Y_mass = 2*R_He/preProton_mass/
             (2+R_He/preProton_mass).              (2.6)
The two ratios satisfy R_He/H_mass=2*C/(2-C), C=R_He/preProton_mass.

This source-matched stoichiometric interpretation is the precise additional PRF20 contribution after DAX's previously known formula mismatch. It is NOT a novel BBN theorem.

LIMITATION: if only fraction f of available neutrons ends in He4, then Y_He4=2f*x, not 2x. Full multinuclide networks, weak reactions, neutron decay, late emission and binding corrections must be accounted for; not even the corrected v3 approximation is a precision BBN solution on its own.

## 3. EXACT purely algebraic diagnostic: same number in wrong target type

The paper uses observed helium MASS fraction yobs=0.245 and sigma=0.003. For hypothetical fixed x=0.12:
    standard revised v3 Ymass=0.240000000
    pinned public code C=0.272727273
    journal/v2 mass-to-H ratio R=0.315789474.

IF a user IMPROPERLY compares any of these numerically to the SAME observed Ymass 0.245+-0.003 without adjusting the target type, implied x ranges (at a ±3 sigma scalar cut) are:

    definition                x center         x interval for y=0.236..0.254
    actual mass fraction     0.1225000000    [0.1180000000,0.1270000000]
    pinned code C            0.1091314031    [0.1055456172,0.1126885537]
    older journal R          0.0983935743    [0.0954692557,0.1012759171]

These THREE intervals are pairwise DISJOINT. This does NOT constitute a 3sigma experimental falsification or any PBH exclusion correction. It only demonstrates that reusing the mass-fraction likelihood on a different observable changes the feasible neutron fraction.

For code output C=0.245: Ymass=2C/(2+C)=0.2182628062, nominal discrepancy -8.9124 observational sigmas and chi2=79.43084 relative to 0.245 (one-point model with NO theory errors).
For older journal-style numerical R=0.245 interpreted as mass He/H: Ymass=R/(1+R)=0.1967871486, nominal -16.071 sigmas, chi2=258.27545.
These are algebraic conditional examples, not actual Figure5 data values.

If the physical mass-fraction observation is 0.245, the correct underlying x in the all-neutron-He4 approximation is x=0.1225; corresponding C=0.2792022792, R=0.3245033113 and He/H NUMBER y=0.0811258278. Comparing 0.245 directly to C or R is an observable-category mistake.

The formulas are monotone but are NOT interchangeable under a shared observational likelihood. A numerical source observable cannot be promoted to a physical bound without source/data version, calibration and target type.

## 4. Exact source-provenance discriminators — no fake action success

The latest author manuscript corrects the equation but no later public code commit exists. This establishes TEXT CURRENTNESS, not final published-figure or hardware-source ancestry. For any independently archived Figure5 Y_P array, IF there is proof that it came from the 2025-12 pinned code without subsequent conversion, a READ-ONLY algebraic remap Ymass=2*C/(2+C) would follow. Without such provenance this is only a conditional operation. IF a private network computation produced the published figure, the separate BBN-simple version and input/normalization would have to be established; authors' statement of "close agreement" is not independent confirmation.

Other independent bottlenecks:
- MECH-S7 numerical mass invariant violation and subedge data absence cannot be fixed by remapping an output column;
- MT13 four-cell dynamical interaction sign reversal does not prove microscopic emission nonadditivity;
- no legally admitted six-species hadron production + updated full BBN nuclear network + actual final Figure5 lineage is established.

This report does NOT recompute published PBH β contours, invalidate the authors' published constraints, accuse authors of misconduct, claim a new result in helium phenomenology or run the Julia/BBN solver. The newer v3 corrected formula is evidence of an author-level fix; changing one rendered equation cannot prove what numerical code was executed.

## 5. Prior-art subtraction and reproducibility

Already mature: PDG 2025 nucleon bookkeeping; helium mass-vs-number abundances; precision BBN multireaction network (Pitrou et al.); source control and source-to-observable-likelihood consistency; optimal decision/identifiability distinctions. Already project owned: DAX formula discrepancy and likelihood remap, MECH mass-cube numerical control, MT13 dynamic 2x2 attribution.

New specifically R20: verified arXiv v3 2026-05-06 correction against v2/printed JCAP; exact pinned code/master last-commit chronology; full physical interpretation of each formula's DIFFERENT DENOMINATOR; falsifiable source-currentness ledger without a premature published-bound claim.

Direct primary sources checked as of 2026-10-23:
1. Published Wu–Xu JCAP PDF: Eqs (2.4),(5.1), text about Figure5 and BBN-simple comparison;
2. Author arXiv PDF v2 and v3 Eq (5.1), plus authors' arXiv submission history and comments;
3. PDG revised2025 BBN PDF Sec24.2 Eq24.1 with screenshot inspection; Pitrou et al. 2018 scholarly BBN review definitions;
4. Original author GitHub API HEAD, exact pinned file and complete six-commit history, not third-party paraphrase;
5. DAX-S7 29–33, MECH-S7 004, MT13 2x2 and the active NASH scientific protocol.

External search was targeted, not a global theorem or novelty priority study. Sample literal queries: "Wu Xu JCAP 2026 063 Eq 5.1 Yp neutron fraction"; "PDG 2025 Big Bang Nucleosynthesis Yp 2(n/p)/(1+n/p)"; "arxiv 2509.05618 v3 May 2026 typos fixed"; "helium mass fraction He/H number and mass ratio conversion". No actual source JLD2 figure grid, original Julia source-time 10D rerun or network validation conducted.

STATUS: SOURCE_TEXT_V3_CORRECTED / PINNED_PUBLIC_CODE_NOT_UPDATED / FIGURE5_NUMERICAL_PROVENANCE_UNKNOWN / NO_CANON / NO_EXEC / NO_NOVELTY / NO_NEW_PHYSICAL_PBH_BOUND / GITHUB_PENDING_BW_INGEST.
