# Agent A3: SpCh and Morphism-Level Phi_3

Date: 2026-04-24

Scope: total-resolution attack on issues 3 and 6:
`SpCh_{\Sigma_2,C}` pushforward/envelope commutation beyond witnessed
data and full morphism-level `\Phi_3` for arbitrary CY3
Fourier--Mukai/cyclic morphisms.

Write scope: this report only.

## Verdict

Arbitrary CY3 morphism-level functoriality of `\Phi_3` cannot be proved
from the current hypotheses.

The manuscript now proves the correct object-level statement on the
framed, witnessed locus:

```tex
\Phi_3^{(\Sigma_2,C)}(\mathcal C)
  =
\SpCh_{\Sigma_2,C}(\PhiFA_3(\mathcal C))
```

under H1--H4, after the Stage-1 witness and the Stage-2 specialisation
datum are fixed. The live anchors are:

- `chapters/theory/cy_to_chiral.tex:518`--`555`:
  witnessed admissible specialisation datum.
- `chapters/theory/cy_to_chiral.tex:557`--`577`:
  Stage-1 `\PhiFA_d` is functorial only on constructed loci; the
  Fourier--Mukai formula is explicitly conditional on
  `conj:phi-d-functoriality`.
- `chapters/theory/cy_to_chiral.tex:579`--`597`:
  `SpCh` is exact for an already constructed hFA and witnessed
  specialisation datum.
- `chapters/theory/cy_to_chiral.tex:599`--`618`:
  the two-stage composite is conditional; arbitrary CY3 morphism
  functoriality, hocolim preservation, and global exactness remain
  conjectural unless extra data are verified.
- `chapters/theory/cy_to_chiral.tex:5203`--`5266`:
  framed object-level `d=3` theorem; line `5265` explicitly excludes
  arbitrary CY3 morphisms.
- `chapters/theory/cy_to_chiral.tex:1187`--`1195`:
  per-`d` functoriality is still a conjecture.
- `chapters/theory/cy3_chain_level_bridge.tex:1074`--`1100`:
  the Stage-1 envelope is object-level, not morphism-level, and does not
  reach CoHA.

The strongest exact theorem is not "all Fourier--Mukai kernels act".
It is a theorem for a category of witnessed CY3 specialisation data.
Morphisms in that category are Fourier--Mukai/cyclic kernels equipped
with all coherences below. With those coherences, the construction is
functorial by composition of the specified 2-cells. Without them there
is no canonical morphism-level `\Phi_3`.

## Attack

### 1. A Fourier--Mukai kernel is not a morphism of tagged Phi_3 outputs

The input to the tagged CY3 object is not only `Perf(X)`. It is the
package

```text
(C, X, Omega_X, sigma_C, F, h_S3, Hol_X, completion,
 Sigma_2, C_0, O_{Sigma_2 x C_0}, BC, Fub).
```

A Fourier--Mukai kernel `K in Perf(X x Y)` can preserve the derived
category while failing to preserve the selected surface, curve,
orientation, formality point, chain-level `S^3` framing, Costello--Li
propagator, analytic completion, or Hall chamber. Therefore it is not,
by itself, a morphism

```tex
\Phi_3^{(\Sigma_2,C_0)}(Perf(X))
  \to
\Phi_3^{(\Sigma'_2,C'_0)}(Perf(Y)).
```

This is already encoded in the live text: `prop:phifa-infty1-kernel`
only gives the morphism formula "when the per-`d` functoriality
hypothesis ... is available" (`cy_to_chiral.tex:568`), and
`conj:phi-d-functoriality` remains conjectural
(`cy_to_chiral.tex:1187`--`1195`).

### 2. Stage-2 pushforward does not automatically commute with the envelope

The Stage-1 envelope theorem is

```tex
\PhiFA_3(\mathcal C)_F
  \simeq
\mathrm{Hol}_{X,\Omega_X}
  (\mathcal U^{FA}(\HH^\bullet(\mathcal C)_F)).
```

See `cy3_chain_level_bridge.tex:967`--`1004`. This proves an object in
`\Ethree HolFA(X)` once the formality point and Costello--Li witness are
chosen. It does not prove

```tex
\int_{\Sigma_2}\mathrm{Hol}_{X,\Omega_X}
  (\mathcal U^{FA}(A))
\simeq
\mathrm{Hol}_{C_0}(
  \mathcal U^{FA}_{C_0}(\int_{\Sigma_2} A)).
```

That equivalence is exactly the Fubini/envelope 2-cell inserted in the
witnessed datum (`cy_to_chiral.tex:542`--`545`). It is not a consequence
of the definition of factorisation homology alone. It must include
compact supports, properness on support, Tor-independence, the
Costello--Li propagator, anomaly cancellation, and the chosen
topological-to-holomorphic completion.

### 3. Beck--Chevalley is a datum, not a slogan

The formula

```tex
(\pi_C)_*(\pi_X^*(-)\otimes^L O_{\Sigma_2 x C})
```

requires a square in which the relevant pullback and pushforward are
defined in holomorphic factorisation cosheaves. The current repair
requires a Beck--Chevalley 2-cell
`BC_s` (`cy_to_chiral.tex:538`--`541`). This is sufficient on the
witnessed locus. Outside it, base-change can fail because:

1. the projection is not proper on support;
2. the incidence kernel is not Tor-independent;
3. compactly supported Dolbeault sections do not commute with the
   required pushforward;
4. renormalised BV kernels introduce boundary or anomaly terms;
5. the chosen curve is moved or mixed by the kernel.

### 4. Hall/stable-envelope naturality is a separate theorem

The Hall target carries more data than the chiral object: vanishing
cycles, orientation local systems, Tate shifts, completions,
Thom--Sebastiani isomorphisms, chamber/polarisation/slope choices, and
stable-envelope pairings. A derived equivalence can preserve `Perf(X)`
but cross a chamber wall. In that case the correct output is not equality
but an `R`-matrix or wall-crossing gauge transformation. Thus
stable-envelope naturality cannot be folded into ordinary
Fourier--Mukai functoriality.

The hCS/Hall bridge records the same issue as a descent obstruction:
`cy3_chain_level_bridge.tex:660`--`735` defines the MC, orientation,
grading/Tate, Thom--Sebastiani, and factorisation obstruction tuple.
Those obstructions are independent of `SpCh` and must vanish before any
Hall-valued `\Phi_3` morphism statement can be made.

### 5. Counterexamples and obstruction tests

These are not counterexamples to the witnessed theorem; they are
counterexamples to the overstrong statement "every CY3
Fourier--Mukai/cyclic morphism acts on the tagged `\Phi_3` output".

1. **Moving the specialisation cycle.** On `K3 x E`, translation on the
   elliptic factor sends the fibre `p_E^{-1}(e_0)` to
   `p_E^{-1}(e_0+a)`. The derived category is preserved, and the fibres
   are isomorphic, but the tagged datum has changed. A morphism of
   tagged outputs requires an explicit identification of incidence
   kernels and the Beck--Chevalley cell.

2. **Mixing factors.** A Fourier--Mukai transform on a product or
   abelian CY3 can mix the selected surface direction with the curve
   direction. Then `Sigma_2` is not carried to a witnessed
   `Sigma'_2`, and the residual `E_1` direction is not functorially
   identified.

3. **Changing Hall chamber.** A spherical twist or wall-crossing kernel
   may preserve the CY category and negative-cyclic class but change the
   Maulik--Okounkov chamber. The stable envelope changes by a wall
   `R`-matrix. Equality of `SpCh` outputs is false unless the wall
   operator is part of the morphism.

4. **Failure of Tor-independence.** An arbitrary kernel with bad support
   can make the projection formula for
   `O_{Sigma_2 x C}` fail. Then the displayed push-pull formula is not
   a morphism in `EnHolFA(C)`.

5. **Anomaly mismatch.** The chain-level Stage-1 envelope can be formed
   locally, but landing in `EdHolFA(X)` on compact non-affine `X` depends
   on the Costello--Li holomorphic/anomaly witness
   (`cy3_chain_level_bridge.tex:1088`--`1093`). A kernel that does not
   transport this witness does not act on the holomorphic output.

## Healed Theorem

Define `WSpCY3` as the category whose objects are witnessed CY3
specialisation data

```text
\mathfrak s =
(C, X, Omega_X, sigma_C, F, h_S3, Hol_X, completion,
 Sigma_2, i_{C_0}, O_{Sigma_2 x C_0}, BC_s, Fub_s),
```

where:

1. `C` is a smooth proper CY3 dg category with negative-cyclic CY class
   `sigma_C`;
2. `F` is the chosen `E_3` formality point and `h_S3` is the chain-level
   `S^3` framing homotopy;
3. `Hol_X` is the Costello--Li holomorphic witness, including anomaly
   cancellation and completion;
4. `Sigma_2 subset X` is compact or properly supported with oriented
   normal datum and compact-support convention;
5. `i_{C_0}:C_0 -> X` is the reference curve;
6. `O_{Sigma_2 x C_0}` is the incidence kernel, proper on support and
   Tor-independent for the factorisation-cosheaf tensor product;
7. `BC_s` is the Beck--Chevalley 2-cell identifying pushforward then
   restriction with the kernel formula;
8. `Fub_s` is the Fubini/envelope 2-cell commuting Stage-2 pushforward
   with the `E_3` factorisation products, compact supports, holomorphic
   propagator, and completion.

A morphism

```text
(K, eta): s -> s'
```

is a cyclic Fourier--Mukai or `A_infty` kernel together with the
following coherent isomorphisms:

1. negative-cyclic CY naturality:
   `K_* sigma_C = sigma_C'`;
2. Hochschild/brace naturality compatible with the chosen `E_3`
   formality point;
3. transport of the `S^3` framing homotopy;
4. Costello--Li naturality of the holomorphic refinement, including
   anomaly and completion;
5. support, properness, and Tor-independence of the induced incidence
   correspondence;
6. Beck--Chevalley compatibility:

   ```tex
   \SpCh_{s'} \circ \PhiFA_3(K)
      \simeq
   K_C^{ch} \circ \SpCh_s;
   ```

7. Fubini/envelope compatibility with convolution;
8. identity and associativity coherence for composition of kernels.

If Hall, stable-envelope, or Borcherds targets are invoked, a morphism
also includes:

1. orientation-line square-root transport;
2. vanishing-cycle normalisation;
3. Tate/degree shift convention;
4. Thom--Sebastiani compatibility;
5. chamber/polarisation/slope compatibility, or an explicit
   wall-crossing `R`-matrix;
6. Borcherds banding/pushforward compatibility.

**Theorem.** On `WSpCY3`, the assignment

```tex
\mathfrak s \mapsto
\Phi_3^{\mathfrak s}(\mathcal C)
  :=
\SpCh_{\mathfrak s}(\PhiFA_3(\mathcal C)_F)
```

is a functor to `E_1-HolFA(C_0)` up to the specified coherent
quasi-isomorphisms. It is exact in the Stage-2 variable and symmetric
monoidal under disjoint union of witnessed cycles. Composition follows
from convolution of Fourier--Mukai kernels together with the
associativity coherence of the Beck--Chevalley and Fubini 2-cells.

This theorem is sufficient for every currently verified CY3 use of
`\Phi_3`: toric/formal loci, the K3-fibre branch after the
Hall--Borcherds hypotheses, and any future compact CY3 whose
framing/anomaly/completion witnesses are constructed.

It is also the exact obstruction statement. If any item in the morphism
data is absent, the manuscript has no canonical construction of
`\Phi_3(K)`. An accidental map of the output chiral algebras may exist,
but it is not the morphism-level functoriality of the two-stage
construction.

## Claim-Status Recommendations

1. `def:witnessed-admissible-specialisation-datum`
   (`cy_to_chiral.tex:518`--`555`): keep `ClaimStatusDefinitional`.
   Recommended upgrade: split off a formal definition of "morphism of
   witnessed data" with the eight coherence requirements above.

2. `prop:spch-infty1-kernel`
   (`cy_to_chiral.tex:579`--`597`): keep `ClaimStatusProvedHere` only on
   the witnessed locus. It should never be cited for arbitrary
   pushforward/envelope commutation.

3. `thm:phi-two-stage-derived`
   (`cy_to_chiral.tex:599`--`618`): keep `ClaimStatusConditional`.
   It is the correct object-level composite, not full morphism-level
   functoriality.

4. `thm:phi-platonic`
   (`cy_to_chiral.tex:1104`--`1152`): keep the current status text:
   functorial at `d <= 2`, framed object-level at `d=3`, morphisms
   conjectural.

5. `conj:phi-d-functoriality`
   (`cy_to_chiral.tex:1187`--`1195`): keep `ClaimStatusConjectured`.
   The total-resolution path is to replace the conjecture by the
   `WSpCY3` theorem on witnessed data, not to assert arbitrary
   Fourier--Mukai functoriality.

6. `thm:cy-to-chiral-d3`
   (`cy_to_chiral.tex:5203`--`5266`): keep `ClaimStatusProvedHere`
   under H1--H4 for object-level outputs. Do not cite it for arbitrary
   morphisms, hCS/Hall comparison, global `G(C)`, or compact non-formal
   strictification without extra witnesses.

7. `def:phi-3-cat-master`
   (`chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex:3936`
   --`3980`): current restriction is correct: morphisms exist only where
   the kernel preserves fixed framed data and derived-centre convolution
   is constructed.

## Manuscript Actions for the Main Integrator

1. Add a definition immediately after
   `def:witnessed-admissible-specialisation-datum`:
   "morphism of witnessed admissible specialisation data".

2. Add a proposition after `thm:phi-two-stage-derived`:
   "Functoriality on witnessed CY3 specialisation data", with the
   theorem stated above and `ClaimStatusProvedHere` or
   `ClaimStatusConditional` depending on whether the manuscript treats
   the eight coherence cells as part of the input data or as lemmas to be
   proved.

3. Add a warning sentence to any place citing `SpCh` as a functor:
   exactness means exactness after the factorisation-homology kernel,
   Beck--Chevalley cell, and Fubini/envelope cell are supplied.

4. Keep arbitrary CY3 Fourier--Mukai functoriality in
   `conj:phi-d-functoriality` until all coherence cells are constructed
   naturally from the kernel rather than specified as data.

## Verification

Read-only audit commands:

```bash
git status --short
rg -n "conj:phi-d-functoriality|thm:cy-to-chiral-d3|def:witnessed-admissible-specialisation-datum|prop:phifa-infty1-kernel|prop:spch-infty1-kernel|thm:phi-two-stage-derived" chapters/theory/cy_to_chiral.tex
nl -ba chapters/theory/cy_to_chiral.tex | sed -n '500,620p'
nl -ba chapters/theory/cy_to_chiral.tex | sed -n '1088,1228p'
nl -ba chapters/theory/cy_to_chiral.tex | sed -n '5190,5305p'
nl -ba chapters/theory/cy3_chain_level_bridge.tex | sed -n '930,1100p'
nl -ba chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex | sed -n '3910,3985p'
```

No tests or build were run: this lane is a theorem-scope audit and
report-only write. No manuscript source was edited.

## Files Changed

- `notes/adversarial_swarm_20260424_total_resolution/agent_A3_spch_functoriality.md`
