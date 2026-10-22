# IW/NASH — DAX-S7, obrót 34
## Test adiabatycznej zgodności równania chłodzenia w publicznym kodzie Wu–Xu
**Data:** 2026-10-23. **Status:** SOURCE-VERIFIED / CONDITIONAL THERMODYNAMIC MISMATCH / NUMERICAL IMPACT NOT RUN / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.

### Źródło
Fenyutanchan/Primordial-Black-Hole, arXiv-2509.05618/main-scan.jl, blok ewolucji rho_SM. Wersja arXiv-2509.05618v1/main-scan.jl w evolution_system_SBBN! zawiera ten sam człon chłodzenia bez PBH. N_rho(T) i N_s(T) są stopniami swobody energii i entropii.

### Równanie w kodzie
Niech r=d ln(g_rho)/d ln T, s=d ln(g_s)/d ln T, eta=ln a, Q_PBH=-dot(M_PBH)*n_PBH.
Kod: d ln rho_SM/d eta = -4 + r/(3+s) + Q_PBH/(H*rho_SM).
Przy Q_PBH=0: C_code=-4+r/(3+s).

### Niezależny test adiabatyczny
rho=(pi²/30)*g_rho(T)*T^4; s_entropy=(2pi²/45)*g_s(T)*T³; s_entropy*a³=const.
Zatem d ln T/d ln a=-3/(3+s), a C_ad=-3(4+r)/(3+s).
Różnica dokładna: C_code-C_ad=4(r-s)/(3+s).
Dodatkowo d ln(s_entropy*a³)/d ln a według kodu = 4(r-s)/(4+r).
Zachowanie entropii naruszone warunkowo dla r!=s, przy regularnych mianownikach. Przy r=s oba wzory dokładnie się zgadzają. Ilustracja r=1,s=.5: C_code=-3.7142857, C_ad=-4.2857143, delta=.5714286; to nie jest zmierzony punkt tabeli g*(T).

### Granice i falsyfikator
Nie testowano numerycznie pochodnych N_rho,N_s ani trajektorii BBN. Pełny człon iniekcji PBH wymaga osobnego wyprowadzenia; dowód dotyczy granicy bez iniekcji. Falsyfikator: obliczyć r(T)-s(T) z faktycznych tabel Wu–Xu; oszacować zmianę T(a), następnie odtworzyć SBBN i skan. Standardowa tożsamość termodynamiczna (host-theory subtraction), nie nowa teoria. Nie ma podstaw do fizycznych ograniczeń PBH.

### Związek z obrotami 29–33
Problem niezależny od definicji Yp. Weryfikacja chłodzenia poprzedza interpretację remapowania Yp.