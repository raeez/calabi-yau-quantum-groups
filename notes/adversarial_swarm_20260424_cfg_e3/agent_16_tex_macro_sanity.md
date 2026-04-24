# Agent 16: TeX macro and scope sanity audit

Date: 2026-04-24.

Scope: `chapters/theory/cy3_chain_level_bridge.tex`,
`chapters/theory/cy_to_chiral.tex`, `main.tex`, and
`notes/adversarial_swarm_20260424_cfg_e3/SYNTHESIS.md`.

No full build was run. The audit used narrow `rg`, `nl`, and `perl`
checks only.

## Verdict

Fatal/sanity-blocking issues found:

1. `chapters/theory/cy3_chain_level_bridge.tex:444`,
   `chapters/theory/cy3_chain_level_bridge.tex:447`
   use `\Br` and `\Sur`, but neither macro is defined in `main.tex` or
   in the compiled chapter tree.
   Recommended patch:
   ```tex
   $\cK=\mathrm{Br}\otimes\mathrm{Sur}$ acting on $\HH^\bullet(\cC)$
   ...
   $\mathrm{Br}\hookrightarrow C_\bullet(\Conf_2;\Q)$
   ```
   Alternative: add preamble macros
   `\providecommand{\Br}{\mathrm{Br}}` and
   `\providecommand{\Sur}{\mathrm{Sur}}`.

2. `chapters/theory/cy_to_chiral.tex:413` has two undefined refs:
   `rem:motivic-grt1-torsor-k3` and `thm:super-grt-quantisation`.
   Likely intended anchors:
   `chapters/theory/cy_categories.tex:917`
   (`rem:cycat-ce-motivic-fundamental-group`) and
   `chapters/theory/quantum_groups_foundations.tex:3313`
   (`thm:qgf-grt1-bkm-transitivity`), or the section anchor
   `sec:qgf-grt1-bkm` at line 3221 if theorem specificity is not intended.

Nonfatal but should be patched:

1. `chapters/theory/cy_to_chiral.tex:164` reverses the composition in the
   section title:
   `\PhiFA_d \circ \SpCh_{\Sigma_{d-1}, C}`.  The manuscript formula
   elsewhere is `\SpCh_{\Sigma_{d-1}, C} \circ \PhiFA_d`.

2. `chapters/theory/cy_to_chiral.tex:171-176` and
   `chapters/theory/cy_to_chiral.tex:251-257` use display grammar of the
   form
   ```tex
   \Phi_d^{(\Sigma_{d-1}, C)} \;=\;
   \CY_d\text{-}\Cat
   \xrightarrow{\;\PhiFA_d\;} ...
   ```
   This compiles, but semantically equates the assignment with the source
   category.  Recommended patch:
   ```tex
   \Phi_d^{(\Sigma_{d-1}, C)} \colon
   \CY_d\text{-}\Cat
   \xrightarrow{\;\PhiFA_d\;}
   \EdHolFA(X)
   \xrightarrow{\;\SpCh_{\Sigma_{d-1}, C}\;}
   \EnHolFA(C).
   ```

3. `chapters/theory/cy_to_chiral.tex:682` duplicates
   `eq:5d-hcs-yangian-voa-allorders`, already present at
   `chapters/theory/gluing/sec_5_factorization.tex:784`.  There are no
   current refs to that label, so rename one side before references are
   added.

4. `chapters/theory/cy_to_chiral.tex:428`,
   `chapters/theory/cy_to_chiral.tex:606`, and
   `chapters/theory/cy_to_chiral.tex:607` use `\P^n`.  In LaTeX `\P` is
   the paragraph symbol, not projective space.  Use `\bP^n` or
   `\mathbb{P}^n`.

## Checks Passed

- `\Obs`, `\cC`, `\EdHolFA`, `\GRT`, and `\Hall` are defined in
  `main.tex`.
- `\rightsquigarrow` is supplied by `amssymb`, loaded in `main.tex`.
- `\mathfrak l_{\cC}` is not an undefined macro; it is `\mathfrak`
  applied to the literal letter `l`.
- Begin/end balance check on the two target `.tex` files returned no
  unmatched environments.
- Citation check against `bibliography/references.tex` for the two target
  `.tex` files returned no missing `\cite{...}` keys.
- `SYNTHESIS.md` is ASCII-compatible; the non-ASCII scan returned no
  lines.

## Commands Run

```bash
git status --short
wc -l chapters/theory/cy3_chain_level_bridge.tex chapters/theory/cy_to_chiral.tex main.tex notes/adversarial_swarm_20260424_cfg_e3/SYNTHESIS.md
rg -n '\\(Obs|cC|EdHolFA|GRT|Hall|rightsquigarrow|label|ref|cref|Cref|input|include|newcommand|providecommand|DeclareMathOperator)' chapters/theory/cy3_chain_level_bridge.tex chapters/theory/cy_to_chiral.tex main.tex notes/adversarial_swarm_20260424_cfg_e3/SYNTHESIS.md
rg -n '\\(newcommand|providecommand|DeclareMathOperator).*\\(Br|Sur|FAct|Hol|CE|FactCosh|Form|Graphs|Ger|Ch|Conf|Aut|Einf|Fact|FactAlg)' main.tex chapters/**/*.tex
rg -n '\\Br\\b|\\Sur\\b|\\P\\b|eq:5d-hcs-yangian-voa-allorders' chapters main.tex appendices bibliography
perl -MFile::Find -e '<scan target refs against labels under chapters appendices bibliography notes main.tex with no_chdir>'
perl -MFile::Find -e '<scan duplicate labels under chapters appendices bibliography main.tex with no_chdir>'
perl -ne 'while(/\\(begin|end)\{([^}]+)\}/g){...}' chapters/theory/cy3_chain_level_bridge.tex chapters/theory/cy_to_chiral.tex
perl -ne 'while(/\\cite\{([^}]+)\}/g){...}' chapters/theory/cy3_chain_level_bridge.tex chapters/theory/cy_to_chiral.tex
perl -ne 'if(/[^\x00-\x7F]/){...}' notes/adversarial_swarm_20260424_cfg_e3/SYNTHESIS.md
```

## Files Changed

Only this report was created:

- `notes/adversarial_swarm_20260424_cfg_e3/agent_16_tex_macro_sanity.md`
