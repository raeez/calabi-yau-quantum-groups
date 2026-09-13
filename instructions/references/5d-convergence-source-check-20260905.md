# 5d hCS convergence: source check

Date: 2026-09-05.

This instruction correction retires an unsupported source attribution. The all-orders identification and analytic-convergence target remain mathematical obligations. This correction changes no manuscript theorem or status ledger.

## Retired instruction assertion

The following bullet appeared in `instructions/mathematical-context.md`, line 61. Its complete wording is preserved as evidence of the retired assertion.

```text
- 5d hCS on $\mathbb{R} \times \mathbb{C}^2$ quantises to the Yangian VOA $Y^{\mathrm{VOA}}(\mathfrak{g})$ to all orders for simply-laced $\mathfrak{g}$ (Costello–Gaiotto–Yagi). Convergence (not asymptotic) by Kontsevich–Tamarkin formality on the holomorphic factor. Non-simply-laced: twisted Yangian; open at all orders.
```

## Primary source results

Costello–Yagi, *Unification of integrability in supersymmetric gauge theories*, appeared in *Advances in Theoretical and Mathematical Physics* 24 (2020), 1931–2041. The inspected arXiv version is v3, dated 8 September 2021. [Publication record](https://arxiv.org/abs/1810.01970v3).

Section 4, printed pp. 32–36, gives a localization derivation. Its six-dimensional input is the topological–holomorphic twist of supersymmetric Yang–Mills theory on $\mathbb{R}^2\times\Sigma\times C$. Here $\Sigma$ is a real surface and $C$ is a complex curve. An $\Omega$-deformation acts on $\mathbb R^2$. Localization yields four-dimensional Chern–Simons theory on $\Sigma\times C$.

Equation (4.1) defines a partial connection. Equations (4.3)–(4.4) give the localized action and parameter identification. There is no Theorem 4.1 in this source. [Section 4, printed p. 32](https://arxiv.org/pdf/1810.01970v3#page=33), [printed p. 33](https://arxiv.org/pdf/1810.01970v3#page=34).

Section 5.3, printed pp. 42–45, invokes Etingof–Varchenko perturbative uniqueness for finite-dimensional dynamical $R$-matrices. It permits transformations and corrections to the elliptic parameter $\tau$. This result supplies no positive-radius estimate for the full 5d Batalin–Vilkovisky (BV) observable algebra. [Section 5.3, printed p. 42](https://arxiv.org/pdf/1810.01970v3#page=43).

Costello–Gwilliam's *Factorization Algebras in Quantum Field Theory, Volume 2* was published by Cambridge University Press in 2021. Its official contents, printed p. viii, list Chapter 4 with sections 4.1–4.6. The cited section 4.10 does not exist in that edition. [Publisher contents, printed p. viii](https://assets.cambridge.org/97811071/63157/toc/9781107163157_toc.pdf).

The author draft's Theorem 8.6.0.1, printed p. 152, establishes a factorization algebra of quantum observables and its classical reduction. Writing $\mathrm{Obs}^{q}$ and $\mathrm{Obs}^{cl}$ for quantum and classical observables, its reduction statement is

\[
\mathrm{Obs}^{q}\otimes_{\mathbb C[[\hbar]]}\mathbb C
\cong \mathrm{Obs}^{cl}.
\]

The retrieved theorem supplies no compact-5d/6d identification, norm comparison, or equality of Borel constants. [Author draft, Theorem 8.6.0.1, printed p. 152](https://people.math.umass.edu/~gwilliam/factorization2.pdf).

The bibliography identifiers also require correction before reuse. [arXiv:2210.13036](https://arxiv.org/abs/2210.13036) identifies Lorenzo Balzotti's *Non-Crossing Shortest Paths are Covered with Exactly Four Forests*. [arXiv:1711.09115](https://arxiv.org/abs/1711.09115) identifies Kanbak–Moosavi-Dezfooli–Frossard's *Geometric robustness of deep networks: analysis and improvement*. Neither identifies the Costello–Gwilliam book.

## Retained target and required comparison

The target is 5d holomorphic Chern–Simons theory on $\mathbb R\times\mathbb C^2$ with a finite-dimensional complex simple gauge Lie algebra $\mathfrak g$. Retain its proposed all-orders identification with a Yangian vertex operator algebra for simply-laced $\mathfrak g$. Retain positive-radius convergence in the perturbative parameter $\hbar$ as a separate analytic target. The proposed non-simply-laced twisted-Yangian extension also requires its own source theorem and hypotheses.

Resolve these obligations before using the retired assertion as a proved input:

1. Identify the exact primary theorem for the stated 5d theory, gauge algebra, observable construction, and Yangian vertex operator algebra.
2. Specify the function spaces, norms, propagator scales, renormalization choices, and normalization of $\hbar$.
3. Prove estimates for the summed perturbative coefficients in those spaces. Establish the growth bounds needed for the claimed convergence or summability.
4. Construct the compact-5d/direct-6d comparison on the specified geometries and completed observable spaces. Establish quantitative estimates for the comparison and inverse.
5. Define the Borel constants being compared. Prove the norm compatibility needed for the stated equality.

Formal equivalence alone supplies no convergence estimate. For example, the formal unit $u(\hbar)=\sum_{n\geq0}n!\hbar^n$ defines an invertible algebra map $x\mapsto u(\hbar)x$ on $\mathbb C[x][[\hbar]]$. Its image of $x$ has zero convergence radius. Any use of formality to transfer convergence therefore requires additional analytic estimates.

## Retrieval limits

The Costello–Yagi PDF text was retrieved from arXiv. The publisher contents and author-draft theorem were retrieved as indexed primary-document text. Direct opens of those two book PDFs failed. No full-volume negative search for Borel estimates was completed. The findings concern the cited section and identified theorem, not every possible comparison theorem.
