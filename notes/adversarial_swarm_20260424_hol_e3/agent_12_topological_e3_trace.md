# Agent 12 -- Topological E3 Trace

Date: 2026-04-24.

Scope: adversarial audit of `B_{E_3}`, `CE^{ch,E_3}_*`, Verdier duality,
factorization-homology traces, and the class `M` higher-genus `E_3` bar
claim. Report only. No chapter or compute file was edited.

## Sources read

- `CLAUDE.md`.
- `AGENTS.md`.
- `.agents/skills/vol3-beilinson-loop/SKILL.md`.
- `.agents/skills/vol3-claim-verification/SKILL.md`.
- `.agents/skills/vol3-build-surface/SKILL.md`.
- `chapters/theory/cy3_chain_level_bridge.tex`.
- `chapters/theory/e2_chiral_algebras.tex`.
- `compute/lib/e3_bar_higher_genus_class_m.py`.
- `compute/tests/test_e3_bar_higher_genus_class_m.py`.
- Neighbor reports in `notes/adversarial_swarm_20260424_hol_e3/`, especially
  Agent 06 on the CFG/topological CS comparison.

## Verification run

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider \
  compute/tests/test_e3_bar_higher_genus_class_m.py
```

Result: `170 passed in 2.64s`.

Direct witness values:

```text
g=1: e4_total=6, e4_is_einf=True, first_higher=None, d5_maps=[]
g=2: e4_total=36, e4_is_einf=True, first_higher=None, d5_maps=[]
g=3: e4_total=216, e4_is_einf=True, first_higher=None, d5_maps=[]
g=4: e4_total=1296, e4_is_einf=False, first_higher=5, d5_maps=[(8, 4)]
g=5: e4_total=7776, e4_is_einf=False, first_higher=5, d5_maps=[(9, 5), (10, 6)]
```

## Local anchors

- `chapters/theory/cy3_chain_level_bridge.tex:101-144`: many-variable
  Dolbeault--chiral CE model and
  `B_{E_3}(\PhiFA_3(\cC)|_P) \simeq CE^{ch,E_3}_*(\mathfrak L_\cC)` on
  the hCS-realized locus.
- `chapters/theory/cy3_chain_level_bridge.tex:360-376`: CFG supplies
  real topological CS factorization-homology traces, not the CY3
  hCS-to-Hall comparison.
- `chapters/theory/cy3_chain_level_bridge.tex:632-643`: ordinary
  `C^\bullet(\mathfrak g)` appears only after the locally constant shadow.
- `chapters/theory/e2_chiral_algebras.tex:806-811`: at `d=3`, the final
  chiral algebra is `E_1`, while the `E_2` braided equivalence is induced
  on the Drinfeld center.
- `chapters/theory/e2_chiral_algebras.tex:1965-2013`: Verdier spectral
  functor is marked `ClaimStatusProvedHere`, but its proof uses finite
  linear duality.
- `chapters/theory/e2_chiral_algebras.tex:2102-2124`: class `M` says
  `dim E_\infty = 6^g` and then immediately admits possible higher
  differentials for `g >= 4`.
- `compute/lib/e3_bar_higher_genus_class_m.py:1-67`: top docstring
  advertises `E_4 = E_inf = (3t(1+t))^g`, then later restricts equality
  to `g <= 3`.
- `compute/lib/e3_bar_higher_genus_class_m.py:296-310`: `einf_*` methods
  return `E_4` with caveats.
- `compute/lib/e3_bar_higher_genus_class_m.py:453-458`: standalone
  `class_m_einf_dimension(g)` returns `6^g` while docstring says
  conjectural for `g >= 4`.
- `compute/tests/test_e3_bar_higher_genus_class_m.py:1-22`: test
  docstring has the correct `g >= 4` caveat.
- `compute/tests/test_e3_bar_higher_genus_class_m.py:237-243`: test class
  still names the all-genus closed form as `dim E_inf = 6^g`.
- `compute/tests/test_e3_bar_higher_genus_class_m.py:365-380`: tests
  detect the first possible `d_5` at `g=4` and termination at `E_{g+2}`.

## Verdict

The local `E_3` bar envelope is correctly typed only as a conditional
Stage-1 / hCS-realized construction. The trace theorem is not chain-level
proved for the CY3 holomorphic object. CFG proves a real topological CS
factorization-homology trace statement; it does not prove CY3
Dolbeault--chiral CE traces, hCS-to-Hall traces, or orientation-compatible
critical CoHA traces.

The class `M` higher-genus computation proves

```tex
E_4(B_{E_3}) = (3t(1+t))^g,\qquad \dim E_4 = 6^g
```

as the Kunneth closed form. The current tests compare this closed form
with the explicit matrix-rank computation for `g=1,2,3`. It proves

```tex
E_\infty = E_4,\qquad \dim E_\infty = 6^g
```

only for `g <= 3`. For `g >= 4`, the exact status is

```tex
\dim E_\infty \leq 6^g,
```

with `d_5` first possible at `g=4`. Any all-genus `E_\infty=6^g` statement
is not chain-level proved by the current manuscript or compute surface.

## ATTACK -> HEAL cycles

### Cycle 1 -- `B_{E_3}` on the final `E_1` chiral algebra

ATTACK. Read `B_{E_3}(A)` in
`e2_chiral_algebras.tex:808-810` as the ordinary bar construction of the
final specialized chiral algebra
`A=\Phi_3^{(\Sigma_2,C)}(\cC)`, even though that algebra is explicitly
`E_1` at `d=3`.

FAILURE MODE. An `E_1` algebra does not by itself determine an `E_3` bar
complex. The extra input is the retained CY3 `S^3`/Stage-1 framing data.
The local model in `cy3_chain_level_bridge.tex:132-144` applies to
`\PhiFA_3(\cC)|_P`, not to a bare specialized curve algebra with the
Stage-1 memory forgotten.

HEAL. Write the `E_3` bar with its datum:

```tex
B_{E_3,F,\eta}\!\left(\PhiFA_3(\cC)\right)
\quad\text{or}\quad
B_{E_3,F,\eta}(A)
```

where `F` is the chosen `E_3` formality/framing datum and `\eta` is the
CY3 trace/framing class retained through specialization. The unadorned
`B_{E_3}(A)` is safe only after a sentence says that `A` is considered
together with this retained Stage-1 CY3 structure.

Patch text:

```tex
At \(d=3\), \(A=\Phi_3^{(\Sigma_2,C)}(\cC)\) is an \(E_1\)-chiral algebra.
The notation \(B_{E_3}(A)\) means the \(E_3\)-bar construction of the
retained Stage-\(1\) CY$_3$ factorisation datum
\((\PhiFA_3(\cC)_F,\eta)\) before the curve specialisation forgets it.
Without this datum the specialised \(E_1\)-algebra has only its ordinary
\(E_1\)-bar complex.
```

Status: `ClaimStatusConditional` unless the retained framing datum is
included in the hypotheses; `ClaimStatusDefinitional` after the notation
is explicitly defined.

### Cycle 2 -- `CE^{ch,E_3}_*` as an ordinary finite CE complex

ATTACK. Treat
`CE^{ch,E_3}_*(\mathfrak L_\cC)` as ordinary
`C^\bullet(\mathfrak g)` or a finite exterior CE complex.

FAILURE MODE. The local object is
`\Omega_c^{0,\bullet}(P,J^\infty_{\mathrm{hol}}\mathfrak l_\cC)[1]`
with continuous duals, completed symmetric algebra, Dolbeault
differential, holomorphic jets, compact supports, and multidirectional
residues. `cy3_chain_level_bridge.tex:640-643` explicitly says ordinary
`C^\bullet(\mathfrak g)` appears only after the locally constant shadow.
The compute file is a finite `d_4` page oracle for the shadow, not a
construction of the completed Dolbeault--chiral CE trace object.

HEAL. Keep three layers:

```tex
\mathrm{CE}^{\mathrm{ch},E_3}_{*,\mathrm{cont}}
\bigl(\Omega_c^{0,\bullet}(P,J^\infty_{\mathrm{hol}}\mathfrak l_\cC)[1]\bigr)
\quad\longrightarrow\quad
C^\bullet(\mathfrak g)
\quad\longrightarrow\quad
\Lambda^\bullet(\kk^{3g}).
```

The first is the CY3 local object; the second is the locally constant
shadow; the third is the finite bar-page compute model.

Patch text:

```tex
The symbol
\(\mathrm{CE}^{\mathrm{ch},E_3}_*(\mathfrak L_\cC)\) denotes the completed
continuous chiral CE chains of the Dolbeault--jet local Lie algebra
\(\mathfrak L_\cC(P)\).  The finite exterior algebra
\(\Lambda^\bullet(\kk^{3g})\) used in the class-\(\mathbf M\) computation
is the associated locally constant \(d_4\)-page shadow; it is not the
full Dolbeault--chiral CE complex.
```

Status: local definitional formula survives; finite compute evidence is
`Computed(E_4 shadow)`, not `ProvedHere(full CE trace)`.

### Cycle 3 -- Factorization-homology traces

ATTACK. Use CFG factorization-homology traces for real 3d CS to declare
CY3 hCS trace formulas chain-level proved.

FAILURE MODE. `cy3_chain_level_bridge.tex:360-376` already blocks this:
CFG constructs a filtered `E_3` algebra for ordinary real 3d
Chern--Simons and recovers Reshetikhin--Turaev link invariants by
factorization-homology traces. The CY3 hCS avatar remembers holomorphic
jets, Dolbeault data, polydisc factorization, and multidirectional
residues. CFG does not construct the oriented hCS-to-Hall comparison,
critical CoHA orientation data, charge/HN completions, or BKM/DT trace
map.

HEAL. Split the trace statements:

```tex
\int_M A_{\lambda}^{\mathrm{top}}
\quad\text{(CFG real topological CS, proved elsewhere)}
```

versus

```tex
\int_X^{\mathrm{hol}}
\Obs_{\hCS}^{q}
\longrightarrow
\int_X^{\Hall}
\CoHA_{\mathrm{crit}}^{\mathrm{or}}
\quad\text{(CY3 hCS/Hall trace, open or conditional).}
```

Patch text:

```tex
The factorisation-homology trace theorem used here has two statuses.
For ordinary real \(3\)-dimensional Chern--Simons, CFG proves that the
filtered \(E_3\)-algebra \(A_\lambda\) and its perfect modules recover
Reshetikhin--Turaev traces. For the CY$_3$ holomorphic theory, this
supplies only the topological grammar. A CY$_3$ trace formula requires
the separate oriented comparison
\[
  \Theta_{\hCS\to\Hall}^{or}:
  \Obs_{\hCS}^{q}\to\CoHA_{\mathrm{crit}}^{or}
\]
as a morphism of completed factorisation cosheaves, including support,
orientation, Tate-twist, and Thom--Sebastiani compatibilities.
```

Status: CFG trace `ProvedElsewhere`; CY3 hCS/Hall trace
`ClaimStatusConditional/Open`.

### Cycle 4 -- Verdier duality on the continuous `E_3` trace complex

ATTACK. Treat Theorem `thm:verdier-spectral-functor` as a proved
Verdier-duality theorem for the continuous Dolbeault--chiral CE
`E_3` trace object.

FAILURE MODE. The proof at `e2_chiral_algebras.tex:1985-2013` uses
finite-dimensional linear duality on graded vector spaces. It does not
prove Verdier duality for completed nuclear/locally convex CE complexes,
compact-support variance, continuous duals, filtration completeness,
pagewise convergence, or compatibility with the full Dolbeault--jet
`E_3` structure. It also compresses the braiding reversal to
Shapovalov transposition without a trace-level proof that the completed
factorization-homology trace pairing is transported.

HEAL. Split the theorem into a finite algebraic lemma and a conditional
continuous theorem.

Patch text:

```tex
\begin{lemma}[Finite Verdier spectral duality]
\ClaimStatusProvedHere{}
Let \(B\) be a finite-dimensional conilpotent \(E_3\)-coalgebra
tricomplex with finite exhaustive filtration and differentials
continuous for the discrete topology. Linear duality sends the spectral
sequence of \(B\) to the spectral sequence of \(B^\vee\) page by page,
and preserves the page dimensions.
\end{lemma}

\begin{theorem}[Continuous Verdier spectral functor]
\ClaimStatusConditional{}
Let \(B\) be the completed Dolbeault--chiral \(E_3\)-bar coalgebra of a
CY$_3$ Stage-\(1\) object. Assume nuclearity, reflexivity for the chosen
continuous dual, strictness of the filtration, convergence of the
spectral sequence, and compatibility of Verdier duality with the
factorisation products and trace pairing. Then the finite Verdier
spectral duality lemma extends to \(B\), and the induced Drinfeld-centre
braiding is reversed by the Shapovalov transposition.
\end{theorem}
```

Status: finite toy/model statement `ProvedHere`; full continuous
Dolbeault trace statement `Conditional`, not presently chain-level
proved.

### Cycle 5 -- Class `M` claim `E_3` bar `= 6^g`

ATTACK. Read `dim E_\infty=6^g at genus g` in
`e2_chiral_algebras.tex:2105-2106` as an all-genus theorem.

FAILURE MODE. The same paragraph admits possible nonzero
`d_5,d_6,...` for `g >= 4`. The compute module and tests agree:
`E_4=(3t(1+t))^g` for all `g`, but `E_4=E_\infty` is proved by degree
reasons only for `g <= 3`. At `g=4`, `d_5:E_4^8 -> E_4^4` is possible;
at `g=5`, possible maps are `(9,5)` and `(10,6)`.

HEAL. Replace the all-genus `E_\infty` claim by the precise page claim.

Patch text:

```tex
\noindent\textbf{Class \(\mathbf M\)}:
the \(d_4\) differential from the quartic shadow \(S_4\ne0\) acts
nontrivially (Proposition~\ref{prop:virasoro-d4}).  For \(g\) independent
Virasoro copies the \(d_4\)-cohomology is
\[
  E_4(B_{E_3})=(3t(1+t))^g,\qquad \dim E_4=6^g.
\]
For \(g\leq3\), degree reasons force \(E_4=E_\infty\), hence
\(\dim E_\infty=6^g\).  For \(g\geq4\), the infinite class-\(\mathbf M\)
shadow tower can support higher differentials beginning with
\(d_5\), so the proved statement is only
\[
  \dim E_\infty\leq 6^g,
\]
with equality an additional computation or conjecture.
```

Status: `Computed/ProvedHere(E_4 all g; E_\infty for g <= 3)`;
`Open/Conjectural(E_\infty=6^g for g >= 4)`.

### Cycle 6 -- Compute API over-advertises `E_\infty`

ATTACK. Treat `class_m_einf_dimension(g)` and `einf_total()` as an
oracle for `E_\infty` at all genera.

FAILURE MODE. The functions return `6^g` for every `g`. Their docstrings
carry caveats, but the names are stronger than the mathematics. The
tests at `compute/tests/test_e3_bar_higher_genus_class_m.py:237-243`
also state "main result: dim E_inf = 6^g" while later tests correctly
detect `d_5` at `g=4`.

HEAL. Rename or guard the API so that all-genus calls return `E_4`, and
`E_\infty` is only returned as exact when `g <= 3`.

Patch text:

```python
def class_m_e4_dimension(g: int) -> int:
    """Total E_4 dimension for class M at genus g: 6^g."""
    return 6 ** g

def class_m_einf_dimension(g: int) -> int:
    """Exact E_inf dimension for class M.

    Exact only for g <= 3. For g >= 4 the current computation proves
    only the E_4 upper bound and possible higher differentials remain.
    """
    if g >= 4:
        raise ValueError("E_inf is not proved for class M at g >= 4; use class_m_e4_dimension")
    return 6 ** g
```

Patch text for the test heading:

```python
# 5. Closed form: dim E_4 = 6^g; E_inf only for g <= 3
class TestClosedForm:
    """The main result: E_4(class M, genus g) has total dimension 6^g."""
```

Status: current tests pass and are useful; function names/docstrings
should be tightened before citing the API as a theorem oracle.

## Final status grid

| Object / claim | Exact status |
|---|---|
| `B_{E_3}(\PhiFA_3(\cC)|_P)` | Conditional/definitional on the hCS-realized Stage-1 locus and chosen `E_3` formality/framing datum. |
| `B_{E_3}(A)` for final specialized `E_1` algebra | Not meaningful without retained Stage-1 CY3 datum; use decorated notation or restate the hypothesis. |
| `CE^{ch,E_3}_{*,cont}(\mathfrak L_\cC)` | Local Dolbeault--jet continuous object; not reduced to ordinary `C^\bullet(\mathfrak g)` except after locally constant shadow. |
| CFG factorization-homology traces | Proved elsewhere for real topological CS; not a CY3 hCS/Hall trace proof. |
| Verdier spectral functor | Proved only for finite algebraic spectral-sequence model as written; continuous Dolbeault trace version is conditional. |
| Class `M` `E_4=6^g` | Computed/proved by Kunneth; independently checked against matrix rank for `g=1,2,3`. |
| Class `M` `E_\infty=6^g` | Proved for `g <= 3`; open/conjectural for `g >= 4`. |
| Trace formulas chain-level proved? | No for the CY3 holomorphic trace/Hall trace. Yes only for the finite `d_4` page and the CFG real topological CS trace lane. |

## Files changed

- `notes/adversarial_swarm_20260424_hol_e3/agent_12_topological_e3_trace.md`.

No chapters or compute files were edited.
