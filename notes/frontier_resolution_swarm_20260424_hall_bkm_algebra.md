# Frontier Resolution Swarm 2026-04-24: Hall-Drinfeld/BKM Algebra

## Claim Attacked

Lane 2 attacked the full algebra comparison

```tex
D_\hbar(\widehat{\mathrm{CoHA}}^{red}(K3\times E))
\stackrel{?}{\simeq}
\widehat U_\hbar(\mathfrak g_{\Delta_5})
```

starting from `working_notes.tex` Theorem `wn:thm:k3e-final-hall-drinfeld-form`.

Verdict: the theorem is correct only as a universal quotient and rank-two defect criterion.  It is not an unconditional algebra isomorphism.  The proved core is numerical/root-theoretic and Borcherds-side structural; the bridge to a Hall-Drinfeld double remains conditional on product, relation, pairing, completion, negative-half, Cartan, and centre data.

## Status Split

### Proved Core

- Borcherds/Gritsenko denominator side: root multiplicities, parity, PBW, Borcherds-Serre ideal, and primitive enveloping coproduct on finite-height BKM quotients are theorem-grade (`chapters/examples/k3e_bkm_chapter.tex:1372`-`1438`).
- K3 x E numerical shadow: `Z_DT^red(K3 x E) = -Phi_10^{-1} = -Delta_5^{-2}`, `\kappa_{\mathrm{BKM}}(Delta_5)=c_{\phi_{0,1}}(0,0)/2=5`, and primitive superdimensions match `c_{\phi_{0,1}}(4rn-beta^2,l_beta)` (`working_notes.tex:1936`-`1981`, `2034`-`2091`).
- Primitive seed, chamber choice, radical quotient necessity, and signed root multiplicities are numerical theorem-level data (`working_notes.tex:2069`-`2073`).
- The positive-half criterion is valid as a criterion: it does not construct the compact Hall positive half or the comparison map (`chapters/examples/k3e_bkm_chapter.tex:1323`-`1355`).
- The double-admissible template is explicit: finite truncations, product, coproduct, Cartan, Serre-Verdier negative half, continuous Hall pairing, closed Hopf radicals, completion, and representation finiteness (`notes/bps_positive_geometry_total_resolution_20260424/agent_07_drinfeld_double_center.md:69`-`263`).

### Conditional Bridge

The bridge from numerical/PBW data to an algebra isomorphism is exactly the data named in `working_notes.tex:1984`-`2031`:

1. Hall product constants match Borcherds root-addition constants.
2. Hall orientation/Tate signs realize the super signs induced by `c_{\phi_{0,1}}(D,l)`.
3. Completed Hall brackets satisfy the Borcherds imaginary-root and Serre relations.
4. The completed reduced Hopf pairing is nondegenerate.
5. The double coproduct is compatible with the Siegel-Borcherds associator.

The final form at `working_notes.tex:2094`-`2152` correctly says: quotient the completed Hall double by the radical, the kernel of the primitive numerical comparison, and the rank-two Hall-Borcherds defects.  The resulting morphism is an isomorphism if and only if those defects vanish in every effective Mukai chamber.

### Conjectural Residue

What remains is not another denominator calculation.  It is the compact Hall-Drinfeld double construction:

- construct the compact oriented critical Hall algebra on the full DWR/Cech/Ran nerve;
- construct the Hall coproduct with Green compatibility in compact Borel-Moore/vanishing-cycle coefficients;
- construct the Serre-Verdier negative half;
- construct the Cartan completion and its action by the Euler/orientation bicharacter;
- prove the continuous Hall pairing, identify and quotient its closed Hopf radical;
- prove the rank-two Hall-Borcherds product/relation theorem in all effective Mukai chambers;
- prove the completed universal `R`/associator and centre compatibility.

This is why `chapters/theory/cy_to_chiral.tex:10521`-`10539` still records the algebra-level `K3 x E` Hall-Borcherds double as conjectural until positive half, pairing, completion, and bracket comparison are constructed.

## Obstruction Coordinates

Killed:

- `o_prim`: primitive BPS numerical seed, after the Oberdieck-Pixton/DMVV denominator comparison.
- chamber coordinate for support: a positive Borcherds/HN chamber is named; chamber dependence is explicit.
- root-multiplicity coordinate: `sdim Prim_gamma = smult(alpha_gamma) = f(nm,l)`.
- Borcherds target coordinate: finite BKM side has PBW, Serre ideal, parity, and primitive enveloping coproduct.
- radical necessity: radical quotient is forced; null classes cannot survive in the reduced double.

Surviving:

- `o_rad` as an exact closed Hopf radical identification, not just the statement that some radical must be killed.
- `o_Delta`: rank-two Hall-Borcherds defects, i.e. product constants and Serre-super relations in every two-root Hall subalgebra.
- `o_pair`: continuous nondegenerate Hall pairing after completion and radical quotient.
- negative half and Cartan completion: typed in the package, not constructed from `working_notes.tex`.
- `o_cent`: centre/derived-centre compatibility and representation-category finiteness; the braided object lives in the `E_1` categorical centre, not on the positive half.
- completion: finite-height inverse-system compatibility for product, coproduct, pairing, radical, and universal `R`.

## Proposed Final Theorem Statement

For `X=K3 x E`, fix an effective Mukai chamber and suppose the completed reduced oriented Hall algebra is double-admissible: it has a continuous Hall product and coproduct, Serre-Verdier negative half, Cartan completion, continuous Hopf pairing, closed Hopf radical quotient, finite-height completion, and centre-compatible continuous representation category.  Let `Psi_num` be the primitive numerical comparison with `n_+(g_Delta5)`.

Then the assignment of primitive Hall generators to BKM root generators induces a canonical continuous Hopf morphism

```tex
Theta_Hall:
D_hbar(\widehat{CoHA}^{red}(K3\times E))/
<rad, ker Psi_num, rank-two Hall-Borcherds defects>
  -> \widehat U_hbar(g_Delta5).
```

This morphism is an isomorphism if and only if the rank-two Hall-Borcherds defects vanish in every effective Mukai chamber and the double-admissible pairing/completion/centre data above are supplied.  Without those hypotheses, the theorem is only the numerical root-multiplicity and PBW shadow.

## Proof Skeleton

1. Root data: use the Gritsenko-Nikulin/Borcherds denominator for `Delta_5`; local anchors `chapters/examples/k3e_bkm_chapter.tex:528`-`548`, `768`-`790`, and `1372`-`1438`.
2. Enumerative shadow: use the reduced DT character `-Phi_10^{-1}=-Delta_5^{-2}` and the primitive numerical comparison in `working_notes.tex:1936`-`1981`, `2034`-`2091`.
3. Positive half: apply the positive-half criterion in `chapters/examples/k3e_bkm_chapter.tex:1323`-`1369`; this proves an isomorphism only from the four finite-height inputs.
4. Double: require D0-D8 from `notes/bps_positive_geometry_total_resolution_20260424/agent_07_drinfeld_double_center.md:69`-`263`; reduced double is `H^- bowtie H^0 bowtie H^+`.
5. Relations: reduce the remaining algebra problem to rank-two Hall-Borcherds defects as in `working_notes.tex:2109`-`2132`.
6. Centre: use the categorical-centre separation in `agent_07_drinfeld_double_center.md:500`-`511`; `E_2` appears on `Z(Rep^{E_1}(H^+))`, not on `H^+`.

The apparent stronger map in `chapters/examples/k3e_cy3_programme.tex:111`-`142` is only a positive-half coefficient projection.  The sentence that charge addition is respected because both products use the same cone is not a proof of Hall product constants or Borcherds-Serre relations.

## Primary Source Anchors Needed

- Gritsenko-Nikulin 1997/1998: denominator identity and `Delta_5`/Lorentzian Kac-Moody root data.
- Borcherds 1995/1998: automorphic products, weight formula, and BKM denominator formalism.
- Eichler-Zagier 1985: weak Jacobi form `phi_{0,1}` normalization and coefficients.
- Oberdieck-Pandharipande/Oberdieck-Pixton/Oberdieck 2018: reduced `K3 x E` DT/PT/Igusa character identity.
- Kontsevich-Soibelman and Davison-Meinhardt: critical/motivic CoHA, wall-crossing, PBW/integrality.
- Schiffmann-Vasserot and Maulik-Okounkov: toric/local positive-half and stable-envelope models used only as comparison evidence, not as a compact `K3 x E` double proof.

## Computations And Tests Run

- `rg` searches over `notes/` and `chapters/` for Hall-Drinfeld, `g_{Delta_5}`, K3xE/K3 x E, Borcherds, BKM, primitive numerical comparison, radical quotient, Hopf pairing, Cartan completion, negative half, and centre/center compatibility.
- Inspected `working_notes.tex` at `wn:thm:k3e-final-hall-drinfeld-form`, `wn:def:compact-cy3-bridge-package`, `wn:def:compact-cy3-apex-obstruction`, and `wn:thm:compact-cy3-apex-closure` without editing it.
- `/opt/homebrew/bin/pytest compute/tests/test_k3e_coha_structure.py compute/tests/test_bkm_shadow_complete.py compute/tests/test_k3_elliptic_genus_bkm_bar.py`: `231 passed in 12.32s`.
- `python -m pytest` failed because `python` is not on PATH; `python3 -m pytest` failed because that interpreter lacks `pytest`. The Homebrew `pytest` runner succeeded.

## Files Changed

- Created `notes/frontier_resolution_swarm_20260424_hall_bkm_algebra.md`.
- Did not edit `working_notes.tex`.
