# Agent 15: hostile synthesis / integration adversary

Scope: whole-conception attack on chambered effective BPS positive geometry.
Owned output only:
`notes/adversarial_bps_positive_geometry_20260424/agent_15_hostile_synthesis.md`.
No manuscript files edited.

Files read:

- `CLAUDE.md`
- `AGENTS.md`
- `chapters/theory/quantum_groups_foundations.tex`
- `chapters/examples/coha_wall_crossing_platonic.tex`
- all reports `notes/adversarial_bps_positive_geometry_20260424/agent_*.md`

Compatibility axes checked: foundations, PBW, Drinfeld double, KS
scattering, toric degeneration, BV/factorization, physics
interpretations, descent/NCCR, K3xE/BKM, categorical centers, spectral
networks, compute evidence recorded by the reports.

## Executive verdict

The current universal reading is false:
\[
  \PBPS_\sigma(X)
  =
  (\Gamma_X,\Gamma^+_{\mathrm{eff},\sigma},\Meff_\sigma,\phi_W,
  \Omega_\sigma,\mathfrak D^{\mathrm{KS}}_\sigma,\Theta^{\mathrm{BPS}}_\sigma)
\]
is not a universally constructed object. It contains nonminimal and
sometimes nonconstructed data: theta basis, motivic/classical wall factor,
support property, strict sector, orientation sign, equivariance group,
critical atlas, and completion topology are all load-bearing.

The core survives as a relative, oriented, sector-completed Hall-scattering
datum, plus a separate theta enhancement where constructed. The toric case
is the terminal rational-polyhedral degeneration. The full quantum group is
not \(Y^+\); it is a completed Hall--Drinfeld double only after PBW,
Cartan, negative half, coproduct, completion, and nondegenerate Hall pairing.
The K3xE/BKM face is non-toric Lorentzian/Humbert automorphic data, not
twenty-four copies of \(\mathbb C^3\), not a toric shuffle character, and not
an unconditional Hall--BKM algebra theorem.

## ATTACK/HEAL cycle 1 -- foundational object

Attacked global claim. Effective BPS positive geometry is the tuple at
`quantum_groups_foundations.tex:15-78`, with
\(\Theta^{\mathrm{BPS}}_\sigma\) included as one component.

Strongest fatal objection. The tuple is not well-typed. Lines 23-26 fix
orientation data and a critical atlas, but the tuple records neither
orientation sign nor atlas. Lines 44-49 define the effective monoid by
nonzero \(\Omega_\sigma\), while \(\Omega_\sigma\) is defined only later by
integration over \(\phi_W\). Lines 65-71 call a classical
\(\exp(\Omega\operatorname{Li}_2(e_\gamma))\) expression an automorphism of
the completed quantum torus. Lines 73-76 include a theta basis while saying
it is conjectural for general compact CY3 chambers. A tuple with an
unconstructed component is not a constructed object.

Healed formulation. The minimal object is a relative BPS Hall-scattering
datum. Fix
\[
  (\sigma,S,o,Q,T_{\mathrm{eq}},\mathfrak A,\bullet),
  \qquad \bullet\in\{\mathrm{mot},\mathrm{cl}\},
\]
where \(S\subset\mathbb C^*\) is a strict sector, \(o\) is orientation data,
\(Q\) is a support-property quadratic form, \(T_{\mathrm{eq}}\) is the
geometry-specific equivariance group, and \(\mathfrak A\) is an oriented
derived critical atlas. Set
\[
  \Gamma_X^{\mathrm{or}}
  =
  (K^{\mathrm{num}}_0(\mathcal C),\langle-,-\rangle,\varepsilon_o),
\]
\[
  \Gamma^{\mathrm{ss}}_{\sigma,S}
  =
  \{\gamma: Z_\sigma(\gamma)\in S,\ \mathcal M_\sigma(\gamma)\ne\varnothing,
  \ Q(\gamma)\ge 0\},
\]
\[
  \Gamma^{\mathrm{BPS},\bullet}_{\sigma,S,o}
  =
  \{\gamma\in\Gamma^{\mathrm{ss}}_{\sigma,S}:
  \Omega^\bullet_{\sigma,o}(\gamma)\ne0\},
  \qquad
  \Gamma^+_{\sigma,S,o}
  =
  \mathbb N\langle\Gamma^{\mathrm{BPS},\bullet}_{\sigma,S,o}\rangle .
\]
The positive stack is indexed by \(\Gamma^{\mathrm{ss}}\); the completion
monoid is \(\Gamma^+\). The theta basis is a later enhancement:
\[
  \mathfrak P^{\mathrm{BPS},\bullet,+\theta}_{\sigma,S,o,T}
  =
  (\mathfrak P^{\mathrm{BPS},\bullet}_{\sigma,S,o,T},
  \Theta^{\mathrm{BPS},\bullet}_{\sigma,S,o,T})
\]
only when broken-line, GMN, or Hall-factorization construction exists.

Precise manuscript edit recommendation. Replace Definition
`def:universal-positive-geometry-grammar` at
`quantum_groups_foundations.tex:15-78` by the relative datum above. Replace
the positive-half definition at lines 80-93 by
\[
  Y^+_{\sigma,S,o,T}(X)
  =
  \widehat{\bigoplus}_{\gamma\in\Gamma^{\mathrm{ss}}_{\sigma,S}}
  H^\bullet_{T_{\mathrm{eq}}}
  (\mathcal M_\sigma^{\mathfrak A}(\gamma),\phi_{\mathfrak A,o})
\]
with Hall product when the critical correspondence is constructed. Move
\(\Theta^{\mathrm{BPS}}\) into a separate theta-enhancement definition.

Status. Definition-grade conditional datum. Theta enhancement: theorem-grade
in toric/cluster/class-S/Hitchin charts; conjectural for a general compact
CY3 chamber.

## ATTACK/HEAL cycle 2 -- KS scattering and motivic/classical ambients

Attacked global claim. The KS scattering diagram in the tuple is fully
specified by walls carrying
\[
  \exp(\Omega_\sigma(\gamma)\operatorname{Li}_2(e_\gamma)).
\]

Strongest fatal objection. The displayed factor is the classical
Euler-specialized Hamiltonian shadow, not the motivic quantum-torus wall
factor. `coha_wall_crossing_platonic.tex:428-465` separates the motivic
quantum ambient
\[
  x_\alpha x_\beta
  =
  \mathbb L^{\langle\alpha,\beta\rangle/2}x_{\alpha+\beta}
\]
from the classical bracket. Lines 571-577 state wall-crossing as equality
of phase-ordered motivic quantum-dilogarithm products before logarithms are
taken. Lines 597-644 show that the exact pentagon contains the bound-state
cocycle \(q^{-1/2}x_0x_1\), which disappears in the classical limit.

Healed formulation. For a strict sector \(V\), use
\[
  A_V(\sigma)
  =
  \prod_{\ell\subset V}^{\curvearrowright}
  \prod_{Z_\sigma(\gamma)\in\ell}
  \mathbb E(x_\gamma)^{\Omega^{\mathrm{mot}}_{\sigma,o}(\gamma)}
  \in \widehat{\mathbb T}^{\mathrm{mot}}_{\Gamma,V}.
\]
The classical wall automorphism is the specialization
\[
  \mathcal K_\gamma^{\mathrm{cl}}(e_\eta)
  =
  e_\eta
  (1-\varepsilon_o(\gamma)e_\gamma)^{
  \Omega^{\mathrm{cl}}_{\sigma,o}(\gamma)\langle\gamma,\eta\rangle}.
\]
The support property is part of the datum: there is \(Q\) negative on
\(\ker Z\) and \(Q(\gamma)\ge0\) for all active \(\gamma\), equivalently
\(\|\gamma\|\le C|Z(\gamma)|\).

Precise manuscript edit recommendation. At
`quantum_groups_foundations.tex:65-72`, replace the single Li2 formula by
two clauses: motivic quantum wall factor and classical Euler specialization.
At `quantum_groups_foundations.tex:172-187`, make strict-sector completion,
support property, and phase-ordered HN factorization explicit before
claiming local finiteness or consistency.

Status. KS wall-crossing: theorem under KS/Joyce/Bridgeland stability,
orientation, support, and HN hypotheses. Compact K3xE motivic scattering:
conditional/conjectural. BCH/log MC expressions: diagnostic shadows, not
DT multiplicity formulae at height \(\ge3\).

## ATTACK/HEAL cycle 3 -- PBW and Drinfeld double

Attacked global claim. The quantum group is simply
\[
  G_\sigma(X)=D(Y^+_\sigma(X)).
\]

Strongest fatal objection. PBW is not a double. Davison--Meinhardt PBW gives
a positive-half filtration:
\[
  \operatorname{gr}_F\mathcal H_{\sigma,\mu}^{\mathrm{crit}}
  \cong
  \operatorname{Sym}_{\mathrm{super}}
  (\operatorname{BPS}_{\sigma,\mu}\otimes H^\bullet(B\mathbb C^*)).
\]
The Drinfeld double also requires a continuous coproduct/antipode or
topological bialgebra substitute, a Serre-dual negative half, a Cartan
completion, and a nondegenerate Hopf pairing. `quantum_groups_foundations.tex:
96-126` already marks this conditional; `coha_wall_crossing_platonic.tex:
1419-1432` overstates that an abstract double is always available.

Healed formulation. The actual object is
\[
  G^{\mathrm{Hall}}_{\sigma,S}(X)
  =
  D_{\sigma,S}
  \left(\widehat{Y^+_{\sigma,S}}(X),
  Y^0_\sigma(X),\langle-,-\rangle_{\sigma,S}\right),
\]
\[
  =
  \widehat{Y^-_{\sigma,S}}(X)\widehat{\bowtie}
  Y^0_\sigma(X)\widehat{\bowtie}
  \widehat{Y^+_{\sigma,S}}(X),
\]
where
\[
  Y^0_\sigma(X)=k((\hbar))[[\Gamma_X]]_\chi,\qquad
  K_\gamma y_\delta K_\gamma^{-1}
  =
  q^{\langle\gamma,\delta\rangle}y_\delta .
\]
The pairing must be stated, for example
\[
  \langle\alpha,\beta\rangle_{\sigma,\gamma}
  =
  \int_{\mathcal M_\sigma(\gamma)}
  \alpha\cup\mathbb D_{\mathrm{Serre}}(\beta)\cap\phi_{\mathfrak A,o},
\]
and quotient by its radical if necessary before doubling.

Precise manuscript edit recommendation. Strengthen
`thm:quantum-group-as-positive-geometry-double` at
`quantum_groups_foundations.tex:96-127` by naming strict-sector completion,
Cartan half, negative half, continuous Hopf pairing, radical quotient, and
topological bialgebra/Hopf structure. Replace the phrase at
`coha_wall_crossing_platonic.tex:1421-1428` with: "the formal dual tensor
product is available; the Drinfeld double is defined only after a compatible
nondegenerate continuous Hopf pairing and completion."

Status. \(\mathbb C^3\): theorem-grade after Schiffmann--Vasserot plus
Prochazka--Rapcak double/evaluation. Standard toric no-compact-4-cycle
positive halves: theorem-grade in RSYZ scope; full named double conditional
on pairing outside proved cases. K3xE: character theorem-grade, Hall--BKM
double conditional.

## ATTACK/HEAL cycle 4 -- toric degeneration, descent, and NCCR

Attacked global claim. Toric/NCCR local data glue globally by pairwise
wall-crossing, and the toric fan is the template for general positive
geometry.

Strongest fatal objection. The toric formula is precise but narrow:
`quantum_groups_foundations.tex:129-170` gives
\[
  \Gamma^+_{\mathrm{eff},\sigma}(X_\Sigma)=\mathbb Z_{\ge0}^{Q_0},
  \qquad
  \Meff_\sigma(X_\Sigma)
  =
  \coprod_{\mathbf d\in\mathbb Z_{\ge0}^{Q_0}}
  [\operatorname{Crit}(W_{\mathbf d})/G_{\mathbf d}],
\]
\[
  Y^+_\sigma(X_\Sigma)=\operatorname{CoHA}(Q_\Sigma,W_\Sigma).
\]
The monoid is indexed by vertices \(Q_0\), not arrows, roots, or Mori
generators. Descent is not pairwise wall-crossing alone: a local NCCR
atlas needs geometric opens, Jacobi algebras, derived Morita bimodules,
triple-overlap 2-cells, and an independent \(\mathbb Z/2\) orientation
gerbe. Ordinary Cech descent and Weiss/Ran factorization descent have
different targets.

Healed formulation. Keep two descent outputs:
\[
  Y^{+,\mathrm{QC}}_\sigma(X)
  =
  \operatorname{Tot}\check C^\bullet
  (\mathfrak U,\operatorname{CoHA}(\Lambda_\alpha,o_\alpha)),
\]
with transitions
\[
  T_{\alpha\beta}\in\operatorname{DPic}(\Lambda_{\alpha\beta}),
  \qquad
  T_{\beta\gamma}\otimes^\mathbb L T_{\alpha\beta}
  \simeq T_{\alpha\gamma},
\]
and orientation cocycle \(\delta o\in\check C^2(\mathfrak U,\mathbb Z/2)\).
The factorization target is
\[
  Y^{+,\mathrm{FA}}_\sigma(X)
  =
  \operatorname{hocolim}_{\mathfrak U^\sqcup}
  \Phi^{\mathrm{FA,or}}_3(U_\alpha).
\]
The comparison \(Y^{+,\mathrm{QC}}\to Y^{+,\mathrm{FA}}\) is an equivalence
only for Weiss covers or after proving higher configuration data trivial.

Precise manuscript edit recommendation. In the positive-geometry paragraph
`coha_wall_crossing_platonic.tex:1500-1519`, replace "the BPS positive
basis" by "the BPS positive basis where constructed, conjectural otherwise."
In the toric descent material, insert the two-target descent remark proposed
by Agent 10. Any theorem saying pairwise wall-crossing determines global
descent must be restricted to two-chart covers or supplemented with the
derived-Picard and orientation triple cocycles.

Status. Toric terminal degeneration: proved on standard toric Hall loci.
Conifold: global Klebanov--Witten NCCR is a global presentation, not a
chart. Local \(\mathbb P^2\): real triple-overlap/equalizer case.
Generic compact CY3, quintic, generic K3xE: no toric/NCCR fan; use the
relative BPS datum instead.

## ATTACK/HEAL cycle 5 -- BV/factorization and the Hall comparison

Attacked global claim. Costello--Gwilliam/Costello--Li locality or 5d hCS
proves \(\PhiFA_3(X)=\operatorname{CoHA}(X)\), and the K3xE boundary is
chain-level \(\mathbf H_{\Delta_5}\).

Strongest fatal objection. The Costello side and Hall side live in different
categories. The Hall side uses oriented critical CoHA
\[
  \operatorname{CoHA}^{\mathrm{or}}_{\mathrm{crit}}(U)
  =
  \bigoplus_{\mathbf d}
  H^{\mathrm{BM}}_{G_{\mathbf d}}
  (\operatorname{Crit}(\operatorname{Tr}W_{U,\mathbf d}),
  \phi_{\operatorname{Tr}W_{U,\mathbf d}}\otimes\mathscr L_{o_U}).
\]
The Costello side supplies holomorphic/topological factorization
observables under BV anomaly, CY form, and locality hypotheses. The missing
identification is an oriented comparison
\[
  \Theta_{\mathrm{hCS}\to\mathrm{Hall}}^{\mathrm{or}}
  :
  \operatorname{Obs}_{\mathrm{hCS}}^q(-,\mathfrak g)
  \longrightarrow
  \operatorname{CoHA}_{\mathrm{crit}}^{\mathrm{or}}(-).
\]
`quantum_groups_foundations.tex:5869-5913` asserts an on-the-nose
boundary identity
\[
  \iota^*\mathcal F_{T_{\mathrm{HT}}[K3\times E]}\simeq\mathbf H_{\Delta_5}
\]
as `ProvedHere`, but the proof matches characters and frameworks rather
than constructing the chain map.

Healed formulation. Stage 1 \(\PhiFA_3\) is a Costello/factorization object
under its H1--H4/framing hypotheses. The Hall equality is a Hall-side theorem
in the constructed local charts. Their identification is conditional on
\(\Theta_{\mathrm{hCS}\to\mathrm{Hall}}^{\mathrm{or}}\), compatible with
orientation, Thom--Sebastiani, descent, BV bracket/Hall product, and the
\(\mathbb C^3\) terminal chart.

Precise manuscript edit recommendation. Insert a "Costello--Hall comparison
hypothesis" before any \(\PhiFA_3\to\operatorname{CoHA}\) conclusion.
Downgrade `prop:qgfnd-clp-3d-ht-k3e-boundary-chiral-algebra` at
`quantum_groups_foundations.tex:5869-5965` from `ProvedHere` to conditional
unless an explicit boundary factorization chain map is supplied. Keep the
framework theorem that a constructed HT boundary has \(E_1\)-chiral
observables.

Status. Local \(\mathbb C^3\) Hall equality: proved elsewhere. Stage 1
Costello locality: theorem under stated BV/framing hypotheses. hCS-to-Hall
comparison: open/conditional in general. K3xE boundary \(\mathbf H_{\Delta_5}\)
chain equivalence: conditional.

## ATTACK/HEAL cycle 6 -- categorical center and MTC endpoint

Attacked global claim. CY-C yields
\[
  \Rep^{\mathrm{fd}}(C(\mathcal C,q))\simeq
  \mathcal MTC(A_\mathcal C),\qquad
  \mathcal MTC(A_\mathcal C)=\Rep^{E_2}(A_\mathcal C)^{\mathrm{ss}},
\]
with \(q\) determined by \(\kappa_{\mathrm{ch}}\).

Strongest fatal objection. At \(d=3\), \(A_\mathcal C\) is natively \(E_1\),
not \(E_2\). The braided object is one level up:
\[
  \mathcal Z(\Rep^{E_1}(A_\mathcal C)).
\]
At a root of unity, the full finite-dimensional \(\Rep_q(\mathfrak g)\) is
not the semisimple MTC; the MTC is the tilting/negligible quotient:
\[
  \mathcal MTC_q(\mathfrak g)
  =
  \operatorname{Tilt}_q(\mathfrak g)/\mathcal N_{\mathrm{negl}},
  \qquad
  q=\exp\left(\frac{\pi i}{d_\mathfrak g(k+h^\vee)}\right).
\]
Also \(q\) is fixed by level, lacing, framing, and \(R\)-matrix
normalization; \(\kappa_{\mathrm{ch}}\) is not enough.

Healed formulation. Define
\[
  \Rep^{E_2}_{\mathrm{cent}}(A)
  :=
  \mathcal Z(\Rep^{E_1}(A))
  \simeq
  \Rep^{E_2}(Z^{\mathrm{der}}_{\mathrm{ch}}(A)).
\]
If this braided tensor category is rigid, finite, ribbon, and factorizable,
set
\[
  \mathcal MTC(A)
  :=
  \Rep^{E_2}_{\mathrm{cent}}(A)/\mathcal N_{\mathrm{negl}}.
\]
In the non-semisimple root-of-unity regime retain a finite tensor category
with modified trace instead of forcing semisimplicity.

Precise manuscript edit recommendation. At
`quantum_groups_foundations.tex:509-524`, replace "q determined by
\(\kappa_{\mathrm{ch}}\)" by "q determined by the full
level/framing/lacing/\(R\)-matrix normalization." Replace the definition
of \(\mathcal MTC(A_\mathcal C)\) by the central category formula above.
At lines 372-390, name the tilting subcategory explicitly in the
root-of-unity proposition, not only in proof attribution.

Status. Drinfeld center formalism and KL/Finkelberg root-of-unity endpoint:
proved elsewhere. CY-C at \(d=3\): conjectural except explicit local Hall
loci with double and center passage.

## ATTACK/HEAL cycle 7 -- K3xE, BKM, and automorphic boundary

Attacked global claim. Toric positivity extends to K3xE; the CoHA equals
\(\mathfrak g_{\Delta_5}\); \(\Delta_5\) is a VOA/black-hole character; the
MO wall is the BKM wall; the four \(\kappa_\bullet\) values add.

Strongest fatal objection. K3xE is non-toric Lorentzian/Humbert data. The
theorem-grade character statement is
\[
  Z^{\mathrm{DT,red}}_{K3\times E,\beta}
  =
  -C/\Phi_{10}
  =
  -C/\Delta_5^2
\]
(`coha_wall_crossing_platonic.tex:1239-1308`). The Hall--BKM comparison is
conditional at `quantum_groups_foundations.tex:4445-4599`. The CoHA, if
identified, is the positive half only:
\[
  \operatorname{CoHA}(K3\times E)
  \simeq
  U(Y^+(\mathfrak g_{\Delta_5}))_{\mathrm{num}},
  \qquad
  \mathfrak g_{\Delta_5}=Y^-\oplus\mathfrak h\oplus Y^+.
\]
The BKM denominator is Lorentzian:
\[
  e^{-2\pi i(\rho,z)}
  \prod_{\alpha\in\Delta_+}
  (1-e^{-2\pi i(\alpha,z)})^{\operatorname{mult}\alpha}
  =
  \Delta_5(2Z)/64.
\]
The \(\mathbb C^3\) MO wall is positive-definite \(A_2\); the BKM wall is
a Lorentzian real-root hyperplane. `quantum_groups_foundations.tex:
6404-6418` explicitly separates them. The toric affine-chart contribution
to \(\kappa_{\mathrm{BKM}}\) is zero, while
\[
  \kappa_{\mathrm{BKM}}(\Delta_5)=c_1(0)/2=10/2=5.
\]

Healed formulation. K3xE has construction-distinct invariants:
\[
  \kappa_{\mathrm{cat}}(K3\times E)=
  \chi(\mathcal O_{K3})\chi(\mathcal O_E)=2\cdot0=0,
\]
\[
  \kappa_{\mathrm{ch}}(K3\times E)=
  \sum_{q=0}^3(-1)^q h^{0,q}=1-1+1-1=0,
\]
\[
  \kappa_{\mathrm{ch}}^{\mathrm{Heis}}=3,\qquad
  \kappa_{\mathrm{BKM}}(\Delta_5)=5,\qquad
  \kappa_{\mathrm{fiber}}(K3)=24.
\]
The useful package is \(\{0,3,5,24\}\), not an additive formula and not
\(\{2,3,5,24\}\) for the total space. The additive falsehood fails already:
\[
  \kappa_{\mathrm{BKM}}(\Delta_5)=5\ne
  \kappa_{\mathrm{ch}}(K3\times E)+\chi(\mathcal O_E)=0+0.
\]

Precise manuscript edit recommendation. Add an explicit status marker to
`coha_wall_crossing_platonic.tex:1533-1535`: conditional/conjectural beyond
reduced/abelian inputs. Keep `quantum_groups_foundations.tex:4445-4599` as
the status model. At `quantum_groups_foundations.tex:6147-6151`, replace
"unconditional geometric data" by "when the lattice, BPS spectrum, and
automorphic denominator are constructed." At lines 6285-6290, "terminal
object" should become "terminal degeneration" unless a morphism category is
supplied. At lines 6445-6460, remove "compact toric CY3" as a general
smooth-Calabi--Yau phrase and restrict to quasi-compact toric fixed-chart
localization.

Status. Safe theorem-grade: \(\Phi_{10}=\Delta_5^2\), reduced primitive
K3xE DT character, \(\kappa_{\mathrm{BKM}}(\Delta_5)=5\), and the
\(\{0,3,5,24\}\) four-subscript fingerprint. Conditional: motivic Hall
lift, Hall--BKM positive-half comparison, Hopf pairing/double, framed
\(\Phi_3^{(K3,E)}\) algebra comparison.

## ATTACK/HEAL cycle 8 -- physics, spectral networks, and compute evidence

Attacked global claim. The positive geometry is validated physically by
attractor MC gauge, AdS3/CFT2, black-hole degeneracy, Costello--Li--Paquette
boundary \(\mathbf H_{\Delta_5}\), and GMN spectral networks.

Strongest fatal objection. These are different status levels. The theorem
is the automorphic/enumerative denominator, not the whole quantum-gravity
state space. The black-hole index uses \(1/\Phi_{10}\); \(\Delta_5\) is the
chiral-half Borcherds denominator. The attractor-flow proposition at
`coha_wall_crossing_platonic.tex:2349-2356` asserts a canonical MC gauge
without a constructed map from split-flow trees to the KS gauge group. The
Chern--Simons dictionary at lines 2443-2462 is an analogy unless an action
functional comparison is supplied. The pentagon=Jacobi theorem at lines
2472-2484 is proved in the conifold/A2 computation, not globally. GMN
spectral networks require a UV curve, spectral cover, and Seiberg--Witten
differential; general CY3 positive geometry has none.

Healed formulation. Use the trichotomy:

- Theorem: DVV/Sen \(1/\Phi_{10}\) dyon index in its charge chamber;
  Oberdieck--Pixton reduced K3xE identity; DMVV symmetric-product elliptic
  genus; \(\Phi_{10}=\Delta_5^2\); toric/cluster/GMN theta bases in their
  constructed settings.
- Conditional: attractor MC gauge for a fixed charge after constructing
  split-flow-to-KS comparison; boundary \(\mathbf H_{\Delta_5}\) chain map;
  M-theory protected operator algebra; DT=Atiyah--Singer index.
- Metaphor: "\(\mathfrak g_{\Delta_5}\) is the boundary CFT" without a
  stress tensor, state space, and module category.

For class S, keep the two-step route:
\[
  I_{\mathrm{Schur}}[T[A_1,\Sigma_{0,24}]]
  \xrightarrow{\operatorname{av}_{M_{24}}}
  \phi^{K3}_{0,1}
  \xrightarrow{\operatorname{Borch}}
  \Delta_5.
\]
Do not assert \(I_{\mathrm{Schur}}=1/\Delta_5\). The corrected class-S data
are
\[
  (n_v,n_h)=(63,88),\quad
  c_{4d}=107/6,\quad
  a_{4d}=403/24,\quad
  c_{2d}=-214,\quad
  \operatorname{rk}_{\mathbb C}\mathcal B=21.
\]

Precise manuscript edit recommendation. Add `ClaimStatusConditional` or
`ClaimStatusHeuristic` to the physical statements in
`coha_wall_crossing_platonic.tex:2328-2488`. Reconcile all black-hole
entropy constants by first defining the discriminant convention. Keep every
black-hole count in \(\Phi_{10}\) unless explicitly labelled "chiral-half".
Treat GMN spectral-network positive bases as theorem-grade only in
class-S/Hitchin settings and as conjectural bridges for compact K3xE.

Status. Compute reports are compatible with the healed package:
Agent 01 reports `31 passed` on CoHA wall-crossing/conifold tests; Agent 04
reports `31 passed` on K3 Yangian adversarial tests; Agent 06 reports
`379 passed` across C3, conifold, local P2, toric DT, and CoHA
wall-crossing tests. Agent 15 ran no new tests and made no manuscript edits.

## Compatibility matrix

| Axis | Survives? | Required correction |
|---|---:|---|
| Foundations | Yes | relative datum with \(S,o,Q,T_{\mathrm{eq}},\mathfrak A,\bullet\); theta separate |
| PBW | Yes | positive-half PBW only; does not imply double or MTC |
| Drinfeld double | Yes | completion, Cartan, negative half, nondegenerate pairing, radical quotient |
| Scattering | Yes | motivic quantum torus first; classical Li2 only after specialization |
| Toric degeneration | Yes | terminal rational-polyhedral degeneration, vertex-indexed dimension vectors |
| Descent/NCCR | Yes, conditional | oriented Morita descent plus Weiss/Ran factorization descent |
| BV/factorization | Yes, conditional | insert \(\Theta_{\mathrm{hCS}\to\mathrm{Hall}}^{\mathrm{or}}\) comparison hypothesis |
| Categorical centers | Yes | \(E_2\) on \(\mathcal Z(\Rep^{E_1}(A))\), not on \(A\) at \(d=3\) |
| Physics | Partly | theorem/conditional/metaphor trichotomy; \(\Phi_{10}\) vs \(\Delta_5\) |
| Spectral networks | Partly | theorem in class-S/Hitchin; conjectural bridge for compact CY3 |
| K3xE/BKM | Yes, stratified | character theorem; Hall--BKM and double conditional; \(\{0,3,5,24\}\) |

## Minimal insertion blueprint

1. Replace the foundational definition in
   `quantum_groups_foundations.tex:15-78` by the relative
   Hall-scattering datum. Move theta basis to a separate enhancement.
2. Replace `quantum_groups_foundations.tex:80-93` by the sector-completed
   positive half \(Y^+_{\sigma,S,o,T}\), with explicit equivariance.
3. Strengthen `quantum_groups_foundations.tex:96-127` with double
   hypotheses: strict-sector completion, topological Hopf/coideal bialgebra,
   Cartan, negative half, nondegenerate pairing, radical quotient.
4. Repair `quantum_groups_foundations.tex:172-187` by naming support
   property, HN factorization, strict sectors, and theta-basis status.
5. Replace the CY-C endpoint at `quantum_groups_foundations.tex:509-524`
   by the central representation category definition; \(q\) requires full
   normalization data, not \(\kappa_{\mathrm{ch}}\) alone.
6. Soften representability prose at `quantum_groups_foundations.tex:718`,
   `775-783`, and `788`: accessible MO locus only; no global \(G(X)\) for
   arbitrary compact CY3.
7. Add conditional status at `coha_wall_crossing_platonic.tex:1533-1535`.
   The K3xE Hall--Drinfeld/R-matrix bridge is not theorem-grade as written.
8. Downgrade or split `coha_wall_crossing_platonic.tex:1729-1853` into
   theorem-grade K3 CoHA inputs plus conditional EK/period/Hall--Drinfeld
   comparison.
9. Add statuses to `coha_wall_crossing_platonic.tex:2328-2488`; conifold/A2
   computations stay theorem-grade, general attractor/CS/Stokes statements
   become conditional or heuristic.
10. Downgrade `quantum_groups_foundations.tex:5869-5965` unless the
    boundary chain map to \(\mathbf H_{\Delta_5}\) is constructed. Keep the
    \(\{0,3,5,24\}\) fingerprint at lines 6110-6133, but detach it from the
    unproved boundary identification.
11. Replace `quantum_groups_foundations.tex:6147-6151` by "when constructed"
    language for CY3 root data. Replace "terminal object" at lines 6285-6290
    by "terminal degeneration" unless a category is supplied.

## Final stable skeleton

```tex
\begin{definition}[Relative BPS Hall-scattering datum]
Let \(\mathcal C\) be a CY3 category. Fix a Bridgeland stability
\(\sigma=(Z,\mathcal P)\), a strict sector \(S\subset\mathbb C^*\),
orientation data \(o\), support form \(Q\), an oriented derived critical
atlas \(\mathfrak A\), an equivariance group \(T_{\mathrm{eq}}\), and
\(\bullet\in\{\mathrm{mot},\mathrm{cl}\}\). Put
\[
  \Gamma_X^{\mathrm{or}}
  =
  (K^{\mathrm{num}}_0(\mathcal C),\langle-,-\rangle,\varepsilon_o).
\]
Define \(\Gamma^{\mathrm{ss}}_{\sigma,S}\),
\(\Gamma^{\mathrm{BPS},\bullet}_{\sigma,S,o}\), and
\(\Gamma^+_{\sigma,S,o}\) as above. The relative BPS Hall-scattering datum
is
\[
\mathfrak P^{\mathrm{BPS},\bullet}_{\sigma,S,o,T_{\mathrm{eq}}}(X)
=
(\Gamma_X^{\mathrm{or}},Q,\Gamma^{\mathrm{ss}}_{\sigma,S},
\Gamma^{\mathrm{BPS},\bullet}_{\sigma,S,o},\Gamma^+_{\sigma,S,o},
\mathcal M^{\mathfrak A}_{\sigma,S},\phi_{\mathfrak A,o},
\mathrm{BPS}_{\sigma,o},\Omega^\bullet_{\sigma,o},
\widehat{\mathbb T}^{\bullet}_{\Gamma,S},
\mathfrak D^{\mathrm{KS},\bullet}_{\sigma,S,o}).
\]
\[
  Y^+_{\sigma,S,o,T_{\mathrm{eq}}}(X)
  =
  \widehat{\bigoplus}_{\gamma\in\Gamma^{\mathrm{ss}}_{\sigma,S}}
  H^\bullet_{T_{\mathrm{eq}}}
  (\mathcal M^{\mathfrak A}_\sigma(\gamma),\phi_{\mathfrak A,o}).
\]
The theta-enhanced positive geometry is this datum plus a constructed
theta basis; it is not part of the minimal datum.
\end{definition}

\begin{theorem}[Toric terminal degeneration]
For a toric CY3 \(X_\Sigma\) with quiver with potential
\((Q_\Sigma,W_\Sigma)\) in a toric chamber,
\[
  \Gamma^{\mathrm{ss}}_{\sigma,S}
  =
  \Gamma^+_{\sigma,S,o}
  =
  \mathbb Z_{\ge0}^{Q_0},
  \qquad
  \mathcal M^{\mathfrak A}_{\sigma,S}
  =
  \coprod_{\mathbf d\in\mathbb Z_{\ge0}^{Q_0}}
  [\operatorname{Crit}(\operatorname{Tr}W_{\mathbf d})/G_{\mathbf d}],
\]
\[
  Y^+_{\sigma,S,o,T}(X_\Sigma)
  =
  \operatorname{CoHA}(Q_\Sigma,W_\Sigma).
\]
For \(X=\mathbb C^3\), this is \(Y^+(\widehat{\mathfrak{gl}}_1)\), not
\(\mathcal W_{1+\infty}\). The full affine Yangian is obtained only after
the Drinfeld double.
\end{theorem}

\begin{theorem}[Conditional Hall--Drinfeld double]
Assume \(Y^+_{\sigma,S,o,T}(X)\) has Davison--Meinhardt PBW integrality,
a compatible completed coproduct, a Serre-dual negative half, a Cartan
completion \(Y^0_\sigma(X)\), and a nondegenerate continuous Hall pairing
after quotienting its radical. Then
\[
  G^{\mathrm{Hall}}_{\sigma,S}(X)
  =
  \widehat{Y^-_{\sigma,S}}(X)\widehat{\bowtie}
  Y^0_\sigma(X)\widehat{\bowtie}
  \widehat{Y^+_{\sigma,S}}(X).
\]
The braided representation category is read from
\(\mathcal Z(\Rep^{E_1}(Y^+_{\sigma,S,o,T}(X)))\) or from the double where
the centre comparison is constructed.
\end{theorem}

\begin{theorem}[K3xE automorphic character and conditional Hall--BKM lift]
For \(X=K3\times E\), the theorem-grade character identity is
\[
  Z^{\mathrm{DT,red}}_{K3\times E}
  =
  -C/\Phi_{10}
  =
  -C/\Delta_5^2,
  \qquad
  \kappa_{\mathrm{BKM}}(\Delta_5)=c_1(0)/2=5.
\]
The four construction-distinct invariants are
\[
  \kappa_{\mathrm{cat}}(K3\times E)=0,\quad
  \kappa_{\mathrm{ch}}^{\mathrm{Heis}}=3,\quad
  \kappa_{\mathrm{BKM}}(\Delta_5)=5,\quad
  \kappa_{\mathrm{fiber}}(K3)=24.
\]
The comparison
\[
  \operatorname{CoHA}(K3\times E)
  \simeq
  U(Y^+(\mathfrak g_{\Delta_5}))_{\mathrm{num}}
\]
and its Drinfeld double are conditional on the motivic Hall lift,
Hall--BKM comparison, Cartan/negative half, and nondegenerate Hall pairing.
\end{theorem}
```

## Final status

CONVERGED for synthesis. The concept survives only after the above
relativization and status separation. The false object is the unconditional
global tuple with theta basis and quantum group already built in.

Files changed: this note only. No build run.
