# Agent 08 -- Witten-Polyakov topological and holographic examination

Object attacked: topological, holographic, and quantum-gravity consequences
of the chain-level `Phi_3` / `E_3` holomorphic factorization construction,
compared with Costello--Francis--Gwilliam 2026, arXiv:2602.12412.

Verdict: CFG proves a strong theorem for ordinary perturbative
three-dimensional Chern--Simons theory: BV quantization gives a filtered
`E_3` algebra `A^lambda`, its classical associated local model is
`C^*(g)`, perfect modules encode Wilson-line defects, and the
factorization-homology trace recovers the Reshetikhin--Turaev invariant of
framed links. This is Witten's Chern--Simons logic made algebraic in the
topological, locally constant setting. It is not a theorem about six-real
dimensional holomorphic Chern--Simons on a CY3, not a proof of the
hCS-to-Hall map, not a construction of a K3 x E BKM boundary algebra, and
not a black-hole microstate theorem.

The CY3 avatar must remain
`CE^bullet_{dbar,chir}(Omega^{0,*}_c(P,g)[1], O_P)` or equivalently the
`E_3` Dolbeault/chiral CE and enveloping factorization object with
holomorphic jets in `z_1,z_2,z_3`, multidirectional OPE residues over
polydiscs, and the subsequent `CE -> chiral CE -> U^ch` passage. Ordinary
`C^*(g)` is only the locally constant/topological associated model obtained
after forgetting this data.

## Source anchors

- CFG 2026 arXiv page: submitted 2026-02-12, authors Costello--Francis--Gwilliam, title "Chern-Simons factorization algebras and knot polynomials"; abstract states the filtered `E_3` algebra by BV quantization and perfect modules from Drinfeld--Jimbo representations.
- CFG HTML lines 51--58: Witten's CS path integral is heuristic; CFG proves a perturbative version of Witten/Reshetikhin--Turaev equivalence by factorization homology.
- CFG HTML lines 147--170: ordinary CS observables are locally constant, hence `E_3`, and the classical local model is the Chevalley--Eilenberg algebra `C^*(g)`.
- CFG HTML lines 197--218: quantizations of CS, filtered `E_3` deformations of `C^*(g)`, braided deformations of `Rep(g)`, and quasi-triangular quasi-Hopf quantizations are equivalent up to the named choices.
- CFG HTML lines 225--233 and 1383--1408: Wilson lines are treated as one-dimensional defects; quantization of the coupled system is established by BV/QME and configuration-space renormalization.
- `chapters/theory/cy3_chain_level_bridge.tex:45`: many-variable CY3 chiral CE model; `:98`--`:109`: `C^*(g)` is only the locally constant shadow; `:294`--`:311`: no CFG shortcut; `:317`--`:330`: hCS-to-Hall comparison remains open.
- `chapters/theory/cy_to_chiral.tex:221`: `PhiFA_d` and `SpCh`; `:271`--`:278`: native level is `E_1` at `d >= 3`; `:4681`--`:4753`: framed object-level `d=3` theorem and scope; `:4739`--`:4740`: non-symmetric braiding comes from the Drinfeld center, not from the topological `E_3 -> E_2` restriction.
- `notes/wave13_h5_holographic_QG_synthesis.tex:35`--`:44`: five-layer holography is advertised too strongly; `:97`--`:123`: 6d hCS non-abelian layer is conjectural; `:141`--`:154`: K3 x E BKM identification is conjectural; `:156`--`:202`: quantum-gravity layer separates theorem-grade dyon counting from conjectural BKM chiral-VOA interpretation.
- `notes/wave12_d4_holographic_AdS3.tex:39`--`:80`: DMVV/Sen theorem-grade BPS counting; `:81`--`:124`: class-S and higher-spin BKM claims are partly conjectural.
- `notes/wave12_d5_quantum_gravity_BH.tex:108`--`:143`: RT/entanglement claim is explicitly conjectural and depends on a stress-tensor identification not established.
- `compute/lib/btz_cy3_e1_engine.py:21`--`:60`: shadow Cardy with `kappa_BKM = 5` does not reproduce Strominger--Vafa entropy for K3 x E.
- `compute/lib/cfg25_adversarial_consistency.py:119`--`:195`: no constructed 6d WRT/RT functor; ZTE obstruction blocks the naive pairwise-R-matrix 6d lift.

## Attack-heal cycles

### Cycle 1 -- Witten CS logic versus CY3 hCS

Attack. Import CFG as a proof that the CY3 `E_3` hFA has the same
topological content as ordinary CS.

Failure mode. CFG is theorem-grade for ordinary 3d topological CS on
real balls. The local constancy is the point: the de Rham Poincare lemma
collapses local fields to constant gauge ghosts and yields `C^*(g)`.
The CY3 hCS object is not locally constant in this sense; it retains
Dolbeault fields, holomorphic jets, partial diagonals in polydiscs, and
three residue directions.

Heal. Use CFG as the topological associated model and trace template:

```
CY3 Dolbeault/chiral CE object
  -> forget Dolbeault jets and holomorphic OPE data
  -> locally constant shadow
  -> CFG-shaped C^*(g).
```

Status. CFG ordinary CS statement: theorem. CY3 hCS statement:
conditional theorem on the framed loci and conjectural/open where the
hCS-to-Hall comparison or compact quantization is missing.

### Cycle 2 -- `C^*(g)` as a black hole or holographic algebra

Attack. Treat `C^*(g)` as the algebra whose characters, modules, or traces
control CY3 BPS states and black-hole microstates.

Failure mode. `C^*(g)` has already forgotten the CY3 data needed for BPS
physics: charge gradings, Hall orientation data, Dolbeault propagators,
curve defects, and the K3 x E automorphic denominator. It cannot see
`g[[z_1,z_2,z_3]]`, the Bochner--Martinelli/heat-kernel singularity, or
root multiplicities of `g_{Delta_5}`.

Heal. The physical CY3 object must be written before topologization:

```
Obs_hCS^cl(P)
 = C^bullet_{Lie,cont}(Omega^{0,*}_c(P,g)[1], C),

B_{E_3}(PhiFA_3|_P)
 = CE^{ch,E_3}_*(J_hol^infty L_hCS),
```

with quantum differential
`dbar^vee + d_CE + hbar Delta_BV + counterterms` only after the anomaly
gate is satisfied. The black-hole side may compare to the Hall/BPS
character only after an oriented `Theta_{hCS -> Hall}` map is built.

Status. The local Dolbeault CE formula is definitional/proved on its
named hCS surface. The BPS/Hall comparison is open. Any claim identifying
`C^*(g)` with a black-hole Hilbert space is a metaphor, not a theorem.

### Cycle 3 -- Factorization-homology trace and CY3 defect traces

Attack. Since CFG proves the factorization-homology trace equals the
Reshetikhin--Turaev invariant, assert a CY3 curve-defect trace, a chiral
Kontsevich invariant, or a quantum-toroidal RT invariant.

Failure mode. CFG needs a framed link in a real 3-manifold and a perfect
module over the filtered `E_3` algebra. Vol III has no general perfect
module over the CY3 Dolbeault/chiral `E_3` object, no constructed
holomorphic curve-defect trace with the required QME data, no root-of-unity
truncation for the quantum toroidal algebra, and no Kirby/ZTE-level
invariance theorem for 6-manifolds.

Heal. The admissible theorem form is conditional:

```
Construct the Dolbeault/chiral E_3 observable algebra.
Construct the curve or surface defect as a perfect module.
Apply factorization homology to the stratified holomorphic pair.
Only then compare the resulting trace to Hall/BPS/automorphic characters.
```

CFG supplies the grammar of the trace, not the CY3 defect module.

Status. CFG trace theorem: theorem. CY3 trace theorem: open/conditional.
The existing compute witness confirms this split: `cfg25_adversarial`
marks WRT and RT lifts as major gaps.

### Cycle 4 -- Holographic five-layer overreach

Attack. Read the five-layer K3 x E synthesis as a compound theorem:
class-S, 5d hCS, 6d hCS, CoHA/BPS/BKM, and AdS3 quantum gravity are not
analogies and are all determined by the Gritsenko weight-5 BKM character.

Failure mode. The layers have unequal status. Ordinary theorem-grade
inputs exist: Gaiotto class-S constructions in their scope, Costello's 5d
abelian/Yangian boundary results in their scope, Schiffmann--Vasserot for
`CoHA(C^3)=Y^+`, DVV/DMVV/Sen for `1/Phi_10` dyon counting. But the
non-abelian 6d hCS fixed point, the K3 x E Hall-to-BKM identification,
and the BKM chiral-VOA interpretation of microstates are marked
conjectural locally. CFG does not upgrade these conjectures.

Heal. State the five layers as a status-stratified diagram:

- theorem: CFG topological CS trace in 3d; DVV/DMVV/Sen `1/Phi_10`
  counting; `Delta_5^2 = Phi_10` as automorphic identity; `CoHA(C^3)=Y^+`;
- conditional theorem: CY3 Stage-1 hCS observables on verified/framed
  loci; `Phi_3^{(Sigma_2,C)}` final output as `E_1` on named loci;
- conjecture: K3 x E non-abelian hCS-to-Hall, BKM boundary algebra,
  class-S `Delta_5` embedding, higher-spin BKM enhancement;
- metaphor: "CFG proves the CY3 holographic theory" or "weight 5 alone
  determines quantum gravity."

Status. The five-layer picture survives as a research architecture, not
as a theorem.

### Cycle 5 -- Black-hole entropy and the `Delta_5` chiral half

Attack. Use `kappa_BKM = 5`, `Delta_5`, or `c=-214` directly as the
black-hole entropy central charge or RT entanglement theorem.

Failure mode. The gravity dyon-counting form is `Phi_10`, not `Delta_5`
alone. The theorem-grade physical count is the DVV/DMVV/Sen contour
with `1/Phi_10`, and `Phi_10 = Delta_5^2` is the bridge from the chiral
half to the full left-right gravity index. The compute engine explicitly
warns that the shadow Cardy formula using `kappa_BKM = 5` gives
`c_eff = 10`, while the standard K3 x E CFT uses `c = 24`; these do not
reproduce the same Strominger--Vafa entropy.

Heal. The safe statement is:

```
Delta_5 is the chiral-half Borcherds lift with kappa_BKM = c_1(0)/2 = 5.
Phi_10 = Delta_5^2 is the full gravity-side dyon-counting form.
Black-hole entropy is theorem-grade only when computed from the standard
DVV/DMVV/Sen/Strominger--Vafa index or its established CHL analogue.
```

The BKM algebra `g_{Delta_5}` may be interpreted as a chiral-half BPS
symmetry only conjecturally until its stress tensor, module category, and
Hall/BPS comparison are constructed.

Status. `Phi_10 = Delta_5^2`: theorem. `1/Phi_10` dyon count and leading
entropy: theorem in the standard string-duality scope. "`Delta_5` alone
is the black-hole partition function": false unless explicitly marked as
chiral-half/holomorphic-square-root data. RT entanglement from `c=-214`:
conjecture at best, and physically dangerous without a ghost-cancellation
or nonunitary holography construction.

### Cycle 6 -- Native `E_3`, boundary braiding, and quantum groups

Attack. Infer from CFG that the CY3 output has native non-symmetric
`E_2` braiding, hence a quantum group module category directly at the
algebra level.

Failure mode. CFG obtains an `E_2`-monoidal module category from a
topological `E_3` algebra. Vol III's final `d=3` chiral output is
`E_1`; the non-symmetric `E_2` braiding lives on the Drinfeld center of
the `E_1` representation category. The `E_3 -> E_2` restriction itself
is topologically symmetric because `pi_1 Conf_2(R^3)=0`.

Heal. Preserve the three distinct levels:

```
Stage 1: PhiFA_3(C) -- holomorphic E_3 factorization algebra.
Stage 2: Phi_3^{(Sigma_2,C)}(C) -- E_1 chiral algebra on the curve.
Braided physics: Z(Rep^{E_1}(A)) -- E_2 center / double / R-matrix.
```

Status. The level separation is theorem/definition in the manuscript.
Any claim of native CY3 `E_2` output is false. CFG supports the
module-category route as a model, not a replacement for the center
construction.

### Cycle 7 -- Polyakov one-loop logic and quantum-gravity consequences

Attack. Treat the Polyakov one-loop/threshold story as a consequence of
CFG's BV factorization-homology theorem.

Failure mode. CFG's one-loop/QME analysis controls ordinary CS
renormalization and link defects. Heterotic threshold corrections, Sen
quantum entropy, DMVV symmetric products, and the Borcherds product
`Phi_10` live in string compactification and automorphic-form theorems,
not in CFG. Conversely, hCS on CY3 has a quartic anomaly slot in complex
dimension three, not CFG's ordinary CS deformation complex.

Heal. The legitimate Witten-Polyakov bridge is:

- theorem: Witten CS path integral becomes CFG factorization homology in
  ordinary 3d topological CS;
- theorem: Harvey--Moore/DVV/DMVV/Sen produce `Phi_10` and its entropy
  asymptotics in the K3 x E / CHL string-duality frame;
- conditional/conjectural: CY3 hCS BV observables may furnish the chiral
  half of this BPS algebra after the Dolbeault anomaly gate and
  hCS-to-Hall comparison close;
- metaphor: "CFG explains black-hole entropy" unless the intervening
  defect/Hall/BPS/duality maps are explicitly supplied.

Status. CFG is a topological theorem and a consistency oracle for any
future CY3 trace theorem. It is not a quantum-gravity derivation.

## No-go list

1. Do not identify `PhiFA_3(Perf(X))` with CFG's `C^*(g)`.
2. Do not use CFG to prove `Theta_{hCS -> Hall}`.
3. Do not use CFG Wilson lines to produce CY3 curve-defect traces without
   constructing the perfect Dolbeault/chiral module.
4. Do not call the K3 x E BKM boundary algebra theorem-grade unless the
   Hall/BPS comparison and stress-tensor identification are supplied.
5. Do not compute black-hole entropy from `kappa_BKM = 5` alone. Use
   `Phi_10 = Delta_5^2` and the standard DVV/DMVV/Sen index for theorem
   claims.
6. Do not plug `c=-214` into Ryu--Takayanagi as a theorem. That is
   conjectural and nonunitary unless a full ghost-cancellation
   holographic model is constructed.
7. Do not claim a 6d RT/WRT functor from the quantum toroidal algebra.
   Root-of-unity truncation, surgery/handle moves, ZTE corrections, and
   higher-simplex coherence are not constructed.

## Status recommendations

- `CFG -> ordinary 3d CS filtered E_3 + RT trace`: theorem, cite CFG.
- `CFG -> CY3 topological associated model`: theorem only after explicitly
  applying the forgetful/locally constant shadow functor.
- `CY3 Stage-1 hCS object`: conditional theorem on verified/framed loci;
  write the Dolbeault/chiral CE object, not `C^*(g)`.
- `CY3 final chiral output`: `E_1` on the curve; `E_2` appears through
  the Drinfeld center where constructed.
- `K3 x E BKM / g_{Delta_5}`: automorphic denominator and
  `kappa_BKM = 5` are theorem-grade; identification with the CY3 BPS
  chiral algebra remains conjectural.
- `Black-hole and holographic claims`: theorem only for standard
  DVV/DMVV/Sen/Strominger--Vafa/CHL statements; heuristic or conjectural
  for the chiral-half BKM interpretation; metaphor for direct CFG-to-BH
  derivations.

## Verification run

Commands run:

```
pytest -q compute/tests/test_cfg25_adversarial_consistency.py
pytest -q compute/tests/test_twisted_holography_k3e.py
pytest -q compute/tests/test_entropy_koszul_complement_cy3.py
pytest -q compute/tests/test_btz_cy3_e1_engine.py
```

Results:

- `51 passed` for CFG adversarial consistency.
- `65 passed` for twisted holography K3 x E consistency checks.
- `4 passed` for entropy/Koszul complementarity.
- `134 passed` for BTZ/CY3 `E_1` checks.

Files changed: this report only.
