#!/usr/bin/env python3
import sys
sys.exit(0)

import json
import sys


def main() -> None:
    payload = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": (
                "Vol III repo mode: mathematical truth lives on the live surface "
                "(`main.tex`, active inputs, dirty diff, build/test logs, compute/tests). "
                "Use Codex skills under `.agents/skills` for audit, rectification, verification, "
                "propagation, build triage, frontier work, compute-engine work, swarm orchestration, "
                "and pre-edit verification. Use hooks as guardrails, not as substitutes for proof."
            ),
        }
    }
    json.dump(payload, sys.stdout)


if __name__ == "__main__":
    main()
