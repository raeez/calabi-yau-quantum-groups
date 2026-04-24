# Agent 5: Niemeier Siblings and K3 Hodge-Parity Yangian

Date: 2026-04-24

## Claim Attacked

1. One of the 23 non-Leech Niemeier siblings constructs a chain-level compact CY or Fake-Monster host for the Vol III BKM/Yangian branch.
2. The compact K3 Hodge-parity Yangian globalisation can be strengthened beyond conjecture.

## Verdict

No chain-level CY/Fake-Monster host is constructed for any rooted Niemeier sibling.

The 23 siblings supply Niemeier/umbral shadow data: root systems, frame-shape eta products, Coxeter-centred Yangian parameters, and mock-modular polar data. They do not supply a CY category, specialisation cycle, oriented compact critical CoHA, BRST complex, Hall pairing, or denominator/Hall comparison. The Leech/Fake-Monster anchor remains the unique rootless transverse lattice witness for the Fake-Monster row.

The compact Hodge-parity \(Y_\hbar(\mathfrak{so}(4\mid20))\) globalisation remains conjectural. The finite theta-fixed current/reflection-equation algebra \(Y_\theta^{(4\mid20)}\) is a separate finite-rank witness; it does not construct compact Cech--Ran descent, compact critical CoHA, Hall pairing, or coproduct/centre/completion comparison.

## Anchors Preserved

- Scheithauer 2008 Theorem 3.2 and equation (3.5): retained as external super-Borcherds/rescaling anchors.
- Ibukiyama 2000/2012 multiplier restrictions: retained.
- Borcherds Fake-Monster \(\mathrm{II}_{25,1}\) / Leech anchor: retained.
- Gritsenko--Nikulin \(\Delta_5\), \(\Phi_{10}=\Delta_5^2\): untouched.

## Files Changed

- `chapters/examples/k3e_bkm_chapter.tex`
- `chapters/examples/k3_yangian_chapter.tex`
- `compute/tests/test_niemeier_shadow.py`
- `compute/tests/test_umbral_23_niemeier_yangian.py`
- `compute/tests/test_k3_super_yangian.py`
- `compute/tests/test_k3_yangian_adversarial.py`
- `notes/frontier_resolution_swarm_20260424/agent5_niemeier_k3_yangian.md`

## Proof/Obstruction

Non-Leech Niemeier obstruction:

- Direct compute witness: all Niemeier lattice VOAs have rank \(24\), \(\kappa_{\mathrm{ch}}^{\mathrm{Heis}}=24\), class \(G\), depth \(2\), and identical shadow tower.
- Direct root witness: the 23 non-Leech lattices have \(|R(N)|>0\); the Leech lattice has \(|R|=0\). The Fake-Monster BRST construction uses the rootless Leech transverse lattice.
- Category witness absent: no scoped file constructs a compact CY category, a specialisation cycle, a compact critical CoHA orientation, or a Hall-to-Borcherds comparison for a rooted Niemeier sibling.

Hodge-parity Yangian obstruction:

- Ungraded \(Y_\hbar(\mathfrak{so}(4,20))\) is covered by the orthogonal Yangian formalism.
- The finite Hodge-parity theta-fixed current algebra is non-Kac: its odd piece carries a symmetric form, not the Kac \(\mathfrak{osp}\) symplectic odd form.
- Existing tests verify sign grammar and small-rank super-Yangian scaffolding; the manuscript's theta-fixed presentation supplies a finite current algebra. Compact Hall globalisation is still open because no chain-level compact descent, compact critical Hall algebra, Hall pairing, or completed Hopf comparison is constructed.

## Tests Run

Targeted scoped pytest slice:

```bash
python3 -m pytest compute/tests/test_niemeier_shadow.py compute/tests/test_umbral_23_niemeier_yangian.py compute/tests/test_k3_super_yangian.py compute/tests/test_k3_yangian_adversarial.py
```

Result: 248 passed in 1.20s.

## Remaining Open Questions

1. Can one construct an explicit compact CY category and specialisation cycle whose BRST/Hall complex realises a rooted Niemeier umbral denominator?
2. Can the finite theta-fixed \(Y_\theta^{(4\mid20)}\) algebra be upgraded to a compact K3 Hall object with verified coproduct, centre, completion, and reflection-equation compatibility?
3. Can the compact K3 Cech--Ran descent be made compatible with that Hall pairing?
