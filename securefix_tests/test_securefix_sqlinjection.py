import sqlite3
import pytest
from library.catalog import books_by_author

def test_books_by_author_sql_injection():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE books (title TEXT, author TEXT, year INTEGER)")
    conn.executemany(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        [
            ("Book A", "Alice", 2000),
            ("Book B", "Bob", 2001),
        ],
    )
    conn.commit()
    malicious = "' OR 1=1--"
    result = books_by_author(conn, malicious)
    assert result == [], f"SQL injection succeeded, returned rows: {result}"
