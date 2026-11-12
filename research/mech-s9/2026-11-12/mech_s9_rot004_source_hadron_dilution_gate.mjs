// Mech-S9 ROT004 -- frozen Wu-Xu HADRON DILUTION timescale and forced-response gate.
// NOT native Julia, NOT a BBN/PBH simulation. Requires the unmodified upstream CSV:
// node mech_s9_rot004_hadron_dilution_gate.mjs N_around_m_e.csv
// Author original commit d395183674cace6c9906a8911bdeb7234ba4040d.
// Original N_around_m_e.csv Git blob 93f2494f026c5d0587ea40fe08bb938dd9d01fa8.
// Source rates from tool_script-parameters.jl blob 0d7198ff3557bdbd5753000bb07a7a7405cc24f5.
// Source 10D source/loss RHS main-scan.jl blob b368ba55d5a493f7bc185909730f7fe5691f10d6.
// CODATA2022 NIST: https://physics.nist.gov/cuu/pdf/JPCRD2022CODATA.pdf
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
if(!process.argv[2])throw Error('Original author N_around_m_e.csv path required');
const raw=readFileSync(process.argv[2]);
const blob=createHash('sha1').update(Buffer.from('blob '+raw.length+'\0')).update(raw).digest('hex');
if(blob!=='93f2494f026c5d0587ea40fe08bb938dd9d01fa8')throw Error('AUTHOR SOURCE BLOB MISMATCH '+blob);
const d=raw.toString('utf8').trim().split(/\r?\n/).map(s=>s.split(',').map(Number));
if(d.length!==1000||d.some((r,i)=>r.length!==3||r.some(x=>!Number.isFinite(x))||(i>0&&r[0]<=d[i-1][0])))throw Error('SOURCE 1000x3 ORDER FAIL');
function gr(T){
 if(T<d[0][0]||T>d.at(-1)[0])throw Error('T outside original source');
 let i=0,j=d.length-1;
 while(j-i>1){const m=(i+j)>>1;d[m][0]<=T?i=m:j=m;}
 const a=d[i],b=d[i+1],frac=Math.log(T/a[0])/Math.log(b[0]/a[0]);
 return a[1]+frac*(b[1]-a[1]);
}
const pi=Math.PI,zeta3=1.202056903159594,G=6.70883e-39,hbar_GeVs=6.582119569e-25;
const hbarC_MeVfm=197.3269804, light_m_s=299792458,etaB=6.1e-10;
const Mred_GeV=1/Math.sqrt(8*pi*G);
const Hcoeff=Math.sqrt(pi*pi/90)*1e-6/(Mred_GeV*hbar_GeVs); // H_rad [s^-1]=Hcoeff sqrt(g_rho) T_MeV^2
const annCoeff=28e-31*light_m_s*etaB*(2*zeta3/(pi*pi))*1e45/(hbarC_MeVfm**3); // lambda_min [s^-1]=annCoeff*T_MeV^3
const GammaPi=1/2.6033e-8,GammaKm=8.1e7,GammaK0L=2.0e7;
function at(T){
 const g=gr(T),H=Hcoeff*Math.sqrt(g)*T*T,lambda=annCoeff*T*T*T;
 return{T_MeV:T,g_rho:g,H_rad_s_inv:H,
  n_gamma_m_inv3:(2*zeta3/(pi*pi))*(T/hbarC_MeVfm)**3*1e45,
  lambda_antibaryon_MIN_s_inv:lambda, 
  epsilon_antibaryon_3H_over_lambda:3*H/lambda,
  epsilon_pion_decay_3H_over_Gamma:3*H/GammaPi,
  epsilon_kaon_minus_decay_3H_over_Gamma:3*H/GammaKm,
  epsilon_K0L_decay_3H_over_Gamma:3*H/GammaK0L,
  PBH_to_SM_energy_ratio_needed_for_3H_over_antibaryon_eq_1:(lambda/(3*H))**2-1};
}
const lo=.03,hi=1;
const knots=[lo,hi,...d.map(v=>v[0]).filter(t=>t>lo&&t<hi)];
const gmin=Math.min(...knots.map(gr)),gmax=Math.max(...knots.map(gr));
const Hmax=Hcoeff*Math.sqrt(gmax)*hi**2,lambdaMin=annCoeff*lo**3;
const pointSupBound=3*Hcoeff/annCoeff*Math.sqrt(gmax)/lo; // tight-ish universal envelope in the specified domain
const timeWindowEnvelope=3*Hmax/lambdaMin; // rigorous |n0(t)-n3H(t)| <= envelope*sup_[t0,t] n3H under forced same J,lambda,H
const sampleMax=Math.max(...knots.map(t=>at(t).epsilon_antibaryon_3H_over_lambda));
if(sampleMax>pointSupBound*(1+1e-13))throw Error('uniform-source interval gate broken');
if(Math.abs(at(.1).epsilon_antibaryon_3H_over_lambda-7.919074597898146e-7)>1e-13)throw Error('bad source endpoint regression');
function constantSource(t,J,L,H){
 const n0=J/L*(-Math.expm1(-L*t));
 const n3=J/(L+3*H)*(-Math.expm1(-(L+3*H)*t));
 return{n0,n3,delta:n0-n3,ratio:n3/n0,eq_limit_relative_decrease:3*H/(L+3*H)};
}
const control=constantSource(.1,10,1000,.01);
if(!(control.delta>0&&control.ratio>0&&control.ratio<=1))throw Error('synthetic positive forced solution control FAIL');
const result={
 status:'SOURCE_LOCKED_STATIC_RATE_SCALE_AND_EXACT_FORCED_SCALAR_ENVELOPE__NOT_NATIVE_JULIA',
 original_source_commit:'d395183674cace6c9906a8911bdeb7234ba4040d',original_EOS_git_blob:blob,
 domain_T_MeV:[lo,hi],input_rows:d.length,source_g_rho_range:[gmin,gmax],
 constants:{G_GeV_minus2:G,hbar_GeV_s:hbar_GeVs,hbarC_MeV_fm:hbarC_MeVfm,etaB,minimum_antibaryon_sigma_mb:28,light_m_s},
 rigorous_radiation_only_bounds:{
 pointwise_3H_over_antibaryon_lambda_le:pointSupBound,
 absolute_forced_trajectory_delta_n_le_coefficient_times_sup_n3H:timeWindowEnvelope,
 pointwise_3H_over_pion_decay_le:3*Hmax/GammaPi,
 pointwise_3H_over_kaon_minus_decay_le:3*Hmax/GammaKm,
 pointwise_3H_over_K0L_decay_le:3*Hmax/GammaK0L
 },max_sampled_source_knots_antibaryon_ratio:sampleMax,
 selected_T_MeV:[.03,.05,.07818527068831995,.099688851247,.1,.2,.5,1].map(at),
 synthetic_constant_J_H_L_scalar_control:control,
 theory:'For identical forced J(t),lambda(t),H(t),same initial n>=0, n0-n3H = integral exp(-int_lambda) 3H n3H ds >=0. If lambda>=lambdaMin,H<=Hmax, difference <=(3Hmax/lambdaMin) sup_history(n3H). This is NOT same-time relative error and NOT a full coupled-model Yp bound.',
 PBH_domination:'At the same T and native nB, when f=rho_PBH/rho_SM>=0, replace H_rad by H_rad*sqrt(1+f); no unbounded-f envelope applies.'
};
console.log(JSON.stringify(result,null,2));
