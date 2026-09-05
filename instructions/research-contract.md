# Research and writing contract

Read for proof, computation, manuscript, or cross-volume work.

## Writing standard: Chriss–Ginzburg north star

Manuscript prose IS mathematics, not a description of mathematics. Seven combined voices: Witten, Etingof, Polyakov, Dirac, Feynman, Costello, Gaiotto. Russian elite school. Every statement inevitable.

`MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md` is binding. Forbidden patterns to scan-and-cut after every draft: meta-narration (*we now turn to*, *having established*, *in what follows*); bookkeeping (*Theorem A* labels embedded in body; status tables in theorem bodies); catalogue IDs (*Wave $N$*, *AP-CY$n$*, *HZ-$n$*, *DNA strand*, *MP$n$*); branding (*magic identity*, *inner music*, *X spine*, *matrix microscope*, *platonic ideal* in prose); hedging (*perhaps*, *notably*, *crucially*, *remarkably*, *clearly* used to skip a proof step); negative framing (*must not*, *would conflate*, *is wrong*, *fails to*); approximation language for exact identifications (*is closely related to*, *corresponds to*, *is the analogue of* — use $=$ or $\simeq$ when the identification is proved); CS jargon (*certificate*, *pipeline*, *API*, *spec*); passive avoidance (*it can be shown*, *it is decided*); evocative metaphor.

Define before use. Motivate before introduce. Concrete example before abstract machine. The reader is serious and adult.

The mathematics earns the equals sign. Two objects that are the same: $X = Y$ with the morphism implementing the identification stated. Not *$X$ is closely related to $Y$*. Courage, after Drinfeld and Polyakov and Nekrasov.

## Research-grade discipline — `INVARIANTS.md §IV` and §XI made actionable

1. **Every load-bearing claim carries an epistemic status.** *Proved / conjectured / expected / heuristic / computed / folklore.* Conditional theorems carry the conditions inline, not in a footnote.
2. **Worked case before general statement.** CY$_3$ before CY$_d$. Abelian Yangian on K3 before elliptic on $K3 \times E$. The 8-row Gritsenko–Cléry catalogue before the universal $\kappa_{\mathrm{BKM}}$ identity.
3. **Named attribution beats passive voice.** *By Maulik–Okounkov (2012)*, *by Nekrasov–Okounkov (2003)*, *by Costello (2013)*. Year + page where the claim is load-bearing.
4. **No "obviously".** $E_d$-chiral vs $E_1$-chiral distinctions, Drinfeld-centre identifications, explicit framings are load-bearing — never hand-wave.
5. **Physical intuition and formal rigor coexist.** 6d hCS / M-theory pictures and their formal counterparts are both first-class.
6. **Honest subtlety.** *This is subtle* + dissection beats *somewhat delicate*. Pattern 273 discipline ($\Phi$-as-functor vs object-level correspondence) is a recurring subtlety — spell it out.
7. **Healing over downgrade.** When an attack finds a broken proof: fix the proof, statement, or construction. Sharpen definitions, add the missing lemma, supply the worked example, mechanize the step, or state the exact obstruction and its repair route. Do not delete the theorem. Do not demote to motivation. Do not move to an appendix and call the manuscript repaired. Do not change a status label without healing the underlying proof. Conjecture / expected / heuristic labels are temporary honest-status markers, not closures (`INVARIANTS.md §XI`).
8. **Three-axis scope check.** Before inscribing any theorem, scope-check: what level, what chart, what ambient. A statement underscoped on any axis is a defect.

## Proof-obligation discipline

- **Proved** → complete argument in this tree or cited reference (page + theorem + year).
- **Conjecture / expected** → named evidence: worked case, cohomological computation, physical heuristic.
- **Heuristic** → physics argument named (BCOV, bootstrap, SUSY localization, anomaly matching) and rigor level called out.
- **Computed** → `compute/` or `notes/` entry; cite file + line. Pattern 273: functorial-level vs chain-level reading is always labeled.


## Verification and bounded investigation

State the exact theorem, hypotheses, (level, chart, ambient) coordinates, convention, and evidence before changing a mathematical claim.
Use direct computation, current TeX in context, independent tests, and primary literature to resolve differences.
A computation requires its own correctness and normalization checks. Neither code nor prose wins by default.
Preserve the three independent verification paths for load-bearing numerical claims and the HZ-3-11 protocol for ProvedHere.
Copied tables or tests consuming the same derivation are not independent paths.
For executable oracles, use at least two independent paths and three for load-bearing values.
Never update expected values solely from engine output.

After a material repair, attack applicable failure modes: signs, conventions, ambient category, missing hypotheses, functoriality, equivalence, numerical constants, and scope.
Repeat when new evidence changes the argument. Completion depends on resolved obligations and relevant verification, not pass counts or subjective scores.
Do not delete, demote, or quietly weaken a theorem to claim that its requested repair is complete.
A bounded investigation may finish with a precisely unresolved obligation, failed routes, evidence, and the next discriminating step.
Such a handoff is not completion of a separately requested proof. Preserve the original theorem target.
Stop dependent changes when authority or a material requirement needs a user decision. Continue independent work already authorized.
Investigate compute/prose, cross-volume, and 8-row/10-row catalogue differences before escalating an unresolved conflict.
Check the compatible-dual-readings table before changing either side. Never silently reassign a catalogue row.

## Scope and collaboration

Instruction maintenance, reference repairs, and status checks are valid deliverables when requested. They do not establish new mathematics.
For mathematical work, prioritize proved results, explicit constructions, exact computations, and precise scope repairs.
Keep unrelated mathematical axes unchanged. Preserve substantive content through semantic integration.
Read the full target chapter for structural work, and the affected claim with dependencies for a local edit.
Read inventory or swarm synthesis before individual historical reports when those records are relevant.
Use the strongest available research model and maximum supported reasoning for difficult proofs, subject to host and user limits.
Use explicit user or host budgets. Checkpoint between substantial proof obligations without dropping equations or hypotheses.

Delegate when authorized and useful. Partition files or independent proof obligations, and name one integration owner.
Workers return evidence, source anchors, formulas, changes, checks, and unresolved questions. They do not vote on truth.
Pass the manuscript-content rule and the ban on mannered prose to every writing agent.
Preserve concurrent work. Only write to assigned repositories and worktrees.
For cross-volume changes, compare conventions and return exact downstream obligations to the owner of unassigned repositories.
Keep progress reports outside manuscript sources. Do not expose private scratch reasoning.

## Operational details

Use the existing AP-CY catalogue types and canonical-values registry. Do not create parallel numbering.
Check the local writing standard, define-before-use, term-coining rules, and honest claim macros on changed prose.
Installed `scripts/hooks/beilinson-gate.sh` provides AP-CY and cache checks. Do not bypass an installed hook.
The tracked script is the source for local hook installation. Check host hook configuration before assuming it ran.
Preserve the shared LaTeX template. Use deterministic tooling for labels, citations, and numbering.
For reconciliation, read both sides and retain substantive proof content. Escalate only the unresolved semantic choice.
No model attribution belongs in commits or manuscripts. Model instructions in instruction files are operational guidance, not attribution.
