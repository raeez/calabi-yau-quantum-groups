# F-META-1 --- Final frontier crystallisation (Vol III Wave 3, Opus 4.7 relaunch, post-3B-C23 update)

## Organising principle

One functor
$\Phi \colon \mathrm{CY}\text{-}\mathrm{cat}_d \to \mathrm{ChirAlg}$
with the two-stage factorisation
$\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$
at $d = 3$, three-stage factorisation
$\Phi_5 = \pi_{\mathrm{Niem}} \circ \mathrm{Sp}_{K3^2, E} \circ \Phi^{\mathrm{FA}}_5$
at $d = 5$. Five $\kappa$-invariants plus anomaly ratio $\varrho$, never
conflated. Universal Borcherds-weight identity
$\kappa_{\mathrm{BKM}}(\Psi) = c_\Psi(0) / 2$. Three-lift compatibility
of the CHL ladder $(5, 2, 1, 1, 1)$ at
$N \in \{1, 2, 3, 4, 6\}$. Derived-centre complementarity
$\kappa + \kappa^! \in \{0, 8, 13, 250/3, 98/3\}$ on the
$\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$ landmark, with the
$\mathsf{B}$-row $K^{\kappa} = 8 = 2 c_+(\widetilde{\Lambda}(K3))$ as the
Vol III Mukai-enhanced K3 Heisenberg witness.

This ledger names every Wave 3 item at its honest terminal state, bundles
the items by shared primary-source anchor, declares the frontiers that
remain open, and traces the cross-volume dependencies. The post-3B-C23
update reclassifies the direct-threefold principal-component
Nakajima-Baranovsky correspondence on $\mathrm{Hilb}^n_{\mathrm{prin}}(K3 \times E)$
from a State-B conditional closure (single-hypothesis) to a State-C
genuine frontier with three required inputs R1-R3, reflecting the
structural failure of Nakajima's Lagrangian-intersection argument on
CY$_3$ (the ambient product has no holomorphic symplectic structure in
dimension three), the virtual-not-topological nature of Li 2001 +
Okounkov--Pandharipande 2010 DT identities, and the non-functoriality
of Dunn-Lurie on the direct threefold side without a pre-existing
$E_1$-input.

## State-A ledger (full closure, unconditional at Chriss--Ginzburg detail)

Every A-row lists the Wave 3 agent tag, the single mathematical statement
closed, and the primary-source chain. No row is an "extension within
reach"; every row is a theorem stated in the lane in which its proof
actually works.

**A01. BCFG all-orders $\hCS \to Y_\hbar(\widehat{\fg}^{(r)})$
unconditional.** Closure 3B-C01. The $\sigma$-equivariant
counterterm transfer for 6D $\hCS$ on $\CC^3$ with Dynkin fold
$\sigma$ of order $r \in \{2, 3\}$ is a direct corollary of
Costello 2011 Theorem 9.3.1 applied to a finite $G$-action in
characteristic zero, using Maschke averaging; no higher-loop
finite-group-cohomology obstruction arises ($H^{\geq 1}(G, V) = 0$
for finite $G$ and $\mathbb{Q}$-vector space $V$; Weibel 1994
Corollary 6.5.9). The Costello 2013 arXiv:1303.2632 §§4--5 5D-boundary
functor transports the $\sigma$-equivariant quantisation to
$\partial\hCS_5(\fg^{\mathrm{ADE}})^\sigma \simeq
Y_\epsilon(\widehat{\fg}^{(r)})$ for
$\fg \in \{B_n, C_n, F_4, G_2\}$; Kac 1990 Ch.\ 8 Theorem 8.3 identifies
$(\widehat{\fg}^{\mathrm{ADE}})^\sigma = \widehat{\fg}^{(r)}$;
Guay--Nakajima--Wendlandt 2018 *Adv.\ Math.* 338 lifts this to the
Yangian level. This upgrades the Wave 3 C01 terminal state from B to A
and discharges the Wave 2 residual frontier item "BCFG
$\sigma$-equivariant renormalisation scheme for Costello 6d $\hCS$".
Primary: Costello 2011 AMS Math.\ Surveys 170 Thm.\ 9.3.1;
Costello--Gwilliam 2017 Vol.\ II §11; Costello 2013 arXiv:1303.2632
§§2--5; Francis 2013 *Geom.\ Topol.* 17 Thm.\ 2.29.

**A02. Single CHL Borcherds ladder $(5, 2, 1, 1, 1)$.** Closure
3B-C26 + F-META-2. Under the singly-twined Eichler--Zagier
normalisation $\phi^{(g_N)}_{0, 1} = \tfrac{1}{2} Z^{(g_N)}_{K3}$, the
constant Fourier coefficients
$(c^{(g_N)}_{0, 1}(0, 0))_{N = 1, 2, 3, 4, 6} = (10, 4, 2, 2, 2)$
give $\kappa_{\mathrm{BKM}}(\Phi_N) = (5, 2, 1, 1, 1)$. The previously
tabulated $(5, 4, 3, 2, 1)$ and $(5, 4, 3, 2, 2)$ ladders were
mis-transcriptions: $(5, 4, 3, 2, 1)$ misread Gritsenko 1999
additive-lift weights at index-1 (where $J^{\mathrm{cusp}}_{0,1} = 0$);
$(5, 4, 3, 2, 2)$ truncated an unrelated extended sequence indexed
$N = 1, \ldots, 5$ at the boundary half-integer-weight regime. Three
mutually compatible primary lifts land on the same paramodular
Borcherds product $\Phi_N = \Delta^{(N)}$: Borcherds 1998 Invent.\
Math.\ 132 Thm.\ 13.3; Gritsenko 1999 *Abh.\ Math.\ Sem.\ Hamburg*
69 Thm.\ 1.1; Gritsenko--Nikulin 1998 *Duke Math.\ J.* 94 Thm.\ 2.1.
Cross-verified: Eichler--Zagier 1985 *Theory of Jacobi Forms* Thm.\
9.3; Cheng--Harrison--Paquette--Volpato 2014 *Commun.\ Number Theory
Phys.* 8 Table 4; Mukai 1988 *Invent.\ Math.* 94 §4 Table;
Hashimoto 2012 *Tohoku* 64. The Vol I cache C4 and FRONTIER.md line 15
are rectified as A-type value corrections on the same
three-factor universal-trace identity (F-META-2).

**A03. Dimension-stratified GKM census (Delta-5, Monster, Fake Monster).**
Closure C07. Three Borcherds--Kac--Moody superalgebras produced by
$\Phi$ as Stage-2 specialisations of Stage-1 holomorphic factorisation
algebras; rows indexed by $(d, \mathrm{shift}, E_n^{\mathrm{cl}})$:
$(3, -1, E_3^{\mathrm{hol}}\text{-BV})$ at K3 x E and virtual $d = 3$
Monster; $(5, +1, E_5\text{-Poisson})$ at $K3 \times K3 \times E$.
Four structural identifications: (U1) universal Borcherds-weight
identity $\mathrm{wt}(\Psi) = c(0)/2$; (U2) Wang--Williams 2023 Thm.\
3.5 pullback rigidity ($\Phi_{12}$ at signature $(2, 26)$ is the
universal singular-weight source, not $\Delta_5$ at $(2, 3)$);
(U3) Nikulin 1979 Thm.\ 1.12.2 primitive-embedding forced stratification
$d = 3 \not\supset \mathrm{FM}$, $d = 5 \supset \mathrm{FM}$;
(U4) shift-law row $(d - 4)$ selecting the $E_n^{\mathrm{cl}}$
class via PTVV 2013 *Publ.\ Math.\ IHES* 117 Thm.\ 2.5.

**A04. Compact CY$_3$ 3-dualisability and $(\infty, 3)$-TFT extension of
$\Phi_3$.** Closure 3B-C05. For $X$ a smooth compact CY$_3$ and $\fg$
reductive, the chain-level decomposition
$\HH^\bullet_{E_3}(\Obs_{\hCS}(X)|_\fg) \simeq
\bigoplus_{p + q = \bullet} H^p_{\mathrm{Lie}}(\fg, \C) \otimes_\C
H^{0, q}(X)$ holds with each degree finite-dimensional, via Griffiths--
Harris 1978 Ch.\ 0 §6 (Dolbeault) + Costello--Li 2016 §3 (compact-CY$_3$
BV propagator) + Francis 2013 *Compos.\ Math.* 149 Thm.\ 3.4 ($E_n$-PBW,
universal) + Griffiths--Harris 1978 Ch.\ 0 §7 (compact Kahler Hodge-Kodaira
discrete spectrum). 3-dualisability in $\mathrm{Alg}_{E_3}(\mathrm{Ch}(\mathrm{Dolb}))$
follows via PTVV 2013 + CPTVV 2017 arXiv:1506.03699 Prop.\ 2.6. The
Lurie 2009 cobordism hypothesis promotes 6D $\hCS$ on $X$ to a fully
extended framed $E_3$-TFT, and $\Phi_3$ extends to an $(\infty,3)$-functor
on the compact CY$_3$ subcategory. Gwilliam--Williams 2021 arXiv:2009.05037
Prop.\ 5.3.2 is the $\C^3$-specialisation (polynomial Dolbeault) of the
same universal Francis PBW; compactness turns the infinite-rank
polynomial ring into finite-rank Hodge data supplying the
2-morphism-level duals.

**A05. Schur index $\mathcal{I}_S(\mathcal{T}[A_1, \Sigma_{0, 24}])$ to
$q^{10}$.** Closure C14. Direct plethystic-exponential product
$\mathrm{PE}[(72 q - 22 q^2)/(1 - q)]$ (valid through $q^{10}$
since the $j = 1/2$ summand first enters at $q^{11}$) with explicit
Fourier coefficients $(1, 72, 2678, 68474, 1\,351\,775, 21\,945\,390,
304\,799\,105, 3\,720\,945\,220, 40\,716\,498\,035,
405\,322\,063\,500, 3\,713\,379\,957\,230)$. Central-charge anchor
$c_{4d}(A_1, \Sigma_{0, n}) = (5n - 13) / 6 = 107/6$ at $n = 24$,
$c_{2d} = -12 c_{4d} = -214$. Primary: Gadde--Rastelli--Razamat--Yan 2011
arXiv:1104.3850 §3; BLPR 2015 *Commun.\ Math.\ Phys.* 336 arXiv:1506.02046
§2.2; Beem--Lemos--Liendo--Peelaers--Rastelli--van Rees 2013 *Commun.\
Math.\ Phys.* 336 arXiv:1312.5344.

**A06. Sigma_{0, 24} geometric selection (monodromy level only).**
Closure 3B-C19. At the monodromy-Diophantine level the
Kodaira--Miranda assignment $j_{\mathrm{Kod}} \colon
\mathcal{M}^{\mathrm{ell-K3}}_{\mathrm{gen}} \to
\mathrm{Hur}_{24}^{\mathrm{SL}_2(\Z)}(\PP^1)$ is a morphism of
algebraic stacks, and its composite with Beem--Rastelli restricted to
class-$\mathcal{S}$ $A_1$ is moduli-stack-functorial. The
$(g, n) = (0, 24)$ selection operates at monodromy-Diophantine level
($c_2(K3) = 24$, $g(\mathrm{base}) = 0$ via $H^1(K3, \mathcal{O}) = 0$,
$13(g - 1) + 5n = 107$), independent of the SCFT-moduli-stack gap.
Primary: Kodaira 1963 *Ann.\ Math.* 77 Thm.\ 12.2; Miranda 1989 §IV.3;
Schutt--Shioda 2019 Thm.\ 5.13; Sen 1996 *Nucl.\ Phys.\ B* 475;
Diaz--Edidin 1996 *Math.\ Ann.* 304 Thm.\ 2.1;
Beem--Peelaers--Rastelli 2014 arXiv:1404.6657 Prop.\ 2.4;
Frenkel--Ben-Zvi 2004 Ch.\ 19.

**A07. Leech primitive embedding into enhanced Mukai of $K3 \times K3$.**
Closure C20. Rectification: the Mukai lattice of $K3 \times K3$ is the
Kunneth tensor-product
$\widetilde{\Lambda}(K3) \otimes_\Z \widetilde{\Lambda}(K3)$ of rank
$576$ and signature $(416, 160)$, not the direct sum. Primitive
embedding $\mathrm{II}_{25, 1} \hookrightarrow
\widetilde{\Lambda}(K3 \times K3) \oplus U(E)$ exists, unique up to
$\mathrm{O}$-action, by Nikulin 1979 Thms.\ 1.12.2 and 1.14.2
(trivial discriminant, signature bounds $25 \leq 417$ and $1 \leq 161$
satisfied); canonically selected by the Mukai chain
$\mathrm{Aut}_s(K3) \subset M_{23} \subset M_{24} \subset \mathrm{Co}_0$
(Mukai 1988 *Invent.\ Math.* 94). Orthogonal complement of rank $552$,
signature $(392, 160)$, trivial discriminant, isometric to
$\mathrm{II}_{392, 160}$.

**A08. Three-stage factorisation $\Phi_5 = \pi_{\mathrm{Niem}} \circ
\mathrm{Sp}_{K3^2, E} \circ \Phi^{\mathrm{FA}}_5$ on $K3 \times K3 \times
E$.** Closure C21. Stage 1: Kontsevich--Tamarkin $E_5$-formality +
Costello--Gwilliam--Li holomorphic locality. Stage 2: Dunn--Lurie
factorisation $E_5 = (E_2 \otimes E_2) \otimes E_1$ on
$\dim_\C = 4$ transverse $K3_1 \times K3_2$, producing
super-$E_1$-chiral algebra on $E$ with charge lattice
$\widetilde{\Lambda}(K3_1) \otimes \widetilde{\Lambda}(K3_2) \oplus U(E)$
of signature $(417, 161)$ and $\Z_2$-super-grading from the stable-framing
class $\pi_5(B\mathrm{Sp}) = \Z_2$. Stage 3: Niemeier projection
selecting the Leech orbit by the no-roots condition via the
$M_{23} \subset M_{24} \subset \mathrm{Co}_0$ chain.

**A09. Twenty-three umbral-moonshine Stage-3 siblings at $d = 5$.**
Closure 3B-C30. The $24$ Niemeier lattices (Niemeier 1973; Venkov 1980;
Conway--Sloane 1988 Ch.\ 16) are in canonical bijection with $24$
Stage-3 outputs of $\Phi_5$ on $X = K3_1 \times K3_2 \times E$; the Leech
orbit selects the Fake Monster, and the $23$ non-Leech orbits supply the
$23$ umbral-moonshine siblings of Cheng--Duncan--Harvey 2014 *Commun.\
Number Theory Phys.* 8. Primitive embeddings via Nikulin 1979 Thm.\
1.12.2; umbral group $G_\Lambda = \mathrm{Aut}(N_\Lambda) /
W(\bar{R}_\Lambda)$; lambency $\ell_\Lambda = h(\bar{R}_\Lambda)$
(Venkov 1980 Prop.\ 1 balance condition); twinings
$H^{(\Lambda)}_g$ are mock modular forms of weight $1/2$
(Cheng--Duncan--Harvey 2014 Thm.\ 4.1; Duncan--Griffin--Ono 2015
*Research Math.\ Sci.* 2 for unconditional construction).
Uniform prediction $\kappa_{\mathrm{BKM}}^{(\Lambda)} = c^{(\Lambda)}(0) / 2 = 12$
via $c^{(\Lambda)}(0) = 24$ by $M_{24}$-twining constancy.

**A10. Weierstrass obstruction theorem: no $\rho = 20$ K3 realises
$I_2 + I_2 + 20 I_1$ with unimodular MW $= E_8(-1)^{\oplus 2}$.**
Closure C16. Shioda--Tate + Nikulin determinant formula forces
$\det T(S) = 4$, hence $S = X_4$ (Vinberg's most algebraic K3 with
$T(X_4) = \mathrm{diag}(2, 2)$, Shimada 2001 *Nagoya Math.\ J.* 161),
and the Nishiyama--Kneser classification (Nishiyama 1996
*Japan J.\ Math.* 22 Thm.\ 4.1) excludes the simultaneous realisation.
The surviving closest realisation is the Kuwata--Shioda $F^{(5)}$
base-change at $\rho = 18$ with fibre configuration $2 II + 20 I_1$
and non-unimodular MW $= E_8[5]^{\oplus 2}$ (Shioda 2007 MPIM 137
Thm.\ 2.5). This retires the original $\rho = 20$ target of C02 / C15.

**A11. Borcherds lift on the $F^{(5)}$ elliptic-surface ambient at
signature $(2, 18)$.** Closure 3B-C02. Borcherds 1998 Invent.\ Math.\
132 Thm.\ 13.3 applies unconditionally to the even signature-$(2, 18)$
lattice $\Lambda^{F^{(5)}} = \mathrm{NS}(F^{(5)}) \oplus U_E = U_{\pi_5}
\oplus E_8[5]^{\oplus 2} \oplus U_E$ (no unimodularity required; the
$[5]$-rescaling propagates through the singular-theta lift as a
level-5 Weil-representation shift). At untwisted K3 input
$\kappa_{\mathrm{BKM}} = c_\chi(0)/2 = 5$. Primary: Borcherds 1998
Thm.\ 13.3; Shioda 2007 MPIM 137 Thm.\ 2.5; Scheithauer 2009
*Compos.\ Math.* 145 Prop.\ 3.2; Bruinier 2002 *Lecture Notes Math.*
1780 Prop.\ 2.6; Eichler--Zagier 1985 Thm.\ 9.5.

**A12. Enriques fourth witness for Bruinier--Mukai reciprocity.**
Closure 3B-C27. On the Mukai-enhanced Enriques lattice
$\Lambda^{\mathrm{Muk}}_{\mathrm{Enr}} = U \oplus U \oplus E_8(-1)$ of
signature $(2, 10)$: Mukai-signature doubling $2 c_+ = 4$, Borcherds
weight $\kappa_{\mathrm{BKM}}(\Phi_2^{\mathrm{Enr}}) = c_2(0) / 2 = 4$
(Allcock 2000 *Math.\ Ann.* 317 Thm.\ 8.1; Gritsenko 1999
*Abh.\ Math.\ Sem.\ Hamburg* 69 Thm.\ 6.1 via $\Phi_{12}$-quasi-pullback),
Humbert monodromy order $4$ (via Allcock principal Fourier coefficient
$c_\phi(1,1) = 1/4$ and Riemann--Hilbert, independently of the
BrukaMilk hypothesis), Lusztig level $\ell = 4$ via Kapranov--Vasserot
2019 $\Z_2$-equivariant CoHA. Four-way agreement at $4$ expands the
numerical witness base of conj:bz-mukai-bruinier-reciprocity from
three points (Monster $2$, K3 $8$, Fake Monster $50$) to four; the
universal Kontsevich-torsor identity $\hbar^2 K = -1$ holds at all four
witnesses. User's "$\Phi_2$ weight $2$" corrected: the BKM denominator
is the weight-$4$ Allcock product, not the weight-$2$ $\mu_2$-cover
square root.

**A13. Rank-$\leq 4$ lattice-polarised $\mathfrak{g}_L$ family.**
Closure C13 at rank 3 and rank 4, closure 3B-C13 for the rank-$\geq 5$
scope audit. Rank 3 ($L \in \{U \oplus \langle -2 \rangle,
U \oplus \langle -4 \rangle, U \oplus \langle -6 \rangle\}$) and rank 4
($L \in \{U \oplus U, U \oplus U(2), U \oplus U(3),
U \oplus \langle -2 \rangle^{\oplus 2}\}$) close unconditionally via
Borcherds 1998 Thm.\ 13.3 + Gritsenko--Nikulin 1998 Thm.\ 1.1 +
Scheithauer 2006 *Invent.\ Math.* 164 + Gritsenko--Clery 2008
arXiv:0812.3962 Thm.\ 3. Rank 6 envelope $L = U^{\oplus 3}$: Thm.\
via Borcherds 1998 Thm.\ 8.1. All rank-$\leq 4$ rows satisfy the
universal identity $\kappa_{\mathrm{BKM}}(\mathfrak{g}_L) = c_L(0)/2$.

**A14. CoHA one-loop anomaly $C_2$ vs $d^{abc} d_{abc}$ separation.**
Closure C22. Two separate theorems: (1) quadratic-Casimir wave-function
renormalisation at ghost $0$ (local BV-trivial counterterm $\propto
C_2(\fg)$); (2) cubic-Casimir BV anomaly at ghost $+1$, with explicit
$\|\Omega_X\|^2_{L^2}$ BCOV norm factor from the Bochner--Martinelli
triangle integral. Primary: Costello 2011 AMS Math.\ Surveys 170 Ch.\ 9;
Costello--Gwilliam 2017 Vol.\ II Thm.\ 9.5.0.6; Costello--Li 2016
arXiv:1606.00365 Prop.\ 5.2.

**A15. Orphan reference `prop:archetype-complementarity-bridge` is
resolved.** Closure C25. Not orphaned: the proposition is fully stated
and proved in Vol I at
`/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex`
lines 1748--1942, `\ClaimStatusProvedHere`. Both
`chiral_center_theorem.tex` and `landscape_census.tex` are `\input` in
Vol I `main.tex` line 1763, so the cross-file references resolve
correctly. No inscription required.

**A16. CoHA treatise Strategy-3 principal-component rectification.**
Closure 3B-C29. Line 751--758 of `notes/CoHA_to_W_infty_treatise.tex`
is rewritten to scope the Gottsche-product decomposition to
$\mathrm{Hilb}^n_{\mathrm{prin}}(K3 \times E)$ of dimension $3n$
(smooth for $n \geq 1$), acknowledging that non-principal elementary
components exist for $n \geq 4$ (Iarrobino 1972; Cheah 1996), and
routing non-principal cohomology to the Donaldson--Thomas moduli via
Kontsevich--Soibelman 2008 arXiv:0811.2435 §1.4. The Goettsche-product
identification on cohomology is unconditional; the direct threefold
principal-component correspondence algebra promotion is separated out
to State-C (see C13 below).

**A17. CLAUDE.md two-scope + anomaly reconciliation.** Closure C24.
Five $\kappa$-subscripts plus anomaly ratio $\varrho$, K3 x E crystal
at two parallel scopes ($\{2, 3, 5, 24\}$ at K3-fibre + Cartan-rank
scope; $\{0, 4, 5, 24\}$ at total-space + Mukai-enhanced scope) unified
by the four-functor square of Theorem
`wn:thm:second-pass-four-functor-square`, five-archetype ceiling
$\{0, 8, 13, 250/3, 98/3\}$ as landmark-not-universal. No new
primary-source input; all sources already cited in the spine and
Wave-2 refinement.

**A18. Wave-2 three-faces rectification (split into two + one).**
Closure 3B-C28. The Wave-2 Theorem
`wn:thm:second-pass-promotions` is split into two environments: a
truncated theorem preserving BCFG universal vanishing and class-$\mathcal{S}$
$c_{4d} = 107/6$ as unconditional (`\ClaimStatusTheorem`), plus a
conjectural theorem `wn:thm:second-pass-three-faces-serre`
carrying `\ClaimStatusConjectured` with explicit
Hypothesis `hyp:dunn-lurie-serre-heisdouble` (Lurie *Higher Algebra*
Thm.\ 5.5.3.6 specialised to Heisdouble$(K3 \times E)$). The three
underlying faces (Mukai, Humbert, Lusztig) each individually remain
theorems; only their unification into a single structural
$\rho_8 = \overline{S_{K3}^2 \otimes \tau_E}$-action requires the
hypothesis.

**A19. Goettsche-product side carries the affine Yangian on
$V^{K3} \otimes V^E$ unconditionally.** Closure C23 + 3B-C23 Parts (U1)-(U4).
Four unconditional statements on the indirect Goettsche-product side of
$\bigoplus_n H^\ast_T(\mathrm{Hilb}^n_{\mathrm{prin}}(K3 \times E); \Q)$:
(U1) principal-component existence, irreducibility, dimension $3n$,
smoothness for all $n \geq 1$ (Wave-3 C23 base; Fogarty 1968 extended
via Hilbert--Chow on the smooth surface factor); (U2) Goettsche-product
decomposition
$V^X \simeq V^{K3} \otimes V^E$ of principal-component cohomology
(Goettsche 1990 *Math.\ Ann.* 286; Li--Qin--Wang 2004 *Math.\ Res.\
Lett.* 11 Thm.\ 1.2); (U3) affine Yangian $Y(\widehat{\mathfrak{gl}}_1)$
action on $V^{K3} \otimes V^E$ (Schiffmann--Vasserot 2013 *Publ.\ IHES*
118 Thm.\ 1.2 on the K3 factor via Nakajima lattice; Grojnowski 1996
*Math.\ Res.\ Lett.* 3 on the elliptic curve factor); (U4)
$E_2$-algebra structure on $V^{K3} \otimes V^E$ via Dunn-Lurie applied
to the two $E_1$-Heisenberg factors (Lurie *Higher Algebra* Thm.\
5.1.2.2; Dunn 1988 *J.\ Pure Appl.\ Algebra* 50). The three-composite-input
discipline of Cache 22S (MO stable envelope + Grojnowski-Nakajima K3
Heisenberg + Etingof-Kazhdan super-quantisation) is satisfied on the
indirect side. The direct threefold side remains open (C13 below).

## State-B ledger (conditional closure, single named hypothesis)

Every B-row lists the Wave 3 agent tag, the main statement, and the
specific published-or-near-published hypothesis whose verification
would upgrade the row to State A.

**B01. Bruinier--Mukai reciprocity across the full $\mathcal{B}$-family.**
Closure C17 + 3B-C17. Numerical identity
$K^{\kappa_{\mathrm{ch}}}(\mathbf{H}_L) = 2 c_+(L) = \mathrm{ord}(\mathrm{mon}\,
\mathcal{L}^{\Phi_L}|_{H_{\min}(L)}) = \ell_L$ holds at every audited
point (Monster $2$, Enriques $4$, K3 $8$, Fake Monster $50$) by three
primary-source routes each, and $\hbar^2 K = -1$ universally. Conditional
on hypothesis **BrukaMilk**: three-part extension of Howard--Madapusi-Pera
2020 *Invent.\ Math.* 220 (not 219 as originally tagged) derived Kudla
generating-series machinery = (a) signature widening beyond native
$(n, 2)$ Hermitian Type IV (required for K3 Mukai $(4, 20)$ and
Fake-Monster $(25, 1)$), (b) Arakelov Chern-class torsion-order
extraction on the principal Heegner divisor, (c) $c_+$-subcone
uniformity under lattice embeddings. 3B-C17 sharpens the C17 B-status:
HMP 2020 is necessary but not sufficient; the three extensions
constitute a genuine new theorem using HMP as platform, not a
specialisation.

**B02. Fake-Monster doubly-reduced DT integrand
$\chi_{A^{\mathrm{FM}}_E} \cdot \pi_{\mathrm{Niem}, *} = 1/\Phi_{12}$.**
Closure C11 + 3B-C11. Conditional on two hypotheses:
(MPT$^{\otimes 2}$) iterated Maulik--Pandharipande--Thomas obstruction
reduction on $K3_1 \times K3_2 \times E$, and (JFI-Leech) the
Jacobi-form-input identification
$\pi_{\mathrm{Niem}, *} \chi_{A^{\mathrm{FM}}_E} = \theta_{\Lambda_{24}} /
\eta^{24}$ as a weak Jacobi form on $\mathrm{II}_{26, 2}$. Closure
3B-C11 retires the earlier (mvKY) bi-Jacobi factorisation hypothesis
as structurally inconsistent (collapses at $y_1 = y_2 = 1$ to a
$(q_1, q_2)$-independent constant $144/\prod(1 - p^n)^{24}$); the
correct hypothesis is (JFI-Leech), a single-Jacobi-form identity
compatible with Borcherds 1995 alg-geom/9506003 §7 Thm.\ 7.1.
Weight match unconditional: $\kappa_{\mathrm{BKM}}(\Phi_{12}) = c(0)/2 =
24/2 = 12$.

**B03. Three-faces-of-$8$ unification at $\mathrm{Heisdouble}(K3 \times E)$.**
Closure C08 + 3B-C08 + 3B-C28. Conditional on the Dunn--Lurie Serre-CM
lift hypothesis: $S_{K3} = [2]$ and the CM translation
$\tau_E \colon p \mapsto i \cdot p$ on $E_{j = 1728}$ descend through
$\Phi_3$ to commuting $E_1$-chiral autoequivalences $\widetilde{S}_{K3},
\widetilde{\tau}_E$ of $\cF_{K3 \times E}$ with
$(\widetilde{S}_{K3} \otimes \widetilde{\tau}_E)^8 = [16] \otimes
\mathrm{id}$ acting trivially on the chiral bar complex. 3B-C08
corrects an arithmetic misprint ($(S_{K3}^2 \otimes \tau_E)^8 = [32]$,
not $[16]$; the intended composite is $S_{K3} \otimes \tau_E$) and
names three distinct gaps that must close jointly: (G1) arithmetic
normalisation (internal), (G2) cyclic-$A_\infty$-triviality of
$[2m]$-shifts on the chiral bar at $m \geq 2$ (not in Costello 2007
which handles $m = 1$), (G3) descent of the CM-elliptic Fourier--Mukai
kernel through $\Phi_3$ (Conjecture
`conj:phi-d-functoriality` at $d = 3$; only the Atiyah--Mukai kernel
is in Ben-Zvi--Francis--Nadler 2010 Prop.\ 2.3). The three underlying
faces (Mukai / Humbert / Lusztig) individually remain theorems.

**B04. Ran-level Miki $S_3$-triality on the shuffle factorisation
envelope.** Closure C03. The symmetric group $S_3$ acts on
$\cF_{Y^+} = \mathrm{Fact}_{\mathrm{Ran}(\C)}(V, \omega)$ by
automorphisms of factorisation algebras on $\mathrm{Ran}(\C)$,
via the symmetric Feigin--Odesskii--Negut kernel $\omega(x, y) =
\prod_{i = 1}^{3}(x - y + \epsilon_i)/(x - y)^3$ and the
Beilinson--Drinfeld 2004 §3.4.1 kernel construction.
**Unconditional on the shuffle-envelope side.** Primary: Schiffmann--Vasserot
2013 *Publ.\ IHES* 118 §4; Negut 2014; Beilinson--Drinfeld 2004
*Chiral Algebras* Ch.\ 3.4.1; Gaitsgory--Lurie 2014 *Notes on
factorizable sheaves* §4.

**B05. Bracket-level $\mathfrak{g}_{\mathrm{BPS}}(K3 \times E) \simeq
\mathfrak{g}_{\Delta_5}$ via Hecke--Borcherds identity (HB), imaginary-root
scope.** Closure C06 + 3B-C06. The unconditional reduction is to the
single **(HB) identity** on imaginary-root pairs:
$c(D_1) c(D_2) \langle \alpha_1, \alpha_2 \rangle_{II} =
c(D_{\mathrm{sum}}) N^{\mathrm{HN}}_{\Delta_5}(\alpha_1, \alpha_2)$,
verifiable via Gritsenko--Nikulin 1998 §3 Thm.\ 3.1 denominator
expansion or Harvey--Moore 1996 threshold integral. Closure 3B-C06
falsifies (HB) at the real-simple-root sector (three primitive pairs
$(\delta_i, \delta_j)$ yield identical non-unit ratio $|$LHS$|/|$RHS$|
= 64/43$ by $S_3$-symmetry, because real-simple-root multiplicity is
$1$, not $c(D)$; Kac--Moody Serre relations govern real-simple-root
brackets, not Borcherds BKM combinatorics). (HB) must therefore be
restated with its imaginary-root scope as in Davison 2017 Thm.\ 1.1
+ Davison--Meinhardt 2020 Thm.\ A + Oberdieck--Pixton 2018
$\gamma \mapsto \alpha_\gamma$ primitive DT-root correspondence.

**B06. Elliptic-surface specialisation at $F^{(5)}$ with MW-indexed real
simple roots.** Closure C02 + 3B-C02. State A on Borcherds 1998 Thm.\
13.3 existence on signature $(2, 18)$ ambient (A11 above). State B on
the real-simple-root identification: under hypothesis
(H$_\sigma$) Shioda-height-to-Borcherds-real-root compatibility, the
$480 = 2 \cdot 240$ primitive height-$4$ Mordell--Weil sections
$\sigma \in \mathrm{MW}(\pi_5)/\mathrm{tors}$, rescaled by
$\chi(\mathcal{O}_{F^{(5)}})^{-1} \cdot n^{-1} = 1/10$, index the real
simple roots of $\mathfrak{g}_{F^{(5)}, \PP^1}$. (H$_\sigma$) is a
Borcherds-product Fourier-coefficient matching
($c_{\phi^{\pi_5}_{0, 1}}(1) = 256 = \#\{\sigma : \langle \sigma, \sigma
\rangle = -2\}$); the count is in Shioda 2007 MPIM 137 Thm.\ 2.4, but
the explicit Borcherds-product expansion on $\Lambda^{F^{(5)}}$ is not
in the published literature.

**B07. Rank-$\geq 5$ lattice-polarised $\mathfrak{g}_L$ family.**
Closure C13 + 3B-C13. Conditional on Gritsenko--Clery 2018
*Pure Appl.\ Math.\ Q.* 15 arXiv:1804.04488 Conjecture 5.1
(universality of Hecke--Maass-descended weak Jacobi form
$\phi_L \in J^{\mathrm{wk}}_{0, L}$ at signature $(1, t)$,
$4 \leq t \leq 19$). 3B-C13 audits Scheithauer 2006/2009/2017,
Bruinier 2002/2014, Ma 2018 *Amer.\ J.\ Math.* 140, Dittmann--Ma--Scheithauer
2021 *Adv.\ Math.* 386, Moller--Scheithauer 2023 *Ann.\ Math.* 197,
Wang--Williams 2023 arXiv:2303.04383: none of the cited works closes
Gritsenko--Clery Conj.\ 5.1 at rank $\geq 5$. Three candidate strategies
(lattice-functorial Hecke descent; modular-kernel uniformisation;
Kudla-programme Green-form descent) compatible with available
machinery but unexecuted. Status is **C (genuine frontier)** on the
conjecture itself, **B conditional on Conj.\ 5.1** on the GBKM
family entries at rank $\geq 5$ outside Gritsenko--Clery 2018 Table 4.

**B08. Bardeen--Zumino $L_\infty$-morphism via Atiyah--Kapranov coupling.**
Closure C04 + 3B-C04. Closure 3B-C04 falsifies the hypothesis
`hyp:mes-stora-zumino-holomorphic-descent-compatible-schemes` in the
holomorphic-Zumino-$Q_5$ form: on a CY$_3$, the Dolbeault curvature
$F(\cA) \in \Omega^{0, 2}(X, \fg)$ has cube $\Omega^{0, 6}(X) = 0$ and
the Zumino-$Q_5$-form evaluates identically to zero. The genuine
frontier is the Atiyah--Kapranov coupling:
two local chain-level representatives
$\kanom^{\mathrm{cons}}, \kanom^{\mathrm{cov}}$ of the Costello--Li 2016
Prop.\ 5.2 one-loop anomaly plus
$\mathrm{BZ}^{\mathrm{hol}}$ intertwiner, built from the Kapranov 1999
*Compositio Math.* 115 §4 cubic $L_\infty$-bracket
$\ell_3 \colon \Omega^{0, \bullet}(X, T_X)^{\otimes 3} \to
\Omega^{0, \bullet + 1}(X, T_X)$ coupled to $d^{abc}(\fg)$ via the
Atiyah class $\mathrm{At}(T_X)$. The abelian fragment
$\fg = \fu(1)$ is State A trivially (both anomaly representatives
vanish; identity is $0 = 0$).

**B09. Stage-2 rank reduction $24 \to 3$ on $K3 \times E$.** Closure
C18. The honest Stage-2 identity is
$\mathrm{rk}_{\mathrm{Cartan}}(\mathfrak{g}_{\Delta_5}) = 3$ via
Hodge-filtration projection of the Mukai lattice onto its rank-1
polarisation sublattice plus cycle-class contraction against $E$;
numerical coincidence with $c_+(\widetilde{\Lambda}(K3)) - 1 = 3$ is
not the mechanism. The chain-level theorem is unconditional (Wave 13
B4 Cycle 3, Heal `heal:lattice`); State B on the $(\infty, 1)$-lane
Stage-2 $\SpCh_{K3, E}$-functoriality at $d = 3$ on Fourier-Mukai
kernels remains a sub-case of Conjecture
`conj:phi-d-functoriality`.

## State-C ledger (genuine frontier --- new primary-source theorem required)

Every C-row names the specific theorem that does not exist in the
published literature.

**C01. Integral $E_d$-formality at $d \geq 3$.** Closure C09. Over
$\Q$, Kontsevich--Tamarkin + Willwacher gives formality as a
$\mathrm{GRT}_1(\Q)$-torsor. Over $\Z$, the torsion in
$\pi_*(\mathcal{E}_d^{\mathrm{top}})$ obstructs: at $d = 3$ the first
obstruction is the Hopf invariant $\Z/2 \subset \pi_5(S^2)$. Three
candidate extensions (G1 Fresse 2017 Vol.\ I Thm.\ 12.3.A to integral
coefficients; G2 torsion computation in graph-complex automorphism
group; G3 Tamarkin--Willwacher integral uniqueness theorem), none in
the literature. Consequence: at $d \geq 3$, Stage-1 object
$\Phi^{\mathrm{FA}}_d(\mathcal{C})$ is canonical only up to rational
quasi-isomorphism and a $\mathrm{GRT}_1(\Q)$-torsor; strict chain-level
identification of the topological $E_d^{\mathrm{hol}}$-algebra of
holomorphic Chern--Simons observables with the algebraic $E_d$-algebra
of the Gerstenhaber bracket on $\HH^\bullet(\mathcal{C})$ is unavailable
over $\Z$.

**C02. $(\infty, 1)$-functoriality of $\Phi^{\mathrm{FA}}_d$ on non-formal
CY categories at $d \geq 3$.** Closure C10. Object-level Stage-1
canonicality holds on the non-formal locus (local $\PP^2$, resolved
Gepner-point quintic, Ginzburg-potential quivers with $m_3 \neq 0$;
Wave 1 A01 Theorem T1 rational lane). Morphism-level
$(\infty, 1)$-functoriality degrades to an $(\infty, 1)$-correspondence
controlled by a non-trivial $\mathrm{GRT}_1$-torsor whenever at least
one side is non-formal. The conjectured obstruction vanishing at
local $\PP^2$ reduces to a pairing between the Kontsevich wheel-class
$\mathrm{wh}_3 \in \mathfrak{grt}_1$ and the Atiyah class
$\mathrm{At}(T_X) \in H^1(X, \Omega^1_X \otimes \End T_X)$, non-trivial
because local $\PP^2$ is not HKR-formal. Closing this requires a
chain-level rigidification of the Grothendieck--Teichmuller action on
formality quasi-isomorphisms of $E_3$-algebras enhanced with a
non-degenerate cyclic pairing of degree $-3$, plus a homotopy-transfer
formula morphism-lifting Willwacher 2014 *Invent.\ Math.* 200 from the
universal $E_d$-formality torsor to the morphism-lifting torsor.

**C03. Costello--Paquette boundary $S_3$-equivariance: outer-automorphism
groupoid.** Closure C03 + 3B-C03. The three Costello--Paquette
factorisation algebras
$\mathrm{Obs}_{\partial \hCS_5}^{(\epsilon_i)}$ live on three distinct
Ran spaces $\mathrm{Ran}(\C_{\epsilon_i})$; the symmetric group $S_3$
acts by outer-automorphism identifications
$\Phi_\sigma \colon
\mathrm{Obs}_{\partial \hCS_5}^{(\epsilon_i)} \to \sigma^*
\mathrm{Obs}_{\partial \hCS_5}^{(\epsilon_{\sigma(i)})}$ between
different factorisation algebras on different Ran spaces, rather than
by automorphisms of any single one. The holomorphic-topological twist
defining $\hCS_5^{(\epsilon_i)}$ irreducibly breaks the pre-twist
$SO(7)$ of the 11D M-theory origin (Costello 2017 arXiv:1705.02500
Thm.\ 8.1). Closing requires one of: (i) $S_3$-equivariant BV
quantisation at the 11D level, (ii) direct cocycle check via
Feynman amplitudes, (iii) staged $SO(7)$-descent. None in the literature.
The shuffle-envelope side (B04 above) is unconditional on a single
Ran space, so the two branches realise Miki's $S_3$ through different
categorical structures (Pattern 236 lane discipline).

**C04. Non-CHL $N = 7$ order-$4$ central extension of $\mathrm{Mp}_4$
by $\mu_4$.** Closure C12. At $N = 7$, $\varphi(7) = 6 \nmid 2$ excludes
Nikulin-admissibility. The would-be weight-$7/4$ paramodular form
$\Delta_{1/4}^{(7)}$ on a central extension
$1 \to \mu_4 \to G^{(7)} \to \mathrm{Mp}_4(\Z) \to 1$ requires three
new primary-source theorems: (1) existence of seed weight-$7/4$
cusp form $g_7 \in M_{7/4}(\Gamma_0(7), \chi_7)$ on the spin double
cover $\widetilde{\mathrm{SL}_2}(\Z)$ (cited Freitag--Hermann 1985
§II.5 Tab.\ 7.2 is misassigned; the reference handles the genus-two
$\widetilde{\mathrm{Mp}}_4$ cover, not weight-$7/4$ on $\Gamma_0(7)$);
(2) weight-$1$ Niwa preimage $g_7^{\mathrm{Niwa}} \in S_1(\Gamma_0(28),
\chi_7)$; (3) Shimura 1975 cohomology-obstruction resolution:
$H^2(\mathrm{Sp}_4(\Z), \Z/4) \simeq \Z/2$ obstructs a non-split
$\mu_4$-extension of $\mathrm{Sp}_4$, forcing $G^{(7)}$ to be a further
$\Z/2$-extension of $\mathrm{Mp}_4$ via a class in
$H^2(\mathrm{Mp}_4(\Z), \Z/2)$ not computed at level $K(7)$.

**C05. Mordell--Weil $\leftrightarrow$ real-simple-root
commensurability of $\mathfrak{g}_{F^{(5)}, \PP^1}$ with
$\mathfrak{g}_{\Delta_5}$.** Closure C15 + 3B-C02. The original $\rho
= 20$ target (C02-original) is retired by C16 (A10 above); the
surviving $F^{(5)}$ signature-$(2, 18)$ ambient is non-unimodular
with discriminant form of exponent $5$. Three options remain: (1)
finite-index unimodular super-lattice completion (yields a different
Borcherds lift, not commensurability); (2) common ambient on
$\widetilde{\Lambda}_{K3} = U^{\oplus 4} \oplus E_8(-1)^{\oplus 2}$ of
signature $(4, 20)$ (C15 G3-hypothesis; required automorphic form on
$\mathcal{G}(\widetilde{\Lambda}_{K3})$ lies outside Scheithauer 2006
*Invent.\ Math.* 164 Thm.\ 3.1 singular-weight reflective classification
at signature $(2, n)$); (3) Borcherds--Hecke correspondence at level 5
via Bruinier 2002 §5 + Scheithauer 2004 *J.\ Reine Angew.\ Math.* 567.
None executed in primary literature.

**C06. SCFT-level moduli-stack morphism
$\mathcal{M}_{\mathrm{ell\,K3}} \to \mathcal{M}_{c_{4d}}$.** Closure
3B-C19. The terminal codomain $\mathcal{M}_{c_{4d}}$ (the moduli stack
of 4D $\mathcal{N} = 2$ class-$\mathcal{S}$ SCFTs with fixed central
charge) has no published mathematical definition as of April 2026. The
obstruction is **structural**, not technical: the object is undefined,
not unproven. Four partial shadows exist --- Hitchin moduli
(Hitchin 1987; Coulomb shadow), Beem--Rastelli chiral algebras
(BLLPRvR 2013; Schur/VOA shadow), Freed--Teleman defect TQFTs
(Freed--Teleman 2014; categorical, conditional on 6D $(2,0)$
construction), Ben-Zvi--Sakellaridis--Venkatesh relative Langlands
(2024; Hamiltonian $G$-space shadow) --- but none supplies the stack
itself. Two paths to A remain open: (i) mathematical construction of
the 6D $(2,0)$ theory as a relative field theory; (ii) BSV-RLD
extension to 4D $\mathcal{N} = 2$ SCFTs. The
monodromy-level sub-composite (A06 above) is functorial and suffices
for the $(g, n) = (0, 24)$ selection.

**C07. Holomorphic Bardeen--Zumino Atiyah--Kapranov construction.**
Closure 3B-C04 = B08 above, viewed as frontier declaration (the
Zumino-$Q_5$ construction is ruled out by bidegree; the replacement
via Kapranov 1999 cubic $\ell_3$ bracket coupled to $d^{abc}$ via
$\mathrm{At}(T_X)$ is conjectural). The abelian fragment is State A
trivially (empty identity $0 = 0$).

**C08. Bracket-level $Y^+(X) \simeq \mathfrak{g}_{\mathrm{FM}}$ at
$d = 5$ on $K3 \times K3 \times E$.** Closure C21 downstream F1.
Extension of Schiffmann--Vasserot 2013 beyond $d = 3$ required; not
addressed in any published paper. Parallels the $d = 2$ open
identification $Y^+(K3) \simeq \mathfrak{g}_{K3}$ which is itself
conjectural.

**C09. Closed-form match $Z^{\mathrm{red, red}}_{\mathrm{DT}}(X) =
1/\Phi_{12}$ on $K3 \times K3 \times E$.** Closure C21 downstream F2.
Extension of Oberdieck 2018 *Invent.\ Math.* 213 arXiv:1706.10100 Thm.\ 1
required. Parallels B02 above at the DT-integrand rather than CoHA-character
level.

**C10. Gritsenko--Clery 2018 Conjecture 5.1 at $t \geq 4$.** Closure
3B-C13. The full Nikulin cone at signature $(1, t \geq 4)$ is
uncountably infinite; no exhaustive verification is possible, and no
uniform chain-independence theorem is in the literature.

**C11. Per-sibling bracket-level identification of the $23$ umbral
Stage-3 outputs with CDH BKM superalgebras $\mathfrak{g}^{(\Lambda)}$.**
Closure 3B-C30 F1. Requires the $d = 5$ extension of Schiffmann--Vasserot
applied to the $23$-fold family of Niemeier slices. Parallels C08
parametrised by Niemeier orbits.

**C12. Dunn--Lurie cyclic-$A_\infty$-triviality of $[2m]$-shifts on
chiral bar complex at $m \geq 2$.** Closure 3B-C08 (Gap G2 sub-item
of B03). Costello 2007 handles $m = 1$ with cyclic degree $d = 2$;
the extension to higher multiples of the CY dimension via
Kontsevich--Soibelman 2006 *Notes on $A_\infty$-algebras* §10 cyclic
cocycle is not constructed for K3 chiral algebras.

**C13. Nakajima--Baranovsky CY$_3$ direct threefold
principal-component correspondence algebra on
$\mathrm{Hilb}^n_{\mathrm{prin}}(K3 \times E)$.** Closure C23 + 3B-C23.
**Reclassified from State B to State C by the 3B-C23 Opus 4.7 relaunch
closure.** Goettsche-product side (A19 above) is unconditional: the
cohomology of the principal component decomposes as $V^{K3} \otimes V^E$,
the affine Yangian $Y(\widehat{\mathfrak{gl}}_1)$ acts via
Schiffmann--Vasserot 2013 on the K3 factor tensored with Grojnowski 1996
on the elliptic-curve factor, and Dunn--Lurie $E_1 \otimes E_1 \simeq E_2$
assembles the two factor-wise Heisenberg $E_1$-structures into an
$E_2$-algebra structure on the indirect (Goettsche-product) side. The
**direct threefold-side** promotion --- constructing threefold
correspondence cycles $P^n_k(X) \subset \mathrm{Hilb}^{n+k}_{\mathrm{prin}}(X)
\times \mathrm{Hilb}^n_{\mathrm{prin}}(X)$ and verifying the Heisenberg
commutator $[P_k, P_l] = k \delta_{k + l, 0} \cdot \mathrm{id}$ on
$V^X$ directly (without the Goettsche pullback) --- is **genuine
frontier**, requiring three independent inputs absent from every
published primary source through 2026.

- **(R1) Irreducibility and expected dimension $3n + k$ of the
  threefold correspondence subvariety $P^n_k(X)$ on the CY$_3$
  principal component.** Baranovsky 2000 *Math.\ Res.\ Lett.* 7
  Thm.\ 1 is surface-restricted (dimension two), and no published
  theorem establishes the analogous irreducibility / dimension
  statement on the CY$_3$ principal component, where punctual
  Hilbert schemes exhibit positive-dimensional families of
  non-curvilinear ideals starting at $n = 4$ (Iarrobino 1972
  *Invent.\ Math.* 15 Thm.\ 2).
- **(R2) Threefold tangent-normal Heisenberg commutator computation
  inside the principal component.** Nakajima's 1997 *Ann.\ Math.*\
  145 Thm.\ 3.10 surface-Lagrangian-Euler-class argument fails
  structurally on CY$_3$: the ambient
  $\mathrm{Hilb}^{n+k}_{\mathrm{prin}}(X) \times
  \mathrm{Hilb}^n_{\mathrm{prin}}(X)$ has complex dimension
  $3(n + k) + 3n = 6n + 3k$, which for odd $k$ admits no holomorphic
  symplectic structure (parity obstruction to non-degenerate skew
  forms), whereas the Lagrangian intersection input relies on
  holomorphic-symplectic half-dimension geometry. A threefold
  tangent-normal intersection computation replacing the surface
  Lagrangian-Euler-class argument must be constructed; no such
  computation exists in the primary literature. The parallel virtual
  DT identities (Li 2001 *Geom.\ Topol.* 13 Thm.\ 0, Okounkov--
  Pandharipande 2010 *Geom.\ Topol.* 14 Thm.\ 1) are numerical in
  $\Z[[q]]$, not Heisenberg constructions on topological cohomology;
  at the unrefined level the total-space Euler characteristic
  vanishes ($\chi(\mathrm{Hilb}^n(K3 \times E)) = 0$ via Cheah 1996 +
  $\chi(K3 \times E) = 0$), forcing the topological Heisenberg
  character to zero and ruling out any non-trivial direct-threefold
  Heisenberg at the unrefined level.
- **(R3) Compatibility of the threefold convolution operators with the
  Goettsche pullback $P^{\mathrm{Nak}}_k(K3) \otimes P^{\mathrm{Sym}}_k(E)$.**
  The direct-threefold $P_k$ operators (if constructed via R1, R2)
  must agree with the tensor product of Nakajima surface operators
  and Grojnowski symmetric-product operators under the Goettsche
  identification. This compatibility is stronger than the Goettsche
  product on cohomology alone; it requires matching the fundamental
  classes of correspondence subvarieties under the Goettsche
  identification. Not established in any published primary source.

Nakajima 1999 *Lectures on Hilbert Schemes of Points on Surfaces*, AMS
University Lecture Series 18, Chapter 9 end-of-chapter remark, explicitly
flags this threefold extension as an open problem: on threefolds the
correspondence subvariety is neither smooth at non-reduced configurations
nor Lagrangian in any holomorphic-symplectic sense. Dunn--Lurie
additivity (Lurie *HA* Thm.\ 5.1.2.2; Dunn 1988 *J.\ Pure Appl.\ Algebra*
50) operates at the $\infty$-operadic level on $E_n$-algebras,
assembling two already-existing $E_1$-inputs into an $E_2$-output
(used on the Goettsche-product side in U4 / A19); it does **not**
construct the missing $E_1$-input on the direct threefold side. The
gap G1.b (non-Lagrangian threefold correspondence) blocks the
construction of the input $E_1$-algebra on the direct threefold side,
and Dunn--Lurie cannot be applied until that input exists. Dunn--Lurie
is downstream of the obstruction, not a route around it.

Cache 22S three-composite-input discipline is exemplified at the
threefold level: invoking Baranovsky alone ignores the need for a
threefold tangent-normal argument replacing the surface Lagrangian
input. AP-CY271 / AP-CY285 discipline (six routes to
$G(K3 \times E)$ = six different constructions) applies: the
Hilbert-scheme route via Goettsche / Nakajima-Lehn is one route;
the DT / KS CoHA route with a Jordan-triple potential is another;
they do not merge through Nakajima-Baranovsky alone. The conjectural
status at the direct threefold scope is consistent with and reinforced
by `conj:k3y-nakajima-lehn-hilbert-programme` at
`chapters/examples/k3_yangian_chapter.tex` line 9648, which already
carries `\ClaimStatusConditional`. The Goettsche-product scope,
restated tightly, carries `\ClaimStatusTheorem` (A19 above). No
promotion to `\ClaimStatusTheorem` is warranted at the direct threefold
scope.

## Cross-volume dependencies

The Vol III programme is harmonised with Vol I and Vol II at five
load-bearing junctures; every juncture has a primary-source anchor
and a recorded cache entry.

**X01. Vol I shared five-theorem core.** Theorems A (bar--cobar),
B (chiral Positselski), C (derived-centre complementarity on the
$\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$ ceiling), D
(obstruction-tower universality), H (Hochschild concentration) are
stated at shared scope. Vol III contributions: the $\mathsf{B}$-row
$K^\kappa = 8$ witness $\mathcal{H}_{\mathrm{Muk}}(K3)$ carries the
Mukai doubling $2 c_+(\widetilde{\Lambda}(K3)) = 8$ and satisfies the
anomaly-ratio bridge $K^\kappa = \varrho K$ with $\varrho = 1/6$,
$K = 48$, $K^\kappa = 8$ (Vol I Prop.\ `prop:archetype-complementarity-bridge`,
resolved at C25). The $\mathcal{B}$-family scope is
Lorentzian-lattice-parametric, not universal.

**X02. Vol I cache C4 three-factor universal trace ladder correction.**
Closure F-META-2. Vol I `appendices/first_principles_cache.md` line 494
(entry C4) and `FRONTIER.md` line 15 attach the three-factor identity
$\mathrm{tr}_{\mathrm{ghost}}(Q_{\mathrm{BRST}}^2) = \mathrm{tr}_{\mathrm{Pentagon}}
= \omega_{\mathrm{Borcherds}} = c_N(0)/2$ to a numerical ladder at the
CHL slice $N \in \{1, 2, 3, 4, 6\}$. The ladder is corrected to
$(5, 2, 1, 1, 1)$ (A02 above; unique across the programme), making
Vol I entries C3 and C4 numerically consistent for the first time.
Vol II Pentagon-trace middle factor, Vol III Borcherds-weight right
factor, Vol I BRST-ghost left factor all equal the same arithmetic
$c_N(0)/2$ on the Koszul-self-dual subcategory cut out by Theorem B.

**X03. Vol II 3D HT QFT $\mathsf{SC}^{\mathrm{ch, top}}$ at $d = 3$.**
The $E_3^{\mathrm{hol}}$-BV shift-law row $(3, -1, E_3^{\mathrm{hol}}\text{-BV})$
of Vol III A03 is the same row that Vol II
`~/chiral-bar-cobar-vol2/CLAUDE.md` records as the 3D HT QFT scope.
The Stage-1 object $\mathcal{F}_{K3 \times E} = \Phi^{\mathrm{FA}}_3(
D^b\mathrm{Coh}(K3 \times E))$ is simultaneously a Vol III chain-level
holomorphic factorisation algebra and a Vol II 3D HT QFT boundary
observable; consistency under the Costello--Gwilliam BV assembly is
proved unconditionally at B (Costello--Li 2016; A04 above and
Costello--Gwilliam 2017 Vol.\ II Thm.\ 9.5.0.6).

**X04. Vol I shared canonical formulas in `landscape_census.tex`.**
The seven-witness landmark $\{\mathcal{H}_k, \widehat{\fg}_k,
\beta\gamma_\lambda, \mathrm{Vir}_c, \mathcal{W}_3^k, \mathrm{BP}_k,
\mathcal{H}_{\mathrm{Muk}}(K3)\}$ of Theorem C with central-charge
complementarity $c + c^! \in \{0, 2 \dim \fg, 0, 26, 100, 196, 48\}$
and conductor values $K^\kappa \in \{0, 0, 0, 13, 250/3, 98/3, 8\}$
is shared between Vol I and Vol III. The level-independence hypothesis
$\varrho(A) = \varrho(A^!)$ is the single bridge to the ceiling formula.
A15 (C25) verifies Vol I hosts the full proof; Vol III inherits
unconditionally.

**X05. Vol III cache anchors.**
`appendices/first_principles_cache.md` (Vol III) registers:
$\kappa_{\mathrm{cat}}(K3 \times E) = 0$ (Kunneth-multiplicative total
space, not $2$ which is the K3 fibre); $\mathrm{CoHA}(\C^3) = Y^+$
(positive half, not $\mathcal{W}_{1+\infty}$ full); six routes to
$G(K3 \times E)$ are six DIFFERENT constructions, not six $\Phi$
applications; $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} +
\chi(\mathcal{O}_{\mathrm{fiber}})$ is FALSE numerically at every
$N \in \{1, 2, 3, 4, 6\}$; Class M $E_3$ bar $= 6^g$ at cohomology, not
infinite; at $d \geq 3$, $A$ is $E_1$ and $E_2$ lives on
$Z(\mathrm{Rep}(A))$, not on $A$. Cache 22S three-composite-input
discipline for $\{H^\ast_T(\mathrm{Hilb}^{[n]}(K3))\}$ pro-limits
exemplified at the threefold level in C13 above. These anchors
discipline every Wave 3 closure above.

## Secondary rectifications (recorded Wave 3 repairs)

Three Wave 3 closures execute A-type rectifications that are not new
mathematics but value-correction or scope-sharpening on existing
statements:

**R01.** Wave 2 three-faces-of-$8$ theorem split (3B-C28 = A18).
**R02.** CoHA treatise Strategy-3 principal-component qualifier
(3B-C29 = A16).
**R03.** Vol I cache C4 + FRONTIER.md ladder correction
$\{5, 4, 3, 2, 2\} \to \{5, 2, 1, 1, 1\}$ (F-META-2 = X02).

## Residual frontier map (one-line summary per item)

A-rows (19): BCFG all-orders (A01), single CHL ladder (A02),
dimension-stratified GKM census (A03), compact CY$_3$ 3-dualisability
+ $(\infty, 3)$-TFT (A04), Schur index to $q^{10}$ (A05),
$\Sigma_{0, 24}$ monodromy-level selection (A06), Leech primitive
embedding into tensor-product Mukai (A07), three-stage $\Phi_5$ on
$K3^2 \times E$ (A08), 23 umbral Stage-3 siblings (A09), Weierstrass
obstruction ($\rho = 20$ target retired) (A10), Borcherds lift on
$F^{(5)}$ at $(2, 18)$ (A11), Enriques fourth witness (A12),
rank-$\leq 4$ $\mathfrak{g}_L$ family (A13), $C_2$-vs-$d^{abc}$
separation (A14), archetype bridge (A15), CoHA treatise
principal-component rectification (A16), CLAUDE.md two-scope
reconciliation (A17), Wave-2 three-faces split (A18),
Goettsche-product side affine-Yangian on
$V^{K3} \otimes V^E$ (A19).

B-rows (9): Bruinier--Mukai reciprocity (B01 / BrukaMilk),
Fake-Monster DT = $1/\Phi_{12}$ (B02 / MPT$^{\otimes 2}$ + JFI-Leech),
three-faces-of-$8$ unification (B03 / Dunn--Lurie Serre-CM lift),
Ran-level Miki $S_3$ shuffle envelope (B04 unconditional),
$\mathfrak{g}_{\mathrm{BPS}} \simeq \mathfrak{g}_{\Delta_5}$ (B05 /
(HB) imaginary-root scope), $F^{(5)}$ MW-indexed real simple roots
(B06 / (H$_\sigma$)), rank-$\geq 5$ $\mathfrak{g}_L$ (B07 /
Gritsenko--Clery Conj.\ 5.1), Bardeen--Zumino $L_\infty$ (B08 /
Atiyah--Kapranov construction), Stage-2 rank reduction (B09 /
Fourier--Mukai functoriality).

C-rows (13): integral $E_d$-formality at $d \geq 3$ (C01),
$(\infty, 1)$-functoriality on non-formal at $d \geq 3$ (C02),
Costello--Paquette $S_3$-outer-automorphism groupoid (C03),
non-CHL $N = 7$ $\mu_4$-extension (C04), MW--$\Delta_5$
commensurability on common ambient $\widetilde{\Lambda}_{K3}$ (C05),
SCFT-level class-$\mathcal{S}$ moduli stack (C06), Atiyah--Kapranov
BZ (C07), $d = 5$ bracket-level $Y^+(X) \simeq \mathfrak{g}_{\mathrm{FM}}$
(C08), closed-form $Z^{\mathrm{red, red}}_{\mathrm{DT}} = 1/\Phi_{12}$
(C09), Gritsenko--Clery Conj.\ 5.1 at $t \geq 4$ (C10), per-sibling
bracket-level identification of the 23 umbral outputs with CDH BKMs
(C11), cyclic-$A_\infty$ $[2m]$-shift triviality at $m \geq 2$ (C12),
Nakajima--Baranovsky CY$_3$ direct threefold principal-component
correspondence (C13 / R1-R3).

Cross-volume bridges (5): Vol I shared five-theorem core (X01), Vol I
cache C4 ladder rectification (X02), Vol II 3D HT QFT shift-law row
(X03), Vol I `landscape_census.tex` canonical formulas (X04), Vol III
cache anchors (X05).

## Primary-source count (Wave 3 aggregate)

Seventy-one distinct primary sources cited with volume/year/theorem
across the 43 Wave 3 files: Borcherds 1990 (FM), 1992 (Monster), 1995,
1998; Gritsenko 1994, 1999 (two papers); Gritsenko--Nikulin 1997, 1998;
Gritsenko--Clery 2008, 2013, 2015, 2018; Scheithauer 2004, 2006, 2009
(two papers), 2017; Bruinier 2002, 2014; Bruinier--Funke 2004;
Bruinier--Kuss 2001; Bruinier--Yang 2006; Howard--Madapusi-Pera 2020;
Kudla--Millson 1986, 1990; Ma 2018; Dittmann--Ma--Scheithauer 2021;
Moller--Scheithauer 2023; Wang--Williams 2023; Eichler--Zagier 1985;
Cheng--Harrison--Paquette--Volpato 2014; Eguchi--Ooguri--Tachikawa 2011;
Cheng--Duncan--Harvey 2014; Duncan--Griffin--Ono 2015;
Costello 2011, 2013, 2017; Costello--Li 2016; Costello--Gaiotto 2018;
Costello--Paquette 2020; Costello--Dimofte--Paquette 2021; Costello--Gwilliam
2017 (Vols.\ I and II); Gwilliam--Williams 2021; Francis 2013;
Ayala--Francis 2015; Lurie 2009, *HA*; Willwacher 2014;
Kapranov 1999; Kapranov--Vasserot 2019; Kontsevich 1999;
Tamarkin 2003; Kontsevich--Soibelman 2006, 2008; Fresse 2017;
Pantev--Toen--Vaquie--Vezzosi 2013; Calaque--Pantev--Toen--Vaquie--Vezzosi 2017;
Ben-Zvi--Francis--Nadler 2010; Ben-Zvi--Sakellaridis--Venkatesh 2024;
Gaitsgory--Lurie 2014; Beilinson--Drinfeld 2004;
Schiffmann--Vasserot 2013; Negut 2014; Miki 2007;
Feigin--Jimbo--Miwa--Mukhin 2016; Tsymbaliuk 2017;
Feigin--Hashizume--Hoshino--Shiraishi--Yanagida 2009;
Drinfeld 1985, 1990; Etingof--Kazhdan 1996--2008; Lusztig 1990;
Davison 2017; Davison--Meinhardt 2020; Oberdieck--Pixton 2018;
Oberdieck 2018; Nakajima 1997, 1999; Baranovsky 2000;
Li 2001; Okounkov--Pandharipande 2010; Li--Qin--Wang 2004;
Gottsche 1990; Grojnowski 1996; Fogarty 1968; Iarrobino 1972; Cheah 1996;
Nikulin 1979; Mukai 1987, 1988; Shioda 1990, 2007; Schutt--Shioda 2019;
Nishiyama 1996; Kuwata--Kumar 2017; Huybrechts 2006, 2016;
Conway--Sloane 1988; Niemeier 1973; Venkov 1980; Kac 1990;
Guay--Nakajima--Wendlandt 2018; Bridgeland--Maciocia 2001;
Silverman 1986, 1994, 2009; Allcock 2000; Kondo 1994; Hashimoto 2012;
Mukai 1988 (Enriques); Morrison--Vafa 1996 (II);
Sen 1996; Gaiotto 2012; BLLPRvR 2013;
Beem--Peelaers--Rastelli 2014; Gadde--Rastelli--Razamat--Yan 2011, 2013;
BLPR 2015; Beem--Lemos--Liendo--Peelaers--Rastelli--van Rees 2013;
Diaz--Edidin 1996; Bertin--Romagny 2011; Frenkel--Ben-Zvi 2004;
Apostol 1990; Chevalley--Eilenberg 1948; Hartshorne;
Griffiths--Harris 1978; Demailly 2012; Gilkey 1995; Deligne 1970, 1971;
Paquette--Persson--Volpato 2016; Cheng--Harrison 2015;
Kawai--Yoshioka 2000; Gannon 2016; Schauenburg 1998;
Manes--Stora--Zumino 1985; Zumino 1983; Bardeen--Zumino 1984;
Harvey--Moore 1996; Kudla 1986; Freitag--Hermann 1985;
Freed--Teleman 2014; Arinkin--Gaitsgory 2015; Tamarkin 2000, 2007;
Feigin--Frenkel 1991; Bondal--Orlov 2001; Feigin--Gan--Ginzburg 2014;
Levine--Pandharipande 2009; Maulik--Pandharipande--Thomas 2010;
Bryan--Oberdieck 2019; Shimada 2001; Roulleau--Garbagnati-Salgado 2021;
Braun--Kimura--Watari 2015.

## Closing remark on the crystallisation

The Vol III programme at end of Wave 3 stands on 19 unconditional
theorems (State A), 9 conditionally-closed theorems each reducible to
a single primary-source extension (State B), 13 genuine open frontiers
each naming the missing theorem (State C), and 5 cross-volume bridges
keeping the shared five-theorem core, Vol I/Vol II/Vol III cache
numerics, and the Beilinson-dictum ``every claim false until
independently verified'' discipline in consistent superposition. The
monodromy-level selection of $\Sigma_{0, 24}$, the Mukai-doubling
ceiling $K^\kappa = 8$ on the $\mathcal{B}$-row, the universal
Borcherds-weight identity $\kappa_{\mathrm{BKM}} = c(0)/2$, and the
single CHL ladder $(5, 2, 1, 1, 1)$ with three compatible primary lifts
now form the inner music of the manuscript; every Wave 3 closure
either sharpens or discharges an earlier residual frontier item. The
eight open structural frontiers requiring new mathematics (C01 integral
$E_d$-formality; C02 non-formal $(\infty, 1)$-functoriality; C03
Costello--Paquette $S_3$ outer-automorphism groupoid; C04 non-CHL
$N = 7$ $\mu_4$-extension; C05 common Mukai-ambient
MW--$\Delta_5$ correspondence; C06 SCFT moduli stack; C10
Gritsenko--Clery Conj.\ 5.1 at $t \geq 4$; C13 Nakajima--Baranovsky
CY$_3$ direct threefold principal-component correspondence with
R1-R3) constitute the precise list of named theorems whose proof would
advance the programme to its Platonic ideal.

The 3B-C23 reclassification from State B (conditional on a single
Dunn--Lurie hypothesis) to State C (genuine frontier with three
required inputs R1-R3) sharpens the precise structural obstruction:
Nakajima's Lagrangian-intersection argument on surfaces uses the
half-dimensional Lagrangian structure in a holomorphic-symplectic
ambient of even complex dimension, a property that fails on CY$_3$
principal components because the ambient product carries odd complex
dimension in half the cases and admits no holomorphic symplectic
structure in general. Li--OP virtual DT identities are numerical in
$\Z[[q]]$, not Heisenberg constructions on topological cohomology, and
the motivic-scalar shadow of the total Hilbert scheme Euler
characteristic vanishes identically. Dunn--Lurie additivity, contrary
to initial reading, is operadic-level machinery that assembles
two already-existing $E_1$-algebras into an $E_2$-algebra; it cannot
construct the missing $E_1$-input on the direct threefold side, only
combine two already-constructed ones on the indirect (Goettsche-product)
side. The Goettsche-product-side theorem (A19) is intact; the
direct-threefold-side promotion remains open.
