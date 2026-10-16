"""The desk printer: shelf labels come from the label script, python -m library.labels <title>."""

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def shelf_label(title):
    """The shelf label for a book, as the desk printer gets it."""
    cmd = f'"{sys.executable}" -m library.labels {title}'
    out = subprocess.run(cmd, shell=True, cwd=ROOT, capture_output=True, text=True, timeout=30)
    return out.stdout.strip()
