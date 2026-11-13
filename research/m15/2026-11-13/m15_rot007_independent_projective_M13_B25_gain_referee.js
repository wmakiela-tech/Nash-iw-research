#!/usr/bin/env node
"use strict";
/* M15 ROT007: independent exact source-locked BigInt rational referee of
   Geeky-S12 ROT015 projective ratio positivity and common-gain calibration.
   Input: original M13 direct_B.json, blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0.
   No Geeky ROT015 code, mathematical function, or machine results are imported.
   Run: node m15_rot007_independent_projective_gain_referee.js direct_B.json
   Math decisions use exact rational endpoints, not displayed floating approximations.
*/
function audit(source) {
 const ab=n=>n<0n?-n:n;
 function gcd(a,b){a=ab(a);b=ab(b);while(b){let t=a%b;a=b;b=t;}return a||1n;}
 function rat(a,b=1n){a=BigInt(a);b=BigInt(b);if(b===0n)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}let g=gcd(a,b);return[a/g,b/g];}
 const ZERO=rat(0),ONE=rat(1);
 const add=(a,b)=>rat(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
 const sub=(a,b)=>add(a,[-b[0],b[1]]);
 const mul=(a,b)=>rat(a[0]*b[0],a[1]*b[1]);
 const div=(a,b)=>rat(a[0]*b[1],a[1]*b[0]);
 const cmp=(a,b)=>{let d=a[0]*b[1]-b[0]*a[1];return d<0n?-1:d>0n?1:0;};
 const mag=x=>[ab(x[0]),x[1]];
 function decimal(t) {
   t=t.trim();let sign=1n;if(t.startsWith("-")){sign=-1n;t=t.slice(1)}else if(t.startsWith("+"))t=t.slice(1);
   let parts=t.toLowerCase().split("e"),components=parts[0].split("."),e=(parts[1]?Number(parts[1]):0)-(components[1]?.length||0);
   let n=sign*BigInt((components[0]||"0")+(components[1]||""));
   return e>=0?rat(n*10n**BigInt(e)):rat(n,10n**BigInt(-e));
 }
 function sourceEndpoint(s){
   if(!s.startsWith("[")||!s.endsWith("]"))throw Error("source bracket");
   let parts=s.slice(1,-1).split(",");if(parts.length!==2)throw Error("source directed bracket");
   let lo=decimal(parts[0]),hi=decimal(parts[1]);
   if(cmp(lo,hi)!==0)throw Error("individual M13 directed cell not point bracket");
   return lo;
 }
 function interval(lo,hi=lo){if(cmp(lo,hi)>0)throw Error("bad interval");return[lo,hi];}
 const z=()=>interval(ZERO);
 const plus=(a,b)=>interval(add(a[0],b[0]),add(a[1],b[1]));
 const minus=(a,b)=>interval(sub(a[0],b[1]),sub(a[1],b[0]));
 function times(a,b){let p=[mul(a[0],b[0]),mul(a[0],b[1]),mul(a[1],b[0]),mul(a[1],b[1])].sort(cmp);return interval(p[0],p[3]);}
 const scale=(a,c)=>times(a,interval(c));
 const positiveDiv=(a,b)=>{if(cmp(b[0],ZERO)<=0)throw Error("nonpositive denominator");return interval(div(a[0],b[1]),div(a[1],b[0]));};
 const polynomialPlus=(a,b)=>Array.from({length:Math.max(a.length,b.length)},(_,k)=>plus(a[k]||z(),b[k]||z()));
 const polynomialMinus=(a,b)=>Array.from({length:Math.max(a.length,b.length)},(_,k)=>minus(a[k]||z(),b[k]||z()));
 function polynomialTimes(a,b){let v=Array.from({length:a.length+b.length-1},z);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)v[i+j]=plus(v[i+j],times(a[i],b[j]));return v;}
 const polynomialScale=(a,c)=>a.map(v=>scale(v,c));
 const deriv=a=>a.slice(1).map((v,i)=>scale(v,rat(i+1)));
 function factorialBinomial(n,k){let x=1n;for(let i=1;i<=k;i++)x=x*BigInt(n-i+1)/BigInt(i);return x;}
 const power=(q,n)=>{let p=ONE;for(let i=0;i<n;i++)p=mul(p,q);return p;};
 function bernsteinOnZeroToFifth(poly) {
   const n=poly.length-1,rad=rat(1n,5n),coef=[];
   for(let k=0;k<=n;k++){
     let term=z();
     for(let j=0;j<=k;j++)
       term=plus(term,scale(poly[j],mul(power(rad,j),div(rat(factorialBinomial(k,j)),rat(factorialBinomial(n,j))))));
     coef.push(term);
   }
   return coef;
 }
 function evaluation(poly,t){let cur=z();for(let i=poly.length-1;i>=0;i--)cur=plus(times(cur,interval(t)),poly[i]);return cur;}
 const eps=rat(1n,10000000n),scaleS=rat(1000000000000n),rows=[2,3,4,5,6],
  N=rows.map(k=>BigInt((41-2*k)**3)),W=N.map((x,i)=>i===4?x:x-N[i+1]);
 let nominal=rows.map(k=>{
   if(!Array.isArray(source[k])||source[k].length!==5)throw Error("source shape");
   return source[k].map(pair=>{
     if(!Array.isArray(pair)||pair.length!==2)throw Error("source pair");
     let l=sourceEndpoint(pair[0]),u=sourceEndpoint(pair[1]);if(cmp(l,u)>0)throw Error("source source lower > upper");
     return interval(l,u);
   });
 });
 const widened=nominal.map(row=>row.map(v=>interval(sub(v[0],mul(eps,mag(v[0]))),add(v[1],mul(eps,mag(v[1]))))));
 function shells(rows5){
   return rows5.map((row,i)=>row.map((raw,j)=>{
     let x=i<4?minus(scale(raw,rat(N[i])),scale(rows5[i+1][j],rat(N[i+1]))):scale(raw,rat(N[i]));
     return scale(positiveDiv(x,interval(rat(W[i]))),scaleS);
   }));
 }
 const S=shells(widened),S0=shells(nominal);
 const shellB=S.map(poly=>bernsteinOnZeroToFifth(poly));
 if(shellB.some(row=>row.some(c=>cmp(c[0],ZERO)<=0)))throw Error("global shell positivity failed");
 // H(t)=s4'(t)s5(t)-s4(t)s5'(t) - s4(t)s5(t)/8
 // i=3,4 are shells s4 and s5 in 1-based shell numbering.
 const B=S[3],C=S[4];
 const H=polynomialMinus(polynomialMinus(polynomialTimes(deriv(B),C),polynomialTimes(B,deriv(C))),polynomialScale(polynomialTimes(B,C),rat(1n,8n)));
 if(H.length!==9)throw Error("unexpected H degree");
 const signs=bernsteinOnZeroToFifth(H);
 if(signs.length!==9)throw Error("9th degree gate shape");
 if(signs.some(x=>cmp(x[0],ZERO)<=0))throw Error("H > 1/8 s4*s5 Bernstein sign failed");
 const alpha=rat(1n,20n),beta=rat(3n,40n);
 const ratio=S.map(poly=>positiveDiv(evaluation(poly,alpha),evaluation(poly,beta)));
 const ordered=ratio.every((q,i)=>i===0||cmp(ratio[i-1][1],q[0])<0);
 if(!ordered)throw Error("ratio ordering NOT interval certified");
 // rmin=r1, rmax=r5. Formula monotone inc rmax, dec rmin.
 const kLower=div(sub(ratio[4][0],ratio[0][1]),add(ratio[4][0],ratio[0][1]));
 const kUpper=div(sub(ratio[4][1],ratio[0][0]),add(ratio[4][1],ratio[0][0]));
 if(cmp(kLower,rat(66n,1000n))<=0||cmp(kUpper,rat(67n,1000n))>=0)throw Error("6.6 / 6.7 robust threshold not proven");
 const midpoint=nominal.map(row=>row.map(v=>interval(div(add(v[0],v[1]),rat(2n)))));
 const SM=shells(midpoint);
 const rats=SM.map(poly=>{
    let a=evaluation(poly,alpha),b=evaluation(poly,beta);
    if(cmp(a[0],a[1])!==0||cmp(b[0],b[1])!==0)throw Error("midpoint unexpected width");
    return div(a[0],b[0]);
 });
 const rsmin=rats.reduce((a,b)=>cmp(a,b)<0?a:b),rsmax=rats.reduce((a,b)=>cmp(a,b)>0?a:b);
 const kappa=div(sub(rsmax,rsmin),add(rsmax,rsmin));
 const c=div(add(rsmax,rsmin),rat(2));
 const eta=rats.map(ri=>sub(div(ri,c),ONE));
 let equalities=0;for(let i=0;i<5;i++){
   const aa=evaluation(SM[i],alpha)[0],bb=evaluation(SM[i],beta)[0];
   if(cmp(aa,mul(c,mul(add(ONE,eta[i]),bb)))!==0)throw Error("exact zero-loss identity failed");
   if(cmp(mag(eta[i]),kappa)>0)throw Error("eta exceeds sharp kappa");
   equalities++;
 }
 function fmt(q) {return q[0].toString()+"/"+q[1].toString();}
 function rounded(q){
   if(q[0]===0n)return "0";
   let na=ab(q[0]).toString(),de=q[1].toString(),an=na.slice(0,17),dn=de.slice(0,17);
   let x=(Number(an)/10**(an.length-1))/(Number(dn)/10**(dn.length-1)),exp=na.length-de.length;
   if(x>=10){x/=10;exp++}if(x<1){x*=10;exp--}
   return (q[0]<0n?"-":"")+x.toPrecision(13)+"e"+(exp>=0?"+":"")+exp;
 }
 return {
  artifact_id:"IW_M15_ROT007_PROJECTIVE_M13_B25_GAIN_SHARP_THRESHOLD_INDEPENDENT_REFEREE_001_20261113",
  source_git_blob_expected:"a6f50fbe5904e580e84c87ee87c5ad043cdec5d0",
  source_coefficient_count:25,epsilon:"1/10000000",source_scale:"10^12",
  sign_method:"independent exact rational coefficient convolution + 9 Bernstein coefficient lower signs (not owner code)",
  shell_global_positivity:5, H_gate_bernstein_positive_count:signs.length,
  H_nine_lower_scaled_1e24:signs.map(x=>rounded(x[0])),
  H_smallest_lower_scaled_1e24:rounded(signs.map(x=>x[0]).reduce((a,b)=>cmp(a,b)<0?a:b)),
  pair_alpha:"1/20",pair_beta:"3/40",
  ratio_intervals_strict_order:ordered,
  pair_ratio_intervals:ratio.map(v=>({low:rounded(v[0]),high:rounded(v[1])})),
  pair_kappa_bound:{low:rounded(kLower),high:rounded(kUpper),more_than_0p066:cmp(kLower,rat(66n,1000n))>0,less_than_0p067:cmp(kUpper,rat(67n,1000n))<0},
  midpoint_kappa:rounded(kappa),midpoint_c:rounded(c),midpoint_eta:eta.map(rounded),
  midpoint_exact_zero_residuals:equalities,
  global_lower_projective:"kappa_crit(alpha,beta)>tanh(abs(alpha-beta)/16) for alpha!=beta, conditional on source 9-sign gate",
  strict_positive_all:signs.every(v=>cmp(v[0],ZERO)>0),
  status:"INDEPENDENT_I1_BOUNDED_EXACT_MATH_PASS_NOT_HISTORIC_PRODUCER_NOT_REAL_PHYSICS_NOT_EXTERNAL_I3"
 };
}
if(typeof require!=="undefined"&&require.main===module){
 const fs=require("fs"),crypto=require("crypto"),path=require("path");
 const p=process.argv[2];if(!p)throw Error("Supply original M13 direct_B.json");
 const bytes=fs.readFileSync(p);
 const sha=crypto.createHash("sha1").update(Buffer.from("blob "+bytes.length+"\0")).update(bytes).digest("hex");
 if(sha!=="a6f50fbe5904e580e84c87ee87c5ad043cdec5d0")throw Error("SOURCE_ORIGINAL_M13_GIT_BLOB_MISMATCH");
 const out=audit(JSON.parse(bytes.toString("utf8")));
 fs.writeFileSync(path.join(path.dirname(__filename),"m15_rot007_projective_referee_result.json"),JSON.stringify(out,null,2)+"\n");
 process.stdout.write(JSON.stringify(out,null,2)+"\n");
}
