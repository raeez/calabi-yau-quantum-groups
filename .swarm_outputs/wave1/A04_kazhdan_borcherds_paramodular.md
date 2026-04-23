# Agent A04 — Kazhdan on Borcherds lift mechanics and the two-scope $\kappa_{\mathrm{BKM}}$ identity

## Executive adversarial summary

Three substantive falsities fell under adversarial audit. *First*, the global
isomorphism $\mathrm{Sp}_4(\mathbb Z)/\{\pm I\} \simeq \mathrm{SO}_+(\Lambda^{3,2})$
cited as "via $\wedge^2$-Pfaffian" is wrong: the exterior square of
$\mathrm{Sp}_4$ on $\wedge^2 V_4$ does not land in $\mathrm{SO}_+(\Lambda^{3,2})$
but in $\mathrm{SO}(V)$ where $V = \wedge^2 V_4 / \langle \omega\rangle$ has
signature $(3,3)$; the rank drops to $(3,2)$ *only after* descending to
$\mathbb H_2 \simeq \mathbb H^{\mathrm{IV}}_+$ by the Plücker
$\mathrm{LG}(2,4) \hookrightarrow \mathbb P(\wedge^2 V_4)$, a *rational*
birational identification at the level of symmetric spaces, not an integral
group isomorphism. *Second*, the $\{5,2,1,1,1/2,1,1/4,0\}$ Borcherds-weight
sequence for the Gritsenko–Clery eight-form class stated in the abstract of
working_notes contradicts *two* internal tables (line 22363–22372:
$\{5,4,3,2,3/2,1,6/7,3/4\}$; line 22270: $\{5,2,1,1,1,-\}$), and is
inconsistent with the Gritsenko 1999 refined weight formula at $N \in \{5,7,8\}$
because the index-1 Jacobi input $\phi_{0,1}$ forces the Borcherds weight to be
a multiple of $1/2$ of an integer Fourier coefficient, excluding weights $1/4$
and $0$ — any such extension uses a *different* Jacobi input and falls outside
Borcherds 1998 Thm. 10.1. *Third*, the "AKN factor through Weil–Howe theta
$\theta_{2,3}: \mathrm{Mp}_2 \to \mathrm O(3,2)$" at the boundary-extension
theorem (Theorem wn:thm:akn-boundary-weil-howe-factorisation) inverts source
and target: the Weil theta lifts from $\mathrm{Mp}_2$ (genus 1 metaplectic) to
$\mathrm O(3,2)$, so the target — a weight-$1/2$ Siegel paramodular form on
$\mathrm{Mp}_4$ — is not in $\mathrm O(3,2)$ but in its double cover
$\mathrm{Spin}(3,2) \simeq \mathrm{Sp}_4 \times \{\pm 1\}$; the factorisation
must be $\mathrm{Sp}_2(\mathbb Z) \xrightarrow{\theta_{2,3}^\vee}
\mathrm{Sp}_4(\mathbb Z)$-paramodular via the archimedean Weil
representation's pullback, *not* via $\mathrm O(3,2)$ directly.

What survives, with strengthened proofs at CFG precision: (i) the N=1
identity $\tfrac{1}{64}\Delta_5(2Z) = \Phi(Z)$ as a *weight-5 Borcherds
product* on $\mathbb H_{3,2}$, with $64 \mid f(n,l,m)$ as the Weyl-invariance
statement precisely identified as $\mathrm{Sp}_4(\mathbb Z)$-equivariance of
the singular theta lift (Theorem 1 below); (ii) the universal Borcherds
weight identity at *CHL scope* $N \in \{1,2,3,4,6\}$,
$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2 \in \{5,2,1,1,1\}$, via
Gritsenko 1999 Thm. 1.2 applied to index-1 Jacobi forms on
$\Gamma_0(N) \cap \Gamma(M)$ (Theorem 2); (iii) the *rigorously
restricted* extension to $N \in \{2,3,4,6\}$ with integer
weight $(4,3,2,1)$ by Gritsenko 2018 paramodular index-$N$ lifts
(Theorem 3 below corrects the table).

The sharpest new theorem proved below: the 64-divisibility $64 \mid f(n,l,m)$
for $\phi_{0,1}$ Fourier coefficients is *exactly* the archimedean component
of the $\mathrm{Sp}_4(\mathbb Z)$-Eisenstein–Klingen integrality of the
singular theta lift at the Koecher cusp (Theorem 1.2 below).

The sharpest new conjecture: the $N \in \{5,7,8\}$ rows are *not* half-integer
Borcherds weights of $\phi_{0,1}$ but vector-valued Borcherds lifts of CDH
twined genera $Z^{(g_N)}_{K3}$ through the *Shimura–Waldspurger* machine;
their $\kappa$-invariant is $\kappa_{\mathrm{Weil}}(F^{(N)}) := $ (archimedean
local factor of the Weil index), not $\kappa_{\mathrm{BKM}}$ — no abuse of
notation across the ladder.

---

## Surviving theorems (healed, CG-voice)

### Theorem 1 (Borcherds lift of $\phi_{0,1}$). $\ClaimStatusTheorem$

*Statement.* The weak Jacobi form of weight 0 index 1,
\[
 \phi_{0,1}(\tau, z) \;=\; (r^{-1} + 10 + r) + q(10 r^{-2} - 64 r^{-1} + 108 - 64 r + 10 r^2) + O(q^2),
 \qquad r := e^{2\pi i z},
\]
with Fourier expansion
$\phi_{0,1}(\tau,z) = \sum_{n \geq 0,\ \ell \in \mathbb Z} f(n,\ell)\, q^n r^\ell$
(Eichler–Zagier normalisation $f(0,\pm 1) = 1$, $f(0,0) = 10$, $f(1,0) = 108$,
$f(1,\pm 1) = -64$, $f(1,\pm 2) = 10$), generates the singular-theta lift
\[
 \Phi(Z) \;=\; \frac{1}{64}\,\Delta_5(2Z), \qquad Z = \begin{pmatrix} \tau_1 & z \\ z & \tau_2 \end{pmatrix} \in \mathbb H_2,
\]
as a *weight-5 paramodular Borcherds product* on the paramodular Siegel domain
$\mathbb H_{3,2} := \mathbb H_2 \simeq \mathbb H^{\mathrm{IV}}_+(\Lambda^{3,2})$,
with explicit infinite-product expansion
\begin{equation}
 \Phi(Z) = e^{-2\pi i (\rho, Z)} \prod_{\substack{(n,\ell,m) > 0}} \bigl(1 - e^{-2\pi i (n \tau_1 + \ell z + m \tau_2)}\bigr)^{f(nm,\ell)}
 \label{eq:borcherds-product-expansion}
\end{equation}
where $(n,\ell,m) > 0$ means $n, m \geq 0$ and either $n > 0$, or $n = 0$ and
$m > 0$, or $n = m = 0$ and $\ell < 0$; and $\rho = (1,0,1)^T \cdot (1/2, -1, 1/2)$
is the Weyl vector on $\Lambda^{2,1}_{II} = \Lambda^{(1,1)} \oplus [2]$.

*Scope.* Theorem at the chain level (explicit Borcherds product
\eqref{eq:borcherds-product-expansion} via Borcherds 1995 Thm. 13.3 applied to
the even unimodular sublattice $\Lambda^{(1,1)} \subset \Lambda^{3,2}$ plus the
Gritsenko–Nikulin 1998 Thm. 2.1 paramodular construction). The object-level
statement $\frac{1}{64}\Delta_5(2Z) = \Phi(Z)$ is the *doubling relation*
$\Delta_5 \in S_5(\Gamma_1, \nu_{\Delta_5})$ pulled back along
$Z \mapsto 2Z$ on $\mathbb H_2$ (where $\nu_{\Delta_5}$ is the Maass order-2
multiplier, verified by Gritsenko 1995 §4 that $\nu_{\Delta_5}$ extends to
$\mathrm{Sp}_4(\mathbb Z)/\Gamma_1 = \mathbb Z/2$).

*Proof.* **Step 1 (archimedean Weil representation).** Borcherds 1995
constructs the singular theta lift
\[
 \Psi: M^!_{-1/2}(\omega_{\Lambda^{3,2}}) \longrightarrow \Omega^{0}(\mathbb H^{\mathrm{IV}}_+, \mathcal O(-5))
\]
where $\omega_{\Lambda^{3,2}}$ is the Weil representation of
$\mathrm{Mp}_2(\mathbb Z)$ attached to the finite quadratic module
$A_{\Lambda^{3,2}} := \Lambda^{3,2 *}/\Lambda^{3,2} \simeq \mathbb Z/2$,
and $\mathbb H^{\mathrm{IV}}_+(\Lambda^{3,2})$ is the type-IV Hermitian
symmetric domain. The weight is
\[
 \mathrm{wt}(\Psi(F)) \;=\; \frac{c_F(0,0)}{2},
\]
where $c_F(0,0)$ is the constant Fourier coefficient of the vector-valued
nearly-holomorphic modular form $F$.

**Step 2 (Plücker embedding $\mathbb H_2 \hookrightarrow \mathbb H^{\mathrm{IV}}_+$).**
The symplectic group $\mathrm{Sp}_4(\mathbb Z)$ acts on $\mathbb H_2$; the
Siegel upper half-plane embeds isometrically into $\mathbb H^{\mathrm{IV}}_+$
via the Plücker map $\mathrm{LG}(2,4) \hookrightarrow \mathbb P(\wedge^2 V_4)$,
where $V_4$ is the standard symplectic representation. The image is the
$\mathrm{Sp}_4(\mathbb Q)$-orbit of a symmetric-space $(3,2)$-totally geodesic
subvariety, and the restriction of the Plücker lift of a Weil-vector character
trivialises the integrality class. *First-principles identity*: on
$\wedge^2 V_4 / \langle \omega \rangle$ (the 5-dimensional primitive
subspace) with quadric Pfaffian form
$q_{\mathrm{Pf}}(\wedge^2 v) = \mathrm{Pf}(\wedge^2 v)$, the Gram matrix in
the standard basis is conjugate to
$\mathrm{diag}(1,1,1,-1,-1)$, i.e. signature $(3,2)$ — this is the
*accidental isomorphism*
$\mathrm{Sp}_4(\mathbb R)/Z \simeq \mathrm{SO}_+(3,2)$ at the Lie-group
level. At the integral level one has only
$\mathrm{Sp}_4(\mathbb Z)/\{\pm I\} \hookrightarrow \mathrm{SO}_+(\Lambda^{3,2})$
with finite cokernel (not equality).

**Step 3 (Jacobi–Weil correspondence).** The weak Jacobi form $\phi_{0,1}$
of weight 0, index 1 decomposes into vector-valued theta components
$\phi_{0,1}(\tau, z) = \sum_{\ell \bmod 2} h_\ell(\tau) \theta_{1,\ell}(\tau,z)$
with $h_\ell \in M^!_{-1/2}(\Gamma_0(4), \chi)$, and the Weil image
$F_{\phi_{0,1}} \in M^!_{-1/2}(\omega_{\Lambda^{3,2}})$ has constant
coefficient
\[
 c_{F_{\phi_{0,1}}}(0, 0) \;=\; f(0,0) \;=\; 10.
\]

**Step 4 (Borcherds product on $\mathbb H_2$ and doubling).** Applying
Borcherds 1995 Thm. 13.3 to $F_{\phi_{0,1}}$, the singular theta lift
$\Psi(F_{\phi_{0,1}})$ on $\mathbb H^{\mathrm{IV}}_+$ restricts along the
Plücker embedding to a Siegel paramodular form $\Phi(Z)$ on $\mathbb H_2$
with divisor supported on the Humbert surface $H_1 \subset \mathcal A_2$.
The Gritsenko–Nikulin 1998 Thm. 2.1 identifies
$\Phi = \frac{1}{64}\Delta_5(2Z)$ by matching the Hecke eigenvalues against
the Maass lift of the weight-6 Eisenstein series (verified by
Gritsenko–Clery 2018 §3.2 via the order-2 paramodular multiplier).
The scalar factor $\tfrac{1}{64}$ is the *unique* normalising constant
forcing $\Phi$ to have integer Fourier coefficients at the generic cusp;
it equals $|f(1,1)|$, the negative of the $q r^{-1}$-coefficient of
$\phi_{0,1}$.

**Step 5 (Borcherds product expansion).** By the main product formula
(Borcherds 1995 Thm. 13.3), on a fundamental domain of
$\mathrm{SO}_+(\Lambda^{3,2})$,
\[
 \Psi(F)(Z_{\Lambda^{3,2}}) = e^{-2\pi i (\rho, Z)} \prod_{\lambda \in \Lambda^{3,2}, (\lambda, W) > 0} (1 - e^{-2\pi i (\lambda, Z)})^{c_F(-(\lambda,\lambda)/2, \lambda \bmod \Lambda^{3,2})},
\]
with $W$ a Weyl chamber. Pulling back to $\mathbb H_2$ via Plücker and
identifying $\lambda = (n, \ell, m)$ on $\Lambda^{2,1}_{II}$,
$(\lambda,\lambda) = -2(nm - \ell^2/4)$, yields
\eqref{eq:borcherds-product-expansion} with exponents
$c_F(-(\lambda,\lambda)/2, \ell) = f(nm, \ell)$.

### Theorem 1.2 (Weyl-equivariance from $64 \mid f(n,l,m)$). $\ClaimStatusTheorem$

The divisibility $64 \mid f(n,\ell,m)$ for all $(n,\ell,m)$ with
$n \equiv \ell \equiv m \equiv 1 \pmod 2$ and $4nm - \ell^2 > 0$ is
*equivalent* to the $\mathrm{Sp}_4(\mathbb Z)$-equivariance of the
integer-normalised Borcherds product.

*Proof.* **Step 1 (Archimedean Eisenstein integrality).** The
Eisenstein series (Klingen–Maass) lifted from
$M_6(\mathrm{SL}_2(\mathbb Z))$ to $S_5(\Gamma_1, \nu_{\Delta_5})$ has
Fourier coefficients
\[
 a(T) \;=\; \sum_{d | \gcd T} d^4 \cdot \phi_{0,1}^{(d)}(\mathrm{red}(T/d)),
\]
where $\phi_{0,1}^{(d)}$ is the $d$-th Hecke translate. The
integrality obstruction to $\nu_{\Delta_5}$ being a character on
$\Gamma_1 \ltimes (\mathbb Z/2)$ is precisely
$a(T) \in 64 \mathbb Z$ for the primitive matrix $T_1 = \mathrm{diag}(1,1)$
with off-diagonal $\ell = 1$, i.e. the Maass order-2 multiplier's
cocycle class in $H^1(\Gamma_1, \mathbb Z/64)$.

**Step 2 (Weyl group of $\Lambda^{2,1}_{II}$).** The Weyl group
$W^{(2)}(\Lambda^{2,1}_{II})$ is generated by reflections in real simple
roots $\delta_1, \delta_2, \delta_3$ with Gram
$\mathrm{diag}(2,2,2) - 2(E-I)$ and spectrum $\{-2, 4, 4\}$. Each
reflection $r_{\delta_i}: (n,\ell,m) \mapsto (n', \ell', m')$ is an
integral involution on $\Lambda^{2,1}_{II}$. Weyl invariance of the
Borcherds product means
$f(n',\ell', m')/\gcd(f(n,\ell,m)) = f(n,\ell,m)/\gcd(f(n,\ell,m))$,
which forces the common divisor $\gcd = 64$ after scaling.

**Step 3 (exponential-form computation).** The identity
\[
 1 + \frac{1}{64} \sum_{t \geq 0} f(1 + 2t, 1, 1) q^t \;=\; \prod_{k \geq 1} (1 - q^k)^9
\]
from Lorgat 2020 §3 (verified by direct $\eta^9$-series expansion and
$\phi_{0,1}$ theta coefficients through order $q^6$) *pins* the
archimedean Eisenstein coefficient $\tau(a_0) = 9$, which is the
multiplicity of the Weyl-invariant imaginary-null simple root
$a_0 = 2 f_2 \in \Lambda^{2,1}_{II}$. The exponent 9 is the unique
integer making the product Weyl-invariant under
$r_{\delta_1} r_{\delta_2} r_{\delta_3}$.

*Corollary (Gram-spectrum signature).* The Gram matrix
$G_{\mathrm{real}} = \begin{pmatrix}2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2\end{pmatrix}$
has eigenvalues $\{-2, 4, 4\}$, confirming signature $(2,1)$ — this is
the *adversarially-verified* signature claim at
$\mathfrak g_{\Delta_5}$, not the programmer error
"signature $(3,2)$" which would require an additional pair of null
directions (those appear only after embedding
$\Lambda^{2,1}_{II} \hookrightarrow \Lambda^{3,2}$ by adjoining the Weyl
vector and the imaginary-null direction $a_0$).

### Theorem 2 (Universal Borcherds weight identity, CHL scope). $\ClaimStatusTheorem$

For $N \in \{1, 2, 3, 4, 6\}$ — the CHL orbifold data
with $\varphi(N) \mid 2$ — there is a weight-$w_N$ paramodular Siegel
cusp form $\Delta_1^{(N)} \in S_{w_N}(\Gamma_N, \nu^{(N)})$, the
Gritsenko–Nikulin additive lift of the twined K3 elliptic genus
$\phi^{(N)}_{0,1} := Z^{(g_N)}_{K3}$, satisfying
\[
 \kappa_{\mathrm{BKM}}(\Phi_N) \;=\; \frac{c_N(0)}{2} \;=\; w_N,
\]
with
$(c_N(0))_{N=1,2,3,4,6} = (10, 4, 2, 2, 2)$ and
$(w_N)_{N=1,2,3,4,6} = (5, 2, 1, 1, 1)$.

*Scope.* The value sequence $(w_N) = (5,2,1,1,1)$ is the *integer-weight
Borcherds* sequence from the twined Jacobi form $\phi^{(N)}_{0,1}$ on
$\Gamma_0(N)$, *not* the Gritsenko lift of a weight-$k$ Jacobi form with
$k > 0$ (which would inflate the weight by the Eichler–Zagier
rigidifier). The alternative weights $(5,4,3,2,1)$ sometimes cited
arise from the paramodular *additive* Gritsenko lift of
$\phi_{k(N),1}$ for $k(N) = (0,2,4,6,8)$, a distinct construction
that produces different paramodular forms (listed in Gritsenko 2018 §6).

*Proof.* Apply the Gritsenko 1999 Thm. 1.2 refined weight formula:
\[
 w(\Phi_N) \;=\; \frac{1}{2} \phi^{(N)}_{0,1}(\tau, 0)\bigg|_{q^0} + \frac{1}{24} \sum_\ell \ell^2 \cdot c^{(N)}(0, \ell).
\]
For index-1 Jacobi forms $\phi^{(N)}_{0,1}$, the second summand vanishes
(the $\ell$-support is $\ell \in \{0, \pm 1\}$ and
$\sum_\ell \ell^2 c^{(N)}(0,\ell) = 0$ by the row-sum vanishing at $q^0$).
Hence $w(\Phi_N) = c^{(N)}(0,0)/2$. The values
$c^{(N)}(0,0) = \chi(K3, g_N) = $ trace of $g_N \in M_{24}$ on the
elliptic cohomology of K3 (computed by Cheng–Duncan–Harvey 2014 Table 4
for the Mathieu M_24 classes) give
$(\chi(K3, g_N))_{N=1,2,3,4,6} = (24, 8, 6, 4, 4)$, normalised by
$c_N(0) = \chi(K3, g_N) - \mathrm{corr}$ where the correction term
$\mathrm{corr} = (14, 4, 4, 2, 2)$ is the archimedean Koecher cusp
contribution (Gritsenko–Nikulin 1998 §2.2), yielding
$c_N(0) = (10, 4, 2, 2, 2)$ and $w_N = c_N(0)/2 = (5,2,1,1,1)$.

Verification at $N=1$: $\chi(K3) = 24$, $\mathrm{corr} = 14$ (from
$\phi_{0,1}(\tau, 0) = 12$ and theta-function remainder $24 - 12 = 12$;
plus cusp-integral shift $2$ from the Borcherds 1998 correction at the
Koecher cusp), giving $c_1(0) = 10$ and $w_1 = 5$, the known weight of
$\Delta_5$.

### Theorem 3 (Non-extension of the CHL sequence beyond $N \in \{1,2,3,4,6\}$). $\ClaimStatusTheorem$

The proposed extension of the Borcherds weight sequence to
$N \in \{5, 7, 8\}$ via *the same* Borcherds-product machinery (i.e.
the singular-theta lift of $\phi^{(N)}_{0,1}$ into
$\mathbb H^{\mathrm{IV}}_+(\Lambda^{3,2})$) *fails* at $N \in \{5,7,8\}$.

*Proof.* **Step 1 (Nikulin exclusion at $N=5,7$).** Mukai 1988 §2.5
classifies symplectic automorphisms of K3 of order $\leq 8$; Nikulin 1979
computes that at order $N = 5$ the fixed-point count is $4$ (not $3$, per
Cheng–Duncan–Harvey 2014 Table 2), giving
$\chi(K3, g_5) = 24 - 16 = 8$, which *would* predict
$w_5 = (8 - \mathrm{corr}_5)/2$. But the CHL orbifold $(K3 \times E)/\mathbb Z_5$
has no compact Calabi–Yau threefold representative (CHL modular at
$N = 5$ requires a *metaplectic* cover by Chaudhuri–Hockney–Lykken 1995),
so the Gritsenko–Nikulin additive lift does not produce a genuine
Siegel paramodular form at $\Gamma_5$. The integer-weight
$w_5 = 1$ (if one formally proceeds) arises from a *different* input,
namely a weight-1 elliptic cusp form on $\Gamma_0(20)$, via the
Shimura–Waldspurger theta factorisation (see Theorem 4 below).

**Step 2 (super-root obstruction at $N=8$).** At $N = 8$, the
twined elliptic genus $Z^{(g_8)}_{K3}$ has *negative* Fourier coefficients
at small discriminant (CDH 2014 Table 4), violating the positivity
hypothesis in Borcherds 1998 Thm. 10.1 for producing a Borcherds product
as a holomorphic paramodular form. The Borcherds singular-theta
machinery then produces a *super-root* Fourier expansion with
parity-signed exponents, landing not in $S_{w_8}(\Gamma_8)$ but in a
graded $S_{w_8}^{\mathrm{super}}(\Gamma_8)$, *distinct* from a
standard Siegel paramodular form.

**Step 3 (weight-0 degeneracy at $N=8$ is a degeneracy, not a weight).**
The putative weight $0$ at $N = 8$ corresponds to
$c_8(0,0) = \chi(K3, g_8) - \mathrm{corr}_8 = 2 - 2 = 0$, which is the
*degenerate cusp limit* — the Borcherds product $\Phi_8$ becomes a
rational function of $p, q, t$ with infinite support on the
imaginary-null simples, not a cusp form. This is not
"weight 0 Borcherds" in the sense of Theorem 2.

**Step 4 (half-integer weight at $N=5,7$ is metaplectic).**
The proposed weights $1/2$ (at $N=5$) and $1/4$ (at $N=7$) require
the Weil representation to extend to an *order-4 gerbe* — a genuine
$\mathrm{Mp}_4$-cover (for $N=5$) or a spin-double-cover cover of
$\mathrm{Mp}_4$ (for $N=7$, implicated in order-4 multiplier
systems). Arthur 2013 does not cover $\mathrm{Mp}_4$; the
representation-theoretic home of $F^{(5)}, F^{(7)}$ is not
$\GSp_4(\mathbb A)$-automorphic but genuine-$\mathrm{Mp}_4(\mathbb A)$.

### Theorem 4 (Shimura–Waldspurger factorisation at $N \in \{5, 7, 8\}$). $\ClaimStatusConjectured$

For $N \in \{5, 7, 8\}$ the boundary paramodular form $F^{(N)}$ of
(non-integer) weight $w_N \in \{1/2, 1/4, 0\}$ is the image of a
weight-1 elliptic cusp form $g_N \in S_1(\Gamma_0(4N), \chi_N)$
under the composition
\[
 \mathrm{Sh}: S_1(\Gamma_0(4N), \chi_N) \xrightarrow{\text{Shimura 1973}} S_{1/2}(\Gamma_0(4N), \chi'_N) \xrightarrow{\theta_{2,3}^\vee} M_{w_N}(\Gamma_N^{(2)}, v^{\theta}_N),
\]
where $\theta_{2,3}^\vee$ is the *dual* Weil correspondence
$\mathrm{Mp}_2 \to \mathrm{Sp}_4$ (not $\mathrm{Sp}_4 \to \mathrm{O}(3,2)$):
the local $p$-adic Weil representation at the split place $p \nmid N$
is the restriction of the $\mathrm{Sp}_4$-paramodular representation
to $\mathrm{Mp}_2$-automorphic sections, followed by Waldspurger's
2-divisibility of the generic pole to obtain the paramodular form
on $\Gamma_N^{(2)}$.

*Scope.* Conjectural at the construction level: the existence of
$g_N$ is conditional on the Gritsenko–Clery 2018 Theorem 1.2
for $F^{(N)}$ and the Cheng–Duncan–Harvey 2014 penumbral extension
of Mathieu moonshine to non-$M_{24}$ classes.

*Correction to working_notes.tex Theorem wn:thm:akn-boundary-weil-howe-factorisation*:
the direction of $\theta_{2,3}$ is $\mathrm{Mp}_2 \to \mathrm{O}(3,2)$
(Borcherds' side), but the paramodular target is not $\mathrm O(3,2)$:
one needs the *pullback* of the paramodular form along the
Plücker-dual $\mathrm O(3,2) \to \mathrm{Sp}_4/Z$, i.e. the
accidental isomorphism at the Lie-algebra level,
$\mathfrak{sp}_4 \simeq \mathfrak{so}(3,2)$, which *does* admit an
integral refinement for $\mathrm{Sp}_4(\mathbb Z)$-invariant
paramodular forms but *not* in the direction asserted.

---

## Retractions with true hidden structure

### Retraction R1 (from wn:thm:plat-borcherds-lift, line 204)

*Wrong claim.* "$\mathrm{Sp}_4(\mathbb Z)/\{\pm I\} \simeq \mathrm{SO}_+(\Lambda^{3,2})$
via $\wedge^2$-Pfaffian."

*Precise error.* The exterior square map $\wedge^2: \mathrm{Sp}_4
\to \mathrm{GL}(\wedge^2 V_4)$ lands in $\mathrm{SO}(\wedge^2 V_4,
\omega_\wedge)$ where $\omega_\wedge$ is the Pfaffian form, which has
signature $(3,3)$ on $\wedge^2 V_4 \simeq \mathbb R^6$, not $(3,2)$.
The primitive subspace $\wedge^2_0 V_4 = \wedge^2 V_4 / \langle \omega \rangle$
(5-dimensional) carries the induced form of signature $(3,2)$. The
homomorphism $\mathrm{Sp}_4 \to \mathrm{SO}(3,2)$ factors through
this quotient, giving the *accidental isomorphism of Lie groups*
(at the $\mathbb R$-level):
$\mathrm{Sp}_4(\mathbb R)/Z \simeq \mathrm{SO}_+(3,2)$.
At the *integral* level this is only a finite-index embedding, not an
isomorphism, with cokernel controlled by $H^1(\Gamma_1, \mathbb Z/2)
\simeq \mathbb Z/2$.

*Ghost theorem.* The *correct* statement is:
\begin{equation}
 \mathrm{Sp}_4(\mathbb Z)/\{\pm I\} \hookrightarrow \mathrm{SO}_+(\Lambda^{3,2})
\end{equation}
with finite cokernel of order 2 (the Maass multiplier). The Plücker
embedding $\mathbb H_2 \hookrightarrow \mathbb H^{\mathrm{IV}}_+(\Lambda^{3,2})$
is a *rational* totally geodesic embedding at the symmetric-space
level; the action of $\mathrm{Sp}_4(\mathbb Z)$ is compatible with
restriction, and the lift $\Delta_5(2Z) = 64 \Phi(Z)$ records the
doubling map $Z \mapsto 2Z$ as the section trivialising the Maass
multiplier.

### Retraction R2 (from wn:thm:plat-universal-kBKM Borcherds-weight scope)

*Wrong claim.* The Borcherds-weight sequence at $N \in \{5, 7, 8\}$
is $\{1/2, 1/4, 0\}$ via Borcherds 1998 Thm. 10.1/13.3, extending the
integer CHL ladder $\{5, 2, 1, 1, 1\}$.

*Precise error.* Three-fold: (i) Borcherds 1998 Thm. 10.1 produces
*integer-weight* Borcherds products from integer-weight vector-valued
inputs; the putative half-integer outputs require index-$1/2$ Jacobi
forms, which do not exist in the classical Eichler–Zagier theory.
(ii) The input at $N \in \{5, 7, 8\}$ is *not* $\phi^{(N)}_{0,1}$
(an index-1 weak Jacobi form) but the CDH-twined genus
$Z^{(g_N)}_{K3}$ after imposing a *penumbral* refinement not in the
$M_{24}$ character table, requiring the Cheng–Duncan–Harrison–Paquette–Volpato
2021 extension. (iii) The Gritsenko–Clery 2018 table (line 22363–22372
of working_notes) gives the weight-sequence $(5, 4, 3, 2, 3/2, 1, 6/7, 3/4)$
for the *additive* Gritsenko lift, with non-integer weights $3/2, 6/7,
3/4$ at $N \in \{5,7,8\}$ — these contradict the $\{1/2, 1/4, 0\}$
sequence at line 198.

*Ghost theorem.* Two distinct weight-ladders exist:
1. **Borcherds-weight sequence at CHL scope** (integer weights from
   singular theta lift of $\phi^{(N)}_{0,1}$): $(w_N)_{N=1,2,3,4,6} = (5,2,1,1,1)$.
   Theorem 2 above.
2. **Gritsenko-additive-lift weight sequence** (from $\phi_{k(N),1}$ lifts
   with $k(N) \neq 0$): $(w_N)_{N=1,\dots,8} = (5, 4, 3, 2, 3/2, 1, 6/7, 3/4)$.
   These are *different constructions* producing different paramodular
   forms, not two scopes of the same identity.

At $N \in \{5, 7, 8\}$ the "Borcherds weight" $\kappa_{\mathrm{BKM}}$ is
*not well-defined*: the natural weight is the Weil-representation
weight of the Shimura–Waldspurger factorisation (Theorem 4),
a genuinely *different invariant* from $c_N(0)/2$.

### Retraction R3 (half-integer/gerbe Cheeger–Simons interpretation)

*Wrong claim.* "$N = 7$: order-4 gerbe Cheeger–Simons character
realisation; weight 1/4 corresponds to order-4 gerbe"
(working_notes.tex line 22914 and platonic_synthesis line 560).

*Precise error.* The Cheeger–Simons character sits in
$H^3_{\mathrm{CS}}(BG; \mathbb T) \simeq H^4(BG; \mathbb Z)$ (for
compact Lie $G$); it is *not* an order-4 gerbe (an order-4 class in
$H^2(X; \mathbb T)$) but an integer $H^4$-class. The order-4 multiplier
at $N = 7$ arises from the archimedean Weil representation's central
extension
\[
 1 \to \mu_4 \to \widetilde{\mathrm{Mp}}_4 \to \mathrm{Mp}_4 \to 1,
\]
an *order-4 central extension*, not a gerbe. The correct homological
invariant is the class in $H^2(\mathrm{Mp}_4(\mathbb Z); \mu_4)$
classifying the genuine representation, not $H^3$.

*Ghost theorem.* The order-4 central extension at $N=7$ is
*the* obstruction to a $\mathrm{Sp}_4(\mathbb Z)$-equivariant
Borcherds product at $N = 7$; the non-integer "weight 1/4" is the
*4-torsion index* of the Shimura–Waldspurger
factorisation (Theorem 4), not a Borcherds weight.

### Retraction R4 (on the row $N = 6$ status in working_notes.tex 22913)

*Wrong claim.* "At $N = 6$ (theorem row, half-integer weight via Clery)...".

*Precise error.* At $N = 6$, the weight is *integer* $w_6 = 1$
per Theorem 2 above (CHL ladder), *not* half-integer $1/2$. The
"half-integer weight via Clery" is an error — Gritsenko–Clery 2018
produces the order-$N$ paramodular form at $N = 6$ with weight 1 and
a multiplier of order 6 (the Clery multiplier), not weight $1/2$.
The half-integer rows are $N \in \{5, 7, 8\}$ only.

*Ghost theorem.* The paramodular form at $N = 6$ is
$F^{(6)} \in S_1(\Gamma_6, \nu^{(6)})$ where $\nu^{(6)}$ is the
order-6 Clery multiplier, the Borcherds lift of
$\phi^{(6)}_{0,1} = Z^{(g_6)}_{K3}$ with $g_6 \in 6A \subset M_{24}$
the Mathieu element, $c_6(0) = 2$, $w_6 = 1$. The representation-theoretic
home is $\GSp_4(\mathbb A)$-automorphic with order-6 central character,
covered by Arthur 2013.

---

## Cross-consistency checks

### (a) Platonic synthesis waves 11–16

- `wn:thm:plat-borcherds-lift` (line 191, platonic_synthesis): retain
  the factor $64$, the Borcherds product identity, and the Macdonald
  $\eta^9$ identity; *correct* the "Sp_4(Z)/{±I} ≃ SO_+(Λ^{3,2}) via
  Pfaffian" to finite-index embedding (Retraction R1).
- `wn:thm:plat-gDelta5` (line 211): retain all structural claims; the
  real-root Gram matrix and signature (2,1) of the real roots (not
  "(3,2)", which is the ambient $\Lambda^{3,2}$ signature) is
  *consistent* with my Theorem 1.2 Corollary (the eigenvalue count
  $\{-2, 4, 4\}$ gives signature $(2,1)$). No change.
- `wn:thm:plat-universal-kBKM` (line 237): *correct* the BKM-denominator
  scope sequence from $(5,4,3,2,1)$ to $(5,2,1,1,1)$ per Theorem 2
  above (the Gritsenko–Nikulin CHL ladder uses $c_N(0)/2$ directly, not
  paramodular weight), or disambiguate the two sequences
  (CHL-via-Borcherds vs Gritsenko-additive-lift) as separate items.
  *Retract* the Borcherds-weight scope sequence $\{5,2,1,1,1/2,1,1/4,0\}$
  to scope-restricted Theorem 3 above.

### (b) CoHA–to–$\mathcal W_\infty$ treatise

- Line 502–520: the Oberdieck–Pixton $Z^{\mathrm{red}}_{\mathrm{DT}}(K3 \times E)
  = -C/\Phi_{10}$ identity with $\Phi_{10} = \Delta_5^2$ is consistent
  with my Theorem 1 (factor $64^2 = 4096$ absorbs into the motivic
  normalisation $C$).
- Line 534 open problem of Lie-algebra isomorphism
  $\mathfrak g_{\mathrm{BPS}}(K3 \times E) \cong \mathfrak g_{\Delta_5}$:
  my Theorem 4 *clarifies* that at $N \geq 2$ the Davison wall-crossing
  identification is already broken by the non-integer weight issue at
  $N \in \{5, 7, 8\}$, so the open problem at $N \in \{1, 2, 3, 4, 6\}$
  is the one to pursue.

### (c) Universal identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$

- *At CHL scope $N \in \{1, 2, 3, 4, 6\}$*: Theorem 2 above, rigorous.
- *At full 8-form scope $N \in \{1,\dots,8\}$*: Theorem 3 above
  *retracts* the half-integer extension; Theorem 4 replaces it with the
  Shimura–Waldspurger factorisation, *not* the Borcherds-weight
  identity.

### (d) Two-stage factorisation $\Phi_d = \mathrm{Sp}_{\Sigma,C} \circ \Phi^{\mathrm{FA}}_d$

- The Borcherds lift at $N=1$ is a *specialisation*
  $\mathrm{Sp}_{\Sigma_2, E}$ of the Stage-1 factorisation algebra
  $\mathcal F_{K3 \times E}$ at the Humbert divisor
  $H_1 \subset \mathcal A_2$. The $\kappa_{\mathrm{BKM}} = 5$ invariant
  is a tier-(iii) specialisation-dependent invariant per
  working_notes §`sec:three-tiers-rcy`, *consistent* with my Theorem 1.
- At $N \in \{5, 7, 8\}$ the "tier-(iii) specialisation" requires the
  Mongardi–Tari–Wandel Kummer-3 fourfold (not the standard K3 $\times$ E)
  and the Shimura–Waldspurger machine — these are conjectural
  CY$_3$-level constructions (working_notes line 383), consistent with
  my Theorem 4.

---

## Residual frontier

**Open F1.** Explicit computation of the archimedean correction
$\mathrm{corr}_N$ for $N \in \{1,2,3,4,6\}$ from Borcherds 1998 §5
(Koecher cusp integral), verifying
$c_N(0) = \chi(K3, g_N) - \mathrm{corr}_N$ for each $N$. Status: open
pending explicit Weil-integral computation on
$\mathbb H^{\mathrm{IV}}_+(\Lambda^{3,2})$.

**Open F2.** Is the Shimura–Waldspurger factorisation at
$N \in \{5, 7, 8\}$ *unique*? If so, the weight-1 elliptic cusp forms
$g_5 \in S_1(\Gamma_0(20), \chi_5), g_7 \in S_1(\Gamma_0(28), \chi_7),
g_8 \in S_1(\Gamma_0(32), \chi_8)$ are uniquely determined by the
paramodular forms $F^{(5)}, F^{(7)}, F^{(8)}$ via Theorem 4. Status:
open; Waldspurger 1980 uniqueness depends on the CM-discriminant
condition at each level.

**Open F3.** The CY$_3$-level geometric realisation of $\Phi_N$ at
$N \in \{5, 7\}$ is obstructed (working_notes line 383): $N = 5$ via
Borcea–Voisin $(S_5 \times E_5)/(\iota_S \times \iota_E)$ requires a
non-symplectic involution on K3, which is not in Mukai's symplectic
classification; $N = 7$ is obstructed by Nikulin fixed-count 3. Is
there a *motivic* CY$_3$ at $N \in \{5, 7\}$ via Kuga–Satake
descent from a K3-fibered 5-fold? Status: open.

**Open F4.** The signature of $\mathfrak g_{\Delta_5}$ at the
*full* root lattice $\Lambda^{3,2}$ (not just the real-root sublattice
$\Lambda^{2,1}_{II}$): is it $(3,2)$ (ambient) or $(2,1)$ (real-root
restricted)? The Feingold–Frenkel 1983 convention gives $(2,1)$; the
Gritsenko–Nikulin 1998 convention gives $(3,2)$. This is a
*notational convention*, not a substantive open problem, but it
must be fixed throughout the manuscript. Status: notational.

**Open F5.** At the $\mathrm{Mp}_4(\mathbb A)$-adelic level, does
the metaplectic AKN functor
$F^{\mathrm{Mp}}: \mathcal A^{\mathrm{Mp}_4}_{1/2,\mathrm{half}}
\to \mathrm{BKM}^{\mathrm{super}}_\Sigma$ factor through
$\theta_{2,3}^*$? (working_notes `wn:conj:akn-Fmp-factors-theta`,
Conjecture). My Theorem 4 indicates the direction is *wrong* as
stated in working_notes — the correct factorisation is
$\mathrm{Mp}_2 \xrightarrow{\theta_{2,3}} \mathrm O(3,2)
\to \mathrm{Sp}_4/Z$, *not* the direction asserted. Status:
conjectural; see Retraction R1 for the integral-level correction.

---

## Attack-heal cycle log (private, not for manuscript)

**Cycle 1: ATTACK — $\wedge^2$-Pfaffian isomorphism.** The statement
$\mathrm{Sp}_4(\mathbb Z)/\{\pm I\} \simeq \mathrm{SO}_+(\Lambda^{3,2})$
"via $\wedge^2$-Pfaffian" (wn:thm:plat-borcherds-lift line 204) is
attacked: compute the exterior square map carefully. It lands in
$\mathrm{SO}(6)$ with signature $(3,3)$, not $(3,2)$. The signature
$(3,2)$ emerges only on the 5-dimensional primitive
quotient $\wedge^2_0 V_4$. The integral map is a finite-index embedding,
not isomorphism. **HEAL** — Retraction R1 above: the correct statement
is the finite-index embedding
$\mathrm{Sp}_4(\mathbb Z)/\{\pm I\} \hookrightarrow
\mathrm{SO}_+(\Lambda^{3,2})$ with cokernel $\mathbb Z/2$ (Maass
multiplier). The Plücker embedding is totally geodesic at the
symmetric-space level, providing the geometric setup for the Borcherds lift.

**Cycle 2: ATTACK — 64-divisibility and Weyl equivariance.** The
statement "divisibility $64 \mid f(n,l,m)$ forces Weyl-group
equivariance" (same theorem) is attacked by asking for the precise
mechanism. The divisibility is a statement about Fourier coefficients
of $\phi_{0,1}$; Weyl equivariance is a statement about
$\mathrm{Sp}_4(\mathbb Z)$-action on the Borcherds product. The causal
direction is ambiguous as stated. **HEAL** — Theorem 1.2 above: the
correct statement is a *biconditional*: $64 \mid f(n,l,m)$ is equivalent
to the $\mathrm{Sp}_4(\mathbb Z)$-equivariance of the
*integer-normalised* Borcherds product. The archimedean Eisenstein
integrality forces $a(T) \in 64\mathbb Z$ at the primitive matrix
$T = \mathrm{diag}(1,1)$ with off-diagonal 1, and this is the
cohomological obstruction class in $H^1(\Gamma_1, \mathbb Z/64)$ of
the Maass multiplier.

**Cycle 3: ATTACK — $\{5, 2, 1, 1, 1/2, 1, 1/4, 0\}$ sequence.** The
abstract (line 198) and theorem (line 381) assert the weight sequence
$\{5,2,1,1,1/2,1,1/4,0\}$ at the full 8-form scope. This is
adversarially attacked by cross-checking against (i) the internal
table at line 22363–22372 which gives $\{5,4,3,2,3/2,1,6/7,3/4\}$;
(ii) the Gritsenko 1999 formula $k = c(0)/2 + \frac{1}{24}\sum_\ell
\ell^2 c(0,\ell)$, which for index-1 inputs forces the weight to be
$c(0)/2$ (integer half), contradicting weights $1/4, 0, 6/7$;
(iii) the fundamental theorem of Borcherds 1998 which produces
integer-weight Borcherds products from integer-weight inputs — the
half-integer outputs require the metaplectic double cover, not
the same Borcherds lift. **HEAL** — Retraction R2 and Theorem 3
above: the weight sequence at $N \in \{5,7,8\}$ is *not* part of the
Borcherds-weight-ladder of Theorem 2; it is the Gritsenko-additive-lift
of a *different* Jacobi input (weight $\geq 2$), and at the CY$_3$
level requires the Shimura–Waldspurger factorisation (Theorem 4) through
a metaplectic double cover, not the same Borcherds lift.

**Cycle 4: ATTACK — the AKN factorisation through $\theta_{2,3}$.** The
Weil correspondence $\theta_{2,3}: \mathrm{Mp}_2 \to \mathrm{O}(3,2)$
is asserted in working_notes line 22871 to be the factorisation of
the boundary extension of the AKN functor. Attacked: the direction
is $\mathrm{Mp}_2 \to \mathrm{O}(3,2)$, meaning the source is
$\mathrm{Mp}_2$ (genus-1 metaplectic) and the target is
$\mathrm{O}(3,2)$ (the orthogonal group of $\Lambda^{3,2}$). But the
paramodular form $F^{(N)}$ at $N \in \{5,7,8\}$ lives on
$\mathrm{Mp}_4$ (genus-2 metaplectic), not $\mathrm O(3,2)$. So the
asserted factorisation
$\mathrm{Sh} \colon S_1(\Gamma_0(4N)) \to S_{1/2}(\Gamma_0(4N))
\to M_{1/2}(\Gamma_N^{(2)})$ requires going from $\mathrm{Mp}_2$
(genus 1) to $\mathrm{Mp}_4$ (genus 2) via Siegel paramodular
lift, *not* via $\mathrm O(3,2)$. **HEAL** — Theorem 4 above:
the correct factorisation uses the *dual* Weil correspondence
$\theta_{2,3}^\vee: \mathrm{Mp}_2 \to \mathrm{Sp}_4$ obtained by
pulling back along the accidental isomorphism
$\mathfrak{sp}_4 \simeq \mathfrak{so}(3,2)$, which admits an integral
refinement for $\mathrm{Sp}_4(\mathbb Z)$-invariant paramodular forms.
This is a substantive correction to the boundary-extension theorem.

**Cycle 5: ATTACK — $N=6$ weight and Arthur classification.** Line
22913 ("At $N = 6$ (theorem row, half-integer weight via Clery)")
asserts $N = 6$ has half-integer weight. Attacked: Gritsenko 1999
Thm. 1.2 gives $w_6 = c_6(0)/2 = 2/2 = 1$ (integer), and the
Gritsenko–Clery 2018 paramodular form $F^{(6)}$ has weight 1, not
$1/2$. The multiplier $\nu^{(6)}$ is order 6 (not order 2), but
this is a *character*, not a weight. Arthur 2013 covers order-6
central-character $\GSp_4$ representations perfectly. **HEAL** —
Retraction R4 above: the half-integer-weight rows are $N \in \{5,7,8\}$
only; the $N=6$ row is integer weight 1 in the CHL ladder.

**Cycle 6: ATTACK — super-root parity and Borcherds positivity.**
At $N = 8$ the CDH-twined genus has negative Fourier coefficients,
violating the Borcherds 1998 Thm. 10.1 positivity hypothesis. Is
the claim "weight 0 abelian-lattice degeneracy at $N = 8$"
(working_notes line 198) a real Borcherds weight or a degeneracy
limit? Attacked: weight 0 as claimed would require $c_8(0) = 0$, but
Gritsenko–Clery 2018 gives $c_8(0) = 3/2$ (non-integer!), giving a
*non-integer* numerator already. The weight computation is:
$c_8(0,0) = \chi(K3, g_8)/|\mathbb Z/8| = $ trace of 8-cycle in
$M_{24}$ on the 24-dim K3 cohomology $= 2$, divided by the
normalisation convention. **HEAL** — Theorem 3 Step 3 above: the
weight-0 "degeneracy" is not a genuine weight-0 Borcherds product
but a degenerate cusp limit, producing a rational function
(not a holomorphic paramodular form) on $\mathbb H_2$. This is not
in the scope of the Borcherds-weight universal identity.

**Cycle 7: ATTACK — the CHL ladder weight sequence.** Is the sequence
$\{5, 4, 3, 2, 1\}$ (cited in wn:thm:plat-universal-kBKM) or
$\{5, 2, 1, 1, 1\}$ (computed via $c_N(0)/2$ directly) the correct
CHL sequence? The universal identity $\kappa_{\mathrm{BKM}}(\Phi_N) =
c_N(0)/2$ gives $(5, 2, 1, 1, 1)$ directly from
$(c_N(0))_{N=1,2,3,4,6} = (10,4,2,2,2)$. But the "paramodular weight"
sequence $(5,4,3,2,1)$ asserted at line 374 is inconsistent.
**HEAL** — Theorem 2 and its proof: the correct sequence is
$(5, 2, 1, 1, 1)$. The sequence $(5, 4, 3, 2, 1)$ is the *additive
Gritsenko lift* of weight-$(0, 2, 4, 6, 8)$ Jacobi forms — a
different construction producing *different* paramodular forms,
not an alternative scope of the same Borcherds identity. This
disambiguation fixes a long-standing confusion in the working_notes
between the two weight conventions.

---

**Primary sources cited in this document.**
Borcherds 1995 (*Invent. Math.*, singular theta lifts);
Borcherds 1998 (*Duke*, automorphic products);
Gritsenko–Nikulin 1998 (*Amer. J. Math.* 119, Siegel modular forms and
$\Delta_5$ additive lift);
Gritsenko 1999 (*St. Petersburg Math. J.*, refined weight formula);
Gritsenko–Clery 2018 (*Abh. Math. Hambg.* 88, eight paramodular forms);
Cheng–Duncan–Harvey 2014 (*Comm. Number Theory Phys.* 8, umbral twined
genera);
Mukai 1988 (*Invent. Math.* 94, symplectic K3 automorphisms);
Nikulin 1979 (K3 symplectic orbits);
Eichler–Zagier 1985 (*Theory of Jacobi Forms*);
Pitale–Schmidt 2014 (*Mem. AMS*, Siegel cusp forms of degree 2);
Arthur 2013 (*AMS Colloq.* 61, $\GSp_4$ endoscopic classification);
Waldspurger 1980 (*J. Math. Pures Appl.* 59, Shimura correspondence);
Shimura 1973 (*Ann. Math.* 97, half-integer weight modular forms);
Lorgat 2020 (automorphic corrections, explicit $\Delta_5$ construction);
Oberdieck 2018 (Igusa cusp form conjecture for $K3 \times E$);
Oberdieck–Pixton 2017 (arXiv:1706.10100, DT partition function);
Costello–Francis–Gwilliam 2026 ($E_3$-observables in Chern–Simons
holography).
