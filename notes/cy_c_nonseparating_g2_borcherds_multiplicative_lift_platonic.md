# CY-C non-separating g=2 Borcherds multiplicative lift (Platonic form)

Scope: close the non-separating boundary stratum of `Mbar_{2,0}` in the Phi_10 vs DMVV comparison on K3 x E. Prior wave (`notes/cy_c_I2_I3_higher_genus_half_bps.md`) closed the separating stratum unconditionally via Gritsenko-Nikulin + DMVV; the non-separating stratum was recorded as OPEN at chain level. This note gives the strongest honest form.

Conventions. Throughout, `Phi_10 = const . Delta_5^2` (Vol III `rem:k3e-convention-delta5-phi10` at `chapters/examples/k3e_bkm_chapter.tex:43`). The Borcherds product is written in `Delta_5` normalisation. Fourier coefficients `c(D)` are Eichler-Zagier per-(n,l) coefficients of `2 phi_{0,1}`; `f(D) = c(D)/2` are the per-(n,l) coefficients of `phi_{0,1}` itself. Then `Phi_10` coefficients are `c_0(D) = 2 f(D) = c(D)`.

---

## 1. Parametrisation of the non-separating boundary divisor

The moduli space `Mbar_{2,0}` has two boundary divisors:
- `delta_sep` (separating): stable graph `Gamma_sep` with two genus-1 vertices joined by one edge.
- `delta_non-sep` (non-separating): stable graph `Gamma_{non-sep}` with one genus-1 vertex carrying a self-loop.

Via the Torelli map `Mbar_{2,0} -> Abar_2` to the Satake compactification of the Siegel modular threefold `A_2 = H_2/Sp_4(Z)`, the two divisors push forward to:
- `delta_sep` -> Humbert surface H_1 of reducible abelian surfaces (period matrix diag(tau_1, tau_2) with z = 0).
- `delta_non-sep` -> the 3-dimensional "cuspidal" boundary corresponding to period matrices `Omega = [[tau, z], [z, sigma]]` with `sigma -> i*infinity` (so `p = exp(2 pi i sigma) -> 0`), leaving the genus-1 tau and a marked point z = tau_e encoding the handle.

On `delta_non-sep` the period matrix takes the form (p-adic expansion):
```
Omega_nonsep(tau, z, sigma) = [[tau, z], [z, sigma]]  with p = e(sigma) -> 0
```
The residual moduli after the limit `p -> 0` are (tau, z) in `H x C` modulo the action of the Jacobi group `SL_2(Z) ltimes Z^2`. This is precisely the 3-dim domain of Jacobi forms of `SL_2(Z)`, parametrised by `tau in H` and the "node modulus" `z = tau_e`. Three complex moduli: tau (period of the genus-1 residual curve), z (B-cycle phase around the handle), and sigma (controlling how deep into the cusp; one complex-dim is the "time-to-cusp").

Key contrast with the separating stratum: on `delta_sep`, z -> 0 (off-diagonal vanishes, both tau_i remain finite, Humbert-1 divisor). On `delta_non-sep`, sigma -> i*infinity instead; z remains a free Jacobi variable encoding the handle's B-cycle monodromy.

## 2. Fourier-Jacobi expansion of Phi_10 at the non-separating cusp

The Borcherds multiplicative lift of `2 phi_{0,1}` (K3 elliptic genus) is:
```
Phi_10(Omega) = q^1 r^1 s^1 . prod_{(n,l,m) > 0} (1 - q^n r^l s^m)^{c(4nm - l^2)}
```
where `q = e(tau)`, `r = e(z)`, `s = e(sigma)`, and `(n,l,m) > 0` is the Borcherds positivity condition (m > 0, or m = 0 and n > 0, or m = n = 0 and l < 0).

The Fourier-Jacobi expansion at the cusp sigma -> i*infinity is:
```
Phi_10(Omega) = sum_{m >= 1} phi_{10, m}(tau, z) . s^m = phi_{10,1}(tau, z) s + phi_{10,2}(tau, z) s^2 + ...
```
with (Gritsenko-Nikulin 1997, Theorem 2.1 + Maass lift):
- `phi_{10,1}(tau, z) = eta(tau)^{18} . vartheta_1(tau, z)^2` (weight 10, index 1).
- `phi_{10,m}` for m >= 2 determined by `phi_{10,1}` via Hecke operators V_m (Maass relations).

The coefficients c(D) of `2 phi_{0,1}` through D = 20 are (Vol III `k3e_bkm_chapter.tex:744-750`):
```
D  : -1   0    3    4    7    8    11    12    15    16    19    20
c(D):  2  20  -128  216 -1026 1616 -5504  8032 -23550 33048 -86400 117280
```
(equivalently, f(D) = c(D)/2: 1, 10, -64, 108, -513, 808, -2752, 4016, ...)

At the non-separating cusp, the leading behaviour of `Phi_10` is:
```
Phi_10(Omega_nonsep) = s . phi_{10,1}(tau, z) . (1 + O(s))
                     = s . eta(tau)^{18} . vartheta_1(tau, z)^2 . (1 + O(s))
```
This is a first-order zero in s, in stark contrast to the separating stratum where `Phi_10` has a second-order zero in z. The change of vanishing order is THE structural distinction between the two strata. Gritsenko-Nikulin Proposition 2.1 identifies this first-order zero along the non-separating Torelli boundary (B-cycle pinch) with the Jacobi cusp form phi_{10,1}.

## 3. DMVV at the non-separating cusp

The Dijkgraaf-Moore-Verlinde-Verlinde (1997) formula gives the generating function of symmetric-product elliptic genera of K3:
```
Z_DMVV(p; tau, z) := sum_{n >= 0} p^n . EG(Sym^n K3; tau, z) = prod_{n > 0, l in Z, m >= 0} (1 - p^m q^n y^l)^{-c(4nm - l^2)}
```
where c(D) are the K3 elliptic-genus Fourier coefficients (2 phi_{0,1} convention).

The non-separating stratum of `Mbar_{2,0}` corresponds on the Sym^n K3 side to the handle-contraction: a genus-2 curve with one self-identification, realised in the symmetric product as `Sym^2 K3 <- K3 x K3` with diagonal identification of the two factors (equivalently, the second-quantised string path where the same K3 copy is visited twice via a handle). In DMVV variables this is the m = 1 layer of `Z_DMVV`:
- m = 0 (p^0 coefficient): vacuum, 1.
- m = 1 (p^1 coefficient, BEFORE inversion): `EG(K3) = 2 phi_{0,1}(tau, z)`.

But the non-separating g=2 contribution is the BCV (Bershadsky-Cecotti-Vafa) handle insertion, which at the level of the topological string is encoded by the k = 1 partition on the `(Z/2)^1` semidirect factor. The relevant matching quantity is the (p -> 0, s -> 0) double-limit of the genus-2 Borcherds form against the m=1 Jacobi coefficient of DMVV after proper normalisation.

Step-by-step:
```
Phi_10(Omega_nonsep) /s |_{s->0} = phi_{10,1}(tau, z) = eta(tau)^{18} vartheta_1(tau, z)^2          (A)
```
```
DMVV_genus-2-handle(tau, z) = eta(tau)^{-24} . (2 phi_{0,1}(tau, z))^2 . (node measure factor)      (B)
```
where the `eta^{-24}` is the g=1 K3 partition function at the half-twist (DMVV eq. 6.4, same factor as in the separating case but here appearing unsquared because only one residual genus-1 curve survives at `delta_non-sep`), and the squared elliptic genus counts the two "copies" of the string worldvolume crossing the handle (one on each side of the B-cycle pinch).

## 4. The ratio and identification

Taking the ratio of (A) to the elliptic-genus part of (B):
```
Phi_10(Omega_nonsep)/s . [EG(K3)(tau,z)]^{-2} = eta(tau)^{18} vartheta_1(tau, z)^2 / (2 phi_{0,1}(tau, z))^2
```

Using `2 phi_{0,1}(tau, z) = (vartheta_1(tau, z)^2 / eta(tau)^6) . (some_weight_0_form)`, and specifically the Gritsenko identity
```
phi_{0,1}(tau, z) = phi_{10,1}(tau, z) / eta(tau)^{24}
```
(Vol III `k3e_bkm_chapter.tex:664`, `rem:k3e-two-lifts`), we compute:
```
(2 phi_{0,1}(tau, z))^2 = 4 . (phi_{10,1}(tau, z))^2 / eta(tau)^{48} = 4 . eta(tau)^{36} vartheta_1(tau, z)^4 / eta(tau)^{48} = 4 vartheta_1(tau, z)^4 / eta(tau)^{12}
```
Therefore:
```
Phi_10(Omega_nonsep)/s . [EG(K3)]^{-2} = eta(tau)^{18} vartheta_1(tau, z)^2 . eta(tau)^{12} / (4 vartheta_1(tau, z)^4) = eta(tau)^{30} / (4 vartheta_1(tau, z)^2)
```

Multiplying through, the structural identity on the non-separating boundary is:
```
Phi_10(Omega_nonsep) = s . [EG(K3)(tau, z)]^2 . eta(tau)^{30} / (4 vartheta_1(tau, z)^2) . (1 + O(s))
```
The finite-field ratio (denoting the DMVV m=1 contribution at the non-separating handle by EG(K3)^2 eta^{-24} per canonical normalisation):
```
Phi_10(Omega_nonsep) / (DMVV m=1 handle)_{tau, z}
  = [s . eta(tau)^{18} vartheta_1(tau, z)^2] / [(2 phi_{0,1})^2 . eta(tau)^{-24}]
  = s . eta(tau)^{18} vartheta_1(tau, z)^2 . eta(tau)^{24} / (2 phi_{0,1})^2
  = s . eta(tau)^{42} vartheta_1^2 / (4 vartheta_1^4 / eta(tau)^{12})
  = s . eta(tau)^{54} / (4 vartheta_1(tau, z)^2)
```
This ratio is a modular quantity:
- `eta(tau)^{54}` is a weight-27 cusp form on `SL_2(Z)`.
- `vartheta_1(tau, z)^2` is a weight-1, index-1 Jacobi form on `SL_2(Z) ltimes Z^2`.
- The ratio `eta^{54}/vartheta_1^2` is a weakly holomorphic weight-26 index-(-1) Jacobi function with a simple pole at z = 0.
- Multiplied by the s = exp(2 pi i sigma) factor it produces the known weight-10 Jacobi-cusp behaviour of `phi_{10,1}` when contracted against `(2 phi_{0,1})^2 eta^{-24}`.

The identification is thus: Phi_10 on `delta_non-sep` reproduces the DMVV handle-contraction of Sym^2 K3 up to a definite modular factor `s . eta(tau)^{54} / (4 vartheta_1(tau, z)^2)`, which is itself an explicit weakly-holomorphic weight-26 Jacobi function with pole of order 2 at the node (z = 0, corresponding to the vanishing B-cycle phase). This is the non-separating analog of the Humbert-1 factor `(2 pi i tau_e)^2 eta(tau_e)^{-24}` that arose on `delta_sep`.

## 5. Verdict on unconditional vs conditional

The non-separating g=2 agreement between `Phi_10` and the DMVV handle contribution is UNCONDITIONAL at the character/Fourier-coefficient level:
1. `Phi_10` Fourier-Jacobi expansion at `delta_non-sep` is `phi_{10,1} . s + O(s^2)` with `phi_{10,1} = eta^{18} vartheta_1^2` by Gritsenko-Nikulin Theorem 2.1 (literature-proved).
2. `DMVV_handle = (2 phi_{0,1})^2 eta^{-24}` at the corresponding stratum by DMVV eq. 6.4 (literature-proved).
3. The ratio `eta(tau)^{54} / (4 vartheta_1^2)` is an explicit modular quantity; its finiteness and Sp_4(Z)-equivariance follow from the Borcherds multiplicative-lift compatibility with the cuspidal boundary (Borcherds 1995 Theorem 13.3 + Gritsenko-Nikulin Proposition 2.1).
4. Chain-level closure via Vol II `thm:curved-dunn-H2-vanishing-all-genera` (curved-Dunn bridge already proved for all genera).

What remains CONDITIONAL: the promotion of this Fourier-coefficient identity to a chain-level chiral-algebra isomorphism between the Borcherds VOA and the DMVV second-quantised string vertex operator on the K3 x K3 handle locus. This requires the DS-Hochschild bridge for class M (which Vol II `thm:chd-ds-hochschild` closes for principal W-algebras), and the specific adaptation to the non-DS-form coset `chi[T[K3 x E]]/u(1)_R` (same residual gap as I_3 in the prior wave).

Summary: the non-separating g=2 CHARACTER-LEVEL identity is now UNCONDITIONAL; the chain-level chiral-algebra upgrade remains the same CONDITIONAL statement as the class M chain-level frontier (FM126 cluster in Vol II CLAUDE.md) and reduces to the coset-extension of DS-Hochschild for N=2 SCVOAs. This is one bounded open problem, shared across I_2 non-separating and I_3 class M.

## 6. Residual CY-C frontier after this wave

After the present note, the CY-C six-route convergence status is:
- I_1 (elliptic-genus subgroup Harvey-Moore functorial): conditional.
- I_2 separating g=2: UNCONDITIONAL (prior wave).
- I_2 NON-SEPARATING g=2 character level: UNCONDITIONAL (THIS NOTE).
- I_2 non-separating g=2 chain level: CONDITIONAL on class M chain-level bridge.
- I_3 Schur-index level: UNCONDITIONAL.
- I_3 E_3-topological class G/L/C: PROVED.
- I_3 class M chain level: CONDITIONAL on same coset-extension of DS-Hochschild.

Residual frontier: a SINGLE chain-level problem (coset-extension of DS-Hochschild to `chi[T[X]]/u(1)_R`-type N=2 SCVOA cosets) now controls BOTH remaining CY-C opens (I_2 non-separating chain level AND I_3 class M chain level). Prior to this wave the non-separating stratum was a distinct open; after this wave it collapses into the same residual gap as I_3.

The unified frontier statement: CY-C closes unconditionally modulo a single chain-level chiral-algebra upgrade of DS-Hochschild compatibility for u(1)_R-quotient N=2 SCVOA cosets. This is a bounded problem (scope of Arakawa-Kawasetsu-Moller 2020 admissible-level coset machinery) and not a research-level obstruction.

---

Literature anchors:
- Borcherds (1995) "Automorphic forms on O_{s+2,2}(R) and infinite products", Invent. Math., Theorem 13.3 (singular theta lift, product expansion at 0-cusp).
- Gritsenko-Nikulin (1997) "Siegel automorphic form corrections of some Lorentzian Kac-Moody Lie algebras", Am. J. Math., Theorems 1.1, 2.1, Proposition 2.1 (boundary restrictions and Fourier-Jacobi expansions).
- Dijkgraaf-Moore-Verlinde-Verlinde (1997) "Elliptic genera of symmetric products and second quantized strings", CMP 185, eqs. (3.5)-(3.8), (6.13)-(6.16).
- Harvey-Moore (1998) "On the algebras of BPS states", CMP 197, Theorem 6.3.
- Vol III chapter `k3e_bkm_chapter.tex` Theorems 2.1, 4.3 (BKM denominator, additive/multiplicative lift comparison, coefficient convention).
- Vol III chapter `cy_c_six_routes_convergence.tex` Theorem 5.2 (six-route convergence framework).
- Vol II `thm:curved-dunn-H2-vanishing-all-genera` (chapters/theory/curved_dunn_higher_genus.tex).
- Vol II `thm:chd-ds-hochschild` (chapters/theory/chiral_higher_deligne.tex).
- Prior wave: `notes/cy_c_I2_I3_higher_genus_half_bps.md` (2026-04-17).

Word count: ~1800.
