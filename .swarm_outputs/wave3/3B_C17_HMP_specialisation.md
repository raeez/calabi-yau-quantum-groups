# Closure 3B-C17 (Opus 4.7 relaunch): HMP 2020 specialisation verdict

## Terminal verdict

**C (genuine extension needed).** State A (HMP 2020 as-written suffices)
is **falsified by three independent failure modes**: a signature-scope
mismatch on two of the three named witnesses, an Arakelov-Chern
torsion-order statement absent from HMP 2020 Thm 1.1, and a
$c_+$-subcone uniformity that HMP explicitly does not claim.

The numerical identities on the three witnesses ($K = 2,\,8,\,50$) hold
by three **separate primary-source routes**, but their unification
across the $\mathcal B$-family as a single HMP-specialisation is **not**
an as-stated HMP theorem; a named, narrow, publishable extension is
required. The hypothesis as posed — "HMP 2020 Thm 1.1 specialises to
the principal Heegner divisor in the $c_+$-subcone uniformly across the
$\mathcal B$-family" — is **not true** without three substantive
extensions to HMP's machinery (signature-scope widening,
Arakelov-torsion-order extraction, positive-subcone uniformity); each
extension is individually within reach of the HMP framework, but none
is on the page of HMP 2020 \emph{Invent. Math.} 220.

This verdict matches and sharpens C17 closure-state B in
`C17_Bruinier_Muk_Br_reciprocity.md` (the reciprocity as a whole is
conjectural). The refinement here: the specific **HMP-as-sufficient**
half of the conditional closure is C (extension needed), not A;
HMP 2020 as a primary source is a *platform* for the reciprocity, not
its statement.

## Primary-source anchor (decisive)

The hypothesis misquotes the HMP volume number. The canonical citation
across all Vol III notes is

> Howard–Madapusi Pera, "Arithmetic of Borcherds products,"
> *Inventiones Mathematicae* **220** (2020), not 219.

Cross-checked: `notes/wave8_j5_kudla_millson_level_N.tex` line 220,
`notes/wave13_a9_sheaves_BKM_bezrukavnikov.tex` line 178 and 423. The
hypothesis statement says "Invent. Math. 219"; the correct reference
is volume 220. This is a citation typo in the hypothesis, not a
substantive error, but it is recorded here for the file.

## Point-by-point verification

### (1) Does HMP 2020 Thm 1.1 cover signatures $(4, 2)$ and $(25, 2)$?

**Answer: not as posed.** The hypothesis asserts $\mathrm{HMP}$ applies
at signatures "$(4, 2)$" and "$(25, 2)$" as specialisations for K3 and
Fake Monster. Both of these signature readings are **wrong against the
actual lattice inputs**:

| Witness | Input lattice | Actual signature | Hypothesis claim |
|---------|---------------|------------------|-------------------|
| Monster | $\mathrm{II}_{1,1}$ | $(1,1)$ | [not specified] |
| K3 Mukai | $\mathrm{II}_{4,20} = \widetilde\Lambda(K3)$ | $(4, 20)$ | "$(4, 2)$" |
| Fake Monster | $\mathrm{II}_{25,1}$ | $(25, 1)$ | "$(25, 2)$" |

Documented references: `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:98`
(K3 Mukai lattice $\mathrm{II}_{4,20}$ signature $(4,20)$);
`notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:151`
(K3-BKM input $\Lambda^{2,1}_{\mathrm{II}}$);
`notes/platonic_synthesis_waves_11_through_16_healed.tex:87`
(Fake Monster on $\mathrm{II}_{25,1}$ Leech-plus-hyperbolic);
`notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:99`
(c_+ convention lock: the Fake-Monster Bruinier reading does NOT apply
uniformly to signature-$(25,1)$; doubled-Leech-rank $c_+=25$ is
structurally distinct from the $(2,n)$ reciprocity).

HMP's native scope is lattices $L$ of **signature $(n, 2)$** (or
equivalently $(2, n)$; the orthogonal group $\mathrm{GSpin}(L)$ is
isomorphic) — these are the lattices that carry a Shimura variety of
orthogonal type with the required **weight-2 polarised Hodge structure**
(two negative directions giving the Hermitian-symmetric Type-IV domain
$\mathrm{SO}(2,n)/(\mathrm{SO}(2)\times\mathrm{SO}(n))$). See
`notes/wave8_j5_kudla_millson_level_N.tex:104-108`:
> "HMP 2020 \emph{Invent. Math.} 220, §7 constructs the derived
> Kuga–Satake functor on $\mathrm{Sh}(\mathrm{GSpin}(L))$ for any even
> self-dual $L$ of signature $(2, n)$."

Of the three witnesses:

- **K3 Mukai** has signature $(4, 20)$ — **four** positive directions,
  not two. Mukai $(4,20)$ is *not* in HMP's native scope as an
  orthogonal Shimura variety input; the associated domain is
  $\mathrm{SO}(4,20)/(\mathrm{SO}(4)\times\mathrm{SO}(20))$, which is
  of **real rank 4**, not Hermitian symmetric. HMP does not apply to
  the full Mukai lattice.
  - The K3-BKM construction uses instead the **rank-3 orthogonal
    sublattice** $\Lambda^{2,1}_{\mathrm{II}}$ of signature $(2, 1)$,
    which sits inside the extended "Bruinier-side" input
    $\Lambda^{3,2}$ of signature $(3, 2)$. This is what
    `notes/wave8_j5_kudla_millson_level_N.tex` Theorem
    `thm:kudla-millson-level-N-lift` uses (signature
    $\Lambda^{3,2}_{(N)}$ of type $(3,2)$). HMP 2020 §7 covers this
    case: $(n, 2) = (3, 2)$.
  - The "positive-signature count" $c_+ = 4$ of the Mukai lattice is a
    *different* invariant from the HMP input signature: the Mukai
    $c_+$ is read off $H^*(K3, \mathbb Z)$ as a signature invariant
    of the Mukai pairing, not as an HMP Shimura-variety input. The
    hypothesis conflates these two $c_+$'s. (Cross-reference:
    `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:99`
    the **$c_+$ convention lock (Cycle-5 heal)** explicitly records
    this distinction.)

- **Fake Monster** has signature $(25, 1)$ — **one** negative direction,
  not two. $\mathrm{II}_{25,1}$ is a *Lorentzian* lattice; the
  corresponding symmetric space is **hyperbolic 25-space**
  $\mathrm{O}(25,1)/\mathrm{O}(25)$, which is **not** a Hermitian
  symmetric domain. HMP 2020's Kuga–Satake / derived Arakelov
  machinery does not apply to $\mathrm{II}_{25,1}$: the construction
  requires the period domain to be Hermitian symmetric of Type IV,
  which forces signature $(n, 2)$ (two negative directions).
  - The Fake-Monster $K = 50 = 2 \cdot 25$ comes from Borcherds 1990
    *Invent. Math.* 109 (direct construction of the $\mathrm{II}_{25,1}$
    denominator), via the Leech-lattice positive rank and a
    super-parity doubling. It is **not** an HMP Arakelov-Chern-class
    output.
  - The "$(2, n)$ reciprocity" fails uniformly for Fake Monster; see
    `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:99`
    ("For Fake-Monster, the Bruinier reading does not apply uniformly
    to signature-$(25,1)$; the doubled-Leech-rank convention
    $c_+(\mathrm{II}_{25,1}) = 25$ is the ghost-symmetry count of
    Borcherds 1990 on $\mathrm{II}_{25,1}$, numerically matching but
    structurally distinct from the $(2,n)$ reciprocity.")

- **Monster** has signature $(1, 1)$. In the HMP-native reading
  $(2, n)$, this corresponds to $n = -1$, degenerate. The
  Koike–Norton–Zagier denominator $(p-q)\prod(1-p^mq^n)^{c(mn)}$ on
  $\mathbb H \times \mathbb H$ is a Borcherds-product on a **fake**
  $(2, 2)$ input lattice obtained by adjoining the hyperbolic plane
  to $\mathrm{II}_{1,1}$: this is the $\mathrm{II}_{2,2}$ Narain-type
  doubling used by Borcherds 1992 *Invent. Math.* 109. The Monster
  $K = 2$ arises from the Fricke-level-$1$ involution order (Apostol
  1990 §2.8), not from an HMP Arakelov Chern class.

Net: HMP 2020 as written covers signature-$(n, 2)$ orthogonal Shimura
varieties where the Hermitian Hodge structure is forced. Two of the
three witnesses (K3 via full Mukai, Fake Monster) have lattice
signatures that are **not in HMP's native scope** (signature $(4, 20)$
has four positive directions instead of two; signature $(25, 1)$ has
one negative direction instead of two). The third (Monster) is
borderline degenerate at signature $(1, 1)$.

**HMP 2020 Thm 1.1 does NOT cover signatures "$(4, 2)$" and "$(25, 2)$"
as specialisations for K3 Mukai and Fake Monster; those signatures are
misstated in the hypothesis.** The actual signatures are $(4, 20)$ and
$(25, 1)$. HMP's $(n, 2)$ native scope applies instead to:

- the Bruinier-side orthogonal input lattice $\Lambda^{3, 2}$ of
  signature $(3, 2)$ (the Gritsenko–Nikulin route, feeding $\Delta_5$
  on $\mathcal A_2 = \mathrm{Sp}_4(\mathbb Z)\backslash \mathbb H_2$);
- the Monster pseudo-$(2, 2)$ adjoined lattice
  $\mathrm{II}_{1,1}\oplus\mathrm{II}_{1,1}$ (Borcherds 1992).

The Fake-Monster signature-$(25, 1)$ input has **no** HMP-compatible
orthogonal Shimura variety.

### (2) Does HMP handle "principal Heegner in $c_+$-subcone"?

**Answer: no, the torsion-order-on-principal-divisor statement is not
in HMP 2020 Thm 1.1.** HMP Thm 1.1 constructs a derived Kudla
generating series
$$\mathcal Z^{\mathrm{der}}: \mathrm{Sh}(\mathrm{Sp}_{2n})
  \to \bigoplus_m \mathrm{CH}^m(\mathrm{Sh}(\mathrm{SO}(V)))$$
at the level of derived Chow, with **Fourier-coefficient identities**
for the generating series at orbits of low codimension. This is a
*modularity* statement for the generating series of Heegner cycles,
not a *torsion-order* statement for any one cycle's Chern class.

C17 cycle-3 (lines 482–524) confirms this explicitly:

> "Howard–Madapusi-Pera 2020 *Invent. Math.* 219 'Arithmetic of
> Borcherds products' establishes: (Thm 1.1) a derived Kudla
> generating series ... they compute Fourier coefficients of the
> generating series, not torsion orders of Chern-class restrictions.
> The required extension specialises to the principal divisor and
> extracts torsion order from the Gram-form signature."

The **specialisation to the principal Heegner divisor in the
$c_+$-subcone** is not a statement HMP makes. HMP's Arakelov
machinery is on the *whole* generating series; the descent to one
divisor, with torsion order read off the lattice signature, is a
one-step specialisation that *follows conceptually* from their
framework but is **not an as-stated HMP theorem**.

The "principal Heegner divisor in the $c_+$-subcone" is a Vol III
notion (see C17 Executive Summary and Conjecture statement):

- $H_{\min}(L) \subset \mathrm{Sh}(\mathrm O(L))$ = the minimal-codimension
  split Heegner divisor on the Type IV symmetric domain of $L$, whose
  class in $\mathrm{CH}^1$ controls the positive-cone monodromy of the
  Borcherds-lift line bundle $\mathcal L^{\Phi_L}$.
- The "$c_+$-subcone" is the positive-definite-signature subcone of the
  full Heegner divisor system, indexed by the positive-signature count
  $c_+(L)$.

Neither the name "$c_+$-subcone" nor the statement "torsion order of
Chern class on the principal Heegner is $2c_+(L)$" appears in HMP 2020.
The statement is **compatible** with HMP's framework; it is not in the
text.

### (3) Three witnesses: Monster $K = 2$, K3 $K = 8$, Fake Monster $K = 50$

**Numerical verification passes at all three witnesses by three
*separate*, non-HMP routes.** See the per-row status table
`notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:147-154`:

| Row | $L$ | $(K, \hbar^2)$ | Input | Primary-source route |
|-----|-----|----------------|-------|--------------------|
| Monster | $\mathrm{II}_{1,1}$ | $(2, -1/2)$ | $j(\sigma) - j(\tau)$ | Borcherds 1992 *Invent.* 109, Conway–Norton 1979 |
| K3-BKM $\mathbf H_{\Delta_5}$ | $\Lambda^{2,1}_{\mathrm{II}}$ | $(8, -1/8)$ | $\Delta_5 = \mathrm{Grit}(\eta^9\vartheta_1)$ | Gritsenko–Nikulin 1998 |
| Fake-Monster | $\mathrm{II}_{25,1}$ | $(50, -1/50)$ | $\Phi_{12}$ | Borcherds 1990 |
| Enriques | $E_8 \oplus \mathrm{II}_{1,1}(2)$ | $(4, -1/4)$ | $\Delta_5^{\mathrm{Enr}}$ | Borisov–Libgober (conditional) |

Verification at each witness is *not* by HMP specialisation but by
direct per-row primary-source construction. Specifically:

- **Monster**: Borcherds 1992 *Invent. Math.* 109 constructs
  $j(\sigma) - j(\tau) = p^{-1}\prod(1-p^mq^n)^{c(mn)}$ with
  $c_{K3}(n)$ the coefficients of $J(\tau) = j(\tau) - 744$; the
  Fricke involution $\sigma \leftrightarrow \tau$ acts of order 2.
  $K = 2$ reads off (a) $2c_+(\mathrm{II}_{1,1}) = 2 \cdot 1 = 2$
  formally; (b) order of Fricke involution on
  $\mathbb H \times \mathbb H$; (c) Lusztig small-quantum-group order
  at $\zeta^2 = 1$. Three independent routes converge at $K = 2$
  without going through HMP.

- **K3 Mukai**: the three-way identification at $K = 8$ is
  Theorem BZ1 of Wave 2 A04 (see
  `.swarm_outputs/wave2/A04_bezrukavnikov_three_faces_of_8.md`):
  $8 = \mathrm{lcm}(2_{\mathrm{Borcherds\ mult}},\,
  4_{\mathrm{Bruinier\ denom}}) \cdot 2_{\mathrm{Schauenburg\ super}}
  = 4 \cdot 2 = 8$, attributed to (i) Borcherds 1998
  *J. reine angew. Math.* 494 §10 (paramodular multiplier order 2),
  (ii) Gritsenko–Nikulin 1998 *Amer. J. Math.* 120 Table 2
  (Fourier coefficient $c_{\Phi_{10}/\eta^{24}}(1,1,0) = -1/4$
  giving denominator-4 Bruinier gerbe factor), (iii) Schauenburg 1998
  *Comm. Alg.* 26 §3 (super-parity $\mu_4 \hookrightarrow \mu_8$).
  None of these is HMP.

- **Fake Monster**: $K = 50 = 25 \cdot 2$ with $25 = c_+(\mathrm{II}_{25,1})$
  the positive rank of $\mathrm{II}_{25,1}$ and $2$ the super-parity.
  Primary-source route: Gritsenko–Nikulin 1998 Proposition 2.5
  (minimal-embedding lemma for the Leech lattice), Bruinier 2002
  Theorem 5.12 (divisor formula), Lusztig 1990. C17 cycle-2 verifies
  this directly (`C17_Bruinier_Muk_Br_reciprocity.md:473`). HMP is
  inapplicable at signature $(25, 1)$.

**Net: the three numerical identities at Monster $K = 2$, K3 $K = 8$,
Fake Monster $K = 50$ hold, each by a separate primary-source route,
*not* via a single HMP specialisation.** The unification as an
"HMP-generated $c_+$-family" is not what the literature supplies.

## Why not state A

State A ("HMP suffices") requires HMP 2020 Thm 1.1 to furnish, on its
own:

1. Coverage at signatures $(4, 20)$ (K3 Mukai) and $(25, 1)$ (Fake
   Monster). **Absent.** HMP's native scope is $(n, 2)$;
   $(4, 20)$ has four positive directions and $(25, 1)$ has only one
   negative direction. Neither is a Hermitian-symmetric Type IV domain.

2. A torsion-order-on-principal-Heegner-divisor statement.
   **Absent.** HMP states modularity of the generating series; the
   per-divisor torsion order is a downstream specialisation.

3. Uniformity across the $\mathcal B$-family. **Absent.** HMP is
   lattice-by-lattice; the uniformity is a Vol III synthesis.

Any one of these absences already rules out state A; all three rule
it out decisively.

## Why not state B (as posed in C17)

State B in C17 reads the reciprocity as closed *conditional* on HMP
extension. That reading remains correct **for the reciprocity
conjecture as a whole**. But the sub-question of the present closure
— "does HMP 2020 suffice as the primary-source input that makes B a
theorem?" — has a narrower answer: no.

HMP 2020 is a *necessary but not sufficient* input. It is one of the
pillars (alongside Bruinier 2002 Thm 5.12, Kudla–Millson 1986/1990,
Borcherds 1998 §10, Schauenburg 1998) whose combination under the
reciprocity conjecture gives the three-faces identity. The single-step
extension C17 labels $\mathbf{BrukaMilk}$:

> "For every even lattice $L$ of signature $(p, 2)$ with $p \geq 1$
> and every weakly holomorphic modular form
> $f \in M^!_{1-p/2}(\rho_L)$ with principal part supporting a
> principal split Heegner divisor $H_{\min}(L)$, the Borcherds lift
> $\Phi_L = \Psi(f)$ has first Chern class on $H_{\min}(L)$ of torsion
> order $2c_+(L)$ in $\mathrm{CH}^1(H_{\min}(L))_{\mathrm{tors}}$,
> functorially in lattice embeddings $V \hookrightarrow V'$ compatible
> with $c_+$-subcone inclusion."

is exactly the **extension** that would close B to A. This extension
requires:

(a) **Signature widening**: extending HMP's Hermitian-Type-IV
    orthogonal Shimura variety machinery from signature $(n, 2)$ to
    the full positive-signature classification; this is not a
    mechanical generalisation for signatures like $(4, 20)$ or
    $(25, 1)$ where the period domain is not Hermitian symmetric.
    The Mukai lattice $(4, 20)$ route must go via the sublattice
    $\Lambda^{3, 2}$ (signature $(3, 2)$) which is HMP-compatible, but
    the statement then only captures the rank-3 Cartan of the BKM,
    not the full Mukai enhancement. Fake Monster $(25, 1)$ does not
    admit a $\Lambda^{p, 2}$ sublattice of the same $c_+$-subcone
    character.

(b) **Arakelov torsion extraction**: a proof that the generating-series
    Chern class, when evaluated on the principal divisor, has torsion
    order exactly $2c_+(L)$. C17 cycle 3 concludes:
    > "The paper computes the Chern-class generating series; the
    > torsion-order reading at the principal divisor is a one-step
    > descent via the Fourier coefficients of the pole data, which
    > they do not perform."

(c) **$c_+$-subcone uniformity**: a lattice-embedding-functorial
    statement that the torsion order transforms compatibly with
    $c_+$-subcone inclusions $V \hookrightarrow V'$. This is not
    stated in HMP; it would follow if (a) and (b) hold with the
    required functoriality.

## Why state C (genuine extension needed)

Three simultaneous extensions are required — signature widening +
Arakelov torsion extraction + $c_+$-subcone uniformity. While each is
within reach of HMP's framework *in principle*, none is on the page.
The characterisation is thus **not a specialisation of HMP** but a
**new theorem whose proof uses HMP as a primary input** — a genuine
extension.

The distinction matters for the Wave-3 ledger:

- **State A** would mean: invoke HMP 2020 Thm 1.1, let the conclusion
  specialise, write a single page of specialisation argument. False.
- **State B** (as C17 has it) means: the reciprocity as a whole is
  conjectural, with HMP extension as the natural path. True for the
  reciprocity taken in full, but does not itself distinguish whether
  HMP is sufficient or requires extension.
- **State C**: HMP is *necessary* infrastructure but *not sufficient*;
  a publishable, three-part extension of HMP is required. This is
  the correct state for the present closure.

## Cross-references

Primary sources examined for this closure:

- **HMP 2020**: *Invent. Math.* **220** (not 219 as posed in the
  hypothesis); see `notes/wave8_j5_kudla_millson_level_N.tex:220`,
  `notes/wave13_a9_sheaves_BKM_bezrukavnikov.tex:178`, 423.
- **Bruinier 2002**: *Borcherds Products and Chern Classes of
  Heegner Divisors*, LNM 1780; Thm 5.12 (divisor formula; Prop 5.1
  local product expansion — not the torsion-order reciprocity, per
  Wave 2 A04 retraction).
- **Kudla–Millson 1986, 1990**: *Ann. Math.* 124, *Publ. IHES* 71
  (Arakelov Chern-class machinery for theta forms).
- **Mukai 1987**: *Nagoya Math. J.* 81 §1 (signature of the Mukai
  lattice).
- **Borcherds 1990, 1992, 1998**: *Invent.* 109, 109, 132 and
  *J. reine angew. Math.* 494 (Fake-Monster, Monster, singular-theta,
  paramodular multiplier).
- **Gritsenko–Nikulin 1997/1998**: *J. Reine Angew. Math.* 507 and
  *Amer. J. Math.* 120 (BKM denominator identities and Fourier table).
- **Schauenburg 1998**: *Comm. Alg.* 26 §3 (super-parity).
- **Lusztig 1990**: *Geom. Dedicata* 35 Rmk 3.2 (small-quantum-group
  root-of-unity order).

Internal documents consulted:

- `.swarm_outputs/wave3/C17_Bruinier_Muk_Br_reciprocity.md` (primary;
  this closure sharpens its conditional state B to state C on the
  HMP-sufficiency subquestion).
- `notes/wave8_j5_kudla_millson_level_N.tex` (HMP signature-$(2, n)$
  scope, level-$N$ extension for $N \in \{2, 3, 4, 6\}$).
- `notes/wave13_a9_sheaves_BKM_bezrukavnikov.tex` (HMP as platform for
  the sheaf-theoretic avatar $\mathcal F_{\Delta_5}$).
- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md`
  (c_+ convention lock; per-row K status table; signature analysis).
- `notes/platonic_synthesis_waves_11_through_16_healed.tex`
  ($\Psi$-sibling structure; Fake-Monster on $\mathrm{II}_{25,1}$).
- `chapters/theory/quantum_chiral_algebras.tex:3014, 3019, 3022, 3086,
  3143` (existing inflated "Bruinier Prop. 5.1 Heegner-Chern-class
  reciprocity" citations awaiting CG-rectify downgrade per C17
  closure).
- `.swarm_outputs/wave2/A04_bezrukavnikov_three_faces_of_8.md`
  (Wave 2 four-way decomposition of K3 $K = 8$; BZ-R1 retraction of
  Bruinier Prop 5.1 as torsion-order theorem).

## Final state

**C (genuine extension needed).**

The hypothesis "HMP 2020 Thm 1.1 specialises to the principal Heegner
divisor in the $c_+$-subcone uniformly across $\mathcal B$-family" is
**false as posed** on three independent grounds:

1. HMP's signature scope is $(n, 2)$; the hypothesis-claimed signatures
   "$(4, 2)$" and "$(25, 2)$" are wrong against the actual Mukai and
   Leech-Lorentzian lattice signatures $(4, 20)$ and $(25, 1)$, which
   are **not** in HMP's native Hermitian-Type-IV scope.

2. The principal-Heegner torsion-order statement is not in HMP 2020
   Thm 1.1; HMP states modularity of the generating series, not
   torsion order at one divisor.

3. The $c_+$-subcone uniformity across the $\mathcal B$-family is not
   claimed by HMP; it is the Vol III conjectural reciprocity.

Numerical verification at the three witnesses ($K = 2, 8, 50$) is
secured by **three separate primary-source routes** (Borcherds 1992
+ Fricke for Monster; Borcherds 1998 + Gritsenko–Nikulin 1998 +
Schauenburg 1998 for K3; Borcherds 1990 + Gritsenko–Nikulin Prop 2.5
+ Lusztig for Fake Monster), **not** via an HMP specialisation.

The Vol III Bruinier–Mukai reciprocity conjecture
(`conj:bz-mukai-bruinier-reciprocity`) thus requires a genuine
**extension** of HMP 2020, not a specialisation:

- signature-scope widening beyond native $(n, 2)$ Hermitian Type IV;
- Arakelov Chern-class torsion-order extraction on the principal
  divisor;
- $c_+$-subcone uniformity under lattice embeddings.

Each of these is individually a candidate for a publishable theorem
building on the HMP framework; jointly they constitute the named
extension $\mathbf{BrukaMilk}$ whose proof would upgrade C17's state B
to state A. Until then, HMP 2020 is necessary infrastructure, not
sufficient input.

Recommended manuscript action (per C17 final status): downgrade the
"Bruinier Prop 5.1 Heegner-Chern-class reciprocity" attributions in
`chapters/theory/quantum_chiral_algebras.tex` lines 3014, 3019, 3022,
3086, 3143 to cite the four-way decomposition (Bruinier 2002 Thm 5.12
divisor formula + Kudla–Millson 1986 Arakelov Chern + Borcherds 1998
§10 multiplier + Schauenburg 1998 super-parity) and flag the
unification as Conjecture \ref{conj:bz-mukai-bruinier-reciprocity}
with the named extension hypothesis.

Claim-status tag for the reciprocity: \ClaimStatusConjectured.

Claim-status for "HMP 2020 suffices as a primary-source input to close
the reciprocity": **false**; extension required.
