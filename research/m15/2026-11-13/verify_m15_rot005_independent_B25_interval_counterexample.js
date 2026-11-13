#!/usr/bin/env node
"use strict";
/*
M15 ROT005: independently implemented exact BigInt rational interval negative witness.
SOURCE: M13 original direct_B.json Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0.
No Geeky ROT007/012/013 mathematical function is imported or executed.
Node 18+ stdlib CLI: node this_file.js path/to/direct_B.json
The source file is verified by exact Git blob SHA-1 before parsing.
Computation concerns ONLY alpha=.03082, delta=.02514, eps=1e-8;
it is NOT a referee proof of Geeky's global Bernstein positivity theorem.
*/
function independentAudit(source) {
 const abs=z=>z<0n?-z:z;
 function gcd(a,b){a=abs(a);b=abs(b);while(b){let x=a%b;a=b;b=x;}return a||1n;}
 function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("Zero divisor");if(d<0n){n=-n;d=-d;}let g=gcd(n,d);return[n/g,d/g];}
 const Z=F(0),add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),
 neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b)),
 mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]),
 cmp=(a,b)=>{let q=a[0]*b[1]-b[0]*a[1];return q<0n?-1:q>0n?1:0;};
 function decimal(str){
   let s=str.trim(),sgn=1n;if(s.startsWith("-")){sgn=-1n;s=s.slice(1);}
   else if(s.startsWith("+"))s=s.slice(1);
   const part=s.toLowerCase().split("e");if(part.length>2)throw Error("Bad decimal");
   const [a,b=""]=part[0].split(".");let power=(part[1]?Number(part[1]):0)-b.length;
   let numerator=sgn*BigInt((a||"0")+b);
   return power>=0?F(numerator*10n**BigInt(power)):F(numerator,10n**BigInt(-power));
 }
 function parseEndpoint(t) {
   if(!t.startsWith("[")||!t.includes(","))throw Error("Source interval expected");
   let parts=t.slice(1,-1).split(",");
   let lo=decimal(parts[0]),hi=decimal(parts[1]);
   if(cmp(lo,hi)!==0)throw Error("Nondegenerate individual source enclosure");
   return lo;
 }
 function I(lo,hi=lo){if(cmp(lo,hi)>0)throw Error("Inverted interval");return[lo,hi];}
 const plus=(a,b)=>I(add(a[0],b[0]),add(a[1],b[1]));
 const minus=(a,b)=>I(sub(a[0],b[1]),sub(a[1],b[0]));
 function times(a,b){
   let p=[mul(a[0],b[0]),mul(a[0],b[1]),mul(a[1],b[0]),mul(a[1],b[1])].sort(cmp);return I(p[0],p[3]);
 }
 function square(x) {
   if(cmp(x[0],Z)>=0)return I(mul(x[0],x[0]),mul(x[1],x[1]));
   if(cmp(x[1],Z)<=0)return I(mul(x[1],x[1]),mul(x[0],x[0]));
   let a=mul(x[0],x[0]),b=mul(x[1],x[1]);return I(Z,cmp(a,b)>0?a:b);
 }
 function divPositive(a,b) {
   if(cmp(b[0],Z)<=0)throw Error("No certified positive denominator");
   return I(div(a[0],b[1]),div(a[1],b[0]));
 }
 const scaled=(x,q)=>times(x,I(q)),af=x=>F(abs(x[0]),x[1]);
 const eps=F(1n,100000000n),scale=F(1000000000000n);
 const k=[2,3,4,5,6],n=k.map(x=>BigInt((41-2*x)**3)),
       weight=n.map((x,i)=>i===4?x:x-n[i+1]);
 if(k.length!==5||weight.some(x=>x<=0n))throw Error("Invalid mask shell sizes");
 const G=k.map(x=>{
   if(!Array.isArray(source[x])||source[x].length!==5)throw Error("M13 input dimensions mismatch");
   return source[x].map(pair=>{
     if(!Array.isArray(pair)||pair.length!==2)throw Error("M13 coefficient endpoint pair");
     let lo=parseEndpoint(pair[0]),hi=parseEndpoint(pair[1]);
     if(cmp(lo,hi)>0)throw Error("M13 direct coefficient interval inverted");
     // Exact independent perturbation of EACH of 25 coefficients.
     return scaled(I(sub(lo,mul(eps,af(lo))),add(hi,mul(eps,af(hi)))),scale);
   });
 });
 const S=G.map((row,i)=>row.map((x,j)=>{
    let nmr=i===4?scaled(x,F(n[i])):minus(scaled(x,F(n[i])),scaled(G[i+1][j],F(n[i+1])));
    return divPositive(nmr,I(F(weight[i])));
 }));
 function shellAt(t) {
   return S.map(row=>{
      let a=row[4];for(let j=3;j>=0;j--)a=plus(times(a,I(t)),row[j]);
      if(cmp(a[0],Z)<=0)throw Error("Shell positivity failed");
      return a;
   });
 }
 function profiledDistance(u,v) {
   const a=shellAt(u),b=shellAt(v);
   let numerator=I(Z),denominator=I(Z),dot=I(Z);
   for(let i=0;i<5;i++){
     denominator=plus(denominator,scaled(square(b[i]),F(weight[i])));
     dot=plus(dot,scaled(times(a[i],b[i]),F(weight[i])));
     for(let j=0;j<i;j++){
       const cross=minus(times(a[i],b[j]),times(a[j],b[i]));
       numerator=plus(numerator,scaled(square(cross),F(weight[i]*weight[j])));
     }
   }
   if(cmp(dot[0],Z)<=0)throw Error("Gain positivity failed");
   return divPositive(numerator,denominator);
 }
 const alpha=F(1541n,50000n),delta=F(1257n,50000n);
 const betaW=F(1n,1000000n),betaL=F(71n,12500n),betaR=F(1399n,25000n);
 if(cmp(alpha,F(1n,5n))>=0||cmp(betaW,Z)<=0||cmp(sub(alpha,betaW),delta)<=0||
    cmp(sub(alpha,betaL),delta)!==0||cmp(sub(betaR,alpha),delta)!==0)
   throw Error("Witness admissibility test failed");
 const witness=profiledDistance(alpha,betaW),
  left=profiledDistance(alpha,betaL),right=profiledDistance(alpha,betaR);
 const gapLeft=sub(left[0],witness[1]), gapRight=sub(right[0],witness[1]);
 if(cmp(gapLeft,Z)<=0||cmp(gapRight,Z)<=0)throw Error("Pointwise robust witness was NOT certified");
 function sci(f) {
   if(f[0]===0n)return "0";
   let a=abs(f[0]).toString(),b=f[1].toString();
   let al=a.slice(0,16),bl=b.slice(0,16);
   let av=Number(al)/10**(al.length-1),bv=Number(bl)/10**(bl.length-1);
   let x=av/bv,e=a.length-b.length;
   if(x>=10){x/=10;e+=1;}else if(x<1){x*=10;e-=1;}
   return (f[0]<0n?"-":"")+x.toPrecision(12)+"e"+(e>=0?"+":"")+e;
 }
 return {
   artifact_id:"IW_M15_ROT005_INDEPENDENT_SOURCE_B25_POINTWISE_INTERVAL_REFEREE_001_20261113",
   source_git_blob:"a6f50fbe5904e580e84c87ee87c5ad043cdec5d0",
   source_coefficient_intervals:25,
   source_widening_epsilon:"1/100000000",
   alpha:"1541/50000",delta:"1257/50000",
   far_legal_beta:"1/1000000",nearest_left:"71/12500",nearest_right:"1399/25000",
   profile:"weighted positive-gain least-squares D² = wedge_sum / weighted_beta_norm²",
   source_scale:"all source g coefficients multiplied exactly by 10^12; D² printed times 10^24",
   weight:weight.map(x=>x.toString()),
   d2_times_1e24:{
     witness:[sci(witness[0]),sci(witness[1])],
     nearest_left:[sci(left[0]),sci(left[1])],
     nearest_right:[sci(right[0]),sci(right[1])]
   },
   lower_gap_D2_times_1e24:{left:sci(gapLeft),right:sci(gapRight)},
   certified_both_positive:true,
   legal_positive_gain_all_points:true,
   exact_rational_interval_arithmetic:true,
   independent_algorithm_no_geeky_certifier_invocation:true,
   ceiling:"POINTWISE_NEGATIVE_ONLY_NO_GLOBAL_NEAREST_AUDIT_NO_SOURCE_FIELD_REALIZABILITY_NO_NOVELTY_NO_CANON_NO_EXEC_SIGN"
 };
}
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module){
  const fs=require("fs"),crypto=require("crypto"),path=require("path");
  const filename=process.argv[2];if(!filename)throw Error("Pass frozen M13 original direct_B.json path");
  const bytes=fs.readFileSync(filename);
  const blob=crypto.createHash("sha1").update(Buffer.from("blob "+bytes.length+"\0")).update(bytes).digest("hex");
  if(blob!=="a6f50fbe5904e580e84c87ee87c5ad043cdec5d0")throw Error("ORIGINAL M13 SOURCE GIT BLOB MISMATCH");
  const summary=independentAudit(JSON.parse(bytes.toString("utf8")));
  const output=path.join(path.dirname(__filename),"m15_rot005_exact_negative_referee.json");
  fs.writeFileSync(output,JSON.stringify(summary,null,2)+"\n");
  process.stdout.write(JSON.stringify(summary,null,2)+"\n");
}
