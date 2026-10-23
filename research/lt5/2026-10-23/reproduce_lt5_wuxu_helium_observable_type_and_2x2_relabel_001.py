"""LT5 ROT10: observable-type transformations of four MT13 printed diagnostic outputs.
This is solely decimal algebra; NO original Julia 10D run, network, or PBH likelihood."""
from decimal import Decimal, getcontext
getcontext().prec=60
D=Decimal
C=[
 D("1.3230817938392783"), D("1.3177406564166434"),
 D("1.3229769529861870"), D("1.3178103739910758")]
# Layout C00, C01, C10, C11: source law public/paper x map exec/sym
X=[v/(D(2)+v) for v in C]  # inverse of AUTHOR CODE C=2X/(1-X)
M=[D(2)*x for x in X]     # approximate mass fraction of 4He
R=[D(2)*x/(D(1)-D(2)*x) for x in X]  # old JOURNAL He/H mass ratio

def differ(v):
    de=v[2]-v[0]; ds=v[3]-v[1]
    mix=v[3]-v[2]-v[1]+v[0]
    return de,ds,mix
dx=differ(X)
dm=differ(M)
dc=differ(C)
dr=differ(R)
assert dx[0]<0 and dx[1]>0
assert all(dm[k] == D(2)*dx[k] for k in range(3))
assert all(C[k] == D(2)*X[k]/(D(1)-X[k]) for k in range(4))
assert all(M[k] == D(2)*C[k]/(D(2)+C[k]) for k in range(4))
assert all(R[k] == C[k]*D(2)/(D(2)-C[k]) for k in range(4))
threshold_X=min(abs(dx[0]),abs(dx[1]))/2
threshold_M=min(abs(dm[0]),abs(dm[1]))/2
assert abs(threshold_X-D("0.00000633356560558"))<D("1e-16")
assert threshold_M == D(2)*threshold_X
# Comparison with a 0.245 mass-fraction datum must PULL BACK the target:
C_observed=D("2")*D(".245")/(D("2")-D(".245"))
assert C_observed > D(".245")
print("layout=public_exec,public_sym,paper_exec,paper_sym")
for name,vals in (("code_C",C),("neutron_X",X),
                  ("helium_mass_approx_M",M),("old_journal_mass_He_over_H_R",R)):
    print(name,[str(v) for v in vals])
    print("  public_to_paper_exec, public_to_paper_sym, interaction:",
          *(str(v) for v in differ(vals)))
print("required global per-X endpoint error <",threshold_X)
print("equivalent global per-mass endpoint error <",threshold_M)
print("author_code_C matching physical 0.245 mass-fraction datum:",C_observed)
print("LT5_HELIUM_TYPE_2X2_DECIMAL_PASS")
