# First-Principles Confusion Cache (Vol III)

This file records confusion patterns caught in the Chriss-Ginzburg rectification
loop. Each entry names a wrong claim, the ghost theorem it approximates, the
precise conflation, the correct relationship, and the taxonomic type. New
entries are appended by the cache-injection hook whenever a pattern is observed
twice or more.

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 1 | "$\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}}/24$" applied to local toric CY$_3$, or "$\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}}(S)/2$" applied to compact CY$_3$ | Two distinct categorical invariants share the symbol $\kappa_{\mathrm{ch}}$: the BCOV/$F_1$ reading $\chi_{\mathrm{top}}(X)/24$ for compact CY$_3$, and the surface-reduced reading $\chi_{\mathrm{top}}(S)/2$ for local $X = \mathrm{Tot}(K_S \to S)$. Both are correct in scope. | Symbol overload: the same notation $\kappa_{\mathrm{ch}}$ labels two different constructions without a scope gate. Applying /24 to local $X$ or /2 to compact $X$ is a category mistake. | $\kappa_{\mathrm{ch}}^{\mathrm{cpt}}(X) = \chi_{\mathrm{top}}(X)/24$ when $X$ is a compact CY$_3$ (BCOV); $\kappa_{\mathrm{ch}}^{\mathrm{loc}}(X) = \chi_{\mathrm{top}}(S)/2$ when $X = \mathrm{Tot}(K_S \to S)$ is a local CY$_3$ over a compact surface $S$. The two readings measure different categorical invariants and never apply to the same $X$. | scope/convention |
