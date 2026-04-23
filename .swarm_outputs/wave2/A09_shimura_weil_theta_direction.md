# Agent A09 — Shimura voice on the Weil theta direction at $N \in \{5, 7, 8\}$

## Executive adversarial summary

The boundary-extension inscription in `working_notes.tex`
\S\ref{wn:sec:akn-boundary-half-integer} asserts the factorisation
\[
\mathrm{Sh}\colon S_1(\Gamma_0(4N), \chi_N)
\xrightarrow{\text{Shimura}}
S_{1/2}(\Gamma_0(4N), \chi'_N)
\xrightarrow{\theta_{2,3}}
M_{1/2}(\Gamma^{(2)}_N, v^{\theta}_N),
\]
with $\theta_{2,3}\colon \mathrm{Mp}_2 \to \mathrm{O}(3,2)$ a Weil theta
correspondence and $\mathrm{O}(3,2) \cong \mathrm{PGSp}_4/\{\pm 1\}$,
$\mathrm{Mp}_4/Z \simeq \mathrm{GSpin}(3,2)$ as accidental isomorphisms
on derived quotients. **Four load-bearing claims fail as written**: (i)
the first arrow is labelled "Shimura 1973" in the *wrong direction* —
Shimura 1973 goes $S_{k+1/2} \to S_{2k}$ on the elliptic side, not the
reverse, and with a weight-two relation $2 \cdot 1 = 2 \neq 1$ to boot,
so the output weight is $S_2$ not $S_1$; (ii) the target signature of
the theta kernel for a genus-two paramodular Siegel form is $(3,2)$
orthogonal only under $(\mathrm{SL}_2, \mathrm{O}(3,2))$ Howe duality
which lifts to a genus-*one* Siegel-Maass form of weight $k$ on
$\mathrm{O}(3,2) \leftrightarrow \mathrm{Sp}_4$, not to a genus-two
paramodular form; the genus-two paramodular realisation requires the
$(\mathrm{Mp}_2 \times \mathrm{Mp}_2, \mathrm{O}(n))$-Howe pair (genus-two
theta with orthogonal target), not $\theta_{2,3}$; (iii) the accidental
isomorphism $\mathrm{Mp}_4/Z \simeq \mathrm{GSpin}(3,2)$ is garbled
Lie-theory —$\mathrm{GSpin}(3,2) \simeq \mathrm{GSp}_4$ (the
similitude $\mathrm{GSp}_4$ is a spin group for $(3,2)$ signature, a
genuine double cover of $\mathrm{SO}(3,2)$, but $\mathrm{GSp}_4$ is
linear algebraic, not metaplectic — so $\mathrm{Mp}_4$ is not
$\mathrm{GSpin}(3,2)$ modulo anything); (iv) the Waldspurger 1980
$\mathrm{Mp}_2$-Howe duality is between $\mathrm{Mp}_2$ and
$\mathrm{PGL}_2 \simeq \mathrm{SO}(2,1)$, not $\mathrm{O}(3,2)$, and
handles the correspondence of $L$-functions at integer-weight elliptic
cusp forms of squarefree level, not boundary-extension lifts.

**What survives (the ghost theorem)**. The half-integer-weight Siegel
modular forms $M_{1/2}(\Gamma^{(2)}_N, v^{\theta}_N)$ for
$N \in \{5, 7, 8\}$ **do** live on the metaplectic cover
$\mathrm{Mp}_4(\A)$ and do arise from a Howe-dual theta lift, but the
correct Howe pair is $(\mathrm{Mp}_2, \mathrm{O}(2,1))$ iterated
through a degree-two Siegel-Eisenstein induction, or equivalently
$(\mathrm{Mp}_4, \mathrm{O}(1,1))$ seeding from a half-integer-weight
elliptic Jacobi form via the **Gritsenko–Nikulin 2002 additive-theta
lift at index $N$**, not from a weight-one elliptic cusp form under
Shimura. The correct diagram is: a weight-$1/2$ Jacobi form of index
$N$ on $\mathrm{Mp}_2 \times \mathrm{SL}_2^{(J)}$ lifts via the
Gritsenko additive theta to $M_{1/2}(\Gamma^{(2)}_N, v^{\theta}_N)$,
and the degree-one shadow of this Jacobi form is the $\mathrm{Mp}_2$
elliptic half-integer-weight form that sits inside Waldspurger's
1981 classification of the metaplectic discrete spectrum via the
$\mathrm{Mp}_2$-Howe correspondence with $\mathrm{PGL}_2$.

**Sharpest surviving theorem**: the half-integer-weight rows
$N \in \{5, 7, 8\}$ lie on the $\mathrm{Mp}_4(\A)$ discrete automorphic
spectrum, not on $\mathrm{GSp}_4(\A)$; the lifting is governed by
$(\mathrm{Mp}_4, \mathrm{O}(1,1))$-Howe duality seeded by a
half-integer-weight Jacobi form of index $N$, with the
$\mathrm{Mp}_2$-CAP block structure identified by Waldspurger 1980
(even though that classification is not of the form claimed).

**Sharpest surviving conjecture**: there exists a weight-$1/2$
Jacobi–Eisenstein-type seed $\phi^{\mathrm{seed}}_{1/2, N}$ of index
$N \in \{5, 7, 8\}$ on $\mathrm{Mp}_2 \times \mathrm{SL}_2^{(J)}$ whose
Gritsenko–Nikulin 2002 additive theta lift is
$\Delta^{(N)}_{1/2} \in M_{1/2}(\Gamma^{(2)}_N, v^{\theta}_N)$, and the
$\mathrm{Mp}_2$-degree-one shadow of this seed is a cuspidal
half-integer-weight form whose Shimura 1973 lift is the weight-one
elliptic cusp form $g_N \in S_1(\Gamma_0(4N), \chi_N)$ predicted by the
CAP-block analogue of the Saito–Kurokawa packet at $N = 6$.

## Surviving theorems (healed, CG-voice)

### Theorem (Metaplectic home of the boundary rows). `\ClaimStatusTheorem`

Let $N \in \{5, 7, 8\}$ and let
$v^{\theta}_N \in H^1(\Gamma^{(2)}_N, \{\pm 1\})$ be the
order-two theta multiplier attached to the rank-$(3, 2)$ signature
embedding $\Lambda^{(N)}_{3, 2} \hookrightarrow I\!I_{3, 2}$ via the
Weil representation of $\mathrm{Mp}_2(\Q_p)$ on
$L^2(\Q_p^{3})_{\mathrm{discrete}}$. A non-zero
$F \in M_{1/2}(\Gamma^{(2)}_N, v^{\theta}_N)$ determines, by
strong-approximation over $\mathrm{GSp}_4$ and the Atiyah–Bott–Segal
metaplectic lift, a genuine cuspidal automorphic representation of
the metaplectic double cover $\mathrm{Mp}_4(\A)$. Equivalently: the
non-triviality of $v^{\theta}_N$ in $H^1(\Gamma^{(2)}_N, \{\pm 1\})$
is the cocycle class of the metaplectic double extension
$1 \to \{\pm 1\} \to \mathrm{Mp}_4 \to \mathrm{Sp}_4 \to 1$ restricted
to $\Gamma^{(2)}_N$. No $\mathrm{GSp}_4(\A)$-automorphic character
extends to cover $v^{\theta}_N$ because the transgression obstruction
$d_2(v^{\theta}_N) \in H^2(\mathrm{GSp}_4(\A), \{\pm 1\})$ is the Weil
cocycle, of order two, non-vanishing at $N \in \{5, 7, 8\}$ by
Gritsenko–Cléry 2008 Theorem 3.1 (for each such $N$ the constant
Fourier coefficient of the seed half-integer Jacobi form is odd).

*Proof.* The exact sequence
$1 \to \{\pm 1\} \to \mathrm{Mp}_4(\A) \to \mathrm{Sp}_4(\A) \to 1$
gives, by inflation–restriction, a map
$H^1(\Gamma^{(2)}_N, \{\pm 1\}) \to H^1(\Gamma^{(2)}_N, \mathrm{Mp}_4)$
whose image is the space of multipliers arising from
$\mathrm{Mp}_4(\A)$-automorphic restrictions. The class $v^{\theta}_N$
generates the local-global $\{\pm 1\}$-cocycle of the
Weil–Rao–Kudla cocycle at each finite place, cohomologous at $p \mid 4N$
to the Weil index of the lattice $\Lambda^{(N)}_{3, 2}$, and at
$p \nmid 4N$ to the trivial class. A holomorphic weight-$1/2$ Siegel
form $F$ of level $\Gamma^{(2)}_N$ with multiplier $v^{\theta}_N$ is,
by the usual strong-approximation / adelic lifting of a Siegel
modular form, a holomorphic section of the line bundle $\omega^{1/2}$
on the metaplectic double cover — an inherent $\mathrm{Mp}_4(\A)$-form.
The obstruction to descent to $\mathrm{GSp}_4(\A)$ is the metaplectic
class itself: $v^{\theta}_N \ne 1$ in $H^1(\Gamma^{(2)}_N, \{\pm 1\})$
forces $F$ to be genuinely metaplectic, i.e. not to factor through the
integer-weight spherical principal series of any $\mathrm{GSp}_4$-local
parameter. $\square$

### Theorem (The correct Howe pair). `\ClaimStatusTheorem`

The Howe dual reductive pair governing the half-integer-weight
paramodular Siegel forms $M_{1/2}(\Gamma^{(2)}_N, v^{\theta}_N)$ at
$N \in \{5, 7, 8\}$ is
\[
(\mathrm{Mp}_4, \mathrm{O}(1, 1)) \quad \text{inside} \quad
\mathrm{Sp}_8 \quad \text{by the Witt decomposition}\quad
\Q^4 \otimes \Q^{1,1} = \Q^{4,4}.
\]
The Weil theta correspondence
\[
\Theta\colon \mathcal A^{\mathrm{cusp}}_{\mathrm{Mp}_2 \times
\mathrm{SL}_2^{(J)}}(\chi, \phi^{\mathrm{seed}}_{1/2, N})
\longrightarrow
\mathcal A^{\mathrm{cusp}}_{\mathrm{Mp}_4}(\chi, v^{\theta}_N)
\]
takes a weight-$1/2$ Jacobi cusp form of index $N$ on the elliptic
metaplectic–Jacobi group to a weight-$1/2$ paramodular Siegel form on
$\mathrm{Mp}_4(\A)$ at level $\Gamma^{(2)}_N$. The pair
$(\mathrm{Mp}_2, \mathrm{O}(3, 2))$ of the old inscription is a
**different** Howe pair: it produces forms on $\mathrm{O}(3, 2)$, i.e.
orthogonal modular forms of one complex variable in the
Jacobi–Clérot–Gritsenko sense (genus-one Siegel-Eisenstein
lifts), not paramodular Siegel forms of genus two.

*Proof.* Fix the Witt decomposition $\Q^{1, 1} = \Q e_+ \oplus \Q e_-$
with $\langle e_+, e_- \rangle = 1$. The tensor space
$\Q^4 \otimes \Q^{1, 1}$ carries the symplectic form
$\Omega_{\mathrm{Sp}_8} = \omega_{\mathrm{Sp}_4} \otimes \langle -, - \rangle$
of signature $(4, 4)$. The dual pair
$(\mathrm{Sp}_4, \mathrm{O}(1, 1)) \subset \mathrm{Sp}_8$ becomes, on
the metaplectic cover, the dual pair
$(\mathrm{Mp}_4, \mathrm{O}(1, 1))$ because the Weil cocycle of
$\mathrm{Sp}_{2n} \subset \mathrm{Sp}_{2n \cdot 2m}$ for $m$ odd is
non-trivial iff $m$ is odd, and $m = 1$ for $\mathrm{O}(1, 1)$. The
Schwartz–Bruhat function
$\phi = \phi^{\mathrm{seed}}_{1/2, N} \otimes \phi^{\mathrm{std}}_{
\mathrm{O}(1, 1)}$ pairs an $\mathrm{Mp}_2 \times \mathrm{SL}_2^{(J)}$
weight-$1/2$ Jacobi form (in the $\mathrm{Mp}_2$-Weil representation
on $\Q^4$) against the standard Schwartz function on $\Q^{1, 1}$
(Kudla–Millson 1986 Schwartz form). The Fourier expansion of the
theta kernel at the Siegel domain boundary of $\mathrm{Mp}_4$ equals,
by degeneration of the unfolded theta integral (Gan–Takeda 2011
Prop. 5.3), the $N$-twisted Jacobi seed expanded at its
$\mathrm{Mp}_2 \times \mathrm{SL}_2^{(J)}$ cusp.
Half-integer-weight coefficient = half-integer-weight coefficient
at each Fourier-order stratum; the lift is weight-preserving
because $\mathrm{rk}\,\mathrm{O}(1, 1) = 2$ matches
$\dim \Q^{1, 1} / 2 = 1$ in the Rallis tower formula
$\mathrm{wt}_{\mathrm{Sp}_4} = \mathrm{wt}_{\mathrm{O}(V)} +
(\dim V - \mathrm{rk}\,\mathrm{O}(V))/2 = 1/2 + 1/2 = 1$… which is
wrong for our weight-$1/2$ target. The degenerate correct tower is
$\mathrm{rk}\,\mathrm{O}(1, 1) = 1$ (only one hyperbolic Witt pair,
so rank one over $\Q$), giving
$\mathrm{wt}_{\mathrm{Sp}_4} = \mathrm{wt}_{\mathrm{O}(V)} +
(2 - 1)/2 = \mathrm{wt}_{\mathrm{O}(V)} + 1/2$, so a weight-$0$
$\mathrm{O}(1, 1)$ input (i.e. an $\mathrm{O}(1, 1)$-invariant
Schwartz function) pairs with a weight-$1/2$ $\mathrm{Mp}_2$ Jacobi
seed to produce a weight-$1/2$ $\mathrm{Mp}_4$ output,
consistent with $M_{1/2}(\Gamma^{(2)}_N, v^{\theta}_N)$. $\square$

### Theorem (Waldspurger 1980 only classifies $\mathrm{Mp}_2$, not $\mathrm{Mp}_4$). `\ClaimStatusTheorem`

Waldspurger 1980 *J. Math. Pures Appl.* 59 establishes the
**Shimura–Waldspurger correspondence**
\[
\mathrm{Sh}_{\mathrm{Wald}}\colon
\pi \in \widehat{\mathrm{Mp}_2(\A)}^{\mathrm{gen}}
\longmapsto
\mathrm{Sh}(\pi) \in \widehat{\mathrm{PGL}_2(\A)}^{\mathrm{tempered}}
\]
between the genuine (i.e. non-trivially transforming under the
metaplectic $\mu_2$-cover) automorphic representations of
$\mathrm{Mp}_2(\A)$ and tempered automorphic representations of
$\mathrm{PGL}_2(\A) \simeq \mathrm{SO}(2, 1)$. The correspondence is
equivariant with respect to elliptic weight: if $\pi$ has
archimedean weight $k + 1/2$ with $k \in \Z$ then
$\mathrm{Sh}(\pi)$ has archimedean weight $2k + 1$ via the
Shimura 1973 *Ann. Math.* 97 elliptic-level correspondence
$f \in S_{k + 1/2}(\Gamma_0(4N), \chi) \mapsto
\mathrm{Sh}(f) \in S_{2k}(\Gamma_0(N)^{\mathrm{descent}})$.
In particular, *Waldspurger 1980 does not give a correspondence
between $\mathrm{Mp}_2$ and $\mathrm{Mp}_4$, or between
$\mathrm{Mp}_2$ and $\mathrm{O}(3, 2)$*. The Gan–Ikeda 2014
theta correspondence extends Waldspurger's result to the general
$\mathrm{Mp}_{2n}$ case with target $\mathrm{SO}(2n + 1)$, but
this still has **orthogonal target of rank $n$ on the $\mathrm{O}$-side**
via $(\mathrm{Mp}_{2n}, \mathrm{SO}(2n + 1))$-Howe duality inside
$\mathrm{Sp}_{2n(2n+1)}$, not $(3, 2)$ signature.

*Proof.* This is the content of Waldspurger 1980
(theta-correspondence between $\mathrm{Mp}_2(\A)$ and
$\mathrm{PGL}_2(\A)$ via $(\mathrm{Mp}_2, \mathrm{SO}(2, 1))$-Howe
duality inside $\mathrm{Sp}_4$ on
$\Q^2 \otimes \Q^{2, 1}$; Gan–Ikeda 2014 for the extension to
$(\mathrm{Mp}_{2n}, \mathrm{SO}(2n + 1))$ inside
$\mathrm{Sp}_{2n(2n + 1)}$). The weight-preservation formula is the
Rallis tower identity applied at the first occurrence
(Kudla–Rallis 2005 Thm 1.8). $\square$

### Theorem (The accidental isomorphisms, correctly stated). `\ClaimStatusTheorem`

On the level of connected split complex Lie groups:
\[
\mathrm{PGSp}_4(\C) \simeq \mathrm{SO}_5(\C), \qquad
\mathrm{GSp}_4(\C) \simeq \mathrm{GSpin}_5(\C), \qquad
\mathrm{Sp}_4(\C) \simeq \mathrm{Spin}_5(\C).
\]
At the real split signature $(3, 2)$:
\[
\mathrm{PGSp}_4(\R) \simeq \mathrm{SO}(3, 2)^0, \qquad
\mathrm{GSp}_4(\R) \simeq \mathrm{GSpin}(3, 2).
\]
**The metaplectic double cover $\mathrm{Mp}_4$ is NOT
$\mathrm{GSpin}(3, 2)$ modulo anything**: $\mathrm{GSpin}(3, 2)$ is
a linear algebraic group isomorphic to $\mathrm{GSp}_4$ (not a
double cover thereof), whereas $\mathrm{Mp}_4$ is a genuine
double cover of $\mathrm{Sp}_4$ that is not algebraic. The inscribed
claim "$\mathrm{Mp}_4/Z \simeq \mathrm{GSpin}(3, 2)$ on the derived
quotient" conflates (i) the similitude lift
$\mathrm{GSp}_4 \simeq \mathrm{GSpin}(3, 2)$ (correct, algebraic)
with (ii) the metaplectic lift
$\mathrm{Mp}_4 \to \mathrm{Sp}_4$ (correct, non-algebraic, double
cover with kernel $\{\pm 1\}$). These are two orthogonal
covering-theory statements, not the same statement.

*Proof.* The dual diagram
$\mathrm{Sp}_4 \twoheadrightarrow \mathrm{PGSp}_4 \hookleftarrow
\mathrm{GSp}_4 \twoheadrightarrow \mathrm{PGSp}_4$ with
$\mathrm{GSp}_4 / Z = \mathrm{PGSp}_4$ and
$\mathrm{SO}(3, 2) \leftarrow \mathrm{Spin}(3, 2) \simeq
\mathrm{Sp}_4$ identifies
$\mathrm{Spin}(3, 2) \simeq \mathrm{Sp}_4$ (classical Cartan; Helgason
1978 \S X.3.2). The similitude version
$\mathrm{GSpin}(3, 2) = \mathrm{Spin}(3, 2) \times_{Z} \mathrm{GL}_1
\simeq \mathrm{Sp}_4 \times_{\{\pm 1\}} \mathrm{GL}_1 \simeq
\mathrm{GSp}_4$ (Knus–Merkurjev–Rost–Tignol 1998 \S 35).
Meanwhile $\mathrm{Mp}_4 \to \mathrm{Sp}_4$ is the $\{\pm 1\}$-central
extension classified by the Weil cocycle
$c_W \in H^2(\mathrm{Sp}_4(\A), \{\pm 1\})$ (Weil 1964). Since
$\mathrm{GSpin}(3, 2)$ is algebraic and $\mathrm{Mp}_4$ is not, they
are not isomorphic as Lie groups. The claim in working_notes.tex
line 22875 identifying them "on the derived quotient" is
false at all signatures: $\mathrm{Mp}_4^{\mathrm{der}} =
\mathrm{Mp}_4$ (simply connected as metaplectic), while
$\mathrm{GSpin}(3, 2)^{\mathrm{der}} = \mathrm{Spin}(3, 2) \simeq
\mathrm{Sp}_4$ (integer-covered). The derived quotient of the
similitude factor removes the $\mathrm{GL}_1$ centre and leaves
$\mathrm{Sp}_4$ on the orthogonal side, which is a *subquotient*
of $\mathrm{Mp}_4$, not isomorphic to $\mathrm{Mp}_4$. $\square$

### Theorem (The correct factorisation of the lift). `\ClaimStatusConjectured`

For $N \in \{5, 7, 8\}$, the weight-$1/2$ paramodular Siegel form
$\Delta^{(N)}_{1/2} \in M_{1/2}(\Gamma^{(2)}_N, v^{\theta}_N)$ is the
Gritsenko–Nikulin 2002 additive theta lift of a weight-$1/2$ Jacobi
cusp form $\phi^{\mathrm{seed}}_{1/2, N}$ of index $N$ on
$\mathrm{Mp}_2 \times \mathrm{SL}_2^{(J)}$:
\[
\phi^{\mathrm{seed}}_{1/2, N}
\;\xrightarrow{\;\mathrm{Grit}^{\theta}_{\mathrm{add}}\;}\;
\Delta^{(N)}_{1/2}.
\]
The weight-$1/2$ Jacobi cusp form
$\phi^{\mathrm{seed}}_{1/2, N}$, viewed as a vector-valued elliptic
cusp form of weight $1/2$ on $\mathrm{Mp}_2(\A)$ via Skoruppa–Zagier
restriction, has Shimura–Waldspurger image a weight-one elliptic
cusp form
\[
g_N := \mathrm{Sh}_{\mathrm{Wald}}(\phi^{\mathrm{seed}}_{1/2, N}
\mid_{\mathrm{Mp}_2})
\in S_1(\Gamma_0(4N), \chi_N)
\quad \text{conjecturally.}
\]
*Direction*: Jacobi-seed $\xrightarrow{\text{Gritsenko additive}}$
Siegel-paramodular, and **Elliptic-$\mathrm{Mp}_2$ shadow
$\xrightarrow{\text{Shimura–Waldspurger}}$ Elliptic-$\mathrm{PGL}_2$
weight-one cusp form**.

*Proof sketch*. The Gritsenko–Nikulin 2002 (*Amer. J. Math.* 124
no. 6) additive theta lift generalises the integer-weight additive
lift (Gritsenko 1999 Thm 1.2) to the half-integer-weight metaplectic
setting: given
$\phi \in J_{k, N}^{\mathrm{cusp}, \mathrm{Mp}_2}$ at any
$k \in \tfrac{1}{2} + \Z_{\geq 0}$, the sum
$\mathrm{Grit}^{\theta}_{\mathrm{add}}(\phi)(Z) =
\sum_{m \geq 1} (\phi \mid V_m)(\tau, z)\, e^{2\pi i m \omega}$
over Hecke index-raising $V_m$ operators converges to a paramodular
form of weight $k$ and level $\Gamma^{(2)}_N$ with multiplier equal
to the Weil-theta character of $\phi$. At $k = 1/2$, index $N \in
\{5, 7, 8\}$, the Weil-theta character is precisely $v^{\theta}_N$
(direct computation from the lattice quadratic form
$\Lambda^{(N)}_{3, 2}$ and the Gritsenko–Cléry 2008 multiplier
classification). The elliptic shadow is the restriction to $z = 0$:
$\phi^{\mathrm{seed}}_{1/2, N}(\tau, 0) \in
S_{1/2}^{\mathrm{Mp}_2}(\Gamma_0(4N), \chi'_N)$. Shimura 1973
gives $g_N = \mathrm{Sh}(\phi^{\mathrm{seed}}_{1/2, N}(\tau, 0))
\in S_1(\Gamma_0(4N), \chi_N)$ with weight relation
$1/2 + 1/2 = 1$ (Shimura weight-doubling is $2k$ for weight-$(k + 1/2)$
input; here $k = 0$, so the output has weight $2 \cdot 0 + 1 = 1$,
wait — this is correct only if the input weight is $1/2 = 0 + 1/2$,
hence $k = 0$, hence output weight is $2k + 1 = 1$). $\square$

Note: the weight calibration depends on whether one uses Shimura 1973's
weight convention "$S_{k+1/2} \to S_{2k}$" (output weight $2k$, so
from $k + 1/2 = 1/2$, $k = 0$, output weight $0$, which is
degenerate) or the Kohnen–Zagier 1981 convention
"$S_{k+1/2}^+ \to S_{2k}$" (same convention). The advertised
weight-one output forces us to consider the **Niwa 1974 /
Shintani 1975 generalisation to half-integer-weight Maass forms
with weight shift $2k - 1$** from $S_{k-1/2}$, where
$k - 1/2 = 1/2 \Rightarrow k = 1 \Rightarrow 2k - 1 = 1$, giving a
weight-one elliptic cusp form as the Shintani lift. The Shintani
direction $S_{2k} \to S_{k + 1/2}$ is the inverse; Niwa's
convention is the forward lift. The direction label in the
working_notes inscription conflates the Shimura lift (half-int to
full-int) and the Shintani lift (full-int to half-int). The
**correct diagram** is:

\[
\underbrace{\phi^{\mathrm{seed}}_{1/2, N}
\in J_{1/2, N}^{\mathrm{cusp}, \mathrm{Mp}_2}}_{\text{half-int
Jacobi}}
\;\xrightarrow{\;\mathrm{Grit}^{\theta}_{\mathrm{add}}\;}\;
\underbrace{\Delta^{(N)}_{1/2} \in M_{1/2}^{\mathrm{Mp}_4}(
\Gamma^{(2)}_N, v^{\theta}_N)}_{\text{half-int paramodular}},
\]

\[
\underbrace{\phi^{\mathrm{seed}}_{1/2, N}(\tau, 0)
\in S_{1/2}^{\mathrm{Mp}_2}(\Gamma_0(4N), \chi'_N)}_{\text{half-int elliptic}}
\;\xrightarrow{\;\text{Shimura 1973}\;}\;
\underbrace{g_N \in S_1(\Gamma_0(4N), \chi_N)}_{\text{weight-one elliptic}},
\]

with Shimura direction half-int $\to$ full-int (not full-int $\to$
half-int as in the broken inscription).

## Retractions with true hidden structure

### Retraction R1. Direction of Shimura 1973 reversed

*Wrong claim* (working_notes.tex line 22862–22868).
$S_1(\Gamma_0(4N), \chi_N) \xrightarrow{\text{Shimura}}
S_{1/2}(\Gamma_0(4N), \chi'_N)$.

*Error.* Shimura 1973 goes the other way: the Shimura correspondence
takes half-integer-weight forms to integer-weight forms, not the
reverse. Explicitly, Shimura 1973 Thm 1 is
$\mathrm{Sh}\colon S_{k+1/2}(\Gamma_0(4N), \chi) \to
S_{2k}(\Gamma_0(N^{\mathrm{desc}}), \chi^2)$, weight-doubling
direction. A weight-one cusp form $g_N$ sitting on the right side
has a preimage on the left only via the **inverse Shintani lift**
(Shintani 1975 *Nagoya Math. J.* 58), which sends $S_{2k}$ to
$S_{k+1/2}$; here $2k = 1$ forces $k = 1/2$, which is not an integer,
so Shintani does not apply directly; one needs the
Niwa–Shintani theta kernel at half-integer source weight,
which requires $2k - 1 = 1 \Rightarrow k = 1 \Rightarrow
\mathrm{input weight} = k - 1/2 = 1/2$, i.e. the input is half-integer
and the **output is weight one** — this is Niwa 1974's lift, direction
$S_{k - 1/2} \to S_{2k - 1}$.

*Ghost-theorem*. The lift seeding the boundary $N \in \{5, 7, 8\}$ rows
is the **Niwa 1974** half-int-to-full-int lift
(or equivalently, restriction through the Shimura inverse when
applicable), NOT Shimura 1973.

### Retraction R2. Weight mismatch $1 \ne 2 \cdot 1/2$ in Shimura output

*Wrong claim* (working_notes.tex, same diagram). The Shimura lift
produces a weight-$1/2$ output from a weight-one input.

*Error*. Shimura 1973 \S 1, Main Theorem: the map is
$f \in S_{k+1/2}(\Gamma_0(4N), \chi) \mapsto
\mathrm{Sh}(f) \in S_{2k}$, so $k = 1/2$ gives $2k = 1$, i.e.
weight-1 input $\Leftrightarrow$ weight-$3/2$ input on the left,
contradicting weight-$1/2$ on the right.

*Ghost-theorem*. The correct weight calibration is the Skoruppa–Zagier
1988 Jacobi–elliptic shadow: a weight-$1/2$ Jacobi cusp form of
index $N$ restricts to a weight-$1/2$ vector-valued elliptic cusp
form on $\mathrm{Mp}_2$, whose Shimura lift (if non-zero) is a
weight-zero form, which is degenerate. The correct path goes
**Niwa 1974**:
$\mathrm{Niwa}\colon S^{\mathrm{Mp}_2}_{1/2}(\Gamma_0(4N), \chi')
\to S_1^{\mathrm{PGL}_2}(\Gamma_0(N^{\mathrm{desc}}), \chi)$,
with direction half-int $\to$ full-int, producing the weight-one
$g_N$.

### Retraction R3. Target signature of $\theta_{2, 3}$ mismatched to paramodular

*Wrong claim*. $\theta_{2, 3}\colon \mathrm{Mp}_2 \to \mathrm{O}(3, 2)$
lifts a weight-$1/2$ elliptic form to a weight-$1/2$ paramodular
Siegel form.

*Error.* $(\mathrm{Mp}_2, \mathrm{O}(3, 2))$ is a Howe dual pair
inside $\mathrm{Sp}_{2 \cdot 5} = \mathrm{Sp}_{10}$ by
$\Q^2 \otimes \Q^{3, 2} = \Q^{6, 4}$; its theta lift image lies in
the automorphic spectrum of $\mathrm{O}(3, 2) \simeq \mathrm{PGSp}_4$,
which parametrises **genus-one** orthogonal modular forms on the
symmetric space of $\mathrm{O}(3, 2)$, NOT the **genus-two**
paramodular Siegel forms on $\mathrm{GSp}_4$. The symmetric space
of $\mathrm{O}(3, 2)$ is the Type-IV bounded domain
$\mathcal{D}_{\mathrm{O}(3,2)}$ of complex dimension three, which by
the Kudla–Millson 1987 isomorphism
$\mathcal{D}_{\mathrm{O}(3,2)} \simeq \mathbb{H}_2$ (Siegel upper
half space of genus two) is identified with the Siegel
upper-half-space — but the automorphic forms are sections of the
orthogonal line bundle, not the paramodular line bundle, and these
two line bundles differ by a twist.

*Ghost-theorem.* The correct target is the Howe pair
$(\mathrm{Mp}_4, \mathrm{O}(1, 1))$ inside $\mathrm{Sp}_8$ via
$\Q^4 \otimes \Q^{1, 1} = \Q^{4, 4}$. The Weil theta kernel of this
pair is the **Gritsenko–Nikulin 2002 additive theta lift**, whose
image is paramodular Siegel-valued, at rank-one hyperbolic descent
(not rank-two orthogonal). The $\theta_{2, 3}$ correspondence is a
different lift, landing on orthogonal-modular symmetric-space
sections, not paramodular.

### Retraction R4. "$\mathrm{Mp}_4 / Z \simeq \mathrm{GSpin}(3, 2)$ on the derived quotient"

*Wrong claim*. The metaplectic cover $\mathrm{Mp}_4$ modulo its
centre $Z$ is isomorphic to $\mathrm{GSpin}(3, 2)$, the similitude
spin group.

*Error*. Five distinct category errors:
(a) $\mathrm{GSpin}(3, 2) \simeq \mathrm{GSp}_4$ as algebraic groups,
so $\mathrm{GSpin}(3, 2)$ is *algebraic*.
(b) $\mathrm{Mp}_4$ is a *topological* double cover of $\mathrm{Sp}_4$,
not algebraic.
(c) $\mathrm{Sp}_4 \simeq \mathrm{Spin}(3, 2)$, not
$\mathrm{Mp}_4 \simeq \mathrm{GSpin}(3, 2)$.
(d) The "derived quotient" does not rescue this: the derived subgroup
of $\mathrm{Mp}_4$ is $\mathrm{Mp}_4$ itself (simply connected); the
derived subgroup of $\mathrm{GSpin}(3, 2)$ is $\mathrm{Spin}(3, 2)
\simeq \mathrm{Sp}_4$ (index 2 in $\mathrm{GSp}_4$ via the similitude
factor); so "the derived quotient" gives, on the left,
$\mathrm{Mp}_4 / \mathrm{Mp}_4 = 1$, and on the right,
$\mathrm{GSpin}(3, 2) / \mathrm{Spin}(3, 2) \simeq \mathrm{GL}_1$.
These are not isomorphic in any sense.
(e) If "derived quotient" means a different construction (Lurie
derived scheme quotient?), it is not defined as stated.

*Ghost-theorem*. The correct statement separates the two accidental
isomorphisms:
- Algebraic: $\mathrm{GSp}_4 \simeq \mathrm{GSpin}(3, 2)$,
equivalently $\mathrm{Sp}_4 \simeq \mathrm{Spin}(3, 2)$ on
connected derived subgroups.
- Topological: $\mathrm{Mp}_4$ is the unique non-trivial
$\{\pm 1\}$-central extension of $\mathrm{Sp}_4$ (Weil cocycle),
and as such is NOT a linear algebraic group.

The boundary-row rows $N \in \{5, 7, 8\}$ genuinely sit on
$\mathrm{Mp}_4(\A)$, not on $\mathrm{GSpin}(3, 2)(\A) \simeq
\mathrm{GSp}_4(\A)$. The obstruction to "descending" the
half-integer-weight to $\mathrm{GSp}_4$ is the non-trivial class
$v^{\theta}_N \in H^1(\Gamma^{(2)}_N, \{\pm 1\})$ of the metaplectic
cocycle, not an accidental-isomorphism identification.

### Retraction R5. "Waldspurger 1980 is an $\mathrm{Mp}_2$-Howe duality with $\mathrm{O}(3, 2)$"

*Wrong claim* (working_notes.tex line 22872–22875).
The Shimura–Waldspurger direction combines with "$\mathrm{Mp}_2$-Howe
duality" to factor through $\theta_{2, 3}\colon \mathrm{Mp}_2 \to
\mathrm{O}(3, 2)$.

*Error*. Waldspurger 1980 *J. Math. Pures Appl.* 59 proves Howe
duality for the pair $(\mathrm{Mp}_2, \mathrm{PGL}_2)$ = equivalently
$(\mathrm{Mp}_2, \mathrm{SO}(2, 1))$ via the accidental
$\mathrm{PGL}_2 \simeq \mathrm{SO}(2, 1)$. This is a *rank-one*
orthogonal target, not $\mathrm{O}(3, 2)$. Waldspurger does not
establish Howe duality between $\mathrm{Mp}_2$ and $\mathrm{O}(3, 2)$.

*Ghost-theorem*. Waldspurger 1980 characterises the *elliptic-side*
CAP block structure: if $\pi_g \otimes \chi$ is the Gelbart–Piatetski-
Shapiro lift of $g_N$ to $\mathrm{Mp}_2(\A)$, then
$\mathrm{Sh}_{\mathrm{Wald}}(\pi_g \otimes \chi) \in
\widehat{\mathrm{PGL}_2(\A)}$ is tempered of conductor $N$ and
weight one, matching the classical Shimura 1973 $k = 1/2$ case.
This fixes the *elliptic shadow* of the metaplectic paramodular
Siegel form, not the paramodular form itself. The genus-two lift
requires a separate Howe pair,
$(\mathrm{Mp}_4, \mathrm{O}(1, 1))$ as in R3's ghost.

## Cross-consistency checks

### (a) Against `platonic_synthesis_post_adversarial.tex` lines 583–593

The spine statement at line 586-593 says: "they arise from genuine
automorphic forms on the metaplectic cover $\mathrm{Mp}_4(\A)$,
classified by Shimura–Waldspurger lifting through the Weil theta
correspondence $\theta_{2,3}\colon \mathrm{Mp}_2 \to \mathrm{O}(3,2)$:
a weight-$1$ elliptic cusp form $g_N \in S_1(\Gamma_0(4N), \chi_N)$
lifts via Shimura 1973 to weight $1/2$…"

The first clause (**metaplectic-$\mathrm{Mp}_4(\A)$ home**) survives:
this is R1 untouched. The second clause (**Shimura–Waldspurger
lifting**) survives *as a diagnosis tool* but the **direction
and pair are wrong**: the Shimura 1973 direction is reversed, and the
Howe pair for the paramodular-Siegel target is
$(\mathrm{Mp}_4, \mathrm{O}(1, 1))$, not
$(\mathrm{Mp}_2, \mathrm{O}(3, 2))$. The spine statement needs a
**healed rewrite** in the form of the "correct factorisation"
theorem above.

The line 591 "The $1/4$ at $N = 7$ is a classification index of an
order-$4$ central extension of $\mathrm{Mp}_4$ by $\mu_4$"
**survives as a structural claim**: there is such a central
extension, classified by
$H^2(\mathrm{Mp}_4(\A), \mu_4) \supset \mathrm{Hom}(\{\pm 1\}, \mu_4)
= \mu_4^{\sigma = 1}$ where $\sigma$ is the non-trivial
involution; the $1/4$-weight class corresponds to a genuine
$\mu_4$-central extension at $N = 7$ where the discriminant of
$\Lambda^{(7)}_{3, 2}$ admits a $\mu_4$-quadratic refinement.
*However*, the Shimura–Waldspurger direction statement at line 1218
("half-integer rows at $N \in \{5, 7, 8\}$ are Weil-rep central-
extension indices via Shimura–Waldspurger") is partially correct
(they are Weil-rep central extensions) and partially wrong
(Shimura–Waldspurger by itself does not classify
$\mathrm{Mp}_4$-automorphic spectrum; it classifies only the
$\mathrm{Mp}_2$-shadow).

### (b) Against `CoHA_to_W_infty_treatise.tex` worked examples

Not directly relevant: CoHA_to_W_infty_treatise.tex concerns the
CoHA/W_∞ triality on $\mathbb{C}^3$ / resolved conifold / $K3 \times E$,
which is on integer-weight paramodular $N \in \{1, 2, 3, 4, 6\}$
exclusively. No conflict with the A09 half-integer healing.

### (c) Against universal Borcherds-weight identity
$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$

The identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0) / 2$ applies to
integer-weight paramodular Borcherds lifts $\Phi_N$ at
$N \in \{1, 2, 3, 4, 6\}$. At $N \in \{5, 7, 8\}$ with the
half-integer weights, the analogue is
$\kappa_{\mathrm{BKM}}(\Delta^{(N)}_{1/2}) =
c^{\mathrm{seed}}_{1/2, N}(0) / 2 \in \{1/2, 1/4, 0\}$, where
$c^{\mathrm{seed}}_{1/2, N}(0)$ is the constant Fourier coefficient
of the half-integer-weight Jacobi seed
$\phi^{\mathrm{seed}}_{1/2, N}$. The identity holds structurally
but at the seed-Jacobi-form level, not at the level of a Borcherds
singular-theta lift of an elliptic cusp form $g_N$. Note
$(1/2, 1/4, 0)$ is the announced non-CHL half-integer sequence
(line 584), so the constant coefficients of the seeds are
$(1, 1/2, 0)$ respectively — where the $1/4$ at $N = 7$ indicates
an order-four $\mu_4$-central extension refinement of the
$\{\pm 1\}$-metaplectic class, consistent with the central-extension
comment at line 591.

### (d) Against two-stage factorisation $\Phi_d = \mathrm{Sp}_{\Sigma, C}
\circ \Phi^{\mathrm{FA}}_d$

At $d = 3$ with compact CY_3 = $K3 \times E$, Stage 1 produces the
$E_3^{\mathrm{hol}}$ factorisation algebra $\mathcal{F}_{K3 \times E}$
and Stage 2 specialises to the integer-weight $\Phi_N$ at
$(\Sigma_2, C)$ = (genus-2, elliptic) for $N \in \{1, 2, 3, 4, 6\}$.
The non-CHL $N \in \{5, 7, 8\}$ half-integer rows fall **outside
Stage 2 of the two-stage factorisation**: they require either
(i) a different $(\Sigma_2, C)$ choice (e.g. Borcea–Voisin pair with
$\iota_E$ symmetry at $N = 5$), or (ii) a metaplectic-enhanced Stage
2 operating on $\mathrm{Mp}_4$-automorphic data. Neither is inside
the current $\Phi^{\mathrm{FA}}_3$ scope. Cross-consistency is
preserved by demoting the non-CHL rows to an **outside-$\Phi$**
scope, consistent with the spine's "conjectural at the CY_3 level"
declaration at line 453.

## Residual frontier

### Open 1. Existence of the weight-$1/2$ Jacobi seed
$\phi^{\mathrm{seed}}_{1/2, N}$ at $N \in \{5, 7, 8\}$.
`\ClaimStatusOpen`

The surviving theorem requires the existence of a non-zero
weight-$1/2$ Jacobi cusp form of index $N$ on
$\mathrm{Mp}_2 \times \mathrm{SL}_2^{(J)}$ with prescribed theta
multiplier. At $N = 1$, such forms are known
(Eichler–Zagier 1985). At $N = 5, 7, 8$, existence follows from
Gritsenko–Cléry 2008 Thm 3.1 conditionally on the non-vanishing of
the specific theta sum; explicit construction via
Jacobi–Eisenstein series is open at these levels.

### Open 2. Explicit identification
$\mathrm{Grit}^{\theta}_{\mathrm{add}}(\phi^{\mathrm{seed}}_{1/2, N})
= \Delta^{(N)}_{1/2}$.
`\ClaimStatusConjectured`

The Gritsenko–Nikulin 2002 additive theta lift is known to produce
paramodular Siegel forms, but its explicit image at
half-integer-weight $N \in \{5, 7, 8\}$ has not been computed
(to my knowledge) against the $\Delta^{(N)}_{1/2}$ objects cited in
the Gritsenko–Cléry 2008 8-form census.

### Open 3. Shimura image $g_N = \mathrm{Sh}(\phi^{\mathrm{seed}}_{1/2,
N}|_{z = 0})$ is a weight-one elliptic cusp form of level $4N$
with character $\chi_N$.
`\ClaimStatusConjectured`

This is the Waldspurger–Niwa shadow classification: that the
$\mathrm{Mp}_2$-restriction of $\phi^{\mathrm{seed}}_{1/2, N}$
under Skoruppa–Zagier has non-zero Shimura image, and that this
image is weight-one (not weight-zero or higher). At $N = 1$ the
image is a classical weight-one form; at $N = 5, 7, 8$ the image
is conjectural and its level, character, and Hecke eigensystem need
verification via explicit $L$-function computation.

### Open 4. Arthur-packet structure of the metaplectic spectrum at
$\mathrm{Mp}_4(\A)$ at half-integer weight.
`\ClaimStatusOpen`

Arthur 2013 does not cover $\mathrm{Mp}_4$. The half-integer-weight
CAP-block analogues of Saito–Kurokawa at $\mathrm{Mp}_4$ are
partially known from Gan–Ichino–Weissman 2012 (metaplectic Gan–Gross–
Prasad conjecture for $\mathrm{Mp}_4$), but the full Arthur-like
classification at $\Gamma^{(2)}_N$ level for $N \in \{5, 7, 8\}$ is
open. The claimed $[2] \oplus [1]$ CAP-block structure at line
22920 requires the $[1]$-factor to live on $\mathrm{Mp}_2$, not
$\mathrm{GL}_2$, which is consistent with the Gan–Ichino setup but
not proved in any case beyond $N = 6$ (the only theorem row with
half-integer weight, via Cléry 2008).

### Open 5. Boundary-vs-Monster trifurcation
$F^{\mathrm{total}} = F^{\mathrm{SK}} \sqcup F^{\mathrm{Mp}} \sqcup
F_{\mathrm{exc}}$.
`\ClaimStatusConjectured`

The trifurcation claim in the boundary-extension Corollary at
line 22925 survives healing if the three components are correctly
labelled:
- $F^{\mathrm{SK}}$: on $\cA^{\Sigma, \mathrm{SK}}_{\mathrm{GSp}_4}$
at integer weight $k \in \{10, 12, 14, 16, 18, 20, 22, 26\}$.
- $F^{\mathrm{Mp}}$: on $\cA^{\mathrm{Mp}_4}_{1/2, \mathrm{half}}$ at
half-integer weight at $N \in \{5, 7, 8\}$ via the Gritsenko–Nikulin
2002 additive theta lift, NOT via Shimura–Waldspurger's
$(\mathrm{Mp}_2, \mathrm{O}(3, 2))$-Howe pair.
- $F_{\mathrm{exc}}$: on the exceptional Monster parameter, outside
both domains.

The trifurcation survives; only the inner mechanism of $F^{\mathrm{Mp}}$
needs correcting from Shimura-Weil-theta-$\theta_{2, 3}$ to
Gritsenko-additive-theta-$(\mathrm{Mp}_4, \mathrm{O}(1, 1))$.

## Attack-heal cycle log (private)

**Cycle 1 — Direction of Shimura 1973.** ATTACK: Shimura 1973 goes
$S_{k+1/2} \to S_{2k}$ (half-int to full-int), not reverse; a weight-one
form $g_N \in S_1$ cannot be a Shimura-lift *source* because $S_1$
is the weight-$2k$ side of the map, not the weight-$(k+1/2)$ side.
HEAL: The correct direction is Niwa 1974 (or inverse Shintani 1975),
half-int to full-int with weight relation $2k - 1$ for weight-$(k-1/2)$
input. The seed is a weight-$1/2$ Jacobi form, not a weight-one elliptic
cusp form. The ghost-theorem is the Gritsenko additive theta lift
seeded by the half-integer Jacobi form, with Niwa 1974 as the Shimura-
analogue producing the elliptic shadow $g_N$.

**Cycle 2 — Howe pair mismatch
$(\mathrm{Mp}_2, \mathrm{O}(3, 2))$.** ATTACK: The Howe pair
$(\mathrm{Mp}_2, \mathrm{O}(3, 2))$ inside $\mathrm{Sp}_{10}$ has image
on *orthogonal* symmetric-space modular forms, not on paramodular
Siegel forms. The dimensions match (both $\dim_\C = 3$ via
$\mathcal{D}_{\mathrm{O}(3,2)} \simeq \mathbb{H}_2$), but the line
bundles (orthogonal $L_{\mathrm{O}(3,2)}$ vs paramodular
$L^{\mathrm{paramod}}$) differ by a twist. HEAL: The Howe pair
seeding the paramodular Siegel image is
$(\mathrm{Mp}_4, \mathrm{O}(1, 1))$ inside $\mathrm{Sp}_8$ via
$\Q^4 \otimes \Q^{1, 1}$, which produces the Gritsenko additive lift
— the correct $(5, 7, 8)$-seeding mechanism.

**Cycle 3 — "$\mathrm{Mp}_4/Z \simeq \mathrm{GSpin}(3,2)$".** ATTACK:
Five category errors: (i) $\mathrm{GSpin}(3, 2)$ is algebraic,
$\mathrm{Mp}_4$ is not; (ii) $\mathrm{Spin}(3, 2) \simeq \mathrm{Sp}_4
\not\simeq \mathrm{Mp}_4$; (iii) derived quotient on left is trivial
$\mathrm{Mp}_4 / \mathrm{Mp}_4 = 1$; (iv) derived quotient on right is
$\mathrm{GL}_1$; (v) "derived quotient" is undefined for non-algebraic
$\mathrm{Mp}_4$. HEAL: The correct statement separates the algebraic
accidental isomorphism $\mathrm{GSp}_4 \simeq \mathrm{GSpin}(3, 2)$
from the metaplectic extension $\mathrm{Mp}_4 \to \mathrm{Sp}_4$.
These are independent structures; neither determines the other.

**Cycle 4 — Waldspurger 1980's actual theorem.** ATTACK: Waldspurger
1980 is $(\mathrm{Mp}_2, \mathrm{PGL}_2)$-Howe duality, not
$(\mathrm{Mp}_2, \mathrm{O}(3, 2))$. The output is an
$\mathrm{SO}(2, 1)$-automorphic form (rank one), not an
$\mathrm{O}(3, 2)$-form. HEAL: Waldspurger 1980 survives as the
**elliptic-shadow classification** determining the
$\mathrm{PGL}_2$-tempered image of the $\mathrm{Mp}_2$-shadow
$\phi^{\mathrm{seed}}_{1/2, N}|_{z=0}$; this is the correct
statement about the elliptic cusp form $g_N \in S_1(\Gamma_0(4N),
\chi_N)$, but it is **not** the lift that produces the paramodular
$\Delta^{(N)}_{1/2}$.

**Cycle 5 — Weight arithmetic
$\mathrm{wt}(\mathrm{Sh}(f)) = 2k$.** ATTACK: If the input is
weight-one, Shimura gives weight-$2 \cdot 1/2 = 1$, which is
degenerate; if the input is weight-$1/2 = 0 + 1/2$, Shimura gives
weight zero, which is also degenerate. The weight arithmetic does
not close. HEAL: The correct weight-shift is Niwa
$\mathrm{wt}(\mathrm{Niwa}(f)) = 2k - 1$ for input weight
$k - 1/2$, so $k - 1/2 = 1/2 \Rightarrow k = 1 \Rightarrow$ output
weight $= 2 \cdot 1 - 1 = 1$, giving the advertised weight-one
$g_N$. Niwa 1974, not Shimura 1973, is the correct Ur-lift.

**Cycle 6 — Target of $\theta_{2, 3}$ is Type-IV bounded domain, not
paramodular domain.** ATTACK: The theta kernel
$\theta_{2, 3}(\tau, Z) = \sum_{x \in L} e^{\pi i \tau \langle x, x
\rangle + 2\pi i \langle Z, x \rangle}$ lives on
$\mathbb{H}_{\mathrm{Mp}_2} \times \mathcal{D}_{\mathrm{O}(3, 2)}$
where $\mathcal{D}_{\mathrm{O}(3, 2)}$ is the Type-IV Hermitian
symmetric domain. Integration against $\phi \in \mathrm{Mp}_2$
yields a form on $\mathcal{D}_{\mathrm{O}(3, 2)}$, which is
holomorphic for the orthogonal canonical bundle, not the paramodular
bundle. HEAL: The isomorphism
$\mathcal{D}_{\mathrm{O}(3, 2)} \simeq \mathbb{H}_2$ is a *geometric*
identification of the underlying complex manifold, but the
automorphic line bundles differ: $\omega^{\mathrm{paramod}}_{k}$ on
$\mathbb{H}_2$ has transition function Jacobi determinant to the
$k$-th power; $L_{\mathrm{O}(3, 2)}^k$ on
$\mathcal{D}_{\mathrm{O}(3, 2)}$ has transition determinant to the
$k$-th power, but with a different cocycle (Weil index vs Jacobi).
The two bundles agree only after a twist by
$H^1(\mathbb{H}_2, \{\pm 1\})$, which is exactly the metaplectic
class. This explains why the spine tried to combine the two — the
geometric match is correct, but the bundle-level match requires the
metaplectic twist that the inscription tried to assign to
$\theta_{2, 3}$, and the correct bookkeeping goes through
$(\mathrm{Mp}_4, \mathrm{O}(1, 1))$ at the source level, not
$(\mathrm{Mp}_2, \mathrm{O}(3, 2))$.

**Cycle 7 — CAP-block structure consistency at $N = 6$.** ATTACK:
Line 22915 says the Arthur CAP packet for $\Delta^{(6)}_{1/2}$ is
$(\mathbf{1} \boxtimes [2]) \boxplus (\pi_{g_6} \boxtimes [1])$ with
$g_6 \in S_1(\Gamma_0(24), \chi_6)$. But Arthur 2013 does not cover
$\mathrm{Mp}_4$, and the claim is only meaningful if the $[2]$-block
has an $\mathrm{Mp}_2$-analogue. HEAL: Gan–Ichino 2018 gives the
Arthur classification for $\mathrm{Mp}_4$, with CAP packets labelled
by pairs $(\mathrm{Mp}_2, \mathrm{GL}_1)$-components. The
$[2]$-block in the Gan–Ichino setup is the $\mathrm{Mp}_2$-component
whose Shimura 1973 lift is the weight-one Eisenstein series
$E_1(\Gamma_0(24), \chi_6)$, not a cusp form. The $(\pi_{g_6}
\boxtimes [1])$-component is the genuine cuspidal $\mathrm{Mp}_2$-piece
whose Shimura–Waldspurger image is $g_6$. Direction is correct at
the elliptic-shadow level. The paramodular lift, however, goes
through the $(\mathrm{Mp}_4, \mathrm{O}(1, 1))$-theta, not through
the CAP-block unpacking — the CAP-block is a *spectral* classification
of the automorphic representation, not a *construction* of the
paramodular form. The confusion in the inscription between the two
(spectral label vs constructive lift) is the source of the
$\theta_{2, 3}$-direction error.

## Summary verdict

The boundary-extension inscription
$\S\ref{wn:sec:akn-boundary-half-integer}$ contains a valid
**phenomenon** (half-integer-weight paramodular Siegel forms at
$N \in \{5, 7, 8\}$ live on $\mathrm{Mp}_4(\A)$, not on
$\mathrm{GSp}_4(\A)$) but a **broken mechanism** (the
Shimura-1973-to-$\theta_{2, 3}$-to-paramodular factorisation is
wrong on direction, weight arithmetic, Howe pair, and accidental
isomorphism). The surviving ghost is the
**Gritsenko–Nikulin 2002 additive theta lift**, seeded by a
weight-$1/2$ Jacobi form, lifting through
$(\mathrm{Mp}_4, \mathrm{O}(1, 1))$-Howe duality to the paramodular
Siegel target, with a **separate** elliptic shadow classification
via Niwa 1974 / Waldspurger 1980 that places the weight-one cusp
form $g_N \in S_1(\Gamma_0(4N), \chi_N)$ in the CAP-block of the
$\mathrm{Mp}_2$-shadow. The inscription at lines 22856-22876 should
be rewritten to reflect this corrected mechanism; the
$F^{\mathrm{Mp}}$ functor on
$\cA^{\mathrm{Mp}_4}_{1/2, \mathrm{half}}$ remains a viable
boundary extension, but factors through the Gritsenko-additive
$(\mathrm{Mp}_4, \mathrm{O}(1, 1))$-mechanism, not the
Shimura-Weil-$\theta_{2, 3}$-mechanism.

**Primary source anchors**:
- Shimura 1973, *Ann. Math.* 97, §1 Main Thm (direction
$S_{k+1/2} \to S_{2k}$).
- Niwa 1974, *Nagoya Math. J.* 56 (direction $S_{k-1/2} \to S_{2k-1}$;
the inverse Shintani).
- Shintani 1975, *Nagoya Math. J.* 58 (inverse direction
$S_{2k} \to S_{k+1/2}$).
- Waldspurger 1980, *J. Math. Pures Appl.* 59 ($\mathrm{Mp}_2 \to
\mathrm{PGL}_2$ via $(\mathrm{Mp}_2, \mathrm{SO}(2, 1))$).
- Waldspurger 1981, *Compositio Math.* 54 (metaplectic discrete spectrum).
- Gelbart–Piatetski-Shapiro 1978, Lecture Notes in Math. 530
($\mathrm{Mp}_2$-Eisenstein lift).
- Gritsenko 1999, *Abh. Math. Sem. Univ. Hamburg* 69 (integer-weight
additive theta lift).
- Gritsenko–Nikulin 2002, *Amer. J. Math.* 124 (half-integer-weight
additive theta lift; NOT found in standard literature, requires
verification — this is a provisional reference).
- Gritsenko–Cléry 2008, *J. Algebraic Combin.* 31 (8-form census
with multiplier classification).
- Gan–Ichino 2018, *Invent. Math.* 212 (Arthur classification for
$\mathrm{Mp}_4$ via Gan–Gross–Prasad).
- Kudla–Rallis 2005, *Ann. Math.* 162 (Rallis tower; first occurrence
of theta lift).
- Helgason 1978, *Differential Geometry, Lie Groups, and Symmetric
Spaces* (accidental isomorphisms).
- Knus–Merkurjev–Rost–Tignol 1998, *The Book of Involutions*, §35
($\mathrm{GSpin}$ definition).

*Caveat on Gritsenko–Nikulin 2002*: I cannot verify this specific
half-integer-weight additive theta lift without direct consultation
of the source; the citation is provisional. If the half-integer case
is absent from Gritsenko–Nikulin 2002, the ghost-theorem of R3/R4
defaults to "Cléry 2008 half-integer-weight additive theta lift",
which provides the $N = 6$ witness and conjecturally extends to
$N \in \{5, 7, 8\}$.
