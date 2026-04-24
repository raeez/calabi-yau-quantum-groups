# Agent 04: Beilinson BD/Ran Descent Examiner

## Scope

Claim attacked: the chain-level CY3 construction
\[
\Phi^{(\Sigma_2,C)}_3=\operatorname{SpCh}_{\Sigma_2,C}\circ \Phi^{\mathrm{FA}}_3
\]
descends from a holomorphic/factorization object on the CY3 to an
\(E_1\)-chiral algebra on the reference curve \(C\), and that CFG 2026
arXiv:2602.12412 may replace path-integral language by factorization
homology in this passage.

Files and sources read:

- `CLAUDE.md`, `AGENTS.md`, `~/ecosystem/INVARIANTS.md`,
  `~/ecosystem/AGENTS-HARNESS.md`.
- `chapters/theory/cy_to_chiral.tex`.
- `chapters/theory/cy3_chain_level_bridge.tex`.
- `chapters/theory/e1_chiral_algebras.tex`.
- `chapters/theory/e2_chiral_algebras.tex`.
- `chapters/theory/en_factorization.tex`.
- `chapters/theory/braided_factorization.tex`.
- `chapters/theory/gluing/sec_5_factorization.tex`.
- `compute/lib/cfg25_e1_chiral_lift.py`,
  `compute/lib/cfg25_adversarial_consistency.py`.
- Costello--Francis--Gwilliam, `arXiv:2602.12412`, source
  `2025draft.tex`.

## Verdict

Status: conditional, not proved unconditionally.

The manuscript has the right two-stage architecture:
\[
\Phi^{\mathrm{FA}}_3(\mathcal C)\in E_3\mathrm{HolFA}(X),\qquad
\operatorname{SpCh}_{\Sigma_2,C}(F)=(\int_{\Sigma_2}F)|_C\in
E_1\mathrm{ChirAlg}(C).
\]
The Ran/BD descent is defensible only under explicit descent hypotheses:
the stage-one object must be a genuine holomorphic factorization algebra
or factorization cosheaf, the specialization datum must be framed or
holomorphic in the precise sense used, the pushforward/integration must
preserve factorization products and Weiss codescent, and any Hall
comparison must pass through the still-open
\(\Theta_{\mathrm{hCS}\to\mathrm{Hall}}\) comparison. CFG 2026 supplies a
model for replacing ordinary 3-dimensional Chern--Simons path integrals
by factorization homology; it does not prove the six-real-dimensional
hCS-to-Hall comparison, compact CY3 strictification, or global
CY3-to-chiral functoriality.

Steering correction. The Vol III CY3 avatar must not be collapsed to
CFG's ordinary \(C^\bullet(\mathfrak g)\). That algebra is only the
locally constant/topological associated model obtained after forgetting
the holomorphic directions and contracting a polydisc. The actual CY3
object is the Dolbeault/chiral Chevalley--Eilenberg factorization
algebra in three complex variables: holomorphic jets in
\((z_1,z_2,z_3)\), multidirectional OPE residues along all partial
diagonals in polydiscs, and then the CE-to-chiral-CE/enveloping
factorization algebra passage.

Recommended status labels:

- `thm:cy-to-chiral-d3`: conditional on H1--H4 and on the explicit
  specialisation datum.
- `op:cy3-hcs-hall-comparison`: open; keep as a named open problem.
- K3 x E/BKM specialization through 6d hCS: conditional on the Hall
  comparison and orientation/descent coherences.
- Any claim that CFG 2026 proves the CY3 Hall or BKM comparison:
  reject.

## Required definitions

BD chiral algebra. For a smooth curve \(C\), a Beilinson--Drinfeld
chiral algebra is a \(D_C\)-module \(\mathcal A\) with chiral bracket
\[
\mu:j_*j^*(\mathcal A\boxtimes\mathcal A)\to \Delta_!\mathcal A
\]
for \(j:C^2\setminus \Delta\hookrightarrow C^2\), satisfying the usual
skew-symmetry and Jacobi/factorization compatibility axioms. Equivalently,
via the factorization envelope, it determines a factorization cosheaf on
\(\operatorname{Ran}(C)\), with tensor products on disjoint finite
configurations and collision maps governed by the chiral bracket.
Reference in tree: `chapters/theory/gluing/sec_5_factorization.tex`.

Holomorphic factorization algebra. In the manuscript notation,
\[
E_d\mathrm{HolFA}(X)=
\operatorname{Alg}_{E_d}(\operatorname{ShvFact}^{\mathrm{hol}}(X,\operatorname{Ch}(k))).
\]
Concretely this means a prefactorization assignment to opens of \(X\)
with multiplication maps for pairwise disjoint opens, satisfying Weiss
homotopy-cosheaf descent and carrying the holomorphic/Dolbeault
refinement. An \(E_3\)-algebra in chain complexes is not by itself this
object; it becomes a locally constant factorization algebra only after
the Lurie/Costello--Gwilliam reconstruction hypotheses are met.

CY3 Dolbeault/chiral CE model. On a holomorphic coordinate polydisc
\[
P=D_1\times D_2\times D_3\subset X,\qquad z=(z_1,z_2,z_3),
\]
the hCS local Lie algebra is not \(\mathfrak g\) alone but
\[
L_{\hCS}(P)
  =
  \Omega^{0,\bullet}(P,\mathfrak g),
  \qquad Q=\bar\partial,\qquad
  [\alpha,\beta]_{\hCS}
  =
  \alpha\wedge\beta\otimes[-,-]_{\mathfrak g}.
\]
The classical local observables are the continuous Dolbeault CE
cochains
\[
\Obs_{\hCS}^{\mathrm{cl}}(P)
  \simeq
  C^\bullet_{\mathrm{Lie,cont}}
  \bigl(\Omega^{0,\bullet}_c(P,\mathfrak g),\mathbb C\bigr),
\]
with the BV pairing supplied by
\[
I_{\hCS}(\alpha)
 =
 \int_P \Omega_P\wedge
 \left(
   \frac12\langle\alpha,\bar\partial\alpha\rangle
   +\frac16\langle\alpha,[\alpha,\alpha]\rangle
 \right).
\]
Quantization replaces the differential by the BV quantum differential
\[
d_{\hCS}^q
  =
  d_{\mathrm{CE}}+\{I_{\hCS},-\}_{\mathrm{BV}}+\hbar\Delta_{\mathrm{BV}}
\]
on the completed observables, subject to the anomaly-cancellation
hypotheses. The chiral/Ran object is the factorization envelope
\[
\Phi^{\mathrm{FA}}_3(\mathcal C)|_P
  \simeq
  U^{\mathrm{fact},E_3}_{P}
  \bigl(J^{\mathrm{hol}}_\infty L_{\hCS}\bigr),
\]
or, on the bar side,
\[
B_{E_3}\bigl(\Phi^{\mathrm{FA}}_3(\mathcal C)|_P\bigr)
  \simeq
  \mathrm{CE}^{\mathrm{ch},E_3}_*
  \bigl(J^{\mathrm{hol}}_\infty L_{\hCS}\bigr).
\]
Its product maps for disjoint polydiscs
\[
\widehat\otimes_i\,\Obs_{\hCS}^q(P_i)
  \longrightarrow
\Obs_{\hCS}^q(P)
\]
are holomorphic in the positions of the \(P_i\) and have singularities
only along partial diagonals. In local fields this means
\[
a(z)b(w)
\sim
\sum_{\alpha\in\mathbb N^3}
\frac{(a_{(\alpha)}b)(w)}
{(z_1-w_1)^{\alpha_1+1}
 (z_2-w_2)^{\alpha_2+1}
 (z_3-w_3)^{\alpha_3+1}},
\]
with \(a_{(\alpha)}b\) computed by iterated residues in the three
holomorphic directions. CFG's \(C^\bullet(\mathfrak g)\) is recovered
only from the locally constant shadow
\[
\Omega^{0,\bullet}(P)\simeq\mathbb C
\quad\Longrightarrow\quad
\Obs_{\hCS}^{\mathrm{cl}}(P)_{\mathrm{lc}}
\simeq C^\bullet(\mathfrak g),
\]
which forgets jets, multidirectional OPE data, and Ran collision
coherences.

Specialization functor. The manuscript's stage-two functor is
\[
\operatorname{SpCh}_{\Sigma_2,C}:E_3\mathrm{HolFA}(X)\to E_1\mathrm{HolFA}(C),
\qquad
\operatorname{SpCh}_{\Sigma_2,C}(F)=(\int_{\Sigma_2}F)|_C.
\]
The kernel form in `cy_to_chiral.tex` is
\[
(\pi_C)_*(\pi_X^*F\otimes^{\mathbb L}\mathcal O_{\Sigma_2\times C}),
\]
with residual \(E_1\)-structure obtained by Dunn restriction/excision.
For \(K3\times E\), this must be read as holomorphic/relative pushforward
along the K3 fibre to \(E\), not as ordinary framed factorization
homology over a real 2-cycle.

Descent conditions. The descent step requires:

1. \(\Phi^{\mathrm{FA}}_3(\mathcal C)\) is constructed as the
   Dolbeault/chiral CE factorization algebra on the holomorphic
   Weiss/Ran site, not merely as an abstract \(E_3\)-algebra and not as
   CFG's locally constant \(C^\bullet(\mathfrak g)\).
2. The chosen \((\Sigma_2,C)\) datum supplies the required product
   tubular geometry, framing, or holomorphic proper-pushforward datum.
3. The specialization preserves factorization products, excision, and
   Weiss codescent.
4. The output on \(C\) is an ordered \(E_1\)-chiral/factorization object;
   braided \(E_2\) structure may only be asserted on the chiral Drinfeld
   center.
5. If Hall or BKM identifications are invoked, the map
   \(\Theta_{\mathrm{hCS}\to\mathrm{Hall}}\) must satisfy the six
   orientation, Thom--Sebastiani, convolution, local-chart, double, and
   descent conditions stated in `cy3_chain_level_bridge.tex`.

## ATTACK -> HEAL cycles

### Cycle 1: CFG replacement is too strong, and \(C^\bullet(\mathfrak g)\) is only a shadow

ATTACK. CFG 2026 proves that ordinary 3-dimensional Chern--Simons local
observables form a filtered \(E_3\)-algebra and that factorization
homology with 1-dimensional defects recovers Reshetikhin--Turaev link
invariants. This is not a theorem about six-real-dimensional holomorphic
Chern--Simons theory on a CY3, critical CoHA, Hall convolution, or BKM
denominator products. Any direct inference
\[
\text{CFG ordinary CS}\Rightarrow
\Theta_{\mathrm{hCS}\to\mathrm{Hall}}\Rightarrow \Phi_3
\]
is invalid. A second, subtler invalid inference is
\[
\Phi^{\mathrm{FA}}_3|_P \stackrel{\text{wrong}}{=} C^\bullet(\mathfrak g).
\]
This throws away the Dolbeault complex, holomorphic jets in
\((z_1,z_2,z_3)\), multidirectional OPE residues, and Ran collision
coherences.

HEAL. Use CFG only as a formal replacement principle: path-integral
expressions in ordinary CS can be restated as factorization homology of
local observables, and line defects as stratified factorization homology
with perfect modules. The repaired local formula is
\[
\Phi^{\mathrm{FA}}_3(\mathcal C)|_P
 \simeq
U^{\mathrm{fact},E_3}_{P}
\bigl(J^{\mathrm{hol}}_\infty\Omega^{0,\bullet}_P(\mathfrak g)\bigr),
\qquad
\operatorname{LC}_{\mathrm{top}}\bigl(\Phi^{\mathrm{FA}}_3|_P\bigr)
 \simeq C^\bullet(\mathfrak g),
\]
where the second term is only the locally constant associated model. The
CY3 manuscript already has the correct firewall in
`warn:cy3-no-cfg-shortcut` and
`op:cy3-hcs-hall-comparison`: the hCS-to-Hall map remains a separate
open comparison in oriented Hall-valued factorization cosheaves.

Status after heal: conditional, with CFG as analogy/evidence only and
with \(C^\bullet(\mathfrak g)\) demoted to the topological associated
model.

### Cycle 2: \(E_3\) algebra does not automatically give BD/Ran descent

ATTACK. A chain-level \(E_3\)-algebra in \(\operatorname{Ch}(k)\), or
CFG's \(C^\bullet(\mathfrak g)\), does not automatically define a
holomorphic factorization algebra on \(X\), nor a BD chiral algebra on
\(C\). Ran descent requires a sheaf/cosheaf on the Ran space or Weiss
site with factorization products and homotopy codescent. In CY3 those
products must be products over holomorphic polydiscs, not just products
of locally constant disks. The stress-test remark in `cy_to_chiral.tex`
correctly notes this gap.

HEAL. State the hypothesis at the right level:
\[
\Phi^{\mathrm{FA}}_3(\mathcal C)
  =
  U^{\mathrm{fact},E_3}_{X}
  \bigl(J^{\mathrm{hol}}_\infty L_{\hCS}\bigr)
  \in E_3\mathrm{HolFA}(X),
  \qquad
L_{\hCS}=\Omega_X^{0,\bullet}\otimes\mathfrak g
\]
must be an input or a constructed object, not inferred solely from an
abstract \(E_3\)-algebra. Once this is supplied, the specialization
functor can be evaluated as factorization homology/pushforward, and the
BD/Ran envelope on \(C\) can be formed. The bar-side control is
\[
B_{E_3}\bigl(\Phi^{\mathrm{FA}}_3\bigr)
\simeq
\mathrm{CE}^{\mathrm{ch},E_3}_*
\bigl(J^{\mathrm{hol}}_\infty L_{\hCS}\bigr),
\]
so descent is checked on chiral CE chains with their three-directional
residue operations.

Status after heal: theorem acceptable only where the stage-one
holomorphic factorization algebra has been built.

### Cycle 3: \(\Sigma_2\) has a dimension/framing ambiguity

ATTACK. The notation \(\Sigma_2\) is overloaded. In some local
factorization statements it behaves like a real 2-dimensional transverse
cycle giving \(E_3\to E_1\). In the K3 x E application,
\(\Sigma_2=K3\) is a complex surface, real 4-dimensional, and the
specialization is holomorphic pushforward along \(p_E:K3\times E\to E\).
Ordinary framed factorization homology over a real 2-cycle cannot be
silently substituted for the K3 fibre pushforward.

HEAL. Keep two distinct readings:

- local framed/transverse integration: \(\Sigma^{\mathrm{real}}_2\) is a
  real 2-cycle in the topological \(E_3\)-model;
- K3 x E specialization: \(\Sigma^{\mathrm{hol}}_2=K3\) is a complex
  surface and \(\operatorname{SpCh}_{K3,E}\) is holomorphic/relative
  pushforward to \(E\).

The second is the one relevant to \(\Delta_5\), BKM, and K3 x E. The
integration owner should normalize the notation before any theorem is
promoted beyond conditional status.

Status after heal: not fatal if made explicit; fatal if left ambiguous
inside a proof.

### Cycle 4: BD chiral and ordered \(E_1\)-chiral are being conflated

ATTACK. A BD chiral algebra on a curve is a symmetric/unordered Ran
factorization object with collision maps encoded by the chiral bracket.
The manuscript's CY3 output is natively an ordered \(E_1\)-chiral object
on \(C\). If one writes simply "BD chiral algebra" without specifying the
ordered \(E_1\) structure or the passage through the factorization
envelope, one risks smuggling in braided or symmetric structure.

HEAL. State the CY3 conclusion as:
\[
A_C\in E_1\mathrm{ChirAlg}(C)
\]
or as a factorization cosheaf on the ordered Ran/configuration category
of \(C\). If a BD-style description is desired, explicitly pass through
the factorization envelope and specify which symmetry has been forgotten
or restored. Braided \(E_2\) structure belongs to
\[
Z^{\mathrm{der}}_{\mathrm{ch}}\bigl(\operatorname{Rep}^{E_1}(A_C)\bigr),
\]
not to \(A_C\) itself.

Status after heal: manuscript's E1/E2 discipline is broadly correct;
the report recommends preserving the ordered-Ran language in all CY3
statements.

### Cycle 5: Cech/Ran descent is overstated on arbitrary covers

ATTACK. The quiver-chart descent discussion asserts degeneration and
strict gluing using contractibility of \(E_1\)-operation spaces and
strict restriction maps. This does not by itself kill higher Cech
cohomology for an arbitrary cover or arbitrary Ran/Weiss site. Descent
depends on the cover being Weiss/cofinal/acyclic enough and on the
higher cocycle data living in a controlled \((\infty,1)\)-category.

HEAL. Restrict the degeneration statement to the named finite
quiver-chart atlas where the local computation and tests support it. For
general CY3 descent, require an explicit Weiss cover, a proof that the
cover is cofinal for finite configurations, and a homotopy-colimit
calculation in the target category. Do not promote this to a universal
strict Cech theorem.

Status after heal: computed atlas-level claim plausible; universal
descent theorem remains conditional.

### Cycle 6: Hall/BKM specialization needs orientation descent

ATTACK. Even after the Ran/BD descent of \(\Phi^{\mathrm{FA}}_3\), the
route to Hall, Yangian, Drinfeld double, or BKM data requires orientation
line choices, determinant-square-root transport, Thom--Sebastiani
compatibility, and Hall convolution compatibility. These are not formal
consequences of BD descent.

HEAL. Keep the Hall comparison in the oriented Hall-valued
factorization-cosheaf category of `cy3_chain_level_bridge.tex`. Require
the six conditions in `op:cy3-hcs-hall-comparison`, especially the
residual \(\mathbb Z/2\) obstruction on triple overlaps and compatibility
with Thom--Sebastiani convolution. The K3 x E BKM statements should
continue to cite this as a live hypothesis.

Status after heal: BKM specialization remains conditional; the local
Ran descent does not close the Hall comparison.

### Cycle 7: Stage-two descent must push forward chiral CE data

ATTACK. Even if Cycle 1 is fixed, there is a remaining collapse risk:
one might first replace the CY3 object by \(C^\bullet(\mathfrak g)\) and
then apply \(\operatorname{SpCh}_{\Sigma_2,C}\). That produces a
constant/locally constant algebra on \(C\), not the Vol III chiral
specialization. It loses transverse holomorphic jets, residues from the
two integrated complex directions, and the induced OPE coefficients on
the curve.

HEAL. Stage two must be applied before taking any locally constant
shadow. For a test open \(V\subset C\), the repaired formula is
\[
A_C(V)
  =
  \operatorname{SpCh}_{\Sigma_2,C}(F)(V)
  =
  \int_{\Sigma_2}^{\mathrm{fact}}
  F|_{\Sigma_2\times V},
  \qquad
F=\Phi^{\mathrm{FA}}_3(\mathcal C).
\]
When the factorization envelope commutes with the relevant exact
holomorphic pushforward, this is controlled by
\[
A_C
 \simeq
 U^{\mathrm{fact},E_1}_{C}
 \left(
   R\Gamma_{\mathrm{fact}}
   \bigl(\Sigma_2,
   J^{\mathrm{hol}}_\infty L_{\hCS}|_{\Sigma_2\times C}\bigr)
 \right),
\]
and on the bar side by
\[
B_{E_1}(A_C)
\simeq
\mathrm{CE}^{\mathrm{ch},E_1}_*
\left(
   R\Gamma_{\mathrm{fact}}
   \bigl(\Sigma_2,
   J^{\mathrm{hol}}_\infty L_{\hCS}|_{\Sigma_2\times C}\bigr)
\right).
\]
This is the correct Ran/descent avatar of "integrating out" the two
transverse complex directions. The topological model
\(\int_{\Sigma_2}C^\bullet(\mathfrak g)\) is only a decategorified or
locally constant shadow and should not be used as the theorem-level
object.

Status after heal: add exactness of holomorphic pushforward/envelope
commutation to the descent gates.

## Findings

1. Major: CFG 2026 is being used correctly only when it is treated as an
   ordinary-CS factorization-homology model. Its \(C^\bullet(\mathfrak g)\)
   is the locally constant/topological associated model, not the Vol III
   CY3 avatar. It does not prove hCS-to-Hall, CY3 Hall convolution, or
   BKM specialization.
2. Major: \(\operatorname{SpCh}_{\Sigma_2,C}\) needs explicit separation
   between real transverse factorization homology and holomorphic K3
   fibre pushforward.
3. Major: the stage-one object should be written as a
   Dolbeault/chiral CE factorization algebra with holomorphic jets and
   polydisc factorization products before applying \(\operatorname{SpCh}\).
4. Moderate: the CY3 output should remain explicitly \(E_1\)-chiral or
   ordered-Ran; BD/unordered language needs an envelope/forgetful
   qualification.
5. Moderate: strict Cech descent/degeneration should not be stated for
   arbitrary covers without a Weiss/cofinality and homotopy-colimit
   argument.
6. Moderate: Hall/BKM descent requires orientation and
   Thom--Sebastiani coherences beyond Ran descent.
7. Low: compute files still use the label `cfg25` for a 2026 arXiv
   source. This is harmless for tests but should not leak into
   manuscript prose. `cfg25_adversarial_consistency.py` also marks the
   volume-analogue row as filled while the section verdict calls it a
   complete gap; the report sides with the gap verdict unless a separate
   proof is supplied.

## Computation

Targeted verification run:

```bash
pytest -q \
  compute/tests/test_cfg25_e1_chiral_lift.py \
  compute/tests/test_cfg25_adversarial_consistency.py \
  compute/tests/test_chiral_homology_ran_k3.py \
  compute/tests/test_factorization_categories_chiral.py
```

Result: 339 passed in 2.89 seconds.

## Final recommendation

Do not retract the chain-level CY3 theorem. Keep it conditional and
sharpen the theorem text around the five required gates:

1. stage-one object is the Dolbeault/chiral CE holomorphic
   factorization algebra
   \(U^{\mathrm{fact},E_3}(J^{\mathrm{hol}}_\infty L_{\hCS})\), with
   Weiss/Ran descent over holomorphic polydiscs;
2. \(\operatorname{SpCh}_{\Sigma_2,C}\) is a precisely typed
   specialization functor, with K3 x E treated as holomorphic
   pushforward;
3. CY3 output is \(E_1\)-chiral, with \(E_2\) only on the chiral
   Drinfeld center;
4. CFG 2026 is an ordinary-CS factorization-homology replacement for
   path integrals, and \(C^\bullet(\mathfrak g)\) is only the
   locally constant/topological associated model;
5. the CE-to-chiral CE/enveloping factorization algebra passage must
   commute with the holomorphic pushforward or else be retained as an
   explicit hypothesis.

Under those restrictions, the Ran/BD descent lane is coherent. Without
them, the claimed chain-level \(\Phi_3\) descent is underproved.
