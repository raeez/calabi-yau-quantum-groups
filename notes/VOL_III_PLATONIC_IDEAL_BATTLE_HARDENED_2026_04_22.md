# Volume III: CY Categories, Quantum Groups, and BPS Algebras — Platonic Ideal

*Raeez Lorgat, Perimeter Institute.*

---

## I. Two-stage factorisation

$$\boxed{\;\Phi_d=\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}\circ\Phi^{\mathrm{FA}}_d\colon\mathrm{CY}_d^{\mathrm{cat}}\to\mathrm{Alg}_{E_1^{\mathrm{ch}}}(C)\text{ in }\mathrm{PresStCat}_\infty,\text{ factoring through }\mathrm{Fact}^{\mathrm{hol}}_{E_d}(X).\;}$$

$$\begin{array}{ccc}\mathrm{CY}_d^{\mathrm{cat}}&\xrightarrow{\;\Phi^{\mathrm{FA}}_d\;}&\mathrm{Fact}^{\mathrm{hol}}_{E_d}(X)\\ \big\downarrow\,{\scriptstyle\mathrm{Shad}_\bullet}&&\big\downarrow\,{\scriptstyle\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}}\\ \mathrm{Alg}_{E_1^{\mathrm{ch}}}(C)&\xleftarrow[\;\Omega^{\mathrm{ch}}_C\;]{B^{\mathrm{ch}}_C}&\mathrm{CoAlg}^{\mathrm{fact}}_{E_1^{\mathrm{ch}}}(C)\end{array}$$

Diagonal $\mathrm{Shad}_\bullet=\Phi_d$. $\mathrm{CY}_d^{\mathrm{cat}}\subset\mathrm{PresStCat}_\infty$: proper smooth $\mathbb C$-linear stable with $\mathbb S_{\mathcal T}\simeq[d]$ (Bondal 1990; Kuznetsov 2004; BBDJS 2015). Dunn forbids $E_d=E_1$ for $d>1$; passage factors through $E_d$-holomorphic. Stage 1: KT $E_d$-formality (Willwacher 2014 Thm 1.2 $H^0(\mathsf{GC}_2)=\mathfrak{grt}_1$) $\cap$ CGL $(0,d)$-locality (Costello-Li 2016 Prop 5.2). Stage 2: $\int_{\Sigma_{d-1}}$ + restriction (Ayala-Francis 2015 Thm 3.16). Family-of-shadows $\mathrm{Shad}_X\colon\mathrm{CycCurve}(X)\to\mathrm{Alg}_{E_1^{\mathrm{ch}}}(\mathrm{SmCurve})$. At $d=5$ FM on $(K3\times K3\times E)/\Z_2$ via PTVV; Borcherds 1998 §14 gives $\Phi_{12}|_{\mathrm{II}_{2,2}}=\Phi_{10}=\Delta_5^2$ as $d=3$ shadow.

**Stage-1 canonicity scope.** $\Phi^{\mathrm{FA}}_d$ is canonical up to contractible choice (Drinfeld associator $\cap$ gauge-fixing $\cap$ RG-propagator, each contractible in its $(\infty,1)$-category) on the *formal locus* $\mathcal U^{\mathrm{adm}}_{\mathrm{at}}(X)$ where $\mathrm{HH}^\bullet(\mathcal C)$ is formal as an $E_d$-algebra: always at $d=1$ (Kontsevich 1999); generically at $d=2$ since $\Omega^3_{K3}=0$ kills the Kuranishi cubic obstruction; on $K3\times E$ at $d=3$ since $\mathrm{At}(T_E)=0$ (elliptic curve is complex Lie group); generally *non*-formal on compact CY-3 with $\mathrm{At}(T_X)\ne 0$ (quintic). Category-level $E_d$-formality of $\mathrm{HH}^\bullet(\mathcal C)$ is proved at $d\le 3$ via three-vanishing; open at $d\ge 4$. (Operad-level $E_d$-formality is Fresse Vol I Thm 14.1.A unconditional, distinct from category-level.)

**Native level dispatch.** PTVV 2013 $(2-d)$-shifted symplectic structure on $\mathcal M(\mathcal C)$ + Dunn-Lurie additivity forces
$$
d=1\Rightarrow n=\infty \text{ (lattice VOA)},\qquad d=2\Rightarrow n=2\text{ (Mukai-Heisenberg)},\qquad d\ge 3\Rightarrow n=1\text{ (CoHA/Yangian/BKM)}.
$$
Schouten-Nijenhuis vanishing at $d\ge 3$ is a concurrent fact, not the driver.

**Uniqueness on the Koszul-self-dual locus.** On $\mathcal C_d^{\mathrm{Kosz}}\subset\mathrm{CY}_d\text{-Cat}^{\mathrm{cyclic,prop}}$ the four universal properties
(U1) Hochschild pullback $B^{\mathrm{ord}}(\Phi(\mathcal C))\simeq CC_\bullet(\mathcal C)$, (U2) CY-morphism functoriality (wall-crossing $\to$ R-matrix gauge), (U3) Drinfeld-centre compatibility $Z(\mathrm{Rep}^{E_1}(\Phi(\mathcal C)))\simeq\mathrm{Rep}^{E_2}(\Phi(\mathcal C))^{\mathrm{centered}}$ for $d\ge 3$, (U4) standard-input recovery (Coh(E) $\to$ lattice VOA at $d=1$; $D^b(K3)\to E_2$-Mukai-Heisenberg at $d=2$; $\mathrm{CoHA}(\C^3)\to Y^+(\widehat{\mathfrak{gl}}_1)$ at $d=3$) characterise $\Phi$ up to natural isomorphism. Off the Koszul-self-dual locus, the central-charge-twisted $\widetilde\Phi_3(\mathcal C):=\Phi_3(\mathcal C)\otimes\varepsilon$ satisfies (U1, U3, U4) but differs from $\Phi_3$; uniqueness then requires Fourier-Mukai kernel rigidification (U5).

## I-bis. $\Phi_3$ on $T^3$

$\Phi_3(T^3)=\mathcal H_3\vert_E=\mathrm{Heis}_{\chi(\mathcal O_{T^3})\cdot c_+(\mathrm{II}_{3,3})}=\mathrm{Heis}_0$ degenerate. Triviality verifies abelian CY-3 baseline. Three-faces degenerate: $K^\kappa(T^3)=0$ aligns with $\mathsf G$-row ceiling.

## II. Shifted symplectic hierarchy

Calaque-Pantev-Toën-Vaquié-Vezzosi $(2-d)$-shifted structure:

| $d$ | shift | BV $E_n$ | output |
|---|---|---|---|
| $1$ | $+1$ | $E_0$ | lattice VOA |
| $2$ | $0$ | $E_1$ | Mukai-Heisenberg |
| $3$ | $-1$ | $E_2$ | CoHA / Yangian / BKM |
| $4$ | $-2$ | $E_3$ | HK CY4 (Kapranov wt-2) |
| $5$ | $-3$ | $E_4$-Poisson | FM on $(K3\times K3\times E)/\Z_2$ |

## III. Three incarnations at $d=3$

(i) **CoHA Hall** (Kontsevich-Soibelman 2008): $\mathrm{CoHA}(\C^3)=H^*_T(\mathrm{Rep}_n(Q_3,W_3),\phi_{W_3})$ with Jordan triple quiver $Q_3$ (one vertex, loops $X,Y,Z$), potential $W_3=\mathrm{tr}(X[Y,Z])$, Jacobi $J(Q_3,W_3)=\mathbb C[X,Y,Z]=\mathcal O_{\C^3}$ via cyclic derivatives. Schiffmann-Vasserot 2013 shuffle isomorphism $\mathrm{CoHA}(\C^3)\otimes_\mathbb F\mathbb F((z))\cong\mathrm{Sh}$ with kernel
$$
\omega(z,w)=\frac{(z-w-\varepsilon_1)(z-w-\varepsilon_2)(z-w-\varepsilon_3)}{(z-w)^3}
$$
and CY-3 slice $\varepsilon_1+\varepsilon_2+\varepsilon_3=0$.

(ii) **6D holomorphic Chern-Simons** on $X=CY_3$ with Lie algebra $\mathfrak g$ and holomorphic volume $\Omega_X\in H^{3,0}(X)$: fields $\mathcal A=c+A_{0,1}+A^*_{0,2}+c^*_{0,3}\in\Omega^{0,\bullet}(X,\mathfrak g)[1]$; action
$$
S_{\mathrm{cl}}=\int_X\Omega_X\wedge\langle\mathcal A,\bar\partial\mathcal A+\tfrac{1}{3}[\mathcal A,\mathcal A]\rangle,
$$
$(-1)$-shifted symplectic via Serre duality. Quantum observables $\mathrm{Obs}_{\mathrm{hCS}}(\C^3)=(\mathrm{Sym}(\mathcal E^\vee[1])[[\hbar]],Q+\hbar\Delta)$ with Bochner-Martinelli propagator
$$
P_{\mathrm{BM}}(z,w)=\frac{2}{(2\pi i)^3}\sum_{k=1}^3(-1)^{k-1}(\bar z_k-\bar w_k)\|z-w\|^{-6}\widehat{d\bar z_k}\wedge dw_1\wedge dw_2\wedge dw_3.
$$
Coefficient $(d-1)!/(2\pi i)^d$ at $d=3$ verifies $2/(2\pi i)^3$. $E_3$-structure on $\mathrm{Ch}(\mathrm{Dolb})$ via sum-over-shuffles; $\mathrm{Obs}_{\mathrm{hCS}}(\C^3)\simeq\mathrm{CE}^\bullet_{\bar\partial,\mathrm{chir}}(\mathcal E_{\mathrm{hCS}},\mathcal O_{\C^3})$. Associativity via Čech-Dolbeault Mayer-Vietoris on $\overline{\mathrm{Conf}}_n(\C^3)$; coherent $E_3$-commutativity via $\pi_1(\mathrm{Conf}_2(\C^3))=\pi_1(S^5)=0$ (binary level only; higher arities governed by little-disk operad, $H_*(E_3)=\mathrm{Pois}_3$ with bracket of degree $-2$).

*One-loop anomaly* on $X=CY_d$ is controlled by a degree-$(d+1)$ invariant polynomial. At $d=3$ this is *quartic* Casimir, schematically $\int_X\mathrm{Tr}_{\mathrm{ad}}(A(F_A)^3)$; the cubic Casimir $d^{abc}$ vanishes by adjoint self-duality (AP113 anomaly/wave-function distinction). *Wave-function renormalisation* (distinct): $S^{(1)}_{\mathrm{c.t.}}=-\hbar C_2(\mathfrak g)(4\pi)^{-3}\log(L/\varepsilon)\int\Omega\wedge\mathrm{Tr}(A\bar\partial A)$; $\mathrm{SU}(N)$ coefficient $N/(32\pi^3)$.

*Deformation moduli:* $\mathrm{Def}(\mathrm{Obs}_{\mathrm{hCS}})=\mathrm{HH}^*_{E_3}(\mathrm{Obs},\mathrm{Obs})[3]$; on flat $\C^3$ with simple $\mathfrak g$, $T_0\mathcal M=H^{0,3}_{\bar\partial,c}(\C^3)\otimes\mathrm{Sym}^2(\mathfrak g^\vee)^{\mathrm{inv}}=\C\cdot\mathrm{Kil}$ matches $Y_{\varepsilon_1,\varepsilon_2,\varepsilon_3}$ Yangian modulo CY slice.

*Minimal $L_\infty$-model:* on flat $\C^3$, $\ell_n^{\min}=0$ for all $n\ge 3$ (Kontsevich-Soibelman homotopy transfer); on compact CY-3, $\mathrm{At}(TX)\in H^1(X,\Omega^1\otimes\mathrm{End}(TX))$ is the formality obstruction; on $K3\times E$, $\mathrm{At}(T_E)=0$ and $\Omega^3_{K3}=0$ kill Kuranishi cubic, formality holds.

*$E_3$-Koszul self-duality:* $\mathcal D_3^!\simeq\mathrm{Lie}[2]$ (Fresse 2017 Vol I Thm 14.1.A). Strict (Gwilliam-Williams 2021) vs homotopy (Francis-Gaitsgory 2012) Koszul compatible via Fresse Thm 12.3.A + Positselski coderived-contraderived transfer. Non-abelian 3-dualisability fails on flat $\C^3$ (HH$^*$ infinite-dim per Gwilliam-Williams 2021 Prop 5.3.2); recovers on compact CY-3.

(iii) **Gluing (Chapter 26, this Vol).** The $E_1$-chiral shadow $\mathcal A^{\mathrm{sh}}_{X,\Sigma_2,C}$ assembles from local 6d hCS quantisation by $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_2,C}$-pushforward over $\Sigma_2$ and restriction to $C$.

## IV. Four routes to $\mathbf H_{\Delta_5}$

**Route A (Wick):** Borcherds lift of $\phi_{0,1}\in J_{0,1}^{\mathrm{K3}}$ (Eichler-Zagier 1985 Thm 9.1, $c_{\phi_{0,1}}(0,0)=20$) via singular theta correspondence (Borcherds 1998 §14) produces $\Delta_5\in M_5(\mathrm{Sp}_4(\Z))$ holomorphic Siegel cusp weight 5 on paramodular Siegel space $\mathcal H_{3,2}$. Wick-contracting $\phi_{0,1}$ OPE weights yield $\kappa_{\mathrm{BKM}}=5$.

**Route B (Gram):** Cartan signature $(+4,+4,-2)=(2,1)$ at rank 3 hyperbolic; Weyl vector $\rho=f_2-\tfrac12 f_3+f_{-2}$; $c_+(\mathrm{II}_{2,1})=2$. $K=2c_+(\mathrm{II}_{2,1})+4=8$. Extension to super-rank with Borcherds super-Serre adjunction of odd imaginary simple roots produces $\mathfrak g_{\Delta_5}$ (GKM with $2+1+\infty$ Cartan and infinitely many odd real imaginary simple roots via $m(a)=-\tfrac{1}{64}f(n,\ell,m)$).

**Route C (Gerstenhaber):** $d=3$ CPTVV shift $-1$ + Dunn-Lurie $E_2$ + Serre-CM of Kuga-Satake gives $\hbar$-twist $\hbar^2=-1/8$, $K=8$, $\hbar^2 K^{\kappa_{\mathrm{ch}}}=-1$. $K=2c_+(L)$ with $L=\mathrm{II}_{2,2}$ for Mukai-enhanced K3 at $d=3$ via fibration over $E$.

**Route D (Borcherds log-derivative):** $Z_{\mathrm{hCS}}^{(1)}[K3\times E]=\log(\Phi_{10}/\eta^{24}(\tau)\eta^{24}(\tau'))$ one-loop via CGP 2018 K3$\times$E instanton. Log-derivative pulls out weight-10 leading coefficient at singular cusp $\Phi_{10}=\Delta_5^2$ (Igusa 1964 Amer J 86 Thm 3).

**Four-route convergence** at $\mathbf H_{\Delta_5}$ for $K3\times E$ CHL siblings $N\in\{1,2,3,4,6\}$: Routes A, B, C, D return same Hall-Drinfeld double construction up to explicit gauge equivalence (witness Monster $V^\natural$ $(K,\hbar^2)=(2,-1/2)$; K3 $(8,-1/8)$; Fake Monster $(50,-1/50)$; Enriques $(4,-1/4)$). **Six routes to $G(K3\times E)$** — Borcherds lift, Mukai pairing, McKay quiver, Maulik-Okounkov instanton lift, factorisation homology via 6D hCS Stage-2, Costello 5d hCS uplift — converge to naturally isomorphic $\Phi_3(D^b(K3\times E))$-outputs; six isomorphisms form a common limit cone in $\mathrm{ChirAlg}^{E_1}_C$. This convergence is *literal* for $K3\times E$ CHL siblings; it is *not* literal for Monster vs Igusa, which are distinct CY-3 inputs, not sibling specialisations.

**Conway boundary** $(2,-1/2)$ is Monster-transported via Duncan 2007 super-twin sign character; routes A, B undefined on positive-definite $\Lambda_{24}$ (no Lorentzian time, no cusp); routes C, D return $+$-sign. Conway is the structural boundary of the $\hbar^2 K=-1$ identity: non-vacuity control.

**Enriques** $K=4$ canonical via three routes: Allcock 2000 J reine angew Math 518 Thm 1 $\Phi_4^{\mathrm{Enr}}$ weight 4 = GN 1997 Duke 87 Prop 2.1 quasi-pullback of $\Phi_{12}$ along $\mathrm{II}_{2,10}\hookrightarrow\mathrm{II}_{2,26}$; Mukai $\Lambda^{\mathrm{Enr}}_{\mathrm{Muk}}=U\oplus U\oplus E_8(-1)$ rank 12 sig $(2,10)$ has $c_+=2$; orbifold halving (Persson-Volpato 2011 Prop 4.1) halves K3 $\chi(\mathcal O)=2$ to Enriques $\chi(\mathcal O)=1$; $\kappa_{\mathrm{BKM}}(\mathrm{Enr}\times E)=4$. Mukai-Kondo $M_{12}\hookrightarrow M_{24}$ (Kondo 1998 Duke 92 Thm 2.1; Mukai 1988 Invent 94 Thm 0.3).

**Fake Monster rank obstruction from compact CY-3:** $\mathrm{rank}(\Lambda_{\mathrm{Leech}})=24$; for any K3-fibered CY-3 $X$, $h^{1,1}(X)\le h^{1,1}(\text{K3 fibre})+2h^{0,2}(\text{K3 fibre})\le 20+2=22<24$. No transverse surface $\Sigma_2$ in a compact CY-3 supplies Niemeier data of rank 24. Fake Monster is thus a $d=5$ cousin (via Dunn-Lurie $E_5\simeq E_2\otimes E_2\otimes E_1$ on $\mathrm{II}_{25,1}$), obstructed at $d=3$.

## IV-bis. Incarnation 7 rigour

Dijkgraaf-Verlinde-Verlinde 1997 $Z^{K3\times T^2}_{\mathcal N=4,D=4}(p,q,y)=1/\Phi_{10}(p,q,y)$ exact BPS-sector identity; 24 $=\chi(K3) = $ 24 $I_1$ nodal fibres $=$ F-theory 24 7-branes $=12\cdot 2=24$ twisted M5 (CGP 2018); leading saddle via Borcherds 1998 + EZ 1985 + Göttsche 1990. Stage-2 $E$-pushforward of $\Phi^{\mathrm{FA}}_3(K3\times E)$ realised: $\mathrm{Trc}\circ\Phi_3(K3\times E)=-1\cdot\mathbf 1+\hbar^2\cdot[m_3,B^{(2)}]\cdot[\Omega]$, with the universal cocycle vanishing on $K3\times E$ via $H^{1,3}(K3\times E)=0$ (Künneth from K3 $h^{1,q\ne 1}=0$ and elliptic $h^{0,q\ge 1}=0$).

One-loop $Z_{\mathrm{hCS}}$ proved here; all-orders conjectural pending T-CL-K3 + T-AllLoop; full off-shell 3D gravity heuristic. MW 2009 is a category error and not DVV.

## V. $\Psi$ four-sibling

$$\boxed{\;\{\Psi,\Psi^{\mathrm{deg}},\Psi^{\mathrm{tor}},\Psi^{\mathrm{metap}}\}:\mathrm{CY}^{\mathrm{Siegel\text{-}aut}}_2\to\mathrm{QHopf}^{\mathrm{BKM}}\;}$$

Jointly surjective onto GN-reflective sig-$(2,n\ge 3)$ on Koszul locus; $24A_1$-Niemeier sig-$(2,24)$ outside. S17+DMS21+S06.

| Sibling | $N$ | Ramification | Weight | $\Phi_N$ | Cover | 3D-QG |
|---|---|---|---|---|---|---|
| $\Psi$ | $1$ | unramified | $5$ | $\Delta_5$ | $\mathrm{Sp}_4$ | $1/\Phi_{10}$ DVV |
| $\Psi^{\mathrm{tor}}$ | $\{2,3,4,6\}$ | torsion CHL | prog $(4,3,2,1)$ / twined $(2,1,1,1)$ | twined $\Phi_N$ | paramod | $1/\Phi_N$ |
| $\Psi^{\mathrm{metap}}$ | $5,7$ | half/quarter-int | $(1/2,1/4)$ | $\Phi_5^{(1/2)},\Phi_7^{(1/4)}$ | $\mathrm{Mp}_4,\widetilde{\mathrm{Mp}}_4$ | CHL |
| $\Psi^{\mathrm{deg}}$ | $8$ | weight-$0$ | $0$ | $\Phi_8^{(0)}$ | diag-divisor | degenerate |

Cover assignment derived from Weil representation via Stone-von Neumann at signature $(2,3)$: integer weight $\to\mathrm{Sp}_4(\Z)$; half-integer $\to\mathrm{Mp}_4(\Z)$; quarter-integer $\to\widetilde{\mathrm{Mp}}_4(\Z)$ (Scheithauer 2015); weight-zero $\to$ degenerate terminal fibre. 22 non-Leech Niemeier Chenevier-residual frontier.

## VI. Canonical CY$_d$ $\kappa_\bullet$

Five $\kappa$-subscripts: $\{\kappa_{\mathrm{ch}},\kappa_{\mathrm{cat}},\kappa_{\mathrm{BKM}},\kappa_{\mathrm{fiber}},\kappa_{\mathrm{ch,BV}}\}$; ratio $\varrho=\kappa_{\mathrm{ch}}/c$. Tier I (CY intrinsics): $\kappa_{\mathrm{cat}}(X)=\chi(\mathcal O_X)$; Mukai; $(-d)$-shifted symplectic. Tier II (Stage-1 output): $\kappa_{\mathrm{fiber}}$. Tier III (Stage-2 output): $\kappa_{\mathrm{BKM}}$; Niemeier-twist; Humbert; CHL twined. $\kappa_{\mathrm{ch,BV}}$ is Costello-Li BCOV one-loop curving at BRST $c=-2$ (Polyakov ghost supertrace, Atiyah-dilaton cocycle $\alpha_{\mathrm{BCOV}}=(\chi_{\mathrm{top}}/24)\cdot\mathrm{tr}\,\mathrm{At}(T_X)\in H^1(X,\mathcal O_X)$); for non-compact $X_{\mathrm{con}}$ the mechanism is boundary-link $\zeta$-regularisation on Sasaki-Einstein $T^{1,1}\simeq S^2\times S^3$ (Klebanov-Witten hep-th/9807080) with $c=-2$ $\beta\gamma$-ghost system (Kausch hep-th/9510149 Eq. (4.12)).

**$\kappa_{\mathrm{ch}}$ Hodge supertrace stratification.** $\kappa_{\mathrm{ch}}(A_X)=\sum_q(-1)^q h^{0,q}(X)$:

- $d=1$ elliptic: $\kappa_{\mathrm{ch}}=0$ (Hodge diamond $1-1$)
- $d=2$ K3: $2$; abelian surface: $0$; bielliptic: $0$
- $d=3$ *any* compact CY-3: $\kappa_{\mathrm{ch}}=0$ by Serre duality $h^{0,q}=h^{d,d-q}$ at odd $d$ (quintic, $K3\times E$, $E^3$, octic-double all 0)
- $d=3$ local $\mathbb P^2$: $3/2$; regularised conifold: $1$
- $d=4$ sextic: $2$; octic-double: $151$; $K3^{[2]}$: $3$; F(Y): $3$
- $d=5$ all compact: $0$ (Serre at odd $d$)

**Canonical conifold row:** $(\kappa_{\mathrm{ch}},\kappa_{\mathrm{cat}},\kappa_{\mathrm{BKM}},\kappa_{\mathrm{ch,BV}})(X_{\mathrm{con}})=(+1,0,+1,-1)$ with Polyakov ghost-mode balance $\kappa_{\mathrm{ch}}+\kappa_{\mathrm{ch,BV}}=\kappa_{\mathrm{cat}}$ on $\mathsf G$-class free-field CY-3 with $\chi_{\mathrm{top}}=2$ (not universal). Local $\P^2$ row $(3/2,0,3/2,-3/2)$ via lens-space $S^5/\Z_3$ boundary link.

**CY-2 and CY-3 values.** $\kappa_{\mathrm{cat}}(K3)=2$, $\mathrm{Enr}=1$, $T^4=0$. $\kappa_{\mathrm{cat}}(K3\times E)=0$; $\P^3=1$; quintic $0$; $T^3=0$. $K3\times E$ spectrum $\{0,3,5,24\}$ arises from four distinct constructions (Künneth total space; chiral Heisenberg-Mukai specialisation; Borcherds weight via $\Delta_5$; Mukai lattice rank of K3), not one $\Phi$-functor applied four times.

Manin-corrected Mukai signature: $\widetilde H(K3,\Z)\cong\mathrm{II}_{4,20}$ signature $(4,20)=(1,1)_{H^0+H^4}\oplus(2,0)_{(H^{2,0}+H^{0,2})_\R}\oplus(1,19)_{H^{1,1}_\R}$; Kuga-Satake $\dim A_{\mathrm{KS}}(T)=2^{n-2}$ for signature $(2,n-2)$; K3 super-Yangian $Y^{K3}=Y_{\mathfrak{osp}(4|20)}=Y(\mathfrak{gl}(4|20))^\theta$ Chevalley-fixed on $V=\C^{4|20}$.

## VII. $\kappa_{\mathrm{BKM}}$ readings

$\kappa_{\mathrm{BKM}}(\Delta_5)=5$ K3 half-BPS; $\kappa_{\mathrm{BKM}}(\Phi_{10})=10$; $\kappa_{\mathrm{BKM}}(\Phi_{12})=12$. Universal $\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2$ (Borcherds 1995 Thm 10.4). Four distinct Jacobi inputs at $N\in\{1,2,3,4,6\}$ and their eight-row Gritsenko-Cléry extension:

- **Programme (Gritsenko).** Hodge-elliptic $\mathrm{Aut}(E)$-orbifold; $c_N(0)=(10,8,6,4,2)$, weights $(5,4,3,2,1)$. Gritsenko 1999 Math Nachr 199 Thm 6.1 canonical. CHL ladder per Gritsenko-Nikulin 1995 Pt II Thm 2.1.
- **Singly-twined $M_{23}$.** $\phi^{(g_N)}_{0,1}=\tfrac12 Z^{(g_N)}_{K3}$; $c_N(0)=(10,4,2,2,2)$, weights $(5,2,1,1,1)$. CHP 2014 Table 4.
- **Physical CHL.** $N\in\{1,2,3,5,7,11\}$, $k_N=24/(N+1)-2$. Jatkar-Sen 2005; David-Jatkar-Sen 2006.
- **Borcherds eight-form.** $N\in\{1,\ldots,8\}$, weights $(5,2,1,1,1/2,1,1/4,0)$, covers $\mathrm{Sp}_4/\mathrm{Sp}_4/\mathrm{Sp}_4/\mathrm{Sp}_4/\mathrm{Mp}_4/\mathrm{Sp}_4/\widetilde{\mathrm{Mp}}_4/\mathrm{deg}$. Cléry-Gritsenko 2013.

Square-doubling $\Phi_{10}=\Delta_5^2$ at $N=1$ only (Igusa 1964 + GN 1995). Programme-canonical ladder is Stage-2 $\Phi_3$-canonical on $K3\times E$. Vol I uses 12 (FM); Vol III uses 5 (K3); the difference reflects the target lattice, not a convention clash.

The additive split $\kappa_{\mathrm{BKM}}=\kappa_{\mathrm{ch}}+\chi(\mathcal O_{\mathrm{fiber}})$ is **false at every $N$**. At $N=1$: $\kappa_{\mathrm{ch}}(K3\times E)=0$ (Kunneth Hodge supertrace + Serre at odd $d$), $\chi(\mathcal O_{K3})=2$, RHS $=2\ne 5=\kappa_{\mathrm{BKM}}$. At $N\ge 2$: 62 adversarial-test witnesses confirm failure.

**Cross-volume bridge at value level.** The Vol I conductor and Vol III Borcherds weight satisfy, on K3-fibered CHL Class A at $N\in\{1,2,3,4,6\}$:
$$
\boxed{\;K(A_{X_N})=c_N(0)=2\kappa_{\mathrm{BKM}}(\Phi_N)\quad\text{with values }\{10,4,2,2,2\}.\;}
$$
Mediator is $K$ (Vol I BRST-ghost conductor), not $\kappa_{\mathrm{ch}}$ (which vanishes at $d=3$ odd by Serre). Factor 2 derivable: (a) bar-cobar total grading $\deg(B)+\deg(\Omega)=2$; (b) $\mathrm{Sp}_4(\Z)\backslash\mathcal H_2$ two-cusp divisor pair each contributing Borcherds weight once. At $N=1$, four independent paths converge at $10$: Vol I BRST-ghost anomaly of $\Phi_3(K3\times E)$; $2\kappa_{\mathrm{BKM}}(\Phi_1)$ via Gritsenko 1999 Thm 1.2; Pentagon trace on Vol II Heptagon face 4 / Dimofte slab; $\zeta$-regularised analytic trace via Dabholkar-Harvey BPS counting on $K3\times T^2$, $\mathcal N=4,D=4$ supermultiplicity.

## VIII. CoHA-to-$\mathcal W_\infty$

$\mathrm{CoHA}(\C^3)=Y^+(\widehat{\mathfrak{gl}}_1)$ (SV 2013 IHES 118 Thm 1.1); $D(Y^+)=Y(\widehat{\mathfrak{gl}}_1)$ with structure function $\varphi(u)=(u+\varepsilon_1)(u+\varepsilon_2)(u+\varepsilon_3)/u^3$ (Tsymbaliuk 2017 arXiv:1703.04551 Thm 1.1). $\mathrm{CoHA}(\C^3)\ne\mathcal W_{1+\infty}$; $\mathcal W_{1+\infty}[\lambda]=\mathrm{ev}_\lambda$-evaluation image of $Y(\widehat{\mathfrak{gl}}_1)$ via state-field correspondence on the vacuum module (Gaiotto-Rapčák 2017 arXiv:1703.00982). Miki $\Z/3$-symmetry. Five descent lines.

**Two $\lambda$-parameters distinguished:** (i) $\lambda_{\mathrm{Tr}}=(\varepsilon_1+\varepsilon_2)/\varepsilon_3$ is the SV/Tsymbaliuk truncation parameter, defined *before* the CY-3 constraint; under $\varepsilon_1+\varepsilon_2+\varepsilon_3=0$ one has $\lambda_{\mathrm{Tr}}=-1$ identically. (ii) $\lambda_W$ is the Gaiotto-Rapčák $\mathcal W_{1+\infty}[\lambda_W]$ central-charge parameter, free. The $\mathcal W_{1+\infty}$-family does not collapse under the CY-3 constraint; the physical slice parameter is $\lambda_{\mathrm{GR}}$, not $\lambda_{\mathrm{Tr}}$.

**Conifold.** $\mathrm{CoHA}(Q_{\mathrm{con}},W_{\mathrm{con}})\simeq Y^+(\widehat{\mathfrak{gl}}(1|1))^{\mathrm{con}}$ as $\Z_2$-graded associative bialgebra in super-vector spaces over $\C((\hbar))$ (not a Hopf algebra; antipode only on Drinfeld double $D(Y^+)=Y(\widehat{\mathfrak{gl}}(1|1))^{\mathrm{con}}$). Five independent routes (Klebanov-Witten super-shuffle, two-chart Čech, Van den Bergh tilting, Kulish-Sklyanin RTT, 5D hCS chiral VOA) converge at structure constant $c^{\mathrm{KW}}_{(1,1)}=(\varepsilon_1\varepsilon_2)^{-1}$ (Li-Yamazaki arXiv:2003.08909 §8.3.6.3). Ungraded shadow $Y^+(\widehat{\mathfrak{gl}}(1|1))^{\mathrm{con}}\twoheadrightarrow Y^+(\widehat{\mathfrak{sl}}_2)^{\mathrm{con}}$ is surjection with kernel generated by the central $K_0$ + Heisenberg ideal $\C h^{\mathrm{tr}}[t,t^{-1}]$ of the supertrace current. Negut conifold bond $\varphi^{0\Rightarrow 1}(u)=(u+h_1)(u+h_2)/[u(u+h_1+h_2)]$ arXiv:1512.06473 eq. (1.6) + Li-Yamazaki eq. (8.125).

## IX. Five structural identities

**SI-1** $\mathrm{hCS}\dashv\mathrm{BKM}$ on $\mathcal U^{\mathrm{adm}}$; Stage-1 unit Costello-Li 2016; Stage-2 counit Borcherds singular theta.

**SI-2** Master $L$-value: $\log Z^{(1)}_{\mathbf H^\Psi_L}=-\log\Delta_L-\kappa_{\mathrm{BGS}}(L)L'(0,\Delta_L,\mathrm{std})+\log C_L$. K3/Monster/FM $\kappa_{\mathrm{BGS}}=24$; Enriques 12.

**SI-3** Unified three-faces: $\hbar_r^2 K_r=-1$, $K_r=2c_+(L_r)$.

**SI-4** $8\times 5$ Bistrata; diagonal witnesses ceiling; $\mathsf B$-row $K^\kappa=8$ inscribed via Bruinier Heegner Chern-class reciprocity on Mukai-enhanced K3 Heisenberg.

**SI-5** $\mathrm{MGSL}\simeq\mathfrak h_{\mathrm{BKM}}\times\mathfrak{grt}_1^{\mathrm{KS}}$. Brown 2011 unconditional $\le 12$.

## X. Open frontier

(1) K3 Yangian past genus 1. (2) Drinfeld-Jimbo BKM Yangians $\mathfrak g_{\Delta_5}$. (3) CY-C general. (4) CY-4 $\Phi_4$. (5) Chenevier non-reduced at 22 non-Leech Niemeier. (6) Bridgeland $\dim\mathrm{Stab}(K3\times E)=48$. (7) Fake Monster $\Psi$-image at $d=5$. (8) Non-CHL $N=7$. (9) $\Phi_4$ framework. (10) $\kappa_{\mathrm{BKM}}$ Fake-Monster row. (11) $\phi^{(n\ge 25)}$. (12) $e_{k\ge 4}$. (13) $\mathrm{GRT}_1$-transitivity. (14) PBW $\mathfrak u_{\zeta_8}$: $8^{129}$. (15) Yetter-Drinfeld $\delta^{(n\ge 7)}$. (16) Category-level $E_d$-formality $d\ge 4$. (17) Stage-1 chain-level $d\ge 4$. (18) Bracket-level identification $\mathfrak g_{\mathrm{BPS}}\cong\mathfrak g_{\Delta_5}$ on $K3\times E$ (graded-dim unconditional via Oberdieck-Pixton reduced DT $Z^{\mathrm{red}}_{DT}=-1/\Phi_{10}=-\Delta_5^{-2}$; bracket open).

## XI. Canonical fixings

$\Delta_{E_6}$ weight 16 via $f_{16}=E_4\Delta$. Chenevier $D^{\mathrm{Chen}}\equiv$ Taylor-Wiles $S^{\mathrm{ps}}$ reduced. 7 Niemeier $\Psi$-interior; 22 exterior. $\Lambda_{\mathrm{Muk}}(K3)=\mathrm{II}_{4,20}$ rank 24; FM no compact CY host (rank bound 22). $\Phi_{10}=\Delta_5^2$ (Saito-Kurokawa rescale factor 4 via Siegel-weight doubling × Andrianov convention, elliptic source $g=\Delta\cdot E_6\in S_{18}$). Four Yangian types distinguished: classical; dg-shifted; chiral on curves; spectral on Ran.

**Canonical anomaly locus.** $\mathrm{Anom}_1=0\iff\mathfrak g\in(\mathrm{Deligne}^{\mathrm{exc}}\setminus\{E_6,A_2\text{-unrefined}\})\cup\{\text{abelian}\}\cup\{\mathrm{str}_{\mathrm{ad}}=0\}\cup\{K^{-1/2}\text{-refined}\}$. Deligne quartic is killed by the quartic-Casimir mechanism; $A_2$-refined Feigin-Frenkel + Dimofte cures; $E_6$ $\mathrm{Sym}^3(\mathbf{27})$ strict. Conway $V^{s\natural}$ $c=12$ super-twin. $(c_{4d},c_{2d})(A_1,\Sigma_{0,24})=(107/6,-214)$ with $-214=-12\cdot c_{4d}-1$ (rescale correction); $(n_v,n_h)=(63,88)$; $c_3=-8$; $-22032=176256/(-8)$. Umbral $(N-1)\mid 24$; $\zeta(3,3,3,3)\approx 0.000296$; Leech root 2. $\Phi_{12}$ home $\mathcal D_{\mathrm{II}_{26,2}}$. $\mathrm{ChirHoch}^3$ pairing $2\mathrm{Vol}(E)(2\pi i)^3$. $8^{129}=\dim\mathfrak b^{\mathrm{re},+}_{\zeta_8}$.

## XII. Scope discipline

Chain-level and $(\infty,1)$-categorical have equal status (Pattern 269; Vol I $\leftrightarrows$ Vol II $\leftrightarrows$ Vol III). Koszul admissible locus
$$
\mathcal U^{\mathrm{adm}}=\overline{\mathcal A_2}\setminus\bigcup_{n\equiv 0,3\bmod 4}H_n.
$$
Two distinct Koszul loci coexist: Atiyah $\mathcal U^{\mathrm{adm}}_{\mathrm{at}}\subset X$ (vanishing of $\mathrm{At}(T_X)\cup B^{(2)}_{\mathrm{Connes}}$) vs Humbert $U^{\mathrm{adm}}\subset\overline{\mathcal A_2}$ (Eichler-Zagier codim-1 theta divisors).

## XIII. Cross-volume bridges

- **Vol II $\rightleftarrows$ Stage-1.** Vol II 6d hCS on $\R^3\times K3\times\C^2$ IS Stage-1 $\Phi^{\mathrm{FA}}_3(K3\times E)$ after $E_6\to E_3$ Dolbeault reduction.
- **Vol I $\rightleftarrows$ Stage-2.** Vol I $E_1$-chiral shadow on $E$ IS Stage-2 pushforward $\mathrm{Sp}^{\mathrm{ch}}_{K3,E}\circ\Phi^{\mathrm{FA}}_3(K3\times E)$.
- **Cross-volume anchor (AP5).** Vol I cites weight 12 (Fake Monster $\Phi_{12}$ on $\mathrm{II}_{26,2}$); Vol III cites weight 5 (K3 $\Delta_5$ on $\mathrm{II}_{2,2}$); the discrepancy is target-lattice dependent, not convention-clash.

## XIV. Ledger

$c_{\phi_{-2,1}}(-n)=0$, $c_{\phi_{0,1}^{K3}}(-1)=2$, $c(0)=20$. Theta prefactor $1/2!$; 3-loop $\chi(K3)^3/3!=2304$. $e_k\in\mathrm{zv}^{\mathrm{sv}}_{3k}$. Arnold / PSL$_2$ / Totaro-Kriz. $Z^{K3}_{3\mathrm{dQG}}=1/\Phi_{10}$ DVV. $\Phi_{10}/(\eta(\tau)^{24}\eta(\tau')^{24})$ weight $(-12,-12)$. $\C^n\to E_{2n}$ classically; $E_n$ after $\bar\partial$ Dolbeault reduction. Wheel-$\zeta$ basepoint. K3 MHS. Ayala-Francis 2015 smooth vs Ayala-Francis-Tanaka 2017 stratified. Non-compact Costello-Gwilliam Vol 2 Prop 8.2.1. CHSW $\mathrm{SU}(3)$; CY-4 BBS/SVW. Quartic Casimir Deligne-killed; cubic $d^{abc}$ live on $A_2,E_6$; $E_6$ strict. Conway $\Psi^{\mathrm{metap}}$ $c=12$. Three ladders (§VII). $\kappa_{\mathrm{BKM}}$ denominator-named. Four Yangian types. $\Phi_d$ two-stage. Three-tier $\kappa_\bullet$ hierarchy. $f_{16}=E_4\Delta$ weight 16. $\Phi_{10}=\Delta_5^2$. Monster/K3/FM/Enriques four-witness inscribed; Conway structural boundary, $(K,\hbar^2)=(2,-1/2)$ Monster-transported via Duncan super-twin. $\kappa_{\mathrm{cat}}(K3\times E)=0$ Künneth.

## XV. One-sentence summary

Vol III establishes $\Phi_d=\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}\circ\Phi^{\mathrm{FA}}_d$ as $(\infty,1)$-functor $\mathrm{CY}_d^{\mathrm{cat}}\to\mathrm{Alg}_{E_1^{\mathrm{ch}}}(C)$ canonical on the formal Koszul-self-dual locus; crystallises $\mathbf H_{\Delta_5}$ under $\hbar^2 K=-1$, $K=2c_+(L)$; four-sibling $\Psi=\{\Psi,\Psi^{\mathrm{tor}},\Psi^{\mathrm{metap}},\Psi^{\mathrm{deg}}\}$ jointly surjective on GN-reflective sig-$(2,n\ge 3)$; CY$_d$ stratified $\{\kappa_{\mathrm{cat}},\kappa_{\mathrm{ch}},\kappa_{\mathrm{fiber}},\kappa_{\mathrm{BKM}}\}$; cross-volume value-level $K=2\kappa_{\mathrm{BKM}}=c_N(0)$ on K3-fibered CHL Class A.

## XVI. Attack-heal closure

Humbert split ($\equiv 3,5\bmod 8$ vs $\equiv 0,3\bmod 4$); $\mathcal W_N$ five-witness $+\{\mathcal W_3,\mathrm{BP}\}$; Vol III 0/21 pairwise distinct from Vol II heptagon; both $\eta^{24}(\tau)\eta^{24}(\tau')$, Igusa 1964 bimodular $(-2,-2)$; Stage-1 canonical on $\mathcal U^{\mathrm{adm}}$ only.

## XVII. Local-global five cycles

| Cycle | Local | Global |
|---|---|---|
| (i) Averaging | $\mathrm{av}^{\mathrm{loc}}_n$ per-disc | $\mathrm{hocolim}_n\mathrm{av}^{\mathrm{loc}}_n$ |
| (ii) Five thms | $T^3$: $\mathcal H_3\vert_E$ chain | $\Phi_d$ $(\infty,1)$-functor |
| (iii) $r(z)$ 7 faces | $r^{\mathrm{Sieg,dyn}}$ | $\mathrm{GRT}_1(\Q)$-torsor (Scope I chain-level strict; Scope II cohomology-class via Brown 2012 motivic Galois) |
| (iv) Family-shadows | per-$(\Sigma,C)$ | $\mathrm{Shad}_X$ over $\mathrm{CycCurve}(X)$ |
| (v) Chenevier/MGSL | per-prime $\bar\rho_\ell$ | $D^{\mathrm{Chen}}$; MGSL |

$\psi_{\Delta_{10}}=\phi_{\Delta_{E_6}}\boxtimes\mathrm{Sym}^1$; $\lambda_p(\Delta_{10})=a_p(\Delta_{E_6})+p^8+p^9$ unconditional $p\le 199$. Padovan $d_n=d_{n-2}+d_{n-3}$.

**Chenevier at $p=691$.** At the Kummer-Bernoulli irregular prime $p=691$ ($B_{12}=-691/2730\equiv 0\bmod 691$), shadow-tower Galois representation at level $r=11$ has
$$
\det\rho_{S_{11}(V_1(\mathfrak g)),\,691}=\chi_{\mathrm{cyc}}^{11}\cdot\varepsilon_{B_{12}}\pmod{691}
$$
via Kubota-Leopoldt $p$-adic $L$-function + Herbrand-Ribet. $\mathrm{GRT}_1(\Q)$ transport $F_2\to F_3$ explicit as Drinfeld associator: $R(z)=1+\hbar\Phi_{\mathrm{KZ}}(z/\hbar,\Omega)$.

## XVIII. Climax — $\mathbf H_{\Delta_5}$ terminal

$$\boxed{\;\mathbf H_{\Delta_5}=\mathcal D_\hbar(\mathcal Y^{\mathrm{Hall}}_\hbar(\mathrm{CoHA}_{\mathrm{K3}\times E}),\widetilde\Phi^{\mathrm{Sieg\text{-}Bor}}_{\mathrm{Sp}_4}[\Phi_{10}/\eta^{24}],R_{\mathrm{Sieg,dyn}})\quad\text{at}\quad\hbar^2=-1/8.\;}$$

Stage-1 canonical up to contractible choice on $\mathcal U^{\mathrm{adm}}$ via KT formality $\cap$ CGL locality. Stage-2 via Ayala-Francis 2015 Thm 3.16 along elliptic pencil + restriction to $E$. Künneth $\mathrm{CoHA}(\mathrm{K3}\times E)=\mathrm{CoHA}(\mathrm{K3})\boxtimes_{E_{\mathrm{Hall}}}\mathrm{CoHA}(E)$ with Mukai rank-24 grading; Drinfeld-doubling yields BKM-superalgebra Hopf, rank-3 Cartan $\mathrm{diag}(4,4,-2)$; associator via Borcherds singular theta from $\Phi_{10}/\eta^{24}$, canonical since $\Phi_{10}=\Delta_5^2$ is the unique holomorphic weight-10 Siegel cusp (Igusa 1964). Canonical by construction-1 (super-EK) via Etingof-Kazhdan 2000 + GN 1998.

## XIX. Factorisation algebra rigour layer

| Cycle | Content |
|---|---|
| FA-III.1 | Stage-1 $\Phi^{\mathrm{FA}}_d$ as $E_d$-holomorphic FA; KT formality $\cap$ CGL $(0,d)$-locality |
| FA-III.2 | Stage-2 factorisation-homology $\int_{\Sigma_{d-1}}$; AF 2015 smooth vs AFT 2017 stratified |
| FA-III.3 | BV on compact CY-3: Costello 2011 Thm 13.4.1 direct; CG Vol 2 Thm 8.6.9 non-compact |
| FA-III.4 | Dolbeault $E_{2d}\to E_d$ via $H^{0,\bullet}$ |
| FA-III.5 | CY-$d$ formality on $\mathcal U^{\mathrm{adm}}$ via Atiyah-class vanishing |
| FA-III.6 | $\mathrm{Shad}_X$ as $(\infty,1)$-functor; K3 Picard $\rho$: $(\rho-1)$-dim image |

## XX. $\mathrm{Ran}(X)$ precision

$\mathrm{Ran}(X)=\mathrm{colim}_S X^S$ (Francis-Gaitsgory 2012 Def 1.2.3). Stage-1 on $\mathrm{Ran}(X)$; Stage-2 $\int_{\Sigma_{d-1}}$ pushes to $\mathrm{Ran}(C)$.

## XXI. $\mathsf{SC}^{\mathrm{ch,top}}$ at $d=3$

Stage-1 = closed colour; Stage-2 = open colour via Dolbeault-topologisation. Directional $(\mathsf{top}\to\mathsf{cl})=\varnothing$.

## XXII. Terminal re-statement

(a) Canonicity by construction-1, not equivalence class. (b) Two distinct Koszul loci: Atiyah $\mathcal U^{\mathrm{adm}}_{\mathrm{at}}\subset X$ vs Humbert $U^{\mathrm{adm}}\subset\overline{\mathcal A_2}$. (c) Non-surjectivity: $24A_1$-Niemeier sig-$(2,24)$ outside $\mathrm{im}(\mathrm{Shad}_\bullet)$.

## XXIII. Kapranov: Hopf at all arities

**Theorem.** $\mathrm{Hopf}_n\colon\mathrm{FM}_4(n)\twoheadrightarrow\mathrm{FM}_2(n)$ stratified $T^{n-1}$-phase bundle, total dim $4n-5$, base $2n-3$, fibre $(S^2)^{\times(n-1)}$; $\{\mathrm{Hopf}_n\}_{n\ge 2}$ assembles into $(\infty,1)$-operad morphism $\mathrm{Hopf}_\bullet\colon\mathrm{FM}_4\to\mathrm{FM}_2$, coherent with two-stage factorisation. Stasheff $K_{n+1}$ $C_n$ vertices indexes pentagon-coherence. Proof by induction: base $n=2$ Hopf fibration $S^3\to S^1$ (Hopf 1931 Math Ann 104 §4); at arity $n+1$, codim-1 strata $\partial_T\mathrm{FM}_2(n+1)\cong\mathrm{FM}_2(k)\times\mathrm{FM}_2(n+2-k)$, $C_n$ Catalan (Stasheff 1963 Trans AMS 108 §2; Loday 2004); Künneth-independent closure via $\mathrm{Hopf}_k\times\mathrm{Hopf}_{n+2-k}$; Stage-1 $E_d$-formality (Kontsevich-Tamarkin 2018) + CGL locality + Francis-Gaitsgory 2012 Thm 5.5 functoriality preserve pentagon; Lurie HA.5.5.3.12 homotopy-coherent extension. Pentagon $K_4$: $C_3=5$; $K_5$: $C_4=14$; $K_6$: $C_5=42$. On K3 ($d=2$): Mukai rank-24 preserved stratum-by-stratum; Pentagon-trace $c_N(0)/2=5$ at $N=1$ propagates. On CY-3: proved on Strata 1-4 unconditional; Stratum 5 ($Q_5$) Čech-HTT conditional; Stratum 6 outside scope.

## XXIV. Bondal-Kuznetsov

**Cubic 4-fold Kuznetsov.** $\mathcal A_Y\simeq D^b(\mathrm K3_Y)$ on Hassett $\mathcal C_d$. **Relative HPD over $E$:** $K^\kappa=8$ constant. **Stab:** $\dim\mathrm{Stab}(K3\times E)=48$, codim 22. **Bondal-Orlov:** fails on $\omega_X\simeq\mathcal O$; $\mathrm{Shad}_X$ non-surjective. **BKR McKay:** CY-C constructed on $\C^3$, K3-fibered; general open.

**Hostless BKM.** $\mathrm{BKM}^{\mathrm{hostless}}\colon\mathrm{JacPair}^{\mathrm{sw}}_0\to\mathrm{BKM}_{\mathrm{Borch}}$, $(L,\phi_L)\mapsto\mathrm{sing\text{-}}\theta_L[\phi_L]$ (Borcherds 1998 §14); $\mathrm{mult}(\alpha)=c_L(\alpha^2/2)$. Source: even $L$ + singular-weight $\phi_L$ (Borcherds 1995 Thm 10.4; Gritsenko 1999 Thm 6.1). Target: BKM with WKB denominator. Triangle commutes on inside-$\mathrm{Shad}$ rows ($\mathrm{Shad}_\bullet=\mathrm{BKM}^{\mathrm{hostless}}\circ\mathrm{H}^\bullet_{\mathrm{Muk}}$); 28 outside-$\mathrm{Shad}$ rows (24$A_1$-Niemeier + 22 non-Leech + 2 hyperbolic + FM) reached directly.

## XXV. $\Phi_3$-canonicity beyond $K3\times E$

**Toric CY-3** ($\C^3$, local $\P^2$, conifold): $\mathrm{at}_X=0$ via $T_X$-splitting + Čech vanishing (Cox-Little-Schenck 2011 Thm 8.1.6; Danilov 1978 §10); $\mathcal U^{\mathrm{canonical}}_{\Phi_3}=\mathcal M_{\mathrm{cx}}$, codim-0 vacuous Humbert; $\dim_\C\le 1$. Stage-2 shadow class $\mathsf G$ with $\kappa_{\mathrm{ch}}\in\{1,3/2,1\}$; no Mukai enhancement.

**Abelian $T^6=E^3$.** $T_{T^6}=\bigoplus_i\pi_i^*T_{E_{\tau_i}}=\bigoplus\mathcal O$, $\mathrm{at}_{T^6}=0$ (Silverman 1986 Ch III Prop 1.5); 9-dim moduli; Humbert on $\overline{\mathcal A_3}$ at $n\equiv 1\bmod 4$ (van der Geer 1988 §IV.2.3); $\mathcal U^{\mathrm{canonical}}_{\Phi_3}(T^6)$ dense open $\dim_\C=9$; CM branches $E_{\zeta_3}^3,E_i^3$ excluded. Stage-2 $\mathcal H_3$ on $E$, $\kappa_{\mathrm{ch}}=3$, three-faces degenerate.

**Schoen K3-fibered** (Schoen 1988 Math Z 197): $\mathrm{at}_X=\mathrm{at}_{X/\P^1}+\pi^*\mathrm{at}_{\P^1}$; $\mathrm{at}_{\P^1}=0$, $\mathrm{at}_{X/\P^1}$ concentrates on 24-point Kodaira $I_1$ divisor $\Delta_{24}\subset\P^1$ via Griffiths transversality; on $\P^1\setminus\Delta_{24}$ fibration smooth, $\mathrm{at}_X=0$. $\dim_\C\mathcal M_{\mathrm{cx}}(X)=122$ ($h^{2,1}=101+20+1$); $\mathcal U^{\mathrm{canonical}}_{\Phi_3}$ dense open $\dim_\C=120$. Stage-2 shadow inherits Mukai rank-24; $K=8$ persists; $K3\times E$ embeds as 21-dim trivial-fibration limit (codim 99).

**Hilbert-scheme Borcea-Voisin** $Y^{\mathrm{Beau}}=\mathrm{Hilb}^2(K3)/\sigma$ (Fogarty 1968 Thm 2.9; Beauville 1983 JDG 18 §II.4): $\dim_\C=22$; Nikulin 1979 classifies 76 $\sigma$-types, 4 admissible ($k\in\{10,14,17,19\}$) with $\mathrm{at}=0$; Mukai restricts to $\mathrm{II}^{\mathrm{inv}}_{(2,k)}$, $K^\kappa=2c_+(\mathrm{II}^{\mathrm{inv}}_{(2,k)})=2+k/2\in\{7,9,21/2,23/2\}$.

**Net union.** $\dim_\C\mathcal U^{\mathrm{net}}_{\Phi_3}=\max_X\dim_\C\mathcal U^{\mathrm{canonical}}_{\Phi_3}(X)=120$ (Schoen). $K3\times E$ 21-dim is the minimal non-degenerate Mukai-enhanced stratum; Schoen 120-dim is the maximal with $K=8$ persistent; Borcea-Voisin 22-dim hosts sub-ceiling $K=23/2$.

**Atiyah-Koszul on $K3\times E$.** $\mathrm{at}_{K3\times E}=\pi_1^*\mathrm{at}_{K3}+\pi_2^*\mathrm{at}_E=0$ via DGMS 1975 Thm 2.1 + Costello-Li 2016 Prop 5.2; $\mathcal U^{\mathrm{adm}}_{\mathrm{at}}(K3\times E)=\mathcal M_{\mathrm{cx}}(K3\times E)$, 21-dim. Humbert-Koszul: $U^{\mathrm{adm}}=\overline{\mathcal A_2}\setminus\bigcup_{n\equiv 3,5\bmod 8}H_n$ (EZ 1985 Thm 3.4); Kuga-Satake $\mathcal P$ via Morrison 1984 Thm 6.3 + Shioda-Inose 1977 Thm 6.3 + Nikulin 1980. Intersection $\mathcal U^{\mathrm{canonical}}_{\Phi_3}(K3\times E)=\mathcal P^{-1}(U^{\mathrm{adm}})$ dense open. Witness $(K3^{\mathrm{gen}}_{\rho=2},E_\tau)$ transcendental. CM witnesses $(K3^{\mathrm{gen}}_{\rho=2},E_{\zeta_3})$ and $(K3^{\mathrm{gen}}_{\rho=2},E_i)$ fail: land on $H_3\cup H_{13}$, $H_5\cup H_{13}$. $\dim_\C=20+1=21$.

## XXVI. Conway resolution

$(K,\hbar^2)=(2,-1/2)$ is Monster-transported via Duncan 2007 Duke 139 Thm 1 super-twin diamond; $(12,-1/12)$ retracted as pattern-match with $c_{V^{s\natural}}=12$, not $K=2c_+$. Routes A (Wick) and B (Borcherds log-derivative) undefined on positive-definite $\Lambda_{24}$ (no Lorentzian time, no cusp); Routes C (Gram signature), D (Gerstenhaber shift $d=12$ even) return $+$, not $-$. Canonical reading: $(2,-1/2)$-inherited-from-Monster on $\Psi^{\mathrm{metap}}$-branch (Scheithauer 2008 Example 7.3); structurally out of scope of $\hbar^2 K^{\kappa_{\mathrm{ch}}}=-1$. Conway sits in §V landscape as $\Psi^{\mathrm{metap}}$-image weight $-12+1/2$. No Hall-Drinfeld-double avatar analogous to $\mathbf H_{\Delta_5}$ at $(8,-1/8)$.

## XXVII. $36$-cell sibling $\times$ Heegner

Four Siegel covers over $\mathcal A_2$ correspond to four quotients of $\mathrm{End}(A^{\mathrm{KS}}_{d_K})\otimes\Q=\mathrm{Mat}_4(\Q(\sqrt{d_K}))$: standard; degenerate; toroidal; metaplectic. Nine class-number-one imaginary quadratic fields (Baker-Heegner-Stark): $\Q(\sqrt{-n})$ at $n\in\{1,2,3,7,11,19,43,67,163\}$, $d_K\in\{-3,-4,-7,-8,-11,-19,-43,-67,-163\}$. Nine singular K3 surfaces $X_{d_K}$ at $\rho=20$: $T(X_{d_K})$ unique positive-definite binary form of disc $|d_K|$ (Shioda-Mitani 1974 Thm 4.3); Shioda-Inose cover to $A_{d_K}=E_{\tau_{d_K}}\times E_{\tau_{d_K}}$ (Shioda-Inose 1977; Morrison 1984 Thm 6.3). Kuga-Satake $A^{\mathrm{KS}}_{d_K}\sim E_{\tau_{d_K}}^{\otimes 4}$ with $\mathrm{End}\otimes\Q=\Q(\sqrt{d_K})$.

Singular weight per sibling: $w^\bullet_{d_K}\in\{5-2/|d_K|,\;5/2-1/|d_K|,\;10-4/|d_K|,\;6-2/|d_K|\}$ for std/deg/tor/metap (Bruinier 2002 Prop 5.1); $\kappa^\bullet_{\mathrm{BKM}}(d_K)=2w^\bullet_{d_K}$. Hopf
$\mathbf H_{\Psi^\bullet_{d_K}}=\mathcal D_\hbar(\mathcal Y^{\mathrm{Hall}}(\mathrm{CoHA}_{X_{d_K}\times E}),\widetilde\Psi^\bullet_{d_K},R^{\mathrm{Sieg,dyn}}_{d_K,\bullet})$ at $\hbar^2_{d_K}=-|d_K|/(10|d_K|-4)$.

| $d_K$ | $j(\tau_{d_K})$ | $T(X_{d_K})$ Gram | $K_{d_K}^{\mathrm{std}}$ | $\hbar^2_{d_K}$ |
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

9-point arithmetic-core fibre of $\Psi=\Psi_1$, not a new sibling. Mumford-Tate cover $\times$ Kuga-Satake CM $=4\times 9=36$ arithmetic cells. $\mathrm{Shad}_{X_{d_K}}$ has image dim $\ge 19$ on each $X_{d_K}$. $K_{d_K}=10-4/|d_K|$ arithmetic sub-ceiling (non-integral except $d_K\in\{-1,-2,-4\}$) distinct from the generic $K=8$.

## XXVIII. Six-stratum CY-3 partition

$\mathrm{CY}_3^{\mathrm{cat}}=\bigsqcup_{i=1}^{6}\mathcal S_i$:

1. flat $T^3=E^3$, bielliptic ($\mathrm{at}_X=0$; class $\mathsf G$ abelian)
2. toric, local $\P^2$, conifold ($\mathrm{at}_X=0$; class $\mathsf G$; Stage-1 canonical via toric formality, Kontsevich 2003)
3. $K3\times E$, Enriques$\times E$ ($\mathrm{at}_X\cdot\Omega=0\in H^{1,3}=0$; Stage-1 canonical via Künneth)
4. BCOV Borel-summable compact non-formal (Gepner rational sub-stratum; perturbative admissible, non-perturbative conjectural)
5. Koszul-empty $Q_5$ (Kähler $\partial\bar\partial$-satisfying; $\mathrm{at}_{Q_5}\cdot\Omega\in\C^{101}\ne 0$; perturbative Čech HTT only)
6. strictly $\partial\bar\partial$-failing Clemens-type (non-Kähler balanced Hermitian $\mathrm{SU}(3)$; NS flux $[H]\in H^3(\hat Y,\Z)$; HDR $E_1$-non-degenerating)

Hyperkähler $d=3$ empty (Calabi 1958; Beauville 1983 JDG 18 Thm 2); abelian-orbifold $\subset\mathcal S_1$; Gepner $\subset\mathcal S_4$ as $C_2$-cofinite; conifold transitions are phase transitions across moduli components. Moishezon $\partial\bar\partial$-satisfying stays in $\mathcal S_5$ (DGMS 1975 Thm 5.22); strictly $\partial\bar\partial$-failing defines $\mathcal S_6$.

**Clemens witness $\tilde Y\to Q_5^{\mathrm{sing},p_0}$** at $p_0=[1\!:\!1\!:\!1\!:\!1\!:\!1]$. Dwork pencil $f_\psi=\sum x_i^5-5\psi\,x_0x_1x_2x_3x_4$ at $\psi=1$ nodal point; local model $\{w_1w_2-w_3w_4=0\}$ (Clemens 1983 §2 Prop 2.1). Small resolution $\pi\colon\tilde Y\to Q_5^{\mathrm{sing},p_0}$ blows down vanishing $S^3$-cycle, replaces with $\mathbf S\subset\tilde Y$ with $[\mathbf S]\ne 0\in H_3(\tilde Y,\Z)$; $K_{\tilde Y}=\mathcal O$ categorical CY-3, not Kähler, strictly $\partial\bar\partial$-failing (Werner 1987 Thm 4.1; Friedman 1986 Prop 3.4). Cohomology: generic $Q_5^\psi$ has $h^{1,1}=1,h^{2,1}=101,b_3=204$; at $\tilde Y$: $b_3\colon 204\to 206$, $h^{1,1}\colon 1\to 0$. $(1,1)$-form witness: $\alpha=\pi^*\omega_{Q_5^\psi}+\epsilon\partial\bar\partial\log|s_{\mathbf S}|^2$ satisfies $d\alpha=0$ and $\int_{\mathbf S}\alpha=-4\pi i\epsilon\ne 0$ via Poincaré-Lelong + $[\mathbf S]\cdot[\mathbf S]=-2$, while $\int_{\mathbf S}\partial\bar\partial f=0$ by Stokes; contradiction. Frölicher $E_1$-non-degeneration: $d_1\colon E_1^{0,2}\to E_1^{1,2}$, $d_1[\tilde\alpha]=[\alpha]\ne 0$ (Friedman 1986 Thm 5.10). Stage-1 KT-formality obstruction: $[\mathrm{at}_{\tilde Y}\cup\mathrm{at}_{\tilde Y}]\cdot\Omega_{\tilde Y}\ne 0\in H^{2,3}(\tilde Y)$. Physical: Costello 2011 Thm 13.4.1 finiteness fails; Costello-Li 2016 Prop 5.2 flat-$\C^3$ parametrix cannot glue; non-perturbative sectors contribute $e^{-\mathrm{Area}(\mathbf S)/\hbar}$ (Candelas-Green-Hübsch 1990; Strominger 1995). $\mathcal S_6$ is the unique stratum where $\Phi_3$ fails at Stage 1.

**Stratum-6 replacement functor.** Clemens $\hat Y$ is balanced-Hermitian (Michelsohn 1982 Thm 6.8; Fu-Yau 2008 JDG 78 Thm 3.2), $d\Omega=0$, $d(J\wedge J)=0$ after rescaling. Mixed Hodge $(W_\bullet,F^\bullet)$ on $H^3(\hat Y)$ (Deligne 1971; Morgan 1978; Schmid 1973): weight-3 $\mathrm{gr}^W_3H^3$ pure; weight-2 $\mathrm{gr}^W_2H^3$ vanishing $S^3$-cycles. Universal cocycle splits
$$
[m_3,B^{(2)}]^{\mathrm{Strat}6}_{\hat Y}=[\mathrm{at}_{\hat Y}\cup B^{(2)}_{\mathrm{Connes}}]^{W_3}+\sum_i f_i\cdot[\mathrm{at}^{W_2}_{S^3_i}\cup B^{(2),\mathrm{Sas}}_{\mathrm{Connes},i}],
$$
Sasakian constant $f_i=\oint_{S^3_i}\Omega/\mathrm{vol}(S^3_i)\in\C^\times$; $\mu_i=\oint_{S^3_i}\Omega=(2\pi i)^3 f_i\mathrm{vol}(S^3_i)$ conifold deformation (Strominger 1995 NPB 451 §2). Replacement functor $\Phi^{\mathrm{Sas},H}_3=\mathrm{Sp}^{\mathrm{ch,Sas}}_{(C,[f_i])}\circ\Phi^{\mathrm{FA},H}_3$ lands in $H$-twisted curve-side Courant-algebroid CDO (Hitchin 2003 Q J Math 54 Thm 1.1). $\mathbf H_{\Delta_5}$-analog: $H$-flux-twisted $\mathbf H^H_{\Delta_5}$ producing Sasakian-twisted $\Phi^H_{10}$ with $f_i\cdot(\mathrm{BPS~count}_{S^3_i})$-terms from D3-branes on vanishing cycles.

## XXIX. Gauge-anomaly locus and all-orders CFG

CFG all-orders dual blocker $Z_{\mathrm{hCS}}=(\Phi_{10}/\eta^{48})^{\hbar c_{K3}}$ splits into T-CL-K3-Extension $\times$ T-AllLoop.

**T-CL-K3** close to proved: four named pillars (Costello-Li 2016 Prop 5.2 flat-$\C^3$ parametrix $P^{(j)}_{\mathrm{CL}}=1/(w_j-w'_j)^2$; Gilkey 1995 §1.7 Thm 1.7.6 heat-kernel; Yau 1978 Ricci-flat K3; AS 1963 / BGV 2004 Thm 4.1 Getzler), Kuranishi-chart gluing with $a_0(K3)=\chi(\mathcal O)=2$, $a_1=0$ (Yau Ricci-flat, Gilkey 1.7.4b), $a_k(K3)=0$ for $k\ge 2$ (hyperkähler $\mathrm{Sp}(1)\subset\mathrm{SU}(2)$ + BGV 2004 on $c_2(K3)=24$).

**T-AllLoop** depends on T-CL + BV-exponentiation lemma: $\log Z^{\mathrm{eff}}_{\mathrm{hCS}}=\sum_n\hbar^n S_n$ with $S_1=\log(\Phi_{10}/\eta^{48})c_{K3}$ (CGP 2018); claim $S_n=a_k(K3)\cdot c_{K3}$-polynomial for $n\ge 2$ modulo lemma identifying $n$-loop Stage-1 effective action with Gilkey $a_k$-multiple; $a_k(K3)=0$ forces $S_{n\ge 2}=0$. T-CL closure turns Stage-1 $\Phi^{\mathrm{FA}}_3(K3\times E)$ Borel-summable-conditional into parametrix-existence-admissible unconditional on K3-flat-twist + 21-dim $\mathcal U^{\mathrm{canonical}}_{\Phi_3}(K3\times E)$. T-AllLoop closure promotes all-orders $1/\Phi_{10}$ from 2-loop-proved to unconditional.

## XXX. Drinfeld six-row closure

Stage-2 $E_1$-chiral shadow $\mathcal A^{\mathrm{sh}}_{X,\Sigma_{d-1},C}$ has OPE pole depth $r_{\max}\in\{1,2,3,4,\infty\}$ corresponding to $\mathsf G/\mathsf L/\mathsf C/\mathsf M/\mathsf M^{\mathrm{ext}}$; $\mathsf M$ split by DS-nilpotent. Sixth archetype $\mathsf B$: CY-enhancement via Mukai rank-24 grading on K3 with $K^\kappa=8$. DS-nilpotent past $\mathfrak{sl}_3$ opens dense rational $K^\kappa$-spectrum inside $\mathsf M$ via hook/rectangular KRW 2003 Thm 6.1 with $\varrho_{\mathrm{rect}}(k,n/k)=(n/k)(H_k-1)$. Exotic CY: toric on $\mathcal U^{\mathrm{adm}}_{\mathrm{at}}$ reduces to $\mathsf G/\mathsf L/\mathsf C/\mathsf M$; CY-auto into $\mathsf B$-row sub-families (Monster $K=2$, FM $K=50$, Conway structural boundary); compact non-formal quintic Stage-1 conditional. $G_2/\mathrm{Spin}(7)$ outside CGL-locality hypothesis. 22 non-Leech Niemeier outside Vol III image. No seventh archetype. $\mathsf B$-row sub-family refinements (Monster, K3, Fake Monster, Enriques, CM-K3 $K_{d_K}=10-4/|d_K|$) stay inside $\mathsf B$.

## XXXI. Kontsevich universal anchor

**Theorem.** On $\mathcal U^{\mathrm{adm}}=\mathcal U^{\mathrm{adm}}_{\mathrm{at}}(X)\cap\mathcal P^{-1}(\mathcal U^{\mathrm{adm}}_{\overline{\mathcal A_2}})$, four-way equivalence
$$
\boxed{\;[m_3,B^{(2)}]_X=0\iff(\text{Theorem B})\iff(\text{Stage-1 canonical})\iff(\mathbf H_{\Delta_5}\text{ canonical})\iff(\hbar^2K=-1).\;}
$$
Universal Atiyah cocycle $\mathrm{at}_X\cup B^{(2)}_{\mathrm{Connes}}$ vanishes iff two-stage $\Phi_d$ produces canonical $E_1$-chiral shadow (Theorem A), iff Stage-1 KT $\cap$ CGL holds, iff $\mathbf H_{\Delta_5}$ realised as CoHA-Hall at $\hbar^2=-1/8$, iff three-faces identity at $K=2c_+(L)$ via Bruinier.

Proof via Kapranov 1999 Prop 4.4 $A_\infty$-structure $m_3=\mathrm{at}_X$; Caldararu-Willerton 2010 Thm 1.6 cyclic $B^{(2)}_{\mathrm{Connes}}$; Quillen 1969 §9 Malcev; Calaque-Van den Bergh 2010 Thm 4.2 Duflo-HKR; Positselski 2011 Thm 7.2.2; Kontsevich-Soibelman 2008 Thm 4.5.1; Borcherds 1995 Thm 10.4; Bruinier 2002 Prop 5.1.

**Verification on $K3\times E$.** $H^{1,3}(K3\times E)=0$ by Künneth (BHPV 2004 §VIII.3 + elliptic $h^{0,q}=0$ for $q\ge 1$); $[m_3,B^{(2)}]_{K3\times E}\cdot\Omega=0$ unconditionally; Humbert admissibility $\mathcal P(K3\times E)\in\mathcal U^{\mathrm{adm}}_{\overline{\mathcal A_2}}$ on transcendental 20-moduli dense open (Deligne 1972 §6 Kuga-Satake); all four climaxes hold unconditionally on 21-dim dense open. Cross-volume $\{5,5,5\}=\{c_{\Delta_5}(0)/2,\,\text{Pentagon trace},\,\omega_{\mathrm{Borcherds}}\}$ at $N=1$.

**Failure on $Q_5$.** $\mathrm{at}_{Q_5}\ne 0$ with 101-dim bracket $[m_3,B^{(2)}]_{Q_5}\ne 0$ (Kapranov 1999 §4; $h^{2,1}(Q_5)=101$); all four climaxes fail strictly. Three-route convergence at $K=8$ unconditional; siblings $\{K=2$ Monster, $K=4$ Enriques, $K=12$ Conway-$K=2$-transported, $K=50$ FM$\}$ conditional on Dunn-Lurie Serre-CM.

## XXXII. Audit layers

| Layer | Finding | Status |
|---|---|---|
| **Witten** | $Z^{\mathrm{AdS}_3\times K3}_{\mathrm{3dQG}}=1/\Phi_{10}$ via Stage-2 $\mathbf H_{\Delta_5}\vert_E$; 24-count six-way; Maloney-Witten 2009 $\ne$ DVV | proved leading; all-orders conjectural |
| **Witten ladder** | Programme-canonical ladder $k_N^{\mathrm{prog}}=(5,4,3,2,1)$ at $N\in\{1,2,3,4,6\}$ via Gritsenko lift: $\kappa_{\mathrm{BKM}}(\Phi_N^{\mathrm{prog}})=c_N(0)/2$ with $c_N(0)=(10,8,6,4,2)$ (Gritsenko 1999 Thm 1.1+2.1; GN 1997 Duke 119 Thm 1.5). Physical CHL $k_N^{\mathrm{CHL}}=24/(N+1)-2=(10,6,4,2,1,0)$ at $N\in\{1,2,3,5,7,11\}$ via $\mathrm{Aut}(\mathrm{Co}_0)\supset M_{23}$-twists (Jatkar-Sen 2005; David-Jatkar-Sen 2006). Two orthogonal setups. Weight-doubling $k_N^{\mathrm{CHL}}=2k_N^{\mathrm{prog}}$ at $N=1$ only: $\Phi_{10}^{\mathrm{CHL}}=\Delta_5^2$ (Igusa 1964 + GN 1995). Four distinct Jacobi ladders; programme canonical for Stage-2 $\Phi_3$ on $K3\times E$. Cross-volume $N=1$: ghost trace (Vol I) = Pentagon trace (Vol II) = Borcherds weight $\kappa_{\mathrm{BKM}}(\Delta_5)$ (Vol III) $=5$ | proved |
| **Drinfeld** | $\Phi_4$ HK-CY4 needs Kapranov-wt-2; $G_2/\mathrm{Spin}(7)$ outside; $\mathrm{Shad}_X$ non-surjective; $(\Sigma,C)$ non-unique at $d\ge 4$; seven incarnations $\ne$ three lenses | rectified |
| **Beilinson** | Stage-1 empty on generic quintic; character-level only; Conway structural boundary of $\hbar^2 K=-1$ | rescoped |
| **Gelfand stress tower** | Stage-2 shadow of $\mathcal W_N$-braided CY$_2$ (Nakajima-MO on $\mathrm{Hilb}^N(\C^2)$) carries $\kappa$-outside-tower $(H_N-1)(4N^3-2N-2)$ via principal DS + $\int_{S^1}$: $N=8$ gives $13949/4$; $N=9$ $1668458/315$; $N=10$ $1074281/140$. Two-path verification (MO-R-matrix / Fateev-Lukyanov Miura; Schiffmann-Vasserot elliptic Hall / Pope-Romans-Shen). Tower unbounded outside landmark closure | proved unbounded |
| **Nekrasov** | 3 earned (BPS-index, $\mathrm{CoHA}=Y^+$, Nek self-dual); 2 downgraded (all-loop, naturality) | 3/5 earned |
| **Manin-Gaitsgory** | Averaging $\Phi_3(T^3)$; two-stage Ran-lift; Chenevier K3; MGSL KS | baseline |
| **MG Atiyah-Koszul** | $\mathcal U^{\mathrm{canonical}}_{\Phi_3}(K3\times E)=\mathcal P^{-1}(U^{\mathrm{adm}})$ dense open 21-dim, transcendental witness | non-empty, dense, $\dim_\C=21$ |
| **Bondal-Kuznetsov** | $\Phi^{\mathrm{FA}}_d$ filtered colim + compact $d\le 2$; symm-monoidal $d\in\{2,3\}$; $\Phi_2(\mathcal K u(Y_3))=\mathcal H_{\mathrm{Muk}(S)}$; $\hbar$-twist IS three-faces | proved smooth CY$_{\le 3}$ |
| **BK hostless** | $\mathrm{BKM}^{\mathrm{hostless}}$ commutes triangle on inside-$\mathrm{Shad}$ rows + $24A_1$ + 2 hyperbolic + FM; 22 non-Leech conditional on Chenevier non-reduced | 26/28 proved |
| **Kapranov** | Iterated EH; Dolbeault local; $\mathrm{Shad}_X$ Cartesian smooth; triangle inherits; $P_d^!\simeq P_d$ smooth CY | 3/5 proved |
| **Kapranov Hopf arity-4** | $\mathrm{FM}_4(4)\to\mathrm{FM}_2(4)$ stratified $T^3$-phase bundle fibre $(S^2)^{\times 3}$; three binary trees Künneth-independently Hopf-reduce; $K_5$ 14-vertex, $K_4$ pentagon verified on five codim-2 strata; arity-3 fibre $S^2\times S^2$ matches Cartan $\mathrm{diag}(4,4,-2)$ BKM | 5/5 proved arity-4 smooth CY$_{\le 2}$; $d\ge 3$ HK conditional |
| **Costello** | Compact $K3\times E$ Costello Thm 13.4.1 direct; non-compact CG Thm 8.6.9; two Koszul loci; $\mathfrak g_{\Delta_5}$ non-Deligne, quartic IS Mukai-Serre $K^\kappa=8$; $\mathrm{Trc}\circ\Phi_3=-1$ | proved leading; unification conjectural |
| **Kontsevich universal cocycle** | $[m_3,B^{(2)}]_X=\mathrm{at}_X\cup B^{(2)}_{\mathrm{Connes}}$ gates Stage-1 strict existence. Four strata: $\C^3$ formal ($\mu_3=0$); conifold formal; local $\P^2$/$K3\times E$ TCFT; quintic $Q_5$ obstructed with $H^{1,3}(Q_5)\simeq\C^{101}$ | universal cocycle gates $\mathbf H_{\Delta_5}$; $K3\times E$ inside; $Q_5$ outside |

**Net verdict.** Two-stage $\Phi_d$ on smooth $\mathrm{CY}_{\le 3}$; canonical $\mathbf H_{\Delta_5}$ construction-1 level; Stage-1 canonicity on $\mathcal U^{\mathrm{adm}}$; Stage-2 specialisation-family; seven-incarnation lock character-level (Göttsche-Borcherds); three-faces three-route unconditional, unification conditional; $\Psi$ surjective via S17+DMS21+S06; $\mathrm{Shad}_X$ non-surjective on $\mathrm{CY}_2^{\mathrm{cat}}$, covered by $\mathrm{BKM}^{\mathrm{hostless}}$ over $\mathrm{JacPair}^{\mathrm{sw}}_0$ through $\Psi_{\mathrm{Borcherds}}$ (28-row complement surjected modulo 22-row $M_{23}$ Chenevier residual). Kontsevich universal cocycle gates $\mathbf H_{\Delta_5}$ climax: on $K3\times E$ cocycle vanishes in $H^{1,3}=0$ by Künneth; $Q_5$ only perturbative.

## XXXIII. Gluing (Chapter 26) four-stratum taxonomy

Every CY-3 carries $\mathrm{Str}(X)\subseteq\{\mathrm i,\mathrm{ii},\mathrm{iii},\mathrm{iv}\}$:
(i) toric $T^d$ (local $\P^2$, $\C^3$, resolved conifold, banana, SPP);
(ii) reduced $\G_m+\mathrm{Aut}(X)$ (K3, $K3\times E$, abelian surface, Nikulin-involution K3);
(iii) orbifold inertia $I(X/G)$ (Mathieu $M_{24}$, McKay $\Gamma\subset\mathrm{SU}(d)$);
(iv) lattice-polarised period domain (Borcherds, Gritsenko $\Delta_5$, Igusa $\Phi_{10}$).

Classification: exactly $15=2^4-1$ non-empty cells, empty cell excluded by Joyce-Song sign theorem (Joyce-Song 2012 Thm 5.14 $\G_m$-scaling of $\Omega_X$ required for $\epsilon(E,F)=(-1)^{\chi(E,F)}$). Four-stratum exhaust by automorphism-tower filtration $\mathrm{Aut}^\circ\lhd\mathrm{Aut}\lhd\widetilde{\mathrm{Aut}}\lhd\Gamma_{\mathrm{arith}}$. Stratum-cell cocycle targets: (i) $H^1(\Sigma,\underline\Pic_{T^d})$; (ii) $\mathrm{Aut}_s$-character data; (iii) $H^1_{\mathrm{Gal}}(G,-)$; (iv) Fourier coefficients of Gritsenko-Cléry weight-$k_\Psi=c_\phi(0,0)/2$ forms. Two-chart Čech atlas is not a Weiss cover (Costello-Gwilliam vol 2 Def 6.1.6); recovers QC-descent only, not factorisation locality. $K3\times E$ is the cell-15 master example where all four strata meet.

**$2.5$-obstruction count on compact CY-3 without $K3\times E$-fibration.** Effective count $2.5=1+1+0.5$ on strict CY-3 with $h^{1,0}=0$. (O1) toric-fan-completeness $|\Sigma|=N_\R$ via Demazure-Fulton §3.4 Thm 3.1.5 + Luna étale slice; (O3) Bogomolov-Beauville-Matsumura $\mathrm{Aut}^\circ$ rigidity via Beauville JDG 18:755 decomposition + Matsumura Proc Japan Acad 39:181; (O1) $\Leftrightarrow$ (O3) via Sumihiro 1974 J Math Kyoto 14:1 Thm 1; (O1) $\Rightarrow$ (O4) via outer-gauge-torus $T_Q^{\mathrm{out}}=\ker(\Z^{Q_1}\to\Z)\otimes\C^\times$ + Bocklandt arXiv:math/0603558 + Hartogs $R=\C$; (O2) BCOV $\alpha_{\mathrm{BCOV}}=(\chi/24)\cdot\mathrm{tr}\,\mathrm{At}(T_X)\in H^1(X,\mathcal O_X)$ logically independent. Correct cohomological home: $H^{0,1}(X,\mathcal O_X)$, not $H^{0,1}(X,\mathrm{Sym}^{\le 2}T^*_X)$. Four-case factor-split: (i) non-compact retractable (conifold); (ii) strict $h^{0,1}=0$ (quintic); (iii) $K3\times E$ Künneth $\chi_{\mathrm{top}}=0$; (iv) abelian-factor CY-3 $=X_{\mathrm{strict}}\times A$. $K3\times E$ has $h^{1,0}=1$ via Künneth from $E$, outside the $2.5$-count hypothesis — the five-fold Serre-equivariant quasi-NCCR catalogue applies. $K_0^{\mathrm{num}}$ rank for strict CY-3: $\mathrm{rk}=2+2h^{1,1}(X)$.

**CoHA(conifold) master identification** $\mathrm{CoHA}(Q_{\mathrm{con}},W_{\mathrm{con}})\simeq Y^+(\widehat{\mathfrak{gl}}(1|1))^{\mathrm{con}}$ (see §VIII).

## XXXIV. Primary-literature fixings

(a) Keller-Van den Bergh arXiv:0906.0761 correct (not cluster-algebra 0912.3781); (b) Costello-Yagi 1810.01970 two-author (simply-laced bosonic all-orders) vs Costello-Gaiotto-Yagi 2103.01835 three-author (distinct twisted-supergravity paper); (c) $Y_{0,1,1}[\psi]=\mathcal W(\mathfrak{gl}(1|1))_\psi$ is Li-Yamazaki synthesis, not a Gaiotto-Rapčák theorem; (d) super-Kontsevich-Tamarkin formality is $E_2$-only (Ginzburg-Schedler arXiv:0807.0174), $E_3$ open; (e) two scopes of universal Borcherds $\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2$: Scope (A) CHL ladder on $N\in\{1,2,3,4,6\}$ with $(10,8,6,4,2)\to(5,4,3,2,1)$ per Gritsenko-Nikulin 1995 Pt II Thm 2.1, Scope (B) Gritsenko-Cléry eight-form atlas with $(10,4,2,2,1,2,1/2,0)\to(5,2,1,1,1/2,1,1/4,0)$ per Gritsenko-Cléry 2013 §3; (f) Saito-Kurokawa lift target $\Phi_{10}=\Delta_5^2$, rescale factor 4 from Siegel-weight doubling $\times$ Andrianov convention, elliptic source $g=\Delta\cdot E_6\in S_{18}$; (g) pentagon in canonical Faddeev-Kashaev form $\Psi(x_0)\Psi(x_1)=\Psi(x_1)\Psi(q^{-1/2}x_0 x_1)\Psi(x_0)$ middle-factor = bound-state $[S_0]+[S_1]$; (h) $\dim\mathrm{Stab}=\mathrm{rk}\,K_0^{\mathrm{num}}$, independent of CY dimension; (i) Bryan-Pandharipande 2001 arXiv:math/0009025 (super-rigidity) vs Bryan-Pandharipande 2005 arXiv:math/0412005 (local GW primitive) vs Pandharipande 1999 arXiv:math/9902107 (Hodge integrals); (j) Negut conifold bond $\varphi^{0\Rightarrow 1}(u)=(u+h_1)(u+h_2)/[u(u+h_1+h_2)]$; (k) BBJ Darboux-for-shifted-symplectic arXiv:1305.6302 Thm 5.18; (l) super-shuffle $\mathrm{Sh}^{\mathrm{super}}_{m,n}=(\C[z^{(0)}]\otimes\Lambda[z^{(1)}])^{S_m\times S_n}$ bigraded polynomial $\otimes$ exterior; (m) super-YBE: $R_{\mathrm{KS}}(u)=I+(\hbar/u)P_s$ linear in $\hbar$; $[P_{12},P_{13}]=(123)_s-(132)_s$; correct Macdonald-Shiraishi double $q$-Pochhammer; crossing symmetry degenerate on $\mathfrak{gl}(1|1)$ (super-dim 0), non-trivial only at $\mathfrak{osp}(4|20)$ lift; Drinfeld-new $\psi^{(0)},\psi^{(1)}$ conjugation act oppositely on $e$.

## XXXV. Structural frontiers

Five eight-form atlas $N=5$ Borcea-Voisin / $N=7$ order-4 gerbe / $N=8$ Kummer$_3$ siblings are load-bearing frontiers (per Lorgat arXiv:2007.14218 Conjecture 1). The $K3\times K3\times E$ $d=5$ Fake-Monster lift via Dunn-Lurie $E_5\simeq E_2\otimes E_2\otimes E_1$ on $\mathrm{II}_{25,1}$ is the natural extension of the $\mathbf H_{\Delta_5}$ framework to the Fake Monster Lie algebra $\mathfrak g_{\Phi_{12}}$. Super-KT formality $E_3$-upgrade is the single obstruction blocking all-orders Costello-Yagi extension to $\mathfrak{gl}(1|1)$-gauge 5D hCS. All-four-climaxes verification on $Q_5$ quintic fails strictly via $\mathrm{at}_{Q_5}\ne 0$ with 101-dim bracket — stratum-free categorical CoHA via MNOP + Davison-Meinhardt integrality is the residual content on compact CY-3 without fibration structure.
