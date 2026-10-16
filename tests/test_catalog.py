from library.catalog import books_by_author, connect


def test_books_by_author_oldest_first():
    conn = connect()
    assert books_by_author(conn, "Frank Herbert") == [("Dune", 1965), ("Children of Dune", 1976)]


def test_unknown_author_has_no_books():
    assert books_by_author(connect(), "Nobody") == []
