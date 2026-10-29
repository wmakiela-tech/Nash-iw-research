---
artifact_id: GEEKY-S11-ROT033-NONSTATIONARY-E-SCHEDULE-DIFFUSION-BUDGET-ORDER-001
origin_cell: MGPT-BUD-01-SUCCESSOR-11 / Geeky-S11
date: 2026-10-29
problem_id: P3_DTC0A_SOURCE_E_VARIABLE_ALPHA_SCHEDULE_ORDER_VS_SMOOTHING_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
class: EXACT_NONSTATIONARY_LIE_INSERTION_SPECTRAL_KERNEL_AND_ORDER_FALSIFIER
status: ANALYTIC_PROOF_AND_12032_EXECUTED_TYPED_CHECKS_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S11 ROT033 — zmienny harmonogram filtracji: budżet wystarcza do stabilności, kolejność zmienia wynik

## 0. Stan wcześniejszy, nauka zewnętrzna i granice

Własna linia naukowa Geeky-S11: ROT015–017 wykryły nieidempotencję rzeczywistej wersji surowego projektora TT na parzystych siatkach i skonstruowały zgodny z rzeczywistością projektor ortogonalny **B=GA**. ROT021–023 ustanowiły gładkie świadki oraz matematyczną pamięć rzutowania. ROT024–026 zbadały identyfikowalność i nieprzemienność wielokrotnego E. **ROT027** jako pierwsza w linii wprowadziła dokładną średnią wszystkich pozycji transportu dla *jednego powtarzanego* E. **ROT029** podała dokładny algorytm różnic dzielonych dla tego samego E, a **ROT032** — ciągłe na całym stabilnym przedziale oszacowanie dwudołkowe oraz warunek \(\alpha_Nm_N/N^2\). ROT033 nie przypisuje sobie ponownie tych wyników: **nowością dla komórki jest różnorodny, czasowo niejednorodny ciąg filtrów i jego niewymienność względem pozycji Liego**.

Dojrzałe podstawy zewnętrzne: dyskretne filtry Fouriera, pochodne wielomianów macierzy, symetryzacja i nieautonomiczne schematy operatorowe; np. N. J. Higham, *Functions of Matrices* (SIAM, 2008), L. N. Trefethen, *Spectral Methods in MATLAB* (SIAM, 2000). Bez roszczenia do nowego twierdzenia, pierwszeństwa lub adopcji przez inne komórki.

**Zachowany niezmieniony pomocniczy plik źródłowy:** `deepseek_python_20260627_a87249.py`, SHA256 `23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801`. Oryginalnego historycznego `dtc0a_runtime_v0_3_1.py` brak. Jest to pełna niemaskowana płaska siatka \((\mathbb Z/N)^3\) z \(h=2\pi/N\), tensorami symetrycznymi rzeczywistymi, trzyelementowym źródłowym Liego i właściwym projektorem \(B=GA\). **NIE** jest to historyczne maskowane \(h=fI,K_A\), York metryki zmiennej ani wynik fizyczny J3/K/NCDG.

## 1. Definicja dokładnego operatora niejednorodnego

Dla każdego całkowitego \(m\ge0\) ustalamy rzeczywisty harmonogram \(\boldsymbol\alpha=(\alpha_1,\ldots,\alpha_m)\) z \(0\le\alpha_j\le1/6\), a \(E_j=I+\alpha_jh^2\Delta_2\). Definiujemy **jednokrotne wstawienie Liego**, uśrednione po wszystkich \(m+1\) pozycjach:

\[
\mathcal U_{\boldsymbol\alpha}(C)
=\frac1{m+1}\sum_{\ell=0}^{m}
E_m\cdots E_{\ell+1}\,\underbrace{B\mathcal L_C B}_{T_C}\,E_{\ell}\cdots E_1.
\tag{33.1}
\]

Każde \(E_j\) komutuje z \(B\), a wszystkie \(E_j\) wzajemnie komutują; nie implikuje to komutacji \(E_j\) z \(T_C\). Gdy wszystkie \(\alpha_j=\alpha\), jest to dokładnie wcześniejsze \(U_m\) ROT027. Dla różnych parametrów nie ma pojedynczej wielomianowej różnicy dzielonej ROT029.

Niech \(S_N(k)=\sum_i\sin^2(\pi k_i/N)\), \(q_j(k)=1-4\alpha_jS_N(k)\), a \(c^r(s)\) będzie dyskretnym zespolonym współczynnikiem Fouriera pola \(C^r\). Dla trybu \(k\to k'=k+s\) pełny **trójczłonowy** źródłowy symbol Liego jest

\[
[M_s(k)V]_{ij}=i\!\left(\sum_r c^r(s)d_r(k)\right)V_{ij}
+i d_i(s)\sum_r c^r(s)V_{rj}+i d_j(s)\sum_r c^r(s)V_{ir},
\qquad d_r(k)=\frac{\sin(hk_r)}h.
\]

Zapisujemy dokładny mnożnik harmonogramu

\[
\boxed{\Omega_{\boldsymbol\alpha}(k',k)=
\frac1{m+1}\sum_{\ell=0}^{m}
\left(\prod_{j=\ell+1}^{m}q_j(k')\right)
\left(\prod_{j=1}^{\ell}q_j(k)\right).}\tag{33.2}
\]

Wówczas **dokładnie**, dla dowolnego rzeczywistego symetrycznego \(H\):

\[
\widehat{\mathcal U_{\boldsymbol\alpha}(C)H}(k')=
B(k')\sum_{s\in\operatorname{supp}\hat C}
\Omega_{\boldsymbol\alpha}(k',k'-s)
M_s(k'-s)B(k'-s)\hat H(k'-s).
\tag{33.3}
\]

W szczególności mnożniki \(q_j\) mogą być **ujemne lub zerowe** przy legalnym \(\alpha_j\): wzór nadal jest rzeczywisty na danych rzeczywistych, bez pierwiastków z ujemnych liczb. Do obliczenia pojedynczego \(\Omega\) można użyć rekurencji \(p_0=w_0=1\), \(w_j=q_j(k')w_{j-1}+q_j(k)p_{j-1}\), \(p_j=q_j(k)p_{j-1}\), \(\Omega=w_m/(m+1)\). Daje \(O(m)\) na przejście bez \(m+1\) źródłowych wywołań Liego, ale **nie** niezależny od \(m\) koszt arytmetyczny dla dowolnego harmonogramu.

## 2. Nowe twierdzenie: budżet łączny daje dokładnie ten sam typ certyfikatu

Przyjmijmy znaną z **ROT032** nierówność widmową w dwóch dołkach, prawdziwą dla każdego \(\alpha\in[0,1/6]\):

\[
|q_\alpha(k)|\le\exp\{-16\alpha r_N(k)^2/N^2\},\quad
|d_N(k)|\le r_N(k),\quad
r_N(k+s)\ge(r_N(k)-|s|)_+.
\]

\(r_N\) to odległość na torusie częstotliwości od bliższego z zera i potrójnego narożnika Nyquista. W każdej pozycji \(\ell\) iloczynu (33.2) obie odległości \(r_N(k)\), \(r_N(k')\) są nie mniejsze niż \((r_N(k)-|s|)_+\). Zatem **każdy** jego składnik spełnia

\[
|\text{składnik}_\ell|\le
\exp\left[-16\frac{A_N}{N^2}(r_N(k)-|s|)_+^2\right],\quad
A_N=\sum_{j=1}^{m}\alpha_j.
\tag{33.4}
\]

Wniosek pozostaje prawdziwy, gdy filtry są przestawiane. Jednostajna kontrola przejścia źródłowego wynika z
\(\|M_s(k)\|\le\|c(s)\|_2(r_N(k)+2|s|)\), \(\|B\|=1\) i
\(\sup_{t\ge0}t\exp(-16\beta_0t^2)=(32e\beta_0)^{-1/2}\).

**R33.1 (sufficient uniform-budget theorem).** Dla dowolnej rodziny parzystych \(N\), rozmaitych stabilnych \(\alpha_{N,j}\), generatorów \(C\) i obcięć jego *próbkowanych* współczynników \(C_S\), jeżeli

\[
\frac{A_N}{N^2}\ge\beta_0>0,
\]

to

\[
\boxed{\|\mathcal U_{\boldsymbol\alpha}(C)-
\mathcal U_{\boldsymbol\alpha}(C_S)\|_{L^2\to L^2}
\le\sum_{s\notin S}\|c(s)\|_2
\left[3|s|+\frac1{\sqrt{32e\beta_0}}\right].}\tag{33.5}
\]

Brak zależności od kolejności, liczby filtrów i nieciągłości przy \(1/6\). Dla analitycznego pola z ROT030, \(C=(0,\sum_{r\ge1}2^{-r}\cos rx,0)\), pasmo \(|s_x|\le L<N/2\) z zachowaniem aliasowanej harmonicznej stałej daje \([3L+6+(32e\beta_0)^{-1/2}]2^{-L}\). To rozszerzenie oszacowania ROT032 z powtórzeń jednego \(E\) na **dowolny legalny harmonogram**.

**R33.2 (necessity on a class, not each C).** Gdy \(\liminf_{N\to\infty}A_N/N^2=0\), istnieje rozbieżny podciąg \(N\), stałe gładkie pole \(C=(0,\varepsilon\cos x,0)\) oraz \(N\)-zależne rzeczywiste dokładne TT tensory \(H_N=\operatorname{diag}(1,0,-1)\cos(K_N y)/\sqrt2\), \(K_N=\max(2,\lfloor N/(8\sqrt{1+A_N})\rfloor)\), dla których

\[
\frac{\|\mathcal U_{\boldsymbol\alpha}(C)H_N\|_2}{\|H_N\|_2}
=\frac{\varepsilon}{\sqrt2}\frac{\sin(hK_N)}{h}
\left(1-\frac1{2(K_N^2+1)}\right)
\Omega_{\boldsymbol\alpha}((1,K_N,0),(0,K_N,0)).\tag{33.6}
\]

Dla dostatecznie dużych \(N\) na tym podciągu obie składowe \(q_j\) są dodatnie i \(\Omega\ge e^{-1}\) (np. \(4\alpha_j\pi^2(K_N^2+1)/N^2<1/4\), \(A_N(K_N^2+1)/N^2\le1/64+o(1)\), a \(\log(1-z)\ge-4z/3\) dla \(z\le1/4\)). W konsekwencji wystarcza konserwatywna stała

\[
\boxed{\|\mathcal U_{\boldsymbol\alpha}(C)\|_{L^2\to L^2}
\ge0.003\,\varepsilon\,\frac{N}{\sqrt{1+A_N}}\to\infty.}\tag{33.7}
\]

Kryterium jest ostre jako **gwarancja jednostajna dla całej klasy generatorów**. Nie twierdzimy, że jest konieczne dla każdego generatora osobno (np. \(C=0\)), ani że jakiś jeden ustalony gładki tensor wejściowy daje rozbieżność.

## 3. Nowe dokładne twierdzenie o kolejności

Zamieńmy **sąsiednie** parametry \(a=\alpha_j\) oraz \(b=\alpha_{j+1}\) w (33.1), zachowując wszystkie pozostałe filtry. Zmienia się tylko pozycja \(\ell=j\). Dla przejścia \(k\to k'\) różnica mnożników **oryginał minus po zamianie** wynosi dokładnie

\[
\boxed{\Delta_j\Omega=
\frac{4(a-b)[S_N(k')-S_N(k)]}{m+1}
\prod_{r<j}q_r(k)\prod_{r>j+1}q_r(k').}\tag{33.8}
\]

Pozostałe \(m\) składników anulują się, ponieważ \(E_aE_b=E_bE_a\). Gdy mnożniki uczestniczących pasm są dodatnie, znak określają dwa różne porządki: wartości \(\alpha_j\) i energie widmowe \(S_N\). Przez kolejne zamiany sąsiadów otrzymujemy dokładną regułę przegrupowania: dla przejścia do wyższej energii widmowej wartości \(\alpha\) uporządkowane **malejąco** od początku dają największą odpowiedź; dla przejścia do niższej energii — **rosnąco**. Jest to twierdzenie o **skalarnym mnożniku przejścia**; nie o normie pełnego tensorowego operatora i nie przy ujemnych \(q_j\), gdzie argument znaku może zawieść.

Dwa pasma boczne ustalonego tensorowego testu \(H_p=T_p\cos(px+y)\), \(p=2,3\), posiadają przeciwne znaki energii względnej: \(p+1\) ma większą, \(p-1\) mniejszą energię od \(p\). Jeden harmonogram nie maksymalizuje zatem obu odpowiedzi jednocześnie.

## 4. Jawny kontrprzykład na dwóch ustalonych gładkich tensorach TT

Wybierzmy parzyste \(m=2n\), stałe \(a\in(0,1/6]\), oraz **dwie permutacje dokładnie tego samego multizbioru filtrów**:

- **EARLY:** \(\alpha_1=\cdots=\alpha_n=a\), a ostatnie \(n\) parametrów wynoszą zero;
- **LATE:** pierwsze \(n\) parametrów są zerowe, a ostatnie \(n\) wynoszą \(a\).

Niech \(q_{j}=1-4a[\sin^2(\pi j/N)+\sin^2(\pi/N)]\). Dla każdej bocznej harmonicznej \(p\to p\pm1\), **dokładnie**

\[
\boxed{\Omega_{\rm EARLY}-\Omega_{\rm LATE}
=\frac{n}{2n+1}\left(q_p^n-q_{p\pm1}^n\right).}\tag{33.9}
\]

Ten wynik można sprawdzić, dzieląc pozycje \(\ell\le n\) i \(\ell>n\): wspólna suma \(\sum_{\ell=0}^n q_{p\pm1}^{n-\ell}q_p^\ell\) znika przy odjęciu, pozostaje wyłącznie \(n(q_p^n-q_{p\pm1}^n)\).

Dla \(v_p=(-1,p,0)/\sqrt{p^2+1}\) weźmy \(T_p=\frac3{10}(e_ze_z^\top-v_pv_p^\top)\). To identyczne, *ustalone i gładkie* rzeczywiste tensory źródłowo poprzeczne i bezśladowe z ROT023/ROT026, bez dotykania Nyquista. Po pełnym źródłowym Liego \(C=(0,\cos x,0)\) i rzeczywistym \(B\), normy bocznych polaryzacji względem \(H_p\) (udowodnione wymiernie już w ROT026) są: \(c_{2,+}=71/200\), \(c_{2,-}=31/40\), \(c_{3,+}=261/680\), \(c_{3,-}=141/200\). Stąd nowa **dokładna skończona formuła normy**:

\[
\boxed{\frac{\|(\mathcal U_{\rm EARLY}-\mathcal U_{\rm LATE})H_p\|_2}{\|H_p\|_2}
=\frac{\sin h}{h}\frac{n}{2n+1}
\sqrt{c_{p,+}^2(q_p^n-q_{p+1}^n)^2+c_{p,-}^2(q_p^n-q_{p-1}^n)^2}.}\tag{33.10}
\]

Jeżeli \(n\sim\beta N^2/2\), to \(q_j^n\to w_j=\exp[-2\pi^2a\beta(j^2+1)]\). Wtedy (33.10) dąży do dodatniej liczby

\[
\boxed{R_p(a,\beta)=\frac12
\sqrt{c_{p,+}^2(w_p-w_{p+1})^2+c_{p,-}^2(w_p-w_{p-1})^2}>0.}\tag{33.11}
\]

Przykład przy \(a=0.1\), \(\beta=.02\): **\(R_2=0.0477573379249\), \(R_3=0.0605105894748\)**. Dla \(N=1024\) bezpośrednia formuła daje odpowiednio 0.0477554143340 i 0.0605073824608. To *niezanikająca* różnica dla tego samego łącznego budżetu i *tych samych* filtrów, lecz innej chronologii. Jest to twierdzenie o nowym sztucznym protokole, nie o oryginalnym eksperymencie historycznym DTC0a.

**Obserwowalność:** oryginalny odczyt \(\langle H_p,\Delta H_p\rangle\) jest równy zero (brak pasma wejściowego po pojedynczym \(L\)), mimo że norma całego pola jest dodatnia. Odczyt w odpowiednio dobranej bocznej polaryzacji wykrywa różnicę; znaki dla \(p+1\) i \(p-1\) są przeciwne.

## 5. Niezależne wykonane kontrole i custody

- **2486** autonomicznych kontroli harmonogramów w kodzie NumPy (`rot033_spectral_schedule_verify.py`): bezpośrednie iloczyny, niezależna rekurencja, zamiany sąsiadów, stabilność \(|\Omega|\le1\), dokładna formuła dwóch bloków i granica dyfuzyjna do \(N=1024\). Maksymalna różnica 3.27e-6 w rekordzie to **błąd skończonego N względem granicy**, nie błąd tożsamości algebraicznej.
- **49** testów z DOSŁOWNYM niezmodyfikowanym źródłem pomocniczym (`rot033_source_native_verify.py`): prawdziwy \(H_p\), \(C=(0,\cos x,0)\), źródłowe `apply_E`, `lie_derivative_tensor`, `apply_P_TT`, sumy po rzeczywistych pozycjach dla \(N=12,16\), w tym \(a=0\) i \(1/6\); maksymalny względny błąd 4.51e-15.
- **9477** osobnych kontroli Python `fractions.Fraction` plus niezależny skaner widmowego oszacowania dwudołkowego (`rot033_exact_and_dualwell_verify.py`): całkowicie ścisłe tożsamości wymierne dla zamian i bloków, ścisłe przegrupowania oraz numeryczne testy oszacowania dla różnych siatek. `Fraction` nie stanowi dokładnej certyfikacji wartości trygonometrycznych.
- **20** całkowicie osobnych testów trójskładowego generatora \(C^x=.15\sin y\), \(C^y=\cos x+.2\sin2x\), \(C^z=.1\cos z\), zawierającego **osiem** niezerowych modów (`rot033_general_vector_source_verify.py`). Dosłowny źródłowy operator Liego / raw TT / stabilne zmienne E, ze strażnikiem G, został porównany z własną implementacją pełnego Fouriera dla losowych rzeczywistych symetrycznych tensorów przy \(N=8,12\). Maksymalny błąd względny 1.49e-15.

**Łącznie 12 032 / 12 032 wykonane, typowane kontrole PASS**. Są to kontrole matematyczne i komputerowe, NIE dane fizyczne. Reproduktor jest jednym ZIP z czterema autonomicznymi plikami `.py`, czterema wykonanymi JSON, niezmienionym źródłem, niniejszym raportem, README, manifestem SHA256 i logami wykonania. Czyste rozpakowanie, CRC, SHA i ponowne odtworzenie należy wykonać przed zgłoszeniem końcowego `REPRO_PASS`.

## 6. Negative knowledge i granice roszczeń

1. Stała \(A_N=\sum\alpha_j\) **wystarcza do certyfikacji normy**, ale **nie determinuje samego \(\mathcal U\)**; porządek filtrów pozostaje merytorycznym parametrem eksperymentu.
2. W przeciwieństwie do ROT029, dla dowolnego harmonogramu nie ma automatycznej stałokosztowej formuły jednej różnicy dzielonej. Rekurencja \(O(m)\) na przejście jest dokładna; dla specjalnych bloków można stosować potęgowanie i formuły zamknięte.
3. Reguła porządkowania sąsiednich filtrów z (33.8) wymaga dodatnich \(q\) do wnioskowania o znaku. Nie rozszerzamy jej bez dowodu na ujemne wysokoczęstotliwościowe mnożniki ani na optymalizację normy całego operatora.
4. Warunek ostrzej konieczny dotyczy jednostajnej klasy gładkich generatorów i wejść zależnych od \(N\), a nie każdego \(C\) lub jednego ustalonego gładkiego \(H\).
5. Historyczna maska \(K_A\), oryginalny production runtime, wyniki J3/K, GR/GW/PBH/BBN, fizyczna pamięć i pomiary NIE są walidowane. Niezależny referee, BW i podpis Moderatora EXEC pozostają otwarte.

`NO_NEW_TASK / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / REFEREE_PENDING / BW_PENDING`
