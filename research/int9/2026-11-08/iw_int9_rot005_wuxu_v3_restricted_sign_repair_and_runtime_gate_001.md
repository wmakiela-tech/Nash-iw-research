---
artifact_id: IW_INT9_ROT005_B6_B9_SIGN_REPAIR_CONDITIONAL_NO_FIG5_TRANSFER_20261108
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_09 / INT9
date: 2026-11-08
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_AUTHOR_PDF_TEX_CHECK / NO_GAMMA_TRACE / NO_JULIA_REPLAY / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---
# INT9 ROT005: source typed sign repair and no runtime/BBN transfer

**Priority:** Mech-S8 ROT008 FIRST identified and independently reproduced the v3 B.6–B.9 algebra inconsistency:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s8/2026-11-05/IW_MECH_S8_ROT008_WUXU_V3_APPENDIX_B6_B9_INTERNAL_ALGEBRA_FALSIFIER_001_20261105.md .
The present INT9 contribution is a restricted exact repair condition, a kinematically sign-definite consequence, and a source-version/run transfer STOP, not a new physical result.

**Sources:** Original authors Wu and Xu, https://arxiv.org/html/2509.05618v3 (6 May 2026), B.6–B.9 and B.15. Original v2 https://arxiv.org/html/2509.05618v2 (30 Dec 2025) is different. Published JCAP 02 (2026) 063 https://doi.org/10.1088/1475-7516/2026/02/063 is a separately identified object. Source HTML read independently. PDF/TeX and historical paper runtime NOT authenticated.

## Exact mathematical test

Remove common factor GF^2 mp^2/16. Put V=gV, A=gA, E=Ee Enu, D=three-momentum dot of electron and neutrino. The source v3 B.6 with its own B.7/B.8 yields:
B6_NR=(V+A)^2 E+(V-A)^2 E+(V^2-A^2)(E-D)=(3V^2+A^2)E-(V^2-A^2)D.
But printed B9=(V^2+3A^2)E+(V^2-A^2)D.
B9-B6_NR=-2(V^2-A^2)(E-D) (Mech-S8 prior).

**Restricted repair candidate:** Change only the scalar coefficient +1 of the THIRD B.6 covariant term to arbitrary c. Then
B9-B6_c=-(c+1)(V^2-A^2)(E-D).
For generic V^2 != A^2 and E != D, equality for all such cases holds iff c=-1. Thus the sole third-term SIGN FLIP is sufficient and unique WITHIN THIS ONE-COEFFICIENT FAMILY. This does not prove the underlying spinor trace or original intended text; alternative global repairs may exist.

**Conditional strict-sign witness:** with V=1,A=1.3 and massive electron, positive-energy massless neutrino, E-D=Enu(Ee-|pe|cos(theta))>0 for all cos(theta) in [-1,1]. Then B9>B6_NR pointwise. Its gap cannot cancel in ordinary angle integration using nonnegative weights at stated leading-order approximation. Source example E=1,D=0 yields B6_NR=469/100, B9=607/100, B9-B6_NR=69/50, relative to B9 138/607 about 22.735%, same numerical example as Mech. This is NOT a percent of a physical beta-decay rate, Yp, PBH beta or figure effect.

## Earliest blocked transfer arrow

The author public v2 Git commit d395183674cace6c9906a8911bdeb7234ba4040d, path arXiv-2509.05618/main-scan.jl, Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6 was read directly. Line 71 uses Gamma_n_SM=(255/tau_n)*(12+6x+x^2)/x^5, line 88 a separate SM conversion contribution, line 89 separate neutron decay -Xn/tau_n. This v2 code does NOT derive the source v3 B.6 amplitude in its historical runtime. The manuscript v3 B.15 and this v2 runtime are not authenticated as byte-identical versions; historical JCAP Fig5 runtime and v3 correction implementation remain OPEN. Therefore even a proven algebra error in a manuscript does NOT imply any particular JCAP Fig5, Yp or PBH abundance error. Mech-S8 ROT007 version erratum first:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s8/2026-11-03/IW_MECH_S8_ROT007_WUXU_V2_V3_PUBLICATION_SOURCE_CUSTODY_ERRATUM_001_20261103.md .

## Repro and guard

Independent Fraction 320 exact tuples, SymPy symbolic sign-coefficient derivation, and seven physical-angle rational witness cases PASS. Local standalone Markdown and 5-member ZIP with source + JSON + manifest checked ZIP CRC PASS, SHA256 PASS and CLEAN_REPLAY PASS. Local report SHA256 35c6d777c695bd2342c48684738522003af4aa63013ebdc26ec4cd7377253c49; local ZIP SHA256 9cf46948d27623763f393767288033dbb22bc6c7f3921a2a478242aaaccfd48f. These bytes reside in Moderator's INT9 conversation, NOT inside this report.

The bounded next audit would source-authenticate v3 PDF/TeX and recompute Dirac spin traces; only source-native v3 rate code and exact historic JCAP figure run identification could enable physical propagation. No automatic task cascade or owner acceptance.

**STATUS: SOURCE_HTML_ALGEBRA_CONFLICT / RESTRICTED_REPAIR_CANDIDATE_PASS / RUNTIME_VERSION_BLOCK / JCAP_FIG5_EFFECT_UNDETERMINED / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_PENDING.**
