---
artifact_id: IW_SW_HILBERT_COMPLEX_HOMOTOPY_DOMAIN_REPAIR_REPORT_001_20261014
title: Dziedziny homotopii spektralnej i dokładne obrazy różniczkowania
revision: 1
created_at: 2026-10-14
as_of: 2026-10-14
origin_cell: SW
function: Kontrola analityczna kompleksów Hilberta
document_type: REPORT
task_id: SW-LT4-CHAPTER4-HILBERT-COMPLEX-AUDIT-001
exposure: PUBLIC
status: DRAFT
result_class: ANALYTIC_PROOFS_AND_DOMAIN_COUNTEREXAMPLES
claim_ceiling: Standardowy rachunek spektralny z jawnymi dziedzinami; bez deklaracji nowości, stabilności fizycznej ani równoważności teorii fizycznych.
archive_mode: PUBLIC_ARTIFACT
sync_state: GITHUB_PENDING_BW_INGEST
bw_ingestion_event_id: NOT_YET_INGESTED
primary_location: research/sw/2026-10-14/IW_SW_HILBERT_COMPLEX_HOMOTOPY_DOMAIN_REPAIR_REPORT_001_20261014.md
content_sha256: EXTERNAL_MANIFEST_TO_AVOID_SELF_REFERENCE
provenance: Samodzielne wyprowadzenia standardowych mechanizmów i kontrola wcześniejszego przykładu diagonalnego.
derived_from: []
supersedes: []
stale_if: Kontrprzykład do dowodu przy dokładnie zadeklarowanych dziedzinach i hipotezach.
acceptance_owner: LT4
return_path: LT4
---

# Dziedziny homotopii spektralnej i dokładne obrazy różniczkowania

Oszacowania mnożników mogą zapewniać istnienie ograniczonego przedłużenia złożenia operatorów, nie zapewniając, że samo złożenie jest określone na całej przestrzeni. W kompleksie Hilberta ta różnica nie niszczy homotopii spektralnej, ale musi być uwzględniona w jej definicji i dowodzie. Poniżej podajemy dokładny świadek, poprawne twierdzenie z dowodem oraz dwa związane rozróżnienia: czas zerowy homotopii cieplnej i zmianę dokładnego obrazu po domknięciu różniczkowania.

Wyniki są analityczne. Nie opieramy wniosków o przestrzeniach nieskończenie wymiarowych na obcięciach numerycznych.

## 1. Ustalenie operatorów i dziedzin

Niech \((H^k,d_k)\) będzie skończonym co do liczby stopni kompleksem Hilberta:
\[
d_k:D(d_k)\subset H^k\longrightarrow H^{k+1}
\]
są gęsto określone i domknięte, \(\operatorname{ran}d_k\subset D(d_{k+1})\) oraz \(d_{k+1}d_k=0\). Na końcach kompleksu stosujemy operatory zerowe na całych właściwych przestrzeniach.

Ustalamy nieujemną samosprzężoną realizację laplasjanu Hodge'a
\[
\Delta_k=d_{k-1}d_{k-1}^*+d_k^*d_k,
\]
o dziedzinie
\[
D(\Delta_k)=
\{u\in D(d_k)\cap D(d_{k-1}^*):
d_ku\in D(d_k^*),\ d_{k-1}^*u\in D(d_{k-1})\}. \tag{1}
\]
W szczególności nie utożsamiamy dziedziny operatora (1) z samą dziedziną jego formy kwadratowej. Dziedzina formy to \(D(d_k)\cap D(d_{k-1}^*)\).

Używamy zgodnego rachunku spektralnego tej realizacji: ograniczone mnożniki zachowują odpowiednie dziedziny, a \(d\) i \(d^*\) splatają mnożniki laplasjanów sąsiednich stopni.

Oznaczmy
\[
M_k=\overline{\operatorname{ran}d_{k-1}},\quad
N_k=\overline{\operatorname{ran}d_k^*},\quad
\mathcal H^k=\ker\Delta_k.
\]
Słaby rozkład Hodge'a ma postać
\[
H^k=M_k\oplus\mathcal H^k\oplus N_k. \tag{2}
\]
Wszystkie trzy podprzestrzenie redukują \(\Delta_k\). Zamkniętość obrazów różniczek nie jest tutaj założona.

### Rejestr założeń

| Warunek | Zastosowanie |
|---|---|
| Gęste dziedziny, domknięte różniczki i własność kompleksu | Sprzężenia, rozkład biegunowy, przejście do granic grafowych |
| Jedna ustalona realizacja Hodge'a i zgodny rachunek spektralny | Rozkład (2), splatanie dziedzin i projekcji |
| \(f,g\) ograniczone borelowskie, \(f(0)=g(0)\) | Ograniczone mapy łańcuchowe i zerowanie różnicy na harmonikach |
| \(h(\lambda)=(f(\lambda)-g(\lambda))/\sqrt\lambda\) ograniczone w odpowiednich miarach spektralnych | Ograniczona homotopia |
| Jawne domknięcie złożenia \(d^*q(\Delta)\), gdy \(q\) jest nieograniczone | Poprawna dziedzina homotopii |

Ani bezzerowość \(f,g\), ani zwartość resolwenty, ani luka spektralna nie są potrzebne do twierdzenia o homotopii poniżej.

## 2. Świadek: ograniczone oszacowania nie dają pełnej dziedziny złożenia

Rozważmy dwustopniowy kompleks
\[
H^0=H^1=L^2((0,1),d\lambda),\qquad d=M_{\sqrt\lambda},
\qquad D(d)=H^0.
\]
Następna różniczka jest zerowa. Operator \(d\) jest ograniczony i domknięty, \(d^*=M_{\sqrt\lambda}\), a \(\Delta_0=\Delta_1=M_\lambda\).

Na całej półosi wybierzmy ograniczone, bezzerowe funkcje
\[
g(\lambda)=1,\qquad
f(\lambda)=1+\min(\sqrt\lambda,1),\qquad f(0)=g(0)=1.
\]
Dla \(\lambda>0\) niech
\[
q(\lambda)=\frac{f(\lambda)-g(\lambda)}{\lambda},\qquad q(0)=0.
\]
Na widmie \((0,1)\) mamy
\[
q(\lambda)=\lambda^{-1/2},\qquad
\sqrt\lambda q(\lambda)=1,\qquad
\lambda q(\lambda)=\sqrt\lambda.
\]
Oba ostatnie mnożniki są ograniczone także na całej półosi. Jednak
\[
D(q(\Delta_1))=
\left\{u\in L^2(0,1):
\int_0^1\frac{|u(\lambda)|^2}{\lambda}\,d\lambda<\infty\right\}
\ne H^1. \tag{3}
\]
Funkcja \(u(\lambda)=1\) nie należy do (3). Literalne złożenie
\[
d^*q(\Delta_1)=I|_{D(q(\Delta_1))}
\]
nie jest zatem operatorem określonym na całym \(H^1\). Ma natomiast jednoznaczne ograniczone przedłużenie, będące jego domknięciem:
\[
\overline{d^*q(\Delta_1)}=I:H^1\longrightarrow H^0. \tag{4}
\]

To kontrprzykład wyłącznie do automatycznej pełności dziedziny literalnego złożenia. Nie jest kontrprzykładem do istnienia homotopii: (4) daje poprawną homotopię.

## 3. Twierdzenie o ograniczonej homotopii z jawnym domknięciem

**Twierdzenie.** Przy założeniach §1 zdefiniujmy
\[
j=f-g,\qquad
h(\lambda)=\frac{j(\lambda)}{\sqrt\lambda},\qquad
q(\lambda)=\frac{j(\lambda)}{\lambda}\quad(\lambda>0),
\]
oraz \(h(0)=q(0)=0\). Załóżmy, że wszystkie \(h(\Delta_k)\) są ograniczone. Niech
\[
d_{k-1}=V_{k-1}|d_{k-1}|
\]
będzie rozkładem biegunowym; \(V_{k-1}\) ma przestrzeń początkową \(N_{k-1}\) i końcową \(M_k\). Wtedy
\[
K_k:=V_{k-1}^*h(\Delta_k)P_{M_k}
=\overline{d_{k-1}^*q(\Delta_k)}
\in\mathcal B(H^k,H^{k-1}) \tag{5}
\]
jest dobrze określone i spełnia
\[
K_k(H^k)\subset D(d_{k-1}),\qquad
d_{k-1}K_k=j(\Delta_k)P_{M_k}. \tag{6}
\]
Na \(D(d_k)\) zachodzi
\[
K_{k+1}d_k=j(\Delta_k)P_{N_k}, \tag{7}
\]
a zatem
\[
f(\Delta_k)-g(\Delta_k)
=d_{k-1}K_k+K_{k+1}d_k. \tag{8}
\]
Tożsamość (8) jako tożsamość literalnych złożeń ma dziedzinę \(D(d_k)\). Po zastąpieniu drugiego składnika jego ograniczonym przedłużeniem jest to tożsamość operatorów na całym \(H^k\).

Ponadto
\[
\|K_k\|\leq\|h(\Delta_k)\|,\qquad
\|d_{k-1}K_k\|\leq\|j(\Delta_k)\|.
\]
Mapy \(f(\Delta)\) i \(g(\Delta)\) indukują ten sam endomorfizm kohomologii algebraicznej pierwotnego kompleksu \(d\).

**Dowód.** Na sektorze \(M_k\) laplasjan jest realizacją \(d_{k-1}d_{k-1}^*\). Rozkład biegunowy daje
\[
d_{k-1}^*=V_{k-1}^*\sqrt{\Delta_k}\,P_{M_k}
\]
na właściwej dziedzinie; na pozostałych sektorach sprzężona różniczka znika. Dla \(u\in D(q(\Delta_k))\) wektor \(q(\Delta_k)u\) należy do \(D(d_{k-1}^*)\), ponieważ jego wkład do kwadratu normy sprzężonej różniczki wynosi
\[
\int_{(0,\infty)}
\lambda|q(\lambda)|^2\,d\|E_k(\lambda)P_{M_k}u\|^2
\leq \|h(\Delta_k)\|^2\|u\|^2.
\]
Zatem literalne złożenie na gęstej dziedzinie \(D(q(\Delta_k))\) jest ograniczeniem prawej strony (5). Jego grafowe domknięcie jest całym ograniczonym operatorem (5). Nie zakładamy ograniczoności samego \(q(\Delta_k)\).

Żeby sprawdzić (6) bez nieuprawnionego składania operatorów nieograniczonych, użyjmy
\[
E_k^{(m)}=\mathbf1_{\{0\}\cup[1/m,m]}(\Delta_k).
\]
Na tych nośnikach wszystkie potrzebne iloczyny mnożników są legalne. Dla \(u_m=E_k^{(m)}u\) otrzymujemy
\[
d_{k-1}K_ku_m=j(\Delta_k)P_{M_k}u_m.
\]
Mamy \(u_m\to u\), \(K_ku_m\to K_ku\), a prawa strona zbiega do \(j(\Delta_k)P_{M_k}u\), gdyż \(j\) jest ograniczone. Domkniętość \(d_{k-1}\) dowodzi obu części (6).

Dla \(u\in D(d_k)\) te same obcięcia zbieżne są w normie grafowej \(d_k\), dzięki splataniu projekcji spektralnych. Na obcięciach rozkład biegunowy i splatanie dają
\[
K_{k+1}d_ku_m=j(\Delta_k)P_{N_k}u_m.
\]
Ograniczoność \(K_{k+1}\), grafowa zbieżność \(u_m\) i ograniczoność \(j(\Delta_k)\) dowodzą (7). Wreszcie \(j(\Delta_k)\) znika na \(\mathcal H^k\), więc (2), (6) i (7) dają (8).

Jeśli \(u\in\ker d_k\), to \(u\in D(d_k)\) i
\[
f(\Delta_k)u-g(\Delta_k)u=d_{k-1}K_ku
\in\operatorname{ran}d_{k-1}.
\]
To rzeczywisty brzeg, nie tylko element domknięcia przestrzeni brzegów. Stąd wniosek dla kohomologii algebraicznej, nawet jeśli obrazy różniczek nie są domknięte. \(\square\)

**Krótsza wystarczająca wersja.** Jeśli dodatkowo \(q(\Delta_k)\) jest ograniczone na całym \(H^k\), złożenie w (5) jest od razu określone wszędzie, więc kreskę domknięcia można pominąć. Ograniczoność \(q\) jest mocniejszą hipotezą, a nie wnioskiem z ograniczoności \(h=\sqrt\lambda q\) i \(j=\lambda q\).

## 4. Homotopia cieplna obejmuje czas zerowy

Niech \(T_t=e^{-t\Delta}\) dla \(t\geq0\), zatem \(T_0=I\). Dla \(s,t\geq0\) i \(\tau=|s-t|\) połóżmy
\[
q_{s,t}(\lambda)=
\frac{e^{-s\lambda}-e^{-t\lambda}}{\lambda}\quad(\lambda>0),
\qquad q_{s,t}(0)=t-s.
\]
Oszacowanie
\[
|e^{-s\lambda}-e^{-t\lambda}|
\leq \min(\tau\lambda,1) \tag{9}
\]
daje
\[
|q_{s,t}(\lambda)|\leq\tau,\quad
|\sqrt\lambda q_{s,t}(\lambda)|
\leq\min(\tau\sqrt\lambda,\lambda^{-1/2})\leq\sqrt\tau,\quad
|\lambda q_{s,t}(\lambda)|\leq1. \tag{10}
\]
Dla \(\tau=0\) wszystkie trzy mnożniki znikają. Wartość \(q_{s,t}(0)\) nie wpływa na \(K\), ponieważ \(d^*\) zeruje sektor harmoniczny.

W tej rodzinie samo \(q_{s,t}(\Delta_k)\) jest ograniczone. Dlatego literalne złożenie
\[
K_{s,t,k}=d_{k-1}^*q_{s,t}(\Delta_k)
\]
jest określone na całym \(H^k\), ma normę co najwyżej \(\sqrt\tau\) i spełnia
\[
T_{s,k}-T_{t,k}
=d_{k-1}K_{s,t,k}+K_{s,t,k+1}d_k
\quad\text{na }D(d_k). \tag{11}
\]
Z punktowej addytywności \(q\) wynika
\[
K_{s,u}=K_{s,t}+K_{t,u}\qquad(s,t,u\geq0). \tag{12}
\]

W szczególności dla każdego cyklu \(u\)
\[
u-T_tu=dK_{0,t}u. \tag{13}
\]
To bezpośredni dowód, że \(T_t\) indukuje identyczność na kohomologii pierwotnego kompleksu. Samo posiadanie homotopii między czasami ściśle dodatnimi nie zawiera jeszcze tego kroku. Przejście graniczne \(s\downarrow0\) w ciągu brzegów nie byłoby wystarczającym argumentem, gdy obraz \(d\) nie jest domknięty.

Dla jednego czasu równego zero nie należy uzasadniać (10) wykładniczym zanikiem wszystkich mnożników w nieskończoności. Wtedy \(\lambda q_{0,t}(\lambda)\to1\), natomiast \(\sqrt\lambda q_{0,t}(\lambda)\to0\). Potrzebna jest ograniczoność, którą daje (10).

Na zwartej gładkiej rozmaitości Riemanna bez brzegu (13) stosuje się również do gładkiego kompleksu de Rhama. Dla gładkiego \(u\) wektor \(K_{0,t}u\) jest gładki: splatanie z potęgami laplasjanów zachowuje wspólną dziedzinę wszystkich ich potęg, a regularność eliptyczna utożsamia tę przestrzeń z gładkimi formami. Zatem (13) daje gładką formę pierwotną. Nie stanowi to twierdzenia o lorentzowskiej ewolucji pola.

## 5. Domknięcie różniczkowania może zmienić dokładny obraz

Na \(\ell^2(\mathbb N)\), \(n\geq1\), niech
\[
dx=(nx_n),\qquad
D(d)=\{x:\sum n^2|x_n|^2<\infty\}.
\]
W dwustopniowym kompleksie \(d\) jest domknięte i surjektywne. Dla \(f(\lambda)=e^{-\lambda}\) rozważmy
\[
A_0=d^f=\operatorname{diag}(ne^{-n^2})|_{D(d)}.
\]
Jest to ograniczony operator na gęstej, właściwej dziedzinie, ale nie operator określony na całym \(\ell^2\). Jego jednoznaczne ograniczone przedłużenie wynosi
\[
A=\operatorname{diag}(ne^{-n^2}):\ell^2\longrightarrow\ell^2.
\]
Ponieważ \(D(d)\) jest gęste i \(A\) jest ciągłe,
\[
\overline{A_0}=A. \tag{14}
\]
W szczególności \(x_n=1/n\notin D(d)\), ale jego skończone obcięcia zbiegają grafowo do \((x,Ax)\), co świadczy o niedomkniętości \(A_0\).

Wyliczenie przeciwobrazów daje dwa różne zbiory:
\[
R_0=\operatorname{ran}A_0
=\left\{y:\sum e^{2n^2}|y_n|^2<\infty\right\}, \tag{15}
\]
\[
R_1=\operatorname{ran}\overline{A_0}
=\left\{y:\sum \frac{e^{2n^2}}{n^2}|y_n|^2<\infty\right\}. \tag{16}
\]
W (15) trzeba wymusić \(A^{-1}y\in D(d)\); w (16) jedynie \(A^{-1}y\in\ell^2\).

Mamy ścisłe inkluzje
\[
R_0\subsetneq R_1\subsetneq\ell^2. \tag{17}
\]
Pierwszą poświadcza \(y_n=e^{-n^2}\): przeciwobraz \(1/n\) należy do \(\ell^2\), lecz nie do \(D(d)\). Drugą poświadcza \(z_n=ne^{-n^2}\in\ell^2\): jego jedyny formalny przeciwobraz jest ciągiem jedynek, który nie należy do \(\ell^2\).

Oba obrazy zawierają ciągi o skończonym nośniku i mają domknięcie \(\ell^2\). Obie różniczki mają zerowe jądro. Stąd w stopniu pierwszym zredukowany iloraz jest zerowy dla obu realizacji, natomiast ilorazy algebraiczne mają różne, jawnie wskazane mianowniki:
\[
\ell^2/R_0\longrightarrow\ell^2/R_1.
\]
Naturalna surjekcja między nimi ma niezerowe jądro \(R_1/R_0\). Nie twierdzimy, że te ilorazy nie mogą być abstrakcyjnie izomorficzne jako same przestrzenie wektorowe. Dowiedziono utraty informacji przy wskazanej naturalnej mapie ilorazowej.

## 6. Domkniętość operatora i domkniętość jego obrazu

W terminologii Arnolda–Falka–Winthera [AFW2010, §3.1.3, s. 301] różniczki kompleksu Hilberta są już domkniętymi operatorami. Określenie „closed Hilbert complex” nakłada dodatkowo domkniętość ich obrazów. Dlatego te dwa warunki trzeba nazywać oddzielnie.

Prosty świadek rozróżnienia jest już zawarty w §2. Operator \(d=M_{\sqrt\lambda}\) jest ograniczony i domknięty, lecz
\[
\operatorname{ran}d
=\{y\in L^2(0,1):\int_0^1|y(\lambda)|^2/\lambda\,d\lambda<\infty\}
\]
jest właściwy i gęsty. Dla \(f\equiv1\) normy grafowe \(d^f\) i \(d\) są identyczne, a obraz nadal nie jest domknięty. Certyfikat równoważności norm grafowych nie promuje więc sam przez się kompleksu do klasy o domkniętych obrazach.

## 7. Zakres wyniku i umiejscowienie w literaturze

| Ustalenie | Status |
|---|---|
| Oszacowania \(\sqrt\lambda q,\lambda q\) nie zapewniają pełnej dziedziny literalnego \(d^*q(\Delta)\) | Udowodnione przez (3) |
| Ograniczona homotopia po jawnym domknięciu | Udowodniona w (5)–(8) |
| Homotopia cieplna z czasem zero i identyczność na pierwotnej kohomologii | Udowodniona w (9)–(13) |
| Zmiana dokładnego obrazu po domknięciu diagonalnego różniczkowania | Udowodniona w (14)–(17) |
| Domkniętość obrazów wynikająca wyłącznie z domkniętości różniczek | Obalona w §6 |
| Równość kohomologii nowych różniczek \(d^f,d^g\) wyłącznie z homotopii map \(f(\Delta),g(\Delta)\) | Nie wynika z powyższego |
| Nowość naukowa, fizyczna stabilność, przyczynowość | Nie są przedmiotem ustaleń |

Tłem jest standardowa teoria kompleksów Hilberta, norm grafowych, rachunku spektralnego i homotopii. AFW2010 §§3.1.2–3.2 jest sprawdzonym źródłem definicji operatorowych i realizacji Hodge'a. Nie przypisujemy temu artykułowi dokładnego sformułowania lematu (5): przedstawiony wyżej dowód jest jawną rekonstrukcją na potrzeby kontroli dziedzin. Nie przeprowadzono systematycznego badania pierwszeństwa.

### Literatura pierwotna sprawdzona dla tej notatki

**[AFW2010]** D. N. Arnold, R. S. Falk, R. Winther, *Finite element exterior calculus: from Hodge theory to numerical stability*, Bulletin of the American Mathematical Society 47(2), 281–354 (2010). DOI: [10.1090/S0273-0979-10-01278-4](https://doi.org/10.1090/S0273-0979-10-01278-4). [Autorska kopia wersji opublikowanej](https://sites.math.rutgers.edu/~falk/papers/bulletin.pdf). Dokładne miejsca: §3.1.2, s. 300; §3.1.3, s. 301–302; początek §3.2, s. 302. Wersja przed publikacją: arXiv:0906.4325v2.
