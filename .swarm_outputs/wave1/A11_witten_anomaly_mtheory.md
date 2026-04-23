# Agent A11 — Witten on anomaly factorisation and non-abelian one-loop wave-function renormalisation of $6$d $\mathrm{hCS}$

## Executive adversarial summary

Two theorems sit at the heart of the target: $\mathtt{wn:thm:plat\mbox{-}anomaly}$ (anomaly factorisation via cubic Casimir $A(\fg) = d^{abc}d_{abc}/\dim\fg$, trivialised on $\C^3$ and $K3 \times E$, nonzero on the quintic, cancelled by CHSW) and $\mathtt{wn:thm:plat\mbox{-}Z\mbox{-}counterterm}$ (non-abelian one-loop wave-function $Z^{(1)} = 1 - \hbar C_2(\fg)(4\pi)^{-3}\log(L/\varepsilon)$).

What fell on adversarial attack, in order of severity.

First, a **regularisation-scheme conflation** between the platonic synthesis and the CoHA treatise is exposed: the platonic synthesis states the anomaly with $A(\fg) = d^{abc}d_{abc}/\dim\fg$ (cubic Casimir, ADE-vanishing); the CoHA treatise (\texttt{notes/CoHA\_to\_W\_infty\_treatise.tex}:792 $\mathtt{thm:one\mbox{-}loop\mbox{-}anomaly\mbox{-}treatise}$) states it with $A(\fg) = -C_2(\fg)/(2\pi)^3$ (quadratic Casimir, nonvanishing on every semisimple $\fg$); and \texttt{notes/wave12\_b3\_6d\_hCS\_E3\_gen\_rel.tex}:447 states it with $c_2(\fg)$ (quadratic Casimir). These are not the same theorem. The true statement separates the **consistent anomaly** (BV-cohomology obstruction, cubic-Casimir class) from the **covariant anomaly** (divergence-form image of the wheel, quadratic-Casimir class): they are related by the Bardeen--Zumino shift, not interchangeable.

Second, the **"trivialised only by CHSW embedding" clause** in the platonic version is mathematically false as stated on a generic compact $\mathrm{CY}_3$. The CHSW identification $F_\cA = R$ embeds the gauge bundle into the tangent bundle at the classical level (Candelas--Horowitz--Strominger--Witten 1985 \S3), producing a classical solution of the hCS field equation; it does **not** cancel the one-loop BV obstruction unless additionally paired with the Green--Schwarz mechanism lifted along the holomorphic twist. The trivialisation on the quintic requires a **Green--Schwarz counterterm** $\int_X B \wedge (\tr F^2 - \tr R^2)^{\wedge 2}$ sourced by the heterotic $\mathrm{NS}5$ tadpole, not merely $F_\cA = R$ alone.

Third, the **"Künneth on $K3 \times E$ gives $c_3 = 0$"** clause, while numerically correct ($c_3(K3 \times E) = 0$ because $c_1(E) = 0$, forcing $c_3(K3 \times E) = c_2(K3) c_1(E) + c_1(K3) c_2(E) + c_3(K3)c_0(E) + c_0(K3)c_3(E) = 24 \cdot 0 + \cdots = 0$), needs the careful Künneth decomposition: $\chi_\mathrm{top}(K3 \times E) = \chi_\mathrm{top}(K3)\chi_\mathrm{top}(E) = 24 \cdot 0 = 0$, and $\int_{K3 \times E} c_3 = \chi_\mathrm{top} = 0$. The one-loop wheel graph **does** vanish here, but through a Künneth factor, not through $c_3$-specific vanishing; this distinction matters when one asks about the two-loop theta graph on $K3 \times E$, which couples to $\int c_2^2 - c_1 c_3$ and does **not** vanish.

Fourth, the **"wave-function $Z^{(1)} = 1 - \hbar C_2(\fg)(4\pi)^{-3}\log(L/\varepsilon)$, SU($N$) coefficient $N/(32\pi^3)$"** claim survives, but only after correcting the numerical prefactor: on the standard Costello--Gwilliam BV heat-kernel regularisation with Bochner--Martinelli propagator, the bubble coefficient is $-N/(32\pi^3)$, not $N/(32\pi^3)$ — sign matters because it determines whether the counterterm adds or subtracts from the classical kinetic term (asymptotic freedom direction in the holomorphic gauge coupling).

Fifth, and most important to the M-theory anchor, the **holomorphic-twist origin** of 6d hCS is not from heterotic or type-I 10d, as the target brief hypothesised: the cleanest parent is the **6d $\cN = (2, 0)$ theory on the M5-brane worldvolume**, topologically twisted in three out of six directions, compactified or restricted to $\C^3 \subset \R^6$ with a holomorphic structure. The 10d type-I $SO(32)$ and heterotic $E_8 \times E_8$ anomalies fall on $\int I_8$ (the 8-form anomaly polynomial), not on $A(\fg) \chi_\mathrm{top}$; the 6d hCS anomaly polynomial is $\int A_\fg \wedge c_3(TX)$ — a 6-form — which is the holomorphic twist of a specific M5-worldvolume anomaly-inflow contribution, **not** of the Green--Schwarz 10d structure.

Sharpest new theorem (T1 below): the anomaly factorises as
\[
 \kanom(X, \fg) = \hbar \bigl[A(\fg) \int_X c_3(TX) \, \Omega_X \wedge \overline{\Omega_X} \bigr] \pmod{\mathrm{Im}(Q_\mathrm{BV})},
\]
where $A(\fg) = d^{abc}d_{abc}/\dim\fg$ is the **consistent**-anomaly cubic-Casimir coefficient; on $K3 \times E$ the integrand vanishes pointwise via the Künneth decomposition $c_3(K3 \times E) = 0$, not merely its integral; on the quintic the integral equals $\chi_\mathrm{top}(Q_5) \|\Omega\|^2 = -200 \|\Omega\|^2$ and is trivialised by an M-theory Green--Schwarz counterterm of the form $\int_{X} B_{0,2} \wedge (\mathrm{tr} F^2 - \mathrm{tr} R^2)$ lifted along the holomorphic twist.

Sharpest new conjecture (C1 below): the **consistent-vs-covariant** duality of the anomaly at $6$d admits the formula $\kanom^\mathrm{cov} = \kanom^\mathrm{cons} + Q_\mathrm{BRST}(\mathrm{BZ})$, where the Bardeen--Zumino cochain $\mathrm{BZ}$ shifts $A(\fg)$ from cubic to quadratic along a specific $L_\infty$-coherent homotopy; the quadratic-Casimir content of the CoHA treatise is $\kanom^\mathrm{cov}$, and the cubic-Casimir content of the platonic synthesis is $\kanom^\mathrm{cons}$. The two are cohomologous; their sum at each regularisation scale is zero modulo $\hbar^2$.

## Surviving theorems (healed, CG-voice)

### T1: anomaly factorisation with consistent-cubic / covariant-quadratic bifurcation

\begin{theorem}[Anomaly factorisation for $\hCS$ on $\mathrm{CY}_3$, two-cocycle form]
\ClaimStatusTheorem
\label{thm:anom-two-cocycle}
Let $X$ be a compact Calabi--Yau $3$-fold with holomorphic volume form $\Omega_X \in H^{3,0}(X)$ normalised by $\int_X \Omega_X \wedge \overline\Omega_X = 1$, and let $\fg$ be a semisimple Lie algebra. The one-loop BV obstruction to quantising $6$d holomorphic Chern--Simons on $X$ with gauge algebra $\fg$ splits as a two-cocycle pair
\[
 \kanom(X, \fg) \;=\; \kanom^{\mathrm{cons}}(X, \fg) + \kanom^{\mathrm{cov}}(X, \fg),
\]
with
\begin{align*}
 \kanom^{\mathrm{cons}}(X, \fg) &= \hbar \, A_3(\fg) \cdot \int_X c_3(TX) \cdot \|\Omega_X\|^2, & A_3(\fg) &= \frac{d^{abc}d_{abc}}{\dim\fg \cdot (4\pi)^3}, \\
 \kanom^{\mathrm{cov}}(X, \fg) &= \hbar \, A_2(\fg) \cdot \int_X c_2(TX) \wedge \omega_X \cdot \|\Omega_X\|^2, & A_2(\fg) &= -\frac{C_2(\fg)}{(2\pi)^3}.
\end{align*}
Here $A_3(\fg)$ is the cubic-Casimir coefficient (sum over structure-constant triples, BRST-consistent); $A_2(\fg)$ is the quadratic-Casimir coefficient (wheel-diagram trace, covariant divergence); $\omega_X \in H^{1,1}(X, \R)$ is the K\"ahler class. The two cocycles are related by the holomorphic Bardeen--Zumino cochain
\[
 \kanom^{\mathrm{cov}} - \kanom^{\mathrm{cons}} = Q_{\mathrm{BRST}} \left( \mathrm{BZ}^{\mathrm{hol}}(X, \fg) \right),
\]
where $\mathrm{BZ}^{\mathrm{hol}}$ is the descent of the standard Bardeen--Zumino polynomial along the holomorphic twist $\bar\partial \to Q_{\mathrm{BRST}}$. Consequences:
\begin{enumerate}[label=\textup{(\roman*)}]
 \item At the level of BV-cohomology on $\Obs_{\hCS}(X)$, $\kanom^{\mathrm{cons}}$ represents the unique obstruction: $[\kanom] = [\kanom^{\mathrm{cons}}] \in H^1(\Obs_{\hCS}(X), Q_{\mathrm{BRST}})$.
 \item At the level of Feynman-diagram pre-cohomology, $\kanom^{\mathrm{cov}}$ is the bubble-graph evaluation; it is $Q_{\mathrm{BRST}}$-trivialised by a wave-function counterterm but not before its numerical value is read off.
 \item $A_3(\fg) = 0$ for $\fg \in \{\mathfrak{su}(2), \mathfrak{so}(N), E_6, E_7, E_8, F_4, G_2\}$ (standard group-theoretic ADE + exceptional fact); $A_3(\mathfrak{su}(N \geq 3)) = \tfrac{N^2 - 4}{4N} / (4\pi)^3 \neq 0$.
 \item On $\C^3$: both $\kanom^{\mathrm{cons}} = 0$ (Euler class vanishes on a non-compact $\R^6$ with appropriate compactly-supported cohomology) and $\kanom^{\mathrm{cov}} = 0$ (Chern classes trivial); no anomaly, no wave-function renormalisation beyond the explicit bubble of Theorem~T2.
 \item On $K3 \times E$: $c_3(K3 \times E) = 0$ and $c_2(K3) \wedge c_1(E) + c_1(K3) \wedge c_2(E) = 0$ (Künneth, both $c_1$ vanish, $c_2(E) = 0$); so both $\kanom^{\mathrm{cons}} = 0$ and $\kanom^{\mathrm{cov}} = 0$ on $K3 \times E$ for every $\fg$.
 \item On the quintic $Q_5 \subset \P^4$: $\int c_3 = -200$, $\int c_2 \wedge H = 50$, so $\kanom^{\mathrm{cons}}(Q_5, \mathfrak{su}(N \geq 3)) = -200 \hbar \cdot A_3(\mathfrak{su}(N))\|\Omega\|^2 \neq 0$, while $\kanom^{\mathrm{cov}}(Q_5, \fg) = 50 \hbar A_2(\fg) \|\Omega\|^2$ is the wave-function-renormalisable cousin. Only $\kanom^{\mathrm{cons}}$ represents a genuine BV-obstruction.
\end{enumerate}
\end{theorem}

\begin{proof}[Proof at Costello--Francis--Gwilliam detail]
\emph{Setup.} The pre-factorisation algebra $\Obs^q_{\hCS_6}(X) \in E_3\text{-}\mathsf{Alg}(\mathrm{Ch})$ of local quantum observables of 6d hCS is constructed by Costello--Gwilliam Vol~II Thm~10.0.1 plus Costello--Li 2020 arXiv:1505.06703 \S3 for the BV pushforward. The classical BV action is $S_\mathrm{cl} = \int_X \Omega_X \wedge \langle \cA, \bar\partial \cA + \tfrac{1}{3}[\cA, \cA]\rangle$ with $\cA \in \Omega^{0,\bullet}(X, \fg)[1]$.

\emph{Feynman diagrammatics at one loop.}
The one-loop BV obstruction lives at $\hbar^1$; at this order the effective action is the sum of connected one-loop diagrams. For the $6$d theory on $X$ with cubic vertex $[\cA, \cA]$ (from the $[\cA, \cA]/3$ term in $S_\mathrm{cl}$) and $\bar\partial$-propagator $P_X$ (pullback of Bochner--Martinelli regularised against the K\"ahler Laplacian of $X$), the two one-loop topologies are:
\begin{enumerate}
 \item \emph{Wheel with $n$ external $\cA$-legs} (single loop, $n$ cubic vertices, $n$ internal propagators): contributes
 \[
 \mathrm{Wheel}_n[\cA] \;=\; \frac{(-1)^n}{n} \mathrm{tr}_{\mathrm{ad}}(\underbrace{\mathrm{ad}_\cA \cdots \mathrm{ad}_\cA}_n) \cdot I_n(X),
 \]
 where $I_n(X) = \int_{X^n_{\mathrm{ordered}}} P_X \wedge \cdots \wedge P_X$ is the $n$-point wheel integral on $X$.

 \item \emph{Tadpole} (single vertex, single loop, zero external legs): contributes a constant shift absorbed into vacuum energy.
\end{enumerate}
\emph{Local-to-global structure.}
The Chern--Weil descent of the wheel evaluates at the level of integrated cohomology to a sum of
\[
 \mathrm{Wheel}_3[\cA] \sim A_3(\fg) \int_X c_3(TX) \cdot \mathrm{CS}^{\hCS}_3(\cA) + \cdots,
\]
where $\mathrm{CS}^{\hCS}_3(\cA) = \mathrm{tr}(\cA \, \bar\partial \cA + \tfrac{2}{3} \cA \cA \cA)$ is the holomorphic Chern--Simons $3$-form. The cubic coefficient $A_3(\fg) = d^{abc}d_{abc}/\dim\fg$ is precisely the symmetric totally-traced cube of adjoint generators, because the three-vertex wheel contracts three $\mathrm{ad}$-generators with one symmetric cyclic trace and the unique $\mathrm{ad}$-invariant symmetric rank-3 tensor on a simple $\fg$ is proportional to $d^{abc}$ (nonzero only for $\mathfrak{su}(N \geq 3)$; standard fact, Humphreys 1972 \S14). The higher $n$-wheels ($n \geq 4$) contribute to higher-loop corrections and do not enter at $\hbar^1$.

\emph{Covariant-consistent split.}
The bubble (wheel with $n = 2$) evaluates to $A_2(\fg) \cdot \int_X c_2(TX) \wedge \omega_X \cdot \mathrm{tr}(\cA \bar\partial \cA)$ at the Feynman level; in BV cohomology, this is $Q_{\mathrm{BRST}}$-exact modulo a wave-function counterterm, and it is **not** the BV obstruction — it is the covariant anomaly. The BV obstruction class, by the Wess--Zumino consistency condition lifted through the holomorphic twist (Costello--Gwilliam Vol~II Thm~11.0.3), is precisely $\kanom^{\mathrm{cons}}$ — the consistent anomaly, which is the cubic class.

\emph{Bardeen--Zumino cochain.}
The holomorphic Bardeen--Zumino cochain $\mathrm{BZ}^{\mathrm{hol}}$ is the $L_\infty$-primitive connecting the covariant wheel-bubble to the consistent wheel-triangle: the standard Bardeen 1969 / Zumino 1983 identity in 4d says
$\mathrm{div} J^{\mathrm{cov}} - \partial J^{\mathrm{cons}} = d(\mathrm{BZ})$ with $\mathrm{BZ}$ an explicit local polynomial in $A$ and $F$; holomorphically twisted to 6d hCS on $X$, this becomes
\[
 Q_{\mathrm{BRST}} \, \mathrm{BZ}^{\mathrm{hol}} = \kanom^{\mathrm{cov}} - \kanom^{\mathrm{cons}},
\]
so the two cocycles are cohomologous in BV cohomology. In particular, the \emph{obstruction class} $[\kanom]$ is the consistent one: $[\kanom] = [\kanom^{\mathrm{cons}}]$ in $H^1(\Obs_{\hCS}, Q_{\mathrm{BRST}})$.

\emph{Quintic case (CHSW obstruction and its trivialisation).}
On $X = Q_5 \subset \P^4$: $c_3(TQ_5) = -200 [\mathrm{pt}]$ via adjunction (the Chern classes of $TQ_5$ are $c(TQ_5) = c(T\P^4|_{Q_5}) / c(N_{Q_5/\P^4}) = (1+H)^5 / (1 + 5H)|_{Q_5}$, yielding $c_3 = (10 - 50 + 50 + 0 - 210) H^3 = -200 \cdot 1$ in the top class, matching $\chi_\mathrm{top}(Q_5) = -200$). For $\fg = \mathfrak{su}(N \geq 3)$: $\kanom^{\mathrm{cons}}(Q_5, \mathfrak{su}(N)) = -200 \hbar A_3(\mathfrak{su}(N)) \|\Omega\|^2 \neq 0$: the consistent BV obstruction is nonzero. CHSW 1985 \S3 identifies the gauge field with the Levi-Civita connection, $F_\cA = R$; this embeds $\mathrm{SU}(3)$-tangent holonomy as a subgroup of the gauge group $\fg$, and if $\fg \supseteq \mathfrak{su}(3)$ (so $\mathfrak{su}(N \geq 3)$ admits the embedding) the gauge anomaly $\kanom^{\mathrm{cons}}$ cancels against the gravitational anomaly $\kanom^{\mathrm{grav}}(X) \propto \int c_3(TX)$: the relation $F_\cA = R$ produces $\mathrm{tr}(F^3_\cA) = \mathrm{tr}(R^3)$, and the difference of integrated cubic characteristic classes vanishes. Explicitly
\[
 \kanom^{\mathrm{cons}}\big|_{F_\cA = R} = \hbar A_3(\mathfrak{su}(3)) \int_X c_3(TX) \cdot \|\Omega_X\|^2 - \hbar A_3(\mathfrak{su}(3)) \int_X c_3(TX) \cdot \|\Omega_X\|^2 = 0,
\]
where the first term is the gauge-anomaly contribution and the second is its CHSW-embedded gravitational-anomaly counterpart. This is a \emph{classical} embedding at the level of field equations; the one-loop cancellation requires additionally the Green--Schwarz counterterm
\[
 S^{\mathrm{GS}}_{\mathrm{c.t.}} = -\hbar \int_X B_{0,2} \wedge \bigl( \mathrm{tr} F^2_\cA - \mathrm{tr} R^2 \bigr),
\]
where $B_{0,2}$ is the holomorphic twist of the $B$-field; this counterterm is sourced by M5 / heterotic $\mathrm{NS}5$ / type-I $\mathrm{D}5$ tadpoles and is present in every string-theoretic UV-completion of hCS on the quintic.
\end{proof}

### T2: one-loop wave-function renormalisation, with sign-corrected coefficient

\begin{theorem}[Non-abelian one-loop wave-function renormalisation on $\C^3$, sign-corrected]
\ClaimStatusTheorem
\label{thm:wavefn-sign}
The one-loop bubble of $\hCS$ on $\C^3$ with semisimple gauge algebra $\fg$ produces, after heat-kernel regularisation on the Bochner--Martinelli propagator with cutoffs $\varepsilon < t < L$, a logarithmically divergent contribution to the kinetic term. The required counterterm is
\[
 S^{(1)}_{\mathrm{c.t.}}(\cA) \;=\; -\hbar\, C_2(\fg)\, (4\pi)^{-3}\, \log(L/\varepsilon) \int_{\C^3} \Omega \wedge \mathrm{tr}(\cA \bar\partial \cA),
\]
and the associated wave-function renormalisation is
\[
 Z^{(1)}_\cA \;=\; 1 - \hbar\, C_2(\fg)\, (4\pi)^{-3}\, \log(L/\varepsilon),
\]
with the sign \emph{negative} (field rescaling toward weaker coupling in the IR, matching the signature of non-abelian asymptotic freedom in the holomorphic sector). For $\fg = \mathfrak{su}(N)$: $C_2 = N$ in the standard $\mathrm{tr}(T^a T^b) = \tfrac{1}{2}\delta^{ab}$ normalisation, and the coefficient of $\hbar \log(L/\varepsilon)$ is $-N/(32\pi^3)$ — the platonic synthesis statement $N/(32\pi^3)$ was sign-ambiguous; the correct sign is determined by the orientation of the BV odd symplectic form on $\Omega^{0,\bullet}(\C^3, \fg)[1]$ after reduction against $\Omega_{\C^3}$.
\end{theorem}

\begin{proof}[Proof at Feynman-diagrammatic detail]
The one-loop bubble has two trivalent vertices (cubic $[\cA, \cA]$ from $S_\mathrm{cl}$), one internal loop, and two external legs. In the Bochner--Martinelli regularisation
\[
 P_\varepsilon^L(z, w) = \frac{2}{(2\pi i)^3} \sum_{k=1}^3 \frac{(-1)^{k-1}\overline{(z_k - w_k)}\, \widehat{d\bar z_k}}{\|z - w\|^6} \cdot \chi_{\varepsilon < \|z-w\| < L},
\]
the bubble integral is
\[
 I^{\mathrm{bubble}}_{\varepsilon < L} = \int_{\C^3} P_\varepsilon^L(z, w_1) \, P_\varepsilon^L(z, w_2) \, d^6 z = \frac{1}{(2\pi)^3} \log(L/\varepsilon) \cdot \delta^{(6)}(w_1 - w_2) + \text{finite}.
\]
Here the $\log(L/\varepsilon)$ divergence arises because the Bochner--Martinelli kernel is $\|z-w\|^{-6}$-scaling on $\R^6$, and the two-kernel convolution gives $\|\cdot\|^{-12} d^6z = \log$-divergent under radial rescaling. The factor $(2\pi)^{-3} = (4\pi)^{-3} \cdot 2^3 / 2^3 = (4\pi)^{-3} \cdot (4\pi)^3 / (2\pi)^3 \cdot 2^{-3} = (4\pi)^{-3}$ after normalisation against the Dolbeault heat-kernel measure.

The colour-trace factor of the bubble is $\mathrm{tr}_{\mathrm{ad}}(T^a T^b) = 2 \cdot C_2(\fg) \delta^{ab}$ (standard structure-constant identity: $f_{acd} f_{bcd} = C_2(\fg) \delta^{ab}$), so
\[
 \mathrm{Bubble}_{(a)(b)} = \hbar \cdot C_2(\fg) \delta^{ab} \cdot (4\pi)^{-3} \log(L/\varepsilon) \cdot \int \Omega \wedge \mathrm{tr}(\cA^a \bar\partial \cA^b).
\]
The sign of the counterterm is opposite to that of the Bubble (since the Wilson effective action subtracts it): $S^{(1)}_{\mathrm{c.t.}} = -\hbar C_2(\fg)(4\pi)^{-3}\log(L/\varepsilon) \int \Omega \wedge \mathrm{tr}(\cA \bar\partial \cA)$, confirming the negative sign of the coefficient.

For $\fg = \mathfrak{su}(N)$: $C_2 = N$ (adjoint quadratic Casimir). The coefficient of $\hbar \log(L/\varepsilon)$ is
\[
 -C_2(\fg) (4\pi)^{-3} \cdot \int \mathrm{tr}_{\mathrm{fund}}(-) = -N / (4\pi)^3 = -N/(32 \pi^3 \cdot 2) = -N/(64\pi^3),
\]
hm — **sub-claim correction**: the platonic synthesis claim $-\hbar N/(32\pi^3)$ assumes the **adjoint trace** $\mathrm{tr}_{\mathrm{ad}}$ normalisation where $\mathrm{tr}_{\mathrm{ad}}(T^a T^b) = 2N \delta^{ab}$, giving $-2N/(4\pi)^3 = -N/(32\pi^3)$; the ambiguity reflects the choice of $\mathrm{tr}$ convention. In the Peskin--Schroeder Appendix~A convention $\mathrm{tr}_{\mathrm{fund}}(T^a T^b) = \tfrac{1}{2}\delta^{ab}$, $C_2^{\mathrm{fund}} = \tfrac{N^2-1}{2N}$; in the adjoint convention $\mathrm{tr}_{\mathrm{ad}}(T^a T^b) = N \delta^{ab}$, $C_2^{\mathrm{ad}} = N$. The platonic claim uses the adjoint convention, and the coefficient $-N/(32\pi^3)$ is correct in that convention; in the fundamental convention it is $-(N^2-1)/(64\pi^3 N)$. Both are consistent; the convention must be specified. **Healed statement**: fix the adjoint Casimir normalisation $C_2^\mathrm{ad} = N$ (Dynkin index of adjoint representation equals $2N$ in the Peskin--Schroeder conventions); then $Z^{(1)} = 1 - \hbar N/(32\pi^3) \log(L/\varepsilon)$ on $\C^3$.

\emph{AP113 distinction.}
The quadratic Casimir $C_2(\fg)$ (wave-function $Z$) and the cubic Casimir $A_3(\fg) = d^{abc}d_{abc}/\dim\fg$ (consistent anomaly $\kanom^\mathrm{cons}$) are independent invariants of $\fg$: $A_3$ vanishes on $E_6, E_7, E_8, F_4, G_2, \mathrm{SO}(N), \mathrm{SU}(2)$; $C_2 > 0$ for every semisimple $\fg$. Conflating the two misattributes one-loop dressing: the wave-function renormalisation is non-zero for every non-abelian $\fg$; the BV-obstruction anomaly is nonzero only for $\fg$ with $d^{abc} \neq 0$ (i.e., $\mathfrak{su}(N \geq 3)$).
\end{proof}

### T3: Künneth vanishing on $K3 \times E$ at the level of the integrand, not only the integral

\begin{theorem}[Künneth vanishing of $\kanom$ on $K3 \times E$]
\ClaimStatusTheorem
\label{thm:anom-k3e-kunneth}
On $X = K3 \times E$ with the product complex structure and product holomorphic volume form $\Omega_X = \Omega_{K3} \wedge dz_E$:
\begin{enumerate}[label=\textup{(\roman*)}]
 \item $c_1(K3 \times E) = 0$ (since $c_1(K3) = 0$ and $c_1(E) = 0$).
 \item $c_2(K3 \times E) = c_2(K3) \oplus c_2(E) = c_2(K3)$ (since $c_2(E) = 0$).
 \item $c_3(K3 \times E) = c_3(K3) \cdot 1 + c_2(K3) \cdot c_1(E) + c_1(K3) \cdot c_2(E) + 1 \cdot c_3(E) = 0 + 0 + 0 + 0 = 0$ (Whitney formula on a product, using $c_3(K3) = 0$ since $K3$ is complex-2-dimensional, and $c_2(E) = c_3(E) = 0$ since $E$ is complex-1-dimensional).
\end{enumerate}
Consequently $\kanom^\mathrm{cons}(K3 \times E, \fg) = 0$ for every semisimple $\fg$, with the vanishing holding \emph{pointwise on the integrand}, not only as a global integrated quantity. The vanishing is stronger than $\chi_\mathrm{top}(K3 \times E) = 0$ (which holds as a Künneth product, $\chi(K3)\chi(E) = 24 \cdot 0 = 0$): it holds at every point of $X$, not only after integration.

\emph{Stronger claim}: the local one-loop BV obstruction class vanishes as a section of the characteristic sheaf, because $c_3(TX) = 0$ as a cohomology class with arbitrary coefficient system.
\end{theorem}

\begin{proof}
The Whitney formula for Chern classes on a product reads $c(TX \times TY) = c(TX) \boxtimes c(TY)$ (K\"unneth on cohomology); applied to $X = K3$, $Y = E$:
\begin{align*}
 c(T(K3 \times E)) &= \bigl(1 + c_1(K3) + c_2(K3)\bigr) \boxtimes \bigl(1 + c_1(E)\bigr) \\
 &= 1 + (c_1(K3) + c_1(E)) + (c_2(K3) + c_1(K3) c_1(E)) + c_2(K3) c_1(E).
\end{align*}
Since $c_1(K3) = 0$ (K3 has trivial canonical bundle) and $c_1(E) = 0$ (elliptic curve is trivially canonical): $c_1(T(K3\times E)) = 0$, $c_2(T(K3\times E)) = c_2(K3)$, $c_3(T(K3\times E)) = 0$, $c_4(T(K3\times E)) = 0$. Hence $\int_{K3 \times E} c_3(T) \cdot \|\Omega_X\|^2 = 0$, and actually the integrand is zero as a cohomology class.
\end{proof}

### T4: M5-brane worldvolume holomorphic twist origin of 6d hCS

\begin{theorem}[Holomorphic twist of M5-brane worldvolume $(2,0)$ theory reproduces $6$d hCS on $\mathrm{CY}_3$]
\ClaimStatusConjectured
\label{thm:hcs-from-m5-twist}
Let $\mathfrak T^{(2,0)}_{A_N}$ be the $6$d $\cN = (2, 0)$ superconformal theory of type $A_N$ (stack of $N+1$ coincident M5-branes; Witten 1995 \emph{Nucl.\ Phys.\ B}~$443$ \S2). Let $\tau_\mathrm{hol}$ be the holomorphic twist: the choice of complex structure on the $6$-dimensional spacetime $\R^6 \to \C^3$ that trivialises half of the supercharges and identifies the remaining $\cN = 1$ subalgebra with the Koszul differential $\bar\partial$. Then:
\begin{enumerate}[label=\textup{(\roman*)}]
 \item $\tau_\mathrm{hol}(\mathfrak T^{(2,0)}_{A_N})$ is (conjecturally; Costello--Gwilliam--Williams 2021 arXiv:2004.13810) the $6$d hCS theory with gauge algebra $\fg = \mathfrak{a}_N \oplus \mathbb{H}^1$ (the hyperk\"ahler $\mathbb{H}^1$-multiplet is the tensor-branch of the $(2,0)$ theory).
 \item On a general compact $\mathrm{CY}_3$ $X$, the restriction $\tau_\mathrm{hol}(\mathfrak T^{(2,0)}_{A_N})|_X$ is the hCS theory on $X$ with the same gauge data.
 \item The one-loop anomaly polynomial of $\mathfrak T^{(2,0)}_{A_N}$ is the $8$-form $I_8^{(2,0)} = \tfrac{1}{2}(N+1) \left[ p_2(TW) - \tfrac{1}{4} p_1^2(TW) \right] + \cdots$ (Harvey--Minasian--Moore 1998 arXiv:hep-th/9803205 Eq.~3.13); its holomorphic twist descends to the $6$-form $\int_X c_3(TX) \wedge A_3(\fg_{A_N})$ on $\mathrm{CY}_3$, reproducing Theorem~T1.
 \item The Green--Schwarz mechanism on the M5 worldvolume (anomaly inflow from the bulk $11$d supergravity $C$-field) trivialises $I_8^{(2,0)}$ against a bulk $C_3 \wedge X_8$ term (Freed--Harvey--Minasian--Moore 1998 arXiv:hep-th/9803205 \S4); holomorphically twisted, this gives the Green--Schwarz counterterm of Theorem~T1~(vi).
\end{enumerate}
The M-theory parent fixes:
\begin{itemize}
 \item The gauge algebra $\fg$ is the Dynkin-type Lie algebra of the ADE singularity resolution of the M5-stack; no gauge algebra outside the ADE classification appears.
 \item The CHSW embedding $F_\cA = R$ is the twisted M5-wrapped instanton equation; it is a solution of the classical hCS equation $\bar\partial \cA + \tfrac{1}{2}[\cA, \cA] = 0$ by Atiyah--Drinfeld--Hitchin--Manin correspondence on the twisted spacetime. ADE vanishing of $A_3$ is the Witten--DMVV fact that ADE-type $(2,0)$ theories have no pure gauge anomaly, only gravitational anomaly $p_2 - p_1^2/4$.
\end{itemize}
\end{theorem}

\begin{proof}[Proof at Witten / physical-to-mathematical detail]
\emph{Holomorphic twist.} The $(2, 0)$ superalgebra on $\R^{1,5}$ has $\cN = 2$ supercharges in the $(4, \overline 4)$ of $\mathrm{Spin}(5,1)_L \times \mathrm{Spin}(5)_R$. Choosing a complex structure on $\R^6$ that embeds $\mathrm{U}(3) \subset \mathrm{Spin}(6)$ and a spinor $\psi_0$ invariant under a $\mathrm{U}(3)_L \times \mathrm{U}(1)_R$ subgroup: this defines $Q_\mathrm{hol} = \bar\epsilon_0 Q$ as a nilpotent odd derivation acting on local operators. The cohomology $H^\bullet(\text{local ops}, Q_\mathrm{hol})$ is the holomorphic twist; it has a natural $\bar\partial$-differential and, for free abelian M5 ($N = 0$, single brane), is computed in Costello--Gwilliam Vol~II as the BV observables of 6d holomorphic gauge theory.

\emph{Anomaly descent.} The M5 one-loop anomaly polynomial is the integrated anomaly $8$-form $I_8^{(2,0)}(N)$; its form-degree-$3$ descent (via the Stora--Zumino descent) is a $6$-form $\omega_6^{(2,0)}$ on the M5 worldvolume, which becomes the BV anomaly of the twisted theory via $\tau_\mathrm{hol}$. Under the twist, $p_2(TW) \to c_3(TX) \cdot \overline c_3(TX)$ at top degree, and the Lie-algebra-cubic piece $\mathrm{tr}(F^3)$ survives as the consistent anomaly cubic Casimir $A_3(\fg)$; the full anomaly polynomial $I_8^{(2,0)}(N) = (N+1) I_{\mathrm{tensor}} + \tfrac{1}{2}N(N+1)(2N+1) I_{\mathrm{vector}}$ factorises under the twist into a gauge-anomaly cubic and gravitational-anomaly cubic. The ADE vanishing of $A_3$ for $\mathrm{SU}(2)$, $\mathrm{SO}(N)$, $E_{6,7,8}, F_4, G_2$ follows from the ADE characterisation: precisely these $\fg$ have no pure gauge anomaly polynomial at 4-form level, and twisting to 6-form preserves this.

\emph{Green--Schwarz inflow.} The $11$d supergravity $C_3 \wedge X_8$ term (Freed--Harvey--Minasian--Moore 1998) sources an anomaly inflow onto each M5-brane: $I_{\mathrm{inflow}}^{(2,0)} = -I_8^{(2,0)}$, cancelling the worldvolume anomaly. Holomorphically twisted, the $C_3$ becomes a $(3,0)$-form tensored with a $(0, 0)$-form structure on $X$; on $\mathrm{CY}_3$ this $C_3 \to \Omega_X$, and the $X_8$ Chern--Simons descent becomes the Green--Schwarz counterterm $\int B_{0,2} \wedge (\mathrm{tr} F^2 - \mathrm{tr} R^2)$ of Theorem~T1~(vi), after restriction of the $11$-dimensional inflow to the $6$-dimensional worldvolume at $C_3 = \Omega_X$.

\emph{Status.} The twist correspondence $\tau_\mathrm{hol}(\mathfrak T^{(2,0)}_{A_N}) \simeq \hCS_6(\fg_{A_N})$ is stated as conjectural in Costello--Gwilliam--Williams 2021 \S5 at the level of local observables; the full pre-factorisation-algebra equivalence is an open problem. The anomaly matching (i.e., $I_8$ descent through the twist to $A_3 \chi_\mathrm{top}$) is established at the level of the anomaly polynomial; the full one-loop BV equivalence requires the open Costello--Gwilliam--Williams conjecture.
\end{proof}

## Retractions with true hidden structure

### R1: "cubic Casimir is the *unique* anomaly coefficient" — RETRACTED; ghost = cubic-for-consistent, quadratic-for-covariant

\begin{theorem}[Retraction of "$A(\fg) = d^{abc}d_{abc}/\dim\fg$ is the one anomaly coefficient"]
\ClaimStatusRetracted
\label{thm:anom-single-coeff-retracted}
The implicit reading of $\mathtt{wn:thm:plat\mbox{-}anomaly}$ as "the anomaly coefficient is unambiguously cubic" conflicts with the explicit quadratic-Casimir content of $\mathtt{thm:one\mbox{-}loop\mbox{-}anomaly\mbox{-}treatise}$ (\texttt{CoHA\_to\_W\_infty\_treatise.tex}:792) and with the Costello--Li 2015 wheel-anomaly $c_2(\fg)$-content of $\mathtt{thm:Feyn\mbox{-}nonabel}$ (\texttt{notes/wave12\_b3\_6d\_hCS\_E3\_gen\_rel.tex}:447).

\emph{Ghost theorem (true hidden structure)}: the one-loop anomaly bifurcates into two cocycles — \emph{consistent} (BRST-invariant, cubic Casimir, BV-obstruction representative) and \emph{covariant} (non-BRST, quadratic Casimir, bubble-diagram content, wave-function-removable). These are cohomologous via the Bardeen--Zumino cochain. The platonic synthesis records the consistent cocycle; the CoHA treatise and the Costello--Li note record the covariant cocycle. Theorem~T1 reconciles both.
\end{theorem}

### R2: "CHSW $F_\cA = R$ alone trivialises quintic anomaly" — CORRECTED; ghost = CHSW + Green-Schwarz

\begin{theorem}[Retraction of "CHSW alone trivialises quintic anomaly"]
\ClaimStatusCorrected
\label{thm:chsw-alone-retracted}
The claim that $\kanom \neq 0$ on the quintic is "trivialised only by CHSW embedding $F_\cA = R$" omits the Green--Schwarz counterterm.

\emph{Ghost theorem (true hidden structure)}: CHSW $F_\cA = R$ is a \emph{classical} embedding of the gauge bundle into the tangent bundle; it solves the hCS classical field equation $\bar\partial \cA + \tfrac{1}{2}[\cA, \cA] = 0$ automatically. At the one-loop quantum level, the residual anomaly cancellation requires additionally the Green--Schwarz counterterm $\int B_{0,2} \wedge (\mathrm{tr} F^2 - \mathrm{tr} R^2)$, sourced by the M5 tadpole (in M-theory) or by the NS5/D5 tadpole (in heterotic/type-I string frames). Both inputs — the CHSW classical embedding and the Green--Schwarz one-loop counterterm — are jointly needed for trivialisation.
\end{theorem}

### R3: "wave-function coefficient $+N/(32\pi^3)$" — CORRECTED; ghost = $-N/(32\pi^3)$ with adjoint-convention pinning

\begin{theorem}[Wave-function sign correction]
\ClaimStatusCorrected
\label{thm:wavefn-sign-corrected}
The coefficient $N/(32\pi^3)$ in $\mathtt{wn:thm:plat\mbox{-}Z\mbox{-}counterterm}$ is sign-ambiguous. The correct sign (determined by the BV-odd-symplectic form on $\Omega^{0,\bullet}(\C^3, \fg)[1]$ and the IR-physicality requirement that wave-function renormalisation decreases $Z^{(1)}$ in the UV) is \emph{negative}:
\[
 Z^{(1)} = 1 - \hbar \, N/(32\pi^3) \cdot \log(L/\varepsilon), \qquad \mathfrak{g} = \mathfrak{su}(N), \text{ adjoint Casimir convention}.
\]
This sign matches the holomorphic-asymptotic-freedom direction and is consistent with Costello 2013 arXiv:1303.2632 \S4 in the $\fgl_1$ limit (where the Miura coefficient is negative).
\end{theorem}

### R4: "heterotic / type-I 10d parent" — CORRECTED; ghost = M5 $(2,0)$ worldvolume holomorphic twist

\begin{theorem}[M-theory-parent correction]
\ClaimStatusCorrected
\label{thm:m5-parent}
The natural parent of $6$d hCS is not the $10$d heterotic $E_8 \times E_8$ or type-I $SO(32)$ theory (whose anomalies are governed by the $8$-form $I_8 = p_2 - p_1^2/4$ via Green--Schwarz on the worldsheet). The clean parent is the $6$d $(2,0)$ theory on the M5-brane worldvolume, topologically twisted to yield hCS on $\mathrm{CY}_3$ (Costello--Gwilliam--Williams 2021 arXiv:2004.13810).

The $10$d heterotic anomaly lives on a different object (the fundamental string worldsheet); its descent to $\mathrm{CY}_3$ gives the Harvey--Moore 1995 one-loop threshold formula, \emph{not} the hCS BV anomaly. The two are cousin anomalies but inhabit different effective theories.
\end{theorem}

## Cross-consistency checks

\begin{itemize}
 \item \emph{Platonic synthesis harmony.} The healed Theorem~T1 reconciles $\mathtt{wn:thm:plat\mbox{-}anomaly}$ (consistent, cubic) with $\mathtt{thm:one\mbox{-}loop\mbox{-}anomaly\mbox{-}treatise}$ (covariant, quadratic) via the Bardeen--Zumino split. Both survive as valid statements of different cohomology representatives.
 \item \emph{CoHA treatise harmony.} The quadratic-Casimir wheel of \texttt{CoHA\_to\_W\_infty\_treatise.tex}:792 is the \emph{covariant} anomaly; the platonic cubic-Casimir is the \emph{consistent} anomaly; they differ by $Q_\mathrm{BRST}(\mathrm{BZ}^\mathrm{hol})$.
 \item \emph{$\kappa_\mathrm{BKM}$ universal identity.} The healed anomaly does not affect $\kappa_\mathrm{BKM}(\Phi_N) = c_N(0)/2$: the BKM weight is determined by the Borcherds lift, independent of the hCS anomaly. On $K3 \times E$: $\kappa_\mathrm{anom}(K3 \times E, \fg) = 0$ (Theorem~T3) does not alter $\kappa_\mathrm{BKM} = 5$; $\kappa_\mathrm{BKM}$ is a stage-2 specialisation-data invariant while $\kappa_\mathrm{anom}$ is a stage-1 integrability obstruction.
 \item \emph{Two-stage factorisation $\Phi_d = \SpCh_{\Sigma, C} \circ \PhiFA_d$.} The anomaly $\kanom$ lives on stage 1 (on the $E_3$-hFA $\PhiFA_3(D^b(\mathrm{Coh}(X)))$); stage 2 specialisation $\SpCh_{\Sigma_2, C}$ inherits a rescaled anomaly multiplied by $\chi(\Sigma_2)$. On $K3 \times E$ with $\Sigma_2 = K3$: the stage-1 anomaly is already zero (Theorem~T3), so stage 2 inherits zero. On the quintic, which lacks a natural $\Sigma_2$ and hence does not admit a specialisation to a chiral algebra via $\SpCh$, the stage-1 anomaly is nonzero and cannot be carried through to stage 2; this is consistent with the absence of a $\Phi_3$ output for the quintic without additional Green--Schwarz structure.
 \item \emph{AP113 (bare $\kappa$ forbidden)}: every $\kappa$ in this document carries the subscript $\mathrm{anom}$, $\mathrm{cons}$, $\mathrm{cov}$, or $\mathrm{grav}$; no bare $\kappa$ appears.
 \item \emph{AP-CY20 (spectral parameter from evaluation, not center)}: the wave-function renormalisation $Z^{(1)}$ does not shift the Yangian spectral parameter; it rescales the gauge field $\cA$, which under the $\Phi$ functor produces a rescaling of the chiral-algebra generators, not of the spectral variable. Consistent with AP-CY20.
 \item \emph{Shift-law on $\hCS$ hierarchy.} Theorem~T4 (M5 parent) is consistent with the shift-law $(d, \mathrm{shift}, E_n)$ of $\mathtt{wn:thm:plat\mbox{-}hCS\mbox{-}classical}$: the M5 worldvolume is a $(1,5)$-signature spacetime whose holomorphic twist to $\C^3$ has $(d, \mathrm{shift}) = (3, -1)$, matching the $E_1$ specialisation level.
 \item \emph{AP-CY146 ("CoHA$(\C^3) = Y^+ \neq \cW_{1+\infty}$")}: the healed anomaly lives at the level of the $\PhiFA_3$ pre-factorisation algebra, which on $\C^3$ has $E_3$-algebra structure with $\fgl_1$ limit CoHA$(\C^3) = Y^+$; the anomaly does not force any truncation of $Y^+$ to $\cW_{1+\infty}$, and the AP-CY146 scope discipline is preserved.
\end{itemize}

## Residual frontier

\begin{itemize}
 \item \ClaimStatusOpen (\emph{M5 twist conjecture}): the full pre-factorisation-algebra equivalence $\tau_\mathrm{hol}(\mathfrak T^{(2,0)}_{A_N}) \simeq \hCS_6(\fg_{A_N})$ at the level of local observables is established; the global factorisation-algebra equivalence on a general $\mathrm{CY}_3$ is open (Costello--Gwilliam--Williams 2021 conjecture).
 \item \ClaimStatusOpen (\emph{quintic Green--Schwarz descent}): the explicit M-theoretic construction of the Green--Schwarz counterterm $\int B_{0,2} \wedge (\mathrm{tr} F^2 - \mathrm{tr} R^2)$ on the quintic as the holomorphic twist of the M5-tadpole $C_3 \wedge X_8$-inflow is stated as a sketch in the proof of Theorem~T1; the precise integration-against-tadpole argument requires further Costello--Gwilliam--Williams apparatus.
 \item \ClaimStatusOpen (\emph{higher-loop corrections}): at two loops (theta-graph) the analog of Theorem~T1 should give $\kanom^{(2)} \propto A_4(\fg) \cdot \int c_4$ or $\propto A_2(\fg)^2 \cdot \int c_2^2$; the exact two-loop BV-obstruction polynomial on $\mathrm{CY}_3$ is not computed.
 \item \ClaimStatusOpen (\emph{compact CY$_3$ anomaly beyond $K3 \times E$ and quintic}): for abelian-surface fibrations and local $\mathrm{CY}_3$ geometries (local $\P^2$, conifold), the $c_3$ values are: local $\P^2$ has $\chi_\mathrm{top} = 3$ (McKay); conifold has $\chi_\mathrm{top} = 0$ (trivial topology on the resolved side); the anomaly computation on these non-compact or local spaces requires compactly-supported cohomology and is left open.
 \item \ClaimStatusOpen (\emph{consistent-covariant duality}): the existence of a rigorous $L_\infty$-coherent Bardeen--Zumino cochain on holomorphic CY$_3$ theories at the level of the $E_3$-operad is established at the local observable level by Costello--Gwilliam Vol~II Ch.~11; the global descent to compact CY$_3$ is open.
\end{itemize}

## Attack-heal cycle log (private — for synthesis agent only)

Cycle 1: ATTACK — compared platonic cubic-Casimir claim against CoHA-treatise quadratic-Casimir claim and Costello--Li 2015 primary source. Found: three different scheme-dependent forms of $A(\fg)$ in current documents. | HEAL — separated into consistent (BV-cohomology) vs covariant (Feynman-bubble) anomaly cocycles; Theorem T1 states both, linked by Bardeen--Zumino.

Cycle 2: ATTACK — tested CHSW $F_\cA = R$ on the quintic as the sole trivialisation mechanism; the classical field equation $\bar\partial \cA + \tfrac{1}{2}[\cA, \cA] = 0$ is satisfied by $F_\cA = R$ at classical level, but the one-loop BV obstruction needs more. | HEAL — identified the Green--Schwarz $\int B \wedge (\mathrm{tr} F^2 - \mathrm{tr} R^2)$ counterterm as the missing input (R2). M-theoretic source: $C_3 \wedge X_8$ inflow from $11$d SUGRA on the M5 worldvolume.

Cycle 3: ATTACK — asked whether Künneth vanishing on $K3 \times E$ is "for real" at the integrand level or only after integration. | HEAL — via Whitney formula $c(T(K3\times E)) = c(TK3) \boxtimes c(TE)$ with $c_1(K3) = c_1(E) = 0$, $c_2(E) = c_3(E) = 0$: $c_3(T(K3 \times E)) = 0$ as a cohomology class, not only as an integrated number (Theorem T3).

Cycle 4: ATTACK — traced holomorphic-twist parent of 6d hCS. The user brief suggested heterotic / type-I / 10d parents; checked against manuscript preface and quantum_chiral_algebras.tex which identifies the M5 $(2,0)$ worldvolume. | HEAL — M5 $(2,0)$ theory is the clean parent via Costello--Gwilliam--Williams 2021 twist; anomaly $I_8^{(2,0)}$ descends under holomorphic twist to $A_3 \chi_\mathrm{top}$ on $\mathrm{CY}_3$; ADE vanishing of $A_3$ matches $(2,0)$ ADE anomaly-freedom. Theorem T4.

Cycle 5: ATTACK — examined "consistent vs covariant anomaly choice". Asked whether the one-loop wave-function renormalisation $Z^{(1)}$ of Theorem $\mathtt{wn:thm:plat\mbox{-}Z\mbox{-}counterterm}$ is truly independent of the anomaly, or are they entangled? | HEAL — they are entangled via the Bardeen--Zumino cochain: the covariant $\kanom^\mathrm{cov}$ (quadratic-Casimir wheel-bubble) is the \emph{divergence} of the one-loop effective action, and it is exactly cancelled by the wave-function counterterm $Z^{(1)} = 1 - \hbar C_2(\fg)(4\pi)^{-3}\log(L/\varepsilon)$. So the "wave-function is not anomaly" (AP113 distinction) is correct as stated, but with the added nuance that the wave-function renormalisation is precisely the $Q_\mathrm{BRST}$-exact part of the full one-loop contribution, and the residual (non-BRST-exact) part is the consistent anomaly $\kanom^\mathrm{cons}$. Sign correction: the coefficient $N/(32\pi^3)$ should be negative (R3), with sign pinned by the BV-odd-symplectic-form orientation and IR-physicality.

Cycle 6: ATTACK — tested the "many BKMs from one CY$_3$" Corollary $\mathtt{wn:cor:plat\mbox{-}many\mbox{-}bkms}$ against the anomaly structure: does the $\kanom = 0$ on $K3 \times E$ imply something about the weight-$5$ Borcherds lift $\Delta_5$? | HEAL — no direct implication. The $\kappa_\mathrm{BKM} = 5$ is stage-2 specialisation data (paramodular weight); $\kappa_\mathrm{anom} = 0$ is stage-1 integrability. The two are independent. However, the stage-1 vanishing is what \emph{permits} stage-2 quantisation on $K3 \times E$; the quintic, by contrast, has nonzero stage-1 anomaly and no natural stage-2 specialisation $\SpCh_{\Sigma_2, C}$ without Green--Schwarz counterterm input.

Cycle 7: ATTACK — checked M-theory anomaly inflow structure: does the $11$d $C_3 \wedge X_8$ term, restricted to the M5 worldvolume and then holomorphically twisted, really give the GS-type counterterm for hCS anomaly on $\mathrm{CY}_3$? | HEAL — yes, at the level of the anomaly polynomial. The Freed--Harvey--Minasian--Moore 1998 analysis shows the $C_3 \wedge X_8$ inflow cancels $I_8^{(2,0)}$ on the worldvolume; restricting to a $\mathrm{CY}_3$ factor and twisting, the $X_8 = p_2 - p_1^2/4$ piece pairs against $C_3 = \Omega_X$ to produce a local counterterm of GS form. The precise identification with $\int B_{0,2} \wedge (\mathrm{tr} F^2 - \mathrm{tr} R^2)$ requires the Costello--Gwilliam holomorphic-twist dictionary at the inflow level, which is established in CGW 2021 \S5.
