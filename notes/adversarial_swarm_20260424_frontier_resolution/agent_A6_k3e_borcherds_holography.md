# Agent A6 report: K3 x E Hall-Borcherds closure and holography boundary

## Verdict

The clean theorem can be made manuscript-grade only as a three-layer package:

1. a proved arithmetic/character normalization theorem distinguishing the primitive Borcherds product `Delta_5` from the squared Igusa product `Phi_10`;
2. a conditional Hall-Borcherds specialization theorem for `X = K3 x E` with fibre `Sigma_2 = p_E^{-1}(e_0) \cong K3` and boundary curve `C = E`;
3. a fenced physics corollary saying the holographic/quantum-gravity statements are consequences only after the compact twisted-M-theory, hCS-to-Hall, and boundary/Hall comparison hypotheses are installed.

Without these fences, the current manuscript intermittently overclaims algebra-level closure, confuses primitive and squared Borcherds normalizations, and promotes one-loop physics evidence to theorem status.

## Attacked claims

| Claim attacked | Failure mode | Local anchors | Repair |
|---|---|---|---|
| `kappa_BKM(Phi_10)=5` or equivalent wording. | Literal `Phi_10` has Borcherds weight `10`; the primitive BKM denominator is `Delta_5` of weight `5`. Writing `kappa_BKM(Phi_10)=5` hides the square-root convention. | `main.tex:1354-1358`; `chapters/examples/k3e_cy3_programme.tex:4568-4573`; compare the clean convention in `chapters/examples/k3e_bkm_chapter.tex:470-472`, `:533-548`, `:578-584`, and `chapters/connections/cy_holographic_datum_master.tex:340-378`. | Write `kappa_BKM(g_{\Delta_5}) = kappa_BKM(\Delta_5) = 5`; write `wt(Phi_10)=10=2 kappa_BKM(g_{\Delta_5})`. Avoid `kappa_BKM(Phi_10)` unless it explicitly means product weight `10`. |
| The Jacobi input for `Delta_5` sometimes carries constant `20`. | `c(0)=20` is the full K3 elliptic genus `2 phi_{0,1}` and lifts to `Phi_10`; the primitive denominator `Delta_5` uses the half-genus/Eichler-Zagier `phi_{0,1}` with `c(0)=10`. | `chapters/theory/cy_to_chiral.tex:10936-10976`; `chapters/examples/k3e_bkm_chapter.tex:1599-1632`; Vol I/Igusa anchor `/Users/raeez/igusa-cusp-form/proj.tex:1091-1135`. | Use two symbols: `phi_{\Delta}=\phi_{0,1}^{EZ}` with `q^0` term `y^{-1}+10+y`, and `Z_{K3}=2 phi_{\Delta}` with constant `20`. Then `Bor(phi_{\Delta})=\Delta_5` and `Bor(Z_{K3})=\Phi_{10}=const\cdot\Delta_5^2`. |
| The Hall-Borcherds object is presented as already equal to `Phi_3(DbCoh(K3 x E))`. | The manuscript has character-level and arithmetic evidence, but the positive half, completion, Hopf pairing, bracket comparison, and bialgebra compatibility are not all constructed in this tree. | Overstrong synopsis at `main.tex:762-766`, `:859-864`; conditional theorem already closer at `chapters/theory/cy_to_chiral.tex:719-746`; scope warning at `chapters/examples/k3e_bkm_chapter.tex:53-65`; open construction boundary at `chapters/theory/cy_to_chiral.tex:9586-9604`. | State algebra-level closure only under explicit HB hypotheses. Character identities remain proved externally; bracket/bialgebra equality remains conditional. |
| The associator scalar `lambda=5` is marked proved here. | The text gives plausible normalization routes but no independent explicit associator/Feynman integral computation sufficient for `ClaimStatusProvedHere`. | `chapters/theory/cy_to_chiral.tex:817-844`. | Remove it from the clean theorem. Treat `lambda=5` as a normalization hypothesis or separate proof obligation until a direct associator computation is inscribed. |
| One-loop/holographic/QG consequences are theorem-grade. | The Borcherds identity is arithmetic. Twisted M-theory, compact 24-M5 reduction, boundary algebra, and black-hole interpretation supply evidence or conditional consequences, not a proof of the Hall-Borcherds closure. | Overstrong one-loop claim at `chapters/examples/k3e_bkm_chapter.tex:106-157`; conjectural M-theory framing at `chapters/examples/k3e_cy3_programme.tex:4775-4816`; good fence at `chapters/connections/cy_holographic_datum_master.tex:424-461`; local-to-compact caveat needed around `chapters/connections/cy_holographic_datum_master.tex:1724-1758`. | Move physics to a conditional corollary: if compact twisted-M-theory reduction, hCS exponentiation, and boundary/Hall comparison are proved, then the boundary partition function is compatible with `Phi_10^{-1}` and primitive chiral half `Delta_5^{-1}`. |

## Repaired theorem package

### Theorem 1: arithmetic normalization for `K3 x E`

Let `phi_Delta = phi_{0,1}^{EZ}` be the weight-zero, index-one weak Jacobi form normalized by

```tex
phi_Delta(\tau,z)=y^{-1}+10+y+O(q).
```

Let `Z_{K3}=2 phi_Delta`, so its `q^0 y^0` coefficient is `20`. Then:

```tex
Bor(phi_Delta)=\Delta_5
```

up to the standard scalar and `Z -> 2Z` convention, and

```tex
wt(\Delta_5)=\frac{10}{2}=5.
```

The full K3 elliptic genus lifts to the squared product

```tex
Bor(Z_{K3})=\Phi_{10}=const\cdot \Delta_5^2,
\qquad
wt(\Phi_{10})=\frac{20}{2}=10.
```

Thus the primitive BKM invariant is

```tex
\kappa_{\mathrm{BKM}}(\mathfrak g_{\Delta_5})
=\kappa_{\mathrm{BKM}}(\Delta_5)
=\frac{c_{\Delta}(0)}{2}
=\frac{10}{2}=5.
```

The reduced DT/DVV/Oberdieck-Pandharipande partition function is the square:

```tex
Z_{\mathrm{red}}(K3\times E)
= C\cdot \Delta_5^{-2}
= C'\cdot \Phi_{10}^{-1},
```

with the prefactor convention fixed locally as `p q t` or absorbed into `C`.

For the CHL-averaged ladder `N in {1,2,3,4,6}`:

```tex
c_N(0)=(10,8,6,4,2),
\qquad
\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2=(5,4,3,2,1).
```

This is a Borcherds/Gritsenko weight theorem, not an Euler-characteristic identity.

### Theorem 2: conditional Hall-Borcherds specialization

Let

```tex
X=K3\times E,\qquad p_E:X\to E,\qquad
\Sigma_2=p_E^{-1}(e_0)\cong K3,\qquad C=E.
```

Assume:

- `HB1`: a CY3 hCS-to-Hall comparison for `Perf(K3 x E)` producing the oriented Hall positive half;
- `HB2`: compatibility of that comparison with specialization to the K3 fibre `Sigma_2=p_E^{-1}(e_0)` and holomorphic pushforward to `C=E`;
- `HB3`: a nondegenerate Hall pairing and completion so that the Hall-Drinfeld double exists;
- `HB4`: the Hall denominator/root-multiplicity comparison identifies the completed double with the primitive `Delta_5` Borcherds denominator;
- `HB5` only for bialgebra enhancement: compatibility with coproduct, associator, and universal `R`-matrix.

Then the Stage-2 specialization of the CY-to-chiral output is conditionally

```tex
\operatorname{SpCh}_{K3,E}
  \bigl(\Phi^{FA}_3(\operatorname{Perf}(K3\times E))\bigr)
\simeq
U_{\mathrm{ch}}(\mathfrak g_{\Delta_5})
```

as an `E_1` chiral algebra. Under `HB5`, this upgrades to the chiral bialgebra/Hall-Drinfeld-double statement. Its primitive denominator invariant is `5`; its squared DT/dyonic character is governed by `Phi_10^{-1}`.

This theorem does not assert a general construction of `G(X)`, does not say the six routes to `G(K3 x E)` are six applications of `Phi`, and does not make `A` itself `E_2`. The `E_2` structure belongs on the derived centre/Drinfeld-centre side.

### Corollary 3: holography and quantum-gravity fence

Assume Theorem 2 and, in addition, a compact twisted-M-theory reduction on `K3 x E`, an all-loop hCS exponentiation theorem, and a boundary/Hall comparison for the compact model. Then the boundary/QG partition function is compatible with

```tex
Z_{\mathrm{boundary}}=C'\Phi_{10}^{-1}=C\Delta_5^{-2},
```

while the primitive chiral algebraic half has BKM weight `5`.

Without those physics hypotheses, the legitimate statement is weaker: the Borcherds arithmetic gives `Delta_5`, OP/DVV gives the squared `Phi_10` character, and the one-loop `2+3=5` calculation is a matching witness. It is not a proof of compact holography, all-order QG, or the Hall-Drinfeld double construction.

## Exact constants and non-identities

- `p_E^{-1}(e_0) = K3`; this is the K3 fibre used in the Stage-2 specialization.
- `c_Delta(0)=10` for the primitive `phi_{0,1}^{EZ}` input.
- `kappa_BKM(g_Delta5)=10/2=5`.
- `Z_K3=2 phi_Delta` has constant `20`.
- `Phi_10=const\cdot Delta_5^2` has weight `10`.
- `kappa_cat(K3 x E)=chi(O_{K3}) chi(O_E)=2\cdot 0=0`.
- compact Hodge/BV supertrace for `K3 x E` is `0`.
- Heisenberg specialization has `kappa_ch^{Heis}=3`.
- fibre Euler witness `kappa_fiber(K3)=24`; fibre holomorphic Euler witness `chi(O_{K3})=2`.
- The additive formula `kappa_BKM = kappa_ch + chi(O_fiber)` is false. With total-space conventions it gives `0+0`; with K3-fibre holomorphic Euler it gives `0+2`; with the Heisenberg specialization it gives `3+2=5` only accidentally and must not be used as a theorem.

## Recommended manuscript edits

1. Replace every intended primitive statement `kappa_BKM(Phi_10)=5` by `kappa_BKM(g_{\Delta_5})=5`; reserve `wt(Phi_10)=10` for the squared partition function.
2. Normalize Jacobi inputs explicitly: `phi_Delta` has constant `10`; `Z_K3=2 phi_Delta` has constant `20`.
3. Move unconditional `H_{\Delta_5}=Phi_3(DbCoh(K3 x E))` language behind `HB1`-`HB5`.
4. Demote or isolate `cy_to_chiral.tex` associator-scalar theorem until the scalar is computed directly.
5. Fence holography/QG claims as conditional corollaries, using `chapters/connections/cy_holographic_datum_master.tex:424-461` as the local model.

## Primary/source anchors inspected

- `chapters/theory/cy_to_chiral.tex:420-455`, `:719-800`, `:817-844`, `:9586-9604`, `:10878-10976`.
- `main.tex:420-450`, `:762-864`, `:1313-1366`, `:1844-1855`.
- `chapters/examples/k3e_bkm_chapter.tex:15-65`, `:67-157`, `:470-585`, `:959-1005`, `:1599-1632`, `:2090-2138`, `:2231-2244`.
- `chapters/examples/k3e_cy3_programme.tex:4528-4573`, `:4775-4844`, `:4937-4965`.
- `chapters/examples/cy_d_kappa_stratification.tex:131-185`, `:2018-2115`, `:2326-2382`, `:2471-2511`.
- `chapters/connections/cy_holographic_datum_master.tex:340-378`, `:424-461`, `:1600-1660`, `:1724-1786`, `:1838-1945`.
- Vol I/Igusa normalization: `/Users/raeez/igusa-cusp-form/proj.tex:1091-1135`, `:1180-1197`.
- Bibliography anchors available in `bibliography/references.tex`: Borcherds 1998, Gritsenko-Nikulin 1995/1998, Gritsenko 1999, Gritsenko-Clery 2013, Oberdieck-Pandharipande 2018, Oberdieck-Pixton 2019.

## Files changed

Only this report:

```text
notes/adversarial_swarm_20260424_frontier_resolution/agent_A6_k3e_borcherds_holography.md
```

No manuscript source was edited.
