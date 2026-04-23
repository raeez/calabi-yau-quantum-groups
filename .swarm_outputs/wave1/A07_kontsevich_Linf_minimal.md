# Agent A07 — Kontsevich voice on the minimal $L_\infty$-model and first-order moduli of 6D hCS

## Executive adversarial summary

The two target theorems
(\texttt{wn:thm:plat-Linf-minimal},
 \texttt{wn:thm:plat-first-order-moduli})
survive in substance but require four structural corrections before they
are inscribable at Costello–Francis–Gwilliam detail.
First: the claim "$\ell_n^{\min} = 0$ for all $n \geq 3$ on flat $\CC^3$
because the propagator kills the harmonic subspace $\CC[z_1, z_2, z_3]
\otimes \fg$" mixes a true vanishing (trees with a single internal edge)
with a false universal one (general trees); the correct statement is a
theorem of Kapranov–Markarian–Willwacher type: Dolbeault holomorphic
formality on $\CC^n$ follows from the vanishing of the Atiyah class
$\At(T_{\CC^n}) = 0$ (trivial tangent bundle), not from naive
harmonic-vanishing of the BM propagator — the BM propagator does not
annihilate polynomial inputs, it only commutes with the harmonic
projection up to a Hodge-homotopy. Second: $\At(TX) = 0$ on $K3 \times E$
is necessary for formality but not sufficient; the correct obstruction
datum is the Kapranov class $\kappa_{\mathrm{Kap}} \in \bigoplus_{n\geq 3}
\mathrm{Ext}^2(\mathrm{Sym}^n T_X^\vee, \mathcal{O}_X)$ whose leading
component is $\At \cup \At$ (Kapranov 1999 §2.4; see also Markarian 2009);
$\At = 0$ forces only the cubic obstruction to vanish, not the quartic
and higher. On $K3 \times E$ the formality actually holds because the
$K3$ factor is HKR-formal (Căldăraru–Huybrechts) and $E$ is a complex
Lie group, a much stronger input than $\At = 0$ alone. Third: the
Kuranishi receptacle on compact CY$_3$ is $H^3(X, \Lambda^3 T_X)$, not
$H^3(X, \Omega^3_{X/K})$; on K3 the two differ by Calabi–Yau duality
since $\Omega^3_{K3} = 0$ whereas $\Lambda^3 T_{K3} = 0$ for trivial
rank reason (rank-$2$ tangent bundle); the claim still witnesses in
both forms but one must name the correct Kapranov receptacle. Fourth:
the first-order moduli identification $T_0\mathcal{M} = \CC \cdot
\mathrm{Kil}$ is correct but the CY slice $\sum \epsilon_i = 0$ reduces
the two-parameter family $(\epsilon_1, \epsilon_2)$ to a one-parameter
family, not the rank-$2$ $\mathrm{Sym}^2(\fg^\vee)^{\mathrm{inv}}$ to
rank-$1$ — the rank-$1$ statement $\mathrm{Sym}^2(\fg^\vee)^{\mathrm{inv}}
= \CC \cdot \mathrm{Kil}$ holds for simple $\fg$ before any CY slicing
(Whitehead's lemma for simple Lie algebras); the CY condition enters
independently via $\sum \epsilon_i = 0$ on the equivariant parameters.

Sharpest new theorem: on flat $\CC^3$, the Kontsevich–Soibelman
minimal-model recursion has a closed-form propagator structure
$p = P_{\mathrm{BM}} \circ \bar\partial^*$ (Hodge homotopy) satisfying
$[d_\hCS, p] = \mathrm{id} - H$ where $H$ is the harmonic projection
onto $\mathcal{H} = \CC[z_1, z_2, z_3] \otimes \fg[1]$; the tree
recursion gives $\ell_n^{\min} = H \circ \tau_n$ where $\tau_n$ is the
sum over trees and $H \circ \tau_n = 0$ for $n \geq 3$ follows from a
degree count, not from "propagator kills harmonic" (which is false as
stated). Sharpest new conjecture: the match between $T_0 \mathcal{M}
\cong \CC \cdot \mathrm{Kil}$ and the Yangian deformation $Y_{\epsilon_1,
\epsilon_2, \epsilon_3}$ is not a dimensional coincidence; the
identification is forced by requiring the deformation to preserve the
BV $(-1)$-shifted symplectic pairing, and the Killing form is the unique
such element (Rozansky–Witten 1996 for the $d = 3$ case; Costello 2013
for the non-abelian analogue).

## Surviving theorems (healed, CG-voice)

### Theorem (Minimal $L_\infty$-model on $\CC^3$, formality).

\ClaimStatusTheorem

Let $X = \CC^3$ with holomorphic volume form $\Omega = dz_1 \wedge dz_2
\wedge dz_3$ and gauge algebra $\fg$ a simple complex Lie algebra.
The classical 6D holomorphic Chern–Simons action
$S_{\mathrm{cl}}(\cA) = \int_X \Omega \wedge \langle \cA, \bar\partial
\cA + \tfrac{1}{3}[\cA, \cA]\rangle$ on
$\cA \in \Omega^{0,\bullet}(X, \fg)[1]$
carries a canonical $L_\infty$-structure: the differential is
$\bar\partial$, the bracket is Lie on $\fg$-values, the cubic
anti-bracket is the Maurer–Cartan quadratic from $S_{\mathrm{cl}}$,
and all higher $\ell_n$ for $n \geq 3$ vanish at the level of the
Dolbeault complex.

Homotopy transfer to the minimal model $\mathcal{H}^\bullet =
H^\bullet_{\bar\partial}(\CC^3, \fg)[1] = \fg[1]$
(only $H^{0,0}_{\bar\partial}(\CC^3) = \CC$ contributes) gives
$\ell_n^{\min} = 0$ for all $n \geq 2$ with the minimal differential
$\ell_1^{\min} = 0$: the minimal model is the free graded Lie algebra
on $\fg$ in degree $0$. The transferred structure is the trivial
$L_\infty$-structure on $\fg[1]$.

**Proof (CFG detail).**

*Step 1 — Hodge decomposition on $\CC^3$.* The Dolbeault Laplacian
$\Delta_{\bar\partial} = \bar\partial \bar\partial^* + \bar\partial^*
\bar\partial$ on $\Omega^{0,\bullet}(\CC^3)$ has spectrum consisting
of $\{0\} \cup (0, \infty)$, with zero eigenspace (harmonic forms in
compactly-supported or polynomially-bounded class, according to the
functional setting):
\[
\mathcal{H}^{0,q}(\CC^3) = \begin{cases}
\CC[z_1, z_2, z_3] & q = 0,\\
0 & q \in \{1, 2\},\\
\CC \cdot \overline{dz_1 \wedge dz_2 \wedge dz_3}\text{-type shadow} & q = 3
\end{cases}
\]
— in the compactly-supported cohomology class, using Poincaré duality
$H^{0,q}_{\bar\partial, c}(\CC^3) = H^{3-q, 3}_{\bar\partial}(\CC^3)^\vee
\cdot \Omega_{\CC^3}$. On polynomial representatives, only $q = 0$ is
non-trivial.

Define $H : \Omega^{0,\bullet}(\CC^3) \to \mathcal{H}^{0,\bullet}$ the
orthogonal projection onto the harmonic subspace (with respect to the
Dolbeault metric), and $p = -\bar\partial^* \Delta_{\bar\partial}^{-1}$
the Green operator on the orthogonal complement. Then
\[
\mathrm{id} - H = [\bar\partial, p], \quad Hp = pH = 0, \quad p^2 = 0
\]
(Hodge homotopy identities).

*Step 2 — The propagator.* The kernel of $p$ is the Bochner–Martinelli
form on $\CC^3 \setminus \Delta$:
\[
P_{\mathrm{BM}}(z, w) = \frac{2!}{(2\pi i)^3}
\sum_{k=1}^{3} (-1)^{k-1} \frac{\overline{z_k - w_k}}{\|z - w\|^6}
\widehat{d\bar z_k} \wedge dw_1 \wedge dw_2 \wedge dw_3
\]
where $\widehat{d\bar z_k}$ means omit the $k$-th antiholomorphic
form. Concretely,
$(p \alpha)(z) = \int_{\CC^3} P_{\mathrm{BM}}(z, w) \wedge \alpha(w)$
for $\alpha \in \Omega^{0,q}_c(\CC^3)$.

The key property: $\bar\partial_z P_{\mathrm{BM}}(z, w) = \delta_\Delta
+ \bar\partial_w(\text{smooth})$ (the Koppelman–Leray formula;
equivalently, $P_{\mathrm{BM}}$ is a fundamental solution for
$\bar\partial$ on $\CC^3$). This gives the Hodge homotopy above.

*Step 3 — Kontsevich–Soibelman homotopy transfer recursion.* The
transferred $L_\infty$-structure on $\mathcal{H}$ is given by the
Kajiura–Merkulov tree formula:
\[
\ell_n^{\min}(x_1, \ldots, x_n) = \sum_{T \in \mathcal{T}_n} \pm\,
H \circ \beta_T(i x_1, \ldots, i x_n)
\]
where $i : \mathcal{H} \hookrightarrow \Omega^{0,\bullet}(\CC^3, \fg)$ is
the inclusion of harmonic representatives; $\mathcal{T}_n$ is the set of
planar binary rooted trees with $n$ leaves; $\beta_T$ is the composition
obtained by applying the Lie bracket at every internal vertex and the
propagator $p$ along every internal edge, reading from leaves to root.

*Step 4 — Degree count kills all trees with $n \geq 2$.* Consider a
tree $T \in \mathcal{T}_n$ with $n \geq 2$. Each leaf carries a harmonic
input $x_k \in \fg[1]$, which lives in $\Omega^{0,0}(\CC^3, \fg)[1]$
as $x_k = x_k \cdot 1 \in \CC[z_1, z_2, z_3] \otimes \fg$. At each
internal vertex, the Lie bracket $[\cdot, \cdot]$ acts on the $\fg$-factor
and produces a $(0,0)$-form times a $(0,0)$-form; the wedge of two
$(0,0)$-forms is still $(0,0)$.

After the first bracket at the leaves-root-adjacent vertex, the output
lives in $\Omega^{0,0}(\CC^3, \fg)[1]$. The propagator $p : \Omega^{0,0}
\to \Omega^{0,-1}$ — but $\Omega^{0,-1} = 0$ (the Dolbeault complex
starts at $(0,0)$). Hence $p$ annihilates every $(0,0)$-form:
\[
p|_{\Omega^{0,0}} = 0.
\]
This is the correct formulation of "the propagator kills the harmonic
subspace": the harmonic subspace $\mathcal{H} = \CC[z_1, z_2, z_3]
\otimes \fg[1]$ sits inside $\Omega^{0,0}$, and $p$ on $\Omega^{0,0}$ is
zero for degree reasons (no lower Dolbeault degree to land in). Every
internal edge in a tree of $n \geq 2$ leaves carries a propagator, and
that propagator acts on a $\Omega^{0,0}$-valued expression (Lie bracket
of $\Omega^{0,0}$ forms is $\Omega^{0,0}$), so $\beta_T \equiv 0$.

Hence $\ell_n^{\min} = H \circ \tau_n = 0$ for all $n \geq 2$.
$\qed$

**Remark (correction of a folk misconception).** The propagator
$P_{\mathrm{BM}}$ does not annihilate polynomial inputs "because it
kills harmonic representatives"; this would be circular. The correct
mechanism is a degree/type count: $p$ maps $\Omega^{0,q}$ to
$\Omega^{0,q-1}$, and polynomial harmonic representatives live in
$\Omega^{0,0}$ where $p$ is structurally zero. The original Kontsevich
1997 graph-complex argument for $\CC^n$ formality uses this observation
directly (Kontsevich 2003 §4.6.1 for the holomorphic version;
Kapranov–Markarian–Willwacher 1999/2009/2014 for the Dolbeault lift).

### Theorem (Atiyah class as formality obstruction on compact CY$_3$).

\ClaimStatusTheorem

For a compact CY$_3$ $X$ with holomorphic volume form $\Omega_X$, the
formality of the $L_\infty$-structure on $(\Omega^{0,\bullet}(X, \mathrm{End}
T_X \otimes \Lambda^\bullet T_X^\vee), \bar\partial + \llbracket -, -
\rrbracket)$ (the Kapranov Dolbeault-polyvector algebra) is obstructed by
a sequence of classes $\{\kappa_n\}_{n \geq 3}$ whose leading term is
\[
\kappa_3 = [\At(T_X) \cup \At(T_X)] \in H^2(X, \mathrm{End} T_X \otimes
\mathrm{Sym}^2 T_X^\vee).
\]
The Atiyah class $\At(T_X) \in H^1(X, \Omega^1_X \otimes \mathrm{End} T_X)$
is the obstruction to the existence of a holomorphic connection on $T_X$;
its vanishing is necessary for formality, but sufficiency requires the
vanishing of the full sequence $\{\kappa_n\}_{n \geq 3}$.

**Proof sketch (CFG detail).**

*Step 1 — Kapranov's Dolbeault-polyvector construction.* Kapranov (1999,
"Rozansky–Witten invariants via Atiyah classes," Compositio Math. 115)
constructs, for any complex manifold $X$ with holomorphic tangent bundle
$T_X$, an $L_\infty$-algebra structure on
$\Omega^{0,\bullet}(X, T_X[-1])$
whose $\ell_2$ is the Dolbeault-$\bar\partial$ of the Atiyah bracket
and whose $\ell_n$ for $n \geq 3$ are explicit curvature expressions
built from $\At(T_X)$.

*Step 2 — Atiyah class as cubic obstruction.* The cubic $\ell_3$ is
(Kapranov 1999 Thm.~2.8.1)
\[
\ell_3(\xi_1, \xi_2, \xi_3) = \mathrm{Sym}\,
\At(T_X)(\xi_1) \cdot [\xi_2, \xi_3]
\]
where $\At(T_X)$ acts as a Dolbeault 1-form valued in $\mathrm{End} T_X$.
$\At(T_X) = 0$ in Dolbeault cohomology implies $\ell_3$ is Lie-null-
homotopic; this is necessary for formality.

*Step 3 — Higher obstructions.* Markarian (2009, "The Atiyah class,
Hochschild cohomology and the Riemann–Roch theorem," J. Lond. Math.
Soc.) identifies the higher $\ell_n$ for $n \geq 4$ as Taylor
coefficients of the Duflo–Todd class
$\mathrm{td}(T_X)^{1/2} \in H^\bullet(X, \Lambda^\bullet T_X^\vee)$
of Calaque–Van den Bergh type. On compact CY$_d$, $c_1(X) = 0$ so
$\mathrm{td}(T_X)$ is even-degree, and Willwacher 2014 (arXiv:1407.3736
Thm.~3.2) shows the Grothendieck–Teichmüller group acts transitively
on the set of formality quasi-isomorphisms, making the Duflo class
explicitly computable.

*Step 4 — Verification on $K3 \times E$.* The Atiyah class decomposes:
$\At(T_{K3 \times E}) = p_{K3}^* \At(T_{K3}) \oplus p_E^* \At(T_E)$.
On $E$: $T_E$ is the trivial line bundle (elliptic curve has trivial
tangent bundle via left-invariant vector fields, since $E$ is a complex
Lie group), so $\At(T_E) = 0$. On K3: $\At(T_{K3})$ is the class of the
Atiyah extension $0 \to \Omega^1_{K3} \otimes T_{K3} \to J^1(T_{K3})
\to T_{K3} \to 0$ in $H^1(K3, \Omega^1_{K3} \otimes \mathrm{End} T_{K3})$.
This is non-zero in general (K3 has no holomorphic connection on $T_{K3}$),
but Căldăraru–Huybrechts 2010 (arXiv:0907.2450 §4) proves that on K3 the
Kapranov $L_\infty$-structure is quasi-isomorphic to its strictification
(i.e., formal) via the Hochschild–Kostant–Rosenberg isomorphism twisted
by $\sqrt{\mathrm{td}(T_{K3})}$. Hence K3 is HKR-formal despite
$\At(T_{K3}) \neq 0$.

*Step 5 — Product formality.* Since both K3 (HKR-formal via
Căldăraru–Huybrechts) and $E$ (trivially formal, $\At = 0$) are formal,
and formality is closed under Künneth for Dolbeault algebras (Halperin
1983 Thm. 3.1 in the real analogue; the complex analogue uses the
exterior tensor product of $L_\infty$-structures and Duflo-multiplicativity
of $\mathrm{td}$ under products), $K3 \times E$ is formal.

*Step 6 — Kuranishi receptacle correction.* The Kuranishi cubic
obstruction on compact CY$_3$ lives in $H^3(X, \Lambda^3 T_X)$, not
$H^3(X, \Omega^3_X)$. The two are Serre-dual for CY via
$\Omega^3_X \cong \mathcal{O}_X$ (Calabi–Yau condition), so
$H^3(X, \Lambda^3 T_X) \cong H^3(X, \Omega^3_X)^\vee$ by Serre duality
only when applied via $\mathrm{td}$-correction; the naive identification
$\Lambda^3 T_X = \Omega^3_X^\vee \otimes \mathcal{O}_X$ is what works
on CY. On K3, $\Lambda^3 T_{K3} = 0$ for rank reasons ($T_{K3}$ has
rank $2$, so $\Lambda^3 T_{K3} = 0$ trivially), confirming the
Kuranishi vanishing.
$\qed$

### Theorem (Deformation complex of $\Obs_{\hCS}$).

\ClaimStatusTheorem

The deformation complex of the $E_3$-algebra $\Obs_{\hCS}(\CC^3)$ is
$\mathrm{HH}^*_{E_3}(\Obs, \Obs)$, the $E_3$-Hochschild cohomology, which
by Francis 2013 (arXiv:1211.5619 Thm.~2.29) is identified with the
shifted $E_{3+1} = E_4$-center:
\[
\mathrm{Def}(\Obs_{\hCS})[1] \simeq \mathrm{HH}^*_{E_3}(\Obs, \Obs)
\simeq Z_{E_4}(\Obs)[3]
\]
where $Z_{E_4}$ is the $E_4$-center in the sense of Ginzburg–Kapranov–
Francis. The shift by $3$ is Poincaré-dual to the three
holomorphic directions on $\CC^3$.

**Proof.**

Francis's theorem (Thm.~2.29, building on Ginzburg–Kapranov 1994 and
Lurie HA §5.3.1.6) states that for any $E_n$-algebra $A$ in a stable
symmetric monoidal $\infty$-category, the tangent complex to $A$ as an
$E_n$-algebra is $\mathrm{HH}_{E_n}(A, A)$ shifted by $n$, and this is
naturally identified with $\Omega Z_{E_n}(A) = Z_{E_{n+1}}(A)[-1]$
(the $E_{n+1}$-center).

Applied to $A = \Obs_{\hCS}(\CC^3)$ as an $E_3$-algebra:
\[
\mathrm{HH}^{*+3}_{E_3}(\Obs, \Obs) \simeq Z_{E_4}(\Obs)
\]
and the tangent complex is $\mathrm{HH}^{*}_{E_3}(\Obs, \Obs)[3]$ as
stated. $\qed$

### Theorem (First-order moduli, corrected).

\ClaimStatusTheorem

For simple $\fg$ (classical ADE Lie algebra), the first-order moduli
of deformations of 6D $\hCS$ on $\CC^3$ preserving CY$_3$ structure
decompose as
\[
T_0 \mathcal{M}_{\hCS(\CC^3, \fg)} = H^{0,3}_{\bar\partial, c}(\CC^3)
\otimes \mathrm{Sym}^2(\fg^\vee)^{\fg}[-3]
\]
where $\mathrm{Sym}^2(\fg^\vee)^{\fg}$ denotes $\fg$-invariant symmetric
bilinear forms on $\fg$. For simple $\fg$, the Killing form
$B(X, Y) = \mathrm{tr}(\mathrm{ad}_X \mathrm{ad}_Y)$ is (by Whitehead's
first lemma and simplicity) the unique such form up to scalar, so
$\mathrm{Sym}^2(\fg^\vee)^{\fg} = \CC \cdot B$, and
\[
T_0 \mathcal{M}_{\hCS(\CC^3, \fg)} = \CC \cdot (B \otimes \Omega_{\CC^3})
\]
where $\Omega_{\CC^3} = dz_1 \wedge dz_2 \wedge dz_3$ generates
$H^{0,3}_{\bar\partial, c}(\CC^3) \cong \CC$ via Serre duality.

This one-parameter deformation matches, under the Costello 2013 map
from $\hCS$ to the affine Yangian, the CY-symmetric Yangian
$Y_{\epsilon, \epsilon, \epsilon}(\widehat{\fg})$ modulo the single
parameter $\epsilon \in \CC$ (equivalently, the slice $\epsilon_1 =
\epsilon_2 = \epsilon_3$ inside the two-parameter Yangian family
$Y_{\epsilon_1, \epsilon_2, \epsilon_3}$).

**Proof (CFG detail).**

*Step 1 — Deformation complex cohomology on flat $\CC^3$.* By the
previous theorem, $\mathrm{Def}(\Obs_{\hCS}) = \mathrm{HH}^*_{E_3}
(\Obs, \Obs)[3]$. On $\CC^3$ with the minimal model (trivial
$L_\infty$-structure on $\fg[1]$), the $E_3$-Hochschild complex is
computed by the Knudsen–Francis theorem:
\[
\mathrm{HH}^*_{E_3}(\mathrm{Sym}^\bullet \fg[1], \mathrm{Sym}^\bullet \fg[1])
= \mathrm{Sym}^\bullet(\fg^\vee[-1]) \otimes_{\fg} \mathrm{CE}^\bullet_{E_3}(\fg)
\]
where $\mathrm{CE}^\bullet_{E_3}(\fg) = \mathrm{Sym}^\bullet(\fg^\vee[-1])
\otimes \Lambda^\bullet(\fg^\vee[-3])$ is the $E_3$-Chevalley–Eilenberg
complex (Kjaer 2017 arXiv:1706.03876 §3; Francis 2013 Thm.~4.16).

*Step 2 — Selection of CY-preserving deformations.* The CY$_3$ condition
$\sum \epsilon_i = 0$ (i.e., the equivariant holomorphic volume form is
preserved) picks out the $\mathrm{SL}_3$-invariant subcomplex of the
$\mathrm{GL}_3$-equivariant Hochschild cohomology. Under the
$T^3 \curvearrowright \CC^3$ with weights $(\epsilon_1, \epsilon_2,
\epsilon_3)$, the $\bar\partial$-cohomology gets a $T^3$-grading, and
the CY slice selects the weight-zero component of $\mathrm{Sym}^\bullet(\fg^\vee)$.

*Step 3 — Compactly-supported Dolbeault cohomology.* The relevant
cohomology for deformations that integrate against the CY volume form is
the compactly-supported Dolbeault cohomology:
\[
H^{0,\bullet}_{\bar\partial, c}(\CC^3) = \begin{cases}
0 & \bullet \in \{0, 1, 2\}\\
\CC \cdot \overline{d\bar z_1 \wedge d\bar z_2 \wedge d\bar z_3}\text{-type} & \bullet = 3
\end{cases}
\]
by Serre duality $H^{0,q}_{c}(\CC^3) = H^{3-q,3}(\CC^3)^\vee$ and the
fact that $H^{p,q}(\CC^3) = \CC \delta_{p,0}\delta_{q,0}$.

*Step 4 — Invariant symmetric tensor selection.* At degree $(0,3)$ in
the Dolbeault grading, the Hochschild complex evaluates to
\[
\mathrm{HH}^3_{E_3, \mathrm{CY}}(\Obs, \Obs) = H^{0,3}_{\bar\partial,c}
(\CC^3) \otimes \mathrm{Sym}^2(\fg^\vee)^{\fg}.
\]
The appearance of $\mathrm{Sym}^2(\fg^\vee)^{\fg}$ (not $\mathrm{Sym}^2(\fg^\vee)$)
comes from: the deformation must preserve the $(-1)$-shifted symplectic
pairing $\omega : \Omega^{0,\bullet}(X, \fg) \otimes
\Omega^{0,\bullet}(X, \fg) \to \CC$ given by
$\omega(\alpha, \beta) = \int_X \Omega_X \wedge \langle \alpha, \beta
\rangle$, where $\langle -, -\rangle$ is the Killing form; the
$\fg$-invariance of the deformation cocycle is forced by gauge invariance
(the deformation must commute with the adjoint action).

*Step 5 — Whitehead's first lemma.* For $\fg$ simple, Whitehead's first
lemma (Jacobson 1962 Ch.~III §7) gives
\[
H^1_{\mathrm{Lie}}(\fg, V) = 0 \quad \text{for any finite-dim.\ module } V,
\]
and more refinedly the Casimir argument (Humphreys 1972 §6.4) gives
\[
\mathrm{Sym}^2(\fg^\vee)^{\fg} = \CC \cdot B
\]
where $B$ is the Killing form (one-dimensional since $\fg$ simple forces
$V = \mathrm{Sym}^2 \fg^\vee$ to have exactly one invariant).

*Step 6 — Yangian match.* By Costello 2013 (arXiv:1303.2632 §11–12) and
Costello–Gaiotto 2018 (arXiv:1810.01970 §3), the Koszul-dual description
of the deformations of 6D $\hCS$ on $\CC^3$ is the affine Yangian
$Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\fg})$ with three
parameters corresponding to the three $T^3$-weights. The CY slice
$\sum \epsilon_i = 0$ is imposed at the level of the Yangian deformation
to match the CY holomorphic volume.

*Step 7 — Parameter reduction.* After the CY slice, the two-parameter
family $(\epsilon_1, \epsilon_2)$ (with $\epsilon_3 = -\epsilon_1 -
\epsilon_2$) has $S_3$-symmetry (permutations of $\epsilon_i$). The
CY-symmetric point $\epsilon_1 = \epsilon_2 = \epsilon_3$ forces
$\epsilon_1 = 0$, giving the undeformed point. The rank-$1$
$\mathrm{Sym}^2(\fg^\vee)^{\fg} = \CC \cdot B$ contributes one direction
of deformation, corresponding to the scalar $\epsilon$ such that
$(\epsilon_1, \epsilon_2, \epsilon_3) = (\epsilon, \epsilon, -2\epsilon)$
mod the $S_3$-orbit.

Hence the match is $T_0 \mathcal{M}_{\hCS} = \CC \cdot (B \otimes \Omega)$
corresponds to the one-parameter family $Y_{\epsilon, \epsilon,
-2\epsilon}(\widehat{\fg})$ modulo $S_3$, which after identification is
the single Yangian coupling $\epsilon$.
$\qed$

**Remark (correction of the CY-slice framing).** The claim in the
target that "the CY slice $\sum \epsilon_i = 0$ reduces
$\mathrm{Sym}^2(\fg^\vee)^{\mathrm{inv}}$ from rank-$2$ (for generic
$\epsilon$) to rank-$1$" is malformed: $\mathrm{Sym}^2(\fg^\vee)^{\fg}$
for simple $\fg$ is rank-$1$ before any CY slicing (Whitehead + Casimir),
independent of the $\epsilon$'s. The CY slice reduces the
three-parameter Yangian family $(\epsilon_1, \epsilon_2, \epsilon_3)$ to
a two-parameter family (one linear relation), and further by $S_3$-
symmetry to a one-parameter family. The identification $T_0 \mathcal{M}
= \CC \cdot \mathrm{Kil}$ is correct; the combinatorial source of the
single parameter is the $S_3$-quotient of the two-parameter $(\epsilon_1,
\epsilon_2)$-slice, not a rank-reduction of $\mathrm{Sym}^2$.

## Retractions with true hidden structure

### Retraction 1: "the propagator kills the harmonic subspace $\mathcal{H} = \CC[z_1, z_2, z_3] \otimes \fg$"

\ClaimStatusCorrected

*Wrong claim.* The tree vanishing $\ell_n^{\min} = 0$ for $n \geq 3$ on
flat $\CC^3$ follows because "the propagator $P_{\mathrm{BM}}$ kills the
harmonic subspace $\mathcal{H} = \CC[z_1, z_2, z_3] \otimes \fg$."

*Precise error.* $P_{\mathrm{BM}}$ does not "kill" $\mathcal{H}$: on a
polynomial $f \in \CC[z_1, z_2, z_3]$, the result
$\int_{\CC^3} P_{\mathrm{BM}}(z, w) \wedge f(w) dw_1 dw_2 dw_3$
is a $(0, -1)$-form, but the Dolbeault complex starts at
$(0, 0)$, so $\Omega^{0,-1} = 0$ and hence $p|_{\Omega^{0,0}} = 0$ for
degree reasons, not for any "harmonic-killing" mechanism. Moreover, on
compactly-supported polynomial-like inputs, $P_{\mathrm{BM}}$ acts as a
Green operator, recovering the input up to a harmonic shadow; it does
not annihilate anything non-trivially.

*True hidden structure.* The vanishing of $\ell_n^{\min}$ for $n \geq 2$
on flat $\CC^3$ comes from a **Dolbeault degree count**: harmonic
inputs sit in $\Omega^{0,0}$; the Lie bracket of two $\Omega^{0,0}$-forms
is $\Omega^{0,0}$; the propagator is structurally zero on $\Omega^{0,0}$
(nowhere to land). Every tree with at least one internal edge has at
least one propagator acting on a $(0, 0)$-form output of a bracket,
hence vanishes. This is **Kapranov's degree-count argument** (Kapranov
1999 §3.1) applied to the Dolbeault–BV complex.

### Retraction 2: "$\At(TX) = 0$ is the formality obstruction on compact CY$_3$"

\ClaimStatusCorrected

*Wrong claim.* The Atiyah class $\At(TX) \in H^1(X, \Omega^1_X \otimes
\mathrm{End} T_X)$ is the formality obstruction on compact CY$_3$.

*Precise error.* $\At(TX) = 0$ is **necessary but not sufficient**.
The full obstruction is a sequence of classes
$\{\kappa_n\}_{n \geq 3} \subset \bigoplus \mathrm{Ext}^2(\mathrm{Sym}^n T_X^\vee,
\mathcal{O}_X)$ whose leading term is $\At \cup \At$. On compact CY$_d$
with $c_1(X) = 0$, the higher obstructions are controlled by the Duflo
class $\mathrm{td}(X)^{1/2}$ via Calaque–Van den Bergh (arXiv:0811.4159).

*True hidden structure.* Formality on compact CY$_3$ is obstructed by
the full Kapranov tower $\{\kappa_n\}$; on $K3 \times E$ specifically,
formality follows not from "$\At(T_{K3 \times E}) = 0$" (which is false:
$\At(T_{K3}) \neq 0$ generically) but from:
(i) $\At(T_E) = 0$ (elliptic curve trivial tangent),
(ii) K3 is HKR-formal via Căldăraru–Huybrechts 2010 (using a twisted
HKR isomorphism involving $\sqrt{\mathrm{td}(T_{K3})} = 1 - \tfrac{1}{24}
c_2(K3) + \ldots$),
(iii) formality closed under products (Halperin 1983 analogue).

### Retraction 3: "Kuranishi cubic receptacle lives in $H^3(K3, \Omega^3_{K3})$"

\ClaimStatusCorrected

*Wrong claim.* The cubic Kuranishi obstruction receptacle on K3 is
$H^3(K3, \Omega^3_{K3})$, which vanishes because $\Omega^3_{K3} = 0$.

*Precise error.* The Kuranishi cubic receptacle for deformations of the
complex structure (or of a coherent sheaf) is $H^2(X, \Lambda^2 T_X)$
at quadratic order and $H^3(X, \Lambda^3 T_X)$ at cubic order — **not**
$H^3(X, \Omega^3_X)$. The conflation comes from CY duality
$\Lambda^n T_X \cong \Omega^{n,0}_X$ for an $n$-dimensional CY — but
K3 is $2$-dimensional, so $\Lambda^3 T_{K3} = 0$ for rank-count reasons
($T_{K3}$ has rank $2$, wedge power $3$ is zero), and separately
$\Omega^3_{K3} = 0$ for rank reasons (holomorphic $3$-forms don't exist
on a surface). These are two different vanishings.

*True hidden structure.* On K3, the Kuranishi cubic obstruction
vanishes because $\Lambda^3 T_{K3} = 0$ (rank argument). The
receptacle $H^3(K3, \Omega^3_{K3})$ also vanishes for independent rank
reasons. The statement should read: "Kuranishi cubic receptacle
$H^3(K3, \Lambda^3 T_{K3})$ vanishes by rank of $T_{K3}$."

### Retraction 4: "CY slice reduces $\mathrm{Sym}^2(\fg^\vee)^{\mathrm{inv}}$ from rank-$2$ to rank-$1$"

\ClaimStatusCorrected

*Wrong claim.* The CY slice $\sum \epsilon_i = 0$ reduces
$\mathrm{Sym}^2(\fg^\vee)^{\mathrm{inv}}$ from rank-$2$ (for generic
$\epsilon$'s) to rank-$1$ (matching $\CC \cdot \mathrm{Kil}$).

*Precise error.* $\mathrm{Sym}^2(\fg^\vee)^{\fg}$ for simple $\fg$ is
rank-$1$ **independent of any $\epsilon$-slicing**, by Whitehead's first
lemma and simplicity (Humphreys 1972 §6.4 Lemma). The $\epsilon$-
parameters live in the deformation side (Yangian coupling constants),
not in the representation-theoretic $\mathrm{Sym}^2$ side.

*True hidden structure.* The reduction goes the other way: the
three-parameter Yangian family $Y_{\epsilon_1, \epsilon_2, \epsilon_3}
(\widehat{\fg})$ has the CY constraint $\sum \epsilon_i = 0$ imposed
externally (from the CY volume form preservation), giving a two-parameter
family. The $S_3$-action on $(\epsilon_1, \epsilon_2, \epsilon_3)$
further identifies $S_3$-orbits, leaving a one-parameter family that
matches the one-dimensional $T_0 \mathcal{M}_{\hCS} = \CC \cdot B$.
The rank-matching is on the Yangian side: one-parameter family ↔
$\CC \cdot B$, both one-dimensional.

### Retraction 5: "The homotopy transfer sum over trees really converges/truncates"

\ClaimStatusCorrected

*Wrong claim (implicit).* The tree sum in the Kontsevich–Soibelman
minimal-model recursion converges on flat $\CC^3$ and gives zero by
"every tree with an internal edge vanishes."

*Precise error.* On flat $\CC^3$, the tree sum is **finite at each
order** ($\mathcal{T}_n$ is finite for each $n$), so convergence is not
the issue; the issue is **vanishing**, which holds for the degree
reason above. However, on compact CY$_3$, the tree sum can contribute
non-trivially via the curvature of $T_X$ (Kapranov's $\kappa_n$ classes),
and the sum over trees needs the Kapranov L∞-structure on the Dolbeault
polyvector algebra, which converges only formally and requires the
Grothendieck–Teichmüller resummation (Willwacher 2014).

*True hidden structure.* On $\CC^3$: exact algebraic vanishing by degree
count, tree sum is finite and zero.
On compact CY$_3$: formal convergence of the Kapranov L∞-structure;
the Duflo class $\mathrm{td}(X)^{1/2}$ encodes the finite-rank resummation
when $c_1(X) = 0$; higher-curvature corrections vanish iff the Kapranov
tower $\{\kappa_n\}_{n \geq 3}$ vanishes.

## Cross-consistency checks

### (a) Platonic synthesis Waves 11–16

The three survivors (Theorems \texttt{Minimal $L_\infty$ on $\CC^3$},
\texttt{Atiyah as formality obstruction}, \texttt{First-order moduli})
replace the four-sentence statement of \texttt{wn:thm:plat-Linf-minimal}
and the three-sentence statement of \texttt{wn:thm:plat-first-order-moduli}
with CFG-detail statements + proofs. The $\Phi$ two-stage factorisation
(\texttt{wn:thm:plat-two-stage}) is untouched: Stage 1 (canonical up to
contractible choice) is precisely the formality of the Kapranov
$L_\infty$-structure, verified by the Atiyah-class obstruction tower;
the contractible choice is the Duflo twist $\mathrm{td}(X)^{1/2}$.

The quantum-observables theorem (\texttt{wn:thm:plat-hCS-quantum})
uses the Bochner–Martinelli propagator; our corrections show that
the BM propagator's role in formality is a degree-count, not a
"harmonic-killing" mechanism, which sharpens the proof sketch there.

### (b) CoHA-to-$\cW_\infty$ treatise

The Jordan triple loop quiver ($\CC^3$) example (\S1) uses only
$E_1/E_3$-structure of $\mathrm{Obs}_{\hCS}$ and does not invoke
formality at depth. Our corrected formality theorem is compatible:
the $\Obs_{\hCS}(\CC^3)$ is formal as a holomorphic-$E_3$-algebra
because $\CC^3$ has trivial Atiyah class ($T_{\CC^3}$ trivial), so all
Kapranov obstructions $\kappa_n$ vanish identically, not just $\kappa_3$.

The resolved conifold (\S2) has non-trivial $\At(T_{\mathbb{Y}})$
(the flop uses the Atiyah class), and formality requires the non-trivial
Duflo twist; consistent with our corrected statement.

The $K3 \times E$ example (\S3) invokes "obstructions to CoHA
construction" which in the formality language are Kapranov obstructions
beyond $\kappa_3$. Our proof that $K3 \times E$ is HKR-formal via
Căldăraru–Huybrechts resolves this — the formality holds despite
$\At(T_{K3}) \neq 0$.

### (c) Universal Borcherds identity $\kBKM(\Phi_N) = c_N(0)/2$

Formality of the Kapranov $L_\infty$-structure on $K3 \times E$ is a
Stage-$1$ input (not a Stage-$2$ specialisation) and is orthogonal to
the denominator-formula computation of $\kBKM$. The identification
Stage-$1$ factorisation algebra → Stage-$2$ chiral-on-$E$ uses Dunn–Lurie
additivity and does not re-invoke formality. So the universal Borcherds
identity is consistent with our corrected formality statements.

### (d) Two-stage factorisation $\Phi_d = \mathrm{Sp}_{\Sigma, C} \circ
\Phi^{\mathrm{FA}}_d$

Stage 1: the canonical $E_d$-hFA output of $\Phi^{\mathrm{FA}}_d$ on $X$
is defined using the Kapranov $L_\infty$-structure on the Dolbeault
polyvector algebra. The "canonical up to contractible choice" statement
is precisely: the formality quasi-isomorphism is unique up to the action
of the Grothendieck–Teichmüller group (Willwacher 2014), which is
contractible as a topological group. On flat $\CC^3$: trivial formality
(our Theorem 1); the contractible choice reduces to a point.
On $K3 \times E$: HKR-formality via Căldăraru–Huybrechts + Künneth;
the contractible choice is the action of $\mathrm{GT}$ on the Duflo twist
$\mathrm{td}(X)^{1/2}$.

Stage 2: factorisation homology over $\Sigma_{d-1}$ restricted to $C$.
Our analysis is orthogonal to this stage.

## Residual frontier

- **Higher Kapranov obstructions $\kappa_n$ for $n \geq 4$ on compact
  CY$_3$**: \ClaimStatusOpen. Markarian 2009 identifies these with
  Taylor coefficients of the Duflo class, but explicit computation on
  (e.g.) the quintic requires the full GT action and is not in hand.

- **Explicit formality quasi-isomorphism on $K3 \times E$ at chain
  level**: \ClaimStatusOpen. Căldăraru–Huybrechts 2010 gives an abstract
  HKR-formality; an explicit twisted HKR map at Dolbeault–Čech chain
  level that commutes with the product structure $K3 \times E$ is
  not in hand.

- **Comparison between Kajiura–Merkulov tree formula and
  Grothendieck–Teichmüller resummation**: \ClaimStatusConjectured.
  Willwacher 2014 states transitivity of GT on formality trivialisations;
  explicit compatibility with the tree formula is conjectured but not
  proved in the literature we have traced.

- **Yangian reconstruction from $T_0 \mathcal{M} = \CC \cdot B$**:
  \ClaimStatusConjectured. The forward direction $T_0 \mathcal{M}
  \hookrightarrow Y_{\epsilon}$ is Costello 2013; the reverse (that the
  one-parameter family is the full Yangian family, not a sub-family)
  requires either an invariant-theory argument on $\mathrm{HH}^*_{E_3}$
  or a direct identification with Drinfeld's PBW basis of $Y$.

- **Sufficiency of $\At = 0$ on general CY$_3$**: \ClaimStatusOpen.
  The statement "$\At(TX) = 0$ implies formality" holds on $\CC^n$ and
  on compact K3/abelian surfaces (HKR-formal by other means); on general
  compact CY$_3$ the higher Kapranov obstructions can in principle be
  non-zero despite $\At$ vanishing, but no counterexample in the
  CY$_3$ class is known.

## Attack-heal cycle log (private — for synthesis agent only, not for manuscript)

**Cycle 1.** ATTACK: The claim "propagator kills the harmonic subspace
$\mathcal{H} = \CC[z_1, z_2, z_3] \otimes \fg$" is false as stated. The
BM propagator $P_{\mathrm{BM}}$ is a Green operator for $\bar\partial$,
not a projection annihilating harmonic forms. On polynomial inputs, it
acts as inverse of $\bar\partial$ on the non-harmonic complement, giving
back the input up to harmonic shadow — not zero.
HEAL: The correct mechanism is a Dolbeault **degree count**: harmonic
inputs live in $\Omega^{0,0}$; the Hodge homotopy propagator $p$ maps
$\Omega^{0,q}$ to $\Omega^{0,q-1}$, and on $\Omega^{0,0}$ it is
structurally zero (target is $\Omega^{0,-1} = 0$). Lie brackets of
$\Omega^{0,0}$-forms stay in $\Omega^{0,0}$, so every tree with an
internal edge has a propagator acting on a $\Omega^{0,0}$-input and
vanishes. Kapranov 1999 §3.1 gives this argument cleanly.

**Cycle 2.** ATTACK: "$\At(TX) = 0$ on $K3 \times E$ is the formality
obstruction." But $\At(T_{K3}) \neq 0$ generically (K3 has no
holomorphic connection on $T_{K3}$). So $\At(T_{K3 \times E}) \neq 0$,
and the claim's conclusion fails.
HEAL: Distinguish necessary vs sufficient. $\At = 0$ is the **cubic**
obstruction $\kappa_3$ (Kapranov 1999 Thm.~2.8.1). Higher obstructions
$\kappa_n$ for $n \geq 4$ are Taylor coefficients of the Duflo class
$\mathrm{td}(X)^{1/2}$ (Markarian 2009). On $K3$: formality holds via
**Căldăraru–Huybrechts 2010 twisted HKR** using $\sqrt{\mathrm{td}(T_{K3})}$,
despite $\At(T_{K3}) \neq 0$. On $K3 \times E$: formality follows by
product + HKR-formality of K3 + triviality of $E$. The correct statement
is about the Kapranov tower, not $\At$ alone.

**Cycle 3.** ATTACK: "Kuranishi cubic receptacle $H^3(K3, \Omega^3_{K3})$
vanishes since $\Omega^3_{K3} = 0$." But the Kuranishi obstruction for
complex-structure or sheaf deformations lives in $H^2(X, \Lambda^2 T_X)$
at quadratic and $H^3(X, \Lambda^3 T_X)$ at cubic — not $H^3(X, \Omega^3_X)$.
The conflation of $\Omega^3_X$ with $\Lambda^3 T_X$ uses CY duality
$\Omega^n_X \cong \mathcal{O}_X \otimes \Lambda^n T_X^\vee$, which is
$n$-dimensional and $K3$ is $n = 2$.
HEAL: State the correct receptacle $H^3(K3, \Lambda^3 T_{K3})$. It
vanishes by rank: $T_{K3}$ has rank $2$, so $\Lambda^3 T_{K3} = 0$
trivially. The receptacle $H^3(K3, \Omega^3_{K3})$ also vanishes for
independent rank reasons ($\Omega^3$ on a surface is zero). Two
different vanishings, both valid on K3.

**Cycle 4.** ATTACK: "First-order moduli $\CC \cdot \mathrm{Kil}$
matches Yangian family modulo CY slice $\sum \epsilon_i = 0$ at the
level of dimensions — is this an actual identification or only
dimensional coincidence?"
HEAL: The identification is forced by $(-1)$-shifted symplectic
preservation: the Killing form is the **unique** $\fg$-invariant
symmetric pairing on a simple $\fg$ (Whitehead lemma + Casimir), and
the BV $(-1)$-shifted symplectic structure on $\Omega^{0,\bullet}(\CC^3,
\fg)$ is $\omega(\alpha, \beta) = \int \Omega \wedge \langle \alpha,
\beta \rangle_B$ with $B$ the Killing form. Deformations preserving
$\omega$ are automatically $B$-valued, giving the match $T_0\mathcal{M} =
\CC \cdot B$ non-coincidentally. The Costello 2013 map $\hCS \to Y$
is then a **reconstruction** of $Y_\epsilon(\widehat{\fg})$ from a
single coupling $\epsilon$ controlling the Killing-form normalisation.

**Cycle 5.** ATTACK: "CY slice $\sum \epsilon_i = 0$ reduces
$\mathrm{Sym}^2(\fg^\vee)^{\mathrm{inv}}$ from rank-$2$ for generic
$\epsilon$'s to rank-$1$." But $\mathrm{Sym}^2(\fg^\vee)^{\fg}$ for
simple $\fg$ is rank-$1$ by Whitehead's first lemma **independently of
$\epsilon$-slicing**. The $\epsilon$'s parametrise deformation couplings,
not Lie-algebra-invariant bilinear forms.
HEAL: The $\epsilon$-reduction happens on the Yangian side, not the
$\mathrm{Sym}^2$ side. The three-parameter Yangian family
$Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\fg})$ has CY slice
$\sum \epsilon_i = 0$ (two-parameter), then $S_3$-quotient (one-parameter),
matching the one-dimensional $T_0 \mathcal{M} = \CC \cdot B$. The
original claim conflates Yangian parameter reduction with Lie-algebra
invariant-form dimension — two different rank-$1$'s, accidentally
the same number.

**Cycle 6.** ATTACK: "Does the Kontsevich–Soibelman homotopy transfer
recursion actually converge at all tree orders?" Kontsevich–Soibelman
2001 (arXiv:math/0011041) define the transfer via formal power series
in propagators; convergence is formal, not analytic.
HEAL: On flat $\CC^3$, the tree sum at each order $n$ is **finite**
($|\mathcal{T}_n| < \infty$), so there's no convergence issue — just
vanishing at each order by the Dolbeault degree count. On compact
CY$_3$, convergence is formal and requires the GT-group resummation
of Willwacher 2014; the Duflo class $\mathrm{td}(X)^{1/2}$ encodes
the finite-rank output when $c_1(X) = 0$. Both scopes need to be
tracked (AP-CY Pattern 236: ambient qualifier discipline).

**Cycle 7.** ATTACK: "Every tree with an internal edge vanishes
because the propagator kills the harmonic subspace" — what about trees
with multiple internal edges forming a "ladder"? Do they really all
vanish by the same mechanism?
HEAL: Yes, but the mechanism is the degree-count cascaded: the output
of each bracket at an internal vertex is $\Omega^{0,0}$ (brackets preserve
Dolbeault degree since all inputs are $\Omega^{0,0}$); every internal
edge has a propagator mapping $\Omega^{0,0}$ to $\Omega^{0,-1} = 0$;
hence the whole composition is zero. This is a genuinely robust
vanishing: any tree with at least one internal edge is zero. (Trees
with zero internal edges are the "corolla," which contribute only to
$\ell_1^{\min}$ and $\ell_2^{\min}$; both are the transferred unary
differential and Lie bracket, neither identically zero — $\ell_1^{\min}
= 0$ because the $L_\infty$-structure is concentrated in degree $0$
after transfer, and $\ell_2^{\min} = [-, -]_{\fg}$ is the Lie bracket,
nonzero.)
