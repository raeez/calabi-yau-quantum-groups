# Beilinson Audit: cy_to_chiral.tex (Wave 13)

**Target**: /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex (1547 lines)
**Mode**: Six-hostile-examiner deep audit, read-only
**Prior waves**: 8-4 (opening rewrite), 9-9 (AP113 kappa-subscript sweep, 15 bare kappa fixed)
**Date**: 2026-04-09

---

## (a) Per-Examiner Counts

| Examiner | Focus | Issues |
|----------|-------|--------|
| 1. Operadic/definitional | E_n levels, functor signature | 2 MODERATE |
| 2. Conditionality/scope (AP-CY6/11/14) | d=3 claims, environment choice | 4 SERIOUS |
| 3. kappa-spectrum (AP113) | subscript compliance | 0 (CLEAN) |
| 4. Numerics/verification | dimension counts, multi-path | 3 MODERATE |
| 5. Prose/AI-slop | writing discipline | 1 MINOR |
| 6. Cross-volume/architectural | AP5, AP-CY2, AP-CY17 | 3 SERIOUS |

**Total: 13 findings (7 SERIOUS, 5 MODERATE, 1 MINOR)**

---

## (b) AP113 kappa-Subscript Verification (Post-Wave-9-9)

Grep of `\kappa` across all 1547 lines: **every occurrence is subscripted.** Scanned 43 hits across lines {4, 43, 207, 236, 338, 368, 481, 536, 539, 543-549, 555-557, 630, 683, 787-788, 1127-1139, 1156, 1163, 1192, 1205, 1246-1249, 1276, 1285-1309, 1324-1341, 1367, 1430-1432, 1471-1473, 1483-1497, 1510-1519}. All subscripts: `\kappa_{\mathrm{ch}}` (dominant), `\kappa_{\mathrm{BKM}}`, `\kappa_{\mathrm{BCOV}}`, `\kappa_{\mathrm{MacMahon}}`. Zero bare `\kappa`. **Wave 9-9 is clean.** The polysemy remark (line 1510-1520) explicitly disambiguates the four roles, consistent with Vol III kappa-spectrum mandate.

---

## (c) d=3 Scope Audit (AP-CY6/AP-CY11/AP-CY14)

Status of statements passing through A_X at d=3 or CY-A_3:

1. **Conjecture CY-A_3** (line 1218, `conj:cy-to-chiral-d3`): correctly `\begin{conjecture}` + `\ClaimStatusConjectured`. **PASS.**
2. **Theorem CY-A_2** (line 32, `thm:cy-to-chiral`): scoped to d=2 in title + signature; uses S^2-framing. **PASS.**
3. **Theorem e1-universality-cy3** (line 577, `\ClaimStatusProvedHere`): statement explicitly limited to *toric* CY_3 with T^3-equivariant Omega-deformation; compact case deferred to conj:cy-to-chiral-d3. **PASS on scope**, but SERIOUS concern below on conditionality propagation.
4. **Conjecture tilting-chart-cover** (line 660): `\begin{conjecture}` + `\ClaimStatusConjectured`. **PASS.**
5. **Conjecture e1-chart-gluing** (line 711): `\begin{conjecture}`. **PASS.**
6. **Corollary kappa-from-charts** (line 1127, `\ClaimStatusProvedHere`): statement hedged with "Conditional on the existence of A_C (Conj e1-chart-gluing)". Environment is corollary, not conjecture, but prose makes the conditionality explicit. **BORDERLINE.** Per AP-CY11 strict reading, this should be `\begin{conjecture}` with `\ClaimStatusConditional` because its proof chain passes through conj:e1-chart-gluing which is ultimately downstream of CY-A_3. The "Conditional on" hedge is insufficient.

---

## (d) Top 5 Findings

**F1 [SERIOUS, AP-CY11/AP-CY14]**: `cor:kappa-from-charts` (line 1127) carries `\ClaimStatusProvedHere` but its conclusion depends on `conj:e1-chart-gluing` (conjectural) and transitively on `CY-A_3`. Per AP-CY11 conditionality propagation, downgrade to `\begin{conjecture}` with explicit dependency chain, OR introduce `\ClaimStatusConditional` and cite the chain.

**F2 [SERIOUS, AP-CY6/AP-CY14]**: `cor:cya3-no-topological-obstruction` (line 233) is marked `\ClaimStatusProvedHere` but asserts a property of an unconstructed object (the d=3 CY-to-chiral functor). Topological triviality of the obstruction is defensible, but the phrasing "For all toric CY_3 tested... the E_1 -> E_2 enhancement obstruction vanishes" slides back toward constructive claims. Recommend: rename to "Topological vanishing of the CY-A_3 obstruction" and clearly state "assuming CY-A_3 is formulated with the symplectic structure group" or similar.

**F3 [SERIOUS, AP-CY2]**: Lines 15, 20, 45, 215, 1226 reference `HH_\bullet(\cC)` (Hochschild homology) as the bearer of the S^d-framing. Per AP-CY2, the CY trace and S^d-framing live on HC^-_d (negative cyclic), NOT HH_d. The chapter conflates the two throughout the four-step construction. At minimum, a footnote or remark should state "Throughout we write HH_\bullet; the S^d-framing refines this to HC^-_\bullet per AP-CY2 (Keller, Kontsevich-Soibelman)." Currently absent.

**F4 [SERIOUS, AP-CY17]**: Line 700 (Gepner remark for the quintic) mentions MF(W_Fermat) with W = x_0^5 + ... + x_4^5 (5 variables), but never states the CY dimension of MF(W). Per AP-CY17, for W: A^n -> A^1, MF(W) is CY_{n-2}, so MF(W_Fermat with 5 vars) = CY_3. Consistent, but the chapter never makes this explicit, and any reader pattern-matching the n-1 error risks miscounting. Recommend inserting "(CY_3 by Dyckerhoff: n-2 = 3)" at the Gepner mention.

**F5 [MODERATE, numerics]**: `prop:center-hocolim` (line 1081) asserts for the conifold: "local centers have dimension 3, global center has dimension 1, Obs = 2", with a parenthetical "braiding anomaly of 2/3". The 2/3 has no derivation trail and doesn't match the 3-1=2 shown in the proof. Either (a) the 2/3 is a typo for "2 of 3", or (b) it's a ratio with unstated normalization. Per AP10, every numerical value needs a derivation trail. Add a footnote or delete the "2/3" parenthetical.

Additional findings (brief):

**F6 [MODERATE]**: `thm:c3-functor-chain` (line 82) is marked ProvedHere and Step 5 claims "the quantum vertex chiral group G(C^3) is recovered"; G(X) is AP-CY7/AP43 territory (G(X) assumes the global chiral-group object which is part of the d=3 programme). Recommend weakening Step 5 to "the E_2-braided representation category is identified with Rep^{E_2}(Y(hat gl_1))" without invoking G(C^3) at theorem status.

**F7 [MODERATE, operadic]**: Line 37: signature is `Phi: CY_2-Cat -> E_2-ChirAlg`. Per Vol III CLAUDE.md Identity: the functor target is `E_2-ChirAlg` at d=2 but the document uses `\Etwo\text{-}\mathrm{ChirAlg}` consistently. Good. However, line 6 and line 8 use `\En\text{-}\mathrm{ChirAlg}` generically, which blurs the d-dependence. Recommend stating signature parameterized: `Phi_d: CY_d-Cat -> E_{d-1}-ChirAlg` or similar, with explicit d=2 case.

**F8 [MODERATE, AP132 bar complex]**: The chapter never writes the bar complex of A_C as `T^c(s^{-1} overline{A_C})` (augmentation ideal). References to bar complex (e.g. lines 42, 484-508, 1114) invoke B(A) without showing the augmentation. AP132 enforcement: add a defining formula somewhere near `prop:c3-bar-euler` stating `B(A) = T^c(s^{-1} bar A)` for reader orientation.

**F9 [MODERATE, AP30]**: `conj:dt-hocolim-shadow` (line 1148) uses the scalar formula `F_g = kappa_ch * lambda_g^FP` on "the uniform-weight lane". Per Vol I AP32/AP30, the shadow flat-identity scalar formula is conditional and tagged (UNIFORM-WEIGHT). The remark at line 1160 partially addresses this. Recommend explicit (UNIFORM-WEIGHT) tag on F_g.

**F10 [MODERATE, cross-volume AP5]**: Line 1276 invokes "kappa_ch(H_1^!) = -1" and complementarity "kappa_ch(A) + kappa_ch(A^!) = 0" on the KM/free-field lane. This is correct per Vol I AP24 but should cross-cite `\ref` to the Vol I complementarity theorem, not merely name the AP.

**F11 [MINOR, prose]**: Line 1022 "This is the reason the hocolim construction succeeds for CY_3 but cannot directly produce an E_2-algebra" uses "succeeds" as vague prose; replace with the precise mechanism ("degenerates at E_2"). Borderline hedging; rewrite for crispness.

**F12 [MODERATE, AP139 variable binding]**: `thm:kappa-c3` statement (line 536) bundles three distinct equalities `kappa_ch(C^3) = kappa_ch(W_{1+inf}, c=1) = kappa_ch(H_1) = 1`. The first equality presupposes the functor Phi(C^3) is defined, which at d=3 passes through CY-A_3. The equality `W_{1+inf} at c=1 = H_1` is a genuine VOA theorem. Recommend separating: Claim 1 (VOA identity, unconditional), Claim 2 (functor output, conditional).

**F13 [SERIOUS, AP-CY11]**: `thm:c3-drinfeld-center` (line 421, ProvedHere) and `thm:e1-universality-cy3` (line 577, ProvedHere) jointly underwrite the d=3 functor chain for C^3. Both are marked ProvedHere but the whole C^3 verification uses the unconstructed A_X logic at Step 4-5 (passing through the Drinfeld double and "quantum vertex chiral group"). The C^3 case is uniquely unconditional ONLY at the character/R-matrix level, not at the "G(C^3) is the quantum vertex chiral group" level. Recommend splitting: the character/algebra identifications are ProvedHere; the G(X) identification is ProvedElsewhere (Schiffmann-Vasserot, Kontsevich-Soibelman) or recast as a Remark.

---

## (e) Health Grade

**B+ (strong with systemic propagation gaps)**

The chapter is mathematically rich, genuinely novel (CY-A_2 as unconditional, Cech homotopy for quintic, E_1 descent degeneration as the structural heart of the d=3 programme), and the Wave 9-9 AP113 sweep is fully compliant. The opening (Wave 8-4 "Where do chiral algebras come from?") is in the CG deficiency-opening style and works well. The d=3 conditionality is explicitly handled for the big conjectures (CY-A_3, tilting-chart-cover, e1-chart-gluing, dt-hocolim-shadow, cy-koszul-mirror all correctly in \begin{conjecture}).

**However**, the conditionality does not propagate per AP-CY11. Several downstream ProvedHere results (F1, F2, F6, F13) silently depend on CY-A_3 or conj:e1-chart-gluing but carry theorem-level status. This is the exact pattern AP-CY11/AP-CY14 target. The AP-CY2 HH_d vs HC^-_d conflation (F3) is a systemic notation issue affecting the four-step construction. AP-CY17 is technically respected but not made explicit (F4).

**Recommended fixes for Wave 14**: (i) downgrade F1/F13 to conjecture or add \ClaimStatusConditional; (ii) insert AP-CY2 notation remark near the four-step construction; (iii) explicit AP-CY17 citation at the Gepner remark; (iv) uniform-weight tags on F_g scalar formulas; (v) remove or derive the 2/3 braiding-anomaly parenthetical.

Word count: ~520
