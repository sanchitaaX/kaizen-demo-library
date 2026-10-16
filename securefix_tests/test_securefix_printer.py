import pytest
from library.printer import shelf_label

def test_command_injection(tmp_path):
    marker = "SFX_MARK_7731"
    # Malicious title that attempts to run a second command
    title = f"normal & echo {marker}"
    output = shelf_label(title)
    lines = [line.strip() for line in str(output).splitlines()]
    assert marker not in lines, f"a second command ran: {output!r}"
