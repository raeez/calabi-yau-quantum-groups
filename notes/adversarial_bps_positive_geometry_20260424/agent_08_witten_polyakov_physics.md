# Agent 08: Witten--Polyakov Physics Axis

Scope: physical BPS, topological holography, and quantum-gravity claims
around the effective BPS positive geometry.  Owned file only.  No manuscript
files were edited.

## Surface Read

- `CLAUDE.md` and `AGENTS.md`: four-\(\kappa_\bullet\) discipline,
  \(d=3\) output is \(E_1\)-chiral, \(E_2\) lives on the derived centre,
  \(G(X)\) is unconstructed in general, and physics claims must be
  labelled theorem / heuristic / metaphor.
- `chapters/examples/coha_wall_crossing_platonic.tex:1239-1308`:
  reduced \(K3\times E\) DT identity
  \(Z^{\mathrm{DT,red}}=-C/\Phi_{10}=-C/\Delta_5^2\), with
  \(\kappa_{\mathrm{BKM}}(\Delta_5)=c_1(0)/2=5\) and
  \(\kappa_{\mathrm{ch}}(K3\times E)=0\).
- `chapters/examples/coha_wall_crossing_platonic.tex:1500-1519`:
  non-toric BPS positive geometry and conditional Drinfeld double.
- `chapters/examples/coha_wall_crossing_platonic.tex:2328-2484`:
  attractor mechanism as MC gauge, Chern--Simons analogy, Stokes analogy,
  and pentagon \(=\) Jacobi.
- `chapters/examples/k3e_cy3_programme.tex:1505-1605`:
  black-hole entropy and Rademacher formula.
- `chapters/examples/k3e_cy3_programme.tex:1656-1742`:
  Costello--Li boundary algebra \(A_E\), explicitly heuristic.
- `chapters/examples/k3e_cy3_programme.tex:1834-1894`:
  BKM root multiplicities from \(2\phi_{0,1}\).
- `chapters/examples/k3e_cy3_programme.tex:4038-4058`:
  CHL AdS\(_3\)/CFT\(_2\) throat and dyon degeneracy.
- `chapters/examples/k3e_cy3_programme.tex:4706-4761`:
  D-brane charge, twisted \(K^0_H\), and proposed DT \(=\) Atiyah--Singer
  index identity.
- `chapters/examples/k3e_cy3_programme.tex:4765-4904`:
  M-theory brane/gravity algebra and conifold parent stratification.
- `chapters/theory/quantum_groups_foundations.tex:4806-4935`:
  \(E_1\)-chiral twisted holography, rejection of a
  \(\Delta_5\)-VOA.
- `chapters/theory/quantum_groups_foundations.tex:5842-6133`:
  Costello--Li--Paquette 3d HT QFT at \(K3\times E\), boundary
  \(\mathbf H_{\Delta_5}\), and four-subscript fingerprint.
- Existing local reports:
  `agent_01_foundations_gelfand.md`, `agent_02_beilinson_status.md`,
  `agent_03_drinfeld_double.md`, `agent_05_kontsevich_soibelman_scattering.md`,
  `agent_06_nekrasov_toric_degeneration.md`.
- Primary web anchors checked: DVV arXiv:hep-th/9607026 states a
  microscopic index formula whose asymptotic growth reproduces
  Bekenstein--Hawking entropy; Dabholkar--Murthy--Zagier arXiv:1208.4074
  states the single-centred / multi-centred mock-Jacobi decomposition;
  Banerjee--Gupta--Mandal--Sen arXiv:1106.0080 states that logarithmic
  corrections vanish for \(1/4\)-BPS \(N=4\) black holes in that
  supergravity setting.

## Verdict

The theorem-grade physical core is smaller than the manuscript surface
sometimes suggests:

1. The automorphic and enumerative denominator identities are theorem-grade
   in their stated loci:
   \[
     Z^{\mathrm{DT,red}}_{K3\times E}=-C/\Phi_{10}=-C/\Delta_5^2,\qquad
     \kappa_{\mathrm{BKM}}(\Delta_5)=5.
   \]
2. The standard \(N=4\) dyon-counting contour using \(1/\Phi_{10}\) is
   theorem-grade in the DVV / Sen / DMVV scope.
3. The statement that the same data constructs a boundary BKM Hilbert
   space, an \(AdS_3\) quantum-gravity CFT, an \(M\)-theory protected
   operator algebra, or a canonical attractor MC gauge is not theorem-grade.
   It is conditional or heuristic unless an independent mathematical
   construction of the relevant state space, stress tensor, module category,
   or gauge map is supplied.

The physical spine survives as a status-stratified diagram.  It does not
survive as a compound theorem.

## Theorem / Heuristic / Metaphor Trichotomy

**Theorem.**

- \(1/\Phi_{10}\) as the \(1/4\)-BPS dyon partition function in the
  standard \(N=4\) string-duality chamber.
- \(\Phi_{10}=\Delta_5^2\) and the Borcherds weight
  \(\kappa_{\mathrm{BKM}}(\Delta_5)=c_1(0)/2=5\).
- DMVV symmetric-product elliptic genus identity.
- Oberdieck--Pixton reduced \(K3\times E\) identity in the primitive
  reduced locus.
- Attractor-flow equations and split-flow trees as physical supergravity
  statements in their charge chambers.

**Heuristic / conditional.**

- Attractor MC gauge: conditional on a constructed map from split-attractor
  flow trees to the completed KS/MC gauge group.
- Costello--Li--Paquette boundary \(\mathbf H_{\Delta_5}\): conditional
  where the manuscript claims on-the-nose chain-level identification, unless
  the actual boundary factorization algebra is constructed and matched to
  the Borcherds presentation.
- \(AdS_3/CFT_2\) interpretation of \(\mathfrak g_{\Delta_5}\): heuristic
  beyond the standard symmetric-product and \(1/\Phi_{10}\) index.
- M-theory brane/gravity Koszul duality on \(K3\times E\): conjectural
  outside Costello's constructed local examples and the Loday--Quillen
  theorem.
- DT \(=\) twisted Atiyah--Singer index on \(\mathrm{Hilb}(K3\times E)\):
  conditional unless the twisted moduli space, orientation, and virtual
  Dirac index are constructed.

**Metaphor.**

- "\(\Delta_5\) is the black-hole partition function" without the
  holomorphic-half qualifier.
- "\(\mathfrak g_{\Delta_5}\) is the boundary CFT" without a stress tensor,
  state space, and module category.
- "Chern--Simons invariant \(=\) denominator identity" unless stated as
  a dictionary between MC-gauge invariants, not an equality of actions.
- "M5 or M2 worldvolume sigma model counts these states" unless recovered
  by an independent DT / stable-envelope / automorphic construction.

## ATTACK/HEAL Cycles

### Cycle 1: Attractor Flow as Canonical MC Gauge

ATTACK.  `coha_wall_crossing_platonic.tex:2349-2356` states that every
generic \(\Theta_A(t)\) is gauge-equivalent to an attractor representative
\(\Theta_A^*\), and that all stability conditions compatible with the
intrinsic spectrum lie in one gauge orbit.  This promotes a supergravity
flow-tree picture to a theorem in the modular convolution dg Lie algebra.

Failure mode.  Ferrara--Kallosh--Strominger and Denef supply physical
attractor-flow equations and split-flow trees.  They do not construct a
chain map
\[
  \mathrm{SplitFlow}_{\gamma}(t,t_*)\longrightarrow
  (\mathfrak g_A^{\mathrm{mod}})^0
\]
whose exponential is the KS wall-crossing gauge element.  Different charges
\(\gamma\) have different attractor points; there is no theorem placing all
charges in one universal MC orbit.

HEAL.  Downgrade the proposition to:

\[
  \Theta_A(t)\sim e^{\alpha_\gamma(t,t_*)}\cdot \Theta_A^*
  \quad\text{for a fixed charge \(\gamma\),}
\]
conditional on a constructed comparison from split-attractor trees to the
completed KS gauge group in a strict sector.  The theorem-grade statement is
KS wall-crossing as gauge equivalence under KS/Joyce/Bridgeland hypotheses.
The attractor representative is a physical gauge choice, not a canonical
mathematical representative until the comparison map is built.

Manuscript recommendation.  Add `\ClaimStatusHeuristic` or
`\ClaimStatusConditional` to `prop:phys-attractor-canonical`.  Replace
"Different attractor points for different total charges ... all in the same
gauge orbit" by "for a fixed charge and a constructed split-flow tree, the
corresponding MC representatives are expected to be gauge-equivalent."

### Cycle 2: Black-Hole Degeneracy Normalisation

ATTACK.  `k3e_cy3_programme.tex:1552-1594` claims
\[
  S_{\mathrm{BH}}=4\pi\sqrt{\Delta},\qquad
  \log d(\Delta)\sim 4\pi\sqrt{\Delta}-\tfrac32\log\Delta.
\]
The same file later states
\[
  \log d_N=2\pi\sqrt{\Delta/N}+(k_N+2)\log\Delta+\cdots
  \quad
  \text{with }\Delta=Q^2P^2-(Q\cdot P)^2
\]
at `k3e_cy3_programme.tex:4050-4054`, while
`wave12_d4_holographic_AdS3.tex:72-74` gives
\(\log d_1=\pi\sqrt{Q^2P^2-(Q\cdot P)^2}+\cdots\).

Failure mode.  The manuscript uses at least three discriminant
normalisations.  The physics theorem is not the bare number
\(4\pi\sqrt{\Delta}\); it is the DVV/Sen contour with a specified
definition of \(\Delta\), charges, and Fourier variables.  Without that
normalisation, the formula is not theorem-grade.

HEAL.  Use the contour as the theorem:
\[
  d(Q,P)=(-1)^{Q\cdot P+1}
  \oint_{\mathcal C}
  \frac{\exp[-i\pi(\rho Q^2+\sigma P^2+2v\,Q\cdot P)]}
       {\Phi_{10}(\rho,\sigma,v)}
  \,d\rho\,d\sigma\,dv,
\]
then define the discriminant once.  If
\(\Delta_{\mathrm{phys}}=Q^2P^2-(Q\cdot P)^2\), the standard leading
entropy should be written in the convention used by the cited theorem,
not mixed with a rescaled \(\Delta\).  If the manuscript wants
\(4\pi\sqrt{\Delta}\), it must define
\(\Delta=(Q^2P^2-(Q\cdot P)^2)/16\) or an equivalent rescaling.

Manuscript recommendation.  Replace the standalone
`prop:bmpv` formula by a convention-first proposition:
"Let \(\Delta_{\mathrm{DVV}}\) be defined by ... Then
\(\log d(Q,P)\sim ...\)."  Reconcile
`k3e_cy3_programme.tex:1552-1594`, `:4038-4058`,
`notes/wave12_d4_holographic_AdS3.tex:72-74`, and
`notes/wave12_d5_quantum_gravity_BH.tex:29-42` before preserving any
coefficient \(1,2,4\) in front of \(\pi\sqrt{\Delta}\).

### Cycle 3: \(\Delta_5\) as Chiral Half vs \(\Phi_{10}\) as Gravity Index

ATTACK.  The physics prose often lets \(\Delta_5\), \(\Phi_{10}\), and
\(\mathfrak g_{\Delta_5}\) trade places.  The black-hole index uses
\(1/\Phi_{10}\); the chiral BKM half has denominator \(\Delta_5\) and
\(\kappa_{\mathrm{BKM}}(\Delta_5)=5\).

Failure mode.  A holomorphic square root of a gravity partition function is
not itself the gravity partition function.  Promoting \(\Delta_5\) to the
full black-hole count loses the left/right or electric/magnetic doubling.

HEAL.  Keep the two formulas separate:
\[
  \Delta_5=\mathrm{Bo}(\phi_{0,1}),\qquad
  \kappa_{\mathrm{BKM}}(\Delta_5)=5,
\]
\[
  \Phi_{10}=\Delta_5^2,\qquad
  Z_{1/4\text{-BPS}}=1/\Phi_{10}.
\]
The surviving physical claim is: \(\Delta_5\) is the chiral-half
Borcherds denominator whose square gives the full Igusa form appearing in
the \(N=4\) dyon index.

Manuscript recommendation.  Every black-hole or quantum-gravity formula
should use \(\Phi_{10}\) unless explicitly labelled "chiral-half" or
"holomorphic square root".  The table entry
`S_{\mathrm{BH}}(\Delta) & 4\pi\sqrt{\Delta}` at
`k3e_cy3_programme.tex:2104` must be tied to the same discriminant
normalisation as the contour.

### Cycle 4: \(AdS_3/CFT_2\) and Boundary CFT Claims

ATTACK.  `k3e_cy3_programme.tex:1834-1844` says the boundary-to-sigma ratio
identifies modular characteristics on the two sides of \(AdS_3/CFT_2\);
`wave13_h5_holographic_QG_synthesis.tex:35-44` says the five projections
are "not analogies" and that the Gritsenko weight-\(5\) BKM character
determines the others.

Failure mode.  The theorem-grade \(AdS_3/CFT_2\) object is the
D1--D5 symmetric-product CFT and its DMVV elliptic genus.  The BKM algebra
\(\mathfrak g_{\Delta_5}\) gives a denominator and root multiplicities.
It does not by itself construct a unitary boundary CFT, a stress tensor,
or an equality of Hilbert spaces.  The local notes already mark the
BKM chiral-VOA interpretation as conjectural.

HEAL.  Replace "the same CFT" claims by a three-level statement:

- theorem: symmetric-product elliptic genera are Fourier coefficients of
  \(1/\Phi_{10}\);
- theorem: \(\Phi_{10}=\Delta_5^2\) is the Borcherds denominator identity;
- conjecture: \(\mathfrak g_{\Delta_5}\) acts as a chiral symmetry of a
  boundary sector whose character recovers the denominator.

Manuscript recommendation.  In any manuscript text derived from
`wave13_h5_holographic_QG_synthesis.tex:35-44`, replace "not analogies"
and "compound theorem" by "status-stratified synthesis".  Keep
\(AdS_3/CFT_2\) theorem-grade only for the standard D1--D5 /
\(\mathrm{Sym}^N(K3)\) sector and the DVV/Sen index.

### Cycle 5: Costello--Li--Paquette Boundary Algebra

ATTACK.  `quantum_groups_foundations.tex:5876-5913` labels as
`\ClaimStatusProvedHere` an on-the-nose chain-level identity
\[
  \iota^*\mathcal F_{T_{\mathrm{HT}}[K3\times E]}\simeq
  \mathbf H_{\Delta_5}
\]
as \(E_1\)-chiral algebras on \(E\).

Failure mode.  Costello--Gwilliam and Costello--Paquette supply a
factorization-algebra framework and specific holographic examples.  They do
not automatically identify the boundary algebra of compact
\(K3\times E\) twisted supergravity with the Borcherds BKM presentation.
Matching partition functions, weights, and Fock characters is evidence; it
is not a chain-level quasi-isomorphism of boundary factorization algebras.

HEAL.  The safe theorem is the operadic/factorization framework:
given a constructed \(3\)d HT theory on \(E\times\mathbb R_{\ge0}\), its
boundary observables form an \(E_1\)-chiral factorization algebra.  The
identification with \(\mathbf H_{\Delta_5}\) is conditional on an explicit
boundary calculation:
\[
  \mathrm{Obs}^{q,\partial}_{T_{\mathrm{HT}}[K3\times E]}
  \xrightarrow{\;\simeq\;}
  \mathbf H_{\Delta_5}
\]
preserving product, differential, charge grading, and Borcherds root
multiplicities.

Manuscript recommendation.  Downgrade
`prop:qgfnd-clp-3d-ht-k3e-boundary-chiral-algebra` from
`\ClaimStatusProvedHere` to conditional unless the proof supplies the
actual chain map.  Preserve the correct \(E_1\) vs \(E_2\) discipline:
\(\mathbf H_{\Delta_5}\) is \(E_1\)-chiral; \(E_2\) appears on
\(\mathcal Z(\mathrm{Rep}^{E_1}(\mathbf H_{\Delta_5}))\).

### Cycle 6: M-Theory Brane Interpretations

ATTACK.  `k3e_cy3_programme.tex:4769-4809` states that M-theory on
\(\mathbb R_t\times(K3\times E)\times\mathbb R^4\) with \(N\) M2-branes
produces brane and gravitational algebras in Koszul duality.  The
definition is physical; the conjecture is labelled, but surrounding prose
risks reading it as a theorem about \(K3\times E\).

Failure mode.  Loday--Quillen--Tsygan is theorem-grade for
\(\mathfrak{gl}_\infty(A)\) and cyclic homology.  Costello's holography
examples are theorem-grade in their constructed local settings.  They do
not construct the \(K3\times E\) M2 protected operator algebra, the large
\(N\) limit, or the BCOV gravity algebra as an actual dual pair.

HEAL.  Keep the M-theory paragraph in the same status discipline already
used for the conifold parent:

- theorem: Loday--Quillen--Tsygan open/closed trace;
- theorem/definition: \(A=\mathrm{End}_{\mathcal C}(\mathcal F)\) and
  cyclic homology in the CY category;
- conjecture: large-\(N\) brane/gravity Koszul duality on compact
  \(K3\times E\);
- metaphor: "M2-branes produce \(\mathbf H_{\Delta_5}\)" unless the
  protected-sector algebra is independently constructed.

Manuscript recommendation.  Add an explicit sentence after
`conj:phys-mth-koszul`: "The \(K3\times E\) brane/gravity duality is not
used as a proof of the BKM or CoHA statements; only the LQT cyclic-homology
shadow is theorem-grade."

### Cycle 7: D-Brane \(K\)-Theory and Atiyah--Singer Index

ATTACK.  `k3e_cy3_programme.tex:4725-4729` asserts a boxed equality
identifying \(Z^{K\text{-DT}}\) with a sum of twisted Atiyah--Singer
indices over \(K^0_H(X)\).  The later remark calls \(\Delta_{10}\) a
"hidden theorem" and says the AS-index lane proves the DT lane.

Failure mode.  The local formula passes through several unproved
identifications: torsion \(H\)-flux / Brauer class compatibility,
existence of the twisted moduli spaces, orientation and
\(\mathrm{Spin}^c\) data, equality of the virtual reduced
\(\chi_y\)-genus with a genuine Dirac index, and equivariance under the
duality group.  The statement may be true, but the manuscript does not yet
show a theorem-grade proof.

HEAL.  Downgrade the AS-index lane to conditional:
\[
  Z^{K\text{-DT}}(K3\times E)
  =
  \sum_\gamma
  \mathrm{ind}^{\mathrm{AS}}_\gamma(\mathcal D_\gamma)\,
  p^{\chi(\gamma)}q^{Q(\gamma)_{K3}}\tilde q^{Q(\gamma)_E}y^{J^R(\gamma)}
\]
provided the twisted stable-pair moduli stack carries the required
orientation, \(\mathrm{Spin}^c\) Dirac package, and virtual index theorem.

Manuscript recommendation.  Replace "Hidden theorem" by "Conditional
index interpretation".  Keep Minasian--Moore and Freed--Witten charge
corrections as theorem-grade physical inputs; do not let them imply the
full \(\Delta_{10}\) AS-index identity without the moduli-space theorem.

## Exact Downgrades

| Anchor | Current surface | Downgrade |
|---|---|---|
| `coha_wall_crossing_platonic.tex:2349-2356` | Attractor = canonical MC gauge representative | Heuristic/conditional for fixed charge and constructed split-flow-to-KS map |
| `coha_wall_crossing_platonic.tex:2362-2364` | Denominator form gauge-invariant throughout | Theorem only for constructed KS/MC moduli; heuristic for attractor-gauge reading |
| `coha_wall_crossing_platonic.tex:2443-2462` | Wall-crossing as Chern--Simons gauge equivalence | Metaphor/dictionary unless a functional and action comparison is supplied |
| `coha_wall_crossing_platonic.tex:2472-2484` | Pentagon = Jacobi at degree 3 | Proved in the conifold/\(A_2\) computation; conditional for general scattering diagrams |
| `k3e_cy3_programme.tex:1552-1594` | \(S_{\mathrm{BH}}=4\pi\sqrt\Delta\), \(I_{27/2}\) Rademacher formula | Theorem only after discriminant and Fourier-normalisation are reconciled |
| `k3e_cy3_programme.tex:1656-1707` | Costello--Li boundary \(A_E\), \(c=24\) | Already heuristic; keep heuristic and do not use as theorem in later deductions |
| `k3e_cy3_programme.tex:1834-1844` | \(AdS_3/CFT_2\) modular characteristics identify the BKM algebra | Theorem for DMVV/DVV denominator; conjecture for BKM boundary CFT |
| `k3e_cy3_programme.tex:4038-4058` | CHL throat formula with \(\Phi_{k_N}^2\) and \(2\pi\sqrt{\Delta/N}\) | Conditional on notation: define whether \(\Phi_{k_N}\) is the half-denominator or full CHL Siegel form |
| `k3e_cy3_programme.tex:4706-4761` | DT \(=\) twisted AS-index theorem | Conditional index interpretation |
| `k3e_cy3_programme.tex:4769-4809` | M-theory brane/gravity algebra production | Conjectural outside LQT/local Costello models |
| `quantum_groups_foundations.tex:4806-4883` | Costello--Paquette identifies \(\Phi_3(D^b\mathrm{Coh}(X))\) with boundary algebra | Conditional unless explicit boundary factorization algebra is computed |
| `quantum_groups_foundations.tex:5842-5965` | \(\iota^*\mathcal F\simeq\mathbf H_{\Delta_5}\) as `ProvedHere` | Conditional chain-level comparison |

## Manuscript Recommendations

1. Insert a convention block for black-hole discriminants before any entropy
   formula:
   \[
     \Delta_{\mathrm{phys}}=Q^2P^2-(Q\cdot P)^2
   \]
   or the chosen rescaling.  Then rewrite every
   \(\pi\sqrt\Delta\), \(2\pi\sqrt\Delta\), and \(4\pi\sqrt\Delta\)
   occurrence against that convention.
2. Replace every "same BKM boundary CFT" assertion by "same automorphic
   denominator / conjectural chiral symmetry" unless the stress tensor and
   module category are constructed.
3. Keep \(\Delta_5\) and \(\Phi_{10}\) separated:
   \(\Delta_5\) is chiral-half Borcherds data;
   \(\Phi_{10}=\Delta_5^2\) is the full dyon-counting form.
4. Downgrade the Costello--Li--Paquette \(K3\times E\) boundary
   identification to conditional, while preserving the theorem-grade
   framework that a constructed \(3\)d HT theory has \(E_1\)-chiral
   boundary observables.
5. Treat attractor-flow material as physics guidance attached to the KS
   theorem, not as a theorem constructing a canonical MC gauge.
6. Convert the D-brane \(K\)-theory / Atiyah--Singer paragraph into a
   conditional proposition with explicit hypotheses on the twisted moduli
   stack, orientation data, and virtual Dirac index.

## Surviving Formulas

\[
  \kappa_{\mathrm{ch}}(K3\times E)
  =
  \chi(\mathcal O_{K3\times E})
  =
  \chi(\mathcal O_{K3})\chi(\mathcal O_E)
  =
  2\cdot0=0.
\]

\[
  \kappa_{\mathrm{BKM}}(\Delta_5)=c_1(0)/2=10/2=5.
\]

\[
  \Phi_{10}=\Delta_5^2,\qquad
  Z_{1/4\text{-BPS}}=1/\Phi_{10}.
\]

\[
  Z^{\mathrm{DT,red}}_{K3\times E,\beta}
  =
  -C/\Phi_{10}
  =
  -C/\Delta_5^2
  \quad
  \text{in the Oberdieck--Pixton reduced primitive locus.}
\]

\[
  \mathrm{mult}_{\mathfrak g_{\Delta_5}}(\alpha)
  =
  2c_0(D_\alpha)
  \quad
  \text{in the \(2\phi_{0,1}\) convention.}
\]

These formulas survive the physical attack.  What does not survive is using
them to prove a quantum-gravity Hilbert space, a boundary BKM CFT, or a
canonical attractor MC gauge without the missing constructions.
