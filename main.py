"""Cat joke entry: a one-line joke, written to /output/entry.txt."""

import os

LINE = "My cat keeps bringing me dead mice because she thinks I'm a terrible hunter. She's right: I buy my food pre-killed too."
# The turn: the cat's gift is a performance review, and the owner fails it the same way.

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    os.makedirs(OUT_DIR, exist_ok=True)
    fd = os.open(OUT_PATH, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, LINE.encode("utf-8"))
    finally:
        os.close(fd)


if __name__ == "__main__":
    main()
