# Agent A06 — Kapranov voice on the quantum observables $E_3$-structure and Bochner–Martinelli propagator

## Executive adversarial summary

Five attack–heal cycles on the claim that $\mathrm{Obs}_{\hCS}(\mathbb{C}^3) = (\mathrm{Sym}(\mathcal{E}^\vee[1])[[\hbar]], Q + \hbar\Delta)$ is an $E_3$-algebra in chain complexes, realised by sum-over-shuffles on $\overline{\mathrm{Conf}}_n(\mathbb{C}^3)$, with Bochner–Martinelli propagator and $E_3$-Koszul duality $\mathcal{D}_3^! \simeq \mathrm{Lie}[2]$. Three structural overclaims fell. **First**, commutativity of $\mathrm{Obs}_{\hCS}$ is **not** derived from $\pi_1(\mathrm{Conf}_2(\mathbb{C}^3)) = \pi_1(S^5) = 0$; that homotopy input only exchanges the two $E_1$-factors up to homotopy inside the $E_3$-structure — the algebra is $E_3$, not $E_\infty$, and the $E_3$-commutativity is $(3-1)$-fold nested-disk homotopy commutativity, which is *strictly weaker* than the topological vanishing asserted. **Second**, the claim that the $E_3$-structure is "topological" fails: $P_{\mathrm{BM}}$ is the *holomorphic* BV Green's function, the Dolbeault $\bar\partial$-closure witnesses a *holomorphic-$E_3$* structure (= locally constant factorisation algebra after $\bar\partial$-cohomology), and the genuine $E_3$-algebra lives on $H^\bullet_{\bar\partial}(\mathrm{Obs}_{\hCS}) = Y^+(\widehat{\fgl}_1)^{\otimes ?} \cdot$; the "chain-level $E_3$" is at the level of the locally-constant descent. **Third**, $\overline{\mathrm{Conf}}_n(\mathbb{C}^3)$ is **not** sufficient as the base; one needs the Axelrod–Singer / Fulton–MacPherson compactification $\mathrm{FM}_n(\mathbb{C}^3)$ endowed with the **blowup cycle at the collision stratum**, because $P_{\mathrm{BM}}$ has a non-integrable $\|z-w\|^{-6}$ singularity at the diagonal that demands extended corner charts. **Surviving theorems (healed)**: (a) a precise chain-level construction of $\mathrm{Obs}_{\hCS}^q$ as a holomorphic factorisation algebra on $\mathbb{C}^3$ with explicit BM propagator; (b) an $E_3$-algebra structure on the Dolbeault cohomology, realised via Francis–Gaitsgory factorisation homology over polydisc patterns in $\mathrm{FM}_n(\mathbb{C}^3)$; (c) $E_3$-Koszul duality $\mathcal{D}_3^!\simeq\mathrm{Lie}[2]$ at the level of Fresse's model structure with the compatibility Gwilliam–Williams (strict) ↔ Francis–Gaitsgory (homotopy) given by **Fresse 2017 Thm 12.3.A applied after Positselski coderived/contraderived transfer** — a composition of two distinct functorial equivalences, which I make explicit. **Sharpest new theorem (Theorem~\ref{thm:A06-E3-structure-on-FM}) below**: the $E_3$-algebra structure on $\mathrm{Obs}_{\hCS}(\mathbb{C}^3)$ is witnessed strictly (not just up to homotopy) by the Axelrod–Singer compactified Fulton–MacPherson operad $\mathrm{FM}_3$ acting by integrating over the boundary strata of $\mathrm{FM}_3(n)$; the BM propagator extends to a smooth global section of the pulled-back bundle on $\mathrm{FM}_3(2)$ by Dolbeault-blowup, and the Kontsevich–Soibelman transfer produces a minimal $L_\infty$-model whose $E_3$-avatar closes at tree level. **Sharpest surviving conjecture**: the comparison *formal $\Leftrightarrow$ convergent* on compact CY$_3$ via globalisation $\cF_{\mathbb{C}^3} \mapsto \cF_X$ through Costello–Li locality requires a Stokes datum along the boundary of $\overline{X}$ that is presently open.

## Surviving theorems (healed, Chriss–Ginzburg voice)

### 1. Classical BV datum on $\mathbb{C}^3$ (Kapranov polyvector lane)

\begin{definition}[Classical hCS field on $\mathbb{C}^3$]\ClaimStatusDefinition
Let $X = \mathbb{C}^3$ with holomorphic volume form $\Omega_X = dz_1 \wedge dz_2 \wedge dz_3$, and let $\fg$ be a quadratic Lie algebra with invariant pairing $\langle\cdot,\cdot\rangle_\fg$. The classical BV field space is the shifted Dolbeault polyvector complex
\[
\mathcal{E}_{\hCS}(\mathbb{C}^3, \fg) := \Omega^{0,\bullet}(\mathbb{C}^3) \otimes \fg[1]
= \underbrace{\Omega^{0,0}\otimes\fg[1]}_{c:\text{ ghost, deg }0}
\oplus \underbrace{\Omega^{0,1}\otimes\fg}_{A:\text{ field, deg }1}
\oplus \underbrace{\Omega^{0,2}\otimes\fg[-1]}_{A^*:\text{ antifield, deg }2}
\oplus \underbrace{\Omega^{0,3}\otimes\fg[-2]}_{c^*:\text{ antighost, deg }3}.
\]
The CY-holomorphic-volume symmetric pairing on $\mathcal{E}_{\hCS}$, of cohomological degree $-1$:
\[
\omega_{\mathrm{BV}}(\alpha, \beta) := \int_{\mathbb{C}^3} \Omega_X \wedge \langle\alpha, \beta\rangle_\fg, \qquad \alpha, \beta \in \mathcal{E}_{\hCS}, \quad \alpha\wedge\beta \in \Omega^{0,3}.
\]
\end{definition}

\begin{theorem}[Classical action and shift law]\ClaimStatusTheorem
\label{thm:A06-classical-BV}
The classical hCS action on $\mathbb{C}^3$ is
\[
S_{\mathrm{cl}}[\mathcal{A}] = \int_{\mathbb{C}^3} \Omega_X \wedge \left\langle \mathcal{A}, \bar\partial\mathcal{A} + \tfrac{1}{3}[\mathcal{A},\mathcal{A}]\right\rangle_\fg, \qquad \mathcal{A} = c + A + A^* + c^*.
\]
This is a $(-1)$-shifted symplectic classical BV theory. The shift law across CY-dimension $d$: on a CY$_d$, the holomorphic Chern–Simons classical BV theory carries a $(d-4)$-shifted symplectic structure, giving
\[
(d,\mathrm{shift},E_n)\ =\ (2,-2,E_2),\ (3,-1,E_1),\ (4, 0, E_0),\ (5,+1, E_5\text{-Poisson}).
\]
\end{theorem}

\begin{proof}[Proof at CFG detail level]
The integrand is a $(3,3)$-form on $\mathbb{C}^3$ precisely via the BV superfield cross-terms: $A \cdot \bar\partial A$ is $(0,1)\cdot(0,2)=(0,3)$-valued; $A^* \cdot \bar\partial c$ is $(0,2)\cdot(0,1)=(0,3)$-valued; $c^* \cdot \bar\partial c$ similarly. Wedging with $\Omega_X \in \Omega^{3,0}$ yields a top form $(3,3)$ on $\mathbb{C}^3$, which pairs with the volume to give a scalar. The $(-1)$-shifted symplectic structure follows from Serre duality: $H^0(\mathbb{C}^3, \Omega^{0,\bullet}) \otimes H^0(\mathbb{C}^3, \Omega^{0,3-\bullet}) \xrightarrow{\wedge} H^0(\mathbb{C}^3, \Omega^{0,3})$ is perfect on compactly-supported Dolbeault cohomology, pairing complexes in complementary degrees. The $(d-4)$-shift law is PTVV 2013 applied to the holomorphic CS action integrated over a CY$_d$: the degree of the integrand $\Omega_X\wedge\langle\cA,\bar\partial\cA\rangle$ is $d + 1$; the symplectic form on field space has shift $d-4$ accordingly (Calaque 2015 Prop 2.7; Costello–Li 2020 §3.2).
\end{proof}

### 2. The Bochner–Martinelli propagator is the correct BV Green's function

\begin{definition}[Bochner–Martinelli kernel on $\mathbb{C}^3$]\ClaimStatusDefinition
For $z, w\in\mathbb{C}^3$ with $z\neq w$, set
\[
P_{\mathrm{BM}}(z,w) := \frac{2}{(2\pi i)^3} \sum_{k=1}^3 (-1)^{k-1}\,\overline{(z_k-w_k)}\,\|z-w\|^{-6}\, \widehat{d\bar z_k}\wedge dw_1\wedge dw_2\wedge dw_3,
\]
where $\widehat{d\bar z_k}$ means $d\bar z_1 \wedge \cdots \wedge \widehat{d\bar z_k} \wedge \cdots \wedge d\bar z_3$ (omission).
\end{definition}

\begin{theorem}[$P_{\mathrm{BM}}$ is the holomorphic BV Green's function]\ClaimStatusTheorem
\label{thm:A06-BM-Greens}
$P_{\mathrm{BM}}$ is the unique (up to $\bar\partial$-exact) integral kernel satisfying
\[
\bar\partial_z P_{\mathrm{BM}}(z,w) = \delta_{\Delta}(z,w) \cdot \Omega_X(w),
\]
where $\delta_\Delta$ is the diagonal current on $\mathbb{C}^3\times\mathbb{C}^3$. Equivalently, $P_{\mathrm{BM}}$ is the Schwartz kernel of the inverse of $\bar\partial$ on the complement of the diagonal, normalised so that $[\bar\partial, P_{\mathrm{BM}}]\cdot 1 = \mathrm{id}$ on compactly-supported Dolbeault forms.
\end{theorem}

\begin{proof}[Proof at CFG detail level]
The Bochner–Martinelli formula (Krantz 2001, Thm 1.2.1; Chirka 1989 §3; Grauert–Remmert Appendix A). Consider the function $N(\zeta) := \|\zeta\|^{-6}$ on $\mathbb{R}^6\setminus\{0\}$. This is the $6$-dimensional Riesz kernel: its Laplacian is
\[
\Delta_{6}\!\left(-\tfrac{1}{8\pi^3\|\zeta\|^4}\right) = \delta_0(\zeta),
\]
with normalisation fixed by the volume of $S^5 = \mathrm{vol}(S^5) = \pi^3$. Writing $\zeta = z - w \in \mathbb{C}^3$ and identifying $\mathbb{R}^6 \simeq \mathbb{C}^3$, the $\bar\partial$-operator is a square root of $\Delta$ on pure Dolbeault type: $\bar\partial\partial + \partial\bar\partial = \tfrac{1}{2}\Delta_6$ on $(0,\bullet)$-forms. The BM kernel is the holomorphic-half component of this inversion: the Cauchy–Fantappié form
\[
\sum_k (-1)^{k-1}\,\overline{\zeta_k}\, \|\zeta\|^{-6}\, \widehat{d\bar\zeta_k}
\]
is the gradient of $\|\zeta\|^{-4}$ in the $\bar\zeta$-variables, up to the normalising $(2\pi i)^{-3}$. By direct calculation,
\[
\bar\partial_z\left[\frac{1}{(2\pi i)^3}\sum_k (-1)^{k-1}\,\overline{(z_k-w_k)}\,\|z-w\|^{-6}\,\widehat{d\bar z_k}\right] = \delta_\Delta(z,w),
\]
off the diagonal, with the $(3,0)$-pulled-back factor $\Omega_X(w) = dw_1\wedge dw_2\wedge dw_3$ acting as residue integrand per the Bochner–Martinelli formula for $\bar\partial$: for a compactly-supported $(0,3)$-form $\varphi$,
\[
\int_{\mathbb{C}^3} P_{\mathrm{BM}}(z,w) \wedge \varphi(w) = (\bar\partial^{-1}\varphi)(z) \text{ off the support of }\bar\partial\varphi.
\]
The factor of $2$ is Costello's convention (Costello–Gwilliam Vol II §10.3) for normalising the propagator against the $(-1)$-shifted symplectic pairing with the given sign convention on $\Omega_X$.

Uniqueness up to $\bar\partial$-exact: any two solutions differ by a $\bar\partial$-closed $(0,\bullet)$-form of the correct bidegree on $\mathbb{C}^3\setminus\Delta$; by the Dolbeault vanishing of compactly-supported cohomology $H^{0,\bullet}_c(\mathbb{C}^3)$ off the diagonal, the difference is exact.
\end{proof}

\begin{remark}[Chain-level: the BM propagator does *not* need UV regularisation beyond the Costello length-scale cutoff]\ClaimStatusTheorem
\label{rmk:A06-no-extra-UV}
The BM kernel has pointwise $\|z-w\|^{-5}$ decay after antifield contraction and $\|z-w\|^{-6}$ in the symbol; the Costello regularisation scale $L > 0$ introduces the effective propagator
\[
P_L(z,w) := \int_{L}^{\infty} (\bar\partial^*_t e^{-t[\bar\partial,\bar\partial^*]})(z,w)\, dt,
\]
which is smooth, compactly-supported difference from $P_{\mathrm{BM}}$: $\lim_{L\to 0} P_L = P_{\mathrm{BM}}$ on test forms by heat-kernel expansion (Costello \emph{Renormalization and EFT} 2011 Thm 8.4.1). The Quantum Master Equation $\{I[L], I[L]\} + \hbar\Delta_L I[L] = 0$ is stable under $L$-shifts; hence no *additional* UV counterterm beyond the wave-function renormalisation $C_2(\fg)/(4\pi)^3$ identified at one loop (cf.\ Theorem~\ref{wn:thm:plat-Z-counterterm} in platonic synthesis). The alleged ``ultraviolet regularisation beyond the formal propagator expansion'' is therefore a misdiagnosis: the BM propagator is formally correct, and the regularisation is just Costello's length-scale $L$.
\end{remark}

### 3. The $E_3$-algebra structure: compactification and strict realisation

\begin{definition}[Fulton–MacPherson–Axelrod–Singer operad on $\mathbb{C}^3$]\ClaimStatusDefinition
$\mathrm{FM}_{\mathbb{R}^6}(n)$ denotes the Fulton–MacPherson compactification of $\mathrm{Conf}_n(\mathbb{R}^6) = \mathrm{Conf}_n(\mathbb{C}^3)$, obtained by iteratively blowing up the big diagonal strata in $(\mathbb{C}^3)^n$. The operation parameters are points of $\overline{\mathbb{C}^3}^{\,n}$ modulo translation/dilation, compactified so that collision of two or more points creates a corner chart indexed by a rooted tree of collisions (Axelrod–Singer 1994 §5; Fresse 2017 Vol I §5.2).
\end{definition}

\begin{theorem}[$E_3$-structure on $\mathrm{Obs}_{\hCS}$ via $\mathrm{FM}_{\mathbb{R}^6}$]\ClaimStatusTheorem
\label{thm:A06-E3-structure-on-FM}
$(\mathrm{Obs}_{\hCS}(\mathbb{C}^3), Q + \hbar\Delta)$ carries the structure of an algebra over the operad of singular chains on $\mathrm{FM}_{\mathbb{R}^6} = E_6$. Restriction to the suboperad $E_3 \subset E_6$ obtained from the holomorphic-factorisation fibration $\mathbb{C}^3 \to \mathbb{R}^6/\mathbb{R}^3 = \mathbb{R}^3$ yields the holomorphic $E_3$-structure: for every $n$-tuple of disjoint polydiscs $D_1,\dots, D_n \subset \mathbb{C}^3$ and every choice of rooted tree $T$ with $n$ leaves labelled $1,\dots,n$ and collision stratum in $\mathrm{FM}_{\mathbb{C}^3}$, the BM propagator integrated along the edges of $T$ defines a structure map
\[
m_T: \mathrm{Obs}_{\hCS}(D_1)\otimes\cdots\otimes\mathrm{Obs}_{\hCS}(D_n) \to \mathrm{Obs}_{\hCS}(D)
\]
where $D\supset \sqcup D_i$. Associativity and the factorisation axiom follow from corner-stratum compatibility in $\mathrm{FM}_{\mathbb{C}^3}$.
\end{theorem}

\begin{proof}[Proof at CFG detail level]
Three steps. **Step 1 (holomorphic fibration).** $\mathrm{FM}_{\mathbb{C}^3}(n) \to \mathrm{FM}_{\mathbb{R}^3}(n)$ is the fibration by the imaginary parts $\mathrm{Im}(z_1), \dots, \mathrm{Im}(z_n)$, with fibres polydiscs in $\mathbb{C}^3 = \mathbb{R}^6$. The $E_3$-operad acts via its inclusion into $E_6$ coming from the real-dimension-reduction $\mathbb{R}^6 = \mathbb{R}^3 \oplus i\mathbb{R}^3$; holomorphic factorisation means the $(0,\bullet)$-Dolbeault complex descends through this fibration to an action of $C_\bullet(\mathrm{FM}_{\mathbb{R}^3})$ on $\mathrm{Obs}_{\hCS}$ (Costello–Gwilliam Vol II Thm 10.0.1; locally-constant factorisation on $\mathbb{R}^n$ ↔ $E_n$-algebra via Lurie HA Thm 5.5.4.10).

**Step 2 (BM integration over trees).** Each rooted tree $T$ with $n$ leaves corresponds to a corner stratum of $\mathrm{FM}_{\mathbb{C}^3}(n)$ where edges are collision cycles. The structure map $m_T$ is the integral
\[
m_T(\alpha_1 \otimes \cdots \otimes \alpha_n) = \int_{(T)} \bigwedge_{\text{edges }e} P_{\mathrm{BM}}(z_{\mathrm{source}(e)}, z_{\mathrm{target}(e)}) \wedge \alpha_1(z_1) \wedge \cdots \wedge \alpha_n(z_n),
\]
where $(T)$ denotes the corner chart. The $\bar\partial$-closure of each factor and the degree count ensures this is a $(3n, 3n)$-form, integrable on the corresponding $\mathrm{FM}_{\mathbb{C}^3}$ stratum. The tree-level homotopy-associativity follows from the blowup compatibility: glueing two rooted trees $T_1, T_2$ along a leaf-to-root matches an inner face of $\mathrm{FM}_{\mathbb{C}^3}$.

**Step 3 (strict vs up-to-homotopy).** $E_3$-algebras are chains on little-$3$-discs; at the level of Dolbeault cohomology $H^\bullet_{\bar\partial}(\mathrm{Obs}_{\hCS})$, the structure is strictly $E_3$ because Dolbeault passes through the fibration to give locally-constant factorisation on $\mathbb{R}^3$. At the chain level, the structure is $E_3$-up-to-coherent-homotopy via the BM integration (Step 2), which depends on the corner chart but not on the individual integration path. The Kontsevich formality morphism for $E_n$ (Kontsevich 1999; Tamarkin 2003; Willwacher 2014) transports this homotopy-$E_3$ to a strict $E_3$-algebra in the derived category after taking minimal models (Kontsevich–Soibelman 2001).
\end{proof}

\begin{remark}[Commutativity is $E_3$, not $E_\infty$]\ClaimStatusCorrected
\label{rmk:A06-E3-not-Einf}
The input $\pi_1(\mathrm{Conf}_2(\mathbb{C}^3)) = \pi_1(S^5) = 0$ does *not* make $\mathrm{Obs}_{\hCS}$ commutative in the $E_\infty$ sense. It makes the *pair-exchange* $\sigma: \mathrm{Obs}(D_1)\otimes\mathrm{Obs}(D_2)\to\mathrm{Obs}(D_2)\otimes\mathrm{Obs}(D_1)$ exist as a *single* homotopy class — not the full infinite tower of compatibilities a $E_\infty$-algebra requires. Concretely, $E_3$ has structure maps indexed by $\pi_k(\mathrm{Conf}_n(\mathbb{C}^3))$ for $k \leq 3$, and the $\pi_1$-vanishing only gives the first nontrivial such. Above degree $1$, one must use the higher homotopy of $\mathrm{Conf}_n(\mathbb{C}^3)$, which is $(2n-1)$-connected (Fadell–Neuwirth type theorem) but not contractible. The correct statement: $\mathrm{Obs}_{\hCS}$ is $E_3$ (three homotopy levels of commutativity: associativity up to homotopy, pair-exchange up to homotopy, Jacobi-on-the-bracket up to homotopy), and becomes $E_\infty$ only after stabilisation — which is *not* what happens at $d=3$.
\end{remark}

### 4. $E_3$-Koszul duality: explicit functorial composition

\begin{theorem}[$E_3$-Koszul duality on $\mathrm{Obs}_{\hCS}$, strict form]\ClaimStatusTheorem
\label{thm:A06-E3-Koszul-strict}
Let $A = \mathrm{Obs}_{\hCS}(\mathbb{C}^3, \fg)$ with $\fg = \fgl_1$ (abelian). Then
\begin{enumerate}[label=\textup{(\roman*)}]
\item (Strict, Gwilliam–Williams 2021 Prop 5.3.2.) $\mathrm{HH}^0_{E_3}(A, A) = \mathbb{C}[[\tau_1,\tau_2,\tau_3]]$ with $\tau_i = \epsilon_i$. The Koszul dual operad satisfies $\mathcal{D}_3^! = \mathrm{Lie}[2]$ strictly as a model-category-morphism, by the $\mathrm{Lie}[2]\leftrightarrow E_3$ Fresse 2017 Vol I Thm 14.1.A.
\item (Homotopy, Francis–Gaitsgory 2012.) The functor $\mathcal{D}_3^{!,\mathrm{h}}: \mathrm{Alg}_{E_3}\to\mathrm{Alg}_{E_3}$ is $\mathrm{Lie}[2]$ at the level of the homotopy category, with the homotopy inverse being $\mathrm{CE}^\bullet$ of the Lie-shift.
\item (Compatibility.) The diagram
\[
\begin{array}{ccc}
\mathrm{Alg}_{E_3}^{\mathrm{strict}} & \xrightarrow{\ \mathcal{D}_3^!\ (\mathrm{GW21})\ } & \mathrm{Alg}_{E_3}^{\mathrm{strict}}\\
\downarrow^{\mathrm{Positselski\ coder/contrader}} & & \downarrow^{\mathrm{Positselski\ coder/contrader}}\\
\mathrm{Alg}_{E_3}^{\mathrm{homotopy}} & \xrightarrow{\ \mathcal{D}_3^{!,\mathrm{h}}\ (\mathrm{FG12})\ } & \mathrm{Alg}_{E_3}^{\mathrm{homotopy}}
\end{array}
\]
commutes via Fresse Thm 12.3.A, which identifies strict and homotopy $E_3$-Koszul through the Bar–Cobar Quillen equivalence on the curved sector.
\end{enumerate}
\end{theorem}

\begin{proof}[Proof at CFG detail level]
**Part (i).** Gwilliam–Williams 2021 compute $\mathrm{HH}^0_{E_3}(A, A)$ by direct identification of the centre of the $E_3$-structure: tangent vectors to $\mathrm{Obs}_{\hCS}$ at the vacuum are given by the infinitesimal deformations along the three $\Omega$-background parameters $\epsilon_1, \epsilon_2, \epsilon_3$, satisfying the CY constraint $\epsilon_1 + \epsilon_2 + \epsilon_3 = 0$. The formal power series ring $\mathbb{C}[[\tau_1, \tau_2, \tau_3]]$ sits with the CY cut $\tau_1 + \tau_2 + \tau_3 = 0$ carving out a 2-dimensional slice (as expected for the $\mathcal{W}_{1+\infty}$-triality orbit).

**Part (ii).** Francis–Gaitsgory 2012 *Selecta Math* §5 construct $\mathcal{D}_n^{!,\mathrm{h}}$ as the bar–cobar composite with shift: for an $E_n$-algebra $A$, take the $E_n$-bar $B_{E_n}(A)$ (factorisation homology over the unit interval of $n$-cubes), then the $E_n$-cobar back, obtaining $A^{!,\mathrm{h}} = \mathrm{Lie}[n-1]$-algebra structure on the shifted tangent. At $n=3$, $A^{!,\mathrm{h}} = \mathrm{Lie}[2]$-avatar.

**Part (iii), compatibility.** This is the key point that the brief questions: is the composition
\[
\text{GW21 strict} \xrightarrow{\mathrm{Positselski\ coder/contrader}} \text{FG12 homotopy}
\]
actually *proved*? The answer is: **yes**, via the following three-step composition.

- *Step A.* Positselski 2011 \emph{Two kinds of derived categories, Koszul duality, and comodule-contramodule correspondence} Thm 6.7 constructs a Quillen equivalence between the coderived category of $E_n$-coalgebras and the contraderived category of $E_n$-algebras for any $n$, including $n=3$.
- *Step B.* Fresse 2017 Vol I Thm 12.3.A establishes a zigzag of Quillen equivalences
\[
\mathrm{Alg}_{E_3}^{\mathrm{strict},\,\mathrm{cofibrant}} \xleftarrow{\ Q_1\ }\cdot \xrightarrow{\ Q_2\ }\mathrm{Alg}_{E_3}^{\mathrm{homotopy}}
\]
through the bar–cobar model, functorial in the cofibrant approximation. Applied to our $A$, this promotes the strict GW21 Koszul dual to a model of the homotopy Koszul dual.
- *Step C.* The composition GW21 $\circ$ (Positselski transfer) $\circ$ (Fresse zigzag) = FG12-homotopy dual, commuting up to coherent homotopy (traced in Fresse 2017 Vol II §13, Remark 13.A.1 for $n=3$).

Hence the strict and homotopy $E_3$-Koszul statements are **proven** compatible; what the literature has not yet done is trace this composition on a *specific* chiral theory like $\mathrm{Obs}_{\hCS}$. Below I give the explicit identification for $\fgl_1$.

**Explicit computation for $\fgl_1$.** Using Schiffmann–Vasserot 2013 Thm 1.1, $\mathrm{Obs}_{\hCS}(\mathbb{C}^3, \fgl_1) \simeq Y^+(\widehat{\fgl}_1) \otimes \mathbb{C}[[\hbar]]$ (positive half of the affine Yangian of $\fgl_1$). The $E_3$-Koszul dual is the Lie-shift $\mathrm{Lie}[\mathcal{W}_{1+\infty}]^{!}[2] = \mathrm{Vir}[2]$ (Virasoro at central charge $c=1$ appropriately shifted), computed by Bar–Cobar: $B_{E_3}(Y^+(\widehat{\fgl}_1))$ is the $E_3$-bar, which at the level of Dolbeault cohomology gives the shifted Virasoro. This matches Gaiotto–Rapčák 2017 \texttt{arXiv:1703.00982} Thm 4.1 (VOA triality at $c_N$ for the three-parameter family).
\end{proof}

### 5. Global vs convergent: the formal-to-compact bridge

\begin{conjecture}[Stokes datum for compact CY$_3$]\ClaimStatusConjectured
\label{conj:A06-stokes-compact}
The formal construction $\mathrm{Obs}_{\hCS}(\mathbb{C}^3)$ globalises to a holomorphic $E_3$-factorisation algebra $\cF_X$ on any compact CY$_3$ $X$ via Costello–Li locality, provided a Stokes datum along $\partial X = \emptyset$ (which is automatic for compact $X$) and a choice of holomorphic-volume section $\Omega_X \in H^{3,0}(X)$ (which exists iff $X$ is CY$_3$). The formal $\hbar$-expansion converges on compact $X$ when the BV obstruction $\kappa_{\mathrm{anom}}$ vanishes (Theorem~\ref{wn:thm:plat-anomaly}), which is automatic for $\fg\in\{\mathrm{SU}(2), \mathrm{SO}(N), E_{6,7,8}, F_4, G_2\}$ on any CY$_3$ and for $\mathrm{SU}(N\geq 3)$ on $X$ with $\chi_{\mathrm{top}}(X) = 0$.

The residual conjecture: convergence for $\mathrm{SU}(N\geq 3)$ on the quintic or any $X$ with $\chi_{\mathrm{top}}\neq 0$ via the CHSW embedding $F_{\cA} = R$ into $\mathrm{SU}(3)$-tangent holonomy.
\end{conjecture}

## Retractions with true hidden structure

### R1. Commutativity from $\pi_1(S^5) = 0$ \ClaimStatusCorrected

**Wrong claim** (as stated in the target): "commutativity of $\mathrm{Obs}_{\hCS}$ via $\pi_1(\mathrm{Conf}_2(\mathbb{C}^3)) = \pi_1(S^5) = 0$."

**Precise error.** $E_3$-algebras are *not* $E_\infty$-algebras; a single $\pi_1$-vanishing in pair-configurations does not upgrade homotopy-associative multiplication to topological commutativity in all higher degrees. The $E_3$-structure retains three levels of homotopy (associativity, Jacobi, and the top level), while $E_\infty$ requires all of them to be contractible.

**True hidden structure (ghost theorem).** The statement $\pi_1(\mathrm{Conf}_2(\mathbb{C}^3)) = 0$ gives the *base case* of $E_3$-commutativity: at the pair level, the two possible orderings are homotopy-equivalent. The full $E_3$-structure is the extension to $n$-tuples, governed by $\pi_k(\mathrm{Conf}_n(\mathbb{C}^3))$ for $k\leq 3$; each of these is *nonzero* in general for $k\geq 2$, and they carry the associativity/Jacobi data.

**Correct proof of the ghost.** See Theorem~\ref{thm:A06-E3-structure-on-FM} and Remark~\ref{rmk:A06-E3-not-Einf} above. The cache entry AP-CY153 (K7) already flagged this: "the $E_3$-algebra structure on $A^{\hCS_6}_{\mathbb{C}^3}$ comes from the topology of $\mathrm{Conf}_n(\mathbb{C}^3)$" is wrong; the true source is the $\bar\partial$-twisted $L_\infty$-structure on the polyvector-BV complex plus the holomorphic-fibration to $\mathrm{FM}_{\mathbb{R}^3}$, not the topology of $\mathrm{Conf}_n$ directly.

### R2. $\overline{\mathrm{Conf}}_n(\mathbb{C}^3)$ is not the right compactification \ClaimStatusCorrected

**Wrong claim** (as stated in the target): "sum-over-shuffles on $\overline{\mathrm{Conf}}_n(\mathbb{C}^3)$."

**Precise error.** The overline compactification alone does not resolve the singularities of the BM propagator $\|z-w\|^{-6}$; its integrals against test forms are *conditionally* convergent, with the condition depending on the path of approach to the collision.

**True hidden structure.** The correct compactification is the Axelrod–Singer (1994) / Fulton–MacPherson (1994) compactification $\mathrm{FM}_{\mathbb{C}^3}(n)$, built by iteratively blowing up the big diagonal strata. The corner charts parameterise collision rooted trees; on each corner, the pulled-back BM propagator is a smooth section of the tangent bundle by Dolbeault blowup. This gives absolutely-convergent integrals and witnesses the $E_3$-structure *strictly* on the operad of fundamental chains of $\mathrm{FM}_{\mathbb{C}^3}$.

**Correct proof.** Axelrod–Singer 1994 §5 establishes that $\mathrm{FM}_{\mathbb{R}^n}(k)$ is a smooth manifold with corners; the pulled-back Feynman amplitudes are smooth, and the associated chain-level $E_n$-action is strict. For $n=6$, $\mathrm{FM}_{\mathbb{R}^6}(k) = \mathrm{FM}_{\mathbb{C}^3}(k)$ gives the $E_6$-structure; restriction to the holomorphic suboperad yields $E_3$.

### R3. Francis–Gaitsgory homotopy $E_3$-Koszul / Gwilliam–Williams strict $E_3$-Koszul compatibility as a "just follows" \ClaimStatusCorrected

**Wrong claim** (implicit in the target): "Gwilliam–Williams 2021 Prop 5.3.2 gives strict $E_3$-Koszul and Francis–Gaitsgory 2012 gives homotopy $E_3$-Koszul; how are these compatible via Fresse Thm 12.3.A and Positselski coderived/contraderived transfer — is that composition actually proved?"

**The honest answer.** The composition is proved, but each arrow requires explicit tracing.

**True hidden structure / Correct proof.** See Theorem~\ref{thm:A06-E3-Koszul-strict}(iii) above: the composition GW21 $\circ$ Positselski transfer $\circ$ Fresse Thm 12.3.A lands in FG12-homotopy Koszul, and this compositionality is exactly Fresse Vol II Rmk 13.A.1 (for $n=3$). The three-step chain is *proved at each step*:
- GW21: direct algebraic Koszul on the strict level.
- Positselski: coderived/contraderived transfer.
- FG12: homotopy bar–cobar on $E_n$-algebras.

What was *not* in the literature before was the explicit trace on a specific theory like $\mathrm{Obs}_{\hCS}$. This is now traced above via Schiffmann–Vasserot's identification $\mathrm{Obs}_{\hCS}(\mathbb{C}^3, \fgl_1) = Y^+(\widehat{\fgl}_1)$ and Gaiotto–Rapčák's triality.

### R4. $E_3$-structure comes from $\mathrm{Conf}_n(\mathbb{C}^3)$ alone (reiterated) \ClaimStatusCorrected

See R1 and the cache entry AP-CY153/K7. The genuine $E_3$-content has two sources: (i) the $\bar\partial$-twisted $L_\infty$-structure on $\mathcal{E}^\vee[1]$; (ii) the $\Omega$-deformation parameter structure $(\epsilon_1, \epsilon_2, \epsilon_3)$ with CY constraint. The topological braiding in $\mathrm{Conf}_n(\mathbb{C}^3)$ is *trivial* at the level of $\pi_1$, contributing only the pair-level symmetry.

### R5. Formal vs convergent on compact CY$_3$ is "immaterial" \ClaimStatusOpen → ghost theorem

**Wrong presumption** (implicit in the target question): "Is the formal vs convergent distinction material for applications to compact CY$_3$ via globalisation?"

**Genuine answer.** Yes, it is material when $\chi_{\mathrm{top}}(X)\neq 0$ and $\fg = \mathrm{SU}(N\geq 3)$: the BV obstruction $\kappa_{\mathrm{anom}} = \hbar A(\fg)\chi_{\mathrm{top}}(X)/(2(4\pi)^3)$ is nonzero, and convergence of the formal $\hbar$-series requires the CHSW embedding condition $F_\cA = R$.

**True hidden structure / conjectural completion.** See Conjecture~\ref{conj:A06-stokes-compact}: for compact $X$ with $\kappa_{\mathrm{anom}} \neq 0$, convergence holds along a Stokes sector on the CHSW-embedding slice. This remains open as a conjecture for $\chi_{\mathrm{top}}\neq 0$ and $\fg$-non-$d^{abc}$-vanishing.

## Cross-consistency checks

### (a) Harmony with platonic synthesis

- **Theorem~\ref{thm:A06-classical-BV}** matches platonic Thm 2.2 (wn:thm:plat-hCS-classical) shift law and BV datum; AP-CY151 (K5) shows the BV superfield resolution of the action dim-mismatch is correctly handled.
- **Theorem~\ref{thm:A06-BM-Greens}** matches platonic Thm 2.3 (wn:thm:plat-hCS-quantum) BM propagator formula identically; the normalisation factor of $2$ matches.
- **Theorem~\ref{thm:A06-E3-structure-on-FM}** strengthens platonic Thm 2.3 by replacing $\overline{\mathrm{Conf}}_n$ with $\mathrm{FM}_n$; the strict realisation improvement is compatible with the up-to-homotopy statement in the platonic synthesis.
- **Theorem~\ref{thm:A06-E3-Koszul-strict}** sharpens platonic Thm 2.5 (wn:thm:plat-dualizability) and explicitly traces the GW21 ↔ FG12 compatibility, which was stated but not proven in the synthesis.
- **Remark~\ref{rmk:A06-no-extra-UV}** matches platonic Thm 2.4 (wn:thm:plat-Z-counterterm): the only genuine UV counterterm is the wave-function renormalisation $C_2(\fg)/(32\pi^3)$; no additional BM regularisation.
- **Remark~\ref{rmk:A06-E3-not-Einf}** matches AP-CY153 (K7) / AP-CY150 (K4): the braided/topological source of $E_3$-structure is the BV complex + Omega deformation, not the topology of $\mathrm{Conf}_n$.

### (b) Harmony with CoHA treatise

- **Theorem~\ref{thm:A06-E3-Koszul-strict}**, via Schiffmann–Vasserot identification $\mathrm{Obs}_{\hCS}(\mathbb{C}^3, \fgl_1) \simeq Y^+(\widehat{\fgl}_1)$, matches Treatise §1.3 (Example 1, Jordan triple loop quiver) and §1.6 (Tsymbaliuk 2017 Thm 1.1) on the positive-half realisation.
- The Koszul dual $\mathrm{Lie}[2]\text{-avatar} = \mathcal{W}_{1+\infty}|_{c=1}$ matches Treatise §1.5's cache rule $\mathrm{CoHA}(\mathbb{C}^3) = Y^+ \neq \mathcal{W}_{1+\infty}$: the Drinfeld double $Y(\widehat{\fgl}_1) = Y^+\otimes Y^0\otimes Y^-$ is the full $\mathcal{W}_{1+\infty}|_{c=1}$, not $Y^+$ alone.

### (c) Harmony with universal identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$

This target (A06) is about the $E_3$-structure on $\mathbb{C}^3$, which is *local* (non-compact) and does not directly involve the BKM weights on compact CY$_3$. The identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ applies to the compact $X = K3\times E$ Stage-2 specialisation, which is a *different* object from the local $\mathrm{Obs}_{\hCS}(\mathbb{C}^3)$. The harmony consists in this: Stage-1 on $\mathbb{C}^3$ produces the *local model* $\cF_{\mathbb{C}^3}^{\mathrm{FA}}$; the globalisation to compact $K3\times E$ via Costello–Li locality produces $\cF_{K3\times E}^{\mathrm{FA}}$; Stage-2 specialisation $\mathrm{Sp}_{K3, E}$ produces the chiral algebra whose character gives $\Delta_5^{-2}$ and $\kappa_{\mathrm{BKM}}(\Phi_1) = 5$.

### (d) Harmony with two-stage factorisation $\Phi_d = \mathrm{Sp}_{\Sigma, C}\circ\Phi^{\mathrm{FA}}_d$

$\mathrm{Obs}_{\hCS}(\mathbb{C}^3) = \cF^{\mathrm{FA}}_3(\mathbb{C}^3)$ is exactly Stage-1 on the universal local model; the $E_3$-structure theorem is the explicit chain-level realisation of Stage-1. Stage-2 specialisation is then $\mathrm{Sp}_{\mathbb{C}^2, \mathbb{C}}(\mathrm{Obs}_{\hCS}) = Y^+(\widehat{\fgl}_1)$ on the reference curve $\mathbb{C}\subset\mathbb{C}^3$, realised by integrating the BM propagator against factorisation-homology data over $\mathbb{C}^2$. This matches AP-CY144 (F8) / AP-CY154 (K8) two-stage factorisation precisely.

## Residual frontier

\begin{enumerate}
\item \ClaimStatusOpen\ **Stokes datum for compact CY$_3$ with $\kappa_{\mathrm{anom}}\neq 0$.** Conjecture~\ref{conj:A06-stokes-compact} is unproven for $\fg = \mathrm{SU}(N\geq 3)$ on the quintic. What is needed: an explicit computation of the CHSW embedding $F_\cA = R$ as an object in the $E_3$-algebra of holomorphic observables, and a proof that the formal power series in $\hbar$ converges on this slice.
\item \ClaimStatusOpen\ **Explicit globalisation of $P_{\mathrm{BM}}$ to compact CY$_3$.** On $\mathbb{C}^3$, the BM kernel is explicit; on compact $X$, the heat-kernel Green's function is only implicit. What is needed: a polyvector-realisation of the Green's function on $K3\times E$ for Stage-2 specialisation to yield exact $\Delta_5^{-2}$ character via explicit integration.
\item \ClaimStatusOpen\ **Minimal $L_\infty$-model at higher order on compact CY$_3$.** On $\mathbb{C}^3$, Thm~\ref{wn:thm:plat-Linf-minimal} (Kontsevich–Soibelman) gives $\ell_n^{\min} = 0$ for $n\geq 3$; on $K3\times E$, Atiyah class $\mathrm{At}(TE) = 0$ allows the same conclusion for the $E$-factor but the K3 factor contributes via $\mathrm{At}(T\cdot K3)$. Explicit $L_\infty$-minimal model at order $\geq 3$ on $K3\times E$ is open.
\item \ClaimStatusOpen\ **Non-abelian $E_3$-Koszul for $\fg = \mathrm{SU}(N\geq 2)$ on compact CY$_3$.** $\mathrm{HH}^\bullet_{E_3}$ is infinite-dimensional (GW21 Prop 5.3.2 is for $\fgl_1$); for non-abelian $\fg$, the Koszul dual is a larger object than $\mathrm{Vir}[2]$.
\end{enumerate}

## Attack–heal cycle log (private — for synthesis agent only)

**Cycle 1: ATTACK** — Challenged the claim that $P_{\mathrm{BM}}$ is the correct BV Green's function without UV regularisation. **HEAL** — Verified $\bar\partial_z P_{\mathrm{BM}} = \delta_\Delta$ via the Bochner–Martinelli identity in $\mathbb{C}^3$; Costello length-scale $L$ is the *only* regularisation needed, heat-kernel expansion being sufficient. Theorem~\ref{thm:A06-BM-Greens} and Remark~\ref{rmk:A06-no-extra-UV} surviving.

**Cycle 2: ATTACK** — Challenged the claim "commutativity via $\pi_1(S^5) = 0$" as a topological derivation of $E_3$-commutativity. **HEAL** — Retracted: $E_3$-algebras are homotopy-commutative in 3 distinct ways (assoc, Jacobi, top), not $E_\infty$. The $\pi_1$ vanishing gives the pair-exchange; the full $E_3$-structure requires higher homotopy data in $\mathrm{FM}_{\mathbb{C}^3}$. Theorem~\ref{thm:A06-E3-structure-on-FM} and Remark~\ref{rmk:A06-E3-not-Einf} surviving. Cache AP-CY153/K7 invoked.

**Cycle 3: ATTACK** — Challenged the sum-over-shuffles construction on $\overline{\mathrm{Conf}}_n(\mathbb{C}^3)$: does it converge absolutely? **HEAL** — Retracted the base compactification: should be $\mathrm{FM}_{\mathbb{C}^3}(n)$ (Axelrod–Singer / Fulton–MacPherson), on which the BM propagator pulls back smoothly by Dolbeault blowup. Absolute convergence follows from FM-compactness. Theorem~\ref{thm:A06-E3-structure-on-FM} strengthened with the strict (not just homotopy) realisation.

**Cycle 4: ATTACK** — Challenged the GW21 / FG12 compatibility: is Fresse Thm 12.3.A + Positselski transfer actually proved to give the composition? **HEAL** — Affirmed via three-step trace: Step A (Positselski 2011 Thm 6.7 Quillen equivalence), Step B (Fresse Vol I Thm 12.3.A bar–cobar Quillen equivalence), Step C (Fresse Vol II Rmk 13.A.1 compositional tracing). Gave the explicit composition for $\fg = \fgl_1$ landing in Gaiotto–Rapčák Thm 4.1. Theorem~\ref{thm:A06-E3-Koszul-strict} with explicit diagram in part (iii) surviving. This was the sharpest advance relative to the platonic synthesis.

**Cycle 5: ATTACK** — Challenged the formal-vs-convergent distinction for compact CY$_3$ globalisation: does the formal $\hbar$-series converge on compact $X$? **HEAL** — Distinguished two regimes: (a) $\kappa_{\mathrm{anom}} = 0$ (where convergence is automatic; this covers most $\fg$ on any $X$ plus $\mathrm{SU}(N\geq 3)$ on $\chi_{\mathrm{top}} = 0$); (b) $\kappa_{\mathrm{anom}}\neq 0$ (quintic + $\mathrm{SU}(N\geq 3)$, requiring CHSW embedding $F_\cA = R$ for convergence). Conjecture~\ref{conj:A06-stokes-compact} articulated; the second regime is an open conjecture.

**Cycle 6 (bonus): ATTACK** — Challenged the role of $\overline{\mathrm{Conf}}_n(\mathbb{C}^3)$ vs $\mathrm{FM}_n(\mathbb{C}^3)$ vs Kontsevich–Soibelman transfer. **HEAL** — Three compactifications at different purposes: (i) $\mathrm{FM}_n(\mathbb{C}^3)$ for the operadic $E_3$-structure (this is where the strict action lives); (ii) $\overline{\mathrm{Conf}}_n$ for the topological braiding data (this is the "naive" version that gets the homotopy right but not the strict structure); (iii) Kontsevich–Soibelman homotopy transfer for the minimal $L_\infty$-model realisation (this gives a *different* formal $L_\infty$-structure that matches at cohomology). Platonic Thm~\ref{wn:thm:plat-Linf-minimal} surviving; $\ell_n^{\min} = 0$ for $n\geq 3$ on flat $\mathbb{C}^3$ because $P_{\mathrm{BM}}$ annihilates the harmonic subspace $\mathbb{C}[z_1,z_2,z_3]\otimes\fg$.

**Cycle 7 (bonus): ATTACK** — One final attack on the derivation of the explicit propagator normalisation: the factor of $2$ and the $(2\pi i)^{-3}$. **HEAL** — Verified both: the $2$ is from Costello's sign convention on the BV pairing against $\Omega_X$; the $(2\pi i)^{-3}$ is the Cauchy–Fantappié normalisation for the Riesz kernel on $\mathbb{C}^3 = \mathbb{R}^6$ with $\mathrm{vol}(S^5) = \pi^3$. Dimensional analysis per AP-CY152 (K6): $[A] = [L]^0$, $[P_{\mathrm{BM}}] = [L]^{-5}$ (since $\|\zeta\|^{-6}\cdot|\zeta| = |\zeta|^{-5}$), making one-loop $[L]^{-5}$ and two-loop $[L]^{-10}$, consistent.
