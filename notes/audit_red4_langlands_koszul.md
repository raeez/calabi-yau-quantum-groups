# RED TEAM AUDIT 4: Langlands Duality = Koszul Duality

**Target**: Conjecture `G(C,G)^! = G(C,G^L)` in `notes/theory_qvcg_koszul.tex` (Conj 6.2) and `notes/physics_sduality_langlands.tex` (Conj 4.1).

**Auditor posture**: maximally adversarial. Every claim examined for circular reasoning, equivocation between different mathematical objects, and logical gaps between "evidence" and "conjecture."

**Date**: 2026-04-02

---

## FINDING 1: The object G(C,G) does not exist

**Severity**: CRITICAL (logical foundation)

**Location**: `theory_qvcg_koszul.tex` Section 6.1, Construction of G(C,G) via the CY-to-chiral functor Phi applied to D^b(Coh(M_H(C,G))).

**The problem**: The conjecture asserts an isomorphism between two objects, G(C,G)^! and G(C,G^L). Neither object has been constructed. Specifically:

1. The CY-to-chiral functor Phi (Theorem CY-A) is itself a target theorem of Volume III, not a proved result. The construction G(C,G) := G(M_H(C,G)) presupposes CY-A.

2. The Hitchin moduli space M_H(C,G) is non-compact. The notes acknowledge this (`notes/theory_qvcg_koszul.tex` line 704: "non-compact CY3 with trivial canonical bundle"). But the CY-to-chiral functor as described in CLAUDE.md requires a CY *category* with a non-degenerate trace Tr: HH_*(C) -> k[-d]. For non-compact CY, the Hochschild homology is typically infinite-dimensional, and the trace requires compactification or a choice of boundary conditions that has not been specified.

3. The root datum R(C,G) in `physics_hitchin_langlands.tex` (Construction 3.4, line 296) is explicitly a *proposal*: "The generalised root datum R(C,G) of the quantum vertex chiral group *associated to* Higgs(C,G) consists of..." with imaginary root multiplicities given by "DT/BPS invariants of M_H" which are themselves conjectural for non-compact targets.

**Assessment**: You cannot prove an isomorphism of objects that have not been constructed. The conjecture is meaningful only if Theorems CY-A through CY-D are first established for non-compact CY geometries. The notes do not address this prerequisite.

**Recommendation**: The note should explicitly state that G(C,G) is a *conjectural* object, contingent on extending CY-A to the non-compact setting (with specified boundary/growth conditions). The conjecture should be reframed as: "If G(C,G) can be defined, then..."

---

## FINDING 2: The five lines of evidence are analogies, not proofs

**Severity**: HIGH (epistemic honesty)

**Location**: `theory_qvcg_koszul.tex` Section 6.4; `physics_sduality_langlands.tex` Section 5.

**The problem**: The notes present four/five "independent directions" of evidence. Each has a critical logical gap.

### (a) Root datum exchange

The root/coroot exchange under Langlands duality is a property of the *finite root system* of G. It says nothing about imaginary roots, which constitute the bulk of the BKM superalgebra data. The note's own Definition 3.5 (Koszul dual root datum) requires the Borcherds involution omega_B on imaginary roots, which is *defined* only when an automorphic form Phi with a functional equation exists (Proposition 7.3). For the Hitchin system, the automorphic form is *conjectured* to exist (Conjecture 3.5 in `physics_hitchin_langlands.tex`), not proved.

The root datum exchange is therefore a *necessary condition* for the conjecture (on the finite part), not evidence. It would be equally consistent with many other operations on the full algebra.

### (b) Feigin-Frenkel at critical level

The Feigin-Frenkel isomorphism z(g_hat) = Fun(Op_{G^L}) is a theorem, but it applies *only at the critical level* k = -h^v. The conjecture is about quantum vertex chiral groups at *all* levels (or at least at a "natural" level determined by the CY geometry).

Moreover, the Feigin-Frenkel isomorphism identifies the *center* of V_{-h^v}(g) with G^L-opers. This is a property of the *center*, not of the *Koszul dual*. Proposition 3.3 of `physics_sduality_langlands.tex` (line 322) asserts: "the Koszul dual of V_{-h^v}(g), viewed as a commutative chiral algebra via the Feigin-Frenkel isomorphism, is the chiral algebra of functions on LocSys_{G^L}(C)." But this conflates two operations: (i) taking the center of V_{-h^v}(g), and (ii) taking the Koszul dual of V_{-h^v}(g). These are different. The center is a sub-object; the Koszul dual is a quotient (or dual) of the bar complex.

The note itself acknowledges this distinction at line 262: "This connection is *external motivation*, not a formal consequence of chiral Koszul duality alone."

### (c) Shifted Yangian / symplectic duality

The shifted Yangian conjecture Y_mu(g)^! = Y_{-mu}(g^v) (equation 6.8) is itself a conjecture, attributed to Volume I Conjecture 26.3.2. Using one conjecture as evidence for another is legitimate as a research programme, but should be explicitly flagged as such.

Furthermore, symplectic duality (BLPW) applies to *conical symplectic resolutions*, which are finite-dimensional. The passage to infinite-dimensional vertex algebras and their E_2 enhancements is not established in BLPW or subsequent literature.

### (d) HMS for Hitchin

The HMS line of evidence reveals a *contradiction* rather than supporting the conjecture. The note states (lines 836-848):

- HMS gives: A_{C,G} = A_{C,G^L} (isomorphism of chiral algebras)
- Koszul gives: A_{C,G}^! = A_{C,G^L} (Koszul dual is the Langlands dual)
- "These are consistent if and only if A_{C,G} is Koszul self-dual"

For simply-laced G, this forces *Koszul self-duality* of A_{C,G}, which is a very strong condition. Is there any independent evidence that the chiral algebra of the Hitchin system is Koszul self-dual? The note provides none.

For non-simply-laced G, the note waves at the E_2-enhancement: "the Koszul involution acts nontrivially on the E_2-enhancement (the braiding), exchanging the quantum group parameter q and q^{-1}." But this means HMS and Koszul duality are *different* operations that happen to act on the same set of objects. The "evidence" is that they give the same *underlying* algebra, while differing on the additional structure. This is not evidence; it is a consistency check that the underlying algebras match, which is a consequence of HMS, not of Koszul duality.

**Assessment**: The evidence establishes that Langlands duality and Koszul duality act *similarly* on certain invariants (root lattice, level, central charge). It does not establish that they are the *same* operation on the full quantum vertex chiral group. Every line of evidence either applies at a special point (critical level), uses a conjectural input, or reveals a tension (HMS vs Koszul).

---

## FINDING 3: The non-simply-laced gap is deeper than acknowledged

**Severity**: HIGH (mathematical substance)

**Location**: `theory_qvcg_koszul.tex` Section 7 (Borcherds involution), `physics_sduality_langlands.tex` Q1 (line 848).

**The problem**: For B_n/C_n, Langlands duality exchanges short and long roots. This changes the Gram matrix: for B_2, the Cartan matrix is ((2,-2),(-1,2)) and the Langlands dual (C_2) has Cartan matrix ((2,-1),(-2,2)). These are *transposes*, not related by the Borcherds involution.

The note's Definition 3.5 (Koszul dual root datum) defines the dual lattice as Lambda^! = Lambda^v with the *negated* Euler form. On real roots, it prescribes "unchanged as a set, but with the negated Gram matrix (up to conjugation by W)." But for B_n, the negated Gram matrix -A has signature issues (as the note itself observes for BKM algebras in Section 7.1: "negating the Cartan matrix produces an algebra with the wrong root multiplicities").

The note's own Warning 3.6 states: "The Koszul dual root datum is *not* obtained by simply negating the Cartan matrix." And Section 7.1 gives three reasons why Cartan negation fails for BKM superalgebras. But then *what is the correct prescription for the real roots of the Koszul dual, when G is non-simply-laced?*

For finite-dimensional Lie algebras, Koszul duality sends g to g itself (the (Lie, Com) pair is self-dual). The Langlands involution sends g to g^L, which is a *different* Lie algebra for non-simply-laced types. If chiral Koszul duality preserves the Lie algebra type (as it does for affine KM: k -> -k - 2h^v within the *same* g), then how does the Langlands dual g^L emerge?

The note's answer (Remark at line 912) is: "For affine Kac-Moody algebras, chiral Koszul duality is k -> -k - 2h^v *within the same Lie algebra* g. The Langlands dual algebra g^L appears only through the Feigin-Frenkel center at critical level, not through Koszul duality. The new content of the conjecture is that for *quantum vertex chiral groups* (which incorporate the full BPS/automorphic data), Koszul duality *does* exchange G and G^L."

This is an honest admission, but it means the conjecture asserts something that has *no precedent* in the known examples. Affine KM Koszul duality does NOT produce the Langlands dual; the conjecture claims that the E_2-chiral enhancement magically makes it do so. The mechanism by which this happens is not specified.

The `physics_sduality_langlands.tex` Q1 (line 848) explicitly asks: "How does [the outer automorphism of the Dynkin diagram] manifest in the Koszul duality of quantum vertex chiral groups? The bar-cobar machine of Volume I does not obviously see diagram automorphisms. This may require the 'metaplectic' version of Koszul duality."

So the authors themselves acknowledge that the non-simply-laced case may require a *different* version of Koszul duality that has not been developed.

**Assessment**: For the simply-laced case, the conjecture is tautological (it predicts self-duality, which is at least self-consistent). The only non-trivial content is for non-simply-laced types, precisely where the mechanism is absent.

---

## FINDING 4: The Feigin-Frenkel-Langlands triangle is not commutative

**Severity**: HIGH (mathematical substance)

**Location**: `theory_qvcg_koszul.tex` Section 6.6, equation (6.10) (the triangle).

**The problem**: The note presents a square (equation 6.10):

```
g_hat_k  --chiral Koszul-->  g_hat_{-k-2h^v}
  |                              |
  | Langlands                    | Langlands
  v                              v
g^L_hat_{k^L}  --chiral Koszul-->  g^L_hat_{-k^L-2h^{v,L}}
```

where k^L satisfies (k + h^v)(k^L + h^{v,L}) = 1. The note then asserts that "at the level of quantum vertex chiral groups, the horizontal and vertical arrows compose to give the diagonal: the passage from G(C,G) to G(C,G^L) is Koszul duality."

But this is a claim about *composition* of two different operations (horizontal: chiral Koszul; vertical: Feigin-Frenkel/Langlands). The note explicitly says the vertical arrows "are *not* chiral Koszul duality; they are Feigin-Frenkel/Langlands duality, a different operation." So the conjecture asserts that two different operations (Koszul and FF/Langlands) become the *same* operation after passing to quantum vertex chiral groups.

This is a strong claim. Let us check whether the composition is even consistent numerically. Starting from g_hat_k:

- Chiral Koszul: k -> k' = -k - 2h^v. Still g, not g^L.
- Langlands on the source: k -> k^L where (k+h^v)(k^L+h^{v,L}) = 1. Moves to g^L.
- Langlands on the target: k' -> (k')^L where (k'+h^v)((k')^L + h^{v,L}) = 1, i.e., (-k-h^v)((k')^L + h^{v,L}) = 1. Moves to g^L.

For commutativity we need: (chiral Koszul on g^L at k^L) = (Langlands applied to chiral Koszul of g at k). That is: -k^L - 2h^{v,L} should equal (k')^L where k' = -k-2h^v.

Computing (k')^L: (k' + h^v)((k')^L + h^{v,L}) = 1, so (-k-h^v)((k')^L + h^{v,L}) = 1, giving (k')^L = -h^{v,L} + 1/(-k-h^v) = -h^{v,L} - 1/(k+h^v).

And: -k^L - 2h^{v,L} = -(1/(k+h^v) - h^{v,L}) - 2h^{v,L} = -1/(k+h^v) + h^{v,L} - 2h^{v,L} = -1/(k+h^v) - h^{v,L}.

So (k')^L = -h^{v,L} - 1/(k+h^v) = -k^L - 2h^{v,L}. The square *does* commute numerically at the level of levels. Good.

But at the critical level k = -h^v: k' = -(-h^v) - 2h^v = -h^v = k. And k^L: (k+h^v)(k^L+h^{v,L}) = 1 gives 0 * (...) = 1, which is *undefined*. The Feigin-Frenkel duality (k+h^v)(k^L+h^{v,L}) = 1 does not apply at the critical level. At k = -h^v, the "dual level" in the Langlands sense is k^L = infinity. The note's claim that "at critical level k = -h^v: kappa = 0, so K = 0 + 0 = 0" (line 883) *circumvents* this divergence by going directly to the kappa formula, but the underlying level algebra is not well-defined.

This means the "triangle" picture actually *degenerates* at the critical level, precisely where the conjecture is supposed to be most natural. The Feigin-Frenkel center at k = -h^v is a limiting phenomenon (the center becomes large as k -> -h^v), not a consequence of the duality formula at k = -h^v itself.

**Assessment**: The square commutes generically (away from critical level), but degenerates at k = -h^v. The conjecture is most natural at critical level (where all three dualities "collapse to a single point"), but the formulas break down there. The note should explicitly address this degeneration.

---

## FINDING 5: Categorical level mismatch

**Severity**: HIGH (conceptual architecture)

**Location**: `physics_sduality_langlands.tex` Section 2 and Q6 (line 882); `theory_qvcg_koszul.tex` Remark at line 756.

**The problem**: Geometric Langlands is a *categorical* equivalence:

```
D-mod(Bun_G(C))  ~  IndCoh_Nilp(LocSys_{G^L}(C))
```

Koszul duality in Volume I is an *algebraic* equivalence:

```
A  <-->  A^!  (chiral algebras, related by bar-cobar)
```

These live at different categorical levels. The passage from one to the other requires:

1. A functor from categories to algebras: the CY-to-chiral functor Phi. This is conjectural (CY-A).
2. A demonstration that the *representation category* of G(C,G)^! recovers the Langlands dual category. The note's CY-C (line 1080) asserts this: "Rep^{E_2}(G(C,G)) is braided equivalent to the Langlands-dual representation category Rep^{E_2}(G(C,G^L)) under the braiding reversal q -> q^{-1}." But CY-C is a target theorem, not a proved result.

The note acknowledges this at Q6 (line 882): "The passage from algebra to category is the representation functor. A precise proof would require showing that Rep^{E_2}(G(C,G)^!) = Rep^{E_2}(G(C,G^L)) recovers the Gaitsgory et al. equivalence."

So the "identification" of Langlands duality with Koszul duality is mediated by at least two conjectural functors (Phi and the representation functor), and the verification that the composite reproduces the Gaitsgory et al. equivalence is listed as an *open question*, not a result.

**Assessment**: The claim "Langlands duality IS Koszul duality" is more accurately stated as: "We conjecture the existence of a framework in which Langlands duality can be *expressed as* Koszul duality, contingent on establishing CY-A, CY-B, CY-C, and CY-D for non-compact CY geometries arising from Hitchin systems." This is a research programme, not an identification.

---

## FINDING 6: The conductor formula has an internal inconsistency

**Severity**: MEDIUM (computational)

**Location**: `theory_qvcg_koszul.tex` Proposition 6.5, lines 852-886.

**The problem**: The Hitchin Koszul conductor is defined as:

```
K_{C,G} = (g_C - 1) * dim(g) * (h^v + h^{v,L})
```

But in the proof sketch (line 876), K is computed as:

```
K = kappa(A_{C,G}) + kappa(A_{C,G^L})
  = (g_C - 1) * dim(g) * [ (k + h^v)/(2h^v) + (k^L + h^{v,L})/(2h^{v,L}) ]
```

For this to equal (g_C - 1) * dim(g) * (h^v + h^{v,L}), we need:

```
(k + h^v)/(2h^v) + (k^L + h^{v,L})/(2h^{v,L}) = h^v + h^{v,L}
```

This is *not* true in general. For example, with the Feigin-Frenkel relation (k+h^v)(k^L+h^{v,L}) = 1:

Let u = k + h^v, so k^L + h^{v,L} = 1/u. Then:

```
u/(2h^v) + 1/(2u * h^{v,L})
```

This depends on u and does not simplify to h^v + h^{v,L} unless u takes a specific value. At the "natural normalization" the note refers to (line 884), the formula is supposed to hold, but no such normalization is defined.

At critical level k = -h^v: u = 0, and the formula gives 0 + 0/0, which is undefined (or 0 if we take the limit, contradicting the stated conductor).

The note says: "At critical level k = -h^v: kappa = 0, so K = 0 + 0 = 0." This is correct (kappa vanishes at critical level on both sides since SL_2 is self-dual at the Lie algebra level). But then the *general* conductor formula K = (g_C-1)*dim(g)*(h^v + h^{v,L}) cannot hold at critical level (where it gives a nonzero value) *and* at generic level simultaneously.

For G = SL_2, g_C = 2: the formula gives K = 1 * 3 * (2 + 2) = 12. But at critical level, K = 0. These are contradictory. The formula must apply only at a specific normalization of k that is neither critical nor generic, but the note does not specify which.

**Assessment**: The conductor formula appears to apply at a specific "natural" level but this level is not defined. The formula is inconsistent with the critical level limit. The proof sketch does not close.

---

## FINDING 7: Equivocation on "Koszul duality"

**Severity**: MEDIUM (conceptual clarity)

**Location**: Throughout both notes.

**The problem**: The term "Koszul duality" is used to mean at least four different things:

1. **Classical Koszul duality** of quadratic algebras (the (Lie, Com) self-duality for finite-dimensional g).
2. **Chiral Koszul duality** of Volume I: the bar-cobar adjunction for chiral algebras on Ran(C), sending A to A^! = (H*(Bar(A)))^v.
3. **BKM Koszul duality** for generalized BKM superalgebras: the Borcherds involution on root data (Definition 3.5 in theory_qvcg_koszul.tex).
4. **E_2-chiral Koszul duality**: the E_2 enhancement of (2), which is "the central innovation" of Volume III per CLAUDE.md.

These are not the same operation. (1) preserves the Lie algebra type. (2) sends k -> -k-2h^v within the same g. (3) permutes imaginary roots by omega_B. (4) is not yet defined.

The conjecture claims that *some version* of Koszul duality exchanges G and G^L. But:
- Version (1) does not (it is self-dual).
- Version (2) does not (it stays within the same g, as explicitly noted at line 914).
- Version (3) might, but only if the Borcherds involution happens to agree with the Langlands involution on the root datum -- which is the *content* of the conjecture, not an independent fact.
- Version (4) is supposed to be the right one, but is not yet defined.

The notes frequently slide between these senses. For example, the "dual level formula" k -> -k - 2h^v is presented as a Koszul duality fact (it is, in sense 2), and then the Feigin-Frenkel center at k = -h^v is presented as revealing G^L (it does, but not via Koszul duality). The conjunction of these two facts is presented as evidence for the conjecture, but neither fact individually *is* Koszul duality in sense (4).

**Assessment**: The notes should explicitly tabulate the four senses and state which is being used in each claim. The conjecture should be tied to sense (4) alone, with clear delineation from senses (1)-(3).

---

## FINDING 8: The HMS/Koszul tension for non-simply-laced groups reveals a potential falsifier

**Severity**: MEDIUM-HIGH (potential falsification)

**Location**: `theory_qvcg_koszul.tex` lines 836-848.

**The problem**: For non-simply-laced G, HMS for Hitchin spaces gives:

```
D^b(Coh(M_H(G)))  ~  Fuk(M_H(G^L))
```

Applying the CY-to-chiral functor to both sides:

```
A_{C,G} = Phi(D^b(Coh(M_H(G))))  ~  Phi(Fuk(M_H(G^L))) = A_{C,G^L}
```

So A_{C,G} and A_{C,G^L} are isomorphic as chiral algebras. The conjecture further claims:

```
A_{C,G}^! = A_{C,G^L}
```

Combining: A_{C,G}^! = A_{C,G}. This says A_{C,G} is Koszul self-dual. But G is not simply-laced, and the Koszul dual root datum *changes* the root system (exchanging long and short roots). If A_{C,G} encodes the root datum of G in its structure, and A_{C,G}^! encodes the root datum of G^L (a *different* root system), then A_{C,G} cannot be isomorphic to A_{C,G}^!... unless the chiral algebra A_{C,G} does NOT encode the root system type.

The note resolves this by claiming that HMS gives an isomorphism of *underlying* chiral algebras, while Koszul duality acts on the E_2-enhancement. But this means:
- As chiral algebras: A_{C,G} = A_{C,G^L} (from HMS).
- As E_2-chiral algebras: A_{C,G} != A_{C,G^L} (different braiding).
- As E_2-chiral algebras: A_{C,G}^! = A_{C,G^L} (Koszul duality changes the braiding).

This is logically consistent only if the Koszul involution acts as q -> q^{-1} on the braiding parameter, which transforms the E_2-structure of G-type into that of G^L-type. But for non-simply-laced groups, q -> q^{-1} is NOT the same as the Langlands involution on the braiding. For B_n/C_n, the quantum group U_q(B_n) at q is not isomorphic to U_{q^{-1}}(C_n) in any obvious way. The parameter q is attached to the *short* root in one convention and the *long* root in the other.

This is a potential falsifier: if q -> q^{-1} does not reproduce the Langlands dual braiding for non-simply-laced groups, the conjecture fails.

---

## FINDING 9: The SL_2, g=2 case is not computed

**Severity**: MEDIUM (missed opportunity)

**Location**: `theory_qvcg_koszul.tex` Section 6.1, `physics_hitchin_langlands.tex` Section 8.

**The problem**: The SL_2 Hitchin system at genus g=2 gives a genuine CY3 (dim_C = 6). This is the *unique* case where the Hitchin moduli space is literally a CY3, making it the natural testing ground for the conjecture.

For SL_2: g^L = sl_2 (self-dual at the Lie algebra level), h^v = 2, h^{v,L} = 2.

The conductor formula gives: K = 1 * 3 * (2+2) = 12.

The kappa formula gives: kappa = (k+2)*3/(2*2) * 1 = 3(k+2)/4.

At critical level k = -2: kappa = 0. Conductor K = 0 (both sides vanish). Consistent.

At the "natural" level (whatever that is): kappa + kappa' = rho * K. But what IS the natural level for the Hitchin CY3? The note never says. The root datum construction in `physics_hitchin_langlands.tex` gives the real roots as {+/- alpha} (a single root pair), with imaginary root multiplicities from DT invariants of M_H(SL_2). These DT invariants have been computed by Hausel-Rodriguez-Villegas and others using motivic methods.

The note could and should compute:
- The explicit generalized root datum R(C, SL_2) for genus 2
- The BKM superalgebra associated to this root datum
- The Borcherds involution on this algebra
- Whether the Koszul dual root datum matches R(C, PGL_2)

Since SL_2 is self-dual at the Lie algebra level, this reduces to checking self-duality of the BKM algebra. The Hitchin base is C^3, the spectral curves are hyperelliptic, and the fibre cohomology is known. This computation would either provide strong evidence or reveal a problem.

**Assessment**: The absence of this computation is a significant gap. The one case that is explicitly checkable has not been checked.

---

## FINDING 10: The "triple identification" S-duality = Langlands = Koszul conflates physical and mathematical claims

**Severity**: MEDIUM (epistemic)

**Location**: `physics_sduality_langlands.tex` Conjecture 4.1 and Section 8 (Conclusion).

**The problem**: The note's central "triple identification" equates:
- S-duality: a physical conjecture (Montonen-Olive) about N=4 SYM
- Langlands duality: a proved mathematical theorem (Gaitsgory et al.)
- Koszul duality: a conjectural operation on conjectural objects

These have different epistemic statuses. S-duality is not a theorem; it is established "at the level of the BPS spectrum by Sen, and at the level of partition functions by Vafa-Witten" (line 103), but not as a full equivalence of QFTs. Langlands duality is proved. Koszul duality here is doubly conjectural (the objects and the operation).

Equating a proved theorem with two conjectures of different types is misleading. What the notes actually establish is a *dictionary* (Section 4.2, the table on line 406), mapping concepts from one framework to another. A dictionary is not an identification. The statement "S-duality = Langlands duality = Koszul duality" should be replaced with something like: "There exists a conjectural framework in which S-duality, Langlands duality, and Koszul duality are manifestations of a single underlying operation on quantum vertex chiral groups."

---

## SUMMARY TABLE

| # | Finding | Severity | Status |
|---|---------|----------|--------|
| 1 | G(C,G) not constructed | CRITICAL | Open |
| 2 | Evidence lines are analogies | HIGH | Acknowledged partially |
| 3 | Non-simply-laced mechanism absent | HIGH | Acknowledged at Q1 |
| 4 | FF-Langlands triangle degenerates at critical level | HIGH | Not addressed |
| 5 | Categorical level mismatch | HIGH | Acknowledged at Q6 |
| 6 | Conductor formula inconsistency | MEDIUM | Not addressed |
| 7 | Equivocation on "Koszul duality" (4 senses) | MEDIUM | Not addressed |
| 8 | HMS/Koszul tension for non-simply-laced = potential falsifier | MEDIUM-HIGH | Partially noted |
| 9 | SL_2 genus 2 computation not done | MEDIUM | Not addressed |
| 10 | Triple identification conflates epistemic levels | MEDIUM | Not addressed |

## OVERALL ASSESSMENT

The conjecture G(C,G)^! = G(C,G^L) is a beautiful organizing principle for a research programme. It is NOT a theorem, NOT close to a theorem, and the evidence for it is weaker than the notes suggest. The strongest honest statement is:

*At the critical level, for simply-laced groups, the Feigin-Frenkel center of the affine vertex algebra sees the Langlands dual group. If one could define quantum vertex chiral groups for Hitchin systems and equip them with a Koszul duality compatible with the E_2 structure, it is plausible that this Koszul duality would exchange G and G^L. The non-simply-laced case requires new ideas (possibly metaplectic Koszul duality) that have not been developed.*

The notes are intellectually honest in many places (the warnings, the open questions, the explicit "this is external motivation" remark). But the framing -- especially the boxed equation and the "triple identification" -- oversells the current state of knowledge.
