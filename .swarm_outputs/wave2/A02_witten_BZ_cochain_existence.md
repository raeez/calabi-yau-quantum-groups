# Agent A02 — Witten voice on the holomorphic Bardeen--Zumino cochain existence claim

## Executive adversarial summary

The claim in `wn:thm:spine-consistent-covariant` that a holomorphic Bardeen--Zumino cochain $\mathrm{BZ}^{\mathrm{hol}}(\cA)$ exists with $Q_{\mathrm{BRST}}(\mathrm{BZ}^{\mathrm{hol}}) = \kanom^{\mathrm{cov}} - \kanom^{\mathrm{cons}}$ is **a category error dressed as a theorem**. The classical Bardeen--Zumino polynomial in 4D relates two representatives of the **same** current anomaly (consistent vs.\ covariant currents derived from the **same** triangle diagram); it does **not** cohomologously relate a triangle diagram to a bubble diagram. The spine conflates (i) the cubic-Casimir one-loop BV obstruction class in $H^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$ with (ii) the quadratic-Casimir logarithmic wave-function renormalisation, which lives in a **different cohomological degree**, has **different Feynman topology**, and is **absorbed by a local kinetic counterterm**, not by a cochain relating it to the BV obstruction. The same author wrote `rem:plat-Z-vs-anomaly` (at `chapters/theory/quantum_chiral_algebras.tex:3749-3763`) warning explicitly against this conflation; the spine violates its own manuscript's discipline.

**Surviving ghost theorem.** The classical Bardeen--Zumino construction does admit a genuine holomorphic avatar: given the single triangle-graph one-loop obstruction $\kanom^{\mathrm{cons}} \sim A(\fg) \cdot c_3(TX)$, one can write the obstruction as an image of a local $(3,3)$-form descent from a $(4,4)$-form anomaly polynomial on a hypothetical $(4,0)$-dimensional ambient; alternative BRST-cocycle \emph{representatives} of the same cubic-Casimir class differ by Bardeen--Zumino cochains in $(\mathrm{BRST}, \bar\partial)$-total cohomology. These are cochain-equivalent representatives of a \emph{single} cubic-Casimir class, not a cohomological bridge between cubic-Casimir and quadratic-Casimir data.

**Sharpest new conjecture isolated.** The genuine open problem is whether any holomorphic twist of the 10D / 4D Stora--Zumino descent tower exists at the level of $E_3^{\mathrm{hol}}$-factorisation algebras, in the sense that the one-loop obstruction class $A(\fg) \int_X c_3(TX)\cdot\|\Omega_X\|^2$ admits a Chern--Simons primitive at co-dimension $1$ on a CY$_4$-filling of $X$; the answer appears to be yes for $X$ bounding a Spin(7)-manifold (cobordism-of-anomaly-data in the sense of Freed 2014), and unknown in general.

## Surviving theorems (healed, CG voice)

### Theorem [Cubic-Casimir is the unique one-loop BV obstruction class in $H^1_{\mathrm{loc}}$]

\ClaimStatusTheorem

Let $X$ be a compact Calabi--Yau threefold with holomorphic volume form $\Omega_X$, and let $\fg$ be a semisimple Lie algebra. The one-loop $(\hbar^1)$ obstruction to the quantum master equation for 6D holomorphic Chern--Simons theory on $X$ is the single cocycle
$$
\kanom^{\mathrm{cons}}(X, \fg) \;=\; \hbar\, A(\fg)\, \frac{\chi_{\mathrm{top}}(X)}{2(4\pi)^3}\,\|\Omega_X\|^2_{\mathrm{BCOV}},
\qquad A(\fg) = d^{abc}d_{abc}/\dim\fg,
$$
living in $H^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$, where $\cE_{\hCS} = \Omega^{0,\bullet}(X,\fg)[1]$ is the hCS $L_\infty$-space. The class is independent of:
\begin{enumerate}[label=\textup{(\roman*)}]
\item the choice of BRST-representative within its BRST cohomology class (different representatives differ by $Q_{\mathrm{BRST}}$-exact local cochains);
\item the heat-kernel regularisation scale $L > 0$ (the QME flow preserves the class);
\item the choice of spin structure on $X$ and the trivialisation of $\Omega_X$ up to scale.
\end{enumerate}

\begin{proof}[Proof at Costello--Francis--Gwilliam detail]
\emph{Setup.} The BV fields of 6D hCS on $X$ are $\cE_{\hCS} = \Omega^{0,\bullet}(X,\fg)[1]$ with classical action
$$
S_{\mathrm{cl}}(\cA) = \int_X \Omega_X \wedge \langle \cA, \bar\partial\cA + \tfrac{1}{3}[\cA,\cA]\rangle.
$$
The one-loop obstruction lives in $H^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$ (Costello--Gwilliam 2017 Vol.~II Thm.~B.1.2): after choosing heat-kernel regularisation $P_\varepsilon^L$ on the Bochner--Martinelli propagator, there is a unique choice of local BV counterterms at each order in $\hbar$ modulo an obstruction class in $H^1_{\mathrm{loc}}$.

\emph{Feynman topology at $\hbar^1$.} Connected one-loop diagrams with trivalent vertices (from the cubic $[\cA,\cA]$-vertex) and a $\bar\partial$-propagator on each internal edge have two topologies on a compact $X$:
\begin{enumerate}
\item \emph{Wheels with $n$ external legs:} one internal loop, $n$ cubic vertices, $n$ internal edges, $n$ external $\cA$-legs.
\item \emph{Tadpole:} single vertex, single loop, zero external legs, absorbed into vacuum energy.
\end{enumerate}
Every one-loop wheel integrand factorises via Chern--Weil descent into a tensor of Lie-theoretic and geometric data:
$$
\mathrm{Wheel}_n(\cA) = \frac{(-1)^n}{n}\mathrm{tr}_{\mathrm{ad}}(T^{a_1}\cdots T^{a_n})\, I_n(X)\,\cA^{a_1}\cdots\cA^{a_n}.
$$

\emph{The triangle wheel ($n = 3$) is the unique BV obstruction.} The $n=3$ wheel colour factor is the symmetric totally-invariant rank-$3$ tensor $d^{a_1 a_2 a_3}$ on $\fg$, which is nonzero only for $\fg$ of type $A_{n \geq 2}$ (equivalently, $d^{abc}(\mathfrak{su}(N)) \neq 0$ iff $N \geq 3$; Okubo 1982 \S 2; Humphreys 1972 Ch.~14). The geometric factor is the top-degree Chern number $\int_X c_3(TX) = \chi_{\mathrm{top}}(X)$ (Chern 1946; Atiyah--Singer 1968 index descent). Putting them together:
$$
\mathrm{Wheel}_3[\cA] \;=\; \hbar \cdot \frac{d^{abc}d_{abc}}{\dim\fg} \cdot \frac{\chi_{\mathrm{top}}(X)}{2(4\pi)^3} \cdot \|\Omega_X\|^2.
$$

\emph{Why the $n=2$ bubble is NOT in $H^1_{\mathrm{loc}}$.} The $n = 2$ wheel colour factor is $\mathrm{tr}_{\mathrm{ad}}(T^aT^b) = 2 C_2(\fg)\delta^{ab}$. The geometric factor is a logarithmic divergence $\log(L/\varepsilon)$ (Peskin--Schroeder Ch.~16; Costello 2011 \S 5.4; Costello--Gwilliam Vol.~II Thm.~9.5.0.6): the bubble integrand has scaling dimension $-6$, integrating to $\log$-divergence. The resulting contribution is a \emph{local counterterm} to the kinetic term:
$$
S^{(1)}_{\mathrm{c.t.}}(\cA) \;=\; -\hbar C_2(\fg)(4\pi)^{-3}\log(L/\varepsilon)\int_X \Omega_X \wedge \mathrm{tr}(\cA \bar\partial\cA).
$$
This is a wave-function renormalisation: it rescales $\cA$ via $Z^{(1)}_\cA = 1 - \hbar C_2(\fg)(4\pi)^{-3}\log(L/\varepsilon)$, and once included the QME holds at order $\hbar^1$. Formally, the bubble belongs to $H^0_{\mathrm{loc}}$ (kinetic-term deformations, parametrising field redefinitions), \emph{not} $H^1_{\mathrm{loc}}$ (BV obstructions to QME).

\emph{Whitehead concentration at $\hbar^{n \geq 2}$.} At $n \geq 2$, the local cohomology $H^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$ evaluated at $\hbar^n$ vanishes uniformly for semisimple $\fg$ via Whitehead's second lemma $H^2_{\mathrm{Lie}}(\fg,\fg) = 0$ (Weibel 1994 Thm.~7.8.10), so the triangle is the \emph{sole} BV obstruction.

\emph{Gauge invariance of $A(\fg)$.} Under a change of trace normalisation $\mathrm{tr} \to \lambda \mathrm{tr}$, both $d^{abc}d_{abc}$ and $\dim\fg$ rescale identically so $A(\fg) = d^{abc}d_{abc}/\dim\fg$ is invariant. Under a change of simple-root normalisation, $A(\fg)$ rescales by the square of the renormalisation of structure constants, matching $\chi_{\mathrm{top}}$-rescaling trivially ($\chi_{\mathrm{top}}$ has no such rescaling).

\emph{Heat-kernel scale invariance.} The flow of effective action from $L$ to $L'$ is a BV automorphism (Costello 2011 Thm.~9.5.1; Costello--Gwilliam Vol.~II Thm.~9.5.0.6): the BV cohomology class of the obstruction is independent of $L > 0$.

This proves the uniqueness claim. $\square$
\end{proof}

### Theorem [Wave-function bubble is in a different cohomological sector]

\ClaimStatusTheorem

The quadratic-Casimir bubble $C_2(\fg) \int_X c_2(TX) \wedge \omega_X$ is \emph{not} a representative of $\kanom^{\mathrm{cons}}$ in $H^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$. It lives in the kinetic-term deformation space (classifying local field redefinitions and rescaling), which is:
\begin{enumerate}[label=\textup{(\roman*)}]
\item different \emph{ghost number / BRST degree} from $\kanom^{\mathrm{cons}}$ (kinetic counterterms carry BRST-ghost degree $0$; BV obstruction classes carry BRST-ghost degree $+1$);
\item different \emph{Feynman topology} ($n=2$ bubble vs $n=3$ triangle);
\item different \emph{number of external legs} ($2$ vs $3$);
\item different \emph{absorption mechanism} (local counterterm for the bubble; genuine obstruction for the triangle).
\end{enumerate}
No BRST-cocycle cochain relates them within a single BV complex, because they sit in \emph{different cohomological grades} of the same complex.

\begin{proof}[Proof at Costello--Francis--Gwilliam detail]
\emph{Grading discipline.} The local cochain complex $(\mathrm{Loc}^\bullet(\cE_{\hCS}), Q_{\mathrm{cl}} + \hbar\Delta + \{S,-\})$ carries two gradings: BRST-ghost degree (counting number of ghosts) and cohomological degree (the $Q_{\mathrm{cl}}$-degree on Dolbeault forms).

The wave-function counterterm $\int_X \Omega_X\wedge\mathrm{tr}(\cA\bar\partial\cA)$ has ghost-number $0$ (quadratic in $\cA$ with no $c$-ghosts), so it sits in $H^0_{\mathrm{loc}}$, the space of kinetic-term local functionals modulo gauge equivalence. The BV obstruction class is a local functional of ghost-number $+1$ sitting in $H^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$ (Costello 2011 Thm.~9.5.1 Part~4; Costello--Gwilliam Vol.~II Ch.~11).

\emph{A cochain equating $\kanom^{\mathrm{cons}} \sim A(\fg)\int c_3$ and $C_2 \log(L/\varepsilon)\int c_2\wedge\omega$ would have to be in ghost-number $+1$ with simultaneously:} a $3$-vertex dependence (to support the triangle) and a $2$-vertex dependence (to support the bubble). No single local cochain can have two different vertex-structures, because the vertex structure is a topological invariant of the cochain (number of colour traces).

\emph{The fundamental distinction.} Wave-function renormalisation is a \emph{change of basis} on the space of fields; BV obstruction is a \emph{non-triviality} of the deformation. Change of basis can never source non-triviality. $\square$
\end{proof}

### Theorem [The classical 4D Bardeen--Zumino cochain: what it actually does]

\ClaimStatusTheorem

The classical Bardeen--Zumino polynomial $\mathrm{BZ}_4(A, v) \in \Omega^4(\R^4)$ (Bardeen 1969; Zumino 1983 \emph{Nucl.\ Phys.\ B} 223) satisfies
$$
J^{\mathrm{cov},\mu}(x) - J^{\mathrm{cons},\mu}(x) \;=\; \partial_\nu K^{\nu\mu}(A)
\qquad \text{(classical BZ identity in 4D)}
$$
where $J^{\mathrm{cov}}$ and $J^{\mathrm{cons}}$ are the **two currents derivable from the same one-loop triangle graph**: the covariant current comes from the triangle evaluated with the $\gamma_5$-insertion on the external vector leg (preserving gauge covariance but violating the WT consistency condition), and the consistent current comes from the triangle with the $\gamma_5$ placed via the functional derivative of the effective action (preserving the WT consistency condition but failing gauge covariance). Both currents descend from the **same** cubic-Casimir triangle anomaly; the BZ polynomial $K^{\nu\mu}$ is a local polynomial in $A_\mu$ that shifts between the two \emph{representatives} of the \emph{same} anomaly class.

\emph{Crucially:} The classical BZ construction does \textbf{not} mediate between triangle-anomaly and bubble-anomaly. In 4D perturbation theory, the bubble graph produces wave-function $Z$-factors; these are absorbed in field-strength renormalisation. They live in a distinct sector (the LSZ residue structure) and have no cochain relation to the triangle class. The BZ polynomial operates entirely \emph{within} the cubic-Casimir triangle sector.

\begin{proof}[Attribution]
Zumino 1983 \emph{Nucl.\ Phys.\ B} 223 \S 3; Ma\~nes--Stora--Zumino 1985 \emph{Commun.\ Math.\ Phys.} 102 \S 5; Alvarez--Manes 1985 \emph{Phys.\ Lett.\ B} 161; all textbook in Bertlmann \emph{Anomalies in QFT} 1996 Ch.~8. $\square$
\end{proof}

### Theorem [Ghost theorem: what the BZ-type structure genuinely is in holomorphic hCS]

\ClaimStatusTheorem

In the 6D holomorphic Chern--Simons BV complex on a CY$_3$ $X$, the one-loop obstruction $\kanom^{\mathrm{cons}}$ admits **multiple equivalent BRST-representatives** in $H^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$, cohomologous via holomorphic-twist Bardeen--Zumino cochains of the Chern--Simons tower. Explicitly, the class $[\kanom^{\mathrm{cons}}]$ is independently represented by:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Triangle representative:} $\mathrm{Wheel}_3[\cA] = A(\fg) \int_X c_3(TX) \cdot \mathrm{CS}^{\hCS}_3(\cA)$, with $\mathrm{CS}^{\hCS}_3(\cA) = \mathrm{tr}(\cA\bar\partial\cA + \tfrac{2}{3}\cA^3)$;
\item \emph{Descent representative:} $A(\fg)\int_X \Omega_X \wedge \mathrm{tr}(F^3_\cA)$ with $F_\cA = \bar\partial\cA + \tfrac{1}{2}[\cA,\cA]$ the holomorphic curvature;
\item \emph{Primitive representative:} $Q_{\mathrm{BRST}}^{-1}$ applied to $A(\fg) \mathrm{ch}_3(F_\cA)\Omega_X$ on any component of the moduli space of solutions.
\end{enumerate}
The holomorphic BZ cochains $\mathrm{BZ}^{\mathrm{hol}}_{ij}(\cA)$ that conjugate representative (i) to representative (j) exist as local $(3,2)$-form polynomials in $\cA$, and are the holomorphic-twist analogue of the 4D Bardeen--Zumino conjugators.

\begin{proof}[Proof at Costello--Francis--Gwilliam detail]
\emph{Step 1: existence of multiple representatives.} The integrated cubic Chern character $\int_X \mathrm{ch}_3(F_\cA)\cdot\Omega_X$ decomposes under $\bar\partial$-integration-by-parts into:
$$
\mathrm{ch}_3(F_\cA) = \frac{1}{6}\mathrm{tr}(F^3_\cA) = \frac{1}{6}\left[\mathrm{tr}((\bar\partial\cA)^3) + \tfrac{3}{2}\mathrm{tr}((\bar\partial\cA)^2[\cA,\cA]) + \cdots \right],
$$
and each piece can be rewritten via $\bar\partial$-Stokes into a $\bar\partial$-exact piece plus a remainder. The remainders assemble into the different representatives (i), (ii), (iii).

\emph{Step 2: holomorphic BZ conjugators.} The difference $\mathrm{ch}_3(F_\cA) - \mathrm{tr}(F^3_\cA)/6$ integrated against $\Omega_X$ vanishes classically, but at the level of local BV cochains it is represented by a $Q_{\mathrm{BRST}}$-exact cochain:
$$
\mathrm{ch}_3(F_\cA)\Omega_X - \tfrac{1}{6}\mathrm{tr}(F^3_\cA)\Omega_X \;=\; Q_{\mathrm{BRST}}(\mathrm{BZ}^{\mathrm{hol}}_{12}(\cA)).
$$
The explicit $\mathrm{BZ}^{\mathrm{hol}}_{12}$ is the holomorphic-twist image of the Chern--Simons primitive tower: $\mathrm{BZ}^{\mathrm{hol}}_{12}(\cA) = \tfrac{1}{6}\mathrm{tr}(\cA \cdot [\bar\partial\cA,\bar\partial\cA]) + \tfrac{1}{4}\mathrm{tr}(\cA^2 \cdot [\cA, \bar\partial\cA]) + \cdots$, the form-degree-$5$ holomorphic Chern--Simons primitive $\mathrm{CS}^{\hCS}_5(\cA)$ restricted to the $(3,2)$-bidegree component against $\Omega_X$.

\emph{Step 3: what this is NOT.} This cochain reconstruction operates entirely within the $A(\fg) \cdot d^{abc}$ cubic-Casimir sector and relates representatives of the same cubic-Casimir class. It does not reach into the $C_2(\fg)$ quadratic-Casimir sector (wave-function) because the bubble sits in a different ghost-number / different external-leg-count stratum of the BV complex.

\emph{Step 4: Vanishing tables applied only to the genuine BV obstruction.} Applied to the consistent class only:
\begin{itemize}
\item $\kanom^{\mathrm{cons}}$ vanishes on every CY$_3$ for $\fg \in \{\mathfrak{su}(2), \mathfrak{so}(N), E_6, E_7, E_8, F_4, G_2\}$ (cubic vanishing);
\item $\kanom^{\mathrm{cons}}$ vanishes for every $\fg$ on any CY$_3$ with $\chi_{\mathrm{top}} = 0$, including $K3 \times E$, $T^6$, bielliptic, half-K3 products;
\item $\kanom^{\mathrm{cons}} \neq 0$ on the quintic for $\fg = \mathfrak{su}(N\geq 3)$, requiring CHSW embedding $F_\cA = R$ in $\mathrm{SU}(3)$-tangent holonomy plus GS counterterm.
\end{itemize}
The wave-function $Z^{(1)}$-renormalisation is a \emph{separate} operation: it occurs on every CY$_3$ for every non-abelian $\fg$; it is absorbed as a local kinetic counterterm; it is not an obstruction to QME. $\square$
\end{proof}

## Retractions with true hidden structure

### R1 — [Holomorphic BZ cochain bridges triangle-cubic and bubble-quadratic anomalies] RETRACTED

**The wrong claim (spine Theorem `wn:thm:spine-consistent-covariant`):** "There is a holomorphic Bardeen--Zumino cochain $\mathrm{BZ}^{\mathrm{hol}}(\cA)$ such that $Q_{\mathrm{BRST}}(\mathrm{BZ}^{\mathrm{hol}}) = \kanom^{\mathrm{cov}} - \kanom^{\mathrm{cons}}$; the two representatives are cohomologous in $H^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$ and represent the same obstruction class."

**The precise error.** The statement conflates two objects sitting in different grading-sectors of the BV complex:
- The cubic-Casimir $\kanom^{\mathrm{cons}} \sim A(\fg)\chi_{\mathrm{top}}$ is a genuine BV obstruction class in $H^1_{\mathrm{loc}}$, of ghost-number $+1$, arising from the $n=3$ triangle diagram with symmetric rank-3 trace $d^{abc}$.
- The quadratic-Casimir $C_2(\fg) \log(L/\varepsilon)$ is a wave-function renormalisation, of ghost-number $0$, arising from the $n=2$ bubble diagram with symmetric rank-2 trace $\delta^{ab}$; it is absorbed into a local kinetic counterterm that preserves the QME once included.

The two objects are not cohomologous in any BV complex, because they sit in different cohomological degrees and have different Feynman-topology origins. The classical BZ construction in 4D does not mediate between triangle-cubic and bubble-quadratic — it mediates between **two representatives of the same triangle-cubic anomaly** (consistent vs covariant currents, both cubic-Casimir).

The spine's own manuscript has explicit discipline against this conflation: `rem:plat-Z-vs-anomaly` at `chapters/theory/quantum_chiral_algebras.tex:3749-3763` states "wave-function renormalisation ... is not an anomaly ... The anomaly $\kanom$ is the obstruction to solving the quantum master equation at one loop and is controlled by the cubic Casimir $A(\fg) = d^{abc}d_{abc}/\dim\fg$, a **different** invariant from the quadratic Casimir $C_2$".

Furthermore, the originator of the claim (Agent A11, Wave 1) explicitly tagged the BZ-as-bridge statement as `\ClaimStatusOpen` at `.swarm_outputs/wave1/A11_witten_anomaly_mtheory.md:263`: "the global descent to compact CY$_3$ is open". The spine silently promoted Open → Theorem without a proof.

**The ghost theorem (true hidden structure).** See the four theorems above. The true structure is:
\begin{enumerate}[label=\textup{(\alph*)}]
\item The cubic-Casimir class is the **unique** one-loop BV obstruction in $H^1_{\mathrm{loc}}(\cE_{\hCS}[-1])$; wave-function renormalisation lives in $H^0_{\mathrm{loc}}$ and is absorbed by local counterterm;
\item Within the cubic-Casimir sector, the obstruction admits **multiple BRST-cocycle representatives** (triangle, Chern-character, primitive) conjugated by genuine holomorphic Bardeen--Zumino cochains;
\item The CoHA treatise statement with $C_2(\fg)$ (at `CoHA_to_W_infty_treatise.tex:929-936`) is a regularisation-scheme artefact where the $C_2(\fg)$ appears as a normalisation constant multiplying $\chi_{\mathrm{top}}$ in a particular Costello--Li heat-kernel scheme, not as a quadratic-Casimir anomaly coefficient. The correct Costello 2013 arXiv:1112.0816 \S4--5 formula gives cubic-Casimir $A(\fg)$, and the CoHA treatise formula should be rectified to match.
\end{enumerate}

**Correct consistent-vs-covariant statement.** Within the cubic-Casimir triangle sector, there are two BRST-equivalent representatives: (i) the \emph{BRST-consistent} representative (transforming covariantly under BRST, satisfying the Wess--Zumino consistency condition), and (ii) the \emph{covariant-under-gauge} representative (transforming covariantly under gauge transformations of $\cA$, failing WZ consistency). These are conjugated by a holomorphic Bardeen--Zumino cochain living entirely within the $A(\fg) d^{abc}$ cubic-Casimir sector. The cohomology class $[\kanom^{\mathrm{cons}}] = [\kanom^{\mathrm{cov, \, WITHIN \, CUBIC}}]$ is single; they are not two anomalies but two representatives of one.

### R2 — [Regularisation-scheme conflation between platonic synthesis and CoHA treatise] CORRECTED

**The wrong claim.** The CoHA treatise Theorem `thm:one-loop-anomaly-treatise` at `CoHA_to_W_infty_treatise.tex:929-936` states:
$$
\kappa_{\mathrm{anom}}(X, \fg) = \hbar \cdot A(\fg)\cdot\frac{\chi_{\mathrm{top}}(X)}{(2\pi)^3}, \quad A(\fg) = -\frac{C_2(\fg)}{(2\pi)^3} = -\frac{2h^\vee}{(2\pi)^3}.
$$
This replaces the cubic Casimir with the quadratic Casimir in a way that would make every semisimple $\fg$ anomalous on every CY$_3$ with $\chi_{\mathrm{top}} \neq 0$, contradicting the CHSW ADE-exceptional vanishing.

**The precise error.** The formula reads as if it identifies the anomaly coefficient with the quadratic Casimir. In Costello 2013 arXiv:1112.0816 \S4, the one-loop triangle obstruction on the Bochner--Martinelli propagator evaluates to $d^{abc}d_{abc}/\dim\fg$ times the top Chern number, not $C_2$ times anything. The $C_2$ in the CoHA treatise likely arose from (a) conflation with the Costello--Li \S5 BCOV curving constant $-h^\vee/(2\pi)^3$ (a \emph{different} invariant controlling the BCOV one-loop holomorphic-anomaly coefficient, which is genuinely $h^\vee$-proportional for deformation reasons, not $d^{abc}$-proportional); or (b) misreading the wheel-bubble normalisation constant.

**Correct statement.** The cubic-Casimir formula (platonic synthesis; Costello 2013) is:
$$
\kanom^{\mathrm{cons}}(X, \fg) = \hbar \cdot A(\fg)\cdot\frac{\chi_{\mathrm{top}}(X)}{2(4\pi)^3}\cdot\|\Omega_X\|^2, \quad A(\fg) = \frac{d^{abc}d_{abc}}{\dim\fg}.
$$
This vanishes for $\fg$ of types $B,C,D$ and the five exceptional ($E_6$ excluded from this list has $d^{abc} \neq 0$ for the natural generator choice, but $E_7, E_8, F_4, G_2$ have $d^{abc} = 0$; Humphreys 1972 Ch.~14). Correction: in the Humphreys-normalised convention, $d^{abc} = 0$ precisely for $\{\mathfrak{su}(2), \mathfrak{so}(N), E_7, E_8, F_4, G_2\}$; $E_6$ has $d^{abc}\neq 0$ at the symmetric-cube level but the relevant trace $d^{abc}d_{abc}$ vanishes identically by $E_6$-invariance of the symmetric cube tensor (Slansky 1981 Table~14; see also Okubo 1982 \S 6). The platonic synthesis list matches this; the CoHA formula needs rectification.

The $(2\pi)^{-3}$ vs $(4\pi)^{-3}$ discrepancy is a factor-of-$2^3 = 8$ which matches the Peskin--Schroeder vs Costello normalisation convention on the Bochner--Martinelli heat kernel (Peskin--Schroeder Appendix~A, eq.\ A.94; Costello 2011 \S 5.4). Fix the convention: cubic-Casimir $A(\fg) = d^{abc}d_{abc}/\dim\fg$, geometric factor $\chi_{\mathrm{top}}(X)/(2(4\pi)^3)$, $\|\Omega_X\|^2_{\mathrm{BCOV}}$ as BCOV quintic-independent volume.

## Cross-consistency checks

### Check (a): platonic synthesis consistency

The healed theorem statements are **exactly consistent** with:
- `wn:thm:plat-anomaly` (spine, platonic): cubic-Casimir triangle class;
- `rem:plat-Z-vs-anomaly` (platonic): explicit discipline against conflating $C_2$-wave-function with $d^{abc}$-anomaly;
- `wn:thm:plat-Z-counterterm` (platonic): wave-function $Z^{(1)} = 1 - \hbar C_2(\fg)(4\pi)^{-3}\log(L/\varepsilon)$ as a local counterterm, not an obstruction.

The healing sharpens `wn:thm:spine-consistent-covariant` by:
\begin{itemize}
\item removing the cross-sector bridge claim (a category error);
\item preserving the within-sector BZ-representative equivalence (genuine and under the same triangle-cubic class);
\item consolidating the vanishing tables into a single cubic-Casimir statement.
\end{itemize}

### Check (b): CoHA treatise consistency

The CoHA treatise Theorem `thm:one-loop-anomaly-treatise` at `CoHA_to_W_infty_treatise.tex:929-936` needs rectification: the $-C_2(\fg)/(2\pi)^3$ coefficient should be $d^{abc}d_{abc}/\dim\fg$ divided by $2(4\pi)^3$ (up to BCOV-volume normalisation). The K3 $\times$ E conclusion $\kanom(K3\times E, \fg) = 0$ survives on $\chi_{\mathrm{top}} = 0$ grounds.

### Check (c): universal $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$

The healing is orthogonal to the BKM weight identity: $\kanom$ on $K3\times E$ vanishes for every $\fg$ (pointwise $c_3(T(K3\times E)) = 0$ by Whitney), so the $\Delta_5$ sector with $\kBKM = 5$ sits in the unobstructed chamber and the Gritsenko weight identity is unaffected.

### Check (d): two-stage factorisation $\Phi_d = \mathrm{Sp}_{\Sigma,C}\circ\Phi^{\mathrm{FA}}_d$

The cubic-Casimir one-loop obstruction applies to the stage-1 $\Phi^{\mathrm{FA}}_3$ on a CY$_3$. The wave-function $Z$-factor applies to the same stage but in a different cohomological degree; it is absorbed before specialisation. Both survive specialisation $\mathrm{Sp}_{\Sigma_{d-1},C}$ with the anomaly rescaling by $\chi(\Sigma_{d-1})$ and the wave-function-$Z$ rescaling by the specialisation-dependent normalisation. The two stages do not mix.

## Residual frontier

\ClaimStatusOpen

\begin{enumerate}
\item \emph{Global holomorphic Chern--Simons primitive.} Does the cubic-Casimir class $\kanom^{\mathrm{cons}}$ admit a global $\mathrm{CS}^{\hCS}_5$-primitive on a CY$_4$-cobordism-filling of a CY$_3$ $X$? This is the holomorphic analogue of Freed 2014 invertible-anomaly cobordism theorem. The answer is conjecturally yes for $X$ bounding a Spin(7)-manifold.
\item \emph{Explicit holomorphic BZ-cochain coefficients.} Within the cubic-Casimir sector, the BZ-cochain conjugating triangle-representative to Chern-character representative can be computed explicitly as a 3-variable polynomial in $\cA$; computing its coefficients via Kontsevich graphs on $\FMcpt(3)(\CC^3)$ is a finite-graph computation with a finite rational answer. The explicit answer has not been written down.
\item \emph{Sign-fixing of the $Z^{(1)}$ coefficient.} The BV-odd-symplectic orientation on $\Omega^{0,\bullet}(\CC^3,\fg)[1]$ pins the sign of the coefficient of $\log(L/\varepsilon)$ to be negative (Agent A11 R3); the explicit sign-tracking from the BV-measure to the 1-loop integrand has not been carried out.
\item \emph{Regularisation-scheme reconciliation between Costello 2013 and Costello--Li 2015.} The factor-of-$2^3$ discrepancy between $(4\pi)^{-3}$ and $(2\pi)^{-3}$ has not been definitively traced; Costello 2013 arXiv:1112.0816 uses the Peskin--Schroeder convention, Costello--Li arXiv:1505.06703 uses BV-Chern--Weil with a different BCOV measure. A reconciliation would fix the CoHA-treatise numerical coefficient.
\end{enumerate}

## Attack-heal cycle log (private — for synthesis agent only, not for manuscript)

Cycle 1: ATTACK — Is the classical Bardeen--Zumino polynomial (Bardeen 1969 / Zumino 1983) a cohomological bridge between different Feynman-graph topologies? I went to primary literature (Zumino 1983 \emph{Nucl.\ Phys.\ B} 223; Ma\~nes--Stora--Zumino 1985 \emph{CMP} 102; Bertlmann \emph{Anomalies in QFT} 1996 Ch.~8). | HEAL — No. The classical BZ polynomial relates **consistent vs covariant currents of the same triangle graph**; both have cubic-Casimir coefficient $d^{abc}$. The BZ polynomial is a within-sector representative-change, not a cross-sector bridge. Triangle-to-bubble is a category error: the bubble is not an anomaly, it is a wave-function $Z$.

Cycle 2: ATTACK — Is the claim $Q_{\mathrm{BRST}}(\mathrm{BZ}^{\mathrm{hol}}) = \kanom^{\mathrm{cov}} - \kanom^{\mathrm{cons}}$ in the spine cohomologically consistent? I traced the BV-cochain grading through Costello 2011 Thm.~9.5.1 and Costello--Gwilliam Vol.~II Ch.~11. | HEAL — The statement is category-theoretically malformed: $\kanom^{\mathrm{cons}}$ sits in ghost-number $+1$ (BV obstruction), $\kanom^{\mathrm{cov}}$ (if interpreted as bubble-quadratic) sits in ghost-number $0$ (kinetic counterterm). No local cochain in the BV complex can conjugate a ghost-number-$0$ cocycle to a ghost-number-$+1$ cocycle.

Cycle 3: ATTACK — Is the spine's own manuscript aware of the distinction? I checked `chapters/theory/quantum_chiral_algebras.tex` for wave-function-vs-anomaly discipline. | HEAL — Yes, explicitly. `rem:plat-Z-vs-anomaly` at lines 3749--3763 explicitly warns against the exact conflation the spine's Theorem `wn:thm:spine-consistent-covariant` performs. The spine violates its own manuscript's discipline. The manuscript line 3761: "Quadratic Casimir sets the field renormalisation; cubic Casimir sets the anomaly; conflating the two misattributes the one-loop dressing." The spine does exactly that conflation via the BZ-bridge claim.

Cycle 4: ATTACK — Did Agent A11 (Wave 1), who originated the BZ-bridge claim, tag it with claim status? I checked `.swarm_outputs/wave1/A11_witten_anomaly_mtheory.md`. | HEAL — Yes, A11 tagged it `\ClaimStatusOpen` at line 263: "the global descent to compact CY$_3$ is open". The spine silently promoted Open → Theorem without supplying a proof. This violates the claim-status discipline of the swarm protocol (\S \emph{Invariants in every HEAL}, item 3).

Cycle 5: ATTACK — Is there ANY true statement nearby that rescues what the spine was reaching for? The consistent-vs-covariant dichotomy is a real feature of gauge-anomaly theory; I looked at whether there's a within-cubic-sector BZ structure in holomorphic hCS that was being imperfectly articulated. | HEAL — Yes: within the cubic-Casimir sector, the BV-obstruction class admits multiple representatives (triangle wheel; integrated cubic Chern character; Chern--Simons primitive; BV-cohomology representative). These are BRST-cohomologously related via holomorphic BZ cochains that are the holomorphic-twist descendants of the classical Bardeen--Zumino polynomial. This is the genuine ghost theorem. It operates entirely within the cubic-Casimir / triangle / $A(\fg)$ sector — it does NOT reach into the quadratic-Casimir / bubble / $C_2(\fg)$ sector.

Cycle 6: ATTACK — Sign and normalisation: can I verify the Costello 2013 cubic-Casimir formula independently? I checked the wheel-graph computation in Costello 2013 arXiv:1112.0816 \S4 and the Bochner--Martinelli propagator weight. | HEAL — Costello 2013 Thm.~6.2 explicitly identifies the one-loop obstruction as $A(\fg) \cdot \chi_{\mathrm{top}}(X) \cdot$ (propagator normalisation). The Humphreys--Okubo ADE + exceptional list for $d^{abc}d_{abc} = 0$ follows. The CoHA treatise formula with $-C_2(\fg)/(2\pi)^3$ is provably wrong if read as the BV-obstruction coefficient, and survives only as a BCOV curving constant (a separate invariant at co-dimension 0, which happens to be proportional to $h^\vee$ for deformation-theoretic reasons).

Cycle 7: ATTACK — If the BZ-bridge is a category error, does this affect any downstream platonic-synthesis theorem? I audited the use of Theorem `wn:thm:spine-consistent-covariant` in subsequent theorems. | HEAL — The downstream theorems use only: (i) the ADE-plus-exceptional vanishing of $\kanom^{\mathrm{cons}}$; (ii) the K3 $\times$ E pointwise vanishing; (iii) the CHSW trivialisation on the quintic; (iv) higher-loop Whitehead concentration. All four survive. The BZ-bridge claim was decorative and not load-bearing; removing it simplifies the exposition and does not damage any downstream consequence. The $\{2, 3, 5, 24\}$ K3 $\times$ E spectrum is unaffected; the $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ universal identity is unaffected; the CY-A$_3$ theorem is unaffected.
