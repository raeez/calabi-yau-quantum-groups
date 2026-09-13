---
name: vol3-cross-volume-propagation
description: Use when changing formulas, definitions, theorem statuses, or terminology that may recur across Volumes I, II, and III. Trigger on propagate, cross-volume, grep other volume, update all occurrences, or changes involving kappa, Theta, bar/cobar, CoHA, E_1/E_2, Borcherds products, quantum groups, or center constructions.
---

# Vol III Cross-Volume Propagation

Read `AGENTS.md` first. This skill exists to prevent local fixes from creating global incoherence.

## Sweep

Search all three volumes:

- `~/calabi-yau-quantum-groups`
- `~/chiral-bar-cobar-vol2`
- `~/chiral-bar-cobar`

## Conversion discipline

Before updating a matching statement, verify whether it is actually the same claim in the same convention:

- Volume I: OPE modes
- Volume II: lambda-brackets and divided powers
- Volume III: motivic/categorical conventions

## Update rule

- Fix all genuine duplicates in the same session when feasible.
- If not feasible, leave an explicit note about what still needs propagation and why.
- Never treat verbal similarity as proof that two formulas are the same object.
