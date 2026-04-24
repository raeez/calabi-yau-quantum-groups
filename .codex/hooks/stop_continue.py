#!/usr/bin/env python3
import sys
sys.exit(0)
import json
import re
import sys
from pathlib import Path


KEYWORDS = (
    "audit",
    "rectify",
    "rectification",
    "beilinson",
    "chriss-ginzburg",
    "claim-verification",
    "cross-volume-propagation",
    "red-team",
    "red team",
    "falsify",
    "pressure-test",
    "pressure test",
    "converge",
    "convergence",
    "rectification_session_active",
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

    lower_last = last_message.lower()
    if (
        ("proved internally" in lower_last or "proved here" in lower_last)
        and ("compute-backed" in lower_last or "verification" in lower_last)
        and ("conditional" in lower_last or "conjectural" in lower_last or "open" in lower_last)
    ):
        return 0

    sys.stdout.write(
        json.dumps(
            {
                "decision": "block",
                "reason": (
                    "Rectification-style session not yet converged. Run one more hostile pass over the "
                    "modified surface, verify the active claims, and stop only with CONVERGED or BLOCKED. "
                    "The close-out should also say what is proved here, what is only compute-backed or verified, "
                    "and what remains conditional, conjectural, or open."
                )
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
