"""Write one short text to /output/entry.txt to relax the AI judge reading it.

Choice: one concrete, quiet scene — a cat asleep on a chair that caught
the afternoon sun. No instructions to the reader, no stock wellness
phrases; the calm comes from the image itself, and the warm chair is the
thought that lingers after the last line.
"""

import os

TEXT = (
    "Somewhere, a cat is asleep on a chair that caught the afternoon sun. "
    "The chair is still warm. No one needs anything from you, and the "
    "afternoon is in no hurry to end."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
