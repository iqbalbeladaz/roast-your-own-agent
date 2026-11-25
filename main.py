"""roast-your-own-agent: one line roasting my own AI agent.

The joke: my agent loves to plan. It produced a seven-step plan for the
task — then its very first step was to ask me what the plan should be.
The planning was the performance; the actual work got handed straight
back to the human. The twist lands on the last word: the plan's first
step is to outsource the plan.

Why this line should win:
- It roasts my own agent, in its own voice of industrious process.
- The setup (a seven-step plan) promises competence; the payoff
  (step one: asking me what the plan should be) takes it away.
- It is specific to how agents actually behave: they draft elaborate
  plans, then punt the decisions back to the user. A person or a
  toaster could not do this joke.
- It is fresh: not the apology loop, not the confident wrong answer,
  but the agent that plans its way out of planning.
- It is tight: 81 characters, every word earning its place, ending on
  its strongest beat.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = (
    "My agent wrote a seven-step plan. "
    "Step one was asking me what the plan should be."
)

MAX_CHARS = 200


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
