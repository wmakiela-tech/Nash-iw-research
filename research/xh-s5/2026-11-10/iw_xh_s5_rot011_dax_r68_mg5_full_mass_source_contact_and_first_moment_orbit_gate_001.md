# XH-S5 ROT011 — DAX source contact gamma gamma to e+e-e+e-: pinned MG5 electron mass configuration and necessary first-moment gate

ARTIFACT: IW_XH_S5_ROT011_DAX_R68_MASSIVE_QED_SOURCE_CONTACT_AND_EXACT_SYMMETRY_GATE_20261110
DATE: 2026-11-10
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_04 / XH-S5
RETURN_ID: XH-S5-ROT011-DAX-R68-MASSIVE-QED-SOURCE-CONTACT-MG5-MASS-RESTRICTION-AND-ORBIT-GATE_20261110
RESPONDS_TO: IW_DAX_S8_ROT006_GAMMAGAMMA_4E_SOURCE_CONTACT_AND_OWNER_REOPEN_GATE_001_20261110 and DAX ROT007 Sotsky four electron cut support
CLAIM_CEILING: EXTERNAL_ORIGINAL_SOURCE_CODE_READ / CLASSICAL_EXACT_SYMMETRY_AND_ONSHELL_NONQED_PHASE_SPACE / NO_MADGRAPH_EXECUTION / NO_NATIVE_4E_MATRIX_ELEMENT / NO_CROSS_SECTION_OR_R68_RATE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_BW_INGEST_ASSUMED

## Ownership and priority
DAX-S8 previously asked for an XH-S5 external source contact for uncutted, massive photon-photon double pair production; its ROT007 report observed owner receipt UNKNOWN. XH-S5 ACKNOWLEDGES this bounded source-contact role now. DAX-S8 and Moderator retain science acceptance. No independent delegation of generator implementation and no auto task cascade. The earlier EKS1 Schall original Source Data T1 is separately closed with NO temporal data in the *supplied* original archive; M14 temporal branch owner disposition pending.

## Original pinned MadGraph code: mass can be silently frozen to zero
Official original MadGraph5_aMC@NLO repo https://github.com/mg5amcnlo/mg5amcnlo
PINNED COMMIT a5b17913ef0b6e1c872016f94d0fb610207dab47 (2026-10-09). Native Github connector read complete bodies, verified returned Git blobs:
- models/sm/parameters.py at https://github.com/mg5amcnlo/mg5amcnlo/blob/a5b17913ef0b6e1c872016f94d0fb610207dab47/models/sm/parameters.py ; blob 3fdef86ab6d328e375a8a70c183b248804b3a79a ; external parameter Me=0.000511 GeV under MASS[11].
- models/sm/particles.py at https://github.com/mg5amcnlo/mg5amcnlo/blob/a5b17913ef0b6e1c872016f94d0fb610207dab47/models/sm/particles.py ; blob 37f079c96019560175c39aa0bb19ca3b1d113b87 ; PDG11 electron mass points to Param.Me.
- models/sm/restrict_default.dat at https://github.com/mg5amcnlo/mg5amcnlo/blob/a5b17913ef0b6e1c872016f94d0fb610207dab47/models/sm/restrict_default.dat ; blob 81943fc1cc83550a8177506015495cda6c981ec0 ; default restriction sets MASS[11] Me to ZERO (0.000000e+00).

Original MadGraph official docs https://cp3.irmp.ucl.ac.be/projects/madgraph/wiki/Models/USERMOD state restricted zero values are fixed at model-import time; default model sm is restricted, sm-full retrieves original unrestricted model. Thus the proposed actual massive e+e-e+e- process CANNOT simply use default sm and a later attempt to set me>0: need an explicitly full model and empirical check of actual generated Me in parameter card and amplitude. Candidate preflight: import model sm-full; validate electron pole mass 0.000511 GeV in generated process and all QED diagrams/identical permutations, no detector cuts. This is source-inventory guidance, NOT a tested MadGraph simulation command.

In current execution gfortran exists but mg5_aMC executable is NOT on PATH; full generator not downloaded, not run. Exact massive full uncut QED executable is ACCESS_BLOCKED HERE. No cross section, no QED energy moment, no native thermal-loss integral established.

## Mature prior art and nonmaps
- Carimalo, da Silva, Kapusta (1999), arxiv:hep-ph/9909339 — early helicity Monte Carlo; cannot treat historical partial work as delivered full present-day 4-body QED R68 simulation.
- Shishkina, Sotsky (2003), arxiv:hep-ph/0312208 — mature helicity matrix element for gamma gamma->4 leptons.
- Bredenstein, Dittmaier, Roth (2004), arxiv:hep-ph/0405169, DOI10.1140/epjc/s2004-01948-4 — lowest-order gamma gamma->4f generator and Whizard/MadGraph comparisons; uncutted massive R68 event receipt not independently present in this XH work.
- Sotsky 2006 arxiv:hep-ph/0604020 — collider-cut figures exclude four-lepton COM region at 0.67-2.12 GeV as DAX already established; paper cut does NOT imply zero physical QED process. No credit duplication.
- WPHACT 2.0 DOI10.17632/ypsy7cswgb.1 is e+e- INITIAL STATE, not gamma gamma. Geant4 nuclear Bethe-Heitler pair production and Pythia gamma gamma->e+e- are DIFFERENT processes from four leptons. Do not substitute process by title similarity.

## Novel-to-this-source-contact necessary symmetry control, NOT novel mathematics
Unpolarized full tree QED with e−_1,e+_1,e−_2,e+_2, on-shell massive and no charge- or label-selective cuts: exchange of the two identical e−, exchange of the two identical e+, and charge conjugation preserve spin-summed law, forming an 8-element group acting transitively on four labels. In lab energy is conserved event by event: sum_i E_i=Egamma+epsilon. Thus all four inclusive energy FIRST moments equal (Egamma+epsilon)/4. This is a necessary acceptance test for any symmetrized full uncut generator, NOT a proof of QED amplitude, total cross section, QED spectral shape or deposition. If cuts break charge/label symmetry, first-moment identities need not hold.

Independent executable A: standard library Fraction group closure verifies 8 permutations, exact first-moment equalities on 4 unequal rational energy tuples; label-specific cut E_label0>4 gives biased index0 average 9 instead of 11/2, independent NEGATIVE CONTROL. No imported QED code.

Independent executable B: NumPy generates 4500 positive-mass four-vector configurations from sequential two-body pair-cluster decays, each individually on shell, and boosts to asymmetric lab with numerically stable lightcone variables. IMPORTANT: sampled configurations are NOT even weighted according to invariant 4-body phase-space measure, let alone amplitude |M|^2; no physics distribution is claimed. Inputs E_gamma=1436.554 GeV; background T=0.07818527068831995 MeV; epsilon/T=1,2.701178,10; me=0.000511 GeV. Three sqrt(s) values 0.6702756547820867, 1.101615524390745, 2.1195977292721255 GeV, each above threshold 4me=0.002044 GeV. Max errors on sampled points: COM four-momentum 4.30e-13 GeV, laboratory four-momentum 4.77e-10 GeV, on-shell mass squared 1.05e-15 GeV^2, orbit-mean energy 1.20e-10 GeV. PASS. The necessary first mean at epsilon/T=1 equals approximately 359.13851955 GeV per lepton, NOT individual-event exact energy.

## Native run completion gate — NOT executed
Version-pin real working generator, ensure me>0 after model restriction and output, entire tree identical-particle interference, genuine 2 incoming photons, no detector pT/eta/angle/invariant-mass cuts, verify all run-card values and sample seeds. Freeze full sigma(s) with errors and all four charged-lepton energy distributions at the three COM energies and at high COM where literature asymptote of order 6.44-6.45 microbarn may be applicable after conventions established. Check summed four-energy conservation and 4 label-symmetric first moments. Only then consider physical thermal bath integration. DO NOT import 2006 collider-cut cross sections as full R68 DPP. NO SOURCE_NATIVE_QED_RUN in this return. OPEN in DAX's owner queue, not claimed delivered.

## Archive and test receipts
Original local archive IW_XH_S5_ROT011_DAX_R68_MASSIVE_QED_SOURCE_CONTACT_REPRO_20261110.zip, 12621 bytes, SHA256 90bd31cc6fe5cceecb3bb90155a1456d4216c5ba4691e0763bf2a0801a7db3a5.
Full local Polish Markdown report SHA256 d91dd767dca5df6ca2cac50f02ad069d54da401ebebc3aa71c94e2ade3a84377.
9 ZIP members: full report; two truly independent Python scripts; two frozen JSON outputs; upstream_receipt.json with original Git file blobs; README; file SHA256SUMS; verify_bundle.py. CRC ZIP PASS. 7 SHA member content checks PASS. Clean extraction, both scripts reexecuted; frozen JSON results BYTE_IDENTICAL PASS. The source receipt records Github file paths and hashes but neither the entire external MadGraph code nor its runtime is in the archive. The GitHub report is NOT the full ZIP. No science novel claim.

END: DAX_SOURCE_CONTACT_ACKNOWLEDGED / UPSTREAM_MG5_MASS_CONFIGURATION_GATE_PASS / EXACT_LABEL_SYMMETRY_AND_ONSHELL_TEST_PASS / TRUE_MASSIVE_UNCUT_MATRIX_ELEMENT_EXEC_ACCESS_BLOCKED / NO_QED_RATE / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_UNVERIFIED / NO_AUTO_TASK_CASCADE.
