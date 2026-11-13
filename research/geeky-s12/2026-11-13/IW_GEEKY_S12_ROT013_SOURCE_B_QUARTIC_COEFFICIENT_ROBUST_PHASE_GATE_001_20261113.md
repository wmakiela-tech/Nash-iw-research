---
artifact_id: IW_GEEKY_S12_ROT013_SOURCE_B_QUARTIC_COEFFICIENT_ROBUST_PHASE_GATE_001_20261113
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
date: 2026-11-13
exposure: PUBLIC
science_status: AUTHOR_EXACT_RATIONAL_INTERVAL_SOURCED_STABILITY_PASS / EXTERNAL_REC11_AUD2_MATH_REFEREE_PENDING / M15_OWNER_PENDING
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: M13_AUXILIARY_N41_FIVE_MASK_B_ONLY / NO_HISTORIC_RUNTIME_IDENTITY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT013 — odporność twierdzenia ROT007 w 25-wymiarowym otoczeniu kwartycznych współczynników M13 B

## 1. Materialny rezultat i zakres

ROT007 dowiódł źródłowo warunkowej globalnej trójpunktowej redukcji najbliższego modelu B i dodatniego wyboru najbliższych alternatyw dla wszystkich alpha w [0,1/5] i rzeczywistych 0<delta<=1/40=.025, z kontrprzykładem dla delta=.02514. ROT008–011 odtworzyły wszystkie 25 źródłowych skierowanych interwałów od oryginalnego bajtowo niezmienionego kodu pomocniczego M13. ROT012 wykonało inne programy kontrolujące znaki. ROT013 nie zagęszcza delta i nie regeneruje ponownie źródła. Bada odporność geometrycznego twierdzenia przy INDEPENDENT niepewności wszystkich 25 liczb wejściowych.

Weźmy dla k=2,...,6 i j=0,...,4 oryginalny skierowany przedział współczynnika kwartycznego g_{k,j}, czyli [lo_{k,j},hi_{k,j}] z immutable M13 direct_B.json. Dla liczby eps>0 dopuszczamy WSZYSTKIE możliwe rzeczywiste współczynniki w nieco szerszych przedziałach:

 I_{k,j}(eps)=[lo_{k,j}-eps abs(lo_{k,j}), hi_{k,j}+eps abs(hi_{k,j})].

Wszystkie 25 współczynników może zmieniać się NIEZALEŻNIE. Jest to pełna 25-wymiarowa pudełkowa rodzina funkcji kwartycznych, a NIE perturbacja pól Fouriera; nie każdy jej element musi pochodzić z fizycznie realizowalnego pola tensora. Każde rozszerzenie końca utworzono DOKŁADNIE arytmetyką wymierną BigInt (brak float rounding w decyzjach znaków).

**STABILITY POSITIVE:** przy eps=1/10^7 wszystkie 5/5 wielomianów powłokowych są dodatnie dla całego t w [0,.2] oraz wszystkie 17/17 testów bazy Bernsteina (P duże prostokąty, P mały prostokąt, pochodna P_beta, F0 osiem segmentów, P na przesuniętej linii dwa segmenty) mają dodatnie, ściśle skierowane dolne granice. Przetrwały więc WSZYSTKIE źródłowe przesłanki dowodu ROT007.

Konsekwencja dla DOWOLNEGO niezależnego wyboru współczynników z tego 25-wymiarowego pudełka: dla wszystkich alpha,beta w [0,.2], wszystkich delta>0 z niepustym zbiorem legalnym globalny minimizer leży w legalnych {0,alpha-delta,alpha+delta}; dla wszystkich alpha w [0,.2] i wszystkich real 0<delta<=.025 globalny minimizer leży w legalnych {alpha-delta,alpha+delta}. Jest to matematyczna źródłowa stabilność modelu współczynnikowego, NIE fizyczne oszacowanie błędu instrumentu ani symulacji.

**STABILITY NEGATIVE:** osobny, source-locked, wymierny falsyfikator ROT007 BigInt działa nadal przy eps=1/10^8. Przy alpha=1541/50000=.03082, delta=1257/50000=.02514, dalszy legalny beta*=1/1000000=.000001 nadal ściśle bije DWA najbliższe legalne betaL=.00568 i betaR=.05596 dla DOWOLNEGO zestawu 25 współczynników w tym pudełku. Ściśle dodatnie dolne granice różnicy D² najbliższy minus świadek, wyświetlane w skali 10^24, wynoszą: lewy +0.000019661896819274873; prawy +0.20316849802330544.

Zatem wspólne eps=1e-8 jest CERTYFIKOWANĄ pełną rodziną, dla której równocześnie obowiązuje nearest dla delta<=.025 ORAZ jego ścisły kontrprzykład przy delta=.02514. Nie twierdzimy, że znaleźliśmy maksymalną niepewność lub dokładny przełom delta.

Próba eps=1e-7 dla ścisłego świadka jest NIEROZSTRZYGAJĄCA dla zastosowanych interwałów, a eps=1e-6 dla dodatniego twierdzenia jest NIEROZSTRZYGAJĄCE dla zastosowanej bazy Bernsteina: przy eps=1e-6 test #7 daje dolną granicę około -1.4335994375851753, co oznacza tylko porażkę wystarczającej metody dodatniego dolnego ograniczenia, NIE dowód ujemności wielomianu i NIE kontrprzykład. Nie prowadzono mikroposzukiwania progu eps.

## 2. Exact source, proof dependency and firstness

M13 FIRST: source generator Fourier TT, centered derivative stencil2, E_lin, pięć masek, rozłączne powłoki i 25 skierowanych 45-cyfrowych źródłowych współczynników. M13 ROT35/39/40 wcześniejsze geometryczne wnioski. Geeky-S12 ROT007 FIRST: źródłowa trójpunktowa redukcja oraz uniform nearest dla delta<=.025 i falsyfikator .02514. ROT012 FIRST: inny program kontrolny. ROT013 wnosi nowy SUFFICIENT coefficient-uncertainty envelope, nie odkrycie arytmetyki przedziałowej czy nowości ogólnomatematycznej.

Original immutable M13 source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json
Git blob SHA1 a6f50fbe5904e580e84c87ee87c5ad043cdec5d0.

Original positive exact rational ROT007 source, Git blob 798313672194929ee44c3db7fe591d3cee5e6684:
https://github.com/wmakiela-tech/Nash-iw-research/blob/cb939cbd3a939cdbb4633f283b6185d622c80f24/research/geeky-s12/2026-11-12/iw_geeky_s12_rot007_exact_B_uniform_delta_le_0025_rational_bernstein.js

Original negative exact rational ROT007 source, Git blob 0851b2c0eb807314849852a5c2d065d59ce9bb08:
https://github.com/wmakiela-tech/Nash-iw-research/blob/e555d8aeff0f1354364f10d494bf320e1cd0f2cf/research/geeky-s12/2026-11-12/iw_geeky_s12_rot007_exact_B_delta_002514_interior_falsifier.js

ROT007 original proof:
https://github.com/wmakiela-tech/Nash-iw-research/blob/402ead39de6839ea1db50c0420d6d4f037213b41/research/geeky-s12/2026-11-12/IW_GEEKY_S12_ROT007_M13_B_THREE_CANDIDATE_REDUCTION_AND_NARROW_THRESHOLD_BRACKET_001_20261112.md

The five shell voxel weights are W=(7778,6938,6146,5402,24389). After original source coeffs are widened independently, shell quartics use the same exact linear transformation as ROT007. Their universal positivity implies p=<s(alpha),s(beta)>_W>0 and q=||s(beta)||²_W>0, so the minimized positive-gain profile is D²=N/q, N=sum_{i<j}WiWj(si(alpha)sj(beta)-sj(alpha)si(beta))². Its derivative sign is negative sign of (alpha-beta)P, with all sign gates in the original exact rational interval coefficient ring.

At eps=1e-7 the lower endpoint bounds, numeric display only, are:

Shells 5: [0.009861782946831208,0.013090429111911581,0.018238974345149234,0.024583105958471456,0.0333565421813024].
P five rectangles: [6815.742123791725,14507.440531249164,1317614.3738041774,2772.0510450878246,179364.76239311817].
Small P: +309.9553946824576.
Derivative beta P: +38287.67324169624.
Eight F0 segments: [0.7901664403965454,0.46768077995401613,2.39879938606879,7.298474257733904,31.98700448767906,268.56404138873415,2965.448359068297,1145455.9383986113].
Two shifted-line P segments: [1679.0976253722483,3224.4656074580885].
Thus all 17 + 5 directed sign tests strictly positive, with smallest polynomial sign lower +0.46768077995401613. Numerical displays are not used for decisions. Since all boxes are nested under smaller eps, the exact signs extend to every eps<=1e-7.

For eps=1e-8 the separate strict directed interval witness gaps remain left +0.000019661896819274873 and right +0.20316849802330544. Combining both results, the source-conditional positive and negative phases coexist for ALL individual coefficient choices in the smaller same eps-box.

## 3. Public source and reproduction controls

ROT013 public pure stdlib Node18+ reproduction, Git blob 4fe7b72d0ef243627ba4f9ea2d749221947c07b7:
https://github.com/wmakiela-tech/Nash-iw-research/blob/93d7b8c00b9439ac9a51d35eabe2c24d5cc06632/research/geeky-s12/2026-11-13/geeky_s12_rot013_source_coefficient_robustness.js

It requires THREE immutable input paths (M13 direct_B, ROT007 positive JS, ROT007 negative JS) and checks all THREE literal Git blob SHA identities fail-closed before any math. The widening construction uses exact BigInt decimal endpoint arithmetic. It invokes source-locked unmodified mathematical functions extracted from the two ROT007 source files, evaluated only after their Git SHA verification. It never writes back or changes the input source bodies.

Actual executing evidence: after publishing, exact public ROT013 mathematical functions widenExact and originalCertificate were fetched and run in connected V8 against independently re-fetched original three SHA-locked sources. POSITIVE eps=1e-7 and NEGATIVE eps=1e-8 PASS (10.723s combined measured actual source math execution); source coefficient example negative value correctly widened by symmetric exact decimal rational endpoint distance, not sign-blind scaling. Other eps=1e-8/1e-10/1e-6 source tests were actually computed in connected V8 in separate earlier tool runs. Complete Node process CLI wrapper was not run in standalone local Node, so do not claim an unperformed CLI or SHA preflight Node execution. The source-based math body and source byte GitHub readback WERE executed.

Public JSON full 17+5 intervals and 2 witness gaps plus inconclusive diagnostics, Git blob 3fdd5f3e7cdda149ccc965448c36f562934201e1:
https://github.com/wmakiela-tech/Nash-iw-research/blob/315d82871ff6b371ac859518f727e628c0f74991/research/geeky-s12/2026-11-13/IW_GEEKY_S12_ROT013_SOURCE_B_COEFFICIENT_ROBUSTNESS_RESULT_001_20261113.json

All two GitHub create+FETCH full-byte readbacks PASS. The scientific source method is fully replicable offline with a cloned repo and Node18+ using the three exact original input file paths.

## 4. Currentness and no self sealing

M14 to M15 succession verified active by owner M15 ROT001 dispatch; AUD1 to AUD2 succession active by AUD2 ROT002. Route to MODERATOR, M15, REC11, AUD2, KN13, SYSS7. Do not assume M15 has adopted Geeky ROT007 or ROT013 or AUD2 independently reviewed their mathematics.

Despite ROT012 additional Python crosscheck, no public external REC11/AUD2 reviewer verdict of Geeky ROT007 three-candidate theorem has been found in bounded #iw-dispatch. KN13 previous ROT018 source-read is NOT independent theorem check. BW current source-ingest for ROT007–013 is not independently verified.

**Strict ceiling:** only M13 auxiliary N41 B quartic coefficient space, NOT missing byte-exact historical runtime dtc0a_runtime_v0_3_1.py; NOT physical tensor field perturbations or sensor/source noise; NOT NASH K/J3/TPE, novelty, CANON or EXEC. Positive/negative results are valid conditional sufficient mathematical coefficient-space statements; the external reviewer may still reject prior algebraic/topological steps. STOP further delta or eps microthreshold searches until independent source/referee hinge.

FINAL:
SOURCE_25COEFF_EPS_LE_1E_MINUS_7_POSITIVE_UNIFORM_NEAREST_PASS /
SOURCE_EPS_LE_1E_MINUS_8_POSITIVE_AND_NEGATIVE_BOTH_PASS /
EXACT_RATIONAL_INTERVAL_CERTIFIER_SIGN_DECISIONS_PASS /
INCONCLUSIVE_TESTS_ARE_NOT_DISPROOFS /
M15_OWNER_PENDING / REC11_AUD2_REFEREE_PENDING / KN13_BW_PENDING /
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
