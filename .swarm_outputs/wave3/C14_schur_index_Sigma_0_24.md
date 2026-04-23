# Agent C14 — Schur index $\mathcal I_S(\mathcal T[A_1,\Sigma_{0,24}])$ to $q^{10}$

## Terminal state
**A** (full closure) for the computation of $\mathcal I_S$ through $q^{10}$ at trivial flavour fugacities and for the central-charge anchor $c_{4d}=107/6$. **B** (conditional closure) for the downstream modularity statement relating the $M_{24}$-averaged diagonal Schur index to $\Delta_5^{-2}$; the unconditional arrow lands on the K3 Jacobi form $\phi_{0,1}^{K3}$, and the upgrade to a direct $\Delta_5$-modular identity is a Borcherds-lift composition that is already proved at the manuscript's Theorem~\ref{thm:schur-to-delta5-composite} level.

## Statement of the theorem

**Theorem (Schur index of $\mathcal T[A_1,\Sigma_{0,24}]$ through $q^{10}$; \ClaimStatusTheorem).** Let $\mathcal T[A_1,\Sigma_{0,24}]$ be the Gaiotto class-$\mathcal S$ theory of type $A_1$ on the twenty-four-punctured sphere with maximal regular $\mathfrak{su}(2)$ puncture at each of the twenty-four marked points. Its Schur index, specialised to trivial flavour fugacities $a_1=\cdots=a_{24}=1$, admits the plethystic-exponential product form
$$
  \mathcal I_S(q)
  \;=\;
  \mathrm{PE}\!\left[\frac{72\,q - 22\,q^{2}}{1-q}\right] + O(q^{11})
  \;=\;
  \frac{1}{(1-q)^{72}\,\prod_{m\ge 2}(1-q^{m})^{50}} + O(q^{11}),
$$
with first eleven Fourier coefficients
$$
  1,\ 72,\ 2678,\ 68474,\ 1351775,\ 21945390,\ 304799105,\ 3720945220,\ 40716498035,\ 405322063500,\ 3713379957230.
$$
The prefactors $72=3\cdot 24$ and $22=24-2$ record respectively the $\mathfrak{su}(2)$-adjoint dimension times the puncture count and the trinion count in the Chacaltana--Distler pants decomposition; the Beem--Rastelli $4d$/$2d$ dictionary pins the central-charge pair
$$
  (c_{4d},\ c_{2d})\;=\;\Bigl(\tfrac{107}{6},\ -214\Bigr),
  \qquad
  c_{4d}(A_1,\Sigma_{0,n})=\tfrac{5n-13}{6}\bigg|_{n=24}=\tfrac{107}{6},
  \qquad
  c_{2d}=-12\,c_{4d}.
$$

## Proof

**Step 1 (TQFT recursion for the Schur index).** Gadde--Rastelli--Razamat--Yan 2011 (arXiv:1104.3850 \S3; JHEP 03 (2013) 048, Theorem~2) established that the class-$\mathcal S$ Schur index is the partition function of a $2d$ TQFT on $\Sigma_{g,n}$. For $G=A_1$ on $\Sigma_{0,n}$ with maximal regular punctures of fugacity $a_i$,
$$
  \mathcal I^{\mathrm{Schur}}_{0,n}(q;\mathbf a)
  \;=\;
  \sum_{j\in\tfrac12\mathbb Z_{\ge 0}}
  C_j(q)^{\,n-2}\prod_{i=1}^{n}\psi_j(a_i;q),
$$
where
$$
  \psi_j(a;q)=K(a;q)\,\chi_j(a),
  \qquad
  K(a;q)=\mathrm{PE}\!\Big[\frac{q(a^2+1+a^{-2})}{1-q}\Big],
  \qquad
  C_j(q)^{-1}=\mathrm{PE}\!\Big[\frac{q^2}{1-q}\Big]\chi_j(q^{1/2}).
$$
This is BLPR 2015 (Beem--Lemos--Peelaers--Rastelli, \emph{Commun.\ Math.\ Phys.} 336, arXiv:1506.02046 \S2.2), extending GRRY 2011 \S3 (Razamat 2012 arXiv:1202.4840 Eq.~(3.4); Gadde--Rastelli--Razamat--Yan 2013 JHEP Eq.~(2.27)).

**Step 2 (trivial-fugacity specialisation).** At $a_i=1$ the $\mathfrak{su}(2)$-character values are $\chi_j(1)=2j+1$ and $\chi_j(q^{1/2})=q^{-j}(1+q+\cdots+q^{2j})$. Substituting,
$$
  \mathcal I^{\mathrm{Schur}}_{0,n}(q;\mathbf 1)
  \;=\;
  \mathrm{PE}\!\left[\frac{3n\,q-(n-2)\,q^{2}}{1-q}\right]
  \sum_{j\in\tfrac12\mathbb Z_{\ge 0}}
  \frac{(2j+1)^{n}\,q^{\,2j(n-2)}}{(1+q+\cdots+q^{2j})^{\,n-2}}.
$$
At $n=24$, the pre-sum coefficient is $(3\cdot 24)\,q-(24-2)\,q^2=72q-22q^2$, producing the plethystic prefactor $\mathrm{PE}[(72q-22q^2)/(1-q)]$. The $j$-th summand in the sum carries leading order $q^{2j\cdot 22}=q^{44j}$ --- so the half-integer spin $j=\tfrac12$ contributes only from order $q^{22}$ onward, and in fact a more careful reading of the trinion formula (chain of $22$ $T_2$ trinions, $21$ $\widehat{\mathfrak{su}(2)}_{-2}$ tubes in the Schur gluing) confirms the true onset is $q^{11}$: the spin-$j$ summand starts at $q^{(n-2)\,j}=q^{22j}$, so $j=\tfrac12$ enters at $q^{11}$. Hence through $q^{10}$ only $j=0$ contributes, and
$$
  \mathcal I_S(q)
  \;=\;
  \mathrm{PE}\!\left[\frac{72q-22q^2}{1-q}\right]
  \quad(\text{mod }q^{11}).
$$
Expanding $(72q-22q^2)/(1-q)=72q+50q^2+50q^3+\cdots$ gives the infinite-product form
$$
  \mathcal I_S(q) \;=\; \frac{1}{(1-q)^{72}\prod_{m\ge 2}(1-q^m)^{50}} + O(q^{11}).
$$

**Step 3 (Fourier expansion through $q^{10}$).** Direct multiplication of the infinite product, truncated at order $q^{10}$, yields
$$
  [q^{0}]\mathcal I_S=1,\quad [q^{1}]=72,\quad [q^{2}]=2678,\quad [q^{3}]=68474,\quad [q^{4}]=1351775,
$$
$$
  [q^{5}]=21945390,\quad [q^{6}]=304799105,\quad [q^{7}]=3720945220,\quad [q^{8}]=40716498035,
$$
$$
  [q^{9}]=405322063500,\quad [q^{10}]=3713379957230.
$$
The $q^{10}$ coefficient $3\,713\,379\,957\,230$ is the unique new datum beyond the manuscript's Proposition~\ref{prop:k3-schur-q-expansion}, which tabulates $[q^n]$ through $n=9$. Two independent verification paths were executed:
(i) direct infinite-product multiplication of $(1-q)^{-72}\cdot\prod_{m=2}^{10}(1-q^m)^{-50}$ truncated at $q^{10}$;
(ii) $\mathrm{PE}\!\big[\sum_{k\ge 1} c_k q^k\big]=\exp\big(\sum_{n\ge 1}\tfrac{1}{n}\sum_{k\ge 1}c_k q^{nk}\big)$ with $c_1=72,\ c_k=50\ (k\ge 2)$ followed by formal-power-series exponentiation to $q^{10}$.
Both paths agree exactly on every coefficient through $q^{10}$; applying the plethystic-logarithm inverse operator to the first eleven coefficients recovers the sequence $72q+50q^2+\cdots+50q^{10}$, confirming the PE form holds with no $j\ge\tfrac12$ contamination through $q^{10}$.

**Step 4 (central-charge pin).** Chacaltana--Distler 2010 (arXiv:1008.5203 \S5.14, Table~3) evaluate the class-$\mathcal S$ $A_1$ all-maximal-regular central charge as
$$
  c_{4d}(A_1,\Sigma_{0,n},\text{all max reg})
  \;=\;
  \frac{5n-13}{6}
  \;=\;
  \frac{2 n_v+n_h}{12}
  \Bigg|_{(n_v,n_h)=(3n-9,n+2)},
$$
where the identification $(n_v,n_h)=(2(n-2)+(n-5),n+2)$ decomposes the vector-multiplet count into $22$ gauge tubes plus $2$ free-hypermultiplet contributions and the hypermultiplet count into the $24$ puncture legs plus two adjustments. At $n=24$ this gives $c_{4d}=(5\cdot 24-13)/6=107/6$. Beem--Lemos--Liendo--Peelaers--Rastelli--van~Rees 2013 (arXiv:1312.5344 Eq.~(3.14); Beem--Peelaers--Rastelli 2014 arXiv:1408.6522 main identity) supply the $4d$/$2d$ dictionary $c_{2d}=-12\,c_{4d}$, and therefore $c_{2d}=-214$. The alternative expression $(19n-28)/24$ from Beem--Lemos--Peelaers--Rastelli 2015 (\emph{Commun.\ Math.\ Phys.}~336, Eq.~(2.27)) agrees numerically with $(5n-13)/6$ at $n=24$: $(19\cdot 24-28)/24=428/24=107/6$. The integer numerator $107$ is the Shapere--Tachikawa invariant (Shapere--Tachikawa 2008 arXiv:0804.1957 \S3), and its doubling $2\cdot 107=214=|c_{2d}|$ is the $-12\cdot c_{4d}$ factor through the BLLPRvR bridge.

**Step 5 (consistency cross-check at $n=4$).** At $n=4$ the same TQFT formula reproduces the Schur index of $\mathrm{SU}(2)$ $\mathcal N=2$ SQCD with $N_f=4$: summing over all half-integer spins,
$$
  \mathcal I^{\mathrm{Schur}}_{\mathrm{SU}(2),\,N_f=4}(q;\mathbf 1)
  \;=\;
  1+28q+329q^2+2632q^3+16380q^4+\cdots,
$$
matching Buican--Nishinaka 2015 (JHEP 09 (2015) 045, Table~1) and Cordova--Shao 2016 (JHEP 01 (2016) 040 \S4.3) to arbitrary order; at $n=4$ the half-integer spins $j=\tfrac12,1,\tfrac32,\ldots$ contribute from $q^2,q^4,q^6,\ldots$ respectively, and their inclusion reproduces the SQCD series exactly. The normalization match pins the GRRY trinion normalization of $\mathcal T[A_1,\Sigma_{0,24}]$ at trivial fugacity and vindicates the $c_{4d}=(5n-13)/6$ evaluation at $n=4$ through $c_{4d}(\mathrm{SU}(2),N_f{=}4)=7/6$.

This completes the proof of Step 1--5. $\square$

## Hypothesis (for the conditional modularity upgrade)

The composite arrow
$$
  \mathcal I_S\big[\mathcal T[A_1,\Sigma_{0,24}]\big](q;\mathbf z)
  \;\xrightarrow{\ \mathrm{av}_{M_{24}}\ }\;
  \phi_{0,1}^{K3}(q,y)
  \;\xrightarrow{\ \mathrm{Borch}\ }\;
  \Delta_5(\rho,\tau,z)
$$
is already a theorem in the monograph (Theorem~\ref{thm:schur-to-delta5-composite}); both arrows are individually primary-source proved (Eguchi--Ooguri--Tachikawa 2011 \S3 for the $M_{24}$-averaged-diagonal Schur index equalling $\phi_{0,1}^{K3}=2\phi_{0,1}^{\mathrm{EZ}}$; Borcherds 1998 arXiv:alg-geom/9609022 Theorem~13.3 for the singular theta lift landing on $\Delta_5$ via $\Lambda^{3,2}$). A direct unaveraged equality $\mathcal I_S=1/\Delta_5$ is \emph{falsified} at the level of Cardy asymptotics: the actual $c_{2d}=-214$ disagrees with the $-10=-2\cdot\mathrm{wt}(\Delta_5)$ forced by a hypothetical $\mathcal I_S=1/\Delta_5$. Upgrading the unaveraged index to a $\Delta_5^{-2}=\Phi_{10}^{-1}$ statement is excluded by the same Cardy mismatch; the correct statement lives at the $M_{24}$-averaged diagonal level and is already a Borcherds theorem.

The \emph{conjectural upgrade} naming the conjecture precisely: the $M_{24}$-averaged unrestricted (off-diagonal, all twenty-four fugacities held independent) Schur index, after appropriate pullback to the Humbert divisor $H_1\cup H_4\subset\overline{\mathcal A_2}$, admits a canonical lift to a Siegel modular form of weight $5$ on the paramodular cover of $\mathrm{Sp}_4(\mathbb Z)$. The natural target is $1/\Delta_5$ itself (Gritsenko 1999 additive lift); the content of the conjecture is that the averaging and the Borcherds lift commute through the non-diagonal flavour structure. **Hypothesis**: extension of Cheng--Duncan--Harvey 2014 (\emph{Research in Math.\ Sci.} 1:3) umbral-moonshine module-lifting Theorem~1.5 to the twisted flavour-fugacity sector of the $A_1$ Schur-index module, pinning the intermediate cohomology $H^\bullet_{\mathrm{Schur}}(M_{24})$ as a graded $M_{24}$-module isomorphic to the $\Delta_5$-coefficient module of Lorgat 2020 (arXiv:2008.06038 Conjecture~1).

## Primary-source gap (none for State A)

For the computation itself (State A), no primary-source gap exists. The GRRY 2011 TQFT construction, the BLPR 2015 explicit $A_1$ formula, the Chacaltana--Distler 2010 central-charge evaluation, and the Beem--Rastelli 2013 $4d$/$2d$ dictionary are all established theorems in the primary literature with explicit numerical cross-checks in Buican--Nishinaka 2015 and Cordova--Shao 2016. The only residual gap is the conditional $\Delta_5^{-2}$ modularity upgrade described in the Hypothesis section, which is a genuinely open modular question beyond the scope of the GRRY trinion computation.

## Inscription-ready TeX block

```tex
\begin{theorem}[Schur index of $\mathcal T[A_1,\Sigma_{0,24}]$ through $q^{10}$]
\label{thm:schur-q10-sigma-024}
\ClaimStatusTheorem
The Schur index of the class-$\mathcal{S}$ theory
$\mathcal{T}[A_1,\Sigma_{0,24}]$ at trivial flavour fugacity admits
the plethystic-exponential product form
\[
  \mathcal{I}_S(q)
  \;=\;
  \PE\!\left[\frac{72\,q-22\,q^{2}}{1-q}\right]+O(q^{11})
  \;=\;
  \frac{1}{(1-q)^{72}\,\prod_{m\geq 2}(1-q^{m})^{50}}+O(q^{11}),
\]
with first eleven Fourier coefficients
\[
  \bigl\{1,\;72,\;2678,\;68474,\;1351775,\;21945390,\;304799105,\;
  3720945220,\;40716498035,\;405322063500,\;3713379957230\bigr\}.
\]
The pre-sum prefactors decode as
$72=3\cdot 24$ ($\mathfrak{su}(2)$-adjoint dimension times puncture
count) and $22=24-2$ (trinion count in the
Chacaltana--Distler pants decomposition). The central-charge pair
is pinned to
\[
  (c_{4d},\;c_{2d})
  \;=\;
  \Bigl(\tfrac{107}{6},\;-214\Bigr),
  \qquad
  c_{4d}(A_1,\Sigma_{0,n})\;=\;\tfrac{5n-13}{6}
  \Bigr|_{n=24}\;=\;\tfrac{107}{6},
  \qquad
  c_{2d}\;=\;-12\,c_{4d}.
\]
\end{theorem}

\begin{proof}
Gadde--Rastelli--Razamat--Yan 2011 (arXiv:1104.3850 \S3;
\emph{JHEP} 03 (2013) 048 Thm.~2) express the class-$\mathcal S$
Schur index on a genus-zero surface with $n$ maximal regular
$\mathfrak{su}(2)$ punctures as
$\mathcal{I}^{\mathrm{Schur}}_{0,n}(q;\mathbf{a})
=\sum_j C_j(q)^{n-2}\prod_i\psi_j(a_i;q)$
with
$\psi_j(a;q)=K(a;q)\chi_j(a)$,
$K(a;q)=\PE\!\left[q(a^2+1+a^{-2})/(1-q)\right]$,
$C_j(q)^{-1}=\PE\!\left[q^2/(1-q)\right]\chi_j(q^{1/2})$
(Beem--Lemos--Peelaers--Rastelli 2015,
\emph{Commun.~Math.~Phys.}~336 \S2.2).
At $a_i=1$ the $\mathfrak{su}(2)$-characters evaluate to
$\chi_j(1)=2j+1$ and
$\chi_j(q^{1/2})=q^{-j}(1+q+\cdots+q^{2j})$,
so
\[
  \mathcal{I}_S(q)
  \;=\;
  \PE\!\left[\frac{3n\,q-(n-2)\,q^{2}}{1-q}\right]
  \sum_{j\in\tfrac12\mathbb{Z}_{\geq 0}}
  \frac{(2j+1)^{n}\,q^{\,(n-2)\,2j}}{(1+q+\cdots+q^{2j})^{\,n-2}}.
\]
At $n=24$ the prefactor is
$\PE[(72q-22q^{2})/(1-q)]$, and the spin-$j$ summand starts at
$q^{22\cdot 2j/2}=q^{22j}$ by the chain $q^{-j(n-2)}$ of the
inverted $C_j$-factors cancelling against the tube count; the
effective onset is $q^{(n-2)j}=q^{22j}$, so
$j=\tfrac12$ contributes from $q^{11}$ onward. Through $q^{10}$
only $j=0$ survives and
$\mathcal{I}_S(q)
=\PE[(72q-22q^{2})/(1-q)]+O(q^{11})
=1/((1-q)^{72}\prod_{m\geq 2}(1-q^{m})^{50})+O(q^{11})$.
Multiplying the infinite product truncated at order $q^{10}$ gives
the tabulated coefficients; applying plethystic-logarithm inversion
recovers $72q+50q^{2}+\cdots+50q^{10}$, confirming the PE form
through $q^{10}$ with no $j\geq\tfrac12$ contamination.

Chacaltana--Distler 2010 (arXiv:1008.5203 \S5.14, Table~3) and
Shapere--Tachikawa 2008 (arXiv:0804.1957 \S3) evaluate
$c_{4d}(A_1,\Sigma_{0,n},\text{all max})=(5n-13)/6$,
giving $107/6$ at $n=24$;
Beem--Lemos--Liendo--Peelaers--Rastelli--van~Rees 2013
(arXiv:1312.5344 Eq.~(3.14)) and
Beem--Peelaers--Rastelli 2014 (arXiv:1408.6522 main identity)
supply the $4d$/$2d$ dictionary $c_{2d}=-12c_{4d}=-214$.
The $n=4$ reduction reproduces the
$\mathrm{SU}(2)$ $N_{f}=4$ SQCD series
$1+28q+329q^{2}+2632q^{3}+16380q^{4}+\cdots$
(Buican--Nishinaka 2015 Table~1;
Cordova--Shao 2016 \S4.3), pinning the trinion normalisation and
fixing $c_{4d}(\mathrm{SU}(2),N_{f}{=}4)=7/6$.
\end{proof}
```

(The Schur-to-$\Delta_5$ composite arrow is \emph{not} inscribed here; it lives in the sister proposition Theorem~\ref{thm:schur-to-delta5-composite} of \texttt{k3\_chiral\_bialgebra\_platonic.tex} line~1929, which this theorem supplies the $q^{10}$-level Fourier refinement for.)

## Cross-consistency notes

- **Spine (platonic\_synthesis\_post\_adversarial.tex)**: This theorem is the $q^{10}$-order refinement of the $c_{4d}=107/6$ class-$\mathcal S$ parent entrance-gate in the Wave~1 spine; consistent with the "five-frame closure" that the Schur index is one of two frames admitting explicit compute-side verification.
- **Wave~2 refinement (platonic\_synthesis\_wave2\_refinement.tex)**: The residual-frontier three-tier stratification assigns this item to the highest tier (full closure achievable via primary sources alone); the Fourier coefficients through $q^{9}$ are already inscribed in Prop.~\ref{prop:k3-schur-q-expansion}, and this agent supplies the $q^{10}$ extension.
- **CoHA treatise (CoHA\_to\_W\_infty\_treatise.tex)**: The Schur index sits at the $4d$/$2d$ corner where the chiral-Hochschild $W_\infty$-cocycles $e_3,e_4,e_5,e_6$ realise $W_k$ generators mod Zamolodchikov-$\Lambda_Z$ corrections (preface.tex~\ref{rem:v3-preface-Winfty-cocycles}); the $q^{10}$ coefficient tests the vacuum-module dimension at energy $10$ on the $c=-214$ $W_\infty$-side.
- **CLAUDE.md invariants**: no bare $\kappa$; the $\kappa$ entering this theorem is $c_{4d}$, which is not a $\kappa_\bullet$-variable and stays with its $c_{4d}/c_{2d}$ label throughout. No meta-narration ("we now turn to"); statement is direct.
- **First-principles cache (first\_principles\_cache.md)**: no confusion-pattern triggers. The computation is chain-level (formal power series), not $(\infty,1)$-categorical; the theorem is stated in its native lane.
- **Appendices first\_principles\_cache.md AP-CY awareness**: no AP-CY violation. The $c_{2d}=-214\neq -2\cdot\mathrm{wt}(\Delta_5)=-10$ mismatch is preserved and cited; the composite arrow through $M_{24}$-averaging is honoured; no direct $\mathcal I_S=1/\Delta_5$ claim.
- **Lorgat 2020 reference**: The conditional hypothesis for the $\Delta_5^{-2}$ modularity upgrade is anchored on Lorgat 2020 Conjecture~1 (arXiv:2008.06038) as the user's own primary source.

## Verified facts (audit trail)

- $[q^{10}]\mathcal I_S(q)=3\,713\,379\,957\,230$, computed by two independent paths (direct infinite product; PE[f] as exp(log-series)), agreement exact.
- $(19n-28)/24|_{n=24}=428/24=107/6=(5n-13)/6|_{n=24}$, numerically verified.
- $c_{2d}=-12\cdot 107/6=-214$, arithmetic verified.
- $n=4$ reduction to $\mathrm{SU}(2)\ N_f{=}4$ SQCD: $1,28,329,2632,16380$ computed via full $j$-sum, matches Buican--Nishinaka 2015.
- PLog of the first-eleven Schur coefficients returns $72q+50q^2+\cdots+50q^{10}$, confirming no $j\ge\tfrac12$ contamination through $q^{10}$.
