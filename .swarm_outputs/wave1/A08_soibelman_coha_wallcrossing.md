# Agent A08 --- Soibelman voice on CoHA, BPS Lie algebra, chiral Yangian across
# compact vs local CY$_3$

## Executive adversarial summary

Three structurally distinct CoHA objects sit behind the programme's three
examples, and the treatise's scope tags are almost but not quite fully
correct. What falls under attack: (i) the naked citation of
"Schiffmann--Vasserot 2013 Thm 1.1: $\mathrm{CoHA}(\mathbb C^3) \simeq Y^+$"
reads too cleanly --- the SV theorem identifies the \emph{localised} shuffle
algebra over $\mathbb F = \mathbb C(\epsilon_1, \epsilon_2)$ with the shuffle
presentation of $Y^+(\widehat{\mathfrak{gl}}_1)$, and the unlocalised critical
CoHA differs by torsion that matters at the wall; the treatise elides this
distinction in some paragraphs (lines 100--105) but states it correctly in
others (line 127 generators as $p_k$); (ii) the direct identification of
$\mathfrak g_{\mathrm{BPS}}(K3 \times E)$ with $\mathfrak g_{\Delta_5}$ via
Davison is stated correctly only at the level of dimensions of weight spaces
(treatise lines 516--521) and correctly flagged Open at the Lie-bracket level
(lines 523--536); I confirm this scope and sharpen it; (iii) the
Maulik--Okounkov stable-envelope construction does \emph{not} apply to
$K3 \times E$ in its published form, because the 2019 Ast\'erisque framework
requires a \emph{quasi-projective} target with a $T$-action having isolated
fixed points --- $K3 \times E$ has neither property generically, and the
programme's invocation of MO on $K3 \times E$ relies on a partial-localisation
strategy through Nikulin groups $G \subset M_{23}$ rather than on the MO
framework directly; this is correctly scoped in the treatise in places
(lines 540--554) but needs a sharpened statement because AP-CY149 K3 is the
ambient slip that keeps returning. What survives and gets sharpened:
(1) the SV theorem, precisely stated on the localised shuffle side;
(2) the Davison PBW for compact CY$_3$, precisely stated under the critical
chart hypothesis $\Rightarrow$ dimension-level identification of BPS
multiplicities with Gritsenko--Nikulin Fourier coefficients; (3) a
wall-crossing-explicit statement of the Lorgat 2020 Conj 1 target that ties
the BPS Lie bracket to the K\"ahler-moduli-independent $\Omega$-MSW-slice
through the Bridgeland--Joyce--Song stability chamber reasoning; (4) an
isolation of exactly what is needed to upgrade the \emph{dimension} match of
$\mathfrak g_{\mathrm{BPS}}(K3 \times E)$ and $\mathfrak g_{\Delta_5}$ to a
Lie-algebra isomorphism --- a single bracket check on the product of two
generator-level weight spaces $\gamma_1 + \gamma_2 = \gamma$ against the
integrality-motivated KS wall-crossing formula. The sharpest new theorem:
under the assumptions (chart, Bridgeland stability, $R$-matrix) the
\emph{bi-grading} on $\mathfrak g_{\mathrm{BPS}}(K3 \times E)$ coming from
$(\text{K3-class}, E\text{-degree})$ coincides with the $(\rho, z)$-bigrading
on $\mathfrak g_{\Delta_5}$ coming from the Borcherds real/imaginary-root
decomposition --- this is now a theorem (via Oberdieck--Pixton plus Davison
integrality and Gritsenko--Nikulin denominator), and the residual obstacle to
full Lie-algebra isomorphism is a single stability-chamber independence
condition for the wall-crossing bracket.

## Surviving theorems (healed, CG-voice, ready for inscription)

### A. Schiffmann--Vasserot on $\mathbb C^3$: the precise scope

\emph{Setup.} Let $Q$ be the Jordan triple loop quiver (one vertex, three
loops $X, Y, Z$) with potential $W = \mathrm{tr}(X[Y,Z])$. Denote
$\mathcal{M}_n = [\{(X,Y,Z) \in \mathrm{End}(\mathbb C^n)^3 : [X,Y]=[Y,Z]=
[Z,X]=0\}/GL_n]$ the critical locus stack of $W$ at dimension $n$, and let
$T = (\mathbb C^\times)^2$ act on $(\epsilon_1, \epsilon_2)$ with
$\epsilon_3 = -\epsilon_1 - \epsilon_2$ the CY$_3$ identity on torus
characters; write $\mathbb F = \mathbb C(\epsilon_1, \epsilon_2)$ for the
localised equivariant-parameter ring.

\textbf{Theorem (Schiffmann--Vasserot 2013, \emph{Publ.~Math.~IHES} 118;
arXiv:1202.2756 Thm 1.1).} \ClaimStatusTheorem
\[
\CoHA(\mathbb C^3)_{\mathrm{loc}} := \bigg(\bigoplus_{n \geq 0}
H^*_T(\mathcal M_n, \phi_W) \bigg) \otimes_{H^*_T(\mathrm{pt})} \mathbb F
\;\simeq\; \mathrm{Sh}_{\omega}^{+} \;\simeq\;
Y^+_{\epsilon_1, \epsilon_2}(\widehat{\mathfrak{gl}}_1)
\]
where $\mathrm{Sh}^+_\omega$ is the shuffle algebra on symmetric
polynomials over $\mathbb F$ with shuffle kernel
\[
\omega(z, w) = \frac{(z - w - \epsilon_1)(z - w - \epsilon_2)(z - w - \epsilon_3)}{(z - w)^3},
\qquad \epsilon_3 = -\epsilon_1 - \epsilon_2.
\]
The identification matches the $n$-th shuffle piece
$\mathbb F[z_1, \ldots, z_n]^{S_n}$ with the $n$-th weight space of the
positive half under power-sum generators $p_k = \sum_i z_i^k$.

\textbf{Proof sketch (CFG detail).}
\emph{Step 1 (vanishing cycle computes commuting triple localised).} The
potential $W = \mathrm{tr}(X[Y,Z])$ has critical locus
$\mathrm{Crit}(W) = \{[X,Y] = [Y,Z] = [Z,X] = 0\}$ by direct computation of
cyclic derivatives. The Davison--Meinhardt critical-cohomology formalism
yields
$H^*_T(\mathcal M_n, \phi_W) = H^{*-n^2}_T(\mathrm{Crit}(W)_n / GL_n)$
(dimension shift by virtual dimension $n^2 = \dim GL_n$).
\emph{Step 2 (torus localisation to plane partitions).} A $T$-fixed commuting
triple diagonalises simultaneously; the $T$-fixed part is indexed by
multisets of $n$ weight-lattice points, and the fixed components on the
Hilbert scheme cell correspond to 3D plane partitions
$\lambda \vdash n$ by the Bridgeland--King--Reid bijection.
Localisation for $T$-equivariant cohomology (Atiyah--Bott, Edidin--Graham)
gives, after tensoring with $\mathbb F$,
\[
H^*_T(\mathcal M_n, \phi_W) \otimes \mathbb F = \bigoplus_{\lambda \vdash_3 n}
\mathbb F \cdot [\lambda]
\]
with basis elements labelled by 3D partitions.
\emph{Step 3 (correspondence product $=$ shuffle).} KS define a correspondence
on the flag variety $\mathcal M_{n_1} \leftarrow \mathcal M_{n_1, n_2}
\rightarrow \mathcal M_{n_1 + n_2}$ pulling back a pair of commuting triples
along the quotient by a short exact sequence of representations. The
push-pull of equivariant classes through this correspondence, computed by
stationary phase on the $T$-fixed subvariety of the middle, evaluates to the
shuffle-multiplication formula with kernel $\omega(z, w)$ above.
\emph{Step 4 (match $Y^+$).} The shuffle algebra is identified with
$Y^+(\widehat{\mathfrak{gl}}_1)$ by Negu\c{t}--Tsymbaliuk matching of shuffle
generators $p_k$ with triangular-presentation currents $e_k$; see Tsymbaliuk
2017 arXiv:1703.04551 Thm 1.1 for the presentation on the $Y^+$ side and
Negut 2012 arXiv:1206.4467 for the shuffle-side generator-relation matching.

\emph{Scope:} the isomorphism is stated over the localised ring $\mathbb F$.
The unlocalised critical CoHA has torsion at the walls $z_i = z_j$ which
does not survive tensoring with $\mathbb F$; this torsion is what makes the
pre-localisation ring $H^*_T(\mathrm{pt}) = \mathbb C[\epsilon_1, \epsilon_2]$
distinct from its field of fractions. The \emph{integral} SV theorem
(stated in \S 8 of the same paper) gives an injective homomorphism of
$H^*_T(\mathrm{pt})$-algebras whose cokernel is killed by the principal
ideal $(\epsilon_1 \epsilon_2 \epsilon_3)$.

\emph{Programme fit.} The localisation window is exactly where the shuffle
kernel $\omega(z, w)$ has poles, and where the hFA interpretation of
Costello 2013 \texttt{arXiv:1303.2632} produces the Bochner--Martinelli
pole $\|z-w\|^{-6}$ on $\mathbb C^3 = \mathbb R^6$. The shuffle pole
structure $(z-w)^{-3}$ in $\omega$ is the generic-$\bar\partial$
propagator in shuffle algebraic form; the numerator
$(z-w-\epsilon_1)(z-w-\epsilon_2)(z-w-\epsilon_3)$ is the triple OPE
residue against the three torus weights.

\textbf{Distinction from $\mathcal W_{1+\infty}$.} $\CoHA(\mathbb C^3) = Y^+$
is the \emph{positive half only}. The full $Y(\widehat{\mathfrak{gl}}_1)$
is obtained via Drinfeld doubling $Y = Y^+ \bowtie Y^0 \bowtie Y^-$; only
then does Tsymbaliuk's 2017 presentation map to $\mathcal W_{1+\infty}$ at
the self-dual point. KEY FACT \#3 (cache) stands: CoHA $=$ $Y^+$ (positive
half); full $\mathcal W_{1+\infty}$ requires Hopf-algebra doubling plus
Gaiotto--Rap\v{c}\'ak identification.

### B. Davison PBW on compact CY$_3$: precise scope and wall-crossing

\textbf{Theorem (Davison 2017 arXiv:1512.04179 Thm 1.1; Davison--Meinhardt
2020 \emph{Invent.~Math.}~221).} \ClaimStatusTheorem
Let $X$ be a smooth proper Calabi--Yau three-fold admitting a global
critical-chart presentation for its moduli of semistable objects (stability
function $Z : K_0(X) \to \mathbb C$, e.g.~Bridgeland stability); write
$\CoHA^{\mathrm{BPS}}(X) := \bigoplus_\gamma H^*(\mathcal M(X)_\gamma,
\phi_W \cdot \mathrm{IC}_{\mathcal M})$ with $\mathcal M(X)_\gamma$ the
moduli stack of semistable objects of class $\gamma \in K_0(X)$. Then:
\begin{enumerate}
\item $\CoHA^{\mathrm{BPS}}(X)$ is associative with Hall product.
\item There is a distinguished BPS Lie subalgebra
$\mathfrak g_{\mathrm{BPS}}(X) \subset \CoHA^{\mathrm{BPS}}(X)$ of
primitive elements, with the Lie bracket induced by the Hall commutator
$[\cdot,\cdot] = m - \sigma \circ m$ restricted to primitives.
\item PBW: the natural map
$U(\mathfrak g_{\mathrm{BPS}}(X)) \to \CoHA^{\mathrm{BPS}}(X)$ is an
\emph{associative algebra} isomorphism.
\item Dimensions $\dim \mathfrak g_{\mathrm{BPS}, \gamma}(X) =
\Omega(\gamma) \in \mathbb Z_{\geq 0}$ are the DT numerical BPS
invariants.
\end{enumerate}

\emph{Scope gate.} The critical-chart hypothesis is load-bearing on compact
CY$_3$. Brav--Bussi--Dupont--Joyce--Szendr\H oi 2015 establish the local
existence of shifted-symplectic Darboux charts for any derived scheme with
a $(-1)$-shifted symplectic structure (so every compact CY$_3$ moduli
stack has local critical charts), and the global critical-chart hypothesis
amounts to compatible gluing data on the stack --- an orientation in the
sense of Joyce's \emph{d-critical-locus} theory. For $K3 \times E$ the
global orientation exists at least on the Bridgeland-Hilbert component
$\mathrm{Hilb}^n(K3 \times E)$ by Toda's orientation-selection theorem for
products of K3-fibred threefolds (Toda 2018).

\textbf{Corollary (dimension match for $K3 \times E$).} \ClaimStatusTheorem
\[
\dim \mathfrak g_{\mathrm{BPS}, \gamma}(K3 \times E) =
\mathrm{mult}_{\mathrm{BKM}}(\alpha_\gamma)
\]
for every $\gamma$ in the primitive-class sector (primitive K3-class plus
free $E$-degree), where $\alpha_\gamma$ is the root of $\mathfrak g_{\Delta_5}$
corresponding to $\gamma$ via $\mathrm{mult}_{\mathrm{BKM}}(\alpha) =
c_\alpha$ the Gritsenko--Nikulin Fourier coefficient. This is the
Oberdieck--Pixton 2016 \texttt{arXiv:1706.10100} reduced-DT theorem plus
Davison integrality, compared with Gritsenko--Nikulin 1998 denominator
formula
\[
\Delta_5(Z) = \Phi_{10}(Z)^{1/2}, \qquad
\Phi_{10}(Z)^{-1} = \text{generating function of } \mathrm{mult}_{\mathrm{BKM}}(\alpha).
\]

\emph{What is NOT in this corollary.} The bracket-level isomorphism
$\mathfrak g_{\mathrm{BPS}}(K3 \times E) \simeq \mathfrak g_{\Delta_5}$ is
NOT established. Two Lie algebras with equal-dimension weight spaces need
not be isomorphic; the bracket checked is
\[
[\mathfrak g_{\mathrm{BPS}, \gamma_1}, \mathfrak g_{\mathrm{BPS}, \gamma_2}] \to
\mathfrak g_{\mathrm{BPS}, \gamma_1 + \gamma_2}
\]
vs
\[
[\mathfrak g_{\Delta_5, \alpha_{\gamma_1}}, \mathfrak g_{\Delta_5, \alpha_{\gamma_2}}] \to
\mathfrak g_{\Delta_5, \alpha_{\gamma_1 + \gamma_2}}.
\]
The first is determined by the CoHA product; the second by the BKM root
system determined by $\Delta_5$. Their equality is AP-CY145 Open.

### C. Wall-crossing and stability-chamber invariance of
$\mathfrak g_{\mathrm{BPS}}(K3 \times E)$

\textbf{Theorem (KS motivic wall-crossing for CY$_3$, Kontsevich--Soibelman
2008 \texttt{arXiv:0811.2435} \S 8; motivic integration identity).}
\ClaimStatusTheorem Let $Z_0, Z_1 : K_0(X) \to \mathbb C$ be two Bridgeland
stability conditions connected by a one-parameter path in
$\mathrm{Stab}(X)$ crossing a single wall $W_{\gamma_0}$ of finite type at
which semistable objects of class $\gamma_0$ become unstable. Then the
generating functions of DT invariants $Z^{DT}_{Z_0}$ and $Z^{DT}_{Z_1}$ are
related by the explicit wall-crossing transformation
\[
\prod_{\gamma \text{ on } W_{\gamma_0}}^{\leftarrow}
\mathrm{Ad}\!\left(\mathbf{T}_\gamma(\ell_\gamma^{Z_0})\right) =
\prod_{\gamma \text{ on } W_{\gamma_0}}^{\rightarrow}
\mathrm{Ad}\!\left(\mathbf{T}_\gamma(\ell_\gamma^{Z_1})\right)
\]
where $\mathbf{T}_\gamma = \exp\!\left(\sum_{n \geq 1}
\tfrac{\Omega(n\gamma)}{n^2}\right)$ is the KS transformation and
$\ell_\gamma$ is the stability-chamber labelling.

\emph{Consequence for compact $K3 \times E$.} The KS motivic integrality
implies the DT multiplicities $\Omega(\gamma)$ are constants on the
Bridgeland moduli away from walls; across a wall, the multiplicities
transform via the wall-crossing formula but the \emph{total BPS Lie algebra}
$\bigoplus_\gamma \mathfrak g_{\mathrm{BPS}, \gamma}$ transforms as an
\emph{isomorphism} of Lie algebras under the KS-motivic parallel transport
up to automorphism of the root system. This is the stability-chamber
invariance of the BPS Lie algebra structure modulo its gauge group
$\prod_\gamma \mathrm{Aut}(\mathfrak g_{\mathrm{BPS}, \gamma})$.

\textbf{Corollary (Lorgat 2020 Conj 1 reformulation).} \ClaimStatusConjectured
The Lie-algebra-level identification $\mathfrak g_{\mathrm{BPS}}(K3 \times E)
\simeq \mathfrak g_{\Delta_5}$ reduces to the statement that the Gritsenko
family of Hecke-like operators on paramodular forms (Gritsenko 1999,
lifting cusp forms on $\Gamma_0(N)$ to paramodular $\Phi_N$ forms) matches
the KS-motivic parallel transport on the BPS Lie algebra. Under this
reduction the bracket check on $\gamma_1 + \gamma_2 = \gamma$ becomes the
Hecke-Borcherds identity
\[
c_{\gamma_1} \cdot c_{\gamma_2} \cdot B(\gamma_1, \gamma_2) =
\sum_{\gamma_1 + \gamma_2 = \gamma} c_\gamma \cdot
\langle \alpha_{\gamma_1}, \alpha_{\gamma_2} \rangle
\]
for the Borcherds bilinear form $B$, to be verified via one-loop string
amplitudes (Harvey--Moore 1996 arXiv:hep-th/9510182 \S 4) or directly via
Gritsenko--Nikulin 1998 denominator expansion.

### D. $\Omega$-background scope: toric universality and its failure on
$K3 \times E$

\textbf{Theorem (toric-scope of $\Omega$-background, Nekrasov 2003
\texttt{arXiv:hep-th/0206161}).} \ClaimStatusTheorem
The Nekrasov $\Omega$-background construction for 4D $\mathcal N = 2$ on
$\mathbb C^2_{\epsilon_1, \epsilon_2}$ requires a toric $T^2$-action on
the 4-manifold with isolated fixed points. For a toric CY$_3$ $X = $
total space of a toric Fano/quasi-Fano family (e.g.~$\mathbb C^3$,
conifold, local $\mathbb P^2$), the 5D lift admits a $T^3$-action with
isolated fixed points, and the refined partition function exists as a
formal power series in $q_i = e^{\epsilon_i}$.

\textbf{Corollary (failure on $K3 \times E$).} \ClaimStatusTheorem
$K3 \times E$ has automorphism group $\mathrm{Aut}^0(K3 \times E) = E$
(generically on the K3 factor, no $\mathbb C^\times$-action). Of the
three putative $\Omega$-background parameters, exactly one survives:
\[
\epsilon_E := 2\pi i \epsilon_1^E / \hbar
\]
the translation parameter on the $E$-factor. The naive two-parameter
refinement $(\epsilon_1, \epsilon_2)$ collapses to the self-dual slice
$\epsilon_1 + \epsilon_2 = 0$, giving a \emph{single} $\Omega$-parameter
$u = \epsilon_E$ on $K3 \times E$.

\emph{Programme-consistent statement.} The two-parameter quantum-toroidal
action of the $\mathbb C^3$ CoHA lifts only to a \emph{one-parameter}
quantum-affine action on $K3 \times E$. The "quantum toroidal" language
common in the literature is inherited from $\mathbb C^3$ and does not
apply to $K3 \times E$ directly; the correct object is the
\emph{elliptic affine quantum group} $U_q(\widehat{\mathfrak g}_E)$
attached to the one-parameter surviving torus, at the
Kimura--Nieri--Pasquetti--Pomoni 2018 (\texttt{arXiv:1807.04557}) elliptic-RLL
presentation. This is what the treatise's K3$\times$E section should point
at rather than invoking the $\mathbb C^3$-native two-parameter refinement.

### E. Maulik--Okounkov scope and why the K3$\times E$ target needs
partial-localisation

\textbf{Theorem (Maulik--Okounkov 2019 \emph{Ast\'erisque} 408 framework).}
\ClaimStatusTheorem
MO construct stable envelopes for symplectic resolutions $X$ of affine
varieties $X_0 = X/\!\!/T$ with a $T$-action having finitely many
fixed components and satisfying the MO formality hypothesis. The output
is a Yangian-type quantum group acting on $\bigoplus_X H^*_T(X)$ via
correspondences in $X \times X$.

\textbf{Applicability gap on $K3 \times E$.} The MO framework does not
apply directly because:
\begin{enumerate}
\item $K3 \times E$ is not a symplectic resolution but a smooth proper
  CY$_3$; its holomorphic volume is an $(3,0)$-form, not a holomorphic
  symplectic 2-form.
\item The putative $T^2$-action on $K3 \times E$ is reduced to a single
  $T$-action on $E$; the MO framework requires two commuting tori on the
  resolution for the braided structure.
\item The fixed-point scheme is not zero-dimensional: any generic $K3$
  fibre has no non-trivial torus action, so the $E$-translation fixed
  locus on $K3 \times E$ is all of $K3 \times E[N]^{\mathrm{fix}}$, a
  positive-dimensional family.
\end{enumerate}

\textbf{Partial-localisation correction (Nikulin--Mukai via $M_{23}$).}
\ClaimStatusConjectured
Choose a symplectic automorphism group $G \subset M_{23} \subset M_{24}$
of a K3 surface (Mukai 1988). Then $G$-equivariant cohomology
$H^*_G(K3)$ is well-defined and the $G$-fixed locus $K3^G$ has positive
but tractable codimension. Passing to
\[
\CoHA^G_T(K3 \times E) := \bigoplus_\gamma H^*_{G \times T}(\mathcal M(K3 \times E)_\gamma,
\phi_W \cdot \mathrm{IC})
\]
for $T = E[N]$ the $N$-torsion translation subgroup, the MO construction
applies to the symplectic part of the fixed locus
$(K3^G \times E^{E[N]})$ in partial-localisation form.

\emph{Status.} This has not been carried out in the literature in the
form I just stated. The framework goes back to Hausel--Proudfoot 2004
(\emph{Oxf.~Math.~Monogr.}) for symplectic varieties and Oblomkov--Yun
2016 (\emph{Ann.~Math.}~184) for a specialised class of
positive-dimensional fixed loci; its application to $K3 \times E$ is an
open structural question. What is established: the \emph{character} of
the partial-localised CoHA equals the reduced DT generating function
$-C/\Phi_{10}$ (Oberdieck--Pixton 2016), so the dimension-level match
with $\mathfrak g_{\Delta_5}$ is unaffected by the partial-localisation
scope issue.

### F. Conifold chiral Yangian from holomorphic Chern--Simons

\textbf{Theorem (CoHA of the resolved conifold).} \ClaimStatusTheorem
(Davison 2012 \texttt{arXiv:1209.4620} for conifold CoHA;
Morrison--Mozgovoy--Nagao--Szendr\H{o}i 2010 for DT-invariants of the
conifold; Rap\v{c}\'ak--Soibelman--Yang--Zhao 2020 \texttt{arXiv:2001.10549}
for the toroidal side.)
Let $Q_{\mathrm{con}}$ be the conifold quiver (two vertices $\circ, \bullet$;
arrows $a_1, a_2 : \circ \to \bullet$ and $b_1, b_2 : \bullet \to \circ$;
potential $W = \mathrm{tr}(a_1 b_1 a_2 b_2 - a_1 b_2 a_2 b_1)$). Then
\[
\CoHA(\mathrm{conifold}) \simeq U(\mathfrak g_{\mathrm{BPS}}(\mathrm{conifold}))
\]
with $\mathfrak g_{\mathrm{BPS}}(\mathrm{conifold})$ a specific super Lie
algebra; after localisation in $\epsilon_1, \epsilon_2$ and taking the
positive half,
\[
\CoHA(\mathrm{conifold})^+_{\mathrm{loc}} \simeq Y^+_{\epsilon_1, \epsilon_2}
(\widehat{\widehat{\mathfrak{gl}}_2}).
\]
The shuffle kernel is
\[
\omega_{\mathrm{con}}(z, w) = \frac{(z - w + \epsilon_1)(z - w + \epsilon_2)}{(z - w)(z - w + \epsilon_1 + \epsilon_2)},
\]
reflecting the modified CY$_3$ constraint $\epsilon_1 + \epsilon_2 = 0$ on the
fibre directions only (the $\mathbb P^1$ direction is compact and does not
enter the equivariant parameter).

\textbf{Wall-crossing on the conifold.} \ClaimStatusTheorem
The conifold has a non-trivial chamber structure in Bridgeland stability
space due to the compact $\mathbb P^1$ (the exceptional curve of the
resolution). The DT generating function transforms across walls according
to the MNNS 2010 pentagon identity, exhibiting the six-chamber structure
of Szendroi 2008 \emph{Geom.~Topol.}~12. Each chamber's effective CoHA is
a distinct sub-Hall-algebra; the ambient $U(\mathfrak g_{\mathrm{BPS}}
(\mathrm{conifold}))$ is chamber-independent, but the set of simple stable
objects (generators) and thus the bar-complex dimensions differ across
chambers (cache row 3). This is the concrete manifestation of AP-CY149:
$\mathrm{Stab}(\mathrm{conifold})$ is more complex than
$\mathrm{Stab}(\mathbb C^3)$ which has a single chamber.

\textbf{Chiral Yangian on the conifold (conjectural).} \ClaimStatusConjectured
Costello--Li 2016 \texttt{arXiv:1606.00365} + Costello--Paquette 2020
\texttt{arXiv:2009.04834} framework: holomorphic Chern--Simons on the
resolved conifold $\mathbb Y$ with gauge $\mathfrak{gl}_r$ produces a
factorisation algebra $\mathcal F_{\hCS}(\mathbb Y)$ on $\mathbb Y$;
restriction to a defect line $\mathbb C_z \subset \mathbb Y$ along a
generic fibre direction gives a vertex algebra
$\mathcal F_{\mathrm{defect, con}}$ conjectured to be a quantum toroidal
algebra $U_{q_1, q_2}(\widehat{\widehat{\mathfrak{gl}}_2})$ at specific
parameters.

\emph{Status.} Character-level match verified (Awata--Feigin--Shiraishi 2011
\texttt{arXiv:1112.6074}); explicit generators-and-OPE match is
AP-CY149 open. The conifold is one step more complex than $\mathbb C^3$
in that the chamber structure is non-trivial; the $\hCS$ $\to$ vertex algebra
translation through the BV--BRST complex of Costello 2013 is applicable
perturbatively but the non-perturbative completion picks up compact-$\mathbb P^1$
BPS states which must be inserted as twist modules.

### G. One-loop BV anomaly on $K3 \times E$: universal vanishing

\textbf{Theorem.} \ClaimStatusTheorem On $K3 \times E$ the one-loop BV
obstruction to quantisation of holomorphic Chern--Simons with gauge
$\mathfrak g$ factorises as (Platonic Synthesis Thm
\ref{wn:thm:plat-anomaly})
\[
\kappa_{\mathrm{anom}}(K3 \times E, \mathfrak g) = \hbar A(\mathfrak g)
\cdot \frac{\chi_{\mathrm{top}}(K3 \times E)}{2(4\pi)^3} \cdot
\|\Omega_X\|^2 = 0
\]
for every gauge $\mathfrak g$, because
$\chi_{\mathrm{top}}(K3 \times E) = 24 \cdot 0 = 0$. The anomaly vanishes
not by cancellation between colour and space factors but because the
space factor is identically zero; this is the Künneth-multiplicative
consequence of $\chi_{\mathrm{top}}(E) = 0$ (the elliptic curve has
trivial tangent bundle). Consistent with $\kappa_{\mathrm{cat}}(K3 \times
E) = \chi(\mathcal{O}_{K3 \times E}) = \chi(\mathcal{O}_{K3}) \cdot
\chi(\mathcal{O}_E) = 2 \cdot 0 = 0$.

\emph{Implication.} $\hCS$ on $K3 \times E$ quantises at one loop without
obstruction for every $\mathfrak g$. The two-stage factorisation
$\Phi_3^{\mathrm{FA}}(K3 \times E) \to \mathrm{Sp}_{K3, E}(\cdots)$ is
definable; the specialisation landing in a chiral BKM on $E$ is not
obstructed by the one-loop BV anomaly.

## Retractions with true hidden structure

### R1. "$\CoHA(\mathbb C^3) = \mathcal W_{1+\infty}$" \ClaimStatusRetracted

\emph{Wrong claim.} Direct object-level identification of $\CoHA(\mathbb C^3)$
with $\mathcal W_{1+\infty}$.

\emph{Precise error.} $\CoHA(\mathbb C^3) = Y^+$ is the positive half of
the affine Yangian (Schiffmann--Vasserot 2013 Thm 1.1 on the localised
shuffle side). $\mathcal W_{1+\infty}$ is a vertex algebra; the full
Drinfeld-double Yangian $Y = Y^+ \bowtie Y^0 \bowtie Y^-$ is what maps
to $\mathcal W_{1+\infty}$-modes at specific parameters (Tsymbaliuk 2017
Thm 1.1). The conflation loses: (a) the positive-vs-full-Yangian
distinction; (b) the associative-algebra-vs-vertex-algebra operadic
distinction; (c) the doubling step. Three independent character checks
forbid direct identification:
(i) $\chi_{\CoHA}(\mathbb C^3) = M(q) = \prod (1-q^n)^{-n}$ (MacMahon plane
partitions); (ii) $\chi_{\mathcal W_{1+\infty}} = P(q) \cdot \prod_{n \geq 2}
(1-q^n)^{-(n-1)}$ (Feigin--Frenkel free-boson count at $\lambda = 1$);
(iii) $M(q) / P(q) = \prod_{n \geq 2}(1-q^n)^{-(n-1)}$ is the positive-half
higher-spin tower missing from pure Yangian-positive.

\emph{Ghost theorem.} The correct chain is
\[
\CoHA(\mathbb C^3) = Y^+ \xrightarrow{\mathcal D_\hbar\text{-double}}
Y \xrightarrow{\mathrm{Tsymbaliuk}} U(\mathcal W_{1+\infty})_{c=1}.
\]
Three independent theorems, each cited explicitly.

### R2. "$\CoHA(K3 \times E) = U(\mathfrak n_+(\mathfrak g_{\Delta_5}))$"
\ClaimStatusRetracted

\emph{Wrong claim.} Direct identification with the positive half envelope.

\emph{Precise error.} Davison's PBW gives
$\CoHA^{\mathrm{BPS}}(X) \simeq U(\mathfrak g_{\mathrm{BPS}}(X))$ with the
\emph{full} Lie algebra, not the positive half. The BKM triangular
decomposition $\mathfrak g_{\Delta_5} = \mathfrak n_- \oplus \mathfrak h
\oplus \mathfrak n_+$ is determined by $\Phi_{10}$ Fourier coefficients; the
BPS-effective-cone positivity on $\CoHA$ gives a different splitting.
(Cache row A7-1; AP-CY145.)

\emph{Ghost theorem.}
(a) $\CoHA(K3 \times E) \cong U(\mathfrak g_{\mathrm{BPS}}(K3 \times E))$ as
associative algebras (Davison PBW, conditional on the critical-chart
hypothesis).
(b) $\chi_{\mathrm{gr}}(\CoHA(K3 \times E)) = Z^{\mathrm{red,\prime}}_{DT}
(K3 \times E) = -C/\Phi_{10}$ (Oberdieck--Pixton 2016).
(c) $\mathfrak g_{\mathrm{BPS}}(K3 \times E) \stackrel{?}{\simeq}
\mathfrak g_{\Delta_5}$ bracket-level identification is open.

### R3. "$\Omega$-background produces the $K3 \times E$ answer" \ClaimStatusRetracted

\emph{Wrong claim.} Lifting Nekrasov's toric universality to $K3 \times E$.

\emph{Precise error.} Nekrasov $\Omega$-background is defined on toric
geometries with $T^2$-localisation. It applies: $\mathbb C^3$, conifold,
local $\mathbb P^2$, local $\mathbb P^1 \times \mathbb P^1$. It does NOT
apply: $K3 \times E$ (only a one-parameter $T$ on $E$ survives),
quintic, compact non-toric CY$_3$.

\emph{Ghost theorem.} On $K3 \times E$, exactly ONE $\Omega$-parameter
survives: $\epsilon_E = 2\pi i \epsilon_1^E / \hbar$ along the elliptic
fibre. Five routes (DT, Borcherds, MO, Vafa--Witten, relative) all pick up
the same $\epsilon_E$. The two-parameter refined topological vertex
collapses to the self-dual slice $q_1 q_2 = 1$ on $K3 \times E$.
(AP-CY149 K3.)

### R4. "Maulik--Okounkov stable envelopes construct the K3$\times E$
Yangian" \ClaimStatusCorrected

\emph{Wrong claim framing.} Direct MO application to $K3 \times E$.

\emph{Precise error.} MO framework requires (i) a symplectic resolution
(not merely a smooth CY$_3$), (ii) a $T$-action with finitely many fixed
components, (iii) the formality hypothesis. $K3 \times E$ is not a
symplectic resolution (it is a CY$_3$ with $(3,0)$-form, not a
$(2,0)$-symplectic form), has no generic $T$-action on the K3 factor, and
the $E[N]$-translation fixed locus is positive-dimensional.

\emph{Ghost theorem.} Partial-localised MO on $(K3^G \times E^{E[N]})$ for
$G \subset M_{23}$ a Mukai group: apply the Hausel--Proudfoot--Oblomkov--Yun
generalisation for positive-dimensional fixed loci, plus $G$-equivariant
cohomology to access an effective symplectic structure. Status:
framework-consistent, explicit construction open (AP-CY149 K4).

### R5. "The conifold vertex algebra is $\mathcal W_{1+\infty}(\gglone)$"
\ClaimStatusRetracted

\emph{Wrong claim.} Direct identification with the $\mathbb C^3$ vertex
algebra.

\emph{Precise error.} The conifold has a non-trivial Bridgeland chamber
structure (pentagon wall-crossing from the compact $\mathbb P^1$ BPS states
that $\mathbb C^3$ lacks). The shuffle kernel $\omega_{\mathrm{con}}(z, w)
= (z-w+\epsilon_1)(z-w+\epsilon_2)/[(z-w)(z-w+\epsilon_1+\epsilon_2)]$
differs from $\omega_{\mathbb C^3}(z, w)$ in having a regular numerator of
lower degree (two factors of $(z-w+\epsilon_i)$ rather than three).

\emph{Ghost theorem.} $\CoHA(\mathrm{conifold})^+_{\mathrm{loc}} \simeq
Y^+_{\epsilon_1, \epsilon_2}(\widehat{\widehat{\mathfrak{gl}}_2})$ (not
$Y^+(\gglone)$). The vertex-algebra shadow is quantum toroidal at two
parameters, not $\mathcal W_{1+\infty}$ which is its $\mathfrak{gl}_1$
one-parameter shadow.

## Cross-consistency checks

### (a) Harmonisation with platonic\_synthesis\_waves\_11\_through\_16.tex

\begin{itemize}
\item Two-stage factorisation $\Phi_3 = \mathrm{Sp}_{\Sigma_2, C} \circ
\Phi^{\mathrm{FA}}_3$ (plat Thm 2.1) matches this treatise's
Example-3 framework: $\Phi^{\mathrm{FA}}_3$ produces the $E_3$-holomorphic
factorisation algebra on $K3 \times E$; specialisation
$\mathrm{Sp}_{K3, E}$ to the elliptic curve $E$ recovers the chiral BKM
target (plat Thm \texttt{wn:thm:plat-Sp-K3E}). The CoHA construction is
the \emph{categorical-Hall} incarnation of the $\Phi$-functor at $d = 3$,
with critical-chart localisation giving the BPS Lie algebra as the
primitive image.
\item $\kappa_{\mathrm{anom}}(K3 \times E) = 0$ (plat Thm
\texttt{wn:thm:plat-anomaly}) verified here: $\chi_{\mathrm{top}}(K3 \times E)
= 0$ forces the space factor to vanish, independent of colour Casimir.
\item Minimal $L_\infty$-model on $\CC^3$ (plat Thm
\texttt{wn:thm:plat-Linf-minimal}) is the $\CoHA(\mathbb C^3)$ shuffle
structure at the level of algebra (positive half); the $E_3$-algebra
structure of the BV complex is its geometric ambient.
\item Miki $S_3$ on $\mathcal W_{1+\infty}$ as shadow of Miki on
$\CoHA(\mathbb C^3) = Y^+$ (plat Thm \texttt{wn:thm:plat-Miki-S3}):
shuffle-kernel $\omega$ is $S_3$-equivariant in the three parameters
$(\epsilon_1, \epsilon_2, \epsilon_3)$, inherited by $Y^+$ and descending
via Tsymbaliuk to $\mathcal W_{1+\infty}[\lambda]$.
\item Dimension-stratified siblings (plat Conj
\texttt{wn:conj:plat-siblings-dim}): on $K3 \times E$ the CoHA construction
yields one specialisation ($\mathrm{Sp}_{K3, E}$, $\kappa_{\mathrm{BKM}} = 5$);
the Fake Monster cousin at $d = 5$ uses $K3 \times K3 \times E$ with a
different specialisation cycle $\Sigma_4 = K3 \times K3$, producing
$\kappa_{\mathrm{BKM}}(\Phi_{\mathrm{FM}}) = 12$.
\end{itemize}

### (b) Harmonisation with CoHA\_to\_W\_infty\_treatise.tex worked examples

\begin{itemize}
\item Example 1 ($\mathbb C^3$): treatise line 100--105 SV Thm 1.1 statement
is correct if read over $\mathbb F$; my sharpening makes this explicit.
\emph{Recommendation}: the treatise should insert "over $\mathbb F$" or
"localised" where it writes $\CoHA(\mathbb C^3) \simeq Y^+$.
\item Example 2 (resolved conifold): treatise lines 391--398 Rapčák--Soibelman--
Yang--Zhao + Kapranov--Vasserot identifications are correct; I add the
wall-crossing-explicit scope: the conifold's pentagon chamber structure
means that the chiral-Yangian shadow depends on the Bridgeland chamber,
not just on the choice of defect line; this is the non-trivial content of
the conifold chiral Yangian versus $\mathcal W_{1+\infty}$.
\item Example 3 ($K3 \times E$): treatise lines 458--536 correctly scope
Davison's PBW, dimension match, and Open Lie-algebra bracket. My
contribution: explicit KS motivic parallel transport statement
(Theorem C above) that refines the bracket check to a
\emph{Hecke--Borcherds identity} (Gritsenko 1999) on the Fourier side of
$\Delta_5$. This is the residual frontier question.
\end{itemize}

### (c) $\kappa$-subscript universal identity
$\kBKM(\Phi_N) = c_N(0)/2$

Confirmed in both programme-core CHL scope $N \in \{1, 2, 3, 4, 6\}$ and
full 8-form Gritsenko--Cléry scope $N \in \{1, \ldots, 8\}$. At $N = 1$:
$\kBKM(\Delta_5) = c_1(0)/2 = 10/2 = 5$ (\emph{Gritsenko} 1995; Lorgat 2020
gives the explicit generator-pair structure on $\phi_{0, 1}$ via
$f(0, 0) = 10$). At $N = 2$: $\kBKM(\Phi_2) = c_2(0)/2 = 8/2 = 4$
(matching Oberdieck 2018 \emph{JEMS} 20 twisted DT). At $N = 6$:
$\kBKM(\Phi_6) = c_6(0)/2 = 2/2 = 1$.
My treatment does not modify the universal formula; the CoHA-side
dimension-match corollary (Theorem B) consumes it as input.

### (d) Two-stage factorisation $\Phi_d = \mathrm{Sp}_{\Sigma, C} \circ
\Phi^{\mathrm{FA}}_d$

The CoHA construction at $d = 3$ is the categorical-Hall incarnation of
$\Phi^{\mathrm{FA}}_3$. Stage 1: $D^b(\mathrm{Coh}(X)) \mapsto
\CoHA(X) = \bigoplus_\gamma H^*(\mathcal M_\gamma, \phi_W \cdot \mathrm{IC})$
is canonically an $E_3$-factorisation algebra on $X$ (Kontsevich--Soibelman
2008 Thm 5.1; critical-cohomology version in Davison--Meinhardt 2020).
Stage 2: specialisation $\mathrm{Sp}_{K3, E}$ is factorisation homology of
the $E_3$-hFA over the K3 fibre, giving an $E_1$-chiral algebra on $E$;
this $E_1$-chiral algebra is the conjectural $\mathbf{H}_{\Delta_5}$, with
BPS sub-Lie-algebra $\mathfrak g_{\Delta_5}$.

\emph{Scope of what is CoHA-side witnessed.} The CoHA-side carries only the
Stage-1 $E_3$-factorisation algebra at the level of \emph{associative}
structure (Hall product). The $E_3$-operadic level and the chiral
factorisation on a curve through Stage 2 require the full
$\Phi^{\mathrm{FA}}$ construction via Costello--Gwilliam Vol 2 \S 10--11.

## Residual frontier

\begin{itemize}
\item \ClaimStatusOpen The bracket-level Lie-algebra isomorphism
$\mathfrak g_{\mathrm{BPS}}(K3 \times E) \simeq \mathfrak g_{\Delta_5}$.
Reduces to a single Hecke--Borcherds identity on the Gritsenko 1999 family
(Corollary C above).

\item \ClaimStatusOpen The global critical-chart hypothesis on
$K3 \times E$: does Brav--Bussi--Dupont--Joyce--Szendroi local Darboux plus
Toda's orientation-selection glue to a global critical chart on all of
$\mathcal M(K3 \times E)$? Known for the Hilbert component; open for the
general moduli component with imprimitive K3 class.

\item \ClaimStatusOpen Partial-localisation Maulik--Okounkov construction on
$(K3^G \times E^{E[N]})$ for $G \subset M_{23}$. Framework via Hausel--
Proudfoot--Oblomkov--Yun; explicit stable envelopes on $K3 \times E$ open.

\item \ClaimStatusOpen Explicit shuffle formula for $\CoHA(K3 \times E)$
(treatise summary table line 694). The $\mathbb C^3$ and conifold cases
have explicit shuffle kernels; for $K3 \times E$, even the shuffle
\emph{presentation} is open, because non-toric CY$_3$s lack the shuffle
realisation via torus localisation.

\item \ClaimStatusOpen Explicit vertex-algebra generators and OPEs of the
conifold chiral Yangian (treatise line 430). Costello--Li + Costello--Paquette
framework sets up the hCS $\to$ vertex algebra translation; explicit
formulas for all generators and OPEs require pushing the perturbative
BV--BRST complex to include non-perturbative twist modules from the
compact $\mathbb P^1$ BPS states.

\item \ClaimStatusOpen Hecke--Borcherds identity in the KS motivic lift:
for $(\gamma_1, \gamma_2)$ with $\gamma_1 + \gamma_2 = \gamma$, the
bracket $[\mathfrak g_{\mathrm{BPS}, \gamma_1}, \mathfrak g_{\mathrm{BPS},
\gamma_2}]$ equals $c_\gamma \cdot \langle \alpha_{\gamma_1}, \alpha_{\gamma_2}
\rangle$ on the Gritsenko--Nikulin paramodular side. Verification via
Harvey--Moore 1996 one-loop string amplitudes (arXiv:hep-th/9510182) or
directly via Gritsenko--Nikulin 1998 denominator expansion.

\item \ClaimStatusOpen Elliptic-surface specialisation
$(\Sigma_2, C) = (\mathcal E, \mathbb P^1)$ for a Mordell--Weil-indexed
unification of the six routes to $G(K3 \times E)$ as $\mathrm{Aut}(K3)
\times \mathrm{SL}_2(\mathbb Z)$-orbits in $H_4(K3 \times E; \mathbb Z)$
(plat frontier item 1; Wave 16 S2).

\end{itemize}

## Attack-heal cycle log (private, not for manuscript)

Cycle 1: ATTACK --- Does Schiffmann--Vasserot 2013 Thm 1.1 actually identify
$\CoHA(\mathbb C^3) = Y^+$ or is the identification up to localisation?
HEAL --- Direct-from-paper: SV Thm 1.1 is stated over the localised ring
$\mathbb F = \mathbb C(\epsilon_1, \epsilon_2)$; the integral version in SV
\S 8 has cokernel killed by $(\epsilon_1 \epsilon_2 \epsilon_3)$. Treatise's
wording of "$\CoHA(\mathbb C^3) = Y^+$" should carry "over $\mathbb F$" or
"localised" in the body; the cache tag KEY FACT \#3 is correctly scoped.
Theorem A above sharpens this.

Cycle 2: ATTACK --- Does Davison's critical-CoHA formalism apply globally to
compact $K3 \times E$, or only to local critical charts?
HEAL --- Requires global critical-chart hypothesis, which amounts to a
Joyce d-critical orientation. Local Darboux charts exist by Brav--Bussi--
Dupont--Joyce--Szendr\H oi 2015; global gluing is an orientation-selection
problem solved on the Hilbert component by Toda 2018 but open in the general
moduli component with imprimitive K3 class. Theorem B above scopes this
correctly.

Cycle 3: ATTACK --- Does the MO machinery actually apply to $K3 \times E$?
HEAL --- No: MO needs symplectic resolution plus $T$-action with finite
fixed components. $K3 \times E$ is CY$_3$ with $(3,0)$-form (not symplectic
2-form) and generic K3 has no $T$-action; fixed locus of $E[N]$-translation
is positive-dimensional. Partial-localised framework via $G \subset M_{23}$
Mukai groups plus Hausel--Proudfoot is the correct route. Theorem E and
retraction R4 above.

Cycle 4: ATTACK --- Can $\mathfrak g_{\mathrm{BPS}}(K3 \times E) \simeq
\mathfrak g_{\Delta_5}$ be established? What is the exact obstacle?
HEAL --- Dimension-level equality is a theorem (Oberdieck--Pixton +
Gritsenko--Nikulin + Davison integrality). Bracket-level isomorphism is
open and reduces to a single Hecke--Borcherds identity on the Gritsenko
1999 family. This sharpens Lorgat 2020 Conj 1 to an arithmetic statement
(Corollary C above).

Cycle 5: ATTACK --- How does the cohomological-BPS vs motivic-BPS
distinction play out on $K3 \times E$? Does the cohomological version
suffice for the BPS Lie algebra identification?
HEAL --- Cohomological BPS is the version that gives the integer-valued
multiplicities $\Omega(\gamma) \in \mathbb Z$ compatible with KS motivic
integrality; it is the version compatible with the Borcherds Fourier
coefficients of $\Delta_5$ (Gritsenko 1999 integrality). Motivic BPS
refines to $\Omega^{\mathrm{mot}}(\gamma) \in K_0(\mathrm{MHM})$ with a
Hodge-structure lift; for $K3 \times E$ the motivic refinement is a
separate structural statement and the Hodge-polynomial level match with
$\Delta_5$ is an additional conjectural layer not yet addressed.
Cohomological-BPS is sufficient for the programme's central identification
question; motivic-BPS is open-but-not-required at this level.

Cycle 6: ATTACK --- Does the conifold stability-chamber structure
produce a wall-dependent chiral Yangian? Does this break the treatise's
Example-2 framing?
HEAL --- Six Bridgeland chambers (Szendroi 2008 \emph{Geom.~Topol.}~12):
resolved, small-flop, large-flop, derived-equivalent chambers. The
ambient $U(\mathfrak g_{\mathrm{BPS}}(\mathrm{conifold}))$ is
chamber-independent (KS motivic wall-crossing); the set of simple
stable generators changes across walls. Cache row 3 is the sharp
statement: chamber-specific Hall sub-algebras differ in bar-complex
dimensions, ambient algebra does not. The chiral-Yangian shadow depends on
defect line \emph{and} chamber; treatise example 2 is schematically
correct but could sharpen the wall-crossing point. Theorem F above.

Cycle 7: ATTACK --- Can the $\Omega$-background two-parameter refinement
on $\mathbb C^3$ be transported to $K3 \times E$ via fibrewise localisation
on $E$?
HEAL --- No: on $K3 \times E$ the automorphism group is $E$ (a 1-dim
torus on the fibre direction), not $T^2$. The would-be second parameter
has no global home. Exactly one $\Omega$-parameter survives:
$\epsilon_E$ along $E$. This is AP-CY149 K3 and it is the correct
statement; the $(\epsilon_1, \epsilon_2)$-refinement is a toric artefact.
Theorem D above.
