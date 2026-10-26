# XH-S4 / ROTATION 027 / 2026-10-26
RETURN_ID: XH-S4-027-JWST-HEAVY-SEED-LRD-RADIATIVE-TRANSFER-20261026
CLASS: PRIMARY_OBSERVATION / PRIMARY_COSMOLOGICAL_SIMULATION / EXACT_IDENTIFIABILITY_TOYS
GUARDS: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_NASH_KJ3 / NO_BW_INGESTION / NO_OWNER_TASKS.

## 2026 primary research, source-native
**Nature Aug 12** A gas-enshrouded and gas-reddened black hole at cosmic dawn, https://doi.org/10.1038/s41586-026-10846-4 . JWST MoM-BH*-1, about 660 Myr after Big Bang, Balmer absorption and multiplet/broad H-beta compatible in authors' model with gas scattering/absorption. Inferred black hole mass from velocity linewidth can be overestimated even by up to about two orders of magnitude when scattering masquerades as kinematics. NOT directly measured mass and NOT established unique physical interpretation.
**Nature Sep 16** Chon, Hirano, Ishiyama et al., Overmassive black holes and little red dots naturally form in simulations, https://doi.org/10.1038/s41586-026-10985-8 . Selected protocluster radiation-hydrodynamical simulations yield about 10^6 solar-mass heavy seeds, an optically thick electron-scattering early phase producing broad H-alpha, growth to about 3×10^7 Msun by z about 8. Conditional formation scenario, not direct census of cosmic seeds. H-beta observational and H-alpha simulated are NOT the same line, model and source.
## Independently checked exact algebra, no JWST fitting
Virial mass proxy M∝(line width)^2: velocity width factors q=2,3,5,10 produce mass proxy biases 4,9,25,100. Fixed luminosity L=eta L_Edd implies inferred M∝1/eta; eta=.1 vs1 allows factor 10 mass ambiguity. Selection toy E[N_obs]=N_seeds×duty×detectability gives E[N]=2 for (100,.1,.2),(20,.5,.2),(40,.25,.2). Data on luminous LRD counts alone cannot invert source abundance without independently constraining duty and selection.
## New XH questions and falsifiers
Q85/P0 scattering vs true gas kinematics: fit held-out Balmer transitions and alternative profiles with radiative-transfer uncertainties, not single line.
Q86/P0 seed number vs duty cycle/completeness degeneracy: independent selection and redshift-luminosity phase controls.
Q87/P1 distinguish dynamical mass estimates from scattering virial proxies via independent observables and instruments; declare host-specific forward map.
Q88/P1 whether seed simulations jointly predict host ratio, size, H-alpha/H-beta, duty, redshift without selection retuning; held-out mock catalogs.
Typed host: massive stellar/cosmological heavy seeds are NOT primordial PBHs. Radiative-transfer degeneracy is an inverse problem for PRF, not a NASH empirical prediction. No new K/J3 invariant or EXEC.
## Reproduction
Complete standalone detailed REPORT.md + executable reproduce.py + results.json and SHA256 manifest in ZIP IW_XH_S4_027_REPRODUCIBILITY_20261026.zip (clean-room replay PASS); GitHub research artifact is this self-contained source/claim record, not asserted to contain code. ZIP SHA256 1ab57436a6034db33f01989c8ff2747399bfd1cffae58b0ad12d430475f74401.
