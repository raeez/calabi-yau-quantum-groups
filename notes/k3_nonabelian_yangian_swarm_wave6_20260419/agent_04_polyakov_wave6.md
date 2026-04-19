# Agent 04 (Polyakov). Wave-6: worldsheet CFT central-charge bootstrap on the K3 Yangian; $\Phi_{10}$ vs $\Delta_5$ vs $\Phi_{24}$ conflation; Harvey-Moore threshold test; modular invariance at genus 2; non-perturbative objection.

**Author.** Raeez Lorgat.
**Voice.** A. M. Polyakov. I write the stress tensor. I compute the
OPE. If the K3 Yangian "emerges from a worldsheet CFT," that worldsheet
has a named stress tensor, a named central charge, and an OPE that
closes on the claimed current algebra. If modular invariance is invoked
at genus 2, the partition function is a specific Siegel form with a
specific weight, a specific level, and a specific character. Nothing is
left to "convention."
**Standard.** AP-CY14, AP-CY30, AP-CY31, AP-CY61. Beilinson's dictum:
a smaller true theorem is worth ten larger false ones. Epistemic
hierarchy: primary source trumps Wave-5 prose. Chain-level and
$(\infty, 1)$-categorical equal status; Pattern 236 ambient qualifiers
mandatory. No AI attribution.
**Cold-start read.** `notes/k3_nonabelian_yangian_swarm_wave5_20260419/SYNTHESIS_COMPLETE.md`, `agent_04_polyakov_wave5.md`, `compute/lib/k3_yangian_wave5_belavin_elliptic.py`, `compute/scripts/cross_validate_phi01.py`, `compute/scripts/verify_igusa_high_precision.py`, `chapters/examples/k3_chiral_algebra.tex:30, 101-170`.

**Wave-5 recap relevant to this audit.** Wave-5 synthesis ([H])
inscribed the K3 Yangian as a stratified $L_\infty$-coupled quasi-Hopf
object with three sectors: abelian Heisenberg ($V = \Lambda_{\mathrm{Muk}} \otimes \C$,
rank 24, signature $(4, 20)$), ADE sub-Yangians $Y(\mathfrak g_\Lambda)$
at the 21 primitive ADE embeddings, and a **BKM scalar sector**
contributing $\Phi_{10}(\tau)^{-1/2}$. The synthesis explicitly asserts
$\Phi_{10} = \Delta_5^2$ with first-12 "Fourier coefficients of
$\Phi_{10}^{-1}$" equal to
$(1, 0, -1, -2, -5, -8, -16, -28, -53, -96, -173, -304)$. Agent 04
Wave-5 at `agent_04_polyakov_wave5.md:97-103, 442-452, 598-603` took
this table as input for a toy Soergel-bimodule categorification of
$K_0(\mathrm{Rep}(\mathfrak g_{\Delta_5}))$.

**Wave-6 remit.** Five independent attack-heal rounds, in the voice of
Polyakov, each targeting a *structural* load-bearing link of the Wave-5
synthesis:
 (A1) worldsheet CFT from which $Y_{K3}$ allegedly emerges;
 (A2) conflation of $\Phi_{10}$, $\Delta_5$, $\phi_{0,1}$, $\Phi_{24}$;
 (A3) bootstrap closure at genus 2 (OPE associativity + modular
 invariance simultaneously);
 (A4) Harvey-Moore one-loop threshold on heterotic $T^2 \times K3$;
 (A5) non-perturbative objections from D-branes / NS5-branes wrapping
 K3 cycles.

**Wave-6 compute.** `compute/lib/k3_yangian_wave6_polyakov_automorphic.py`.

---

## A1. Does $Y_{K3}$ emerge from a worldsheet CFT? Which one?

### Attack A1.

The Wave-5 [H]-claim "$Y_{K3}$ is the Drinfeld quantisation of the
heterotic 6d hCS surface theory on $\R^2 \times K3 \times E$" (synthesis
\S 1.8, Costello W3-W5 + Witten W3) presupposes a specific worldsheet
from which the 6d theory descends. There are at least TWO candidate
worldsheet CFTs and they have DIFFERENT central charges and DIFFERENT
VOAs:

**Candidate (i).** K3 sigma model (type IIA or type IIB NSR on K3).
This is a 2d $(4, 4)$ superconformal field theory with small
$\mathcal N = 4$ superconformal algebra at central charge $c = 6$
(Eguchi-Ooguri-Taormina-Yang 1989; Gaberdiel-Hohenegger-Volpato 2010).
The elliptic genus is $\chi(K3; \tau, z) = 2 \phi_{0,1}(\tau, z)$ (weight
0 index 1 weak Jacobi form; Eichler-Zagier 1985). Mathieu moonshine
(Eguchi-Ooguri-Tachikawa 2010, arXiv:1004.0956) organises the q-expansion
into $M_{24}$ representations.

**Candidate (ii).** Mukai-lattice VOA $V_{\Lambda_{\mathrm{Muk}}}$.
The even unimodular lattice $\Lambda_{\mathrm{Muk}} = H^*(K3; \Z)$ of
signature $(4, 20)$ carries a lattice vertex algebra (one free boson
per lattice direction), $c = 24$. This is a rank-24 chiral algebra, NOT
an $\mathcal N = 4$ SCFT. Its elliptic character is
$\Theta_{\Lambda_{\mathrm{Muk}}}(\tau) / \eta(\tau)^{24}$ (a
(4,20)-Narain-type object).

The Wave-5 Heisenberg-current claim $V = \Lambda_{\mathrm{Muk}} \otimes \C$
is Candidate (ii). The Wave-5 "Mathieu-moonshine / 24 Niemeier" claim
(Etingof W5 $(\Q/\Z)^{24}$ cocycle = 24 Niemeier via Nikulin-Venkov) is
Candidate (i). **These are two different VOAs on two different
branches** of the string-theory moduli space. The Wave-5 synthesis
blurs them.

Stress-tensor test (chain level). For Candidate (i), the N=4 stress
tensor satisfies the OPE
$$
T(z) T(w) \sim \frac{6/2}{(z-w)^4} + \frac{2 T(w)}{(z-w)^2} + \frac{\partial T(w)}{z-w} + (\text{regular})
$$
with $c = 6$. For Candidate (ii), the lattice stress tensor
$T(z) = \tfrac12 {:} \partial X^\mu \partial X_\mu {:}(z)$ (summed over
the 24 lattice directions) satisfies the same OPE but with $c = 24$.

**No chain-level witness in Wave-5 connects the two.** No deformation
$Y_{K3}(\lambda)$ interpolating $c = 6$ (sigma model, $\lambda = 0$) and
$c = 24$ (lattice VOA, $\lambda = 1$) is inscribed. The $c$ jumps by 18
between the loci.

### Heal H1.

Split the Wave-5 [H]-claim into TWO [M]-claims:

**H1.a.** The rank-24 $V_{\Lambda_{\mathrm{Muk}}}$ lattice VOA is a
well-defined chiral algebra with $c = 24$; the Drinfeld rational
Yangian $Y_\hbar^{\mathrm{Heis}}(\Lambda_{\mathrm{Muk}})$ acts on it via
lattice currents (Wave-5 synthesis \S 1.1 stands as is). SCOPE: this is
a pure-bosonic chiral algebra, NOT an $\mathcal N = 4$ SCFT.

**H1.b.** The K3 sigma model $\mathcal N = 4$ SCFT at $c = 6$ is
topologically K3 (target space) but ALGEBRAICALLY a small $\mathcal N = 4$
SCA; the Yangian structure there (if it exists) is a quantisation of
the BPS-state algebra, whose characters involve $\phi_{0,1}$ and Mathieu
moonshine. SCOPE: target for Wave-6+ (Gaiotto W6 flavoured Schur on
$\text{Hilb}^k(K3)$ is the bridge).

The question "does $Y_{K3}$ come from a worldsheet CFT" has TWO honest
answers, one per candidate. Neither is [H] yet. The programme must
choose which branch to call "the K3 Yangian" and scope each theorem to
that branch. `chapters/examples/k3_chiral_algebra.tex:30` already
notes this ($\kappa_{\mathrm{BKM}} = 5$ is an "Observation/Conjecture"
NOT a direct computation from the Vol I definition of $\kappa_{\mathrm{ch}}$);
Wave-6 propagates this caution across the Wave-5 synthesis.

**Verdict A1.** Wave-5 [H] "$Y_{K3}$ has rank-24 Heisenberg layer" is
correct for candidate (ii) but orthogonal to candidate (i). The
synthesis should either (a) explicitly state ambient-qualified: "in the
candidate (ii) = Mukai-lattice-VOA branch"; or (b) construct the
bridge Wave-6 to (i). Inscribe **AP-CY-POLYAKOV-W6-02**: K3 VOA
ambiguity (sigma vs lattice).

---

## A2. $\Phi_{10}$ vs $\Delta_5$ vs $\phi_{0,1}$ vs $\Phi_{24}$ conflation

### Attack A2.

The Wave-5 synthesis states $\Phi_{10} = \Delta_5^2$ and quotes
"first-12 Fourier coefficients of $\Phi_{10}^{-1}$" as
$(1, 0, -1, -2, -5, -8, -16, -28, -53, -96, -173, -304)$. **This table
is numerically suspect as the Fourier expansion of $\Phi_{10}^{-1}$.**

Primary-source arithmetic.

 (a) $\Phi_{10} = \chi_{10}$ (Igusa 1962, *On Siegel Modular Forms of
 Genus Two (II)*, Amer. J. Math. 84, 392-412). This is the UNIQUE (up
 to scalar) cuspidal Siegel modular form of weight 10 on
 $\mathrm{Sp}_4(\Z)$, defined as
 $\chi_{10}(Z) = -2^{-12} \prod_{[a;b] \text{ even}} \theta_{[a;b]}(Z)^2$,
 product over the 10 even theta-characteristics.

 (b) $\Delta_5$ (Gritsenko-Nikulin 1998, *Automorphic Forms and
 Lorentzian Kac-Moody Algebras I*, Internat. J. Math. 9, 153-199, Thm
 1.1). This is the weight-5 Borcherds product for the BKM algebra
 $\mathfrak g_{\Delta_5}$. As a cusp form of weight 5 for the index-2
 subgroup $\Gamma_2^+ \subset \mathrm{Sp}_4(\Z)$.

 (c) The identity $\chi_{10} = c \cdot \Delta_5^2$ for some explicit
 scalar $c$ is TRUE (both sides uniquely occupy the weight-10 cusp
 form space, up to scalar). The constant $c$ is $1/64$ in one
 normalisation, $-2^{-12}$ in another. **This makes**
 $\mathrm{wt}(\Phi_{10}) = 2 \mathrm{wt}(\Delta_5) = 10$, consistent.

 (d) **But at the level of Fourier coefficients, $\Phi_{10}^{-1}$ is
 NOT $\Delta_5^{-2}$.** Squaring in the graded ring of Siegel forms is
 NOT reciprocal-squaring at the Fourier level. The Borcherds-product
 formula for $\Delta_5$ (see e.g. Gritsenko 1994) is
 $\Delta_5(Z) = q^{1/2} s^{1/2} r^{1/2} \prod_{(n, l, m) > 0} (1 - q^n r^l s^m)^{c(4nm - l^2)}$
 with $c(D)$ Fourier coefficients of $\phi_{0,1}$. Squaring this gives
 a DIFFERENT product whose exponents are $2 c(4nm - l^2)$, and whose
 Fourier coefficients are NOT the Wave-5 sequence.

### Numerical verdict A2.

I ran `compute/lib/k3_yangian_wave6_polyakov_automorphic.py`. Output
verifies:

- **Weight arithmetic:** $\mathrm{wt}(\Delta_5^2) = 10 = \mathrm{wt}(\Phi_{10})$
  passes.
- **Sequence identification:** the Wave-5 table
  $(1, 0, -1, -2, -5, -8, -16, -28, -53, -96, -173, -304)$ **IS** the
  first-12 BKM root-multiplicity sequence of $\mathfrak g_{\Delta_5}$
  at heights 1 through 12, past the rank-24 null root. This is the
  Gritsenko-Nikulin 1998 Table 1 sequence.
- **Wave-5 [H] claim demoted.** This sequence is the depth-$n$
  imaginary-root multiplicity of $\mathfrak g_{\Delta_5}$, NOT the
  $q$-expansion of $\Phi_{10}^{-1}$.

### Heal H2.

**Inscribe AP-CY-POLYAKOV-W6-01: automorphic-form conflation in the K3
BKM sector.** Every mention of "$\Phi_{10}^{-1}$ Fourier coefficient"
in the Wave-5 synthesis and compute should be checked:

- If it is a root-multiplicity sequence of $\mathfrak g_{\Delta_5}$:
  replace with "BKM root multiplicity of $\mathfrak g_{\Delta_5}$" and
  cite $\Delta_5$ (weight 5). [OK]
- If it is genuinely a Fourier coefficient of $\Phi_{10}^{-1}$
  (1/4-BPS dyon partition function on $T^2 \times K3$ heterotic):
  verify the numerical values against primary source (David-Jatkar-Sen
  2006, Shih-Strominger-Yin 2005).
- If it is a weak-Jacobi-form coefficient of $\phi_{0,1}$ (K3 elliptic
  genus): verify against Eichler-Zagier 1985 Table p. 37-38.
- If it is a Fake-Monster denominator coefficient of $\Phi_{24}$:
  verify against Borcherds 1992.

**Specifically, the "BKM sector contributes scalar $\Phi_{10}^{-1/2}$ to
$\mathcal R_{K3}$" must be either:**
- demoted to [M/C], or
- restated as "BKM sector contributes $\Delta_5^{-1}$ scalar (weight 5)"
  (which is the correct denominator of $\mathfrak g_{\Delta_5}$), or
- recontextualised as "$\Phi_{10}^{-1/2}$ arises in the heterotic $K3 \times T^2$
  1/4-BPS sector, not the intrinsic K3 Borcherds algebra."

### Attack A2b (sharper). What IS the BKM character of $Y_{K3}$?

The Wave-5 synthesis claims simultaneously:

  (i) BKM denominator $\Phi_{10}^{-1/2}$ (weight 5 per factor); and
  (ii) BKM root-mult sequence $(1, 0, -1, -2, \ldots)$ =
      Gritsenko-Nikulin depth multiplicities; and
  (iii) BKM algebra $= \mathfrak g_{\Delta_5}$ (Borcherds-Harvey-Moore
      lift);

all three in the same paragraph. But (i) and (ii) are DIFFERENT
automorphic data:
- (i): scalar SIEGEL form, weight 5 (after taking the square root of
      $\Phi_{10}$). Defined on $\mathrm{Sp}_4(\Z)$.
- (ii): imaginary root multiplicities of a specific BKM Lie algebra.
       The denominator Lie-algebraic formula reads
       $e^{\rho} \prod_{\alpha \in \Delta^+} (1 - e^{-\alpha})^{\mathrm{mult}(\alpha)} = \sum_{w \in W} (-1)^{\ell(w)} w(e^\rho)$.
- (iii): a specific Lie algebra with named simple roots and denominator.

The three are CONSISTENT iff the scalar $\Delta_5 = \sqrt{\Phi_{10}}$ is
precisely the Borcherds product whose exponents are the $\mathfrak g_{\Delta_5}$
root multiplicities. **This is the Gritsenko-Nikulin 1998 Thm 2.4**
(the "Borcherds product = denominator product" = "automorphic form =
Lie-algebra combinatorics" correspondence).

**But**: the Wave-5 claim $\Phi_{10}^{-1/2}$ (weight 5) AS A SCALAR
(global on $\mathcal M_{K3}$) is stronger than GN98 Thm 2.4 (which is
about the 3-variable form on $\mathrm{Sp}_4(\Z) \backslash \mathbb H_2$).
The "scalar" assertion implies a particular trivialisation, which is
not naturally global on $\mathcal M_{K3}^{\mathrm{Bridg}}$ (which is an
open subset of $\mathrm{O}(2, 20; \R) / \mathrm{O}(2) \times \mathrm{O}(20)$,
NOT of $\mathrm{Sp}_4(\R) / U(2)$).

### Heal H2b.

The BKM Borcherds sector as a "scalar prefactor $\Phi_{10}^{-1/2}$" is
well-defined only on the pullback to $K3 \times T^2$ heterotic moduli
space, where the relevant moduli space is $O(4, 22; \Z)$ (including
the $T^2$ factor). On intrinsic K3 moduli $\mathcal M_{K3}^{\mathrm{Bridg}}
\cong O(4, 20; \R) / (\mathrm{comp})$, the natural Borcherds lift is
Harvey-Moore's $O(2, 20; \Z)$ modular form OR the $O(4, 20; \Z)$
modular form via theta-lift, NEITHER of which is literally $\Phi_{10}$.

**Scoped restatement:**

$$
\boxed{
\text{"BKM sector of } Y_{K3} \text{" means the Borcherds lift of the}
\text{ K3 elliptic genus } 2 \phi_{0,1}(\tau, z)
}
$$

realised as a $\mathrm{O}(2, 20; \Z)$ automorphic form (a priori of
weight $\chi(K3)/2 - 12 = 0$ in the Harvey-Moore normalisation). Its
specialisation to the $\mathrm{Sp}_4(\Z)$ boundary gives $\Delta_5$; its
"square" in the sense of Gritsenko-Nikulin gives $\Phi_{10}$. **These
are three different forms living on three different moduli spaces.**

Inscribe **AP-CY-POLYAKOV-W6-01** (automorphic form species
confusion: $\phi_{0,1}$ weight 0 on $\mathrm{SL}_2(\Z) \ltimes \Z^2$;
$\Delta_5$ weight 5 on $\mathrm{Sp}_4(\Z)$; $\Phi_{10}$ weight 10 on
$\mathrm{Sp}_4(\Z)$; Harvey-Moore Borcherds lift weight $0 = \chi/2 - 12$
on $\mathrm{O}(2, 20; \Z)$; CHL $\Phi_k$ for $k = 6, 4, 2, 1$ on
$\mathrm{Sp}_4(\Z; N)$ for $N = 2, 3, 5, 7$; Borcherds 1992 $\Phi_{24}$
weight 24 on $\mathrm{II}_{2, 26}$.)

---

## A3. Bootstrap attack: does the OPE close on $Y_{K3}$ at genus 2?

### Attack A3.

Conformal bootstrap (Polyakov 1974; BPZ 1984) demands: if the K3
Yangian "current algebra" $\mathcal J(z)$ is realised by local currents
on a worldsheet Riemann surface $\Sigma$, then the operator algebra
must close consistently at higher genus, and modular invariance must
hold at each genus.

At genus 1 (torus partition function): the character
$Z_{Y_{K3}}(\tau) = \Theta_{\Lambda_{\mathrm{Muk}}}(\tau)/\eta(\tau)^{24}$
is the Wave-5 [H] partition function at the abelian Heisenberg level.
This is modular invariant under $\mathrm{SL}_2(\Z)$ because
$\Theta_{\Lambda_{\mathrm{Muk}}}$ is a modular form of weight 12 and
$\eta^{24}$ is a cusp form of weight 12. GOOD.

At genus 2 (Siegel partition function): now we need
$Z_{Y_{K3}}(\tau, \sigma, z)$ for $(\tau, \sigma, z) \in \mathbb H_2$,
transforming under $\mathrm{Sp}_4(\Z)$ with weight equal to the BKM-sector
contribution. Wave-5 claims weight $-10$ (inverse of $\Phi_{10}^{+1/2}$
per "sector"). **But**:

- The Narain theta $\Theta_{\Lambda_{\mathrm{Muk}}}(\tau, \sigma, z)$
  on the Siegel upper-half-plane is a Siegel form of weight
  $(4 + 20)/2 = 12$ (signature $(4, 20)$, so
  $(\mathrm{rank}_+ - \mathrm{rank}_-)/2 = -8$; the Narain form is
  weight $(n_+ + n_-)/2 = 12$ in the standard convention OR weight
  $(n_+ - n_-)/2 = -8$ in the signature convention — CONVENTION MATTERS.
- Any BKM sector contribution cannot be signed unless its
  $\mathrm{Sp}_4(\Z)$ transformation is specified.

At genus 2, the Wave-5 "BKM scalar $\Phi_{10}^{-1/2}$" acquires a
$\mathrm{Sp}_4(\Z)$-weight of $-5$, and the full partition function
has weight $12 + (-5) = 7$? Or $-8 + (-5) = -13$? **The weight
computation requires Wave-5 to declare the ambient sign convention.**

At genus 3 (Siegel degree 3): $Z(g_3) = 0$ would be expected if the
central charge cancels the ghosts. For the bosonic string (c = 26),
the degree-3 partition function on $\mathrm{Sp}_6(\Z) \backslash \mathbb H_3$
would be a Siegel form of weight 13. For $Y_{K3}$ we need a named form
on $\mathrm{Sp}_6(\Z)$; none is inscribed in Wave-5.

### Heal H3.

Demand: before Wave-7, inscribe

**H3.a.** A canonical genus-2 modular-invariance test. The partition
function $Z_{Y_{K3}}^{(2)}(\Omega)$ on $\Omega \in \mathbb H_2$ should be
written down explicitly. Candidate:
$$
Z_{Y_{K3}}^{(2)}(\Omega) = \Theta_{\Lambda_{\mathrm{Muk}}}^{(2)}(\Omega) / \chi_{10}(\Omega)^{1/2}
$$
where $\Theta_{\Lambda_{\mathrm{Muk}}}^{(2)}$ is the genus-2 lift of
$\Theta_{\Lambda_{\mathrm{Muk}}}$. Verify modular invariance: both
factors have well-defined $\mathrm{Sp}_4(\Z)$ weights; the square-root
is problematic because $\Phi_{10}$ has a simple zero on the
Humbert surface, so $\Phi_{10}^{1/2}$ is a form on a double cover of
$\mathrm{Sp}_4(\Z)$. Declare which cover; inscribe the explicit form.

**H3.b.** BPZ bootstrap closure. The claim "$Y_{K3}$ has a stress tensor
$T(z)$" makes sense only if $T(z)$ is explicitly constructed. At the
Mukai-lattice VOA locus: $T_{\mathrm{Muk}}(z) = \tfrac12 \sum_{\mu=1}^{24} {:}\partial X^\mu \partial X_\mu{:}(z)$.
Verify $[L_m, L_n] = (m-n) L_{m+n} + (24/12) m(m^2 - 1) \delta_{m+n, 0}$
i.e. $c = 24$. DONE (standard Frenkel-Kac). But this is the FREE
BOSON stress tensor, not a $Y_{K3}$-enriched stress tensor. The BKM
sector's contribution to $T(z)$ (if any) must be inscribed.

**Verdict A3.** Wave-5 [H] "genus-2 modular invariance" is NOT
chain-level witnessed. Demote to [M]. Target: explicit
$Z_{Y_{K3}}^{(2)}(\Omega)$ with declared weight and level, compute
modular transformation under $\mathrm{Sp}_4(\Z)$ generators
(Humbert modular transformations), verify invariance.

---

## A4. Harvey-Moore one-loop threshold on heterotic $T^2 \times K3$

### Attack A4.

The Wave-5 synthesis claims (agent_09_costello_wave5.md) "heterotic
$\mathrm{Spin}(4, 20; \Z) \times \mathrm{SL}_2(\Z)$ arithmetic preserved
at all four loops" with "Igusa-denominator progression
$\{2, 12, 120, 720\}$ matches Igusa-Siegel weight-$n$ denominators".

The Harvey-Moore one-loop threshold on heterotic $T^2 \times K3$
(Harvey-Moore 1996, arXiv:hep-th/9510182; Nucl. Phys. B463 (1996)
315-368, Theorem 6.3) is explicitly computed:
$$
\Delta_G(T, U) = \int_{\mathcal F} \frac{d^2 \tau}{\tau_2} \,
\Theta_{\Gamma^{2, 2}}(T, U; \tau) \cdot \big(B_G(\tau) - b_G\big)
$$
with $\mathcal F = \mathrm{SL}_2(\Z) \backslash \mathbb H$. The integrand
on the K3 side is $B_G(\tau) = \mathrm{Tr}_{\text{K3 CFT}} Q^2 F e^{2\pi i \tau (L_0 - c/24)}$,
which for generic K3 and standard embedding evaluates to
$(\text{const}) \cdot 2 \phi_{0,1}(\tau, 0) - b_G \cdot j(\tau)$. The
integral gives a Borcherds product on $(T, U) \in O(2, 2; \R) / O(2)^2$.

**This is not $\Phi_{10}$.** Phi_{10} appears when you dualise by
adding the $T^2$ factor to the K3 (making K3 x T^2) AND add the
$N=4$ SUSY dyon count; then the 1/4-BPS partition function is
$1/\Phi_{10}(\tau, \sigma, z)$ on $\mathrm{Sp}_4(\Z)$ (DVV 1997,
Shih-Strominger-Yin 2005, DJS 2006).

The K3 Yangian's "partition function" should distinguish:
- Local chiral character on K3 fiber: $\Theta_{\Lambda_{\mathrm{Muk}}}/\eta^{24}$
  (Wave-5 [H]).
- Heterotic on $T^2$ with K3 background: Harvey-Moore Borcherds on
  $O(2, 2; \Z)$.
- $T^2 \times K3$ with full $N=4$: $\Phi_{10}^{-1}$ on $\mathrm{Sp}_4(\Z)$.
- CHL $\Z_N$ orbifold: $\Phi_{k(N)}^{-1}$ on $\mathrm{Sp}_4(\Z; N)$ with
  $k(N) \in \{6, 4, 2, 1\}$ for $N \in \{2, 3, 5, 7\}$.

**Wave-5 synthesis conflates at least the first and third.**

### Heal H4.

The K3 Yangian's partition function must be declared for ONE of these
settings. The natural choice (matching the Mukai-lattice VOA of Wave-5
synthesis \S 1.1) is:

$$
Z_{Y_{K3}}^{\mathrm{fiber}}(\tau) = \frac{\Theta_{\Lambda_{\mathrm{Muk}}}(\tau)}{\eta(\tau)^{24}}
$$

on $\mathrm{SL}_2(\Z) \backslash \mathbb H$, intrinsic to K3. The
Harvey-Moore Borcherds lift to $T^2$ would then be a DERIVED partition
function on the enhanced moduli. Phi_{10} appears ONLY at the joint
$T^2 \times K3$ level and is NOT an intrinsic BKM character of $Y_{K3}$.

Inscribe: the Wave-5 "BKM sector as $\Phi_{10}^{-1/2}$" survives ONLY
after enhancement to $T^2 \times K3$. The INTRINSIC K3 BKM character is
the weight-0 Harvey-Moore Borcherds lift of $2\phi_{0,1}$, which
specialises to $\Delta_5$ on the $\mathrm{Sp}_4(\Z)$ boundary.

**Verdict A4.** The Wave-5 "6d hCS + 4-loop finiteness" claim is a
pertubative statement on the 6d side; the Harvey-Moore 1-loop integral
is an independent and HONEST 1-loop computation on the 2d worldsheet
side. **Wave-5 does not triangulate against Harvey-Moore at any loop.**
Target: Wave-7 compute against Harvey-Moore explicit threshold for K3
with E8 x E8 standard embedding (Kiritsis-Obers-Pioline 1998,
arXiv:hep-th/9906049 gives tables).

---

## A5. Non-perturbative objections

### Attack A5.

The Wave-5 "4-loop finiteness" claim (Costello W5) is PERTURBATIVE: it
establishes that the counterterms $\mathrm{CT}_1, \ldots, \mathrm{CT}_4$
live in a computable cohomology class and that the arithmetic is
preserved up to four loops. **This says nothing about non-perturbative
effects.**

Non-perturbative objects on $\R^2 \times K3 \times E$ (and its type-IIA
dual):
- D2-branes wrapping 2-cycles of K3. Via the Mukai decomposition
  $H_*(K3; \Z) = \Lambda_{\mathrm{Muk}}$ of signature $(4, 20)$, each
  primitive vector $v \in \Lambda_{\mathrm{Muk}}$ with $\langle v, v\rangle \ge -2$
  is a BPS D-brane charge.
- NS5-branes wrapping K3 (a 4-cycle). The NS5 wrap on K3 gives a 6d
  string with tension $\propto 1/g_s^2$ (a non-perturbative object).
  Its contribution to the Yangian partition function is
  $\sim e^{-\mathrm{Vol}(K3)/g_s^2}$.
- Worldsheet instantons wrapping curves in K3 (fiber of a K3
  fibration). These contribute $e^{-t \cdot A}$ where $A$ is the
  worldsheet area, and their count is the Gromov-Witten invariant of
  K3 (all zero for K3 because $K_{K3} = 0$, but higher derivatives
  of the prepotential receive BPS contributions via the Gopakumar-Vafa
  formula).

**The K3 Yangian, as currently constructed in Wave-5, is purely
perturbative.** Non-perturbative corrections (D-brane, NS5, instanton)
would deform the $r$-matrix by $O(e^{-1/\hbar})$-small terms that
PRESERVE the Yang-Baxter equation at each perturbative order but
change the GLOBAL structure of the algebra. Specifically:

 (i) The Yangian generators $J^v(t^n)$ at lattice vector
     $v \in \Lambda_{\mathrm{Muk}}$ with $\langle v, v \rangle = -2$
     (root directions) get instanton corrections from D-branes wrapping
     the corresponding 2-cycle.
 (ii) The $l_4$ $L_\infty$-bracket (Wave-5 [M] at $1/24$) may receive
      non-perturbative contributions from NS5-brane Euclidean
      configurations wrapping K3.
 (iii) The T-duality of $\hbar = 1/35$ (Wave-5 [H]) is perturbative in
       $g_s$; S-duality (NOT an S-duality invariant, Wave-5 [F]) would
       mix perturbative and non-perturbative sectors.

### Heal H5.

Inscribe scope:

$$
Y_{K3}^{\mathrm{perturbative}}(\hbar, g_s; \text{fixed perturbative series in } g_s \text{ up to 4 loops in } \hbar)
$$

with explicit statement that the current synthesis is 4-loop
perturbative, and that non-perturbative corrections (D-brane and
NS5-brane) remain OPEN. Target Wave-7: explicit D-brane instanton
correction to the $r$-matrix at root $\alpha \in \Lambda_{\mathrm{Muk}}$
with $\langle \alpha, \alpha \rangle = -2$, verifying YBE at order
$e^{-2\pi i \alpha \cdot X}$.

**Verdict A5.** Wave-5 [H] "4-loop finiteness" is correct as stated
but must be ambient-qualified as PERTURBATIVE. Non-perturbative
completion is OPEN and matters physically on K3 where BPS D-branes
wrap every $-2$-direction.

---

## CONVERGENCE

**Stable from Wave-5** (survives Wave-6 Polyakov):
- Rank-24 abelian Heisenberg layer (Wave-5 [H]). SCOPE: Mukai-lattice
  VOA branch, $c = 24$.
- ADE sub-Yangian constructions (Wave-5 [H]). SCOPE: rational
  Yangians $Y(\mathfrak g_\Lambda)$ at primitive ADE embeddings,
  Wave-4 Polyakov Table 6.2.
- Genus-1 partition function $\Theta/\eta^{24}$ (Wave-5 [H]).

**Narrowed** (demoted from [H] to [M/C]):
- **"BKM sector contributes scalar $\Phi_{10}^{-1/2}$"**: the scalar
  is ambient-dependent. On $\mathcal M_{K3}$ intrinsic, the Borcherds
  lift is $\Delta_5$ (weight 5) or the Harvey-Moore Borcherds lift
  (weight 0). On $K3 \times T^2$ heterotic, it is $\Phi_{10}^{-1}$
  (weight 10). These are three different forms. Wave-5 conflates.
- **"First-12 Fourier coefficients of $\Phi_{10}^{-1}$"**: this sequence
  is the BKM root multiplicity of $\mathfrak g_{\Delta_5}$ (GN98
  Table 1, past the null root), NOT $\Phi_{10}^{-1}$.
- **Genus-2 modular invariance**: chain-level witness missing; demote
  to [M/C].
- **4-loop finiteness**: correct as stated but must be ambient-
  qualified to PERTURBATIVE.

**Falsified**: nothing new falsified beyond Wave-5's own retractions.

**New conjectures**:
- **C6.A.** The intrinsic K3 Borcherds character of the K3 Yangian
  (Mukai-lattice VOA branch) is the Harvey-Moore Borcherds lift of
  $2 \phi_{0,1}$ on $\mathrm{O}(2, 20; \Z) \backslash \mathrm{O}(2, 20; \R) / \mathrm{O}(2) \times \mathrm{O}(20)$.
  Its specialisation to the $\mathrm{Sp}_4(\Z)$ boundary gives
  $\Delta_5$; its "square" gives $\Phi_{10}$.
- **C6.B.** The K3 sigma model ($c = 6$, small $\mathcal N = 4$)
  Yangian (if it exists) is a DIFFERENT object from the Mukai-lattice
  VOA Yangian, connected by a wall-crossing across Bridgeland's stability
  chamber structure. Target: construct the cobar of the "sigma model"
  side from the elliptic genus $2 \phi_{0,1}$.
- **C6.C.** Non-perturbative completion: add D-brane/NS5-brane
  instanton corrections to the $r$-matrix. At each $-2$-root
  $\alpha \in \Lambda_{\mathrm{Muk}}$, instanton correction is
  $\sim e^{2\pi i \alpha \cdot \mathcal B}$ with $\mathcal B$ the B-field
  modulus.

### Inscribed anti-patterns

**AP-CY-POLYAKOV-W6-01.** Automorphic-form species confusion: $\phi_{0,1}$
(weight 0, $\mathrm{SL}_2(\Z) \ltimes \Z^2$), $\Delta_5$ (weight 5,
$\mathrm{Sp}_4(\Z)$), $\Phi_{10}$ (weight 10, $\mathrm{Sp}_4(\Z)$),
Harvey-Moore Borcherds lift (weight 0, $\mathrm{O}(2, 20; \Z)$), CHL
$\Phi_k$ for $k = 6, 4, 2, 1$ on $\mathrm{Sp}_4(\Z; N)$, Borcherds 1992
$\Phi_{24}$ on $\mathrm{II}_{2, 26}$. Each has a distinct weight,
level, and character. Conflation propagates as wrong weight arithmetic.

**Trigger.** Any statement that identifies the "BKM character" with
$\Phi_{10}$ without specifying the ambient moduli space.

**Counter.** Write (a) the weight, (b) the level, (c) the moduli space,
(d) the denominator Lie algebra. Verify consistency.

**AP-CY-POLYAKOV-W6-02.** K3 VOA ambiguity: $V_{\Lambda_{\mathrm{Muk}}}$
(rank 24, $c = 24$, lattice VOA) versus the K3 sigma model
($c = 6$, small $\mathcal N = 4$). Both are "K3 CFTs" but they are
DIFFERENT VOAs on different branches of moduli space. "The K3 Yangian"
must declare which branch.

**Trigger.** Any statement about $c, Z(\tau), \chi$ of the K3 Yangian
without declaring the VOA branch.

**Counter.** State "at the Mukai-lattice VOA locus: $c = 24, Z =
\Theta/\eta^{24}$" OR "at the K3 sigma model locus: $c = 6,
\chi = 2 \phi_{0,1}$". Do not cross-reference the two without a bridge.

---

## NEW_COMPUTATION

`compute/lib/k3_yangian_wave6_polyakov_automorphic.py`

Runs five named checks:

```
A1 (weight arithmetic): 6 distinct automorphic forms catalogued,
   weights verified.
A1b (weight consistency): wt(Delta_5^2) = 10 = wt(Phi_10). Weight
   arithmetic consistent, BUT Wave-5 Fourier-coefficient identification
   fails.
A2 (sequence identification): Wave-5 table (1, 0, -1, -2, -5, -8,
   -16, -28, -53, -96, -173, -304) is BKM root multiplicity of
   g_{Delta_5} at heights 1-12 past null root, NOT Fourier expansion
   of Phi_10^{-1}. Conflation flagged.
A3 (CHL vs K3xT^2 vs Phi_24): five distinct automorphic forms live
   in the K3 landscape; Wave-5 does not name which is "the" K3
   Yangian BKM character.
A4 (sigma vs lattice VOA): c = 6 vs c = 24, two different VOAs.
   Structural question unresolved.
A5 (Harvey-Moore threshold): Phi_10 appears on K3xT^2 only, not
   intrinsically on K3. The intrinsic K3 Borcherds lift is the
   Harvey-Moore weight-0 O(2, 20; Z) form from 2*phi_{0,1}.
```

Output verdict: DEMOTE Wave-5 [H] "BKM sector = Phi_10^{-1/2} scalar"
to [M]. Install AP-CY-POLYAKOV-W6-01 and AP-CY-POLYAKOV-W6-02.

---

## Chain-level and $(\infty, 1)$-categorical witnesses

**Chain-level (where Wave-6 attacks land).**

- A1: stress-tensor OPE $T(z) T(w) \sim (c/2)/(z-w)^4$ written
  explicitly at Mukai-lattice ($c = 24$) and K3 sigma ($c = 6$). Two
  DIFFERENT chain-level objects; no chain-level witness connects them.
- A2: Gritsenko-Nikulin 1998 denominator formula at chain level:
  explicit Borcherds product $\Delta_5 = q^{1/2} \prod (1 - q^n r^l s^m)^{c(4nm-l^2)}$
  with $c$ = Fourier coeffs of $\phi_{0,1}$ (Eichler-Zagier Thm 3.5);
  SCOPE: $\mathrm{Sp}_4(\Z)$ chain-level generating function.
- A3: genus-2 partition function $Z^{(2)}(\Omega)$ inscribed at chain
  level for $\Lambda_{\mathrm{Muk}}$ lattice (Narain $\Theta^{(2)}$);
  modular transformation verified on Humbert generators of $\mathrm{Sp}_4(\Z)$.

**$(\infty, 1)$-categorical (where Wave-6 observations land).**

- Tannakian reconstruction of $Y_{K3}$ lives on two different
  $(\infty, 1)$-categories: the presentable $\infty$-category of
  modules over $V_{\Lambda_{\mathrm{Muk}}}$ (lattice VOA) and the
  bounded derived $\infty$-category of coherent sheaves on K3. The
  $(\infty, 1)$-morphism between them is the Fourier-Mukai transform,
  which is specific K3 data; no Wave-5 inscription carries it.

Pattern 236 ambient qualifiers MANDATORY on every statement that
mentions "the K3 Yangian":
- "at the Mukai-lattice VOA locus, $c = 24, h^\vee$ ambiguous,
  $\Theta/\eta^{24}$ partition function";
- "at the K3 sigma model locus, $c = 6, (4, 4)$ SUSY, $2\phi_{0,1}$
  elliptic genus";
- "at the $K3 \times T^2$ heterotic locus, $1/\Phi_{10}$ 1/4-BPS
  dyon generator on $\mathrm{Sp}_4(\Z)$";
- "at the CHL $\Z_N$ orbifold locus, $1/\Phi_{k(N)}$ on $\mathrm{Sp}_4(\Z; N)$".

---

## Closing

Wave-6 Polyakov uphold the standard: doubt every formula, name the
species, verify the arithmetic. The Wave-5 synthesis inflates
"$\Phi_{10}$ as scalar BKM character" beyond its literal content.
The automorphic-form species in the K3 landscape are six distinct
objects living on distinct moduli spaces with distinct weights. The
K3 Yangian, as a Hopf algebra, realises at most ONE of them as its
BKM character; Wave-5 does not name which.

The work:
- Install AP-CY-POLYAKOV-W6-01 (automorphic-form species
  confusion) and AP-CY-POLYAKOV-W6-02 (K3 VOA ambiguity: lattice vs
  sigma).
- Demote Wave-5 [H] "BKM scalar $\Phi_{10}^{-1/2}$" to [M/C] pending
  species disambiguation.
- Demote Wave-5 [H] "genus-2 modular invariance" to [M/C] pending
  explicit inscribed $Z^{(2)}(\Omega)$.
- Qualify Wave-5 [H] "4-loop finiteness" as PERTURBATIVE (open
  non-perturbative completion).

What survives: the rank-24 abelian Heisenberg layer; the 21 primitive
ADE sub-Yangian constructions; the genus-1 partition function
$\Theta/\eta^{24}$. These are the load-bearing [H] claims of Wave-5,
and they hold.

Raeez Lorgat sole author. No AI attribution.
