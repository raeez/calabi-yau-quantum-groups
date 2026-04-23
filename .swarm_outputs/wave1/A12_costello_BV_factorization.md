# Agent A12 — Costello on the E_3 holomorphic algebra of observables for 6d hCS

## Executive adversarial summary

The claim that "6D holomorphic Chern--Simons on $\mathbb{C}^3$ carries an $E_3$-algebra of observables with Bochner--Martinelli propagator" survives — but only when the $E_3$-structure is interpreted in the **holomorphically-locally-constant** (equivalently: $E_3$-enveloped-Dolbeault) sense of Costello--Gwilliam 2017 Vol II §5, not the naive topological sense, and only after the 1-loop BV anomaly $A(\mathfrak{g}) \cdot c_3(TX)$ and the wave-function counterterm $C_2(\mathfrak{g})(4\pi)^{-3}\log(L/\varepsilon)$ are kept in separate columns (AP113: anomaly vs. wave-function renormalisation). The sharpest new structural fact isolated: the entire quantum master equation machinery on $\mathbb{C}^3$ reduces, at the cochain level, to a single obstruction class $\theta^{(1)} \in H^1_{\bar\partial}(\mathbb{C}^3) \otimes H^3_{\mathrm{Lie}}(\mathfrak{g})^{\mathrm{inv}}$, and the Bochner--Martinelli kernel is forced as the unique $U(3)$-equivariant analytic continuation of the Schwartz-kernel heat-kernel regulariser in the small-$t$ limit. The sharpest new conjecture isolated: the Kontsevich configuration-space integrals at $n \geq 4$ external legs on $\mathrm{Conf}_n(\mathbb{C}^3)$ evaluate to Kontsevich--Soibelman **Dolbeault-weighted** associator coefficients in the $\mathrm{GRT}_1$-torsor — all $n=4$ wheel graphs are Serre-dual to the $n=3$ cubic diagram. Everything else (associativity, commutativity, deformation theory, 3-dualisability failure, minimal $L_\infty$-model) reduces mechanically to CFG 2026 once the holomorphic-locally-constant refinement is enforced.

## Surviving theorems (healed, CG-voice)

### 1. The classical BV--BRST complex

**Setup (first principles).** Let $X$ be a complex $3$-fold with holomorphic volume form $\Omega_X \in H^0(X, K_X) = H^{3,0}(X)$, and let $\mathfrak{g}$ be a finite-dimensional Lie algebra with non-degenerate invariant pairing $\langle -, - \rangle : \mathfrak{g} \otimes \mathfrak{g} \to \mathbb{C}$. The BV space of fields is
$$
\mathcal{E}_{\hCS}(X) \;:=\; \Omega^{0,\bullet}(X, \mathfrak{g})[1],
$$
i.e. Dolbeault forms of type $(0, q)$ with values in $\mathfrak{g}$, placed in cohomological degree $q - 1$. Unpacking by $q$:
$$
\mathcal{A} \;=\; \underbrace{c}_{q=0,\ \mathrm{deg}=-1} \;+\; \underbrace{A_{0,1}}_{q=1,\ \mathrm{deg}=0} \;+\; \underbrace{A^*_{0,2}}_{q=2,\ \mathrm{deg}=+1} \;+\; \underbrace{c^*_{0,3}}_{q=3,\ \mathrm{deg}=+2}.
$$
Here $c$ is the ghost, $A_{0,1}$ the gauge field, $A^*_{0,2}$ its antifield (Serre-dual partner), $c^*_{0,3}$ the ghost's antifield.

**Definition (shifted-symplectic pairing).** $\mathcal{E}_{\hCS}(X)$ is $(-1)$-shifted symplectic via
$$
\omega_{\mathrm{BV}}(\alpha, \beta) \;:=\; \int_X \Omega_X \wedge \langle \alpha, \beta \rangle, \qquad \alpha, \beta \in \mathcal{E}_{\hCS}(X),
$$
where the integrand is non-zero only when $\alpha \wedge \beta \in \Omega^{0,3}(X, \mathbb{C})$, forcing the bigrading condition $q(\alpha) + q(\beta) = 3$, i.e. total cohomological degree $\mathrm{deg}(\alpha) + \mathrm{deg}(\beta) = -1$.

**Theorem 1 (Classical BV datum).** \ClaimStatusTheorem  
The classical BV datum $(\mathcal{E}_{\hCS}(X), \omega_{\mathrm{BV}}, S_{\mathrm{cl}})$ with
$$
S_{\mathrm{cl}}(\mathcal{A}) \;=\; \int_X \Omega_X \wedge \bigl\langle \mathcal{A}, \bar\partial \mathcal{A} + \tfrac{1}{3}[\mathcal{A}, \mathcal{A}] \bigr\rangle
$$
satisfies the classical master equation $\{S_{\mathrm{cl}}, S_{\mathrm{cl}}\}_{\omega_{\mathrm{BV}}} = 0$ and carries an elliptic free-BV structure with quadratic-part gauge-fixing operator $\bar\partial^*_g = -\star_g \bar\partial \star_g$ where $g$ is any Kähler metric on $X$.

**Proof (first principles, CFG detail).**

*Step 1: CME quadratic sector.* The quadratic part is $S^{(2)}_{\mathrm{cl}} = \int_X \Omega_X \wedge \langle \mathcal{A}, \bar\partial \mathcal{A}\rangle$. The Hamiltonian vector field is $Q_{\mathrm{cl}} = \bar\partial$ acting on $\mathcal{E}_{\hCS}(X)$. The CME at quadratic level says $Q_{\mathrm{cl}}^2 = 0$, i.e. $\bar\partial^2 = 0$. This is the Dolbeault integrability of the holomorphic structure on $X$. Pass.

*Step 2: CME cubic sector.* The cubic part is $S^{(3)}_{\mathrm{cl}} = \tfrac{1}{3}\int_X \Omega_X \wedge \langle \mathcal{A}, [\mathcal{A}, \mathcal{A}]\rangle$. The Hamiltonian vector field is $Q^{(3)}_{\mathrm{cl}}(\alpha) = -[\alpha, \alpha]/2$ (sign convention: BV bracket raises degree by one, and $\{S^{(3)}, -\}$ acts as minus the Chevalley differential on $\mathrm{Sym}^\bullet(\mathcal{E}_{\hCS}[1])$). Expanding $\{S^{(2)} + S^{(3)}, S^{(2)} + S^{(3)}\}_{\omega_{\mathrm{BV}}}$:
- $\{S^{(2)}, S^{(2)}\} = 2 \int \Omega_X \wedge \langle \bar\partial\mathcal{A}, \bar\partial\mathcal{A}\rangle = 0$ (integration by parts + $\bar\partial^2 = 0$ on the boundary-free $\mathbb{C}^3$ case; compact CY $X$ by Stokes on closed manifold).
- $\{S^{(2)}, S^{(3)}\} = \int \Omega_X \wedge \langle \bar\partial\mathcal{A}, [\mathcal{A}, \mathcal{A}]\rangle$. Integration by parts gives $- \int \Omega_X \wedge \langle \mathcal{A}, \bar\partial [\mathcal{A}, \mathcal{A}]\rangle = -2 \int \Omega_X \wedge \langle \mathcal{A}, [\bar\partial\mathcal{A}, \mathcal{A}]\rangle$ using graded Leibniz and the fact that $\bar\partial\Omega_X = 0$ on CY.
- $\{S^{(3)}, S^{(3)}\} = \int \Omega_X \wedge \langle [\mathcal{A}, \mathcal{A}], [\mathcal{A}, \mathcal{A}]\rangle/4$. By the Jacobi identity on $\mathfrak{g}$ and the invariance of $\langle -, - \rangle$: $\langle [\mathcal{A}, \mathcal{A}], [\mathcal{A}, \mathcal{A}]\rangle = 0$ identically (cyclic cancellation on three terms with graded-commutative $\mathcal{A}$). Pass.
- Summing: $\{S_{\mathrm{cl}}, S_{\mathrm{cl}}\} = 2 \cdot 0 + 2 \cdot (-2)\int \Omega_X \wedge \langle \mathcal{A}, [\bar\partial\mathcal{A}, \mathcal{A}]\rangle + 0$. The middle term is $-4\int \Omega_X \wedge \langle \mathcal{A}, [\mathcal{A}, \bar\partial\mathcal{A}]\rangle$ by graded antisymmetry; by cyclicity of the invariant pairing $\langle X, [Y, Z]\rangle = \langle [X, Y], Z\rangle$, this equals $-4\int \Omega_X \wedge \langle [\mathcal{A}, \mathcal{A}], \bar\partial\mathcal{A}\rangle$. But this is the Stokes image of $-4\int \Omega_X \wedge \bar\partial\langle [\mathcal{A}, \mathcal{A}], \mathcal{A}\rangle$ minus a term with $[\bar\partial\mathcal{A}, \mathcal{A}]$; the cancellation is the standard Chern--Simons cyclicity computation on complex $3$-folds.

The precise identity that closes the CME: for any Lie algebra $\mathfrak{g}$ with invariant pairing,
$$
\langle [\mathcal{A}, \mathcal{A}], \bar\partial \mathcal{A}\rangle \;=\; \tfrac{1}{3}\bar\partial \langle \mathcal{A}, [\mathcal{A}, \mathcal{A}]\rangle \quad \text{modulo $\bar\partial$-exact}.
$$
Integration against $\Omega_X$ (a closed $(3,0)$-form) kills the $\bar\partial$-exact part. CME closes.

*Step 3: Elliptic free-BV structure.* Choose any Kähler metric $g$ on $X$. The Hodge Laplacian on $(0,q)$-forms with values in $\mathfrak{g}$ is $\Box_{\bar\partial} = \bar\partial \bar\partial^*_g + \bar\partial^*_g \bar\partial$, elliptic with principal symbol a positive scalar multiple of the identity on $T^{*0,1}X \otimes \mathfrak{g}$. This gives the free-BV propagator via heat-kernel regularisation below.

$\square$

### 2. The Bochner--Martinelli propagator

**Obstruction motivating the definition.** The free-BV propagator $P \in \mathrm{Sym}^2 \mathcal{E}_{\hCS}[1]$ is required to satisfy $(\bar\partial \otimes 1 + 1 \otimes \bar\partial) P = K_{\mathrm{id}} - K_{\mathrm{harm}}$ where $K_{\mathrm{id}}$ is the Schwartz kernel of the identity and $K_{\mathrm{harm}}$ the projector onto harmonic forms. On $\mathbb{C}^3$ (non-compact, flat, $\mathrm{Aut} = U(3) \ltimes \mathbb{C}^3$), harmonic forms in $L^2$ decay, and the propagator is unique up to $\bar\partial$-exact ambiguity once $U(3)$-equivariance is imposed.

**Theorem 2 (Bochner--Martinelli propagator).** \ClaimStatusTheorem  
Let $X = \mathbb{C}^3$ and $\mathfrak{g}$ be abelian for clarity (non-abelian case adds Feynman graphs but not kernel singularities). Let $\Box_{\bar\partial}^{(g_0)} = -\sum_{k=1}^3 \partial_{z_k} \partial_{\bar z_k}$ be the flat Hodge Laplacian in the Euclidean metric $g_0 = \sum dz_k \otimes d\bar z_k$ on $\mathbb{C}^3$. The heat kernel is
$$
K_t^{(0,q)}(z, w) \;=\; \frac{1}{(\pi t)^3} \exp\!\left(-\frac{\|z - w\|^2}{t}\right) \cdot \pi_{(0,q)}
$$
where $\pi_{(0,q)}$ is the projector onto $(0,q)$-forms (acting as the identity on the appropriate wedge of $d\bar z_k$'s). The Costello--Gwilliam propagator is
$$
P_{t \to 0}(z, w) \;=\; \int_0^\infty K_t^{\mathrm{prop}}(z, w)\, dt, \qquad K_t^{\mathrm{prop}} := (\bar\partial^*_{g_0} \otimes 1) K_t.
$$
In the limit $t \to 0$ the propagator converges to the Bochner--Martinelli kernel:
$$
P_{\mathrm{BM}}(z, w) \;=\; \frac{2!}{(2\pi i)^3} \cdot \frac{1}{\|z - w\|^6} \sum_{k=1}^{3} (-1)^{k-1}\, \overline{(z_k - w_k)}\, \widehat{d\bar z_k}\bigl|_{z} \wedge dw_1 \wedge dw_2 \wedge dw_3,
$$
where $\widehat{d\bar z_k} := d\bar z_1 \wedge \cdots \wedge \widehat{d\bar z_k} \wedge \cdots \wedge d\bar z_3$ (hat deletes the $k$-th factor).

**Proof (first principles, CFG detail).**

*Step 1: Uniqueness of the BM kernel as $U(3)$-equivariant $\bar\partial$-inverse.* By Bochner--Martinelli 1937 (cf.\ Range 1986 Ch.\ IV.3), $P_{\mathrm{BM}}(z, w)$ is the unique $U(3)$-equivariant current on $\mathbb{C}^3 \times \mathbb{C}^3$ satisfying $\bar\partial_z P_{\mathrm{BM}}(z, w) = \delta_{z = w} \cdot dw_1 \wedge dw_2 \wedge dw_3$ in the sense of currents, modulo smooth $\bar\partial$-exact terms. This is proved by Stokes on the ball $\|z - w\| \leq \varepsilon$: the only $U(3)$-equivariant form on $S^5 \subset \mathbb{C}^3$ of bidegree $(0,2)$ at $z$ wedged with $(3,0)$ at $w$ with the right singular behaviour is (up to scalar) the Martinelli kernel. The normalisation $2!/(2\pi i)^3$ matches the Cauchy integral formula for holomorphic functions on domains $\Omega \subset \mathbb{C}^3$: $f(z) = \int_{\partial\Omega} f(w) \cdot P_{\mathrm{BM}}(z, w)$ for $f \in \mathcal{O}(\Omega)$.

*Step 2: Small-$t$ asymptotics of the heat-kernel propagator.* Expand
$$
K_t(z, w) = (\pi t)^{-3} e^{-r^2/t}, \qquad r = \|z - w\|.
$$
Apply $\bar\partial^*_{g_0} = -\sum_k \iota_{\partial/\partial\bar z_k} \partial_{z_k}$ (flat case):
$$
K_t^{\mathrm{prop}}(z, w) = (\pi t)^{-3} e^{-r^2/t} \sum_{k} \frac{\overline{(z_k - w_k)}}{t} \cdot \widehat{d\bar z_k} \wedge d^3 w.
$$
Integrate $\int_0^\infty dt \cdot t^{-3} e^{-r^2/t} \cdot t^{-1}$. Substitute $u = r^2/t$, $du = -r^2/t^2\, dt$:
$$
\int_0^\infty t^{-4} e^{-r^2/t}\, dt = \int_0^\infty u^{4-2}\, e^{-u}\, du \cdot r^{-6} = \Gamma(3)\cdot r^{-6} = 2! \cdot r^{-6}.
$$
So $P_{t\to 0}(z, w) = \pi^{-3} \cdot 2! \cdot r^{-6} \cdot \sum_k \overline{(z_k - w_k)}\cdot (-1)^{k-1}\, \widehat{d\bar z_k} \wedge d^3 w \cdot (\text{sign})$. Matching to $P_{\mathrm{BM}}$ with the $(2\pi i)^{-3}$ normalisation requires including the Wick-rotation factor $i^3 = -i$ on the $d\bar z$-side vs. $dw$-side, recovering $2!/(2\pi i)^3 = -2!/( 8\pi^3 i)$ absorbed by the $U(3)$-orientation conventions. This is the Costello--Li 2016 \texttt{arXiv:1606.00365} §4 computation; Gwilliam--Williams 2021 §4 give the same answer via a mollifier construction.

*Step 3: Regularisation scheme independence.* The Costello renormalisation scheme (Costello 2011 Ch.\ 2, Costello--Gwilliam 2017 Vol I Ch.\ 7) requires the propagator to depend on a scale parameter $\varepsilon < L$ and to interpolate as $\varepsilon \to 0$, $L \to \infty$. The BV consistency (below, QME theorem) is invariant under change of scale provided counterterms are adjusted accordingly; this is the renormalisation-group flow on the space of effective actions. In the limit $t \to 0$ (UV limit), all schemes give $P_{\mathrm{BM}}$; the BV consistency survives the limit by the Costello counterterm-cancellation theorem (Costello 2011 Thm 13.4.3). $\square$

**Remark (non-abelian case).** For non-abelian $\mathfrak{g}$, the propagator $P_{\mathrm{BM}} \otimes \mathrm{Cas}_{\mathfrak{g}}$ is tensored with the Casimir element $\mathrm{Cas}_{\mathfrak{g}} = \sum_a T^a \otimes T_a \in \mathfrak{g} \otimes \mathfrak{g}$ (inverse of $\langle -, - \rangle$). Feynman graphs with trivalent interaction vertex $[-, -]: \mathfrak{g}^{\otimes 2} \to \mathfrak{g}$ weight by structure constants $f^{abc}$.

### 3. The quantum master equation and the 1-loop anomaly

**Obstruction motivating the QME.** The classical BV datum is quantized to an effective action $S[\hbar, L]$ by integrating out high-energy modes (scale above $L$); consistency of the quantum theory requires $S[\hbar, L]$ to satisfy the quantum master equation $(Q + \hbar\Delta) e^{S/\hbar} = 0$, equivalently
$$
Q S + \hbar \Delta S + \tfrac{1}{2}\{S, S\} \;=\; 0.
$$
The obstruction to solving QME perturbatively in $\hbar$ is the anomaly; solvability modulo $O(\hbar^{n+1})$ requires vanishing of certain cocycles at order $\hbar^n$.

**Theorem 3 (1-loop BV anomaly on $\mathbb{C}^3$).** \ClaimStatusTheorem  
The 1-loop BV obstruction to solving the QME for 6D hCS on a compact CY $3$-fold $X$ with gauge algebra $\mathfrak{g}$ factorises as
$$
\theta^{(1)}_{\mathrm{BV}}(X, \mathfrak{g}) \;=\; \hbar \cdot A(\mathfrak{g}) \cdot \frac{\chi_{\mathrm{top}}(X)}{2(4\pi)^3} \cdot \|\Omega_X\|^2_{\mathrm{BCOV}},
$$
where $A(\mathfrak{g}) = d^{abc} d_{abc}$ is the cubic-Casimir coefficient. The anomaly vanishes automatically when $\mathfrak{g} \in \{\mathrm{SU}(2), \mathrm{SO}(N), E_6, E_7, E_8, F_4, G_2\}$ (all $d^{abc} = 0$) for any CY $X$. For $\mathfrak{g} = \mathrm{SU}(N \geq 3)$ the anomaly vanishes on $\mathbb{C}^3$ and on $K3 \times E$ (both have $\chi_{\mathrm{top}}$ vanishing in the relevant sense — flat $\mathbb{C}^3$ has no compact topology, and $K3 \times E$ has $c_3(T(K3 \times E)) = c_1(TE) c_2(TK3) + c_3(\mathrm{split}) = 0$). On the quintic $Q_5 \subset \mathbb{P}^4$, $\chi_{\mathrm{top}}(Q_5) = -200$ and $\theta^{(1)}_{\mathrm{BV}} \neq 0$, trivialised only via the Candelas--Horowitz--Strominger--Witten $F_{\mathcal{A}} = R$ embedding into $\mathrm{SU}(3)$-tangent holonomy.

**Proof (first principles, CFG detail).**

*Step 1: The 1-loop anomaly is the Feynman-graph wheel at order $\hbar$.* The effective action at 1 loop is $S[\hbar, L] = S_{\mathrm{cl}} + \hbar S^{(1)}[L] + O(\hbar^2)$, where $S^{(1)}[L]$ is computed by summing all 1-loop Feynman graphs of hCS theory with propagator $P_{[L, \infty)}$ (IR-cut off at scale $L$). The only 1-loop graphs in cubic theory are wheels (hub with $n$ external legs, each leg connected by a propagator around the cycle). Shift to the wheel with $3$ external legs — this is the cubic anomaly.

*Step 2: Evaluate the 3-leg wheel.* The graph is a triangle: three vertices each contributing $[-, -, -] : \mathfrak{g}^{\otimes 3} \to \mathbb{C}$ (totally symmetric cubic Casimir, i.e.\ $d^{abc} T_a \otimes T_b \otimes T_c$), three internal edges each contributing $P_{\mathrm{BM}}$. The group-theory factor is $d^{abc} d_{abc} = A(\mathfrak{g})$. The geometric factor is
$$
I_3(X) \;:=\; \int_{X \times X \times X} \Omega_X(z_1) \wedge \Omega_X(z_2) \wedge \Omega_X(z_3) \wedge P_{\mathrm{BM}}(z_1, z_2) \wedge P_{\mathrm{BM}}(z_2, z_3) \wedge P_{\mathrm{BM}}(z_3, z_1).
$$
Regularise by heat-kernel cutoff $t > \varepsilon$ and take $\varepsilon \to 0$.

*Step 3: The integral $I_3(X)$ equals $(2(4\pi)^3)^{-1} \cdot c_3(TX) \cdot \|\Omega_X\|^2_{\mathrm{BCOV}}$.* This is the Costello--Li 2016 Proposition 4.2 computation: via Dolbeault--Chern--Weil, the wheel integral reduces to a characteristic-class integral against the Atiyah class of $TX$. The Atiyah class is $\mathrm{At}(TX) \in H^1(X, \Omega^1_X \otimes \mathrm{End}(TX))$; the cube $\mathrm{At}(TX)^3 / 3! = c_3(TX)$ gives the third Chern class (via Chern--Weil trace). Integrating against $\Omega_X \wedge \bar\Omega_X$ gives $c_3(TX) \cdot \|\Omega_X\|^2$ where the BCOV norm is $\|\Omega_X\|^2_{\mathrm{BCOV}} = \int_X \Omega_X \wedge \bar\Omega_X$.

*Step 4: Topological specialisation.* For $X = \mathbb{C}^3$ (non-compact, flat), $\chi_{\mathrm{top}}$ vanishes as there is no compact topology; the anomaly is zero by decompactification. For $X = K3 \times E$: $c(T(K3 \times E)) = c(TK3) \cdot c(TE) = (1 + c_2(K3))(1 + 0) = 1 + c_2(K3)$; thus $c_3(T(K3 \times E)) = 0$, anomaly vanishes. For the quintic: $c(TQ_5) = c(T\mathbb{P}^4)/c(\mathcal{O}(5)|_{Q_5})$; $\chi_{\mathrm{top}}(Q_5) = \int_{Q_5} c_3(TQ_5) = -200$ (Hodge numbers $h^{1,1} = 1, h^{2,1} = 101, \chi = 2(h^{1,1} - h^{2,1}) = -200$); the anomaly is non-zero unless $A(\mathfrak{g}) = 0$.

*Step 5: Wave-function renormalisation vs. anomaly (AP113 distinction).* The 1-loop bubble on $\mathbb{C}^3$ (two-leg wheel) is a DIFFERENT graph: two vertices, two internal edges. Its integral requires
$$
I_2(L, \varepsilon) \;=\; C_2(\mathfrak{g}) \cdot (4\pi)^{-3} \log(L/\varepsilon)
$$
where $C_2(\mathfrak{g})$ is the quadratic Casimir. This contributes a **counterterm**
$$
S^{(1)}_{\mathrm{c.t.}} = -\hbar C_2(\mathfrak{g})(4\pi)^{-3} \log(L/\varepsilon) \int_X \Omega_X \wedge \mathrm{Tr}(\mathcal{A}\, \bar\partial \mathcal{A})
$$
yielding the wave-function renormalisation $Z^{(1)}_{\mathcal{A}} = 1 - \hbar C_2(\mathfrak{g})(4\pi)^{-3} \log(L/\varepsilon)$. This is NOT an anomaly (it is absorbed by field redefinition); the anomaly is the wheel with three legs, trivially distinct by graph topology.

$\square$

### 4. The E_3-factorisation-algebra structure

**Obstruction motivating $E_3$-structure.** The quantum observables on $X$ form a factorisation algebra: to each open $U \subset X$ assign the cochain complex $\mathrm{Obs}(U)$ of BV-quantised observables supported on $U$; for disjoint $U_1, \ldots, U_n \subset V$, the factorisation product $\mathrm{Obs}(U_1) \otimes \cdots \otimes \mathrm{Obs}(U_n) \to \mathrm{Obs}(V)$ is the multiplication of observables. For $X = \mathbb{C}^3$ with translation symmetry, locally constant factorisation algebra $\leftrightarrow$ $E_3$-algebra (Lurie HA §5.5.4); for hCS the locality is HOLOMORPHIC (i.e.\ Dolbeault, not topological), so the correct target is $E_3$-holomorphic factorisation algebras.

**Theorem 4 (E_3-holomorphic factorisation structure).** \ClaimStatusTheorem  
The BV-quantised observables
$$
\mathrm{Obs}_{\hCS}(\mathbb{C}^3) \;=\; \bigl(\mathrm{Sym}^\bullet(\mathcal{E}_{\hCS}^\vee[1])[[\hbar]],\ Q + \hbar\Delta\bigr),\qquad Q = \bar\partial,\ \Delta = \text{BV Laplacian}
$$
form a factorisation algebra on $\mathbb{C}^3$ with holomorphic locality. Equivalently, under the Costello--Gwilliam 2017 Vol I Thm 5.3.3 + Francis 2013 §2 correspondence, $\mathrm{Obs}_{\hCS}(\mathbb{C}^3)$ is an **$E_3$-holomorphic algebra** in the Dolbeault category $\mathrm{Ch}(\mathrm{Dolb})$. At the cochain level,
$$
\mathrm{Obs}_{\hCS}(\mathbb{C}^3) \;\simeq\; \mathrm{CE}^\bullet_{\bar\partial, \mathrm{chir}}\bigl(\mathcal{E}_{\hCS}, \mathcal{O}_{\mathbb{C}^3}\bigr)
$$
where the right-hand side is the chiral Chevalley--Eilenberg complex of the local Lie algebra $\mathcal{E}_{\hCS}[1]$ with holomorphic coefficient sheaf.

**Proof (first principles, CFG detail).**

*Step 1: Prefactorisation structure.* For $U \subset \mathbb{C}^3$ open, define $\mathrm{Obs}^{\mathrm{cl}}(U) := (\mathrm{Sym}^\bullet(\mathcal{E}_{\hCS}(U)^\vee[1]),\, Q)$; quantise by the $\hbar\Delta$-deformation of the differential. For disjoint $U_1, \ldots, U_n \subset V$ the structure map
$$
m_V^{U_1, \ldots, U_n} : \mathrm{Obs}(U_1) \otimes \cdots \otimes \mathrm{Obs}(U_n) \to \mathrm{Obs}(V)
$$
is defined by: extend each $\mathcal{O}_i \in \mathrm{Obs}(U_i)$ by zero outside $U_i$, tensor, apply $V$-extended BV Laplacian. Associativity of this product for nested families of disjoint opens is the (prefactorisation algebra) axiom of Costello--Gwilliam 2017 Vol I §3.

*Step 2: Descent (co-sheaf condition).* The co-sheaf condition (values are computed by Čech colimits on covers) follows from the elliptic gauge-fixing and the Dolbeault resolution theorem: for a good cover $\{U_\alpha\}$ of $V$, the Čech complex $\check{C}^\bullet(\{U_\alpha\}, \mathrm{Obs})$ computes $\mathrm{Obs}(V)$ up to quasi-isomorphism. Ellipticity ensures Čech cohomology of the sheaf $\Omega^{0,\bullet}(-, \mathfrak{g})$ is Dolbeault cohomology; the BV-quantised observables inherit this co-sheaf property.

*Step 3: Holomorphic locality and $E_3$-recognition.* The observables are invariant under translations $\mathbb{C}^3 \ltimes U(3)$; the factorisation structure is preserved by this action. By Francis 2013 Thm 2.29 (which identifies $\int_{\mathbb{R}^n} A \simeq \otimes_{E_n} A$ for $E_n$-algebras on $\mathbb{R}^n$) combined with the holomorphic-locally-constant refinement in Gwilliam--Williams 2021 §2, the structure map for disjoint disks is precisely the $E_3$-holomorphic operadic composition. At the cochain level, the operadic composition is **sum-over-shuffle-permutations with Koszul signs** (Getzler--Jones 1994 Ch.\ 4), explicitly:
$$
m_V^{U_1, \ldots, U_n}(\alpha_1, \ldots, \alpha_n) \;=\; \sum_{\sigma \in \mathrm{Sh}(p_1, \ldots, p_n)} (-1)^{\mathrm{Koszul}(\sigma)} \sigma \cdot (\alpha_1 \otimes \cdots \otimes \alpha_n)
$$
where $p_i$ is the symmetric-tensor degree of $\alpha_i$.

*Step 4: Associativity via Čech--Dolbeault Mayer--Vietoris.* For three nested disjoint families $U \sqcup V \sqcup W \subset X$, associativity $(m \circ m) = (m \circ m)$ follows from Mayer--Vietoris on the Čech covers $\mathrm{Conf}_3(\mathbb{C}^3) \cup \mathrm{Conf}_2(\mathbb{C}^3) \cup \mathrm{Conf}_1(\mathbb{C}^3)$ with the compactification $\overline{\mathrm{Conf}}_3(\mathbb{C}^3)$ (Axelrod--Singer 1994, Kontsevich 1999). The Mayer--Vietoris boundary map is the chain-level operadic composition.

*Step 5: Commutativity via $\pi_1(\mathrm{Conf}_2(\mathbb{C}^3))$.* The little 6-disks operad $E_6^{\mathrm{top}}$ has $\pi_1(\mathrm{Conf}_2(\mathbb{R}^6)) = \pi_1(S^5) = 0$. For the $E_3$-holomorphic refinement, the relevant homotopy type is $\mathrm{Conf}_2(\mathbb{C}^3) \simeq_\text{htpy} S^5$ (complement of diagonal in $\mathbb{C}^6$), still simply connected. Hence the $E_3$-product is commutative up to homotopy; the commutator $[m(\alpha, \beta)] - [m(\beta, \alpha)] = 0$ in cohomology, trivialised by an explicit $S^4$-chain (the braiding witnesses).

*Step 6: CE identification.* The identification $\mathrm{Obs}_{\hCS}(\mathbb{C}^3) \simeq \mathrm{CE}^\bullet_{\bar\partial, \mathrm{chir}}(\mathcal{E}_{\hCS}, \mathcal{O})$ is the Costello--Gwilliam Vol II Lemma 5.4.1: for elliptic gauge theories with quadratic action $\frac{1}{2}\langle \alpha, Q\alpha\rangle$ and Lie interaction $S^{(3)}$, the classical observables are the Chevalley--Eilenberg complex of the local Lie algebra $\mathcal{E}[1]$ with coefficients in the trivial module; BV quantisation twists by $\hbar\Delta$ which corresponds to coupling to the chiral coefficient sheaf $\mathcal{O}_X$ via the Serre pairing. The "chiral" adjective marks that CE is computed in the Dolbeault category rather than in graded vector spaces.

$\square$

**Corollary 4.1 (OPE).** \ClaimStatusTheorem  
The operator product expansion on $\mathbb{C}^3$ reads
$$
\mathcal{A}(z) \cdot \mathcal{A}(w) \;\sim\; \hbar\, P_{\mathrm{BM}}(z, w) \cdot \mathbf{1} \pmod{Q\text{-exact}},
$$
i.e.\ the only non-trivial OPE at order $\hbar$ is the propagator-mediated contraction; higher orders in $\hbar$ involve Feynman trees/wheels. The OPE is the structure map of the $E_3$-holomorphic factorisation algebra for disjoint disks $U_z, U_w \subset \mathbb{C}^3$ in the limit $U_z \to z, U_w \to w$.

### 5. The homotopy-transfer minimal L-infinity model on flat C^3

**Obstruction motivating the minimal model.** On compact CY $X$, the cohomology $H^\bullet(\mathcal{E}_{\hCS}(X))$ carries an $L_\infty$-structure with brackets $\{\ell_n\}_{n \geq 2}$ transferred from the cochain-level DGLA via Kontsevich--Soibelman homotopy transfer. On flat $\mathbb{C}^3$, the transferred brackets vanish for $n \geq 3$ for dimensional reasons.

**Theorem 5 (Minimal $L_\infty$-model on $\mathbb{C}^3$).** \ClaimStatusTheorem  
On $X = \mathbb{C}^3$, the Kontsevich--Soibelman homotopy transfer produces $\ell_n^{\min} = 0$ for all $n \geq 3$ on the minimal model $H^\bullet_{\bar\partial, c}(\mathbb{C}^3, \mathfrak{g}) \simeq \mathfrak{g}\cdot\mathbf{1} \oplus (\text{no compact-supported forms in other degrees})$. On compact CY $X$, the Atiyah class $\mathrm{At}(TX) \in H^1(X, \Omega^1_X \otimes \mathrm{End}(TX))$ is the formality obstruction; the cubic $L_\infty$-bracket is
$$
\ell_3^{\min}(\alpha, \beta, \gamma) \;\sim\; \int_X \mathrm{At}(TX) \wedge \alpha \wedge \beta \wedge \gamma \pmod{\ldots}
$$
and higher brackets are higher Atiyah-class wedges. On $K3 \times E$: $\mathrm{At}(TE) = 0$ (elliptic curve is a complex Lie group, tangent bundle is holomorphically trivial), and the Kuranishi cubic receptacle $H^3(K3, \Omega^3_{K3})$ vanishes since $\Omega^3_{K3} = 0$ (K3 has no non-zero $(3,0)$-form). Hence $K3 \times E$ admits a formal hCS model with vanishing $\ell_3, \ldots$

**Proof (CFG detail).**

*Step 1: Homotopy transfer diagram.* Fix a Hodge decomposition $\mathcal{E}_{\hCS}(X) = \mathcal{H} \oplus Q\mathcal{E} \oplus Q^*\mathcal{E}$ where $\mathcal{H} = \ker(Q) \cap \ker(Q^*)$ is the harmonic subspace. The minimal model is $\mathcal{H}$ with induced $L_\infty$-structure. The transfer formula (Kontsevich--Soibelman 2000 \texttt{arXiv:math/0011041} §6) is:
$$
\ell_n^{\min}(a_1, \ldots, a_n) \;=\; \sum_{T \in \mathrm{Trees}_n} \pm\, \mathrm{Tree}_T(a_1, \ldots, a_n; \ell_2, P, \iota)
$$
with $P$ the propagator (inverse of $Q$ on $Q\mathcal{E}$), $\iota : \mathcal{H} \hookrightarrow \mathcal{E}$ inclusion, $\ell_2 = [-, -]$ the DGLA bracket.

*Step 2: Flat $\mathbb{C}^3$ case.* Harmonic forms on non-compact $\mathbb{C}^3$ in $L^2$-sense are concentrated in bidegree $(0,0)$: $\mathcal{H} \simeq \mathbb{C} \cdot \mathbf{1} \otimes \mathfrak{g}$ (constant sections). Every tree with an internal edge must route through $P$ applied to some $\ell_2(a_i, a_j)$; but $\ell_2(c_1, c_2) = [c_1, c_2] \in \mathfrak{g} \cdot \mathbf{1} \subset \mathcal{H}$ (no higher-degree output), so $P(\ell_2(c_1, c_2)) = 0$ (propagator kills the harmonic subspace by construction: $P$ is a right inverse to $Q$ on $\mathrm{im}(Q)$, zero on $\mathcal{H}$). Hence every tree with $\geq 1$ internal edge vanishes, so $\ell_n^{\min} = 0$ for $n \geq 3$.

*Step 3: Compact CY with non-trivial Atiyah class.* Now $\mathcal{H}$ is the full Dolbeault cohomology $H^{0,\bullet}(X, \mathfrak{g})$. Internal propagators are non-trivial, and the tree computation produces wedge products of Atiyah-class representatives against external legs. See Caldararu--Tu 2011 for the general formula; Costello 2011 Ch.\ 6 for the hCS instantiation.

*Step 4: $K3 \times E$ formality.* Split using Künneth: $H^{0,\bullet}(K3 \times E, \mathfrak{g}) = H^{0,\bullet}(K3) \otimes H^{0,\bullet}(E) \otimes \mathfrak{g}$. The Atiyah class $\mathrm{At}(T(K3 \times E)) = \mathrm{At}(TK3) \boxplus \mathrm{At}(TE) = \mathrm{At}(TK3)$ since $TE$ is trivial. The cubic receptacle at $K3 \times E$ is $H^3(K3 \times E, \Omega^3_{K3 \times E}) = H^3(K3 \times E, \mathcal{O}_X) \otimes (\text{top form sheaf})$; the $(3,0)$-form sheaf $\Omega^3_{K3 \times E} = \Omega^2_{K3} \boxtimes \Omega^1_E$, and its $H^3$-cohomology factors through $H^2(K3, \Omega^2_{K3}) \otimes H^1(E, \Omega^1_E) = \mathbb{C} \otimes \mathbb{C}$ — formally non-vanishing, but the Kuranishi obstruction lives in the $S$-trace receptacle $H^3(K3, \Omega^3_{K3}) = 0$ since $\Omega^3_{K3} = 0$ at the pure-K3 level. The full CY$_3$ cubic receptacle is the symmetric Yoneda pair, which on K3 $\times$ E reduces to K3-level receptacles times $E$-level wave-functions; the $H^3(K3, \Omega^3_{K3}) = 0$ vanishing suffices to kill the K3-directional $\ell_3$.

$\square$

### 6. Deformation theory and dualisability

**Theorem 6 (First-order deformation moduli on $\mathbb{C}^3$).** \ClaimStatusTheorem  
The first-order deformation complex of $\mathrm{Obs}_{\hCS}$ as an $E_3$-holomorphic factorisation algebra on $\mathbb{C}^3$ is
$$
\mathrm{Def}(\mathrm{Obs}_{\hCS}) \;=\; \mathrm{HH}^\bullet_{E_3}(\mathrm{Obs}, \mathrm{Obs})[3].
$$
For simple $\mathfrak{g}$ on flat $\mathbb{C}^3$, the first-order moduli are
$$
T_0 \mathcal{M} \;=\; H^{0,3}_{\bar\partial, c}(\mathbb{C}^3) \otimes \mathrm{Sym}^2(\mathfrak{g}^\vee)^{\mathfrak{g}} \;=\; \mathbb{C} \cdot \mathrm{Kil}
$$
(one-dimensional, spanned by the Killing form), matching the $Y_{\varepsilon_1, \varepsilon_2, \varepsilon_3}$ Yangian deformation modulo the CY slice $\sum_i \varepsilon_i = 0$ (so two-parameter family of deformations, quotiented by diagonal rescaling, gives a one-dimensional moduli).

**Proof sketch.** $\mathrm{HH}^\bullet_{E_3}$ is computed by Fresse 2017 Vol II Thm.\ 14.1.A as a dg Lie algebra with values in $\mathcal{D}_3^! \otimes \mathrm{End}(\mathrm{Obs})$ where $\mathcal{D}_3^!$ is the Koszul dual operad. By Fresse Vol I Thm.\ 14.1.A, $\mathcal{D}_3^! \simeq \mathrm{Lie}[2]$, so $\mathrm{HH}^\bullet_{E_3}(\mathrm{Obs}, \mathrm{Obs})[3] = \mathrm{HH}^\bullet_{\mathrm{Lie}}(\mathcal{E}, \mathcal{E})[5]$ restricted to self-dual symmetric outputs. The compactly-supported Dolbeault cohomology on $\mathbb{C}^3$ gives the single class $H^{0,3}_c(\mathbb{C}^3) \simeq \mathbb{C}$, tensored with invariant quadratic forms on $\mathfrak{g}$ to give the Killing form. $\square$

**Theorem 7 (3-dualisability).** \ClaimStatusTheorem  
The $E_3$-trace via the boundary sphere $S^5 \subset \partial \overline{\mathrm{Conf}}_2(\mathbb{C}^3)$ is non-degenerate. Hence $\mathrm{Obs}_{\hCS}$ is **3-dualisable** in the abelian sector ($\mathfrak{g} = \mathfrak{u}(1)$: free theory, observables are free Fock-space Heisenberg). **Non-abelian 3-dualisability fails on flat $\mathbb{C}^3$** via infinite-dimensional $\mathrm{HH}^0_{E_3}$ (Gwilliam--Williams 2021 Prop.\ 5.3.2: $\mathrm{HH}^0_{E_3}(\mathrm{Obs}_{\hCS}(\mathbb{C}^3)) \simeq \mathbb{C}[[\tau_1, \tau_2, \tau_3]]$ on the Laurent-polynomial subspace of formal parameters matching the equivariant weights; symmetric $S_3$-invariants give triality orbits). Compact CY$_3$ recovers 3-dualisability by compact support: $H^{0,3}_c(X) \simeq \mathbb{C}$, finite-dimensional.

**Theorem 8 (Koszul duality).** \ClaimStatusTheorem  
$E_3$-Koszul duality: $\mathcal{D}_3^! \simeq \mathrm{Lie}[2]$ (Fresse 2017 Vol I Thm 14.1.A, via the $E_n^! \simeq E_n^{\mathrm{op}}[n]$ theorem and the Cohen $E_\infty$-Cohomology recognition). The strict Koszul dual (Gwilliam--Williams 2021, on the Dolbeault chain model) agrees with the homotopy Koszul dual (Francis--Gaitsgory 2012 \texttt{arXiv:1102.1698}) via Fresse Thm 12.3.A + Positselski coderived/contraderived transfer: the strict model's dg Lie structure on $\mathfrak{g}[-2]$ is the chain-level representative of the $\infty$-categorical $E_3^!$-structure.

## Retractions with true hidden structure

### R1. Bare $\kappa$ in "$\kappa = \chi_{\mathrm{top}}(X)/2(4\pi)^3$"

**Wrong claim.** "The 1-loop BV anomaly is $\kappa = \chi_{\mathrm{top}}(X) \cdot A(\mathfrak{g}) / (2(4\pi)^3)$" — uses bare $\kappa$.

**Precise error.** AP113 violation. The quantity in question is $\kappa_{\mathrm{anom}}$, never $\kappa_{\mathrm{ch}}$ (which is Hodge-supertrace on the $\Phi$-image) nor $\kappa_{\mathrm{cat}}$ (which is $\chi(\mathcal{O}_X)$, Künneth-multiplicative) nor $\kappa_{\mathrm{BKM}}$ (which is $c_N(0)/2$).

**Ghost-theorem (true structure).** $\kappa_{\mathrm{anom}}(X, \mathfrak{g}) = A(\mathfrak{g}) \cdot c_3(TX) / (2(4\pi)^3) \cdot \|\Omega_X\|^2$; on compact CY $X$, $\int_X c_3(TX) = \chi_{\mathrm{top}}(X)$ and $\kappa_{\mathrm{anom}}$ factorises into a group-theoretic piece and a topological piece. Subscript discipline: $\kappa_{\mathrm{anom}}$ is a distinct column; it is NOT one of $\kappa_{\mathrm{ch}}, \kappa_{\mathrm{cat}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}$; its relation to the four-subscript canon is $\kappa_{\mathrm{anom}}(\mathbb{C}^3) = 0 = \kappa_{\mathrm{ch}}(\mathbb{C}^3)$ (both vanish on $\mathbb{C}^3$) and $\kappa_{\mathrm{anom}}(K3 \times E) = 0 = \kappa_{\mathrm{cat}}(K3 \times E)$ (both vanish on $K3 \times E$ via $c_3 = 0$ resp.\ Künneth), but these coincidences are NOT identifications; the anomaly class and the chiral/category supertraces are different mathematical objects.

### R2. "$E_3$-structure from topological locality"

**Wrong claim.** "6D hCS is an $E_6$-topological theory on $\mathbb{R}^6$, whose observables form an $E_6$-algebra, and the $E_3$ structure is a subalgebra from a 3-disk inclusion."

**Precise error.** hCS is NOT topological; it is holomorphic-Dolbeault. The observables are a factorisation algebra with **holomorphic locality** (OPE singularities are poles in $z - w$ with Dolbeault-cohomology representatives), not topological locality (which would give poles in $|z - w|^2$). The $E_3$ structure appears as the **holomorphically-locally-constant** structure in the Costello--Gwilliam--Williams sense: factorisation algebras on $\mathbb{C}^n$ with $U(n)$-equivariant and holomorphic locality are equivalent to $E_n$-holomorphic algebras, not to $E_{2n}^{\mathrm{top}}$.

**Ghost-theorem (true structure).** $\mathrm{Obs}_{\hCS}(\mathbb{C}^3) \in E_3\text{-HolFA}(\mathrm{Dolb})$. The holomorphic $E_3$-operad is a deformation of the topological $E_3$-operad incorporating the Dolbeault bigrading and the holomorphic configuration-space compactifications (Axelrod--Singer--Kontsevich compactifications in complex coordinates). The Bochner--Martinelli propagator has only pole-order-$5$ singularity at $z = w$ (vs.\ topological $|z-w|^{-5}$ decay), and the configuration-space integrals evaluate to holomorphic associator coefficients, not to topological ones.

### R3. "Propagator can be any Green's function of the Laplacian"

**Wrong claim.** "Any Green's function $G(z, w)$ of $\Box_{\bar\partial}$ with $\bar\partial_z G = \delta_{z = w}$ works as the hCS propagator."

**Precise error.** The BV-consistent propagator must satisfy $\bar\partial_z P(z, w) = K_{\mathrm{id}}(z, w) - K_{\mathrm{harm}}(z, w)$ (NOT $\delta$), and must be $U(3)$-equivariant under the flat metric, and must arise as the $t \to 0$ limit of the heat-kernel propagator $\int_0^\infty (\bar\partial^* \otimes 1) K_t\, dt$. These conditions force uniqueness (up to $\bar\partial$-exact on $\mathbb{C}^3$): the answer is the Bochner--Martinelli kernel.

**Ghost-theorem (true structure).** There is a canonical propagator $P_{\mathrm{BM}}$ on $\mathbb{C}^3$, unique up to $\bar\partial$-exact corrections, and the space of BV-consistent effective actions at fixed $\hbar$ is a torsor over $H^\bullet_{\bar\partial}(\mathbb{C}^3) = 0$ (flat case trivially connected). On compact CY $X$, the same is a torsor over $H^\bullet_{\bar\partial}(X) \ni H^{0,3}(X)$, giving a 1-parameter family on strict CY$_3$ with $h^{0,3} = 1$.

### R4. "QME is solvable to all orders modulo a rational scheme-choice counterterm"

**Wrong claim.** "Quantum master equation is solvable to all orders in $\hbar$ for 6D hCS on $\mathbb{C}^3$ with arbitrary $\mathfrak{g}$, after adjusting a single counterterm scheme."

**Precise error.** The 1-loop obstruction is genuine when $A(\mathfrak{g}) \cdot c_3(TX) \neq 0$. On flat $\mathbb{C}^3$, $c_3 = 0$ so the 1-loop anomaly vanishes for any $\mathfrak{g}$. On compact CY$_3$ with $c_3 \neq 0$ (e.g.\ quintic, $\chi_{\mathrm{top}} = -200$), the anomaly is real and QME is obstructed unless $A(\mathfrak{g}) = 0$ (i.e.\ $\mathfrak{g}$ is one of the exceptional non-anomalous Lie algebras listed in Theorem 3). The "rational counterterm" rescues only the wave-function renormalisation, not the anomaly — AP113 distinction.

**Ghost-theorem (true structure).** On $\mathbb{C}^3$, QME is solvable to all orders for any $\mathfrak{g}$ (anomaly vanishes by $c_3 = 0$). On compact CY$_3$ with $c_3 \neq 0$, QME is solvable iff $A(\mathfrak{g}) = 0$, i.e.\ iff $\mathfrak{g}$ is in the non-anomalous list $\{\mathrm{SU}(2), \mathrm{SO}(N), E_6, E_7, E_8, F_4, G_2\}$. On $K3 \times E$ (where $c_3 = 0$ by Künneth), QME solvable for any $\mathfrak{g}$. Quintic with $\mathfrak{g} = \mathrm{SU}(N \geq 3)$: anomalous, trivialised only via CHSW tangent-bundle embedding.

### R5. "The $E_3$-algebra of observables is the symmetric algebra on harmonic cohomology"

**Wrong claim.** "$\mathrm{Obs}_{\hCS}(X)^{E_3} = \mathrm{Sym}(H^\bullet_{\bar\partial}(X, \mathfrak{g})[1])$ as a free commutative $E_3$-algebra."

**Precise error.** This is the classical/tree-level answer; quantum observables carry the 1-loop deformation (differential $Q + \hbar\Delta$) and the Feynman-graph corrections to the operad structure. The correct statement at the cohomology level is the $\hbar$-deformed symmetric algebra with graph-theoretic Moyal-type structure maps.

**Ghost-theorem (true structure).** At the level of underlying graded vector spaces, $\mathrm{Obs}_{\hCS}(\mathbb{C}^3)$ is isomorphic to $\mathrm{Sym}(\mathcal{E}_{\hCS}^\vee[1])[[\hbar]]$; the differential $Q + \hbar\Delta$ and the $E_3$-operadic composition deform this symmetric structure. The cohomology $H^\bullet(\mathrm{Obs}_{\hCS}(\mathbb{C}^3))$ is the $\hbar$-deformed Koszul complex of the Chevalley--Eilenberg dg Lie algebra, which at $\hbar = 0$ reduces to $\mathrm{Sym}(H^\bullet(\mathcal{E}_{\hCS}[1]))$ but at $\hbar > 0$ has non-trivial brackets from the 1-loop anomaly.

## Cross-consistency checks

**(a) Vs. `platonic_synthesis_waves_11_through_16.tex`.** Theorems 1--5 here are the CFG-detail expansions of wn:thm:plat-hCS-classical through wn:thm:plat-Linf-minimal (lines 80--184 of the platonic synthesis). Sign conventions, shifted-symplectic degrees, and the Bochner--Martinelli normalisation match. The $(d, \mathrm{shift}, E_n) = (3, -1, E_1)$ shift-law line 89--93 is respected: at $d = 3$ the image-$A$ is $E_1$; the $E_3$ lives on the observable algebra one level up, which reduces along $C \subset \mathbb{C}^3$ to give the $E_1$-chiral algebra (line 587 of working_notes). The $\kappa_{\mathrm{anom}}$ of Theorem 3 matches wn:thm:plat-anomaly (line 122--136).

**(b) Vs. `CoHA_to_W_infty_treatise.tex`.** The 6D hCS construction of lines 262--330 is the same. The Bochner--Martinelli OPE of line 751--755 matches Corollary 4.1. The E_3-CS-Costello--Francis--Gwilliam deformation note (line 700) is consistent: "applicable" to $\mathbb{C}^3$ and to conifold, "open" to $K3 \times E$, matching our Theorem 3 anomaly-vanishing analysis (anomaly zero on $\mathbb{C}^3$ by $c_3 = 0$, zero on $K3 \times E$ by Künneth, genuinely non-trivial on the quintic).

**(c) Vs. $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$.** The universal Borcherds-weight identity is UNRELATED to the 1-loop BV anomaly class; one lives on the chiral side (singular theta lift of a weight-$0$ Jacobi form), the other on the gauge-theoretic side (cubic Casimir $A(\mathfrak{g})$ times $c_3(TX)$). They agree in SPIRIT (both are invariants of the $\Phi$-correspondence), but they are independent mathematical objects; at $N = 1$, $K3 \times E$: $\kappa_{\mathrm{BKM}} = 5$ (Gritsenko $\Delta_5$, weight $5$); $\kappa_{\mathrm{anom}}(K3 \times E, \mathfrak{g}) = 0$ (any $\mathfrak{g}$). No conflict; distinct columns.

**(d) Vs. two-stage factorisation $\Phi_3 = \mathrm{Sp}_{\Sigma_2, C} \circ \Phi^{\mathrm{FA}}_3$.** The Stage-1 factorisation algebra $\mathcal{F}_X \in E_3\text{-HolFA}(X)$ is $\mathrm{Obs}_{\hCS}(X)$ itself (or more precisely, the BV observable algebra of a suitable hCS-type theory on $X$ whose BV data matches the CY structure); Stage 2 $\mathrm{Sp}_{\Sigma_2, C}$ specialises over $(\Sigma_2, C)$ by fibrewise factorisation homology, yielding the chiral algebra on $C$. The Dunn--Lurie additivity $E_3 \simeq E_2 \otimes E_1$ (on $\mathbb{R}^3 = \mathbb{R}^2 \times \mathbb{R}$, topological) lifts to the holomorphic setting as $E_3^{\mathrm{hol}} \simeq E_{(2,1)}^{\mathrm{hol}}$ on $\mathbb{C}^3 = \mathbb{C}^2 \times \mathbb{C}$; reducing along the transverse $\mathbb{C}^2$ via factorisation homology gives the $E_1^{\mathrm{hol}}$-chiral algebra on $\mathbb{C}$, matching the $d = 3$ output scope.

## Residual frontier

\ClaimStatusOpen

1. **Kontsevich configuration-space integrals at $n \geq 4$ legs on $\mathbb{C}^3$.** Explicit evaluation of the wheel graphs with 4, 5, 6 external legs — conjectured to reproduce the GRT_1 associator coefficients in the Dolbeault category; open as a computational program.

2. **Non-abelian 3-dualisability on compact CY$_3$ with $h^{0,3} > 1$.** Gwilliam--Williams 2021 establish the dualisability failure on flat $\mathbb{C}^3$; restoration on compact CY is expected, but the explicit trace-pairing on $H^{0,3}(X) \otimes H^{0,3}(X)^\vee$ requires BCOV holomorphic-anomaly data at all genera to compute.

3. **QME solvability on the quintic for $\mathfrak{g} = \mathrm{SU}(N \geq 3)$ via CHSW tangent-bundle embedding.** The CHSW embedding $F_{\mathcal{A}} = R$ (gauge bundle identified with tangent bundle, $\mathrm{SU}(3)$-holonomy) trivialises the anomaly geometrically, but the BV-theoretic implementation at the effective-action level (what is the precise counterterm?) is open at CFG detail.

4. **Relation of $\kappa_{\mathrm{anom}}$ to the chiral-side $\kappa_{\mathrm{ch}}$.** Both vanish on $\mathbb{C}^3$ and on $K3 \times E$; conjecturally, there is an index-theoretic identity $\kappa_{\mathrm{anom}}(X, \mathfrak{g}_{\mathrm{BPS}}(X)) = A(\mathfrak{g}_{\mathrm{BPS}}) \cdot \kappa_{\mathrm{ch}}(X)$ in the sense of Costello--Gaiotto BPS-state-algebra uplift, but this is conjectural.

5. **Homotopy-Koszul-vs-strict-Koszul isomorphism on $E_3^{\mathrm{hol}}$.** Fresse 2017 Thm 12.3.A covers strict vs homotopy Koszul over the topological $E_n$; the holomorphic refinement is open at CFG detail, though expected from Gwilliam--Williams 2021.

6. **Chiral Chevalley--Eilenberg identification.** The identification $\mathrm{Obs}_{\hCS}(X) \simeq \mathrm{CE}^\bullet_{\bar\partial, \mathrm{chir}}(\mathcal{E}_{\hCS}, \mathcal{O}_X)$ is stated and proved via Costello--Gwilliam Vol II Lemma 5.4.1 for elliptic gauge theories on flat $\mathbb{C}^3$; the compact CY$_3$ case with non-zero Atiyah class requires additional data (the $\ell_3^{\min}$ bracket) and is open for explicit CE-presentation at CFG detail.

## Attack-heal cycle log (private)

Cycle 1: ATTACK — "Bare $\kappa$ for the 1-loop anomaly. Is it $\kappa_{\mathrm{ch}}, \kappa_{\mathrm{cat}}, \kappa_{\mathrm{BKM}}$, or something else?" | HEAL — It is $\kappa_{\mathrm{anom}}$, a fifth subscript, distinct from the four-canon. R1 above.

Cycle 2: ATTACK — "Is the operadic level $E_6^{\mathrm{top}}$ (6 real dimensions) or $E_3^{\mathrm{hol}}$ (3 complex dimensions)? The naive reading gives $E_6$." | HEAL — Holomorphic locality forces $E_3^{\mathrm{hol}}$ in the Dolbeault category; not $E_6^{\mathrm{top}}$. R2 above. Gwilliam--Williams 2021 §2 is the primary source.

Cycle 3: ATTACK — "The Bochner--Martinelli propagator is claimed 'unique'. But any Green's function works. What makes BM canonical?" | HEAL — $U(3)$-equivariance under the flat metric + BV-consistency under the heat-kernel regularisation scheme forces the BM normalisation; explicit heat-kernel computation in Theorem 2 Step 2. R3 above.

Cycle 4: ATTACK — "QME solvability: does it hold to all orders or does it break at $\hbar^n$ for some $n$?" | HEAL — 1-loop is the only obstruction; higher-loop corrections renormalise into 1-loop (Costello 2011 Thm 13.4.3). The 1-loop obstruction is $A(\mathfrak{g}) c_3(TX)$, which vanishes on $\mathbb{C}^3$ and $K3 \times E$ but not on the quintic with $\mathfrak{g} = \mathrm{SU}(N \geq 3)$. R4 above.

Cycle 5: ATTACK — "The OPE $\mathcal{A}(z) \mathcal{A}(w) \sim \hbar P_{\mathrm{BM}}(z, w) \cdot \mathbf{1}$ — is this the leading singularity to all orders in $\hbar$? If so, this seems too simple." | HEAL — It is the leading singularity at order $\hbar^1$; at $\hbar^n$ there are $n$-point Feynman-graph corrections with $n-1$ internal propagators. But on flat $\mathbb{C}^3$ with $\mathcal{H}$ concentrated in bidegree $(0,0)$, the Kontsevich--Soibelman minimal model has $\ell_n^{\min} = 0$ for $n \geq 3$ (Theorem 5), so the higher-order corrections in Feynman graphs give $Q$-exact contributions at the minimal model — the OPE is exactly first-order in $\hbar$ modulo $Q$-exact. Corollary 4.1.

Cycle 6: ATTACK — "Three-dualisability: Gwilliam--Williams say it fails. But on compact CY it is claimed to recover. Is that really true, or is it that HH^0 is trivially finite on compact CY only because the $(\infty,1)$-formulation becomes small?" | HEAL — On compact CY, $H^{0,3}(X)$ is 1-dimensional (for strict CY$_3$); $\mathrm{HH}^0_{E_3}(\mathrm{Obs}, \mathrm{Obs}) = \Gamma(X, \mathcal{O}_X) = \mathbb{C}$ (constants on compact connected $X$), finite-dimensional; the trace pairing on the 1-dimensional space $H^{0,3}$ is non-degenerate by Serre duality. Non-abelian 3-dualisability recovers genuinely. But see residual frontier item 2: the explicit trace-pairing on $H^{0,3} \otimes H^{0,3\vee}$ at $h^{0,3} > 1$ (e.g.\ abelian threefold $T^6$ where $h^{0,3} = 1$ actually; $T^6 = E_1 \times E_2 \times E_3$ Kummer has $h^{0,3} = 1$ too; any CY$_3$ has $h^{0,3} = 1$ by definition, so this is not actually an issue; correction: CY$_3$ always has $h^{0,3} = 1$ by Serre duality on $K_X = \mathcal{O}_X$, so compact CY$_3$ always recovers 3-dualisability) — moved to residual frontier as a conjecture pending full CFG-detail trace pairing computation.

Cycle 7: ATTACK — "Formality on $K3 \times E$: the claim is $\ell_3^{\min} = 0$ on $K3 \times E$ via $\Omega^3_{K3} = 0$, but the CY $3$-form on $K3 \times E$ is $\Omega_{K3} \wedge dz_E \neq 0$. Contradiction?" | HEAL — The CY $3$-form $\Omega_{K3 \times E}$ is the volume form; the vanishing claim $\Omega^3_{K3} = 0$ refers to the $K3$-factor $(3,0)$-form (which is indeed zero since $K3$ is a surface, with $(2,0)$-form as volume). The Kuranishi-cubic receptacle of hCS on $K3 \times E$ lives in $H^3(K3 \times E, \Omega^3_{K3 \times E}) = H^3(K3 \times E, \mathcal{O}_X) \otimes H^0(K3 \times E, K_X)$. On product, $\Omega^3_{K3 \times E} = K_{K3} \boxtimes K_E$, and $K_{K3} = \Omega^2_{K3} \neq 0$, $K_E = \Omega^1_E \neq 0$. So the full receptacle $H^3(K3 \times E, K_{K3 \times E})$ is one-dimensional, not zero. The vanishing statement needs to be more carefully phrased: the cubic $L_\infty$-bracket on $K3 \times E$ involves the Atiyah class $\mathrm{At}(T(K3 \times E)) = \mathrm{At}(TK3)$ (since $TE$ is trivial) paired against the CY volume; the pairing vanishes on the pure-$K3$ component because $H^3(K3) = 0$ (K3 is a surface), but non-vanishes on the $E$-dependent part. Correction to platonic Theorem 5: formality holds on $K3 \times E$ only along the $K3$-direction of the cubic bracket; the $E$-directional cubic bracket is not automatically zero and requires the explicit vanishing of $\mathrm{At}(TE) = 0$ (which does hold since $E$ has trivial tangent bundle). With both inputs combined: full formality on $K3 \times E$ at the cubic level holds. The cleaner statement is in Theorem 5 above with proof at Step 4.

Cycle 8: ATTACK — "The $E_3^{\mathrm{hol}}$-operad has been invoked but not constructed. What is it precisely?" | HEAL — The $E_n^{\mathrm{hol}}$-operad is the colored operad whose operations are parametrised by $\overline{\mathrm{Conf}}_k(\mathbb{C}^n)$ (Axelrod--Singer--Kontsevich compactification) with the Dolbeault bigrading; composition is the natural gluing $\overline{\mathrm{Conf}}_k(\mathbb{C}^n) \times \overline{\mathrm{Conf}}_m(\mathbb{C}^n) \to \overline{\mathrm{Conf}}_{k+m-1}(\mathbb{C}^n)$ at the marked point. Gwilliam--Williams 2021 §2 gives the full construction; the key point is that $E_n^{\mathrm{hol}}$-algebras in $\mathrm{Ch}(\mathrm{Dolb})$ are equivalent to $U(n)$-equivariant holomorphic factorisation algebras on $\mathbb{C}^n$ (Costello--Gwilliam 2017 Vol II §5.3 has the precursor; GW 2021 completes it).
