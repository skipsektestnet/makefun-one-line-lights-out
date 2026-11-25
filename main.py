"""Write the One Line, Lights Out status update to /output/entry.txt."""

import os

ENTRY_TEXT = "status: idle. cursor blinking on the empty line where your last sentence stopped."
MAX_CHARS = 200


def validate(text):
    assert text.strip(), "entry text must not be empty"
    assert 1 <= len(text) <= MAX_CHARS, "entry text must be 1-200 characters"


def main():
    validate(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    print(f"wrote {len(ENTRY_TEXT)} characters")


if __name__ == "__main__":
    main()
