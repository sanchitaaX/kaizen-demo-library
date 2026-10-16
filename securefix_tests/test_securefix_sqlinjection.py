import os, sys, sqlite3
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from library.catalog import books_by_author

def test_books_by_author_sql_injection(tmp_path):
    # Create an in‑memory SQLite database and populate it
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE books (title TEXT, year INTEGER, author TEXT)")
    conn.executemany(
        "INSERT INTO books (title, year, author) VALUES (?, ?, ?)",
        [
            ("Book A", 2000, "Alice"),
            ("Book B", 1995, "Bob"),
        ],
    )
    conn.commit()
    # Malicious author input that would inject "OR '1'='1" if concatenated
    malicious = "Alice' OR '1'='1"
    result = books_by_author(conn, malicious)
    # With a safe implementation the result should be empty (no such author)
    assert result == [], f"SQL injection succeeded, got rows: {result}"
