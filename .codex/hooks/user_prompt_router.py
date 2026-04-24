#!/usr/bin/env python3
import sys
sys.exit(0)

import json
import re
import sys


def main() -> None:
    data = json.load(sys.stdin)
    prompt = (data.get("prompt") or "").strip()
    lower = prompt.lower()
    notes = []

    rectification = re.search(
        r"\b(audit|rectif|fortif|beilinson|red[- ]team|pressure[- ]test|repair|tighten|converge)\b",
        lower,
    )
    if rectification:
        notes.append("RECTIFICATION_SESSION_ACTIVE")
        notes.append(
            "Prefer `vol3-beilinson-loop`. Read the live surface before editing, fix in dependency order, "
            "and stop only with CONVERGED or BLOCKED."
        )

    if re.search(r"\b(chriss|ginzburg|chapter|architectur|platonic rewrite|inevitable)\b", lower):
        notes.append(
            "For chapter-scale structural work, prefer `vol3-chriss-ginzburg-rectification`."
        )

    if re.search(
        r"\b(verify|formula|coefficient|invariant|kappa|r-matrix|rmatrix|bar complex|cobar|mf\(|shadow class|check)\b",
        lower,
    ):
        notes.append(
            "Prefer `vol3-pre-edit-verification` plus `vol3-claim-verification`. Use at least three independent paths when feasible."
        )

    if re.search(r"\b(propagat|cross-volume|cross[ -]?volume|all files|other volume)\b", lower):
        notes.append(
            "Prefer `vol3-cross-volume-propagation`. Search Volumes I, II, and III before declaring success."
        )

    if re.search(r"\b(make|pdflatex|latex|build|pytest|test|warning|log)\b", lower):
        notes.append(
            "Prefer `vol3-build-surface`. Stabilize the build surface before trusting warning counts."
        )

    if re.search(r"\b(engine|oracle|compute engine|scaffold|compute|test surface|hardcoded)\b", lower):
        notes.append(
            "Prefer `vol3-compute-engine`. Record source and normalization, and keep engine and tests independently justified."
        )

    if re.search(r"\b(frontier|research|programme|program|new theorem|conjecture|architecture|synthesis)\b", lower):
        notes.append(
            "Prefer `vol3-frontier-research`. Separate proved core, conditional bridge, conjectural extension, and heuristic picture."
        )

    if re.search(r"\b(swarm|sub-agent|subagent|parallel agent|delegate|delegation|rectify-all)\b", lower):
        notes.append(
            "Use `vol3-swarm-orchestration` only if the user explicitly authorizes delegation; otherwise run the same workflow locally."
        )

    if not notes:
        return

    payload = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": "\n".join(notes),
        }
    }
    json.dump(payload, sys.stdout)


if __name__ == "__main__":
    main()
