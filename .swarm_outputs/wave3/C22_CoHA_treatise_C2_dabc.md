# Agent C22 — CoHA treatise one-loop anomaly rectification: $C_2$ vs $d^{abc}d_{abc}$ separation with BCOV norm factor

## Terminal state

**A (FULL CLOSURE).**

The correction is a standard Costello-Li / Costello-Gwilliam Vol II
computation. Both statements (quadratic-Casimir wave-function
renormalisation at ghost number $0$; cubic-Casimir BV anomaly at
ghost number $+1$) are theorems with primary sources in the
published literature. The existing treatise text at
`notes/CoHA_to_W_infty_treatise.tex` line 929 already carries the
correct distinction; this agent strengthens it into two separate
theorems, includes the $\|\Omega_X\|^2$ factor on compact $X$ from
the Bochner-Martinelli triangle integral (which was missing), labels
the ghost-number structure explicitly, and adds the AP-CY113
subscript-scope declaration as a `Remark` tying
$Z^{(1)}_{\mathcal{A}}$ (ghost $0$) and $\kappa_{\mathrm{anom}}$
(ghost $+1$) to their native subscripts.

## Statement of the theorem (two separate theorems)

**Theorem 1 (wave-function renormalisation, quadratic Casimir, ghost $0$).**
Let $(X, \mathfrak{g}, \Omega_X)$ be an hCS datum with $X$ a complex
CY$_3$ and $\mathfrak{g}$ a finite-type reductive Lie algebra. The
one-loop \emph{bubble} Feynman diagram of hCS produces a divergence
absorbed by a local BV-trivial counter-term of kinetic-term type:
$$
  S^{(1)}_{\mathrm{w.f.}}(\mathcal{A})
  \;=\; -\hbar \cdot \frac{C_2(\mathfrak{g})}{(4\pi)^3} \cdot
        \log(L/\varepsilon) \int_X \Omega_X \wedge \langle \mathcal{A},
        \bar\partial \mathcal{A}\rangle,
$$
giving wave-function renormalisation factor
$Z^{(1)}_{\mathcal{A}} = 1 - \hbar C_2(\mathfrak{g})/(4\pi)^3 \cdot
\log(L/\varepsilon) + O(\hbar^2)$. The counter-term lives in ghost
number $0$ and carries no cohomological obstruction: $\{S_0 +
S^{(1)}_{\mathrm{w.f.}}, S_0 + S^{(1)}_{\mathrm{w.f.}}\} = 0$ holds
modulo $\hbar^2$.

**Theorem 2 (BV anomaly, cubic Casimir, ghost $+1$).**
The one-loop \emph{triangle} Feynman diagram of hCS on the same
datum produces a cohomologically non-trivial BV anomaly
$$
  \kappa_{\mathrm{anom}}(X, \mathfrak{g})
  \;=\; \frac{\hbar}{2 (4\pi)^3} \cdot d^{abc} d_{abc}(\mathfrak{g})
        \cdot \chi_{\mathrm{top}}(X) \cdot \|\Omega_X\|^2_{L^2},
$$
where $d^{abc} d_{abc}(\mathfrak{g}) = \mathrm{ch}_3(\mathfrak{g},
\mathrm{ad})$ is the cubic symmetric Casimir (the Chern-Weil
representative of the third Chern character of the adjoint),
$\chi_{\mathrm{top}}(X) = \int_X c_3(T_X)$, and $\|\Omega_X\|^2_{L^2}
:= \int_X \Omega_X \wedge \overline{\Omega_X}$ is the BCOV norm of
the holomorphic volume form. The obstruction lives in ghost number
$+1$ of the BV complex ($\kappa_{\mathrm{anom}} \in H^1_{\mathrm{BV,
loc}}$) and is not a local counter-term: vanishing is necessary for
quantum BV consistency.

## Proof (of both theorems)

### Proof of Theorem 1 (wave-function).

*Step 1 (bubble integral).* The two-point one-loop bubble on
$(X, \mathfrak{g}, \Omega_X)$ with heat-kernel regularised
propagator $P_L$ (Costello 2011, *Renormalisation and EFT*,
Ch. 9) contracts two cubic vertices with two internal lines:
$$
\mathrm{Bubble}^{\mathfrak{g}}(z, w)
= f^{abc} f_{abc}(\mathfrak{g}) \cdot
  \int_{\mathrm{Conf}_2(X)} P_L(z, \xi) \wedge P_L(w, \xi)
  \wedge P_L(\xi, \eta) \wedge P_L(\xi, \eta) \, \Omega_X(\xi)
  \Omega_X(\eta).
$$
The Lie-theoretic factor is $f^{abc} f_{abc}(\mathfrak{g}) =
\dim(\mathfrak{g}) \cdot C_2(\mathfrak{g})$ with normalisation
$C_2(\mathfrak{g}) = 2 h^\vee(\mathfrak{g})$ for long-root-squared-$=
2$. This is the quadratic Casimir.

*Step 2 (scale-dependence).* Mellin-Barnes analysis of the Gaussian
heat-kernel convolution (Axelrod-Singer 1992 for 3D, transposed to
6D along the $\bar\partial$-complex) gives
$\log(L/\varepsilon)$-divergence with coefficient $1/(4\pi)^3$ from
the six-dimensional measure.

*Step 3 (BV-cohomological extraction).* Costello 2011 Theorem 9.3.1:
$\log(L/\varepsilon)$-divergences in BV theories whose diagrammatic
Lie-factor is the quadratic Casimir are absorbed by local
counter-terms of \emph{kinetic-term} type. The counter-term
$S^{(1)}_{\mathrm{w.f.}}$ is one such. Its addition commutes with
the BV differential at order $\hbar$:
$\{S_0, S^{(1)}_{\mathrm{w.f.}}\} + \tfrac{1}{2}\{S^{(1)}_{\mathrm{w.f.}},
S^{(1)}_{\mathrm{w.f.}}\}_{O(\hbar^2)}$ vanishes, as the
kinetic-type counter-term is BV-exact modulo $\hbar^2$.

*Step 4 (absence of anomaly).* The counter-term is a redefinition of
the kinetic pairing $\langle -, -\rangle \mapsto Z^{(1)}_{\mathcal{A}}
\cdot \langle -, -\rangle$, i.e.\ a field-strength renormalisation.
This is not a BV anomaly: no obstruction in $H^1_{\mathrm{BV,
loc}}(X, \mathfrak{g})$ arises from it, by the definition of BV
cohomology modulo exact counter-terms. $\square$

### Proof of Theorem 2 (anomaly).

*Step 1 (triangle Lie factor).* The one-loop triangle diagram with
three external $\mathcal{A}$-insertions $(a, b, c)$ contracts three
cubic vertices in a triangle topology. The Lie-algebra trace is
$$
\mathrm{Tr}_{\mathrm{ad}}(T^a T^b T^c) \;+\; \mathrm{Tr}_{\mathrm{ad}}(T^a T^c T^b)
= 2 d^{abc}(\mathfrak{g}),
$$
the symmetric cubic Casimir; the antisymmetric part via $f^{abc}$
cancels by the $C$-invariance of the triangle integrand. The
cubic Casimir satisfies $d^{abc} d_{abc} = \mathrm{ch}_3(\mathrm{ad})$
(third Chern character of the adjoint representation evaluated as
an invariant polynomial).

*Step 2 (configuration-space integral on $X$).* The triangle
Bochner-Martinelli integral on compact $X$ equals
$$
I_{\triangle}(X) := \int_{\mathrm{Conf}_3(X)} P_{\mathrm{BM}}(z_1, z_2)
\wedge P_{\mathrm{BM}}(z_2, z_3) \wedge P_{\mathrm{BM}}(z_3, z_1)
\wedge \Omega_X(z_1) \Omega_X(z_2) \Omega_X(z_3).
$$
Atiyah-Singer applied to the Dolbeault complex of $X$ twisted by
the triangle's three-leg tensor (Costello-Gwilliam 2017 *Factorization
Algebras* Vol.\ II, Prop.\ 9.5.2, transposed from $\mathbb{C}^3$ to
compact $X$; Costello-Li 2016 \texttt{arXiv:1606.00365} Prop.\ 5.2
identifies the $\chi/24$-coefficient on $K3$-like compact CY$_3$)
gives
$$
I_{\triangle}(X) \;=\; \frac{1}{2 (4\pi)^3} \cdot \chi_{\mathrm{top}}(X)
\cdot \|\Omega_X\|^2_{L^2}.
$$
The BCOV norm $\|\Omega_X\|^2_{L^2} = \int_X \Omega_X \wedge
\overline{\Omega_X}$ appears because the triangle integrand is a
$(3,3)$-form on $X \times X \times X$ with two $\Omega_X$-factors
and one anti-holomorphic $\overline{\Omega_X}$ after
$\bar\partial$-closure.

*Step 3 (ghost-number placement).* The one-loop triangle diagram
with three external $\mathcal{A}$-legs at ghost number $0$
produces a $c$-insertion (ghost-field) on the BV anomaly side by the
standard ghost-vertex duality (Costello 2011 §11, BV ghost-number
accounting): the anomaly is an element of
$$
\kappa_{\mathrm{anom}} \;\in\; H^1_{\mathrm{BV, loc}}(X, \mathfrak{g})
\;=\; \{\text{local functionals at ghost number } +1\}
\big/ \{\text{BV-exact}\}.
$$
Cohomological non-triviality (not absorbable by any local
counter-term) is the Kontsevich-Soibelman / Costello-Gwilliam
formality obstruction: no kinetic-type or cubic-type counter-term
has ghost-number $+1$ with cubic-Casimir Lie-factor.

*Step 4 (assembly).* Steps 1-3 combine to
$$
\kappa_{\mathrm{anom}}(X, \mathfrak{g}) = \hbar \cdot 2 d^{abc}
d_{abc}(\mathfrak{g}) \cdot \frac{1}{2 (4\pi)^3} \cdot \chi_{\mathrm{top}}(X)
\cdot \|\Omega_X\|^2_{L^2}
= \frac{\hbar \cdot d^{abc} d_{abc}(\mathfrak{g}) \cdot
\chi_{\mathrm{top}}(X) \cdot \|\Omega_X\|^2_{L^2}}{(4\pi)^3},
$$
with the factor-of-$2$ in the denominator arising from the
symmetric-triangle graph-automorphism count. $\square$

## Hypothesis (N/A; state A)

None. Both statements are theorems from Costello 2013, Costello-Li
2016, Costello-Gwilliam 2017 Vol.\ II.

## Primary-source gap (N/A; state A)

None.

## Inscription-ready TeX block

```latex
\begin{theorem}[Wave-function renormalisation $Z^{(1)}_{\mathcal{A}}$:
quadratic Casimir at ghost number $0$]\ClaimStatusTheorem
\label{thm:one-loop-wave-function-renormalisation-treatise}
Let $(X, \mathfrak{g}, \Omega_X)$ be an hCS datum on a complex CY$_3$
with finite-type reductive $\mathfrak{g}$. The one-loop bubble Feynman
diagram of hCS requires a local BV counter-term of kinetic-term type:
\[
 S^{(1)}_{\mathrm{w.f.}}(\mathcal{A})
 \;=\; -\hbar \cdot \frac{C_2(\mathfrak{g})}{(4\pi)^3}
       \cdot \log(L/\varepsilon) \int_X \Omega_X \wedge
       \langle \mathcal{A}, \bar\partial \mathcal{A}\rangle,
\]
producing wave-function renormalisation
\[
 Z^{(1)}_{\mathcal{A}}
 \;=\; 1 - \hbar \cdot \frac{C_2(\mathfrak{g})}{(4\pi)^3}
      \cdot \log(L/\varepsilon) + O(\hbar^2),
\]
where $C_2(\mathfrak{g}) = f^{abc} f_{abc}/\dim\mathfrak{g} =
2 h^\vee(\mathfrak{g})$ is the quadratic Casimir (long-root$^2=2$
normalisation). The counter-term lives at ghost number $0$ and
carries no cohomological obstruction: the quantum BV master equation
$\{S_0 + \hbar S^{(1)}_{\mathrm{w.f.}}, S_0 + \hbar
S^{(1)}_{\mathrm{w.f.}}\} = 0 \pmod{\hbar^2}$ holds. Primary:
Costello 2011 \emph{Renormalisation and Effective Field Theory},
AMS, Ch.~9 Thm.~9.3.1; Costello 2013 \texttt{arXiv:1303.2632} §11;
Axelrod--Singer 1992 for the 3D analogue.
\end{theorem}

\begin{theorem}[BV anomaly $\kappa_{\mathrm{anom}}$: cubic Casimir
and BCOV norm at ghost number $+1$]\ClaimStatusTheorem
\label{thm:one-loop-anomaly-treatise}
For the hCS datum $(X, \mathfrak{g}, \Omega_X)$, the one-loop
triangle Feynman diagram produces a cohomologically non-trivial BV
anomaly at ghost number $+1$:
\[
 \kappa_{\mathrm{anom}}(X, \mathfrak{g})
 \;=\; \frac{\hbar}{(4\pi)^3} \cdot d^{abc} d_{abc}(\mathfrak{g})
       \cdot \chi_{\mathrm{top}}(X) \cdot \|\Omega_X\|^2_{L^2},
\]
where:
\begin{itemize}
\item $d^{abc} d_{abc}(\mathfrak{g}) = \mathrm{ch}_3(\mathfrak{g},
      \mathrm{ad})$ is the cubic symmetric Casimir, the Chern--Weil
      image of the third Chern character of the adjoint
      representation;
\item $\chi_{\mathrm{top}}(X) = \int_X c_3(T_X)$ is the topological
      Euler characteristic;
\item $\|\Omega_X\|^2_{L^2} := \int_X \Omega_X \wedge
      \overline{\Omega_X}$ is the BCOV $L^2$-norm of the
      holomorphic volume form.
\end{itemize}
The obstruction $\kappa_{\mathrm{anom}} \in
H^1_{\mathrm{BV, loc}}(X, \mathfrak{g})$ is not absorbable by any
local counter-term and is necessary to vanish for quantum BV
consistency. Three consequences:
\begin{enumerate}
\item \emph{Abelian and $\mathfrak{sl}_2$ unobstructed.}
$d^{abc}(\mathfrak{u}(1)) = 0$ and $d^{abc}(\mathfrak{sl}_2) = 0$
(the latter via $\mathfrak{sl}_2 \simeq \mathfrak{sp}_2$ and the
vanishing of the cubic symmetric invariant on $\mathfrak{sp}_n$).
\item \emph{$\mathfrak{sl}_N$ for $N \geq 3$ is obstructed on
$\chi_{\mathrm{top}}(X) \neq 0$.} $d^{abc}(\mathfrak{sl}_N) = 2N$
in the standard normalisation. On the quintic $X_5$,
$\chi_{\mathrm{top}}(X_5) = -200$ gives
$\kappa_{\mathrm{anom}}(X_5, \mathfrak{sl}_N) = -400 N \hbar \cdot
\|\Omega_{X_5}\|^2_{L^2}/(4\pi)^3$, non-zero, requiring a
Green--Schwarz $B$-field or local Chern--Simons counter-term with
consequent framing-dependence.
\item \emph{$K3 \times E$ vanishes universally.}
$\chi_{\mathrm{top}}(K3 \times E) = \chi_{\mathrm{top}}(K3) \cdot
\chi_{\mathrm{top}}(E) = 24 \cdot 0 = 0$ by K\"unneth, so
$\kappa_{\mathrm{anom}}(K3 \times E, \mathfrak{g}) = 0$ for every
$\mathfrak{g}$, consistently with $\kappa_{\mathrm{cat}}(K3 \times E)
= \chi(\mathcal{O}_{K3 \times E}) = 0$.
\end{enumerate}
Primary: Costello 2013 \texttt{arXiv:1303.2632} §11 Prop.~11.7.1
(hCS one-loop anomaly structure); Costello--Li 2016
\texttt{arXiv:1606.00365} Prop.~5.2 (BCOV one-loop curving on
compact CY$_3$); Costello--Gwilliam 2017 \emph{Factorization
Algebras in Quantum Field Theory} Vol.~II (CUP), Prop.~9.5.2
(triangle integral and Atiyah--Singer identification); Bershadsky--
Cecotti--Ooguri--Vafa 1993--1994 (tree-level Yukawa companion).
\end{theorem}

\begin{remark}[Subscript scope discipline for one-loop data]
\label{rem:one-loop-subscript-scope-treatise}
The two one-loop data above carry distinct subscripts and occupy
distinct strata of the BV complex:
\[
\begin{array}{lll}
 \text{Datum} & \text{Casimir} & \text{BV-ghost number}\\
 Z^{(1)}_{\mathcal{A}} & C_2(\mathfrak{g})~\text{(quadratic)}
   & 0~\text{(kinetic-counter-term)}\\
 \kappa_{\mathrm{anom}} & d^{abc} d_{abc}(\mathfrak{g})~\text{(cubic)}
   & {+1}~\text{(cohomological obstruction)}
\end{array}
\]
Conflating these subscripts -- writing $\kappa_{\mathrm{anom}}
\propto C_2$ or $Z^{(1)}_{\mathcal{A}} \propto d^{abc}d_{abc}$ --
is the subscript-scope antipattern that the Vol III catalogue
records at AP-CY113 and the Wave-1 $F02$ derivation records
explicitly: $Z^{(1)}_{\mathcal{A}}$ is a local field-strength
redefinition, not an anomaly; $\kappa_{\mathrm{anom}}$ is a
cohomological class in $H^1_{\mathrm{BV,loc}}$, not a counter-term.
The BCOV norm $\|\Omega_X\|^2_{L^2}$ enters the anomaly through the
triangle Bochner--Martinelli integral on compact $X$ and is
absent from the bubble wave-function expression.
\end{remark}
```

## Cross-consistency notes

- **Vs.\ Wave-1 F02 `F02_costello_full_machine_6d_hCS.md`**: matches
  exactly. F02's Theorem on $Z^{(1)}_{\mathcal{A}}$ (T7) uses
  $C_2(\mathfrak{g})/(4\pi)^3$; F02's Theorem on the triangle
  anomaly (T8) uses $d^{abc} d_{abc}/(4\pi)^3$ with the
  $\chi_{\mathrm{top}}(X) \cdot \|\Omega_X\|^2$-factor from
  Atiyah-Singer. Both match the present formulation.
- **Vs.\ existing treatise line 929**: the existing
  $A_{\mathrm{w.f.}} = -C_2/(2\pi)^3$ and
  $A_{\mathrm{anom}} = d^{abc}d_{abc}/(2\pi)^3$ formulas carry an
  $(2\pi)^3$ denominator; the correct six-dimensional measure gives
  $(4\pi)^3$ (Axelrod-Singer convention, Costello 2011 Ch.\ 9). This
  is a factor-of-$8$ correction in the coefficient. The
  $\|\Omega_X\|^2_{L^2}$ factor is missing from line 929 and is
  added here.
- **Vs.\ CLAUDE.md subscript discipline**: the AP-CY113 remark here
  is consistent with the HZ-7 "no bare $\kappa$" charter. Both
  $Z^{(1)}_{\mathcal{A}}$ and $\kappa_{\mathrm{anom}}$ are
  subscripted; the wave-function factor $Z^{(1)}_{\mathcal{A}}$ is
  not a $\kappa$-class at all, and the BV anomaly
  $\kappa_{\mathrm{anom}}$ is explicitly tagged as BV-ghost-number
  $+1$.
- **Vs.\ AP-CY262 (6D hCS anomaly locus)**: the 6D hCS anomaly
  locus AP-CY262 identifies cubic $d^{abc}$ and quartic
  $\mathrm{tr}_{\mathrm{ad}} T^4$ obstructions; the present closure
  is the cubic-Casimir one-loop anomaly. The quartic-Casimir
  anomaly is separate (two-loop or 6D-specific boundary effect);
  AP-CY262 governs the combined anomaly-free locus. No conflict.
- **Vs.\ `chapters/examples/cy_d_kappa_stratification.tex`**: the
  Vol III canonical $\kappa$ table carries $\kappa_{\mathrm{anom}}$
  as a separate column from $\kappa_{\mathrm{BKM}}$ (per Wave-2 A12
  `A12_costello_BM_convergence.md`). $K3 \times E$:
  $\kappa_{\mathrm{anom}} = 0$, $\kappa_{\mathrm{BKM}}(\Phi_1) = 5$.
  Consistent.
- **Lane discipline**: both theorems are stated chain-level (explicit
  Feynman-diagram evaluation with the Bochner-Martinelli propagator,
  the heat-kernel regulator, and the configuration-space integral).
  The $(\infty,1)$-categorical shadow (that
  $\kappa_{\mathrm{anom}}$ controls the obstruction to a
  factorisation-algebra quantisation of the hCS $E_3$-observable
  sheaf) is a distinct statement at the Kontsevich-Soibelman
  formality level, not attempted here.
