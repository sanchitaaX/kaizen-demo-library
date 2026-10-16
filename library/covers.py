"""Cover images of the books, served from library/covers/ by file name."""

import os

COVERS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "covers")


def read_cover(name):
    full_path = os.path.abspath(os.path.join(COVERS_DIR, name))
    if not full_path.startswith(os.path.abspath(COVERS_DIR) + os.sep):
        raise ValueError("Invalid cover path")
    with open(full_path, "rb") as fh:
        return fh.read()


def list_covers():
    return sorted(os.listdir(COVERS_DIR))
