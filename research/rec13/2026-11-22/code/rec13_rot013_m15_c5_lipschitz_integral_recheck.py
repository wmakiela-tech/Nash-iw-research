import mpmath as mp
mp.mp.dps=65
N=41
modes=[(20,20,20),(20,20,0),(20,0,0),(7,0,0),(12,12,13),(3,13,7)]
a=[]; f=[]; h=[]
for k in modes:
 C=[mp.cos(2*mp.pi*t/N) for t in k]
 a.append(sum(C)/3);f.append((C[0]*C[1]+C[0]*C[2]+C[1]*C[2])/3);h.append(C[0]*C[1]*C[2])
H=mp.matrix([[mp.mpf(1) for v in a],a,[v*v for v in a],[v**3 for v in a],f]); w=list(mp.lu_solve(H[:,:5],-H[:,5]))+[mp.mpf(1)]
A0=mp.mpf(1); thA=list(map(mp.mpf,['0.12','0.1','0.08']))
B0=mp.mpf(99779719687217)/10**14
thB=[mp.mpf(316869474178226)/2494492992180425,mp.mpf(93110637627687)/997797196872170,mp.mpf(205860943554709)/2494492992180425]
def vv(beta, theta,j): return beta*(1+theta[0]*a[j]+theta[1]*f[j]+theta[2]*h[j])
Delta=sum(w[j]*mp.log(vv(B0,thB,j)/vv(A0,thA,j)) for j in range(6)); idx=sorted(range(6),key=lambda i:a[i])
def K(t):return sum(w[i]*(a[i]-t)**3 for i in range(6) if a[i]>t)/6
def Kp(t):return -sum(w[i]*(a[i]-t)**2 for i in range(6) if a[i]>t)/2
tstar=mp.findroot(K,(mp.mpf('.02'),mp.mpf('.04')))
ends=[a[j] for j in idx];pieces=[]
for i in range(5):
 cuts=[ends[i]]
 if ends[i]<tstar<ends[i+1]:cuts.append(tstar)
 cuts.append(ends[i+1])
 for lo,hi in zip(cuts[:-1],cuts[1:]):pieces.append(abs(mp.quad(K,[lo,hi])))
R=sum(pieces);L=mp.mpf('16.5'); M=mp.mpf('50'); c=mp.mpf('0.00045');hh=mp.mpf('.15');margin=Delta-2*L*R+L*c*hh*hh
for label,v in [('nodes',a),('ordered',[a[i] for i in idx]),('w',w),('nuisance',[sum(w[i]*H[r,i] for i in range(6)) for r in range(5)]),('Delta',Delta),('tstar',tstar),('R',R),('Kp(-h)',Kp(tstar-hh)),('Kp(0)',Kp(tstar)),('Kp(+h)',Kp(tstar+hh)),('Margin',margin),('Lmax',Delta/(2*R-c*hh*hh)),('hmax',L/(2*M))]:
 print(label, [mp.nstr(x,30) for x in v] if isinstance(v,list) else mp.nstr(v,55))
deffull=c*(2*L*hh*hh-mp.mpf(4)*M*hh**3/3)
marginnew=Delta-2*L*R+deffull
P=sum(ww for ww in w if ww>0)
delta=mp.mpf(1)/80000
penalty=P*mp.log((1+delta)/(1-delta))
crit=marginnew/2-penalty
print('NEW-def',mp.nstr(deffull,55),'vs old',mp.nstr(L*c*hh**2,55))
print('NEW-margin',mp.nstr(marginnew,55),'vs old',mp.nstr(margin,55))
print('P',mp.nstr(P,55),'logpenalty',mp.nstr(penalty,55))
print('delta=1/80000 residual decision margin',mp.nstr(crit,55))
for n in [100000000000,120000000000,150000000000,180000000000,200000000000,300000000000,400000000000]:
 er=12*mp.exp(-mp.mpf(n)/(4*(80000**2)))
 print('n',n,'errorUpper',mp.nstr(er,20),'successLB',mp.nstr(1-er,20))
assert crit>mp.mpf('0.000002')
assert marginnew>mp.mpf('.00008718')
assert abs(margin-mp.mpf('0.00002137477833689214438009622057948'))<mp.mpf('1e-28')
