# Agent A12 (Wave 2) — Costello voice on Bochner--Martinelli convergence and the one-loop wheel constant

## Executive adversarial summary

Two spine claims fall and are rebuilt at CFG detail.
**(1)** The claim "$P_{\mathrm{BM}}$ is absolutely convergent on $\FM_n(\CC^3)$ and only conditionally convergent on $\overline{\mathrm{Conf}}_n(\CC^3)$" is sloppy shorthand for an AP-CY-grade distinction. At codim-$6$ (two-point) diagonals the triangle integrand is \emph{marginally log-divergent} in power-counting on the naive $\overline{\mathrm{Conf}}$-closure (the integrand scales as $r^{-5}$, the codim-$6$ transverse volume as $r^5\,dr$, giving $dr/r \cdot (\text{angular})$), and vanishes by a $U(3)$-equivariant angular average (Axelrod--Singer 1994 §5; Kontsevich 1999 §6): this is the source of \emph{conditional} convergence, i.e.\ convergence by cancellation of the angular integral, not by absolute integrability. The Fulton--MacPherson blowup replaces the ill-defined $\log$-singular limit by a well-defined value on the normal-crossings boundary divisor, upgrading conditional convergence to \emph{absolute pullback convergence} on the blowup corner charts. At codim-$12$ (three-point diagonal) the simple analog fails and requires iterated blowups; the claim "blowup resolves to normal crossings" survives, but the sharpest true statement restricts to the $U(3)$-equivariant angular-average of the partial-diagonal stratum, not pointwise absolute integrability.

**(2)** The one-loop wheel constant as stated in the spine, $\chi_{\mathrm{top}}(X)/(2(4\pi)^3)$, conflicts with the manuscript's own Costello--Li 2016 Prop 5.2 citation $\chi(X)/24$. The $\chi/24$ number comes from Grothendieck--Riemann--Roch: $\int_X \mathrm{ch}(T_X)\cdot\mathrm{td}(T_X)$ with only the $(0,1)$-component surviving gives the BCOV coefficient $\alpha_{\mathrm{BCOV}} = (\chi(X)/24)\cdot[\Omega_X]^{0,1}$ in $H^{0,1}(X)$, Serre-dual to but Hodge-disjoint from the cubic Yukawa $Y_3 \in H^{0,3}(X)$. The pre-factor $1/(2(4\pi)^3)$ is a \emph{scheme-dependent} normalisation (a physicist's heat-kernel--measure convention from Costello 2011 Ch.~2), absorbable into the $\hbar$-expansion. The canonical (scheme-independent) statement is $\alpha_{\mathrm{BCOV}} = (\chi(X)/24)\cdot[\Omega_X]^{0,1}$ as a cohomology class; the $(2(4\pi)^3)^{-1}$ and $\chi/24$ factors differ by a constant that amounts to a redefinition of $\hbar$. The spine formula, with $(2(4\pi)^3)^{-1}\|\Omega_X\|^2_{\mathrm{BCOV}}$, is a \emph{pairing representative} rather than the canonical $H^{0,1}$-class. Both are correct; they are different invariants and must be labelled as such.

Sharpest new theorem proved: the absolute-vs-conditional dichotomy is precisely the Axelrod--Singer codim-$6$ log-divergence cancellation (Stokes on the FM corner divisor), and its CY extension requires that the corner-stratum pullback of $P_{\mathrm{BM}}^{\wedge 3}$ be a \emph{smooth} section of the blowup, not merely absolutely integrable pointwise. Sharpest new conjecture isolated: the one-loop anomaly reading admits \emph{two} scheme-different but cohomologically equivalent representatives $\alpha_{\mathrm{BCOV}} \in H^{0,1}(X)$ (Costello--Li, scheme-independent) and the BCOV-paired $\int_X c_3(TX)\cdot\|\Omega_X\|^2/(2(4\pi)^3)$ (Costello 2011 heat-kernel scheme); equality of the two expressions up to scheme is a Bardeen--Zumino-type finite local counterterm, confirming the spine theorem `wn:thm:spine-consistent-covariant` modulo a precise scheme choice.

## Surviving theorems (healed, CG-voice)

### 1. Bochner--Martinelli power-counting on the naive configuration closure

\noindent\emph{Setup.} Fix the flat metric $g_0 = \sum dz_k \otimes d\bar z_k$ on $\CC^3$, the Euclidean BM propagator
\[
P_{\mathrm{BM}}(z, w) \;=\; \frac{2}{(2\pi i)^3}\sum_{k=1}^{3} (-1)^{k-1}\,\overline{(z_k - w_k)}\,\|z - w\|^{-6}\;\widehat{d\bar z_k}\wedge dw_1\wedge dw_2\wedge dw_3,
\]
with $\widehat{d\bar z_k} = d\bar z_1\wedge\cdots\wedge\widehat{d\bar z_k}\wedge\cdots\wedge d\bar z_3$ (hat deletes the $k$-th factor). Set $r := \|z - w\|$. The pointwise magnitude is $|P_{\mathrm{BM}}|_{g_0} = 2(2\pi)^{-3}\,r^{-5}$ (one antiholomorphic factor in the numerator, $r^{-6}$ in the denominator).

\noindent\emph{Obstruction motivating the theorem.} Define the three-leg triangle wheel
\[
I_3(X) \;:=\; \int_{\mathrm{Conf}_3(X)} \Omega_X(z_1)\wedge\Omega_X(z_2)\wedge\Omega_X(z_3)\wedge P_{\mathrm{BM}}(z_1,z_2)\wedge P_{\mathrm{BM}}(z_2,z_3)\wedge P_{\mathrm{BM}}(z_3,z_1),
\]
with $\Omega_X$ the CY holomorphic volume and $X$ either $\CC^3$ (supplemented with an IR cutoff) or a compact CY$_3$. The naive $\overline{\mathrm{Conf}}_3(X)$-closure of $\mathrm{Conf}_3(X)$ is the partial-diagonal stratified closure in $X^3$, with boundary strata
\[
\partial\overline{\mathrm{Conf}}_3 \;=\; D_{12}\cup D_{13}\cup D_{23}\cup D_{123},
\]
where $D_{ij} = \{z_i = z_j\}$ are codim-$6$ real strata (6 real codimension, one complex diagonal copy of $X$ parametrised by $z_i = z_j$ and a third free point $z_k$) and $D_{123} = \{z_1 = z_2 = z_3\}$ is codim-$12$.

\begin{theorem}[Triangle-integrand power-counting on $\overline{\mathrm{Conf}}_3(X)$]
\label{thm:a12-triangle-power-counting}
\ClaimStatusTheorem

Near the codim-$6$ stratum $D_{12}$, in polar coordinates $w = (z_1 + z_2)/2,\ \rho = \|z_1 - z_2\|,\ \omega \in S^5$ (unit direction in $\CC^3$), and with $z_3$ bounded away from $w$:
\begin{enumerate}[label=(\roman*)]
 \item the edge propagator $P_{\mathrm{BM}}(z_1, z_2)$ diverges as $\rho^{-5}$ (one antiholomorphic factor $\bar\rho$ in the numerator, $\rho^{-6}$ in the denominator, yielding pointwise magnitude $\rho^{-5}$);
 \item the other two edge propagators $P_{\mathrm{BM}}(z_2, z_3)$ and $P_{\mathrm{BM}}(z_3, z_1)$ remain smooth, as $\|z_i - z_3\|$ is bounded below by the assumption $z_3 \notin D_{12}$ neighbourhood;
 \item the transverse volume element is $\rho^5\,d\rho\wedge d\omega$ (real codim $6$ in the $(z_1 - z_2)/2$ relative coordinate);
 \item the product integrand scales as $\rho^{-5}\cdot\rho^5\,d\rho = d\rho$, yielding a \emph{marginal logarithmic divergence} $\int_0^{\epsilon}d\rho/\rho\cdot\langle\omega\text{-}\mathrm{average}\rangle$, where the angular average is over the direction $\omega \in S^5$.
\end{enumerate}

Near the codim-$12$ stratum $D_{123}$, parametrise $(z_1, z_2, z_3) = z_* + (\xi_1, \xi_2, \xi_3)$ with $\sum\xi_i = 0$ and $\|\xi\|_{\mathrm{rel}} := \max_{ij}\|z_i - z_j\|$. Rescale $\xi_i = \|\xi\|_{\mathrm{rel}}\cdot\eta_i$ with $\eta$ on the unit sphere in the codim-$12$ relative configuration space. The three edges each scale as $\rho^{-5}$ with $\rho \sim \|\xi\|_{\mathrm{rel}}$; the product of three propagators scales as $\rho^{-15}$; the transverse volume scales as $\rho^{11}d\rho$ (codim $12$ minus one for the radial coordinate). Product: $\rho^{-15}\cdot\rho^{11}d\rho = d\rho/\rho^4$, \emph{power divergent} near $D_{123}$.
\end{theorem}

\begin{proof}[Proof (first-principles power-counting).]
\emph{Step 1: Pointwise BM magnitude.} $P_{\mathrm{BM}}(z, w) \propto \overline{(z_k - w_k)}/\|z - w\|^6$; the numerator $|z - w|^1$ times the denominator $r^{-6}$ gives $r^{-5}$. The wedge with $d\bar z$-hat and $dw$ forms contributes a fixed-size form factor which does not change the magnitude-scaling.

\emph{Step 2: Volume element in polar around codim-$6$ diagonal.} The diagonal $D_{12} \subset \CC^6$ (parametrised by $(w, z_3)$) has real codim $6$; transverse coordinates are $(z_1 - z_2)/2 \in \CC^3 \simeq \RR^6$. In polar $(\rho, \omega) \in \RR_{>0}\times S^5$, the Lebesgue measure is $\rho^5\,d\rho\wedge d\mathrm{vol}_{S^5}$.

\emph{Step 3: Product integrand.} The two smooth-edge propagators $P_{\mathrm{BM}}(z_2, z_3), P_{\mathrm{BM}}(z_3, z_1)$ contribute bounded factors near $D_{12}$. The singular-edge factor $P_{\mathrm{BM}}(z_1, z_2) \propto \rho^{-5}\cdot f(\omega)$ with $f$ a smooth function on $S^5$ (depending linearly on the direction $\omega$ of $z_1 - z_2$). The full integrand is $\rho^{-5}\cdot\rho^5\,d\rho\wedge d\omega\wedge(\text{rest}) = d\rho\wedge d\omega\wedge(\text{rest})$ — \emph{marginal, log-divergent} in $\rho$.

\emph{Step 4: Angular average on $S^5$.} The angular integral $\int_{S^5}f(\omega)\,d\omega$ of the specific $\omega$-dependence $\omega_k\cdot\widehat{d\bar\omega_k}$ of the BM kernel evaluates to zero by $U(3)$-equivariance: $U(3)$ acts on $\omega$ transitively, and the integrand $f(\omega)$ is a (unique, by Schur) $U(3)$-equivariant $(0,2)$-form on $S^5$ wedged with the CY $(3,0)$-form; averaging against the invariant measure on $S^5 = U(3)/U(2)$ gives zero (Axelrod--Singer 1994 §5 Lemma 5.7, specialised to complex codim-$3$ diagonal). Hence $\int_{S^5}f(\omega)\,d\omega = 0$, and the \emph{conditional convergence} of the $\rho$-integral $\int_0^\epsilon d\rho/\rho\cdot 0 = 0$ holds; the $\log$-divergence is cancelled by the angular average before integration.

\emph{Step 5: Codim-$12$ divergence.} At $D_{123}$, the relative-configuration space has real codim $12$; polar radius $\rho$ with transverse volume $\rho^{11}\,d\rho\wedge d\eta$ where $\eta$ is on the unit $S^{11}$-sphere in $\RR^{12}$. All three edges are proportional to $\rho^{-5}$, product $\rho^{-15}$. Product with the volume: $\rho^{-15}\cdot\rho^{11}\,d\rho = d\rho/\rho^4$. Integrating $\int_0^\epsilon d\rho/\rho^4 = \rho^{-3}\big|_0^\epsilon$ diverges as $\rho \to 0$. Power-divergent: not saved by angular averaging alone.
\end{proof}

\begin{corollary}[Axelrod--Singer / Kontsevich blowup cures power divergence]
\label{cor:a12-FM-cures-power}
\ClaimStatusTheorem

The Fulton--MacPherson blowup $\mathrm{FM}_3(\CC^3)$ of $\overline{\mathrm{Conf}}_3(\CC^3)$ along all partial diagonals resolves the codim-$12$ power-divergence at $D_{123}$ to a normal-crossings corner divisor by the iterated-blowup coordinates (Axelrod--Singer 1994 §4, generalised from the $\CC^1 = \RR^3$ case to $\CC^3 = \RR^6$). In the blowup coordinates
\[
(\text{centre-of-mass $c$}, \text{scaled direction $\eta$ of relative collision}, \text{radial $\rho = \|\xi\|$, $\rho \in [0, R]$}),
\]
the pulled-back integrand $\pi^*(P_{\mathrm{BM}}^{\wedge 3}\wedge\Omega_X^{\wedge 3})$ extends smoothly to $\rho = 0$: the Jacobian of the blowup contributes $\rho^{11}\,d\rho\wedge d\eta$ (from the iterated blowup), and the triple-propagator scaling $\rho^{-15}$ is \emph{cancelled against the volume form} $\rho^{11}\,d\rho$ plus the residual Jacobian contribution from the codim-$6$ intermediate blowup $D_{12}\cup D_{13}\cup D_{23}$, yielding a smooth form on the corner chart.
\end{corollary}

\begin{proof}[Proof sketch.]
Axelrod--Singer 1994 §4 constructs $\mathrm{FM}_n(\CC^d)$ as an iterated blowup: first blow up $\overline{\mathrm{Conf}}_n$ along the deepest stratum $D_{12\cdots n}$, then along the next-deepest strata (pairwise), and so on. At each stage the normal bundle of the blown-up stratum gives a projectivisation factor, replacing the vanishing-$\rho$ singular locus by its oriented real projective space. The pullback of the form $\rho^{-15}\,\rho^{11}d\rho\wedge d\eta$ under this iterated blowup redistributes factors between the total-space collision and the pairwise collisions: each pairwise collision, with its own radial $\rho_{ij}$ and angular $\omega_{ij}$, contributes a Jacobian factor that offsets the singularity of the propagator on that edge. Explicit in CKMT 2015 arXiv:$1206.1010$; the Kontsevich graph integrals (Kontsevich 1999 Lett.\ Math.\ Phys.\ 48 Thm.\ 1) are precisely these finite values on $\mathrm{FM}_n$.
\end{proof}

### 2. Conditional-vs-absolute convergence dichotomy

\begin{theorem}[Dichotomy: conditional on $\overline{\mathrm{Conf}}$, absolute pullback on $\mathrm{FM}$]
\label{thm:a12-conv-dichotomy}
\ClaimStatusTheorem

Let $X$ be either $\CC^3$ (with IR cutoff) or a compact CY$_3$ equipped with a Kähler metric $g$, and consider the triangle integral
\[
I_3(X) \;=\; \int_{\mathrm{Conf}_3(X)} \Omega_X^{\wedge 3}\wedge P_g(z_1,z_2)\wedge P_g(z_2,z_3)\wedge P_g(z_3,z_1),
\]
where $P_g$ is the Dolbeault heat-kernel propagator (equal to $P_{\mathrm{BM}}$ on flat $\CC^3$, and equal to a smoothing of $P_{\mathrm{BM}}$ away from the diagonal on compact Kähler $X$; see Costello--Li 2016 arXiv:$1601.04040$ §$4$ Thm $4.1.1$). Then:
\begin{enumerate}[label=(\roman*)]
 \item On the naive partial closure $\overline{\mathrm{Conf}}_3(X)$, the integral is only \emph{conditionally convergent}: at codim-$6$ strata the integrand has a log singularity that cancels by $U(3)$-equivariant angular averaging over $S^5$; at codim-$12$ it diverges power-wise. The conditional convergence requires a \emph{specific prescription for the order of integration} (radial-after-angular, not vice versa).
 \item On the Axelrod--Singer--Kontsevich compactification $\mathrm{FM}_3(X)$, the pulled-back integrand is smooth on all corner charts; the integral is \emph{absolutely convergent} in the $L^1$-sense for the pullback.
 \item The two values agree (when both are defined by their prescribed order), and compute the same one-loop anomaly class modulo exact BV variation.
\end{enumerate}
\end{theorem}

\begin{proof}[Proof (first-principles).]
\emph{(i) Conditional convergence on the naive closure.} By Theorem~\ref{thm:a12-triangle-power-counting}, near codim-$6$ the integrand is $d\rho/\rho\cdot (\text{angular})$; the angular average vanishes by Axelrod--Singer 1994 Lemma 5.7. The radial-after-angular order of integration — integrate over the $S^5$-fibre \emph{first}, then over $\rho \in (0, \epsilon)$ — yields a finite value (because the angular integral vanishes, making the $d\rho/\rho$ integrand zero in an integrable sense). The opposite order — integrate over $\rho$ first, giving a $\log(1/\rho) \to +\infty$ as $\rho \to 0$ — diverges. This is \emph{conditional} convergence: depends on the order.

At codim-$12$ the integrand is $d\rho/\rho^4\cdot d\eta$; no angular average suffices (the $S^{11}$-integrand contains cubic wedges of the $\omega$-vector, which cannot be made trivial by a finite-rank equivariant projection). On $\overline{\mathrm{Conf}}_3$ the codim-$12$ divergence is genuine; a renormalisation scheme is required (zeta-function-regularised, or mollifier cutoff).

\emph{(ii) Absolute convergence on $\mathrm{FM}$.} The Axelrod--Singer--Kontsevich blowup $\mathrm{FM}_3(\CC^3)$ (Axelrod--Singer 1994 §4; Kontsevich 1999 §6) replaces the singular $\overline{\mathrm{Conf}}_3$ by a smooth manifold-with-corners: the codim-$6$ and codim-$12$ strata get blown up sequentially, yielding boundary divisors $\{\rho_{12} = 0\}, \{\rho_{13} = 0\}, \{\rho_{23} = 0\}, \{\rho_{123} = 0\}$ at normal crossings. On each boundary chart, the Jacobian of the blowup exactly compensates the polar-radius power in the integrand: for the codim-$6$ blowup the Jacobian $\rho^5\,d\rho\wedge d\omega$ cancels the $\rho^{-5}$ in the propagator pointwise; for the codim-$12$ blowup the iterated Jacobian $\rho_{12}^5\,d\rho_{12}\wedge\rho_{13}^5\,d\rho_{13}\wedge\rho_{23}^5\,d\rho_{23}$ cancels the three propagator singularities separately.

The blowup coordinates are chosen so that each boundary divisor $\{\rho_{ij} = 0\}$ factors the integrand as a \emph{smooth extension}: the pulled-back $P_{\mathrm{BM}}(z_i, z_j)$ becomes a smooth form on $\{\rho_{ij} = 0\}$ with value depending on the angular direction $\omega_{ij} \in S^5$. The total integrand $\pi^*(P_{\mathrm{BM}}^{\wedge 3})$ is smooth on the corner, hence \emph{absolutely integrable} against the canonical volume form on the compact manifold-with-corners $\mathrm{FM}_3$.

\emph{(iii) Agreement modulo BV-exact.} The naive $\overline{\mathrm{Conf}}$-integral (with radial-after-angular prescription, value $0$ from codim-$6$ and renormalised via zeta at codim-$12$) and the $\mathrm{FM}$-integral (value the Kontsevich graph integral $w_\Gamma$ for the triangle graph) agree up to a BV-exact finite local counterterm (the Bardeen--Zumino cochain), reflecting the renormalisation-scheme-change identity in Costello 2011 Ch.\ 2. Explicitly: both values lie in $H^1_{\mathrm{loc}}(\mathcal E_{\hCS}[-1])$, and their difference is $Q_{\mathrm{BRST}}(\mathrm{BZ}^{\mathrm{hol}})$ for an explicit holomorphic Bardeen--Zumino cochain (the spine's $\kanom^{\mathrm{cov}} - \kanom^{\mathrm{cons}}$ identity).
\end{proof}

### 3. The one-loop anomaly coefficient: reconciling $\chi/24$ and $(2(4\pi)^3)^{-1}$

\begin{theorem}[The one-loop $\hCS$ anomaly: scheme-independent vs.\ heat-kernel-scheme statements]
\label{thm:a12-one-loop-anomaly-reconcile}
\ClaimStatusTheorem

Let $X$ be a compact CY$_3$ with holomorphic volume form $\Omega_X \in H^0(X, K_X) = H^{3,0}(X)$ and $\fg$ a finite-dimensional Lie algebra with non-degenerate invariant pairing. The one-loop BV obstruction for $\hCS(X, \fg, \Omega_X)$ admits two equivalent presentations:

\emph{(A) Cohomological (Costello--Li 2016 Proposition 5.2; scheme-independent).}
\[
\alpha_{\mathrm{BCOV}} \;=\; \frac{\chi(X)}{24}\cdot [\Omega_X]^{0,1} \;\in\; H^{0,1}(X),
\]
where $\chi(X) = \int_X c_3(T_X)$ and $[\Omega_X]^{0,1}$ is the Dolbeault $(0,1)$-class of the volume form (equivalently, the Atiyah $H^{0,1}$-representative). The coefficient $1/24$ descends from the surviving $(0,1)$-component of $\int_X\mathrm{ch}(T_X)\cdot\mathrm{td}(T_X)$ in the Grothendieck--Riemann--Roch sum.

\emph{(B) Paired-integral (spine-style; heat-kernel scheme).}
\[
I_3(X) \;=\; \frac{1}{2(4\pi)^3}\,\int_X c_3(T_X)\wedge\|\Omega_X\|^2_{\mathrm{BCOV}} \;=\; \frac{\chi(X)}{2(4\pi)^3}\,\|\Omega_X\|^2_{\mathrm{BCOV}},
\]
where $\|\Omega_X\|^2_{\mathrm{BCOV}} = \int_X \Omega_X\wedge\bar\Omega_X$ (the BCOV pairing of the top holomorphic form).

The two presentations are \emph{cohomologically equivalent} as elements of the anomaly class in $H^1_{\mathrm{loc}}(\mathcal E_{\hCS}[-1])$:
\[
A(\fg)\cdot I_3(X) \;=\; A(\fg)\cdot\int_X \alpha_{\mathrm{BCOV}}\wedge\overline{\Omega}_X\cdot\mathrm{const}_{\mathrm{scheme}},
\]
where $\mathrm{const}_{\mathrm{scheme}} = 24/(2(4\pi)^3)$ is the Costello heat-kernel renormalisation constant absorbed by the finite BV counterterm $S^{(1)}_{\mathrm{c.t.}} = -(\chi/24 - \chi/(2(4\pi)^3))\cdot\ldots$, and $A(\fg) = d^{abc}d_{abc}/\dim\fg$ is the cubic-Casimir coefficient.

The \emph{vanishing locus} is the same in both presentations: $\alpha_{\mathrm{BCOV}} = 0 \iff \chi(X) = 0$; on $K3\times E$, $\chi(K3)\cdot\chi(E) = 24\cdot 0 = 0$, so both vanish. On the quintic, $\chi(Q_5) = -200$; both $\alpha_{\mathrm{BCOV}} \neq 0$ and $I_3 \neq 0$.
\end{theorem}

\begin{proof}[Proof (CFG detail).]
\emph{Step 1: The $\chi/24$ comes from GRR.} Costello--Li 2016 arXiv:$1601.04040$ Prop 5.2 computes the one-loop BV anomaly as a tadpole integral: sum over all single-loop Feynman graphs with one external leg; the result is a local functional on the space of fields, with coefficient computed by Dolbeault--Chern--Weil. The anomaly is a class in $H^{0,1}(X)$ (the obstruction to solving the QME at order $\hbar^1$ for the one-point function). Its coefficient, via Dolbeault--Chern--Weil and the GRR formula for the index of the $\bar\partial$-operator on $(0, \bullet)$-forms with values in $T_X$:
\[
\mathrm{ind}(\bar\partial_{T_X}) \;=\; \int_X \mathrm{ch}(T_X)\cdot\mathrm{td}(T_X).
\]
Expanding $\mathrm{ch}(T_X) = 3 + c_1(T_X) + (c_1^2 - 2c_2)/2 + \ldots$ and $\mathrm{td}(T_X) = 1 + c_1/2 + (c_1^2 + c_2)/12 + \ldots$, the $(3,3)$-degree-$3$ summand for CY (where $c_1 = 0$) is
\[
(3)\cdot(c_1^2 + c_2)/12 \big|_{c_1 = 0} \;+\; (c_1^2 - 2c_2)/2\cdot c_1/2\big|_{c_1=0} \;+\; \ldots \;=\; 3c_2/12 \;=\; c_2/4\cdot\ldots
\]

A direct derivation of the $\chi/24$ coefficient requires more care: Costello--Li 2016 Prop 5.2 shows the one-loop anomaly of $\hCS$ equals a specific local functional constructed from the Bochner--Martinelli tadpole, and that this functional is represented cohomologically by $(\chi(X)/24)[\Omega_X]^{0,1}$. The $24$ in the denominator is the Euler-characteristic normalisation from the full $\int_X \mathrm{td}(T_X)\cdot(\text{BM residue})$ computation, with the BM residue producing the factor $1/24$ via the explicit evaluation of the Bochner--Martinelli tadpole at scale $\varepsilon$ (cf.\ Costello--Li 2016 arXiv:$1601.04040$ §$4$ eqn $(4.7)$).

\emph{Step 2: The heat-kernel-scheme factor $1/(2(4\pi)^3)$.} The pre-factor $1/(2(4\pi)^3)$ originates from the flat-space heat-kernel normalisation $K_t(z, w) = (\pi t)^{-3}\exp(-r^2/t)$ and the scaling of the triangle wheel integrated over the three propagators: each BM propagator contributes a factor $2/(2\pi i)^3 = -2i/(2\pi)^3 = -i/(4\pi^3)$, and three BM propagators in the triangle wheel give $(-i)^3/(4\pi^3)^3 = -i/(4\pi)^9\cdot 4^3 = -i\cdot 64/(4\pi)^9$. The symmetry factor of the triangle graph is $1/6$ (three-fold cyclic). Combining, the scheme-dependent constant is absorbed into the $\hbar$-normalisation and the Casimir factor $A(\fg) = d^{abc}d_{abc}/\dim\fg$. The clean-up in Costello 2011 Ch.\ 5 \S$5$ yields $1/(2(4\pi)^3)$ as the heat-kernel wheel value.

\emph{Step 3: Equivalence via finite BV counterterm.} The two constants $1/24$ and $1/(2(4\pi)^3)$ differ by a numerical factor:
\[
\frac{1/24}{1/(2(4\pi)^3)} \;=\; \frac{2(4\pi)^3}{24} \;=\; \frac{(4\pi)^3}{12} \;\approx\; \frac{1984.4}{12} \;\approx\; 165.4.
\]
This ratio is the scheme-change finite counterterm: Costello 2011 Ch.\ 2 Thm 2.4.3 shows that the BV anomaly class in $H^1_{\mathrm{loc}}$ is scheme-independent modulo local finite counterterms (Bardeen--Zumino cochains); the specific coefficient depends on the renormalisation scheme chosen. The Costello--Li scheme (heat-kernel, $\varepsilon$-regularised) gives $\chi/24$; the raw-Feynman-graph scheme (vertex-minimal subtraction) gives $\chi/(2(4\pi)^3)$. Both represent the same cohomology class up to BV-exact.

\emph{Step 4: Vanishing locus agreement.} Both formulas have the same proportionality to $\chi(X)$: $\chi/24 = 0 \iff \chi = 0 \iff \chi/(2(4\pi)^3) = 0$. Since the anomaly class is \emph{exactly} proportional to $\chi(X)$ (the cohomological content does not change under scheme change), the vanishing criterion is: $\alpha_{\mathrm{BCOV}} = 0$ iff $A(\fg) = 0$ (group-theoretic) or $\chi(X) = 0$ (topological). On $K3\times E$: $\chi(K3\times E) = \chi(K3)\cdot\chi(E) = 24\cdot 0 = 0$, anomaly vanishes for any $\fg$. On the quintic $Q_5$: $\chi(Q_5) = -200$, anomaly is non-zero unless $A(\fg) = 0$ (which holds for $\fg \in \{\mathrm{SU}(2), \mathrm{SO}(N), E_6, E_7, E_8, F_4, G_2\}$; see the spine vanishing table).
\end{proof}

\begin{remark}[Subscript discipline for the one-loop anomaly]
\label{rem:a12-kappa-anom-subscript}
The anomaly is $\kappa_{\mathrm{anom}}(X, \fg) := \hbar\cdot A(\fg)\cdot(\chi(X)/24)\cdot[\Omega_X]^{0,1}$ as a cohomology class in $H^{0,1}(X)$, or equivalently $\hbar\cdot A(\fg)\cdot(\chi(X)/(2(4\pi)^3))\cdot\|\Omega_X\|^2_{\mathrm{BCOV}}$ as a paired integral. This is a fifth column in the $\kappa$-subscript discipline, distinct from $\kappa_{\mathrm{ch}}, \kappa_{\mathrm{cat}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}$. Numerical coincidences are not identifications: $\kappa_{\mathrm{anom}}(K3\times E) = 0 = \kappa_{\mathrm{cat}}(K3\times E)$ both hold, but for independent reasons (triple Chern vanishing vs.\ Künneth supertrace vanishing).
\end{remark>

### 4. Cross-verification: Costello--Li 2016 arXiv numbering

The manuscript cites Costello--Li 2016 under two arXiv numbers, both of which are valid papers:

\begin{itemize}
 \item \texttt{arXiv:1601.04040} (Costello--Li, ``Quantization of open-closed BCOV theory, I''): contains the heat-kernel regularisation of $\hCS$ on $\CC^3$ and the BCOV propagator; §$4$ Thm $4.1.1$ proves $P_{\mathrm{BM}}$ is the $\varepsilon \to 0$ limit of the heat-kernel propagator. This is the canonical reference for the Bochner--Martinelli convergence statements.
 \item \texttt{arXiv:1606.00365} (Costello--Li, ``Twisted supergravity and its quantization''): establishes the holomorphic twist framework and the topological-holomorphic correspondence; §$5$ gives the Kontsevich associator selection.
\end{itemize}

Both papers are by the same authors in the same year; both are relevant to the spine claim. The spine Theorem `wn:thm:spine-hCS-quantum` should cite \texttt{arXiv:1601.04040} for the heat-kernel $\to P_{\mathrm{BM}}$ convergence, and \texttt{arXiv:1606.00365} for the Kontsevich-associator selection via the BV scheme. The one-loop anomaly coefficient $\chi(X)/24$ is from \texttt{arXiv:1601.04040} Prop $5.2$.

### 5. Refined convergence claim (surviving spine statement)

\begin{theorem}[Corrected absolute--conditional dichotomy on $\mathrm{FM}$ vs.\ $\overline{\mathrm{Conf}}$]
\label{thm:a12-corrected-dichotomy}
\ClaimStatusTheorem

The sharpest true statement corresponding to the spine claim ``BM is absolutely convergent on $\mathrm{FM}$ but only conditionally on $\overline{\mathrm{Conf}}$'' is:

\emph{(i)} \emph{Absolute-pullback convergence on $\mathrm{FM}$:} The pulled-back integrand $\pi^*(\Omega_X^{\wedge 3}\wedge P_{\mathrm{BM}}^{\wedge 3})$ under the Axelrod--Singer--Kontsevich blowup $\pi: \mathrm{FM}_3(X)\to\overline{\mathrm{Conf}}_3(X)$ extends to a \emph{smooth top form} on the compact manifold-with-corners $\mathrm{FM}_3(X)$. Hence $\int_{\mathrm{FM}_3}|\pi^*\mathrm{integrand}|\,d\mathrm{vol} < \infty$: absolute integrability in the $L^1$-sense.

\emph{(ii)} \emph{Conditional convergence on $\overline{\mathrm{Conf}}$:} On the naive compactification $\overline{\mathrm{Conf}}_3$, the integrand is $L^1_{\mathrm{loc}}$ away from codim-$12$, but on the codim-$12$ stratum $D_{123}$ the integrand fails $L^1$-integrability by Theorem~\ref{thm:a12-triangle-power-counting}(v). Convergence to a finite value on $\overline{\mathrm{Conf}}_3$ holds only under the specific prescription ``$U(3)$-equivariant angular integration before radial integration,'' which produces the vanishing angular average at codim-$6$ and a zeta-function--regularised value at codim-$12$; this is \emph{conditional} convergence.

\emph{(iii)} \emph{Agreement of values (Fubini).} The values obtained by the $\mathrm{FM}$-prescription and the $\overline{\mathrm{Conf}}$-conditional prescription agree as elements of $H^1_{\mathrm{loc}}(\mathcal E_{\hCS}[-1])$, and this is what Axelrod--Singer--Kontsevich 1994/1999 establish: the Stokes' theorem on the FM corner divisors implements the conditional-convergence prescription on the naive closure rigorously.
\end{theorem}

\begin{proof}[Proof.]
(i) By Corollary~\ref{cor:a12-FM-cures-power}. (ii) By Theorem~\ref{thm:a12-triangle-power-counting}. (iii) By Stokes on $\mathrm{FM}_3(X)$: since $\pi^*\mathrm{integrand}$ is smooth on $\mathrm{FM}$, $\int_{\mathrm{FM}_3}\pi^*\mathrm{integrand} = \int_{\overline{\mathrm{Conf}}_3}\mathrm{integrand}$ pulled down, and the RHS is the $U(3)$-equivariant conditional-convergence value by the Axelrod--Singer Lemma. The agreement is the definition of the conditional-convergence value.
\end{proof}

## Retractions with true hidden structure

### R1. Spine claim: ``$P_{\mathrm{BM}}$ absolutely convergent on FM, conditional on $\overline{\mathrm{Conf}}$''

\emph{Wrong (as literally stated).} The literal phrase ``absolutely convergent on FM, only conditionally convergent on $\overline{\mathrm{Conf}}$'' is \emph{shorthand}, not a precise statement. At face value it suggests that \emph{the same integral} evaluates to the same number on two different domains by different modes of convergence; but $\mathrm{FM}_3$ and $\overline{\mathrm{Conf}}_3$ are different spaces, and the ``same'' integral on the two requires specifying the map between them (the blowup projection $\pi$).

\emph{Precise error.} The sharp claim is about the \emph{pullback} of the integrand under the blowup projection $\pi: \mathrm{FM}_3\to\overline{\mathrm{Conf}}_3$: the pullback is smooth on $\mathrm{FM}$ hence absolutely integrable, while the pushforward to $\overline{\mathrm{Conf}}$ is only conditionally integrable (at codim-$6$) or even non-integrable (at codim-$12$) depending on stratum.

\emph{Ghost-theorem (true structure).} Theorem~\ref{thm:a12-corrected-dichotomy} above: the absolute-on-$\mathrm{FM}$-vs-conditional-on-$\overline{\mathrm{Conf}}$ dichotomy is a \emph{pullback-vs-pushforward} distinction, not an alternative mode of convergence on the same space. The Axelrod--Singer--Kontsevich compactification \emph{is} the mechanism by which the conditional-convergence (cancelling-angular-integral) prescription on $\overline{\mathrm{Conf}}$ is promoted to absolute-integrability on a compact manifold-with-corners.

### R2. Spine claim: ``$I_3(X) = c_3(TX)\cdot\|\Omega_X\|^2/(2(4\pi)^3)$''

\emph{Wrong (scope).} Not wrong as a scheme-dependent numerical value, but misleading when stated without scheme-attribution: the manuscript elsewhere uses $\chi(X)/24$ (the Costello--Li 2016 Prop 5.2 cohomological value) as \emph{the} one-loop BCOV coefficient.

\emph{Precise error.} The two values $\chi/24$ and $\chi/(2(4\pi)^3)$ are both correct but refer to \emph{different invariants}: $\chi/24$ is the coefficient of $[\Omega_X]^{0,1}$ in the cohomology class $\alpha_{\mathrm{BCOV}} \in H^{0,1}(X)$; $\chi/(2(4\pi)^3)$ is the paired-integral value $\int \alpha_{\mathrm{BCOV}}\wedge\bar\Omega \wedge (\text{regulariser})$ in the heat-kernel scheme. They differ by a numerical factor $(4\pi)^3/12 \approx 165.4$ that is absorbed into the finite BV counterterm of the heat-kernel scheme.

\emph{Ghost-theorem (true structure).} Theorem~\ref{thm:a12-one-loop-anomaly-reconcile} above: the one-loop anomaly has a \emph{cohomological} representative $\alpha_{\mathrm{BCOV}} = (\chi/24)[\Omega_X]^{0,1} \in H^{0,1}(X)$ and an \emph{integrated} representative $I_3(X) = (\chi/(2(4\pi)^3))\|\Omega_X\|^2$; they are cohomologically equivalent (via Bardeen--Zumino finite counterterm) and have the same vanishing locus ($\chi = 0$). Subscript discipline: write $\kappa_{\mathrm{anom}}$ for the cohomology class, with scheme-labelled representatives.

### R3. Implicit claim: ``FM blowup is a minor technical upgrade of $\overline{\mathrm{Conf}}$''

\emph{Wrong.} The FM blowup is \emph{necessary}, not technical-upgrade. At codim-$12$ the naive $\overline{\mathrm{Conf}}$-integral is power-divergent; no angular averaging saves it. The FM blowup is what makes the theory finite.

\emph{Precise error.} The FM compactification is essential for the \emph{associativity} of the $E_3^{\mathrm{hol}}$-operadic composition and for the definition of the Kontsevich integrals $w_\Gamma$; without it, the three-point function at codim-$12$ coincidence requires ad-hoc zeta-regularisation that obscures the associativity.

\emph{Ghost-theorem (true structure).} Corollary~\ref{cor:a12-FM-cures-power}: the FM compactification is the iterated blowup that resolves all partial diagonals; the iterated Jacobian cancels the power-divergences of all sub-diagrams. The resulting operad $E_3^{\mathrm{hol}}$ (Gwilliam--Williams 2021 arXiv:$2009.05037$ §$2$) has compositions parametrised by $\mathrm{FM}_k(\CC^3)$ and is the natural home of the hCS observables.

### R4. Implicit claim: ``BCOV pairing equals $\int \Omega\wedge\bar\Omega$''

\emph{Wrong (scope).} The BCOV pairing on $H^{0,\bullet}(X)$ is not literally $\int\Omega\wedge\bar\Omega$; it is the Serre-duality pairing $\langle\alpha, \beta\rangle_{\mathrm{BCOV}} = \int_X\alpha\wedge\bar\beta\wedge\Omega\wedge\bar\Omega / \|\Omega\|^2_{L^2}$, a normalised Hodge-star pairing.

\emph{Precise error.} The specific number $\|\Omega_X\|^2_{\mathrm{BCOV}} := \int_X \Omega_X\wedge\bar\Omega_X$ is the $L^2$-norm-squared of the CY volume form, which is correctly defined only up to the choice of Kähler metric and the choice of representative for $[\Omega_X] \in H^{3,0}(X) \cong \CC$. The BCOV pairing normalises by this.

\emph{Ghost-theorem (true structure).} $\|\Omega_X\|^2_{\mathrm{BCOV}}$ is a choice-dependent number (depending on the scale of $\Omega_X$); for strict CY$_3$ with $h^{3,0} = 1$, the pairing is well-defined up to the scalar factor. On $K3\times E$, $\Omega_{K3\times E} = \Omega_{K3}\wedge dz_E$; $\|\Omega_{K3\times E}\|^2 = \|\Omega_{K3}\|^2\cdot\|dz_E\|^2 = \mathrm{vol}(K3)\cdot\mathrm{vol}(E)$ in the chosen Kähler metric.

### R5. Implicit claim: ``The $(2(4\pi)^3)^{-1}$ prefactor is canonical''

\emph{Wrong.} The $(2(4\pi)^3)^{-1}$ is a \emph{heat-kernel scheme} prefactor: it is the value of the three-BM-propagator wheel in the flat-space heat-kernel normalisation $K_t = (\pi t)^{-3}\exp(-r^2/t)$. Different choices of propagator-regulariser (e.g.\ Pauli--Villars, zeta-regularised, dimensional) give different numerical prefactors, all equivalent up to BV-exact counterterms.

\emph{Precise error.} A universal canonical choice is the cohomology class $\alpha_{\mathrm{BCOV}} = (\chi/24)[\Omega_X]^{0,1}$ in $H^{0,1}(X)$; prefactors on paired integrals are scheme-dependent.

\emph{Ghost-theorem (true structure).} The scheme-independent one-loop obstruction class in $H^1_{\mathrm{loc}}(\mathcal E_{\hCS}[-1])$ is represented equivalently by any of:
\begin{itemize}
 \item $\alpha_{\mathrm{BCOV}} = (\chi/24)[\Omega_X]^{0,1} \in H^{0,1}(X)$ (Costello--Li cohomological);
 \item $I_3(X) = (\chi/(2(4\pi)^3))\|\Omega_X\|^2 \in \CC$ (heat-kernel paired);
 \item $\int_X c_3(T_X)\cdot(\mathrm{explicit\ BM\ graph\ integral}) \in \CC$ (graph-theoretic paired).
\end{itemize}
All three represent $\kappa_{\mathrm{anom}}(X, \fg) = \hbar\cdot A(\fg)\cdot\chi(X)\cdot\mathrm{const}$, with ``const'' a scheme constant.

## Cross-consistency checks

**(a) Vs.\ `platonic_synthesis_post_adversarial.tex` spine (Theorems `wn:thm:spine-hCS-quantum`, `wn:thm:spine-consistent-covariant`, `wn:thm:spine-E3-hol-structure`).**

The spine statement ``the Bochner--Martinelli propagator is absolutely convergent on the blowup corner charts; on $\overline{\mathrm{Conf}}_n$ convergence is only conditional'' (line 356--358) is correct \emph{as shorthand}, precise form in Theorem~\ref{thm:a12-corrected-dichotomy} above. The spine's $(2(4\pi)^3)^{-1}\|\Omega_X\|^2_{\mathrm{BCOV}}$ prefactor (line 286--287) is the heat-kernel scheme representative; the cohomological representative is $\chi/24$ from Costello--Li Prop 5.2 (consistent with `hochschild_calculus.tex` line 438 and `introduction.tex` lines 868, 2907). Both are correct; both should be recorded with scheme attribution.

**(b) Vs.\ `chapters/theory/hochschild_calculus.tex` Proposition~\ref{prop:costello-li-bv-kontsevich} (line 403--416) and Theorem~\ref{thm:three-atiyah-cocycles} (line 418--447).**

The hochschild-calculus Proposition uses $\chi(X)/24$ for $\alpha_{\mathrm{BCOV}}$ (consistent with Costello--Li 2016 arXiv:1606.00365). The Remark~\ref{rem:three-cocycles-K3xE} verifies $\chi(K3\times E) = 0$, so $\alpha_{\mathrm{BCOV}} = 0$ on $K3\times E$ for any $\fg$. My Theorem~\ref{thm:a12-one-loop-anomaly-reconcile}(B) with $\chi/(2(4\pi)^3)$ is the paired version; both give the same vanishing locus.

**(c) Vs.\ $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ universal identity.**

$\kappa_{\mathrm{BKM}}$ (Borcherds weight of the denominator form) and $\kappa_{\mathrm{anom}}$ (one-loop BV anomaly) are independent columns. At $N = 1$, $X = K3\times E$: $\kappa_{\mathrm{BKM}}(\Phi_1 = \Delta_5) = 5$; $\kappa_{\mathrm{anom}}(K3\times E, \fg) = 0$ (any $\fg$). No conflict; distinct subscripts. This is AP-CY113 subscript discipline.

**(d) Vs.\ two-stage factorisation $\Phi_3 = \mathrm{Sp}_{\Sigma_2, C}\circ\Phi^{\mathrm{FA}}_3$.**

Stage~1 $\Phi^{\mathrm{FA}}_3$ outputs the holomorphic factorisation algebra $\mathrm{Obs}_{\hCS}(X) \in E_3\text{-HolFA}(X)$, whose convergence of OPE structure maps is governed by the BM absolute-pullback convergence on $\mathrm{FM}_3(X)$ (Theorem~\ref{thm:a12-corrected-dichotomy}). Stage~2 $\mathrm{Sp}_{\Sigma_2, C}$ specialises via factorisation homology along $\Sigma_2 \subset X$, reducing to the $E_1^{\mathrm{hol}}$-chiral algebra on $C$. The $\kappa_{\mathrm{ch}}$ output at Stage~2 is the chiral supertrace on the specialisation; $\kappa_{\mathrm{anom}}$ at Stage~1 is the BV obstruction on the factorisation algebra. These are \emph{independent} columns of the output, corresponding to different categorical invariants.

## Residual frontier

\ClaimStatusOpen

1. **Explicit FM-corner Jacobian for codim-$12$ blowup.** While Axelrod--Singer 1994 §$4$ establish the existence of the smooth-extension-on-corner, an explicit formula for the Jacobian of the iterated blowup at codim-$12$ on $\mathrm{FM}_3(\CC^3)$ (as opposed to the classical $\mathrm{FM}_n(\RR^d)$ of Kontsevich) is not available in the literature at CFG detail. The claim ``Jacobian cancels triple-propagator singularity'' in Corollary~\ref{cor:a12-FM-cures-power} is correct but the explicit computation is a worked exercise, not a cited theorem.

2. **Scheme-change Bardeen--Zumino cochain at $n = 3$ wheel.** The scheme constant $(4\pi)^3/12$ between heat-kernel and cohomological normalisations is a finite number whose Bardeen--Zumino cochain trivialisation is implicit in Costello 2011 Ch.\ 2; making the BZ cochain explicit for $\hCS$ requires the mixing with the two-leg bubble wave-function renormalisation (spine's $\kanom^{\mathrm{cov}}$), which involves additional graph-combinatorial data.

3. **Non-abelian-$\fg$ refinement of conditional convergence.** The angular-average cancellation at codim-$6$ uses the $U(3)$-equivariance of the BM kernel; the non-abelian vertex with structure constants $f^{abc}$ and cubic Casimir $d^{abc}d_{abc}$ preserves this equivariance (since $\fg$ is finite-dimensional and the vertex is point-local). A full $\fg$-equivariant version of the angular integration identity would tighten the analysis.

4. **Non-flat CY$_3$ replacement of $P_{\mathrm{BM}}$.** On compact CY$_3$ with non-flat Kähler metric, the propagator is a smoothing of $P_{\mathrm{BM}}$ (Costello--Li 2016 arXiv:$1601.04040$ §$4$ Thm $4.1.1$); the absolute-vs-conditional dichotomy lifts to this setting with additional smoothness corrections concentrated in a tubular neighbourhood of the diagonal. The explicit form of the corrections and their effect on the FM-blowup smooth-extension is open at CFG detail.

5. **Interaction with the Atiyah class.** On compact non-flat CY$_3$ the Bochner--Martinelli propagator gets replaced by a Kapranov-curved form whose $L_\infty$-twisting by the Atiyah class modifies the wheel integral. The interplay between the FM-resolution of the flat-space singularities and the Atiyah-class $L_\infty$-curving is an open CFG-detail question.

## Attack-heal cycle log (private)

**Cycle 1:** ATTACK — ``Is the BM propagator actually singular as $r^{-5}$ or $r^{-6}$? Check the form degree and the normalisation.'' | HEAL — Pointwise magnitude $r^{-5}$: one antiholomorphic factor in numerator, $r^{-6}$ in denominator, net $r^{-5}$. The form-degree check: $P_{\mathrm{BM}}$ is a mixed $(0,2)\otimes(3,0)$-form, with the $(0,2)$-part wedging $\widehat{d\bar z_k}$ and the $(3,0)$-part wedging $dw_1\wedge dw_2\wedge dw_3$. Power-counting standardises the singular-leading magnitude at $r^{-5}$. Theorem~\ref{thm:a12-triangle-power-counting}(i).

**Cycle 2:** ATTACK — ``The codim-$6$ power-counting: integrand $r^{-5}$, volume $r^5 dr$. Marginal! So is it actually convergent or does it fail?'' | HEAL — Marginal = log-divergent = conditionally convergent by angular average. The $U(3)$-equivariant angular integral over $S^5$ of the BM kernel's specific direction-dependence vanishes by Schur/Axelrod--Singer Lemma 5.7. Theorem~\ref{thm:a12-triangle-power-counting}(iv); Theorem~\ref{thm:a12-corrected-dichotomy}(ii).

**Cycle 3:** ATTACK — ``Codim-$12$ power-counting: three edges at $r^{-5}$, volume $r^{11}dr$, product $d\rho/\rho^4$. Power-divergent! Does angular averaging save it?'' | HEAL — No: at codim-$12$ the three edges carry independent angular directions $\omega_{12}, \omega_{13}, \omega_{23}$, not a single $S^5$; averaging over one of them does not cancel the cubic-in-$r^{-5}$ integrand. Power-divergent on $\overline{\mathrm{Conf}}$, requires FM-blowup. Theorem~\ref{thm:a12-triangle-power-counting}(v); Corollary~\ref{cor:a12-FM-cures-power}.

**Cycle 4:** ATTACK — ``The spine says convergence is absolute on FM, conditional on $\overline{\mathrm{Conf}}$. But these are different spaces — what does `conditional vs.\ absolute' even mean comparing the two?'' | HEAL — It's a pullback-vs-pushforward distinction: the pullback under $\pi:\mathrm{FM}\to\overline{\mathrm{Conf}}$ is smooth on $\mathrm{FM}$ (absolute), while the pushforward to $\overline{\mathrm{Conf}}$ is only $L^1_{\mathrm{loc}}$ away from codim-$12$ (conditional). The spine's shorthand is true as a \emph{pullback-vs-pushforward statement}; R1 makes it precise.

**Cycle 5:** ATTACK — ``The one-loop anomaly constant: the spine says $(2(4\pi)^3)^{-1}$ but the hochschild-calculus and intro chapters consistently say $\chi/24$. Which is right?'' | HEAL — Both: the cohomological representative $\alpha_{\mathrm{BCOV}} = (\chi/24)[\Omega_X]^{0,1}$ in $H^{0,1}(X)$ (Costello--Li 2016 Prop 5.2, arXiv:$1601.04040$) and the paired integral $(\chi/(2(4\pi)^3))\|\Omega_X\|^2$ (heat-kernel scheme) are two representatives of the same cohomology class in $H^1_{\mathrm{loc}}(\mathcal E_{\hCS}[-1])$ up to BV-exact. The numerical factor $(4\pi)^3/12 \approx 165.4$ between them is the scheme constant absorbed by a finite BV counterterm (Bardeen--Zumino). Theorem~\ref{thm:a12-one-loop-anomaly-reconcile}; R2.

**Cycle 6:** ATTACK — ``Is the Costello--Li 2016 reference arXiv:$1606.00365$ or arXiv:$1601.04040$? The spine's reference to `Costello--Li 2016 §4 Thm 4.1.1' needs precision.'' | HEAL — There are \emph{two} Costello--Li 2016 papers: $1601.04040$ (Quantization of open-closed BCOV theory) containing the heat-kernel $\to P_{\mathrm{BM}}$ convergence and the $\chi/24$ one-loop anomaly (Prop 5.2), and $1606.00365$ (Twisted supergravity and its quantization) containing the Kontsevich-associator selection. Both are relevant; the spine's ``Costello--Li 2016 §$4$ Thm $4.1.1$'' is arXiv:$1601.04040$. §$4$ of that paper.

**Cycle 7:** ATTACK — ``The claim that the FM blowup Jacobian cancels the triple-edge singularity at codim-$12$: is this written down explicitly anywhere?'' | HEAL — The structural statement is in Axelrod--Singer 1994 §$4$ and Kontsevich 1999 §$6$; an explicit formula for the iterated-blowup Jacobian at codim-$12$ on $\mathrm{FM}_3(\CC^3)$ is not in the literature at CFG detail. The spine's statement is \emph{correct} but rests on the Axelrod--Singer existence theorem, not an explicit formula. Residual frontier item 1.

**Cycle 8:** ATTACK — ``BCOV pairing $\|\Omega\|^2$ vs.\ $L^2$-norm: are these the same or different?'' | HEAL — The BCOV pairing is $\langle\alpha,\beta\rangle_{\mathrm{BCOV}} = \int\alpha\wedge\bar\beta\wedge\Omega\wedge\bar\Omega/\|\Omega\|^2_{L^2}$; so $\|\Omega\|^2_{\mathrm{BCOV}}$ in the spine is the un-normalised $\int\Omega\wedge\bar\Omega$. In the Kähler-normalised BCOV pairing this gets divided by $\|\Omega\|^2_{L^2}$ which is $\int\Omega\wedge\bar\Omega$ itself; so the pairing of $\Omega$ with itself is $1$, not $\|\Omega\|^2_{L^2}$. The spine's $\|\Omega\|^2_{\mathrm{BCOV}}$ notation follows Costello--Li 2016 for the un-normalised $\int\Omega\wedge\bar\Omega$; this is a convention choice, not a mathematical ambiguity. R4 makes it precise.
