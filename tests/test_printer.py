from library.printer import shelf_label


def test_shelf_label_for_a_known_book():
    assert shelf_label("Dune") == "Dune | Frank Herbert | 1965"


def test_shelf_label_for_an_unknown_book():
    assert shelf_label("Nothing Here") == "not on the shelves"
