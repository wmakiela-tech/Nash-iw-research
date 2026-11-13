#!/usr/bin/env node
"use strict";
/* M15 ROT008: new independent rational interval KKT checker, Geeky-S12 ROT016.
 * Original M13 direct_B.json Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0.
 * Node 18 stdlib. No Geeky-S12 mathematical code imported or invoked.
 */
function audit016(data){
 const abs=x=>x<0n?-x:x;
 function gcd(a,b){a=abs(a);b=abs(b);while(b){let c=a%b;a=b;b=c;}return a||1n;}
 function F(a,b=1n){if(Array.isArray(a))return a;a=BigInt(a);b=BigInt(b);if(!b)throw Error("ZERO_DIV");if(b<0n){a=-a;b=-b;}let g=gcd(a,b);return[a/g,b/g];}
 const z=F(0),one=F(1),add=(a,b)=>F(a[0]*b[1]+a[1]*b[0],a[1]*b[1]),sub=(a,b)=>add(a,[-b[0],b[1]]),
 mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]),
 cmp=(a,b)=>{let c=a[0]*b[1]-b[0]*a[1];return c<0n?-1:c>0n?1:0;};
 function decimal(s){
  s=s.trim();let sign=1n;if(s[0]==="-"){sign=-1n;s=s.slice(1);}else if(s[0]==="+")s=s.slice(1);
  let [mant,exp="0"]=s.toLowerCase().split("e"),[int,frac=""]=mant.split(".");
  let e=Number(exp)-frac.length, v=sign*BigInt((int||"0")+frac);
  return e>=0?F(v*10n**BigInt(e)):F(v,10n**BigInt(-e));
 }
 function endpoint(bracket){
  let m=bracket.match(/^\[([^,]+),\s*([^\]]+)\]$/);
  if(!m)throw Error("INVALID_ORIGINAL_BRACKET");
  let a=decimal(m[1]),b=decimal(m[2]);if(cmp(a,b)!==0)throw Error("DIRECTIONAL_NOT_POINT");
  return a;
 }
 function iv(a,b=a){if(cmp(a,b)>0)throw Error("INVERTED_INTERVAL");return[a,b];}
 const ia=(a,b)=>iv(add(a[0],b[0]),add(a[1],b[1])),
 is=(a,b)=>iv(sub(a[0],b[1]),sub(a[1],b[0]));
 function im(a,b){let products=[mul(a[0],b[0]),mul(a[0],b[1]),mul(a[1],b[0]),mul(a[1],b[1])].sort(cmp);return iv(products[0],products[3]);}
 const sc=(a,q)=>im(a,iv(F(q)));
 const ratio=(a,b)=>{if(cmp(b[0],z)<=0)throw Error("DENOM_NOT_POS");return iv(div(a[0],b[1]),div(a[1],b[0]));};
 function square(a){
  if(cmp(a[0],z)>=0)return iv(mul(a[0],a[0]),mul(a[1],a[1]));
  if(cmp(a[1],z)<=0)return iv(mul(a[1],a[1]),mul(a[0],a[0]));
  const u=mul(a[0],a[0]),v=mul(a[1],a[1]);return iv(z,cmp(u,v)>0?u:v);
 }
 const ns=[2,3,4,5,6].map(k=>BigInt((41-2*k)**3)),
 w=ns.map((n,i)=>i===4?n:n-ns[i+1]),
 eps=F(1n,10000000n),ss=F(1000000000000n),
 alpha=F(1n,20n),beta=F(3n,40n),kappa=F(33n,500n),
 u=sub(one,kappa),v=add(one,kappa);
 const source=[2,3,4,5,6].map(k=>{
  if(!Array.isArray(data[k])||data[k].length!==5)throw Error("BAD_M13_SHAPE");
  return data[k].map(pair=>{
   if(!Array.isArray(pair)||pair.length!==2)throw Error("BAD_M13_PAIR");
   let a=endpoint(pair[0]),b=endpoint(pair[1]);if(cmp(a,b)>0)throw Error("SOURCE_ORDER");
   return iv(a,b);
  });
 });
 const widened=source.map(row=>row.map(([a,b])=>{
  const am=F(abs(a[0]),a[1]),bm=F(abs(b[0]),b[1]);
  return sc(iv(sub(a,mul(eps,am)),add(b,mul(eps,bm))),ss);
 }));
 function shell(coeff) {
  return coeff.map((row,i)=>row.map((x,j)=>{
   const numer=i<4?is(sc(x,ns[i]),sc(coeff[i+1][j],ns[i+1])):sc(x,ns[i]);
   return ratio(numer,iv(F(w[i])));
  }));
 }
 function evalAt(coef,t){
  let a=iv(z);for(let i=coef.length-1;i>=0;i--)a=ia(im(a,iv(t)),coef[i]);
  if(cmp(a[0],z)<=0)throw Error("SOURCE_SHELL_NOT_POSITIVE");
  return a;
 }
 const S=shell(widened),a=S.map(x=>evalAt(x,alpha)),b=S.map(x=>evalAt(x,beta));
 const r=a.map((x,i)=>ratio(x,b[i])),A=b.map((x,i)=>sc(square(x),w[i]));
 for(let i=1;i<5;i++)if(cmp(r[i-1][1],r[i][0])>=0)throw Error("RATIO_ORDER_UNDECIDED");
 // Pair KKT stationarity, using two active shells; then test ALL strict hinge signs.
 const denominator=ia(sc(A[0],mul(u,u)),sc(A[4],mul(v,v)));
 const numerator=ia(sc(im(A[0],r[0]),u),sc(im(A[4],r[4]),v));
 const c=ratio(numerator,denominator);
 const lo=r.map(x=>is(x,sc(c,u))),hi=r.map(x=>is(x,sc(c,v)));
 if(cmp(lo[0][1],z)>=0||cmp(hi[4][0],z)<=0)throw Error("EXTREME_ACTIVE_SET_FAIL");
 for(let i=1;i<4;i++)if(cmp(lo[i][0],z)<=0||cmp(hi[i][1],z)>=0)throw Error("INNER_INACTIVE_FAIL_"+i);
 const g=is(sc(r[4],u),sc(r[0],v));
 if(cmp(g[0],z)<=0)throw Error("STRICT_POSITIVE_CALIBRATION_GAP_FAIL");
 const loss=ratio(im(im(A[0],A[4]),square(g)),denominator);
 // source signal scale: s multiplied by 10^12, hence loss by 10^24.
 const boundLo=F(43n,10000000n),boundHi=F(442n,100000000n);
 const conservativeBound=(cmp(loss[0],boundLo)>0&&cmp(loss[1],boundHi)<0);
 // Separate midpoint exactly rational, direct clipped five-term optimizer vs KKT expression.
 const center=source.map(row=>row.map(([l,h])=>sc(iv(div(add(l,h),F(2))),ss)));
 const M=shell(center),aa=M.map(x=>evalAt(x,alpha)).map(x=>x[0]),bb=M.map(x=>evalAt(x,beta)).map(x=>x[0]);
 const R=aa.map((x,i)=>div(x,bb[i])),B=bb.map((x,i)=>mul(F(w[i]),mul(x,x)));
 const dm=add(mul(B[0],mul(u,u)),mul(B[4],mul(v,v)));
 const cm=div(add(mul(B[0],mul(u,R[0])),mul(B[4],mul(v,R[4]))),dm);
 let clipped=z,active=[];
 for(let i=0;i<5;i++){
  let target=R[i],fit,which;
  if(cmp(target,mul(u,cm))<0){fit=mul(u,cm);which="LOW";}
  else if(cmp(target,mul(v,cm))>0){fit=mul(v,cm);which="HIGH";}
  else{fit=target;which="NONE";}
  active.push(which);
  clipped=add(clipped,mul(B[i],mul(sub(target,fit),sub(target,fit))));
 }
 const closed=div(mul(mul(B[0],B[4]),mul(sub(mul(u,R[4]),mul(v,R[0])),sub(mul(u,R[4]),mul(v,R[0])))),dm);
 if(cmp(clipped,closed)!==0||active.join(",")!=="LOW,NONE,NONE,NONE,HIGH")throw Error("MIDPOINT_EXACT_KKT_FAIL");
 const inner=(x,y)=>x.reduce((acc,xi,i)=>add(acc,mul(F(w[i]),mul(xi,y[i]))),z);
 const common=sub(inner(aa,aa),div(mul(inner(aa,bb),inner(aa,bb)),inner(bb,bb)));
 if(cmp(common,z)<=0)throw Error("COMMON_GAIN_BASELINE_NONPOS");
 function display(q){
  if(q[0]===0n)return "0";
  const a=abs(q[0]).toString(),b=q[1].toString(),aa=a.slice(0,15),bb=b.slice(0,15);
  let x=(Number(aa)/10**(aa.length-1))/(Number(bb)/10**(bb.length-1)),ex=a.length-b.length;
  if(x>=10){x/=10;ex++;}else if(x<1){x*=10;ex--;}
  return(q[0]<0n?"-":"")+x.toPrecision(12)+"e"+(ex>=0?"+":"")+ex;
 }
 return {
  artifact_id:"IW_M15_ROT008_ORIGINAL_M13_B25_TWO_ACTIVE_CONVEX_RISK_INDEPENDENT_REFEREE_001_20261113",
  original_M13_git_blob:"a6f50fbe5904e580e84c87ee87c5ad043cdec5d0",
  source_coefficients:25,relative_box_epsilon:"1/10000000",
  alpha:"1/20",beta:"3/40",kappa:"33/500",
  two_active_shells:[1,5],three_inactive_shells:[2,3,4],
  certified_full_box_active_set:true,
  exact_KKT_convex_profile_global_optimum:true,
  scaled_loss_1e24_outer_interval:{lower:display(loss[0]),upper:display(loss[1])},
  strict_simple_risk_bound_4p30eMinus6_to_4p42eMinus6:conservativeBound,
  original_source_midpoint_scaled_risk_1e24:display(clipped),
  original_source_midpoint_common_only_scaled_risk_1e24:display(common),
  midpoint_relative_to_common:display(div(clipped,common)),
  original_midpoint_exact_5_hinge_terms_equal_pair_formula:true,
  center_gain_interval:{lower:display(c[0]),upper:display(c[1])},
  active_set_guard:{
   shell1_upper_r_minus_u_c:display(lo[0][1]),
   shell5_lower_r_minus_v_c:display(hi[4][0]),
   middle_r_minus_u_c_lower:[1,2,3].map(i=>display(lo[i][0])),
   middle_r_minus_v_c_upper:[1,2,3].map(i=>display(hi[i][1]))
  },
  scope:"INTERNAL_NONBLIND_I1_MATHEMATICAL_SOURCE_AUXILIARY_ONLY_NO_HISTORIC_RUNTIME_NO_PHYSICS_NO_CANON"
 };
}
if(typeof require!=="undefined"&&require.main===module){
 const fs=require("fs"),crypto=require("crypto"),path=require("path");
 const p=process.argv[2];if(!p)throw Error("Pass frozen original M13 direct_B.json");
 const bytes=fs.readFileSync(p),blob=crypto.createHash("sha1").update(Buffer.from("blob "+bytes.length+"\0")).update(bytes).digest("hex");
 if(blob!=="a6f50fbe5904e580e84c87ee87c5ad043cdec5d0")throw Error("ORIGINAL_SOURCE_M13_GIT_BLOB_MISMATCH");
 const result=audit016(JSON.parse(bytes.toString("utf8")));
 fs.writeFileSync(path.join(path.dirname(__filename),"m15_rot008_two_active_results.json"),JSON.stringify(result,null,2)+"\n");
 process.stdout.write(JSON.stringify(result,null,2)+"\n");
 if(!result.strict_simple_risk_bound_4p30eMinus6_to_4p42eMinus6)process.exitCode=1;
}
