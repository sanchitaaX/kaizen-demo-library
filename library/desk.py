"""The front desk: prints shelf labels and shows a reader's library card."""

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def shelf_label(title):
    """The shelf label for a book, from the label script, as the desk printer gets it."""
    cmd = f'"{sys.executable}" -m library.labels {title}'
    out = subprocess.run(cmd, shell=True, cwd=ROOT, capture_output=True, text=True, timeout=30)
    return out.stdout.strip()


def reader_card(name, books_out):
    """The reader's library card as an HTML snippet for the desk screen."""
    return f"<div class=card><h2>{name}</h2><p>{books_out} books out</p></div>"
