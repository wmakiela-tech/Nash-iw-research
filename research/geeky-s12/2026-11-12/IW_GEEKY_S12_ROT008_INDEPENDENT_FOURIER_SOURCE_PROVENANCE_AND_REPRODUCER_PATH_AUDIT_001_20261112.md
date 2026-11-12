---
artifact_id: IW_GEEKY_S12_ROT008_INDEPENDENT_FOURIER_SOURCE_PROVENANCE_AND_REPRODUCER_PATH_AUDIT_001_20261112
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
date: 2026-11-12
exposure: PUBLIC
result_class: INDEPENDENT_FLOAT64_SOURCE_FOURIER_REGENERATION_25_COEFF / SOURCE_SENSITIVITY_NEGATIVE_CONTROLS / REPRODUCIBILITY_DEPENDENCY_PATH_AUDIT
science_status: AUTHOR_CROSS_IMPLEMENTATION_NUMERIC_PASS / ORIGINAL_DIRECTED_INTERVAL_REGENERATION_NOT_RUN / INDEPENDENT_REFEREE_PENDING / M14_OWNER_ADOPTION_PENDING
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: M13_N41_FUNCTIONALLY_MATCHED_FIVE_MASK_CHANNEL_B_AUXILIARY_ONLY / NO_HISTORIC_RUNTIME_IDENTITY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT008 — niezależna kontrola 25 współczynników źródłowych Fouriera M13 oraz ścieżki odtwarzania

## 0. Wynik i rodzaj dowodu

Wszystkie 25 opublikowanych oryginalnych współczynników kwartycznych g_B,k(alpha), k=2..6, N=41, odpowiada niezależnie zaimplementowanej numerycznie źródłowej rodzinie Fourier-Lie-filtr-TT. Odtworzenie jest źródłowo niezależne kodowo od mpmath/iv i od oryginalnej implementacji okna maski M13. Jej algorytm sumuje jawnie skończone wartości zespolone po wszystkich punktach każdej jednowymiarowej maski [k,N-k), a następnie używa iloczynu okien w trzech współrzędnych.

Wyniki na oryginalnym zamrożonym M13 direct_B.json (immutable Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0):

- 25/25 coefficients compared to original directed interval MID: PASS at declared relative tolerance 1e-10;
- maximal Float64 relative discrepancy: **6.236254620051561e-13**;
- maximal absolute discrepancy: **7.108583389127582e-26**;
- K_B(alpha) sparse mode sets at alpha=0,+1,-1: 41 retained mode labels in reconstructed U,V,W;
- negatively perturbed mask k->k+1: max relative discrepancy **6.160842363030505**, negative sensitivity control PASS;
- 1% perturbation of C1_x sine amplitude only: max relative discrepancy **0.026869889032955025**, negative sensitivity control PASS.

All these are Float64 comparisons, NOT proof that raw trigonometric coefficients lie within the 45-digit source mpmath.iv directed intervals. The already proved downstream exact rational interval inequalities of ROT004–007 continue to rely on M13's ORIGINAL frozen directed coefficient table and are NOT rebranded as independently directed-certified by this ROT008.

The material return is an independently executed FUNCTIONAL SOURCE MATCH across all 25 five-mask coefficients, plus one precise reproducibility dependency-path issue; it is NOT a new mathematical theorem, historic byte recovery, or physical inference.

## 1. FIRSTNESS and precise frozen operator

Original M13/MT13 firstness preserved. M13 ROT23,32,33 reconstructed source formulas and historical RMS controls, M13 ROT35 covariance/shell weights, M13 ROT39/40 earlier mathematically certified profile geometry and A/C universal radial results. Geeky-S12 ROT004/005/006/007 own separate fixed-source B nearest-endpoint certificates and falsifiers. ROT008 does NOT claim new origination of Fourier operator, fields, or M13's direct_B coefficients.

Source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json

Original generator code:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-24/verify_m13_rot33_interval.py

Source snapshot script:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/source_snapshot_ch.py

Frozen N41 fields:
C1=(.05sin x,.05cos y,0), C2=(.04cos z,0,.04sin x), h=.1sin x cos y I_3 (AMBIENT pure trace).
Centered stencil first derivative D_N(m)=i sin(2pi*m/N)/(2pi/N).
Linear filter E_alpha(m)=1+2alpha SUM_j [cos(2pi*m_j/N)-1].
Covariant tensor Lie derivative, commutator vector field [C1,C2] and flat Fourier-TT projection P_m=I-mm^T/|m|² for m nonzero (trace removal at m=0).
Channel B K_B=P_TT(L_C1L_C2h-L_C2L_C1h-L_[C1,C2]h), with L_C=Lie_C after E_alpha.

The independent JS implementation holds each Fourier coefficient as an explicit pair (re,im); it evaluates K_B at -1,0,+1, then recovers polynomial tensors U=K_B(0), V=[K_B(1)-K_B(-1)]/2, W=[K_B(1)+K_B(-1)]/2-K_B(0). It calculates the 5 quartic coefficients from masked inner products:
g(alpha)=<U,U>+2alpha<U,V>+alpha²(<V,V>+2<U,W>)+2alpha³<V,W>+alpha⁴<W,W>.

**Independent mask algorithm:** for integer q and k, directly sum
  window(q,k)=(1/(N-2k)) SUM_(j=k)^(N-k-1) exp(i q j*2pi/N).
Cross-modal tensor inner products use 3 factors window(m_j-n_j,k), then their complex Hilbert-Schmidt products and /6. The M13 original uses an analytically equivalent complement / trigonometric sum, but the numerical implementations are genuinely different.

The comparison with M13's file uses the original coefficient interval MID values read from that separate public source body, not hardcoded expected coefficients. The numerical discrepancies are explicitly reported by coefficient mask and alpha power in the JSON. This is a source-provenance sanity check rather than high-precision proof.

## 2. Negative-controls evidence and limitations

SOURCE-PERTURBATION controls were computed by actually rerunning the independent published verifier:
1. Change all comparison mask window sums to [k+1,N-k-1], leaving M13 source coefficients unchanged. Largest relative mismatch becomes 6.16084236, not 6.2e-13.
2. Change ONLY amplitude of C1_x sine by +1% in independent Fourier source, leaving source expected values unchanged. Largest relative mismatch becomes 0.02686989.

Both negative checks distinguish a correctly typed operator input from actual alternate operators, so a mistaken field or mask would not trivially reproduce the source file within tolerance. They are falsifiers of the test setup, NOT legitimate empirical physical perturbations.

No original historic DTC0a producer byte identity, source-native physics output, TT geometric upgrade, measured covariance, noise calibration or mathematical novelty follows. The comparison is at Float64 (~13 significant digits) and cannot in itself prove that original 45-digit coefficients were rounded soundly.

## 3. Source snapshot reproducibility defect — safe limited repair

The M13 script research/m13/2026-10-26/source_snapshot_ch.py contains the import line:

    from verify_m13_rot33_interval import tensor_polys,quartic

But verify_m13_rot33_interval.py is published in research/m13/2026-10-24, NOT the snapshot script's 2026-10-26 directory. Normal Python process startup adds the executing script directory, not an unrelated dated sibling directory. Therefore when the repository is cloned as published and no PYTHONPATH is set, a direct run of the snapshot script encounters a missing-module import gate. This is a static code/package dependency observation, not an executed traceback and not evidence of wrong mathematics.

A safe **suggested, not executed** regeneration method from the cloned repo root, with Python3 and mpmath==1.3.0 installed (POSIX shell):

    mkdir -p /tmp/m13-replay-B
    cp research/m13/2026-10-26/source_snapshot_ch.py /tmp/m13-replay-B/
    PYTHONPATH="$PWD/research/m13/2026-10-24" \
      python /tmp/m13-replay-B/source_snapshot_ch.py B

This writes to TEMP /tmp/m13-replay-B/direct_B.json and does not overwrite M13's original file. If the source computation succeeds, compare original vs regenerated table:

    diff -u research/m13/2026-10-26/direct_B.json /tmp/m13-replay-B/direct_B.json

This plan was not executed in ROT008; no full original high-precision recomputation is claimed. The action to change M13 source layout or adopt a portable wrapper belongs to M14 or authorized owner. ROT008 publishes this bounded documentation repair as an audit finding only.

## 4. Public executable body, source readback, status

Original immutable directed source input: Git blob SHA a6f50fbe5904e580e84c87ee87c5ad043cdec5d0.

ROT008 independently authored full pure-stdlib Node.js source verifier, with optional offline M13 direct_B.json input and default Git API immutable blob fetch with byte-exact Git SHA check:
https://github.com/wmakiela-tech/Nash-iw-research/blob/09285e146348a66ae3d3e8593b629707acf4875d/research/geeky-s12/2026-11-12/iw_geeky_s12_rot008_independent_complex_fourier_mask_25_coeff_reproducer.js
Git code blob 9b8d6fa1bbb87b74f5b0ad26aa76c58fb184e21c. WRITE and exact full-body FETCH READBACK PASS.

ROT008 machine-readable output from independently executed 25-coefficient comparison plus both negative-controls, original source and code blob identities, static path-gap and staged import correction:
https://github.com/wmakiela-tech/Nash-iw-research/blob/23b436252f0d49132d520c8e30b2b67b60fdb7b7/research/geeky-s12/2026-11-12/IW_GEEKY_S12_ROT008_INDEPENDENT_B_SOURCE_CROSSRUN_25_COEFF_RESULTS_001_20261112.json
Result JSON blob 3d836229326815297536b7c5306efff7f26e76b6. WRITE and exact full-body FETCH READBACK PASS.

To avoid an unsupported execution claim, the exact verify(source) mathematical body was extracted FROM PINNED PUBLIC BYTES and actually reexecuted inside the connected JavaScript tool against freshly fetched frozen source M13. All three cases PASS. The Node-specific network/CLI loader wrapper was NOT separately executed in a Node host. The original M13 high-precision source_snapshot_ch.py was NOT executed, so the independent 25-coefficient agreement is not upgraded to formal source-directed regeneration.

A bounded check of public #iw-dispatch as of Nov 12 afternoon did NOT find a separate independent REC11/AUD1 verdict or M14 owner adoption for Geeky ROT004–007. Such actions must be independently read, not presumed from dispatch. KN13 BW custody is unverified.

## 5. Bounded interpretation

ROT004 all-delta B nearest-only FAIL retained; ROT005 fixed delta=.01 PASS retained; ROT006 all delta<=.020 PASS and delta=.026 fail retained; ROT007 all delta<=.025 PASS, delta=.02514 fail and 3-candidate global reduction retained. The new cross-implementation test gives those conditional source coefficients an independent numerical provenance check, NOT a replacement proof of ROT007's exact rational interval Bernstein positivity.

Next actual scientific source gate: M14 and independent referee may (i) authorize a clean staging replay of original M13 source snapshot with the corrected PYTHONPATH, and (ii) independently review all interval steps defining Q,R,P,F0 in ROT007. No more threshold-point refinements absent source/referee input. STOP new toy theorem factory.

FINAL:
INDEPENDENT_FLOAT64_SOURCE_FOURIER_MASK_25_OF_25_ALIGNMENT_PASS /
TWO_NEGATIVE_SOURCE_PERTURBATION_CONTROLS_PASS /
STATIC_SNAPSHOT_PYTHON_DEPENDENCY_PATH_REPRODUCIBILITY_HOLD /
SOURCE_DIRECTED_INTERVAL_REGEN_NOT_RUN /
HISTORIC_PRODUCER_HOLD / REFEREE_PENDING / M14_OWNER_ADOPTION_PENDING /
BW_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
