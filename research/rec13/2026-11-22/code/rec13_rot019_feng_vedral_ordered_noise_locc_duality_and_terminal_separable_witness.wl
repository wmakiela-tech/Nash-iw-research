(* REC13 ROT019 original independent Wolfram replay of Feng-Vedral v2 source (2026-11-10).
   Distinguish unrestricted final separable state preparation (LOCC gap zero for ONE input)
   from LOCC applied BEFORE externally fixed D_r^tensor2 (positive universal witness gap).
   No experiment, no general interleaved LOCC theorem, no novelty or canon claim. *)
Module[{GG=6.67430*^-11,hbar=1.054571817*^-34,mm=1.*^-14,LL=40.*^-6,dd=10.*^-6,rr=.1,th,xx,yy,zz,ii,psi,rho,pst,pt,w,v,h,inv,weights,p,prep,neg,bound,norm,allgood},
 th=GG*mm^2/(4*hbar)*(1/(LL-dd)+1/(LL+dd)-2/LL);
 xx={{0,1},{1,0}};yy={{0,-I},{I,0}};zz={{1,0},{0,-1}};ii=IdentityMatrix[2];
 psi=Exp[I*th*{1,-1,-1,1}]/2;rho=Outer[Times,psi,Conjugate[psi]];
 h=Table[Count[MapThread[Unequal,{IntegerDigits[i-1,2,2],IntegerDigits[j-1,2,2]}],True],{i,4},{j,4}];
 pst=rho*rr^h;
 pt[a_]:=ArrayReshape[Transpose[ArrayReshape[a,{2,2,2,2}],{1,4,3,2}],{4,4}];
 v={-1,I,-I,1}/2;w=pt[Outer[Times,v,Conjugate[v]]];inv=w*rr^(-h);
 p=<|"XI"->Re[N[Tr[KroneckerProduct[xx,ii].pst]]],
 "IX"->Re[N[Tr[KroneckerProduct[ii,xx].pst]]],
 "XX"->Re[N[Tr[KroneckerProduct[xx,xx].pst]]],
 "ZY"->Re[N[Tr[KroneckerProduct[zz,yy].pst]]],
 "YZ"->Re[N[Tr[KroneckerProduct[yy,zz].pst]]]|>;
 weights=Values[p];
 (* Identity I4/4 and each (I4 + s PauliA tensor PauliB)/4 is an explicit
    separable mixture of local Pauli-eigenstate projectors. *)
 prep=(1-Total[Abs[weights]])*IdentityMatrix[4]/4;
 Do[prep=prep+Abs[weights[[i]]]*(IdentityMatrix[4]+Sign[weights[[i]]]*
   KroneckerProduct[Switch[i,1,xx,2,ii,3,xx,4,zz,5,yy],
                    Switch[i,1,ii,2,xx,3,xx,4,yy,5,zz]])/4,{i,5}];
 neg=Abs[Sin[2*th]]/2;
 norm=Max[Abs[Eigenvalues[N[inv]]]];
 bound=neg/(2*norm);
 allgood=And[
  Max[Abs[Flatten[prep-pst]]]<1.*^-12,
  Abs[bound-rr^2*Abs[Sin[2*th]]/(1+2*rr-rr^2)]<1.*^-12,
  Min[Eigenvalues[N[pt[pst]]]]>0,
  1-Total[Abs[weights]]>0,
  Abs[Tr[w.rho]+neg]<1.*^-12
 ];
 <|"status"->If[allgood,"SOURCE_PROOF_CHECK_PASS","SCIENCE_FAIL_CLOSED"],
 "theta"->th,"r"->rr,"ppt_target_min"->Min[Eigenvalues[N[pt[pst]]]],
 "separable_prep_weight_I4"->(1-Total[Abs[weights]]),
 "local_product_coefficients"->p,
 "terminal_LOCC_prep_max_abs_entry_error"->Max[Abs[Flatten[prep-pst]]],
 "pure_target_negativity"->neg,"inverse_noise_witness_norm"->norm,
 "fixed_postcomposed_noise_LOCC_trace_distance_lower_bound"->bound,
 "lower_bound_formula"->"r^2*Abs[Sin[2 Theta]]/(1+2 r-r^2)",
 "strict_scope"->"One input |++>, LOCC before fixed D_r tensor D_r, not arbitrary interleaved noise; no lab data or physical novelty."|>
]
