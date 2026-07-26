# Wave 17 Unified Cross-Check Engine

Engine file: `k3_yangian_unified_cross_check.py`
Test suite: `compute/tests/test_k3_yangian_unified_cross_check.py`

End-to-end verification of the Wave-14 / Wave-15 / Wave-16 claims on the
non-abelian K3 chiral bialgebra $\mathbf{H}_{\Delta_5}$.

## Eight cross-checks

| Tag | Identity | Primary route | Cross-check routes |
|-----|----------|---------------|--------------------|
| A | $\hbar^2 \cdot K^{\kappa_{\mathrm{ch}}} = -1$ | Lusztig $\ell = 8 \Rightarrow \hbar^2 = -1/8$ | Mukai $K = 2c_+ = 8$; Humbert $H_1$ order 8 (Bruinier 2002) |
| B | $(c_{4d}, c_{2d}) = (107/6, -214)$ | Chacaltana-Distler $(5n-13)/6$ at $n=24$ | Beem-Rastelli $c_{2d} = -12 c_{4d}$; SU(2) $N_f=4$ sanity |
| C | BKM Cartan rank 3; Mukai rank 24 | Gritsenko-Nikulin 1997 Gram det $= -32$ | Mukai lattice $II_{4,20}$; $K = 2 c_+ = 8$ |
| D | $\mathrm{wt}(\Delta_5) = 5$ | $\eta^9 \theta_1$ weight $9/2 + 1/2$ | $\chi(\mathcal{O}_{\mathrm{K3}}) + $ Kodaira $= 2 + 3$; paramodular anomaly |
| E | Five-frame duality convergence | Harvey-Moore het $K3 \times T^2$ | IIA DMVV; IIB D1-D5; M on $K3 \times T^3$; F on elliptic-$K3$ |
| F | Heegner pattern $c_n \propto [H_n]$ | Bruinier Prop 5.1 multiplicities | EOT 2011 $c_{K3}$ table at disc $\in \{-1, 0, 3\}$ |
| G | Arthur $\psi_{\Delta_{10}} = \phi_{\Delta_{E_6}} \boxplus \mathrm{Sym}^1$ | Ikeda / Andrianov Hecke formula | First-principles $a_p(f_{18}) = a_p(E_6 \Delta)$; Ramanujan-Petersson |
| H | Schur index $\mathrm{PE}[(72q - 22q^2)/(1-q)]$ | Gadde-Rastelli-Razamat-Yan | BLLPRvR; Beem-Peelaers-Rastelli 2014 |

## How to run

```bash
# Engine demo (prints pass/fail table plus highlights)
python3 -m compute.lib.k3_yangian_unified_cross_check

# Test suite (58 assertions across A-H plus cache audit and global consistency)
python3 -m pytest compute/tests/test_k3_yangian_unified_cross_check.py -v
```

Expected outputs: 8/8 cross-checks PASS; 58/58 tests PASS.

## Interpretation

**All 8 passing means**: the Wave-14, Wave-15, and Wave-16 compute modules
are numerically consistent across the universal identity, central charges,
lattice ranks, Siegel weight, five-frame duality, Heegner divisor pattern,
Arthur packet, and Schur-index Fourier expansion. The engine does not
re-derive — it cross-binds.

**Failure modes and what they'd mean**:

- **A fail**: some face of $K^{\kappa_{\mathrm{ch}}} = 8$ disagrees with the
  others. Would indicate that Mukai doubling, Humbert monodromy, or Lusztig
  root-of-unity has drifted in a predecessor module.
- **B fail**: $(c_{4d}, c_{2d})$ pair disagrees with $(5n-13)/6$ evaluation
  at $n=24$. The Wave-14 retraction to $26$ would re-emerge if the
  Chacaltana-Distler pants-decomposition fit is reverted.
- **C fail**: BKM Gram determinant drifted from $-32$ or Mukai signature
  from $(4,20)$. Indicates a lattice-ambient conflation or a sign error in
  the simple-root table.
- **D fail**: $\mathrm{wt}(\Delta_5) \neq 5$ via at least one of the three
  routes. Would flag a pumping of the Gritsenko weight formula or a
  miscount of Kodaira I_1 fibres.
- **E fail**: some duality frame disagrees on weight or Narain lattice.
  Strong signal that a cross-frame identification has been corrupted.
- **F fail**: EOT $c_{K3}$ table drift (disc $-1, 0, 3$). A silent
  re-indexing of the Heegner label convention (e.g. $H_n$ vs disc $4n-1$)
  would trigger this.
- **G fail**: first-principles $a_p(f_{18})$ disagrees with the transcribed
  table OR Ramanujan-Petersson bound fails. Former indicates an $E_6$ or
  $\Delta$ Fourier-expansion error; latter indicates a stale Hecke
  eigenvalue.
- **H fail**: Schur-index plethystic expansion disagrees with manuscript
  table. Indicates the $(72, -22)$ generator pair has drifted, or
  plethystic-exponential computation is incorrect.

## Cache-violation audit

The engine's `cache_violation_audit()` records the top 5 confusion-patterns
that the Wave-14/15/16 synthesis was constructed to avoid:

1. **CoHA $\neq$ chiral**: CoHA$(\mathbb{C}^3) = Y^+$; the Phi-functor maps
   to (not equals) a chiral algebra.
2. **$\kappa_{\mathrm{cat}}(\mathrm{K3} \times E) = 0$** (not 2): Künneth
   vanishing on $\chi(\mathcal{O}_E) = 0$.
3. **Native vs. derived $E_n$**: $\mathbf{H}_{\Delta_5}$ is $E_1$-native on
   $E$, $E_2$-derived on factorization.
4. **Six routes distinct**: five duality frames + class-S avatar = six
   DIFFERENT morphism families converging to $\mathbf{H}_{\Delta_5}$, not
   six $\Phi$-functors.
5. **Averaging vs. derived centre**: Mukai doubling (averaging-invariant)
   and Bruinier Prop 5.1 (derived-centre) independently produce 8.

## Predecessor modules

Directly imported (10):

- `k3_yangian_schur_index_classS_A1_24.py` (cross-check H)
- `k3_yangian_arthur_hecke_delta10.py` (cross-check G)
- `k3_yangian_gritsenko_additive_explicit.py` (cross-checks D, F)
- `k3_yangian_twisted_11dsugra_1loop.py` (cross-checks D, E, F)
- `k3_yangian_bi_based_ran.py` (dataclass import only)
- `k3_yangian_pentagon_coboundary_hbar3.py` (Phi_10 leading value)
- `k3_yangian_humbert_monodromy_8.py` (cross-check A)
- `k3_yangian_M24_umbral_cocycle_order6.py` (Schur multiplier)
- `k3_yangian_pentagon_coboundary_hbar45.py` (EOT normalisation)
- `k3_yangian_schur_index_classS_ANm1_24.py` (cross-check B)

## Primary literature (aggregated across all cross-checks)

- Mukai 1987, Tata Inst (Mukai lattice and moduli of bundles on K3).
- Bruinier 2002, Lecture Notes Math 1780, Prop 5.1 (Heegner Chern classes).
- Lusztig 1990, Geom. Dedicata 35 (quantum groups at roots of unity).
- Gritsenko 1999, St. Petersburg Math. J. 6 (additive lift).
- Gritsenko-Nikulin 1997-98 (product-side BKM denominator).
- Eguchi-Ooguri-Tachikawa 2011, Exp. Math. 20 (K3 elliptic genus).
- Borcherds 1998, Invent. Math. 132 (singular-theta lift).
- Chacaltana-Distler 2010, arXiv:1008.5203 (class-S pants).
- Beem et al. 2013, arXiv:1312.5344 (4d / 2d correspondence).
- Ikeda 2001, Ann. Math. 154 (Saito-Kurokawa lift at degree 2).
- Andrianov 1974, Russian Math. Surveys 29:3 (spinor L-factor).
- Deligne 1974; Weissauer 2009 (Ramanujan-Petersson, elliptic and Siegel).
- Gadde-Rastelli-Razamat-Yan 2011, arXiv:1110.3740 (Schur-index PE).
- Harvey-Moore 1996, Nucl.Phys.B 463 (heterotic threshold).
- Witten 1995 + Vafa 1996 + Morrison-Vafa 1996 II (duality frames).

## Status

Wave-17 unified cross-check: **all 8 PASS**. The Wave-14 / Wave-15 /
Wave-16 synthesis is numerically self-consistent at the 58-assertion level.
