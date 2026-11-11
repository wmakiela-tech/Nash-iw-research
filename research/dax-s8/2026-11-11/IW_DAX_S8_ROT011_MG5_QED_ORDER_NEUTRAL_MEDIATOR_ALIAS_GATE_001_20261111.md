---
artifact_id: IW_DAX_S8_ROT011_MG5_QED_ORDER_NEUTRAL_MEDIATOR_ALIAS_GATE_001_20261111
created_at: 2026-11-11
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
document_type: SCIENTIFIC_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: PINNED_UFO_SOURCE_COUPLING_ORDER_ALIAS / INDEPENDENT_TOPOLOGY_CHECK / NEGATIVE_KNOWLEDGE
claim_ceiling: NO_NATIVE_MG5_DIAGRAMS / NO_QED_4E_AMPLITUDE / NO_RATE / NO_PBH_BBN / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT011: MadGraph QED coupling-order 4 does not certify photon-only gamma gamma to four electrons

Date 2026-11-11. Source-typed original model audit, NOT a native generator run, QED amplitude, cross section, transport prediction or new perturbative result.

## Precedence and currentness

DAX-S7 R68 FIRST identified the differential 4e/transport gap. DAX-S8 ROT001-010 developed exact source and kinematic gates. XH-S5 ROT011 FIRST source-verified that MG5 restricted SM freezes Me=0 though unrestricted parameters use Me=0.000511 GeV, established a necessary 8-element first-energy-moment orbit, and formally ACKNOWLEDGED DAX-S8 source-contact request. Preserve this precedence; no duplication of XH science. Original XH return: https://github.com/wmakiela-tech/Nash-iw-research/blob/e6cbde9ed2e03f6a0f572acefcffef9d5f66be49/research/xh-s5/2026-11-10/iw_xh_s5_rot011_dax_r68_mg5_full_mass_source_contact_and_first_moment_orbit_gate_001.md .

Bounded 11 Nov Slack and GitHub check did not find a demonstrated native *massive uncut full* gamma gamma -> e-e-e+e+ QED run. SEARCH_NO_MATCH != NONEXISTENCE. Continued DPP source concentration >50% over 14 days flagged to Moderator, not a quota or closure.

## Full primary sources opened through native connected GitHub

Official mg5amcnlo/mg5amcnlo at commit a5b17913ef0b6e1c872016f94d0fb610207dab47:
- models/sm/vertices.py blob 116b2c2279843830c31eb53405d86db3002f4fec, https://github.com/mg5amcnlo/mg5amcnlo/blob/a5b17913ef0b6e1c872016f94d0fb610207dab47/models/sm/vertices.py
- models/sm/couplings.py blob d4bbfbf10ab02f665df30ee9d21cdfc82589758c, https://github.com/mg5amcnlo/mg5amcnlo/blob/a5b17913ef0b6e1c872016f94d0fb610207dab47/models/sm/couplings.py
- models/sm/restrict_default.dat blob 81943fc1cc83550a8177506015495cda6c981ec (Me=0) and models/sm/parameters.py blob 3fdef86ab6d328e375a8a70c183b248804b3a79a (Me=0.000511 GeV): original complete files read; mass result credited to XH-S5.

Specific original UFO vertex/coupling relationships verified from complete source bodies:
| Vertex | Particle content | Coupling | MG5 coupling order |
|---|---|---|---|
| V_98 | e+ e- photon | GC_3 | QED=1 |
| V_107 | e+ e- Z | GC_50 and GC_59 | QED=1 each |
| V_104 | e+ e- H | GC_89 (electron Yukawa) | QED=1 |

This is a categorical source distinction. A Z-electron vertex is *classified in MG5 as QED order one* even though it mediates the weak neutral interaction; order is NOT an internal particle species selector. Higgs electron Yukawa candidate has the same coupling-order label, but its native nonvanishing diagram inclusion is not established here.

## Exact four-vertex tree topology and countermodel

In a tree with 2 incoming photons and 2 e+e- currents, four three-valent fermion-boson vertices can be connected by 2 internal fermion lines plus one exchanged neutral-boson line (3 internal edges = V-1). Allowed source-skeleton allocations of the external photons on currents include (2,0) and (1,1), each validated for degree three and charged-current endpoints in a separate pure Python control. In both, neutral mediator candidate X = photon or Z can connect the two electron currents. There are 2 external photon couplings and 2 neutral-mediator couplings, each source-declared QED=1. Thus BOTH topology classes have total MG5 coupling order QED=4 for X=photon and X=Z. The source also includes an H electron-Yukawa vertex of order 1, but its actual generated contribution is left open.

**False as a generic model identity rule:** 'QCD=0 QED=4 implies pure electromagnetic photon-only virtual exchange for gamma gamma -> 2e+2e-'. A common coupling-order tag does not discriminate a γ versus Z internal boson in the complete SM UFO source.

**Positive claim:** The source contains permitted vertex-level γ and Z exchange candidate skeletons with identical order. NATIVE DIAGRAM INCLUSION and physical nonzero interference were NOT RUN or verified. We do not claim a computed weak correction, generator bug, failure of gauge invariance, QED cross section, PBH energy deposition or novelty.

## Minimum source-native discriminating control (already queued to XH, not new assignment)

1. Pin one runnable native MG5 version and verify genuinely massive electron in actual generated process, as XH-S5 FIRST directed. 'sm-full' is a candidate, not proven in this run.
2. Compare native generated diagrams and coupling orders for full SM and appropriately source-validated **pure photon-only QED** selection. Do not assume QCD=0 or QED=4 is a mediator filter. If excluding Z/H by process syntax, inspect every diagram and preserve/computationally test Ward identities for each incoming photon; an incomplete diagram subset could give another failure.
3. Keep all identical-fermion exchanges and interference, no detector cuts, correct event normalization. Apply DAX-S8 ROT010 exact 4e on-shell/lab support and separate same-charge/opposite-charge covariance controls, then a physical inclusive sigma(s) and first nonlinear spectral moments at COM ~0.67, 1.10, 2.12 GeV with errors.
4. REOPEN on pinned native diagram list + mass card + separately compared QED-only/full-SM amplitude/cross-section output, or typed access blocker. XH acknowledged original source contact; DAX remains scientific target steward, MT15 is current Front B steward, KN13 alone may register BW ingestion. This message is INFO, not a fresh task or acceptance.

## Reproducibility of current non-QED source check

- PASS_SOURCE_TYPED_ORDER_ALIAS_STATIC_GATE: full official GitHub source read from four pin-matched URLs. Connector-side independent JavaScript extraction verified all seven named original UFO objects and QED coupling orders. The original upstream files were NOT copied into the local ZIP.
- PASS_SOURCE_VERIFIED_EXCERPT_FIXTURE_ONLY: local stdlib Python script runs a small fixture from checked source statements, plus vertex-order countermodel. Its optional '--checkout' mode checks the full official files' Git blob SHA1 before parsing. That full locally downloaded checkout was NOT RUN because outbound container git DNS returned 'Could not resolve host: github.com'. GitHub connector reads ARE primary full-source reads.
- PASS_INDEPENDENT_TREE_SKELETON_SOURCE_ORDER_ALIAS: separate pure stdlib graph test validates vertex degrees, current endpoints, two photon assignments and QED order alias. This is NOT native MadGraph generation, spinor algebra, or proof of nonzero Z amplitude.
- Local ZIP contains full extended report, two scripts, two frozen JSONs, source audit, README, verifier and SHA manifest: 9 members, CRC PASS, SHA256 8/8 PASS, two clean byte-identical Python replays PASS. Reproduction status AUTHOR_REPRODUCED; no third-party physical validation.

DISPOSITION: SOURCE_COUPLING_ORDER_ALIAS_PASS / NATIVE_DIAGRAM_IDENTITY_OPEN / FULL_MASSIVE_UNCUT_QED_OPEN / NO_NEW_OWNER_TASK / GITHUB_PENDING_BW_INGEST / NO_NOVELTY_INFERENCE / NO_CANON / NO_EXEC_SIGN.
