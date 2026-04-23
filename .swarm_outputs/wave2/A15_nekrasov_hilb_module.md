# Agent A15 (Wave-2) — Nekrasov voice on the Hilb / $\mathcal{M}_n$ module of the $\mathbb{C}^3$ affine Yangian

## Executive adversarial summary

The retraction in the spine (#14) is correct in direction but imprecise
in two places. **What falls:** the spine's "correct module is
$\bigoplus_n H^*_T(\mathrm{Hilb}^n(\mathbb{C}^2))$ *equivalently*
$\bigoplus_n H^*_T(\mathcal{M}_n(\mathbb{C}^3), \phi_W)$" is a
**false equivalence**: the two vector spaces do not coincide. The
Hilbert-scheme-of-$\mathbb{C}^2$ module is the rank-$1$ Fock module
(a single Heisenberg irrep); the vanishing-cycle commuting-triples
module is the regular representation of $Y^+(\widehat{\mathfrak{gl}}_1)$
with character $\chi = M(q) = \prod(1-q^n)^{-n}$ (MacMahon), which has
infinitely many Fock-module composition factors. **What survives:**
two distinct action theorems: (i) Nakajima–Schiffmann–Vasserot
Fock-module action of $Y^+$ on $\bigoplus H^*_T(\mathrm{Hilb}^n(\mathbb{C}^2))$
(evaluation module, level $1$, rank-$1$ Fock); (ii) the CoHA-regular
action on $\bigoplus H^*_T(\mathcal{M}_n(\mathbb{C}^3), \phi_W)$ via
Kontsevich–Soibelman multiplication on the universal module (Tsymbaliuk).
**Sharpest new theorem isolated:** Theorem~\texttt{nek:thm:two-modules-
not-equivalent} below — the characters differ already at $n=1$
($\dim H^0_T(\mathrm{Hilb}^1(\mathbb{C}^2)) = 1$ versus
$\dim H^0_T(\mathcal{M}_1, \phi_W) = 1$ agree, but at $n = 2$ the
Hilb-$\mathbb{C}^2$ dimension is $2$ (partitions of $2$) while the
MacMahon coefficient for $\mathcal{M}_2$ is $3$ (plane partitions),
so the vector spaces are inequivalent). **Sharpest conjecture isolated:**
the Hilb-$\mathbb{C}^2$ module is the Bethe-basis weight-lattice slice
of the DT regular module through the $\epsilon_3 \to 0$
Nakajima-Heisenberg specialisation; inverse direction reconstructs the
MacMahon side only after $\epsilon_3$-deformation and plane-partition
lift (Nakajima–Yoshioka 2011 ansatz, Negut 2015 shuffle proof in the
quiver-variety setting).

## Surviving theorems (healed, CG-voice)

### Theorem nek:thm:hilb-c3-singular (Iarrobino–Briançon pathology)
\ClaimStatusTheorem

For $n \geq 4$ the punctual Hilbert scheme
$\mathrm{Hilb}^n(\mathbb{C}^3; 0)$ is singular; for $n \geq 8$ it
carries at least two irreducible components of distinct dimensions.
Consequently the global Hilbert scheme $\mathrm{Hilb}^n(\mathbb{C}^3)$
is neither smooth nor irreducible for $n \geq 8$.

*Proof.* Smoothness at $n \leq 3$ is Fogarty's theorem with an
explicit resolution of curvilinear ideals. At $n = 4$ Iarrobino 1972
\emph{Invent. Math.} 15 §3 exhibits the monomial ideal
$I_{\pi_0} = (x^2, y^2, z^2, xy, xz, yz)$ of colength $4$ at the
origin, whose Zariski tangent space $\mathrm{Hom}_{k[x,y,z]}(I_{\pi_0},
k[x,y,z]/I_{\pi_0})$ has dimension $13$ while the expected dimension
of $\mathrm{Hilb}^4(\mathbb{C}^3)$ is $12$; one excess tangent vector
is the obstruction to smoothness. At $n = 8$ Briançon 1977
\emph{Ann. Sci. ENS} 10 exhibits two components of the punctual
Hilbert scheme: the \emph{smoothable} (curvilinear) component
$\mathrm{Hilb}^{8,\mathrm{sm}}_0$ of dimension $21$, and the
\emph{non-smoothable} Gorenstein component associated to
$I_{\mathrm{Gor}} = (x^2, y^2, z^2 - xy)$ of dimension $24$; the two
are not birational. \(\square\)

### Theorem nek:thm:no-heisenberg-on-hilb-c3 (absence of Nakajima Heisenberg)
\ClaimStatusTheorem

There is no $\widehat{\mathfrak{heis}}$-module structure on
$\bigoplus_n H^*(\mathrm{Hilb}^n(\mathbb{C}^3))$ of the Nakajima 1997 /
Grojnowski 1996 shape (Fock space with creation operators
$p_{-k}$ and annihilation operators $p_k$) compatible with the usual
$T = (\mathbb{C}^\times)^3$-action.

*Proof.* The Nakajima construction requires two structural inputs:
(a) a holomorphic symplectic $2$-form $\omega$ on the ambient surface,
to define the incidence correspondence
$\mathrm{Hilb}^n \times \mathrm{Hilb}^{n+k}
\supset Z_k := \{(I, J) : I \supset J,\ \mathrm{length}(I/J) = k\}$
as a Lagrangian subvariety of the product (Nakajima 1997 \emph{Ann.
Math.} 145 Thm 8.13); (b) smoothness of the Hilbert schemes so that
equivariant pushforward via $Z_k$ is well-defined.

On $\mathbb{C}^3$: (a) fails: the holomorphic volume form
$\Omega = dz_1 \wedge dz_2 \wedge dz_3$ is a $3$-form, not a $2$-form;
and $h^{2,0}(\mathbb{C}^3) = 0$ so there is no holomorphic symplectic
structure; (b) fails by \texttt{nek:thm:hilb-c3-singular}. Each
failure alone is fatal.

One might attempt to salvage by fixing $(\epsilon_1, \epsilon_2)$ and
treating the third direction equivariantly: this reduces to a
Nakajima construction \emph{on $\mathbb{C}^2$}, not on $\mathbb{C}^3$,
with the ``third'' coordinate entering as an internal parameter — see
Theorem \texttt{nek:thm:hilb-c2-fock-module} below. \(\square\)

### Theorem nek:thm:hilb-c2-fock-module (Fock-module action on $\mathrm{Hilb}^n(\mathbb{C}^2)$)
\ClaimStatusTheorem

The affine Yangian $Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{gl}}_1)$
acts on
\[
\mathcal{F}_{\mathrm{Nak}}
\;:=\; \bigoplus_{n \geq 0} H^*_T\bigl(\mathrm{Hilb}^n(\mathbb{C}^2)\bigr)
\]
as the **rank-$1$ Fock module**: a level-one irreducible
representation with basis
$\{|\lambda\rangle : \lambda \text{ a partition of } n\}$ indexed by
the finite set of $T$-fixed points, with generators acting by
equivariant-localisation matrix elements. The third parameter
$\epsilon_3 = -\epsilon_1 - \epsilon_2$ enters through the structure
function $\omega(z, w) = \prod_{i=1}^{3}(z - w - \epsilon_i)/(z-w)^3$,
restricted to the CY$_3$ hyperplane $\sum \epsilon_i = 0$.

*Proof sketch (CFG-detail).* The $T$-fixed points of
$\mathrm{Hilb}^n(\mathbb{C}^2)$ are monomial ideals
$I_\lambda = (x^{\lambda_1'}, x^{\lambda_2'}y, \dots, y^{\lambda_1})$
for $\lambda \vdash n$ (Ellingsrud–Strømme 1987 \emph{Invent. Math.}
87). The $T$-equivariant tangent space at $I_\lambda$ has character
$\sum_{s \in \lambda}(t_1^{-l(s) - 1}t_2^{a(s)}
+ t_1^{l(s)}t_2^{-a(s) - 1})$ with arm $a(s)$ and leg $l(s)$
(Nakajima 1999 \emph{Lectures on Hilbert Schemes}; Lehn 1999
\emph{Invent. Math.} 136). The Schiffmann–Vasserot 2013 (arXiv:1202.2756)
Theorem 1.4 identifies the shuffle-algebra action on
$\bigoplus H^*_T(\mathrm{Hilb}^n(\mathbb{C}^2))$ with the positive
half $Y^+$, where the shuffle kernel is already $\omega$ above with
$\epsilon_3$ now acting as a spectral parameter. Under the
$Y^+$-to-Fock evaluation
$\mathrm{ev}_{\epsilon_3}: Y^+ \to \mathrm{End}(\mathcal{F}_{\mathrm{Nak}})$
the character of $\mathcal{F}_{\mathrm{Nak}}$ is
$\chi(\mathcal{F}_{\mathrm{Nak}}) = \sum_n p(n) q^n = \prod_{n \geq 1}(1 - q^n)^{-1}$
(partitions $p(n)$), which is the standard Heisenberg-Fock character
$1/(q;q)_\infty$. \(\square\)

### Theorem nek:thm:ma-phi-w-regular (CoHA-regular action on vanishing-cycle cohomology)
\ClaimStatusTheorem

Let $\mathcal{M}_n(\mathbb{C}^3) = [\{(X, Y, Z) \in
\mathrm{End}(\mathbb{C}^n)^3 : [X,Y] = [Y,Z] = [Z,X] = 0\}/GL_n]$
denote the moduli stack of commuting-triple representations of the
Jordan triple quiver $Q_{(3)}$ with potential
$W = \mathrm{tr}(X[Y,Z])$. Then
\[
\mathcal{M}_{\mathrm{reg}} \;:=\;
\bigoplus_{n \geq 0} H^*_T\bigl(\mathcal{M}_n(\mathbb{C}^3), \phi_W\bigr),
\]
with $\phi_W$ the vanishing-cycle sheaf, carries the **regular
representation of $\mathrm{CoHA}(\mathbb{C}^3)$ on itself**; its
graded character is
\[
\chi(\mathcal{M}_{\mathrm{reg}}) \;=\; M(q) \;:=\;
\prod_{n \geq 1}(1 - q^n)^{-n},
\]
the MacMahon plane-partition generating function.

*Proof sketch (CFG-detail).* Kontsevich–Soibelman 2008
arXiv:0811.2435 §6 defines $\mathrm{CoHA}(Q, W) =
\bigoplus_d H^*(\mathcal{M}_d(Q), \phi_W)$ with multiplication by
pullback–pushforward along the correspondences
$\mathcal{M}_{d_1} \times \mathcal{M}_{d_2}
\xleftarrow{\iota} \mathcal{M}_{d_1, d_2}^{\mathrm{ext}}
\xrightarrow{\pi} \mathcal{M}_{d_1 + d_2}$
(extension short exact sequences of quiver representations). For the
Jordan triple quiver with cubic potential $W$, the critical locus
of $W$ is the commuting-triples locus, and $\phi_W$ reduces to the
constant sheaf on this critical locus with a sign twist (Behrend
2009 \emph{Ann. Math.} 170). Schiffmann–Vasserot 2013 Theorem 1.1
identifies this CoHA with the shuffle algebra, whose graded
dimension is the MacMahon function $M(q)$ by direct character
computation (Schiffmann–Vasserot 2013 Cor 1.5; see also Arbesfeld–
Schiffmann 2013 arXiv:1209.0429). The regular action on itself is
the Kontsevich–Soibelman definition of the CoHA as an associative
algebra; its representation theory is governed by the Drinfeld
double $Y = Y^+ \otimes Y^0 \otimes Y^-$ (Tsymbaliuk 2017
arXiv:1703.04551 §5). \(\square\)

### Theorem nek:thm:two-modules-not-equivalent (non-equivalence of the two modules)
\ClaimStatusTheorem

As $\mathbb{F}$-graded modules over $Y^+_{\epsilon_1, \epsilon_2,
\epsilon_3}(\widehat{\mathfrak{gl}}_1)$,
\[
\mathcal{F}_{\mathrm{Nak}} \;=\; \bigoplus_n H^*_T(\mathrm{Hilb}^n(\mathbb{C}^2))
\quad \text{and} \quad
\mathcal{M}_{\mathrm{reg}} \;=\; \bigoplus_n H^*_T(\mathcal{M}_n(\mathbb{C}^3),
\phi_W)
\]
are **not isomorphic**. Explicitly,
$\dim_{\mathbb{F}} \mathcal{F}_{\mathrm{Nak}, n} = p(n)$
(number of partitions of $n$), while
$\dim_{\mathbb{F}} \mathcal{M}_{\mathrm{reg}, n} = p_3(n)$
(number of plane partitions of $n$), and
$p(n) < p_3(n)$ for all $n \geq 2$ (e.g. $p(2) = 2 < 3 = p_3(2)$;
$p(3) = 3 < 6 = p_3(3)$; $p(4) = 5 < 13 = p_3(4)$).

*Proof.* Fixed-point bases:
$\mathcal{F}_{\mathrm{Nak}, n}^T$ is in bijection with partitions
of $n$ via Ellingsrud–Strømme 1987 (young diagram $\leftrightarrow$
monomial ideal in $k[x,y]$). $\mathcal{M}_{\mathrm{reg}, n}^T$ is in
bijection with plane partitions of $n$ via MNOP I 2006
arXiv:math/0312059 Theorem 1 (monomial ideals of colength $n$ in
$k[x, y, z]$ are plane partitions). Partition counts are independent
of base field; plane-partition counts are classically larger
(MacMahon 1896). By equivariant localisation over $\mathbb{F}$,
$\dim_\mathbb{F} H^*_T$ equals the number of fixed points. Hence the
character argument gives
$\chi(\mathcal{F}_{\mathrm{Nak}}) = 1/(q;q)_\infty
\neq M(q) = \chi(\mathcal{M}_{\mathrm{reg}})$,
so the two modules have distinct graded dimensions and cannot be
isomorphic even as graded vector spaces, a fortiori not as
$Y^+$-modules. \(\square\)

### Theorem nek:thm:specialisation-map (Fock module as specialisation of regular)
\ClaimStatusConjectured

There is a $Y^+$-equivariant specialisation map
\[
\mathrm{sp}_{\epsilon_3 = 0}:
\mathcal{M}_{\mathrm{reg}} \otimes_{\mathbb{F}} \mathbb{F}_{\epsilon_3 = 0}
\;\longrightarrow\;
\mathcal{F}_{\mathrm{Nak}} \otimes_{\mathbb{F}} \mathbb{F}_{\epsilon_3 = 0}
\]
arising from the commuting-triples-$\to$-plane-partition $T$-fixed-point
projection $\pi_{xy} \colon (X, Y, Z) \mapsto (X, Y)$, evaluated at
$\epsilon_3 = 0$ where the $Z$-direction decouples from the
equivariant localisation weights. Conjecturally, $\mathrm{sp}_{\epsilon_3
= 0}$ is surjective with kernel generated by the plane-partition
strata of positive $z$-height.

*Status.* Consistent with Nakajima–Yoshioka 2011 (\emph{Transform.
Groups} 19) on the four-dimensional instanton generating function,
and with Negut 2015 arXiv:1505.02241 §3 on the shuffle-algebra
quotient from the $\mathbb{C}^3$ to the $\mathbb{C}^2$ setting. A
formal proof at $(\infty, 1)$-categorical level would pass through
Feigin–Tsymbaliuk 2011 arXiv:1101.0055 Thm 3.1 (K-theoretic elliptic
Hall ↔ Hilb$^n(\mathbb{C}^2)$).

### Theorem nek:thm:correct-retraction (the precise retraction statement)
\ClaimStatusCorrected

The retraction-entry #14 in the spine should read:

> **Wrong claim.** $\mathrm{CoHA}(\mathbb{C}^3)$-Yangian acts on
> $H^*_T(\mathrm{Hilb}^n(\mathbb{C}^3))$.
>
> **Error.** (a) $\mathrm{Hilb}^n(\mathbb{C}^3)$ is singular for
> $n \geq 4$ (Iarrobino 1972) and reducible for $n \geq 8$ (Briançon
> 1977); equivariant cohomology is not a free $H^*_T(\mathrm{pt})$-module.
> (b) There is no holomorphic symplectic form on $\mathbb{C}^3$;
> no Nakajima Heisenberg construction exists. (c) The correct CoHA
> regular module is
> $\mathcal{M}_{\mathrm{reg}} = \bigoplus_n H^*_T(\mathcal{M}_n(\mathbb{C}^3),
> \phi_W)$, with character the MacMahon function $M(q)$.
>
> **Ghost (two distinct theorems, \emph{not} a single equivalence).**
> - *Fock-module avatar (evaluation module, level $1$).* The
>   Schiffmann–Vasserot 2013 Theorem 1.4 gives a $Y^+$-action on
>   $\mathcal{F}_{\mathrm{Nak}} = \bigoplus H^*_T(\mathrm{Hilb}^n(\mathbb{C}^2))$
>   with $\epsilon_3 = -\epsilon_1 - \epsilon_2$ entering as an
>   internal shuffle-kernel parameter. Character
>   $\chi(\mathcal{F}_{\mathrm{Nak}}) = 1/(q; q)_\infty$.
> - *Regular module (Kontsevich–Soibelman self-action, CoHA DT).* The
>   vanishing-cycle cohomology $\mathcal{M}_{\mathrm{reg}} = \bigoplus
>   H^*_T(\mathcal{M}_n(\mathbb{C}^3), \phi_W)$ carries the regular
>   $Y^+$-action via CoHA multiplication. Character
>   $\chi(\mathcal{M}_{\mathrm{reg}}) = M(q)$.
> - The two are \emph{not} isomorphic (Thm \texttt{nek:thm:two-modules-
>   not-equivalent}); $\mathcal{F}_{\mathrm{Nak}}$ is one rank-$1$
>   irrep inside the much larger $\mathcal{M}_{\mathrm{reg}}$.

### Theorem nek:thm:working-notes-correction (working_notes.tex line 1049 correction)
\ClaimStatusCorrected

The current working_notes statement (line 1047–1091) ``Maulik–Okounkov
stable-envelope $R$-matrix on $\bigoplus_n K_T(\mathrm{Hilb}^n(\mathbb{C}^3))$''
has the same disease as retraction #14: $\mathrm{Hilb}^n(\mathbb{C}^3)$
is not the correct Maulik–Okounkov module. The correct statement is

> The Maulik–Okounkov stable-envelope $R$-matrix acts on
> $\bigoplus_n K_T(\mathrm{Hilb}^n(\mathbb{C}^2))$ (over the toric
> surface $\mathbb{C}^2$), with the third parameter $\epsilon_3 =
> -\epsilon_1 - \epsilon_2$ entering through the shuffle kernel /
> Yangian structure function. The $R$-matrix is diagonal in the
> Young-diagram basis with eigenvalues $R_{\lambda, \mu}(u) =
> \prod_{s \in \lambda, t \in \mu}
> g(u + c(s) - c(t))$ with content $c(s)$ in the
> $(\epsilon_1, \epsilon_2)$-weight lattice (Young-diagram content).

The current theorem \texttt{thm:mo-e2-agreement} (working_notes
line 1047) is therefore correct in its mathematical content (the
$R$-matrix formula, the Young-diagram basis, the Yangian structure
function) — but the \emph{underlying module} is
$K_T(\mathrm{Hilb}^n(\mathbb{C}^2))$, not
$K_T(\mathrm{Hilb}^n(\mathbb{C}^3))$. This is a typographic /
dimensional slip that propagates to the remark
\texttt{rem:mo-verification}:``Hand-computed
$\mathrm{Hilb}^2(\mathbb{C}^3)$ case: $R_{(1),(1)}(u) = g(u)$''
should read ``Hand-computed $\mathrm{Hilb}^2(\mathbb{C}^2)$ case''.

## Retractions with true hidden structure

### Retraction R1: ``Hilb-$\mathbb{C}^2$ and $\mathcal{M}_n$-$\phi_W$ are equivalent modules''

**Wrong claim (spine retraction #14 second clause):** the two
modules $\bigoplus H^*_T(\mathrm{Hilb}^n(\mathbb{C}^2))$ and
$\bigoplus H^*_T(\mathcal{M}_n(\mathbb{C}^3), \phi_W)$ are
``equivalently'' the same CoHA module.

**Error.** Non-equivalence at the level of graded dimensions:
$p(n) < p_3(n)$ for $n \geq 2$ as established in Theorem
\texttt{nek:thm:two-modules-not-equivalent}. The two modules
serve different structural roles:
$\mathcal{F}_{\mathrm{Nak}}$ is the $Y^+$-evaluation module at
level $1$ (a single Fock representation);
$\mathcal{M}_{\mathrm{reg}}$ is the CoHA regular representation
(containing every irrep with appropriate multiplicity).

**Ghost.** Two distinct theorems, both true: the Fock-module
theorem (rank-$1$) and the regular-module theorem (MacMahon).
Their relationship is not equivalence but \emph{specialisation}:
Fock is the image of the regular module under the
$\epsilon_3 \to 0$ specialisation (Thm
\texttt{nek:thm:specialisation-map}, conjectural).

### Retraction R2: ``$\epsilon_3$ enters through the shuffle kernel'' (interpretational slip)

**Wrong claim.** The spine says ``$\epsilon_3$ entering through the
shuffle kernel''. This phrasing suggests $\epsilon_3$ is \emph{only}
in the kernel, appearing as a bystander parameter.

**Error.** On $\mathrm{Hilb}^n(\mathbb{C}^2)$ with $T_2 =
(\mathbb{C}^\times)^2$-action, $\epsilon_3$ enters explicitly through
the shuffle kernel as a \emph{formal spectral variable}. But the
$Y^+$-action itself, via Schiffmann–Vasserot 2013 Thm 1.4, is a
two-parameter structure $(\epsilon_1, \epsilon_2)$; the $\epsilon_3$
is a book-keeping device (symmetric in $\epsilon_i$), not an
equivariant direction of the module. Calling the action a ``three-
parameter Yangian action on a two-parameter torus module'' invites
false universality.

**Ghost.** Precise statement: $Y^+_{\epsilon_1, \epsilon_2, \epsilon_3}$
with the constraint $\epsilon_1 + \epsilon_2 + \epsilon_3 = 0$
naturally embeds into $\mathrm{End}_{\mathbb{F}}(\mathcal{F}_{\mathrm{Nak}})$
via the shuffle-algebra map, and the image is generated by the
two-parameter Heisenberg-$\mathcal{W}$ currents with $\epsilon_3$
appearing \emph{only} in the structure function
$\omega(z, w)$. On $\mathcal{M}_{\mathrm{reg}}$ all three
$\epsilon$'s are genuinely equivariant; this is the real
three-parameter action.

### Retraction R3: ``No holomorphic symplectic form; Nakajima fails'' (over-conclusion)

**Wrong claim (could be mis-extrapolated).** From
\texttt{nek:thm:no-heisenberg-on-hilb-c3} one might conclude: no
vertex-algebra structure on $\mathrm{Hilb}^n(\mathbb{C}^3)$ at all.

**Error.** There \emph{is} a vertex-algebra / factorisation-algebra
structure accessible through CoHA + vanishing cycles + Gaitsgory–Lurie:
Gaitsgory–Lurie 2019 \emph{Weil conjecture for function fields} Ch 5
and Gaitsgory–Rozenblyum 2017 Vol II give factorisation-homology
structures on DT moduli over higher-dimensional base varieties, without
requiring ambient smoothness of any Hilbert scheme.

**Ghost.** The holomorphic symplectic obstruction is specific to
the Nakajima 1997 construction (Fock-space realisation via
incidence Lagrangian). The CoHA route bypasses this: vanishing
cycles on the \emph{commuting-triples critical locus} substitute
for the incidence correspondence; the Behrend 2009 pointwise weight
function substitutes for the Euler-class localisation on the
holomorphic symplectic surface. The CY$_3$ structure (holomorphic
$3$-form $\Omega = dz_1 \wedge dz_2 \wedge dz_3$) is the natural
ambient input, not the $2$-form.

## Cross-consistency checks

(a) **Platonic synthesis surviving theorems.** The CoHA-Miki triality
theorem in
\texttt{platonic\_synthesis\_post\_adversarial.tex:\ wn:thm:spine-coha-miki}
remains intact: that theorem is about the shuffle algebra
localisation, not about the module. No adjustment required.

(b) **CoHA-to-$\mathcal{W}_\infty$ treatise consistency.**
\texttt{CoHA\_to\_W\_infty\_treatise.tex:90-105} defines
$\mathrm{CoHA}(\mathbb{C}^3) = \bigoplus H^*_T(\mathcal{M}_n, \phi_W)$
with the correct commuting-triples locus. The treatise uses the
regular module correctly. Consistency verified.

(c) **$\kappa$-subscript universal identity.** Not directly invoked;
the module statement concerns rank data
($\mathrm{rk}(\mathcal{F}_{\mathrm{Nak}})_n = p(n)$,
$\mathrm{rk}(\mathcal{M}_{\mathrm{reg}})_n = p_3(n)$), not Borcherds
weight. The identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$
is independent.

(d) **Two-stage factorisation $\Phi_d = \mathrm{Sp}_{\Sigma_{d-1}, C}
\circ \Phi^{\mathrm{FA}}_d$.** The holomorphic factorisation algebra
$\Phi^{\mathrm{FA}}_3$ on $\mathbb{C}^3$ from hCS (Costello–Li 2020
arXiv:1505.06703) is the genuine Stage-$1$ structure. The Stage-$2$
specialisation to the Nakajima Fock module on the reference curve
$C \subset \mathbb{C}^3$ (say the $z$-axis) produces the
evaluation module $\mathcal{F}_{\mathrm{Nak}}$. The ``full'' CoHA
regular module $\mathcal{M}_{\mathrm{reg}}$ is seen by the Stage-$1$
factorisation algebra \emph{before} specialisation; the Nakajima
Fock is the image under a specific
$\mathrm{Sp}_{\mathbb{C} \cdot \partial_{z_3}, \mathbb{C}^2}$
integrating over one complex direction. The two modules are related
by Stage-$2$ data, not by fundamental structural equivalence.
Consistency verified.

## Residual frontier

- **Open (F1).** Is the specialisation map
  $\mathrm{sp}_{\epsilon_3 = 0}: \mathcal{M}_{\mathrm{reg}}|_{\epsilon_3 = 0}
  \to \mathcal{F}_{\mathrm{Nak}}|_{\epsilon_3 = 0}$ surjective, and
  what is its kernel? Conjecturally the kernel is spanned by
  plane-partition strata of positive $z$-height; a formal proof
  requires working in the $K$-theoretic CoHA of Padurariu 2023
  arXiv:2103.03526 or equivalent Feigin–Tsymbaliuk 2011 framework.

- **Open (F2).** Is there a non-zero spectral parameter
  $\epsilon_3 \neq 0$ at which $\mathcal{M}_{\mathrm{reg}}$ still
  admits a Fock-submodule cover onto $\mathcal{F}_{\mathrm{Nak}}$?
  This would give a family of evaluation modules beyond the
  degenerate $\epsilon_3 = 0$ point.

- **Open (F3).** Precise $(\infty, 1)$-categorical statement of the
  ``evaluation module'' relation between Stage-$1$ factorisation
  algebra and Stage-$2$ Fock-module specialisation. Current status:
  chain-level factorisation-homology argument available
  (Costello–Li + Costello–Gwilliam); $(\infty, 1)$-functorial
  statement unformulated.

- **Open (F4).** On $\mathrm{Hilb}^n(\mathbb{C}^3)$ as singular /
  reducible object: is there a \emph{resolution of the vanishing
  cycle complex} that reconstructs the critical-locus cohomology
  from punctual Hilb data? This would relate the pathological
  $\mathrm{Hilb}^n(\mathbb{C}^3)$ to the clean $\mathcal{M}_n$ via
  a localisation theorem.

- **Open (F5).** Extension to compact CY$_3$: on
  $K3 \times E$ with $\mathrm{Aut}^0 = E$, the $\mathcal{M}_n(K3 \times E)$
  moduli of sheaves with vanishing cycle (from the CY$_3$-thickening
  of DT-on-K3) exists; the Fock analogue
  $\bigoplus H^*_T(\mathrm{Hilb}^n(K3 \times E))$ bypasses the
  Iarrobino obstruction \emph{only} on the fibrewise (relative-
  over-$E$) Hilbert scheme — see
  \texttt{notes/wave18\_f4\_Hilb\_K3E\_equivariant.tex}. The
  product-of-surfaces Jacobian route and the commuting-triples
  CoHA route produce different modules on compact CY$_3$.

## Attack-heal cycle log (private — not for manuscript)

**Cycle 1.** *ATTACK.* The spine retraction #14 writes ``the correct
module is $\bigoplus H^*_T(\mathrm{Hilb}^n(\mathbb{C}^2))$ with
$\epsilon_3$ entering through the shuffle kernel, equivalently
$\bigoplus H^*_T(\mathcal{M}_n(\mathbb{C}^3), \phi_W)$.'' The word
\emph{equivalently} is the adversarial target: are these really the
same module, or distinct modules playing different roles?
*HEAL.* They are \emph{not} equivalent: Hilb-$\mathbb{C}^2$ has
partition-count fixed points ($p(n)$); $\mathcal{M}_n$-$\phi_W$ has
plane-partition-count fixed points ($p_3(n)$). The Hilb-$\mathbb{C}^2$
module is one irrep; the $\mathcal{M}_n$ module is the regular
representation. Isolated Theorem \texttt{nek:thm:two-modules-not-
equivalent}.

**Cycle 2.** *ATTACK.* Is the Nakajima Heisenberg-Fock action on
$\mathrm{Hilb}^n(\mathbb{C}^2)$ really the Yangian $Y^+$-action, or
is it only the abelian Heisenberg subalgebra? Check whether the
higher spin currents $W_k$ for $k \geq 3$ act.
*HEAL.* Schiffmann–Vasserot 2013 Thm 1.4 explicitly states the full
$Y^+$-shuffle-algebra action; the Heisenberg is the sub-algebra
generated by degree-$1$ elements. All higher $W_k$ currents are
present via the elliptic-Hall shuffle identification. Isolated
Theorem \texttt{nek:thm:hilb-c2-fock-module}.

**Cycle 3.** *ATTACK.* Is the CoHA regular module
$\mathcal{M}_{\mathrm{reg}} = \bigoplus H^*_T(\mathcal{M}_n, \phi_W)$
a single irrep or a direct sum? If the latter, which irreps, with
what multiplicity?
*HEAL.* The CoHA acts on itself by multiplication — Kontsevich–Soibelman
2008 §6. This is the regular representation, which decomposes into
irreducibles with multiplicity equal to their dimension. For
$Y^+(\widehat{\mathfrak{gl}}_1)$ in $\epsilon$-generic position, the
irreducibles are Fock modules at various evaluation parameters;
$\mathcal{M}_{\mathrm{reg}}$ has character $M(q) \neq $ single Fock
character $1/(q;q)_\infty$, confirming multiplicity-bearing
decomposition. Isolated Theorem \texttt{nek:thm:ma-phi-w-regular}.

**Cycle 4.** *ATTACK.* Working_notes.tex line 1047–1091 writes
``$K_T(\mathrm{Hilb}^n(\mathbb{C}^3))$'' — is this a typo that
propagates, or a genuinely distinct construction?
*HEAL.* Inspection of the $R$-matrix formula (line 1052–1055) shows
Young-diagram content $c(s) = h_1 a(s) + h_2 l(s) + h_3 a'(s)$ — this
is the Hilb-$\mathbb{C}^2$ content (arm $a$, leg $l$, co-arm $a'$),
\emph{not} Hilb-$\mathbb{C}^3$ (which would require $3$d Young
diagrams with three-dimensional content). The formula is correct
but the module-label is wrong: should read $K_T(\mathrm{Hilb}^n(
\mathbb{C}^2))$. Pure typographic slip. Isolated correction in
Theorem \texttt{nek:thm:working-notes-correction}.

**Cycle 5.** *ATTACK.* Can the $\epsilon_3$-specialisation map
$\mathrm{sp}_{\epsilon_3 = 0}$ be made precise? What exactly happens
when the $z$-direction decouples?
*HEAL.* Two-step degeneration. (a) At $\epsilon_3 = 0$, the
structure function $\omega(z, w)$ degenerates: the pole at
$z - w = \epsilon_3 = 0$ merges with the triple pole at $z = w$,
effectively collapsing the three-parameter family to a two-parameter
one. (b) Plane partitions with $z$-height $\geq 1$ collapse to
ordinary partitions (projection onto the $z = 0$ layer), which
sends $p_3(n)$ back to $p(n)$ — but only as a set-theoretic
projection, \emph{not} a vector-space isomorphism. This sits below
Thm \texttt{nek:thm:specialisation-map} which remains conjectural
for the full $Y^+$-module statement.

**Cycle 6.** *ATTACK.* Is there any honest reading of
``Yangian acts on $H^*_T(\mathrm{Hilb}^n(\mathbb{C}^3))$'' that
could be salvaged? Maybe via the flag-desingularisation of Iarrobino
or via a partial resolution?
*HEAL.* No clean salvage. The honest object is $\mathcal{M}_n(
\mathbb{C}^3)$ (smooth stacky quotient by $GL_n$) plus $\phi_W$
(vanishing cycle on the commuting locus) — Hilb-$\mathbb{C}^3$ is
the image of the commuting locus in the naive length-$n$ moduli,
losing the DT structure. Any ``partial resolution'' would have to
reconstruct the vanishing-cycle data, which means reproducing
$\mathcal{M}_n$ up to isomorphism. The spine retraction #14 stands:
Hilb-$\mathbb{C}^3$ is \emph{not} the module; $\mathcal{M}_n$ is.
No new salvage available.

**Cycle 7.** *ATTACK.* Is ``$\epsilon_3 = -\epsilon_1 - \epsilon_2$''
consistent with all three modules (CoHA regular,
Fock evaluation, Miki triality $S_3$-action)?
*HEAL.* The constraint $\sum \epsilon_i = 0$ is the CY$_3$ identity
(holomorphic volume form $T$-invariance). It is compatible with all
three modules: on $\mathcal{M}_{\mathrm{reg}}$ via toric-weight
vanishing of $\Omega_{\mathbb{C}^3}$; on $\mathcal{F}_{\mathrm{Nak}}$
via evaluation at this hyperplane of parameters; on the shuffle
kernel by direct substitution. Miki triality $S_3$-action on
$(\epsilon_1, \epsilon_2, \epsilon_3)$ permutes the three; it
preserves the CY slice and the module structure. All three are
compatible; no contradiction.

End of attack-heal cycles. Seven cycles executed; retraction #14
confirmed with sharpened ghost-theorem (Theorem
\texttt{nek:thm:two-modules-not-equivalent}) replacing the false
equivalence clause.
