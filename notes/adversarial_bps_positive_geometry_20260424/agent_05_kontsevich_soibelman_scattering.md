# Agent 05: Kontsevich--Soibelman Scattering Axis

Scope: stability, scattering diagrams, wall-crossing, motivic quantum tori, quantum dilogarithms, Harder--Narasimhan factorisation, and the theta-basis/tropical-degeneration interface.

Owned file: `notes/adversarial_bps_positive_geometry_20260424/agent_05_kontsevich_soibelman_scattering.md`.

Manuscript files were read for anchors only. No manuscript edit is made here.

## Anchor Ledger

- `chapters/examples/coha_wall_crossing_platonic.tex:40-72`: KS wall-crossing lives first in the motivic Hall Lie algebra; the bridge to the chiral convolution dgLA passes through `\Phi^{FA}_3` and is proved for `\mathbb C^3`, conditional beyond that locus.
- `chapters/examples/coha_wall_crossing_platonic.tex:414-547`: motivic and classical KS ambients, brackets, HN completion, wall-crossing gauge action, MC equation, and quantum-dilogarithm pentagon.
- `chapters/examples/coha_wall_crossing_platonic.tex:571-587`: KS phase-ordered product in the motivic quantum torus and Euler-characteristic specialisation.
- `chapters/examples/coha_wall_crossing_platonic.tex:597-654`: local quantum dilogarithm normalisation and the conifold/A2 pentagon.
- `chapters/examples/coha_wall_crossing_platonic.tex:657-700`: quantum/classical ambient distinction is load-bearing.
- `chapters/examples/coha_wall_crossing_platonic.tex:703-733`: bar-side MC and Hall-side MC are distinct dg Lie algebras linked by the first-stage `\Phi^{FA}_3` map.
- `chapters/theory/cy_to_chiral.tex:4065-4077`: KS wall-crossing, hocolim, and MC gauge equivalence are asserted together; the text already warns that the pentagon holds in the quantum torus, not by naive BCH.
- `chapters/theory/cy_to_chiral.tex:4095-4116`: scattering diagrams are asserted as `E_1` MC data; this needs strict-sector, support-property, and completion hypotheses.
- `chapters/theory/cy_to_chiral.tex:4152-4164`: overlap wall algebras and the wall automorphism `K_\gamma`.
- `chapters/examples/k3_quantum_toroidal_chapter.tex:1037-1099`: K3 tropical limit, GHKK cluster-shadow conjecture, theta functions, and GPS pentagon.
- `chapters/examples/k3_quantum_toroidal_chapter.tex:1104-1120`: tropical BPS/broken-line/theta coefficient conjecture.
- `chapters/examples/k3e_cy3_programme.tex:2847-2906`: BKM scattering open problem and scattering diagram as tropical shadow conjecture.
- `chapters/examples/k3e_cy3_programme.tex:4236-4308`: motivic DT wall-crossing at `K3 x E` is conjectural; numerical Oberdieck identity is theorem-grade.
- `chapters/examples/k3e_cy3_programme.tex:4311-4356`: motivic quantum-dilogarithm factorisation, orientation data, and `GL_2(Q)`/Igusa wall-crossing conjecture.
- `compute/lib/scattering_diagram.py:1-39`: local computation confirms the pair-commutator approach does not reproduce `\phi_{0,1}` multiplicities; full motivic wall-crossing is needed.
- `compute/lib/scattering_diagram_e1_mc.py:1-113`: compute scaffold distinguishes exact quantum-torus pentagon from BCH-level residues.
- `compute/tests/test_scattering_diagram_e1_mc.py:1-57`: local tests encode AP42: BCH multiplicities are not DT invariants at height `>= 3`.

Primary-source anchors already present locally:

- `bibliography/references.tex:538-539`: Kontsevich--Soibelman 2011 CoHA.
- `bibliography/references.tex:692-693`: Kontsevich--Soibelman 2008 stability structures, motivic DT invariants, and cluster transformations.
- `compute/lib/scattering_diagram_e1_mc.py:104-110`: Gross--Siebert, GPS tropical vertex, GHKK theta functions, KS 2008, Keller quantum dilogarithms, Bridgeland scattering/stability.

## Baseline Object

Let `\Gamma` be a finitely generated charge lattice, let
`\langle-,-\rangle:\Gamma\times\Gamma\to\mathbb Z` be skew-symmetric, and let
`Z:\Gamma\to\mathbb C` be a central charge. Fix a positive cone
`\Gamma_+\subset\Gamma` and a norm `||-||` on `\Gamma_\mathbb R`.

A strict sector is an open convex cone `V\subset\mathbb C^*` of angular width
`<\pi` whose boundary contains no ray `Z(\gamma)` with active BPS charge
`\Omega(\gamma)\ne 0`. The completed sector Lie algebra is
\[
  \widehat{\mathfrak g}_V
  =
  \prod_{\substack{\gamma\in\Gamma_+\\ Z(\gamma)\in V}}
  \mathbb k\cdot e_\gamma,
  \qquad
  [e_\alpha,e_\beta]
  =
  (-1)^{\langle\alpha,\beta\rangle}
  \langle\alpha,\beta\rangle e_{\alpha+\beta}.
\]
At motivic level replace this by the completed quantum torus
\[
  \widehat{\mathbb T}^{\mathrm{mot}}_V
  =
  \prod_{\substack{\gamma\in\Gamma_+\\ Z(\gamma)\in V}}
  \mathcal R\cdot x_\gamma,
  \qquad
  x_\alpha x_\beta
  =
  \mathbb L^{\langle\alpha,\beta\rangle/2}x_{\alpha+\beta},
\]
with `\mathcal R=K_0(\mathrm{Var}_{\mathbb C})[\mathbb L^{-1},(1-\mathbb L^{-k})^{-1}]`
or the corresponding `K_0(\mathrm{MMHS})[\mathbb L^{\pm1/2}]` refinement when
mixed Hodge structures are part of the statement.

The support property is part of the datum: there is a quadratic form `Q` on
`\Gamma_\mathbb R`, negative definite on `\ker Z`, such that
`Q(\gamma)\ge 0` for every active semistable charge. Equivalently, after
choosing a norm, there is `C>0` with
\[
  ||\gamma||\le C\, |Z(\gamma)|
  \qquad
  \text{for all active } \gamma.
\]
This is the hypothesis that prevents an infinite cloud of BPS rays from
destroying local finiteness in strict sectors.

## ATTACK/HEAL Cycle 1: Local Finiteness

ATTACK. The phrase "the KS scattering diagram for `K3 x E`" is false if it
means an ordinary locally finite wall arrangement in `\Gamma_\mathbb R`
without completions. `K3 x E` has infinitely many BPS charges; roots of the
BKM cone and Bridgeland walls can accumulate at isotropic directions. A
path-ordered product crossing infinitely many walls has no meaning unless the
sector, topology, and filtration are fixed.

HEAL. The chamber/scattering object must be completed sector-by-sector. For a
strict sector `V`, define the mass filtration
\[
  F^{>R}\widehat{\mathfrak g}_V
  =
  \prod_{\substack{\gamma\in\Gamma_+,\,Z(\gamma)\in V\\ |Z(\gamma)|>R}}
  \mathbb k e_\gamma.
\]
The support property implies that for each `R` and each bounded subset of
`\Gamma_\mathbb R/F^{>R}`, only finitely many active charges contribute. A
wall structure is locally finite modulo every `F^{>R}`; the real object is the
inverse system of finite truncations. In the toric/conifold chart this is
theorem-grade. For compact `K3 x E`, the local finiteness statement is
conjectural until the motivic integrality/support-property package of
`k3e_cy3_programme.tex:4236-4308` is established.

Status: proved in toric/cluster charts; conjectural for compact `K3 x E`.

## ATTACK/HEAL Cycle 2: Support Property

ATTACK. The scattering diagram cannot be derived from numerical invariants
`\Omega(\gamma;\sigma)` alone. If the active support violates the support
property, infinitely many charges of bounded phase and bounded central charge
can contribute to one sector, and the KS product need not converge in any
HN/Novikov completion.

HEAL. A stability-scattering datum is not `(\Omega,Z)` but
\[
  \mathsf S=(\Gamma,\langle-,-\rangle,Z,Q,\Omega,o),
\]
where `Q` is the support-property quadratic form and `o` is orientation data
for the motivic square-root/sign. The active support is
\[
  \operatorname{Supp}(\Omega)
  =
  \{\gamma\in\Gamma_+:\Omega(\gamma)\ne 0,\ Q(\gamma)\ge 0\}.
\]
Only this support enters walls. For a primitive active charge `\gamma`, the
wall in a chamber of the central-charge plane is
\[
  \mathfrak d_\gamma
  =
  \{m\in\Gamma_\mathbb R^\vee:\langle m,\gamma\rangle=0,\ Z(\gamma)\in V\},
\]
decorated by a group element in the completion of the ray algebra
`\widehat{\mathfrak g}_{\mathbb R_{>0}\gamma}`.

At `K3 x E`, the note must not state "the support property holds for the full
motivic BPS spectrum" as a theorem. The precise healed statement is: conditional
on Bridgeland stability with support property on the Oberdieck--Pixton
component and on motivic integrality/orientation data, the sector completions
above define the KS wall structure.

Status: definition-grade; global `K3 x E` existence conditional.

## ATTACK/HEAL Cycle 3: Strict Sectors and HN Factorisation

ATTACK. "The ordered KS product is chamber-independent" is too imprecise. The
product is not over all charges at once. KS wall-crossing is a factorisation
law over strict sectors and rays, and it depends on the clockwise/counterclockwise
phase ordering. Without the HN property, there is no unique factorisation into
semistable phases.

HEAL. For each strict sector `V`, define
\[
  A_V(Z)
  =
  \prod_{\ell\subset V}^{\curvearrowright}
  A_\ell(Z),
  \qquad
  A_\ell(Z)
  =
  \prod_{\substack{\gamma\in\Gamma_+\\ Z(\gamma)\in\ell}}^{\curvearrowright}
  \mathbb E(x_\gamma)^{\Omega^{\mathrm{mot}}(\gamma;Z)}
  \in \widehat{\mathbb T}^{\mathrm{mot}}_V.
\]
The product over rays is phase-ordered inside `V`. If
`V=V_1\sqcup V_2` with every ray of `V_1` preceding every ray of `V_2` in the
chosen orientation, the HN factorisation condition is
\[
  A_V(Z)=A_{V_1}(Z)\,A_{V_2}(Z).
\]
This is the scattering form of Harder--Narasimhan uniqueness: every object has
a finite HN filtration with strictly decreasing phases, and the Hall-algebra
class of all objects factors as the ordered product of semistable classes.

The local manuscript anchor is `coha_wall_crossing_platonic.tex:571-577`, where
the KS theorem is written as equality of phase-ordered products before taking
the logarithm and extracting a wall generator. This is the correct direction:
HN factorisation first, logarithmic MC/gauge expression second.

Status: theorem for the KS/Hall setting with stability data and HN property;
conditional where the stability component is only conjecturally constructed.

## ATTACK/HEAL Cycle 4: Path-Ordered Products and Consistency

ATTACK. The formula `K_\gamma=\exp(\Omega(\gamma)\operatorname{Li}_2(X^\gamma))`
in a wall-overlap paragraph is not by itself a scattering diagram. It lacks
the normal vector, crossing sign, singular support, and loop consistency
condition. It also risks confusing a wall automorphism with the full
path-ordered product.

HEAL. A chamber scattering diagram subordinate to `\mathsf S` is a collection
\[
  \mathfrak D
  =
  \{(\mathfrak d_i,\theta_i)\}_{i\in I},
\]
where each `\mathfrak d_i` is a rational codimension-one cone in
`\Gamma_\mathbb R^\vee`, each `\theta_i` is an automorphism of the completed
torus, and the singular locus is the union of boundaries and pairwise
intersections of non-parallel walls. For a primitive normal `n_i` and charge
`\gamma_i`, the classical wall automorphism is
\[
  \theta_i(x^m)
  =
  x^m\, f_i^{\langle n_i,m\rangle},
  \qquad
  f_i
  =
  \exp\!\left(
    \sum_{k\ge 1}
    \frac{\Omega(k\gamma_i)}{k^2}x^{k\gamma_i}
  \right),
\]
with the motivic/quantum lift obtained by replacing `f_i` by the corresponding
quantum-dilogarithm factor in `\widehat{\mathbb T}^{\mathrm{mot}}`.

For a smooth path `\wp` crossing walls
`\mathfrak d_{i_1},\ldots,\mathfrak d_{i_s}` transversely and avoiding the
singular locus,
\[
  \mathfrak p_{\wp,\mathfrak D}
  =
  \theta_{i_s}^{\varepsilon_s}\cdots\theta_{i_1}^{\varepsilon_1},
  \qquad
  \varepsilon_j
  =
  \operatorname{sign}\langle n_{i_j},\dot\wp(t_j)\rangle.
\]
The diagram is consistent if `\mathfrak p_{\wp,\mathfrak D}` depends only on
the endpoints, equivalently if it is the identity for every sufficiently small
loop around every joint, modulo every finite filtration quotient. This is the
rigorous version of `cy_to_chiral.tex:4095-4116` and
`coha_wall_crossing_platonic.tex:2486-2488`.

Status: definition-grade; consistency theorem in the standard KS/Gross--Siebert
settings; conjectural after chiralisation outside proved toric charts.

## ATTACK/HEAL Cycle 5: Motivic Quantum Torus and Quantum Dilogarithm

ATTACK. The manuscript contains both classical and motivic language. If the
quantum torus is silently replaced by the classical symplectic torus, the
pentagon loses the `q^{1/2}` cocycle and becomes only a classical Rogers
shadow. That would erase the bound-state middle factor.

HEAL. Use the motivic quantum torus when stating the exact KS scattering
identity. With `q=\mathbb L`, the local convention in
`coha_wall_crossing_platonic.tex:597-654` is
\[
  \Psi(x)
  =
  \prod_{k\ge0}(1-\mathbb L^{k+1/2}x)^{-1}
  =
  \sum_{n\ge0}
  \frac{\mathbb L^{n^2/2}}
       {\prod_{j=1}^n(\mathbb L^j-1)}
  x^n,
\]
\[
  \log\Psi(x)
  =
  \sum_{n\ge1}
  \frac{x^n}{n(\mathbb L^{n/2}-\mathbb L^{-n/2})}\,
  \mathbb L^{n/2}.
\]
For two charges with skew pairing `+1`, the exact pentagon is
\[
  \Psi(x_0)\Psi(x_1)
  =
  \Psi(x_1)\Psi(q^{-1/2}x_0x_1)\Psi(x_0).
\]
The middle term is the non-split bound-state variable
\[
  x_{[S_0\oplus S_1]}=q^{-1/2}x_0x_1,
\]
not the untwisted monomial `x_{e_0+e_1}`. The Euler-characteristic
specialisation sends `\mathbb L^{1/2}\to 1` in the classical discussion and
collapses `\Psi(x)` to `\exp(\operatorname{Li}_2(x))`; this is a shadow, not
the motivic identity.

At `K3 x E`, the alternative convention
`\mathbb E(z)=\prod_{n\ge0}(1+\mathbb L^{-1/2}z^{2n+1})^{-1}` appears in
`k3e_cy3_programme.tex:4311-4328`. It is admissible only after recording the
normalisation map and the orientation-data sign. Do not mix the two conventions
inside a single formula.

Status: exact in the motivic quantum torus; classical formula is a
specialisation.

## ATTACK/HEAL Cycle 6: MC Equation Versus Naive BCH

ATTACK. The slogan "scattering diagram consistency is the MC equation" is
dangerous because a truncated BCH computation in the lattice Lie algebra sees
only leading commutators. The local compute surface explicitly reports that
pair-commutator multiplicities do not reproduce `\phi_{0,1}` root
multiplicities (`compute/lib/scattering_diagram.py:8-23`), and the E1-MC test
scaffold records AP42: BCH multiplicities are not DT invariants at height
`>=3` (`compute/tests/test_scattering_diagram_e1_mc.py:47-57`).

HEAL. State the MC/scattering relation in two layers.

Layer 1, exact Hall/quantum layer:
\[
  A_V(Z)
  =
  \prod_{\ell\subset V}^{\curvearrowright}
  \mathbb E_\ell^{\Omega^{\mathrm{mot}}_\ell}
\]
is invariant under deformation of `Z` inside the chamber structure, and crossing
a wall changes the factorisation by conjugation in
`\widehat{\mathbb T}^{\mathrm{mot}}_V`. This is the KS wall-crossing theorem.

Layer 2, logarithmic completed Lie layer:
\[
  \Theta_V=\log A_V(Z)\in\widehat{\mathfrak g}_V,
  \qquad
  d\Theta_V+\frac12[\Theta_V,\Theta_V]=0
\]
means that all joint holonomies vanish in the completed filtration. At finite
height `h`, the new wall term `\Theta^{(h)}` is determined by the degree-`h`
part of
\[
  d\Theta^{(<h)}
  +
  \frac12[\Theta^{(<h)},\Theta^{(<h)}]
  +
  \sum_{r\ge3}\frac1{r!}\ell_r(\Theta^{(<h)},\ldots,\Theta^{(<h)}),
\]
when a genuine `L_\infty` model is used. In the purely Lie/BCH truncation the
`\ell_{r\ge3}` terms are absent; this is why the conifold/A2 pentagon is
visible at low height but the BKM/K3 elliptic-genus multiplicities are not
recovered from pair commutators alone.

Status: exact at Hall/quantum level; BCH-only multiplicities are diagnostic,
not DT invariants.

## ATTACK/HEAL Cycle 7: Theta Basis and Toric Degeneration

ATTACK. "The theta basis is the KS scattering diagram" is too strong. GHKK
theta functions require a consistent scattering diagram on an integral affine
base plus broken-line convergence/positivity hypotheses. KS wall-crossing
gives automorphisms in a charge torus. The two are expected to agree under
tropicalisation/toric degeneration, but this is not automatic for compact
`K3 x E`.

HEAL. For a consistent diagram `\mathfrak D` on an affine base `B`, the theta
function attached to an integral point `p` is
\[
  \vartheta_p(Q)
  =
  \sum_{\beta}
  \left(
    \sum_{\substack{\mathfrak b\ \mathrm{broken\ line}\\
                    \mathrm{end}(\mathfrak b)=Q,\ \mathrm{in}(\mathfrak b)=p\\
                    \mathrm{mon}(\mathfrak b)=c_{\mathfrak b}x^\beta}}
    c_{\mathfrak b}
  \right)x^\beta.
\]
The multiplication constants are broken-line counts:
\[
  \vartheta_p\vartheta_q
  =
  \sum_r N_{pq}^r\,\vartheta_r,
  \qquad
  N_{pq}^r
  =
  \#\{\text{compatible pairs of broken lines from }p,q\text{ ending at }r\}
\]
with coefficients in the relevant monoid algebra or its motivic lift. This is
the theta-basis side of `k3_quantum_toroidal_chapter.tex:1081-1099` and
`1104-1120`.

The correct consistency conjecture with toric degeneration is:

Conjecture (KS/Gross--Siebert compatibility under toric degeneration). Let
`\pi:\mathcal X\to\Delta` be a toric or maximally unipotent degeneration of
CY3 categories with tropical affine base `B`, charge lattice `\Gamma`, and
central charges `Z_t` whose phase tropicalisation sends active charges
`\gamma` to primitive affine directions `n_\gamma` in `B`. Assume:

1. Bridgeland stability with support property on the relevant component.
2. Fixed orientation data `o`.
3. Motivic DT integrality in the sector under study.
4. Gross--Siebert/GHKK consistency for the limiting affine scattering diagram.

Then for every strict sector `V` and every path `\wp` avoiding joints,
\[
  \operatorname{Trop}_{t\to0}
  \left(
    \mathfrak p_{\wp_t,\mathfrak D^{\mathrm{KS}}_{X_t,V}}
  \right)
  =
  \mathfrak p_{\wp,\mathfrak D^{\mathrm{GS}}_{B,V}},
\]
and the coefficient comparison is
\[
  \operatorname{Trop}
  \left(
    \Omega^{\mathrm{mot}}(\gamma;\sigma_t)
  \right)
  =
  N^{\mathrm{log/trop}}_\gamma
  =
  \#\{\text{broken lines of charge }\gamma\}
\]
after the declared motivic-to-log coefficient specialisation. Consequently
the GHKK theta basis is the tropicalisation of the KS chamber basis:
\[
  \operatorname{Trop}_{t\to0}(\vartheta^{\mathrm{KS}}_\gamma)
  =
  \vartheta^{\mathrm{GHKK}}_{n_\gamma}.
\]

For `K3 x E`, this conjecture specialises to the programme in
`k3e_cy3_programme.tex:2847-2906`: the BKM scattering diagram on
`\Gamma^{2,2}_\mathbb R` should be the tropical skeleton of the shadow
obstruction tower. The coefficient statement remains conditional at the
motivic level because `k3e_cy3_programme.tex:4236-4308` explicitly records
the motivic lift/integrality as conjectural, while the numerical Oberdieck
partition function is theorem-grade.

Status: theorem-grade in standard toric/GHKK charts; conjectural compatibility
for compact `K3 x E`.

## Chamber/Scattering Definition for Manuscript Repair

Definition. A KS chamber-scattering datum for a CY3 category `\mathcal C` is
the tuple
\[
  \mathfrak S(\mathcal C)
  =
  (\Gamma,\langle-,-\rangle,Z,Q,o,\Omega^{\mathrm{mot}},\mathfrak D)
\]
where:

1. `\Gamma=K_0^{\mathrm{num}}(\mathcal C)` and `\langle-,-\rangle` is the
   skew Euler form.
2. `Z:\Gamma\to\mathbb C` is a Bridgeland central charge.
3. `Q` satisfies the support property.
4. `o` is orientation data for the motivic square root.
5. `\Omega^{\mathrm{mot}}(\gamma;\sigma)` is the motivic DT invariant in the
   declared coefficient ring.
6. `\mathfrak D` is a locally finite modulo filtration collection of walls
   `(\mathfrak d_\gamma,\theta_\gamma)` whose automorphisms are generated by
   motivic quantum dilogarithms in the completed torus.

For each strict sector `V`, the sector group element is
\[
  A_V(\sigma)
  =
  \prod_{\ell\subset V}^{\curvearrowright}
  \prod_{\substack{\gamma\in\Gamma_+\\Z_\sigma(\gamma)\in\ell}}
  \mathbb E(x_\gamma)^{\Omega^{\mathrm{mot}}(\gamma;\sigma)}.
\]
The datum is consistent if:

1. HN factorisation holds: `A_{V_1\cup V_2}=A_{V_1}A_{V_2}` for ordered
   decompositions of strict sectors.
2. Path-ordered products around joints are identity in every finite quotient.
3. For any two generic central charges in the same connected component, the
   total KS class `A_V` is unchanged after refactorisation by rays.

This definition is strong enough to support the manuscript's intended
scattering-MC statement and weak enough not to overclaim compact `K3 x E`
motivic existence.

## Findings

1. The current `cy_to_chiral.tex:4095-4116` statement needs hypotheses:
   strict sector, support property, completion, and a declaration of quantum
   versus classical ambient. Without these, local finiteness and path products
   are undefined.
2. The exact pentagon belongs in the motivic/quantum torus. The BCH/log Lie
   expression is a derived shadow and is unreliable for multiplicities at
   height `>=3`.
3. HN factorisation is the mathematical source of ordered sector products.
   It should be named before the MC/gauge reformulation.
4. The theta-basis bridge is a toric-degeneration/GHKK conjecture for compact
   `K3 x E`, not a consequence of KS wall-crossing alone.
5. The `K3 x E` coefficient comparison must remain conditional at motivic
   level. The numerical `-C/\Delta_{10}` identity does not prove motivic
   polynomiality, per-class invariance, or theta-basis existence.

Recommended manuscript-level repair: replace any global sentence of the form
"the KS scattering diagram is the MC element" by the chamber-scattering
definition above, then state the toric result and compact `K3 x E` compatibility
as separate theorem/conjecture layers.
