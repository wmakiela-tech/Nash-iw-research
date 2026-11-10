---
artifact_id: IW_DAX_S8_ROT009_BOOST_FRAME_CUT_TRANSFER_AND_XH_SOURCE_RECEIPT_GATE_001_20261111
created_at: 2026-11-11
origin_cell: IW_DIVERGENT_SEARCH_AND_ANOMALY_CELL_001_SUCCESSOR_07 / DAX-S8
document_type: SCIENTIFIC_RETURN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
result_class: EXACT_LORENTZ_FRAME_TYPED_KINEMATIC_NONMAP / XH_SOURCE_RECEIPT_RECONCILIATION / NEGATIVE_KNOWLEDGE
claim_ceiling: NO_NATIVE_MADGRAPH / NO_4E_QED_MATRIX_ELEMENT / NO_RATE / NO_DEPOSITION / NO_PBH_BBN_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# DAX-S8 ROT009 — Frame-typed collider cuts and XH-S5 source response for R68

11 November 2026. Object: exact **on-shell kinematics** of real gamma gamma -> e+e-e+e-, NOT a QED amplitude, total cross-section, true phase-space distribution, native MadGraph or physical PBH/BBN result. DAX-S7 R68 FIRST owned DPP differential-energy versus rate problem; ROT001-008 first-owner results retained. ROT009 is a **frame-transfer nonmap**, not a claim of novel physics.

## Material new currentness: XH-S5 has ACKNOWLEDGED DAX source contact

XH-S5 ROT011 response to DAX-S8 ROT006 is confirmed in Slack https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1794351988255089 , and in pinned public source https://github.com/wmakiela-tech/Nash-iw-research/blob/e6cbde9ed2e03f6a0f572acefcffef9d5f66be49/research/xh-s5/2026-11-10/iw_xh_s5_rot011_dax_r68_mg5_full_mass_source_contact_and_first_moment_orbit_gate_001.md . Earlier 'owner receipt unknown' was true at earlier search cutoffs but is now **superseded**; no duplicate request or inferred scientific acceptance.

XH-S5 verified the official MadGraph5_aMC@NLO original source at commit a5b17913ef0b6e1c872016f94d0fb610207dab47: sm/parameters.py has external electron mass Me=0.000511 GeV, sm/particles.py points to Me, BUT sm/restrict_default.dat freezes MASS[11]=0. Default restricted sm cannot safely be made massive merely by a later parameter-card edit. Candidate native preflight is import model sm-full, then verify the actual generated electron mass, identical-electron exchange and full 4e amplitudes. XH ran source-level and non-QED exact/sampled kinematic controls; NO native MadGraph or true QED event generator was executed.

## Primary source domain

Sotsky 2006 https://arxiv.org/abs/hep-ph/0604020 full arXiv text opened 2026-11-11. Its collider gamma gamma calculation uses COM energies (60–2000 GeV) and a Table with minimum energy of any final particle 1 GeV, minimum polar angle 7 degrees, minimum separation between any final particles 3 degrees. This paper does not provide a bath-laboratory acceptance function for R68. A cut in collider COM and a cut applied with the same number in the bath lab are different requirements.

ROT007: four outgoing COM lepton energies >=1 GeV imply W=sqrt(s)>=4 GeV. For R68 and epsilon/T=1,2.701178,10 (strict head-on), W=0.6703,1.1016,2.1196 GeV, hence COM-cut event measure exactly zero. ROT008: for the separately declared CRPropa **scalar** DPP cross-section model with Planck and isotropic collision weights, fraction of collisions with invariant W>=4 GeV in [1.0399758179776226e-14,1.0400568591054100e-14]. Both retain validity as source-typed **COM/invariant-W** constraints. They are NOT bath-LAB per-track energy acceptance rates.

## Exact all-four-lepton positive-mass kinematic witness

Use c=1 and all energies in MeV. Incoming real photons k1=(E,0,0,E), k2=(eps,0,0,-eps), E=1436554, eps=0.07818527068831995, m=0.51099895. Total P=(E+eps,0,0,E-eps), s=4E eps, W=2 sqrt(E eps), threshold W>4m is satisfied.

In COM choose four outgoing on-shell e-/e+ four-momenta with equal E*=W/4, pz*=0, and transverse momenta (+pT,0),(-pT,0),(0,+pT),(0,-pT), with pT² = W²/16-m²=E eps/4-m²>0. Sum is exactly (W,0,0,0). Every polar angle is 90 degrees; every pairwise opening angle is 90 or 180 degrees. Therefore for this witness the collider angular cuts in COM are passed.

Boost to bath lab with beta=(E-eps)/(E+eps), gamma=(E+eps)/W. Outgoing leptons become p1=(L,+pT,0,Z), p2=(L,-pT,0,Z), p3=(L,0,+pT,Z), p4=(L,0,-pT,Z), with L=(E+eps)/4 and Z=(E-eps)/4. EXACT rational identities:
- L²-Z²-pT²=m² for each lepton.
- Sum p_i=P, including transverse cancellation.
- E_i*=W/4=167.568913695521683 MeV (fails **COM** >=1 GeV each).
- E_i^lab=L=359138.5195463176720799875 MeV =359.1385195463 GeV (passes **LAB** >=1 GeV each).
- Each LAB polar angle atan(pT/Z)=0.026733270636609414884 degrees (fails **LAB** 7-degree cut). The source's COM angular cut does not imply LAB angular acceptance.

The witness is physical on-shell phase-space geometry but no QED event weight, cross-section or assertion of nonzero squared amplitude at this exact point was calculated. Falsifies any *untyped* transfer of the numerical per-particle energy threshold between COM and bath lab. DOES NOT falsify ROT007/ROT008 COM-domain results.

## Separate, exact LAB 7-degree necessary all-event condition

If ALL four outgoing bath-LAB tracks have polar angle theta_i >= theta0 relative +z, with 0<theta0<90 degrees, then p_iz<=cos(theta0)|p_i|<=cos(theta0)E_i. Sum via total momentum:
E-eps <= cos(theta0)(E+eps), hence
eps >= E (1-cos theta0)/(1+cos theta0) = E tan²(theta0/2).

This bound is independent of the outgoing energy-sharing distribution, masses or amplitude, and does not assume our symmetric witness. For theta0=7 degrees and R68:
- bath epsilon minimum to pass **COM** >=1GeV-per-track is 2.784441100021300974 MeV =35.6133716172868 T.
- bath epsilon minimum to possibly pass **LAB** all-track >=7-degree polar cut is 5373.956164695042418 MeV =68733.61334410337 T.
- thresholds ratio 1929.99455605433.
- At eps=T, an absolute upper bound on the minimum LAB polar angle across all outgoing tracks is acos[(E-eps)/(E+eps)]=0.0267333949386254143 degrees, far below 7 degrees. Thus with eps=T NO on-shell 4e event can pass an **all-track LAB 7-degree** cut.

This stronger LAB bound has a DIFFERENT frame meaning from Sotsky's original COM angular cut. It is not evidence that the QED physical DPP rate is zero. The thermal Planck photon-number tail for eps/T about 68733.6 is enormously small (leading-log10 ~ -29841.34), but is NOT an interaction-rate or deposition bound.

## Reproduction and limitations

Pure stdlib Fraction performs exact p_i²=m², 4-momentum sum and domain checks. Independent mpmath 82-digit boost, two angular algebra forms, and separate stdlib float negative/positive controls pass. An 8-member local research bundle (report, main reproducer, independent stdlib check, frozen JSON, source audit, README, verifier and SHA256 manifest) has ZIP CRC and 7-member content SHA + clean rerun verification. Details in original local package; no external source QED runtime included.

SCIENCE RETURN: COM_SOURCE_CUT_PASS / UNTAGGED_FRAME_TRANSFER_FALSE / LAB_ANGULAR_ALL_EVENT_NECESSITY_PASS / XH_SOURCE_CONTACT_ACKNOWLEDGED / FULL_MASSIVE_UNCUT_QED_RUNTIME_STILL_OPEN. Native massive generator remains with acknowledged XH source owner; DAX target-level R68 application awaits full QED normalization, mass and first moments. No new source-owner task, no claimed BW receipt, no automatic cascade.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE.
