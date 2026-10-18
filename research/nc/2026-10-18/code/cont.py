import numpy as np
# CONTINUOUS-SPECTRUM instance: multiplication operators on L^2([0,1]), discretized.
# A = mult by a(x), B = mult by b(x), J = mult by j(x).
# Then J m(A) = m(B) J  <=>  j(x)[ m(a(x)) - m(b(x)) ] = 0 a.e.
# So: for ALL bounded Borel m  <=>  j = 0 a.e. on {a != b}.
# Hypothesis with h gives: j = 0 a.e. on {h(a) != h(b)}.
# SHARP: hypothesis => conclusion  iff  j = 0 a.e. on COLLISION = {a!=b} AND {h(a)=h(b)}.
N=20000
x=(np.arange(N)+0.5)/N
h=lambda w: np.cos(np.pi*w)
MS=[('1/(1+w)',lambda w:1/(1+w)),('exp(-.7w)',lambda w:np.exp(-.7*w)),
    ('1_{w>1.5}',lambda w:(w>1.5).astype(float)),('w',lambda w:w),('sin(3w)',lambda w:np.sin(3*w))]
def defect(j,a,b,m):             # operator norm of a multiplication operator = sup |symbol|
    return np.max(np.abs(j*(m(a)-m(b))))

# a and b collide under h on the middle third: a=1, b=3 there (cos(pi*1)=cos(pi*3)=-1)
a=np.where((x>1/3)&(x<2/3), 1.0, x*0.5)
b=np.where((x>1/3)&(x<2/3), 3.0, x*0.5)
coll=((np.abs(a-b)>1e-12)&(np.abs(h(a)-h(b))<1e-12))
print("CONTINUOUS-SPECTRUM INSTANCE: multiplication operators on L^2([0,1])")
print(f"  sigma(A) is a continuum on the non-collision part; collision set measure = {coll.mean():.4f}")
print(f"  on the collision set a=1, b=3, h(a)=h(b)={h(np.array([1.0]))[0]:+.1f}")
print()
print(f"{'j supported where':<34} {'||j|_coll||inf':>14} {'hyp defect':>12} {'max_m defect':>13} {'predicted':>16}")
tests={
 'everywhere (couples collision)': np.ones(N),
 'ONLY off the collision set':      (~coll).astype(float),
 'only ON the collision set':       coll.astype(float),
 'smooth bump off collision':       np.exp(-((x-0.1)/0.05)**2),
 'smooth bump centred on collision':np.exp(-((x-0.5)/0.05)**2),
}
for name,j in tests.items():
    jc=np.max(np.abs(j[coll])) if coll.any() else 0.0
    hyp=defect(j,a,b,h)
    worst=max(defect(j,a,b,m) for _,m in MS)
    pred='FULL TRANSPORT' if jc<1e-12 else 'FAILS'
    print(f"{name:<34} {jc:>14.3e} {hyp:>12.3e} {worst:>13.3e} {pred:>16}")
print()
print("  -> the criterion is j=0 a.e. ON THE COLLISION SET, not injectivity of h.")
print("     'smooth bump off collision' is a NON-separating h with FULL transport and j != 0.")
