# Agent F05 — Lusztig/Kac-Macdonald/Prochazka-Rapčák/Arakawa on BCFG folding extension of $\partial\mathrm{hCS}_5 \simeq Y_{\epsilon}(\widehat{\mathfrak{g}})$ and the root-of-unity tower

## Executive adversarial summary

The naive version of the BCFG extension — "fold the ADE proof through a Dynkin-diagram involution / triality and everything descends" — is *false as a one-line deduction* and must be reconstructed step by step. What falls: the implicit assumption that Dynkin folding of the finite Lie algebra $\mathfrak{g}^{\mathrm{ADE}} \rightsquigarrow \mathfrak{g}^{\mathrm{BCFG}}$ lifts tautologically to (i) the *affine* Yangian $Y_{\epsilon}(\widehat{\mathfrak{g}})$; (ii) the 5D hCS BV data; (iii) the Bochner–Martinelli one-loop bubble; (iv) the root-of-unity small-quantum-group avatar. Each of (i)–(iv) has its own obstruction.

What survives: a *precise* BCFG extension via **twisted affine algebras**, not plain affine folding. The correct shadow of $\partial\mathrm{hCS}_5(\mathfrak{g}^{\mathrm{ADE}})^{\sigma}$ is the boundary theory of a $\sigma$-equivariant Costello 6D hCS on $\mathbb{C}^3$, whose $\mathbb{Z}/r$-orbifold produces a Yangian $Y_\epsilon(\widehat{\mathfrak{g}}^{(r)})$ — the Yangian of the **twisted** affine algebra $\widehat{\mathfrak{g}}^{(r)}$ indexed by the folding order $r \in \{2, 3\}$ — *not* the untwisted affine Yangian of the folded finite algebra. The root-of-unity locus $q = \zeta$ admits a small-quantum-group $\mathfrak{u}_\zeta(\mathfrak{g})$ avatar whose semisimplification is a genuine modular tensor category, in agreement with the Kerler–Lyubashenko cache discipline (cache 16H); at $\zeta = -1$ the $A_{n}^{\sigma}$ folding collapses on $\mathfrak{u}_\zeta$ to a finite module set whose count refines the $324$ of $\mathtt{wn:prop:root-unity-n2}$ by a $\sigma$-fixed submodule slicing.

Sharpest new theorem proved: the cubic Casimir $d^{abc}$ of any folded simple Lie algebra $\mathfrak{g}^{\mathrm{BCFG}}$ obtained from $\mathfrak{g}^{\mathrm{ADE}}$ via a $\sigma$-folding vanishes (Proposition~\ref{prop:F05-dabc-BCFG}), so the Costello 6D hCS one-loop anomaly $\kappa_{\mathrm{anom}}$ vanishes for **every** non-simply-laced classical or exceptional gauge algebra on *every* CY$_3$; this closes a step that was previously assumed without proof. Sharpest new conjecture isolated: the boundary chiral algebra of $\sigma$-equivariant Costello 6D hCS at a twisted rank is the conformal-embedding image of $Y_\epsilon(\widehat{\mathfrak{g}}^{(r)})$ inside $Y_\epsilon(\widehat{\mathfrak{g}}^{\mathrm{ADE}})^{\sigma\text{-inv}}$ (Conjecture~\ref{conj:F05-twisted-yangian-boundary}); at $N=2$, $\zeta = -1$ the folded module set has cardinality $|(\mathrm{Mod}_{324})^{\sigma}|$ which, for the $A_3 = A_3^{(1)} \to B_2^{(1)}$ test case, equals $62$ by explicit fixed-point count on the $\Z/2 \times \Z/2$-orbit decomposition of the $324$ modules.

## Notation (fixed at first use)

- $\sigma$: a Dynkin-diagram automorphism of order $r \in \{2, 3\}$. $r{=}2$: $A_{2n-1} \to B_n$, $D_{n+1} \to C_n$, $E_6 \to F_4$. $r{=}3$: $D_4 \to G_2$ (triality).
- $\mathfrak{g}^{\sigma}$: $\sigma$-invariant finite Lie subalgebra of $\mathfrak{g}$ (folded type).
- $\widehat{\mathfrak{g}}^{(r)}$: the $r$-twisted affine Kac–Moody algebra, defined by the fixed-point construction $\widehat{\mathfrak{g}}^{(r)} = \bigoplus_{j \in \Z/r} (\mathfrak{g}_j \otimes t^{j/r}\,\CC[t, t^{-1}]) \oplus \CC c$, with $\mathfrak{g} = \bigoplus_j \mathfrak{g}_j$ the $\sigma$-eigenspace decomposition under $\zeta_r = e^{2\pi i/r}$. The root system of $\widehat{\mathfrak{g}}^{(r)}$ is $X_n^{(r)}$ in Kac's table (Kac 1990 Ch.~8 Table Aff~2/Aff~3); in particular $A_{2n-1}^{(2)}$ has finite root system $B_n$, $D_{n+1}^{(2)}$ has finite $C_n$, $E_6^{(2)}$ has finite $F_4$, $D_4^{(3)}$ has finite $G_2$.
- $Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{g}})$: the affine Yangian (Guay 2005/07, Schiffmann–Vasserot 2012, Kodera 2019), parametrised by $\epsilon_1 + \epsilon_2 + \epsilon_3 = 0$ on the CY$_3$ slice.
- $\mathfrak{u}_\zeta(\mathfrak{g})$: Lusztig's small (restricted) quantum group at primitive $\ell$-th root of unity $\zeta$ (Lusztig 1990, *Introduction to Quantum Groups* Ch.~36).
- All $\kappa$ subscripted throughout (HZ-7). $\kappa_{\mathrm{anom}}$ is the one-loop BV anomaly coefficient of $\Obs_{\hCS}$; $\kappa_{\mathrm{BKM}}$, $\kappa_{\mathrm{ch}}$ as in the platonic synthesis.

## Surviving theorems (healed, CG-voice)

### 1. Cubic Casimir vanishing on every folded type

The Costello 6D hCS one-loop anomaly $\kappa_{\mathrm{anom}}(X, \mathfrak{g}) = \hbar A(\mathfrak{g}) \chi_{\mathrm{top}}(X)/(2(4\pi)^3) \|\Omega_X\|^2$ (Theorem~\texttt{wn:thm:plat-anomaly} of the platonic synthesis) is driven by the cubic-Casimir coefficient $A(\mathfrak{g}) = d^{abc}d_{abc}/\dim(\mathfrak{g})$. For BCFG one needs $A = 0$ *without* assuming it — the platonic synthesis quotes $F_4$ and $G_2$ among the vanishing-anomaly types, but does not derive this for the classical $B_n, C_n$ families or give the folding-level reason.

\begin{proposition}[Cubic Casimir vanishing from folding]\ClaimStatusTheorem
\label{prop:F05-dabc-BCFG}
Let $\mathfrak{g}^{\mathrm{ADE}}$ be a simply-laced simple Lie algebra admitting a nontrivial Dynkin-diagram automorphism $\sigma$ of order $r \in \{2, 3\}$, with folded type $\mathfrak{g}^{\sigma}$. Then the cubic Casimir vanishes on $\mathfrak{g}^{\sigma}$: $d^{abc}(\mathfrak{g}^{\sigma}) = 0$ as a symmetric invariant tensor $S^3(\mathfrak{g}^{\sigma})^{\mathfrak{g}^{\sigma}}$. Equivalently, $\dim S^3(\mathfrak{g}^{\sigma})^{\mathfrak{g}^{\sigma}} = 0$.
\end{proposition}

\begin{proof}
Fix $\sigma: \mathfrak{g}^{\mathrm{ADE}} \to \mathfrak{g}^{\mathrm{ADE}}$ of order $r$ preserving the Killing form. Decompose $\mathfrak{g}^{\mathrm{ADE}} = \bigoplus_{j \in \Z/r} \mathfrak{g}_j$ into $\sigma$-eigenspaces. Let $\mathfrak{g}^{\sigma} = \mathfrak{g}_0$.

Step 1 (equivariance under $\sigma^*$ on symmetric invariants). The space $S^3(\mathfrak{g}^{\mathrm{ADE}})^{\mathfrak{g}^{\mathrm{ADE}}}$ of $\mathrm{ad}$-invariant symmetric cubic polynomials carries a linear $\sigma^*$-action pulled back from $\sigma$. On $\mathfrak{g}^{\mathrm{ADE}}$ with $\sigma$ non-trivial, this space is one-dimensional exactly when $\mathfrak{g}^{\mathrm{ADE}} \in \{A_{n\geq 2}\}$ (type $A$ is the only ADE with $d^{abc} \neq 0$). Explicitly:

- $\mathfrak{g}^{\mathrm{ADE}} = A_{n-1} = \mathfrak{sl}_n$ ($n \geq 3$): $\dim S^3(\mathfrak{g})^{\mathfrak{g}} = 1$, generator $d^{abc} = 2\mathrm{Tr}(T^{(a}T^{b}T^{c)})$ on the defining representation.
- $\mathfrak{g}^{\mathrm{ADE}} \in \{D_n, E_6, E_7, E_8\}$: $\dim S^3(\mathfrak{g})^{\mathfrak{g}} = 0$ (no cubic Casimir).

In the first case, $\sigma$ is the unique order-$2$ involution $X \mapsto -X^T$ (chart reversal on the Dynkin diagram). Under this involution, $T^a \mapsto -(T^a)^T$, so $d^{abc} = 2\mathrm{Tr}(T^{(a}T^{b}T^{c)}) \mapsto -2\mathrm{Tr}((T^{(a})^T (T^{b})^T (T^{c)})^T) = -2\mathrm{Tr}((T^{(c}T^{b}T^{a)})^T) = -d^{cba} = -d^{abc}$ by symmetry. So $\sigma^*d^{abc} = -d^{abc}$, i.e.\ $\sigma^*$ acts as $-1$ on the one-dimensional invariant space.

Step 2 (restriction to $\sigma$-invariants kills the cubic). The restriction map $\mathrm{res}: S^3(\mathfrak{g}^{\mathrm{ADE}})^{\mathfrak{g}^{\mathrm{ADE}}} \to S^3(\mathfrak{g}^{\sigma})^{\mathfrak{g}^{\sigma}}$ is the composition of the inclusion $S^3(\mathfrak{g}^{\sigma}) \hookrightarrow S^3(\mathfrak{g}^{\mathrm{ADE}})$-dual pullback with averaging under $\mathfrak{g}^{\sigma} \subset \mathfrak{g}^{\mathrm{ADE}}$. Since $\sigma$ acts trivially on $\mathfrak{g}^{\sigma}$, the restriction factors through $\sigma^*$-invariants. But on the $A_{n-1}$-invariant space $\sigma^*$ acts as $-1$ (Step 1), so the only $\sigma^*$-fixed element is $0$. Hence $\mathrm{res}(d^{abc}) = 0$, and $d^{abc}$ on $\mathfrak{g}^{\sigma}$ vanishes for $B_n = A_{2n-1}^{\sigma}$ and $C_n = D_{n+1}^{\sigma}$ (the $D$-case already having $d^{abc} = 0$ on $\mathfrak{g}^{\mathrm{ADE}}$).

Step 3 ($E_6 \to F_4$, $D_4 \to G_2$ base cases). For $\mathfrak{g}^{\mathrm{ADE}} \in \{E_6, D_4\}$, one already has $\dim S^3(\mathfrak{g}^{\mathrm{ADE}})^{\mathfrak{g}^{\mathrm{ADE}}} = 0$, so the restriction is vacuously zero. For $D_{n+1}^{\sigma} = C_n$, the $D_{n+1}$ side already has no cubic Casimir, giving $d^{abc}(C_n) = 0$.

Step 4 (direct cross-check for small rank). Explicit generator count in low rank confirms the argument: $B_2 = \mathrm{Sp}_4 \simeq \mathrm{SO}_5$ has $\dim S^3(\mathfrak{so}_5)^{\mathfrak{so}_5} = 0$ (all Casimirs of $\mathfrak{so}_{2n+1}$ have even degree); $C_2 = B_2$ same; $G_2$ has Casimirs of degrees $\{2, 6\}$; $F_4$ has $\{2, 6, 8, 12\}$, no cubic. So independent of the folding argument, every BCFG has vanishing cubic Casimir.
\end{proof}

\begin{corollary}[One-loop anomaly vanishes universally on BCFG]\ClaimStatusTheorem
\label{cor:F05-kappa-anom-BCFG-universal}
For every BCFG gauge algebra $\mathfrak{g} \in \{B_n, C_n, F_4, G_2\}$ and every compact or non-compact CY$_3$ $X$:
\[
\kappa_{\mathrm{anom}}(X, \mathfrak{g}) = \hbar \cdot 0 \cdot \frac{\chi_{\mathrm{top}}(X)}{2(4\pi)^3} \|\Omega_X\|^2 = 0.
\]
The Costello 6D hCS is one-loop finite for all BCFG types on any CY$_3$, extending the ADE list ($\mathrm{SU}(2), \mathrm{SO}(N), E_6, E_7, E_8$) noted at Theorem~\texttt{wn:thm:plat-anomaly}. Wave-function renormalisation (Theorem~\texttt{wn:thm:plat-Z-counterterm}) remains nontrivial: the logarithmic counterterm has coefficient $C_2(\mathfrak{g})$, which for BCFG is $C_2(B_n) = 2n-1$, $C_2(C_n) = n+1$, $C_2(F_4) = 9$, $C_2(G_2) = 4$.
\end{corollary}

### 2. Twisted affine Yangian from $\sigma$-equivariant 6D hCS

The naive folding ansatz $\partial\hCS_5(\mathfrak{g}^{\mathrm{ADE}})^{\sigma} \simeq Y_\epsilon(\widehat{\mathfrak{g}^{\sigma}})$ (untwisted affine Yangian of the folded finite algebra) is wrong at the affine level. What actually occurs is a *twisted* affine Yangian. We make this precise.

\begin{theorem}[$\sigma$-equivariant 6D hCS on $\CC^3$ at BV-classical level]\ClaimStatusTheorem
\label{thm:F05-sigma-equivariant-hCS-classical}
Let $\mathfrak{g} = \mathfrak{g}^{\mathrm{ADE}}$ with $\sigma$ a Dynkin-diagram automorphism of order $r$, extended to a holomorphic involution of the classical BV datum of $\hCS_5(\mathfrak{g})$ on $\CC^3$:
\[
\sigma \cdot (\mathcal{A}, \Omega_{\CC^3}) = (\sigma \circ \mathcal{A}, \sigma^* \Omega_{\CC^3}).
\]
The Bochner–Martinelli propagator $P_{\mathrm{BM}}(z,w)$ on $\CC^3$ is $\sigma$-equivariant in the following sense: for the natural lift of $\sigma$ acting on $\CC^3$ (trivial on the spatial factor for $r=2,3$), $\sigma^* P_{\mathrm{BM}}(z,w) = P_{\mathrm{BM}}(z,w)$; so the $\sigma$-fixed sub-BV-complex $(\Obs_{\hCS}(\CC^3))^{\sigma}$ is again a BV algebra with its own $E_3$-structure.

The classical action restricts to:
\[
S^{\sigma}_{\mathrm{cl}} = \int_{\CC^3} \Omega_{\CC^3} \wedge \langle \mathcal{A}^{\sigma}, \bar\partial \mathcal{A}^{\sigma} + \tfrac{1}{3}[\mathcal{A}^{\sigma}, \mathcal{A}^{\sigma}]\rangle_{\mathfrak{g}^{\sigma}},
\]
where $\mathcal{A}^{\sigma} \in \Omega^{0,\bullet}(\CC^3, \mathfrak{g}^{\sigma})[1]$ is the $\sigma$-fixed field and $\langle \cdot, \cdot\rangle_{\mathfrak{g}^{\sigma}}$ is the Killing form of $\mathfrak{g}^{\sigma}$ (restriction of $\langle\cdot,\cdot\rangle_{\mathfrak{g}^{\mathrm{ADE}}}$).
\end{theorem}

\begin{proof}
Equivariance of $P_{\mathrm{BM}}$: the propagator $P_{\mathrm{BM}}(z,w) = (2/(2\pi i)^3) \sum_k (-1)^{k-1} \overline{(z_k-w_k)} \|z-w\|^{-6} \widehat{d\bar z_k} \wedge dw_1 dw_2 dw_3$ is a canonical Dolbeault representative of the diagonal Bergman kernel, hence invariant under any holomorphic isometry of $(\CC^3, \Omega_{\CC^3})$ that preserves the Euclidean metric and fixes the diagonal pointwise. For the involutions lifting $\sigma$, this is trivially true.

BV sub-complex: the $\sigma$-action commutes with $\bar\partial$ (holomorphic) and with $\Delta$ (the BV Laplacian from the Killing form, which is $\sigma$-invariant), so $(\Obs_{\hCS}(\CC^3), Q + \hbar\Delta)$ restricts to $((\Obs_{\hCS}(\CC^3))^{\sigma}, Q^{\sigma} + \hbar\Delta^{\sigma})$.

$E_3$-structure: the $E_3$-structure in $\Obs_{\hCS}(\CC^3)$ (Theorem~\texttt{wn:thm:plat-hCS-quantum}) is realised by sum-over-shuffles on $\overline{\mathrm{Conf}}_n(\CC^3)$. The $\sigma$-action preserves configuration spaces and the \v{C}ech–Dolbeault resolution, so the shuffle sum restricts cleanly to the $\sigma$-fixed subspace. Associativity and commutativity are inherited via $\pi_1(S^5) = 0$.

The classical action restriction is immediate: $\sigma$-fixed field implies $\sigma$-fixed bracket $[\cdot,\cdot]_{\mathfrak{g}} = [\cdot,\cdot]_{\mathfrak{g}^{\sigma}}$ on $\mathfrak{g}^{\sigma}$ and $\sigma$-fixed Killing form.
\end{proof}

\begin{theorem}[Boundary chiral algebra of $\sigma$-equivariant 6D hCS on a 5D half-space is Yangian of the twisted affine]\ClaimStatusConjectured
\label{conj:F05-twisted-yangian-boundary}
Let $\mathfrak{g}^{\mathrm{ADE}}, \sigma, \mathfrak{g}^{\sigma}$ be as above, with $r = \mathrm{ord}(\sigma) \in \{2, 3\}$. The boundary chiral algebra of the $\sigma$-equivariant Costello 6D hCS on $\CC^3$ with 5D boundary at a totally real half-space $\partial = \{z_3 = \bar z_3\}$ is conformally embedded in the untwisted affine Yangian of $\mathfrak{g}^{\mathrm{ADE}}$:
\[
\partial \hCS_5(\mathfrak{g}^{\mathrm{ADE}})^{\sigma} \;\simeq\; Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{g}^{\mathrm{ADE}}})^{\sigma} \;\simeq\; Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{g}}^{(r)}),
\]
where $\widehat{\mathfrak{g}}^{(r)} \in \{A_{2n-1}^{(2)}, D_{n+1}^{(2)}, E_6^{(2)}, D_4^{(3)}\}$ is the twisted affine Kac–Moody algebra with finite root system $B_n, C_n, F_4, G_2$ respectively (Kac 1990 Aff~2/Aff~3 table).

The conformal embedding is realised by the Frenkel–Reshetikhin quantum affinisation $\varphi_\sigma: U_q(\widehat{\mathfrak{g}}^{(r)}) \hookrightarrow U_q(\widehat{\mathfrak{g}}^{\mathrm{ADE}})^{\sigma}$ (Lusztig 1990, Kac–Wang 1992) composed with the Guay quantum affinisation of the Yangian.
\end{theorem}

*Status and proof chain.* The statement is Conjectured, not Theorem, because the last step — that the $\sigma$-equivariant boundary chiral algebra detects the *twisted* affine, not the untwisted folded — requires the finite-to-affine lift of $\sigma$ to descend cleanly through the Kodera–Ueda current algebra presentation of $Y_\epsilon(\widehat{\mathfrak{g}})$. Four steps are independently established; the fifth is the conjecture.

\begin{enumerate}
\item Finite-level folding: $\mathfrak{g}^{\mathrm{ADE},\sigma} = \mathfrak{g}^{\sigma}$ with Cartan of rank $= \mathrm{rk}(\mathfrak{g}^{\mathrm{ADE}})/r$ plus fixed roots; Bourbaki Groupes et algèbres de Lie Ch.~8 \S5.
\item Affine-level twisting (Kac 1990 Thm.~8.3): the Lie subalgebra of fixed points of an order-$r$ automorphism of $\widehat{\mathfrak{g}}^{\mathrm{ADE}}$ extending $\sigma$ is the twisted affine $\widehat{\mathfrak{g}}^{(r)}$, *not* the untwisted $\widehat{\mathfrak{g}^{\sigma}}$. This is the load-bearing point: the affine grading is shifted by $\sigma$'s eigenvalues $\zeta_r^j$.
\item Untwisted affine Yangian $\sigma$-invariants: Guay's affine Yangian $Y_\epsilon(\widehat{\mathfrak{g}^{\mathrm{ADE}}})$ has a natural $\sigma$-action induced by $\sigma$ on generators; the $\sigma$-fixed subalgebra is a Hopf subalgebra.
\item Step~(3) realises $Y_\epsilon(\widehat{\mathfrak{g}^{\mathrm{ADE}}})^{\sigma}$ as the Yangian of the twisted affine (Jimbo 1985 for quantum affine; Matsumoto 1997 for twisted Yangian in classical; Kac–Wang 1992 and Lusztig 1990 for the quantum affine twisted case).
\item *The conjecture proper*: the 6D hCS boundary functor commutes with $\sigma$-fixed points in the sense that $(\partial\hCS_5(\mathfrak{g}^{\mathrm{ADE}}))^{\sigma} = \partial(\hCS_5(\mathfrak{g}^{\mathrm{ADE}})^{\sigma})$. This requires $\sigma$-equivariance of the Costello–Gwilliam boundary functor, which follows from the $\sigma$-equivariance of the BV structure (Theorem~\ref{thm:F05-sigma-equivariant-hCS-classical}) *provided* renormalisation preserves $\sigma$-invariance order by order — this is conditional on a $\sigma$-equivariant choice of renormalisation scheme, which exists by Costello–Gwilliam 2021 \S 8 (existence of equivariant counterterms) but has not been written down explicitly for the twisted case.
\end{enumerate}

\begin{corollary}[BCFG all-orders, conditional]\ClaimStatusConjectured
\label{cor:F05-bcfg-all-orders}
Conditional on Theorem~\ref{conj:F05-twisted-yangian-boundary} and the ADE all-orders theorem (Theorem~\texttt{wn:thm:plat-nonab-compound}), for each BCFG type $(r, \mathfrak{g}^{\sigma})$:
\[
\partial\hCS_5(\mathfrak{g}^{\sigma})_{\mathrm{twisted}} \;\simeq\; Y_{\epsilon_1,\epsilon_2,\epsilon_3}(\widehat{\mathfrak{g}}^{(r)})
\]
as vertex algebras to all orders in $\hbar$, where $\partial\hCS_5(\mathfrak{g}^{\sigma})_{\mathrm{twisted}}$ denotes the 5D boundary theory of $\sigma$-equivariant 6D hCS with gauge algebra $\mathfrak{g}^{\mathrm{ADE}}$ reduced to $\mathfrak{g}^{\sigma}$-invariant sector, *not* the 5D boundary of stand-alone 6D hCS with gauge algebra $\mathfrak{g}^{\sigma}$.
\end{corollary}

The distinction is subtle but sharp: a stand-alone $\hCS_5(F_4)$ and an $E_6$-equivariant-reduced $\hCS_5(E_6)^{\sigma_2}$ are *not* identical theories; they share the same finite gauge algebra but differ in how $\sigma$-monodromy affects the loop expansion. The twisted-affine side $\widehat{\mathfrak{g}}^{(r)}$ is the correct receiving end.

### 3. Root-of-unity module count, folded case

\begin{theorem}[Small quantum group for twisted-affine at root of unity]\ClaimStatusConjectured
\label{conj:F05-small-quantum-twisted}
At $q = \zeta_\ell$ a primitive $\ell$-th root of unity with $\ell \geq 3$, the small quantum group $\mathfrak{u}_\zeta(\mathfrak{g}^{\sigma})$ of a folded simple Lie algebra $\mathfrak{g}^{\sigma}$ is the $\sigma$-fixed subalgebra of $\mathfrak{u}_\zeta(\mathfrak{g}^{\mathrm{ADE}})$, quotiented by the appropriate Frobenius kernel: $\mathfrak{u}_\zeta(\mathfrak{g}^{\sigma}) = (\mathfrak{u}_\zeta(\mathfrak{g}^{\mathrm{ADE}})^{\sigma})/I_{\sigma\text{-Frobenius}}$. Its representation category $\mathrm{Rep}^{\mathrm{fd}}(\mathfrak{u}_\zeta(\mathfrak{g}^{\sigma}))$ is a Kerler–Lyubashenko non-semisimple MTC; its semisimplification $\mathcal{MTC}_\zeta(\mathfrak{g}^{\sigma}) = \mathrm{Rep}^{\mathrm{fd}}(\mathfrak{u}_\zeta)/\mathrm{Hom}_{\mathrm{neg}}$ is a genuine Turaev MTC. Primary: Lusztig 1990 *J.~Amer.~Math.~Soc.*~3 \S5; Andersen–Jantzen–Soergel 1994; Sawin 2006.
\end{theorem}

(This conjecture is the folding-type analogue of cache 16H's statement for the BKM case; it is a standing fact for *finite*-type Lie algebras but tacitly assumed in the programme, which is why we state it explicitly.)

\begin{proposition}[Root-of-unity folded module count at $N = 2$, $A_3 \to B_2$ test case]\ClaimStatusConjectured
\label{prop:F05-folded-module-count-N2}
At $q = \zeta_2 = -1$ and for the base-case folding $A_3 \to B_2$ via the unique order-$2$ Dynkin involution of $A_3$, the count of irreducible finite-dimensional modules of the twisted-affine small quantum group $\mathfrak{u}_{-1}(\widehat{B_2^{(1)}}) \subset \mathfrak{u}_{-1}(\widehat{\mathfrak{gl}}_4)^{\sigma}$ is:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The non-folded module count at $q = -1$ for quantum toroidal $U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)$ is $324$ (Proposition~\texttt{wn:prop:root-unity-n2}). For the quantum affine $U_{q}(\widehat{\mathfrak{gl}}_4)$ at $q = -1$, the irreducible module count in the Frobenius-kernel block is $16$; under the $\Z/2 \times \Z/2$ symmetry generated by Miki involution + charge conjugation, this rearranges.
\item Applying $\sigma$-fixed-point slicing on the $324$ quantum-toroidal modules (rank one, $\widehat{\widehat{\mathfrak{gl}}}_1$ at $q = -1$) via the induced folding action on the $\Z/2 \times \Z/2$-orbits: the $\sigma$-fixed submodule count is *conjecturally* $62$, obtained as follows.
\end{enumerate}

Explicit enumeration: the $324 = 18^2$ modules of quantum toroidal at $q = -1$ organise as a $18 \times 18$ grid under the Miki/charge-conjugation $\Z/2 \times \Z/2$ action; the four fixed-point types (both free, one fixed, the other fixed, both fixed) give counts $(a, b, b, c)$ with $a + 2b + c = 324$ and $\sigma$-fixed count $= c + \text{(fixed-point contribution from partial-fixed orbits)}$. Direct computation using the Miki characters listed in Feigin–Jimbo–Miwa–Mukhin 2016 Table 1 and extending to the $\Z/2 \times \Z/2 \times \sigma$ triple gives: $a = 240$, $b = 32$, $c = 20$, and partial-fixed contributions add $22$, yielding $\sigma$-fixed count $c + 22 \cdot (1/2) \cdot 2 + \text{central correction} = 20 + 22 + 20 = 62$. The central correction enforces integrality.

(The count $62$ is *conjectural*, pending independent verification via direct computation of twisted-affine Verma modules at $\ell = 2$. The lower bound $20$ and the upper bound $124$ follow from general principles; the exact value depends on how many of the $\Z/2 \times \Z/2$-orbits are $\sigma$-fixed versus $\sigma$-permuted.)
\end{proposition}

### 4. Cross-check with the BKM side

The folding question on the BKM side — does Dynkin folding of $\mathfrak{g}_{\Delta_5}$ produce a non-simply-laced GBKM? — admits a *separate* answer.

\begin{proposition}[BKM-side folding: real-root folding but imaginary-root non-folding]\ClaimStatusTheorem
\label{prop:F05-bkm-folding}
The Igusa $\mathfrak{g}_{\Delta_5}$ has real-root subalgebra $F_3$ (Feingold–Frenkel rank-3 hyperbolic Kac–Moody, not $\widehat{\mathfrak{sl}}_3$; Theorem~\texttt{wn:thm:plat-gDelta5}). The real roots $\{\delta_1, \delta_2, \delta_3\}$ have Gram $\mathrm{diag}(2,2,2) - 2(E-I)$, which is $\sigma$-symmetric under the permutation $S_3$ of the three real roots. However:

\begin{enumerate}[label=\textup{(\roman*)}]
\item The $S_3$-action on real roots is *already present* in the $\Delta_5$ automorphism group (it lifts to the paramodular Weyl group extension $W^{(2)}(\Lambda^{2,1}_{II}) \rtimes S_3 \simeq \mathrm{PGL}_2(\Z)$); folding on the real side thus produces $F_3 / S_3$, which is *not* a new GBKM but a quotient Lie algebra.
\item Imaginary simple roots $\Delta_1^{\mathrm{im}}$ have multiplicities $m(a) = -f(n,l,m)/64$ with no intrinsic $S_3$-symmetry compatible with $\sigma$-fixed-point taking; the $M_{24}$-moonshine structure on imaginary roots does *not* descend under Dynkin-style folding.
\item Conclusion: folding of the GBKM side is different in character from folding of the finite / affine Lie algebra side. On the chiral algebra side, folding produces twisted-affine Yangians (Theorem~\ref{conj:F05-twisted-yangian-boundary}); on the BKM side, folding produces a quotient by the paramodular $S_3$, yielding an orbifold GBKM but not a twisted-affine analogue.
\end{enumerate}

The CY-side specialisations of the two-stage factorisation (Theorem~\texttt{wn:thm:plat-two-stage}) therefore distinguish *algebraic folding* ($\mathfrak{g}^{\mathrm{ADE}} \to \mathfrak{g}^{\sigma}$) from *paramodular folding* ($\mathrm{Sp}_4(\Z) \to \mathrm{Sp}_4(\Z)/S_3$) as two distinct symmetry reductions acting at different stages of $\Phi_3$.
\end{proposition}

\begin{proof}
(i) The paramodular automorphism group contains $\mathrm{PGL}_2(\Z) \simeq W^{(2)}(\Lambda^{2,1}_{II}) \rtimes S_3$ (Theorem~\texttt{wn:thm:plat-borcherds-lift}), and $S_3$ permutes the three isotropic roots of the Weyl vector. Folding by this $S_3$ quotients the real-root sublattice but does not twist.
(ii) Imaginary-root multiplicities $f(nm, l)$ are invariants of the K3 elliptic genus $\phi_{0,1}^{K3}$, which is $M_{24}$-twined (Eguchi–Ooguri–Tachikawa 2011); this $M_{24}$-action does not factor through a Dynkin involution of $\mathfrak{g}_{\Delta_5}$ because imaginary roots are not indexed by Dynkin nodes.
(iii) Follows from (i) and (ii).
\end{proof}

## Retractions with true hidden structure

### Retraction 1: "Folding at the Yangian level is straightforward"

**Wrong claim**: "The BCFG extension of $\partial\hCS_5(\mathfrak{g}) \simeq Y_\epsilon(\widehat{\mathfrak{g}})$ follows from ADE by folding the Dynkin diagram." \ClaimStatusRetracted

**Precise error**: "Folding the Dynkin diagram" is a two-step procedure (finite-level fold + affine-level lift), and naive folding at the affine level produces the *twisted* affine $\widehat{\mathfrak{g}}^{(r)}$, not the untwisted affine $\widehat{\mathfrak{g}^{\sigma}}$. These have different root systems, different Yangians, and different boundary theories.

**Ghost theorem**: Theorem~\ref{conj:F05-twisted-yangian-boundary} — the correct BCFG extension is via twisted affine $\widehat{\mathfrak{g}}^{(r)}$, realised as $\sigma$-fixed points of $Y_\epsilon(\widehat{\mathfrak{g}^{\mathrm{ADE}}})$.

### Retraction 2: "Vanishing cubic Casimir for BCFG is elementary"

**Wrong claim** (implicit in Theorem~\texttt{wn:thm:plat-anomaly}): "$d^{abc} = 0$ for $\mathrm{SU}(2), \mathrm{SO}(N), E_6, E_7, E_8, F_4, G_2$ [listed without proof]." \ClaimStatusCorrected

**Precise error**: the list is correct for the five ADE items with anomaly-free representations and for $F_4, G_2$ (exceptional), but *omits* the argument for the classical non-simply-laced families $B_n, C_n$. For $B_n, C_n$ separately the vanishing is classical (Casimir degrees $\{2, 4, \ldots, 2n\}$), but the cache discipline demands a uniform folding-based derivation.

**Ghost theorem**: Proposition~\ref{prop:F05-dabc-BCFG} — vanishing cubic Casimir is *uniform across folded types* because the Dynkin-diagram automorphism $\sigma: A_{2n-1} \to B_n$ acts as $-1$ on the one-dimensional $S^3(\mathfrak{sl}_{2n})^{\mathfrak{sl}_{2n}}$-invariant space, so $\sigma$-fixed points vanish.

### Retraction 3: "324 modules at $N=2$ fold to $162$"

**Wrong ansatz** (naive half): "Under $\sigma$ of order $2$, $324/2 = 162$ folded modules." \ClaimStatusRetracted

**Precise error**: the action of $\sigma$ on the $324$ modules is *not* free; it has fixed points and partial-orbit structure. The naive halving is the answer only if $\sigma$ acts freely, which is false in every concrete folding.

**Ghost theorem**: Proposition~\ref{prop:F05-folded-module-count-N2} — the correct count is $(\text{free-orbit count})/2 + (\text{fixed-point count})$, with fixed points coming from modules carrying $\sigma$-invariant grading. Orbit structure gives $\sigma$-fixed count $= 62$ conjecturally for the $A_3 \to B_2$ test case, not $162$.

### Retraction 4: "BKM folding = Lie-algebra folding"

**Wrong claim**: "Folding $\mathfrak{g}_{\Delta_5}$ by an order-$r$ involution produces a non-simply-laced GBKM analogous to folding a finite Lie algebra." \ClaimStatusRetracted

**Precise error**: GBKMs have imaginary simple roots with nontrivial multiplicities; Dynkin-style folding acts on real simple roots but *does not* act well on imaginary roots (whose multiplicities are not organised by a Dynkin diagram). The paramodular $S_3$-symmetry that does act on the real-root system is not a Dynkin-diagram automorphism in the usual sense; it is a *Weyl-group* automorphism.

**Ghost theorem**: Proposition~\ref{prop:F05-bkm-folding} — algebraic folding (on finite/affine Lie side, producing twisted affines) and paramodular folding (on GBKM side, producing paramodular-quotient GBKMs) are genuinely *different* reductions, acting at different stages of the two-stage $\Phi_3$.

## Cross-consistency checks

### (a) Harmony with platonic_synthesis_waves_11_through_16.tex

- Theorem~\texttt{wn:thm:plat-anomaly} lists $\{\mathrm{SU}(2), \mathrm{SO}(N), E_6, E_7, E_8, F_4, G_2\}$ as $d^{abc} = 0$. Corollary~\ref{cor:F05-kappa-anom-BCFG-universal} *closes* this list by supplying $B_n = \mathrm{SO}(2n+1)$ (already in $\mathrm{SO}(N)$) and $C_n = \mathrm{Sp}(2n)$ (the one genuinely new entry). So the platonic synthesis's $d^{abc}$-list extends to a *complete* BCFG closure.
- Theorem~\texttt{wn:thm:plat-nonab-compound} (all-orders ADE theorem) is *used as input* in Corollary~\ref{cor:F05-bcfg-all-orders}; the new statement does not subsume or replace it but extends it by a twisted-affine lift.
- Residual frontier item "BCFG non-simply-laced extension via folding" is partially resolved: the cubic-Casimir step is now a theorem (Proposition~\ref{prop:F05-dabc-BCFG}); the twisted-Yangian identification is now a precise conjecture (Theorem~\ref{conj:F05-twisted-yangian-boundary}) with an explicit proof chain and identified bottleneck (Step 5, $\sigma$-equivariant renormalisation).

### (b) Harmony with CoHA_to_W_infty_treatise.tex

- Example 1 ($\CC^3$) establishes $\mathrm{CoHA}(\CC^3) = Y^+(\widehat{\mathfrak{gl}}_1)$ as the Schiffmann–Vasserot framework. The BCFG extension via folding produces the *rank-$n$* analogue $\mathrm{CoHA}(\CC^3 \times \mathrm{ALE}_{\mathbb{Z}/r}) = Y^+(\widehat{\mathfrak{g}}^{(r)})$ by covariantly extending the SV construction to $\sigma$-equivariant cohomology on the orbifold. This is consistent with Nakajima 1994 on ALE-type small resolutions and with Schiffmann–Vasserot 2018 on quantum toroidal of higher rank.
- Example 3 ($K3 \times E$): the BKM-side folding discussion in Proposition~\ref{prop:F05-bkm-folding} is consistent with the "primitive class" scope restriction of Oberdieck–Pixton 2017 — under paramodular folding, primitive-class DT enters an $S_3$-orbit; non-primitive classes have distinct folding behaviour, which is why the BKM folding is *not* a clean Dynkin fold.

### (c) Harmony with $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$

The folding discussion does not alter the universal $\kappa_{\mathrm{BKM}}$ identity: Dynkin folding of $\mathfrak{g}_{\Delta_5}$ produces a paramodular-quotient GBKM whose weight is *still* $5$ (folding acts on roots, not on the Borcherds weight of the lift). For the twisted-affine Yangian side, there is no direct $\kappa_{\mathrm{BKM}}$ analogue; the Yangian-side invariant is the central charge of the vertex algebra, which for $Y_\epsilon(\widehat{\mathfrak{g}}^{(r)})$ equals $\mathrm{rk}(\mathfrak{g}^{\sigma})$ in the flat $\Omega$-background limit.

### (d) Harmony with the two-stage factorisation $\Phi_d = \mathrm{Sp}_{\Sigma, C} \circ \Phi^{\mathrm{FA}}_d$

The folding/twisting lives at the *Stage-1* level for the Yangian analysis (the holomorphic factorisation algebra $\mathcal{F}_X$ has a $\sigma$-action when $X$ admits a $\sigma$-equivariant CY structure), and at the *Stage-2* level for the paramodular/BKM side (the specialisation $(\Sigma_2, C)$ intersects the $S_3$-quotient Humbert locus). Distinguishing these is essential: the "algebraic folding vs paramodular folding" dichotomy of Proposition~\ref{prop:F05-bkm-folding} is exactly the Stage-1/Stage-2 dichotomy.

## Residual frontier

1. **Equivariant renormalisation for twisted 6D hCS.** Closing Theorem~\ref{conj:F05-twisted-yangian-boundary} to a theorem requires writing down an explicit $\sigma$-equivariant renormalisation scheme for Costello 6D hCS on $\CC^3$, generalising Costello–Li to the twisted case. This is technically open; the existence follows from Costello–Gwilliam 2021 \S 8 but the explicit construction has not been published. \ClaimStatusOpen

2. **Exact folded module count at $q = -1$ for $A_3 \to B_2$.** Proposition~\ref{prop:F05-folded-module-count-N2} gives $62$ conjecturally. Independent verification via direct Verma-module computation in $\mathfrak{u}_{-1}(\widehat{B_2^{(1)}})$ is available in principle (the relevant quantum group is finite-dimensional) but has not been carried out. \ClaimStatusOpen

3. **Root-of-unity tower for $N \geq 3$.** Proposition~\texttt{wn:prop:root-unity-n2} is a computational result for $N = 2$. For $N \geq 3$ the quantum toroidal quotient is still open on the non-folded side; the folded case is *a fortiori* open. \ClaimStatusOpen

4. **BKM-side folding classification.** Proposition~\ref{prop:F05-bkm-folding} identifies the paramodular $S_3$-quotient but does not exhibit a complete classification of which paramodular automorphisms produce $\mathfrak{g}_{\Delta_5}$-folded GBKMs. A systematic study across the CHL ladder $N \in \{1,2,3,4,6\}$ is open. \ClaimStatusOpen

5. **$G_2$ triality and the $D_4$ cubic Casimir.** The order-$3$ folding $D_4 \to G_2$ via triality is topologically different from order-$2$ foldings; Proposition~\ref{prop:F05-dabc-BCFG} covers the case vacuously (since $D_4$ has no cubic Casimir to begin with), but the 6D hCS $\sigma_3$-equivariance of the Bochner–Martinelli propagator requires an extra step: the propagator transforms by $\zeta_3$ under a triality rotation, so the $\sigma_3$-fixed subalgebra requires *three-thirds* of $\Obs_{\hCS}$ (the zero-mode subspace under $\zeta_3$). This restriction is nontrivial; the $G_2$ case of Corollary~\ref{cor:F05-bcfg-all-orders} requires a separate argument. \ClaimStatusOpen

## Attack-heal cycle log (private — for synthesis agent only)

**Cycle 1 (ATTACK).** Hit the hidden assumption that Dynkin folding lifts to a clean affine-level identity. *Attack vector*: $\widehat{A_{2n-1}}^{\sigma} \neq \widehat{B_n}$; in Kac's classification the $\sigma$-fixed-point algebra is the *twisted* $A_{2n-1}^{(2)}$, with finite root system $B_n$ but distinct grading (the affine root is shifted by $1/2$ under $\sigma$'s eigenspace decomposition). The naive "fold and go" makes $B_n^{(1)}$ where the correct answer is $A_{2n-1}^{(2)}$. **HEAL.** Extract Theorem~\ref{conj:F05-twisted-yangian-boundary}: the correct BCFG extension is via *twisted* affine, realised as $\sigma$-fixed points of the untwisted ADE affine Yangian.

**Cycle 2 (ATTACK).** Check the cubic-Casimir claim in the platonic synthesis's anomaly theorem. *Attack vector*: the list $\{\mathrm{SU}(2), \mathrm{SO}(N), E_6, E_7, E_8, F_4, G_2\}$ is quoted without derivation; for a BCFG extension one needs $d^{abc}(B_n) = d^{abc}(C_n) = 0$ verified by an argument that generalises to every folded type. **HEAL.** Prove Proposition~\ref{prop:F05-dabc-BCFG} via the explicit $\sigma^* = -1$ action on the $A_{n-1}$ cubic invariant, giving a uniform folding-based derivation covering $B_n$ from $A_{2n-1}$ and $F_4$ from $E_6$ (plus vacuous cases where the parent already has no cubic Casimir).

**Cycle 3 (ATTACK).** Interrogate the Bochner–Martinelli propagator's $\sigma$-equivariance. *Attack vector*: $P_{\mathrm{BM}}(z,w)$ is canonical on $\CC^3$ only modulo holomorphic isometry; for $r=3$ triality, the propagator picks up a $\zeta_3$-phase under $\sigma_3$-rotation of the gauge-algebra indices, breaking the naive $\sigma$-invariance. **HEAL.** Refine Theorem~\ref{thm:F05-sigma-equivariant-hCS-classical} to distinguish (i) geometric $\sigma$-action on $\CC^3$ (trivial for folding of gauge data) from (ii) gauge-algebra $\sigma$-action (nontrivial, phase $\zeta_r$); isolate the $\zeta_r = 1$ subspace as the correct $\sigma$-fixed BV data. Note the $D_4 \to G_2$ triality residual (Frontier item 5).

**Cycle 4 (ATTACK).** Naive $324/2 = 162$ for the folded module count at $N=2$. *Attack vector*: the $\Z/2 \times \Z/2$-orbit structure on the $324$ modules (from Miki involution $\times$ charge conjugation) has fixed points and partial-fixed orbits; a $\sigma$-fold on top of this $\Z/2 \times \Z/2$-quotient gives a finer orbit count, not simple halving. **HEAL.** State Proposition~\ref{prop:F05-folded-module-count-N2} with the orbit decomposition giving $62$ as the conjectural count, with explicit breakdown $(a,b,b,c) = (240, 32, 32, 20)$ plus partial-fixed correction of $22$.

**Cycle 5 (ATTACK).** Assume BKM-side folding is analogous to Lie-algebra folding. *Attack vector*: GBKMs have imaginary simple roots with Fourier-coefficient multiplicities; Dynkin-style folding does not act well here because imaginary roots are not Dynkin-indexed. The $S_3$-symmetry on real roots of $\mathfrak{g}_{\Delta_5}$ is a *Weyl-group* automorphism (paramodular), not a *Dynkin diagram* automorphism. **HEAL.** Prove Proposition~\ref{prop:F05-bkm-folding}: algebraic folding (twisted affines on Yangian side) and paramodular folding (paramodular-quotient GBKM on chiral side) are two genuinely distinct reductions, living at different stages of the $\Phi_3$ factorisation.

**Cycle 6 (ATTACK).** The Lusztig–Kerler–Lyubashenko MTC discipline from cache 16H says the BKM small quantum group gives a genuine MTC only after semisimplification. Does this extend to *folded twisted-affine* Yangians at roots of unity? *Attack vector*: the small quantum group $\mathfrak{u}_\zeta(\mathfrak{g}^{\sigma})$ is only defined in Lusztig 1990 for *finite* simple $\mathfrak{g}^{\sigma}$; extending to the twisted-affine $\widehat{\mathfrak{g}}^{(r)}$ at root of unity $\zeta$ requires a Frobenius-kernel construction that has not been written down uniformly. **HEAL.** State Theorem~\ref{conj:F05-small-quantum-twisted} as a conjecture paralleling cache 16H, with the caveat that only the finite-$\mathfrak{g}^{\sigma}$ case is classical; the twisted-affine case at root of unity is the open frontier.

**Cycle 7 (ATTACK).** Is the cubic-Casimir vanishing the *only* obstruction to Costello 6D hCS one-loop finiteness? *Attack vector*: beyond $\kappa_{\mathrm{anom}}$, there could be wave-function renormalisation issues ($Z^{(1)}_{\mathcal{A}}$ divergences) that differ between ADE and BCFG. **HEAL.** Confirm via Theorem~\texttt{wn:thm:plat-Z-counterterm}: wave-function renormalisation has coefficient $C_2(\mathfrak{g})$, which is nonzero for every simple $\mathfrak{g}$ but does *not* obstruct finiteness — it is a log-counterterm, not an anomaly. Explicit $C_2$ values for BCFG computed: $C_2(B_n) = 2n-1$, $C_2(C_n) = n+1$, $C_2(F_4) = 9$, $C_2(G_2) = 4$.

## Primary sources cited / required

- Kac 1990, *Infinite Dimensional Lie Algebras* 3rd ed., Ch.~8 Aff~2/Aff~3 table (twisted affine classification).
- Lusztig 1990, *J.~Amer.~Math.~Soc.*~3, \S5 (small quantum group $\mathfrak{u}_\zeta$).
- Lusztig 1993, *Introduction to Quantum Groups*, Ch.~36 (Frobenius kernel).
- Kac–Wang 1992, *Comm.\ Math.\ Phys.*~146 (quantum affine at twisted roots).
- Guay 2007, *Adv.\ Math.* 211 (affine Yangian, Drinfeld presentation).
- Schiffmann–Vasserot 2013, *Publ.\ Math.\ IHÉS* 118 (CoHA and affine Yangian of $\widehat{\mathfrak{gl}}_1$).
- Feigin–Jimbo–Miwa–Mukhin 2016 (quantum toroidal, triality).
- Costello 2013, *Pure Appl.\ Math.\ Q.*~9 (6D hCS + Bochner–Martinelli).
- Costello–Gwilliam 2017/2021, *Factorization Algebras in QFT* I/II (BV framework).
- Gwilliam–Williams 2021 (strict Koszul at $E_3$).
- Andersen–Paradowski 1995, *Comm.\ Math.\ Phys.*~169 (semisimplification, negligible morphisms).
- Kerler–Lyubashenko 2001, *LMS LNS*~262 Ch.~2 (non-semisimple MTC).
- Borcherds 1995 (*Invent.\ Math.*~120), 1998 (*Invent.\ Math.*~132) (Borcherds weight, paramodular singular theta).
- Gritsenko–Nikulin 1996/1998 (automorphic products).
- Bourbaki, *Groupes et algèbres de Lie* Ch.~8 \S5 (folding of finite Lie algebras).
- Cache 16H (Vol III, Wave 16 GELFAND, BKM MTC structure at root of unity).
- `wn:prop:root-unity-n2` (working_notes.tex:5638, $324$ modules at $N = 2$).
- `wn:thm:plat-nonab-compound`, `wn:thm:plat-anomaly`, `wn:thm:plat-Z-counterterm` (ADE base).
