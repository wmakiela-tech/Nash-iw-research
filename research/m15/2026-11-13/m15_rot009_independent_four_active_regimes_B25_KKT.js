#!/usr/bin/env node
"use strict";
/* M15 ROT009 independent author-logic ref for source-M13 B Geeky-S12 ROT017:
   exact BigInt directed rational 25D source box, four convex KKT branches,
   independent wedge formula, no original Geeky code imported.
   Usage: node this_file.js ORIGINAL_direct_B.json
*/
function audit(data){
 const abs=x=>x<0n?-x:x;
 function gcd(a,b){a=abs(a);b=abs(b);while(b){let t=a%b;a=b;b=t;}return a||1n;}
 function F(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("DIV_0");if(b<0n){a=-a;b=-b;}let g=gcd(a,b);return[a/g,b/g];}
 const Z=F(0),O=F(1);
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]), neg=a=>[-a[0],a[1]];
 const sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
 const cmp=(a,b)=>{let d=a[0]*b[1]-b[0]*a[1];return d<0n?-1:d>0n?1:0;};
 const mg=a=>[abs(a[0]),a[1]];
 function dec(s){
   s=s.trim();let sign=1n;if(s[0]==="-"){sign=-1n;s=s.slice(1);}else if(s[0]==="+")s=s.slice(1);
   let [base,ex="0"]=s.toLowerCase().split("e"),[p,q=""]=base.split("."),n=sign*BigInt((p||"0")+q),e=Number(ex)-q.length;
   return e>=0?F(n*10n**BigInt(e)):F(n,10n**BigInt(-e));
 }
 function rawPoint(s){let m=s.match(/^\[([^,]+),\s*([^\]]+)\]$/);if(!m)throw Error("DIRECTED_BRACKET_SYNTAX");let a=dec(m[1]),b=dec(m[2]);if(cmp(a,b)!==0)throw Error("ORIGINAL_SINGLE_CELL_NOT_POINT");return a;}
 function I(a,b=a){if(cmp(a,b)>0)throw Error("INTERVAL_ORDER");return[a,b];}
 const iz=()=>I(Z), ia=(a,b)=>I(add(a[0],b[0]),add(a[1],b[1])), is=(a,b)=>I(sub(a[0],b[1]),sub(a[1],b[0]));
 function im(a,b){let v=[mul(a[0],b[0]),mul(a[0],b[1]),mul(a[1],b[0]),mul(a[1],b[1])].sort(cmp);return I(v[0],v[3]);}
 const isc=(a,q)=>im(a,I(q)), id=(a,b)=>{if(cmp(b[0],Z)<=0)throw Error("DEN_NOT_POS");return I(div(a[0],b[1]),div(a[1],b[0]));};
 function sq(x){if(cmp(x[0],Z)>=0)return I(mul(x[0],x[0]),mul(x[1],x[1]));if(cmp(x[1],Z)<=0)return I(mul(x[1],x[1]),mul(x[0],x[0]));let a=mul(x[0],x[0]),b=mul(x[1],x[1]);return I(Z,cmp(a,b)>0?a:b);}
 const n=[2,3,4,5,6].map(k=>BigInt((41-2*k)**3)),w=n.map((v,i)=>i<4?v-n[i+1]:v);
 const alpha=F(1n,20n),beta=F(3n,40n),eps=F(1n,10000000n),scale=F(1000000000000n);
 const original=[2,3,4,5,6].map(k=>{
   if(!Array.isArray(data[k])||data[k].length!==5)throw Error("SOURCE_ARRAY_DIM");
   return data[k].map(pair=>{
      if(!Array.isArray(pair)||pair.length!==2)throw Error("SOURCE_CELL_DIM");
      let lo=rawPoint(pair[0]),hi=rawPoint(pair[1]);if(cmp(lo,hi)>0)throw Error("SOURCE_DIRECTED_ORDER");
      return I(lo,hi);
   });
 });
 function toShells(g){
   return g.map((row,i)=>row.map((coeff,j)=>{
      let weighted=isc(coeff,F(n[i]));
      if(i<4)weighted=is(weighted,isc(g[i+1][j],F(n[i+1])));
      return id(weighted,I(F(w[i])));
   }));
 }
 const uncertain=original.map(row=>row.map(q=>isc(I(sub(q[0],mul(eps,mg(q[0]))),add(q[1],mul(eps,mg(q[1])))),scale)));
 const shells=toShells(uncertain);
 function evalAt(poly,t){
   let v=iz();for(let j=poly.length-1;j>=0;j--)v=ia(im(v,I(t)),poly[j]);
   if(cmp(v[0],Z)<=0)throw Error("SHELL_POSITIVITY_FIXED_POINT_FAIL");
   return v;
 }
 const aval=shells.map(s=>evalAt(s,alpha)),bval=shells.map(s=>evalAt(s,beta));
 const r=aval.map((x,i)=>id(x,bval[i])),A=bval.map((x,i)=>isc(sq(x),F(w[i])));
 for(let i=1;i<5;i++)if(cmp(r[i-1][1],r[i][0])>=0)throw Error("RATIO_ORDER_FAIL");
 const center=original.map(row=>row.map(q=>isc(I(div(add(q[0],q[1]),F(2))),scale)));
 const mid=toShells(center);
 const am=mid.map(s=>evalAt(s,alpha)[0]),bm=mid.map(s=>evalAt(s,beta)[0]);
 const rm=am.map((x,i)=>div(x,bm[i])),Bm=bm.map((x,i)=>mul(F(w[i]),mul(x,x)));
 function display(x){
   if(x[0]===0n)return "0";let a=abs(x[0]).toString(),b=x[1].toString(),na=a.slice(0,18),nb=b.slice(0,18);
   let v=(Number(na)/10**(na.length-1))/(Number(nb)/10**(nb.length-1)),e=a.length-b.length;
   if(v>=10){v/=10;e++;}else if(v<1){v*=10;e--;}
   return (x[0]<0n?"-":"")+v.toPrecision(15)+"e"+(e>=0?"+":"")+e;
 }
 const configs=[
  {k:F(1n,100n),low:[0,1,2,3],high:[4]},
  {k:F(1n,25n),low:[0,1,2],high:[4]},
  {k:F(3n,50n),low:[0,1],high:[4]},
  {k:F(33n,500n),low:[0],high:[4]}
 ];
 let results=[];
 for(const c of configs){
   let u=sub(O,c.k),v=add(O,c.k);
   let act=[...c.low,...c.high],ts=act.map(i=>c.low.includes(i)?u:v);
   let denominator=iz(),numerator=iz();
   for(let t=0;t<act.length;t++){
      let i=act[t],mult=ts[t];
      denominator=ia(denominator,isc(A[i],mul(mult,mult)));
      numerator=ia(numerator,isc(im(A[i],r[i]),mult));
   }
   let gain=id(numerator,denominator);
   let classifications=[],margins=[];
   for(let i=0;i<5;i++){
     let l=is(r[i],isc(gain,u)),h=is(r[i],isc(gain,v)),state="";
     if(c.low.includes(i)){if(cmp(l[1],Z)>=0)throw Error("LOW_SIGN_FAIL k="+display(c.k)+" i="+i);state="LOW";margins.push(neg(l[1]));}
     else if(c.high.includes(i)){if(cmp(h[0],Z)<=0)throw Error("HIGH_SIGN_FAIL k="+display(c.k)+" i="+i);state="HIGH";margins.push(h[0]);}
     else {if(cmp(l[0],Z)<=0||cmp(h[1],Z)>=0)throw Error("INACTIVE_SIGN_FAIL k="+display(c.k)+" i="+i);state="INACTIVE";margins.push(l[0],neg(h[1]));}
     classifications.push(state);
   }
   // Independent positive wedge identity for exact globally minimized active loss:
   // sum_i Ai ri² - (sum_i Ai ti ri)²/(sum_i Ai ti²)
   // == [sum_{i<j} Ai Aj(ri tj-rj ti)²] / sum_i Ai ti².
   let wedge=iz();
   for(let i=0;i<act.length;i++)for(let j=i+1;j<act.length;j++){
     const ii=act[i],jj=act[j];
     const x=is(isc(r[ii],ts[j]),isc(r[jj],ts[i]));
     wedge=ia(wedge,im(im(A[ii],A[jj]),sq(x)));
   }
   const loss=id(wedge,denominator);
   if(cmp(loss[0],Z)<=0)throw Error("RISK_STRICT_LOWER_FAIL k="+display(c.k));
   // On exact ORIGINAL source rational midpoint, check min via TWO distinct identities.
   let xm=Z,ym=Z,zm=Z,lossDirect=Z;
   for(let j=0;j<act.length;j++){
     let i=act[j],t=ts[j];
     xm=add(xm,mul(Bm[i],mul(t,rm[i])));
     ym=add(ym,mul(Bm[i],mul(t,t)));
     zm=add(zm,mul(Bm[i],mul(rm[i],rm[i])));
   }
   const cm=div(xm,ym);
   let clip=Z;
   for(let i=0;i<5;i++){
     let pred=cmp(rm[i],mul(u,cm))<0?mul(u,cm):cmp(rm[i],mul(v,cm))>0?mul(v,cm):rm[i];
     clip=add(clip,mul(Bm[i],mul(sub(rm[i],pred),sub(rm[i],pred))));
   }
   const minMid=sub(zm,div(mul(xm,xm),ym));
   if(cmp(clip,minMid)!==0)throw Error("MIDPOINT_DERIVATION_NOT_EQUAL k="+display(c.k));
   let minSign=margins.reduce((p,q)=>cmp(p,q)<0?p:q);
   results.push({
      kappa:display(c.k),active_count:act.length,
      branch:classifications, source_box_kkt_all_strict:true,
      min_source_scaled_loss_1e24:{lower:display(loss[0]),upper:display(loss[1])},
      min_source_scaled_loss_lower_strict_positive:true,
      midpoint_loss_scaled_1e24:display(clip),
      midpoint_wedge_equals_quadratic_exact:true,
      strict_kkt_margin_rational_display:display(minSign)
   });
 }
 return {
  artifact_id:"IW_M15_ROT009_INDEPENDENT_SOURCE_B25_FOUR_KAPPA_5_4_3_2_KKT_REFEREE_001_20261113",
  source_original_git_blob:"a6f50fbe5904e580e84c87ee87c5ad043cdec5d0",
  source_25_coeff_box_epsilon:"1/10000000",alpha:"1/20",beta:"3/40",
  original_source_scale:"10^12",loss_scale:"10^24",
  proof_type:"exact directed rational interval 25D source, global convex KKT; independent wedge formula and midpoint clipped identity",
  universal_breakpoints_at_most:10,universal_convex_regions_at_most:11,
  four_regimes:results,
  scope:"I1_DIFFERENT_CELL_NONBLIND_SOURCE_MATH_ONLY_NOT_HISTORIC_RUNTIME_NOT_PHYSICAL_NOT_I3_NO_NOVELTY_NO_CANON_NO_EXEC_SIGN"
 };
}
if(typeof require!=="undefined"&&require.main===module){
 const fs=require("fs"),crypto=require("crypto"),path=require("path");
 const f=process.argv[2];if(!f)throw Error("Pass original direct_B.json");
 const bytes=fs.readFileSync(f);
 const blob=crypto.createHash("sha1").update(Buffer.from("blob "+bytes.length+"\0")).update(bytes).digest("hex");
 if(blob!=="a6f50fbe5904e580e84c87ee87c5ad043cdec5d0")throw Error("ORIGINAL_M13_GIT_BLOB_MISMATCH");
 const r=audit(JSON.parse(bytes.toString("utf8")));
 fs.writeFileSync(path.join(path.dirname(__filename),"m15_rot009_four_branch_exact_results.json"),JSON.stringify(r,null,2)+"\n");
 process.stdout.write(JSON.stringify(r,null,2)+"\n");
}
