# Geeky-S10 NC J3 affine RMS extrema geometric classification

RETURN_ID: GEEKY-S10-NC-J3-AFFINE-RMS-EXTREMA-GEOMETRIC-CLASSIFICATION-001  
DATE: 2026-10-17  
STATUS: PASS_EXACT_ABSTRACT / SEPARATE_FROM_STOPPED_NECESSITY_SEAM / NO PHYSICAL J3 / NO CANON / NO EXEC_SIGN

Durable native Google Doc:
https://docs.google.com/document/d/1PFRvykm6UHnZTrLvbK-xEZcbBwpGcEDOfNaD1bnpCc0/edit

## Exact setup

For the affine defect

J(a)=aU+a^2V,

define

A=||U||^2,
B=Re<U,V>,
C=||V||^2.

Then

g(a)=||J(a)||^2
=Aa^2+2Ba^3+Ca^4,

and

g'(a)=2a(A+3Ba+2Ca^2).

For a>0 the stationary equation is

A+3Ba+2Ca^2=0.

## Complete classification

Assume A,C>0 and define

Delta=9B^2-8AC.

- If B>=0: g is strictly increasing.
- If B<0 and Delta<0: g is strictly increasing.
- If B<0 and Delta=0: there is one horizontal stationary point
  a0=-3B/(4C), but no extremum; g remains strictly increasing.
- If B<0 and Delta>0: there are exactly two positive roots

  a_- = (-3B-sqrt(Delta))/(4C),
  a_+ = (-3B+sqrt(Delta))/(4C),

  with a_- a strict local maximum and a_+ a strict local minimum.

Degenerate cases U=0 or V=0 are monotone unless J is identically zero.

## Geometric condition

By Cauchy-Schwarz, B^2<=AC.

Define

c=B/sqrt(AC) in [-1,1].

A positive local max/min pair exists iff

c < -2 sqrt(2)/3
≈ -0.942809.

Thus the linear and quadratic defect directions must be very strongly anti-aligned.

Firewall:

A QUADRATIC VECTOR DEFECT DOES NOT GENERICALLY IMPLY AN INTERIOR RMS MAXIMUM.

## Antiparallel witness

If V=-beta U, beta>0, then

J(a)=a(1-beta a)U.

The local maximum is at

a_-=1/(2beta),

and the local minimum is at

a_+=1/beta,

where J(a_+)=0.

## Global maximum guard

On the unbounded domain a>=0, any nontrivial affine defect norm is unbounded as a->infinity. Therefore a finite stationary maximum is only LOCAL.

A finite global a_max requires a declared finite legal interval or other admissibility restriction.

On [0,a_L], the only candidates are:
- a_L;
- a_- when it exists and lies inside the interval.

## Signed functional versus RMS

For a signed linear functional ell,

ell(J)=aK1+a^2K2

has stationary point -K1/(2K2), when defined.

This is unrelated in general to the Hilbert/RMS extremum, which depends on A,B,C.

SIGNED PROJECTION EXTREMUM != RMS EXTREMUM.

## Discrete residual guard

M13 ROT07 gives

J_discrete(a)
=
R0(I+aBop)h
+
aM(I+aBop)h,

with R0=[L1,L2]-L12.

The classification above applies directly only after R0=0 or after the bracket residual has been independently removed.

FORMAL AFFINE J3 EXTREMUM CLASSIFICATION != FINITE-DIFFERENCE DTC EXTREMUM CLASSIFICATION AUTOMATICALLY.

## Diagnostic

Any source-native implementation claiming an interior RMS maximum from the affine exact formula should report:
A, B, C, Delta, c, legal a interval, and the bracket residual at a=0.

If c>=-2sqrt(2)/3, an interior local RMS maximum is impossible under the exact affine assumptions.

## Disposition

AFFINE_J3_RMS_EXTREMA = CLASSIFIED_EXACTLY_ABSTRACT.  
SCALAR_AMAX_AS_RMS_MAX = REJECT_UNLESS_EXTRA_CONDITIONS_PROVED.  
INTERIOR_RMS_MAX_REQUIRES_STRONG_ANTI_ALIGNMENT = c<-2sqrt(2)/3.  
SOURCE_NATIVE_DTC_AUDIT = OPEN_UNTOUCHED.  
R1_DS_REFEREE = OPEN_UNTOUCHED.  
REC9_NECESSITY_SEAM_STOP = RESPECTED.

NO novelty / NO canon / NO EXEC_SIGN / NO NEW TASK.
