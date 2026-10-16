import pytest
from library.printer import shelf_label

def test_shelf_label_no_command_injection():
    marker = 'SFX_MARK_7731'
    normal_title = 'TestBook'
    malicious_input = normal_title + ' & echo ' + marker
    output = shelf_label(malicious_input)
    lines = [line.strip() for line in str(output).splitlines()]
    assert marker not in lines, f"a second command ran: {output!r}"