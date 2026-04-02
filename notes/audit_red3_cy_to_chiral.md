# RED TEAM AUDIT 3: CY-to-Chiral Construction (Theorem CY-A)

**Target**: `notes/theory_cy_to_chiral_construction.tex`
**Auditor**: Adversarial falsification, all four steps
**Date**: 2 April 2026

---

## Summary Verdict

**Theorem CY-A is not a theorem.** It is a partially-proved construction for d=2
and a conjectural programme for d=3. The note is generally honest about this in its
dependency table (Section 7), but the top-level statement (Theorem 5.1 / thm:cy-a)
is labeled [PH] ("proved here") when it should be labeled PH/CJ depending on d.
Below I give seven findings, three of which are genuine gaps.

---

## FINDING 1 [GENUINE GAP]: Step 1 lambda-bracket construction has a hidden circularity

**Location**: Construction 2.5 (constr:lie-conformal-from-cy), equation (2.1)

**The claim**: The Gerstenhaber bracket + CY pairing determine a lambda-bracket on
L_C = HH^{*+1}(C) tensor k[d], and the Lie conformal axioms are verified from
"standard properties."

**The problem**: The lambda-bracket formula (2.1) is presented as a *definition*
determined recursively by the Jacobi identity, with the leading term being [a,b]_G
and the lambda^1 term involving the CY pairing. But the "Verification" paragraph
claims the Jacobi identity *follows from* the Jacobi identity for [,]_G plus
cyclic invariance of the CY pairing. This is circular: you cannot simultaneously
*define* the higher lambda-terms by requiring Jacobi AND *verify* Jacobi from the
input data, unless you prove that the recursive definition is consistent (i.e., that
the system of equations determined by requiring Jacobi at each order in lambda has a
unique solution).

**What is actually needed**: A proof that the map
```
(graded Lie algebra + invariant pairing) --> (Lie conformal algebra)
```
is well-defined. This is a known result in the theory of Lie conformal algebras: given
a Lie algebra g with an invariant symmetric bilinear form B, the *affinization*
g-hat = g tensor k[t,t^{-1}] + k.K carries a lambda-bracket [a_lambda b] = [a,b] +
lambda B(a,b) K. This is the standard Kac-Moody lambda-bracket. The note's
construction *generalizes* this to the case where g is the Gerstenhaber algebra
(graded, bracket of degree -1) and B is the CY pairing (of degree -d).

**The fix**: The note should state explicitly that Construction 2.5 is the
*affinization* of the shifted Gerstenhaber algebra by the CY pairing, cite the
standard result (Kac, "Vertex Algebras for Beginners", Proposition 2.6), and verify
that the grading shifts are compatible. The higher-order terms in (2.1) (the
lambda^2, lambda^3, etc.) are *zero* in the affinization -- they only appear if the
Lie conformal algebra is non-linear (e.g., W-algebra type). The formula as written,
with the "..." suggesting infinitely many higher terms, is misleading: for an
affinization, the lambda-bracket is *linear* in lambda. The presence of higher-order
terms would require additional structure beyond the Gerstenhaber bracket and CY
pairing.

**Severity**: MEDIUM. The construction is correct for the cases of interest (where
the lambda-bracket is linear in lambda, i.e., Kac-Moody type), but the formula (2.1)
overclaims by suggesting a general recursive construction that is not justified. For
non-linear cases (e.g., W-algebra vertex algebras from CY categories with higher
Massey products), the construction would need the full A-infinity structure, not just
the Gerstenhaber bracket.

**Status annotation correction**: Construction 2.5 should be [PE] (affinization is
standard), not [PH].

---

## FINDING 2 [GENUINE GAP]: Step 3 for d=3 -- the "quantum corrections from pi_2" argument is not a proof

**Location**: Warning 3.6 (warn:cy3-symmetric), Theorem 3.5 (thm:e2-enhancement-d3)

**The claim**: For d=3, pi_1(Conf_2(R^3)) = Z/2, so the braiding is symmetric at
the topological level. But "pi_2(Conf_2(R^3)) != 0" provides quantum corrections
that give a non-trivial braiding after deformation.

**The problem**: This is the most critical gap in the construction. Let me be precise:

(a) **pi_2 claim is wrong as stated**. Conf_2(R^3) is homotopy equivalent to S^2
(the direction between two points). So pi_1(Conf_2(R^3)) = 0 (not Z/2 -- the note
confuses the *unordered* configuration space with the ordered one). For the *ordered*
configuration space, pi_1 = 1 (trivial). For the *unordered* configuration space
UConf_2(R^3), pi_1 = Z/2 (the symmetric group). Meanwhile pi_2(Conf_2(R^3)) =
pi_2(S^2) = Z. This Z in pi_2 is what the note wants to use.

(b) **The mechanism for "quantum corrections from pi_2" is not explained**. The
note says the higher homotopy data of the E_3 action "encodes the deformation
parameter hbar". But HOW? In the E_2 case, the braiding comes from pi_1(Conf_2(R^2))
= Z, which acts on the representation category via the braid group action. For E_3,
the analogous pi_1 is trivial (for ordered) or Z/2 (for unordered), giving at most a
symmetric braiding. The pi_2 = Z could in principle give a "secondary" braiding, but:
  - An E_2-algebra structure on a category C gives a braiding on C (a natural
    isomorphism tau: X tensor Y -> Y tensor X).
  - The pi_2 data in an E_3-algebra gives a *homotopy* between tau^2 and the
    identity, not a deformation of tau itself.
  - This homotopy is precisely the data that makes the braiding "closer to
    symmetric," not the data that gives quantum group non-commutativity.

(c) **The physics analogy is misleading**. The note cites 3d N=4 theories where
"braiding is symmetric at tree level but acquires quantum corrections from loop
effects." But in those theories, the non-symmetric braiding comes from the
*failure of formality* of the E_3 operad in the derived setting (i.e., the
E_3-algebra structure on the category O is not formal, and the non-formality gives
deformation parameters). The mechanism is NOT "pi_2 gives quantum corrections" --
it is that the E_3-algebra, when *deformation-quantized*, produces an E_2-algebra
that is not formal. This is a completely different (and much more subtle) argument
than what the note presents.

**What would actually work for d=3**: The correct route to quantum groups from CY3
categories passes through:
  1. The Kontsevich-Soibelman CoHA construction, where the E_3 structure on
     Hochschild homology (via the CY3 S^3-framing) gives a CoHA with an associative
     multiplication (the E_1 inside E_3) and a commutative factorization (the E_2
     inside E_3). The quantum group structure comes from the *associative* direction
     (E_1), not from the braided direction (E_2).
  2. The Drinfeld center of the E_1-monoidal representation category: Z(Rep^{E_1})
     is braided monoidal, and THIS is where the quantum group braiding lives. The
     braiding in the center is non-trivial even though the underlying E_2 braiding
     is symmetric, because the center construction introduces new morphisms.

**Severity**: HIGH. The d=3 case of Theorem CY-A, as currently argued, does not
produce a non-trivially braided category. The claimed mechanism (pi_2 quantum
corrections) is heuristic at best and incorrect at worst. The construction needs
either:
  (a) A fundamentally different argument for d=3 (e.g., via the Drinfeld center
      route), or
  (b) An honest admission that for d=3, the E_2 structure obtained by restricting E_3
      is symmetric, and the quantum group braiding must come from a different source.

**Status annotation correction**: Theorem 3.5 (thm:e2-enhancement-d3) should be [CJ],
not [PH].

---

## FINDING 3 [GENUINE GAP]: Step 4 -- Kaledin degeneration scope

**Location**: Theorem 4.1 (thm:cy-quantization), item (iii)

**The claim**: "Unobstructedness follows from Kaledin's degeneration theorem" for
smooth, proper CY categories of dimension d in {2, 3}.

**The problem**: There are two distinct issues:

(a) **Kaledin's original theorem** (2008) proves Hodge-to-de Rham degeneration for
smooth proper dg algebras (not categories) over a field of characteristic zero. The
extension to dg *categories* requires Keller's Morita-invariance results. The further
extension to the claim that HC^-_*(C) = HH_*(C)[[hbar]] (stated in the proof outline)
is a *consequence* of the degeneration, but the identification as stated is too
strong: what the degeneration actually gives is that the spectral sequence
HH_*(C)[u] => HC^-_*(C) (with u of degree 2) degenerates at E_1. This means
HC^-_*(C) is *free* over k[[u]] with HC^-_*(C) / (u) = HH_*(C), but the isomorphism
HC^-_*(C) ~ HH_*(C)[[hbar]] requires choosing a splitting, which is non-canonical.
The proof outline conflates hbar (the quantization parameter) with u (the Hodge
filtration parameter).

(b) **The implication "degeneration => unobstructed quantization" is not proved**.
The proof says this is "formal given the degeneration," but the deformation theory
of chiral algebras is NOT the same as the deformation theory of associative algebras.
The obstruction to quantizing a chiral Poisson algebra lies in HH^2_{ch}(A^{cl}),
which is a *chiral* cohomology group. The Kaledin degeneration says something about
the Hochschild-to-cyclic spectral sequence of the *input category C*, not about the
chiral cohomology of the *output chiral algebra*. The missing step is: how does the
degeneration of the HC spectral sequence for C translate into the vanishing of
obstructions in HH^2_{ch}(Fact_X(L_C))?

**What would close the gap**: One would need either:
  1. A comparison theorem relating HH^2_{ch}(Fact_X(L_C)) to HC^-_*(C), so that
     degeneration for the latter implies vanishing for the former, or
  2. A direct BV/BRST argument showing that the BV operator Delta = B o iota_sigma
     provides an explicit deformation (not just first-order), and that the higher-order
     terms are determined by the BV master equation, which is satisfied by the CY
     structure.

Route (2) is essentially Costello's approach (2007), and the note invokes it ("the
BV structure from CY is proved in the literature"). But Costello's theorem applies to
*topological* field theories, not directly to chiral algebras. The passage from
Costello's TCFT quantization to chiral algebra quantization requires the
factorization-algebra formalism of Costello-Gwilliam, and specifically the
"factorization quantization" theorem (CG, Volume 2, Chapter 5). The note should cite
this as the actual mechanism, not Kaledin degeneration.

**Severity**: MEDIUM-HIGH. The unobstructedness is almost certainly true for the cases
of interest, but the proof as stated has a logical gap (Kaledin degeneration is about
the wrong object). The fix is to route through Costello-Gwilliam factorization
quantization instead.

**Status annotation correction**: "Unobstructed quantization" should be [PH*] with a
footnote saying it follows from Costello-Gwilliam, not Kaledin.

---

## FINDING 4 [PRESENTATION ISSUE]: pi_1(Conf_2(R^3)) stated incorrectly

**Location**: Warning 3.6, line 497

**The text**: "pi_1(Conf_2(R^3)) = Z/2 (the symmetric group, not the braid group)"

**The correction**: The *ordered* configuration space Conf_2(R^3) has the homotopy
type of S^2, so pi_1 = 0. The *unordered* configuration space UConf_2(R^3) = 
Conf_2(R^3) / S_2 has pi_1 = Z/2. The note should specify which configuration space
it means. Since E_d(2) = Conf_2(R^d) (ordered), the relevant pi_1 is trivial for
d >= 3, which means the braiding for an E_3-algebra (restricted to E_2) is trivial
at the pi_1 level.

**Severity**: LOW (but contributes to the confusion in Finding 2).

---

## FINDING 5 [PRESENTATION ISSUE]: HKR theorem scope for non-commutative CY

**Location**: Theorem 2.2 (thm:cy-hkr)

**The claim**: The CY-HKR decomposition holds for smooth, proper CY categories
over char 0.

**The issue**: The HKR decomposition HH^*(C) ~ bigoplus H^p(C, wedge^q T_C) makes
sense for categories that are "close to commutative" (i.e., derived categories of
varieties, or deformations thereof). For general CY categories (e.g., Fukaya
categories, which are genuinely A-infinity and not derived from a commutative ring),
the right-hand side is not well-defined: "H^p(C, wedge^q T_C)" requires the
categorical tangent complex to decompose, which uses smoothness + formality.

The note does say the isomorphism is "non-canonical" and depends on a formality
quasi-isomorphism. But it does not flag that for non-formal CY categories (e.g.,
Fukaya categories of non-formal symplectic manifolds), the HKR decomposition may
fail entirely. This does not affect the construction (which only needs the
Gerstenhaber bracket on HH^*, not the HKR decomposition), but it makes Theorem 2.2
overclaim.

**Severity**: LOW. The HKR decomposition is used for illustrative purposes (Examples
2.8, 2.9) but is not logically needed for the construction.

---

## FINDING 6 [CORRECT -- NOT A BUG]: Functoriality claim

**Location**: Theorem 5.1(v)

**The claim**: Phi sends CY functors to chiral algebra homomorphisms, and Morita
equivalences to quasi-isomorphisms.

**Verification**: This follows because each step in the construction is functorial:
- Step 1: A CY functor F: C -> D induces a map on HH^* compatible with the
  Gerstenhaber bracket and CY pairing (by functoriality of HH).
- Step 2: Fact_X is a functor from Lie conformal algebras to chiral algebras.
- Step 3: The E_d-enhancement is natural in the CY structure.
- Step 4: Quantization is unique up to gauge, so functorial on the nose.

Morita equivalences preserve HH, so the claim is correct.

**Severity**: NONE. This is fine.

---

## FINDING 7 [BOUNDARY ISSUE]: "Smooth and proper" excludes most examples of interest

**Location**: Definition 1.1 (def:input), stated throughout

**The issue**: The construction requires C to be smooth AND proper. The note
acknowledges in Open Problem O3 that non-compact CY categories require completed
tensor products. But the severity is worse than stated:

- **Wrapped Fukaya categories** Fuk^w(X) are smooth but NOT proper (infinite-
  dimensional Hom spaces). These are the CY categories relevant to 3d N=4 mirror
  symmetry and the main physics motivation.
- **Derived categories of non-compact CY manifolds** (e.g., local CY3 geometries
  like O(-1,-1) -> P^1, or crepant resolutions of singularities) are not proper.
- **Matrix factorization categories MF(W)** for non-isolated singularities are
  neither smooth nor proper in general.
- **Fukaya categories of compact symplectic manifolds** ARE proper (finite-
  dimensional Floer cohomology) but smoothness requires non-degeneracy of the
  Fukaya category, which is conjectural in general (homological smooth = split-
  generated, which is open for most symplectic manifolds).

The bottom line: the "standard landscape" of CY categories (Part V of the monograph)
consists almost entirely of categories that are either non-proper or conjecturally
smooth. The construction as stated applies rigorously only to D^b(Coh(X)) for X a
smooth projective CY manifold -- and for these, the CY-to-chiral construction is
essentially the Beilinson-Drinfeld chiral algebra of the Kodaira-Spencer Lie algebra,
which is well-known.

**Severity**: MEDIUM. This is a scope issue, not a mathematical error. But it
significantly limits the novelty of the construction in its current rigorous form.

---

## OVERALL ASSESSMENT

### What Theorem CY-A actually is:

| Case | Status | Description |
|------|--------|-------------|
| d=2, C = D^b(Coh(S)) for S smooth projective CY2 | THEOREM | All steps proved (literature + this note). Lambda-bracket is affinization. E_2 from Kontsevich-Vlassopoulos S^2-framing. Quantization via Costello-Gwilliam. |
| d=2, C = Fuk(M) for M compact | CONDITIONAL THEOREM | Conditional on smoothness of Fuk(M) (conjectural in general). |
| d=3, C = D^b(Coh(X)) for X smooth projective CY3 | PROGRAMME | Steps 1-2 proved. Step 3 requires chain-level S^3-framing (conjectural) AND the pi_2 mechanism for non-trivial braiding (unjustified). Step 4 unobstructedness argument has a gap. |
| d=3, C = Fuk(X) or wrapped Fukaya | PROGRAMME | All of the above + smoothness/properness issues. |
| d >= 4 | VACUOUS | Braiding is symmetric, so no quantum group content. |

### Recommended changes to the note:

1. **Relabel Theorem CY-A** (thm:cy-a): Split into "Theorem CY-A (d=2)" which is
   genuinely proved, and "Conjecture CY-A (d=3)" which is a programme.

2. **Fix the lambda-bracket construction** (Finding 1): State explicitly that for
   the Kac-Moody type case (which covers all examples), the lambda-bracket is linear
   in lambda (affinization). Reserve the higher-order formula for a remark about
   potential W-algebra generalizations.

3. **Rewrite Warning 3.6** (Finding 2): The "pi_2 quantum corrections" argument is
   not a proof. Replace with an honest discussion of the two routes to quantum groups
   from CY3: (a) the Drinfeld center route, (b) the CoHA route. Acknowledge that
   neither is the direct E_3-to-E_2 restriction.

4. **Fix the unobstructedness argument** (Finding 3): Route through Costello-Gwilliam
   factorization quantization, not Kaledin degeneration (which addresses the wrong
   cohomology).

5. **Fix pi_1 statement** (Finding 4): Ordered Conf_2(R^3) has pi_1 = 0, not Z/2.

---

## Cross-references

- The monograph chapter `chapters/theory/cy_to_chiral.tex` states Theorem CY-A
  only for d=2 (line 27: "CY categories of dimension d = 2"), which is more honest
  than the working note. The working note should match this restriction for the
  theorem statement.
- The fibration note `notes/theory_cy2_cy3_fibration.tex` provides an alternative
  route to CY3 quantum groups via CY2 fibered over an elliptic curve. This may be
  the correct approach for d=3, rather than the direct S^3-framing route.
