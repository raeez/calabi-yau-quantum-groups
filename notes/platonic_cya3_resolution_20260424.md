# CY-A3 Witnessed-Functoriality Primitive, 2026-04-24

## Claim Attacked

The object-level CY-A3 theorem might be read as global functoriality of
`\Phi_3` on arbitrary CY3 morphisms.

## Resolution

The object theorem does not imply arbitrary morphism functoriality.  The
strongest closed statement in the owned scope is the finite witness
criterion now inscribed as
`chapters/theory/cy_to_chiral.tex`,
Corollary `cor:cya3-finite-witness-package`.

Within the chapter's two-stage construction, a CY3 morphism is in the
proved functorial scope exactly when it carries:

1. fixed `E_3` formality point and `GRT_1(Q)` gauge;
2. negative-cyclic CY3 class plus cyclic bar-transfer homotopy;
3. chain-level `S^3` framing homotopy compatible with Costello TCFT;
4. Costello--Li naturality, anomaly cancellation, and OPE completion;
5. witnessed Stage-2 specialization with Beck--Chevalley, Fubini,
   compact-support, properness, and Tor-independence cells;
6. coherent convolution unit and associativity cells.

If one item is absent, the object-level outputs may still exist, but no
two-stage morphism `SpCh o PhiFA_3(f)` is defined in the target.

## Remaining Primitive Obligations

For compact non-formal examples such as the quintic, the topological
`S^3` vanishing and Cech perturbative homotopy are not enough.  The
remaining primitive is an explicit cyclic framing homotopy plus OPE
completion compatible with the Costello--Li anomaly witness.

For arbitrary CY3 morphisms, the remaining primitive is construction of
the witness package above for the chosen kernel.  This is the open part
of Conjecture `conj:phi-d-functoriality`, not a consequence of
Theorem `thm:cy-to-chiral-d3`.
