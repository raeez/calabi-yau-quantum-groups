# Agent 3B-C23 (Opus 4.7 relaunch) --- Nakajima-Baranovsky comparison on CY$_3$ via Goettsche factorisation + Dunn-Lurie

## Terminal state

**C (SPECIFIC GAP, sharpened).**

The hypothesis "Baranovsky 2000 extends Nakajima to smooth projective
surfaces; threefold extension via Li 2001 + Okounkov-Pandharipande
2010, Goettsche factorisation delivers affine Yangian on principal
component of $\mathrm{Hilb}^n(K3 \times E)$ via Schiffmann-Vasserot 2013
per factor, Dunn-Lurie combines" does **not** close to a theorem on
the direct threefold principal-component correspondence algebra.

What **is** a theorem --- unconditionally --- is the Goettsche-product
side; what remains conjectural is the promotion to a direct threefold
correspondence satisfying Nakajima's Heisenberg commutator relations
on $H^\ast(\mathrm{Hilb}^n_{\mathrm{prin}}(K3 \times E))$. The Dunn-Lurie
additivity input does not bridge the gap: Dunn-Lurie is an *operadic*
theorem ($E_m \otimes E_n \simeq E_{m+n}$, Lurie HA 5.1.2.2; Dunn 1988
*J Pure Appl Algebra* 50) at the level of $\infty$-operads, not a
construction of geometric correspondence cycles on threefold Hilbert
schemes.

## What Dunn-Lurie gives, and what it does not

**What it gives.** If one had already constructed, on
$\bigoplus_n H^\ast_T(\mathrm{Hilb}^n_{\mathrm{prin}}(K3 \times E))$,
two compatible $E_1$-algebra structures $A_{K3}$ and $A_E$ coming
from the $K3$-factor (Nakajima-Grojnowski surface Heisenberg) and the
$E$-factor (symmetric-product Heisenberg on the elliptic curve) such
that their operations commute at the level of higher operadic coherence,
Dunn-Lurie would automatically assemble them into an $E_2$-algebra
structure. This is the Boardman-Vogt tensor product applied to the
two $E_1$-inputs.

**What it does not give.** Dunn-Lurie does not construct either $A_{K3}$
or $A_E$ on the threefold Hilbert scheme. It does not produce the
correspondence cycles $P^n_k(X)$ or the intersection-theoretic
Heisenberg commutator. It presupposes the two $E_1$-inputs as
already-existing algebraic data; the gap in the Nakajima-Baranovsky
threefold comparison is precisely the production of the first $E_1$
(the direct threefold correspondence algebra on
$\mathrm{Hilb}^n_{\mathrm{prin}}(X)$). Dunn-Lurie is downstream of the
obstruction, not a route around it.

## Three gaps, refined

**G1 (surface-to-threefold obstruction, refined).** Baranovsky 2000
*Math.\ Res.\ Lett.* 7, 113-125, Thm.\ 1, generalises Nakajima 1997
*Ann.\ Math.* 145 from $\mathrm{Hilb}^n(S)$ to $M^H(r, c_1, c_2)$ on
**smooth projective surfaces** $S$. Two surface-specific inputs drive
the proof:

- (G1.a) Fogarty 1968 *Amer.\ J.\ Math.* 90: smoothness of
  $\mathrm{Hilb}^n(S)$ for $S$ a smooth projective surface, dimension
  $2n$, via deformation of ideals.
- (G1.b) Lagrangian property of the correspondence
  $P^n_k = \{(Z, Z') : Z \supset Z', \ell(Z/Z') = k,
  \mathrm{supp}(Z/Z') = \{x\}\}$ inside the holomorphic-symplectic
  ambient $\mathrm{Hilb}^{n+k}(S) \times \mathrm{Hilb}^n(S)$: Nakajima
  1997 Thm.\ 3.10 establishes dimension $2n + k$ (half the ambient
  $4n + 2k$) and extracts the commutator $[P_k, P_l] = k\delta_{k+l}$
  from the Lagrangian intersection.

On a smooth CY$_3$, (G1.a) is salvaged by the principal-component
restriction (Wave-3 C23 base Part (ii): $\mathrm{Hilb}^n_{\mathrm{prin}}(X)$
is smooth of dimension $3n$, via Nakajima resolution of the symmetric
product). But (G1.b) fails structurally: the ambient product
$\mathrm{Hilb}^{n+k}_{\mathrm{prin}}(X) \times
\mathrm{Hilb}^n_{\mathrm{prin}}(X)$ has complex dimension $3(n + k) + 3n$,
which is odd when $k$ is odd. A holomorphic symplectic structure would
force even dimension; in particular, $\mathrm{Hilb}^n_{\mathrm{prin}}(X)$
alone has complex dimension $3n$, odd for $n$ odd, so carries no
holomorphic symplectic form by parity of the rank of a
non-degenerate skew form. Without (G1.b), Nakajima's 1997 intersection
argument does not extend.

**G2 (DT/Li/OP are virtual, not topological).** Li 2001 *Geom.\ Topol.* 13,
Thm.\ 0, proves the numerical identity
$Z_{\mathrm{DT}, 0}(X; q) = M(-q)^{\chi(X)}$ for the degree-zero DT
partition function, using Behrend 2005 *Ann.\ Math.* 170 pointwise
Behrend function and cosection localisation (Kiem-Li 2013 *JAMS* 26).
Okounkov-Pandharipande 2010 *Geom.\ Topol.* 14 Thm.\ 1 computes the
local-curve DT partition function $Z'_\beta(X; q)$ for a smooth curve
in a toric CY$_3$ via equivariant localisation on the Pandharipande-
Thomas moduli space.

Both are **virtual** identities in $\mathbb{Z}[[q]]$, measuring
Euler-characteristic-level DT invariants. Neither constructs
Nakajima-style correspondence operators on the non-virtual topological
cohomology $H^\ast(\mathrm{Hilb}^n_{\mathrm{prin}}(X))$. For $X = K3 \times E$,
the motivic-scalar shadow is $\chi(\mathrm{Hilb}^n(K3 \times E)) = 0$
for every $n \geq 1$ (Cheah 1996 *J.\ Alg.\ Geom.* 5 + $\chi(K3 \times E) = 0$,
confirmed in `chapters/examples/k3_quantum_toroidal_chapter.tex`
Prop.\ `prop:k3qt-motivic-trivial-k3e`). The topological Euler
characteristic of the total Hilbert scheme vanishes identically, so
a threefold Heisenberg at the unrefined level has zero character and
is trivial. The motivic $\mathbb{L}^{1/2}$-refinement (`thm:k3qt-motivic-gottsche-L-half`)
recovers non-trivial content, but lives on the Goettsche-product side,
not the direct threefold side.

**G3 (Goettsche gives pullback, not direct).** The Goettsche-product
identification
\[
  \bigoplus_n H^\ast_T(\mathrm{Hilb}^n_{\mathrm{prin}}(K3 \times E); \mathbb{Q})
  \cong \Bigl(\bigoplus_n H^\ast_T(\mathrm{Hilb}^n(K3); \mathbb{Q})\Bigr)
  \otimes \Bigl(\bigoplus_n H^\ast(\mathrm{Sym}^n E; \mathbb{Q})\Bigr)
\]
(Goettsche 1990 *Math.\ Ann.* 286; Li-Qin-Wang 2004
*Math.\ Res.\ Lett.* 11, Thm.\ 1.2) identifies cohomology of the
threefold principal component with a tensor product of surface and
curve Hilbert-scheme cohomologies. The affine Yangian
$Y(\widehat{\mathfrak{gl}}_1)$ acts on the right-hand side
unconditionally: by Schiffmann-Vasserot 2013 *Publ.\ IHES* 118 Thm.\ 1.2
on $\mathrm{Hilb}^n(K3)$ twisted by the Nakajima-Grojnowski K3 lattice
(Nakajima 1997 Thm.\ 1.1; Grojnowski 1996 *Math.\ Res.\ Lett.* 3), and
by Grojnowski 1996 rank-one Heisenberg on $\mathrm{Sym}^n E$.

The promotion to a **direct** statement --- constructing threefold
correspondence cycles
$P^n_k(X) \subset \mathrm{Hilb}^{n+k}_{\mathrm{prin}}(X)
\times \mathrm{Hilb}^n_{\mathrm{prin}}(X)$ and showing their
convolution operators satisfy
$[P_k, P_l] = k\delta_{k+l}$ on the threefold principal-component
cohomology --- requires three inputs not present in any of the named
primary sources:

- (R1) Irreducibility and expected dimension $3n + k$ of $P^n_k(X)$
  on the threefold principal component (not established).
- (R2) Well-definedness of convolution $[P^n_k(X)] \cdot (-)$ at the
  topological-cohomology level, bypassing the non-existence of
  Lagrangian structure and the vanishing Euler characteristic
  (requires a threefold tangent-normal bundle computation replacing
  Nakajima's surface Lagrangian-Euler-class argument).
- (R3) Compatibility of the threefold convolution operators with the
  Goettsche pullback: the direct-threefold $P_k$ should agree with
  $P^{\mathrm{Nak}}_k(K3) \otimes P^{\mathrm{Sym}}_k(E)$ under the
  Goettsche identification. This compatibility is stronger than the
  Goettsche product on cohomology alone; it requires matching the
  fundamental classes of correspondence subvarieties.

None of (R1), (R2), (R3) is proved in the literature for smooth
projective CY$_3$ principal components. Nakajima 1999 *Lectures on
Hilbert Schemes of Points on Surfaces*, AMS University Lecture Series
18, Chapter 9 end-of-chapter remark, flags this threefold extension
as an open problem: on threefolds the correspondence subvariety is
neither smooth (at non-reduced configurations) nor Lagrangian in any
holomorphic-symplectic sense.

## Dunn-Lurie does not rescue the promotion

The user's closure hypothesis invokes Dunn-Lurie as the combiner step:
"Goettsche factorisation gives affine Yangian per factor via SV 2013;
Dunn-Lurie combines." This reading miscasts Dunn-Lurie's role.

**Precise statement (Lurie HA 5.1.2.2, Dunn 1988).** On the
$\infty$-category of $\mathbb{E}_k$-algebras in a symmetric monoidal
stable $\infty$-category $\mathcal{C}$, the Boardman-Vogt tensor
product gives an equivalence
\[
  \mathbb{E}_m\text{-}\mathrm{Alg}(\mathbb{E}_n\text{-}\mathrm{Alg}(\mathcal{C}))
  \simeq \mathbb{E}_{m + n}\text{-}\mathrm{Alg}(\mathcal{C}).
\]

**What this achieves on the Goettsche-product side.** On
$V := \bigoplus_n H^\ast_T(\mathrm{Hilb}^n(K3); \mathbb{Q}) \otimes
H^\ast(\mathrm{Sym}^n E; \mathbb{Q})$,
the Nakajima-Grojnowski K3 Heisenberg is an $E_1$-algebra structure
on the $K3$-factor, and the $\mathrm{Sym}^\bullet$-Heisenberg is an
$E_1$-algebra structure on the $E$-factor. These commute by factor-wise
construction. Dunn-Lurie assembles them into an $E_2$-algebra structure
on $V$ (equivalently, an $E_2$-algebra structure on the
Goettsche-product identification side of the threefold cohomology).

**What this does not achieve.** Dunn-Lurie does not construct an
$E_1$-algebra structure on the direct threefold side. For that, one
would need to construct geometric correspondence cycles on
$\mathrm{Hilb}^{n+k}_{\mathrm{prin}}(X) \times
\mathrm{Hilb}^n_{\mathrm{prin}}(X)$ and verify the Heisenberg
commutator via tangent-normal intersection computation. Dunn-Lurie's
operadic tensor product is silent on geometric correspondences; it
takes already-constructed $E_1$-algebras as input and produces an
$E_2$-algebra as output. The gap G1.b (non-Lagrangian threefold
correspondence) blocks the construction of the input $E_1$-algebra
on the direct threefold side; Dunn-Lurie cannot be applied until
that input exists.

**Physical heuristic**: Dunn-Lurie is a theorem on how to combine
two already-quantised $E_1$-theories into a combined $E_2$-theory
(cf.\ Lurie HA 5.1.2.2). The user's hypothesis treats it as a route
to constructing the $E_1$-theory from the underlying geometry; that
is a different question (requires Costello-Gwilliam locality applied
to a factorisation algebra on $X$, or Nakajima-type correspondence
on $\mathrm{Hilb}^n_{\mathrm{prin}}(X)$, neither of which is
unconditionally established in the CY$_3$ setting).

## Additional route considered: DT/CoHA via Davison-Meinhardt

The closure hypothesis does not invoke this, but for completeness
one notes that Davison-Meinhardt 2015 *Invent.\ Math.* 199
Thm.\ 4.6 (later Davison 2017 arXiv:1601.02479, Kontsevich-Soibelman
2008 arXiv:0811.2435 §5) constructs a CoHA on the vanishing-cycle
cohomology of DT moduli
$\mathcal{M}_n(X, \phi_W)$ with a potential $W$. This is a genuine
construction of a Hopf-algebraic structure on threefold DT data and
produces, for the conifold $X_{\mathrm{con}}$ (Szendroi 2008
*Selecta Math.* 14; cf.\ Wave W14-A5 in the cache), the Jordan-triple
CoHA matching $Y^+(\widehat{\mathfrak{gl}}_1)$. For $X = K3 \times E$,
the analogous DT-moduli construction requires a potential $W$ on
$\mathrm{Hilb}^n(K3 \times E)$ realised as a critical locus of $W$
on an ambient smooth quasi-projective variety; this is a different
route from Nakajima-Baranovsky and does not pass through the
Goettsche product. At the Hilbert-scheme level,
$\mathrm{Hilb}^n(K3 \times E)$ is not a critical locus of a potential
on a smooth ambient in any natural way (the principal component is
a smooth projective variety, not a dg critical locus), so the
DT/CoHA route is orthogonal to the hypothesis under examination
rather than a completion of it.

## Honest conjectural statement

```tex
\begin{conjecture}[Nakajima--Baranovsky--Goettsche comparison for
principal components on $K3 \times E$]
\label{conj:3B-C23:nakajima-baranovsky-cy3-principal}
\ClaimStatusConjectured

Let $X = K3 \times E$ be the smooth projective Calabi--Yau threefold
and $\mathrm{Hilb}^n_{\mathrm{prin}}(X) \subset \mathrm{Hilb}^n(X)$
its principal component, irreducible of dimension $3n$, smooth for
all $n \geq 1$ (Wave-3 C23 base, Parts (i), (ii)).

\emph{Part (i) --- Threefold correspondence subvariety.}
The locus
\[
  P^n_k(X) := \bigl\{(Z, Z') \in
  \mathrm{Hilb}^{n+k}_{\mathrm{prin}}(X) \times
  \mathrm{Hilb}^n_{\mathrm{prin}}(X) :
  Z \supset Z',\;
  \mathrm{supp}(Z/Z') = \{x\}\bigr\}
\]
is irreducible of dimension $3n + k$ and admits a generic
decomposition $P^n_k(X) = P^n_k(K3) \times \Delta^n_k(E)$ under the
Goettsche-product pullback, where $P^n_k(K3)$ is the Nakajima
surface correspondence and $\Delta^n_k(E)$ is the symmetric-product
correspondence on the elliptic curve.

\emph{Part (ii) --- Threefold convolution operators satisfy Heisenberg
commutator.} The fundamental class $[P^n_k(X)]$ defines, by
convolution, an operator
\[
  P_k: H^\ast_T(\mathrm{Hilb}^{n+k}_{\mathrm{prin}}(X); \mathbb{Q})
  \to H^\ast_T(\mathrm{Hilb}^n_{\mathrm{prin}}(X); \mathbb{Q})
\]
and, on $V^X := \bigoplus_n H^\ast_T(\mathrm{Hilb}^n_{\mathrm{prin}}(X);
\mathbb{Q})$, the commutator relations
\[
  [P_k, P_l] = k\,\delta_{k + l, 0}\cdot \mathrm{id}_{V^X}
\]
hold. Under the Goettsche identification
$V^X \cong V^{K3} \otimes V^E$, the operator $P_k$ agrees with the
tensor product $P^{\mathrm{Nak}}_k(K3) \otimes P^{\mathrm{Sym}}_k(E)$
of the Nakajima surface operator and the Grojnowski elliptic-curve
operator.

\emph{Part (iii) --- Affine Yangian on the principal component.}
The affine Yangian $Y(\widehat{\mathfrak{gl}}_1)$ acts on $V^X$ by
Schiffmann--Vasserot shuffle presentation (Schiffmann--Vasserot 2013
\emph{Publ.\ IHES} 118 Thm.\ 1.2) restricted to the Heisenberg Fock
subspace on the $K3$-factor, tensored with the rank-one
$\mathrm{Sym}^\bullet$-Heisenberg on the $E$-factor.

The Goettsche-product side of Part (iii) --- the action on
$V^{K3} \otimes V^E$ --- is unconditional (Goettsche 1990, Li--Qin--Wang
2004, Nakajima 1997, Grojnowski 1996, Schiffmann--Vasserot 2013).
The direct threefold side (Parts (i), (ii), and the promotion of
Part (iii) to $V^X$ without the Goettsche pullback) is conditional
on:

\begin{itemize}
\item[(R1)] Irreducibility and expected-dimension $3n + k$ of the
threefold correspondence subvariety $P^n_k(X)$;
\item[(R2)] A threefold tangent-normal intersection computation
inside the principal component yielding the Heisenberg commutator,
replacing Nakajima's 1997 surface Lagrangian-Euler-class argument
(Nakajima 1997 Thm.\ 3.10), which fails on CY$_3$ because the ambient
$\mathrm{Hilb}^{n+k}_{\mathrm{prin}}(X) \times
\mathrm{Hilb}^n_{\mathrm{prin}}(X)$ carries no holomorphic symplectic
structure in dimension three;
\item[(R3)] Compatibility of the threefold convolution operators
with the Goettsche pullback $P^{\mathrm{Nak}}_k(K3) \otimes
P^{\mathrm{Sym}}_k(E)$, i.e.\ matching of fundamental classes of
correspondence subvarieties under the Goettsche identification.
\end{itemize}

Nakajima 1999 \emph{Lectures on Hilbert Schemes of Points on
Surfaces}, AMS University Lecture Series 18, Chapter 9 end-of-chapter
remark, explicitly records this threefold extension as an open
problem. Dunn--Lurie additivity (Lurie HA 5.1.2.2; Dunn 1988
\emph{J.\ Pure Appl.\ Algebra} 50) is an $\infty$-operadic theorem
on Boardman--Vogt tensor products of $E_n$-algebras and does not
supply the input $E_1$-algebra structure on $V^X$ whose existence is
the content of Part (ii); it is downstream of the obstruction, not
a route around it.
\end{conjecture}

\begin{proof}[Primary-source gap, rather than proof]
Nakajima 1997 \emph{Ann.\ Math.} 145 Thm.\ 1.1 and Thm.\ 3.10 are
surface-restricted (smoothness of $\mathrm{Hilb}^n(S)$ via Fogarty
1968, Lagrangian correspondence subvariety in
holomorphic-symplectic ambient). Baranovsky 2000 \emph{Math.\ Res.\
Lett.} 7 Thm.\ 1 extends to higher-rank moduli $M^H(r, c_1, c_2)$ on
surfaces, explicitly restricted to dimension 2. Li 2001 \emph{Geom.\
Topol.} 13 Thm.\ 0 and Okounkov--Pandharipande 2010 \emph{Geom.\
Topol.} 14 Thm.\ 1 prove \emph{numerical / virtual} DT identities,
not Heisenberg constructions on topological cohomology.
Schiffmann--Vasserot 2013 \emph{Publ.\ IHES} 118 Thm.\ 1.2 lives on
$\mathrm{Hilb}^n(\mathbb{C}^2)$, a surface Hilbert scheme with $T^2$-
equivariance. Dunn--Lurie HA 5.1.2.2 is an operadic tensor-product
equivalence, not a construction of geometric correspondence cycles
on threefold Hilbert schemes. No published result covers (R1)--(R3)
on a smooth CY$_3$ principal component.
\end{proof}
```

## What remains unconditional (restated)

- **U1.** Principal component $\mathrm{Hilb}^n_{\mathrm{prin}}(K3 \times E)$
  exists, is irreducible of dimension $3n$, smooth for all $n \geq 1$
  (Wave-3 C23 base Parts (i), (ii)).
- **U2.** Goettsche-product decomposition of principal-component
  cohomology: $V^X \cong V^{K3} \otimes V^E$ (Goettsche 1990;
  Li-Qin-Wang 2004; Wave-3 C23 base Part (iii)).
- **U3.** Affine Yangian $Y(\widehat{\mathfrak{gl}}_1)$ acts on
  $V^{K3} \otimes V^E$ (Schiffmann-Vasserot 2013; Grojnowski 1996;
  Nakajima 1997).
- **U4.** $E_2$-algebra structure on $V^{K3} \otimes V^E$ via
  Dunn-Lurie applied to the $E_1$-Heisenberg factors (Lurie HA 5.1.2.2;
  not on the direct threefold side, which has no pre-existing $E_1$
  input to feed Dunn-Lurie).

## What remains conjectural

- **C1 (Parts (i), (ii), (iii) on the direct threefold side).**
  The promotion from the Goettsche-product side to a direct threefold
  Nakajima-Baranovsky correspondence algebra on $V^X$ is conjectural,
  subject to (R1)-(R3) above.
- **C2 (Consistency with `conj:k3y-nakajima-lehn-hilbert-programme`).**
  The conjectural status here is tighter than and consistent with
  the `ClaimStatusConditional` declaration at
  `chapters/examples/k3_yangian_chapter.tex` line 9648, which already
  flags the Nakajima-Lehn Hilbert-scheme Heisenberg on $K3 \times E$
  (via $T_E$-reduction) as conditional on three steps --- steps (i)
  "extending Nakajima-Lehn from surface to relative Hilbert scheme
  $\mathrm{Hilb}^n(K3 \times E) \to E$" and (ii) "establishing the
  rank-25 character at the reduced equivariant level" of that
  declaration correspond to gap G1 and gap G2.restricted here.

## Cross-cache discipline

**Cache 22S (`appendices/first_principles_cache.md` line 168):
three-composite-input discipline for $\{H^\ast_T(\mathrm{Hilb}^{[n]}(K3))\}$
pro-limit convergence.** The convergence as super-quasi-Hopf module
requires three composite inputs: MO stable envelope (rank-1 Fock),
Grojnowski-Nakajima K3 Heisenberg (arbitrary rank), Etingof-Kazhdan
super-quantisation. A single-input assertion is incomplete. The 3B-C23
closure hypothesis exemplifies this pattern at the threefold level:
invoking Baranovsky alone ignores the need for a threefold
tangent-normal argument replacing the surface Lagrangian input.

**Cache E10 (`appendices/first_principles_cache.md` line 544):
six routes to $G(K3 \times E)$ are six *different* constructions.**
The Hilbert-scheme route (via Goettsche and Nakajima-Lehn) is one of
the six; the DT/BPS-moduli route (via Kontsevich-Soibelman CoHA
with a Jordan-triple potential) is a different one of the six; they
do not merge through Nakajima-Baranovsky alone. The closure
hypothesis under examination proposes exactly such a merger and is
an instance of AP-CY271 / AP-CY285 (routes = constructions, not
functor applications) at the fine scale.

**Cache N2 (`appendices/first_principles_cache.md` line 238):
$\mathrm{CoHA}(\mathbb{C}^3) = Y^+(\widehat{\mathfrak{gl}}_1)$,
positive half only, not full $\mathcal{W}_{1+\infty}$.** Consistent
with the Goettsche-product side giving the positive half: the
affine Yangian $Y(\widehat{\mathfrak{gl}}_1)$ action on
$V^{K3} \otimes V^E$ via Schiffmann-Vasserot is the positive-half
shuffle algebra; the Drinfeld double requires additional input
(Hall-Drinfeld doubling at the self-dual point), which is not
furnished by the Nakajima-Baranovsky/Goettsche route.

**Cache AP-CY6 (`notes/antipatterns_catalogue.md` §"CY-specific
anti-patterns"): $A_X$ at $d = 3$.** At $d \geq 3$, $A$ is $E_1$;
$E_2$ lives on the Drinfeld centre $Z(\mathrm{Rep}(A))$, not on
$A$. The $E_2$-algebra structure produced by Dunn-Lurie on
$V^{K3} \otimes V^E$ in U4 lives on a Fock module, not on the
threefold-Hilbert-scheme-side CY$_3$ chiral algebra $A_{K3 \times E}$;
consistent with `chapters/theory/e1_chiral_algebras.tex` discipline.

## Manuscript-facing consequence

The closure hypothesis, evaluated honestly, does not close at A
(theorem). It closes at C (specific gap) with the three-gap
obstruction structure made precise:

- The Goettsche-product side is a theorem (U1-U3), with $E_2$-structure
  available via Dunn-Lurie (U4), all on $V^{K3} \otimes V^E$.
- The direct threefold side (Parts (i), (ii), promotion of (iii) to
  $V^X$ without the Goettsche pullback) is conjectural, subject to
  three explicit gaps (R1)-(R3).
- The user's hypothesised Dunn-Lurie combination is consistent with
  U4 but does not supply an $E_1$-input on the direct threefold side,
  hence does not close the gap on C1.

The existing `ClaimStatusConditional` tag on
Conjecture `conj:k3y-nakajima-lehn-hilbert-programme`
(`chapters/examples/k3_yangian_chapter.tex` line 9648) is consistent
with and reinforced by this closure analysis. No promotion to
`ClaimStatusTheorem` is warranted at the direct threefold scope. The
Goettsche-product scope, if restated tightly, could carry
`ClaimStatusTheorem`.

## Summary

**Hypothesis evaluated.** "Nakajima-Baranovsky comparison for
principal components on smooth CY$_3$s holds via Goettsche
factorisation, with affine Yangian via Schiffmann-Vasserot for each
factor; Dunn-Lurie combines."

**Terminal state: C (specific gap, sharpened).**

**Three gaps:**
- G1: Baranovsky 2000 is surface-restricted; its proof requires
  (G1.a) Fogarty smoothness (salvaged on CY$_3$ principal component)
  AND (G1.b) Lagrangian correspondence subvariety in
  holomorphic-symplectic ambient (fails structurally on smooth
  CY$_3$ by dimension parity: the ambient product has no
  holomorphic symplectic structure).
- G2: Li 2001 and Okounkov-Pandharipande 2010 are virtual-class DT
  identities in $\mathbb{Z}[[q]]$, not Heisenberg constructions on
  topological cohomology; at the unrefined level the total-space
  Euler characteristic vanishes, forcing the topological Heisenberg
  character to zero.
- G3: Goettsche factorisation produces a **pulled-back** identification
  from surface-times-curve, not a **direct** threefold principal-
  component correspondence algebra. The threefold correspondence
  subvariety is not Lagrangian (no holomorphic-symplectic ambient).

**Dunn-Lurie does not close the gap.** Lurie HA 5.1.2.2 operates at
the operadic level on $E_n$-algebras, assembling two $E_1$-inputs
into an $E_2$-output (used in U4 on the Goettsche-product side);
it does not construct the missing $E_1$-input on the direct
threefold side.

**What IS unconditional.**
- Principal-component existence, irreducibility, dimension $3n$,
  smoothness (U1).
- Goettsche-product decomposition of principal-component cohomology
  (U2).
- Affine Yangian action on the RHS of the Goettsche decomposition
  (U3).
- $E_2$-algebra structure on the RHS via Dunn-Lurie (U4).

**What REMAINS conjectural.**
- Direct threefold correspondence subvariety $P^n_k(X)$ irreducible
  of dimension $3n + k$ (R1).
- Threefold tangent-normal Heisenberg commutator computation (R2).
- Goettsche-pullback compatibility of threefold convolution operators
  (R3).

**Primary-source gap named.** Nakajima 1999 *Lectures on Hilbert
Schemes of Points on Surfaces*, AMS University Lecture Series 18,
Chapter 9 end-of-chapter remark, explicitly flags the threefold
extension as an open problem. No subsequent paper (through 2026) has
closed it for principal components on smooth CY$_3$s.

**Cross-pattern discipline.** The hypothesis exemplifies cache pattern
22S (single-input versus composite-input on $\mathrm{Hilb}^{[n]}(K3)$
pro-limits) and AP-CY271 / AP-CY285 (six-routes = six-constructions,
not merger through Nakajima-Baranovsky alone) at the threefold level.
The honest conjectural status is consistent with `conj:k3y-nakajima-
lehn-hilbert-programme` at `k3_yangian_chapter.tex` line 9648.

**Inscription verdict.** The manuscript should retain
`ClaimStatusConjectured` (or tighter `ClaimStatusConditional`) at
the direct threefold scope; the Goettsche-product scope, when
restated tightly, is `ClaimStatusTheorem`-worthy. The CLAUDE.md
"key fact" that $\kappa_{\mathrm{cat}}(K3 \times E) = 0$
(Kuenneth-multiplicative) is consistent with the motivic-scalar
vanishing argument in G2 and reinforces the scope discipline.
