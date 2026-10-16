from library.desk import reader_card, shelf_label


def test_shelf_label_for_a_known_book():
    assert shelf_label("Dune") == "Dune | Frank Herbert | 1965"


def test_shelf_label_for_an_unknown_book():
    assert shelf_label("Nothing Here") == "not on the shelves"


def test_reader_card_shows_name_and_count():
    card = reader_card("Ada Lovelace", 2)
    assert "Ada Lovelace" in card and "2 books out" in card
