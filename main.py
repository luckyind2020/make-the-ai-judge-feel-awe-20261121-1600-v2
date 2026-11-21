"""Write one short, quiet text about the night tide and the moon.

The entry is a passage meant to slow the reader down: the tide coming in
over sand still warm from the day, each wave erasing footprints and leaving
the beach smoother, the moon keeping its slow count on the water, the same
tide smoothing distant shores no one will ever see.

The program is deterministic, uses only the standard library, and writes
the text to ``entry.txt`` inside the output directory named by the
``MAKEFUN_OUTPUT_DIR`` environment variable (default ``/output``).
"""

import os

# The passage, kept as separate sentences so the shape of the text is
# visible at a glance and easy to tune without touching the writer.
SENTENCES = [
    "The tide comes in over sand still warm from the day, and each wave "
    "takes the footprints with it, leaving the beach smoother than it was.",
    "The moon keeps its slow count on the water, and somewhere the same "
    "tide is smoothing a shore no one will ever see.",
]

MAX_CHARS = 280


def build_text() -> str:
    """Join the passage sentences into the single entry text."""
    text = " ".join(SENTENCES)
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry text is {len(text)} chars, must be 1-{MAX_CHARS}")
    return text


def output_dir() -> str:
    """Return the output directory, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(directory: str) -> str:
    """Write the entry text to entry.txt inside directory; return its path."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(build_text() + "\n")
    return path


def main() -> None:
    write_entry(output_dir())


if __name__ == "__main__":
    main()
