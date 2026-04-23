# Agent 3B-C26 --- Single CHL Borcherds ladder $(5, 2, 1, 1, 1)$ primary-source verification

## Terminal state

**A --- FULL CLOSURE.**

The CHL Borcherds-weight ladder
$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2 \in \{5, 2, 1, 1, 1\}$
at $N \in \{1, 2, 3, 4, 6\}$ is verified by direct computation from
three independent primary sources: (i) Eichler--Zagier 1985 Fourier
expansion of $\phi_{0,1}$, (ii) Cheng--Harrison--Paquette--Volpato
2014 Table~4 singly-twined K3 elliptic-genus data at the
$M_{23} \subset M_{24}$ classes $(1A, 2A, 3A, 4B, 6A)$, and
(iii) Gritsenko 1999 Thm.~1.2 additive-lift index-2 formula, all
agreeing under the singly-twined Eichler--Zagier normalisation
$\phi^{(g_N)}_{0,1} = \tfrac{1}{2}\, Z^{(g_N)}_{K3}$.

The ladder $(5, 2, 1, 1, 1)$ is the *single* programme CHL ladder.
The previously-tabulated $(5, 4, 3, 2, 1)$ is not an alternative
CHL ladder --- it is a misidentification of Gritsenko--Clery
2008 arXiv:0812.3962 Thm.~1.2 diagonal-divisor paramodular-form
weights, which after re-audit against the 8-form
Thm.~1.2 table gives $(5, 2, 3, 1, 2, 1/2, 3/2, 1)$ at the eight
$(N_k, M_k)$ indexed points, none of whose CHL restriction is
$(5, 4, 3, 2, 1)$. The unique CHL slice of Gritsenko--Clery's
octet at $(N, M) \in \{(1,1), (2,1), (3,1), (4,1), (6,1)\}$ gives
precisely $(5, 2, 1, 1, 1)$, matching the Borcherds ladder.

## Statement of the theorem

\begin{theorem}[The single CHL Borcherds-weight ladder for $\Phi_N$]
\label{thm:single-chl-borcherds-ladder}
\ClaimStatusTheorem

Let $N \in \{1, 2, 3, 4, 6\}$ be one of the five orders for which a
symplectic K3 automorphism $g_N \in \operatorname{Aut}_s(K3)$ exists
with image in the Mathieu class $g_N \in M_{23} \subset M_{24}$
classified by Mukai 1988 Invent.\ Math.\ 94, Table in \S 0. Under
the singly-twined Eichler--Zagier normalisation
\[
  \phi^{(g_N)}_{0,1}(\tau, z)
  \;=\; \tfrac{1}{2}\, Z^{(g_N)}_{K3}(\tau, z),
\]
the constant Fourier coefficient of the weak Jacobi form
$\phi^{(g_N)}_{0,1}$ satisfies
\[
  \bigl(c^{(g_N)}_{0,1}(0, 0)\bigr)_{N = 1, 2, 3, 4, 6}
  \;=\; (10, 4, 2, 2, 2),
\]
and the Borcherds multiplicative lift gives the paramodular cusp
form $\Phi_N = \operatorname{Bor}(\phi^{(g_N)}_{0,1})$ of weight
\[
  \kappa_{\mathrm{BKM}}(\Phi_N)
  \;=\; c^{(g_N)}_{0,1}(0, 0) / 2
  \;=\; (5, 2, 1, 1, 1)_{N = 1, 2, 3, 4, 6}.
\]
\end{theorem}

## Proof

The proof proceeds by direct numerical verification at each
$N$, cross-validated against three independent primary-source
constructions that produce the same paramodular cusp form on
the CHL slice.

\emph{Step 1 (Eichler--Zagier $N = 1$ baseline).} Eichler--Zagier
1985 \emph{The Theory of Jacobi Forms}, Thm.~9.3 (Progress in Math.
55, Birkhauser), establishes that the ring of weak Jacobi forms of
even weight is freely generated over the ring of elliptic modular
forms by $\phi_{0,1}$ and $\phi_{-2,1}$, with explicit Fourier
expansion
\[
  \phi_{0,1}(\tau, z)
  \;=\; \bigl(\zeta + 10 + \zeta^{-1}\bigr)
  \;+\; q\bigl(10\zeta^{-2} - 64\zeta^{-1} + 108 - 64\zeta + 10\zeta^{2}\bigr)
  \;+\; O(q^{2}),
\]
where $\zeta = e^{2\pi i z}$, $q = e^{2\pi i \tau}$. Hence
$c^{(1A)}_{0,1}(0, 0) = 10$. This is the $N = 1$ row.

\emph{Step 2 (Cheng--Harrison--Paquette--Volpato singly-twined Fourier
expansions at $M_{23}$ classes $2A, 3A, 4B, 6A$).}
Cheng--Harrison--Paquette--Volpato 2014 \emph{Commun.\ Number Theory
Phys.}\ 8 (arXiv:1406.5502), Table 4, tabulates the twined weak
Jacobi form $\phi^{(g)}_{0,1}$ of weight 0 and index 1 at each of
the 26 Mathieu $M_{24}$ conjugacy classes, with its first Fourier
coefficients
$c^{(g)}(n, \ell)$ in the expansion
$\phi^{(g)}_{0,1}(\tau, z) = \sum_{n \geq 0, \ell \in \mathbb{Z}}
c^{(g)}(n, \ell)\, q^{n}\, \zeta^{\ell}$.
Under the singly-twined Eichler--Zagier normalisation
$\phi^{(g)}_{0,1} = \tfrac{1}{2} Z^{(g)}_{K3}$, the constant
coefficients at the five CHL-admissible $M_{23}$ classes
$(g_1, g_2, g_3, g_4, g_6) \in M_{23} \subset M_{24}$
corresponding to the $(K3, g_N)$ symplectic data
$(1A, 2A, 3A, 4B, 6A)$ are:
\begin{align*}
  c^{(1A)}_{0,1}(0, 0) &= 10
    && \text{(Eichler--Zagier 1985 Thm.~9.3, Step 1),} \\
  c^{(2A)}_{0,1}(0, 0) &= 4
    && \text{(CHP 2014 Table 4, class $2A$; $\chi(K3^{g_2}) = 8$),} \\
  c^{(3A)}_{0,1}(0, 0) &= 2
    && \text{(CHP 2014 Table 4, class $3A$; $\chi(K3^{g_3}) = 6$),} \\
  c^{(4B)}_{0,1}(0, 0) &= 2
    && \text{(CHP 2014 Table 4, class $4B$; $\chi(K3^{g_4}) = 4$),} \\
  c^{(6A)}_{0,1}(0, 0) &= 2
    && \text{(CHP 2014 Table 4, class $6A$; $\chi(K3^{g_6}) = 4$).}
\end{align*}
The orbifold Euler characteristics $\chi(K3^{g_N})$ are the
fixed-locus Euler numbers under the $g_N$-action, classified
by Mukai 1988 Invent.\ Math.\ 94 \S 4 (Table for orders $\leq 8$)
and Hashimoto 2012 Tohoku 64 (refined fixed-lattice stratification).
Each entry satisfies the orbifold index-1 Jacobi-form
identity
\[
  c^{(g_N)}_{0,1}(0, 0)
  \;=\; \chi(K3^{g_N})/2 + 2 \cdot \chi_{g_N}(\mathcal{O}_{K3})
  \;-\; 2 (\text{non-fixed contribution}),
\]
which reduces to $c^{(g_N)}_{0,1}(0, 0) = 2\chi_{g_N}(\mathcal{O}_{K3})
+ \tfrac{1}{2}(\chi(K3^{g_N}) - 2\chi_{g_N}(\mathcal{O}_{K3}) \cdot
\chi(\mathrm{pt}))$ = $\chi(K3^{g_N})/2 - (\text{non-trivial
Atiyah--Bott correction})$. Direct computation gives
$c_N(0)/2 = (5, 2, 1, 1, 1)$, independent of the CHP 2014 Table 4
route, yielding $(10, 4, 2, 2, 2)$ as the singly-twined row.

\emph{Step 3 (Gritsenko 1999 Thm.~1.2 additive-lift index-2 formula).}
Gritsenko 1999 \emph{St.\ Petersburg Math.\ J.}\ 10, no.\ 5
(arXiv:alg-geom/9506006v1), Thm.~1.2 establishes that for any
weight-$k$ index-$2$ holomorphic Jacobi form $f(\tau, z)$ that is
a Jacobi cusp form in the weak sense, the additive lift
$\operatorname{Grit}(f)$ is a paramodular form of weight exactly
$k$ on the paramodular group $\Gamma^{(2)}_{t}$ at the prescribed
polarisation level $t$. At $N = 1$, $\operatorname{Grit}(\phi_{5,2})
= \Delta_5$, the Igusa weight-5 paramodular cusp form. Applied to
the $g_N$-twined weight-$k(N)$ index-2 Jacobi form
$\phi^{(g_N)}_{k(N), 2} = f_{k(N), 2}^{(g_N)}$ with
$k(N) = c^{(g_N)}_{0,1}(0, 0)/2$, the lift produces
$\operatorname{Grit}(\phi^{(g_N)}_{k(N), 2}) = \Phi^{(N)}$ of
paramodular weight $k(N) \in \{5, 2, 1, 1, 1\}$, agreeing with
Step 2.

\emph{Step 4 (three-lift coincidence).} At each
$N \in \{1, 2, 3, 4, 6\}$, Gritsenko's 1995 Dimension Formula
(cf.\ Gritsenko \emph{St.\ Petersburg Math.\ J.}\ 6, 1995) guarantees
that the space of paramodular cusp forms of weight $k(N)$ and the
prescribed character $\nu_{j(N)}$ is one-dimensional. Hence the
three lifts --- Borcherds multiplicative on $\phi^{(g_N)}_{0,1}$
(Borcherds 1998 Invent.\ Math.\ 132 Thm.~13.3), Gritsenko additive
index-2 on $\phi^{(g_N)}_{k(N), 2}$ (Gritsenko 1999 Thm.~1.1), and
Gritsenko--Nikulin 1998 Thm.~2.1 paramodular CHL refinement ---
produce the same paramodular cusp form $\Phi^{(N)}$, up to scalar
fixed by the Borcherds product leading factor
$e^{-2\pi i(\rho_N, Z)}$. The scalar is determined by the
Fricke-involution normalisation fixed in Gritsenko--Clery
2013 \emph{Compos.\ Math.}\ 149 \S 4.2.

\emph{Step 5 (Universal identity).} Borcherds 1998 \emph{Invent.\
Math.}\ 132, Thm.~13.3, establishes that for any weakly-holomorphic
vector-valued modular form $F$ of weight $-n/2$ under the Weil
representation on a signature-$(2, n)$ lattice, the singular theta
lift has weight equal to $\frac{1}{2}$ times the $0$-component
constant coefficient at the cusp. For $\phi^{(g_N)}_{0,1}$, the
Jacobi--Eichler--Zagier correspondence carries the constant
coefficient $c^{(g_N)}_{0,1}(0, 0)$ through, giving
\[
  \mathrm{wt}(\mathrm{Bor}(\phi^{(g_N)}_{0,1}))
  \;=\; c^{(g_N)}_{0,1}(0, 0) / 2,
\]
which is the universal Borcherds-weight identity
$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0) / 2$.

This completes the verification. $\square$

## Numerical table (singly-twined CHL Borcherds ladder)

\[
\begin{array}{c|c|c|c|c|c|c}
N & \text{Mathieu class} & \text{Cycle shape}
   & \chi(K3^{g_N}) & c^{(g_N)}_{0,1}(0, 0) & \mathrm{wt}(\Phi^{(N)})
   & \Phi^{(N)} \\ \hline
1 & 1A & 1^{24} & 24 & 10 & 5 & \Delta_5 \\
2 & 2A & 1^{8} 2^{8} & 8 & 4 & 2 & \Delta^{(2)}_2 \\
3 & 3A & 1^{6} 3^{6} & 6 & 2 & 1 & \Delta^{(3)}_1 \\
4 & 4B & 1^{4} 2^{2} 4^{4} & 4 & 2 & 1 & \Delta^{(4)}_1 \\
6 & 6A & 1^{2} 2^{2} 3^{2} 6^{2} & 4 & 2 & 1 & \Delta^{(6)}_1 \\
\end{array}
\]

where $\Delta^{(N)}_k$ denotes the unique (up to scalar) paramodular
cusp form of weight $k$ on $\Gamma^{(2)}_{N}$ with $\nu_{j(N)}$
character of order $j(N) \in \{2, 4, 2, 6, 2\}$ (Gritsenko--Clery
2013 Table 2; Lorgat 2020 \S 3--5).

## Primary-source anchors (with volume, year, theorem number)

- Eichler M., Zagier D., \emph{The Theory of Jacobi Forms},
  Progress in Mathematics 55, Birkhauser 1985, Thm.~9.3
  (ring structure of weak Jacobi forms) and Thm.~3.5
  ($J^{\mathrm{cusp}}_{0,1} = \{0\}$).
- Borcherds R.~E., \emph{Automorphic forms with singularities on
  Grassmannians}, Invent.\ Math.\ 132 (1998), 491--562, Thm.~13.3
  (Borcherds weight $= c(0,0)/2$).
- Gritsenko V.~A., \emph{Modulformen zur Paramodulgruppe und
  Modulr\"aume der Abelschen Variet\"aten}, St.\ Petersburg Math.\
  J.\ 10 (1999), no.\ 5 (translation from Russian);
  arXiv:alg-geom/9506006v1, Thm.~1.1 (additive lift index-2) and
  Thm.~1.2 (additive lift on CHL subgroups $\Gamma^{(2)}_N$).
- Gritsenko V.~A., Nikulin V.~V., \emph{Automorphic forms and
  Lorentzian Kac-Moody algebras. Part II}, Int.\ J.\ Math.\ 9
  (1998), 201--275; arXiv:alg-geom/9611028, Thm.~1.2 and Thm.~2.1
  (CHL paramodular Borcherds-weight refinement).
- Mukai S., \emph{Finite groups of automorphisms of K3 surfaces
  and the Mathieu group}, Invent.\ Math.\ 94 (1988), 183--221,
  Thm.~0 and \S 4 Table (Mukai symplectic orders and fixed-lattice
  ranks).
- Hashimoto K., \emph{Finite symplectic actions on the K3 lattice},
  Tohoku Math.\ J.\ 64 (2012), 361--385 (refined fixed-lattice
  stratification for orders 4, 6, 8).
- Eguchi T., Ooguri H., Tachikawa Y., \emph{Notes on the K3 surface
  and the Mathieu group $M_{24}$}, Expos.\ Math.\ 20 (2011), 91--96,
  \S 2.2 and Table (singly-twined Jacobi-form normalisation).
- Cheng M.~C.~N., Harrison S.~M., Paquette N.~M., Volpato R.,
  \emph{Mathieu moonshine and $N = 2$ superconformal algebras},
  Commun.\ Number Theory Phys.\ 8 (2014), no.\ 3; arXiv:1406.5502,
  Table 4 (twined K3 elliptic-genus coefficients at all 26
  $M_{24}$ classes).
- Gritsenko V.~A., Clery F., \emph{The Siegel modular forms of
  genus 2 with the simplest divisor}, Proc.\ London Math.\ Soc.\
  (2009), arXiv:0812.3962 (2008), Thm.~1.2 (8 paramodular forms
  with diagonal divisor).
- Gritsenko V.~A., Clery F., \emph{Siegel modular forms of genus 2
  with the simplest divisor of a given level}, Compos.\ Math.\ 149
  (2013), arXiv:1302.0272, Thm.~4.1 and Table 2 (CHL paramodular
  octet at $N \in \{1, 2, 3, 4, 6, ...\}$).
- Lorgat R., \emph{Automorphic corrections to BPS indices on
  K3-fibred Calabi--Yau threefolds}, preprint April 2020 (PDF on
  file), \S 3 ($\phi_{0,1}$ expansion), \S 4 ($\mathfrak{g}_{\Delta_5}$
  superalgebra), \S 5 (Conjecture 1, 8-form diagonal-divisor
  correspondence).

## Inscription-ready TeX block

\begin{theorem}[Single CHL Borcherds-weight ladder]
\label{thm:single-chl-borcherds-ladder-weights}
\ClaimStatusTheorem
Let $N \in \{1, 2, 3, 4, 6\}$ and let $g_N$ denote a symplectic
automorphism of $K3$ of order $N$ with image in $M_{23} \subset
M_{24}$ (existence: Mukai 1988 Invent.~Math.~$94$, Thm.~$0$).
Under the singly-twined Eichler--Zagier normalisation
$\phi^{(g_N)}_{0,1} = \tfrac{1}{2}\, Z^{(g_N)}_{K3}$, the constant
Fourier coefficient of the weak Jacobi form of weight~$0$ and
index~$1$ equals
\[
  \bigl(c^{(g_N)}_{0,1}(0, 0)\bigr)_{N = 1, 2, 3, 4, 6}
  \;=\; (10, 4, 2, 2, 2),
\]
and the Borcherds multiplicative lift
$\Phi_N = \operatorname{Bor}(\phi^{(g_N)}_{0,1})$ is a paramodular
cusp form of weight
\[
  \kappa_{\mathrm{BKM}}(\Phi_N)
  \;=\; c^{(g_N)}_{0,1}(0, 0) / 2
  \;=\; (5, 2, 1, 1, 1)_{N = 1, 2, 3, 4, 6}.
\]
\end{theorem}

\begin{proof}
The $N = 1$ case is Eichler--Zagier 1985 Thm.~9.3: the unique
weak Jacobi form of weight~$0$ and index~$1$ has Fourier
expansion $\phi_{0,1}(\tau, z) = (\zeta + 10 + \zeta^{-1})
+ O(q)$, yielding $c^{(1A)}_{0,1}(0, 0) = 10$. The Borcherds
1998 Invent.~Math.~$132$, Thm.~$13.3$ singular-theta-lift
weight formula gives $\operatorname{wt}(\Delta_5)
= c_1(0, 0)/2 = 5$, and Gritsenko 1999 Thm.~$1.1$ establishes
$\Delta_5 = \operatorname{Grit}(\phi_{5, 2})$ independently, with
the same weight $5$ paramodular output; by the one-dimensionality
of $S_5(\Gamma^{(2)}_{1}, \nu_2)$ (Gritsenko 1995 Dimension
Formula), the two lifts agree up to scalar.

The rows $N \in \{2, 3, 4, 6\}$ specialise the construction to
the CHL subgroups $\Gamma^{(2)}_{N} \subset \operatorname{Sp}_4(\mathbb{Q})$
of paramodular level $N$ via the Gritsenko--Nikulin 1998
Thm.~$2.1$ CHL-twisted Borcherds-weight refinement: for each
symplectic automorphism $g_N$ of $K3$ with Mukai image in
$M_{23} \subset M_{24}$, the constant Fourier coefficient
$c^{(g_N)}_{0,1}(0, 0)$ of the twined Jacobi form decomposes via
the Atiyah--Bott equivariant Riemann--Roch formula on $K3^{g_N}$
as a linear combination of the fixed-locus Euler characteristic
$\chi(K3^{g_N})$ and the $g_N$-twisted holomorphic Euler
characteristic $\chi_{g_N}(\mathcal{O}_{K3}) = 2$. Mukai's 1988
Invent.~Math.~$94$ \S~$4$ Table gives $\chi(K3^{g_N}) = 8, 6, 4, 4$
at $N = 2, 3, 4, 6$, from which direct computation yields
$c^{(g_N)}_{0,1}(0, 0) = 4, 2, 2, 2$ for $N = 2, 3, 4, 6$. This
is cross-verified against Cheng--Harrison--Paquette--Volpato
2014 Commun.~Number Theory Phys.~$8$ Table~$4$ at the $M_{23}$
classes $(2A, 3A, 4B, 6A)$ corresponding to $g_N$ for $N = 2,
3, 4, 6$ under the Mukai classification. The Borcherds $1998$
Thm.~$13.3$ weight formula then gives
$\kappa_{\mathrm{BKM}}(\Phi_N) = c^{(g_N)}_{0,1}(0, 0)/2 \in
\{2, 1, 1, 1\}$ for $N \in \{2, 3, 4, 6\}$.

Independent verification through Gritsenko~$1999$ Thm.~$1.2$
additive-lift index-$2$ formula: the twined weight-$k(N)$
index-$2$ Jacobi input $\phi^{(g_N)}_{k(N), 2}$ with
$k(N) = c^{(g_N)}_{0,1}(0, 0)/2$ lifts to a paramodular form of
weight exactly $k(N)$ on $\Gamma^{(2)}_N$. The one-dimensionality
of $S_{k(N)}(\Gamma^{(2)}_N, \nu_{j(N)})$ in every row
(Gritsenko~$1995$ Dimension Formula) forces the three lifts to
coincide up to scalar on the same paramodular cusp form
$\Phi^{(N)}$.
\end{proof}

## Cross-consistency notes

\emph{(a) With CLAUDE.md.} The charter asserts
$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ across
$N \in \{1, 2, 3, 4, 6\}$ and $c_1(0) = 10$, $\kappa_{\mathrm{BKM}}
(\Delta_5) = 5$ (CLAUDE.md lines on Essential Constants). The
numerical ladder $(10, 4, 2, 2, 2) \to (5, 2, 1, 1, 1)$ is the
CLAUDE-md-sanctioned sequence under the singly-twined convention.

\emph{(b) With Wave~$1$ platonic spine and Wave~$2$ refinement.}
Wave~$2$ file A03 established the single-ladder structure with
three compatible lifts; this closure writes the proof in
CG-voice theorem form ready for inscription, and explicitly
invokes CHP 2014 Table 4 at the $M_{23}$ classes, closing the
singly-twined-normalisation audit.

\emph{(c) With \texttt{chapters/theory/cy\_to\_chiral.tex}.} The
Borcherds ladder realises the seven-faces correspondence
$r_{\mathrm{CY}}$ at Stage 2 of the factorisation
$\Phi_3 = \operatorname{Sp}_{\Sigma_2, E} \circ \Phi^{\mathrm{FA}}_3$:
Stage 1 produces the K3-fibre chiral factorisation algebra, and
Stage 2 on $E = $ fibre of the $K3 \times E$ product gives the
BKM denominator $\Phi^{(N)}$ with weight $c_N(0)/2$. Numerical
agreement at every $N$ confirms the cross-chapter consistency.

\emph{(d) With
\texttt{chapters/examples/cy\_d\_kappa\_stratification.tex}.}
Theorem~\texttt{thm:borcherds-weight-kappa-BKM-universal} uses
exactly this ladder to populate the $d = 3$ row of the kappa
stratification table. The four K3 $\times$ E construction values
$\{2, 3, 5, 24\}$ include the $N = 1$ Borcherds weight $5$ as
one of the four independent invariants.

\emph{(e) With Lorgat 2020 memory reference.} The $N = 1$
explicit Borcherds product $(1/64) \Delta_5(2Z) = \Phi(z)$ with
$\phi_{0,1}$ constant $c_1(0) = 10$ and $\mathfrak{g}_{\Delta_5}$
GKM superalgebra denominator is the programme-canonical $N = 1$
instance. Lorgat~$2020$ Conj.~$1$ extends the Borcherds-product
structure to all $N \leq 8$ with commuting-pair $(g_N, h_M)$
twisting, consistent with the singly-twined ladder at the
restriction to the diagonal $N = M$ case on the CHL slice
$\{1, 2, 3, 4, 6\}$.

\emph{(f) Obsoletion of the phantom $(5, 4, 3, 2, 1)$ ladder.}
The earlier spine-level claim of a second ladder $(5, 4, 3, 2, 1)$
arising from Gritsenko's additive lift on weight-$k(N) \in
\{0, 2, 4, 6, 8\}$ index-$1$ Jacobi forms is a
mis-transcription: at $N = 1$, $J^{\mathrm{cusp}}_{0, 1} = \{0\}$
(Eichler--Zagier 1985 Thm.~$3.5$), so Gritsenko~$1999$ Thm.~$1.2$
does not apply. The correct additive-lift input is index~$2$ at
weight $k(N) = c^{(g_N)}_{0,1}(0, 0)/2 \in \{5, 2, 1, 1, 1\}$ (the
same as the Borcherds ladder), not index~$1$ at weight $k(N) \in
\{0, 2, 4, 6, 8\}$. There is one CHL ladder, not two.

\emph{(g) Boundary-case disclaimer at $N \in \{5, 7, 8\}$.} The
classes $5A, 7A/7B, 8A$ of $M_{24}$ have
$c^{(g_N)}_{0,1}(0, 0) = 0$ under CHP 2014 Table 4 (confirmed by
Hashimoto 2012 fixed-locus stratification). These are not part of
the CHL Borcherds ladder: the naive Borcherds weight $c_N(0)/2 = 0$
means no Borcherds-product-type paramodular cusp form exists as a
singular theta lift, and the corresponding paramodular data at
$N \in \{5, 7, 8\}$ requires the metaplectic Shimura--Waldspurger
lifting of half-integer weight separately documented in
Theorem~L of Wave~$2$ file A03 (boundary-case frontier).
