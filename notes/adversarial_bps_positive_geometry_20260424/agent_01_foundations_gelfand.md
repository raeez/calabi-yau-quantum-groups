# Agent 01 foundations report: effective BPS positive geometry

Gelfand-Manin axis. Object attacked:
\[
  \mathfrak P^{\mathrm{BPS}}_\sigma(X)
  =
  (\Gamma_X,\Gamma^+_{\mathrm{eff},\sigma}(X),
  \mathcal M^+_{\mathrm{eff},\sigma}(X),\phi_W,
  \Omega_\sigma,\mathfrak D^{\mathrm{KS}}_\sigma,
  \Theta^{\mathrm{BPS}}_\sigma).
\]

Scope is only the foundations of the object. No manuscript files were
edited.

## Local surface read

- `AGENTS.md`: mathematics mission, HZ-7 discipline, CY-C remains
  conjectural, CoHA is the positive half, and theorem-status labels do
  not repair missing constructions.
- `CLAUDE.md`: positive-geometry grammar
  \(Y^+(X)=H^\bullet_{\mathrm{eq}}(\mathcal M^+_{\mathrm{eff}}(X),\phi_W)\),
  \(G(X)=D(Y^+(X))\), four equivariance strata, CoHA positive-half
  discipline, and \(d=3\) native \(E_1\) scope.
- `chapters/theory/quantum_groups_foundations.tex:15-78`: current
  definition of \(\mathfrak P^{\mathrm{BPS}}_\sigma(X)\).
- `chapters/theory/quantum_groups_foundations.tex:80-114`: positive
  half and conditional Drinfeld double.
- `chapters/theory/quantum_groups_foundations.tex:129-187`: toric
  degeneration and conjectural effective cone/theta-basis statement.
- `chapters/theory/quantum_groups_foundations.tex:189-202`: equivariance
  is stratified by geometry and is not universal.
- `chapters/examples/coha_wall_crossing_platonic.tex:414-547`: KS
  wall-crossing has separate motivic and classical ambients.
- `chapters/examples/coha_wall_crossing_platonic.tex:657-701`: quantum
  versus classical ambient distinction is load-bearing.
- `chapters/examples/coha_wall_crossing_platonic.tex:860-925`:
  Davison-Meinhardt BPS decomposition and chamber independence in the
  toric no-compact-4-cycle regime.
- `chapters/examples/coha_wall_crossing_platonic.tex:1500-1519`: the
  chapter explicitly uses the positive-geometry definition as the
  non-toric replacement for a toric fan.

## Fatal attacks

### Cycle 1 ATTACK/HEAL: the tuple is not a constructed object in general

The definition fixes a Bridgeland chamber, orientation data, and a
derived critical atlas at
`quantum_groups_foundations.tex:23-26`, then immediately says that if
the oriented critical atlas is unavailable the datum is not constructed
(`quantum_groups_foundations.tex:57-60`). The theta basis is also placed
inside the tuple while its construction is theorem-grade only in
cluster/toric charts and conjectural for general compact CY3 chambers
(`quantum_groups_foundations.tex:73-76`).

Verdict: as written, the tuple is a conditional grammar, not a
definition of a universally constructed object. This is not a cosmetic
status issue. A tuple containing a nonconstructed theta basis is not an
object.

Heal: split the definition into a constructed relative Hall-scattering
datum and a theta-enhancement. The basic object should stop before
\(\Theta^{\mathrm{BPS}}_\sigma\). The theta basis is an enhancement
available under cluster/toric/GHKK-type hypotheses.

Primary-source obligations:
- KS 2008, arXiv:0811.2435, Sections 2.3, 4, 6.2, 7 for wall-crossing
  and motivic/classical integration.
- Brav-Bussi-Dupont-Joyce-Szendroi 2015 for orientation data and
  vanishing-cycle sheaves on oriented derived critical charts.
- GHKK 2018, JAMS 31, and Gross-Pandharipande-Siebert 2010 for
  broken-line theta bases and scattering consistency in cluster/tropical
  regimes. No local theorem currently supplies this for a general compact
  CY3 chamber.

### Cycle 2 ATTACK/HEAL: the KS scattering component is not well-typed

The current clause says that a wall carries
\[
  \exp(\Omega_\sigma(\gamma)\operatorname{Li}_2(e_\gamma))
\]
as an automorphism of the completed quantum torus
(`quantum_groups_foundations.tex:65-72`). This mixes the classical
Hamiltonian notation with the motivic quantum-torus ambient. The chapter
itself distinguishes:
\[
  x_\gamma x_{\gamma'} =
  \mathbb L^{\langle\gamma,\gamma'\rangle/2}x_{\gamma+\gamma'}
\]
in the motivic quantum torus
(`coha_wall_crossing_platonic.tex:428-439`, `469-478`), while the
classical ambient is the Euler-characteristic Poisson limit
(`coha_wall_crossing_platonic.tex:441-465`).

Verdict: fatal unless the definition records the ambient
\(\bullet\in\{\mathrm{mot},\mathrm{cl}\}\). The displayed
\(\operatorname{Li}_2\) formula is classical after the KS sign twist; it
is not the motivic quantum-dilogarithm wall factor.

Heal: define two scattering diagrams:
\[
  \mathfrak D^{\mathrm{mot}}_{\sigma,S,o}(X)
  \quad\text{and}\quad
  \mathfrak D^{\mathrm{cl}}_{\sigma,S,o}(X),
\]
with wall factors
\[
  U^{\mathrm{mot}}_\gamma =
  \mathbb E(x_\gamma)^{\Omega^{\mathrm{mot}}_{\sigma,o}(\gamma)}
  \in \widehat{\mathbb T}^{\mathrm{mot}}_{\Gamma,S},
\]
and, after Euler-characteristic specialisation and the KS sign
convention,
\[
  \mathcal K^{\mathrm{cl}}_\gamma(e_\eta)
  =
  e_\eta\,
  (1-\varepsilon_o(\gamma)e_\gamma)^{
     \Omega^{\mathrm{cl}}_{\sigma,o}(\gamma)
     \langle\gamma,\eta\rangle}.
\]
Equivalently the classical automorphism is generated by the Hamiltonian
\(\Omega^{\mathrm{cl}}_{\sigma,o}(\gamma)
\operatorname{Li}_2(\varepsilon_o(\gamma)e_\gamma)\). The sign
\(\varepsilon_o\) is the orientation/quadratic-refinement sign and must
not be suppressed.

Local anchors:
- `coha_wall_crossing_platonic.tex:428-439`: motivic bracket after
  square-root torsor twist.
- `coha_wall_crossing_platonic.tex:441-465`: classical Euler
  specialisation.
- `coha_wall_crossing_platonic.tex:571-587`: KS equality of
  phase-ordered products and Euler specialisation.
- `coha_wall_crossing_platonic.tex:657-701`: why dropping \(q\) changes
  the object.

### Cycle 3 ATTACK/HEAL: \(\Gamma^+_{\mathrm{eff},\sigma}\) is circular and too coarse

The effective monoid is defined as generated by classes with nonempty
semistable stack and nonzero BPS invariant
(`quantum_groups_foundations.tex:44-49`). But \(\Omega_\sigma\) is
defined later by integrating \(\phi_W\) over the stacks
(`quantum_groups_foundations.tex:61-64`). Worse, the monoid generated by
nonzero BPS charges may contain sums whose semistable moduli are empty
or whose primitive BPS invariant vanishes. This is harmless for a
completed quantum torus, but not harmless if the same monoid indexes
\(\mathcal M^+_{\mathrm{eff},\sigma}\).

Verdict: fatal as a first-principles definition. It conflates three
different supports:

1. semistable support,
2. BPS support,
3. HN/completion monoid.

Heal: split them:
\[
  \Gamma^{\mathrm{ss}}_{\sigma,S}
  =
  \{\gamma\in\Gamma_X\mid Z_\sigma(\gamma)\in S,\,
  \mathcal M_\sigma(\gamma)\neq\varnothing\},
\]
\[
  \Gamma^{\mathrm{BPS},\bullet}_{\sigma,S,o}
  =
  \{\gamma\in\Gamma^{\mathrm{ss}}_{\sigma,S}\mid
  \Omega^\bullet_{\sigma,o}(\gamma)\neq 0\},
\]
\[
  \Gamma^+_{\sigma,S,o}
  =
  \mathbb N\langle
  \Gamma^{\mathrm{BPS},\bullet}_{\sigma,S,o}
  \rangle.
\]
Index the critical stack by \(\Gamma^{\mathrm{ss}}_{\sigma,S}\), and
complete the quantum torus along \(\Gamma^+_{\sigma,S,o}\). The strict
sector \(S\subset\mathbb C\) is necessary for local finiteness and
path-ordered products; it is not optional bookkeeping.

Local anchors:
- `quantum_groups_foundations.tex:172-187`: local finiteness is
  conjectural after strict-sector completion.
- `coha_wall_crossing_platonic.tex:469-478`: HN completion is the
  algebraic setting for exponentials.
- `coha_wall_crossing_platonic.tex:551-564`: KS construction is
  pro-finite after HN completion.

### Cycle 4 ATTACK/HEAL: orientation and equivariance are load-bearing but not in the tuple

The definition fixes orientation data before the tuple
(`quantum_groups_foundations.tex:23-26`), but the tuple records only
\(\phi_W\). Orientation changes the motivic square-root and sign data;
it is part of the object, not a harmless choice. The same problem
appears for equivariance: the positive half uses
\(H^\bullet_{\mathrm{eq}}\) (`quantum_groups_foundations.tex:82-88`),
while the equivariance group is declared non-universal only later
(`quantum_groups_foundations.tex:189-202`).

Verdict: fatal for any comparison between chambers or geometries. The
same stack with a different orientation datum or equivariance group can
produce a different motivic wall factor and a different equivariant
positive half.

Heal: include \(o\) and \(T_{\mathrm{eq}}\) as parameters or tuple
entries. The notation should be
\[
  \mathfrak P^{\mathrm{BPS},\bullet}_{\sigma,S,o,T_{\mathrm{eq}}}(X)
\]
or the definition should explicitly be "relative to
\((\sigma,S,o,T_{\mathrm{eq}},\mathfrak A)\)" where \(\mathfrak A\) is
the oriented critical atlas.

Primary-source obligations:
- KS 2008 Section 5.2 for orientation data in motivic DT.
- Brav-Bussi-Dupont-Joyce-Szendroi 2015 for orientation data on
  locally presented \((-1)\)-shifted symplectic stacks.
- Maulik-Okounkov for equivariant stable envelopes when the MO path is
  invoked; local scope restriction appears at
  `quantum_groups_foundations.tex:742-770`.

### Cycle 5 ATTACK/HEAL: the charge lattice is missing the form and the sign refinement

The tuple lists \(\Gamma_X\), while the definition text separately
mentions the antisymmetric Euler form
(`quantum_groups_foundations.tex:19-24`). The quantum torus and KS Lie
bracket cannot be built from the bare abelian group. In CY3,
Serre duality gives
\[
  \chi(\gamma,\eta)=-\chi(\eta,\gamma),
  \qquad
  \langle\gamma,\eta\rangle
  =
  \chi(\gamma,\eta)-\chi(\eta,\gamma)=2\chi(\gamma,\eta),
\]
locally proved at
`coha_wall_crossing_platonic.tex:389-412` and used at
`coha_wall_crossing_platonic.tex:445-453`.

Verdict: fatal if \(\Gamma_X\) means only a lattice. It survives only if
\(\Gamma_X\) is explicitly defined as a lattice with skew form and
orientation sign/quadratic refinement.

Heal: replace the first component by
\[
  \Gamma_X^{\mathrm{or}}
  =
  (K^{\mathrm{num}}_0(\mathcal C),
   \langle-,-\rangle,
   \varepsilon_o).
\]

### Cycle 6 ATTACK/HEAL: \(\Omega_\sigma\) is redundant as data but necessary as an interface

If \(\phi_W\) and the oriented critical stacks are retained, then
\(\Omega_\sigma\) is not independent: it is the motivic or numerical
integration of the BPS sheaf. This is already stated at
`quantum_groups_foundations.tex:61-64`. But scattering diagrams use the
integrated coefficients, and the chapter's KS theorem separates motivic
coefficients from numerical coefficients
(`coha_wall_crossing_platonic.tex:483-509`, `672-679`).

Verdict: \(\Omega_\sigma\) is redundant for minimal foundations, but
operationally indispensable. It should be defined as an output of the
BPS sheaf and then recorded as part of the scattering interface.

Heal:
\[
  \mathrm{BPS}_{\gamma,\sigma,o}
  =
  H^\bullet_{c,T_{\mathrm{eq}}}
  (\mathcal M_\sigma(\gamma),\phi_{\mathfrak A,o}),
\]
\[
  \Omega^{\mathrm{mot}}_{\sigma,o}(\gamma)
  =
  [\mathrm{BPS}_{\gamma,\sigma,o}]_{\mathrm{vir}}\in\mathcal R,
  \qquad
  \Omega^{\mathrm{cl}}_{\sigma,o}(\gamma)
  =
  \chi(\mathrm{BPS}_{\gamma,\sigma,o})\in\mathbb Q.
\]
The motivic class is primary; the numerical Euler characteristic is its
shadow.

Local anchors:
- `coha_wall_crossing_platonic.tex:870-878`: BPS sheaves in the
  Davison-Meinhardt decomposition.
- `coha_wall_crossing_platonic.tex:887-920`: chamber filtration and
  integration-map compatibility.

### Cycle 7 ATTACK/HEAL: the theta basis is not minimal

\(\Theta^{\mathrm{BPS}}_\sigma\) is included in the tuple at
`quantum_groups_foundations.tex:73-76`, but the same lines say it exists
only when broken-line or Hall-factorisation constructions are available.
The conjecture at `quantum_groups_foundations.tex:172-187` is precisely
the missing existence statement for the general chamber.

Verdict: nonminimal and conditionally defined. Keeping it inside the
basic tuple makes the basic object conditional even when the Hall datum
exists.

Heal: define the object first, then define a theta enhancement:
\[
  \mathfrak P^{\mathrm{BPS},\bullet,+\theta}_{\sigma,S,o,T}(X)
  =
  (\mathfrak P^{\mathrm{BPS},\bullet}_{\sigma,S,o,T}(X),
   \Theta^{\mathrm{BPS},\bullet}_{\sigma,S,o,T})
\]
when the scattering diagram is consistent and a broken-line or
Hall-factorisation basis has been constructed. Status:
proved elsewhere in cluster/toric regimes; conjectural for general
compact CY3.

## Healed core

### Definition proposal: relative BPS Hall-scattering datum

Let \(\mathcal C\) be a CY3 category with support \(X\). Fix:

- a Bridgeland stability condition \(\sigma=(Z,\mathcal P)\);
- a strict sector \(S\subset\mathbb C\) for HN completion;
- orientation data \(o\) for determinant-line square roots;
- an oriented derived critical atlas \(\mathfrak A\) on the semistable
  moduli stacks;
- an equivariance group \(T_{\mathrm{eq}}\) appropriate to the geometry;
- an ambient \(\bullet\in\{\mathrm{mot},\mathrm{cl}\}\).

The relative BPS Hall-scattering datum is
\[
\begin{aligned}
 \mathfrak P^{\mathrm{BPS},\bullet}_{\sigma,S,o,T_{\mathrm{eq}}}(X)
 :=(&
  \Gamma_X^{\mathrm{or}},
  \Gamma^{\mathrm{ss}}_{\sigma,S},
  \Gamma^{\mathrm{BPS},\bullet}_{\sigma,S,o},
  \Gamma^+_{\sigma,S,o},\\
 &\mathcal M^{\mathrm{crit}}_{\sigma,S}(\mathfrak A),
  \phi_{\mathfrak A,o},
  \mathrm{BPS}_{\sigma,o},
  \Omega^\bullet_{\sigma,o},
  \widehat{\mathbb T}^{\bullet}_{\Gamma,S},
  \mathfrak D^{\mathrm{KS},\bullet}_{\sigma,S,o}
 ).
\end{aligned}
\]
Here
\[
  \Gamma_X^{\mathrm{or}}
  =
  (K^{\mathrm{num}}_0(\mathcal C),
  \langle-,-\rangle,\varepsilon_o),
\]
\[
  \mathcal M^{\mathrm{crit}}_{\sigma,S}(\mathfrak A)
  =
  \coprod_{\gamma\in\Gamma^{\mathrm{ss}}_{\sigma,S}}
  \mathcal M^{\mathrm{der}}_\sigma(\gamma),
\]
and
\[
  Y^+_{\sigma,S,o,T_{\mathrm{eq}}}(X)
  =
  H^\bullet_{T_{\mathrm{eq}}}
  \bigl(\mathcal M^{\mathrm{crit}}_{\sigma,S}(\mathfrak A),
  \phi_{\mathfrak A,o}\bigr)
\]
with Hall product whenever the critical Hall correspondence exists.

The theta-enhanced effective BPS positive geometry is this datum plus a
constructed theta basis. It is not part of the foundational datum until
the broken-line/Hall-factorisation theorem is available.

### Theorem proposal: toric degeneration

Status: proved elsewhere on standard toric Hall loci; conditional on
the Hopf-pairing hypothesis in exotic compact-4-cycle cases.

For a toric CY3 \(X_\Sigma\) with quiver-with-potential
\((Q_\Sigma,W_\Sigma)\) in a toric chamber,
\[
  \Gamma^{\mathrm{ss}}_{\sigma,S}
  =
  \Gamma^+_{\sigma,S,o}
  =
  \mathbb Z_{\ge 0}^{Q_0},
  \qquad
  \mathcal M^{\mathrm{crit}}_{\sigma,S}
  =
  \coprod_{\mathbf d\in\mathbb Z_{\ge0}^{Q_0}}
  [\operatorname{Crit}(W_{\mathbf d})/G_{\mathbf d}],
\]
and
\[
  Y^+_{\sigma,S,o,T}(X_\Sigma)
  =
  \operatorname{CoHA}(Q_\Sigma,W_\Sigma).
\]
For \(X=\mathbb C^3\),
\[
  Y^+_{\sigma,S,o,T}(\mathbb C^3)
  =
  Y^+(\widehat{\mathfrak{gl}}_1),
\]
not \(\mathcal W_{1+\infty}\). The full quantum group is the completed
Drinfeld double only after the Hopf pairing is available:
\[
  G_\sigma(X)=D(Y^+_{\sigma,S,o,T}(X))
  =
  Y^+_{\sigma,S,o,T}(X)
  \bowtie Y^0_{\sigma,S,o,T}(X)
  \bowtie Y^-_{\sigma,S,o,T}(X).
\]

Local anchors:
- `quantum_groups_foundations.tex:129-170`: toric degeneration already
  states the same collapse.
- `quantum_groups_foundations.tex:96-126`: Drinfeld double is
  conditional on atlas, PBW, and pairing.
- `quantum_groups_foundations.tex:545-568`: CoHA is positive half, not a
  vertex algebra or full Yangian.

## Exact formulas

Charge lattice and CY3 skew form:
\[
  \Gamma_X = K^{\mathrm{num}}_0(\mathcal C),\qquad
  \chi(\gamma,\eta)=-\chi(\eta,\gamma),\qquad
  \langle\gamma,\eta\rangle=2\chi(\gamma,\eta).
\]

Semistable support, BPS support, and completion monoid:
\[
  \Gamma^{\mathrm{ss}}_{\sigma,S}
  =
  \{\gamma\mid Z_\sigma(\gamma)\in S,\,
  \mathcal M_\sigma(\gamma)\neq\varnothing\},
\]
\[
  \Gamma^{\mathrm{BPS},\bullet}_{\sigma,S,o}
  =
  \{\gamma\in\Gamma^{\mathrm{ss}}_{\sigma,S}\mid
  \Omega^\bullet_{\sigma,o}(\gamma)\neq0\},
  \qquad
  \Gamma^+_{\sigma,S,o}
  =
  \mathbb N\langle\Gamma^{\mathrm{BPS},\bullet}_{\sigma,S,o}\rangle.
\]

Positive half:
\[
  Y^+_{\sigma,S,o,T_{\mathrm{eq}}}(X)
  =
  H^\bullet_{T_{\mathrm{eq}}}
  \bigl(\mathcal M^{\mathrm{crit}}_{\sigma,S}(\mathfrak A),
  \phi_{\mathfrak A,o}\bigr).
\]

Hall product in the critical CoHA:
\[
  m_H=\pi_*p^*:
  \mathcal H_{\gamma_1}\otimes\mathcal H_{\gamma_2}
  \longrightarrow
  \mathcal H_{\gamma_1+\gamma_2}.
\]

Davison-Meinhardt BPS decomposition in the QP regime:
\[
  \mathcal H(Q,W)
  \simeq
  \operatorname{Sym}\Bigl(
    \bigoplus_{\gamma}
    \mathrm{BPS}_\gamma(Q,W)\otimes H^\bullet(B\mathbb C^\times)
  \Bigr).
\]

Motivic quantum torus:
\[
  x_\gamma x_\eta
  =
  \mathbb L^{\langle\gamma,\eta\rangle/2}x_{\gamma+\eta},
  \qquad
  [x_\gamma,x_\eta]_q
  =
  \bigl(\mathbb L^{\langle\eta,\gamma\rangle/2}
       -\mathbb L^{-\langle\eta,\gamma\rangle/2}\bigr)
  x_{\gamma+\eta}.
\]

Motivic and classical wall factors:
\[
  U^{\mathrm{mot}}_\gamma
  =
  \mathbb E(x_\gamma)^{\Omega^{\mathrm{mot}}_{\sigma,o}(\gamma)},
\]
\[
  \mathcal K^{\mathrm{cl}}_\gamma(e_\eta)
  =
  e_\eta
  (1-\varepsilon_o(\gamma)e_\gamma)^{
  \Omega^{\mathrm{cl}}_{\sigma,o}(\gamma)\langle\gamma,\eta\rangle}.
\]

Conditional Drinfeld double:
\[
  G_\sigma(X)
  =
  D(Y^+_{\sigma,S,o,T}(X))
  =
  Y^+_{\sigma,S,o,T}(X)\bowtie
  Y^0_{\sigma,S,o,T}(X)\bowtie
  Y^-_{\sigma,S,o,T}(X).
\]

## Tuple minimality verdict

| Component | Verdict | Reason | Heal |
|---|---|---|---|
| Charge lattice | indispensable but under-specified | quantum torus needs skew form and orientation sign | use \(\Gamma_X^{\mathrm{or}}=(K^{num}_0,\langle-,-\rangle,\varepsilon_o)\) |
| Effective monoid | indispensable but conflated | semistable support, BPS support, and HN completion are different | split into \(\Gamma^{ss}\), \(\Gamma^{BPS}\), \(\Gamma^+\) |
| Critical stack | indispensable | source of Hall product and BPS sheaves | use oriented derived critical stack/atlas, not just informal stack |
| Vanishing cycles | indispensable | CoHA and BPS invariants are built from \(\phi_W\) | write \(\phi_{\mathfrak A,o}\), tied to orientation |
| BPS invariants | redundant but operational | decategorification of BPS sheaves, but needed for wall factors | define as output and record motivic/classical versions |
| KS scattering | derived, not primitive | follows from \(\Omega\), torus, completion, and KS theorem | include as structure only after ambient and consistency are specified |
| Theta basis | not minimal | theorem-grade only in cluster/toric regimes, conjectural generally | move to theta-enhancement |

Missing load-bearing data: \(\sigma\) as more than a subscript, strict
sector \(S\), orientation \(o\), critical atlas \(\mathfrak A\),
equivariance \(T_{\mathrm{eq}}\), motivic/classical ambient, sign
refinement \(\varepsilon_o\), support property/local finiteness, and
Hall-pairing/completion hypotheses for the Drinfeld double.

## Claim statuses

- Constructed Hall-scattering datum in toric quiver-with-potential
  chambers: **proved elsewhere**. Local anchors:
  `quantum_groups_foundations.tex:129-170`,
  `coha_wall_crossing_platonic.tex:92-141`,
  `coha_wall_crossing_platonic.tex:209-250`.
- CoHA has no internal differential and is an associative graded Hall
  algebra: **proved here / primary-supported**. Local anchors:
  `coha_wall_crossing_platonic.tex:209-255`.
- KS wall-crossing in motivic and classical ambients:
  **primary-supported, locally formulated**. Local anchors:
  `coha_wall_crossing_platonic.tex:414-547`,
  `coha_wall_crossing_platonic.tex:549-655`.
- Davison-Meinhardt BPS decomposition:
  **primary-supported in QP/toric regime**. Local anchors:
  `coha_wall_crossing_platonic.tex:860-925`.
- General compact CY3 theta basis:
  **conjectural**. Local anchors:
  `quantum_groups_foundations.tex:73-76`,
  `quantum_groups_foundations.tex:172-187`.
- General compact CY3 \(G(X)=D(Y^+(X))\):
  **conditional** on oriented critical atlas, PBW integrality, and
  nondegenerate Hall pairing. Local anchors:
  `quantum_groups_foundations.tex:96-126`.

## Manuscript insertion recommendations

1. Replace Definition `def:universal-positive-geometry-grammar` with a
   relative definition carrying
   \((\sigma,S,o,T_{\mathrm{eq}},\mathfrak A,\bullet)\).
2. Split the effective monoid clause into semistable support, BPS
   support, and HN completion monoid.
3. Replace the single KS scattering clause by motivic and classical
   clauses. Do not call \(\exp(\Omega\operatorname{Li}_2(e_\gamma))\)
   an automorphism of the motivic quantum torus.
4. Move \(\Theta^{\mathrm{BPS}}_\sigma\) out of the basic tuple and
   into a separate theta-enhancement definition/proposition.
5. Add an explicit equivariance parameter to the positive-half
   definition; the later stratification remark should become part of the
   definition's input.
6. Keep the Drinfeld double theorem conditional exactly as now, but
   make its dependencies refer to the healed relative datum.

## Files changed

- Created `notes/adversarial_bps_positive_geometry_20260424/agent_01_foundations_gelfand.md`.
- No manuscript files edited.

## Verification run

Attempted:

```bash
python -m pytest compute/tests/test_coha_wall_crossing_platonic.py compute/tests/test_conifold_wall_crossing.py -q
```

Result: `python` is not on PATH in this environment.

Passed:

```bash
python3 -m pytest compute/tests/test_coha_wall_crossing_platonic.py compute/tests/test_conifold_wall_crossing.py -q
```

Result: `31 passed in 0.15s`.
