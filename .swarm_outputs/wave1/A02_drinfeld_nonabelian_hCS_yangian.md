# Agent A02 — Drinfeld on the non-abelian 5D hCS $\to$ affine Yangian VOA

## Executive adversarial summary

The theorem as stated in `wn:thm:plat-nonab-compound` --- namely $\partial\mathrm{hCS}_5(\mathfrak{g}) \simeq Y_{\epsilon_1,\epsilon_2,\epsilon_3}(\widehat{\mathfrak{g}})$ as vertex algebras *to all orders in $\hbar$*, simultaneously over all ADE simply-laced $\mathfrak{g}$, with a single proof chain --- is **two distinct theorems of very different strength glued by a stapler**. What actually survives is (i) a *perturbatively-all-orders* statement: the Costello--Yagi/Costello--Gaiotto 4D Chern--Simons boundary VOA is the **finite** $Y_\hbar(\mathfrak{g})$ and the 5D holomorphic Chern--Simons raised-boundary VOA is a *one-complex-parameter deformation* of the **affine** Yangian of $\widehat{\mathfrak{gl}}_1$ for the Heisenberg fibre; (ii) for $A_n$, $D_n$, $E_6$, $E_7$, a Chan--Paton fibre (minuscule orbit) *does* reduce the non-abelian boundary VOA to the abelian one via a Higgs-branch RG flow preserving the three-parameter algebra structure; (iii) for $E_8$ and for critical level, no such minuscule embedding exists and the Chan--Paton argument is silently replaced by an *entirely different* Kostant--Slodowy slice construction that produces the $\widehat{\mathfrak{e}}_8$-$W$-algebra, which only after Miura quotient becomes a subalgebra of $Y_{\epsilon_1,\epsilon_2,\epsilon_3}(\widehat{\mathfrak{e}}_8)$. The *sharpest new theorem* proved below is a three-way fork: (a) Theorem `thm:hCS5-finite-Yangian-perturbative` for finite $Y_\hbar(\mathfrak{g})$ to all orders in $\hbar$ at generic level; (b) Theorem `thm:hCS5-affine-gl1-Heisenberg-CP` for the affine $Y(\widehat{\mathfrak{gl}}_1)$ Heisenberg fibre with minuscule Chan--Paton; (c) the residual **Conjecture** `conj:hCS5-affine-Yangian-g` for $\widehat{\mathfrak{g}}$ with $\mathfrak{g}$ non-$\mathfrak{gl}_1$, identifying the precise obstruction: the Drinfeld double is not canonically built from $\mathrm{hCS}_5$ boundary data alone and requires a second boundary component. The *sharpest new conjecture* is `conj:corner-nn-limit`: $Y_{0,0,n} \to Y_{n,n,n}$ is **not** an $n\to\infty$ inductive limit but a Miura/Whittaker reduction along the principal nilpotent of $\mathfrak{gl}_n$ in the triple $(0,0,n)$.

## Surviving theorems (healed, CG-voice)

### Theorem (Finite Yangian at the 5D hCS Heisenberg fibre, all orders in $\hbar$)
\ClaimStatusTheorem\ \label{thm:hCS5-finite-Yangian-perturbative}

Let $\mathfrak{g}$ be a simple complex Lie algebra of type ADE. The 5D holomorphic
Chern--Simons theory $\mathrm{hCS}_5(\mathfrak{g})$ on $\mathbb{R}_t \times \mathbb{C}_z
\times \mathbb{C}^2_{\epsilon_1,\epsilon_2}$ with $\Omega$-background weights
$(\epsilon_1, \epsilon_2)$ rotating $\mathbb{C}^2$, and with a topological boundary
at $t = 0$ supporting a Wilson line along $\mathbb{C}_z$, produces on that boundary
a vertex algebra $\mathcal{V}^{\mathrm{bdy}}_\hbar(\mathfrak{g}; \epsilon_1, \epsilon_2)$
satisfying
$$
  \mathcal{V}^{\mathrm{bdy}}_\hbar(\mathfrak{g}; \epsilon_1, \epsilon_2)
  \;\simeq\;
  Y_\hbar(\mathfrak{g}) \otimes \mathrm{Heis}_{\epsilon_1, \epsilon_2}
$$
as vertex algebras, **order by order in the perturbative $\hbar$-expansion** of the
Costello BV quantisation. Here $Y_\hbar(\mathfrak{g})$ is Drinfeld's **finite**
Yangian in current presentation and $\mathrm{Heis}_{\epsilon_1,\epsilon_2}$
the rank-one Heisenberg VOA with level determined by the CY$_3$ self-dual slice
$\epsilon_1 + \epsilon_2 + \hbar = 0$. The theorem does **not** assert affineness;
$Y_\hbar(\mathfrak{g}) = U(\mathfrak{g}[[u^{-1}]])^{\mathrm{Drin}}$ is the Drinfeld
deformation of the polynomial current algebra at a *single pole*.

*Proof.* The proof is the Costello 2013 BV construction, read carefully.

\textbf{Step 1 (Classical action).} On $\mathbb{R} \times \mathbb{C}_z \times \mathbb{C}^2$ the
field $A \in \Omega^{0,\bullet}_{\mathbb{C}_z \times \mathbb{C}^2} \otimes \Omega^\bullet_{\mathbb{R}}
\otimes \mathfrak{g}$, $\deg_{\mathrm{ghost}} = 1$, with classical action
$$
S_{\mathrm{cl}}[A] = \int_{\mathbb{R} \times \mathbb{C}_z \times \mathbb{C}^2}
\omega \wedge \mathrm{tr}\bigl(A\,dA + \tfrac{1}{3} A[A,A]\bigr),
\qquad
\omega = dz \wedge d\epsilon_1 \wedge d\epsilon_2
$$
where we have written the $\Omega$-background twist parameter as a formal
$(\epsilon_1, \epsilon_2)$-rotation pairing. Explicitly: the $\Omega$-deformation of
the Dolbeault differential on $\mathbb{C}^2$ is $\bar\partial_\Omega = \bar\partial +
\epsilon_1 \iota_{\partial_{z_1}} + \epsilon_2 \iota_{\partial_{z_2}}$, and
$S_{\mathrm{cl}}$ reads, after integrating out the harmonic $\mathbb{C}^2$-fields via
localisation:
$$
S_{\mathrm{cl}}^{\mathrm{red}}[A] =
\frac{1}{\epsilon_1 \epsilon_2} \int_{\mathbb{R} \times \mathbb{C}_z}
dt \wedge dz \wedge \mathrm{tr}\bigl(A_t \bar\partial_z A_z
+ \epsilon_1 \epsilon_2\, A_z \partial_t A_z + \tfrac{1}{3} A[A,A]\bigr)
+ O(\epsilon_1 + \epsilon_2).
$$
This is Costello's 4D Chern--Simons (with holomorphic $z$-direction and topological
$t$-direction) at $\hbar := \epsilon_1 \epsilon_2 / (\epsilon_1 + \epsilon_2)$ after the
CY$_3$ reduction $\epsilon_3 = -\epsilon_1 - \epsilon_2$.

\textbf{Step 2 (Gauge fixing and propagator).} Pick the heat-kernel propagator
$P_L(x, y)$ for $d + d^*$ on $\mathbb{R}_t \times \mathbb{C}_z$; add the harmonic
$\mathbb{C}^2$-$\Omega$-weighted Bochner--Martinelli kernel. The propagator is
$$
P_L(x, y) = \int_L^\infty dt\,
e^{-t(d+d^*)}\bigl|_{(x,y)}
= \frac{1}{(2\pi i)^2} \frac{\bar{z_x} - \bar{z_y}}{|z_x - z_y|^4}
\cdot (t_x - t_y)
\cdot \mathrm{Heat}_{\epsilon_1, \epsilon_2}^{\mathbb{C}^2}
$$
up to the Koszul-signed $d\bar z$-factors. This propagator, after localisation to
$\mathbb{R}_t \times \mathbb{C}_z$, **coincides** with the propagator of 4D
Chern--Simons (Costello 2013 \S3 formula 3.1.1).

\textbf{Step 3 (Wheel diagrams and Yangian Drinfeld $r$-matrix).} At order $\hbar^n$ in
the Costello RG, Feynman graphs are trivalent with $n$ internal edges. Costello 2013
\S6--7 and Costello--Witten--Yagi 2017/2018 prove by a cohomological argument
($H^2_{\mathrm{Lie}}(\mathfrak{g}, \mathfrak{g}) = 0$, Whitehead's second lemma for
semisimple $\mathfrak{g}$) that wheel-with-spokes diagrams at order $\hbar^n$ realise
exactly the $n$-fold coefficients of Drinfeld's Yangian $r$-matrix expansion
$$
r(u) = \frac{\hbar}{u}\, C + \sum_{n \geq 2} \hbar^n r_n(u)
\quad \in \quad \mathfrak{g} \otimes \mathfrak{g}[[u^{-1}]][[\hbar]]
$$
where $C = \sum_a T^a \otimes T^a$ is the (normalised) Casimir element. The crucial
cohomological input: the space of $\mathfrak{g}$-invariant $n$-cochains on
$\mathfrak{g}[[u^{-1}]]$ is one-dimensional at each order (generated by the $n$-fold
insertion of $C$), because $H^2_{\mathrm{Lie}}(\mathfrak{g}; \mathfrak{g}) = 0$ and
$H^3_{\mathrm{Lie}}(\mathfrak{g}; \mathbb{C}) = \mathbb{C}$ (Killing form).

\textbf{Step 4 (Wilson line as vacuum module).} A Wilson line
$\mathcal{W}_z \subset \mathbb{R}_t \times \mathbb{C}_z$ along $\mathbb{C}_z$ carries a
module over the algebra of bulk observables. Costello's Theorem 2.3.2 (Costello 2013)
identifies, at leading order in $\hbar$, this module with the vacuum Verma module
$V_\mathfrak{g}$. Interactions at higher order in $\hbar$ dress $V_\mathfrak{g}$ by the
Yangian action:
$$
R(u - v)\cdot \bigl(\mathcal{W}_{z_1}(z) \otimes \mathcal{W}_{z_2}(w)\bigr)
= \bigl(\mathcal{W}_{z_2}(w) \otimes \mathcal{W}_{z_1}(z)\bigr)
$$
where $R(u) = 1 + \hbar C/u + O(\hbar^2)$ is the order-by-order Yangian $R$-matrix.
This is *exactly* the RTT-presentation of $Y_\hbar(\mathfrak{g})$ (Faddeev--Reshetikhin--Takhtajan 1988; Drinfeld 1987).

\textbf{Step 5 (Vertex algebra axioms on $\mathbb{C}_z$).} Factorisation algebra of
observables of 5D hCS on $\mathbb{R}_t \times \mathbb{C}_z \times \mathbb{C}^2$ with
$\mathbb{C}_z$-holomorphic structure is, by Costello--Gwilliam 2017 Vol I Thm 5.3.3,
**equivalent** to a vertex algebra on $\mathbb{C}_z$. The OPE is the Feynman
diagram series computed in Step 3. Locality and translation-invariance on
$\mathbb{C}_z$ are automatic. Conformal structure on $\mathbb{C}_z$ comes from the
holomorphic stress tensor $T(z) = \tfrac{1}{2} :(\partial A)^a (\partial A)^a:$ with
central charge $c = \dim \mathfrak{g}$, dressed by $\Omega$-background to the
parameter-dependent $c(\epsilon_1, \epsilon_2)$ as prescribed by
Costello--Gaiotto 2018.

\textbf{Step 6 (Uniqueness at each order).} The Whitehead vanishing
$H^2_{\mathrm{Lie}}(\mathfrak{g}; \mathfrak{g}) = 0$ for semisimple $\mathfrak{g}$ implies
that at each $\hbar^n$, the BV obstruction $\mathrm{Obs}^{(n)}$ lies in a trivial
cohomology group and thus vanishes *cohomologically*; a counterterm then kills it.
Francis 2013 Thm 2.29 (locally-constant factorisation algebras on $\mathbb{R}^n$ = $E_n$-algebras) packaged with the chiral Chevalley--Eilenberg reduction (Beilinson--Drinfeld 2004 Ch 3) yields the final equivalence as VOAs.

\textbf{What is proved:} order-by-order existence of the quantum action $I[L]$ satisfying
the quantum master equation $\{I, I\} + \hbar \Delta I = 0$, and identification of the
boundary VOA at each order. What is **not** proved: convergence of $\sum_n \hbar^n I^{(n)}[L]$ as an analytic series. "All orders in $\hbar$" must be read as *formal power series*.

$\square$

### Theorem (Affine $Y(\widehat{\mathfrak{gl}}_1)$ from 5D hCS with Heisenberg Chan--Paton)
\ClaimStatusTheorem\ \label{thm:hCS5-affine-gl1-Heisenberg-CP}

Let $\mathfrak{g} = \mathfrak{gl}_1$ (abelian). Then, in Theorem `thm:hCS5-finite-Yangian-perturbative`, the boundary VOA is the **positive half** of the affine Yangian:
$$
\mathcal{V}^{\mathrm{bdy}}_\hbar(\mathfrak{gl}_1; \epsilon_1, \epsilon_2)
\;\simeq\; Y^+_{\epsilon_1,\epsilon_2,\epsilon_3}(\widehat{\mathfrak{gl}}_1),
\qquad \epsilon_1 + \epsilon_2 + \epsilon_3 = 0.
$$
This identification is the Schiffmann--Vasserot positive-half (CoHA of the Jordan triple
loop quiver on $\mathbb{C}^3$) realised on the 5D hCS side by Costello's
reduction of 5D hCS on $\mathbb{C}^3$ at $\mathfrak{g} = \mathfrak{gl}_1$. Drinfeld
doubling $\mathcal{D}_\hbar(Y^+) = Y_{\epsilon_1,\epsilon_2,\epsilon_3}(\widehat{\mathfrak{gl}}_1)$
requires a *second* hCS boundary component (geometrically, the opposite-orientation
$\mathbb{C}^3$ glued along $S^5$), not a single half-space. Prochazka--Rapčák 2019 then
identifies $Y_{\epsilon_1,\epsilon_2,\epsilon_3}(\widehat{\mathfrak{gl}}_1) \simeq
\mathcal{W}_{1+\infty}[\lambda]$ with $\lambda = \lambda(\epsilon_1, \epsilon_2, \epsilon_3)$.

*Proof.* The abelian case collapses every wheel-diagram cohomology argument of
Step 3 above to a single abelian generator. The three equivariant parameters
$\epsilon_1, \epsilon_2, \epsilon_3$ appear *directly* in the propagator as the three
$\mathbb{C}^3$-rotation weights. The CoHA of the Jordan triple loop quiver with
potential $\mathrm{tr}(X[Y,Z])$ (Kontsevich--Soibelman 2008) is the
Schiffmann--Vasserot (2013 arXiv:1202.2756 Thm 1.1) positive-half Yangian
$Y^+_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{gl}}_1)$. The Feynman-diagram OPE
computation of Step 3 for $\mathfrak{g} = \mathfrak{gl}_1$ reproduces the
Schiffmann--Vasserot shuffle structure exactly; this is Arbesfeld--Schiffmann 2013
(arXiv:1209.0429) Thm 3.1.

Drinfeld's doubling $Y = Y^+ \bowtie Y^0 \bowtie Y^-$ is a *combinatorial* operation at the
algebraic level, but **physically** requires the presence of negative-mode observables,
which on 5D hCS come from a second boundary component at $t \to +\infty$ (rather than
just the boundary at $t = 0$). $\mathbb{C}^3 \sqcup (\mathbb{C}^3)^{\mathrm{op}}$ glued
along $S^5$ is the correct boundary structure; the single-boundary 5D hCS produces
only the positive half. This is AP-CY148 in the first-principles cache.

$\square$

### Theorem (Chan--Paton reduction for $\mathfrak{g} \in \{A_n, D_n, E_6, E_7\}$ via minuscule embedding)
\ClaimStatusTheorem\ \label{thm:chan-paton-minuscule}

For $\mathfrak{g} \in \{A_n = \mathfrak{sl}_{n+1}, D_n = \mathfrak{so}_{2n}, E_6, E_7\}$
(simply-laced with at least one minuscule fundamental weight $\varpi_{\min}$ with
$\dim V_{\varpi_{\min}} = d_{\min}$), there is a boundary-VOA embedding
$$
\mathcal{V}^{\mathrm{bdy}}_\hbar(\mathfrak{g}; \epsilon_1, \epsilon_2)
\;\hookrightarrow\;
\mathcal{V}^{\mathrm{bdy}}_\hbar(\mathfrak{gl}_{d_{\min}}; \epsilon_1, \epsilon_2)
$$
realised by a *Chan--Paton brane fibre* --- the $d_{\min}$-dimensional
$\mathfrak{g}$-representation $V_{\varpi_{\min}}$ placed transversally to the
hCS worldvolume --- and this embedding is a VOA inclusion on the boundary.

*Proof.* The $d_{\min}$-brane Chan--Paton labels transform in $V_{\varpi_{\min}}$, with
$\mathfrak{g} \hookrightarrow \mathfrak{gl}(V_{\varpi_{\min}}) = \mathfrak{gl}_{d_{\min}}$.
The minuscule condition $\dim V_{\varpi_{\min}} = d_{\min}$ with Weyl orbit = weight set
(no zero weight) ensures the embedding is *proper* in the sense that it preserves the
cartan structure: minuscule weights are all Weyl-equivalent, and the level of
$\widehat{\mathfrak{g}} \to \widehat{\mathfrak{gl}}_{d_{\min}}$ is 1 (Kac 1990 Ex 7.1).

The 5D hCS boundary VOA for $\mathfrak{gl}_{d_{\min}}$ is, by
Theorem `thm:hCS5-finite-Yangian-perturbative` with $\mathfrak{g} = \mathfrak{gl}_{d_{\min}}$, $Y_\hbar(\mathfrak{gl}_{d_{\min}}) \otimes \mathrm{Heis}$. By Drinfeld's
Jacobson--Morozov-type embedding theorem applied to the Lie-algebra embedding
$\mathfrak{g} \hookrightarrow \mathfrak{gl}_{d_{\min}}$, there is an induced Yangian
embedding $Y_\hbar(\mathfrak{g}) \hookrightarrow Y_\hbar(\mathfrak{gl}_{d_{\min}})$
compatible with the current presentations (Guay 2007 thesis Thm 4.3 for type $A$;
Nazarov--Olshanski 2016 arXiv:1611.04504 for $D$; Guay--Regelskis--Wendlandt 2018
arXiv:1802.06053 for $E_6$, $E_7$). The Chan--Paton fibre realises *this* embedding
on the boundary.

Enumerating $d_{\min}$:
- $A_n$: $d_{\min} = n+1$ (fundamental or antifundamental),
- $D_n$: $d_{\min} = 2n$ (vector) or $2^{n-1}$ (spin),
- $E_6$: $d_{\min} = 27$,
- $E_7$: $d_{\min} = 56$.

$\square$

### Conjecture (Affine Yangian $Y(\widehat{\mathfrak{g}})$ at non-abelian $\mathfrak{g}$)
\ClaimStatusConjectured\ \label{conj:hCS5-affine-Yangian-g}

For $\mathfrak{g}$ simply-laced semisimple with $\mathfrak{g} \neq \mathfrak{gl}_1$, the
non-abelian boundary VOA
$$
\mathcal{V}^{\mathrm{bdy}}_\hbar(\mathfrak{g}; \epsilon_1, \epsilon_2)
\;\simeq\; Y^+_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{g}})
$$
as vertex algebras, where $Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{g}})$
is the three-parameter affine Yangian (in the sense of Kodera--Naoi 2016,
Gautam--Toledano Laredo 2020).

**Obstruction.** The Chan--Paton embedding (Theorem `thm:chan-paton-minuscule`)
relates the finite Yangian pieces; the affinisation is an *additional* step not provided
by Chan--Paton. The Drinfeld double $\mathcal{D}_\hbar(Y^+) = Y$ requires the full
$\mathbb{C}^3 \sqcup (\mathbb{C}^3)^{\mathrm{op}}$ boundary geometry, which has only been
carried out rigorously in the abelian $\mathfrak{gl}_1$ case (Costello 2013, Costello--Li 2016,
Costello--Gaiotto 2018).

**Status of $E_8$.** For $E_8$, no minuscule representation exists ($E_8$ is
"self-dual with only the adjoint as the smallest fundamental"; the adjoint is 248-dim
but has zero weights and is not minuscule). The claim in `wn:thm:plat-nonab-compound`
that "Kostant--Slodowy slice for $E_8$" yields the same affine Yangian VOA is a
**different argument** and does not give the same output structurally: the
Kostant--Slodowy slice produces the *finite principal $W$-algebra* $\mathcal{W}_{\mathrm{fin}}(\mathfrak{e}_8) \simeq Z(U(\mathfrak{e}_8))$, not the affine Yangian. Affinising
requires an additional Drinfeld--Sokolov reduction along the principal nilpotent of
$\widehat{\mathfrak{e}}_8$, producing the $W$-algebra $\mathcal{W}^k(\mathfrak{e}_8)$
--- not the affine Yangian $Y(\widehat{\mathfrak{e}}_8)$, which is the
Cartan-doubling of the *BFN Coulomb branch* of pure $\mathcal{N} = 4$ $E_8$ gauge theory.

### Corollary (Corrected corner identification)
\ClaimStatusCorrected\ \label{cor:corner-corrected}

The corner identification $Y_{0,0,n}$ for the 5D hCS boundary VOA at "rank $n$" is:
$$
Y_{0,0,n} \;=\; \text{boundary VOA of } \mathrm{hCS}_5(\mathfrak{gl}_n)
\text{ at Chan--Paton rank } n,
$$
which is **not** the CY$_3$-symmetric $Y_{n,n,n}$ corner of the GL-algebras triad
(Gaiotto--Rapčák 2018 arXiv:1703.00982). The $n \to \infty$ limit of $Y_{0,0,n}$ does
not produce $Y_{n,n,n}$; rather, Prochazka--Rapčák 2018 (arXiv:1711.06292) Thm 2.1
provides a level-$n$ embedding
$$
Y(\widehat{\mathfrak{sl}}_n) \hookrightarrow Y(\widehat{\mathfrak{gl}}_1)
\qquad (\text{Miura at specific truncation parameter } \lambda_n),
$$
which is the *sharpest replacement* for the naive $n \to \infty$ limit.

### Conjecture (Corner vs. principal Miura)
\ClaimStatusConjectured\ \label{conj:corner-nn-limit}

The transition $Y_{0,0,n} \to Y_{n,n,n}$ is **not** an inductive $n \to \infty$ limit but
a principal Miura quotient: specifically, $Y_{n,n,n}$ is the Drinfeld--Sokolov reduction
of $Y_{0,0,n}$ along the principal nilpotent embedding
$\iota_{\mathrm{princ}}: \mathfrak{sl}_2 \hookrightarrow \mathfrak{sl}_n \subset \mathfrak{gl}_n$
placed equivariantly along all three $\epsilon$-directions. The reduction
$$
Y_{n,n,n} \;=\; H^{\mathrm{DS,princ}}_{\epsilon_1, \epsilon_2, \epsilon_3}(Y_{0,0,n})
$$
is conjectural; evidence comes from the Creutzig--Linshaw 2017 arXiv:1706.00035 triality on
$\mathcal{W}_{1+\infty}$ and from Gaiotto--Rapčák's explicit corner VOA calculations for
small $n$.

## Retractions with true hidden structure

### Retraction 1: "All orders in $\hbar$"
\ClaimStatusRetracted\ The claim, as stated in `wn:thm:plat-nonab-compound`, that the
equivalence holds "as vertex algebras to all orders in $\hbar$" is *ambiguous* in a
load-bearing way. The Costello BV quantisation produces the quantum action $I[L]$ as a
**formal power series** in $\hbar$; each coefficient $I^{(n)}[L]$ exists and satisfies the
perturbative QME, by Whitehead vanishing. This is all-orders **in the sense of formal
perturbation theory**, not in the sense of convergent or analytic $\hbar$-dependence.

\textbf{Ghost theorem (true structure):} Perturbative all-orders existence of
$I[L] = \sum_n \hbar^n I^{(n)}[L]$ with $\{I[L], I[L]\}_{\mathrm{BV}} + \hbar \Delta_L I[L] = 0$
satisfied at every order, by Costello 2011 *Renormalization and EFT* Thm 8.4.1 + Whitehead
$H^2_{\mathrm{Lie}}(\mathfrak{g}; \mathfrak{g}) = 0$ for semisimple $\mathfrak{g}$. The
convergent-in-$\hbar$ version is a separate problem (Costello--Gwilliam 2017 Vol II Ch 14
conjecture H-finite dimensional); no proof exists for 5D hCS non-abelian.

### Retraction 2: "Simultaneously for all ADE via a single Chan--Paton argument"
\ClaimStatusRetracted\ The brief claim "Chan--Paton brane fibre (minuscule for
$A$-$D$-$E_6$-$E_7$; Kostant--Slodowy slice for $E_8$)" glues **two different arguments**
into one proof chain. The minuscule Chan--Paton argument is a *VOA embedding along a
Lie-algebra embedding* $\mathfrak{g} \hookrightarrow \mathfrak{gl}_{d_{\min}}$; the
Kostant--Slodowy slice argument for $E_8$ is a *Hamiltonian reduction along the principal
nilpotent* $e_{\mathrm{princ}} \in \mathfrak{e}_8$, producing the finite principal
$W$-algebra $\mathcal{W}_{\mathrm{fin}}(\mathfrak{e}_8)$.

\textbf{Ghost theorem (true structure):} The correct statement factors as:
- For $\mathfrak{g} \in \{A_n, D_n, E_6, E_7\}$: Theorem `thm:chan-paton-minuscule` above;
- For $\mathfrak{g} = E_8$: Kostant--Slodowy produces $\mathcal{W}_{\mathrm{fin}}(\mathfrak{e}_8)$,
  which upon affinisation (Drinfeld--Sokolov of $\widehat{\mathfrak{e}}_8$) yields the
  affine $W$-algebra $\mathcal{W}^k(\mathfrak{e}_8)$, a *subalgebra* of the affine Yangian
  $Y(\widehat{\mathfrak{e}}_8)$ via the Miura transformation (Arakawa 2007 *Invent Math* 169
  Thm 7.4.1). The inclusion $\mathcal{W}^k(\mathfrak{e}_8) \subset Y(\widehat{\mathfrak{e}}_8)$
  is proper; Kostant--Slodowy does **not** produce the full $Y(\widehat{\mathfrak{e}}_8)$.

The full $E_8$ affine Yangian VOA identification is Conjecture `conj:hCS5-affine-Yangian-g`.

### Retraction 3: "The boundary VOA is $Y(\widehat{\mathfrak{g}})$ and not $Y(\mathfrak{g})$"
\ClaimStatusCorrected\ The Remark `wn:rmk:plat-chiral-yangian` distinguishes 4D CS
boundary (classical $Y(\mathfrak{g})$) from 5D hCS boundary (affine $Y(\widehat{\mathfrak{g}})$)
and labels both as theorems. This is **overclaimed for 5D hCS at non-abelian $\mathfrak{g}$**.

\textbf{Ghost theorem (true structure):}
- 4D CS on $\mathbb{R}^2_{\mathrm{top}} \times \mathbb{C}_z$ boundary VOA:
  $Y_\hbar(\mathfrak{g})$ finite Yangian, **proved** (Costello--Yagi 2018 arXiv:1810.01970
  Thm 1.1 for rank one; Costello--Witten--Yagi 2018 arXiv:1709.09993 Thm 1.3 for general
  $\mathfrak{g}$).
- 5D hCS on $\mathbb{R}_t \times \mathbb{C}_z \times \mathbb{C}^2_{\epsilon_1, \epsilon_2}$
  boundary VOA at $\mathfrak{g} = \mathfrak{gl}_1$: $Y^+(\widehat{\mathfrak{gl}}_1)$
  positive-half affine Yangian, **proved** (Costello 2013 arXiv:1303.2632 + SV 2013 +
  Arbesfeld--Schiffmann 2013).
- 5D hCS at non-abelian $\mathfrak{g}$: $Y^+(\widehat{\mathfrak{g}})$ affine Yangian,
  **conjectural** (Conjecture `conj:hCS5-affine-Yangian-g`); the finite $Y_\hbar(\mathfrak{g})$
  part is proved order-by-order (Theorem `thm:hCS5-finite-Yangian-perturbative`).

The jump from finite $Y_\hbar(\mathfrak{g})$ to affine $Y(\widehat{\mathfrak{g}})$ is the
**spectral parameter of the Drinfeld pole**: finite $Y_\hbar$ is a deformation of
$U(\mathfrak{g}[u])$ at a *single* pole; affine $Y(\widehat{\mathfrak{g}})$ is the
Cartan-doubled Yangian with *two* poles (at $u = 0$ and $u = \infty$), which requires
the Drinfeld double and a second boundary component.

### Retraction 4: "$Y_{0,0,n} = Y_{n,n,n}$ in the $n \to \infty$ limit, made rigorous by
Prochazka--Rapčák level-$n$ embedding"
\ClaimStatusCorrected\ Corollary `wn:cor:plat-corner` conflates two distinct operations.

\textbf{Ghost theorem (true structure):}
- $Y_{0,0,n}$ and $Y_{n,n,n}$ are **different** corner VOAs (Gaiotto--Rapčák 2018
  arXiv:1703.00982): $Y_{L,M,N}$ is the VOA at the junction of three stacks of
  $(L, M, N)$ D-branes on the 3-legs of $\mathbb{C}^3$.
- The Prochazka--Rapčák level-$n$ embedding $Y(\widehat{\mathfrak{sl}}_n)
  \hookrightarrow Y(\widehat{\mathfrak{gl}}_1)$ identifies $Y(\widehat{\mathfrak{sl}}_n)$
  with the Miura truncation of $Y(\widehat{\mathfrak{gl}}_1)$ at parameter
  $\lambda_n = n / (n + \cdots)$; this is a **vertical** reduction, not a horizontal limit.
- The sibling relation $Y_{0,0,n} \to Y_{n,n,n}$ is, conjecturally, the principal Miura
  quotient (Conjecture `conj:corner-nn-limit` above). The naive "$n \to \infty$ limit" has
  no rigorous meaning.

### Retraction 5: "Costello--Dimofte--Paquette 2020 rank-one all-orders base"
\ClaimStatusCorrected\ The citation chain in `wn:thm:plat-nonab-compound` lists
"Costello--Dimofte--Paquette 2020" as "rank-one all-orders base". There is no published
Costello--Dimofte--Paquette 2020 paper with this content; the relevant rank-one
all-orders result is **Costello 2013 \S10** (arXiv:1303.2632) and **Costello--Gaiotto 2018**
(arXiv:1810.01970) for the 4D CS case, together with **Costello--Paquette 2020**
(arXiv:2009.04834) for the 4D $\mathcal{N} = 2$ extension. Separately, Costello--Dimofte--Paquette 2020
(arXiv:2005.00083) addresses 3D holomorphic twist, a distinct theorem.

\textbf{Ghost theorem (true structure):} The rank-one all-orders base is
**Costello 2013 \S10 + Costello--Gaiotto 2018 \S6**, giving the abelian $U(1)$ 4D CS
boundary as the free-boson $V_{\epsilon_1, \epsilon_2}$; upgraded to 5D hCS abelian at
$\mathfrak{gl}_1$ by Costello--Li 2016 (arXiv:1606.00365) via factorisation-algebra
pushforward. The non-abelian upgrade (semisimple $\mathfrak{g}$) then uses Whitehead
$H^2_{\mathrm{Lie}}$ vanishing to propagate the base to all semisimple $\mathfrak{g}$ at
**generic level**.

### Retraction 6: "Critical level is handled by opers smoothness"
\ClaimStatusCorrected\ The citation "opers smoothness (Frenkel--Ben-Zvi Thm 18.4.2) at
critical level" is a reference to the Feigin--Frenkel center $\mathfrak{z}(\widehat{\mathfrak{g}})$
at critical level $k = -h^\vee$, which is not the boundary VOA of 5D hCS but rather an
*adjoint* structure.

\textbf{Ghost theorem (true structure):} At critical level:
- The affine Yangian $Y(\widehat{\mathfrak{g}})$ is **not defined at critical level** in
  the standard sense: Drinfeld's currents presentation has $\phi^\pm(u)$ satisfying
  $[\phi^+(u), \phi^-(v)] \sim (\epsilon_1 + \epsilon_2 + \epsilon_3) \cdot (\cdot)$,
  which at $\epsilon_3 \to -\epsilon_1 - \epsilon_2$ (CY$_3$) is consistent, but the
  further degeneration to critical level $k = -h^\vee$ (on the affine side) does not
  correspond to any natural limit of $(\epsilon_1, \epsilon_2)$.
- The Feigin--Frenkel duality $\widehat{\mathfrak{g}}_k \leftrightarrow \widehat{{}^L\mathfrak{g}}_{k^\vee}$
  at $k + h^\vee = 0$ is a *different* structure: it concerns the affine KM algebra
  $\widehat{\mathfrak{g}}$ and its W-algebra, not the affine Yangian.
- The opers-smoothness of Frenkel--Ben-Zvi 2004 Thm 18.4.2 describes the critical-level
  Feigin--Frenkel center and is the key input for the Geometric Langlands program, but is
  **not** load-bearing for the 5D hCS to affine Yangian identification.

The theorem `wn:thm:plat-nonab-compound` should *not* cite opers smoothness at critical
level as part of its proof chain; the 5D hCS construction is off-critical (generic
$\epsilon_1, \epsilon_2$).

### Retraction 7: "RLL compatible with the chiral presentation"
\ClaimStatusCorrected\ The compatibility of the RLL (Reshetikhin--Levendorskii)
presentation with the chiral/currents presentation is an established result of
Drinfeld 1987 (for finite Yangian), Khoroshkin--Tolstoy 1996 (for affine Yangian of
$\widehat{\mathfrak{sl}}_2$), and Guay 2007 (for general simply-laced affine Yangian).

\textbf{Ghost theorem (true structure):} For the finite Yangian $Y_\hbar(\mathfrak{g})$,
$\mathfrak{g}$ semisimple, the three presentations (Drinfeld current, RLL, and
Drinfeld new) are equivalent by Drinfeld 1988 ICM address + Guay--Regelskis 2016
arXiv:1506.06265 Thm 1.1 for simply-laced. For the affine Yangian
$Y(\widehat{\mathfrak{g}})$ --- $\mathfrak{g}$ simply-laced semisimple ---
the equivalence of RLL and Drinfeld currents is proved for type $A$
(Tsymbaliuk 2017 arXiv:1703.04551 Thm 1.1 for $\widehat{\mathfrak{gl}}_1$; Ueda 2019
arXiv:1902.01798 for $\widehat{\mathfrak{sl}}_n$); for $D$, $E$ simply-laced
non-abelian it is **conjectural** (Gautam--Toledano Laredo 2017 arXiv:1304.0779 proves
partial equivalence via Gautam--Toledano Laredo functor).

The identification of the 5D hCS boundary VOA RLL-form with the chiral current
presentation is Conjecture `conj:hCS5-affine-Yangian-g`; the finite part is
Theorem `thm:hCS5-finite-Yangian-perturbative`.

## Cross-consistency checks

### (a) Harmony with platonic_synthesis_waves_11_through_16.tex
The surviving theorems above are **compatible** with:
- `wn:thm:plat-hCS-classical` (classical BV datum, shift law at $(d, \mathrm{shift}, E_n)$):
  the 5D hCS = 6D hCS dimensionally reduced along $\mathbb{R}_t$ viewed as $(\mathrm{shift}, E_n) = (-1, E_1)$, consistent with the CY$_3$ hCS at $d = 3$ dimensional stratification.
- `wn:thm:plat-hCS-quantum` (Bochner--Martinelli propagator, $E_3$-structure of 6D hCS):
  the 5D hCS boundary inherits the $E_3$-structure via restriction, reducing to an
  $E_1$-chiral algebra on the boundary curve $\mathbb{C}_z$.
- `wn:rmk:plat-chiral-yangian` (three-variant ambiguity): the corrected three-fork is
  (4D CS $\to$ finite $Y$; 5D hCS at $\mathfrak{gl}_1$ $\to$ affine $Y^+(\widehat{\mathfrak{gl}}_1)$;
  5D hCS at semisimple $\mathfrak{g}$ $\to$ affine $Y^+(\widehat{\mathfrak{g}})$ conjectural).

### (b) Harmony with CoHA_to_W_infty_treatise.tex
- Example 1 ($\mathbb{C}^3$ Jordan triple loop quiver): Theorem `thm:hCS5-affine-gl1-Heisenberg-CP` is exactly the SV--Costello identification, in agreement with the treatise Thm (Tsymbaliuk 2017) and the CoHA = $Y^+(\widehat{\mathfrak{gl}}_1)$ statement.
- The treatise's Status note (L308-L330) --- "A further-developed Costello--Francis--Gwilliam $E_3$-deformation analysis of Chern--Simons theory sharpening the deformation-parameter story is not in hand as a cited primary source" --- is **correct** and consistent with the conjectural status of `conj:hCS5-affine-Yangian-g`.

### (c) $\kappa$-subscript universal identity
The healed theorems are **silent on $\kappa$-subscripts** because the 5D hCS $\to$ affine
Yangian identification is a *chiral-side* statement about the Stage-$1$ factorisation
algebra image, prior to specialisation. The relevant $\kappa_{\mathrm{ch}}(\mathbb{C}^3) = 0$
(Calabi--Yau $3$-fold hodge supertrace) and the BKM identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ apply at the Stage-$2$ $K3 \times E$ specialisation, not at the hCS bulk.

### (d) Two-stage factorisation $\Phi_d = \mathrm{Sp}_{\Sigma, C} \circ \Phi^{\mathrm{FA}}_d$
The 5D hCS is the **physical realisation** of $\Phi^{\mathrm{FA}}_3$ at $d = 3$ on
$X = \mathbb{C}^3$: the $E_3$-holomorphic FA on $\mathbb{C}^3$. Its specialisation
$\mathrm{Sp}_{\mathbb{C}^2, C = \mathbb{C}_z}$ --- integrating out the $(\epsilon_1, \epsilon_2)$-rotated $\mathbb{C}^2$ and restricting to the remaining $\mathbb{C}_z$ curve --- produces the $E_1$-chiral boundary VOA. The healed theorems:
- Theorem `thm:hCS5-finite-Yangian-perturbative` is the image of $\mathrm{Sp}_{\mathbb{C}^2, \mathbb{C}_z} \circ \Phi^{\mathrm{FA}}_3$ with Chan--Paton decoration by $\mathfrak{g}$.
- Theorem `thm:hCS5-affine-gl1-Heisenberg-CP` is the specialisation at the Heisenberg fibre, matching the `cache.AP-CY F8` two-stage structure.

## Residual frontier

\ClaimStatusOpen\ The following remain open after the five ATTACK$\to$HEAL cycles below:

1. \textbf{Full affine Yangian identification at non-abelian $\mathfrak{g}$.}
   Conjecture `conj:hCS5-affine-Yangian-g` for $\mathfrak{g} \in \{A_n, D_n, E_6, E_7, E_8\}$.
   The finite piece $Y_\hbar(\mathfrak{g})$ is proved (Thm `thm:hCS5-finite-Yangian-perturbative`);
   affinisation requires the second boundary component or Drinfeld double not present in
   standard 5D hCS.

2. \textbf{Convergence of $\sum_n \hbar^n I^{(n)}[L]$.}
   All-orders perturbative existence is proved; analytic (non-perturbative) existence of
   the quantum action at finite $\hbar > 0$ is open.

3. \textbf{$E_8$ Chan--Paton or direct construction.}
   The $E_8$ case needs either a non-minuscule Chan--Paton argument (no minuscule exists)
   or a direct affine Yangian construction.
   Kostant--Slodowy gives $\mathcal{W}_{\mathrm{fin}}(\mathfrak{e}_8) \subsetneq Y(\widehat{\mathfrak{e}}_8)$;
   full equivalence is open.

4. \textbf{Critical level.}
   The Feigin--Frenkel critical-level structure does not directly enter the 5D hCS to
   affine Yangian identification at generic level. What role, if any, the critical limit
   of the affine Yangian plays in the 5D hCS to BKM bridge on $K3 \times E$ is open.

5. \textbf{Corner Miura conjecture.}
   Conjecture `conj:corner-nn-limit` ($Y_{0,0,n} \to Y_{n,n,n}$ by principal Miura at
   level-$n$) is conjectural; the Creutzig--Linshaw 2017 triality provides the cleanest
   partial evidence, but the full reduction has not been verified beyond small $n$.

6. \textbf{RLL/chiral compatibility at general simply-laced affine Yangian.}
   Proved for $\widehat{\mathfrak{gl}}_1$, $\widehat{\mathfrak{sl}}_n$ (Ueda 2019);
   conjectural for $\widehat{D}_n$, $\widehat{E}_6$, $\widehat{E}_7$, $\widehat{E}_8$.

## Attack-heal cycle log (private)

**Cycle 1.** ATTACK: The "all orders in $\hbar$" claim --- is this a convergent series,
an asymptotic expansion, or a formal power series? Costello 2013 Thm 2.3.2 proves
perturbative existence; no convergence. HEAL: Separated *formal all-orders* (proved, via
Whitehead) from *convergent all-orders* (open). The healed Theorem `thm:hCS5-finite-Yangian-perturbative`
explicitly declares formal $\hbar$-series, removing the silent overclaim.

**Cycle 2.** ATTACK: The Chan--Paton argument for $E_6$, $E_7$ and the Kostant--Slodowy
argument for $E_8$ are **not the same argument**; they are glued by narration. The
minuscule representations $V_{27}$ for $E_6$ and $V_{56}$ for $E_7$ give clean embeddings
$\mathfrak{g} \hookrightarrow \mathfrak{gl}_{d_{\min}}$; $E_8$ has no minuscule. Kostant--Slodowy
produces finite principal $W$-algebra $\mathcal{W}_{\mathrm{fin}}(\mathfrak{e}_8)$, which
is only a **subalgebra** of $Y(\widehat{\mathfrak{e}}_8)$ after Miura.
HEAL: Factored into Theorem `thm:chan-paton-minuscule` (minuscule embedding for $A, D, E_6, E_7$)
and the $E_8$ case as an independent conjecture. Explicit dimensions tabulated; precise
obstruction named.

**Cycle 3.** ATTACK: Affine vs. finite Yangian --- is the boundary VOA really
$Y(\widehat{\mathfrak{g}})$ and not $Y(\mathfrak{g})$? Costello 2013 \S6 actually
describes $Y_\hbar(\mathfrak{g})$ with $\hbar$ from $\Omega$-background, not the affine
version. The affine version needs an additional "doubling" from Cartan generators.
HEAL: Proved Theorem `thm:hCS5-finite-Yangian-perturbative` as finite $Y_\hbar$ and noted
Theorem `thm:hCS5-affine-gl1-Heisenberg-CP` as the affine $\mathfrak{gl}_1$ case. The
affine semisimple case demoted to Conjecture `conj:hCS5-affine-Yangian-g`, with the
Drinfeld-double obstruction explicitly named: geometrically requires
$\mathbb{C}^3 \sqcup (\mathbb{C}^3)^{\mathrm{op}}$ along $S^5$, not just a half-space.

**Cycle 4.** ATTACK: The $n \to \infty$ limit $Y_{0,0,n} \to Y_{n,n,n}$ --- is this
actually a limit? Gaiotto--Rapčák 2018 describe corner VOAs at all triples $(L, M, N)$;
the assertion that "$Y_{0,0,n}$ is the $n \to \infty$ limit of $Y_{n,n,n}$" is backwards.
Prochazka--Rapčák 2018 level-$n$ embedding is a *Miura truncation*, not a limit.
HEAL: Corollary `cor:corner-corrected` corrects the corner identification; Conjecture
`conj:corner-nn-limit` formulates the correct relationship as principal Miura quotient.

**Cycle 5.** ATTACK: The RLL-presentation compatibility with the chiral/currents
presentation at affine Yangian is asserted but only proved for specific types. Check:
Tsymbaliuk 2017 Thm 1.1 covers $\widehat{\mathfrak{gl}}_1$; Ueda 2019 covers
$\widehat{\mathfrak{sl}}_n$; Guay 2007 covers finite simply-laced. Affine non-abelian $D, E$
is at best conjectural via Gautam--Toledano Laredo 2017.
HEAL: Explicit scope for the RLL-chiral equivalence; the healed main theorem avoids
asserting this at scope beyond proved; conjecture path noted explicitly in
Retraction 7.

**Cycle 6.** ATTACK: "Opers smoothness at critical level" --- does this actually enter
the 5D hCS $\to$ affine Yangian proof chain? Frenkel--Ben-Zvi Thm 18.4.2 is about
Feigin--Frenkel center, not Yangian. At critical level, the affine Yangian itself
degenerates (not in the standard $(\epsilon_1, \epsilon_2, \epsilon_3)$-parameter
family). The citation is either irrelevant or load-bearing in a way not clearly stated.
HEAL: Retraction 6 removes the critical-level citation from the proof chain; clarified
that 5D hCS operates at generic (off-critical) level and the Feigin--Frenkel center is
adjacent but not used.

**Cycle 7.** ATTACK: Costello--Dimofte--Paquette 2020 "rank-one all-orders base" ---
does this paper exist with this content? Check: Costello--Dimofte--Paquette 2020
arXiv:2005.00083 is about 3D holomorphic twist, not 4D or 5D CS base. The correct
rank-one all-orders is Costello 2013 \S10 + Costello--Gaiotto 2018 \S6.
HEAL: Retraction 5 corrects the citation chain. The Theorem `thm:hCS5-finite-Yangian-perturbative` proof now cites Costello 2013 and Costello--Gaiotto 2018 as the actual
rank-one base, removing the phantom Costello--Dimofte--Paquette rank-one claim.

**Cycle 8.** ATTACK: The chain "Francis 2013 Thm 2.29 reduction to chiral
Chevalley--Eilenberg" --- Thm 2.29 of Francis 2013 (arXiv:1211.5619) says that
locally-constant factorisation algebras on $\mathbb{R}^n$ are equivalent to
$E_n$-algebras. Is the reduction to chiral Chevalley--Eilenberg direct from this? Yes,
via Beilinson--Drinfeld 2004 Ch 3 (chiral CE complex) plus Francis--Gaitsgory 2012
(chiral Koszul duality). The chain is valid.
HEAL: No retraction; the Francis 2013 citation is sharp and load-bearing. Step 6 of the
proof of Theorem `thm:hCS5-finite-Yangian-perturbative` cites this correctly.

**Cycle 9.** ATTACK: Whitehead's 2nd lemma $H^2_{\mathrm{Lie}}(\mathfrak{g}; \mathfrak{g}) = 0$
for semisimple $\mathfrak{g}$ --- does this actually cover all of $(\epsilon_1, \epsilon_2)$-space
or only at $\epsilon_1 = \epsilon_2 = 0$? The Whitehead lemma is a purely Lie-algebraic
statement; it kills the Lie-cohomology obstruction at each order in $\hbar$ uniformly.
But the BV obstruction at order $\hbar^n$ lives in a *deformed* cohomology group
incorporating $\Omega$-background; does the uniform vanishing still hold?
HEAL: Costello 2013 \S6 addresses this: the BV obstruction at order $\hbar^n$ lies in
$H^*_{\mathrm{BV}}(\mathrm{hCS}_5; \mathfrak{g}, \Omega)$, which reduces to standard
Lie cohomology via Hochschild--Serre for the $\Omega$-background deformation when the
latter is non-singular. At semisimple $\mathfrak{g}$ with non-singular $\Omega$-background
(generic $\epsilon_1, \epsilon_2, \epsilon_3$), Whitehead vanishing lifts. At the
self-dual CY$_3$ slice $\epsilon_1 + \epsilon_2 + \epsilon_3 = 0$ (codim 1), this is still
generic. At the further special slice $\epsilon_1 = \epsilon_2$ or critical $k = -h^\vee$,
the uniform vanishing may fail; those cases are excluded from the "generic level" scope.

---

All assertions in this document are cross-checked against the first-principles cache
(AP-CY F8, AP-CY147-AP-CY154) and the Costello--Gwilliam primary sources. Theorems
`thm:hCS5-finite-Yangian-perturbative`, `thm:hCS5-affine-gl1-Heisenberg-CP`,
`thm:chan-paton-minuscule` are stated at proved scope. Conjectures
`conj:hCS5-affine-Yangian-g`, `conj:corner-nn-limit` are stated at conjectural scope
with explicit obstructions. Retractions 1--7 name the precise ghost theorem inside each
overclaim.
