# MT13 Front B: state interaction, proxy curvature and global precision gate
Date: 2026-10-23. RETURN_ID: MT13-FRONTB-2X2-STATE-READOUT-PRECISION-GATE-001_20261023
SCIENTIFIC STATUS: independent exact four-cell recomputation from MECH-S6/S7 reported values. No new Julia solve, no source-valid PBH/BBN endpoint, no novelty, no CANON/EXEC.

SOURCES:
MECH-S6 https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s6/2026-10-19/mech_s6_frontb_wuxu_source_law_x_charge_map_2x2_dynamic_comparator_001.md
MECH-S7 https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-22/mech_s7_frontb_common_background_target_gate_002.md
Four source-reported reduced helium PROXY Y=2X/(1-X), X=Xn(Tnuc), rows law=public/paper, columns B=exec/sym:
Y00=1.3230817938392783; Y01=1.3177406564166434; Y10=1.3229769529861870; Y11=1.3178103739910758.
All Y>1: NOT physical helium abundances. Xij=Yij/(Yij+2).

EXACT THEOREM: Define x=X00, a=X10-x, b=X01-x, c=X11-x, d=1-x; Ix=c-a-b, Iy=Y11-Y10-Y01+Y00. Then EXACTLY
Iy=(2/d^2)*Ix+(2/d^2)*(c^2/(d-c)-a^2/(d-a)-b^2/(d-b)).
Proof: phi(x+h)-phi(x)=2h/[d(d-h)] with phi(x)=2x/(1-x). Subtract tangent term (2/d²)h, yielding exact remainder 2h²/[d²(d-h)]; take the mixed finite difference. Signs of individual conditional law effects are preserved by any strictly increasing phi; signs of mixed interactions are NOT generally preserved (counterexample x00=.20,x10=x01=.21,x11=.22 gives Ix=0, Iy=0.000811424862>0).

50-digit decimal independent results from four printed Y cells:
Ix=+3.16556977854786243e-5
Iy=+1.745584275237e-4
phi'(x)*Ix=+1.74784918989837284e-4
curvature remainder=-2.26491466137284334e-7 (=-0.129751% of Iy).
Conditional source-law effects in X: exec=-1.89885665743214338e-5; sym=+1.26671312111571905e-5. Thus the source-law sign reversal is present in STATE X, and the nonlinear readout accounts for just -0.13% correction to proxy interaction. This does not certify physical source validity or solver accuracy. IX differs slightly from MECH-S6's full precision because we inverted printed rounded Y.

MECH-S7 fixed-T conditional interaction decomposition (rounded source numbers):
common background = +2.724384e-5 (86.06%);
background-choice contribution=+3.858770e-6 (12.19%);
replay residual contribution=+5.530804e-7 (1.75%);
sum=+3.16556904e-5. Algebraic percentages only, NOT statistical/physical uncertainty budget; replay residual is NOT a bound on Julia global errors. Same-a readout is a different target.

RIGOROUS ENDPOINT NUMERICAL ACCEPTANCE: if each calculated Xij at SAME Tnuc has an independent certified absolute global error <=eps_X relative to each frozen-executor exact trajectory, each conditional law contrast has error <=2eps_X and Ix has error <=4eps_X. Both opposite signs are guaranteed if eps_X < min(|DeltaX_exec|,|DeltaX_sym|)/2=6.33356560558e-6. Positive Ix guaranteed if eps_X<|Ix|/4=7.91392444637e-6. The combined sufficient bound is eps_X<6.33356560558e-6. THIS IS A SPECIFICATION; NO CURRENT GLOBAL SOLVER CERTIFICATE HAS PASSED IT. Nominal reltol/abstol and bit-exact replication are not global endpoint bounds.

Fixed-T conditioning: if exact T(eta) monotone |T'|>=m_T>0, |X'|<=L_X, approximate functions have uniform errors eps_state and eps_temp, and target found as That(etahat)=Tnuc, then |Xhat(etahat)-X(eta_star)|<=eps_state+(L_X/m_T)eps_temp. For actual linear interpolation in Q/T add eps_interp. Need all three errors certified with sum <6.33356560558e-6 per run, based on frozen common background and accepted-step source-active terminal window M<1e9g. No such m_T,L_X/solver/interpolation certificate exists yet.

HOST SUBTRACTION: these are standard rational-function finite differences, coordinate monotonicity and inverse-function Lipschitz stability. New scoped project utility is exact numerical separation of state, readout and saved-background contributions plus a quantified source-native precision gate. It does NOT establish published Wu-Xu-run genealogy, source-valid hadronization, modern Yp/DH likelihood, new exclusion, mathematical novelty, CANON or EXEC. No new task cascade. LT5 owns monograph; MECH-S7 source run; Rec10 independent review; KN11 BW qualification pending.
