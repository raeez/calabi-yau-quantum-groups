# Agent A1 - Oriented hCS-to-Hall comparison

Date: 2026-04-24.

Scope: adversarial audit of the proposed orientation-preserving comparison
\[
\Theta_{\hCS\to\Hall}^{\or}:
  \Obs_{\hCS}^{q}(-,\mathfrak g)\longrightarrow
  \CoHA_{\crit}^{\or}(-)
\]
from CY3 holomorphic Chern-Simons observables to critical CoHA with
vanishing cycles.  I made no manuscript edits.

## Verdict

The manuscript cannot honestly claim a constructed map
\(\Theta_{\hCS\to\Hall}^{\or}\) in general.  The current sources prove or
cite the two ends of the intended bridge:

- the hCS observable/factorization side, anomaly-gated and completed;
- the local Hall theorem \(\CoHA(\mathbb C^3)\cong Y^+\), with
  \(\mathcal W_{1+\infty}\) appearing only after Drinfeld doubling and
  representation/evaluation.

What is missing is the comparison itself: a continuous natural
transformation on the full Dolbeault-Weiss/Ran nerve, with orientation,
shift, Tate twist, completion, and Thom-Sebastiani compatibilities.  This
is not supplied by CFG, not supplied by chartwise critical CoHA, and not
supplied by equality of characters or low-rank computations.

The strongest inscribable result now is a definition of an oriented
hCS-Hall comparison datum and a conditional proposition: if such a datum
exists, then the local-to-toric Hall bridge and the \(\mathbb C^3\)
positive-half comparison follow with the stated normalizations.  The
construction of the datum remains an open proof obligation, not a theorem.

## Claims attacked

1. CFG/topological Chern-Simons supplies \(\Theta_{\hCS\to\Hall}^{\or}\).
   False.  CFG controls an \(E_3\) formality/topological-CS model; it does
   not carry the CY3 Dolbeault differential, holomorphic jets, residue
   pairing, compact-support convention, orientation datum, vanishing-cycle
   target, or Hall correspondences.

2. Chartwise \(\CoHA(\mathbb C^3)=Y^+\) constructs the global comparison.
   False.  This identifies the Hall-side local algebra in the affine
   toric model.  It does not produce a map from hCS observables, nor does
   it solve descent across overlaps.

3. Ordinary BM cohomology or an unshifted critical locus is enough.
   False.  The target is vanishing-cycle BM homology with orientation
   local system, cohomological/perverse shift, Tate twist, and
   equivariant/localized completion.

4. The superscript \(\or\) is decorative.
   False.  The comparison needs determinant-line square roots, transport
   across local critical charts, compatibility under direct sums and
   extensions, and vanishing of the residual \(\mathbb Z/2\) orientation
   cocycle on triple overlaps.

5. Thom-Sebastiani compatibility follows automatically from Hall
   multiplication.
   False.  Hall multiplication uses iterated extension correspondences.
   A comparison must specify coherent TS isomorphisms for both
   parenthesisations, including signs, shifts, Tate twists, and
   orientation local systems.

6. The hCS-to-Hall comparison is proved by K3xE/BKM character agreement.
   False.  Character and root-multiplicity agreements are evidence for
   the expected target, not a construction of a chain-level algebra map.

7. \(\CoHA(\mathbb C^3)=\mathcal W_{1+\infty}\).
   False.  The manuscript now correctly separates
   \(\CoHA(\mathbb C^3)=Y^+\) from the Drinfeld double/Fock/evaluation
   route to \(\mathcal W_{1+\infty}\).

## Fatal gaps for a proof now

- No DWR/Ran natural transformation has been constructed on all
  \(k\)-simplices of the cover nerve.
- No overlap coherence transports the orientation datum across all local
  critical charts.
- No proof kills the residual \(\mathbb Z/2\) orientation obstruction on
  triple overlaps.
- The shift \(s(U,d)\) and Tate twist \(t(U,d)\) are named but not fixed
  by a convention that matches the hCS grading.
- The completion comparison is not constructed: Hall-side
  charge/HN-adic and equivariant-localized completions must be matched
  with hCS \(\hbar\)-adic and continuous-dual completions.
- The BV bracket/factorization product on hCS has not been identified
  with Hall extension product after the CY3 shift.
- Thom-Sebastiani coherence for iterated short exact sequences is not
  proved.
- Gauge/rank datum, stability condition, equivariant parameters, compact
  support convention, and anomaly cancellation are necessary hypotheses;
  without them the source and target are not even typed in the same
  category.
- Existing compute tests verify structural toy models, positive-half
  dimensions, wall-crossing signatures, and CFG consistency.  They do not
  test or construct \(\Theta_{\hCS\to\Hall}^{\or}\).

## Surviving proof spine

1. The hCS source is well typed where the Costello-Gwilliam/Li
   quantization data exist and the one-loop obstruction is cancelled.
   The manuscript defines
   \[
   \Obs_{\hCS}^{q}(U,\mathfrak g)
   =
   (\mathcal O(\mathcal E_{\hCS,c}(U,\mathfrak g))[[\hbar]],
   Q+\{I[L],-\}+\hbar\Delta_L)
   \]
   with compact supports and completion.

2. The Stage-1 CY3 chain-level envelope identifies the left end:
   \(\Phi^{\FA}_3\) is modeled by the holomorphic/dolbeault
   factorization construction on the verified locus.  The \(E_3\)
   formality input is conditional and torsor-valued; it does not choose
   a Hall comparison.

3. The Hall target can be specified as a Hall-valued factorization
   cosheaf with vanishing-cycle BM summands
   \[
   H^{BM}_{G_d}(\Crit(f_{U,d}),\phi_{f_{U,d}}\otimes
   \mathcal L_{o_U})[s(U,d)](t(U,d)).
   \]
   This is a target definition, not a comparison theorem.

4. The local Hall theorem on \(\mathbb C^3\) survives:
   \(\CoHA(\mathbb C^3)\cong Y^+(\widehat{\mathfrak{gl}}_1)\).
   The path to \(\mathcal W_{1+\infty}\) passes through the Drinfeld
   double and a representation/evaluation functor.

5. Toric descent is available only conditionally: if the oriented
   comparison datum exists on the DWR/Ran nerve and the orientation gerbe
   is trivialized compatibly, then chartwise Hall identifications glue.

6. Joyce/KPS/BBJ/PTVV/DHSM-style local results provide credible
   ingredients for determinant lines, orientations, shifted symplectic
   critical charts, and vanishing-cycle transport.  They do not by
   themselves construct the hCS observable map.

## Strongest statement to inscribe now

Do not inscribe a theorem saying \(\Theta_{\hCS\to\Hall}^{\or}\) has been
constructed.  Inscribe a definition plus a conditional proposition of the
following form.

```tex
\begin{definition}[Oriented hCS--Hall comparison datum]
Let \(X\) be a Calabi--Yau threefold with holomorphic volume form
\(\Omega_X\), gauge/rank datum \(\mathfrak g\), stability condition, and
equivariant parameters.  An oriented hCS--Hall comparison datum is the
following data on a Dolbeault--Weiss--Ran polydisc basis:
\begin{enumerate}
\item an anomaly-cancelled quantum hCS factorization cosheaf
      \(\Obs_{\hCS}^{q}(-,\mathfrak g)\), completed \(\hbar\)-adically
      and in continuous duals;
\item an oriented critical Hall factorization cosheaf
      \(\CoHA_{\crit}^{\or}(-)\), completed charge/HN-adically and
      equivariantly localized;
\item for every chart and dimension vector, a fixed shift \(s(U,d)\) and
      Tate twist \(t(U,d)\) in the vanishing-cycle BM summand;
\item square roots of virtual determinant lines, with orientation local
      systems and coherences for direct sums, extensions, and chart
      overlaps;
\item coherent Thom--Sebastiani isomorphisms for all iterated extension
      correspondences, including both parenthesisations;
\item a continuous natural transformation on the full
      Dolbeault--Weiss--Ran Cech nerve
      \[
      \Theta_{\hCS\to\Hall}^{\or}:
      \Obs_{\hCS}^{q}(-,\mathfrak g)\to\CoHA_{\crit}^{\or}(-)
      \]
      compatible with restrictions, products, CY3 shifts, twists,
      orientations, and completions.
\end{enumerate}
\end{definition}

\begin{proposition}[Conditional oriented local-to-Hall bridge]
Assume an oriented hCS--Hall comparison datum exists for \(X\).  Then
\(\Theta_{\hCS\to\Hall}^{\or}\) is a morphism of completed
Hall-valued factorization cosheaves.  On the affine toric
\(\mathbb C^3\) chart its Hall-side reduction is the
Kontsevich--Soibelman--Schiffmann--Vasserot positive-half algebra
\(\CoHA(\mathbb C^3)\cong Y^+\).  After Drinfeld doubling and
representation/evaluation one obtains the corresponding
\(\mathcal W_{1+\infty}\)-module shadow; the undoubled critical CoHA is
not itself \(\mathcal W_{1+\infty}\).
\end{proposition}
```

Proof outline for the conditional proposition:

1. The definition places source and target in the same completed
   Hall-valued factorization-cosheaf category.
2. Naturality on the DWR/Ran nerve gives descent, not merely chartwise
   agreement.
3. Compatibility with extension products and TS isomorphisms identifies
   hCS factorization multiplication with Hall multiplication, including
   orientation local systems and parenthesisation signs.
4. Fixed \(s(U,d)\), \(t(U,d)\), and completions make the map homogeneous
   and continuous.
5. On \(\mathbb C^3\), the Hall-side reduction is the known
   KS/SV positive-half theorem.  The \(\mathcal W_{1+\infty}\) statement
   follows only after the already separate double/evaluation step.

This statement advances the manuscript without downgrading it: the
construction remains open, while every conditional consequence is typed.

## File anchors

- `chapters/theory/cy3_chain_level_bridge.tex:11`: hCS BV complex
  \(\Omega^{0,\bullet}(X,\mathfrak g)[1]\), \(\bar\partial\), and
  degree \(-1\) BV pairing.
- `chapters/theory/cy3_chain_level_bridge.tex:73`: quantum hCS
  observables with compact supports and \(\hbar\)-adic completion.
- `chapters/theory/cy3_chain_level_bridge.tex:198`: typed bridge diagram
  \(\Phi^{\FA}_3 \dashrightarrow \CoHA_{\crit}\to Y^+\to D(Y^+)\to
  \mathcal W_{1+\infty}\).
- `chapters/theory/cy3_chain_level_bridge.tex:223`: Hall-valued
  factorization-cosheaf target lists orientation data, completions, and
  TS coherences.
- `chapters/theory/cy3_chain_level_bridge.tex:262`: local critical-CoHA
  normalization with \(H^{BM}\), \(\phi_f\), orientation local system,
  shift, and Tate twist.
- `chapters/theory/cy3_chain_level_bridge.tex:294`: local
  \(\mathbb C^3\) core \(\CoHA(\mathbb C^3)\cong Y^+\).
- `chapters/theory/cy3_chain_level_bridge.tex:430`: open problem
  defining the required \(\Theta_{\hCS\to\Hall}^{\or}\).
- `chapters/theory/cy3_chain_level_bridge.tex:488`: status ledger says
  \(\Phi^{\FA}_3\to\CoHA_{\crit}(X)\) is open in general.
- `chapters/theory/cy_to_chiral.tex:122`: local \(\mathbb C^3\)
  Hall model is not obtained by applying \(\Phi_3\) to CoHA.
- `chapters/theory/cy_to_chiral.tex:387`: CFG side-by-side; CFG is a
  template, not the CY3 Dolbeault-Hall comparison.
- `chapters/theory/cy_to_chiral.tex:583`: critical CoHAs are Hall-side
  \(E_1\) algebras, not inputs to \(\Phi_3\).
- `chapters/examples/toric_cy3_coha.tex:15`: toric descent requires
  orientation-compatible overlap Morita data and residual
  \(\mathbb Z/2\) orientation-gerbe trivialisation.
- `chapters/examples/derived_categories_cy.tex:946`: DHSM/Morita and
  vanishing-cycle transport anchors for local Hall-side chart transport.
- `chapters/examples/k3_chiral_bialgebra_platonic.tex:4091`:
  Joyce/KPS/PTVV/BBJ orientation and determinant-line anchors.
- `notes/wave_cfg2026/agent_1_kt_e3_formality.tex:89`: \(E_3\)
  formality is available only after choosing formality data.
- `notes/wave_cfg2026/agent_10_coha_e3_factorization.tex:203`:
  Schiffmann-Vasserot positive-half Hall anchor.
- `notes/adversarial_swarm_20260424_cfg_e3/SYNTHESIS.md:173`:
  prior CFG swarm isolates \(\Theta_{\hCS\to\Hall}^{\or}\) as an open
  obligation.
- `notes/adversarial_swarm_20260424_hol_e3/agent_11_kontsevich_soibelman_hall.md:90`:
  previous Hall-focused attack gives the same missing datum list.

## Compute and test anchors

- `compute/lib/coha_chart_explicit.py:1`: symbolic critical CoHA and
  vanishing-cycle chart computations; useful for local dimensions, not
  for \(\Theta\).
- `compute/tests/test_coha_chart_explicit.py:441`: tests
  vanishing-cycle placeholders and plane-partition dimensions.
- `compute/tests/test_coha_wall_crossing_platonic.py:225`: KS
  wall-crossing as MC data; not a determinant-line orientation proof.
- `compute/lib/coha_gluing_morphisms.py:1`: Cech/wall-crossing
  gluing model; not the hCS observable map and not an orientation-gerbe
  proof.
- `compute/tests/test_cfg25_adversarial_consistency.py:1`: CFG
  consistency tests; they do not construct the CY3 hCS-to-Hall map.
- `compute/lib/hcs_vs_sigma_adversarial.py:1`: route audit marking the
  hCS/K3 Yangian route conjectural.
- `compute/lib/k3e_coha_structure.py:1`: K3xE CoHA/BKM structural
  evidence; not a chain-level \(\Theta\).

## Primary source anchors present locally

Bibliography entries in `bibliography/references.tex`:

- Costello 2013, Yangian from supersymmetric gauge theory.
- Costello-Gwilliam, factorization algebras in QFT.
- Costello-Li 2016/2020, quantum BCOV and anomaly/renormalization
  technology.
- Kontsevich-Soibelman 2008 and 2011, motivic DT/wall-crossing and CoHA.
- Schiffmann-Vasserot 2013, cohomological Hall algebra and Yangian.
- PTVV 2013, shifted symplectic structures.
- Safronov 2017 and Calaque-PTVV 2017, shifted Poisson/symplectic
  deformation anchors.
- RSYZ 2020, CoHA/vertex-algebra corner correspondence.

Local prose anchors not all present as bibliography items:

- Brav-Bussi-Joyce 2019 and Joyce/Kinjo-Park-Safronov orientation
  material in `chapters/examples/k3_chiral_bialgebra_platonic.tex`.
- Davison-Hennecart-Schedler-Meinhardt vanishing-cycle transport and
  derived Morita material in `chapters/examples/derived_categories_cy.tex`.

## Files changed

Only this report:

- `notes/adversarial_swarm_20260424_frontier_resolution/agent_A1_theta_hcs_hall.md`
