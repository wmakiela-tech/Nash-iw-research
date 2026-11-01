# M14 ROT024 — NC-NUM-005. Exact classical 2D return (2026-11-01)
owner: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_09 / M14
origin: NC-SUCCESSION-READDRESS-033-QUEUE-001_20261031
status: SOURCE_TYPED / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / BW_PENDING / REFEREE_PENDING

First owners: M13 generator, NC 029 rank-one cycle / pumping, Grok and NC 033 n=2-only restriction and T2 degradation.
Source NC 029: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-24/IW_NC_OPN002_DYCHOTOMIA_MU2_I_BRAK_SKONCZONEGO_SUFITU_029_20261024.md

Let A=[[-11/10,4],[1,-41/10]], eigenvalues (-1/10,-51/10), mu2=-13/5+sqrt(34)/2=0.3154759474. Set alpha=(5+sqrt34)/10, beta=(sqrt34-5)/10, and r(t)=alpha exp(-t/10)-beta exp(-51t/10). This is max over unit w of w^T exp(tA) w. For n=2, Pi=ww^T rank1, radius(exp(tA)Pi)=abs(w^T exp(tA)w). Unique optimum:
tstar=log(51*(sqrt34-5)/(sqrt34+5))/5=0.272846861447588128.
rhostar=(50/51)*alpha*(51*beta/alpha)^(-1/50)=1.033277247747220940.

Choose w top eigenvector sym(A), d orthogonal, repeated interval tstar, initial v0=w, e=d, gamma1. For ideal projection u=0 the j-th measured pulse has abs(c_j)=kappa*rhostar^(j-1), kappa=(3/10)*(exp(-tstar/10)-exp(-51tstar/10))=0.217316079122215343. Thus L2 norm of m measurements is kappa sqrt((rhostar^(2m)-1)/(rhostar²-1)): m8=0.6931601265, m15=1.0796273725, m16=1.1365244818. One-flow M(A)=1.0866135704. This proves repeating growth, but rhostar alone DOES NOT recover NC's finite result 1.0858 (its original schedule/m are not asserted).

FINITENESS: D(u)=ww^T+u dd^T, s=-log(u) finite. ellstar is lower eigenvalue of sym(exp(tstar A)). p_u(1)=1-rhostar+u*(exp(-26tstar/5)-ellstar); ucrit=(rhostar-1)/(exp(-26tstar/5)-ellstar)=0.622014181832007898. At this fixed period/rank1 axis the cyclic map has radius >1 whenever 0<=u<ucrit. Direct finite u=.001 and m16 norm=1.1351906180 >M(A). For n>2 trace formula invalid (NC/Grok first).

Original full Polish report, SymPy+mpmath90 and INDEPENDENT SciPy matrix-exp replay, two JSON in LOCAL archive; CRC PASS, SHA 7/7, clean JSON byte-match PASS. ZIP SHA256 73c87a97a947ddc3cb827e018720db7702360f092d49f713f4a436561301b330. ZIP not claimed GitHub hosted. Unresolved global five-tone Lorentz question from ROT023 remains OPEN. No new math or physical NASH claim.
