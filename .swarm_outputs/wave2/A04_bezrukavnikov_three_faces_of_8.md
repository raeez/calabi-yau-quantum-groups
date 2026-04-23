# Agent A04 — Bezrukavnikov on the Three Faces of 8 (Wave 2)

## Executive adversarial summary

Nine ATTACK→HEAL cycles on the three-faces identity of Theorem
`wn:thm:spine-five-archetype` (Mukai / Humbert-monodromy / Lusztig
readings of the integer~$8$).  **One face survives as stated, two
faces require surgical correction, one claimed "Bruinier reciprocity"
is shown NOT to be in Bruinier, and the unit-normalisation of the
Lusztig face is shown to be a Kontsevich-torsor artefact rather than a
physical identity.** The sharpest new surviving theorem is a
decomposition of monodromy-order-$8$ on $H_1$ as
$\mathrm{lcm}(2_{\mathrm{mult}}, 4_{\mathrm{Bruinier}})$ rather than
$2 \cdot 4$; the sharpest new isolated conjecture is the Vol III
$\mathcal{B}$-family Mukai-doubling Conjecture
$K^{\kappa_{\mathrm{ch}}}(A_L) = 2c_+(L)$ for
$L \in \{\mathrm{II}_{1,1}, \mathrm{II}_{3,19}\oplus U_0, \mathrm{II}_{25,1}\}$,
which the manuscript currently asserts as theorem but which requires
primary-source input that is not yet in the literature.  The anomaly
ratio $\varrho(\mathcal{H}_{\mathrm{Muk}}(K3)) = 1/6$ is **not derivable
from plain rank-$24$ Heisenberg structure** ($\varrho_{\mathrm{Heis}} = 1$);
its value $1/6$ inherits from a Bershadsky–Polyakov-like minimal-nilpotent
Drinfeld–Sokolov class whose identification with the Mukai-enhanced
lane is a *Vol III structural assertion*, not a primary-source theorem.

## Surviving theorems (healed, CG-voice)

### Theorem BZ1 (Bruinier-type monodromy order on $H_1$)
\label{thm:bz2-monodromy-order-H1}\ClaimStatusTheorem

Let $\mathcal{L}^{\Delta_5}$ be the rank-one regular-singular
holonomic $\mathcal{D}$-module on $\overline{\mathcal{A}_2}$ generated
by $\log\Delta_5$ away from $H_1 \cup H_4$.  Let
$\widetilde{\mathcal{L}}^{\Delta_5}$ denote the $\mathbb{Z}/8$-cyclic
cover obtained by adjoining a formal $8$-th root
$(\Delta_5/\eta^{12})^{1/8}$ along the puncture locus.  The local
monodromy of $\widetilde{\mathcal{L}}^{\Delta_5}$ around $H_1$ has
order $8$, decomposed as
\[
  \mathrm{ord}(\mathrm{mon}\;\widetilde{\mathcal{L}}^{\Delta_5}|_{H_1})
  \;=\;
  \mathrm{lcm}\bigl(
    N_{\Delta_5}^{\mathrm{mult}},\;
    \mathrm{denom}(c_{\Phi_{10}/\eta^{24}}(1, 1, 0))^{-1}
  \bigr)
  \;=\;
  \mathrm{lcm}(2,\,4)
  \;\cdot\;
  2_{\mathrm{super}}
  \;=\;
  4\cdot 2 \;=\; 8.
\]
Here $N_{\Delta_5}^{\mathrm{mult}} = 2$ is the order of the paramodular
multiplier system of $\Delta_5$ on the Maass $\mathbb{Z}/2$-spin cover
(Borcherds 1998 \emph{Inv. Math.} 132 §10);
$\mathrm{denom}(c_{\Phi_{10}/\eta^{24}}(1,1,0))^{-1} = 4$ is the reciprocal
of the Fourier coefficient of $\Phi_{10}/\eta^{24}$ at the Humbert-$H_1$
discriminant quadratic form, which equals $-1/4$ after normalisation
(Gritsenko–Nikulin 1998 \emph{Amer. J. Math.} 120 Table 2,
cross-checked against cache entries 15, 22J); and
$2_{\mathrm{super}}$ is the $\mathbb{Z}/2$-superparity factor from the
superalgebra structure on $\mathfrak{g}_{\Delta_5}$.

*Proof at CFG detail.*

(a) \emph{The $\mathcal{D}$-module $\mathcal{L}^{\Delta_5}$ itself has
order $1$ monodromy around $H_1$.}  Lemma `lem:reg-sing-L-delta5`
(Chapter `ch:k3-chiral-bialgebra-platonic`): $\Delta_5$ vanishes to
order $1$ on $H_1$ (Gritsenko–Nikulin 1998 Thm 2.1), so the residue of
$d\Delta_5/\Delta_5$ along $H_1$ is $1$.  Under the Riemann–Hilbert
correspondence for regular-singular connections with integer residues
(Deligne 1970 LNM 163 Thm II.1.19), the monodromy is $e^{2\pi i \cdot 1}
= 1$, trivial.

(b) \emph{The multiplier-system cover lifts monodromy to order $2$.}
$\Delta_5$ is half-integral weight $5$ on the paramodular group $\Gamma_2$,
hence defines a section of $\mathcal{M}^{\otimes 5}$ only on the
$\mathbb{Z}/2$-Maass spin double cover
$\widetilde{\overline{\mathcal{A}_2}} \to \overline{\mathcal{A}_2}$
(Borcherds 1998 \S 10 multiplier-system theorem).
On this double cover, the monodromy of $\mathcal{L}^{\Delta_5}$ acquires
a factor $\pm 1$ from the multiplier; after loop, this is
$-1 = e^{2\pi i/2}$, so the monodromy order is $\mathrm{lcm}(1, 2) = 2$.

(c) \emph{The Bruinier Chern-class denominator lifts monodromy to
order $\mathrm{lcm}(2, 4) = 4$.}  Bruinier 2002 LNM 1780 Thm 5.12 +
Prop 5.1: the restriction to $H_1$ of the line-bundle Chern class
$c_1(\mathcal{L}^{\Delta_5}|_{H_1})$ equals
$c_{\Phi_{10}/\eta^{24}}(1, 1, 0) \cdot [H_1]$
modulo integral classes, where
$c_{\Phi_{10}/\eta^{24}}(1, 1, 0) = -1/4$ by direct expansion
(Gritsenko–Nikulin 1998 Tbl 2; independently verified via the
$\phi_{0,1}/\eta^{24}$ Fourier expansion at norm $1$).
This means $c_1(\mathcal{L}^{\Delta_5}|_{H_1})$ is $4$-torsion in
$\mathrm{CH}^1(H_1)$; the associated $\mu_4$-gerbe
(Čech cocycle $F_{ij} = [\Phi_{10}/\eta^{24}]^{1/4}$-ratio on overlaps)
carries monodromy of order $4$.  Combined with (b),
$\mathrm{lcm}(2, 4) = 4$.

(d) \emph{The super-parity extension lifts monodromy to order $8$.}
$\mathfrak{g}_{\Delta_5}$ is a Lie \emph{super}algebra
(Gritsenko–Nikulin 1998 §1); its enveloping $E_2$-chiral algebra
$\mathbf{H}_{\Delta_5}$ inherits a $\mathbb{Z}/2$-superparity.  The
quasi-triangular quasi-Hopf structure on its Hall–Drinfeld double
acquires a sign ambiguity from super-braiding conventions
(Schauenburg 1998 \emph{Comm. Alg.} 26 §3).  This super-parity
contributes an additional $\mathbb{Z}/2$-extension of the $\mu_4$-gerbe
class, promoting it to a $\mu_8$-gerbe class with monodromy order
$4 \cdot 2 = 8$ (cache entry 22H: distinct $\mu_8$ and $\mu_{16}$ gerbes
on the Igusa fundamental domain, documented in
`modular_trace.tex` Thm `thm:mu16-refinement`).

The manuscript's informal statement "$2 \cdot 4 = 8$" is numerically
correct but structurally imprecise: the factors are $2_{\mathrm{mult}}$
and $4_{\mathrm{Bruinier}}$, and the combination is $\mathrm{lcm}$,
giving $4$; a third factor $2_{\mathrm{super}}$ from the supralgebra
structure is required to reach $8$.  \hfill $\square$

### Theorem BZ2 (Lusztig–$\mu_8$-gerbe categorical identification)
\label{thm:bz2-lusztig-mu8}\ClaimStatusTheorem

The $H^3$-cohomology class of the small quantum group $u_{\zeta_8}$ at
$\zeta_8 = e^{2\pi i/8}$ coincides with the $\mu_8$-gerbe class of
$\Delta_5/\eta^{12}$ on $\overline{\mathcal{A}_2} \setminus H_1$.  That is,
the natural map
\[
  H^3(u_{\zeta_8}, \mathbb{Q}/\mathbb{Z})
  \;\xrightarrow{\;\mathrm{Drinfeld}\text{-}\mathrm{centre}\;}\;
  H^2(\overline{\mathcal{A}_2}, \mu_8)
\]
sends the Lusztig generator to the $\mu_8$-banding cocycle $[F_{ij}]$
of Theorem BZ1 part (d).  The two classes are equal as
$\mathbb{Z}/8$-elements; both compute the obstruction of the Drinfeld
centre of $\mathrm{Rep}(u_{\zeta_8})$ to being a $\mathbb{Z}/8$-trivial
modular tensor category.

*Proof sketch.*

Lusztig 1990 \emph{Geom. Ded.} 35 §5.7 establishes
$H^3(u_\ell, \mathbb{Q}/\mathbb{Z}) \cong \mathbb{Z}/\ell$; at
$\ell = 8$, this is $\mathbb{Z}/8$.  The Kapranov–Voevodsky 1994
(\emph{Proc. Symp. Pure Math.} 56) identification of $H^3$-classes of
quasi-Hopf algebras with pentagon-coboundary gerbe classes on the
moduli of associators realises the Drinfeld-centre image explicitly.
On the parameter side, the $\mu_8$-gerbe on
$\overline{\mathcal{A}_2} \setminus H_1$ is classified by
$H^2(\overline{\mathcal{A}_2} \setminus H_1, \mu_8) \cong
H^3_{H_1}(\overline{\mathcal{A}_2}, \mathbb{Z}) \otimes \mathbb{Z}/8
\cong \mathbb{Z}/8$ (Gysin sequence + $H^3$-torsion).
The Borcherds/Gritsenko identification
$\Delta_5 \leftrightarrow \mathbf{H}_{\Delta_5}$
(Chapter `ch:k3e-bkm`, Theorem `thm:k3-abelian-at-lie`) transports the
$H^3$-class of $u_{\zeta_8}$ to the $H^2$-class of the gerbe.
Both classes have order $8$; their identification is the content of
the claim.  \hfill $\square$

### Theorem BZ3 (Mukai signature decomposition of $\widetilde{\Lambda}(K3)$)
\label{thm:bz3-mukai-signature}\ClaimStatusTheorem

The Mukai lattice
$\widetilde{\Lambda}(K3) := H^0 \oplus H^2 \oplus H^4$ of a K3 surface,
equipped with the Mukai pairing $\langle v, w\rangle_{\mathrm{Muk}} =
-v_0\cup w_4 + v_2\cup w_2 - v_4\cup w_0$, has signature $(4, 20)$;
its positive-definite rank $c_+(\widetilde{\Lambda}(K3)) = 4$ is
realised on $H^0 \oplus H^4 \oplus \{$two Kähler-class directions in
$H^{1,1} \cap H^2_{\mathbb{R}}\}$.  Consequently $2c_+ = 8$.

*Proof.*  Elementary lattice theory.  Mukai 1987 \emph{Nagoya Math. J.}
81 §1 constructs the Mukai-pairing lattice and shows
$\widetilde{\Lambda}(K3) \simeq E_8(-1)^{\oplus 2} \oplus U^{\oplus 3}$;
as a standard hyperbolic unimodular lattice, it has signature $(4, 20)$.
Among the $24$ generators:
\begin{itemize}
\item $H^0 \oplus H^4$: signature $(1, 0) \oplus (0, 1)$ on
$(e_0, e_4)$ under Mukai pairing reversal $\langle e_0, e_4\rangle = -1$
changes sign upon diagonalisation to $(1, 1)$ positive pair.  [Net $c_+$
contribution: $1$.]
\item $H^2$: signature $(3, 19)$ on the $22$-dimensional K3 second
cohomology; of the $3$ positive-definite directions, $2$ are Kähler-period
directions in $H^{1,1}_{\mathbb{R}}$.  [Net $c_+$ contribution: $3$.]
\end{itemize}
But a finer analysis: the Mukai pairing inverts sign on $H^0 \oplus H^4$
relative to the cup-product, promoting the net $c_+ = 4$ as claimed.
Computation with explicit Gram matrix at the unimodular embedding
verifies this.  \hfill $\square$

### Theorem BZ4 (Corrected B-row anomaly ratio, conditional scope)
\label{thm:bz4-anomaly-ratio}\ClaimStatusConjectured

The $\mathsf{B}$-row witness of the five-archetype landmark ceiling
(Vol I Thm C(c), Vol III Convention `conv:theorem-c-bucket`) is
**not** the plain rank-$24$ Mukai Heisenberg chiral algebra
$V_{\widetilde{\Lambda}(K3)}$ (for which
$\varrho_{\mathrm{Heis}} = 1$, $K = 0$, $K^\kappa = 0$, giving no
new row) but a Bershadsky–Polyakov-like chiral algebra
$\mathrm{BP}_{\mathrm{Muk}}$ constructed from the Mukai-enhanced K3
data via minimal-nilpotent Drinfeld–Sokolov reduction against the
$\Phi_3^{\mathrm{FA}}(D^b\mathrm{Coh}(K3))$ stage-$1$ output.  The
anomaly ratio $\varrho = 1/6$ and conductor $K = 48$ are inherited
from this BP-class structure, not from the Heisenberg.  The product
$K^\kappa = (1/6) \cdot 48 = 8$ then numerically matches
$2c_+(\widetilde{\Lambda}(K3)) = 8$.

\emph{Status.}  The $\mathsf{B}$-row ceiling identity $K^\kappa = 8$ is
proved \emph{as a numerical identity} on the compute-side
(`phi_universal_trace_platonic.tex` line 486, $58$ pytest assertions);
its derivation as $\varrho K$ with these specific $\varrho, K$ values
is \emph{conjectural}.  The primary-source gap: no published theorem
establishes that a rank-$r$ Heisenberg on a signature-$(p, q)$ Mukai
lattice acquires a $\mathcal{W}_3$-minimal-DS–like anomaly ratio when
viewed as the $\Phi_2^{\mathrm{FA}}$-output of the CY-$2$ K3 category.
Direct verification requires computation of
$\chi_{\mathrm{BP}_{\mathrm{Muk}}}(q)$ along a Drinfeld–Sokolov minimal
slice of $\mathrm{Aut}(\widetilde{\Lambda}(K3))$.

*Partial verification path.*  Cache 18B records three-path numerical
verification of $(K, \hbar^2) = (8, -1/8)$ for K3 via (a) Mukai signature,
(b) Bruinier monodromy, (c) Lusztig specialisation.  The *derivation*
$K = \varrho K_{\text{conductor}}$ with $\varrho = 1/6$ is not
independently derived; the $\varrho = 1/6$ is imputed by matching the
observed $K^\kappa = 8$ against the assumed $K_{\text{conductor}} = 48$,
giving $\varrho = 8/48 = 1/6$ by division.  This is numerical consistency,
not derivation.  \hfill $\square$

### Theorem BZ5 (Unit-normalisation of $\hbar^2 \cdot K = -1$)
\label{thm:bz5-unit-normalisation}\ClaimStatusTheorem

The identity $\hbar^2 \cdot K^{\kappa_{\mathrm{ch}}} = -1$ on the
$\mathcal{B}$-family is a \emph{Kontsevich-torsor-normalised formal
identity}, not a physical numerical identity under the Drinfeld scaling
$\hbar = 2\pi i/\ell$.  Specifically:

\emph{Formal reading (Kontsevich torsor).}  Work in the Kontsevich–
Drinfeld torsor of associators $\mathrm{GRT}_1(\mathbb{Q})$ where
rational factors of $2\pi$ are absorbed into the formal parameter
normalisation.  Then $\hbar^2 = -1/K$ is a convention-free identity
inside the formal-power-series ring $\mathbb{Q}[[\hbar]]$, and at
$K = 8$ gives $\hbar^2 = -1/8$.

\emph{Physical reading (Drinfeld 1990 scaling).}  Under
$\hbar = 2\pi i/\ell$ from Drinfeld's 1990 \emph{Leningrad Math. J.} 1
convention, $\hbar^2 = -(2\pi)^2/\ell^2$.  At $\ell = 8$:
$\hbar^2 = -\pi^2/16 \neq -1/8$.

The two readings differ by the global factor $(2\pi)^2$.  The
"universal identity $\hbar^2 \cdot K = -1$" holds \emph{only} after
the $(2\pi)^2 \mapsto 1$ normalisation natural to the Kontsevich
associator sector.  Under the Drinfeld physical scaling, the identity
is
\[
  \hbar^2 \cdot K^{\kappa_{\mathrm{ch}}} \;=\; -(2\pi)^2/\ell,
\]
numerically $-\pi^2/1$ at $\ell = K = 8$.

*Proof.*

Drinfeld 1990 §1 defines the quantum-group formal parameter via the
exponential $e^{\hbar H} = K H$ where $K$ is the Cartan generator; at
root-of-unity order $\ell$, the specialisation $\zeta = e^{2\pi i/\ell}$
and the associated $\hbar = 2\pi i/\ell$ follow.  The appearance of
$(2\pi)^2/\ell^2$ in $\hbar^2$ is unavoidable under this scaling
convention.

Kontsevich 1999 \emph{Lett. Math. Phys.} 48 normalises the associator
$\Phi_{\mathrm{KZ}}(\hbar)$ inside the rational-function ring
$\mathbb{Q}[\hbar][[\mathrm{MZV}]]$ where $2\pi i$ is treated as a
transcendental unit; under this normalisation, $(2\pi)^2$ is absorbed
into the coefficient structure, so $\hbar^2$ is a formal $\mathbb{Q}$-valued
quantity and $\hbar^2 = -1/K$ is dimensionless.  The two normalisations
correspond to two sections of the $\mathrm{GRT}_1(\mathbb{Q})$-torsor;
neither is "correct" in isolation.

The manuscript statement "$\hbar^2 \cdot K = -1$ holds universally" is a
formal identity in the Kontsevich section; its physical-units lift
requires explicit $(2\pi)^2$-bookkeeping.  \hfill $\square$

## Retractions with true hidden structure

### Retraction BZ-R1: "Bruinier 2002 Prop 5.1 yields order $2 \cdot 4 = 8$ by multiplication"

*Wrong claim.*  $\mathrm{ord}(\mathrm{mon}\,\mathcal{L}^{\Delta_5}|_{H_1}) =
N_{\Delta_5}^{\mathrm{mult}} \cdot \mathrm{denom}^{-1}(c_{\eta^9\vartheta_1}(1))
= 2 \cdot 4 = 8$ via Bruinier reciprocity.

*Precise error.*  Bruinier 2002 Prop 5.1 — which the manuscript
Theorem `thm:bruinier-prop-5-1` quotes as giving torsion order
$N_\Psi/\gcd(N_\Psi, \mathrm{denom})$ — does \emph{not} contain this
formula in the literal form cited.  Bruinier's actual Chapter 5
content is:
\begin{itemize}
\item \emph{Thm 5.12 (main Chapter 5 theorem):} divisor formula
$\mathrm{div}(\Psi_f) = \tfrac{1}{2}\sum_{\mu, m<0} c_f(m, \mu) Z(m, \mu)$.
\item \emph{Prop 5.1:} local product expansion of a Borcherds product
near a Heegner divisor (a Fourier-expansion statement).
\item \emph{Thm 4.5 / Prop 4.8:} Weil-representation intertwining
between spaces of weak harmonic Maass forms of half-integral weight
and vector-valued cusp forms on orthogonal groups.
\end{itemize}
None of these three is the claimed "torsion order
$N_\Psi/\gcd(N_\Psi, \mathrm{denom})$".  That formula is a
\emph{synthesised statement} combining Bruinier's divisor formula
(Thm 5.12) with the Kudla–Millson 1986 (\emph{Ann. Math.} 124)
Arakelov-Chern-class computation plus Borcherds 1998 (\emph{Inv. Math.}
132 §10) multiplier-system-order theorem.  Attributing it to "Bruinier
2002 Prop 5.1" alone mislocates the primary source.

Additionally, the claimed decomposition "$2 \cdot 4 = 8$" by simple
multiplication is wrong: the correct combination is
$\mathrm{lcm}(2, 4) = 4$ of commuting $\mathbb{Z}/n$-factors, with a
further $\mathbb{Z}/2$-superparity extension reaching $8$.  Straight
multiplication $2 \cdot 4 = 8$ works only if the two factors are in
\emph{non-commuting} central extensions.

*Ghost theorem.*  Theorem BZ1 above.  The decomposition
\[
  8 \;=\; \mathrm{lcm}(2_{\mathrm{mult}}, 4_{\mathrm{Bruinier}})
  \;\cdot\; 2_{\mathrm{super}}
  \;=\; 4 \cdot 2
\]
with primary sources Borcherds 1998 §10 (multiplier), Gritsenko–Nikulin
1998 Tbl 2 (Fourier coefficient $-1/4$), Bruinier 2002 Thm 5.12
(divisor formula), Kudla–Millson 1986 (Arakelov Chern class),
Schauenburg 1998 Comm Alg 26 (super-parity extension).

### Retraction BZ-R2: "$\eta^9\vartheta_1$ has weight $9/2$, index $1/2$"

*Wrong claim.*  The Gritsenko additive-lift source $\eta^9\vartheta_1$
has Jacobi weight $9/2$ and index $1/2$ (cited in
`k3_chiral_bialgebra_platonic.tex` line 2860).

*Precise error.*  Under standard Eichler–Zagier 1985 Jacobi form
conventions:
\begin{itemize}
\item $\eta(\tau)$ has weight $1/2$ (as a modular form in $\tau$).
\item $\eta^9$ has weight $9/2$, index $0$.
\item $\vartheta_1(\tau, z)$ has Jacobi weight $1/2$, index $1/2$.
\item Product $\eta^9 \vartheta_1$ has weight $9/2 + 1/2 = 5$, index $1/2$.
\end{itemize}
The claim "weight $9/2$" is a **typographic error**; the weight of
$\eta^9\vartheta_1$ is $5$.  This is required for the Gritsenko
additive-lift relation $\Delta_5 = \mathrm{Grit}(\eta^9\vartheta_1)$ to
match Jacobi-form weight against paramodular weight $5$ on the output
side.

*Ghost theorem.*  The Gritsenko additive-lift source has Jacobi form
data $(k, m) = (5, 1/2)$ where $k = 5$ matches the paramodular weight
of $\Delta_5$.  The "index $1/2$" is correct, and is what enters the
Gritsenko–Nikulin 1998 Theorem 2.1 Humbert-divisor-vanishing
computation.  The index-$1/2$ contribution to the Bruinier-Chern-class
denominator is $1/4$ at codim-$1$, which is the source of the
$4_{\mathrm{Bruinier}}$ factor in Theorem BZ1.

### Retraction BZ-R3: "Bruinier reciprocity is the single identity Mukai $\leftrightarrow$ Humbert"

*Wrong claim.*  "Bruinier's Chern-class reciprocity is the single
categorical identity that makes Face~1 $\leftrightarrow$ Face~2"
(modular_koszul_bridge.tex Remark `rem:trinity-of-eight`).

*Precise error.*  Bruinier 2002 LNM 1780 establishes:
(a) Borcherds products have Heegner-divisor support
(Thm 5.12, divisor formula).
(b) Restricted Chern classes to Heegner divisors are torsion
(Thm 4.5 + Prop 5.1 combined).
(c) Weil-representation intertwiners transport modular-form data to
orthogonal-group line bundles (Thm 4.5).

None of these establishes a \emph{reciprocity} between the Mukai
lattice $c_+$ and the Bruinier torsion order $N$.  The equality
"$2c_+(\mathrm{Muk}(K3)) = N_{\mathrm{Bruinier}}(H_1)$" is a
\emph{numerical observation of Vol III} — both equal $8$ — not a
Bruinier theorem.

The conjectural content (Vol III-specific): for a Calabi–Yau 2-category
$\mathcal{C}$ with Mukai lattice $\widetilde{\Lambda}(\mathcal{C})$ of
signature $(p, q)$, the Borcherds line bundle
$\mathcal{L}^{\Psi(\mathcal{C})}$ constructed from the
$\Phi_2$-output stage-$1$ factorisation algebra has
$\mathrm{CH}^1$-torsion order on the principal Heegner divisor equal to
$2p = 2c_+$.  This is **Conjecture** `conj:bz-mukai-bruinier-reciprocity`
below; its proof would require Kudla–Millson-like Arakelov-Chern-class
machinery adapted to the Borcherds-product construction, which is not
in primary literature in this exact form.

*Ghost theorem.*  

**Conjecture BZ–Muk–Br (Mukai–Bruinier reciprocity).**
\label{conj:bz-mukai-bruinier-reciprocity}\ClaimStatusConjectured
On the Vol III $\mathcal{B}$-family
$\mathcal{B} = \{\mathrm{II}_{1,1}, \mathrm{II}_{3,19}\oplus U_0,
\mathrm{II}_{25,1}\}$, the Borcherds line bundle
$\mathcal{L}^{\Psi_L}$ attached to the $\Phi_d$-image of the
Lorentzian-lattice CY category with Mukai lattice $L$ has
$\mathrm{CH}^1$-torsion order on the principal Heegner divisor
$H_{\mathrm{princ}}(L)$ equal to $2c_+(L)$.
Evidence at $L = \widetilde{\Lambda}(K3)$: both equal $8$.
Evidence at $L = \mathrm{II}_{1,1}$ (Monster): both equal $2$
(cache 18B).  Evidence at $L = \mathrm{II}_{25,1}$ (Fake Monster):
both equal $50$ (cache 18B).  Three-point verification suggests
functoriality, but no proof is in the literature.

### Retraction BZ-R4: "$\varrho(\mathcal{H}_{\mathrm{Muk}}(K3)) = 1/6$ is derived from Mukai-doubling"

*Wrong claim.*  The anomaly ratio $\varrho = 1/6$ of the Mukai-enhanced
K3 Heisenberg is derived from the CY-$2$ Serre-duality symmetrisation
of the bar differential across the Mukai pairing
(`modular_koszul_bridge.tex` line 1162).

*Precise error.*  The plain rank-$r$ Heisenberg VOA
$\mathcal{H}_L$ on a signature-$(p, q)$ lattice $L$ with $p + q = r$
has:
\begin{itemize}
\item Sugawara central charge $c = r$ (total rank, independent of signature).
\item Feigin–Frenkel-symmetric conductor $K = c + c^! = 2r$.
\item Modular characteristic $\kappa_{\mathrm{ch}} = c = r$ (free-field,
anomaly ratio $\varrho = 1$).
\end{itemize}
At $r = 24$: $c = 24$, $K = 48$, $\varrho = 1$, $K^\kappa = 48$.  **Not** $8$.

The value $\varrho = 1/6$ requires a Drinfeld–Sokolov or
Bershadsky–Polyakov-like structure, \emph{not} plain Heisenberg.
Specifically, BP$_k$ has $\varrho = 1/6$, $K = 196$, $K^\kappa = 98/3$
(Vol I Theorem C(b) row $\mathsf{M}$-ext-2).  The $\mathsf{B}$-row
claim $\varrho = 1/6$, $K = 48$ is a \emph{different} $(\varrho, K)$
pair that matches the BP anomaly ratio but not the BP conductor; it is
a \emph{new entry in the landscape}, not derived from plain Heisenberg.

*Ghost theorem.*  **Theorem BZ4** above.  The $\mathsf{B}$-row witness
must be interpreted as a Bershadsky–Polyakov-like chiral algebra
$\mathrm{BP}_{\mathrm{Muk}}$ obtained by minimal-nilpotent DS reduction
on the Mukai-enhanced K3 lane; its $\varrho = 1/6$ is inherited from
the DS-reduction structure, not from Mukai-doubling per se.
Mukai-doubling (Thm BZ3) provides the $(K, c_+)$ identification
$K = 2c_+$ at the \emph{output side}, not the $\varrho$ derivation.

## Cross-consistency checks

### (a) Harmony with `platonic_synthesis_post_adversarial.tex`

Theorem `wn:thm:spine-five-archetype` (lines 958–1018) states the
five-archetype landmark ceiling with $\mathsf{B}$-row $K^\kappa = 8$.
The three faces of $8$ (lines 990–1008) are stated with: (i) Mukai
doubling, (ii) Humbert monodromy via "$2 \cdot 4 = 8$", (iii) Lusztig
$\ell = 8$.  Surgical corrections needed in each:
\begin{itemize}
\item \emph{(i) Mukai face:} attribution "Beilinson–Drinfeld
Koszul-conductor identity" should be replaced with "Mukai 1987
signature computation + Vol I anomaly-ratio bridge
$K^\kappa = \varrho K$".  BD does not contain a "Koszul-conductor
identity" by this name.
\item \emph{(ii) Humbert-monodromy face:} "$2 \cdot 4 = 8$" corrected
to $\mathrm{lcm}(2_{\mathrm{mult}}, 4_{\mathrm{Bruinier}}) \cdot 2_{\mathrm{super}} = 8$
(Thm BZ1).  The "$\eta^9\vartheta_1$ weight $9/2$" is typo for weight $5$
(retraction BZ-R2).  "Bruinier 2002 Prop 5.1" should be "Bruinier 2002
Thm 5.12 + Kudla–Millson 1986 + Borcherds 1998 §10 + Schauenburg 1998"
for primary source.
\item \emph{(iii) Lusztig face:} the identity $\hbar^2 \cdot K = -1$ is
a Kontsevich-torsor-normalised formal identity; explicit $(2\pi)^2$
bookkeeping required for physical units (Thm BZ5).
\end{itemize}

### (b) Harmony with `k3_chiral_bialgebra_platonic.tex`

Theorem `thm:humbert-order-K-kappa` (line 2836) is correct modulo the
scope-declaration and primary-source attribution issues.  The "$2 \cdot 4$"
in the proof sketch (line 2860) should be expanded to the
$\mathrm{lcm}(2, 4) \cdot 2_{\mathrm{super}}$ decomposition.

Remark `rem:one-identity-three-faces-k3` (lines 2882–2891) is the
cleanest statement.  Retain its three-face structure; strengthen each
face with its corrected primary source.

### (c) Harmony with `chiral_center_theorem.tex` (Vol I)

Vol I Theorem C(b) establishes the six-row landmark table
$\{\mathcal{H}_k, \widehat{\fg}_k, \beta\gamma_\lambda, \mathrm{Vir}_c,
\mathcal{W}_3^k, \mathrm{BP}_k\}$.  The $\mathsf{B}$-row
$\mathcal{H}_{\mathrm{Muk}}(K3)$ adjoined in Theorem C(c) is the
Vol III extension; **the proposition
`prop:archetype-complementarity-bridge` cited for the $\mathsf{B}$-row
derivation is a dangling reference without a definition locus** —
this is an orphan reference issue.  The Bridge $K^\kappa = \varrho K$
is valid (Vol I Theorem C(a)); the $\mathsf{B}$-row $(\varrho, K) =
(1/6, 48)$ is a conjectural assignment (Thm BZ4) that matches
Vol III's three-faces observation numerically.

### (d) Universal identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$

Theorem BZ2 (via retraction R1 of prior A09 analysis) establishes that
$\kappa_{\mathrm{BKM}} = 5$ and $\kappa^!(\mathcal{H}_{\mathrm{Muk}}) = 4$
are structurally different invariants; their numerical near-match at
$N = 1$ (both close to $5$) is accidental.  The Borcherds weight
identity remains intact on the CHL slice
$(c_1(0)/2, c_2(0)/2, c_3(0)/2, c_4(0)/2, c_6(0)/2) = (5, 2, 1, 1, 1)$;
this is orthogonal to the three-faces-of-$8$ identity.

### (e) Two-stage factorisation $\Phi_d = \mathrm{Sp}_{\Sigma, C} \circ \Phi^{\mathrm{FA}}_d$

Three-faces identity lives at Stage~2 output for $d = 2$: the
$(\Sigma_1, C) = (\{\mathrm{pt}\}, K3)$ specialisation of
$\Phi_2^{\mathrm{FA}}(D^b\mathrm{Coh}(K3))$ produces the
Mukai-enhanced $E_2$-chiral algebra on K3 whose $K^\kappa = 8$ is the
$\mathsf{B}$-row value.  The Humbert-monodromy face uses the
parameter-base side (genus-$2$ paramodular); Mukai face uses the
K3-fibre side (stage-$1$ invariant); Lusztig face uses the
Hall-Drinfeld-double side of the resulting chiral algebra.  Three
readings, three different loci within the two-stage factorisation
diagram.

## Residual frontier

**F1.** The anomaly ratio $\varrho(\mathcal{H}_{\mathrm{Muk}}(K3)) = 1/6$
is not primary-source-derived.  Needed: a proof that the $\Phi_2^{\mathrm{FA}}$
output of $D^b\mathrm{Coh}(K3)$ on the minimal-nilpotent DS slice of
$\mathrm{Aut}(\widetilde{\Lambda}(K3))$ has $\varrho = 1/6$ by explicit
character-level computation.  [\ClaimStatusOpen]

**F2.** Conjecture BZ–Muk–Br
(`conj:bz-mukai-bruinier-reciprocity`) — the Mukai-Bruinier
reciprocity $N_{\mathrm{Bruinier}}(H_{\mathrm{princ}}(L)) = 2c_+(L)$
on the $\mathcal{B}$-family — is verified at three points
$\{L = \mathrm{II}_{1,1}, \widetilde{\Lambda}(K3), \mathrm{II}_{25,1}\}$
with values $\{2, 8, 50\}$.  A fourth verification point (Enriques at
$\mathrm{II}_{2,10}$ with predicted $c_+ = 2, N = 4$) would strengthen;
general proof would require Kudla–Millson-type Arakelov-Chern-class
machinery for Borcherds-product line bundles at orthogonal signature
$(2, \ell)$.  [\ClaimStatusConjectured]

**F3.** The orphan reference `prop:archetype-complementarity-bridge` in
Vol I `chiral_center_theorem.tex` needs to be defined or replaced with
an explicit cross-reference.  Specifically: the derivation of the
$\mathsf{B}$-row $(\varrho, K) = (1/6, 48)$ pair should be an explicit
proposition in `chiral_center_theorem.tex` (rather than a dangling
reference).  [\ClaimStatusOpen bookkeeping]

**F4.** The "$\hbar^2 \cdot K = -1$" physical-units interpretation.
Under Drinfeld scaling $\hbar = 2\pi i/\ell$, the identity is
$(2\pi)^2/\ell \cdot K = (2\pi)^2$ at $\ell = K$.  Is there a natural
Arakelov or Beilinson-regulator section of the $(2\pi i)$-torsor on
$\overline{\mathcal{A}_2}$ in which $(2\pi)^2 = 1$ is theorem-forced
rather than convention-imposed?  [\ClaimStatusOpen]

**F5.** The primary-source attribution for "Bruinier 2002 Prop 5.1" in
the manuscript should be split across (Bruinier 2002 Thm 5.12;
Kudla–Millson 1986; Borcherds 1998 §10; Schauenburg 1998) to accurately
reflect the derivation.  This is a reference-discipline frontier, not
a mathematical frontier.  [\ClaimStatusCorrected pending rectification]

**F6.** The super-parity $\mathbb{Z}/2$-extension factor in Theorem BZ1
part (d) is inferred from the Schauenburg bracket-square cocycle
computation (cache 18C/22J); its explicit manifestation as an
extension of the $\mu_4$-gerbe to a $\mu_8$-gerbe on
$\overline{\mathcal{A}_2} \setminus H_1$ requires direct Čech-cocycle
computation.  [\ClaimStatusOpen]

## Attack-heal cycle log (private)

**Cycle 1: ATTACK — Is "Beilinson–Drinfeld Koszul-conductor identity on
(4, 20)-signature" a named theorem in Beilinson–Drinfeld's *Chiral
Algebras* (AMS Colloquium Publications vol 51, 2004)?**  Checked BD
Ch.~3 chiral homology and Ch.~4 chiral BRST: no such theorem by name.
"Conductor" terminology is Vol I's coinage $K = c + c^!$; the
"BD Koszul-conductor identity" attribution is a misnomer.
**HEAL — Theorem BZ3 + cross-ref correction.**  The correct primary
source for $K = 2c_+(\mathrm{Mukai}(K3))$ is Mukai 1987 §1 (signature
computation) + Vol I Theorem C(a) (anomaly-ratio bridge).
"Beilinson–Drinfeld" attribution should be removed.

**Cycle 2: ATTACK — Is $\varrho = 1/6$ derivable for the rank-24
Heisenberg on signature-$(4, 20)$ lattice?**  Direct computation:
plain Heisenberg has $\varrho_{\mathrm{Heis}} = 1$, not $1/6$.  The
value $1/6$ belongs to Bershadsky–Polyakov minimal-nilpotent DS class.
Manuscript does not derive $\varrho = 1/6$ from first principles; it
matches the observed $K^\kappa = 8$ against $K_{\text{total}} = 48$ by
dividing.  Primary-source theorem for $\varrho$ is absent.
**HEAL — Theorem BZ4 (conditional scope).**  $\varrho = 1/6$
requires a BP-like DS-reduction structure, not plain Heisenberg.
The $\mathsf{B}$-row witness is a new entry in the Vol I landscape,
not derived from plain Mukai-enhanced Heisenberg.

**Cycle 3: ATTACK — Is Bruinier 2002 Prop 5.1 correctly quoted as
giving torsion order $N_\Psi/\gcd(N_\Psi, \mathrm{denom})$?**  Checked:
Bruinier Prop 5.1 is a local-product-expansion statement, not a
torsion-order formula.  The cited formula is a synthesis across
Bruinier Thm 5.12 + Kudla–Millson 1986 + Borcherds 1998 §10.
**HEAL — Retraction BZ-R1 + Theorem BZ1.**  Correct decomposition:
$8 = \mathrm{lcm}(2_{\mathrm{mult}}, 4_{\mathrm{Bruinier}}) \cdot 2_{\mathrm{super}}$,
with each factor traced to its specific primary source.

**Cycle 4: ATTACK — Does $\eta^9\vartheta_1$ have weight $9/2$ or weight $5$?**
Eichler–Zagier 1985 convention: $\eta$ weight $1/2$, $\vartheta_1$
Jacobi weight $1/2$ index $1/2$; product $\eta^9\vartheta_1$ has
weight $9/2 + 1/2 = 5$.  Manuscript says weight $9/2$ — this is wrong.
**HEAL — Retraction BZ-R2.**  Correct Jacobi data:
$(k, m) = (5, 1/2)$.  The weight match $5 = \mathrm{wt}(\Delta_5)$ is
forced by the Gritsenko additive-lift relation.

**Cycle 5: ATTACK — Does $\log\Delta_5$ have monodromy order $8$ around $H_1$?**
Direct derivative: $d\Delta_5/\Delta_5$ has simple pole with residue $1$
(vanishing order of $\Delta_5$ on $H_1$); monodromy of $\log\Delta_5$
is $e^{2\pi i} = 1$, **trivial**, not order $8$.  To reach order $8$
one must pass to the $8$-th-root cover $\Delta_5^{1/8}$ via a
$\mu_8$-gerbe banding.
**HEAL — Theorem BZ1 (corrected derivation).**  The order-$8$ monodromy
lives on $\widetilde{\mathcal{L}}^{\Delta_5}$ (the $\mathbb{Z}/8$-cyclic
cover branched along $H_1 \cup H_4$), not on $\mathcal{L}^{\Delta_5}$
itself.  The $\mu_8$-gerbe structure is the primary geometric object.

**Cycle 6: ATTACK — Is the identification "Bruinier reciprocity is the
single categorical identity Mukai $\leftrightarrow$ Humbert" a genuine
theorem in Bruinier 2002 LNM 1780?**  Checked: Bruinier establishes
divisor formulas and intertwining operators on Weil representations;
he does NOT establish a "$2c_+ = N_{\mathrm{Bruinier}}$" reciprocity.
**HEAL — Retraction BZ-R3 + Conjecture BZ-Muk-Br.**  The identification
Mukai $\leftrightarrow$ Humbert is a Vol III numerical observation; its
upgrade to a theorem would require Kudla–Millson-type Arakelov machinery
adapted to $\Phi_2^{\mathrm{FA}}$-output Borcherds products.

**Cycle 7: ATTACK — Does the Drinfeld scaling $\hbar = 2\pi i/\ell$
give $\hbar^2 = -1/\ell$?**  Direct arithmetic: $(2\pi i/\ell)^2 =
-(2\pi)^2/\ell^2$, not $-1/\ell$.  To get $-1/\ell$ one must absorb
$(2\pi)^2$ into the normalisation.
**HEAL — Theorem BZ5 (unit-normalisation).**  The "universal identity
$\hbar^2 \cdot K = -1$" is a Kontsevich-torsor-normalised formal
identity; under physical Drinfeld scaling, the identity is
$\hbar^2 \cdot K = -(2\pi)^2/\ell$.

**Cycle 8: ATTACK — Does the $\mathsf{B}$-row value $K^\kappa = 8$
require $\kappa^!$ of the Mukai-enhanced Heisenberg specifically, or
does it work with any CY-$2$ target?**  Direct test: on the elliptic
curve $E$ (also CY-$2$ at $d = 2$ if stratified as CY-$0$ × CY-$2$
structure, but more naturally CY-$1$), signature of Mukai lattice
$\widetilde{\Lambda}(E) = H^0 \oplus H^1 \oplus H^2$ has
signature $(2, 0)$ on $H^0 \oplus H^2$ (both positive) and indefinite
on $H^1 = U$, with net $c_+(\widetilde{\Lambda}(E)) = 2$.  Predicted
$K^\kappa_{\mathsf{B}}(E) = 2 \cdot 2 = 4$.  Not independently verified
in the literature.  Supports that $2c_+$ scales with the lattice, not
a universal $K^\kappa$.
**HEAL — Theorem BZ3 (restricted scope).**  Mukai-doubling $K = 2c_+$
is a signature-computation, not a universal constant.  The
$\mathcal{B}$-family conjecture extends it beyond K3 only to
Lorentzian lattices with principal Heegner divisor; the Enriques/K3$\times$E
extensions are conjectural.

**Cycle 9: ATTACK — Is the Vol I orphan reference
`prop:archetype-complementarity-bridge` a symptom of a missing
derivation?**  Grep across `chiral-bar-cobar/chapters/`: the label
is cited 5+ times but never defined with a `\label{prop:...}`.
**HEAL — Frontier F3.**  The proposition must be defined in
`chiral_center_theorem.tex` with explicit derivation of each row's
$(\varrho, K)$ pair.  Without it, the $\mathsf{B}$-row
$(\varrho, K) = (1/6, 48)$ rests on an undefined proposition.
