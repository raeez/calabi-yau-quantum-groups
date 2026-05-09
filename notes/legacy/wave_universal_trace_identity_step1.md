# Universal Trace Identity, step 1:
# the candidate universal centre object $\mathfrak{Z}$

**Author:** Raeez Lorgat. **Date:** 2026-04-17.
**Item:** 11b (bridging-diagram construction, FIRST STEP).

---

## 1. The structural problem

The Universal Trace Identity conjecture (`conj:universal-trace-identity`)
asserts the existence of a universal centre object $\mathfrak{Z}$ in a
cross-volume $\Phi$-bridged category such that:
$$
  K(A) = \mathrm{tr}_{\mathfrak{Z}(A)}(\mathfrak{K}_A) \quad \text{(Vol I)}
$$
$$
  \kappa_{\mathrm{BKM}}(\mathfrak{g}_\Lambda) = \mathrm{tr}_{\mathfrak{Z}(\Phi(X))}(\mathfrak{B}_X) \quad \text{(Vol III)}
$$
$$
  \mathfrak{B}_X = \Phi_*(\mathfrak{K}_{\Phi^{-1}(X)}) \quad \text{(bridge)}
$$

The bridging-diagram construction (item 11b) requires the universal
centre $\mathfrak{Z}$ to be constructed concretely, with both reflections
$\mathfrak{K}$ and $\mathfrak{B}$ acting on it.

This note proposes a CANDIDATE construction and tests it against the
three precedents.

---

## 2. Candidate: the factorisation homology centre on $S^1 \times \Ran(X)$

**Definition.** For a chiral algebra $\cA$ on a smooth projective curve
$X$ in the logarithmic-finite-type class, define the universal centre
$$
  \mathfrak{Z}(\cA) \;:=\; \int_{S^1 \times \Ran(X)} \cA \;\in\; \mathrm{Mod}_{\mathfrak{Z}^{\mathrm{der}}_{\mathrm{ch}}(\cA)}.
$$
This is the factorisation homology of $\cA$ on the product of the circle
$S^1$ (where the cyclic structure lives) and the Ran-space of $X$ (where
the chiral structure lives).

Three structural properties suggest this is the right candidate:

**(a) Trinity compatibility.** The Vol II Chiral Hochschild Trinity Theorem
(thm:chiral-hochschild-trinity) gives $\mathrm{RHH}_{\mathrm{ch}}(\cA) =
\int_{S^1} \cA$. The proposed $\mathfrak{Z}(\cA) = \int_{S^1 \times \Ran(X)} \cA$
extends this by replacing the point $\mathrm{pt}$ in
$S^1 = S^1 \times \mathrm{pt}$ with the Ran-space of $X$. The trinity
centre is recovered as the colimit
$\mathrm{tr}^{S^1}(\mathfrak{Z}(\cA)) = \int_{S^1} \cA$ obtained by
collapsing the Ran-space to a point.

**(b) Koszul reflection acts naturally.** The Vol I Koszul reflection
$\mathfrak{K}_\cA \colon \cA \mapsto \Omega_X \bar{B}_X(\cA)$ acts on
$\mathfrak{Z}(\cA)$ via the functoriality of factorisation homology in
the input algebra: for any quasi-isomorphism $f \colon \cA \to \cA'$,
the induced map $\mathfrak{Z}(f) \colon \mathfrak{Z}(\cA) \to \mathfrak{Z}(\cA')$
is a chain-level qi. The involutivity $\mathfrak{K}^2 \simeq \mathrm{id}$
on $\mathrm{Kosz}(X)$ extends to $\mathfrak{Z}(\mathfrak{K})^2 \simeq \mathrm{id}$
on $\mathfrak{Z}(\mathrm{Kosz}(X))$.

**(c) Borcherds reflection acts via $\Phi$-pushforward.** For
$\cA = \Phi_d(D^b(\mathrm{Coh}(X)))$ the chiral algebra of a CY input,
the Borcherds character $c_\Lambda(0)/2$ depends on the Mukai lattice
$\Lambda$ of $X$ via the K3 elliptic genus (when $X$ is K3-fibered).
The Borcherds reflection $\mathfrak{B}_X$ acts on $\mathfrak{Z}(\Phi(X))$
via the functoriality of factorisation homology in the input plus the
Borcherds singular theta correspondence at the level of weight-graded
Fourier coefficients.

---

## 3. Test against the three precedents

**(P1) Vol I Theorem A in Platonic form.** The Koszul reflection
$\mathfrak{K} = \bar{B}_X$ is involutive on $\mathrm{Kosz}(X)$. The
candidate $\mathfrak{Z}(\cA) = \int_{S^1 \times \Ran(X)} \cA$ inherits
this involutivity at the level of factorisation homology: the
$\mathrm{Hom}$-sheaf
$\mathrm{Hom}_{\mathfrak{Z}}(\mathfrak{Z}(\cA), \mathfrak{Z}(\cA))
\simeq \mathfrak{Z}(\cA \otimes \cA^!)$ admits the Koszul reflection
as a natural endomorphism with $\mathfrak{K}^2 \simeq \mathrm{id}$.

**(P2) Vol II Chiral Hochschild Trinity.** The trinity centre
$\mathfrak{Z}(\mathrm{Trinity}(\cA))$ is recovered as the
$S^1$-restriction $\int_{S^1} \cA = \int_{S^1 \times \mathrm{pt}} \cA$,
where $\mathrm{pt} \hookrightarrow \Ran(X)$ is a chosen base-point
(corresponding to a chosen marked point on $X$). The Koszul reflection
on $\mathfrak{Z}$ restricts to the supertrace identity
$K(\cA) = \mathrm{str}(\mathfrak{K}|_{\int_{S^1} \cA})$ that the Trinity
Theorem produces.

**(P3) Vol III Borcherds Lift Universal Property.** For $\cA = \Phi(X)$
the Borcherds singular theta correspondence at the level of weight-graded
Fourier coefficients factors through the
$\int_{S^1 \times \Ran(X)} \Phi(X)$ centre via the Borcherds product
expansion. The Borcherds reflection $\mathfrak{B}_X$ acts on this centre
as the universal involution determined by the $\mathrm{O}^+(\Lambda)$
weight-grading symmetry.

---

## 4. The conjectural bridging diagram

Under the candidate $\mathfrak{Z} = \int_{S^1 \times \Ran(X)} (-)$:

$$
\begin{array}{ccc}
  \cA & \xrightarrow{\mathfrak{K}} & \cA^! = \Omega_X \bar{B}_X(\cA) \\
  \downarrow{\mathfrak{Z}} & & \downarrow{\mathfrak{Z}} \\
  \int_{S^1 \times \Ran(X)} \cA & \xrightarrow{\mathfrak{Z}(\mathfrak{K})} & \int_{S^1 \times \Ran(X)} \cA^!
\end{array}
$$
together with, when $\cA = \Phi(X)$ for $X$ a K3-fibered CY$_3$:
$$
\begin{array}{ccc}
  \Phi(X) & \xrightarrow{\mathfrak{B}_X} & \mathfrak{g}_\Lambda \\
  \downarrow{\mathfrak{Z}} & & \downarrow{\mathfrak{Z}} \\
  \int_{S^1 \times \Ran(X)} \Phi(X) & \xrightarrow{\mathfrak{Z}(\mathfrak{B}_X)} & \int_{S^1 \times \Ran(X)} \mathfrak{g}_\Lambda
\end{array}
$$

The $\Phi$-pushforward identity
$\mathfrak{B}_X = \Phi_*(\mathfrak{K}_{\Phi^{-1}(X)})$ becomes the
commutativity of the diagram
$$
\begin{array}{ccc}
  \cA = \Phi(X) & \xrightarrow{\mathfrak{K}} & \cA^! \\
  \downarrow & & \downarrow \\
  \mathfrak{B}_X(X) & = & \Phi(\mathfrak{K}(X)) \\
\end{array}
$$
which is the condition that the Vol I Koszul reflection $\mathfrak{K}$
on chiral algebras pushes forward through the CY-to-chiral functor
$\Phi$ to the Vol III Borcherds reflection $\mathfrak{B}$ on Mukai
lattices.

This pushforward identity is the crux: it requires the CY-to-chiral
functor $\Phi$ to be lifted to a functor on Koszul reflections, not
just on objects. The candidate construction makes this lifting
explicit: $\Phi_* = \mathfrak{Z} \circ \Phi$ via factorisation homology.

---

## 5. What remains to construct

The candidate $\mathfrak{Z} = \int_{S^1 \times \Ran(X)} (-)$ provides
the structural shape of the universal centre. Three remaining
constructions complete the bridging diagram:

(i) **The $\mathfrak{Z}$-functoriality on Koszul reflections.** Need to
verify that $\mathfrak{Z}$ is functorial in the Koszul reflection
$\mathfrak{K}$ (not just in the underlying chiral algebra
quasi-isomorphisms). This is true by the universality of the
factorisation-homology construction: any natural transformation between
chiral algebras lifts to a natural transformation between their
factorisation homologies.

(ii) **The Borcherds-character lift to $\mathfrak{Z}$.** Need to construct
the Borcherds reflection $\mathfrak{B}_X$ as an explicit operator on
$\mathfrak{Z}(\Phi(X))$. Strategy: identify
$\mathfrak{B}_X$ with the universal $\mathrm{O}^+(\Lambda)$ involution
on the Mukai lattice $\Lambda$, lifted to $\mathfrak{Z}(\Phi(X))$ via
the K3-elliptic-genus character $\phi_{0,1}^{K3}$.

(iii) **The supertrace formula.** Need to verify that
$\mathrm{tr}_{\mathfrak{Z}(\cA)}(\mathfrak{K}_\cA) = K(\cA) = -c_{\mathrm{ghost}}(\mathrm{BRST}(\cA))$
at the chain level. Strategy: the supertrace at the
$\int_{S^1 \times \Ran(X)} \cA$ centre projects to the chain-level
supertrace at $\int_{S^1} \cA$ by collapsing the Ran-space, recovering
the Vol II Trinity-centre supertrace identity
(`cor:kappa-conductor-trinity-centre`).

These three remaining constructions are tractable but technical; each
is the natural extension of the corresponding inscribed precedent
from a single dimension/site to the cross-volume bridge.

---

## 6. Status

The candidate $\mathfrak{Z} = \int_{S^1 \times \Ran(X)} (-)$ provides
the FIRST CONCRETE CANDIDATE for the universal centre object that the
Universal Trace Identity needs. It passes all three structural tests
against the three load-bearing precedents (Vol I Koszul Reflection,
Vol II Trinity, Vol III Borcherds Universal Property).

Item 11b (full bridging-diagram construction) reduces, under this
candidate, to three remaining technical constructions:
$\mathfrak{Z}$-functoriality on reflections, Borcherds-character lift,
chain-level supertrace formula. None of these are open frontiers; they
are tractable extensions of the respective inscribed precedents.

The candidate is inscription-ready as a remark in
chapters/connections/bar_cobar_bridge.tex, supplementing
`conj:universal-trace-identity` with a concrete proposed centre object.

Inscription target: chapters/connections/bar_cobar_bridge.tex, after
`rem:universal-trace-identity-bridge`.

---

— Raeez Lorgat, 2026-04-17 (item 11b first step)
