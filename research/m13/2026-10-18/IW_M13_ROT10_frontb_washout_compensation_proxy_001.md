# M13 ROT10 — neutron endpoint washout or compensation gate

RETURN_ID: M13-ROT10-FRONTB-MECHS6-TRAJECTORY-TO-ENDPOINT-WASHOUT-OR-COMPENSATION-AND-PROXY-DEPENDENCE-001_20261018
DATE: 2026-10-18
RESULT: exact conditional application of LT4 Ch.6 Th.6.6 to Mech-S6 Wu-Xu v2 two-map diagnostic. No BBN/physical endpoint; no novelty.

Mech-S6 reports delta X_n(t*) approximately -0.0728514990 at t*=5.06095 s and reduced Y proxies 1.3230817938392783 (current) and 1.3177406564166434 (charge symmetric), Y=2X/(1-X).

Exact inversion X=Y/(Y+2):
X_current=0.39814903030438903756;
X_repaired=0.39718012734602391457;
delta_end=-0.00096890295836512298.
The proxy delta Y=-0.0053411374226349 is exactly 2 delta X/[(1-X_current)(1-X_repaired)]; it is not a second independent endpoint measurement.

For two realized directional-rate histories x_i'=(1-x_i)A_i-x_i B_i, with R_1=A_1+B_1>=0, let delta=x_1-x_0, W=(1-x_0)(A_1-A_0)-x_0(B_1-B_0).
Then delta(T)=exp(-D)delta(t*)+I with D=int_{t*}^T R_1, I=int_{t*}^T exp[-int_s^T R_1]W(s)ds.
For the Mech-S6 numbers delta(t*)=-p, delta(T)=-d, p=0.0728514990, d=0.00096890295836512:
I=p exp(-D)-d.
Threshold Dcrit=ln(p/d)=4.320013927229. If I<=0, necessarily D>=Dcrit. If D<Dcrit, necessarily I>0 (opposing weighted forcing). If D>Dcrit, I<0. No actual D or I computed, hence neither physical mechanism established.

Claim ceilings: exact host identity and arithmetic, conditional on actual 2-state full directional rate representation; no full-network Yp, D/H, PBH bound, low-mass source validation, independent solver rerun, canon, EXEC_SIGN, novelty or task cascade.
Mech result: https://github.com/wmakiela-tech/Nash-iw-research/blob/c133d23cd96d94e3d8d349b5c6364ae342d21efc/research/mech-s6/2026-10-18/mech_s6_frontb_wuxu_charge_map_dynamic_comparator_result_001.md
LT4 source: https://docs.google.com/document/d/1cn97_kO65BcJRRWQrvrL9fKlEYBT3PHg6BJItn1Q4FQ/edit
Complete local MD SHA256 24176803768ac075f9f43040c7659458bdcea8aa60bc412d32a21b3ff8748e63.
REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD / NO_NEW_TASK.