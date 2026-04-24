# Agent A4 report: CY3 holomorphic defects, endpoint modules, and trace theorem

Date: 2026-04-24.

Scope: attack whether Vol III can presently construct holomorphic
perfect defects/modules for `PhiFA_3`, endpoint/puncture data, and a
factorization-homology trace theorem, compared with the
Costello--Francis--Gwilliam ordinary Chern--Simons module theorem.

Owned output: this report only.

## Verdict

Vol III can now give the correct formal target for holomorphic
defects/modules over the Stage-1 object
`F_X = PhiFA_3(C)_F`, and it has a local compute-backed
`C^3`, `gl_1`, codimension-2 OPE witness. It cannot yet claim a full
construction of holomorphic perfect defects/modules for arbitrary
CY3 inputs, K3 x E Hall/BKM modules, or a Borcherds/DT trace theorem.

The strongest theorem available now is conditional:

1. If `F_X = PhiFA_3(C)_F` is constructed on the framed Stage-1 locus
   and `(Sigma_2,C)` is an admissible specialization datum, then one can
   define a holomorphic constructible `E_{1 subset 3}` coefficient
   system supported on a holomorphic curve `C subset X`. A perfect
   defect is a compact/dualizable module object in that holomorphic
   factorization category, finite over the normal-completed local
   algebra and compatible with the CY orientation datum.
2. If such a defect is trace-class, factorization homology gives a
   chiral trace class in the holomorphic stratified factorization
   homology of `(X,C)`, and after Stage 2 a trace class for the
   `E_1` chiral algebra
   `A_C = SpCh_{Sigma_2,C}(F_X)`.
3. A comparison of that trace with Hall, DT, BKM, or the Gritsenko--
   Nikulin denominator is not available until the hCS-to-Hall map and
   its module-level analogue are constructed.

CFG proves the corresponding ordinary real 3-dimensional Chern--Simons
statement: a locally constant filtered `E_3` algebra deforming
`C^*(g)`, perfect modules, endpoint objects, and RT traces by
factorization homology. It supplies the Morita/trace grammar and the
topological shadow, not the CY3 holomorphic object.

## Attacked claims

### 1. CFG perfect modules are already CY3 perfect modules

Failure mode. CFG perfectness is finite/topological: ordinary CS on
real 3-balls reaches `C^*(g)` by local constancy, and the defect module
is finite-dimensional representation data after filtered Koszul
duality. Vol III's CY3 object is Dolbeault-local and remembers
holomorphic jets, normal formal modes, CY orientation, and many-variable
residues. The local model in
`chapters/theory/cy3_chain_level_bridge.tex:102` is not `C^*(g)` but
the many-variable chiral CE/enveloping object

```tex
L_C(P)=Omega_c^{0,*}(P,J^\infty_hol l_C)[1],
\qquad
PhiFA_3(C)|_P ~= U_P^{fact,E_3}(L_C).
```

Heal. Define CY3 perfectness internally: compact/dualizable in the
holomorphic factorization module category over `F_X`, coherent for the
Dolbeault/chiral CE action on all polydiscs, finite Tor-amplitude over
normal completions, and compatible with orientation and endpoint duals.
This is a definition plus a conditional existence problem, not a CFG
corollary.

### 2. Normal directions may be contracted away

Failure mode. CFG contracts the de Rham formal normal disk. In the
holomorphic CY3 setting the normal formal disk contributes holomorphic
functions, not constants. For a polydisc
`P = D_z x D_u x D_v` with `C cap P = D_z x {0,0}`, the defect sees

```tex
L_{X,C}^{hat}(D_z)
  = Omega_c^{0,*}(D_z,
      J^\infty_hol(l_C|_C) \hat\otimes Sym^hat N_{C/X}^\vee)[1].
```

Equivalently, in the trivial normal chart it sees `g[[u,v]]`. These
normal modes are precisely what carry the two-parameter
Omega-background and the local quantum-toroidal/defect OPE data.

Heal. A locally constant shadow functor may reduce to CFG's line-only
model, but only after a named de Rham/constant-mode reduction. Before
that reduction, the holomorphic defect algebra must retain the normal
completion.

### 3. CFG endpoint data are CY3 punctures

Failure mode. CFG half-line endpoints are boundary conditions for a
one-dimensional fermion coupled to real topological CS, with classical
observables such as `C^*(g,S_rho)`. A CY3 puncture is a marked point on
a holomorphic defect curve with Dolbeault boundary condition, normal
mode residues, orientation local systems, and possibly class-S flavor
data. Class-S punctures on `Sigma_{0,24}` are not CFG line endpoints.

Heal. An endpoint/puncture datum for CY3 should be a compact object
`M_p` in the one-sided module category of the nearby holomorphic defect
algebra, with dual `M_p^vee`, evaluation/coevaluation maps satisfying
the zigzag identities, and compatibility with the normal-mode residue
operation. In a free-fermion shadow, `M_p` may reduce to the CFG spinor
or Fock endpoint. In the K3 x E class-S branch it is a protected
chiral-sector module whose comparison with `F_X` is still conjectural.

### 4. CFG factorization traces imply Borcherds/DT traces

Failure mode. CFG traces are RT invariants for ordinary CS modules.
K3 x E BKM/DT traces require oriented critical CoHA, charge/HN
completions, vanishing cycles, Thom--Sebastiani compatibility, and
automorphic Borcherds input. The open comparison
`Theta_{hCS->Hall}^{or}` is stated explicitly in
`chapters/theory/cy3_chain_level_bridge.tex:487`, and CFG supplies none
of its Hall-side data.

Heal. The correct theorem must be a composite of separately constructed
maps:

```tex
Tr^{hol}_{F_X}(M_C)
  -> Tr^{Hall}_{CoHA_crit}(Theta_M(M_C))
  -> Borcherds/DT character.
```

Only the first arrow is formal once the holomorphic perfect module is
constructed. The second and third are independent Hall/automorphic
comparison theorems.

### 5. The final d=3 chiral algebra is natively E2

Failure mode. CFG modules over an `E_3` algebra form an `E_2`-monoidal
category. This does not promote Vol III's curve-specialized d=3 output
to a native `E_2` chiral algebra. The two-stage theorem states that
`A_C = SpCh_{Sigma_2,C}(PhiFA_3(C))` is native `E_1` for `d >= 3`
(`chapters/theory/cy_to_chiral.tex:283`). The `E_2` structure lives on
the Drinfeld center of the `E_1` representation category, not on `A_C`
itself.

Heal. Use:

```tex
Z(Rep^{E_1}(A_C))
  ~= Rep^{E_2}(Z^{der}_{ch}(A_C)),
```

not `Rep^{E_2}(A_C)` unless a separate `E_2` structure on `A_C` has
been constructed.

### 6. The codimension-2 OPE witness proves the global module theorem

Failure mode. The compute engine
`compute/lib/hcs_codim2_defect_ope.py:1` proves a local
`C^3`, `gl_1`, low-spin defect witness. It derives, for a codimension-2
defect on the `z_1`-curve,

```tex
J(z)J(w) ~ Psi/(z-w)^2,
Psi = -sigma_2,
```

and a Sugawara Virasoro field with central charge `c = 1`. The same
scope is recorded in
`notes/adversarial_swarm_20260424_hol_e3/agent_09_gaiotto_defects_modules.md:35`.
This does not construct global holomorphic perfect modules, endpoint
duals, Hall modules, or BKM traces.

Heal. Keep the OPE witness as a local theorem and a test oracle for the
normal-completed definition. Do not use it to upgrade K3 x E or compact
CY3 defect-module statements.

## Surviving formalism

The following structure survives the attack.

### Stage 1

On the verified framed locus,

```tex
F_X = PhiFA_3(C)_F in E_3-HolFA(X).
```

The local polydisc model is the Dolbeault/chiral CE object of
`chapters/theory/cy3_chain_level_bridge.tex:102`, with ordinary
`C^*(g)` appearing only after taking the locally constant shadow. The
Stage-1 envelope theorem at
`chapters/theory/cy3_chain_level_bridge.tex:851` records this as an
object-level construction and explicitly does not supply the
hCS-to-Hall comparison.

### Stage 2

For admissible `(Sigma_2,C)`,

```tex
A_C = SpCh_{Sigma_2,C}(F_X) in E_1-ChirAlg(C),
\qquad
SpCh_{Sigma_2,C}(F) = (int_{Sigma_2} F)|_C.
```

This is Definition `def:phi-fa-and-sp` at
`chapters/theory/cy_to_chiral.tex:229` and the two-stage theorem at
`chapters/theory/cy_to_chiral.tex:249`. The current d=3 theorem is
object-level under hypotheses H1--H4; arbitrary CY3 morphism
functoriality remains outside the theorem
(`chapters/theory/cy_to_chiral.tex:571`,
`chapters/theory/cy_to_chiral.tex:9717`).

### Holomorphic defect category

For a holomorphic curve `i:C -> X` and a finite endpoint set
`S subset C`, define

```tex
HolDef^{perf}_{F_X}(C;S)
```

to be the full subcategory of holomorphic constructible
`E_{1 subset 3}` modules over `F_X` whose objects consist of:

1. Bulk coefficients `F_X(P)` on polydiscs `P subset X`.
2. Curve coefficients `M_C(D)` on curve discs `D subset C`, acted on by
   the normal-completed algebra `L_{X,C}^{hat}(D)`.
3. Endpoint objects `M_p` and `M_p^vee` at `p in S`, with
   evaluation/coevaluation maps.
4. Descent data for the stratified Ran/Cech nerve of `(X,C,S)`.
5. Orientation-line, charge-completion, and Thom--Sebastiani
   compatibilities whenever Hall comparison is requested.

Perfect means compact and dualizable in this holomorphic factorization
module category, finite over the normal-completed local algebra, and
trace-class for the relevant continuous Dolbeault complexes. This is
the CY3 analogue of CFG's perfect module condition, not its consequence.

### Endpoint/puncture datum

A puncture at `p in C` should be a one-sided module object for the
completed defect algebra on the punctured formal disc:

```tex
M_p in Mod^{cont}_{L_{X,C}^{hat}(D_p^\times)}.
```

It must carry:

1. a Lagrangian BV boundary condition in the normal directions;
2. a compatible orientation square root or local system;
3. a dual object `M_p^vee`;
4. evaluation and coevaluation maps;
5. residue compatibility for normal modes;
6. in class-S shadows, a specified flavor/chiral-sector module.

This is the exact location where CFG endpoint data can be used as a
shadow check, not as the CY3 construction.

## Strongest theorem/proof package available now

### Theorem A: local abelian codimension-2 defect OPE

Status: computed/local theorem.

Let `X = C^3`, let `C = C_{z_1}` be the coordinate curve, and take the
abelian hCS gauge algebra `gl_1`. With Omega-background parameters
`h_1,h_2,h_3`, the normal-completed codimension-2 defect algebra on `C`
has spin-1 current OPE

```tex
J(z)J(w) ~ Psi/(z-w)^2,
\qquad
Psi = -sigma_2 = -(h_1 h_2+h_1 h_3+h_2 h_3),
```

and Sugawara stress tensor

```tex
T(z)T(w) ~ (1/2)/(z-w)^4 + 2T(w)/(z-w)^2 + partial T(w)/(z-w),
\qquad c=1.
```

Proof plan available now. Restrict the six-dimensional hCS propagator
to the codimension-2 defect, keep the two normal formal variables,
read the Heisenberg level from the Omega-normal determinant, and apply
the Sugawara construction. This is implemented in
`compute/lib/hcs_codim2_defect_ope.py:152`,
`compute/lib/hcs_codim2_defect_ope.py:417`, and
`compute/lib/hcs_codim2_defect_ope.py:454`; the manuscript records the
same local formulas at
`chapters/theory/quantum_chiral_algebras.tex:1400` and
`chapters/theory/quantum_chiral_algebras.tex:2151`.

Boundary of theorem. This is local, abelian, low-spin, and chart-level.
It is not a construction of K3 x E holomorphic perfect modules or a
Borcherds trace theorem.

### Theorem B: formal holomorphic trace from a constructed perfect defect

Status: conditional/formal.

Assume:

1. `F_X = PhiFA_3(C)_F` is constructed as an `E_3` holomorphic
   factorization algebra on the framed Stage-1 locus.
2. `C subset X` with endpoints `S` is an admissible holomorphic
   defect datum.
3. `M_C in HolDef^{perf}_{F_X}(C;S)` is compact, dualizable, and
   trace-class.
4. Endpoint objects occur in dual pairs, or the trace is taken in the
   corresponding open/closed bordism type.

Then stratified holomorphic factorization homology produces a trace
class

```tex
Tr^{hol}_{F_X,C,S}(M_C)
  in int^{hol}_{(X,C,S)} (F_X,M_C,{M_p}).
```

After applying Stage 2, it yields a chiral trace class for

```tex
A_C = SpCh_{Sigma_2,C}(F_X)
```

in the factorization homology / Hochschild trace object of the native
`E_1` chiral algebra on `C`.

Proof plan available now. This is the formal `E_{1 subset 3}` Morita
trace theorem with holomorphic coefficients: build the stratified
factorization algebra with bulk value `F_X`, curve value
`End_{F_X}(M_C)`, endpoint values `M_p,M_p^vee`, then apply
factorization homology. CFG proves this grammar in the real
locally-constant CS setting; Vol III may import the formal pattern after
the holomorphic coefficient system and dualizability hypotheses are
supplied. The relevant manuscript trace object is a
factorization-homology module trace, not a Fourier--Mukai trace
(`chapters/theory/phi_universal_trace_platonic.tex:169`).

Boundary of theorem. The theorem is not an existence theorem for
`M_C`. It does not identify the trace with Hall, DT, or Borcherds
characters.

### Conditional theorem C: Hall/Borcherds trace comparison

Status: open until all comparison maps below are constructed.

If the oriented hCS-to-Hall comparison and its module analogue exist,
and if the Hall trace is identified with the relevant automorphic
Borcherds character, then the holomorphic defect trace maps to the
BKM/DT character. This is the desired frontier theorem, but it is not
available now.

## Exact open maps

1. Bulk hCS-to-Hall comparison:

```tex
Theta_{hCS->Hall}^{or}:
  Obs^{q}_{hCS}(X)
  -> CoHA_{crit}^{or,wedge}(X)
```

as a morphism of Hall-valued factorization cosheaves, preserving
vanishing cycles, shifts, Tate twists, orientation square roots,
charge/HN completions, and Thom--Sebastiani products. This is precisely
Problem `op:cy3-hcs-hall-comparison` at
`chapters/theory/cy3_chain_level_bridge.tex:487`.

2. Module/defect comparison:

```tex
Theta_M:
  HolDef^{perf}_{F_X}(C;S)
  -> Perf^{or,wedge}_{CoHA_{crit}(X)}(C;S).
```

This must preserve endpoint duals, orientation local systems, normal
mode completions, charge filtrations, and trace pairings.

3. Specialization/enveloping compatibility:

```tex
SpCh_{Sigma_2,C}(U_P^{fact,E_3}(L_X))
  -> U_C^{ch}(pi_* L_X)
```

with a proof that the holomorphic normal modes are pushed forward by
the correct residue/Omega operation rather than discarded by a CFG-style
de Rham contraction.

4. Locally constant shadow functor:

```tex
LC:
  HolDef^{perf}_{F_X}(C;S)
  -> Perf_{A_lambda}^{top}(K; endpoints).
```

This should recover the CFG module theorem only after a named
topological reduction. It is a test oracle, not a route to Hall/BKM.

5. Endpoint/puncture comparison:

```tex
Punct_{class-S}(Sigma_{0,24})
  -> HolDef^{perf}_{F_X}(C;S).
```

For the K3 x E branch this must compare class-S protected chiral-sector
modules, puncture flavor data, and the chosen K3-fibre specialization.
The wave note records that the candidate curves `E`, the spectral
curve `C`, and `Sigma_{0,24}` are distinct constructions, with no
canonical defect curve (`notes/wave12_c5_chiral_BKM_defect_curve.tex:84`,
`notes/wave12_c5_chiral_BKM_defect_curve.tex:96`).

6. Trace/character comparison:

```tex
Tr^{hol}_{F_X}(M_C)
  -> Tr^{Hall}_{CoHA}(Theta_M(M_C))
  -> Borcherds/DT character.
```

The numerical and automorphic trace identities in
`chapters/theory/phi_universal_trace_platonic.tex:103`,
`chapters/theory/phi_universal_trace_platonic.tex:230`, and
`chapters/theory/phi_universal_trace_platonic.tex:505` are structural
or numerical on their stated domains. They do not replace this
defect-module trace comparison.

## CFG comparison

| Slot | CFG ordinary CS | CY3 Vol III target |
|---|---|---|
| Space | real 3-manifold, locally constant balls | complex CY3, holomorphic polydiscs |
| Differential | de Rham | Dolbeault plus holomorphic jets |
| Local model | `C^*(g)` after local constancy | `CE^{ch,E_3}_{bar partial}(Omega^{0,*},J_hol^\infty l_C)` |
| Defect support | framed real line/link | holomorphic curve with normal formal disk |
| Normal directions | de Rham-contractible | `Sym^hat N_{C/X}^vee`, Omega parameters |
| Endpoint | fermion boundary object, `S_rho` shadow | puncture object with BV/orientation/residue data |
| Perfectness | finite topological `A_lambda`-module | compact/dualizable continuous holomorphic factorization module |
| Trace | RT link invariant | holomorphic/chiral factorization trace, Hall/Borcherds only after open comparisons |
| Braiding | `E_2` module category over topological `E_3` algebra | `E_2` recovered on `Z(Rep^{E_1}(A_C))`, not native on `A_C` |

## Anchors read

- `chapters/theory/cy3_chain_level_bridge.tex:102`: many-variable
  Dolbeault/chiral CE local model for `PhiFA_3`.
- `chapters/theory/cy3_chain_level_bridge.tex:279`: Hall-valued
  factorization-cosheaf target.
- `chapters/theory/cy3_chain_level_bridge.tex:464`: no CFG shortcut.
- `chapters/theory/cy3_chain_level_bridge.tex:487`: hCS-to-Hall
  comparison open problem.
- `chapters/theory/cy3_chain_level_bridge.tex:851`: Stage-1 envelope
  theorem, object-level and anomaly-gated.
- `chapters/theory/cy_to_chiral.tex:4`: headline two-stage
  factorization.
- `chapters/theory/cy_to_chiral.tex:147`: CY trace is negative-cyclic
  data, not only a Hochschild shadow.
- `chapters/theory/cy_to_chiral.tex:229`: definition of
  `PhiFA_d` and `SpCh`.
- `chapters/theory/cy_to_chiral.tex:283`: native operadic level
  `n(d)=1` for `d >= 3`.
- `chapters/theory/cy_to_chiral.tex:389`: CFG is a topological analogue
  and test oracle, not the CY3 source theorem.
- `chapters/theory/cy_to_chiral.tex:407`: CFG `C^*(g)` is only the
  locally constant model; CY3 keeps Dolbeault/jets/residues.
- `chapters/theory/cy_to_chiral.tex:9717`: d=3 theorem scope and
  Drinfeld-center recovery.
- `notes/adversarial_swarm_20260424_cfg_e3/SYNTHESIS.md:14`: CFG
  theorem-grade ordinary CS spine.
- `notes/adversarial_swarm_20260424_cfg_e3/SYNTHESIS.md:70`: killed
  claims including CFG proves `PhiFA_3` and Hall/BKM traces.
- `notes/adversarial_swarm_20260424_cfg_e3/SYNTHESIS.md:183`: open
  obligation to build CY3 holomorphic perfect defect/module categories.
- `notes/adversarial_swarm_20260424_cfg_e3/agent_09_gaiotto_defects_modules.md:19`:
  CFG modules are topological shadows, not CY3 modules.
- `notes/adversarial_swarm_20260424_cfg_e3/agent_09_gaiotto_defects_modules.md:72`:
  proposed local normal-completed CY3 defect model.
- `notes/adversarial_swarm_20260424_cfg_e3/agent_12_topology_e3_trace.md:179`:
  conditional CY3 analogue of CFG trace.
- `notes/adversarial_swarm_20260424_hol_e3/agent_09_gaiotto_defects_modules.md:35`:
  local codimension-2 OPE witness scope.
- `notes/adversarial_swarm_20260424_hol_e3/agent_12_topological_e3_trace.md:231`:
  CFG trace proved; CY3 trace conditional.
- `notes/adversarial_swarm_20260424_hol_e3/agent_15_hostile_synthesis.md:498`:
  build holomorphic defect/module categories before boundary or
  holographic traces.
- `compute/lib/hcs_codim2_defect_ope.py:1`: local codimension-2 OPE
  engine.
- `chapters/theory/quantum_chiral_algebras.tex:522`: universal defect
  and holomorphic Wilson-line language.
- `chapters/theory/quantum_chiral_algebras.tex:1133`: defect algebra
  controlled by ambient holomorphic theory, with 6d not reduced to lower
  dimensions.
- `chapters/theory/quantum_chiral_algebras.tex:1684`: defect algebra
  DAG and K3 x E conjectural status.
- `chapters/theory/quantum_chiral_algebras.tex:2184`: 6d lift of CFG
  Koszul duality remains conjectural.
- `chapters/theory/phi_universal_trace_platonic.tex:169`: object traced
  is a factorization-homology module trace, not Fourier--Mukai.
- `chapters/theory/phi_universal_trace_platonic.tex:489`: six routes to
  `G(K3 x E)` are not six `Phi_3` applications.
- `notes/wave12_c5_chiral_BKM_defect_curve.tex:84`: three candidate
  defect curves are distinct constructions.

## Files changed

- `notes/adversarial_swarm_20260424_frontier_resolution/agent_A4_defects_trace.md`

No manuscript, compute, or test file was edited.

## Verification

No build or tests were run in this pass. Verification was read-only:
the local manuscript anchors, CFG/E3 adversarial reports, holomorphic
E3 reports, defect/OPE compute engine, and wave-12 defect-curve note
were inspected. The compute-backed OPE witness is cited as existing
local evidence, not rerun here.
