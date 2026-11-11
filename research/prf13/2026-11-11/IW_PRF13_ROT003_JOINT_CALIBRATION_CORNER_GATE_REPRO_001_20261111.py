#!/usr/bin/env python3
"""PRF13 ROT003: score-copula corner gate and exact one-sided binomial reference.

Independent arithmetic from public R31/R34/PRF13 ROT002 sources.
Runs with Python >=3.10 and SciPy for exact-binomial CDF/quantile.
Quantum m_B values are TRANSCIBED from independent ROT002 Lindblad replay;
this program does not independently re-solve the Lindblad equation.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_HARDWARE / REFEREE_PENDING.
"""
from decimal import Decimal as D, getcontext
from itertools import product
from scipy.stats import binom

getcontext().prec=65
W=(D('.18'),D('.20'),D('.62'))
ALPHA=(D('.943'),D('.907'),D('.347'))
BETA=(D('1'),D('1'),D('.018'))
MB=(D('0.521973443495413435543930779327'),
    D('0.002313357852128669138375189507'),
    D('0.048097378848838209203928789030'))
PROB_B=tuple((1+m)/2 for m in MB)
P0=D('.99'); P1=D(247)/D(4600); B_CEIL=D('.2828')
S=sum(w*max(a,b) for w,a,b in zip(W,ALPHA,BETA))
assert S==D('.59514')


def source_B_score(p0,p1,theta):
    """B with the SAME detector p0,p1 in both shots of a pair; p0>=p1."""
    assert D(0)<=p1<=p0<=D(1) and D(0)<=theta<=D(1)
    val=D(0)
    for w,a,b,p in zip(W,ALPHA,BETA,PROB_B):
        q=p1+(p0-p1)*p
        independent=a*q*q+b*(1-q)*(1-q)
        t_latch=p1+(p0-p1)*p*p
        latched=a*t_latch+b*(1-2*q+t_latch)
        val+=w*((1-theta)*independent+theta*latched)
    return val


def safe_theta_for_rectangle(lo0,hi0,lo1,hi1,b_ceiling=B_CEIL):
    """Exact four-corner bound valid ONLY if hi1<=lo0 and the family is fixed."""
    assert D(0)<lo1<=hi1<=lo0<=hi0<=D(1)
    constraints=[]
    for p0,p1 in product((lo0,hi0),(lo1,hi1)):
        base=source_B_score(p0,p1,D(0))
        full=source_B_score(p0,p1,D(1))
        gain=full-base
        assert gain>=0
        if base>b_ceiling:
            constraints.append(D('-Infinity'))
        elif gain==0:
            constraints.append(D('Infinity'))
        else:
            constraints.append((b_ceiling-base)/gain)
    return min(D(1),min(constraints))


def pair_threshold(theta,p1=P1):
    """P(++ | prepared ideal --), scalar shared-latch mixture detector."""
    return p1*p1+theta*p1*(1-p1)


def one_sided_binomial_test(n,t_bad,alpha):
    """Largest c with P[Bin(n,t_bad)<=c]<=alpha, else -1."""
    t_bad=float(t_bad)
    c=int(binom.ppf(alpha,n,t_bad))
    while binom.cdf(c,n,t_bad)>alpha:
        c-=1
    while binom.cdf(c+1,n,t_bad)<=alpha:
        c+=1
    return c


def theta_upper_from_pair_reference(t_upper,p1_lower):
    """On a joint valid event, bound theta for 0<p1_lower<1 and t>=p1**2."""
    assert 0<p1_lower<1 and 0<=t_upper<=1
    raw=(t_upper-p1_lower*p1_lower)/(p1_lower*(1-p1_lower))
    if raw<0:
        raise ValueError('No admissible theta on joint confidence event: check model/coverage')
    return min(D(1),raw)


def check():
    b0=source_B_score(P0,P1,D(0))
    b1=source_B_score(P0,P1,D(1))
    assert abs(b0-D('0.2706830837549804812431409270108193491137643624'))<D('1e-40')
    assert abs(b1-D('0.2829257326676373768993068657668155839608137364'))<D('1e-40')
    critical=(B_CEIL-b0)/(b1-b0)
    assert abs(critical-D('0.989729945820190114643421556757587267968795'))<D('1e-38')
    print('source_B_independent=',b0)
    print('source_B_shared_latch=',b1)
    print('critical_theta=',critical)
    print('P1=',P1,' P(++|--,theta=critical)=',pair_threshold(critical))
    for delta in (D('0'),D('.0001'),D('.001'),D('.002'),D('.005'),D('0.009398133420642572')):
        t=safe_theta_for_rectangle(P0-delta,P0+delta,P1-delta,P1+delta)
        print('common_shot_marginal_rectangle_halfwidth=',delta,' robust_theta_ceiling=',t)
        # Empirical interior-check as a diagnostic only; convexity is proved analytically.
        corners=list(product((P0-delta,P0+delta),(P1-delta,P1+delta)))
        for factor in (D('.1'),D('.3'),D('.5'),D('.7'),D('.9')):
            for theta in (D('0'),D('.25'),D('.5'),D('1')):
                x=(P0-delta)*(1-factor)+(P0+delta)*factor
                y=(P1-delta)*(1-factor)+(P1+delta)*factor
                assert source_B_score(x,y,theta)<=max(source_B_score(a,b,theta) for a,b in corners)
        if t>=0:
            assert max(source_B_score(a,b,t) for a,b in corners)<=B_CEIL+D('1e-60')

    # With fixed P1 and ideal reference --, rejecting bad detector theta>=theta_c
    # when K_ref<=c controls the H0 error at fixed predeclared n.
    # Fixed n and 90%-power examples, not minima, no physical data.
    alpha=.005
    examples=((D('0'),137),(D('.5'),971),(D('.9'),34898),(D('.98'),3053998))
    tcrit=pair_threshold(critical)
    for theta,n in examples:
        c=one_sided_binomial_test(n,tcrit,alpha)
        size=binom.cdf(c,n,float(tcrit))
        power=binom.cdf(c,n,float(pair_threshold(theta)))
        assert size<=alpha+1e-12 and power>=.90
        print('fixed_n_example', 'theta=',theta,'n_pairs=',n,'physical_reads=',2*n,
              'count_threshold=',c,'type_I=',format(size,'.12g'),
              'power=',format(power,'.12g'))

    # One-step anytime e-factor against BAD detector H0: t>=tcrit,
    # with predeclared alternative t_alt<tcrit.
    t_alt=pair_threshold(D('.9'))
    factor_plus=t_alt/tcrit
    factor_zero=(1-t_alt)/(1-tcrit)
    assert factor_plus<1<factor_zero
    for p in (tcrit,(tcrit+D(1))/2,D(1)):
        emean=p*factor_plus+(1-p)*factor_zero
        assert emean<=1
    print('one_step_anytime_null_factor_E_at_threshold=',
          tcrit*factor_plus+(1-tcrit)*factor_zero)
    # At fixed exact p1, theta upper t-statistic is monotone decreasing in p1:
    # numerator of derivative = -(p1-t)^2 - t(1-t) <=0.
    for upper in (D('.03'),D('.05'),D('.07')):
        assert theta_upper_from_pair_reference(upper,D('.050'))>=theta_upper_from_pair_reference(upper,D('.053')) if upper>=D('.053')**2 else True
    print('PASS ROT003: analytic identities / four-corner fixtures / exact binomial tests / e-factor one-step')


if __name__=='__main__':
    check()
