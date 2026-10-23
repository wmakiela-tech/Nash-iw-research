"""INT8 ROT013: finite-difference Lie bracket/Leibniz witness, synthetic NumPy."""
import numpy as np

def d(f,h):
    return (np.roll(f,-1)-np.roll(f,1))/(2*h)

def defect(f,g,h):
    return d(f*g,h)-f*d(g,h)-g*d(f,h)

def scalar_check(N,k=1,l=2):
    h=2*np.pi/N
    x=h*np.arange(N)
    f=np.sin(k*x);g=np.cos(l*x)
    a=d(f,h);b=d(g,h)
    K=2*(f*d(b,h)-g*d(a,h)-d(f*b-g*a,h))
    rhs=2*(defect(g,a,h)-defect(f,b,h))
    assert np.max(np.abs(K-rhs))<1e-10
    spectral=np.zeros(N,dtype=complex)
    for j,F in ((k,-.5j),(-k,.5j)):
        for m,G in ((l,.5),(-l,.5)):
            symbol=lambda t: np.sin(t*h)/h
            coeff=2*(symbol(m)-symbol(j))*(symbol(j+m)-symbol(j)-symbol(m))
            spectral+=coeff*F*G*np.exp(1j*(j+m)*x)
    assert np.max(abs(K-spectral.real))<1e-10
    return np.sqrt(np.mean(K*K))

if __name__=='__main__':
    for N in (9,17,31,61,121,241):
        h=2*np.pi/N
        low=scalar_check(N)
        hi=scalar_check(N,N//7,N//5)
        print(N, 'smooth=',low,'smooth_over_h2=',low/h**2,
              'high=',hi,'high_times_h2=',hi*h*h)
    print('PASS exact Leibniz defect and Fourier symbol reconstruction')
