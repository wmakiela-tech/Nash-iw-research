### Step A: compact sector |ξ|≤35, interval grid + analytic Lipschitz

The precise unitary and Bloch rotations under A are Rodrigues rotations about (0,±Ω,ξ) and (±Ω,0,ξ), with noncommutative finite pulses; the free Z rotation is exactly by ξΔ. Compute p_A at 3,501 point locations ξ_j=−35+j/50, j=0,...,3500, in outward-rounded multiprecision interval arithmetic (mpmath.iv, 40 decimal places) with direct sin, cos, sqrt, arithmetic and **no stochastic simulation**. Every enclosed lower endpoint exceeds 0.5835; the observed lowest enclosed point is at ξ=−21.8 and equals ≈0.58351516902764.

All xi-dependence in the one-shot Hamiltonian has form ξZ/2, including both driven and free stages. Duhamel and trace-distance contractivity imply for any one-shot final Z mean value

 \[|m_J(ξ)-m_J(η)|\le T_J|ξ-η|,\]

where T_X=T_Y=Δ+2t and T_Z=Δ+t. Consequently equation (R22.1) is Lipschitz with |p_A(ξ)-p_A(η)|≤L|ξ−η|, L=Δ+2t=.5+π/10<.815. Every point in [−35,35] is at most .01 from a grid center. Thus

 \[\boxed{p_A(ξ)>.5835−.815(.01)=.57535>.5753\quad(|ξ|\le35).}\tag{R22.4}\]

This is a CONTINUUM certificate, not just a dense scan. The integer-grid and analytic Lipschitz calculations are exact; pointwise interval evaluation uses the published mpmath.iv directed-rounding implementation. No independent formally verified proof assistant or hardware calibration exists.

### Step B: ALL far detunings |ξ|≥35, direct transition-amplitude inequality

For any finite square transverse π/2 pulse with |Ω|=10 and static xi, the exact qubit transition amplitude between Z computational basis states obeys

 \[|\langle1|U_{\rm pulse}(ξ)|0\rangle|\le\frac{Ω}{\sqrt{ξ^2+Ω^2}}=:v(ξ).\]

The free Z stage does not flip computational basis states. A source-A X/Y shot consists of TWO such pulses and the free Z stage; by a triangle inequality for transition amplitudes, final transition probability is ≤(2v)^2. The Z shot has just ONE pulse and flip probability ≤v². Hence

 \[m_X,m_Y\ge1−8v^2,\qquad m_Z\ge1−2v^2.\]

For |ξ|≥35, v²≤100/1325=4/53 and both right sides are positive, so from (R22.1)

 \[p_A(ξ)\ge \frac12+\frac{2(1−8(4/53))^2+(1−2(4/53))^2}{6}
 =0.6724813100747598\ldots>.6724.\tag{R22.5}\]

The far-tail inequality is completely analytic and does not invoke a Cauchy density. Combining (R22.4) and (R22.5) proves p_A≥.5753 globally, without any phase prior.

### Step C: B value enclosed by Taylor with controlled source-active Lindbladian remainder

For B, each driven 3×3 real Bloch generator is G=[Ωe_axis]_×−diag(1,1,0). Its matrix infinity norm ≤11, and each pulse t=π/20<.16 gives ||Gt||∞<2. Propagate the exact Bloch vectors using the Taylor polynomial of order 65. Its neglected tail is bounded by

 \[\|R_{65}\|_\infty\le e^2\frac{2^{66}}{66!}<1.1\times10^{-72}\]

