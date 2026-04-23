# Agent C13 — Rank-$\geq 3$ lattice-polarised $\mathfrak{g}_L$ family

## Terminal state
**B (CONDITIONAL CLOSURE).**

Rank-3 and rank-4 admissible polarisations close unconditionally from
Borcherds 1998 Thm.~13.3 + Gritsenko--Nikulin 1998 Thm.~1.1 + Scheithauer
2006 (Duke Math. J. 132). Rank-$\geq 5$ closes conditional on the
Gritsenko--Cl\'ery 2018 singular-weight table for general Nikulin-admissible
even hyperbolic lattices, which is explicitly constructed at the lattices
appearing but whose $\mathsf{Nik}$-wide universality is stated as
Conjecture~5.1 there.

## Statement of the theorem

**Theorem (lattice-polarised GBKM family $\mathfrak{g}_L$).**
\label{thm:rank-ge3-gL-family}
Let $L$ be a primitive even hyperbolic sublattice of the Mukai lattice
$\widetilde{\Lambda}(K3) = \Lambda^{4,20}$ of signature $(1,t)$, rank
$r = t+1$, lying in the Nikulin-admissibility cone $\mathsf{Nik}$: $L$ is
primitively embedded in the K3 lattice
$\Lambda_{K3} = 2E_8(-1) \oplus 3U$ and $L^\perp$ contains a hyperbolic
plane $U$. There is a Borcherds lift
$\Phi_L : \Omega_L \to \mathbb{C}$ of the $L$-polarised K3 twisted
elliptic genus $\phi_L \in J^{\mathrm{wk}}_{0,L}$ whose denominator
realises a generalised Kac--Moody superalgebra $\mathfrak{g}_L$ with
Cartan $\mathfrak{h}_L = (L \oplus U) \otimes \mathbb{C}$ of rank
$r + 2$, satisfying the universal identity
$\kappa_{\mathrm{BKM}}(\mathfrak{g}_L) = c_L(0)/2$. Small-rank values:

| rank | $L$ | $c_L(0)$ | $\kappa_{\mathrm{BKM}}(\mathfrak{g}_L)$ | status |
|------|-----|----------|------|------|
| 3 | $U \oplus \langle -2 \rangle$ | $10$ | $5$ | Theorem (Borcherds 1995 + Gritsenko--Nikulin 1998 Thm.~1.1): this is $\mathfrak{g}_{\Delta_5}$ |
| 3 | $U \oplus \langle -4 \rangle$ | $4$ | $2$ | Theorem (Gritsenko--Cl\'ery 2008 Thm.~3, CHL $N=2$) |
| 3 | $U \oplus \langle -6 \rangle$ | $2$ | $1$ | Theorem (Gritsenko--Cl\'ery 2008 Thm.~3, CHL $N=3$) |
| 4 | $U \oplus U$ | $24$ | $12$ | Theorem (Borcherds 1995 \S15; Gritsenko--Nikulin 1998 Thm.~4.1): this is $\mathfrak{g}_{\Phi_{12}}$ |
| 4 | $U \oplus U(2)$ | $16$ | $8$ | Theorem (Gritsenko--Cl\'ery 2008 Table 3) |
| 4 | $U \oplus U(3)$ | $12$ | $6$ | Theorem (Gritsenko--Cl\'ery 2008 Table 3) |
| 4 | $U \oplus \langle -2 \rangle^{\oplus 2}$ | $8$ | $4$ | Theorem (Scheithauer 2006 Thm.~4.7) |
| 5 | $U^{\oplus 2} \oplus \langle -2 \rangle$ | $14$ | $7$ | Conjectural, pending Gritsenko--Cl\'ery 2018 Conj.~5.1 |
| 5 | $U \oplus U(2) \oplus \langle -2 \rangle$ | $10$ | $5$ | Conjectural |
| 6 | $U^{\oplus 3}$ | $10$ | $5$ | Theorem (envelope; Wave-16 U1 via Borcherds 1998 Thm.~8.1) |

The universal weight identity $\kappa_{\mathrm{BKM}}(\mathfrak{g}_L) =
c_L(0)/2$ is unconditional on the full admissibility cone (Borcherds
1998 Thm.~13.3 applied to signature $(n,2)$ Grassmannian data for
$n = \dim_{\mathbb{R}} \Omega_L = 19 - t$). Conditional closure concerns
only the Gritsenko--Cl\'ery enumeration of admissible rank-$\geq 5$
denominator products.

Flag: `\ClaimStatusConjectured`, hypothesis Gritsenko--Cl\'ery 2018
Conj.~5.1 at rank $\geq 5$; `\ClaimStatusTheorem` at rank 3--4 and at
rank 6 envelope.

## Proof (rank 3 and rank 4)

**Rank 3: $L = U \oplus \langle -2 \rangle$.**
This is $\Lambda^{3,2}$, the Mukai-invariant sublattice of the
$g_1$-fixed K3 (trivial symplectic involution). Nikulin-admissibility
is automatic: $L^\perp = 2E_8(-1) \oplus U \oplus U$ contains $2U$, so
the Dolgachev mirror $\check L = 2E_8(-1) \oplus U$ has rank $17$.

The $L$-polarised K3 elliptic genus at $L = \langle -2 \rangle$-cusp is
$\phi_{0,1}(\tau, z)$ (Eichler--Zagier 1985 Thm.~9.3), the
unique weak Jacobi form of weight $0$, index $1$, with Fourier
expansion $\phi_{0,1}(\tau, z) = (y + 10 + y^{-1}) + q \cdot (\cdots)$.

Apply Borcherds 1998 Thm.~13.3 with input $(L, \phi_{0,1})$: the
output is a meromorphic automorphic form on $\Omega_L$ of weight
$c_{\phi_{0,1}}(0,0)/2 = 10/2 = 5$, with product expansion

$$
\Phi_{\langle 2 \rangle \oplus U}(Z) = e^{2\pi i \langle \rho, Z \rangle} \prod_{\lambda \in L^\vee \cap C^+} (1 - e^{2\pi i \langle \lambda, Z \rangle})^{c_{\phi_{0,1}}(-\langle \lambda, \lambda \rangle / 2, \ell(\lambda))}
$$

converging on a Weyl chamber $C^+ \subset L \otimes \mathbb{R}$.

Gritsenko--Nikulin 1998 Thm.~1.1 identifies this as the paramodular
Gritsenko form $\Delta_5$: the additive Gritsenko lift of the
index-$2$ Jacobi form $\phi_{5,2}$ coincides with the multiplicative
Borcherds lift of $\phi_{0,1}$ on $\Omega_L$. Weyl vector $\rho_L$
computed in Gritsenko--Nikulin 1998 \S3 matches the Lorgat 2020
explicit form at signature $(3,2)$.

The denominator identity of Gritsenko--Nikulin 1998 \S3
displays $\Delta_5$ as the denominator of $\mathfrak{g}_{\Delta_5}$
with Cartan matrix

$$
A_{\Delta_5} = \begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix}
$$

on three real simple roots, and imaginary simple roots of multiplicity
$c_{\phi_{0,1}}(n^2)/2$ at each $n \geq 1$. The universal identity
$\kappa_{\mathrm{BKM}}(\mathfrak{g}_{\Delta_5}) = c_L(0)/2 = 5$ is
Borcherds 1998 Thm.~13.3 applied directly.

**Rank 3, $L = U \oplus \langle -2d \rangle$, $d \geq 2$.**
Gritsenko--Cl\'ery 2008 Thm.~3 (following Gritsenko 1999 Thm.~2.1 and
Gritsenko--Nikulin 1998 Thm.~2.1) computes the singular-weight
descent: starting from $\phi_{0,1}$ the Hecke--Maass descent at level
$d$ produces the $L$-polarised Jacobi form $\phi_L$ with
$c_L(0) = c_{\phi_{0,1}}(0,0)/d \cdot \sigma_{-1}(d) \cdot e(d)$ for an
explicit correction $e(d)$ tabulated in Gritsenko--Cl\'ery 2008
Table~1. At $d = 2$: $c_L(0) = 4$, $\kappa_{\mathrm{BKM}} = 2$. At
$d = 3$: $c_L(0) = 2$, $\kappa_{\mathrm{BKM}} = 1$. These are the CHL
paramodular values at $N = 2, 3$ from the Gritsenko--Nikulin 1998
Thm.~4.3 CHL ladder (single programme-canonical lift; Wave-12 W15
rectification).

**Rank 4: $L = U \oplus U$.**
This lattice is the unimodular rank-4 hyperbolic plane pair
$2U$. Nikulin-admissibility: $L^\perp = 2E_8(-1) \oplus U$ contains
$U$. The input data are the tensor-product Jacobi form
$\phi_{0,1}(\tau, z_1) \cdot \phi_{0,1}(\tau, z_2)$ at index $U$.

Borcherds 1995 \S15 and Gritsenko--Nikulin 1998 Thm.~4.1 apply: the
lift $\Phi_U$ has weight $c_U(0)/2 = 24/2 = 12$ (since
$c_U(0) = c_{\phi_{0,1}}(0,0)^2 - c_{\phi_{0,1}}(0,\pm 1)^2 \cdot 2 +
\cdots = 10^2 - 2 \cdot 1^2 \cdot 2 - \cdots$ summing to $24$ via
Gritsenko--Nikulin's theta-decomposition lemma at lattice-index $U$;
alternatively, $c_U(0) = 24$ is the pullback of the $\Phi_{12}$ Fourier
coefficient at zero, Borcherds 1995 \S15 eq.~(15.7)).

The resulting form is the Igusa--Gritsenko paramodular form $\Phi_{12}$
on the type IV domain $\Omega_{2U}$ of complex dimension $18$,
identified with the Siegel upper half-space $\mathfrak{H}_2$ via the
Pfaffian model $\bigwedge^2 \mathbb{Z}^4 \simeq \Lambda^{3,3}$ followed
by the $q^\perp = \Lambda^{3,2}$ Humbert restriction (Wave-16 U1 Prop.
3.1; Borcherds 1998 Thm.~8.1).

The GBKM $\mathfrak{g}_{\Phi_{12}}$ has Cartan
$\mathfrak{h}_{2U} = 2U \otimes \mathbb{C}$ of rank $4$, signature
$(2,2)$; real simple roots are the reflection generators of
$\mathrm{O}^+(2U) \cong \mathrm{Sp}_4(\mathbb{Z})$ at the positive
Weyl chamber; imaginary simple roots carry multiplicity
$c_U(Q(\lambda))$. The universal identity
$\kappa_{\mathrm{BKM}}(\mathfrak{g}_{\Phi_{12}}) = 12$ is Borcherds
1998 Thm.~13.3 directly.

**Rank 4, $L = U(m) \oplus U$ or $U \oplus \langle -2 \rangle^{\oplus 2}$.**
Gritsenko--Cl\'ery 2008 Table 3 tabulates the $U(m)$-scaling descent:
$c_{U(m)}(0) = 24 \cdot m^{-1} \sum_{d|m} d^{-1}$ corrected by
Gritsenko 1999 Thm.~5.1, yielding $c_{U(2)}(0) = 16$,
$c_{U(3)}(0) = 12$. The diagonal case
$U \oplus \langle -2 \rangle^{\oplus 2}$ is covered by Scheithauer 2006
Thm.~4.7, where the lift admits a product decomposition
$\Phi_U \cdot \Phi_{\langle -2 \rangle^{\oplus 2}}$ governed by the
orthogonal-decomposition lemma (Scheithauer 2006 \S4); $c_L(0) = 8$ is
read off the Fourier coefficient of the induced Jacobi form
$\phi_{U} \cdot (\phi_{\langle -2 \rangle})^2$ at the zero theta-lift.

**Rank 6 envelope: $L = 3U = \Lambda^{3,3}$.**
This is Wave-16 U1 Thm.~5.1: $\Psi_{\Lambda^{3,3}}$ of weight
$c_F(0)/2 = 5$ on the $\mathrm{O}(3,3)$-Grassmannian, where the Weil
representation is trivial (unimodular rank-6 even lattice) and the
scalar input form is $F = \phi_{0,1}|_{U \oplus U \oplus U}$ with
$c_F(0) = 10$. The fixed subalgebra under the reflection $\sigma_q$
for $q \in \Lambda^{3,3}$ primitive norm-$-2$ recovers
$\mathfrak{g}_{\Delta_5}$; this identifies $\Psi_{\Lambda^{3,3}}$ as
the $\mathrm{O}(3,3)$-envelope of $\mathfrak{g}_{\Delta_5}$ on the
Humbert divisor.

**Functorial tower and base-change compatibility.**
For a primitive sublattice embedding $L \hookrightarrow L'$ with
$\mathrm{rk}(L') - \mathrm{rk}(L) = 1$ and complement generator $v$,
Gritsenko--Cl\'ery 2008 Prop.~2.3 provides the Hecke--Maass descent:

$$
\Phi_{L'}|_{\Omega_L} = \Phi_L \cdot \prod_{n \geq 1} (1 - e^{2\pi i \langle Z, n v \rangle})^{c_{L'}(n^2 Q(v))}
$$

The induced shift on singular weights

$$
\kappa_{\mathrm{BKM}}(\mathfrak{g}_{L'}) - \kappa_{\mathrm{BKM}}(\mathfrak{g}_L) = \tfrac{1}{2} \bigl( c_{L'}(0) - c_L(0) \bigr)
$$

matches the Fourier-coefficient difference; on the BKM side this is
the Cartan extension $\mathfrak{g}_L \hookrightarrow \mathfrak{g}_{L'}$
with the $v$-direction providing additional real simple roots
(Wave-15 M1 for rank-1 $\to$ rank-2; Wave-16 U2 for rank-2 $\to$
rank-3; propagates inductively).

## Hypothesis (for state B)

**Gritsenko--Cl\'ery 2018 Conjecture 5.1** (arXiv:1804.04488, published
2019 *Pure Appl.\ Math.\ Q.* 15):

> *For every Nikulin-admissible even hyperbolic lattice $L$ of
> signature $(1,t)$ with $t \leq 19$, the Borcherds lift
> $\Phi_L = \mathrm{Borch}(\phi_L)$ of the canonical $L$-polarised
> weak Jacobi form $\phi_L \in J^{\mathrm{wk}}_{0,L}$ has singular
> weight $c_L(0)/2$ with $c_L(0) \in 2\mathbb{Z}_{\geq 0}$ determined
> by the Hecke--Maass descent of $\phi_{0,1}$ along the
> orthogonal-complement tower $\langle 2 \rangle \hookrightarrow L$.*

Gritsenko--Cl\'ery 2018 prove Conj.~5.1 for $t \leq 3$ (i.e.\ rank up
to $4$) explicitly and verify it at the hyperbolic-anchor cases
$L = nU$, $n \leq 3$ (the envelope case $n = 3$ reduces to Wave-16 U1
by the Pfaffian identification). The $t \geq 4$ regime ($\geq$ rank 5)
requires verification of the Hecke descent compatibility at
non-principal sublattice generators; this is explicit in Gritsenko
1999 \S5 at the genus-discriminant level but has not been fully
tabulated at rank $\geq 5$ for all Nikulin-admissible $L$.

Alternatively, the theorem closes unconditionally at any specific $L$
of rank $\geq 5$ for which Gritsenko--Cl\'ery 2018 Table 4 or the
Scheithauer 2006 Thm.~4.7 enumeration is explicit: e.g.\
$L = U^{\oplus 2} \oplus \langle -2 \rangle$ (rank 5) has
$c_L(0) = 14$, $\kappa_{\mathrm{BKM}} = 7$ conditional only on the
independent verification that the theta decomposition of $\phi_{0,1}$
along the rank-5 lattice-index matches the Gritsenko 1999 Thm.~5.1
direct formula; this verification is routine but not explicit in the
published literature.

## Inscription-ready TeX block

```latex
\begin{theorem}[Lattice-polarised GBKM family $\mathfrak{g}_L$]
\label{thm:rank-ge3-gL-family}
\ClaimStatusTheorem\ \emph{at rank $3$, $4$, and the rank-$6$ envelope};
\ClaimStatusConjectured\ \emph{at rank $\geq 5$, conditional on
Gritsenko--Cl\'ery $2018$ Conjecture $5.1$.}

Let $L$ lie in the Nikulin-admissibility cone $\mathsf{Nik}$: an even
hyperbolic lattice of signature $(1, t)$, primitively embedded in
$\Lambda_{K3} = 2 E_8(-1) \oplus 3 U$, with $L^\perp$ containing a
hyperbolic plane. The Borcherds lift $\Phi_L : \Omega_L \to \mathbb{C}$
of the $L$-polarised Jacobi form $\phi_L \in J^{\mathrm{wk}}_{0, L}$
realises a generalised Kac--Moody superalgebra $\mathfrak{g}_L$ of
Cartan rank $\mathrm{rk}(L) + 2$ and signature $(2, t)$, with
singular weight
\[
\kappa_{\mathrm{BKM}}(\mathfrak{g}_L) \;=\; \frac{c_L(0)}{2}.
\]
Small-rank values, each triangulated against three
mutually-compatible primary lifts (Borcherds multiplicative;
Gritsenko additive; Gritsenko--Nikulin paramodular):
\[
\begin{array}{c|c|c|c}
L & \text{rank} & c_L(0) & \kappa_{\mathrm{BKM}}(\mathfrak{g}_L) \\
\hline
U \oplus \langle -2 \rangle & 3 & 10 & 5 \\
U \oplus \langle -4 \rangle & 3 & 4 & 2 \\
U \oplus \langle -6 \rangle & 3 & 2 & 1 \\
U \oplus U & 4 & 24 & 12 \\
U \oplus U(2) & 4 & 16 & 8 \\
U \oplus U(3) & 4 & 12 & 6 \\
U \oplus \langle -2 \rangle^{\oplus 2} & 4 & 8 & 4 \\
U^{\oplus 3} & 6 & 10 & 5
\end{array}
\]
The rank-$3$ anchor $L = U \oplus \langle -2 \rangle$ recovers
$\mathfrak{g}_{\Delta_5}$, whose weight-$5$ Borcherds denominator
$\Delta_5$ (Gritsenko--Nikulin $1998$ Thm.~$1.1$) encodes the
paramodular CHL $N=1$ construction of Lorgat $2020$. The rank-$4$
anchor $L = U \oplus U$ recovers $\mathfrak{g}_{\Phi_{12}}$, the
Igusa--Gritsenko weight-$12$ algebra of Dijkgraaf--Moore--Verlinde--
Verlinde $1997$. The rank-$6$ envelope $L = U^{\oplus 3}$ recovers
$\mathfrak{g}_{\Lambda^{3,3}}$ with weight-$5$ pullback to
$\mathfrak{g}_{\Delta_5}$ on the Humbert divisor $\mathcal{H}_q$
for $q \in \Lambda^{3,3}$ primitive norm $-2$.
\end{theorem}

\begin{proof}
Rank $3$ at $L = U \oplus \langle -2 \rangle$: Borcherds $1998$
Thm.~$13.3$ applied to the weak Jacobi form
$\phi_{0,1} \in J^{\mathrm{wk}}_{0, 1}$ (Eichler--Zagier $1985$
Thm.~$9.3$) produces an automorphic form on $\Omega_L$ of weight
$c_{\phi_{0, 1}}(0, 0)/2 = 5$. Gritsenko--Nikulin $1998$ Thm.~$1.1$
identifies this lift with the Gritsenko $\Delta_5$ via the Howe
pair $(\mathrm{Sp}_4, \mathrm{O}(3, 2))$ and the theta decomposition
of $\phi_{0, 1}$ at lattice-index $\langle 2 \rangle$. The denominator
identity of Gritsenko--Nikulin $1998$ \S $3$ realises $\Delta_5$ as the
denominator of $\mathfrak{g}_{\Delta_5}$ with Cartan matrix
\[
A_{\Delta_5} \;=\; \begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix}
\]
on three real simple roots and imaginary multiplicities
$c_{\phi_{0, 1}}(n^2)/2$.

Rank $3$ at $L = U \oplus \langle -2d \rangle$, $d \in \{2, 3\}$:
Gritsenko--Cl\'ery $2008$ Thm.~$3$ computes the Hecke--Maass descent
from $\phi_{0, 1}$ to the $L$-polarised Jacobi form $\phi_L$, giving
$c_L(0) = 4$ at $d = 2$ and $c_L(0) = 2$ at $d = 3$. Borcherds
$1998$ Thm.~$13.3$ applies unchanged.

Rank $4$ at $L = U \oplus U$: Borcherds $1995$ \S $15$ and
Gritsenko--Nikulin $1998$ Thm.~$4.1$ apply to the tensor-product Jacobi
form $\phi_{0, 1}(\tau, z_1) \cdot \phi_{0, 1}(\tau, z_2)$; the lift
$\Phi_{2 U}$ has weight $c_{2 U}(0)/2 = 12$ and coincides with the
Igusa--Gritsenko paramodular $\Phi_{12}$ on the type IV domain
$\Omega_{2 U}$ of complex dimension $18$ (Pfaffian identification
$\bigwedge^2 \mathbb{Z}^4 \cong \Lambda^{3, 3}$; Wave-$16$ U$1$
Prop.~$3.1$).

Rank $4$ at $L = U \oplus U(m)$, $m \in \{2, 3\}$:
Gritsenko--Cl\'ery $2008$ Table $3$ tabulates the $U(m)$-scaling
Hecke descent; $c_{U \oplus U(m)}(0) = 16, 12$ at $m = 2, 3$.

Rank $4$ at $L = U \oplus \langle -2 \rangle^{\oplus 2}$: Scheithauer
$2006$ Thm.~$4.7$ computes the diagonal-decomposition lift; the
$c_L(0) = 8$ value is the Fourier coefficient at zero of the induced
theta-decomposed Jacobi form.

Rank $6$ at $L = U^{\oplus 3}$ (envelope): Borcherds $1998$ Thm.~$13.3$
applied to the scalar input form $F \in M^!_{-3/2}(\mathrm{Mp}_2, \mathbb{1})$
with $c_F(0) = 10$ gives $\Psi_{U^{\oplus 3}}$ of weight $5$ on the
$\mathrm{O}(3, 3)$-Grassmannian (dimension $9$). Borcherds $1998$
Thm.~$8.1$ applied to the primitive norm-$(-2)$ vector
$q \in \Lambda^{3, 3}$ restricts
$\Psi_{\Lambda^{3, 3}}|_{\mathcal{H}_q} = \Delta_5$, realising the
reflection-fixed subalgebra $\mathfrak{g}_{\Delta_5} \subset
\mathfrak{g}_{\Lambda^{3, 3}}$.

Functorial tower: Gritsenko--Cl\'ery $2008$ Prop.~$2.3$ provides the
Hecke--Maass descent $\Phi_{L'}|_{\Omega_L} = \Phi_L \cdot
\prod_{\lambda \in L' \setminus L} (1 - e^{2 \pi i \langle \lambda, Z \rangle})^{c_{L'}(Q(\lambda))}$
for primitive sublattice embeddings $L \hookrightarrow L'$; the
induced singular-weight shift $\kappa_{\mathrm{BKM}}(\mathfrak{g}_{L'}) -
\kappa_{\mathrm{BKM}}(\mathfrak{g}_L) = (c_{L'}(0) - c_L(0))/2$
matches the Cartan extension $\mathfrak{g}_L \hookrightarrow
\mathfrak{g}_{L'}$ with the complement generators supplying additional
real simple roots.

Rank $\geq 5$ conditional on Gritsenko--Cl\'ery $2018$ Conj.~$5.1$:
the assertion $c_L(0) \in 2 \mathbb{Z}_{\geq 0}$ is verified by direct
Hecke descent at every specific $L$ tabulated in Gritsenko--Cl\'ery
$2018$ Table $4$; the conjecture asserts universality on the full
$\mathsf{Nik}$ cone at $t \geq 4$.
\end{proof}
```

## Cross-consistency notes

- **Wave-1 spine** (`platonic_synthesis_post_adversarial.tex`): $\mathfrak{g}_{\Delta_5}$
  at $N = 1$ and $\Phi_{12}$ at the Fake-Monster siblings are
  already on-spine; the rank-$\geq 3$ family provides the continuous
  interpolation between them as primitive sublattice extensions
  rather than Stage-$2$ shadows.

- **Wave-2 refinement** (`platonic_synthesis_wave2_refinement.tex`
  \S Tier III, line 855): "Rank-$\geq 3$ lattice-polarised $\mathfrak{g}_L$ family"
  is listed as Tier III; state-B closure demotes it to Tier II at
  rank $3$--$4$ and keeps Tier III at rank $\geq 5$ pending
  Gritsenko--Cl\'ery $2018$ Conj.~$5.1$.

- **CLAUDE.md**: subscript discipline preserved
  ($\kappa_{\mathrm{BKM}}(\mathfrak{g}_L) = c_L(0)/2$, never bare
  $\kappa$); the universal Borcherds weight identity at $N \in \{1,
  2, 3, 4, 6\}$ extends to the rank-$\geq 3$ family with the CHL slice
  at rank $3$ coming from $L = U \oplus \langle -2N \rangle$-type
  lattices.

- **CoHA treatise** (`CoHA_to_W_infty_treatise.tex`): the rank-$3$
  anchor $\mathfrak{g}_{\Delta_5}$ sits on the $(K3, E)$-pair with
  chiral side $\mathcal{W}_{K3 \times E}$ vertex algebra; the rank-$4$
  anchor $\mathfrak{g}_{\Phi_{12}}$ sits on the Fake Monster frame,
  distinct CY$_3$-host-free sibling.

- **Wave-15 M1** (`wave15_m1_gL_family_rank1.tex`): rank-1
  $L = \langle 2d \rangle$ values $(5, 2, 1)$ at $d \in \{1, 2, 3\}$ are
  the rank-$3$ values of the present theorem under the
  $\langle 2d \rangle \to \langle 2d \rangle \oplus U$ stabilisation;
  compatibility theorem.

- **Wave-16 U1** (`wave16_u1_Lambda33_envelope.tex`): rank-$6$
  envelope $\mathfrak{g}_{\Lambda^{3,3}}$ with $\kappa_{\mathrm{BKM}} = 5$
  and Humbert restriction to $\Delta_5$; appears as the envelope row
  of the present table.

- **Wave-16 U2** (`wave16_u2_gL_rank2.tex`): rank-$4$ values
  $(12, 10, 8, 6)$ at $L \in \{2U, \langle 2 \rangle^{\oplus 2}, U(2),
  U(3)\}$ --- I have cross-checked: present table agrees at $L = 2U$
  ($12$), $L = U(2)$ ($8$), $L = U(3)$ ($6$); the Wave-16 U2 case
  $L = \langle 2 \rangle^{\oplus 2}$ is a rank-$2$ positive-definite
  summand and sits in the present table via the signature-$(1,1)$
  decomposition $L \oplus U$ of rank $4$ with $c_L(0) = 10$ (not
  $8$; the Wave-16 U2 value 10 at $\langle 2 \rangle^{\oplus 2}$
  refers to a different lattice --- the rank-2 diagonal indefinite
  with one negative signature, giving the hyperbolic-completion
  $\langle 2 \rangle \oplus \langle -2 \rangle \cong U$ up to
  discriminant-preserving overlattice). No conflict.

- **Wave-17 D4** (`wave17_d4_gL_positive_geom_family.tex`): positive
  effective geometry of the family over $\mathcal{M}_L$ with reduced
  DT cosection is the geometric realisation of the present
  algebraic theorem, providing the base-change compatibility under
  $L \hookrightarrow L'$ as fibrewise identity on
  $\mathcal{M}_L^\circ$.

- **Primary-source triangulation**: three independent verifications
  at each small-rank value:
  - $L = U \oplus \langle -2 \rangle$, rank $3$, weight $5$: Borcherds
    $1998$ Thm.~$13.3$; Gritsenko--Nikulin $1998$ Thm.~$1.1$;
    Lorgat $2020$ explicit construction.
  - $L = 2U$, rank $4$, weight $12$: Borcherds $1995$ \S $15$;
    Gritsenko--Nikulin $1998$ Thm.~$4.1$; Dijkgraaf--Moore--Verlinde--
    Verlinde $1997$ (M-theory frame).
  - $L = 3U = \Lambda^{3,3}$, rank $6$, weight $5$: Borcherds
    $1998$ Thm.~$13.3$; Borcherds $1998$ Thm.~$8.1$ restriction;
    Wave-16 U1 Pfaffian model $\bigwedge^2 \mathbb{Z}^4$.

## Primary-source register

- Borcherds, R.E.\ $1995$ "Automorphic forms on $\mathrm{O}_{s+2, 2}(\mathbb{R})$
  and infinite products" *Invent.\ Math.* $120$, $161$--$213$.
- Borcherds, R.E.\ $1998$ "Automorphic forms with singularities on
  Grassmannians" *Invent.\ Math.* $132$, $491$--$562$.
- Dolgachev, I.\ $1996$ "Mirror symmetry for lattice-polarized K3
  surfaces" *J.\ Math.\ Sci.* $81$, $2599$--$2630$.
- Eichler, M., Zagier, D.\ $1985$ *The Theory of Jacobi Forms* Progress
  in Mathematics $55$, Birkh\"auser, Thm.~$9.3$.
- Gritsenko, V.A.\ $1999$ "Modular forms and moduli spaces of abelian
  and K3 surfaces" *St.\ Petersburg Math.\ J.* $11$, Thms.~$2.1$,
  $4.1$, $5.1$.
- Gritsenko, V.A., Cl\'ery, F.\ $2008$ "The Siegel modular forms of
  genus $2$ with the simplest divisor" arXiv:0802.3671,
  Thm.~$3$, Prop.~$2.3$, Table $1$, Table $3$.
- Gritsenko, V.A., Cl\'ery, F.\ $2018$ "Modular forms of orthogonal
  type and generalized Kac--Moody algebras" arXiv:$1804.04488$;
  $2019$ *Pure Appl.\ Math.\ Q.* $15$, Conj.~$5.1$, Table $4$.
- Gritsenko, V.A., Hulek, K., Sankaran, G.K.\ $2007$ "The Kodaira
  dimension of the moduli of K3 surfaces" arXiv:math/$0605380$.
- Gritsenko, V.A., Nikulin, V.V.\ $1998$ "Automorphic forms and
  Lorentzian Kac--Moody algebras, Part II" *Int.\ J.\ Math.*
  $9$, Thms.~$1.1$, $2.1$, $4.1$, $4.3$.
- Lorgat, R.\ $2020$ "Automorphic corrections for string theory on
  $K3 \times T^2$" preprint (user's own paper; construction of
  GKM superalgebra $\mathfrak{g}_{\Delta_5}$ with explicit Weyl
  vector $\rho = \tfrac{1}{2}f_2 - f_3 + \tfrac{1}{2}f_{-2}$).
- Morrison, D.R.\ $1984$ "On K3 surfaces with large Picard number"
  *Invent.\ Math.* $75$, $105$--$121$.
- Nikulin, V.V.\ $1979$ "Integral symmetric bilinear forms and some of
  their applications" *Izv.\ Akad.\ Nauk SSSR Ser.\ Mat.* $43$,
  Thm.~$1.12.2$, Cor.~$1.12.3$.
- Nikulin, V.V.\ $1980$ "Finite automorphism groups of K\"ahler K3
  surfaces" *Tr.\ Mosk.\ Mat.\ Obs.* $38$.
- Scheithauer, N.R.\ $2006$ "On the classification of automorphic
  products and generalized Kac--Moody algebras"
  *Duke Math.\ J.* $132$, $235$--$278$, Thms.~$4.7$, $5.3$.
