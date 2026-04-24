# Agent 09 - Holography / Quantum-Gravity Consequences

Report-only adversarial audit. No manuscript files were edited.

## Scope

Audited the holography / quantum-gravity claims in:

- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md`
- `notes/vol3_rearchitecture_proposal.tex`
- `notes/platonic_synthesis_post_adversarial.tex`
- `chapters/connections/cy_holographic_datum_master.tex`
- `chapters/connections/*.tex` by targeted search
- Vol I cross-volume anchors:
  - `/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex`
  - `/Users/raeez/chiral-bar-cobar/chapters/connections/master_concordance.tex`
  - `/Users/raeez/chiral-bar-cobar/worldview_synthesis_2026_04_17.tex`

Verdict: theorem-grade Borcherds / Igusa arithmetic is mostly stable. The
failure mode is status inflation: physics readings, AdS3 black-hole language,
and universal trace comparisons are sometimes written as theorem-level
consequences of `\Phi_3` before the comparison maps are proved.

Tests run:

```bash
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider \
  compute/tests/test_bps_entropy_shadow.py \
  compute/tests/test_bps_microstate_shadow.py \
  compute/tests/test_genus2_chiral_partition.py \
  compute/tests/test_twisted_holography_k3e.py
```

Result: `271 passed in 2.88s`.

## ATTACK_1: AdS3 dyon formula is overpackaged as a theorem

Claim attacked: the AdS3 throat / dyon degeneracy package is theorem-grade as a
CY-to-chiral consequence.

Failure mode found:

- `notes/platonic_synthesis_post_adversarial.tex:1135-1183` declares
  `Near-horizon throat and dyon count` with `\ClaimStatusTheorem`.
- The denominator is written as `1/\Phi_{k_N}^2`
  (`notes/platonic_synthesis_post_adversarial.tex:1152-1157`). At `N=1`,
  the physical CHL weight is `k_1 = 10`, so this reads `1/\Phi_{10}^2`.
  The DVV/Igusa convention and the compute witnesses use
  `1/\Phi_{10} = 1/\Delta_5^2`, not `1/\Phi_{10}^2`.
- The same theorem ends with
  `graviton finiteness = E_2-chiral rigidity`
  (`notes/platonic_synthesis_post_adversarial.tex:1178-1182`), but no
  comparison theorem identifies the physical graviton finiteness statement
  with Hochschild rigidity of the K3 Mukai-Heisenberg sector.
- The architecture note is more honest:
  `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:360`
  marks the leading statement proved and all-orders statement conjectural.
- Compute-side arithmetic agrees with the conservative reading:
  `compute/lib/bps_entropy_shadow.py:42-44` says
  `\Delta_5^2 = const * \Phi_{10}` and BPS degeneracies are coefficients of
  `1/\Phi_{10}`; `compute/tests/test_genus2_chiral_partition.py:499-505`
  tests `Z_2^{K3xE}=1/\Phi_{10}`.

## HEAL_1

Split the result into three statements:

1. External physics theorem/computation: near-horizon geometry, Brown-Henneaux
   central charge, and DVV/CHL contour formula, cited as physics input.
2. Exact modular identity: at `N=1`,
   `\Phi_{10} = const * \Delta_5^2`, hence the relevant reciprocal is
   `1/\Phi_{10} = const^{-1}\Delta_5^{-2}`.
3. CY-to-chiral comparison: the claim that the Stage-2
   `\mathbf H_{\Delta_5}|_E` boundary recovers the full dyon partition
   function is conjectural unless a BRST-to-Borcherds / universal trace
   comparison is supplied.

Proposed edit:

```tex
d_N(Q,P)=\oint_{\mathcal C_N}
  \frac{e^{-i\pi(Q,\Omega)\cdot T(Q,\Omega)^T}}
       {\Phi_{k_N}(\Omega)}\,d\rho\,d\sigma\,dv,
```

or, if the square-root convention is intended, explicitly write
`\Phi_{k_N}=\Delta_{k_N/2}^2` and keep the denominator unsquared.

## ATTACK_2: `\Delta_5` one-loop output is stronger than the proof

Claim attacked: `\Delta_5` is a one-loop-forced output of twisted 11D
supergravity, agreeing with the CY-to-chiral programme "to all orders at one
loop."

Failure mode found:

- `chapters/connections/cy_holographic_datum_master.tex:421-453` states
  `\Delta_5` is the one-loop output and gives the arithmetic
  `wt(\Delta_5)=2+3=5`.
- `chapters/connections/cy_holographic_datum_master.tex:1633-1649` repeats
  the twisted-M-theory reading and says four duality frames confirm the same
  arithmetic numerically.
- The theorem-grade part is narrower and solid:
  `chapters/connections/cy_holographic_datum_master.tex:359-375` proves only
  `wt(\Phi_{10})=2\kappa_{\mathrm{BKM}}=10`, with
  `\kappa_{\mathrm{BKM}}=c_1(0)/2=5` and
  `\Phi_{10}=const\cdot\Delta_5^2`.
- The compute slice verifies the modular identity and weight convention, not
  the twisted-11D anomaly derivation:
  `compute/tests/test_twisted_holography_k3e.py:183-190` separates
  `\Delta_5` weight 5 from Siegel-Igusa `\Phi_{10}` weight 10.

## HEAL_2

Keep the Borcherds / Igusa statement theorem-grade. Recast the twisted-M-theory
paragraph as a physical heuristic or computed witness:

```tex
The Borcherds weight computation gives
\(\kappa_{\mathrm{BKM}}(\mathfrak g_{\Delta_5})=c_1(0)/2=5\).
The twisted-M-theory one-loop calculation is evidence for the same weight:
it predicts the decomposition \(5=2+3\) from the K3 Hodge summand and the
Kodaira-residue contribution. This physics comparison is not used as a proof
of the Borcherds weight identity.
```

Replace "agree to all orders at one loop" by "agree at the checked one-loop
weight level."

## ATTACK_3: `\Phi_3(K3\times E)` is collapsed with the BKM algebra

Claim attacked: the BKM route, the `\Phi_3` output, and the universal trace
identity are already a proved single object.

Failure mode found:

- Vol III notes correctly state the boundary:
  `notes/vol3_rearchitecture_proposal.tex:334-338` says the
  `\Delta_5` denominator identity is theorem-grade, but its bar Euler product
  comparison is conditional on CY-A3, Vol I bar-cobar, and CY-C arrows.
- The same proposal keeps six-route convergence conjectural:
  `notes/vol3_rearchitecture_proposal.tex:340-356` and `563-582`.
- `chapters/connections/cy_holographic_datum_master.tex:1011-1018` labels
  the Universal `\Phi`-Trace Identity as a conjecture.
- But `chapters/connections/cy_holographic_datum_master.tex:2138-2141`
  says each projection preserves it and the supertrace equals weight 5 in
  every slice, with no conditional qualifier.
- Vol I has the sharpest collision:
  `/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:4499-4502`
  says `\Phi_3(K3\times E)` is the Gritsenko-Nikulin BKM algebra
  `\mathfrak g_{\Delta_5}`. This contradicts the Vol III separation:
  `\Phi_3` gives an `E_1`-chiral boundary object; the BKM algebra is a
  Stage-2 / Borcherds specialisation route.
- The same Vol I passage says
  `as \Phi_{10}=\Delta_5 in the Vol III labelling`
  (`holographic_datum_master.tex:4521-4523`), but the verified convention is
  `\Phi_{10}=const\cdot\Delta_5^2`.

## HEAL_3

Make the governing statement:

```tex
The BKM route attached to \(K3\times E\) is
\(\mathfrak g_{\Delta_5}\), with
\(\kappa_{\mathrm{BKM}}=c_1(0)/2=5\). The object
\(\Phi_3(D^b\mathrm{Coh}(K3\times E))\) is the \(E_1\)-chiral boundary
object on the verified framed locus. Identifying its universal trace or bar
Euler product with the BKM denominator is the Universal \(\Phi\)-Trace
Identity / CY-C comparison, hence conditional.
```

Vol I should replace `\Phi_3(K3\times E) is \mathfrak g_{\Delta_5}` by
"the BKM route attached to \(K3\times E\) is \(\mathfrak g_{\Delta_5}\)."
It should also replace `\Phi_{10}=\Delta_5` by
`\Phi_{10}=const\cdot\Delta_5^2`.

## ATTACK_4: `\mathcal W_{1+\infty}` / lambda / Bethe-root claims leak into theorem form

Claim attacked: the CY3 Gaudin theorem proves the full
`\mathcal W_{1+\infty}` Bethe-spectrum and DT-root multiplicity statements.

Failure mode found:

- The local guard is correct:
  `chapters/connections/cy_holographic_datum_master.tex:721-724` says
  `\mathrm{CoHA}(\mathbb C^3)=Y^+` and
  `\mathcal W_{1+\infty}` appears only after Drinfeld double / centre /
  vacuum evaluation.
- The battle note also separates the two lambda parameters:
  `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:155-157`
  distinguishes `\lambda_{\mathrm{Tr}}` from `\lambda_W`.
- But `chapters/connections/cy_holographic_datum_master.tex:948-972`
  marks the full Face 7 statement `\ClaimStatusProvedHere`, including:
  (ii) spectrum governed by `\mathcal W_{1+\infty}` Bethe ansatz, and
  (iii) DT counts supplying Bethe-root multiplicities.
- The proof sketch at `chapters/connections/cy_holographic_datum_master.tex:985-994`
  proves only the Gaudin commutativity from the classical Yang-Baxter
  equation and cites the `\mathcal W_{1+\infty}` vacuum-evaluation side.
  It does not prove a DT/PT-to-Bethe-root bijection.
- Vol I's `\mathcal W_\infty` endpoint theorem
  (`/Users/raeez/chiral-bar-cobar/worldview_synthesis_2026_04_17.tex:673-689`)
  should not be imported as a CY3 theorem without the Drinfeld-centre and
  evaluation hypotheses.

## HEAL_4

Split Face 7:

- ProvedHere: Gaudin Hamiltonian commutativity for `\mathbb C^3` from the
  classical Yang-Baxter equation of the doubled affine Yangian residue.
- ProvedElsewhere / cited: `\mathcal W_{1+\infty}` vacuum-evaluation Bethe
  ansatz for the full doubled Yangian in the relevant Fock modules.
- Conjectural or computed evidence: DT/PT plane partitions furnish the Bethe
  root multiplicities beyond character-level agreement.

Keep the lambda warning adjacent to every `\mathcal W_{1+\infty}[\lambda]`
use: `\lambda_{\mathrm{Tr}}=-1` under the CY3 equivariant constraint is not the
free Gaiotto-Rapcak `\lambda_W`.

## ATTACK_5: Monster / Fake Monster / `\mathfrak g_{\Delta_5}` are not one CY3 holographic family

Claim attacked: Monster, Fake Monster, and the K3 `\Delta_5` BKM are
dimension-stratified outputs of one CY3 holographic mechanism.

Failure mode found:

- `chapters/connections/cy_holographic_datum_master.tex:1381-1408` correctly
  warns that the three BKM algebras are not one tier-(iii) family, but then
  says Monster `V^\natural` is at `d=3`, arising from a CY3 whose Mukai
  lattice is the Leech lattice with signature `(25,1)`.
- The battle note is stricter:
  `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:81-85`
  treats Conway / Monster transport as a boundary phenomenon and says no
  compact CY3 supplies the needed Niemeier rank-24 transverse data; Fake
  Monster is a `d=5` cousin, obstructed at `d=3`.
- Vol I's corollary
  `/Users/raeez/chiral-bar-cobar/worldview_synthesis_2026_04_17.tex:637-647`
  is a standalone lattice-VOA / Moonshine statement about
  `V^\natural`, not a proved AdS3 x K3 or CY3 `\Phi_3` consequence.

## HEAL_5

Rewrite the Monster paragraph as a boundary / Vol I lattice-VOA phenomenon
unless a concrete CY3 category and lattice realisation are supplied:

```tex
Monster \(V^\natural\) is a Vol I lattice-VOA / Moonshine boundary object.
It is not presently realised as a tier-(iii) \(K3\times E\) CY3
specialisation. The K3 \(d=3\) BKM route is
\(\mathfrak g_{\Delta_5}\); the Fake Monster remains a \(d=5\) or
hostless Borcherds cousin.
```

Any quantum-gravity consequence involving Monster moonshine must name the
twining map, the CHL/M24 sector, and the comparison to the K3 dyon partition
function. Otherwise it remains motivational.

## ATTACK_6: Black-hole entropy mixes `24`, `3`, and `5` unless the invariant lane is named

Claim attacked: the black-hole entropy is controlled by the same invariant
that controls the chiral shadow, the fibre rank, or the route count.

Failure mode found:

- `notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md:360`
  says "24-count six-way" in the Witten row; this is too compressed.
- `notes/platonic_synthesis_post_adversarial.tex:1144-1150` correctly says
  the reduced Brown-Henneaux central charge is `24` and that
  `k_N=24/(N+1)-2` is a Borcherds weight, not a central charge.
- `chapters/connections/cy_holographic_datum_master.tex:1878-1899` correctly
  keeps the four-value `K3\times E` spectrum
  `{0,3,5,24}` in four distinct lanes and says none is a VOA central charge of
  `\Phi_3(D^bCoh(X))`.
- Compute-side entropy arithmetic says the leading entropy is governed by the
  discriminant/Cardy saddle, while the modular weight enters subleading terms:
  `compute/lib/bps_entropy_shadow.py:46-55` and `72-74`.

## HEAL_6

Use the following lane separation everywhere:

- `c_L^{reduced}=24`: physical D1-D5 / MSW / Brown-Henneaux central-charge
  datum.
- `\kappa_{\mathrm{fiber}}=24`: Mukai-lattice rank / Kodaira-fibre count.
- `\kappa_{\mathrm{ch}}^{Heis}=3`: Heisenberg mode-trace anomaly.
- `\kappa_{\mathrm{BKM}}=5`: Borcherds weight of `\Delta_5`, controlling the
  modular-weight lane and subleading Rademacher correction.
- `1/\Phi_{10}=1/\Delta_5^2`: dyon / DT reciprocal form at `N=1`.

Never compress these as "24-count six-way" in theorem prose.

## Proposed manuscript edits

1. In `notes/platonic_synthesis_post_adversarial.tex:1135-1183`, demote the
   CY-to-chiral comparison part of the AdS3 theorem to conjectural/heuristic
   and fix the CHL denominator to `1/\Phi_{k_N}` unless a square-root notation
   is explicitly introduced.
2. In `chapters/connections/cy_holographic_datum_master.tex:421-453` and
   `1633-1649`, relabel the one-loop `2+3=5` reading as physics evidence,
   not the proof of `\kappa_{\mathrm{BKM}}=5`.
3. In `chapters/connections/cy_holographic_datum_master.tex:2138-2141`, add
   "assuming Conjecture `conj:universal-trace-identity`" before asserting the
   supertrace equals weight `5` in every slice.
4. In Vol I
   `/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:4499-4523`,
   replace `\Phi_3(K3\times E)=\mathfrak g_{\Delta_5}` by the BKM-route
   formulation and fix `\Phi_{10}=\Delta_5` to
   `\Phi_{10}=const\cdot\Delta_5^2`.
5. In `chapters/connections/cy_holographic_datum_master.tex:948-972`, split
   the Face 7 theorem into commutativity (proved), `\mathcal W_{1+\infty}`
   vacuum evaluation (cited/external), and DT/PT Bethe multiplicities
   (conjectural or computed witness).
6. In `chapters/connections/cy_holographic_datum_master.tex:1381-1408`, remove
   the claim that Monster `V^\natural` arises from a CY3 with Leech Mukai
   lattice unless a concrete CY3 category and specialisation map are supplied.

## Remaining open questions

1. Is there a primary-source-complete derivation of the one-loop
   `2+3=5` decomposition in the twisted-11D/K3 x E setting, or is it only a
   duality-frame mnemonic?
2. Can the Universal `\Phi`-Trace Identity be proved at `K3\times E`, even
   just for the value-level equality `K(\Phi_3(K3\times E))/2=5`?
3. Is there an actual CY3 source category producing a Monster/Leech
   specialisation, or should Monster be kept entirely in the Vol I lattice-VOA
   and hostless Borcherds lanes?
4. Can the DT/PT-to-Bethe-root multiplicity claim in Face 7 be proved beyond
   character-level agreement for `\mathbb C^3`?
5. Which CHL notation is canonical in the manuscript: physical
   `\Phi_{k_N}` of weight `k_N`, or square-root Borcherds forms
   `\Delta_{k_N/2}`? The denominator formula must choose one.
