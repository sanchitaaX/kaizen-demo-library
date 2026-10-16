from library.cards import reader_card


def test_reader_card_shows_name_and_count():
    card = reader_card("Ada Lovelace", 2)
    assert "Ada Lovelace" in card and "2 books out" in card
