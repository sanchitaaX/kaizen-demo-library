# Little Library

A small front-desk toolkit for a neighbourhood library, written with the Python standard library only.

- `library/catalog.py` keeps the book catalogue in SQLite and lists the books by one author.
- `library/fines.py` works out late fees with the fee rule the desk sets (for example `days * 0.25`).
- `library/basket.py` remembers a reader's basket between visits in a cookie.
- `library/covers.py` serves cover images from `library/covers/` by file name.

## Run the tests

No packages to install beyond pytest:

```
python -m pytest -q
```
