# Frontier Resolution Swarm 2026-04-24: Phi_3 Kernel Witnesses

Lane: 3 of 6, `Phi_3^{wit}` witnessed kernel data.

Write scope: this report only.

## Claim Attacked

The primitive question in `working_notes.tex:2905-2912` asks whether the
seven kernel cells for `Phi_3^{wit}` can be constructed:

1. proper/perfect support;
2. negative-cyclic orientation transport;
3. cyclic transfer;
4. `E_3` formality with `S^3`-framing compatibility;
5. Costello--Li naturality/completion;
6. Stage-2 base-change cells;
7. convolution units/associativity.

The maximal-domain theorem in `working_notes.tex:4771-4805` is correct:
`Phi_3^{wit}` is theorem-level only on a category whose objects and
morphisms already carry those witnesses. Extending it to all compact
CY3 kernels is exactly the missing construction problem.

## Verdict

**Proved core.** The manuscript proves the formal theorem: if the
seven witnesses are supplied, `Phi_3^{wit}` is functorial. This is
`def:phi3-admissible-kernel-datum`, `thm:phi3-witnessed-kernel-functoriality`,
`prop:phi3-arbitrary-morphism-obstruction-criterion`, and
`cor:cya3-finite-witness-package` in
`chapters/theory/cy_to_chiral.tex:678-916`.

**Conditional bridge.** Several witnesses are constructed on restricted
loci: perfect-support for diagonal/spherical/flop/McKay kernels
(`chapters/examples/derived_categories_cy.tex:544-582`); casewise
witnessed kernels after extra orientation/cyclic/framing/completion data
are attached (`derived_categories_cy.tex:585-657`); pentagon coherence
once convolution cells are supplied (`derived_categories_cy.tex:659-700`);
and a local Morse--Bott matrix-factorisation locus where K1--K7 are
claimed canonically from the local hypothesis
(`cy_to_chiral.tex:951-1093`).

**Conjectural residue.** No source in the inspected tree constructs all
seven witnesses for arbitrary compact non-formal CY3 Fourier--Mukai
kernels. The compact non-formal residue is not philosophical: it is the
explicit chain-level `S^3` framing transport, Costello--Li naturality
and analytic completion, Stage-2 Beck--Chevalley/Fubini/Tor cells, and
higher convolution coherences for each kernel.

## Seven Witness Audit

| Witness | Local status | Killed coordinates | Surviving coordinates |
|---|---|---|---|
| K1/O1 proper/perfect support | Proved for standard geometric kernels under strict support hypotheses; local Morse--Bott has finite Tor amplitude. | Diagonal, spherical twist, simple flop off the exceptional curve, and McKay universal-family support. | Arbitrary compact kernels still need finite Tor amplitude, properness over both factors, strict-fibre support, and closure under convolution. |
| K2/O2 negative-cyclic orientation transport | Built into witnessed datum; local Morse--Bott claims volume/cyclic preservation supplies it. | Identity and explicitly cyclic/volume-preserving local morphisms. | Determinant-line transport and a Connes-closed homotopy carrying `[\sigma_C]` to `[\sigma_D]` are not automatic for a raw FM kernel. |
| K3/O3 cyclic transfer | Constructed when the morphism is a cyclic `A_infty` functor preserving negative-cyclic complexes; Merkulov sign for `f_0` is fixed. | `b`, `B`, and curved `f_0` sign convention on witnessed strict loci. | Compatibility with `B^{(2)}` and the full `S^3` Connes hierarchy remains data for general compact kernels. |
| K4/O4 `E_3` formality and `S^3` framing | Derived/topological obstruction vanishing is proved after the formality point and chain-level framing witness are fixed. | `HH^{-2}_{E_1}` and topological `pi_3(BSp)` obstructions on the stated connective/unit-connected/symplectic loci. | The actual chain-level `A_infty`-compatible `S^3` framing homotopy and its transport through a kernel remain genuine hypotheses outside local/product cases. |
| K5/O5 Costello--Li naturality/completion | Sufficient cell is specified; local/toric hCS and Morse--Bott routes give partial construction. | Local holomorphic-factorisation maps where the Costello--Li witness and completion are fixed. | Compact holomorphic-twist naturality, anomaly transport, and OPE completion under arbitrary kernels are unconstructed. |
| K6/O6 Stage-2 base-change cells | Proved only for witnessed specialisation data. | Beck--Chevalley/Fubini/projection-formula cells when supplied by the datum. | Kernels moving or mixing `(\Sigma_2,C)`, failure of Tor-independence, compact-support failure, and envelope/pushforward noncommutation. |
| K7/O7 convolution units/associativity | Formal once K7 cells are supplied; FM associativity supplies the raw geometric pattern. | Identity kernel and pentagon on the witnessed tower. | Higher coherences are not derived from arbitrary kernels; they must be supplied or constructed by a relative BV model. |

## Obstruction Coordinates

The live obstruction criterion is exact:
`cy_to_chiral.tex:806-857` lists O1--O7 and states that without the
corresponding choices there is no defined composite
`SpCh o PhiFA_3(f)`. The finite witness package at
`cy_to_chiral.tex:859-916` compresses the same data into W1--W6.

For `working_notes.tex:2840-2891`, this kills only the `Phi_3^{wit}`
branch of the apex vector when K1--K7 are supplied. It does not kill the
separate Hall cosheaf, hCS-to-Hall, Drinfeld-double, OPE, or boundary
host coordinates.

## Proposed Final Theorem Statement

Let `CY_3-Cat_{Phi_3}^{wit}` be the category of witnessed CY3 objects
and witnessed kernels of `def:phi3-admissible-kernel-datum`: objects
carry H1--H4 of `thm:cy-to-chiral-d3`, a formality point, chain-level
`S^3` framing, Costello--Li anomaly/completion witness, and witnessed
Stage-2 datum; morphisms carry K1--K7.

Then

```tex
\Phi_3^{wit}:
CY_3-Cat_{\Phi_3}^{wit}
  -> E_1-HolFA(C_0)^{(\infty,1)}
```

is an `(infty,1)`-functor, sending
`x` to `SpCh_s(PhiFA_3(C))` and a witnessed kernel to the Stage-2
specialisation of the Stage-1 Costello--Li naturality map. If any K-cell
is absent, `thm:cy-to-chiral-d3` may still give two object-level outputs,
but it gives no morphism between them. On the isolated Morse--Bott
matrix-factorisation locus the seven cells are conditionally constructed
from the finite Jacobian/cyclic local model; outside that locus, and in
particular for arbitrary compact non-formal CY3 kernels, the global
construction of K1--K7 remains a genuine hypothesis.

## Proof Skeleton With Local Anchors

1. Object construction: `thm:cy-to-chiral-d3` gives the framed object
   under H1--H4 and witnessed specialisation; it explicitly excludes
   arbitrary morphisms and global `G(C)`.
2. Witness definition: `cy_to_chiral.tex:678-737` defines K1--K7.
3. Formal functoriality: `cy_to_chiral.tex:739-804` proves functoriality
   because K1--K7 are part of the source category.
4. Necessity: `cy_to_chiral.tex:806-857` proves that omitting any cell
   leaves `SpCh o PhiFA_3(f)` undefined.
5. Finite package: `cy_to_chiral.tex:859-916` records the finite witness
   package and flags compact non-formal examples such as the quintic as
   still requiring explicit cyclic framing and OPE completion.
6. Standard kernels: `derived_categories_cy.tex:544-700` proves support,
   casewise witnessed kernels, and pentagon coherence only under stated
   witness hypotheses.
7. Local construction locus: `cy_to_chiral.tex:951-1093` supplies the
   Morse--Bott local-germ construction; its scope is local/isolated, not
   arbitrary compact CY3.
8. Cross-volume check: Vol I bar/cobar and Vol II Swiss-cheese material
   consume the chiral algebra and its open/closed structure; targeted
   greps did not find a cross-volume construction of the missing compact
   CY3 kernel cells.

## Primary Source Anchors Needed Before Any Upgrade

- Perfect support and convolution: Mukai 1981; Bondal--Orlov 1995;
  Bridgeland--King--Reid 2001; Lipman 2009; Neeman 1996.
- Negative-cyclic CY and cyclic functors: Kontsevich--Soibelman 2006;
  Ginzburg 2006.
- Cyclic transfer/BV: Merkulov 2005; Dolgushev--Tamarkin--Tsygan 2007;
  Tradler--Zeinalian; Van den Bergh 1998; Menichi 2009.
- `E_3` formality/framing: Kontsevich 1999; Tamarkin 2007; Willwacher
  2015; Lurie HA Dunn additivity; Costello open-closed TCFT.
- Holomorphic twist/completion: Costello--Gwilliam 2017;
  Costello--Li 2016/2020; Costello--Li--Williams 2020.
- Stage-2 base change: Lurie HA 5.5.3; Francis--Gaitsgory 2012.
- Local Morse--Bott construction: Dyckerhoff 2010; Polishchuk--Vaintrob
  2010; Ayala--Francis 2012; Berger--Gurski--Kapranov 2004.

## Computations and Tests Run

No build or tests were run. Verification was read-only: `sed`, `nl`,
`rg`, `find`, and `git status --short`, plus targeted Vol I/II greps.

## Files Changed

- `notes/frontier_resolution_swarm_20260424_phi3_kernel_witnesses.md`
