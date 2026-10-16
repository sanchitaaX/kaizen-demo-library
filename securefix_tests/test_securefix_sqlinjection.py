import os, sys, sqlite3
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from library.catalog import books_by_author

def test_books_by_author_sql_injection(tmp_path):
    # Set up in‑memory SQLite database with sample data
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE books (title TEXT, year INTEGER, author TEXT)")
    conn.executemany(
        "INSERT INTO books (title, year, author) VALUES (?, ?, ?)",
        [
            ("Book A", 2000, "Alice"),
            ("Book B", 2010, "Bob"),
        ],
    )
    conn.commit()

    # Malicious input that would return all rows if concatenated
    malicious_author = "a' OR '1'='1"
    result = books_by_author(conn, malicious_author)
    # Safe implementation should return no rows because no author matches the exact string
    assert result == [], f"SQL injection succeeded, returned rows: {result}"

    # Verify normal behaviour still works for a valid author
    normal = books_by_author(conn, "Alice")
    assert normal == [("Book A", 2000)], "Normal query did not return expected result"
