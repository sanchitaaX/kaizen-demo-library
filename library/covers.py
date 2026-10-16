"""Cover images of the books, served from library/covers/ by file name."""

import os

COVERS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "covers")


def read_cover(name):
    with open(os.path.join(COVERS_DIR, name), "rb") as fh:
        return fh.read()


def list_covers():
    return sorted(os.listdir(COVERS_DIR))
