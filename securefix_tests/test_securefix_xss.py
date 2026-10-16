import library.cards

def test_reader_card_xss():
    malicious = "<script>alert(1)</script>"
    output = library.cards.reader_card(malicious, 3)
    assert "<script>" not in output, "Raw script tag should not appear"
    assert "&lt;script&gt;" in output, "Escaped script tag should appear"
    assert "alert(1)" in output, "Script content should be preserved"
    normal = library.cards.reader_card("Alice", 5)
    assert normal == "<div class=card><h2>Alice</h2><p>5 books out</p></div>", "Normal output should be unchanged"