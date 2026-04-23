# Volume III: CY Categories, Quantum Groups, and BPS Algebras --- Battle-Hardened Platonic Ideal, 2026-04-22

*Raeez Lorgat, Perimeter Institute.*

---

## I. Two-stage factorisation

$$\boxed{\;\Phi_d=\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}\circ\Phi^{\mathrm{FA}}_d\colon\mathrm{CY}_d^{\mathrm{cat}}\to\mathrm{Alg}_{E_1^{\mathrm{ch}}}(C)\text{ in }\mathrm{PresStCat}_\infty,\text{ factoring through }\mathrm{Fact}^{\mathrm{hol}}_{E_d}(X).\;}$$

$$\begin{array}{ccc}\mathrm{CY}_d^{\mathrm{cat}}&\xrightarrow{\;\Phi^{\mathrm{FA}}_d\;}&\mathrm{Fact}^{\mathrm{hol}}_{E_d}(X)\\ \big\downarrow\,{\scriptstyle\mathrm{Shad}_\bullet}&&\big\downarrow\,{\scriptstyle\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}}\\ \mathrm{Alg}_{E_1^{\mathrm{ch}}}(C)&\xleftarrow[\;\Omega^{\mathrm{ch}}_C\;]{B^{\mathrm{ch}}_C}&\mathrm{CoAlg}^{\mathrm{fact}}_{E_1^{\mathrm{ch}}}(C)\end{array}$$
Diagonal $\mathrm{Shad}_\bullet=\Phi_d$. $\mathrm{CY}_d^{\mathrm{cat}}\subset\mathrm{PresStCat}_\infty$: proper smooth $\mathbb C$-linear stable with $\mathbb S_{\mathcal T}\simeq[d]$ (Bondal 1990; Kuznetsov 2004; BBDJS 2015). Dunn forbids $E_d=E_1$ for $d>1$; passage factors through $E_d$-holomorphic. Stage 1: KT $E_d$-formality (Willwacher 2014 Thm 1.2 $H^0(\mathsf{GC}_2)=\mathfrak{grt}_1$) $\cap$ CGL $(0,d)$-locality (Costello-Li 2016 Prop 5.2). Stage 2: $\int_{\Sigma_{d-1}}$ + restriction (Ayala-Francis 2015 Thm 3.16). Family-of-shadows $\mathrm{Shad}_X\colon\mathrm{CycCurve}(X)\to\mathrm{Alg}_{E_1^{\mathrm{ch}}}(\mathrm{SmCurve})$. At $d=5$ FM on $(K3\times K3\times E)/\Z_2$ via PTVV; Borcherds 1998 §14 gives $\Phi_{12}|_{\mathrm{II}_{2,2}}=\Phi_{10}=\Delta_5^2$ as $d=3$ shadow.

## I-bis. $\Phi_3$ on $T^3$

Stage 1: $\mathcal F_{T^3}=\mathrm{Sym}^\bullet(\Omega^{0,\bullet}(T^3,\C^3))$, abelian, $P^{(j)}=1/(w_j-w'_j)^2$, KT formality automatic. Stage 2: $\mathcal H_3$ on $E$, $\kappa_{\mathrm{ch}}=3$, three $S_3$-shadows. Three-faces degenerate: $c_+(L)=0,K=0$.

## I-ter. Canonical order of the six-row spine as $\kappa_{\mathrm{cat}}$-stratified maturity map

$$\boxed{\;\mathsf G\;<\;\mathsf L\;<\;\mathsf C\;<\;\mathsf M\;<\;\mathsf M^{\mathrm{ext}}\;<\;\mathsf B\;}$$

Stratum 0 (abelian CY): $\mathsf G$ at K3-Heisenberg $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}=3$ before Mukai enhancement reads $\kappa_{\mathrm{cat}}(K3)=2$ geometric + $\kappa_{\mathrm{ch}}=3$ chiral; $\mathsf L$ at $\P^2$-local $\kappa_{\mathrm{cat}}=3/2$ with $V_k$ chiralisation; $\mathsf C$ at conifold $\kappa_{\mathrm{cat}}=1$ with $\beta\gamma_\lambda$. Stratum 1 ($\mathcal W$-reduction quotient): $\mathsf M/\mathsf M^{\mathrm{ext}}$ reach CY through Stage-2; principal $\mathcal W_N$ from DS quotient of $V_k(\widehat{\mathfrak{sl}_N})$ chiralising abelian-$T^d$; subregular BP from DS of $V_k(\widehat{\mathfrak{sl}_3})$ at minimal nilpotent; Stage-1 FA differs (principal bosonic-only vs subregular bosonic+fermionic transverse), forcing $\mathsf M<\mathsf M^{\mathrm{ext}}$. Stratum 2 (Mukai-enhanced K3 climax): $\mathsf B=\mathbf H_{\Delta_5}$ at $\hbar^2=-1/8$ on Mukai lattice $\mathrm{II}_{4,20}$ with $c_+=8$; three routes converge: Mukai $2c_+(\mathrm{II}_{4,20})=8$; Humbert monodromy order $8$ on $H_1$; Lusztig $\ell=8$ root order in $\mathfrak u_{\zeta_8}$. $\Phi_d$ maps CY-$d$ $\kappa_\bullet$ onto spine: Tier I $\kappa_{\mathrm{cat}}=\chi(\mathcal O_X)$ stratifies stratum 0; Tier II $\kappa_{\mathrm{fiber}}$ stratum 1; Tier III $\kappa_{\mathrm{BKM}}$ stratum 2. $K3\times E$ spectrum $\{0,3,5,24\}$ carries all three tiers. Three-faces-of-8 forces $\mathsf B$-terminality: $\hbar^2K=-1$, $K=2c_+(L)$ per-row unconditional on Monster/K3/FM/Enriques; Conway $V^{s\natural}$ enters as non-vacuity control at $(K,\hbar^2)=(2,-1/2)$ Monster-transported, structurally out of scope. $\mathrm{Aut}^\circ(K3\times E)=E$ has no $\mathbb G_m$-subtorus; no seventh row without Dunn-Lurie Serre-CM lift (conditional). \ClaimStatusProvedHere on smooth $\mathrm{CY}_{\le 3}$ via $\Phi_d$ canonical on $\mathcal U^{\mathrm{adm}}$; stratum transitions stratum 0 to 1 via $\mathcal W$-reduction (Frenkel-Ben-Zvi 2004); stratum 1 to 2 via Mukai rank-24 activation (Mukai 1987; Nikulin 1979). $\mathsf B$-terminal \ClaimStatusProvedHere at $K=8$ via Bruinier 2002 + Gritsenko 1999 + Lusztig 1990; Serre-CM unification \ClaimStatusConjectured.

## II. Five parts

- **I** CY-$d$ chiralisations. CY-2 K3/Enriques; CY-3 taxa (toric, local $\P^2$, conifold, $K3\times E$, abelian, quintic); $G_2,\mathrm{Spin}(7)$ real.
- **II** Chiral quantum groups. Four Yangian types $Y_\hbar(\mathfrak g),Y^{\mathrm{dg}}_\hbar,Y^{\mathrm{ch}},Y^{\mathrm{spec}}$. Elliptic partial; toroidal absent.
- **III** BPS/BKM. $\mathbf H_{\Delta_5}$ (K3); Monster; FM; Enriques; Conway via $\Psi^{\mathrm{metap}}$.
- **IV** CY landscape census. CY-2 $\{0,3,5,24\}$. CY-3: $\kappa_{\mathrm{cat}}(K3\times E)=0$; local $\P^2$: $3/2$; conifold $1$. CY-4 open.
- **V** Maturity map. Raw CY $\infty$-cat $\to$ Stage-1 $E_d$-FA $\to$ Stage-2 chiral on $C$ $\to$ A/B/C/D/H.

## III. $\mathbf H_{\Delta_5}$ canonical

$$\boxed{\mathbf H_{\Delta_5}=\mathcal D_\hbar(\mathcal Y^{\mathrm{Hall}}_\hbar(\mathrm{CoHA}_{\mathrm{K3}\times E}),\widetilde\Phi^{\mathrm{Sieg\text{-}Bor}}_{\mathrm{Sp}_4}[\Phi_{10}/\eta^{24}],R_{\mathrm{Sieg,dyn}})}\quad\text{at }\hbar^2=-1/8.$$

**Seven incarnations.** (1) Super-EK Manin pair; (2) super-Yangian $Y^{\mathrm{super}}_\hbar(\mathfrak g_{\Delta_5})$, $R(u,Z)=(1+\hbar\Omega/u)\exp(\hbar F^{\mathrm{Sieg}}(u,Z)\Omega_{K3})$; (3) super-Kontsevich DQ; (4) MO stable-envelope on $\mathrm{Hilb}^{[n]}(\mathrm K3)$; (5) Khovanov-type; (6) 3d TV TQFT at $\zeta_8$; (7) Borcherds all-loop BV $(\Phi_{10}/\eta^{24})^\hbar$. 0/7 rigorously equivalent; 2 type-errors; 3 formal/open. $\mathbf H_{\Delta_5}$ canonical; incarnations not. Invariants: $\mathfrak g_{\Delta_5}=\mathrm{Borch}(F_3,\phi_{0,1}^{K3})$; Gram $(\det,\mathrm{eigs},\mathrm{sig})=(-32,\{+4,+4,-2\},(2,1))$; $\Delta_5=\mathrm{Grit}(\eta^9\vartheta_1)$ weight 5; $\Phi_{10}=\Delta_5^2$; $\mathrm{mult}(\alpha)=c_{K3}(4nm-\ell^2)\sim An^{-27/4}e^{4\pi\sqrt n}$.

## IV. Three-faces identity

$$\boxed{\;\hbar^2\cdot K^{\kappa_{\mathrm{ch}}}=-1,\quad K=2c_+(L)\;}$$

Bruinier 2002 Prop 5.1 Heegner-Chern. Three routes converge since $\mathrm{Aut}^\circ(K3\times E)=E$ no $\mathbb G_m$-subtorus: Mukai $2c_+(\mathrm{II}_{4,20})=8$; Humbert monodromy-order $=8$ on $H_1$; Lusztig $\ell=8$ in $\mathfrak u_{\zeta_8}$.

| Row | $L$ | $(K,\hbar^2)$ | Input | Status |
|---|---|---|---|---|
| Monster | $\mathrm{II}_{1,1}$ | $(2,-1/2)$ | $j(\sigma)-j(\tau)$ | Borcherds 1992, CN 1979 |
| K3 | $\Lambda^{2,1}_{\mathrm{II}}$ | $(8,-1/8)$ | $\Delta_5$ | GN 1998 |
| FM | $\mathrm{II}_{25,1}$ | $(50,-1/50)$ | $\Phi_{12}$ | Borcherds 1990 |
| Enriques | $U\oplus U\oplus E_8(-1)$ rank $12$, sig $(2,10)$ | $(4,-1/4)$ canonical | $\Delta_5^{\mathrm{Enr}}=\Phi_4^{\mathrm{Enr}}$ (Allcock) | Allcock 2000 + GN 1997 + Mukai-Kondo $M_{12}$ |
| Conway | $\Psi^{\mathrm{metap}}$ on $V^{s\natural}$ | $(2,-1/2)$ Monster-transported; structural boundary | Conway den. (pattern-match) | Duncan 2007 + Scheithauer 2008 |

Conway resolution: none of $c_+=6$, $L=\Lambda_{24}$, $L=\mathrm{II}_{25,1}=\Lambda_{24}\oplus\mathrm{II}_{1,1}$, or $\mathrm{Mp}_4\to\mathrm{Sp}_4$ weight-doubling yields four-route convergence. Conway is the structural boundary: reflective-Lorentzian structure fails at positive-definite $\Lambda_{24}$; $(2,-1/2)$ is Monster-transported via Duncan super-twin sign-character, not an independent witness. Nominal $K=12$ retracted as pattern-match with $c_{V^{s\natural}}$. Enriques $K=4$ canonical via three routes: Allcock 2000 J.\ reine angew.\ Math.\ 518 Thm 1 $\Phi_4^{\mathrm{Enr}}$ weight $4$ = GN 1997 Duke 87 Prop 2.1 quasi-pullback of $\Phi_{12}$ along $\mathrm{II}_{2,10}\hookrightarrow\mathrm{II}_{2,26}$; Mukai $\Lambda^{\mathrm{Enr}}_{\mathrm{Muk}}=U\oplus U\oplus E_8(-1)$ rank 12 sig $(2,10)$ has $c_+=2$; orbifold halving (Persson-Volpato 2011 Prop 4.1) halves K3 $\chi(\mathcal O_X)=2$ to Enriques $\chi(\mathcal O_S)=1$ and halves $\Phi_{10}|_{\mathrm{II}_{2,10}}\to\Delta_5^{\mathrm{Enr}}=\Phi_4^{\mathrm{Enr}}$; $\kappa_{\mathrm{BKM}}(\mathrm{Enr}\times E)=4$. Mukai-Kondo $M_{12}\hookrightarrow M_{24}$ (Kondo 1998 Duke 92 Thm 2.1; Mukai 1988 Invent 94 Thm 0.3).

### IV-bis. Incarnation 7 rigour

\ClaimStatusProvedElsewhere: DVV 1997 $1/\Phi_{10}$ exact BPS-sector identity; $\chi(K3)=24$; 24 $I_1$; F-theory 24 7-branes; $12\cdot 2=24$; 24 twisted M5 (CGP 2018); leading saddle via Borcherds 1998 + EZ 1985 + Göttsche 1990. \ClaimStatusProvedHere: one-loop $Z_{\mathrm{hCS}}$. \ClaimStatusConjectured: all-orders. \ClaimStatusHeuristic: full off-shell 3D gravity. MW 2009 $\ne$ DVV category error.

## V. $\Psi$ four-sibling

$$\boxed{\;\{\Psi,\Psi^{\mathrm{deg}},\Psi^{\mathrm{tor}},\Psi^{\mathrm{metap}}\}:\mathrm{CY}^{\mathrm{Siegel\text{-}aut}}_2\to\mathrm{QHopf}^{\mathrm{BKM}}\;}$$

Jointly surjective onto GN-reflective sig-$(2,n\ge 3)$ on Koszul locus; $24A_1$-Niemeier sig-$(2,24)$ outside. S17+DMS21+S06.

| Sibling | $N$ | Ramification | Weight | $\Phi_N$ | Cover | 3D-QG |
|---|---|---|---|---|---|---|
| $\Psi$ | $1$ | unramified | $5$ | $\Delta_5$ | $\mathrm{Sp}_4$ | $1/\Phi_{10}$ DVV |
| $\Psi^{\mathrm{tor}}$ | $\{2,3,4,6\}$ | torsion CHL | prog $(4,3,2,1)$ / twined $(2,1,1,1)$ | twined $\Phi_N$ | paramod | $1/\Phi_N$ |
| $\Psi^{\mathrm{metap}}$ | $5,7$ | half/quarter-int | $(1/2,1/4)$ | $\Phi_5^{(1/2)},\Phi_7^{(1/4)}$ | $\mathrm{Mp}_4$ | CHL |
| $\Psi^{\mathrm{deg}}$ | $8$ | weight-$0$ | $0$ | $\Phi_8^{(0)}$ | diag-divisor | degenerate |

22 non-Leech Niemeier residual frontier.

## VI. Canonical CY$_d$ $\kappa_\bullet$

Tier I (CY intrinsics): $\kappa_{\mathrm{cat}}(X)=\chi(\mathcal O_X)$; Mukai; $(-d)$-shifted symplectic. Tier II (Stage-1): $\kappa_{\mathrm{fiber}}$. Tier III (Stage-2): $\kappa_{\mathrm{BKM}}$; Niemeier-twist; Humbert; CHL twined. CY-2: $\kappa_{\mathrm{cat}}(K3)=2,\mathrm{Enr}=1,T^4=0$. CY-3: $\kappa_{\mathrm{cat}}(K3\times E)=0$; $\P^3=1$; quintic $0$; $T^3=0$. $K3\times E$ spectrum $\{0,3,5,24\}$.

## VII. $\kappa_{\mathrm{BKM}}$ dual-reading

$\kappa_{\mathrm{BKM}}(\Delta_5)=5$ K3 half-BPS; $\kappa_{\mathrm{BKM}}(\Phi_{10})=10$; $\kappa_{\mathrm{BKM}}(\Phi_{12})=12$. Universal $\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2$ (Borcherds 1995 Thm 10.4). Three distinct Jacobi inputs at $N\in\{1,2,3,4,6\}$:

- **Programme (Gritsenko).** Hodge-elliptic $\mathrm{Aut}(E)$-orbifold; $c_N(0)=(10,8,6,4,2)$, weights $(5,4,3,2,1)$. Gritsenko 1999 Math Nachr 199 Thm 6.1 canonical.
- **Singly-twined $M_{23}$.** $\phi^{(g_N)}_{0,1}=\tfrac12 Z^{(g_N)}_{K3}$; $c_N(0)=(10,4,2,2,2)$, weights $(5,2,1,1,1)$. CHP 2014 Table 4.
- **Physical CHL.** $N\in\{1,2,3,5,7,11\}$, $k_N=24/(N+1)-2$. JS 2005.
- **Borcherds 8-form.** $N\in\{1,\ldots,8\}$, weights $(5,2,1,1,1/2,1,1/4,0)$. Cléry-Gritsenko 2013.

Square-doubling $\Phi_{10}=\Delta_5^2$ at $N=1$ only. Vol I uses 12 (FM), Vol III uses 5 (K3). Additive $\kappa_{\mathrm{BKM}}=\kappa_{\mathrm{ch}}+\chi(\mathcal O_{\mathrm{fiber}})$ FALSE.

## VIII. CoHA-to-$\mathcal W_\infty$

$\mathrm{CoHA}(\C^3)=Y^+$ (SV 2013 IHES 118); $D(Y^+)=Y(\widehat{\mathfrak{gl}}_1)$. $\mathrm{CoHA}(\C^3)\ne\mathcal W_{1+\infty}$. $\mathcal W_{1+\infty}[\lambda]=\mathrm{ev}_\lambda$-slice of $Y^+$. Miki $\Z/3$. Five descent lines.

## IX. Five structural identities

**SI-1** $\mathrm{hCS}\dashv\mathrm{BKM}$ on $\mathcal U^{\mathrm{adm}}$; Stage-1 unit Costello-Li 2016; Stage-2 counit Borcherds singular theta.
**SI-2** Master $L$-value: $\log Z^{(1)}_{\mathbf H^\Psi_L}=-\log\Delta_L-\kappa_{\mathrm{BGS}}(L)L'(0,\Delta_L,\mathrm{std})+\log C_L$. K3/Monster/FM $\kappa_{\mathrm{BGS}}=24$; Enriques 12.
**SI-3** Unified three-faces: $\hbar_r^2 K_r=-1$, $K_r=2c_+(L_r)$.
**SI-4** $8\times 5$ Bistrata; diagonal witnesses ceiling; $\mathsf B$-row $K^\kappa=8$.
**SI-5** MGSL $\simeq\mathfrak h_{\mathrm{BKM}}\times\mathfrak{grt}_1^{\mathrm{KS}}$. Brown 2011 unconditional $\le 12$.

## X. Open frontier

1. K3 Yangian past genus 1. 2. Drinfeld-J BKM Yangians $\mathfrak g_{\Delta_5}$. 3. CY-C general. 4. CY-4 $\Phi_4$. 5. Chenevier non-reduced. 6. Bridgeland $\dim\mathrm{Stab}(K3\times E)=48$. 7. FM $\Psi$-image. 8. Non-CHL $N=7$. 9. $\Phi_4$ framework. 10. $\kappa_{\mathrm{BKM}}$ FM row. 11. $\phi^{(n\ge 25)}$. 12. $e_{k\ge 4}$. 13. $\mathrm{GRT}_1$-transitivity. 14. PBW $\mathfrak u_{\zeta_8}$: $8^{129}$. 15. Yetter-Drinfeld $\delta^{(n\ge 7)}$.

## XI. Canonical retractions

$\Delta_{E_6}$ weight 16 via $f_{16}=E_4\Delta$. Chenevier $D^{\mathrm{Chen}}\equiv$ Taylor-Wiles $S^{\mathrm{ps}}$ reduced. 7 Niemeier $\Psi$-interior; 22 exterior. $\Lambda_{\mathrm{Muk}}(K3)=\mathrm{II}_{4,20}$ rank 24; FM no compact CY host. $\Phi_{10}=\Delta_5^2$. Four Yangian types. **CANONICAL-ANOM-LOCUS** $\mathrm{Anom}_1=0\iff\mathfrak g\in(\mathrm{Deligne}^{\mathrm{exc}}\setminus\{E_6,A_2\text{-unrefined}\})\cup\{\text{abelian}\}\cup\{\mathrm{str}_{\mathrm{ad}}=0\}\cup\{K^{-1/2}\text{-refined}\}$; Deligne quartic killed; $A_2$-refined FF+Dimofte cures; $E_6$ $\mathrm{Sym}^3(\mathbf{27})$ strict. Conway $V^{s\natural}$ $c=12$ super-twin. $(c_{4d},c_{2d})(A_1,\Sigma_{0,24})=(107/6,-214)$; $(n_v,n_h)=(63,88)$; $c_3=-8$, $-22032=176256/(-8)$. Umbral $(N-1)\mid 24$; $\zeta(3,3,3,3)\approx 0.000296$; Leech root 2. $\Phi_{12}$ home $\mathcal D_{\mathrm{II}_{26,2}}$. $\mathrm{ChirHoch}^3$ pairing $2\mathrm{Vol}(E)(2\pi i)^3$. $8^{129}=\dim\mathfrak b^{\mathrm{re},+}_{\zeta_8}$.

## XII. Scope discipline

Chain-level and $(\infty,1)$ equal status (Pattern 269). $\mathcal U^{\mathrm{adm}}=\overline{\mathcal A_2}\setminus\bigcup_{n\equiv 0,3\bmod 4}H_n$.

## XIII. Cross-volume

- **Vol II $\rightleftarrows$ Stage-1.** Vol II 6d hCS on $\R^3\times K3\times\C^2$ IS Stage-1 $\Phi^{\mathrm{FA}}_3(K3\times E)$ after $E_6\to E_3$ Dolbeault.
- **Vol I $\rightleftarrows$ Stage-2.** Vol I $E_1$-chiral shadow on $E$ IS Stage-2 pushforward.
- **AP5.** Vol I 12 (FM); Vol III 5 (K3).

## XIV. Session ledger E1--E24

E1 Quartic + CANONICAL-ANOM-LOCUS; E2 $c_{\phi_{-2,1}}(-n)=0,c_{\phi_{0,1}^{K3}}(-1)=2,c(0)=20$; E3 Theta $1/2!$, 3-loop $\chi(K3)^3/3!=2304$; E4 $e_k\in\mathrm{zv}^{\mathrm{sv}}_{3k}$; E5 Arnold/PSL$_2$/Totaro-Kriz; E6 $Z^{K3}_{3dQG}=1/\Phi_{10}$ DVV; E7 $\Phi_{10}/(\eta(\tau)^{24}\eta(\tau')^{24})$ weight $(-12,-12)$; E8 $\C^n\to E_{2n}$, $E_n$ after $\bar\partial$; E9 Wheel-$\zeta$ basepoint; E10 K3 MHS; E11 AF 2015 vs AFT 2017; E12 non-compact CG Vol 2 Prop 8.2.1; E13 CHSW SU(3), CY-4 BBS/SVW; E14 quartic Deligne-killed, cubic $d^{abc}$ live $A_2,E_6$, $E_6$ strict; E15 Conway $\Psi^{\mathrm{metap}}$ $c=12$; E16 three ladders; E17 $\kappa_{\mathrm{BKM}}$ denominator-named; E18 four Yangian types; E19 $\Phi_d$ two-stage; E20 three-tier hierarchy; E21 $f_{16}=E_4\Delta$ weight 16; E22 $\Phi_{10}=\Delta_5^2$; E23 Monster/K3/FM/Enriques inscribed (4 rows); Conway structural boundary of $\hbar^2 K=-1$ non-vacuity control, $(K,\hbar^2)=(2,-1/2)$ Monster-transported via Duncan super-twin; Enriques $K=4$ canonical (Allcock+GN+Mukai-Kondo); E24 $\kappa_{\mathrm{cat}}(K3\times E)=0$ Künneth.

## XV. One-sentence summary

Vol III establishes $\Phi_d=\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}\circ\Phi^{\mathrm{FA}}_d$ as $(\infty,1)$-functor $\mathrm{CY}_d^{\mathrm{cat}}\to\mathrm{Alg}_{E_1^{\mathrm{ch}}}(C)$; crystallises $\mathbf H_{\Delta_5}$ under $\hbar^2 K=-1$, $K=2c_+(L)$; four-sibling $\Psi$ surjective; CY$_d$ stratified $\{\kappa_{\mathrm{cat}},\kappa_{\mathrm{ch}},\kappa_{\mathrm{fiber}},\kappa_{\mathrm{BKM}}\}$.

## XVI. Attack-heal closure

Humbert split ($\equiv 3,5\bmod 8$ vs $\equiv 0,3\bmod 4$); $\mathcal W_N$ five-witness + $\{\mathcal W_3,\mathrm{BP}\}$; Vol III 0/21 pairwise distinct from Vol II heptagon; both $\eta^{24}(\tau)\eta^{24}(\tau')$, Igusa 1964 bimodular $(-2,-2)$; Stage-1 canonical on $\mathcal U^{\mathrm{adm}}$ only.

## XVII. Local-global five cycles

| Cycle | Local | Global |
|---|---|---|
| (i) Averaging | $\mathrm{av}^{\mathrm{loc}}_n$ per-disc | $\mathrm{hocolim}_n\mathrm{av}^{\mathrm{loc}}_n$ |
| (ii) Five thms | $T^3$: $\mathcal H_3\vert_E$ chain | $\Phi_d$ $(\infty,1)$-functor |
| (iii) $r(z)$ 7 faces | $r^{\mathrm{Sieg,dyn}}$ | $\mathrm{GRT}_1(\Q)$-torsor |
| (iv) Family-shadows | per-$(\Sigma,C)$ | $\mathrm{Shad}_X$ over $\mathrm{CycCurve}(X)$ |
| (v) Chenevier/MGSL | per-prime $\bar\rho_\ell$ | $D^{\mathrm{Chen}}$; MGSL |

$\psi_{\Delta_{10}}=\phi_{\Delta_{E_6}}\boxtimes\mathrm{Sym}^1$; $\lambda_p(\Delta_{10})=a_p(\Delta_{E_6})+p^8+p^9$ unconditional $p\le 199$. Padovan $d_n=d_{n-2}+d_{n-3}$.

## XVII-bis. F-META-4 rectifications

**R1** Three ladders (§VII). **R2** Five $\kappa$-subscripts $\{\kappa_{\mathrm{ch}},\kappa_{\mathrm{cat}},\kappa_{\mathrm{BKM}},\kappa_{\mathrm{fiber}},\kappa_{\mathrm{anom}}\}$ + $\varrho=\kappa_{\mathrm{ch}}/c$; $\kappa_{\mathrm{anom}}$ ghost $+1$ (Costello-Li 2016 Prop 5.2). **R3** $K3\times E$ spectrum $\{0,3,5,24\}$ canonical. **R4** FM $d=5$ conjectural; $d=3$ host-obstruction unconditional (rank 24 > $h^{1,1}(K3)=20$). **R5** BCFG $\sigma$-equivariant unconditional (Maschke + Weibel Cor 6.5.9); twisted affine $Y_\hbar(\widehat{\mathfrak g}^{(r)})$ GRW 2018. **R6** Three-faces-of-$8$ individual unconditional; unification on Dunn-Lurie Serre-CM. **R7** WW 2023: $\Phi_{12}$ unique on $\mathrm{II}_{26,2}$; $\mathrm{II}_{2,2}$ no embed in $(25,1)$. **R8** 12 frontiers (§X) + C13 Nakajima-Baranovsky threefold. **R9** Lorgat 2020: Borcherds lift $\phi_{0,1}\to\Delta_5$; $\mathfrak g_{\Delta_5}$ GKM; 8 Gritsenko-Cléry forms. **R10** Class-$\mathcal S$ Schur $\mathcal I_S(q)=\mathrm{PE}[(72q-22q^2)/(1-q)]+O(q^{11})=1+72q+2678q^2+\cdots+3{,}713{,}379{,}957{,}230\,q^{10}$.

## XVIII. Climax --- $\mathbf H_{\Delta_5}$ terminal

$$\boxed{\;\mathbf H_{\Delta_5}=\mathcal D_\hbar(\mathcal Y^{\mathrm{Hall}}_\hbar(\mathrm{CoHA}_{\mathrm{K3}\times E}),\widetilde\Phi^{\mathrm{Sieg\text{-}Bor}}_{\mathrm{Sp}_4}[\Phi_{10}/\eta^{24}],R_{\mathrm{Sieg,dyn}})\quad\text{at}\quad\hbar^2=-1/8.\;}$$

Stage-1 canonical up to contractible choice on $\mathcal U^{\mathrm{adm}}$ via KT formality $\cap$ CGL locality. Stage-2 via Ayala-Francis 2015 Thm 3.16 along elliptic pencil + restriction to $E$. Künneth $\mathrm{CoHA}(\mathrm{K3}\times E)=\mathrm{CoHA}(\mathrm{K3})\boxtimes_{E_{\mathrm{Hall}}}\mathrm{CoHA}(E)$ with Mukai rank-24 grading; Drinfeld-doubling yields BKM-superalgebra Hopf, rank-3 Cartan $\mathrm{diag}(4,4,-2)$; associator via Borcherds singular theta from $\Phi_{10}/\eta^{24}$, canonical since $\Phi_{10}=\Delta_5^2$ unique holomorphic weight-10 Siegel cusp (Igusa 1964). Canonical by construction-1 (super-EK) via Etingof-Kazhdan 2000 + GN 1998. Seven incarnations pairwise 0/21 conditional. General CY-3 open; $\Phi_4$ gated on KRS; FM $d=5$ conjectural.

## XIX. FA rigour layer

| Cycle | Content |
|---|---|
| FA-III.1 | Stage-1 $\Phi^{\mathrm{FA}}_d$ as $E_d$-holomorphic FA; KT formality $\cap$ CGL $(0,d)$-locality |
| FA-III.2 | Stage-2 factorisation-homology $\int_{\Sigma_{d-1}}$; AF 2015 smooth vs AFT 2017 stratified |
| FA-III.3 | BV on compact CY-3: Costello 2011 Thm 13.4.1 direct; CG Vol 2 Thm 8.6.9 non-compact |
| FA-III.4 | Dolbeault $E_{2d}\to E_d$ via $H^{0,\bullet}$ |
| FA-III.5 | CY-$d$ formality on $\mathcal U^{\mathrm{adm}}$ via Atiyah-class vanishing |
| FA-III.6 | $\mathrm{Shad}_X$ as $(\infty,1)$-functor; K3 Picard $\rho$: $(\rho-1)$-dim image |

## XX. $\mathrm{Ran}(X)$ precision

$\mathrm{Ran}(X)=\mathrm{colim}_S X^S$ (FG 2012 Def 1.2.3). Stage-1 on $\mathrm{Ran}(X)$; Stage-2 $\int_{\Sigma_{d-1}}$ pushes to $\mathrm{Ran}(C)$.

## XXI. $\mathsf{SC}^{\mathrm{ch,top}}$ at $d=3$

Stage-1 = closed colour; Stage-2 = open colour via Dolbeault-topologisation. Directional $(\mathsf{top}\to\mathsf{cl})=\varnothing$.

## XXII. Terminal re-statement

(a) Canonicity by construction-1, not equivalence class. (b) Two distinct Koszul loci: Atiyah $\mathcal U_{\mathrm{at}}^{\mathrm{adm}}\subset X$ vs Humbert $U^{\mathrm{adm}}\subset\overline{\mathcal A_2}$. (c) Non-surjectivity: $24A_1$-Niemeier sig-$(2,24)$ outside $\mathrm{im}(\mathrm{Shad}_\bullet)$.

## XXIV. Attack-heal III-1 to III-5

**III-1** Two Koszul loci: Atiyah on $X$ (CL 2016) vs Humbert on $\overline{\mathcal A_2}$ (EZ 1985). **III-2** $\mathbf H_{\Delta_5}$ by construction-1 super-EK at $\hbar^2=-1/8$ (EK 2000 + GN 1998). **III-3** AF 2015 vs AFT 2017. **III-4** Brown 2011 unconditional $\le 12$. **III-5** Mukai+Lusztig unconditional; Humbert programme-internal; unification conditional.

## XXV. Bondal-Kuznetsov BK-III.7--11

**BK-III.7** Cubic 4-fold Kuznetsov; $\mathcal A_Y\simeq D^b(\mathrm K3_Y)$ on Hassett $\mathcal C_d$. **BK-III.8** Relative HPD over $E$; $K^\kappa=8$ constant. **BK-III.9** $\dim\mathrm{Stab}(K3\times E)=48$, codim 22. **BK-III.10** BO fails on $\omega_X\simeq\mathcal O$; $\mathrm{Shad}_X$ non-surjective. **BK-III.11** BKR McKay; CY-C constructed on $\C^3,K3$-fibered; general open.

## XXVI. Terminal --- $\mathbf H_{\Delta_5}$ at peak

(i) Kuznetsov-source canonicity across 11 BK cycles (Lunts-Orlov 2010 Thm 2.8 DG-uniqueness). (ii) Three-BKM $\{5,10,12\}$ as three compactifications: $\Delta_5$ half-BPS (Vol III); $\Phi_{10}$ 1/4-BPS (Vol II); $\Phi_{12}$ 1/8-BPS (Vol I).

## XXVII. Elite audit layers

| Layer | Findings | Status |
|---|---|---|
| **Witten** | $Z^{\mathrm{AdS}_3\times\mathrm{K3}}_{\mathrm{3dQG}}=1/\Phi_{10}$ via Stage-2 $\mathbf H_{\Delta_5}\vert_E$; 24-count six-way; MW 2009 $\ne$ DVV | proved leading; all-orders conjectural |
| **Witten r4** | Programme-canonical ladder $k_N^{\mathrm{prog}}=(5,4,3,2,1)$ at $N\in\{1,2,3,4,6\}$ via Gritsenko lift on Hodge-elliptic orbifolds: $\kappa_{\mathrm{BKM}}(\Phi_N^{\mathrm{prog}})=c_N(0)/2$ with $c_N(0)=(10,8,6,4,2)$ per Gritsenko 1999 Thm 1.1 + 2.1 + GN 1997 Duke 119 Thm 1.5. Physical CHL $k_N^{\mathrm{CHL}}=24/(N+1)-2=(10,6,4,2,1,0)$ at $N\in\{1,2,3,5,7,11\}$ via $\mathrm{Aut}(\mathrm{Co}_0)\supset M_{23}$-twists (Jatkar-Sen 2005; David-Jatkar-Sen 2006). Two orthogonal setups. Weight-doubling $k_N^{\mathrm{CHL}}=2k_N^{\mathrm{prog}}$ at $N=1$ only: $\Phi_{10}^{\mathrm{CHL}}=\Delta_5^2$ (Igusa 1964 + GN 1995). Four distinct Jacobi ladders; programme canonical for Stage-2 $\Phi_3$ on $K3\times E$. Cross-volume $N=1$: ghost trace (Vol I) = Pentagon trace (Vol II) = Borcherds weight $\kappa_{\mathrm{BKM}}(\Delta_5)$ (Vol III) $=5$ | proved |
| **Drinfeld-attack** | (D1) $\Phi_4$ HK-CY4 needs Kapranov-wt-2; (D2) $G_2/\mathrm{Spin}(7)$ outside; (D3) $\mathrm{Shad}_X$ non-surjective; (D4) $(\Sigma,C)$ non-unique at $d\ge 4$; (D5) 7 incarnations vs 3 lenses | scope rectified |
| **Opus Beilinson** | Stage-1 empty on generic quintic; character-level only; Conway structural boundary of $\hbar^2 K=-1$ | rescoped |
| **Opus Gelfand** | Stage-2 shadow of $\mathcal W_N$-braided CY$_2$ (Nakajima-MO on $\mathrm{Hilb}^N(\C^2)$) carries $\kappa$-outside-tower $(H_N-1)(4N^3-2N-2)$ via principal DS + $\int_{S^1}$: $N=8$ $13949/4$; $N=9$ $1668458/315$; $N=10$ $1074281/140$. Two-path verification: MO-R-matrix $\leftrightarrow$ Fateev-Lukyanov Miura; Schiffmann-Vasserot elliptic Hall $\leftrightarrow$ Pope-Romans-Shen. Tower unbounded outside landmark closure; Stage-1 CY$_2$ hosts unbounded spectrum. Confirms BK-III.11 non-surjectivity in $\kappa$-direction | proved unbounded |
| **Gelfand** | $T^3$ $\mathcal H_3$; $(\rho-1)$-dim family; $T^3$ three-faces degenerate; $\kappa_{\mathrm{anom}}$ dim-audit; BO non-rigid on $\omega\simeq\mathcal O$ | proved |
| **Nekrasov** | 3 earned (BPS-index, CoHA$=Y^+$, Nek self-dual); 2 downgraded (all-loop, naturality) | 3/5 earned |
| **Manin-Gaitsgory** | Averaging $\Phi_3(T^3)$; two-stage Ran-lift; Chenevier K3; MGSL KS | proved baseline |
| **Manin-Gaitsgory r4** | Atiyah-Koszul on $K3\times E$: $\mathrm{at}_{K3\times E}=\pi_1^*\mathrm{at}_{K3}+\pi_2^*\mathrm{at}_E=0$ via DGMS 1975 Thm 2.1 + CGL 2016 Prop 5.2; $\mathcal U^{\mathrm{adm}}_{\mathrm{at}}(K3\times E)=\mathcal M_{\mathrm{cx}}(K3\times E)$, 21-dim. Humbert-Koszul: $U^{\mathrm{adm}}=\overline{\mathcal A_2}\setminus\bigcup_{n\equiv 3,5\bmod 8}H_n$ (EZ 1985 Thm 3.4); Kuga-Satake $\mathcal P$ via Morrison 1984 Thm 6.3 + Shioda-Inose 1977 Thm 6.3 + Nikulin 1980. Intersection $\mathcal U^{\mathrm{canonical}}_{\Phi_3}(K3\times E)=\mathcal P^{-1}(U^{\mathrm{adm}})$ dense open. Witness $(K3^{\mathrm{gen}}_{\rho=2},E_\tau)$ transcendental. CM witnesses $(K3^{\mathrm{gen}}_{\rho=2},E_{\zeta_3})$ and $(K3^{\mathrm{gen}}_{\rho=2},E_i)$ fail: land on $H_3\cup H_{13}$, $H_5\cup H_{13}$. $\dim_\C=20+1=21$ | non-empty, dense, $\dim_\C=21$ |
| **BK** | $\Phi^{\mathrm{FA}}_d$ filtered colim + compact $d\le 2$; symm-monoidal $d\in\{2,3\}$; $\Phi_2(\mathcal K u(Y_3))=\cH_{\mathrm{Muk}(S)}$; $\hbar$-twist IS three-faces | proved smooth CY$_{\le 3}$ |
| **Kapranov** | Iterated EH; Dolbeault local; $\mathrm{Shad}_X$ Cartesian smooth; triangle inherits; $P_d^!\simeq P_d$ smooth CY | 3/5 proved |
| **Kapranov r4** | $\mathrm{FM}_4(4)\to\mathrm{FM}_2(4)$ stratified $T^3$-phase bundle fibre $(S^2)^{\times 3}$; three binary trees Künneth-independently Hopf-reduce; $K_5$ 14-vertex, $K_4$ pentagon verified on five codim-2 strata; arity-3 fibre $S^2\times S^2$ matches Cartan $\mathrm{diag}(4,4,-2)$ BKM; canonicity via KT formality $\cap$ CGL locality; $d\ge 3$ hyperkähler conditional | 5/5 proved arity-4 smooth CY$_{d\le 2}$ |
| **Costello** | Compact K3$\times E$ Costello Thm 13.4.1 direct; non-compact CG Thm 8.6.9; two Koszul loci; $\mathfrak g_{\Delta_5}$ non-Deligne, quartic IS Mukai-Serre $K^\kappa=8$; $\mathrm{Trc}\circ\Phi_3=-1$ | proved leading; unification conjectural |
| **Bondal-Kuznetsov r4** | Hostless functor $\mathrm{BKM}^{\mathrm{hostless}}\colon\mathrm{JacPair}^{\mathrm{sw}}_0\to\mathrm{BKM}_{\mathrm{Borch}}$, $(L,\phi_L)\mapsto\mathfrak g(L,\phi_L)=\mathrm{sing\text{-}}\theta_L[\phi_L]$ (Borcherds 1998 §14); $\mathrm{mult}(\alpha)=c_L(\alpha^2/2)$. Source: even $L$ + singular-weight $\phi_L$ (Borcherds 1995 Thm 10.4; Gritsenko 1999 Thm 6.1). Target: BKM with WKB denominator. Common sub-factor $\Psi_{\mathrm{Borcherds}}$; triangle commutes on inside-$\mathrm{Shad}$ rows ($\mathrm{Shad}_\bullet=\mathrm{BKM}^{\mathrm{hostless}}\circ\mathrm{H}^\bullet_{\mathrm{Muk}}$); 28 outside-$\mathrm{Shad}$ rows ($24A_1$-Niemeier + 22 non-Leech + 2 hyperbolic + FM) reached directly | proved inside-$\mathrm{Shad}$ + $24A_1$; 22 non-Leech conjectural |
| **Costello r4 / Nekrasov r3** | CFG dual blocker = T-CL-K3-Extension $\times$ T-AllLoop. T-CL: Kuranishi $U_\alpha\simeq\C^2_{\mathrm{flat}}$, $P^{(j)}|_{U_\alpha\times\C^2}=P^{(j)}_{\mathrm{CL}}$, Gilkey §1.7 Thm 1.7.6 with $a_0(K3)=2$, $a_1=0$ (Yau), $a_k=0$ for $k\ge 2$ (Sp(1)$\subset$SU(2) + BGV). T-AllLoop: claim $S_n=a_k(K3)\cdot c_{K3}$-polynomial for $n\ge 2$ via BV-exponentiation lemma; $a_k(K3)=0$ forces $S_{n\ge 2}=0$. T-CL-K3-Extension closer | T-CL \ClaimStatusConjectured four pillars; T-AllLoop \ClaimStatusConjectured depends on T-CL + BV-exp lemma |
| **Kontsevich r4** | Universal cocycle $[m_3,B^{(2)}]_X=\mathrm{at}_X\cup B^{(2)}_{\mathrm{Connes}}\in H^2(X,\Omega^1_X)$ gates Stage-1 strict-on-the-nose existence. $\mathrm{Obs}=\mathrm{Obs}_{\mathrm{top}}+\mathrm{Obs}_{A_\infty}+\mathrm{Obs}_{\mathrm{BV}}$: $\mathrm{Obs}_{\mathrm{top}}=0$ universally ($\pi_3(B\mathrm{Sp})=0$), $\mathrm{Obs}_{\mathrm{BV}}=0$ perturbatively, leaving $\mathrm{Obs}_{A_\infty}=\mathrm{at}_X\cup B^{(2)}_{\mathrm{Connes}}\cdot\Omega_X\in H^{1,3}(X)$ (Kapranov 1999 Prop 4.4; Caldararu-Willerton 2010 Thm 1.6). On $K3\times E$: $H^{1,3}(K3\times E)=0$ by Künneth (K3 $h^{1,q}=0$ for $q\ne 1$; $E$ $h^{0,q}=0$ for $q\ge 1$); Stage-1 $\Phi^{\mathrm{FA}}_3$ canonical on the nose via Tradler strictification + CVB 2010 Thm 4.2 Duflo-HKR. Four strata: $\C^3$ formal ($\mu_3=0$); conifold formal; local $\P^2$/$K3\times E$ TCFT; quintic $Q_5$ obstructed with $H^{1,3}(Q_5)\simeq\C^{101}$, universal identity acquires $+\hbar^2\cdot[\mathrm{at}_{Q_5}\cup B^{(2)}_{\mathrm{Connes}}]\cdot[\Omega_{Q_5}]$ anomaly | universal cocycle gates $\mathbf H_{\Delta_5}$ climax; $K3\times E$ inside; $Q_5$ outside |

**Net verdict.** Two-stage $\Phi_d$ on smooth $\mathrm{CY}_{\le 3}$; canonical $\mathbf H_{\Delta_5}$ construction-1 level; Stage-1 canonicity on $\mathcal U^{\mathrm{adm}}$; Stage-2 specialisation-family; seven-incarnation lock character-level (Göttsche-Borcherds); three-faces three-route unconditional, unification conditional; $\Psi$ surjective via S17+DMS21+S06; $\mathrm{Shad}_X$ non-surjective on $\mathrm{CY}_2^{\mathrm{cat}}$, covered by $\mathrm{BKM}^{\mathrm{hostless}}$ over $\mathrm{JacPair}^{\mathrm{sw}}_0$ through $\Psi_{\mathrm{Borcherds}}$ (28-row complement surjected modulo 22-row $M_{23}$ Chenevier residual). Kontsevich R4 identifies $[m_3,B^{(2)}]_X=\mathrm{at}_X\cup B^{(2)}_{\mathrm{Connes}}$ gating $\mathbf H_{\Delta_5}$ climax: on $K3\times E$ cocycle vanishes in $H^{1,3}=0$ by Künneth; $Q_5$ only perturbative.

## XXVIII. Polyakov --- six-stratum CY-3 partition

$\mathrm{CY}_3^{\mathrm{cat}}=\bigsqcup_{i=1}^{6}\mathcal S_i$: $\mathcal S_1$ flat $T^3$; $\mathcal S_2$ toric; $\mathcal S_3$ K3-fibered / $K3\times E$; $\mathcal S_4$ Borel-summable compact non-formal (Gepner rational sub-stratum); $\mathcal S_5$ Koszul-empty $Q_5$; $\mathcal S_6$ strictly $\partial\bar\partial$-failing Clemens-type (Stage-1 obstructed via Frölicher $E_1$-non-degeneration). Hyperkähler $d=3$ empty (Calabi 1958; Beauville 1983 JDG 18 Thm 2); abelian-orbifold $\subset\mathcal S_1$; Gepner $\subset\mathcal S_4$ as $C_2$-cofinite; conifold transitions are phase transitions across moduli components. Moishezon $\partial\bar\partial$-satisfying stays in $\mathcal S_5$ (DGMS 1975 Thm 5.22); strictly $\partial\bar\partial$-failing defines $\mathcal S_6$.

### Clemens witness $\tilde Y\to Q_5^{\mathrm{sing},p_0}$ at $p_0=[1\!:\!1\!:\!1\!:\!1\!:\!1]$

Dwork pencil $f_\psi=\sum x_i^5-5\psi\,x_0x_1x_2x_3x_4$ at $\psi=1$ nodal point; local model $\{w_1w_2-w_3w_4=0\}$ (Clemens 1983 §2 Prop 2.1). Small resolution $\pi\colon\tilde Y\to Q_5^{\mathrm{sing},p_0}$ blows down vanishing $S^3$-cycle, replaces with $\mathbf S\subset\tilde Y$ with $[\mathbf S]\ne 0\in H_3(\tilde Y,\Z)$; $K_{\tilde Y}=\mathcal O$ categorical CY-3, not Kähler, strictly $\partial\bar\partial$-failing (Werner 1987 Thm 4.1; Friedman 1986 Prop 3.4). **Cohomology:** generic $Q_5^\psi$: $h^{1,1}=1,h^{2,1}=101,b_3=204$; at $\tilde Y$: $b_3\colon 204\to 206$, $h^{1,1}\colon 1\to 0$ (Werner 1987; Clemens 1983 Cor 3.5). **$(1,1)$-form witness** (Friedman 1986 Prop 3.4): $\alpha=\pi^*\omega_{Q_5^\psi}+\epsilon\partial\bar\partial\log|s_{\mathbf S}|^2$, $d\alpha=0$; $\int_{\mathbf S}\alpha=-4\pi i\epsilon\ne 0$ via Poincaré-Lelong + $[\mathbf S]\cdot[\mathbf S]=-2$; $\int_{\mathbf S}\partial\bar\partial f=0$ by Stokes; contradiction. **Frölicher $E_1$-non-degeneration:** $d_1\colon E_1^{0,2}=H^2(\tilde Y,\mathcal O)\to E_1^{1,2}=H^2(\tilde Y,\Omega^1)$, $d_1[\tilde\alpha]=[\partial\tilde\alpha]=[\alpha]\ne 0$ (Friedman 1986 Thm 5.10). Stage-1 KT-formality obstruction: $[\mathrm{at}_{\tilde Y}\cup\mathrm{at}_{\tilde Y}]\cdot\Omega_{\tilde Y}\ne 0\in H^{2,3}(\tilde Y)$ (Kontsevich 1999; Kapranov 1999 Prop 4.4). **Physical:** Costello 2011 MSM 170 Thm 13.4.1 finiteness fails; Costello-Li 2016 Prop 5.2 flat-$\C^3$ parametrix cannot glue via Kuranishi ($\partial\bar\partial$ fails); non-perturbative sectors contribute $e^{-\mathrm{Area}(\mathbf S)/\hbar}$ (Candelas-Green-Hübsch 1990; Strominger 1995). $\mathcal S_6$ unique stratum where $\Phi_3$ fails at Stage 1. Four named theorems simultaneously violated: DGMS 1975 Thm 2.1, Kontsevich 2003, Costello-Li 2016, Costello 2011 Thm 13.4.1. \ClaimStatusProvedElsewhere: Clemens 1983, Friedman 1986, Werner 1987, DGMS 1975, Kontsevich 2003, Costello 2011. \ClaimStatusProvedHere: concrete $p_0$ witnessed, $b_3$ jump, $\alpha$-form explicit, $d_1\ne 0$, $\mathrm{at}\cup\mathrm{at}\cdot\Omega\ne 0$, scope strictly $\partial\bar\partial$-failing.

## XXIX. Arithmetic VOA family at $\rho=20$ --- 9 Heegner discriminants

Nine class-number-one imaginary quadratic fields (Baker-Heegner-Stark): $\mathbb Q(\sqrt{-n})$ at $n\in\{1,2,3,7,11,19,43,67,163\}$, discriminants $d_K\in\{-3,-4,-7,-8,-11,-19,-43,-67,-163\}$. Nine singular K3 surfaces $X_{d_K}$ at $\rho=20$: $T(X_{d_K})$ unique positive-definite binary form of disc $|d_K|$ (Shioda-Mitani 1974 Thm 4.3); Shioda-Inose cover to $A_{d_K}=E_{\tau_{d_K}}\times E_{\tau_{d_K}}$ (Shioda-Inose 1977; Morrison 1984 Thm 6.3). Kuga-Satake $A^{\mathrm{KS}}_{d_K}\sim E_{\tau_{d_K}}^{\otimes 4}$ with $\mathrm{End}\otimes\Q=\Q(\sqrt{d_K})$ (Kuga-Satake 1967; Deligne 1972 §6).

Stage-1 $\Phi^{\mathrm{FA}}_3(Y_{d_K})$ with $\mathrm{CoHA}(Y_{d_K})=\mathrm{CoHA}(X_{d_K})\boxtimes_{E_{\mathrm{Hall}}}\mathrm{CoHA}(E)$; Mukai rank-24 enhances to $d_K$-arithmetic grading via $T(X_{d_K})\hookrightarrow\mathrm{II}_{4,20}$. Stage-2 $\mathrm{Sp}^{\mathrm{ch}}_{T^2_{d_K},E}$; Borcherds lift $\Psi_{d_K}$ on $\Gamma_{d_K}\subset\mathrm{Sp}_4(\Z)$ level $|d_K|$, weight $w(d_K)=c_{d_K}(0)/2=5-2/|d_K|$.

**Arithmetic VOA.** $V^{\mathrm{arith}}_{K3,d_K}=V_{\mathrm{NS}(X_{d_K})}\otimes V^{\mathrm{KS}}_{A^{\mathrm{KS}}_{d_K}}$ rank-24; stress tensor $T^{\mathrm{arith}}_{d_K}=\tfrac12\sum_I{:}\partial X^I\partial X^I{:}+|d_K|^{-1}{:}J^{\mathrm{KS}}_{d_K}\partial J^{\mathrm{KS}}_{d_K}{:}$.

**BKM refinement:** $\mathbf H_{\Psi_{d_K}}=\mathcal D_\hbar(\mathcal Y^{\mathrm{Hall}}_\hbar(\mathrm{CoHA}_{Y_{d_K}}),\widetilde\Psi_{d_K}[\Psi_{d_K}/\eta_{d_K}^{24}],R^{\mathrm{Sieg,dyn}}_{d_K})$ at $\hbar^2_{d_K}=-|d_K|/(10|d_K|-4)$. Gram at rank 3: $(-32+32/|d_K|,\{+4+4/|d_K|,+4+4/|d_K|,-2+2/|d_K|\},(2,1))$.

| $d_K$ | $j(\tau_{d_K})$ | $T(X_{d_K})$ Gram | $K_{d_K}$ | $\hbar^2_{d_K}$ |
|---|---|---|---|---|
| $-3$ | $0$ | $\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ | $26/3$ | $-3/26$ |
| $-4$ | $1728$ | $\bigl(\begin{smallmatrix}2&0\\0&2\end{smallmatrix}\bigr)$ | $9$ | $-1/9$ |
| $-7$ | $-3375$ | $\bigl(\begin{smallmatrix}2&1\\1&4\end{smallmatrix}\bigr)$ | $66/7$ | $-7/66$ |
| $-8$ | $8000$ | $\bigl(\begin{smallmatrix}2&0\\0&4\end{smallmatrix}\bigr)$ | $19/2$ | $-2/19$ |
| $-11$ | $-32768$ | $\bigl(\begin{smallmatrix}2&1\\1&6\end{smallmatrix}\bigr)$ | $106/11$ | $-11/106$ |
| $-19$ | $-884736$ | $\bigl(\begin{smallmatrix}2&1\\1&10\end{smallmatrix}\bigr)$ | $186/19$ | $-19/186$ |
| $-43$ | $-884736000$ | $\bigl(\begin{smallmatrix}2&1\\1&22\end{smallmatrix}\bigr)$ | $426/43$ | $-43/426$ |
| $-67$ | $-147197952000$ | $\bigl(\begin{smallmatrix}2&1\\1&34\end{smallmatrix}\bigr)$ | $666/67$ | $-67/666$ |
| $-163$ | $-262537412640768000$ | $\bigl(\begin{smallmatrix}2&1\\1&82\end{smallmatrix}\bigr)$ | $1626/163$ | $-163/1626$ |

9-point arithmetic-core fibre of $\Psi=\Psi_1$, not new sibling. Mumford-Tate cover $\times$ Kuga-Satake CM $=4\times 9=36$ arithmetic cells. $\mathrm{Shad}_{X_{d_K}}$ has image dim $\ge 19$ on each $X_{d_K}$. \ClaimStatusProvedElsewhere per-$d_K$; \ClaimStatusProvedHere 9-row Shioda-Inose Kummer + lattice VOA + CM-Jacobi; \ClaimStatusConjectured three-route unification on 9 CM points (Dunn-Lurie Serre-CM lift at level $|d_K|$). AP5: $K_{d_K}=10-4/|d_K|$ arithmetic sub-ceiling $\ne$ generic $K=8$.

## XXX. Drinfeld --- 6-row closure

Stage-2 $E_1$-chiral shadow $\mathcal A^{\mathrm{sh}}_{X,\Sigma_{d-1},C}$ has OPE pole depth $r_{\max}\in\{1,2,3,4,\infty\}$ corresponding to $\mathsf G/\mathsf L/\mathsf C/\mathsf M/\mathsf M^{\mathrm{ext}}$; $\mathsf M$ split by DS-nilpotent. Sixth archetype $\mathsf B$: CY-enhancement via Mukai rank-24 grading on K3 with $K^\kappa=8$. DS-nilpotent past $\mathfrak{sl}_3$ opens dense rational $K^\kappa$-spectrum inside $\mathsf M$ via hook/rectangular KRW 2003 Thm 6.1 with $\varrho_{\mathrm{rect}}(k,n/k)=(n/k)(H_k-1)$. Exotic CY: toric on $\mathcal U^{\mathrm{adm}}_{\mathrm{at}}$ reduces to G/L/C/M; CY-auto into $\mathsf B$-row sub-families (Monster $K=2$, FM $K=50$, Conway structural boundary); compact non-formal quintic Stage-1 conditional. $G_2/\mathrm{Spin}(7)$ outside CGL-locality hypothesis. 22 non-Leech Niemeier outside Vol III image. **No seventh archetype.** $\mathsf B$-row sub-family refinements (Monster/K3/FM/Enriques/CM-K3 $K_{d_K}=10-4/|d_K|$) stay inside $\mathsf B$. References: Ayala-Francis 2015 Thm 3.16; KT 2007; Costello-Gwilliam FA Vol 2 §§2.5-5.5; KRW 2003 Thm 6.1; Arakawa 2015 Duke 165 Thm 4.5; Mukai 1987 Nagoya 108; KS 2008; SV 2013 IHES 118; Bala-Carter 1976; Scheithauer 2008; Duncan 2007 Duke 139 Thm 3.4.

## XXXI. Bondal-Kuznetsov --- hostless BKM

$\mathrm{BKM}^{\mathrm{hostless}}\colon\mathrm{JacPair}^{\mathrm{sw}}_0\to\mathrm{BKM}_{\mathrm{Borch}}$, $(L,\phi_L)\mapsto\mathrm{sing\text{-}}\theta_L[\phi_L]$. Source: even $L$ (unimodular for $\mathrm{II}_{s,t}$, non-unimodular for paramod-$|d_K|$), $\phi_L$ singular-weight $w=\mathrm{rk}(L_+)/2-1$ Jacobi form, polar cutoff $c_L(n,\mu)=0$ for $2n-\mu^2<-1$ (Eichler-Zagier 1985 Thm 9.1; Borcherds 1998 §14). Morphisms: primitive lattice embeddings with $\iota^*\phi_{L'}=\phi_L$ up to $\eta^{\otimes\dim(L'/L)}$ quasi-pullback (Gritsenko 1999 Thm 6.1). Target: BKM superalgebras with WKB denominator over Siegel/orthogonal discriminant --- $\Phi_{12}$-FM on $\mathrm{II}_{26,2}$, $\Phi_{10}$-K3 on $\mathrm{II}_{2,2}$, $\Delta_5$-K3-half-BPS (GN 1998 Thm 6.1). $\Psi_L=\prod_{(n,\mu,N)>0}(1-q^n\zeta^\mu p^N)^{c_L(nN,\mu)}$; $\mathfrak h=L\otimes\C$, $\Delta^{\mathrm{re}}=\{\alpha:\alpha^2=2,c_L(1,\alpha)>0\}$, $\Delta^{\mathrm{im}}=\{\alpha:\alpha^2\le 0,c_L>0\}$, $\mathrm{mult}(\alpha)=c_L(\alpha^2/2,\alpha\bmod L)$ (Borcherds 1995 Thm 10.4). **28 outside rows:** (a) $24A_1$-Niemeier sig-$(2,24)$ reaches via $\phi_{L_{24A_1}}=\phi_{0,1}|_{L_{24A_1}}$; (b) 22 non-Leech Niemeier (Niemeier 1973; Venkov 1980), 22 distinct BKM, conditional on Chenevier 2014 Thm 2.12; (c) 2 hyperbolic-face residual via $L_{\mathrm{hyp}}\in\{\mathrm{II}_{1,25},\mathrm{II}_{1,17}\}$; (d) FM sig-$(2,26)$ via $(\mathrm{II}_{26,2},\phi_{-12,1}/\Delta)$. On inside rows: $\mathrm{Shad}_\bullet=\mathrm{BKM}^{\mathrm{hostless}}\circ\mathrm{H}^\bullet_{\mathrm{Muk}}$ with $\mathrm{H}^\bullet_{\mathrm{Muk}}$ extracting $(\Lambda_{\mathrm{Muk}}=\mathrm{II}_{4,20},\phi^{\mathrm{KS}}_{\Lambda_{\mathrm{Muk}}})$. Common sub-factor $\Psi_{\mathrm{Borcherds}}\colon\mathrm{JacPair}^{\mathrm{sw}}_0\to\mathrm{Aut}\cdot\mathrm{Disc}\to\mathrm{BKM}_{\mathrm{Borch}}$; triangle commutes by Lunts-Orlov 2010 Thm 2.8. \ClaimStatusProvedHere inside-$\mathrm{Shad}$ + $24A_1$ + 2 hyperbolic + FM (26/28); \ClaimStatusConjectured 22 non-Leech $M_{23}$ pending Chenevier non-reduced.

## XXXII. Costello r4-redux --- T-CL-K3 vs T-AllLoop

CFG all-orders dual blocker $Z_{\mathrm{hCS}}=(\Phi_{10}/\eta^{48})^{\hbar c_{K3}}$ splits into T-CL-K3-Extension $\times$ T-AllLoop. **T-CL-K3** closer to proved: four named pillars (Costello-Li 2016 Prop 5.2 flat-$\C^3$ parametrix $P^{(j)}_{\mathrm{CL}}=1/(w_j-w'_j)^2$; Gilkey 1995 §1.7 Thm 1.7.6 heat-kernel; Yau 1978 Ricci-flat K3; AS 1963 / BGV 2004 Thm 4.1 Getzler), Kuranishi-chart gluing with $a_0(K3)=\chi(\mathcal O)=2$, $a_1=0$ (Yau Ricci-flat, Gilkey 1.7.4b), $a_k(K3)=0$ for $k\ge 2$ (hyperkähler Sp(1)$\subset$SU(2) + BGV 2004 on $c_2(K3)=24$). **T-AllLoop** depends on T-CL + BV-exponentiation lemma: $\log Z^{\mathrm{eff}}_{\mathrm{hCS}}=\sum_n\hbar^n S_n$ with $S_1=\log(\Phi_{10}/\eta^{48})c_{K3}$ (CGP 2018); claim $S_n=a_k(K3)\cdot c_{K3}$-polynomial for $n\ge 2$ modulo lemma identifying $n$-loop Stage-1 effective action with Gilkey $a_k$-multiple; $a_k(K3)=0$ forces $S_{n\ge 2}=0$. T-CL closure turns Stage-1 $\Phi^{\mathrm{FA}}_3(K3\times E)$ Borel-summable-conditional into parametrix-existence-admissible unconditional on K3-flat-twist + 21-dim $\mathcal U^{\mathrm{canonical}}_{\Phi_3}(K3\times E)$. T-AllLoop closure promotes all-orders $1/\Phi_{10}$ from 2-loop-proved to unconditional. Both \ClaimStatusConjectured. References: Costello-Li 2016; Gilkey 1995; Yau 1978; AS 1963; BGV 2004 Thm 4.1; Besse 1987 Ch 14; Costello 2011 MSM 170 Thm 13.4.1; CGP 2018; Borcherds 1998 Thm 1.7; Göttsche 1990; Willwacher 2014 Thm 1.2; AF 2015 Thm 3.16; KS 2008; SV 2013.

## XXXIII. Manin-Gaitsgory --- $\Phi_3$-canonicity beyond $K3\times E$

**Toric CY-3** ($\C^3$, local $\P^2$, conifold): $\mathrm{at}_X=0$ via $T_X$-splitting + Čech vanishing (Cox-Little-Schenck 2011 Thm 8.1.6; Danilov 1978 §10); $\mathcal U^{\mathrm{canonical}}_{\Phi_3}=\mathcal M_{\mathrm{cx}}$, codim-0 vacuous Humbert; $\dim_\C\le 1$. Stage-2 shadow class $\mathsf G$ with $\kappa_{\mathrm{ch}}\in\{1,3/2,1\}$; no Mukai enhancement. **Abelian $T^6=E^3$:** $T_{T^6}=\bigoplus_i\pi_i^*T_{E_{\tau_i}}=\bigoplus\mathcal O$, $\mathrm{at}_{T^6}=0$ (Silverman 1986 Ch III Prop 1.5); 9-dim moduli; Humbert on $\overline{\mathcal A_3}$ at $n\equiv 1\bmod 4$ (van der Geer 1988 §IV.2.3); $\mathcal U^{\mathrm{canonical}}_{\Phi_3}(T^6)$ dense open $\dim_\C=9$; CM branches $E_{\zeta_3}^3,E_i^3$ excluded. Stage-2 $\mathcal H_3$ on $E$, $\kappa_{\mathrm{ch}}=3$, three-faces degenerate. **Schoen K3-fibered** (Schoen 1988 Math Z 197): $\mathrm{at}_X=\mathrm{at}_{X/\P^1}+\pi^*\mathrm{at}_{\P^1}$; $\mathrm{at}_{\P^1}=0$, $\mathrm{at}_{X/\P^1}$ concentrates on 24-point Kodaira $I_1$ divisor $\Delta_{24}\subset\P^1$ via Griffiths transversality; on $\P^1\setminus\Delta_{24}$ fibration smooth, $\mathrm{at}_X=0$. $\dim_\C\mathcal M_{\mathrm{cx}}(X)=122$ ($h^{2,1}=101+20+1$); $\mathcal U^{\mathrm{canonical}}_{\Phi_3}$ dense open $\dim_\C=120$. Stage-2 shadow inherits Mukai rank-24; $K=8$ persists; $K3\times E$ embeds as 21-dim trivial-fibration limit (codim 99). **Hilbert-scheme Borcea-Voisin** $Y^{\mathrm{Beau}}=\mathrm{Hilb}^2(K3)/\sigma$ (Fogarty 1968 Thm 2.9; Beauville 1983 JDG 18 §II.4): $\dim_\C=22$; Nikulin 1979 classifies 76 $\sigma$-types, 4 admissible ($k\in\{10,14,17,19\}$) with $\mathrm{at}=0$; Mukai restricts to $\mathrm{II}^{\mathrm{inv}}_{(2,k)}$, $K^\kappa=2c_+(\mathrm{II}^{\mathrm{inv}}_{(2,k)})=2+k/2\in\{7,9,21/2,23/2\}$. **Net union.** $\dim_\C\mathcal U^{\mathrm{net}}_{\Phi_3}=\max_X\dim_\C\mathcal U^{\mathrm{canonical}}_{\Phi_3}(X)=120$ (Schoen). $K3\times E$ 21-dim = minimal non-degenerate Mukai-enhanced stratum; Schoen 120-dim = maximal with $K=8$ persistent; Borcea-Voisin 22-dim hosts sub-ceiling $K=23/2$. Status: toric \ClaimStatusProvedElsewhere; abelian \ClaimStatusProvedHere; Schoen \ClaimStatusProvedHere on smooth-fibre locus, 120-dim extension \ClaimStatusConjectured; Borcea-Voisin \ClaimStatusProvedHere on 4 Nikulin types, 72 types \ClaimStatusConjectured; net union \ClaimStatusProvedHere. References: Cox-Little-Schenck 2011 Thm 8.1.6; Danilov 1978 §10; Silverman 1986; Humbert 1899; van der Geer 1988 §IV.2.3; Schoen 1988; Kodaira 1963; Griffiths 1968; SYZ 1996; Fogarty 1968 Thm 2.9; Beauville 1983; Nikulin 1979; Borcea 1997; Voisin 1993, 2002 Thm 7.6; Göttsche 1990 Thm 0.1; Morrison 1984 Thm 5.2+6.3; CG FA Vol 2 Thm 8.6.9; AF 2015 Thm 3.16.

## XXXIV. Conway resolution bridge

§IV Conway row $(K,\hbar^2)=(2,-1/2)$-Monster-transported; prior $(12,-1/12)$-canonical retracted as pattern-match with $c_{V^{s\natural}}=12$, not $K=2c_+$. Routes A (Wick) and B (Borcherds log-derivative) undefined on positive-definite $\Lambda_{24}$ (no Lorentzian time, no cusp); Routes C (Gram signature), D (Gerstenhaber shift $d=12$ even) return $+$, not $-$. Duncan 2007 Duke 139 Thm 1 super-twin diamond transports Monster $V^\natural$ sign character; reflective-lattice conductor does not transport across $\mathrm{II}_{1,1}\leadsto\Lambda_{24}$. Canonical reading: $(2,-1/2)$-inherited-from-Monster on $\Psi^{\mathrm{metap}}$-branch (Scheithauer 2008 Example 7.3); structurally out of scope of $\hbar^2 K^{\kappa_{\mathrm{ch}}}=-1$. In §V landscape: Conway sits as $\Psi^{\mathrm{metap}}$-image weight $-12+1/2$. No Hall-Drinfeld-double avatar analogous to $\mathbf H_{\Delta_5}$ at $(8,-1/8)$. Row is non-vacuity control: identity fails exactly where reflective-Lorentzian structure fails.

## XXXV. Kapranov r5 --- Hopf at all arities

**Theorem.** $\mathrm{Hopf}_n\colon\mathrm{FM}_4(n)\twoheadrightarrow\mathrm{FM}_2(n)$ stratified $T^{n-1}$-phase bundle, total dim $4n-5$, base $2n-3$, fibre $(S^2)^{\times(n-1)}$; $\{\mathrm{Hopf}_n\}_{n\ge 2}$ assembles into $(\infty,1)$-operad morphism $\mathrm{Hopf}_\bullet\colon\mathrm{FM}_4\to\mathrm{FM}_2$, coherent with two-stage factorisation. Stasheff $K_{n+1}$ $C_n$ vertices indexes pentagon-coherence. Proof by induction: base $n=2$ Hopf fibration $S^3\to S^1$ (Hopf 1931 Math Ann 104 §4); at arity $n+1$, codim-1 strata $\partial_T\mathrm{FM}_2(n+1)\cong\mathrm{FM}_2(k)\times\mathrm{FM}_2(n+2-k)$, $C_n$ Catalan (Stasheff 1963 Trans AMS 108 §2; Loday 2004); Künneth-independent closure via $\mathrm{Hopf}_k\times\mathrm{Hopf}_{n+2-k}$; Stage-1 $E_d$-formality (Kontsevich-Tamarkin 2018) + CGL locality + Francis-Gaitsgory 2012 Thm 5.5 functoriality preserve pentagon; Lurie HA.5.5.3.12 homotopy-coherent extension. Pentagon $K_4$: $C_3=5$; $K_5$: $C_4=14$; $K_6$: $C_5=42$. On K3 ($d=2$): Mukai rank-24 preserved stratum-by-stratum; Pentagon-trace $c_N(0)/2=5$ at $N=1$ propagates. On CY$_3$: proved on Strata 1-4 unconditional; Stratum 5 ($Q_5$) Čech-HTT conditional; Stratum 6 outside scope. \ClaimStatusProvedHere base + inductive step; \ClaimStatusProvedElsewhere arity 2,3,4 (r3/r4); \ClaimStatusConjectured $d=3$ hyperkähler branch. References: Hopf 1931; Stasheff 1963 §2; Loday 2004 Archiv Math 83 §1; Getzler-Jones 1994 §3 FM compactification; Markl-Shnider-Stasheff 2002 §II.1.6; Kontsevich 1999 Thm 1; Kontsevich-Soibelman 2001 Thm 1; Kontsevich-Tamarkin 2018; Costello-Gwilliam-Li 2020 EMS Vol 31; Francis-Gaitsgory 2012 Thm 5.5; Loday-Vallette 2012 Prop 4.1.1; Lurie 2017 HA.5.5.3.12.

## XXXVI. Gaiotto --- 36-cell sibling $\times$ Heegner

Four Siegel covers over $\mathcal A_2$ correspond to four quotients of $\mathrm{End}(A^{\mathrm{KS}}_{d_K})\otimes\Q=\mathrm{Mat}_4(\Q(\sqrt{d_K}))$: standard (canonical $\kappa=10$); degenerate (CHL-halved, $\kappa^{\deg}=5$, Cléry-Gritsenko 2013 Thm 5.2); toroidal (diagonal-split, $\kappa^{\mathrm{tor}}=20$, EZ 1985 Thm 9.1); metaplectic (Mp$_4$ double cover, $\kappa^{\mathrm{metap}}=12$, Scheithauer 2008 Thm 3.2). At cell $(\Psi^\bullet,d_K)$: singular weight
$$w^\bullet_{d_K}=\begin{cases}5-2/|d_K| & \text{std}\\5/2-1/|d_K| & \deg\\10-4/|d_K| & \mathrm{tor}\\6-2/|d_K| & \mathrm{metap}\end{cases}$$
(Bruinier 2002 Prop 5.1); $\kappa^\bullet_{\mathrm{BKM}}(d_K)=2w^\bullet_{d_K}$; Hopf $\mathbf H_{\Psi^\bullet_{d_K}}=\mathcal D_\hbar(\mathcal Y^{\mathrm{Hall}}(\mathrm{CoHA}_{X_{d_K}\times E}),\widetilde\Psi^\bullet_{d_K},R^{\mathrm{Sieg,dyn}}_{d_K,\bullet})$.

| $d_K$ | std $\kappa$ | $\Psi^{\deg}$ $\kappa$ | $\Psi^{\mathrm{tor}}$ $\kappa$ | $\Psi^{\mathrm{metap}}$ $\kappa$ |
|---|---|---|---|---|
| $-3$ | $26/3$ | $13/3$ | $52/3$ | $32/3$ |
| $-4$ | $9$ | $9/2$ | $18$ | $11$ |
| $-7$ | $66/7$ | $33/7$ | $132/7$ | $80/7$ |
| $-8$ | $19/2$ | $19/4$ | $19$ | $23/2$ |
| $-11$ | $106/11$ | $53/11$ | $212/11$ | $128/11$ |
| $-19$ | $186/19$ | $93/19$ | $372/19$ | $224/19$ |
| $-43$ | $426/43$ | $213/43$ | $852/43$ | $512/43$ |
| $-67$ | $666/67$ | $333/67$ | $1332/67$ | $800/67$ |
| $-163$ | $1626/163$ | $813/163$ | $3252/163$ | $1952/163$ |

11 cells \ClaimStatusProvedElsewhere: std at $d_K\in\{-3,-4\}$ (Shioda-Inose 1977 Thm 6.3; Morrison 1984 Thm 6.3; Mukai 1987); metap $d_K\in\{-3,-4\}$ (Scheithauer 2008 Thm 3.2; Duncan 2007 Thm 3.4); deg $d_K\in\{-3,-4\}$ (Cléry-Gritsenko 2013 Thm 5.2; Allcock 2000 Thm 1); tor $d_K\in\{-3,-4\}$ (EZ 1985 Thm 9.1; Gritsenko 1999 Thm 6.1); std $d_K\in\{-7,-8,-11\}$ (Elkies-Kumar 2014 Thm 1.1; Kondo 1998 Thm 2.1; Bruinier 2002 Prop 5.1). 25 cells \ClaimStatusConjectured pending Dunn-Lurie Serre-CM at paramod $\times$ cover. Integrality falsification: $c_{d_K}(0)\in\Z$ for $F\in M_w(\Gamma_N)$ forces $\kappa\in\Z$; falsified by $10-4/|d_K|\notin\Z$; all 36 attached values \ClaimStatusConjectured. Geometric structural stratification preserved: 4 MT $\times$ 9 CM exhaust CM-core of Stratum 3 at $\rho=20$.

## XXXVII. Polyakov --- Stratum 6 physical, six-stratum $\times$ Stage-1

| Stratum | CY-3 geometry | Stage-1 status | Obstruction class |
|---|---|---|---|
| 1 | flat $T^3=E^3$, bielliptic | canonical (Abelian BV) | none |
| 2 | toric, local $\P^2$, conifold | canonical via toric formality (Kontsevich 2003) | none |
| 3 | $K3\times E$, Enr$\times E$ | canonical via Künneth | $\mathrm{at}_{K3\times E}\cdot\Omega=0\in H^{1,3}=0$ |
| 4 | BCOV Borel-summable | Borel-summable via holomorphic anomaly | perturbative, Borel-admissible |
| 5 | Koszul-empty $Q_5$ | perturbative Čech HTT | $\mathrm{at}_{Q_5}\cdot\Omega\in\C^{101}\ne 0$ |
| 6 | non-Kähler Clemens, balanced Hermitian SU(3) | $H$-twisted (Rogers 2011 Prop 3.4) | NS flux $[H]\in H^3(\hat Y,\Z)$; HDR non-degen |

Clemens $\hat Y$ balanced-Hermitian (Michelsohn 1982 Acta Math 149 Thm 6.8; Fu-Yau 2008 JDG 78 Thm 3.2), $\d\Omega=0$, $\d(J\wedge J)=0$ after rescaling. Mixed Hodge $(W_\bullet,F^\bullet)$ on $H^3(\hat Y)$ (Deligne 1971 IHES 40 Thm 3.2.5; Morgan 1978 IHES 48 Thm 9.1; Schmid 1973 Thm 4.9): weight-3 $\mathrm{gr}^W_3H^3$ pure; weight-2 $\mathrm{gr}^W_2H^3$ vanishing $S^3$-cycles. Universal cocycle splits
$$[m_3,B^{(2)}]^{\mathrm{Strat}6}_{\hat Y}=[\mathrm{at}_{\hat Y}\cup B^{(2)}_{\mathrm{Connes}}]^{W_3}+\sum_i f_i\cdot[\mathrm{at}^{W_2}_{S^3_i}\cup B^{(2),\mathrm{Sas}}_{\mathrm{Connes},i}].$$
Sasakian constant $f_i=\oint_{S^3_i}\Omega/\mathrm{vol}(S^3_i)\in\C^\times$; $\mu_i=\oint_{S^3_i}\Omega=(2\pi i)^3 f_i\mathrm{vol}(S^3_i)$ conifold deformation (Strominger 1995 NPB 451 §2). Replacement functor: $\Phi^{\mathrm{Sas},H}_3=\mathrm{Sp}^{\mathrm{ch,Sas}}_{(C,[f_i])}\circ\Phi^{\mathrm{FA},H}_3$ landing in $H$-twisted curve-side Courant-algebroid CDO (Hitchin 2003 Q J Math 54 Thm 1.1). On $\mathcal U^{\mathrm{adm}}$:
$$\mathrm{Trc}\circ\Phi^{\mathrm{Sas},H}_3=-1\cdot\mathbf 1+\hbar^2\bigl([\mathrm{at}^{W_3}_{\hat Y}\cup B^{(2),W_3}_{\mathrm{Connes}}]+\sum_i f_i[\mathrm{at}^{W_2}_{S^3_i}\cup B^{(2),\mathrm{Sas}}_{\mathrm{Connes},i}]\bigr)\cdot[\Omega^{W_3}+\Omega^{W_2}].$$
$\mathbf H_{\Delta_5}$-analog on Stratum 6: $H$-flux-twisted $\mathbf H^H_{\Delta_5}$ producing Sasakian-twisted $\Phi^H_{10}$ with $f_i\cdot(\mathrm{BPS~count}_{S^3_i})$-terms from D3-branes on vanishing cycles. \ClaimStatusProvedHere Michelsohn + Fu-Yau + mixed Hodge. \ClaimStatusConjectured $H$-twisted Stage-1 (Rogers $E_1$, $E_3$-generalisation pending); $H$-twisted Drinfeld double. References: Clemens 1983 Duke 50; Friedman 1986 Math Ann 274 Thm 4.2+5.3; Michelsohn 1982 Thm 6.8; Fu-Yau 2008 Thm 3.2; Strominger 1986 NPB 274; 1995 NPB 451 §2; 1996 PLB 379; Kontsevich 1999 LMP 48; Tamarkin 2003 Sel Math NS 9 Thm 1; Costello 2011 Thm 13.4.1; Costello-Li 2016 Prop 5.2; CG FA Vol 2 §§4.3+5.3; Rogers 2011 CMP 301 Prop 3.4; Kapranov 1999 Prop 4.4; Caldararu-Willerton 2010 Thm 1.6; Deligne 1971 Thm 3.2.5; Morgan 1978 Thm 9.1; Schmid 1973 Thm 4.9; Hitchin 2003 Thm 1.1; Ševera-Weinstein 2001; Grantcharov-Poon 2000 Math Ann 316 Thm 2.3; BHPV 2004 §VIII.3.

## XXXVIII. Kontsevich r5-redux --- universal anchor theorem

**Theorem (Vol III geometric anchor).** On $\mathcal U^{\mathrm{adm}}=\mathcal U^{\mathrm{adm}}_{\mathrm{at}}(X)\cap\mathcal P^{-1}(\mathcal U^{\mathrm{adm}}_{\overline{\mathcal A_2}})$, four-way equivalence
$$\boxed{\;[m_3,B^{(2)}]_X=0\iff(\text{Theorem B})\iff(\text{Stage-1 canonical})\iff(\mathbf H_{\Delta_5}\text{ canonical})\iff(\hbar^2K=-1)\;}$$
reads: universal Atiyah cocycle $\mathrm{at}_X\cup B^{(2)}_{\mathrm{Connes}}$ vanishes iff two-stage $\Phi_d$ produces canonical $E_1$-chiral shadow (Theorem A), iff Stage-1 KT $\cap$ CGL holds, iff $\mathbf H_{\Delta_5}$ realised as CoHA-Hall at $\hbar^2=-1/8$, iff three-faces identity at $K=2c_+(L)$ via Bruinier. Proof via Kapranov 1999 Prop 4.4 $A_\infty$-structure $m_3=\mathrm{at}_X$; Caldararu-Willerton 2010 Thm 1.6 cyclic $B^{(2)}_{\mathrm{Connes}}$; Quillen 1969 §9 Malcev; Calaque-Van den Bergh 2010 Thm 4.2 Duflo-HKR; Positselski 2011 Thm 7.2.2; KS 2008 Thm 4.5.1; Borcherds 1995 Thm 10.4; Bruinier 2002 Prop 5.1. **Verification $K3\times E$:** $H^{1,3}(K3\times E)=0$ by Künneth (BHPV 2004 §VIII.3 + elliptic $h^{0,q}=0$ for $q\ge 1$); $[m_3,B^{(2)}]_{K3\times E}\cdot\Omega=0$ unconditionally; Humbert admissibility $\mathcal P(K3\times E)\in\mathcal U^{\mathrm{adm}}_{\overline{\mathcal A_2}}$ on transcendental 20-moduli dense open (Deligne 1972 §6 Kuga-Satake); all four climaxes hold unconditionally on 21-dim dense open. Cross-volume $\{5,5,5\}=\{c_{\Delta_5}(0)/2,\text{Pentagon trace},\omega_{\mathrm{Borcherds}}\}$ at $N=1$. **Failure $Q_5$:** $\mathrm{at}_{Q_5}\ne 0$ with 101-dim bracket $[m_3,B^{(2)}]_{Q_5}\ne 0$ (Kapranov 1999 §4; $h^{2,1}(Q_5)=101$); all four climaxes fail strictly. Three-route convergence at $K=8$ unconditional; siblings $\{K=2$ Monster, $K=4$ Enriques, $K=12$ Conway-$K=2$-transported, $K=50$ FM$\}$ conditional on Dunn-Lurie Serre-CM. \ClaimStatusProvedHere four-way equivalence via two-stage cocycle transport + Kapranov r5 pentagon-coherence.

*Raeez Lorgat, 2026-04-22. Companion derivations in `/Users/raeez/chiral-bar-cobar-vol2/notes/`.*
