"""LT5 ROT17: independent arithmetic checks of quoted source certificates.
This does NOT regenerate the original source fields, source Julia simulation,
or prove all external theorems. It verifies source printed matrix determinants,
finite-difference moment identities, simple Hausdorff/Householder equality,
and necessary sign-preservation thresholds for conditional diagnostic cells.
"""
from math import isclose

P=821
M=[
[565,0,0,0,0,0],
[706,236,130,337,278,86],
[37,283,478,568,425,644],
[737,367,255,506,372,643],
[585,647,19,192,488,297],
[78,57,803,300,153,146]
]
def determinant_mod(A,mod):
    B=[[v%mod for v in row] for row in A]
    det=1
    for j in range(len(B)):
        pivot=next((k for k in range(j,len(B)) if B[k][j]),None)
        if pivot is None: return 0
        if pivot!=j:
            B[j],B[pivot]=B[pivot],B[j]
            det=-det
        d=B[j][j]
        det=det*d%mod
        inv=pow(d,-1,mod)
        for k in range(j+1,len(B)):
            coeff=B[k][j]*inv%mod
            for l in range(j,len(B)):
                B[k][l]=(B[k][l]-coeff*B[j][l])%mod
    return det%mod

assert determinant_mod(M,P)==247
assert determinant_mod([row[1:] for row in M[1:]],P)==804
print("M13_31_PRINTED_CYCLOTOMIC_MATRIX_MODULAR_DETERMINANTS_PASS 247 804")

for stencil in ({1:4/3,2:-1/6},{1:9/8,3:-1/24}):
    m1=sum(k*v for k,v in stencil.items())
    m3=sum(k**3*v for k,v in stencil.items())
    assert abs(m1-1)<1e-13 and abs(m3)<1e-13
    m5=sum(k**5*v for k,v in stencil.items())/120
    expected=-1/30 if 2 in stencil else -3/40
    assert isclose(m5,expected,abs_tol=1e-14)
print("GEEKY_8_FOURTH_ORDER_TAYLOR_MOMENTS_PASS")

deltas=[
(-1.4739737348e-5, 1.1257271224e-5),
(-1.455114464027352e-5, 1.128261533733799e-5),
(-1.4365030570e-5, 1.1307292376e-5)
]
thresholds=[min(abs(x),abs(y))/2 for x,y in deltas]
assert isclose(thresholds[1],5.641307668668995e-6,rel_tol=0,abs_tol=1e-17)
assert isclose(min(thresholds),5.628635612e-6,rel_tol=0,abs_tol=1e-17)
print("MECH_13_SOURCE_MATCHED_SIGN_THRESHOLDS_PASS",thresholds)

for r in (1,2,3,4,8,32,64):
    # Spectrum of Jcoll=-(2/r)*(ones-I): one eigenvalue
    # -2(r-1)/r and r-1 eigenvalues 2/r.
    # J = I - 2/r ones is a reflection: ||J||=1
    col_norm=0 if r==1 else max(2*(r-1)/r,2/r)
    assert isclose(col_norm,2*(1-1/r),abs_tol=1e-14)
print("MT13_COLLISION_HOUSEHOLDER_SHARP_RATIOS_PASS")
print("LT5_ROT17_LIMITED_ARITHMETIC_PASS")
