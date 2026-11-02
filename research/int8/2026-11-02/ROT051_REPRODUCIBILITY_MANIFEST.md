# INT8 ROT051 — exact complete H(z) kernel N7/N9, original-source fidelity and SHA custody

ORIGIN: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
DATE: 2026-11-02
ARTIFACT ID: IW_INT8_ROT051_STABLE_FILTER_DARK_Z_FIBERS_001_20261102
EXPOSURE: PUBLIC
SYNC: GITHUB_PENDING_BW_INGEST
CLAIM CEILING: EXACT STABLE FILTER DARK FIBERS, FULL H(z) KERNEL ONLY N7 AND N9 / NO CANON / NO EXEC / NO NOVELTY / NO PHYSICAL UPGRADE

## GitHub files — actually read back

1) Scientific report: iw_int8_rot051_exact_stable_filter_dark_fibers_full_z_kernel_001.md. Git blob 62b76c9575785737ae43f6a9dbdc209c36cd2725. Full source type and exact T051.1–T051.4.
2) Complete original independent EXACT SymPy/stdlib modular rank program: audit_int8_rot051_exact.py. Git blob ef55bfd95b0761ad0411734619b91855105e80cd. BYTE-IDENTICAL to full frozen local executable, SHA256 52b4dc9861a41dddbac07d69ee2d96dd0295c0d0f97c3d5c2c5cb20803e6ac77. Does NOT import NumPy or original DTC0a. Run:
   python audit_int8_rot051_exact.py --out exact_results.json
Output: EXACT_CYCLOTOMIC_MODULAR_PASS, 2 exact root-of-unity identities, 9 exact modular rank witnesses, 7 nonzero 6x6 minors on all positive z harmonic classes at N7/N9. Proof via irreducible polynomials of 2cos(2pi/N), F41 root14 and F53 root4. Output exposes witness minor row indices and nonzero residues.
3) Separately locally EXECUTED original-source native minimal program: public_source_int8_rot051_dark_fibers.py. Git blob a9fb65f5df4b8fba18d21bac2d86c56991e38483; SHA256 e07b06e9527d57f9d4adc4d4c7f08786e89bd06d1108bf0186464e39bc965f3d. Independently checks all 6 real Sym2 bases times cos/sin in both dark N7/9 sectors; nonzero first projected original tensor is then killed by second original E; near-alpha .05 restores nonzero result. Requires NumPy and the USER-RETAINED original unchanged helper file:
   OPENBLAS_NUM_THREADS=1 python public_source_int8_rot051_dark_fibers.py --source /your/path/deepseek_python_20260627_a87249.py
Original helper SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801; script rejects unverified bytes. Original helper NOT redistributed.

## COMPLETE frozen original 8-file Moderator-local ZIP, independently tested

Name: iw_int8_rot051_exact_stable_filter_dark_fibers_bundle.zip
SHA256: 09520c69380dbb25f233379230fc420a833ccc08aeb3216b4049a2a5f5ce914d
ZIP CRC PASS, 7/7 member SHA256 PASS.

| Original ZIP payload file | SHA256 |
|---|---|
| README.md | 53c2d303c908b5fc4e43881021817e88728126346e91240377e3b6bc157c5331 |
| RUNLOG.txt | 496b25b212f91a3002691bb25cad61845c52ab2a4beec0ecb8a3f62e184d92c9 |
| audit_int8_rot051_exact.py | 52b4dc9861a41dddbac07d69ee2d96dd0295c0d0f97c3d5c2c5cb20803e6ac77 |
| exact_results.json | d6cbde76599e7e71cb802a95021a1b0a6ed555b7b994ff2248435112c2608923 |
| iw_int8_rot051_exact_filter_dark_fibers_complete_z_kernel_report.md | c7b869c76c3e32e558a717a256b24c3d7a57c9627f97b1598a536946c08ef185 |
| main_results.json | 7c70d8793c23e3d0c4fd4fc38aca2feecae7884308d2f5abf7ce2fe594886a05 |
| reproduce_int8_rot051.py | 7b9ae755c7e2bee81ca546188ee6cdf7f1399805d99c09237336422492ffdcd0 |
| SHA256SUMS | contains the seven SHA256 above, verified |

The ORIGINAL complete NumPy/Fourier 150-case program and complete original source-result JSON reside in ZIP; not falsely asserted separately uploaded to GitHub. Public exact program is the complete frozen original; public source-native program is a separately locally executed minimal witness.

## Clean replay actually completed

- CLEAN_A new ZIP extraction with byte-SHA verified original DTC0a helper: main JSON and exact independent JSON BYTE IDENTICAL to originals.
- CLEAN_B separate clean ZIP extraction with the same byte-SHA verified helper: both JSON BYTE IDENTICAL.
- CLEAN_C fresh ZIP extraction without original source: independent exact JSON BYTE IDENTICAL, all 150 mathematical Fourier block records and mathematical dark fiber entries exactly equal; main source status properly SOURCE_SKIPPED_NO_HELPER and no native source cases. No false native source PASS.
- 36 original full-grid source compute_K_A_out cases in frozen main run, 2 original intermediate source E annihilation checks.
- 150 floating 6D fiber spectral tests at N7,9,11,15,21,31 and alpha0,.05,1/6 (some rank observations at N>=11 remain NOT EXACT CERTIFIED).

NEGATIVE KNOWLEDGE: initial N9 ell4 finite-field choice F37 root5 yielded rank5 (unhelpful specialized lower rank), NOT a real source counterexample and not proof. The independent final F53 root4 rank6 has an actual nonzero minor46, with explicit row indices, certifying the REAL algebraic rank.

## Strict scope STOP

Theorem for ALL stable odd N>=7: intermediate e_shell factor can vanish ONLY N7 ell±3 alpha1/7 or N9 ell±4 alpha1/6. Complete REAL K_A_out kernel dimension 3 ordinarily/15 at spectral-dark parameters PROVED ONLY ON N7 AND N9 H(z) (all six tensor polarizations; no x,y dependence). N>=11 geometry core full rank is not proven; no generic-3 kernel assertion there.

Only the literal original AUXILIARY unmasked compute_K_A_out with centered derivative and RAW-k TT. Not full original historical production dtc0a_runtime_v0_3_1.py (byte unavailable), masked h=fI K_A, mask RMS, even-grid Nyquist, curved York, GR gauge, physical J3/K, Noether/GW energy or experimental anomaly. BW actual ingestion, independent referee, source owner adoption and Moderator EXEC remain unverified. NO NEW TASK CASCADE.
