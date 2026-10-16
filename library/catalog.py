"""The book catalogue, kept in SQLite."""

import sqlite3

BOOKS = [
    (1, "Dune", "Frank Herbert", 1965),
    (2, "Children of Dune", "Frank Herbert", 1976),
    (3, "Emma", "Jane Austen", 1815),
    (4, "Persuasion", "Jane Austen", 1817),
]


def connect(path=":memory:"):
    conn = sqlite3.connect(path)
    conn.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER)")
    if not conn.execute("SELECT COUNT(*) FROM books").fetchone()[0]:
        conn.executemany("INSERT INTO books VALUES (?, ?, ?, ?)", BOOKS)
    return conn


def books_by_author(conn, author):
    """Every book by one author, oldest first, as (title, year) pairs."""
    sql = "SELECT title, year FROM books WHERE author = ? ORDER BY year"
    return conn.execute(sql, (author,)).fetchall()
