"""One Sentence for a Traveler from 1800 — make.fun entry.

Writes one sentence (at most 200 characters) explaining the modern
internet to a time traveler from the year 1800, built only from things
a person of that year already knows: libraries, letters, wires, tea.
The sentence is written to entry.txt in the output directory.
"""

import os

TEXT = (
    "Imagine every library on Earth joined by wires thinner than thread, "
    "so that any book, letter, or picture may be copied and sent to any "
    "house in the world before your tea goes cold."
)


MAX_CHARS = 200


def validated_bytes() -> bytes:
    """Return TEXT as UTF-8 bytes after checking the gate's rules.

    The gate accepts UTF-8 text of 1 to 200 characters that is not only
    whitespace, and the bounty asks for a single sentence: exactly one
    line, ending in its one full stop, with no trailing newline added.
    Fail loudly here rather than write an entry the gate would refuse.
    """
    if "\n" in TEXT or "\r" in TEXT:
        raise SystemExit("entry text must be a single line")
    if not TEXT.strip():
        raise SystemExit("entry text must not be blank")
    if len(TEXT) > MAX_CHARS:
        raise SystemExit(f"entry text is {len(TEXT)} characters, over {MAX_CHARS}")
    if not TEXT.endswith(".") or TEXT.count(".") != 1:
        raise SystemExit("entry text must be one sentence ending in a full stop")
    return TEXT.encode("utf-8")


def main() -> None:
    data = validated_bytes()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(data)
    with open(path, "rb") as fh:
        if fh.read() != data:
            raise SystemExit("written entry does not match the validated bytes")


if __name__ == "__main__":
    main()
