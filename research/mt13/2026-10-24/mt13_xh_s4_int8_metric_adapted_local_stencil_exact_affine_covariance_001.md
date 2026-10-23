# MT13 — XH-S4 Q43 × INT8: local metric-adapted stencil exactly repairs E_lin on finite affine torus
DATE 2026-10-24
RETURN_ID MT13-XH-S4-INT8-METRIC-ADAPTED-LOCAL-STENCIL-EXACT-AFFINE-COVARIANCE-001_20261024
PROBLEM_ID P3_DTC0A_METRIC_NATURALITY_FILTER_OPERATOR_HOST_001 / XH Q43
CLASS EXACT FINITE-LATTICE CLASSICAL THEOREM / ORIGINAL RETAINED SOURCE HELPER EXECUTED / TT-GEOMETRY AND TWO-SHEAR REPRO PASS
NO NOVELTY / NO CANON / NO EXEC / NO NONFLAT YORK / NO PHYSICAL NASH J3/K / NO ORIGINAL BYTE-EXACT DTC RUNTIME / BW_PENDING.

## Others first; no overlapping priorities
XH-S4 ROT020 derived standard metric-dependent York naturality and raised the unsolved E_g naturality question Q43:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-23/IW_XH_S4_GEOMETRIC_NATURALITY_MOVING_YORK_PROJECTOR_DTC0A_REPRO_AUDIT_020_20261023.md
XH ROT021–024 separately checks genuinely curved metrics and Bianchi/Noether/ordered Duhamel: these are NOT answered here:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-23/IW_XH_S4_OFFSHELL_BIANCHI_DUHAMEL_NOETHER_RESEARCH_024_20261023.md
INT8 ROT019/020 proves exact full-band optimal distance of E_lin to ANY ONE UNIVERSAL FIXED scalar convolution under all integer SL3 shears, tending to 6|alpha|:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/int8/2026-10-24/iw_int8_rot020_sharp_minimax_distance_to_shear_equivariant_dtc_filter_001.md
INT8 explicitly excludes any claim against a metric-adapted operator FAMILY.
LT5 Chapter 4, M13 source recovery and PRF11 high-frequency estimates remain separate established results.

## Source and exact positive theorem (no approximation)
On periodic G_N=(Z/NZ)^3, the ORIGINAL retained user helper deepseek_python_20260627_a87249.py, function apply_E, defines
  E0 h = h + alpha sum_j (tau_ej + tau_-ej -2I) h,
  tau_v h(x)=h(x+v).
Its exact source SHA256:
23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801.
Historical original dtc0a_runtime_v0_3_1.py is still unavailable, so this is source HELPER execution, not original physical runtime replay.

Let A in SL(3,Z), metric g_A=A^T A, covariant tensor pullback U_A h(x)=A^T h(Ax) A.
Define LOCAL METRIC-STENCIL FAMILY
  E_{g_A} = I + alpha sum_j (tau_{A^-1 ej} + tau_{-A^-1 ej} - 2I).
**IDENTITY ON ALL TENSORS, ALL FINITE FREQUENCIES, ALL ALPHA**:
  E_{g_A} U_A = U_A E0.                                      (1)
Proof: tau_{A^-1 ej} U_A = U_A tau_ej and constant A matrices commute with scalar componentwise additions. Each stencil displacement A^-1 ej has g_A-length 1: no extended physical-range convolution is required.

If A'^T A'=A^T A, then A'=R A with R an integer orthogonal signed permutation. E0 commutes with U_R; hence E_g is independent of representation A on this AFFINE FLAT METRIC ORBIT. For B in SL3Z, U_B U_A=U_{A B} and E_{B^Tg_A B}U_B=U_B E_g. Natural family rather than fixed universal kernel.

For the constant-metric Fourier York P_g (covariant rank-2 TT), geometric tensor pullback satisfies P_{g_A}U_A=U_A P_I. Thus
  P_{g_A} E_{g_A} P_{g_A} U_A= U_A P_I E0 P_I.                (2)
No independent nonflat elliptic York solver and no arbitrary diffeomorphism is asserted.

## Exact source-fixed no-go on a GENUINE TT input
Choose A=[[1,1,0],[0,1,0],[0,0,1]] and g_A=[[1,1,0],[1,2,0],[0,0,1]],
H=diag(0,1,-1), h_m(x,y,z)=cos(m x) H, 1<=m<=(N-1)/2 with N odd.
Then h_m is exactly flat TT, U_Ah_m=cos[m(x+y)]H is exactly g_A-TT:
tr(g_A^-1 H)=0 and (m,m,0) g_A^-1 H=0.
The source E0 scalar Fourier symbol is e(k)=1-4alpha sum_j sin²(pi k_j/N).
Old k=(m,0,0), pulled k'=(m,m,0); both TT.
Thus EVEN WITH THE CORRECT MOVING TT PROJECTOR, the fixed E0 gives the exact relative defect
 ||P_g(E0 U_A-U_A E0)h_m||_{L2(g)} / ||U_A h_m||_{L2(g)}
   = 4|alpha| sin²(pi m/N).                                  (3)
The metric-dependent family E_g makes the defect IDENTICALLY ZERO by (1). On fixed m, (3)=O(N^-2); on m=(N-1)/2, (3)->4|alpha|. These are different target quantifiers. This source-specific one-shear TT lower witness DOES NOT equal INT8's universal fixed-filter minimax constant 6|alpha|, so do not conflate them.

## Direct original-source execution and independent geometry controls
Source apply_E(...,E_lin,dx,order=2,alpha=.05) run without modification. All eight exact source TT tests:
N=9 m1 fixed .023395555688 / m4 fixed .193969262079;
N=15 m1 fixed .008645454236 / m7 fixed .197814760073;
N=31 m1 fixed .002047005875 / m15 fixed .199486932339;
N=41 m1 fixed .001171957622 / m20 fixed .199706580118.
All metric-adapted outputs agree with transformed source within 1e-15. Analytic fixed defect (3) agrees within 2e-13.
Independent metric York single-mode projection for special and generic polarizations PASS. Random FULL symmetric tensor N11: adapted relative error 2.2779425e-16. Two distinct unimodular shears compose consistently with the adapted filter within 4e-14; integer signed-permutation E0 stabilizer defect exactly 0.
Local ZIP includes original verified user helper, executable Python, Polish 12KB full proof, JSON, log, manifest/README. CLEAN EXTRACT CRC+SHA VERIFY and RERUN ALL_PASS.
LOCAL ZIP exact SHA256: 7ce86b20e18c4b453cf5c9917af5b23e8cd84b54c40226b3542f16b53b9c5329.

## Owner-science implications (PROPOSED, not claimed accepted)
XH-S4 Q43: AFFINE-FLAT finite-grid source-matched POSITIVE PASS and simultaneous fixed-E negative witness. Q42 nonflat York and Q62-Q68 Noether/off-shell/Duhamel remain distinct and OPEN for this host. XH original role and authorship preserved.
INT8: fixed universal convolution NO-GO and metric-dependent stencil YES coexist; the metric is itself transported, not held fixed, so no contradiction to INT8 ROT020.
M13: helper-matched, not byte-recovered historic K_A on original puretrace h=fI; not a masked RMS / same domain continuum result.
LT5: optional one targeted contrast in Chapter4: fixed-source-stencil obstruction versus transported metric-local stencil PASS on restricted orbit; REV021 remains STAGED.
Geeky-S11/PRF11: no even-N checkerboard or source Nyquist conclusions, no continuum uniform smooth-input claim; affine flat torus only.
NC: research independence and nonblind exposure preserved.
General curved g(x) needs metric connection, covariant Laplacian, York zero-mode/boundary choice, and for exp[B(C)Box_g] correct noncommutative Frechet/Duhamel variations and on-shell stress equations, none supplied here.

NO PHYSICAL NASH K/J3 / NO GRAVITY DISCOVERY / NO NOVELTY / NO CANON / NO EXEC / BW_PENDING / OWNER_ADOPTION_PENDING.