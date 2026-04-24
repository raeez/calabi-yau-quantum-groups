# Agent A2: quantum BV-renormalised many-variable CE/bar and Hall comparison

Date: 2026-04-24.

Scope: issue 2 of the total-resolution swarm.  I attacked the current
CY3 many-variable CE/bar material, the Costello--Li/BV renormalisation
hypotheses, the quantum master equation, compact-support topologies, and
the Hall-valued target.  I made no manuscript or compute edits.

Owned file:

```text
notes/adversarial_swarm_20260424_total_resolution/agent_A2_quantum_ce_bar.md
```

## Verdict

The classical theorem now has the right type:

```tex
  \Obs^{\mathrm{cl}}_{\cC}(P)
  \simeq
  \left(
    B_{E_3}U^{\mathrm{fact},E_3}_P(\mathfrak L_{\cC})
  \right)^\vee_b .
```

It should not be promoted to the quantum BV-renormalised theorem by
adding `[[\hbar]]`.  The quantum source in the manuscript is

```tex
  \Obs_{\hCS}^{q}(U,\mathfrak g)
  =
  \left(
    \mathcal O(\cE_{\hCS,c}(U,\mathfrak g))[[\hbar]],
    Q_{\hCS}+\{I[L],-\}_{\BV}+\hbar\Delta_L
  \right),
```

with QME

```tex
  Q_{\hCS}I[L]
  +\frac12\{I[L],I[L]\}_{\BV}
  +\hbar\Delta_L I[L]=0 .
```

The current continuous CE/bar proposition does not construct the
renormalised effective action `I[L]`, does not identify the BV Laplacian
with a continuous coderivation of the completed `E_3` bar coalgebra, and
does not build a chain map to critical CoHA.  The strongest proof-grade
statement available now is a conditional quantum comparison theorem:
if an RG-compatible, anomaly-free Costello--Li quantisation and a
BV-to-`E_3`-bar transfer datum are supplied, then the quantum observables
are the strong continuous dual of a deformed completed `E_3` bar
coalgebra.  If, in addition, the oriented hCS-to-Hall comparison datum
of the adjacent lane is supplied, then the Hall comparison follows.

This is a real upgrade over the previous state: the obstruction is no
longer vague.  It is the absence of the continuous quantum coderivation

```tex
  D_B^\hbar = d_B+\sum_{r\geq 1}\hbar^r D_r
```

on the completed `E_3` bar coalgebra whose strong dual is

```tex
  Q_{\hCS}+\{I[L],-\}_{\BV}+\hbar\Delta_L .
```

## Red attack

### Attack 1: `Obs^q` is not `Obs^cl[[hbar]]`

The classical object at
`chapters/theory/cy3_chain_level_bridge.tex:101-214` is

```tex
  C^\bullet_{\mathrm{Lie,cont}}(\mathfrak L_{\cC}(P),\mathbb C).
```

The quantum object at
`chapters/theory/cy3_chain_level_bridge.tex:73-99` has a different
differential:

```tex
  Q_{\hCS}+\{I[L],-\}_{\BV}+\hbar\Delta_L .
```

The term `\hbar\Delta_L` is second order on functionals.  It is not the
dual of the classical CE differential, and it is not determined by the
Lie bracket alone.  A quantum CE/bar theorem needs a deformed bar
differential, not the classical bar differential tensored with
`[[\hbar]]`.

### Attack 2: the BV Laplacian is not defined on every continuous functional

The manuscript writes

```tex
  \mathcal O(\cE_{\hCS,c}(U,\mathfrak g))[[\hbar]]
```

but the Costello BV Laplacian is a renormalised operator on the chosen
space of local or multilocal functionals after heat-kernel regularisation
and counterterms.  It is not an everywhere-defined operator on the full
completed symmetric algebra of all continuous linear functionals on the
strict nuclear LF space.  A theorem must name the admissible subspace:
for example, local functionals completed by the Costello renormalisation
scheme, with wavefront/heat-kernel control sufficient for `\Delta_L`.

### Attack 3: strong dual exactness is being used at the edge of its range

The classical proposition uses strict nuclear LF spaces and strong
continuous duals at
`chapters/theory/cy3_chain_level_bridge.tex:216-289`.  That is the
right lane for classical compact-support CE cochains.  The quantum BV
operator introduces kernels supported on diagonals and distributions
coming from the propagator.  Strong duality is exact only in the
chosen strict nuclear subcategory and for strict morphisms; it does not
automatically commute with all renormalised distributional operations.
The quantum theorem must therefore add a strictness hypothesis:
all renormalised Feynman operations must be continuous maps between the
same strict nuclear LF/DFS completions.

### Attack 4: QME is an obstruction equation, not a decorative hypothesis

The QME at `cy3_chain_level_bridge.tex:87-96` is the equation that makes

```tex
  (Q_{\hCS}+\{I[L],-\}_{\BV}+\hbar\Delta_L)^2=0.
```

Equivalently, if a deformed bar differential exists, it must satisfy

```tex
  (D_B^\hbar)^2=0.
```

Writing `B_{E_3}` without constructing the higher `D_r` does not solve
QME.  At order `\hbar^n`, the obstruction is the cohomology class of

```tex
  [d_B,D_n]
  +\frac12\sum_{i+j=n}[D_i,D_j]
  -
  \left(T_L^\vee\right)^{-1}
    \bigl(\{I_n[L],-\}_{\BV}+\delta_{n,1}\Delta_L\bigr)
    T_L^\vee
```

in the continuous derivation complex of the completed bar coalgebra.
Here `T_L` is the missing BV-to-bar transfer map.  This formula is the
first honest receptacle for the quantum obstruction.

### Attack 5: the quartic Costello--Li anomaly is still a gate

The manuscript correctly records the local one-loop anomaly slot:

```tex
  P_4\in\Sym^4(\mathfrak g^\vee)^{\mathfrak g}
```

at `chapters/theory/cy3_chain_level_bridge.tex:458-487`, and warns at
`:489-498` that this quartic anomaly is not the `S_4` coefficient of the
`E_3` bar spectral sequence.  A quantum CE/bar theorem must explicitly
assume that this Costello--Li anomaly class vanishes or is killed by a
chosen counterterm.  Otherwise `Obs^q` does not exist as a differential
graded factorisation algebra, so there is no quantum bar theorem to
state.

### Attack 6: CFG is not the quantum CY3 theorem

The manuscript already fences CFG at
`chapters/theory/cy3_chain_level_bridge.tex:500-518` and
`:1035-1072`.  CFG proves the ordinary real 3d Chern--Simons
factorisation-envelope grammar.  It does not supply the CY3 Dolbeault
fields, holomorphic jets in `z_1,z_2,z_3`, compact-support LF topology,
Costello--Li holomorphic twist, critical-CoHA orientation data, or the
Hall target.  CFG can serve as a normal form for the `E_3` envelope and
configuration-space/QME grammar, not as a source theorem for this lane.

### Attack 7: Hall comparison is a separate chain map, not a consequence of CE/bar

The Hall target begins at
`chapters/theory/cy3_chain_level_bridge.tex:316-379`.  The open problem
at `:602-658` requires a continuous natural transformation

```tex
  \Theta_{\hCS\to\Hall}^{\mathrm{or}}\colon
  \Obs_{\hCS}^{q}(-,\mathfrak g)
  \longrightarrow
  \CoHA_{\mathrm{crit}}^{\mathrm{or}}(-)
```

on the whole DWR Cech/Ran nerve, preserving orientation, shifts, Tate
twists, completions, Thom--Sebastiani, and factorisation.  The CE/bar
theorem lives entirely on the source side.  Even a perfect quantum
CE/bar theorem would not by itself construct `\Theta`.

### Attack 8: the finite tests do not certify the analytic theorem

The passing tests verify finite CE/bar and Hall/Drinfeld shadows:

```text
compute/tests/test_chiral_ce_complex.py
compute/tests/test_dolbeault_cy3_homotopy.py
compute/tests/test_coha_drinfeld_bulk.py
```

They do not model continuous LF spaces, strong duals, heat-kernel
regularisation, QME counterterms, distributional BV Laplacians, or
vanishing-cycle Hall targets.  They are useful falsification oracles for
finite shadows, not proof of the quantum theorem.

## Surviving core

The following core survives the attacks.

1. Classical source:

```tex
  \Obs_{\cC}^{\mathrm{cl}}(P)
  \simeq
  \left(
    B_{E_3}U^{\mathrm{fact},E_3}_P(\mathfrak L_{\cC})
  \right)^\vee_b
```

on the Stage-1 verified locus, with strict nuclear LF topology and
strong continuous duals.  This is exactly the theorem at
`cy3_chain_level_bridge.tex:216-289`.

2. Quantum source:

```tex
  \Obs_{\hCS}^{q}(U,\mathfrak g)
```

exists only after Costello--Li/Costello--Gwilliam renormalisation,
anomaly cancellation, compact-support convention, and a domain for
`\Delta_L` have been fixed.

3. Quantum bar candidate:

```tex
  B_{E_3}^{\hbar}
  U^{\mathrm{fact},E_3}_P(\mathfrak L_{\cC})
  :=
  \left(
    B_{E_3}U^{\mathrm{fact},E_3}_P(\mathfrak L_{\cC})[[\hbar]],
    D_B^\hbar
  \right)
```

where

```tex
  D_B^\hbar=d_B+\sum_{r\geq1}\hbar^rD_r
```

is a continuous coderivation, filtered by loop order and local along
partial diagonals.

4. Hall comparison:

```tex
  \Theta_{\hCS\to\Hall}^{\mathrm{or}}
```

is an additional oriented descent datum.  It is not produced by the
quantum bar theorem; it is a separate map from the quantum source to the
critical Hall cosheaf.

## Conditional theorem to inscribe

The following theorem is the strongest honest formulation I can defend.

```tex
\begin{theorem}[Quantum BV/bar comparison on a CY3 polydisc]
\label{thm:cy3-quantum-bv-bar-conditional}
\ClaimStatusConditional{}
Let $P\subset X$ be a holomorphic polydisc in a smooth CY$_3$ with
holomorphic volume form $\Omega_X$.  Let
$\mathfrak L_{\cC}(P)$ be the many-variable compact-support
Dolbeault--jet dg Lie algebra of
Definition~\ref{def:cy3-many-variable-chiral-ce}.  Assume:
\begin{enumerate}
\item the Stage-$1$ $E_3$ formality point and Costello--Li holomorphic
      witness used in Proposition~\ref{prop:cy3-continuous-e3-bar-ce};
\item a Costello--Gwilliam/Costello--Li renormalisation datum
      $(I[L],\Delta_L,W_{\Gamma,L})$ on $P$ satisfying the
      renormalisation group equation and the quantum master equation;
\item vanishing, or chosen counterterm cancellation, of the local
      Costello--Li anomaly class
      $[P_4]\in H^1_{\mathrm{loc}}
      (\mathfrak L_{\cC},\mathcal O_{\mathrm{loc}})$;
\item a strict nuclear LF/DFS completion in which every renormalised
      Feynman operation $W_{\Gamma,L}C_\Gamma$ is continuous and
      compatible with extension by zero for disjoint polydiscs;
\item a continuous BV-to-bar transfer
      $T_L\colon
      B_{E_3}U^{\mathrm{fact},E_3}_P(\mathfrak L_{\cC})[[\hbar]]
      \to
      \Obs_{\hCS}^{q}(P,\mathfrak g)^\vee_b$
      whose classical limit is the duality of
      Proposition~\ref{prop:cy3-continuous-e3-bar-ce};
\item continuous coderivations
      $D_r$ on the completed $E_3$ bar coalgebra such that
      $D_B^\hbar=d_B+\sum_{r\geq1}\hbar^rD_r$ satisfies
      $(D_B^\hbar)^2=0$ and
      $(T_L^\vee)D_B^\hbar(T_L^\vee)^{-1}
      =
      Q_{\hCS}+\{I[L],-\}_{\BV}+\hbar\Delta_L$.
\end{enumerate}
Then there is a natural quasi-isomorphism of $\hbar$-adically complete
factorisation algebras
\[
  \Obs_{\hCS}^{q}(P,\mathfrak g)
  \simeq
  \left(
    B_{E_3}^{\hbar}
    U^{\mathrm{fact},E_3}_P(\mathfrak L_{\cC})
  \right)^\vee_b .
\]
Its associated graded at $\hbar=0$ is
Proposition~\ref{prop:cy3-continuous-e3-bar-ce}.
\end{theorem}
```

Proof.  The assumptions put the Costello--Li BV complex and the
completed `E_3` bar coalgebra in the same strict completed category.
The QME is equivalent to the square-zero identity for the renormalised
BV differential.  Assumption (6) transports that differential through
`T_L` to the completed bar coalgebra, so `D_B^\hbar` is square-zero.
Taking the strong continuous dual is exact on the strict nuclear
subcategory fixed in assumption (4), hence gives the displayed
quasi-isomorphism.  Factorisation follows from continuity and
extension-by-zero compatibility of the Feynman operations.  The
associated graded drops the `D_r`, `I_{r>0}`, and `\Delta_L` terms and
recovers the classical continuous-duality theorem.

This theorem is conditional because assumptions (2), (5), and (6) are
not constructed in the current manuscript.

## Conditional Hall corollary

The quantum CE/bar theorem can feed Hall only under the oriented Hall
comparison hypotheses.

```tex
\begin{corollary}[Quantum bar-to-Hall comparison]
\ClaimStatusConditional{}
Assume Theorem~\ref{thm:cy3-quantum-bv-bar-conditional}.  Assume in
addition an oriented hCS-to-Hall comparison datum on the DWR Cech/Ran
nerve whose obstruction tuple
\[
  (o_{\mathrm{MC}},o_{\mathrm{or}},o_{\mathrm{gr}},
   o_{\mathrm{TS}},o_{\mathrm{fact}})
\]
vanishes in the sense of
Definition~\ref{def:hcs-hall-descent-obstruction}.  Then the composite
\[
  \left(
    B_{E_3}^{\hbar}
    U^{\mathrm{fact},E_3}(\mathfrak L_{\cC})
  \right)^\vee_b
  \xrightarrow{\ \simeq\ }
  \Obs_{\hCS}^{q}
  \xrightarrow{\Theta_{\hCS\to\Hall}^{\mathrm{or}}}
  \CoHA_{\mathrm{crit}}^{\mathrm{or}}
\]
is a morphism of completed Hall-valued factorisation cosheaves.  On
the $\mathbb C^3$ chart its Hall-side reduction is the
Kontsevich--Soibelman/Schiffmann--Vasserot positive half
$\CoHA(\mathbb C^3)\cong Y^+(\widehat{\mathfrak{gl}}_1)$; any
$\mathcal W_{1+\infty}$ statement passes through the Drinfeld double
and Fock/evaluation representation.
\end{corollary}
```

This corollary is not a construction of `\Theta`.  It is a typed
consequence once the issue-1 comparison map exists.

## Exact obstruction list

The total obstruction to the requested unconditional theorem has seven
pieces.

1. `O_QME`: construct `I[L]` and `\Delta_L` on the chosen local
   functional space and prove QME.

2. `O_anom`: prove vanishing or counterterm cancellation of the
   Costello--Li quartic local anomaly
   `P_4\in\Sym^4(\mathfrak g^\vee)^{\mathfrak g}`.

3. `O_top`: specify a strict topological vector-space category in which
   the BV propagator kernels, compact-support extension maps, completed
   tensor products, strong duals, and bar coalgebras all live.

4. `O_transfer`: build the BV-to-bar transfer `T_L`, not only its
   classical associated graded.

5. `O_quantbar`: construct the continuous loop coderivations `D_r` and
   prove `(D_B^\hbar)^2=0`.

6. `O_descent`: prove the quantum operations are compatible with
   restriction, extension by zero, Weiss descent, and Ran collision
   residues.

7. `O_Hall`: construct the oriented Hall comparison map with vanishing
   MC, orientation, grading/Tate, Thom--Sebastiani, and factorisation
   obstructions.

The first six are source-side quantum CE/bar obligations.  The seventh
is the Hall comparison obligation.

## Claim-status recommendation

- Keep `prop:cy3-continuous-e3-bar-ce` as `ClaimStatusConditional`.
  It is a classical continuous-duality theorem conditional on the
  Stage-1 `E_3` witness.  It should not mention quantum BV.

- Add a new theorem of the form
  `thm:cy3-quantum-bv-bar-conditional` only as
  `ClaimStatusConditional`, with the six source-side assumptions listed
  above.

- Keep `def:cy3-hcs-quantum-observables` definitional but sharpen its
  domain in the manuscript when editing: `\mathcal O` should mean the
  Costello-renormalised local/multilocal functional space on which
  `\Delta_L` is defined, not all continuous polynomial functions.

- Keep `op:cy3-hcs-hall-comparison` open until `O_Hall` is actually
  constructed.

- Do not cite CFG 2026 as proof of the CY3 quantum Hall comparison.
  Cite it only as the ordinary Chern--Simons `E_3` envelope and QME
  grammar.

## Local anchors

- Quantum hCS observables and QME:
  `chapters/theory/cy3_chain_level_bridge.tex:73-99`.
- Many-variable compact-support Dolbeault/chiral CE model:
  `chapters/theory/cy3_chain_level_bridge.tex:101-214`.
- Classical continuous dual CE/bar theorem:
  `chapters/theory/cy3_chain_level_bridge.tex:216-289`.
- Quartic Costello--Li anomaly slot:
  `chapters/theory/cy3_chain_level_bridge.tex:458-487`.
- Warning that the Costello--Li quartic anomaly is not the `S_4` bar
  coefficient:
  `chapters/theory/cy3_chain_level_bridge.tex:489-498`.
- CFG no-shortcut warning:
  `chapters/theory/cy3_chain_level_bridge.tex:500-518`.
- Hall comparison open problem:
  `chapters/theory/cy3_chain_level_bridge.tex:602-658`.
- Hall descent obstruction dg Lie algebra:
  `chapters/theory/cy3_chain_level_bridge.tex:660-711`.
- Status ledger:
  `chapters/theory/cy3_chain_level_bridge.tex:780-797`.
- Stage-1 left-end assembly:
  `chapters/theory/cy3_chain_level_bridge.tex:799-817`.
- The `E_3` lift is extra Stage-1 data:
  `chapters/theory/cy3_chain_level_bridge.tex:900-938`.
- Chain-level Stage-1 envelope:
  `chapters/theory/cy3_chain_level_bridge.tex:967-1033`.
- CFG side-by-side scope fence:
  `chapters/theory/cy3_chain_level_bridge.tex:1035-1072`.
- Scope of the Stage-1 envelope:
  `chapters/theory/cy3_chain_level_bridge.tex:1074-1102`.
- Bibliography entries:
  `bibliography/references.tex:408-416` for Costello--Gwilliam and
  Costello--Li; `bibliography/references.tex:688-734` for KS and CFG.

## Verification run

Command:

```bash
python3 -m pytest \
  compute/tests/test_chiral_ce_complex.py \
  compute/tests/test_dolbeault_cy3_homotopy.py \
  compute/tests/test_coha_drinfeld_bulk.py \
  -q
```

Result:

```text
236 passed in 0.45s
```

Interpretation: these tests support the finite CE/bar, Dolbeault
homotopy, and Hall/Drinfeld positive-half shadows.  They do not test the
quantum BV renormalisation, the BV-to-bar transfer, or the Hall-valued
comparison map.

## Files changed

Only this report:

```text
notes/adversarial_swarm_20260424_total_resolution/agent_A2_quantum_ce_bar.md
```
