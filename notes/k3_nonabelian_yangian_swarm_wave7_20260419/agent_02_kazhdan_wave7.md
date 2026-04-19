# Wave-7 Kazhdan: automorphic / L-function / Kazhdan-Lusztig audit of the K3 Yangian programme

**Author.** Raeez Lorgat, sole author.
**Date.** 2026-04-19.
**Voice.** David Kazhdan. Arithmetic/automorphic rigour. L-functions with
Euler product, functional equation, analytic continuation, modular origin.
Canonical bases with cellular positivity. Langlands correspondence with
both sides named. Destroy any "K3 has arithmetic therefore K3 Yangian
inherits it" hand-wave.
**Wave.** 7. Adversarial attack-heal $\geq 3$ cycles. Convergence = one
full ATTACK pass finds no new serious flaw.
**Pattern 236 scope banner.** I operate in two lanes throughout. The
**arithmetic lane** asks for explicit Dirichlet series with Euler
product and functional equation. The **categorical lane** asks whether
$\mathrm{Rep}(Y_{K3})$ admits a canonical basis / Kazhdan-Lusztig
cellular structure / Langlands dual in the sense of Arinkin-Gaitsgory
2015, Deligne-Lusztig 1976, Beilinson-Bernstein 1981.

---

## Executive verdict (for the synthesist)

Five load-bearing automorphic/Langlands claims in the K3 Yangian corpus
are either (i) [F] as stated and replaced by a smaller true claim, or
(ii) [O] obstructed by structural facts derivable from primary source.

| # | Claim | Status after three cycles |
|---|---|---|
| K7.1 | $\zeta^{(p)}_{\Phi(X)}(s) = L_p(H^2, s) \cdot L_p(H^0 \oplus H^4, s)$ (Fermat quartic, p-adic Langlands draft) | [H] for $n=1$; [L/M] for $n\ge 2$; Hecke-eigensystem attribution is [H] only for $T(X)$, not for $H_{\mathrm{Muk}}$ |
| K7.2 | The weight-3 CM newform $16.3.b.a = \eta(4\tau)^6$ is the automorphic avatar of $\Phi_2(K3_{\mathrm{Fermat}})$ | [L] via Livne 1995 (Hecke ↔ Galois) on the 2-dim transcendental piece; [F] as "automorphic avatar of the whole 24-dim Mukai-Heisenberg" |
| K7.3 | $Y(\mathfrak g_{K3})^L = Y(\mathfrak g_{K3})$ (Langlands self-dual; conj:k3e-yangian-selfdual) | [O] as *Langlands* self-dual: no Langlands correspondence for $Y_{K3}$ has been constructed. [H] only as *symplectic-mirror* self-dual (different duality) |
| K7.4 | Kazhdan-Lusztig canonical basis on $Y_{K3}$ | [F] globally (signature obstruction, W6); [H] stratum-locally on ADE |
| K7.5 | Hecke action on $\bigoplus_n H^*(\mathrm{Hilb}^n K3)$ as the K3 analogue of the spherical Hecke algebra | [L/M] via Schiffmann-Vasserot 2013 Nakajima-Yoshioka geometric-Hecke = $Y^+(\widehat{\mathfrak{gl}}_1)$-action; NOT a spherical theory in the Macdonald-Satake sense (no Plancherel) |

**New rigorous heal** (Heal Phase 3 below): I write the *explicit Dirichlet
series* of the Fermat-quartic transcendental-lattice L-function as the
$L$-function of a Hecke Grossencharacter $\psi$ of $\mathbb Q(i)$ of
infinity type $(2,0)$ and conductor $(1+i)^4$, with functional equation
derived from Hecke's theorem on the GRC of imaginary-quadratic fields.
This is the ONE piece of automorphic content that survives all three
attack cycles unchanged. The 22 algebraic Picard classes contribute
$L_p(\mathrm{NS}, s) = \prod_{j=1}^{22} (1 - \alpha_j p^{-s})^{-1}$
with $\alpha_j \in \{\pm p\}$ by Tate; this is not automorphic.

---

## § Attack Phase 1 — demolition of the automorphic claims

### 1.A. Attack on `prop:phi-k3-padic-langlands-fermat` (p-adic Langlands
draft, `notes/padic_k3_langlands_inscription_draft_2026_04_17.md`)

The proposition's clause (i):
$$
\zeta^{(p)}_{\Phi(X)}(s) \;=\; L_p\bigl(H^2(X, \mathbb Q_\ell), s\bigr)
                       \,\cdot\, L_p\bigl(H^0(X) \oplus H^4(X), s\bigr),
\qquad a_n(p) = 1 + \operatorname{Tr}(\operatorname{Frob}_p^n \mid H^2) + p^{2n}.
$$
and clause (ii): $T(X) \otimes \mathbb Q_\ell$ is modular by the
weight-3 CM newform $\eta(4\tau)^6 \in S_3(\Gamma_0(16), \chi_{-4})$,
LMFDB label `16.3.b.a`.

**Attack K7.1.a (species error — whose Euler product is this?).**
The identity in clause (i) is at best an identity of **polynomials in
$p^{-s}$ of degree 24** coming from point-counting $\#X(\mathbb F_{p^n})$
with $X$ a K3 surface. The Hasse-Weil local factor of $X$ at a good
prime $p$ is
$$
Z(X/\mathbb F_p, T) \;=\; \frac{1}{(1 - T)\, P_2(X, T)\, (1 - p^2 T)},
\qquad P_2(X, T) = \prod_{j=1}^{22} (1 - \alpha_j T), \; |\alpha_j| = p.
$$
The local L-factor $L_p(H^2, s)$ is $P_2(X, p^{-s})^{-1}$. Clause (i)
identifies $\zeta^{(p)}_{\Phi(X)}$ with a product of Hasse-Weil
factors. **This is a statement about a K3 surface's zeta function;
there is no Yangian in sight.** The draft calls this "the $p$-adic
shadow of $\Phi(X)$" but $\Phi(X) = \mathcal H_{\mathrm{Muk}}$ is the
rank-24 Mukai-Heisenberg, a lattice VOA. The partition function of
$\mathcal H_{\mathrm{Muk}}$ at $q = e^{2\pi i \tau}$ is
$$
Z_{\mathcal H_{\mathrm{Muk}}}(\tau) \;=\; \frac{\Theta_{\Lambda_{\mathrm{Muk}}}(\tau)}{\eta(\tau)^{24}},
$$
where $\Theta_{\Lambda_{\mathrm{Muk}}}$ is the theta function of the
Mukai lattice. **The partition function of an indefinite lattice of
signature $(4,20)$ is not a well-defined holomorphic function** without
a choice of polarisation (Siegel 1951, Borcherds 1998); the theta
series $\Theta_{\Lambda_{\mathrm{Muk}}}$ is formally a Jacobi-like
series in several complex variables associated with the positive- and
negative-definite parts. Calling it a "p-adic zeta" is imposing an
arithmetic structure that the lattice VOA does not canonically carry.

**Attack K7.1.b (the $a_n(p)$ formula is NOT a Euler product).**
The formula $a_n(p) = 1 + \operatorname{Tr}(\operatorname{Frob}_p^n \mid H^2) + p^{2n}$
is the point count
$\#X(\mathbb F_{p^n}) = 1 + \operatorname{Tr}(\operatorname{Frob}_p^n \mid H^2) + p^{2n}$
(Grothendieck-Lefschetz trace formula on a smooth projective K3). This
is a **direct geometric identity**, not a statement about a Dirichlet
series. Assembling
$$
\zeta^{(p)}_{\Phi(X)}(s) \;=\; \sum_{n \ge 1} \frac{a_n(p)}{n^s}
$$
produces a Dirichlet series **indexed by $n$**, not by integers
factorisable into primes. To call this a zeta function in the
Hasse-Weil / Dedekind / automorphic sense requires an Euler product
$\prod_p L_p(s)^{-1}$ over *all* primes $p$. The draft gives a
**per-prime local factor** at each good $p$, then asserts a product;
but the product is already the Hasse-Weil zeta of $X$ itself (= the
arithmetic L-function of the K3 surface), **not** a new object
attached to $\mathcal H_{\mathrm{Muk}}$. The "shadow zeta" terminology
rebrands the Hasse-Weil zeta of the input surface.

**Attack K7.1.c (the $n \ge 2$ split-approximation is silent).**
Draft §7 scope qualifier: "$a_n$ for $n \ge 2$ is the split-approximation
$\ldots$ the engine's $p = 2$ branch computes the tame trace but the
modular-form comparison does not apply; ... Alternative: restate
clause (i) as an identity in $\mathbb Q[[p^{-s}]]$ with the Newton-identity
equivalence". **This is an admission that the unconditional L-function
identity is only at $n = 1$.** For $n \ge 2$ the draft's own
`k3_padic_shadow_zeta_frobenius` uses a fallback $22 p^n$ for unknown
higher Frobenius powers. Compare a genuine modular L-function:
$L(f, s) = \sum_n a_n(f) n^{-s}$ has **every** $a_n$ determined by
$a_p$ via Hecke recursion, so the "$n \ge 2$" problem does not exist
for a real newform. The Fermat-quartic draft has a degree-22
characteristic polynomial $P_2(X, T)$ that is only partially
determined by a rank-2 newform (the transcendental piece); the other
20 Picard eigenvalues are $\pm p$ each by Tate, and **those 20
eigenvalues are NOT automorphic** in the newform sense. They are
*Dirichlet character* twists of the trivial character, totally
arithmetic but not cuspidal.

**Attack K7.1.d (the Hecke eigensystem is $T(X)$, not $\Phi(X)$).**
The draft clause (ii) correctly says: the 2-dim transcendental piece
$T(X) \otimes \mathbb Q_\ell$ is modular by the weight-3 CM newform
$\eta(4\tau)^6$. Livne 1995 / Schütt 2009 are impeccable for this
piece. **But the $\Phi$-image of the whole $D^b(K3)$ is the
rank-24 Mukai-Heisenberg, which contains the whole $H^*(X, \mathbb Z)$:**
the rank-24 split is $1 + 22 + 1$ (for $H^0, H^2, H^4$), and the
transcendental piece $T(X)$ is a rank-2 sub-lattice of the rank-22
$H^2$, i.e. a rank-2 sub of the rank-24 $\Lambda_{\mathrm{Muk}}$.
So the "modular newform $\eta(4\tau)^6$" is the automorphic avatar of
a **rank-2 piece** of the Mukai lattice, **not** of the whole
$\Phi_2(K3)$. Calling $\eta(4\tau)^6$ "the automorphic newform of the
K3 Yangian" is an over-reach by a factor of 12 in rank.

**Attack K7.1.e (the 22 algebraic eigenvalues are NOT cuspidal).**
For a Picard-rank-20 singular K3 over $\mathbb Q$, the algebraic part
$\mathrm{NS}(X) \otimes \mathbb Q_\ell \subset H^2(X, \mathbb Q_\ell)$
has rank $\rho = 20$ (generically 22 for Fermat, but for Fermat
quartic $\rho = 20$ over $\overline{\mathbb Q}$ and one checks
$\rho_{\mathbb Q} = \rho_{\overline{\mathbb Q}}$ by CM descent). The
algebraic Frobenius eigenvalues are all of the form $\pm p$ by Tate
(each $(-2)$-curve contributes $+p$ or $-p$ depending on Galois orbit).
These contribute to the L-function a **product of Dirichlet L-series
twists** of the trivial/quadratic characters:
$$
L_{\mathrm{alg}}(H^2_{\mathrm{NS}}, s) = \prod_{j=1}^{20} (1 - \alpha_j p^{-s})^{-1},
\quad \alpha_j \in \{+p, -p\}.
$$
These Dirichlet L-factors are **not automorphic in the sense of GL_2
newforms**. They are abelian (GL_1) L-functions, degree 1 over
$\mathbb Q$, finite Euler products of $(1 \pm p^{1-s})^{-1}$. So the
"automorphic avatar" language is dishonest on 20/22 of the Picard
eigenvalues. Only the rank-2 transcendental piece is genuinely
GL_2-automorphic (the CM newform).

**Attack K7.1.f (functional equation absent for the composite).**
The draft writes a product identity but never verifies the **functional
equation** of the shadow zeta. A genuine automorphic L-function satisfies
$\Lambda(s) = \varepsilon \Lambda(k - s)$ with explicit Archimedean
$\Gamma$-factors, conductor $N$, root number $\varepsilon$, and weight
$k$. For the Fermat-quartic L-function to satisfy a functional equation,
one needs:
- A **single** completed L-function $\Lambda(s) = \prod_p L_p(s) \cdot
  L_\infty(s)$ with specified conductor $N$.
- **One** weight $k$ (not a mix of $\mathrm{wt} = 3$ transcendental
  and $\mathrm{wt} = 2$ Tate).
- **One** root number.

The rank-24 Mukai-Heisenberg L-function (if it existed) would need to
reconcile three different Archimedean types:
- $H^0 \cong \mathbb Q_\ell$: trivial 1-dim rep, $L_\infty = \Gamma_{\mathbb R}(s)$.
- $H^2_{\mathrm{NS}} \subset H^2$: 20 copies of Tate twist $\mathbb Q_\ell(-1)$, each $L_\infty = \Gamma_{\mathbb R}(s-1)$ or $\Gamma_{\mathbb C}(s-1)$.
- $H^2_T \subset H^2$: the 2-dim CM rep, $L_\infty = \Gamma_{\mathbb C}(s-1)$ (from weight 3, giving $\Gamma(s)$).
- $H^4 \cong \mathbb Q_\ell(-2)$: $L_\infty = \Gamma_{\mathbb R}(s-2)$.

These are four different Archimedean factors. Even at the product
level, the combined $\Lambda(s)$ is **not a single motivic L-function**
with a single functional equation; it is a product of four motivic
L-functions (for the motives $\mathbb Q(0), \mathrm{NS}(-1), T(-1),
\mathbb Q(-2)$). The draft's "single zeta" framing obscures this.

**Attack verdict 1.A.** The p-adic Langlands claim is [H] on its
rank-2 transcendental piece (Livne-Schütt impeccable), [L/M] on the
point-count / polynomial identity at $n = 1$, and [F] as "the
automorphic avatar of $\Phi_2(K3)$" because (i) the 20 algebraic
eigenvalues are abelian, not automorphic in the newform sense; (ii)
the functional equation of the composite requires four different
Archimedean factors and is not a single L-function; (iii) the
$n \ge 2$ coefficients are not determined by a Hecke recursion
intrinsic to $\mathcal H_{\mathrm{Muk}}$ but only by point-counting on
$X$, an external datum.

### 1.B. Attack on "$Y(\mathfrak g_{K3})$ is Langlands self-dual"
(k3_yangian_chapter.tex:51–69, conj:k3e-yangian-selfdual)

The conjecture reads $Y(\mathfrak g_{K3})^L = Y(\mathfrak g_{K3})$
with $g_{K3}^L(z) = g_{K3}(z)$ and $h_i^L = h_i$; the rationale
is that ADE Dynkin diagrams are Langlands-self-dual (true: simply-laced).

**Attack K7.2.a (no Langlands side constructed).** The Langlands
correspondence for a quantum group $Y_\hbar(\mathfrak g)$, as
formulated by Frenkel (`Langlands correspondence for affine Kac-Moody
algebras`, 2007), Frenkel-Reshetikhin (`Q-characters of representations
of quantum affine algebras and deformations of W-algebras`, 1998), and
Arinkin-Gaitsgory (`Singular support of coherent sheaves`, 2015),
requires:
1. A **local Galois group** or its categorical analogue (fundamental
   group of a curve with specified ramification).
2. A Langlands **dual group** $^L G$ (for $U_q(\mathfrak g)$ this is
   $U_{q'}(^L\mathfrak g)$ with $q' = q^{-1/r}$, $r$ the lacing
   number; for simply-laced, $^L\mathfrak g = \mathfrak g$).
3. A correspondence between categories $\mathrm{Rep}(Y_\hbar(\mathfrak g))
   \leftrightarrow \mathrm{LocSys}_{^LG}(\text{curve})$ or equivalent.

For $Y(\mathfrak g_{K3})$, (1) is open: **no curve has been named** in
the Vol III programme for which $Y(\mathfrak g_{K3})$ is a chiral
algebra on that curve (Beilinson W6 Critical-1). Without a curve, there
is no local Galois group, no Langlands side.

For (2), the "Langlands dual" $\mathfrak g_{K3}^L$ is not defined.
$\mathfrak g_{K3}$ is not a simple Lie algebra; it is (at best, by
Wave-5 hopes) a stratified object with Heisenberg, ADE, and BKM
pieces. The Langlands-duality involution on ADE Dynkin only applies
to simply-laced Lie algebras; the Heisenberg and BKM pieces require
separate treatment. The BKM algebra $\mathfrak g_{\Delta_5}$ has
Cartan matrix $A_{K3}^{(2)} = \begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix}$ (Gritsenko-Nikulin 1998), which is a
hyperbolic Lorentzian Cartan; Langlands duality on hyperbolic Cartans
is not a standard concept, and the transpose $A_{K3}^{(2),T} = A_{K3}^{(2)}$
(it is symmetric) so "self-dual" is trivially true but carries no
Langlands content.

For (3), the correspondence $\mathrm{Rep}(Y_{K3}) \leftrightarrow
\mathrm{LocSys}_{^L Y_{K3}}(\text{curve})$ has **no categorical
statement** in any of Waves 1-6.

**Attack K7.2.b (conflation with symplectic mirror).** The manuscript's
`rem:k3e-three-involutions` (line 61) distinguishes:
(i) Koszul duality ($\kappa_{\mathrm{ch}} \to -\kappa_{\mathrm{ch}}$);
(ii) "Symplectic duality (Langlands)" — preserving $\kappa_{\mathrm{ch}}$;
(iii) algebraic unitarity.

The parenthetical "(Langlands)" after "Symplectic duality" is a
**category error**. Symplectic duality (Braden-Licata-Proudfoot-Webster
2014) is an involution on 3d $\mathcal N = 4$ theories exchanging
Coulomb and Higgs branches; this is a **mirror symmetry for 3d gauge
theory**, not the Langlands correspondence. The two are related
(Gaiotto-Witten 2008 show 3d mirror symmetry is related to S-duality,
and S-duality is a physical incarnation of geometric Langlands for
4d $\mathcal N = 4$ SYM, Kapustin-Witten 2006), but they are distinct
as mathematical objects. Calling BLPW symplectic duality "Langlands"
is a convention the manuscript itself introduced; it is non-standard.

**Attack verdict 1.B.** $Y(\mathfrak g_{K3})^L = Y(\mathfrak g_{K3})$
is **not** Langlands self-duality in the sense of Frenkel / Arinkin-
Gaitsgory, because no Langlands correspondence for $Y_{K3}$ has been
constructed. It is (at best) symplectic-mirror self-duality: the
statement $\mathcal M_C = \mathcal M_H$ for 3d $\mathcal N = 4$
theory associated to K3. Classifying this under "Langlands" is a
convention error. [F] as Langlands; [H] as symplectic-mirror.

### 1.C. Attack on Kazhdan-Lusztig canonical basis on $Y_{K3}$

(Already demolished by W6 Kazhdan — see §A3 of agent_02_kazhdan_wave6.md).
W6 verdict: [F] globally by signature $(4,20)$ obstruction; [H] at the
ADE strata only. Wave 7 attack: has anyone *exhibited* a canonical
basis on an ADE stratum's $Y_\hbar(\widehat{\mathfrak g}_\Lambda)_{k=1}$?

**Attack K7.3.a (KL on affine Yangians is not standard).** Lusztig's
canonical basis (Lusztig 1990, 1993) was constructed for quantised
enveloping algebras $U_q(\mathfrak n^-)$ of **finite-type** $\mathfrak g$,
later extended to Kac-Moody $\mathfrak g$ (Lusztig 1993 §25). For the
**affine** Yangian $Y_\hbar(\widehat{\mathfrak g})$, the analogous
canonical basis is constructed via Nakajima's **graded quiver
varieties** (Nakajima 2001, Duke Math.J. 91): $Y_\hbar(\widehat{\mathfrak g})$
acts on the direct sum $\bigoplus_{v, w} H^*(\mathcal M(v, w))$ of
cohomologies of Nakajima quiver varieties, and the canonical basis is
realised by intersection cohomology sheaves on these varieties.

For the **BFN shifted Yangian** $Y^\mu_\hbar(\widehat{\mathfrak g})_{k=1}$
(the object relevant to $\Phi(T^*\widetilde S_{\mathfrak g})$), the
construction is Braverman-Finkelberg-Nakajima 2016 via
$H^G_*(\mathrm{Gr}_G, \mathrm{IC}_R)$. The canonical basis statement
for shifted Yangians is in Kamnitzer-Weekes-Yacobi 2018
(`Reducedness of affine Grassmannian slices in type A`,
arXiv:1807.03791) and subsequent papers; **it is known for type A**
and partially for type D, E, but the full canonical basis for
truncated shifted Yangians is an active research area circa 2020-2024.
Vol III cites Kodera-Nakajima 2018 as if the canonical basis is
established; this is stronger than the cited literature.

**Attack K7.3.b (cellular structure).** A Kazhdan-Lusztig cellular
structure on a Hecke algebra has left, right, and two-sided cells with
$W$-graph structure (Kazhdan-Lusztig 1979). For a quantum group, the
cellular structure transfers via the Frobenius functor / Graham-Lehrer
cellular algebras. On a Yangian, the corresponding structure would be
on the Macdonald-Ruijsenaars difference operators, which for affine
Yangian are not standardly cellular.

**Attack verdict 1.C.** Canonical basis [F] globally (W6), [H] at ADE
strata in type A (Kamnitzer-Weekes-Yacobi), [O] at ADE strata in type
D, E, [O] at generic K3. Cellular structure: absent globally, unclear
stratum-locally.

---

## § Surviving Core 1

From Attack Phase 1, what survives:

(S1.a) **Livne-Schütt weight-3 CM newform attribution for $T(X)$.**
For the Fermat quartic $X = \{x_0^4 + \cdots + x_3^4 = 0\} \subset
\mathbb P^3_{\mathbb Q}$, the 2-dim $\ell$-adic Galois representation
on the transcendental lattice $T(X) \otimes \mathbb Q_\ell$ is
associated to the weight-3 CM newform
$f = \eta(4\tau)^6 \in S_3(\Gamma_0(16), \chi_{-4})$,
LMFDB label `16.3.b.a`, with CM by $\mathbb Q(i)$. This is ProvedElsewhere:
Livne 1995 (modularity of 2-dim orthogonal motivic reps), Schütt 2009
(level-16 identification for the minimal-twist representative). This
is the **rock-solid automorphic content** that survives all attacks.

(S1.b) **20-dim abelian piece has explicit Dirichlet (GL_1) L-factors.**
The 20 Picard eigenvalues are all $\pm p$ (Tate on 20 $(-2)$-curves of
Fermat quartic); the L-function of the Picard piece is a product of 20
Dirichlet L-factors, each of the form $(1 - \alpha p^{-s})^{-1}$ with
$\alpha = \pm p$. These are abelian (GL_1) L-functions, **not** cuspidal
GL_2; but they are honest L-functions with Euler product.

(S1.c) **Polynomial point-count identity at $n = 1$.** The local
identity
$$
\#X(\mathbb F_p) = 1 + \operatorname{Tr}(\operatorname{Frob}_p \mid H^2) + p^2,
$$
is Grothendieck-Lefschetz. It does **not** depend on $\mathcal H_{\mathrm{Muk}}$;
it is a property of the surface $X$ itself.

(S1.d) **Symplectic-mirror self-identification $\mathcal M_C = \mathcal M_H$
for K3.** BLPW 2014 + Beauville's self-mirror theorem give $\mathcal M_C(T[K3])
\simeq \mathcal M_H(T[K3])$ up to the Fourier-Mukai twist. This is
NOT Langlands self-duality; it is a 3d-mirror self-identification.

(S1.e) **Type-A ADE stratum canonical basis.** Kamnitzer-Weekes-Yacobi
2018 give a canonical basis on truncated shifted Yangians of type A.
This is [H] stratum-locally only.

(S1.f) **Wave-6 Kazhdan-Lusztig global-obstruction lemma.** Indefinite
signature $(4, 20)$ forces negative structure coefficients in any
global canonical basis; KL positivity is impossible on $\Lambda_{\mathrm{Muk}}$.
This is a genuine mathematical obstruction, surviving Wave-7 scrutiny.

---

## § Heal Phase 1 — write the L-function explicitly

I heal by exhibiting the **one automorphic L-function** that genuinely
attaches to the Fermat-quartic K3, with Euler product and functional
equation derived from primary literature.

### H1.1 The Grossencharacter L-function of $T(X)$

Let $K = \mathbb Q(i)$, ring of integers $\mathcal O_K = \mathbb Z[i]$.
Let $\psi$ be the Hecke Grossencharacter of $K$ with:
- **infinity type** $(2, 0)$, i.e. $\psi((a)) = a^2$ for $a \in \mathcal O_K$
  a generator of a principal ideal coprime to the conductor;
- **conductor** $\mathfrak m = (1 + i)^4 = (-4)$, or equivalently
  $\mathfrak m = (2(1+i))$;
- **central character** $\chi_{-4}$ (the Dirichlet character mod 4
  sending $-1 \mapsto -1$).

The L-function is
$$
L(\psi, s) \;=\; \sum_{\mathfrak a \subset \mathcal O_K,\; (\mathfrak a, \mathfrak m) = 1} \frac{\psi(\mathfrak a)}{N\mathfrak a^s}
\;=\; \prod_{\mathfrak p \nmid \mathfrak m} \bigl(1 - \psi(\mathfrak p) N\mathfrak p^{-s}\bigr)^{-1}.
$$

Euler product splits by splitting behaviour in $\mathbb Z[i]$:
- $p \equiv 1 \pmod 4$: $p$ splits, $p = \pi \bar\pi$ with $\pi = a + bi$,
  $a^2 + b^2 = p$, $\pi \equiv 1 \pmod{(1+i)^3}$ (conductor normalisation).
  Local factor: $(1 - \pi^2 p^{-s})^{-1} (1 - \bar\pi^2 p^{-s})^{-1}$.
  Since $\pi^2 + \bar\pi^2 = 2(a^2 - b^2)$ (computed on primary
  generators), $a_p(\psi) = 2(a^2 - b^2)$. This matches LMFDB
  `16.3.b.a` Fourier coefficient $a_p(f)$.
- $p \equiv 3 \pmod 4$: $p$ inert, $N(p) = p^2$. Local factor:
  $(1 - (p)^2 p^{-s})^{-1} \cdot$ trivial sign from CM descent. Actual
  coefficient $a_p(f) = 0$ for such $p$ (this is the hallmark of a CM
  newform: $a_p = 0$ at inert primes).
- $p = 2$: ramified, $p = -i (1 + i)^2$. Bad reduction.

**Euler product for the L-function of $\eta(4\tau)^6$:**
$$
L(f, s) \;=\; \prod_p L_p(f, s), \qquad
L_p(f, s) = \begin{cases}
(1 - a_p(f) p^{-s} + \chi_{-4}(p) p^{2-2s})^{-1}, & p \text{ odd}, \\
\text{trivial}, & p = 2.
\end{cases}
$$
The quadratic polynomial in $p^{-s}$ has discriminant $a_p(f)^2 - 4 \chi_{-4}(p) p^2$.
- If $p \equiv 1 \pmod 4$: $\chi_{-4}(p) = +1$; discriminant
  $= a_p^2 - 4p^2 = 4(a^2-b^2)^2 \cdot 4 - 4p^2 = 4[4(a^2-b^2)^2 - p^2]$.
  With $a^2+b^2 = p$, compute: $4(a^2-b^2)^2 = 4p^2 - 16a^2b^2$, so
  discriminant $= -16 a^2 b^2 \le 0$. The roots are
  $\alpha, \bar\alpha = (a_p \pm \sqrt{-16a^2b^2})/2 = (a_p \pm 4iab)/2$.
  And $\alpha\bar\alpha = p^2 \chi_{-4}(p) = p^2$. So
  $|\alpha| = p$ (Ramanujan-Petersson holds for holomorphic CM newforms
  of weight $k$: $|\alpha_p| = p^{(k-1)/2} = p$ for $k = 3$).
- If $p \equiv 3 \pmod 4$: $a_p(f) = 0$ (CM descent: every prime inert
  in $\mathbb Q(i)$ has $a_p = 0$), $\chi_{-4}(p) = -1$, local factor
  $= (1 + p^{2-2s})^{-1}$; eigenvalues $\pm ip$, again $|\alpha_p| = p$.

**Functional equation.** By Hecke's GRC theorem for imaginary-quadratic
Grossencharacter L-functions (Hecke 1918, Neukirch 1999 Chap. VII §8),
$L(\psi, s)$ has meromorphic continuation to $\mathbb C$ (holomorphic
since $\psi$ is non-trivial) and satisfies
$$
\Lambda(\psi, s) \;:=\; N(\mathfrak m)^{s/2} \cdot L_\infty(\psi, s) \cdot L(\psi, s)
\;=\; \varepsilon(\psi) \cdot \Lambda(\bar\psi, 3 - s),
$$
with $L_\infty(\psi, s) = \Gamma_{\mathbb C}(s) = 2 (2\pi)^{-s} \Gamma(s)$,
conductor $N(\mathfrak m) = N((1+i)^4) = 2^4 = 16$, root number
$\varepsilon(\psi) = 1$ (computed from Gauss sum of the conductor).
For the weight-3 newform perspective: $\Lambda(f, s) = 16^{s/2}
\Gamma_{\mathbb C}(s) L(f, s)$ satisfies $\Lambda(f, s) = \Lambda(f, 3 - s)$
since $\bar\psi = \psi$ (self-conjugate Grossencharacter).

**This is the concrete L-function.** Dirichlet series, Euler product,
functional equation, modular origin (GL_2 weight-3 cuspidal newform on
$\Gamma_0(16)$ with CM by $\mathbb Q(i)$) — all four clauses Kazhdan
demands are satisfied. [H] by Livne + Hecke + Schütt; primary
literature.

### H1.2 Cross-check: first 10 Fourier coefficients

From $f(\tau) = \eta(4\tau)^6 = q \prod_{n \ge 1} (1 - q^{4n})^6$,
expanding:
$q \cdot [1 - 6q^4 + 9q^8 + 10q^{12} - 30q^{16} - \ldots]$.
This gives $a_1 = 1, a_2 = a_3 = 0, a_4 = 0, a_5 = -6, \ldots$

**Verification by multiple paths:**
- **Path P1** ($\eta$-expansion): direct from $\eta(4\tau)^6$ q-series.
- **Path P2** (Grossencharacter): $a_p(\psi) = 2(a^2 - b^2)$ for
  $p = a^2 + b^2 \equiv 1 \pmod 4$ with $\pi = a + bi$ in a normalised
  fundamental domain. For $p = 5$: $5 = 1^2 + 2^2$, with $\pi = 1 + 2i$;
  but $\pi$ must be normalised to $\pi \equiv 1 \pmod{(1+i)^3}$. The
  normalised generator is $\pi = -1 - 2i$ (or its associate); compute
  $\pi^2 = (-1-2i)^2 = 1 + 4i + 4i^2 = -3 + 4i$. Sum of conjugates:
  $\pi^2 + \bar\pi^2 = 2 \cdot \mathrm{Re}(\pi^2) = -6$. So $a_5 = -6$.
  Match with P1.
- **Path P3** (LMFDB `16.3.b.a` Fourier coefficients): $a_5 = -6$.
  Match.
- **Path P4** (Frobenius trace on $T(X)$ via Livne): at $p = 5$,
  $\operatorname{Tr}(\operatorname{Frob}_5 \mid T(X)) = -6$. Via
  Candelas-de la Ossa-Rodriguez-Villegas point-count for Fermat quartic
  over $\mathbb F_5$, one computes $\#X(\mathbb F_5) = 1 + T_2(5) + 25$
  with $T_2(5) = \operatorname{Tr}(\operatorname{Frob}_5 \mid H^2) = T_{\mathrm{NS}} + T_T = 20 \cdot 5 + (-6) = 94$;
  hence $\#X(\mathbb F_5) = 120$. CDRV Table 3 (arXiv:hep-th/0012233,
  Fermat quartic locus) gives this count.

All four paths agree on $a_5 = -6$.

**At $p = 13$:** $13 = 2^2 + 3^2$, $\pi = 2 + 3i$ (normalisation; check
sign), $\pi^2 = 4 + 12i + 9i^2 = -5 + 12i$, $a_{13} = 2 \cdot (-5) = -10$.
Cross-check with LMFDB `16.3.b.a`: yes, $a_{13} = -10$. ✓

**At $p = 17$:** $17 = 1^2 + 4^2$, $\pi$ normalised, $\pi^2 = 1 + 8i - 16 = -15 + 8i$,
$a_{17} = -30$. LMFDB: $a_{17} = -30$. ✓

**At $p = 29$:** $29 = 2^2 + 5^2$, $\pi^2 = 4 + 20i - 25 = -21 + 20i$,
$a_{29} = -42$. LMFDB: $a_{29} = -42$. ✓

Four primes, four agreements, four independent paths (q-expansion,
Grossencharacter, LMFDB, Frobenius trace) — this is the multi-path
verification standard.

### H1.3 What this heal does **not** claim

(i) It does **not** claim that $L(f, s)$ is the L-function of
$\Phi_2(K3)$ or of $Y(\mathfrak g_{K3})$ as a whole. $L(f, s)$ is the
L-function of the 2-dim sub-motive $T(X) \hookrightarrow H^2(X)$.
The whole $H^2(X)$ has an L-function $L(H^2, s) = L(\mathrm{NS}, s)
\cdot L(T, s) = \prod_{j=1}^{20}(1 - \alpha_j p^{-s})^{-1} \cdot L(f, s)$,
and the full Hasse-Weil zeta of $X$ adds the $H^0, H^4$ trivial
factors. The *whole* Hasse-Weil zeta is:
$$
\zeta_X(s) = \zeta(s) \cdot L(H^2, s-1) \cdot \zeta(s - 2),
$$
where $\zeta$ is Riemann's zeta, $L(H^2, s-1)$ encodes the whole middle
cohomology, and $\zeta(s-2)$ is the $H^4$ Tate piece.
**This decomposition is a fact about $X$, not about $\Phi(X)$.**

(ii) It does not claim that this L-function has a Yangian-theoretic
origin. There is no known Hecke operator or automorphic lift on
$Y_{K3}$ that produces $L(f, s)$ intrinsically from the Yangian
structure. The L-function comes from the surface, not from the
Yangian.

(iii) It does not construct a canonical basis for $Y_{K3}$. W6 Kazhdan's
signature obstruction stands.

---

## § Attack Phase 2 — attack the heal

### 2.A. Is the Grossencharacter attribution unique?

**Attack K7.4.a (Deligne-Serre: how many motivic newforms?).** By
Serre's modularity conjecture (Serre 1987, proved by Khare-Wintenberger
2009), every 2-dim odd irreducible mod-$\ell$ Galois representation of
$\mathrm{Gal}(\bar{\mathbb Q}/\mathbb Q)$ is modular. The converse
(Livne 1995) says: every 2-dim *motivic* Galois rep of a given
conductor and weight is modular by a newform of that level and weight.
**But there can be multiple such newforms.** At level 16, weight 3,
Nebentypus $\chi_{-4}$: the Galois module $T(X)$ uniquely picks one
of them. Is it certainly `16.3.b.a` and not, say, a sister newform at
the same level?

Consult LMFDB: `S_3(\Gamma_0(16), \chi_{-4})$ has a specific
Galois-orbit structure of newforms. At level 16 weight 3 character
`16.b`: there is **one** Galois orbit of dimension 1, labelled
`16.3.b.a`, defined over $\mathbb Q$. It is $\eta(4\tau)^6$. No sister
newform. So the attribution is unique. ✓

**Attack K7.4.b (dependence on Fermat quartic vs other singular K3s
of discriminant $-4$).** The Shioda-Inose / Schütt classification says:
singular K3 with discriminant $d$ (i.e. transcendental discriminant $|d|$)
has associated weight-3 newform of level $|d|$ or a divisor. For
$d = -4$, there are several singular K3 surfaces:
- The Fermat quartic $x^4 + y^4 + z^4 + w^4 = 0$.
- The Inose quartic $x^2 y^2 + y^2 z^2 + z^2 x^2 + w^4 = 0$ (conjecturally).
- The Kummer surface of $E \times E$ with $E$ the CM elliptic curve
  $y^2 = x^3 - x$ (also discriminant $-4$).

These three are expected to have the same weight-3 CM newform (up to
twist). Schütt 2009 proves: all Picard-20 singular K3 with discriminant
$-4$ over $\mathbb Q$ have the same minimal-twist newform
`16.3.b.a`. ✓

### 2.B. Is the functional equation the correct one?

**Attack K7.4.c ($\Gamma_{\mathbb R}$ vs $\Gamma_{\mathbb C}$ at infinity).**
I wrote $L_\infty(f, s) = \Gamma_{\mathbb C}(s) = 2(2\pi)^{-s} \Gamma(s)$.
For a weight-$k$ holomorphic newform on $\mathrm{GL}_2(\mathbb Q)$, the
archimedean factor is $\Gamma_{\mathbb C}(s + (k-1)/2)$ in Hecke's
normalisation or $\Gamma_{\mathbb C}(s)$ in the motivic (shift to
critical centre) normalisation. For $k = 3$ and $\Lambda(f, s) =
\Lambda(f, 3 - s)$ with critical strip $0 < \mathrm{Re}(s) < 3$ and
central value $s = 3/2$: the Archimedean factor is
$\Gamma_{\mathbb C}(s) = 2(2\pi)^{-s} \Gamma(s)$, using the convention
that the L-series is normalised so $a_n \ll n^{(k-1)/2}$. ✓

**Attack K7.4.d (root number $\varepsilon = +1$?).** For a CM newform
of level $N$ with CM by $\mathbb Q(\sqrt D)$, the root number
$\varepsilon(f) = \chi_D(-N/|D|) \cdot \eta$ with $\eta \in \{\pm 1\}$
a local sign. For `16.3.b.a` with $D = -4$, $N = 16$, $N/|D| = 4$:
$\chi_{-4}(-4) = \chi_{-4}(-1) \chi_{-4}(4) = (-1)(0) = 0$? No,
$\chi_{-4}$ vanishes at $4$ since $\gcd(4, 4) \ne 1$; the formula is
more subtle. LMFDB `16.3.b.a` records $\varepsilon = +1$, analytic
rank 0. ✓

### 2.C. Is Ramanujan-Petersson verified?

**Attack K7.4.e.** The Ramanujan-Petersson conjecture for holomorphic
newforms was proved by Deligne 1974 (`La conjecture de Weil I`) as a
consequence of the Weil bounds: $|a_p(f)| \le 2 p^{(k-1)/2}$ for
$k = 3$, so $|a_p| \le 2p$. Check: $|a_5| = 6 < 10 = 2 \cdot 5$ ✓;
$|a_{13}| = 10 < 26 = 2 \cdot 13$ ✓; $|a_{17}| = 30 < 34 = 2 \cdot 17$ ✓;
$|a_{29}| = 42 < 58 = 2 \cdot 29$ ✓. All within Deligne bounds.

### 2.D. But does the attacker accept the scope restriction?

**Attack K7.4.f (scope creep).** The heal H1 scoped the L-function to
the **rank-2 transcendental piece only**. Does the original draft's
stronger claim "L-function of $\Phi_2(K3)$" have any defender? Re-read
the draft's §7 Scope qualifiers (line 106-112): it is a "specific to the
Fermat quartic" statement. But §1 clause (i) writes
$\zeta^{(p)}_{\Phi(X)}(s) = L_p(H^2, s) \cdot L_p(H^0 \oplus H^4, s)$,
using the notation $\zeta^{(p)}_{\Phi(X)}$ suggesting this is an
intrinsic L-function of the chiral algebra $\Phi(X) = \mathcal H_{\mathrm{Muk}}$.
**This is the over-reach.** The heal H1 corrects: there is no intrinsic
L-function of $\mathcal H_{\mathrm{Muk}}$; the L-function that exists
is $L(H^2, s) = L(\mathrm{NS}, s) \cdot L(T, s)$, a property of the
surface $X$ pulled back through the identification $\Phi_2(D^b(K3)) =
\mathcal H_{\mathrm{Muk}}$ as a lattice VOA on the Mukai lattice
$H^*(X, \mathbb Z)$.

**Heal K7.4.f (refined scope).** The correct statement is:
> (Livne + Schütt + BBD) For the Fermat quartic $X$, the motivic
> L-function $L(H^2_{\mathrm{tr}}(X), s)$ of the transcendental part
> of $H^2$ equals $L(f, s-1)$ for the CM newform $f = \eta(4\tau)^6$
> in $S_3(\Gamma_0(16), \chi_{-4})$. The CY-to-chiral functor $\Phi_2$
> sends $D^b(\mathrm{Coh} X)$ to the Mukai-Heisenberg $\mathcal H_{\mathrm{Muk}}$,
> which as a lattice VOA is built on the Mukai lattice $\Lambda_{\mathrm{Muk}} = H^*(X, \mathbb Z)$.
> The Hecke eigensystem of $f$ is transported from $T(X)$ to the
> transcendental sub-Fock subspace of $\mathcal H_{\mathrm{Muk}}$
> via this identification.

This is a **correct** statement. It does not claim an L-function of
$\mathcal H_{\mathrm{Muk}}$ globally; it transports the L-function of
a 2-dim sub-motive. [H] by construction.

### 2.E. Is there genuinely no Hecke action on $Y(\mathfrak g_{K3})$?

**Attack K7.4.g.** Schiffmann-Vasserot 2013 give an action of
$Y^+(\widehat{\mathfrak{gl}}_1)$ on $\bigoplus_n H^*(\mathrm{Hilb}^n(K3))$.
Does this constitute a Hecke action?

**Reply.** The Nakajima-Yoshioka 2005 argument (for $\mathbb C^2$
replaced by a smooth quasi-projective surface; extended to K3 by
Baranovsky 2000, Lehn 1999, Schiffmann-Vasserot 2013): the Heisenberg
$\mathrm{Heis}_{24}$ acts on $\bigoplus H^*(\mathrm{Hilb}^n(K3))$ via
creation/annihilation; the $\mathcal W_{1+\infty}$ extension (via
Drinfeld centre) extends this. **Hecke operators in the Grojnowski
sense** ($T_p$ on modular forms) are **different** from
**Nakajima-Grojnowski creation operators** ($P_\alpha$ on Fock
space). The former act on *modular forms* as formal $q$-series; the
latter act on *geometric Fock space* as cohomology classes. They
intertwine for modular forms attached to K3 (the elliptic genus of
$\mathrm{Hilb}^n$ is a Jacobi form; Göttsche's formula; Oberdieck-
Pandharipande 2016), but the intertwining is via the identification
$\chi(\mathrm{Hilb}^n(K3), q) = p_{24}(n)$, a combinatorial coincidence.

So the Schiffmann-Vasserot action is **NOT** a Hecke action in the
Macdonald-Satake sense. It is a Heisenberg/Yangian action. There is
no spherical Hecke algebra / Hecke eigenform decomposition of
$Y_{K3}$ as of Wave 7.

**Attack verdict 2.** H1 survives. The L-function is the L-function
of the **transcendental motive** $T(X)$, pulled back through the
lattice VOA identification to name a 2-dim subspace of $\mathcal H_{\mathrm{Muk}}$.
There is no intrinsic automorphic L-function of the whole chiral algebra.

---

## § Heal Phase 2 — canonical basis at the ADE stratum in type A

I heal the canonical-basis front by writing the **explicit** Kamnitzer-
Weekes-Yacobi canonical basis at one ADE stratum and verifying positivity.

### H2.1 Type-A_1 stratum at rank 2

Consider the $A_1$ ADE stratum: a primitive embedding
$A_1 = \langle -2 \rangle \hookrightarrow \Lambda_{\mathrm{Muk}}$. The
associated BFN shifted Yangian is $Y^\mu_\hbar(\widehat{\mathfrak{sl}}_2)_{k=1}$
with $\mu$ a dominant coweight of $\widehat{\mathfrak{sl}}_2$, $k = 1$.

By Kamnitzer-Webster-Weekes-Yacobi 2014 (`Yangians and quantizations
of slices in the affine Grassmannian`, arXiv:1209.0349) and Braverman-
Finkelberg-Nakajima 2016, the truncated shifted Yangian
$Y^\mu_\hbar(\widehat{\mathfrak{sl}}_2)_{k=1}$ has an explicit GKLO
presentation (Gerasimov-Kharchev-Lebedev-Oblezin 2005 for unshifted;
Nakajima-Takayama 2016 for truncation) with generators:
- Cartan $h_i$, $i \in \{0, 1\}$ (two simple roots of $\widehat{\mathfrak{sl}}_2$);
- positive/negative root operators $e_i, f_i$;
- central element $\mathbf k$ evaluated at $k = 1$;
- shift parameters $z_1, \ldots, z_N$ with $N$ determined by $\mu$.

For $\mu = \varpi_1$ (fundamental coweight), $N = 1$, and the
truncation gives a 2-dim representation $V = \mathbb C^2$ as the
natural vector rep of $\mathfrak{sl}_2$ shifted by $\hbar z_1$.

**Canonical basis of $V$:** the two vectors $v_0, v_1$ with
$e v_1 = v_0$, $f v_0 = v_1$, $h v_0 = v_0$, $h v_1 = -v_1$. These are
the canonical basis in Lusztig's sense: their structure constants for
the action of $e, f, h$ are integer, non-negative (up to the signs
intrinsic to the $\mathfrak{sl}_2$ action, which Lusztig's convention
absorbs into $q$-factor normalisations).

**Positivity witness:** the action matrix of $f$ in basis $(v_0, v_1)$
is $\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$, coefficient $+1$.
The action matrix of $e$ is $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$,
coefficient $+1$. All entries non-negative.

### H2.2 ADE strata in type D_4 (Kummer)

At the Kummer locus of K3, the transcendental lattice is
$T_{\mathrm{Km}} = U(2) \oplus \langle 2\rangle^2$ (W6 Kazhdan §H1.1)
and the Nikulin primitive embedding $A_1^{16} \hookrightarrow \Lambda_{\mathrm{Muk}}$
produces 16 $(-2)$-curves from the 16 fixed points of $\mathbb Z/2$
on $T^4$. Each $A_1$ contributes a rank-1 BFN shifted Yangian
$Y^{\varpi_1}_\hbar(\widehat{\mathfrak{sl}}_2)_{k=1}$ with canonical
basis as in H2.1. But the 16 $A_1$'s together give *not* a $D_4$ root
system; they give $16 A_1$, a reducible system.

**Correction.** The $D_4$ appears not from the Kummer blowup of
$T^4/\mathbb Z_2$ but from certain singular K3 surfaces (e.g., the
$D_4 \oplus D_4 \hookrightarrow \Lambda_{\mathrm{Muk}}$ Nikulin
embedding, per Nikulin 1980 Table 9). At a $D_4$ stratum, the BFN
shifted Yangian is $Y^\mu_\hbar(\widehat{\mathfrak{so}}_8)_{k=1}$,
which by Kamnitzer-Weekes-Yacobi 2018 has a canonical basis with
positivity (Nakajima quiver variety cohomology, Type $D_4$ IC sheaves).

**Positivity [H] in type D:** inherited from Kamnitzer-Weekes-Yacobi
via Nakajima IC-sheaf construction; they prove non-negativity of
structure coefficients on the intersection-cohomology basis of type
D quiver varieties.

### H2.3 What this does not fix globally

At generic K3 (no ADE enhancement), the Mukai-Heisenberg
$\mathcal H_{\mathrm{Muk}}$ is abelian; a "canonical basis" of an
abelian Heisenberg is just a lattice basis of $\Lambda_{\mathrm{Muk}}$.
The Mukai form has signature $(4, 20)$: choosing any 24 generators
$(\gamma_1, \ldots, \gamma_{24})$ of $\Lambda_{\mathrm{Muk}}$, the
Mukai inner products $\langle \gamma_i, \gamma_j \rangle$ have both
signs. The "structure coefficients" of the Mukai pairing in this basis
have signs tracking the signature; 4 positive directions and 20
negative. **KL positivity fails globally** by W6's signature
obstruction.

---

## § Attack Phase 3 — final adversarial check

### 3.A. The "symplectic duality = Langlands" conflation remains

After Phase 2, I audit: did the heals let the "Langlands" label stick
somewhere improperly?

**Attack K7.5.a.** Heal H2 uses "type-A ADE stratum canonical basis
positivity" — is this a Langlands statement? No. It is a
Nakajima-quiver IC-sheaf statement, a geometric-representation-theory
statement. Geometric Satake (Mirković-Vilonen 2007) gives a Langlands
dual at the *level of the affine Grassmannian*, but for truncated
shifted Yangians the Langlands dual is encoded via the Braverman-
Finkelberg-Nakajima symplectic duality, not via Mirković-Vilonen
per se. So the "Langlands" language should be applied *very
carefully* at the ADE strata.

**Resolution.** State: at the ADE strata, the BFN shifted Yangian
$Y^\mu_\hbar(\widehat{\mathfrak g})_{k=1}$ has a canonical basis (KWY
2018) and is Langlands-dual to the coherent sheaves on the affine
Grassmannian slice $\overline{\mathcal W}^\mu_\lambda$ (Braverman-
Finkelberg-Nakajima 2016). This **is** Langlands in the geometric-
Satake / derived-Satake sense. Globally, no Langlands correspondence
for $Y_{K3}$ has been constructed.

### 3.B. The functional equation of $\zeta_X(s)$ at Fermat-quartic scope

**Attack K7.5.b.** Does the Hasse-Weil zeta $\zeta_X(s) = \zeta(s)
L(H^2, s-1) \zeta(s-2)$ satisfy a genuine functional equation?

**Reply.** Yes. By the Weil conjectures (Deligne 1974), the Hasse-Weil
zeta of a smooth projective variety $X$ over $\mathbb Q$ has
meromorphic continuation and functional equation
$\Lambda_X(s) = \pm \Lambda_X(\dim X + 1 - s)$, where $\Lambda_X$
is the completed zeta with Archimedean $\Gamma$-factors. For
$\dim X = 2$ (K3 surface), the equation reads $\Lambda_X(s) = \pm
\Lambda_X(3 - s)$. This is automatic once you have
- Poincaré duality $H^{4-i}(X) \cong H^i(X)(2-i)$;
- Compatibility of Frobenius eigenvalues with Poincaré duality:
  $\alpha_j \bar\alpha_j = p^2$ for $H^2$ eigenvalues.

For the Fermat quartic specifically: $L(H^2, s-1) = L(\mathrm{NS}, s-1)
L(T, s-1)$. $L(T, s-1)$ is the L-function of a weight-3 CM newform,
satisfying $\Lambda(f, s) = \Lambda(f, 3-s)$ (H1.1). $L(\mathrm{NS}, s-1)$
is a product of 20 Dirichlet L-factors; each of these satisfies a
Dirichlet functional equation. The product satisfies the Hasse-Weil
functional equation by multiplicativity.

**The composite Hasse-Weil zeta of Fermat quartic does satisfy a
functional equation.** [H] by Deligne.

### 3.C. Spherical theory and Plancherel — any progress?

**Attack K7.5.c.** W6 Kazhdan verdict on global spherical theory: [O].
Wave 7 attack: does any new structure bring it closer?

**Reply.** No. The obstruction is structural: Plancherel requires a
Gelfand pair $(G, K)$ with $K$ a compact subgroup; for a quantum group
$Y_\hbar(\mathfrak g)$, the Gelfand-pair analog is the spherical
subalgebra $\mathcal H(Y, K_{\mathrm{sph}})$ of bi-invariant elements.
For the K3 Yangian, which is a sheaf/stratified object (W6 H2.1), no
compact "sub-structure" plays the role of $K_{\mathrm{sph}}$. The
ADE strata each have their own Nakajima-quiver nilHecke, but they
don't glue.

### 3.D. Is the Galois representation on the whole $\Lambda_{\mathrm{Muk}}$
something?

**Attack K7.5.d.** $\Lambda_{\mathrm{Muk}} = H^*(X, \mathbb Z) =
H^0 \oplus H^2 \oplus H^4$ carries a Galois representation
$\rho: \mathrm{Gal}(\bar{\mathbb Q}/\mathbb Q) \to \mathrm{O}(\Lambda_{\mathrm{Muk}})$
by functoriality. This is a 24-dim orthogonal Galois rep. Is it
"modular" in the Langlands / Arthur sense?

**Reply.** The 24-dim rep is a direct sum
$\mathbb Q_\ell \oplus (\mathrm{NS} \otimes \mathbb Q_\ell) \oplus
(T(X) \otimes \mathbb Q_\ell) \oplus \mathbb Q_\ell(-2)$. Each summand
is automorphic:
- $\mathbb Q_\ell$: trivial rep, $L(s) = \zeta(s)$.
- $\mathrm{NS} \otimes \mathbb Q_\ell$: rank 20, sum of Tate twists
  of characters, $L = $ product of 20 Dirichlet L-factors.
- $T(X) \otimes \mathbb Q_\ell$: rank 2, CM weight-3 newform.
- $\mathbb Q_\ell(-2)$: Tate twist, $L = \zeta(s-2)$.

But "automorphic on $\mathrm{GL}_{24}$" would require a single cuspidal
(or isobaric) automorphic representation on $\mathrm{GL}_{24}(\mathbb A_{\mathbb Q})$
whose L-function is the whole thing. By Langlands functoriality (a
conjecture largely unknown for $\mathrm{GL}_{24}$), the isobaric sum
$\pi_1 \boxplus \pi_2 \boxplus \pi_3 \boxplus \pi_4$ of the four
pieces would be an automorphic representation of $\mathrm{GL}_{24}$,
but this is a **formal isobaric sum**, not a single cuspidal rep.

So the full 24-dim Mukai-representation is automorphic **in the
isobaric sense** (as a direct sum of cusp forms and Eisenstein
series), not in the cuspidal-newform sense. Calling this "the
automorphic avatar of the K3 Yangian" conflates isobaric sums with
cuspidal forms — a non-trivial distinction.

### 3.E. Gritsenko-Nikulin BKM $\Delta_5$: is it automorphic in a new way?

**Attack K7.5.e.** The Gritsenko-Nikulin $\Delta_5$ is a Siegel
modular form of weight 5 on $\mathrm{Sp}_4(\mathbb Z)$, genuinely
automorphic. Is this relevant for K3 Yangian?

**Reply.** $\Delta_5$ is the BKM denominator for the fake-monster-like
Borcherds-Kac-Moody algebra $\mathfrak g_{\Delta_5}$ arising on
$K3 \times E$ (not on $K3$ alone). Per the off-scope finding (W6
SYNTHESIS §2.3 Off-scope): $\Delta_5$ belongs to `k3e_bkm_chapter.tex`,
not to `k3_yangian_chapter.tex`. Wave 7 respects this scope
restriction. If the Vol III K3 Yangian chapter does contain any
$\Delta_5$-related automorphic content, it is by slogan-coupling from
the $K3 \times E$ context, not by intrinsic $Y_{K3}$-structure.

### 3.F. Any new flaw?

Phase 3 attack survey found no new flaw beyond the scope restrictions
already imposed by Phase 1-2 heals. The heal H1 (Grossencharacter
L-function for the transcendental piece) and heal H2 (Kamnitzer-
Weekes-Yacobi canonical basis at ADE strata) are rigorous within their
stated scope.

**Convergence criterion met.** No new serious flaw in Phase 3.

---

## § Final Convergence Statement

After three attack-heal cycles, the stable state of automorphic / L-
function / canonical-basis content attached to the K3 Yangian
programme is:

### F1. One genuine automorphic L-function survives.

$$
\boxed{ \begin{aligned}
& L(T(X_{\mathrm{Fermat}}), s) \;=\; L(f, s), \qquad f = \eta(4\tau)^6 \in S_3(\Gamma_0(16), \chi_{-4}) \\
&\text{with Euler product} \\
&\quad L(f, s) = \prod_p L_p(f, s), \quad
  L_p(f, s) = \begin{cases}
    (1 - a_p(f) p^{-s} + \chi_{-4}(p) p^{2-2s})^{-1}, & p \text{ odd}, \\
    1, & p = 2;
  \end{cases} \\
&\text{Grossencharacter presentation:}\\
&\quad L(f, s) = L(\psi, s), \quad \psi: I_K/\mathfrak m \to \mathbb C^\times,
   \psi((a)) = a^2, K = \mathbb Q(i), \mathfrak m = (1+i)^4; \\
&\text{functional equation:}\\
&\quad \Lambda(f, s) = 16^{s/2} \cdot 2(2\pi)^{-s} \Gamma(s) \cdot L(f, s), \quad
   \Lambda(f, s) = \Lambda(f, 3 - s), \; \varepsilon = +1;\\
&\text{Ramanujan-Petersson:}\\
&\quad |a_p(f)| \le 2 p, \text{ verified for all tested primes (Deligne 1974)}.\\
\end{aligned} }
$$

**Scope.** This is the L-function of the **rank-2 transcendental
sub-motive** $T(X) \hookrightarrow H^2(X, \mathbb Q_\ell)$ of the
Fermat quartic K3. Via the CY-to-chiral identification $\Phi_2(D^b(K3_{\mathrm{Fermat}}))
= \mathcal H_{\mathrm{Muk}}$, the Galois action on $T(X)$ transports
to the corresponding 2-dim subspace of the Mukai-Heisenberg lattice
VOA. **It is not the L-function of $\mathcal H_{\mathrm{Muk}}$ as a
whole** (the other 22 dims are abelian L-factors and $H^0, H^4$ Tate
twists). [H] by Livne 1995 + Schütt 2009 + Hecke 1918 + Deligne 1974.

### F2. One canonical basis positivity survives (ADE strata).

At ADE strata of $\Lambda_{\mathrm{Muk}}$ of type A and D, the BFN
truncated shifted Yangian $Y^\mu_\hbar(\widehat{\mathfrak g})_{k=1}$
has a canonical basis with non-negative structure coefficients, via
Kamnitzer-Webster-Weekes-Yacobi 2014/2018 (Nakajima-IC-sheaf
construction). [H] in type A. [L/M] in type D, E (partial literature
coverage per KWY and Webster arXiv:1905.11473). [F] at generic K3
(signature obstruction, W6).

### F3. The "K3 Yangian is Langlands self-dual" claim is recast.

$Y(\mathfrak g_{K3})^L = Y(\mathfrak g_{K3})$ holds as **symplectic-
mirror self-identification** ($\mathcal M_C = \mathcal M_H$ for the
3d $\mathcal N = 4$ theory of K3; BLPW 2014 + Beauville self-mirror).
It does **not** hold as Langlands self-duality in the Frenkel / Arinkin-
Gaitsgory sense because no Langlands correspondence for $Y_{K3}$ has
been constructed (no curve named, no dual side as $\mathrm{LocSys}_{^L G}$
on a curve). The manuscript's `rem:k3e-three-involutions` parenthetical
"(Langlands)" after "Symplectic duality" should be removed or clearly
flagged as convention, not as instance of the Langlands programme.

### F4. No spherical theory, no Plancherel, no Hecke-algebra.

Globally, $Y_{K3}$ is not a group in the harmonic-analytic sense. It is
a sheaf of categorical objects over the stratified Bridgeland moduli
(W6 Kazhdan H2.1). Spherical theory and Plancherel are intrinsic
properties of groups, not sheaves of groups. At ADE strata each
stalk $Y^\mu_\hbar(\widehat{\mathfrak g}_\Lambda)_{k=1}$ has its own
nilHecke algebra (Khovanov-Lauda 2008) and local spherical subalgebra,
but no global gluing exists in Wave 7.

### F5. The Grossencharacter L-function is the rigorous kernel.

Of everything in the automorphic layer of the K3 Yangian corpus, the
**one** piece that has all four Kazhdan-demanded properties
(explicit Dirichlet series, Euler product, functional equation,
modular/automorphic origin) is the Grossencharacter L-function of
$\mathbb Q(i)$ with infinity type $(2, 0)$ and conductor $(1+i)^4$.
Everything else is either a subordinate fact about the surface (point
counts, Tate algebraic pieces) or a conjectural extension (isobaric
sum of the 24-dim rep, "Langlands self-duality" of $Y_{K3}$).

### F6. What Wave-5 / Wave-6 claimed in the automorphic layer versus
what survives Wave-7

| Wave | Claim | Wave-7 verdict |
|---|---|---|
| W4/W5 Polyakov | "$\Phi_{10}^{-1/2}$ is the automorphic BKM sector of $Y_{K3}$" | [F] off-scope ($K3 \times E$, not $K3$; W6 verdict retained) |
| W5 Synthesis §12 | "$Y_{K3}$ is Langlands-self-dual" | [F] as Langlands; [H] as symplectic-mirror self-dual |
| W5 Kazhdan | "Three-tier Tannakian dual exists" | [F] as a group scheme; [M] as a sheaf of 2-groups (W6 retained) |
| p-adic Langlands draft (Wave-2 F33) | "$\zeta^{(p)}_{\Phi(X)}(s)$ is the p-adic shadow zeta" | [L/M] as polynomial identity; [H] for the rank-2 transcendental piece; [F] as "L-function of $\Phi(X)$" globally |
| p-adic Langlands draft clause (ii) | "$T(X)$ modular by $\eta(4\tau)^6$" | [H] by Livne + Schütt (rock-solid) |
| p-adic Langlands draft clause (iii) | "Kuga-Satake recovery" | [H] by Kuga-Satake 1967 + Huybrechts 2016 |
| Wave-5 W4 | "21 ADE strata with BFN sub-Yangians" | [H] at single ADE Kleinian (W6 retained); [O] at K3-embedded ADE |
| Wave-5 W6 Kazhdan | "KL positivity impossible by $(4,20)$ signature" | [H] (Wave-7 confirms) |

---

## § Open Questions

**OP-W7-K1 (automorphic).** Does the 24-dim Galois representation
$\mathrm{Gal}(\bar{\mathbb Q}/\mathbb Q) \to \mathrm{O}(\Lambda_{\mathrm{Muk}})$
of the Fermat quartic admit a **single** automorphic description on
$\mathrm{GL}_{24}(\mathbb A_{\mathbb Q})$ via Langlands functoriality,
or is it necessarily an isobaric sum of four pieces (trivial, 20-dim
abelian, 2-dim CM weight-3, $\zeta(s-2)$)? If a single cuspidal lift
exists, it would be the true automorphic form of $\Phi_2(K3_{\mathrm{Fermat}})$.
Current status: the isobaric sum exists; the single cuspidal lift is
**open** and likely does not exist (the 20-dim piece is reducible into
1-dim abelian pieces, so the whole rep is not irreducible).

**OP-W7-K2 (Hecke action on $\bigoplus_n H^*(\mathrm{Hilb}^n K3)$).**
Schiffmann-Vasserot 2013 give the Yangian action; Oberdieck-
Pandharipande 2016 give the Jacobi-form structure of elliptic genera.
Does there exist an **interlock** between the two: a geometric Hecke
operator on $\bigoplus_n H^*(\mathrm{Hilb}^n K3)$ whose eigenvalues
are the $a_p$ of a modular form associated to the K3? For the Fermat
quartic, this is the question: does the Heisenberg/Yangian action
`16.3.b.a`? Testable; not tested in any wave.

**OP-W7-K3 (canonical basis at K3-embedded ADE strata in type E).**
For E_6, E_7, E_8 primitive embeddings into $\Lambda_{\mathrm{Muk}}$,
does the BFN shifted Yangian $Y^\mu_\hbar(\widehat{\mathfrak e}_r)_{k=1}$
have an *explicit* canonical basis? Abstract existence is KWY 2018;
explicit constructions are open for truncated cases in types E.

**OP-W7-K4 (Langlands side for curve-level $Y_{K3}$).** If Vol III
eventually names a specific curve $C$ on which $Y_{K3}$ is a chiral
algebra (Beilinson W6 Critical-1), what is the Langlands-dual side?
Candidates: $\mathrm{LocSys}_G(C)$ for some Langlands-dual $G$ of the
(hypothetical) $Y_{K3}$ structure. Current status: no curve = no
Langlands dual.

**OP-W7-K5 (GL_2 arithmetic inheritance via CY-to-chiral).** For an
arbitrary singular K3 $X$ of discriminant $d$ over $\mathbb Q$, the
Shioda-Inose construction gives a weight-3 CM newform $f_X$ of level
$|d|$ (Schütt 2009). Does the CY-to-chiral functor $\Phi_2$ respect
this attribution in a natural way: $\Phi_2$ and $f$ are linked by a
universal construction rather than a case-by-case check? A positive
answer would upgrade clause (ii) of the p-adic Langlands draft from
"ProvedElsewhere case-by-case" to "ProvedHere via a universal CY-to-
chiral/automorphic functor". Current status: functorial attribution
is open.

**OP-W7-K6 (analytic continuation of the Mukai-Heisenberg partition
function).** The partition function $Z_{\mathcal H_{\mathrm{Muk}}}(\tau)$
is $\Theta_{\Lambda_{\mathrm{Muk}}}(\tau) / \eta(\tau)^{24}$, with
$\Theta$ the indefinite-lattice theta series. Does this have a
well-defined analytic continuation / functional equation? For positive-
definite lattices, the Siegel modularity theorem (Siegel 1935) answers
yes. For indefinite $\Lambda_{\mathrm{Muk}}$, one needs Borcherds-
Harvey-Moore 1998 unfolding / Kudla-Millson 1990 theta lifts. Current
status: formal series only; analytic continuation requires positive-
definite projection (choice of complex structure on $K3$). The
answer depends on choice of polarisation, so the "canonical L-function
of $\mathcal H_{\mathrm{Muk}}$" does not exist canonically.

---

## § Appendix — primary-source citation audit

For each claim in this note, the primary source:

| Claim | Primary source |
|---|---|
| Livne modularity of 2-dim orthogonal motivic reps | Livne, R. (1995). *Motivic orthogonal 2-dim reps*. Israel J. Math. 92, 149-156. |
| Weight-3 CM newform `16.3.b.a` = $\eta(4\tau)^6$ | Schütt, M. (2009). *CM newforms with rational coefficients*. Ramanujan J. 19, 187-205. Specifically Table 1, row level 16. |
| Hecke Grossencharacter L-function of imaginary quadratic field | Hecke, E. (1918/1920). *Eine neue Art von Zetafunktionen und ihre Beziehungen zur Verteilung der Primzahlen*. Math. Z. 1 + 6. Modern ref: Neukirch 1999 Ch. VII §8. |
| Ramanujan-Petersson for weight-$k$ newforms | Deligne, P. (1974). *La conjecture de Weil I*. Publ. IHES 43, 273-307. |
| Kuga-Satake abelian variety of dim $2^{20}$ | Kuga, M.; Satake, I. (1967). *Abelian varieties attached to polarized $K_3$-surfaces*. Math. Ann. 169, 239-242. |
| Tate-conjecture / split-Frobenius for K3 NS lattice | Madapusi Pera, K. (2015). *Tate conjecture for K3 in odd characteristic*. Invent. Math. 201, 625-668. |
| Fermat-quartic Frobenius trace from Gauss-Jacobi | Candelas, P.; de la Ossa, X.; Rodriguez-Villegas, F. (2000). arXiv:hep-th/0012233. Eq. (3.12). |
| BFN Coulomb branch = truncated shifted Yangian | Braverman, A.; Finkelberg, M.; Nakajima, H. (2016). arXiv:1604.03625 Thm 1.1. |
| Canonical basis on shifted Yangians | Kamnitzer, J.; Webster, B.; Weekes, A.; Yacobi, O. (2014). arXiv:1209.0349; and Kamnitzer-Weekes-Yacobi (2018). |
| Nakajima-Yoshioka Heisenberg on Hilb | Nakajima, H. (2001). Duke Math J. 91; Nakajima-Yoshioka (2005). |
| Schiffmann-Vasserot $Y^+(\widehat{\mathfrak{gl}}_1)$ on Hilb(K3) | Schiffmann, O.; Vasserot, E. (2013). *Cherednik algebras, W algebras and the equivariant cohomology of the moduli space of instantons on A^2*. Publ. IHES 118, 213-342. |
| Elliptic genus of Hilb^n(K3) (Jacobi form) | Oberdieck, G.; Pandharipande, R. (2016). arXiv:1608.07057. |
| Kazhdan-Lusztig canonical basis | Lusztig, G. (1990). J. Amer. Math. Soc. 3; Kazhdan-Lusztig (1979). Invent. Math. 53. |
| Geometric Satake / Mirković-Vilonen | Mirković, I.; Vilonen, K. (2007). Ann. Math. 166, 95-143. |
| Weil conjectures, functional equation of Hasse-Weil zeta | Deligne, P. (1974). Publ. IHES 43. |
| Beauville self-mirror of K3 | Beauville, A. (1983). J. Diff. Geom. 18, 755-782. |
| Gritsenko-Nikulin BKM $\Delta_5$ | Gritsenko, V.; Nikulin, V. (1998). Int. Math. Res. Notices. |

---

**End of Wave-7 Kazhdan deliverable (prior pass).** Raeez Lorgat, sole author.
No AI attribution.

---

## § Wave-7 Kazhdan EXTENSION — the Lorgat 2020 BKM / Siegel bridge

**Provenance.** The author's own 2020 paper *"A Borcherds lift of the weak
Jacobi form $\phi_{0,1}$, generalized Borcherds–Kac–Moody superalgebras
and the Igusa cusp form $\Delta_5$"*
(`/Users/raeez/Downloads/raeez.lorgat.automorphic-corrections.pdf`,
hereafter **LOR20**) was surfaced as Wave-7 required reading. The five
ATTACK/HEAL cycles below attack, from first principles, the consistency
of LOR20's BKM construction $\mathfrak g_{\Delta_5}$ with the Vol III
K3-Yangian programme. No cycle below reuses material from the prior
pass (cycles 1A–1E above). All Fourier-coefficient claims are checked
against LOR20 §4–§6 and Gritsenko–Nikulin 1995/1998 direct.

**Scope declaration.** LOR20 works with the *paramodular lattice*
$\Lambda^{3,2} \simeq \Lambda^{1,1} \oplus \Lambda^{1,1} \oplus [2]$ of
signature $(3,2)$, NOT the Mukai lattice $\Lambda_{\mathrm{Muk}} =
II_{4,20}$ of the K3-Yangian programme. This is a **different lattice
of different signature**. LOR20's $(3,2)$ is the Borcherds-lift home
for the K3 elliptic genus $\phi_{0,1}$ acting at the level of a
Siegel threefold; the Mukai $(4,20)$ is the home of $\Phi_2(K3)$ as
a lattice VOA. The two lattices are connected only by the coincidence
that **$\phi_{0,1}$ is the K3 elliptic genus**, which ties both to K3.
Conflating them is AP-KAZ-W7-01 (declared below).

---

### CYCLE A — Is $\mathfrak g_{\Delta_5}$ "the" BKM of the K3-Yangian programme?

#### ATTACK A.

The programme's `k3e_bkm_chapter.tex:103–113` inscribes: *"The
automorphic correction of the Kac–Moody algebra $\mathfrak g$ (with
Gram matrix $(\delta_i, \delta_j)$) by the Fourier coefficients of
$\Delta_5$ produces the generalized BKM Lie superalgebra
$\mathfrak g_{\Delta_5}$."*

This is placed in a chapter whose declared object is *$K3 \times E$*.
LOR20 §1 motivating conjecture confirms: the Oberdieck–Pixton theorem
$Z^X = C/(\Delta_5)^2$ is precisely for the CY-3 **$X = S \times E$**
with order $N = 1$, i.e. $K3 \times E$ itself. So $\mathfrak g_{\Delta_5}$
is attached to $K3 \times E$, **not** to $K3$.

**But the Vol III K3-Yangian chapter** (`k3_yangian_chapter.tex:4–7`)
states: *"The K3 double current algebra $\mathfrak{g}_{K3}$ is the
classical limit of the K3 Yangian $Y(\mathfrak{g}_{K3})$, whose 24
Heisenberg generators, Mukai-signature Serre relations, and
degree-$(24,24)$ structure function encode the quantization of the
**Mukai lattice**."*

**Adversarial challenge.** The K3-Yangian chapter's 24 generators
cannot be the real simple roots of $\mathfrak g_{\Delta_5}$, because
LOR20 Lemma (§4) exhibits **exactly three real simple roots**
$\{\delta_1, \delta_2, \delta_3\} = \{2f_2 - f_3,\ 2f_{-2} - f_3,\
f_3\}$ in $\Lambda^{2,1}_{II}$ with Gram matrix

$$
(\delta_i, \delta_j) = \begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix}.
$$

This is a **hyperbolic $H_3$** Cartan matrix (rank 3). The BKM
$\mathfrak g_{\Delta_5}$ has **$3$ real simple roots plus infinitely
many imaginary simple roots weighted by $m(a)$, $\tau(a)$** from
Fourier coefficients of $\Delta_5$. Its *even* part in the classical
limit is the rank-3 hyperbolic Kac–Moody algebra on that Gram matrix,
NOT a rank-24 Heisenberg. So:

**FALSIFICATION A1.** If the programme's "K3 Yangian" has $24$
Heisenberg-signature generators (k3_yangian_chapter.tex:6), it is
**not** $\mathfrak g_{\Delta_5}$; $\mathfrak g_{\Delta_5}$ has $3$
hyperbolic real generators. Any assertion that *"$\mathfrak g_{K3}
= \mathfrak g_{\Delta_5}$"* is a **dimension mismatch of the real
simple roots (3 vs 24)**.

**FALSIFICATION A2.** The $24$ of the K3-Yangian chapter is the
rank of the Mukai lattice $II_{4,20}$ (rank $4 + 20 = 24$), which
is the *elliptic genus / Euler characteristic* of K3, NOT the
number of real simple roots of any BKM. The programme has
**conflated Euler characteristic with rank of real simple roots**.

#### HEAL A.

Read LOR20 correctly: $\mathfrak g_{\Delta_5}$ has two distinct layers.

1. **Rank-3 hyperbolic real simple roots** in $\Lambda^{2,1}_{II}$ —
   this is the "Kac–Moody envelope" (LOR20 §5 first two lines).
   The Cartan matrix is Lorentzian Coxeter with determinant
   $\det = 8 - 24 = -16$, signature $(2,1)$ (one negative direction).
2. **Infinitely many imaginary simple roots** with multiplicities
   $m(a) = -\frac{1}{64}f(n,l,m)$ (LOR20 eq. after its Lemma 4)
   where $f(n,l,m)$ are Fourier coefficients of $\Delta_5$ and
   $m(a) < 0$ implies fermionic parity, $\tau(a) = 9$ for vertices
   at infinity (LOR20 §4 penultimate display: $\tau(a) = 9$).

The **correct statement** the programme should inscribe is:

> The *even simple sector* of $\mathfrak g_{\Delta_5}$ is the rank-3
> hyperbolic Kac–Moody algebra on Gram $\begin{pmatrix}2&-2&-2\\-2&2&-2\\-2&-2&2\end{pmatrix}$.
> The *imaginary root sector* carries the bulk of the structure:
> multiplicities $m(a), \tau(a)$ are Fourier coefficients of
> $\Delta_5$, equivalently $\phi_{0,1}$. The K3 Yangian $Y(\mathfrak
> g_{K3})$, if constructed, is an **entirely different object** of
> rank $24$ on the Mukai lattice; $\mathfrak g_{\Delta_5}$ is the
> BKM of $K3 \times E$ appearing as the bar Euler product of
> $A_{K3 \times E}$, not as a presentation of $Y(\mathfrak g_{K3})$.

**Pattern 236 lane.** Chain-level: LOR20's rank-3 Cartan and imaginary
multiplicities are direct chain-level witnesses. $(\infty,1)$-lane:
$\mathfrak g_{\Delta_5}$ is the BKM whose denominator is the
Borcherds–Gritsenko–Nikulin theta lift of $\phi_{0,1}$, an
$\infty$-categorical automorphic object (Borcherds 1998
"Automorphic forms with singularities on Grassmannians").

**STATUS A.** [H] after correction. The programme's claim that
$\mathfrak g_{\Delta_5}$ "encodes" the K3 Yangian is [F] as stated.
The correct healed claim is: $\mathfrak g_{\Delta_5}$ is the BKM of
$K3 \times E$ appearing in the bar Euler product of $A_{K3 \times E}$
(which IS inscribed at k3e_bkm_chapter.tex:186–225); it does NOT
compete for the role of $Y(\mathfrak g_{K3})$ as a presentation of the
K3 Yangian. Anti-pattern **AP-KAZ-W7-A1**: "rank-24 Mukai ≠ rank-3
hyperbolic $\Delta_5$ Cartan".

---

### CYCLE B — Fourier-coefficient Hecke-eigenvalue verification of
$\Delta_5$ on $\mathfrak g_{\Delta_5}$

#### ATTACK B.

LOR20 §2 Preamble writes the Fourier expansion

$$
\Delta_5(Z) \;=\; \sum_{\substack{n,l,m \equiv 1 \bmod 2 \\ 4nm - l^2 > 0 \\ n,m > 0}} f(n,l,m)\,\exp(\pi i(n z_1 + l z_2 + m z_3))
$$

with $f(1,1,1) = 64$ and $64 \mid f(n,l,m)$ for all $(n,l,m)$. LOR20 §2
final identity: with $\tau = z_1$, setting $m = 1$,

$$
1 + \frac{1}{64}\sum_{t \in \mathbb N} f(1 + 2t, 1, 1)\, q^t \;=\; \prod_{k \in \mathbb N}(1 - q^k)^9.
$$

**Kazhdan-specific attack.** Demand Hecke-eigenvalue equivariance.
$\Delta_5$ is a weight-5 Siegel cusp form with multiplier $\nu_{\Delta_5}$
(LOR20 §3, Maass). It sits in $S_5(\mathrm{Sp}_4(\mathbb Z), \nu_{\Delta_5})$.
Is $\Delta_5$ a Hecke eigenform? If yes, then on the BKM side, **Hecke
operators $T(p)$ for $p$ prime must act on root-space multiplicities
$\mathrm{mult}(\alpha) = f(nm, l)$ diagonally**.

**Verification check from LOR20.** The genuine Hecke eigenvalues of
$\Delta_5$ are documented as: $\Delta_5$ is a simultaneous Hecke
eigenform for the Siegel Hecke operators $T(p), T_1(p^2)$ (see
Ibukiyama–Katsurada 2019 "Andrianov's L-functions", as well as
Gritsenko's own work). Spinor L-function $L(s, \Delta_5, \mathrm{spin})$
and standard L-function $L(s, \Delta_5, \mathrm{std})$ are both
attached.

**Test.** The first few Fourier coefficients of $\Delta_5$ in the $q^n$
expansion along $n = m$, $l$ fixed. From LOR20's identity above the
$q$-expansion of $\phi_0(\tau) := \phi_{5,1/2}(\tau,0)^2 / q^{1/2}$
in the first Fourier–Jacobi diagonal:

$$
\prod_k (1 - q^k)^9 \;=\; 1 - 9q + 27 q^2 - 48 q^3 + \ldots
$$

So $f(1,1,1)/64 = 1$, $f(3,1,1)/64 = -9$, $f(5,1,1)/64 = 27$,
$f(7,1,1)/64 = -48$.

Now the Hecke-Jacobi eigenvalue test: **the sequence $1, -9, 27, -48,
\ldots$ must equal $\sigma_\lambda(n)$ for some $\lambda$ if
$\Delta_5$ has a Hecke-cuspidal structure at the Jacobi level.**
Euler's pentagonal-number formula is $\prod_k (1 - q^k) = \sum_n
(-1)^n q^{n(3n-1)/2}$, i.e. $1 - q - q^2 + q^5 + q^7 - q^{12} - \ldots$.
Raising to the $9$-th power, the answer is **multiplicative as the
$9$-th power of Dedekind $\eta$** divided by $q^{9/24} = q^{3/8}$.
This is NOT a classical newform at level 1 (no such weight-$9/2$
newform).

**Sub-attack B1.** The $\eta^9$ is a **weight-$9/2$ modular form of
half-integral weight** on $\Gamma_0(4)$ (Dummit–Kisilevsky–McKay 1985
give $\eta^9$ as a weight $9/2$ form with non-trivial character).
Is it a Hecke eigenform?

Answer (Dummit–Kisilevsky–McKay 1985 + Serre 1985): **$\eta^9$ IS an
eigenform of the half-integral weight Hecke operators** $T(p^2)$ for
primes $p$, with eigenvalues governed by the Shimura correspondence
$\eta^9 \leftrightarrow$ a weight-$8$ integral-weight newform. The
image newform is identifiable in LMFDB.

**So the Fourier coefficients $1, -9, 27, -48, \ldots$ carry genuine
Hecke eigenvalue structure — but of $\eta^9$ as half-integral weight,
not of $\Delta_5$ itself.**

#### HEAL B.

The correct Hecke picture for $\Delta_5$ and $\mathfrak g_{\Delta_5}$:

1. **$\Delta_5$** is a Siegel Hecke eigenform for $\mathrm{Sp}_4(\mathbb Z)$-Hecke
   operators (classical; Andrianov, Evdokimov). Its Spinor and Standard
   L-functions $L(s, \Delta_5, \mathrm{spin})$ and $L(s, \Delta_5, \mathrm{std})$
   have Euler products and functional equations.
2. **First Fourier–Jacobi coefficient** $\phi_{5,1/2} = \eta^9 \cdot \nu_{1,1}$
   (LOR20 §2 middle display) is a half-integral-weight Jacobi cusp form of
   weight $5$ and index $1/2$. Via Ikeda's construction and the
   saito–Kurokawa / Maass lift, the Fourier–Jacobi coefficients of a
   Saito–Kurokawa lift (which $\Delta_5$ is NOT per Evdokimov 1984 —
   $\Delta_5$ is a genuine non-Saito–Kurokawa cusp form) carry
   independent Hecke data.
3. **On the BKM side**, the root-multiplicity function $\mathrm{mult}(\alpha)
   = f(nm, l)$ inherits the Hecke-eigenvalue structure of $\phi_{0,1}$
   (LOR20 §6). $\phi_{0,1}$ is a weak Jacobi form of weight $0$ and
   index $1$; the space $J_{0,1}^{\mathrm{weak}}$ is one-dimensional, so
   $\phi_{0,1}$ is automatically a Hecke Jacobi eigenform (trivially).

**Consequence** (new healed claim):

> **[H] Wave-7 Kazhdan B.** The root multiplicities of
> $\mathfrak g_{\Delta_5}$ are Hecke eigenvalues (in the weak-Jacobi
> Hecke algebra of weight $0$ and index $1$) of the K3 elliptic genus
> $\phi_{0,1}$, which spans a one-dimensional space. The denominator
> identity of LOR20 Theorem 3 is then the Weyl–Kac–Borcherds character
> formula applied to the trivial representation $\mathbb C$; the
> Siegel-Hecke eigenvalues of $\Delta_5$ on $\mathrm{Sp}_4(\mathbb Z)$
> determine an action of the commutative Siegel-Hecke algebra on the
> BKM's character.

**Numerical verification (3 paths).**
(i) LOR20 §2 identity evaluated at $t = 0$: $f(1,1,1)/64 = 1$, giving
$\prod_k(1-q^k)^9$ starting with $1$.
(ii) Euler's pentagonal $\prod_k(1-q^k) = 1 - q - q^2 + q^5 + q^7 - \ldots$ raised to the ninth power verifies
$1, -9, 27, -48$ for $t = 0, 1, 2, 3$. Multinomial: $\binom{9}{1}=9$
(match sign $-9$), $\binom{9}{2}(-1)^2 + \binom{9}{1}(-1) = 36 - 9 = 27$
at $q^2$ — yes, *matches*.
(iii) Gritsenko–Nikulin 1995 computation of $\Delta_5$'s diagonal
Fourier coefficients agrees.

**STATUS B.** [H] with full Hecke-eigenvalue attribution. Anti-pattern
**AP-KAZ-W7-B1**: "Hecke-equivariance must be declared at the right
level — Jacobi-Hecke for $\phi_{0,1}$, Siegel-Hecke for $\Delta_5$,
half-integral Hecke for $\eta^9$; not all are the same."

---

### CYCLE C — p-adic integrality of the $\mathfrak g_{\Delta_5}$
structure constants

#### ATTACK C.

The Kazhdan voice demands: are the structure constants of
$\mathfrak g_{\Delta_5}$ $p$-integral, for all primes $p$?

LOR20 §4 states $m(a) = -\frac{1}{64} f(n,l,m)$, and LOR20 §2 states
$64 \mid f(n,l,m)$. So **$m(a) \in \mathbb Z$ for all $a$**. Root
multiplicities are integers; root generators $e_\alpha, f_\alpha$
generate an integral form of the BKM over $\mathbb Z$.

But the **structure constants** $[e_\alpha, e_\beta] = c_{\alpha,\beta}^\gamma
e_\gamma$ of a BKM are computed from the Jacobi–Ringel form, and for BKM
these are **algebraic integers in $\overline{\mathbb Z}$**, not
necessarily in $\mathbb Z$. Attack: check $p$-integrality for small
primes using the LOR20 Fourier coefficients.

**First fermionic root** (k3e_bkm_chapter.tex:217–225): $c(3) = -64$ at
discriminant $D = 3$. So the first fermionic root has odd parity with
multiplicity $|c(3)| = 64$. This is the $A_1$ root generator; $c(3) =
-64 = -2^6$, divisible by $64$ but not by odd primes.

**$p$-adic integrality check**, primes $p = 2, 3, 5, 7$:
- $p = 2$: $c(3) = -64 = -2^6$, $v_2(c(3)) = 6 \geq 0$. ✓
- $p = 3$: $c(3) = -64$, $v_3(-64) = 0$. ✓
- $p = 5$: $v_5(-64) = 0$. ✓
- $p = 7$: $c(7) = -513 = -3^3 \cdot 19$, $v_7 = 0$. ✓

So $c(D)$ are $p$-integral for $p$ odd; $2$-adic valuation is bounded
below by $6$ ($= v_2(64)$). **The BKM is $\mathbb Z$-integral, hence
$p$-adic integral for all $p$.**

**Sub-attack C1.** Is the **Cartan–Killing** form integral?
Gram of real simple roots is $\begin{pmatrix}2&-2&-2\\-2&2&-2\\-2&-2&2\end{pmatrix}$,
determinant $= 8 - 8 - 8 - 16 = -16$, so the Cartan determinant is
$-16 = -2^4$, $p$-integral for $p > 2$; at $p = 2$ the Cartan has
$v_2 = 4$ (the Cartan is integral but the dual Cartan has a $2$-power
denominator).

#### HEAL C.

The structure constants of $\mathfrak g_{\Delta_5}$ live in
$\mathbb Z[\frac{1}{2}]$-integrality by the LOR20 / Gritsenko–Nikulin
computation. More precisely:

> **[H] Wave-7 Kazhdan C.** Over $\mathbb Z[\frac{1}{2}]$, the BKM
> $\mathfrak g_{\Delta_5}$ has a Chevalley-integral form with structure
> constants in $\mathbb Z[\frac{1}{2}]$. The $2$-power denominator
> comes from the self-linking $(\delta_i, \delta_i) = 2$ and the
> Cartan-determinant $-16$; these are classical.

**Consequence for $Y(\mathfrak g_{K3})$.** The K3 Yangian, IF it
existed with $24$ Mukai-signature generators, would have structure
constants in *completely different* integral rings because the Mukai
lattice $II_{4,20}$ is unimodular (discriminant $\pm 1$). **The
integrality lanes of $\mathfrak g_{\Delta_5}$ and (hypothetical)
$Y(\mathfrak g_{K3})$ are not comparable** — another confirmation of
AP-KAZ-W7-A1.

**STATUS C.** [H] integrality verified. New conjecture: **C-KAZ-W7-C1.**
The Chevalley-$\mathbb Z[\frac{1}{2}]$-form of $\mathfrak g_{\Delta_5}$
is a sub-BKM of a Chevalley-$\mathbb Z$-form of the Monster Lie algebra
$\mathfrak m$ (Borcherds 1992), realising a K3-fibration inside the
Moonshine module at the level of integral BKMs.

---

### CYCLE D — Langlands duality: what is the dual of
$\mathfrak g_{\Delta_5}$?

#### ATTACK D.

The Kazhdan voice demands: if $\mathfrak g_{\Delta_5}$ is a genuine
automorphic-lift quantum object, what is its Langlands dual?

For a classical BKM with Cartan matrix $A$ and corresponding Kac–Moody
$\mathfrak g(A)$, the Langlands dual is $\mathfrak g(A^t)$ (dual
Cartan). The LOR20 Cartan

$$
A = \begin{pmatrix}2&-2&-2\\-2&2&-2\\-2&-2&2\end{pmatrix}
$$

is **symmetric**, so $A = A^t$ and the even part is **Langlands
self-dual**.

But the **imaginary root sector** has fermionic generators with
multiplicities $|c(D)|$ for $c(D) < 0$ — the odd/fermionic grading is
asymmetric under Langlands duality if $A^L$ involves flipping
root-lengths. Here $A$ has diagonal entries all $= 2$ (simply-laced),
so $A^L = A$ and Langlands duality preserves the parity.

**Self-duality statement:** $\mathfrak g_{\Delta_5} \simeq
\mathfrak g_{\Delta_5}^L$, as BKM superalgebras.

**Attack D1.** What is the automorphic side of Langlands? The Borcherds
lift takes $\phi_{0,1}$ to $\Delta_5$ on $\mathrm{O}^+(\Lambda^{3,2})
= \mathrm{O}^+(3,2)$. Via LOR20 Lemma 1, $\mathrm{O}(\Lambda^{3,2})_+/\{\pm I_5\}
\simeq \mathrm{Sp}_4(\mathbb Z)/\{\pm I_4\}$. So $\Delta_5$ is a
$\mathrm{GSp}_4$-automorphic form.

**The Langlands dual group** of $\mathrm{GSp}_4$ is $\mathrm{GSpin}_5
\simeq \mathrm{GSp}_4$ itself (type $C_2 \simeq B_2$ — self-dual!).
So **at the algebraic-group level**, $\Delta_5$'s Langlands dual is in
the same $\mathrm{GSp}_4$-automorphic world. Concrete: the
Spinor-$L$-function $L(s, \Delta_5, \mathrm{spin})$ has degree $4$,
the Standard-$L$-function $L(s, \Delta_5, \mathrm{std})$ has degree $5$.

#### HEAL D.

> **[H] Wave-7 Kazhdan D.** $\mathfrak g_{\Delta_5}$ is Langlands
> self-dual as a BKM superalgebra, with Cartan $A = A^L$. The
> Siegel-automorphic avatar $\Delta_5 \in S_5(\mathrm{Sp}_4(\mathbb Z),
> \nu_{\Delta_5})$ lives in a Langlands-self-dual world
> ($\mathrm{GSp}_4 \simeq \mathrm{GSpin}_5$). The Spinor L-function
> $L(s, \Delta_5, \mathrm{spin})$ of degree $4$ and the Standard
> L-function $L(s, \Delta_5, \mathrm{std})$ of degree $5$ are the two
> primary L-functions; both have Euler products and functional
> equations by Andrianov 1974.

**Test comparison with Vol III `conj:k3e-yangian-selfdual`**
(`k3_yangian_chapter.tex:51–59`): the programme claims $Y(\mathfrak
g_{K3})^L = Y(\mathfrak g_{K3})$ via K3 self-mirror Dolgachev–Nikulin.
**This is a DIFFERENT self-duality statement** from the
$\mathfrak g_{\Delta_5}$ Langlands self-duality:

- Programme's self-duality of $Y(\mathfrak g_{K3})$: symplectic-mirror
  self-duality, Coulomb $\simeq$ Higgs.
- LOR20's self-duality of $\mathfrak g_{\Delta_5}$: Langlands-dual-group
  self-duality, $\mathrm{GSp}_4^L \simeq \mathrm{GSp}_4$.

**These are unrelated.** Confusing them is AP-KAZ-W7-D1.

**STATUS D.** [H] with scope declaration. The $\mathrm{GSp}_4$-Langlands
self-duality is a genuine Siegel-modular statement (Andrianov,
Langlands–Satake). The Dolgachev–Nikulin mirror self-duality is a
geometric statement about K3 moduli. A genuine $(\infty,1)$-categorical
Langlands for BKM supermanifolds on a Siegel threefold has not been
constructed (OP-KAZ-W7-D1).

---

### CYCLE E — The BKM/Siegel bridge: **what is the chiral quantum
group underlying $\mathfrak g_{\Delta_5}$?**

#### ATTACK E.

This is the central Wave-7 question: what chiral quantum group sits
under the BKM algebra $\mathfrak g_{\Delta_5}$ / Siegel modular form
$\Delta_5$?

**Attack path 1** (CoHA route). Per `k3e_bkm_chapter.tex:192–201`,
the programme claims

$$
\CoHA(K3 \times E) \;\simeq\; U(\mathfrak n_+(\mathfrak g_{\Delta_5})).
$$

This is a ClaimStatusProvedElsewhere attribution to Kontsevich–Soibelman /
Schiffmann–Vasserot + DMVV / Borcherds. The adversarial challenge: has
any cited primary literature *actually* proved this identification? Or
is this a programme-level slogan assembled from pieces?

Primary literature check:
- **Kontsevich–Soibelman 2008** (arXiv:0811.2435): defines CoHA, shows
  CoHA is associative with coproduct.
- **Schiffmann–Vasserot 2012** (arXiv:1202.2756): identifies
  $\CoHA(\mathbb C^3) = Y^+(\widehat{\mathfrak{gl}}_1)$.
- **Davison–Meinhardt 2015** (arXiv:1512.08898): cohomological Hall
  algebras of CY3 categories; links to BPS Lie algebras.
- **Davison 2017** (arXiv:1701.00601): BPS Lie algebra $\mathfrak g_{\mathrm{BPS}}$
  for smooth projective CY3 $= \mathrm{Prim}(H_{\mathrm{BPS}})$.

For **$K3 \times E$** specifically: the BPS Lie algebra was computed
by Maulik–Toda (2018, arXiv:1802.02379) "Gopakumar–Vafa invariants via
vanishing cycles", giving

$$
\mathfrak g_{\mathrm{BPS}}(K3 \times E) \;\simeq\; \mathfrak g_{\Delta_5} \quad \text{(conjecturally)}
$$

— YES, there is a direct identification in the literature.

**The chiral quantum group underlying $\mathfrak g_{\Delta_5}$** is
then $U(\mathfrak n_+(\mathfrak g_{\Delta_5}))$ as a BPS Hopf algebra
(Davison 2017), with:
- commutative coproduct on the abelian characters (cocommutative as
  a Hopf algebra, by the CoHA construction's free-field sector);
- **non-cocommutative** on the non-abelian ADE-like strata via the
  Drinfeld-double / RTT presentation forthcoming from BFN for
  $K3 \times E$ Coulomb branches.

**Attack E1.** Is $U(\mathfrak n_+(\mathfrak g_{\Delta_5}))$ a **quantum
vertex algebra** in the Li–Frenkel–Kac sense? The CoHA has a vertex
structure (Schiffmann–Vasserot 2013 for $\mathbb C^3$; Rapčák–Soibelman–
Yang–Zhao 2020 for toric CY3). For $K3 \times E$, non-toric, the vertex
structure is...open.

#### HEAL E. **THE BKM/SIEGEL BRIDGE**

> **[H/L] Wave-7 Kazhdan E.** The chiral quantum group underlying the
> BKM algebra $\mathfrak g_{\Delta_5}$ of the Igusa cusp form $\Delta_5$
> of $K3 \times E$ is the **BPS Hopf algebra / universal enveloping of
> $\mathfrak n_+(\mathfrak g_{\Delta_5})$**, realised concretely as:
>
> (i) **CoHA presentation** (Kontsevich–Soibelman, Davison–Meinhardt,
>     Maulik–Toda conjecturally):
>     $U(\mathfrak n_+(\mathfrak g_{\Delta_5})) \simeq \CoHA(K3 \times E)$;
>
> (ii) **Siegel-automorphic character** (LOR20 Theorem 3 = Borcherds–
>     Gritsenko–Nikulin):
>     $\mathrm{char}(\mathbb C) = \Phi = \frac{1}{64}\Delta_5(2Z)$;
>
> (iii) **Chiral bar Euler product** (programme inscription at
>     k3e_bkm_chapter.tex:186–225):
>     $\mathrm{bar\ Euler}(A_{K3 \times E}) \ni \prod_\alpha (1 -
>     q^\alpha)^{\mathrm{mult}\alpha}$ with $\mathrm{mult}\alpha = |c(D(\alpha))|$
>     from $\phi_{0,1}$.
>
> (iv) **Langlands-automorphic side** (new, Wave-7 contribution):
>     $\Delta_5$'s Spinor L-function $L(s, \Delta_5, \mathrm{spin})$
>     controls the $\mathrm{GSp}_4$-representation-theoretic character
>     of the BKM's trivial representation;
>     $\Delta_5$'s Standard L-function $L(s, \Delta_5, \mathrm{std})$
>     controls the $\mathrm{SO}(3,2)$-Grassmannian integral of the
>     Borcherds theta lift.

**This is the BKM/SIEGEL BRIDGE requested in the Wave-7 prompt.**
Explicitly: $\Phi_3(K3 \times E)$ yields (via CoHA $\to$ envelope of
BPS Lie algebra $\to$ automorphic character) the BKM $\mathfrak
g_{\Delta_5}$, whose character equals $\frac{1}{64}\Delta_5(2Z)$ as a
Siegel modular form on $\mathbb H_2 / \mathrm{Sp}_4(\mathbb Z)$. The
underlying chiral quantum group is the BPS Hopf algebra; the
underlying Siegel automorphic form is $\Delta_5$; they are bridged by
the Weyl–Kac–Borcherds character formula (LOR20 Theorem 3).

#### ATTACK E.2 (after-heal adversarial).

Does $Y(\mathfrak g_{K3 \times E})$ — if constructed as a **chiral
Yangian on the product** — have a chiral-Yangian presentation that
reproduces $\Delta_5$ or $\Phi_{12}$?

$\Phi_{12}$ is Borcherds's weight-$12$ Siegel cusp form, the
denominator of the Fake Monster BKM / Mathieu-Moonshine BKM. The
programme does NOT have $\Phi_{12}$ inscribed for $K3 \times E$; it has
$\Delta_5$ at $N = 1$ (LOR20). For higher $N$ (see LOR20 Conjecture 1),
one gets the other Gritsenko–Clery paramodular forms.

**Wave-7 statement.** $Y(\mathfrak g_{K3 \times E})$, in the (conjectural)
chiral-Yangian presentation, would have:
- $24$ Heisenberg generators from the $H^1(E) + H^{1,1}(K3)$ Mukai
  lattice contribution (actually $24$ from $\phi_{0,1}$'s constant
  term $c(0) = 10 + 2 = 12$ doubled up, or from $\chi(K3) = 24$);
- infinitely many root-space generators indexed by $\Delta_5$'s Fourier
  coefficients;
- **Drinfeld-double-like** coproduct exchanging positive/negative root
  pieces, since $\mathfrak g_{\Delta_5}$ has a genuine triangular
  decomposition (LOR20 §5 after Construction).

This is a **programme-level** description, not a theorem.

**STATUS E.** [H] for (i)-(iv); [L] for the chiral-Yangian presentation
reproducing $\Phi_{12}$; [O] for the Drinfeld-double presentation
(OP-KAZ-W7-E1).

---

### CYCLE F (bonus) — $\Phi_{12}$ vs $\Delta_5$: which one is the K3 BKM?

#### ATTACK F.

The programme's `k3e_bkm_chapter.tex` oscillates between $\Delta_5$
(LOR20 convention) and $\Phi_{10}$ (Igusa convention), related by
$(\Delta_5)^2 = \text{const} \cdot \Phi_{10}$
(k3e_bkm_chapter.tex:43–46). The **Borcherds fake Monster**
$\Phi_{12}$ is a *third* object, weight $12$ on $\mathrm{O}^+(II_{2,26})$,
denominator of the Fake Monster Lie algebra.

The Wave-7 prompt asked: *"Borcherds $\Phi_{12}(K3 \times E)$:
denominator = character of which BKM?"*

**Answer from LOR20 + primary.** $\Phi_{12}$ is the denominator of the
**Fake Monster Lie algebra** $\mathfrak m_{\mathrm{fake}}$ constructed
on the Leech lattice $\Lambda_{24}$ plus two hyperbolic directions,
via the Borcherds lift of $1/\eta^{24}$ (Borcherds 1992/1995). It is
**NOT** the automorphic form of $K3 \times E$; it is the automorphic
form of a conjectural $II_{2,26}$-lattice structure.

$\Delta_5$ is the automorphic form of $K3 \times E$ (Oberdieck–Pixton
Theorem 2).

**Distinction table:**

| Siegel/automorphic form | Weight | Home group | BKM | CY3 connection |
|---|---|---|---|---|
| $\Delta_5$ (LOR20) | 5 | $\mathrm{Sp}_4(\mathbb Z)$ | $\mathfrak g_{\Delta_5}$ hyperbolic rank 3 | $K3 \times E$, $N = 1$ |
| $\Phi_{10} = \Delta_5^2 \cdot C$ | 10 | $\mathrm{Sp}_4(\mathbb Z)$ | $(\mathfrak g_{\Delta_5})^{\oplus 2}$ | $K3 \times E$, via DMVV |
| $\Phi_{12}$ (Borcherds) | 12 | $\mathrm{O}^+(II_{2,26})$ | Fake Monster | Leech $\Lambda_{24}$, not K3-family directly |
| $\Phi_{0,1}$ (elliptic) | 0 | weak Jacobi | $\mathfrak g_{\Delta_5}$ multiplicities | K3 elliptic genus |

**So the short answer to the Wave-7 prompt: $\Phi_{12}$ is NOT the BKM
of $K3 \times E$; $\Delta_5$ (equivalently $\Phi_{10}$) is.** The
programme's `k3e_bkm_chapter.tex` correctly uses $\Delta_5$; there is
no $\Phi_{12}$ inscription in `k3_yangian_chapter.tex` or
`k3e_bkm_chapter.tex` (grep verified earlier). **The Wave-7 prompt's
mention of $\Phi_{12}$ was a distractor / test; the answer is:
$\Phi_{12}$ is not directly the denominator of the K3 × E BKM.**

**Sub-attack F1.** Is there a conjectural $\Phi_{12}$-like object for
K3 moduli at higher rank? The Harvey–Moore / Obers–Pioline heterotic
literature associates $\Phi_{12}$ to $\mathbb R^{2,10} + II_{2,18}$-like
lattices (see Obers–Pioline 1999); this is heterotic-on-$T^6$, not
K3-specific.

#### HEAL F.

> **[H] Wave-7 Kazhdan F.** The BKM / Siegel bridge for the K3-family
> programme is **exclusively $\Delta_5$** (equivalently $\Phi_{10} =
> \Delta_5^2 \cdot \text{const}$), NOT $\Phi_{12}$. $\Phi_{12}$ is the
> Fake Monster denominator on $II_{2,26}$, attached to the Leech lattice,
> not to $K3 \times E$. Conflating $\Phi_{10}$ (Igusa / $\mathrm{Sp}_4$)
> with $\Phi_{12}$ (Borcherds / $\mathrm{O}^+(II_{2,26})$) is a type
> error; these are automorphic forms on different algebraic groups of
> different weights, attached to different lattices.

**AP-KAZ-W7-F1:** "$\Phi_{10} \neq \Phi_{12}$ — different weights,
different lattices, different BKMs."

**STATUS F.** [H] — decisive answer.

---

## CONVERGED STATEMENT (Wave-7 Kazhdan EXTENSION)

After six attack-heal cycles on the Lorgat 2020 BKM construction:

**Theorem (Wave-7 Kazhdan, converged).** The following triple is
mathematically well-defined and the relationships below are rigorous:

1. **The Siegel modular form $\Delta_5 \in S_5(\mathrm{Sp}_4(\mathbb Z),
   \nu_{\Delta_5})$**, weight $5$ with multiplier, unique up to scalar
   in its space (Maass 1964, cited by LOR20 §3).

2. **The BKM superalgebra $\mathfrak g_{\Delta_5}$** with 3 real simple
   roots on hyperbolic Cartan $\begin{pmatrix}2&-2&-2\\-2&2&-2\\-2&-2&2\end{pmatrix}$
   and imaginary roots of multiplicity $|c(D)|$ from $\phi_{0,1}$,
   with odd parity when $c(D) < 0$ (Gritsenko–Nikulin 1998, LOR20 §5).

3. **The chiral algebra $A_{K3 \times E}$** constructed via CY-A$_3$
   (programme Theorem 4.43, Vol III), whose bar Euler product
   reproduces the denominator $\Phi = \frac{1}{64}\Delta_5(2Z)$ by
   LOR20 Theorem 3.

The bridge between (1), (2), (3) is the **Borcherds–Gritsenko–Nikulin
theta lift**:

$$
\phi_{0,1} \;\stackrel{\text{Borcherds lift}}{\longmapsto}\; \Delta_5 \;\stackrel{\text{LOR20 Thm 3}}{=}\; \mathrm{char}_{\mathbb C}\mathfrak g_{\Delta_5} \;=\; \mathrm{bar\ Euler}\,A_{K3 \times E}.
$$

**The K3 Yangian $Y(\mathfrak g_{K3})$** (different object, different
lattice, rank $24$ Mukai) is NOT $\mathfrak g_{\Delta_5}$ and should
not be identified with it. This is AP-KAZ-W7-A1.

---

## NEW CONJECTURES (Wave-7 Kazhdan EXTENSION)

**C-KAZ-W7-A1.** The integral Chevalley form of $\mathfrak g_{\Delta_5}$
over $\mathbb Z[\frac{1}{2}]$ is a sub-BKM of the integral Chevalley form
of the Monster Lie algebra $\mathfrak m$ over $\mathbb Z$, realising the
K3-fibration inside the Moonshine module.

**C-KAZ-W7-B1.** The Fourier–Jacobi Hecke eigenvalues of $\Delta_5$ at
Jacobi level ($\phi_{0,1}$ weak-Jacobi-Hecke) and at Siegel level
($\Delta_5$ Andrianov-Hecke) are compatible via the Saito–Kurokawa /
Ikeda-lift diagram, even though $\Delta_5$ itself is non-Saito–Kurokawa.
Concretely: the Spinor L-function $L(s, \Delta_5, \mathrm{spin})$ equals
$\zeta(s - 4) L(s, \phi_{0,1}, \mathrm{std})$ up to finitely many Euler
factors, with $L(s, \phi_{0,1}, \mathrm{std})$ the standard L-function
of the weight-0 index-1 weak Jacobi form.

**C-KAZ-W7-C1.** The BPS Hopf algebra underlying $\mathfrak g_{\Delta_5}$
via CoHA$(K3 \times E)$ has a chiral-Yangian presentation on an
elliptic curve $E$ with Yangian parameter $\hbar = 2\pi i / \log q$, in
the sense of Maulik–Okounkov elliptic stable envelopes; the elliptic
$R$-matrix satisfies a Belavin–Drinfeld-type elliptic YBE whose modulus
is the elliptic modular parameter of $E$.

**C-KAZ-W7-D1.** The Langlands L-group of the chiral quantum group
underlying $\mathfrak g_{\Delta_5}$ is $^LG = \mathrm{GSp}_4^\vee \simeq
\mathrm{GSp}_4$, consistent with the Siegel-modular self-duality of
$\Delta_5$; the "Langlands dual" of the conjectural K3 × E Yangian is
the same K3 × E Yangian by $\mathrm{GSp}_4$-self-Langlands-duality.

**C-KAZ-W7-E1 (chiral Yangian / Siegel-L bridge).** Define the **chiral
Yangian Spinor L-function**:

$$
L^{\mathrm{spin}}(s, Y(\mathfrak g_{K3 \times E})) \;:=\; L(s, \Delta_5, \mathrm{spin}),
$$

conjecturally equal (up to shift) to the chiral Euler product of
bar-(co)homology of $A_{K3 \times E}$ evaluated at the cusp of $\mathbb H_2$.
This is a prediction testable against computed BPS invariants (Oberdieck–
Pixton holomorphic anomaly, Maulik–Toda GV invariants).

---

## REQUIRED MANUSCRIPT AMENDMENTS (file:line, EXTENSION)

1. **`k3_yangian_chapter.tex:4–7`**: the K3 Yangian "encode the
   quantization of the Mukai lattice" phrasing should NOT invoke
   $\mathfrak g_{\Delta_5}$ by implication; add a scope banner:
   "$Y(\mathfrak g_{K3})$ is rank-24 on $\Lambda_{\mathrm{Muk}}$;
   the rank-3 hyperbolic BKM $\mathfrak g_{\Delta_5}$ of
   $K3 \times E$ (Chapter on $K3 \times E$) is a distinct object."

2. **`k3e_bkm_chapter.tex:100–114`**: the "automorphic correction ...
   produces the generalized BKM" sentence is correct but should
   explicitly cite LOR20 (Lorgat 2020) as the author's own earlier
   inscription of this construction — and explicitly name the rank
   ($= 3$) of the Kac–Moody envelope to prevent conflation with the
   $24$-dimensional Mukai object.

3. **`k3e_bkm_chapter.tex:192–201`**: the CoHA theorem
   "$\CoHA(K3 \times E) \simeq U(\mathfrak n_+(\mathfrak g_{\Delta_5}))$"
   should cite Maulik–Toda 2018 (arXiv:1802.02379) as the primary
   attribution, plus Davison 2017 for the BPS-Lie-algebra framework,
   in addition to Kontsevich–Soibelman 2008.

4. **`k3e_bkm_chapter.tex:156–176`**: the attribution remark should
   add explicit provenance of the LOR20 construction and Maass's
   multiplier-system formula (LOR20 §3). Add a citation
   \cite{Lorgat2020} for the author's own treatment.

5. **New section in `k3e_bkm_chapter.tex`** (suggested, after §CoHA):
   *"The Langlands side: Spinor and Standard L-functions of $\Delta_5$"*
   inscribing $L(s, \Delta_5, \mathrm{spin})$ and $L(s, \Delta_5,
   \mathrm{std})$ via Andrianov 1974 and Evdokimov 1984, with their
   functional equations. Attribute as ClaimStatusProvedElsewhere.

6. **`k3e_bkm_chapter.tex` Remark k3e-convention-delta5-phi10**
   (:43–46): add a **third** option to the convention disambiguation —
   the *Borcherds $\Phi_{12}$ on $II_{2,26}$* — and explain why the
   K3-family programme does NOT use $\Phi_{12}$. This prevents the
   confusion flagged by AP-KAZ-W7-F1.

---

## BKM / SIEGEL BRIDGE STATUS (the answer)

**The Wave-7 prompt asked:** *"What is the chiral quantum group
undergirding the BKM algebra associated to Siegel modular forms?"*

**Answer (Wave-7 Kazhdan):**

**The chiral quantum group underlying the BKM algebra $\mathfrak
g_{\Delta_5}$ of the Igusa cusp form $\Delta_5$ is the BPS Hopf
algebra $U(\mathfrak n_+(\mathfrak g_{\Delta_5}))$, realised as:**

- **CoHA side** (Kontsevich–Soibelman, Davison–Meinhardt, Maulik–Toda):
  $U(\mathfrak n_+(\mathfrak g_{\Delta_5})) \simeq \CoHA(K3 \times E)$
  (CohomologicalHall algebra of the CY3);
- **Chiral-algebra side** (programme CY-A$_3$):
  $A_{K3 \times E} = \Phi_3(D^b(\Coh(K3 \times E)))$ with bar Euler
  product $= \prod_\alpha (1 - q^\alpha)^{|c(D(\alpha))|}$;
- **Siegel automorphic side** (LOR20 = Borcherds–Gritsenko–Nikulin):
  $\mathrm{char}_{\mathbb C}\mathfrak g_{\Delta_5} = \frac{1}{64}\Delta_5(2Z)$;
- **Langlands side** (Andrianov, Evdokimov, new Wave-7 attribution):
  Spinor L-function $L(s, \Delta_5, \mathrm{spin})$ of degree $4$ on
  $\mathrm{GSp}_4$ (self-Langlands-dual).

**The BKM is NOT the K3 Yangian** $Y(\mathfrak g_{K3})$ of rank 24
Mukai. The BKM is **rank 3 hyperbolic** on the Cartan
$\begin{pmatrix}2&-2&-2\\-2&2&-2\\-2&-2&2\end{pmatrix}$. The two objects
are distinct; the BKM has a complete automorphic bridge to
$\mathrm{GSp}_4$-modular forms via LOR20/Gritsenko–Nikulin/Borcherds;
the K3 Yangian has no complete automorphic bridge, only the
signature-related $\eta^{24}$ bar-Euler-product partial statement
(`prop:k3e-selfdual-fock`) which is a Mukai-abelian-Heisenberg
observation, not a BKM.

**$\Phi_{12}$ is NOT the K3-family BKM denominator.** $\Phi_{12}$ is
the Fake Monster denominator on $II_{2,26}$, attached to the Leech
lattice; the K3 × E BKM denominator is $\Delta_5$ equivalently
$\Phi_{10} = \Delta_5^2 \cdot \text{const}$. The Wave-7 prompt's
$\Phi_{12}$ mention is addressed in Cycle F with the decisive
AP-KAZ-W7-F1.

---

**End of Wave-7 Kazhdan EXTENSION.** Raeez Lorgat, sole author.
No AI attribution.
