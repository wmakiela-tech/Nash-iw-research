(* Mech-S8 ROT020: original AUTHOR Wu-Xu v2 numeric JLD2 audit.
   Original repo Fenyutanchan/Primordial-Black-Hole commit
   d395183674cace6c9906a8911bdeb7234ba4040d (2025-12-30).
   Observes original 100x100 Y_P and chi2 source, archived notebook pipeline.
   SAME-X counterfactual is NOT a calibrated corrected PBH bound.
   No native Julia solver execution or JCAP figure-release identity claim.
   Requires Wolfram Language HDF5 support and network. *)
Module[{root,file,nb,m,b,y,c,yt,ct,source,fig,flags,err,result},
 root="https://raw.githubusercontent.com/Fenyutanchan/Primordial-Black-Hole/"<>
      "d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/";
 file=URLDownload[root<>"data/out/scanning.jld2"];
 nb=URLDownload[root<>"main.ipynb"];
 If[FileByteCount[file]!=151089||
    FileHash[file,"SHA256","HexString"]!=
    "51844a46ca904f57f941e0d0ebc3b5920c38bace76eea9e1d89cb5fd1f2c5786",
    Return[<|"status"->"ORIGINAL_JLD2_HASH_FAIL"|>]];
 If[FileByteCount[nb]!=2526919||
    FileHash[nb,"SHA256","HexString"]!=
    "61d427c4de71b3920387234f6808ea7dee759d9166c77e1a9090695c5f5202d1",
    Return[<|"status"->"ORIGINAL_NOTEBOOK_HASH_FAIL"|>]];
 m=Import[file,{"HDF5","Data","/m_PBH_list [gram]"}];
 b=Import[file,{"HDF5","Data","/β_PBH_list"}];
 y=Import[file,{"HDF5","Data","/Y_P_mat"}];
 c=Import[file,{"HDF5","Data","/chi2_mat"}];
 yt=2 y/(2+y);
 ct=((yt-.245)/.003)^2;
 err=Max[Abs[Flatten[c-((y-.245)/.003)^2]]];
 source=StringJoin[Lookup[#,"source",{}]]&/@
      Lookup[Import[nb,"RawJSON"],"cells",{}];
 fig=Select[source,StringContainsQ[#,"scanning.jld2"]&];
 flags=<|
  "arrays_100_by_100"->(Dimensions[y]==={100,100}&&Dimensions[c]==={100,100}),
  "axes_100"->(Dimensions[m]==={100}&&Dimensions[b]==={100}),
  "chi2_formula_all_10000"->(err<10^-9),
  "notebook_loads_scanning_jld2"->(Length[fig]>=1),
  "notebook_uses_heatmap_Y"->AnyTrue[fig,StringContainsQ[#,"Yₚ_mat"]&&StringContainsQ[#,"heatmap!"]&],
  "notebook_uses_contour_chi2_4"->AnyTrue[fig,StringContainsQ[#,"χ²_mat"]&&StringContainsQ[#,"levels=[4]"]&],
  "notebook_saves_Y_P_pdf_and_png"->AnyTrue[fig,StringContainsQ[#,"plot_basename = \"Y_P\""]&&
       StringContainsQ[#,"\".pdf\""]&&StringContainsQ[#,"\".png\""]&],
  "uncalibrated_baseline_not_observational"->(yt[[1,1]]<.239)
 |>;
 result=<|
  "status"->If[And@@Values[flags],"PASS","FAIL"],
  "checks"->flags,
  "jld2_sha256"->FileHash[file,"SHA256","HexString"],
  "notebook_sha256"->FileHash[nb,"SHA256","HexString"],
  "source_rows"->Dimensions[y],
  "mass_g_range"->{Min[m],Max[m]},
  "beta_range"->{Min[b],Max[b]},
  "chi2_max_abs_residual"->err,
  "source_Y_range"->{Min[y],Max[y]},
  "same_X_correct_Y_range"->{Min[yt],Max[yt]},
  "source_chi2_le_4_cells"->Count[Flatten[c],v_/;v<=4],
  "uncalibrated_same_X_chi2_le_4_cells"->Count[Flatten[ct],v_/;v<=4],
  "first_Y_code"->y[[1,1]],
  "first_Y_correct_same_X"->yt[[1,1]],
  "code_Y_needing_Y_correct_0p251"->(2*.251/(2-.251)),
  "claim_ceiling"->"AUTHOR_REPO_SOURCE_GRID_AND_NOTEBOOK_LINK_ONLY / NO_CALIBRATED_PHYSICAL_PBH_BOUND / NO_JCAP_RELEASE_ID / NO_CANON / NO_EXEC_SIGN"|>;
 Print[result["status"]];
 result
]