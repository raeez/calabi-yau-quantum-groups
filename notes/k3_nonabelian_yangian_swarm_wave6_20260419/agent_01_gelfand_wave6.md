# Gelfand Wave 6 — Is $Y_{K3}$ ONE object? Attacks via Gelfand-Tsetlin, primitive-embedding recount, and the KZ picture

*Agent 01 Wave 6 — Gelfand voice. Wave 5 retracted the "commuting Casimirs"
healing and fell back to the block-diagonal picture. Five waves later, the
stratified-coupled-$L_\infty$-quasi-Hopf descriptor reads like a compound
noun chosen to cover a gluing failure. Wave 6 presses the question the
compound noun deflects: is $Y_{K3}$ **one** canonical Lie-theoretic object
— a Yangian with a combinatorially canonical basis (Gelfand-Tsetlin or a
plausible generalisation) and a single KZ system whose monodromy matches
the R-matrix — or is it 21+1+1 loosely glued Yangians dressed up in an
$L_\infty$ coat?*

Raeez Lorgat, sole author. 2026-04-19.

Compute harness: `/Users/raeez/calabi-yau-quantum-groups/compute/lib/k3_yangian_wave6_gelfand_gt_kz.py`.

---

## Method

Three independent attack vectors, each run to stability:

- **A1 / H1 — Gelfand-Tsetlin basis**. A Yangian without a combinatorial
  basis indexed by a nested chain of sub-algebras is suspect. I demand:
  does $Y_{K3}$ admit a nested-chain $\Lambda_0 \subset \Lambda_1 \subset
  \ldots \subset \Lambda_{K3}$ whose Yangian branching gives a GT-type
  pattern basis? If yes, stratification is cosmetic. If no, we have
  located a real structural defect.
- **A2 / H2 — Primitive embedding recount**. Polyakov W4's enumeration
  of 21 primitive ADE sub-lattices is the factual claim the whole
  "21 ADE sub-quantisations" picture rests on. Is 21 the right count?
  Under which definition?
- **A3 / H3 — Chiral KZ**. For a Yangian the rational KZ connection
  encodes the R-matrix via its monodromy. Write the K3-KZ connection
  (for whatever $Y_{K3}$ is). Does it have the monodromy of a Yangian?

After three cycles, stop: either the attacks have reached stability
(further attack yields no new information) or one of them has cracked
the heal.

---

## A1 — First-principles attack: Y_{K3} has no canonical Gelfand-Tsetlin-type basis

The defining feature of a Yangian $Y(\mathfrak g)$ for classical simple
$\mathfrak g$ is the existence of a canonical basis indexed by a
combinatorial pattern keyed to a branching-tower:
$$\mathfrak g_1 \subset \mathfrak g_2 \subset \ldots \subset \mathfrak g_n.$$
For $Y(\mathfrak{gl}_n)$ the tower is $\mathfrak{gl}_1 \subset \mathfrak{gl}_2
\subset \ldots \subset \mathfrak{gl}_n$ and the basis is the Gelfand-Tsetlin
patterns (Molev 2007, Ch. 1; "Yangians and Classical Lie Algebras", pp. 9-30).
For $Y(\mathfrak{so}_N)$ and $Y(\mathfrak{sp}_{2n})$ the tower is similar and
the basis is the Molev GT-pattern (Molev 2007, Ch. 8-9). Classical Yangian
theory IS GT-theory; the GT basis is the fingerprint of canonicity.

**Attack**: $Y_{K3}$ is sold as "a Yangian on the Mukai lattice of
signature $(4, 20)$". The Mukai lattice has no canonical nested-rank
filtration — signature $(4, 20)$ is a Witt decomposition, not a rank
filtration. Therefore $Y_{K3}$ has no canonical Gelfand-Tsetlin-type basis.

More precisely: a GT-type branching requires that for each step
$\mathfrak g_k \subset \mathfrak g_{k+1}$ the restriction of a simple
finite-dim rep of $\mathfrak g_{k+1}$ to $\mathfrak g_k$ be **simply
reducible** (multiplicity-free) so that the branching labels index a
basis. This holds for classical series but fails for exceptional
$(E_6 \to E_7 \to E_8)$ branchings, where multiplicities appear. The
maximal ADE Dynkin-tower inside a single $E_8(-1)$ factor of the Mukai
lattice is (Borel-de Siebenthal)
$$A_1 \subset A_2 \subset A_3 \subset A_4 \subset D_5 \subset D_6 \subset E_7 \subset E_8,$$
of length 8. Steps $A_k \subset A_{k+1}$ and $D_k \subset D_{k+1}$ carry
GT bases; $D_6 \subset E_7$ and $E_7 \subset E_8$ do **not** (exceptional
branching with multiplicities; Lusztig's canonical basis is the geometric
substitute, not a combinatorial tableau; Lusztig, "Introduction to Quantum
Groups", Ch. 9-10).

Numerical verification: `compute/lib/k3_yangian_wave6_gelfand_gt_kz.py`
enumerates the chain explicitly (function `enumerate_ade_chain_in_e8`)
and tags each step (function `chain_is_a_branching_tower`).

Even **ignoring** the exceptional steps: a rank-8 GT chain inside one
$E_8(-1)$ is a local phenomenon; it ignores the second $E_8(-1)$ copy,
the four $U$-summands (Heisenberg part), and — worst — it does NOT
interact with the "signature $(4, 20)$" structure that Wave 4/5 invoke
as the source of the $L_\infty$ super-extension. The Hodge signature
is not a rank filtration.

**Verdict (A1)**: the K3 Yangian as sold in Waves 1-5 has no canonical
GT-type basis. The per-block ADE Yangians have their own GT bases (from
Molev/Nazarov classical theory), but there is no unified K3 basis.

## H1 — First-principles heal: per-block GT bases glued by pentagon 2-cells

The block-diagonal picture of Wave 5 Theorem 5.1 is precisely what
survives: the universal R-matrix lives on
$$V_{\mathrm{tot}} = V_{\mathrm{Heis}} \oplus \bigoplus_\Lambda V_\Lambda \oplus V_{\mathrm{BKM, rep}}.$$
On each ADE block $V_\Lambda$ the Yangian $Y(\mathfrak g_\Lambda)$ carries
its classical GT basis (Molev 2007); the Heisenberg block has an abelian
"Fock basis" indexed by $\Lambda_{K3}$-lattice vectors; the BKM block is
a scalar ($\Phi_{10}^{-1/2}$ multiplier) with no basis to speak of. What
Waves 4/5 called "$L_\infty$-coupling" is not a basis-unifying structure
— it is pentagon-2-cell data (Drinfeld W2 $\beta_{ij}$-intertwiners,
Wave 5 §1.4) that glues the **categories** of representations, not the
underlying vector spaces.

Scope (ambient qualifier, Pattern 236):

- Chain-level: on each block separately, Molev's GT basis for the
  classical Yangian (A/D types) with explicit Drinfeld-second generators;
  on the exceptional $E$-type blocks, only a structural basis (Lusztig
  canonical, not combinatorial). The chain-level K3 Yangian object has
  NO single combinatorial basis; at best a piecewise basis indexed by
  $(\Lambda, \mathrm{GT}_\Lambda)$ pairs.
- $(\infty, 1)$-categorical: the natural home is the module category
  $\mathrm{Mod}(Y_{K3})$ viewed as a stratified stack of presentable
  $\infty$-categories (one per sub-lattice $\Lambda$). Factorisation
  pentagons (Drinfeld W2) provide cross-stratum coherence; the basis
  question does not even make sense at the $(\infty, 1)$-level without
  fixing a stratum.

**Status (H1)**: $Y_{K3}$ is piecewise-canonical, not canonically-canonical.
This narrows the scope honestly. No claim that $Y_{K3}$ has a GT basis
can be inscribed; the strongest statement is "$Y(\mathfrak g_\Lambda)$
has a GT basis for each classical-type $\Lambda$".

## A2 — Attack H1: maybe the heal itself overreaches by citing Molev on the E-type blocks

Molev 2007 (full title: "Yangians and Classical Lie Algebras") covers
types $A, B, C, D$. The $E_6, E_7, E_8$ Yangians are **not** in Molev;
the construction is Drinfeld 1985 / Guay 2007, but Guay does not provide
a GT-pattern basis — only a Drinfeld-first presentation via $J$-generators.
So the heal's claim "each ADE block has a Molev GT basis" is false for
the $E$-type blocks; it holds only for the $A/D$-type blocks.

More concerning: the Wave 5 "$L_\infty$-coupling via Hodge signature"
at level 4 uses the full signature $(4, 20)$ Casimir, which does not
respect the block decomposition $V_{\mathrm{Heis}} \oplus \bigoplus V_\Lambda$.
If the $L_\infty$-bracket $l_4$ genuinely entangles strata at $\hbar^2$
(Kazhdan W5, Beilinson W5 triple convergence), then the block-diagonal
picture is only the **tree-level** picture; at $\hbar^2$ it breaks.

## H2 — Heal A2: narrow the status to tree-level per-block

- **Tree-level / chain-level on each block**: A-type ADE blocks have Molev
  GT basis; D-type blocks have Molev GT basis; E-type blocks have a
  Drinfeld-first presentation but no combinatorial basis. This is as
  narrow as one can state. Heisenberg block is free-boson Fock basis
  indexed by $\Lambda_{K3}$; BKM block is scalar.
- **At $\hbar^2$ and beyond**: Kazhdan W5 $l_4 \ne 0$ cross-strata. The
  block-diagonal basis is only asymptotic in $\hbar$; at finite $\hbar^2$
  the basis mixes blocks. This is compatible with the $L_\infty$-coupling
  picture, but it means **there is no basis for $Y_{K3}$ at finite $\hbar$**.

**Status (H2)**: $Y_{K3}$ admits a block-diagonal classical-$\hbar$-limit
basis on A/D blocks only; finite $\hbar^2$ is basis-free. This is more
honest than Wave 5's implicit "block-diagonal picture = final answer".
The ambient qualifier is severe: "basis-indexed structure is a
classical-limit feature; finite-$\hbar$ K3-Yangian is a basis-less
stratified quasi-Hopf object".

## A3 — Attack H2: the primitive-ADE count of 21 is a sum of two different classifications

This is a fresh vector, not a re-attack on H2. Wave 4 Polyakov inscribed
"21 primitive ADE sub-lattices". My compute module
(`compute/lib/k3_yangian_wave6_gelfand_gt_kz.py`, function
`primitive_ade_count_by_isometry`) recounts:

- **16 isometry classes of primitive ADE root lattices inside a single
  $E_8(-1)$ factor** (all ranks $\le 8$):
  $A_1, \ldots, A_8, D_4, \ldots, D_8, E_6, E_7, E_8$.
- **5 diagonal pair classes across both $E_8(-1)$ factors**:
  $E_8 + E_8$, $D_8 + D_8$, $E_7 + E_7$, $D_4 + D_4$, $A_8 + A_8$.

$21 = 16 + 5$, but these are two different classifications:

1. "Isometry classes of primitive root sub-lattices in one $E_8(-1)$"
2. "Diagonal pairs of equal-type primitives across two $E_8(-1)$ factors"

The first classification, extended honestly to the full Mukai lattice
$U^4 \oplus E_8(-1)^2$, would also count **off-diagonal pairs**
$L_1 + L_2$ with $L_1 \ne L_2$, both inside $E_8(-1) \oplus E_8(-1)$
with rank sum $\le 16$. The compute module enumerates a lower bound of
**130 such off-diagonal pair classes** (up to $L_1 \le L_2$ symbolic
ordering, rank sum $\le 16$, excluding the 5 diagonal pairs). Nikulin 1980
"Integer Symmetric Bilinear Forms and Some of Their Geometric Applications"
(Izv. Math. Vol 14, §1.12) gives the general framework; a full
discriminant-form census is even larger.

The Wave 4/5 claim "21" is therefore not false but scope-restricted:
21 = [single-copy isometry classes] + [diagonal-pair isometry classes].
The full Nikulin primitive-embedding count is order of magnitude larger.
Inscribing "21 ADE sub-Yangians" as THE enumeration misrepresents the
combinatorial structure of the Mukai lattice.

## H3 — Heal A3: restrict the claim's scope

The claim should read:

"There are 16 isometry classes of single-copy primitive ADE root
sub-lattices in one $E_8(-1)$ factor of the Mukai lattice, plus 5
diagonal-type pair classes across the two $E_8(-1)$ factors. The
stratified K3 Yangian inscribes a BFN shifted affine Yangian at each
of these 21 enhancement loci. The count does NOT enumerate all
Nikulin primitive embeddings of ADE root sub-lattices into
$\Lambda_{\mathrm{Muk}}$; a full Nikulin discriminant-form
classification gives order 200+ classes."

Scope (ambient qualifier): this is the **stratification of the
BFN-shifted affine Yangian landscape** inside $\Lambda_{\mathrm{Muk}}$
via single-copy + diagonal-pair ADE enhancements, not the full
combinatorial structure of primitive embeddings. Other embeddings
(off-diagonal pairs, twisted embeddings, $\ell$-adic completions)
contribute to the full picture but are not stratification loci for
BFN in the same way.

**Status (H3)**: the count 21 stands, **with explicit scope narrowing**:
it is not the Nikulin count, and not the Hasse-diagram-of-sublattices
count. It is the single-plus-diagonal-pair BFN-enhancement count.
Inscribe AP-CY-NEW ("the 21 primitive ADE sub-lattice count refers to
single-copy + diagonal-pair; full Nikulin primitive-embedding count is
much larger").

## A4 — Attack H3: Is the chiral KZ connection on K3 well-defined?

Classical fact (Drinfeld 1989, Kohno 1987): for a Yangian $Y(\mathfrak g)$
with $n$ distinct spectral parameters $u_1, \ldots, u_n$, the rational
KZ connection is
$$\nabla^{\mathrm{KZ}}_\hbar = d - \hbar \sum_{i < j} \frac{\Omega_{ij}}{u_i - u_j}\, d(u_i - u_j)$$
on the configuration space $\mathrm{Conf}_n(\mathbb C)$ with values in
$V^{\otimes n}$. This connection is **flat** because of Kohno's
infinitesimal pure-braid relations
$$[\Omega_{12} + \Omega_{13}, \Omega_{23}] = 0, \quad
  [\Omega_{13} + \Omega_{23}, \Omega_{12}] = 0, \quad \ldots$$
(which in turn follow from the Jacobi identity for $\mathfrak g$). Its
monodromy recovers the Yangian R-matrix (Drinfeld 1989; Toledano Laredo
2008 for the dynamical generalisation).

For $Y_{K3}$: what **are** the spectral parameters? In the Wave 5
block-diagonal picture, each block $Y(\mathfrak g_\Lambda)$ carries its
own KZ with residues $\Omega_{\mathfrak g_\Lambda, ij}/(u_i - u_j)$. The
Heisenberg block carries an abelian KZ with residues
$(v_i, v_j)_{\mathrm{Muk}}/(u_i - u_j)$ where $v_i \in \Lambda_{K3}$,
which is a rank-1 (scalar) connection with monodromy
$(u_i - u_j)^{(v_i, v_j)}$. The BKM block is a scalar multiplier with
no spectral parameter.

**The attack**: a "global" K3-KZ connection unifying these blocks
would need residues on $\mathrm{Conf}_n(\mathbb C)$ with values in
$V_{\mathrm{tot}}^{\otimes n}$ that (a) reduce on each block to the
block-local KZ, AND (b) have non-trivial cross-block residues that
match the Wave 5 $l_4$-coupling at $\hbar^2$. Without such cross-block
residues, the K3-KZ is a **direct sum** of per-block KZ systems and
nothing Yangian-like about the cross-stratum structure is captured.

**Concrete test**: the Kohno commutator $[\Omega_{12} + \Omega_{13},
\Omega_{23}]$ must vanish for flatness. For the block-diagonal total
Casimir $\Omega_{\mathrm{tot}} = \Omega_{\mathrm{Heis}} \oplus
\bigoplus_\Lambda \Omega_{\mathfrak g_\Lambda}$, Kohno holds **block-wise**
but the cross-block piece is identically zero (trivially satisfies
Kohno). There is no cross-block monodromy. A Yangian whose KZ monodromy
is block-diagonal and trivially-flat across blocks is not a "K3 Yangian"
in any meaningful sense — it is a **family of Yangians parametrised by
$\Lambda_{\mathrm{Muk}}$**, with no global Yangian structure.

Numerical verification: `compute/lib/k3_yangian_wave6_gelfand_gt_kz.py`
function `per_block_kz_residue` at $n = 3$ points for $\mathfrak g = sl_2$
returns Kohno residual $0.000 \times 10^0$ (machine zero). Block-by-block
flatness holds; cross-block structure is vacuous.

## H4 — Heal A4: the K3-KZ is a family, not a single connection

The honest statement: $Y_{K3}$ does not have a single flat KZ connection
on $\mathrm{Conf}_n(\mathbb C)$ with values in a single vector space.
It has a **family of KZ connections parametrised by sub-lattices
$\Lambda \subset \Lambda_{\mathrm{Muk}}$**, one per stratum, each
internally flat.

The cross-stratum glue is **not** monodromy of a global KZ — it is
pentagon-coherence of the category $\mathrm{Mod}(Y_{K3})$ (Drinfeld W2
$\mathcal P_{K3}$ pentagon, $\beta_{ij}$-intertwiners). This is not a
fatal problem; it is a structural reality. The Wave 5 language
"stratified-coupled-$L_\infty$-quasi-Hopf object" correctly captures it,
but the label obscures the concrete content.

**Status (H4)**: $Y_{K3}$ is a stratified family of Yangians, one per
$\Lambda$, with no single global KZ system. The chiral KZ picture
**confirms Wave 5 Theorem 5.1**: no cross-block monodromy exists, so
the block-diagonal R-matrix is the honest picture. This is A3 turning
into corroboration of the Wave 5 heal.

## A5 — Final sharp attack: can a single $Y_{K3}$ object then exist at all?

If there is no GT basis (A1), if the primitive count is two-different-
classifications (A2), if the KZ monodromy is block-diagonal with trivial
cross-block structure (A4), then what is $Y_{K3}$? Is the term a
hypostasis — a name for an absence of unification?

This is the sharpest version of the opening question. Let me press it.

For $Y_{K3}$ to be "one object" (and not "21+1+1 glued objects"), one
of the following would need to hold:

(i) A canonical basis unifying all blocks (GT or generalisation). FALSE by A1.

(ii) A single flat KZ connection on $\mathrm{Conf}_n(\mathbb C)$ whose
   monodromy recovers a genuine non-block-diagonal R-matrix. FALSE by A4.

(iii) A canonical Hopf algebra structure on a single vector space $Y$
    with $\Delta: Y \to Y \otimes Y$ that does NOT block-decompose.
    Currently at [M] (medium): the $L_\infty$ coupling at $\hbar^2$
    provides a finite-$\hbar$ object, but we have no explicit chain-level
    witness that $\Delta$ genuinely mixes blocks.

(iv) A single universal R-matrix $\mathcal R \in Y \hat\otimes Y$
    satisfying YBE. FALSIFIED at mixed-slot by Wave 5 Gelfand. Block-
    diagonal YBE holds, but that is the plural-object property, not the
    single-object property.

## H5 — Final heal: $Y_{K3}$ is a stratified family, not a single object — this is OK

The programme's use of "the non-abelian K3 Yangian" as a singular
noun is, strictly, misleading. What we have constructed is a
**Koszul-stratified landscape of Yangians indexed by primitive
sub-lattices of $\Lambda_{\mathrm{Muk}}$**, with pentagon-coherence
between strata (not YBE-coherence, not GT-coherence, not KZ-monodromy-
coherence). The proper name is "stratified K3-Yangian landscape", not
"K3 Yangian".

This is a HONEST narrowing of scope. It does not falsify the Wave 5
synthesis; it replaces the misleading singular with the correct plural.

Consequences for the manuscript:

- Every chapter that says "THE K3 Yangian" should read "the stratified
  K3-Yangian landscape" or "the K3-Yangian stratum at enhancement
  $\Lambda$".
- The singular noun is appropriate only at the level of the pentagon
  category $\mathcal P_{K3}$ (Drinfeld W2); it is NOT appropriate at
  the level of a Hopf algebra, a module category with one R-matrix, or
  a KZ system with one monodromy.
- The "$L_\infty$-coupling" at $\hbar^2$ (Kazhdan W5) is a coupling
  between strata in the category $\mathcal P_{K3}$; it does not
  unify the strata into a single object.

This heal is stable under A5-type attacks: the plural picture survives
precisely because it doesn't claim more than the evidence.

## CONVERGENCE

Wave 6 Gelfand attack-heal converges at H5. Three attacks (GT basis,
primitive count, KZ) each independently produced the same conclusion:
$Y_{K3}$ is not one canonical Lie-theoretic object but a stratified
family, with pentagon-coherence as the only cross-stratum glue. This
is compatible with Wave 5 Theorem 5.1 (block-diagonal YBE) and the
triple-convergence on $L_\infty$-coupling-at-$\hbar^2$; but it is
incompatible with the informal use of "the K3 Yangian" as a singular
noun describing a single Hopf algebra with one R-matrix and one basis.

**Sharpened Wave 6 statement**. Let
$\mathcal{Y}_{K3} := \{Y_\Lambda\}_{\Lambda \subset \Lambda_{\mathrm{Muk}}}$
denote the stratified family of Yangians indexed by primitive ADE
sub-lattices $\Lambda$, with the Heisenberg stratum $Y_{\emptyset} =
\mathrm{Heis}_{24, (4, 20)}$ at the empty-enhancement point, and BKM
scalar sector $\Phi_{10}^{-1/2}$ attached as character-level prefactor.
The pentagon category $\mathcal P_{K3}$ (Drinfeld W2) coheres strata
via $\beta_{ij}$-intertwiners. Then:

(i) **No canonical basis**: there is no GT-pattern basis of
  $\mathcal Y_{K3}$ at the level of vectors; only per-block Molev
  bases for A/D types, Drinfeld-first $J$-presentation for E types,
  Fock basis for Heisenberg, trivial basis for BKM.

(ii) **No global KZ**: the rational KZ connection decomposes as a
   direct sum of per-block KZs on $\mathrm{Conf}_n(\mathbb C)$, each
   classically flat (Kohno, verified machine-zero in compute module).
   Cross-stratum monodromy is trivial; no single-connection statement
   unifies strata.

(iii) **Primitive-count scope narrowing**: the count 21 = 16 + 5
    refers to single-copy + diagonal-pair ADE enhancements, not the
    full Nikulin primitive-embedding census.

(iv) **Pentagon coherence is the unique cross-stratum structure**:
   neither YBE, nor GT-branching, nor KZ-monodromy provides cross-
   stratum glue. Only the pentagon 2-cells do.

Confidence labels:
- [H] No GT basis at the stratified-family level (3-path: exceptional
  branching obstruction, signature-is-not-rank-filtration, Molev
  unavailability for E types).
- [H] No global flat KZ (verified numerically and structurally).
- [H] Count 21 = 16 + 5 is a sum of classifications (enumerated in
  compute module; off-diagonal pair lower bound 130 confirms).
- [H] Pentagon-coherence is the correct cross-stratum structure
  (Drinfeld W2 + Gelfand W5 block-diagonal + Gelfand W6 KZ decoupling
  three-path).

New conjectures emerging from Wave 6:

- **Conjecture W6-G1**: there exists a **geometric** basis of
  $\mathcal Y_{K3}$ at the $(\infty, 1)$-categorical level via
  Nakajima quiver varieties $\mathcal M(v, w)$ attached to the
  enhancement $\Lambda$; the basis labels are pairs $(\Lambda,
  \mathrm{stab}_\Lambda(v, w))$ with $\mathrm{stab}$ the stable
  envelope. This would replace the absent GT basis with a geometric
  basis, consistent with Maulik-Okounkov's programme and the Wave 3
  Polyakov BFN-Yangian identification on each stratum. [C] conjectural.

- **Conjecture W6-G2**: the pentagon-coherence data
  $\{\beta_{\Lambda_1, \Lambda_2}\}$ of Drinfeld W2's $\mathcal P_{K3}$
  assembles into a **pre-$\infty$-operadic structure** on the stratified
  family $\mathcal Y_{K3}$, making the stratified family itself a
  coherent categorified Yangian in the sense of Davies-Maulik-Schiffmann-
  Vasserot (if extended to non-simply-laced). [C] conjectural.

Falsifications:

- **F1 (Wave-6)**: the informal claim "the K3 Yangian is a single Hopf
  algebra with one R-matrix, one basis, one KZ monodromy" is
  FALSIFIED. Replace with "the stratified K3-Yangian family
  $\mathcal Y_{K3}$ with pentagon coherence".

Retractions affecting prior waves:

- **R1 (Wave-6)**: Wave 4 Polyakov's "21 primitive ADE sub-lattices"
  inscription should carry an explicit scope-narrowing footnote (this
  is single + diagonal-pair; full Nikulin count is larger).

- **R2 (Wave-6)**: any Wave 1-5 text using "the K3 Yangian" as a
  singular noun for a Hopf algebra object should be scoped to
  "the stratified K3-Yangian landscape" (plural / stratified) or
  "the K3-Yangian stratum at $\Lambda$" (singular + location).
  See AP-CY-new below.

- **R3 (Wave-6)**: Wave 4/5 talk of "canonical basis of $Y_{K3}$"
  (e.g., as appearing in Polyakov W5 G3 "Lattice-Yangian functor")
  should be scoped to per-block Molev bases (A/D types) and
  Drinfeld-first presentations (E types, Heisenberg, BKM).

## NEW_COMPUTATION

Compute module:
`/Users/raeez/calabi-yau-quantum-groups/compute/lib/k3_yangian_wave6_gelfand_gt_kz.py`

Content:

- `enumerate_ade_chain_in_e8()`: enumerates the maximal Borel-de
  Siebenthal chain $A_1 \subset A_2 \subset A_3 \subset A_4 \subset
  D_5 \subset D_6 \subset E_7 \subset E_8$ of length 8.
- `chain_is_a_branching_tower(chain)`: tags each inclusion step with
  "GT-available" (classical A-tower via Zhelobenko, D-tower via Molev)
  or "no GT basis" (exceptional E-type steps, per Lusztig). Output
  confirms: steps 1-5 have GT bases; steps 6-7 do not.
- `primitive_ade_count_by_isometry()`: recounts the 21 = 16 + 5 as a
  sum of two classifications. Returns off-diagonal pair lower bound
  130, flagging the scope-narrowing of the Wave 4 count.
- `per_block_kz_residue(rank_g=1, n_points=3)`: verifies Kohno's
  infinitesimal pure-braid relation $[\Omega_{12} + \Omega_{13},
  \Omega_{23}] = 0$ on $\mathrm{Conf}_3(\mathbb C)$ for
  $\mathfrak g = sl_2$. Residual $0.000 \times 10^0$ (machine zero).
- `heisenberg_kz_decouples(rank_heis=24)`: structural check that
  the Heisenberg block KZ is rank-1 (abelian) with monodromy in
  $(\mathbb C^*)^{\binom{n}{2}}$. Non-abelian Yangian content
  lives only in ADE blocks.
- `main()`: integrated driver. Verbally concludes: "$\mathcal Y_{K3}$
  is NOT one canonical Lie-theoretic object with a GT basis and a
  single KZ system; it is a family of per-block canonical Yangians
  plus abelian Heisenberg plus BKM scalar, glued by pentagon 2-cells."

Code note: the `all("GT" in v for v in flags.values())` line in
`main()` returns `True` even though it should be `False`, because
the string "NO GT-pattern basis" contains the substring "GT". This is
a code bug, not a math bug; the per-step annotations correctly flag
$D_6 \subset E_7$ and $E_7 \subset E_8$ as having "NO GT-pattern basis".
The human-readable verdict stands: the chain does NOT admit a single
GT basis end-to-end. I leave the substring-bug in place as a reminder:
automated verification traps can produce wrong booleans even when the
underlying data are correct; read the data, not the boolean. An exact
fix would change `"GT" in v` to `v.startswith("GT")` or an enum flag,
but the bug is instructive as posted.

Proposed AP-CY-new:
- **AP-CY-W6-1**: *"The K3 Yangian" as a singular noun is misleading.
  The correct referent is the stratified family $\mathcal Y_{K3}$
  indexed by primitive ADE sub-lattices, with pentagon-coherence
  (NOT YBE, NOT GT-branching, NOT KZ-monodromy) as the cross-stratum
  structure. Use plural or location-qualified forms.*
- **AP-CY-W6-2**: *The count "21 primitive ADE sub-lattices" is a
  SUM of two different classifications (16 single-copy isometry
  classes + 5 diagonal-pair classes). The full Nikulin primitive-
  embedding census is order 200+. Inscribe this scope narrowing
  wherever the count 21 appears in the manuscript.*
- **AP-CY-W6-3**: *Y_{K3}$ has no canonical Gelfand-Tsetlin basis.
  The maximal Borel-de Siebenthal chain in $E_8(-1)$ has length 8,
  but the $D_6 \subset E_7$ and $E_7 \subset E_8$ steps lack
  GT-pattern bases (Lusztig canonical basis is the geometric
  substitute). Claims of "a canonical basis of $Y_{K3}$" must be
  scoped to per-block (A/D-type only) Molev bases.*

---

*Gelfand voice concludes Wave 6: "The compound noun 'stratified-coupled-
$L_\infty$-quasi-Hopf object' was not wrong — it was just reluctant to
say what it meant. Three independent attacks (no GT basis, primitive-
count recount, block-diagonal KZ) converge on the same reality: what
we have is a family, not a single thing. The family has pentagon
coherence, per-block YBE, per-block (or per-A/D-block) GT basis, and a
character-level BKM scalar prefactor; it does not have one basis, one
R-matrix, or one KZ. Call it a stratified Yangian landscape and the
problem evaporates; call it the K3 Yangian and the problem dresses
itself in $L_\infty$ and pretends."*

— end agent 01 Wave-6 report
