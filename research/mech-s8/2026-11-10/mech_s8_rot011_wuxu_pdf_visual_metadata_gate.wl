(* IW_MECH_S8_ROT011, 2026-11-10. ORIGINAL SOURCE PDF FIGURE DIFFERENCE GATE.
   Downloads original author Git commit d395183 v2 and original arXiv v3 SOURCE.
   Compares actual raw-file SHA256, byte differences, rendered pixels (288 dpi),
   exported PageGraphics/PageObjects/PagePlaintext and PDF producer/creation date.
   Requires online Wolfram Language with PDF import. No Wolfram Hash[Import[...,"Byte"]]
   mislabelled as file checksum; FileHash is mandatory.
   This is NOT a historical executable build identity or physical PBH validation. *)
Module[{gurl, gu, archive, out, arxivPDF, gitPDF, bg, ba, delta, rg, ra,
    pg, pa, og, oa, tg, ta, dg, da, mc, result, checks},
 gurl="https://raw.githubusercontent.com/Fenyutanchan/Primordial-Black-Hole/"<>
      "d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/plots/Y_P.pdf";
 gitPDF=URLDownload[gurl];
 archive=URLDownload["https://arxiv.org/src/2509.05618v3"];
 out=CreateDirectory[];ExtractArchive[archive,out];
 arxivPDF=FileNameJoin[{out,"fig","Y_P.pdf"}];
 bg=BinaryReadList[gitPDF,"Byte"];
 ba=BinaryReadList[arxivPDF,"Byte"];
 delta=Flatten[Position[MapThread[Unequal,{bg,ba}],True]];
 rg=First[Import[gitPDF,{"PDF","PageImages"},ImageResolution->288]];
 ra=First[Import[arxivPDF,{"PDF","PageImages"},ImageResolution->288]];
 pg=Import[gitPDF,{"PDF","PageGraphics"}];
 pa=Import[arxivPDF,{"PDF","PageGraphics"}];
 og=Import[gitPDF,{"PDF","PageObjects"}];
 oa=Import[arxivPDF,{"PDF","PageObjects"}];
 tg=Import[gitPDF,{"PDF","PagePlaintext"}];
 ta=Import[arxivPDF,{"PDF","PagePlaintext"}];
 dg=Import[gitPDF,{"PDF","CreationDate"}];
 da=Import[arxivPDF,{"PDF","CreationDate"}];
 checks=<|
  "both_one_page"->(Import[gitPDF,{"PDF","PageCount"}]===1&&Import[arxivPDF,{"PDF","PageCount"}]===1),
  "expected_git_sha256"->(FileHash[gitPDF,"SHA256","HexString"]==="95f5249c880ef8411361f9cb1d06300c3042996f5a6c78b72f55b72ca74169b4"),
  "expected_arxiv_sha256"->(FileHash[arxivPDF,"SHA256","HexString"]==="453c2842636a2e4ca3b36cb6ee22b854fac943f0069f85debf2ec988b96f7fa9"),
  "equal_byte_count"->(Length[bg]===111995&&Length[ba]===111995),
  "257_byte_differences"->(Length[delta]===257),
  "diff_positions_match"->(First[delta]===111376&&Last[delta]===111648),
  "1800x1500_raster"->(ImageDimensions[rg]==={1800,1500}&&ImageDimensions[ra]==={1800,1500}),
  "exact_raster_equality"->(ImageData[rg,"Byte"]===ImageData[ra,"Byte"]),
  "exact_page_graphics_equality"->(pg===pa),
  "exact_page_objects_equality"->(og===oa),
  "exact_page_text_equality"->(tg===ta),
  "creation_date_differs"->(dg=!=da),
  "same_pdf_producer"->(Import[gitPDF,{"PDF","Producer"}]===Import[arxivPDF,{"PDF","Producer"}])
 |>;
 result=<|
  "return_id"->"IW_MECH_S8_ROT011_WUXU_Y_P_PDF_RENDER_EQUIVALENCE_METADATA_BYTE_GATE_001_20261110",
  "verification"->If[And@@Values[checks],"PASS","FAIL"],
  "checks"->checks,
  "files"-><|
   "original_author_git"-> <|"url"->gurl,"bytes"->FileByteCount[gitPDF],
       "sha256"->FileHash[gitPDF,"SHA256","HexString"],
       "creation_date"->ToString[dg,InputForm]|>,
   "arxiv_v3"-> <|"url"->"https://arxiv.org/src/2509.05618v3",
       "path_inside_archive"->"fig/Y_P.pdf","bytes"->FileByteCount[arxivPDF],
       "sha256"->FileHash[arxivPDF,"SHA256","HexString"],
       "creation_date"->ToString[da,InputForm]|>
   |>,
  "raster_pixel_dimensions"->ImageDimensions[rg],
  "different_byte_positions_1based"-><|"count"->Length[delta],
     "first"->First[delta],"last"->Last[delta]|>,
  "claim_ceiling"->"PDF_RENDER_AND_PAGE_GRAPHICS_IDENTITY_ONLY / NO_HISTORICAL_BUILD_ID / NO_PHYSICAL_PBH_BOUND / NO_CANON / NO_EXEC_SIGN"
 |>;
 Print[result["verification"]];
 result
]