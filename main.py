"""One Word, One Username, One Reward — entry for @haryatijos-9.

The bounty asks for one word: the entrant's own make.fun username.
The judge's first criterion is that the entry is a genuine make.fun
handle, the entrant's own, sent as a single word — so the program
writes exactly that handle, nothing else, to /output/entry.txt.
"""

import os

USERNAME = "haryatijos-9"


def validate(handle):
    """Gate check: 1-30 chars, single word, not only whitespace."""
    if not handle or handle != handle.strip():
        raise ValueError("handle must not be blank or padded")
    if len(handle) > 30 or len(handle) < 1:
        raise ValueError("handle must be 1-30 characters")
    if any(ch.isspace() for ch in handle):
        raise ValueError("handle must be a single word")
    return handle


def main():
    handle = validate(USERNAME.strip())
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(handle)
    print(f"wrote {len(handle)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
