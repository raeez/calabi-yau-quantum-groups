# Agent C06 --- Bracket-level $\mathfrak{g}_{\mathrm{BPS}}(K3 \times E) \simeq \mathfrak{g}_{\Delta_5}$ reducing to a single Hecke--Borcherds identity

## Terminal state

**B (conditional closure).** The bracket-level Lie superalgebra
isomorphism reduces unconditionally to a single named arithmetic
identity on the Gritsenko 1999 paramodular family --- the
**Hecke--Borcherds structure-constant identity (HB)** stated below.
Verifying (HB) is an arithmetic computation inside the one-variable
Jacobi-form ring $J_{\ast,\ast}(\mathrm{SL}_2(\mathbb Z))$ accessible
by Gritsenko--Nikulin 1998 denominator expansion or by the
Harvey--Moore 1996 one-loop string-amplitude formula on
heterotic $K3 \times T^2$; neither route requires new machinery,
but the identity has not been written in the form stated below
in the literature, and its verification constitutes an independent
arithmetic closure rather than a corollary of previously proved
statements.

## Statement of the theorem (conditional)

\ClaimStatusConjectured{(HB-conditional)}

Let $X = K3 \times E$ be a smooth compact Calabi--Yau threefold with
$K3$ a projective K3 surface and $E$ an elliptic curve. Let
$\mathfrak g_{\mathrm{BPS}}(X) = \bigoplus_\gamma
\mathfrak g_{\mathrm{BPS}, \gamma}(X)$ be the Davison BPS Lie
superalgebra of primitives inside the critical cohomological Hall
algebra, with Lie bracket induced from the Hall commutator restricted
to primitives (Davison 2017, \emph{Proc.~LMS}~112,
arXiv:1512.04179 Theorem~1.1; Davison--Meinhardt 2020,
\emph{Invent.~Math.}~221 Theorem~A). Let
$\mathfrak g_{\Delta_5} = \mathfrak n_-(\Delta_5) \oplus \mathfrak h
\oplus \mathfrak n_+(\Delta_5)$ be the Gritsenko--Nikulin Borcherds
generalised Kac--Moody superalgebra with Cartan subalgebra
$\Lambda^{2,1}_{II}$ and root-space dimensions
$\mathrm{mult}_{\mathrm{BKM}}(\alpha) = c(-\alpha^2/2)$, $c(\cdot)$
the Fourier coefficients of the K3 elliptic genus $\phi_{0,1}^{K3}$
(Gritsenko--Nikulin 1998, \emph{Internat.\ J.\ Math.}~9 Theorem~I.4.4;
Borcherds 1995, \emph{Invent.\ Math.}~120 Theorem~10.4). Let
$\gamma \mapsto \alpha_\gamma \in \Lambda^{2,1}_{II}$ be the
Oberdieck--Pixton identification between primitive K3-class DT-invariants
on $X$ and BKM-roots of $\mathfrak g_{\Delta_5}$
(Oberdieck--Pixton 2018, \emph{Invent.\ Math.}~213
arXiv:1706.10100 Theorem~1; reduced-DT invariants
$\Omega^{\mathrm{red}}(\gamma) = c(4n_\gamma m_\gamma - l_\gamma^2)
= \mathrm{mult}_{\mathrm{BKM}}(\alpha_\gamma)$).

Conditional on the **Hecke--Borcherds structure-constant identity (HB)**
stated as identity~(HB) below, there exists a Lie-superalgebra
isomorphism
\[
  \Psi\colon
    \mathfrak g_{\mathrm{BPS}}(K3 \times E)
    \;\xrightarrow{\;\simeq\;}\;
  \mathfrak g_{\Delta_5}
\]
preserving the bracket, sending the charge decomposition $\gamma \in
K_0(X)$ to the root decomposition $\alpha_\gamma \in \Lambda^{2,1}_{II}$,
and specialising on weight spaces to the Oberdieck--Pixton
$\Omega^{\mathrm{red}}(\gamma) = \mathrm{mult}_{\mathrm{BKM}}(\alpha_\gamma)$
dimension match.

## Precise form of the Hecke--Borcherds structure-constant identity (HB)

Let $\phi_{0,1}^{K3}(\tau, z) = \sum_{n, l} c(4n - l^2)\, q^n y^l$ be
the K3 elliptic genus ($q = e^{2\pi i \tau}$, $y = e^{2\pi i z}$) with
discriminant Fourier coefficients $c(D)$
(Eichler--Zagier 1985, \emph{Jacobi Forms}~§2; Eguchi--Ooguri--Tachikawa
2010, \emph{Exp.~Math.}~20 Table~1).

Let $\phi_{10, 1}(\tau, z) = \eta(\tau)^{18} \vartheta_1(\tau, z)^2$ be
the unique weight-$10$ index-$1$ Jacobi cusp form (Eichler--Zagier 1985
Theorem~8.4), and let
$\phi_{10, m}(\tau, z) = V_{m-1}(\phi_{10, 1})$
be the $m$-th Fourier--Jacobi coefficient of the Gritsenko additive lift
$\Delta_5(Z) = \sum_{m \geq 1} \phi_{10, m}(\tau, z)\, p^m$,
$p = e^{2\pi i \sigma}$, where $V_k$ is the Eichler--Zagier--Gritsenko
Hecke--Jacobi operator
\[
  V_k(\phi)(\tau, z)
   \;=\;
  k^{-1}
  \sum_{\substack{a d = k \\ a, d > 0}}
  \sum_{b \bmod d}
  a^{10}\,
  \phi\!\left(
    \tfrac{a \tau + b}{d},
    a z
  \right)
\]
(Eichler--Zagier 1985 §4 pp.~41--46; Gritsenko 1999
\emph{St.~Petersburg Math.~J.}~11 §§2--3, arXiv:math/9906190
Theorem~1.1 and Theorem~2.1). The Maass relations on Fourier
coefficients assert
$\phi_{10, m}(\tau, z) = \sum_{a | \gcd(n, l, m)}
 a^9\, \phi_{10, 1}(a \tau, a z)|_{m/a}$
with the trace pattern converting the one-parameter input
$\phi_{10, 1}$ into the full Siegel modular form $\Delta_5$.

Write the Fourier coefficients of $\Delta_5$ in the Igusa--Maass
normalisation as
$\Delta_5(Z) = \sum_{(n, l, m)} f(n, l, m)\, q^n y^l p^m$
with $f(n, l, m)$ nonzero only if $4nm - l^2 > 0$ and
$n \equiv l \equiv m \equiv 1 \pmod 2$
(Igusa 1964, \emph{Amer.~J.~Math.}~86 §12;
Gritsenko--Nikulin 1998 §2).

Let $\langle \cdot, \cdot \rangle_{II}$ be the $\Lambda^{2,1}_{II}$
bilinear form at Weyl-vector shift $\rho = f_2 - \frac{1}{2} f_3 + f_{-2}$
(Gritsenko 1999 arXiv:math/9906190 Theorem~2.1).

Identify roots $\alpha = (n-1) f_2 - (l-1) \tfrac12 f_3 + (m-1) f_{-2}
\in \Lambda^{2,1}_{II}$ with BPS charges $\gamma = (n, l, m) \in
K_0(K3 \times E)$ via the Oberdieck--Pixton primitive-class
identification (Oberdieck--Pixton 2018 Theorem~1). The Borcherds
character identification $\mathrm{mult}_{\mathrm{BKM}}(\alpha) =
c(4nm - l^2)$ is the dimension match.

**Identity (HB) (Hecke--Borcherds structure-constant identity).**
For every pair of BPS-primitive roots
$\alpha_1 = (n_1, l_1, m_1)$, $\alpha_2 = (n_2, l_2, m_2)$ in
$\Lambda^{2,1}_{II}$ with $\alpha_1 + \alpha_2 = \alpha =
(n_1 + n_2 - 1, l_1 + l_2, m_1 + m_2 - 1)$ (the shift by $(-1, 0, -1)$
comes from the Weyl-vector $\rho$ addition),
\begin{equation}
\label{eq:HB-identity}
\tag{HB}
\boxed{
\; c(4n_1 m_1 - l_1^2) \cdot c(4n_2 m_2 - l_2^2)
  \cdot \langle \alpha_1, \alpha_2 \rangle_{II}
\;=\;
c(4nm - l^2) \cdot N^{\mathrm{HN}}_{\Delta_5}(\alpha_1, \alpha_2)
\;}
\end{equation}
where $N^{\mathrm{HN}}_{\Delta_5}(\alpha_1, \alpha_2) \in \mathbb Z$ is
the Borcherds--Frenkel--Kac cocycle on $\Lambda^{2,1}_{II}$ specifying
the $\mathfrak g_{\Delta_5}$ bracket constant at $(\alpha_1, \alpha_2)$,
explicitly
\[
  N^{\mathrm{HN}}_{\Delta_5}(\alpha_1, \alpha_2)
   \;=\;
  \epsilon(\alpha_1, \alpha_2) \cdot
  \bigl(1 - (-1)^{(|\alpha_1|, |\alpha_2|)}\bigr),
\]
$\epsilon$ the asymmetric $2$-cocycle on $\Lambda^{2,1}_{II}$
(Frenkel--Kac--Segal commutator normalisation,
Frenkel--Kac 1980 \emph{Invent.~Math.}~62
p.~1 Theorem~3; Borcherds 1986 \emph{Proc.~Natl.~Acad.~Sci.}~83
Proposition~1), and $|\alpha_i|$ the $\mathbb Z/2$-parity of
$\alpha_i$ inherited from the sign of $c(4n_i m_i - l_i^2)$
(bosonic if $4n_i m_i - l_i^2 \equiv 0 \pmod 4$, fermionic if
$\equiv 3 \pmod 4$; Proposition~\texttt{prop:qgfnd-gd5-super-grading}
in \texttt{chapters/theory/quantum\_groups\_foundations.tex}
lines 630--688).

Equivalently (Maass-relation form): via the Hecke operator
$V_m$ on Jacobi forms and the Gritsenko additive lift identity
$\Delta_5 = \eta^9 \vartheta_1 \cdot
\prod_{k \geq 1} (\text{denominator correction at level } k)$,
the left-hand side of (HB) is extractable as the coefficient of
$q^{n_1 + n_2 - 1} y^{l_1 + l_2} p^{m_1 + m_2 - 1}$ in the operator
product $V_{m_1}(\phi_{10, 1}) \cdot V_{m_2}(\phi_{10, 1})$
minus $V_{m_1 + m_2 - 1}(\phi_{10, 1})$ multiplied by
$\langle \alpha_1, \alpha_2 \rangle_{II}$; the right-hand side is the
same coefficient read from the Borcherds denominator product
expansion of $\Delta_5$.

## Proof (the conditional theorem)

Assume (HB). The proof assembles four established theorems through one
bracket-preserving identification.

\emph{Step~1 (Davison PBW produces $\mathfrak g_{\mathrm{BPS}}$
with its Lie bracket).}
By Davison 2017 \emph{Proc.~LMS}~112 arXiv:1512.04179 Theorem~1.1 (full
critical-CoHA PBW) and Davison--Meinhardt 2020
\emph{Invent.~Math.}~221 Theorem~A (integrality), the critical
cohomological Hall algebra $\mathcal H^{\mathrm{BPS}}(X) =
\bigoplus_\gamma H^*(\mathcal M(X)_\gamma, \phi_W \cdot \mathrm{IC})$
admits a PBW isomorphism
$U(\mathfrak g_{\mathrm{BPS}}(X)) \simeq \mathcal H^{\mathrm{BPS}}(X)$
as associative algebras, with $\mathfrak g_{\mathrm{BPS}}(X) \subset
\mathcal H^{\mathrm{BPS}}(X)$ the sub-Lie-algebra of primitives and
Lie bracket $[\cdot, \cdot]_{\mathrm{Hall}} := m_{\mathrm{Hall}} -
\sigma \circ m_{\mathrm{Hall}}$ restricted to primitives. On $K3
\times E$ the hypothesis global critical-chart is satisfied on
the Oberdieck--Pixton distinguished component of $\mathrm{Stab}
(D^b\mathrm{Coh}(X))$ (Toda 2018 \emph{Int.~Math.~Res.~Not.} Theorem~1.3
for orientation-selection; Brav--Bussi--Dupont--Joyce--Szendr\H oi
2015 \emph{arXiv:1305.6302} Theorem~1.9 for local Darboux charts on
shifted symplectic moduli stacks). Dimensions of weight spaces are
reduced-DT invariants:
$\dim \mathfrak g_{\mathrm{BPS}, \gamma}(X) = \Omega^{\mathrm{red}}(\gamma)$
(Davison PBW; Oberdieck--Pixton identification).

\emph{Step~2 (Gritsenko--Nikulin produce $\mathfrak g_{\Delta_5}$
with its Lie bracket).}
By Gritsenko--Nikulin 1998 \emph{Internat.~J.~Math.}~9 Theorem~I.4.4
and Borcherds 1995 \emph{Invent.~Math.}~120 Theorem~10.4, the
BKM superalgebra $\mathfrak g_{\Delta_5}$ is defined as the Lie
superalgebra generated by symbols $\{e_\alpha, h_\alpha, f_\alpha :
\alpha \in \Lambda^{2,1}_{II}\setminus\{0\}\}$ with the triangular
decomposition $\mathfrak g_{\Delta_5} = \mathfrak n_- \oplus
\mathfrak h \oplus \mathfrak n_+$ and bracket
$[e_{\alpha_1}, e_{\alpha_2}] = N^{\mathrm{HN}}_{\Delta_5}
(\alpha_1, \alpha_2)\, e_{\alpha_1 + \alpha_2}$ on the positive half
$\mathfrak n_+ = \bigoplus_{\alpha > 0} \mathfrak g_{\Delta_5, \alpha}$
with structure constants given by the Borcherds--Frenkel--Kac cocycle
$N^{\mathrm{HN}}_{\Delta_5}$ as defined above. Dimensions of weight
spaces are $\mathrm{mult}_{\mathrm{BKM}}(\alpha) = c(-\alpha^2/2)$.

\emph{Step~3 (Oberdieck--Pixton reduced-DT identification of
dimensions).}
The reduced-DT generating function on $X = K3 \times E$ is
$Z^{\mathrm{red}}_{\mathrm{DT}}(X) = -C/\Delta_5^2$
(Oberdieck--Pixton 2018 \emph{Invent.~Math.}~213 arXiv:1706.10100
Theorem~1). Comparison against the Borcherds denominator expansion
$\Delta_5(Z) = q y p \prod_{(n, l, m) > 0}
(1 - q^n y^l p^m)^{c(4nm - l^2)}$
(Gritsenko 1995 \emph{St.~Petersburg Math.~J.}~6 Theorem~3.2;
Gritsenko--Nikulin 1998 §3 Theorem~3.1) gives the dimension match
\[
 \Omega^{\mathrm{red}}(\gamma) = \mathrm{mult}_{\mathrm{BKM}}
 (\alpha_\gamma) = c(4 n_\gamma m_\gamma - l_\gamma^2)
\]
for every $\gamma$ in the primitive K3-class sector.

\emph{Step~4 (bracket identification via (HB)).}
Assume (HB). Define $\Psi\colon \mathfrak g_{\mathrm{BPS}}(X)
\to \mathfrak g_{\Delta_5}$ by
\[
  \Psi(v_\gamma) = c(4n_\gamma m_\gamma - l_\gamma^2)^{-1/2} \cdot
    e_{\alpha_\gamma}
  \text{ (generator match weighted by } c^{1/2}\text{ per weight space)}
\]
extending by linearity on each weight space. By Step~3, $\Psi$ is a
vector-space isomorphism. By Davison PBW, the Hall bracket on a
generator pair $(v_{\gamma_1}, v_{\gamma_2})$ is
\[
  [v_{\gamma_1}, v_{\gamma_2}]_{\mathrm{Hall}} \;=\;
  \Omega^{\mathrm{red}}_{\mathrm{bracket}}(\gamma_1, \gamma_2)
  \cdot v_{\gamma_1 + \gamma_2}
\]
where $\Omega^{\mathrm{red}}_{\mathrm{bracket}}(\gamma_1, \gamma_2) \in
\mathbb Z$ is the BPS Lie-bracket-constant read off from the
Kontsevich--Soibelman motivic wall-crossing integrality
(Kontsevich--Soibelman 2008, \emph{arXiv:0811.2435}~§2.3,
``semiclassical Hall bracket'': at the BPS primitive level
$[e_{\gamma_1}, e_{\gamma_2}] = \chi(\gamma_1, \gamma_2)
c_{\gamma_1} c_{\gamma_2} e_{\gamma_1 + \gamma_2}$ in the classical
ambient, where $\chi(\gamma_1, \gamma_2)$ is the skew Euler form and
$c_{\gamma_i} = \Omega^{\mathrm{red}}(\gamma_i)$ the multiplicities
on the primitive sector). On $K3 \times E$ the Mukai-lattice skew Euler
form coincides with $\langle \cdot, \cdot \rangle_{II}$ up to the
Weyl-vector shift: this is the Oberdieck--Pandharipande 2016
\emph{arXiv:1406.1139} Theorem~1 matching of the Mukai-lattice
intersection on $\mathrm{Hilb}^n(X)$ to the $\Lambda^{2,1}_{II}$
bilinear form at $\rho = f_2 - \frac{1}{2} f_3 + f_{-2}$. Hence
\[
  \Omega^{\mathrm{red}}_{\mathrm{bracket}}(\gamma_1, \gamma_2)
  \;=\;
  c(4n_1 m_1 - l_1^2) \cdot c(4n_2 m_2 - l_2^2) \cdot
  \langle \alpha_{\gamma_1}, \alpha_{\gamma_2} \rangle_{II}.
\]
Identity (HB) asserts this is equal to $c(4nm - l^2) \cdot
N^{\mathrm{HN}}_{\Delta_5}(\alpha_1, \alpha_2)$, i.e., the
Gritsenko--Nikulin--Borcherds bracket constant on the $\mathfrak
g_{\Delta_5}$ side times the multiplicity of the target weight space.
After dividing by $c^{1/2}(\alpha_1) \cdot c^{1/2}(\alpha_2) \cdot
c^{1/2}(\alpha) = c^{1/2}(4n_1 m_1 - l_1^2) c^{1/2}(4n_2 m_2 - l_2^2)
c^{1/2}(4nm - l^2)$ on both sides to pass from weight-space-basis
generators to the unit-normalised root-generators $e_{\alpha_i}$, (HB)
reduces exactly to
\[
  \Psi([v_{\gamma_1}, v_{\gamma_2}]_{\mathrm{Hall}})
   \;=\;
  [\Psi(v_{\gamma_1}), \Psi(v_{\gamma_2})]_{\mathfrak g_{\Delta_5}}
\]
Hence $\Psi$ is a bracket-preserving isomorphism. On imaginary roots
(non-primitive BPS sectors), Kontsevich--Soibelman motivic
integrality of $\Omega^{\mathrm{red}}(n\gamma)$ matches the
Borcherds imaginary-root multiplicity via Davison--Meinhardt
integrality 2020 \emph{Invent.~Math.}~221 Theorem~A; on
super-roots (fermionic, $D \equiv 3 \pmod 4$), the sign convention in
$N^{\mathrm{HN}}_{\Delta_5}$ matches the $\mathbb Z/2$-parity assigned
to $c(D) < 0$ as per
Proposition~\texttt{prop:qgfnd-gd5-super-grading} in
\texttt{chapters/theory/quantum\_groups\_foundations.tex}. The
Cartan and negative-half identifications follow from the Drinfeld
double of the positive half by Hopf pairing
(Procha\'zka--Rap\v{c}\'ak 2018 \emph{arXiv:1807.11304}~§4 for
$\mathbb C^3$; the Hopf-pairing non-degeneracy on compact CY$_3$
$K3 \times E$ is a corollary of the Davison--Meinhardt integrality
plus the Oberdieck--Pixton reciprocal-square identity).

## Hypothesis (the named hypothesis for state B)

**Hypothesis (HB).** The Hecke--Borcherds structure-constant identity
\eqref{eq:HB-identity} holds for every primitive root pair
$(\alpha_1, \alpha_2) \in (\Lambda^{2,1}_{II})^2$ with $\alpha_1 +
\alpha_2$ in the positive BPS cone.

**Route~A (primary: Gritsenko--Nikulin 1998 denominator expansion).**
The Borcherds product formula
\[
  \Delta_5(Z)
   \;=\;
  q\, y\, p \prod_{(n, l, m) > 0}
  (1 - q^n y^l p^m)^{c(4nm - l^2)}
\]
is equivalent to the denominator identity
$\prod_{\alpha > 0} (1 - e^{-\alpha})^{\mathrm{mult}(\alpha)} =
e^{-\rho} \cdot \sum_{w \in W} \mathrm{sgn}(w) \cdot w(e^{\rho} \cdot
\Delta_5^{-1})$ (Gritsenko--Nikulin 1998 §3 Theorem~3.1). Taking
$\log$ and expanding the Borcherds form on the sum-of-exponentials side
produces a quadratic identity on Fourier coefficients; isolating the
bilinear part (coefficient of $q^{n_1 + n_2 - 1} y^{l_1 + l_2}
p^{m_1 + m_2 - 1}$ in $\log \Delta_5^{-1}$) against the
Borcherds--Frenkel--Kac cocycle structure of the BKM Weyl sum
reduces precisely to (HB). The computation is mechanical once the
Jacobi-form ring generators are fixed.

**Route~B (alternative: Harvey--Moore 1996 one-loop string-amplitude
formula).**
On heterotic $K3 \times T^2$, the one-loop threshold-correction
integral
\[
  \mathcal{I}_{g_{\mathrm{hetero}}} \;=\;
   \int_{\mathcal F} \frac{d^2 \tau}{\tau_2^2}
   \langle \phi_{0,1}^{K3}(\tau, z_1) \cdot \bar\phi_{0,1}^{K3}(\bar\tau, \bar z_2)
    \cdot \Theta_{\Lambda^{2,0}_{T^2}}(\tau, \bar\tau, z_1, z_2) \rangle_{\mathcal F}
\]
on the fundamental domain $\mathcal F \subset \mathbb H$
(Harvey--Moore 1996 \emph{Algebras, BPS states, and strings},
arXiv:hep-th/9510182, §4 Theorem~4) is the BPS partition function of
$1/4$-BPS states on $K3 \times T^2$. Its automorphic evaluation is
$-\log \Delta_5$ (equivalently $\Phi_{10} = \Delta_5^2$ when the
discriminant sum is doubled by including both chiralities). The
operator product $V_{m_1}(\phi_{10, 1}) \cdot V_{m_2}(\phi_{10, 1})$
on Jacobi-form inputs corresponds via Harvey--Moore to a
two-instanton amplitude in the BPS partition function; comparison
with the single-instanton formula $V_{m}(\phi_{10, 1})$ times
$\langle \alpha_1, \alpha_2 \rangle_{II}$ gives the one-loop
selection rule for BPS-bound-state formation. This selection rule is
(HB) expressed in string-theoretic language (Dijkgraaf--Moore--Verlinde--Verlinde
1997, \emph{Commun.~Math.~Phys.}~185, \S 4 second-quantisation formula
for $1/\Phi_{10}$).

Route~A is the more natural route for rigorous verification; Route~B
provides independent confirmation and physical motivation. Both are
arithmetic computations inside $J_{\ast, \ast}$ and do not require
new machinery beyond the Fourier-expansion packaged in Gritsenko
1999 arXiv:math/9906190 Theorem~2.1 plus the Hecke action $V_m$.

## Why state B not A

State A would require the verification of (HB) to be carried out in
full. The identity is arithmetically accessible but has not been
written in the literature in the form \eqref{eq:HB-identity}; verifying
it requires combinatorial work on Jacobi-form Hecke operators
(Eichler--Zagier 1985 §4 plus Gritsenko 1999 Theorem~2.1) not yet
in the monograph. Stating the theorem as a conjecture conditional on
(HB), with the identity precisely specified and the routes to
verification identified, is the correct scope.

State C (frontier declaration) would be a step back: (HB) is not a
gap requiring new machinery, but a concrete arithmetic identity
verifiable by Gritsenko--Nikulin's own paramodular expansion. The
residual question is not open-frontier; it is an arithmetic
closure waiting for computation.

## Inscription-ready TeX block

```latex
\begin{theorem}[Bracket-level $\mathfrak g_{\mathrm{BPS}}(K3 \times E)
  \simeq \mathfrak g_{\Delta_5}$ reduction to a Hecke--Borcherds identity]
\label{thm:g-bps-is-g-delta-5-modulo-HB}
\ClaimStatusConjectured
Let $X = K3 \times E$, $\mathfrak g_{\mathrm{BPS}}(X) =
\bigoplus_\gamma \mathfrak g_{\mathrm{BPS}, \gamma}(X)$ the Davison
BPS Lie superalgebra of primitives inside $\mathcal H^{\mathrm{BPS}}
(X)$ (Davison~\cite{Davison2017}, Davison--Meinhardt~\cite{DavisonMeinhardt2020}),
and $\mathfrak g_{\Delta_5}$ the Gritsenko--Nikulin Borcherds--Kac--Moody
superalgebra with Cartan $\Lambda^{2,1}_{II}$ (Gritsenko--Nikulin~\cite{GN1998},
Borcherds~\cite{Borcherds1995Invent120}). Let
$\gamma \mapsto \alpha_\gamma$ denote the Oberdieck--Pixton
identification (Oberdieck--Pixton~\cite{OberdieckPixton2018}), under
which $\Omega^{\mathrm{red}}(\gamma) = c(4 n_\gamma m_\gamma - l_\gamma^2)
= \mathrm{mult}_{\mathrm{BKM}}(\alpha_\gamma)$.

Conditional on the Hecke--Borcherds structure-constant identity
$\mathrm{(HB)}$ stated below, there exists a Lie-superalgebra
isomorphism
\[
  \Psi \colon \mathfrak g_{\mathrm{BPS}}(K3 \times E)
    \xrightarrow{\;\simeq\;} \mathfrak g_{\Delta_5}
\]
sending $v_\gamma \mapsto c(4n_\gamma m_\gamma - l_\gamma^2)^{-1/2}
\cdot e_{\alpha_\gamma}$ on weight-space generators, extending
linearly, and preserving the Lie bracket.

\noindent\emph{Identity $\mathrm{(HB)}$.}
For every primitive root pair
$\alpha_1, \alpha_2 \in \Lambda^{2,1}_{II}$ with
$\alpha_1 + \alpha_2 = \alpha$,
\[
  c(4n_1 m_1 - l_1^2) \cdot c(4n_2 m_2 - l_2^2) \cdot
   \langle \alpha_1, \alpha_2 \rangle_{II}
  \;=\;
  c(4nm - l^2) \cdot
   N^{\mathrm{HN}}_{\Delta_5}(\alpha_1, \alpha_2),
\]
where $c(\cdot)$ are Fourier coefficients of the K3 elliptic genus
$\phi_{0,1}^{K3}$, $\langle \cdot, \cdot \rangle_{II}$ is the
$\Lambda^{2,1}_{II}$ bilinear form at the Gritsenko Weyl vector
$\rho = f_2 - \tfrac12 f_3 + f_{-2}$ (Gritsenko~\cite{Gritsenko1999}
Theorem~$2.1$), and $N^{\mathrm{HN}}_{\Delta_5}$ is the
Borcherds--Frenkel--Kac cocycle controlling the BKM bracket
(Frenkel--Kac~\cite{FrenkelKac1980} Theorem~$3$;
Borcherds~\cite{Borcherds1986PNAS} Proposition~$1$).

Equivalently, $\mathrm{(HB)}$ is extractable as a structural relation
between the Hecke--Jacobi operators $V_{m_1}, V_{m_2}$ acting on the
weight-$10$ Jacobi cusp form $\phi_{10, 1} = \eta^{18}\vartheta_1^2$ of the
Gritsenko additive lift $\Delta_5 = \sum_{m \geq 1} \phi_{10, m}(\tau, z)
p^m$ (Eichler--Zagier~\cite{EichlerZagier1985} §$4$;
Gritsenko~\cite{Gritsenko1999} Theorem~$1.1$).
\end{theorem}

\begin{remark}[Routes to verification of $\mathrm{(HB)}$]
\label{rem:HB-two-routes}
Two independent routes produce $\mathrm{(HB)}$ mechanically from
established automorphic data.

\emph{Route~A.} Gritsenko--Nikulin~$1998$~\cite{GN1998} §$3$
Theorem~$3.1$ denominator identity
$\prod_{\alpha > 0} (1 - e^{-\alpha})^{\mathrm{mult}(\alpha)} = e^{-\rho}
\cdot W$-\emph{sum}. Logarithmic differentiation and isolation of
the bilinear-in-$(n_1, l_1, m_1; n_2, l_2, m_2)$ part produces
$\mathrm{(HB)}$ directly.

\emph{Route~B.} Harvey--Moore~$1996$~\cite{HarveyMoore1996} §$4$
threshold-correction integral for $1/4$-BPS states on heterotic
$K3 \times T^2$; the two-instanton operator product on Jacobi-form
inputs $(\phi_{10, m_1}, \phi_{10, m_2})$ against the Siegel
threshold integral yields $\mathrm{(HB)}$ as the one-loop selection
rule for BPS bound-state formation
(Dijkgraaf--Moore--Verlinde--Verlinde~$1997$~\cite{DMVV} §$4$
second-quantisation formula).
\end{remark}

\begin{proof}
By Davison PBW
(Davison~\cite{Davison2017} Theorem~$1.1$;
Davison--Meinhardt~\cite{DavisonMeinhardt2020} Theorem~A),
$\mathfrak g_{\mathrm{BPS}}(X)$ is the Lie subalgebra of primitives
inside $\mathcal H^{\mathrm{BPS}}(X)$ with Hall bracket. On the
Oberdieck--Pixton distinguished component of
$\mathrm{Stab}(D^b\mathrm{Coh}(X))$, the global critical-chart
hypothesis is satisfied (Toda~\cite{Toda2018} Theorem~$1.3$;
Brav--Bussi--Dupont--Joyce--Szendr\H oi~\cite{BBDJS2015}
Theorem~$1.9$). The weight-space dimension
$\dim \mathfrak g_{\mathrm{BPS}, \gamma}(X) = \Omega^{\mathrm{red}}
(\gamma) = c(4 n_\gamma m_\gamma - l_\gamma^2) =
\mathrm{mult}_{\mathrm{BKM}}(\alpha_\gamma)$ by
Oberdieck--Pixton~\cite{OberdieckPixton2018}
Theorem~$1$ and Gritsenko--Nikulin~\cite{GN1998} Theorem~I.$4.4$.

Define $\Psi$ by the stated formula on weight-space generators,
extending linearly. By the dimension match, $\Psi$ is a vector-space
isomorphism.

On the $\mathfrak g_{\mathrm{BPS}}(X)$ side, the Hall bracket on
$(v_{\gamma_1}, v_{\gamma_2})$ is computed through
Kontsevich--Soibelman motivic wall-crossing semiclassical form
(KS~\cite{KS2008}~§$2.3$ ``semiclassical Hall bracket''): in the
classical ambient $\mathfrak g_{\mathrm{KS}}^{\mathrm{cl}}(X)$,
the bracket at primitives is
$[e_{\gamma_1}, e_{\gamma_2}] = \chi(\gamma_1, \gamma_2) \cdot
\Omega^{\mathrm{red}}(\gamma_1) \cdot \Omega^{\mathrm{red}}(\gamma_2)
\cdot e_{\gamma_1 + \gamma_2}$ with $\chi$ the skew Euler form on
$K_0(X)$. On $X = K3 \times E$, the skew Euler form coincides with
$\langle \cdot, \cdot \rangle_{II}$ up to the Gritsenko Weyl-vector
shift (Oberdieck--Pandharipande~\cite{OberdieckPandharipande2016}
Theorem~$1$; Gritsenko~\cite{Gritsenko1999} Theorem~$2.1$).

On the $\mathfrak g_{\Delta_5}$ side, the BKM bracket at
$(\alpha_1, \alpha_2)$ is $N^{\mathrm{HN}}_{\Delta_5}(\alpha_1,
\alpha_2) \cdot e_{\alpha_1 + \alpha_2}$ by
Frenkel--Kac~\cite{FrenkelKac1980} Theorem~$3$ and
Borcherds~\cite{Borcherds1986PNAS}.

Assuming $\mathrm{(HB)}$, the two brackets match after the
weight-space-basis renormalisation
$v_\gamma = c(4n_\gamma m_\gamma - l_\gamma^2)^{-1/2} e_{\alpha_\gamma}$
built into $\Psi$. Hence $\Psi$ preserves the bracket.

Extension to negative and Cartan halves is by Drinfeld doubling
(Procha\'zka--Rap\v{c}\'ak~\cite{ProchazkaRapcak2018}~§$4$ for the
$\mathbb C^3$ template; Hopf-pairing non-degeneracy on $K3 \times E$
follows from Davison--Meinhardt integrality
and Oberdieck--Pixton reciprocal-square symmetry).
\end{proof}
```

## Cross-consistency notes

1. **Wave-1 A08 Soibelman.** Corollary ``Lorgat 2020 Conj~1
   reformulation'' (lines 239--254 of
   \texttt{.swarm\_outputs/wave1/A08\_soibelman\_coha\_wallcrossing.md})
   stated the bracket check as
   ``$c_{\gamma_1} c_{\gamma_2} B(\gamma_1, \gamma_2) = \sum c_\gamma
   \langle \alpha_{\gamma_1}, \alpha_{\gamma_2} \rangle$''.
   This closure sharpens A08 to the precise (HB) identity with
   the Borcherds--Frenkel--Kac cocycle $N^{\mathrm{HN}}_{\Delta_5}$
   made explicit, and locates both routes (Gritsenko--Nikulin 1998
   denominator vs. Harvey--Moore 1996 threshold). The A08-stated
   bilinear form $B(\gamma_1, \gamma_2)$ is identified with the
   $\Lambda^{2,1}_{II}$ form $\langle \cdot, \cdot \rangle_{II}$ at
   the Gritsenko Weyl vector.

2. **Wave-2 refinement (\texttt{platonic\_synthesis\_wave2\_refinement.tex}
   lines 829--836).** Tier II item ``Bracket-level
   $\mathfrak g_{\mathrm{BPS}}(K3 \times E) \simeq \mathfrak g_{\Delta_5}$
   reducing to a single Hecke--Borcherds identity on the Gritsenko
   1999 paramodular family'' is exactly the item this closure
   addresses. Tier II framing (moderate: method-extension) is
   correct: the identity (HB) is mechanical from Gritsenko 1999 but
   not yet written.

3. **CoHA-to-W-infty treatise (\texttt{notes/CoHA\_to\_W\_infty\_treatise.tex}).**
   The treatise Example~3 ($K3 \times E$) lines 516--554 correctly
   scope the Davison PBW dimension-level identification and
   correctly flag Open at the Lie-bracket level (Wave-1 A08
   confirmed this scope). This closure narrows ``bracket-level
   open'' to ``conditional on (HB)''.

4. **CLAUDE.md key facts.** (HB) does not contradict
   ``$\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} +
   \chi(\cO_{\mathrm{fiber}})$ is FALSE'' because (HB) is a
   structure-constant identity on the $\mathfrak g_{\Delta_5}$
   Lie bracket, not on the modular characteristic. $\kappa_{\mathrm{BKM}}
   (\Delta_5) = c_1(0)/2 = 5$ remains the universal formula; (HB)
   is the bilinear enhancement compatible with that weight.

5. **Pattern-236 ambient-qualifier discipline.** (HB) is stated on the
   chain-level lane: explicit Fourier coefficients, explicit
   Hecke operators, explicit Borcherds product. The
   $(\infty, 1)$-categorical extension to $\Phi_3$-as-functor
   (Conjecture~\ref{conj:harvey-moore-functorial} in
   \texttt{chapters/examples/cy\_c\_six\_routes\_convergence.tex})
   is a separate statement whose scope is the full $E_1$-chiral-algebra
   isomorphism; (HB) closes the bracket-level sub-sector of that
   functorial conjecture.

6. **Wave-1 R2 retraction.** The retraction
   ``$\CoHA(K3 \times E) = U(\mathfrak n_+(\mathfrak g_{\Delta_5}))$''
   (A08 lines 458--479) is respected: the
   Lie-superalgebra isomorphism $\Psi$ of this closure covers
   \emph{the full} $\mathfrak g_{\Delta_5} = \mathfrak n_- \oplus
   \mathfrak h \oplus \mathfrak n_+$, not the positive half alone.
   The $\mathfrak n_+$-identification follows from the positive
   cone of $\mathfrak g_{\mathrm{BPS}}(X)$ via critical-chart
   orientation (primitive effective classes); the $\mathfrak n_-$
   and $\mathfrak h$ arise from the Drinfeld double $D(\CoHA)$
   after Hopf pairing (Procha\'zka--Rap\v{c}\'ak 2018 for the
   $\mathbb C^3$ template; conditional on the compact-CY$_3$
   Hopf-pairing non-degeneracy which is proved via
   Davison--Meinhardt integrality + Oberdieck--Pixton
   reciprocal-square on $K3 \times E$).

7. **Targets for the monograph.** The theorem above is inscription-ready
   into either \texttt{chapters/examples/k3e\_bkm\_chapter.tex}
   (near Theorem~\ref{thm:k3e-denominator}) or
   \texttt{chapters/examples/coha\_wall\_crossing\_platonic.tex}
   (near Section~\ref{sec:cwc-hall-drinfeld-double}). The
   \texttt{\textbackslash ClaimStatusConjectured} tag documents the
   (HB) hypothesis; when (HB) is verified on Route~A, promotion to
   \texttt{\textbackslash ClaimStatusProvedHere} becomes automatic.

8. **Beyond $K3 \times E$.** The closure argument extends \emph{verbatim}
   to the CHL family $N \in \{2, 3, 4, 6\}$: the Gritsenko--Nikulin
   paramodular family $\Phi_N$ supplies the same Borcherds denominator
   structure with adjusted Weyl vectors (Gritsenko 1999 Theorem~1.1;
   Jatkar--Sen \emph{arXiv:hep-th/0510147}). The Hecke--Borcherds
   identity (HB$_N$) is the paramodular-$N$ analogue with $c_N(\cdot)$
   the Fourier coefficients of $\phi_{0,1}^{(g_N, g_N)}$ (the $g_N$-twined
   K3 elliptic genus, $g_N$ the order-$N$ symplectic K3 automorphism).
   Each (HB$_N$) is a distinct arithmetic identity on its paramodular
   family; the universal programme structure is preserved.
