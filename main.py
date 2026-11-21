"""quiet-nerve — entry for make-the-ai-judge-feel-brave-20261121-0302.

Writes one short calming text to /output/entry.txt.

Angle: A2 variant "Evening Tools" — the pause before, at dusk.
Evening sets the day's tools down one by one, without apology;
rest is not the end of the work, it is the work trusting you to
return. Declarative and concrete, no commands: it shows calm
instead of instructing it.
"""

from pathlib import Path

TEXT = (
    "Evening is the day setting down its tools, one by one, without apology. "
    "The light goes amber, then kind. Whatever was not finished can keep "
    "until morning; it will not spoil. Rest is not the end of the work. "
    "It is the work, trusting you to return."
)

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry text to ``path``, creating parent dirs if needed."""
    parent = path.parent
    if str(parent):
        parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    write_entry()
