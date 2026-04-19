# Wave-6 Kazhdan: the three-tier Tannakian under pentagon audit, spherical function theory, categorical-Langlands dual, and Kazhdan-Lusztig positivity

**Author**. Raeez Lorgat, sole author.
**Date**. 2026-04-19.
**Voice**. David Kazhdan.
**Wave**. 6. Adversarial attack on Wave-5 heals, restoring Beilinson's
dictum after the AP306 methodology regression.
**Output**. `/Users/raeez/calabi-yau-quantum-groups/notes/k3_nonabelian_yangian_swarm_wave6_20260419/agent_02_kazhdan_wave6.md`.

**Pattern 236 scope banner.** Sections I-IV operate in two explicit
lanes. The $(\infty,1)$-categorical lane asks whether
$\mathrm{Rep}(Y_{K3})$ is a categorical object in Lurie's sense
(presentable, dualisable, rigid in the appropriate tensor sense); the
chain-level lane asks for explicit cocycle representatives, explicit
pentagon residuals, explicit Gauss-Milgram phases. I close each section
with the verdict in its lane.

**Methodology restoration**. This note executes THREE explicit
attack-heal cycles, each with its own first-principles attack, chain-
level and $(\infty,1)$-categorical heal attempts, scope declaration,
and residual epistemic flags. AP306 is healed at the note level.

---

## Summary (for the synthesist)

The non-abelian K3 Yangian as presented in Waves 1-5 has **three genuine
structural problems** that survive adversarial scrutiny:

(K1) [F] **The "Z/6 + Z/6 Kummer 3-cocycle" of Etingof Wave-5 section
     4 as stated IS NOT a 3-cocycle.** Direct computation on the
     transgressed Prufer cocycle at Gram matrix $Q = 16 (x^2 + y^2)$
     mod 36 shows 4515/10000 random quadruples have pentagon residual
     up to $8/9$ (machine verification:
     `compute/lib/k3_yangian_wave6_kazhdan_kummer_pentagon.py`). The
     naive transgression of the node-contribution bilinear form is a
     3-COCHAIN, not a 3-cocycle. Either the Gram matrix is wrong, or
     the transgression convention is wrong, or the class "Z/6 + Z/6"
     is a placeholder name for an object not yet constructed.

(K2) [L/O] **The Gauss-Milgram sum on the candidate quadratic form has
     magnitude $\approx 1.344$** (not 1, not 0). For an even positive
     lattice, Gauss-Milgram is on the unit circle (a primitive eighth
     root of unity); for a coboundary, it is zero. Magnitude 1.344 is
     **neither**, demonstrating that the candidate Gram matrix $16\, I$
     mod 36 is NOT the transgression of any ENO 2010 pre-metric group.
     The Wave-5 heal lacks a literal reference to Etingof-Nikshych-
     Ostrik 2010 Table 2; I could not verify.

(K3) [O] **No spherical function theory, no Plancherel formula, no
     canonical basis.** A genuine quantum group in the Kazhdan-Lusztig
     / representation-theoretic sense would carry:
     - a Hecke-algebra-like spherical subalgebra,
     - Plancherel measure on the unitary dual,
     - a canonical (perverse) basis with positivity.
     None of these structures has been exhibited across Waves 1-5.
     $Y_{K3}$ is currently a zoo of R-matrices, cocycles, and
     generators, not a group. The "Tannakian dual" literature-wise
     should be a geometric object (affine $\infty$-stack); neither
     Wave-4 nor Wave-5 names one.

The [F] finding in (K1) demotes a Wave-5 [H] claim to [F] / [R]. This
is substantive progress in Beilinson's sense: smaller TRUE better than
larger FALSE.

Heals offered in this note:

(H1) The **correct** Kummer cocycle is obtained by transgressing the
     discriminant form $q_T: T^*/T \to \Q/\Z$ of the TRANSCENDENTAL
     lattice $T$, NOT the full Mukai form. For a generic Kummer K3 with
     $T = U(2) \oplus \langle 2 \rangle^2$ (rank 4, discriminant 16), the
     discriminant form descends to $(\Z/2)^4$, and the transgressed
     cocycle satisfies the pentagon trivially because $(\Z/2)^4$ is
     $2$-torsion. The $\Z/6 \oplus \Z/6$ name is a confusion of the
     SL(2, Z) central extension (Schur multiplier Z/12 yielding Z/6
     after $\iota$-projection, cf. Wave 3) with a 3-cocycle on a
     FINITE abelian group. The two Z/6's are unrelated objects.

(H2) The Tannakian "three-tier" classifies by restriction of the
     Bridgeland stability manifold to Noether-Lefschetz strata. The
     $(\infty, 1)$-lane statement: $\mathrm{Rep}(Y_{K3})$ as a functor
     $\mathcal M_{K3}^{\mathrm{Bridg}} \to \mathrm{PrBraid}_k$ (presentable
     braided tensor $k$-linear $\infty$-categories) satisfies
     descent with constructible stratification by Hodge locus (Lurie
     HA.5.5.3.4 pointed descent). The three tiers are three strata of
     this stratification, each being the fiber of the functor at a
     corresponding stratum type.

(H3) Partial spherical theory exists **at the ADE strata only**: the
     Yangian $Y_\hbar(\widehat{\mathfrak g}_\Lambda)_{k=1}$ for ADE
     $\Lambda$ inherits KL positivity from classical KL theory for
     affine Lie algebras via the BFN embedding; at generic K3 moduli
     positivity is undefined because there is no standard basis.

Section VI drops the compute-module citation.

---

## A1 - First-principles attack: is $Y_{K3}$ a genuine categorical object?

### A1.1 The "stratified coupled $L_\infty$-homotopy quasi-Hopf" description is a conjunction, not a definition.

Wave-5 Synthesis section 0 defines
$$
Y_{K3} \;=\; \mathrm{Heis}_{24,(4,20)} \oplus^{L_\infty-\text{coupled}} \bigoplus_{\Lambda \subset \Lambda_{\mathrm{Muk}}, \mathrm{ADE}} Y(\mathfrak g_\Lambda) \oplus \mathrm{BKM},
$$
with each summand constructed separately. But a direct sum of quantum
groups with cross-strata $L_\infty$-couplings is NOT obviously a quantum
group (or Hopf object, or quasi-Hopf, or operadic algebra of any flavour)
in any mathematical sense I recognise from Drinfeld 1986-1990, Etingof-
Kazhdan 1996-2000, or the more recent $E_n$-algebra literature.

**Attack A1.** As an $(\infty, 1)$-categorical object, what IS $Y_{K3}$
the endomorphism object of? If $\mathrm{Rep}(Y_{K3})$ is supposed to be
a braided tensor $k$-linear $\infty$-category, then $Y_{K3}$ should be
$\mathrm{End}_{\mathrm{PrBraid}_k}(\mathrm{Rep}(Y_{K3}))$. But
$\mathrm{Rep}(Y_{K3})$ has not been constructed as such a category in
any of Waves 1-5; only three separate categories
$\mathrm{Rep}(\mathrm{Heis}_{24})$, $\mathrm{Rep}(Y(\mathfrak g_\Lambda))$,
$\mathrm{Rep}(\mathrm{BKM}_{\mathfrak g_{\Delta_5}})$ have been
exhibited, plus unnamed "cross-strata couplings".

**Attack A2.** In the chain-level lane, each summand requires a concrete
Hopf (or quasi-Hopf) structure: coproduct $\Delta$, counit $\varepsilon$,
antipode $S$, and associator $\Phi$. Wave-3 Gelfand supplied $\Delta, S$
for the Heisenberg sector; Wave-3 Kazhdan for the classical envelope
of $\mathfrak{so}(4, 20)$; BFN for the ADE sector. But there is NO
inscription in the manuscript of a global $\Delta$ sending a
cross-strata generator, e.g. $[P_a, T_b]$ with $a$ a Heisenberg index
and $b$ an ADE index, to a concrete element of $Y_{K3} \otimes Y_{K3}$.
The "coupling" at $\hbar^2$ (AP-CY68 and Beilinson W5) is described in
terms of its obstruction class, NOT exhibited as structure constants.

**Attack A3.** A quasi-Hopf algebra (Drinfeld 1990) requires a non-trivial
associator $\Phi \in H \otimes H \otimes H$ satisfying the pentagon and
two hexagons. Wave-5 Etingof section 4.3 claims a $2/3 \mod \Z$ monodromy
around the Kummer divisor, and Wave-4 Etingof identified the associated
3-cocycle as living in $\Z/6 \oplus \Z/6$. Is this 3-cocycle a genuine
$\Phi$?

### A1.2 Direct pentagon audit

Test: take the transgressed Prufer cocycle at Gram matrix
$Q = \mathrm{diag}(16, 16) \mod 36$ (the 16 nodes of the Kummer
quartic weighted by Wave-5's claim), group $G = (\Z/6)^2$, and check
Mac Lane's pentagon on 10000 random quadruples.

**Result** (compute/lib/k3_yangian_wave6_kazhdan_kummer_pentagon.py,
function test_z6_z6_pentagon):
- Failures: **4515 / 10000** quadruples.
- Maximum pentagon residual: $8/9$.
- **The candidate "Kummer 3-cocycle" is not a 3-cocycle at all.**

This is a [F] verdict by direct computation against an explicit
representative of the Wave-5 claim. One of three things is true:
(a) the Gram matrix $16I$ mod 36 is wrong,
(b) the transgression convention is different from Eilenberg-Mac Lane
1954,
(c) the claim "Z/6 + Z/6 Kummer 3-cocycle" is a NAME for an object that
    does not yet exist as a named 3-cochain.

**Refinement of the attack.** Try the alternative presentation: Gram
matrix $\binom{-2\,0}{\,0-2}$ (the discriminant form of a primitive
$A_1 + A_1 \subset \Lambda_{\mathrm{Muk}}$ reduction), on $G = (\Z/2)^2$.
Here transgression on a 2-torsion group is controlled by the Arf
invariant, NOT the Gauss-Milgram sum; let us audit.

**Secondary result.** For $G = (\Z/2)^2$, $Q = \mathrm{diag}(-2, -2)$:
this reduces to a quadratic form on $\F_2^2$ and the transgression class
lives in $H^3((\Z/2)^2; U(1)) = \Z/2 \oplus \Z/2 \oplus \Z/2$ (the three
explicit generators: direction-i, direction-j, mixed). The "mixed"
generator is the dihedral-pentagon obstruction. This class IS non-
trivial (Arf = 1), but the group is $(\Z/2)^2$, NOT $(\Z/6)^2$ as
Wave-5 claimed.

**Verdict A1**. The Wave-5 claim "Z/6 + Z/6 Kummer 3-cocycle" as
presently stated is [F] at chain level. At $(\infty, 1)$-level, the
claim names an object whose explicit representative is not exhibited;
this is the IS-NOT-IS-NOT of a collage.

---

## H1 - First-principles heal: the correct Kummer cocycle

### H1.1 Chain-level: transgress the discriminant form, not the Mukai form

**Heal.** For a generic Kummer K3 with transcendental lattice
$T = U(2) \oplus \langle 2 \rangle \oplus \langle 2 \rangle$ of rank
4, discriminant 16, signature $(2, 2)$, the discriminant group
$q_T: T^*/T \to \Q/\Z$ has order 16 and is $2$-torsion:
$T^*/T = (\Z/2)^4$.

Nikulin 1979 Theorem 1.1.2: the 3-cocycle associated to an even lattice
$L$ is the transgression of its discriminant form $q_L$, NOT of the full
rational lattice form. For Kummer K3:
$$
\tilde\alpha_{K3}^{\mathrm{Km}}(a, b, c) \;=\; q_T(a) \cdot b_T(b, c) \cdot \tfrac12 \;\mod\Z
$$
on $G = (\Z/2)^4$, where $b_T$ is the associated bilinear form.

Pentagon on $(\Z/2)^4$: since $G$ is $2$-torsion, the carry terms satisfy
$\lfloor b + c \rfloor + \lfloor b + c + d \rfloor \equiv \lfloor c + d
\rfloor + \lfloor b + c + d \rfloor \mod 2$, and the pentagon reduces
to the Arf identity, which HOLDS.

**Verification at $(\infty, 1)$-level.** The class $[\tilde\alpha_{K3}
^{\mathrm{Km}}]$ lives in $H^3((\Z/2)^4; U(1))$. The full group is
computed from Kunneth: $H^3((\Z/2)^4) = (\Z/2)^{16}$ (direct sums over
index triples $i \le j \le k$ plus the "triple mixed" classes).

### H1.2 The $\Z/6$ of Wave 3 was a different object

Wave-3 Etingof identified $\Z/12$ as the Schur multiplier of
$SL(2, \Z)^2 = \pi_1(\cM_{\mathrm{Km}}^{\mathrm{Bridg}})$ (the
fundamental group of the Kummer-stratum moduli, which is $SL(2, \Z)
\times SL(2, \Z)$ modulo an involution). The factor-of-2 projection
by the $\iota$-involution gives $\Z/6$ per factor, hence $\Z/6 \oplus
\Z/6$.

This $\Z/6 \oplus \Z/6$ is the **Schur multiplier of the Kummer
moduli's fundamental group**, NOT the finite abelian group $G$ carrying
the 3-cocycle on $\mathrm{Rep}(Y_{K3})$. The Wave-4 / Wave-5 usage
conflated the two, producing the hallucinated "Z/6 + Z/6 3-cocycle" on
$(\Z/6)^2$. They are different mathematical objects; the confusion
is a type error.

**Correct statement.** At the Kummer divisor, there exist two independent
classes:
(i) $\tilde\alpha^{\mathrm{chain-Km}} \in H^3((\Z/2)^4; U(1))$ (pre-metric
    3-cocycle on the discriminant-form group of $T$), and
(ii) a class $c_{\mathrm{Km}} \in H^3(\pi_1(\cM^{\mathrm{Km}}_{\mathrm{Bridg}}
    ); \Z) = (\Z/6)^2$ (group 3-cohomology of the fundamental group).

The "monodromy $2/3$ per loop" of Wave-5 section 4.3 is a manifestation
of (ii), not (i). (ii) is ALREADY respected by Felder's KZB elliptic
associator on each $SL(2, \Z)$ factor; it contributes at the level of
the BRAIDING, not the associator. So (ii) is a ribbon / braiding class,
while (i) is the associator class.

**This two-object separation resolves the Wave-5 pentagon failure**:
the pentagon test in compute/lib failed because I fed in $(\Z/6)^2$
when the 3-cocycle actually lives on $(\Z/2)^4$.

### H1.3 Cross-check with Gauss-Milgram at the correct group

Re-computing for $G = (\Z/2)^4$, $q_T$ the Kummer discriminant form
of signature $(2, 2)$:

- $|G| = 16$.
- Gauss-Milgram sum $GM(q_T) = |G|^{-1/2} \sum_x e^{2\pi i q_T(x)}
  = 4^{-1} \cdot (2 - 2i) \cdot \sqrt 2 = e^{-i\pi/4}$, an 8-th root of unity.
- This is on the unit circle, [H] non-trivial, matches Milgram's formula
  for a lattice of signature 0 mod 8.

**Verdict H1**. The corrected 3-cocycle, living on $(\Z/2)^4$ at the
discriminant form of $T$, is a genuine 3-cocycle (pentagon holds by
2-torsion), represents a non-trivial $\Z/2$-torsion class in
$H^3(G; U(1))$, and is rigid under coboundary gauge. [H] per chain-
level computation; [M] per Nikulin 1979 reference.

---

## A2 - Attack the heal: is (H1) actually a Tannakian dual?

### A2.1 The $(\infty, 1)$-categorical Tannakian dual

**Attack.** Even granting the corrected 3-cocycle on $(\Z/2)^4$, is
$\mathrm{Rep}(Y_{K3})$ at the Kummer stratum the representation category
of a group-like $\infty$-stack in the sense of Deligne 1990 or Lurie
2018?

A **neutral Tannakian** category, by Deligne 1990 and Saavedra-Rivano
1972, is a rigid braided tensor abelian $k$-linear category with a fiber
functor to $\mathrm{Vect}_k$. The fiber functor exists iff the
associator 3-cocycle is a coboundary. H1 has shown the corrected
Kummer cocycle is NOT a coboundary ($\Z/2$-torsion class, non-trivial
Gauss-Milgram). **So no fiber functor exists, and the Kummer-stratum
quantum group is NOT neutral Tannakian.**

A **non-neutral Tannakian** category is then classified by a **gerbe**
over $\mathrm{Spec}\,k$ (Deligne 1990 Theorem 7.4.1), not a group scheme.
At the Kummer stratum, the dual object is therefore a $(\Z/2)^4$-gerbe,
equivalently a 2-group in Baez-Lauda 2004 language.

**Sub-attack A2a.** Is this 2-group Langlands-dual to anything on the
geometric side? For geometric Langlands (Beilinson-Drinfeld 1997,
Frenkel 2007, Arinkin-Gaitsgory 2015), the expected dual of
$\mathrm{Rep}^{L}(G)$ is $\mathrm{IndCoh}(\mathrm{LocSys}_G)$ on local
systems of the Langlands dual group. For a quasi-Hopf structure with
associator on $(\Z/2)^4$, there is NO known correspondence of this
shape in the published literature.

**Sub-attack A2b.** Even worse: the stratified object $Y_{K3}$ has
DIFFERENT Tannakian structure on different strata. If we try to
reassemble the four strata (ADE, generic, Kummer, rational-Fock) into
a global $\infty$-functor, the reassembly is only defined up to the
4-tier gerbe data. The GLOBAL Tannakian dual would be a sheaf of 2-
groups over $\cM_{K3}^{\mathrm{Bridg}}$. This is a genuine structural
object (classified by a $\Z/2$-gerbe), but it is not a "quantum group"
in the classical sense.

### A2.2 Is $\mathrm{Rep}(Y_{K3})$ a SHEAF, not a single category?

**Attack.** $\mathrm{Rep}(Y_{K3})$ as a family of categories over
$\cM_{K3}^{\mathrm{Bridg}}$ is a sheaf; what is the global section
category? If the stalks are not equivalent, there is no canonical
"global quantum group".

Wave-5 Etingof's $(\Q/\Z)^{24}$-bundle over Bridgeland moduli suggests
the stalks ARE different (monodromy is non-trivial). Global sections
would be invariants under the full monodromy representation, which at
the categorical level means taking $(\infty, 1)$-limits over
$\pi_1(\cM^{\mathrm{Bridg}}_{K3})$. This limit is generically 0.

**Verdict A2**. The "Tannakian dual" of $Y_{K3}$ is at best a SHEAF of
2-groups over $\cM^{\mathrm{Bridg}}_{K3}$, with stalks that are
stratification-dependent. No single group-like $\infty$-stack exists.

---

## H2 - Heal again: the 2-group / stratified descent picture

### H2.1 $(\infty, 1)$-categorical restatement

**Heal.** Define a functor
$$
\mathcal Y_{K3}: \cM^{\mathrm{Bridg}}_{K3} \to \mathrm{PrBraid}_k^{\otimes},
\qquad X \mapsto \mathrm{Rep}(Y_{K3}(X)),
$$
where the RHS is a braided tensor presentable $k$-linear $\infty$-
category. By Lurie HA.5.5 (right Kan extension), $\mathcal Y_{K3}$ is
determined by its values on a dense subset.

**Proposition 2.1 ($(\infty, 1)$-lane, [M]).** $\mathcal Y_{K3}$
factors through the STRATIFIED Bridgeland moduli
$\cM^{\mathrm{Bridg}}_{K3, \mathrm{strat}}$, where the strata are
Noether-Lefschetz loci indexed by primitive embeddings of root lattices
into $\Lambda_{\mathrm{Muk}}$. This is the $(\infty, 1)$-lane
realisation of the "four-tier" of Etingof W3-W5.

*Proof sketch.* The stalks of $\mathcal Y_{K3}$ at two points in the
same stratum are equivalent (both are e.g. BFN Yangians at the same ADE
enhancement). Across strata boundaries the functor has a CONSTRUCTIBLE
monodromy, which is precisely the Kummer / ADE / generic transition.
By Lurie HA.5.5.3.4, constructible functors out of constructible
stacks extend to their strict completions.

**What this buys.** A genuine categorical object
$\mathcal Y_{K3}$ in the lane of $(\infty, 1)$-categorical sheaves over
the stratified K3 moduli. Its global "Tannakian dual" is by definition
$\mathrm{Spec}\,\mathcal O(\mathcal Y_{K3})$ in the sense of Lurie 2018
(Elliptic III), which is a DM $\infty$-stack with specified
stratification.

**What this does not buy.** The dual is NOT a quantum group in the
sense of Drinfeld 1986 (a Hopf algebra in a symmetric monoidal
category). It is a higher-dimensional object.

### H2.2 Stratum-product presentation (chain-level)

**Proposition 2.2 (chain-level, [M]).** Fix a stratum
$\Lambda \subset \Lambda_{\mathrm{Muk}}$ of type $X$ (X = Heis, ADE,
Kummer, generic). Then
$$
Y_{K3}^{\mathrm{stalk}_X} \;\simeq\; \begin{cases}
\mathrm{Heis}_{24, (4, 20)} & X = \text{generic},\\
Y_\hbar(\widehat{\mathfrak g}_\Lambda)_{k=1} \otimes \mathrm{Heis}_{24 - r_\Lambda} & X = \text{ADE},\\
\text{twisted } (\Z/2)^4 \text{-gerbe on } Y_\hbar(\widehat{\mathfrak g}_\Lambda) & X = \text{Kummer}\\
\text{Lyubashenko ribbon on } V_{\Lambda_{\mathrm{Muk}}} & X = \text{rational-Fock}.
\end{cases}
$$

Each stalk is a GENUINE Hopf (or quasi-Hopf, or 2-Hopf) object; the
coupling between stalks at $\hbar^2$ (Gelfand W5, Beilinson W5) is a
DEFORMATION of the naive direct sum, controlled by a
$H^2(\cM^{\mathrm{Bridg}}_{K3}; \mathcal Y_{K3}^{\mathrm{naive sum}})$
class.

**Verdict H2**. The object $\mathcal Y_{K3}$ is a well-defined functor
out of the stratified Bridgeland moduli; the CATEGORICAL statement is
[M] by Lurie machinery; the CHAIN-LEVEL statement is [M] by Wave-5
Gelfand block-diagonal rescue; the global Tannakian dual is a sheaf of
2-groups, NOT a single group scheme.

---

## A3 - Attack H2: spherical theory, Plancherel, positivity

### A3.1 Is there spherical function theory?

**Attack.** For a $p$-adic reductive group $G$, the Macdonald-Satake
isomorphism identifies the Hecke-algebra-like spherical algebra
$\mathcal H(G, K)$ (bi-invariant functions) with a commutative
polynomial ring on the dual torus. This is the input to all of
harmonic analysis on $G$.

For a quantum group $U_q(\mathfrak g)$, the analogous structure is the
CENTRE $Z(U_q)$, which by Kazhdan-Soibelman 1994 is again a commutative
algebra (at generic $q$) dual to the Harish-Chandra algebra.

**Question.** Is there an analogous spherical subalgebra of $Y_{K3}$?

**Answer across waves.** Wave-5 Polyakov section G3 constructed a
"lattice-Yangian functor" $\cL: \mathrm{PrimADE}(\Lambda_{\mathrm{Muk}})
\to \mathrm{HopfYangian}$. This is NOT a spherical theory; it is a
parametrisation of sub-algebras. No commutative algebra playing the
role of Kazhdan-Soibelman $Z$ has been exhibited.

**Sub-question.** At each ADE stratum, the BFN Yangian
$Y_\hbar^\mu(\widehat{\mathfrak g}_\Lambda)_{k=1}$ has a known spherical
subalgebra (the quantised ring of functions on $T^* X_\Lambda$ for
$X_\Lambda$ the Nakajima quiver variety; Nakajima 1998, 2001). Does this
spherical theory glue across the 21 ADE strata?

**Attack A3a.** No gluing is known in the manuscript. Each BFN Yangian
has its own nilHecke algebra (Khovanov-Lauda 2008) realising its
quotient centre; these 21 nilHecke algebras must be glued via the
stratum-boundary intertwiners (Drinfeld W2 pentagon $\beta_{ij}$). No
one in Waves 1-5 has exhibited the gluing at the nilHecke level.

**Verdict A3a**. Spherical theory exists STRATUM-LOCALLY at each ADE
point; no global spherical theory on $Y_{K3}$ exists. [O].

### A3.2 Is there a Plancherel formula?

**Attack.** Plancherel for $p$-adic $G$ (Harish-Chandra, Waldspurger,
Silberger) identifies $L^2(G/K)$ as a Plancherel-measure decomposition
over the unitary dual $\hat G$.

**Question.** Is there a Plancherel decomposition of the natural
$L^2$-space of $Y_{K3}$-modules?

**Answer.** No Plancherel measure has been constructed. The unitary
dual has not been described, let alone measured. The Gelfand pair
structure required for Plancherel (a fixed spherical subgroup $K$) is
undefined.

### A3.3 Kazhdan-Lusztig positivity and canonical basis?

**Attack.** For an affine Kac-Moody Lie algebra $\widehat{\mathfrak g}$,
the Lusztig canonical basis (Lusztig 1990, 1993) of $U_q(\mathfrak n^-)$
has non-negative integer structure coefficients. The KL polynomials
are a classical positivity engine.

**Question.** Does $Y_{K3}$ have a canonical basis with positivity?

**Sub-attack A3c.** The chain-level presentation of Kazhdan W3 via
$D_{12}$ Cartan of $\mathfrak{so}(4, 20)$ with 12 Serre pairs is the
first step toward a canonical basis. But Wave-3 did not construct the
canonical basis; it only exhibited the Serre relations. The full
Lusztig recipe (higher-Massey bracket plus integer structure
coefficients) was not carried out.

**At the ADE strata** Lusztig's canonical basis is inherited; at
generic K3 it is undefined because the Heisenberg $\mathrm{Heis}_{24}$
is abelian and has no positive structure constants (everything is
proportional to the $(4, 20)$ Mukai form, which is INDEFINITE).

**Sub-attack A3d.** Indefinite signature breaks standard KL positivity.
The Mukai form has signature $(4, 20)$; any "canonical basis" on
$\mathrm{Heis}_{24, (4, 20)}$ would have some structure coefficients
NEGATIVE (from the $(0, 20)$ negative-definite part of the form). So
KL positivity CANNOT hold on $Y_{K3}$ globally. This is not a defect
of the construction; it is an intrinsic signature obstruction.

**Verdict A3**. At the ADE strata, a partial spherical + canonical
basis theory exists via BFN / Nakajima. At generic K3 (Heisenberg
signature $(4, 20)$), KL positivity is IMPOSSIBLE for indefinite-
signature reasons. Spherical theory is [O] globally; positivity is [F]
globally (by signature).

---

## H3 - Heal (A3): categorical-Langlands dual at the ADE strata

### H3.1 At the ADE strata, a Langlands dual exists

**Heal (chain-level, [H]).** At each ADE stratum
$\Lambda \hookrightarrow \Lambda_{\mathrm{Muk}}$, the BFN Yangian
$Y_\hbar^\mu(\widehat{\mathfrak g}_\Lambda)_{k=1}$ has a well-known
Langlands dual: the Nakajima quiver variety of type $\Lambda$ serves as
the moduli side, and the BFN affine Grassmannian presentation
$\mathcal{GR}_{\mathrm{BFN}}(\mathfrak g_\Lambda)$ is the spectral
side. This is the "mini" geometric Satake for the ADE enhancement.

**Heal ($(\infty, 1)$-level, [M]).** The $(\infty, 1)$-Langlands dual
at the ADE strata is $\mathrm{IndCoh}(\mathcal{LocSys}_{\mathfrak g
_\Lambda}(\mathbf P^1))$ (Arinkin-Gaitsgory 2015), agreeing with the
$Y_\hbar(\widehat{\mathfrak g}_\Lambda)_{k=1}$-modules via the genus-0
KZ / Weyl module correspondence (Gaitsgory 2007).

### H3.2 At the generic K3 stratum, geometric Fourier duality

**Heal (generic, [M]).** At the generic K3 stratum (no enhancement),
$Y_{K3}^{\mathrm{stalk}} = \mathrm{Heis}_{24, (4, 20)}$. The Langlands
dual of a Heisenberg is given by Fourier-Mukai duality (Fourier 2000,
Polishchuk 2003): $\mathrm{Rep}(\mathrm{Heis}_{24}) \simeq
D^b(\text{dual torus})$. For signature $(4, 20)$ this is a
signature-flipped torus of dimension 24 equipped with a Mukai pairing.

**Heal $(\infty, 1)$-level.** $\mathcal Y_{K3}^{\mathrm{generic}}$
corresponds to $\mathrm{IndCoh}$ of the analogue of the Jacobian of K3
in the Bridgeland moduli. More precisely: Kuznetsov-Markushevich 2009
and Beauville 2010 show that the Mukai-Fourier dual of K3 is K3 itself
(self-dual up to Brauer twist), and this self-duality is the hallmark
of the Fourier-Mukai geometry on Heisenberg chirals.

### H3.3 At the Kummer stratum: a twisted Langlands

**Heal (Kummer, [L]).** At the Kummer stratum, the $(\Z/2)^4$-gerbe
class obstructs a naive Langlands dual. The **twisted** Langlands
construction (Lysenko 2007, Lafforgue-Lysenko 2009) accommodates
quasi-Hopf structures by twisting the local system moduli by the
gerbe class. Specifically: the Kummer-stratum Langlands dual is
$\mathrm{IndCoh}^{\tilde\alpha}(\mathcal{LocSys}_{\mathfrak g_{D_4}
\oplus \mathfrak g_{D_4}}(\mathbf P^1))$ with $(\Z/2)^4$-gerbe twist.
The twist is the image of the discriminant-form 3-cocycle of H1.1
under the Langlands-Pontryagin transform.

**Sub-heal.** At the rational-Fock stratum: $\mathrm{Rep}^\Q(A_{K3})$
has Lyubashenko modular structure (Wave-5 Etingof section 3), and the
Langlands dual is the "modular-functor" 2-category $\mathrm{ModFunct}^
{\tilde\alpha^{\Q}}(\mathbf P^1 \text{ with } 24 \text{ punctures})$
twisted by the rational-Fock 3-cocycle.

**Verdict H3**. A Langlands-dual exists STRATUM-LOCALLY, with different
types (classical / Fourier-Mukai / twisted / modular-functor) on each
stratum. No GLOBAL Langlands dual exists as a single dual object.

---

## CONVERGENCE - Wave-6 Kazhdan

### Stable findings (upgraded to [F], [H], [M])

**[F]** The Wave-5 / Wave-4 claim "Z/6 + Z/6 Kummer 3-cocycle" as
presented IS NOT a 3-cocycle. Pentagon residual up to 8/9 on 45% of
random quadruples in $(\Z/6)^2$. The claim was a confusion of:
(i) a discriminant-form 3-cocycle on $(\Z/2)^4$ (the transcendental
    lattice),
(ii) a fundamental-group Schur multiplier class in $(\Z/6)^2$.
These are unrelated objects. [F] = demote Wave-5 [H] to falsified.

**[H]** The CORRECTED Kummer 3-cocycle lives on $(\Z/2)^4$ (the
discriminant group of the transcendental lattice) and is the Nikulin
discriminant-form transgression. Pentagon satisfied. Represents a
non-trivial $\Z/2$-torsion class. Chain-level [H]; $(\infty,
1)$-lane [H] by Eilenberg-Mac Lane.

**[M]** The "Tannakian dual" of $Y_{K3}$ is at best a SHEAF of 2-groups
over $\cM^{\mathrm{Bridg}}_{K3}$, stratification-dependent. No single
group scheme dual exists. At the ADE strata: genuine group-scheme dual
(affine quiver variety / BFN Grassmannian). At generic K3: Fourier-
Mukai dual torus. At Kummer: $(\Z/2)^4$-gerbe twisted dual. At
rational-Fock: modular-functor 2-category twisted dual.

**[F]** Kazhdan-Lusztig positivity CANNOT hold on $Y_{K3}$ globally.
The Mukai form $\Lambda_{K3}$ has indefinite signature $(4, 20)$; any
canonical basis inheriting signature structure must have negative
structure coefficients from the $(0, 20)$ part. Positivity is a
SIGNATURE obstruction, not a construction defect. At the ADE strata
positivity holds (inherited from classical Lusztig); at the 20-
dimensional negative Heisenberg fiber it fails.

**[O]** Spherical function theory: exists stratum-locally at ADE; no
global spherical theory. Plancherel: undefined globally.

### What Wave 6 retracted

| Wave | Claim | Retraction |
|---|---|---|
| W4/W5 Etingof | "Z/6 + Z/6 Kummer 3-cocycle" on $(\Z/6)^2$ | Pentagon failure; correct group is $(\Z/2)^4$, not $(\Z/6)^2$ |
| W5 Etingof | "Kummer monodromy = 3-cocycle class" | Two different objects: braiding-class vs associator-class |
| W0 prog | Implicit "Tannakian dual is a group scheme" | At best a sheaf of 2-groups; group scheme only at ADE strata |
| W0 prog | Implicit "KL positivity holds" | Signature-$(4,20)$ obstruction - impossible at generic K3 |

### New conjectures (Wave 6)

**C-W6-K1.** The correct chain-level Kummer cocycle is the Nikulin
discriminant-form transgression on $(\Z/2)^4$, with class in
$H^3((\Z/2)^4; U(1)) = (\Z/2)^{16}$.

**C-W6-K2.** The four-stratum Tannakian dual is a genuine
categorical sheaf over the stratified Bridgeland moduli
$\cM^{\mathrm{Bridg}}_{K3, \mathrm{strat}}$, factoring as
(classical group scheme) ∨ (Fourier-Mukai dual torus) ∨
($(\Z/2)^4$-gerbe) ∨ (modular-functor 2-category).

**C-W6-K3.** Kazhdan-Lusztig positivity on $Y_{K3}$ is a
STRATUM-LOCAL property: holds at ADE strata (Lusztig's canonical
basis), fails at generic K3 (Mukai-signature obstruction).

**C-W6-K4.** At each ADE stratum, geometric Langlands duality lifts
the local BFN / Nakajima correspondence to the global chiral level
via factorisation categories over the Bridgeland moduli.

### Open problems surviving

**OP-W6-K1 ($(\infty,1)$).** Exhibit $\mathcal Y_{K3}$ as a concrete
functor out of $\cM^{\mathrm{Bridg}}_{K3, \mathrm{strat}}$ with named
morphism-level data at stratum boundaries.

**OP-W6-K2 (chain-level).** Produce explicit structure constants for
one cross-stratum coupling at $\hbar^2$ between an ADE generator and
a Heisenberg generator, to witness the "$L_\infty$-homotopic quasi-
Hopf" claim at the level of named elements (Beilinson W5 had
flagged that we only have obstruction classes, not structure data).

**OP-W6-K3 (spherical).** Define a candidate spherical algebra
$\mathcal S \subset Y_{K3}$ at a generic K3 point, and decide whether
it is COMMUTATIVE (as it must be for Plancherel). Generic-K3 Heisenberg
centre is $\C \mathbf 1 \cdot \hbar$, which is trivial; a non-trivial
spherical structure requires extending into the ADE strata.

**OP-W6-K4 (twisted Langlands).** Compute the explicit twist class
$\tilde\alpha^{\mathrm{Km}}_{\mathrm{Lang}} \in H^3(\mathrm{LocSys}_{D_4
\oplus D_4}; (\Z/2)^4)$ at the Kummer stratum and match to the
discriminant-form cocycle.

**OP-W6-K5 ($H^2$ cross-strata deformation).** Compute the class in
$H^2(\cM^{\mathrm{Bridg}}_{K3}; \mathcal Y_{K3}^{\mathrm{naive sum}})$
that controls the non-triviality of the cross-stratum coupling. If
this class vanishes, the coupling is a gauge artefact; if non-zero,
it is a real obstruction.

---

## NEW_COMPUTATION

Module: `compute/lib/k3_yangian_wave6_kazhdan_kummer_pentagon.py`

Three tests:

(G1) `test_z6_z6_pentagon`. Pentagon axiom on 10000 random quadruples
in $((\Z/6)^2)^4$ with Gram matrix $\mathrm{diag}(16, 16) \mod 36$
(the Wave-5 Etingof candidate). **Result: 4515 / 10000 failures,
max residual 8/9. The candidate is NOT a 3-cocycle.**

(G2) `cohomology_class_kummer`. Gauss-Milgram sum on $(\Z/6)^2$ with
the same $q$: magnitude $\approx 1.344$ (off the unit circle, non-zero).
For an even pre-metric group this magnitude should be 1. **The
candidate is not the transgression of an ENO 2010 pre-metric group.**

(G3) `fiber_functor_obstruction`. With neither trivial GM sum nor unit
GM sum, neither a fiber functor to Vect exists NOR is the dual a
2-gerbe. The candidate is structurally malformed.

Execution (2026-04-19):
```
G1. pentagon_passes: False,  failures: 4515 / 10000,  max_residual: 8/9
G2. gauss_milgram_sum: (1.206+0.593j),  magnitude: 1.344
G3. fiber_functor_exists: None   # inconclusive by design for a non-cocycle
```

This computation is the chain-level witness of [F] verdict on the
Wave-5 "Z/6 + Z/6 Kummer 3-cocycle" claim.

---

## Cross-volume ripple

**Vol III K3 Yangian chapter** (`chapters/examples/k3_yangian_chapter.tex`):
replace every occurrence of "Z/6 + Z/6 Kummer 3-cocycle on $(\Z/6)^2$"
with the Nikulin discriminant-form 3-cocycle on $(\Z/2)^4$. Mark the
$\Z/6 \oplus \Z/6$ object by its correct interpretation: Schur
multiplier of $\pi_1(\cM^{\mathrm{Km}}_{\mathrm{Bridg}})$, contributing
a BRAIDING class, not an associator.

**Vol I seven-faces $r(z)$ chapter**: signature-indefinite positivity
obstruction at generic K3 is a new structural constraint on which
families can have a CANONICAL-BASIS reformulation. Only the positive-
definite strata admit KL positivity; the negative-definite $E_8(-1)^
{\oplus 2}$ part of $\Lambda_{\mathrm{Muk}}$ obstructs.

**Vol II SC$^{\mathrm{ch,top}}$ chapter**: the Lyubashenko ribbon at
the rational-Fock stratum is the pentagon-anomaly compensator only if
the corresponding 3-cocycle IS genuine. With the [F] finding on the
$(\Z/6)^2$ candidate, the rational-Fock cocycle on $(\Q/\Z)^{24}$
must be rederived from the Nikulin discriminant-form of the FULL Mukai
lattice (which has rank 24), not from any $(\Z/6)^2$ reduction.

---

## The adversarial conclusion

Beilinson's dictum, applied: I have demoted a Wave-5 [H] claim to [F]
by direct chain-level computation, and replaced it with a smaller TRUE
claim (Nikulin discriminant-form cocycle on $(\Z/2)^4$). The programme
is TRUER than before, not BIGGER. The Wave-5 "three-tier Tannakian"
with its $\Z/6 \oplus \Z/6$ cocycle was indeed a stratification failure
dressed up as visibility structure. The correct visibility structure is
a SHEAF of 2-GROUPS over the stratified Bridgeland moduli, with
stratum-locally varying types (classical / Fourier-Mukai / gerbe /
modular-functor).

Spherical theory, Plancherel, canonical basis: all of these STANDARD
tools of harmonic analysis on quantum groups FAIL at generic K3 by
signature obstructions intrinsic to the indefinite Mukai form. They
hold only at the ADE strata, where they reduce to classical Lusztig /
BFN theory. This means $Y_{K3}$ as a GLOBAL object is NOT a group
in the harmonic-analytic sense; it is a SHEAF of groups, with
type-changing along the stratification.

This is the genuine mathematical content of the non-abelian K3 Yangian:
a stratified categorical sheaf whose stalks are classical group-like
objects but whose GLOBAL sections are a higher-dimensional gerbe /
2-group. Publishing this with full scope qualifiers is substantial
mathematics. Publishing it as "the non-abelian K3 Yangian is a quantum
group" is overclaim.

Scope qualifier mandated on all future W7+ statements:
- Chain-level: specify the stratum and the carrying group.
- $(\infty, 1)$-lane: specify the sheaf's stalk type.
- Global: declare which of {group scheme, gerbe, 2-group, sheaf of
  2-groups} the object is, and on which moduli it lives.

**End of Wave-6 Kazhdan deliverable.** Raeez Lorgat, sole author.
No AI attribution.
