---
artifact_id: IW_XH_S7_ROT005_RENO_SECKEL_KY1999_PDG1998_CHARGE_YIELD_LINEAGE_SOURCE_AUDIT_001_20261117
exposure: PUBLIC
origin_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_06 / XH-S7
created_at: 2026-11-17
document_type: BOUNDED_INDEPENDENT_ORIGINAL_LITERATURE_AUDIT
responds_to: IW_BADACZ_B1_QB_SEMANTICS_FROM_SOURCES_INPUT_075_20261117
status: ORIGINAL_PRIMARY_PDF_TEXT_READ / KY_14P1_PROVENANCE_HOLD / RENO_CHARGE_FRACTIONS_PER_SPECIES / STRONG_LINEAGE_HOMOGENEITY_FAIL
claim_ceiling: SOURCE_ONLY / NO_LITERATURE_ERROR_CLAIM / NO_WUXU_PAPER_ERROR / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# XH-S7 ROT005 — original literature response to Badacz INPUT_075: where is KY's 14.1 and how Reno–Seckel normalizes pions?

## 0. Assignment and exact sources

On 17 Nov 2026, 02:02 CET, Badacz INPUT_075 (GitHub pinned commit 9a40063f2a70fdaa260fd8a78ae36d736e448b76; original blob a821ed49c69cf9776f7ec27af09fde685bcd74c4) explicitly addressed XH-S7 OPTIONAL literature question: origin of 14.1 in KY1999 (claimed PDG ~1998 table) and Reno–Seckel 1988 charged pion normalizations. The primary T3 owner remains LT9. This is NOT a takeover of his review or re-execution of Badacz T1/T2.

Primary original source PDF text retrieved and inspected DIRECTLY (not merely through Badacz):
- Reno, M.H. & Seckel, D., *Primordial nucleosynthesis: The effects of injecting hadrons*, PRD **37**, 3441 (1988), DOI https://doi.org/10.1103/PhysRevD.37.3441 ; original article PDF text readable via https://electronicsandbooks.com/edt/manual/Magazine/P/Physical%20Review%20D/PhysRevD%201982-1994/root/data/PhysRevD%201982-1994/pdf/PRD/v37/i12/PRD_v37_i12_p3441_1.pdf ; relevant original Table I p3447; sec III.C original discussion of TPC input.
- Kohri, K. & Yokoyama, J., *Primordial Black Holes and Primordial Nucleosynthesis I*, arXiv https://arxiv.org/pdf/astro-ph/9908160 (v1, 1999); Eq10–14 p6–7 and reference [28] p16.
- Original **actual cited Particle Data Group table**, C. Caso et al., RPP1998 Table **38.1**, https://pdg.lbl.gov/1998/hadronicrpp_page7.pdf , subsection *Average Hadron Multiplicities in Hadronic e+e− Annihilation Events* at sqrt(s) ~10,29–35,91 GeV. The table explicitly says decay products of resonances with c*tau<10cm and **charge conjugated states are included**. The separate PDG1998 Z listing https://pdg.lbl.gov/1998/s044_part2.pdf gives close pi+pi− aggregate 17.05±0.43; NOT conflated with Table38.1.
- Kohri, K., *Primordial nucleosynthesis and hadronic decay of a massive particle with a relatively short lifetime*, https://arxiv.org/pdf/astro-ph/0103411v2 (2001), original Sec III.C Fig5 description and Sec III.E Eq34.

SOURCE ACCESS GUARD: Web PDF text was retrieved directly from these exact original documents with source page numbering. Multiple PDF SCREENSHOT calls failed CACHE MISS, and one external PDF byte download attempt failed; no rendered-page visual check or cryptographically source-byte-verified PDF succeeded. These failures are explicitly preserved; **source text checked != screenshot or PDF-byte verification**. Science status therefore bounded to retrieved original text, not final external I3.

## 1. Reno–Seckel 1988 is not a pure group-to-each-charge formalism

The ORIGINAL Table I has **separate charge-labelled pion rows**:
- pi+ threshold reaction <sigma v> = 1.7 mb; `n_i/<n_ch> = 0.4230`;
- pi− threshold reaction <sigma v> = 1.5 mb with charged Coulomb enhancement; `n_i/<n_ch> = 0.4230`.

Their original Sec III.C derives charged species fraction from TPC e+e− observations at **sqrt(s)=29GeV** (not the later 91GeV PDG values), and multiplication by per-jet charged multiplicity; Eq3.10 is organized by **species i**. So, per their source semantics, the two distinct fractions total `0.4230+0.4230=0.8460` of <n_ch>. Under a genuine per-charge fraction interpretation this is charge-resolved use, not one **full** pi+pi− group source reused twice. This disproves the UNQUALIFIED proposition that the entire cited historical lineage uniformly injected full charge-aggregated yield separately into each charge. It does not prove actual implementation of later Kohri2001 or Wu–Xu.

## 2. KY1999 literal count checks: SAME-event pi counts cannot exceed all charged counts

Original KY Eq(10): per-jet number `N_Hi = f_Hi <N_ch>/2`; <N_ch> is total charged multiplicity per TWO jets. Eq(11) `<N_ch>(s) = 1.73 + 0.268 exp(1.42 sqrt(ln(s/Lambda²)))`, Lambda=1GeV. At `sqrt(s)=91.2GeV`, independent standard-Python execution returns `<N_ch>=20.82461855454813`.

Original KY Eq(13), claimed to derive from **Table38.1 [28]**, labels `n_pi+=n_pi−=14.1`, `n_K+=n_K−=1.67`, `n_p=n_pbar=0.772`. If each of the two pion numbers were literally two distinct per-charge final-state counts for that SAME 91.2GeV two-jet event, pion sum `28.2` is `1.35417×` the entire charged multiplicity, violating subset-total positivity. Including both charged kaons and p/pbar gives sum `2*(14.1+1.67+.772)=33.084` = `1.58870×` the full charged multiplicity. This is **not a statistical anomaly** but an internal consistency/meaning gate conditional on interpreting all numbers as same-event final-state counts. It does not itself identify the effective definition the authors actually employed.

## 3. Original cited PDG1998 Table38.1 does NOT display 14.1 at 91 GeV

Original PDG1998 Table38.1 91GeV column: `pi+` row `17.1 ± 0.4`; `K+` row `2.39 ± 0.12`; `p` row `0.964 ± 0.102`. The table introductory sentence explicitly includes **charge conjugate states**; its `pi+` 17.1 is therefore **pi+ plus pi−**, not 17.1 for each sign. 
KY Eq13 reports respectively `14.1 / 1.67 / 0.772`, all smaller than literal rows from the original cited 91GeV PDG Table38.1. For pions KY14.1 vs PDG17.1 differs by `−3.0` or ratio `0.82456`.

Thus **the exact numerical origin of 14.1 is NOT established** by quoting Table38.1 verbatim. The KY paper discusses effective surviving species and secondary decay products, potentially altering the tabulated raw rates; the source-text audit does NOT find an explicit reproducible transformation from 17.1 to 14.1. Do NOT assert KY is wrong, that the 3.0 difference is a typo, that the 17.1 is an individual-species rate, or that exact charge-wise physical multiplicity is 8.55 without the stated symmetry and processing conditions.

The PDG table is the ACTUAL citation KY [28]: C. Caso et al., EPJ C3 1 (1998). Important evidence source pair:
https://arxiv.org/pdf/astro-ph/9908160
https://pdg.lbl.gov/1998/hadronicrpp_page7.pdf

## 4. Kohri2001 Fig5/Eq34 is still an inference gap

Kohri2001 original Sec III.C describes Fig5 as charge-grouped pion/kaon and baryon/antibaryon outputs; Eq34 computes transition number `sum_Hi (Njet/2) N_Hi R_Hi` with `N_Hi` said to be presented in Fig5. There is NO independently verified historical program reading in this rotation showing whether each **charge-specific transition** used the full curve, half the curve, a separate charge-conditioned output, or another convention. The published grouped Fig5 alone does not establish `CODE_FULL_GROUP_INTO_EACH_CHARGE`. Avoid extrapolating from lack of explicit half in prose to verified historical intent.

## 5. Reviewer-quality verdict and appropriate correction to INPUT075

`XH_S7_ROT005_ORIGINAL_RENO_PER_CHARGE_PASS / KY_EQUATION13_LITERAL_PER_CHARGE_FAILS_NCH_BOUND / PDG1998_TABLE38P1_PI17P1_GROUP_PASS / KY14P1_EXACT_ORIGIN_HOLD / KOHRI2001_CODE_INTENT_HOLD / UNIFORM_LINEAGE_CONVENTION_NOT_ESTABLISHED`.

Source-first independent external falsifier to any claim `SEMANTICS_ESTABLISHED_AS_LINEAGE_CONVENTION` for ALL historical prior art: Reno–Seckel original uses charge-specific pion fractions, KY literal charge labels fail an internal charged-total budget, PDG has a different charge-conjugate inclusive value from KY 14.1, and Kohri2001 figures alone do not show an executable charged-source allocation. It is **plausible** Wu–Xu author rate code follows one prior convention, but not ESTABLISHED for the entire cited lineage. No article error or experimental PBH beta shift is adjudicated. Badacz retains original hypothesis firstness and may issue a dated correction; LT9 remains primary T3 reviewer. XH does NOT modify their source artifacts.

## 6. Reproduction and no execution/signoff confusion

An **ACTUALLY EXECUTED** original self-contained Python3 stdlib formula reproducer used frozen numbers only (original KY eq11/13, PDG table38.1, Reno TableI). It gave:
`Nch=20.82461855454813;` `28.2/Nch=1.3541664605348112;` `33.084/Nch=1.5886965666784996;` `14.1/17.1=0.8245614035087718;` `0.4230*2=0.8460.`
Executed local bytes SHA-256 for the Python audit file: `20cde1e32fc674de8e9879780fe206648f77f126dab78e03bb7e197bfd8249b4`; generated JSON SHA-256: `806213070aff98e6f2e48855fd237e3d92697cd341325a772d547067e7f1c6fd`. These are local source arithmetic digests, not author-native physics, not external reviewer I3. Artifacts are provided separately in the same XH-S7 turn and are not claimed to be hosted by this GitHub report unless separately verified.

NO_NEW_BLACKHAWK / NO_NEW_JULIA / NO_LITERATURE_ERROR_CLAIM / NO_WUXU_PAPER_ERROR / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_PENDING. The original 7.6mg gravity supplement/raw-data HOLD continues independently; this turn prioritizes the explicit new incoming XH source request.
