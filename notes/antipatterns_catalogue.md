# Anti-Pattern Catalogue (Vol III)

This note collects all CY-specific anti-patterns (AP-CY1 through AP-CY33)
and cross-programme anti-patterns (AP150--AP157, FM24) into a reference
table. Each entry records the failure mode, its severity, and the
counter-measure. These patterns were identified through systematic error
archaeology across 100+ commits.

*Relocated from `appendices/antipatterns.tex` on 2026-04-17 per the
Manuscript Metadata Hygiene rule in `CLAUDE.md`: the anti-pattern
catalogue is working-notes scaffolding and does not belong in the
typeset manuscript.*

## Severity levels

| Level    | Meaning                                                    | Action                                 |
| -------- | ---------------------------------------------------------- | -------------------------------------- |
| Critical | Theorem status wrong (conjecture $\to$ theorem)            | Immediate fix; audit all instances     |
| High     | Numerical or structural error propagates                   | Fix before next build                  |
| Medium   | Convention clash or ambiguity                              | Fix in current session                 |
| Low      | Cosmetic or cross-reference staleness                      | Fix in batch                           |

## CY-specific anti-patterns: AP-CY1 through AP-CY8

- **AP-CY1 -- CY dim $\neq$ cpx dim (High).**
  $\mathrm{Fuk}(X)$ and $D^b(\mathrm{Coh}(X))$ are $\mathrm{CY}_n$ where
  $n$ is the *complex* dimension, not the real dimension $2n$.
  **Counter**: always state "$\mathrm{CY}_d$ with $d = \dim_{\mathbb{C}} X$".

- **AP-CY2 -- CY trace target (High).**
  The CY trace lives in $\mathrm{HC}^-_d(\mathcal{C})$ (negative cyclic
  homology), not just $\mathrm{HH}_d \to k$. The negative cyclic
  refinement is essential for the $S^1$-framing.
  **Counter**: always write $\mathrm{HC}^-_d$, never bare
  $\mathrm{HH}_d \to k$.

- **AP-CY3 -- $E_2 \neq$ commutative (High).**
  $E_2$ braiding is *not* symmetric. $E_2 \to E_\infty$ loses all
  quantum group structure.
  **Counter**: never write "commutative" for $E_2$; write "braided".

- **AP-CY4 -- Drinfeld $\neq$ derived center (High).**
  $Z(\mathcal{C})$ (monoidal center via half-braidings) $\neq$
  $Z^{der}(A)$ (Hochschild cochains). The relationship: Drinfeld center
  categorifies the derived center.
  **Counter**: always specify which center.

- **AP-CY5 -- Root-of-unity requirement (Medium).**
  Kazhdan--Lusztig equivalence requires $q$ a root of unity. At generic
  $q$, $\mathrm{Rep}_q(\mathfrak{g})$ is semisimple.
  **Counter**: state the $q$-specialization explicitly.

- **AP-CY6 -- $A_X$ at $d=3$ (Critical).**
  $A_X$ for CY3 does *not* exist --- it IS the $d=3$ programme.
  Results depending on $A_X$ at $d=3$ must use `\begin{conjecture}`
  and `\ClaimStatusConditional`, naming CY-A$_3$.
  **Counter**: decision tree HZ3-1.

- **AP-CY7 -- CoHA $\neq$ $E_1$-chiral (High).**
  CoHA is associative (Hall product), not a chiral algebra.
  "$E_1$-sector of $G(X)$" assumes $G(X)$ exists.
  **Counter**: connection is via the functor $\Phi$, not identification.

- **AP-CY8 -- Borcherds $\neq$ bar Euler (High).**
  The identification $\Phi_{10} = $ bar Euler product is an
  *observation* (for $K3 \times E$), not a theorem. Conditional on
  CY-A$_2$ and Vol I Borcherds-lift identification.
  **Counter**: cite both CY-A and Vol I anchor.

## Empirical anti-patterns: AP-CY9 through AP-CY13

- **AP-CY9 -- Jacobi discriminant (High).**
  For $\phi_{k,m}$ of index $m$, only discriminants $D$ with $D \equiv 0$
  or $3 \pmod{4}$ (at $m=1$) can appear. Also $c(-1) = 2$ for
  $\phi_{0,1}$ in Eichler--Zagier convention, not $1$.
  **Counter**: verify discriminant constraint before filling tables.

- **AP-CY10 -- Flop $\neq$ Koszul dual (High).**
  Birational flop $X \dashrightarrow X^+$ preserves $\kappa_{ch}$.
  Koszul dual $A^!$ satisfies
  $\kappa_{ch}(A) + \kappa_{ch}(A^!) = \rho_K$. Flop exchanges chambers;
  Koszul exchanges algebra/coalgebra.
  **Counter**: $\kappa_{ch}(A_X) = \kappa_{ch}(A_{X^+})$ for flop.

- **AP-CY11 -- Conditional transitivity (Critical).**
  If Result B depends on Result A which depends on CY-A$_3$, then B is
  *also* conditional on CY-A$_3$. Conditionality propagates.
  **Counter**: use `\ClaimStatusConditional` with full chain.

- **AP-CY12 -- Shadow class computation (High).**
  G/L/C/M must be computed from the full shadow tower, not from
  generator counting or non-formality ($m_3 \neq 0$) alone. Local
  $\mathbb{P}^2$ is class M (infinite depth), not class L.
  **Counter**: always compute the full tower.

- **AP-CY13 -- Stale Part references (Low).**
  After any Part restructuring, grep all three volumes for stale
  `Part~[IVXL]` references.
  **Counter**: use `\ref{part:...}` exclusively.

## Deep empirical anti-patterns: AP-CY14 through AP-CY20

- **AP-CY14 -- Unconstructed in thm (Critical).**
  Any statement whose proof chain passes through $G(X)$ at $d=3$,
  $A_{K3 \times E}$, or any unconstructed object **must** use
  `\begin{conjecture}`, never `\begin{theorem}`.
  **Counter**: default to `\begin{conjecture}` in Vol III.

- **AP-CY15 -- README inflation (Medium).**
  README must not claim "verified" for structural analogies.
  **Counter**: after README edits, verify every "proved" against
  `\ClaimStatus` tags.

- **AP-CY16 -- Matrix size conflation (Medium).**
  $\mathrm{Sp}_4$ quotient by $\pm I_4$ ($4 \times 4$), not $\pm I_5$.
  $O(\Lambda^{3,2})$ quotient by $\pm I_5$ ($5 \times 5$).
  **Counter**: verify matrix dimensions match group rank.

- **AP-CY17 -- MF CY dimension (High).**
  For $W\colon \mathbb{A}^n \to \mathbb{A}^1$, $\mathrm{MF}(W)$ is
  $\mathrm{CY}_{n-2}$, not $\mathrm{CY}_{n-1}$. ADE in 2 variables:
  $\mathrm{CY}_0$. Need 4 variables for $\mathrm{CY}_2$, 5 for
  $\mathrm{CY}_3$.
  **Counter**: verify $n - 2$ against desired CY dimension.

- **AP-CY18 -- Lattice theta series (Medium).**
  Leech theta: minimum norm${}^2 = 4$, first correction at $q^2$ not
  $q^1$. Never conflate $j(\tau)$ coefficients with $V_\Lambda$
  character.
  **Counter**: verify by direct computation.

- **AP-CY19 -- $\hat{A}$-genus halving (High).**
  $\hat{A}(x) = \frac{x/2}{\sinh(x/2)}$; convergence radius $= 2\pi$
  (first pole of $\sin(x/2)$ at $x = 2\pi$). Dropping the $/2$ gives
  spurious radius $\pi$.
  **Counter**: always include the $/2$ in the argument.

- **AP-CY20 -- Normal bundle $\neq$ spectral (High).**
  The $\mathbb{Z} \times \mathbb{Z}$ grading from $N_{C/Y}$ connects to
  $(q,t)$ through the $\Omega$-background, not directly.
  **Counter**: name the intermediary mechanism (equivariant
  localization).

## 6d hCS session anti-patterns: AP-CY21 through AP-CY26

- **AP-CY21 -- $E_3$ bar class M (High).**
  $(1+t)^{3g}$ holds for classes L and C only. Class M:
  infinite-dimensional ($d_4$ survives).
  **Counter**: state the shadow class before claiming $E_3$ bar
  cohomology.

- **AP-CY22 -- Miki is algebra-specific (Medium).**
  The $S_3$ permutation of $(q_1, q_2, q_3)$ comes from the Weyl group
  of the CY torus, not from the $E_3$ operad.
  **Counter**: state it requires
  $U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)$.

- **AP-CY23 -- $E_1$ not $E_\infty$ bialgebra (Critical).**
  The coproduct $\Delta_z$ lives on the $E_1$ (ordered) side.
  $E_\infty$ averaging kills Hopf structure. Li's vertex bialgebra
  ($E_\infty$) is the wrong categorical home.
  **Counter**: formulate Hopf data at $E_1$ level using $B^{ord}$.

- **AP-CY24 -- Docstring confabulation (Medium).**
  Correct code but fabricated "ground truth" in docstrings.
  **Counter**: verify every numerical value against actual function
  output.

- **AP-CY25 -- $R$-matrix from vacuum (High).**
  $R(z) = (\mathrm{id} \otimes S) \circ \Delta_z(1_A)$ is wrong (counit
  axiom gives $1 \otimes 1$). Correct: construct via the half-braiding.
  **Counter**: never extract $R$ from $\Delta(1)$.

- **AP-CY26 -- Verdier $\neq$ $\sigma_2$ inversion (High).**
  $k^! = -k$ comes from Shapovalov form transposition, not from
  $\sigma_2(-h_i) = -\sigma_2$ (false: $\sigma_2$ is degree-2
  homogeneous, hence even).
  **Counter**: derive $k^!$ from Shapovalov/Verdier.

## Swarm-mined anti-patterns: AP-CY27 through AP-CY33

- **AP-CY27 -- Sandbox non-persistence (High).**
  Background agents report successful writes but files do not persist
  (sandbox isolation).
  **Counter**: verify file existence with `ls` after agent completion.

- **AP-CY28 -- Pole-unsafe test points (High).**
  When testing $g(z)$ with poles at $z = \pm h_i$, test points must
  avoid these values.
  **Counter**: use $h = (37, 41, -78)$ for large-parameter safety.

- **AP-CY29 -- Wrong-repo file writes (Medium).**
  Agents write files to the wrong volume's directory.
  **Counter**: verify full path includes correct repo root.

- **AP-CY30 -- Factored $\neq$ solved (Critical).**
  $S_{ijk} = R_{ij} R_{ik} R_{jk}$ from YBE-satisfying $R$ does *not*
  satisfy ZTE. $O(\kappa_{ch}^2)$ obstruction proved
  (`thm:zte-failure`).
  **Counter**: never assume pairwise $\Rightarrow$ higher-order.

- **AP-CY31 -- Spectral $z \neq$ worldsheet $z$ (High).**
  Drinfeld coproduct $\Delta_z$: Yangian spectral parameter. OPE
  $T(z)T(w)$: worldsheet coordinate. Different objects.
  **Counter**: always state whether $z$ is spectral or worldsheet.

- **AP-CY32 -- Reorganization $\neq$ bypass (Medium).**
  The 6d factorization homology route appears to bypass CY-A$_3$ but
  reorganizes the conjecture into subproblems, solving none
  independently.
  **Counter**: verify each subproblem is independently resolved.

- **AP-CY33 -- Chain $\neq$ rational (High).**
  $E_3$ structure is genuine at the chain level but collapses to $E_2$
  under formality (rational coefficients). Physical content lives at
  the chain level.
  **Counter**: state whether claim is chain-level or rational.

## Cross-programme anti-patterns: AP150--AP157 and FM24

- **AP150 -- Confabulated composites (Critical).**
  Agents stitch real ingredients into composite structures that do not
  exist.
  **Counter**: verify each arrow independently before writing composite
  diagrams.

- **AP151 -- $\hbar$ convention clash (High).**
  Two definitions of $\hbar$ can coexist in one chapter.
  **Counter**: grep for existing definitions; one file, one $\hbar$.

- **AP152 -- "Ordered" ambiguity (Medium).**
  "Ordered product" can mean labeled-ordered ($E_1$ bar), time-ordered
  (OPE), or normally-ordered (Wick).
  **Counter**: bare "ordered" is forbidden; always qualify.

- **AP153 -- $E_3$ scope inflation (High).**
  $E_3$ on Hochschild cochains (Deligne conjecture) requires $E_\infty$
  input. For $E_1$ input, Hochschild cochains carry only $E_2$.
  **Counter**: verify input is $E_\infty$ before claiming $E_3$.

- **AP154 -- Two $E_3$ structures (Medium).**
  Algebraic $E_3$ (Deligne) vs topological $E_3$ (configuration space).
  Agree under formality; differ at chain level.
  **Counter**: specify which $E_3$ and whether formality is assumed.

- **AP155 -- Novelty overclaim (Medium).**
  When $\Phi$ recovers a known invariant, the invariant is not new,
  only the construction path.
  **Counter**: state "$\Phi$ recovers the known invariant $X$
  (due to [cite]) via a new path".

- **AP156 -- Weierstrass $P_1$ ambiguity (Medium).**
  $\theta_1'/\theta_1$ vs Weierstrass $\zeta(\cdot; \Lambda)$ differ by
  $\mathrm{Im}(z)$-dependent terms.
  **Counter**: specify convention and state quasi-periodicity.

- **AP157 -- Degeneration-type dependence (High).**
  Different degenerations (large complex structure, conifold, orbifold,
  MUM, tropical) produce different chiral algebras.
  **Counter**: name the degeneration type explicitly.

- **FM24 -- B-cycle $i^2$ sign (Critical).**
  $i^2 = -1$ not $+1$. Error gives $|q| = 1$ instead of $|q| < 1$,
  destroying $q$-expansion convergence.
  **Counter**: verify $|q| < 1$ and $\mathrm{Im}(\tau) > 0$.

## Statistics

| Category                            | Count |
| ----------------------------------- | ----: |
| CY-specific (AP-CY1--AP-CY33)       |    33 |
| Cross-programme (AP150--AP157)      |     8 |
| Formula-mechanical (FM24)           |     1 |
| **Total catalogued**                |  **42** |
| Critical severity                   |     8 |
| High severity                       |    19 |
| Medium severity                     |    12 |
| Low severity                        |     1 |

Two anti-patterns have required fixes in 10+ independent instances:
AP-CY6/AP-CY14 (unconstructed object in theorem environment, 11+
fixes) and AP113 (bare $\kappa$, 15+ fixes). These two alone account
for approximately 40% of all error-correction commits in Vol III.
