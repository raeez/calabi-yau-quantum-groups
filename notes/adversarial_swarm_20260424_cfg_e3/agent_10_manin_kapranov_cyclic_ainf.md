# Agent 10 -- Manin-Kapranov Cyclic A-infinity / CY-Category Examiner

Date: 2026-04-24

Scope: chain-level input side for `PhiFA_3`, against the CFG 2026
filtered `E_3` Chern--Simons construction, arXiv:2602.12412.

Owned file: `notes/adversarial_swarm_20260424_cfg_e3/agent_10_manin_kapranov_cyclic_ainf.md`.

Manuscript files edited: none.

## Executive Verdict

The minimal true input for chain-level `PhiFA_3` is not the ordinary
Chevalley--Eilenberg algebra `C^*(g)`.  CFG's `C^*(g)` is the
locally-constant/topological associated model obtained after the de Rham
or Dolbeault directions have been collapsed by a Poincare lemma.  The
CY3 object relevant here is the Dolbeault/chiral CE object in three
holomorphic variables: compactly supported Dolbeault fields on
polydiscs, holomorphic jets in `z_1,z_2,z_3`, multidirectional OPE
residues, and the CE-to-chiral-CE/enveloping factorization algebra.

The correct input side is:

1. A smooth proper/pretriangulated cyclic `A_\infty` category `C` over
   characteristic zero, with the full operations `m_n` retained at
   chain level.
2. A negative-cyclic CY3 class `[sigma] in HC^-_3(C)`, not merely a
   Hochschild trace, whose Hochschild image gives a nondegenerate
   degree `-3` cyclic pairing / trace.
3. A compatible cyclic bar/cobar package: `B(C)`, cyclic bar quotient,
   Connes operator, and the homotopies recording cyclicity at chain
   level.
4. A CY3 target or local CY3 chart with Dolbeault operator and
   holomorphic volume form `Omega_X`, so that the topological `E_3`
   envelope is lifted to a holomorphic factorization algebra.
5. A chain-level `S^3`-framing datum or Costello-TCFT cancellation
   witness compatible with `[sigma]`, the cyclic bar construction, and
   the Connes hierarchy.
6. For the final curve-valued chiral algebra, an admissible
   specialization datum `(Sigma_2,C)`.  This belongs to `Phi_3`, not to
   the native Stage-1 object alone.

Status: conditional in general, verified only in the manuscript's
declared formal/toric/local loci.  CFG supplies a valuable comparison
object for the locally constant shadow, but it does not replace the
CY3 cyclic `A_\infty` input and does not prove the hCS-to-Hall or
`PhiFA_3` construction.

## Source Anchors Read

Local manuscript and compute anchors:

- `chapters/theory/cyclic_ainf.tex:55-84`: cyclic `A_\infty` algebra,
  degree `d` pairing, and the negative-cyclic lift.
- `chapters/theory/cyclic_ainf.tex:97-135`: cyclic bar complex and the
  obstruction from non-adjacent contractions; strict `[m_k,B^{(2)}]`
  is not zero in general.
- `chapters/theory/cyclic_ainf.tex:240-261`: CY3 chain-level statement
  is conditional; `S^3` framing is an input or separately verified
  witness.
- `chapters/theory/cy_categories.tex:207-226`: cyclic `A_\infty`
  category and negative-cyclic CY class.
- `chapters/theory/cy_categories.tex:229-255`: the `d=3` extension is
  object-level and conditional on the `S^3` framing plus admissible
  specialization.
- `chapters/theory/cy_to_chiral.tex:221-298`: two-stage construction
  `PhiFA_d` then `SpCh`, and the `d>=3` holomorphic/framing obstruction.
- `chapters/theory/cy3_chain_level_bridge.tex:45-110`: CY3 hCS
  observables, Dolbeault CE, holomorphic jets, polydisc factorization,
  and ordinary `C^*(g)` only as locally constant shadow.
- `chapters/theory/cy3_chain_level_bridge.tex:294-360`: CFG warning and
  open hCS-to-Hall comparison.
- `chapters/theory/cy3_chain_level_bridge.tex:410-569`: Deligne-
  Tamarkin, Tradler--Menichi--Ginzburg BV operator, conditional `E_3`
  envelope, and holomorphic lift.
- `chapters/theory/cy3_chain_level_bridge.tex:599-660`: CFG comparison
  and stated scope restrictions.
- `compute/lib/s3_framing_chain_level.py`: schematic `S^3` framing
  data, `d=3 -> E_1`, and toy/formal verification lanes.
- `compute/tests/test_s3_framing_chain_level.py`: regression tests for
  `S^3` framing, including a limitation noted below.
- `compute/lib/cy3_chain_framing.py`: local obstruction hierarchy,
  hCS trivialization witness, and non-toric analytic obstruction lane.
- `compute/tests/test_cy3_chain_framing.py`: targeted framing and hCS
  obstruction tests.

CFG arXiv source anchors, from `arXiv:2602.12412`:

- `2025draft.tex:218-229`: main theorem constructs filtered `E_3`
  Chern--Simons algebra and Wilson-line module trace.
- `2025draft.tex:343-354`: Chern--Simons factorization algebra is
  locally constant; locally constant factorization algebras on `R^3`
  are `E_3` algebras.
- `2025draft.tex:377-397`: local observables on a ball are described
  by `C^*(g)` and filtered deformations of it.
- `2025draft.tex:1578-1588`: classical observables are
  `C^*(Omega^*(M) tensor g)`.
- `2025draft.tex:1630-1636`: for `M=R^3`, Poincare lemma gives
  `C^*(g^{R^3}) ~= C^*(g)`.
- `2025draft.tex:1672-1710`: local constancy and the filtered `E_3`
  algebra associated to `C^*(g)`.
- `2025draft.tex:1740-1750`: deformation complex
  `C_Lie^{>=1}(g)[3]`; no obstruction by `H^4(g)=0`, deformations by
  `H^3(g)`.
- `2025draft.tex:1861-1864`: quantum observables remain locally
  constant and determine filtered `E_3` algebras.
- `2025draft.tex:1944-1949`: first-order shifted Poisson bracket on
  `C^*(g)[[hbar]]` from the invariant pairing.

## Cycle 1 -- Is a Hochschild Trace Enough?

Attack: replace the negative-cyclic CY3 class by a Hochschild trace
`Tr: HH_3(C) -> k`.  This would make the input look like an ordinary
Frobenius/cyclic pairing, and might appear sufficient for the
Tradler--Menichi BV operator.

Failure mode: this loses the `S^1`-equivariant datum.  The manuscript
explicitly states that the cyclic invariance data lift the Hochschild
class to `HC^-_d(A)` and that this lift is essential for the `S^d`
framing.  `cy_categories.tex` likewise defines the CY structure by a
negative-cyclic class whose Hochschild image is nondegenerate.

Heal: the minimal input must include `[sigma] in HC^-_3(C)`, with its
Hochschild image giving the degree `-3` trace/pairing.  A bare
Hochschild trace is a shadow, not the chain-level CY3 datum.

Status: attack rejected.  Minimal datum strengthened from "trace" to
"negative-cyclic CY3 class plus nondegenerate Hochschild image."

## Cycle 2 -- Does a Cyclic Pairing Automatically Give `PhiFA_3`?

Attack: once a smooth proper CY3 category has a cyclic `A_\infty`
enhancement, the chain-level factorization algebra `PhiFA_3(C)` should
follow automatically.

Failure mode: cyclicity controls adjacent contractions in the cyclic
bar complex.  It does not by itself kill non-adjacent contractions.
The local source records that strict `[m_k,B^{(2)}]` is generically
nonzero for non-formal CY3 cyclic `A_\infty` algebras; only the full
Costello-TCFT cross-degree cancellation makes the total anticommutator
vanish.  The `cy_to_chiral.tex` construction separates the algebra at
a point, the topological `E_d` factorization envelope, and the
holomorphic `E_d` factorization algebra; for `d>=3`, the last step is
the `S^d` framing problem / `[m_3,B^{(2)}]` obstruction.

Heal: cyclic `A_\infty` structure is necessary but not sufficient.
One must add a chain-level `S^3` framing / TCFT cancellation witness,
or restrict to the formal/toric loci where the manuscript and compute
suite verify the witness.

Status: attack succeeds against any unconditional phrasing.  The healed
claim remains conditional.

## Cycle 3 -- Can We Retain Only Cohomology or `HH^*(C)`?

Attack: use the cohomological Gerstenhaber algebra `HH^*(C)` and its
Deligne--Tamarkin `E_2` action as the complete input.  Then Dunn
additivity and a cyclic BV operator can be used to promote to an `E_3`
algebra, avoiding the full `A_\infty` model.

Failure mode: the manuscript's own cyclic discussion distinguishes
chain-level nonminimal data from cohomology.  Cyclicity, Connes
operators, cyclic rotations, and the non-adjacent contraction
cancellations are chain-level statements.  The `cy3_chain_level_bridge`
does use Deligne--Tamarkin and Tradler--Menichi--Ginzburg, but its
Stage-1 theorem is conditional and its canonicity is only up to the
GRT torsor.  A strict chain model still needs the full operations
`m_n`, compatible cyclic homotopies, and transfer data.

Heal: `HH^*(C)` with its brace/Gerstenhaber structure is part of the
envelope construction, but it is not a replacement for the cyclic
`A_\infty` input.  The minimal datum should be stated at the category
or chosen model level, not merely at cohomology level.

Status: attack rejected as a shortcut; accepted as a useful associated
cohomological description.

## Cycle 4 -- Can CFG's `C^*(g)` Replace the CY3 Input?

Attack: CFG constructs a filtered `E_3` algebra deforming `C^*(g)`;
therefore use `C^*(g)` as the CY3 avatar for `PhiFA_3`.

Failure mode: CFG reaches `C^*(g)` through local constancy.  In the
paper source, classical observables on `M` are
`C^*(Omega^*(M) tensor g)`, and for `M=R^3` the Poincare lemma gives
`C^*(g^{R^3}) ~= C^*(g)`.  This is exactly the topological associated
model.  The CY3 bridge source explicitly says the hCS object on a
polydisc is
`C^*_{Lie,cont}(Omega_c^{0,*}(P,g)[1])`, then its holomorphic-jet and
chiral CE/enveloping factorization algebra.  It has factorization over
disjoint holomorphic polydiscs and multi-index poles
`(z_i-w_i)^(-alpha_i-1)`.

Heal: CFG may be cited as evidence for the locally constant
topological shadow and for filtered `E_3` technology.  It cannot be
used as the CY3 chiral/Dolbeault construction.  Any comparison must
pass through an explicit functor from the Dolbeault/chiral CE object to
the locally constant model, and must record the information lost:
holomorphic jets, multidirectional residues, polydisc descent, and the
CY volume-form coupling.

Status: attack rejected.  This is the central no-shortcut point.

## Cycle 5 -- Does `pi_3(BU)=0` Close the `S^3` Framing Problem?

Attack: the compute module reports the odd-dimensional obstruction
group `pi_3(BU)=0`; therefore the `S^3` framing is automatic.

Failure mode: topological obstruction vanishing is weaker than a
chain-level framing map compatible with the cyclic bar complex,
Connes hierarchy, and CY trace.  The `s3_framing_chain_level.py`
witness is deliberately schematic: it records `d=3 -> E_1`, a formal
`F=B^{(3)}` dictionary, and verified toy/formal cases.  It does not
derive the required Costello-TCFT cancellation for arbitrary compact
CY3 categories.  One test labelled as a nontrivial `F^2=0` check uses
trace keys on mixed triples but constructs repeated-generator elements,
so it is vacuous for nonzero triple contractions; it is still a useful
regression test for the formal zero lane, not a proof of the general
claim.

Heal: distinguish:

- Topological obstruction: vanishes in the relevant odd-dimensional
  obstruction group.
- Chain-level obstruction: still requires a chosen or constructed
  `S^3` framing / TCFT cancellation witness.
- Verified loci: toric/formal local cases and conifold-style witnesses
  covered by compute tests.
- General compact CY3: conditional/open.

Status: attack succeeds against overreading the compute witness.

## Cycle 6 -- Does Bar/Cobar Inversion Already Produce Chiral CE?

Attack: since `B(A)` and `Omega B(A)=A` encode the cyclic algebra, the
chiral CE/enveloping factorization algebra follows formally.

Failure mode: bar/cobar inversion is algebraic.  The CY3 chiral object
requires holomorphic factorization over polydiscs, Dolbeault
resolution, continuous CE duals, holomorphic jets, and multi-residue
OPEs.  The bridge source explicitly separates
`CE_*^{ch,E3}(J_hol^\infty L_hCS)` from the ordinary CE algebra and
says ordinary `C^*(g)` appears only after the locally constant collapse.

Heal: bar/cobar is part of the input algebraic package, but the
chiralisation step is additional.  The reportable minimal datum should
say "cyclic bar/cobar plus a holomorphic factorization-envelope
construction", not "bar/cobar alone."

Status: attack rejected as an algebraic overreach.

## Cycle 7 -- Does `PhiFA_3` Automatically Identify With Hall/CoHA?

Attack: once hCS-style `PhiFA_3` exists, identify it with the CY3 Hall
or CoHA object.

Failure mode: the bridge source states the hCS-to-Hall comparison as an
open theorem-shaped problem.  The required map must preserve Dolbeault
topology, Weiss descent, the BV bracket/Hall product after CY3 shift,
the `C^3` chart, Drinfeld doubling, orientation data, determinant-line
square roots, and Thom--Sebastiani products.  CFG has no such Hall
comparison; it is ordinary 3d Chern--Simons.

Heal: keep the hCS-to-Hall orientation comparison as a separate
obstruction, not as part of CFG and not as a consequence of cyclic
`A_\infty` input alone.

Status: attack succeeds against any immediate Hall identification.

## Minimal True Input Datum

This is the narrowest input statement I can defend after the attacks:

Let `C` be a smooth proper/pretriangulated cyclic `A_\infty` category
over a characteristic-zero field, with `HH^0(C)=k`.  Choose:

1. A chain-level cyclic `A_\infty` model for `C`, including all
   operations `m_n` and their cyclic invariance homotopies.
2. A negative-cyclic CY3 class `[sigma] in HC^-_3(C)` whose image in
   Hochschild homology induces a nondegenerate degree `-3` trace /
   pairing.
3. The cyclic bar/cobar data: bar coalgebra, cyclic bar quotient,
   Connes operator, and compatibility of `[sigma]` with the cyclic
   differential.
4. A CY3 analytic target or local chart `(X,Omega_X)` with Dolbeault
   complex; locally this supplies `Omega_c^{0,*}(P,g)[1]`,
   holomorphic jets, and continuous/chiral CE observables.
5. A chain-level `S^3` framing datum or equivalent Costello-TCFT
   cancellation witness compatible with the cyclic bar complex and the
   Dolbeault/chiral envelope.
6. A choice of Deligne--Tamarkin/Formality pinning, recorded up to the
   expected GRT torsor.
7. For the curve-valued specialization only, an admissible
   `(Sigma_2,C)` specialization datum.

Then the defended output is a conditional object-level native
holomorphic factorization algebra

```text
PhiFA_3(C) in E_3 HolFA(X)
```

and after specialization a curve-side `E_1` chiral algebra

```text
Phi_3^{(Sigma_2,C)}(C) = SpCh(PhiFA_3(C)).
```

This statement must not be rewritten as `PhiFA_3(C)=C^*(g)`.  At most,
`C^*(g)` is a locally constant associated model after collapsing the
three real/topological directions, or a special finite-dimensional
shadow of the Dolbeault/chiral CE construction.

## Obstruction List

1. Negative-cyclic lift obstruction: a Hochschild trace is insufficient
   for the CY3 framing.  Need `[sigma] in HC^-_3(C)`.
2. Non-adjacent contraction obstruction: cyclic invariance controls
   adjacent contractions but does not by itself force
   `[m_k,B^{(2)}]=0` for non-formal CY3 categories.
3. `S^3` framing obstruction: `pi_3(BU)=0` removes one topological
   obstruction but does not construct the chain-level framing map or
   its Connes compatibility.
4. Formality/GRT obstruction: Deligne--Tamarkin formality gives
   structure up to torsor choices; it does not produce a unique strict
   chain-level `PhiFA_3`.
5. Holomorphic lift obstruction: the move from topological `E_3`
   algebra to holomorphic factorization algebra needs Dolbeault
   operator, volume form, analytic locality, and anomaly cancellation.
6. Chiral CE obstruction: ordinary CE cochains do not encode
   holomorphic jets or multi-index OPE residues.  Need chiral CE /
   enveloping factorization algebra.
7. CFG collapse obstruction: CFG's `C^*(g)` is obtained by local
   constancy and Poincare lemma.  It is not the CY3 object before
   collapse.
8. Bar/cobar insufficiency: `Omega B(A)=A` does not by itself give
   the holomorphic Ran/polydisc factorization algebra.
9. Hall comparison obstruction: hCS-to-Hall orientation-preserving
   comparison remains a separate open datum.
10. Functoriality obstruction: the local theorem is object-level; a
    global functor on all CY3 morphisms is not established by these
    ingredients.
11. Compact CY3 obstruction: toric/formal/local witnesses do not prove
    the generic compact CY3 case.

## CFG Classification

CFG 2026 proves, in the inspected source, a filtered `E_3` deformation
of the locally constant Chern--Simons observable algebra whose
classical local model is quasi-isomorphic to `C^*(g)` on `R^3`.  The
paper also constructs representation-theoretic modules and recovers
Reshetikhin--Turaev link invariants by factorization homology trace.

This is not the same input problem as chain-level `PhiFA_3` from a
cyclic CY3 `A_\infty` category.  The CFG model may be used as:

- a topological associated model;
- evidence that filtered `E_3` deformation technology behaves well in
  ordinary 3d Chern--Simons;
- a comparison target after locally constant collapse;
- a warning that the `E_3` structure alone does not remember the
  holomorphic CY3 data.

It may not be used as:

- a replacement for `[sigma] in HC^-_3(C)`;
- a replacement for the cyclic `A_\infty` operations and their
  homotopies;
- a proof of the Dolbeault/chiral CE object;
- a proof of multidirectional OPE/factorization over polydiscs;
- a proof of hCS-to-Hall or CoHA identification;
- a proof that compact CY3 categories automatically satisfy the
  chain-level `S^3` framing.

## Compute/Test Verification

Targeted tests run:

```bash
python3 -m pytest \
  compute/tests/test_s3_framing_chain_level.py \
  compute/tests/test_cy3_chain_framing.py \
  compute/tests/test_chiral_ce_complex.py \
  compute/tests/test_dolbeault_cy3_homotopy.py -q
```

Result:

```text
301 passed in 0.47s
```

CFG-adjacent consistency tests run:

```bash
python3 -m pytest \
  compute/tests/test_cfg25_adversarial_consistency.py \
  compute/tests/test_cfg25_e1_chiral_lift.py \
  compute/tests/test_qg_from_fh_3d_6d.py -q
```

Result:

```text
248 passed in 3.84s
```

Interpretation: the tests support the repo discipline that `d=3`
specializes to `E_1` rather than native braided `E_2`, that CFG-style
ordinary CE is only a topological shadow, and that local formal/toric
witnesses behave as claimed.  They do not prove the general compact
CY3 chain-level `S^3` framing theorem.

## Final Status Recommendation

Use the following status language:

```text
Conditional, object-level.  For a smooth proper cyclic A_infinity CY3
category with negative-cyclic CY class, a chosen compatible S^3
framing / TCFT cancellation witness, and a CY3 Dolbeault target, the
chain-level construction gives a native holomorphic E_3 factorization
algebra PhiFA_3.  Its curve specialization is E_1-chiral.  CFG 2026
identifies a filtered E_3 locally constant Chern--Simons shadow whose
classical ball model is C^*(g); this is not the CY3 Dolbeault/chiral
CE object and is not a substitute for the cyclic A_infinity input.
```

Do not state:

```text
CFG proves PhiFA_3(C)=C^*(g).
```

Do not state:

```text
A CY3 trace on HH_3(C) is enough.
```

Do not state:

```text
The S^3 framing is automatic for all compact CY3 categories because
pi_3(BU)=0.
```

The safe frontier is narrow but real: build the CY3 chain-level object
from negative cyclic CY data plus a verified `S^3`-framing/TQFT
cancellation witness, keep the Dolbeault/chiral CE variables visible,
and use CFG only for the locally constant associated `E_3` model.
