# Agent 13 -- Holomorphic Locality and Residues

Date: 2026-04-24.

Scope: adversarial audit of the many-variable chiral CE/OPE normal form for
the CY3 Stage-1 object. Focus: holomorphic jets in `z_1,z_2,z_3`,
multidirectional Grothendieck residues, partial diagonals, Dolbeault compact
supports, and the locally constant shadow. Report only. No chapter or compute
file was edited.

## Sources Read

- `CLAUDE.md`.
- `AGENTS.md`.
- `.agents/skills/vol3-beilinson-loop/SKILL.md`.
- `chapters/theory/cy3_chain_level_bridge.tex`.
- `chapters/theory/quantum_chiral_algebras.tex`.
- `chapters/theory/m3_b2_obstruction.tex`.
- `chapters/theory/cy_to_chiral.tex`.
- `compute/lib/chiral_ce_complex.py`.
- Neighbor report `notes/adversarial_swarm_20260424_hol_e3/agent_12_topological_e3_trace.md`.
- Bibliography anchors in `bibliography/references.tex`.

## Verification Run

```bash
PYTHONDONTWRITEBYTECODE=1 python3 compute/lib/chiral_ce_complex.py
```

Result: the finite CE shadow engine ran successfully. Witness values:

```text
heisenberg: genus_3_dim = 8, d_squared_zero = True
sl2:        genus_3_dim = 512, d_squared_zero = True
virasoro:   shadow_tower = {2: 1/2, 3: 2, 4: 10/27}
yangian:    genus_3_dim = 512, d_squared_zero = True
```

Interpretation: this verifies finite exterior CE algebra and shadow-tower
bookkeeping in `compute/lib/chiral_ce_complex.py`; it does not verify the full
Dolbeault--jet, many-variable, continuous chiral CE object of the CY3 local
normal form.

## Local Anchors

- `chapters/theory/cy3_chain_level_bridge.tex:101-176`: definition of the
  many-variable chiral CE model on a holomorphic polydisc.
- `chapters/theory/cy3_chain_level_bridge.tex:145-160`: factorisation
  products over disjoint holomorphic polydiscs, polar support on partial
  diagonals, coordinate Laurent normal form, and Grothendieck residue sentence.
- `chapters/theory/cy3_chain_level_bridge.tex:161-175`: ordinary
  `C^\bullet(\mathfrak g)` appears only after the locally constant shadow.
- `chapters/theory/cy3_chain_level_bridge.tex:203-240`: Hall-valued
  factorisation-cosheaf target and the requirement that maps live on the full
  Cech/Ran nerve.
- `chapters/theory/cy3_chain_level_bridge.tex:305-340`: local-to-toric
  descent is conditional on the full comparison map, not a list of chartwise
  quasi-isomorphisms.
- `chapters/theory/cy3_chain_level_bridge.tex:651-686`: Stage-1 envelope
  claims the holomorphic local normal form is Definition
  `def:cy3-many-variable-chiral-ce`.
- `chapters/theory/cy3_chain_level_bridge.tex:716-752`: CFG gives the
  topological grammar only after the locally constant shadow; it has no
  Dolbeault differential, holomorphic jets, or polydisc residues.
- `chapters/theory/quantum_chiral_algebras.tex:20-33`: hCS observables are
  stated as a conditional classical Dolbeault--chiral CE model; quantum
  observables require renormalisation and anomaly cancellation.
- `chapters/theory/quantum_chiral_algebras.tex:3809-3867`: Bochner--Martinelli
  propagator and OPE statement on `C^3`.
- `chapters/theory/m3_b2_obstruction.tex:1647-1690`: compactly supported
  Dolbeault cohomology enters the deformation tangent calculation.
- `chapters/theory/cy_to_chiral.tex:384-405`: CFG locally constant `E_3`
  model is not the CY3 Dolbeault object; the CY3 object keeps Dolbeault
  differential, holomorphic jets, and polydisc residues.
- `compute/lib/chiral_ce_complex.py:1-25`: finite strict Lie conformal CE
  model.
- `compute/lib/chiral_ce_complex.py:189-199`: one-variable lambda-bracket and
  one-variable residue convention.
- `compute/lib/chiral_ce_complex.py:223-234`: `zeroth_product` extracts only
  the `lambda^0` coefficient.
- `compute/lib/chiral_ce_complex.py:476-491`: finite exterior CE differential.
- `compute/lib/chiral_ce_complex.py:754-870`: `L_infinity` corrections are
  represented in a finite exterior/tensor warning model, not as the completed
  Dolbeault--jet bar object.
- `compute/lib/chiral_ce_complex.py:1094-1124`: finite genus-3 `E_3` bar
  dimension comparison.

## Verdict

The manuscript now has the correct high-level type: the CY3 local object is a
completed Dolbeault--chiral CE/factorisation algebra over holomorphic jets on
polydiscs, and ordinary `C^\bullet(\mathfrak g)` is only a locally constant
shadow.

The weak point is definitional precision around residues. The displayed
many-variable OPE normal form is usable as a local coordinate expression, but
the exact operation must be stated as a residue in local cohomology along the
diagonal, with a fixed product-torus orientation, a multi-index lambda
convention, support/continuous-dual topology, and a named shadow functor. The
compute engine is a finite shadow oracle; it must not be cited as evidence for
coordinate independence, multidirectional residues, Dolbeault compact-support
continuity, or partial-diagonal associativity.

## ATTACK -> HEAL Cycles

### Cycle 1 -- Coordinate Laurent Formula Without a Residue Definition

ATTACK. Read the displayed normal form

```tex
a(z)b(w)\sim
\sum_{\alpha\in\mathbb N^3}
\frac{(a_{(\alpha)}b)(w)}
{(z_1-w_1)^{\alpha_1+1}
 (z_2-w_2)^{\alpha_2+1}
 (z_3-w_3)^{\alpha_3+1}}
```

at `cy3_chain_level_bridge.tex:149-155` as an actual OPE operation before
the residue convention has been fixed.

FAILURE MODE. Fatal if cited as a theorem. In several complex variables,
there is no single contour residue around `z=w`; the operation is a
Grothendieck/local-cohomology residue in the three normal directions to the
diagonal. The phrase "small product torus" at line 158 is the right idea but
not yet enough: orientation, order, independence of radii, coordinate
trivialisation by `Omega_X`, and exclusion of other partial diagonals must be
part of the definition.

HEAL. Define the coefficient first, then display the Laurent normal form.
For `P subset X` with local CY coordinate trivialisation
`Omega_X = u(z) dz_1 wedge dz_2 wedge dz_3`, and for a kernel with polar
support on the diagonal, set

```tex
\[
  a_{(\alpha)}b(w)
  :=
  \operatorname{Res}^{\Omega_X}_{\Delta,\alpha}(a(z)b(w))
  =
  \frac{1}{(2\pi i)^3}
  \int_{|z_i-w_i|=\varepsilon_i}
  (z-w)^\alpha\,a(z)b(w)\,
  dz_1\wedge dz_2\wedge dz_3 .
\]
```

The product torus is oriented by
`d arg(z_1-w_1) wedge d arg(z_2-w_2) wedge d arg(z_3-w_3)`, with
`0 < epsilon_3 << epsilon_2 << epsilon_1` only when an iterated-residue
order is required by a chosen partial-diagonal nesting. For the full binary
diagonal, the class is independent of small radii as long as the torus stays
inside `P^2 \setminus (other polar strata)`. Under coordinate change, the
Jacobian is absorbed by the chosen CY volume form.

Patch text:

```tex
The coefficient \(a_{(\alpha)}b\) is not defined by a one-dimensional
contour. It is the Grothendieck residue of the diagonal local-cohomology
class in the three normal directions to \(\Delta\subset P\times P\):
\[
  a_{(\alpha)}b(w)=
  \frac{1}{(2\pi i)^3}
  \int_{|z_i-w_i|=\varepsilon_i}
  (z-w)^\alpha a(z)b(w)\,
  dz_1\wedge dz_2\wedge dz_3 .
\]
The orientation is the product orientation in the order
\((z_1,z_2,z_3)\), and the Calabi--Yau volume form
\(\Omega_X\) makes the definition invariant under holomorphic coordinate
change. The Laurent display is the coordinate representative of this
local-cohomology residue class.
```

Manuscript implication: add this immediately after
`cy3_chain_level_bridge.tex:157-160`. Without it, all later "residue/OPE"
formulae remain normal-form slogans rather than defined operations.

Status recommendation: `ClaimStatusDefinitional` after this definition is
inserted; otherwise only `ClaimStatusHeuristicNormalForm`.

### Cycle 2 -- Pairwise OPE Does Not Define All Partial-Diagonal Singularities

ATTACK. Treat the binary OPE at `cy3_chain_level_bridge.tex:149-155` as if it
already defines the factorisation product for arbitrary configurations in
`P^n`.

FAILURE MODE. Fatal for associativity. In `n` variables, singular support
lives on the full union of partial diagonals

```tex
\Delta_\pi=\{z_i=z_j \text{ whenever } i,j \text{ lie in the same block of }\pi\}
\subset P^n,
```

not only on one pairwise diagonal. Binary residues do not by themselves fix
the compatibility of nested collisions, signs, or the order in which
different blocks collapse. This is exactly where the Fulton--MacPherson/Ran
boundary and Cech/Ran nerve in `cy3_chain_level_bridge.tex:203-240` become
load-bearing.

HEAL. Define factorisation products as sections or distributions on
`P^n \setminus \Delta_{\mathrm{big}}` with polar support on the union of
partial diagonals, and define collision maps by local cohomology residues
along a partition refinement. For a refinement `pi <= rho`, use normal
coordinates `u_e = z_i-z_j` for a spanning forest of each collapsing block and
write

```tex
\[
  \operatorname{Res}_{\rho/\pi}:
  H^\bullet_{\Delta_\rho}(P^n,\mathcal F^{\boxtimes n})
  \longrightarrow
  H^{\bullet-3(|\rho|-|\pi|)}_{\Delta_\pi}
  (P^n,\mathcal F^{\boxtimes |\pi|}).
\]
```

The associativity condition is the equality of iterated residues
`Res_{sigma/pi} = Res_{rho/pi} Res_{sigma/rho}` for refinements
`pi <= rho <= sigma`, with the Fulton--MacPherson boundary orientation
fixing the Koszul sign.

Patch text:

```tex
For \(n\) insertions the polar support is the union of partial diagonals
\(\Delta_\pi\subset P^n\). A collision operation is the local-cohomology
residue along a refinement of partitions; binary OPE is the special case
\(|\pi|=n-1\). The factorisation associativity condition is the equality
of iterated residues for nested refinements of partitions, with signs fixed
by the Fulton--MacPherson boundary orientation.
```

Manuscript implication: strengthen `cy3_chain_level_bridge.tex:145-160`.
The Hall-valued cosheaf definition at lines 203-240 is already compatible
with this; the normal-form definition should explicitly say that binary OPE
is only the local generator of the full partial-diagonal calculus.

Status recommendation: factorisation associativity remains `Conditional` at
the hCS/Hall comparison level, but the local residue grammar can be
`Definitional`.

### Cycle 3 -- Compact Supports and Continuous Duals Are Not Optional

ATTACK. Replace

```tex
\mathfrak L_\cC(P)=
\Omega_c^{0,\bullet}
(P,J^\infty_{\mathrm{hol}}\mathfrak l_\cC)[1]
```

by an uncompleted finite-dimensional Lie algebra and read
`C^\bullet_{\mathrm{Lie,cont}}` at `cy3_chain_level_bridge.tex:127-131`
as ordinary algebraic CE cochains.

FAILURE MODE. Fatal for locality. Compact supports are what make extension
by zero define factorisation products for disjoint polydiscs. Continuous
duals are what make observables on infinite-dimensional Dolbeault--jet fields
well-defined. Algebraic duals are too large and destroy descent; finite CE
cochains forget the holomorphic jet topology and all compact-support
variance.

HEAL. State the topology in the definition. Let

```tex
\[
\mathfrak L_{\cC,c}(P)
=\Omega_c^{0,\bullet}(P,J^\infty_{\mathrm{hol}}\mathfrak l_\cC)[1]
\]
```

be the usual LF nuclear Dolbeault space of compactly supported smooth forms
with holomorphic-jet coefficients. Define

```tex
\[
C^\bullet_{\mathrm{Lie,cont}}(\mathfrak L_{\cC,c}(P),\mathbb C)
=
\widehat{\mathrm{Sym}}
\bigl((\mathfrak L_{\cC,c}(P))^\vee_{\mathrm{cont}}[-1]\bigr),
\]
```

using the strong continuous dual and the completed symmetric algebra. For
disjoint `P_i subset P`, the product is dual to extension by zero:

```tex
\[
\bigoplus_i \mathfrak L_{\cC,c}(P_i)\longrightarrow
\mathfrak L_{\cC,c}(P).
\]
```

Patch text:

```tex
The subscript \(c\) and the word \(\mathrm{cont}\) are part of the
structure. The local Lie algebra is an LF nuclear Dolbeault space of
compactly supported fields with holomorphic-jet coefficients; observables
use its strong continuous dual and completed symmetric algebra. The
factorisation product for disjoint holomorphic polydiscs is dual to
extension by zero on compactly supported fields.
```

Manuscript implication: insert after `cy3_chain_level_bridge.tex:127-131`.
The current formula is correct but too compressed for theorem-grade use.

Status recommendation: `Definitional`; any theorem using algebraic duals or
ordinary finite CE at this point should be downgraded to the locally constant
shadow.

### Cycle 4 -- Bochner--Martinelli Kernel Misread as a Meromorphic OPE

ATTACK. Read

```tex
\cA(z)\cA(w) \sim \hbar P_{\mathrm{BM}}(z,w)\cdot \mathbf 1
```

at `quantum_chiral_algebras.tex:3826-3828` as a meromorphic Laurent OPE in
the Beilinson--Drinfeld sense.

FAILURE MODE. Fatal if used directly in a chiral algebra calculation. The
Bochner--Martinelli kernel is a Dolbeault propagator on
`C^3 \setminus Delta`; it contains anti-holomorphic numerator data and
represents the diagonal class by the equation
`\bar\partial P_{\mathrm{BM}}=\delta_\Delta`
(`quantum_chiral_algebras.tex:3841-3852`). It is not itself the meromorphic
three-variable Laurent coefficient system of the chiral CE normal form. The
meromorphic OPE appears only after passing to diagonal local cohomology,
choosing a holomorphic representative or equivariant reduction, and applying
the residue map of Cycle 1.

HEAL. State this as a contraction kernel, not as a finished chiral OPE.

Patch text:

```tex
The symbol \(\sim\) here denotes the Costello--Gwilliam Wick contraction
kernel in the Dolbeault BV factorisation algebra. The
Bochner--Martinelli form represents the diagonal local-cohomology class
because \(\bar\partial P_{\mathrm{BM}}=\delta_\Delta\). Its chiral OPE
normal form is obtained only after applying the diagonal residue map of
Definition~\ref{def:cy3-many-variable-chiral-ce} and choosing a
meromorphic local representative.
```

Manuscript implication: add this after `quantum_chiral_algebras.tex:3826-3838`
or cross-reference the strengthened residue definition in the CY3 bridge.
This prevents the BM kernel from being conflated with the BD chiral OPE.

Status recommendation: the BM propagator statement is `ProvedElsewhere` by
Costello--Gwilliam/Costello--Li; the extracted meromorphic OPE coefficients
are `Definitional/Conditional` on the chosen local-cohomology representative.

### Cycle 5 -- Multi-Index Lambda Bracket and Factorial Convention Missing

ATTACK. Import the one-variable convention of
`compute/lib/chiral_ce_complex.py:189-199`

```python
{a_lambda b} = sum_{n>=0} (a_{(n)} b) * lambda^n / n!
```

into the CY3 many-variable OPE without saying whether the multi-index
convention is
`\lambda^\alpha` or `\lambda^\alpha/\alpha!`.

FAILURE MODE. Moderate-to-fatal for formula comparison. A multi-directional
lambda bracket must choose

```tex
\lambda^\alpha/\alpha!
\quad\text{with}\quad
\alpha!=\alpha_1!\alpha_2!\alpha_3!
```

or absorb factorials into the definition of `a_{(\alpha)}b`. Without this,
the same Laurent coefficient gives different lambda-bracket structure
constants, and comparisons with `compute/lib/chiral_ce_complex.py` are off by
multi-factorials.

HEAL. Fix the convention at the same point as the residue definition:

```tex
\[
\{a_{\boldsymbol\lambda}b\}_{(3)}
=
\sum_{\alpha\in\mathbb N^3}
\frac{\boldsymbol\lambda^\alpha}{\alpha!}\,
(a_{(\alpha)}b),
\qquad
\boldsymbol\lambda^\alpha=\lambda_1^{\alpha_1}
\lambda_2^{\alpha_2}\lambda_3^{\alpha_3}.
\]
```

Here `a_{(\alpha)}b` is the Grothendieck-residue coefficient of Cycle 1.
If the manuscript wants the no-factorial convention, it must say so and the
compute comparison must insert the factorial conversion.

Patch text:

```tex
We use the factorial lambda convention
\(\{a_{\boldsymbol\lambda}b\}_{(3)}
=\sum_{\alpha}\boldsymbol\lambda^\alpha(a_{(\alpha)}b)/\alpha!\).
Thus the residue coefficient \(a_{(\alpha)}b\) agrees with the coefficient
of \((z-w)^{-\alpha-\mathbf 1}\) in the Laurent normal form, while the
generating lambda bracket carries the usual multi-index factorial.
```

Manuscript implication: add after the residue definition. This also gives a
precise bridge to the one-variable compute file.

Status recommendation: `Definitional`.

### Cycle 6 -- Locally Constant Shadow Is Not a Dolbeault Quasi-Isomorphism

ATTACK. Read the shadow line

```tex
\Omega^{0,\bullet}(P)\simeq \mathbb C
```

at `cy3_chain_level_bridge.tex:165` as a quasi-isomorphism of the actual
Dolbeault complex used in the local model.

FAILURE MODE. Fatal for compact supports and jets. On a Stein polydisc,
ordinary Dolbeault cohomology has holomorphic functions in degree `0`, not
canonically only constants. With compact supports, top Dolbeault cohomology
is Serre-dual to holomorphic functions and is again not the finite algebra
`C`. The displayed arrow is therefore not a quasi-isomorphism of the CY3
local object; it is a separate locally constant/constant-mode shadow functor.

HEAL. Name the functor and state what it forgets:

```tex
\[
\operatorname{Sh}_{\mathrm{lc},x}:
\Omega_c^{0,\bullet}
(P,J^\infty_{\mathrm{hol}}\mathfrak l_\cC)[1]
\longrightarrow
H^\bullet(\mathfrak l_{\cC,x})
\]
```

It is obtained by forgetting compact-support variance, passing to the
topological locally constant model, evaluating holomorphic functions and
jets at the chosen point `x`, and discarding positive jet modes. It is not a
canonical equivalence of Dolbeault factorisation algebras.

Patch text:

```tex
The arrows in the locally constant shadow are not quasi-isomorphisms of the
Dolbeault compact-support complex. They denote the shadow functor
\(\operatorname{Sh}_{\mathrm{lc},x}\): forget compact-support variance,
project to the constant topological mode, evaluate holomorphic jets at
\(x\), and discard positive jet modes. Only after this functor is applied
does the local object reduce to \(C^\bullet(H^\bullet(\mathfrak l_{\cC,x}))\);
in a constant hCS chart this is \(C^\bullet(\mathfrak g)\).
```

Manuscript implication: replace or qualify `cy3_chain_level_bridge.tex:161-175`.
The current wording is directionally correct but too close to a false
Dolbeault quasi-isomorphism.

Status recommendation: shadow statement becomes `Definitional`; any proof
using it as a quasi-isomorphism of the full local model is invalid.

### Cycle 7 -- Compute Engine Over-Advertised as Chiral CE/OPE Normal Form

ATTACK. Use `compute/lib/chiral_ce_complex.py` as evidence for the full
many-variable chiral CE/OPE normal form.

FAILURE MODE. Fatal if cited as verification of holomorphic locality. The
compute file has:

- one-variable lambda brackets (`compute/lib/chiral_ce_complex.py:189-199`);
- `zeroth_product` extracting only the `lambda^0` term
  (`compute/lib/chiral_ce_complex.py:223-234`);
- finite exterior CE chains (`compute/lib/chiral_ce_complex.py:476-491`);
- finite genus-3 dimension comparisons (`compute/lib/chiral_ce_complex.py:1094-1124`).

It has no Dolbeault complex, no compact supports, no holomorphic jets, no
multi-index lambda variables, no product-torus residues, no local cohomology
along partial diagonals, no continuous dual topology, and no Cech/Ran descent.

HEAL. Treat it as the locally constant shadow oracle:

```tex
\[
\operatorname{Sh}_{\mathrm{lc},x}
\left(
\mathrm{CE}^{\mathrm{ch},E_3}_{*,\mathrm{cont}}
(\mathfrak L_\cC(P))
\right)
\simeq
\mathrm{CE}_*
\left(H^\bullet(\mathfrak l_{\cC,x})\right),
\]
```

with the additional restriction that the current Python implementation models
strict finite Lie conformal examples and selected `L_\infty` shadow
coefficients.

Patch text for the manuscript:

```tex
The finite CE computations in
\texttt{compute/lib/chiral\_ce\_complex.py} verify the locally constant
shadow of this definition: strict one-variable lambda brackets, finite
exterior CE chains, and selected \(L_\infty\) shadow coefficients. They do
not construct the Dolbeault--jet factorisation algebra, the
multi-directional Grothendieck residue operations, or the Cech/Ran descent
data.
```

Patch text for the compute docstring if/when compute edits are allowed:

```python
SHADOW SCOPE
============
This module is a finite locally constant shadow of the CY3
Dolbeault--chiral CE model. It does not model holomorphic jets in
z1,z2,z3, compact supports, product-torus Grothendieck residues, partial
diagonal local cohomology, or Cech/Ran descent.
```

Manuscript implication: any theorem citing this compute file must say
`Computed(lc shadow)` or `Computed(finite CE model)`, not
`Computed(full CY3 chiral CE/OPE normal form)`.

Status recommendation: compute evidence is `Computed(lc shadow)` only.

## Exact Manuscript Implications

1. Strengthen `def:cy3-many-variable-chiral-ce` after
   `cy3_chain_level_bridge.tex:157-160` with the product-torus
   Grothendieck residue definition, orientation, CY-volume coordinate
   invariance, and multi-index lambda convention.

2. Qualify `cy3_chain_level_bridge.tex:145-160`: binary OPE is the local
   generator of a partial-diagonal local-cohomology calculus on `P^n`, not
   the whole factorisation product by itself.

3. Add topology after `cy3_chain_level_bridge.tex:127-131`: the CE algebra is
   completed and continuous; compact support is used for extension-by-zero
   factorisation products.

4. Replace the locally constant shadow display at
   `cy3_chain_level_bridge.tex:161-175` by a named shadow functor
   `Sh_{lc,x}`. Do not write it as a Dolbeault quasi-isomorphism.

5. In `quantum_chiral_algebras.tex:3826-3838`, say that
   `P_BM` is the Dolbeault BV contraction kernel representing the diagonal
   local-cohomology class, not the final meromorphic Laurent OPE until the
   residue map is applied.

6. When citing `compute/lib/chiral_ce_complex.py`, label the evidence as
   finite locally constant shadow evidence. The script run in this pass
   confirms the finite CE values but supplies no holomorphic-locality or
   residue theorem.

## Primary Source Anchors Already Present Locally

- Beilinson--Drinfeld, `Chiral Algebras` (2004):
  `bibliography/references.tex:30-31`.
- Costello--Gwilliam, `Factorization Algebras in Quantum Field Theory`,
  Vols. 1-2: `bibliography/references.tex:90-91`.
- Costello--Li holomorphic/local Lie algebra and anomaly references:
  `bibliography/references.tex:412-416`; cited in the target chapter at
  `cy3_chain_level_bridge.tex:351-352` and `cy3_chain_level_bridge.tex:677-681`.
- CFG 2026 topological CS comparison:
  `bibliography/references.tex:726`; used in
  `cy3_chain_level_bridge.tex:716-752`.
- Bochner--Martinelli local representative:
  `quantum_chiral_algebras.tex:3841-3852` cites Range 1986 and
  Costello--Li regularisation.

Primary-source gap to patch later: `cy3_chain_level_bridge.tex:157` names
Grothendieck residues, but the local bibliography search found no explicit
residue/local-cohomology source anchor. Add one before relying on the
multi-residue definition in a theorem proof.

## Final Status Grid

| Object / claim | Exact status |
|---|---|
| Many-variable local object `L_c(P)` | Definitional as compactly supported Dolbeault holomorphic-jet dg Lie algebra. |
| Binary OPE Laurent display | Coordinate normal form; theorem-grade only after product-torus Grothendieck residue definition. |
| Partial-diagonal factorisation products | Need local-cohomology residue compatibility for partition refinements; currently implicit. |
| Bochner--Martinelli OPE | Dolbeault BV contraction kernel; not a meromorphic OPE until local-cohomology residue extraction. |
| Locally constant `C^\bullet(g)` | Shadow functor output only; not a Dolbeault quasi-isomorphism of the full local model. |
| `compute/lib/chiral_ce_complex.py` | Computed finite locally constant CE shadow; not full CY3 Dolbeault--chiral CE. |
| hCS-to-Hall comparison | Still open/conditional as in Problem `op:cy3-hcs-hall-comparison`. |

## Files Changed

- `notes/adversarial_swarm_20260424_hol_e3/agent_13_holomorphic_locality_residues.md`.

No chapters or compute files were edited.
