---
artifact_id: IW_REC11_ROT034_KN14_ROT002_ORIGINAL_WUXU_NATIVE_MASS_CUBIC_CHEBYSHEV_CLOCK_REFEREE_001_20261113
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-13
source_class: I1_NONBLIND_INDEPENDENT_ACTUAL_NATIVE_BINARY_SOURCE_EXACT_RATIONAL_REFEREE
status: PASS_KN14_SOURCE_INVARIANT_DRIFT / NEW_SHARP_FOUR_POINT_CHEBYSHEV_TIMESTAMP_LOWER_CERTIFICATE
ceiling: ORIGINAL_J22_10000_SAMPLE_DENSE_INTERPOLANT_ONLY / NO_NEW_JULIA / NO_SOLVER_ERROR_BOUND / NO_PBH_BBN_PHYSICS / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
owner_ack: UNVERIFIED
bw_receipt: UNVERIFIED
---

# REC11 ROT034 — Ostra czteropunktowa granica niezgodności zegara sześcianu masy w oryginalnym Wu–Xu

## 1. Pierwszeństwo i zakres recenzji

**KN14 ROT002 jako pierwszy** niezależnie wykrył na oryginalnym natywnym wyjściu Julia dla j22, że estymatory stałej utraty masy `C` w dwóch rozłącznych oknach różnią się o `−0.6105193519359677%`. Oryginalny model należy do autorów Wu–Xu; **Mech-S9 ROT012/013 pierwszy** wykonał natywny autorowski `magic()` i zachował 10 000 próbek. Odrębne źródłowe pierwszeństwo PRF13 ROT017 dotyczyło prawa M³ oraz liczby hadronów emitowanych spod dolnego węzła tabeli.

KN14 ROT002 raport pierwotny (odczytany bezpośrednio, Git blob `b2661237ab865f1d516d4fdef71c888ffbf1f8fb`):
https://github.com/wmakiela-tech/Nash-Priv/blob/1bb84c218cda5f3517f769dc6d5aaa22d4cb91e6/research/kn14/2026-11-13/IW_KN14_ROT002_ORIGINAL_WUXU_NATIVE_MASS_CUBIC_CLOCK_INVARIANT_DRIFT_SOURCE_SUBGRID_AND_B1_NUMERIC_GATE_001_20261113.md

**Nowe REC11 ROT034:** ścisły, OPTYMALNY rachunek minimalnej maksymalnej poprawki czasowej, koniecznej, aby wszystkie CZTERY oryginalne zapisane punkty mogły leżeć na jednym dokładnym zegarze `M³+3Ct=const` przy niezmienionych masach; niezależne wyznaczenie optimum za pomocą (a) certyfikatu dualnego i (b) enumeracji 32 trójek ograniczeń liniowych. To klasyczne aproksymowanie Czebyszewa, nie twierdzenie o nowej fizyce.

## 2. Autentyczność kodu i rzeczywistych danych

Oryginalny autor Wu–Xu `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d` był bezpośrednio odczytany w tym obrocie:
- `arXiv-2509.05618/main-scan.jl`, original Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`: oryginalne `d_m_PBH_dt = -N_PBH * NU.m_Pl^4 / m_PBH^2` w wierszu 80; przełącznik po wyparowaniu; `evolution_solution=solve(...,AutoTsit5(Rosenbrock23()))` w wierszu 177; próbki `results_list=(evolution_solution ∘ log).(geomspace(...,10000))` w wierszach 179–184. Zapisane obserwacje są **próbkami gęstego interpolantu rozwiązania ODE**, nie udokumentowanymi wewnętrznymi zaakceptowanymi krokami.
- `arXiv-2509.05618/tool_script-parameters.jl`, original blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`: `N_BH(T_BH)=(27/4) Nᵨ(T_BH)/(30720π)`, `T_BH(m)=NU.M_Pl²/m`.
- `arXiv-2509.05618/tool_script-N_relativistic_species.jl`, original blob `0437c032bdc4bafca6cb634c0db4cd2c46fb7efc`: ponad-tabelaryczna ekstrapolacja stała dla `Nᵨ(T)`.
- Dwie odczytane bezpośrednio oryginalne tabele wejściowe mają git bloby `28b0c13563d7b3bdeaee191a3a981197345d05b8` i `33aceb876fc36cb2486d36c690e6401d85d76b46`, maksymalny węzeł temperatury `279783.067 MeV` (~279.783 GeV). Dla czterech mas `M∈[1.4489122×10⁸, 1.0939060×10⁹] g` temperatura Hawkinga wynosi około 9.665–72.969 TeV według standardowego wzoru termodynamicznego, zatem wszystkie leżą ponad ostatnim węzłem temperatury, zgodnie ze źródłowym założeniem stałego `N_BH`. Rachunek temperatur jest niezależną kontrolą wymiarową, nie nowym runem Julii.

**Natywne rzeczywiste wejście (bez podmiany):** Mech-S9 original Actions run `43436800793`, artifact ID `14045176436`, zip **713794 B** SHA256 `71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486`; CSV `author_native_raw_hadron_history_10000.csv` SHA256 `45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1`. Oryginalne ZIP CRC PASS, 16/16 źródłowych SHA wewnętrznych PASS, 10 000 indeksów źródłowych PASS. Wszystkie cztery punkty mają `nPBH_zero=0`, a więc są PRZED source-switch.

| Źródłowy indeks (od 1) | t [s] (dokładny token) | M [g] (dokładny token) |
|---:|---:|---:|
| 8200 | 0.0238548276963661 | 1093905989.08506 |
| 8350 | 0.0754433392575876 | 1029767412.34217 |
| 8500 | 0.238855246398204 | 739689980.046328 |
| 8544 | 0.334927351810113 | 144891220.526512 |

## 3. Exact source invariant and KN14 replay

Under the source high-T constant `N_BH`, the exact model is `dot M=−C/M²`, hence `M³+3Ct=const`, where `C>0` is a single number. Secants computed INDEPENDENTLY using exact standard-library `Fraction` on the original decimal strings:
- 8200→8350: `C_e=1.402212424739247228...×10²⁷ g³/s`;
- 8500→8544: `C_l=1.393651646530963556...×10²⁷ g³/s`;
- `C_l/C_e−1=−0.006105193519359677...`.

This **confirms KN14's original numerical diagnostic**; it does not establish a numerical ODE error mechanism or a physically independent PBH result.

## 4. NEW sharp four-point source-serialized timestamp lower bound

Treat the four saved `M_i` as fixed exact source tokens; allow independent corrections `δt_i` of four saved timestamps and a freely chosen overall epoch plus freely chosen `C>0`. Let

`x_i=(M_i³−M_8200³)/10²⁷`, so `x_8200=0>x_8350>x_8500>x_8544`.

A single exact source clock is equivalent to an affine fit `t_i≈a+b x_i` with `b<0` and `C=−10²⁷/(3b)`. Consider the Chebyshev problem:

`E* = inf_(a∈R,b<0) max_{i=8200,8350,8500,8544} |t_i−a−b x_i|`.

**Certified optimum from exact native decimal rational inputs:**

`E* = 0.000197854784135115095... s = 0.197854784135115095... ms`.

The optimum global `C_opt=1.39941567313862487...×10²⁷ g³/s`, and errors at these four samples, in source index order, are

`(+0.0001978547841351151, +0.00009475442942850975, −0.0001978547841351151, +0.0001978547841351151) s`.

**Exact lower certificate independent of fitting algorithm.** On indices 8200, 8500, 8544 define

`w_0=x_8500−x_8544>0`, `w_2=x_8544−x_8200<0`, `w_3=x_8200−x_8500>0`.

Then `Σw=Σwx=0`, so EVERY affine candidate has

`max_i |t_i−a−b x_i| >= |Σ_(0,2,3)w_i t_i|/(|w_0|+|w_2|+|w_3|) = E*`.

**Constructive equality:** let `b=(t_8544−t_8200)/(x_8544−x_8200)<0`, `a=t_8200−E*`. Exact source arithmetic gives residuals `(+E*, −E*, +E*)` for rows 8200, 8500, 8544 and a STRICT interior residual at row8350, magnitude `<E*`. This establishes the GLOBAL optimum for all `C>0` and epochs. No floating-point search enters the proof.

For comparison, the weaker necessary lower bound obtained by equalizing only disjoint two-window secants (without the full common intercept condition) is `0.000102868784900855362... s` = `0.102868785 ms`; the four-point certificate is strictly stronger. **Do not call the two-secant lower bound a sharp four-point fit.**

The independent second Python script, with a distinct exact rational Gaussian-elimination solver and NO import from the first, enumerated ALL 32 sign/triple active configurations of the `L∞` affine LP: 24 nonsingular and 4 feasible, giving the SAME E*, indices `(8200,8500,8544)` and sign pattern `(+,-,+)`. This is a separate algorithmic check of the analytic dual certificate.

## 5. Status, interpretations, and physics stop

- Both source times and masses are **serialization of a single adaptive ODE and its dense interpolation**, not certified exact continuum physical data. The result is conditional on treating printed masses as fixed and permitting changes to timestamps only. If mass values are also adjusted, it is a different joint error allocation problem; this E* does NOT bound a fully free simultaneous mass+time correction.
- `E*` is NOT a numerical solver-error lower bound in some physical norm. In particular it does not identify whether the discrepancy originates from adaptive stepping, dense interpolant, stopping/switching, source parameter evaluation, or an external numerical effect.
- The physical meaning of original published JCAP Fig5 binary/run identifier, E4 subgrid generator, two rate prescriptions, near-terminal ODE tolerance convergence and source original `X_n(T0)` error remain OPEN. The source one-point `β=1.00586353e-17` is +0.586% above the published original beta scan ceiling per Mech-S9 ROT014, so no claim original scan-grid replication or observational bound.
- Mathematical maturity: the cubic Hawking mass clock is standard, and Chebyshev affine minimax and dual alternation are classical. No original external math novelty, no physics upgrade, no CANON/EXEC_SIGN.

## 6. Execution, reproducibility and routing

Actually executed first independent Python stdlib program `verify_rec11_rot034_mass_clock.py`: source-native provider SHA lock, CRC, all 16 native inner SHA, full 10k original index scan, **exact rational** dual/primal, original KN ratio recheck, JSON/stdout deterministic. Actually executed second independently written `independent_vertex_enumerator.py` with 32 exact triple constraints and independent CSV source parsing, same E*. Five deliberate source mutations rejected (provider byte, duplicate index, mass nonmonotonic, time nonmonotonic, pre-PBH flag), some tested on isolated scientific parser after bypassing the archive verification to check scientific guards separately.

Self-contained local ZIP `IW_REC11_ROT034_KN14_WUXU_MASS_CUBIC_SHARP_TIME_CHEBYSHEV_REPRO_001_20261113.zip` preserves unchanged source native ZIP, both actually executed programs and JSON/stdout, negative test, this report, README, SHA256 manifest. **Verified ZIP CRC PASS, 12/12 payload SHA256 PASS, clean isolated rerun 3/3 JSON and stdout byte-identical PASS, 5/5 deliberately corrupted source controls fail-closed. The outer ZIP SHA256 is recorded outside the archive to avoid self-reference.** This user-local archive is not claimed to be a GitHub/BW blob. External public report is source-typed text, different from locally saved report; exact-byte equivalence to LOCAL is asserted only if independent full Git blob readback passes.

**OWNER TO FOLLOW:** KN14 for numerical invariant custody, Badacz+Mech-S9 for any permission-gated Julia tolerance/step sampling, AUD2 independent science, Moderator for native experiment authorization. New source result does NOT authorize native runs or automatic task cascades. BW/owner scientific acceptance remains UNVERIFIED.

RETURN_ID `IW_REC11_ROT034_KN14_ROT002_ORIGINAL_WUXU_MASS_CUBIC_CHEBYSHEV_SOURCE_REFEREE_001_20261113`.

FINAL `PASS_KN14_ORIGINAL_C_SECANT_DRIFT / PASS_SHARP_4POINT_TIMESTAMP_CORRECTION_0P197855_MS / PASS_INDEPENDENT_EXACT_32_VERTEX_LP / HOLD_SOURCE_SOLVER_INTERNAL_STEPS / NO_PHYSICAL_PBH / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.

## 7. Pinned local reproducibility archive receipt (outside archive to avoid cyclic hash)

Verified complete local ZIP `IW_REC11_ROT034_KN14_WUXU_MASS_CUBIC_SHARP_TIME_CHEBYSHEV_REPRO_001_20261113.zip`: **729204 bytes**, SHA256 **`8496bad91192a9ed63f6ca9e4c7494e40e9b05c2e5ed91e3a3fa236518e5d74d`**; CRC PASS, 12/12 payload SHA256 PASS, 3/3 clean independent JSON and stdout byte-identical replays PASS, 5/5 negative controls rejected. The archived `REPORT.md` does NOT itself contain the ZIP SHA because that would create cyclic hashing. This GitHub report is a distinct source-typed text receipt and does not claim byte equality to archived local `REPORT.md`.
