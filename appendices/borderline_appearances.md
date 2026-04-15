# Borderline Appearances — Cross-Programme

Claims that are technically correct but could mislead, need deeper investigation, or have ambiguous wording. Updated as the line-by-line pass proceeds.

## Vol I

| # | File | Line | Claim | Issue | Severity |
|---|------|------|-------|-------|----------|
| 1 | introduction.tex | 498 vs heisenberg_frame.tex 48 | sin vs sinh in genus expansion | introduction uses sin (correct positive coefficients); heisenberg_frame used sinh (wrong signs). **FIXED**: heisenberg_frame.tex sinh→sin. The resolution: Â(iℏ) = ℏ/2/sin(ℏ/2). | FIXED |
| 2 | introduction.tex | 1107 | "the denominator k+h^∨ in κ vanishes" | k+h^∨ is in the NUMERATOR of κ=dim(g)(k+h^∨)/(2h^∨). In the Sugawara construction T=Σ:J^aJ_a:/(2(k+h^∨)), k+h^∨ IS the denominator. Ambiguous wording — refers to Sugawara denominator, not κ formula denominator. | LOW |
| 3 | introduction.tex | 1507 | "κ(A) as av(r(z)) at degree 2" | For non-abelian KM, av(r(z)) = κ_dp, not full κ (needs Sugawara shift). But this is a conceptual reframing statement; the full formula was given at L1287. | LOW |
| 4 | introduction.tex | 1753 | "at generic level, ordered chiral homology recovers U_q(g)" | KL equivalence most interesting at root of unity (non-semisimple). At generic level result is trivial (semisimple). The bar complex framework works at all levels. | LOW |
| 5 | chiral_koszul_pairs.tex | 1134-1136 | "dim H^1_CE(Witt_{<0}) = 3" with "three independent cocycles L_{-1}*, L_{-2}*, L_{-3}*" | L_{-3}* is NOT a 1-cocycle: d(L_{-3}*)(L_{-1}, L_{-2}) = L_{-3}*([L_{-1}, L_{-2}]) = L_{-3}*(L_{-3}) = 1 ≠ 0. **FIXED**: corrected to dim=2, cocycles {L_{-1}*, L_{-2}*}, with explicit proof that L_{-3}* fails. Discrepancy 2-1=1. | FIXED |
| 6 | chiral_koszul_pairs.tex | 1434 vs 1488-1495 | Cor says V_k(g) "chirally Koszul at all k including k=-h^∨"; Rem says "full Koszulness (diagonal Ext) fails at k=-h^∨" | **FIXED**: added caveat to Corollary distinguishing PBW-Koszul (condition (ii), holds at all k) from Ext-diagonal (condition (iv), fails at k=-h^∨). | FIXED |

## Vol II

(To be populated as the pass continues)

## Vol III

(To be populated as the pass continues)
