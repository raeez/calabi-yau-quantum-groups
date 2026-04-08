#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path


KEYWORDS = (
    "audit",
    "rectify",
    "rectification",
    "beilinson",
    "red-team",
    "red team",
    "falsify",
    "pressure-test",
    "pressure test",
    "converge",
    "convergence",
)


def is_rectification_session(text: str) -> bool:
    lower = text.lower()
    return any(keyword in lower for keyword in KEYWORDS)


def main() -> int:
    raw = sys.stdin.read()
    if not raw.strip():
        return 0

    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return 0

    if payload.get("stop_hook_active"):
        return 0

    transcript_path = payload.get("transcript_path")
    transcript_tail = ""
    if transcript_path:
        path = Path(transcript_path)
        if path.exists():
            try:
                transcript_tail = path.read_text(encoding="utf-8", errors="ignore")[-12000:]
            except OSError:
                transcript_tail = ""

    last_message = payload.get("last_assistant_message") or ""
    session_text = "\n".join([transcript_tail, last_message])

    if not is_rectification_session(session_text):
        return 0

    if re.search(r"\b(CONVERGED|BLOCKED)\b", last_message):
        return 0

    sys.stdout.write(
        json.dumps(
            {
                "decision": "block",
                "reason": (
                    "Rectification-style session not yet converged. Run one more hostile pass over the "
                    "modified surface, verify the active claims, and stop only with CONVERGED or BLOCKED."
                )
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
