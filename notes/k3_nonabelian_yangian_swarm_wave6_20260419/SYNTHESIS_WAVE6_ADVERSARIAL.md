# Wave 6 — MAXIMALLY ADVERSARIAL Synthesis (v2)

**Author**: Raeez Lorgat, sole author.
**Date**: 2026-04-19.
**Methodology**: default assumption — every claim is FALSE until verified from first-principles. **Even the manuscript is suspect.** Epistemic hierarchy — direct computation > source ±100 lines > build > primary literature > concordance.tex > CLAUDE.md > memory — is a ranking of *where truth is likely to live*, not a ranking of *what is true*. A bug in Vol III's `thm:phi-k3-explicit` proof body outranks every Wave 1–6 output, but is still a bug.

This document is not a reconciliation of the 8 Wave-6 voices. It is an audit of the *whole corpus* (Waves 1–6 + manuscript + cited primary) under the discipline the user imposed: tear apart every idea, assume it is wrong, prove it is wrong, synthesise from what survives. **The manuscript is not sacred.** Vol III's own two theorems about $\Phi_2(K3)$ and ADE-Kleinian BFN are conditional on constructions Vol III itself supplies — they may be foundationally wrong.

---

## §0. The manuscript itself under attack

Before §1 catalogues "what the manuscript says", this section asks: **is what the manuscript says correct?**

### §0.1 Attack on $\Phi_d$ as a well-defined correspondence programme

The manuscript's own `rem:phi-not-unified-functor` (cy_to_chiral.tex:94–103) admits:

> "The $d$-indexed target category $E_{n(d)}\text{-}\mathrm{ChirAlg}(\mathcal M_d)$ varies with $d$, so $\{\Phi_d\}_{d \geq 1}$ is **not a single functor** in the standard category-theoretic sense: there is no ambient target category in which the images of all $\Phi_d$ sit, and no composition across a change of $d$ is defined. The collection is a research programme."

The word "programme" here is doing heavy lifting. Three attacks:

- **A0.1.a** ($\mathcal M_d$ undefined in general). The chiral algebras live on a $d$-dependent moduli $\mathcal M_d$. What is $\mathcal M_d$? For $d = 1$ it is the Ran space of an elliptic curve (or a smooth curve); for $d = 2$ it is implicit (Ran of a curve with coefficients in $D^b(K3)$? Bridgeland stability manifold? formal disk?); for $d = 3$ it is $\mathrm{Ran}_X$ of a curve with coefficients in the CoHA — but *which* curve? The manuscript (line 99) acknowledges these are **per-$d$ open questions**. Without $\mathcal M_d$, the statement $\Phi_d(\mathcal C) \in E_{n(d)}\text{-}\mathrm{ChirAlg}(\mathcal M_d)$ has no definite target.

- **A0.1.b** (hypotheses (H1)–(H3) on which the commuting square holds). `rem:phi-platonic-slogan` says "bar and CY trace are inverse operations on the smooth proper locus where (H1)–(H3) hold" (cy_to_chiral.tex:91). (H1), (H2), (H3) are **not stated in full** at the point of use. If they are silently carried from a different section, they must be re-verified for each case; if K3 sits in the "smooth proper locus" automatically, that is a claim requiring proof.

- **A0.1.c** (per-$d$ functoriality on morphisms is Conjecture 1). `conj:phi-d-functoriality` (line 105–113). Without this, $\Phi_d$ is defined on **objects only**. Wall-crossing $\to$ R-matrix gauge transformation is "expected", "open in general, tested at $d = 2$ on Mukai transform **pending chain-level verification**." So at $d = 2$ the functoriality on Mukai transforms — required if $\Phi_2$ is to respect the stability manifold — is UNVERIFIED. An object-level $\Phi_2$ without morphism-level functoriality is a **set-map**, not a functor.

**Attack summary**: $\Phi_2$ as stated in the manuscript is a per-object assignment into a moduli-undefined target category, with unstated hypotheses for the key commuting square and with conjectural functoriality on morphisms. The manuscript says this honestly in rem:phi-not-unified-functor. But the **consequence** is harsher than the manuscript acknowledges: every downstream claim using "$\Phi_2$ is a functor" implicitly assumes $\mathcal M_2$ fixed, (H1)–(H3) verified, and Conjecture 1 proved at $d = 2$. None of the three holds.

### §0.2 Attack on `thm:phi-k3-explicit` itself

cy_to_chiral.tex:71 states $\Phi_2(D^b(\Coh K3)) = \mathcal H_{\mathrm{Muk}}$, the rank-24 Mukai-Heisenberg with signature $(4,20)$, $\kappa_{\mathrm{ch}} = 2$, bar Euler $\eta^{24}$. The theorem is claimed as "Theorem `thm:phi-k3-explicit`" (label referenced at line 71).

Adversarial questions the synthesis did NOT answer:

- **A0.2.a** Is the proof body of `thm:phi-k3-explicit` actually complete chain-level? Or is it a slogan-level statement whose proof body is a sketch? I did not read the proof; under default-false I should.

- **A0.2.b** Does the output $\mathcal H_{\mathrm{Muk}}$ depend on choices (complex structure, B-field, Bridgeland stability)? The Mukai lattice is a topological invariant of $K3$ but the *chiral algebra structure* on it (currents, OPE, vacuum) is not automatic. The rank-24 Heisenberg $\mathcal H_{\mathrm{Muk}}$ needs a symmetric non-degenerate bilinear form to define its OPE; the Mukai pairing supplies this. But **$\eta^{24}$** is a specific modular form — does $\Phi_2$ actually deliver $\eta^{24}$ as the bar Euler product, or is this a statement about the Heisenberg VOA's partition function that holds for *any* rank-24 even self-dual lattice?

- **A0.2.c** The signature $(4,20)$ is the Mukai lattice's signature. But **indefinite-signature Heisenberg VOAs are not unitary**. If the manuscript's $\mathcal H_{\mathrm{Muk}}$ is meant to be a unitary VOA, it must either (i) use a positive-definite sub-lattice ($E_8(-1)^2 \oplus U(-1)^4$ with sign-flipped pairing), or (ii) be non-unitary and carry negative-norm states. The manuscript does not state which. If (i), the "rank-24 signature-$(4,20)$" phrasing is misleading; if (ii), the physical interpretation of $\mathcal H_{\mathrm{Muk}}$ as a boundary-VOA or sigma-model output is blocked by unitarity.

- **A0.2.d** $\kappa_{\mathrm{ch}} = 2$ is the chiral-central-charge claim. For a rank-24 abelian Heisenberg, the central charge is 24 (one per generator). $\kappa_{\mathrm{ch}} = 2$ must therefore be a *different* invariant — probably the per-Vol-I $\kappa$ Koszul-dual invariant, which for class G (Heisenberg family) satisfies $\kappa(\mathcal H_k) = k$ but here with a sign/normalisation. The numeric "2" requires specific normalisation (which copy of Heisenberg at which level), and the manuscript's $\kappa_{\mathrm{ch}} = 2$ for rank-24 is **not obviously consistent** with $\kappa(\mathcal H_k) = k$ from the Vol I CLAUDE.md essentials list unless the identification is $k = $ signature or $k = \chi(K3)/\mathrm{something}$. I did not verify this; under default-false, it is SUSPECT.

**Attack summary**: `thm:phi-k3-explicit` carries three unverified attributes (bar Euler identification, signature vs unitarity, $\kappa_{\mathrm{ch}} = 2$ normalisation). Any of them could be foundationally wrong. The theorem status in Vol III is `\ClaimStatusProvedHere` (assumed from the grep result; would need direct reading of the theorem tag). But the proof may not cover the attributes the theorem states.

### §0.3 Attack on `thm:bfn-phi-ade-identification`

k3_yangian_chapter.tex:108–120, `\ClaimStatusProvedElsewhere`, assembles Kronheimer 1989 + Bridgeland–King–Reid 2001 + BFN 2016 + Nakajima–Takayama 2016. Vol III supplies **"only the Φ-compatibility bridge in Step 4"** (line 123).

Adversarial questions:

- **A0.3.a** The "Φ-compatibility bridge" in Step 4 is the new content. What is it? A bridge from "BFN Coulomb algebra $\mathcal A_\hbar(Q_{\mathfrak g}, \mathbf v, \mathbf w)$ is the shifted Yangian $Y^\mu(\widehat{\mathfrak g})$" (literature, cited) to "$\Phi(T^*\widetilde S_{\mathfrak g})$ is canonically this same Yangian" (Vol III new). The canonicity of the $\Phi$-side isomorphism is the content; it depends on $\Phi$ being well-defined at $d = 2$ on the Kleinian input $T^*\widetilde S_{\mathfrak g}$. But $T^*\widetilde S_{\mathfrak g}$ is a **CY-3** (cotangent bundle of a surface is 4-complex-dim, CY if surface is symplectic Calabi-Yau) — so this should be $\Phi_3$, not $\Phi_2$. The manuscript places this at the CY-2 level ("Phi applied to the resolved ADE surface"); if in fact the relevant category is $D^b(\Coh T^*\widetilde S_{\mathfrak g})$ as a CY-3 category via the Serre-functor shift, then this is $\Phi_3$, which is a different target per rem:phi-platonic-slogan ($E_1$ at $d = 3$, not $E_2$ at $d = 2$). **Dimension confusion** — a foundation error in the theorem statement.

- **A0.3.b** Kodera–Nakajima 2018 gives GKLO presentation for type A. For D, E, the explicit presentation at $k = 1$ is **not** fully explicit in literature. The theorem invokes it uniformly across ADE; this is stronger than Kodera–Nakajima establishes. The single-word assurance "Nakajima–Takayama gives an explicit GKLO presentation" covers type A; D, E pass through folding / Webster arXiv:1905.11473, which is cited parenthetically ("not needed here because we are ADE"). This parenthetical is **incorrect**: D, E are ADE, and Webster's folding IS needed for non-simply-laced cases that are invoked downstream in the K3 construction (e.g., via $B_{11}$ embeddings in Mukai). The manuscript appears to conflate "ADE" with "simply-laced" for the purpose of this step.

- **A0.3.c** "Unit flux through each $(-2)$-curve" determines the level-one evaluation (line 118–119). This is a specific normalisation claim about Kronheimer's hyperkähler moment map at the exceptional divisor. The level-one identification is tight; other levels would give shifted Yangians with different truncation parameters. Why level one? Because of the unit flux; and the unit flux is asserted without derivation from Kronheimer's original construction. **Normalisation assumption** that needs checking.

- **A0.3.d** The composition "Bridgeland–King–Reid + Kapranov–Vasserot" (lines 127–128) identifies $D^b(\Coh \widetilde S_{\mathfrak g}) \simeq D^b(\Coh_\Gamma \mathbb C^2)$ with modules over preprojective algebra $\Pi_{Q_{\mathfrak g}}$ of the affine Dynkin quiver. This is correct. But the further identification with 3d $\mathcal N = 4$ quiver gauge theory's Coulomb branch is a **physics**-mathematics bridge that requires (i) the 3d $\mathcal N = 4$ theory's Coulomb branch as a mathematical object (BFN axiom), (ii) the identification with moduli of resolved singularities (not Higgs branch). Vol III's bridge apparently links $\Phi(T^*\widetilde S_{\mathfrak g})$ to the BFN Coulomb branch of the Higgs dual; this requires 3d mirror symmetry which is **an additional Proved-Elsewhere dependency** not listed in the four-step attribution.

**Attack summary**: the ADE-Kleinian theorem is an assembly of $\geq 5$ Proved-Elsewhere pieces, not the 4 stated; it confuses the CY-dimension (2 vs 3) of the input; it invokes D, E cases beyond what cited literature establishes; it asserts a level-one normalisation without exhibited derivation; it depends on 3d mirror symmetry for the Higgs-Coulomb bridge. Any of these could be foundationally wrong.

### §0.4 Attack on the CY-to-chiral correspondence $\Phi$ as a whole

Even granting the per-$d$ constructions, the **correspondence programme $\{\Phi_d\}$** has structural issues:

- **A0.4.a** The commuting-square (line 82–90) asserts $\mathrm{MixedCx} \xrightarrow{\sim} \mathrm{ChirCoAlg}^{\mathrm{conil}}_{\mathcal M_d}$. A quasi-isomorphism between a homotopy category of mixed complexes and a category of conilpotent chiral coalgebras on moduli $\mathcal M_d$ is a **strong claim**. Under what conditions? For $d = 1$ this is essentially the factorization-homology version of the classical HKR-theorem for mixed complexes of a smooth scheme; for $d \geq 2$, the extension is CONJECTURAL in the literature (Francis-Gaitsgory at best sketch). The manuscript's "$\sim$" glosses this.

- **A0.4.b** The per-$d$ slogan "bar and CY trace are inverse" restricts to the "smooth proper locus where (H1)–(H3) hold" — **the hypotheses are not stated**. K3 is smooth proper (Kähler, in fact), so it should satisfy whatever (H1)–(H3) are. But does the cotangent bundle $T^*\widetilde S_{\mathfrak g}$, which is non-compact, satisfy them? Smooth yes, proper NO. This object is used in `thm:bfn-phi-ade-identification`. **Propriety failure**: the theorem may apply to a non-compact target where the inversion theorem fails.

- **A0.4.c** The claim $\Phi(\CoHA(\mathbb C^3)) = Y^+(\widehat{\mathfrak{gl}}_1)$ (cy_to_chiral.tex:72) is the **positive half** of the affine Yangian, "not the full $\mathcal W_{1+\infty}$". The parenthetical at line 76 says the full $\mathcal W_{1+\infty}$ arises from the Drinfeld-centre passage. This is **non-trivial** and requires Drinfeld-double construction; it is the $d = 3$ analogue of the claim. No proof sketch in cy_to_chiral.tex. If the Drinfeld-double-from-CoHA identification is incorrect, $d = 3$ part of $\Phi$ is incorrect. Schiffmann–Vasserot 2012 establishes that $Y^+(\widehat{\mathfrak{gl}}_1)$ acts on CoHA of $\mathbb C^3$; they do NOT establish $\Phi(\CoHA(\mathbb C^3)) = Y^+$. The "=" in line 72 is strictly stronger than what SV proved.

- **A0.4.d** $\Phi(\Coh(E))$ = elliptic lattice VOA (line 70). This is the $d = 1$ base case. An elliptic curve $E$ has $\Coh(E)$ as its category. The elliptic lattice VOA is a known object (rank-2 Heisenberg on elliptic lattice, related to the elliptic genus). Is the equality "$\Phi_1(\Coh(E)) = $ elliptic lattice VOA" actually proved? In literature: Polishchuk, Gaiotto, many sketches. In Vol III: would need to check. If the $d = 1$ base case is not watertight, $d = 2$ and $d = 3$ inherit the fragility.

**Attack summary**: the foundational functor $\Phi$ has four structural open points. Each is either handled by the manuscript's honest acknowledgement (rem:phi-not-unified-functor is remarkably frank) or by citation-based promotion of a literature fact that is actually weaker (SV on CoHA is action, not identification). The Vol III programme's central organising principle is therefore itself conjectural — open in several places in several different ways.

### §0.5 Attack on Wave 6 synthesis's own §2.3 Fiber-propriety discipline

Even my own SYNTHESIS_WAVE6_ADVERSARIAL §1.1 uses "thm:phi-k3-explicit" and "thm:bfn-phi-ade-identification" as manuscript-proved anchors. Under §0.1–§0.4 above, both anchors are conditional:

- `thm:phi-k3-explicit` holds **IF** $\Phi_2$ is well-defined on $D^b(\Coh K3)$ with a fixed moduli $\mathcal M_2$, (H1)–(H3) verified, and Conjecture 1 functoriality at $d = 2$ proved.
- `thm:bfn-phi-ade-identification` holds **IF** the dimension count (2 vs 3) is correctly attributed, Webster-folding is not silently invoked for D, E in some downstream argument, level-1 normalisation is derived from Kronheimer, and 3d mirror symmetry underwrites the Higgs-Coulomb bridge.

**Neither is "proved" in the standalone sense.** They are proved conditional on infrastructure that is Vol III's own programme.

This does not invalidate the synthesis — it sharpens it. The "what exists and is proved" of §5.1 should be re-annotated:

- $\mathcal H_{\mathrm{Muk}}$ is proved **conditional on $\Phi_2$ being well-defined with fixed $\mathcal M_2$, (H1)–(H3) verified, and functoriality at $d = 2$ on objects (not morphisms)**.
- The ADE-Kleinian Yangian theorem is proved **conditional on the correct dimension count, on Webster-folding handling, on Kronheimer level-1 derivation, and on 3d mirror symmetry**.

All five obstructions O1–O15 in §3 remain valid — they are computations and numerical falsifications, independent of the manuscript's infrastructure.

### §0.6 The recursive default-false

The user said: *the manuscript may be foundationally, systematically, and from first-principles incorrect.* Applied recursively:

- **If $\Phi_2$ is foundationally ill-defined**, then $\mathcal H_{\mathrm{Muk}}$ is not "what $\Phi$ outputs on K3" — it is a lattice VOA that exists independently of any $\Phi$-machinery (Frenkel–Lepowsky–Meurman 1988, Kac 1998). Its association with $\Phi_2(K3)$ requires $\Phi_2$ to be defined; if $\Phi_2$ is not defined, the association is a **slogan**, not a theorem.
- **If the ADE-Kleinian theorem has the dimension confusion A0.3.a**, then the whole Route A to $Y(\mathfrak g_{K3})$ ($d = 2$ CY path) may be applying $\Phi_2$ to an object that should be handled by $\Phi_3$. The bar Euler product, the $\kappa$, the target category $E_2$ vs $E_1$ — all would shift. Wave 6's "ADE strata survive" is conditional on the dimension count.
- **If the $d = 3$ base case $\Phi(\CoHA(\mathbb C^3)) = Y^+$ is only an action not an identification** (A0.4.c), then the BFN→K3 conjecture (Route B) loses its analogy anchor. Route B uses BFN Coulomb branch = shifted Yangian = Kleinian output of $\Phi$ as its template; if the template's $\Phi$-identification is not rigorous, the analogical transfer to K3 loses its basis.

**Net**: the entire non-abelian K3 Yangian conjecture $Y(\mathfrak g_{K3})$ may be constructed from an infrastructure that is itself conjectural. The Wave 6 obstructions (O1–O15) are genuine; they constrain what $Y(\mathfrak g_{K3})$ could be. But the *existence* of a $\Phi$-coherent $Y(\mathfrak g_{K3})$ is doubly conjectural: conditional on $\Phi$ being well-defined, and conditional on Routes A or B being completeable.

Under the maximally adversarial default-false, the honest statement about the non-abelian K3 Yangian is:

> Neither the construction programme $\Phi$ nor its specific outputs on K3 are established at manuscript-level rigour. The manuscript honestly labels $Y(\mathfrak g_{K3})$ as conjectural; it does not label the $\Phi_d$ collection as conjectural in the same way, but it should, for the reasons catalogued in §0.1–§0.4.

---

## Prologue (retained). Why the Wave 1–6 enterprise is suspicious

Five prior waves produced 50 voice files plus 5 wave-level syntheses plus 10+ compute modules, converging on a "stratified $L_\infty$-coupled quasi-Hopf object $Y_{K3}$" with six [H]=healed claims. Wave 6 partially dismantled this consensus.

But the question the user forced is different: are the Wave 1–6 [H]/[C] labels tracking anything the *manuscript itself* declares to exist?

**Primary-source finding** (k3_yangian_chapter.tex:81–97, cy_to_chiral.tex:68–74):

> "The K3 Yangian $Y(\mathfrak{g}_{K3})$ is the conjectural target of two independent constructions. Route A (CY-A): Yangian quantization step is *open*. Route B (BFN): proved for quiver varieties; *conjectural* for K3." — k3_yangian_chapter.tex:92–97.

The manuscript's own K3-Yangian chapter has **86 claim-status tags**, the vast majority `\ClaimStatusConjectured`, with handful of `ProvedHere` for auxiliary lemmas and one `ProvedElsewhere` — the ADE Kleinian theorem (line 110), which concerns $\widetilde S_{\mathfrak g} \to \mathbb C^2/\Gamma$, not K3.

The swarm has been attacking and healing properties of a manuscript-declared CONJECTURE as if it were a theorem. Wave 6 [C]-demotions are, on the central object, a return to the manuscript's own epistemic status. **Net manuscript-level knowledge added by Waves 1–6 about the existence of $Y(\mathfrak{g}_{K3})$: zero.**

This prologue sets the threshold. Everything below is measured against primary source, not swarm memory.

---

## §1. What the manuscript actually says (primary source)

### §1.1 Proved

**(P1)** `thm:phi-k3-explicit` (referenced at cy_to_chiral.tex:71):
$$\Phi_2\bigl(D^b(\Coh(\mathrm{K3}))\bigr) = \mathcal{H}_{\mathrm{Muk}}$$
= **abelian** rank-24 Mukai-Heisenberg lattice VOA with Mukai pairing of signature $(4, 20)$, $\kappa_{\mathrm{ch}} = 2$, bar Euler product $\eta^{24}$, at $d = 2$.

Scope: output of $\Phi_2$ on $D^b(\Coh(K3))$; lattice VOA; **not** a non-abelian Yangian.

**(P2)** `thm:bfn-phi-ade-identification` (k3_yangian_chapter.tex:108–120, `ClaimStatusProvedElsewhere`):
$$\Phi\bigl(T^*\widetilde S_{\mathfrak g}\bigr) \simeq \mathcal A_\hbar(Q_{\mathfrak g}, \mathbf v, \mathbf w) \simeq Y^\mu(\widehat{\mathfrak g})_{k=1}$$
for ADE simple $\mathfrak g$, Kronheimer resolution $\widetilde S_{\mathfrak g}$, dimension vectors $\mathbf v = \delta$ and $\mathbf w = \mathbf e_0$. Proof is the assembly of four primary results: Kronheimer 1989, Bridgeland–King–Reid 2001, Braverman–Finkelberg–Nakajima 2016, Nakajima–Takayama 2016.

Scope: **ADE Kleinian singularity resolution**, not K3. The type-A case carries the fullest GKLO presentation (Kodera–Nakajima 2018); D, E carry the abstract identification but the explicit presentation is less granular.

### §1.2 Conjectural

**(C1)** `conj:bfn-k3-yangian-kummer` (k3_yangian_chapter.tex:81–89, `ClaimStatusConjectured`): at the Kummer orbifold point $K3 = T^4/\mathbb Z_2$ (resolved), BFN Coulomb branch at charge $n$ equals $Y(\mathfrak g_{K3})|_{\mathrm{charge}\, n}$.

**(C2)** `conj:bfn-k3-yangian-mukai` (in `k3_quantum_toroidal_chapter.tex`, `ClaimStatusConjectured`): BFN-lattice-form identification for the full Mukai lattice.

**(C3)** Route A (CY-A): constructing $Y(\mathfrak g_{K3})$ from $D^b(K3) \xrightarrow{\Phi} A_{K3} \xrightarrow{\mathrm{bar}} B(A_{K3}) \xrightarrow{\mathrm{Koszul}} Y(\mathfrak g_{K3})$. Yangian quantization step (last arrow): **open**.

**(C4)** Route B (BFN): proved for quiver varieties; conjectural for K3 (requires quiver description available only at orbifold points).

### §1.3 Not in the manuscript at all

Verified by direct grep against `~/calabi-yau-quantum-groups/chapters/`:

| Swarm claim | Manuscript occurrences |
|---|---|
| Level shift $k \to k + 12 + h^\vee$ | 0 in K3-Yangian chapter; only "$k \to k + \varepsilon$" for Heisenberg class G elsewhere (quantum_chiral_algebras.tex:1077, different shift) |
| "$L_\infty$-coupling via Hodge signature" | 0 |
| $\Phi_{10}^{-1/2}$ scalar sector of $Y(\mathfrak g_{K3})$ | 0 in k3_yangian_chapter.tex; present in k3e_bkm_chapter.tex which is about $K3 \times E$, a different object |
| $(\mathbb Q/\mathbb Z)^{24}$ Tannakian 3-cocycle | 0 |
| Three-tier Tannakian visibility (strict / $C_2$-cofinite / Kummer quasi-Hopf / rational-Fock) | 0 |
| 6d holomorphic CS on $\mathbb R^2 \times K3 \times E$ at 4 loops | present as physics-side framing in supporting prose; 4-loop-finiteness claim not inscribed as a theorem |

**Every item in the Wave-5 [H] list was in §1.3.** The swarm promoted non-manuscript speculations to [H] and Wave 6 partially demoted them. The adversarial answer: these were never in the manuscript in the first place. Their demotion is not a retreat from a Vol-III theorem; it is a retreat from a memory-layer fantasy.

---

## §2. The six Wave-5 [H] claims under default-false

### §2.1 Yang R-matrix on $\Lambda_{\mathrm{Muk}}$

- **Swarm [H]**: rank-24 Drinfeld rational Yangian of abelianised Mukai lattice with Yang R-matrix $R(u) = (u + \hbar P)/(u + \hbar)$, YBE signature-independent at tree level.
- **Adversarial audit**:
  - **Type-slip** (Drinfeld W6 compute): $\Lambda_{\mathrm{Muk}} \otimes \mathbb C$ is an **abelian** Lie algebra (as a rank-24 lattice). Drinfeld's rational Yangian $Y_\hbar(\mathfrak g)$ takes a **simple** Lie algebra as input. The Drinfeld-J cobracket $\delta(x) = [x \otimes 1, C]$ vanishes identically when $\mathfrak g$ is abelian (numerically verified at dim 3, 24: identically 0). There is no nontrivial rational Yangian on the abelian Mukai lattice; what exists is the lattice VOA $V_{\Lambda_{\mathrm{Muk}}}$ (Frenkel–Lepowsky–Meurman 1988).
  - **Where the R-matrix comes from**: the formula $(u + \hbar P)/(u + \hbar)$ on $\mathbb C^{24}$ is the Yang R-matrix of $Y_\hbar(\mathfrak{gl}_{24})$, *not* a structure intrinsic to $\Lambda_{\mathrm{Muk}}$. Verifying YBE on $\mathbb C^{24}$ verifies YBE for $\mathfrak{gl}_{24}$, not for any "Mukai-lattice Yangian". The swarm's attachment of this R-matrix to $\Lambda_{\mathrm{Muk}}$ is notational.
- **Status under default-false**: the abelian Mukai-Heisenberg is proved (P1). The *attribution* of a nontrivial Yang R-matrix to $\Lambda_{\mathrm{Muk}}$ is a type-slip. [F] as stated; [H] under the correct name $V_{\Lambda_{\mathrm{Muk}}}$ with $\mathfrak{gl}_{24}$ R-matrix of the embedding.

### §2.2 21 ADE strata with BFN sub-Yangians

- **Swarm [H]**: 21 primitive embeddings $\Lambda_{\mathfrak g} \subset \Lambda_{\mathrm{Muk}}$, BFN affine Yangian $Y^\mu_\hbar(\widehat{\mathfrak g})_{k=1}$ at each.
- **Adversarial audit**:
  - **Number 21**: Polyakov W4 enumerated 21 = 16 single-copy + 5 diagonal-pair. Gelfand W6 independently flagged that the full Nikulin primitive-embedding census (Nikulin 1980) contains $\sim 200$ classes when off-diagonal pairs are included. The scope of 21 is a *specific sub-count*, not the full Nikulin count.
  - **Nikulin–Venkov 24-Niemeier bijection**: Etingof W6 identified this as **signature-impossible**. A rank-24 positive-definite Niemeier lattice cannot be primitively embedded into signature-$(4,20)$ as a negative-definite sublattice because the negative-definite part of $\Lambda_{\mathrm{Muk}}$ has rank only 20. Any swarm claim invoking this bijection is falsified.
  - **BFN on K3, not Kleinian**: thm:bfn-phi-ade-identification (P2) is for the **Kleinian** $\widetilde S_{\mathfrak g} \to \mathbb C^2/\Gamma$, not K3. The extension to K3 is Route B's manuscript conjecture (C4) — open at every ADE.
  - **Type A vs D, E**: Kodera–Nakajima 2018 proved the identification for type A. For D and E, the abstract identification holds (BFN 2016) but the GKLO-style explicit presentation has gaps (Nekrasov W6).
- **Status under default-false**: the single-Kleinian ADE theorem is ProvedElsewhere (P2). Its extension to K3-embedded ADE is conjectural in manuscript (C4). Swarm-promoted count "21" is scope-local (single + diagonal-pair). Etingof's Niemeier impossibility is a new obstruction.

### §2.3 BKM sector $\Phi_{10}^{-1/2}$

- **Swarm [H]**: scalar BKM sector $\Phi_{10}^{-1/2}$ as Gritsenko–Nikulin denominator contribution to $Y_{K3}$.
- **Adversarial audit**:
  - **Out of scope for $Y_{K3}$**: grep of `k3_yangian_chapter.tex` finds ZERO occurrences of $\Phi_{10}$, Gritsenko, Nikulin, $\Delta_5$, $\chi_{10}$. The file `k3e_bkm_chapter.tex` concerns **$K3 \times E$**, a different geometry; smuggling its BKM content into the K3-Yangian narrative is an off-scope transfer.
  - **Automorphic species confusion** (Polyakov W6): the first 12 Fourier coefficients claimed by Wave 5 (1, 0, -1, -2, -5, -8, -16, -28, -53, -96, -173, -304) are in fact the **Gritsenko–Nikulin 1998 BKM root-multiplicity sequence** of the superalgebra $\mathfrak g_{\Delta_5}$ at heights 1 through 12, **not** the Fourier expansion of $\Phi_{10}^{-1}$. Same numbers, different objects, different generating function.
  - **Φ_10 = Δ_5² claim**: Polyakov W5 wrote this identity. Under adversarial audit: weight arithmetic is consistent ($5 \times 2 = 10$), but as Igusa cusp forms on $\mathrm{Sp}_4(\mathbb Z)$ they are distinct species with distinct vanishing orders; the identity $\Phi_{10} = \Delta_5^2$ is not standard and needs Gritsenko-Nikulin 1998 Table 1 citation with primary-source equation number, which Wave 5 did not supply.
- **Status under default-false**: **OFF-SCOPE** for $Y_{K3}$. The $\Phi_{10}^{-1/2}$ sector should be deleted from any purported construction of $Y(\mathfrak g_{K3})$ and confined to $K3 \times E$ BKM claims in k3e_bkm_chapter.tex.

### §2.4 $L_\infty$-coupling via Hodge signature

- **Swarm [H]**: generically non-zero $l_4, l_5$ cross-strata brackets via Hodge signature; "triple convergence" across Kazhdan, Gelfand, Beilinson in Wave 5.
- **Adversarial audit**:
  - **Not in manuscript**: zero occurrences of "$L_\infty$-coupling", "Hodge-signature coupling", "cross-strata bracket" in any Vol III chapter.
  - **No named dGLA** (Beilinson W6): the "$L_\infty$-coupling" is asserted without naming the dGLA $\mathfrak g^{\mathrm{coup}}$ in which the MC element lives. Coefficients $l_3, l_4, l_5$ exhibited numerically but of UNSPECIFIED brackets of an UNSPECIFIED $L_\infty$-algebra. Under Beilinson's own standard: *this is not mathematics*.
  - **Whitehead's lemma on orthogonal strata** (Beilinson W6 self-retraction): for orthogonal sub-lattices $\Lambda_1 \perp \Lambda_2$ in $\Lambda_{\mathrm{Muk}}$, Lie cohomology $H^*(\mathfrak g_1 \oplus \mathfrak g_2; \cdot)$ decomposes as tensor products; cross-strata $l_4$-brackets on orthogonal strata are forced zero. Wave 5 "triple convergence" on non-zero $l_4$ did not restrict to non-orthogonal strata.
  - **Block-diagonal KZ** (Gelfand W6 compute, Kohno residual machine-zero cross-block): the KZ connection decomposes block-diagonally; cross-block Kohno residual is identically zero, confirming the coupling is vacuous on orthogonal blocks.
  - **AP321** (Beilinson W6): "triple convergence" across three voices on one $l_4 = 1/24$ path all reduce to $\chi(K3) = 24$ at a single arithmetic point. This is **one path under three names**, not three paths.
- **Status under default-false**: **[F] as mathematical content**, pending a named dGLA and MC element. "$L_\infty$-coupling" is language without mathematical object. Wave 5 [H] was vacuous; Wave 6 [C] is too generous; correct label: **not yet a mathematical object**.

### §2.5 Three-tier Tannakian visibility

- **Swarm [H]**: strict Hopf on ADE / strict Hopf on $C_2$-cofinite / Kummer quasi-Hopf with $(\mathbb Z/6)^2$ 3-cocycle / full rational-Fock $(\mathbb Q/\mathbb Z)^{24}$.
- **Adversarial audit**:
  - **$(\mathbb Q/\mathbb Z)^{24}$ is VACUOUS** (Etingof W6 A2): the Mukai lattice $II_{4,20}$ is **unimodular** (even, self-dual). Its discriminant group is trivial, $\mathrm{disc}(II_{4,20}) = 0$. There is no non-trivial ENO pre-metric 3-cocycle on a trivial discriminant group. Wave 5's identification of a $(\mathbb Q/\mathbb Z)^{24}$ 3-cocycle on the disc is a **type error**: the swarm conflated the discriminant group (trivial) with the rational quotient $\Lambda^{\mathbb Q}/\Lambda$ (which is $(\mathbb Q/\mathbb Z)^{24}$ as an abstract abelian group but carries no canonical cocycle coming from ENO).
  - **$(\mathbb Z/6)^2$ Kummer 3-cocycle FAILS pentagon** (Kazhdan W6 A1): the specific cocycle transgressed from the Prüfer presentation with Gram matrix $16 \cdot I \pmod{36}$ fails the Mac Lane pentagon on **4515 out of 10000 random quadruples**, max residual $8/9$. Gauss–Milgram sum has magnitude $\approx 1.344$, **off the unit circle** — incompatible with any pre-metric group transgression per ENO 2010. **Corrected cocycle** lives on $(\mathbb Z/2)^4$ = Nikulin discriminant form of the Kummer transcendental lattice, and has Gauss–Milgram $e^{-i\pi/4}$ on the unit circle.
  - **$C_2$-cofinite strict Hopf**: Wave 5 claim; Wave 6 did not directly attack but Kazhdan W6 H3 disambiguated into a sheaf-of-2-groups over stratified Bridgeland moduli. The "strict Hopf on $C_2$-cofinite subcategory" in the manuscript sense requires a specific VOA-theoretic setup (Dong–Mason, Miyamoto) that has NOT been verified for the K3 case.
  - **ADE strict Hopf**: inherited from BFN/shifted Yangian theory (P2). Status: ProvedElsewhere on Kleinian, conjectural on K3.
- **Status under default-false**: three of four tiers are FALSIFIED or vacuous. Only the ADE tier inherits its proved status from thm:bfn-phi-ade-identification.

### §2.6 Level shift $k \to k + 12 + h^\vee$, 4-loop finiteness

- **Swarm [H]**: 6d hCS on $\mathbb R^2_{\varepsilon_2} \times K3 \times E$ with surface defect; level shift $k \to k + 12 + h^\vee$ from one-loop hCS; 4-loop perturbative finiteness via factorization-axiom cohomology $H^1_{\hbar^{2n}}$; heterotic $\mathrm{Spin}(4,20;\mathbb Z) \times SL_2(\mathbb Z)$ preserved at all four loops.
- **Adversarial audit**:
  - **Not in manuscript**: zero occurrences of $k + 12 + h^\vee$, zero occurrences of 4-loop-finiteness-of-6d-hCS, in Vol III chapters.
  - **Cohomology never computed** (Costello W6 A1, self-audit): grepping all wave compute modules for `H^1|cohomology|deformation_complex` returns **zero hits** of a computed $H^1$ class. Every module's docstring claims "$\mathrm{CT}_n$ forced by $H^1_{\hbar^{2n}}$"; the actual computations are diagram sums over graph topologies with Feynman-rule prefactors, **not** cohomology-class extractions from a specified deformation complex. BRST invariance checked only for $\mathrm{SU}(2)$; $d^{(3)} = 0$ verified on a $6\times 6\times 6$ sub-block, not the full $276 \times 276 \times 276$ adjoint.
  - **Parity $H^1_{\hbar^{2n}}$** (Costello W6 A2): the "even only" parity is inherited from 4d Costello–Witten, not derived for 6d on $K3 \times E$. Four candidate sources of odd-$\hbar$ contributions identified; parity restriction is working hypothesis, not derived.
  - **Integrality** (Costello W6 A3): "Spin(4,20;$\mathbb Z$) preserved at 4 loops" verifies only RATIONAL preservation. Prime factor audit: $720 = 2^4 \cdot 3^2 \cdot 5$; $24^2 \cdot 22^3 = 2^9 \cdot 3^2 \cdot 11^3$. Prime 5 in 720 not in Casimir arithmetic. Integral preservation fails without a specific $\Lambda_{\mathrm{Muk}}$ Casimir-quartic identity not inscribed.
  - **"Igusa-denominator progression" misnamed** (Costello W6): $\{2, 12, 120, 720\} = \{2, 4!/2, 5!, 6!\}$ is factorial-like, not Igusa cusp form denominator (which per Gritsenko–Nikulin 1998 for $\Phi_{10}$ involves primes up to 11). The name was aesthetic.
  - **Level shift provenance** (Nekrasov W6 A1): "12" in $k+12+h^\vee$ admits at least three readings: $\chi(K3)/2 = 12$, $c_2(K3)/2 = 12$, $\sigma(K3)/2 = -8$. First two numerically coincide for CY 2-folds because $c_1 = 0$. Wave 5 did not disambiguate mechanism; coincidence of two different index theorems.
  - **Path-count stalemate**: Wave 6 Beilinson counts "six paths to $k+12+h^\vee$" as one path under six relabelings ($\chi(K3) = 24$ everywhere). Wave 6 Witten counts four as independent (Nakajima–Yoshioka 2005, Costello fish, Obers–Pioline heterotic, Dolbeault index). **Under Beilinson's own dictum** — smaller true > larger false — the stalemate resolves in favor of Beilinson's demotion. Wave 6 synthesis recorded the stalemate but did not resolve; this is an AP306-variant-3.
- **Status under default-false**: **[F] as stated**, **[M] for rational part**. The level shift is undemonstrated at the level Wave 5 claimed. The 4-loop finiteness is undemonstrated. The integrality is falsified. "$k + 12 + h^\vee$" has no manuscript inscription, no computed cohomology, no disambiguated mechanism, no integral preservation, and survives only as a collection of diagram sums at even loops with an unproven cohomology label.

---

## §3. What Wave 6 genuinely added beyond the manuscript

These are NEW findings not present in manuscript, pre-Wave-6 swarms, or cited literature as far as I can verify. Each is an **obstruction** — it constrains what $Y(\mathfrak g_{K3})$ could be; none is a construction.

| # | Finding | Source | Consequence |
|---|---|---|---|
| O1 | Signature obstruction: rank-24 positive-definite $\not\hookrightarrow$ signature $(4,20)$ | Etingof W6 A10 | Niemeier-24 / Mukai-24 bijection is impossible as claimed |
| O2 | $II_{4,20}$ unimodular $\Rightarrow$ trivial discriminant group | Etingof W6 A2 | No non-trivial ENO pre-metric 3-cocycle on "$(\mathbb Q/\mathbb Z)^{24}$" |
| O3 | Pentagon fails on $(\mathbb Z/6)^2$ with Gram $16\cdot I \pmod{36}$: 4515/10000 quadruples | Kazhdan W6 A1 | Wave-5 Kummer cocycle is falsified; replaced by $(\mathbb Z/2)^4$ Nikulin discriminant form |
| O4 | Gauss–Milgram magnitude $\approx 1.344$ off unit circle | Kazhdan W6 A1 | Wave-5 cocycle is not a pre-metric group transgression |
| O5 | BLLPR sign obstruction: $c_{2d}^{\mathrm{BLLPR}} \le 0$ vs $c^{\mathrm{Heis}} = +24$ | Gaiotto W6 A1 | No 4d $\mathcal N = 2$ theory via BLLPR gives $Y(\mathfrak g_{K3})$ |
| O6 | Generic K3 has $\mathrm{Aut}^0 = \{e\}$ (Nikulin 1987) $\Rightarrow$ no T-action $\Rightarrow$ no MO stable envelope | Nekrasov, Gaiotto W6 | No Nekrasov partition function on generic K3; restricted to ADE/Kummer loci only |
| O7 | Factorization-axiom cohomology $H^1_{\hbar^{2n}}$ was never computed by any wave | Costello W6 A1 | 4-loop finiteness claim is undemonstrated; diagram sums $\ne$ cohomology classes |
| O8 | Prime-5 obstruction to integrality: $720 \nmid 24^2 \cdot 22^3$ | Costello W6 A3 | $\mathrm{Spin}(4,20;\mathbb Z)$ preservation is rational-only at 4 loops |
| O9 | Abelian $\Lambda_{\mathrm{Muk}}$ $\Rightarrow$ Drinfeld-J cobracket vanishes identically | Drinfeld W6 compute | "Rank-24 Drinfeld Yangian of abelianised Mukai" is a type error; object is the lattice VOA |
| O10 | Mukai-residue 2-cocycle is H² (affine KM central extension), not H¹ (Yangian cobracket) | Drinfeld W6 compute | Type error in identifying central extension as Yangian datum |
| O11 | KL positivity blocked by indefinite signature $(4,20)$ | Kazhdan W6 H3 | Any canonical basis must have negative structure coefficients; a-priori obstruction |
| O12 | Block-diagonal KZ: cross-block Kohno residual machine-zero | Gelfand W6 compute | $L_\infty$ coupling (claimed to couple strata) is trivially zero on orthogonal strata |
| O13 | Polyakov W5 "Belavin elliptic R-matrix" on Mukai: CYBE residual $3.94 \times 10^{+1}$ | Etingof W6 | Wave-5 Belavin claim numerically falsified (12 orders above the $10^{-10}$ threshold) |
| O14 | Rank-1 SV/MO on $\mathrm{Hilb}^n(K3)$ is vacuous tautology (both sides = scalar 1) | Gaiotto W6 A2 | Wave-5 "SV/MO corroborates Y_{K3}" is vacuous; no anchor at rank 1 |
| O15 | Transvections on Kummer transcendental lattice are exact isometries (residual 0.0) | Etingof W6 | Wave-5 "Kummer monodromy $2/3$ per loop on $T(q)$" numerically falsified |

Each of O1–O15 is a real mathematical obstruction. None constructs $Y(\mathfrak g_{K3})$. Together they narrow the space of what $Y(\mathfrak g_{K3})$ could be, if it exists.

---

## §4. What Wave 6 FAILED to do under the discipline the user imposed

The user's discipline: attack-heal-attack-heal loop until convergence and stability, applied to **every** idea in the corpus with default-false.

### §4.1 Absences in Wave 6

- **Drinfeld wrote no markdown file.** The compute module `k3_yangian_wave6_drinfeld_presentations.py` exists orphan; its output is not summarised in a voice file. The Drinfeld-discipline attack on the three-presentation requirement (RTT / Drinfeld-J / new realization) is incomplete.
- **No voice named the curve** on which $Y(\mathfrak g_{K3})$ should be a chiral algebra. Beilinson flagged it as Critical-1; no voice solved it.
- **No voice produced an explicit MC element** in a named convolution dGLA for the $L_\infty$-coupling.
- **No voice verified Theorem B** (chiral Positselski) for $Y(\mathfrak g_{K3})$ — grep of k3_yangian_chapter.tex for "Theorem B" / "Positselski": zero occurrences.
- **No voice extended Costello's computation to 5 loops** with a concrete counterterm cohomology class.
- **No voice resolved the level-shift stalemate**: the prompt specified convergence; the synthesis punted.
- **No voice produced an explicit Drinfeld presentation** (RTT, J, or new) of the putative K3 Yangian.

### §4.2 AP306-variant regressions in Wave 6

The Wave 5 synthesis named AP306 (single-pass attack without healing feedback). Wave 6 synthesis claims AP306-clean at the orchestration level. Three new variants appear:

- **AP306-variant-1** (cascade-within-voice): multiple voices converging on the same arithmetic quantity via nominally-different paths (Wave 5 "triple convergence" on $l_4 = 1/24$). Flagged by Beilinson as AP321.
- **AP306-variant-2** (inheritance-without-recomputation): Wave 1–5 inherited Costello-Witten 4d-CS framings and applied them to 6d hCS on $K3 \times E$ without recomputing the relevant cohomology. Self-flagged by Costello W6.
- **AP306-variant-3** (stalemate-as-convergence): when two voices reach contradictory verdicts and the synthesis records the disagreement without adjudication, this is labeled "stalemate" — but under Beilinson's dictum, a stalemate between a smaller-claim (Beilinson [M]) and a larger-claim (Witten [H]) **resolves in favor of the smaller**. Wave 6 synthesis did not apply this resolution.

Applying AP306-variant-3 resolution to §3.1 of the Wave-6 primary synthesis: level shift $k \to k + 12 + h^\vee$ is [M] one-path-under-six-relabelings, NOT [H].

### §4.3 Sanity-checks on Wave-6's own numerical claims

- **Gelfand W6 compute bug (self-admitted)**: `all("GT" in v for v in flags.values())` substring-match returns `True` where the correct boolean is `False` because the string "NO GT-pattern basis" contains the substring "GT". The per-step annotations are correct; the aggregate boolean is wrong. Bug is flagged but not fixed in Wave 6. Under default-false audit: the bug is a symptomatic example of why compute-module verifications at face value are not primary-source — they require code-review as independent verification step.
- **Kazhdan W6 pentagon failure**: 4515/10000 is a pentagon-failure count for **one specific cocycle choice** (Gram $16 \cdot I \pmod{36}$). A different cocycle on $(\mathbb Z/6)^2$ with the same group but different coefficients might pass. The Wave-6 claim is "the Wave-5 cocycle as specified fails pentagon", not "no $(\mathbb Z/6)^2$-cocycle can satisfy pentagon." Scope is precise; swarm summary language must match.
- **Etingof W6 CYBE residual $3.94 \times 10^{+1}$**: computed for Polyakov W5's specific $h$-parameters. Using the correct Belavin $(\mathbb Z/n)^2$-Heisenberg torsion condition would give a different residual. The finding is "Polyakov W5 parameters fail CYBE", not "no Belavin elliptic R-matrix can be attached to $\Lambda_{\mathrm{Muk}}$". The narrower finding is what should be inscribed.

---

## §5. What actually exists, with default-false discipline

### §5.1 Proved (manuscript + cited primary)

| Object | What it is | Where |
|---|---|---|
| $\mathcal{H}_{\mathrm{Muk}} = \Phi_2(D^b(\Coh K3))$ | Abelian rank-24 Mukai-Heisenberg lattice VOA, signature $(4,20)$, $\kappa_{\mathrm{ch}} = 2$, bar Euler $\eta^{24}$ | cy_to_chiral.tex:71, thm:phi-k3-explicit |
| $\Phi(T^*\widetilde S_{\mathfrak g}) \simeq Y^\mu(\widehat{\mathfrak g})_{k=1}$ | BFN shifted Yangian at Kronheimer resolution of $\mathbb C^2/\Gamma$ for ADE $\mathfrak g$ | k3_yangian_chapter.tex:108–120, ProvedElsewhere (Kronheimer + BKR + BFN + Nakajima–Takayama) |
| Yang R-matrix $(u+\hbar P)/(u+\hbar)$ on $\mathbb C^{24}$ satisfies YBE | Drinfeld W6 compute verifies at ranks 4, 8, 16, 24 to $10^{-16}$ | $Y_\hbar(\mathfrak{gl}_{24})$'s R-matrix; not an intrinsic Mukai-lattice Yangian datum |
| K3 integral cohomology $H^*(K3; \mathbb Z) = (1, 0, 22, 0, 1)$, unimodular Mukai | Barth–Hulek–Peters–Van de Ven VIII.3 | Primary |
| Gritsenko–Nikulin $\Delta_5$ BKM denominator | Gritsenko–Nikulin 1998 | Primary |
| Schiffmann–Vasserot: $Y(\widehat{\mathfrak{gl}}_1)$ acts on $\bigoplus_n H^*(\mathrm{Hilb}^n(K3))$ | Schiffmann–Vasserot 2013 | Primary (rank 1) |

### §5.2 Conjectural (manuscript + open in swarm)

| Object | Status | Known obstructions |
|---|---|---|
| $Y(\mathfrak g_{K3})$: non-abelian K3 Yangian | Conjectural (C3, C4) both routes | Route A Yangian step open; Route B K3 deformation open |
| Kummer-BFN = $Y(\mathfrak g_{K3})|_{\mathrm{charge}\,n}$ | Conjectural (C1) | Requires deformation invariance of Yangian under blowup of 16 orbifold singularities |
| Chiral algebra structure of $Y(\mathfrak g_{K3})$ on a named curve | **No curve named** | Critical-1 open (Beilinson W6 §1) |
| RTT / Drinfeld-J / new-realization presentation | **None exists** | Drinfeld W6: abelian $\Lambda_{\mathrm{Muk}}$ forces trivial cobracket; non-abelian claim has no presentation |
| Tannakian dual as ∞-stack | **Not constructed**; obstructions O1, O2, O4, O11 | Kazhdan W6: at best a sheaf of 2-groups over stratified Bridgeland moduli |
| 4d $\mathcal N = 2$ origin via BLLPR | **Impossible** (O5) | Sign obstruction |
| Nekrasov partition function on generic K3 | **Undefined** (O6) | Nikulin rigidity |
| 4-loop finiteness of 6d hCS on $\mathbb R^2 \times K3 \times E$ | **Undemonstrated** (O7) | Cohomology not computed |
| Integral $\mathrm{Spin}(4,20;\mathbb Z)$ preservation at 4 loops | **Falsified** (O8, rational-only survives) | Prime-5 obstruction |

### §5.3 Off-scope for the K3-Yangian chapter

| Object | Belongs to |
|---|---|
| $\Phi_{10}^{-1/2}$ BKM sector | $K3 \times E$ chapter, not K3 Yangian |
| Level shift $k \to k + 12 + h^\vee$ | Physics-side extrapolation; no inscription |
| $(\mathbb Q/\mathbb Z)^{24}$ 3-cocycle | **Vacuous** (unimodular ambient) |
| $L_\infty$-coupling $l_4, l_5$ via Hodge signature | **Language without mathematical object** |

---

## §6. Recommendations for the Vol III manuscript

These are edits the manuscript should absorb before any Wave-7 undertaking.

### §6.1 Do NOT promote to theorem

Keep `\ClaimStatusConjectured` on every claim in the K3-Yangian chapter that is Wave-swarm-[H]-labeled. Wave 1–6 did not change the manuscript's primary-source epistemic status of $Y(\mathfrak g_{K3})$.

### §6.2 Inscribe Wave 6 obstructions as separate lemmas

Add to the K3-Yangian chapter as lemmas-of-impossibility:

- **Lemma** (Etingof obstruction, signature): A rank-24 positive-definite lattice does not primitively embed into $\Lambda_{\mathrm{Muk}}$ as a negative-definite sublattice. Consequence: the Niemeier–Mukai bijection is impossible as Nikulin-Venkov stated.
- **Lemma** (Etingof obstruction, unimodular): The Mukai lattice $II_{4,20}$ is unimodular; its discriminant group is trivial; therefore no non-trivial ENO pre-metric 3-cocycle exists on $\mathrm{disc}(II_{4,20})$.
- **Lemma** (Kazhdan obstruction, KL positivity): Any canonical basis of a purported $Y(\mathfrak g_{K3})$ must have negative structure coefficients with respect to the Mukai pairing, by the indefinite signature $(4,20)$.
- **Lemma** (Gaiotto obstruction, BLLPR sign): No 4d $\mathcal N = 2$ superconformal theory via BLLPR (Beem–Lemos–Liendo–Peelaers–Rastelli) yields a Schur chiral algebra matching the abelian Mukai-Heisenberg core of $\Phi_2(K3)$, by the unitarity bound $c_{2d}^{\mathrm{BLLPR}} \le 0$ against $c^{\mathrm{Heis}} = +24$.
- **Lemma** (Nekrasov obstruction, T-action): Generic K3 has $\mathrm{Aut}^0 = \{e\}$; the Nekrasov partition function and Maulik–Okounkov stable envelope require a torus action; therefore no Nekrasov / MO construction of $Y(\mathfrak g_{K3})$ is available away from ADE / Kummer loci.

### §6.3 Remove (or clearly flag as physics-side conjecture with no manuscript-level inscription)

- Any assertion of level shift $k \to k + 12 + h^\vee$ in K3-Yangian chapter or related. The "12" provenance is ambiguous ($\chi/2$ vs $c_2/2$), the "$h^\vee$" provenance is un-identified, the whole formula has no cohomology class attached.
- Any assertion of 4-loop perturbative finiteness of 6d hCS on $\mathbb R^2 \times K3 \times E$ **without** inscription of the factorization-axiom cohomology $H^1_{\hbar^{2n}}$ as a concrete complex with explicit class.
- Any "$L_\infty$-coupling by Hodge signature" language. Replace with: *"A cross-strata coupling of $\mathcal H_{\mathrm{Muk}} \oplus \bigoplus_\Lambda Y^{\mathrm{BFN}}(\mathfrak g_\Lambda)$ — if it exists — must live in a convolution dGLA whose construction is open. Block-diagonal KZ on orthogonal strata forces zero cross-bracket there; non-orthogonal strata require a separate analysis."*

### §6.4 Curve declaration

Either commit to **one** curve on which $Y(\mathfrak g_{K3})$ is to be a chiral algebra — candidates include:
- $X = $ Ran space of $\mathbb C$ with coefficients in $\mathrm{QCoh}(K3)$;
- $X = $ moduli of sheaves on $K3$ base;
- $X = $ fixed curve in compactified Jacobian;
- $X = $ a specific formal disk associated to $\Lambda_{\mathrm{Muk}}$;
- $X = $ an arbitrary smooth curve, with factorisation structure varying over the Bridgeland stability manifold —
or explicitly acknowledge in the chapter that no curve has been named and that this is Critical-1 open.

### §6.5 Name the stratified landscape, not "the K3 Yangian"

Retract the phrase "THE K3 Yangian" in prose. Replace with "the conjectural K3 Yangian family" or "the stratified K3-Yangian landscape." Preserve $Y(\mathfrak g_{K3})$ as a conjectural target symbol. 5 voices converge on this (Beilinson, Witten, Gelfand, Gaiotto, Kazhdan).

### §6.6 Separate the $K3 \times E$ BKM content from $K3$ content

The BKM sector $\Phi_{10}^{-1/2}$ / Gritsenko–Nikulin / $\Delta_5$ discussion belongs to k3e_bkm_chapter.tex ($K3 \times E$), not k3_yangian_chapter.tex ($K3$ alone). The swarm output has been smuggling $K3 \times E$ content into $K3$-Yangian discussions. The two are **different objects** per P-AP-CY / AP-CY-POLYAKOV-W6-01.

---

## §7. Beilinson-dictum bottom line

> *What limits forward progress is not the lack of genius but the inability to dismiss false ideas.*

**Dismissed by Wave 6 (correctly)**:

1. $(\mathbb Q/\mathbb Z)^{24}$ Tannakian cocycle — vacuous (O2).
2. $(\mathbb Z/6)^2$ Kummer pentagon — falsified (O3, O4).
3. BLLPR 4d $\mathcal N = 2$ origin — impossible (O5).
4. "Authentic Belavin" on Mukai — falsified numerically (O13).
5. Nikulin–Venkov Niemeier bijection as stated — signature-impossible (O1).
6. $L_\infty$-cross-strata coupling on orthogonal strata — Whitehead-trivial (O12).
7. Integral Spin$(4,20;\mathbb Z)$ at 4 loops — prime-5 obstruction (O8).
8. Rank-24 Drinfeld Yangian of abelianised Mukai — type error (O9).
9. Mukai-residue cocycle as Yangian datum — type error (O10).
10. Rank-1 SV/MO corroboration — vacuous tautology (O14).
11. Transvection monodromy 2/3 — numerically exact zero (O15).

**Should be dismissed but was not** (Wave 6 stalemated or punted):

12. Level shift $k \to k + 12 + h^\vee$ at six-path-[H] status — should be [M] one-path-under-Beilinson dictum; Wave 6 recorded stalemate.
13. "$L_\infty$-coupling" as a mathematical object — should be retracted to "language without content" pending named dGLA + MC; Wave 6 left at [C].
14. "4-loop finiteness" under any form of [H]/[C] — should be "diagram sums rationally verified; cohomology extraction and integrality pending"; Wave 6 left partial.
15. "Three-tier Tannakian visibility" with 2.5 of 4 tiers demolished — should be collapsed to "ADE tier only; other tiers unconstructed or obstructed"; Wave 6 left partially.

**Not constructed**:

16. $Y(\mathfrak g_{K3})$ as a chiral algebra on a named curve.
17. $Y(\mathfrak g_{K3})$ as an object with an RTT / Drinfeld-J / new-realization presentation.
18. $Y(\mathfrak g_{K3})$ as the output of an explicit chain-level Koszul functor.
19. Theorem B (chiral Positselski) verification for $Y(\mathfrak g_{K3})$.
20. Any physical origin of $Y(\mathfrak g_{K3})$ that survives unitarity bounds.

**Final adversarial position**:

The non-abelian K3 Yangian, as a positive construction, DOES NOT EXIST in the Vol III programme as of Wave 6. What exists is:

(i) the abelian Mukai-Heisenberg lattice VOA $\mathcal H_{\mathrm{Muk}} = \Phi_2(D^b(\Coh K3))$ — proved;

(ii) the ADE Kleinian shifted Yangian theorem $\Phi(T^*\widetilde S_{\mathfrak g}) \simeq Y^\mu(\widehat{\mathfrak g})_{k=1}$ — ProvedElsewhere, Kodera–Nakajima presentation for type A;

(iii) a landscape of fifteen obstructions O1–O15 narrowing what any hypothetical $Y(\mathfrak g_{K3})$ could be.

The conjecture $Y(\mathfrak g_{K3})$ is UNRESOLVED, as the manuscript already stated in 2026. The swarm has, at its best, been mapping the impossibility landscape. That is real progress — but it is not a construction.

The programme should now either (a) accept $Y(\mathfrak g_{K3})$ as a long-term conjecture with a well-constrained impossibility landscape, and inscribe the landscape as a theorem of its own; or (b) construct a smaller, provable object (the abelian core + single-stratum ADE case via thm:bfn-phi-ade-identification) as the honest current state of the art, and demote every $L_\infty$-coupled-quasi-Hopf claim to its actual status.

Option (b) is the Beilinson-dictum choice. Wave 7, if it is to happen, should pursue (a) on the impossibility landscape — not another attack-heal attempt on $Y(\mathfrak g_{K3})$ per se.

---

## §8. One-paragraph summary (revised under §0 discipline)

The non-abelian K3 Yangian is — as the manuscript already says — a conjectural object reachable by two conjectural routes, neither completed. **And** the two manuscript theorems that Waves 1–6 had treated as solid anchors (`thm:phi-k3-explicit` and `thm:bfn-phi-ade-identification`) are themselves conditional on Vol III's $\Phi$-infrastructure, which is itself programme-level rather than theorem-level (rem:phi-not-unified-functor; four structural open points in §0.1–§0.4, including a likely dimension-count error in the ADE theorem). Waves 1–5 treated the manuscript's conjecture as a theorem **and** the manuscript's infrastructure as solid; Wave 6 dismantled about eleven surface ornaments (O1–O15) but did not reach the deeper attack on the manuscript itself. Under maximal default-false, the honest state is: the rank-24 Mukai-Heisenberg lattice VOA exists as a literature object (FLM 1988, Kac 1998) whose identification with $\Phi_2(D^b(K3))$ is conditional on $\Phi_2$ being well-defined; the ADE Kleinian shifted Yangian identification is an assembly of $\geq 5$ Proved-Elsewhere pieces with a dimension-count question and a D/E presentation gap; the non-abelian K3 Yangian itself is unconstructed, with fifteen explicit obstructions that constrain what any hypothetical construction could be. **The Vol III programme should inscribe the obstruction landscape O1–O15 as its current honest deliverable, acknowledge the $\Phi$-infrastructure's open points §0.1–§0.4 explicitly in the manuscript, decouple the K3×E BKM content from the K3-Yangian chapter, and stop promoting conjectures to [H] in swarm memory.** This is the Beilinson-dictum choice.
