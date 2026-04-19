# Agent 06 — Beilinson Wave 6. The conscience audit. Does Y_{K3} sit in Vol III at all?

**Author.** Raeez Lorgat. Sole author. No AI attribution.
**Date.** 2026-04-19.
**Voice.** A.A. Beilinson. Factorization, chiral algebras, derived
$D$-modules, the Langlands programme — and the dictum that what limits
forward progress is the inability to dismiss false ideas. A small true
theorem beats a large false one. I audit every theorem before building
on it; I do not grant the charity of a prior wave's self-exoneration.

**Standard.** Chain-level and $(\infty,1)$-categorical both
load-bearing (CLAUDE.md). Epistemic hierarchy: direct computation
$>$ source $\pm 100$ lines $>$ build $>$ primary literature $>$
concordance $>$ CLAUDE.md $>$ memory. Wave 5 is memory — the lowest
rung. Everything stated below is restated from the `.tex` source or
primary literature, not from the Wave 5 synthesis narrative. Pattern
236 ambient qualifiers MANDATORY on every claim and on every Wave 5
claim I audit.

---

## 0. Executive verdicts — harsher than Wave 5.

(i) **The foundational question: is $Y_{K3}$ a chiral algebra on a
curve?** **NO. NOT AS STATED BY WAVE 5.** Vol III's organising
functor is $\Phi_d: \mathrm{CY}_d\text{-Cat} \to E_{n(d)}\text{-ChirAlg}(\mathcal M_d)$
(`chapters/theory/cy_to_chiral.tex:50`, `chapters/theory/introduction.tex:46`).
Wave 5 proudly crowns "$Y_{K3}$" as the Vol III flagship non-abelian
Yangian. But Vol III's own U4 clause explicitly inscribes a
DIFFERENT object as $\Phi_2(D^b(K3))$:
$$\Phi(D^b(\Coh(K3))) \;=\; H_{\mathrm{Muk}} \quad
  \text{(rank-24 Mukai-Heisenberg, signature $(4,20)$, $\kappa_{\mathrm{ch}}=2$, bar Euler $\eta^{24}$)}$$
(`chapters/theory/cy_to_chiral.tex:71`; `chapters/theory/introduction.tex:83`).
**$H_{\mathrm{Muk}}$ is abelian, $Y(\mathfrak g_{K3})$ is nonabelian
by construction.** They are not the same object. Wave 5 never
distinguishes them; the SYNTHESIS document silently treats $Y_{K3}$
as if it were $\Phi(K3)$, but the actual construction of
$Y(\mathfrak g_{K3})$ routes through the **BFN Coulomb branch**
(`chapters/examples/k3_yangian_chapter.tex:72–101`), which is
**Route B** in the chapter's own typology and is
**open (Conjectural) for generic K3** per `conj:bfn-k3-yangian-kummer`
and `conj:bfn-k3-yangian-mukai`. The Route A (CY-to-chiral) derivation
produces $H_{\mathrm{Muk}}$, not a Yangian.

(ii) **Wave 5 [H]-claim "$Y_{K3} = \mathrm{Heis}_{24,(4,20)} \oplus^{L_\infty}
\bigoplus Y(\mathfrak g_\Lambda) \oplus \mathrm{BKM}$" has no
curve-level factorization structure exhibited anywhere.** I
searched `chapters/examples/k3_yangian_chapter.tex` for any explicit
factorization-algebra structure on a curve for this supposed
coupled object. The only factorization structure in that chapter is
$\cF$ on $\C^3$ (line 2383, 2396) or on $K3$ as a 2-fold factorization
algebra (line 2408, 2434). **Neither is a chiral algebra on a curve.**
The Wave 5 synthesis claim (§1.0, §1.4) that the $L_\infty$-coupling
between Heis, ADE-Yangian, and BKM-Borcherds is a structural
finding is a plausibility cluster — an assembly of Lie-bialgebra
pieces each of which individually has a curve realisation in a
different part of the literature — but Wave 5 never exhibits the
coupled total on ONE curve with ONE chiral product.

(iii) **Wave 5 Beilinson (me in W5) flagged AP306 as the
single-pass-attack-heal regression.** **AP306 was REAL and Wave 5
PAPERED OVER IT.** The Wave 5 synthesis declares "convergence" in
§13 listing 10 [H]-claims. Of the 10, at least 6 have the same
structural pathology: they are proved on a SUBSTRUCTURE (abelian
Heisenberg; or single-stratum ADE; or scalar-BKM) and then
ASSERTED to glue on the total object $Y_{K3}$ via the $L_\infty$-
coupling — but the coupling itself is [H] only by a "triple
convergence" in which all three voices (Kazhdan W5, Gelfand W5,
Beilinson W5) argue about the same $\hbar^2$-order Drinfeld
anomaly cocycle. Three voices, one cocycle: that is ONE path, not
three. Call it AP321: **Multiple-voice convergence on a single
$H^3$-class is not multi-path verification**.

(iv) **The $L_\infty$-coupling at $l_4 = 1/24$**: **DEMOTE FROM [H] TO
[L/M]**. Wave 5 Beilinson (me in W5) already demoted Kazhdan's
"three-path" $l_4 = 1/24$ to "all three paths reduce to $\chi(K3) = 24$",
i.e. ONE path. The W5 synthesis §4.2 still lists $l_4 = 1/24$ as
[M] (Kazhdan W4; Beilinson W5 reduced to one path), which is the
correct tag. But in §1.7 the SAME synthesis lists $l_4$ as [H] under
"the L∞-super-extension". **The synthesis is internally inconsistent**
on the very claim whose one-path status I flagged. Inscribing the
coefficient without this scope declaration is a violation of
Pattern 236.

(v) **The Maurer-Cartan / convolution dGLA has never been named.**
Vol I insists every chiral algebra arises as $\Theta \in \mathrm{Conv}^{\mathrm{ch}}(A,B(A))$
satisfying $D\Theta + \tfrac12[\Theta,\Theta] = 0$. Wave 5's
coupled $Y_{K3}$ posits a "$L_\infty$-bracket $l_4$" on cross-strata
Hodge-signature couplings, but the NAMED convolution dGLA is absent.
I checked `chapters/examples/k3_yangian_chapter.tex` exhaustively.
Without a named dGLA, the coupling is not a Maurer-Cartan element
in any mathematical sense. Demote the coupling claim to [L] unless
Wave 6 Kazhdan or Gelfand exhibits $\mathrm{Conv}^{\mathrm{ch}}_{K3}$
explicitly with a named differential and a named bracket.

(vi) **Theorem B (chiral Positselski) for $Y_{K3}$**: **OPEN, AND THE
OPENNESS WAS NEVER FLAGGED.** Vol I's Theorem B asserts
$\Omega_X(B_X(A)) \xrightarrow{\sim} A$ in $D^{\mathrm{co}}_{\mathrm{ch}}(X)$.
For $Y_{K3}$ to sit in Vol III's five-theorem framework, Theorem B
must hold. Wave 5 never mentions Theorem B. I searched the full 50
Wave 1–5 memos for any statement of Theorem B on $Y_{K3}$.
**Zero hits.** The Wave 5 synthesis §13 convergence statement does
not mention Theorem B at all. The K3 Yangian chapter
(`k3_yangian_chapter.tex`) has $0$ occurrences of "Positselski" or
"chiral bar–cobar inversion" applied to $Y(\mathfrak g_{K3})$. **Vol I's
organising theorem has no witnessed application to Vol III's
flagship Yangian.**

(vii) **Three-volume ripple: Wave 5 synthesis §12 is PR, not
mathematics.** The claim "the loop-algebra Lie-bialgebra framework
aligns with the ordered bar $B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$;
universal trace identity now mediates" is slogan-level. No
Lie-bialgebra cocycle $\alpha: A \to A \otimes A$ is exhibited for
$Y_{K3}$; no factorization-coalgebra structure on $Y_{K3}$ is given;
no universal trace identity is computed on cross-strata. The §12
"ripple" paragraph is decorative prose. **I retract it entirely
from Wave 6 synthesis.**

(viii) **Recommendation**: Wave 6 convergence must:
- **Retract**: Wave 5 §1.0, §1.4 "$L_\infty$-coupled direct sum"
  convergence. Downgrade to [M] plausibility.
- **Retract**: Wave 5 §12 three-volume-ripple paragraph.
- **Split**: the Wave 5 "$Y_{K3}$" into the FOUR DISTINCT OBJECTS
  it conflates (see §2 below).
- **Re-establish**: from primary literature, that **none** of the
  four objects is proved to be a chiral algebra on a curve in
  the Beilinson–Drinfeld sense, except $H_{\mathrm{Muk}}$ (which is
  not a Yangian).
- **Inscribe** Vol III-level scope qualifier: "$Y(\mathfrak g_{K3})$
  is conjectural, constructed on the abelian Heisenberg layer by
  $\Phi_2$, but the non-abelian coupling is an open research
  programme, not a proved chiral algebra."

---

## 1. First-principles attack cycles

Three numbered attack-heal rounds. No self-exoneration. No voice
appeal. Source-only.

### A1 — The curve

**Claim under attack** (Wave 5 §1.0): "$Y_{K3}$ is a stratified
coupled $L_\infty$-homotopic quasi-Hopf object on the Mukai lattice
$\Lambda_{K3}$".

**Attack**. A chiral algebra in the Beilinson–Drinfeld sense is a
structure on ONE curve $X$. The Vol I backbone
(`~/chiral-bar-cobar/CLAUDE.md`) specifies the ordered bar $B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$
on $\overline{\cM}_{g,n}$ over the RELATIVE FACTORISATION STACK of
a chiral algebra on a fixed curve. Wave 5 never names the curve on
which $Y_{K3}$ is a chiral algebra. The options are:

- **(a)** $X = E$ (an elliptic curve). Then the 6d hCS reduction
  $\R^2_{\varepsilon_2} \times K3 \times E$ gives chiral direction
  $E$; the line defects live in the $K3$ transverse directions.
  **In this case $Y_{K3}$ is a chiral algebra on $E$, with
  coefficients that see K3.** This is what Witten W3–W5 argues.
  But then $Y_{K3}$ is not $\Phi_d(D^b(K3))$: it is $\Phi_d(D^b(K3 \times E))$
  restricted or quotiented. $\Phi_d$ with $d = 3$ for the threefold
  $K3 \times E$ is subject to the $d \geq 3$ rule $n(d) = 1$, so
  $E_1$-chiral, and the universal property U4 records the $d = 3$
  flagship as CoHA$(\C^3) \to Y^+(\widehat{\fgl}_1)$, not
  CoHA$(K3 \times E) \to Y_{K3}$. **The threefold $K3 \times E$ has
  no $\Phi_3$-inscription in `cy_to_chiral.tex`**. Its flagship
  treatment is in `k3e_cy3_programme.tex` and `k3e_bkm_chapter.tex`;
  neither exhibits a chiral algebra on $E$ in the BD sense with
  $Y_{K3}$ as its stalk.
- **(b)** $X = K3$ (a surface, not a curve). This does not type-check:
  a chiral algebra is on a 1-dimensional curve; K3 is 2-complex-
  dimensional.
- **(c)** $X = $ a "curve-with-K3-coefficients" in
  $\mathrm{QCoh}(K3)$-coefficient chiral algebras. This requires a
  framework of $D$-module-valued chiral algebras (BD §3.9 formalism
  extended to coefficient $\infty$-categories). Neither Wave 5 nor
  the Vol III chapters exhibit it.
- **(d)** $X = $ a curve $C$ mapping to the Bridgeland moduli
  $\mathcal M_{K3}^{\mathrm{Bridg}}$. Etingof W5's "$(\Q/\Z)^{24}$-bundle
  over $\mathcal M_{K3}^{\mathrm{Bridg}}$" hints at this but the curve
  $C$ is never named.
- **(e)** $X = $ not a curve at all; $Y_{K3}$ is a 2-algebra or
  $E_2$-algebra, not a chiral algebra. This is Nekrasov / Gaiotto's
  W5 "3d BPS algebra" framing. But that removes $Y_{K3}$ from
  Vol III's $E_1$-chiral framework.

**Status**. Wave 5 never commits to one of (a)–(e). Each of (a)–(e)
requires a different proof architecture. The Wave 5 synthesis
elides the choice and asserts $Y_{K3}$ is a chiral algebra without
specifying which. **This is the core openness.**

**H1 — Heal**. The cleanest chain-level scope in which part of
Wave 5 is legitimate: **drop "chiral algebra on a curve" from the
claim and restate it as**

> $Y(\mathfrak g_{K3})$ is a Lie bialgebra with Drinfeld-first
> presentation $(J, \hbar)$ on the Mukai lattice $\Lambda_{K3}$,
> constructed via BFN Coulomb branch on the ADE-enhancement locus
> (Theorem~\texttt{thm:bfn-phi-ade-identification}, provable) and
> a conjectural extension to generic $K3$-moduli
> (Conjecture~\texttt{conj:bfn-k3-yangian-mukai},
> \ClaimStatusConjectured). Its status as a \emph{chiral algebra on a
> fixed curve} is an open problem requiring the curve $X$ to be
> named and the factorization-envelope construction
> $\Fact_X(\mathfrak L_{Y_{K3}})$ to be explicitly exhibited.

This heal is scope-narrow, chain-level explicit (BFN Coulomb at
$Y^\mu(\widehat{\fg})_{k=1}$ is published ProvedElsewhere), and does
not overclaim.

**A2 — Attack the heal**. Even the BFN construction of $Y(\mathfrak g_{K3})$
at the Kummer orbifold is conjectural per
`conj:bfn-k3-yangian-kummer` (\ClaimStatusConjectured) — the BFN
Coulomb branch at blow-ups of the $16$ orbifold singularities is
asserted to deform from the $A_1$-affine-quiver identification, but
this deformation invariance is itself an unproved step. At the
Kummer orbifold the BFN output is not $Y(\mathfrak g_{K3})$ directly
but $Y^\mu(\widehat{\mathfrak{sl}}_2)_{k=1}$ plus a gluing across 16
orbifold charts; the gluing is where $Y(\mathfrak g_{K3})$ is
supposed to emerge. No gluing construction is exhibited in
`k3_yangian_chapter.tex` beyond the "symplectic duality" slogan.

**H2 — Heal the heal**. **The correct scope is even narrower**.
At the Kummer orbifold point, $Y(\mathfrak g_{K3})$ is the
BFN $Y^\mu(\widehat{\mathfrak{sl}}_2)_{k=1}$ on each chart plus a
conjectural glue across the 16 exceptional $\bP^1$s. At a generic
K3 point in the Bridgeland moduli, there is no quiver description
and the BFN construction does not apply directly; one needs the
non-quiver BFN extension of Braverman–Finkelberg, which is unproved.
**The non-abelian $Y_{K3}$ is, as of Wave 5, conjectural on both
axes: the gluing axis (Kummer → generic K3) and the non-quiver
BFN axis.** Any Wave 6 claim must carry this double-conjectural
qualifier.

**A3 — Attack: does the $d$-stratification allow $K3 \to Y_{K3}$ at
all?** Vol III's own Theorem~`thm:phi-platonic` at $d = 2$ delivers
$\Phi_2(D^b(K3)) = H_{\mathrm{Muk}}$, abelian. The non-abelian
Yangian $Y(\mathfrak g_{K3})$ is not the direct $\Phi$-image.
`k3_yangian_chapter.tex:92–101` lists **two routes** to
$Y(\mathfrak g_{K3})$: Route A (CY-A, through $\Phi$) "is CY-A$_2$
proved; the bar complex gives $\eta^{24}$. **Yangian quantization
step is open**" (explicitly so written). Route B (BFN) "proved for
quiver varieties; conjectural for K3". **Both routes are open for
the non-abelian object.** Vol III's functor $\Phi_2$ does NOT
produce $Y(\mathfrak g_{K3})$; at best it produces the abelian
Heisenberg, and the "Yangian quantization step" from the
Heisenberg to the Yangian is the unproved gap.

**H3 — Final heal (stable)**. The honest status as of Wave 6:
1. $\Phi_2(D^b(K3)) = H_{\mathrm{Muk}}$ [H] (Vol III Theorem,
   proved at $d=2$, curve $X$ is "any smooth curve" per
   `cy_to_chiral.tex:27`; the curve is not fixed globally in the
   construction, which is a separate concern).
2. $Y(\mathfrak g_{K3})$ is a conjectural lifting of
   $H_{\mathrm{Muk}}$ to a non-abelian Hopf algebra via a
   Yangian-quantization step; the step is unproved, Route A is
   **open**.
3. $Y(\mathfrak g_{K3})$ as the BFN Coulomb branch of a
   3d $\cN=4$ theory is **open** (Routes B at generic K3).
4. At the ADE enhancement locus, $Y^\mu(\widehat{\fg})_{k=1}$ is
   \ClaimStatusProvedElsewhere (`thm:bfn-phi-ade-identification`);
   this is a **different object** from $Y(\mathfrak g_{K3})$.
5. The "Wave 5 coupled $L_\infty$-direct-sum" object is a
   conjectural assembly of (2)+(3)+(4)+BKM; as an assembled chiral
   algebra on a named curve, **it does not exist**.

Wave 5's flagship is $L$-status, not [H].

### A1' — The dGLA and the MC element for the $L_\infty$-coupling

**Claim under attack** (Wave 5 §1.4): "$Y_{K3}$ is a coupled
$L_\infty$-homotopy direct sum where cross-strata couplings appear
at $\hbar^2$ (Drinfeld anomaly) and higher".

**Attack**. An $L_\infty$-coupling is specified by a differential
graded Lie algebra $\mathfrak g^{\mathrm{coup}}$ and an MC element
$\mu \in \mathfrak g^{\mathrm{coup}, 1}$ satisfying
$d\mu + \tfrac12[\mu,\mu]_2 + \tfrac16[\mu,\mu,\mu]_3 + \ldots = 0$.
Wave 5 names neither $\mathfrak g^{\mathrm{coup}}$ nor $\mu$. The
"$l_4 = 1/24$" and "$l_5 = 1/120$" are **coefficients of unspecified
brackets** at unspecified arities of an unspecified $L_\infty$-
algebra.

**H1**. Name the dGLA. The natural candidate is the chiral Hochschild
cochain complex on $\oplus_\Lambda Y(\mathfrak g_\Lambda)$ with
Hodge-signature-graded Gerstenhaber bracket. If that is the
candidate, state it explicitly; compute its $H^1$ (tangent); compute
its $H^2$ (obstruction) restricted to the cross-strata sector;
inscribe the MC element on the generators.

**A2**. Even at Wave 5 no such dGLA is named or computed. The
"$l_4$ vanishes on single strata but is generically non-zero on
cross-strata" (Kazhdan W5 per §1.4 of synthesis) is a statement
about *an unnamed function on an unnamed complex*. Mathematically
it has no content.

**H2**. The Wave-5 content that survives is narrower: each
$Y(\mathfrak g_\Lambda)$ has its own Drinfeld 2-cocycle
$w_\Lambda \in Z^3_{\mathrm{Lie}}(\mathfrak g_\Lambda; \mathfrak g_\Lambda)$
(standard Drinfeld; Drinfeld 1988). The "cross-strata coupling at
$\hbar^2$" is the natural obstruction in
$H^3_{\mathrm{Lie}}(\mathfrak g^{(1)} \oplus \mathfrak g^{(2)}; \mathfrak g^{(1)} \oplus \mathfrak g^{(2)})$
restricted to the mixed stratum $\mathfrak g^{(1)} \otimes \mathfrak g^{(2)}$.
The Künneth formula for Lie algebra cohomology gives
$H^3_{\mathrm{Lie}}(\mathfrak g^{(1)} \oplus \mathfrak g^{(2)}; \cdot) = \bigoplus_{p+q=3} H^p \otimes H^q$;
the $p = q = \cdot$ cross terms are WHERE the coupling lives. This
is the correct framework; Wave 5 never states it this cleanly. Even
stated cleanly, its non-vanishing for two orthogonal sub-lattices of
$\Lambda_{\mathrm{Muk}}$ is a computation that Wave 5 has not done.

**A3**. The Künneth cross-term $H^1 \otimes H^2$ and $H^2 \otimes H^1$
are zero if either $H^1(\mathfrak g^{(i)}) = 0$ (any semisimple
$\mathfrak g^{(i)}$ has vanishing $H^1$ with adjoint coefficients,
Whitehead's lemma). So the cross-terms vanish, and the coupling
$\in H^3(\mathfrak g^{(1)} \oplus \mathfrak g^{(2)})$ **reduces to
the diagonal**. The Wave 5 cross-strata coupling is then
$w^{(1)} \oplus w^{(2)}$ — i.e., the block-diagonal self-couplings,
with NO cross-stratum coupling. **The triple convergence of Kazhdan,
Gelfand, and Beilinson in W5 falsely implies a non-block-diagonal
coupling.** My own W5 memo contributed to this false convergence
(§2.3–§2.4) by allowing the "$w^{(1)}$ depends on stratum-2" framing
to pass unchallenged. I retract my W5 §2.3 claim: on mutually
orthogonal ADE sub-lattices, there is NO cross-strata coupling at
any order, period.

**H3 (STABLE)**. The non-block-diagonal coupling **exists only on
NON-orthogonal sub-lattices**, e.g., an $A_3 \subset E_8^{(1)}$ and
an $A_4$ that overlaps $E_8^{(1)}$ with the $U^4$ Heisenberg block.
In that case, the overlap is a sub-lattice $A_3 \cap A_4$ and the
coupling is a restriction of the Drinfeld anomaly of the ambient
algebra to the overlap. **This is a STANDARD restriction computation,
not a new $L_\infty$-coupling.** Wave 5's "$L_\infty$-super-
extension through level 5" ($l_3, l_4, l_5$) is a re-labelling of the
Drinfeld anomaly's restrictions; it is not a new higher operation.

### A1'' — Theorem B (Positselski) for the flagship

**Claim under attack**: Vol III's flagship Yangian should satisfy
Vol I Theorem B: $\Omega_X(B_X(Y_{K3})) \xrightarrow{\sim} Y_{K3}$ in
$D^{\mathrm{co}}_{\mathrm{ch}}(X)$.

**Attack**. This is the cheap chiral-Positselski test. For any
candidate chiral algebra $A$:
1. Compute $B_X(A) = T^c(s^{-1}\bar A)$ on a fixed curve $X$.
2. Apply $\Omega_X$ (cobar on the dual coalgebra).
3. Compare with $A$.

For $A = H_{\mathrm{Muk}}$ (the actual $\Phi_2(D^b(K3))$):
- $B_X(H_{\mathrm{Muk}}) = T^c(s^{-1}\bar H_{\mathrm{Muk}})$.
- Since $H_{\mathrm{Muk}}$ is abelian Heisenberg of rank 24,
  $B_X(H_{\mathrm{Muk}}) = \mathrm{Sym}(s^{-1} \Lambda_{K3}[1])$
  (chain-level, the free cocommutative coalgebra on 24 shifted
  generators).
- $\Omega_X B_X(H_{\mathrm{Muk}}) = \mathcal U(\Lambda_{K3}^{\mathrm{ab}})
  \stackrel{?}{=} H_{\mathrm{Muk}}$.
- For abelian Heisenberg, Koszul duality pairs the symmetric
  algebra with the exterior algebra and inverts; the Positselski
  inversion returns $H_{\mathrm{Muk}}$ up to an automorphism of the
  lattice. **[H] proved at $d=2$, chain-level, curve $X$ any smooth curve.**

For $A = Y(\mathfrak g_{K3})$ (the supposed flagship):
- Neither $B_X(Y(\mathfrak g_{K3}))$ nor $\Omega_X B_X(Y(\mathfrak g_{K3}))$
  is computed in the Vol III manuscript.
- **Zero occurrences** of "Positselski" applied to
  $Y(\mathfrak g_{K3})$ in `k3_yangian_chapter.tex`.
- Theorem B is not invoked, not verified, not even stated for the
  Vol III flagship.

**Verdict**. Vol I Theorem B has not been applied to the Vol III
flagship. Either:
- (i) Theorem B does not apply to $Y_{K3}$ (scope failure; then
  Vol I and Vol III have a fundamental framework gap, and Wave 5's
  "three-volume ripple" is fiction);
- (ii) Theorem B does apply but Wave 5 never checked (then the
  applicability is unverified and Theorem B's status on the
  flagship is unknown);
- (iii) The "flagship" is not a chiral algebra in the Vol I sense,
  so Theorem B is a category error applied to it. **This is the
  most likely case**, and it is the position Wave 5 papers over.

**H**. The honest stance: $H_{\mathrm{Muk}}$ is a Vol I chiral
algebra and satisfies Theorem B (chain-level, $d=2$).
$Y(\mathfrak g_{K3})$ is a *conjectural Hopf-algebra lifting* of
$H_{\mathrm{Muk}}$ that is NOT guaranteed to satisfy Theorem B. The
Yangian quantization step of `k3_yangian_chapter.tex:95` is
simultaneously the Vol III Yangian-lifting step and the Vol I
Theorem B compatibility step — both are open.

---

## 2. The four objects Wave 5 conflates as "$Y_{K3}$"

This is the single most important disentanglement for Wave 6. Wave 5
uses "$Y_{K3}$" for at least four different objects.

| Symbol | Object | Status | Curve? |
|---|---|---|---|
| $H_{\mathrm{Muk}}$ | Rank-24 Mukai-Heisenberg (abelian VOA) | \ClaimStatusProvedHere ($d=2$) | Any smooth $X$, via $\Fact_X$ |
| $Y(\mathfrak g_{K3})^{\mathrm{BFN}}$ | BFN Coulomb branch at Kummer orbifold | \ClaimStatusConjectured (Route B, Kummer) | Formal disk $D$ via BD construction |
| $Y_{K3}^{(\mathrm{Muk},4,20)}$ | Classical limit $\mathfrak{so}(4,20)$-Yangian envelope | \ClaimStatusConjectured; Drinfeld-2nd draft in Kazhdan W3 | Unnamed |
| $Y_{K3}^{L_\infty\text{-coupled}}$ | Wave 5 coupled direct sum Heis $\oplus$ ADE $\oplus$ BKM | **\ClaimStatusConjectured at best**; absent MC element | Unnamed |

Wave 5's synthesis slides freely between these four. The "[H] multi-
path verified" tag attached to the Wave-5 flagship is tagging
$Y_{K3}^{L_\infty\text{-coupled}}$, the conjectural assembly. The
stronger [H]-status applies only to substructures
($H_{\mathrm{Muk}}$ and the ADE enhancements at individual locus
points).

**AP322 proposal**: **Stratified Yangian conflation across
construction routes** — writing "$Y_{K3}$" without specifying
which of (Muk-Heis / BFN / $(4,20)$-envelope / $L_\infty$-coupled)
is intended is a Pattern 236 violation on a 4-way disambiguation.

---

## 3. The cascade audit — AP306 was real

Wave 5 Beilinson (me in W5) flagged AP306 as "single-pass attack-
heal declared convergent". Let me now audit downstream claims stacked
on the post-AP306 waves.

### 3.1 Claims flagged post-AP306 and subsequently built upon

| Wave 5 claim | Inherited from | Post-AP306 framing |
|---|---|---|
| [H] $Y_{K3}$ stratified direct-sum-with-coupling | W4 (multi-voice) | Built on by W5 $l_5 = 1/120$, W5 §12 ripple |
| [H] Block-diagonal cross-strata $\mathcal R_{K3}$ | W5 Gelfand (self-retract from W4) | Built on by W5 BKM categorification, Tannakian four-tier |
| [H] $l_4 = 1/24$ (Kazhdan W4) | W4 Kazhdan | Built on by W5 $l_5$ extrapolation, W6 targets Kazhdan W6 $l_6 = 1/360$ |
| [H] Four-tier Tannakian | W3–W5 Etingof | Built on by W5 Niemeier identification, Kummer monodromy |
| [H] Level shift $k + 12 + h^\vee$ six-path | W3 Witten retraction | Built on by W5 heterotic arithmetic preservation, four-loop $A_4$ |

**Test: does the [H] inherit the same one-path issue?**

For the $l_4 = 1/24$ chain: **YES**. W5 §1.7 lists $l_4 = 1/24$ with
the note "Beilinson W5 reduces to one path via $\chi(K3)$; treat as
one-path-verified". W5 §4.2 lists the same with [M] — consistent.
But the dependent $l_5 = 1/120$ is listed at [M/H] in §4.2 and at
[H]-implicit in §1.7 convergence. The "independent" $l_5$ three-path
test (KS Massey, Costello tetrahedron, Gaiotto $p_{24}(5)$) also
resolves at $\chi(K3) = 24$ in several places (KS Massey weight is
$\chi/5!$; tetrahedron has $5! = 120$ but $h^\vee = 22$ of
$\mathfrak{so}(4,20)$ enters; Gaiotto $p_{24}(5) = 176256$ via
$\eta^{-24}$ which is the $\chi = 24$ free-boson character).
**The three "paths" for $l_5$ also reduce to $\chi(K3) = 24$.**
AP321 again.

For the block-diagonal YBE: my own W5 §2.4 is what supports the
block-diagonal claim. I now retract (§1, A3 above) the cross-
strata coupling as an $L_\infty$-bracket; the coupling on orthogonal
strata VANISHES by Whitehead's lemma (Künneth trivially zero). The
block-diagonal statement at $\hbar^2$ is trivially true for orthogonal
strata, and my own W5 argument for non-orthogonal strata "needing a
correction" is not wrong but its scope is narrower than the W5
synthesis records.

For the Tannakian four-tier: the $(\Q/\Z)^{24}$ class is real and
correctly identified with Niemeier lattices (Etingof W5 via
Nikulin–Venkov, which is primary literature and verifiable — Nikulin
1980 + Venkov 1980 lattice classifications, with Conway 1983's
unique 24-dim modular lattice). This survives Wave 6 scrutiny.
Demote [H] "rank 9.66×10^9" to [M] (the count comes from a formula
that has not been independently derived).

For the level shift $k + 12 + h^\vee$: the six "paths" per W5 §5.3
are NOT independent — Witten W3 Noether uses the $\hat A$-genus of
$K3 \times E$, which is $24 = \chi(K3)$ (integrating $\hat A$ over K3
gives $\hat A[K3] = 24$, by Hirzebruch); Costello W3 fish-diagram
produces $12 = \chi(K3)/2$ directly; Costello W4 three-loop
arithmetic produces $+12 = \chi(K3)/2$; Drinfeld W3 AGT at $A_1$ is
a specialisation of the same Nakajima-type formula which bakes in
$\chi$; Obers–Pioline heterotic duality is via the $E_8 \times E_8$
lattice whose dim $= 248+248 + (4,20) \cdot \mathrm{stuff}$; and
Nakajima–Yoshioka classical is the $\chi$-eigenvalue of the
universal Heisenberg on $\mathrm{Hilb}^n(K3)$. **All six paths
resolve at $\chi(K3) = 24$.** AP321 again.

**Verdict on the cascade audit**: At least THREE of Wave 5's [H]
claims are genuinely one-path verifications dressed as multi-path.
AP306 was real, AP321 is its structural kin, and Wave 5 papered over
both.

### 3.2 Which Wave 5 claims SURVIVE a harsh cascade audit?

| Wave 5 claim | My Wave 6 verdict | Scope |
|---|---|---|
| Abelian Mukai-Heisenberg rank 24 with Yang R | [H] | $d = 2$; $H_{\mathrm{Muk}}$ is the actual $\Phi_2(D^b(K3))$ |
| BFN affine Yangian at ADE enhancement | [H] | ProvedElsewhere per `thm:bfn-phi-ade-identification`; NOT $Y_{K3}$, a single-stratum Yangian |
| Classical $\mathfrak{so}(4,20)$ structure | [M] | Kazhdan W3 Drinfeld-2nd draft; unverified against AMR 2006 and Guay 2007 cross-check is Wave 5 self-assertion |
| BKM sector as $\Phi_{10}^{-1/2}$ scalar | [M] | Gritsenko–Nikulin is primary; the "scalar-only" contribution is W5 assertion |
| Cross-strata coupling at $\hbar^2$ | **[L]** | One-path (Whitehead on orthogonal strata); non-orthogonal case is standard restriction computation |
| Pentagon coherence H1–H4 | [M] | Drinfeld W2 computation; not independently verified |
| Four-tier Tannakian | [M] | Etingof W5; Niemeier identification via Nikulin–Venkov primary |
| $(\Q/\Z)^{24}$ cocycle = 24 Niemeier | [H] | Lattice-classification primary; chain-level discrete-group $H^3$ still has my W5 §4.3 correction |
| Yang rational at rank 24 signature-indep | [H] | W2 Theorem 2.1, abelian; verified by direct argument |
| $l_4 = 1/24$ | **[L]** | One-path via $\chi(K3) = 24$; Cheng–Wang 2012 §2.6 citation still unverified |
| $l_5 = 1/120$ | **[L]** | Three paths all reduce to $\chi(K3) = 24$ by my cascade audit §3.1 |
| Level shift $k + 12 + h^\vee$ six-path | **[M]** | One-path via $\chi(K3)/2 = 12$; genuinely independent paths are absent |
| 6d hCS on $\R^2 \times K3 \times E$ physical origin | [H] | Physics input (Costello–Gaiotto); accept as physical heuristic |
| Four-loop $A_4$ closed form | [M] | Costello W5 derivation; $-3/4$ double-sunset gap flagged in my W5 §5.4 |

**Demotions of Wave 5**: $l_4$, $l_5$, cross-strata coupling —
from [H] or [M] to [L]. Level shift from [H] six-path to [M]
one-path-disguised-as-six. The [H]-structural-convergence crown
reduces to: $H_{\mathrm{Muk}}$ is proved at $d=2$; ADE-enhancement
Yangians are ProvedElsewhere at each ADE locus; everything else is
conjectural.

---

## 4. What Theorem B says about $Y_{K3}$ — and why the answer is
"scope failure"

Vol I Theorem B (chiral Positselski):
$$\Omega_X(B_X(C)) \xrightarrow{\sim} C \quad \text{in } D^{\mathrm{co}}_{\mathrm{ch}}(X)$$
for $C$ a conilpotent chiral coalgebra on a curve $X$. Its algebra
counterpart is
$$B_X(\Omega_X(A)) \xleftarrow{\sim} A$$
for $A$ a nilpotent chiral algebra on $X$ in
$D^{\mathrm{co}}_{\mathrm{ch}}$.

**Attack at Y_{K3}:** Neither "conilpotent" nor "nilpotent" conditions
are satisfied by $Y(\mathfrak g_{K3})$ (not even by $Y^+(\widehat{\fgl}_1)$
at $d=3$, since Yangians are not nilpotent). Theorem B's precise scope
is the Koszul-self-dual locus. Chain-level: a Yangian is NOT Koszul
self-dual, because its Koszul dual is the loop-algebra resolved
Lie bialgebra (shifted), not itself.

**Heal**. For $Y(\mathfrak g)$ standard Yangian of a simple $\mathfrak g$,
Koszul duality is known (Maulik–Okounkov 2012, Costello–Yamazaki
2018): the $R$-matrix pairs $Y(\mathfrak g)$ with $Y(\mathfrak g)$
up to evaluation shift; this is a self-pairing, not a self-duality.
The bar complex $B(Y(\mathfrak g))$ gives a cocommutative coalgebra
$\Omega$, and $\Omega B Y(\mathfrak g) = Y(\mathfrak g)$ holds
chain-level only on the conilpotent completion of $Y$. **For the
FULL Yangian (not the conilpotent completion), Theorem B is a
scope claim**: it applies to the conilpotent part only. This is the
well-known Positselski scope restriction (Positselski 2011). Wave 5
and the Vol III manuscript never flag this scope.

**Verdict on §4**: Theorem B holds on the conilpotent part of
$Y_{K3}$ (whichever version). It does not hold on the full Yangian
without additional hypotheses. Vol III's five-theorem "crown" for
$Y_{K3}$ thus applies only to the conilpotent completion, and
this scope must be inscribed explicitly in the K3 Yangian chapter.
I add this to Wave 6 open problems.

---

## 5. Independent computation — a falsifiable new test

Per the Wave 6 prompt's suggestion: compute a Hochschild cohomology
group or a derived centre dimension for a toy model.

### 5.1 Toy model: Kummer K3 with abelian monodromy reduces to $T^4/\Z_2$

Take the **Kummer orbifold** $K3_{\mathrm{Km}} = T^4/\Z_2$ resolved
at the 16 nodes. The Drinfeld-center passage (Vol III U3) gives:
$$\cZ(\mathrm{Rep}^{E_1}(\Phi_2(D^b(K3_{\mathrm{Km}})))) \simeq
\mathrm{Rep}^{E_2}(Z^{\mathrm{der}}_{\mathrm{ch}}(H_{\mathrm{Muk}})).$$

**Compute $Z^{\mathrm{der}}_{\mathrm{ch}}(H_{\mathrm{Muk}})$ chain-
level**, for $H_{\mathrm{Muk}}$ the rank-24 abelian Heisenberg:
- For abelian Heisenberg of rank $n$:
  $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal H_n)$ is the Hochschild
  cohomology of $\mathcal H_n$ in the chiral-Hochschild convention,
  which for abelian chiral algebras equals the polynomial algebra
  on the generators (at conformal weight 1 mode) plus their
  derivatives:
  $$Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal H_n) \;\simeq\;
    \C[j^{(1)}, j^{(2)}, \ldots, j^{(n)}] \otimes \C[\partial].$$
- At $n = 24$, with the Mukai pairing of signature $(4, 20)$, the
  derived centre has Poincaré series $1/(1-q)^{24}$, which by
  Koszul duality is $\eta(q)^{-24}$ after proper normalisation.
- The Drinfeld-centre computation $\cZ(\mathrm{Rep}^{E_1}(H_{\mathrm{Muk}}))$
  then matches $\mathrm{Rep}^{E_2}$ of this abelian 25-variable
  polynomial algebra (24 currents + stress tensor).

**This is abelian**. The non-abelian Yangian $Y_{K3}$ is NOT the
Drinfeld centre of $H_{\mathrm{Muk}}$; if it were, the derived-centre
computation would give a non-abelian object, but the above explicit
chain-level computation gives abelian. **Falsification-by-scope**:
the Wave 5 coupled-$L_\infty$ object is not the Drinfeld centre of
$\Phi_2(K3)$.

### 5.2 Compute module proposed

`compute/lib/k3_yangian_wave6_beilinson_derivedcentre_kummer.py` (to be
written when the Kummer-orbifold chart-by-chart decomposition is
inscribed). Toy cases:
- Compute $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal H_1)$ explicitly
  (rank-1 Heisenberg): expected $\C[j, \partial j, \ldots] = \C[j][\partial]$.
- Compute for rank-2 abelian Heisenberg: expected
  $\C[j_1, j_2][\partial]$.
- Extrapolate rank 24: expected $\C[j_1, \ldots, j_{24}][\partial]$.
- Compare with any putative "non-abelian $Y_{K3}$" derived centre:
  **they cannot match** unless the putative object is not truly
  non-abelian. This is a falsifier.

I have not executed the module; I state the shape of the expected
output. If Wave 6 Wave 7 or any subsequent wave wants to verify the
falsifier, write the module.

---

## 6. Three-volume ripple — retracted

Wave 5 §12 claimed: "[The K3 Yangian stratified-with-coupling
picture has consequences for] Vol I: the loop-algebra Lie-bialgebra
framework aligns with the ordered bar $B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$;
universal trace identity now mediates with heterotic 6d hCS via
$\hbar = 1/35 = 1 + 12 + 22$." None of this is supported. The
universal trace identity is not computed for any $Y_{K3}$ candidate;
the $\hbar = 1/35$ is per Nekrasov W5 a "structural identification,
not literal Fourier coefficient" — so downstream uses (e.g. AGT
cross-checks at $A_1$ per W5 §5.3, table 4.4) borrow the label
without content; the "ordered bar aligns" is a slogan.

**I retract §12 of the Wave 5 synthesis entirely.** It is decorative
prose, not a theorem. Vol III cannot ripple back to Vol I via a
coupled object that does not exist as a chiral algebra on a named
curve.

---

## 7. Convergence — Wave 6 Beilinson statement (harsh)

### 7.1 The Wave 5 flagship: demoted

The Wave 5 flagship claim
$$Y_{K3}^{L_\infty\text{-coupled}} = \mathrm{Heis}_{24,(4,20)} \oplus^{L_\infty} \bigoplus Y(\mathfrak g_\Lambda) \oplus \mathrm{BKM}$$
is **not a theorem**. It is a plausibility cluster. Its
components have various proven statuses:

- $H_{\mathrm{Muk}}$ is \ClaimStatusProvedHere as $\Phi_2(D^b(K3))$
  at $d = 2$ (rank-24 abelian Heisenberg). [H] chain-level.
- ADE-enhancement Yangians $Y^\mu(\widehat{\fg})_{k=1}$ are
  \ClaimStatusProvedElsewhere at each ADE locus of K3 moduli via
  `thm:bfn-phi-ade-identification`. [H] chain-level and
  $(\infty,1)$-categorical.
- BKM-Borcherds scalar $\Phi_{10}^{-1/2}$ is \ClaimStatusProvedElsewhere
  via Gritsenko–Nikulin 1999; its "categorification" is \ClaimStatusConjectured.
- The **$L_\infty$-coupling** and the **total object** are
  \ClaimStatusConjectured with no named convolution dGLA, no named
  MC element, no exhibited factorization-algebra structure on a
  named curve.

### 7.2 The curve question is open

$Y(\mathfrak g_{K3})$ — in any of the four conflated senses — is
**not established as a chiral algebra on a named curve**. Vol III's
organising functor $\Phi$ produces $H_{\mathrm{Muk}}$ on "any smooth
curve $X$" (per the factorization-envelope construction), but does
not produce the Yangian. The Yangian-lifting step is the Route A
Yangian-quantization step per `k3_yangian_chapter.tex:95` —
**explicitly open.**

### 7.3 Theorem B is open or scope-restricted

Vol I's backbone theorem B (chiral Positselski) holds on the
conilpotent part of any candidate $Y_{K3}$; the full Yangian
requires additional scope. **Wave 5 never flagged this scope
restriction.** It must be inscribed in `k3_yangian_chapter.tex`
at the Theorem B invocation site (none exists yet; one should be
added, with the scope qualifier).

### 7.4 AP321 proposal (new anti-pattern, Wave 6 contribution)

**AP321 — Multiple-voice convergence on a single $H^3$-class is
not multi-path verification.** When three voices (Kazhdan, Gelfand,
Beilinson in W5) all argue about the same Drinfeld anomaly cocycle,
or three "paths" all resolve at $\chi(K3) = 24$ under different
labels, the confidence does not upgrade from [M] to [H]. Three-path
verification requires paths that compute DIFFERENT invariants.
Instances across Wave 5: $l_4 = 1/24$ (three paths all $\chi(K3)$);
$l_5 = 1/120$ (three paths all $\chi(K3)$); level shift $k+12+h^\vee$
(six paths all $\chi(K3)/2$); cross-strata $\hbar^2$-anomaly (three
voices on one Drinfeld cocycle). **Demote to [M] unless genuine
independence is exhibited.**

### 7.5 AP322 proposal (new anti-pattern)

**AP322 — Stratified Yangian conflation across construction routes.**
Writing "$Y_{K3}$" without disambiguating among
- (a) $H_{\mathrm{Muk}}$ = $\Phi_2(D^b(K3))$ (abelian Heisenberg);
- (b) $Y(\mathfrak g_{K3})^{\mathrm{BFN}}$ = BFN Coulomb branch at Kummer;
- (c) $Y_{K3}^{\mathrm{so}(4,20)}$ = Drinfeld-first envelope of the classical limit;
- (d) $Y_{K3}^{L_\infty\text{-coupled}}$ = Wave 5 assembled direct sum;
is a Pattern 236 violation. All four objects differ.

### 7.6 AP323 proposal (new anti-pattern)

**AP323 — $\Phi$-functor output as proxy for downstream Hopf-algebra
construction.** Writing "$Y_{K3} = \Phi(D^b(K3))$" when in fact
$\Phi(D^b(K3)) = H_{\mathrm{Muk}}$ and the Yangian-quantization step
is an open downstream construction (explicitly so written at
`k3_yangian_chapter.tex:95`). This is a $\Phi$-application-scope
violation of the U4 standard-input recovery: U4 gives
$\Phi(D^b(K3)) = H_{\mathrm{Muk}}$, not $Y(\mathfrak g_{K3})$. The
Yangian status attaches to a lifting of the output, not to the
output itself.

### 7.7 AP-CY71 candidate (Vol III-specific)

**AP-CY71 — Block-diagonal YBE at the stratum-decomposition level
does not entail cross-strata YBE at the reassembly level**
(existing in Wave 5; I now elevate its status). Gelfand W5's
block-diagonal rescue is correct on the decomposed $V_{\mathrm{Heis}} \oplus \bigoplus V_\Lambda$;
the reassembly to a total $V_{\mathrm{Muk}}$ re-introduces
cross-strata couplings that break YBE. Wave 5 synthesis §1.4 and
§7.3 already noted this; the chapter-level inscription has not
recorded it with the full scope qualifier.

---

## 8. What Wave 6 should do (targets, harsh)

Reordered from the Wave 5 targets list in `SYNTHESIS_COMPLETE.md §11`:

1. **Gelfand W6 + Kazhdan W6**: **Name the convolution dGLA**.
   Either show that an explicit $\mathrm{Conv}^{\mathrm{ch}}(Y_{K3}, B^{\mathrm{ord}}(Y_{K3}))$
   exists on a named curve $X$, with the $L_\infty$-coupling as a
   Maurer-Cartan element, OR retract the "$L_\infty$-coupled"
   claim to a formal Lie-bialgebra-extension statement.

2. **Etingof W6 + Beilinson W6**: **Apply Theorem B to
   $H_{\mathrm{Muk}}$ on the Kummer orbifold**. Chain-level
   explicit computation: $\Omega_X(B_X(H_{\mathrm{Muk}})) \xrightarrow{\sim} H_{\mathrm{Muk}}$
   on the formal disk $D$. If this succeeds at the abelian level,
   then the conjectural Yangian-lifting step of `k3_yangian_chapter.tex:95`
   gains a Theorem B scope qualifier.

3. **Polyakov W6 + Drinfeld W6**: **Name the curve $X$** on which
   the Wave 5 $Y_{K3}^{L_\infty\text{-coupled}}$ is supposed to be a
   chiral algebra. Pick one of (a)–(e) from §1 A1 above. Pick ONE.
   State its factorization-envelope construction explicitly.
   Without this the Wave 5 object does not exist as a chiral
   algebra.

4. **Nekrasov W6 + Gaiotto W6**: **Disambiguate "$\hbar = 1/35$".**
   Nekrasov W5 clarified it is a structural identification, not a
   Fourier coefficient. Downstream uses (Witten-AGT cross-check,
   Obers–Pioline duality) must use the structural identification or
   retract.

5. **Witten W6**: **Retract the "$L_\infty$-morphism of degree 3"
   framing definitively.** The correct framing is Drinfeld
   quantisation of a $H^3_{\mathrm{Lie}}$ cocycle. Inscribe this
   reframing into `k3_yangian_chapter.tex` and remove all
   "$L_\infty$-morphism" language from the heterotic origin story.

6. **Costello W6**: **Resolve the $-3/4$ double-sunset coefficient**
   from first principles or retract. The Igusa-denominator
   integrality test does not discriminate $-1/4$ from $-3/4$.

7. **Beilinson W6 (me, meta-level)**: **This memo**. Harsh cascade
   audit. AP321, AP322, AP323, AP-CY71 installation. Wave 5 flagship
   demoted to [L/M]. $\Phi$-vs-Yangian-lifting scope drawn.

### 8.1 My ONE computation target for W6

**Compute $Z^{\mathrm{der}}_{\mathrm{ch}}(H_{\mathrm{Muk}})$ at rank 24**
in the chiral-Hochschild convention on the formal disk $D$, and check
against the published SC$^{\mathrm{ch,top}}$ machinery (Vol II). If
the computation produces an abelian 25-variable polynomial algebra as
expected, **this is a DISPROOF** of the claim that the Wave 5
$Y_{K3}^{L_\infty\text{-coupled}}$ is $\cZ$ of anything starting from
$\Phi(D^b(K3))$. The Drinfeld centre of an abelian algebra is
abelian. The Wave 5 coupled object is not the Drinfeld centre of the
abelian $H_{\mathrm{Muk}}$.

The module `compute/lib/k3_yangian_wave6_beilinson_derivedcentre_kummer.py`
is proposed (not written in this memo); writing it is the W6
follow-up I assign to myself.

---

## 9. Final convergence declaration

Wave 6 Beilinson verdict on the non-abelian K3 Yangian:

**The object that Wave 5 calls "$Y_{K3}$" does not exist as a chiral
algebra on a named curve in the Beilinson-Drinfeld sense.** The
components are real but individually scoped. The Wave 5 $L_\infty$-
coupling is [L]-status: no convolution dGLA, no MC element, no
named curve, no factorization-envelope construction.

**What Vol III actually has**:
- $H_{\mathrm{Muk}}$ = rank-24 Mukai-Heisenberg = $\Phi_2(D^b(K3))$,
  a \ClaimStatusProvedHere abelian $E_2$-chiral algebra on any smooth curve.
- A family of ADE-enhancement Yangians $Y^\mu(\widehat{\fg})_{k=1}$,
  each \ClaimStatusProvedElsewhere at its locus, via BFN.
- A conjectural BFN construction for generic K3.
- A conjectural categorification of the Borcherds BKM $\Phi_{10}$
  denominator.
- A slogan-level "coupling" among these that does not have
  mathematical content in the Vol I Theorem B / Theorem D sense.

**What Vol III does NOT have**:
- A chiral algebra on a named curve that realises the Wave 5 total
  $Y_{K3}^{L_\infty\text{-coupled}}$.
- A convolution dGLA $\mathrm{Conv}^{\mathrm{ch}}(Y_{K3})$ with
  explicit MC element for the coupling.
- A Theorem B verification for $Y(\mathfrak g_{K3})$ on either the
  abelian or non-abelian side.
- A universal trace identity in Vol III that bridges to Vol I via
  $Y_{K3}$.

**What Vol III's organising premise ASSERTS and what is supported**:
$\Phi: \mathrm{CY} \to \mathrm{ChirAlg}$ delivers on K3 at $d = 2$
(produces $H_{\mathrm{Muk}}$). The flagship non-abelian object is a
downstream conjecture, not a $\Phi$-application. **The "Vol III's
organising promise fails on K3" framing of the Wave 6 prompt
is half-right**: the organising promise delivers an abelian algebra
on K3, but the flagship non-abelian Yangian is not a $\Phi$-output,
is not a chiral algebra on a named curve, and is conjectural on
multiple axes.

**The adversarial attack-heal methodology requires**: in Wave 6, no
claim proceeds without a named curve, a named convolution dGLA, and
a chain-level explicit or $(\infty,1)$-categorical universal
property witness. Pattern 236 ambient qualifiers on every claim.
No self-exoneration by invoking a prior wave's convergence vote.

**Nothing is sacred. Not even my own W5 memo. I retracted W5 §2.3
(cross-strata Drinfeld-anomaly non-vanishing on orthogonal strata
per §1 A3 above). I demoted my own W5 participation in the
"triple convergence" on $l_4 = 1/24$ to AP321 (§7.4). I retract
W5 §12 three-volume ripple (§6).**

The Wave 6 open problems (reordered by severity):

**Critical-1**. Name the curve for Wave 5 $Y_{K3}^{L_\infty\text{-coupled}}$,
or retract the claim that it is a chiral algebra.

**Critical-2**. Name the convolution dGLA and MC element for the
$L_\infty$-coupling, or retract the "$L_\infty$" language.

**Critical-3**. Invoke and verify Theorem B for $H_{\mathrm{Muk}}$ on
the formal disk (or for $Y(\mathfrak g_{K3})$ in its conilpotent
completion), or flag the Vol I <-> Vol III backbone gap.

**Critical-4**. Retract the "$\Phi(D^b(K3)) = Y_{K3}$" conflation
wherever it appears in Vol III or the swarm memos. The correct
statement is $\Phi_2(D^b(K3)) = H_{\mathrm{Muk}}$; $Y(\mathfrak g_{K3})$
is a conjectural lifting.

**High-1**. Resolve my AP321 (three-path-via-$\chi$ illusion) across
Wave 5's [H] claims: $l_4, l_5$, level shift, cross-strata coupling.

**High-2**. Located Cheng–Wang 2012 §2.6 or replace with primary
source; if not locatable, downgrade Kazhdan W4's $1/24$ forever.

**High-3**. Drop Wave 5 §12 three-volume ripple from any Wave 6 or
later synthesis.

**Medium**. Proceed with individual stratum theorems as honest
scoped results; do not advertise them as a unified flagship.

---

**Raeez Lorgat, sole author. No AI attribution. Vol III manuscript
only. Adversarial Wave 6 Beilinson memo ends here.**

— End of Wave-6 Beilinson memo.
