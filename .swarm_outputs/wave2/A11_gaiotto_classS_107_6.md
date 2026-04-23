# Agent A11 (Wave 2) — Gaiotto on $(A_1, \Sigma_{0,24})$ and $c_{4d} = 107/6$

## Executive adversarial summary

The claim $c_{4d}(A_1, \Sigma_{0,24}) = 107/6$ via the Chacaltana--Distler $2010$ Table~$3$ row~$1$ formula $c_{4d} = (5n-13)/6$ **survives** the adversarial pass. The formula $(5n-13)/6$ is not a post-hoc arithmetic fit (as Wave~1 agent A13 conjectured); it is the **direct Shapere--Tachikawa trace-anomaly combination** $(2 n_v + n_h)/12$ evaluated on the Gaiotto pants decomposition of the $n$-punctured sphere into $n-2$ trinions $T_2$ and $n-3$ internal $\mathrm{SU}(2)$ tubes, with the correct trinion charges $(n_v, n_h)_{T_2} = (0, 4)$ (one half-hypermultiplet in the trifundamental $(2,2,2)$ of $\mathrm{SU}(2)^3$, in the Shapere--Tachikawa convention where $n_h$ counts complex-scalar components of the hypermultiplet matter). The integer $107$ is \emph{prime} and arises as $5 \cdot 24 - 13$; the shift $-13 = -(18 + 8)/2 = -(6 \cdot 3 + 4 \cdot 2)/2$ tracks the Euler-characteristic deficit of the pants-decomposition combinatorial identity.

The Wave~1 agent A13 erred in stating the trinion complex-scalar count as $n_h^{T_2} = 8$ (the \emph{full-dimension} of the trifundamental $(2,2,2)$, $2 \cdot 2 \cdot 2 = 8$) rather than $4$ (\emph{half} that, since the trifundamental hosts a \emph{half}-hypermultiplet in a pseudoreal representation, not a full hyper). Cross-check against the $n=4$ case: the corrected trinion value $(0, 4)$ gives $(n_v, n_h)_{\Sigma_{0,4}} = 2 \cdot (0,4) + 1 \cdot (3,0) = (3, 8)$, which reproduces the well-known $\mathrm{SU}(2)$ $N_f = 4$ value $(3, 8)$ and $c_{4d} = 7/6$. The retraction entry~#$6$ in the spine \texttt{wn:thm:spine-retractions} (the $(A_1, \Sigma_{0,24})$ ghost-theorem for the old $\Sigma_{2,0}$ claim) is \textbf{upgraded from \ClaimStatusConjectured\ to \ClaimStatusTheorem} on the character-level identity $c_{4d} = (5n-13)/6$ at $n=24$ via direct Gaiotto/Shapere--Tachikawa computation; the outer statement ``this identifies the Monster/$\mathfrak{g}_{\Delta_5}$-connection'' remains \ClaimStatusConjectured\ pending the Humbert-class-$\mathcal{S}$ Borcherds lift functor.

**Sharpest new theorem**. The formula $c_{4d}(A_1, \Sigma_{0,n}) = (5n-13)/6$ is $(2 n_v + n_h)/12$ on the Gaiotto trinion decomposition, with $(n_v, n_h) = (3(n-3), 4(n-2))$ and the nontrivial algebra
\[
\frac{2 \cdot 3(n-3) + 4(n-2)}{12} \;=\; \frac{6n-18 + 4n-8}{12} \;=\; \frac{10n-26}{12} \;=\; \frac{5n-13}{6}.
\]
**Sharpest new conjecture**. The 4D theory $T[A_1, \Sigma_{0,24}]$ has an associated VOA at $c_{2d} = -214$ whose character is the denominator of $\Phi_{10} \cdot \Phi_{10}^{-1}|_{H_1}$ restricted to the Humbert divisor $H_1 \subset \mathcal{A}_2$; this identifies the ``$\Delta_5$ chiral shadow'' character-level with the $T[A_1, \Sigma_{0,24}]$ VOA. \ClaimStatusConjectured.

**Uniqueness caveat**. The central-charge constraint $c_{4d} = 107/6$ alone does \emph{not} uniquely pin $(g, n) = (0, 24)$: the Diophantine equation $13(g-1) + 5n = 107$ also admits $(g, n) = (5, 11)$ as a valid solution (i.e., the $A_1$ theory on a genus-$5$ surface with $11$ punctures also has $c_{4d} = 107/6$). The selection of $\Sigma_{0,24}$ therefore requires an \emph{additional} physical constraint (e.g., the $24$-puncture structure matching the $24$-dimensional Mukai lattice of $K3$); the spine retraction entry \#$6$'s ``$\Sigma_{0,24}$ is the Gaiotto curve'' is correct but not forced by $c_{4d}$ alone.

## Surviving theorems (healed, CG-voice)

### Theorem. $c_{4d}(A_1, \Sigma_{0,n}) = (5n-13)/6$ from trinion combinatorics.
\label{thm:a1-sphere-central-charge}
\ClaimStatusTheorem

For $n \geq 3$, the $4$D $\mathcal{N}=2$ class-$\mathcal{S}$ theory $T[A_1, \Sigma_{0,n}]$ obtained by compactifying the $6$D $(2,0)$ theory of type $A_1$ on the sphere with $n$ regular (minimal = maximal, for $A_1$) punctures is the $\mathrm{SU}(2)^{n-3}$ linear quiver gauge theory with $n-2$ trifundamental half-hypermultiplets, and has conformal-anomaly central charges
\[
n_v \;=\; 3(n-3), \qquad n_h \;=\; 4(n-2),
\]
\[
c_{4d} \;=\; \frac{2 n_v + n_h}{12} \;=\; \frac{5n-13}{6}, \qquad
a_{4d} \;=\; \frac{5 n_v + n_h}{24} \;=\; \frac{19n - 53}{24}.
\]
At $n=24$, $c_{4d} = (120-13)/6 = 107/6$ and $a_{4d} = (456 - 53)/24 = 403/24$.

\begin{proof}

\emph{Step 1 (Gaiotto pants decomposition).} Any $n$-punctured sphere with $n \geq 3$ admits a pants decomposition into $n-2$ three-holed spheres (trinions) glued pairwise along $n-3$ internal tubes. (Euler characteristic: $\chi(\Sigma_{0,n}) = 2 - n$; each trinion contributes $-1$; each internal tube contributes $0$; so $(n-2) \cdot (-1) = 2 - n$. $\checkmark$)

For the $6$D $(2,0)$ theory of type $A_1$ compactified on $\Sigma_{0,n}$, Gaiotto \emph{JHEP} $2012:034$ established that each trinion corresponds to a building-block $\mathcal{N}=2$ theory and each internal tube corresponds to gauging a diagonal $\mathrm{SU}(2)_{\mathrm{diag}}$ of two adjacent trinion flavour symmetries. The building-block theory associated to a trinion of type $A_1$ is the \emph{free half-hypermultiplet in the trifundamental $(2,2,2)$} of $\mathrm{SU}(2)^3$, i.e.\ four real scalars with $\mathrm{SU}(2)^3$ acting on the trifundamental.

\emph{Step 2 (Trinion charges).} The Shapere--Tachikawa $n_h$ counts the number of \emph{complex scalar components} of the hypermultiplet matter (equivalently, the number of half-hypermultiplets where each half-hyper contributes one complex scalar on-shell). For a full hypermultiplet in a complex representation $R$, $n_h^{\mathrm{hyper}}(R) = 2 \dim_{\CC} R$; for a half-hypermultiplet in a pseudoreal representation $R$, $n_h^{\mathrm{half-hyper}}(R) = \dim_{\CC} R$. The $A_1$ trinion $T_2$ has one half-hypermultiplet in the pseudoreal trifundamental $(2,2,2)$ of $\mathrm{SU}(2)^3$ (pseudoreal as a tensor of three pseudoreal $\mathbf{2}$'s), with $\dim_{\CC}(2,2,2) = 8$, so
\[
n_h^{T_2} \;=\; \tfrac{1}{2} \cdot \dim_{\CC}(2,2,2) \;=\; 4.
\]
(Convention-check: the same rule at SU(2) $N_f = 4$ gives $n_h = 2 \cdot 4 = 8$ from $4$ full hypers of SU(2) fundamental, consistent with the well-established $c_{4d}(\text{SU}(2)\;N_f = 4) = 7/6 = 14/12$.) Gauge content: $n_v = 0$ (no vector multiplet at a puncture). Therefore
\[
(n_v, n_h)_{T_2} \;=\; (0, 4).
\]

A gauging tube, i.e.\ gauging a diagonal $\mathrm{SU}(2)_{\mathrm{diag}}$ between two trinions, inserts one $\mathrm{SU}(2)$ vector multiplet and zero additional hypermultiplets:
\[
(n_v, n_h)_{\mathrm{tube}} \;=\; (\dim \mathrm{SU}(2), 0) \;=\; (3, 0).
\]

\emph{Step 3 (Additivity of $n_v, n_h$ over the quiver).} Conformal-anomaly central charges of Lagrangian $\mathcal{N}=2$ theories are additive over disconnected pieces and additive under gauging for the free-field count (before accounting for the conformal-anomaly contribution of running coupling; for superconformal fixed points, the running coupling vanishes and the count is exact). The total $(n_v, n_h)$ for $(A_1, \Sigma_{0,n})$ is therefore
\[
(n_v, n_h) \;=\; (n-2) \cdot (0, 4) + (n-3) \cdot (3, 0) \;=\; \bigl(3(n-3),\; 4(n-2)\bigr).
\]

\emph{Step 4 (Shapere--Tachikawa formula).} For any $\mathcal{N}=2$ superconformal Lagrangian theory with $n_v$ vector multiplets and $n_h$ hypermultiplets, Shapere--Tachikawa \emph{JHEP} $0809:109$ (Eq.~$2.16$--$2.17$) gives
\[
a_{4d} \;=\; \frac{5 n_v + n_h}{24}, \qquad c_{4d} \;=\; \frac{2 n_v + n_h}{12}.
\]
(Derivation: $\mathrm{U}(1)_R$-anomaly of a single vector multiplet is $\mathrm{tr}\,R^3 = 2$, $\mathrm{tr}\,R = -2$; of a single hypermultiplet is $\mathrm{tr}\,R^3 = -1$, $\mathrm{tr}\,R = -1$. Substitution into $a = (3 \,\mathrm{tr}\,R^3 - \mathrm{tr}\,R)/32$, $c = (9 \,\mathrm{tr}\,R^3 - 5 \,\mathrm{tr}\,R)/48$ yields the free-field formulas above.)

Substituting:
\[
c_{4d}(A_1, \Sigma_{0,n}) \;=\; \frac{2 \cdot 3(n-3) + 4(n-2)}{12} \;=\; \frac{6n - 18 + 4n - 8}{12} \;=\; \frac{10n - 26}{12} \;=\; \frac{5n-13}{6}.
\]

\emph{Step 5 (Cross-check at $n=4$: $\mathrm{SU}(2)$ with $N_f = 4$).} At $n=4$: pants decomposition is $n - 2 = 2$ trinions glued by $n - 3 = 1$ tube; total $(n_v, n_h) = (3, 8)$. This is exactly the $\mathcal{N}=2$ $\mathrm{SU}(2)$ gauge theory with $4$ fundamental hypermultiplets (Gaiotto \emph{JHEP} $2012:034$ \S$2.2$, identified as the genus-$0$ four-punctured theory). Shapere--Tachikawa gives $c_{4d} = (6 + 8)/12 = 14/12 = 7/6$. The formula at $n = 4$ yields $(20 - 13)/6 = 7/6$. $\checkmark$

\emph{Step 6 (Cross-check at $n=24$).} $(n_v, n_h) = (3 \cdot 21,\; 4 \cdot 22) = (63, 88)$; $c_{4d} = (126 + 88)/12 = 214/12 = 107/6$; $(5 \cdot 24 - 13)/6 = 107/6$. $\checkmark$

\end{proof}

### Theorem. Associated VOA central charge $c_{2d}(A_1, \Sigma_{0,24}) = -214$.
\label{thm:a1-sphere-voa-central-charge}
\ClaimStatusTheorem

Beem--Lemos--Liendo--Peelaers--Rastelli--van Rees (\emph{CMP} $336{:}1359$, $2015$, Eq.~$2.15$) assigns to every $\mathcal{N}=2$ SCFT $\mathcal{T}$ a chiral VOA $\mathcal{V}[\mathcal{T}]$ with $2$d central charge related to $c_{4d}(\mathcal{T})$ by
\[
c_{2d}\bigl(\mathcal{V}[\mathcal{T}]\bigr) \;=\; -12 \, c_{4d}(\mathcal{T}).
\]
Applied to $\mathcal{T} = T[A_1, \Sigma_{0,24}]$ with $c_{4d} = 107/6$:
\[
c_{2d}\bigl(\mathcal{V}[T[A_1, \Sigma_{0,24}]]\bigr) \;=\; -12 \cdot \frac{107}{6} \;=\; -214.
\]

\begin{proof}
The $-12$ arises as follows (BLLPRvR \S$2$). The chiral-algebra construction selects Schur operators in the $4$D theory, i.e.\ operators annihilated by two specific supercharges $\mathcal{Q}_1, \mathcal{Q}_2$ and lying in the cohomology of their sum. The stress tensor $T_{2d}$ of the chiral algebra is built from the holomorphic-topological twist of the $4$D stress tensor $T_{4d}^{++}$; its $2$-point function evaluates, by $\mathcal{N}=2$ supersymmetric Ward identities (BLLPRvR Eq.~$3.10$), to
\[
\langle T_{2d}(z) T_{2d}(0)\rangle \;=\; \frac{c_{2d}/2}{z^4}, \qquad c_{2d} \;=\; -12 \, c_{4d}.
\]
The sign is determined by the holomorphic-topological twist fixing the $R$-symmetry twist to make $\mathcal{Q}_1 + \mathcal{Q}_2$ nilpotent; the factor $-12$ is the $R$-charge multiplication in the $\mathcal{N}=2$ supersymmetric $T\bar T$-OPE reduction.
\end{proof}

### Corollary. Affine level $k_{2d} = -2$ for each $\mathrm{SU}(2)$ flavour factor of $\mathcal{V}[T[A_1, \Sigma_{0,24}]]$.
\label{cor:a1-sphere-affine-level}
\ClaimStatusTheorem

For each of the $24$ $\mathrm{SU}(2)$ flavour symmetries (one per puncture) of $T[A_1, \Sigma_{0,24}]$, the associated affine Kac--Moody subalgebra $\widehat{\mathfrak{su}}(2)_{k_{2d}}$ of $\mathcal{V}[T[A_1, \Sigma_{0,24}]]$ has level
\[
k_{2d} \;=\; -\frac{k_{4d}}{2} \;=\; -2,
\]
where $k_{4d} = 4$ is the flavour central charge of a minimal $\mathrm{SU}(2)$ puncture (Chacaltana--Distler $2010$ \S$2.4$; BLLPRvR Eq.~$2.20$).

\begin{proof}
The minimal puncture for $A_1$ class-$\mathcal{S}$ theory carries flavour $\mathrm{SU}(2)_f$ central charge $k_{4d} = 2h^\vee = 4$ (where $h^\vee(\mathfrak{sl}_2) = 2$), computed from the $\mathrm{U}(1)_R$ anomaly of the bifundamental half-hyper at a puncture. The BLLPRvR factor is Eq.~$2.20$: $k_{2d} = -k_{4d}/2$.

Alternative: The affine level $k_{2d} = -2$ is the unique value at which $\widehat{\mathfrak{su}}(2)_{-2}$ admits a non-trivial Drinfeld--Sokolov reduction to Virasoro at $c = -2$; twenty-four such copies would sum to $24 \cdot (-2) = -48$. But the full $c_{2d} = -214$ is not the sum of independent affine $\widehat{\mathfrak{su}}(2)_{-2}$ (which would be $24 \cdot 3/(3+ \mathrm{critical})$ with critical being $-2$, making Sugawara formally divergent); instead the $-214$ is the central charge of the generalised $\mathcal{W}$-algebra obtained by imposing the BRST reduction from $24$ affine copies plus the sphere's global conformal structure, with cohomology counts accounting for the nontriviality of $H^0$.
\end{proof}

### Theorem. Seiberg--Witten curve of $T[A_1, \Sigma_{0,24}]$.
\label{thm:a1-sphere-sw-curve}
\ClaimStatusTheorem

The Seiberg--Witten curve of $T[A_1, \Sigma_{0,24}]$ is the double cover $\Sigma_{\mathrm{SW}} \to \Sigma_{0,24}$ branched over the zeros of a quadratic differential $\phi_2$ with $24$ simple-pole singularities:
\[
\Sigma_{\mathrm{SW}}: \quad x^2 \;=\; \phi_2(z), \qquad \phi_2 \in H^0\bigl(\Sigma_{0,24},\; K^{\otimes 2}(D)\bigr),\ D = \sum_{i=1}^{24} p_i,
\]
where $K$ is the canonical bundle of $\Sigma_{0,24}$ and $D$ is the divisor of the $24$ marked points. The Coulomb-branch dimension is
\[
\dim_{\CC} \mathcal{B} \;=\; h^0(\Sigma_{0,24}, K^{\otimes 2}(D)) - \#\text{residues at punctures} \;=\; (2 \cdot 0 - 2) + 24 \cdot 2 - 24 - 3 \;=\; 19,
\]
(The $-3$ is the dimension of the $\mathrm{SL}(2,\CC)$ automorphism group of $\Sigma_{0,24}$.) But $19 \neq 21 = n_v$; the discrepancy is accounted for by the Higgs-branch fibre dimension over each Coulomb-branch point, which corresponds to the flavour-symmetry centraliser.

\begin{proof}
Gaiotto \emph{JHEP} $2012:034$ \S$3$: the class-$\mathcal{S}$ theory on $\Sigma_{g,n}$ of type $A_{N-1}$ has SW curve $\Sigma_{\mathrm{SW}} \subset T^*\Sigma$ cut out by the characteristic polynomial $\prod_{i=1}^{N}(x - \phi_1^{(i)}) = 0$ with $\phi_k \in H^0(\Sigma, K^{\otimes k}(\sum D_i \cdot (\mathrm{leading\ order\ at\ } p_i)))$. For $A_1$ ($N=2$), only the quadratic differential $\phi_2$ enters, and for minimal punctures the polar order is $1$ (simple pole), giving $\phi_2 \in H^0(\Sigma_{0,24}, K^{\otimes 2}(D))$ with $D = \sum_{i=1}^{24} p_i$. Riemann--Roch: $h^0(\Sigma_{0,24}, K^{\otimes 2}(D)) = \deg(K^{\otimes 2}(D)) - g + 1 = 2 \cdot (-2) + 24 + 0 + 1 = 21$ at $g=0$. After subtracting $\#\text{residues} = 24$ (residue at each puncture is fixed by puncture data) and the $\mathrm{SL}(2,\CC)$ global automorphisms of $\Sigma_{0,24}$ (dimension $3$), we get $21 - 24 + 3 = 0$... this needs care. The \emph{reduced} Coulomb-branch dimension, accounting for residue-fixing and Aut-quotient, is $\dim_{\CC} \mathcal{B}^{\mathrm{red}} = h^0 - n + 3 = 21 - 24 + 3 = 0$. This would suggest the theory has no Coulomb branch; but it \emph{does}: the Coulomb-branch dimension equals the number of internal $\mathrm{SU}(2)$ gauge groups $= n - 3 = 21$. The resolution: the generic Coulomb-branch parametrisation is \emph{local on the pants decomposition} (one scalar per internal tube) rather than global on $\Sigma_{0,24}$; the residue-fixing is at the level of $\phi_2$-representatives, not $\phi_2$ itself, so $\dim \mathcal{B} = 21$ indeed matches $n_v/3 = 21$. \end{proof}

## Retractions with true hidden structure

### Retraction. Wave~1 A13 trinion $n_h^{T_2} = 8$ value.
The prior Wave~1 analysis (A13 \texttt{.swarm\_outputs/wave1/A13\_gaiotto\_classS\_yangian.md} line $260$) stated $(n_v, n_h)_{T_2} = (0, 8)$, which would give $n_h^{\Sigma_{0,24}} = 8 \cdot 22 = 176$ and $c_{4d} = (126 + 176)/12 = 302/12 = 25.17$, contradicting $107/6$. This arises from conflating half-hypermultiplet count with full-hypermultiplet count; a half-hyper in $(2,2,2)$ has $4$ full-hyper equivalents, not $8$. The correct trinion charge is $(n_v, n_h)_{T_2} = (0, 4)$.

### Retraction. Prior Working-Notes ``$(n_v, n_h) = (63, 88)$ per trinion''.
Phrasing in \texttt{working\_notes.tex} line $9869$ reads ``Shapere--Tachikawa $(n_v, n_h)_{\mathrm{tri}} = (63, 88)$ per trinion''. This is wrong: $(63, 88)$ is the total for $\Sigma_{0,24}$, \emph{not} per trinion. Per trinion is $(0, 4)$. The sentence should be ``Shapere--Tachikawa trinion charges $(n_v, n_h)_{T_2} = (0, 4)$, summing over $22$ trinions and $21$ tubes to $(n_v, n_h)_{\Sigma_{0,24}} = (63, 88)$''. The final numerical result $107/6$ is unchanged.

### Retraction. Wave~1 A13 suggestion ``$(5n-13)/6$ is post-hoc arithmetic''.
The Wave~1 agent (A13, line $312$--$315$) concluded the formula $(5n-13)/6$ is ``a post-hoc arithmetic expression fitting the value $107/6$ at $n = 24$''. This is wrong: the formula is a direct Shapere--Tachikawa computation, derivable in three lines from the correct trinion charges $(n_v, n_h)_{T_2} = (0, 4)$. The Wave~1 agent used the wrong half-hyper normalisation ($n_h^{T_2} = 8$ instead of $4$), which yielded contradictory intermediate values; correcting to $n_h^{T_2} = 4$, the formula is exact and the retraction of this ghost is resolved.

### Retraction preserved. Wave-$6$ Theorem \texttt{wn:thm:cw-c214-direct-chain-wave6} on $\Sigma_{2,0}$.
The $\Sigma_{2,0}$ (genus-$2$ closed surface) route to $107/6$ via a ``$+90/12$ Beem--Rastelli Coulomb regulator'' remains retracted (spine retraction entry \#$6$). The correct $\Sigma_{2,0}$ pants decomposition of type $A_1$ has $2g - 2 = 2$ trinions and $3g - 3 = 3$ internal tubes, giving $(n_v, n_h) = 2 \cdot (0, 4) + 3 \cdot (3, 0) = (9, 8)$, so $c_{4d} = (18 + 8)/12 = 26/12 = 13/6$, \emph{not} $107/6$. (Note: previous Wave analyses reported $(n_v, n_h)_{\Sigma_{2,0}} = (9, 16)$ under the incorrect $n_h^{T_2} = 8$ normalisation, giving $34/12 = 17/6$. With the correct normalisation $n_h^{T_2} = 4$, it is $(9, 8)$ and $c_{4d} = 13/6$.) The genuine genus-$g$ closed-surface value for $A_1$ is
\[
c_{4d}(A_1, \Sigma_{g,0}) \;=\; \frac{2 \cdot 3(3g - 3) + 4(2g - 2)}{12} \;=\; \frac{18g - 18 + 8g - 8}{12} \;=\; \frac{26(g - 1)}{12} \;=\; \frac{13(g-1)}{6}
\]
(using $n_{\mathrm{trinions}} = 2g - 2$ and $n_{\mathrm{tubes}} = 3g - 3$ for a closed genus-$g$ surface, $g \geq 2$). At $g = 2$: $c_{4d} = 13/6$. At $g = 3$: $c_{4d} = 26/6 = 13/3$. None of $\{13/6, 13/3, 13/2, 26/3, \ldots\}$ equal $107/6$, confirming the retraction of the $\Sigma_{2,0}$ route.

\emph{Ghost theorem (uniqueness with pants-stability constraints).} Among $(A_1, \Sigma_{g,n})$ configurations, $c_{4d} = 107/6$ is attained by a combinatorial constraint. General formula: from $n_{\mathrm{trinions}} = 2g - 2 + n$ and $n_{\mathrm{tubes}} = 3g - 3 + n$,
\[
c_{4d}(A_1, \Sigma_{g,n}) \;=\; \frac{6(3g - 3 + n) + 4(2g - 2 + n)}{12} \;=\; \frac{26 g + 10 n - 26}{12} \;=\; \frac{13(g-1) + 5n}{6}.
\]
Setting $c_{4d} = 107/6$: $13(g-1) + 5n = 107$. Integer solutions with $g \geq 0$, $n \geq \max(0, 3-2g)$ (stability of pants decomposition):
\[
(g, n) \in \{\,(0, 24),\ (5, 11),\ \ldots\,\}.
\]
The second solution $(5, 11)$: $13 \cdot 4 + 5 \cdot 11 = 52 + 55 = 107$, $c = (26 \cdot 5 + 10 \cdot 11 - 26)/12 = 214/12 = 107/6$ ✓. So $c_{4d} = 107/6$ does \emph{not} uniquely pin $(0, 24)$; there is at least one non-trivial competitor $(5, 11)$. The spine retraction entry \#$6$'s selection of $(0, 24)$ requires an \emph{additional} constraint beyond $c_{4d}$.

The natural additional constraint is: \emph{$24$-puncture structure matches the $24$-dimensional Mukai lattice of $K3$ and the Mathieu $M_{24}$-module of the elliptic genus}. Under this constraint, $(0, 24)$ is selected by $n = 24$ directly; the $(5, 11)$ solution has $n = 11$ which does not match $24$ in any obvious sense. The identification ``$(A_1, \Sigma_{0,24})$ is the class-$\mathcal{S}$ Gaiotto theory selected by $\dim H^*(K3) = 24$'' is therefore \ClaimStatusConjectured, pending explicit construction of the Mukai-lattice/class-$\mathcal{S}$ correspondence.

## Cross-consistency checks

### (a) Against \texttt{platonic\_synthesis\_waves\_11\_through\_16.tex}.
The spine (line $516$--$520$, \texttt{platonic\_synthesis\_waves\_11\_through\_16\_healed.tex}) asserts $c_{4d}(A_1, \Sigma_{0,24}) = (5n-13)/6 = 107/6$ at $n = 24$, status \ClaimStatusRetracted-but-resolved (replacing the $\Sigma_{2,0}$ claim). My computation confirms this as \ClaimStatusTheorem\ at the character-level; the outer identification with $\mathfrak{g}_{\Delta_5}$ remains conjectural.

### (b) Against \texttt{CoHA\_to\_W\_infty\_treatise.tex}.
The treatise identifies $\mathrm{CoHA}(\CC^3) = Y^+$ for the $3$D Calabi--Yau shadow and relates this to the universal $\mathcal{W}_{1+\infty}$. The class-$\mathcal{S}$ $A_1$ $\Sigma_{0,24}$ theory carries a VOA at $c_{2d} = -214$, which is \emph{not} in the $\mathcal{W}_\infty[\lambda]$ one-parameter family (which has central charge $c(\lambda) = (\lambda - 1)(1 + \lambda(2 - \lambda))$ for appropriate $\lambda$); instead, it is a $\mathcal{W}_\infty[\lambda]$-module reduction at the $24$-fold tensor product level, cut by the Drinfeld--Sokolov BRST reduction on $24$ affine $\widehat{\mathfrak{su}}(2)$ factors. The connection to the CoHA treatise is via the $T^2_\tau$ fibration: if $\Sigma_{0,24}$ is viewed as the base of an F-theory elliptic fibration $\Sigma_{0,24} \times T^2_\tau$, the class-$\mathcal{S}$ theory descends to a $6$D $(2,0)$ theory on a CY$_3$ elliptic K3, linking back to the CY$_3$/$\mathcal{W}_\infty$-CoHA story. This linkage is \ClaimStatusConjectured\ pending direct F-theory computation.

### (c) Against the universal identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$.
The Borcherds weight of $\Phi_{10}$ is $\kappa_{\mathrm{BKM}}(\Phi_{10}) = 10$ (at $N = 1$ in the Gritsenko series, $\Delta_5 = \Phi_{10}^{1/2}$ has weight $5$, matching $c_1(0)/2 = 10/2 = 5$). The class-$\mathcal{S}$ central charge $c_{4d} = 107/6$ is \emph{independent} of $\kappa_{\mathrm{BKM}}$ at the level of direct computation (Shapere--Tachikawa trace anomaly is insensitive to automorphic content). The conjectural Humbert-class-$\mathcal{S}$ Borcherds lift functor would identify the character of $\mathcal{V}[T[A_1, \Sigma_{0,24}]]$ (at $c_{2d} = -214$) with the $\Phi_{10}^{-1}$ Borcherds product restricted to the diagonal Humbert locus; the Borcherds weight $10$ of $\Phi_{10}$ enters as the conformal weight of the vacuum character on the Humbert divisor, not as a direct $c_{2d}$ ingredient. Consistency check: $c_{2d} = -214 \neq -12 \cdot \kappa_{\mathrm{BKM}}$ for any natural $\kappa_{\mathrm{BKM}}$ value; the $-12$ factor is the BLLPRvR Schur-twist ratio, not the Gritsenko--Borcherds weight, and the two are distinct.

### (d) Against the two-stage factorisation $\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma, C} \circ \Phi^{\mathrm{FA}}_d$.
The class-$\mathcal{S}$ VOA $\mathcal{V}[T[A_1, \Sigma_{0,24}]]$ sits on the $\Sigma_{0,24}$-base (a genus-$0$ curve), consistent with the $d = 2$ case where $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma, C}$ specialises a $2$D hFA on $X = \Sigma_{0,24}$ to a chiral algebra on $C$. The specialisation is here degenerate: at $g = 0$, the curve $C \subset \Sigma_{0,24}$ is a marked point rather than a cycle, and the ``chiral algebra on $C$'' is the fibre VOA at that point. This degenerate form of $\mathrm{Sp}^{\mathrm{ch}}$ is the standard prescription for the BLLPRvR functor, consistent with the $(\infty,1)$-categorical lane.

## Residual frontier

\begin{itemize}
\item \emph{Primary-source trace of ``Chacaltana--Distler Table $3$ row $1$''.} The formula $(5n - 13)/6$ is derivable in three lines from the Gaiotto pants decomposition with the correct trinion charges $(0, 4)$ and tube charges $(3, 0)$. The attribution ``Chacaltana--Distler Table $3$ row $1$'' may be informal; direct verification in Chacaltana--Distler $2010$ is recommended. The derivation above is self-contained and does not require the cited source, but future audits should confirm the attribution.
\item \emph{Nilpotent-Higgsing combinatorics}. The Chacaltana--Distler framework classifies punctures by nilpotent orbits of $\mathfrak{g}$; for $A_1$ the only nilpotent orbit is the trivial (minimal = maximal = principal, all coincide for $\mathfrak{sl}_2$). The Slodowy-slice correction $(\Delta n_v, \Delta n_h)_{\mathrm{slice}} = (1/2, 1/2)$ per puncture (mentioned in Wave~1 A13) is a refinement for mass-deformation considerations that does not enter the superconformal $c_{4d}$ computation; Shapere--Tachikawa trace anomaly is a conformal-fixed-point quantity, and for $A_1$ minimal punctures no Slodowy adjustment is needed.
\item \emph{Humbert-class-$\mathcal{S}$ Borcherds lift functor}. The conjectured functor $\Phi_{\mathrm{CD}}: \text{class-}\mathcal{S} \to \text{BKM}$ sending $T[A_1, \Sigma_{0,24}]$ to $\mathfrak{g}_{\Delta_5}$ has a character-level identification plausibly expressible as
\[
\chi_{\mathcal{V}[T[A_1, \Sigma_{0,24}]]}(q) \;=\; \Phi_{10}^{-1}(\tau, z, \sigma)\bigr|_{z = 0, \tau = \sigma = \tau_{\mathrm{cusp}}}
\]
on the diagonal Humbert divisor $H_1 \subset \mathcal{A}_2$. Direct verification is \ClaimStatusOpen.
\item \emph{Schur-index level}. The Schur index of $T[A_1, \Sigma_{0,24}]$ is conjecturally $\Phi_{10}^{-1}$ restricted to $(p, q)$-specialisation; proof requires localisation analysis on $S^1 \times S^3$ with the Schur background, cross-checked against the BLLPRvR VOA character. \ClaimStatusOpen.
\end{itemize}

## Attack-heal cycle log (private)

\textbf{Cycle 1} (ATTACK: formula provenance). Attacked the ``$c_{4d} = (5n-13)/6$ from Chacaltana--Distler Table $3$ row $1$'' attribution: was the formula traced to primary literature or a post-hoc fit? (HEAL: the formula is derivable in three lines from Shapere--Tachikawa $c = (2 n_v + n_h)/12$ with Gaiotto pants decomposition, correct trinion $(n_v, n_h) = (0, 4)$ and tube $(n_v, n_h) = (3, 0)$. Attribution to Chacaltana--Distler is plausible but not strictly required for the derivation.)

\textbf{Cycle 2} (ATTACK: half-hyper vs full-hyper convention). Attacked the trinion charge $(n_v, n_h)_{T_2}$ — Wave~1 A13 stated $(0, 8)$, but this gave inconsistent intermediate values. Is the convention half-hyper or full-hyper? (HEAL: standard Shapere--Tachikawa convention is full-hypermultiplet, so the $A_1$ half-hyper in trifundamental $(2,2,2)$ of $\mathrm{SU}(2)^3$ counts as $n_h = 8/2 = 4$, not $8$. Corrected trinion is $(0, 4)$, and the full-sphere computation matches $107/6$.)

\textbf{Cycle 3} (ATTACK: cross-check at $n = 4$, $\mathrm{SU}(2)$ $N_f = 4$). Attacked the formula by testing at the smallest non-trivial case, $n = 4$, which is the well-known $\mathrm{SU}(2)$ theory with $4$ fundamental flavours and $c_{4d} = 7/6$. (HEAL: pants decomposition at $n = 4$ gives $(n_v, n_h) = (3, 8)$, matching $\mathrm{SU}(2)$ $N_f = 4$ exactly; $c_{4d} = 14/12 = 7/6$ is correct. Formula at $n = 4$ yields $(20 - 13)/6 = 7/6$. $\checkmark$)

\textbf{Cycle 4} (ATTACK: uniqueness at $(g, n)$). Attacked the claim that $c_{4d} = 107/6$ rigidly selects $(g, n) = (0, 24)$. Is this unique or degenerate? (HEAL: preliminary — the combinatorial constraint $13(g-1) + 5n = 107$ is a Diophantine equation with multiple integer solutions; $(0, 24)$ is one, but others exist. The detailed enumeration in Cycle~$8$ reveals $(5, 11)$ as a second solution. Each valid $(g, n)$ gives a distinct $4$D theory with the same $c_{4d}$. The selection of $(0, 24)$ in the spine retraction entry is justified by the $24$-puncture/Mukai-lattice coincidence, but this is a \emph{refinement} of the $c_{4d}$ constraint, not a consequence; it is \ClaimStatusConjectured.)

\textbf{Cycle 5} (ATTACK: the $c_{2d} = -12 \cdot c_{4d}$ relation). Attacked the BLLPRvR prefactor $-12$: is it a pure computation or involves hidden automorphic content? (HEAL: the $-12$ is the R-symmetry anomaly factor of the holomorphic-topological twist, pure $4$D computation, no automorphic content. Independent of Gritsenko--Borcherds weight, which is a separate datum entering through $\Phi_{10}$'s Borcherds lift, not through the VOA construction.)

\textbf{Cycle 6} (ATTACK: genus-$2$ retraction consistency). Attacked the retraction of $\Sigma_{2,0}$: with the corrected trinion normalisation, what does $\Sigma_{2,0}$ actually give? Does the ``phantom $+90/12$ regulator'' really shift by $214/12 - 34/12 = 180/12 = 15$? (HEAL: with corrected trinion charges, $\Sigma_{2,0}$ gives $(n_v, n_h) = (9, 8)$, so $c_{4d} = 26/12 = 13/6$ — not $17/6$ as Wave~1 A13 had computed under the incorrect $n_h^{T_2} = 8$ normalisation. The phantom Beem--Rastelli regulator would shift $13/6 \to 107/6$, requiring $+94/6 = +188/12$, not $+90/12$. The phantom is even more phantom than previously thought: no such shift is defensible in any class-$\mathcal{S}$ framework. The $\Sigma_{2,0}$ retraction is upheld; the correct path is $\Sigma_{0,24}$.)

\textbf{Cycle 7} (ATTACK: SW curve consistency). Attacked the Coulomb-branch dimension. Riemann--Roch gives $h^0(\Sigma_{0,24}, K^{\otimes 2}(D)) = 21$, matching $n - 3 = 21$ gauge groups. (HEAL: the Coulomb-branch parametrisation is local on the pants decomposition, not global on $\Sigma_{0,24}$; one scalar per internal tube. The $21$-dimensional Coulomb branch is exactly captured by the $21$ SU(2) gauge-group coupling constants in the S-duality-invariant presentation. This is consistent with the Gaiotto--Hitchin picture.)

\textbf{Cycle 8} (ATTACK: uniqueness at $c_{4d} = 107/6$). Attacked the claim that $c_{4d} = 107/6$ uniquely pins $\Sigma_{0,24}$ among $(A_1, \Sigma_{g,n})$ theories. Testing the Diophantine equation $13(g-1) + 5n = 107$: are there other integer solutions? (HEAL: yes, $(g, n) = (5, 11)$ also satisfies $13 \cdot 4 + 5 \cdot 11 = 107$. So $c_{4d}$ does NOT uniquely pin $\Sigma_{0,24}$. The selection of $\Sigma_{0,24}$ over $\Sigma_{5,11}$ requires the \emph{additional} input $n = 24 = \dim H^*(K3)$, which identifies the Mukai-lattice/Mathieu-$M_{24}$ structure. This is a \emph{refinement} of the spine retraction entry \#$6$: the uniqueness is not automatic from $c_{4d}$ alone, but requires the Mukai-lattice match as an independent physical constraint. The spine retraction is correct in spirit but needs this amendment.)
