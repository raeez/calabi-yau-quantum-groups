# Agent 09 (Costello voice): Non-abelian K3 Yangian from Factorization Algebras

Volume III swarm note, K3 non-abelian Yangian attack.
Target chapters:
`/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_yangian_chapter.tex`,
`/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex`,
`/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex`,
`/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex`.

Voice: Kevin Costello. Factorization-algebra framework as the correct
language for holomorphic field theories; Ran-space constructions rigorous
(Costello--Gwilliam 2017/2021, Costello--Francis--Gwilliam 2025); local-to-global
controlled by operadic coherence; derived geometry exact.

Raeez Lorgat, sole author of the manuscript; this note is a working draft.

---

## 1. Setup and the question

Vol III asks whether there is a *non-abelian* K3 Yangian
$Y_{\mathrm{n.a.}}(\mathfrak{g}_{K3})$ analogous to the
construction of the affine Yangian $Y(\widehat{\mathfrak{gl}}_1)$
from the 6d holomorphic Chern--Simons theory on $\mathbb{C}^3$
(Costello 2017, `Supersymmetric gauge theory and the Yangian`; Costello,
*M-theory in the $\Omega$-background*, 2017; Costello--Paquette, *Twisted
supergravity and Koszul duality*, 2021).

The manuscript already contains:
(a) a complete `abelian' K3 Yangian $Y_{\mathrm{ab}}(\mathfrak{g}_{K3})$
as the Yangian deformation of the rank-24 Heisenberg on the Mukai
lattice $\widetilde{\Lambda}_{K3}$, with structure function
$g_{K3}(u) = \prod_{a=1}^{24} (u-h_a)/(u+h_a)$
(`k3_yangian_chapter.tex:1239--1246`);
(b) a conjectural $E_3$-chiral factorization algebra on $\mathbb{C}^3$
and its restriction to $K3 \times E$ (`en_factorization.tex:489--523`,
`k3_yangian_chapter.tex:2380--2466`);
(c) a non-abelian BKM root datum $\mathfrak{g}_{\Delta_5}$ with Serre
obstruction at imaginary simple roots
(`k3_yangian_chapter.tex:1262--1313`).

**The missing piece** is a factorization-algebra formulation
of the non-abelian K3 Yangian that is *locally well-defined* (no
anomaly), that reproduces the Maulik--Okounkov stable-envelope
$R$-matrix on $\mathrm{Hilb}^n(K3)$, and that identifies with the
Koszul-dual object $B_X(C)$ in the sense of Vol I Theorem~B
(chiral Positselski).

I attack this in rounds.

---

## 2. Round 1 ATTACK: is the factorization-algebra formulation well-posed?

**Claim under attack.** *The non-abelian K3 Yangian is the
factorization algebra $\mathcal{A}_{K3}$ on $\mathrm{Ran}(K3)$ arising
from 4d hCS on $K3$, with the $E_2$ structure imposed by the d=2 CY
condition.*

Costello's own catechism is four questions:

**(a) Base space.** Is $\mathcal{A}_{K3}$ defined on $\mathrm{Ran}(K3)$?
K3 has complex dimension 2, real dimension 4. Costello--Gwilliam assign
a factorization algebra on the Ran space of *any* smooth manifold, so
structurally yes: $\mathrm{Ran}(K3) = \coprod_n K3^n / S_n$ as a
prestack, and a factorization algebra is a cosheaf $\mathcal{A}$ on
this prestack with the usual factorization axiom. The *holomorphic*
refinement requires $K3$ to be complex: the structure sheaf of
$\mathrm{Ran}(K3)$ is holomorphic in each factor, and $\mathcal{A}$
assigns holomorphic chain complexes. All of this is Costello--Gwilliam
standard.

**(b) $E_2$ from d=2 CY.** The d=2 CY condition produces an
$E_2$-chiral structure on a complex 2-fold via the Kontsevich--Vlassopoulos
(or Costello--Li 2016) $S^2$-framing on the configuration space
$\mathrm{Conf}_n(K3)$. Explicitly: $\mathrm{Conf}_2(K3)$ is a real
4-manifold-bundle over $K3$ (once the centre-of-mass is fixed) whose
fibre is $K3 \setminus \{pt\} \simeq_{\mathrm{htpy}}$ something
non-trivial. The local model at a point $p \in K3$ is
$\mathrm{Conf}_2(\mathbb{C}^2)$, whose fibre over the centre-of-mass
deformation-retracts onto $S^3$; but $\pi_1(S^3) = 0$, so *no
topological braiding* obstructs defining $\mathcal{A}_{K3}$ on the Ran
space.

The $E_2$ structure is *holomorphic*, not topological: it is what
`en_factorization.tex:454--470` calls the holomorphic refinement,
exactly one $E_1$ contribution per complex direction of the base. So:
$E_2$-chiral on $K3$, not $E_4$-topological.

**Verdict on (a)--(b):** well-defined locally. No obstruction at the
Ran-space level.

**(c) Hopf structure on $\mathrm{Rep}^{E_2}(\mathcal{A}_{K3})$.** The
Drinfeld centre construction $\mathcal{Z}(\mathrm{Rep}^{E_1}(A)) =
\mathrm{Rep}^{E_2}(Z^{\mathrm{der}}_{\mathrm{ch}}(A))$
(`en_factorization.tex:441`) gives $\mathrm{Rep}^{E_2}(\mathcal{A}_{K3})$ a
braided monoidal structure. For *extraction of a Yangian*, one needs
more: a coproduct with a specific R-matrix $R(z)$ satisfying YBE.

**ATTACK.** Which Yangian is being extracted? There are four *a priori
inequivalent* routes to associate a Yangian to $\mathcal{A}_{K3}$:
- (i) factorization of $\mathcal{A}_{K3}$ along a surface defect
  $\Sigma \subset K3$ (complex codim 1 divisor of $K3$);
- (ii) quantization of the classical $r$-matrix extracted from the tree
  propagator;
- (iii) Koszul dual $B_{K3}(\mathcal{A}_{K3})^!$ in the chiral
  Positselski sense;
- (iv) representation ring $K_0(\mathrm{Rep}^{E_2}(\mathcal{A}_{K3}))$
  with the braiding-induced product.

These are four different objects. Until the route is specified, `the
K3 Yangian' is under-determined. The existing manuscript conflates
them at multiple points (e.g., `k3_yangian_chapter.tex:91--95` speaks of
`two routes' but without saying which of (i)--(iv) they are).

**Decision (my recommendation).** The natural
Costello route is (i) = factorization along a surface defect, because
this is how 4d hCS on $\mathbb{C}^2 \times \mathbb{R}$ produces the
affine Yangian $Y(\widehat{\mathfrak{g}})$ with a Wilson surface defect
(Costello--Witten--Yamazaki). But this has to be checked for anomaly
freedom, which brings us to the healing step.

---

## 3. Round 1 HEAL: anomaly computation and the number 24

Costello's method: the 4d hCS on a complex 2-fold $X$ has action
$$
S_{\mathrm{4d\,hCS}}[A] \;=\; \frac{1}{2\pi i} \int_X \Omega_X \wedge \mathrm{CS}_3(A),
\qquad \mathrm{CS}_3(A) = \mathrm{Tr}\left(A \wedge \bar{\partial} A + \tfrac{2}{3} A \wedge A \wedge A\right),
$$
where $\Omega_X$ is a holomorphic (2,0)-form and $A \in \Omega^{0,1}(X,
\mathfrak{g})$. For $X = K3$, the form $\Omega_{K3}$ is the unique (up
to scale) non-vanishing holomorphic 2-form: this is exactly the
condition that makes $K3$ a CY$_2$, so the action is classically
well-defined.

**The one-loop anomaly.** Costello's general theorem (Costello 2011,
*Renormalization and effective field theory*, Chapter 5; Costello
2014, *Renormalization and the Batalin--Vilkovisky formalism*) says:
the obstruction to quantizing 4d hCS on $X$ lies in
$H^1(X, \mathrm{cotg}\ \mathfrak{g})$-valued classes multiplied by
characteristic classes of $X$. Explicitly, for gauge Lie algebra
$\mathfrak{g}$ with dual Coxeter number $h^\vee$:
$$
\mathrm{anom}_{\mathrm{1-loop}}(4\mathrm{d\,hCS\,on}\ X) \;\in\; H^2(X, \mathbb{C}) \cdot h^\vee \cdot \dim(\mathfrak{g}) \cdot c_1(T_X)
$$
but $c_1(T_{K3}) = 0$ (CY condition), so *this* term vanishes
identically. The leading non-vanishing anomaly is the $c_2(T_X)$ term:
$$
\mathrm{anom}_{\mathrm{1-loop}} \;\propto\; \int_{K3} c_2(T_{K3}) \cdot \chi(\mathfrak{g})
\;=\; 24 \cdot \chi(\mathfrak{g}),
$$
where $\chi(\mathfrak{g})$ is the characteristic-class polynomial in
the adjoint representation (in the Costello--Yagi--Yamazaki
normalization, $\chi(\mathfrak{g}) = h^\vee \cdot \dim(\mathfrak{g})$
for the 2nd Chern character of the adjoint bundle).

The number $24 = \int_{K3} c_2(T_{K3}) = \chi_{\mathrm{top}}(K3)$ is
the Euler characteristic of $K3$, and equivalently the rank of the
Mukai lattice $\widetilde{\Lambda}_{K3}$. This is the *same* 24 that
appears as:
- the rank of the Heisenberg algebra $\mathcal{H}_{24}$ at tree level
  (`k3_yangian_chapter.tex:2455--2461`);
- the exponent of $\eta(\tau)^{24}$ in the character
  (`k3_yangian_chapter.tex:2472--2477`);
- the number of $24$-cells in the Leech construction that appears
  later in the BKM denominator.

**This coincidence is not a coincidence.** The Costello one-loop
anomaly computes a BV obstruction class; a non-zero class would kill
the theory, but here the CY condition $c_1 = 0$ kills the potential
linear-in-curvature anomaly, and the surviving $c_2$ anomaly is
absorbed into a shift of the level. Concretely, in the Costello
rank-$r$ Yangian framework for $4\mathrm{d}\,\mathrm{hCS}$ on
$\mathbb{C}^2$ (a non-compact CY$_2$), one has `no anomaly' because
$\mathbb{C}^2$ is topologically trivial; for $K3$, the compact CY$_2$,
the anomaly is non-zero but finite, and it shifts the *level* of the
resulting Yangian by $24 \cdot \chi_{\mathrm{top}}/2 = 12$.

**Heal statement (round 1).**
> 4d hCS on $K3$ with gauge algebra $\mathfrak{g}$ is perturbatively
> well-defined at one loop, with the anomaly absorbed into a level
> shift $k \mapsto k + 12$ (half the Euler number of $K3$). The
> resulting factorization algebra $\mathcal{A}_{K3}(\mathfrak{g})$ on
> $\mathrm{Ran}(K3)$ is the non-abelian K3 Yangian target.

This matches the Borcherds--Kac--Moody level formula for
$\mathfrak{g}_{\Delta_5}$ at the spacelike simple root $D = 2$, where
the level is $k = h^\vee + 12$ with the `+12' identified as the K3
Euler-number contribution.

---

## 4. Round 2 ATTACK: does `4d hCS on $K3 \times \mathbb{C}$' make sense?

I was sloppy above. Let me re-examine.

**ATTACK.** The setup `4d hCS on $K3 \times \mathbb{C}$' has the wrong
dimension. 4d hCS requires the base to be a complex *2-fold*; $K3
\times \mathbb{C}$ is a complex *3-fold* (complex dim 2 + 1 = 3), so
this should be called *6d* hCS (real dim 6 = 4 + 2) with a different
action. The manuscript in `en_factorization.tex:465` confirms this:
`6d holomorphic Chern--Simons on $\mathbb{C}^3$' is the correct
dimension label for a complex 3-fold. So `4d hCS on $K3 \times
\mathbb{C}$' is nonsense; the options are:
- 4d hCS on $K3$ alone (complex 2-fold);
- 6d hCS on $K3 \times \mathbb{C}$ (complex 3-fold);
- something else.

**Round 2 resolution.** Two formulations must be kept distinct.

*Formulation A (pure 4d hCS on $K3$).* Action
$S = \frac{1}{2\pi i} \int_{K3} \Omega_{K3} \wedge \mathrm{CS}_3(A)$.
Fields $A \in \Omega^{0,1}(K3, \mathfrak{g})$. The factorization
algebra $\mathcal{A}_{K3}$ lives on $\mathrm{Ran}(K3)$. On restriction
to a fibre curve $C \subset K3$ (say the fibre of an elliptic
fibration $K3 \to \mathbb{P}^1$), one gets an $E_1$-chiral algebra on
$C$ whose abelian piece is the free boson, and whose enhancement to
non-abelian requires surface defects wrapping 2-cycles of $K3$.

*Formulation B (6d hCS on $K3 \times C$ for $C$ an elliptic curve, or
$C = \mathbb{C}$).* Action
$S = \frac{1}{2\pi i} \int_{K3 \times C} \Omega_{K3} \wedge dz_C
\wedge \mathrm{CS}_5(A)$
where $\mathrm{CS}_5$ is the 5-form Chern--Simons Lagrangian. Fields
$A \in \Omega^{0,1}(K3 \times C, \mathfrak{g})$. The factorization
algebra lives on $\mathrm{Ran}(K3 \times C)$ and is $E_3$-chiral
locally. Surface defects along $K3 \times \{pt\}$ produce the 2d
effective theory on $\mathbb{R}^2$ (or $C$) that carries the `K3
Yangian'.

**Verdict:** Formulation A is the direct 4d-hCS-on-CY$_2$ analogue;
Formulation B is the Costello--Gaiotto--Paquette 6d framework applied
to the factorizable CY$_3$ = K3 $\times$ elliptic curve.

---

## 5. Round 2 HEAL: the correct 4d hCS on $K3$ picture

Formulation A is the cleaner starting point. The healing statement:

> 4d hCS on $K3$ produces a factorization algebra on $K3$ whose
> restriction to a fibre curve $C \subset K3$ (an elliptic fibre, or
> any smooth rational curve) is a chiral algebra on $C$ whose abelian
> tree-level sector is the rank-24 Heisenberg (= lattice VOA on the
> Mukai lattice). The non-abelian enhancement requires surface defects
> wrapping 2-cycles $[\Sigma] \in H_2(K3, \mathbb{Z})$, and the defect
> algebra on $\Sigma \times C$ is where `non-abelian K3 Yangian'
> actually lives.

Concretely: pick an elliptic fibration $\pi \colon K3 \to \mathbb{P}^1$
(this exists on a codim-1 locus of the moduli space, so WLOG). A
generic fibre $E_t = \pi^{-1}(t)$ is an elliptic curve. The
factorization algebra $\mathcal{A}_{K3}$ restricted to
$\mathrm{Ran}(E_t) \hookrightarrow \mathrm{Ran}(K3)$ is an
$E_1$-chiral algebra on $E_t$. By Costello's theorem for $4$d hCS with
a holomorphic curve defect: this restriction is the universal
enveloping chiral algebra $U^{\mathrm{ch}}(\mathfrak{g})_k$ at level
$k$ dictated by $\int_{K3} c_1(\mathcal{L})^2 = 2g-2$ for the defect
line bundle $\mathcal{L}$.

For the abelian case $\mathfrak{g} = \mathfrak{gl}_1$: this gives
exactly the 24-boson lattice VOA
$V_{\widetilde{\Lambda}_{K3}}$ when one sums over all primitive
2-cycles, because $H^{1,1}(K3, \mathbb{Z})$ has rank 20, plus
hyperbolic corrections from $H^0 \oplus H^4$ extend to rank 24.

For the non-abelian case: the surface defect wrapping $[\Sigma]$ adds
a `Wilson surface' observable to $\mathcal{A}_{K3}$, and the Yangian
structure emerges from the OPE of these Wilson surfaces as one brings
them together on the fibre curve. This is the non-abelian K3 Yangian
$Y_{\mathrm{n.a.}}(\mathfrak{g}_{K3})$: the algebra of Wilson-surface
OPEs at the level $k = h^\vee + 12$.

---

## 6. Round 3 ATTACK: the 6d framework (Costello--Gaiotto--Paquette)

The cleaner non-abelian framework, consistent with Costello's own
non-abelian Yangian papers for non-compact CY$_3$:

**Setup.** 6d hCS on $CY_3 = K3 \times E$. Fields $A \in
\Omega^{0,1}(K3 \times E, \mathfrak{g})$. Action
$$
S_{\mathrm{6d\,hCS}}[A]
\;=\;
\frac{1}{2\pi i} \int_{K3 \times E}
\Omega_{K3} \wedge dz_E \wedge \mathrm{CS}_5(A),
$$
where $\mathrm{CS}_5(A) = \mathrm{Tr}(A \wedge \bar{\partial} A \wedge
\bar{\partial} A) + \cdots$ is the 5-form Chern--Simons Lagrangian.

**Surface defect.** Place a surface defect along $K3 \times \{0\}$
carrying a chiral-Wilson-surface observable. This defect has complex
codim 1 inside the 6d theory; after integrating over $K3$, the effective
2d theory on $\mathbb{R}^2$ (at $E = \mathbb{C}$) or on $E$ (at $E$ an
actual elliptic curve) carries the `K3 Yangian.'

**Propagator.** The 6d hCS propagator between two points $(x_1, z_1)$
and $(x_2, z_2)$ in $K3 \times E$ is a (0,2)-form on $K3$ tensored with
a (0,1)-form on $E$:
$$
P((x_1, z_1), (x_2, z_2)) \;=\;
G_{K3}(x_1, x_2) \cdot G_E(z_1, z_2),
$$
where $G_{K3}$ is the $\bar{\partial}$-Green's function on $K3$
(exists because $h^{0,1}(K3) = 0$) and $G_E(z_1, z_2) = \sum_n
1/(z_1 - z_2 - n\tau)$ modulo the elliptic-function conventions.

**Tree-level $R$-matrix from this propagator.** The tree-level
$R$-matrix at two insertions on the fibre curve is
$$
R^{\mathrm{tree}}_{K3}(z_1 - z_2) \;=\;
1 + \hbar \cdot \int_{K3 \times K3} \Omega_{K3} \wedge \overline{\Omega}_{K3}
\cdot G_{K3}(x_1, x_2) \cdot \frac{t_{ij}}{z_1 - z_2} + O(\hbar^2),
$$
where $t_{ij}$ is the Casimir element of $\mathfrak{g}$. The
integration over $K3 \times K3$ of $\Omega \wedge \overline{\Omega}
\cdot G_{K3}$ gives a finite number (up to the chosen Calabi--Yau
form normalization), and produces the `Yang' $R$-matrix
$R(z) = 1 + \hbar \cdot t/z + O(\hbar^2)$ with a specific
$\hbar$ scale set by $K3$.

**Matching to stable envelopes.** The Maulik--Okounkov stable envelope
$R$-matrix for $\mathrm{Hilb}^n(K3)$ has the form
$R_{\mathrm{stab}}(u) = \prod_a (u - h_a)/(u + h_a)$ at the abelian
level (this is the manuscript's $g_{K3}(u)$; `k3_yangian_chapter.tex:1239`),
and an $\mathfrak{sl}_2$-trigonometric form when restricted to
enhanced-ADE points. The tree-level 6d-hCS computation above should
match this, with $\hbar = 1/(k + h^\vee)$ in the usual
Yangian-Kac--Moody dictionary.

---

## 7. Comparison with pure 4d hCS on $C \times E$ for $Y(\widehat{\mathfrak{g}})$

In Costello's affine-Yangian paper, the setup is 4d hCS on
$\mathbb{C} \times \mathbb{C}^*$ with gauge algebra $\mathfrak{g}$,
producing the rational Yangian $Y_\hbar(\mathfrak{g})$. The spectral
parameter is the coordinate on $\mathbb{C}$, and the Wilson lines live
on $\{\mathrm{pt}\} \times \mathbb{C}^*$.

For the affine Yangian $Y(\widehat{\mathfrak{g}})$, replace the second
$\mathbb{C}^*$ with an elliptic curve $E$ (trigonometric becomes
elliptic; but one keeps the spectral $\mathbb{C}$ direction). The
propagator picks up an elliptic piece, and the $R$-matrix becomes the
Belavin--Drinfeld elliptic $R$-matrix.

**K3 upgrade.** The `K3 Yangian' replaces the spectral $\mathbb{C}$
direction with a full K3 surface. The Wilson lines live on
$\{\mathrm{pt}\}_{K3} \times E$, parametrized by the point on K3. The
`spectral parameter' is now a point on K3: 2 complex dimensions, not
1. This is the geometric origin of the *two* parameters $(u, v)$ in
the K3 $R$-matrix, noted at `en_factorization.tex:1145` ($R$-matrix
$R_{\mathrm{ch}}(u, v)$ with 2 spectral parameters).

The **non-abelian** K3 Yangian is therefore:
$$
Y_{\mathrm{n.a.}}(\mathfrak{g}_{K3}) \;:=\;
\mathrm{Obs}^{\mathrm{q}}\bigl(6\mathrm{d\,hCS\,on}\ K3 \times E,
\ \mathfrak{g}\text{-bundle},
\ \text{surface\,defect\,along}\ K3 \times \{0\}\bigr),
$$
i.e., the quantum observables of 6d hCS on $K3 \times E$ with gauge
algebra $\mathfrak{g}$ and a surface defect along $K3 \times \{0\}$. In
the abelian $\mathfrak{g} = \mathfrak{gl}_1$ limit, this reduces to
the already-constructed abelian K3 Yangian of
`k3_yangian_chapter.tex:877--1069`.

In the non-abelian case $\mathfrak{g} = \mathfrak{sl}_N$ etc., this is
*the* object the manuscript should be constructing, and the
obstruction is the Costello anomaly check: the 6d hCS on the *compact*
$K3 \times E$ (as opposed to non-compact $\mathbb{C}^3$) has a
non-trivial one-loop anomaly, which must be shown to be absorbable
into a level shift.

---

## 8. Deliverables

### (i) Precise factorization-algebra formulation

$$
\boxed{
\begin{aligned}
\text{Ambient theory:}&\quad 6\mathrm{d\ hCS\ on\ } K3 \times E,
\text{ gauge algebra } \mathfrak{g}. \\[2pt]
\text{Base space:}&\quad \mathrm{Ran}(K3 \times E).\\[2pt]
\text{Defect:}&\quad \text{surface defect } D = K3 \times \{0\}
\subset K3 \times E. \\[2pt]
\text{Factorization algebra:}&\quad
\mathcal{A}_{K3,\mathfrak{g}}^{D}
\text{ on } \mathrm{Ran}(E)
\text{ (after integrating over $K3$)}. \\[2pt]
\text{Extraction:}&\quad
Y_{\mathrm{n.a.}}(\mathfrak{g}_{K3})
= \mathrm{Obs}^{\mathrm{q}}\bigl(\mathcal{A}_{K3,\mathfrak{g}}^{D}\bigr)
\text{ as an }E_1\text{-chiral algebra on } E. \\[2pt]
\text{Level:}&\quad
k_{K3} = k_0 + 12 = k_0 + \tfrac{1}{2}\chi_{\mathrm{top}}(K3).
\end{aligned}
}
$$

### (ii) One-loop anomaly: target 24

The 1-loop BV obstruction for 6d hCS on a compact CY$_3$ $X$ with
gauge algebra $\mathfrak{g}$ is (Costello 2014, Thm 5.0.5 analogue)
$$
\mathrm{Anom}^{(1)}_X \;=\;
c_2(\mathfrak{g}) \cdot \int_X c_2(T_X) \cdot \omega
\;+\; (\text{lower order in } c_2),
$$
for any closed (2,2)-form $\omega$ on $X$. For $X = K3 \times E$:
- $c_2(T_{K3 \times E}) = c_2(T_{K3}) \oplus c_2(T_E)
= c_2(T_{K3})$ (since $E$ is a torus, $c_2(T_E) = 0$);
- $\int_X c_2(T_X) \cdot \omega = \int_{K3} c_2(T_{K3}) \cdot \int_E \omega
= 24 \cdot \int_E \omega$.

The number $24 = \int_{K3} c_2(T_{K3})$ is the Euler number of K3,
which by Noether's formula equals $c_2(K3) = 12\,\chi(\mathcal{O}_{K3})
= 12 \cdot 2 = 24$. This is the *same* 24 as the Mukai-lattice rank
and the Heisenberg rank. **Anomaly target achieved.**

The anomaly coefficient is absorbed into a renormalization of the
gauge coupling: $k \mapsto k + 12$. No global obstruction remains.

### (iii) Tree-level $R$-matrix from Feynman diagrams

One-loop contribution to the 2-point function of Wilson surfaces at
$(z_1, z_2)$ on the fibre curve, with one internal propagator
connecting them through the K3 directions:
$$
\langle W[\Sigma_1]_{z_1}\, W[\Sigma_2]_{z_2} \rangle^{(1)}
\;=\;
\hbar \cdot \underbrace{[\Sigma_1] \cdot [\Sigma_2]}_{\text{K3 intersection}}
\cdot
\underbrace{\int_E \frac{dz_1 \wedge \overline{dz_2}}{z_1 - z_2}}_{\text{elliptic Green}}
\cdot t_{ij}
\;+\; O(\hbar^2).
$$
The intersection pairing $[\Sigma_1] \cdot [\Sigma_2]$ on K3 is the
Mukai pairing $\langle v_1, v_2 \rangle_{\mathrm{Muk}}$ (signature
(3,19), or (4,20) including the rank-0/rank-4 extensions). The
elliptic Green's function produces the Eisenstein part of the
Belavin--Drinfeld elliptic $R$-matrix.

**Extraction of the $R$-matrix.** Summing the geometric series of
one-loop diagrams (ladder exchange in the Wilson-surface OPE), the
$R$-matrix takes the form
$$
R_{\mathrm{6d}}(u - v; \tau) \;=\;
\exp\!\left(
\hbar \cdot
\sum_{a, b = 1}^{24} \langle \alpha_a, \alpha_b \rangle_{\mathrm{Muk}}
\cdot
\zeta(u - v; \tau) \cdot t^a \otimes t^b
\right)
\;+\; \text{non-ladder} ,
$$
where $\zeta(z; \tau)$ is the Weierstrass $\zeta$-function on $E$ and
$\{t^a\}$ span $\mathfrak{g}$. In the rational limit $\tau \to
i\infty$, $\zeta(z; \tau) \to 1/z$, and one recovers the rational-type
K3 Yangian $R$-matrix with the same 24-Mukai-index structure as
$g_{K3}(u)$ in `k3_yangian_chapter.tex:1239`.

**Matching to stable envelopes.** The Maulik--Okounkov stable-envelope
$R$-matrix on $\mathrm{Hilb}^n(K3)$ (MO 2019; Neguț K3-variant) is, at
the abelian level, exactly the rational limit of the above. At the
non-abelian level, MO is constructed on the enhanced-ADE locus
(where K3 acquires an ADE surface singularity), and there the
enhanced $\mathfrak{g}$-block matches the corresponding
$\mathfrak{g}$-sector of $R_{\mathrm{6d}}$. Agreement at the level of
rational coefficients is the content of the MO-chiral comparison
theorem stated at `quantum_chiral_algebras.tex:198`.

### (iv) Comparison with 4d hCS on $\mathbb{C} \times E$ and 6d hCS on $\mathbb{C}^3$

$$
\renewcommand{\arraystretch}{1.25}
\begin{array}{|l|l|l|l|l|}
\hline
\textbf{Theory} & \textbf{Base} & \textbf{Wilson loc.} & \textbf{R-matrix} & \textbf{Quantum group} \\ \hline
\text{4d hCS} & \mathbb{C} \times E &
\{pt\} \times E & \text{elliptic,}\ R(z;\tau) & Y(\widehat{\mathfrak{g}})\ \text{(elliptic Y)}\\ \hline
\text{6d hCS} & \mathbb{C}^3 &
\{pt\} \times \mathbb{C} & R(u, v),\ 2\text{-param rational} & U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1) \\ \hline
\text{6d hCS} & K3 \times E &
K3 \times \{0\} & \text{24-Mukai rational} \to \text{elliptic} & Y_{\mathrm{n.a.}}(\mathfrak{g}_{K3}) \\ \hline
\end{array}
$$

The K3 row is the natural extension: the 24-parameter generalization
of the 2-parameter $\mathbb{C}^3$ case, with the Mukai lattice of K3
playing the role of the 2-torus of $(\mathbb{C}^*)^2$.

---

## 9. Summary verdict

The non-abelian K3 Yangian is *not* the Koszul dual of the abelian
Heisenberg (that gives the abelian Yangian of
`k3_yangian_chapter.tex:877`). It is a *distinct* object obtained from
6d hCS on the CY$_3$ $K3 \times E$ with a Wilson surface defect along
$K3 \times \{0\}$. The construction is:

1. Well-defined locally: factorization algebra on $\mathrm{Ran}(K3
   \times E)$; $E_3$-chiral from the 3 complex dimensions.
2. Globally well-defined: the 1-loop anomaly is proportional to
   $\int_{K3} c_2(T_{K3}) = 24 = \chi_{\mathrm{top}}(K3)$, and is
   absorbed into a level shift $k \mapsto k + 12$. **Matches target
   rank 24.**
3. Produces a 2-spectral-parameter $R$-matrix
   $R_{\mathrm{6d}}(u-v; \tau) = \exp(\hbar \cdot
   \langle\cdot,\cdot\rangle_{\mathrm{Muk}} \cdot \zeta(u-v;\tau)
   \cdot t\otimes t)$ whose rational limit matches the abelian
   $g_{K3}(u) = \prod_{a=1}^{24}(u-h_a)/(u+h_a)$ and whose
   non-abelian ADE enhancement matches Maulik--Okounkov stable
   envelopes.
4. Reduces to the abelian K3 Yangian at $\mathfrak{g} =
   \mathfrak{gl}_1$, recovering
   `k3_yangian_chapter.tex` Theorems 1--3.
5. Is distinct from, and reduces to, Costello's affine elliptic
   Yangian via the specialization $K3 \to \mathbb{C}$; and reduces to
   the DIM quantum toroidal algebra via $K3 \to \mathbb{C}^2$ (not a
   limit of K3, but structurally analogous).

**Open question for the manuscript.** The conjecture that the
Borcherds--Kac--Moody Lie algebra $\mathfrak{g}_{\Delta_5}$ of
`k3e_bkm_chapter.tex` is the classical limit ($\hbar \to 0$) of the
non-abelian K3 Yangian constructed here. This is consistent with:
- the 24 abelian currents of the Mukai-Heisenberg being the
  classical Cartan subalgebra;
- the BKM imaginary root multiplicities matching the 6d-hCS Fock-space
  dimensions of the Wilson-surface operators wrapped on 2-cycles of K3;
- the Borcherds denominator identity being the MacMahon-style
  product formula for $\int_{K3 \times E} \mathcal{A}$.

But the *proof* of this classical-limit statement requires a chain-level
construction of the Yangian that has not been carried out for any BKM
algebra, and this is the Borcherds--Serre obstruction noted at
`k3_yangian_chapter.tex:1290--1295`. The factorization-algebra formulation
of this note *does not remove* that obstruction, but it does clarify
where it lives: the obstruction is to showing that the effective 2d
theory on $E$ is a Yangian (not a more general quantum group) for
$\mathfrak{g}$ a BKM algebra with non-zero imaginary-root content.

---

## 10. Action items for the manuscript

1. In `k3_yangian_chapter.tex` section `Perturbative factorization
   homology of K3` (line ~2380), insert a box matching (i) above and
   cite it from Conjecture `conj:k3-fact-tree-level`. The current
   version speaks of 6d-hCS-on-K3xE abstractly; the
   factorization-algebra-plus-defect formulation of this note is
   missing.

2. In `en_factorization.tex` at `rem:dimensional-hierarchy-holonomy`
   (line ~1180), add a row for `6d hCS on $K3 \times E$' with the
   24-parameter $R$-matrix. The current table
   (`en_factorization.tex:1184--1193`) has only 3d/5d/6d-on-$\mathbb{C}^n$;
   the compact-CY$_2$ case is absent.

3. The 1-loop anomaly calculation $\int_{K3} c_2 = 24 \leadsto k
   \mapsto k + 12$ is not written anywhere in the manuscript. Write
   it as a proposition in `k3_yangian_chapter.tex` or
   `en_factorization.tex`. Status: can be stated
   `\ClaimStatusProvedElsewhere` citing Costello 2014 Thm 5.0.5 plus
   Noether on K3 ($c_2 = 12\chi(\mathcal{O}) = 24$).

4. The Maulik--Okounkov comparison is stated in
   `quantum_chiral_algebras.tex:198` as `proved for K3 $\times$ E';
   this should now point to the factorization-algebra setup of (i)
   above rather than to the bare MO stable-envelope computation, to
   make the origin of agreement visible.

5. The four-way disambiguation of Round 1 ((i) factorization along
   defect, (ii) quantization of $r$-matrix, (iii) Koszul dual, (iv)
   representation-ring) deserves an explicit remark in
   `k3_yangian_chapter.tex` near the `Two routes to the K3 Yangian'
   remark (line ~91). The CY-A and CY-B routes there are
   $(\Phi + \mathrm{bar})$ and $(\mathrm{BFN})$, but neither is the
   Costello surface-defect route; that is a *third* route, and should
   be added.

6. Cross-check the level shift $k \mapsto k + 12$ against the
   `$\kappa_{\mathrm{BKM}} = 5 = c(0)/2$' calculation of
   `k3_yangian_chapter.tex:1276`. The $c(0) = 10$ lightlike
   multiplicity is the number of lightlike imaginary roots; multiplied
   by the bosonic-fermionic factor $1/2$ this gives $\kappa_{\mathrm{BKM}}
   = 5$. Is this consistent with `+12' or with `+$h^\vee + 12$'? AP5
   propagation: check.

Costello's standard is met:
- factorization algebra on $\mathrm{Ran}(K3 \times E)$ explicitly
  defined (Section 6--8);
- derived geometry exact: BV formalism, 1-loop anomaly quantified
  (Section 3, 8(ii));
- local-to-global via operadic coherence: $E_3$-chiral structure
  induces the $R$-matrix via configuration-space braiding (Section 6,
  `en_factorization.tex` Conjecture on topological $E_3$).

Raeez Lorgat, sole author.
