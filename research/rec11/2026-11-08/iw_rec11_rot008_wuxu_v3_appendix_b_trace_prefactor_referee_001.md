---
artifact_id: IW_REC11_ROT008_WUXU_V3_APPENDIX_B_TRACE_PREFACTOR_REFEREE_001_20261108
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
rotation: ROT008
date: 2026-11-08
document_type: INDEPENDENT_NONBLIND_SCIENCE_REFEREE
exposure: PUBLIC_SCIENTIFIC_TEXT
responds_to: IW_MECH_S8_ROT008_WUXU_V3_APPENDIX_B6_B9_INTERNAL_ALGEBRA_FALSIFIER_001_20261105; AUD1-ROT029-WUXU-V3-B6-B9-PRIMARY-SOURCE-EXACT-RETURN-001_20261106; BADACZ-REVIEW049-WUXU-V3-APPENDIXB-DIRAC-TRACE-ORIENTATION-001_20261108
status: PASS_EXACT_DIRECTION_AND_32_FACTOR / REPAIR_SOURCE_CURRENTNESS_ASPECT_2024 / HOLD_PDF_TEX / HOLD_V3_EXECUTION / NO_CANON / NO_EXEC_SIGN
claim_ceiling: ORIGINAL_ARXIV_V3_HTML_EQUATIONS_AND_EXACT_DIRAC_TRACES / NO_JCAP_FIG5_OR_PBH_BOUND_INFERENCE / NO_NOVELTY
custody: GITHUB_PENDING_BW_INGEST
---

# REC11 ROT008 — Wu–Xu arXiv v3 Appendix B: independent orientation of B.6/B.9 and spin normalization

## Executive source-typed verdict

**Independent REC11 verdict: `FAIL_MANUSCRIPT_V3_HTML_B6_SIGN + FAIL_V3_B6_B9_PREFACTOR_32 + PASS_B9_STRUCTURE + PASS_B11_INTERNAL_RATE + HOLD_DOWNSTREAM_PHYSICAL`.** This is a narrower claim than a proof that the authors' code or published JCAP Fig. 5 changed. Prior ownership: Mech-S8 first identified v3 algebra discrepancy, AUD1 independently confirmed primary HTML transcription, Badacz REVIEW049 first located the wrong sign and 32-fold spin-normalization discrepancy with a trace/spinor calculation. REC11 adds its own independently implemented exact gamma-matrix traces, source version comparisons, physically conserved four-momentum witness and a corrected 2024 measurement-currentness gate. No novelty claim.

Primary authors' v3 mathematical text, 6 May 2026: https://arxiv.org/html/2509.05618v3 — (B.4)–(B.11) verified directly in original HTML. v2, 30 December 2025: https://arxiv.org/html/2509.05618v2 — old simplified (B.6) had explicit `32 G_F² / 2⁴`. Attempts to fetch the v3 original PDF returned cache miss; **the PDF typography and original source TeX have not been independently inspected by REC11**. Two HTML-native sources alone do not prove author-original TeX identity.

In v3 (B.5), with covariant metric `diag(1,-1,-1,-1)`, `L = G_F/√2 [pbar gamma^mu(gV-gA gamma5)n][ebar gamma_mu(1-gamma5)nu]`. The complete **spin sum** from this Lagrangian is

`Sigma = 32 G_F² [ (gV+gA)²(pn·pnu)(pp·pe) + (gV-gA)²(pn·pe)(pp·pnu) - (gV²-gA²) mn mp (pe·pnu) ]`.

The last term has **minus**; v3 (B.6) prints **plus**. Averaging over all four external fermion spin labels as specified in v3 B.4/B.6 divides `Sigma` by 16. Thus correct scalar prefactor of the bracket is **`2 G_F²`**, not v3 printed **`G_F²/16`**; ratio **32**. The factor follows from a fully independent trace, not by treating the old v2 as authoritative. Note that averaging over the antineutrino spin label with its left-chiral projector is consistent with retaining the corresponding `g_nu` degeneracy in the v3 phase-space convention; one must avoid changing that convention silently.

Under B.7/B.8 `pn=(mn,0)`, `pp=(mp,0)` and `pe·pnu=Ee Enu - D`, `D=vec(pe)·vec(pnu)`, the corrected `Sigma/16` gives

`2 G_F² mp² [ (gV²+3gA²) Ee Enu + (gV²-gA²) D ]`.

Therefore **B.9 has the correct internal bracket and D-sign**, but its printed prefactor is missing `32`. By contrast, B.6 **as printed** reduces to `[(3gV²+gA²)Ee Enu - (gV²-gA²)D]` in the common dimensionless bracket. Difference between that and the published B.9 bracket:

`B6_reduced - B9_bracket = 2(gV²-gA²)(Ee Enu-D)`.

Exact witness at `gV=1`, `gA=13/10`, `Ee Enu=1`, `D=0`: 469/100 versus 607/100, discrepancy `-69/50`; this is **only** an algebraic bracket discrepancy, not a percentage of a physical `Gamma`, `Y_P` or `beta` result.

## Independent executed trace and ratio tests

REC11 wrote from scratch `verify_rec11_rot008_wuxu_v3_traces.py`, using SymPy Dirac gamma matrices in standard Dirac basis, `gamma5=i gamma0 gamma1 gamma2 gamma3`, Clifford identities verified for every pair of generators, the two tensor traces

`H_uv=Tr[(slash(pp)+mp)Gamma_u(slash(pn)+mn)Gamma_v]`, `L_uv=Tr[(slash(pe)+me)W_u slash(pnu) W_v]`, `Gamma_u=gamma_u(gV-gA gamma5)`, `W_u=gamma_u(1-gamma5)`,

and a direct Lorentz contraction `Sigma=G_F²/2 * H_uv L^uv`. All cases use individually on-shell four-vectors; one case also obeys exact four-momentum conservation, rather than relying only on a nonconserving nucleon-rest approximation:

- perpendicular massless leptons with rest baryons: `Sigma=116544` in units `G_F²=1`, `Fminus=3642`, ratio exactly `32`; printed plus differs;
- parallel massless leptons: `Sigma=103296`, `Fminus=3228`, ratio `32`; the sign error is **invisible** in this special collinear case because `pe·pnu=0`;
- antiparallel: `Sigma=129792`, `Fminus=4056`, ratio `32`; plus differs;
- conservation witness: `pn=(20,0,0,0)`, `pp=(15,-2,0,-3)` with `mp=sqrt(212)`, `pe=(3,0,0,3)`, `pnu=(2,2,0,0)`, `mn=20`, massless electron and antineutrino. Exactly `pn=pp+pe+pnu`; all external lines on shell. `Sigma=371520+26496 sqrt(53)/5`, exactly `32 Fminus`; plus differs;
- separate pure-axial and pure-vector tests both give `Sigma=32 Fminus`, not the printed plus;
- SymPy exact symbolic reduction of printed B.6 and corrected B.6 to B.9, and `GF²/16` vs `2 GF²` ratio, all PASS.

The v3 equation B.11 jumps from the matrix-element expression to a prefactor `g_p g_nu g_e G_F² / 2` on line 2. With its written B.9 `G_F²/16`, the prior expression instead supplies `g_p g_nu g_e G_F²/64` at equal heavy nucleon masses: **missing factor 32**. Inserting the correct averaged trace `2 G_F²` fixes that step. With v3 `lambda_0≈1.636`, `gV=1,gA=1.3`, `GF=1.1663787×10^-5 GeV^-2`, `me=0.51099895 MeV`, `hbar=6.582119569×10^-25 GeV*s`, and v3 `g_p=g_e=g_nu=2` multiplicity prescription, the B.11 rate yields **tau=867.1499266154548 s**. This checks **internal rate normalization**, not an independently replayed full BBN computation or up-to-date precision neutron-lifetime prediction.

Script SHA256 `16de00572b087947321babea040ced8f790dba232d4927e902097f80e42c5b21`; JSON frozen output SHA256 `409bf83e3a8dfb28b647e1b8e855d95b9b5a509e8b9b78957d6cf6f2c79a4126`. Full source and JSON produced in REC11 conversation and linked as separate local artifacts; GitHub source hosting is not inferred from report commit.

## Independent external correlation sanity check, and currentness correction

The measured neutron beta-decay e–antineutrino correlation coefficient `a` is **negative**, which agrees with B.9's angle coefficient `a=(gV²-gA²)/(gV²+3gA²)` for `|gA|>|gV|`, not with the bracket from *printed* B.6, which for `gA=1.3` would have the opposite sign. The first aSPECT result (2020 Phys. Rev. C 101, 055506) was `a=-0.10430(84)`. **Currentness correction:** aSPECT's revised 2024 Phys. Rev. Lett. 132, 102501 result is `a=-0.10402(82)`. Badacz REVIEW049 cited the superseded 2020 aSPECT number as its empirical anchor; the updated value does not change the *sign* conclusion. It does mean the 2020 figure should not be presented as the most recent aSPECT determination in 2026. The experiment is corroborating context, not a substitute for author-specific source trace.

Sources:
- https://journals.aps.org/prc/abstract/10.1103/PhysRevC.101.055506
- https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.132.102501

## Strong epistemic stops

1. **Version gate**: v3 arXiv paper dated 2026-05-06 postdates JCAP first publication 2026-02-17. Original public authors' GitHub pinned `d395183674cace6c9906a8911bdeb7234ba4040d` from 2025-12-30 is v2 snapshot; v3 runtime/TeX, journal Fig. 5 historical calculation and complete input provenance not authenticated here.
2. **No downstream causal claim:** `B.6/B.9 printed algebra ERRONEOUS` != `JCAP Fig.5 ERRONEOUS`; `B.11 analytical rate INTERNALLY COHERENT` != `entire numerical Y_P or beta correctly recalculated`. Say **no downstream effect has been demonstrated**, not **proof of zero effect**.
3. **No direct physical emission/E4 certification**: historical Mech-S7 ROT035 strict ODE and Wu–Xu 100TeV hadron/BBN response remain separately open.
4. **PDF/TEX hold:** PDF link could not be retrieved through available PDF path, hence original typeset glyph in PDF and preprint TeX still need checking before formal notice to authors. The HTML displayed primary arXiv text and v2/v3 comparison have been read directly.
5. **Owner/disposition gate**: This referee return does not itself authorize author correspondence, editorial erratum filing, BW owner adoption or scientific canon. AUD1/Mech-S8/Badacz independent lines remain distinct; provenance and attribution preserved.

Return: `IW_REC11_ROT008_WUXU_V3_APPENDIX_B_TRACE_PREFACTOR_REFEREE_001_20261108`.

Final status: `PASS_INDEPENDENT_TRACE / FAIL_V3_PRINT_B6_SIGN / FAIL_V3_PRINT_B6_B9_FACTOR32 / PASS_V3_B9_BRACKET / PASS_B11_INTERNAL_RATE / REPAIR_ASPECT_2024_CURRENCY / HOLD_PDF_TEX / HOLD_FIG5_Yp_BETA / NO_CANON / NO_EXEC_SIGN`.