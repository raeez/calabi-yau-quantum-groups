# Anti-Pattern Catalogue (Vol III)

This note collects all CY-specific anti-patterns (AP-CY1 through AP-CY142; AP-CY141 single-valued MZV scope and AP-CY142 Humbert--Heegner admissibility filter added in Waves 28-29).

## Canonical values at the latest-wave verdict (2026-04-21)

When any entry in this catalogue or the first-principles cache appears
to assert one value while a later entry asserts another, the **latest
wave's verdict takes precedence**. The registry below pins the
canonical value for every quantity that has flipped at any point across
Waves 1-26. Every AP/cache entry that names an older value does so only
in retraction context (explicitly flagged as "wrong claim" / "old draft"
/ "retracted").

| Quantity | Canonical value (latest-wave verdict) | Retracted earlier values | Lock |
|---|---|---|---|
| $(c_{4d}, c_{2d})$ of $\mathcal T[A_1, \Sigma_{0, 24}]$ | $(107/6, -214)$ (Wave 15 Gaiotto) | $(26, -312)$ (Wave 14 error); $(23/4, -69)$ (Wave 25 Gaiotto agent error) | WOV-2 |
| Trinion/tube count at $n=24$ | $(n_v, n_h) = (63, 88)$ | $(21, 27)$ (Wave 25 confusion of trinion/tube count with multiplicities) | Chacaltana--Distler 2010 §5.14 |
| Universal $c_{4d}$ formula, $A_1$ genus 0 | $c_{4d} = (5n - 13)/6$ | $(12(g-1) + 7n)/6$ (Wave 14 error — fails $\mathrm{SU}(2)$ $N_f = 4$) | Shapere--Tachikawa 2008 |
| Monster BKM Cartan rank | $2$ (on $\mathrm{II}_{1,1}$) | $26$ (Wave 16 confusion with Fake-Monster) | Borcherds 1992 *Invent Math* 109 |
| Fake-Monster Cartan rank | $26$ (on $\mathrm{II}_{25,1}$) | --- | Borcherds 1992 |
| K3-BKM Cartan rank | $3$ (on $\Lambda^{2,1}_{II}$) | --- | Gritsenko--Nikulin 1998 §3 |
| $c_3$ (Borcherds coefficient) | $-8$ in Bruinier reduced-class convention | $176256$ (= $p_{24}(5)$, Wave 16 error; also the Gritsenko--Nikulin Cartan-matrix value with conversion factor $-22032$) | WOV-5 |
| $\zeta(3,3,3,3)$ numerical value | $0.000295999\ldots$ (depth-4, weight 12) | $0.0028565$ (Wave 17 draft, 10× error) | Brown 2012 motivic basis |
| $c(1, 2, \pm 2)$ heterotic lift coefficient | $-2$ (Wave 22 Witten) | $+1$ (Wave 21 error) | $\eta^{18} \theta_1^2$ direct expansion + DMZ 2012 + holomorphic-anomaly (three-path) |
| Humbert $H_4$ arithmetic description | $(2, 2)$-isogeny quotient of $E_1 \times E_2$ with $\mathrm{End} \supset \mathbb{Z}[2i]$; monodromy order 2 | $\mathbb{Q}(\sqrt 2)$-RM locus (Wave 15 imprecise; that is $H_8$, not $H_4$) | van der Geer 1988 Ch IX |
| Theorem B scope (Koszul locus) | $\overline{\mathcal A_2} \setminus \bigcup_{n \,\mathrm{admissible}} H_n$ (all admissible Heegner divisors) | $\overline{\mathcal A_2} \setminus (H_1 \cup H_4)$ (Wave 15 narrow) | Wave 18 Beilinson tightening |
| K3-BKM Weyl denominator | $\Delta_5 = \mathrm{Grit}(\eta^9 \vartheta_1) \in S_5(K(1))$ (additive) | $\Phi_{12}$ attempted (Fake-Monster, $\mathrm{II}_{25,1}$, multiplicative — different object) | Gritsenko 1999 Thm 6.1 |
| Umbral $A_{N-1}$ labelling rule | $(N-1) \mid 24$; at $N = 6$ reanchor to Niemeier $6 D_4$ | $N \mid 24$ (Wave 18 error) | Wave 19 Gaiotto |
| Leech lattice simple root norm | $2$; $r_\lambda = (\lambda; 1, 1 - \lambda^2/2) = (\lambda; 1, -1)$ at $\lambda^2 = 4$ | $6$ (Wave 24 Nekrasov formula error, using $r_\lambda = (\lambda; e + (\lambda^2 - 2)/2\,f)$) | Conway 1983 *Proc R Soc Lond A* 384; SPLAG Ch 27 |
| Fake-Monster Weyl vector | $\rho = e = (0_\Lambda; 1, 0)$ lightlike, $\rho_\Lambda = 0$ | Sign-inconsistent Wave-23 draft | Borcherds 1992 Thm 10.1 |
| $\Phi_{12}$ automorphic home | Orthogonal Shimura variety $\mathcal{D}_{\mathrm{II}_{26,2}} = O(26, 2)^+ / (O(26) \times O(2))$, complex dim 26, singular weight $12 = (26 - 2)/2$ | Siegel $\mathrm{Sp}_{26}(\mathbb Z)$ (impossible, $\mathbb H_{26}$ has dim 351); Jacobi-in-26-variables (no torus direction) | Borcherds 1992 |
| Restriction sublattice for $\Phi_{12} \to \Phi_{10}$ | Primitive $\mathrm{II}_{2,2} \hookrightarrow \mathrm{II}_{25,1}$, giving $O^+(\mathrm{II}_{2,2}) \cong \mathrm{Sp}_4(\mathbb Z)$ | $\mathrm{II}_{2,1}$ (Wave 23 error — sig $(2,1)$ carries no holomorphic modular form) | Gritsenko--Nikulin 1998 |
| Master $L$-value identification | $\log Z^{(1)}_{\mathbf H_{\Delta_5}} = -\log \Delta_5 - \kappa_{\mathrm{BGS}} \cdot L'(0, \Delta_5, \mathrm{std}) + \log C$, $\kappa_{\mathrm{BGS}} = 24$ | $L'(0, \Delta_{10}, \mathrm{ad}^0)$ (Wave 24 Costello — CAP-reducible, conflates three $L$-functions); $L'(0, \mathrm{ad}^0 \rho_{\Delta_{12}})$ (Wave 25 Gaiotto agent alternative, incompatible regulator) | Bruinier--Kühn 2003 Thm 4.11; Yoshikawa 2004 Thm 5.7 |
| Bloch--Kato Selmer on representation of $\mathbf H_{\Delta_5}$ deformation | $\dim H^1_f(\mathbb Q, \mathrm{std}\,\rho_{\Delta_5}) = 1$ (paramodular cyclotomic Hida family tangent) | $\dim H^1_f(\mathrm{ad}^0 \rho_{\Delta_{10}}) = 1$ (Wave 24 — right number, wrong representation; the adjoint spinor is rigid, dim 0) | Pilloni 2011 + Urban 2011 + Poor--Yuen 2015 + Thorne 2020 |
| Bridgeland $\dim \mathrm{Stab}(K3 \times E)$ | $48 = \mathrm{rk}\,\mathcal N(K3 \times E) = 24 \cdot 2$ | $26$ (Wave 23 claimed "codim-0 slice" — actual Künneth image has codim $22 = \mathrm{rk}\,T_{K3}$) | Bridgeland 2007 Thm 1.2 |
| Codim of $\mathrm{Stab}^\Phi$ inside ambient | $22$ | $0$ (Wave 23 error) | via four independent paths |
| Rank of $u_{\zeta_8}^{\mathrm{tilt}}$-mod | $162 = 27 \cdot 6 = (\ell' - 1)^3 \cdot \lvert S_3 \rvert$ | --- | Andersen--Polo--Wen 1994 |
| Structure of rank-$162$ MTC | $(A_1)_{k=2}^{\otimes 3} \rtimes S_3$ ($S_3$-crossed braided fusion) | $(A_1)_{k=2}^{\otimes 3} \boxtimes \mathbb Z[S_3]$ (Wave 23 tensor claim — $\mathrm{Vec}_{S_3}$ non-modular) | Turaev 2000; ENO 2010 |
| Conway $V^{s\natural}$ central charge | $c = 12$ | $c = 24$ (Wave 23 inherited from Monster error) | Duncan 2007 *Duke Math J* 139 |
| Conway $V^{s\natural}$ $\Psi$-placement | $\Psi^{\mathrm{metap}}$-image on metaplectic $\overline{\mathcal A_2^{(2)}}$ branch | Bosonic $\Psi$-image with $(K, \hbar^2) = (2, -1/2)$ (Wave 19/23 — Leech has no hyperbolic plane, universal identity out of scope) | Scheithauer 2008 |
| "Four is all" citation chain | Scheithauer 2017 + Dittmann--Ma--Scheithauer 2021 + Scheithauer 2006 (three papers) | Scheithauer 2017 alone (Wave 23/24 incomplete) | Scope: GN-reflective signature-$(2, n)$ with $n \ge 3$ |
| Fifth Borcherds product outside GN-scope | $24 A_1$ Niemeier product (Borcherds 1995 *Invent Math* 120 §13), reflective automorphic on sig-$(2, 24)$ singular weight 12 but fails GN-reflectivity (divisor non-rational-quadratic-hyperplane components) | --- | Borcherds 1995 |
| Pentagon admissibility congruence variable | $D_n = (n - 3)/2 \pmod 4 \in \{0, 1\}$, equivalently $n \equiv 3, 5 \pmod 8$ | $n \not\equiv 0, 3 \pmod 4$ (loose restatement) | Eichler--Zagier 1985 Thm 9.1 |
| Humbert--Heegner admissible $n \in [3, 36]$ | $\{3, 5, 11, 13, 19, 21, 27, 29, 35\}$ (nine values) | All Padovan-positive $n$ (loose) | Eichler--Zagier 1985 Thm 9.3 + Gritsenko--Nikulin 1998 |
| First admissible non-vanishing $\phi^{(n)}$ | $\phi^{(5)} = -2 \cdot [\mathrm{gen}]^{\otimes 5}$ | --- | Gritsenko--Nikulin 1998 Table 2 |
| Padovan $d_n$ reference table ($n \le 12$) | $(d_3, \dots, d_{12}) = (1, 0, 1, 1, 1, 2, 2, 2, 3, 4)$ with $d_n = d_{n-2} + d_{n-3}$, seeds $(1, 0, 1)$ | Fibonacci recurrence (AP-CY138) | Brown 2012 *Ann Math* 175 Thm 1 |
| $\phi^{(n)} \ne 0$ on K3-Humbert iff | (i) $n \equiv 3, 5 \pmod 8$ AND (ii) $d_n > 0$ AND (iii) $D_n \le 1$ (polar cutoff) | Padovan-only (AP-CY142) | Eichler--Zagier Thm 9.3; Gritsenko--Nikulin 1998 |
| $\Psi$-functor completeness | **Four** sibling functors $\{\Psi, \Psi^{\deg}, \Psi^{\mathrm{tor}}, \Psi^{\mathrm{metap}}\}$ (disjoint union surjective) | $\Psi$ alone surjective (Wave 23 claim falsified) | Baily--Borel--Freitag stratification of $\overline{\mathcal A_2}$ |
| $\mathrm{grt}_1^{(1/2)}$ extension status | Non-split, non-abelian, non-central (three distinct properties) | "Split because central" (Wave 24 conflation) | Lie $H^2_{\mathrm{Lie}}(\mathfrak q; \mathrm{grt}_1)$ via van Est transgression |
| Obstruction cohomology type | Lie $H^2_{\mathrm{Lie}}$ via van Est transgression from group $H^1_{\mathrm{grp}}$ (Saito--Kurokawa Eichler cocycle) | Group $H^1$ only (Wave 24 misattribution) | Costello--Gwilliam 2017 BV realisation |
| $[\widetilde\sigma_2, \widetilde\sigma_2]$ | $288 \widetilde\sigma_4$ via $\tau(2)^2 / 2 = 288$ | --- | $\tau(2) = -24$ |
| $e_5$ vs $W_5$ | $e_5 = W_5$ identically at every $c$ | --- | Wang 1998 *Prog Theor Phys* Prop 4.2 three-leg uniqueness |
| $e_4$ at $c = -214$ | $:T \partial^2 T: - (3/2):(\partial T)^2: + (321/10) \partial^4 T + \hbar\mathrm{qt}(J^{(4)})$; pairing $(65193/10) \mathrm{Vol}(E) (2\pi i)^4$ | --- | Pope--Romans--Shen 1990; Wang 1998 |
| Chiral-Hochschild $e_k$ motivic home | Single-valued $\mathrm{zv}^{\mathrm{sv}}_{3k}$ (Brown 2014; Schnetz 2013) | Full motivic $\mathrm{Per}^{\mathrm{mot}}_{3k}$ (Wave 23 naive Costello cross-cut) | BGS analytic torsion on Shimura varieties forces SV |
| Pseudo-character target | Chenevier 2014 determinant $D_{\Delta_{10}}$ of dim 4 | Pseudo-representation (loses mod-$\ell^n$ Cayley--Hamilton for reducible $\rho_{\Delta_{10}}$) | Chenevier 2014 *Ann Inst Fourier* 64 |
| Hecke field of $\Delta_{10}$ | $\mathbb Q$ (since $\dim S_{26}(\mathrm{SL}_2(\mathbb Z)) = 1$); minimal coefficient ring $\mathbb Z$ | --- | Standard |
| Humbert divisor / AD correspondence | Humbert divisor $= $ Argyres--Douglas point at $E_{\tau_1} \times E_{\tau_2}$ (SW curve degenerates to pair of elliptic curves → $(A_1, A_{2N-1})$) | --- | GMN 2009 *Adv Theor Math Phys* 13 Ex 8.3 |
| $\kappa_\bullet$ indexing (K3 $\times$ E) | Four distinct values: $\kappa_{\mathrm{cat}} = 0$ (multiplicative Künneth), $\kappa_{\mathrm{ch}}^K = 3$ (additive), $\kappa_{\mathrm{BKM}}$ family-specific, $\kappa_{\mathrm{fibre}}(K3) = 2$ | Naive "$\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal O_{\mathrm{fibre}})$" (fails for $N \ge 2$ — $N = 1$ accident only) | Always name the $\kappa_\bullet$ index |
| $\kappa_{\mathrm{BKM}}(\mathbf H_{\Delta_5})$ cross-volume value | **Pending AP5 lock** — Vol I abstract says 12, Vol III abstract says 5 (different $N$-index conventions for $c_N(0)/2$); every site must name the input denominator (Fake-Monster $\Phi_{12}$ vs paramodular $\Phi_{10} = \Delta_5^2$) | Both values occur in published inscriptions; resolve via landscape-census audit | Open AP5 audit |
| CoHA vs chiral-algebra type | $\mathrm{CoHA}_{K3 \times E}$ is $E_1$-associative (Hall product); chiralisation via $\Phi_3$-arrow gives $\mathbf H_{\Delta_5} = \Phi_3(\mathcal D_\hbar(\mathcal Y^{\mathrm{Hall}}(\mathrm{CoHA}_{K3 \times E})))$ | "CoHA is a chiral algebra" (type error) | Schiffmann--Vasserot + $\Phi_d$-functor framework |
| $\mathrm{CoHA}(\mathbb C^3)$ identification | $Y^+(\widehat{\mathfrak{gl}}_1)$ — the **positive half** of the affine Yangian | $W_{1+\infty}$ (classical limit only); full Yangian $Y$ | Schiffmann--Vasserot |
| $W_{1+\infty}$ vs $W_\infty[c]$ | $W_{1+\infty} = W_\infty[c] \otimes \mathcal H$ (Heisenberg); different objects | Conflating the two | Pope--Romans--Shen 1990 |
| Two-$\hbar$ discipline | $\hbar^{\mathrm{Drinfeld}} = 2\pi i / \ell$ (root-of-unity) vs $\hbar^{\mathrm{BV}}$ (loop-counting); semantically distinct but agree numerically at $\hbar^2 = -1/8$ for $\ell = 8$ | Using bare $\hbar$ without subscript | AP151 bridge |
| Bar cohomology class-$\mathbf M$ at $E_3$-level | $6^g$ (cohomological dim at $g \in \{1, 2, 3\}$; chain level is infinite) | "Infinite at cohomological level" | Wave 12 Vol III |
| $\kappa_{\mathrm{cat}}(K3 \times E)$ | $0$ (total space, Künneth multiplicative $\chi(\mathcal O_{K3}) \chi(\mathcal O_E) = 2 \cdot 0$) | $2$ (fiber only) | AP-CY68/AP234 discipline |

**Every cache/AP entry citing an older value must appear in a "Wrong
Claim" / "retracted" / "earlier draft" context. Any standalone assertion
of an older value is itself a latent AP violation; report it via
Gate 0 on sight.**


## Compatible dual readings (non-contradictions)

Some statements appear in different waves with apparently conflicting
framings yet describe the **same mathematical object** through two
compatible frames. An agent reading only one framing may mistake the
pair for a contradiction and attempt to "fix" one side, destroying
content. Every entry below is a certified **non-contradiction**: both
framings are correct simultaneously and reconcile through the named
mechanism. Do not flatten either reading. Do not treat this as an AP
retraction list; treat it as a frame-compatibility registry.

| Statement A (frame 1) | Statement B (frame 2) | Compatibility mechanism | Primary reference |
|---|---|---|---|
| Conway $V^{s\natural}$ is the $\Psi^{\mathrm{metap}}$-image on the metaplectic $\overline{\mathcal A_2^{(2)}}$ branch (canonical preamble, row 41). | Conway $V^{s\natural}$ is the $\mathbb Z/2$-super-twin of $V^\natural$ via Duncan's commutative orbifolding diamond (W20.2 healing). | Same VOA-super-algebra read from the $\Psi$-functor / $\overline{\mathcal A_2}$-stratification side and from the commutative-orbifolding-diamond side; the metaplectic $\Psi$-image equals the super-twin of the Leech CFT via the Duncan 2007 Frame-change. | Duncan 2007 *Duke Math J* 139; Scheithauer 2008. |
| $\kappa_{\mathrm{BKM}}(\mathbf H_{\Delta_5}) = 12$ (Vol I three-faces identity, Fake-Monster $\Phi_{12}$ input). | $\kappa_{\mathrm{BKM}}(\mathbf H_{\Delta_5}) = 5$ (Vol III Borcherds-weight count on paramodular $\Delta_5$). | Reconciled via W26.8: the two values index different input denominators ($\Phi_{12}$ vs $\Phi_{10} = \Delta_5^2$) under the same $c_N(0)/2$ rule. Each site must name the input denominator; the two are $(c_{\Phi_{12}}(0)/2, c_{\Delta_5}(0)/2) = (12, 5)$. | Borcherds 1992; Gritsenko 1999 Thm 6.1; canonical preamble row 57. |
| $e_4 = W_4 - (107/11)\Lambda_Z$ in the $W$-basis (Vol III abstract, $c = -214$). | $e_4 = {:}T\partial^2 T{:} - (3/2){:}(\partial T)^2{:} + (321/10)\partial^4 T + \hbar\,\mathrm{qt}(J^{(4)})$ in the Virasoro-composite basis (canonical preamble row 51). | Same cocycle class, two bases. Pope--Romans--Shen projection $W_k = e_k + (-c/22)\Lambda_Z$ converts between $W$-basis and Virasoro-composite basis; the scalar $-107/11 = c/22$ at $c = -214$ is the frame-change constant. | Pope--Romans--Shen 1990; Wang 1998 Prop 4.2. |
| Archetype $\mathbf B$ row: $\kappa + \kappa^! = 8$ (Vol I five-archetype table, $r(z)$-families). | K3 Mukai pairing $K = 2c_+ = 8$ (Vol III Mukai form on $\Lambda^{3,19}$). | Three faces of the same canonical $K = 8$: (i) derived-centre complementarity sum $\kappa + \kappa^!$; (ii) Mukai pairing $K = 2c_+$ with $c_+ = 4$; (iii) Lusztig reflection length $\ell_{\mathrm{Lusztig}} = 8$ at $\zeta_8$. All three equal $8$ because $K3 \times \mathrm{elliptic}$ pairs with $\mathbf H_{\Delta_5}$ through a single self-dual lattice indexing. | Borcherds--Mukai pairing; Lusztig 1989 at $\zeta_8$; Gritsenko--Nikulin 1998. |
| Padovan counts $d_n = d_{n-2} + d_{n-3}$ give MZV basis dimensions in weight $n$ (Brown 2012 conjecture). | Humbert-Heegner divisor filter selects arithmetically admissible $n \equiv 3, 5 \pmod 8$ on $\phi^{(n)}$ (Vol I / Vol III pentagon admissibility row). | Orthogonal filters. Padovan counts basis vectors; Humbert-Heegner selects admissible embedding points. The two do not compete: Padovan $d_n$ governs the motivic dimension; Humbert-Heegner governs the arithmetic non-vanishing locus. Compatible because $\phi^{(n)}$ lives in a weight-$n$ MZV-period space filtered further by admissibility. | Brown 2012; Eichler--Zagier 1985 Thm 9.1 (canonical row 44). |
| $(\infty, 1)$-obstruction tower (W21.2) gives the Maurer--Cartan tower of universal obstructions in an $(\infty, 1)$-stable category. | $(\infty, 2)$-adjunction AR structure (W22.1) exhibits bar--cobar as an adjunction in an $(\infty, 2)$-category with an Auslander--Reiten sequence. | The $(\infty, 2)$ structure is the $2$-categorical lift of the $(\infty, 1)$ obstruction tower: AR sequence at object level descends to the MC obstruction tower at morphism level. Both proved, both load-bearing. | Lurie HA 5.5; Riehl--Verity 2020. |
| Six-path $\chi_3$ (W22.6): six independent verification paths for the third Chern character. | Seven-path $\chi_3$ (W25.4): seven paths including a derived-deformation check. | Six independent paths plus one additional derived-deformation path, consistent with prior comparison. The seventh path refines the six without contradicting them. Every path reports the same $\chi_3$ value. | Beilinson multi-path verification discipline; W25.4 cache entry. |
| Four sibling functors $\{\Psi, \Psi^{\deg}, \Psi^{\mathrm{tor}}, \Psi^{\mathrm{metap}}\}$ parametrise the Baily--Borel--Freitag stratification of $\overline{\mathcal A_2}$ (canonical preamble row 46). | Five $\Psi$-image rows including the Conway $V^{s\natural}$ row on the metaplectic branch (W20.2 table). | The four siblings parametrise the four strata; each sibling has one image row, and the $\Psi^{\mathrm{metap}}$ sibling hosts two rows (Conway $V^{s\natural}$ and a second metaplectic image). Row count $5 = 4$ siblings with one extra Conway row on the metaplectic branch. | Baily--Borel--Freitag; Duncan 2007. |
| Absolute Kuznetsov HPD blocked on $K3 \times E$ (obstruction from the non-trivial Brauer class on $K3 \times E$). | Relative HPD over $E$ works (the relative $E$-base kills the obstruction by descent). | Obstruction at the absolute level; healing at the relative level. Both statements are proved theorems; relative HPD is the correct home for the $K3 \times E$ Kuznetsov lift. | Kuznetsov 2007; Perry 2019 relative HPD. |
| Pseudo-character framework (Taylor 1991) is sufficient on reduced rings for Galois deformations of $\rho_{\Delta_{10}}$. | Chenevier determinant framework (2014) is necessary on non-reduced rings (where mod-$\ell^n$ Cayley--Hamilton fails for reducible $\rho$). | Compatible hierarchy, not competing frameworks. Taylor's pseudo-character suffices on reduced; Chenevier's determinant is the correct lift to non-reduced. Each dominates in its natural domain; neither refutes the other. Canonical preamble row 53 pins the non-reduced case to Chenevier; reduced-ring calculations may still cite Taylor. | Taylor 1991 *Invent Math* 116; Chenevier 2014 *Ann Inst Fourier* 64. |

**Operating rule.** If you encounter two inscriptions that seem to
contradict, before editing either side **check this table**. If the
pair matches an entry, both are correct. If not, escalate through
Gate 0: the confusion is a candidate for a new compatibility mechanism,
not a candidate for retraction.


---

and cross-programme anti-patterns (AP150--AP164, FM24--FM27) into a reference
table. Each entry records the failure mode, its severity, and the
counter-measure. These patterns were identified through systematic error
archaeology across 100+ commits and the Waves 1-24+ adversarial-swarm
campaign.

*Relocated from `appendices/antipatterns.tex` on 2026-04-17 per the
Manuscript Metadata Hygiene rule in `CLAUDE.md`: the anti-pattern
catalogue is working-notes scaffolding and does not belong in the
typeset manuscript.*

## Severity levels

| Level    | Meaning                                                    | Action                                 |
| -------- | ---------------------------------------------------------- | -------------------------------------- |
| Critical | Theorem status wrong (conjecture $\to$ theorem)            | Immediate fix; audit all instances     |
| High     | Numerical or structural error propagates                   | Fix before next build                  |
| Medium   | Convention clash or ambiguity                              | Fix in current session                 |
| Low      | Cosmetic or cross-reference staleness                      | Fix in batch                           |

## CY-specific anti-patterns: AP-CY1 through AP-CY8

- **AP-CY1 -- CY dim $\neq$ cpx dim (High).**
  $\mathrm{Fuk}(X)$ and $D^b(\mathrm{Coh}(X))$ are $\mathrm{CY}_n$ where
  $n$ is the *complex* dimension, not the real dimension $2n$.
  **Counter**: always state "$\mathrm{CY}_d$ with $d = \dim_{\mathbb{C}} X$".

- **AP-CY2 -- CY trace target (High).**
  The CY trace lives in $\mathrm{HC}^-_d(\mathcal{C})$ (negative cyclic
  homology), not just $\mathrm{HH}_d \to k$. The negative cyclic
  refinement is essential for the $S^1$-framing.
  **Counter**: always write $\mathrm{HC}^-_d$, never bare
  $\mathrm{HH}_d \to k$.

- **AP-CY3 -- $E_2 \neq$ commutative (High).**
  $E_2$ braiding is *not* symmetric. $E_2 \to E_\infty$ loses all
  quantum group structure.
  **Counter**: never write "commutative" for $E_2$; write "braided".

- **AP-CY4 -- Drinfeld $\neq$ derived center (High).**
  $Z(\mathcal{C})$ (monoidal center via half-braidings) $\neq$
  $Z^{der}(A)$ (Hochschild cochains). The relationship: Drinfeld center
  categorifies the derived center.
  **Counter**: always specify which center.

- **AP-CY5 -- Root-of-unity requirement (Medium).**
  Kazhdan--Lusztig equivalence requires $q$ a root of unity. At generic
  $q$, $\mathrm{Rep}_q(\mathfrak{g})$ is semisimple.
  **Counter**: state the $q$-specialization explicitly.

- **AP-CY6 -- $A_X$ at $d=3$ (Critical).**
  $A_X$ for CY3 does *not* exist --- it IS the $d=3$ programme.
  Results depending on $A_X$ at $d=3$ must use `\begin{conjecture}`
  and `\ClaimStatusConditional`, naming CY-A$_3$.
  **Counter**: decision tree HZ3-1.

- **AP-CY7 -- CoHA $\neq$ $E_1$-chiral (High).**
  CoHA is associative (Hall product), not a chiral algebra.
  "$E_1$-sector of $G(X)$" assumes $G(X)$ exists.
  **Counter**: connection is via the functor $\Phi$, not identification.

- **AP-CY8 -- Borcherds $\neq$ bar Euler (High).**
  The identification $\Phi_{10} = $ bar Euler product is an
  *observation* (for $K3 \times E$), not a theorem. Conditional on
  CY-A$_2$ and Vol I Borcherds-lift identification.
  **Counter**: cite both CY-A and Vol I anchor.

## Empirical anti-patterns: AP-CY9 through AP-CY13

- **AP-CY9 -- Jacobi discriminant (High).**
  For $\phi_{k,m}$ of index $m$, only discriminants $D$ with $D \equiv 0$
  or $3 \pmod{4}$ (at $m=1$) can appear. Also $c(-1) = 2$ for
  $\phi_{0,1}$ in Eichler--Zagier convention, not $1$.
  **Counter**: verify discriminant constraint before filling tables.

- **AP-CY10 -- Flop $\neq$ Koszul dual (High).**
  Birational flop $X \dashrightarrow X^+$ preserves $\kappa_{ch}$.
  Koszul dual $A^!$ satisfies
  $\kappa_{ch}(A) + \kappa_{ch}(A^!) = \rho_K$. Flop exchanges chambers;
  Koszul exchanges algebra/coalgebra.
  **Counter**: $\kappa_{ch}(A_X) = \kappa_{ch}(A_{X^+})$ for flop.

- **AP-CY11 -- Conditional transitivity (Critical).**
  If Result B depends on Result A which depends on CY-A$_3$, then B is
  *also* conditional on CY-A$_3$. Conditionality propagates.
  **Counter**: use `\ClaimStatusConditional` with full chain.

- **AP-CY12 -- Shadow class computation (High).**
  G/L/C/M must be computed from the full shadow tower, not from
  generator counting or non-formality ($m_3 \neq 0$) alone. Local
  $\mathbb{P}^2$ is class M (infinite depth), not class L.
  **Counter**: always compute the full tower.

- **AP-CY13 -- Stale Part references (Low).**
  After any Part restructuring, grep all three volumes for stale
  `Part~[IVXL]` references.
  **Counter**: use `\ref{part:...}` exclusively.

## Deep empirical anti-patterns: AP-CY14 through AP-CY20

- **AP-CY14 -- Unconstructed in thm (Critical).**
  Any statement whose proof chain passes through $G(X)$ at $d=3$,
  $A_{K3 \times E}$, or any unconstructed object **must** use
  `\begin{conjecture}`, never `\begin{theorem}`.
  **Counter**: default to `\begin{conjecture}` in Vol III.

- **AP-CY15 -- README inflation (Medium).**
  README must not claim "verified" for structural analogies.
  **Counter**: after README edits, verify every "proved" against
  `\ClaimStatus` tags.

- **AP-CY16 -- Matrix size conflation (Medium).**
  $\mathrm{Sp}_4$ quotient by $\pm I_4$ ($4 \times 4$), not $\pm I_5$.
  $O(\Lambda^{3,2})$ quotient by $\pm I_5$ ($5 \times 5$).
  **Counter**: verify matrix dimensions match group rank.

- **AP-CY17 -- MF CY dimension (High).**
  For $W\colon \mathbb{A}^n \to \mathbb{A}^1$, $\mathrm{MF}(W)$ is
  $\mathrm{CY}_{n-2}$, not $\mathrm{CY}_{n-1}$. ADE in 2 variables:
  $\mathrm{CY}_0$. Need 4 variables for $\mathrm{CY}_2$, 5 for
  $\mathrm{CY}_3$.
  **Counter**: verify $n - 2$ against desired CY dimension.

- **AP-CY18 -- Lattice theta series (Medium).**
  Leech theta: minimum norm${}^2 = 4$, first correction at $q^2$ not
  $q^1$. Never conflate $j(\tau)$ coefficients with $V_\Lambda$
  character.
  **Counter**: verify by direct computation.

- **AP-CY19 -- $\hat{A}$-genus halving (High).**
  $\hat{A}(x) = \frac{x/2}{\sinh(x/2)}$; convergence radius $= 2\pi$
  (first pole of $\sin(x/2)$ at $x = 2\pi$). Dropping the $/2$ gives
  spurious radius $\pi$.
  **Counter**: always include the $/2$ in the argument.

- **AP-CY20 -- Normal bundle $\neq$ spectral (High).**
  The $\mathbb{Z} \times \mathbb{Z}$ grading from $N_{C/Y}$ connects to
  $(q,t)$ through the $\Omega$-background, not directly.
  **Counter**: name the intermediary mechanism (equivariant
  localization).

## 6d hCS session anti-patterns: AP-CY21 through AP-CY26

- **AP-CY21 -- $E_3$ bar class M (High).**
  $(1+t)^{3g}$ holds for classes L and C only. Class M:
  infinite-dimensional ($d_4$ survives).
  **Counter**: state the shadow class before claiming $E_3$ bar
  cohomology.

- **AP-CY22 -- Miki is algebra-specific (Medium).**
  The $S_3$ permutation of $(q_1, q_2, q_3)$ comes from the Weyl group
  of the CY torus, not from the $E_3$ operad.
  **Counter**: state it requires
  $U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)$.

- **AP-CY23 -- $E_1$ not $E_\infty$ bialgebra (Critical).**
  The coproduct $\Delta_z$ lives on the $E_1$ (ordered) side.
  $E_\infty$ averaging kills Hopf structure. Li's vertex bialgebra
  ($E_\infty$) is the wrong categorical home.
  **Counter**: formulate Hopf data at $E_1$ level using $B^{ord}$.

- **AP-CY24 -- Docstring confabulation (Medium).**
  Correct code but fabricated "ground truth" in docstrings.
  **Counter**: verify every numerical value against actual function
  output.

- **AP-CY25 -- $R$-matrix from vacuum (High).**
  $R(z) = (\mathrm{id} \otimes S) \circ \Delta_z(1_A)$ is wrong (counit
  axiom gives $1 \otimes 1$). Correct: construct via the half-braiding.
  **Counter**: never extract $R$ from $\Delta(1)$.

- **AP-CY26 -- Verdier $\neq$ $\sigma_2$ inversion (High).**
  $k^! = -k$ comes from Shapovalov form transposition, not from
  $\sigma_2(-h_i) = -\sigma_2$ (false: $\sigma_2$ is degree-2
  homogeneous, hence even).
  **Counter**: derive $k^!$ from Shapovalov/Verdier.

## Swarm-mined anti-patterns: AP-CY27 through AP-CY33

- **AP-CY27 -- Sandbox non-persistence (High).**
  Background agents report successful writes but files do not persist
  (sandbox isolation).
  **Counter**: verify file existence with `ls` after agent completion.

- **AP-CY28 -- Pole-unsafe test points (High).**
  When testing $g(z)$ with poles at $z = \pm h_i$, test points must
  avoid these values.
  **Counter**: use $h = (37, 41, -78)$ for large-parameter safety.

- **AP-CY29 -- Wrong-repo file writes (Medium).**
  Agents write files to the wrong volume's directory.
  **Counter**: verify full path includes correct repo root.

- **AP-CY30 -- Factored $\neq$ solved (Critical).**
  $S_{ijk} = R_{ij} R_{ik} R_{jk}$ from YBE-satisfying $R$ does *not*
  satisfy ZTE. $O(\kappa_{ch}^2)$ obstruction proved
  (`thm:zte-failure`).
  **Counter**: never assume pairwise $\Rightarrow$ higher-order.

- **AP-CY31 -- Spectral $z \neq$ worldsheet $z$ (High).**
  Drinfeld coproduct $\Delta_z$: Yangian spectral parameter. OPE
  $T(z)T(w)$: worldsheet coordinate. Different objects.
  **Counter**: always state whether $z$ is spectral or worldsheet.

- **AP-CY32 -- Reorganization $\neq$ bypass (Medium).**
  The 6d factorization homology route appears to bypass CY-A$_3$ but
  reorganizes the conjecture into subproblems, solving none
  independently.
  **Counter**: verify each subproblem is independently resolved.

- **AP-CY33 -- Chain $\neq$ rational (High).**
  $E_3$ structure is genuine at the chain level but collapses to $E_2$
  under formality (rational coefficients). Physical content lives at
  the chain level.
  **Counter**: state whether claim is chain-level or rational.

## Cross-programme anti-patterns: AP150--AP157 and FM24

- **AP150 -- Confabulated composites (Critical).**
  Agents stitch real ingredients into composite structures that do not
  exist.
  **Counter**: verify each arrow independently before writing composite
  diagrams.

- **AP151 -- $\hbar$ convention clash (High).**
  Two definitions of $\hbar$ can coexist in one chapter.
  **Counter**: grep for existing definitions; one file, one $\hbar$.

- **AP152 -- "Ordered" ambiguity (Medium).**
  "Ordered product" can mean labeled-ordered ($E_1$ bar), time-ordered
  (OPE), or normally-ordered (Wick).
  **Counter**: bare "ordered" is forbidden; always qualify.

- **AP153 -- $E_3$ scope inflation (High).**
  $E_3$ on Hochschild cochains (Deligne conjecture) requires $E_\infty$
  input. For $E_1$ input, Hochschild cochains carry only $E_2$.
  **Counter**: verify input is $E_\infty$ before claiming $E_3$.

- **AP154 -- Two $E_3$ structures (Medium).**
  Algebraic $E_3$ (Deligne) vs topological $E_3$ (configuration space).
  Agree under formality; differ at chain level.
  **Counter**: specify which $E_3$ and whether formality is assumed.

- **AP155 -- Novelty overclaim (Medium).**
  When $\Phi$ recovers a known invariant, the invariant is not new,
  only the construction path.
  **Counter**: state "$\Phi$ recovers the known invariant $X$
  (due to [cite]) via a new path".

- **AP156 -- Weierstrass $P_1$ ambiguity (Medium).**
  $\theta_1'/\theta_1$ vs Weierstrass $\zeta(\cdot; \Lambda)$ differ by
  $\mathrm{Im}(z)$-dependent terms.
  **Counter**: specify convention and state quasi-periodicity.

- **AP157 -- Degeneration-type dependence (High).**
  Different degenerations (large complex structure, conifold, orbifold,
  MUM, tropical) produce different chiral algebras.
  **Counter**: name the degeneration type explicitly.

- **FM24 -- B-cycle $i^2$ sign (Critical).**
  $i^2 = -1$ not $+1$. Error gives $|q| = 1$ instead of $|q| < 1$,
  destroying $q$-expansion convergence.
  **Counter**: verify $|q| < 1$ and $\mathrm{Im}(\tau) > 0$.

## Statistics

| Category                            | Count |
| ----------------------------------- | ----: |
| CY-specific (AP-CY1--AP-CY33)       |    33 |
| Cross-programme (AP150--AP157)      |     8 |
| Formula-mechanical (FM24)           |     1 |
| **Total catalogued**                |  **42** |
| Critical severity                   |     8 |
| High severity                       |    19 |
| Medium severity                     |    12 |
| Low severity                        |     1 |

Two anti-patterns have required fixes in 10+ independent instances:
AP-CY6/AP-CY14 (unconstructed object in theorem environment, 11+
fixes) and AP113 (bare $\kappa$, 15+ fixes). These two alone account
for approximately 40% of all error-correction commits in Vol III.

## K3 chiral bialgebra $\mathbf{H}_{\Delta_5}$ anti-patterns: AP-CY34 through AP-CY49

Identified through the adversarial swarm campaign April 2026 across
the non-abelian K3 chiral bialgebra construction, paramodular
automorphic data, and super-Etingof--Kazhdan quantisation.

- **AP-CY34 -- Conway $V^{s\natural}$ as bosonic $\Psi$-image (High).**
  $V^{s\natural}$ has $c = 12$, not 24; is the $\mathbb{Z}/2$-orbifold
  $A(\Lambda_{24})^+ \oplus A(\Lambda_{24})^{\mathrm{tw},+}$ of the
  24-generator fermionic VSA on Leech (Duncan 2007 *Duke Math J* 139).
  Treating Conway as a fifth bosonic $\Psi$-image with
  $(K, \hbar^2) = (2, -1/2)$ inherited from Monster conflates two
  different functors. Universal identity $\hbar^2 K^\kappa = -1$
  has no scope on Leech (positive-definite, no hyperbolic plane).
  **Counter**: Conway is a $\Psi^s$-image of the parallel super-functor
  $\Psi^s$ on super-lattices with half-integer Jacobi input:
  $\phi^s_{\mathrm{Conway}} = \vartheta_1(\tau,z)\Theta_{\Lambda_{24}}(\tau,z)/\eta(\tau)^{24}$
  weight $1/2$, index 1 (Scheithauer 2008 *Invent Math* 172 Thm 3.2).
  "Four is all" is Gritsenko--Nikulin-reflective-scoped via three-paper
  chain Scheithauer 2017 + Dittmann--Ma--Scheithauer 2021 + Scheithauer
  2006; $24A_1$ Niemeier Borcherds product is a non-GN fifth lift.

- **AP-CY35 / AP-CY141 -- Chenevier determinant, not Taylor--Wiles
  pseudo-character, as arithmetic anchor for $\mathbf H_{\Delta_5}$
  (Critical; W25 canonical).**

  **(a) Ghost (what is real)**: the Taylor 1991 *Duke* 63 pseudo-character
  $S^{\mathrm{ps}} : \mathbb T^{\mathrm{par}}_1 \to \mathcal O_E$
  (symmetry / multiplicativity / dimension-$d$ axioms) is a real object
  (Taylor 1991 Thm 2.1; Rouquier 1996 *J Algebra* 180). The Hecke-algebra
  4-tuple $(\Sigma_1, \Sigma_2, \Sigma_3, \Sigma_4)$ computed from the
  Saito--Kurokawa lift Satake parameters of $\Delta_{10} =
  \mathrm{Ik}(\Delta_{E_6})$ is correct data (Ikeda 2001 *Ann Math* 154
  Cor 16.2). The bridge from pseudo-character to a 4-dimensional Galois
  representation $\rho_{\Delta_{10}} : \mathrm{Gal}(\overline{\mathbb Q}
  / \mathbb Q) \to \mathrm{GSp}_4(\mathcal O_E)$ works on **reduced
  rings** via Chenevier 2014 Thm 2.12 (pseudo-characters $\leftrightarrow$
  determinants coincide on reduced rings).

  **(b) Precise error**: conflates the Taylor--Wiles pseudo-character
  (older, weaker, a multilinear symmetric trace function) with the
  Chenevier 2014 determinant (newer, stronger, a **single homogeneous
  polynomial law** of degree $d$ satisfying multiplicativity $+$
  unitality $+$ Cayley--Hamilton as a single axiom). On non-reduced
  rings --- exactly the deformation rings $R^{\mathrm{def}}_{\Delta_5}$
  around the Saito--Kurokawa lift (Open Problem #6 / W26.6) and the
  deformation rings felt by Vol III's Hodge-theoretic pairings --- the
  two objects differ: the determinant captures nilpotent
  Cayley--Hamilton witnesses (mod-$\ell^n$ Cayley--Hamilton identities
  for reducible $\rho$ with non-trivial nilpotent deformations) that
  the pseudo-character silently drops. For Saito--Kurokawa
  $\rho_{\Delta_{10}} = \rho_{\Delta_{E_6}} \oplus \chi^8 \oplus \chi^9$
  (reducible), calling the Galois-side invariant a pseudo-character is
  a type error.

  **(c) Correct**: use the **Chenevier determinant** $D^{\mathrm{Chen}}
  : \mathbb T^{\mathrm{par}}_1 \to \mathcal O_E \otimes \mathbb Z_\ell$,
  a 4-dimensional homogeneous polynomial law. Its graded components
  $(\Sigma_1, \Sigma_2, \Sigma_3, \Sigma_4)$ at Hecke generators $T_p$
  recover the Saito--Kurokawa Satake data via the **reciprocal spinor
  $L$-factor expansion**
  $$\prod_{i=1}^4 (1 - \alpha_i x) = 1 - \Sigma_1 x + \Sigma_2 x^2
  - \Sigma_3 x^3 + \Sigma_4 x^4$$
  with $\Sigma_1(T_p) = a_p(f_{16}) + p^8 + p^9$ (where $f_{16} = E_4
  \cdot \Delta$ is the weight-16 primary form) and $\Sigma_4(T_p) = p^{32}$.
  Verified empirically at 46 primes $p \le 199$. Factorisation
  $D^{\mathrm{Chen}}_{\Delta_{10}} = D_{\rho_{\Delta_{E_6}}} \otimes
  D_{\chi_\ell^8 \oplus \chi_\ell^9}$, unramified outside $\{2, \ell\}$;
  Hecke field $\mathbb Q(\lambda_p) = \mathbb Q$ (since
  $\dim S_{26}(\mathrm{SL}_2(\mathbb Z)) = 1$), minimal coefficient ring
  $\mathcal O_E = \mathbb Z$. **Non-reduced-ring extension**: on
  $R^{\mathrm{def}}_{\Delta_5}$ (Open Problem #6 / W26.6), the
  Chenevier determinant is well-defined via the polynomial-law axioms;
  the Taylor--Wiles pseudo-character is not.

  **Primary literature**: Chenevier 2014 arXiv:1301.0635
  (in *Automorphic Forms and Galois Representations*, Vol I) \S 1.2
  Def/Prop 1.9, Thm 2.12 (determinant = pseudo-character on reduced
  rings; strict inequality on non-reduced); Taylor 1991 *Duke* 63
  Thm 2.1 (pseudo-character original); Ikeda 2001 *Ann Math* 154
  Cor 16.2 (Saito--Kurokawa lift); Weissauer 2005 *LNM* 1868 \S 4
  (spinor Galois representation construction); Laumon 2005 *Publ IHES*
  102 Thm I.10 (geometric Satake on $\mathrm{GSp}_4$); Pitale--Saha--Schmidt
  2014 *Memoirs AMS* 232 (transfer of automorphic representations on
  $\mathrm{GSp}_4$); Poor--Schmidt--Yuen 2020 *Nagoya Math J* 239
  (paramodular newforms of weight 5).

  **Cross-volume cross-reference**: Vol I AP353 / AP902 / Remark
  `rem:dl-w25-determinant-not-pseudocharacter` and Theorem alias
  `thm:dl-determinant-delta10` in `chapters/theory/derived_langlands.tex`
  (Vol I Pattern 295 / W25 in `notes/first_principles_cache_comprehensive.md`
  cache entry 422); Vol II AP-V2-23 in
  `notes/antipatterns_catalogue.md` and W27-A entry 135 in tip cache
  `notes/first_principles_cache.md`; Vol III tip cache row 8
  (`appendices/first_principles_cache.md`) and comprehensive cache
  entry 55 + W25 long-form entry below (`notes/first_principles_cache_comprehensive.md`);
  Vol III `ADJUDICATION_LEDGER` \S III.C. Distinct from Creutzig--Ridout
  2013 *Nucl Phys B* 875 Thm 3.4 logarithmic-VOA coend pseudo-traces
  (appearing in Vol III `modular_trace.tex`, `quantum_groups_foundations.tex`):
  those are Kerler--Lyubashenko modified-trace functionals on
  non-semisimple MTCs, categorically unrelated to the Chenevier
  polynomial-law axiomatisation on Hecke algebras.

- **AP-CY36 -- Bridgeland $\mathrm{Stab}^\Phi$ codim-0 (High).**
  Claiming $\mathrm{Stab}^\Phi(K3 \times E) = \mathrm{Stab}(K3) \times \mathrm{Stab}(E)$
  is a codim-0 slice is wrong. Bridgeland 2007 Thm 1.2:
  $\dim \mathrm{Stab} = \mathrm{rk}\,\mathcal{N}$. Künneth on
  numerical K-theory gives $\mathrm{rk}\,\mathcal{N}(K3 \times E) = 24 \cdot 2 = 48$;
  the Künneth image uses only rank-one tensors with $24 + 2 = 26$
  parameters.
  **Counter**: $\dim_\mathbb{C} \mathrm{Stab}(K3 \times E) = 48$;
  codim of $\mathrm{Stab}^\Phi$ is $22 = \mathrm{rk}\,T_{K3}$
  (transcendental lattice). Three non-Künneth CY$_3$-rigid families
  populate the complement: Fourier--Mukai twists on transcendental
  classes, non-split vertical extensions, isogeny-graph spectral sheaves.
  Scope: stability-manifold count 48 (even $K_{\mathrm{num}} \cong H^{\mathrm{even}}$);
  full Betti rank 96 (odd cohomology has zero Euler pairing).

- **AP-CY37 -- Tensor factorisation of $u_{\zeta_8}^{\mathrm{tilt}}$-mod
  through $\mathrm{Vec}_{S_3}$ (High).**
  Rank-162 tilting MTC does not factorise as tensor
  $(A_1)_{k=2}^{\otimes 3} \boxtimes \mathbb{Z}[S_3]$ since
  $\mathrm{Vec}_{S_3}$ is not modular (DGNO 2010 *Selecta Math* 16
  Prop 2.11: modular $\mathrm{Vec}_G$ requires abelian $G$ with
  non-degenerate quadratic form). Alternative ranks ruled out:
  $\mathrm{Rep}(S_3) = 3$, $D(S_3)\text{-mod} = 8 \Rightarrow 216 \ne 162$,
  equivariantisation $= 22$.
  **Counter**: $u_{\zeta_8}^{\mathrm{tilt}}\text{-mod} =
  (A_1)_{k=2}^{\otimes 3} \rtimes S_3$, $S_3$-crossed braided fusion
  (Turaev 2000 arXiv:math/0005291; ENO 2010 *Quantum Topol* 1). Six
  $S_3$-graded pieces (identity + 3 transpositions + 2 three-cycles)
  each invertible bimodule of rank 27; total $162$. Modular data
  $S = S^{(A_1)^{\otimes 3}} \otimes (1/\sqrt{6}) F_{S_3}$ is crossed-structure
  spectral data, not tensor factorisation.

- **AP-CY38 -- Fake-Monster Leech root norm 6 (High).**
  Claiming Leech simple roots have norm 6 from
  $r_\lambda = (\lambda; e + (\lambda^2-2)/2\,f)$ fails Borcherds'
  simple-root condition $(\rho, r) = -r^2/2$: the formula at
  $\lambda^2 = 4$ gives $r^2 = 6$ but $(\rho, r_\lambda) = 1 \ne -3$.
  **Counter**: Correct Conway 1983 *Proc R Soc Lond A* 384 Thm 1 +
  Conway--Sloane *SPLAG* Ch 27: $r_\lambda = (\lambda; 1, 1-\lambda^2/2)
  = (\lambda; 1, -1)$ at $\lambda^2 = 4$, norm 2, satisfying
  $(\rho, r_\lambda) = -1 = -r^2/2$. Leech roots are **norm 2**,
  $196{,}560$ of them in a single $\mathrm{Co}_0$-orbit.

- **AP-CY39 -- Fake-Monster automorphic home as Siegel $\mathrm{Sp}_{26}$
  (High).**
  $\Phi_{12}$ is not a Siegel form on $\mathrm{Sp}_{26}(\mathbb{Z})$
  (which acts on $\mathbb{H}_{26}$ of complex dim 351) nor a Jacobi
  form in 26 variables.
  **Counter**: $\Phi_{12}$ is a Borcherds-Hermitian automorphic form
  on the type-IV Hermitian symmetric domain
  $\mathcal{D}_{\mathrm{II}_{26,2}} = O(26,2)^+/(O(26) \times O(2))$
  of complex dim 26, singular weight $12 = (26-2)/2$, for
  $O^+(\mathrm{II}_{26,2})$. Restriction along primitive
  $\mathrm{II}_{2,2} \hookrightarrow \mathrm{II}_{25,1}$ gives
  $\Phi_{10} = \Delta_5^2$ (signature-$(2,1)$ sublattice $\mathrm{II}_{2,1}$
  cannot carry a holomorphic modular form; hyperbolic 2-ball, not
  Hermitian symmetric).

- **AP-CY40 -- Master $L$-value as $L'(0, \Delta_{10}, \mathrm{ad}^0)$
  (Critical).**
  Three distinct conflations: (a) adjoint vs standard — Yoshikawa 2004
  Thm 5.7 + Bruinier--Kühn 2003 Thm 4.11 on signature-$(2,3)$
  Borcherds-lift line bundles give the degree-5 **standard** $L$-function,
  not adjoint spinor; (b) $\Delta_5$ vs $\Delta_{10}$ — 1-loop anomaly
  $-\log \Delta_5$ with twisting sheaf $\mathcal{O}(\Delta_5^{-1})$
  pins the paramodular base-point, not the full-level Ikeda lift;
  (c) CAP reducibility —
  $L(s, \Delta_{10}, \mathrm{ad}^0) = L(s, \mathrm{Sym}^2 \Delta_{E_6})
  \cdot \zeta(s+1) \cdot \zeta(s-1)$ (Pitale--Saha--Schmidt 2014
  *Memoirs AMS* 232 §7); cyclotomic factors at $s = 0$ contribute
  only trivial $\zeta'(0) = -(1/2)\log(2\pi)$, not a BKM regulator.
  **Counter**: Correct master identity
  $\log Z^{(1)}_{\mathbf{H}_{\Delta_5}} = -\log \Delta_5 -
  \kappa_{\mathrm{BGS}} \cdot L'(0, \Delta_5, \mathrm{std}) + \log C$
  with $\kappa_{\mathrm{BGS}} = 24 = \chi_{\mathrm{top}}(K3)$. Paramodular
  standard $L$ via $\phi_{\Delta_5} \colon L_F \to \mathrm{GSp}_4$
  composed with $\mathrm{std} \colon \mathrm{GSp}_4 \to \mathrm{SO}_5
  \hookrightarrow \mathrm{GL}_5$ (Schmidt 2005 *Pacific J Math* 220).
  Kudla--Rallis seesaw $(\mathrm{Sp}_4, O(2,2))$ regulator $= L'(0, \Delta_5, \mathrm{std})$.
  Waldspurger squaring at unramified places
  $L(2s, \Delta_5, \mathrm{std}) \cdot L(2s, \Delta_5 \otimes \epsilon_{K(1)}, \mathrm{std})
  = L(s, \Delta_{10}, \mathrm{std}) \cdot (\text{bad primes})$
  (Waldspurger 1980 *Compositio* 54; Furusawa--Morimoto 2014
  *Adv Math* 255) relates standard $L$-functions, not adjoint.

- **AP-CY41 -- Bloch--Kato Selmer $\dim H^1_f(\mathrm{ad}^0 \rho_{\Delta_{10}}) = 1$
  (Critical).**
  Adjoint spinor at the CAP point is rigid:
  $\dim H^1_f(\mathrm{ad}^0 \rho_{\Delta_{10}}) = 0$
  (Chenevier 2014 + Diamond--Flach--Guo 2004 CAP rigidity of
  level-one Ikeda lifts). Right numerical answer, wrong
  representation.
  **Counter**: Correct representation is paramodular standard
  $\mathrm{std}\,\rho_{\Delta_5}$:
  $\dim H^1_f(\mathrm{std}\,\rho_{\Delta_5}) = 1$ via three
  independent paths: (A) Fontaine--Mazur Euler characteristic with
  $\Gamma_\infty = \Gamma_\mathbb{C}(s+4)\Gamma_\mathbb{C}(s+3)\Gamma_\mathbb{R}(s)$
  forcing order 1 at non-critical $s=0$ + Jannsen purity $H^2_f = 0$;
  (B) Loeffler--Pilloni--Skinner--Zerbes 2021 Euler system + Liu 2019
  Kolyvagin; (C) Pilloni 2011 + Urban 2011 $\mathrm{GSp}_4$ control
  + Poor--Yuen 2015 $\dim S_5(K(1)) = 1$ + Thorne 2020 $R = T$.
  The 1-dim tangent is the paramodular cyclotomic Hida family at tame
  level $K(1)$.

- **AP-CY42 -- Pentagon admissibility on $n$ modulo 4 (High).**
  Admissibility congruence for $\phi^{(n)}$ is not on $n$ itself.
  It is on the Heegner discriminant $D_n = (n-3)/2 \pmod 4 \in \{0, 1\}$,
  equivalently $n \equiv 3, 5 \pmod 8$.
  **Counter**: Humbert--Heegner admissibility filtration
  $\mathfrak{H}_D$: $\phi^{(n)} = 0$ unless $n \equiv 3, 5 \pmod 8$.
  Mechanism: Eichler--Zagier 1985 *Prog Math* 55 Thm 9.1 — weak Jacobi
  index-$m$ polar support $\Delta \ge -m^2$ annihilates Heegner
  coefficient at non-admissible $n \ge 7$. First admissible non-vanishing:
  $\phi^{(5)} = -2 \cdot [\mathrm{gen}]^{\otimes 5}$ with
  $c_{\Phi_{10}/\eta^{24}}(1, 1, 1) = -2$ (Gritsenko--Nikulin 1998
  *Invent Math* 130 Table 2). Coincides with paramodular critical-$L$-value
  congruence (Gritsenko--Nikulin 1998 Thm 1.4; Ibukiyama--Poor--Yuen
  2013 Thm 5.1). Unconditional on K3 side; bypasses Zagier--Hoffman
  motivic-depth conjecture.

- **AP-CY43 -- $\mathrm{grt}_1^{(1/2)}$ extension splitting via Saito--Kurokawa
  cocycle (High).**
  Conflating non-split, non-abelian, non-central (distinct Lie-extension
  properties). Also: Saito--Kurokawa Eichler cocycle
  $[\mathrm{SK}(\Delta)/\Delta] \in
  H^1(\mathrm{Sp}_4(\mathbb{Z}); \mathrm{Hom}(\mathrm{grt}_1, \mathbb{Q}[v_{\Delta_5}]))$
  is a group 1-cocycle; splitting obstruction for a Lie-algebra
  extension is Lie $H^2$.
  **Counter**: All three properties hold simultaneously for
  $\mathrm{grt}_1^{(1/2)}$. Obstruction
  $[\omega_{\mathrm{SK}}] \in H^2_{\mathrm{Lie}}(\mathfrak{q}; \mathrm{grt}_1)$
  related to the group cocycle via **van Est transgression**
  $\tau_{\mathrm{vE}} \colon H^1_{\mathrm{grp}} \to H^2_{\mathrm{Lie}}$.
  Concrete witness: $[\widetilde\sigma_2, \widetilde\sigma_2] = 288 \widetilde\sigma_4$
  via $\tau(2)^2/2 = 288$. Hilbert series disagree at every even weight
  (Brown 2012 *Ann Math* 175; Furusho 2011 *Ann Math* 174), so
  $\mathrm{grt}_1^{(1/2)} \not\cong \mathrm{grt}_1$ as graded or ungraded
  Lie algebras. BV realisation (Costello--Gwilliam 2017):
  $\omega_{\mathrm{SK}}$ is the commutator defect of BV derivations on
  $\mathrm{Obs}^q(\mathbf{H}_{\Delta_5})$.

- **AP-CY44 -- $\Psi$-functor surjectivity onto super-EK-quantisable
  BKMs (Medium).**
  $\Psi$ alone is not surjective; super-affine
  $\widehat{\mathfrak{gl}}(m|n)$, quantum-toroidal
  $U_{q,t}(\widehat{\widehat{\mathfrak{g}}})$, and metaplectic Conway
  $V^{s\natural}$ all escape the reflective-interior image.
  **Counter**: Minimal complete family is four sibling functors
  $\{\Psi, \Psi^{\deg}, \Psi^{\mathrm{tor}}, \Psi^{\mathrm{metap}}\}$
  indexed by Baily--Borel--Freitag stratification of $\overline{\mathcal{A}_2}$.
  No fifth stratum: (a) 0-cusp is $\Psi^{\deg}$-vacuum; (b) higher-$\omega_N$
  are inner automorphisms of $U_{q,t}$; (c) Hain--Looijenga hyperelliptic
  genus-2 locus sits inside $\overline{H_1}$ via Mumford--Torelli.
  Class-$\mathcal{S}$: four-fold stratification = CDT $\cup$ AD join =
  $\{\text{regular, irregular, AD, twisted}\}$; Humbert divisor = Argyres--Douglas
  via $E_{\tau_1} \times E_{\tau_2}$ Seiberg--Witten degeneration
  (GMN 2009 *Adv Theor Math Phys* 13 Ex 8.3).

- **AP-CY45 -- Chiral-Hochschild $e_k$ independent of $W_\infty[c]$
  primaries (Medium).**
  $e_5 = W_5$ identically by Wang 1998 *Prog Theor Phys* Prop 4.2
  three-leg weight-5 quasi-primary uniqueness at every central charge.
  **Counter**: Pope--Romans--Shen 1990 *Nucl Phys B* 339 $W_\infty[c]$
  primary identification at $c = -214$:
  $e_4 = W_4 - (107/11)\Lambda_Z$ with Zamolodchikov weight-4 extra
  $\Lambda_Z = :TT: - (3/10)\partial^2 T$; $e_5 = W_5$;
  $e_6 = W_6 - (107/11)\partial^2 \Lambda_Z + (\text{explicit}):T\Lambda_Z:$.
  Generic-$c$: $\alpha_4^{(3)} = -3c/20$, $\beta_5^{(2)} = -c(c+2)/280$,
  $\rho_6 = -c(c-2)/42$. Substitution at $c = -214$: $321/10$,
  $-5671/35$, $-7704/7$.

- **AP-CY46 -- Class-$\mathcal{S}$ $\mathcal{T}[A_1, \Sigma_{0,24}]$
  central charges $(21, 27)$ (High).**
  Arithmetic error. 22 trinions + 21 tubes for $n = 24$ on $\mathbb{P}^1$
  (gluing $n - 2$ trinions along $n - 3$ tubes). Each $A_1$ trinion
  contributes $n_h = 4$ half-hypermultiplets (tri-fundamental
  $\mathrm{SU}(2)^3/\mathbb{Z}_2$); each tube adds $n_v = 3$ vectors.
  Not "$(0, 4)$ per trinion + $(1, -1)$ per tube".
  **Counter**: $(n_v, n_h) = (21 \cdot 3, 22 \cdot 4) = (63, 88)$,
  $c_{4d} = (2 n_v + n_h)/12 = 214/12 = 107/6$,
  $c_{2d} = -12 c_{4d} = -214 = -2 \cdot 107$. Universal formula at
  $A_1$ genus 0: $c_{4d} = (5n - 13)/6$. WOV-2 lock via Chacaltana--Distler
  2010 §5.14 + Shapere--Tachikawa 2008 + Beem--Rastelli 2013.

- **AP-CY47 -- Chiral-Hochschild $e_k$ equals full motivic-period
  $\phi^{(3k)}$ projection (Medium).**
  BGS analytic torsion on Shimura varieties forces landing in the
  single-valued subring $\mathrm{zv}^{\mathrm{sv}}$ (Brown 2014
  *Forum Math Sigma* 2; Schnetz 2013 graphical-function normalisation),
  not the full motivic-period ring.
  **Counter**: $e_k = \mathrm{sv} \circ \pi^{\mathrm{depth} \le k}(\phi^{(3k)})$ —
  single-valued depth-$k$ projection. Motivic home shrinks from
  Padovan-dim $\mathrm{Per}^{\mathrm{mot}}_{3k}$ to strict subspace
  $\mathrm{zv}^{\mathrm{sv}}_{3k}$. At $k=3$: dim-2
  $\mathbb{Q}\zeta^{\mathrm{sv}}(3)^3 \oplus \mathbb{Q}\zeta^{\mathrm{sv}}(9)$.
  At $k=4$: dim-3 SV, NOT $\mathbb{Q}\pi^4$ (falsifies naive Tate ansatz).
  At $k=12$: depth $\le 12$ by MC iteration, Conway at $\hbar^{12}$ consistent.

- **AP-CY48 -- Six-routes-to-$G(K3 \times E)$ as six $\Phi$-applications
  (Medium).**
  Six **different constructions** (CoHA, Schiffmann--Vasserot,
  Maulik--Okounkov, Borcherds, Toda, DMVV) witness the same
  $\Phi_3$-output, not six $\Phi_3$-applications. Each takes a different
  CY-input category; $\Phi_3$ produces the same chiral algebra via a
  pentagon colimit.
  **Counter**: $\Phi$ gives ONE output per category. Different
  $\kappa$-values across the routes come from different constructions,
  not different $\Phi$-applications. The routes stratify by lattice
  rank $\rho^{R_i} \in \{3, 12, 24\}$ (generator level), not by
  $\kappa_{\mathrm{ch}}$ (categorical invariant of $\Phi_3(\mathcal{C})$,
  route-independent).

- **AP-CY49 -- Cross-volume $\kappa_{\mathrm{BKM}}$ (High).**
  Vol I abstract says $\kappa_{\mathrm{BKM}}(\mathbf{H}_{\Delta_5}) = 12$;
  Vol III abstract says $= 5$. Indexing convention for "$N$" in
  $\kappa_{\mathrm{BKM}}(X) = c_N(0)/2$ differs: if $N$ is BKM family
  index (Monster=1, K3=2,...) and $c_1(0) = 24$ gives 12; if $N$
  indexes the Siegel weight directly and $c_N(0) = 10$ for $\Phi_{10}$
  gives 5.
  **Counter**: Fix $N$ per CLAUDE.md landscape-census Borcherds-family
  index. Every Vol I/II/III occurrence of $\kappa_{\mathrm{BKM}}$ must
  explicitly name the input denominator (Fake-Monster $\Phi_{12}$ vs
  paramodular $\Phi_{10} = \Delta_5^2$ vs ...). AP5 audit required
  across all three volumes. Canonical value pending whole-object-verifier
  lock.

## Cross-programme anti-patterns: AP158 through AP164

- **AP158 -- Hook-cascade content loss (Critical).**
  Automated CG-rectify cascades do NOT preserve mathematical inscriptions
  that contain bookkeeping vocabulary in prose, titles, or labels.
  The 2026-04-20/21 cascade removed seven substantive adversarial-swarm
  inscriptions (Beilinson $\mathrm{Stab} = 48$; Kazhdan Selmer;
  Costello master BV; Drinfeld GRT-super; Gelfand rank-162 MTC;
  Gaiotto four siblings; Witten master $L$-value correction) as
  collateral because those inscriptions contained "Wave N" / "DNA" /
  "AP\d+" tags.
  **Counter**: Inscriptions are bookkeeping-free from the first
  keystroke. Named section/remark titles denote mathematical objects
  (not waves). Equations bear mathematical labels (not catalogue IDs).
  Agent prompts for chapter-body inscriptions must include the
  forbidden-vocabulary constraint explicitly.

- **AP159 -- Agent-inscription report $\ne$ disk state (High).**
  Multiple agents returned truncated or empty summaries despite
  high tool-use counts and long runtimes (Polyakov 52+ tools, Gelfand
  957 seconds). Treating the agent's summary as a proxy for what was
  written to disk leads to false claims of completed work.
  **Counter**: After every agent completion, verify via `grep -l` on
  key theorem labels, proposition names, specific formula coefficients,
  plus file-size delta. Never trust an agent summary without an
  independent disk check.

- **AP160 -- Numerical oscillation mistaken for iterative refinement
  (High).**
  Values that flip sign or magnitude across adjacent adversarial waves
  without independent path-verification are not converging; they are
  adversarially ping-ponging. Examples: Leech root norm ($2 \to 6 \to 2$);
  Witten heterotic-lift $c(1, 2, \pm 2)$ ($+1 \to -2$); Fake-Monster
  $c(28)$ Borcherds coefficient.
  **Counter**: Convergence threshold is two consecutive waves with
  zero sign flips or value corrections on any coefficient claimed
  "verified". Every numerical claim needs three independent
  path-verifications (direct computation, alternative formula, limiting
  case, symmetry, cross-family, primary literature). Use `compute/lib/`
  whole-object verifier (WOV) to lock values.

- **AP161 -- Orphan-file inscription (High).**
  Target files placed under `chapters/examples/` or `chapters/theory/`
  in Vol III are not automatically included in the build; they must
  be explicitly `\input`ed from `main.tex`. Vol III
  `chapters/examples/hochschild_calculus.tex` was orphaned; the built
  chapter at `chapters/theory/hochschild_calculus.tex` lacked the
  Wave-25 Polyakov $e_k$ inscription.
  **Counter**: Before inscribing new content, verify the target file
  is wired via `grep -n "input.*TARGET" main.tex`. Canonical homes:
  Vol III chiral-Hochschild at `chapters/theory/hochschild_calculus.tex`;
  Vol I at `chapters/theory/hochschild_cohomology.tex`. Cross-reference
  remark disambiguating conformal weight (Virasoro grading) from
  cohomological degree (ChirHoch concentration set $\{0, 1, 2, d\}$).

- **AP162 -- Non-split vs non-abelian vs non-central Lie extensions
  (Medium).**
  Three distinct properties are routinely conflated: non-abelian
  (ideal or quotient not central) vs non-split (no Lie section) vs
  non-central (mixed brackets nonzero). A non-abelian extension can
  still split. An extension with the ideal central can be non-split.
  **Counter**: Name the precise property. For $\mathrm{grt}_1^{(1/2)}$
  all three hold simultaneously; each requires its own witness.
  Non-splitness uses Lie $H^2$ (not group $H^1$); non-centrality
  exhibits explicit mixed brackets; non-abelianness shows the ideal
  carries its own bracket.

- **AP163 -- $\mathrm{Vec}_G$ modular for nonabelian $G$ (High).**
  Pointed fusion category $\mathrm{Vec}_G$ is modular only for abelian
  $G$ with non-degenerate quadratic form (DGNO 2010 *Selecta Math* 16
  Prop 2.11). Using $\mathrm{Vec}_{S_3}$ as a factor in a modular
  tensor factorisation is a type error.
  **Counter**: For nonabelian $G$, use $G$-crossed braided fusion
  categories $\mathcal{C} \rtimes G$ (Turaev 2000; ENO 2010) — $G$ grades
  $\mathcal{C}$ via outer automorphisms, graded pieces are invertible
  $\mathcal{C}$-bimodules. Modular data is crossed-structure spectral
  data, not tensor factorisation. Grothendieck-ring identity can
  survive at the $\mathbb{Z}$-algebra level even though MTC factorisation
  fails.

- **AP164 -- Scheithauer 2017 as sole citation for "four is all"
  (Medium).**
  Single-paper attribution is incomplete. Scheithauer 2017
  arXiv:1706.02546 Thm 1.1 gives lift-existence for holomorphic
  reflective automorphic products of singular weight; the finiteness
  half requires Dittmann--Ma--Scheithauer 2021 *Adv Math* 386
  (finiteness of reflective signature-$(2,n)$ even genera) and
  Scheithauer 2006 *Invent Math* 164 §3 (prime-level enumeration).
  **Counter**: Cite the three-paper chain. Scope: "four is all" is
  Gritsenko--Nikulin-reflective-scoped; the $24A_1$ Niemeier Borcherds
  product (Borcherds 1995 *Invent Math* 120 §13) is a reflective
  automorphic on signature $(2, 24)$ of singular weight 12 that
  fails GN-reflectivity (divisor has non-rational-quadratic-hyperplane
  components). A fifth exists outside GN-scope.

## Formula-mechanical additions: FM25 through FM27

- **FM25 -- Heegner discriminant variable (Critical).**
  Admissibility congruence on pentagon $A_\infty$-tower is on
  $D_n = (n-3)/2 \pmod 4$, not on $n \pmod 4$ or $n \pmod 8$ directly.
  Error: stating "$n \not\equiv 0, 3 \pmod 4$" instead of the correct
  $D_n \in \{0, 1\} \pmod 4$, equivalently $n \equiv 3, 5 \pmod 8$.
  **Counter**: Write the congruence in terms of $D_n$ and derive the
  $n$-form only as a translation.

- **FM26 -- $W_{1+\infty}$ vs $W_\infty[c]$ (Medium).**
  $W_{1+\infty}$ has generators at every nonnegative weight including
  a $\mathfrak{u}(1)$ current at weight 1; $W_\infty[c]$ has generators
  only at weights $\ge 2$. The relation is $W_{1+\infty} = W_\infty[c]
  \otimes \mathcal{H}$ with $\mathcal{H}$ Heisenberg.
  **Counter**: Name which algebra. $\mathrm{CoHA}(\mathbb{C}^3) =
  Y^+(\widehat{\mathfrak{gl}}_1)$ is the positive half of the affine
  Yangian; its classical limit is $W_{1+\infty}$, not $W_\infty[c]$
  and not the full affine Yangian.

- **FM27 -- Saito--Kurokawa spinor vs standard factorisation (High).**
  $L(s, \Delta_5, \mathrm{spin}) = \zeta(s - 5/2) \zeta(s - 7/2)
  L(s - 1/2, \Delta_{12})$ is the spinor-$L$-function factorisation
  through Saito--Kurokawa. The BV 1-loop determinant of
  $\mathbf{H}_{\Delta_5}$ couples to the **standard** $L$-function,
  not the spinor. No identity of the form
  $L(s, \Delta_{10}, \mathrm{ad}^0) = L(s, \Delta_5, \mathrm{std}) \cdot
  L(s, \chi, \bullet)$ exists.
  **Counter**: What does hold is Waldspurger squaring at unramified
  places: $L(2s, \Delta_5, \mathrm{std}) \cdot L(2s, \Delta_5 \otimes
  \epsilon_{K(1)}, \mathrm{std}) = L(s, \Delta_{10}, \mathrm{std}) \cdot
  (\text{bad primes})$. This is a **standard**-$L$-function squaring,
  not an adjoint-spinor identity. $\Delta_5$ has spin-cover Satake
  parameters $\{\pm \alpha_p^{1/2}, \pm \beta_p^{1/2}\}$ whose squares
  are $\{\alpha_p^{\pm 1}, \beta_p^{\pm 1}\}$ of $\Delta_{10}$.

## Wave 20-24 anti-patterns: AP-CY83 through AP-CY107

Exhaustive catalogue of Vol-III-relevant anti-patterns surfaced across
Waves 20-24 adjudication (2026-04-20). Each entry names the failure
mode, severity, and counter-measure; primary-literature citations
appear in the corresponding entries of the comprehensive cache
(`notes/first_principles_cache_comprehensive.md` Entries 166-200).

- **AP-CY83 -- $\Psi$-surjectivity scope (Critical).**
  Bare "$\Psi$ surjects onto $\mathrm{BKM}^{\mathrm{GN}}$" is false.
  22 non-Leech Niemeier BKMs $\mathfrak g^{(N)}$ (Scheithauer 2000 Thm
  6.2) are super-EK-quantisable reflective GKMs outside
  $\mathrm{Im}(\Psi_{d \in \{2, 3\}})$. Explicit counterexample:
  $\mathfrak g^{(24A_1)}$ on rank-26 $\mathrm{II}_{25, 1}$. $d \geq 4$
  extension blocked by FM43 $\mathbb S^d$-framing obstruction.
  **Counter**: always name domain $\mathrm{CY}^{\mathrm{Siegel-aut}}_{d
  \in \{2, 3\}}$; triple-verify via lattice-rank / Serre-parity /
  modular-characteristic.

- **AP-CY84 -- Conway $V^{s\natural}$ as 5th $\Psi$-image (Critical).**
  Advertising Conway $V^{s\natural}$ as independent 5th $\Psi$-image
  with $(K, \hbar^2) = (2, -1/2)$ from $c_+(\Lambda_{24}) = 0$ fails
  three ways: (a) venue Duke 139 not MRL 14; (b) Duncan uses
  $A(\Lambda_{24})$ on Leech, not $E_8$ super-lattice; (c) Leech
  signature $(24, 0)$ gives $c_+(\Lambda_{24}) = 24$ not 0.
  **Counter**: Duncan 2007 §6 commutative diamond reading places
  $V^{s\natural}$ as $\mathbb Z/2$-super-twin of $V^\natural$ INSIDE
  Monster row; $(K, \hbar^2) = (2, -1/2)$ inherited from Monster.
  Alternative: Scheithauer 2008 Thm 3.2 as Fake-Monster
  $\mathbb Z/2$-subsector. Downgrade to `\begin{conjecture}`.

- **AP-CY85 -- Enriques metaplectic weight $5/2$ (High).**
  Enriques BKM on $E_8(-1) \oplus \mathrm{II}_{1, 1}$ signature
  $(1, 9)$ does NOT carry Siegel weight 5; carries metaplectic weight
  $5/2$ on $\widetilde{K(2)}$ double cover.
  **Counter**: always write $\Delta_5^{\mathrm{Enr}} \in
  S_{5/2}(\widetilde{K(2)}^{v_{\mathrm{Enr}}})$; never weight 5.

- **AP-CY86 -- Direct $M_{12}$ moonshine on Enriques (Critical).**
  $f_{\mathrm{En}}(0, 1) = 10$ is not an $M_{12}$ irreducible
  dimension; ATLAS $M_{12}$ dimensions
  $\{1, 11, 11, 16, 16, 45, 54, 55, 55, 55, 66, 99, 120, 144, 176\}$
  exclude 10. Template-mismatch with $M_{24}$ Mathieu moonshine.
  **Counter**: Persson-Volpato 2013 point-stabiliser VIRTUAL
  decomposition $f^{K3}(0, 1) = 10 = 16 + 16 - 11 - 11$; $\iota$-halving
  gives $f_{\mathrm{En}}(0, 1) = 5 = 16 - 11$ (virtual, signed).

- **AP-CY87 -- Parity-of-$D$ vs parity-of-$c_{K3}(D)$ (High).**
  Half-integer $f_{\mathrm{En}}(D)$ locus is $\{D : c_{K3}(D)
  \text{ odd}\}$, not $\{D \text{ odd}\}$. Through $D \leq 60$ this
  is $\{7, 15, 31, 47, 55\}$; $D = 11, 19$ odd but give INTEGER
  $f_{\mathrm{En}}$.
  **Counter**: verify $c_{K3}(D) \pmod 2$ before asserting
  half-integer status.

- **AP-CY88 -- Unit-weight Mass formula (High).**
  $M_{12}$-invariant projector is not unit-weight $\sum_{[g]} \phi^g$;
  correct is centraliser-weighted $|M_{12}|^{-1} \sum_{[g]} |C_g|
  \phi^g$.
  **Counter**: always use centraliser-weighting per Schur
  orthogonality.

- **AP-CY89 -- Uniform non-negative $M_{12}$ multiplicities (High).**
  Gannon 2016 positivity is SIGN-ALTERNATING by $D \pmod 4$: $D \equiv
  0 \pmod 4$ massive-long non-negative; $D \equiv 3 \pmod 4$
  massive-short non-positive.
  **Counter**: $\mathrm{sgn}(n_i(D)) = (-1)^{D+1}$; threshold $D_0 = 0$
  sharp.

- **AP-CY90 -- Coxeter-void at $N = 11$ (Medium).**
  Siegel-weight ladder has no Niemeier correspondent at $N = 11$
  (Coxeter-void: $h(A_{10}) = 11$ unique, no filler). "$4A_5$ Niemeier"
  does NOT exist.
  **Counter**: four-regime taxonomy naive / substitute / void /
  Leech-escape; verify root-system rank sums to 24.

- **AP-CY91 -- $\mu_8$ vs $\mu_{16}$ cover base (Medium).**
  $\mu_8$ Čech cocycle on $\overline{\mathcal A_2} \setminus (H_1
  \cup H_4)$; $\mu_{16}$ refinement on $\overline{\mathcal A_2}
  \setminus H_1$ (metaplectic cover over $H_4$). Order 16 from
  $\mathrm{ord}_{H_4}(\Delta_5) = 2$ plus metaplectic doubling.
  **Counter**: specify cover base and obstruction divisor.

- **AP-CY92 -- $\mathfrak u_{\zeta_8}$ finite Hopf dimension (High).**
  $8^{129}$ is NOT Hopf-quotient dimension; $\mathfrak u_{\zeta_8}$
  is pro-finite with infinite imaginary cone. No integer $N_\star$
  between $N = 2$ ($d = 22$) and $N = 3$ ($d = 238$) gives
  $d(N_\star) = 63$.
  **Counter**: reinterpret as $\dim \mathfrak b^{\mathrm{re}, +}
  _{\zeta_8}$ or Kerler-Lyubashenko projective-index cardinality.

- **AP-CY93 -- YD Borcherds exponent $\lceil n/2 \rceil$ (High).**
  YD-tower $\delta^{(n)} \propto (\Phi_{10}/\eta^{24})^{\lceil n/2
  \rceil}$ is wrong. Even-arity Schauenburg bracket-square adds
  Bruinier Heegner-divisor twist; correct weight is $\lfloor n/2
  \rfloor + 1$ with effective sequence $\{1, 2, 2, 3, 3, 4, 4,
  \ldots\}$.
  **Counter**: expand full cocycle via Catalan-Padovan trees at
  arities $\geq 4$.

- **AP-CY94 -- Fake-Monster R-matrix theta absence (Medium).**
  $R^{\mathrm{FM}}(u, Z) = (1 + \hbar \Omega_{\mathrm{II}_{25, 1}}/u)
  \cdot \theta^{\mathrm{FM}}(u, Z)$; Leech-theta cocycle with Borcherds
  bicharacter $\epsilon(\alpha, \beta) = (-1)^{(\alpha, \beta) +
  (\alpha, \alpha)(\beta, \beta)}$ is not absent.
  **Counter**: include $\theta^{\mathrm{FM}}$; cite Borcherds 1986 §5.

- **AP-CY95 -- Leech-Conway universal ratio exception (Medium).**
  Universal $\ell_X/\ell_Y = c_+(L_X)/c_+(L_Y)$ BREAKS on Leech-Conway
  row: $c_+(\Lambda_{24}) = 24$, $\ell_{\mathrm{Conway}} = 2$; no
  Fricke involution on positive-definite lattice.
  **Counter**: restrict universal identity to four rows
  Monster/Enriques/K3/Fake-Monster; flag Leech-Conway exception.

- **AP-CY96 -- Six routes as single $\Phi_3$-application (Critical).**
  Six routes to $G(K3 \times E)$ are six DIFFERENT constructions, not
  six $\Phi_3$-applications. Generator-level stratification
  $\rho^{R_i} \in \{3, 12, 24\}$ falsifies six-way isomorphism.
  **Counter**: assemble five non-source routes into pentagon COLIMIT
  over named intertwiners $\beta_{13}, \beta_{34}, \beta_{45},
  \beta_{56}, \beta_{61}$; $R_2$ Borcherds is source.

- **AP-CY97 -- Absolute HPD on $K3 \times E$ (High).**
  Absolute Kuznetsov HPD blocked by Fano obstruction ($\omega_Y \simeq
  \mathcal O_Y$).
  **Counter**: use RELATIVE HPD over $E$ via Kuznetsov-Markushevich
  2009 arXiv 0904.4330.

- **AP-CY98 -- $\kappa_{\mathrm{ch}} = \chi(\mathcal O_X)$ at $d \geq
  3$ (Critical).**
  Hodge supertrace identification holds at $d = 2$ only. At $d \geq 3$
  fails: odd-$d$ Serre forces $\chi = 0$ while $\kappa_{\mathrm{ch}}$
  remains nonzero via products-additivity.
  **Counter**: state Beauville-Bogomolov tri-stratum: odd-$d$ Serre /
  strict-CY even-$d$ / holomorphic-symplectic.

- **AP-CY99 -- Missing row B in five-archetype (Medium).**
  Landscape omitting BKM crown row B at $\kappa_{\mathrm{ch}} +
  \kappa_{\mathrm{ch}}^! = 8$ is incomplete.
  **Counter**: $G/L/C/M/\mathbf B$ with $\kappa + \kappa^! \in \{0, 8,
  13, 250/3, 98/3\}$; $\mathbf B$ witnessed by $(K, \hbar^2) = (8,
  -1/8)$.

- **AP-CY100 -- GRT$_1$ unconditional transitivity (High).**
  GRT$_1$ transitivity on super-EK-quantisable BKMs is
  SCOPE-RESTRICTED to Koszul locus through weight 12 via
  Deligne-Goncharov motivic alignment; conditional on Zagier-Hoffman
  above.
  **Counter**: always cite motivic weight threshold; explicit
  obstruction $\mathrm{ob}^{\mathrm{GN}} \in H^2(\mathfrak{grt}_1;
  \widehat{\mathrm{Imag}})$.

- **AP-CY101 -- $\chi_3$ cohomological degree (Medium).**
  $\chi_3$ is NOT Etingof-Kazhdan deformation (degree 2) or
  Drinfeld-centre deformation (degree 4); it is degree-3 class
  classifying GN Borcherds twist.
  **Counter**: $\chi_3 \in H^3(\mathfrak{grt}_1; \mathrm{Imag})$.

- **AP-CY102 -- Plancherel single-input (High).**
  $\{H^*_T(\mathrm{Hilb}^{[n]}(K3))\}$ pro-limit does NOT converge
  from MO alone; requires COMPOSITE MO + Grojnowski-Nakajima + EK
  super-quantisation.
  **Counter**: state all three inputs.

- **AP-CY103 -- $\mathrm{CoHA}(\mathbb C^3) = \mathcal W_{1 + \infty}$
  full algebra (High).**
  $\mathrm{CoHA}(\mathbb C^3) = Y^+$ positive half only; Hall-Drinfeld
  doubling needed for full $\mathcal W_{1 + \infty}$.
  **Counter**: write $Y^+(\widehat{\widehat{\mathfrak{gl}}}_1)$; apply
  $\mathcal D_\hbar(-)$ explicitly.

- **AP-CY104 -- Refined topological vertex on non-toric (High).**
  Refined topological vertex is TORIC-only; $K3 \times E$ refined GW/DT
  off self-dual slice is conjectural.
  **Counter**: tag with `\ClaimStatusConjectured`; cite
  Aganagic-Okounkov 2016 refined stable envelope alternative.

- **AP-CY105 -- KKV semisimple $\mathbf H_{\Delta_5}$-modules (High).**
  KKV BPS with negative / non-integral refinement correspond to
  Jordan-block projective covers, NOT semisimple irreducibles
  (logarithmic CFT scope).
  **Counter**: tempered stratum controls semisimple correspondence;
  flag logarithmic.

- **AP-CY106 -- Real-root halving (Critical).**
  Enriques imaginary-root halving $\mathrm{mult}_{\mathrm{Enr}}(\alpha)
  = c^{K3}(-\alpha^2/2)/2$ does NOT apply to real roots ($D = -1$);
  BKM real-root axiom (Borcherds 1988 Defn 1.1) fixes $\mathrm{mult}
  = 1$.
  **Counter**: restrict halving to $D \geq 0$ imaginary cone.

- **AP-CY107 -- Class pair $\{2A, 2B\}$ twining identity (Medium).**
  $\iota$-class $2A$ and non-$\iota$ order-2 class $2B$ have DIFFERENT
  twining genera: $f^{2A}_{\mathrm{En}}(1, \pm 1) = 0$ vs
  $f^{2B}_{\mathrm{En}}(1, \pm 1) = -8$.
  **Counter**: split $\{2A, 2B\}, \{4A, 4B\}, \{6A, 6B\}$; distinguish
  $\iota$-class from non-$\iota$ members of $\mathcal C_\iota$.

## Wave 20-24 reinforcement anti-patterns: AP-CY108 through AP-CY114

These entries reinforce thin coverage identified through a systematic
coverage audit of the Wave 20-24 arc. They extend AP-CY84 / AP-CY86 /
AP-CY92 / AP-CY94 / AP-CY95 / AP-CY100 with the dedicated richer
format (severity / trigger / ghost / error / correction / primary
citation / inscription anchor / cross-reference).

- **AP-CY108 -- Universal ratio-of-levels $\ell_X / \ell_Y = c_+(L_X) /
  c_+(L_Y)$ as per-archetype numerology (High).**
  - *Trigger*: any statement that the Lusztig level $\ell_X$ of a
    $\Psi$-image BKM is "algebra-specific" or "per-archetype".
  - *Ghost error*: "$\ell_X$ is per-family numerology with no
    cross-family structure" (typical in first-draft Frenkel--Zhu
    adaptations on a single lattice).
  - *Correct statement*: $\ell_X / \ell_Y = c_+(L_X) / c_+(L_Y)$ is a
    UNIVERSAL identity across the four $\Psi$-image rows
    Monster / Enriques / K3 / Fake-Monster, with
    $(c_+, \ell) = (1, 2), (2, 4), (4, 8), (25, 50)$.
    Mukai-doubling factor $\ell = 2 c_+(L_X)$ cancels in the ratio,
    making the law a SIGNATURE-theoretic invariant independent of
    the doubling convention.
  - *Universal-exception clause*: Leech--Conway row $(\Lambda_{24},
    c_+ = 24, \ell_{\mathrm{Conway}} = 2)$ BREAKS the identity
    because the positive-definite Leech lattice admits no Fricke
    involution; this is the sole exception and is structural, not
    numerological (cf. AP-CY95).
  - *Three verification paths*: (i) lattice-signature invariant
    $c_+(L)$ computed from Gram matrix; (ii) Fricke-monodromy order
    on $L \otimes \mathbb R$; (iii) Lusztig-quantum-group grading
    $\mathrm{gr}_\ell U_q(\mathfrak g_L) / I_\ell$. All three
    predict the same ratio.
  - *Primary*: Scheithauer 2008 *Duke Math J* 143 §4 (lift-level
    prefactor); Gritsenko--Nikulin 1998 *Duke Math J* 92 §2 (Mukai
    doubling).
  - *Inscription anchor*: `chapters/theory/universal_ratio_of_levels.tex`;
    downstream check in `compute/lib/psi_image_ratio_consistency.py`.
  - *Cross-reference*: refines AP-CY95 (exception side);
    complements AP-CY99 (row B at $\kappa + \kappa^! = 8$);
    interacts with Vol I $\kappa$-families via $\Phi$.

- **AP-CY109 -- GRT$_1$-transitivity on $\mathrm{Quant}(\mathfrak g_{\Delta_5})$
  as unconditional Etingof--Kazhdan Part V transport (High).**
  - *Trigger*: citing Etingof--Kazhdan 2000 Part V verbatim for
    $\Psi$-image BKMs.
  - *Ghost error*: "$\mathrm{GRT}_1$ acts unconditionally on
    $\mathrm{Quant}(\mathfrak g_{\Delta_5})$ extending
    Etingof--Kazhdan Part V verbatim."
  - *Correct statement*: the $\mathrm{GRT}_1$-action is a
    SCOPE-RESTRICTED torsor on
    $\mathrm{Quant}^{\mathrm{GN},\mathrm{Koszul}}(\mathfrak g_{\Delta_5}) /
    (\mathbb Z / 2)_{\mathrm{super}}$ with an EXPLICIT obstruction
    cocycle $\mathrm{ob}^{\mathrm{GN}} \in
    H^2(\mathfrak{grt}_1; \widehat{\mathrm{Imag}})$.
  - *Vanishing criterion*: $\mathrm{ob}^{\mathrm{GN}}$ vanishes on
    the Koszul locus via Deligne--Goncharov motivic weight
    alignment through weight 12; CONDITIONAL on Zagier--Hoffman
    above weight 12.
  - *Quantitative obstruction*: the BKM imaginary cone has
    Hardy--Ramanujan growth
    $\dim \mathrm{Imag}_N \sim N^{-27/4} \exp(4\pi\sqrt N)$,
    breaking the finite-rank Etingof--Kazhdan Part V transport
    verbatim (EK Part V requires finite-dimensional representation
    in each degree; the BKM imaginary cone is infinite-dimensional
    in every positive degree).
  - *Three verification paths*: (i) direct computation of
    $\mathrm{ob}^{\mathrm{GN}}$ on the Kac--Moody subsector where
    it vanishes; (ii) Deligne--Goncharov motivic periods through
    weight 12 (established); (iii) growth rate as obstruction to
    finite-rank transport.
  - *Primary*: Etingof--Kazhdan 2000 *Selecta Math* 6 Part V;
    Deligne--Goncharov 2005 *Ann Sci ENS* 38; Borcherds 1995
    *Invent Math* 120 (Hardy--Ramanujan growth).
  - *Inscription anchor*: `chapters/theory/grt1_scoped_transitivity.tex`;
    `compute/lib/grt1_obstruction_weight12.py`.
  - *Cross-reference*: extends AP-CY100 (severity upgrade with
    explicit cocycle and growth-rate argument); interacts with
    AP-CY101 ($\chi_3$ cohomological degree).

- **AP-CY110 -- Persson--Volpato $M_{12}$ Enriques mass formula as
  Gannon sign-flipped Mathieu (Critical).**
  - *Trigger*: any equation of the form
    "$f^{\mathrm{Enr}}_g = \epsilon \cdot f^{K3}_g$" for a class
    $g \in M_{12}$ with $\epsilon \in \{\pm 1\}$ presented as the
    Enriques mass formula.
  - *Ghost error*: "$M_{12}$-moonshine for Enriques is the Gannon
    2016 Mathieu theorem with a sign change in the twining genus."
  - *Correct statement*: the Persson--Volpato 2013 construction is
    $M_{12} \hookrightarrow M_{24}$ as a POINT-STABILISER, yielding
    a VIRTUAL signed $M_{12}$-character decomposition of the
    $\iota$-invariant of $f^{K3}$. The mass formula has three
    genuinely separate components:
    (a) centraliser-weighted trace-sum (Schur orthogonality-weighted,
        not unit-weighted; cf. AP-CY88);
    (b) sign-alternating positivity
        $\mathrm{sgn}(n_i(D)) = (-1)^{D + 1}$ with sharp threshold
        $D_0 = 0$ (Mersenne-flavoured exceptional locus
        $\{7, 15, 31, 47, 55, \ldots\}$; cf. AP-CY87);
    (c) Plancherel-norm identity requiring composite input
        (Grojnowski--Nakajima + super-EK; cf. AP-CY102).
  - *Virtual-character correction*:
    $f_{\mathrm{En}}(0, 1) = 5 = 16 - 11$ is a VIRTUAL signed
    $M_{12}$-character sum, NOT a direct irreducible
    decomposition; the integer 5 is not an ATLAS dimension
    but a signed sum of ATLAS dimensions 16 and 11.
  - *Three verification paths*: (i) Persson--Volpato 2013 §4
    $\iota$-halving of $f^{K3}$; (ii) centraliser-weighted
    projector on $M_{12}$-invariant subspace; (iii) sign
    alternation by $D \pmod 4$ checked against Gannon 2016 Thm 1.2.
  - *Primary*: Persson--Volpato 2013 *Commun Num Theor Phys* 8 §4;
    Gannon 2016 *Adv Math* 306 §3.
  - *Inscription anchor*: `chapters/connections/enriques_m12_mass.tex`;
    `compute/lib/enriques_m12_virtual_character.py`.
  - *Cross-reference*: extends AP-CY86 (upgrades from "direct
    moonshine fails" to full three-component mass formula
    inventory); coordinates with AP-CY87, AP-CY88, AP-CY89, AP-CY102.

- **AP-CY111 -- Conway super-twin three-defect inventory (Critical).**
  - *Trigger*: citations to Duncan 2007 for the Conway super-twin
    $V^{s\natural}$ placed as an independent fifth $\Psi$-image.
  - *Three separate ghost errors*:
    (a) Venue: citing "Duncan 2007 *MRL* 14" — the correct venue is
        *Duke Math J* 139;
    (b) Construction: claiming $V^{s\natural}$ is built from an
        $E_8$ super-lattice — the correct construction is
        $A(\Lambda_{24})^+ \oplus A(\Lambda_{24})^{\mathrm{tw}, +}$,
        a fermionic VOA on the Leech lattice;
    (c) Central-charge signature: claiming
        $c_+(\Lambda_{24}) = 0$ to justify
        $(K, \hbar^2) = (2, -1/2)$ independently of Monster —
        the correct value is $c_+(\Lambda_{24}) = 24$ from the
        positive-definite $(24, 0)$ signature.
  - *Correct statement*: $V^{s\natural}$ is the $\mathbb Z/2$-super-twin
    of $V^\natural$ INSIDE the Monster row of the landscape, not an
    independent fifth row. Its $(K, \hbar^2)$ inherits from
    Monster; the separate $\mathbb Z/2$-graded structure does not
    purchase an independent $\Psi$-image slot.
  - *Three verification paths*: (i) Duncan 2007 *Duke Math J* 139
    §6 commutative diamond; (ii) Leech lattice Gram matrix
    signature $(24, 0)$; (iii) Scheithauer 2008 Thm 3.2
    alternative reading as Fake-Monster $\mathbb Z/2$-subsector
    (same conclusion via different embedding).
  - *Primary*: Duncan 2007 *Duke Math J* 139; Scheithauer 2008
    *Duke Math J* 143 Thm 3.2.
  - *Inscription anchor*: `chapters/theory/conway_super_twin_inventory.tex`.
  - *Cross-reference*: extends AP-CY84 (explicit three-defect
    inventory); coordinates with AP-CY34 (Conway $V^{s\natural}$
    as bosonic $\Psi$-image).

- **AP-CY112 -- $\Psi$ non-surjectivity three-path verification for
  $24 A_1$ counterexample (High).**
  - *Trigger*: claims of $\Psi$-surjectivity on
    $\mathrm{BKM}^{\mathrm{GN}}$ defended by a single lattice-rank
    count.
  - *Ghost error*: "$\Psi : \mathrm{CY}^{\mathrm{Siegel-aut}} \to
    \mathrm{BKM}^{\mathrm{GN}}$ surjects onto all reflective
    Scheithauer GKMs."
  - *Correct statement*: $24 A_1$ Niemeier Borcherds product is a
    super-EK-quantisable reflective GKM OUTSIDE
    $\mathrm{Im}(\Psi_{d \in \{2, 3\}})$, witnessed by THREE
    independent mismatches:
    (i) *lattice-rank signature*: $(25, 1)$ for $24 A_1$ mismatches
        the CY-$d$ Mukai-lattice signature at $d \in \{2, 3\}$
        (signature $(4, 20)$ for $d = 2$ K3, signature $(3, 3)$
        or $(4, 2)$ for $d = 3$ depending on CY3 type);
    (ii) *Serre-parity / Caldararu 2005*: 24 real-root weight-1
        classes in $\mathrm{HH}_0$ are ruled out by the parity
        constraint on the Mukai pairing for smooth projective
        Calabi--Yau;
    (iii) *modular weight*: the prospective image
        $\kappa_{\mathrm{BKM}} = 12$ would collide with
        Fake-Monster but at the wrong lattice signature
        $(25, 1)$ versus Fake-Monster's $(25, 1)$-via-$\mathrm{II}_{25, 1}$
        with different Gram matrix.
  - *Three verification paths* (intrinsic to the claim): listed
    above; any one suffices to rule out
    $24 A_1 \in \mathrm{Im}(\Psi)$.
  - *Primary*: Scheithauer 2000 Thm 6.2; Caldararu 2005 *Adv Math*
    194 §3; Borcherds 1995 *Invent Math* 120.
  - *Inscription anchor*: `chapters/examples/psi_nonsurj_24A1.tex`;
    `compute/lib/psi_nonsurj_24A1_three_paths.py`.
  - *Cross-reference*: refines AP-CY83 ($\Psi$-surjectivity scope);
    provides the canonical worked counterexample.

- **AP-CY113 -- $\mathfrak u_{\zeta_8}$ arithmetic gap at $d(N_\star) =
  63$ (High).**
  - *Trigger*: any claim that $\mathfrak u_{\zeta_8}$ has Hopf-quotient
    dimension $8^{129}$ (or any finite integer power of 8).
  - *Ghost error*: "$\dim_{\mathbb C} \mathfrak u_{\zeta_8} =
    8^{129}$ as a finite-dimensional Hopf algebra."
  - *Correct statement*: in the truncation sequence
    $(d(1), d(2), d(3)) = (2, 22, 238)$ for the
    $\mathfrak u_{\zeta_8}$ tower, the prospective index $d(N_\star) = 63$
    (arising from the $8^{129}$ reinterpretation attempt) has no
    integer $N_\star$ solution: 63 is strictly between $d(2) = 22$
    and $d(3) = 238$, and the sequence is monotone strictly
    increasing with no gap fill.
  - *First-principles basis*: this arithmetic gap is the direct
    first-principles basis for rejecting $8^{129}$ as a
    Hopf-quotient dimension. The correct reinterpretation is
    $\dim \mathfrak b^{\mathrm{re}, +}_{\zeta_8}$ (real-root
    positive Borel) or Kerler--Lyubashenko projective-index
    cardinality.
  - *Three verification paths*: (i) direct enumeration of
    $d(N)$ via Lusztig--Kashiwara PBW basis; (ii) Lusztig 1990
    quantum-Frobenius exact sequence forcing infinite imaginary
    cone; (iii) Kerler--Lyubashenko 2001 projective-index count
    as alternative.
  - *Primary*: Lusztig 1990 *Contemp Math* 110; Kerler--Lyubashenko
    2001 *Lecture Notes Math* 1765.
  - *Inscription anchor*: `chapters/examples/u_zeta8_arithmetic_gap.tex`;
    `compute/lib/u_zeta8_dim_truncation.py`.
  - *Cross-reference*: extends AP-CY92 (Hopf dimension);
    coordinates with AP-CY93 (YD Borcherds exponent).

- **AP-CY114 -- Fake-Monster $R$-matrix YBE term-by-term
  $\hbar$-verification (High).**
  - *Trigger*: any assertion of Yang--Baxter for
    $R^{\mathrm{FM}}(u, Z)$ without explicit $\hbar$-order
    verification.
  - *Ghost error*: "YBE holds for $R^{\mathrm{FM}}(u, Z)$ by
    general rational-Yangian YBE" (elides the theta factor).
  - *Correct statement*: $R^{\mathrm{FM}}(u, Z) = (1 + \hbar
    \Omega_{\mathrm{II}_{25, 1}} / u) \cdot \theta^{\mathrm{FM}}(u, Z)$
    with the Fake-Monster theta prefactor
    $\theta^{\mathrm{FM}}(u, Z) = \theta_\Lambda(u, Z) /
    \eta^{24}(\tau)$ (cf. AP-CY94). YBE is verified
    term-by-term in $\hbar$:
    - $O(\hbar^0)$: theta triple product identity on
      $\mathrm{II}_{25, 1}$ lifted to three-factor
      Borcherds denominator (Borcherds 1990 Thm 10.4);
    - $O(\hbar^1)$: classical $r$-matrix Jacobi identity
      for $\Omega_{\mathrm{II}_{25, 1}}$ on the full 26-dim
      Cartan (Drinfeld 1989 §4);
    - $O(\hbar^n), n \geq 2$: Etingof--Kazhdan 1996 §6
      quantisation functor applied inductively, with theta
      factor treated as abelian twist.
  - *Three verification paths*: (i) Borcherds 1990 Thm 10.4
    denominator match at $O(\hbar^0)$; (ii) Leech-theta expansion
    $\theta_\Lambda / \eta^{24}$ matched to Fake-Monster
    denominator; (iii) Yangian YBE for
    $\Omega_{\mathrm{II}_{25, 1}}$ at $O(\hbar^1)$ and higher
    via EK.
  - *Primary*: Borcherds 1990 *Contemp Math* 138 Thm 10.4;
    Drinfeld 1989 *Leningrad Math J* 1 §4; Etingof--Kazhdan 1996
    *Selecta Math* 2 §6.
  - *Inscription anchor*: `chapters/theory/fake_monster_r_matrix_ybe.tex`;
    `compute/lib/fake_monster_ybe_hbar_order.py`.
  - *Cross-reference*: extends AP-CY94 (theta absence, supplies the
    explicit theta prefactor and YBE proof); coordinates with
    AP-CY109 ($\mathrm{GRT}_1$ scope via EK §6).

## Cross-volume anti-patterns from Wave 20-24 (AP-Vol-III-prop)

- **AP-Vol-III-prop-1 -- bare $\kappa$ (Critical, recurrent).**
  Bare $\kappa$ forbidden in Vol III. Four distinct $\kappa$'s on
  $K3 \times E$: $\kappa_{\mathrm{ch}} = 3$, $\kappa_{\mathrm{cat}} =
  0$, $\kappa_{\mathrm{BKM}} = 5$ **(paramodular $\Phi_{10} = \Delta_5^2$
  convention; Fake-Monster $\Phi_{12}$ convention gives $12$ — AP5
  dual-indexing, pending landscape-census lock per canonical preamble
  row "$\kappa_{\mathrm{BKM}}(\mathbf H_{\Delta_5})$ cross-volume value"
  / AP-CY49)**, $\kappa_{\mathrm{fiber}} = 2$.
  **Counter**: always subscript $\kappa_{\bullet}$; always name the
  $\Phi_N$ denominator when stating $\kappa_{\mathrm{BKM}}$.

- **AP-Vol-III-prop-2 -- $N = 1$ coincidence inflation (Critical).**
  $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal
  O_{\mathrm{fiber}})$ fails at $N \geq 2$. Correct universal:
  $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$.
  **Counter**: cite Borcherds weight theorem; verify at multiple $N$.

- **AP-Vol-III-prop-3 -- CoHA-vs-full-Yangian (High).**
  $\mathrm{CoHA}(\mathbb C^3) = Y^+$ only; full $\mathcal W_{1 +
  \infty}$ needs Hall-Drinfeld doubling.
  **Counter**: state half/full explicitly.

- **AP-Vol-III-prop-4 -- six routes as $\Phi$-applications (Critical).**
  Six routes to $G(K3 \times E)$ are different constructions of same
  output, not six functor evaluations.
  **Counter**: pentagon colimit over named intertwiners; never
  "six-way isomorphism".

## Updated statistics (post exhaustive audit)

| Category                                              | Count |
| ----------------------------------------------------- | ----: |
| CY-specific original (AP-CY1--AP-CY33)                |    33 |
| CY-specific swarm (AP-CY34--AP-CY49)                  |    16 |
| CY-specific historical W14-W22 (AP-CY50--AP-CY82)     |    33 |
| CY-specific Wave 20-24 (AP-CY83--AP-CY107)            |    25 |
| CY-specific Wave 20-24 reinforcement (AP-CY108--AP-CY114) | 7 |
| CY-specific foundational W1-W13 (AP-CY115--AP-CY127)  |    13 |
| CY-specific VERIFIED-template W14-W19 (AP-CY128--AP-CY140) | 13 |
| Cross-programme (AP150--AP164)                        |    15 |
| Formula-mechanical (FM24--FM27)                       |     4 |
| Cross-volume Vol-III-prop (1--4)                      |     4 |
| **Total catalogued**                                  | **163** |
| Critical severity                                     |    28 |
| High severity                                         |    68 |
| Medium severity                                       |    44 |
| Low severity                                          |     3 |

Three Wave-20-24 anti-patterns have already driven 5+ independent
fixes: AP-CY83 ($\Psi$-surjectivity scope, 6 fixes across
\texttt{cy\_to\_chiral.tex} + downstream); AP-CY84 (Conway
$V^{s\natural}$ 5th $\Psi$-image, 4 fixes + conjecture downgrade + 4
downstream ref updates); AP-CY86 (direct $M_{12}$ moonshine, 5 fixes
across \texttt{k3e\_bkm\_chapter.tex}).


## K3 chiral bialgebra anti-patterns from Waves 14-22 (historical + structural, April 2026)

These AP-CY entries capture mathematical-content corrections and
structural patterns surfaced across the adversarial-swarm waves 14
through 22 before the Wave 23-26 closure campaign. Every pattern
below was the subject of at least one cross-volume retraction or
formal correction.

- **AP-CY50 -- $(c_{4d}, c_{2d})$ central-charge reversal (Critical).**
  Wave-14 erroneously retracted Wave-13's $(107/6, -214)$ to
  $(26, -312)$ via the formula $(12(g-1) + 7n)/6$. Failure mode: the
  formula fails the $\mathrm{SU}(2)$ $N_f = 4$ cross-check ($n = 4$
  gives $8/3$ not $7/6$). Wave-15 Gaiotto healed via the correct
  $(5n - 13)/6 = (2n_v + n_h)/12$ at $n = 24$ with trinion
  $(n_v, n_h) = (63, 88)$.
  **Counter**: final stable $(c_{4d}, c_{2d}) = (107/6, -214)$,
  anchored by Chacaltana--Distler 2010 §5.14; Beem--Rastelli 2013
  $c_{2d} = -12 c_{4d}$. WOV-2 locks this. Wave-16/17 propagated the
  correction across ~20 cross-volume files; any residual $(26, -312)$
  or $(26, 312)$ fragments must be reverted.

- **AP-CY51 -- Monster BKM hyperbolic Cartan rank (Critical).**
  Wave-16 erroneously asserted that the Monster BKM has hyperbolic
  Cartan rank 26 (inherited from confusion with Fake-Monster).
  Monster sits on $\mathrm{II}_{1,1}$ (rank 2); Fake-Monster sits on
  $\mathrm{II}_{25,1}$ (rank 26); K3-BKM sits on $\Lambda^{2,1}_{II}$
  (rank 3). Wave-17 Drinfeld correction: four convergent routes
  (Mukai-doubling, Fricke $w_1$, super-EK $\mathbb{Z}/2$,
  Conway--Norton identity-class) all give $\ell_{\mathrm{Monster}} = 2 = 2c_+(\mathrm{II}_{1,1})$.
  **Counter**: rank 2 Monster, rank 26 Fake-Monster, rank 3 K3-BKM;
  Borcherds 1992 *Invent Math* 109 Thm 3 + Gritsenko--Nikulin 1998 §3.
  Never conflate the three.

- **AP-CY52 -- $c_3$ coefficient normalisation (High).**
  Wave-16 erroneously asserted $c_3 = 176256 \cdot [H_3]$. Failure mode:
  $176256 = p_{24}(5) = \chi(\mathrm{Hilb}^5(\mathrm{K3}))$, unrelated
  to the $\phi_{10,1}$ Fourier expansion. Wave-17 correction:
  $c_3 = -8 \cdot [H_3]$ via four independent paths (direct
  $\theta_1^2/\eta^6$, theta decomposition, $\phi_{10,1}/\eta^{24}$,
  Hecke congruence). Wave-18 Costello: factor
  $-22032 = 176256/(-8)$ is the conversion ratio between the
  Bruinier reduced-class convention ($c_3 = -8$) and the
  Gritsenko--Nikulin Cartan-matrix convention ($c_3 = 176256$ up to
  the Cartan prefactor).
  **Counter**: use **Bruinier reduced-class convention** throughout.
  Canonical $c_3 = -8$; any reference citing $176256$ must annotate
  with the conversion $176256 = -22032 \cdot (-8)$ and redirect to
  the Bruinier normalisation. WOV-5 locks.

- **AP-CY53 -- Umbral Niemeier labelling rule (High).**
  Wave-18 erroneously asserted "$N \mid 24$" divisor rule for $A_{N-1}$
  umbral labelling. Wave-19 Gaiotto correction: the rule is
  "$(N-1) \mid 24$" OR substitute a Niemeier root system.
  **Counter**: $A_{N-1}$ for $N \in \{2, 3, 4, 5\}$ via
  $(24/\mathrm{rk}(A_{N-1})) \cdot A_{N-1}$. At $N = 6$ the rule
  forces re-anchoring to Niemeier root system $6D_4$ (since $4A_5$
  is not Niemeier); umbral group $3.\mathrm{Sym}_6$ (order 2160);
  $k_6 = 9/2$.

- **AP-CY54 -- $\zeta(3,3,3,3)$ numerical value (High).**
  Wave-17 Etingof draft used $\zeta(3,3,3,3) = 0.0028565$; correct
  value $0.000295999\ldots$ (10× error). Wave-19 in-flight correction
  to $c_{12}^{(9)} = 6.1795 \times 10^{-13}$. First genuinely depth-4
  MZV at weight 12; entered the pentagon tower at this point.
  **Counter**: numerical MZV values must be cross-checked against two
  independent evaluators (Borwein-Bailey tables + Brown 2012 motivic
  basis numerics); never trust a single-source value. Every MZV-bearing
  formula must be regression-tested.

- **AP-CY55 -- Integer heterotic-lift coefficient $c(1,2,\pm 2)$
  (High).** Wave-21 Witten integer heterotic lift used
  $c(1, 2, \pm 2) = +1$. Wave-22 Witten correction: $c(1, 2, \pm 2) = -2$
  via direct $\eta^{18} \theta_1^2$ expansion + DMZ 2012 BPS-counting
  cross-check + holomorphic-anomaly third path. The sign flip changed
  three downstream computations.
  **Counter**: integer-lift coefficients must be cross-verified via
  three independent paths (direct Fourier expansion, BPS counting,
  holomorphic-anomaly / Borcherds product). Single-path lifts are
  fragile under convention shifts.

- **AP-CY56 -- Humbert $H_4$ vs $H_8$ identification (High).**
  Wave-15 inscription described $H_4$ as the "$\mathbb{Q}(\sqrt 2)$-RM
  locus" at Vol I `chiral_climax_platonic.tex:1748`. Wave-16 Kazhdan
  correction: $H_4$ is the $(2, 2)$-isogeny quotient of $E_1 \times E_2$
  with $\mathrm{End} \supset \mathbb{Z}[2i]$; the $\mathbb{Q}(\sqrt 2)$-RM
  locus is $H_8$, not $H_4$.
  **Counter**: $H_4$ has monodromy order 2 (van der Geer 1988 Ch. IX);
  $H_8$ has monodromy order 16. Humbert divisor descriptions must name
  the arithmetic characterisation (isogeny type, endomorphism ring)
  explicitly.

- **AP-CY57 -- Theorem B scope narrowness (Medium).**
  Wave-15 statement: bar-cobar inversion on $\overline{\mathcal{A}_2}
  \setminus (H_1 \cup H_4)$. Wave-18 Beilinson tightening: strict
  chain-level bar-cobar on $\overline{\mathcal{A}_2} \setminus
  \bigcup_{n\,\mathrm{admissible}} H_n$ — all admissible Heegner
  divisors excluded, not just $H_1 \cup H_4$.
  **Counter**: programme-canonical scope is the Wave-18 Beilinson
  tightening. "Admissible" means $n \equiv 0, 3 \pmod 4$. Older
  inscriptions excluding only $H_1 \cup H_4$ must be updated via the
  constitutional concordance patch.

- **AP-CY58 -- Borcherds weight vs Gritsenko weight (Medium).**
  The K3-BKM denominator is $\Delta_5$ (Gritsenko additive), NOT
  $\Phi_{12}$ (Borcherds multiplicative). Wave-16 Gaiotto discipline.
  **Counter**: $\mathrm{Borch}(\phi_{0,1}^{K3}) = \Phi_{12}$ on
  Fake-Monster $\mathrm{II}_{25,1}$ at weight 12; $\mathrm{Grit}(\eta^9
  \vartheta_1) = \Delta_5$ on paramodular $K(1)$ at weight 5. Two
  different constructions, two different weights. Never conflate.

- **AP-CY59 -- Two-$\hbar$ convention conflation (High).**
  $\hbar^{\mathrm{Drinfeld}} = 2\pi i / \ell$ (Lusztig-type root-of-unity
  specialisation) and $\hbar^{\mathrm{BV}}$ (Costello 1-loop expansion
  parameter) are semantically distinct quantisation parameters. They
  agree numerically at $\hbar^2 = -1/8$ for $\ell = 8$, but via different
  mechanisms.
  **Counter**: every $\hbar$-bearing identity must name which $\hbar$ is
  in play. Use AP151 bridge notation across all three volumes.
  Pattern: $\hbar^{\mathrm{Drinfeld}}$ for root-of-unity; $\hbar^{\mathrm{BV}}$
  for loop-counting; `\hbar_{\mathrm{Lusztig}}` / `\hbar_{\mathrm{BV}}`
  subscripts in manuscript when the two coexist.

- **AP-CY60 -- Sylvester vs Feingold--Frenkel signature (Medium).**
  Naive Sylvester principal-minor test applied to $G_{\mathrm{BKM}}$
  gives $(2, 0, -32)$, which is misleading (the $m_2 = 0$ is an
  isotropic $S_3$-symmetry artefact).
  **Counter**: use Feingold--Frenkel 1983 eigenvalue-based signature
  $\{+4, +4, -2\}$, true signature $(2, 1)$; Sylvester is a trap
  here. Cache 17-BKM-signature.

- **AP-CY61 -- Archimedean Schmidt parameter conflation (Medium).**
  Two Schmidt parameter pairs appear depending on Siegel-form target.
  $(17/2, 15/2)$ is the Schmidt parameter for $\Delta_{10}$
  (holomorphic discrete series on $\mathrm{Sp}_4(\mathbb{R})$);
  $(7/2, 5/2) \otimes \mathrm{sgn}_{\mathbb{R}}$ is the Schmidt
  parameter for $\Delta_5$ on the Maass-spin cover.
  **Counter**: both are correct for their respective forms. Name the
  form explicitly when quoting either pair. Conflation produces
  silent type errors in local-global Langlands analyses.

- **AP-CY62 -- CoHA vs chiral algebra type (Critical).**
  $\mathrm{CoHA}_{K3 \times E}$ is an $E_1$-associative algebra (Hall
  product, Schiffmann--Vasserot), not a chiral algebra. Chiralisation
  requires the explicit $\Phi_3$-arrow.
  **Counter**: $\mathbf{H}_{\Delta_5} = \Phi_3(\mathcal{D}_\hbar
  (\mathcal{Y}^{\mathrm{Hall}}(\mathrm{CoHA}_{K3 \times E})))$. The
  $\Phi_3$-arrow performs the CoHA $\to$ chiral conversion via
  factorisation on the curve $E$. CoHA $\ne$ chiral at the object
  level; the functor $\Phi_3$ makes the passage explicit. (Overlaps
  with classical confusion #6 "CoHA != chiral" in top-15 cache.)

- **AP-CY63 -- $\kappa_{\mathrm{cat}}(K3 \times E) = 0$ (High).**
  Künneth: $\kappa_{\mathrm{cat}}(K3 \times E) = \chi(\mathcal{O}_{K3})
  \cdot \chi(\mathcal{O}_E) = 2 \cdot 0 = 0$ (total space). Confusing
  total $\kappa_{\mathrm{cat}} = 0$ with fibre $\kappa_{\mathrm{fibre}}(K3) = 2$
  or with chiral Künneth-additive $\kappa_{\mathrm{ch}}^K = 3$ is a
  frequent source of error.
  **Counter**: distinguish four $\kappa_\bullet$'s: $\kappa_{\mathrm{cat}}
  = 0$ (total, multiplicative Künneth), $\kappa_{\mathrm{ch}}^K = 3$
  (chiral Künneth-additive), $\kappa_{\mathrm{BKM}}$ (family-specific
  Borcherds), $\kappa_{\mathrm{fibre}}(K3) = 2$. Name the invariant
  explicitly at every site.

## Foundational anti-patterns from Waves 1-13 (AP-CY115 through AP-CY127)

These entries capture the foundational errors surfaced across Waves
1-13 as the CY-to-chiral functor $\Phi$, the four universal properties
$\mathrm{U1}$-$\mathrm{U4}$, the K3 abelian Yangian presentation, and
the $K3 \times E$ CY-3 anchor were being first constructed. Every
pattern below was the subject of at least one explicit retraction
before stabilisation.

- **AP-CY115 -- Functor $\Phi$ presented as construction without
  universal property (High).**
  The CY-to-chiral functor $\Phi \colon \mathrm{CY}^{\mathrm{cat}}_d \to
  \mathrm{ChirAlg}_d^{E_n}$ was initially advertised as a "construction
  that produces chiral algebras from CY categories", without naming the
  four universal properties that pin its codomain uniquely up to
  contractible choice. A functor without a universal property is a
  zoo of arbitrary constructions.
  **Counter**: always accompany every $\Phi$ invocation with the
  applicable universal property $\mathrm{U}i$: $\mathrm{U1}$
  (fibre-dimension: $\Phi_d(\mathcal{C}) \in \mathrm{ChirAlg}^{E_n}_d$
  with $n = n(d)$ scoped per AP-CY56); $\mathrm{U2}$ (Serre: Serre
  functor $\mathbb S_{\mathcal{C}} = [d]$ pulls back to CY trace on
  $\mathrm{HC}^-_d$); $\mathrm{U3}$ (Künneth-additivity:
  $\kappa_{\mathrm{ch}}(\Phi_d(\mathcal{C} \boxtimes \mathcal{D})) =
  \kappa_{\mathrm{ch}}(\Phi_d(\mathcal{C})) +
  \kappa_{\mathrm{ch}}(\Phi_d(\mathcal{D}))$); $\mathrm{U4}$ (Mukai
  faithfulness on full-subcategory generators).

- **AP-CY116 -- CY-A existence at generic $d$ conflated with CY-A$_2$
  (High).** The existence axiom CY-A was originally advertised "holds
  at each $d$". CY-A$_2$ (K3, Enriques, Kummer, bielliptic, $T^4$,
  half-K3) was proved with chain-level witnesses; CY-A$_3$ was
  proved only as an $(\infty, 1)$-existence theorem; CY-A$_{d \geq 4}$
  remains open. The three lanes of CY-A coexist and must never be
  conflated.
  **Counter**: state CY-A$_d$ with $d$ explicit; declare the ambient
  (chain-level / $(\infty, 1)$-categorical / still-open).

- **AP-CY117 -- K3 Yangian abelian presentation as the full
  non-abelian Yangian (Critical).**
  The K3 abelian Yangian $Y^{\mathrm{Heis}}_\hbar(\Lambda_{K3})$ is
  the 24-generator free-boson VOA with quadratic $r$-matrix
  $\Omega_{H^*(K3)} / z$; it is the K3 Heisenberg VSA, not the
  non-abelian K3 Yangian. The non-abelian Yangian requires Matrix
  Miura + Serre constraints and is conjectural for $\mathfrak{g}_{K3} = \mathfrak{so}(4, 20)$.
  **Counter**: always name "abelian" or "non-abelian". The abelian
  presentation (6-part: 24 generators, $R$-matrix from Mukai pairing,
  Drinfeld coproduct from factorisation, $T$-$T$ OPE, abelian Serre
  vacuity, vacuum) is Theorem (Thm `thm:k3-abelian-yangian-presentation`).
  The non-abelian lift is open.

- **AP-CY118 -- BFN affine Yangian at $k = 1$ treated as $k = 0$
  (High).** The Braverman-Finkelberg-Nakajima Coulomb-branch
  construction of the affine Yangian $Y_\hbar(\widehat{\mathfrak{g}})$
  fixes the level at $k = 1$ (the lifting parameter of the equivariant
  $K$-theory of instantons). Treating it as $k = 0$ produces the
  classical Yangian and misses the affinisation shift.
  **Counter**: always cite BFN 2019 *JEMS* 21 §2; level $k = 1$
  mandatory in BFN Coulomb definitions; affine Yangian $\ne$ classical
  Yangian under the BFN construction.

- **AP-CY119 -- $K3 \times E$ as the unique CY-3 anchor (Medium).**
  $K3 \times E$ is THE canonical CY-3 anchor for the programme because
  it (a) is fibred by K3 (where CY-A$_2$ is chain-level proved);
  (b) admits the Gritsenko-Nikulin Borcherds lift $\Delta_5^2 = \Phi_{10}$;
  (c) has $\chi(\mathcal{O}_{K3 \times E}) = 0$ (Künneth) while
  $\kappa_{\mathrm{ch}} = 3$; (d) sits at the Humbert divisor $H_1$ of
  $\overline{\mathcal{A}_2}$. Other CY-3 anchors (quintic, local $\mathbb{P}^2$,
  conifold) are not substitutes; each has its own BKM/non-BKM status.
  **Counter**: never write "CY-3 anchor" bare; always specify
  $K3 \times E$ / quintic / local $\mathbb{P}^2$ / conifold /
  $Y_{(n)}$-family / other.

- **AP-CY120 -- Mukai Lagrangian as total-space Lagrangian (Medium).**
  The Mukai Lagrangian $\mathcal{L}_{\mathrm{Muk}} \subset H^*(K3, \mathbb{Z})$
  is the even self-dual lattice $\mathrm{II}_{4, 20}$ inside the
  full K3 Mukai lattice. It is not the total-space Lagrangian
  of $K3$ as a complex Lagrangian submanifold; it is the lattice-level
  shadow of Mukai's rank-2 polarisation structure (Mukai 1987
  *Invent Math* 77).
  **Counter**: distinguish lattice-level Mukai Lagrangian (rank 24,
  signature $(4, 20)$) from symplectic-geometric Lagrangians in
  $\mathrm{Hilb}^{[n]}(K3)$.

- **AP-CY121 -- $K3$ chiral bialgebra $\mathbf H_{\Delta_5}$
  introduced before Waves 14-17 lattice lock (Critical, historical).**
  Wave 13 introduced $\mathbf H_{\Delta_5}$ at
  $c_{4d} = 26$ rather than the correct $107/6$ (later healed at Wave 15 Gaiotto);
  W13 inscription survived into Vol III abstracts. This is a
  historical archaeological note: the object $\mathbf H_{\Delta_5}$
  is now stable but early advertising overclaimed.
  **Counter**: never cite Wave-13 values without cross-checking against
  the Wave-19 adjudication ledger (`notes/ADJUDICATION_LEDGER_WAVES_14_TO_19.md`).

- **AP-CY122 -- Six-way $G(K3 \times E)$ iso as proved (Critical, W13
  retraction).** Wave 13 advertised a "six-way isomorphism" reaching
  $G(K3 \times E)$ from CoHA / SV / MO / Borcherds / Toda / DMVV routes.
  Wave 14 Gelfand falsified via rank-stratification: $\rho^{R_i} \in \{3, 12, 24\}$
  splits the six routes into three rank-tiers.
  **Counter**: the six-way claim is a pentagon colimit (conjectural,
  CY-C status); never "six-way isomorphism" unqualified. Cites AP-CY48/AP-CY96.

- **AP-CY123 -- Anti-pattern catalogue first inscription as
  manuscript artefact (Low, historical).**
  The AP-CY catalogue was originally placed at
  `appendices/anti_pattern_catalogue.tex` and `\input`ed into
  `main.tex`. Manuscript Metadata Hygiene (2026-04-17) moved it to
  `notes/antipatterns_catalogue.md` as working-notes scaffolding.
  The `.tex` file remains as `.archive` and must not be `\input`ed.
  **Counter**: all AP-CY entries live in `notes/antipatterns_catalogue.md`
  and `notes/first_principles_cache_comprehensive.md`. Never append
  to the archived `.tex` file.

- **AP-CY124 -- Four universal properties $\mathrm{U1}$-$\mathrm{U4}$
  advertised without proofs (High, historical).**
  Waves 1-5 advertised $\mathrm{U1}$-$\mathrm{U4}$ as "the universal
  properties of $\Phi$" with thin constructions and missing proofs.
  Waves 6-9 proved $\mathrm{U1}$ at $d = 2$ (chain-level), $\mathrm{U2}$
  at $d \leq 3$ (Serre pullback), $\mathrm{U3}$ universally (Künneth
  functoriality), $\mathrm{U4}$ at $d = 2$ (Mukai faithfulness).
  **Counter**: every citation of $\mathrm{U}i$ must name its ambient
  ($d$-scope, chain-level vs $(\infty, 1)$, chain homotopy witness).

- **AP-CY125 -- K3 elliptic genus as $\phi_{0,1}$ without factor-of-2
  (High, W13 retraction).** The K3 elliptic genus
  $\mathrm{Ell}_{K3}(\tau, z) = 2 \phi_{0, 1}(\tau, z)$ in the
  Eguchi-Ooguri-Tachikawa 2010 normalisation; the factor 2 is
  $\chi_{\mathrm{top}}(K3)/12 = 2$. Writing
  $\mathrm{Ell}_{K3} = \phi_{0, 1}$ silently halves every downstream
  BPS count.
  **Counter**: verify $c(-1) = 2$ for $\mathrm{Ell}_{K3}$ per
  AP-CY9/AP-CY42; state the Eguchi-Ooguri-Tachikawa normalisation
  (EOT 2011 *Exper Math* 20 Thm 1.1).

- **AP-CY126 -- CoHA $\mathbb{C}^3$ advertised as the K3 Yangian
  target (High, W10 retraction).**
  $\mathrm{CoHA}(\mathbb{C}^3) = Y^+(\widehat{\widehat{\mathfrak{gl}}}_1)$
  is the affine Yangian positive half for $\mathfrak{gl}_1$;
  $\mathrm{CoHA}(K3) = $ K3 Heisenberg (2024 Schiffmann-Vasserot
  result); $\mathrm{CoHA}(K3 \times E)$ is the conjectural BKM object
  $\mathbf H_{\Delta_5}$. Never conflate the three CoHA inputs.
  **Counter**: always name the CoHA source variety. $\mathbb{C}^3$
  gives affine Yangian $\mathfrak{gl}_1$; $K3$ gives K3 Heisenberg;
  $K3 \times E$ gives the conjectural BKM.

- **AP-CY127 -- $K3 \times E$ signature $(4, 21)$ vs $(4, 20)$
  (Medium).** $K3$ has Mukai-lattice signature $(4, 20)$
  (rank 24). $K3 \times E$ has total Betti rank 96 but numerical
  K-theory rank 48 (see AP-CY36/cache Entry 57). The orthogonal
  lattice signature governing the BKM is $(2, 3)$ on
  $\overline{\mathcal{A}_2}$ (Siegel threefold); mixing these three
  signatures (24, 48, 5) produces type errors.
  **Counter**: always name the signature and the ambient: K3 Mukai
  $(4, 20)$; $K3 \times E$ numerical K-theory $48$; Siegel threefold
  orthogonal $(2, 3)$.

## Waves 14-19 VERIFIED-item anti-patterns (AP-CY128 through AP-CY140)

These entries turn the 32 VERIFIED items of the Wave-19 adjudication
ledger (`notes/ADJUDICATION_LEDGER_WAVES_14_TO_19.md §I`) into
AP-templates against mis-statement. Each VERIFIED value is stable but
each is also the subject of at least one first-principles
mis-statement that the AP-template guards against.

- **AP-CY128 -- Bi-canonical $K^{\mathrm{super}}$ identification
  conflated with $K^{\mathrm{bos}}$ (High).**
  The bi-canonical identification is $K^{\mathrm{super}} = 2c_+ = 8$
  in the super-lattice (non-trivial $\mathbb{Z}/2$-graded) sector.
  The bosonic analogue $K^{\mathrm{bos}} = c_+$ applies on reduced
  even lattices only. Universal three-faces identity
  $\hbar^2 \cdot K^{\kappa_{\mathrm{ch}}} = -1$ uses super $K$.
  **Counter**: state $K^{\mathrm{super}}$ or $K^{\mathrm{bos}}$
  explicitly; super for BKM, bosonic for affine KM class.

- **AP-CY129 -- $\hbar^2 = -1/8$ as rational $-0.125$ (Medium).**
  The three-faces identity fixes $\hbar^2 = \mathrm{Fraction}(-1, 8)$
  exactly; decimal $-0.125$ loses the exact-fraction discipline
  required by the whole-object verifier (WOV).
  **Counter**: always store $\hbar^2$ as $\mathrm{Fraction}(-1, 8)$
  in compute modules; never float.

- **AP-CY130 -- $c_{4d}(A_1, \Sigma_{0, 24}) = 107/6$ reduced to
  $17.833\ldots$ or approximated (Medium).**
  The 4d central charge is $107/6$, with 107 prime. Decimal
  $17.8333$ breaks primality tracking; Vol-III WOV-2 locks the
  exact rational.
  **Counter**: always $107/6$, never $17.833$. 107 prime carries
  the information that class-$\mathcal{S}$ $(A_1, n = 24)$ is the
  only place $c_{4d}$ hits this prime.

- **AP-CY131 -- $\Delta_5 = \mathrm{Grit}(\eta^9 \vartheta_1)$
  citation (Medium).**
  $\Delta_5$ is the Gritsenko additive lift of $\eta^9 \vartheta_1$
  (Gritsenko 1999 *Math Nachr* 199 Thm 6.1; Gritsenko-Nikulin 1998
  *Invent Math* 130 Thm 2.1), not the Borcherds multiplicative lift
  (which gives $\Phi_{10} = \Delta_5^2$). Citing $\Delta_5$ through
  Borcherds products produces a squaring error.
  **Counter**: always cite Gritsenko 1999 for the additive
  construction of $\Delta_5$; Borcherds for $\Phi_{10}$.

- **AP-CY132 -- Four Fricke rows advertised uniformly (Medium).**
  The four $\Psi$-image rows are Monster / Fake-Monster / K3 /
  Enriques with $(c_+, \ell) = (1, 2), (25, 50), (4, 8), (2, 4)$.
  The Leech-Conway row is the fifth and breaks universality because
  Leech is positive-definite with no Fricke involution
  (AP-CY95/AP-CY111).
  **Counter**: never state "four Fricke rows" as universal. Always
  qualify: "four GN-reflective rows (with Leech-Conway breaking
  universality)".

- **AP-CY133 -- Arthur parameter $\psi_{\Delta_{10}}$ as
  irreducible (High).** The Arthur parameter
  $\psi_{\Delta_{10}} = \phi_{\Delta_{E_6}} \boxtimes \mathrm{Sym}^1$
  is reducible (Saito-Kurokawa CAP); this is the content of
  AP-CY35/AP-CY41. Irreducibility breaks the CAP structure and
  removes the Chenevier-determinant correction.
  **Counter**: always name "Saito-Kurokawa CAP" and use Chenevier
  2014 determinant $D_{\Delta_{10}}$, not pseudo-character.

- **AP-CY134 -- Hecke Euler factor convolution without primes
  (High).** The Hecke dictionary
  $\lambda_p(\Delta_{10}) = a_p(\Delta_{E_6}) + p^8 + p^9$ holds at
  the primes $p \leq 79$ (WOV-6); extrapolation to large primes
  requires $E_4 \cdot \Delta$ convolution and the Deligne-Petersson
  bound $|a_p| \leq 2 p^{15/2}$.
  **Counter**: never extrapolate the Hecke dictionary beyond 79
  without $E_4 \cdot \Delta$ convolution; large-prime values require
  continuation via Wave 20 $p = 109$.

- **AP-CY135 -- $p = 2$ ramified local Langlands conductor
  ambiguity (Medium).** At $p = 2$,
  $\psi_{\Delta_5, 2} = \phi_{\Delta_{E_6}, 2} \boxtimes \mathrm{Sym}^1
  \otimes \varepsilon_2$ with conductor $2^{17}$. The sign character
  $\varepsilon_2 \leftrightarrow \sqrt 2 \in \mathbb{Q}_2^\times / (\mathbb{Q}_2^\times)^2$
  is load-bearing; dropping it changes conductor calculation.
  **Counter**: always include $\varepsilon_2$ and cite $2^{17}$
  conductor.

- **AP-CY136 -- MTC at $q = \zeta_8$ presented as semisimple
  (Critical).** At $q = \zeta_8$, the small quantum group
  $\mathfrak{u}_{\zeta_8}$-mod is non-semisimple Kerler-Lyubashenko
  (Kerler-Lyubashenko 2001 *LNM* 1765); semisimplification is
  Turaev. PBW upper bound $|\Lambda| \leq 8^{129}$. Treating the
  MTC as semisimple erases the projective-cover structure that
  carries the Plancherel integration to $1/\Phi_{10}(Z)$.
  **Counter**: always state "non-semisimple KL" at $q = \zeta_8$;
  semisimplification via Turaev.

- **AP-CY137 -- Modular $S$-matrix eigenvalues as $\{1, -1\}$
  (Medium).** The modular $S$-matrix at the Fricke $w_8$ level
  satisfies $S^4 = \mathrm{id}$ with eigenvalues $\{1, i, -1, -i\}$.
  Treating eigenvalues as $\{1, -1\}$ forces $S^2 = \mathrm{id}$
  and loses the complex-conjugation structure.
  **Counter**: always state $\{1, i, -1, -i\}$; generic $\mathrm{tr}(S) = 0$;
  $M_{24}$-invariant Humbert-block trace $= 4 = |\Psi_{\Delta_{10}}|$.

- **AP-CY138 -- Padovan dimensions confused with Fibonacci (Medium).**
  The pentagon MZV basis dimensions through $n = 12$ satisfy
  $d_n = d_{n-2} + d_{n-3}$ (Padovan), not $d_n = d_{n-1} + d_{n-2}$
  (Fibonacci). Seeds $(d_1, d_2, d_3) = (1, 0, 1)$. At $n = 12$,
  $d_{12} = 9$; at $n = 24$, $p_{24}(12) = 10{,}914{,}317{,}934$
  coincides with $\chi(\mathrm{Hilb}^{12}(K3))$.
  **Counter**: never cite Fibonacci; always Padovan with explicit
  recurrence.

- **AP-CY139 -- $A_\infty$-quasi-Hopf as closed structure (Medium).**
  $\mathbf H_{\Delta_5}$ is $A_\infty$-quasi-Hopf *non-closed*:
  the imaginary cone is infinite-dimensional
  ($\dim \mathrm{Imag}_N \sim N^{-27/4} \exp(4\pi\sqrt N)$,
  Hardy-Ramanujan); $\phi^{(n)} \ne 0$ for all admissible $n$.
  Closed quasi-Hopf would terminate the obstruction tower.
  **Counter**: always name "non-closed" $A_\infty$-quasi-Hopf;
  obstruction tower open in every degree.

- **AP-CY140 -- Heegner admissibility as $n \not\equiv 0, 3 \pmod 4$
  (High).** Admissibility congruence is on
  $D_n = (n - 3)/2 \pmod 4 \in \{0, 1\}$, equivalently
  $n \equiv 3, 5 \pmod 8$, not on $n$ directly (AP-CY42/FM25).
  The $n$-form is a translation of the $D_n$-form and is fragile
  under base shifts.
  **Counter**: always write the congruence on $D_n$; derive the
  $n$-form as a translation, never as primary.
  **See AP-CY142 for the full Humbert--Heegner admissibility filter
  entry** (ghost / precise error / correct / Padovan reference table /
  three verification paths / primary citations).

- **AP-CY141 -- Single-valued MZV scope of chiral-Hochschild
  periods (Critical).**
  (a) **Ghost.** The Deligne-Goncharov 2005 *Ann Sci ENS* 38
  mixed-Tate motivic framework gives the full motivic Galois
  $\mathrm{grt}_1^{\mathrm{mot}}$ acting on the motivic MZV ring
  $\mathrm{MZV}^{\mathrm{mot}}$; the chiral-Hochschild period
  $\chi_3 = 2\mathrm{Vol}(E)(2\pi i)^3$ is a genuine weight-3
  period. The Vol III CoHA Casimir (Path A,
  Schiffmann-Vasserot 2017 *IHES* 118) and Kuznetsov relative HPD
  (Path D, Kuznetsov-Markushevich 2009 + Addington-Thomas 2014
  *Duke Math J* 163) readings of $\chi_3$ $a\text{-}priori$
  expand in $\mathrm{MZV}^{\mathrm{mot}}$.
  (b) **Precise error.** Asserting that the chiral-Hochschild
  period identity $\chi_3 = 2\mathrm{Vol}(E)(2\pi i)^3$ lies in
  the full motivic ring $\mathrm{MZV}^{\mathrm{mot}}$ is a scope
  inflation. The Arnold forms $\eta_{ij} = d\log|z_{ij}|^2$ that
  witness the chain-level $\chi_3$ cocycle on $\mathrm{Conf}_n(E)$
  are **single-valued real**; the period pairing factors through
  Brown 2013 *Ann Math* 175 projection
  $\mathrm{proj}: \mathrm{MZV}^{\mathrm{mot}} \to
  \mathrm{MZV}^{\mathrm{sv}}$. At weight 2, $\zeta^{\mathrm{sv}}(2)
  = 0$; conflating the two rings overcounts admissible periods and
  would predict spurious $\zeta(2)$-weighted contributions in the
  Schiffmann-Vasserot Casimir pairing on
  $K^T(\mathrm{Hilb}^n\mathrm{K3})$ that do not survive
  single-valued projection.
  (c) **Correct.** Chiral-Hochschild periods live in
  $\zeta^{\mathrm{sv}}$ (Brown 2013 single-valued MZVs), **not**
  in $\mathrm{grt}_1^{\mathrm{mot}}$-stable full motivic MZVs.
  Three sites must be distinguished: **chain-level** (explicit
  $\eta_{ij}$-integrals on $\mathrm{Conf}_n(E)$,
  rational-coefficient), **motivic** ($\mathrm{MZV}^{\mathrm{mot}}$
  target of the period map), **single-valued**
  ($\zeta^{\mathrm{sv}}$ image under Brown's projection). Canonical
  identifications: $\zeta^{\mathrm{sv}}(2) = 0$,
  $\zeta^{\mathrm{sv}}(3) = 2\zeta(3)$,
  $\zeta^{\mathrm{sv}}(2k+1) = 2\zeta(2k+1)$ at odd weight, and
  $\zeta^{\mathrm{sv}}$ is a **proper** subring at depth $\ge 2$
  (Schnetz 2014 *Commun Num Theor Phys* 8; Panzer 2015
  *Commun Num Theor Phys* 9).
  **Vol III reading.** Single-valued scope constrains Vol III's
  CoHA Casimir (Path A) and Kuznetsov relative HPD (Path D)
  readings of $\chi_3$. The CoHA $\to Y^+(\widehat{\mathfrak{gl}}_1)
  \to \mathrm{VOA} \to$ chiral arrow composes with the Brown 2013
  $\mathrm{proj}: \mathrm{MZV}^{\mathrm{mot}} \to
  \mathrm{MZV}^{\mathrm{sv}}$ — the Schiffmann-Vasserot Casimir
  pairing lands in $\zeta^{\mathrm{sv}}$, not full motivic. The
  Kuznetsov relative HPD pairing on $D^b\mathrm{Coh}(\mathrm{K3}
  \times E)$-Kuznetsov components factors through the
  Addington-Thomas cubic-fourfold intermediate Jacobian (Hodge
  real structure), itself a single-valued weight-3 period. Theorem
  H amplitude bound $\mathrm{ChirHoch}^\bullet \in \{0, 1, 2\}$ is
  recovered as a **single-valued consequence** of
  $\zeta^{\mathrm{sv}}(2) = 0$, not imposed.
  **Counter**: never equate chiral-Hochschild periods with
  $\mathrm{MZV}^{\mathrm{mot}}$; always name the Brown 2013
  projection and land in $\zeta^{\mathrm{sv}}$.
  Cross-reference Vol I AP901 and Theorem
  `thm:sv-scope-restriction-chiralhoch` in
  `/Users/raeez/chiral-bar-cobar/chapters/theory/motivic_shadow_tower.tex`.
  Related: AP888 (shadow-ChirHoch bridge); seven-path $\chi_3$
  comparison theorem; Vol II V2-AP126 (one-loop Quillen / cyclic
  chiral homology single-valued landing).
  **Primary citations**: Brown 2013 *Ann Math* 175 "Mixed Tate
  motives over $\mathbb Z$"; Brown 2013 *Ann Sci ENS* 46
  single-valued multiple polylogarithms; Schnetz 2014 single-valued
  zeta; Deligne-Goncharov 2005 *Ann Sci ENS* 38; Panzer 2015
  single-valued algorithms.

- **AP-CY142 -- Humbert--Heegner admissibility filter
  $n \equiv 3, 5 \pmod 8$ on the pentagon coboundary tower
  $\phi^{(n)}$ (Critical).**
  (a) **Ghost.** The pentagon coboundary tower
  $\{\phi^{(n)}\}_{n \ge 3}$ of Definition
  \texttt{def:phi-n-pent-EK} (Vol I
  \texttt{chapters/theory/shadow\_tower\_higher\_coefficients.tex})
  has a well-defined three-filter admissibility structure on the K3
  $A_\infty$-Humbert regime of the BKM crown algebra
  $\mathbf H_{\Delta_5}$. Eichler--Zagier 1985 polar-support cutoff
  $\Delta \ge -1$ on the paramodular index-1 K3 elliptic genus is a
  real theorem (Eichler--Zagier *Prog Math* 55 Thm 9.3 with
  $C(-1) = 2$, $C(0) = 20$). Gritsenko--Nikulin 1998 *J Reine Angew
  Math* 507 paramodular lift of the K3 elliptic genus gives explicit
  $c_{\Phi_{10}/\eta^{24}}$ Fourier data. Brown 2012 *Ann Math* 175
  Thm 1 Padovan recurrence $d_n = d_{n-2} + d_{n-3}$ counts the
  motivic-MZV transcendence basis at weight $n$ (real theorem).
  (b) **Precise error.** Bare Padovan-dimension $d_n$ count WITHOUT
  the Humbert--Heegner admissibility filter overcounts. Most
  Padovan-admissible $n \ge 3$ (all $n \ge 3$ except $n = 4$) are
  Humbert--Heegner-FORBIDDEN: the paramodular lattice sum
  $\sum_{4NM - \ell^2 = -D_n} c_{\Phi_{10}/\eta^{24}}(N, \ell, M)$
  with $D_n = (n - 3)/2$ is non-empty iff
  $D_n \bmod 4 \in \{0, 1\}$, forcing $n \equiv 3, 5 \pmod 8$.
  Asserting a non-zero $\phi^{(n)}$ on the K3--Humbert regime on the
  sole basis of $d_n > 0$ (e.g., at $n = 7, 9, 12, 24, 26, \dots$)
  silently conflates the MZV-transcendence count with the paramodular
  Humbert--Heegner signature and misses the Heegner--Bruinier
  obstruction class
  $\mathrm{ob}^{\mathrm{HB}}_n \in H^2(H_n, \mathrm{Sym}^2
  T^{\mathrm{poly}}_{\mathrm{ch}} |_{H_n})$ of Bruinier-torsion order
  $c_n$ (Bruinier 2002 LNM 1780 §5 Chern class on Heegner divisors).
  (c) **Correct.**
  $\phi^{(n)} \big|_{\mathrm{K3\text{-}Humbert}} \ne 0$ iff (i)
  $n \equiv 3, 5 \pmod 8$ AND (ii) the $d_n$-dimensional Brown
  canonical basis is non-empty AND (iii) $D_n \le 1$ (Eichler--Zagier
  polar cutoff). First non-vanishing: $\phi^{(3)}$ = Drinfeld pentagon
  cocycle ($D_3 = 0$, $C(0) = 20 \ne 0$);
  $\phi^{(5)} = -2 \cdot [\mathrm{gen}]^{\otimes 5}$ with
  Gritsenko--Nikulin 1998 Table 2 sign on $\Phi_{10}/\eta^{24}$
  ($D_5 = 1$, $C(-1) = 2 \ne 0$). Humbert--Heegner admissible
  $n \in [3, 36]$: $\{3, 5, 11, 13, 19, 21, 27, 29, 35\}$.
  Padovan-positive HH-forbidden $n$ (e.g.,
  $4, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26,
  28, 30, 31, 32, 33, 34, 36$) all give $\phi^{(n)} = 0$ on
  K3--Humbert. HH-admissible $n \ge 11$ give $\phi^{(n)} = 0$ by
  Eichler--Zagier polar support ($D_n \ge 4 > 1$).

  **Condensed reference table** $(n, d_n, D_n, \mathrm{HH},
  \phi^{(n)}\text{-K3})$:
  $(3, 1, 0, Y, \text{non-zero})$; $(4, 0, 1/2, -, 0)$;
  $(5, 1, 1, Y, -2[\mathrm{gen}]^{\otimes 5})$;
  $(6, 1, 3/2, -, 0)$; $(7, 1, 2, N, 0)$; $(8, 2, 5/2, -, 0)$;
  $(9, 2, 3, N, 0)$; $(10, 2, 7/2, -, 0)$;
  $(11, 3, 4, Y, 0\,\text{polar})$; $(12, 4, 9/2, -, 0)$;
  $(13, 5, 5, Y, 0\,\text{polar})$;
  $(19, 17, 8, Y, 0\,\text{polar})$;
  $(21, 28, 9, Y, 0\,\text{polar})$;
  $(27, 90, 12, Y, 0\,\text{polar})$;
  $(29, 149, 13, Y, 0\,\text{polar})$;
  $(35, 504, 16, Y, 0\,\text{polar})$.

  **Vol III framing (admissible discriminant set in $c_{K3}$ Fourier
  expansion).** The filter is tied to the admissible discriminant set
  in the $c_{K3}$ Fourier expansion of the K3 elliptic genus: only
  $D_n \in \{0, 1\} \pmod 4$ discriminants contribute to the
  paramodular lattice sum over
  $\sum_{4NM - \ell^2 = -D_n} c_{\Phi_{10}/\eta^{24}}(N, \ell, M)$;
  Fourier coefficients $c_{K3}(-D_n)$ at non-admissible $D_n$ either
  vanish by the polar-support cutoff (when $D_n > 1$) or correspond to
  HH-forbidden non-paramodular signatures. The CY-3 anchor
  $K3 \times E$ sits at the Humbert divisor $H_1 = \{\tau_{12} = 0\}$
  of $\overline{\mathcal A_2}$; under the CY-3-to-chiral functor
  $\Phi_3$, the Humbert--Heegner filter on $\phi^{(n)}$ translates
  into an admissibility condition on the discriminants seen by
  $\mathbf H_{\Delta_5}$'s YD-tower weights $\delta^{(n)}$ (cross-ref
  AP-CY78). The filter locks which CoHA Casimir (Path A) readings of
  $\chi_n$ have non-trivial Schiffmann--Vasserot contributions and
  which Kuznetsov relative HPD (Path D) readings have non-trivial
  Addington--Thomas cubic-fourfold intermediate-Jacobian residues;
  readings at non-admissible $n$ vanish.

  **Three verification paths for the filter.** (i) Discriminant-form
  signature — the index-1 paramodular form
  $4NM - \ell^2 \equiv -\ell^2 \pmod 4$ takes values in
  $\{0, -1\} \pmod 4$, so $-D_n$ is representable iff
  $D_n \in \{0, 1\} \pmod 4$, forcing $n \equiv 3, 5 \pmod 8$ by
  odd-$n$ integrality.
  (ii) Eichler--Zagier 1985 weak-Jacobi-form polar-support cutoff
  ($C(\Delta) = 0$ for $\Delta < -m^2 = -1$, real theorem).
  (iii) Gritsenko--Nikulin 1998 paramodular lift of the K3 elliptic
  genus with explicit $c_{\Phi_{10}/\eta^{24}}$ Fourier table (real
  object) — verify at low $n$: $c(-1) = 2$ at $n = 5$ matches the
  $\phi^{(5)} = -2 \cdot [\mathrm{gen}]^{\otimes 5}$ coefficient
  directly.

  **Counter**: never assert non-zero $\phi^{(n)}$ on K3--Humbert on
  Padovan-only grounds; always install the HH filter
  $n \equiv 3, 5 \pmod 8$ and check the Eichler--Zagier polar
  $D_n \le 1$ cutoff.
  Cross-reference Vol I Theorem
  \texttt{thm:phi-n-humbert-heegner-admissibility} in
  \texttt{/Users/raeez/chiral-bar-cobar/chapters/theory/shadow\_tower\_higher\_coefficients.tex}
  (lines 4364-4433).
  Related: AP-CY78 (YD-tower weight parity);
  AP-CY80 (Coxeter-void at $N = 11$ — Padovan $d_{11} = 3$ but
  $n = 11$ HH-admissible only, with $\phi^{(11)}$ polar-zero);
  AP-CY140 (congruence-variable discipline); AP-CY141
  (single-valued MZV scope); Vol II AP-V2-24 / V2-AP127 (partner
  entry on Swiss-cheese coloured-bar reading).
  **Primary citations**: Eichler--Zagier 1985 *Prog Math* 55 Thm 9.3
  (polar-support cutoff); Gritsenko--Nikulin 1998 *J Reine Angew
  Math* 507 (Humbert--Heegner structure, paramodular
  $\Phi_{10}/\eta^{24}$ sign convention Table 2); Bruinier 2002 LNM
  1780 §5 (Chern class on Heegner divisors, torsion orders $c_n$);
  Brown 2012 *Ann Math* 175 Thm 1 (Padovan motivic-MZV dimension).

