# Agent 01 -- Gelfand-Kapranov Formal-Moduli Examination

Date: 2026-04-24

Object attacked: the chain-level, full-homotopical construction of
\(\Phi\) on CY\(_3\), especially the assertion that the CY\(_3\) avatar
is produced from the Costello--Francis--Gwilliam 2026 local
\(C^*(\mathfrak g)\) model.

Verdict: CFG 2026 supplies the locally constant/topological associated
model for ordinary real \(3\)-dimensional Chern--Simons theory.  It does
not identify the Vol III CY\(_3\) avatar with ordinary \(C^*(\mathfrak g)\).
The repaired CY\(_3\) object is the Dolbeault/formal-moduli and chiral
CE object in three holomorphic variables.  On a holomorphic polydisc
\(U \subset X\) with coordinates \(z_1,z_2,z_3\),
\[
  L_U^{\hCS}
  :=
  \Omega^{0,\bullet}(U)\widehat\otimes \mathfrak g,
  \qquad
  d_{L_U}=\bar\partial,\qquad
  [\alpha\otimes x,\beta\otimes y]
  =
  \alpha\wedge\beta\otimes[x,y].
\]
The formal-moduli observable algebra is
\[
  \Obs_{\hCS}^{\cl}(U)
  =
  C^*_{\Lie,\cont}(L_U^{\hCS})
  =
  \prod_{n\ge 0}
  \Sym^n_{\cont}\!\left((L_U^{\hCS})^\vee[-1]\right),
  \qquad
  d=d_{\bar\partial}+d_{[,]},
\]
where \((-)^\vee\) is the Costello--Gwilliam differentiable-vector-space
continuous dual.  On the formal polydisc at \(x\),
\[
  H^0_{\bar\partial}(L_{\widehat x}^{\hCS})
  \simeq
  \mathfrak g\widehat\otimes \mathbb C[[z_1,z_2,z_3]],
  \qquad
  \Obs_{\hCS,\widehat x}^{\cl}
  \simeq
  C^*_{\Lie,\cont}\!\left(
    \mathfrak g\widehat\otimes \mathbb C[[z_1,z_2,z_3]]
  \right).
\]
The ordinary \(C^*(\mathfrak g)\) of CFG is only the locally constant
associated/contracted model obtained by replacing the Dolbeault-jet
object by the de Rham local system on a real \(3\)-ball, or by applying
the evaluation \(z_i\mapsto 0\).  The latter gives a contravariant map
\[
  C^*(\mathfrak g)
  \longrightarrow
  C^*_{\Lie,\cont}\!\left(
    \mathfrak g\widehat\otimes \mathbb C[[z_1,z_2,z_3]]
  \right),
\]
not a CY\(_3\) equivalence.

## Source Anchors

- CFG 2026 arXiv:2602.12412, `2025draft.tex:307-397`: factorization
  algebras, local constancy on real \(3\)-balls, filtered \(E_3\)-algebra,
  and the ordinary \(C^*(\mathfrak g)\) model.
- CFG 2026, `2025draft.tex:400-419`: ghosts for constant gauge
  transformations and CE cochains as derived invariants.
- CFG 2026, `2025draft.tex:1571-1710`: formal moduli
  \(B\mathfrak g^M\), \(C^*(\Omega^*(M)\otimes\mathfrak g)\), DVS
  continuous duals, Poincare quasi-isomorphism on \(\mathbb R^3\).
- CFG 2026, `2025draft.tex:1830-1955`: quantum observables, filtration,
  locally constant filtered \(E_3\)-algebra, and first-order shifted
  Poisson bracket.
- `chapters/theory/cy3_chain_level_bridge.tex:11-43`: hCS BV complex
  \(\Omega^{0,\bullet}(X,\mathfrak g)[1]\) and anomaly-gated
  \(\Obs_{\hCS}^q\).
- `chapters/theory/cy3_chain_level_bridge.tex:45-68`: typed CY\(_3\)
  bridge and the fact that \(\CoHA(\mathbb C^3)=Y^+\), not
  \(\mathcal W_{1+\infty}\) directly.
- `chapters/theory/cy3_chain_level_bridge.tex:70-130`: Hall-valued
  factorization-cosheaf target, orientation datum, completions, shifts,
  and critical-CoHA normalization.
- `chapters/theory/cy3_chain_level_bridge.tex:203-239`: quartic anomaly
  gate and the warning that CFG is not an hCS-to-Hall shortcut.
- `chapters/theory/cy3_chain_level_bridge.tex:244-317`: open
  \(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\) comparison and status ledger.
- `chapters/theory/cy_to_chiral.tex:4-41`, `271-294`, `4680-4792`:
  two-stage \(\PhiFA_3\to\Phi_3^{(\Sigma_2,C)}\), native \(E_1\) final
  output, and open compact CY\(_3\) strictification/Hall comparison.
- `chapters/theory/cyclic_ainf.tex:71-85`, `115-135`: CY dimension,
  negative cyclic class, \(S^3\)-framing, and non-adjacent contraction
  obstruction.
- `chapters/theory/en_factorization.tex:590-641`: conjectural
  \(E_3\)-chiral factorization on \(\mathbb C^3\), three OPE residue
  differentials, and \(E_3\)-Koszul duality.
- `chapters/theory/cy_to_chiral.tex:4911-4933`: bar--CE identification
  for chiral envelopes.
- `compute/lib/holomorphic_cs_chiral_engine.py:1-61`, `226-235`:
  hCS hierarchy and chiral CE variants.
- `compute/lib/e3_config_space_chiral.py:1-83`: \(\Conf_n(\mathbb C^3)\),
  trivial topological \(\pi_1\), Omega-background deformation, and
  \(E_3\)-organized Feynman integrals.

## Repaired Formula Package

The repaired local input is not a single Lie algebra \(\mathfrak g\), but
the Dolbeault local dg Lie algebra \(L_U^{\hCS}\).  The holomorphic-jet
shadow at a point is
\[
  J_{\widehat x}^{\hol}\mathfrak g
  :=
  \mathfrak g\widehat\otimes\mathbb C[[z_1,z_2,z_3]].
\]
The chiral/formal-moduli passage should be written as
\[
  \mathfrak L_{\hCS}^{\ch}(U)
  =
  \bigl(
    \Omega^{0,\bullet}(U)\widehat\otimes\mathfrak g,\,
    \bar\partial,\,
    [-,-],\,
    \partial_{z_1},\partial_{z_2},\partial_{z_3}
  \bigr),
\]
\[
  \Obs_{\hCS}^{\cl}(U)
  =
  C^*_{\Lie,\cont}(\mathfrak L_{\hCS}^{\ch}(U)),
  \qquad
  \Obs_{\hCS}^{q}
  =
  U^{\ch,E_3}_{\hbar}(\mathfrak L_{\hCS}^{\ch})
  \quad
  \text{after anomaly cancellation}.
\]
Here \(U^{\ch,E_3}_{\hbar}\) means the BV/chiral enveloping
factorization algebra, not the ordinary enveloping algebra of
\(\mathfrak g\).  For disjoint holomorphic polydiscs
\(U_1,\ldots,U_k\subset V\),
\[
  m_V^{U_1,\ldots,U_k}\colon
  \Obs_{\hCS}^{q}(U_1)\widehat\otimes\cdots\widehat\otimes
  \Obs_{\hCS}^{q}(U_k)
  \longrightarrow
  \Obs_{\hCS}^{q}(V)
\]
is the factorization product.  Collision is controlled by singularities
along all partial diagonals in \((\mathbb C^3)^k\).  A local
multi-directional OPE has the form
\[
  a(z)b(w)
  \sim
  \sum_{\alpha\in\mathbb N^3}
  \frac{(a_{(\alpha)}b)(w)}
  {(z_1-w_1)^{\alpha_1+1}
   (z_2-w_2)^{\alpha_2+1}
   (z_3-w_3)^{\alpha_3+1}},
\]
with residue operations
\[
  d_i^{\OPE}=\operatorname{Res}_{z_i=w_i},
  \qquad i=1,2,3.
\]
The \(E_3\) bar/chiral CE comparison that is actually needed is
\[
  B_{E_3}\!\left(U^{\ch,E_3}_{\hbar}(\mathfrak L_{\hCS}^{\ch})\right)
  \simeq
  \CE_{*,\ch}^{E_3}(\mathfrak L_{\hCS}^{\ch}),
\]
with differential schematically
\[
  d_{\mathrm{bar}}
  =
  d_{\CE}
  +
  d_1^{\OPE}+d_2^{\OPE}+d_3^{\OPE}
  +
  \hbar\Delta_{\BV}
  +
  \text{higher }L_\infty\text{/renormalization terms}.
\]
Status: the one-variable Lie-conformal bar--CE statement is proved in
the manuscript; the displayed \(E_3\) Dolbeault/chiral upgrade is the
precise conjectural/conditional lemma needed for the CY\(_3\) bridge.

## ATTACK -> HEAL Cycles

### Cycle 1 -- Ordinary \(C^*(\mathfrak g)\) vs Dolbeault CE in three variables

Claim attacked: CFG's local \(C^*(\mathfrak g)\) can be used as the
CY\(_3\) avatar of \(\PhiFA_3\).

Failure mode: CFG reaches \(C^*(\mathfrak g)\) because ordinary
Chern--Simons on a real \(3\)-ball has de Rham dg Lie algebra
\(\Omega^*(D^3)\otimes\mathfrak g\), and Poincare contraction gives
\(\mathfrak g\).  A holomorphic CY\(_3\) polydisc has Dolbeault dg Lie
algebra \(\Omega^{0,\bullet}(U)\widehat\otimes\mathfrak g\).  Dolbeault
Poincare on a Stein polydisc leaves holomorphic functions; on the formal
polydisc it leaves \(\mathfrak g[[z_1,z_2,z_3]]\), not \(\mathfrak g\).

Surviving core: CFG correctly teaches the formal-moduli rule
\[
  \text{functions on }B L = C^*_{\Lie,\cont}(L).
\]
The rule transfers, but \(L\) changes from
\(\Omega^*(D^3)\otimes\mathfrak g\) to
\(\Omega^{0,\bullet}(U)\widehat\otimes\mathfrak g\).

Healed statement with epistemic status: Proved for CFG ordinary
topological CS; conditional/expected for the CY\(_3\) hCS local chart:
\[
  \Obs_{\hCS}^{\cl}(U)
  =
  C^*_{\Lie,\cont}
  \left(\Omega^{0,\bullet}(U)\widehat\otimes\mathfrak g\right),
  \qquad
  \Obs_{\hCS,\widehat x}^{\cl}
  \simeq
  C^*_{\Lie,\cont}
  \left(\mathfrak g\widehat\otimes\mathbb C[[z_1,z_2,z_3]]\right).
\]
Ordinary \(C^*(\mathfrak g)\) is only the locally constant associated
model.

Proof obligations: define the continuous dual and completed symmetric
powers in the Dolbeault DVS category; prove the Dolbeault contraction is
compatible with polydisc factorization; specify whether the chart uses
smooth Dolbeault forms, holomorphic functions, or formal jets; record the
non-equivalence with \(C^*(\mathfrak g)\).

Anchors: CFG `2025draft.tex:377-397`, `1571-1710`;
`chapters/theory/cy3_chain_level_bridge.tex:11-43`;
`compute/lib/dolbeault_cy3_homotopy.py:1-120`.

### Cycle 2 -- Formal derived stack of flat bundles vs CY\(_3\) hCS formal moduli

Claim attacked: the CFG formal derived stack of flat bundles on a ball
is the same formal stack needed for the CY\(_3\) Hall bridge.

Failure mode: CFG studies the formal neighborhood of the trivial flat
\(G\)-bundle, modeled by \(B(\Omega^*(M)\otimes\mathfrak g)\).  The
CY\(_3\) bridge needs formal moduli of holomorphic structures/MC
solutions for \(\Omega^{0,\bullet}(U)\otimes\mathfrak g\), and then a
comparison to critical stacks
\[
  [\operatorname{Rep}_{\mathbf d}(Q_U)/G_{\mathbf d}],
  \qquad
  f_{U,\mathbf d}=\operatorname{Tr}(W_U)_{\mathbf d},
\]
with vanishing cycles, orientation local systems, shifts, Tate twists,
and completions.  The CFG formal stack has no Hall charge, stability,
vanishing-cycle, or determinant-square-root datum.

Surviving core: both sides are formal-moduli problems controlled by dg
Lie or \(L_\infty\) algebras.  The correct comparison target is a natural
transformation of factorization cosheaves, not an identification of
underlying cochains.

Healed statement with epistemic status: Open in general; expected on
local toric/quiver charts after all normalizations are chosen:
\[
  \Theta_{\hCS\to\Hall}^{\mathrm{or}}\colon
  \Obs_{\hCS}^{q}(-,\mathfrak g)
  \longrightarrow
  \CoHA_{\mathrm{crit}}^{\mathrm{or}}(-)
\]
inside
\(\mathsf{FactCosh}_{\Hall}^{\mathrm{or},\wedge}(X)\).  On the
\(\mathbb C^3\) chart, the target normalization must reduce to the
Kontsevich--Soibelman/Schiffmann--Vasserot positive-half model
\(\CoHA(\mathbb C^3)=Y^+\).

Proof obligations: construct the local Ext-quiver-with-potential chart;
match the hCS \(L_\infty\) Maurer--Cartan equation with the critical
locus of \(\operatorname{Tr}W\); preserve KS/Joyce orientation data on
overlaps; prove Thom--Sebastiani compatibility; fix shifts/Tate twists
before asserting any graded quasi-isomorphism.

Anchors: `chapters/theory/cy3_chain_level_bridge.tex:70-130`,
`244-291`; CFG `2025draft.tex:1581-1588`, `1666-1703`.

### Cycle 3 -- Ghosts for constant gauge transformations

Claim attacked: CFG's ghosts for constant gauge transformations transfer
verbatim and exhaust the CY\(_3\) ghost sector.

Failure mode: CFG's explanation is for perturbative ordinary CS: Lie
algebra invariants are not exact, so derived invariants introduce CE
ghosts, and on a real ball the de Rham model contracts to constant
\(\mathfrak g\)-ghosts.  The CY\(_3\) hCS gauge algebra over a polydisc is
\(\Omega^{0,0}(U)\otimes\mathfrak g\), and its formal holomorphic
residue is \(\mathfrak g[[z_1,z_2,z_3]]\).  Constant ghosts are only the
degree-zero constant summand of the holomorphic-jet ghost complex.

Surviving core: the derived-invariants principle survives exactly:
ghosts encode the derived quotient by gauge transformations.  The local
CY\(_3\) ghost complex is the holomorphic/Dolbeault gauge Lie algebra,
not merely the finite-dimensional constant Lie algebra.

Healed statement with epistemic status: Proved for CFG ordinary CS;
conditional for hCS charts:
\[
  \mathfrak{gh}_{\hCS}(U)
  =
  \Omega^{0,0}(U)\otimes\mathfrak g[1],
  \qquad
  \mathfrak{gh}_{\hCS,\widehat x}
  =
  \mathfrak g[[z_1,z_2,z_3]][1].
\]
The ordinary constant ghost sector is the image of
\(\mathfrak g[1]\hookrightarrow \mathfrak g[[z_1,z_2,z_3]][1]\), not the
whole CY\(_3\) ghost sector.

Proof obligations: identify the BRST ghost differential with the tangent
complex of the holomorphic quotient stack; handle reducible stabilizers
and compact CY\(_3\) \(H^0(X,\mathcal O_X)\)-automorphisms; compare the
BRST differential with the equivariant differential in the Hall
\(G_{\mathbf d}\)-quotient.

Anchors: CFG `2025draft.tex:400-419`;
`chapters/theory/cy3_chain_level_bridge.tex:104-130`, `244-291`.

### Cycle 4 -- Local observables and multidirectional OPE over polydiscs

Claim attacked: local observables become an \(E_3\)-algebra merely
because CFG proves local constancy on real \(3\)-balls.

Failure mode: CFG's \(E_3\) follows from locally constant factorization
algebras on \(\mathbb R^3\).  CY\(_3\) hCS is holomorphic/Dolbeault in
three complex variables.  The relevant local category is polydiscs with
Weiss/Ran factorization and singularities along diagonals in
\((\mathbb C^3)^n\), not topological balls with all geometry contracted.
The OPE has three holomorphic coordinate directions, so a one-variable
Lie-conformal OPE is insufficient.

Surviving core: CFG's factorization-product axiom transfers:
\[
  m_V^{U_1,\ldots,U_k}\colon
  \Obs(U_1)\widehat\otimes\cdots\widehat\otimes\Obs(U_k)\to\Obs(V)
\]
for disjoint opens.  What changes is the analytic geometry of the opens
and the singularity calculus of collision.

Healed statement with epistemic status: Conditional/conjectural for
CY\(_3\) hCS:
\[
  a(z)b(w)
  \sim
  \sum_{\alpha\in\mathbb N^3}
  \frac{(a_{(\alpha)}b)(w)}
  {(z_1-w_1)^{\alpha_1+1}
   (z_2-w_2)^{\alpha_2+1}
   (z_3-w_3)^{\alpha_3+1}},
\]
and the \(E_3\) bar object has three residue differentials
\[
  d_i^{\OPE}=\operatorname{Res}_{z_i=w_i},\qquad
  [d_i^{\OPE},d_j^{\OPE}]=0
  \quad \text{as a required coherence, not an automatic slogan.}
\]

Proof obligations: construct the multidirectional chiral operations as
local distributions/currents on polydisc configuration spaces; prove
Weiss descent; prove pairwise and triple collision compatibility;
separate trivial topological \(\pi_1(\Conf_2(\mathbb C^3))\) from
Omega-background \(R\)-matrix data.

Anchors: CFG `2025draft.tex:324-354`; `chapters/theory/en_factorization.tex:607-641`;
`compute/lib/e3_config_space_chiral.py:17-31`, `71-83`.

### Cycle 5 -- CE cochains vs chiral CE/enveloping factorization algebra

Claim attacked: the CE cochain algebra of formal moduli is already the
final chiral factorization algebra produced by \(\Phi_3\).

Failure mode: formal-moduli CE cochains are the algebra of functions on
the derived solution stack.  The Vol III output requires the chiral CE
and enveloping factorization passage: ordered/symmetric bar complexes,
chiral OPE residues, and Verdier/Ran duality.  The manuscript proves the
one-variable Lie-conformal bar--CE identification, but the \(E_3\)
Dolbeault upgrade is not yet proved.

Surviving core: the bar--CE pattern is the correct algebraic spine.  It
must be upgraded from
\[
  B(U^{\ch}(\mathfrak L))\simeq \CE_*(\mathfrak L)
\]
to an \(E_3\) Dolbeault/chiral statement involving
\(\mathfrak L_{\hCS}^{\ch}\).

Healed statement with epistemic status: Proved in the manuscript for
ordinary Lie conformal inputs; conjectural/conditional for the CY\(_3\)
Dolbeault object:
\[
  B_{E_3}\!\left(U^{\ch,E_3}_{\hbar}(\mathfrak L_{\hCS}^{\ch})\right)
  \simeq
  \CE_{*,\ch}^{E_3}(\mathfrak L_{\hCS}^{\ch}),
\]
with
\[
  d_{\mathrm{bar}}
  =
  d_{\CE}
  +d_1^{\OPE}+d_2^{\OPE}+d_3^{\OPE}
  +\hbar\Delta_{\BV}
  +\text{higher }L_\infty\text{ terms}.
\]
The CY\(_3\) avatar is this Dolbeault/chiral CE envelope, not ordinary
\(C^*(\mathfrak g)\).

Proof obligations: define \(U^{\ch,E_3}_{\hbar}\) as a genuine
factorization enveloping functor on the Dolbeault/Ran site; prove PBW or
filtered associated-graded control; match the three OPE residue
differentials with the three complex directions; prove compatibility
with the cyclic \(S^3\)-framing and the Costello TCFT homotopy.

Anchors: `chapters/theory/cy_to_chiral.tex:4911-4933`;
`compute/lib/holomorphic_cs_chiral_engine.py:30-35`, `226-235`;
`chapters/theory/cyclic_ainf.tex:71-85`, `115-135`.

### Cycle 6 -- Quantum deformation and anomaly transfer

Claim attacked: CFG's obstruction-free ordinary CS quantization implies
obstruction-free CY\(_3\) hCS quantization.

Failure mode: CFG's filtered \(E_3\) quantum observables are ordinary
CS observables, with associated graded abelian CS and a deformation
controlled by the pairing.  In CY\(_3\) hCS, the local one-loop anomaly
lies in the invariant-polynomial slot of degree \(4\).  The cubic
surface/five-dimensional slot does not transfer to complex dimension
\(3\), and the quantum object only exists after the quartic anomaly gate
is passed.

Surviving core: CFG's filtration principle is useful.  The quantum
observables should be a filtered deformation of the Dolbeault CE/chiral
object, with BV Laplacian lowering symmetric degree and \(\hbar\)-adic
completion.

Healed statement with epistemic status: CFG ordinary CS is proved;
CY\(_3\) hCS is proved elsewhere only after anomaly cancellation:
\[
  \Obs_{\hCS}^{q}(U)
  =
  \left(
    \Obs_{\hCS}^{\cl}(U)[[\hbar]],
    d_{\bar\partial}+d_{[,]}+\hbar\Delta_{\BV}
      +\sum_{\ell\ge 1}\hbar^\ell I_\ell
  \right)
\]
provided the degree-\(4\) invariant-polynomial obstruction vanishes or is
canceled by extra matter/counterterm data.

Proof obligations: compute the quartic Casimir/anomaly class for the
chosen gauge dg Lie algebra; specify the renormalization scheme and
propagator on polydiscs; prove QME; show the \(\hbar\)-filtration is
compatible with chiral factorization and with the Hall completion.

Anchors: CFG `2025draft.tex:1830-1955`;
`chapters/theory/cy3_chain_level_bridge.tex:203-225`, `294-317`.

### Cycle 7 -- Transfer from topological CS to holomorphic CY\(_3\)

Claim attacked: CFG's ordinary \(3\)d CS \(E_3\)-algebra plus
factorization homology already proves the full chain-level \(\Phi_3\)
construction on compact CY\(_3\) inputs.

Failure mode: CFG proves a topological locally constant \(E_3\)-algebra
and its module/factorization-homology consequences for ordinary CS.
Vol III needs a holomorphic \(E_3\)-factorization algebra in three
complex variables, the specialization
\(\Phi_3^{(\Sigma_2,C)}=\SpCh_{\Sigma_2,C}\circ\PhiFA_3\) to an
\(E_1\)-chiral curve output, and the open
\(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\) comparison.  CFG supplies neither
the compact CY\(_3\) analytic strictification nor the Hall orientation
data.

Surviving core: CFG is an excellent associated model for how BV
quantization, local observables, \(E_3\)-operations, modules, and
factorization homology should interact once the correct hCS object has
been built.

Healed statement with epistemic status: The safe Vol III statement is:
\[
  \PhiFA_3(\mathcal C)
  \quad\text{is a conditional holomorphic }E_3\text{-factorization algebra,}
\]
\[
  \Phi_3^{(\Sigma_2,C)}(\mathcal C)
  =
  \SpCh_{\Sigma_2,C}(\PhiFA_3(\mathcal C))
  \quad\text{is the native }E_1\text{-chiral output,}
\]
and the Hall/quantum-group avatar requires
\[
  \PhiFA_3(\mathcal C)
  \xrightarrow{\Theta_{\hCS\to\Hall}^{\mathrm{or}}}
  \CoHA_{\mathrm{crit}}^{\mathrm{or}}(X)
  \to Y^+\to\mathcal D(Y^+)\to\mathcal W_{1+\infty}.
\]
The first arrow remains open in general.

Proof obligations: prove the Dolbeault \(E_3\) chiral envelope; prove
compact CY\(_3\) analytic/gluing strictification; construct the
hCS-to-Hall natural transformation; prove specialization to \(E_1\) on
the curve preserves the needed OPE data; only then import CFG-style
module/factorization-homology arguments.

Anchors: `chapters/theory/cy_to_chiral.tex:4-41`, `271-294`,
`4680-4792`; `chapters/theory/cy3_chain_level_bridge.tex:45-68`,
`227-291`.

## Claims to Preserve

1. Preserve the warning `warn:cy3-no-cfg-shortcut`.  CFG 2026 is not a
   proof of \(\Theta_{\hCS\to\Hall}\).
2. Do not write the CY\(_3\) local object as ordinary \(C^*(\mathfrak g)\)
   except when explicitly naming the locally constant/topological
   associated model.
3. The exact local CY\(_3\) formula must keep
   \(\mathfrak g[[z_1,z_2,z_3]]\), or its analytic version
   \(\mathfrak g\otimes\mathcal O(U)\), after Dolbeault contraction.
4. Constant ghosts are a summand of the holomorphic-jet ghost sector, not
   the full sector.
5. The \(E_3\) object is Stage 1.  The final curve-specialized Vol III
   output at \(d=3\) is native \(E_1\), with \(E_2\) braiding recovered
   through the Drinfeld center when it exists.

## Remaining Open Obligations

- Prove the Dolbeault DVS CE formula for hCS local observables on
  polydiscs with continuous duals and compact-support conventions fixed.
- Construct the multidirectional chiral OPE calculus over
  \(\mathbb C^3\), including triple-collision coherences and the three
  commuting OPE residue differentials.
- Prove the \(E_3\) Dolbeault bar--chiral-CE identification
  \(B_{E_3}(U^{\ch,E_3}_\hbar(\mathfrak L))\simeq
  \CE_{*,\ch}^{E_3}(\mathfrak L)\).
- Compute/cancel the degree-\(4\) hCS anomaly for each gauge datum used
  in the CY\(_3\) bridge.
- Construct \(\Theta_{\hCS\to\Hall}^{\mathrm{or}}\) with orientation,
  shift, Tate twist, charge/HN completion, equivariant localization, and
  Thom--Sebastiani compatibility.

## Verification Run

Command:
`python3 -m pytest compute/tests/test_s3_framing_chain_level.py compute/tests/test_dolbeault_cy3_homotopy.py compute/tests/test_e1_e2_obstruction_cy3.py compute/tests/test_holomorphic_cs_chiral_engine.py compute/tests/test_factorization_categories_chiral.py -q`

Result: 451 passed in 2.87s.

Files changed: this report only.
