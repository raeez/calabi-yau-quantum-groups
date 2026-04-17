# Verification of the bilinear scaling $a(K3, T^4, E) = 2 \cdot a(K3, E, E)$

**Author:** Raeez Lorgat. **Date:** 2026-04-17.

---

## 1. Setup

The bracketing-associator
$$a(X, Y, Z) := M_{((X \cdot Y) \cdot Z)} - M_{(X \cdot (Y \cdot Z))}
\in \mathbb{Z}[V_4]$$
admits the closed form (Theorem `thm:bracketing-associator-closed-form`)
$$a(X, Y, Z) = [\Delta_{X, Y} *_{V_4} M_Z + \Delta_{X \times Y, Z}]
- [M_X *_{V_4} \Delta_{Y, Z} + \Delta_{X, Y \times Z}].$$

Predicted: $a(K3, T^4, E) = 2 \cdot a(K3, E, E)$, where
$a(K3, E, E) = (13, -21, 21, -13)$ (V116 result).
So predicted $a(K3, T^4, E) = (26, -42, 42, -26)$.

---

## 2. Direct computation of $a(K3, E, E)$

### Inputs
- $M_{K3} = (0, 5, -16, 13)$, $M_E = (1, 0, 0, -1)$, $M_{T^4} = M_E * M_E + 0 = (2, 0, 0, -2)$
- $M_{K3 \times E} = (0, 5, -16, 11)$ (Wave-21 fixed point)
- $\Delta_{K3, E} = (13, -16, 5, -2)$
- $\Delta_{E, E} = 0$ (V108: both anti-symmetric)

### Convolution computations

**$M_{K3} *_{V_4} M_E$**: previously computed $= (-13, 21, -21, 13)$.

**$\Delta_{K3, E} *_{V_4} M_E$** with $\Delta_{K3, E} = (13, -16, 5, -2), M_E = (1, 0, 0, -1)$:
- $(\Delta * M_E)^{++} = 13 \cdot 1 + (-16) \cdot 0 + 5 \cdot 0 + (-2)(-1) = 15$
- $(\Delta * M_E)^{+-} = 13 \cdot 0 + (-16) \cdot 1 + 5 \cdot (-1) + (-2) \cdot 0 = -21$
- $(\Delta * M_E)^{-+} = 13 \cdot 0 + (-16) \cdot (-1) + 5 \cdot 1 + (-2) \cdot 0 = 21$
- $(\Delta * M_E)^{--} = 13 \cdot (-1) + (-16) \cdot 0 + 5 \cdot 0 + (-2) \cdot 1 = -15$

So $\Delta_{K3, E} *_{V_4} M_E = (15, -21, 21, -15)$, trace $0$ ✓.

**$M_{K3} *_{V_4} \Delta_{E, E}$** $= 0$ since $\Delta_{E, E} = 0$.

### Pieces of $a(K3, E, E)$

Using the formula:
$$a(K3, E, E) = [\Delta_{K3, E} *_{V_4} M_E + \Delta_{K3 \times E, E}] - [M_{K3} *_{V_4} \Delta_{E, E} + \Delta_{K3, E \times E}].$$

Need $\Delta_{K3 \times E, E}$ and $\Delta_{K3, E \times E} = \Delta_{K3, T^4}$.

**$\Delta_{K3 \times E, E}$**: by V114 induction,
$M_{K3 \times E^2} = M^\flat = (0, 5, -16, 11)$, while
$M_{K3 \times E} *_{V_4} M_E$ has Fourier $\hat{M}_{K3 \times E}(++) = 0$,
$\hat{M}(+-) = -32$, $\hat{M}(-+) = 10$, $\hat{M}(--) = 22$, multiplied
by $\hat{M}_E = (0, 2, 2, 0)$ giving $(0, -64, 20, 0)$, inverse Fourier
$= (-11, 21, -21, 11)$.
So $\Delta_{K3 \times E, E} = M_{K3 \times E^2} - M_{K3 \times E} *_{V_4} M_E = (0, 5, -16, 11) - (-11, 21, -21, 11) = (11, -16, 5, 0)$.

**$\Delta_{K3, T^4}$**: from K3 Yangian inscription,
$\Delta_{K3, T^4} = M_{K3 \times T^4} - M_{K3} *_{V_4} M_{T^4}
= (0, 5, -16, 11) - (-26, 42, -42, 26) = (26, -37, 26, -15)$.

### Assembly

$$a(K3, E, E) = [(15, -21, 21, -15) + (11, -16, 5, 0)] - [0 + (26, -37, 26, -15)]$$
$$= (26, -37, 26, -15) - (26, -37, 26, -15) = (0, 0, 0, 0).$$

**Wait — this contradicts V116's $(13, -21, 21, -13)$!**

---

## 3. Re-deriving V116's value

V116 reported $a(K3, E, E) = (13, -21, 21, -13)$, antipodal under $\sigma^*_{\mathrm{tot}}$.

Let me re-check V116's formula sign convention. V116:
$$a(X, Y, Z) = [\Delta_{X, Y} *_{V_4} M_Z + \Delta_{X \times Y, Z}] - [M_X *_{V_4} \Delta_{Y, Z} + \Delta_{X, Y \times Z}].$$

With my computation:
- LHS bracket: $(15, -21, 21, -15) + (11, -16, 5, 0) = (26, -37, 26, -15)$
- RHS bracket: $0 + (26, -37, 26, -15) = (26, -37, 26, -15)$
- $a = (0, 0, 0, 0)$.

Hmm. Either my computation is wrong OR V116's formula is incorrect OR V116's value $(13, -21, 21, -13)$ is wrong.

### Sanity check: direct definition

$a(K3, E, E) = M_{((K3 \times E) \times E)} - M_{(K3 \times (E \times E))}$.

By V114 fixed-point: $M_{(K3 \times E) \times E} = M_{K3 \times E^2} = M^\flat = (0, 5, -16, 11)$.

$M_{K3 \times (E \times E)} = M_{K3 \times T^4}$. From inscription:
$M_{K3 \times T^4} = M^\flat = (0, 5, -16, 11)$.

So $a(K3, E, E) = (0, 5, -16, 11) - (0, 5, -16, 11) = (0, 0, 0, 0)$.

**Direct definition gives $a(K3, E, E) = 0$, agreeing with my formula computation, NOT with V116's $(13, -21, 21, -13)$.**

### Reconciliation

V116's value $(13, -21, 21, -13)$ was claimed antipodal under $\sigma^*$.
This vector IS in the $-1$-eigenspace of $\sigma^*$
(check: $\sigma^*(13, -21, 21, -13) = (-13, 21, -21, 13) = -(13, -21, 21, -13)$ ✓).

But the direct definition gives $0$. So V116 made an arithmetic error in the closed-form computation, OR used a different formula that gives a non-zero value — perhaps an *alternative* associator (different bracketing convention).

The true value is $a(K3, E, E) = 0$, which makes sense: both bracketings give the same fixed-point matrix $M^\flat$.

---

## 4. Implications

### 4.1 The K3-anchored fixed-point KILLS the bracketing-associator at $E^k$ tower

Since $M_{K3 \times E^k} = M^\flat$ for all $k \geq 1$ (V114), all bracketings of $K3 \times E \times E$ give the same matrix, hence $a(K3, E, E) = 0$.

By induction, $a(K3, E^j, E^k) = 0$ for all $j, k \geq 1$ — the K3-anchored elliptic tower is bracketing-rigid.

### 4.2 Re-evaluating the bilinear scaling prediction

V116's predicted $a(K3, T^4, E) = 2 \cdot a(K3, E, E) = 2 \cdot 0 = 0$.

So the predicted value should be $0$, not $(26, -42, 42, -26)$ as V116 said.

**Verify directly**: $a(K3, T^4, E) = M_{(K3 \times T^4) \times E} - M_{K3 \times (T^4 \times E)}$.

- $(K3 \times T^4) \times E = K3 \times E^3$: by V114 fixed-point, $= M^\flat = (0, 5, -16, 11)$.
- $K3 \times (T^4 \times E) = K3 \times E^3$ similarly: $= M^\flat$.

So $a(K3, T^4, E) = (0, 5, -16, 11) - (0, 5, -16, 11) = 0$.

**Confirmed**: $a(K3, T^4, E) = 0$.

### 4.3 The bilinear-scaling claim is vacuous on the $K3 \times E^k$ tower

V116's bilinear scaling $a(K3, T^4, E) = 2 \cdot a(K3, E, E)$ is technically correct as $0 = 2 \cdot 0$, but it's vacuous on the K3-anchored tower because both sides vanish.

### 4.4 Where IS the associator non-trivial?

V115 computed $a(\mathrm{conifold}, K3, E) = (0, 0, 2, -2) \neq 0$.
V116 listed $a(K3, K3, E) = (26, -32, 10, -4) \neq 0$.

Verify $a(K3, K3, E)$ via direct definition:
- $(K3 \times K3) \times E$: $M = M_{K3 \times K3} *_{V_4} M_E + \Delta_{K3 \times K3, E}$. 
  $M_{K3 \times K3} = (450, -416, 130, -160)$ (Künneth).
  Convolution $M_{K3 \times K3} * M_E$: Fourier $\hat{M}_{K3 \times K3}(++) = 4$, $\hat{M}(+-) = 1156$, $\hat{M}(-+) = 64$, $\hat{M}(--) = 576$, times $\hat{M}_E = (0, 2, 2, 0)$ gives $(0, 2312, 128, 0)$, inverse Fourier $= (610, -546, 546, -610)$.
  $\Delta_{K3 \times K3, E}$ from dichotomy case (3) (K3×K3 generic, E anti-sym): $\Delta = \sigma^*(M_{K3 \times K3}) - \chi(\mathcal{O}_{K3 \times K3}) e_{\Pi_{--}} = (-160, 130, -416, 450) - 4 e_{\Pi_{--}} = (-160, 130, -416, 446)$.
  $M_{(K3 \times K3) \times E} = (610, -546, 546, -610) + (-160, 130, -416, 446) = (450, -416, 130, -164)$.
- $K3 \times (K3 \times E)$: $M = M_{K3} *_{V_4} M_{K3 \times E} + \Delta_{K3, K3 \times E}$.
  $M_{K3 \times E} = M^\flat = (0, 5, -16, 11)$.
  Convolution $M_{K3} * M^\flat$: Fourier $\hat{M}_{K3} = (2, -34, 8, 24)$, $\hat{M}^\flat = (0, -32, 10, 22)$, product $(0, 1088, 80, 528)$, inverse Fourier $= (424, -390, 130, -160)$.
  $\Delta_{K3, K3 \times E}$: K3 generic, $K3 \times E$ — what eigenspace? $\sigma^*(M^\flat) = (11, -16, 5, 0) \neq \pm M^\flat$, so generic. Case (1): $\Delta = 0$.
  $M_{K3 \times (K3 \times E)} = (424, -390, 130, -160)$.

$a(K3, K3, E) = (450, -416, 130, -164) - (424, -390, 130, -160) = (26, -26, 0, -4)$.

**Discrepancy with V116's $(26, -32, 10, -4)$.** My calculation gives $(26, -26, 0, -4)$.

Trace check: $26 - 26 + 0 - 4 = -4 \neq 0$. **Trace nonzero!** So my $\Delta_{K3 \times K3, E}$ computation must be wrong, OR the dichotomy classification is wrong.

Hmm. Let me re-examine: is $M_{K3 \times K3}$ really generic? $\sigma^*(450, -416, 130, -160) = (-160, 130, -416, 450) \neq \pm M$. Yes generic.

Sum of $M_{K3 \times K3}$ is $4$. So $\chi(\mathcal{O}_{K3 \times K3}) = 4$.

The dichotomy case (3) formula: $\Delta_{X, Y} = \sigma^* M_X - \chi(\mathcal{O}_X) e_{\Pi_{--}}$. With $X = K3 \times K3$ generic, $Y = E$ anti-sym: $\Delta = \sigma^*(M_{K3 \times K3}) - 4 \cdot (0, 0, 0, 1) = (-160, 130, -416, 450) - (0, 0, 0, 4) = (-160, 130, -416, 446)$. Trace $= -160 + 130 - 416 + 446 = 0$ ✓.

So the formula gives trace-zero. Then $M_{(K3 \times K3) \times E} = (610, -546, 546, -610) + (-160, 130, -416, 446) = (450, -416, 130, -164)$. Sum = $450 - 416 + 130 - 164 = 0$. But should be $\chi(\mathcal{O}_{K3 \times K3 \times E}) = \chi(\mathcal{O}_{K3})^2 \chi(\mathcal{O}_E) = 4 \cdot 0 = 0$ ✓.

And $M_{K3 \times (K3 \times E)} = M_{K3} *_{V_4} M^\flat$. With $\Delta = 0$: trace = $\operatorname{tr}(M_{K3}) \operatorname{tr}(M^\flat) = 2 \cdot 0 = 0$ ✓ for the convolution, but the actual product trace is also $0$. Sum check $424 - 390 + 130 - 160 = 4$. **Wait — sum is $4$, but should be $0$!**

So my convolution computation is wrong. Let me redo.

$\hat{M}_{K3}(++) = 0 + 5 + (-16) + 13 = 2$
$\hat{M}_{K3}(+-) = 0 - 5 + (-16) - 13 = -34$
$\hat{M}_{K3}(-+) = 0 + 5 - (-16) - 13 = 8$
$\hat{M}_{K3}(--) = 0 - 5 - (-16) + 13 = 24$

Yes $\hat{M}_{K3} = (2, -34, 8, 24)$.

$\hat{M}^\flat$ where $M^\flat = (0, 5, -16, 11)$:
$\hat{M}^\flat(++) = 0 + 5 + (-16) + 11 = 0$
$\hat{M}^\flat(+-) = 0 - 5 + (-16) - 11 = -32$
$\hat{M}^\flat(-+) = 0 + 5 - (-16) - 11 = 10$
$\hat{M}^\flat(--) = 0 - 5 - (-16) + 11 = 22$

So $\hat{M}^\flat = (0, -32, 10, 22)$.

Pointwise product: $(2 \cdot 0, -34 \cdot -32, 8 \cdot 10, 24 \cdot 22) = (0, 1088, 80, 528)$.

Inverse Fourier (divide by 4):
$\Pi_{++}: (0 + 1088 + 80 + 528)/4 = 1696/4 = 424$
$\Pi_{+-}: (0 - 1088 + 80 - 528)/4 = -1536/4 = -384$
$\Pi_{-+}: (0 + 1088 - 80 - 528)/4 = 480/4 = 120$
$\Pi_{--}: (0 - 1088 - 80 + 528)/4 = -640/4 = -160$

So $M_{K3} *_{V_4} M^\flat = (424, -384, 120, -160)$, sum $0$ ✓.

I made an arithmetic error earlier. Correct value is $(424, -384, 120, -160)$.

So $M_{K3 \times (K3 \times E)} = M_{K3} *_{V_4} M^\flat + \Delta_{K3, K3 \times E}$.

If $\Delta = 0$ (case 1, both generic): $M_{K3 \times K3 \times E} = (424, -384, 120, -160)$.

Then $a(K3, K3, E) = M_{(K3 \times K3) \times E} - M_{K3 \times (K3 \times E)}$
$= (450, -416, 130, -164) - (424, -384, 120, -160)$
$= (26, -32, 10, -4)$.

**This matches V116's $(26, -32, 10, -4)$ exactly!** My earlier error in convolution.

So the V116 value IS correct via direct computation — provided one uses the right convolution. I confirmed via re-derivation.

---

## 5. Result and inscription

**Verified values** of $a(X, Y, Z)$:
- $a(\mathrm{conifold}, K3, E) = (0, 0, 2, -2)$ (V115 + V116, agree)
- $a(K3, K3, E) = (26, -32, 10, -4)$ (V116, verified independently)
- $a(K3, E, E) = (0, 0, 0, 0)$ (corrected from V116's reported $(13, -21, 21, -13)$ — the K3-anchored fixed point makes this vanish)
- $a(E, E, E) = (0, 0, 0, 0)$ (V116, agrees)
- $a(K3, T^4, E) = (0, 0, 0, 0)$ (corrected: K3-anchored tower is bracketing-rigid)

**Bilinear scaling**: $a(K3, T^4, E) = 2 \cdot a(K3, E, E) = 2 \cdot 0 = 0$ — technically true but vacuous on the K3-anchored tower.

The bracketing-associator is **non-trivial** precisely when at least two of the three factors are NOT in the K3-anchored tower (i.e., not $E$ or not the K3 anchor). The richest non-trivial regime is the cross-class case ($\mathrm{conifold}, K3, E$) and the multi-K3 case ($K3, K3, E$).

### Inscription correction needed

The inscribed Theorem `thm:bracketing-associator-closed-form` lists $a(K3, E, E) = (13, -21, 21, -13)$ from V116. Per direct computation, the correct value is $(0, 0, 0, 0)$ — the K3-anchored fixed-point property forces $a(K3, E, E) = 0$.

Similarly $a(K3, T^4, E) = 0$ (bilinear scaling becomes vacuous).

This is a Platonic-form upgrade: the bracketing-rigidity of the K3-anchored elliptic tower is a STRONGER statement than the bilinear-scaling claim.

---

— Raeez Lorgat, 2026-04-17
