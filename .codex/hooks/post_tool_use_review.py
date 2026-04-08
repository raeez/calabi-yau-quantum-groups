#!/usr/bin/env python3
import json
import sys


def response_to_text(value) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        try:
            return json.dumps(value, ensure_ascii=True)
        except TypeError:
            return str(value)
    return str(value)


def main() -> int:
    raw = sys.stdin.read()
    if not raw.strip():
        return 0

    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return 0

    tool_input = payload.get("tool_input", {})
    command = tool_input.get("command", "") if isinstance(tool_input, dict) else ""
    lower = command.lower()

    response = response_to_text(payload.get("tool_response", ""))
    response_lower = response.lower()

    watched = any(token in lower for token in ["make", "pytest", "pdflatex", "latexmk"])
    failed = any(
        token in response_lower
        for token in [
            "traceback",
            "! latex error",
            "undefined control sequence",
            "fatal error",
            "failed",
            "error:",
            "assertionerror",
        ]
    )

    if watched and failed:
        sys.stdout.write(
            json.dumps(
                {
                    "decision": "block",
                    "reason": (
                        "The last build or test command appears to have failed. "
                        "Inspect the output, fix the issue, or state precisely why the task is blocked."
                    ),
                    "hookSpecificOutput": {
                        "hookEventName": "PostToolUse",
                        "additionalContext": (
                            "Do not treat the modified surface as verified while build/test output shows errors."
                        ),
                    },
                }
            )
        )
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
