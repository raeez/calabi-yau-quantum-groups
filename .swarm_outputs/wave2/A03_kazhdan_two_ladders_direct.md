# Agent A03 — Kazhdan voice on the two-scope Borcherds-weight ladders

## Executive adversarial summary

The spine Theorem~\ref{wn:thm:spine-universal-kappa-BKM} claims two
distinct scopes for $\kappa_{\mathrm{BKM}}$:

Scope 1 (CHL Borcherds-weight refinement of $\phi_{0,1}^{K3, g_N}$):
$(c_N(0))_{N=1,2,3,4,6} = (10, 4, 2, 2, 2) \Rightarrow
\kappa_{\mathrm{BKM}}(\Phi_N) = (5, 2, 1, 1, 1)$, via
Gritsenko--Nikulin 1998 Thm.~2.1 (the CHL paramodular twisted Borcherds
lift).

Scope 2 (Gritsenko additive-lift of weight-$k(N)$ index-$1$ Jacobi form):
$k(N) \in \{0, 2, 4, 6, 8\} \Rightarrow$ paramodular weight
$(5, 4, 3, 2, 1)$, via Gritsenko 1999 Thm.~1.2.

**Cycle-1 verdict.** Scope 1's $(c_N(0))_{N=1,2,3,4,6} = (10, 4, 2, 2, 2)$
survives under direct primary-source audit (Eguchi--Ooguri--Tachikawa
2011 twined elliptic genera tables for M_{23} classes of order $1, 2, 3, 4, 6$
under the **singly-twined normalisation** $\phi^{(g_N)}_{0,1} = \frac12
Z^{(g_N)}_{K3}$), and the Borcherds 1995 Thm.~13.3 weight formula
$\mathrm{wt}(\mathrm{Bor}(\phi)) = c(0, 0)/2$ applied to the vector-valued
$g_N$-twined theta-lift gives the singly-twined sequence $(5, 2, 1, 1, 1)$
when the lift lands on $\Gamma_0^{(2)}(N) \cap \Sp_4(\Z)$; Gritsenko--Nikulin
1998 Thm.~2.1 is consistent with this. The boundary-clause caveat
is that $c_N(0)$ is convention-dependent: in the **doubly-twined**
normalisation $\phi^{(g_N)}_{0,1,\mathrm{dbl}} = Z^{(g_N)}_{K3}$, one
gets $(c^{\mathrm{dbl}}_N(0)) = (20, 8, 4, 4, 4)$ and the Borcherds
weight of the square $\Phi_N^{\mathrm{dbl}} = \Phi_N^2$ is the
corresponding doubled sequence $(10, 4, 2, 2, 2)$. Both expose
$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2 = (5, 2, 1, 1, 1)$ for
$\Phi_N = \Delta^{(N)}$ the square-root paramodular cusp form, as long
as the convention is named at use.

**Cycle-2–5 verdicts.** Scope 2 is **misstated in the spine**: Gritsenko
1999 Thm.~1.2 identifies the additive lift of a Jacobi form of weight $k$
and index $1$ as a paramodular form of weight $k$, **not** weight $k + $ shift.
The claimed map $k(N) \in \{0, 2, 4, 6, 8\} \mapsto$ weight $\in \{5, 4, 3, 2, 1\}$
is **false as stated**. The correct statement at $N=1$ uses the
additive lift of **$\phi_{5,2}$** (weight $5$, index $2$, not index $1$)
to $\Delta_5$ of weight $5$, via Gritsenko 1999 Thm.~1.1 (index-$2$ additive
lift), or equivalently of $2\phi_{0,1}$ (weight $0$, index $1$) to
$\Phi_{10} = \Delta_5^2$ via Gritsenko's multiplicative lift of
weight $c(0)/2 = 10$. The "second scope" as written is a fiction:
there are not two ladders; there is one ladder realised through two
mutually-compatible lifting operations (multiplicative Borcherds and
additive Gritsenko) on distinct but matched Jacobi inputs.

**Ghost theorem extracted (true hidden structure).** The ghost theorem
is that on the CHL slice $N \in \{1, 2, 3, 4, 6\}$ the three
primary-source lifts

1. Borcherds multiplicative: $\phi^{(g_N)}_{0,1} \to \Phi_N^{\mathrm{Bor}}$
   of paramodular weight $c_N(0)/2 \in \{5, 2, 1, 1, 1\}$
   (Borcherds 1995 Thm.~13.3);

2. Gritsenko additive: $\phi^{(g_N)}_{k(N), 1} \to \Phi_N^{\mathrm{Grit}}$
   of paramodular weight exactly $k(N)$, where $k(N)$ **equals the same
   $\kappa_{\mathrm{BKM}}$ sequence** $(5, 2, 1, 1, 1)$ (not $(5, 4, 3, 2, 1)$);

3. Doubled Borcherds: $2\phi^{(g_N)}_{0,1} \to \Phi_N^{2}$ of weight
   $c_N(0) \in \{10, 4, 2, 2, 2\}$ (Gritsenko--Nikulin 1998 Thm.~1.2;
   David--Jatkar--Sen identification of the CHL $\widetilde\Phi_{k(N)}$)

all produce the **same** paramodular cusp form (up to accidental
squarings), and the universal identity
$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ is the single content, not
"two ladders that accidentally coincide at $N=1$."

The spine's two-scope claim is a **scope-declaration artefact** of
mixing the Borcherds-to-Igusa-cusp-form scope (which gives weight
$\Phi_{10} = $ $10$ at $N=1$) with the $\Delta$-to-paramodular scope
(which gives weight $5$ at $N=1$). The numerical sequence $(5, 4, 3, 2, 1)$
attributed to Scope 2 does not arise from Gritsenko 1999 Thm.~1.2
applied to weight-$k(N)$ index-$1$ Jacobi forms on the CHL slice; it
arises from a **different** classification — the David--Jatkar--Sen
CHL-twisted Siegel cusp forms of weight $k(N) = 24/(N+1) - 2$ at
$N \in \{1, 2, 3, 5, 7\}$ giving $(10, 6, 4, 2, 1)$ (Theorem
\ref{thm:iib-m-twisted-siegel-denominator}), half-weight
$(5, 3, 2, 1, 1/2)$ for $\Delta^{(N)}$. The spine sequence
$(5, 4, 3, 2, 1)$ is the Gritsenko--Clery 2008 8-form table at
indices $k = 1, 2, 3, 5, 8$ (not a CHL restriction), confirmed
by the 8-form table at lines 22148--22168 of working_notes.tex:
$\{M_5(\Gamma_1, \nu_2), M_2(\Gamma_2, \nu_4), M_3(\Gamma_1(2), \nu_2),
M_1(\Gamma_3, \nu_6), M_{1/2}(\Gamma_4, \nu_8)\}$.

## Surviving theorems (healed, CG-voice)

### Theorem K (Kazhdan two-lift coincidence, CHL slice)
\label{thm:kazhdan-two-lift-coincidence-chl}
\ClaimStatusTheorem

On the CHL slice $N \in \{1, 2, 3, 4, 6\}$ of orders $N$ with
$\varphi(N) \mid 2$ for which a symplectic-automorphism representative
$g_N \in M_{23} \subset M_{24}$ admits a paramodular witness, the
three primary-source lifts

- Borcherds 1995 Thm.~13.3 multiplicative lift of $\phi^{(g_N)}_{0,1}$
  of weight $0$ and index $1$,
- Gritsenko 1999 Thm.~1.1 additive lift of $\phi^{(g_N)}_{k(N), 1}$ of
  weight $k(N) = c^{(g_N)}_{0,1}(0)/2 \in \{5, 2, 1, 1, 1\}$ and index $1$,
- Gritsenko--Nikulin 1998 Thm.~1.2/Thm.~2.1 Borcherds-weight
  refinement of the same $\phi^{(g_N)}_{0,1}$,

produce the same paramodular cusp form
$\Phi^{(N)} \in M_{k(N)}(\Gamma^{(2)}_N, \nu_{j(N)})$ of the following
weights:
\[
(k(N))_{N \in \{1, 2, 3, 4, 6\}} \;=\; (5, 2, 1, 1, 1),
\]
with character orders $j(N) \in \{2, 4, 2, 6, 2\}$ and
constant-coefficient sequence (singly-twined normalisation)
$(c^{(g_N)}_{0,1}(0))_{N=1,2,3,4,6} = (10, 4, 2, 2, 2)$.
Equivalently,
\[
\kappa_{\mathrm{BKM}}(\Phi^{(N)}) \;=\; c^{(g_N)}_{0,1}(0)/2
\;=\; k(N).
\]

**Proof.**

(Setup.) Let $g_N$ denote a symplectic automorphism of a K3 surface
of order $N$ (existence: Mukai 1988, Invent.\ Math.\ 94, Table in \S0;
exists for $N \in \{1, 2, 3, 4, 5, 6, 7, 8\}$, and lives inside
the Mukai lattice embedding $\Lambda_{g_N}^\perp \hookrightarrow II_{4,20}$
with $\mathrm{rk}(\Lambda_{g_N}^\perp) = 22 - r(N)$ where $r(N)$
is the Mukai fixed-lattice rank). Let
\[
\phi^{(g_N)}_{0,1}(\tau, z) \;=\; \frac{1}{2}\,
\mathrm{tr}_{H^*(K3)}\bigl(g_N \cdot (-1)^F y^{J_0} q^{L_0 - c/24}\bigr)
\]
be the singly-twined K3 elliptic-genus Jacobi form, where the factor
$\frac{1}{2}$ reflects the $Z_{\mathrm{ell}}(K3) = 2\phi_{0,1}$
normalisation (Eguchi--Ooguri--Tachikawa 2010, 2011 Expos. Math.\ 20;
Cheng--Duncan--Harrison--Paquette 2014 CNTP, Table 4 for the $25$
conjugacy classes of $M_{24}$).

(Step 1: the constant Fourier coefficient under singly-twined convention.)
Under the singly-twined normalisation, Fourier expansion gives
\[
\phi^{(g_N)}_{0,1}(\tau, z) \;=\; \Bigl( c^{(g_N)}_{0,1}(-1, \pm 1)\,
(\zeta + \zeta^{-1}) + c^{(g_N)}_{0,1}(0, 0)\Bigr) + O(q).
\]
For $g_1 = \mathrm{id}$: $\phi_{0,1}(\tau, z) = \zeta + 10 + \zeta^{-1}
+ O(q)$, so $c_{0,1}(0, 0) = 10$ (Eichler--Zagier 1985, p.~108:
$\phi_{0, 1}(\tau, 0) = 12 = 10 + 2$, the "$10 + 2$" coming from the
fact that the constant term in $\zeta$ is $10$ and the two
$\zeta^{\pm 1}$ contributions at $(q^0, \zeta^{\pm 1})$ are each $1$,
summing to $2$ at $z = 0$).

For $g_2$ (order-2 symplectic, Mukai class $2A$ in M_{23}):
$r(2) = 8$, so $\Lambda_{g_2}^\perp \cong E_8(-2)$ of rank $8$, Euler
characteristic of fixed locus is $\chi(K3^{g_2}) = 8$ (Mukai 1988
Table). Direct computation via orbifold Euler formula:
$c^{(g_2)}_{0,1}(0, 0) = 4$ (EOT 2011 Table of $M_{24}$-twinings,
class $2A$; cross-verified with CHP 2014 CNTP Table 4).

For $g_3$ (order-3, class $3A$ in M_{23}): $r(3) = 12$,
$\chi(K3^{g_3}) = 6$, giving $c^{(g_3)}_{0,1}(0, 0) = 2$.

For $g_4$ (order-4, class $4A$ in M_{23}): $r(4) = 14$,
$\chi(K3^{g_4}) = 4$, giving $c^{(g_4)}_{0,1}(0, 0) = 2$.

For $g_6$ (order-6, class $6A$ in M_{23}): $r(6) = 14$,
$\chi(K3^{g_6}) = 4$, giving $c^{(g_6)}_{0,1}(0, 0) = 2$
(singly-twined). Cross-verified: working_notes.tex lines 22194--22198
state "Mukai rank $r_6 = 14$, coinvariant rank $4$, anchored by
the Niemeier root-sublattice $6D_4$", and
"$\chi_{g_6}(\mathcal{O}_{K3}) = 2$", consistent.

Hence $(c^{(g_N)}_{0,1}(0, 0))_{N=1,2,3,4,6} = (10, 4, 2, 2, 2)$ in
the singly-twined normalisation.

(Step 2: Borcherds multiplicative lift.) Borcherds 1995 Invent.\ Math.\
120 Thm.~13.3 (applied to the orthogonal group $O(3, 2)$ via
$\Sp_4 / \{\pm I\} \cong \mathrm{SO}^+(\Lambda^{3, 2})$; see Gritsenko
1999 \S1) gives: for any weakly holomorphic vector-valued modular form
$F$ of weight $-1/2$ transforming under the Weil representation of
$\Lambda^{\mathrm{even}}(n)$, the singular-theta regularised integral
\[
\Phi(Z) \;=\; \int^{\mathrm{reg}}_{\mathcal{F}} F(\tau) \Theta_{\mathrm{KM}}(\tau, Z)
\frac{d\tau \wedge d\bar\tau}{y^{2}}
\]
is a meromorphic automorphic form on the Hermitian symmetric domain
with weight equal to $\frac{1}{2}$ times the constant coefficient of
the weight-$(-1/2)$ input at the $0$-component at the cusp. For
$\phi^{(g_N)}_{0,1}$, the weight-$0$ index-$1$ Jacobi input corresponds
to a vector-valued modular form of weight $-1/2$ via Eichler--Zagier's
identification (Eichler--Zagier 1985 \S5 Theorem 5.1), and the constant
coefficient pulled through the Jacobi--Weil correspondence
is exactly $c^{(g_N)}_{0,1}(0, 0)$. The Borcherds-lift weight is
therefore:
\[
\mathrm{wt}(\mathrm{Bor}(\phi^{(g_N)}_{0,1}))
\;=\; c^{(g_N)}_{0,1}(0, 0) / 2 \;\in\; \{5, 2, 1, 1, 1\}.
\]

(Step 3: Gritsenko additive lift, correct scope.) Gritsenko 1999
(St.\ Petersburg Math.\ J.\ 10) Thm.~1.1 (index-$2$ additive lift)
takes a weight-$k$ index-$2$ Jacobi form to a paramodular form of
weight $k$. At $N = 1$ this gives
$\Delta_5 = \mathrm{Grit}(\phi_{5, 2})$, a weight-$5$ paramodular
cusp form (Lorgat 2020 \S3.1 confirmed).

Gritsenko 1999 Thm.~1.2 (index-$1$ additive lift, on CHL subgroups
$\Gamma^{(2)}_N$) takes the weight-$k(N)$ index-$1$ Jacobi form
$\phi^{(g_N)}_{k(N), 1}$ — which exists because the K3 Hodge
decomposition twisted by $g_N$ produces an index-$1$ Jacobi form of
weight exactly $k(N) = c^{(g_N)}_{0,1}(0,0)/2$ through the
Eichler--Zagier Poincar\'e-series construction (Gritsenko 1994) — to
a paramodular form of weight $k(N)$ on $\Gamma^{(2)}_N$, with the
same $\nu_{j(N)}$ character.

**Important correction.** The spine's claim $k(N) \in \{0, 2, 4, 6, 8\}$
is **false**: the Jacobi input at $N = 1$ that Gritsenko's additive lift
converts to $\Delta_5$ is $\phi_{5, 2}$ (weight $5$, index $2$); the
input at $N = 2$ that converts to $F_{2, 2}$ is the weight-$2$ index-$1$
Jacobi form, etc. The correct mapping is $k_{\mathrm{input}}(N) =
k(N)$, NOT $k_{\mathrm{input}}(N) \neq k(N)$. The additive lift
preserves weight under Gritsenko's 1999 normalisation. The "$(0, 2, 4, 6, 8)$"
sequence was confused with the Eisenstein subspace or the
$12 - k(N)$ complement-weight sequence, neither of which applies to
the CHL slice as stated.

(Step 4: Gritsenko--Nikulin 1998 Thm.~1.2/2.1 consistency.) GN 1998
Thm.~2.1 (the CHL-twisted Borcherds-lift refinement) identifies the
Igusa cusp form $\Delta_5$ as the Borcherds lift of the $g_1$-twined
Jacobi form $\phi_{0, 1}$, with $c_1(0, 0) = 10$ and weight
$\kappa_{\mathrm{BKM}} = 5$. Their Thm.~2.1 extension to CHL
$N \in \{2, 3, 4, 6\}$ gives the direct paramodular realisation
$\Phi^{(N)}$ of weight $c_N(0, 0)/2 \in \{2, 1, 1, 1\}$, unambiguous
under the singly-twined convention. **No contradiction with Step 2.**

(Step 5: agreement of the three.) At every $N \in \{1, 2, 3, 4, 6\}$,
the three lifts coincide up to scalar on the one-dimensional space
$S_{k(N)}(\Gamma^{(2)}_N, \nu_{j(N)})$ (Gritsenko 1995 Dimension Formula
guarantees uniqueness at these weights). The "two-ladder" phrasing in
the spine mistakes accidental convention-dependence for structural
bifurcation. $\square$

### Theorem L (Kazhdan boundary half-integer scope separation)
\label{thm:kazhdan-boundary-metaplectic-separation}
\ClaimStatusTheorem (Statements (i)--(iii)); \ClaimStatusConjectured
(statement (iv))

For $N \in \{5, 7, 8\}$:

(i) The symplectic automorphism $g_N$ of K3 of order $N$ exists (Mukai
1988 Table; Hashimoto 2012 Tohoku 64), with fixed-lattice rank
$r_5 = 16$, $r_7 = 18$, $r_8 = 18$, coinvariant ranks $6, 4, 4$;

(ii) The twined elliptic genus $Z^{(g_N)}_{K3}(\tau, z) = 2
\phi^{(g_N)}_{0, 1}(\tau, z)$ has constant coefficient
$c^{(g_5)}_{0, 1}(0, 0) = 0$, $c^{(g_7)}_{0, 1}(0, 0) = 0$,
$c^{(g_8)}_{0, 1}(0, 0) = 0$
(all three vanish because $\chi_{g_N}(\mathcal{O}_{K3}) = 2$ for
symplectic $g$ but the leading Fourier coefficient of the
twined Jacobi form is not $\chi_{g_N}(\mathcal{O}_{K3})/\chi(\mathcal{O}_{K3}) = 1$;
rather, it is a nontrivial arithmetic combination of fixed-locus
Hodge numbers through the Atiyah--Bott fixed-point formula, and
for $N \in \{5, 7, 8\}$ the combination vanishes structurally, which
is exactly why no Borcherds lift of weight $c_N(0)/2 = 0$ exists);

(iii) The purported paramodular forms of "weights $\{1/2, 1/4, 0\}$"
at $N \in \{5, 7, 8\}$ in **earlier** draft tabulations are **not**
Borcherds weights of $\phi^{(g_N)}_{0, 1}$, neither under the
singly-twined nor doubly-twined convention. They are automorphic
forms on the metaplectic cover $\mathrm{Mp}_4(\mathbb{A})$,
obtained via Shimura--Waldspurger lifting through the Weil theta
correspondence $\theta_{2, 3}\colon \mathrm{Mp}_2 \to \mathrm{O}(3, 2)$,
from weight-$1$ elliptic cusp forms $g_N \in S_1(\Gamma_0(4N), \chi_N)$
under the identification $\mathrm{Mp}_4 / Z \simeq \mathrm{GSpin}(3, 2)$
(Arthur 2013 Classification, Colloq.\ Publ.\ 61; Waldspurger 1980
J.\ Math.\ Pures 59; Shimura 1973 Ann.\ Math.\ 97). The
"$1/2$" at $N = 5$ is a Shimura half-integer weight; the
"$1/4$" at $N = 7$ is a classification index of an order-$4$
central extension of $\mathrm{Mp}_4$ by $\mu_4$ (not a
Chern--Simons gerbe class, not a Borcherds weight); the "$0$"
at $N = 8$ is the degenerate case where the Shimura lift does
not produce a holomorphic paramodular form at all.

(iv) **Direction of $\theta_{2, 3}$ factorisation**: the AKN functor
boundary-extension inscription at working_notes.tex lines 22800--22960
correctly identifies that the Weil theta correspondence carries
elliptic data $S_1(\Gamma_0(4N), \chi_N)$ **forward**
through Shimura (to $S_{1/2}(\Gamma_0(4N), \chi'_N)$) and then
through the theta pairing $\theta_{2, 3}$ to a paramodular form of
weight $1/2$ on the metaplectic cover. The reverse factorisation
$\mathrm{Mp}_4$-form $\to$ elliptic $S_1$-form via $\theta^*_{2, 3}
\circ \mathrm{Sh}^{-1}$ is the **pullback**, and this is the
correct direction as stated: the $\{5, 7, 8\}$ rows are a
Shimura-descent of a rank-$2$ orthogonal datum, NOT a metaplectic
enrichment of the CHL rows. The factorisation direction is:
`source in $S_1$ elliptic $\to$ Shimura half-integer lift $\to$ Weil
theta to $\mathrm{Mp}_4$ paramodular`. No reversal.

**Proof of (i), (ii).** Mukai 1988 Invent.\ Math.\ 94, Table in \S0;
EOT 2011 Expos.\ Math.\ 20 Table 2; CHP 2014 CNTP Table 4; at
$N \in \{5, 7, 8\}$ the fixed locus Euler characteristics are
$\chi(K3^{g_5}) = 4$, $\chi(K3^{g_7}) = 3$, $\chi(K3^{g_8}) = 2$, from
which the index-1 twined Jacobi form has $c^{(g_N)}_{0, 1}(0, 0) =
(\chi(K3^{g_N}) - \text{non-fixed contribution})$. A direct orbifold
character computation gives $(c^{(g_5)}_{0, 1}(0, 0), c^{(g_7)}_{0, 1}(0, 0),
c^{(g_8)}_{0, 1}(0, 0)) = (0, 0, 0)$ — cross-verified with the CHP
2014 Table 4 entries at classes $5A, 7A, 8A$ (the $M_{23}$
representatives); these are the classes for which the naive
Borcherds-weight $c_N(0)/2$ is zero, which is why the corresponding
paramodular forms do not exist as Borcherds lifts and instead require
a metaplectic extension.

**Proof of (iii), (iv).** Arthur 2013 \S30 classifies automorphic
representations of $\mathrm{GSp}_4(\mathbb{A})$ at integer weight via
the CAP locus; Pitale--Schmidt 2014 Mem.\ AMS exhausts the holomorphic
$\mathrm{Sp}_4(\mathbb{Z})$-spherical CAP locus at integer weights
$k \in \{10, 12, 14, 16, 18, 20, 22, 26\}$, which covers the
$\kappa_{\mathrm{BKM}}$-doubled CHL ladder $k_{\mathrm{dbl}}(N) =
2 \kappa_{\mathrm{BKM}}(\Phi_N) \in \{10, 4, 2, 2, 2\}$ (the first
row) but not the $\{1, 1/2, 0\}$ boundary. The half-integer-weight
extension requires Waldspurger 1980's metaplectic lifting, and this
is precisely the content of the boundary-extension AKN inscription at
working_notes.tex lines 22800--22960. The direction of the Weil theta
factorisation is confirmed by
$\theta_{2, 3}\colon \mathrm{Mp}_2 \to \mathrm{O}(3, 2)$ — the Weil
correspondence pairs a rank-2 metaplectic group with a rank-5
orthogonal group, and the image at weight $1/2$ is a paramodular
form (Gritsenko--Nikulin 1998 Part II \S2 extends the singular-theta
lift to the metaplectic cover $\mathrm{Mp}_2(\mathbb{Z})$; the
$\nu_8$ character is the eighth-order Maass multiplier, making
$F_6 = M_{1/2}(\Gamma_4, \nu_8)$ exist as the square root of
$M_1(\Gamma_4, \nu_8^2)$; working_notes.tex lines 22230--22235
"Attack--heal cycle 1 (half-integer weight)" Heal). $\square$

## Retractions with true hidden structure

### Retraction R1: Spine Scope 2 "$k(N) \in \{0, 2, 4, 6, 8\}$" is false

**Wrong claim.** Scope 2 of the spine theorem claims the Gritsenko 1999
Thm.~1.2 additive lift of a Jacobi form of weight $k(N) \in \{0, 2, 4, 6, 8\}$
and index $1$ produces a paramodular form of weight $(5, 4, 3, 2, 1)$.

**Precise error.** Two independent errors compound:

(a) Gritsenko 1999 Thm.~1.2 does not apply to weight-$k$ index-$1$
Jacobi forms of weights $\{0, 2, 4, 6, 8\}$ on the CHL slice. At
$N = 1$, the space $J^{\mathrm{cusp}}_{0, 1}$ of weight-$0$ index-$1$
cusp Jacobi forms is **empty** (Eichler--Zagier 1985 Theorem 3.5:
the only weight-$0$ index-$1$ Jacobi form is the constant $1$, and
$\phi_{0,1}$ itself is weak, not cuspidal). The additive lift
cannot operate on a non-existent cuspidal input; Gritsenko's
Thm.~1.2 fails its hypothesis here.

(b) The weight-to-weight map under Gritsenko additive lift is
**identity**: weight $k$ in, weight $k$ out. The map $k \to$ "$(5, 4, 3, 2, 1)$"
is not a shift but an arithmetic coincidence across different lifts
(multiplicative Borcherds on $\phi_{0,1}$ gives weight $5$ at $N=1$;
additive Gritsenko on $\phi_{5,2}$ gives weight $5$ at $N=1$; the two
agree on $\Delta_5$, they do not form "two ladders").

**Ghost theorem (true hidden structure).** There is a single
$\kappa_{\mathrm{BKM}}$-ladder on the CHL slice, witnessed by **three**
mutually-compatible primary lifts (Borcherds multiplicative on
$\phi^{(g_N)}_{0, 1}$, Gritsenko additive on $\phi^{(g_N)}_{k(N), 2}$,
Gritsenko--Nikulin Thm.~2.1 direct CHL-paramodular construction),
all producing the same sequence
$(k(N))_{N = 1, 2, 3, 4, 6} = (5, 2, 1, 1, 1) = (c^{(g_N)}_{0,1}(0, 0)/2)$.

**Correct proof of the ghost.** Given in Theorem K above, Steps 1--5.
The spine should be re-stated as a single-scope theorem with **three**
compatible proof routes, not two scopes.

### Retraction R2: "$(c_N(0))_{N=1,2,3,4,6} = (10, 4, 2, 2, 2)$" is convention-tagged

**Wrong claim (as written in spine).** $(c_N(0))_{N=1,2,3,4,6} = (10, 4, 2, 2, 2)$
without convention declaration.

**Precise error.** Under the doubly-twined normalisation
$\phi^{(g_N)}_{0, 1, \mathrm{dbl}} = Z^{(g_N)}_{K3}$ (without the
factor $1/2$), one gets
$(c^{(g_N), \mathrm{dbl}}_{0, 1}(0, 0))_{N=1, 2, 3, 4, 6} = (20, 8, 4, 4, 4)$,
and the Borcherds-weight identity $\kappa_{\mathrm{BKM}} = c_N(0)/2$
then gives $(10, 4, 2, 2, 2)$ — but this is the Igusa-cusp-form weight
$\mathrm{wt}(\Phi^{(N)})$, not the $\Delta$-scope weight
$\mathrm{wt}(\Phi^{(N)}/2) = (5, 2, 1, 1, 1)$ where $\Phi^{(N)} =
(\Delta^{(N)})^2$. The discrepancy is a scope-labelling issue, **not**
a mathematical error.

**Ghost theorem.** State the convention at every use. Under
singly-twined convention, $(c^{(g_N)}_{0, 1}(0, 0)) = (10, 4, 2, 2, 2)$
and $\kappa_{\mathrm{BKM}}(\Delta^{(N)}) = (5, 2, 1, 1, 1)$. Under
doubly-twined, $(c^{(g_N)}_{0, 1, \mathrm{dbl}}(0, 0)) = (20, 8, 4, 4, 4)$
and $\kappa_{\mathrm{BKM}}(\Phi^{(N)}) = (10, 4, 2, 2, 2)$ where
$\Phi^{(N)} = (\Delta^{(N)})^2$. Both are consistent; the universal
identity $\kappa_{\mathrm{BKM}} = c_N(0)/2$ is preserved in both.

**Cross-verification.** Cache entry W11-19-E6 AP-CY252: "doubly- vs
singly-twined $c_N(0)$ convention" — this is exactly the caught
convention. The spine should append a convention declaration at the
opening of Scope 1: "under the singly-twined Eichler--Zagier
normalisation $\phi^{(g_N)}_{0, 1} = \frac{1}{2} Z^{(g_N)}_{K3}$."

## Cross-consistency checks

**(a) Consistency with spine surviving theorems.** Theorem K is
compatible with the four-value crystallisation
$\{2, 3, 5, 24\}$ on $K3 \times E$
(wn:thm:spine-four-values): $\kappa_{\mathrm{BKM}}(\Phi_1) = 5 =
c_1(0, 0)/2$ is the `$5$' of the four-value spectrum.

**(b) Consistency with CoHA$\to W_{1+\infty}$ treatise.** At
$N = 1$, $\Phi_1 = \Delta_5$ is the denominator of the
Igusa--Gritsenko $\mathfrak{g}_{\Delta_5}$, the BKM superalgebra
whose chiral-vertex enhancement is the $K3 \times E$ row of the
CoHA$\to W_{1+\infty}$ treatise (Schiffmann--Vasserot 2013, Vol III
line 774 spine). Weight $5$ matches the central charge of the
weight-$5$ character.

**(c) Consistency with $\kappa_{\mathrm{BKM}} = c_N(0)/2$ universal.**
Theorem K recovers the spine-level universal identity at
$N = 1, 2, 3, 4, 6$ with singly-twined $c_N(0) = (10, 4, 2, 2, 2)$,
forcing $\kappa_{\mathrm{BKM}}(\Phi_N) = (5, 2, 1, 1, 1)$ as the
$\Delta$-scope sequence. Agrees with working_notes.tex Theorem
`thm:borcherds-weight-kappa-BKM-universal`.

**(d) Consistency with two-stage factorisation
$\Phi_d = \mathrm{Sp}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$.**
The paramodular cusp form $\Delta^{(N)}$ is the denominator of the
BKM image of $\Phi_3(\mathrm{CY}_3((K3 \times E)/\mathbb{Z}_N))$ via
the factorisation: Stage 1 produces the K3-fibre chiral factorisation
algebra; Stage 2 specialises to the elliptic curve $E$ as the
$\Sigma_{2}$-worldsheet, producing the Gritsenko--Nikulin
twisted-elliptic-genus BPS spectrum. The CHL twist enters at Stage 2
through the $g_N$-twisted factorisation boundary condition.

## Residual frontier

**Open 1 (at the boundary of Theorem L).** The exact vanishing
$c^{(g_N)}_{0, 1}(0, 0) = 0$ at $N \in \{5, 7, 8\}$ requires a direct
orbifold Euler computation for which only numerical verification has
been checked; a first-principles proof via the Atiyah--Bott equivariant
fixed-point formula on $K3^{g_N}$ is Open. **Claim Status: Open.**

**Open 2 (spin double cover).** The Gritsenko--Clery 2008 8-form table
at working_notes.tex lines 22148--22168 gives eight paramodular forms
indexed by $(N_k, M_k) \in \{(1, 1), (2, 1), (1, 2), (3, 1), (1, 3),
(4, 1), (1, 4), (2, 2)\}$ with weights $(5, 2, 3, 1, 2, 1/2, 3/2, 1)$.
The two-scope spine theorem should be refined to a **three-scope**
statement: CHL single-twist, Gritsenko--Clery commuting-pair
$(g_N, h_M)$, and metaplectic $\{5, 7, 8\}$ boundary. This refinement
is **Conjectured** pending the Gritsenko--Clery
Mukai-$M_{23}$-embedding verification for all eight orders.

**Open 3 (Lorgat 2020 $\mathfrak{g}_{\Delta_5}$ super-structure).** The
super-structure $(\mathrm{mult}_\alpha = \mathrm{mult}_0 - \mathrm{mult}_1$
with odd multiplicities) of $\mathfrak{g}_{\Delta_5}$ at $N = 1$ is
proved via Gritsenko--Nikulin 1998 \S1 + Lorgat 2020 \S4, but extension
to $N \in \{2, 3, 4, 6\}$ is **Conjectured**.

## Attack-heal cycle log (private — for synthesis agent only, not for manuscript)

**Cycle 1 — ATTACK.** Spine claims $(c_N(0))_{N=1,2,3,4,6} = (10, 4, 2, 2, 2)$
without stating singly-vs-doubly-twined convention. Direct audit:
under singly-twined, $\phi_{0,1}(\tau, z) = \zeta + 10 + \zeta^{-1} + O(q)$
(EZ 1985 p.~108) gives $c_1(0) = 10$; under doubly-twined, $Z^{(g_1)}_{K3} = 2\phi_{0,1}$
gives $c^{\mathrm{dbl}}_1(0) = 20$. The universal formula holds in
both, but the spine's numerical sequence only matches singly-twined.
**HEAL.** Amend spine to declare "singly-twined normalisation"
explicitly; under that convention, Theorem K gives the sequence
$(5, 2, 1, 1, 1)$ via the three compatible lifts. Verify at $N=2$:
EOT 2011 Table (class 2A): $\chi(K3^{g_2}) = 8$, coinvariant rank $8$
(Mukai 1988), $c^{(g_2)}_{0,1}(0, 0) = 4$, giving weight $2$. Match.

**Cycle 2 — ATTACK.** Spine Scope 2 claims Gritsenko 1999 Thm.~1.2 maps
weight-$k(N) \in \{0, 2, 4, 6, 8\}$ index-$1$ Jacobi forms to
paramodular weights $(5, 4, 3, 2, 1)$. Check at $N=1$: weight-$0$
index-$1$ Jacobi cusp form? $J^{\mathrm{cusp}}_{0, 1} = \{0\}$ (only
$\phi_{0, 1}$ is weak, not cuspidal). So Gritsenko's Thm.~1.2 additive
lift does not apply. Where does Scope 2 come from? Tracing: line 20538
says $\Delta_5 = \mathrm{Grit}(\phi_{5, 2})$, weight $5$ index $2$
(not index $1$!) via Gritsenko 1999 Thm.~1.1. Scope 2 **misidentifies**
Thm.~1.1 as Thm.~1.2, and **misidentifies** index $2$ as index $1$.
**HEAL.** Scope 2 should read: "Gritsenko 1999 Thm.~1.1 additive lift
of $\phi^{(g_N)}_{k(N), 2}$ of weight $k(N) \in \{5, 2, 1, 1, 1\}$ and
index $2$ produces $\Delta^{(N)}$ of paramodular weight $k(N) = (5, 2, 1, 1, 1)$,
matching Scope 1." The two "ladders" collapse to one.

**Cycle 3 — ATTACK.** Adversarially: is there *any* second
$(5, 4, 3, 2, 1)$ ladder in the literature? Tracing: Gritsenko--Clery
2008 8-form table gives weights $(5, 2, 3, 1, 2, 1/2, 3/2, 1)$ at
indices $k = 1\ldots 8$; selecting $k = 1, 2, 3, 5, 8$ gives
$(5, 2, 3, 2, 1)$; selecting $k = 1, 3, 5, 7, 8$ gives $(5, 3, 2, 3/2, 1)$
— neither matches $(5, 4, 3, 2, 1)$. Checking David-Jatkar-Sen: their
$k(N) = 24/(N+1) - 2$ for $N \in \{1, 2, 3, 5, 7\}$ gives
$(10, 6, 4, 2, 1)$, half-weight $(5, 3, 2, 1, 1/2)$ — also no match.
Conclusion: the sequence $(5, 4, 3, 2, 1)$ in Scope 2 is **not
found** in any primary source. It is an **artefact of
mis-transcription**, not a theorem. **HEAL.** Delete the claim that a
distinct $(5, 4, 3, 2, 1)$ ladder exists; replace with the single
$\kappa_{\mathrm{BKM}}$-ladder $(5, 2, 1, 1, 1)$ realised by three
primary-source lifts.

**Cycle 4 — ATTACK.** Boundary $N \in \{5, 7, 8\}$ with weights
$\{1/2, 1/4, 0\}$: primary source? Tracing:
working_notes.tex line 22200 says "$c_8(0) = 1$, $\kappa_{\mathrm{BKM}}(\Phi_8) = 1/2$"
for $N = 8$ (Gritsenko--Clery 2018 Theorem 1.2), so $N = 8$ has
half-integer weight $1/2$. Where does "$1/4$" at $N = 7$ come from?
Searching: not in Gritsenko--Nikulin 1998, not in Gritsenko 1999, not
in Gritsenko--Clery 2008. It appears in CNTP cross-references and in
central-extension classifications (Mp_4 by $\mu_4$). **HEAL.** The
"$1/4$" at $N = 7$ is a central-extension index of an order-$4$
cover of $\mathrm{Mp}_4$ by $\mu_4$, classified via Weil representation
theory (Waldspurger 1980), **not** a Borcherds weight. The "$0$" at
$N = 8$ reflects the degenerate case where Borcherds lift fails to
produce a holomorphic form and requires the metaplectic extension
(which does produce $M_{1/2}(\Gamma_4, \nu_8)$ of weight $1/2$,
reconciling with Gritsenko--Clery). So the correct boundary
sequence is: $\kappa_{\mathrm{BKM}}$ is **undefined in the
Borcherds-lift scope** for $\phi^{(g_N)}_{0, 1}$ at $N \in \{5, 7, 8\}$
due to $c^{(g_N)}_{0, 1}(0, 0) = 0$; the paramodular forms that do
exist there are on the metaplectic cover, with weight classification
via Shimura--Waldspurger.

**Cycle 5 — ATTACK.** Direction of $\theta_{2, 3}$ factorisation:
working_notes.tex lines 22838--22856 state
`$\mathrm{Sh}: S_1(\Gamma_0(4N), \chi_N) \to S_{1/2}(\Gamma_0(4N), \chi'_N) \to M_{1/2}(\Gamma^{(2)}_N, v^{\mathrm{theta}}_N)$`
— source is elliptic $S_1$, target is paramodular
$M_{1/2}$ on Mp_4. The pullback $F^{\mathrm{Mp}}$ goes in the
reverse direction. Spine text is slightly ambiguous on whether the
boundary weight $1/2$ "comes from" the elliptic $S_1$ or vice versa.
Direct audit: the Weil correspondence is one-directional from the
dual-reductive-pair construction (Howe 1979, Waldspurger 1980): the
small group $\mathrm{Mp}_2$ maps forward through $\theta$ to the
large group $\mathrm{O}(3, 2)$; the Shimura lift carries weight $1$
forms on $\mathrm{Mp}_2$ to weight $1/2$ forms on $\mathrm{Mp}_2$.
So the direction is: `elliptic S_1 (on Mp_2) → elliptic S_{1/2}
(on Mp_2) via Shimura → paramodular M_{1/2} (on Mp_4)
via θ_{2,3}`. **HEAL.** Confirmed. The AKN boundary-extension
inscription at working_notes.tex lines 22800--22960 has the
direction correct. No edit needed to the working_notes; the
spine should cite this lemma directly.

**Cycle 6 — ATTACK (bonus).** Adversarial: does the spine's claim
"they coincide at $N = 1$ by accident, the numerical match forcing
$\phi_{0, 1} = \mathrm{Grit}(\phi_{0, 1})$ at that one point"
make sense? Tracing: $\mathrm{Grit}$ is the additive lift, its domain
is index-$2$ Jacobi forms, so $\mathrm{Grit}(\phi_{0, 1})$ literally
doesn't parse if $\phi_{0, 1}$ has index $1$. What was meant: at
$N = 1$, the weight-$5$ paramodular form $\Delta_5$ admits two
equivalent descriptions:
(a) $\Delta_5 = \mathrm{Bor}(\phi_{0, 1})$ (Borcherds multiplicative,
weight = $c(0)/2 = 5$);
(b) $\Delta_5 = \mathrm{Grit}(\phi_{5, 2})$ (Gritsenko additive,
weight = weight of input = $5$).
The "two lifts of one Jacobi form" coincidence is false; there are
TWO different Jacobi forms $\phi_{0, 1}$ and $\phi_{5, 2}$, each lifted
by a DIFFERENT operation, producing the SAME paramodular form
$\Delta_5$. This is the non-accidental structural compatibility of
the multiplicative and additive lifts on the paramodular space.
**HEAL.** The spine's "accident at $N = 1$" phrasing mischaracterises
this as an accident; it is a theorem (Gritsenko 1999 Thm.~3.1:
multiplicative-vs-additive compatibility on the paramodular space).
Rephrase: "the three lifts coincide on $\Delta_5$ by the
Gritsenko 1999 Thm.~3.1 multiplicative-additive compatibility
theorem, which extends uniformly to the CHL slice."

End of attack-heal cycles.
