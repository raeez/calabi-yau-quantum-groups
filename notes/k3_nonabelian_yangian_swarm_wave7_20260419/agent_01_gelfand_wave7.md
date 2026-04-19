# Agent 01 — Gelfand Wave 7. Combinatorial demolition of $Y_{\mathrm{BFN}}(K3)$ and the Siegel/BKM bridge

*Wave 7. I. M. Gelfand voice. Raeez Lorgat, sole author. 2026-04-19.*

**Premise.** Six waves converged on "stratified landscape with pentagon
glue" (SYNTHESIS_WAVE6_ADVERSARIAL §7, §8): a K3 Yangian that is not
one object, not one Hopf algebra, not one basis, not one KZ system,
not one R-matrix. Wave 6 then reopened the very anchors —
`thm:phi-k3-explicit` and `thm:bfn-phi-ade-identification` —
revealing that the $\Phi$-infrastructure on which the K3-Yangian
programme rests is itself not a theorem but a "research programme"
(cy_to_chiral.tex:94–103, `rem:phi-not-unified-functor`).

In the programme I co-founded (Gelfand 1950 / Gelfand–Tsetlin 1950
*Doklady* 71: 825–828, 1017–1020), representation theory is not
done by adjective. A Yangian is a combinatorial object: basis indexed
by patterns, modules indexed by patterns, representation theory
computed by counting patterns satisfying branching inequalities,
Plancherel measures given by dimension formulas. The Wave 1–6
corpus produced the word "Yangian" attached to many decorations
("stratified", "coupled", "$L_\infty$", "quasi-Hopf", "BFN-flavoured",
"pentagon-cohered") and not one basis of one module.

Wave 7 demands something new: in light of the **automorphic
corrections paper** (`raeez.lorgat.automorphic-corrections.pdf`,
which gives an **explicit** generator–relation presentation of a
generalised BKM superalgebra $\mathfrak g_{\Delta_5}$ on a **rank-3
hyperbolic lattice** $\Lambda^{2,1}_{II}$ with Gram matrix
$\begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix}$
— not rank 24, not the Mukai lattice, not the whole Niemeier zoo, but
a *rank-3 triangle* with explicit Weyl vector, explicit real simple
roots, and explicit imaginary-simple-root multiplicities read off
from the K3 elliptic genus via the automorphic correction
$\mathfrak g \to \mathfrak g_{\Delta_5}$), the question sharpens:

> Is the true "non-abelian K3 Yangian" in fact the Yangian of
> $\mathfrak g_{\Delta_5}$ — a **rank-3 hyperbolic BKM superalgebra**,
> NOT a rank-24 Mukai object, NOT the stratified family of
> ADE-Kleinians, NOT the $L_\infty$-compound of Waves 4–5?

This is the Wave-7 hypothesis I now falsify and heal.

Five ATTACK–HEAL cycles follow. Each attacks a different pillar of
what is currently called "$Y_{\mathrm{BFN}}(K3)$". Each heal extracts
the surviving core. Cycle 5 arrives at a convergent statement and
the Siegel/BKM answer.

Compute reference for this voice:
`/Users/raeez/calabi-yau-quantum-groups/compute/lib/k3_yangian_wave7_gelfand_bkm_gram.py`
(to scaffold; contains Gram matrix checks of $\Lambda^{2,1}_{II}$,
Weyl vector consistency, and discriminant comparisons against
$\Lambda_{\mathrm{Muk}} = II_{4,20}$).

---

## Preflight — what Wave 6 concluded, what I suspect is still wrong

**Wave 6 convergent position** (my own H5, agent 01 Wave 6; and SYNTHESIS_WAVE6_ADVERSARIAL §5.2):

- $Y_{K3}$ is "a stratified family $\{Y_\Lambda\}$ indexed by primitive
  ADE sub-lattices $\Lambda \subset \Lambda_{\mathrm{Muk}}$, with
  pentagon coherence between strata; no GT basis, no global KZ,
  no single R-matrix".
- The count 21 = 16 + 5 is single-copy + diagonal-pair ADE enhancements;
  full Nikulin primitive embeddings are $\sim 200$.
- Claims of "the K3 Yangian" as a singular noun are inappropriate
  above the pentagon-category level.
- Independently in the same wave: the manuscript's own $\Phi_2$ is a
  programme (not a functor); `thm:phi-k3-explicit` is conditional on
  $\Phi_2$ being well-defined with fixed $\mathcal M_2$, Conjecture 1
  functoriality, and the hypotheses (H1)–(H3).

**What I now suspect is still wrong with this convergent position**:

1. **The rank-24 framing may be a red herring.** The automorphic
   corrections paper operates not on $\Lambda_{\mathrm{Muk}} = II_{4,20}$
   (rank 24) but on a rank-3 hyperbolic sublattice
   $\Lambda^{2,1}_{II} \subset \Lambda^{3,2} \cong \bigwedge^2 \Lambda^4$
   (where $\Lambda^4$ is a free $\mathbb Z$-module of rank 4). The
   signature of $\Lambda^{2,1}_{II}$ is $(2,1)$: indefinite, hyperbolic,
   rank 3. *This* is where $\Delta_5$ exhibits the explicit BKM
   structure. The rank-24 / signature-$(4,20)$ embedding of the Mukai
   lattice has no analogous explicit BKM.
2. **The Gram matrix of the real simple roots is concrete**: $(\delta_i, \delta_j) = \begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix}$
   (automorphic-corrections p. 7, §4). This is the Cartan matrix of a
   rank-3 hyperbolic Kac–Moody algebra $\mathfrak g$ (determinant $= 0$,
   in fact $\det = 16 \cdot ?$; certainly not positive-definite).
   No Wave 1–6 output ever wrote this matrix.
3. **Imaginary simple roots are indexed by lattice points of positive
   $m(a) < 0$ or $\tau(a) > 0$ with $(a,a) \le 0$ in the
   hyperbolic cone.** Multiplicities are $\mathrm{mult}\alpha = f(4nm - l^2, l)$
   for the K3 elliptic genus Fourier coefficients $f(n,l)$ (automorphic-corrections §6).
4. **The "Yangian of a hyperbolic Kac–Moody" is not a standard object.**
   Guay 2007 constructs Yangians of affine Kac–Moody; no-one constructs
   a Yangian of a *hyperbolic* Kac–Moody, and certainly not of a
   *generalised* BKM superalgebra. My suspicion: the
   "non-abelian K3 Yangian" is either (a) rigorously the Yangian of
   $\mathfrak g_{\Delta_5}$'s rank-3 symmetric Cartan part (but this is
   a finite-rank object orthogonal to Mukai-rank-24 claims), or (b) not
   a Yangian at all but an affine factorisation algebra associated to
   the denominator function $\Phi$ on $\mathbb H_2 / \mathrm{Sp}_4(\mathbb Z)$.

I now attack each of these suspicions.

---

## CYCLE 1 — ATTACK: rank is undefined for $Y_{\mathrm{BFN}}(K3)$ because no Cartan subalgebra exists

**Claim under attack**: $Y_{\mathrm{BFN}}(K3)$ has rank $r \in \{24, 22, 4+20, 26\}$ for some specific choice consistent with $\Lambda_{\mathrm{Muk}}$.

### A1. The rank question is ill-posed without a Cartan.

In classical Yangian theory, the **rank** of $Y(\mathfrak g)$ is the
rank of the underlying simple Lie algebra $\mathfrak g$: its Cartan
subalgebra $\mathfrak h \subset \mathfrak g$ has dimension equal to
the rank, and the Drinfeld-J presentation has $\mathrm{rank}(\mathfrak g)$
copies of the $h$-generators. For $Y(\mathfrak{gl}_n)$, rank is $n$;
for $Y(\mathfrak{so}_N)$, rank is $\lfloor N/2 \rfloor$. The rank is
the number of simple-root directions; the basis of $\mathfrak h$ is
dual to the simple roots.

For the purported $Y_{\mathrm{BFN}}(K3)$, there is no named Cartan.
`k3_yangian_chapter.tex:1` opens: "The K3 double current algebra
$\mathfrak g_{K3}$ is the classical limit of the K3 Yangian
$Y(\mathfrak g_{K3})$, whose 24 Heisenberg generators, Mukai-signature
Serre relations, and degree-$(24, 24)$ structure function encode the
quantization of the Mukai lattice." The phrase "24 Heisenberg
generators" suggests rank 24, but these are the **abelian** generators
of $\cH_{\mathrm{Muk}}$ — which is the *abelian* free-field part, not
the Cartan of a non-abelian Yangian.

The attack: **the rank-24 framing treats the Mukai lattice as if it
were a Cartan, which it is not**. $\Lambda_{\mathrm{Muk}} \otimes \mathbb C$
is an abelian Lie algebra (it has no root decomposition: all simple
roots are defined via a choice of indefinite pairing and a choice of
positive cone, and any choice depends on a *sublattice* of
$\Lambda_{\mathrm{Muk}}$, not the whole thing). Drinfeld W6 verified
this numerically: the Drinfeld cobracket $\delta(x) = [x \otimes 1, C]$
vanishes identically on abelian input, so no non-trivial Yangian
structure arises on $\Lambda_{\mathrm{Muk}}$ as written.

### A1 sharpened via the automorphic-corrections paper.

The paper constructs a specific Kac–Moody algebra $\mathfrak g$ (p. 8,
§5) whose real Cartan part is $\Lambda^{2,1}_{II} \otimes \mathbb R$
— a **rank-3 hyperbolic** lattice, **not** the Mukai lattice. The
simple roots are $\mathcal P_{II, \mathrm{prim}} = \{\delta_1, \delta_2, \delta_3\}$;
the Gram matrix is
$(\delta_i, \delta_j) = \begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix}$
(p. 7). Determinant: $2 \cdot (4 - 4) - (-2)(-4 - 4) + (-2)(4 + 4) = 0 - 16 - 16 = -32$, so
the Gram matrix is **non-degenerate of signature $(1,2)$** (one positive,
two negative eigenvalues; hyperbolic rank 3).

This means: **the only place a non-abelian generator-and-relation
presentation for "the K3 Yangian" currently exists is on this rank-3
hyperbolic lattice**, not on the rank-24 Mukai lattice. The Yangian,
if it exists, has rank 3 — not 24.

### A1, sanity check against literature.

Guay 2007 ("Affine Yangians and deformed double current algebras",
*Adv. Math.* 211, pp. 436–484) constructs $Y(\widehat{\mathfrak{sl}}_n)$
for affine simply-laced types. Nowhere in Guay, Varagnolo–Vasserot,
Feigin–Tsymbaliuk, Bezerra–Mukhin, or Maulik–Okounkov is a **Yangian
of a hyperbolic Kac–Moody** (let alone of a BKM superalgebra) constructed.
The literature gap is real: no rigorous mathematical object called
"$Y(\mathfrak g_{\Delta_5})$" or "$Y(\mathfrak g_{\mathrm{hyp}})$" exists.

**Verdict A1**: the rank of $Y_{\mathrm{BFN}}(K3)$, as written in the
manuscript, is ill-posed. The only well-posed non-abelian candidate
($\mathfrak g_{\Delta_5}$) has **rank 3 on the real part**, plus
infinitely many imaginary-simple-root directions enumerated by
$\{a \in \Lambda^{2,1}_{II} \cap \mathbb R_{\ge 0} \mathcal P_{II} :
(a, a) \le 0\}$ with multiplicity $\mathrm{mult}\alpha = f(4nm - l^2, l)$.
Not 24. Not 22. Not $4 + 20$.

### H1. Heal — rank is 3 in the real-root sector; imaginary directions are infinite-dimensional

**Restatement**: the "non-abelian K3 Yangian", if it exists at all,
should be interpreted as the Yangian deformation of the *envelope* of
$\mathfrak g_{\Delta_5}$, which is a **rank-3 hyperbolic generalised
Kac–Moody superalgebra**. Its real-root lattice is $\Lambda^{2,1}_{II}$
of signature $(2,1)$; its imaginary-root lattice is an infinite union
of hyperbolic lightlike and timelike cones, each with multiplicities
from the K3 elliptic genus.

**Chain-level content** (Pattern 236 ambient qualifier):
- Cartan subalgebra: $\mathfrak h = \Lambda^{2,1}_{II} \otimes \mathbb R$,
  abelian, dimension 3.
- Real simple roots: $\delta_1, \delta_2, \delta_3$ with Gram matrix
  given above (explicit integer entries, off-diagonal $-2$).
- Imaginary simple roots: $\Delta^{\mathrm{im}}_{\overline 0} = \{\tau(a) a : (a,a) = 0, \tau(a) > 0\}$ (even sector)
  and $\Delta^{\mathrm{im}}_{\overline 1} = \{m(a) a : (a,a) < 0, m(a) < 0\}$ (odd sector).
- Generators: $h_\alpha, e_\alpha, f_\alpha$ for $\alpha \in \Delta^{\mathrm{re}} \cup \Delta^{\mathrm{im}}$.
- Serre-type relations as in automorphic-corrections p. 8:
  - $[h_\alpha, e_{\alpha'}] = (\alpha, \alpha') e_{\alpha'}$;
  - $[e_\alpha, f_{\alpha'}] = h_\alpha$ if $\alpha = \alpha'$, else $0$;
  - $(\mathrm{ad}\, e_\alpha)^{1 - 2(\alpha, \alpha')/(\alpha, \alpha)} e_{\alpha'} = 0$ if $\alpha \in \Delta^{\mathrm{re}}$, similarly for $f$;
  - $[e_\alpha, e_{\alpha'}] = 0$ if $(\alpha, \alpha') = 0$.

**$(\infty, 1)$-categorical content**: the module category
$\mathrm{Mod}(\mathfrak g_{\Delta_5})$ is a BKM module category in the
sense of Borcherds 1992; the Koszul-self-dual presentation needed for
the chiral lift is open. Any "chiral Yangian" extending this BKM is a
conjectural deformation, **not** the classical $Y(\mathfrak g)$ of
Drinfeld; no generator–relation presentation for the affine/current
extension exists in the literature.

**Falsifiable prediction (C1.1)**: if $Y_{\mathrm{BFN}}(K3)$ exists
as a Yangian-like object deforming $\mathfrak g_{\Delta_5}$, then its
representation theory should have:
- A **3-dimensional weight lattice** (real part), not 24-dimensional.
- **Imaginary weights** at every lightlike / timelike direction in
  $\Lambda^{2,1}_{II}$, with multiplicities matching K3 elliptic-genus
  Fourier coefficients $f(4nm - l^2, l)$.
- Characters whose denominator function is $\Delta_5(Z)$ evaluated on
  the Type-IV domain $\mathbb H^{\mathrm{IV}}_+ \cong \mathbb H_2$
  (automorphic-corrections Lemma 1, §3).

**Status (H1)**: the rank question has a real answer once we choose
the right lattice. The correct answer is rank 3 (hyperbolic), not 24
(Mukai). The manuscript's "24 Heisenberg generators" phrasing refers
to the abelian $\cH_{\mathrm{Muk}}$ core; the **non-abelian** Yangian
content, if any exists, lives on the rank-3 BKM real part — a
completely different object that is **not** a deformation of rank-24
Mukai data.

---

## CYCLE 2 — ATTACK: "highest weight" and "integrable" are undefined for a hyperbolic Kac–Moody

Having narrowed rank to 3 (in C1), the next question is
representation-theoretic. Classical Yangian integrable-representation
theory (Drinfeld 1988, Chari–Pressley 1994, Molev 2007) requires a
positive root system, a dominant chamber, and a **highest-weight
classification**. Does this exist for $\mathfrak g_{\Delta_5}$?

### A2. Hyperbolic Kac–Moody has no classification of integrable highest-weight reps

**Fact (Kac 1990, *Infinite Dimensional Lie Algebras*, Ch. 10–11)**:
- For *finite* Kac–Moody (ADE, BCFG), integrable highest-weight reps
  are classified by dominant integral weights $\Lambda \in \mathfrak h^*$
  with $\langle \Lambda, \alpha^\vee_i \rangle \in \mathbb Z_{\ge 0}$
  for all simple coroots $\alpha^\vee_i$.
- For *affine* Kac–Moody, same classification + a level condition
  $\langle \Lambda, K \rangle = k$ for a fixed central element $K$.
- For *hyperbolic* Kac–Moody (indefinite Cartan matrix), **no
  classification of integrable highest-weight reps exists**. The
  only known integrable highest-weight rep is the trivial
  one-dimensional representation $\mathbb C_0$ (where "integrable"
  means locally nilpotent action of all root vectors, Kac Theorem
  10.4).

This is a central fact. Feingold–Frenkel 1983 (*Math. Ann.* 263: 87–144)
and Gritsenko–Nikulin 1995/1998 construct specific BKM superalgebras
with lattice Weyl vectors, but their *integrable-rep theory* is
essentially trivial: only the one-dimensional trivial rep is
integrable highest-weight. (Non-integrable highest-weight reps form
an unbounded family, and no finite-dim or even tame integrable ones
exist.)

**Attack**: the programme's informal talk of "modules of
$Y_{\mathrm{BFN}}(K3)$" with a basis is **structurally impossible**
in the hyperbolic Kac–Moody lane. There is no Verma-module / integrable-
quotient construction that produces a non-trivial finite-dimensional
or graded-tame rep of $\mathfrak g_{\Delta_5}$, let alone a Yangian
deformation thereof. The one integrable highest-weight module is
one-dimensional — a scalar, with a trivial GT-type basis (one vector).

### A2, explicit via automorphic-corrections denominator identity

The Weyl–Kac–Borcherds character formula applied to the trivial
1-dim rep gives the denominator identity
$$\frac{1}{64} \Delta_5(2Z) = \Phi(z) = \sum_{w \in W^{(2)}(\Lambda^{2,1}_{II})} \det(w) \bigl[ \exp(-2\pi i(w(\rho), z)) - \sum_{a \in \Lambda^{2,1}_{II} \cap \mathbb R_{>0} \mathcal P_{II}} m(a) \exp(-2\pi i (w(\rho + a), z)) \bigr]$$
(automorphic-corrections §5, p. 9). This is the *unique* non-trivial
character computation in the hyperbolic regime — and it is the
character of the **trivial representation**, dressed by the Weyl
element sum.

Consequence: the only "module with a basis" is the trivial 1-dim
module. There is no GT-pattern combinatorics — because there is no
module of dimension $\ge 2$ to combinatorially index.

### H2. Heal — integrable representation theory IS denominator-identity combinatorics

The attack seems fatal until one notices: the denominator identity is
*itself* a combinatorial object. The Fourier coefficients
$\frac{1}{64} f(n, l, m)$ of $\Delta_5$ and the root multiplicities
$\mathrm{mult}\alpha$ are the combinatorial content that a GT basis
would have indexed.

**Reinterpreted Gelfand-style combinatorics for $\mathfrak g_{\Delta_5}$**:
- The "basis" of the putative Yangian is not indexed by a finite
  nested chain of sub-algebras (as in classical GT). It is indexed by
  **pairs $(w, a)$** with $w \in W^{(2)}(\Lambda^{2,1}_{II})$ (lattice
  Weyl group of $\Lambda^{2,1}$) and $a \in \Lambda^{2,1}_{II} \cap \mathbb R_{>0} \mathcal P_{II}$
  (positive root cone), with multiplicities $\mathrm{mult}\alpha = f(4nm - l^2, l)$.
- Each pair $(w, a)$ contributes a *term* to the character. The
  "pattern" is the root-cone element $a$ plus the Weyl-element label.
- This is **not a finite-dimensional branching pattern**; it is an
  infinite-dimensional lattice-cone combinatorics.

**Chain-level statement**:
$$\dim_{\mathbb C} U(\mathfrak n_+(\mathfrak g_{\Delta_5}))_\alpha = \sum_{\substack{(n_1, \ldots, n_k) \\ \sum n_i \delta_{s_i} = \alpha}} \prod_i \mathrm{mult}(\delta_{s_i})^{n_i} / (\text{Weyl counting})$$
where the sum is over multi-compositions of $\alpha$ as a positive-
cone element. The generating function is $\prod_{\alpha > 0} (1 - z^\alpha)^{-\mathrm{mult}\alpha}$,
which is the BKM denominator function $\Phi^{-1}$ up to the Weyl
factor.

**$(\infty,1)$-categorical statement**: the universal enveloping
algebra $U(\mathfrak g_{\Delta_5})$ is an $\infty$-BKM Hopf algebra in
the sense of Borcherds 1992 + Gritsenko–Nikulin 1995/1998; its
category of integrable highest-weight $\infty$-modules is equivalent
to the category of automorphic forms on $\mathbb H_2$ with multiplier
system $\nu_{\Delta_5}$. The Yangian deformation, if it exists, would
be a compatibility $\mathfrak{Sp}_4(\mathbb Z) \times \mathbb C^\times$
twist — but no construction of this exists in the literature.

**Status (H2)**: integrable representation theory is *replaced* by
denominator-identity combinatorics in the hyperbolic / BKM regime.
This is consistent with Gelfand's programme — combinatorics remains
primary — but the patterns are root-cone lattice points (with
multiplicities), not nested-chain branching patterns.

**Falsifiable prediction (C2.1)**: if the Yangian deformation
$Y(\mathfrak g_{\Delta_5})$ exists, its character on the trivial 1-dim
module should produce the $\hbar$-deformed Weyl–Kac–Borcherds denominator
$$\Delta_5(Z; \hbar) = \hbar^{\mathrm{const}} \cdot (\text{classical } \Delta_5(Z)) \cdot (1 + \hbar \cdot (\text{first quantum correction}) + \cdots),$$
with the first quantum correction encoding the Yangian J-cocycle on
the rank-3 hyperbolic Cartan. **This is open**: no-one has computed
the $\hbar$-deformation of the Igusa cusp form. If such a deformation
does not exist (as a modular form of paramodular level), the Yangian
deformation also does not exist.

---

## CYCLE 3 — ATTACK: no explicit Chevalley / GKLO / RTT presentation exists; "BFN K3 Yangian" is a label, not a construction

### A3. BFN-K3 has three names and zero presentations

The manuscript attributes $Y_{\mathrm{BFN}}(K3)$ to three possible
origins:
1. **Conjecture \ref{conj:bfn-k3-yangian-kummer}** (k3_yangian_chapter.tex:81–89):
   Kummer orbifold $K3 = T^4/\mathbb Z_2$ (resolved), BFN Coulomb branch
   at charge $n$ "equals" $Y(\mathfrak g_{K3})|_{\text{charge } n}$.
   Reduces to the $\mathfrak g = \mathfrak{sl}_2$ / affine-$A_1$ case
   of `thm:bfn-phi-ade-identification` plus blowup deformation-invariance
   of the BFN Coulomb branch — **open**.
2. **Conjecture \ref{conj:bfn-k3-yangian-mukai}** (k3_quantum_toroidal_chapter.tex):
   full Mukai-lattice form. "Requires the non-quiver BFN extension for
   generic K3 moduli" — **open**.
3. **Route A (CY-A)**: $D^b(K3) \xrightarrow{\Phi} A_{K3} \xrightarrow{\text{bar}} B(A_{K3}) \xrightarrow{\text{Koszul}} Y(\mathfrak g_{K3})$.
   "Yangian quantization step" — **open**.

All three conjectural. None writes a single generator-relation
presentation of the purported $Y(\mathfrak g_{K3})$.

By contrast, the ADE sub-theorem `thm:bfn-phi-ade-identification`
(k3_yangian_chapter.tex:108–120, `ClaimStatusProvedElsewhere`)
produces the **shifted affine Yangian** $Y^\mu(\widehat{\mathfrak g})_{k=1}$
with the **Kodera–Nakajima GKLO presentation for type A** (arXiv:1606.02002,
Theorem A). Explicit generators $e_i^{(r)}, f_i^{(r)}, h_i^{(r)}$ for
$i$ a node of the affine Dynkin diagram and $r \ge 0$, with Yangian
Serre relations in the current form.

**Attack**: for the K3 case (not the ADE-Kleinian sub-case),
**no-one has written such a presentation**. Kodera–Nakajima applies
only to ADE simply-laced affine types with quiver variety input;
Webster 2019 extends to non-simply-laced via folding; Finkelberg–
Rybnikov 2014 gives GKLO for affine types A and D. **None of this
literature covers K3 as the geometric input** — because K3 is not a
Nakajima quiver variety (except at orbifold points, where the ADE
sub-case applies).

### A3 reinforced by cross-volume grep

```
grep -r "GKLO" /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_yangian_chapter.tex
```
yields only references to ADE sub-cases via `thm:bfn-phi-ade-identification`.
No GKLO presentation for $Y(\mathfrak g_{K3})$ is written anywhere
in Vol III outside the ADE sub-case.

```
grep -r "RTT" /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_yangian_chapter.tex
```
yields references to the Yang R-matrix check on $\mathbb C^{24}$
(`compute/lib/ade_yangian_level1.py`, per `thm:bfn-phi-ade-identification`
Path V2). But this check is **for $Y_\hbar(\mathfrak{gl}_{24})$**
(Drinfeld W6 voice: $(u + \hbar P)/(u + \hbar)$ on rank 24 is the
Yang R-matrix of $\mathfrak{gl}_{24}$, not an intrinsic Mukai structure).

**Verdict A3**: there is no Chevalley-type, no GKLO-type, no RTT-type
presentation of "$Y_{\mathrm{BFN}}(K3)$" in the manuscript or the
literature. What exists is:
- ADE-Kleinian case: Kodera–Nakajima type A; abstract BFN for D, E.
- Abelian rank-24 Mukai-Heisenberg core: $\mathfrak{gl}_{24}$ Yang
  R-matrix on $\mathbb C^{24}$, satisfies YBE but is **unrelated to
  Mukai** (Drinfeld W6).
- $\mathfrak g_{\Delta_5}$ rank-3 hyperbolic BKM: explicit generators
  and relations (automorphic-corrections §5), but **no Yangian
  deformation** is constructed.

No presentation of "the K3 Yangian" exists; only presentations of
various approximations exist.

### H3. Heal — the correct minimal presentation is the $\mathfrak g_{\Delta_5}$ Chevalley-Serre presentation, interpreted as the $\hbar = 0$ classical limit of an as-yet-unconstructed Yangian

Let me write down what a presentation would look like:

**Classical limit generators** (automorphic-corrections §5):
- $h_i$ for $i \in \{1, 2, 3\}$ (rank-3 Cartan);
- $e_\delta, f_\delta$ for $\delta \in \{\delta_1, \delta_2, \delta_3\}$ (real simple roots);
- $e_\alpha^{(\mu)}, f_\alpha^{(\mu)}$ for $\alpha \in \Delta^{\mathrm{im}}$ and $\mu = 1, \ldots, \mathrm{mult}\alpha$ (imaginary simple roots with multiplicity).

**Classical limit relations**:
- $[h_i, h_j] = 0$;
- $[h_i, e_{\alpha}] = \alpha_i \cdot e_\alpha$, $[h_i, f_{\alpha}] = -\alpha_i \cdot f_\alpha$;
- $[e_\alpha, f_{\alpha'}] = \delta_{\alpha, \alpha'} \cdot h_\alpha$;
- Serre-type: $(\mathrm{ad}\, e_{\delta_i})^{1 - 2(\delta_i, \delta_j)/(\delta_i, \delta_i)} e_{\delta_j} = 0$ for real simple $\delta_i \ne \delta_j$ (here the exponent $1 + 2 = 3$ by the Gram matrix);
- $[e_\alpha, e_{\alpha'}] = 0$ if $(\alpha, \alpha') = 0$ (orthogonal imaginary generators commute).

**Yangian deformation (conjectural, rank-3 version)**:
- Add Drinfeld-$J$ generators $J(h_i)$ in current form
  $J(h_i)_\lambda$ for spectral parameter $\lambda$;
- Serre relations deformed by $\hbar$-corrections of the form
  $[J(h_i), J(e_\alpha)] = \alpha_i \cdot J(e_\alpha) + \hbar \cdot (\text{cubic correction})$;
- Classical $r$-matrix: $r(z) = \sum_{i,j} (G^{-1})_{ij} \cdot h_i \otimes h_j / z + \sum_{\alpha \in \Delta^{\mathrm{re}}} e_\alpha \otimes f_\alpha / z$ where $G = (\delta_i, \delta_j)$ is the Gram matrix.

(Cross-reference to Vol I `landscape_census.tex`: the **$r$-matrix trace
form** I write here uses the *inverse* of the rank-3 Gram matrix $G$ as
the bilinear form on the Cartan. $G$ has determinant $-32 \ne 0$, so
$G^{-1}$ is well-defined and has signature $(1, 2)$.)

**Scope (Pattern 236)**:
- **Chain-level**: the classical presentation is inscribed in the
  automorphic-corrections paper; it is rigorous.
- **$(\infty, 1)$-categorical**: the Yangian extension, if it exists,
  lives in the $\infty$-category of affine quantum groups over
  hyperbolic Kac–Moody BKM superalgebras — a category that *is
  not yet constructed* in the literature.

**Status (H3)**: the non-abelian K3 Yangian, on its correct rank-3
BKM interpretation, has a **classical-limit presentation** (the
$\mathfrak g_{\Delta_5}$ Chevalley-Serre presentation) but **no
Yangian-level presentation**. This is more precise than Wave 6's
"stratified landscape": the reason Wave 6 could not find a unified
R-matrix is that **the deformation theory of hyperbolic BKM
superalgebras is not available in the literature**, not because the
object is structurally impossible.

**Falsifiable prediction (C3.1)**: if one can construct a central
extension of $U_\hbar(\mathfrak g_{\Delta_5})$ satisfying associativity,
co-associativity, and an $\hbar$-deformed Weyl–Kac–Borcherds formula,
then this IS the K3 Yangian in the sense of the programme. The
conjecture would be: $\Phi_3$ on $D^b(\mathrm{Coh}(K3 \times E))$
outputs $Y_\hbar(\mathfrak g_{\Delta_5})$, not a rank-24 or stratified
object. (This is a **specific strengthening** of
`conj:bfn-k3-yangian-mukai` that makes it falsifiable.)

---

## CYCLE 4 — ATTACK: the chiral algebra of K3 is NOT finitely generated

### A4. The K3 chiral algebra has infinitely many generating fields

The manuscript `cy_to_chiral.tex:1282–1305` states
$\Phi(D^b(\mathrm{Coh}(K3))) = \cH_{\mathrm{Muk}}$, a rank-24 Heisenberg
VOA. As a **Heisenberg VOA**, this is finitely generated by 24 Heisenberg
currents $J^a(z)$, $a = 1, \ldots, 24$, with OPE
$J^a(z) J^b(w) \sim \omega^{ab}_{\mathrm{Muk}}/(z-w)^2$.

But this is only the **abelian** output. The actual chiral algebra of
K3, whatever it is, should include:
- The 24 abelian Heisenberg currents (from $H^*(K3, \mathbb C)$ abelian
  classes under HKR);
- **Vertex operators for lattice elements** $v \in \Lambda_{\mathrm{Muk}}$
  of norm $(v, v)_{\mathrm{Muk}} = -2$ (real roots) — these are not
  finitely many.
- **Twisted sectors** from Enriques / Nikulin / Kummer involutions.
- **Discriminant-form modules** of the lattice VOA
  $V_{\Lambda_{\mathrm{Muk}}}$ (trivial at rank 24 because
  $\Lambda_{\mathrm{Muk}}$ is unimodular, but non-trivial for K3
  transcendental lattices after Nikulin branching).

The full $V_{\Lambda_{\mathrm{Muk}}}$ lattice VOA (Frenkel–Lepowsky–Meurman
1988, Borcherds 1986) is **not finitely generated as a vertex algebra**:
it has infinitely many primary fields, one per vector in
$\Lambda_{\mathrm{Muk}}$, organised by conformal weight.

**Attack**: the Wave-6 statement "$\mathcal Y_{K3}$ is piecewise-
canonical on ADE strata" suggests per-stratum finite generation. But
the **total** chiral algebra on $K3$ is the lattice VOA
$V_{\Lambda_{\mathrm{Muk}}}$, which is infinitely generated. The chiral
Yangian, if it extends this, must also be infinitely generated (at
least in the real-root direction).

Moreover — and this is sharper — the **genus-0 K3 operad** (the operad
of points moving on $K3$ as a two-fold) has infinitely many generators
per arity. `cy_to_chiral.tex:1282` constructs $\Phi_2(D^b(K3))$ but
does not claim finite generation: "The generating fields $J^a(z)$,
$a = 1, \ldots, 24$" refers to the **Heisenberg part only**, not the
full chiral algebra of factorisation $D$-modules over $\mathrm{Ran}(K3)$.

### A4 reinforced via elliptic-cohomology / topological modular forms

$H^*(K3, \mathbb C) = 24$-dimensional, but $H^*(K3 \times E, \mathbb C) = 24 \cdot 2 = 48$-dimensional for an elliptic curve $E$. The chiral algebra of $K3 \times E$ should
have infinitely many generators from the elliptic tower of $E$ alone.
The $K3 \times E$ BKM object $\mathfrak g_{\Delta_5}$ (k3e_bkm_chapter.tex)
precisely inscribes this: it has $3$ real simple roots + infinitely
many imaginary roots from the K3 elliptic-genus Fourier coefficients.

### H4. Heal — the non-abelian K3 Yangian is a finitely generated extension of $\mathfrak g_{\Delta_5}$ on a rank-3 hyperbolic cone, with infinitely many generators via lattice vertex operators indexed by $\Lambda^{2,1}_{II} \cap \mathbb R_{\ge 0} \mathcal P_{II}$

The heal collapses the rank-24 / rank-3 dichotomy. The **correct
picture** is:

1. **Finite generation in the real sector**: 3 Heisenberg generators
   on $\Lambda^{2,1}_{II} \otimes \mathbb R \cong \mathbb R^3$ (the
   real Cartan of $\mathfrak g_{\Delta_5}$).
2. **Infinite generation in the imaginary sector**: lattice vertex
   operators $V_\alpha(z)$ for $\alpha$ in the positive hyperbolic
   cone $\mathbb R_{\ge 0} \mathcal P_{II}$, with multiplicities
   $\mathrm{mult}\alpha$ from the K3 elliptic genus.
3. **Character**: $\chi(V_{\Lambda^{2,1}_{II}}; q, y, p) = \Delta_5(Z)^{-1} \cdot (\text{Heisenberg Fock factor})$, matching the denominator formula.

**Scope**: this replaces the Mukai-24 picture entirely. The 24
Heisenberg currents of `thm:phi-k3-explicit` are part of the
**$\Phi_2$ output on the abelian K3 only**; the **non-abelian lift**
to $\mathfrak g_{\Delta_5}$ lives naturally on **$K3 \times E$**
(automorphic lift), and its rank-3 structure is hyperbolic, not
positive-definite of rank 24.

**Falsifiable prediction (C4.1)**: if $Y(\mathfrak g_{\Delta_5})$
exists with the chiral structure above, then:
- The OPE of two lattice vertex operators
  $V_\alpha(z) \cdot V_\beta(w) \sim (z - w)^{(\alpha, \beta)_{\mathrm{hyp}}} \cdot V_{\alpha + \beta}(w) + \ldots$
  should match the Gritsenko–Nikulin automorphic product expansion
  of $\Delta_5$ (automorphic-corrections §4, §6).
- The corresponding **OPE pole order** is $(\alpha, \beta)_{\mathrm{hyp}}$,
  where $(\cdot, \cdot)_{\mathrm{hyp}}$ is the Gram matrix of
  $\Lambda^{2,1}_{II}$ evaluated on the pair.

**Verification paths** (Beilinson 3+ paths discipline):
- Path 1: direct OPE computation of $V_\alpha(z) V_\beta(w)$ in the
  lattice VOA $V_{\Lambda^{2,1}_{II}}$ (FLM 1988 + Kac 1998).
- Path 2: Fourier-coefficient extraction from the Borcherds product
  for $\Delta_5$ (automorphic-corrections §6, with
  $f(n, l)$ = K3 elliptic genus coefficients $\phi_{0,1}(\tau, z)$,
  verified equations 1, 10 + r, 10r^{-2} - 64 r^{-1} + 108 - 64 r + 10 r^2$
  matching the BKM root multiplicities).
- Path 3: cross-check against the Gritsenko–Nikulin 1995/1998
  primary-source product formula for $\Delta_5$.

**Status (H4)**: the "non-abelian K3 Yangian" is a finitely-generated
extension of $\mathfrak g_{\Delta_5}$ in the real sector, infinitely-
generated in the imaginary sector. The rank-24 Mukai framing is a
**$K3$-alone shadow**; the true non-abelian BKM object needs
**$K3 \times E$** (one more dimension) for the elliptic-genus
multiplicity data.

---

## CYCLE 5 — ATTACK: the connection to the Wave 5–6 "stratified landscape" is incoherent

### A5. The rank-3 BKM picture (Cycles 1–4) and the stratified-21-ADE picture (Waves 4–5) are two different objects claimed to be the same

Wave 5 inscribed:
- 21 ADE sub-Yangians at single-copy + diagonal-pair enhancements
  (Polyakov W4 / Wave 6 rescoped);
- Pentagon coherence $\{\beta_{\Lambda_1, \Lambda_2}\}$ as cross-stratum
  glue (Drinfeld W2);
- $L_\infty$-coupling via Hodge signature at $\hbar^2$ (Kazhdan W5 /
  Wave 6 retracted as "language without object").

Cycles 1–4 above construct a **single rank-3 BKM object**
$\mathfrak g_{\Delta_5}$ with explicit presentation and explicit
imaginary-simple-root combinatorics. This is **not** a stratified
family; it is a single object.

**These are two different mathematical objects.** Waves 4–5 wrote
"$Y_{\mathrm{BFN}}(K3)$" to denote a stratified family of ADE-Kleinian
Yangians. Cycles 1–4 use "$Y(\mathfrak g_{\Delta_5})$" to denote the
Yangian of a BKM superalgebra on a hyperbolic lattice. Neither the
manuscript nor any Wave 1–6 output provides a map between them.

**Attack**: is there any relation? Or are we just using the same
symbol for different objects?

### A5 resolved via the denominator-identity bridge

There is a relation, and it is subtle. The key observation:

1. The 21 ADE sub-Yangians of Polyakov W4 correspond to **primitive
   ADE embeddings $\Lambda_{\mathfrak g} \subset \Lambda_{\mathrm{Muk}}$**
   of positive-definite root lattices into the Mukai lattice
   $II_{4,20}$ of signature $(4, 20)$.
2. The BKM superalgebra $\mathfrak g_{\Delta_5}$ lives on the
   **rank-3 hyperbolic $\Lambda^{2,1}_{II} \subset \Lambda^{3,2}$**
   (the *paramodular* lattice of signature $(3, 2)$, automorphic-
   corrections §3). This $\Lambda^{3,2}$ is **NOT** a primitive
   sublattice of $\Lambda_{\mathrm{Muk}} = II_{4,20}$; it is a
   **different** rank / signature.
3. The Mukai lattice $II_{4,20}$ has signature $(4, 20)$; the
   paramodular lattice $\Lambda^{3,2}$ has signature $(3, 2)$; the
   K3 transcendental lattice $T(K3)$ has signature $(2, \rho)$ with
   $\rho = 20 - $ Picard rank.
4. The relevant inclusion is NOT $\Lambda^{3,2} \subset \Lambda_{\mathrm{Muk}}$
   (rank mismatch, $3 + 2 = 5 < 24$, so as pure $\mathbb Z$-ranks it
   fits; but the *signature* $(3,2)$ cannot embed into $(4, 20)$
   while preserving both positive and negative parts — Etingof O1).
5. Instead, $\Lambda^{3,2}$ lives **outside** the Mukai lattice as
   an independent Siegel / paramodular structure governing
   $K3 \times E$ modular forms (Gritsenko–Nikulin). The BKM
   $\mathfrak g_{\Delta_5}$ is a **$K3 \times E$ object**, not a
   **$K3$-alone object**.

**Verdict A5**: the Wave 5 stratified-ADE picture on $\Lambda_{\mathrm{Muk}}$
and the Wave 7 BKM picture on $\Lambda^{3,2}$ are **two different
mathematical objects on two different lattices**. The identification
"both are $Y_{\mathrm{BFN}}(K3)$" is a **type error**. One is about
$K3$, the other is about $K3 \times E$.

### H5. Heal — "the non-abelian K3 Yangian" should be split into two objects with different lattice structures

**Renaming proposal** (for manuscript inscription):

1. **$Y_{\mathrm{stratified}}(K3)$** := the stratified family of
   ADE-shifted Yangians indexed by primitive ADE embeddings into
   $\Lambda_{\mathrm{Muk}} = II_{4,20}$, with pentagon coherence.
   Rank per stratum: $\mathrm{rank}(\mathfrak g_\Lambda)$, typically
   $\le 8$. No single-object structure beyond pentagon category.
   Wave 6 convergent position.
   **Lives on $K3$**.
2. **$Y_{\Delta_5}(K3 \times E)$** := the hypothetical Yangian
   deformation of $\mathfrak g_{\Delta_5}$, a single rank-3 hyperbolic
   BKM superalgebra. Rank 3 in real sector, infinite-rank in
   imaginary sector. Has explicit classical-limit presentation
   (automorphic-corrections §5).
   **Lives on $K3 \times E$**.

These are distinct objects. The manuscript (Vol III) should inscribe
**both** with their respective scopes, and **never identify them**.
The Wave 1–6 confusion arose because both carry the decoration "K3",
and both invoke the Mukai lattice at various points, but they are
structurally distinct (different lattices, different ranks, different
types).

**Chain-level cross-check**: Gelfand's combinatorial programme
applied to each:
- For $Y_{\mathrm{stratified}}(K3)$: per-stratum Molev GT basis for
  A / D types; Drinfeld-$J$ presentation for E types; no global GT
  basis. Wave 6 converged here.
- For $Y_{\Delta_5}(K3 \times E)$: no GT basis in the classical sense
  (rank-3 hyperbolic is not a branching tower); combinatorics is
  automorphic (denominator function $\Delta_5$, root multiplicities
  from K3 elliptic genus). This is Wave 7's content.

**$(\infty, 1)$-categorical cross-check**:
- $Y_{\mathrm{stratified}}(K3)$: sheaf of presentable $\infty$-categories
  over primitive-sublattice moduli, pentagon-cohered.
- $Y_{\Delta_5}(K3 \times E)$: hypothetical presentable $\infty$-category
  living over $\mathrm{Sp}_4(\mathbb Z) \backslash \mathbb H_2$, the
  Siegel moduli space of $(1,1)$-polarised abelian surfaces.

**Status (H5)**: the non-abelian K3 Yangian is **two objects**, not
one. Both are real mathematical objects with real definitional content.
Their conflation in Waves 1–6 was the root error.

---

## CONVERGED STATEMENT — Wave 7 Gelfand final position

Let me state what I now believe, combinatorially and rigorously:

**The "non-abelian K3 Yangian" is two distinct objects**:

### Object 1: $Y_{\mathrm{stratified}}(K3)$

- **Definition**: a presheaf of Yangian-like objects over the moduli
  $\mathcal M_{\mathrm{ADE}} \subset \mathrm{Stab}^\dagger(K3)$ of
  primitive ADE sub-lattice embeddings $\Lambda_{\mathfrak g} \hookrightarrow \Lambda_{\mathrm{Muk}}$
  with pentagon 2-cell coherence.
- **Combinatorics per stratum**: Molev GT basis for A, D types; Drinfeld-$J$
  for E types. No unified basis.
- **Reality**: 21 strata (single + diagonal-pair); $\sim 200$ strata under
  full Nikulin primitive-embedding census (Wave 6 correction).
- **Proved content**: ADE-Kleinian case (single stratum, $K3 \to \mathbb C^2/\Gamma$
  locally), `thm:bfn-phi-ade-identification`. Full K3 case: open
  (Conjecture \ref{conj:bfn-k3-yangian-kummer} / \ref{conj:bfn-k3-yangian-mukai}).

### Object 2: $Y_{\Delta_5}(K3 \times E)$

- **Definition** (conjectural): the Yangian deformation
  $U_\hbar(\mathfrak g_{\Delta_5})$ of the generalised Kac–Moody superalgebra
  $\mathfrak g_{\Delta_5}$ of Borcherds / Gritsenko–Nikulin / Lorgat
  (automorphic-corrections §5).
- **Classical limit**: $\mathfrak g_{\Delta_5}$ on $\Lambda^{2,1}_{II}$
  with Gram matrix $\begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix}$.
- **Combinatorics**: real simple roots $\{\delta_1, \delta_2, \delta_3\}$
  (rank 3); imaginary simple roots in the positive hyperbolic cone with
  multiplicities $\mathrm{mult}\alpha = f(4nm - l^2, l)$ from the K3
  elliptic genus $\phi_{0,1}$.
- **Character**: $\chi_{\text{triv}} = \Delta_5(Z)$ (Weyl–Kac–Borcherds
  denominator identity, automorphic-corrections Theorem 3 / Theorem 4).
- **Proved content**: the **classical** BKM superalgebra is constructed
  (automorphic-corrections); the **Yangian deformation** is **not** constructed.
- **Lives on**: $K3 \times E$, Siegel moduli $\mathrm{Sp}_4(\mathbb Z) \backslash \mathbb H_2$.

These two objects are **NOT** identified. The manuscript Vol III currently
conflates them under the single symbol $Y(\mathfrak g_{K3})$ — this is
the error Wave 7 identifies and the manuscript should correct.

---

## NEW CONJECTURES

### Conjecture W7-G1 (rank-3 BKM hypothesis)

The symbol "$Y_{\mathrm{BFN}}(K3 \times E)$" should be rigorously
interpreted as the Yangian deformation
$Y_\hbar(\mathfrak g_{\Delta_5})$ of the generalised BKM superalgebra
$\mathfrak g_{\Delta_5}$, a rank-3 hyperbolic Kac–Moody object on
$\Lambda^{2,1}_{II}$ with Gram matrix
$\begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix}$.

**Falsifiability**: (a) if a non-trivial deformation of the
universal enveloping $U(\mathfrak g_{\Delta_5})$ satisfying a
deformed Weyl–Kac–Borcherds denominator identity cannot be constructed,
this conjecture is falsified. (b) if the deformation exists but
does not agree with the $\hbar = 0$ classical limit equal to
$\mathfrak g_{\Delta_5}$, this conjecture is falsified. (c) if
$\Phi_3(D^b(\mathrm{Coh}(K3 \times E)))$ turns out to be explicitly
different from $Y_\hbar(\mathfrak g_{\Delta_5})$, this conjecture is
falsified.

**Status**: [C] conjectural.

### Conjecture W7-G2 (two-object decomposition)

The "non-abelian K3 Yangian programme" should be split into two
programmes with distinct scopes:
1. $Y_{\mathrm{stratified}}(K3)$ on $\Lambda_{\mathrm{Muk}}$, stratified family.
2. $Y_{\Delta_5}(K3 \times E)$ on $\Lambda^{3,2}$, single rank-3 BKM-superalgebra Yangian (conjectural deformation).

These are genuinely different objects; no canonical identification
between them exists.

**Falsifiability**: if a canonical equivalence
$Y_{\mathrm{stratified}}(K3) \xrightarrow{\sim} Y_{\Delta_5}(K3 \times E)$
is constructed as $\infty$-categorical quasi-isomorphism (or as
Hopf-algebra isomorphism at each stratum), the conjecture is falsified.

**Status**: [C] conjectural.

### Conjecture W7-G3 (combinatorial-basis replacement)

The correct Gelfand-style combinatorial basis of
$Y_\hbar(\mathfrak g_{\Delta_5})$, if the Yangian exists, is **not a
GT pattern** but a pair $(w, a)$ with:
- $w \in W^{(2)}(\Lambda^{2,1}_{II})$ (even Weyl group of $\Lambda^{2,1}_{II}$, generated by reflections in vectors of square 2 — automorphic-corrections p. 6);
- $a \in \Lambda^{2,1}_{II} \cap \mathbb R_{\ge 0} \mathcal P_{II}$ (positive root cone);

with multiplicity $\mathrm{mult}(w, a) = \det(w) \cdot m(a)$. The
Plancherel formula gives characters on the positive cone via the
$\Delta_5$ denominator.

**Falsifiability**: direct construction of a putative Yangian module
with a different basis (e.g., a quiver-variety stable basis that is
combinatorially different from $(w, a)$) would refute this.

**Status**: [C] conjectural.

---

## REQUIRED MANUSCRIPT AMENDMENTS

### Vol III `k3_yangian_chapter.tex`

1. **Line 1**: opening says "The K3 double current algebra
   $\mathfrak g_{K3}$ is the classical limit of the K3 Yangian
   $Y(\mathfrak g_{K3})$, whose 24 Heisenberg generators..."
   — **Amendment**: split the claim. 24 Heisenberg generators refers
   to the abelian Mukai-Heisenberg core $\cH_{\mathrm{Muk}}$ (a
   separate, proved object, `thm:phi-k3-explicit`). The non-abelian
   K3 Yangian, if it exists, is a rank-3 hyperbolic BKM-based object
   (Conjecture W7-G1), not a "rank-24 quantization of the Mukai
   lattice".
2. **Lines 81–97, Conjectures `bfn-k3-yangian-kummer` and
   `bfn-k3-yangian-mukai`**: add a scope note that these conjectures
   live on the **stratified landscape** (Object 1), not on the BKM
   object (Object 2). Conflating the two is the Wave-7 identified
   error.
3. **Line 108, Theorem `thm:bfn-phi-ade-identification`**: the $\le 5$
   primary-source dependency audit (Wave 6 SYNTHESIS §0.3) should be
   honestly inscribed. In particular, the CY-dimension (2 vs 3) of
   $T^*\widetilde S_{\mathfrak g}$ as a CY-object: since
   $T^*\widetilde S_{\mathfrak g}$ is a CY-3 (complex dimension 4,
   cotangent bundle of a complex surface), this is a $\Phi_3$-output,
   not $\Phi_2$. The chapter should clarify whether the theorem
   targets $\Phi_2(\widetilde S_{\mathfrak g})$ or
   $\Phi_3(T^*\widetilde S_{\mathfrak g})$; the current prose is
   ambiguous between these.

### Vol III `cy_to_chiral.tex`

4. **Line 71, property (U4) bullet for K3**: the identification
   $\Phi(D^b(\mathrm{Coh}(K3))) = \cH_{\mathrm{Muk}}$ is proved with
   $\kappa_{\mathrm{ch}} = 2 = \chi(\mathcal O_{K3})$, bar Euler
   $\eta^{24}$ — this is the **abelian** output (Object 0). The
   **non-abelian** lift to $\mathfrak g_{\Delta_5}$ needs
   **$K3 \times E$** (add to the list of standard inputs: see (U4)
   extension for $d = 3$ on $K3 \times E$).
5. **Line 1287, Theorem `thm:phi-k3-explicit`**: the proof body
   (1307–1423) is correct for the abelian case. Amend the statement
   to clarify that this is the **abelian** $\Phi_2$-output, and that
   the non-abelian $\Phi_3$-output on $K3 \times E$ is a separate
   (conjectural) Yangian-like object on $\mathfrak g_{\Delta_5}$
   (Conjecture W7-G1).

### Vol III `k3e_bkm_chapter.tex`

6. **Line 122, Section "The denominator identity: $\Delta_5 = \Phi$"**:
   this chapter correctly treats $\mathfrak g_{\Delta_5}$ as the BKM
   superalgebra of $K3 \times E$. Amend to add **scope note**: this
   IS the correct home of the "non-abelian K3 Yangian" programme
   (Object 2 of Wave 7). The rank-3 hyperbolic presentation from
   automorphic-corrections §5 is the minimal explicit content.
7. **Line 190 / 197, Proposition relating $\mathrm{CoHA}(K3 \times E)$
   to $U(\mathfrak n_+(\mathfrak g_{\Delta_5}))$**: this is an
   explicit bridge from the $\Phi_3$ / CoHA side to the BKM / Siegel
   side. Amend the chapter to cross-reference Conjecture W7-G1 and
   state that the full Yangian $Y(\mathfrak g_{\Delta_5})$ is the
   conjectural double of this.

### New AP-CY patterns to register

**AP-CY-W7-1** (new): *"The K3 Yangian" is a collision of two
structurally distinct objects: (i) the stratified family
$Y_{\mathrm{stratified}}(K3)$ on $\Lambda_{\mathrm{Muk}}$, and (ii)
the BKM Yangian $Y(\mathfrak g_{\Delta_5})$ on $\Lambda^{3,2}$ /
$K3 \times E$. These live on different lattices of different ranks
and different signatures; they are not equivalent and should not be
conflated. Use the object-1 / object-2 notation or restate with
explicit lattice.*

**AP-CY-W7-2** (new): *The rank of a purported "K3 Yangian" is not
24 (Mukai), not 22 (transcendental), not $4+20$ (Hodge). In the
BKM interpretation (Object 2), the rank is 3 in the real-root
sector; in the stratified interpretation (Object 1), the rank is
per-stratum $\le 8$. There is no single rank for "the K3 Yangian".*

**AP-CY-W7-3** (new): *Hyperbolic Kac–Moody algebras have no classical
integrable-highest-weight representation theory beyond the trivial
1-dim module. Representation-theoretic talk about
"$\mathfrak g_{\Delta_5}$-modules" must be replaced by automorphic /
denominator-identity combinatorics. GT basis is not applicable.*

---

## BKM / SIEGEL BRIDGE STATUS

This is the central Wave-7 question. My answer:

### The Siegel modular form $\Delta_5$ is the denominator function of a **concrete**, **explicitly-presented** generalised BKM Lie superalgebra $\mathfrak g_{\Delta_5}$.

The automorphic-corrections paper (Lorgat 2020, attached) constructs
$\mathfrak g_{\Delta_5}$ by:

1. Starting from the Kac–Moody algebra $\mathfrak g$ of the rank-3
   hyperbolic Gram matrix $\begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix}$.
2. Adding **imaginary simple roots** indexed by lattice points
   $a \in \Lambda^{2,1}_{II} \cap \mathbb R_{>0} \mathcal P_{II}$ with
   $\tau(a) > 0$ (even imaginary roots) or $m(a) < 0$ (odd imaginary
   roots), with multiplicities $f(4nm - l^2, l)$ for the K3 elliptic
   genus Fourier coefficients.
3. Verifying that the Weyl–Kac–Borcherds denominator identity recovers
   $\Delta_5(2Z)/64 = \Phi(z)$ on the complexified positive cone
   $\Omega(\mathcal C(\Lambda^{2,1})_+)$.

**This is an explicit construction. It is not open. It is the
automorphic-corrections paper's main theorem.**

### The Yangian / chiral quantum group lifting

The question "what chiral quantum group undergirds $\Delta_5$?" has
the answer: **a conjectural Yangian deformation
$Y_\hbar(\mathfrak g_{\Delta_5})$, which has not yet been constructed**.
The classical limit is $\mathfrak g_{\Delta_5}$ (rigorous, above).
The deformation theory is a literature gap (no-one constructs
Yangians of generalised Kac–Moody or BKM superalgebras).

**Required for the bridge**:
1. Construction of a central extension of $U(\mathfrak g_{\Delta_5})$
   with a deformation parameter $\hbar$;
2. An $\hbar$-deformed denominator identity
   $\Delta_5(Z; \hbar) = \Delta_5(Z) \cdot (1 + O(\hbar))$ with
   explicit first correction;
3. A coproduct $\Delta: Y_\hbar(\mathfrak g_{\Delta_5}) \to
   Y_\hbar(\mathfrak g_{\Delta_5}) \otimes Y_\hbar(\mathfrak g_{\Delta_5})$
   respecting the BKM grading.

### A sub-question from the probing prompt

The prompt asks specifically about $\Phi_{12}$ (Borcherds). The
automorphic-corrections paper does not treat $\Phi_{12}$ directly; it
focuses on $\Delta_5$. But the Gritsenko–Nikulin programme produces
many such BKM denominators from weak Jacobi form input, and $\Phi_{12}$
is the Borcherds lift from $J(\tau) - 744$ (j-function). The analogous
BKM is $\mathfrak g_{\Phi_{12}}$, the **Fake Monster Lie algebra** of
Borcherds 1992 (*Invent. Math.* 109: 405–444). Its chiral quantum
group, by the same two-object logic, is conjecturally
$Y_\hbar(\mathfrak g_{\Phi_{12}})$ — also unconstructed. The Fake
Monster is a **rank-26 hyperbolic Kac–Moody** (on $II_{25,1}$), with
real simple roots the $24$-dim Leech lattice roots + one time direction,
so rank-25 real simple root system + infinitely many imaginary roots.

### Gelfand-style verdict

There **is** an explicit generator–relation presentation for a specific
BKM superalgebra associated to $\Delta_5$ (Lorgat 2020, following
Borcherds / Gritsenko–Nikulin methodology): rank-3 real Cartan + rank-3
real simple roots + infinitely many imaginary simple roots with
elliptic-genus multiplicities. The Gram matrix is explicitly
$\begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix}$.

**There is no explicit generator–relation presentation for its
Yangian deformation.** This is a real literature gap; the chiral
quantum group "undergirding" $\Delta_5$ is open.

---

## CONCLUDING NOTE — Wave 7 Gelfand voice

The compound noun "stratified-coupled-$L_\infty$-quasi-Hopf object"
of Waves 4–5 was, as I said in Wave 6, reluctant to say what it meant.
Wave 6 said: it is a stratified family, not one object. Wave 7
sharpens this further: the stratified family on $\Lambda_{\mathrm{Muk}}$
is a **different mathematical object** from the BKM Yangian on
$\Lambda^{3,2}$. Both exist (the first as a pentagon-cohered sheaf of
shifted affine Yangians, the second conjecturally as a Yangian of
$\mathfrak g_{\Delta_5}$). Neither is a rank-24 Mukai object. The
rank-24 framing is a red herring from the abelian $\Phi_2$-output,
not the non-abelian BKM lift.

In the programme I co-founded: combinatorics is primary. The
combinatorics of $\mathfrak g_{\Delta_5}$ is the triangle Gram matrix
$\begin{pmatrix} 2 & -2 & -2 \\ -2 & 2 & -2 \\ -2 & -2 & 2 \end{pmatrix}$
plus the K3 elliptic-genus coefficients $f(n, l)$ controlling
imaginary multiplicities. That is the explicit content. Any Yangian
lifting must carry this combinatorics as its classical limit. The
Mukai-lattice rank-24 is a separate, abelian, finite-dim combinatorial
object — do not conflate.

Wave 7 closes with two conjectures, one literature gap, and the
obligation on the manuscript to split "the K3 Yangian" symbol into
its two distinct objects.

— end agent 01 Wave 7 report
